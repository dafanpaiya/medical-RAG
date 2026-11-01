import os
import json
import math
import re
from typing import List, Dict, Any, Optional

class UnresolvedTableIngestionError(ValueError):
    """
    Raised when a table document with unresolved 2D structure (chunk_type=='TABLE_CHUNK'
    and status=='TABLE_UNRESOLVED_STRUCTURE') is submitted for plain text vector indexing.
    """
    pass


class MedicalVectorStore:
    """
    Lightweight, deterministic Hybrid Vector Store & Index for Life Sciences RAG.
    Features:
    1. Dense semantic vector storage & cosine similarity matching.
    2. Exact keyword / BM25-style lexical matching for device IDs & medical entities.
    3. Strict metadata filtering (e.g. enforce latest document versions, GxP document status).
    4. Full provenance tracking (doc_id, page, version, timestamp).
    """

    def __init__(self, storage_path: Optional[str] = None, read_only: bool = False):
        self.storage_path = storage_path
        self.read_only = read_only
        self.documents: List[Dict[str, Any]] = []
        self.embeddings: List[List[float]] = []

    def add_documents(self, docs: List[Dict[str, Any]], embeddings: Optional[List[List[float]]] = None):
        if self.read_only:
            raise RuntimeError(
                f"[SecurityGuard] MedicalVectorStore is in READ-ONLY mode. add_documents() operation was rejected."
            )

        # Ingestion Guard: Validate against unresolved table chunk ingestion
        for idx, doc in enumerate(docs):
            if not isinstance(doc, dict):
                continue
            chunk_type = doc.get("chunk_type") or (doc.get("metadata") or {}).get("chunk_type")
            table_meta = doc.get("table_metadata") or {}
            if not isinstance(table_meta, dict):
                table_meta = {}
            doc_meta = doc.get("metadata") or {}
            if not isinstance(doc_meta, dict):
                doc_meta = {}

            status = (
                doc.get("status")
                or table_meta.get("table_status")
                or doc_meta.get("status")
                or doc_meta.get("table_status")
            )

            if chunk_type == "TABLE_CHUNK" and status == "TABLE_UNRESOLVED_STRUCTURE":
                doc_id = doc.get("chunk_id") or doc.get("doc_id") or f"index_{idx}"
                raise UnresolvedTableIngestionError(
                    f"[IngestionGuard] Unresolved table document rejected: doc_id='{doc_id}', "
                    f"chunk_type='{chunk_type}', status='{status}'. "
                    f"Unresolved 2D tables must not enter normal text vector indexing."
                )

        for idx, doc in enumerate(docs):
            self.documents.append(doc)
            if embeddings and idx < len(embeddings):
                self.embeddings.append(embeddings[idx])
            else:
                self.embeddings.append([])

    @staticmethod
    def cosine_similarity(v1: List[float], v2: List[float]) -> float:
        if not v1 or not v2 or len(v1) != len(v2):
            return 0.0
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))
        if norm1 == 0.0 or norm2 == 0.0:
            return 0.0
        return dot / (norm1 * norm2)

    STOPWORDS = {
        "如何", "怎么", "什么", "使用", "设计", "进行", "可以", "请问", "关于", "什么是", "并且", "以及",
        "通过", "具有", "包括", "及其", "对于", "根据", "按照", "一个", "各个", "各种", "所有", "这个",
        "那个", "这些", "那些", "的", "了", "和", "是", "就", "在", "也", "与", "或", "于", "之", "为",
        "而", "及", "等", "以", "从", "到", "将", "被", "有", "无", "中", "上", "下", "来", "去", "做",
        "让", "使", "用", "技", "术", "设", "计", "如", "何", "成", "做", "好",
        "我想", "想知", "知道", "相关", "内容", "了解", "有关", "具体", "介绍", "资料", "信息",
        "我", "想", "知", "道", "相", "关", "内", "容", "有哪些", "有什么",
        "the", "a", "an", "is", "are", "was", "were", "of", "and", "in", "to", "for", "with",
        "on", "by", "at", "from", "as", "how", "what", "which", "who", "when", "where", "why",
        "can", "could", "should", "would", "do", "does", "did"
    }

    @classmethod
    def tokenize(cls, text: str, filter_stopwords: bool = True) -> List[str]:
        """Bilingual tokenizer supporting both English words and Chinese CJK n-grams with stopword filtering."""
        text_lower = text.lower()
        # English / alphanumeric words
        words = re.findall(r"[a-z0-9_]+", text_lower)
        # Chinese / CJK characters
        cjk_chars = re.findall(r"[\u4e00-\u9fff]", text_lower)

        tokens = []
        for w in words:
            if filter_stopwords and w in cls.STOPWORDS:
                continue
            tokens.append(w)

        # Add individual CJK characters if not stopwords
        for char in cjk_chars:
            if filter_stopwords and char in cls.STOPWORDS:
                continue
            tokens.append(char)

        # Add CJK 2-grams
        for i in range(len(cjk_chars) - 1):
            bi = cjk_chars[i] + cjk_chars[i+1]
            if filter_stopwords and bi in cls.STOPWORDS:
                continue
            tokens.append(bi)

        # Add CJK 3-grams
        for i in range(len(cjk_chars) - 2):
            tri = cjk_chars[i] + cjk_chars[i+1] + cjk_chars[i+2]
            if filter_stopwords and tri in cls.STOPWORDS:
                continue
            tokens.append(tri)

        return tokens

    def bm25_lexical_score(self, query: str, text: str) -> float:
        """Token coverage score supporting bilingual (English + CJK) medical queries."""
        query_tokens = set(self.tokenize(query))
        text_tokens = set(self.tokenize(text))
        if not text_tokens or not query_tokens:
            return 0.0

        matches = sum(1 for q in query_tokens if q in text_tokens)
        query_coverage = matches / len(query_tokens)

        # Bonus for exact query string containment
        if query.strip().lower() in text.lower():
            query_coverage += 0.35
        return min(query_coverage, 1.0)

    @classmethod
    def generate_embedding(cls, text: str, dim: int = 256) -> List[float]:
        """
        Generates a normalized, dense semantic vector embedding for medical & statutory text
        using bilingual character and n-gram subword hashing with L2 normalization.
        """
        tokens = cls.tokenize(text, filter_stopwords=True)
        if not tokens:
            return [0.0] * dim
        vec = [0.0] * dim
        try:
            import xxhash
            for t in tokens:
                h = xxhash.xxh32(t.encode("utf-8")).intdigest()
                idx = h % dim
                sign = 1.0 if (h >> 16) & 1 else -1.0
                weight = 1.5 if len(t) > 1 else 1.0
                vec[idx] += sign * weight
        except ImportError:
            for t in tokens:
                h = hash(t)
                idx = abs(h) % dim
                sign = 1.0 if (h > 0) else -1.0
                vec[idx] += sign

        norm = math.sqrt(sum(x * x for x in vec))
        if norm > 0.0:
            vec = [round(x / norm, 6) for x in vec]
        return vec

    def search(
        self,
        query: str,
        query_embedding: Optional[List[float]] = None,
        top_k: int = 5,
        filters: Optional[Dict[str, Any]] = None,
        alpha: float = 0.5  # 0.5 semantic vector, 0.5 lexical
    ) -> List[Dict[str, Any]]:
        """
        Hybrid search combining cosine similarity and exact keyword matching,
        with strict regulatory metadata filtering.
        """
        if query_embedding is None:
            query_embedding = self.generate_embedding(query)

        candidates = []

        for idx, doc in enumerate(self.documents):
            # 1. Apply Metadata Filters (e.g. version == 'latest', doc_type, etc.)
            if filters:
                match = True
                doc_meta = doc.get("metadata", {})
                for k, v in filters.items():
                    if doc_meta.get(k) != v:
                        match = False
                        break
                if not match:
                    continue

            # 2. Semantic score via Cosine Similarity
            semantic_score = 0.0
            if query_embedding and idx < len(self.embeddings) and self.embeddings[idx]:
                semantic_score = self.cosine_similarity(query_embedding, self.embeddings[idx])
            elif query_embedding:
                # On-demand generate if missing
                doc_text = f"{doc.get('title', '')} {doc.get('content', '')}"
                doc_emb = self.generate_embedding(doc_text)
                semantic_score = self.cosine_similarity(query_embedding, doc_emb)

            # 3. Lexical score via exact term matching (title + jurisdiction + content bilingually)
            content = doc.get("content", "")
            content_zh = doc.get("content_zh", "")
            content_en = doc.get("content_en", "")
            doc_title = doc.get("metadata", {}).get("doc_title", "")
            doc_title_zh = doc.get("metadata", {}).get("doc_title_zh", "")
            doc_title_en = doc.get("metadata", {}).get("doc_title_en", "")
            jurisdiction = doc.get("metadata", {}).get("jurisdiction", "")
            searchable_text = f"{doc_title} {doc_title_zh} {doc_title_en} {jurisdiction} {content} {content_zh} {content_en}"
            lexical_score = self.bm25_lexical_score(query, searchable_text)

            # 4. Normalized Hybrid Score
            # Branch-free: a non-positive semantic score must be damped, never promoted to a
            # full-weight lexical score, or a document with negative semantic similarity
            # outranks one with positive similarity.
            hybrid_score = (alpha * max(semantic_score, 0.0)) + ((1.0 - alpha) * min(lexical_score, 1.0))

            candidates.append({
                "doc_id": doc.get("doc_id"),
                "content": content,
                "content_zh": content_zh or content,
                "content_en": content_en or content,
                "metadata": doc.get("metadata", {}),
                "semantic_score": round(semantic_score, 4),
                "lexical_score": round(lexical_score, 4),
                "hybrid_score": round(hybrid_score, 4)
            })

        # Sort by hybrid score descending
        candidates.sort(key=lambda x: x["hybrid_score"], reverse=True)
        return candidates[:top_k]

    def save(self, filepath: str):
        if self.read_only:
            raise RuntimeError(
                f"[SecurityGuard] MedicalVectorStore is in READ-ONLY mode. Save operation to '{filepath}' was rejected."
            )
        data = {
            "documents": self.documents,
            "embeddings": self.embeddings
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self, filepath: str, read_only: Optional[bool] = None):
        if read_only is not None:
            self.read_only = read_only
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                self.documents = data.get("documents", [])
                self.embeddings = data.get("embeddings", [])
            elif isinstance(data, list):
                self.documents = data
                self.embeddings = []

        # Automatically compute in-memory embeddings if empty, without modifying file on disk
        has_dense_embeddings = bool(self.embeddings and len(self.embeddings) == len(self.documents) and any(bool(e) for e in self.embeddings))
        if not has_dense_embeddings and self.documents:
            print(f"[VectorStore] Populating in-memory embeddings for {len(self.documents)} documents (Read-Only mode: disk write disabled).")
            self.embeddings = [
                self.generate_embedding(f"{d.get('title', '')} {d.get('content', '')}")
                for d in self.documents
            ]
            # NEVER save back to disk during load! Silent write vulnerability eliminated.
