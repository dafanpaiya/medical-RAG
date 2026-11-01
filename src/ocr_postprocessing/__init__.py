# -*- coding: utf-8 -*-
"""
Pharmacopoeia OCR Post-Processing & Structured Chunking Package.
"""

from .models import (
    RawOCRBox, ProcessedLine, CandidateChunk, LayoutAnalysis,
    LineClassification, LayoutType, CorrectionRecord
)
from .parser import load_ocr_json_file, parse_ocr_payload
from .layout_detector import detect_page_layout, reconstruct_reading_order
from .noise_filter import classify_line_noise
from .normalizer import normalize_text_line
from .chunker import build_candidate_chunks
from .pipeline import PharmacopoeiaPostProcessor
from .worker import init_worker, get_worker_ocr, configure_conservative_threading, get_worker_telemetry

__all__ = [
    "PharmacopoeiaPostProcessor",
    "init_worker",
    "get_worker_ocr",
    "configure_conservative_threading",
    "get_worker_telemetry",
    "RawOCRBox",
    "ProcessedLine",
    "CandidateChunk",
    "LayoutAnalysis",
    "LineClassification",
    "LayoutType",
    "CorrectionRecord",
    "load_ocr_json_file",
    "parse_ocr_payload",
    "detect_page_layout",
    "reconstruct_reading_order",
    "classify_line_noise",
    "normalize_text_line",
    "build_candidate_chunks"
]
