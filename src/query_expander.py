import re
from typing import List, Dict, Set

class RegulatoryQueryExpander:
    """
    Query Expander for Life Sciences & Medical Regulatory RAG.
    Bridges the vocabulary gap between colloquial user queries and formal statutory language
    using an authoritative medical & regulatory terminology ontology.
    """

    # Domain-specific synonym dictionary bridging colloquial terms to statutory terms
    REGULATORY_SYNONYM_MAP: Dict[str, List[str]] = {
        # Software & AI Medical Devices
        "bug": ["软件缺陷", "遗留缺陷", "残余风险", "software anomaly", "defect"],
        "漏洞": ["网络安全漏洞", "未知漏洞", "CVE", "cybersecurity vulnerability", "SBOM"],
        "网络安全": ["Cybersecurity", "Section 524B", "SBOM", "网络安全漏洞"],
        "医疗器械": ["Medical Device", "Device", "SaMD", "SiMD", "医疗器械软件"],
        "补丁": ["软件更新", "安全补丁", "patching infrastructure", "over-the-air"],
        "换代": ["重大软件变更", "版本变更", "PCCP", "Predetermined Change Control Plan"],
        "升级": ["版本命名规则", "增强型更新", "重大软件变更"],
        "app": ["移动医疗App", "独立软件", "SaMD", "通用计算平台"],
        "人工智能": ["AI算法", "机器学习", "深度学习", "泛化性能", "算法可解释性"],
        "算法": ["核心算法验证", "泛化性能报告", "算法可解释性说明"],

        # Preclinical, Clinical & Animal Studies
        "动物实验": ["非临床安全性评价", "体内试验", "in-vivo toxicity", "生物相容性"],
        "免临床": ["免除临床试验", "免于进行临床试验", "人用经验证据", "基准样品一致性"],
        "不用做临床": ["免除临床试验", "临床评价免于进行临床试验", "人用经验"],
        "临床试验": ["I期临床", "II期临床", "III期临床", "验证性临床试验", "人用经验"],
        "有效性": ["临床疗效", "主治病证", "验证性临床", "生物等效性"],

        # Traditional Chinese Medicine (TCM)
        "中药方子": ["中药复方制剂", "古代经典名方", "人用经验", "处方来源"],
        "老祖宗方子": ["古代经典名方目录", "第3类中药", "传统工艺配制", "人用经验考证"],
        "人用经验": ["真实世界临床数据", "历代医籍考证", "临床经验方", "中医药理论"],

        # Chemical Pharmaceuticals & BE
        "仿制药": ["化学药品仿制药", "质量和疗效一致性评价", "同名同方药", "参比制剂 RLD"],
        "原研药": ["参比制剂", "Reference Listed Drug", "RLD", "标杆制剂"],
        "溶出度": ["多介质体外溶出曲线", "相似因子 f2", "溶出行为等同性"],
        "吸收": ["药代动力学 PK", "血药浓度", "AUC0-t", "峰浓度 Cmax"],
        "等效": ["生物等效性 BE", "几何均值比 90% 置信区间", "80.00%~125.00%"],

        # FDA / International Overview vs Subtopics
        "fda": ["Food and Drug Administration", "FDA Overview", "Mission and Statutory Mandate", "CDRH CDER CBER", "FD&C Act", "机构定位与监管范围"],
        "美国fda": ["Food and Drug Administration", "FDA Overview", "Mission and Statutory Mandate", "CDRH CDER CBER", "FD&C Act", "机构定位与监管范围"],
        "524b": ["FD&C Act Section 524B", "Cybersecurity in Medical Devices", "Cyber Device", "SBOM"],
        "fda 524b": ["FD&C Act Section 524B", "Cybersecurity in Medical Devices", "Cyber Device", "SBOM"],
        "qmsr": ["Quality Management System Regulation", "QMSR", "21 CFR Part 820", "ISO 13485 Harmonization"],
        "fda qmsr": ["Quality Management System Regulation", "QMSR", "21 CFR Part 820", "ISO 13485 Harmonization"],
        "510k": ["510(k) Premarket Notification", "Substantial Equivalence", "Predicate Device", "Class II Device"],
        "510(k)": ["510(k) Premarket Notification", "Substantial Equivalence", "Predicate Device", "Class II Device"],
        "pccp": ["Predetermined Change Control Plan", "PCCP", "Machine Learning Software Changes"],
        "part 11": ["21 CFR Part 11", "Electronic Records", "Electronic Signatures", "Audit Trail", "GxP"],

        # NMPA Overview vs Subtopics
        "nmpa": ["国家药品监督管理局", "NMPA Overview", "机构职责与组织架构", "CDE CMDE", "医疗器械监督管理条例"],
        "国家药监局": ["国家药品监督管理局", "NMPA Overview", "机构职责与组织架构", "CDE CMDE", "医疗器械监督管理条例"],
        "物料清单": ["Software Bill of Materials", "SBOM", "SPDX", "CycloneDX"],
        "黑客": ["网络安全威胁", "524B Cyber Device", "威胁建模", "渗透测试"],
        "iso": ["ISO 13485:2016", "ISO 14971", "QMSR", "21 CFR Part 820"],
        "质量体系": ["QMSR", "Quality Management System", "Design Controls", "21 CFR 820.30"],

        # EU MDR
        "eu mdr": ["Regulation (EU) 2017/745", "EU MDR Overview", "Notified Body", "Annex VIII Rule 11", "CE marking"],
        "欧洲": ["Regulation (EU) 2017/745", "EU MDR Overview", "Notified Body", "Annex VIII Rule 11"],
        "欧盟": ["Regulation (EU) 2017/745", "EU MDR Overview", "Notified Body", "Annex VIII Rule 11"],
        "分类": ["Rule 11", "Class I", "Class IIa", "Class IIb", "Class III", "安全性级别"],

        # ICH & PMDA
        "ich": ["ICH Guidelines", "ICH Harmonization", "Quality Safety Efficacy", "PMDA Japan", "PMD Act"],
        "pmda": ["PMDA Japan", "PMD Act", "Pharmaceuticals and Medical Devices Agency", "MHLW"],

        # Chinese Pharmacopoeia (ChP - 《中华人民共和国药典》)
        "中国药典": ["《中华人民共和国药典》", "ChP", "国家法定药品标准", "药典四部通则", "Chinese Pharmacopoeia"],
        "药典": ["《中华人民共和国药典》", "ChP", "国家法定药品标准", "药典四部通则", "Chinese Pharmacopoeia"],
        "chp": ["Chinese Pharmacopoeia", "《中华人民共和国药典》", "药典通则", "国家药品标准"],
        "usp": ["United States Pharmacopeia", "USP-NF", "USP <71>", "USP <85>", "USP <621>", "USP <711>"],
        "美国药典": ["United States Pharmacopeia", "USP-NF", "USP <71>", "USP <85>", "USP <621>", "USP <711>"],
        "高效液相": ["高效液相色谱法", "HPLC", "通则0512", "系统适用性试验", "理论板数", "分离度", "拖尾因子", "重复性RSD"],
        "hplc": ["高效液相色谱法", "通则0512", "系统适用性", "理论板数", "分离度", "拖尾因子", "重复性RSD"],
        "细菌内毒素": ["细菌内毒素检查法", "通则1143", "鲎试剂 TAL", "最大有效稀释倍数 MVD", "内毒素限值 L=K/M", "凝胶限度试验"],
        "内毒素": ["通则1143", "细菌内毒素检查法", "鲎试剂 TAL", "最大有效稀释倍数 MVD", "凝胶限量试验"],
        "无菌检查": ["无菌检查法", "通则1101", "薄膜过滤法", "硫乙醇酸盐流体培养基 FTM", "胰酪大豆胨液体培养基 TSB", "14天培养"],
        "微生物限度": ["非无菌药品微生物限度检查", "通则1105", "通则1106", "需氧菌总数 TAMC", "霉菌和酵母菌总数 TYMC", "控制菌检查"],
        "稳定性试验": ["通则9014", "ICH Q1A", "影响因素试验", "加速试验 40℃ 75%RH", "长期留样试验 25℃ 60%RH", "显著变化"],
        "崩解时限": ["通则0101", "通则0921", "普通片15分钟", "薄膜衣片30分钟", "肠溶衣片耐酸2小时"],
        "可见异物": ["注射剂通则 0102", "可见异物通则 0904", "灯检法 1000~1500lx", "不溶性微粒 0903", "光阻法"],
        "不溶性微粒": ["通则0903", "光阻法", "注射剂微粒", "10微米 6000粒", "25微米 600粒", "大容量输液 25粒/ml"],
        "农药残留": ["中国药典一部", "33种禁用农药残留", "通则2341", "甲拌磷", "水胺硫磷", "氧化乐果"],
        "33种农残": ["中国药典一部", "33种禁用农药残留", "通则2341", "高毒农药", "GC-MS/MS LC-MS/MS"],
        "重金属限量": ["中国药典一部", "通则2321", "ICP-MS", "铅 镉 砷 汞 铜", "Pb Cd As Hg Cu", "ICH Q3D"],
        "黄曲霉毒素": ["通则2351", "黄曲霉毒素 B1 5ug/kg", "真菌毒素", "中药饮片安全标准"],
        "陈皮": ["《中华人民共和国药典》2025年版一部 品种正文 陈皮", "广陈皮", "Citri Reticulatae Pericarpium", "橙皮苷", "川陈皮素", "橘皮素", "理气健脾", "燥湿化痰"],
        "广陈皮": ["《中华人民共和国药典》2025年版一部 品种正文 陈皮", "广陈皮", "Citri Reticulatae Pericarpium", "川陈皮素", "橘皮素", "橙皮苷"],
        "当归": ["《中华人民共和国药典》2025年版一部 品种正文 当归", "Angelicae Sinensis Radix", "阿魏酸", "酒当归", "补血活血", "调经止痛", "润肠通便"],
        "茯苓": ["《中华人民共和国药典》2025年版一部 品种正文 茯苓", "Poria", "茯苓酸", "茯苓个", "茯苓块", "茯苓片", "利水渗湿", "健脾宁心"],
        "凌霄花": ["《中华人民共和国药典》2025年版一部 品种正文 凌霄花", "Campsis Flos", "洋丁香酚苷", "毛蕊花糖苷", "清热凉血", "散瘀消癥"],
        "阿司匹林": ["《中华人民共和国药典》2025年版二部 品种正文 阿司匹林", "Aspirin", "乙酰水杨酸", "游离水杨酸", "阿司匹林肠溶片", "非甾体抗炎药"],
        "乙酰水杨酸": ["《中华人民共和国药典》2025年版二部 品种正文 阿司匹林", "Aspirin", "阿司匹林", "游离水杨酸"],
        "甲硝唑": ["《中华人民共和国药典》2025年版二部 品种正文 甲硝唑", "Metronidazole", "2-甲基-5-硝基咪唑", "甲硝唑有关物质", "灭滴灵"],
        "奥美拉唑": ["《中华人民共和国药典》2025年版二部 品种正文 奥美拉唑", "Omeprazole", "奥美拉唑肠溶胶囊", "耐酸力", "释放度", "洛赛克"],
        "纯化水": ["《中华人民共和国药典》2025年版二部 品种正文 纯化水", "Aqua Purificata", "电导率表", "25℃ 5.1uS/cm", "总有机碳TOC 0.50mg/L", "微生物限度100CFU/ml"],
        "纯化水电导率": ["《中华人民共和国药典》2025年版二部 品种正文 纯化水", "纯化水电导率法定限度表", "0~100℃电导率", "25℃ 5.1uS/cm", "阶段1阶段2阶段3"],
        "狂犬疫苗": ["《中华人民共和国药典》2025年版三部 品种正文 冻干人用狂犬病疫苗", "Rabies Vaccine", "Vero细胞", "NIH小鼠效价", "2.5IU", "宿主DNA残留"],
        "狂犬病疫苗": ["《中华人民共和国药典》2025年版三部 品种正文 冻干人用狂犬病疫苗", "Rabies Vaccine", "Vero细胞", "NIH小鼠效价", "2.5IU", "宿主DNA残留"],
        "胶囊剂": ["《中华人民共和国药典》2025年版四部 制剂通则 0103 胶囊剂", "通则0103", "硬胶囊30分钟", "软胶囊60分钟", "肠溶胶囊耐酸2小时", "装量差异"],
        "0103": ["《中华人民共和国药典》2025年版四部 制剂通则 0103 胶囊剂", "胶囊剂通则", "通则0103", "崩解时限", "装量差异"],
        "胶囊剂通则": ["《中华人民共和国药典》2025年版四部 制剂通则 0103 胶囊剂", "通则0103", "硬胶囊30分钟", "软胶囊60分钟", "肠溶胶囊耐酸2小时", "装量差异"],
        "紫外分光光度法": ["《中华人民共和国药典》2025年版四部 检验方法通则 0401 紫外-可见分光光度法", "通则0401", "波长检定", "氧化钬", "吸光度重铬酸钾", "杂散光1.2%氯化钾"],
        "0401": ["《中华人民共和国药典》2025年版四部 检验方法通则 0401 紫外-可见分光光度法", "通则0401", "波长准确度", "氧化钬", "重铬酸钾", "杂散光"],
        "对乙酰氨基酚": ["《中华人民共和国药典》2025年版二部 品种正文 对乙酰氨基酚", "扑热息痛", "Paracetamol", "Acetaminophen", "对氨基酚"],
        "扑热息痛": ["《中华人民共和国药典》2025年版二部 品种正文 对乙酰氨基酚", "对乙酰氨基酚", "Paracetamol", "对氨基酚"],
        "布洛芬": ["《中华人民共和国药典》2025年版二部 品种正文 布洛芬", "Ibuprofen", "非甾体抗炎药", "NSAID"],
        "二甲双胍": ["《中华人民共和国药典》2025年版二部 品种正文 盐酸二甲双胍", "盐酸二甲双胍", "Metformin", "双氰胺", "降糖药"],
        "盐酸二甲双胍": ["《中华人民共和国药典》2025年版二部 品种正文 盐酸二甲双胍", "Metformin", "双氰胺", "溶出度"],
        "阿莫西林": ["《中华人民共和国药典》2025年版二部 品种正文 阿莫西林", "Amoxicillin", "聚合物", "高分子杂质", "青霉素"],
        "阿托伐他汀": ["《中华人民共和国药典》2025年版二部 品种正文 阿托伐他汀钙", "Atorvastatin", "阿托伐他汀钙", "他汀", "对映异构体"],
        "人参": ["《中华人民共和国药典》2025年版一部 品种正文 人参", "Ginseng", "人参皂苷", "Rg1", "Re", "Rb1"],
        "黄连": ["《中华人民共和国药典》2025年版一部 品种正文 黄连", "Coptis", "小檗碱", "盐酸小檗碱", "味连", "雅连", "云连"],
        "甘草": ["《中华人民共和国药典》2025年版一部 品种正文 甘草", "Glycyrrhiza", "甘草酸", "甘草苷"],
        "安宫牛黄丸": ["《中华人民共和国药典》2025年版一部 品种正文 安宫牛黄丸", "牛黄", "麝香", "黄芩苷", "栀子苷"],
        "人血白蛋白": ["《中华人民共和国药典》2025年版三部 品种正文 人血白蛋白", "Human Albumin", "白蛋白", "多聚体", "铝残留量"],
        "胰岛素": ["《中华人民共和国药典》2025年版三部 品种正文 重组人胰岛素", "Recombinant Human Insulin", "重组人胰岛素", "高分子蛋白"],
        "重组人胰岛素": ["《中华人民共和国药典》2025年版三部 品种正文 重组人胰岛素", "Insulin", "重组人胰岛素", "效价"],
        "曲妥珠单抗": ["《中华人民共和国药典》2025年版三部 品种正文 注射用曲妥珠单抗", "Trastuzumab", "赫赛汀", "HER2", "单克隆抗体"],
        "片剂通则": ["《中华人民共和国药典》2025年版四部 通则0101 片剂", "通则0101", "崩解时限15分钟", "脆碎度1.0%", "含量均匀度"],
        "注射剂通则": ["《中华人民共和国药典》2025年版四部 通则0102 注射剂", "通则0102", "可见异物0904", "不溶性微粒0903", "无菌检查"],
        "药材检定通则": ["《中华人民共和国药典》2025年版四部与一部 通则0212 药材和饮片检定通则", "通则0212", "33种农残", "水分灰分"],
        "冬虫夏草": ["《中华人民共和国药典》2025年版一部 品种正文 冬虫夏草", "Cordyceps", "腺苷", "33种禁用农残", "重金属"],
        "板蓝根": ["《中华人民共和国药典》2025年版一部 品种正文 板蓝根", "Isatidis Radix", "告依春", "水分灰分浸出物"],
        "大黄": ["《中华人民共和国药典》2025年版一部 品种正文 大黄", "Rhei Radix", "总蒽醌", "芦荟大黄素", "大黄酸", "大黄素"],
        "地西泮": ["《中华人民共和国药典》2025年版二部 品种正文 地西泮", "Diazepam", "2-甲氨基-5-氯二苯甲酮", "安定"],
        "头孢克肟": ["《中华人民共和国药典》2025年版二部 品种正文 头孢克肟", "Cefixime", "聚合物", "有关物质"],
        "乙肝疫苗": ["《中华人民共和国药典》2025年版三部 品种正文 重组乙型肝炎疫苗", "Hepatitis B Vaccine", "CHO细胞", "外源性DNA"],
        "微晶纤维素": ["《中华人民共和国药典》2025年版四部 药用辅料正文 微晶纤维素", "MCC", "Microcrystalline Cellulose", "pH", "水溶物", "干燥失重"],


        # China GMP & Data Integrity
        "gmp": ["药品生产质量管理规范", "China GMP", "附录1 无菌药品", "洁净度 A级 B级 C级 D级", "计算机化系统附录", "ALCOA+"],
        "洁净区": ["GMP 附录1 无菌药品", "A级 B级 C级 D级", "悬浮粒子 0.5微米 3520", "沉降菌 浮游菌", "无菌保证水平 SAL 10^-6"],
        "悬浮粒子": ["GMP 附录1 无菌药品", "悬浮粒子标准表", "A级 3520", "B级静态 3520 动态 352000", "0.5微米 5.0微米"],
        "无菌保证水平": ["无菌保证水平 SAL 10^-6", "最终灭菌 F0值", "标准湿热灭菌 121℃ 15分钟", "GMP 附录1"],
        "sal": ["无菌保证水平 SAL 10^-6", "最终灭菌 F0值", "GMP 附录1 无菌药品"],
        "数据完整性": ["数据完整性 ALCOA+", "计算机化系统附录", "系统审计追踪 Audit Trail", "永久开启不可篡改", "GAMP 5"],
        "alcoa": ["ALCOA+", "可追溯 可读 即时 原始 准确 完整 一致 持久 可获取", "数据完整性", "GMP 计算机化系统"],
        "审计追踪": ["系统审计追踪 Audit Trail", "不可关闭 不可修改 不可删除", "GMP 计算机化系统附录", "数据完整性"],
        "audit trail": ["系统审计追踪 Audit Trail", "不可关闭 不可修改 不可删除", "GMP 计算机化系统附录", "数据完整性"],

        # Drug Registration & Expedited Pathways
        "药品注册管理办法": ["国家市场监督管理总局令第27号", "MAH制度", "化学药中药生物制品1-5类", "突破性治疗 附条件批准 优先审评 特别审批"],
        "mah": ["药品上市许可持有人 MAH", "药品管理法", "药品注册管理办法第27号令", "全生命周期质量主体责任"],
        "突破性治疗": ["突破性治疗药物程序", "药品注册管理办法第27号令", "加快审评通道", "重大疾病重大临床获益"],
        "优先审评": ["优先审评审批程序", "130个工作日", "药品注册管理办法第27号令", "罕见病 儿童用药"],

        # FDA cGMP & OOS
        "cgmp": ["FDA 21 CFR Part 211", "Current Good Manufacturing Practice", "Quality Control Unit § 211.22", "OOS Investigation"],
        "21 cfr 211": ["FDA 21 CFR Part 211", "Finished Pharmaceuticals cGMP", "§ 211.68 Automated Equipment", "§ 211.165 Testing"],
        "oos": ["Out-of-Specification", "超标结果调查", "FDA OOS Guidance", "Phase I 实验室调查", "Phase II 生产根因调查"],

        # Good Clinical Practice (GCP)
        "gcp": ["药物临床试验质量管理规范", "GCP 2020年第57号公告", "主要研究者 PI", "知情同意书 ICF", "伦理委员会 IRB", "监查员 CRA", "SAE", "SUSAR"],
        "知情同意": ["知情同意书 ICF", "法定代理人", "充分告知", "受试者自主决定", "GCP 规范", "弱势群体保护"],
        "伦理委员会": ["伦理委员会 IRB", "IEC", "受试者保护", "跟踪审查", "年度审查", "独立委员"],
        "irb": ["伦理委员会 IRB", "Institutional Review Board", "IEC", "审查批准", "受试者保护"],
        "sae": ["严重不良事件 SAE", "24小时报告", "致死或危及生命", "SUSAR", "GCP 第五章", "住院或功能丧失"],
        "严重不良事件": ["严重不良事件 SAE", "24小时报告", "住院或延长住院", "残疾", "SUSAR", "主要研究者报告"],
        "susar": ["可疑且非预期严重不良反应 SUSAR", "7天快速报告", "15天安全报告", "致死或危及生命", "CDE", "年度安全性报告 DSUR"],
        "cra": ["临床监查员 CRA", "基于风险的监查", "原始数据核查 SDV", "监查报告", "申办者质量管理"],
        "tmf": ["试验主文档 TMF", "Trial Master File", "档案保存期限", "上市后至少5年"],

        # Good Laboratory Practice (GLP)
        "glp": ["药物非临床研究质量管理规范", "GLP", "专题负责人 SD", "质量保证部门 QAU", "毒理学试验", "档案保存10年"],
        "非临床": ["非临床安全性评价", "GLP", "专题负责人 SD", "毒代动力学 TK", "急性毒性", "长期毒性"],
        "sd": ["专题负责人 SD", "Study Director", "GLP 法定职责", "试验方案", "总结报告"],
        "qau": ["质量保证部门 QAU", "Quality Assurance Unit", "质量保证声明 QA Statement", "GLP 独立监督"],
        "毒理试验": ["单次给药毒性", "重复给药毒性", "遗传毒性标准电池", "安全药理学", "生殖毒性", "NOAEL"],
        "ames": ["Ames试验", "细菌回复突变试验", "遗传毒性标准电池", "鼠伤寒沙门氏菌", "ICH S2(R1)"],
        "遗传毒性": ["遗传毒性标准电池试验", "Ames试验", "染色体畸变", "体内微核试验", "ICH S2(R1)"],

        # Analytical Method Validation (ICH Q2 / ChP)
        "方法验证": ["ICH Q2(R2)", "分析方法验证指导原则", "特异度", "专属性", "线性", "准确度", "精密度", "LOD", "LOQ", "耐用性"],
        "ich q2": ["ICH Q2(R2)", "分析方法验证指导原则", "特异度", "线性 r>=0.999", "加标回收率", "精密度", "LOD", "LOQ"],
        "专属性": ["专属性 Specificity", "特异度", "分离度 R>=1.5", "二极管阵列 DAD 峰纯度", "ICH Q2"],
        "线性": ["线性范围 Linearity", "相关系数 r>=0.999", "R^2>=0.998", "残差正态分布", "ICH Q2"],
        "回收率": ["准确度 Accuracy", "加标回收率", "3个浓度水平各3份", "98.0%~102.0%", "ICH Q2"],
        "精密度": ["精密度 Precision", "重复性 Repeatability RSD<=1.0%", "中间精密度", "重现性", "ICH Q2"],
        "lod": ["检测下限 LOD", "信噪比 S/N>=3:1", "3.3 sigma / S", "ICH Q2"],
        "loq": ["定量下限 LOQ", "信噪比 S/N>=10:1", "10 sigma / S", "精密度 RSD<=10%", "ICH Q2"],
        "耐用性": ["耐用性 Robustness", "流动相 pH+-0.2", "柱温+-5℃", "流速+-10%", "ICH Q2"],

        # ChP General Chapters (0941, 0401, 0861)
        "含量均匀度": ["中国药典通则 0941", "含量均匀度检查法", "A + 1.80S <= 15.0", "初试10片", "复试20片", "小剂量制剂<25mg"],
        "0941": ["中国药典通则 0941", "含量均匀度检查法", "A + 1.80S <= 15.0", "初试10片", "复试20片"],
        "a+1.80s": ["通则 0941 含量均匀度判定公式", "A + 1.80S <= 15.0", "复试 A + 1.45S <= 15.0"],
        "紫外分光光度法": ["中国药典通则 0401", "紫外-可见分光光度法", "波长检定 氧化钬", "吸光度最佳区间 0.2~0.8", "比吸收系数"],
        "0401": ["中国药典通则 0401", "紫外-可见分光光度法", "波长检定 氧化钬", "吸光度最佳区间 0.2~0.8", "杂散光"],
        "氧化钬": ["氧化钬玻璃滤光片", "通则 0401", "波长校正 241.15nm 287.15nm 361.5nm", "允许误差 +-1nm"],
        "比吸收系数": ["比吸收系数 E(1%, 1cm)", "通则 0401", "重铬酸钾硫酸溶液", "允许误差 +-0.5%"],
        "残留溶剂": ["中国药典通则 0861", "ICH Q3C", "顶空气相色谱 HS-GC", "一类溶剂 苯 2ppm", "二类溶剂 乙腈 410ppm", "三类溶剂 5000ppm"],
        "0861": ["中国药典通则 0861", "残留溶剂测定法", "顶空气相色谱 HS-GC", "一类二类三类溶剂限度"],
        "一类溶剂": ["第一类溶剂 Class 1", "苯 2ppm", "四氯化碳 4ppm", "1,2-二氯乙烷 5ppm", "应当避免使用"],
        "二类溶剂": ["第二类溶剂 Class 2", "限制使用", "乙腈 410ppm", "甲醇 3000ppm", "二氯甲烷 600ppm", "PDE"],
        "顶空气相": ["顶空气相色谱法 HS-GC", "通则 0861", "平衡温度 80℃", "毛细管柱 DB-624", "FID检测器"],

        # Biologics & Monoclonal Antibodies
        "单抗": ["重组单克隆抗体", "SEC-HPLC 聚集体 HMWS<=1.0%", "单体纯度>=95.0%", "宿主细胞蛋白 HCP<=50ng/mg", "残余DNA<=10pg/剂"],
        "单克隆抗体": ["重组单克隆抗体", "中国药典三部", "SEC-HPLC 聚集体", "电荷异构体 iCIEF", "HCP ELISA", "残余 DNA"],
        "sec-hplc": ["分子排阻色谱 SEC-HPLC", "单抗聚集体 HMWS", "单体纯度 Monomer >=95%", "碎片 LMWS"],
        "聚集体": ["单抗聚集体 HMWS", "分子排阻色谱 SEC-HPLC", "限度 <=1.0%~2.0%", "免疫原性风险"],
        "hcp": ["宿主细胞蛋白 HCP", "Host Cell Protein", "ELISA 双抗体夹心法", "限度 <=50ng/mg 或 100ppm"],
        "宿主细胞蛋白": ["宿主细胞蛋白 HCP", "Host Cell Protein", "ELISA 双抗体夹心法", "限度 <=50ng/mg 或 100ppm"],
        "残余dna": ["宿主细胞残余 DNA resDNA", "qPCR 定量", "限度 <=100pg/剂 或 <=10pg/剂", "片段<200bp"],

        # FDA IND & NDA (Part 312 / 314)
        "ind": ["FDA 21 CFR Part 312", "Investigational New Drug", "Form FDA 1571", "Form FDA 1572", "30天审评时钟", "Clinical Hold"],
        "nda": ["FDA 21 CFR Part 314", "New Drug Application", "CTD 模块 1-5", "Form FDA 356h", "PDUFA 10个月/6个月"],
        "clinical hold": ["临床试验暂停 Clinical Hold", "21 CFR § 312.42", "受试者重大安全风险", "30天答辩复审期"],
        "1571": ["Form FDA 1571", "IND 申请表单", "申办者法律承诺", "21 CFR § 312.23"],
        "1572": ["Form FDA 1572", "Statement of Investigator", "主要研究者资质与承诺", "GCP 声明"],

        # Pharmaceutical Water Systems (ChP Vol II & Vol IV)
        "纯化水": ["中国药典二部 纯化水", "通则0261 制药用水", "电导率标准表", "总有机碳 TOC 0.50mg/L", "易氧化物", "微生物限度 100 CFU/ml", "酸碱度 pH", "硝酸盐 0.06ppm", "亚硝酸盐 0.02ppm", "氨 0.3ppm", "不挥发物 1mg", "重金属 0.5ppm"],
        "纯净水": ["纯化水", "中国药典二部 纯化水", "通则0261 制药用水", "电导率", "总有机碳 TOC", "微生物限度 100 CFU/ml"],
        "纯净水要求": ["纯化水法定标准", "中国药典二部 纯化水", "通则0261 制药用水", "电导率标准", "总有机碳 TOC", "微生物限度 100 CFU/ml", "酸碱度"],
        "注射用水": ["中国药典二部 注射用水", "WFI", "蒸馏法", "细菌内毒素 0.25 EU/ml", "微生物限度 10 CFU/100ml", "纯化水全检指标"],
        "灭菌注射用水": ["中国药典二部 灭菌注射用水", "通则1101 无菌检查 14天", "细菌内毒素 0.25 EU/ml", "通则0903 不溶性微粒"],
        "制药用水": ["通则0261 制药用水", "饮用水", "纯化水", "注射用水", "灭菌注射用水", "316L 不锈钢", "3D 盲管规则", "70度循环保温", "工艺用水选择矩阵表"],
        "氯化钠注射液": ["0.9% 氯化钠注射液", "生理盐水", "标示量 95.0%~105.0%", "pH 4.5~7.0", "渗透压 260~320 mOsmol/kg", "内毒素 0.50 EU/ml"],
        "葡萄糖注射液": ["葡萄糖注射液", "pH 3.2~5.5", "5-羟甲基糠醛 5-HMF 吸光度 0.32", "细菌内毒素 0.25 EU/ml", "旋光度法"]
    }

    def __init__(self):
        pass

    def clean_conversational_query(self, query: str) -> str:
        """Strips conversational noise and prefixes from natural Chinese/English questions."""
        # Step 0: Professional Term Masking and unspaced English segmentation
        from src.term_masker import ProfessionalTermMasker
        segmented, _ = ProfessionalTermMasker().mask_and_segment_unspaced_query(query)

        # Step 1: Chinese conversational prefix/suffix stripping
        cleaned = re.sub(
            r"^(我想(了解|知道|问|请教)?|请问(一下)?|帮我(查查|看看|找找)?|能否告诉我|有没有关于|我想看|你有什么|有哪些|什么是|介绍一下|介绍|请介绍)(关于)?",
            "",
            segmented,
            flags=re.IGNORECASE
        ).strip()
        cleaned = re.sub(
            r"(主要内容|主要背景|相关内容|有关内容|具体内容|相关法规|有哪些法规|有哪些规定|相关规定|的相关信息|的相关规定|的法规|的资料|的信息|有哪些|是什么|内容|法规|规定)[\?？!！]*$",
            "",
            cleaned,
            flags=re.IGNORECASE
        ).strip()
        # Step 2: English conversational prefix/suffix stripping
        cleaned = re.sub(
            r"^(i\s+(wanna|want\s+to)?\s*(know|learn|understand|see)?|please\s+(tell\s+me|help\s+me)?|what\s+(is|are)?|tell\s+me\s+about|show\s+me|introduce)\s*(about)?\s*",
            "",
            cleaned,
            flags=re.IGNORECASE
        ).strip()
        cleaned = re.sub(
            r"\s*(main\s+context|core\s+context|context|knowledge|regulations?|rules?|guidelines?|info|information|details?)[\?!\.]*$",
            "",
            cleaned,
            flags=re.IGNORECASE
        ).strip()

        # Step 3: Normalize colloquial synonyms to official statutory terms
        colloquial_normalizations = {
            "纯净水要求": "纯化水",
            "纯净水": "纯化水",
            "中药方子": "中药复方制剂",
            "老祖宗留下来的": "古代经典名方",
            "老祖宗方子": "古代经典名方",
            "老祖宗": "古代经典名方",
            "免临床": "免除临床试验",
            "不用做临床": "免除临床试验",
            "bug": "软件已知缺陷",
            "漏洞": "网络安全漏洞",
            "物料清单": "软件物料清单 SBOM",
            "动物实验": "非临床安全性评价",
            "生理盐水": "氯化钠注射液",
            "盐水": "氯化钠注射液",
            "糖水": "葡萄糖注射液"
        }
        for colloquial, statutory in colloquial_normalizations.items():
            if colloquial in cleaned:
                cleaned = cleaned.replace(colloquial, statutory)

        return cleaned.strip() if cleaned.strip() else query

    def normalize_query_for_rerank(self, query: str) -> str:
        """
        Normalizes conversational noise and converts colloquial terminology into statutory equivalents
        to ensure precise scoring during the reranking phase.
        """
        cleaned = self.clean_conversational_query(query)
        cleaned_lower = cleaned.lower()

        # Direct agency definitional shortcuts
        if cleaned_lower in ("fda", "food and drug administration", "美国fda", "u.s. fda"):
            return "U.S. FDA Mission Regulatory Authority Review Centers CDRH CDER CBER FD&C Act"
        if cleaned_lower in ("nmpa", "国家药监局", "国家药品监督管理局"):
            return "国家药品监督管理局 NMPA 机构职责 审评中心 CDE CMDE 医疗器械监督管理条例"
        if cleaned_lower in ("eu mdr", "eumdr", "欧洲医疗器械法规", "欧盟mdr"):
            return "EU MDR Regulation 2017/745 Notified Body Competent Authority CE marking"
        if cleaned_lower in ("ich", "国际人用药品注册技术协调会"):
            return "ICH Guidelines Quality Safety Efficacy PMDA PMD Act"
        if cleaned_lower in ("chp", "中国药典", "药典", "中华人民共和国药典", "chinese pharmacopoeia"):
            return "《中华人民共和国药典》2025年版 ChP 国家法定药品标准 2025年10月1日施行 通则0261 9209微生物控制 纯化水 注射用水"
        # Substance Monographs & Specific Preparations (Prioritized over generic test methods)
        if any(w in cleaned_lower for w in ["纯化水", "纯净水"]):
            return "中国药典2025年版二部 品种正文 纯化水 酸碱度 pH 5.0-7.0 硝酸盐 0.06ppm 亚硝酸盐 0.02ppm 氨 0.3ppm 电导率 25℃ 5.1 总有机碳 TOC 0.50mg/L 易氧化物 不挥发物 1mg 重金属 0.5ppm 微生物限度 100 CFU/ml"
        if any(w in cleaned_lower for w in ["注射用水", "wfi"]):
            return "中国药典2025年版二部 品种正文 注射用水 WFI 纯化水蒸馏 膜法反渗透超滤等效技术 细菌内毒素 0.25 EU/ml 微生物限度 10 CFU/100ml"
        if any(w in cleaned_lower for w in ["灭菌注射用水"]):
            return "中国药典2025年版二部 品种正文 灭菌注射用水 通则1101 无菌检查 14天 细菌内毒素 0.25 EU/ml 通则0903 不溶性微粒 10微米 25微米"
        if any(w in cleaned_lower for w in ["制药用水", "0261"]):
            return "中国药典2025年版四部 通则0261 制药用水通则 饮用水 纯化水 注射用水 灭菌注射用水 膜过滤制备注射用水 316L 不锈钢 3D 盲管规则 70度循环保温 在线灭菌"
        if any(w in cleaned_lower for w in ["9209", "水微生物", "制药用水微生物"]):
            return "中国药典2025年版四部 指导原则9209 制药用水微生物监测和控制指导原则 警戒限度 Alert 纠偏限度 Action 取样点设计 POU 生物膜 Biofilm 假单胞菌"
        if any(w in cleaned_lower for w in ["医疗器械软件", "独立软件", "samd", "软件指导原则"]):
            return "国家药监局 医疗器械软件注册审查指导原则 2022年第9号通告 软件安全性级别 轻微 中等 严重 COTS SOUP 重大软件更新判定 软件研究报告"
        if any(w in cleaned_lower for w in ["医疗器械网络安全", "网络安全原则", "网络安全能力", "22项"]):
            return "国家药监局 医疗器械网络安全注册审查指导原则 2022年第7号通告 22项网络安全能力 自动注销 访问控制 审计追踪 软件物料清单 SBOM 漏洞生命周期管理"
        if any(w in cleaned_lower for w in ["fda 网络安全", "fda cybersecurity", "524b"]):
            return "FDA Premarket Cybersecurity Guidance 2023 FD&C Act Section 524B Cyber Device Threat Modeling SBOM CBOM CVD Vulnerability Management"
        if any(w in cleaned_lower for w in ["fda 软件", "software functions", "basic documentation", "enhanced documentation"]):
            return "FDA Content of Premarket Submissions for Device Software Functions 2023 Basic Documentation Enhanced Documentation Architecture SRS SDS Traceability Analysis"
        if any(w in cleaned_lower for w in ["qmsr", "fda 820", "21 cfr 820", "iso 13485"]):
            return "FDA Quality Management System Regulation QMSR Final Rule 21 CFR Part 820 ISO 13485:2016 2026年2月2日生效 Design Controls Risk Management ISO 14971"
        if any(w in cleaned_lower for w in ["rule 11", "mdr 软件", "eu mdr software", "mdcg 2019"]):
            return "EU MDR Regulation 2017/745 Annex VIII Rule 11 MDCG 2019-11 MDSW Class I Class IIa Class IIb Class III Notified Body"
        if any(w in cleaned_lower for w in ["q9", "质量风险管理", "formality", "主观性"]):
            return "ICH Q9(R1) Quality Risk Management 2023 Formality in QRM Addressing Subjectivity Risk-Based Decision Making FMEA"
        if any(w in cleaned_lower for w in ["当归", "酒当归", "阿魏酸"]):
            return "中国药典2025年版一部 品种正文 当归 Angelicae Sinensis Radix 阿魏酸 0.050% 挥发油 酒当归 补血活血 调经止痛 润肠通便"
        if any(w in cleaned_lower for w in ["茯苓", "茯苓酸", "茯苓个", "茯苓块", "茯苓片"]):
            return "中国药典2025年版一部 品种正文 茯苓 Poria 茯苓酸 0.050% 茯苓个 茯苓块 茯苓片 利水渗湿 健脾 宁心"
        if any(w in cleaned_lower for w in ["凌霄花", "洋丁香酚苷"]):
            return "中国药典2025年版一部 品种正文 凌霄花 Campsis Flos 洋丁香酚苷 0.15% 清热凉血 散瘀消癥"
        if any(w in cleaned_lower for w in ["甲硝唑", "灭滴灵", "2-甲基-5-硝基咪唑"]):
            return "中国药典2025年版二部 品种正文 甲硝唑 Metronidazole 2-甲基-5-硝基咪唑 杂质0.1% 总杂质0.5% 含量测定 99.0%"
        if any(w in cleaned_lower for w in ["奥美拉唑", "洛赛克", "奥美拉唑肠溶"]):
            return "中国药典2025年版二部 品种正文 奥美拉唑 Omeprazole 奥美拉唑肠溶胶囊 耐酸力 10% 缓冲液释放度 75% 篮法"
        if any(w in cleaned_lower for w in ["狂犬疫苗", "狂犬病疫苗", "人用狂犬病疫苗"]):
            return "中国药典2025年版三部 品种正文 冻干人用狂犬病疫苗 Rabies Vaccine Vero细胞 宿主DNA残留 3.0pg NIH效价 2.5IU"
        if any(w in cleaned_lower for w in ["胶囊剂", "0103", "硬胶囊", "软胶囊", "肠溶胶囊"]):
            return "中国药典2025年版四部 制剂通则0103 胶囊剂 硬胶囊30分钟 软胶囊60分钟 肠溶胶囊耐酸2小时 装量差异"
        if any(w in cleaned_lower for w in ["纯化水", "纯化水电导率", "制药用水纯化水"]):
            return "中国药典2025年版二部 品种正文 纯化水 Aqua Purificata 电导率表 0~100℃ 25℃ 5.1uS/cm 总有机碳TOC 0.50mg/L 微生物限度 100CFU/ml"
        if any(w in cleaned_lower for w in ["紫外分光光度法", "0401", "紫外可见", "氧化钬", "比吸收系数"]):
            return "中国药典2025年版四部 检验方法通则0401 紫外-可见分光光度法 波长检定 氧化钬 吸光度重铬酸钾 杂散光1.2%氯化钾透光率 0.5% 最佳读数区间 0.2~0.8"
        if any(w in cleaned_lower for w in ["陈皮", "广陈皮"]):
            return "中国药典2025年版一部 品种正文 陈皮 广陈皮 橙皮苷 3.5% 川陈皮素 橘皮素 0.42% 33种农残 水分 灰分 理气健脾 燥湿化痰"
        if any(w in cleaned_lower for w in ["阿司匹林", "aspirin", "乙酰水杨酸"]):
            return "中国药典2025年版二部 品种正文 阿司匹林 乙酰水杨酸 游离水杨酸 0.1% 熔点 135-140 阿司匹林肠溶片 释放度 耐酸 缓冲液"
        if any(w in cleaned_lower for w in ["对乙酰氨基酚", "扑热息痛", "paracetamol", "acetaminophen"]):
            return "中国药典2025年版二部 品种正文 对乙酰氨基酚 扑热息痛 对氨基酚 0.005% 熔点 168-172 解热镇痛"
        if any(w in cleaned_lower for w in ["布洛芬", "ibuprofen"]):
            return "中国药典2025年版二部 品种正文 布洛芬 熔点 75-78 有关物质 杂质 0.1% 非甾体抗炎药"
        if any(w in cleaned_lower for w in ["氯化钠注射液", "生理盐水"]):
            return "中国药典二部 氯化钠注射液 0.9% 标示量 95.0%~105.0% pH 4.5~7.0 渗透压 0.9~1.1 细菌内毒素 0.50 EU/ml 无菌"
        if any(w in cleaned_lower for w in ["葡萄糖注射液"]):
            return "中国药典二部 葡萄糖注射液 5% 标示量 95.0%~105.0% 细菌内毒素 0.25 EU/ml 无菌"



        # General Chapters & Analytical Methods
        if any(w in cleaned_lower for w in ["高效液相", "hplc"]):
            return "中国药典 通则0512 高效液相色谱法 HPLC 系统适用性 理论板数 分离度 拖尾因子 重复性"
        if any(w in cleaned_lower for w in ["细菌内毒素", "内毒素", "鲎试剂", "mvd"]):
            return "中国药典 通则1143 细菌内毒素检查法 鲎试剂 TAL 最大有效稀释倍数 MVD 凝胶限度试验"
        if any(w in cleaned_lower for w in ["无菌检查", "无菌试验"]):
            return "中国药典 通则1101 无菌检查法 薄膜过滤法 硫乙醇酸盐流体培养基 FTM 14天培养"
        if any(w in cleaned_lower for w in ["微生物限度", "tamc", "tymc"]):
            return "中国药典 通则1105 通则1106 非无菌药品微生物限度检查 TAMC TYMC 控制菌 大肠埃希菌"
        if any(w in cleaned_lower for w in ["洁净区", "悬浮粒子", "gmp无菌"]):
            return "药品生产质量管理规范 China GMP 附录1 无菌药品 A级 B级 C级 D级 悬浮粒子标准 SAL"
        if any(w in cleaned_lower for w in ["数据完整性", "alcoa", "审计追踪"]):
            return "药品生产质量管理规范 计算机化系统附录 数据完整性 ALCOA+ 系统审计追踪 Audit Trail"
        if any(w in cleaned_lower for w in ["33种农残", "农残", "重金属限量"]):
            return "中国药典一部 中药材及饮片 33种禁用农药残留 通则2341 重金属及有害元素限度 铅镉砷汞铜 通则2321"
        if any(w in cleaned_lower for w in ["gcp", "临床试验质量管理", "知情同意", "irb", "伦理委员会", "sae", "susar", "cra"]):
            return "国家药监局 国家卫健委 2020年第57号公告 GCP 伦理委员会 IRB 主要研究者 PI 知情同意书 ICF 监查员 CRA SAE 24小时 SUSAR 7天"
        if any(w in cleaned_lower for w in ["glp", "非临床研究", "专题负责人", "qau", "毒理试验", "ames", "遗传毒性"]):
            return "国家药品监督管理局 GLP 药物非临床研究质量管理规范 专题负责人 SD 质量保证部门 QAU 毒理学试验 遗传毒性 Ames 档案保存10年"
        if any(w in cleaned_lower for w in ["方法验证", "ich q2", "分析方法验证", "专属性", "线性", "回收率", "精密度", "lod", "loq", "耐用性"]):
            return "ICH Q2(R2) 分析方法验证指导原则 特异度 专属性 线性 r>=0.999 准确度 回收率 精密度 重复性 RSD LOD LOQ 耐用性"
        if any(w in cleaned_lower for w in ["含量均匀度", "0941", "a+1.80s", "均匀度"]):
            return "中国药典 通则0941 含量均匀度检查法 A + 1.80S <= 15.0 初试10片 复试20片 小剂量制剂"
        if any(w in cleaned_lower for w in ["紫外分光光度法", "0401", "紫外", "氧化钬", "比吸收系数"]):
            return "中国药典 通则0401 紫外-可见分光光度法 波长检定 氧化钬 吸光度准确度 重铬酸钾 最佳读数区间 0.2~0.8"
        if any(w in cleaned_lower for w in ["残留溶剂", "0861", "顶空气相", "一类溶剂", "二类溶剂", "三类溶剂"]):
            return "中国药典 通则0861 残留溶剂测定法 ICH Q3C 一类溶剂 苯 2ppm 二类溶剂 乙腈 410ppm 三类溶剂 5000ppm 顶空气相色谱 HS-GC"
        if any(w in cleaned_lower for w in ["ind", "fda 312", "clinical hold", "1571", "1572"]):
            return "FDA 21 CFR Part 312 IND Form 1571 Form 1572 30天审评时钟 7-Day Alert Clinical Hold"
        if any(w in cleaned_lower for w in ["nda", "fda 314", "pdufa"]):
            return "FDA 21 CFR Part 314 NDA Form 356h CTD Module 1-5 PDUFA 审评周期"

        colloquial_normalizations = {
            "纯净水要求": "纯化水",
            "纯净水": "纯化水",
            "中药方子": "中药复方制剂",
            "老祖宗留下来的": "古代经典名方",
            "老祖宗方子": "古代经典名方",
            "老祖宗": "古代经典名方",
            "免临床": "免除临床试验",
            "不用做临床": "免除临床试验",
            "bug": "软件已知缺陷",
            "漏洞": "网络安全漏洞",
            "物料清单": "软件物料清单 SBOM",
            "动物实验": "非临床安全性评价"
        }
        for colloquial, statutory in colloquial_normalizations.items():
            if colloquial in cleaned:
                cleaned = cleaned.replace(colloquial, statutory)
        return cleaned

    def expand_query(self, query: str) -> List[str]:
        """
        Expands the user query into multiple search variants:
        1. Original query
        2. Cleaned core query (without conversational noise)
        3. Enriched query with injected formal statutory synonyms
        4. Focused keywords variant
        """
        core_query = self.clean_conversational_query(query)
        query_lower = query.lower()
        core_lower = core_query.lower()

        # Check for specific FDA/NMPA subtopics to avoid diluting specific searches with generic agency overviews
        has_fda_subtopic = any(k in query_lower for k in ["524b", "cyber", "qmsr", "820", "510k", "510(k)", "pccp", "part 11", "ind", "nda", "312", "314"])
        has_nmpa_subtopic = any(k in query_lower for k in ["软件", "ai", "人工智能", "中药", "be", "仿制药", "gcp", "glp", "739", "严重级别", "知情同意", "sae", "susar"])

        matched_synonyms: Set[str] = set()

        for colloquial_key, formal_syns in self.REGULATORY_SYNONYM_MAP.items():
            # Skip generic agency overview injection if a specific subtopic is being queried
            if colloquial_key in ("fda", "美国fda") and has_fda_subtopic:
                continue
            if colloquial_key in ("nmpa", "国家药监局") and has_nmpa_subtopic:
                continue

            if colloquial_key in query_lower or colloquial_key in core_lower:
                matched_synonyms.update(formal_syns)

        variants = [query]
        if core_query != query:
            variants.append(core_query)

        if matched_synonyms:
            top_syns = list(matched_synonyms)[:4]
            enriched = f"{core_query} {' '.join(top_syns)}"
            variants.append(enriched)
            variants.append(" ".join(top_syns))

        return list(dict.fromkeys(variants))

    def expand_query_conservative(self, query: str):
        """Wrapper delegating to ConservativeQueryExpander."""
        return ConservativeQueryExpander.expand_query(query)


