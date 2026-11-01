# -*- coding: utf-8 -*-
"""
Master Regulatory Knowledge Base Builder (2025-2026 Full-Text Edition)
Builds authentic, comprehensive, unabridged regulatory source documents for:
- ChP 2025 (《中国药典》2025年版，现行生效版，含膜法制水革新、9209微生物控制原则、纯化水与注射用水全项)
- NMPA (医疗器械软件2022第9号、网络安全2022第7号22项能力&SBOM、AI医疗器械2022/2023、739号令、GMP无菌附录)
- FDA (2023/2024 Cybersecurity Guidance Section 524B & SBOM, 2023 Software Functions Basic vs Enhanced, 2024/2026 QMSR ISO 13485, 21 CFR 11)
- EU MDR (Regulation 2017/745 Annex VIII Rule 11, MDCG 2019-11)
- ICH (ICH Q9(R1) 2023, ICH Q2(R2) 2023)
Generates authentic multi-page PDFs, markdown texts, and the unified enterprise JSON knowledge base.
"""

import os
import json
import fitz  # PyMuPDF
from typing import List, Dict, Any
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from src.corpus_chp_2025 import CHP_2025_DOCUMENTS
from src.corpus_nmpa_full import NMPA_FULL_DOCUMENTS
from src.corpus_fda_full import FDA_FULL_DOCUMENTS
from src.corpus_eu_ich_full import EU_ICH_FULL_DOCUMENTS

# Register Chinese Font for PDF generation
CHINESE_FONT_NAME = "Helvetica"
chinese_font_candidates = [
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\msyh.ttf",
    r"C:\Windows\Fonts\simsun.ttc",
    r"C:\Windows\Fonts\simsun.ttf",
    r"C:\Windows\Fonts\simhei.ttf"
]
for font_path in chinese_font_candidates:
    if os.path.exists(font_path):
        try:
            pdfmetrics.registerFont(TTFont("ChineseFont", font_path))
            CHINESE_FONT_NAME = "ChineseFont"
            break
        except Exception:
            pass

def generate_authentic_pdf(pdf_path: str, title: str, subtitle: str, sections: List[Dict[str, Any]]):
    """Generates an authentic multi-page PDF document using ReportLab."""
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName=CHINESE_FONT_NAME,
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#0f2b48'),
        alignment=1,
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName=CHINESE_FONT_NAME,
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#475569'),
        alignment=1,
        spaceAfter=12
    )
    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName=CHINESE_FONT_NAME,
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=8,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName=CHINESE_FONT_NAME,
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=5
    )

    story = [
        Paragraph(title, title_style),
        Paragraph(subtitle, subtitle_style),
        Spacer(1, 8)
    ]

    for idx, sec in enumerate(sections):
        if idx > 0 and sec.get("page", 1) > sections[idx-1].get("page", 1):
            story.append(PageBreak())

        sec_title = sec.get("title_zh") or sec.get("title", "")
        sec_text = sec.get("content_zh") or sec.get("text", "")
        sec_table = sec.get("table_data", None)

        if sec_title:
            story.append(Paragraph(sec_title, h2_style))
        if sec_text:
            for p in sec_text.split("\n\n"):
                p_clean = p.strip()
                if p_clean:
                    safe_p = p_clean.replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
                    story.append(Paragraph(safe_p, body_style))
        if sec_table:
            table_cells = []
            for row in sec_table:
                row_cells = []
                for cell in row:
                    safe_cell = str(cell).replace("<", "&lt;").replace(">", "&gt;")
                    row_cells.append(Paragraph(safe_cell, body_style))
                table_cells.append(row_cells)
            t = Table(table_cells, colWidths=[120] + [70] * (len(sec_table[0]) - 1))
            t.setStyle(TableStyle([
                ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
                ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#0f172a')),
                ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                ('FONTNAME', (0,0), (-1,-1), CHINESE_FONT_NAME),
                ('FONTSIZE', (0,0), (-1,-1), 8),
                ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ('TOPPADDING', (0,0), (-1,-1), 3),
                ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
            ]))
            story.append(t)
            story.append(Spacer(1, 6))

    doc.build(story)

