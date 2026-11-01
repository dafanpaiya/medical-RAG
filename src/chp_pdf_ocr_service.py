# -*- coding: utf-8 -*-
"""
ChP 2025 Authentic Physical Volume OCR & Processing Service
Handles layout-aware OCR extraction, caching, and text retrieval
for the 4 complete master scanned PDF volumes (4,353 pages total).
"""

import os
import json
import time
from typing import Dict, List, Optional, Any
import fitz  # PyMuPDF
from rapidocr_onnxruntime import RapidOCR

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHP_RAW_DIR = os.path.join(BASE_DIR, "data", "raw", "authentic_full_texts", "chp_2025")
OCR_CACHE_DIR = os.path.join(BASE_DIR, "data", "ocr_cache", "chp_2025")

VOL_FILENAMES = {
    1: "《中国药典》2025年版 一部.pdf",
    2: "《中国药典》2025年版 二部.pdf",
    3: "《中国药典》2025年版 三部.pdf",
    4: "《中国药典》2025年版 四部.pdf",
}

VOL_METADATA = {
    1: {
        "title": "《中华人民共和国药典》2025年版 一部",
        "scope": "中药材、中药饮片、中药提取物与成方制剂",
        "varieties": 3069,
        "filename": "《中国药典》2025年版 一部.pdf",
    },
    2: {
        "title": "《中华人民共和国药典》2025年版 二部",
        "scope": "化学药品、原料药与常用单味及复方制剂",
        "varieties": 2776,
        "filename": "《中国药典》2025年版 二部.pdf",
    },
    3: {
        "title": "《中华人民共和国药典》2025年版 三部",
        "scope": "生物制品、重组治疗蛋白、血液制品、单克隆抗体与疫苗",
        "varieties": 320,
        "filename": "《中国药典》2025年版 三部.pdf",
    },
    4: {
        "title": "《中华人民共和国药典》2025年版 四部",
        "scope": "通用技术要求、制剂通则、检验方法通则、指导原则与药用辅料",
        "varieties": 350,
        "filename": "《中国药典》2025年版 四部.pdf",
    },
}

class ChPVolumeOCRService:
    def __init__(self):
        self.ocr_engine = None  # Lazy initialize
        os.makedirs(OCR_CACHE_DIR, exist_ok=True)
        for v in [1, 2, 3, 4]:
            os.makedirs(os.path.join(OCR_CACHE_DIR, f"vol{v}"), exist_ok=True)

    def _get_ocr(self):
        if self.ocr_engine is None:
            self.ocr_engine = RapidOCR()
        return self.ocr_engine

    def get_pdf_path(self, vol_num: int) -> str:
        fname = VOL_FILENAMES.get(vol_num)
        if not fname:
            raise ValueError(f"Unknown volume number: {vol_num}")
        path = os.path.join(CHP_RAW_DIR, fname)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Pharmacopoeia Volume {vol_num} PDF not found at {path}")
        return path

    def get_volume_info(self, vol_num: int) -> Dict[str, Any]:
        pdf_path = self.get_pdf_path(vol_num)
        doc = fitz.open(pdf_path)
        page_count = len(doc)
        file_size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        doc.close()
        meta = VOL_METADATA.get(vol_num, {}).copy()
        meta.update({
            "vol_num": vol_num,
            "pdf_path": pdf_path,
            "total_pages": page_count,
            "file_size_mb": round(file_size_mb, 2),
            "is_scanned": True,
        })
        return meta

    def get_cache_path(self, vol_num: int, page_num: int) -> str:
        return os.path.join(OCR_CACHE_DIR, f"vol{vol_num}", f"page_{page_num:04d}.json")

    def get_page_text(self, vol_num: int, page_num: int, dpi: int = 150) -> str:
        cache_file = self.get_cache_path(vol_num, page_num)
        if os.path.exists(cache_file):
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("text", "")
            except Exception:
                pass

        # Perform OCR on page
        pdf_path = self.get_pdf_path(vol_num)
        doc = fitz.open(pdf_path)
        if page_num < 0 or page_num >= len(doc):
            doc.close()
            return ""

        page = doc[page_num]
        pix = page.get_pixmap(dpi=dpi)
        img_bytes = pix.tobytes("png")
        doc.close()

        ocr = self._get_ocr()
        t0 = time.time()
        result, elapse = ocr(img_bytes)
        t_ocr = time.time() - t0

        lines = [line[1] for line in result] if result else []
        text = "\n".join(lines)

        cache_data = {
            "vol_num": vol_num,
            "page_num": page_num,
            "ocr_time_sec": round(t_ocr, 2),
            "char_count": len(text),
            "lines": lines,
            "text": text,
            "cached_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)

        return text

    def extract_and_cache_range(self, vol_num: int, start_page: int, end_page: int, dpi: int = 120) -> List[Dict[str, Any]]:
        results = []
        for pno in range(start_page, end_page + 1):
            text = self.get_page_text(vol_num, pno, dpi=dpi)
            results.append({
                "vol_num": vol_num,
                "page_num": pno,
                "text": text,
                "length": len(text)
            })
        return results

    def get_all_volumes_overview(self) -> List[Dict[str, Any]]:
        overview = []
        for v in [1, 2, 3, 4]:
            try:
                info = self.get_volume_info(v)
                overview.append(info)
            except Exception as e:
                overview.append({"vol_num": v, "error": str(e)})
        return overview
