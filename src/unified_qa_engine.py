# -*- coding: utf-8 -*-
"""Unified Enterprise + ChP 2025 runtime engine (Option A).

One knowledge base, one query path: `data/staging/unified_kb_candidate/unified_kb_candidate.json`
(84 enterprise records + 11,852 ChP 2025 candidate records). Activation is opt-in through
`RAG_UNIFIED_KB_ENABLED` in `src/app.py`; the default stays `SecureQAEngine` over the
84-record enterprise KB until the consolidated tests pass and production activation is
explicitly approved.

Evidence policy enforced here:
- ChP citations expose printed pages as `pages`; physical PDF pages stay in
  `physical_pages` / `physical_volume`, never mixed into the citation-facing value.
- `CANDIDATE_ATTRIBUTION` records are labelled non-authoritative in every citation and in
  the answer-level evidence status; they are never presented as verified attribution.
- ChP entity scope comes from the recorded `attributed_entity`. Records are never forced
  into a category the source does not state; parameter queries fail closed when the entity
  relationship cannot be established.
- Enterprise records are passed through unchanged; their citations keep the existing shape.
- Unresolved enterprise/ChP source conflicts are surfaced, not adjudicated.

Startup integrity (fail-closed):
- The candidate file bytes must hash to APPROVED_CANDIDATE_SHA256 before it is loaded.
  `UNIFIED_KB_PATH` and `db_path` may point to a copy, but never to a different artifact.
- The trusted enterprise baseline is `data/enterprise_regulatory_kb.json` pinned to
  ENTERPRISE_KB_SHA256; all 84 documents and embeddings must match it exactly. A missing,
  malformed or mismatched baseline refuses startup.
- The authority conflict report must sit beside the candidate and be loadable; a missing or
  malformed report refuses startup instead of silently dropping conflict surfacing.
- This is the only startup engine (see `src/app.py::_build_engine`); there is no fallback
  corpus and no runtime switch.
"""

import hashlib
import inspect
import json
import os
import re
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

from src.entity_boundary_reranker import is_placeholder, rerank_hits
from src.reranker import MedicalReranker
from src.secure_qa_engine import SecureQAEngine

# The recovery path re-enters the base pipeline with a rewritten query; binding against the
# base signature keeps positional and keyword call sites working identically.
_ANSWER_QUERY_SIGNATURE = inspect.signature(SecureQAEngine.answer_query)

_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT_UNIFIED_KB = os.path.join(
    _BASE_DIR, "data", "staging", "phase54_ocr_repair",
    "unified_kb_candidate_phase54.json")
DEFAULT_ENTERPRISE_KB = os.path.join(_BASE_DIR, "data", "enterprise_regulatory_kb.json")
UNIFIED_KB_PATH_ENV = "UNIFIED_KB_PATH"

# Startup integrity pins. The candidate artifact and the trusted enterprise baseline are
# accepted only when their bytes match these approved values. A path override cannot bypass
# the check; approving a new hash requires a reviewed change to these constants plus a
# governance record (see data/staging/phase44_runtime_integration/).
APPROVED_CANDIDATE_SHA256 = "e8fcfff3cf7b4ddd8841046694132c6c5834ee53f87ce621a997259350328528"
ENTERPRISE_KB_SHA256 = "2699121ee7569e6673292a49f9422be43914139a30223125eed50cd97399818a"

CHP_JURISDICTION = "NMPA / Chinese Pharmacopoeia 2025"
CHP_STATUSES = (
    "CANDIDATE_ATTRIBUTION",
    "VERIFIED_ATTRIBUTION",
    "RECOVERED_VERIFIED_ATTRIBUTION",
)
EXPECTED_UNIFIED_TOTAL = 12089
EXPECTED_ENTERPRISE = 84
EXPECTED_CHP = 12005
EXPECTED_STATUS_COUNTS = {
    "CANDIDATE_ATTRIBUTION": 9482,
    "VERIFIED_ATTRIBUTION": 2364,
    "RECOVERED_VERIFIED_ATTRIBUTION": 159,
}

CHP_EVIDENCE_LABELS = {
    "CANDIDATE_ATTRIBUTION": {
        "evidence_level": "CANDIDATE_ATTRIBUTION_NON_AUTHORITATIVE",
        "zh": "非权威候选归因（CANDIDATE_ATTRIBUTION），不得作为已验证证据引用",
        "en": "non-authoritative candidate attribution (CANDIDATE_ATTRIBUTION)",
    },
    "VERIFIED_ATTRIBUTION": {
        "evidence_level": "VERIFIED_SOURCE_TEXT",
        "zh": "已验证归因（VERIFIED_ATTRIBUTION）",
        "en": "verified attribution (VERIFIED_ATTRIBUTION)",
    },
    "RECOVERED_VERIFIED_ATTRIBUTION": {
        "evidence_level": "RECOVERED_VERIFIED_SOURCE_TEXT",
        "zh": "恢复血统验证归因（RECOVERED_VERIFIED_ATTRIBUTION，非自动验证）",
        "en": "recovery-lineage verified attribution (RECOVERED_VERIFIED_ATTRIBUTION, not automatically verified)",
    },
}

_GENERAL_CHAPTER_KEYS = ("通则", "指导原则", "凡例", "总则", "总论")
_DOSAGE_FORM_MARKERS = (
    "片", "胶囊", "颗粒", "注射", "丸", "软膏", "乳膏", "凝胶", "栓", "散剂", "糖浆",
    "口服液", "滴眼", "眼用", "气雾", "贴剂", "肠溶", "喷雾", "洗剂", "酊剂",
)


def _file_sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _is_general_chapter_entity(entity: Any) -> bool:
    text = str(entity or "").strip()
    if not text:
        return False
    if re.match(r"^\d{4}", text):
        return True
    return any(key in text for key in _GENERAL_CHAPTER_KEYS)


def _normalize(value: Any) -> str:
    from src.entity_boundary_reranker import normalize
    return normalize(value)


def _chapter_referenced(entity: Any, query: str) -> bool:
    normalized_query = _normalize(query)
    normalized_entity = _normalize(entity)
    if normalized_entity and normalized_entity in normalized_query:
        return True
    match = re.match(r"^(\d{4})", str(entity or "").strip())
    return bool(match and match.group(1) in normalized_query)


