# -*- coding: utf-8 -*-
"""
Authentic Full-Text Master Aggregator for Chinese Pharmacopoeia 2025 Edition (《中国药典》2025年版四部全集)
Statutory effective date: October 1, 2025 (Announcement No. 29 of 2025 by NMPA & NHC).
Systematically covers:
- Volume I (一部：中药材、饮片、中药提取物与成方制剂)
- Volume II (二部：化学药品、原料药与常用制剂)
- Volume III (三部：生物制品、血液制品、疫苗、重组治疗蛋白与单克隆抗体)
- Volume IV (四部：通用技术要求、制剂通则、检测方法、指导原则与药用辅料)
"""

from src.corpus_chp_2025_vol1 import CHP_2025_VOL1_DOCUMENTS
from src.corpus_chp_2025_vol2 import CHP_2025_VOL2_DOCUMENTS
from src.corpus_chp_2025_vol3 import CHP_2025_VOL3_DOCUMENTS
from src.corpus_chp_2025_vol4 import CHP_2025_VOL4_DOCUMENTS

ADDITIONAL_VOL4_CHAPTERS = [
    {
        "doc_id": "chp_2025_vol4_general_chapter_1101_1105",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 通则 1101 无菌检查法与通则 1105 微生物计数法",
        "doc_title_en": "ChP 2025 Vol IV General Chapters 1101 & 1105: Sterility Testing & Microbial Enumeration Tests",
        "version": "2025-ChP-Vol4-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol4_general_chapter_1101_1105_microbiology_full.pdf",
        "md_file": "chp_2025_vol4_general_chapter_1101_1105_microbiology_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_general_chapter_1101_1105_microbiology_full.pdf",
        "sections": [
            {
                "section_id": "chp_2025_vol4_1101_sec1_sterility_procedure",
                "page": 1,
                "title_zh": "第一节：通则 1101 无菌检查法法定规程与 14 天培养判定标准",
                "title_en": "Section 1: General Chapter 1101 Sterility Testing Procedure & 14-Day Incubation",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 通则 1101 无菌检查法\n\n"
                    "一、环境与人员要求：\n"
                    "无菌检查必须在 B 级背景下的 A 级单向流洁净台或经确认的隔离操作器（Isolator）内进行。日常必须监测空气沉降菌、浮游菌及手套表面微生物。\n\n"
                    "二、法定培养基与培养条件：\n"
                    "1. 硫乙醇酸盐流体培养基（FTM）：主要用于厌氧菌及需氧菌的培养。培养温度为 30℃ ~ 35℃。\n"
                    "2. 胰酪大豆胨液体培养基（TSB）：主要用于真菌及需氧菌的培养。培养温度为 20℃ ~ 25℃。\n\n"
                    "三、试验方法与培养观察：\n"
                    "1. 优先采用薄膜过滤法（孔径 <= 0.45 μm 滤膜）。\n"
                    "2. 培养时间：接种培养基后，必须连续培养不少于 14 天。在培养期间应定期观察培养基是否浑浊；培养至第 14 天确认无任何微生物生长，方可判定供试品符合无菌检查规定。"
                ),
                "content_en": (
                    "ChP 2025 General Chapter 1101: Sterility Testing\n\n"
                    "1. Controlled Environment: Conducted in Class A laminar flow hood within Class B cleanroom or in a qualified barrier isolator.\n"
                    "2. Media & Incubation Parameters:\n"
                    "- Fluid Thioglycollate Medium (FTM): Aerobic and anaerobic bacteria; incubated at 30-35 C.\n"
                    "- Soybean-Casein Digest Medium (TSB): Fungi and aerobic bacteria; incubated at 20-25 C.\n"
                    "3. Incubation Period: Not less than 14 days. Clear media with no microbial turbidity throughout 14 days certifies compliance."
                )
            },
            {
                "section_id": "chp_2025_vol4_1105_sec2_microbial_enumeration",
                "page": 2,
                "title_zh": "第二节：通则 1105 非无菌产品微生物限度计数法与菌数报告",
                "title_en": "Section 2: General Chapter 1105 Microbial Enumeration Tests (TAMC & TYMC)",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 通则 1105 非无菌产品微生物限度检查：微生物计数法\n\n"
                    "一、检测指标：\n"
                    "1. 需氧菌总数（Total Aerobic Microbial Count / TAMC）：采用胰酪大豆胨琼脂（TSA），30℃ ~ 35℃ 培养 3 ~ 5 天；水质检验采用 R2A 琼脂培养 5 天以上。\n"
                    "2. 霉菌和酵母菌总数（Total Combined Yeasts/Molds Count / TYMC）：采用沙氏葡萄糖琼脂（SDA），20℃ ~ 25℃ 培养 5 ~ 7 天。\n\n"
                    "二、结果报告与判定原则：\n"
                    "如限度规定为 100 CFU/ml，实测值 <= 200 CFU/ml 判定符合规定（可接受的最大菌数为规定限度的 2 倍，即 $2 \\times 10^2$ CFU/g 或 ml）。"
                ),
                "content_en": (
                    "ChP 2025 General Chapter 1105: Microbial Enumeration Tests\n\n"
                    "1. Test Parameters:\n"
                    "- Total Aerobic Microbial Count (TAMC): TSA at 30-35 C for 3-5 days (R2A for water systems >= 5 days).\n"
                    "- Total Combined Yeasts/Molds Count (TYMC): SDA at 20-25 C for 5-7 days.\n"
                    "2. Acceptance Criteria Interpretation: When criterion is 100 CFU/ml, maximum acceptable count is 200 CFU/ml (factor of 2)."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_general_chapter_1143",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 通则 1143 细菌内毒素检查法",
        "doc_title_en": "ChP 2025 Vol IV General Chapter 1143: Bacterial Endotoxins Test",
        "version": "2025-ChP-Vol4-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol4_general_chapter_1143_bacterial_endotoxins_full.pdf",
        "md_file": "chp_2025_vol4_general_chapter_1143_bacterial_endotoxins_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_general_chapter_1143_bacterial_endotoxins_full.pdf",
        "sections": [
            {
                "section_id": "chp_2025_vol4_1143_sec1_gel_and_photometric",
                "page": 1,
                "title_zh": "第一节：凝胶法、光度测定法与最大有效稀释倍数(MVD)计算",
                "title_en": "Section 1: Gel-Clot, Turbidimetric/Chromogenic Assays & MVD Calculation Formula",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 通则 1143 细菌内毒素检查法\n\n"
                    "一、方法分类与原理：\n"
                    "利用鲎试剂（Tachypleus Amebocyte Lysate / TAL）与内毒素产生凝集反应的机理。分为凝胶法（限量试验与半定量试验）和光度测定法（浊度法与显色基质生色法）。当有争议时，除各品种项下另有规定外，以凝胶法限量试验结果为准。\n\n"
                    "二、最大有效稀释倍数（MVD）法定计算公式：\n"
                    "$$MVD = \\frac{L \\times C}{\\lambda}$$\n"
                    "- $L$：供试品的细菌内毒素限值（如注射用水为 0.25 EU/ml；大容量注射剂按剂量公式 $L = K / M$ 计算，其中注射剂阈值 $K = 5.0\\text{ EU/kg/h}$）；\n"
                    "- $C$：供试品溶液的浓度（mg/ml 或 ml/ml）；\n"
                    "- $\\lambda$：鲎试剂标示灵敏度（EU/ml，凝胶法常采用 0.03、0.06、0.125 或 0.25 EU/ml）。\n\n"
                    "三、干扰试验要求：\n"
                    "使用新批号鲎试剂或供试品配方改变时，必须进行供试品干扰试验，确认供试品溶液在不大于 MVD 的稀释倍数下对鲎试剂无抑制或增强作用。"
                ),
                "content_en": (
                    "ChP 2025 General Chapter 1143: Bacterial Endotoxins Test\n\n"
                    "1. Methodologies: Gel-clot assay (official referee method), turbidimetric technique, and chromogenic technique using TAL/LAL lysate.\n"
                    "2. Maximum Valid Dilution (MVD) Formula:\n"
                    "MVD = (L * C) / lambda\n"
                    "where L is endotoxin limit (e.g. 0.25 EU/ml for WFI; K/M for drug products with K=5.0 EU/kg/h), C is concentration, and lambda is lysate sensitivity.\n"
                    "3. Inhibition/Enhancement Testing: Compulsory validation to confirm absence of interfering factors within working dilution range <= MVD."
                )
            }
        ]
    }
]

# Combined Master ChP 2025 Document Corpus covering all 4 Volumes
CHP_2025_DOCUMENTS = (
    CHP_2025_VOL1_DOCUMENTS +
    CHP_2025_VOL2_DOCUMENTS +
    CHP_2025_VOL3_DOCUMENTS +
    CHP_2025_VOL4_DOCUMENTS +
    ADDITIONAL_VOL4_CHAPTERS
)
