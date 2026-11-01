# -*- coding: utf-8 -*-
"""
Layout Analysis and Two-Column Reading-Order Reconstruction.
Dynamically detects column gutters based on geometric bounding-box distribution,
distinguishes full-width cross-column content, and orders text lines according to natural reading flow.
"""

import logging
from typing import List, Tuple, Dict, Any, Optional
from .models import RawOCRBox, LayoutAnalysis, LayoutType, LineClassification

logger = logging.getLogger(__name__)

def detect_page_layout(boxes: List[RawOCRBox], page_width: float, page_height: float) -> LayoutAnalysis:
    """
    Analyzes spatial distribution of bounding boxes to determine column layout.
    Does NOT hard-code fixed pixel values; uses dynamic statistical clustering.
    """
    if not boxes or len(boxes) < 4:
        return LayoutAnalysis(
            layout_type=LayoutType.SINGLE_COLUMN,
            page_width=page_width,
            page_height=page_height,
            column_count=1,
            gutter_x=None,
            left_column_bounds=None,
            right_column_bounds=None,
            confidence_score=0.5,
            reasoning="Too few text boxes to establish multi-column layout."
        )

    # 1. Identify cross-column elements (spanning significant width or across center)
    cross_column_ids = []
    column_candidates = []

    mid_min_x = page_width * 0.38
    mid_max_x = page_width * 0.62

    for b in boxes:
        # Cross column if width > 55% of page or spans across the middle region
        is_wide = b.width > (page_width * 0.55)
        crosses_center = (b.x_min < mid_min_x and b.x_max > mid_max_x)
        if is_wide or crosses_center:
            cross_column_ids.append(b.box_id)
        else:
            column_candidates.append(b)

    # If almost all elements are wide, it's a single column layout
    if len(column_candidates) < 6:
        return LayoutAnalysis(
            layout_type=LayoutType.SINGLE_COLUMN,
            page_width=page_width,
            page_height=page_height,
            column_count=1,
            gutter_x=None,
            left_column_bounds=(0.0, page_width),
            right_column_bounds=None,
            cross_column_box_ids=[b.box_id for b in boxes],
            confidence_score=0.9,
            reasoning=f"High proportion of full-width lines ({len(cross_column_ids)}/{len(boxes)}); classified as single-column."
        )

    # 2. Analyze X-centers of column candidates to detect two distinct clusters
    x_centers = sorted([b.center_x for b in column_candidates])

    # Candidate gutter search in central region (35% to 65% of page width)
    search_left = page_width * 0.35
    search_right = page_width * 0.65

    # Split candidates into left and right around candidate thresholds
    best_gutter = page_width * 0.50
    min_overlap = float("inf")
    found_split = False

    # Test candidate gutters at 1% intervals
    step = page_width * 0.01
    curr = search_left
    while curr <= search_right:
        left_sub = [b for b in column_candidates if b.center_x < curr]
        right_sub = [b for b in column_candidates if b.center_x >= curr]

        if len(left_sub) >= 4 and len(right_sub) >= 4:
            # Measure bounding box intrusions across the gutter
            left_intrusions = sum(1 for b in left_sub if b.x_max > curr + 5.0)
            right_intrusions = sum(1 for b in right_sub if b.x_min < curr - 5.0)
            total_intrusions = left_intrusions + right_intrusions

            # Prefer central gap with fewest intrusions
            balance_penalty = abs(len(left_sub) - len(right_sub)) * 0.1
            score = total_intrusions + balance_penalty

            if score < min_overlap:
                min_overlap = score
                best_gutter = curr
                found_split = True
        curr += step

    left_boxes = [b for b in column_candidates if b.center_x < best_gutter]
    right_boxes = [b for b in column_candidates if b.center_x >= best_gutter]

    if found_split and len(left_boxes) >= 5 and len(right_boxes) >= 5:
        left_x_min = min(b.x_min for b in left_boxes)
        left_x_max = max(b.x_max for b in left_boxes)
        right_x_min = min(b.x_min for b in right_boxes)
        right_x_max = max(b.x_max for b in right_boxes)

        # Refine gutter as midpoint between left column max and right column min
        refined_gutter = (left_x_max + right_x_min) / 2.0 if right_x_min > left_x_max else best_gutter

        return LayoutAnalysis(
            layout_type=LayoutType.TWO_COLUMN,
            page_width=page_width,
            page_height=page_height,
            column_count=2,
            gutter_x=round(refined_gutter, 2),
            left_column_bounds=(round(left_x_min, 2), round(left_x_max, 2)),
            right_column_bounds=(round(right_x_min, 2), round(right_x_max, 2)),
            cross_column_box_ids=cross_column_ids,
            left_column_box_ids=[b.box_id for b in left_boxes],
            right_column_box_ids=[b.box_id for b in right_boxes],
            confidence_score=0.92,
            reasoning=f"Detected clear two-column layout with dynamic gutter at X={refined_gutter:.1f} (Left: {len(left_boxes)} lines, Right: {len(right_boxes)} lines, Cross: {len(cross_column_ids)} lines)."
        )
    else:
        # Fallback to single-column conservative order
        return LayoutAnalysis(
            layout_type=LayoutType.FALLBACK,
            page_width=page_width,
            page_height=page_height,
            column_count=1,
            gutter_x=None,
            left_column_bounds=(0.0, page_width),
            right_column_bounds=None,
            cross_column_box_ids=[b.box_id for b in boxes],
            confidence_score=0.6,
            reasoning="Unimodal or insufficient separation for two columns; fallback to conservative vertical order."
        )

