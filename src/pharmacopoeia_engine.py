# -*- coding: utf-8 -*-
"""Pharmacopoeia-backed variant of SecureQAEngine.

Additive adapter only: it subclasses `SecureQAEngine` and points it at a copy of the
2025 Chinese Pharmacopoeia staged index whose document metadata carries the physical page
number in the fields the citation builder reads (`pages` / `page`).

Phase 43.5.10 additionally installs the entity-boundary reranker on this engine only:
the retrieval pool is widened and re-ordered by exact/related entity tier before the
answer-path reranker runs. The 84-chunk enterprise regulatory corpus and `src.app` are
untouched and remain the default; no protected file is modified.

No protected file is modified. The 84-chunk enterprise regulatory corpus is untouched and
remains the default for `SecureQAEngine()` / `src.app`.

The index this points at is a metadata projection: every document and every embedding is
byte-identical to `data/staging/phase43_5_3/phase43_5_3_staged_kb.json`; only the citation
metadata was added (`pages`, `page`, `physical_volume`, `version`). See the Phase 43.5.7
and Phase 43.5.10 reports for the verification.
"""

import os

from src.entity_boundary_reranker import EntityAwareVectorStore, EntityTierReranker
from src.secure_qa_engine import SecureQAEngine

_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Overridable so a differently-named projection can be used without editing this file.
DEFAULT_CHP_INDEX = os.path.join(
    _BASE_DIR,
    "data", "staging", "phase43_5_7_demo_and_chp_20261025_132122",
    "chp2025_staged_kb_metadatamapped.json",
)


class PharmacopoeiaQAEngine(SecureQAEngine):
    """SecureQAEngine over the Chinese Pharmacopoeia 2025 corpus."""

    def __init__(self, db_path: str = None):
        index_path = db_path or os.environ.get("CHP_INDEX_PATH") or DEFAULT_CHP_INDEX
        if not os.path.exists(index_path):
            raise FileNotFoundError(
                f"Pharmacopoeia index not found: {index_path}. Set CHP_INDEX_PATH or pass db_path.")
        super().__init__(db_path=index_path)
        self.kb_engine.vector_store = EntityAwareVectorStore(self.kb_engine.vector_store)
        self.kb_engine.reranker = EntityTierReranker(self.kb_engine.reranker)