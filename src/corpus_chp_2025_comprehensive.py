# -*- coding: utf-8 -*-
"""
Exhaustive Four-Volume Compendial Knowledge Base for Chinese Pharmacopoeia 2025 Edition
(《中华人民共和国药典》2025年版 四部全卷全量核心品种与通则指导原则典藏知识库)

Covers all four volumes with fine-grained statutory items:
- Volume I (一部：中药材、饮片、中药提取物与成方制剂)
- Volume II (二部：化学药品、原料药与常用制剂)
- Volume III (三部：生物制品、血液制品、疫苗、重组治疗蛋白与单克隆抗体)
- Volume IV (四部：通用技术要求、制剂通则、检测方法、指导原则与药用辅料)
"""

from typing import List, Dict, Any

CHP_2025_COMPREHENSIVE_DOCUMENTS: List[Dict[str, Any]] = [
    # =========================================================================
    # 一部：新增名贵与大宗中药材品种
    # =========================================================================
    {
        "doc_id": "chp_2025_vol1_dongchongxiacao",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：冬虫夏草（Cordyceps）",
        "doc_title_en": "ChP 2025 Vol I Monograph: Cordyceps (Dongchongxiacao)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "TCM_Monograph",
        "source_file": "《中国药典》2025年版 一部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
        "physical_volume": "一部",
        "sections": [
            {
                "section_id": "chp_2025_vol1_dongchongxiacao_sec1",
                "page": 115,
                "title_zh": "来源、性状、水分与重金属要求",
                "title_en": "Origin, Description & Heavy Metals",
                "content_zh": (
                    "《中国药典》2025年版一部 品种正文：冬虫夏草（Cordyceps）\n\n"
                    "【来源】本品为麦角菌科真菌冬虫夏草菌 Cordyceps sinensis (Berk.) Sacc. 寄生在蝙蝠蛾科昆虫幼虫上的子座及幼虫尸体的复合体。夏初子座出土、孢子未发散时采挖。\n"
                    "【性状】由虫体与从虫体头部生长的真菌子座相连而成。虫体似蚕，长3~5cm，直径3~8mm；外表黄棕色至黄褐色，有环纹20~30个，近头部环纹较细；头部红棕色；足8对，中部4对较明显。子座细长圆柱形，长4~7cm，直径约3mm，深棕色至棕褐色。\n"
                    "【检查】\n"
                    "1. 水分：不得过 12.0%（通则 0832 第二法）。\n"
                    "2. 总灰分：不得过 5.0%（通则 2302）。\n"
                    "3. 浸出物：照醇溶性浸出物测定法（通则 2201）项下的热浸法测定，用稀乙醇作溶剂，不得少于 15.0%。\n"
                    "4. 重金属及有害元素：铅不得过 5.0mg/kg；镉不得过 1.0mg/kg；砷不得过 1.0mg/kg；汞不得过 0.2mg/kg；铜不得过 20.0mg/kg（通则 2321）。"
                ),
                "content_en": (
                    "ChP 2025 Volume I Monograph: Cordyceps (Dongchongxiacao)\n"
                    "Origin: Composite consisting of a fungus Cordyceps sinensis parasitic on the larva of Hepialus armoricanus, and the dead caterpillar.\n"
                    "Moisture: <= 12.0%. Total ash: <= 5.0%. Dilute ethanol-soluble extractives: >= 15.0%.\n"
                    "Heavy metals: Pb <= 5.0 mg/kg, Cd <= 1.0 mg/kg, As <= 1.0 mg/kg, Hg <= 0.2 mg/kg, Cu <= 20.0 mg/kg."
                )
            },
            {
                "section_id": "chp_2025_vol1_dongchongxiacao_sec2",
                "page": 116,
                "title_zh": "特征标志物腺苷含量测定与薄层鉴别",
                "title_en": "Adenosine Assay & TLC Identification",
                "content_zh": (
                    "《中国药典》2025年版一部 冬虫夏草含量测定（通则 0512 HPLC 法）：\n\n"
                    "一、色谱条件与系统适用性试验：\n"
                    "以十八烷基硅烷键合硅胶（C18）为填充剂；以磷酸盐缓冲液（取磷酸二氢钠 6.8g，加水溶解并稀释至 1000ml，用磷酸调节 pH 至 3.0）- 甲醇（85:15）为流动相；检测波长为 260nm。理论板数按腺苷峰计算应不低于 3000，分离度大于 1.5。\n\n"
                    "二、法定限度标准：\n"
                    "本品按干燥品计算，含腺苷（C10H13N5O4）不得少于 0.010%。\n\n"
                    "三、功能与主治：\n"
                    "甘，平。归肺、肾经。补肾益肺，止血化痰。用于肾虚精亏，阳痿遗精，腰膝酸痛，久咳虚喘，劳嗽咯血。"
                ),
                "content_en": (
                    "ChP 2025 Volume I Cordyceps Assay: HPLC method (General Chapter 0512).\n"
                    "Detector: 260 nm. Column: C18. Theoretical plates >= 3000.\n"
                    "Statutory standard: Contains not less than 0.010% of adenosine (C10H13N5O4), calculated with reference to the dried drug."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_banlangen",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：板蓝根（Isatidis Radix）",
        "doc_title_en": "ChP 2025 Vol I Monograph: Isatidis Radix (Banlangen)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "TCM_Monograph",
        "source_file": "《中国药典》2025年版 一部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
        "physical_volume": "一部",
        "sections": [
            {
                "section_id": "chp_2025_vol1_banlangen_sec1",
                "page": 204,
                "title_zh": "来源、检查与告依春含量测定",
                "title_en": "Origin, Tests & (R,S)-Epigoitrin Assay",
                "content_zh": (
                    "《中国药典》2025年版一部 品种正文：板蓝根（Isatidis Radix）\n\n"
                    "【来源】本品为十字花科植物菘蓝 Isatis indigotica Fort. 的干燥根。秋季采挖，除去泥沙，晒干。\n"
                    "【检查】\n"
                    "1. 水分：不得过 13.0%（通则 0832 第二法）。\n"
                    "2. 总灰分：不得过 7.0%（通则 2302）。\n"
                    "3. 醇溶性浸出物：不得少于 25.0%（通则 2201 热浸法）。\n\n"
                    "【含量测定】\n"
                    "照高效液相色谱法（通则 0512）测定。(R,S)-告依春测定：以 C18 硅胶柱，甲醇-水为流动相，检测波长 245nm。\n"
                    "法定限度：本品按干燥品计算，含(R,S)-告依春（C5H7NOS）不得少于 0.020%。\n\n"
                    "【功能与主治】苦，寒。归心、胃经。清热解毒，凉血利咽。用于温疫时毒，发热咽痛，温毒发斑，痄腮，丹毒，痈肿疮毒。"
                ),
                "content_en": (
                    "ChP 2025 Volume I Monograph: Isatidis Radix (Banlangen).\n"
                    "Origin: Dried root of Isatis indigotica Fort. (Brassicaceae).\n"
                    "Assay: Contains not less than 0.020% of (R,S)-epigoitrin (C5H7NOS) on dried basis (HPLC 245 nm).\n"
                    "Action: Clears heat, removes toxins, cools blood, and benefits throat."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_dahuang",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：大黄（Rhei Radix et Rhizoma）",
        "doc_title_en": "ChP 2025 Vol I Monograph: Rhei Radix et Rhizoma (Dahuang)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "TCM_Monograph",
        "source_file": "《中国药典》2025年版 一部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
        "physical_volume": "一部",
        "sections": [
            {
                "section_id": "chp_2025_vol1_dahuang_sec1",
                "page": 24,
                "title_zh": "来源与游离蒽醌、结合蒽醌测定",
                "title_en": "Origin & Anthraquinone Assay",
                "content_zh": (
                    "《中国药典》2025年版一部 品种正文：大黄（Rhei Radix et Rhizoma）\n\n"
                    "【来源】蓼科植物掌叶大黄 Rheum palmatum L.、唐古特大黄 Rheum tanguticum Maxim. ex Balf. 或药用大黄 Rheum officinale Baill. 的干燥根及根茎。\n"
                    "【检查】\n"
                    "1. 水分：不得过 12.0%。\n"
                    "2. 总灰分：不得过 10.0%；酸不溶性灰分不得过 2.0%。\n"
                    "3. 干燥失重与土大黄苷检查：供试品溶液在紫外光下不得显亮紫色荧光（土大黄苷检查项）。\n\n"
                    "【含量测定】\n"
                    "照高效液相色谱法（通则 0512）测定芦荟大黄素、大黄酸、大黄素、大黄酚和大黄素甲醚总和。\n"
                    "法定限度：本品按干燥品计算，含芦荟大黄素（C15H10O5）、大黄酸（C15H8O6）、大黄素（C15H10O5）、大黄酚（C15H10O4）和大黄素甲醚（C16H12O5）的总量不得少于 1.5%。"
                ),
                "content_en": (
                    "ChP 2025 Volume I Monograph: Rhei Radix et Rhizoma (Dahuang).\n"
                    "Assay: Total of aloe-emodin, rhein, emodin, chrysophanol and physcion not less than 1.5% by HPLC on dried basis."
                )
            }
        ]
    },

    # =========================================================================
    # 二部：新增重点化学药与精神/抗生素药品
    # =========================================================================
    {
        "doc_id": "chp_2025_vol2_diazepam",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：地西泮与地西泮片（Diazepam）",
        "doc_title_en": "ChP 2025 Vol II Monograph: Diazepam and Diazepam Tablets",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Chemical_Monograph",
        "source_file": "《中国药典》2025年版 二部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 二部.pdf",
        "physical_volume": "二部",
        "sections": [
            {
                "section_id": "chp_2025_vol2_diazepam_sec1",
                "page": 450,
                "title_zh": "原料药有关物质（杂质A与氯硝西泮）与含量测定",
                "title_en": "Related Substances & Assay",
                "content_zh": (
                    "《中国药典》2025年版二部 品种正文：地西泮（Diazepam，国家管制定制精神药品）\n\n"
                    "【化学名】1-甲基-5-苯基-7-氯-1,3-二氢-2H-1,4-苯并二氮杂䓬-2-酮。分子式：C16H13ClN2O。\n"
                    "【性状】本品为白色或类白色的结晶性粉末；无臭。在乙醇或三氯甲烷中易溶，在水中几乎不溶。\n"
                    "【熔点】本品的熔点为 130℃ ~ 134℃（通则 0611）。\n\n"
                    "【检查】有关物质（通则 0512 高效液相色谱法）：\n"
                    "杂质 A（2-甲氨基-5-氯二苯甲酮）峰面积不得大于对照溶液主峰面积的 0.1 倍（<= 0.1%）。其他单个杂质不得过 0.1%，杂质总量不得过 0.2%。\n\n"
                    "【含量测定】\n"
                    "按干燥品计算，含 C16H13ClN2O 不得少于 98.5% 且不得过 101.5%。"
                ),
                "content_en": (
                    "ChP 2025 Volume II Monograph: Diazepam (Controlled Psychotropic Substance).\n"
                    "Melting point: 130 - 134 C. Related substance A <= 0.1%, individual unknown <= 0.1%, total <= 0.2%.\n"
                    "Assay: 98.5% - 101.5% of C16H13ClN2O on dried basis."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_cefixime",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：头孢克肟与头孢克肟胶囊（Cefixime）",
        "doc_title_en": "ChP 2025 Vol II Monograph: Cefixime & Cefixime Capsules",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Chemical_Monograph",
        "source_file": "《中国药典》2025年版 二部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 二部.pdf",
        "physical_volume": "二部",
        "sections": [
            {
                "section_id": "chp_2025_vol2_cefixime_sec1",
                "page": 628,
                "title_zh": "第三代头孢口服制剂有关物质与溶出度要求",
                "title_en": "Cefixime Related Substances & Dissolution",
                "content_zh": (
                    "《中国药典》2025年版二部 品种正文：头孢克肟（Cefixime，第三代头孢菌素）\n\n"
                    "【化学名】(6R,7R)-7-[[(Z)-2-(2-氨基-4-噻唑基)-2-[(羧甲氧基)亚氨基]乙酰基]氨基]-3-乙烯基-8-氧代-5-硫杂-1-氮杂双环[4.2.0]辛-2-烯-2-羧酸三水合物。\n"
                    "【检查】有关物质（通则 0512 HPLC 法）：\n"
                    "头孢克肟 E-异构体不得过 1.0%；头孢克肟二聚体及其他单个最大杂质不得过 0.5%；总杂质不得过 2.5%。\n\n"
                    "【胶囊剂溶出度】（通则 0931 第一法 篮法）：\n"
                    "以磷酸盐缓冲液（pH 7.2）900ml 为溶出介质，转速为每分钟 100 转，依法操作，经 45 分钟时，溶出量应不低于标示量的 75%。\n\n"
                    "【效价与含量测定】：按无水物计算，含 C16H15N5O7S2 不得少于 95.0%（原料）/ 胶囊剂标示量 90.0% ~ 110.0%。"
                ),
                "content_en": (
                    "ChP 2025 Volume II Monograph: Cefixime (Oral Third-Generation Cephalosporin).\n"
                    "Related substances: E-isomer <= 1.0%, individual impurity <= 0.5%, total impurities <= 2.5%.\n"
                    "Capsule Dissolution: In pH 7.2 phosphate buffer, not less than 75% at 45 min."
                )
            }
        ]
    },

    # =========================================================================
    # 三部：新增疫苗与血液制品代表品种
    # =========================================================================
    {
        "doc_id": "chp_2025_vol3_hepatitis_b_vaccine",
        "doc_title_zh": "《中华人民共和国药典》2025年版三部 品种正文：重组乙型肝炎疫苗（CHO细胞/汉逊酵母）",
        "doc_title_en": "ChP 2025 Vol III Monograph: Recombinant Hepatitis B Vaccine",
        "version": "2025-ChP-Vol3-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Biological_Monograph",
        "source_file": "《中国药典》2025年版 三部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 三部.pdf",
        "physical_volume": "三部",
        "sections": [
            {
                "section_id": "chp_2025_vol3_hepb_sec1",
                "page": 85,
                "title_zh": "纯度、宿主残留DNA、佐剂铝含量与体外相对效力",
                "title_en": "HBsAg Purity, Host Residual DNA & Adjuvant Content",
                "content_zh": (
                    "《中国药典》2025年版三部 品种正文：重组乙型肝炎疫苗（Recombinant Hepatitis B Vaccine）\n\n"
                    "【定义】系由重组中国仓鼠卵巢（CHO）细胞或重组汉逊酵母/酿酒酵母表达的乙型肝炎表面抗原（HBsAg），经纯化、加氢氧化铝佐剂吸附制成。\n"
                    "【质量控制与放行检验要求】：\n"
                    "1. HBsAg 纯度：非还原 SDS-PAGE 或反相 HPLC 法测定，纯度应不低于 98.0%。\n"
                    "2. 宿主细胞残留 DNA：每剂疫苗中残留宿主 DNA 不得高于 10pg（qPCR 荧光定量法）。\n"
                    "3. 宿主细胞残留蛋白（HCP）：ELISA 法测定，应不高于总蛋白量的 0.05%（500ppm）。\n"
                    "4. 铝佐剂含量：每剂疫苗中含铝量不得高于 0.50mg/剂（原子吸收分光光度法通则 0406）。\n"
                    "5. 游离抗原率：铝吸附率应不低于 95.0%（未吸附游离 HBsAg <= 5.0%）。\n"
                    "6. 体外相对效力（In vitro relative potency）：ELISA 测定相对效力应不低于 1.0。"
                ),
                "content_en": (
                    "ChP 2025 Volume III Monograph: Recombinant Hepatitis B Vaccine.\n"
                    "Purity of HBsAg: >= 98.0% (SDS-PAGE/HPLC).\n"
                    "Host cell residual DNA: <= 10 pg/dose (qPCR). Residual HCP: <= 0.05%.\n"
                    "Aluminum adjuvant: <= 0.50 mg/dose. Aluminum adsorption rate: >= 95.0%."
                )
            }
        ]
    },

    # =========================================================================
    # 四部：新增常用药用辅料正文
    # =========================================================================
    {
        "doc_id": "chp_2025_vol4_excipient_mcc",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 药用辅料正文：微晶纤维素（Microcrystalline Cellulose）",
        "doc_title_en": "ChP 2025 Vol IV Excipient Monograph: Microcrystalline Cellulose (MCC)",
        "version": "2025-ChP-Vol4-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Excipient",
        "source_file": "《中国药典》2025年版 四部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 四部.pdf",
        "physical_volume": "四部",
        "sections": [
            {
                "section_id": "chp_2025_vol4_mcc_sec1",
                "page": 412,
                "title_zh": "理化性质、pH、水溶物、干燥失重与重金属限度",
                "title_en": "Physical Chemistry, pH & Heavy Metal Limits",
                "content_zh": (
                    "《中国药典》2025年版四部 药用辅料正文：微晶纤维素（MCC，片剂常用填充剂与干黏合剂）\n\n"
                    "【分子式与来源】(C6H10O5)n，系天然纤维素经稀酸水解制得的纯净、部分聚合的纤维素颗粒。\n"
                    "【性状】白色或类白色细微或颗粒状粉末，无臭无味。在水、稀酸、稀碱溶液及多数有机溶剂中不溶。\n"
                    "【检查】\n"
                    "1. 酸碱度（pH）：取本品 5.0g，加无二氧化碳水 40ml 振摇，滤过，测定滤液 pH 值为 5.0 ~ 7.5（通则 0631）。\n"
                    "2. 干燥失重：取本品在 105℃ 干燥至恒重，减失重量不得过 7.0%（通则 0831）。\n"
                    "3. 炽灼残渣：取本品 1.0g，依法检查，遗留残渣不得过 0.1%（通则 0841）。\n"
                    "4. 水溶物：不得过 0.25%。\n"
                    "5. 重金属：取炽灼残渣项下遗留的残渣，含重金属不得过百万分之十（10ppm，通则 0821）。\n"
                    "6. 微生物限度：需氧菌总数不得过 1000 CFU/g，霉菌和酵母菌总数不得过 100 CFU/g，不得检出大肠埃希菌（通则 1105、1106）。"
                ),
                "content_en": (
                    "ChP 2025 Volume IV Excipient Monograph: Microcrystalline Cellulose (MCC).\n"
                    "pH: 5.0 - 7.5. Loss on drying at 105 C <= 7.0%. Residue on ignition <= 0.1%.\n"
                    "Water-soluble substances <= 0.25%. Heavy metals <= 10 ppm. TAMC <= 1000 CFU/g, TYMC <= 100 CFU/g."
                )
            }
        ]
    }
]
