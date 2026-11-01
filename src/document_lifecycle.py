"""
GxP and Regulatory Knowledge Lifecycle Governance Module
Defines the authoritative lifecycle states, supersession relationships,
and retrieval eligibility rules for medical, pharmacopoeial, and regulatory documents.
"""

from enum import Enum
from typing import Dict, Any, List, Optional, Tuple, Set
import re
import datetime

class LifecycleStatus(str, Enum):
    """
    Standardized regulatory document lifecycle statuses.
    """
    CURRENT = "CURRENT"                             # Verified effective, statutory, eligible for present-day retrieval
    SUPERSEDED = "SUPERSEDED"                       # Replaced by a newer verified effective document; excluded from default retrieval
    HISTORICAL = "HISTORICAL"                       # Deprecated edition retained for traceability; excluded from default retrieval
    PENDING_VERIFICATION = "PENDING_VERIFICATION"   # Ingested/OCR draft, effective status unverified; not eligible for current retrieval
    REVOKED_OR_WITHDRAWN = "REVOKED_OR_WITHDRAWN"   # Authoritatively withdrawn or repealed; strictly excluded from retrieval

class IndexEligibility(str, Enum):
    """
    Index and retrieval eligibility classification.
    """
    ELIGIBLE_FOR_CURRENT_RETRIEVAL = "ELIGIBLE_FOR_CURRENT_RETRIEVAL"
    HISTORICAL_AUDIT_ONLY = "HISTORICAL_AUDIT_ONLY"
    EXCLUDED_UNVERIFIED = "EXCLUDED_UNVERIFIED"
    EXCLUDED_REVOKED = "EXCLUDED_REVOKED"