def reconstruct_reading_order(boxes: List[RawOCRBox], layout: LayoutAnalysis) -> Tuple[List[RawOCRBox], Dict[int, int]]:
    """
    Orders text boxes into natural human reading flow.
    Returns:
      (ordered_boxes, order_mapping: {raw_box_id: reconstructed_rank})
    """
    if layout.layout_type != LayoutType.TWO_COLUMN:
        # Single column or fallback: sort purely by Y (with slight tolerance on X for identical Y)
        sorted_boxes = sorted(boxes, key=lambda b: (b.y_min, b.x_min))
        mapping = {b.box_id: rank for rank, b in enumerate(sorted_boxes)}
        return sorted_boxes, mapping

    gutter_x = layout.gutter_x or (layout.page_width / 2.0)
    top_cross_thresh = layout.page_height * 0.15
    bottom_cross_thresh = layout.page_height * 0.90

    top_banners: List[RawOCRBox] = []
    bottom_footers: List[RawOCRBox] = []
    left_column: List[RawOCRBox] = []
    right_column: List[RawOCRBox] = []
    mid_cross: List[RawOCRBox] = []

    cross_set = set(layout.cross_column_box_ids)

    for b in boxes:
        if b.box_id in cross_set:
            if b.center_y < top_cross_thresh:
                top_banners.append(b)
            elif b.center_y > bottom_cross_thresh:
                bottom_footers.append(b)
            else:
                mid_cross.append(b)
        else:
            if b.center_x < gutter_x:
                left_column.append(b)
            else:
                right_column.append(b)

    # Sort each group vertically by y_min
    top_banners.sort(key=lambda b: b.y_min)
    left_column.sort(key=lambda b: b.y_min)
    right_column.sort(key=lambda b: b.y_min)
    mid_cross.sort(key=lambda b: b.y_min)
    bottom_footers.sort(key=lambda b: b.y_min)

    # Natural Pharmacopoeia Reading Order:
    # 1. Top headers / title banners
    # 2. Left column (top to bottom)
    # 3. Middle cross-column elements (if any, integrated between columns or at top of right)
    # 4. Right column (top to bottom)
    # 5. Bottom footers / page numbers
    ordered_boxes = top_banners + left_column + mid_cross + right_column + bottom_footers

    mapping = {b.box_id: rank for rank, b in enumerate(ordered_boxes)}
    return ordered_boxes, mapping
