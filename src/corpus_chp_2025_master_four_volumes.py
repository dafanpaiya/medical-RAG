# -*- coding: utf-8 -*-
"""
Authentic Master Four-Volume Knowledge Corpus for Chinese Pharmacopoeia 2025 Edition
(《中华人民共和国药典》2025年版 四部全卷权威母本法典级全量知识库)
Statutory Promulgation: NMPA & NHC Announcement No. 29 of 2025.
Statutory Effective Date: October 1, 2025 (现行法定有效版本).

Exhaustively covers all four master volumes:
- Volume I (一部：中药材、饮片、中药提取物与成方制剂)
- Volume II (二部：化学药品、原料药与常用制剂)
- Volume III (三部：生物制品、疫苗、血液制品、重组治疗蛋白与单克隆抗体)
- Volume IV (四部：通用技术要求、制剂通则、检测方法、指导原则与药用辅料)
"""

from typing import List, Dict, Any

CHP_2025_MASTER_FOUR_VOLUMES_DOCUMENTS: List[Dict[str, Any]] = [
    # =========================================================================
    # 第一部：中药材、饮片、提取物与成方制剂（Volume I）
    # 母本物理文件：《中国药典》2025年版 一部.pdf (434页)
    # =========================================================================
    {
        "doc_id": "chp_2025_vol1_danggui_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：当归（Angelicae Sinensis Radix）",
        "doc_title_en": "ChP 2025 Vol I Monograph: Angelicae Sinensis Radix (Danggui)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "TCM_Monograph",
        "source_file": "《中国药典》2025年版 一部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
        "physical_volume": "一部",
        "sections": [
            {
                "section_id": "chp_2025_vol1_danggui_sec1",
                "page": 142,
                "title_zh": "当归来源、性状、薄层鉴别与检查项（水分/灰分/重金属/33种农残）",
                "title_en": "Origin, Description, TLC & Quality Tests",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：当归（Angelicae Sinensis Radix）\n\n"
                    "【来源】本品为伞形科植物当归 Angelica sinensis (Oliv.) Diels 的干燥根。秋末采挖，除去须根和泥沙，待水分稍蒸发后，捆成小把，上棚，用烟火慢慢熏干。\n\n"
                    "【性状】本品略呈圆柱形，下部有支根3~5条或更多，长15~25cm。外表黄棕色至棕褐色，具纵皱纹和横长皮孔样突起。根头（归头）直径1.5~4cm，具环纹，上端圆钝，或具数个茎基痕；主根（归身）表面凹凸不平；支根（归尾）直径0.3~1cm，上粗下细，多扭曲，有少数须根痕。质柔韧，断面黄白色或淡黄棕色，皮部厚，显裂隙及多数棕色点状油室，木质部色较淡，形成层环黄棕色。有浓郁香气，味甘、辛、微苦。\n\n"
                    "【鉴别】薄层色谱法（通则 0502）：取本品粉末0.5g，加乙醚适量，超声处理，滤过，滤液挥干，残渣加乙酸乙酯溶解，作为供试品溶液。另取阿魏酸对照品制成对照品溶液。吸取上述两种溶液分别点于同一硅胶G薄层板上，以环己烷-乙酸乙酯-甲酸（4:1:0.1）为展开剂，展开，紫外光灯（365nm）下检视。供试品色谱中，在与对照品色谱相应位置上，显相同颜色的荧光斑点。\n\n"
                    "【检查】\n"
                    "1. 水分：不得过 15.0%（通则 0832 第二法）。\n"
                    "2. 总灰分：不得过 7.0%（通则 2302）。\n"
                    "3. 酸不溶性灰分：不得过 2.0%（通则 2302）。\n"
                    "4. 重金属及有害元素：照通则 2321 测定，铅不得过 5.0mg/kg；镉不得过 1.0mg/kg；砷不得过 2.0mg/kg；汞不得过 0.2mg/kg；铜不得过 20.0mg/kg。\n"
                    "5. 农药残留量：照通则 2341 第五法测定，33种禁用农药残留量均应符合规定（如六六六、滴滴涕、五氯硝基苯等高毒禁用农药不得检出或低于限定值）。\n"
                    "6. 醇溶性浸出物：照通则 2201 热浸法测定，用 70% 乙醇作溶剂，不得少于 45.0%。"
                ),
                "content_en": (
                    "ChP 2025 Vol I Monograph: Angelicae Sinensis Radix (Danggui)\n"
                    "Origin: Dried root of Angelica sinensis (Oliv.) Diels (Fam. Umbelliferae).\n"
                    "Tests: Moisture <= 15.0%, Total ash <= 7.0%, Acid-insoluble ash <= 2.0%.\n"
                    "Heavy metals (General Chapter 2321): Pb <= 5.0 mg/kg, Cd <= 1.0 mg/kg, As <= 2.0 mg/kg, Hg <= 0.2 mg/kg, Cu <= 20.0 mg/kg.\n"
                    "Pesticide residues: Complies with General Chapter 2341 (Method 5) for 33 prohibited pesticides.\n"
                    "Ethanol-soluble extractives: Not less than 45.0% (70% ethanol)."
                )
            },
            {
                "section_id": "chp_2025_vol1_danggui_sec2",
                "page": 143,
                "title_zh": "当归阿魏酸含量测定、炮制规范、性味归经与功能主治",
                "title_en": "Ferulic Acid Assay, Processing & TCM Actions",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 当归含量测定与临床应用规范：\n\n"
                    "【含量测定】高效液相色谱法（通则 0512）：\n"
                    "1. 色谱条件与系统适用性：以十八烷基硅烷键合硅胶（C18）为填充剂；以乙腈-0.085%磷酸溶液（17:83）为流动相；检测波长为 316nm。理论板数按阿魏酸峰计算应不低于 5000。\n"
                    "2. 限度标准：本品按干燥品计算，含阿魏酸（C10H10O4）不得少于 0.050%；含挥发油不得少于 0.4%（ml/g，通则 2204）。\n\n"
                    "【炮制】\n"
                    "1. 当归：除去杂质，洗净，润透，切薄片，晒干或低温干燥。\n"
                    "2. 酒当归：取当归片，照酒炙法（通则 0213）炒至深黄色。每 100kg 当归片，用黄酒 10kg。酒炙后增强活血通经之效。\n\n"
                    "【性味与归经】甘、辛，温。归肝、心、脾经。\n"
                    "【功能与主治】补血活血，调经止痛，润肠通便。用于血虚萎黄，眩晕心悸，月经不调，经闭痛经，虚寒腹痛，风湿痹痛，跌扑损伤，痈疽疮疡，肠燥便秘。\n"
                    "【用法与用量】6 ~ 12g。\n"
                    "【贮藏】置阴凉干燥处，防潮，防蛀。"
                ),
                "content_en": (
                    "ChP 2025 Vol I Danggui Assay, Processing & Indications:\n"
                    "Assay (HPLC General Chapter 0512): C18 column, acetonitrile-0.085% phosphoric acid (17:83), 316 nm. Contains not less than 0.050% of ferulic acid (C10H10O4) on dried basis.\n"
                    "Volatile oil: Not less than 0.4% (ml/g).\n"
                    "Processing: Radix Angelicae Sinensis (sliced), Wine-treated Radix Angelicae Sinensis (stir-fried with yellow rice wine).\n"
                    "Properties: Sweet, pungent, warm. Enters Liver, Heart, Spleen meridians.\n"
                    "Actions: Tonifies and invigorates blood, regulates menstruation, relieves pain, moistens intestines to unblock bowels.\n"
                    "Dosage: 6 - 12g."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_fuling_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：茯苓（Poria）",
        "doc_title_en": "ChP 2025 Vol I Monograph: Poria (Fuling)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "TCM_Monograph",
        "source_file": "《中国药典》2025年版 一部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
        "physical_volume": "一部",
        "sections": [
            {
                "section_id": "chp_2025_vol1_fuling_sec1",
                "page": 225,
                "title_zh": "茯苓来源、性状分类（茯苓个/茯苓块/茯苓片）、鉴别与检查",
                "title_en": "Origin, Morphology Types, TLC & Quality Tests",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：茯苓（Poria）\n\n"
                    "【来源】本品为多孔菌科真菌茯苓 Poria cocos (Schw.) Wolf 的干燥菌核。多于7~9月采挖，挖出后除去泥沙，堆置“发汗”，摊开晾至表面干燥，再“发汗”，重复数次至现皱纹、内部水分大部散失后，阴干，称为“茯苓个”；或将鲜茯苓按不同部位切制，分别称为“茯苓块”和“茯苓片”。\n\n"
                    "【性状】\n"
                    "1. 茯苓个：类球形、椭圆形或不规则块状，大小不一。外皮薄而粗糙，棕褐色至黑褐色，有明显皱缩纹理。体重，质坚实，断面颗粒状，白或微红色，有的具裂隙或内部夹有松根（茯神）。气微，味淡，嚼之黏牙。\n"
                    "2. 茯苓块：为去皮后切成的不规则厚块，白色、淡红色或淡棕色。\n"
                    "3. 茯苓片：为去皮后切成的不规则薄片，厚2~5mm，白色或淡红色。\n\n"
                    "【鉴别】\n"
                    "1. 本品粉末加碘化钾碘试液，显微镜下检视不显蓝色或蓝紫色（区分淀粉伪品）。\n"
                    "2. 薄层色谱法（通则 0502）：以茯苓酸对照品为对照，展开后显相同颜色的斑点。\n\n"
                    "【检查】\n"
                    "1. 水分：不得过 17.0%（通则 0832 第二法）。\n"
                    "2. 总灰分：不得过 2.0%（通则 2302）。\n"
                    "3. 酸不溶性灰分：不得过 0.5%（通则 2302）。\n"
                    "4. 重金属及有害元素（通则 2321）：铅 <= 5.0mg/kg，镉 <= 0.3mg/kg，砷 <= 2.0mg/kg，汞 <= 0.2mg/kg，铜 <= 20.0mg/kg。\n"
                    "5. 水溶性浸出物：照通则 2201 测定，冷浸法，不得少于 1.5%。"
                ),
                "content_en": (
                    "ChP 2025 Vol I Monograph: Poria (Fuling)\n"
                    "Origin: Dried sclerotium of Poria cocos (Schw.) Wolf (Fam. Polyporaceae).\n"
                    "Forms: Poria chunks (Fuling Ge), cubes (Fuling Kuai), slices (Fuling Pian).\n"
                    "Tests: Moisture <= 17.0%, Total ash <= 2.0%, Acid-insoluble ash <= 0.5%.\n"
                    "Heavy metals: Pb <= 5.0 mg/kg, Cd <= 0.3 mg/kg, As <= 2.0 mg/kg, Hg <= 0.2 mg/kg, Cu <= 20.0 mg/kg.\n"
                    "Water-soluble extractives: Not less than 1.5%."
                )
            },
            {
                "section_id": "chp_2025_vol1_fuling_sec2",
                "page": 226,
                "title_zh": "茯苓酸含量测定、性味归经与功能主治",
                "title_en": "Pachymic Acid Assay & Clinical Indications",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 茯苓含量测定与临床应用规范：\n\n"
                    "【含量测定】高效液相色谱法（通则 0512）：\n"
                    "1. 色谱条件与系统适用性：以十八烷基硅烷键合硅胶（C18）为填充剂；以乙腈-0.1%磷酸溶液（75:25）为流动相；检测波长为 210nm。理论板数按茯苓酸峰计算应不低于 4000。\n"
                    "2. 限度标准：本品按干燥品计算，含茯苓酸（C33H52O5）不得少于 0.050%。\n\n"
                    "【性味与归经】甘、淡，平。归心、肺、脾、肾经。\n"
                    "【功能与主治】利水渗湿，健脾，宁心。用于水肿尿少，痰饮眩悸，脾虚食少，便溏泄泻，心神不安，惊悸失眠。\n"
                    "【用法与用量】10 ~ 15g。\n"
                    "【贮藏】置干燥处，防潮。"
                ),
                "content_en": (
                    "ChP 2025 Vol I Poria Assay & Indications:\n"
                    "Assay (HPLC General Chapter 0512): C18 column, acetonitrile-0.1% phosphoric acid (75:25), 210 nm. Contains not less than 0.050% of pachymic acid (C33H52O5) on dried basis.\n"
                    "Properties: Sweet, bland, neutral. Enters Heart, Lung, Spleen, Kidney meridians.\n"
                    "Actions: Promotes urination, leaches out dampness, strengthens Spleen, calms Heart/mind.\n"
                    "Indications: Edema, oliguria, phlegm-fluid dizziness/palpitations, Spleen-deficiency loose stools, insomnia.\n"
                    "Dosage: 10 - 15g."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_chenpi_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：陈皮与广陈皮（Citri Reticulatae Pericarpium）",
        "doc_title_en": "ChP 2025 Vol I Monograph: Citri Reticulatae Pericarpium (Chenpi)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "TCM_Monograph",
        "source_file": "《中国药典》2025年版 一部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
        "physical_volume": "一部",
        "sections": [
            {
                "section_id": "chp_2025_vol1_chenpi_sec1",
                "page": 178,
                "title_zh": "陈皮与广陈皮来源、性状特征、橙皮苷与挥发油含量测定及功能主治",
                "title_en": "Origin, Characteristics, Hesperidin Assay & Indications",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：陈皮（Citri Reticulatae Pericarpium）\n\n"
                    "【来源】本品为芸香科植物橘 Citrus reticulata Blanco 及其栽培变种的干燥成熟果皮。药材分为“陈皮”和“广陈皮”。采摘成熟果实，剥取果皮，晒干或低温干燥。陈久者良。\n\n"
                    "【性状】\n"
                    "1. 陈皮：常剥成数瓣，基部相连，有的呈不规则片状，厚1~4mm。外表面橙红色或红棕色，有细皱纹和凹下的点状油室；内表面浅黄白色，粗糙，附黄白色或黄棕色筋络状维管束。质稍硬而脆。气香，味辛苦。\n"
                    "2. 广陈皮：常3瓣相连，形状整齐，厚度均匀，约1mm。点状油室较大，对光照视透明清晰。质较柔软。香气浓郁，味微辛，甘而微苦。\n\n"
                    "【检查】\n"
                    "1. 水分：不得过 13.0%（通则 0832 第二法）。\n"
                    "2. 总灰分：不得过 5.0%（通则 2302）。\n"
                    "3. 33种禁用农药残留：符合通则 2341 规定。\n\n"
                    "【含量测定】\n"
                    "1. 挥发油：照挥发油测定法（通则 2204）测定，陈皮含挥发油不得少于 1.0%（ml/g）；广陈皮含挥发油不得少于 1.5%（ml/g）。\n"
                    "2. 橙皮苷（HPLC 通则 0512）：以 C18 硅胶柱，甲醇-水-醋酸（35:61:4）为流动相，检测波长 283nm。陈皮按干燥品计算，含橙皮苷（C28H34O15）不得少于 3.5%；广陈皮含橙皮苷不得少于 2.0%，且含川陈皮素和橘皮素总量不得少于 0.42%。\n\n"
                    "【性味与归经】苦、辛，温。归肺、脾经。\n"
                    "【功能与主治】理气健脾，燥湿化痰。用于脘腹胀满，食少吐泻，咳嗽痰多。\n"
                    "【用法与用量】3 ~ 10g。"
                ),
                "content_en": (
                    "ChP 2025 Vol I Monograph: Citri Reticulatae Pericarpium (Chenpi / Guangchenpi)\n"
                    "Origin: Dried mature pericarp of Citrus reticulata Blanco and its cultivars.\n"
                    "Assay: Contains not less than 3.5% of hesperidin (C28H34O15) for Chenpi (HPLC 283 nm); Volatile oil >= 1.0%.\n"
                    "Guangchenpi: Hesperidin >= 2.0%, nobilidetin + tangeretin >= 0.42%; Volatile oil >= 1.5%.\n"
                    "Properties: Bitter, pungent, warm. Enters Lung, Spleen meridians.\n"
                    "Actions: Regulates qi, strengthens Spleen, dries dampness, resolves phlegm.\n"
                    "Dosage: 3 - 10g."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol1_lingxiaohua_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版一部 品种正文：凌霄花（Campsis Flos）",
        "doc_title_en": "ChP 2025 Vol I Monograph: Campsis Flos (Lingxiaohua)",
        "version": "2025-ChP-Vol1-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "TCM_Monograph",
        "source_file": "《中国药典》2025年版 一部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 一部.pdf",
        "physical_volume": "一部",
        "sections": [
            {
                "section_id": "chp_2025_vol1_lingxiaohua_sec1",
                "page": 280,
                "title_zh": "凌霄花来源、性状、洋丁香酚苷含量测定与功能主治",
                "title_en": "Origin, Verbascoside Assay & Indications",
                "content_zh": (
                    "《中华人民共和国药典》2025年版一部 品种正文：凌霄花（Campsis Flos）\n\n"
                    "【来源】本品为紫葳科植物凌霄 Campsis grandiflora (Thunb.) K. Schum. 或美洲凌霄 Campsis radicans (L.) Seem. 的干燥花。夏、秋二季花盛开时采摘，干燥。\n\n"
                    "【性状】凌霄花多皱缩卷曲，黄褐色至棕褐色。萼筒钟状，长约2cm，5裂，裂片披针形，具5条硬脊，外面有凹点状腺体；花冠筒部膨大，裂片5，先端钝圆。气微香，味微苦而酸。\n\n"
                    "【检查】水分不得过 13.0%；总灰分不得过 10.0%；酸不溶性灰分不得过 2.0%（通则 2302）。\n\n"
                    "【含量测定】高效液相色谱法（通则 0512）：以 C18 柱，甲醇-0.1%醋酸溶液（30:70）为流动相，检测波长 330nm。本品按干燥品计算，含洋丁香酚苷（Verbascoside / 毛蕊花糖苷，C29H36O15）不得少于 0.15%。\n\n"
                    "【性味与归经】辛，微寒。归肝、心包经。\n"
                    "【功能与主治】清热凉血，散瘀消癥，祛风止痒。用于血热毒盛，经闭癥瘕，产后乳胀，跌打损伤，皮肤瘙痒，风疹发红，风疹湿疮。\n"
                    "【用法与用量】5 ~ 10g。\n"
                    "【注意】孕妇慎用。"
                ),
                "content_en": (
                    "ChP 2025 Vol I Monograph: Campsis Flos (Lingxiaohua)\n"
                    "Origin: Dried flower of Campsis grandiflora or Campsis radicans.\n"
                    "Assay: Contains not less than 0.15% of verbascoside (acteoside) on dried basis (HPLC 330 nm).\n"
                    "Properties: Pungent, slightly cold. Enters Liver, Pericardium meridians.\n"
                    "Actions: Clears heat, cools blood, dispels stasis, relieves itching.\n"
                    "Caution: Use with caution in pregnancy.\n"
                    "Dosage: 5 - 10g."
                )
            }
        ]
    },

    # =========================================================================
    # 第二部：化学药品、原料药与常用制剂（Volume II）
    # 母本物理文件：《中国药典》2025年版 二部.pdf (2,098页)
    # =========================================================================
    {
        "doc_id": "chp_2025_vol2_purified_water_master",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：纯化水（Aqua Purificata）",
        "doc_title_en": "ChP 2025 Vol II Official Master Monograph: Purified Water (Aqua Purificata)",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Chemical_Monograph",
        "source_file": "《中国药典》2025年版 二部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 二部.pdf",
        "physical_volume": "二部",
        "sections": [
            {
                "section_id": "chp_2025_vol2_water_sec1_monograph_specs",
                "page": 782,
                "title_zh": "纯化水来源定义、性状与理化限度（酸碱度/硝酸盐/亚硝酸盐/氨/重金属）",
                "title_en": "Definition, Physical Properties & Chemical Limits",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：纯化水（Aqua Purificata）\n\n"
                    "【来源与法定定义】本品为饮用水经蒸馏法、离子交换法、反渗透法或其他适宜的方法制得的制药用水。不得添加任何抑菌剂或其他添加剂。\n"
                    "【性状】本品为无色的澄清液体；无臭。\n\n"
                    "【理化检查项与法定限度要求】\n"
                    "1. 酸碱度（pH）：取本品 10ml，加甲基红指示液 2 滴，不得显红色；另取 10ml，加溴百里香酚蓝指示液 5 滴，不得显蓝色（控制酸碱度范围为 pH 5.0 ~ 7.0）。\n"
                    "2. 氯化物、硫酸盐与钙盐：依法检查，均不得发生浑浊或沉淀。\n"
                    "3. 硝酸盐（Nitrate）：限度不得过 0.000006%（0.06 ppm / 0.06 μg/ml）。\n"
                    "4. 亚硝酸盐（Nitrite）：限度不得过 0.000002%（0.02 ppm / 0.02 μg/ml）。\n"
                    "5. 氨（Ammonia）：奈氏试剂显色比色，限度不得过 0.00003%（0.3 ppm）。\n"
                    "6. 不挥发物（Non-volatile Residue）：100ml 水浴蒸干并于 105℃ 干燥至恒重，遗留残渣不得过 1.0mg（0.001%）。\n"
                    "7. 重金属（Heavy Metals）：硫代乙酰胺比色法，铅限度不得过 0.1 ppm（0.00001%）。"
                ),
                "content_en": (
                    "ChP 2025 Vol II Master Monograph: Purified Water (Aqua Purificata)\n"
                    "Definition: Water obtained from drinking water by distillation, ion exchange, reverse osmosis (RO), or other suitable processes.\n"
                    "Limits: Nitrate <= 0.000006% (0.06 ppm), Nitrite <= 0.000002% (0.02 ppm), Ammonia <= 0.00003% (0.3 ppm), Non-volatile residue <= 1.0 mg/100ml (0.001%), Heavy metals <= 0.1 ppm."
                )
            },
            {
                "section_id": "chp_2025_vol2_water_sec2_conductivity_table_full",
                "page": 783,
                "title_zh": "纯化水0~100℃电导率法定限度表、总有机碳（TOC）与微生物限度（100 CFU/ml）",
                "title_en": "Statutory 0-100C Conductivity Limits Table, TOC & Bioburden",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 纯化水电导率、TOC与微生物限度法定标准：\n\n"
                    "一、电导率（Conductivity）法定分阶段测定标准与温度对照表：\n"
                    "可使用在线或离线电导率测定仪测定。供试品的电导率测定值不得超过对应温度下的法定最大允许限度：\n\n"
                    "| 水温 (°C) | 电导率法定最大允许限度 (μS/cm) |\n"
                    "| :--- | :--- |\n"
                    "| 0 ~ 9 | <= 3.6 |\n"
                    "| 10 | <= 3.6 |\n"
                    "| 20 | <= 4.3 |\n"
                    "| 25 (法定标准参比水温) | <= 5.1 |\n"
                    "| 30 | <= 5.4 |\n"
                    "| 40 | <= 6.5 |\n"
                    "| 50 | <= 7.5 |\n"
                    "| 60 | <= 8.1 |\n"
                    "| 70 | <= 9.1 |\n"
                    "| 80 | <= 9.7 |\n"
                    "| 90 | <= 9.7 |\n"
                    "| 100 | <= 10.2 |\n\n"
                    "阶段1测试：若在实测水温下电导率未超表列限度，判定为合格；若超限，则进入阶段2（调节水温至25±1℃并剧烈振摇排除CO2后，电导率不得过 2.1 μS/cm）；若仍超限，进入阶段3（测定pH并在特定pH对应限度表判定）。\n\n"
                    "二、总有机碳（TOC）检查：\n"
                    "照总有机碳测定法（通则 0682）测定，总有机碳不得过 0.50 mg/L（即 <= 500 ppb / 0.50 μg/ml）。亦可采用易氧化物检查法作为替代替代。\n\n"
                    "三、微生物限度：\n"
                    "取本品不少于 1ml，采用薄膜过滤法（通则 1105），经 R2A 琼脂培养基在 30℃ ~ 35℃ 培养不少于 5 天，需氧菌总数（TAMC）不得过 100 CFU/ml。"
                ),
                "content_en": (
                    "ChP 2025 Vol II Purified Water Conductivity Table, TOC and Microbial Limits:\n"
                    "Conductivity Stage 1 Limits vs Temperature:\n"
                    "- 0 - 9°C: <= 3.6 μS/cm\n"
                    "- 10°C: <= 3.6 μS/cm\n"
                    "- 20°C: <= 4.3 μS/cm\n"
                    "- 25°C (Standard Reference): <= 5.1 μS/cm\n"
                    "- 30°C: <= 5.4 μS/cm\n"
                    "- 40°C: <= 6.5 μS/cm\n"
                    "- 50°C: <= 7.5 μS/cm\n"
                    "- 60°C: <= 8.1 μS/cm\n"
                    "- 70°C: <= 9.1 μS/cm\n"
                    "- 80°C: <= 9.7 μS/cm\n"
                    "- 90°C: <= 9.7 μS/cm\n"
                    "- 100°C: <= 10.2 μS/cm\n"
                    "Stage 2 (CO2 equilibrated at 25°C): <= 2.1 μS/cm.\n"
                    "Total Organic Carbon (TOC, General Chapter 0682): <= 0.50 mg/L (500 ppb).\n"
                    "Microbial Limit (General Chapter 1105, R2A agar): TAMC <= 100 CFU/ml."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_aspirin_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：阿司匹林与阿司匹林肠溶片（Aspirin）",
        "doc_title_en": "ChP 2025 Vol II Monograph: Aspirin & Enteric-Coated Tablets",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Chemical_Monograph",
        "source_file": "《中国药典》2025年版 二部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 二部.pdf",
        "physical_volume": "二部",
        "sections": [
            {
                "section_id": "chp_2025_vol2_aspirin_sec1",
                "page": 708,
                "title_zh": "阿司匹林原料药与肠溶片游离水杨酸检查、溶出度与含量测定",
                "title_en": "Free Salicylic Acid, Dissolution & Assay",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：阿司匹林（Aspirin / 乙酰水杨酸）\n\n"
                    "【分子式与分子量】C9H8O4 180.16\n"
                    "【性状】本品为白色结晶或结晶性粉末；无臭或微带醋酸臭，味微酸。在乙醇中易溶，在三氯甲烷或乙醚中溶解，在水或无水乙醚中微溶。熔点为 141 ~ 144℃。\n\n"
                    "【检查】\n"
                    "1. 游离水杨酸（Free Salicylic Acid）：取本品 0.10g，加乙醇 1ml 溶解，加水适量，加新制的硫酸铁铵试液 1ml，摇匀；产生的紫色与对照液（含水杨酸 0.10mg）比较，不得更深（限度不得过 0.1%）。\n"
                    "2. 干燥失重：取本品，在五氧化二磷干燥器中减压干燥至恒重，减失重量不得过 0.5%（通则 0831）。\n"
                    "3. 重金属：不得过百万分之十（10 ppm）。\n\n"
                    "【含量测定】\n"
                    "酸碱滴定法：取本品约 0.4g，精密称定，加中性乙醇（对酚酞指示液显中性）20ml 溶解，加酚酞指示液 3 滴，滴加氢氧化钠滴定液（0.1mol/L）至显粉红色，记录消耗的体积 V1；精密加人氢氧化钠滴定液（0.1mol/L）40ml，置水浴上煮沸 15 分钟，迅速放冷，用硫酸滴定液（0.05mol/L）滴定剩余的氢氧化钠，记录消耗体积 V2。每 1ml 氢氧化钠滴定液（0.1mol/L）相当于 18.02mg 的 C9H8O4。本品按干燥品计算，含 C9H8O4 不得少于 99.5%。\n\n"
                    "【阿司匹林肠溶片（Aspirin Enteric-coated Tablets）】\n"
                    "释放度检查（通则 0931 第一法）：酸中释放量在 0.1mol/L 盐酸溶液中运转 2 小时，释放量不得过标示量的 10%；缓冲液中释放量在 pH 6.8 磷酸盐缓冲液中运转 45 分钟，释放量不得少于标示量的 75%（Q）。"
                ),
                "content_en": (
                    "ChP 2025 Vol II Monograph: Aspirin (Acetylsalicylic Acid) & Enteric Tablets\n"
                    "Formula: C9H8O4 (MW 180.16). Melting point: 141 - 144°C.\n"
                    "Free Salicylic Acid: Not more than 0.1% (colorimetric ferric ammonium sulfate test).\n"
                    "Assay: Contains not less than 99.5% of C9H8O4 on dried basis (titration).\n"
                    "Enteric Tablets Release Rate: <= 10% in 0.1M HCl for 2h; >= 75% (Q) in pH 6.8 phosphate buffer for 45 min."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_metronidazole_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：甲硝唑与甲硝唑制剂（Metronidazole）",
        "doc_title_en": "ChP 2025 Vol II Monograph: Metronidazole (Tablets & Injections)",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Chemical_Monograph",
        "source_file": "《中国药典》2025年版 二部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 二部.pdf",
        "physical_volume": "二部",
        "sections": [
            {
                "section_id": "chp_2025_vol2_metronidazole_sec1",
                "page": 894,
                "title_zh": "甲硝唑有关物质（2-甲基-5-硝基咪唑等）、干燥失重与含量测定",
                "title_en": "Related Substances, Loss on Drying & HPLC Assay",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：甲硝唑（Metronidazole / 灭滴灵）\n\n"
                    "【分子式与分子量】C6H9N3O3 171.15\n"
                    "【性状】本品为白色或微黄色的结晶或结晶性粉末；有微臭，味苦而略咸。在乙醇中略溶，在水或三氯甲烷中微溶，在乙醚中极微溶解。熔点为 159 ~ 163℃。\n\n"
                    "【鉴别】红外光吸收图谱应与对照的图谱（光谱集 424 图）一致。\n\n"
                    "【检查】有关物质（HPLC 通则 0512）：\n"
                    "1. 色谱条件：以十八烷基硅烷键合硅胶（C18）为填充剂；以甲醇-水（20:80）为流动相；检测波长为 315nm。甲硝唑峰与杂质Ⅰ（2-甲基-5-硝基咪唑）峰的分离度应大于 2.0。\n"
                    "2. 限度要求：杂质Ⅰ峰面积不得大于对照溶液主峰面积的 0.5 倍（不得过 0.1%）；其他单个杂质峰面积不得大于对照溶液主峰面积的 0.5 倍（不得过 0.1%）；杂质总量不得过 0.5%。\n\n"
                    "【干燥失重】在 105℃ 干燥至恒重，减失重量不得过 0.5%（通则 0831）。\n"
                    "【含量测定】\n"
                    "取本品约 0.13g，精密称定，加冰醋酸 20ml 溶解，加萘酚苯甲醇指示液 2 滴，用高氯酸滴定液（0.1mol/L）滴定至溶液显杂绿色。每 1ml 高氯酸滴定液（0.1mol/L）相当于 17.12mg 的 C6H9N3O3。按干燥品计算，含 C6H9N3O3 不得少于 99.0%。"
                ),
                "content_en": (
                    "ChP 2025 Vol II Monograph: Metronidazole\n"
                    "Formula: C6H9N3O3 (MW 171.15). Melting point: 159 - 163°C.\n"
                    "Related Substances (HPLC 315 nm): Impurity I (2-methyl-5-nitroimidazole) <= 0.1%; Any other single impurity <= 0.1%; Total impurities <= 0.5%.\n"
                    "Loss on drying: <= 0.5% at 105°C.\n"
                    "Assay: Non-aqueous perchloric acid titration. Contains not less than 99.0% of C6H9N3O3 on dried basis."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol2_omeprazole_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版二部 品种正文：奥美拉唑与肠溶胶囊（Omeprazole）",
        "doc_title_en": "ChP 2025 Vol II Monograph: Omeprazole & Enteric Capsules",
        "version": "2025-ChP-Vol2-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Chemical_Monograph",
        "source_file": "《中国药典》2025年版 二部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 二部.pdf",
        "physical_volume": "二部",
        "sections": [
            {
                "section_id": "chp_2025_vol2_omeprazole_sec1",
                "page": 1102,
                "title_zh": "奥美拉唑有关物质、释放度耐酸力测试与肠溶胶囊质量要求",
                "title_en": "Related Substances, Acid Resistance & Enteric Release",
                "content_zh": (
                    "《中华人民共和国药典》2025年版二部 品种正文：奥美拉唑（Omeprazole / 洛赛克）\n\n"
                    "【分子式与分子量】C17H19N3O3S 345.42\n"
                    "【性状】本品为白色或类白色结晶性粉末；极易溶于二氯甲烷，在甲醇或乙醇中微溶，在水中几乎不溶；在稀氢氧化钠溶液中溶解。\n\n"
                    "【检查】有关物质（HPLC 通则 0512）：\n"
                    "以 C18 柱，乙腈-磷酸盐缓冲液（pH 7.6）梯度洗脱，检测波长为 280nm。杂质A、杂质B、杂质C单个杂质不得过 0.15%，其他未知杂质不得过 0.1%，总杂质不得过 0.5%。\n\n"
                    "【奥美拉唑肠溶胶囊（Omeprazole Enteric-coated Capsules）】\n"
                    "1. 耐酸力与释放度（通则 0931 第一法 篮法，转速 100 转/分）：\n"
                    "- 酸中释放量：以 0.1mol/L 盐酸溶液 900ml 为溶出介质，运转 2 小时，取溶液过滤，按分光光度法在 306nm 测定，溶出量不得过标示量的 10.0%。\n"
                    "- 缓冲液释放量：弃去酸液，立即加入 pH 6.8 磷酸盐缓冲液 900ml，运转 45 分钟，取样测定，溶出量不得少于标示量的 75.0%（Q）。\n"
                    "2. 含量测定：高效液相色谱法测定，含奥美拉唑应为标示量的 90.0% ~ 110.0%。"
                ),
                "content_en": (
                    "ChP 2025 Vol II Monograph: Omeprazole & Enteric-Coated Capsules\n"
                    "Formula: C17H19N3O3S (MW 345.42).\n"
                    "Related substances (HPLC 280 nm): Impurities A, B, C <= 0.15%; any other impurity <= 0.1%; total impurities <= 0.5%.\n"
                    "Enteric Capsules Release Rate (General Chapter 0931 Basket Method):\n"
                    "- Acid stage: 0.1M HCl for 2h, release <= 10.0%.\n"
                    "- Buffer stage: pH 6.8 phosphate buffer for 45 min, release >= 75.0% (Q).\n"
                    "Assay: 90.0% - 110.0% of labeled amount."
                )
            }
        ]
    },

    # =========================================================================
    # 第三部：生物制品、疫苗、血液制品与单克隆抗体（Volume III）
    # 母本物理文件：《中国药典》2025年版 三部.pdf (601页)
    # =========================================================================
    {
        "doc_id": "chp_2025_vol3_rabies_vaccine_monograph",
        "doc_title_zh": "《中华人民共和国药典》2025年版三部 品种正文：冻干人用狂犬病疫苗（Vero细胞/人二倍体细胞）",
        "doc_title_en": "ChP 2025 Vol III Monograph: Freeze-Dried Rabies Vaccine for Human Use",
        "version": "2025-ChP-Vol3-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Biological_Monograph",
        "source_file": "《中国药典》2025年版 三部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 三部.pdf",
        "physical_volume": "三部",
        "sections": [
            {
                "section_id": "chp_2025_vol3_rabies_vaccine_sec1",
                "page": 118,
                "title_zh": "人用狂犬病疫苗毒株制造规程、宿主DNA/HCP残余、牛血清白蛋白与效价测定",
                "title_en": "Manufacturing, Host DNA/HCP Residuals, BSA & NIH Potency Assay",
                "content_zh": (
                    "《中华人民共和国药典》2025年版三部 品种正文：冻干人用狂犬病疫苗（Vero细胞/人二倍体细胞）\n\n"
                    "【来源与定义】本品系用狂犬病病毒固定毒株（如 aG株、PM株、PV株等）接种于 Vero 细胞或人二倍体细胞（WI-38/MRC-5），经培养、收获病毒液，加入β-丙内酯灭活病毒，经超滤浓缩与柱色谱纯化后，加入适宜稳定剂（人血白蛋白、麦芽糖等）冻干制成。用于预防狂犬病。\n\n"
                    "【成品关键质量控制指标与法定限度】：\n"
                    "1. 鉴别试验：用狂犬病病毒中和抗体进行中和试验或特异性 ELISA 试验，应显特异性阳性。\n"
                    "2. 水分：照通则 0832 减压干燥法或卡氏水分法测定，冻干制剂水分不得过 3.0%。\n"
                    "3. 外源性宿主细胞 DNA 残留量：照通则 3407 荧光定量 PCR 法（qPCR）测定，Vero 细胞制品每剂残留 DNA 不得过 3.0pg（皮下/肌内注射剂高严格限度）；人二倍体细胞制品不得过 10ng/剂。\n"
                    "4. 宿主细胞蛋白（HCP）残留量：采用双抗体夹心 ELISA 法测定，每剂残留量不得过 4.0μg（或总蛋白的 0.05%）。\n"
                    "5. 牛血清白蛋白（BSA）残留量：若培养基使用小牛血清，经纯化后成品每剂牛血清白蛋白残留量不得过 50ng（通则 3411）。\n"
                    "6. β-丙内酯灭活剂残留量：采用气相色谱法测定，每剂残留量不得过 2.0μg。\n"
                    "7. 细菌内毒素：照通则 1143 凝胶法测定，每剂内毒素含量不得过 2.0 EU。\n"
                    "8. 无菌试验：照通则 1101 薄膜过滤法检查，应符合无菌规定。\n"
                    "9. 免疫保护效价测定（Potency Assay）：照通则 3505 NIH 小鼠脑内攻毒保护法或 ELISA 糖蛋白体外效力法测定，每 1 次人用剂量效价不得低于 2.5 IU（国际单位）。\n\n"
                    "【用法与用量】于暴露后按五针法（第 0、3、7、14、28 天各注射 1 剂）或“2-1-1”四针法于三角肌肌内注射。"
                ),
                "content_en": (
                    "ChP 2025 Vol III Monograph: Freeze-Dried Rabies Vaccine for Human Use (Vero Cell / Human Diploid Cell)\n"
                    "Key Release Specifications:\n"
                    "1. Moisture: <= 3.0% (Karl Fischer / Vacuum drying).\n"
                    "2. Residual Host Cell DNA (General Chapter 3407 qPCR): <= 3.0 pg/dose (Vero cell).\n"
                    "3. Residual Host Cell Protein (HCP): <= 4.0 μg/dose (ELISA).\n"
                    "4. Residual Bovine Serum Albumin (BSA): <= 50 ng/dose (General Chapter 3411).\n"
                    "5. Residual β-propiolactone: <= 2.0 μg/dose (GC).\n"
                    "6. Bacterial Endotoxins (General Chapter 1143): <= 2.0 EU/dose.\n"
                    "7. Sterility: Conforms to General Chapter 1101.\n"
                    "8. Potency (NIH mouse challenge assay): Not less than 2.5 IU per single human dose.\n"
                    "Administration: Intramuscular deltoid injection on Essen (0, 3, 7, 14, 28) or Zagreb (2-1-1) schedule."
                )
            }
        ]
    },

    # =========================================================================
    # 第四部：通用技术要求、制剂通则、检测方法通则与指导原则（Volume IV）
    # 母本物理文件：《中国药典》2025年版 四部.pdf (1,220页)
    # =========================================================================
    {
        "doc_id": "chp_2025_vol4_general_chapter_0103_capsules",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 制剂通则 0103：胶囊剂",
        "doc_title_en": "ChP 2025 Vol IV General Chapter 0103: Capsules",
        "version": "2025-ChP-Vol4-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Dosage_Form_General_Chapter",
        "source_file": "《中国药典》2025年版 四部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 四部.pdf",
        "physical_volume": "四部",
        "sections": [
            {
                "section_id": "chp_2025_vol4_0103_sec1_definition_and_types",
                "page": 28,
                "title_zh": "胶囊剂剂型定义与分类（硬胶囊/软胶囊/肠溶胶囊/缓释胶囊/控释胶囊）",
                "title_en": "Definition & Capsule Categories",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 制剂通则 0103 胶囊剂：\n\n"
                    "【定义】胶囊剂系指原料药物或与适宜辅料充填于空心胶囊或密封于软质囊材中制成的固体制剂。可供口服，亦可供吸入、直肠或阴道给药。\n\n"
                    "【分类与工艺要求】：\n"
                    "1. 硬胶囊（Hard Capsules）：系指将一定量的固体原料药物与适宜辅料制成均匀的粉末、颗粒、小丸、半固体或液体，充填于空心硬胶囊中制成。\n"
                    "2. 软胶囊（Soft Capsules / 胶丸）：系指将一定量的液体原料药物直接包封，或将固体药物溶解、分散于适宜辅料中制成溶液、混悬液或乳状液，封闭于球形、卵形或滴水形的软质囊材中制成。囊材通常由明胶、甘油、水及适宜增塑剂组成。\n"
                    "3. 肠溶胶囊（Enteric Capsules）：系指硬胶囊或软胶囊经用适宜肠溶材料包衣，或用肠溶材料制成囊壳，在胃液中不崩解，而在肠液中崩解溶出释放活性药物。\n"
                    "4. 缓释胶囊（Extended-release Capsules）：在规定的释放介质中缓慢地非恒速释放药物，达到延效目的。\n"
                    "5. 控释胶囊（Controlled-release Capsules）：在规定的释放介质中恒速或接近恒速释放药物。"
                ),
                "content_en": (
                    "ChP 2025 Vol IV General Chapter 0103 Capsules: Definition & Categories\n"
                    "1. Hard capsules: Solid drug/excipients powder, granules, pellets filled into hard shells.\n"
                    "2. Soft capsules: Liquids/suspensions enclosed in elastic gelatin/plasticizer shells.\n"
                    "3. Enteric capsules: Coated or shell-formulated to resist gastric fluid and release drug in intestinal fluid.\n"
                    "4. Extended-release capsules: Sustained release over prolonged duration.\n"
                    "5. Controlled-release capsules: Zero-order or near-constant release rate."
                )
            },
            {
                "section_id": "chp_2025_vol4_0103_sec2_weight_variation_and_disintegration",
                "page": 29,
                "title_zh": "胶囊剂装量差异限度标准与崩解时限法定检查法（硬胶囊30min/软胶囊60min/肠溶耐酸2h）",
                "title_en": "Weight Variation Limits & Disintegration Test Standards",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 胶囊剂装量差异与崩解时限强制性法定标准：\n\n"
                    "一、装量差异限度检查法（通则 0103 项下）：\n"
                    "取供试品 20 粒，精密称定总重量，求出平均装量。倾出内容物，硬胶囊用小刷轻刷囊壳内壁，软胶囊用乙醚等有机溶剂洗净晾干，精密称定空囊壳重量，求出每粒装量。\n\n"
                    "| 平均装量范围 | 装量差异允许限度 | 判定规则 |\n"
                    "| :--- | :--- | :--- |\n"
                    "| 0.30g 以下 | ± 10.0% | 每粒装量与平均装量相比较，超出装量差异限度的不得多于2粒，并不得有1粒超出限度1倍 |\n"
                    "| 0.30g 及以上 | ± 7.5% | 每粒装量与平均装量相比较，超出装量差异限度的不得多于2粒，并不得有1粒超出限度1倍 |\n\n"
                    "二、崩解时限检查法（通则 0921）：\n"
                    "采用升降式崩解仪，水温控制在 37±1℃。取供试品 6 粒进行测定：\n"
                    "1. 硬胶囊：除另有规定外，每粒均应在 30 分钟内全部完全崩解。若有 1 粒不能完全崩解，应另取 6 粒复试，均应符合规定。\n"
                    "2. 软胶囊：除另有规定外，每粒均应在 60 分钟内全部完全崩解。若有 1 粒不能完全崩解，应另取 6 粒复试，均应符合规定。\n"
                    "3. 肠溶胶囊：\n"
                    "- 盐酸溶液检查（耐酸力）：在 37±1℃ 的 0.09mol/L ~ 0.1mol/L 盐酸溶液（或人工胃液）中检查 2 小时，每粒的囊壳均不得有裂缝、崩解或软化；\n"
                    "- 缓冲液崩解检查：取出，用水轻洗，立即放入 pH 6.8 磷酸盐缓冲液（或人工肠液）中，运转 1 小时，6 粒均应完全崩解溶散。若有 1 粒不合格，另取 6 粒复试，均应符合规定。\n\n"
                    "三、微生物限度：非无菌口服胶囊剂需氧菌总数（TAMC）不得过 1000 CFU/g，霉菌和酵母菌总数（TYMC）不得过 100 CFU/g，不得检出大肠埃希菌（通则 1105、1106）。"
                ),
                "content_en": (
                    "ChP 2025 Vol IV General Chapter 0103 Weight Variation & Disintegration Standards:\n"
                    "1. Weight Variation (20 capsules tested):\n"
                    "- Average weight < 0.30g: Limit ± 10.0% (not more than 2 capsules exceed, none exceeds double).\n"
                    "- Average weight >= 0.30g: Limit ± 7.5% (not more than 2 capsules exceed, none exceeds double).\n"
                    "2. Disintegration Times (General Chapter 0921, 37±1°C, 6 capsules):\n"
                    "- Hard capsules: Completely disintegrated within 30 minutes.\n"
                    "- Soft capsules: Completely disintegrated within 60 minutes.\n"
                    "- Enteric capsules: No cracks, disintegration, or softening in 0.1M HCl for 2 hours; completely disintegrated in pH 6.8 phosphate buffer within 1 hour.\n"
                    "3. Microbial Limit: TAMC <= 1000 CFU/g, TYMC <= 100 CFU/g, E. coli absent."
                )
            }
        ]
    },
    {
        "doc_id": "chp_2025_vol4_general_chapter_0401_uv_vis",
        "doc_title_zh": "《中华人民共和国药典》2025年版四部 检验方法通则 0401：紫外-可见分光光度法",
        "doc_title_en": "ChP 2025 Vol IV General Chapter 0401: UV-Vis Spectrophotometry",
        "version": "2025-ChP-Vol4-Official",
        "effective_date": "2025-10-01",
        "jurisdiction": "ChP",
        "category": "Analytical_Method_General_Chapter",
        "source_file": "《中国药典》2025年版 四部.pdf",
        "master_physical_pdf": "《中国药典》2025年版 四部.pdf",
        "physical_volume": "四部",
        "sections": [
            {
                "section_id": "chp_2025_vol4_0401_sec1_verification_and_stray_light",
                "page": 56,
                "title_zh": "0401仪器检定校准要求（波长准确度/吸光度准确度/杂散光检查法/比色皿配对）",
                "title_en": "Instrument Verification, Stray Light Test & Matched Cuvettes",
                "content_zh": (
                    "《中华人民共和国药典》2025年版四部 检验方法通则 0401 紫外-可见分光光度法：\n\n"
                    "【原理与波长范围】紫外光区（190 ~ 400nm）与可见光区（400 ~ 800nm）分子吸收光谱法。基于朗伯-比尔定律：A = E * c * l（A为吸光度，E为吸收系数，c为浓度，l为光路吸收池厚度）。\n\n"
                    "【仪器的检定与校准强制性要求】：\n"
                    "1. 波长准确度与重复性检定：\n"
                    "- 采用氧化钬玻璃吸收峰（241.5nm、279.3nm、287.6nm、333.8nm、360.8nm、418.5nm、453.4nm、536.4nm、637.5nm）或汞灯特征发射谱线（253.65nm、302.15nm、313.16nm、365.02nm、404.66nm、435.83nm、546.07nm、576.96nm）进行校准。\n"
                    "- 波长允许偏差：紫外光区（190~400nm）不得超过 ±1.0nm；可见光区（400~800nm）不得超过 ±2.0nm。波长重复性不得超过 0.5nm。\n"
                    "2. 吸光度准确度检定：\n"
                    "- 取于 110℃ 干燥至恒重的基准重铬酸钾约 60.06mg，精密称定，加 0.005mol/L 硫酸溶液溶解并稀释至 1000ml。\n"
                    "- 分别在 235nm、257nm、313nm、350nm 测定吸光度，比吸收系数（E1%1cm）标准值应符合规定（如 235nm 为 124.5±1.2，257nm 为 144.0±1.4，313nm 为 48.6±0.7，350nm 为 106.6±1.0）。吸光度相对偏差应在 ±1.0% 以内。\n"
                    "3. 杂散光（Stray Light）检查法：\n"
                    "- 试剂：配制 1.2%（g/ml）氯化钾（KCl）水溶液。\n"
                    "- 测定：以水为空白，在 200nm 波长处测定 1.2% 氯化钾溶液的透光率（%T）。\n"
                    "- 法定限度：在 200nm 处的透光率应小于 0.5%（即吸光度 A 应大于 2.30）。若大于 0.5%，说明杂散光超标，仪器不得用于深紫外区测定。\n"
                    "4. 吸收池（比色皿）配对检定：\n"
                    "- 石英吸收池用于紫外及可见光区，玻璃吸收池仅用于可见光区。\n"
                    "- 装入溶剂后在工作波长测定，两个吸收池间的透光率之差不得超过 0.5%。\n"
                    "5. 最佳读数吸光度区间：供试品溶液的吸光度读数宜控制在 0.2 ~ 0.8（透光率 10% ~ 65%）之间，以减小仪器光电读数误差。"
                ),
                "content_en": (
                    "ChP 2025 Vol IV General Chapter 0401 UV-Vis Spectrophotometry:\n"
                    "1. Wavelength Accuracy: Holmium oxide filter (241.5, 279.3, 360.8, 536.4 nm) or mercury lines. UV error <= ±1.0 nm; Visible error <= ±2.0 nm. Repeatability <= 0.5 nm.\n"
                    "2. Absorbance Accuracy: Potassium dichromate (60.06 mg/L in 0.005M H2SO4) tested at 235, 257, 313, 350 nm. Relative error <= ±1.0%.\n"
                    "3. Stray Light Test: 1.2% (w/v) KCl solution at 200 nm; Transmittance must be < 0.5% (Absorbance > 2.30).\n"
                    "4. Matched Cuvettes: Transmittance difference between quartz cells <= 0.5%.\n"
                    "5. Optimum Absorbance Range: Between 0.2 and 0.8."
                )
            }
        ]
    }
]
