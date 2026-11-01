import fitz
import numpy as np
import time
import os
import multiprocessing as mp
from rapidocr_onnxruntime import RapidOCR

_worker_ocr = None
_worker_doc = None
_worker_pdf_path = None

def init_worker(pdf_path):
    global _worker_ocr, _worker_doc, _worker_pdf_path
    os.environ["OMP_NUM_THREADS"] = "1"
    os.environ["MKL_NUM_THREADS"] = "1"
    os.environ["OPENBLAS_NUM_THREADS"] = "1"
    _worker_ocr = RapidOCR(Global={'use_angle_cls': False})
    _worker_pdf_path = pdf_path
    _worker_doc = fitz.open(pdf_path)

def ocr_page_task(pno):
    global _worker_ocr, _worker_doc
    page = _worker_doc[pno]
    pix = page.get_pixmap(dpi=80)
    # direct numpy buffer without png encode/decode
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    res, _ = _worker_ocr(img)
    txt = "\n".join([l[1] for l in res]) if res else ""
    return pno, len(txt)

def main():
    pdf_path = r"data/raw/authentic_full_texts/chp_2025/《中国药典》2025年版 一部.pdf"
    tasks = list(range(10, 30))  # 20 pages
    t0 = time.time()
    with mp.Pool(processes=6, initializer=init_worker, initargs=(pdf_path,)) as pool:
        results = pool.map(ocr_page_task, tasks)
    total_time = time.time() - t0
    print(f"20 pages processed in {total_time:.2f}s ({len(tasks)/total_time:.2f} pages/sec)")
    for pno, l in results[:5]:
        print(f"  Page {pno}: {l} chars")

if __name__ == "__main__":
    main()
