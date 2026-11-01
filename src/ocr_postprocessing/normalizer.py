# -*- coding: utf-8 -*-
"""
Pharmaceutical Terminology, Notation, and Typo Normalization Module.
Applies conservative, rule-governed corrections with full provenance records.
Protects numbers, formulas, and units; flags uncertain terms rather than guessing.
"""

import re
from typing import List, Tuple, Dict, Any, Optional
from .models import CorrectionRecord

# Explicitly verified pharmaceutical domain typo corrections
# Mapping: (pattern, replacement, rule_id, rationale)
EXPLICIT_TERM_RULES = [
    (
        re.compile(r"总葱醒"),
        "总蒽醌",
        "RULE_TERM_001",
        "Known OCR glyph confusion: botanical/chemical class '总蒽醌' (total anthraquinones) misread as '总葱醒'."
    ),
    (
        re.compile(r"维管策"),
        "维管束",
        "RULE_TERM_002",
        "Known OCR glyph confusion: plant anatomical term '维管束' (vascular bundle) misread as '维管策'."
    ),
    (
        re.compile(r"导管策"),
        "导管束",
        "RULE_TERM_003",
        "Known OCR glyph confusion: histological term '导管束' misread as '导管策'."
    ),
    (
        re.compile(r"皇星状"),
        "呈星状",
        "RULE_TERM_004",
        "Known OCR glyph confusion: descriptive anatomical phrase '呈星状' (radiating in star-shape) misread as '皇星状'."
    ),
    (
        re.compile(r"根蒸髓部"),
        "根茎髓部",
        "RULE_TERM_005",
        "Known OCR glyph confusion: botanical organ description '根茎髓部' (rhizome pith) misread as '根蒸髓部'."
    ),
    (
        re.compile(r"酚献指示液"),
        "酚酞指示液",
        "RULE_TERM_006",
        "Known OCR glyph confusion: chemical indicator '酚酞指示液' (phenolphthalein indicator solution) misread as '酚献指示液'."
    ),
    (
        re.compile(r"定[盘量]响雾剂"),
        "定量喷雾剂",
        "RULE_TERM_007",
        "Known OCR glyph confusion: formulation category '定量喷雾剂' (metered-dose sprays) misread as '定盘响雾剂'."
    ),
    (
        re.compile(r"非无[谢菌]药品"),
        "非无菌药品",
        "RULE_TERM_008",
        "Known OCR glyph confusion: pharmacopoeial category '非无菌药品' (non-sterile drugs) misread as '非无谢药品'."
    )
]

# Context-dependent scientific notation repairs
SCIENTIFIC_CONTEXT_RULES = [
    (
        # Vaccine bacterial concentration context only: 含菌6.0×10°/ml -> 含菌6.0×10^9/ml
        re.compile(r"(含菌\s*[0-9.]+\s*[×x]\s*)10[°o]\s*/\s*ml"),
        r"\g<1>10^9/ml",
        "RULE_SCI_001",
        "Vaccine concentration context: '含菌...×10°/ml' indicates bacterial count where superscript 9 was misread as degree symbol '°'."
    )
]

# OCR whitespace cleanup between Chinese characters
CHINESE_WHITESPACE_PAT = re.compile(r"([\u4e00-\u9fff])\s+([\u4e00-\u9fff])")

def normalize_text_line(
    raw_text: str,
    line_id: int
) -> Tuple[str, List[CorrectionRecord], List[str]]:
    """
    Normalizes an OCR text line using explicit, traceable rules.
    Returns:
      (clean_text, corrections_list, anomaly_flags)
    """
    clean = raw_text
    corrections: List[CorrectionRecord] = []
    anomaly_flags: List[str] = []

    # 1. Apply explicit domain terminology rules
    for pat, rep, rule_id, rationale in EXPLICIT_TERM_RULES:
        if pat.search(clean):
            before = clean
            clean = pat.sub(rep, clean)
            corrections.append(CorrectionRecord(
                original_text=before,
                corrected_text=clean,
                rule_id=rule_id,
                rationale=rationale,
                line_id=line_id
            ))

    # 2. Apply context-specific scientific notation repairs
    for pat, rep, rule_id, rationale in SCIENTIFIC_CONTEXT_RULES:
        if pat.search(clean):
            before = clean
            clean = pat.sub(rep, clean)
            corrections.append(CorrectionRecord(
                original_text=before,
                corrected_text=clean,
                rule_id=rule_id,
                rationale=rationale,
                line_id=line_id
            ))

    # 3. Clean stray whitespace between consecutive Chinese characters
    if CHINESE_WHITESPACE_PAT.search(clean):
        before = clean
        clean = CHINESE_WHITESPACE_PAT.sub(r"\1\2", clean)
        # Repeat once for 3-character sequences with multiple spaces
        clean = CHINESE_WHITESPACE_PAT.sub(r"\1\2", clean)
        if before != clean:
            corrections.append(CorrectionRecord(
                original_text=before,
                corrected_text=clean,
                rule_id=rule_id,
                rationale="Removed OCR-induced intra-character space between Chinese characters.",
                line_id=line_id
            ))

    # 4. Check for unhandled suspicious symbols that should NOT be blindly rewritten
    if "10°" in clean and "RULE_SCI_001" not in [c.rule_id for c in corrections]:
        # Unresolved 10° outside known context -> flag for review, preserve original!
        anomaly_flags.append("SUSPECTED_UNRESOLVED_SUPERSCRIPT_10_DEG")

    if re.search(r"[a-zA-Z0-9][°℃][a-zA-Z]", clean):
        anomaly_flags.append("SUSPECTED_EMBEDDED_DEGREE_GLYPH")

    return clean, corrections, anomaly_flags