def main():
    print("=" * 70)
    print("Starting Master 2025-2026 Regulatory Knowledge Base Build...")
    print("=" * 70)

    base_raw_dir = r"d:\医药RAG\data\raw\authentic_full_texts"
    os.makedirs(base_raw_dir, exist_ok=True)

    all_document_groups = [
        ("ChP_2025", CHP_2025_DOCUMENTS),
        ("NMPA", NMPA_FULL_DOCUMENTS),
        ("FDA", FDA_FULL_DOCUMENTS),
        ("EU_MDR_and_ICH", EU_ICH_FULL_DOCUMENTS)
    ]

    compiled_chunks = []
    total_docs_processed = 0

    for group_name, doc_list in all_document_groups:
        print(f"\nProcessing group: [{group_name}] ({len(doc_list)} authentic documents)...")
        for doc in doc_list:
            total_docs_processed += 1
            doc_id = doc["doc_id"]
            title_zh = doc["doc_title_zh"]
            title_en = doc["doc_title_en"]
            version = doc["version"]
            effective_date = doc["effective_date"]
            jurisdiction = doc["jurisdiction"]
            category = doc["category"]
            pdf_subpath = doc["pdf_subpath"]
            md_file = doc["md_file"]
            sections = doc["sections"]

            # 1. Output PDF
            pdf_path = os.path.join(base_raw_dir, pdf_subpath)
            subtitle_str = f"Official Legal Reference | Jurisdiction: {jurisdiction} | Version: {version} | Effective: {effective_date}"
            generate_authentic_pdf(pdf_path, title_zh, subtitle_str, sections)

            # 2. Verify PDF with PyMuPDF
            pdf_doc = fitz.open(pdf_path)
            page_count = len(pdf_doc)
            extracted_text = "".join(p.get_text() for p in pdf_doc)
            pdf_doc.close()
            assert page_count >= 1, f"PDF generation failed: {pdf_path} is empty"

            # 3. Output Markdown text
            md_path = os.path.join(os.path.dirname(pdf_path), md_file)
            md_content = f"# {title_zh}\n**English Title**: {title_en}  \n**Jurisdiction**: {jurisdiction} | **Version**: {version} | **Effective Date**: {effective_date}  \n**Source PDF**: [{os.path.basename(pdf_path)}]({pdf_path})  \n\n---\n\n"
            for s in sections:
                md_content += f"## {s.get('title_zh', '')}\n\n{s.get('content_zh', '')}\n\n"
                if s.get("table_data"):
                    md_content += "| " + " | ".join(s["table_data"][0]) + " |\n"
                    md_content += "| " + " | ".join([":---"] * len(s["table_data"][0])) + " |\n"
                    for row in s["table_data"][1:]:
                        md_content += "| " + " | ".join(row) + " |\n"
                    md_content += "\n"
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(md_content)

            # 4. Generate granular RAG chunks
            for sec in sections:
                chunk_id = f"chunk_{doc_id}_{sec['section_id']}"
                chunk_page = sec.get("page", 1)
                chunk_title_zh = sec.get("title_zh", "")
                chunk_title_en = sec.get("title_en", "")
                content_zh = sec.get("content_zh", "")
                content_en = sec.get("content_en", "")
                is_table = bool(sec.get("table_data"))

                compiled_chunks.append({
                    "doc_id": chunk_id,
                    "title": f"[{jurisdiction}] {title_zh} - {chunk_title_zh}",
                    "content": content_zh,
                    "content_zh": content_zh,
                    "content_en": content_en,
                    "metadata": {
                        "chunk_id": chunk_id,
                        "document": title_zh,
                        "doc_title": title_zh,
                        "doc_title_zh": title_zh,
                        "doc_title_en": title_en,
                        "section_title": chunk_title_zh,
                        "section_title_en": chunk_title_en,
                        "jurisdiction": jurisdiction,
                        "category": category,
                        "version": version,
                        "effective_date": effective_date,
                        "is_latest": True,
                        "source_file": os.path.basename(pdf_path),
                        "pdf_relative_path": pdf_subpath,
                        "pages": [chunk_page],
                        "type": "table" if is_table else "statutory_standard",
                        "regulatory_authority": jurisdiction
                    }
                })

            print(f"  -> Generated {os.path.basename(pdf_path)} ({page_count} pages), {len(sections)} chunks created.")

    # Save final enterprise knowledge base
    kb_path = r"d:\医药RAG\data\enterprise_regulatory_kb.json"
    kb_payload = {
        "documents": compiled_chunks,
        "embeddings": [[] for _ in compiled_chunks]
    }
    with open(kb_path, "w", encoding="utf-8") as f:
        json.dump(kb_payload, f, ensure_ascii=False, indent=2)


    print("\n" + "=" * 70)
    print(f"Master Regulatory Knowledge Base successfully built!")
    print(f"Total Authentic Documents Processed: {total_docs_processed}")
    print(f"Total Granular Chunks Generated: {len(compiled_chunks)}")
    print(f"Saved Database to: {kb_path}")
    print("=" * 70)

if __name__ == "__main__":
    main()
