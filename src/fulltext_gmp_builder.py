"""
Authentic Full-Text Document Builder for China GMP & Regulatory Provisions
Covers:
1. China GMP (2010 Revision) Annex 1: Sterile Medicinal Products (无菌药品附录完整规程)
2. China GMP Annex on Computerized Systems & Data Integrity (计算机化系统与数据完整性ALCOA+)
3. SAMR Order No. 27: Provisions for Drug Registration (药品注册管理办法总局令第27号)
"""

def get_gmp_and_regulatory_fulltext_documents():
    docs = []

    # =========================================================================
    # 1. China GMP (2010 Revision) Annex 1: Sterile Medicinal Products
    # =========================================================================
    docs.append({
        "doc_id": "china_gmp_annex1_sterile",
        "doc_title": "《药品生产质量管理规范》（GMP 2010年修订版）附录1：无菌药品",
        "doc_title_zh": "《药品生产质量管理规范》（GMP 2010年修订版）附录1：无菌药品",
        "doc_title_en": "China GMP (2010 Revision) Annex 1: Sterile Medicinal Products",
        "jurisdiction": "GMP",
        "source_file": "china_gmp_2010_annex1_sterile_products_full.md",
        "version": "2010-China-GMP-Official",
        "sections": [
            {
                "section_id": "gmp_sterile_sec1_cleanroom_classes",
                "section_title": "附录1 第一章：洁净级别划分与空气悬浮粒子法定标准表",
                "section_title_en": "Chapter 1: Cleanroom Grades & Airborne Particle Standards",
                "pages": [1],
                "content_zh": (
                    "《药品生产质量管理规范》（2010年修订版）附录1：无菌药品\n\n"
                    "第八条：洁净区级别划分与技术定义：\n"
                    "无菌药品生产的洁净区划分为四个级别：\n"
                    "- A级：高风险操作区，如灌装区、放置胶塞桶和敞口安瓿的区域以及无菌装配或连接操作的区域。通常采用单向流操作台（罩）维持该区的环境状态。单向流系统在其工作区域必须均匀送风，风速应为 0.36 ~ 0.54 m/s（指导值）。\n"
                    "- B级：指无菌配制和无菌灌装等 A 级洁净区所处的背景区域。\n"
                    "- C级和D级：指无菌药品生产过程中重要程度较低操作步骤的洁净区。\n\n"
                    "第九条：各洁净级别空气悬浮粒子的标准规定如下表：\n\n"
                    "| 洁净度级别 | 静态 >= 0.5 μm | 静态 >= 5.0 μm | 动态 >= 0.5 μm | 动态 >= 5.0 μm |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| A级 | <= 3,520 个/m³ | <= 20 个/m³ | <= 3,520 个/m³ | <= 20 个/m³ |\n"
                    "| B级 | <= 3,520 个/m³ | <= 29 个/m³ | <= 352,000 个/m³ | <= 2,900 个/m³ |\n"
                    "| C级 | <= 352,000 个/m³ | <= 2,900 个/m³ | <= 3,520,000 个/m³ | <= 29,000 个/m³ |\n"
                    "| D级 | <= 3,520,000 个/m³ | <= 29,000 个/m³ | 不作事先规定 | 不作事先规定 |\n\n"
                    "注：静态系指所有生产设备均已安装就绪，生产人员不在场状态；动态系指生产设备按预定工艺运行，生产人员按规程操作状态。"
                ),
                "content_en": (
                    "China GMP (2010 Revision) Annex 1: Sterile Medicinal Products\n\n"
                    "Article 8: Cleanroom Grade Classifications:\n"
                    "- Grade A: High-risk zone for aseptic operations (filling, stopper bowl, open ampoules). Unidirectional airflow velocity maintained at 0.36 ~ 0.54 m/s.\n"
                    "- Grade B: Background environment surrounding Grade A aseptic preparation and filling areas.\n"
                    "- Grade C & D: Clean areas for less critical steps (e.g. preparation of solutions prior to terminal sterilization).\n\n"
                    "Article 9: Maximum Permitted Airborne Particle Concentrations:\n\n"
                    "| Grade | At Rest (>=0.5 um) | At Rest (>=5.0 um) | In Operation (>=0.5 um) | In Operation (>=5.0 um) |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| Grade A | <= 3,520 / m3 | <= 20 / m3 | <= 3,520 / m3 | <= 20 / m3 |\n"
                    "| Grade B | <= 3,520 / m3 | <= 29 / m3 | <= 352,000 / m3 | <= 2,900 / m3 |\n"
                    "| Grade C | <= 352,000 / m3 | <= 2,900 / m3 | <= 3,520,000 / m3 | <= 29,000 / m3 |\n"
                    "| Grade D | <= 3,520,000 / m3 | <= 29,000 / m3 | Not predetermined | Not predetermined |\n\n"
                    "Note: 'At rest' condition: facility fully equipped, no personnel. 'In operation': normal production with operating personnel."
                )
            },
            {
                "section_id": "gmp_sterile_sec2_microbial_sal",
                "section_title": "附录1 第二章：微生物动态监测限度与灭菌保证水平（SAL / F0）",
                "section_title_en": "Chapter 2: Microbial Limits & Sterility Assurance Level (SAL / F0)",
                "pages": [2],
                "content_zh": (
                    "《药品生产质量管理规范》（2010年修订版）附录1：无菌药品\n\n"
                    "第十一条：洁净区微生物动态监测法定限度表（平均值）：\n\n"
                    "| 级别 | 浮游菌 (CFU/m³) | 沉降菌 Φ90mm, 4小时 (CFU/皿) | 表面接触碟 Φ55mm (CFU/碟) | 5指手套印点 (CFU/手套) |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| A级 | < 1 | < 1 | < 1 | < 1 |\n"
                    "| B级 | 10 | 5 | 5 | 5 |\n"
                    "| C级 | 100 | 50 | 25 | - |\n"
                    "| D级 | 200 | 100 | 50 | - |\n\n"
                    "注：表中各数值均为平均值。单个沉降碟或印点出现菌落即应进行调查。\n\n"
                    "第六十三条：无菌保证水平与灭菌工艺验证要求：\n"
                    "1. 无菌保证水平（Sterility Assurance Level, SAL）：\n"
                    "任何最终灭菌药品的灭菌工艺，必须使产品中微生物存活的概率不得高于百万分之一，即 SAL <= 10^-6。\n"
                    "2. 湿热灭菌 F0 值计算与控制：\n"
                    "- 标准湿热灭菌法要求在 121℃ 灭菌 15 分钟，其标准 F0 值必须 >= 8 分钟（过度杀灭法要求 F0 >= 12 分钟）；\n"
                    "- 灭菌过程必须使用双探头温度传感器，并监控灭菌腔体内最冷点温度与压力；\n"
                    "- 干热灭菌去热原工艺：通常采用 250℃ 处理不少于 45 分钟，保证热原去除率降低至少 3 个对数级（3-log reduction）。"
                ),
                "content_en": (
                    "China GMP (2010 Revision) Annex 1: Sterile Medicinal Products\n\n"
                    "Article 11: Recommended Limits for Microbial Contamination (In Operation):\n\n"
                    "| Grade | Air Sample (CFU/m3) | Settle Plates (90mm, 4h, CFU/plate) | Contact Plates (55mm, CFU/plate) | Glove Print (5 fingers, CFU/glove) |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| Grade A | < 1 | < 1 | < 1 | < 1 |\n"
                    "| Grade B | 10 | 5 | 5 | 5 |\n"
                    "| Grade C | 100 | 50 | 25 | - |\n"
                    "| Grade D | 200 | 100 | 50 | - |\n\n"
                    "Article 63: Sterilization Assurance Level (SAL) & F0 Validation:\n"
                    "1. Sterility Assurance Level (SAL):\n"
                    "The theoretical probability of finding a non-sterile unit following terminal sterilization must not exceed 1 in 1 million (SAL <= 10^-6).\n"
                    "2. F0 Parameter Validation:\n"
                    "- Terminal moist heat sterilization at 121°C requires F0 >= 8 minutes (overkill sterilization requires F0 >= 12 minutes).\n"
                    "- Depyrogenation tunnel: Dry heat at 250°C for not less than 45 minutes achieving >= 3-log reduction in endotoxin challenge."
                )
            }
        ]
    })

    # =========================================================================
    # 2. China GMP Annex on Computerized Systems & Data Integrity
    # =========================================================================
    docs.append({
        "doc_id": "china_gmp_computerized_systems",
        "doc_title": "《药品生产质量管理规范》计算机化系统附录与国家药监局数据完整性指导原则",
        "doc_title_zh": "《药品生产质量管理规范》计算机化系统附录与国家药监局数据完整性指导原则",
        "doc_title_en": "China GMP Annex on Computerized Systems & NMPA Data Integrity Guidelines",
        "jurisdiction": "GMP",
        "source_file": "china_gmp_computerized_systems_data_integrity_full.md",
        "version": "2015-Annex-Official",
        "sections": [
            {
                "section_id": "gmp_comp_sec1_alcoa",
                "section_title": "计算机化系统附录：数据完整性 ALCOA+ 原则与生命周期验证（GAMP 5）",
                "section_title_en": "Data Integrity ALCOA+ Principles & GAMP 5 Lifecycle Validation",
                "pages": [1],
                "content_zh": (
                    "《药品生产质量管理规范》计算机化系统附录与药品数据完整性指导原则\n\n"
                    "1. 国际通行数据完整性 ALCOA+ 原则法定解析：\n"
                    "- Attributable（可追溯性/可归属性）：所有电子数据的生成、修改、删除必须能确切归属至具体执行人员。系统严禁共用公用账号，每个操作人必须持有独立的唯一账号和密码；\n"
                    "- Legible（清晰易读性）：数据在法定保存期限内（药品有效期加一年且不少于五年）必须清晰可读，且所有历史修订痕迹必须可读；\n"
                    "- Contemporaneous（同步即时性）：记录必须在操作发生时同步生成并由系统自动记录可信时间戳，严禁事后补录或倒签日期；\n"
                    "- Original（原始性）：必须保存系统生成的第一手原始电子记录（含原始元数据 Metadata，如色谱原始积分线、峰高、光谱文件），不得仅保存打印版纸质报告；\n"
                    "- Accurate（准确性）：数据必须如实反映实际检验或生产操作，无未经批准的人工干预、测试至合格或丢弃不良数据行为；\n"
                    "- Complete（完整性）：包含完整元数据、审计追踪和重测记录；\n"
                    "- Consistent（一致性）：时间序列与工艺步序保持严格逻辑一致；\n"
                    "- Enduring（持久性）：存储在经过验证的抗磁、防灾存储介质中；\n"
                    "- Available（可获取性）：在药监部门现场检查时必须能随时调阅和导出。\n\n"
                    "2. 计算机化系统生命周期验证（GAMP 5）：\n"
                    "系统上线前必须完成用户需求规范（URS）、功能规范（FS）、安装确认（IQ）、运行确认（OQ）及性能确认（PQ），定期执行灾难恢复与备份恢复演练。"
                ),
                "content_en": (
                    "China GMP Annex on Computerized Systems & Data Integrity\n\n"
                    "1. Statutory ALCOA+ Principles:\n"
                    "- Attributable: Traceable to the individual who created, recorded, or modified it via unique personal credentials.\n"
                    "- Legible: Permanently readable throughout the required retention period (shelf life + 1 year, not less than 5 years).\n"
                    "- Contemporaneous: Recorded synchronously at the real time of execution with verified system timestamps.\n"
                    "- Original: Primary raw electronic data including full metadata (chromatographic integration parameters, spectra).\n"
                    "- Accurate: Truthful representation of reality, free from unauthorized manual edits or trial injections.\n"
                    "- Complete, Consistent, Enduring, Available.\n\n"
                    "2. GAMP 5 Lifecycle Validation:\n"
                    "Validation must span URS, FS, IQ, OQ, and PQ, with periodic backup recovery drills."
                )
            },
            {
                "section_id": "gmp_comp_sec2_audit_trail",
                "section_title": "计算机化系统附录：系统审计追踪（Audit Trail）强制规则与QA复核程序",
                "section_title_en": "Mandatory Audit Trail Regulations & QA Review Procedures",
                "pages": [2],
                "content_zh": (
                    "《药品生产质量管理规范》计算机化系统附录\n\n"
                    "第十七条：系统审计追踪（Audit Trail）法定强制规则：\n"
                    "1. 审计追踪自动记录机制：\n"
                    "计算机化系统必须具备独立且受保护的自动审计追踪功能。审计追踪必须如实记录每次操作的日期、时间（精确至秒）、操作人员唯一身份、操作类型（新建、修改、删除）、修改前旧值、修改后新值以及强制输入的操作原因。\n\n"
                    "2. 严禁篡改与关闭审计追踪：\n"
                    "【法定绝对应对红线】：**系统的审计追踪功能必须处于永久开启状态！系统内任何用户（包括 IT 部门最高管理员、仪器超级管理员 Administrator）均绝对没有权限关闭、暂停、修改、重命名或删除审计追踪日志！** 任何删除或修改审计追踪日志的行为均构成重大虚假记录，将依法吊销药品生产许可证！\n\n"
                    "3. 质量管理部门（QA）批放行审计追踪复核规程：\n"
                    "- 在每批药品放行出厂前，质量保证部（QA）专职审核员必须对该批次药品生产与检验全生命周期涉及的审计追踪记录进行全面复核；\n"
                    "- 重点审查项目：色谱积分基线修改（手动积分 Manual Integration）、异常测试中止、样品重测原因、删除的临时进样记录、称量重量修改、设备报警重置等；\n"
                    "- 复核完成后，QA 必须签署专门的《批生产与检验审计追踪复核报告》并归入批记录档案备查。"
                ),
                "content_en": (
                    "China GMP Annex on Computerized Systems\n\n"
                    "Article 17: Mandatory Audit Trail Rules & QA Batch Review:\n"
                    "1. Automatic Audit Trail Tracking:\n"
                    "Computerized systems must feature an automated, secure, time-stamped audit trail capturing date, time, operator ID, action type, old value, new value, and stated justification for change.\n\n"
                    "2. Absolute Prohibition Against Disabling/Altering Audit Trails:\n"
                    "[STATUTORY RED LINE]: The audit trail MUST REMAIN PERMANENTLY ENABLED. NO USER (including IT System Administrators) shall possess privileges to disable, pause, edit, rename, or delete audit trail files.\n\n"
                    "3. QA Review Before Batch Release:\n"
                    "QA must review critical audit trails (manual integration changes, re-injections, aborted runs, weight edits) prior to releasing each batch."
                )
            }
        ]
    })

    # =========================================================================
    # 3. SAMR Order No. 27: Provisions for Drug Registration (药品注册管理办法)
    # =========================================================================
    docs.append({
        "doc_id": "samr_order_27_drug_registration",
        "doc_title": "国家市场监督管理总局令第27号《药品注册管理办法》",
        "doc_title_zh": "国家市场监督管理总局令第27号《药品注册管理办法》",
        "doc_title_en": "SAMR Order No. 27 Provisions for Drug Registration",
        "jurisdiction": "NMPA",
        "source_file": "nmpa_samr_order_27_drug_registration_full.md",
        "version": "SAMR-Order-27-Official",
        "sections": [
            {
                "section_id": "order27_sec1_mah_classification",
                "section_title": "《药品注册管理办法》：MAH 法定主体责任与化学药/中药1~5类注册分类",
                "section_title_en": "MAH Statutory Obligations & Chemical/TCM Class 1-5 Classifications",
                "pages": [1],
                "content_zh": (
                    "国家市场监督管理总局令第27号《药品注册管理办法》（2020年最新版）\n\n"
                    "第一章 总则与药品上市许可持有人（MAH）制度：\n"
                    "第六条：药品上市许可持有人（MAH）依法对药品的非临床安全性研究、临床试验、生产制造、经营销售、上市后安全性监测及药品不良反应监测（ADR）和缺陷产品召回承担全生命周期的法律主体责任。\n\n"
                    "第二章 药品注册分类法定标准：\n"
                    "1. 化学药品注册分类：\n"
                    "- 1类：境内外均未上市的创新药（全新化学结构实体，新靶点/新作用机制）；\n"
                    "- 2类：境内外均未上市的改良型新药（具有明显临床优势的新盐型、新晶型、新剂型、新给药途径、新复方制剂或新适应症）；\n"
                    "- 3类：仿制境外上市但境内未上市原研药品的制剂；\n"
                    "- 4类：仿制境内已上市原研药品的制剂（严格要求生物等效性 BE 试验与参比制剂 RLD 具有质量与疗效一致性）；\n"
                    "- 5类：境外已上市药品申请在境内上市（5.1类境外上市原研药申请进口，5.2类境外上市仿制药申请进口）。\n\n"
                    "2. 中药注册分类：\n"
                    "- 1类：中药创新药；\n"
                    "- 2类：中药改良型新药；\n"
                    "- 3类：古代经典名方中药复方制剂（符合国家名方目录与人用经验考证者，依法免于进行临床试验）；\n"
                    "- 4类：同名同方药。"
                ),
                "content_en": (
                    "SAMR Order No. 27: Provisions for Drug Registration\n\n"
                    "Chapter 1: Marketing Authorization Holder (MAH) System:\n"
                    "Article 6: The MAH holds complete life-cycle legal accountability for non-clinical studies, clinical trials, commercial manufacturing, post-market surveillance, adverse drug reaction (ADR) reporting, and product recall.\n\n"
                    "Chapter 2: Drug Registration Classification:\n"
                    "1. Chemical Drugs:\n"
                    "- Class 1: Innovative drugs not marketed globally (New Chemical Entity NCE).\n"
                    "- Class 2: Improved new drugs (novel salt form, crystal, dosage form, delivery route, or indication with significant clinical superiority).\n"
                    "- Class 3: Generic drugs based on innovative drugs marketed overseas but unapproved in China.\n"
                    "- Class 4: Generic drugs based on originator reference drugs approved in China (BE mandatory).\n"
                    "- Class 5: Imported drug applications for drugs approved overseas.\n\n"
                    "2. Traditional Chinese Medicine (TCM):\n"
                    "- Class 1: Innovative TCM.\n"
                    "- Class 2: Improved new TCM.\n"
                    "- Class 3: Classical famous TCM prescriptions (exempt from clinical trials based on historical human experience data).\n"
                    "- Class 4: Same-name same-formula TCM."
                )
            },
            {
                "section_id": "order27_sec2_expedited_pathways",
                "section_title": "《药品注册管理办法》：四条加快上市审评审批通道法定程序",
                "section_title_en": "Four Expedited Review Pathways for Drug Approvals",
                "pages": [2],
                "content_zh": (
                    "国家市场监督管理总局令第27号《药品注册管理办法》\n\n"
                    "第四章 药品加快上市注册程序（四条法定快速审评通道）：\n\n"
                    "1. 突破性治疗药物程序（Breakthrough Therapy Designation）：\n"
                    "- 申请阶段：通常在 I、II 期临床试验阶段申请；\n"
                    "- 适用条件：针对危及生命或严重影响生存质量的重大疾病，临床初步证据显示疗效明显优于现有治疗手段的新药；\n"
                    "- 扶持政策：药审中心（CDE）指派专门审评团队进行一对一沟通指导，优先安排临床试验方案沟通与滚动审评。\n\n"
                    "2. 附条件批准程序（Conditional Approval）：\n"
                    "- 适用条件：针对治疗严重危及生命且尚无有效治疗手段的疾病、利用替代终点指标可合理预测临床获益的急需新药，或应对突发公共卫生事件急需药品；\n"
                    "- 后续监管：申请人必须在药品上市后规定时限内完成确证性临床试验，提交全套长期安全性与疗效数据。\n\n"
                    "3. 优先审评审批程序（Priority Review）：\n"
                    "- 适用条件：临床急需且具有明显临床价值的儿童用药、罕见病用药（孤儿药）、重大传染病防治药、纳入突破性治疗程序的药品；\n"
                    "- 【法定审评时限】：**将审评工作时限直接大幅压缩至 130 个工作日！**（罕见病药品甚至可缩短至 70 个工作日）。\n\n"
                    "4. 特别审批程序（Special Approval）：\n"
                    "- 适用条件：在国家发生重大公共卫生突发事件时快速启动，统一指挥、早期介入、随到随审、快速检验。"
                ),
                "content_en": (
                    "SAMR Order No. 27: Four Expedited Review Pathways\n\n"
                    "1. Breakthrough Therapy Designation:\n"
                    "- Applied during Phase I/II clinical trials for drugs treating life-threatening diseases demonstrating substantial clinical superiority over existing treatments. CDE assigns dedicated team for rolling review.\n\n"
                    "2. Conditional Approval:\n"
                    "- For drugs treating life-threatening diseases where surrogate endpoints reasonably predict clinical benefit. Confirmatory post-market clinical trials are legally mandatory within stipulated timelines.\n\n"
                    "3. Priority Review:\n"
                    "- For pediatric drugs, rare disease orphan drugs, and critical public health vacancies. Statutory review timeline compressed to 130 working days (or 70 working days for urgent rare diseases).\n\n"
                    "4. Special Approval:\n"
                    "- Deployed during national public health emergencies for expedited unified review and clearance."
                )
            }
        ]
    })

    return docs