_IDENTITY_SEPARATORS = r"[\s　．.·…,，;；:：()（）\[\]【】、/]*"
_IDENTITY_LEAD = re.compile(
    r"^([一-龥A-Za-z0-9Ⅰ-Ⅻ()（）·\-]{2,40}?)(?:的|中|里|项下|品种)")
_IDENTITY_EXCLUDED_PREFIXES = (
    "通则", "指导原则", "凡例", "总则", "总论", "中国药典", "药典")
_CHAPTER_SHAPED_SUFFIXES = ("法", "通则", "指导原则", "凡例")
_COMPENDIUM_PREAMBLE = re.compile(
    r"^\s*《?\s*中国药典\s*》?\s*(?:\d{4}\s*年版)?\s*(?:[一二三四]部)?\s*[，,、中]*\s*")
_SPECIFICATION_CUES = (
    "不得过", "不得超过", "不超过", "不能超过", "最多", "不得少于", "不少于", "不低于",
    "限度", "上限", "下限", "应为", "是多少")
_VOLUME_NUMERALS = {"一": 1, "二": 2, "三": 3, "四": 4}
_VOLUME_PATTERN = re.compile(r"(?:^|[《（(，,、\s]|中国药典|年版)([一二三四])部")


def _identity_entity_pattern(entity: Any) -> Optional["re.Pattern"]:
    """Tolerant matcher for one recorded entity surface inside a raw query.

    Punctuation, including parentheses, may vary between the record and the query, so
    every character is joined by an optional separator run and either parenthesis width
    matches the other.
    """
    text = str(entity or "").strip()
    if not text:
        return None
    parts = ["[()（）]" if char in "()（）" else re.escape(char) for char in text]
    return re.compile(_IDENTITY_SEPARATORS.join(parts))


def _query_identity_surface(query: Any) -> Optional[str]:
    """The leading noun phrase a query puts forward as a monograph identity, if any.

    Deliberately structural: it reports what the question names, not whether the
    knowledge base can resolve that name.
    """
    if not query:
        return None
    source = _COMPENDIUM_PREAMBLE.sub("", str(query).strip())
    match = _IDENTITY_LEAD.match(source)
    if match is None:
        return None
    surface = match.group(1).strip()
    if len(surface) < 2:
        return None
    if surface.startswith(_IDENTITY_EXCLUDED_PREFIXES):
        return None
    if re.match(r"^\d{4}", surface):
        return None
    return surface


def _declares_specification(query: Any) -> bool:
    text = str(query or "")
    return any(cue in text for cue in _SPECIFICATION_CUES)


def _request_only_qualifier(raw_query: str, entity: Any, content: str = "") -> Optional[str]:
    """Grade/type/salt qualifier carried by the request but absent from the record.

    Returns the qualifier text when the raw query attaches a parenthetical qualifier such
    as `（32）` or `（B型）` directly to the record's entity surface and that qualifier is
    present neither in the recorded entity nor in the record text. An identity-bearing
    qualifier can never be satisfied by a base-name match.
    """
    pattern = _identity_entity_pattern(entity)
    if pattern is None or not raw_query:
        return None
    match = pattern.search(raw_query)
    if match is None:
        return None
    tail = raw_query[match.end():match.end() + 24]
    qualifier_match = re.match(r"\s*[（(]\s*([^（）()]{1,20}?)\s*[）)]", tail)
    if qualifier_match is None:
        return None
    qualifier = qualifier_match.group(1).strip()
    normalized = _normalize(qualifier)
    if not normalized:
        return None
    if normalized in _normalize(entity):
        return None
    if content and normalized in _normalize(content):
        return None
    return qualifier


def _requested_volume(raw_query: Any) -> Optional[int]:
    """The ChP volume the request explicitly asks for, if it states one."""
    if not raw_query:
        return None
    match = _VOLUME_PATTERN.search(str(raw_query))
    if match is None:
        return None
    return _VOLUME_NUMERALS[match.group(1)]


def _volume_conflict(raw_query: Any, volume_number: Any) -> bool:
    requested = _requested_volume(raw_query)
    if requested is None or volume_number is None:
        return False
    try:
        return int(volume_number) != requested
    except (TypeError, ValueError):
        return False


def _surface_named(entity: Any, raw_query: Any) -> bool:
    normalized_entity = _normalize(entity)
    if len(normalized_entity) < 2 or not raw_query:
        return False
    return normalized_entity in _normalize(raw_query)


_RECOVERY_LEADING_NOISE = ("的", "中", "在", "里", "项下", "品种")
_RECOVERY_MAX_TERM = 8
_IDEOGRAPH = re.compile(r"[一-鿿]")
_CLOSING_BRACKETS = ("）", ")", "】", "]", "》")


def _identity_boundary_ok(text: str, match: "re.Match") -> bool:
    """True when the matched name is not embedded inside a longer Chinese word."""
    left = text[match.start() - 1] if match.start() > 0 else ""
    right = text[match.end()] if match.end() < len(text) else ""
    if left in _CLOSING_BRACKETS:
        # `（32）甘油酯`: the name continues a parenthetical compound, so this occurrence
        # is a fragment of a different identity.
        return False
    left_inside = bool(left) and bool(_IDEOGRAPH.match(left))
    right_inside = bool(right) and bool(_IDEOGRAPH.match(right))
    return not (left_inside and right_inside)


def _recovery_terms(query: str, identity: str) -> List[str]:
    """Candidate parameter phrases: CJK runs of the question, identity removed."""
    pattern = _identity_entity_pattern(identity)
    stripped = pattern.sub(" ", str(query)) if pattern is not None else str(query)
    terms = []
    for run in re.split(r"[^一-鿿]+", stripped):
        for noise in _RECOVERY_LEADING_NOISE:
            while run.startswith(noise):
                run = run[len(noise):]
        if len(run) >= 2:
            terms.append(run)
    return terms


