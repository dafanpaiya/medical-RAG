# -*- coding: utf-8 -*-
"""
Header, Footer, and Watermark Detection & Filtering Module.
Uses normalized coordinates and regular expressions to identify non-body elements.
Maintains full traceability and never silently discards content.
"""

import re
from typing import Tuple, Optional, Dict, Any
from .models import RawOCRBox, LineClassification

WATERMARK_PATTERNS = [
    re.compile(r"扫描全能王", re.IGNORECASE),
    re.compile(r"3亿人都在用的扫描App", re.IGNORECASE),
    re.compile(r"CamScanner", re.IGNORECASE),
    re.compile(r"扫描王", re.IGNORECASE)
]

HEADER_PATTERNS = [
    re.compile(r"^\s*中国药典2025年版\s*$"),
    re.compile(r"^\s*·?\s*(一部|二部|三部|四部)\s*·?\s*$"),
    re.compile(r"^\s*中国药典\s*$")
]

FOOTER_PAGE_NUM_PATTERNS = [
    re.compile(r"^[.\s·:-]*([0-9]{1,4})[.\s·:-]*$"),
    re.compile(r"^(?:第\s*([0-9]+)\s*页)|(?:·\s*([0-9]+)\s*·)|(?:-\s*([0-9]+)\s*-)|(?:\.\s*([0-9]+)\s*[\.:])$")
]

def classify_line_noise(
    box: RawOCRBox,
    page_width: float,
    page_height: float,
    expected_printed_page: Optional[int] = None
) -> Tuple[LineClassification, Optional[Dict[str, Any]]]:
    """
    Classifies a raw text box into BODY, HEADER, FOOTER, WATERMARK, or AMBIGUOUS.
    Returns:
      (classification, detection_metadata)
    """
    text = box.text.strip()
    norm_y = box.norm_y_center
    norm_x = box.norm_x_center

    # 1. Check for Watermark signatures anywhere on page
    for pat in WATERMARK_PATTERNS:
        if pat.search(text):
            return LineClassification.WATERMARK, {
                "rule_id": "RULE_WM_001",
                "pattern": pat.pattern,
                "matched_text": text,
                "action": "FILTER_WATERMARK",
                "rationale": "Matched external scanner commercial promotional watermark.",
                "coordinates": box.box
            }

    # 2. Check for Header Candidates (Typically top 8% of page)
    if norm_y < 0.08:
        for pat in HEADER_PATTERNS:
            if pat.search(text):
                return LineClassification.HEADER, {
                    "rule_id": "RULE_HDR_001",
                    "pattern": pat.pattern,
                    "matched_text": text,
                    "action": "CLASSIFY_HEADER",
                    "rationale": "Matched Pharmacopoeia top running header pattern.",
                    "coordinates": box.box
                }

    # 3. Check for Footer Page Number Candidates (Typically bottom 8% of page)
    if norm_y > 0.92:
        for pat in FOOTER_PAGE_NUM_PATTERNS:
            m = pat.search(text)
            if m:
                detected_num = m.group(1) if m.group(1) else (m.group(2) if len(m.groups()) > 1 else None)
                return LineClassification.FOOTER, {
                    "rule_id": "RULE_FTR_001",
                    "pattern": pat.pattern,
                    "matched_text": text,
                    "detected_page_number": detected_num,
                    "expected_printed_page": expected_printed_page,
                    "action": "CLASSIFY_FOOTER",
                    "rationale": f"Matched bottom printed page number pattern (detected: {detected_num}).",
                    "coordinates": box.box
                }

    # 4. Check for edge ambiguous text
    if norm_y < 0.04 or norm_y > 0.96:
        # Near extreme edge but didn't match known patterns -> mark for review
        return LineClassification.AMBIGUOUS, {
            "rule_id": "RULE_AMB_001",
            "matched_text": text,
            "norm_y": norm_y,
            "action": "FLAG_FOR_REVIEW",
            "rationale": "Text located at extreme page edge; preserved but flagged for human inspection.",
            "coordinates": box.box
        }

    # Default: Main Body content
    return LineClassification.BODY, None
