# -*- coding: utf-8 -*-
"""Phase 43.5.10 — entity-boundary reranking for the ChP staged index.

General mechanism only. No query names, aliases, dosage-form lists, or per-entity
exceptions appear in this file. The rule is:

    tier 3 — normalized attributed_entity equals the normalized query
    tier 2 — one normalized string contains the other (same entity family)
    tier 0 — unrelated, or the attributed_entity is a page placeholder

Candidates are ordered by (tier, existing score) descending, preserving the original
order within equal keys. This makes an exact entity match outrank a formulation or
combination-product document that merely contains the query string, without any
numeric threshold being introduced.

Additive only: protected files are untouched. The proxy and reranker wrappers are
installed explicitly by a caller (see src/pharmacopoeia_engine.py wiring, if used).
"""

import re
from typing import Any, Dict, List, Optional

_PUNCT = re.compile(r"[\s　．.·…·,，;；:：()（）\[\]【】、/]+")
_PLACEHOLDER = re.compile(
    r"^(Volume_\d+_Page_\d+|Vol\d+_P\d+_[A-Za-z0-9_]+|\[UNPARSED_NAME)"
)


def normalize(value: Any) -> str:
    return _PUNCT.sub("", str(value or "")).lower()


def is_placeholder(entity: Any) -> bool:
    return bool(_PLACEHOLDER.match(str(entity or "").strip()))


def entity_tier(query: str, entity: Any) -> int:
    """Return 3 (exact), 2 (same family), or 0 (unrelated/placeholder)."""
    q = normalize(query)
    e = normalize(entity)
    if not q or not e or is_placeholder(entity):
        return 0
    if e == q:
        return 3
    if len(q) >= 2 and (e in q or q in e):
        return 2
    return 0


def rerank_hits(
    query: str,
    hits: List[Dict[str, Any]],
    top_k: Optional[int] = None,
    score_key: str = "hybrid_score",
) -> List[Dict[str, Any]]:
    """Stable sort by (entity tier, score) descending. Does not mutate inputs."""
    decorated = []
    for position, hit in enumerate(hits):
        entity = (hit.get("metadata") or {}).get("attributed_entity")
        tier = entity_tier(query, entity)
        score = hit.get(score_key)
        try:
            score = float(score)
        except (TypeError, ValueError):
            score = 0.0
        item = dict(hit)
        item["entity_tier"] = tier
        decorated.append((tier, score, position, item))
    decorated.sort(key=lambda x: (x[0], x[1], -x[2]), reverse=True)
    ranked = [item for _, _, _, item in decorated]
    return ranked[:top_k] if top_k is not None else ranked


class EntityAwareVectorStore:
    """Search proxy that widens the candidate pool, then applies entity tiers."""

    def __init__(self, inner: Any, pool_k: int = 50):
        self.inner = inner
        self.pool_k = pool_k

    def search(self, query, query_embedding=None, top_k: int = 5, filters=None, alpha: float = 0.5):
        pool = self.inner.search(
            query=query,
            query_embedding=query_embedding,
            top_k=max(top_k, self.pool_k),
            filters=filters,
            alpha=alpha,
        )
        return rerank_hits(query, pool, top_k=top_k)

    def __getattr__(self, name):
        return getattr(self.inner, name)


class EntityTierReranker:
    """Wraps MedicalReranker so the answer path keeps entity tiers after reranking."""

    def __init__(self, inner: Any):
        self.inner = inner

    def rerank(self, query: str, candidates: List[Dict[str, Any]], top_n: int = 3):
        scored = self.inner.rerank(query=query, candidates=candidates, top_n=len(candidates))
        return rerank_hits(query, scored, top_k=top_n, score_key="rerank_score")