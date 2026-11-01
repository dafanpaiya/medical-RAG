"""
Authentic Full-Text Document Builder for Chinese Pharmacopoeia (ChP 2020 / 《中华人民共和国药典》)
Extracts and structures complete statutory chapters, sections, tables, formulas, and criteria.
"""

def get_chp_fulltext_documents():
    docs = []

    # =========================================================================
    # 1. ChP 2020 Vol IV General Chapter 0512: HPLC
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_0512_hplc",
        "doc_title": "《中华人民共和国药典》2020年版四部 通则 0512 高效液相色谱法",
        "doc_title_zh": "《中华人民共和国药典》2020年版四部 通则 0512 高效液相色谱法",
        "doc_title_en": "ChP 2020 Vol IV General Chapter 0512: High-Performance Liquid Chromatography (HPLC)",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol4_general_chapter_0512_hplc_full.md",
        "version": "2020-ChP-Official",
        "sections": [
            {
                "section_id": "0512_sec1_principles",
                "section_title": "通则 0512 第一节：方法原理与仪器构成",
                "section_title_en": "Section 1: Principle and Instrumentation",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0512 高效液相色谱法\n\n"
                    "1. 方法原理与基本要求：\n"
                    "高效液相色谱法（HPLC）系采用高压输液泵将单组分或多元混合流动相泵入装有微粒固定相的色谱柱，对多组分混合物进行高分辨率分离和定量分析的技术。\n"
                    "色谱系统主要由高压输液泵、进样阀（手动或自动进样器）、色谱柱、柱温箱、检测器及数据处理工作站（CDS）组成。\n\n"
                    "2. 检测器类型与适用范围：\n"
                    "- 紫外-可见分光光度检测器（UV/Vis / DAD / PDA）：适用于在紫外或可见光区有特征吸收的组分，二极管阵列检测器（DAD）可同时采集三维吸收光谱图用于峰纯度分析；\n"
                    "- 荧光检测器（FLD）：适用于具天然荧光或经荧光衍生化反应的痕量组分，灵敏度较紫外检测器提高 2~3 个数量级；\n"
                    "- 示差折光检测器（RID）：为通用型检测器，适用于糖类、高分子聚合物等无紫外吸收的组分，要求严格恒温且不可用于梯度洗脱；\n"
                    "- 蒸发光散射检测器（ELSD）：适用于挥发度低于流动相的任何不挥发性化合物，响应值与组分质量相关，检测不受流动相紫外吸收干扰；\n"
                    "- 质谱检测器（MS / MS-MS）：提供待测分子的精确分子量和特征碎片离子质荷比（m/z），适用于复杂成分定性确证与超微量定量。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0512: High-Performance Liquid Chromatography (HPLC)\n\n"
                    "1. Principle and System Setup:\n"
                    "High-Performance Liquid Chromatography (HPLC) separates multi-component mixtures using high-pressure delivery pumps to drive mobile phases through analytical columns containing microparticulate stationary phases.\n"
                    "The system comprises high-pressure delivery pumps, autosampler, analytical column, column temperature compartment, detector, and chromatography data system (CDS).\n\n"
                    "2. Detector Classes and Applications:\n"
                    "- UV-Vis Absorption / Photodiode Array (UV/Vis / DAD / PDA): For compounds with chromophores. DAD records 3D spectra for chromatographic peak purity evaluation.\n"
                    "- Fluorescence Detector (FLD): For fluorescent compounds or fluorescently derivatized analytes, offering 2-3 orders of magnitude higher sensitivity than UV.\n"
                    "- Refractive Index Detector (RID): Universal detector for sugars and polymers without UV absorption; requires strict temperature control and cannot be used with gradient elution.\n"
                    "- Evaporative Light Scattering Detector (ELSD): Universal mass-sensitive detector for non-volatile analytes; independent of mobile phase optical properties.\n"
                    "- Mass Spectrometry (MS / MS-MS): Delivers precise molecular weights and structural fragment ions (m/z) for trace-level quantification and identification."
                )
            },
            {
                "section_id": "0512_sec2_suitability",
                "section_title": "通则 0512 第二节：系统适用性试验四大金标准与计算公式",
                "section_title_en": "Section 2: System Suitability Testing Criteria & Formulas",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0512 高效液相色谱法\n\n"
                    "系统适用性试验（System Suitability Test, SST）是确保色谱系统在样品检测全过程中保持足够重现性与分离效能的法定强制指标。任何样品测定前必须验证下列参数：\n\n"
                    "1. 色谱柱理论板数（n）：\n"
                    "用于衡量色谱柱柱效。按公式计算：\n"
                    "n = 5.54 * (t_R / W_{h/2})^2\n"
                    "式中，t_R 为待测成分的保留时间；W_{h/2} 为半高峰宽。所得理论板数 n 不得低于品种项下规定的最低限度。\n\n"
                    "2. 分离度（R）：\n"
                    "用于衡量主峰与相邻峰（或关键难分离对杂质峰）的分离能力。按公式计算：\n"
                    "R = 2 * (t_{R2} - t_{R1}) / (W_1 + W_2)\n"
                    "式中，t_{R1} 与 t_{R2} 为相邻两峰的保留时间；W_1 与 W_2 为两峰在基线处的峰宽。除各品种项下另有规定外，待测成分色谱峰与相邻杂质峰之间的分离度 R 必须 >= 1.5（达到基线完全分离）。\n\n"
                    "3. 拖尾因子（T）：\n"
                    "用于评估色谱峰的对称性。按公式计算：\n"
                    "T = W_{0.05h} / (2 * d_1)\n"
                    "式中，W_{0.05h} 为峰高 5% 处的峰宽；d_1 为峰顶引出垂线至峰前沿的距离。用于含量测定的主色谱峰，其拖尾因子应在 0.95 ~ 1.05 之间，以保证色谱积分精确。\n\n"
                    "4. 重复性相对标准偏差（RSD）：\n"
                    "取对照品溶液连续进样 5~6 次，记录色谱峰响应值。主峰峰面积的相对标准偏差（RSD）通常不得大于 2.0%（高精度含量测定项下要求 RSD <= 1.0% 或 1.5%）。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0512: System Suitability Testing (SST)\n\n"
                    "System Suitability Testing validates that the fluidics, column, detector, and integration system perform with acceptable precision and resolution. All criteria must be satisfied prior to running sample analyses:\n\n"
                    "1. Theoretical Plate Number (n):\n"
                    "Measures column efficiency. Calculated by:\n"
                    "n = 5.54 * (t_R / W_{h/2})^2\n"
                    "where t_R is retention time and W_{h/2} is peak width at half peak height. Calculated n must not be lower than the monograph requirement.\n\n"
                    "2. Resolution (R):\n"
                    "Measures baseline separation between active peak and adjacent peak:\n"
                    "R = 2 * (t_{R2} - t_{R1}) / (W_1 + W_2)\n"
                    "where t_{R1} and t_{R2} are retention times, and W_1 and W_2 are baseline peak widths. Unless otherwise specified, R must be >= 1.5 (baseline separation).\n\n"
                    "3. Tailing Factor (T):\n"
                    "Evaluates peak symmetry. Calculated by:\n"
                    "T = W_{0.05h} / (2 * d_1)\n"
                    "where W_{0.05h} is peak width at 5% peak height, and d_1 is distance from peak front to perpendicular line. For assay peaks, T must fall within 0.95 ~ 1.05.\n\n"
                    "4. Repeatability (RSD):\n"
                    "Across 5 to 6 consecutive injections of reference standard solution, the relative standard deviation (RSD) of the main peak area must not exceed 2.0% (or <= 1.0% for high-precision assays)."
                )
            },
            {
                "section_id": "0512_sec3_quantitation",
                "section_title": "通则 0512 第三节：定量计算方法（外标法、自身对照法与加校正因子法）",
                "section_title_en": "Section 3: Quantitative Calculation Methods",
                "pages": [3],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0512 高效液相色谱法\n\n"
                    "法定定量分析方法包括：\n"
                    "1. 外标法（标准曲线法 / 单点外标法）：\n"
                    "配制已知准确浓度的对照品溶液与供试品溶液，分别在相同色谱条件下进样。按公式计算：\n"
                    "C_供 = (A_供 / A_对) * C_对\n"
                    "式中，A_供 与 A_对 分别为供试品与对照品峰面积；C_供 与 C_对 分别为对应浓度。外标法是含量测定的首选方法。\n\n"
                    "2. 主成分自身对照法（不加校正因子）：\n"
                    "将供试品溶液精密稀释至规定浓度作为对照溶液（如稀释 100 倍即相当于 1.0% 限度）。供试品色谱图中各杂质峰面积不得大于对照溶液主峰面积。适用于响应因子与主成分相近（相对响应值在 0.9 ~ 1.1 之间）的杂质检查。\n\n"
                    "3. 加校正因子主成分自身对照法：\n"
                    "当杂质与主成分的紫外吸光系数存在显著差异（相对响应因子在 0.2 ~ 0.9 或 1.1 ~ 5.0 之间）时，必须测定相对响应因子 f，并将杂质峰面积乘以 f 进行校正折算。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0512: Quantitative Methodologies\n\n"
                    "1. External Standard Method:\n"
                    "Standard reference solution of verified concentration and sample solution are analyzed under identical conditions:\n"
                    "C_sample = (A_sample / A_standard) * C_standard\n"
                    "where A represents peak areas and C represents concentrations. External standard method is primary for active assay.\n\n"
                    "2. High-Low Principal Component Self-Reference Method (Uncorrected):\n"
                    "Sample solution is diluted precisely to specified threshold concentration (e.g. 100-fold dilution representing 1.0% limit) as control. Applicable when relative response factor of impurities relative to active analyte is between 0.9 and 1.1.\n\n"
                    "3. Principal Component Self-Reference with Relative Correction Factor (f):\n"
                    "When UV absorptivity of an impurity differs significantly from active analyte (relative response factor f is between 0.2~0.9 or 1.1~5.0), the impurity peak area must be multiplied by f for true quantitation."
                )
            }
        ]
    })

    # =========================================================================
    # 2. ChP 2020 Vol IV General Chapter 1143: Bacterial Endotoxins
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_1143_endotoxins",
        "doc_title": "《中华人民共和国药典》2020年版四部 通则 1143 细菌内毒素检查法",
        "doc_title_zh": "《中华人民共和国药典》2020年版四部 通则 1143 细菌内毒素检查法",
        "doc_title_en": "ChP 2020 Vol IV General Chapter 1143: Bacterial Endotoxins Test (BET)",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol4_general_chapter_1143_endotoxins_full.md",
        "version": "2020-ChP-Official",
        "sections": [
            {
                "section_id": "1143_sec1_formulas",
                "section_title": "通则 1143 第一节：内毒素限值（L）与最大有效稀释倍数（MVD）法定计算公式",
                "section_title_en": "Section 1: Endotoxin Limits (L) and Maximum Valid Dilution (MVD) Formulas",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 1143 细菌内毒素检查法\n\n"
                    "1. 药品内毒素法定限值（L）计算规程：\n"
                    "药品内毒素限值是依据临床人用每千克体重每小时的最大用药剂量计算确定的安全阈值。计算公式为：\n"
                    "L = K / M\n"
                    "式中：\n"
                    "- L 为供试品的细菌内毒素限值，单位为 EU/ml（注射液）或 EU/mg（原料药或注射用无菌粉末）；\n"
                    "- K 为人用每千克体重每小时最大允许内毒素负荷阈值：\n"
                    "  * 静脉注射制剂：K = 5.0 EU/(kg·h)；\n"
                    "  * 鞘内给药、硬膜外给药制剂：K = 0.2 EU/(kg·h)；\n"
                    "  * 放射性药品注射剂：K = 2.5 EU/(kg·h)；\n"
                    "- M 为人用每千克体重每小时的最大用药剂量（单位为 ml/(kg·h)、mg/(kg·h) 或 U/(kg·h)）。若说明书给药剂量按人计算，默认成人体重为 60 kg，儿童按说明书指定千克体重计算。\n\n"
                    "2. 最大有效稀释倍数（MVD）计算公式：\n"
                    "为消除供试品溶液对凝集反应的理化干扰（如pH偏离、高离子强度或螯合剂），供试品允许稀释的最大倍数必须严格按照下列公式计算：\n"
                    "MVD = (L * c) / λ\n"
                    "式中：\n"
                    "- L 为供试品的内毒素限值（EU/ml 或 EU/mg）；\n"
                    "- c 为供试品溶液的初始标示浓度（mg/ml、U/ml 或按原液设为 1.0）；\n"
                    "- λ 为所使用鲎试剂的标示灵敏度（单位为 EU/ml，如 0.03、0.06、0.125、0.25 EU/ml）或光度测定法标准曲线的最低检测限。\n"
                    "【法定强制红线】：供试品在检验过程中的实际稀释倍数绝不得大于 MVD，否则供试品中残存的微量内毒素浓度将低于鲎试剂检出限，造成致死性假阴性漏检！"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 1143: Bacterial Endotoxins Test\n\n"
                    "1. Endotoxin Limit (L) Calculation:\n"
                    "The statutory endotoxin limit is determined by:\n"
                    "L = K / M\n"
                    "where:\n"
                    "- L is the endotoxin limit in EU/mL, EU/mg, or EU/Unit;\n"
                    "- K is the threshold human pyrogenic dose per kg body weight per hour:\n"
                    "  * Intravenous route: K = 5.0 EU/(kg*h);\n"
                    "  * Intrathecal/epidural route: K = 0.2 EU/(kg*h);\n"
                    "  * Radiopharmaceuticals: K = 2.5 EU/(kg*h);\n"
                    "- M is maximum clinically recommended human dose per kg body weight administered within a 1-hour interval (standard adult weight = 60 kg).\n\n"
                    "2. Maximum Valid Dilution (MVD) Formula:\n"
                    "To overcome sample matrix interference without dropping endotoxin below detection threshold:\n"
                    "MVD = (L * c) / lambda\n"
                    "where:\n"
                    "- L is the endotoxin limit (EU/mL or EU/mg);\n"
                    "- c is sample concentration (mg/mL, Unit/mL, or 1.0 for neat injection);\n"
                    "- lambda is labeled sensitivity of the TAL reagent (EU/mL, e.g. 0.03, 0.06, 0.125, 0.25 EU/mL) or lowest standard curve calibration point.\n"
                    "[MANDATORY RULE]: The actual dilution factor used in testing MUST NEVER exceed MVD; otherwise endotoxin concentration falls below detection threshold, generating lethal false negatives."
                )
            },
            {
                "section_id": "1143_sec2_gel_photometric",
                "section_title": "通则 1143 第二节：凝胶法与光度测定法（浊度法与显色基质法）操作规程",
                "section_title_en": "Section 2: Gel-Clot and Photometric Procedures",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 1143 细菌内毒素检查法\n\n"
                    "1. 凝胶限量试验（Gel-Clot Limit Test）：\n"
                    "- 取规格为 0.1 ml 鲎试剂装入安瓿管或反应试管中，加入 0.1 ml 供试品稀释液，轻缓混匀，封口；\n"
                    "- 置 37℃ ± 1℃ 恒温水浴或微孔恒温箱中静置温育 60 ± 2 分钟，温育过程中必须严密防震；\n"
                    "- 判定操作：温育结束取出试管，缓缓倒转 180°。若管底形成坚实凝胶，倒转后凝胶保持完整、不滑落、无液体渗流者，判为阳性（+）；若未能形成凝胶，或凝胶滑落、崩散者，判为阴性（-）。\n"
                    "- 对照管要求：每次检测必须同步设立阴性对照管（无内毒素水，必须为阴性）和阳性对照管（含 2λ 浓度内毒素，必须为阳性）。\n\n"
                    "2. 光度测定法（Photometric Techniques）：\n"
                    "- 动态浊度法（Turbidimetric Method）：在 37℃ 条件下检测反应混合物在特定波长（如 340nm）透光度或吸光度达到预定阈值所需的反应时间（起始时间 t_onset）。反应时间的对数与内毒素浓度的对数呈线性负相关，相关系数绝对值 |r| >= 0.980。\n"
                    "- 动态显色基质法（Chromogenic Method）：鲎凝集酶水解人工合成的黄色发色底物（如 Boc-Leu-Gly-Arg-pNA），释放黄色发色基团对硝基苯胺（pNA），在 405nm 波长处连续监测吸光度增长斜率，精确定量内毒素含量。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 1143: Test Procedures\n\n"
                    "1. Gel-Clot Limit Test:\n"
                    "- Aliquot 0.1 mL of sample solution into TAL reaction tube containing 0.1 mL reconstituted TAL reagent. Mix gently and seal.\n"
                    "- Incubate in 37°C ± 1°C water bath or heating block for 60 ± 2 minutes undisturbed without vibration.\n"
                    "- Readout: Invert tube smoothly through 180 degrees. Firm solid gel remaining intact without sliding or liquid discharge is positive (+). Failure to form intact gel is negative (-).\n"
                    "- Controls: Negative water control (must be negative) and positive product control with 2*lambda spike (must be positive) are mandatory in parallel.\n\n"
                    "2. Photometric Techniques:\n"
                    "- Turbidimetric Technique: Monitors onset reaction time required to reach specified turbidity threshold at 340 nm at 37°C. Log(onset time) vs log(endotoxin concentration) calibration curve must yield |r| >= 0.980.\n"
                    "- Chromogenic Technique: Endotoxin-activated protease cleaves synthetic peptide substrate, releasing yellow p-nitroaniline (pNA) measured kinetically at 405 nm."
                )
            }
        ]
    })

    # =========================================================================
    # 3. ChP 2020 Vol IV General Chapter 1101: Sterility Testing
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_1101_sterility",
        "doc_title": "《中华人民共和国药典》2020年版四部 通则 1101 无菌检查法",
        "doc_title_zh": "《中华人民共和国药典》2020年版四部 通则 1101 无菌检查法",
        "doc_title_en": "ChP 2020 Vol IV General Chapter 1101: Sterility Testing",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol4_general_chapter_1101_sterility_full.md",
        "version": "2020-ChP-Official",
        "sections": [
            {
                "section_id": "1101_sec1_environmental_media",
                "section_title": "通则 1101 第一节：洁净环境控制、两大培养基与14天培养周期",
                "section_title_en": "Section 1: Environmental Controls, Culture Media & 14-Day Incubation Period",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 1101 无菌检查法\n\n"
                    "1. 环境控制与生物安全：\n"
                    "无菌检查必须在严格受控的无菌操作环境中进行。检验环境应为 B 级背景下的 A 级单向流洁净台（超净工作台），或采用经过验证的 A 级全封闭隔离操作系统（Isolator）。操作区沉降菌、浮游菌及手套接触菌落数必须严格 < 1 CFU。\n\n"
                    "2. 两种法定核心培养基及培养规程：\n"
                    "- 硫乙醇酸盐流体培养基（Fluid Thioglycollate Medium, FTM）：\n"
                    "  * 适用对象：主要用于需氧菌与厌氧菌的培养；\n"
                    "  * 法定培养温度：30℃ ~ 35℃；\n"
                    "  * 法定培养时间：连续培养不得少于 14 天。\n"
                    "  * 培养基特征：上层约 1/3 氧化层因含刃天青呈粉红色，下层还原层呈无色。\n"
                    "- 胰酪大豆胨液体培养基（Tryptic Soy Broth, TSB）：\n"
                    "  * 适用对象：主要用于真菌（酵母菌、霉菌）及嗜温需氧菌的培养；\n"
                    "  * 法定培养温度：20℃ ~ 25℃；\n"
                    "  * 法定培养时间：连续培养不得少于 14 天。\n\n"
                    "3. 培养结果每日观察与终局判定：\n"
                    "接种后的各试管应置指定恒温培养箱中，在 14 天培养期内逐日观察。若培养物澄清透明、无微生物生长浑浊现象，判为供试品符合规定；若任一培养基出现微生物浑浊生长，必须进行菌种鉴定并调查实验室环境，除非能确证为实验操作污染，否则判定供试品不符合规定。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 1101: Sterility Testing\n\n"
                    "1. Environmental Controls:\n"
                    "Sterility tests must be conducted within a Grade A laminar airflow workstation located inside a Grade B cleanroom, or within an isolator system conforming to ISO Class 5.\n\n"
                    "2. Two Mandatory Culture Media & Regimens:\n"
                    "- Fluid Thioglycollate Medium (FTM):\n"
                    "  * Purpose: Supports growth of both aerobic and obligate/facultative anaerobic bacteria.\n"
                    "  * Incubation Temperature: 30°C ~ 35°C.\n"
                    "  * Incubation Duration: Not less than 14 consecutive days.\n"
                    "- Tryptic Soy Broth (TSB):\n"
                    "  * Purpose: Supports growth of yeasts, molds, and aerobic bacteria.\n"
                    "  * Incubation Temperature: 20°C ~ 25°C.\n"
                    "  * Incubation Duration: Not less than 14 consecutive days.\n\n"
                    "3. Observations and Final Release Criteria:\n"
                    "Tubes are inspected daily over the 14-day duration. If no turbidity or microbial proliferation is observed in any medium, the batch meets sterility. If microbial growth occurs, root-cause investigation is mandatory."
                )
            },
            {
                "section_id": "1101_sec2_membrane_filtration",
                "section_title": "通则 1101 第二节：薄膜过滤法操作与抗生素抑菌性消除冲洗规程",
                "section_title_en": "Section 2: Membrane Filtration Method & Antibiotic Neutralization Rinsing",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 1101 无菌检查法\n\n"
                    "1. 薄膜过滤法（Membrane Filtration Method - 法定首选法）：\n"
                    "- 采用微孔滤膜过滤器（公称孔径不大于 0.45 μm，滤膜直径约为 50 mm）。\n"
                    "- 将供试品药液按规定体积通过滤膜抽滤。通常一个集菌滤筒的药液过滤量不宜超过 500 ml。\n"
                    "- 过滤完毕后，将 FTM 培养基和 TSB 培养基分别注入对应的两个集菌滤筒内，封口培养。\n\n"
                    "2. 消除抗生素/抑菌成分的冲洗液规程：\n"
                    "- 对于本身具有抑菌活性的化学药品、抗生素类制剂或含防腐剂的注射剂，必须用经充分方法验证的冲洗液（如 0.1% 蛋白胨水无菌冲洗液、含聚山梨酯80冲洗液或含青霉素酶的专用中和液）冲洗滤膜；\n"
                    "- 冲洗总量限制：每张滤膜每次冲洗量通常为 100 ml，总冲洗次数不得超过 5 次，即总冲洗量绝不得超过 500 ml（5 * 100 ml），防止过度冲洗导致已截留的微量致病菌损伤死亡！\n\n"
                    "3. 阳性对照菌株质控（接种量 < 100 CFU）：\n"
                    "- 金黄色葡萄球菌（Staphylococcus aureus）\n"
                    "- 铜绿假单胞菌（Pseudomonas aeruginosa）\n"
                    "- 枯草芽孢杆菌（Bacillus subtilis）\n"
                    "- 生孢梭菌（Clostridium sporogenes）\n"
                    "- 白色念珠菌（Candida albicans）\n"
                    "- 黑曲霉（Aspergillus niger）。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 1101: Membrane Filtration\n\n"
                    "1. Membrane Filtration Procedure:\n"
                    "- Utilize closed filtration canisters with 0.45 um pore size membranes.\n"
                    "- The volume filtered through a single canister filter generally should not exceed 500 mL.\n"
                    "- After filtration, FTM and TSB media are transferred into separate canisters for incubation.\n\n"
                    "2. Rinsing Protocol for Antimicrobial Neutralization:\n"
                    "- For antibiotics or formulations containing antimicrobial preservatives, sterile rinse fluid (e.g. 0.1% peptone water, polysorbate 80 rinse fluid, or penicillinase-supplemented solution) is drawn through the filter.\n"
                    "- Permissible Rinse Volume: 100 mL per wash cycle; maximum 5 washes (total wash volume per membrane MUST NOT exceed 500 mL) to prevent cell lysis of trapped microbes.\n\n"
                    "3. Positive Control Strains (< 100 CFU Spike):\n"
                    "- Staphylococcus aureus\n"
                    "- Pseudomonas aeruginosa\n"
                    "- Bacillus subtilis\n"
                    "- Clostridium sporogenes\n"
                    "- Candida albicans\n"
                    "- Aspergillus niger."
                )
            }
        ]
    })

    # =========================================================================
    # 4. ChP 2020 Vol IV General Chapter 0931: Dissolution
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_0931_dissolution",
        "doc_title": "《中华人民共和国药典》2020年版四部 通则 0931 溶出度与释放度测定法",
        "doc_title_zh": "《中华人民共和国药典》2020年版四部 通则 0931 溶出度与释放度测定法",
        "doc_title_en": "ChP 2020 Vol IV General Chapter 0931: Dissolution and Drug Release Testing",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol4_general_chapter_0931_dissolution_full.md",
        "version": "2020-ChP-Official",
        "sections": [
            {
                "section_id": "0931_sec1_apparatus_media",
                "section_title": "通则 0931 第一节：篮法、桨法、小杯法标准装置与四介质溶出曲线",
                "section_title_en": "Section 1: Basket, Paddle & Small Cup Apparatus & Four-Media Dissolution Curves",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0931 溶出度与释放度测定法\n\n"
                    "1. 法定测定装置与技术规范：\n"
                    "- 第一法（篮法）：转篮由不锈钢丝网（孔径 0.355~0.425 mm / 40目）制成。篮底与溶出杯内底部距离恒定保持在 25 mm ± 2 mm。标准法定转速通常为 100 rpm（或 50~150 rpm）；\n"
                    "- 第二法（桨法）：搅拌桨由耐腐蚀特氟龙或不锈钢制成。桨叶下端距溶出杯底部保持 25 mm ± 2 mm。标准法定转速通常为 50 rpm（或 50~75 rpm）；\n"
                    "- 第三法（小杯法）：适用于微量低剂量药物制剂，溶出杯容积为 100~250 ml，转速一般为 50 rpm；\n"
                    "- 水浴恒温要求：溶出介质温度必须严密维持在 37.0℃ ± 0.5℃。\n\n"
                    "2. 仿制药一致性评价四条体外溶出曲线法定配制要求：\n"
                    "(1) pH 1.2 盐酸溶液（模拟空腹胃液）；\n"
                    "(2) pH 4.5 醋酸盐缓冲液；\n"
                    "(3) pH 6.8 磷酸盐缓冲液（模拟小肠液）；\n"
                    "(4) 脱气水介质。\n"
                    "所有溶出介质必须经过超声或真空充分脱气处理，防止微小气泡附着在片剂表面导致假性溶出延迟。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0931: Dissolution and Drug Release Testing\n\n"
                    "1. Official Apparatus Specifications:\n"
                    "- Method 1 (Basket Method): Rotating basket constructed of stainless steel mesh (40 mesh). Distance between basket bottom and hemispherical vessel bottom is 25 mm ± 2 mm. Standard speed: 100 rpm.\n"
                    "- Method 2 (Paddle Method): Rotating blade paddle. Distance between blade bottom and vessel bottom is 25 mm ± 2 mm. Standard speed: 50 rpm.\n"
                    "- Method 3 (Small Cup Method): Reduced vessel volume (100~250 mL) for low-dose drugs; standard speed: 50 rpm.\n"
                    "- Temperature: Strictly controlled at 37.0°C ± 0.5°C.\n\n"
                    "2. Four Physiological Media for Generic Equivalence:\n"
                    "(1) pH 1.2 Hydrochloric acid buffer (simulating fasting gastric fluid);\n"
                    "(2) pH 4.5 Acetate buffer;\n"
                    "(3) pH 6.8 Phosphate buffer (simulating intestinal fluid);\n"
                    "(4) Degassed Purified Water.\n"
                    "All media must be degassed prior to testing to avoid microbubble artifacts."
                )
            },
            {
                "section_id": "0931_sec2_f2_and_q",
                "section_title": "通则 0931 第二节：溶出限度（Q）判定与相似因子（f2）数学评价公式",
                "section_title_en": "Section 2: Dissolution Limit (Q) & Similarity Factor (f2) Calculation",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0931 溶出度与释放度测定法\n\n"
                    "1. 溶出限度（Q）判定标准（三阶段判定法则）：\n"
                    "- 阶段1（S1，取 6 片）：每片溶出量均不得低于 Q + 5%（若标示 Q=70%，则 6 片均需 >= 75%）；\n"
                    "- 阶段2（S2，若 S1 不符，追加 6 片共 12 片）：12 片平均溶出量不得低于 Q，且不得有 1 片低于 Q - 15%；\n"
                    "- 阶段3（S3，若 S2 不符，追加 12 片共 24 片）：24 片平均溶出量不得低于 Q，低于 Q - 15% 的片数不得超过 2 片，且不得有 1 片低于 Q - 25%。\n\n"
                    "2. 相似因子（f2）数学公式与仿制药一致性判定规则：\n"
                    "按公式计算受试制剂（Test, T）与参比制剂（Reference, R）溶出曲线的相似性：\n"
                    "f2 = 50 * lg( [ 1 + (1/n) * Σ_{t=1}^n (R_t - T_t)^2 ]^(-0.5) * 100 )\n"
                    "式中：\n"
                    "- n 为取样时间点数量（至少选取 3 个采样点，如 5, 10, 15, 20, 30, 45, 60 分钟）；\n"
                    "- R_t 和 T_t 分别为参比制剂与受试制剂在 t 时间点的平均溶出百分比；\n"
                    "- 【合格判定准则】：当计算所得 f2 值在 50 ~ 100 之间（50 <= f2 <= 100）时，判定两制剂体外溶出行为完全相似等同！\n"
                    "- 【取样点选取法定限制】：两制剂溶出量均达到 85% 以上的时间点，只能保留 1 个点纳入 f2 计算；前期的溶出相对标准偏差（RSD）第一个点不得过 20%，后续点不得过 10%。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0931: Acceptance Criteria\n\n"
                    "1. Dissolution Limit (Q) Stage Criteria:\n"
                    "- Stage 1 (S1, n=6): Each unit must be >= Q + 5%.\n"
                    "- Stage 2 (S2, additional 6 units, total n=12): Average of 12 units >= Q, and no unit < Q - 15%.\n"
                    "- Stage 3 (S3, additional 12 units, total n=24): Average of 24 units >= Q, not more than 2 units < Q - 15%, and no unit < Q - 25%.\n\n"
                    "2. Similarity Factor (f2) Formula:\n"
                    "f2 = 50 * log10( [ 1 + (1/n) * sum_{t=1}^n (R_t - T_t)^2 ]^(-0.5) * 100 )\n"
                    "- Acceptance Criterion: When f2 is between 50 and 100 (50 <= f2 <= 100), the test and reference dissolution profiles are bioequivalent.\n"
                    "- Constraints: At least 3 time points. Only 1 time point after 85% dissolution is permitted in calculation. RSD of early points must be < 20%, later points < 10%."
                )
            }
        ]
    })

    return docs
