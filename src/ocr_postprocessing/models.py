# -*- coding: utf-8 -*-
"""
Data models for Pharmacopoeia OCR Post-Processing & Structured Chunking.
Preserves raw values, normalized values, classifications, and audit traceability.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Tuple
from enum import Enum

class LineClassification(str, Enum):
    BODY = "BODY"
    HEADER = "HEADER"
    FOOTER = "FOOTER"
    WATERMARK = "WATERMARK"
    CROSS_COLUMN_HEADING = "CROSS_COLUMN_HEADING"
    CROSS_COLUMN_TABLE = "CROSS_COLUMN_TABLE"
    AMBIGUOUS = "AMBIGUOUS"

class LayoutType(str, Enum):
    TWO_COLUMN = "TWO_COLUMN"
    SINGLE_COLUMN = "SINGLE_COLUMN"
    MIXED = "MIXED"
    FALLBACK = "FALLBACK"

@dataclass
class PageDimensions:
    width: float
    height: float

@dataclass
class CorrectionRecord:
    original_text: str
    corrected_text: str
    rule_id: str
    rationale: str
    line_id: int
    char_span: Optional[Tuple[int, int]] = None

@dataclass
class RawOCRBox:
    box_id: int
    text: str
    box: List[List[float]]  # 4 corner points [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    confidence: float
    x_min: float = 0.0
    x_max: float = 0.0
    y_min: float = 0.0
    y_max: float = 0.0
    width: float = 0.0
    height: float = 0.0
    center_x: float = 0.0
    center_y: float = 0.0
    norm_x_center: float = 0.0
    norm_y_center: float = 0.0

    def __post_init__(self):
        if self.box and len(self.box) >= 4:
            xs = [p[0] for p in self.box]
            ys = [p[1] for p in self.box]
            self.x_min = min(xs)
            self.x_max = max(xs)
            self.y_min = min(ys)
            self.y_max = max(ys)
            self.width = self.x_max - self.x_min
            self.height = self.y_max - self.y_min
            self.center_x = (self.x_min + self.x_max) / 2.0
            self.center_y = (self.y_min + self.y_max) / 2.0

@dataclass
class ProcessedLine:
    line_id: int
    raw_box_id: int
    raw_text: str
    clean_text: str
    column_id: Optional[int]  # 0: left column, 1: right column, None: cross-column/single
    classification: LineClassification
    confidence: float
    box: List[List[float]]
    corrections: List[CorrectionRecord] = field(default_factory=list)
    anomaly_flags: List[str] = field(default_factory=list)

@dataclass
class LayoutAnalysis:
    layout_type: LayoutType
    page_width: float
    page_height: float
    column_count: int
    gutter_x: Optional[float]
    left_column_bounds: Optional[Tuple[float, float]]
    right_column_bounds: Optional[Tuple[float, float]]
    cross_column_box_ids: List[int] = field(default_factory=list)
    left_column_box_ids: List[int] = field(default_factory=list)
    right_column_box_ids: List[int] = field(default_factory=list)
    confidence_score: float = 1.0
    reasoning: str = ""

@dataclass
class CandidateChunk:
    chunk_id: str
    volume: str
    monograph: str
    section_heading: str
    source_pdf: str
    physical_page: int
    printed_page: Optional[int]
    content_raw: str
    content_clean: str
    source_box_ids: List[int]
    line_count: int
    char_count: int
    corrections_applied: List[Dict[str, Any]]
    anomaly_flags: List[str]
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def raw_box_ids(self) -> List[int]:
        """Backward-compatible alias for source_box_ids."""
        return self.source_box_ids
