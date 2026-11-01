import re
from typing import List, Dict, Any

class MedicalReranker:
    """
    Reranking engine for high-stakes medical & life-sciences retrieval.
    Re-scores and re-orders hybrid search candidates using:
    1. Exact medical entity match boosting (e.g. drug/device names).
    2. Term density and proximity scoring (penalizing scattered coincidental words).
    3. Structural priority (e.g. table chunks prioritized when user asks for specific attributes/requirements).
    4. Recency & version enforcement.
    """

    ENTITY_SUFFIX_PATTERN = r"(质量标准|质量要求|技术要求|检测方法|检验规程|含量测定|质量|标准|要求|指标|检查|测定)$"

    def __init__(self, entity_extractor=None):
        # Optional hook: when the caller can resolve the query's compendial entity, use that
        # as the exact-match subject. Natural-language parameter queries ("丁香 性状",
        # "纯化水的质量标准是什么") otherwise never reach the exact-entity bonus, and a
        # relevant chunk then scores below the frozen answer threshold.
        self.entity_extractor = entity_extractor

    def rerank(self, query: str, candidates: List[Dict[str, Any]], top_n: int = 3) -> List[Dict[str, Any]]:
        if not candidates:
            return []

        query_lower = query.lower()
        # Clean question prefixes to extract core entity
        core_query = re.sub(r"^(什么是|请问什么是|请问|关于|介绍一下|如何理解|简述|what is an|what is a|what is|what are|overview of)\s*", "", query_lower).strip()
        core_query = re.sub(r"[？?。!！]$", "", core_query).strip()
        core_entity = re.sub(self.ENTITY_SUFFIX_PATTERN, "", core_query).strip()
        if self.entity_extractor is not None:
            resolved_entity = self.entity_extractor(query)
            if resolved_entity:
                core_entity = str(resolved_entity).strip().lower()

        # Extract English words (>2 chars) and CJK character n-grams (>=2 chars)
        en_words = [w for w in re.findall(r"[a-z0-9_]+", query_lower) if len(w) > 2]
        cjk_chars = re.findall(r"[\u4e00-\u9fff]", query_lower)
        cjk_ngrams = []
        for i in range(len(cjk_chars) - 1):
            cjk_ngrams.append(cjk_chars[i] + cjk_chars[i+1])
        STOPWORDS = {
            "如何", "怎么", "什么", "使用", "设计", "进行", "可以", "请问", "关于", "什么是", "并且", "以及",
            "通过", "具有", "包括", "及其", "对于", "根据", "按照", "一个", "各个", "各种", "所有", "这个",
            "那个", "这些", "那些", "的", "了", "和", "是", "就", "在", "也", "与", "或", "于", "之", "为",
            "而", "及", "等", "以", "从", "到", "将", "被", "有", "无", "中", "上", "下", "来", "去", "做",
            "让", "使", "用", "技", "术", "设", "计",
            "我想", "想知", "知道", "相关", "内容", "了解", "有关", "具体", "介绍", "资料", "信息",
            "我", "想", "知", "道", "相", "关", "内", "容", "有哪些", "有什么", "请问",
            "质量", "标准", "要求", "指标", "规定", "规程", "检定", "检验", "测定", "项目", "方法", "条件", "限度",
            "the", "a", "an", "is", "are", "was", "were", "of", "and", "in", "to", "for", "with"
        }
        # Filter out trailing single-character or non-essential sub-words
        raw_words = en_words + [ng for ng in cjk_ngrams if ng not in STOPWORDS]
        query_words = [w for w in raw_words if w not in STOPWORDS]

        # Bilingual check if query asks for tabular / requirement / data lookup
        tabular_keywords = [
            "table", "requirement", "specification", "level", "spec", "comparison", "matrix",
            "表", "要求", "对比", "级别", "矩阵", "资料", "附表", "清单"
        ]
        is_tabular_query = any(w in query_lower for w in tabular_keywords)

        # Overview / Definition query detection (e.g. 什么是FDA, 介绍国家药监局, What is FDA)
        overview_keywords = ["什么是", "是什么", "介绍", "简介", "概况", "总览", "职责", "机构", "架构", "what is", "overview", "definition"]
        is_overview_query = any(k in query_lower for k in overview_keywords)

        substantive_cjk = [c for c in cjk_chars if c not in STOPWORDS]

        reranked = []
        for doc in candidates:
            content = doc.get("content", "").lower()
            content_zh = doc.get("content_zh", "").lower()
            content_en = doc.get("content_en", "").lower()
            metadata = doc.get("metadata", {})
            doc_title = metadata.get("doc_title", "").lower()
            doc_title_zh = metadata.get("doc_title_zh", "").lower()
            doc_title_en = metadata.get("doc_title_en", "").lower()
            jurisdiction = metadata.get("jurisdiction", "").lower()
            searchable_text = f"{doc_title} {doc_title_zh} {doc_title_en} {jurisdiction} {content} {content_zh} {content_en}"
            base_score = doc.get("hybrid_score", 0.0)

            # 1. Entity & Term Proximity Boost
            exact_phrase_bonus = 0.0
            if (core_query and core_query in searchable_text) or (core_entity and len(core_entity) >= 2 and core_entity in searchable_text) or query_lower in searchable_text:
                exact_phrase_bonus += 0.40

            term_hits = sum(1 for w in query_words if w in searchable_text)
            term_coverage = term_hits / max(len(query_words), 1)

            # For concise substantive medical entities (<= 4 CJK characters), if exact entity is absent, penalize
            if substantive_cjk and len(substantive_cjk) in (2, 3, 4) and (core_query not in searchable_text and core_entity not in searchable_text and query_lower not in searchable_text):
                term_coverage = term_coverage * 0.3

            # Critical zero-hallucination check:
            if exact_phrase_bonus == 0 and (term_hits == 0 or term_coverage < 0.22):
                calibrated_score = round(base_score * 0.15 * term_coverage, 4)
            else:
                # 2. Structural Boost: Tables prioritized for requirement queries
                structural_bonus = 0.0
                if is_tabular_query and doc.get("metadata", {}).get("type") == "table":
                    structural_bonus += 0.25

                # 3. Overview / Mandate boost for definition queries
                overview_bonus = 0.0
                if is_overview_query:
                    if any(k in doc_title_zh for k in ["总览", "职责", "组织架构", "法定职责"]) or any(k in doc_title_en for k in ["overview", "mandate", "structure"]):
                        overview_bonus += 0.35

                # 4. Title / Section Direct Match Boost
                title_scope = f"{doc_title} {doc_title_zh} {doc_title_en} {metadata.get('section_title', '').lower()} {metadata.get('section_title_en', '').lower()}"
                title_hits = sum(1 for w in query_words if w in title_scope)
                title_bonus = round(min(0.25 * (title_hits / max(len(query_words), 1)), 0.25), 4)

                # Dedicated Main Document Subject Match Boost (exact subject matching in main title)
                subject_bonus = 0.0
                if core_entity and len(core_entity) >= 2 and (core_entity in doc_title or core_entity in doc_title_zh or core_entity in doc_title_en):
                    subject_bonus = 0.25
                elif (core_query and (core_query in doc_title or core_query in doc_title_zh or core_query in doc_title_en)) or (query_lower in doc_title or query_lower in doc_title_zh):
                    subject_bonus = 0.15

                # 5. Recency / Latest Version Boost (only applies to relevant docs)
                recency_bonus = 0.0
                if metadata.get("is_latest", False):
                    recency_bonus += 0.10

                # Compute final calibrated rerank score
                calibrated_score = (
                    (base_score * 0.35) +
                    (term_coverage * 0.30) +
                    exact_phrase_bonus +
                    structural_bonus +
                    overview_bonus +
                    title_bonus +
                    subject_bonus +
                    recency_bonus
                )

            scored_doc = dict(doc)
            scored_doc["rerank_score"] = round(calibrated_score, 4)
            reranked.append(scored_doc)

        reranked.sort(key=lambda x: x["rerank_score"], reverse=True)
        return reranked[:top_n]