def _entity_scope_ok(entity: Any, query_entity: str, raw_query: str) -> bool:
    """Conservative entity relationship for ChP records.

    Exact match is always accepted. A longer recorded entity (e.g. 阿司匹林片, 丁香茎叶油)
    is accepted only when its distinguishing remainder is named in the query; otherwise the
    formulation or related-entity record is not treated as the queried monograph.
    """
    normalized_entity = _normalize(entity)
    normalized_query_entity = _normalize(query_entity)
    normalized_raw = _normalize(raw_query)
    if not normalized_entity or not normalized_query_entity:
        return False
    if normalized_entity == normalized_query_entity:
        return True
    if normalized_query_entity in normalized_entity:
        remainder = normalized_entity.replace(normalized_query_entity, "", 1)
        if not remainder:
            return True
        if remainder in normalized_raw:
            return True
        # A dosage-form suffix is only meaningful when the query names a form.
        return any(marker in remainder and marker in normalized_raw for marker in _DOSAGE_FORM_MARKERS)
    if normalized_entity in normalized_query_entity:
        return True
    return False


class _EntityScopedVectorStore:
    """Search proxy: widen the pool only for queries with a resolved compendial entity.

    Non-entity queries keep the caller's exact top_k, so the enterprise path is unchanged.
    """

    def __init__(self, inner: Any, resolver, pool_k: int = 100):
        self.inner = inner
        self.resolver = resolver
        self.pool_k = pool_k

    def search(self, query, query_embedding=None, top_k: int = 5, filters=None, alpha: float = 0.5):
        focus = self.resolver(query)
        if not focus:
            return self.inner.search(
                query=query, query_embedding=query_embedding, top_k=top_k,
                filters=filters, alpha=alpha)
        pool = self.inner.search(
            query=query, query_embedding=query_embedding, top_k=max(top_k, self.pool_k),
            filters=filters, alpha=alpha)
        # Tier against the raw query, not the resolved entity: a query that names a
        # formulation ("阿司匹林片 溶出度") must keep the formulation eligible, while a
        # query that names only the substance ranks the substance record first.
        return rerank_hits(query, pool, top_k=top_k)

    def __getattr__(self, name):
        return getattr(self.inner, name)


class _EntityFocusReranker:
    """MedicalReranker over the caller's entity, then entity-tier ordering."""

    def __init__(self, resolver):
        self.resolver = resolver
        self.inner = MedicalReranker(entity_extractor=resolver)

    def rerank(self, query: str, candidates: List[Dict[str, Any]], top_n: int = 3):
        scored = self.inner.rerank(query=query, candidates=candidates, top_n=len(candidates))
        return rerank_hits(query, scored, top_k=top_n, score_key="rerank_score")


