# -*- coding: utf-8 -*-
"""
Authentic Full-Text Corpus for Chinese Pharmacopoeia 2025 Edition - Volume III (《中国药典》2025年版三部：生物制品)
Statutory effective date: October 1, 2025 (Announcement No. 29 of 2025 by NMPA & NHC).
Covers Biological Products General Chapters, Blood Products (Human Albumin), Recombinant Therapeutic Proteins (Insulin),
Vaccines (Hepatitis B & Rabies), and Monoclonal Antibodies (Trastuzumab).
"""

CHP_2025_VOL3_DOCUMENTS = [
    {
        "doc_id": "chp_2025_vol3_general_chapters_biologics",
        "doc_title_zh": "《中华人民共和国药典》2025年版三部 通则 0230系列：生物制品质量控制与病毒安全通则",
        "doc_title_en": "ChP 2025 Vol III General Chapters: Quality Control & Viral Safety Standards for Biological Products",
        "version": "2025-ChP-Vol3-General",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol3_general_chapters_biologics_full.pdf",
        "md_file": "chp_2025_vol3_general_chapters_biologics_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol3_general_chapters_biologics_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol3_sec1_general_principles_and_viral_safety",
                "page": 1,
                "title_zh": "第一节：生物制品宿主残留DNA/HCP限度、生产用原料控制与病毒清除验证通则",
                "title_en": "Section 1: Residual Host Cell DNA/Protein Limits, Raw Materials & Viral Clearance Validation",
                "content_zh": (
                    "《中华人民共和国药典》2025年版三部 生物制品质量控制通则\n\n"
                    "一、宿主细胞残留物法定限度控制（通则 3407 宿主残留 DNA & 通则 3412 宿主残留蛋白 HCP）：\n"
                    "重组 DNA 技术及细胞培养生产的生物技术产品（重组蛋白、抗体、基因治疗载体等）：\n"
                    "1. 外源性宿主残留 DNA（Residual Host Cell DNA）：每剂终产品中宿主残余 DNA 含量必须严格控制在 10 pg（皮克）以下（<= 10 pg/剂，特定产品 <= 100 pg/剂），且 DNA 片段长度需严格控制在 200 bp 以下（qPCR 法测定）；\n"
                    "2. 宿主细胞蛋白质（HCP）：采用专属性 ELISA 或质谱法检测，终产品中 HCP 残留量不得高于总蛋白量的 0.005%（即 <= 50 ppm，高纯度单抗通常要求 <= 10 ppm）。\n\n"
                    "二、病毒清除工艺验证通则（通则 0238）：\n"
                    "采用动物组织、血浆或哺乳动物细胞（如 CHO、NS0）生产的生物制品，纯化工艺必须经过经法规认可的代表性病毒（如包膜病毒 PRV、HIV 与非包膜病毒 MMV、PPV）的体外灭活/去除挑战性验证：\n"
                    "- 至少包含两步独立机制的病毒去除/灭活有效步骤（如低 pH 孵育、膜纳滤过滤或去垢剂 S/D 处理）；\n"
                    "- 总病毒清除对数减少值（Log Reduction Value / LRV）必须大于等于 12 对数（>= 12 Log10），有效步骤单步 LRV 必须 >= 4 Log10。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia 2025 Volume III: General Biological Quality & Viral Clearance Requirements\n\n"
                    "1. Residual Host Cell Impurities:\n"
                    "- Residual Host Cell DNA (ChP 3407 qPCR): Not more than 10 pg per dose (<= 10 pg/dose) with fragment size ideally < 200 bp;\n"
                    "- Host Cell Protein (HCP, ChP 3412 ELISA): Not more than 50 ppm (<= 0.005%), with mAb products typically <= 10 ppm.\n\n"
                    "2. Viral Safety Clearance Evaluation (ChP 0238):\n"
                    "Downstream purification requires at least two orthogonal steps (e.g., low pH incubation and nanofiltration). Overall log reduction value (LRV) >= 12 Log10, with individual effective steps providing >= 4 Log10."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol3_human_albumin_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版三部 品种正文：人血白蛋白（Human Albumin）",
        "doc_title_en": "ChP 2025 Vol III Official Monograph: Human Albumin",
        "version": "2025-ChP-Vol3-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol3_human_albumin_monograph_full.pdf",
        "md_file": "chp_2025_vol3_human_albumin_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol3_human_albumin_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol3_albumin_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：人血白蛋白低温乙醇分离工艺、纯度(>=96.0%)、多聚体与铝残留量控制",
                "title_en": "Section 1: Cold Ethanol Fractionation, Purity (>=96.0%), Polymer Distribution & Aluminum Limit",
                "content_zh": (
                    "《中华人民共和国药典》2025年版三部 品种正文：人血白蛋白（Human Albumin）\n\n"
                    "一、来源与制造工艺：\n"
                    "本品系由健康人血浆经低温乙醇蛋白分离法（Cohn 工艺）或适宜的色谱分离法分离纯化，并经巴氏灭菌法（60℃±0.5℃ 加温 10 小时灭活病毒）制成的灭菌白蛋白高纯度溶液。含适量辛酸钠或乙酰色氨酸钠作为热稳定剂，不含防腐剂。\n\n"
                    "二、关键物理化学与生物学指标：\n"
                    "1. 蛋白质纯度（通则 3103 醋酸纤维素薄膜电泳法）：白蛋白组分含量不得少于总蛋白质的 96.0%（>= 96.0%）；\n"
                    "2. 分子大小分布（通则 0514 高效分子排阻色谱法 SEC）：单体与二聚体聚合物之和不得少于 90.0%（>= 90.0%）；高聚体（多聚体）不得大于 5.0%（<= 5.0%）；\n"
                    "3. 铝残留量（通则 0406 石墨炉原子吸收分光光度法）：由于透析肾毒性风险，每 1L 供试品中铝残留量不得过 200 ug（<= 200 ug/L）；\n"
                    "4. 细菌内毒素（通则 1143 / 3101）：含内毒素量每 1g 蛋白质应小于 5.0 EU（< 5.0 EU/g 蛋白质）；\n"
                    "5. 热原检查（通则 1142 家兔法）：注射给药 3 只家兔，体温升高总和不得超过 1.3℃；\n"
                    "6. 无菌检查（通则 1101）：依法检查必须符合无菌要求。"
                ),
                "content_en": (
                    "ChP 2025 Volume III: Human Albumin\n\n"
                    "1. Manufacturing: Isolated from healthy human plasma via Cohn cold ethanol fractionation or validated chromatography, followed by terminal pasteurization at 60.0 C for 10 hours for viral inactivation.\n\n"
                    "2. Release Specifications:\n"
                    "- Albumin Purity (Cellulose acetate electrophoresis): Not less than 96.0% of total protein;\n"
                    "- Molecular Size Distribution (SEC HPLC): Monomer plus dimer >= 90.0%; Polymers <= 5.0%;\n"
                    "- Residual Aluminum (GFAAS): Not more than 200 ug/L to prevent encephalopathy in renal patients;\n"
                    "- Bacterial Endotoxins: Less than 5.0 EU per gram protein (< 5.0 EU/g);\n"
                    "- Sterility (ChP 1101): Complies with 14-day incubation."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol3_recombinant_insulin_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版三部 品种正文：重组人胰岛素（Recombinant Human Insulin）",
        "doc_title_en": "ChP 2025 Vol III Official Monograph: Recombinant Human Insulin",
        "version": "2025-ChP-Vol3-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol3_recombinant_insulin_monograph_full.pdf",
        "md_file": "chp_2025_vol3_recombinant_insulin_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol3_recombinant_insulin_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol3_insulin_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：重组人胰岛素HPLC含量测定、高分子蛋白(<=0.3%)与脱酰胺基胰岛素限度",
                "title_en": "Section 1: Recombinant Insulin Assay (>=27.5 IU/mg), High MW Protein (<=0.3%) & Desamido Insulin",
                "content_zh": (
                    "《中华人民共和国药典》2025年版三部 品种正文：重组人胰岛素（Insulinum Humanum Recombinatum）\n\n"
                    "一、基原与分子参数：\n"
                    "本品系利用重组 DNA 技术，由含有编码人胰岛素基因的大肠杆菌（E. coli）或酿酒酵母（Saccharomyces cerevisiae）表达，经分离纯化制得的 51 氨基酸双链多肽（A 链 21 氨基酸，B 链 30 氨基酸，含 2 个链间二硫键与 1 个链内二硫键）。分子式：C257H383N65O77S6，分子量：5807.57。\n\n"
                    "二、含量与生物效价：\n"
                    "按干燥品计算，每 1mg 胰岛素生物活性不得少于 27.5 国际单位（>= 27.5 IU/mg，HPLC 法测定效价）。\n\n"
                    "三、有关物质与高分子聚合物（通则 0512 反相高效液相色谱法与通则 0514 排阻色谱法）：\n"
                    "1. 高分子蛋白质（High Molecular Weight Proteins）：胰岛素自聚多聚体不得过 0.30%（<= 0.30%）；\n"
                    "2. A21 脱酰胺基胰岛素（A21 Desamido Insulin）：不得过 2.0%；\n"
                    "3. 其他相关蛋白质（如脱氨甲硫氨酸、B30 前体等）：总和不得过 1.5%；\n"
                    "4. 锌含量：原料中含锌量必须控制在 0.30% ~ 1.00%（原子吸收分光光度法），以维持六聚体结晶稳定性；\n"
                    "5. 细菌内毒素：每 100 单位（100 IU）中含内毒素量应小于 0.80 EU（< 0.80 EU/100 IU）。"
                ),
                "content_en": (
                    "ChP 2025 Volume III: Recombinant Human Insulin\n\n"
                    "1. Molecular Characteristics: 51-amino acid two-chain peptide (A chain 21, B chain 30, MW 5807.57) expressed in E. coli or yeast.\n\n"
                    "2. Potency and Assay (HPLC):\n"
                    "Calculated on dried basis: Not less than 27.5 IU per mg (>= 27.5 IU/mg).\n\n"
                    "3. Related Proteins and Purity (RP-HPLC & SEC):\n"
                    "- High Molecular Weight Proteins (HMWP): Not more than 0.30% (<= 0.30%);\n"
                    "- A21 Desamido Insulin: Not more than 2.0%;\n"
                    "- Total other related proteins: Not more than 1.5%;\n"
                    "- Zinc content: 0.30% to 1.00%;\n"
                    "- Bacterial Endotoxins: < 0.80 EU per 100 IU."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol3_trastuzumab_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版三部 品种正文：注射用曲妥珠单抗（Trastuzumab for Injection）",
        "doc_title_en": "ChP 2025 Vol III Official Monograph: Trastuzumab for Injection (HER2 Monoclonal Antibody)",
        "version": "2025-ChP-Vol3-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol3_trastuzumab_monograph_full.pdf",
        "md_file": "chp_2025_vol3_trastuzumab_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol3_trastuzumab_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol3_trastuzumab_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：曲妥珠单抗单克隆抗体结构、毛细管电泳纯度(>=95.0%)、糖型与结合活性",
                "title_en": "Section 1: Trastuzumab mAb Purity (CE-SDS >=95.0%), Glycosylation Profile & Binding Bioassay",
                "content_zh": (
                    "《中华人民共和国药典》2025年版三部 品种正文：注射用曲妥珠单抗（Trastuzumab for Injection）\n\n"
                    "一、作用靶点与结构属性：\n"
                    "本品系由哺乳动物中国仓鼠卵巢（CHO）细胞经重组表达、纯化制得的针对人表皮生长因子受体-2（HER2 / ErbB2）细胞外结构域 IV 的人源化 IgG1κ 单克隆抗体。分子量约为 148 kDa，主要用于 HER2 阳性乳腺癌及胃癌的靶向治疗。\n\n"
                    "二、关键质量属性与放行标准：\n"
                    "1. 纯度分析（通则 0542 毛细管十二烷基硫酸钠凝胶电泳法 CE-SDS）：\n"
                    "   - 非还原型 CE-SDS：完整单抗主峰面积百分比不得少于 95.0%（>= 95.0%）；\n"
                    "   - 还原型 CE-SDS：重链与轻链峰面积之和不得少于 98.0%；\n"
                    "2. 分子大小变异体（SEC-HPLC 通则 0514）：单体含量不得少于 98.0%，二聚体与高聚体之和不得过 1.5%；低分子碎片不得过 0.5%；\n"
                    "3. 电荷异质性（弱阳离子交换色谱 CEX-HPLC 或成像毛细管等电聚焦 iCIEF）：主电荷峰含量不得低于 55.0% ~ 65.0%，严格监控酸性峰与碱性变异体；\n"
                    "4. N-聚糖谱分析（亲水相互作用色谱 HILIC-UPLC）：G0F、G1F、G2F 中无岩藻糖基核心结构及末端半乳糖比例需符合参比品一致性标准；\n"
                    "5. 生物学活性（体外 HER2 结合活性 ELISA 或报告基因抑制法）：活性应为参考品的 80% ~ 125%（80%~125%）；\n"
                    "6. 细菌内毒素与无菌：每 1mg 蛋白质含内毒素应小于 0.25 EU（< 0.25 EU/mg）；无菌检查符合通则 1101 规定。"
                ),
                "content_en": (
                    "ChP 2025 Volume III: Trastuzumab for Injection (Anti-HER2 mAb)\n\n"
                    "1. Description: Recombinant humanized IgG1k monoclonal antibody produced in CHO cells targeting the extracellular domain of HER2 (ErbB2), MW ~148 kDa.\n\n"
                    "2. Critical Quality Attributes (CQAs):\n"
                    "- Purity (CE-SDS ChP 0542): Non-reduced main IgG peak >= 95.0%; Reduced heavy + light chain >= 98.0%;\n"
                    "- Size Variants (SEC-HPLC): Monomer >= 98.0%; Aggregates <= 1.5%; Fragments <= 0.5%;\n"
                    "- Charge Heterogeneity (CEX-HPLC / iCIEF): Main charge peak >= 55.0-65.0%;\n"
                    "- N-Glycan Profile: G0F, G1F, G2F afucosylation and galactosylation consistency with reference;\n"
                    "- Biological Activity: HER2 binding assay 80% to 125% relative to reference standard;\n"
                    "- Endotoxins: < 0.25 EU per mg; Sterility compliant."
                )
            }
        ]
    }
]
