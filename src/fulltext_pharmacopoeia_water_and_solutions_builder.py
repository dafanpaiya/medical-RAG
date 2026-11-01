"""
Authentic Full-Text Document Builder for Chinese Pharmacopoeia (ChP 2020) Pharmaceutical Water Systems
and Large-Volume Parenterals / Core Solution Monographs.

Covers:
1. ChP 2020 Vol II Monograph: Purified Water (《中国药典》2020年版二部【纯化水】官方正文全文)
2. ChP 2020 Vol II Monograph: Water for Injection & Sterile WFI (【注射用水】与【灭菌注射用水】官方正文全文)
3. ChP 2020 Vol IV General Chapter 0261: Pharmaceutical Water (【通则 0261 制药用水】全文)
4. ChP 2020 Vol II Monographs: Sodium Chloride Injection (0.9% 生理盐水) & Glucose Injection (5%/10%)
"""

def get_pharmacopoeia_water_and_solutions_fulltext_documents():
    docs = []

    # =========================================================================
    # 1. ChP 2020 Vol II Monograph: Purified Water (纯化水)
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_vol2_purified_water",
        "doc_title": "《中华人民共和国药典》2020年版二部 品种正文：纯化水",
        "doc_title_zh": "《中华人民共和国药典》2020年版二部 品种正文：纯化水",
        "doc_title_en": "ChP 2020 Vol II Official Monograph: Purified Water (Aqua Purificata)",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol2_purified_water_monograph_full.md",
        "version": "2020-ChP-Vol2-Official",
        "sections": [
            {
                "section_id": "water_sec1_monograph_specs",
                "section_title": "纯化水正文第一节：来源定义、性状、酸碱度、硝酸盐/亚硝酸盐、氨、不挥发物与重金属",
                "section_title_en": "Section 1: Definition, Appearance, pH, Nitrate, Nitrite, Ammonia & Heavy Metals",
                "pages": [1],
                "content_zh": (
                    "《中华人民共和国药典》2020年版二部 品种正文：纯化水（Aqua Purificata）\n\n"
                    "一、来源与性状：\n"
                    "1. 来源与法定定义：本品为饮用水经蒸馏法、离子交换法、反渗透法或其他适宜的方法制得的制药用水。不得添加任何抑菌剂或其他添加剂。\n"
                    "2. 性状：本品为无色的澄清液体；无臭。\n\n"
                    "二、理化检查项与法定限度要求：\n"
                    "1. 酸碱度（pH）：取本品 10ml，加甲基红指示液 2 滴，不得显红色；另取 10ml，加溴百里香酚蓝指示液 5 滴，不得显蓝色（控制酸碱度范围约为 pH 5.0 ~ 7.0）。\n"
                    "2. 氯化物、硫酸盐与钙盐：取本品各依法检查，均不得发生浑浊或沉淀。\n"
                    "3. 硝酸盐（Nitrate）：取本品 5ml，置试管中，于冰浴中冷却，加 10% 氯化钾溶液 0.4ml 与 0.1% 二苯胺硫酸溶液 0.1ml，摇匀，缓缓滴加硫酸 5ml，摇匀，于 50℃ 水浴中放置 15 分钟，溶液产生的蓝色与标准硝酸盐对照液比较，不得更深（法定限度：不得过 0.000006%，即 0.06 ppm / 0.06 μg/ml）。\n"
                    "4. 亚硝酸盐（Nitrite）：取本品 10ml，加对氨基苯磺酰胺稀盐酸溶液 5ml 与盐酸萘乙二胺溶液 1ml，摇匀，放置 10 分钟，溶液产生的粉红色与标准亚硝酸盐对照液比较，不得更深（法定限度：不得过 0.000002%，即 0.02 ppm / 0.02 μg/ml）。\n"
                    "5. 氨（Ammonia）：取本品 50ml，加碱性碘化汞钾试液（奈氏试剂）2ml，放置 15 分钟；显色与氯化铵标准溶液比较，不得更深（法定限度：不得过 0.00003%，即 0.3 ppm / 0.3 μg/ml）。\n"
                    "6. 不挥发物（Non-volatile Matter）：取本品 100ml，置于 105℃ 干燥至恒重的蒸发皿中，在水浴上蒸干，并在 105℃ 干燥至恒重，遗留残渣不得过 1 mg（即残渣限量不得过 0.001%）。\n"
                    "7. 重金属（Heavy Metals）：取本品 40ml，加醋酸盐缓冲液（pH 3.5）2ml 与硫代乙酰胺试液 2ml，显色不得深于标准铅对照液（法定限度：不得过千万分之五，即 <= 0.5 ppm）。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2020 Volume II Monograph: Purified Water (Aqua Purificata)\n\n"
                    "1. Definition and Physical Properties:\n"
                    "- Source: Water obtained from drinking water by distillation, ion exchange, reverse osmosis (RO), or other suitable methods. Contains no added substances.\n"
                    "- Description: Clear, colorless liquid; odorless.\n\n"
                    "2. Chemical Specifications and Limits:\n"
                    "- Acidity/Alkalinity (pH): 10ml with methyl red indicator does not turn red; 10ml with bromothymol blue indicator does not turn blue (pH ~ 5.0 to 7.0).\n"
                    "- Chlorides, Sulfates, Calcium: Negative for opalescence or precipitate.\n"
                    "- Nitrate (NO3-): Diphenylamine sulfuric acid assay in 50°C bath; color intensity does not exceed standard (Limit: <= 0.000006%, 0.06 ppm).\n"
                    "- Nitrite (NO2-): Diazotization with sulfanilamide and NED dihydrochloride; pink color does not exceed standard (Limit: <= 0.000002%, 0.02 ppm).\n"
                    "- Ammonia (NH4+): Nessler's reagent assay; yellow color does not exceed ammonium chloride standard (Limit: <= 0.00003%, 0.3 ppm).\n"
                    "- Non-Volatile Matter: 100ml evaporated on water bath and dried at 105°C to constant weight; residue <= 1 mg (<= 0.001%).\n"
                    "- Heavy Metals: Thioacetamide colorimetric test; limit does not exceed <= 0.5 ppm."
                )
            },
            {
                "section_id": "water_sec2_conductivity_toc_microbial",
                "section_title": "纯化水正文第二节：电导率法定温度对照表、总有机碳（TOC）与微生物限度（100 CFU/ml）",
                "section_title_en": "Section 2: Conductivity Limits Table, Total Organic Carbon (TOC) & Microbial Limit",
                "pages": [2],
                "content_zh": (
                    "《中华人民共和国药典》2020年版二部 品种正文：纯化水\n\n"
                    "一、电导率（Conductivity）法定检测标准：\n"
                    "可使用在线或离线电导率测定仪测定。供试品的电导率测定值不得超过对应水温下的法定限度：\n\n"
                    "| 水温 (°C) | 电导率法定最大允许限度 (μS/cm) |\n"
                    "| :--- | :--- |\n"
                    "| 0 ~ 9 | <= 3.6 |\n"
                    "| 10 | <= 3.6 |\n"
                    "| 20 | <= 4.3 |\n"
                    "| 25 (标准室温) | <= 5.1 |\n"
                    "| 30 | <= 5.4 |\n"
                    "| 40 | <= 6.5 |\n"
                    "| 50 | <= 7.5 |\n"
                    "| 60 | <= 8.1 |\n"
                    "| 70 | <= 9.1 |\n"
                    "| 80 | <= 9.7 |\n"
                    "| 90 | <= 10.3 |\n"
                    "| 100 | <= 10.7 |\n\n"
                    "二、总有机碳（TOC）或易氧化物（二选一）：\n"
                    "1. 总有机碳（TOC）：采用经过系统适用性试验（蔗糖和 1,4-苯醌验证，回收率 85% ~ 115%）的 TOC 分析仪在线或离线测定。纯化水总有机碳限度：不得过 0.50 mg/L（即 500 μg/L 或 0.50 ppm）。\n"
                    "2. 易氧化物（化学替代法）：取本品 100ml，加稀硫酸 10ml，煮沸后加高锰酸钾滴定液（0.02 mol/L）0.10ml，再煮沸 5 分钟，粉红色不得完全消失。\n\n"
                    "三、微生物限度（Microbial Limits）：\n"
                    "1. 测定规程：按照中国药典非无菌药品微生物限度检查法（通则 1105、1106）检查，必须采用薄膜过滤法；\n"
                    "2. 培养基与培养条件：采用低营养的 R2A 琼脂培养基，培养温度为 30℃ ~ 35℃，培养时间不少于 5 天；\n"
                    "3. 法定合格判定限度：需氧菌总数不得过 100 CFU/ml（<= 100 CFU/ml）。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2020 Volume II Monograph: Purified Water\n\n"
                    "1. Temperature-Compensated Conductivity Limits:\n"
                    "Measured inline or offline; electrical conductivity must not exceed the following limits:\n\n"
                    "| Temperature (°C) | Maximum Conductivity Limit (μS/cm) |\n"
                    "| :--- | :--- |\n"
                    "| 0 to 9 | <= 3.6 |\n"
                    "| 10 | <= 3.6 |\n"
                    "| 20 | <= 4.3 |\n"
                    "| 25 (Standard Ambient) | <= 5.1 |\n"
                    "| 30 | <= 5.4 |\n"
                    "| 40 | <= 6.5 |\n"
                    "| 50 | <= 7.5 |\n"
                    "| 60 | <= 8.1 |\n"
                    "| 70 | <= 9.1 |\n"
                    "| 80 | <= 9.7 |\n"
                    "| 90 | <= 10.3 |\n"
                    "| 100 | <= 10.7 |\n\n"
                    "2. Total Organic Carbon (TOC) / Oxidizable Substances:\n"
                    "- Total Organic Carbon (TOC): Calibrated with sucrose and 1,4-benzoquinone (85%-115% recovery); Limit: Not more than 0.50 mg/L (500 μg/L / 0.50 ppm).\n"
                    "- Oxidizable Substances Alternative: 100ml with 10ml dilute H2SO4 and 0.10ml 0.02 mol/L KMnO4 boiled for 5 minutes; pink color must not completely fade.\n\n"
                    "3. Microbial Limit:\n"
                    "- Membrane filtration method using low-nutrient R2A agar.\n"
                    "- Incubation: 30°C to 35°C for not less than 5 days.\n"
                    "- Acceptance Criterion: Total Aerobic Microbial Count (TAMC) <= 100 CFU/ml."
                )
            }
        ]
    })

    # =========================================================================
    # 2. ChP 2020 Vol II Monograph: Water for Injection & Sterile WFI
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_vol2_wfi_sterile_water",
        "doc_title": "《中华人民共和国药典》2020年版二部 品种正文：注射用水与灭菌注射用水",
        "doc_title_zh": "《中华人民共和国药典》2020年版二部 品种正文：注射用水与灭菌注射用水",
        "doc_title_en": "ChP 2020 Vol II Official Monographs: Water for Injection (WFI) & Sterile WFI",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol2_wfi_and_sterile_water_full.md",
        "version": "2020-ChP-Vol2-Official",
        "sections": [
            {
                "section_id": "wfi_sec1_monograph_specs",
                "section_title": "注射用水正文第一节：蒸馏法来源、细菌内毒素（< 0.25 EU/ml）与微生物限度（10 CFU/100ml）",
                "section_title_en": "Section 1: WFI Distillation, Bacterial Endotoxins (< 0.25 EU/ml) & Bioburden",
                "pages": [1],
                "content_zh": (
                    "《中华人民共和国药典》2020年版二部 品种正文：注射用水（Aqua ad Iniectabilia / WFI）\n\n"
                    "一、来源与制备工艺原则：\n"
                    "1. 法定定义：本品为纯化水经蒸馏所制得的水。必须采用多效蒸馏水机或热压式蒸馏水机蒸馏制备，不含任何添加剂。\n"
                    "2. 质量控制要求：除细菌内毒素与微生物限度外，注射用水必须符合【纯化水】项下的全部理化检查要求（包括酸碱度、氯化物、硫酸盐、钙盐、硝酸盐 <= 0.06 ppm、亚硝酸盐 <= 0.02 ppm、氨 <= 0.3 ppm、电导率、TOC <= 0.50 mg/L、不挥发物 <= 1 mg/100ml、重金属 <= 0.5 ppm）。\n\n"
                    "二、关键无菌注射剂核心控制指标：\n"
                    "1. 细菌内毒素（Bacterial Endotoxins）：\n"
                    "   - 检查方法：按照中国药典细菌内毒素检查法（通则 1143），采用鲎试剂（TAL）凝胶法或光度测定法；\n"
                    "   - 法定合格标准：每 1ml 注射用水中含内毒素量应小于 0.25 EU（< 0.25 EU/ml）。\n"
                    "2. 微生物限度（Bioburden / Microbial Limit）：\n"
                    "   - 测定方法：薄膜过滤法，取样量不得少于 200ml；\n"
                    "   - 培养基与培养：过滤薄膜贴于 R2A 琼脂培养基平板，于 30℃ ~ 35℃ 培养不少于 5 天；\n"
                    "   - 法定限度标准：需氧菌总数不得过 10 CFU/100ml（<= 10 CFU/100ml，即平均每 10ml 不得过 1 CFU）。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2020 Volume II Monograph: Water for Injection (WFI)\n\n"
                    "1. Source and Production Requirements:\n"
                    "- Source: Water obtained by distillation of Purified Water using multi-effect or vapor compression stills. Contains no added substances.\n"
                    "- Physical/Chemical Compliance: Must meet all chemical tests for Purified Water (pH, nitrate, nitrite, ammonia, conductivity, TOC <= 0.50 mg/L, non-volatile residue <= 1 mg/100ml, heavy metals <= 0.5 ppm).\n\n"
                    "2. Critical Biological Release Specifications:\n"
                    "- Bacterial Endotoxins (BET, General Chapter 1143): Less than 0.25 EU/ml (< 0.25 EU/ml).\n"
                    "- Microbial Limit (TAMC): Membrane filtration of not less than 200ml sample onto R2A agar; incubated at 30°C-35°C for not less than 5 days; Acceptance criterion: TAMC <= 10 CFU / 100ml."
                )
            },
            {
                "section_id": "wfi_sec2_sterile_water_injection",
                "section_title": "灭菌注射用水正文第二节：无菌检查（通则 1101，14天）与不溶性微粒控制",
                "section_title_en": "Section 2: Sterile WFI Sterility Test (General Chapter 1101) & Particulate Matter",
                "pages": [2],
                "content_zh": (
                    "《中华人民共和国药典》2020年版二部 品种正文：灭菌注射用水（Aqua ad Iniectabilia Sterilisata）\n\n"
                    "一、来源与临床用途：\n"
                    "本品为注射用水照注射剂生产工艺灌装与最终灭菌制备所得。用于注射用灭菌粉末的溶剂或注射液的稀释剂。\n\n"
                    "二、法定质量标准：\n"
                    "1. 无菌检查（Sterility Test）：\n"
                    "   - 按照中国药典无菌检查法（通则 1101）薄膜过滤法检查；\n"
                    "   - 采用硫乙醇酸盐流体培养基（FTM，30℃ ~ 35℃）和胰酪大豆胨液体培养基（TSB，20℃ ~ 25℃）双套培养，法定培养观察期必须满 14 天；\n"
                    "   - 判定标准：应符合规定（14天培养期内培养基无任何微生物混浊生长）。\n"
                    "2. 细菌内毒素：每 1ml 中含内毒素量应小于 0.25 EU（< 0.25 EU/ml）。\n"
                    "3. 不溶性微粒（Sub-visible Particulate Matter）：\n"
                    "   - 按照注射剂通则 0102 及不溶性微粒检查法（通则 0903）光阻法测定；\n"
                    "   - 标示装量 100ml 以下的包装：每容器中含 10 μm 及以上微粒不得过 6000 粒；含 25 μm 及以上微粒不得过 600 粒；\n"
                    "   - 标示装量 100ml 及以上的包装：每 1ml 中含 10 μm 及以上微粒不得过 25 粒；含 25 μm 及以上微粒不得过 3 粒。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2020 Volume II Monograph: Sterile Water for Injection\n\n"
                    "1. Scope and Indication:\n"
                    "Prepared from Water for Injection filled and terminally sterilized in accordance with finished parenteral standards. Used as diluent for parenteral powders or concentrated solutions.\n\n"
                    "2. Compendial Release Specifications:\n"
                    "- Sterility Test (General Chapter 1101): Membrane filtration method into Fluid Thioglycollate Medium (FTM, 30-35°C) and Tryptic Soy Broth (TSB, 20-25°C) incubated for a minimum of 14 days; Complies if no microbial growth is observed.\n"
                    "- Bacterial Endotoxins: < 0.25 EU/ml.\n"
                    "- Sub-Visible Particulate Matter (General Chapter 0903 Light Obscuration):\n"
                    "  * Volume < 100ml: Particles >= 10 μm <= 6,000 per container; particles >= 25 μm <= 600 per container.\n"
                    "  * Volume >= 100ml: Particles >= 10 μm <= 25 particles/ml; particles >= 25 μm <= 3 particles/ml."
                )
            }
        ]
    })

    # =========================================================================
    # 3. ChP 2020 Vol IV General Chapter 0261: Pharmaceutical Water
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_vol4_general_chapter_0261_water",
        "doc_title": "《中华人民共和国药典》2020年版四部 通则 0261 制药用水通则",
        "doc_title_zh": "《中华人民共和国药典》2020年版四部 通则 0261 制药用水通则",
        "doc_title_en": "ChP 2020 Vol IV General Chapter 0261: Pharmaceutical Water General Chapter",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol4_general_chapter_0261_pharmaceutical_water_full.md",
        "version": "2020-ChP-Vol4-Official",
        "sections": [
            {
                "section_id": "chp0261_sec1_classification_selection",
                "section_title": "通则 0261 第一节：制药用水四级分类体系与生产工艺各阶段用水选择矩阵表",
                "section_title_en": "Section 1: Four-Tier Water Classification & GMP Process Application Matrix",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0261 制药用水：\n\n"
                    "一、制药用水四级法定分类定义：\n"
                    "制药用水是指药品生产过程中使用的水，包含：\n"
                    "1. 饮用水（Drinking Water）：指天然水经净化、消毒处理符合国家生活饮用水标准（GB 5749）的水，主要用于设备初洗、非无菌原料药合成前期的初始反应；\n"
                    "2. 纯化水（Purified Water）：饮用水经蒸馏、反渗透（RO）、电去离子（EDI）等脱盐软化处理制成，不含添加剂，用于非无菌药品的配制、原料药精制、直接接触药品的设备清洗最后淋洗；\n"
                    "3. 注射用水（WFI）：纯化水经多效或气压蒸馏制成，不含添加剂，内毒素 < 0.25 EU/ml，微生物 <= 10 CFU/100ml，用于无菌注射剂的配制及无菌器具最后冲洗；\n"
                    "4. 灭菌注射用水：注射用水灌装灭菌后的无菌溶剂。\n\n"
                    "二、药品生产各环节用水法定选择标准表：\n\n"
                    "| 生产环节与工艺用途 | 法定最低用水标准 | 推荐监控重点 |\n"
                    "| :--- | :--- | :--- |\n"
                    "| 口服固体制剂（片剂/胶囊）制粒配料 | 纯化水 | 微生物限度 <= 100 CFU/ml、电导率 |\n"
                    "| 口服液体制剂、外用制剂配料 | 纯化水 | 微生物限度、TOC <= 0.50 mg/L |\n"
                    "| 无菌药品（小容量/大容量注射剂）处方配液 | 注射用水 (WFI) | 细菌内毒素 < 0.25 EU/ml、微生物 <= 10 CFU/100ml |\n"
                    "| 冻干无菌粉针剂配液 | 注射用水 (WFI) | 细菌内毒素、无菌保证 |\n"
                    "| 直接接触无菌药品的包装容器与胶塞最终精洗 | 注射用水 (WFI) | 细菌内毒素、不溶性微粒 |\n"
                    "| 非无菌药品生产设备与容器最终淋洗 | 纯化水 | 电导率、微生物限度 |\n"
                    "| 注射用无菌原料药的结晶与精制洗涤 | 注射用水 (WFI) | 细菌内毒素、TOC |"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2020 Volume IV General Chapter 0261: Pharmaceutical Water\n\n"
                    "1. Four-Tier Classification:\n"
                    "- Drinking Water: Complies with national potable water standard GB 5749; used for initial equipment washing and early chemical synthesis.\n"
                    "- Purified Water: Prepared from drinking water via RO, EDI, or distillation. Used for non-sterile formulations, excipient dissolution, and final rinsing of non-sterile equipment.\n"
                    "- Water for Injection (WFI): Distilled from Purified Water. Mandatory for sterile injectables and final rinsing of components coming into direct contact with sterile drugs.\n"
                    "- Sterile WFI: Packaged and terminally sterilized WFI used as sterile reconstituting solvent.\n\n"
                    "2. GMP Process Application Selection Matrix:\n\n"
                    "| Process Step | Mandatory Grade | Critical Quality Attributes |\n"
                    "| :--- | :--- | :--- |\n"
                    "| Oral Solid Dosage (Granulation) | Purified Water | Microbial <= 100 CFU/ml, Conductivity |\n"
                    "| Oral Liquids & Topical Preparations | Purified Water | TAMC <= 100 CFU/ml, TOC <= 0.50 mg/L |\n"
                    "| Sterile Injectable Formulations (SVP/LVP) | Water for Injection | Endotoxin < 0.25 EU/ml, Bioburden <= 10 CFU/100ml |\n"
                    "| Lyophilized Sterile Powders | Water for Injection | Bacterial Endotoxins, Sterility Assurance |\n"
                    "| Final Rinse of Sterile Primary Packaging | Water for Injection | Endotoxins, Particulate Matter |\n"
                    "| Final Rinse of Non-Sterile Equipment | Purified Water | Conductivity, Bioburden |\n"
                    "| Final Crystallization of Sterile API | Water for Injection | Endotoxins, TOC |"
                )
            },
            {
                "section_id": "chp0261_sec2_piping_sanitization",
                "section_title": "通则 0261 第二节：制药用水管路工程设计（316L 不锈钢、3D 盲管规则、70℃ 保温循环）与消毒",
                "section_title_en": "Section 2: Engineering Design (316L SS, 3D Dead-Leg Rule, 70°C Hot Loop) & Sanitization",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0261 制药用水：\n\n"
                    "一、水系统管路工程设计与防止生物膜（Biofilm）控制准则：\n"
                    "1. 管道与储罐材质：纯化水及注射用水储罐与输送管道必须采用卫生级不锈钢（接触注射用水推荐采用 316L 超低碳不锈钢），与水接触内表面必须进行机械研磨或电解抛光，内表面粗糙度必须达到 Ra <= 0.4 μm（或 Ra <= 0.6 μm），管道焊接必须采用全自动轨道氩气保护焊；\n"
                    "2. 死水段（盲管）控制：管路设计严禁存在死角与盲管。盲管长度（从主管道中心线至盲端距离）必须严格遵守 3D 规则（即盲管长度不得超过支管内径的 3 倍），高卫生要求推荐控制在 1.5D 以内；\n"
                    "3. 循环流速控制：注射用水系统必须采用连续循环回路管网设计。回水管道流速必须维持在 1.0 m/s 以上（雷诺数 Re > 10,000，保持完全湍流状态以冲刷管壁抑制细菌附着与生物膜形成）。\n\n"
                    "二、储存温度与系统消毒规程：\n"
                    "1. 热循环储存（推荐）：注射用水储罐和循环回路必须在 70℃ 以上恒温循环保温储存（通常保持在 75℃ ~ 80℃），或在 4℃ 以下低温循环储存；\n"
                    "2. 周期性灭菌消毒规程：\n"
                    "   - 纯化水系统：定期采用巴氏消毒法（80℃ 热水循环不少于 1 小时）、臭氧在线消毒（维持水中臭氧浓度 0.1 ~ 0.2 ppm 至少 30 分钟）或化学消毒剂（过氧化氢/过氧乙酸）循环冲洗；\n"
                    "   - 注射用水系统：定期采用纯蒸汽灭菌（SIP，蒸汽温度 >= 121℃，保温保压不少于 30 分钟）或过热水在线灭菌；\n"
                    "3. 日常监控频率：纯化水每周至少进行一次全项目检验，注射用水使用点（POU）每日必须轮流取样进行电导率、TOC、微生物限度及细菌内毒素全检。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2020 Volume IV General Chapter 0261: Pharmaceutical Water\n\n"
                    "1. Piping Engineering and Biofilm Prevention Rules:\n"
                    "- Material of Construction: Storage tanks and distribution loops must be fabricated from sanitary stainless steel (316L SS for WFI); electropolished internal surface finish Ra <= 0.4 μm; automatic orbital welding with inert argon shielding.\n"
                    "- Dead-Leg Minimization: Strict adherence to the 3D dead-leg rule (distance from main line center to dead end <= 3 times pipe diameter; 1.5D preferred).\n"
                    "- Turbulent Flow Velocity: Return loop velocity maintained >= 1.0 m/s (Reynolds number Re > 10,000) to prevent biofilm adhesion.\n\n"
                    "2. Temperature Maintenance and Sanitization Protocols:\n"
                    "- Continuous Hot Loop: WFI stored and distributed under continuous recirculation at >= 70°C (typically 75°C-80°C) or cold recirculation at <= 4°C.\n"
                    "- System Sanitization:\n"
                    "  * Purified Water: Pasteurization (80°C hot water recirculation for >= 1 hour), ozone sanitization (0.1-0.2 ppm dissolved ozone for >= 30 min), or chemical sanitization (H2O2 / peracetic acid).\n"
                    "  * Water for Injection: Pure steam sterilization (SIP at >= 121°C for >= 30 minutes) or superheated water sanitization.\n"
                    "- Monitoring Routine: Purified water tested weekly for all attributes; WFI points of use (POU) sampled daily on rotation for conductivity, TOC, endotoxin, and TAMC."
                )
            }
        ]
    })

    # =========================================================================
    # 4. ChP 2020 Vol II Monographs: Large-Volume Parenterals (Saline & Glucose)
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_vol2_saline_glucose_injections",
        "doc_title": "《中华人民共和国药典》2020年版二部 大容量注射剂核心品种：氯化钠注射液与葡萄糖注射液",
        "doc_title_zh": "《中华人民共和国药典》2020年版二部 大容量注射剂核心品种：氯化钠注射液与葡萄糖注射液",
        "doc_title_en": "ChP 2020 Vol II Large-Volume Parenterals: Sodium Chloride Injection & Glucose Injection",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol2_saline_and_glucose_injections_full.md",
        "version": "2020-ChP-Vol2-Official",
        "sections": [
            {
                "section_id": "lvp_sec1_nacl_saline_specs",
                "section_title": "第一节：0.9% 氯化钠注射液法定标准（标示量 95%~105%、pH 4.5~7.0、渗透压、内毒素 < 0.50 EU/ml）",
                "section_title_en": "Section 1: 0.9% Sodium Chloride Injection (Assay 95%-105%, Osmolality, Endotoxin)",
                "pages": [1],
                "content_zh": (
                    "《中华人民共和国药典》2020年版二部 品种正文：氯化钠注射液（Sodium Chloride Injection, 0.9%）\n\n"
                    "一、处方与标示量标准：\n"
                    "1. 处方规格：含氯化钠（NaCl）按标示量计应为 95.0% ~ 105.0%（即 0.855% ~ 0.945% g/ml）；\n"
                    "2. 性状：本品为无色的澄明液体；味微咸。\n\n"
                    "二、法定检查与放行限度：\n"
                    "1. 酸碱度（pH）：应为 4.5 ~ 7.0（通则 0631 测定）；\n"
                    "2. 渗透压摩尔浓度（Osmolality）：按照冰点下降法（通则 0632）检查，应为 260 ~ 320 mOsmol/kg（等渗溶液标准）；\n"
                    "3. 重金属：取本品 50ml，依法检查，含重金属不得过千万分之三（<= 0.3 ppm）；\n"
                    "4. 不溶性微粒（通则 0903）：光阻法测定，每 1ml 中含 10 μm 及以上微粒不得过 25 粒；含 25 μm 及以上微粒不得过 3 粒；\n"
                    "5. 细菌内毒素（通则 1143）：每 1ml 氯化钠注射液中含内毒素量应小于 0.50 EU（< 0.50 EU/ml）；\n"
                    "6. 无菌检查（通则 1101）：应符合规定（薄膜过滤法双培养基 14 天培养无菌生长）。\n\n"
                    "三、含量测定方法（硝酸银滴定法）：\n"
                    "精密量取本品 10ml，加水 40ml，加糊精溶液 5ml 与荧光黄指示液 5 滴，用硝酸银滴定液（0.1 mol/L）滴定至浑浊液由黄绿色变为微红色。每 1ml 硝酸银滴定液（0.1 mol/L）相当于 5.844 mg 的 NaCl。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2020 Volume II: Sodium Chloride Injection (0.9% Normal Saline)\n\n"
                    "1. Assay & Identification:\n"
                    "- Strength: Contains 95.0% to 105.0% of labeled amount of NaCl (0.855% to 0.945% w/v).\n"
                    "- Description: Clear, colorless liquid; faintly salty taste.\n\n"
                    "2. Quality Release Specifications:\n"
                    "- pH Value: 4.5 to 7.0 (General Chapter 0631).\n"
                    "- Osmolality (Freezing Point Depression, General Chapter 0632): 260 to 320 mOsmol/kg.\n"
                    "- Heavy Metals: <= 0.3 ppm.\n"
                    "- Sub-Visible Particles (General Chapter 0903): >= 10 μm <= 25 particles/ml; >= 25 μm <= 3 particles/ml.\n"
                    "- Bacterial Endotoxins (General Chapter 1143): Less than 0.50 EU/ml (< 0.50 EU/ml).\n"
                    "- Sterility (General Chapter 1101): Complies with 14-day membrane filtration incubation.\n\n"
                    "3. Quantitative Assay Method: Titration with 0.1 mol/L AgNO3 using fluorescein indicator."
                )
            },
            {
                "section_id": "lvp_sec2_glucose_injection_specs",
                "section_title": "第二节：葡萄糖注射液法定标准（pH 3.2~5.5、5-HMF 吸光度 <= 0.32、内毒素 < 0.25 EU/ml）",
                "section_title_en": "Section 2: Glucose Injection (pH 3.2-5.5, 5-HMF Absorbance <= 0.32, Endotoxin)",
                "pages": [2],
                "content_zh": (
                    "《中华人民共和国药典》2020年版二部 品种正文：葡萄糖注射液（Glucose Injection, 5% / 10%）\n\n"
                    "一、标示量与理化属性：\n"
                    "1. 标示量：含葡萄糖（C6H12O6·H2O）应为标示量的 95.0% ~ 105.0%；\n"
                    "2. 性状：本品为无色或几乎无色的澄明液体；味甜。\n\n"
                    "二、法定关键检查项与安全限度：\n"
                    "1. 酸碱度（pH）：应为 3.2 ~ 5.5（微酸性，防止湿热灭菌过程中葡萄糖分子高温焦化分解）；\n"
                    "2. 5-羟甲基糠醛（5-HMF，焦化降解杂质）：\n"
                    "   - 测定方法：精密量取本品适量，加水稀释制成每 1ml 中含葡萄糖 20 mg 的溶液，在 284 nm 波长处测定吸光度（通则 0401）；\n"
                    "   - 合格限度：吸光度不得过 0.32（<= 0.32），严格限制毒性杂质 5-羟甲基糠醛残留；\n"
                    "3. 细菌内毒素（通则 1143）：每 1ml 葡萄糖注射液中含内毒素量应小于 0.25 EU（< 0.25 EU/ml）；\n"
                    "4. 不溶性微粒与无菌：每 1ml 中 >= 10 μm 微粒 <= 25 粒，>= 25 μm 微粒 <= 3 粒；无菌检查 14 天培养符合规定。\n\n"
                    "三、含量测定方法（旋光度法）：\n"
                    "按通则 0621 测定旋光度，计算公式：$C = \\frac{\\alpha}{2.0852 \\times l}$，其中 $\\alpha$ 为测得的旋光度，$l$ 为测定管长度（dm），2.0852 为葡萄糖的比旋度常数比率。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia (ChP) 2020 Volume II: Glucose / Dextrose Injection (5% / 10%)\n\n"
                    "1. Assay & Identification:\n"
                    "- Strength: Contains 95.0% to 105.0% of labeled glucose (C6H12O6·H2O).\n"
                    "- Description: Clear, colorless or almost colorless liquid; sweet taste.\n\n"
                    "2. Critical Quality Specifications:\n"
                    "- pH Value: 3.2 to 5.5 (Acidic to suppress heat degradation and caramelization during autoclaving).\n"
                    "- 5-Hydroxymethylfurfural (5-HMF Degradant, General Chapter 0401): Absorbance at 284 nm must not exceed 0.32 (<= 0.32).\n"
                    "- Bacterial Endotoxins: Less than 0.25 EU/ml (< 0.25 EU/ml).\n"
                    "- Particulate Matter & Sterility: >= 10 μm <= 25 / ml; >= 25 μm <= 3 / ml; 14-day Sterility Test compliant.\n\n"
                    "3. Assay Method: Optical rotation measurement at 20°C (General Chapter 0621)."
                )
            }
        ]
    })

    return docs