class UnifiedQAEngine(SecureQAEngine):
    """SecureQAEngine over the unified enterprise + ChP 2025 staging candidate."""

    def __init__(
        self,
        db_path: Optional[str] = None,
        delta_db_path: Optional[str] = None,
    ):
        kb_path = db_path or os.environ.get(UNIFIED_KB_PATH_ENV) or DEFAULT_UNIFIED_KB
        if not os.path.exists(kb_path):
            raise FileNotFoundError(
                f"Unified KB candidate not found: {kb_path}. Set {UNIFIED_KB_PATH_ENV} or pass db_path.")
        self.unified_kb_path = kb_path
        self.candidate_sha256 = self._verify_candidate_sha256(kb_path)
        if delta_db_path is None:
            super().__init__(db_path=kb_path)
        else:
            super().__init__(db_path=kb_path, delta_db_path=delta_db_path)
        documents = self.kb_engine.vector_store.documents
        self.candidate_verification = self._verify_candidate(documents)
        self._doc_metadata = {
            doc.get("doc_id"): (doc.get("metadata") or {}) for doc in documents}
        # Authoritative chunk text. `metadata.content_zh` is not usable as evidence here:
        # some candidate records carry another monograph's Chinese text in that field, while
        # `content` is the text the citation and the answer are actually built from.
        self._doc_text = {
            doc.get("doc_id"): (doc.get("content") or "") for doc in documents}
        self._authority_conflicts, self._conflict_report_status = self._load_authority_conflicts(kb_path)
        self.kb_engine.vector_store = _EntityScopedVectorStore(
            self.kb_engine.vector_store, self._resolve_query_entity)
        self.kb_engine.reranker = _EntityFocusReranker(self._resolve_query_entity)
        # Distinct recorded ChP identities, longest first: used only to tell "the KB holds
        # no record for the identity the question names" apart from "the matching record
        # contradicts the identity the question names" when building a refusal reason.
        self._chp_entity_surfaces = sorted(
            {
                _normalize(meta.get("attributed_entity"))
                for meta in self._doc_metadata.values()
                if meta.get("attribution_status") and meta.get("attributed_entity")
            },
            key=len,
            reverse=True,
        )
        # General chapters and guidelines are addressed by name, not by monograph identity,
        # so an unanswered chapter question is never reported as an identity problem.
        self._chp_chapter_surfaces = [
            surface for surface in self._chp_entity_surfaces
            if _is_general_chapter_entity(surface) and len(surface) >= 3
        ]
        # Normalized identity -> the entity string as recorded, so a recovery query can use
        # the source spelling instead of the punctuation- and case-folded lookup key.
        self._chp_entity_names = {}
        for meta in self._doc_metadata.values():
            entity = meta.get("attributed_entity")
            if meta.get("attribution_status") and entity:
                self._chp_entity_names.setdefault(_normalize(entity), str(entity))

    # ------------------------------------------------------------------
    # Candidate verification and conflict evidence
    # ------------------------------------------------------------------
    def _verify_candidate_sha256(self, kb_path: str) -> str:
        try:
            actual = _file_sha256(kb_path)
        except OSError as exc:
            raise RuntimeError(
                f"Unified KB candidate is unreadable: {kb_path}: {exc}") from exc
        if actual != APPROVED_CANDIDATE_SHA256:
            raise RuntimeError(
                "Unified KB candidate SHA-256 mismatch: "
                f"expected {APPROVED_CANDIDATE_SHA256}, got {actual} for {kb_path}. "
                "A different candidate requires a new approved hash recorded through the governance process.")
        return actual

    def _verify_candidate(self, documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        enterprise = [d for d in documents if not (d.get("metadata") or {}).get("attribution_status")]
        chp = [d for d in documents if (d.get("metadata") or {}).get("attribution_status")]
        if len(documents) != EXPECTED_UNIFIED_TOTAL:
            raise RuntimeError(
                f"Unified KB candidate has {len(documents)} documents, expected {EXPECTED_UNIFIED_TOTAL}.")
        if len(enterprise) != EXPECTED_ENTERPRISE or len(chp) != EXPECTED_CHP:
            raise RuntimeError(
                f"Unified KB composition mismatch: enterprise={len(enterprise)} "
                f"(expected {EXPECTED_ENTERPRISE}), ChP={len(chp)} (expected {EXPECTED_CHP}).")
        status_counts = Counter((d.get("metadata") or {}).get("attribution_status") for d in chp)
        if dict(status_counts) != EXPECTED_STATUS_COUNTS:
            raise RuntimeError(
                f"Unified KB attribution counts mismatch: {dict(status_counts)} "
                f"!= {EXPECTED_STATUS_COUNTS}.")
        ids = [d.get("doc_id") for d in documents]
        if len(set(ids)) != len(ids):
            raise RuntimeError("Unified KB candidate contains duplicate doc_id values.")
        for doc in chp:
            meta = doc["metadata"]
            entity = meta.get("attributed_entity")
            if not entity or is_placeholder(entity):
                raise RuntimeError(f"ChP record {doc.get('doc_id')} has a placeholder attribution entity.")
            if meta.get("page_mapping_status") != "VERIFIED":
                raise RuntimeError(f"ChP record {doc.get('doc_id')} has no verified page mapping.")
            printed = meta.get("printed_pages")
            if not isinstance(printed, list) or not printed or meta.get("pages") != printed:
                raise RuntimeError(
                    f"ChP record {doc.get('doc_id')} has inconsistent printed page fields.")
            if meta.get("physical_page_1idx") is None:
                raise RuntimeError(f"ChP record {doc.get('doc_id')} has no physical page index.")
            if meta.get("attribution_status") == "CANDIDATE_ATTRIBUTION":
                if meta.get("is_authoritative") is not False or not meta.get("candidate_evidence"):
                    raise RuntimeError(
                        f"CANDIDATE_ATTRIBUTION record {doc.get('doc_id')} is not marked non-authoritative.")
        enterprise_check = self._verify_enterprise_prefix(documents)
        return {
            "verified": True,
            "candidate_sha256": self.candidate_sha256,
            "total": len(documents),
            "enterprise": len(enterprise),
            "chp": len(chp),
            "status_counts": dict(status_counts),
            "enterprise_prefix": enterprise_check,
        }

    def _verify_enterprise_prefix(self, documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        baseline_path = DEFAULT_ENTERPRISE_KB
        if not os.path.exists(baseline_path):
            raise RuntimeError(
                f"Trusted enterprise baseline missing: {baseline_path}. Unified engine startup refused.")
        try:
            actual_hash = _file_sha256(baseline_path)
        except OSError as exc:
            raise RuntimeError(
                f"Trusted enterprise baseline unreadable: {baseline_path}: {exc}") from exc
        if actual_hash != ENTERPRISE_KB_SHA256:
            raise RuntimeError(
                "Trusted enterprise baseline SHA-256 mismatch: "
                f"expected {ENTERPRISE_KB_SHA256}, got {actual_hash} for {baseline_path}. "
                "Unified engine startup refused.")
        try:
            with open(baseline_path, encoding="utf-8") as handle:
                production = json.load(handle)
        except (OSError, ValueError) as exc:
            raise RuntimeError(
                f"Trusted enterprise baseline malformed or unreadable: {baseline_path}: {exc}") from exc
        production_docs = production.get("documents")
        production_embeddings = production.get("embeddings")
        if not isinstance(production_docs, list) or not isinstance(production_embeddings, list):
            raise RuntimeError(
                "Trusted enterprise baseline must contain 'documents' and 'embeddings' lists.")
        if len(production_docs) != EXPECTED_ENTERPRISE:
            raise RuntimeError(
                f"Enterprise baseline count mismatch: baseline={len(production_docs)}, "
                f"expected={EXPECTED_ENTERPRISE}.")
        if len(production_embeddings) != len(production_docs):
            raise RuntimeError(
                f"Enterprise baseline embedding count mismatch: documents={len(production_docs)}, "
                f"embeddings={len(production_embeddings)}.")
        if len(documents) != EXPECTED_UNIFIED_TOTAL:
            raise RuntimeError(
                f"Enterprise candidate count mismatch: candidate={len(documents)}, "
                f"expected={EXPECTED_UNIFIED_TOTAL}.")
        unified_embeddings = self.kb_engine.vector_store.embeddings
        if len(unified_embeddings) != len(documents):
            raise RuntimeError(
                f"Enterprise candidate embedding count mismatch: documents={len(documents)}, "
                f"embeddings={len(unified_embeddings)}.")
        prefix_docs = documents[:EXPECTED_ENTERPRISE]
        for index, doc in enumerate(prefix_docs):
            if (doc.get("metadata") or {}).get("attribution_status"):
                raise RuntimeError(
                    f"Enterprise prefix contains an attributed record at index {index} "
                    f"(doc_id={doc.get('doc_id')!r}). Unified engine startup refused.")
            if doc != production_docs[index]:
                raise RuntimeError(
                    f"Enterprise document mismatch at index {index} "
                    f"(doc_id={doc.get('doc_id')!r}). Unified engine startup refused.")
            if unified_embeddings[index] != production_embeddings[index]:
                raise RuntimeError(
                    f"Enterprise embedding mismatch at index {index} "
                    f"(doc_id={doc.get('doc_id')!r}). Unified engine startup refused.")
        return {
            "baseline_path": baseline_path,
            "expected_sha256": ENTERPRISE_KB_SHA256,
            "actual_sha256": actual_hash,
            "checked": True,
            "identical": True,
            "documents": len(production_docs),
            "embeddings": len(production_embeddings),
        }

    def _load_authority_conflicts(self, kb_path: str):
        report_path = os.path.join(
            os.path.dirname(os.path.abspath(kb_path)), "page_and_metadata_conflicts.json")
        if not os.path.exists(report_path):
            raise RuntimeError(
                "Authority conflict report missing beside the candidate: %s. "
                "Unresolved-source-conflict surfacing is required, so startup is refused "
                "rather than silently losing it." % report_path)
        try:
            with open(report_path, encoding="utf-8") as handle:
                report = json.load(handle)
        except (OSError, ValueError) as exc:
            raise RuntimeError(
                "Authority conflict report unreadable or malformed: %s: %s"
                % (report_path, exc)) from exc
        conflicts = report.get("authority_conflicts")
        if not isinstance(conflicts, list):
            raise RuntimeError(
                "Authority conflict report has no 'authority_conflicts' list: %s"
                % report_path)
        return conflicts, "LOADED"

    # ------------------------------------------------------------------
    # Entity resolution and conservative attribution filtering
    # ------------------------------------------------------------------
    def _resolve_query_entity(self, query: str) -> str:
        entity, _, _ = self._extract_compendial_entity_and_intent(query or "")
        return entity or ""

    def _extract_compendial_entity_and_intent(
        self, query: str
    ) -> Tuple[Optional[str], bool, Optional[str]]:
        """Parent resolution, plus an explicit signal when a named identity stayed unresolved.

        Step 6.5 only runs when one of its three inputs is set. A question that names a
        monograph and asks for one of its specifications ("月桂酰聚氧乙烯（32）甘油酯的游离
        甘油不得过多少？") used to leave all three empty, so the boundary filter was skipped
        and unrelated ChP evidence was accepted unchecked. Marking it as a monograph-parameter
        question routes it into Step 6.5 with an unresolved identity, which is then decided
        fail-closed instead of silently skipped. The entity itself is deliberately left
        unresolved: a surface name is not a verified identity.
        """
        entity, is_param, jurisdiction = super()._extract_compendial_entity_and_intent(query)
        if entity is None and jurisdiction is None and not is_param:
            if _query_identity_surface(query) and _declares_specification(query):
                is_param = True
        return entity, is_param, jurisdiction

    def _verify_candidate_entity_attribution(
        self,
        query_entity: Optional[str],
        is_monograph_param: bool,
        candidate_doc: Dict[str, Any],
        req_jurisdiction: Optional[str] = None,
        raw_query: str = "",
    ) -> bool:
        meta = candidate_doc.get("metadata", {})
        status = meta.get("attribution_status")
        if not status:
            return super()._verify_candidate_entity_attribution(
                query_entity, is_monograph_param, candidate_doc, req_jurisdiction, raw_query)
        if req_jurisdiction and req_jurisdiction != "ChP":
            return False
        entity = meta.get("attributed_entity")
        if not entity or is_placeholder(entity):
            return False
        content = candidate_doc.get("content") or candidate_doc.get("content_zh") or ""

        # Identity attributes are checked before any acceptance rule, so a record that
        # matches only a base name can never stand in for the requested identity.
        qualifier = _request_only_qualifier(raw_query, entity, content)
        if qualifier and not self._is_declared_alias(qualifier, entity):
            return False
        if _volume_conflict(raw_query, meta.get("volume_number")):
            return False

        # The record's own identity, named verbatim by the question, is sufficient. This
        # keeps genuine in-monograph evidence answerable when the resolver returned no
        # entity, a truncated name, or a phrase that is not the monograph at all.
        if _surface_named(entity, raw_query):
            return True

        general_chapter = _is_general_chapter_entity(entity)
        if query_entity:
            doc_id = candidate_doc.get("doc_id") or ""
            mentioned = (
                query_entity in str(entity)
                or query_entity in doc_id
                or query_entity in content
            )
            if not mentioned:
                return False
            if general_chapter:
                if is_monograph_param:
                    return _chapter_referenced(entity, raw_query)
                return True
            return _entity_scope_ok(entity, query_entity, raw_query)
        if not is_monograph_param:
            return True
        return general_chapter and _chapter_referenced(entity, raw_query)

    def _is_declared_alias(self, qualifier: str, entity: Any) -> bool:
        """True only when the qualifier resolves to the same identity through the project's
        declared alias table. No inferred synonyms: an unknown qualifier stays a conflict."""
        alias_entity, _, _ = self._extract_compendial_entity_and_intent(qualifier)
        if not alias_entity:
            return False
        return _normalize(alias_entity) == _normalize(entity)

    # ------------------------------------------------------------------
    # Answer-path evidence labelling
    # ------------------------------------------------------------------
    def answer_query(self, *args, **kwargs) -> Dict[str, Any]:
        query = args[0] if args else (kwargs.get("query") or "")
        result = super().answer_query(*args, **kwargs)
        recovered = self._attempt_targeted_recovery(query, args, kwargs, result)
        return self._apply_runtime_evidence_policy(recovered or result, query)

    # ------------------------------------------------------------------
    # Phase 58: bounded, evidence-gated retrieval recovery
    # ------------------------------------------------------------------
    def _attempt_targeted_recovery(self, query, args, kwargs, result):
        """Re-query a refused question with `<named identity> <named parameter>`.

        Only runs when the ordinary path already refused: a question that answered is never
        re-ranked, so no successful answer changes. The re-query reuses the whole pipeline,
        so the frozen threshold, the Phase 57 identity checks and the audit trail all still
        apply. The recovered answer is accepted only when its top citation is that same
        identity and its text contains the very parameter the question named - never another
        monograph, grade, salt, hydration state or volume.
        """
        if result.get("citations"):
            return None
        if result.get("evidence_level") != "INSUFFICIENT_EVIDENCE_REFUSAL":
            return None
        identities = self._named_identities(query)
        if len(identities) != 1:
            return None
        identity = identities[0]
        texts = self._identity_texts(identity)
        parameter = self._named_parameter(query, identity, texts)
        if not parameter:
            return None
        sub_query = "%s %s" % (identity, parameter)
        call = self._recovery_call(query, sub_query, args, kwargs)
        if call is None:
            return None
        try:
            recovered = SecureQAEngine.answer_query(self, *call[0], **call[1])
        except Exception:
            return None
        if not recovered.get("citations"):
            return None
        top_id = recovered["citations"][0].get("chunk_id") or ""
        top_meta = self._doc_metadata.get(top_id) or {}
        if _normalize(top_meta.get("attributed_entity")) != _normalize(identity):
            return None
        top_text = self._doc_text.get(top_id, "")
        if not top_text or _normalize(parameter) not in _normalize(top_text):
            return None
        # The recovered evidence must also satisfy the *original* question's identity
        # constraints: a rewritten query must never launder a grade, type, salt/hydration
        # state or volume that Phase 57 refused.
        query_entity, is_param, jurisdiction = self._extract_compendial_entity_and_intent(query)
        top_doc = {"doc_id": top_id, "metadata": top_meta, "content": top_text}
        if not self._verify_candidate_entity_attribution(
                query_entity, is_param, top_doc, jurisdiction, query):
            return None
        recovered["recovery"] = {
            "policy": "PHASE58_PARAMETER_FOCUSED_REQUERY",
            "identity": identity,
            "parameter": parameter,
        }
        return recovered

    def _named_identities(self, query):
        """Recorded ChP identities the question actually names, longest match first.

        An occurrence only counts when one of its sides is a boundary (punctuation, space or
        the end of the question). A bare substring inside a longer name is not the identity:
        `甘油` inside `月桂酰聚氧乙烯（32）甘油酯` must not become a recovery subject.
        """
        found = []
        rest = str(query or "")
        for surface in self._chp_entity_surfaces:
            if len(surface) < 2:
                continue
            name = self._chp_entity_names.get(surface, surface)
            pattern = _identity_entity_pattern(name)
            if pattern is None:
                continue
            match = pattern.search(rest)
            if match is None or not _identity_boundary_ok(rest, match):
                continue
            found.append(name)
            rest = rest[:match.start()] + " " + rest[match.end():]
        return found

    def _identity_texts(self, identity):
        return [
            self._doc_text.get(doc_id, "")
            for doc_id, meta in self._doc_metadata.items()
            if meta.get("attribution_status") and meta.get("attributed_entity") == identity
        ]

    @staticmethod
    def _named_parameter(query, identity, texts):
        """Longest question phrase that this identity's own chunks actually contain."""
        if not texts:
            return None
        for run in _recovery_terms(query, identity):
            for length in range(min(len(run), _RECOVERY_MAX_TERM), 1, -1):
                candidate = run[:length]
                if any(candidate in text for text in texts):
                    return candidate
        return None

    @staticmethod
    def _recovery_call(query, sub_query, args, kwargs):
        try:
            # The signature is the unbound function's, so `self` is bound as a placeholder
            # and dropped again when the call is rebuilt.
            bound = _ANSWER_QUERY_SIGNATURE.bind_partial(None, *args, **kwargs)
        except TypeError:
            return None
        bound.arguments["query"] = sub_query
        client_id = str(bound.arguments.get("client_id") or "web_user")
        bound.arguments["client_id"] = client_id + "#phase58_recovery"
        return bound.args[1:], bound.kwargs

    def _apply_runtime_evidence_policy(
        self, result: Dict[str, Any], query: str = ""
    ) -> Dict[str, Any]:
        if result.get("evidence_level") == "CATALOG_NAVIGATION_ONLY":
            self._rewrite_catalog_message(result)
            return result
        citations = result.get("citations") or []
        if not citations:
            self._apply_identity_refusal(result, query)
            return result
        unsupported = self._unsupported_parameter_answer(citations, query)
        if unsupported is not None:
            self._apply_parameter_refusal(result, unsupported, query)
            return result

        annotated: List[Dict[str, Any]] = []
        chp_statuses: List[str] = []
        matched_conflicts: Dict[str, Dict[str, Any]] = {}
        enterprise_count = 0
        for cite in citations:
            meta = self._doc_metadata.get(cite.get("chunk_id") or "")
            if not meta or not meta.get("attribution_status"):
                enterprise_count += 1
                annotated.append(cite)
                if meta:
                    for conflict in self._match_conflicts(meta):
                        matched_conflicts[str(conflict.get("entity"))] = conflict
                continue
            status = meta["attribution_status"]
            annotated.append(self._annotate_chp_citation(cite, meta))
            chp_statuses.append(status)
            for conflict in self._match_conflicts(meta):
                matched_conflicts[str(conflict.get("entity"))] = conflict

        result["citations"] = annotated
        conflict_note = ""
        if matched_conflicts:
            result["authority_conflicts"] = [
                self._describe_conflict(conflict) for conflict in matched_conflicts.values()]
            conflict_note = "\n\n【未裁决来源冲突】系统未选择任一来源为权威，引用各自保留其来源页码。\n" + "\n".join(
                f"- {entry}" for entry in result["authority_conflicts"])
        if not chp_statuses:
            if conflict_note:
                result["answer"] = f"{result.get('answer') or ''}{conflict_note}"
                views = result.get("translated_views")
                if isinstance(views, dict):
                    for key in list(views):
                        if views[key]:
                            views[key] = f"{views[key]}{conflict_note}"
            return result

        counts = Counter(chp_statuses)
        summary = dict(counts)
        summary["ENTERPRISE_AUTHORITATIVE"] = enterprise_count
        result["attribution_summary"] = summary
        if counts.get("CANDIDATE_ATTRIBUTION"):
            result["evidence_level"] = "CANDIDATE_EVIDENCE_NON_AUTHORITATIVE"
            result["evidence_label"] = (
                "包含非权威候选归因（CANDIDATE_ATTRIBUTION）；候选记录不得作为已验证证据引用")
        elif counts.get("RECOVERED_VERIFIED_ATTRIBUTION"):
            result["evidence_level"] = "RECOVERED_VERIFIED_EVIDENCE"
            result["evidence_label"] = (
                "包含恢复血统验证归因（RECOVERED_VERIFIED_ATTRIBUTION，非自动验证）")
        else:
            result["evidence_level"] = "VERIFIED_SOURCE_TEXT"
            result["evidence_label"] = "全部 ChP 引用为已验证归因（VERIFIED_ATTRIBUTION）"

        zh_note = self._evidence_status_note(annotated)
        answer = result.get("answer") or ""
        result["answer"] = f"{answer}\n\n{zh_note}{conflict_note}"

        views = result.get("translated_views")
        if isinstance(views, dict):
            for key in list(views):
                if not views[key]:
                    continue
                if key == "English":
                    views[key] = f"{views[key]}\n\n{self._english_status_note(annotated)}"
                else:
                    views[key] = f"{views[key]}\n\n{zh_note}{conflict_note}"
        return result

    def _apply_identity_refusal(self, result: Dict[str, Any], query: str) -> None:
        """Separate an identity refusal from an empty-corpus refusal.

        Only reached with nothing cited and a recorded top score of exactly zero: a positive
        score below the frozen threshold is a relevance refusal, never an identity one, and
        is left untouched. The response carries only the client-facing reason code and
        message; scores, candidate ids and resolver output stay in staging diagnostics.
        """
        if result.get("evidence_level") != "INSUFFICIENT_EVIDENCE_REFUSAL":
            return
        if (result.get("top_score") or 0.0) > 0.0:
            return
        if not _query_identity_surface(query):
            return
        normalized_surface = _normalize(_query_identity_surface(query))
        if normalized_surface.endswith(_CHAPTER_SHAPED_SUFFIXES):
            return
        if any(
            chapter in normalized_surface or normalized_surface in chapter
            for chapter in self._chp_chapter_surfaces
        ):
            return
        # A record only counts as "held by the KB" when its whole identity sits inside the
        # identity the question names; short entity fragments (e.g. 甘油 inside 甘油酯) do
        # not make a question about a different substance look resolvable.
        named = any(
            surface in normalized_surface
            for surface in self._chp_entity_surfaces if len(surface) >= 3)
        reason = "ENTITY_MISMATCH" if named else "ENTITY_UNRESOLVED"
        if reason == "ENTITY_MISMATCH":
            zh = ("无法确认所查询品种的确切身份：问题中指定的品种规格、型号或部次与知识库收录的品种记录不一致。"
                  "依据零幻觉策略，系统不以相近品种替代作答。请核对品种全称后重试，"
                  "或点击下方【转交人工专家】由法规事务专家核实。")
            en = ("The exact identity of the requested monograph cannot be confirmed: the grade, type or "
                  "volume stated in the question does not match any indexed monograph record. Under the "
                  "zero-hallucination policy the system will not answer from a similar substance. Please "
                  "verify the full monograph name or contact a regulatory specialist.")
        else:
            zh = ("无法确认问题所指的具体品种：知识库中未收录与问题所指名称一致的品种正文。"
                  "依据零幻觉策略，系统在品种身份无法确认时不予作答。请提供品种全称，"
                  "或点击下方【转交人工专家】由法规事务专家核实。")
            en = ("The monograph the question refers to cannot be identified: the knowledge base holds no "
                  "monograph record matching the name as stated. Under the zero-hallucination policy the "
                  "system does not answer when the identity cannot be confirmed. Please state the full "
                  "monograph name or contact a regulatory specialist.")
        english = not bool(re.search(r"[一-鿿]", query))
        result["evidence_level"] = reason + "_REFUSAL"
        result["intent"] = reason
        result["answer"] = en if english else zh
        views = result.get("translated_views")
        if isinstance(views, dict):
            views["Simplified Chinese"] = zh
            views["English"] = en

    # ------------------------------------------------------------------
    # Phase 60: parameter-evidence gate on the ordinary answer path
    # ------------------------------------------------------------------
    def _unsupported_parameter_answer(self, citations, query):
        """Return the unsupported (identity, parameter) pair, or None when the answer stands.

        This is the rule Phase 58 already applied to a recovered answer, applied to the
        ordinary answer path: the parameter phrase the question names - anchored in the cited
        monograph's own text - must actually appear in the cited evidence. The identity is
        taken from the evidence being cited, not from counting names in the question, because a
        question legitimately names analytes that are themselves monographs
        (「苯扎氯铵…苯甲醇、苯甲醛与氯化苄」). Where no parameter can be anchored, the existing
        rules decide rather than refusing on an inference.

        The check is against the *first* cited record - the one the answer leads with, exactly
        as Phase 58 gates a recovered answer. Testing the union of the citations instead lets a
        later record that merely mentions the test item carry an answer whose primary evidence
        does not state it (V4-B17 with top_n=10: the 贮藏/含量测定 chunk led the answer while a
        sibling chunk supplied the word 检查).
        """
        anchor, primary_text = None, ""
        for cite in citations:
            chunk_id = cite.get("chunk_id") or ""
            meta = self._doc_metadata.get(chunk_id) or {}
            if not meta.get("attribution_status"):
                continue
            anchor = str(meta.get("attributed_entity") or "")
            primary_text = self._doc_text.get(chunk_id, "")
            break
        if not anchor or not primary_text:
            return None
        parameter = self._named_parameter(query, anchor, self._identity_texts(anchor))
        if not parameter:
            return None
        if _normalize(parameter) in _normalize(primary_text):
            return None
        return {"identity": anchor, "parameter": parameter}

    def _apply_parameter_refusal(self, result, unsupported, query):
        zh = ("系统检索到的正文证据未覆盖问题所询问的具体检验项目，因此依据零幻觉策略不予作答。"
              "建议核对检验项目名称，或点击下方【转交人工专家】由法规事务专家核实。")
        en = ("The retrieved source text does not cover the specific test item the question asks "
              "about, so under the zero-hallucination policy the system will not answer from "
              "evidence that does not support the requested claim. Please verify the test-item "
              "name or contact a regulatory specialist.")
        english = not bool(re.search(r"[一-鿿]", query or ""))
        result["citations"] = []
        result["evidence_level"] = "UNSUPPORTED_PARAMETER_EVIDENCE_REFUSAL"
        result["intent"] = "PARAMETER_EVIDENCE_UNSUPPORTED"
        result["answer"] = en if english else zh
        result["translated_views"] = {"Simplified Chinese": zh, "English": en}
        result["needs_human_escalation"] = True

    def _annotate_chp_citation(self, cite: Dict[str, Any], meta: Dict[str, Any]) -> Dict[str, Any]:
        status = meta.get("attribution_status")
        label = CHP_EVIDENCE_LABELS[status]
        printed = self._as_page_list(meta.get("printed_pages"))
        physical = self._as_page_list(meta.get("physical_pages"))
        if not printed and meta.get("printed_page_number") is not None:
            printed = [meta["printed_page_number"]]
        if not physical and meta.get("physical_page_1idx") is not None:
            physical = [meta["physical_page_1idx"]]
        page_scheme = meta.get("page_scheme") or ("printed_primary" if printed else "physical_only")
        citation_pages = printed if printed else physical

        annotated = dict(cite)
        annotated["pages"] = ", ".join(str(page) for page in citation_pages)
        annotated["printed_pages"] = printed
        annotated["physical_pages"] = physical
        annotated["page_scheme"] = page_scheme
        annotated["page_mapping_status"] = meta.get("page_mapping_status")
        annotated["physical_volume"] = meta.get("physical_volume")
        annotated["volume_number"] = meta.get("volume_number")
        annotated["attribution_status"] = status
        annotated["is_authoritative"] = bool(meta.get("is_authoritative"))
        annotated["authority_basis"] = meta.get("authority_basis")
        annotated["candidate_evidence"] = bool(meta.get("candidate_evidence"))
        annotated["source_type"] = "CHP2025"
        annotated["evidence_level"] = label["evidence_level"]
        annotated["evidence_label"] = label["zh"]
        annotated["source_file"] = meta.get("source_file", annotated.get("source_file"))
        annotated["master_physical_pdf"] = meta.get(
            "master_physical_pdf", annotated.get("master_physical_pdf"))
        return annotated

    @staticmethod
    def _as_page_list(value: Any) -> List[Any]:
        if isinstance(value, list):
            return list(value)
        if value is None:
            return []
        return [value]

    def _evidence_status_note(self, citations: List[Dict[str, Any]]) -> str:
        lines = [
            "【运行时证据状态】以下标注逐条保留；CANDIDATE_ATTRIBUTION 为非权威候选归因，"
            "不得视为已验证证据。引用页码为印刷页，物理 PDF 页单独保留。"
        ]
        for cite in citations:
            if cite.get("source_type") != "CHP2025":
                continue
            lines.append(
                f"- [{cite.get('chunk_id')}] attribution_status={cite.get('attribution_status')}; "
                f"is_authoritative={cite.get('is_authoritative')}; "
                f"authority_basis={cite.get('authority_basis')}; "
                f"印刷页={cite.get('printed_pages')}; 物理页={cite.get('physical_pages')}; "
                f"卷={cite.get('physical_volume')}; 映射={cite.get('page_mapping_status')}"
            )
        return "\n".join(lines)

    def _english_status_note(self, citations: List[Dict[str, Any]]) -> str:
        lines = [
            "Runtime evidence status: ChP citations keep their recorded attribution status. "
            "CANDIDATE_ATTRIBUTION records are non-authoritative candidates and must not be cited "
            "as verified evidence. Citation pages are printed pages; physical PDF pages are kept "
            "separately. No verified English translation exists for the cited ChP text, so the "
            "original Chinese is shown."
        ]
        for cite in citations:
            if cite.get("source_type") != "CHP2025":
                continue
            lines.append(
                f"- [{cite.get('chunk_id')}] attribution_status={cite.get('attribution_status')}; "
                f"printed_pages={cite.get('printed_pages')}; physical_pages={cite.get('physical_pages')}"
            )
        return "\n".join(lines)

    def _match_conflicts(self, meta: Dict[str, Any]) -> List[Dict[str, Any]]:
        entity = str(meta.get("attributed_entity") or "")
        title = f"{meta.get('doc_title_zh') or ''} {meta.get('doc_title') or ''}"
        matched = []
        for conflict in self._authority_conflicts:
            names = {str(conflict.get("entity") or "")}
            for side in ("enterprise", "chp"):
                for record in conflict.get(side) or []:
                    if record.get("entity"):
                        names.add(str(record["entity"]))
            names.discard("")
            if any((name == entity) or (name in title) for name in names):
                matched.append(conflict)
        return matched

    def _describe_conflict(self, conflict: Dict[str, Any]) -> str:
        parts = []
        for side_label, side in (("企业库", "enterprise"), ("ChP 候选", "chp")):
            groups: Dict[tuple, int] = {}
            for record in conflict.get(side) or []:
                doc_id = record.get("doc_id")
                meta = self._doc_metadata.get(doc_id) or {}
                printed = self._as_page_list(meta.get("printed_pages"))
                if not printed:
                    printed = self._as_page_list(record.get("printed_page"))
                physical = self._as_page_list(meta.get("physical_pages"))
                if not physical:
                    physical = self._as_page_list(record.get("physical_page_1idx"))
                pages = self._as_page_list(meta.get("pages")) or printed
                status = meta.get("attribution_status") or "ENTERPRISE_AUTHORITATIVE"
                volume = meta.get("physical_volume") or record.get("physical_volume") or ""
                key = (str(volume), tuple(map(str, pages)), tuple(map(str, physical)), status)
                groups[key] = groups.get(key, 0) + 1
            for (volume, pages, physical, status), count in groups.items():
                entry = f"{side_label} 卷:{volume} 印刷页:{list(pages)}"
                if physical:
                    entry += f"/物理页:{list(physical)}"
                entry += f"（{status}，{count} 条）"
                parts.append(entry)
        return (
            f"实体「{conflict.get('entity')}」：" + "；".join(parts)
            + f"。裁决状态：UNRESOLVED（{conflict.get('note') or '未裁决'}）"
        )

    def _rewrite_catalog_message(self, result: Dict[str, Any]) -> None:
        citation = (result.get("citations") or [{}])[0]
        guide = citation.get("document") or "《中国药典》2025年版 编目分类指引"
        was_english = "Statutory Catalog Index Guide" in (result.get("answer") or "")
        zh = (
            "【法定编目索引指引 · 未检索到可引用的正文证据】\n\n"
            f"经核查《中华人民共和国药典》2025年版法定编目架构，编目归属线索为：{guide}。\n\n"
            "本次统一知识库检索未定位到可直接引用的正文块（或相关度低于证据门槛），"
            "系统依据零幻觉合规策略，不输出未经验证的检验规格、限度数值或具体处方。"
            "建议核对纸质母本对应条款，或转交法规专家人工核实。"
        )
        en = (
            "[Statutory Catalog Index Guide · No citable full-text evidence retrieved]\n\n"
            f"Catalog lead: {guide}. The unified knowledge base did not return a citable source "
            "chunk above the evidence threshold, so no specifications or limits are provided. "
            "Please verify against the printed master or escalate to a regulatory specialist."
        )
        result["answer"] = en if was_english else zh
        result["translated_views"] = {"Simplified Chinese": zh, "English": en}