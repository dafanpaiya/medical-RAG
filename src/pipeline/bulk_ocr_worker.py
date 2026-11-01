# -*- coding: utf-8 -*-
"""
Bulk OCR Worker Module for Phase 43.5 Full Four-Volume Processing.
Designed for multiprocessing on Windows with thread clamping and atomic caching.
"""

import os
import sys
import time
import json
import traceback
from typing import Dict, Any, Tuple
import pymupdf
import numpy as np

# Ensure project root is in sys.path
_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _BASE_DIR not in sys.path:
    sys.path.insert(0, _BASE_DIR)

from src.ocr_postprocessing.worker import init_worker, get_worker_ocr


def worker_init_fn():
    """Initializer invoked once per worker process to pre-warm RapidOCR with clamped threads."""
    init_worker(intra_op=1, inter_op=1)


def ocr_page_task(task_args: Tuple[int, int, str, str, int]) -> Dict[str, Any]:
    """
    Executes or reuses OCR for a single physical page.
    Args:
        task_args: (volume, physical_page, pdf_path, ocr_cache_dir, dpi)
    Returns:
        Telemetry dict with status, timings, counts, and cache path.
    """
    volume, physical_page, pdf_path, ocr_cache_dir, dpi = task_args
    cache_path = os.path.join(ocr_cache_dir, f"vol{volume}", f"page_{physical_page:04d}.json")

    # 1. Fast cache check (idempotent / zero rework / strictly preserve existing cache)
    if os.path.exists(cache_path):
        try:
            if os.path.getsize(cache_path) > 10:
                with open(cache_path, "r", encoding="utf-8") as f:
                    cached_data = json.load(f)
                boxes = cached_data.get("bounding_boxes", [])
                return {
                    "volume_number": volume,
                    "physical_page_1idx": physical_page,
                    "status": "CACHED_REUSED",
                    "box_count": len(boxes),
                    "char_count": cached_data.get("char_count", sum(len(b.get("text", "")) for b in boxes)),
                    "render_time_sec": cached_data.get("render_time_sec", 0.0),
                    "ocr_time_sec": cached_data.get("ocr_time_sec", 0.0),
                    "total_time_sec": 0.0,
                    "cache_path": cache_path,
                    "error": None
                }
        except Exception:
            # If cache file is unreadable/corrupt, proceed to re-OCR and overwrite safely
            pass

    # 2. Live OCR Execution
    t_start = time.time()
    t_render = 0.0
    t_ocr = 0.0

    try:
        # Render PDF page
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        doc = pymupdf.open(pdf_path)
        p0 = physical_page - 1
        if p0 < 0 or p0 >= len(doc):
            doc.close()
            raise IndexError(f"Physical page {physical_page} out of bounds for Volume {volume} (total pages: {len(doc)})")

        page = doc[p0]
        t0 = time.time()
        pix = page.get_pixmap(dpi=dpi)
        img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
        t_render = round(time.time() - t0, 3)
        doc.close()

        # Run worker singleton RapidOCR
        ocr = get_worker_ocr()
        t1 = time.time()
        res, elapse = ocr(img)
        t_ocr = round(time.time() - t1, 3)

        bounding_boxes = []
        lines = []
        if res:
            for b_idx, item in enumerate(res):
                box_coords, text, conf = item
                text_clean = str(text).strip()
                lines.append(text_clean)
                bounding_boxes.append({
                    "box_id": b_idx,
                    "coordinates": box_coords,
                    "text": text_clean,
                    "confidence": round(float(conf), 4)
                })

        full_text = "\n".join(lines)
        t_total = round(time.time() - t_start, 3)

        payload = {
            "volume_number": volume,
            "physical_page_1idx": physical_page,
            "render_time_sec": t_render,
            "ocr_time_sec": t_ocr,
            "total_page_time_sec": t_total,
            "char_count": sum(len(b["text"]) for b in bounding_boxes),
            "lines": lines,
            "text": full_text,
            "bounding_boxes": bounding_boxes,
            "cached_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "cache_source": "phase43_5_live_bulk_ocr"
        }

        # Atomic write: write to .tmp then replace
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        tmp_path = f"{cache_path}.tmp_{os.getpid()}_{int(time.time()*1000)}"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)
        os.replace(tmp_path, cache_path)

        return {
            "volume_number": volume,
            "physical_page_1idx": physical_page,
            "status": "LIVE_OCR_SUCCESS",
            "box_count": len(bounding_boxes),
            "char_count": payload["char_count"],
            "render_time_sec": t_render,
            "ocr_time_sec": t_ocr,
            "total_time_sec": t_total,
            "cache_path": cache_path,
            "error": None
        }

    except Exception as exc:
        t_total = round(time.time() - t_start, 3)
        return {
            "volume_number": volume,
            "physical_page_1idx": physical_page,
            "status": "FAILED",
            "box_count": 0,
            "char_count": 0,
            "render_time_sec": t_render,
            "ocr_time_sec": t_ocr,
            "total_time_sec": t_total,
            "cache_path": cache_path,
            "error": f"{type(exc).__name__}: {str(exc)}\n{traceback.format_exc()}"
        }
