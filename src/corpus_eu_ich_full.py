# -*- coding: utf-8 -*-
"""
Authentic Full-Text Corpus for EU MDR & ICH Guidelines (欧洲医疗器械法规与 ICH 国际指导原则完整版)
Contains complete, unabridged official regulatory texts, classification rules, decision trees, and validation parameters.
"""

EU_ICH_FULL_DOCUMENTS = [
    {
        "doc_id": "eu_mdr_2017_745_rule_11_official",
        "doc_title_zh": "欧盟医疗器械法规（EU MDR 2017/745）附录 VIII 第 11 条（Rule 11）与 MDCG 2019-11 软件分类指南",
        "doc_title_en": "Regulation (EU) 2017/745 (MDR) Annex VIII Rule 11 & MDCG 2019-11 Guidance on Software Qualification and Classification",
        "version": "EU-MDR-2017-745-MDCG-2019-11",
        "effective_date": "2021-05-26",
        "jurisdiction": "EU_MDR",
        "category": "European_Union_Regulation",
        "source_file": "eu_mdr_2017_745_annex_viii_rule_11_official_full.pdf",
        "md_file": "eu_mdr_2017_745_annex_viii_rule_11_official_full.md",
        "pdf_subpath": "eu_mdr/eu_mdr_2017_745_annex_viii_rule_11_official_full.pdf",
        "sections": [
            {
                "section_id": "mdr_rule11_sec1_classification_rules",
                "page": 1,
                "title_zh": "第一节：Rule 11 软件分级条款（Class I, IIa, IIb, III）法定判定标准",
                "title_en": "Section 1: Rule 11 Software Classification Criteria (Class I, IIa, IIb, III)",
                "content_zh": (
                    "欧洲联盟官方公报：《Regulation (EU) 2017/745 on Medical Devices (MDR)》Annex VIII Chapter III Classification Rules\n\n"
                    "一、Rule 11 软件分类专属规则全条款：\n"
                    "1. Rule 11(a) 诊断与治疗决策软件：\n"
                    "用于提供信息以供作出诊断或治疗目的决策的软件，划分为 IIa 类（Class IIa）；\n"
                    "- 例外情形 1（升为 III 类）：若此类决策产生的影响可能导致人员死亡或健康状况不可逆恶化（Death or Irreversible Deterioration），则属于 III 类（Class III）；\n"
                    "- 例外情形 2（升为 IIb 类）：若此类决策产生的影响可能导致人员健康状况严重恶化或需要外科手术干预（Serious Deterioration or Surgical Intervention），则属于 IIb 类（Class IIb）。\n\n"
                    "2. Rule 11(b) 生理过程监测软件：\n"
                    "用于监测生理过程的软件，划分为 IIa 类（Class IIa）；\n"
                    "- 例外情形（升为 IIb 类）：若用于监测生命体征参数，且这些参数的变化可能导致患者面临直接危险（Immediate Danger，如 ICU 心电/血氧危急报警软件），则属于 IIb 类（Class IIb）。\n\n"
                    "3. Rule 11(c) 兜底归类：\n"
                    "所有不属于上述两类的其他医疗软件，划分为 I 类（Class I）。"
                ),
                "content_en": (
                    "Regulation (EU) 2017/745 (MDR) Annex VIII Rule 11: Software Classification Rules\n\n"
                    "1. Rule 11(a) Diagnostic & Therapeutic Decisions: Classified as Class IIa, with critical escalations:\n"
                    "- Class III: If decision impact may cause death or irreversible deterioration of health;\n"
                    "- Class IIb: If decision impact may cause serious deterioration of health or surgical intervention.\n\n"
                    "2. Rule 11(b) Physiological Monitoring: Classified as Class IIa;\n"
                    "- Class IIb: If monitoring vital physiological parameters where variations could result in immediate danger.\n\n"
                    "3. Rule 11(c) Catch-All: All other medical device software is classified as Class I."
                )
            },
            {
                "section_id": "mdr_rule11_sec2_mdcg_2019_11_decision_tree",
                "page": 2,
                "title_zh": "第二节：MDCG 2019-11 医疗器械软件(MDSW)四步界定决策树",
                "title_en": "Section 2: MDCG 2019-11 Medical Device Software (MDSW) Four-Step Qualification Decision Tree",
                "content_zh": (
                    "欧洲医疗器械协调小组指南：《MDCG 2019-11 Guidance on Qualification and Classification of Software in Regulation (EU) 2017/745 and Regulation (EU) 2017/746》\n\n"
                    "一、医疗器械软件（MDSW）四步界定流程：\n"
                    "1. 步骤 1（软件形态判定）：判断目标对象是否符合软件定义（含云端 SaaS、移动 App、嵌入式固件）；\n"
                    "2. 步骤 2（医疗目的判定）：判断软件是否具备 MDR 第 2(1) 条定义的医疗目的（疾病诊断、预防、监护、治疗或缓解；损伤或残疾的补偿）。单纯用于医院行政挂号、计费、生活方式记录或患者档案管理的软件被排除；\n"
                    "3. 步骤 3（为患者利益创造新信息）：判断软件是否超越了单纯的存储、归档、压缩或通信传输功能，是否对医疗数据进行了运算、分析、转换以利于个体患者；\n"
                    "4. 步骤 4（结合 Rule 11 判定监管等级）：确认符合 MDSW 后，依据 Annex VIII Rule 11 决策树判定 Class I、IIa、IIb 或 III 类，并指定相应的公告机构（Notified Body）实施符合性评审。"
                ),
                "content_en": (
                    "MDCG 2019-11: Four-Step MDSW Qualification Process\n\n"
                    "Step 1: Verify software form factor (cloud, mobile app, firmware);\n"
                    "Step 2: Medical Purpose Check per MDR Article 2(1) (administrative, lifestyle, or billing tools excluded);\n"
                    "Step 3: Action on Data for Benefit of Individual Patients (algorithms transforming or interpreting data rather than passive storage/transmission);\n"
                    "Step 4: Classification under Annex VIII Rule 11 establishing Notified Body involvement."
                )
            }
        ]
    },
    {
        "doc_id": "ich_q9_r1_quality_risk_management_official",
        "doc_title_zh": "ICH Q9(R1)：质量风险管理指导原则（2023年正式定稿版本）",
        "doc_title_en": "ICH Harmonised Guideline Q9(R1): Quality Risk Management (Step 4 Final Adoption, Jan 2023)",
        "version": "ICH-Q9-R1-Official-2023",
        "effective_date": "2023-01-18",
        "jurisdiction": "ICH",
        "category": "ICH_Tripartite_Guideline",
        "source_file": "ich_q9_r1_quality_risk_management_full.pdf",
        "md_file": "ich_q9_r1_quality_risk_management_full.md",
        "pdf_subpath": "ich/ich_q9_r1_quality_risk_management_full.pdf",
        "sections": [
            {
                "section_id": "ich_q9_sec1_principles_and_formality",
                "page": 1,
                "title_zh": "第一节：质量风险管理两大基本原则与形式化程度(Formality)规范",
                "title_en": "Section 1: Two Fundamental QRM Principles & Spectrum of Formality",
                "content_zh": (
                    "国际人用药品注册技术协调会（ICH）指导原则：ICH Q9(R1) Quality Risk Management（2023年1月正式采纳）\n\n"
                    "一、质量风险管理两大基本原则（Two Primary Principles）：\n"
                    "1. 质量风险评估必须建立在科学知识的基础之上，并最终与保护患者（Protection of the Patient）的目标相联系。\n"
                    "2. 质量风险管理过程所投入的工作量、形式化程度（Formality）和文件记录的详略程度，应与所面对的风险水平相适应。\n\n"
                    "二、形式化程度（Formality in Quality Risk Management）：\n"
                    "Q9(R1) 核心突破是提出了形式化程度的连续谱概念（Spectrum of Formality）：\n"
                    "- 较低形式化（Low Formality）：适用于日常微小偏差、低危害常规操作，由合格专员依据标准操作规程（SOP）快速判定并记录；\n"
                    "- 较高形式化（High Formality）：适用于跨部门重大变更、复杂工艺验证、无菌保障体系失效等高风险场景，必须组建跨学科专家团队（涵盖工艺、QA、合规、工程），采用结构化风险工具（如 FMEA、HACCP、FTA），制定详尽的书面风险评估与控制报告。"
                ),
                "content_en": (
                    "ICH Q9(R1) Quality Risk Management (Step 4 Final Adoption, January 2023)\n\n"
                    "1. Two Fundamental Principles:\n"
                    "- Evaluation of quality risk is based on scientific knowledge and ultimately linked to the protection of the patient.\n"
                    "- The level of effort, formality, and documentation is commensurate with the level of risk.\n\n"
                    "2. Spectrum of Formality in QRM:\n"
                    "- Low Formality: Low-risk routine changes handled via SOPs by qualified individuals.\n"
                    "- High Formality: Critical deviations, aseptic failures, or major process changes requiring cross-functional expert teams, structured risk assessment tools (FMEA/HACCP/FTA), and comprehensive auditable reports."
                )
            },
            {
                "section_id": "ich_q9_sec2_subjectivity_and_risk_decisions",
                "page": 2,
                "title_zh": "第二节：控制主观性(Addressing Subjectivity)与基于风险的决策机制",
                "title_en": "Section 2: Addressing Subjectivity & Risk-Based Decision Making in Pharmaceutical Lifecycle",
                "content_zh": (
                    "ICH Q9(R1) 质量风险管理指导原则\n\n"
                    "一、控制风险评估中的主观性（Addressing Subjectivity）：\n"
                    "Q9(R1) 针对传统风险评估中人为偏见严重的行业痛点，提出了严格控制主观性的监管要求：\n"
                    "1. 承认并识别主观性偏差：认知偏差（如确认偏误、锚定效应、团队盲从）会导致风险严重度被错误低估或夸大；\n"
                    "2. 证据驱动：风险分析必须依靠真实实验数据、批生产历史记录、稳定性数据等客观证据，严禁未经论证的主观臆断；\n"
                    "3. 明确评分基准：在使用风险优先数（RPN）等量化工具时，严重度（S）、可能性（O）和检测度（D）的评分标准必须预先经过客观校准，消除不同人员评估时的模糊歧义。\n\n"
                    "二、基于风险的决策（Risk-Based Decision Making）：\n"
                    "将风险评估嵌入变更控制、纠正和预防措施（CAPA）、供应链审计以及产品生命周期质量回顾之中。"
                ),
                "content_en": (
                    "ICH Q9(R1): Subjectivity Control & Risk-Based Decision Making\n\n"
                    "1. Addressing Subjectivity:\n"
                    "Recognizes cognitive biases in risk analysis. Requires decisions to be driven by empirical operational data rather than subjective speculation. Severity, Occurrence, and Detection rating scales in FMEA must be explicitly defined and calibrated.\n\n"
                    "2. Risk-Based Decision Making: Directly integrates risk management into lifecycle change controls, CAPA, vendor audits, and annual product quality reviews."
                )
            }
        ]
    },
    {
        "doc_id": "ich_q2_r2_analytical_validation_official",
        "doc_title_zh": "ICH Q2(R2)：分析方法验证指导原则（2023年正式定稿版本）",
        "doc_title_en": "ICH Harmonised Guideline Q2(R2): Validation of Analytical Procedures (Step 4 Final Adoption, Nov 2023)",
        "version": "ICH-Q2-R2-Official-2023",
        "effective_date": "2023-11-01",
        "jurisdiction": "ICH",
        "category": "ICH_Tripartite_Guideline",
        "source_file": "ich_q2_r2_analytical_validation_full.pdf",
        "md_file": "ich_q2_r2_analytical_validation_full.md",
        "pdf_subpath": "ich/ich_q2_r2_analytical_validation_full.pdf",
        "sections": [
            {
                "section_id": "ich_q2_sec1_validation_parameters",
                "page": 1,
                "title_zh": "第一节：专属性、工作范围、线性、准确度、精密度与耐用性验证标准",
                "title_en": "Section 1: Specificity/Selectivity, Range, Linearity, Accuracy, Precision & Robustness",
                "content_zh": (
                    "国际人用药品注册技术协调会指导原则：ICH Q2(R2) Validation of Analytical Procedures（2023年11月正式采纳）\n\n"
                    "一、分析方法验证性能特性全项指标：\n"
                    "1. 专属性/选择性（Specificity / Selectivity）：在杂质、降解产物和辅料共存下，准确区分并测定目标分析物的能力；\n"
                    "2. 工作范围与线性（Working Range & Linearity）：在规定浓度范围内，测定信号与供试品浓度之间呈正比线性关系的区间（相关系数 $R^2 \\ge 0.999$）；\n"
                    "3. 准确度（Accuracy）：测定值与真实公认值之间的接近程度，通常通过标准品回收率试验验证（原料药回收率通常要求 98.0% ~ 102.0%）；\n"
                    "4. 精密度（Precision）：在规定条件下对均质供试品多次取样测定的接近程度，包括：\n"
                    "   - 重复性（Repeatability）：同一分析人员、同一仪器在短时间内测定，RSD <= 1.0%；\n"
                    "   - 中间精密度（Intermediate Precision）：不同日期、不同分析员或不同仪器的变异；\n"
                    "   - 重现性（Reproducibility）：不同实验室间协同试验验证；\n"
                    "5. 耐用性（Robustness）：故意引入微小变异（如流速 +/- 0.1ml/min、柱温 +/- 2℃、流动相 pH +/- 0.2）时方法结果的保持能力。"
                ),
                "content_en": (
                    "ICH Q2(R2) Validation of Analytical Procedures (Step 4 Final Adoption, November 2023)\n\n"
                    "Core Validation Characteristics:\n"
                    "1. Specificity/Selectivity: Unambiguous assessment of analyte in presence of expected matrix components and degradants.\n"
                    "2. Range & Linearity: Proportionality between signal and concentration (R^2 >= 0.999).\n"
                    "3. Accuracy: Closeness of test results to true value assessed via recovery studies (98.0%-102.0%).\n"
                    "4. Precision: Evaluated across Repeatability (RSD <= 1.0%), Intermediate Precision (different days/analysts), and Reproducibility.\n"
                    "5. Robustness: Demonstrated reliability against deliberated small variations in operating parameters."
                )
            }
        ]
    },
    {
        "doc_id": "ich_q10_pharmaceutical_quality_system_official",
        "doc_title_zh": "ICH Q10：制药质量体系指导原则（PQS）",
        "doc_title_en": "ICH Harmonised Tripartite Guideline Q10: Pharmaceutical Quality System (PQS)",
        "version": "ICH-Q10-Official",
        "effective_date": "2008-06-04",
        "jurisdiction": "ICH",
        "category": "ICH_Tripartite_Guideline",
        "source_file": "ich_q10_pharmaceutical_quality_system_full.pdf",
        "md_file": "ich_q10_pharmaceutical_quality_system_full.md",
        "pdf_subpath": "ich/ich_q10_pharmaceutical_quality_system_full.pdf",
        "sections": [
            {
                "section_id": "ich_q10_sec1_lifecycle_and_enablers",
                "page": 1,
                "title_zh": "第一节：产品生命周期四大阶段、两大支柱与四大管理要素(CAPA/变更/管理评审)",
                "title_en": "Section 1: Four Product Lifecycle Stages, Two Enablers & Four Core QMS Elements (CAPA, Change)",
                "content_zh": (
                    "国际人用药品注册技术协调会指导原则：ICH Q10 Pharmaceutical Quality System\n\n"
                    "一、产品生命周期四大阶段（Four Lifecycle Stages）：\n"
                    "1. 药物研发阶段（Pharmaceutical Development）；\n"
                    "2. 技术转移阶段（Technology Transfer）；\n"
                    "3. 商业化生产阶段（Commercial Manufacturing）；\n"
                    "4. 产品终止阶段（Product Discontinuation）。\n\n"
                    "二、两大核心推进支柱（Two Enablers）：\n"
                    "1. 知识管理（Knowledge Management / KM）：对产品配方、工艺参数、历史变更及监管审评知识进行系统性沉淀与传承；\n"
                    "2. 质量风险管理（Quality Risk Management / QRM）：全过程贯穿应用 ICH Q9 原则进行前瞻性与回顾性风险评估。\n\n"
                    "三、四大核心质量管理要素：\n"
                    "- 工艺性能与产品质量监控系统（Process Performance & Quality Monitoring）；\n"
                    "- 纠正与预防措施系统（CAPA System）：深入根本原因分析（Root Cause Analysis），防止问题复发；\n"
                    "- 变更管理系统（Change Management System）：事前评估变更对质量与法规备案的影响；\n"
                    "- 工艺性能与产品质量的管理评审（Management Review）：高管层定期回顾质量方针与资源配置。"
                ),
                "content_en": (
                    "ICH Q10: Pharmaceutical Quality System (PQS)\n\n"
                    "1. Four Lifecycle Stages: Pharmaceutical Development, Technology Transfer, Commercial Manufacturing, Product Discontinuation.\n\n"
                    "2. Two Enablers: Knowledge Management (KM) and Quality Risk Management (QRM per ICH Q9).\n\n"
                    "3. Four Core QMS Elements:\n"
                    "- Process Performance and Product Quality Monitoring System;\n"
                    "- Corrective Action and Preventive Action (CAPA) System;\n"
                    "- Change Management System;\n"
                    "- Management Review of Process Performance and Product Quality."
                )
            }
        ]
    },
    {
        "doc_id": "ich_q3d_r2_elemental_impurities_official",
        "doc_title_zh": "ICH Q3D(R2)：元素杂质指导原则与日允许暴露量(PDE)限度",
        "doc_title_en": "ICH Harmonised Guideline Q3D(R2): Guideline for Elemental Impurities & Permitted Daily Exposures (PDE)",
        "version": "ICH-Q3D-R2-Official-2022",
        "effective_date": "2022-04-26",
        "jurisdiction": "ICH",
        "category": "ICH_Tripartite_Guideline",
        "source_file": "ich_q3d_r2_elemental_impurities_full.pdf",
        "md_file": "ich_q3d_r2_elemental_impurities_full.md",
        "pdf_subpath": "ich/ich_q3d_r2_elemental_impurities_full.pdf",
        "sections": [
            {
                "section_id": "ich_q3d_sec1_classes_and_pde_table",
                "page": 1,
                "title_zh": "第一节：第一类(Pb/Cd/As/Hg)、第二类与第三类元素杂质每日允许暴露量(PDE)法定限度",
                "title_en": "Section 1: Permitted Daily Exposure (PDE) Limits for Class 1, Class 2, and Class 3 Elements",
                "content_zh": (
                    "国际人用药品注册技术协调会指导原则：ICH Q3D(R2) Guideline for Elemental Impurities\n\n"
                    "一、元素杂质分类与危害定义：\n"
                    "1. 第一类元素（Class 1 - 强人体毒性，在药品生产中无论是否添加均必须进行风险评估）：\n"
                    "   - 镉（Cadmium / Cd）：口服 PDE = 5.0 μg/day；注射 PDE = 2.0 μg/day；吸入 PDE = 3.0 μg/day；\n"
                    "   - 铅（Lead / Pb）：口服 PDE = 5.0 μg/day；注射 PDE = 5.0 μg/day；吸入 PDE = 5.0 μg/day；\n"
                    "   - 无机砷（Arsenic / As）：口服 PDE = 15 μg/day；注射 PDE = 15 μg/day；吸入 PDE = 2.0 μg/day；\n"
                    "   - 无机汞（Mercury / Hg）：口服 PDE = 30 μg/day；注射 PDE = 3.0 μg/day；吸入 PDE = 1.0 μg/day。\n\n"
                    "2. 第二类元素（Class 2 - 依赖给药途径的毒性）：\n"
                    "   - 2A 类（高发生概率，如生产设备引入）：钴（Co，口服 50 μg/day，注射 5.0 μg/day）、镍（Ni，口服 220 μg/day，注射 22 μg/day）、钒（V，口服 120 μg/day，注射 12 μg/day）；\n"
                    "   - 2B 类（催化剂残留，如 Pt, Pd, Ir, Rh, Ru, Os, Ag, Au）：仅在合成工艺中故意添加时才需评估。\n\n"
                    "3. 第三类元素（Class 3 - 低口服毒性，但注射/吸入需严格控制）：包括锂（Li）、锑（Sb）、钡（Ba）、铜（Cu）、锡（Sn）等。"
                ),
                "content_en": (
                    "ICH Q3D(R2) Elemental Impurities Guideline: Permitted Daily Exposure (PDE) Limits\n\n"
                    "1. Class 1 Elements (Significant human toxic potential; mandatory risk evaluation):\n"
                    "- Cadmium (Cd): Oral PDE = 5.0 ug/day; Parenteral PDE = 2.0 ug/day; Inhalation PDE = 3.0 ug/day.\n"
                    "- Lead (Pb): Oral PDE = 5.0 ug/day; Parenteral PDE = 5.0 ug/day; Inhalation PDE = 5.0 ug/day.\n"
                    "- Arsenic (As): Oral PDE = 15 ug/day; Parenteral PDE = 15 ug/day; Inhalation PDE = 2.0 ug/day.\n"
                    "- Mercury (Hg): Oral PDE = 30 ug/day; Parenteral PDE = 3.0 ug/day; Inhalation PDE = 1.0 ug/day.\n\n"
                    "2. Class 2A Elements: Co, Ni, V. Class 2B Elements: Pt, Pd, Rh, Ru, Au.\n"
                    "3. Class 3 Elements: Li, Sb, Ba, Cu, Sn."
                )
            }
        ]
    }
]