# Master Document Lifecycle Registry
# Maps document family / edition identifier to verified authoritative lifecycle record.
DOCUMENT_LIFECYCLE_REGISTRY: Dict[str, Dict[str, Any]] = {
    # --------------------------------------------------------------------------
    # Chinese Pharmacopoeia (ChP) - National Medical Products Administration (NMPA)
    # --------------------------------------------------------------------------
    "ChP-2025": {
        "document_family": "ChP",
        "edition": "2025年版",
        "official_title": "《中华人民共和国药典》2025年版",
        "issuing_authority": "国家药典委员会 / 国家药品监督管理局 (NMPA)",
        "publication_date": "2025-06-01",
        "effective_date": "2025-10-01",
        "lifecycle_status": LifecycleStatus.CURRENT.value,
        "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
        "supersedes": "ChP-2020",
        "superseded_by": None,
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "ChP",
        "governing_scope": "全品种法定药品标准（一部、二部、三部、四部）",
        "notes": "当前法定执行标准，自2025年10月1日起全面实施。"
    },
    "ChP-2020": {
        "document_family": "ChP",
        "edition": "2020年版",
        "official_title": "《中华人民共和国药典》2020年版",
        "issuing_authority": "国家药典委员会 / 国家药品监督管理局 (NMPA)",
        "publication_date": "2020-07-02",
        "effective_date": "2020-12-30",
        "lifecycle_status": LifecycleStatus.SUPERSEDED.value,
        "index_eligibility": IndexEligibility.HISTORICAL_AUDIT_ONLY.value,
        "supersedes": "ChP-2015",
        "superseded_by": "ChP-2025",
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "ChP",
        "governing_scope": "历史药品标准",
        "notes": "已于2025年10月1日被2025年版废止替代，仅可作为历史溯源对照，不得作为现行法规依据。"
    },
    "ChP-2015": {
        "document_family": "ChP",
        "edition": "2015年版",
        "official_title": "《中华人民共和国药典》2015年版",
        "issuing_authority": "国家药典委员会 / 国家食品药品监督管理总局 (CFDA)",
        "publication_date": "2015-06-05",
        "effective_date": "2015-12-01",
        "lifecycle_status": LifecycleStatus.HISTORICAL.value,
        "index_eligibility": IndexEligibility.HISTORICAL_AUDIT_ONLY.value,
        "supersedes": "ChP-2010",
        "superseded_by": "ChP-2020",
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "ChP",
        "governing_scope": "历史药品标准",
        "notes": "历史档案，禁止用于现行检索。"
    },

    # --------------------------------------------------------------------------
    # NMPA Medical Device Software & Quality Regulations
    # --------------------------------------------------------------------------
    "NMPA-CMDE-2022-No9": {
        "document_family": "NMPA_DEVICE_SOFTWARE",
        "edition": "2022年版",
        "official_title": "国家药监局器审中心《医疗器械软件注册审查指导原则（2022年修订版）》（2022年第9号）",
        "issuing_authority": "国家药品监督管理局医疗器械技术审评中心 (CMDE)",
        "publication_date": "2022-03-09",
        "effective_date": "2022-03-09",
        "lifecycle_status": LifecycleStatus.CURRENT.value,
        "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
        "supersedes": "NMPA-CMDE-2015-No50",
        "superseded_by": None,
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "NMPA",
        "governing_scope": "独立软件及含有软件组件的医疗器械注册申报",
        "notes": "现行有效指导原则。"
    },
    "NMPA-CMDE-2022-No7": {
        "document_family": "NMPA_CYBERSECURITY",
        "edition": "2022年版",
        "official_title": "国家药监局器审中心《医疗器械网络安全注册审查指导原则（2022年修订版）》（2022年第7号）",
        "issuing_authority": "国家药品监督管理局医疗器械技术审评中心 (CMDE)",
        "publication_date": "2022-03-07",
        "effective_date": "2022-03-07",
        "lifecycle_status": LifecycleStatus.CURRENT.value,
        "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
        "supersedes": "NMPA-CMDE-2017-No13",
        "superseded_by": None,
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "NMPA",
        "governing_scope": "医疗器械网络安全能力建设与注册审查",
        "notes": "现行有效指导原则。"
    },
    "NMPA-ORDER-739": {
        "document_family": "NMPA_REGULATION",
        "edition": "2021年版",
        "official_title": "国务院令第739号《医疗器械监督管理条例》",
        "issuing_authority": "中华人民共和国国务院",
        "publication_date": "2021-02-09",
        "effective_date": "2021-06-01",
        "lifecycle_status": LifecycleStatus.CURRENT.value,
        "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
        "supersedes": "国务院令第650号",
        "superseded_by": None,
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "NMPA",
        "governing_scope": "医疗器械研制、生产、经营、使用及监督管理总则",
        "notes": "医疗器械行业最高行政法规，现行有效。"
    },

    # --------------------------------------------------------------------------
    # US FDA Regulations & Guidances
    # --------------------------------------------------------------------------
    "FDA-QMSR-2024": {
        "document_family": "FDA_QSR_QMSR",
        "edition": "2024年最终规则",
        "official_title": "Medical Devices; Quality System Regulation Amendments (QMSR) Final Rule (89 FR 7496)",
        "issuing_authority": "US Food and Drug Administration (FDA)",
        "publication_date": "2024-02-02",
        "effective_date": "2026-02-02",
        "lifecycle_status": LifecycleStatus.CURRENT.value,
        "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
        "supersedes": "21 CFR Part 820 (1996 Legacy QSR)",
        "superseded_by": None,
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "FDA",
        "governing_scope": "21 CFR Part 820 质量管理体系法规（整合 ISO 13485:2016）",
        "notes": "最终规则已于2024年2月2日公布，过渡期截至2026年2月2日生效。"
    },
    "FDA-CYBERSECURITY-2023": {
        "document_family": "FDA_CYBERSECURITY",
        "edition": "2023年最终指南",
        "official_title": "Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions",
        "issuing_authority": "US Food and Drug Administration (FDA)",
        "publication_date": "2023-09-27",
        "effective_date": "2023-09-27",
        "lifecycle_status": LifecycleStatus.CURRENT.value,
        "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
        "supersedes": "FDA-Cybersecurity-Draft-2022",
        "superseded_by": None,
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "FDA",
        "governing_scope": "含软件医疗器械网络安全上市前申报（落实 FD&C Act Section 524B）",
        "notes": "现行有效法定指南。"
    },

    # --------------------------------------------------------------------------
    # European Union Medical Device Regulation (EU MDR)
    # --------------------------------------------------------------------------
    "EU-MDR-2017-745": {
        "document_family": "EU_MDR",
        "edition": "2017/745",
        "official_title": "Regulation (EU) 2017/745 on Medical Devices (MDR)",
        "issuing_authority": "European Parliament and Council of the European Union",
        "publication_date": "2017-05-05",
        "effective_date": "2021-05-26",
        "lifecycle_status": LifecycleStatus.CURRENT.value,
        "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
        "supersedes": "MDD 93/42/EEC",
        "superseded_by": None,
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "EU_MDR",
        "governing_scope": "欧盟医疗器械上市法规",
        "notes": "现行强制执行法规。"
    },

    # --------------------------------------------------------------------------
    # International Council for Harmonisation (ICH)
    # --------------------------------------------------------------------------
    "ICH-Q9-R1": {
        "document_family": "ICH_QUALITY",
        "edition": "Q9(R1)",
        "official_title": "ICH Guideline Q9(R1) on Quality Risk Management",
        "issuing_authority": "International Council for Harmonisation (ICH) / NMPA 转化采信",
        "publication_date": "2023-01-18",
        "effective_date": "2023-01-18",
        "lifecycle_status": LifecycleStatus.CURRENT.value,
        "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
        "supersedes": "ICH-Q9-2005",
        "superseded_by": None,
        "verification_status": "AUTHORITATIVE_VERIFIED",
        "jurisdiction": "ICH",
        "governing_scope": "药品全生命周期质量风险管理原则与方法",
        "notes": "现行最新修订版本。"
    }
}

