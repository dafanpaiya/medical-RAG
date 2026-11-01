import fitz
from rapidocr_onnxruntime import RapidOCR
import time, multiprocessing as mp

def ocr_single_page(args):
    pdf_path, pno = args
    ocr = RapidOCR()
    doc = fitz.open(pdf_path)
    page = doc[pno]
    pix = page.get_pixmap(dpi=100)
    img_bytes = pix.tobytes("png")
    doc.close()
    res, _ = ocr(img_bytes)
    txt = "\n".join([l[1] for l in res]) if res else ""
    return pno, len(txt)

def main():
    pdf_path = r"data/raw/authentic_full_texts/chp_2025/《中国药典》2025年版 一部.pdf"
    tasks = [(pdf_path, i) for i in range(10, 20)]
    t0 = time.time()
    with mp.Pool(8) as pool:
        results = pool.map(ocr_single_page, tasks)
    total_time = time.time() - t0
    print(f"10 pages processed in {total_time:.2f}s ({len(tasks)/total_time:.2f} pages/sec)")
    for pno, l in results:
        print(f"  Page {pno}: {l} chars")

if __name__ == "__main__":
    main()
