# -*- coding: utf-8 -*-
"""
Authentic Full-Text Corpus for Chinese Pharmacopoeia 2025 Edition - Volume I (《中国药典》2025年版一部：中药)
Statutory effective date: October 1, 2025 (Announcement No. 29 of 2025 by NMPA & NHC).
Covers Chinese Materia Medica, Prepared Slices, Plant Oils/Extracts, Proprietary Chinese Medicines,
and TCM General Inspection Chapters (General Chapters 0212, 2341, 2351, 2321).
"""

CHP_2025_VOL1_DOCUMENTS = [
    {
        "doc_id": "chp_2025_vol1_general_chapter_0212_tcm_inspection",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部与一部 通则 0212：药材和饮片检定通则",
        "doc_title_en": "ChP 2025 General Chapter 0212: General Requirements for Testing of Chinese Materia Medica and Prepared Slices",
        "version": "2025-ChP-Vol4-0212",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_General_Chapter",
        "source_file": "chp_2025_vol1_general_chapter_0212_tcm_inspection_full.pdf",
        "md_file": "chp_2025_vol1_general_chapter_0212_tcm_inspection_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol1_general_chapter_0212_tcm_inspection_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol1_0212_sec1_general_inspection",
                "page": 1,
                "title_zh": "第一节：药材和饮片来源、性状鉴别、水分与灰分控制通用标准",
                "title_en": "Section 1: Origin, Identification, Moisture, Ash & Impurity Testing Criteria",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部与四部 通则 0212 药材和饮片检定通则\n\n"
                    "一、总则与法定地位：\n"
                    "本通则适用于中药材和中药饮片的质量检定与标准制定。中药材和饮片必须符合正文品种项下的各项规定，包括基原植物/动物/矿物、产地加工、炮制方法、性状、鉴别、检查、浸出物与含量测定。\n\n"
                    "二、通用检验项目与控制原则：\n"
                    "1. 杂质检查（通则 2301）：药材中混存的非药用部位及外来杂质，除另有规定外，不得超过法定限度；\n"
                    "2. 水分测定（通则 0832）：烘干法（105℃）、甲苯法（含挥发性成分药材）或费休氏法，饮片水分通常控制在 9.0% ~ 13.0% 以下；\n"
                    "3. 总灰分与酸不溶性灰分（通则 2302）：总灰分测定高温炽灼温度为 500℃ ~ 600℃；酸不溶性灰分采用 10% 稀盐酸处理，严格控制泥沙等硅酸盐无机污染物；\n"
                    "4. 浸出物测定（通则 2201）：水溶性浸出物（冷浸/热浸）与醇溶性浸出物，作为有效成分未明或综合质量评价指标。"
                ),
                "content_en": (
                    "Chinese Pharmacopoeia 2025 General Chapter 0212: General Requirements for Testing of Chinese Materia Medica\n\n"
                    "1. General Scope: Applies to compendial quality assessment of medicinal herbs and prepared slices, specifying botanical origin, processing, macroscopic/microscopic identification, testing, extracts, and assay.\n\n"
                    "2. General Inspection Parameters:\n"
                    "- Foreign Matter (ChP 2301): Residual non-medicinal parts or foreign contaminants strictly controlled.\n"
                    "- Moisture (ChP 0832): Oven drying at 105 C, toluene distillation for volatile-containing herbs, or Karl Fischer titration.\n"
                    "- Total Ash & Acid-Insoluble Ash (ChP 2302): Ashing at 500-600 C; acid-insoluble ash treated with 10% hydrochloric acid to quantify siliceous soil residue.\n"
                    "- Extractives (ChP 2201): Water-soluble or ethanol-soluble extractive assays."
                )
            },
            {
                "section_id": "chp_vol1_0212_sec2_safety_limits_pesticides_metals",
                "page": 2,
                "title_zh": "第二节：外源性有害残留物（33种禁用农药、重金属与黄曲霉毒素）强制控制标准",
                "title_en": "Section 2: Mandatory Safety Standards for 33 Banned Pesticides, Heavy Metals & Aflatoxins",
                "content_zh": (
                    "《中国药典》2025年版中药安全保障关键指标：\n\n"
                    "一、33 种禁用农药残留测定法（通则 2341 第五法）：\n"
                    "中药材及饮片中全面执行 33 种高毒、禁用农药的基线强制限量筛查（采用气相色谱-串联质谱法 GC-MS/MS 与液相色谱-串联质谱法 LC-MS/MS 测定）：\n"
                    "- 涵盖甲拌磷、水胺硫磷、甲基对硫磷、对硫磷、久效磷、氧乐果、克百威、氟虫腈、三氯杀螨醇、滴滴涕（DDT）、六六六（BHC）等；\n"
                    "- 法定定量限要求：禁用农药残留检出值必须低于定量限（LOQ，通常为 0.01 ~ 0.1 mg/kg），一律判定为不得检出。\n\n"
                    "二、重金属及有害元素测定法（通则 2321，ICP-MS 法）：\n"
                    "铅（Pb）<= 5.0 mg/kg；镉（Cd）<= 1.0 mg/kg；砷（As）<= 2.0 mg/kg；汞（Hg）<= 0.2 mg/kg；铜（Cu）<= 20.0 mg/kg。\n\n"
                    "三、真菌毒素测定法（通则 2351）：\n"
                    "易霉变易污染真菌毒素的中药（如酸枣仁、陈皮、桃仁、地龙等）：黄曲霉毒素 B1 <= 5 ug/kg，黄曲霉毒素总量（B1+B2+G1+G2）<= 10 ug/kg。"
                ),
                "content_en": (
                    "ChP 2025 Mandatory Exogenous Harmful Contaminant Standards:\n\n"
                    "1. 33 Banned Pesticide Residues (ChP 2341 Method 5):\n"
                    "Multi-residue screening via GC-MS/MS and LC-MS/MS covering phorate, isocarbophos, parathion-methyl, parathion, monocrotophos, omethoate, carbofuran, fipronil, dicofol, DDT, and BHC. Statutory rule: Must not exceed compendial Limit of Quantification (LOQ: 0.01-0.1 mg/kg).\n\n"
                    "2. Heavy Metals and Toxic Elements (ChP 2321, ICP-MS):\n"
                    "Lead (Pb) <= 5.0 mg/kg; Cadmium (Cd) <= 1.0 mg/kg; Arsenic (As) <= 2.0 mg/kg; Mercury (Hg) <= 0.2 mg/kg; Copper (Cu) <= 20.0 mg/kg.\n\n"
                    "3. Mycotoxins (ChP 2351):\n"
                    "Aflatoxin B1 <= 5 ug/kg; Total Aflatoxins (B1 + B2 + G1 + G2) <= 10 ug/kg for susceptible medicinal items."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_chenpi_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：陈皮（广陈皮）",
        "doc_title_en": "ChP 2025 Vol I Official Monograph: Citri Reticulatae Pericarpium (Dried Tangerine Peel)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol1_chenpi_monograph_full.pdf",
        "md_file": "chp_2025_vol1_chenpi_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol1_chenpi_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol1_chenpi_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：陈皮与广陈皮基原、性状鉴别、农残限量与橙皮苷/川陈皮素含量测定",
                "title_en": "Section 1: Origin, Identification, 33 Pesticides, Hesperidin & Nobiletin Assay",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：陈皮（Citri Reticulatae Pericarpium）\n\n"
                    "一、来源与采收加工：\n"
                    "本品为芸香科植物橘 Citrus reticulata Blanco 及其栽培变种的干燥成熟果皮。药材分为“陈皮”和“广陈皮”。采摘成熟果实，剥取果皮，晒干或低温干燥。陈皮以陈久者良。\n\n"
                    "二、性状鉴别：\n"
                    "1. 陈皮：常剥成数瓣，基部相连，厚 1~4mm。外表面橙红色至红棕色，有细皱纹和凹下的点状油室；内表面浅黄白色，粗糙，附黄白色或黄棕色筋络状维管束。气香，味微苦、辛。\n"
                    "2. 广陈皮：常 3 瓣相连，形状整齐，厚度均匀，质较柔软，海绵状浮起，点状油室大而透光。\n\n"
                    "三、安全检查项目：\n"
                    "1. 水分：不得过 13.0%（通则 0832 第二法）；总灰分：不得过 5.0%（通则 2302）；\n"
                    "2. 农药残留限量：符合 33 种禁用农药残留规定（通则 2341），重金属铅镉砷汞符合通则 2321 限度。\n\n"
                    "四、含量测定（高效液相色谱法 通则 0512）：\n"
                    "1. 橙皮苷（Hesperidin）：按干燥品计算，陈皮含橙皮苷（C28H34O15）不得少于 3.5%；广陈皮含橙皮苷不得少于 2.0%；\n"
                    "2. 川陈皮素与橘皮素（广陈皮专属）：按干燥品计算，广陈皮含川陈皮素（C21H22O8）和橘皮素（C20H20O7）的总量不得少于 0.42%。\n\n"
                    "【性味与归经】苦、辛，温。归肺、脾经。【功能与主治】理气健脾，燥湿化痰。用于脘腹胀满，食少吐泻，咳嗽痰多。"
                ),
                "content_en": (
                    "ChP 2025 Volume I: Citri Reticulatae Pericarpium (Chenpi / Guangchenpi)\n\n"
                    "1. Botanical Origin: Dried mature pericarp of Citrus reticulata Blanco and its cultivars. Classified into Chenpi and Guangchenpi (produced in Guangdong Xinhui).\n\n"
                    "2. Mandatory Testing:\n"
                    "- Moisture <= 13.0%; Total Ash <= 5.0%.\n"
                    "- 33 Banned Pesticide Residues (ChP 2341 compliant).\n\n"
                    "3. Assay Specifications (HPLC ChP 0512):\n"
                    "- Hesperidin: Chenpi contains not less than 3.5%; Guangchenpi contains not less than 2.0%.\n"
                    "- Polymethoxyflavones (Guangchenpi): Total of Nobiletin and Tangeretin contains not less than 0.42%.\n\n"
                    "Action & Indications: Regulates qi, invigorates spleen, dries dampness, resolves phlegm."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_renshen_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：人参（Ginseng Radix et Rhizoma）",
        "doc_title_en": "ChP 2025 Vol I Official Monograph: Ginseng Radix et Rhizoma (Ginseng)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol1_renshen_monograph_full.pdf",
        "md_file": "chp_2025_vol1_renshen_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol1_renshen_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol1_renshen_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：人参来源、性状特征、人参皂苷 Rg1/Re/Rb1 含量测定与安全限度",
                "title_en": "Section 1: Origin, Characteristics, Ginsenosides Rg1, Re, Rb1 Assay & Safety Criteria",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：人参（Ginseng Radix et Rhizoma）\n\n"
                    "一、来源与分类：\n"
                    "本品为五加科植物人参 Panax ginseng C. A. Mey. 的干燥根和根茎。栽培者统称为“园参”；播种在山林野生状态下自然生长的称“林下山参”。秋季采挖，洗净，晒干或烘干者称“生晒参”。\n\n"
                    "二、性状鉴别特征：\n"
                    "主根呈纺锤形或圆柱形，长 3~15cm，直径 1~2cm。表面灰黄色，上部或全体有疏浅断续的粗横纹及明显的纵皱，下部有支根 2~3 条，并着生多数细长须根，须根上常有不明显的细小疣状突起。根茎（芦头）长 1~4cm，多拘挛而弯曲，具不定根（艼）和稀疏凹窝状茎痕（芦碗）。气微香而特异，味微苦、甘。\n\n"
                    "三、检查项目：\n"
                    "1. 水分：不得过 12.0%；总灰分：不得过 5.0%；有机氯及禁用农残符合通则 2341 规定；重金属铅镉砷汞符合通则 2321。\n\n"
                    "四、含量测定（高效液相色谱法 通则 0512）：\n"
                    "按干燥品计算，含人参皂苷 Rg1（C42H72O14）和人参皂苷 Re（C48H82O18）的总量不得少于 0.30%，含人参皂苷 Rb1（C54H92O23）不得少于 0.20%（三者皂苷总量不得少于 0.50%）。\n\n"
                    "【性味与归经】甘、微苦，微温。归脾、肺、心、肾经。【功能与主治】大补元气，复脉固脱，补脾益肺，生津养血，安神益智。"
                ),
                "content_en": (
                    "ChP 2025 Volume I: Ginseng Radix et Rhizoma (Ginseng)\n\n"
                    "1. Origin: Dried root and rhizome of Panax ginseng C. A. Mey. (Araliaceae).\n\n"
                    "2. Assay Criteria (HPLC ChP 0512):\n"
                    "Calculated on dried basis:\n"
                    "- Sum of Ginsenoside Rg1 (C42H72O14) and Ginsenoside Re (C48H82O18) shall not be less than 0.30%;\n"
                    "- Ginsenoside Rb1 (C54H92O23) shall not be less than 0.20%.\n"
                    "- Total major ginsenosides not less than 0.50%.\n\n"
                    "Action: Strongly reinforces primordial qi, restores pulse, tonifies spleen and lung, promotes fluid production, tranquilizes mind."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_huanglian_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：黄连（Coptidis Rhizoma）",
        "doc_title_en": "ChP 2025 Vol I Official Monograph: Coptidis Rhizoma (Coptis Root)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol1_huanglian_monograph_full.pdf",
        "md_file": "chp_2025_vol1_huanglian_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol1_huanglian_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol1_huanglian_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：黄连三种基原（味连、雅连、云连）、性状特征与小檗碱/总生物碱含量测定",
                "title_en": "Section 1: Origins (Weilian, Yalian, Yunlian), Berberine Assay (>=5.5%) & Total Alkaloids",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：黄连（Coptidis Rhizoma）\n\n"
                    "一、基原植物与药材分类：\n"
                    "本品为毛茛科植物黄连 Coptis chinensis Franch.、三角叶黄连 Coptis deltoidea C. Y. Cheng et Hsiao 或云连 Coptis teeta Wall. 的干燥根茎。以上三种分别习称“味连”（鸡爪连）、“雅连”和“云连”。秋季采挖，除去须根和泥沙，干燥，撞去残留须根。\n\n"
                    "二、性状鉴别特征：\n"
                    "味连：多集聚成簇，常弯曲，形如鸡爪，单枝长 3~6cm，直径 0.3~0.8cm。表面灰黄色或黄褐色，粗糙，有不规则结节状隆起、须根及须根残基。部分节间较长，平滑如茎秆，习称“过桥”。质硬，折断面不整齐，皮部暗棕色或暗黄色，木部金黄色，射线有裂隙，髓部红棕色。气微，味极苦。\n\n"
                    "三、安全检查项目：\n"
                    "水分：不得过 14.0%；总灰分：不得过 5.0%；33种禁用农药符合规定。\n\n"
                    "四、含量测定（高效液相色谱法 通则 0512）：\n"
                    "按干燥品计算：\n"
                    "1. 盐酸小檗碱（C20H18ClNO4）：含小檗碱以盐酸小檗碱计，味连不得少于 5.5%，雅连不得少于 4.2%，云连不得少于 7.0%；\n"
                    "2. 黄连碱、巴马汀与药根碱：含黄连碱不得少于 1.6%，巴马汀不得少于 1.5%，表小檗碱不得少于 0.8%。\n\n"
                    "【性味与归经】苦，寒。归心、脾、胃、肝、胆、大肠经。【功能与主治】清热燥湿，泻火解毒。用于湿热痞满，呕吐吞酸，泻痢，黄疸，高热神昏，心烦不寐，血热吐衄，目赤，牙痛，消渴，痈肿疔疮。"
                ),
                "content_en": (
                    "ChP 2025 Volume I: Coptidis Rhizoma (Huanglian)\n\n"
                    "1. Botanical Origin: Coptis chinensis Franch., Coptis deltoidea, or Coptis teeta (Ranunculaceae).\n\n"
                    "2. Compendial Assay (HPLC ChP 0512):\n"
                    "Calculated on dried basis:\n"
                    "- Berberine hydrochloride: Weilian not less than 5.5%; Yalian not less than 4.2%; Yunlian not less than 7.0%.\n"
                    "- Coptisine not less than 1.6%; Palmatine not less than 1.5%.\n\n"
                    "Action: Clears heat and dries dampness, purges fire and detoxifies."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_gancao_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：甘草（Glycyrrhizae Radix et Rhizoma）",
        "doc_title_en": "ChP 2025 Vol I Official Monograph: Glycyrrhizae Radix et Rhizoma (Licorice)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol1_gancao_monograph_full.pdf",
        "md_file": "chp_2025_vol1_gancao_monograph_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol1_gancao_monograph_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol1_gancao_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：甘草三种基原、性状鉴别、甘草酸(>=2.0%)与甘草苷(>=0.50%)含量测定",
                "title_en": "Section 1: Origin, Characteristics, Glycyrrhizic Acid (>=2.0%) & Liquiritin (>=0.50%) Assay",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：甘草（Glycyrrhizae Radix et Rhizoma）\n\n"
                    "一、基原植物：\n"
                    "本品为豆科植物乌拉尔甘草 Glycyrrhiza uralensis Fisch.、胀果甘草 Glycyrrhiza inflata Batalin 或光果甘草 Glycyrrhiza glabra L. 的干燥根和根茎。春、秋二季采挖，除去须根，晒干。\n\n"
                    "二、性状鉴别特征：\n"
                    "根呈圆柱形，长 25~100cm，直径 0.6~3.5cm。外皮松紧不一，表面红棕色或灰棕色，具显著的纵皱纹、沟纹、皮孔及稀疏的细根痕。质坚实，断面略显纤维性，黄白色，粉性，形成层环纹明显，射线放射状，常有裂隙。气微，味甜而特殊。\n\n"
                    "三、检查项目：\n"
                    "水分：不得过 12.0%；总灰分：不得过 7.0%；酸不溶性灰分：不得过 2.0%；重金属与33种农残符合规定。\n\n"
                    "四、含量测定（高效液相色谱法 通则 0512）：\n"
                    "按干燥品计算：\n"
                    "1. 甘草苷（Liquiritin，C21H22O9）：不得少于 0.50%；\n"
                    "2. 甘草酸（Glycyrrhizic Acid，以甘草酸单铵盐计算）：不得少于 2.0%。\n\n"
                    "【性味与归经】甘，平。归心、肺、脾、胃经。【功能与主治】补脾益气，清热解毒，祛痰止咳，缓急止痛，调和诸药。用于脾胃虚弱，倦怠乏力，心悸气短，咳嗽痰多，脘腹、四肢挛急疼痛，痈肿疮毒，缓解药物毒性、烈性。"
                ),
                "content_en": (
                    "ChP 2025 Volume I: Glycyrrhizae Radix et Rhizoma (Licorice Root)\n\n"
                    "1. Botanical Origin: Glycyrrhiza uralensis Fisch., Glycyrrhiza inflata, or Glycyrrhiza glabra (Fabaceae).\n\n"
                    "2. Compendial Assay (HPLC ChP 0512):\n"
                    "Calculated on dried basis:\n"
                    "- Liquiritin (C21H22O9) shall not be less than 0.50%;\n"
                    "- Glycyrrhizic acid shall not be less than 2.0%.\n\n"
                    "Action: Tonifies spleen, replenishes qi, clears heat, resolves phlegm, relieves spasms and pain, harmonizes herbal characteristics in formulas."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_angong_niuhuang_wan",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：安宫牛黄丸",
        "doc_title_en": "ChP 2025 Vol I Official Monograph: Angong Niuhuang Wan (Bolus of Calculus Bovis)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Pharmacopoeia_Monograph",
        "source_file": "chp_2025_vol1_angong_niuhuang_wan_full.pdf",
        "md_file": "chp_2025_vol1_angong_niuhuang_wan_full.md",
        "pdf_subpath": "chp_2025/chp_2025_vol1_angong_niuhuang_wan_full.pdf",
        "sections": [
            {
                "section_id": "chp_vol1_angong_sec1_monograph",
                "page": 1,
                "title_zh": "第一节：安宫牛黄丸处方组成、制法、人工麝香/牛磺胆酸/栀子苷含量测定",
                "title_en": "Section 1: Prescription, Preparation, Quality Control (Taurocholic Acid, Geniposide, Baicalin)",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：安宫牛黄丸\n\n"
                    "一、法定处方组成（11味经典药材）：\n"
                    "体外培育牛黄（或牛黄）100g、水牛角浓缩粉 200g、人工麝香（或麝香）25g、珍珠 50g、朱砂 100g、雄黄 100g、黄连 100g、黄芩 100g、栀子 100g、郁金 100g、冰片 25g。辅料为赋形剂炼蜜。\n\n"
                    "二、性状与鉴别：\n"
                    "本品为包金衣或不包金衣的大蜜丸，除去金衣显黄橙色至红棕色；气芳香浓郁，味微苦、辛凉。\n\n"
                    "三、重金属汞与砷特征性控制：\n"
                    "处方中含朱砂（硫化汞 HgS）与雄黄（二硫化二砷 As2S2），严格限定其入药必须经过“水飞”超微粉碎工艺，以控制游离可溶性二价汞离子与三价砷离子，保障临床安全性。\n\n"
                    "四、含量测定（通则 0512 HPLC 法）：\n"
                    "1. 黄芩苷（Baicalin）：每丸含黄芩以黄芩苷计不得少于 18.0 mg；\n"
                    "2. 栀子苷（Geniposide）：每丸含栀子以栀子苷计不得少于 7.5 mg；\n"
                    "3. 胆酸与牛磺胆酸（牛黄特征成分）：HPLC-ELSD 或 LC-MS 测定符合法定下限。\n\n"
                    "【功能与主治】清热解毒，镇惊开窍。用于热病，邪入心包，高热惊厥，神昏谵语；中风昏迷及脑炎、脑膜炎、中毒性脑病见上述证候者。"
                ),
                "content_en": (
                    "ChP 2025 Volume I: Angong Niuhuang Wan\n\n"
                    "1. Compendial Formula: Calculus Bovis, Pulvis Cornus Bubali Concentratus, Moschus, Margarita, Cinnabaris, Realgar, Coptidis Rhizoma, Scutellariae Radix, Gardeniae Fructus, Curcumae Radix, Borneolum Syntheticum, refined honey.\n\n"
                    "2. Quantitative Standards (HPLC ChP 0512):\n"
                    "- Baicalin: Not less than 18.0 mg per bolus;\n"
                    "- Geniposide: Not less than 7.5 mg per bolus.\n\n"
                    "Actions: Clears heat and detoxifies, tremors-calming and opens sensory orifices for acute febrile loss of consciousness, stroke coma, encephalitis."
                )
            }
        ]
    }
]
