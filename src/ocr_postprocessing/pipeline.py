# -*- coding: utf-8 -*-
"""
Pharmacopoeia OCR Post-Processing and Chunking Pipeline.
Integrates parsing, noise filtering, dynamic column reconstruction,
traceable terminology normalization, and structural semantic chunking.
"""

import os
import json
import logging
from typing import Dict, Any, List, Optional
from .models import (
    RawOCRBox, ProcessedLine, CandidateChunk, LayoutAnalysis,
    LineClassification, LayoutType
)
from .parser import load_ocr_json_file, parse_ocr_payload
from .layout_detector import detect_page_layout, reconstruct_reading_order
from .noise_filter import classify_line_noise
from .normalizer import normalize_text_line
from .chunker import build_candidate_chunks

logger = logging.getLogger(__name__)

class PharmacopoeiaPostProcessor:
    """End-to-end post-processor for Pharmacopoeia OCR outputs."""

    def __init__(self):
        pass

    def process_file(self, filepath: str) -> Dict[str, Any]:
        """Processes an OCR JSON file and returns structured results."""
        metadata, dims, raw_boxes = load_ocr_json_file(filepath)
        return self._execute_pipeline(metadata, dims, raw_boxes)

    def process_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Processes an in-memory OCR JSON dictionary."""
        metadata, dims, raw_boxes = parse_ocr_payload(payload)
        return self._execute_pipeline(metadata, dims, raw_boxes)

    def _execute_pipeline(
        self,
        metadata: Dict[str, Any],
        dims: tuple,
        raw_boxes: List[RawOCRBox]
    ) -> Dict[str, Any]:
        page_width, page_height = dims
        page_coords = metadata.get("page_coordinates", {})
        volume = page_coords.get("volume") or metadata.get("volume", "一部")
        phys_p = page_coords.get("physical_page_1indexed") if page_coords.get("physical_page_1indexed") is not None else metadata.get("physical_page", 0)
        prt_p = page_coords.get("expected_printed_page") if page_coords.get("expected_printed_page") is not None else metadata.get("printed_page", None)
        monograph = page_coords.get("target_monograph") or metadata.get("target_monograph") or metadata.get("monograph", "未指定专论")
        master_pdf = metadata.get("master_pdf", {}).get("filename") or metadata.get("source_pdf", "unknown.pdf")

        # 1. Detect Layout (Dynamic Gutter Determination)
        layout: LayoutAnalysis = detect_page_layout(raw_boxes, page_width, page_height)

        # 2. Reconstruct Reading Order (Two-Column Dewarping)
        ordered_boxes, order_mapping = reconstruct_reading_order(raw_boxes, layout)

        # 3. Classify Noise & Normalize Terminology in Reconstructed Order
        processed_lines: List[ProcessedLine] = []
        filter_records: List[Dict[str, Any]] = []
        all_corrections: List[Dict[str, Any]] = []

        gutter_x = layout.gutter_x or (page_width / 2.0)

        for line_idx, box in enumerate(ordered_boxes):
            # Classify noise (header / footer / watermark / body)
            classification, noise_meta = classify_line_noise(
                box, page_width, page_height, expected_printed_page=prt_p
            )
            if noise_meta:
                filter_records.append({
                    "line_id": line_idx,
                    "box_id": box.box_id,
                    "raw_text": box.text,
                    **noise_meta
                })

            # Determine column ID
            if box.box_id in layout.cross_column_box_ids:
                col_id = None
            elif box.center_x < gutter_x:
                col_id = 0
            else:
                col_id = 1

            # Normalize terminology & scientific notation
            clean_text, line_corrections, anomaly_flags = normalize_text_line(box.text, line_idx)

            for c in line_corrections:
                all_corrections.append({
                    "line_id": line_idx,
                    "box_id": box.box_id,
                    "original": c.original_text,
                    "corrected": c.corrected_text,
                    "rule_id": c.rule_id,
                    "rationale": c.rationale
                })

            processed_line = ProcessedLine(
                line_id=line_idx,
                raw_box_id=box.box_id,
                raw_text=box.text,
                clean_text=clean_text,
                column_id=col_id,
                classification=classification,
                confidence=box.confidence,
                box=box.box,
                corrections=line_corrections,
                anomaly_flags=anomaly_flags
            )
            processed_lines.append(processed_line)

        # 4. Generate Semantic Candidate Chunks
        candidate_chunks = build_candidate_chunks(
            processed_lines=processed_lines,
            monograph_name=monograph,
            volume=volume,
            source_pdf=master_pdf,
            physical_page=phys_p,
            printed_page=prt_p
        )

        # 5. Formulate Before / After Comparison Texts
        # Before: Naive OCR line concatenation (Y-sorted raw boxes)
        naive_raw_text = "\n".join(b.text for b in sorted(raw_boxes, key=lambda x: x.box_id))

        # After: Column-reconstructed & cleaned body text
        reconstructed_body_lines = [
            l.clean_text for l in processed_lines
            if l.classification not in (LineClassification.HEADER, LineClassification.FOOTER, LineClassification.WATERMARK)
        ]
        reconstructed_clean_text = "\n".join(reconstructed_body_lines)

        # Assemble Output Result
        result = {
            "page_metadata": {
                "volume": volume,
                "monograph": monograph,
                "physical_page_1indexed": phys_p,
                "expected_printed_page": prt_p,
                "master_pdf": master_pdf,
                "dimensions": [page_width, page_height]
            },
            "layout_analysis": {
                "layout_type": layout.layout_type.value,
                "column_count": layout.column_count,
                "gutter_x": layout.gutter_x,
                "confidence": layout.confidence_score,
                "reasoning": layout.reasoning,
                "cross_column_count": len(layout.cross_column_box_ids),
                "left_column_count": len(layout.left_column_box_ids),
                "right_column_count": len(layout.right_column_box_ids)
            },
            "reading_order_traceability": {
                "raw_to_reconstructed_rank": order_mapping,
                "reconstructed_to_raw_id": {rank: b.box_id for rank, b in enumerate(ordered_boxes)}
            },
            "noise_filtering_records": filter_records,
            "terminology_corrections": all_corrections,
            "processed_lines": [
                {
                    "reconstructed_rank": l.line_id,
                    "raw_box_id": l.raw_box_id,
                    "raw_text": l.raw_text,
                    "clean_text": l.clean_text,
                    "column_id": l.column_id,
                    "classification": l.classification.value,
                    "confidence": l.confidence,
                    "box": l.box,
                    "anomaly_flags": l.anomaly_flags
                }
                for l in processed_lines
            ],
            "candidate_chunks": [
                {
                    "chunk_id": c.chunk_id,
                    "volume": c.volume,
                    "monograph": c.monograph,
                    "section_heading": c.section_heading,
                    "physical_page": c.physical_page,
                    "printed_page": c.printed_page,
                    "char_count": c.char_count,
                    "line_count": c.line_count,
                    "content_clean": c.content_clean,
                    "content_raw": c.content_raw,
                    "source_box_ids": c.source_box_ids,
                    "raw_box_ids": c.source_box_ids,
                    "corrections_applied": c.corrections_applied,
                    "anomaly_flags": c.anomaly_flags,
                    "metadata": c.metadata
                }
                for c in candidate_chunks
            ],
            "text_comparison": {
                "before_reconstruction_interleaved_snippet": naive_raw_text[:600] + ("..." if len(naive_raw_text) > 600 else ""),
                "after_reconstruction_clean_snippet": reconstructed_clean_text[:600] + ("..." if len(reconstructed_clean_text) > 600 else ""),
                "total_raw_chars": len(naive_raw_text),
                "total_clean_body_chars": len(reconstructed_clean_text),
                "chunks_generated": len(candidate_chunks)
            }
        }
        return result
