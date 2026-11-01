import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.secure_qa_engine import SecureQAEngine

def test_answers():
    engine = SecureQAEngine()
    test_qs = [
        ("纯化水电导率", "中国药典2025纯化水电导率要求"),
        ("陈皮", "陈皮的药典标准与含量测定"),
        ("阿司匹林", "阿司匹林含量测定与游离水杨酸限度"),
        ("当归", "当归鉴别与功能主治"),
        ("茯苓", "茯苓性状与检查项"),
        ("甲硝唑", "甲硝唑有关物质要求"),
        ("奥美拉唑", "奥美拉唑肠溶胶囊释放度与耐酸力"),
        ("狂犬疫苗", "人用狂犬病疫苗质控标准与效价"),
        ("胶囊剂0103", "胶囊剂0103通则崩解时限与装量差异"),
        ("紫外分光0401", "紫外分光光度法0401检定要求与杂散光"),
        ("凌霄花", "凌霄花功能主治与含量测定")
    ]

    report = []
    for label, q in test_qs:
        res = engine.answer_query(q)
        cits = res.get("citations", [])
        top_cit = cits[0] if cits else {}
        report.append({
            "label": label,
            "query": q,
            "top_score": res.get("top_score", 0),
            "top_document": top_cit.get("document", "N/A"),
            "master_pdf": top_cit.get("master_physical_pdf", "N/A"),
            "pages": top_cit.get("pages", "N/A"),
            "answer_preview": res.get("answer", "")[:400]
        })

    with open("data/retrieval_verification_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("Successfully generated retrieval verification report!")

if __name__ == "__main__":
    test_answers()
