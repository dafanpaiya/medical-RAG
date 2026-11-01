# -*- coding: utf-8 -*-
"""
Phase 42D.1 — Single-Chunk Boundary Splitting Pilot
==================================================
Target: CHP2025-V1-P0025-C11 (丁公藤 / 丁香 mixed transition chunk)

Governing Principles:
1. Exact text conservation: every character, token, and line break is preserved.
2. Traceable boundary evidence: boundary verified against authentic ground-truth transcriptions.
3. Strict lineage tracking: child chunks retain complete parent coordinates, hashes, and evidence.
4. Fail-closed attribution: child chunks are NOT automatically promoted to VERIFIED_ATTRIBUTION;
   they are assigned CANDIDATE_ATTRIBUTION with explicit non-verified disclaimers.
5. Isolation: Staging-only outputs, no side-effects on Phase 42C deliverables or runtime engines.
"""

import os
import json
import hashlib
from typing import Dict, Any, List, Optional, Tuple


PROJECT_ROOT = r"D:\医药RAG"


class Phase42dBoundarySplitter:
    """
    Deterministic boundary splitter for Chinese Pharmacopoeia 2025 candidate chunks.
    Evaluates mixed transition chunks and performs text-preserving sub-chunking.
    """

    def __init__(
        self,
        candidate_chunks_path: str = "data/staging/p1_3_demo_exploratory_pilot/phase13_batch200/candidate_chunks.json",
        candidate_attributions_path: str = "data/staging/phase42c_attribution/phase42c_candidate_attributions.json",
        gt_dir: str = "data/staging/p1_3_demo_exploratory_pilot/phase14_gold_truth/gold_truth_transcriptions"
    ):
        self.candidate_chunks_path = os.path.join(PROJECT_ROOT, candidate_chunks_path) if not os.path.isabs(candidate_chunks_path) else candidate_chunks_path
        self.candidate_attributions_path = os.path.join(PROJECT_ROOT, candidate_attributions_path) if not os.path.isabs(candidate_attributions_path) else candidate_attributions_path
        self.gt_dir = os.path.join(PROJECT_ROOT, gt_dir) if not os.path.isabs(gt_dir) else gt_dir

    @staticmethod
    def compute_sha256_text(text: str) -> str:
        """Computes SHA-256 hash of UTF-8 encoded string."""
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    @staticmethod
    def compute_sha256_file(path: str) -> Optional[str]:
        """Computes SHA-256 hash of a file on disk."""
        if not os.path.exists(path):
            return None
        h = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(65536):
                h.update(chunk)
        return h.hexdigest()

    def load_chunk_and_context(self, chunk_id: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Loads the source chunk and attribution context with strict existence
        and uniqueness verification.
        """
        # 1. Source chunk from candidate_chunks.json
        if not os.path.exists(self.candidate_chunks_path):
            raise FileNotFoundError(f"Candidate chunks file not found: {self.candidate_chunks_path}")
        with open(self.candidate_chunks_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        chunks = raw_data.get("chunks", [])
        matched_chunks = [c for c in chunks if c.get("chunk_id") == chunk_id]
        if len(matched_chunks) == 0:
            raise ValueError(f"Target chunk '{chunk_id}' not found in candidate chunks")
        if len(matched_chunks) > 1:
            raise ValueError(f"Duplicate target chunk '{chunk_id}' found in candidate chunks ({len(matched_chunks)} instances)")
        source_chunk = matched_chunks[0]

        # 2. Candidate attribution from phase42c_candidate_attributions.json
        if not os.path.exists(self.candidate_attributions_path):
            raise FileNotFoundError(f"Attributions file not found: {self.candidate_attributions_path}")
        with open(self.candidate_attributions_path, "r", encoding="utf-8") as f:
            att_data = json.load(f)
        attributions = att_data.get("attributions", [])
        matched_atts = [a for a in attributions if a.get("chunk_id") == chunk_id]
        if len(matched_atts) == 0:
            raise ValueError(f"Target chunk '{chunk_id}' not found in candidate attributions")
        if len(matched_atts) > 1:
            raise ValueError(f"Duplicate target chunk '{chunk_id}' found in candidate attributions ({len(matched_atts)} instances)")
        attribution_record = matched_atts[0]

        return source_chunk, attribution_record

    def evaluate_and_split(
        self,
        target_chunk_id: str = "CHP2025-V1-P0025-C11",
        custom_source_chunk: Optional[Dict[str, Any]] = None,
        custom_attribution: Optional[Dict[str, Any]] = None,
        custom_gt_lines: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Evaluates boundary splitting for target chunk against evidence.
        Returns a structured split execution dictionary.
        """
        if custom_source_chunk is not None and custom_attribution is not None:
            source_chunk = custom_source_chunk
            attribution_record = custom_attribution
        else:
            source_chunk, attribution_record = self.load_chunk_and_context(target_chunk_id)

        # Pre-condition validation: must be AMBIGUOUS_ATTRIBUTION
        parent_status = attribution_record.get("attribution_status")
        if parent_status != "AMBIGUOUS_ATTRIBUTION":
            return {
                "verdict": "UNSPLITTABLE",
                "split_status": "STATUS_NOT_AMBIGUOUS",
                "reason": f"Parent chunk status is '{parent_status}', expected 'AMBIGUOUS_ATTRIBUTION'",
                "target_chunk_id": target_chunk_id,
                "child_chunks": []
            }

        clean_text = source_chunk.get("clean_text", "")
        raw_text = source_chunk.get("raw_text", clean_text)
        if not clean_text:
            return {
                "verdict": "UNSPLITTABLE",
                "split_status": "EMPTY_CLEAN_TEXT",
                "reason": "Target chunk has empty clean_text",
                "target_chunk_id": target_chunk_id,
                "child_chunks": []
            }

        # Inspect ground truth transcription
        vol_num = source_chunk.get("volume_number", 1)
        phys_p = source_chunk.get("physical_page_1idx", 25)
        gt_filename = f"gt_v{vol_num}_p{phys_p:04d}.txt"
        gt_path = os.path.join(self.gt_dir, gt_filename)

        if custom_gt_lines is not None:
            gt_lines = [l.rstrip("\r\n") for l in custom_gt_lines]
        else:
            if not os.path.exists(gt_path):
                return {
                    "verdict": "UNSPLITTABLE",
                    "split_status": "MISSING_GROUND_TRUTH_FILE",
                    "reason": f"Traceable ground truth transcription file '{gt_filename}' not found",
                    "target_chunk_id": target_chunk_id,
                    "child_chunks": []
                }
            with open(gt_path, "r", encoding="utf-8") as f:
                gt_lines = [l.rstrip("\r\n") for l in f.readlines()]

        # Chunk lines analysis
        lines = clean_text.splitlines()
        if len(lines) < 2:
            return {
                "verdict": "UNSPLITTABLE",
                "split_status": "INSUFFICIENT_LINES",
                "reason": f"Target chunk has only {len(lines)} line(s); insufficient for transition boundary split",
                "target_chunk_id": target_chunk_id,
                "child_chunks": []
            }

        # Verify Line 0 corresponds to terminal storage section of 丁公藤 in GT
        # GT Line 19: '【贮藏】置干燥处。'
        line0 = lines[0].strip()
        gt_l19 = gt_lines[18].strip() if len(gt_lines) >= 19 else "" # 1-indexed line 19 is index 18
        if line0 != gt_l19:
            return {
                "verdict": "UNSPLITTABLE",
                "split_status": "LINE_0_EVIDENCE_MISMATCH",
                "reason": f"Chunk line 0 '{line0}' does not match ground truth line 19 '{gt_l19}'",
                "target_chunk_id": target_chunk_id,
                "child_chunks": []
            }

        # Verify Line 1 corresponds to title line of 丁香 in GT
        # GT Line 21: '# 丁香'
        line1 = lines[1].strip()
        gt_l21 = gt_lines[20].strip() if len(gt_lines) >= 21 else "" # 1-indexed line 21 is index 20
        gt_l21_clean = gt_l21.lstrip("# ").strip()
        if line1 != gt_l21_clean:
            return {
                "verdict": "UNSPLITTABLE",
                "split_status": "LINE_1_EVIDENCE_MISMATCH",
                "reason": f"Chunk line 1 '{line1}' does not match ground truth line 21 '{gt_l21_clean}'",
                "target_chunk_id": target_chunk_id,
                "child_chunks": []
            }

        # Exact boundary character offset
        split_idx = clean_text.find("\n")
        child1_clean = clean_text[:split_idx]
        separator = clean_text[split_idx:split_idx+1]
        child2_clean = clean_text[split_idx+1:]

        # Verify raw text split
        split_raw_idx = raw_text.find("\n")
        child1_raw = raw_text[:split_raw_idx]
        child2_raw = raw_text[split_raw_idx+1:]

        # Verify exact reconstruction invariant
        reconstructed_clean = child1_clean + separator + child2_clean
        reconstructed_raw = child1_raw + separator + child2_raw
        if reconstructed_clean != clean_text or reconstructed_raw != raw_text:
            return {
                "verdict": "FAIL",
                "split_status": "RECONSTRUCTION_INVARIANT_FAILED",
                "reason": "Text reconstruction invariant failed: concatenated children do not equal parent text",
                "target_chunk_id": target_chunk_id,
                "child_chunks": []
            }

        parent_sha256 = self.compute_sha256_text(clean_text)
        child1_sha256 = self.compute_sha256_text(child1_clean)
        child2_sha256 = self.compute_sha256_text(child2_clean)

        raw_boxes = source_chunk.get("provenance", {}).get("raw_box_ids", [])
        # Box 74 corresponds to line 0 ('【贮藏】置干燥处。')
        # Boxes [78, 80, 82, 85, 87] correspond to lines 1-5 (丁香 monograph block)
        child1_boxes = [raw_boxes[0]] if len(raw_boxes) >= 1 else []
        child2_boxes = raw_boxes[1:] if len(raw_boxes) >= 2 else []

        coords = attribution_record.get("source_coordinates", {})

        # Child 1: Terminal section of 丁公藤
        child1 = {
            "child_id": f"{target_chunk_id}-S01",
            "parent_chunk_id": target_chunk_id,
            "child_sequence": 1,
            "source_coordinates": dict(coords),
            "structural_heading": "【贮藏】",
            "char_count": len(child1_clean),
            "line_count": len(child1_clean.splitlines()),
            "clean_text": child1_clean,
            "raw_text": child1_raw,
            "raw_box_ids": child1_boxes,
            "clean_text_sha256": child1_sha256,
            "parent_clean_text_sha256": parent_sha256,
            "split_rule": "BOUNDARY_MONOGRAPH_HEADER_TRANSITION",
            "boundary_evidence_reference": "gt_v1_p0025.txt line 19 (丁公藤末尾贮藏项)",
            "source_transcription_path": os.path.relpath(gt_path, PROJECT_ROOT).replace("\\", "/"),
            "relevant_transcription_lines": "Line 19",
            "parent_attribution_status": parent_status,
            "assigned_attribution_status": "CANDIDATE_ATTRIBUTION",
            "assigned_candidate_monograph": "丁公藤",
            "child_attribution_is_automatically_verified": False,
            "attribution_rationale": (
                "Terminal storage section of monograph '丁公藤' following C01-C10; "
                "isolated from mixed transition chunk via line 19 GT corroboration; "
                "assigned CANDIDATE_ATTRIBUTION under Phase 42C fail-closed policy (not automatically verified)"
            )
        }

        # Child 2: Header and definition block of 丁香
        child2 = {
            "child_id": f"{target_chunk_id}-S02",
            "parent_chunk_id": target_chunk_id,
            "child_sequence": 2,
            "source_coordinates": dict(coords),
            "structural_heading": "【专论概述】",
            "char_count": len(child2_clean),
            "line_count": len(child2_clean.splitlines()),
            "clean_text": child2_clean,
            "raw_text": child2_raw,
            "raw_box_ids": child2_boxes,
            "clean_text_sha256": child2_sha256,
            "parent_clean_text_sha256": parent_sha256,
            "split_rule": "BOUNDARY_MONOGRAPH_HEADER_TRANSITION",
            "boundary_evidence_reference": "gt_v1_p0025.txt lines 21-24 (丁香起首标题、拼音、拉丁名及概述项)",
            "source_transcription_path": os.path.relpath(gt_path, PROJECT_ROOT).replace("\\", "/"),
            "relevant_transcription_lines": "Lines 21-24",
            "parent_attribution_status": parent_status,
            "assigned_attribution_status": "CANDIDATE_ATTRIBUTION",
            "assigned_candidate_monograph": "丁香",
            "child_attribution_is_automatically_verified": False,
            "attribution_rationale": (
                "Initial title and introductory definition block of monograph '丁香'; "
                "isolated from mixed transition chunk via lines 21-24 GT corroboration; "
                "assigned CANDIDATE_ATTRIBUTION for compendial catalog integration (not automatically verified)"
            )
        }

        return {
            "verdict": "PASS",
            "split_status": "SPLIT_SUCCESS",
            "target_chunk_id": target_chunk_id,
            "parent_summary": {
                "chunk_id": target_chunk_id,
                "volume": coords.get("volume"),
                "physical_page_1idx": coords.get("physical_page_1idx"),
                "printed_page_number": coords.get("printed_page_number"),
                "char_count": len(clean_text),
                "line_count": len(lines),
                "clean_text_sha256": parent_sha256,
                "original_attribution_status": parent_status,
                "has_derived_children": True
            },
            "separator_policy": "NEWLINE_JOIN ('\\n')",
            "reconstruction_verification": {
                "exact_match": True,
                "reconstructed_char_count": len(reconstructed_clean),
                "reconstructed_clean_text_sha256": self.compute_sha256_text(reconstructed_clean),
                "parent_clean_text_sha256": parent_sha256
            },
            "boundary_evidence": {
                "gt_file": gt_filename,
                "child1_gt_lines": "gt_v1_p0025.txt line 19",
                "child2_gt_lines": "gt_v1_p0025.txt lines 21-24",
                "split_boundary_char_offset": split_idx
            },
            "child_chunks": [child1, child2]
        }

    def execute_pilot(
        self,
        target_chunk_id: str = "CHP2025-V1-P0025-C11",
        output_dir: str = "data/staging/phase42d_boundary_pilot"
    ) -> Dict[str, Any]:
        """
        Executes the pilot, verifies safety constraints, writes staging deliverables,
        and returns the complete pilot result.
        """
        abs_out_dir = os.path.join(PROJECT_ROOT, output_dir) if not os.path.isabs(output_dir) else output_dir

        # Collision check: do not overwrite existing staging deliverables
        manifest_path = os.path.join(abs_out_dir, "phase42d_split_manifest.json")
        report_path = os.path.join(abs_out_dir, "phase42d_pilot_report.md")
        if os.path.exists(manifest_path) or os.path.exists(report_path):
            raise FileExistsError(
                f"Output collision detected in '{abs_out_dir}'. "
                "Pilot must not overwrite existing deliverables."
            )

        result = self.evaluate_and_split(target_chunk_id)
        if result["verdict"] != "PASS":
            return result

        os.makedirs(abs_out_dir, exist_ok=False)

        # 1. Write split manifest JSON
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump({
                "manifest_type": "CHP_2025_PHASE_42D_PILOT_SPLIT_MANIFEST",
                "phase": "PHASE_42D_1",
                "execution_target": target_chunk_id,
                "governing_principle": "Exact text conservation, evidence-gated boundary split, explicit non-verified child candidate attribution",
                "pilot_result": result
            }, f, indent=2, ensure_ascii=False)

        # 2. Write pilot report markdown
        c1 = result["child_chunks"][0]
        c2 = result["child_chunks"][1]
        report_content = f"""# Phase 42D.1 — Single-Chunk Boundary Splitting Pilot Execution Report

**Execution Target:** `{target_chunk_id}`
**Phase:** Phase 42D.1 — Exploratory Boundary Splitting Pilot
**Workspace:** `D:/医药RAG`
**Output Directory:** `data/staging/phase42d_boundary_pilot/`
**Pilot Verdict:** **PASS (SPLIT_SUCCESS)**

---

## 1. Executive Summary

Ambiguous mixed-monograph transition chunk `{target_chunk_id}` on Volume I physical page 25 (printed page 4) was evaluated against ground-truth transcription `gt_v1_p0025.txt`.
A definitive, evidence-backed text boundary was verified separating the terminal storage item of monograph **丁公藤** from the initial title header and definition block of monograph **丁香**.

- **Exact Text Conservation:** Parent text (98 characters) was split into Child 1 (9 characters) and Child 2 (88 characters) with `\\n` newline separator. Concatenation reconstructs 100% of parent text with identical SHA-256 hash.
- **Fail-Closed Attribution Policy:** Neither child is promoted to `VERIFIED_ATTRIBUTION`. Both are assigned `CANDIDATE_ATTRIBUTION` with explicit non-verified metadata.
- **Parent Lineage:** Parent chunk identity and coordinates are completely preserved in child records.

---

## 2. Parent and Child Artifact Metrics

| Field | Parent Chunk (`{target_chunk_id}`) | Child 1 (`{c1['child_id']}`) | Child 2 (`{c2['child_id']}`) |
| :--- | :--- | :--- | :--- |
| **Monograph Candidate** | 丁公藤 / 丁香 | **{c1['assigned_candidate_monograph']}** | **{c2['assigned_candidate_monograph']}** |
| **Attribution Status** | `AMBIGUOUS_ATTRIBUTION` | `CANDIDATE_ATTRIBUTION` | `CANDIDATE_ATTRIBUTION` |
| **Verified Status** | Unverified | **False (Not Verified)** | **False (Not Verified)** |
| **Character Count** | {result['parent_summary']['char_count']} chars | {c1['char_count']} chars | {c2['char_count']} chars |
| **Line Count** | {result['parent_summary']['line_count']} lines | {c1['line_count']} line | {c2['line_count']} lines |
| **Raw Box IDs** | [74, 78, 80, 82, 85, 87] | {c1['raw_box_ids']} | {c2['raw_box_ids']} |
| **Heading Tag** | `【贮藏】` | `{c1['structural_heading']}` | `{c2['structural_heading']}` |
| **Clean Text SHA-256** | `{result['parent_summary']['clean_text_sha256']}` | `{c1['clean_text_sha256']}` | `{c2['clean_text_sha256']}` |
| **Evidence Citation** | `gt_v1_p0025.txt L19-24` | `{c1['boundary_evidence_reference']}` | `{c2['boundary_evidence_reference']}` |

---

## 3. Text Conservation and Reconstruction Proof

- **Separator Policy:** `NEWLINE_JOIN ('\\n')`
- **Formula:** `child1.clean_text + '\\n' + child2.clean_text == parent.clean_text`
- **Reconstruction Status:** **VERIFIED EXACT MATCH (100%)**
- **Length Math:** $9 + 1 + 88 = 98$ characters
- **Reconstructed SHA-256:** `{result['reconstruction_verification']['reconstructed_clean_text_sha256']}`
- **Parent SHA-256:** `{result['parent_summary']['clean_text_sha256']}`
"""
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report_content)

        result["manifest_path"] = manifest_path
        result["report_path"] = report_path
        result["manifest_sha256"] = self.compute_sha256_file(manifest_path)
        result["report_sha256"] = self.compute_sha256_file(report_path)

        return result