class DocumentLifecycleManager:
    """
    Evaluates document lifecycle status, supersession relationships,
    and retrieval eligibility.
    """

    @classmethod
    def get_lifecycle_record(cls, identifier: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves lifecycle record by document ID, family key, or version text.
        """
        if not identifier:
            return None

        # Exact registry key lookup
        if identifier in DOCUMENT_LIFECYCLE_REGISTRY:
            return DOCUMENT_LIFECYCLE_REGISTRY[identifier]

        # Normalize text and search
        norm = identifier.lower().replace(" ", "").replace("-", "").replace("_", "")
        for key, record in DOCUMENT_LIFECYCLE_REGISTRY.items():
            k_norm = key.lower().replace("-", "").replace("_", "")
            if k_norm in norm or norm in k_norm:
                return record
            if record["edition"] in identifier or identifier in record["edition"]:
                return record
            if record["official_title"] in identifier or identifier in record["official_title"]:
                return record

        return None

    @classmethod
    def determine_chunk_lifecycle(cls, chunk_metadata: Dict[str, Any]) -> Dict[str, Any]:
        """
        Determines and returns verified lifecycle metadata for a given chunk.
        """
        doc_title = chunk_metadata.get("doc_title") or chunk_metadata.get("doc_title_zh", "")
        version = chunk_metadata.get("version", "")
        edition = chunk_metadata.get("edition", "")
        source_file = chunk_metadata.get("source_file", "")
        jur = chunk_metadata.get("jurisdiction", "")

        # 0. Explicit lifecycle override preservation
        if chunk_metadata.get("lifecycle_status") and chunk_metadata.get("edition"):
            st = chunk_metadata.get("lifecycle_status")
            ed = chunk_metadata.get("edition")
            is_cur = (st == LifecycleStatus.CURRENT.value)
            return {
                "edition": ed,
                "lifecycle_status": st,
                "is_latest": chunk_metadata.get("is_latest", is_cur),
                "superseded_by": chunk_metadata.get("superseded_by", ("ChP-2025" if "2020" in ed else None)),
                "index_eligibility": chunk_metadata.get("index_eligibility") or (IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value if is_cur else IndexEligibility.HISTORICAL_AUDIT_ONLY.value),
                "effective_date": chunk_metadata.get("effective_date"),
                "authority": chunk_metadata.get("authority") or "国家药典委员会 / NMPA",
                "jurisdiction": jur or "ChP"
            }

        # 1. ChP 2025 chunks
        if "2025" in doc_title or "2025" in version or "2025" in edition or "2025" in source_file:
            rec = DOCUMENT_LIFECYCLE_REGISTRY["ChP-2025"]
            return {
                "edition": "2025年版",
                "lifecycle_status": LifecycleStatus.CURRENT.value,
                "is_latest": True,
                "superseded_by": None,
                "index_eligibility": IndexEligibility.ELIGIBLE_FOR_CURRENT_RETRIEVAL.value,
                "effective_date": "2025-10-01",
                "authority": rec["issuing_authority"],
                "jurisdiction": "ChP"
            }

        # 2. ChP 2020 chunks (Superseded)
        if "2020" in doc_title or "2020" in version or "2020" in edition or "2020" in source_file:
            rec = DOCUMENT_LIFECYCLE_REGISTRY["ChP-2020"]
            return {
                "edition": "2020年版",
                "lifecycle_status": LifecycleStatus.SUPERSEDED.value,
                "is_latest": False,
                "superseded_by": "ChP-2025",
                "index_eligibility": IndexEligibility.HISTORICAL_AUDIT_ONLY.value,
                "effective_date": "2020-12-30",
                "authority": rec["issuing_authority"],
                "jurisdiction": "ChP"
            }

        # 3. Match against formal registry
        for key, rec in DOCUMENT_LIFECYCLE_REGISTRY.items():
            if rec["edition"] in doc_title or rec["edition"] in version:
                return {
                    "edition": rec["edition"],
                    "lifecycle_status": rec["lifecycle_status"],
                    "is_latest": (rec["lifecycle_status"] == LifecycleStatus.CURRENT.value),
                    "superseded_by": rec["superseded_by"],
                    "index_eligibility": rec["index_eligibility"],
                    "effective_date": rec["effective_date"],
                    "authority": rec["issuing_authority"],
                    "jurisdiction": rec["jurisdiction"]
                }

        # 4. Fallback for unclassified records: fail-closed to PENDING_VERIFICATION
        return {
            "edition": edition or "UNKNOWN",
            "lifecycle_status": LifecycleStatus.PENDING_VERIFICATION.value,
            "is_latest": False,
            "superseded_by": None,
            "index_eligibility": IndexEligibility.EXCLUDED_UNVERIFIED.value,
            "effective_date": None,
            "authority": "UNKNOWN",
            "jurisdiction": jur or "UNKNOWN"
        }

    @classmethod
    def is_eligible_for_current_retrieval(cls, chunk_metadata: Dict[str, Any], query_intent: Optional[Dict[str, Any]] = None) -> Tuple[bool, str]:
        """
        Strict retrieval eligibility filter.
        Returns: (is_eligible, reason_code)
        """
        lifecycle = cls.determine_chunk_lifecycle(chunk_metadata)
        status = lifecycle.get("lifecycle_status")
        is_latest = lifecycle.get("is_latest")

        # If query specifically targets historical/deprecated versions, allow historical retrieval
        req_edition = (query_intent or {}).get("requested_edition")
        if req_edition and req_edition in ("2020年版", "2020版", "2015年版", "2010年版"):
            if status in (LifecycleStatus.SUPERSEDED.value, LifecycleStatus.HISTORICAL.value):
                # Verify exact edition match for historical query
                if req_edition in lifecycle.get("edition", ""):
                    return True, "HISTORICAL_RETRIEVAL_EXPLICITLY_REQUESTED"
                else:
                    return False, f"HISTORICAL_EDITION_MISMATCH: Query requests [{req_edition}], chunk is [{lifecycle.get('edition')}]."

        # Default present-day query: ONLY CURRENT is eligible
        if status == LifecycleStatus.CURRENT.value and is_latest:
            return True, "CURRENT_STATUTORY_DOCUMENT"

        if status == LifecycleStatus.SUPERSEDED.value:
            superseded_by = lifecycle.get("superseded_by") or "ChP-2025"
            return False, f"SUPERSEDED_DOCUMENT_EXCLUDED: Replaced by [{superseded_by}]. Older editions cannot compete with current statutory requirements."

        if status == LifecycleStatus.HISTORICAL.value:
            return False, "HISTORICAL_DOCUMENT_EXCLUDED: Archived document retained for audit only."

        if status == LifecycleStatus.REVOKED_OR_WITHDRAWN.value:
            return False, "REVOKED_OR_WITHDRAWN_DOCUMENT_EXCLUDED: Document has been officially withdrawn."

        if status == LifecycleStatus.PENDING_VERIFICATION.value:
            return False, "UNVERIFIED_LIFECYCLE_STATUS_EXCLUDED: Document effective status cannot be verified."

        return False, f"INELIGIBLE_FOR_CURRENT_RETRIEVAL: Unknown lifecycle status [{status}]."

    @classmethod
    def validate_supersession(cls, requested_edition: Optional[str], candidate_chunks: List[Dict[str, Any]]) -> Tuple[bool, str, Dict[str, Any]]:
        """
        Validates supersession across candidate evidence chunks.
        Returns: (is_valid, reason_code, details)
        """
        if not candidate_chunks:
            return False, "EMPTY_CANDIDATE_LIST", {}

        detected_editions = set()
        detected_statuses = set()
        superseded_hits = []

        for c in candidate_chunks:
            meta = c.get("metadata", {})
            lc = cls.determine_chunk_lifecycle(meta)
            ed = lc.get("edition")
            st = lc.get("lifecycle_status")
            cid = c.get("doc_id") or meta.get("chunk_id", "UNKNOWN")

            detected_editions.add(ed)
            detected_statuses.add(st)

            if st in (LifecycleStatus.SUPERSEDED.value, LifecycleStatus.HISTORICAL.value):
                superseded_hits.append((cid, ed, st, lc.get("superseded_by")))

        # Check 1: Mixed versions across chunks
        if len(detected_editions) > 1:
            return False, "MIXED_EDITIONS_ACROSS_EVIDENCE", {
                "detected_editions": list(detected_editions),
                "error": "候选证据中混合包含多个不同药典版本，禁止跨版本拼装。"
            }

        # Check 2: Superseded chunk serving current query
        is_historical_query = requested_edition in ("2020年版", "2020版", "2015年版", "2010年版")
        if not is_historical_query and superseded_hits:
            hit_cid, hit_ed, hit_st, hit_super = superseded_hits[0]
            return False, "SUPERSEDED_EVIDENCE_REJECTED", {
                "chunk_id": hit_cid,
                "chunk_edition": hit_ed,
                "superseded_by": hit_super,
                "error": f"候选证据 [{hit_cid}] 属于已被废止/替代的版本 ({hit_ed})，已被 [{hit_super}] 替代，禁止作为现行法定标准输出。"
            }

        # Check 3: Query explicitly requests 2020, but candidate is 2025
        if requested_edition in ("2020年版", "2020版") and "2025年版" in detected_editions:
            return False, "REVERSE_EDITION_MISMATCH", {
                "requested_edition": requested_edition,
                "evidence_editions": list(detected_editions),
                "error": f"查询明确要求历史版本（{requested_edition}），但候选证据为现行2025年版，未建立跨版本等效对照。"
            }

        return True, "EVIDENCE_LIFECYCLE_COMPATIBLE", {
            "editions": list(detected_editions),
            "statuses": list(detected_statuses)
        }
