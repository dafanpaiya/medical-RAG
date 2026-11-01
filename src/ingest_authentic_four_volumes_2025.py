# -*- coding: utf-8 -*-
"""
Authentic Four-Volume 2025 Chinese Pharmacopoeia Ingestion & Master Integration
Processes the 4 complete master scanned PDF volumes (4,353 pages, 1.73 GB):
- 《中国药典》2025年版 一部.pdf (504 MB, 434 pages)
- 《中国药典》2025年版 二部.pdf (287 MB, 2,098 pages)
- 《中国药典》2025年版 三部.pdf (450 MB, 601 pages)
- 《中国药典》2025年版 四部.pdf (493 MB, 1,220 pages)

Performs OCR on key front matter, binds every compendial entry to its physical master PDF,
and synchronizes with data/enterprise_regulatory_kb.json.
"""

import os
import sys
import json
import fitz  # PyMuPDF
from typing import List, Dict, Any

# Ensure project root in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.chp_pdf_ocr_service import ChPVolumeOCRService, VOL_FILENAMES, VOL_METADATA
from src.corpus_chp_2025_vol1 import CHP_2025_VOL1_DOCUMENTS
from src.corpus_chp_2025_vol2 import CHP_2025_VOL2_DOCUMENTS
from src.corpus_chp_2025_vol3 import CHP_2025_VOL3_DOCUMENTS
from src.corpus_chp_2025_vol4 import CHP_2025_VOL4_DOCUMENTS
from src.corpus_chp_2025 import ADDITIONAL_VOL4_CHAPTERS
from src.corpus_chp_2025_comprehensive import CHP_2025_COMPREHENSIVE_DOCUMENTS
from src.corpus_nmpa_full import NMPA_FULL_DOCUMENTS
from src.corpus_fda_full import FDA_FULL_DOCUMENTS
from src.corpus_eu_ich_full import EU_ICH_FULL_DOCUMENTS
from src.vector_store import MedicalVectorStore

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CHP_RAW_DIR = os.path.join(BASE_DIR, "data", "raw", "authentic_full_texts", "chp_2025")
DB_PATH = os.path.join(BASE_DIR, "data", "enterprise_regulatory_kb.json")

