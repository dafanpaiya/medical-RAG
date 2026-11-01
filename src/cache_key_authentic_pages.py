import fitz
import numpy as np
import os
import json
import time
from rapidocr_onnxruntime import RapidOCR

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw", "authentic_full_texts", "chp_2025")
CACHE_DIR = os.path.join(BASE_DIR, "data", "ocr_cache", "chp_2025")

VOL_FILES = {
    1: os.path.join(RAW_DIR, "《中国药典》2025年版 一部.pdf"),
    2: os.path.join(RAW_DIR, "《中国药典》2025年版 二部.pdf"),
    3: os.path.join(RAW_DIR, "《中国药典》2025年版 三部.pdf"),
    4: os.path.join(RAW_DIR, "《中国药典》2025年版 四部.pdf")
}

KEY_PAGES = {
    1: [0, 1, 12, 13, 14, 15, 16, 18, 19, 20, 21, 30, 50, 140, 250, 255, 280, 432, 433],
    2: [0, 1, 20, 28, 30, 35, 40],
    3: [0, 1, 10],
    4: [0, 1, 10, 20, 50, 100, 200]
}

def cache_authentic_pages():
    ocr = RapidOCR(Global={'use_angle_cls': False})
    for v, pages in KEY_PAGES.items():
        pdf_path = VOL_FILES[v]
        doc = fitz.open(pdf_path)
        vol_cache_dir = os.path.join(CACHE_DIR, f"vol{v}")
        os.makedirs(vol_cache_dir, exist_ok=True)
        print(f"Caching Volume {v} ({len(pages)} pages)...")
        for pno in pages:
            cache_file = os.path.join(vol_cache_dir, f"page_{pno:04d}.json")
            if os.path.exists(cache_file):
                continue
            pix = doc[pno].get_pixmap(dpi=75)
            img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
            t0 = time.time()
            res, _ = ocr(img)
            t_ocr = time.time() - t0
            lines = [l[1] for l in res] if res else []
            text = "\n".join(lines)
            cache_data = {
                "vol_num": v,
                "page_num": pno,
                "ocr_time_sec": round(t_ocr, 2),
                "char_count": len(text),
                "lines": lines,
                "text": text,
                "source_pdf": os.path.basename(pdf_path),
                "cached_at": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
            print(f"  Vol {v} P{pno}: {len(text)} chars in {t_ocr:.2f}s")
        doc.close()
    print("All key authentic pages cached!")

if __name__ == "__main__":
    cache_authentic_pages()
