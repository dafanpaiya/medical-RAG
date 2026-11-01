# -*- coding: utf-8 -*-
"""
Pharmacopoeia Structure Recognition and Semantic Candidate Chunking Module.
Partitions column-reconstructed text into structural chunks based on formal Pharmacopoeia headings.
Maintains heading-body cohesion, avoids arbitrary length cutoffs, and embeds full provenance metadata.
"""

import re
from typing import List, Dict, Any, Optional
from .models import ProcessedLine, CandidateChunk, LineClassification

# Standard Chinese Pharmacopoeia Monograph Structural Section Headings
CH_HEADING_PATTERNS = [
    re.compile(r"【来源】"),
    re.compile(r"【处方】"),
    re.compile(r"【制法】"),
    re.compile(r"【性状】"),
    re.compile(r"【鉴别】"),
    re.compile(r"【检查】"),
    re.compile(r"【浸出物】"),
    re.compile(r"【含量测定】"),
    re.compile(r"【炮制】"),
    re.compile(r"【性味与归经】"),
    re.compile(r"【功能与主治】"),
    re.compile(r"【用法与用量】"),
    re.compile(r"【注意】"),
    re.compile(r"【规格】"),
    re.compile(r"【贮藏】"),
    re.compile(r"【制剂】"),
    re.compile(r"【分子式与分子量】"),
    re.compile(r"【类别】")
]

# General chapter / Guideline hierarchical clause patterns
CLAUSE_HEADING_PATTERNS = [
    re.compile(r"^(?:[0-9]{4}\s+[^\n]+)"),             # e.g., "0112 喷雾剂"
    re.compile(r"^(?:[一二三四五六七八九十]+、\s*[^\n]+)"), # e.g., "一、 原料要求"
    re.compile(r"^(?:（[一二三四五六七八九十]+）\s*[^\n]+)")
]

def is_structural_heading(text: str) -> Optional[str]:
    """Checks if text contains or matches a formal Pharmacopoeia structural heading."""
    stripped = text.strip()
    for pat in CH_HEADING_PATTERNS:
        m = pat.search(stripped)
        if m:
            return m.group(0)
    for pat in CLAUSE_HEADING_PATTERNS:
        m = pat.match(stripped)
        if m:
            return m.group(0).strip()
    return None

def build_candidate_chunks(
    processed_lines: List[ProcessedLine],
    monograph_name: str,
    volume: str,
    source_pdf: str,
    physical_page: int,
    printed_page: Optional[int]
) -> List[CandidateChunk]:
    """
    Groups processed lines (in reconstructed reading order) into semantic chunks.
    Filters out headers, footers, and watermarks from chunk body, but retains their metadata.
    """
    chunks: List[CandidateChunk] = []

    # Filter for body and structural heading lines only
    body_lines = [
        l for l in processed_lines
        if l.classification not in (LineClassification.HEADER, LineClassification.FOOTER, LineClassification.WATERMARK)
    ]

    if not body_lines:
        return chunks

    current_section = "【专论概述】"
    current_lines: List[ProcessedLine] = []
    section_index = 0

    def flush_chunk():
        nonlocal section_index, current_lines, current_section
        if not current_lines:
            return

        raw_text_block = "\n".join(l.raw_text for l in current_lines)
        clean_text_block = "\n".join(l.clean_text for l in current_lines)
        box_ids = [l.raw_box_id for l in current_lines]

        all_corrections = []
        for l in current_lines:
            for c in l.corrections:
                all_corrections.append({
                    "original": c.original_text,
                    "corrected": c.corrected_text,
                    "rule_id": c.rule_id,
                    "rationale": c.rationale,
                    "line_id": c.line_id
                })

        all_anomalies = []
        for l in current_lines:
            all_anomalies.extend(l.anomaly_flags)

        chunk_id = f"chunk_chp2025_{volume}_p{physical_page:04d}_s{section_index:02d}"

        chunk = CandidateChunk(
            chunk_id=chunk_id,
            volume=volume,
            monograph=monograph_name,
            section_heading=current_section,
            source_pdf=source_pdf,
            physical_page=physical_page,
            printed_page=printed_page,
            content_raw=raw_text_block,
            content_clean=clean_text_block,
            source_box_ids=box_ids,
            line_count=len(current_lines),
            char_count=len(clean_text_block),
            corrections_applied=all_corrections,
            anomaly_flags=list(set(all_anomalies)),
            metadata={
                "jurisdiction": "ChP",
                "edition": "2025",
                "document": f"《中国药典》2025年版 {volume}",
                "doc_title": f"《中国药典》2025年版 {volume}",
                "monograph": monograph_name,
                "section_heading": current_section,
                "physical_page": physical_page,
                "printed_page": printed_page,
                "candidate_status": "DEMO_CANDIDATE_UNVERIFIED",
                "is_table": any("表" in l.clean_text for l in current_lines)
            }
        )
        chunks.append(chunk)
        section_index += 1
        current_lines = []

    for line in body_lines:
        heading = is_structural_heading(line.clean_text)
        if heading and current_lines:
            # New section boundary encountered
            flush_chunk()
            current_section = heading
            current_lines.append(line)
        elif heading:
            current_section = heading
            current_lines.append(line)
        else:
            current_lines.append(line)

    # Flush final remaining lines
    flush_chunk()

    return chunks