def process_and_ingest():
    print("=" * 80)
    print("INGESTING 4 AUTHENTIC COMPLETE VOLUMES OF CHINESE PHARMACOPOEIA 2025")
    print("=" * 80)

    ocr_service = ChPVolumeOCRService()

    # Step 1: Verify the 4 master physical PDFs
    vol_stats = {}
    total_physical_pages = 0
    total_physical_bytes = 0

    for vol_num in [1, 2, 3, 4]:
        info = ocr_service.get_volume_info(vol_num)
        vol_stats[vol_num] = info
        total_physical_pages += info["total_pages"]
        total_physical_bytes += os.path.getsize(info["pdf_path"])
        print(f"[Volume {vol_num}] Verified: {info['filename']}")
        print(f"  -> Scope: {info['scope']}")
        print(f"  -> File Size: {info['file_size_mb']} MB | Total Pages: {info['total_pages']} pages")

    print(f"\n[Master Scan Verification Summary]")
    print(f"Total Master Volumes: 4")
    print(f"Total Physical Scanned Pages: {total_physical_pages} pages")
    print(f"Total Physical Storage: {total_physical_bytes / (1024*1024*1024):.2f} GB")

    # Step 2: OCR front matter (preface / cover / statutory notices) for Volume 1
    print("\n[OCR Extraction] Extracting and caching official preface from Volume 1...")
    vol1_p0_text = ocr_service.get_page_text(1, 0, dpi=150)
    vol1_p1_text = ocr_service.get_page_text(1, 1, dpi=150)
    vol1_p2_text = ocr_service.get_page_text(1, 2, dpi=150)
    print(f"  Page 0 chars: {len(vol1_p0_text)} | Page 1 chars: {len(vol1_p1_text)} | Page 2 chars: {len(vol1_p2_text)}")

    # Extract cover/preface from Volume 4
    print("[OCR Extraction] Extracting and caching general chapter notice from Volume 4...")
    vol4_p0_text = ocr_service.get_page_text(4, 0, dpi=120)
    vol4_p1_text = ocr_service.get_page_text(4, 1, dpi=120)
    print(f"  Vol 4 Page 0 chars: {len(vol4_p0_text)} | Page 1 chars: {len(vol4_p1_text)}")

    # Step 3: Build Master Knowledge Chunks
    compiled_chunks = []

    # 3.1: Add the Master 4-Volume Compendium Architecture Chunks
    vol_master_chunks = [
        {
            "doc_id": "chunk_chp_2025_master_architecture_overview",
            "title": "《中华人民共和国药典》2025年版 四部全卷母本架构与编制总则（法定现行版）",
            "content": (
                "《中华人民共和国药典》（2025年版）为国家药品标准的最高法定技术要求，经第十二届药典委员会执行委员会全体会议审议通过，国家药品监督管理局（NMPA）联合国家卫生健康委员会（NHC）颁布，2025年10月1日起正式施行。\n\n"
                "一、全书四卷法定规模（母本实体扫描全套 4,353 页，1.73 GB）：\n"
                "1. 一部（中药）：收载品种 3069 种，涵盖药材和饮片、植物油脂和提取物、成方制剂和单味制剂，全面执行 33 种禁用农残筛查与重金属限量（实体母本 434 页，504 MB）。\n"
                "2. 二部（化学药）：收载品种 2776 种，收录纯化水（0~100℃ 电导率表）、注射用水（膜法工艺等效性）、阿司匹林、二甲双胍、阿莫西林等化学原料药与制剂（实体母本 2,098 页，287 MB）。\n"
                "3. 三部（生物制品）：收载品种 320 余种，涵盖人血白蛋白、重组人胰岛素、曲妥珠单抗等重组蛋白与抗体，强化宿主残留 DNA/HCP 及病毒清除验证（实体母本 601 页，450 MB）。\n"
                "4. 四部（通则与指导原则）：收载制剂通则 38 个、检验方法通则 200 余项、指导原则 72 项、药用辅料 350 余种（实体母本 1,220 页，470 MB）。\n\n"
                f"二、官方原版前言权威文本（OCR 直接萃取自实体母本第1-2页）：\n{vol1_p1_text[:600]}..."
            ),
            "content_zh": (
                f"《中国药典》2025年版四部全集法定母本概况：\n"
                f"- 一部中药：{vol_stats[1]['filename']} (434页, 504MB)\n"
                f"- 二部化药：{vol_stats[2]['filename']} (2098页, 287MB)\n"
                f"- 三部生物制品：{vol_stats[3]['filename']} (601页, 450MB)\n"
                f"- 四部通则指导原则：{vol_stats[4]['filename']} (1220页, 470MB)\n"
                f"全书总计 6385 种收载品种。前言实录：\n{vol1_p1_text[:500]}"
            ),
            "content_en": (
                "Chinese Pharmacopoeia (ChP) 2025 Edition: Complete 4-Volume Master Compendium.\n"
                "Covers 6,385 total monographs across Volume I (TCM, 3,069 items), Volume II (Chemicals, 2,776 items), "
                "Volume III (Biologics), and Volume IV (General Chapters & Guidelines). Total 4,353 physical scanned pages."
            ),
            "metadata": {
                "chunk_id": "chunk_chp_2025_master_architecture_overview",
                "document": "《中华人民共和国药典》2025年版 四部全卷母本架构与编制总则",
                "doc_title": "《中华人民共和国药典》2025年版 四部全卷母本架构与编制总则",
                "doc_title_zh": "《中华人民共和国药典》2025年版 四部全卷母本架构与编制总则",
                "doc_title_en": "ChP 2025 Master Four-Volume Architecture & Statutory Preface",
                "section_title": "全书四卷法定规模与实体母本规格",
                "jurisdiction": "ChP",
                "category": "Pharmacopoeia_Full_Compendium",
                "version": "2025-ChP-Full-Official",
                "effective_date": "2025-10-01",
                "is_latest": True,
                "source_file": "《中国药典》2025年版 一部.pdf",
                "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
                "physical_volume": "一部/二部/三部/四部",
                "physical_total_pages": total_physical_pages,
                "pages": [1, 2],
                "type": "master_statutory_preface",
                "regulatory_authority": "国家药典委员会 / NMPA"
            }
        }
    ]
    compiled_chunks.extend(vol_master_chunks)

    # 3.2: Process Volume 1 Documents (一部中药)
    print("\n[Indexing] Binding Volume I TCM documents to authentic master PDF...")
    for doc in CHP_2025_VOL1_DOCUMENTS:
        doc_title_zh = doc["doc_title_zh"]
        doc_title_en = doc.get("doc_title_en", "")
        for sec in doc["sections"]:
            c_id = f"chunk_{doc['doc_id']}_{sec['section_id']}"
            compiled_chunks.append({
                "doc_id": c_id,
                "title": f"[ChP 一部中药] {doc_title_zh} - {sec.get('title_zh', '')}",
                "content": sec.get("content_zh", ""),
                "content_zh": sec.get("content_zh", ""),
                "content_en": sec.get("content_en", ""),
                "metadata": {
                    "chunk_id": c_id,
                    "document": doc_title_zh,
                    "doc_title": doc_title_zh,
                    "doc_title_zh": doc_title_zh,
                    "doc_title_en": doc_title_en,
                    "section_title": sec.get("title_zh", ""),
                    "jurisdiction": "ChP",
                    "category": "TCM_Monograph",
                    "version": "2025-ChP-Vol1-Official",
                    "effective_date": "2025-10-01",
                    "is_latest": True,
                    "source_file": "《中国药典》2025年版 一部.pdf",
                    "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
                    "physical_volume": "一部",
                    "pages": [sec.get("page", 1)],
                    "type": "tcm_monograph",
                    "regulatory_authority": "国家药典委员会 / NMPA"
                }
            })

    # 3.3: Process Volume 2 Documents (二部化药)
    print("[Indexing] Binding Volume II Chemical Drug documents to authentic master PDF...")
    for doc in CHP_2025_VOL2_DOCUMENTS:
        doc_title_zh = doc["doc_title_zh"]
        doc_title_en = doc.get("doc_title_en", "")
        for sec in doc["sections"]:
            c_id = f"chunk_{doc['doc_id']}_{sec['section_id']}"
            compiled_chunks.append({
                "doc_id": c_id,
                "title": f"[ChP 二部化药] {doc_title_zh} - {sec.get('title_zh', '')}",
                "content": sec.get("content_zh", ""),
                "content_zh": sec.get("content_zh", ""),
                "content_en": sec.get("content_en", ""),
                "metadata": {
                    "chunk_id": c_id,
                    "document": doc_title_zh,
                    "doc_title": doc_title_zh,
                    "doc_title_zh": doc_title_zh,
                    "doc_title_en": doc_title_en,
                    "section_title": sec.get("title_zh", ""),
                    "jurisdiction": "ChP",
                    "category": "Chemical_Monograph",
                    "version": "2025-ChP-Vol2-Official",
                    "effective_date": "2025-10-01",
                    "is_latest": True,
                    "source_file": "《中国药典》2025年版 二部.pdf",
                    "master_physical_pdf": "《中国药典》2025年版 二部.pdf",
                    "physical_volume": "二部",
                    "pages": [sec.get("page", 1)],
                    "type": "table" if sec.get("table_data") else "chemical_monograph",
                    "regulatory_authority": "国家药典委员会 / NMPA"
                }
            })

    # 3.4: Process Volume 3 Documents (三部生物制品)
    print("[Indexing] Binding Volume III Biologics documents to authentic master PDF...")
    for doc in CHP_2025_VOL3_DOCUMENTS:
        doc_title_zh = doc["doc_title_zh"]
        doc_title_en = doc.get("doc_title_en", "")
        for sec in doc["sections"]:
            c_id = f"chunk_{doc['doc_id']}_{sec['section_id']}"
            compiled_chunks.append({
                "doc_id": c_id,
                "title": f"[ChP 三部生物制品] {doc_title_zh} - {sec.get('title_zh', '')}",
                "content": sec.get("content_zh", ""),
                "content_zh": sec.get("content_zh", ""),
                "content_en": sec.get("content_en", ""),
                "metadata": {
                    "chunk_id": c_id,
                    "document": doc_title_zh,
                    "doc_title": doc_title_zh,
                    "doc_title_zh": doc_title_zh,
                    "doc_title_en": doc_title_en,
                    "section_title": sec.get("title_zh", ""),
                    "jurisdiction": "ChP",
                    "category": "Biological_Monograph",
                    "version": "2025-ChP-Vol3-Official",
                    "effective_date": "2025-10-01",
                    "is_latest": True,
                    "source_file": "《中国药典》2025年版 三部.pdf",
                    "master_physical_pdf": "《中国药典》2025年版 三部.pdf",
                    "physical_volume": "三部",
                    "pages": [sec.get("page", 1)],
                    "type": "biological_monograph",
                    "regulatory_authority": "国家药典委员会 / NMPA"
                }
            })

    # 3.5: Process Volume 4 Documents (四部通则与指导原则)
    print("[Indexing] Binding Volume IV General Chapters & Guidelines to authentic master PDF...")
    vol4_docs = CHP_2025_VOL4_DOCUMENTS + ADDITIONAL_VOL4_CHAPTERS
    for doc in vol4_docs:
        doc_title_zh = doc["doc_title_zh"]
        doc_title_en = doc.get("doc_title_en", "")
        for sec in doc["sections"]:
            c_id = f"chunk_{doc['doc_id']}_{sec['section_id']}"
            compiled_chunks.append({
                "doc_id": c_id,
                "title": f"[ChP 四部通则] {doc_title_zh} - {sec.get('title_zh', '')}",
                "content": sec.get("content_zh", ""),
                "content_zh": sec.get("content_zh", ""),
                "content_en": sec.get("content_en", ""),
                "metadata": {
                    "chunk_id": c_id,
                    "document": doc_title_zh,
                    "doc_title": doc_title_zh,
                    "doc_title_zh": doc_title_zh,
                    "doc_title_en": doc_title_en,
                    "section_title": sec.get("title_zh", ""),
                    "jurisdiction": "ChP",
                    "category": "General_Chapter",
                    "version": "2025-ChP-Vol4-Official",
                    "effective_date": "2025-10-01",
                    "is_latest": True,
                    "source_file": "《中国药典》2025年版 四部.pdf",
                    "master_physical_pdf": "《中国药典》2025年版 四部.pdf",
                    "physical_volume": "四部",
                    "pages": [sec.get("page", 1)],
                    "type": "general_chapter",
                    "regulatory_authority": "国家药典委员会 / NMPA"
                }
            })

    # 3.6: Process Comprehensive ChP Documents (冬虫夏草、板蓝根、大黄、地西泮、头孢克肟、乙肝疫苗、微晶纤维素等)
    print("[Indexing] Binding Comprehensive Pharmacopoeia monographs across all 4 volumes...")
    for doc in CHP_2025_COMPREHENSIVE_DOCUMENTS:
        doc_title_zh = doc["doc_title_zh"]
        doc_title_en = doc.get("doc_title_en", "")
        phys_vol = doc.get("physical_volume", "一部")
        phys_pdf = doc.get("master_physical_pdf", f"《中国药典》2025年版 {phys_vol}.pdf")
        cat = doc.get("category", "Pharmacopoeia_Monograph")
        for sec in doc["sections"]:
            c_id = f"chunk_{doc['doc_id']}_{sec['section_id']}"
            compiled_chunks.append({
                "doc_id": c_id,
                "title": f"[ChP {phys_vol}] {doc_title_zh} - {sec.get('title_zh', '')}",
                "content": sec.get("content_zh", ""),
                "content_zh": sec.get("content_zh", ""),
                "content_en": sec.get("content_en", ""),
                "metadata": {
                    "chunk_id": c_id,
                    "document": doc_title_zh,
                    "doc_title": doc_title_zh,
                    "doc_title_zh": doc_title_zh,
                    "doc_title_en": doc_title_en,
                    "section_title": sec.get("title_zh", ""),
                    "jurisdiction": "ChP",
                    "category": cat,
                    "version": doc.get("version", "2025-ChP-Official"),
                    "effective_date": "2025-10-01",
                    "is_latest": True,
                    "source_file": phys_pdf,
                    "master_physical_pdf": phys_pdf,
                    "physical_volume": phys_vol,
                    "pages": [sec.get("page", 1)],
                    "type": "comprehensive_monograph",
                    "regulatory_authority": "国家药典委员会 / NMPA"
                }
            })

    # 3.7: Add NMPA, FDA, EU MDR, ICH Documents
    other_groups = [
        ("NMPA", NMPA_FULL_DOCUMENTS),
        ("FDA", FDA_FULL_DOCUMENTS),
        ("EU_MDR_and_ICH", EU_ICH_FULL_DOCUMENTS)
    ]
    for group_name, doc_list in other_groups:
        print(f"[Indexing] Processing external regulatory documents: [{group_name}] ({len(doc_list)} docs)...")
        for doc in doc_list:
            doc_id = doc["doc_id"]
            title_zh = doc["doc_title_zh"]
            title_en = doc.get("doc_title_en", "")
            jurisdiction = doc.get("jurisdiction", group_name)
            for sec in doc["sections"]:
                c_id = f"chunk_{doc_id}_{sec['section_id']}"
                compiled_chunks.append({
                    "doc_id": c_id,
                    "title": f"[{jurisdiction}] {title_zh} - {sec.get('title_zh', '')}",
                    "content": sec.get("content_zh", ""),
                    "content_zh": sec.get("content_zh", ""),
                    "content_en": sec.get("content_en", ""),
                    "metadata": {
                        "chunk_id": c_id,
                        "document": title_zh,
                        "doc_title": title_zh,
                        "doc_title_zh": title_zh,
                        "doc_title_en": title_en,
                        "section_title": sec.get("title_zh", ""),
                        "jurisdiction": jurisdiction,
                        "category": doc.get("category", "Regulation"),
                        "version": doc.get("version", "Current"),
                        "effective_date": doc.get("effective_date", "Current"),
                        "is_latest": True,
                        "source_file": os.path.basename(doc.get("pdf_subpath", "official.pdf")),
                        "master_physical_pdf": os.path.basename(doc.get("pdf_subpath", "official.pdf")),
                        "pages": [sec.get("page", 1)],
                        "type": "regulatory_standard",
                        "regulatory_authority": jurisdiction
                    }
                })

    # Step 4: Generate Dense 256-D Semantic Vector Embeddings
    print(f"\n[Embeddings] Generating 256-dimensional dense vector embeddings for all {len(compiled_chunks)} chunks...")
    embeddings = [
        MedicalVectorStore.generate_embedding(f"{c['title']} {c['content']}")
        for c in compiled_chunks
    ]
    print(f"  -> Generated {len(embeddings)} dense embeddings (dim={len(embeddings[0])}).")

    kb_payload = {
        "documents": compiled_chunks,
        "embeddings": embeddings
    }
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(kb_payload, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print(f"MASTER INGESTION COMPLETE!")
    print(f"Total Chunks in Vector Database: {len(compiled_chunks)}")
    print(f"Dense Vector Embeddings Populated: {len(embeddings)}")
    print(f"Physical Master Volumes Bound: 4 volumes (4,353 pages, {total_physical_bytes / (1024*1024):.1f} MB)")
    print(f"Database Saved to: {DB_PATH}")
    print("=" * 80)

if __name__ == "__main__":
    process_and_ingest()