class ConservativeQueryExpander:
    """
    Principled, generalized pharmaceutical query expander.
    Maps colloquial expressions, general chapter abbreviations, and common pharmaceutical
    aliases to formal statutory headings and general chapter codes.
    Strictly avoids hardcoded drug-specific numerical limits or unverified threshold values.
    """
    CONSERVATIVE_RULES = [
        ("RULE-01-MOISTURE", r"里面能含有多少水分|能含多少水|水分限度|水分要求", "【检查】 水分 通则0832"),
        ("RULE-02-IMPURITY", r"杂质比例不能超过多少|杂质不能超过多少|杂质限量|杂质限度", "【检查】 杂质 通则2301"),
        ("RULE-03-STORAGE", r"平常应该怎么存放|怎么存放|怎么保存|储藏条件|保存条件|保存要求", "【贮藏】 密封 干燥 避光"),
        ("RULE-04-HPLC-COND", r"流动相比例|流动相是什么|色谱条件", "高效液相色谱法 通则0512 色谱条件"),
        ("RULE-05-TOTAL-ASH", r"总灰分限度|总灰分要求", "【检查】 总灰分 通则2302"),
        ("RULE-06-DRYING-LOSS", r"烘干减重|减重不得过|干燥失重", "【检查】 干燥失重 通则0831"),
        ("RULE-07-STERILITY", r"无菌检查|无菌检测", "【检查】 无菌 通则1101"),
        ("RULE-08-PURITY", r"主峰纯度|主峰相对百分含量|纯度要求", "【检查】 峰面积归一化 主峰"),
        ("RULE-09-ICP-MS", r"ICP-MS|等离子体质谱", "通则0412 电感耦合等离子体质谱法"),
        ("RULE-10-NMR", r"NMR|核磁共振波谱|核磁共振", "通则0441 核磁共振波谱法"),
        ("RULE-11-ELISA", r"ELISA|酶联免疫", "通则3429 酶联免疫吸附法"),
        ("RULE-12-RAMAN", r"激光拉曼", "拉曼光谱 通则0400"),
        ("RULE-13-NIR", r"近红外光|近红外光谱", "通则0403 近红外光谱法 漫反射模式"),
        ("RULE-14-ASPIRIN", r"乙酰水杨酸", "阿司匹林 Aspirin"),
        ("RULE-15-ASPARAGINASE", r"门冬酰胺酶针剂", "注射用门冬酰胺酶"),
        ("RULE-16-DT-VACCINE", r"白破二联|白破疫苗", "吸附白喉破伤风联合疫苗"),
        ("RULE-17-JE-VACCINE", r"乙脑活疫苗", "乙型脑炎减毒活疫苗 中和试验"),
        ("RULE-18-SUPPOSITORY", r"直肠栓剂.*阴道栓剂|栓剂.*外形", "通则0108 栓剂 直肠栓 阴道栓 鱼雷形 鸭嘴形")
    ]

    @classmethod
    def expand_query(cls, query: str):
        """
        Applies conservative terminology expansion rules.
        Returns:
            expanded_search_query: str (original query + appended terms, or original query if no match)
            added_terms: List[str] (list of added phrase strings)
            telemetry: List[Dict[str, str]] (list of matched rule metadata records)
        """
        added_terms = []
        telemetry = []
        for rule_id, pattern, expansion in cls.CONSERVATIVE_RULES:
            if re.search(pattern, query):
                added_terms.append(expansion)
                telemetry.append({
                    "rule_id": rule_id,
                    "pattern": pattern,
                    "added_terms": expansion
                })

        if added_terms:
            expanded_search_query = query + " " + " ".join(added_terms)
        else:
            expanded_search_query = query

        return expanded_search_query, added_terms, telemetry
