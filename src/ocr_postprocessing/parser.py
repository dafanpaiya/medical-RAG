# -*- coding: utf-8 -*-
"""
OCR JSON Parser and Raw Data Preservation.
Adapts to Pharmacopoeia OCR JSON format, validates structure, and computes normalized coordinates.
"""

import json
import logging
from typing import Dict, Any, List, Tuple, Optional
from .models import RawOCRBox, PageDimensions

logger = logging.getLogger(__name__)

def parse_ocr_payload(data: Dict[str, Any]) -> Tuple[Dict[str, Any], Tuple[float, float], List[RawOCRBox]]:
    """
    Parses OCR JSON dictionary.
    Returns:
      (metadata, (page_width, page_height), list_of_raw_boxes)
    """
    metadata = data.get("metadata", {})
    rendered_image = metadata.get("rendered_image", {})
    dims = rendered_image.get("dimensions", [0, 0])

    # Extract raw boxes
    raw_boxes_data = data.get("bounding_boxes", [])
    raw_lines = data.get("lines", [])

    # If dimensions not in rendered_image, estimate from max coordinates
    max_x, max_y = 0.0, 0.0
    for b in raw_boxes_data:
        box_pts = b.get("box", [])
        for pt in box_pts:
            if len(pt) >= 2:
                if pt[0] > max_x: max_x = pt[0]
                if pt[1] > max_y: max_y = pt[1]

    page_width = float(dims[0]) if (len(dims) >= 2 and dims[0] > 0) else (max_x + 50.0 if max_x > 0 else 1650.0)
    page_height = float(dims[1]) if (len(dims) >= 2 and dims[1] > 0) else (max_y + 50.0 if max_y > 0 else 2340.0)

    parsed_boxes: List[RawOCRBox] = []

    # Process each box
    for idx, item in enumerate(raw_boxes_data):
        text = item.get("text", "")
        box = item.get("box", [])
        conf = float(item.get("confidence", 0.0))

        if not text and not box:
            logger.warning("Empty OCR item at index %d skipped.", idx)
            continue

        raw_box = RawOCRBox(
            box_id=item.get("box_id", idx),
            text=text,
            box=box,
            confidence=conf
        )

        # Compute normalized coordinates
        if page_width > 0:
            raw_box.norm_x_center = round(raw_box.center_x / page_width, 5)
        if page_height > 0:
            raw_box.norm_y_center = round(raw_box.center_y / page_height, 5)

        parsed_boxes.append(raw_box)

    return metadata, (page_width, page_height), parsed_boxes

def load_ocr_json_file(filepath: str) -> Tuple[Dict[str, Any], Tuple[float, float], List[RawOCRBox]]:
    """Loads and parses an OCR JSON file from disk."""
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return parse_ocr_payload(data)
