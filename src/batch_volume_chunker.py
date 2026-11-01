# -*- coding: utf-8 -*-
"""
ChP 2025 Background Batch OCR & Progressive Chunking Pipeline
Extracts text from scanned pages of the 4 master physical PDFs,
performs layout & recursive semantic chunking, and appends into the vector database.
"""

import os
import sys
import json
import argparse
from typing import List, Dict, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.chp_pdf_ocr_service import ChPVolumeOCRService, VOL_FILENAMES, VOL_METADATA

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.path.join(BASE_DIR, "data", "enterprise_regulatory_kb.json")

def chunk_and_index_pages(vol_num: int, start_page: int, end_page: int, chunk_size: int = 600, chunk_overlap: int = 80):
    print(f"=== Starting Batch OCR & Chunking: Volume {vol_num} (Pages {start_page} to {end_page}) ===")
    ocr_service = ChPVolumeOCRService()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", "。", "；", " "]
    )

    vol_meta = VOL_METADATA.get(vol_num, {})
    vol_title = vol_meta.get("title", f"《中国药典》2025年版 第{vol_num}部")
    pdf_filename = VOL_FILENAMES.get(vol_num)

    new_chunks = []
    for pno in range(start_page, end_page + 1):
        print(f"Processing Vol {vol_num} Page {pno}...", end="", flush=True)
        page_text = ocr_service.get_page_text(vol_num, pno, dpi=130)
        if not page_text or len(page_text.strip()) < 20:
            print(f" [Skipped: empty or short ({len(page_text)} chars)]")
            continue

        raw_splits = text_splitter.split_text(page_text)
        print(f" [OCR: {len(page_text)} chars -> Generated {len(raw_splits)} chunks]")

        for s_idx, split_text in enumerate(raw_splits):
            c_id = f"chunk_chp2025_vol{vol_num}_p{pno:04d}_s{s_idx:02d}"
            new_chunks.append({
                "doc_id": c_id,
                "title": f"[{vol_title}] 第 {pno} 页 切片 #{s_idx+1}",
                "content": split_text,
                "content_zh": split_text,
                "content_en": split_text,
                "metadata": {
                    "chunk_id": c_id,
                    "document": vol_title,
                    "doc_title": vol_title,
                    "doc_title_zh": vol_title,
                    "doc_title_en": f"ChP 2025 Volume {vol_num}",
                    "section_title": f"第 {pno} 页扫描正文",
                    "jurisdiction": "ChP",
                    "category": "Pharmacopoeia_Scanned_Master",
                    "version": "2025-ChP-Full-Official",
                    "effective_date": "2025-10-01",
                    "is_latest": True,
                    "source_file": pdf_filename,
                    "master_physical_pdf": pdf_filename,
                    "physical_volume": f"第{vol_num}部",
                    "pages": [pno],
                    "type": "scanned_ocr_chunk",
                    "regulatory_authority": "国家药典委员会 / NMPA"
                }
            })

    if not new_chunks:
        print("No new chunks generated.")
        return 0

    # Load existing database and append
    if os.path.exists(DB_PATH):
        with open(DB_PATH, "r", encoding="utf-8") as f:
            kb_data = json.load(f)
    else:
        kb_data = {"documents": [], "embeddings": []}

    existing_ids = {d["doc_id"] for d in kb_data["documents"]}
    added_count = 0
    for chunk in new_chunks:
        if chunk["doc_id"] not in existing_ids:
            kb_data["documents"].append(chunk)
            kb_data["embeddings"].append([])
            existing_ids.add(chunk["doc_id"])
            added_count += 1

    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(kb_data, f, ensure_ascii=False, indent=2)

    print(f"\nSuccessfully added {added_count} new atomic chunks into {DB_PATH}!")
    print(f"Total chunks in vector database now: {len(kb_data['documents'])}")
    return added_count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ChP 2025 Scanned PDF Batch Chunker")
    parser.add_argument("--vol", type=int, default=1, choices=[1, 2, 3, 4], help="Volume number (1-4)")
    parser.add_argument("--start", type=int, default=0, help="Start page number (0-indexed)")
    parser.add_argument("--end", type=int, default=5, help="End page number (inclusive)")
    parser.add_argument("--chunk_size", type=int, default=600, help="Chunk size in characters")
    args = parser.parse_args()

    chunk_and_index_pages(args.vol, args.start, args.end, args.chunk_size)
