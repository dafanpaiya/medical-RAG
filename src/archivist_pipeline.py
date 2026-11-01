import pymupdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import json
import re

INPUT_PDF = r"d:\医药RAG\data\raw\mock_fda_guidance.pdf"
OUTPUT_DIR = r"d:\医药RAG\data\processed"

def table_to_markdown(table_data):
    if not table_data or len(table_data) < 1:
        return ""
    header = table_data[0]
    md_lines = []
    clean_header = [str(c or "").replace("\n", " ").strip() for c in header]
    md_lines.append("| " + " | ".join(clean_header) + " |")
    md_lines.append("| " + " | ".join(["---"] * len(clean_header)) + " |")

    for row in table_data[1:]:
        clean_row = [str(c or "").replace("\n", " ").strip() for c in row]
        while len(clean_row) < len(clean_header):
            clean_row.append("")
        md_lines.append("| " + " | ".join(clean_row) + " |")
    return "\n".join(md_lines)

def is_bbox_inside_table(bbox, table_bboxes):
    bx0, by0, bx1, by1 = bbox
    b_mid_x = (bx0 + bx1) / 2.0
    b_mid_y = (by0 + by1) / 2.0
    for tx0, ty0, tx1, ty1 in table_bboxes:
        if tx0 <= b_mid_x <= tx1 and ty0 <= b_mid_y <= ty1:
            return True
    return False

def extract_layout_aware_elements(pdf_path):
    doc = pymupdf.open(pdf_path)
    document_elements = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        page_height = page.rect.height

        tables = page.find_tables()
        table_bboxes = []
        table_items = []
        for t in tables.tables:
            table_bboxes.append(t.bbox)
            md_table = table_to_markdown(t.extract())
            table_items.append({
                "type": "table",
                "content": md_table,
                "bbox": t.bbox,
                "top": t.bbox[1],
                "page": page_num + 1
            })

        text_blocks = page.get_text("blocks")
        text_items = []
        for b in text_blocks:
            x0, y0, x1, y1, text, block_no, block_type = b

            # Header/footer cleaning
            if y0 < page_height * 0.08 and ("FDA" in text or "Guidance" in text):
                continue
            if y1 > page_height * 0.92 and "Page " in text:
                continue

            if is_bbox_inside_table((x0, y0, x1, y1), table_bboxes):
                continue

            cleaned_text = text.strip()
            if cleaned_text:
                text_items.append({
                    "type": "text",
                    "content": cleaned_text,
                    "bbox": (x0, y0, x1, y1),
                    "top": y0,
                    "page": page_num + 1
                })

        page_elements = sorted(text_items + table_items, key=lambda el: el["top"])
        document_elements.extend(page_elements)

    return document_elements

def build_atomic_chunks(elements, max_text_chunk_size=700):
    """
    World-Class Layout & Semantic Chunker:
    - Looks ahead: if a text element is a table title/caption preceding a table, binds it directly to the table.
    - Flushes narrative chunks along paragraph and sentence boundaries.
    - Preserves tables as self-contained markdown units.
    """
    chunks = []
    current_text_buffer = []
    current_pages = set()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_text_chunk_size,
        chunk_overlap=80,
        separators=["\n\n", "\n", ". ", " "]
    )

    def flush_text_buffer():
        nonlocal current_text_buffer, current_pages
        if current_text_buffer:
            buffer_text = "\n\n".join(current_text_buffer)
            for split_chunk in text_splitter.split_text(buffer_text):
                chunks.append({
                    "type": "narrative",
                    "content": split_chunk,
                    "pages": sorted(list(current_pages))
                })
            current_text_buffer = []
            current_pages = set()

    skip_indices = set()

    for i in range(len(elements)):
        if i in skip_indices:
            continue

        el = elements[i]

        # Lookahead: Check if this text block is a title/caption for the immediately following table
        if el["type"] == "text" and i + 1 < len(elements) and elements[i + 1]["type"] == "table":
            if re.match(r"^(Table|Figure|Exhibit|表|附表|图)\s*\d+[:\.\s]?", el["content"], re.IGNORECASE):
                # Flush existing narrative before this table
                flush_text_buffer()

                # Combine caption with the table
                table_el = elements[i + 1]
                combined_table_content = f"### {el['content']}\n\n{table_el['content']}"
                chunks.append({
                    "type": "table",
                    "content": combined_table_content,
                    "pages": sorted(list(set([el["page"], table_el["page"]])))
                })
                skip_indices.add(i + 1)
                continue

        if el["type"] == "table":
            flush_text_buffer()
            chunks.append({
                "type": "table",
                "content": el["content"],
                "pages": [el["page"]]
            })
        else:
            current_text_buffer.append(el["content"])
            current_pages.add(el["page"])
            current_len = sum(len(t) for t in current_text_buffer)
            if current_len >= max_text_chunk_size:
                flush_text_buffer()

    flush_text_buffer()
    return chunks

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("=== Running Layout-Aware Archivist Pipeline (v3: Lookahead Caption-Binding) ===")
    elements = extract_layout_aware_elements(INPUT_PDF)
    chunks = build_atomic_chunks(elements)

    print(f"Generated {len(chunks)} optimized chunks:\n")
    for idx, c in enumerate(chunks, 1):
        print(f"--- [Chunk {idx} | Type: {c['type']} | Page(s): {c['pages']}] ---")
        print(c["content"])
        print("-" * 50 + "\n")

    output_file = os.path.join(OUTPUT_DIR, "processed_chunks.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"Processed chunks saved to: {output_file}")
