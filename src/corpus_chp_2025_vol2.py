# -*- coding: utf-8 -*-
"""
Authentic Full-Text Corpus for Chinese Pharmacopoeia 2025 Edition - Volume II (《中国药典》2025年版二部：化学药)
Statutory effective date: October 1, 2025 (Announcement No. 29 of 2025 by NMPA & NHC).
Covers Chemical Active Pharmaceutical Ingredients (APIs), Oral Solid Dosage Forms, Large Volume Parenterals,
Antibiotics, Cardiovascular, Endocrine, and NSAID Essential Medicine Monographs.
"""

CHP_2025_VOL2_DOCUMENTS = [
    {
        "doc_id": "chp_2025_vol2_purified_water",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：纯化水",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Purified Water (Aqua Purificata)",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_purified_water_monograph_full.pdf",
        "md_file": "chp_2025_vol2_purified_water_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_purified_water_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_2025_vol2_water_sec1_monograph_specs",
                "page": 1,
                "title_zh": "第一节：纯化水法定来源、性状与理化指标限度",
                "title_en": "Section 1: Source, Definition, Physical Properties & Physicochemical Limits",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：纯化水（Aqua Purificata）\n"
                    "【法定来源与定义】：本品为饮用水经蒸馏法、离子交换法、反渗透法或其他适宜的方法制得的制药用水。不得添加任何抑菌剂或其他添加剂。\n"
                    "【性状】：本品为无色的澄清液体；无臭。\n\n"
                    "【法定检验与限度要求】：\n"
                    "1. 酸碱度（pH）：取本品 10ml，加甲基红指示液 2 滴，不得显红色；另取 10ml，加溴百里香酚蓝指示液 5 滴，不得显蓝色（控制酸碱度范围约为 pH 5.0 ~ 7.0）。\n"
                    "2. 氯化物、硫酸盐与钙盐：取本品各 50ml，依法检查，均不得发生浑浊或沉淀，证明氯化物、硫酸盐与钙盐检查符合规定。\n"
                    "3. 硝酸盐（Nitrate）：取本品 5ml，置试管中，于冰浴中加 10% 氯化钾溶液 0.4ml 与 0.1% 二苯胺硫酸溶液 0.1ml，摇匀，缓缓滴加硫酸 5ml，在 50℃ 水浴中保温 15 分钟，所显蓝色与对照液比较，不得更深（限度：<= 0.06 mg/L，即 0.06 ppm）。\n"
                    "4. 亚硝酸盐（Nitrite）：取本品 10ml，加对氨基苯磺酰胺的稀盐酸溶液与盐酸萘乙二胺溶液，所显粉红色不得深于标准对照液（限度：<= 0.02 mg/L，即 0.02 ppm）。\n"
                    "5. 氨（Ammonia）：取本品 50ml，加碱性碘化汞钾试液 2ml，放置 15 分钟；如显色，与氯化铵对照液比较，不得更深（限度：<= 0.3 mg/L，即 0.3 ppm）。\n"
                    "6. 不挥发物（Non-volatile Residue）：取本品 100ml，置在 105℃ 恒重的蒸发皿中，在水浴上蒸干，并在 105℃ 干燥至恒重，遗留残渣不得过 1.0 mg（限度：<= 1 mg / 100ml）。\n"
                    "7. 重金属（Heavy Metals）：取本品 40ml，加醋酸盐缓冲液（pH 3.5）2ml 与硫代乙酰胺试液 2ml，依法检查，显色不得深于标准铅对照液（限度：<= 0.5 ppm / 0.5 mg/L）。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2025 Edition, Volume II Official Monograph: Purified Water (Aqua Purificata)\n"
                    "Source & Definition: Water for pharmaceutical use prepared from drinking water by distillation, ion-exchange, reverse osmosis (RO), or other suitable processes. Contains no antimicrobial agents or other added substances.\n"
                    "Description: Clear, colorless liquid; odorless.\n\n"
                    "Physicochemical Specifications & Statutory Limits:\n"
                    "1. Acidity and Alkalinity (pH): 10 ml with methyl red must not show red; 10 ml with bromothymol blue must not show blue (pH range 5.0 to 7.0).\n"
                    "2. Chloride, Sulfate, and Calcium: 50 ml aliquots examined per compendial procedures show no turbidity or precipitation.\n"
                    "3. Nitrate: Must not exceed 0.06 mg/L (0.06 ppm) tested with diphenylamine sulfuric acid reagent.\n"
                    "4. Nitrite: Must not exceed 0.02 mg/L (0.02 ppm) tested with sulfanilamide and NED dihydrochloride.\n"
                    "5. Ammonia: Must not exceed 0.3 mg/L (0.3 ppm) with alkaline mercuric potassium iodide reagent.\n"
                    "6. Non-volatile Residue: 100 ml evaporated on water bath and dried at 105 C yields no more than 1.0 mg (<= 1 mg / 100ml).\n"
                    "7. Heavy Metals: 40 ml complies with test (<= 0.5 ppm Pb)."
                )
            },
            {
                "section_id": "chp_2025_vol2_water_sec2_conductivity_toc_microbial",
                "page": 2,
                "title_zh": "第二节：电导率三阶段法定检验、总有机碳(TOC)与微生物限度",
                "title_en": "Section 2: Three-Stage Conductivity Test, Total Organic Carbon (TOC) & Microbial Limits",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：纯化水\n\n"
                    "一、电导率（Conductivity）法定三阶段测定标准：\n"
                    "可使用在线或离线电导率仪测定。阶段 1 测定值不得超过对应水温下的法定限度：\n"
                    "- 0℃ ~ 9℃: <= 3.6 μS/cm\n"
                    "- 10℃: <= 3.6 μS/cm\n"
                    "- 20℃: <= 4.3 μS/cm\n"
                    "- 25℃: <= 5.1 μS/cm（基准参考温度）\n"
                    "- 30℃: <= 5.4 μS/cm\n"
                    "- 40℃: <= 6.5 μS/cm\n"
                    "- 50℃: <= 7.5 μS/cm\n"
                    "- 60℃: <= 8.1 μS/cm\n"
                    "- 70℃: <= 9.1 μS/cm\n"
                    "- 80℃: <= 9.7 μS/cm\n"
                    "- 90℃: <= 9.7 μS/cm\n"
                    "- 100℃: <= 10.2 μS/cm\n"
                    "若阶段 1 超过上述限度，需进行阶段 2 剧烈搅拌消除溶解空气（25℃ <= 2.1 μS/cm）及阶段 3 测定。\n\n"
                    "二、总有机碳（TOC）检验：\n"
                    "采用总有机碳测定仪（通则 0682），测定纯化水中的易被氧化的有机物总量。法定合格限度为：总有机碳不得过 0.50 mg/L（<= 0.50 mg/L 或 500 ppb）。也可采用易氧化物化学法作为替代，高锰酸钾滴定液红色不得完全褪去。\n\n"
                    "三、微生物限度：\n"
                    "取本品不少于 1ml，采用薄膜过滤法（通则 1105），以 R2A 琼脂培养基在 30℃ ~ 35℃ 下培养不少于 5 天。好氧菌总数（TAMC）不得过 100 CFU/ml。"
                ),
                "content_en": (
                    "ChP 2025 Vol II Official Monograph: Purified Water (Section 2)\n\n"
                    "1. Electrical Conductivity Three-Stage Statutory Test:\n"
                    "Stage 1 in-line/off-line conductivity thresholds by temperature:\n"
                    "- 0 to 9 C: <= 3.6 uS/cm\n"
                    "- 10 C: <= 3.6 uS/cm\n"
                    "- 20 C: <= 4.3 uS/cm\n"
                    "- 25 C (Reference Standard): <= 5.1 uS/cm\n"
                    "- 30 C: <= 5.4 uS/cm\n"
                    "- 40 C: <= 6.5 uS/cm\n"
                    "- 50 C: <= 7.5 uS/cm\n"
                    "- 60 C: <= 8.1 uS/cm\n"
                    "- 70 C: <= 9.1 uS/cm\n"
                    "- 80-90 C: <= 9.7 uS/cm\n"
                    "- 100 C: <= 10.2 uS/cm\n"
                    "If Stage 1 fails, proceed to Stage 2 (vigorous stirring at 25 C <= 2.1 uS/cm) and Stage 3.\n\n"
                    "2. Total Organic Carbon (TOC, ChP 0682):\n"
                    "Statutory Limit: Must not exceed 0.50 mg/L (500 ppb).\n\n"
                    "3. Microbial Limits (ChP 1105):\n"
                    "Membrane filtration on R2A agar incubated at 30-35 C for >= 5 days: TAMC <= 100 CFU/ml."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_wfi_and_sterile_water",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：注射用水与灭菌注射用水",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Water for Injection (WFI) & Sterile Water for Injection",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_wfi_and_sterile_water_full.pdf",
        "md_file": "chp_2025_vol2_wfi_and_sterile_water_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_wfi_and_sterile_water_full.pdf",
        "sections": [
            {
                "section_id": "chp_2025_vol2_wfi_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：注射用水（WFI）双工艺路径（蒸馏与膜法RO+CEDI+UF）、内毒素与微生物限度",
                "title_en": "Section 1: WFI Dual Production Routes (Distillation & Membrane RO+CEDI+UF), Endotoxins & Bioburden",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：注射用水（Aqua ad Iniectabilia / Water for Injection, WFI）\n\n"
                    "一、重大技术革新与法定工艺来源：\n"
                    "本品为纯化水经蒸馏法或以反渗透（RO）联合连续电去离子（CEDI）及超滤（UF）等反渗透+非蒸馏膜法纯化工艺制备的制药用水。2025年版中国药典二部正式确立膜法制水与蒸馏法在注射用水生产中的法定等效地位。\n\n"
                    "二、法定限度与关键控制项目：\n"
                    "1. 电导率：符合 25℃ <= 1.3 μS/cm（在线）或按温度对照表阶段 1 限度；\n"
                    "2. 总有机碳（TOC）：不得过 0.50 mg/L（<= 500 ppb）；\n"
                    "3. 细菌内毒素（通则 1143 鲎试剂法）：每 1ml 中含内毒素量应小于 0.25 EU（< 0.25 EU/ml）；\n"
                    "4. 微生物限度：取样量不少于 200ml，薄膜过滤法在 R2A 培养基上培养，需氧菌总数（TAMC）不得过 10 CFU/100ml；\n"
                    "5. 生产输送规范：循环管路必须在 70℃ 以上保温循环，或定期进行在线纯蒸汽灭菌（SIP）及臭氧消毒。"
                ),
                "content_en": (
                    "ChP 2025 Vol II: Water for Injection (WFI)\n\n"
                    "1. Statutory Production Innovation: Prepared from purified water by distillation OR equivalent membrane purification processes (RO + CEDI + Ultrafiltration). Distillation and membrane routes are officially equivalent in 2025 edition.\n\n"
                    "2. Specifications:\n"
                    "- In-line Conductivity: <= 1.3 uS/cm at 25 C;\n"
                    "- TOC <= 0.50 mg/L;\n"
                    "- Bacterial Endotoxins (ChP 1143): Less than 0.25 EU/ml;\n"
                    "- Bioburden: TAMC <= 10 CFU/100ml using membrane filtration on R2A agar."
                )
            },
            {
                "section_id": "chp_2025_vol2_wfi_sec2_sterile_wfi",
                "page": 2,
                "title_zh": "第二节：灭菌注射用水无菌保证（通则1101）、不溶性微粒与包装残留物",
                "title_en": "Section 2: Sterile Water for Injection Sterility Assurance (ChP 1101) & Particulate Matter (ChP 0903)",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：灭菌注射用水（Aqua ad Iniectabilia Sterilisata）\n\n"
                    "一、定义与工艺：\n"
                    "本品为注射用水经灭菌工艺制得的无菌制药用水。主要用于注射用灭菌粉末的溶剂或注射剂的稀释剂。\n\n"
                    "二、关键法定控制指标：\n"
                    "1. 无菌检查（通则 1101）：依法检查，经硫乙醇酸盐流体培养基及胰酪大豆胨液体培养基 14 天恒温培养，结果必须符合无菌规定；\n"
                    "2. 细菌内毒素（通则 1143）：含内毒素量小于 0.25 EU/ml；\n"
                    "3. 不溶性微粒（通则 0903 光阻法）：针对标示装量 100ml 以下的注射液：每支含 10μm 及以上微粒不得过 6000 粒；含 25μm 及以上微粒不得过 600 粒；\n"
                    "4. pH 范围：由于灭菌及玻璃/塑料包装溶出，pH 规定放宽至 5.0 ~ 7.0。"
                ),
                "content_en": (
                    "ChP 2025 Vol II: Sterile Water for Injection\n\n"
                    "1. Definition: WFI sterilized in final containers. Used as vehicle/diluent for parenteral powders or injections.\n\n"
                    "2. Critical Limits:\n"
                    "- Sterility (ChP 1101): Complies with 14-day incubation incubation test in FTM and TSB;\n"
                    "- Bacterial Endotoxins: < 0.25 EU/ml;\n"
                    "- Sub-visible Particulate Matter (ChP 0903 Light Obscuration, containers < 100ml): Particles >= 10 um <= 6000/container; particles >= 25 um <= 600/container;\n"
                    "- pH range 5.0 to 7.0."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_metformin_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：盐酸二甲双胍与盐酸二甲双胍片",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Metformin Hydrochloride & Tablets",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_metformin_monograph_full.pdf",
        "md_file": "chp_2025_vol2_metformin_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_metformin_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol2_metformin_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：二甲双胍分子结构、有关物质双氰胺限度(<=0.02%)与溶出度标准",
                "title_en": "Section 1: Metformin Structure, Related Substance Dicyandiamide (<=0.02%) & Dissolution",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：盐酸二甲双胍（Metformini Hydrochloridum）\n\n"
                    "一、原料药分子式与性状：\n"
                    "本品为 1,1-二甲基双胍盐酸盐。分子式：C4H11N5·HCl，分子量：165.62。本品为白色结晶或结晶性粉末；无臭。本品在水中易溶，在乙醇中微溶，在三氯甲烷或乙醚中不溶。熔点：220℃ ~ 225℃。\n\n"
                    "二、有关物质与特征性毒性杂质控制（HPLC 法 通则 0512）：\n"
                    "1. 双氰胺（杂质 A / Dicyandiamide）：双氰胺为合成前体及降解杂质，对肝肾具有潜在蓄积毒性。供试品溶液色谱图中，按外标法以峰面积计算，双氰胺不得过 0.02%（<= 0.02%）；\n"
                    "2. 其他单个杂质：不得过 0.10%；杂质总量：不得过 0.50%；\n"
                    "3. 亚硝胺类基因毒性杂质（NDMA，N-亚硝基二甲胺）：采用 GC-MS/MS 或 LC-MS/MS，限度不得超过 96.0 ng/天（以最大日剂量计算相当于 <= 0.032 ppm）。\n\n"
                    "三、制剂溶出度测定（片剂 通则 0931 第一法 篮法）：\n"
                    "以水 1000ml 为溶出介质，转速为每分钟 100 转，依法操作，经 45 分钟时，取溶液滤过，紫外分光光度法在 233nm 波长测定。溶出量不得少于标示量的 80%（>= 80%）。缓释制剂在 1h（20%~40%）、3h（45%~65%）、10h（>=85%）分阶段控制。"
                ),
                "content_en": (
                    "ChP 2025 Volume II: Metformin Hydrochloride & Tablets\n\n"
                    "1. Structure & Properties: 1,1-Dimethylbiguanide hydrochloride (C4H11N5 HCl, MW 165.62). White crystalline powder, melting point 220-225 C.\n\n"
                    "2. Related Substances (HPLC ChP 0512):\n"
                    "- Dicyandiamide (Impurity A): Precursor/degradation impurity limited to <= 0.02%;\n"
                    "- Any other single impurity <= 0.10%; Total impurities <= 0.50%;\n"
                    "- Genotoxic nitrosamine NDMA strictly controlled (<= 96 ng/day, corresponding to <= 0.032 ppm).\n\n"
                    "3. Dissolution Test (ChP 0931 Method 1 Basket, 100 rpm, Water 1000 ml):\n"
                    "At 45 minutes, not less than 80% of labeled amount dissolved."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_amoxicillin_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：阿莫西林与阿莫西林胶囊",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Amoxicillin & Capsules",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_amoxicillin_monograph_full.pdf",
        "md_file": "chp_2025_vol2_amoxicillin_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_amoxicillin_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol2_amoxicillin_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：阿莫西林高分子聚合物杂质、青霉素降解物与过敏反应控制标准",
                "title_en": "Section 1: High Molecular Polymers, Degradation Impurities & Allergenicity Control",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：阿莫西林（Amoxicillinum）\n\n"
                    "一、来源与分子特性：\n"
                    "本品为 (2S,5R,6R)-3,3-二甲基-6-[(R)-(-)-2-氨基-2-(4-羟基苯基)乙酰氨基]-7-氧代-4-硫杂-1-氮杂双环[3.2.0]庚烷-2-甲酸三水合物。分子式：C16H19N3O5S·3H2O，分子量：419.45。按无水物计算，含 C16H19N3O5S 不得少于 95.0%（原料药）。\n\n"
                    "二、高分子聚合物与致敏杂质控制（分子排阻色谱法 SEC 通则 0514）：\n"
                    "β-内酰胺类抗生素引起严重过敏反应（过敏性休克）的主要致敏原为药物自身在生产和贮藏过程中开环聚合形成的高分子聚合物（Amoxicillin Polymers）：\n"
                    "- 采用葡聚糖凝胶 G-10（Sephadex G-10）或适宜的排阻色谱柱，以含磷酸盐缓冲液为流动相；\n"
                    "- 原料药中阿莫西林聚合物峰面积不得大于对照溶液主峰面积的 0.15%（<= 0.15%）；胶囊剂聚合物不得过 0.40%；\n\n"
                    "三、有关物质（HPLC 法 通则 0512）：\n"
                    "测定阿莫西林开环物（青霉素酸）、阿莫西林二聚体及其杂质 I，单个未知杂质不得过 1.0%，杂质总量不得过 3.0%。\n\n"
                    "四、胶囊剂溶出度检查（通则 0931 浆法）：\n"
                    "以水 900ml 为介质，转速 100 转/分，30 分钟时溶出量不得少于标示量的 80%。"
                ),
                "content_en": (
                    "ChP 2025 Volume II: Amoxicillin & Capsules\n\n"
                    "1. Chemical Formula: (2S,5R,6R)-Amoxicillin trihydrate (C16H19N3O5S 3H2O, MW 419.45).\n\n"
                    "2. High Molecular Weight Polymers (Size Exclusion Chromatography SEC ChP 0514):\n"
                    "Polymers formed by beta-lactam self-condensation constitute primary allergens responsible for anaphylaxis.\n"
                    "- API polymer content limited to <= 0.15%;\n"
                    "- Capsule formulation polymers limited to <= 0.40%.\n\n"
                    "3. Dissolution Test (ChP 0931 Paddle, 100 rpm, Water 900 ml):\n"
                    "At 30 minutes, not less than 80% dissolved."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_atorvastatin_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：阿托伐他汀钙与阿托伐他汀钙片",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Atorvastatin Calcium & Tablets",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_atorvastatin_monograph_full.pdf",
        "md_file": "chp_2025_vol2_atorvastatin_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_atorvastatin_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol2_atorvastatin_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：阿托伐他汀立体异构体对映体、有关物质 HPLC 梯度检验与多晶型要求",
                "title_en": "Section 1: Stereoisomeric Enantiomers, Related Substances HPLC Gradient & Polymorphism",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：阿托伐他汀钙（Atorvastatinum Calcicum）\n\n"
                    "一、化学结构与分子式：\n"
                    "本品为 [R-(R*,R*)]-2-(4-氟苯基)-β,δ-二羟基-5-(1-甲基乙基)-3-苯基-4-[(苯氨基)羰基]-1H-吡咯-1-庚酸钙盐三水合物。分子式：(C33H34FN2O5)2Ca·3H2O，分子量：1209.42。本品为 HMG-CoA 还原酶抑制剂。\n\n"
                    "二、有关物质 HPLC 梯度洗脱测定（通则 0512）：\n"
                    "1. 对映异构体（Enantiomer，手性杂质）：采用手性色谱柱（如 Chiralpak AD-H），对映异构体限度不得过 0.30%；\n"
                    "2. 非对映异构体（Diastereomers）：单个非对映异构体不得过 0.20%；\n"
                    "3. 内酯杂质（Atorvastatin Lactone）：不得过 0.15%；\n"
                    "4. 其他单个未知杂质：不得过 0.10%；杂质总量：不得过 1.0%。\n\n"
                    "三、晶型要求（通则 0451 X射线粉末衍射法 / XRD）：\n"
                    "阿托伐他汀钙存在多种晶型（晶型 I、无定形等），其生物利用度与溶出度高度依赖晶型。原料药生产及制剂必须明确标明并严格控制特定的稳定晶型，X 射线衍射主特征峰位必须完全对应一致。"
                ),
                "content_en": (
                    "ChP 2025 Volume II: Atorvastatin Calcium & Tablets\n\n"
                    "1. Chemical Structure: Calcium salt of (3R,5R)-7-[2-(4-fluorophenyl)-5-isopropyl-3-phenyl-4-(phenylcarbamoyl)pyrrol-1-yl]-3,5-dihydroxyheptanoic acid trihydrate ((C33H34FN2O5)2Ca 3H2O, MW 1209.42).\n\n"
                    "2. Related Substances (HPLC Gradient ChP 0512):\n"
                    "- Enantiomer chiral impurity <= 0.30%;\n"
                    "- Diastereomer impurities <= 0.20%;\n"
                    "- Atorvastatin lactone <= 0.15%; Total impurities <= 1.0%.\n\n"
                    "3. Polymorphic Consistency (X-ray Powder Diffraction XRD ChP 0451):\n"
                    "Specific crystalline or amorphous forms strictly standardized to ensure consistent oral bioavailability."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_aspirin_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：阿司匹林与阿司匹林肠溶片",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Aspirin & Enteric-Coated Tablets",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_aspirin_monograph_full.pdf",
        "md_file": "chp_2025_vol2_aspirin_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_aspirin_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol2_aspirin_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：阿司匹林游离水杨酸(<=0.1%)、熔点与肠溶片耐酸释放度检验",
                "title_en": "Section 1: Free Salicylic Acid (<=0.1%), Melting Point & Acid-Resistant Dissolution",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：阿司匹林（Aspirinum / 乙酰水杨酸）\n\n"
                    "一、原料药法定定义与分子参数：\n"
                    "本品为 2-(乙酰氧基)苯甲酸。含 C9H8O4 应为 99.5% ~ 101.0%（按干燥品计算）。分子量：180.16。\n"
                    "【性状】：本品为白色结晶或结晶性粉末；无臭，微带酸味；在湿空气中易水解为水杨酸和醋酸。在乙醇中易溶，在三氯甲烷或乙醚中溶解，在水或无水乙醚中微溶。熔点：135℃ ~ 140℃。\n\n"
                    "二、鉴别试验：\n"
                    "1. 三氯化铁显色反应：取本品水溶液煮沸放冷后，加三氯化铁试液 1 滴，即显紫堇色（酚羟基络合物）；\n"
                    "2. 碳酸钠水解反应：在碳酸钠试液中煮沸放冷，加过量稀硫酸即析出白色水杨酸沉淀，并散发醋酸臭气。\n\n"
                    "三、游离水杨酸（Free Salicylic Acid）专项杂质限度检验（高效液相色谱法 通则 0512）：\n"
                    "阿司匹林极易水解产生游离水杨酸，引起胃黏膜糜烂与胃溃疡：\n"
                    "- 原料药限度：含游离水杨酸不得过 0.1%（<= 0.1%）；\n"
                    "- 阿司匹林片（普通片）：含游离水杨酸不得过 0.3%（<= 0.3%）；\n"
                    "- 阿司匹林肠溶片：含游离水杨酸不得过 1.5%（<= 1.5%）。\n\n"
                    "四、阿司匹林肠溶片双介质释放度检验（通则 0931 第一法 篮法）：\n"
                    "1. 酸中释放量（耐酸力检验）：在 0.1 mol/L 盐酸溶液中，转速 100 转/分，操作 2 小时，立即取样测定，释放量不得过标示量的 10%（<= 10%）；\n"
                    "2. 缓冲液中释放量：随后将转篮移入 pH 6.8 磷酸盐缓冲液中，继续转动 45 分钟，释放量不得少于标示量的 75%（>= 75%）。"
                ),
                "content_en": (
                    "ChP 2025 Volume II: Aspirin & Enteric-Coated Tablets\n\n"
                    "1. Chemical Definition: 2-(Acetyloxy)benzoic acid (C9H8O4, MW 180.16, mp 135-140 C).\n\n"
                    "2. Free Salicylic Acid Impurity Limits (HPLC ChP 0512):\n"
                    "- API: Not more than 0.1% (<= 0.1%);\n"
                    "- Plain Tablets: Not more than 0.3%;\n"
                    "- Enteric-Coated Tablets: Not more than 1.5%.\n\n"
                    "3. Two-Stage Dissolution Test (ChP 0931 Basket Method):\n"
                    "- Acid Phase (0.1 M HCl, 2 hours): Release <= 10%;\n"
                    "- Buffer Phase (pH 6.8 Phosphate Buffer, 45 min): Release >= 75%."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_paracetamol_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：对乙酰氨基酚（扑热息痛）",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Paracetamol (Acetaminophen)",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_paracetamol_monograph_full.pdf",
        "md_file": "chp_2025_vol2_paracetamol_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_paracetamol_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol2_paracetamol_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：对乙酰氨基酚性状、特征毒性杂质对氨基酚限度(<=0.005%)与有关物质",
                "title_en": "Section 1: Paracetamol Properties, Toxic Impurity 4-Aminophenol (<=0.005%) & Related Substances",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：对乙酰氨基酚（Paracetamolum / 扑热息痛）\n\n"
                    "一、原料药性状与熔点：\n"
                    "本品为 N-(4-羟基苯基)乙酰胺。含 C8H9NO2 必须在 99.0% ~ 101.0% 之间（按干燥品计算）。分子量：151.16。本品为白色结晶或结晶性粉末；无臭，味微苦。在热水或乙醇中易溶，在丙酮中溶解，在水中微溶。熔点：168℃ ~ 172℃。\n\n"
                    "二、专项毒性杂质对氨基酚（4-Aminophenol）限度控制（通则 0512 HPLC 法）：\n"
                    "对氨基酚是对乙酰氨基酚合成前体及水解产物，具有严重的肾毒性及高铁血红蛋白血症诱发毒性：\n"
                    "- 供试品溶液中对氨基酚峰面积不得大于对照品溶液峰面积（严格控制限度：<= 0.005%，即不得过 50 ppm）；\n"
                    "- 有关物质检测中：对氯乙酰苯胺不得过 0.001%（10 ppm）；其他单个未知杂质不得过 0.05%；杂质总量不得过 0.10%。\n\n"
                    "三、制剂溶出度检查（通则 0931 浆法）：\n"
                    "以 pH 5.8 磷酸盐缓冲液 900ml 为介质，转速每分钟 50 转，30 分钟时溶出量不得少于标示量的 80%。"
                ),
                "content_en": (
                    "ChP 2025 Volume II: Paracetamol (Acetaminophen)\n\n"
                    "1. Properties: N-(4-hydroxyphenyl)acetamide (C8H9NO2, MW 151.16, mp 168-172 C).\n\n"
                    "2. Critical Toxic Impurity 4-Aminophenol (HPLC ChP 0512):\n"
                    "- 4-Aminophenol causes severe nephrotoxicity and methemoglobinemia. Compendial limit: Not more than 0.005% (<= 50 ppm);\n"
                    "- 4-Chloroacetanilide <= 0.001% (10 ppm); Total impurities <= 0.10%.\n\n"
                    "3. Dissolution Test (ChP 0931 Paddle, 50 rpm, pH 5.8 buffer 900 ml): >= 80% dissolved at 30 min."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_ibuprofen_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：布洛芬与布洛芬缓释胶囊",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Ibuprofen & Sustained-Release Capsules",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_ibuprofen_monograph_full.pdf",
        "md_file": "chp_2025_vol2_ibuprofen_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_ibuprofen_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol2_ibuprofen_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：布洛芬有关物质杂质 A/B/C/D、熔点与缓释微丸释放度三阶段标准",
                "title_en": "Section 1: Related Substances (Impurities A/B/C/D), mp & 3-Stage Sustained-Release Dissolution",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：布洛芬（Ibuprofenum）\n\n"
                    "一、分子式与理化性状：\n"
                    "本品为 2-(4-异丁基苯基)丙酸。分子式：C13H18O2，分子量：206.28。本品为白色结晶性粉末；气微弱特异，味微苦。在乙醇、三氯甲烷或乙醚中极易溶解，在水中几乎不溶。熔点：75.0℃ ~ 78.0℃。\n\n"
                    "二、有关物质 HPLC 检测（通则 0512）：\n"
                    "1. 4-异丁基苯乙酮（杂质 A）：为合成起始物及光照降解产物，具有光毒性，不得过 0.10%；\n"
                    "2. 杂质 B、C、D 及其他单个未知杂质：不得过 0.10%；杂质总量不得过 0.50%。\n\n"
                    "三、布洛芬缓释胶囊三阶段释放度标准（通则 0931 桨法）：\n"
                    "以 pH 7.2 磷酸盐缓冲液 900ml 为溶出介质，转速 50 转/分，分阶段取样测定：\n"
                    "1. 1 小时释放量：应为标示量的 20% ~ 45%（控制突释）；\n"
                    "2. 4 小时释放量：应为标示量的 50% ~ 75%；\n"
                    "3. 8 小时释放量：不得少于标示量的 80%（>= 80%，保证充分释放）。"
                ),
                "content_en": (
                    "ChP 2025 Volume II: Ibuprofen & Sustained-Release Capsules\n\n"
                    "1. Properties: 2-(4-isobutylphenyl)propanoic acid (C13H18O2, MW 206.28, mp 75.0-78.0 C).\n\n"
                    "2. Related Substances (HPLC ChP 0512):\n"
                    "- 4-Isobutylacetophenone (Impurity A, phototoxic): <= 0.10%;\n"
                    "- Any other single impurity <= 0.10%; Total impurities <= 0.50%.\n\n"
                    "3. Three-Stage Dissolution for Sustained-Release Formulations (pH 7.2 buffer, 50 rpm):\n"
                    "- 1 hour: 20% to 45% (prevents dose dumping);\n"
                    "- 4 hours: 50% to 75%;\n"
                    "- 8 hours: >= 80%."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_saline_and_glucose_injections",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：0.9%氯化钠注射液与葡萄糖注射液",
        "doc_title_en": "ChP 2025 Vol II Official Monograph: Sodium Chloride Injection & Glucose Injections",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol2_saline_and_glucose_injections_full.pdf",
        "md_file": "chp_2025_vol2_saline_and_glucose_injections_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol2_saline_and_glucose_injections_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol2_saline_glucose_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：大容量注射液渗透压摩尔浓度、无菌保证、不溶性微粒与内毒素限度",
                "title_en": "Section 1: Large Volume Parenterals Osmolality, Sterility, Sub-visible Particles & Endotoxin Limits",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：大容量注射液（大输液）\n\n"
                    "一、0.9% 氯化钠注射液（生理盐水）：\n"
                    "本品为氯化钠的灭菌水溶液。含 NaCl 应为标示量的 95.0% ~ 105.0%。pH 值为 4.5 ~ 7.0。\n"
                    "1. 渗透压摩尔浓度（通则 0632 冰点下降法）：应为 260 ~ 320 mOsmol/kg（等渗溶液）；\n"
                    "2. 细菌内毒素（通则 1143）：每 1ml 含内毒素量应小于 0.50 EU（< 0.50 EU/ml）；\n"
                    "3. 不溶性微粒（通则 0903 光阻法）：每 1ml 中含 10μm 以上微粒不得过 25 粒，含 25μm 以上微粒不得过 3 粒；\n"
                    "4. 无菌检查（通则 1101）：必须符合无菌规定。\n\n"
                    "二、葡萄糖注射液（5%、10%、50%）：\n"
                    "本品为 D-葡萄糖一水合物的灭菌水溶液。含 C6H12O6·H2O 应为标示量的 95.0% ~ 105.0%。pH 值为 3.2 ~ 5.5（酸性环境防止葡萄糖灭菌焦化）。\n"
                    "1. 5-羟甲基糠醛（5-HMF）：由于高温灭菌分解产生，采用紫外分光光度法在 284nm 波长测定吸收度不得过 0.25；\n"
                    "2. 细菌内毒素：每 1ml 含内毒素量应小于 0.25 EU（< 0.25 EU/ml）；\n"
                    "3. 葡萄糖氯化钠注射液：兼顾含糖与含盐双重指标，内毒素 < 0.50 EU/ml。"
                ),
                "content_en": (
                    "ChP 2025 Volume II: Sodium Chloride (0.9%) and Glucose (5%, 10%) Injections\n\n"
                    "1. 0.9% Sodium Chloride Injection (Normal Saline):\n"
                    "- Osmolality (ChP 0632): 260 to 320 mOsmol/kg (isotonic);\n"
                    "- Bacterial Endotoxins (ChP 1143): < 0.50 EU/ml;\n"
                    "- Sub-visible Particles (ChP 0903, per ml): >= 10 um <= 25 particles/ml; >= 25 um <= 3 particles/ml;\n"
                    "- Sterility (ChP 1101): Complies with 14-day incubation test.\n\n"
                    "2. Glucose Injection:\n"
                    "- 5-Hydroxymethylfurfural (5-HMF): Absorbance at 284 nm <= 0.25;\n"
                    "- Endotoxins: < 0.25 EU/ml; pH 3.2 to 5.5."
                )
            }
        ]
    }
]
