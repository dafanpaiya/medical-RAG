# -*- coding: utf-8 -*-
"""
Monograph Boundary Resolver (Phase 41B)
======================================
Deterministic compendial monograph boundary and entity attribution engine.
Resolves and enriches candidate chunks with verified or candidate monograph entities
according to a strict 4-level evidence hierarchy, preserving Phase 38 fail-closed
security guardrails against cross-monograph attribution errors.
"""

import os
import re
import json
import hashlib
from typing import Dict, List, Any, Optional, Tuple, Set
from collections import Counter


class MonographBoundaryResolver:
    """
    Deterministic resolver for Chinese Pharmacopoeia monograph boundaries.
    Prefers evidence in strict hierarchical order:
    1. Explicit chunk-level verified mapping (Gold Truth).
    2. Monograph title explicitly declared in chunk text header.
    3. Structural continuation of active monograph across adjacent chunks on same page.
    4. Unambiguous page-level corroboration (with conflict detection against multi-monograph pages).
    """

    def __init__(
        self,
        chunk_verified_map: Optional[Dict[str, Dict[str, Any]]] = None,
        page_monograph_map: Optional[Dict[Tuple[int, int], Tuple]] = None,
        quarantined_chunk_ids: Optional[Set[str]] = None
    ):
        self.chunk_verified_map = chunk_verified_map or {}
        self.page_monograph_map = page_monograph_map or {}
        self.quarantined_chunk_ids = quarantined_chunk_ids or set()

        # Identify pages that contain multiple verified monographs
        self.multi_monograph_pages: Set[Tuple[int, int]] = self._detect_multi_monograph_pages()

    def _detect_multi_monograph_pages(self) -> Set[Tuple[int, int]]:
        page_to_monos: Dict[Tuple[int, int], Set[str]] = {}
        for cid, info in self.chunk_verified_map.items():
            vol = info.get("volume")
            page = info.get("page")
            mono = info.get("verified_monograph")
            if vol is not None and page is not None and mono:
                key = (vol, page)
                if key not in page_to_monos:
                    page_to_monos[key] = set()
                # If there's an explicit split like 'A/B', count as multi-monograph page
                if "/" in mono:
                    return {key}
                page_to_monos[key].add(mono)

        return {k for k, mset in page_to_monos.items() if len(mset) > 1}

    def extract_monograph_title_from_text(self, clean_text: str, heading: str) -> Optional[str]:
        """
        Deterministically extracts an explicit compendial title declared on the first line.
        """
        if not clean_text:
            return None
        lines = [l.strip() for l in clean_text.split("\n") if l.strip()]
        if not lines:
            return None
        l0 = lines[0]

        # Pattern A: General Chapter / Standard Method Code e.g. "0101 片剂", "通则0101 片剂", "0512"
        m_gen = re.match(r"^(?:通则)?([0-9]{4}\s*[\u4e00-\u9fa5]+)", l0)
        if m_gen:
            return m_gen.group(0).strip()

        # Pattern B: Standard compendial monograph title block
        # Line 0: 2 to 12 Chinese characters without general punctuation
        if 2 <= len(l0) <= 12 and not any(c in l0 for c in "，。；：！？（）()【】<>《》0123456789%~-"):
            if len(lines) > 1:
                l1 = lines[1]
                # Corroborated by Pinyin, Latin capital name, or compendial intro statement
                is_pinyin_latin = bool(re.match(r"^[A-Za-z\s\(\)]+", l1))
                is_compendial_intro = any(l1.startswith(p) for p in ["本品为", "本品系", "本品含", "【来源】", "系由"])
                if is_pinyin_latin or is_compendial_intro:
                    return l0.strip()

        return None

    def resolve_chunk(
        self,
        chunk: Dict[str, Any],
        active_monograph: Optional[str] = None,
        active_source: Optional[str] = None
    ) -> Tuple[Dict[str, Any], Optional[str], Optional[str]]:
        """
        Resolves a single chunk according to the 4-level evidence hierarchy.
        Returns (enriched_chunk, updated_active_monograph, updated_active_source).
        """
        cid = chunk["chunk_id"]
        vol = chunk.get("volume_number")
        p1 = chunk.get("physical_page_1idx")
        c_type = chunk.get("chunk_type", "TEXT_CHUNK")
        defects = chunk.get("defect_tags", [])
        clean_text = chunk.get("clean_text", "")
        heading = chunk.get("structural_heading", "")
        page_key = (vol, p1)

        assigned_entity: Optional[str] = None
        status: Optional[str] = None
        evidence_source: Optional[str] = None
        rationale: Optional[str] = None
        is_quarantined: bool = False

        # -------------------------------------------------------------
        # Guard: Table and Matrix Defect Quarantine
        # -------------------------------------------------------------
        if c_type == "TABLE_CHUNK" or "TABLE_UNRESOLVED_STRUCTURE" in defects or cid in self.quarantined_chunk_ids:
            if cid not in self.chunk_verified_map:
                status = "QUARANTINED_TABLE"
                is_quarantined = True
                evidence_source = "TABLE_QUARANTINE_RULE"
                rationale = "Quarantined table or unresolved matrix structure"

        # -------------------------------------------------------------
        # Level 1: Explicit Validated Chunk-Level Mapping (Gold Truth)
        # -------------------------------------------------------------
        if not status and cid in self.chunk_verified_map:
            v_info = self.chunk_verified_map[cid]
            assigned_entity = v_info.get("verified_monograph")
            v_status = v_info.get("attribution_status")
            if v_status == "PARTIAL_MONOGRAPH_SPLIT":
                status = "AMBIGUOUS_ATTRIBUTION"
                rationale = f"Boundary split transition: {v_info.get('attribution_evidence')}"
            else:
                status = "VERIFIED_ATTRIBUTION"
                rationale = v_info.get("attribution_evidence", "Gold truth chunk-level attribution")
            evidence_source = "CHUNK_VERIFIED_MONOGRAPH_MAP"

            # Update page active context if not an ambiguous split
            if "/" not in str(assigned_entity):
                active_monograph = assigned_entity
                active_source = "CHUNK_VERIFIED"

        # -------------------------------------------------------------
        # Level 2: Monograph Title Explicitly Present in Chunk Text
        # -------------------------------------------------------------
        if not status:
            detected_title = self.extract_monograph_title_from_text(clean_text, heading)
            if detected_title:
                assigned_entity = detected_title
                status = "CANDIDATE_ATTRIBUTION"
                evidence_source = "EXPLICIT_CHUNK_TEXT_HEADER"
                rationale = f"Compendial monograph title declared in chunk text: '{detected_title}'"
                active_monograph = detected_title
                active_source = "CHUNK_HEADER"

        # -------------------------------------------------------------
        # Level 3: Structural Section Continuation on Same Physical Page
        # -------------------------------------------------------------
        if not status and active_monograph:
            # Check if this chunk is a standard compendial monograph section
            is_compendial_section = any(
                h in str(heading)
                for h in ["性状", "鉴别", "检查", "含量测定", "炮制", "性味", "功能", "用法", "贮藏", "规格", "注意", "浸出物"]
            )
            if is_compendial_section:
                assigned_entity = active_monograph
                status = "CANDIDATE_ATTRIBUTION"
                evidence_source = "PAGE_ADJACENT_SECTION_CONTINUATION"
                rationale = f"Inherited from preceding active monograph '{active_monograph}' on physical page {p1} ({active_source})"

        # -------------------------------------------------------------
        # Level 4: Page-Level Mapping as Conflict-Aware Corroboration
        # -------------------------------------------------------------
        if not status and page_key in self.page_monograph_map:
            page_hint_mono = self.page_monograph_map[page_key][0]
            # Safety check: Do not apply page map if this page has multiple verified monographs
            if page_key in self.multi_monograph_pages:
                status = "AMBIGUOUS_ATTRIBUTION"
                assigned_entity = None
                evidence_source = "MULTI_MONOGRAPH_PAGE_CONFLICT"
                rationale = f"Physical page {p1} contains multiple monographs; page-level hint '{page_hint_mono}' rejected to prevent cross-monograph attribution leakage"
            else:
                assigned_entity = page_hint_mono
                status = "CANDIDATE_ATTRIBUTION"
                evidence_source = "PAGE_MAP_CORROBORATED"
                rationale = f"Corroborated by verified single-monograph page inventory for page {p1}"
                active_monograph = page_hint_mono
                active_source = "PAGE_MAP"

        # -------------------------------------------------------------
        # Fallback: Unmapped Attribution
        # -------------------------------------------------------------
        if not status:
            status = "UNMAPPED_ATTRIBUTION"
            assigned_entity = None
            evidence_source = "NONE"
            rationale = "No explicit title block, verified mapping, or unambiguous section boundary found"

        enriched_chunk = dict(chunk)
        enriched_chunk["attribution_status"] = status
        enriched_chunk["assigned_entity"] = assigned_entity
        enriched_chunk["evidence_source"] = evidence_source
        enriched_chunk["decision_rationale"] = rationale
        enriched_chunk["is_quarantined"] = is_quarantined

        return enriched_chunk, active_monograph, active_source

    def resolve_corpus(self, chunks: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any], List[Dict[str, Any]]]:
        """
        Executes deterministic monograph resolution across all chunks in page order.
        """
        # Group chunks by physical page to respect page boundaries
        page_groups: Dict[Tuple[int, int], List[Dict[str, Any]]] = {}
        for c in chunks:
            key = (c.get("volume_number", 0), c.get("physical_page_1idx", 0))
            if key not in page_groups:
                page_groups[key] = []
            page_groups[key].append(c)

        enriched_corpus: List[Dict[str, Any]] = []
        unresolved_list: List[Dict[str, Any]] = []
        status_counts = Counter()
        volume_counts = Counter()
        conflicts_count = 0

        for key, page_chunk_list in page_groups.items():
            active_mono = None
            active_src = None
            for c in page_chunk_list:
                enriched, active_mono, active_src = self.resolve_chunk(c, active_mono, active_src)
                enriched_corpus.append(enriched)

                st = enriched["attribution_status"]
                status_counts[st] += 1
                volume_counts[f"Volume_{enriched.get('volume_number')}"] += 1

                if st in ("UNMAPPED_ATTRIBUTION", "AMBIGUOUS_ATTRIBUTION", "QUARANTINED_TABLE"):
                    unresolved_list.append({
                        "chunk_id": enriched["chunk_id"],
                        "volume_number": enriched.get("volume_number"),
                        "physical_page_1idx": enriched.get("physical_page_1idx"),
                        "attribution_status": st,
                        "structural_heading": enriched.get("structural_heading"),
                        "decision_rationale": enriched["decision_rationale"]
                    })

                if st == "AMBIGUOUS_ATTRIBUTION" or enriched["evidence_source"] == "MULTI_MONOGRAPH_PAGE_CONFLICT":
                    conflicts_count += 1

        summary = {
            "manifest_type": "CHP_2025_MONOGRAPH_BOUNDARY_RECONCILIATION",
            "phase": "PHASE_41B",
            "total_input_chunks": len(chunks),
            "total_enriched_chunks": len(enriched_corpus),
            "attribution_status_breakdown": dict(status_counts),
            "volume_breakdown": dict(volume_counts),
            "quarantined_table_chunks": status_counts.get("QUARANTINED_TABLE", 0),
            "conflicting_or_ambiguous_assignments": conflicts_count,
            "mapping_coverage_pct": round(
                (status_counts.get("VERIFIED_ATTRIBUTION", 0) + status_counts.get("CANDIDATE_ATTRIBUTION", 0)) / len(chunks) * 100, 2
            ),
            "denominator": len(chunks)
        }

        return enriched_corpus, summary, unresolved_list

    def save_derived_artifacts(
        self,
        output_dir: str,
        enriched_chunks: List[Dict[str, Any]],
        summary: Dict[str, Any],
        unresolved_chunks: List[Dict[str, Any]],
        source_hashes: Dict[str, str]
    ) -> Dict[str, str]:
        """
        Saves derived artifacts exclusively under the specified output directory.
        """
        os.makedirs(output_dir, exist_ok=True)
        summary["source_artifact_hashes"] = source_hashes

        p_chunks = os.path.join(output_dir, "candidate_enriched_chunks.json")
        p_summary = os.path.join(output_dir, "reconciliation_summary.json")
        p_unresolved = os.path.join(output_dir, "unresolved_chunks.json")

        with open(p_chunks, "w", encoding="utf-8") as f:
            json.dump({"total_chunks": len(enriched_chunks), "chunks": enriched_chunks}, f, ensure_ascii=False, indent=2)

        with open(p_summary, "w", encoding="utf-8") as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)

        with open(p_unresolved, "w", encoding="utf-8") as f:
            json.dump({"total_unresolved": len(unresolved_chunks), "unresolved_chunks": unresolved_chunks}, f, ensure_ascii=False, indent=2)

        return {
            "candidate_enriched_chunks": p_chunks,
            "reconciliation_summary": p_summary,
            "unresolved_chunks": p_unresolved
        }
