import os
import sys
import json
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import reportlab
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

from src.fulltext_chp_builder import get_chp_fulltext_documents
from src.fulltext_gmp_builder import get_gmp_and_regulatory_fulltext_documents
from src.fulltext_nmpa_fda_ich_builder import get_nmpa_fda_ich_fulltext_documents
from src.fulltext_clinical_and_validation_builder import get_clinical_and_validation_fulltext_documents
from src.fulltext_pharmacopoeia_water_and_solutions_builder import get_pharmacopoeia_water_and_solutions_fulltext_documents
from src.compile_bilingual_kb import compile_bilingual_knowledge_base
from src.expand_authentic_kb import expand_knowledge_base_with_pharmacopoeia_and_gmp

def sanitize_for_pdf(text: str) -> str:
    replacements = {
        r"\le": "<=", r"\ge": ">=", r"\pm": "+/-", r"\times": "x",
        r"\circ": " deg ", r"\mu": "u", r"\sigma": "sigma",
        r"\bar{X}": "X_bar", r"\sum": "sum", r"\sqrt": "sqrt",
        r"\frac": "", "$": "", "≤": "<=", "≥": ">=", "±": "+/-",
        "μ": "u", "°": " deg ", "—": "-", "–": "-", "“": '"', "”": '"',
        "‘": "'", "’": "'", "•": "*"
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

def generate_pdf_for_document(doc_title, text_content, pdf_path):
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=54, leftMargin=54,
        topMargin=54, bottomMargin=36
    )
    styles = getSampleStyleSheet()
    story = []

    # Title
    safe_title = sanitize_for_pdf(doc_title).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    story.append(Paragraph(safe_title, styles['Title']))
    story.append(Spacer(1, 14))

    # Paragraphs
    for para in text_content.split('\n\n'):
        p_clean = para.strip()
        if not p_clean:
            continue
        if p_clean.startswith('|'):
            # Table
            rows = [line.strip('|').split('|') for line in p_clean.split('\n') if not line.startswith('| :')]
            table_data = [[sanitize_for_pdf(c.strip()) for c in r] for r in rows]
            if table_data:
                t = Table(table_data)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#2563eb')),
                    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,-1), 8),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                    ('GRID', (0,0), (-1,-1), 0.5, colors.grey)
                ]))
                story.append(t)
                story.append(Spacer(1, 10))
        elif p_clean.startswith('#'):
            clean_heading = sanitize_for_pdf(p_clean.lstrip('#').strip()).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            story.append(Paragraph(clean_heading, styles['Heading2']))
            story.append(Spacer(1, 6))
        else:
            safe_text = sanitize_for_pdf(p_clean).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            story.append(Paragraph(safe_text, styles['Normal']))
            story.append(Spacer(1, 8))

    doc.build(story)

