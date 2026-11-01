import fitz
import numpy as np
import time
import os
import json
import re
import multiprocessing as mp
from rapidocr_onnxruntime import RapidOCR

_worker_ocr = None
_worker_doc = None

def init_worker(pdf_path):
    global _worker_ocr, _worker_doc
    os.environ["OMP_NUM_THREADS"] = "1"
    _worker_ocr = RapidOCR(Global={'use_angle_cls': False})
    _worker_doc = fitz.open(pdf_path)

def ocr_page(pno):
    global _worker_ocr, _worker_doc
    page = _worker_doc[pno]
    pix = page.get_pixmap(dpi=80)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    res, _ = _worker_ocr(img)
    lines = [l[1] for l in res] if res else []
    return pno, lines

def scan_vol1_toc():
    pdf_path = r"data/raw/authentic_full_texts/chp_2025/《中国药典》2025年版 一部.pdf"
    pages = list(range(17, 28))
    t0 = time.time()
    with mp.Pool(processes=6, initializer=init_worker, initargs=(pdf_path,)) as pool:
        results = pool.map(ocr_page, pages)
    print(f"Scanned {len(pages)} TOC pages of Vol 1 in {time.time()-t0:.2f}s")

    vol1_toc = {}
    for pno, lines in results:
        vol1_toc[pno] = lines

    with open("data/vol1_toc_full.json", "w", encoding="utf-8") as f:
        json.dump(vol1_toc, f, ensure_ascii=False, indent=2)
    print("Saved to data/vol1_toc_full.json")

if __name__ == "__main__":
    scan_vol1_toc()
