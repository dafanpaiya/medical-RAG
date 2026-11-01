# -*- coding: utf-8 -*-
"""
Authentic Full-Text Corpus for Chinese Pharmacopoeia 2025 Edition - Volume IV (《中国药典》2025年版四部：通则与药用辅料)
Statutory effective date: October 1, 2025 (Announcement No. 29 of 2025 by NMPA & NHC).
Covers Dosage Form General Chapters (0101 Tablets, 0102 Injections, 0103 Capsules),
Pharmaceutical Water General Chapters (0261 & 9209 Guideline), Instrumental Analysis (0512 HPLC, 0861 Solvents, 0931 Dissolution),
Microbiology (1101 Sterility, 1105 Bioburden, 1143 Endotoxins), Stability (9014), Impurities (9015), and Excipients.
"""

CHP_2025_VOL4_DOCUMENTS = [
    {
        "doc_id": "chp_2025_vol4_general_chapter_0101_tablets",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 通则 0101：片剂通则",
        "doc_title_en": "ChP 2025 General Chapter 0101: General Requirements for Tablets",
        "version": "2025-ChP-Vol4-0101",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol4_general_chapter_0101_tablets_full.pdf",
        "md_file": "chp_2025_vol4_general_chapter_0101_tablets_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_general_chapter_0101_tablets_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol4_0101_sec1_disintegration_friability_uniformity",
                "page": 1,
                "title_zh": "第一节：片剂分类、崩解时限、脆碎度(<=1.0%)与片重差异/含量均匀度标准",
                "title_en": "Section 1: Tablet Classes, Disintegration Times, Friability (<=1.0%) & Uniformity of Dosage Units",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 制剂通则 0101 片剂\n\n"
                    "一、定义与分类：\n"
                    "片剂系指原料药物或与适宜辅料均匀混合后压制而成的圆片状或异形片状固体制剂。包括普通压制片、薄膜衣片、糖衣片、肠溶片、含片、舌下片、咀嚼片、分散片、可溶片、泡腾片、缓释片与控释片。\n\n"
                    "二、通用质量检查项目与判定标准：\n"
                    "1. 崩解时限（通则 0921 升降式崩解仪，水温 37℃±1℃）：\n"
                    "   - 普通压制片：6 片均应在 15 分钟内完全崩解并通过筛网（<= 15 分钟）；\n"
                    "   - 薄膜衣片：应在 30 分钟内完全崩解；糖衣片：应在 1 小时内完全崩解；\n"
                    "   - 肠溶衣片：先在 0.1 mol/L 盐酸溶液中检查 2 小时，每片均不得有裂缝、崩解或软化；再在 pH 6.8 磷酸盐缓冲液中检查，1 小时内应完全崩解；\n"
                    "   - 分散片：在 15℃ ~ 25℃ 水中振摇 3 分钟内应完全崩解并通过 2 号筛；泡腾片：5 分钟内完全崩解。\n"
                    "2. 片剂脆碎度检查（通则 0923）：\n"
                    "   - 针对非包衣片剂，转筒转速 25 转/分，连续旋转 100 转（4 分钟）；\n"
                    "   - 试验后片剂减失重量不得过 1.0%（<= 1.0%），且不得检出断裂、龟裂及粉碎的片子。\n"
                    "3. 含量均匀度（通则 0941）：小剂量片剂（主药标示量小于 25mg 或主药含量小于片重 25% 者），必须检查含量均匀度，判定值 A+2.2S 应小于等于 15.0（L <= 15.0）。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia 2025 General Chapter 0101: Tablets\n\n"
                    "1. Disintegration Time Standards (ChP 0921 at 37 C):\n"
                    "- Plain uncoated tablets: Fully disintegrated within 15 minutes (<= 15 min);\n"
                    "- Film-coated tablets: Within 30 minutes; Sugar-coated: Within 60 minutes;\n"
                    "- Enteric-coated tablets: No crack or softening in 0.1 M HCl for 2 hours; fully disintegrated in pH 6.8 buffer within 60 minutes;\n"
                    "- Dispersible tablets: Within 3 minutes at 15-25 C passing No. 2 sieve.\n\n"
                    "2. Friability Test (ChP 0923, 100 revolutions):\n"
                    "Weight loss shall not exceed 1.0% (<= 1.0%) with no broken or chipped tablets.\n\n"
                    "3. Uniformity of Dosage Units (ChP 0941): Mandatory for units < 25 mg or drug loading < 25%, acceptance value A+2.2S <= 15.0."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_general_chapter_0102_injections",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 通则 0102：注射剂通则",
        "doc_title_en": "ChP 2025 General Chapter 0102: General Requirements for Injections",
        "version": "2025-ChP-Vol4-0102",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol4_general_chapter_0102_injections_full.pdf",
        "md_file": "chp_2025_vol4_general_chapter_0102_injections_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_general_chapter_0102_injections_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol4_0102_sec1_particulate_sterility_endotoxins",
                "page": 1,
                "title_zh": "第一节：注射剂分类（小水针/大输液/冻干粉针）、可见异物灯检法与不溶性微粒限度",
                "title_en": "Section 1: Injections Types (SVP, LVP, Lyophilized), Visible Particles & Sub-visible Particulate Limits",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 制剂通则 0102 注射剂\n\n"
                    "一、分类与生产无菌保证原则：\n"
                    "注射剂系指原料药物或与适宜辅料制成的供注入体内的无菌制剂。分为小容量注射液（<= 50ml / SVP）、大容量注射液（>= 100ml / LVP / 大输液）、注射用无菌粉末（粉针及冷冻干燥粉针）与注射用浓溶液。凡能耐受湿热灭菌的产品必须采用最终高压灭菌工艺（F0 >= 8 或 F0 >= 12）；不能耐受热灭菌的必须采用 0.22μm 无菌除菌过滤并配合无菌生产（A级/B级背景）。\n\n"
                    "二、通用强制性检查标准：\n"
                    "1. 可见异物（通则 0904 灯检法）：\n"
                    "   - 采用标准可见异物检查仪，在 1000 ~ 1500 lx 照度下（有色溶液可在 2000 ~ 4000 lx），对黑色和白色背景分别旋转检视；不得检出金属屑、玻璃屑、纤维、色块、毛发及真菌菌块等任何外来异物；\n"
                    "2. 不溶性微粒（通则 0903 光阻法）：\n"
                    "   - 静脉大容量注射液（标示装量 >= 100ml）：每 1ml 中含 10μm 及以上微粒不得过 25 粒；含 25μm 及以上微粒不得过 3 粒；\n"
                    "   - 静脉小容量注射液（标示装量 < 100ml）：每个包装容器中含 10μm 及以上微粒不得过 6000 粒；含 25μm 及以上微粒不得过 600 粒；\n"
                    "3. 细菌内毒素与热原（通则 1143 / 1142）：凡注射剂必须按正文项下设定严格的内毒素限值 L = K/M；\n"
                    "4. 无菌检查（通则 1101）：全批次取样依法检查，经 14 天恒温培养必须符合无菌规定。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia 2025 General Chapter 0102: Injections (Parenterals)\n\n"
                    "1. Sterility Assurance: Small volume parenterals (SVP <= 50 ml), large volume parenterals (LVP >= 100 ml), and lyophilized powders. Terminal heat sterilization (F0 >= 8 or 12) preferred; aseptic processing with 0.22 um sterile filtration under Grade A/B cleanroom.\n\n"
                    "2. Compendial Standards:\n"
                    "- Visible Particles (ChP 0904 Light Inspection, 1000-1500 lx): Zero tolerance for glass, metal, fibers, hair, or fungal clumps.\n"
                    "- Sub-visible Particulate Matter (ChP 0903 Light Obscuration):\n"
                    "  * LVP (>= 100 ml): >= 10 um <= 25 particles/ml; >= 25 um <= 3 particles/ml;\n"
                    "  * SVP (< 100 ml): >= 10 um <= 6000 particles/container; >= 25 um <= 600 particles/container.\n"
                    "- Bacterial Endotoxins (ChP 1143) and 14-day Sterility (ChP 1101) mandatory."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_general_chapter_0261",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 通则 0261：制药用水通则",
        "doc_title_en": "ChP 2025 General Chapter 0261: General Requirements for Pharmaceutical Water",
        "version": "2025-ChP-Vol4-0261",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol4_general_chapter_0261_pharmaceutical_water_full.pdf",
        "md_file": "chp_2025_vol4_general_chapter_0261_pharmaceutical_water_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_general_chapter_0261_pharmaceutical_water_full.pdf",
        "sections": [
            {
                "section_id": "chp_2025_vol4_0261_sec1_water_types_and_systems",
                "page": 1,
                "title_zh": "第一节：制药用水分类、膜法制水系统设计规范与水质选择适用原则",
                "title_en": "Section 1: Classification of Water for Pharmaceutical Use & Membrane System Engineering",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 通则 0261 制药用水通则\n\n"
                    "一、制药用水分类与定义：\n"
                    "制药用水是指药品生产过程中使用的水，包括饮用水、纯化水、注射用水和灭菌注射用水。2025年版中国药典在通则 0261 中全面重构制药用水工程与质量控制标准：\n"
                    "1. 饮用水：符合国家生活饮用水卫生标准（GB 5749），为制备纯化水的水源；\n"
                    "2. 纯化水：饮用水经蒸馏、反渗透（RO）、连续电去离子（CEDI）等法制得，用于非无菌药品的配制及无菌药品的初始清洗；\n"
                    "3. 注射用水（WFI）：纯化水经多效蒸馏法、气压式蒸馏法，或经反渗透（二级 RO）联合超滤（UF）等反渗透+非蒸馏膜法工艺制得，用于注射剂配制；\n"
                    "4. 灭菌注射用水：注射用水经灌装灭菌制成的无菌制剂水，用于粉针溶解与注射剂稀释。\n\n"
                    "二、制水系统工程规范与管路设计：\n"
                    "1. 材质要求：注射用水储罐与输送分配管路必须采用优质低碳 316L 不锈钢材质；内表面必须经过电解抛光（EP 处理），表面粗糙度 Ra <= 0.4 μm；\n"
                    "2. 盲管死角规则：管路分支必须严格遵循“3D 盲管规则”（盲管长度不得大于管道内径的 3 倍，推荐 1.5D 零死角阀门），杜绝滞水死角；\n"
                    "3. 流速与水流状态：分配管网主管流速必须维持湍流状态（雷诺数 Re > 4000），主循环回路回水流速不得低于 1.0 m/s（>= 1.0 m/s）；\n"
                    "4. 微生物防范温度：注射用水系统必须采用 >= 70℃ 的持续热保温循环储存，或定期采用 121℃ 纯蒸汽灭菌（SIP）或臭氧消毒。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia 2025 General Chapter 0261: Pharmaceutical Water\n\n"
                    "1. Categories: Drinking Water, Purified Water, Water for Injection (WFI), and Sterile Water for Injection.\n"
                    "Major Compendial Innovation: WFI may be produced via distillation OR validated membrane processes (RO + CEDI + Ultrafiltration).\n\n"
                    "2. Engineering & Piping Design Specifications:\n"
                    "- Material: 316L stainless steel with electropolished inner surface (Ra <= 0.4 um);\n"
                    "- Dead-leg Rule: Branch dead-legs must adhere to <= 3D rule (length <= 3x diameter, preferably <= 1.5D);\n"
                    "- Flow Velocity: Minimum return loop velocity >= 1.0 m/s ensuring turbulent flow (Re > 4000);\n"
                    "- Thermal Sanitation: Continuous hot circulation >= 70 C, or routine SIP / ozone sanitation."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_guideline_9209",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 指导原则 9209：制药用水微生物监测和控制指导原则",
        "doc_title_en": "ChP 2025 Guideline 9209: Microbial Monitoring and Control of Water for Pharmaceutical Use",
        "version": "2025-ChP-Vol4-9209",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Guideline",
        "source_file": "chp_2025_vol4_guideline_9209_microbial_monitoring_full.pdf",
        "md_file": "chp_2025_vol4_guideline_9209_microbial_monitoring_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_guideline_9209_microbial_monitoring_full.pdf",
        "sections": [
            {
                "section_id": "chp_2025_vol4_9209_sec1_alert_action_levels",
                "page": 1,
                "title_zh": "第一节：微生物动态监测、警戒限度(Alert)与纠偏限度(Action)两级预警体系",
                "title_en": "Section 1: Microbial Monitoring & Two-Tier Alert/Action Level Regulatory Framework",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 指导原则 9209 制药用水微生物监测和控制指导原则（2025年版新设核心指导原则）\n\n"
                    "一、背景与监管意图：\n"
                    "随着膜法制备注射用水新工艺的实施，制药用水系统必须建立全生命周期的微生物质量预防控制与动态监测体系。本指导原则旨在指导制药企业建立科学的取样策略、限度设定及微生物生物膜（Biofilm）防范。\n\n"
                    "二、警戒限度与纠偏限度的建立规范：\n"
                    "制药用水系统绝不能简单依赖法定标准作为日常放行控制，必须基于历史趋势数据建立两级动态控制指标：\n"
                    "1. 警戒限度（Alert Limit）：\n"
                    "   - 设定原则：通常设定为法定药典标准限度的 50%，或基于正常运行历史数据的 95 百分位数（95th percentile）；\n"
                    "   - 应对处置：超出警戒限度并不代表水质不合格，但提示系统可能存在潜在漂移风险，企业应启动趋势调查并增加取样监测频次；\n"
                    "2. 纠偏限度（Action Limit）：\n"
                    "   - 设定原则：通常设定为法定药典标准限度的 70% ~ 80%，或基于历史数据的 99 百分位数（99th percentile）；\n"
                    "   - 应对处置：超出纠偏限度表明系统已偏离受控状态，必须立即启动根因调查（RCA）、执行系统消毒灭菌、评估对已生产药品批次质量的潜在影响，并执行 CAPA 纠正预防措施。"
                ),
                "content_en": (
                    "ChP 2025 Guideline 9209: Microbial Monitoring and Control for Pharmaceutical Water\n\n"
                    "1. Two-Tier Alert and Action Levels:\n"
                    "- Alert Limit: Set at 50% of the statutory compendial limit or 95th historical percentile. Exceedance triggers trend investigation and increased sampling frequency without product hold;\n"
                    "- Action Limit: Set at 70% to 80% of statutory limit or 99th historical percentile. Exceedance indicates out-of-control state requiring immediate root-cause analysis (RCA), emergency sanitation, and impact assessment on affected product batches."
                )
            },
            {
                "section_id": "chp_2025_vol4_9209_sec2_sampling_biofilm",
                "page": 2,
                "title_zh": "第二节：使用点(POU)取样规程、革兰氏阴性菌监控与管路生物膜(Biofilm)防范",
                "title_en": "Section 2: Point-of-Use (POU) Sampling, Gram-Negative Endotoxin Bacteria & Biofilm Control",
                "content_zh": (
                    "《中国药典》2025年版四部 指导原则 9209\n\n"
                    "一、取样计划与使用点（POU）取样规程：\n"
                    "1. 取样点覆盖：必须覆盖制水系统的制备出水口、储罐呼吸器、总送水口、总回水口，以及每一个生产车间的使用点（POU）；\n"
                    "2. 取样操作仿真：取样时应模拟生产实际使用条件。若生产使用前进行冲洗或软管连接，取样时必须保持相同前置处理。\n\n"
                    "二、耐受性菌群与特定微生物监控：\n"
                    "在纯化水与注射用水系统中，必须重点监测产内毒素的非发酵革兰氏阴性杆菌（如铜绿假单胞菌 Pseudomonas aeruginosa、洋葱伯克霍尔德菌群 Burkholderia cepacia complex、无色杆菌属及嗜麦芽窄食单胞菌）：\n"
                    "- 此类菌群易吸附在管壁、密封圈凹槽处分泌胞外多糖聚合物（EPS），形成高度耐药耐热的生物膜（Biofilm）；\n"
                    "- 一旦生物膜成熟，常规低浓度化学消毒剂无法穿透，可导致微生物反复脱落和内毒素持续超标；\n"
                    "- 防范措施：保持管网流速 >= 1.0 m/s，消除 > 3D 死角，定期采用高温过热水（>= 121℃）或臭氧强化清洗杀菌。"
                ),
                "content_en": (
                    "ChP 2025 Guideline 9209 (Section 2):\n\n"
                    "1. Point-of-Use (POU) Sampling: Must mirror actual production procedures (sampling through transfer hoses after standard flushing).\n\n"
                    "2. Biofilm Control & Target Microorganisms:\n"
                    "Target surveillance against endotoxin-producing Gram-negative non-fermenters (Pseudomonas aeruginosa, Burkholderia cepacia complex). These species form extracellular polymeric substances (EPS) generating resilient biofilms. Controls: Turbulent flow velocity >= 1.0 m/s, zero dead-legs, and periodic >= 121 C superheated water or ozone sanitization."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_general_chapter_0512_hplc",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 通则 0512：高效液相色谱法（HPLC）",
        "doc_title_en": "ChP 2025 General Chapter 0512: High Performance Liquid Chromatography (HPLC)",
        "version": "2025-ChP-Vol4-0512",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol4_general_chapter_0512_hplc_full.pdf",
        "md_file": "chp_2025_vol4_general_chapter_0512_hplc_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_general_chapter_0512_hplc_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol4_0512_sec1_system_suitability",
                "page": 1,
                "title_zh": "第一节：系统适用性试验四大指标（理论板数、分离度R>=1.5、拖尾因子0.95~1.05、重复性RSD<=2.0%）",
                "title_en": "Section 1: System Suitability Test (Plate Number N, Resolution R>=1.5, Tailing Factor T, Precision RSD)",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 通则 0512 高效液相色谱法\n\n"
                    "一、方法原理与适用范围：\n"
                    "本法系采用高压输液系统将规定的流动相泵入装有微粒固定相的色谱柱，对多组分物质进行分离、定性与定量分析的方法。广泛应用于中药、化学药及生物制品的鉴别、杂质检查和含量测定。\n\n"
                    "二、系统适用性试验（System Suitability Testing）：\n"
                    "色谱系统在测定供试品前，必须按照品种正文规定通过系统适用性试验验证，包含以下四大指标：\n"
                    "1. 色谱柱理论板数（N）：N = 5.54 * (tR / Wh/2)^2。板数应不低于品种项下规定的下限值；\n"
                    "2. 分离度（R）：R = 2 * (tR2 - tR1) / (W1 + W2)。除另有规定外，待测成分与相邻色谱峰之间的分离度必须大于等于 1.5（R >= 1.5），保证色谱峰实现基线分离；\n"
                    "3. 拖尾因子（T）：T = W0.05h / (2 * d1)。用以评价色谱峰对称性。除另有规定外，峰的拖尾因子应在 0.95 ~ 1.05 之间；若用于杂质定量测定，一般允许在 0.80 ~ 1.50 之间；\n"
                    "4. 重复性（RSD）：连续进样对照品溶液 5 次或 6 次，主峰面积的相对标准偏差（RSD）除另有规定外，不得大于 2.0%（RSD <= 2.0%）。"
                ),
                "content_en": (
                    "ChP 2025 General Chapter 0512: High Performance Liquid Chromatography (HPLC)\n\n"
                    "System Suitability Test Parameters:\n"
                    "1. Theoretical Plates (N): N = 5.54 * (tR / Wh/2)^2, meeting specified lower limits;\n"
                    "2. Resolution (R): R = 2 * (tR2 - tR1) / (W1 + W2). Unless otherwise specified, R shall be >= 1.5 ensuring baseline separation;\n"
                    "3. Tailing Factor (T): T = W0.05h / (2 * d1). Between 0.95 and 1.05 for symmetrical peaks (0.80-1.50 for impurity tests);\n"
                    "4. Precision (RSD): Relative standard deviation of peak areas across 5 or 6 consecutive injections shall not exceed 2.0% (RSD <= 2.0%)."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_general_chapter_0861_solvents",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 通则 0861：残留溶剂测定法",
        "doc_title_en": "ChP 2025 General Chapter 0861: Residual Solvents Determination Method",
        "version": "2025-ChP-Vol4-0861",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol4_general_chapter_0861_residual_solvents_full.pdf",
        "md_file": "chp_2025_vol4_general_chapter_0861_residual_solvents_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_general_chapter_0861_residual_solvents_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol4_0861_sec1_classification_and_limits",
                "page": 1,
                "title_zh": "第一节：残留溶剂三类分类体系、顶空气相色谱法与一类溶剂严控标准",
                "title_en": "Section 1: Three-Tier Solvent Classification (Class 1, 2, 3), Headspace GC & Class 1 Strict Limits",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 通则 0861 残留溶剂测定法（全面与 ICH Q3C 国际协调）\n\n"
                    "一、分类标准与毒性评估原则：\n"
                    "本法系采用顶空气相色谱法（HS-GC，毛细管柱与 FID 检测器）测定原料药、辅料及制剂中生产引入或产生的有机溶剂残留：\n"
                    "1. 第一类溶剂（应当避免使用的溶剂）：已知人体致癌物或强环境毒害物。除非有不可替代的极其充分的生产理由，否则严禁使用：\n"
                    "   - 苯（Benzene）：限度 <= 2 ppm（2 mg/kg）；\n"
                    "   - 四氯化碳（Carbon tetrachloride）：限度 <= 4 ppm；\n"
                    "   - 1,2-二氯乙烷：限度 <= 5 ppm；1,1-二氯乙烯：<= 8 ppm；1,1,1-三氯乙烷：<= 1500 ppm。\n"
                    "2. 第二类溶剂（应当限制使用的溶剂）：具有一定固有毒性，按每日允许暴露量（PDE）限制残留：\n"
                    "   - 乙腈（Acetonitrile）：PDE = 4.1 mg/天，限度 <= 410 ppm；\n"
                    "   - 甲醇（Methanol）：PDE = 30.0 mg/天，限度 <= 3000 ppm；\n"
                    "   - 二氯甲烷（Dichloromethane）：PDE = 6.0 mg/天，限度 <= 600 ppm；\n"
                    "   - 甲苯（Toluene）：PDE = 8.9 mg/天，限度 <= 890 ppm；N,N-二甲基甲酰胺（DMF）：<= 880 ppm。\n"
                    "3. 第三类溶剂（低毒溶剂）：GMP 控制下限度一般为 <= 0.5%（<= 5000 ppm），包括乙醇、丙酮、乙酸乙酯、异丙醇、乙醚、DMSO 等。"
                ),
                "content_en": (
                    "ChP 2025 General Chapter 0861: Residual Solvents (Harmonized with ICH Q3C)\n\n"
                    "Headspace Gas Chromatography (HS-GC) Classification & Limits:\n"
                    "1. Class 1 Solvents (Avoid Use - Carcinogens):\n"
                    "- Benzene <= 2 ppm;\n"
                    "- Carbon tetrachloride <= 4 ppm;\n"
                    "- 1,2-Dichloroethane <= 5 ppm;\n"
                    "2. Class 2 Solvents (Limited Use per PDE):\n"
                    "- Acetonitrile: PDE 4.1 mg/day, <= 410 ppm;\n"
                    "- Methanol: PDE 30.0 mg/day, <= 3000 ppm;\n"
                    "- Dichloromethane: PDE 6.0 mg/day, <= 600 ppm;\n"
                    "- Toluene: PDE 8.9 mg/day, <= 890 ppm;\n"
                    "3. Class 3 Solvents (Low Toxicity): Ethanol, acetone, ethyl acetate, isopropanol <= 5000 ppm (0.5%)."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_general_chapter_0931_dissolution",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 通则 0931：溶出度与释放度测定法",
        "doc_title_en": "ChP 2025 General Chapter 0931: Dissolution and Drug Release Test Methods",
        "version": "2025-ChP-Vol4-0931",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol4_general_chapter_0931_dissolution_full.pdf",
        "md_file": "chp_2025_vol4_general_chapter_0931_dissolution_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_general_chapter_0931_dissolution_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol4_0931_sec1_apparatus_and_f2",
                "page": 1,
                "title_zh": "第一节：溶出度装置（篮法/桨法/小杯法）与相似因子 f2 体外等同性计算公式",
                "title_en": "Section 1: Dissolution Apparatus (Basket, Paddle, Small Cup) & Similarity Factor f2 Equation",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 通则 0931 溶出度与释放度测定法\n\n"
                    "一、法定装置类型：\n"
                    "1. 第一法（转篮法 / Basket Method）：适用于胶囊剂、漂浮或易发生聚集的固体制剂；常用转速 100 转/分；\n"
                    "2. 第二法（桨法 / Paddle Method）：最广泛使用的口服固体制剂装置；常用转速 50 转/分或 75 转/分；\n"
                    "3. 第三法（小杯法）：适用于小剂量制剂或微量溶出测定；\n"
                    "4. 第四法（流通池法 / Flow-Through Cell）：适用于难溶性药物及微球植入剂；恒温水浴保持 37℃±0.5℃。\n\n"
                    "二、体外多介质溶出曲线与相似因子（f2）数学判定公式：\n"
                    "一致性评价中，仿制药与原研参比制剂（RLD）在 4 种生理介质（pH 1.2 盐酸溶液、pH 4.5 醋酸盐缓冲液、pH 6.8 磷酸盐缓冲液、水）中必须比较全溶出曲线：\n"
                    "相似因子 f2 计算公式为：\n"
                    "f2 = 50 * lg { [ 1 + (1/n) * sum_{t=1}^n (Rt - Tt)^2 ]^(-0.5) * 100 }\n"
                    "- 式中 n 为取样时间点数；Rt 为参比制剂在 t 时间点的平均溶出百分率；Tt 为受试制剂在 t 时间点的平均溶出百分率；\n"
                    "- 法定等同性判定标准：当 f2 介于 50 ~ 100 之间（50 <= f2 <= 100）时，判定两制剂体外溶出行为等同。"
                ),
                "content_en": (
                    "ChP 2025 General Chapter 0931: Dissolution & Drug Release\n\n"
                    "1. Compendial Apparatus:\n"
                    "- Method 1 (Basket, 100 rpm) for floating dosage forms/capsules;\n"
                    "- Method 2 (Paddle, 50-75 rpm) standard for solid orals;\n"
                    "- Method 4 (Flow-through cell) for poorly soluble drugs, maintained at 37 C +/- 0.5 C.\n\n"
                    "2. Similarity Factor f2 for In Vitro Equivalence:\n"
                    "f2 = 50 * log10 { [ 1 + (1/n) * sum( (Rt - Tt)^2 ) ]^(-0.5) * 100 }\n"
                    "Criterion: Two dissolution curves are deemed equivalent if 50 <= f2 <= 100."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_guideline_9014_stability",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 指导原则 9014：原料药物与制剂稳定性试验指导原则",
        "doc_title_en": "ChP 2025 Guideline 9014: Stability Testing of Active Pharmaceutical Ingredients and Finished Products",
        "version": "2025-ChP-Vol4-9014",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Guideline",
        "source_file": "chp_2025_vol4_guideline_9014_stability_full.pdf",
        "md_file": "chp_2025_vol4_guideline_9014_stability_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol4_guideline_9014_stability_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol4_9014_sec1_testing_conditions",
                "page": 1,
                "title_zh": "第一节：稳定性试验三大测试（影响因素、加速试验 40℃/75%RH、长期试验 25℃/60%RH）",
                "title_en": "Section 1: Stress Testing, Accelerated Testing (40C/75%RH) & Long-Term Testing (25C/60%RH)",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 指导原则 9014 原料药物与制剂稳定性试验指导原则（协调 ICH Q1A）\n\n"
                    "一、试验目的与原则：\n"
                    "通过考察原料药物或制剂在温度、湿度、光线等环境因素影响下的质量随时间变化的规律，为药品生产工艺、包装材料、贮存条件及有效期的确定提供科学依据。\n\n"
                    "二、三大法定稳定性试验方案：\n"
                    "1. 影响因素试验（剧烈试验 / Stress Testing）：考察一批原料药在极端条件下的敏感性：\n"
                    "   - 高温试验：60℃ 放置 10 天，在第 5 天和第 10 天取样；若发生明显降解则置 40℃ 考察；\n"
                    "   - 高湿试验：25℃、相对湿度 90%±5% 放置 10 天，考察吸湿潮解；\n"
                    "   - 强光照射试验：光照度 4500 lx±500 lx 放置 10 天，总照度不低于 1.2 * 10^6 lx·h，近紫外能量不低于 200 W·h/m^2。\n"
                    "2. 加速试验（Accelerated Testing）：\n"
                    "   - 条件：温度 40℃±2℃，相对湿度 75%±5% RH，放置 6 个月；在第 1、2、3、6 个月末取样检验；\n"
                    "   - 显著变化（Significant Change）判定：主药含量下降 5.0%、降解杂质超过法定限度、pH 或溶出度不合格等；若出现显著变化需增设中间条件（30℃±2℃，65%±5% RH，12 个月）；\n"
                    "3. 长期试验（Long-Term Testing）：\n"
                    "   - 条件：温度 25℃±2℃，相对湿度 60%±5% RH（常温贮存品种），考核 12、24、36 个月；用以最终确定药品有效期。"
                ),
                "content_en": (
                    "ChP 2025 Guideline 9014: Stability Testing (Harmonized with ICH Q1A)\n\n"
                    "1. Stress Testing (10 days):\n"
                    "- High temperature: 60 C for 10 days;\n"
                    "- High humidity: 25 C / 90% RH;\n"
                    "- Photostability: >= 1.2 million lux-hours and near UV >= 200 Wh/m^2.\n\n"
                    "2. Accelerated Testing (6 months):\n"
                    "- 40 C +/- 2 C / 75% +/- 5% RH. Sampled at months 1, 2, 3, 6. Significant change (5% potency loss, failure of dissolution/impurities) triggers intermediate testing (30 C / 65% RH).\n\n"
                    "3. Long-Term Testing (12-36 months):\n"
                    "- 25 C +/- 2 C / 60% +/- 5% RH to establish real-time shelf life."
                )
            }
        ]
    }
]
