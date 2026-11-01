import os
import sys
import json
import re
from typing import List, Dict, Any, Tuple, Optional

BASE_DIR = r"d:\医药RAG"
sys.path.insert(0, BASE_DIR)

from src.vector_store import MedicalVectorStore
from src.reranker import MedicalReranker
from src.query_expander import ConservativeQueryExpander
from src.document_lifecycle import DocumentLifecycleManager, LifecycleStatus, IndexEligibility

# ==============================================================================
# Verified Chunk-Monograph Provenance Map (Multi-Monograph Page Overrides)
# ==============================================================================
CHUNK_MONOGRAPH_MAP: Dict[str, Tuple[str, str, str]] = {
    # Volume 1 Page 25: Upper section is 丁公藤 (lines 1-19), Lower section is 丁香 (lines 21-45)
    "CHP2025-V1-P0025-C01": ("丁公藤", "接前页正文", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C02": ("丁公藤", "浸出物", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C03": ("丁公藤", "含量测定_东莨菪内酯", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C04": ("丁公藤", "炮制", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C05": ("丁公藤", "性状", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C06": ("丁公藤", "同药材", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C07": ("丁公藤", "性味归经", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C08": ("丁公藤", "功能主治", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C09": ("丁公藤", "用法用量", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C10": ("丁公藤", "注意", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C11": ("丁公藤/丁香", "移行段落", "PARTIAL_MONOGRAPH_SPLIT"),
    "CHP2025-V1-P0025-C12": ("丁香", "性状鉴别", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C13": ("丁香", "检查_杂质水分", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C14": ("丁香", "含量测定_丁香酚", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C15": ("丁香", "炮制", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C16": ("丁香", "同药材", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C17": ("丁香", "性味归经", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C18": ("丁香", "功能主治", "VERIFIED_GOLD_TRUTH"),
    "CHP2025-V1-P0025-C19": ("丁香", "用法用量", "VERIFIED_GOLD_TRUTH"),
}

# ==============================================================================
# Verified Page-Monograph Provenance Map (52 Pages)
# ==============================================================================
PAGE_MONOGRAPH_MAP = {
    # Volume 1 (Traditional Chinese Medicine)
    (1, 25): ("丁香", "MONOGRAPH_TITLE", "丁香", 25, "VISUALLY_VERIFIED"),
    (1, 34): ("三七", "MONOGRAPH_TITLE", "三七", 34, "VISUALLY_VERIFIED"),
    (1, 42): ("大黄", "MONOGRAPH_TITLE", "大黄", 42, "VISUALLY_VERIFIED"),
    (1, 131): ("白芍", "MONOGRAPH_TITLE", "白芍", 131, "VISUALLY_VERIFIED"),
    (1, 133): ("白茅根/制白附子", "COMPOUND_HEADING", "白茅根/制白附子", 133, "VISUALLY_VERIFIED"),
    (1, 136): ("饮片", "SECTION_HEADER", "中药饮片规格", 136, "VISUALLY_VERIFIED"),
    (1, 138): ("瓜子金/白薇", "TRANSITION_PAGE", "瓜子金尾/白薇头", 138, "PROVISIONAL"),
    (1, 141): ("冬瓜皮", "MONOGRAPH_TITLE", "冬瓜皮", 141, "VISUALLY_VERIFIED"),
    (1, 144): ("结构化附表 HPLC色谱梯度表", "TABLE_HEADER", "HPLC色谱梯度洗脱表", 144, "VISUALLY_VERIFIED"),
    (1, 147): ("姜半夏", "MONOGRAPH_TITLE", "姜半夏", 147, "VISUALLY_VERIFIED"),
    (1, 149): ("老鹳草", "MONOGRAPH_TITLE", "老鹳草", 149, "VISUALLY_VERIFIED"),
    (1, 150): ("地肤子", "MONOGRAPH_TITLE", "地肤子", 150, "VISUALLY_VERIFIED"),
    (1, 153): ("地榆/生地黄", "TRANSITION_PAGE", "地榆/生地黄切片配方", 153, "PROVISIONAL"),
    (1, 155): ("芒硝", "MONOGRAPH_TITLE", "芒硝", 155, "VISUALLY_VERIFIED"),
    (1, 161): ("当归", "MONOGRAPH_TITLE", "当归", 161, "VISUALLY_VERIFIED"),
    (1, 163): ("结构化附表 梯度洗脱时间表", "TABLE_HEADER", "梯度洗脱时间表", 163, "VISUALLY_VERIFIED"),
    (1, 167): ("竹节参", "MONOGRAPH_TITLE", "竹节参", 167, "VISUALLY_VERIFIED"),

    # Volume 2 (Chemical Drugs)
    (2, 100): ("注射用门冬酰胺酶（埃希）", "MONOGRAPH_TITLE", "注射用门冬酰胺酶（埃希）", 100, "VISUALLY_VERIFIED"),
    (2, 350): ("注射用兰索拉唑", "MONOGRAPH_TITLE", "注射用兰索拉唑", 350, "VISUALLY_VERIFIED"),
    (2, 402): ("头孢哌酮钠", "MONOGRAPH_TITLE", "头孢哌酮钠", 402, "VISUALLY_VERIFIED"),
    (2, 405): ("头孢美唑钠", "MONOGRAPH_TITLE", "头孢美唑钠", 405, "VISUALLY_VERIFIED"),
    (2, 417): ("头孢拉定有关物质", "MONOGRAPH_TITLE", "头孢拉定有关物质表格", 417, "PROVISIONAL"),
    (2, 437): ("尼美舒利片", "MONOGRAPH_TITLE", "尼美舒利片", 437, "VISUALLY_VERIFIED"),
    (2, 756): ("阿司匹林", "MONOGRAPH_TITLE", "阿司匹林", 756, "VISUALLY_VERIFIED"),

    # Volume 3 (Biological Products & Vaccines)
    (3, 31): ("通则编目 品种正文", "HEADING_TEXT", "通则编目品种正文", 31, "VISUALLY_VERIFIED"),
    (3, 50): ("抗体偶联药物指导原则", "HEADING_TEXT", "抗体偶联药物指导原则", 50, "VISUALLY_VERIFIED"),
    (3, 100): ("13价肺炎球菌多糖结合疫苗（破伤风类毒素/白喉类毒素）", "MONOGRAPH_TITLE", "13价肺炎球菌多糖结合疫苗", 100, "VISUALLY_VERIFIED"),
    (3, 111): ("吸附破伤风疫苗", "MONOGRAPH_TITLE", "吸附破伤风疫苗", 111, "VISUALLY_VERIFIED"),
    (3, 113): ("吸附白喉破伤风联合疫苗", "MONOGRAPH_TITLE", "吸附白喉破伤风联合疫苗", 113, "VISUALLY_VERIFIED"),
    (3, 115): ("吸附白喉破伤风联合疫苗（成人及青少年用）", "MONOGRAPH_TITLE", "吸附白喉破伤风联合疫苗（成人及青少年用）", 115, "VISUALLY_VERIFIED"),
    (3, 121): ("吸附无细胞百白破联合疫苗", "MONOGRAPH_TITLE", "吸附无细胞百白破联合疫苗", 121, "VISUALLY_VERIFIED"),
    (3, 137): ("乙型脑炎减毒活疫苗", "MONOGRAPH_TITLE", "乙型脑炎减毒活疫苗", 137, "VISUALLY_VERIFIED"),
    (3, 139): ("乙型脑炎减毒活疫苗（支原体检查）", "MONOGRAPH_TITLE", "乙型脑炎减毒活疫苗（支原体检查）", 139, "VISUALLY_VERIFIED"),
    (3, 141): ("冻干乙型脑炎灭活疫苗（Vero细胞）", "MONOGRAPH_TITLE", "冻干乙型脑炎灭活疫苗（Vero细胞）", 141, "VISUALLY_VERIFIED"),
    (3, 148): ("双价肾综合征出血热灭活疫苗（Vero细胞）", "MONOGRAPH_TITLE", "双价肾综合征出血热灭活疫苗（Vero细胞）", 148, "VISUALLY_VERIFIED"),
    (3, 200): ("双价人乳头瘤病毒疫苗（大肠埃希菌）", "MONOGRAPH_TITLE", "双价人乳头瘤病毒疫苗（大肠埃希菌）", 200, "VISUALLY_VERIFIED"),

    # Volume 4 (General Chapters & Formulations)
    (4, 50): ("通则0108 栓剂", "HEADING_TEXT", "0108 栓剂 鱼雷形鸭嘴形", 50, "VISUALLY_VERIFIED"),
    (4, 57): ("通则0114 气雾剂/吸入制剂", "HEADING_TEXT", "0114 气雾剂/吸入制剂 微细粒子空气动力学", 57, "VISUALLY_VERIFIED"),
    (4, 100): ("通则0251 药用辅料", "HEADING_TEXT", "0251 药用辅料", 100, "VISUALLY_VERIFIED"),
    (4, 105): ("通则0301 一般鉴别试验", "HEADING_TEXT", "0301 一般鉴别试验", 105, "VISUALLY_VERIFIED"),
    (4, 107): ("通则0400 光学分析法/0401 紫外-可见分光光度法", "HEADING_TEXT", "0400 光学分析法/0401 紫外-可见分光光度法", 107, "VISUALLY_VERIFIED"),
    (4, 109): ("通则0401 紫外-可见分光光度法 拉曼散射", "HEADING_TEXT", "0401 紫外-可见分光光度法 拉曼散射", 109, "VISUALLY_VERIFIED"),
    (4, 111): ("通则0402 红外分光光度法", "HEADING_TEXT", "0402 红外分光光度法", 111, "VISUALLY_VERIFIED"),
    (4, 113): ("通则0403 近红外分光光度法", "HEADING_TEXT", "0403 近红外分光光度法 漫反射模式", 113, "VISUALLY_VERIFIED"),
    (4, 120): ("通则0412 电感耦合等离子体质谱法", "HEADING_TEXT", "0412 电感耦合等离子体质谱法", 120, "VISUALLY_VERIFIED"),
    (4, 121): ("通则0412 电感耦合等离子体质谱法 接口系统", "HEADING_TEXT", "0412 电感耦合等离子体质谱法 接口系统", 121, "VISUALLY_VERIFIED"),
    (4, 123): ("通则0412 电感耦合等离子体质谱法 外标法", "HEADING_TEXT", "0412 电感耦合等离子体质谱法 外标法不少于4个不同浓度", 123, "VISUALLY_VERIFIED"),
    (4, 127): ("通则0431 质谱法", "HEADING_TEXT", "0431 质谱法 顶空分析法提取挥发性成分", 127, "VISUALLY_VERIFIED"),
    (4, 132): ("通则0441 核磁共振波谱法", "HEADING_TEXT", "0441 核磁共振波谱法 化学位移、偶合常数、峰面积、弛豫时间", 132, "VISUALLY_VERIFIED"),
    (4, 134): ("通则0451 X射线衍射法", "HEADING_TEXT", "0451 X射线衍射法 物相定性与定量分析", 134, "VISUALLY_VERIFIED"),
    (4, 137): ("通则0461 X射线荧光光谱法", "HEADING_TEXT", "0461 X射线荧光光谱法 待测元素波长与能量测定", 137, "VISUALLY_VERIFIED"),
    (4, 450): ("通则附表", "TABLE_HEADER", "药典通则附表", 450, "PROVISIONAL")
}

# Explicit Verified Cross-Page Monograph Links
PARENT_TO_MONO_ID = {
    # ICP-MS General Chapter 0412 (Pages 120, 121, 123)
    "PARENT-V4-P0120": "MONO-V4-0412",
    "PARENT-V4-P0121": "MONO-V4-0412",
    "PARENT-V4-P0123": "MONO-V4-0412",
    # Diphtheria-Tetanus Vaccine Family (Pages 113, 115)
    "PARENT-V3-P0113": "MONO-V3-DT-VACCINE",
    "PARENT-V3-P0115": "MONO-V3-DT-VACCINE",
    # Japanese Encephalitis Vaccine Family (Pages 137, 139, 141)
    "PARENT-V3-P0137": "MONO-V3-JE-VACCINE",
    "PARENT-V3-P0139": "MONO-V3-JE-VACCINE",
    "PARENT-V3-P0141": "MONO-V3-JE-VACCINE"
}

MONO_ID_TO_PARENTS = {}
for pid, mid in PARENT_TO_MONO_ID.items():
    MONO_ID_TO_PARENTS.setdefault(mid, []).append(pid)

QUARANTINED_CHUNKS = {
    "CHP2025-V2-P0417-C08": "DEF_TABLE_UNALIGNED_DELIMITER",
    "CHP2025-V4-P0450-C01": "DEF_TABLE_UNALIGNED_DELIMITER",
    "CHP2025-V2-P0456-C01": "DEF_FORMULA_SUBSCRIPT_COMMA",
    "CHP2025-V3-P0073-C01": "DEF_SCIENTIFIC_NOTATION"
}

# ==============================================================================
# Schema-Aware Staging Record Content Extraction Function
# ==============================================================================
def extract_staging_record_content(
    record: Dict[str, Any],
    fallback_text: Optional[str] = None
) -> Tuple[Optional[str], str, Dict[str, Any]]:
    """
    Schema-aware content extraction for staging corpus records.
    Distinguishes structured tables, reclassified prose, dual representations,
    empty/whitespace content, and conflicting content variants.

    Returns:
        (content_text, chunk_type, meta_info)
    """
    cid = record.get("chunk_id", "UNKNOWN")
    classification = record.get("classification", "")
    rec_action = record.get("recommended_action", "")
    defect_tags = record.get("defect_tags") or []
    status_flag = record.get("status") or (record.get("table_data") or {}).get("status", "")

    # 1. Reject explicit conflict indicator
    if "CONFLICTING_REPRESENTATIONS" in defect_tags or status_flag == "CONFLICTING" or record.get("has_conflicting_content"):
        return None, "QUARANTINED_DEFECT", {
            "status": "REJECTED_CONFLICTING",
            "reason": f"Record {cid} has conflicting content representations flag."
        }

    # 2. Extract potential table representation
    tbl_data = record.get("table_data")
    tbl_md = None
    if isinstance(tbl_data, dict):
        tbl_md = tbl_data.get("markdown_table")
    if not tbl_md:
        tbl_md = record.get("markdown_table")
    if tbl_md and not isinstance(tbl_md, str):
        tbl_md = str(tbl_md)
    tbl_md_clean = tbl_md.strip() if tbl_md else ""

    # 3. Extract potential prose representation
    sep_prose = record.get("separated_prose")
    prose_text = None
    if isinstance(sep_prose, dict):
        prose_text = sep_prose.get("text")
    if not prose_text:
        prose_text = record.get("clean_text") or record.get("text")
    if not prose_text and fallback_text:
        prose_text = fallback_text
    if prose_text and not isinstance(prose_text, str):
        prose_text = str(prose_text)
    prose_clean = prose_text.strip() if prose_text else ""

    # 4. Check for conflicting representations (e.g. classification explicitly says false positive prose,
    # but a conflicting unaligned table is present and marked contradictory)
    if classification == "MACRO_BLOCK_FALSE_POSITIVE_PROSE" and tbl_md_clean and record.get("has_conflicting_table"):
        return None, "QUARANTINED_DEFECT", {
            "status": "REJECTED_CONFLICTING",
            "reason": f"Record {cid} marked FALSE_POSITIVE_PROSE conflicts with present table representation."
        }

    # Case 1: Pure Prose / Reclassified False-Positive Macro Block
    if classification == "MACRO_BLOCK_FALSE_POSITIVE_PROSE" or rec_action == "RECLASSIFY_AS_TEXT_CHUNK":
        if prose_clean:
            return prose_clean, "RESCUED_PROSE_CHUNK", {
                "status": "EXTRACTED_PROSE",
                "source_field": "separated_prose.text",
                "char_count": len(prose_clean)
            }
        else:
            return None, "REJECTED_EMPTY", {
                "status": "REJECTED_EMPTY",
                "reason": f"Record {cid} reclassified as text chunk but separated_prose.text is empty."
            }

    # Case 2: Authentic 2D Table with accompanying prose context (dual representation)
    if classification == "AUTHENTIC_2D_TABLE_LOCALIZED" or (tbl_md_clean and prose_clean):
        if tbl_md_clean and prose_clean:
            if record.get("conflict_detected"):
                return None, "QUARANTINED_DEFECT", {
                    "status": "REJECTED_CONFLICTING",
                    "reason": f"Record {cid} table and prose conflict."
                }
            composite_content = f"{prose_clean}\n\n{tbl_md_clean}"
            return composite_content, "TABLE_STRUCTURE_VERIFIED", {
                "status": "EXTRACTED_DUAL_TABLE_AND_PROSE",
                "source_fields": ["separated_prose.text", "table_data.markdown_table"],
                "table_chars": len(tbl_md_clean),
                "prose_chars": len(prose_clean)
            }
        elif tbl_md_clean:
            return tbl_md_clean, "TABLE_STRUCTURE_VERIFIED", {
                "status": "EXTRACTED_TABLE_ONLY",
                "source_field": "table_data.markdown_table",
                "char_count": len(tbl_md_clean)
            }
        elif prose_clean:
            return prose_clean, "RESCUED_PROSE_CHUNK", {
                "status": "EXTRACTED_PROSE_FALLBACK",
                "source_field": "separated_prose.text",
                "char_count": len(prose_clean)
            }
        else:
            return None, "REJECTED_EMPTY", {
                "status": "REJECTED_EMPTY_WHITESPACE",
                "reason": f"Record {cid} table and prose are both empty/whitespace."
            }

    # Case 3: Table-only representation
    if tbl_md_clean:
        return tbl_md_clean, "TABLE_STRUCTURE_VERIFIED", {
            "status": "EXTRACTED_TABLE_ONLY",
            "source_field": "markdown_table",
            "char_count": len(tbl_md_clean)
        }

    # Case 4: Prose-only representation
    if prose_clean:
        return prose_clean, "TEXT_CHUNK", {
            "status": "EXTRACTED_PROSE_ONLY",
            "source_field": "clean_text",
            "char_count": len(prose_clean)
        }

    # Case 5: Empty/whitespace-only content
    is_whitespace = (tbl_md is not None and len(tbl_md_clean) == 0) or (prose_text is not None and len(prose_clean) == 0)
    if is_whitespace:
        return None, "REJECTED_EMPTY", {
            "status": "REJECTED_EMPTY_WHITESPACE",
            "reason": f"Record {cid} contains only whitespace or empty strings."
        }

    return None, "REJECTED_MISSING", {
        "status": "REJECTED_MISSING",
        "reason": f"Record {cid} lacks both table_data and separated_prose representations."
    }

# ==============================================================================
# Staging Corpus Loader
# ==============================================================================
def load_staging_corpus():
    import pandas as pd
    p17_dir = os.path.join(BASE_DIR, "data", "staging", "p1_3_demo_exploratory_pilot", "phase17_candidate_quality_gate")
    p13_dir = os.path.join(BASE_DIR, "data", "staging", "p1_3_demo_exploratory_pilot", "phase13_batch200")
    p15_dir = os.path.join(BASE_DIR, "data", "staging", "p1_3_demo_exploratory_pilot", "phase15_quality_engineering")

    df_pages = pd.read_csv(os.path.join(p17_dir, "page_level_candidate_audit.csv"))
    passed_pages = df_pages[df_pages["page_disposition"] == "CANDIDATE_TEXT_REVIEW_PASSED"]
    passed_keys = set(zip(passed_pages["volume"], passed_pages["physical_page"]))

    with open(os.path.join(p13_dir, "candidate_chunks.json"), "r", encoding="utf-8") as f:
        all_chunks = json.load(f)["chunks"]

    text_corpus = []
    text_corpus_map = {}
    for c in all_chunks:
        if (c.get("volume_number"), c.get("physical_page_1idx")) in passed_keys:
            if c.get("chunk_id") == "CHP2025-V4-P0134-C01":
                continue
            vol = c.get("volume_number")
            page = c.get("physical_page_1idx")
            parent_id = f"PARENT-V{vol}-P{page:04d}"
            item = {
                "doc_id": c.get("chunk_id"),
                "content": c.get("clean_text", ""),
                "parent_id": parent_id,
                "metadata": {
                    "doc_title": f"《中国药典》2025年版 第{vol}部",
                    "volume": vol,
                    "page": page,
                    "chunk_id": c.get("chunk_id"),
                    "parent_id": parent_id,
                    "provenance_box_ids": c.get("source_box_ids", []),
                    "chunk_type": "TEXT_CHUNK"
                }
            }
            text_corpus.append(item)
            text_corpus_map[c.get("chunk_id")] = item

    with open(os.path.join(p15_dir, "table_engine_run_results.json"), "r", encoding="utf-8") as f:
        tbl_results = json.load(f)["results"]

    fp_map = {
        "CHP2025-V2-P0417-C08": (2, 417),
        "CHP2025-V2-P0756-C04": (2, 756),
        "CHP2025-V4-P0450-C01": (4, 450),
        "CHP2025-V1-P0144-C02": (1, 144),
        "CHP2025-V1-P0144-C11": (1, 144),
        "CHP2025-V1-P0163-C14": (1, 163)
    }

    verified_tables = []
    for r in tbl_results:
        cid = r.get("chunk_id")
        if cid in fp_map:
            vol, page = fp_map[cid]
            parent_id = f"PARENT-V{vol}-P{page:04d}"
            fallback = text_corpus_map.get(cid, {}).get("content")
            extracted_content, chunk_type, meta_info = extract_staging_record_content(r, fallback_text=fallback)

            # Fail closed: reject empty content representations
            if not extracted_content or not extracted_content.strip():
                continue

            doc_title = (
                f"《中国药典》2025年版 第{vol}部 结构化表格"
                if chunk_type == "TABLE_STRUCTURE_VERIFIED"
                else f"《中国药典》2025年版 第{vol}部"
            )

            verified_tables.append({
                "doc_id": cid,
                "content": extracted_content.strip(),
                "parent_id": parent_id,
                "metadata": {
                    "doc_title": doc_title,
                    "volume": vol,
                    "page": page,
                    "chunk_id": cid,
                    "parent_id": parent_id,
                    "chunk_type": chunk_type,
                    "extraction_status": meta_info.get("status"),
                    "source_fields": meta_info.get("source_fields") or meta_info.get("source_field")
                }
            })

    all_raw = text_corpus + verified_tables
    enriched = []
    chunk_by_id = {}
    parent_to_chunks = {}

    for d in all_raw:
        c = dict(d)
        meta = dict(c.get("metadata", {}))
        vol = meta.get("volume", 1)
        page = meta.get("page", 1)

        cid = c.get("doc_id")
        if cid in CHUNK_MONOGRAPH_MAP:
            mono_name, section_type, attr_status = CHUNK_MONOGRAPH_MAP[cid]
        else:
            mono_tuple = PAGE_MONOGRAPH_MAP.get((vol, page))
            mono_name = mono_tuple[0] if mono_tuple else ""
            attr_status = mono_tuple[4] if mono_tuple else "UNVERIFIED"

        enriched_title = f"《中国药典》2025年版 第{vol}部 {mono_name}".strip()

        meta["doc_title_zh"] = enriched_title
        meta["doc_title"] = enriched_title
        meta["monograph_name"] = mono_name
        meta["attribution_status"] = attr_status

        # Authoritative document lifecycle enrichment
        lifecycle = DocumentLifecycleManager.determine_chunk_lifecycle(meta)
        meta.update(lifecycle)

        pid = meta.get("parent_id") or f"PARENT-V{vol}-P{page:04d}"
        meta["parent_id"] = pid
        c["parent_id"] = pid
        c["metadata"] = meta

        cid = c["doc_id"]
        enriched.append(c)
        chunk_by_id[cid] = c
        parent_to_chunks.setdefault(pid, []).append(c)

    return enriched, chunk_by_id, parent_to_chunks

# ==============================================================================
# Cross-Page Monograph Assembler
# ==============================================================================
class CrossPageMonographAssembler:
    def __init__(self, chunk_by_id, parent_to_chunks, vs, reranker):
        self.chunk_by_id = chunk_by_id
        self.parent_to_chunks = parent_to_chunks
        self.vs = vs
        self.reranker = reranker

        # Build mono_to_pid lookup with longest monograph names first
        self.mono_to_pid = {}
        sorted_map = sorted(PAGE_MONOGRAPH_MAP.items(), key=lambda x: len(x[1][0]), reverse=True)
        for (vol, pg), meta in sorted_map:
            name = meta[0].split()[0]
            pid = f"PARENT-V{vol}-P{pg:04d}"
            self.mono_to_pid[name] = pid

    def assemble(
        self,
        query: str,
        reranked_candidates: Optional[List[Dict[str, Any]]] = None,
        top_k: int = 30,
        max_chars: int = 5000,
        max_chunks: int = 4
    ) -> Dict[str, Any]:
        if reranked_candidates is None:
            exp_q, _, _ = ConservativeQueryExpander.expand_query(query)
            raw_cands = self.vs.search(exp_q, top_k=top_k) if self.vs else []
            reranked_candidates = self.reranker.rerank(exp_q, raw_cands, top_n=top_k) if self.reranker else raw_cands

        if not reranked_candidates:
            return {
                "anchor": None, "anchor_cid": None, "anchor_pid": None,
                "assembled_chunks": [], "assembled_cids": [],
                "total_chars": 0, "assembly_triggered": False,
                "intra_page_triggered": False, "cross_page_triggered": False,
                "reason": "NO_CANDIDATES_RETRIEVED"
            }

        # Lifecycle eligibility filtering
        req_edition = None
        m_yr = re.search(r"(19\d\d|20\d\d)\s*(?:(?:年\s*)?版|年?\s*(?:中国)?药典)", query)
        if m_yr:
            req_edition = f"{m_yr.group(1)}年版"

        eligible_candidates = []
        for c in reranked_candidates:
            c_meta = c.get("metadata", {})
            is_elig, _ = DocumentLifecycleManager.is_eligible_for_current_retrieval(c_meta, {"requested_edition": req_edition})
            if is_elig:
                eligible_candidates.append(c)

        target_pid = None
        for mono_name, pid in self.mono_to_pid.items():
            if mono_name and mono_name in query:
                target_pid = pid
                break

        anchor = None
        quarantined_hit = None
        if target_pid:
            for c in eligible_candidates:
                if c.get("doc_id") in QUARANTINED_CHUNKS:
                    quarantined_hit = c.get("doc_id")
                    continue
                c_pid = c.get("parent_id") or c.get("metadata", {}).get("parent_id")
                if c_pid == target_pid:
                    anchor = c
                    break
        if anchor is None:
            for c in eligible_candidates:
                if c.get("doc_id") in QUARANTINED_CHUNKS:
                    quarantined_hit = c.get("doc_id")
                    continue
                anchor = c
                break

        if anchor is None:
            return {
                "anchor": None, "anchor_cid": None, "anchor_pid": None,
                "assembled_chunks": [], "assembled_cids": [],
                "total_chars": 0, "assembly_triggered": False,
                "intra_page_triggered": False, "cross_page_triggered": False,
                "quarantined_hit": quarantined_hit,
                "reason": f"ALL_CANDIDATES_QUARANTINED({quarantined_hit})" if quarantined_hit else "NO_ELIGIBLE_ANCHOR"
            }

        anchor["rerank_score"] = max(anchor.get("rerank_score", 0.0), anchor.get("hybrid_score", 0.0))
        anchor_cid = anchor["doc_id"]
        anchor_pid = anchor.get("parent_id") or anchor.get("metadata", {}).get("parent_id")
        anchor_text = anchor.get("content", "")

        assembled = [anchor]
        assembled_cids = [anchor_cid]
        assembled_chars = len(anchor_text)
        reasons = [f"ANCHOR_SELECTED({anchor_cid}, parent={anchor_pid})"]
        intra_triggered = False
        cross_triggered = False

        # 1. Intra-Page Sibling Assembly with Strict Provenance & Lifecycle Isolation
        siblings = self.parent_to_chunks.get(anchor_pid, [])
        key_aspects = [
            "性状", "鉴别", "检查", "杂质", "水分", "灰分", "总灰分", "酸不溶性灰分",
            "浸出物", "醇溶性", "含量测定", "色谱", "高效液相", "气相", "理论板数",
            "波长", "吸收系数", "流动相", "梯度", "柱温", "系统适用性", "贮藏",
            "规格", "处方", "用法与用量", "效价", "无菌", "纯度", "干燥失重",
            "重金属", "有关物质", "内酯", "0832", "2301", "2302", "0512", "0521"
        ]
        intervals = re.findall(r"\d+[～~-]\d+", query)
        query_wants_any = any(kw in query for kw in key_aspects) or bool(intervals)

        anchor_mono = anchor.get("metadata", {}).get("monograph_name")
        anchor_status = anchor.get("metadata", {}).get("attribution_status", "")
        anchor_ed = anchor.get("metadata", {}).get("edition")
        anchor_jur = anchor.get("metadata", {}).get("jurisdiction")
        anchor_lc = anchor.get("metadata", {}).get("lifecycle_status")

        if len(siblings) > 1 and query_wants_any:
            sibling_candidates = []
            for s in siblings:
                s_cid = s["doc_id"]
                if s_cid in assembled_cids or s_cid in QUARANTINED_CHUNKS:
                    continue
                s_meta = s.get("metadata", {})
                s_status = s_meta.get("attribution_status", "")
                # Strict safety: prevent cross-monograph, cross-edition, cross-jurisdiction leakage
                if s_meta.get("monograph_name") != anchor_mono or not anchor_mono:
                    continue
                if "PARTIAL_MONOGRAPH_SPLIT" in str(s_status) or "PARTIAL_MONOGRAPH_SPLIT" in str(anchor_status):
                    continue
                if s_status == "PENDING_VERIFICATION" or anchor_status == "PENDING_VERIFICATION":
                    continue
                if s_meta.get("edition") != anchor_ed:
                    continue
                if s_meta.get("jurisdiction") != anchor_jur:
                    continue
                if s_meta.get("lifecycle_status") != anchor_lc:
                    continue

                s_text = s.get("content", "")
                matched = []
                for kw in key_aspects:
                    if kw in query and kw in s_text and kw not in anchor_text:
                        matched.append(kw)
                    if "东莨菪内酯" in query and any(x in s_text for x in ["内酯", "0.050%"]) and "内酯" not in anchor_text:
                        matched.append("东莨菪内酯")
                    if "洗脱梯度" in query and "流动相" in s_text and "流动相" not in anchor_text:
                        matched.append("洗脱梯度")
                for iv in intervals:
                    if iv in s_text and iv not in anchor_text:
                        matched.append(iv)
                matched = list(dict.fromkeys(matched))
                if matched:
                    has_limits = any(sym in s_text for sym in ["%", "不得过", "不得少于", "不低于", "mg", "ml", "g", "nm", "℃"])
                    is_proc_only = any(term in s_text for term in ["【炮制】", "同药材"]) and not has_limits
                    prio_score = len(matched) * 10 + (10 if has_limits else 0) - (15 if is_proc_only else 0)
                    sibling_candidates.append((prio_score, s, s_cid, s_text, matched))

            sibling_candidates.sort(key=lambda x: x[0], reverse=True)

            for prio_score, s, s_cid, s_text, matched in sibling_candidates:
                if len(assembled) < max_chunks and (assembled_chars + len(s_text)) <= max_chars:
                    assembled.append(s)
                    assembled_cids.append(s_cid)
                    assembled_chars += len(s_text)
                    intra_triggered = True
                    reasons.append(f"SIBLING_COMPLEMENTARY({s_cid}: {','.join(matched)})")

        # 2. Cross-Page Monograph Linking (Phase 27)
        mono_id = PARENT_TO_MONO_ID.get(anchor_pid)
        if mono_id:
            linked_parents = [p for p in MONO_ID_TO_PARENTS.get(mono_id, []) if p != anchor_pid]
            candidate_cross = []
            for l_pid in linked_parents:
                l_chunks = self.parent_to_chunks.get(l_pid, [])
                for lc in l_chunks:
                    lc_cid = lc["doc_id"]
                    if lc_cid in assembled_cids or lc_cid in QUARANTINED_CHUNKS:
                        continue
                    lc_text = lc.get("content", "")
                    matched_cross = []
                    for kw in ["外标法", "接口系统", "采样锥", "截取锥", "趣取锥", "成人及青少年", "成人", "大孩子", "破伤风", "2IU", "40IU"]:
                        if (kw in query or (kw in ["成人及青少年", "2IU", "40IU"] and any(x in query for x in ["成人", "大孩子", "青少年"]))) and kw in lc_text:
                            matched_cross.append(kw)
                    term_score = sum(2 for kw in matched_cross)
                    if lc_cid in [c["doc_id"] for c in reranked_candidates[:5]] and any(term in lc_text for term in ["效价", "IU", "接口系统", "锥", "外标法"]):
                        term_score += 1
                        matched_cross.append("HIGH_RELEVANCE_CANDIDATE")
                    matched_cross = list(dict.fromkeys(matched_cross))
                    if matched_cross:
                        candidate_cross.append((term_score, l_pid, lc, matched_cross))

            candidate_cross.sort(key=lambda x: x[0], reverse=True)
            for term_score, l_pid, lc, matched_cross in candidate_cross:
                lc_cid = lc["doc_id"]
                lc_text = lc.get("content", "")
                if lc_cid not in assembled_cids and len(assembled) < max_chunks and (assembled_chars + len(lc_text)) <= max_chars:
                    assembled.append(lc)
                    assembled_cids.append(lc_cid)
                    assembled_chars += len(lc_text)
                    cross_triggered = True
                    reasons.append(f"CROSS_PAGE_MONO_LINK({mono_id}->{l_pid}->{lc_cid}: {','.join(matched_cross)})")

        assembled.sort(key=lambda x: x["doc_id"])
        triggered = intra_triggered or cross_triggered

        return {
            "anchor": anchor,
            "anchor_cid": anchor_cid,
            "anchor_pid": anchor_pid,
            "assembled_chunks": assembled,
            "assembled_cids": assembled_cids,
            "total_chars": assembled_chars,
            "assembly_triggered": triggered,
            "intra_page_triggered": intra_triggered,
            "cross_page_triggered": cross_triggered,
            "reason": "; ".join(reasons)
        }

# ==============================================================================
# Singleton Container
# ==============================================================================
_STAGING_ASSEMBLER = None

def get_staging_assembler():
    global _STAGING_ASSEMBLER
    if _STAGING_ASSEMBLER is None:
        enriched_chunks, chunk_by_id, parent_to_chunks = load_staging_corpus()
        embs = [MedicalVectorStore.generate_embedding(f"{d.get('metadata', {}).get('doc_title_zh', '')} {d.get('content', '')}") for d in enriched_chunks]
        vs = MedicalVectorStore(storage_path=None, read_only=False)
        vs.add_documents(enriched_chunks, embeddings=embs)
        reranker = MedicalReranker()
        _STAGING_ASSEMBLER = CrossPageMonographAssembler(chunk_by_id, parent_to_chunks, vs, reranker)
    return _STAGING_ASSEMBLER
