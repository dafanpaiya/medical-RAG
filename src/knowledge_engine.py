import os
import json
import uuid
import datetime
from typing import List, Dict, Any, Optional

from src.archivist_pipeline import extract_layout_aware_elements, build_atomic_chunks
from src.vector_store import MedicalVectorStore
from src.reranker import MedicalReranker
from src.audit_logger import AuditLogger

DATABASE_FILE = r"d:\医药RAG\data\knowledge_base.json"

class PharmaceuticalKnowledgeEngine:
    """
    Core Enterprise Knowledge Base Engine for Medical Device & Life Sciences.
    Orchestrates:
    - Data Ingestion & Layout-Aware Parsing
    - Dense / Lexical Indexing
    - Editable CMS with 21 CFR Part 11 Audit Trail
    - Hybrid Search + Reranking with Recency/Version Filtering
    - Citation Generation and Human Escalation Routing
    """

    def __init__(self, db_path: str = DATABASE_FILE, read_only: bool = True):
        self.db_path = db_path
        self.read_only = read_only
        self.vector_store = MedicalVectorStore(storage_path=db_path, read_only=read_only)
        self.reranker = MedicalReranker()
        self.audit_logger = AuditLogger()
        self.load_if_exists()

    def load_if_exists(self):
        if os.path.exists(self.db_path):
            self.vector_store.load(self.db_path, read_only=self.read_only)
            print(f"[KnowledgeEngine] Loaded {len(self.vector_store.documents)} chunks from database (read_only={self.read_only}).")

    def save_state(self):
        if self.read_only:
            raise RuntimeError(
                f"[SecurityGuard] PharmaceuticalKnowledgeEngine is in READ-ONLY mode for database '{self.db_path}'. save_state() rejected."
            )
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.vector_store.save(self.db_path)

    def ingest_pdf(
        self,
        pdf_path: str,
        doc_title: str,
        version: str,
        jurisdiction: str = "FDA",
        is_latest: bool = True,
        uploaded_by: str = "system_archivist"
    ) -> List[str]:
        """Ingests a PDF, strips noise, parses tables into Markdown, chunks, indexes, and logs."""
        if self.read_only:
            raise RuntimeError(
                f"[SecurityGuard] Ingestion rejected: PharmaceuticalKnowledgeEngine is in READ-ONLY mode for '{self.db_path}'."
            )
        print(f"[Archivist] Parsing {pdf_path} [{jurisdiction}] (Version: {version})...")
        elements = extract_layout_aware_elements(pdf_path)
        chunks = build_atomic_chunks(elements)

        # Mark older versions of this same document as is_latest = False
        if is_latest:
            for d in self.vector_store.documents:
                if d.get("metadata", {}).get("doc_title") == doc_title:
                    d["metadata"]["is_latest"] = False

        chunk_ids = []
        new_docs = []
        now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

        for c in chunks:
            chunk_id = f"chunk_{uuid.uuid4().hex[:8]}"
            chunk_ids.append(chunk_id)
            meta = {
                "chunk_id": chunk_id,
                "doc_title": doc_title,
                "jurisdiction": jurisdiction.upper(),
                "source_file": os.path.basename(pdf_path),
                "version": version,
                "is_latest": is_latest,
                "pages": c["pages"],
                "type": c["type"],
                "created_at": now_iso,
                "updated_at": now_iso
            }
            new_docs.append({
                "doc_id": chunk_id,
                "content": c["content"],
                "metadata": meta
            })

        self.vector_store.add_documents(new_docs)
        self.save_state()

        # 21 CFR Part 11 Audit Event
        self.audit_logger.log_event(
            event_type="DOCUMENT_INGESTION",
            user_id=uploaded_by,
            details={
                "doc_title": doc_title,
                "jurisdiction": jurisdiction.upper(),
                "version": version,
                "total_chunks": len(chunks),
                "is_latest": is_latest
            },
            doc_id=doc_title
        )
        print(f"[KnowledgeEngine] Successfully indexed {len(chunks)} chunks for '{doc_title}' [{jurisdiction}].")
        return chunk_ids

    def edit_or_enrich_chunk(
        self,
        chunk_id: str,
        new_content: str,
        edited_by: str,
        reason_for_change: str
    ) -> bool:
        """
        Editable CMS feature:
        Takes effect IMMEDIATELY, while logging exact before/after state to 21 CFR Part 11 audit trail.
        """
        if self.read_only:
            raise RuntimeError(
                f"[SecurityGuard] Chunk modification rejected: PharmaceuticalKnowledgeEngine is in READ-ONLY mode for '{self.db_path}'."
            )
        target_doc = None
        for doc in self.vector_store.documents:
            if doc.get("doc_id") == chunk_id:
                target_doc = doc
                break

        if not target_doc:
            return False

        old_content = target_doc["content"]
        target_doc["content"] = new_content
        now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
        target_doc["metadata"]["updated_at"] = now_iso
        target_doc["metadata"]["last_edited_by"] = edited_by

        self.save_state()

        # Audit Log
        self.audit_logger.log_event(
            event_type="CONTENT_MODIFICATION",
            user_id=edited_by,
            details={
                "reason": reason_for_change,
                "old_content": old_content,
                "new_content": new_content
            },
            doc_id=chunk_id
        )
        return True

    def query_knowledge_base(
        self,
        query: str,
        jurisdiction: Optional[str] = None,
        require_latest: bool = True,
        confidence_threshold: float = 0.20
    ) -> Dict[str, Any]:
        """
        Retrieval workflow:
        1. Hybrid Search (filters metadata for jurisdiction & latest version).
        2. Medical Reranking (prioritizes domain terms, tables, recency).
        3. Confidence evaluation: triggers Human Escalation if below threshold.
        4. Synthesizes verifiable citations.
        """
        filters = {}
        if require_latest:
            filters["is_latest"] = True
        if jurisdiction and jurisdiction.upper() != "ALL":
            filters["jurisdiction"] = jurisdiction.upper()

        # Step 1: Hybrid candidate retrieval
        candidates = self.vector_store.search(
            query=query,
            top_k=8,
            filters=filters if filters else None
        )

        # Step 2: Reranking
        reranked = self.reranker.rerank(query, candidates, top_n=3)

        top_score = reranked[0]["rerank_score"] if reranked else 0.0

        # Step 3: Human Escalation Check
        requires_human_escalation = (len(reranked) == 0 or top_score < confidence_threshold)

        # Step 4: Format Citations
        citations = []
        for doc in reranked:
            m = doc.get("metadata", {})
            pages_str = ", ".join(str(p) for p in m.get("pages", []))
            citations.append({
                "chunk_id": doc.get("doc_id"),
                "jurisdiction": m.get("jurisdiction", "UNKNOWN"),
                "document": m.get("doc_title"),
                "version": m.get("version"),
                "pages": pages_str,
                "type": m.get("type"),
                "score": doc.get("rerank_score"),
                "content_preview": doc.get("content")[:180] + "..."
            })

        result = {
            "query": query,
            "top_score": top_score,
            "requires_human_escalation": requires_human_escalation,
            "escalation_message": "Information not found with high confidence in the approved regulatory database. Click to route to an internal specialist." if requires_human_escalation else None,
            "citations": citations,
            "retrieved_context": [d.get("content") for d in reranked]
        }

        # Query audit log
        self.audit_logger.log_event(
            event_type="SEARCH_QUERY",
            user_id="employee_query",
            details={
                "query": query,
                "top_score": top_score,
                "requires_escalation": requires_human_escalation,
                "num_results": len(reranked)
            }
        )

        return result