def run_master_fulltext_pipeline():
    print("=" * 80)
    print("ENTERPRISE PHARMACEUTICAL & REGULATORY FULL-TEXT RAG COMPILATION SPRINT")
    print("Jurisdictions: Chinese Pharmacopoeia (ChP), China GMP, NMPA, FDA, ICH, EU MDR")
    print("=" * 80)

    base_raw_dir = r"d:\医药RAG\data\raw\authentic_full_texts"
    kb_path = r"d:\医药RAG\data\enterprise_regulatory_kb.json"
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()

    # 1. Compile foundational and intermediate documents first
    compile_bilingual_knowledge_base()
    expand_knowledge_base_with_pharmacopoeia_and_gmp()
    with open(kb_path, "r", encoding="utf-8") as f:
        existing_kb = json.load(f)
    combined_docs = existing_kb.get("documents", [])
    existing_ids = {d["doc_id"] for d in combined_docs}

    # 2. Gather all full-text documents
    all_fulltext_doc_sets = [
        ("chp_2020", get_chp_fulltext_documents()),
        ("china_gmp", get_gmp_and_regulatory_fulltext_documents()),
        ("nmpa_fda_ich", get_nmpa_fda_ich_fulltext_documents()),
        ("clinical_and_validation", get_clinical_and_validation_fulltext_documents()),
        ("chp_water_and_solutions", get_pharmacopoeia_water_and_solutions_fulltext_documents())
    ]

    total_fulltext_docs = 0
    total_sections_added = 0
    total_pdfs_built = 0

    for category, doc_set in all_fulltext_doc_sets:
        for doc in doc_set:
            total_fulltext_docs += 1
            doc_id = doc["doc_id"]
            doc_title = doc["doc_title"]
            doc_title_zh = doc["doc_title_zh"]
            doc_title_en = doc["doc_title_en"]
            jurisdiction = doc["jurisdiction"]
            source_file = doc["source_file"]
            version = doc["version"]

            # Save full markdown document to raw folder
            folder_map = {
                "ChP": "chp_2020",
                "GMP": "china_gmp",
                "NMPA": "nmpa_regulations",
                "FDA": "fda_regulations",
                "ICH": "ich_guidelines",
                "EU_MDR": "eu_mdr"
            }
            target_subfolder = os.path.join(base_raw_dir, folder_map.get(jurisdiction, "nmpa_regulations"))
            os.makedirs(target_subfolder, exist_ok=True)
            raw_md_path = os.path.join(target_subfolder, source_file)

            full_md_content = f"# {doc_title_zh}\n## {doc_title_en}\n\n"
            for sec in doc["sections"]:
                full_md_content += f"### {sec['section_title']}\n\n{sec['content_zh']}\n\n"
                full_md_content += f"#### English Version: {sec['section_title_en']}\n\n{sec['content_en']}\n\n"

            with open(raw_md_path, "w", encoding="utf-8") as f:
                f.write(full_md_content)

            # Generate real PDF for each document in data/raw/
            pdf_filename = source_file.replace(".md", ".pdf")
            pdf_path = os.path.join(target_subfolder, pdf_filename)
            try:
                # Use English content for PDF generation to ensure ASCII/Latin-1 standard font compliance without font embedding errors
                full_pdf_content = f"{doc_title_en}\n\n"
                for sec in doc["sections"]:
                    full_pdf_content += f"Section: {sec['section_title_en']}\n\n{sec['content_en']}\n\n"
                generate_pdf_for_document(doc_title_en, full_pdf_content, pdf_path)
                total_pdfs_built += 1
            except Exception as e:
                print(f"[Warning] PDF generation skipped for {pdf_filename}: {e}")

            # Chunk sections into RAG database
            for sec in doc["sections"]:
                chunk_id = f"chunk_{doc_id}_{sec['section_id']}"
                if chunk_id in existing_ids:
                    continue

                primary_content = sec["content_en"] if jurisdiction in ("FDA", "ICH", "EU_MDR") else sec["content_zh"]
                combined_docs.append({
                    "doc_id": chunk_id,
                    "content": primary_content,
                    "content_zh": sec["content_zh"].strip(),
                    "content_en": sec["content_en"].strip(),
                    "metadata": {
                        "chunk_id": chunk_id,
                        "doc_title": doc_title,
                        "doc_title_zh": doc_title_zh,
                        "doc_title_en": doc_title_en,
                        "section_title": sec["section_title"],
                        "section_title_en": sec["section_title_en"],
                        "jurisdiction": jurisdiction,
                        "source_file": pdf_filename,
                        "version": version,
                        "is_latest": True,
                        "bilingual": True,
                        "pages": sec["pages"],
                        "type": "table" if "|" in sec["content_zh"] else "statutory_standard",
                        "created_at": now_iso,
                        "updated_at": now_iso
                    }
                })
                existing_ids.add(chunk_id)
                total_sections_added += 1

    # Save finalized comprehensive RAG database
    output_data = {
        "documents": combined_docs,
        "database_metadata": {
            "version": "Enterprise-FullText-v4",
            "compiled_at": now_iso,
            "total_chunks": len(combined_docs),
            "jurisdictions_covered": ["ChP", "GMP", "NMPA", "FDA", "ICH", "EU_MDR", "USP"]
        }
    }

    with open(kb_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 80)
    print("RAG DATABASE FULL-TEXT INGESTION COMPLETE!")
    print(f"Total Full-Text Regulatory Documents Processed: {total_fulltext_docs}")
    print(f"Real Multi-Page PDFs Generated in data/raw/: {total_pdfs_built}")
    print(f"Newly Added Authentic Statutory Sections: {total_sections_added}")
    print(f"Total Chunks in Enterprise Database: {len(combined_docs)}")
    print("=" * 80)

if __name__ == "__main__":
    run_master_fulltext_pipeline()
