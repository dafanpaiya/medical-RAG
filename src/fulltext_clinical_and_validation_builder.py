"""
Authentic Full-Text Document Builder for Clinical Trials (GCP), Laboratory Studies (GLP),
Analytical Method Validation (ICH Q2), and Quality Specifications (ChP 0941, 0401, 0861, Biologics, FDA Part 312/314).

Covers:
1. NMPA & NHC Notice [2020] No. 57: Good Clinical Practice (GCP 全文核心规程)
2. NMPA Good Laboratory Practice (GLP 药物非临床研究质量管理规范全文)
3. ICH Q2(R2) Validation of Analytical Procedures (分析方法验证最新法定指导原则)
4. ChP 2020 Vol IV General Chapter 0941: Uniformity of Dosage Units (通则 0941 含量均匀度检查法)
5. ChP 2020 Vol IV General Chapter 0401: Ultraviolet-Visible Spectrophotometry (通则 0401 紫外-可见分光光度法)
6. ChP 2020 Vol IV General Chapter 0861: Residual Solvents Determination (通则 0861 残留溶剂测定法 & ICH Q3C)
7. ChP 2020 Vol III & ICH Q6B: Monoclonal Antibodies & Biologics Quality Standards (重组单抗与生物制品质量控制规范)
8. FDA 21 CFR Part 312 (IND) & Part 314 (NDA): Clinical Investigations & Marketing Approvals
"""

def get_clinical_and_validation_fulltext_documents():
    docs = []

    # =========================================================================
    # 1. NMPA & NHC Notice [2020] No. 57: Good Clinical Practice (GCP)
    # =========================================================================
    docs.append({
        "doc_id": "nmpa_nhc_gcp_2020",
        "doc_title": "国家药监局 国家卫生健康委《药物临床试验质量管理规范》（2020年第57号公告）",
        "doc_title_zh": "国家药监局 国家卫生健康委《药物临床试验质量管理规范》（2020年第57号公告）",
        "doc_title_en": "NMPA & NHC Good Clinical Practice for Drugs (GCP, Notice No. 57 of 2020)",
        "jurisdiction": "NMPA",
        "source_file": "nmpa_nhc_gcp_2020_official_full.md",
        "version": "2020-GCP-No.57-Official",
        "sections": [
            {
                "section_id": "gcp_sec1_irb_ethics",
                "section_title": "第二章：伦理委员会（IRB/IEC）组成、审查职责与法定审查原则",
                "section_title_en": "Chapter 2: Institutional Review Board (IRB) Composition & Review Mandate",
                "pages": [1],
                "content_zh": (
                    "国家药品监督管理局 国家卫生健康委员会 2020年第57号公告《药物临床试验质量管理规范》（GCP）\n\n"
                    "第十一条 至 第十五条：伦理委员会的组成与审查职责：\n"
                    "1. 伦理委员会的设立与组成：伦理委员会的职责是保护受试者的权益和安全，应当由医学、药学及其他专业人员、非医药专业人员组成，且至少应有一名非本机构的独立委员，至少由5名及以上委员组成，并推举主任委员。\n"
                    "2. 审查与批准原则：临床试验必须在获得伦理委员会正式书面审查批准后方可开展。伦理委员会应当重点审查：\n"
                    "   - 研究者的资格、经验以及是否有充分的时间和资源开展临床试验；\n"
                    "   - 试验方案是否充分考虑了科学性、伦理合理性，受试者的风险是否最小化且与预期获益相比具有合理性；\n"
                    "   - 知情同意书及向受试者提供的其他文字材料是否通俗易懂，符合伦理原则；\n"
                    "   - 受试者招募方式是否公平、合规，是否存在不当诱导或强迫；\n"
                    "   - 对弱势群体受试者（如儿童、重症患者、认知障碍者等）是否有特殊的保护措施；\n"
                    "3. 跟踪审查：伦理委员会应当对正在实施的临床试验进行跟踪审查，审查频率至少每年一次；任何对试验方案的修改均须经伦理委员会批准后方可执行（紧急规避安全风险除外）。"
                ),
                "content_en": (
                    "NMPA & NHC Notice No. 57 (2020) Good Clinical Practice (GCP)\n\n"
                    "Articles 11 to 15: Institutional Review Board (IRB / IEC) Governance:\n"
                    "1. Composition: The IRB protects the rights, safety, and well-being of trial subjects. It must consist of at least 5 members, including medical/scientific professionals, at least one non-scientific member, and at least one independent member unaffiliated with the trial institution.\n"
                    "2. Mandatory Review Mandate: No clinical trial may commence prior to written unconditional IRB approval. Core review criteria include:\n"
                    "   - Investigator qualifications, clinical expertise, and resource adequacy;\n"
                    "   - Trial protocol scientific validity and ethical justification; subject risk-benefit ratio minimization;\n"
                    "   - Informed Consent Form (ICF) readability, completeness, and non-coercive framing;\n"
                    "   - Subject recruitment advertisements and compensation plans;\n"
                    "   - Protective safeguards for vulnerable populations (pediatrics, unconscious, mentally incapacitated subjects).\n"
                    "3. Continuing Review: The IRB must perform continuing review of ongoing trials at intervals appropriate to risk, at least once annually."
                )
            },
            {
                "section_id": "gcp_sec2_investigator_icf",
                "section_title": "第三章：研究者职责与知情同意书（ICF）法定签署流程与弱势受试者保护",
                "section_title_en": "Chapter 3: Investigator Duties & Informed Consent Process (ICF)",
                "pages": [2],
                "content_zh": (
                    "国家药品监督管理局 国家卫生健康委员会 2020年第57号公告《药物临床试验质量管理规范》（GCP）\n\n"
                    "第十六条 至 第二十四条：主要研究者（PI）与知情同意法定规程：\n"
                    "1. 主要研究者资格与职责：主要研究者应当具备在医疗机构合法执业的医师资格，具备临床试验所需的专业知识、培训经历及良好资信。PI全面负责临床试验在该中心的现场实施，确保遵守试验方案及GCP规范。\n"
                    "2. 知情同意书签署法定规程：\n"
                    "   - 任何受试者入组前，必须由受试者或其法定代理人亲自签署并由执行知情同意的研究者共同签署知情同意书，签署双方必须亲笔书写姓名并签署签署日期（年、月、日、时、分）；\n"
                    "   - 知情同意过程应当充分告知试验性质、目的、可能的获益与已知及潜在的风险、备选治疗方案、受试者的权利（包括随时无条件退出试验且不影响常规诊疗的权利）；\n"
                    "   - 严禁对受试者采用任何诱导、强迫或不正当影响手段；\n"
                    "3. 特殊受试者法定监护人签署规程：\n"
                    "   - 对于无行为能力或限制民事行为能力的受试者（如儿童、昏迷或重度精神障碍患者），必须由其法定代理人签署书面知情同意书；若儿童具备一定认知与表达能力，还应当同时获得儿童本人的知情同意或表示同意（Assent）；\n"
                    "   - 若在紧急抢救情况下无法在入组前获得知情同意，必须符合试验方案预设的紧急知情规程并在方案中获得伦理委员会特别批准，一旦受试者恢复知情能力或法定代理人到达，必须立即补充补办知情同意手续。"
                ),
                "content_en": (
                    "NMPA & NHC Notice No. 57 (2020) Good Clinical Practice (GCP)\n\n"
                    "Articles 16 to 24: Principal Investigator (PI) & Informed Consent Mandate:\n"
                    "1. Investigator Responsibility: The Principal Investigator must hold valid medical practice licensure, formal GCP certification, and take total accountability for trial conduct at the investigative site.\n"
                    "2. Informed Consent Execution:\n"
                    "   - Prior to any trial-related intervention or procedure, the subject or legal representative must personally sign and date the IRB-approved Informed Consent Form (ICF), counter-signed by the consenting investigator.\n"
                    "   - Subjects must receive comprehensive explanations regarding experimental aspects, expected benefits, reasonably foreseeable risks, alternative treatments, and unconditional right to withdraw at any juncture without forfeiture of standard medical care.\n"
                    "3. Vulnerable Subjects & Minors:\n"
                    "   - For pediatric subjects or incapacitated patients, written informed consent must be executed by their legal guardians; assent must additionally be obtained from minors capable of understanding.\n"
                    "   - In emergency situations where prior consent is impossible, special ethical approval and deferred consent procedures stipulated in the protocol must be followed."
                )
            },
            {
                "section_id": "gcp_sec3_sponsor_monitoring",
                "section_title": "第四章：申办者质量管理体系、监查员（CRA）与独立稽查规程",
                "section_title_en": "Chapter 4: Sponsor Quality System, Monitoring (CRA) & Auditing",
                "pages": [3],
                "content_zh": (
                    "国家药品监督管理局 国家卫生健康委员会 2020年第57号公告《药物临床试验质量管理规范》（GCP）\n\n"
                    "第二十五条 至 第三十九条：申办者职责与质量监督：\n"
                    "1. 质量保证与质量控制体系：申办者是临床试验质量和受试者安全的法定责任主体。申办者应当建立涵盖临床试验设计、执行、记录、评估及报告的全流程质量保证与质量控制标准操作规程（SOP）。\n"
                    "2. 临床监查员（CRA）职责与监查计划：\n"
                    "   - 申办者应当指派具备充分培训与胜任力的监查员，制定基于风险的监查计划（Risk-Based Monitoring Plan）；\n"
                    "   - 监查员必须定期实地访问试验机构，核实原始数据一致性（Source Data Verification, SDV），确认受试者入组符合标准、知情同意签署完整有效、试验用药品保存符合温度标准与溯源记录清晰；\n"
                    "   - 监查员每次监查后必须在规定时间内向申办者提交书面监查报告，并向研究者反馈需整改的缺陷项。\n"
                    "3. 独立稽查（Auditing）：申办者应当指派独立于临床试验项目团队的专业稽查员实施稽查，评估试验实施是否符合试验方案、SOP、GCP及现行法律法规，出具独立稽查报告。"
                ),
                "content_en": (
                    "NMPA & NHC Notice No. 57 (2020) Good Clinical Practice (GCP)\n\n"
                    "Articles 25 to 39: Sponsor Quality Management & Monitoring Protocols:\n"
                    "1. Sponsor Quality Oversight: The sponsor holds ultimate statutory responsibility for trial quality, data integrity, and subject safety, requiring established QA/QC SOP systems.\n"
                    "2. Clinical Research Associate (CRA) Monitoring:\n"
                    "   - The sponsor must deploy qualified CRAs following a Risk-Based Monitoring (RBM) plan.\n"
                    "   - CRAs perform on-site visits to execute 100% Source Data Verification (SDV) for critical data points, verify protocol adherence, informed consent execution, and investigational product accountability.\n"
                    "   - Comprehensive written monitoring reports must be submitted to the sponsor and PI after each visit.\n"
                    "3. Independent Auditing: The sponsor conducts independent QA audits separate from routine monitoring to evaluate protocol, SOP, and regulatory compliance."
                )
            },
            {
                "section_id": "gcp_sec4_safety_sae_susar",
                "section_title": "第五章：安全性报告：严重不良事件（SAE）与 SUSAR 快速报告时限表（法定强制要求）",
                "section_title_en": "Chapter 5: Safety Reporting: SAE & SUSAR Expedited Timelines (Mandatory)",
                "pages": [4],
                "content_zh": (
                    "国家药品监督管理局 国家卫生健康委员会 2020年第57号公告《药物临床试验质量管理规范》（GCP）\n\n"
                    "第四十条 至 第四十五条：安全性事件法定定义与严格报告时限要求：\n\n"
                    "1. 关键术语法定定义：\n"
                    "- 不良事件（Adverse Event, AE）：受试者接受试验用药品后出现的所有不良医学事件，不一定与试验药物有因果关系。\n"
                    "- 严重不良事件（Serious Adverse Event, SAE）：临床试验过程中发生的导致以下后果之一的事件：① 导致死亡；② 危及生命；③ 导致住院或延长住院时间；④ 导致永久或显著的残疾/功能丧失；⑤ 先天性畸形或出生缺陷；⑥ 其他重要医学事件。\n"
                    "- 可疑且非预期严重不良反应（SUSAR）：怀疑与试验药物相关（可能或很可能相关），且其性质或严重程度与现有《研究者手册》或药品说明书不一致的严重不良事件。\n\n"
                    "2. 法定报告时限与途径表（法定不可违背）：\n\n"
                    "| 事件类型 | 报告责任人 | 报告对象 | 首次法定报告时限 | 随访报告时限 |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| 严重不良事件 (SAE) | 主要研究者 (PI) | 申办者、伦理委员会 | 获知后 24小时内 | 持续随访直至事件缓解或稳定 |\n"
                    "| 致死或危及生命的 SUSAR | 申办者 (Sponsor) | 国家药监局(CDE)、伦理委员会 | 首次获知后 7个自然日内 | 首次报告后 8个自然日内提交完整报告 |\n"
                    "| 非致死/非危及生命的 SUSAR | 申办者 (Sponsor) | 国家药监局(CDE)、伦理委员会 | 首次获知后 15个自然日内 | 收到新信息后 15个自然日内提交更新 |\n"
                    "| 年度安全性更新报告 (DSUR) | 申办者 (Sponsor) | 国家药监局(CDE)、各中心机构与IRB | 试验启动后 每年一次 | 报告周期截止后 60天内提交 |"
                ),
                "content_en": (
                    "NMPA & NHC Notice No. 57 (2020) Good Clinical Practice (GCP)\n\n"
                    "Articles 40 to 45: Safety Definitions & Expedited Safety Reporting Timelines:\n\n"
                    "1. Statutory Definitions:\n"
                    "- Serious Adverse Event (SAE): Any untoward medical occurrence that results in death, is life-threatening, requires inpatient hospitalization or prolongation of existing hospitalization, results in persistent or significant disability/incapacity, congenital anomaly/birth defect, or medically important event.\n"
                    "- SUSAR (Suspected Unexpected Serious Adverse Reaction): An SAE suspected of having a causal relationship with the investigational drug whose nature or severity is inconsistent with the Investigator's Brochure (IB).\n\n"
                    "2. Mandatory Reporting Timelines:\n\n"
                    "| Event Type | Reporter | Recipient | Initial Statutory Timeline | Follow-up Timeline |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| SAE (All types) | PI | Sponsor, IRB | Within 24 hours of awareness | Continuous follow-up until resolution |\n"
                    "| Fatal or Life-Threatening SUSAR | Sponsor | NMPA (CDE), IRB | Within 7 calendar days | Comprehensive report within +8 calendar days |\n"
                    "| Non-Fatal, Non-Life-Threatening SUSAR | Sponsor | NMPA (CDE), IRB | Within 15 calendar days | Updated report within 15 calendar days |\n"
                    "| Development Safety Update Report (DSUR) | Sponsor | NMPA (CDE), IRB | Annually | Within 60 days of data lock point |"
                )
            },
            {
                "section_id": "gcp_sec5_data_edc_tmf",
                "section_title": "第六章：试验用药品管理、EDC电子数据系统与试验档案（TMF）保存期限",
                "section_title_en": "Chapter 6: IP Control, Electronic Data Capture (EDC) & TMF Retention",
                "pages": [5],
                "content_zh": (
                    "国家药品监督管理局 国家卫生健康委员会 2020年第57号公告《药物临床试验质量管理规范》（GCP）\n\n"
                    "第四十六条 至 第五十五条：试验用药品、电子数据与档案归档标准：\n"
                    "1. 试验用药品（IP）全过程管理：\n"
                    "   - 试验用药品必须具有合格的检验报告书，双盲试验药品外观、气味、包装必须严格一致；\n"
                    "   - 机构必须配备专人专库（专柜）双人双锁管理，温湿度连续监测记录，发放、回收、销毁具备闭环记录凭证。\n"
                    "2. 电子数据采集系统（EDC）与数据完整性：\n"
                    "   - EDC系统必须经过计算机化系统验证，具备严格的用户权限分级管理与密码保护；\n"
                    "   - 必须具备不可关闭、不可删除的计算机审计追踪功能（Audit Trail），自动记录所有数据录入、修改人员姓名、时间戳以及修改原因；\n"
                    "   - 录入数据必须与源文件（病历、化验单、心电图等）完全一致，任何疑问必须通过系统疑问（Query）流程规范闭环。\n"
                    "3. 临床试验主文档（TMF）法定归档保存期：\n"
                    "   - 研究机构和申办者必须妥善保存临床试验所有记录资料；\n"
                    "   - 保存期限：中国GCP法定要求申办者和试验机构应当妥善保存临床试验文件，保存时间至药品上市许可后至少 5 年；未上市药品的资料应当保存至临床试验终止后至少 5 年（ICH GCP要求保存至产品退市后或更长时间）。"
                ),
                "content_en": (
                    "NMPA & NHC Notice No. 57 (2020) Good Clinical Practice (GCP)\n\n"
                    "Articles 46 to 55: Investigational Product, EDC Validation & TMF Archiving:\n"
                    "1. Investigational Product (IP) Accountability: Qualified release certificates required; double-blind placebos matching active drug in appearance, taste, and packaging. Temperature-controlled storage with continuous monitoring and complete chain-of-custody documentation.\n"
                    "2. Electronic Data Capture (EDC) & Data Integrity: EDC software must be validated, role-based access controlled, and equipped with immutable 21 CFR Part 11 compliant audit trails capturing timestamps, user identities, and modification reasons for all data changes.\n"
                    "3. Trial Master File (TMF) Retention: Statutory requirement dictates retention of all clinical trial documentation by sponsor and investigator sites for at least 5 years after marketing approval, or at least 5 years following formal trial discontinuation."
                )
            }
        ]
    })

    # =========================================================================
    # 2. NMPA Good Laboratory Practice (GLP)
    # =========================================================================
    docs.append({
        "doc_id": "nmpa_glp_official",
        "doc_title": "国家药品监督管理局《药物非临床研究质量管理规范》（GLP规范）",
        "doc_title_zh": "国家药品监督管理局《药物非临床研究质量管理规范》（GLP规范）",
        "doc_title_en": "NMPA Good Laboratory Practice for Non-Clinical Laboratory Studies (GLP)",
        "jurisdiction": "NMPA",
        "source_file": "nmpa_glp_nonclinical_studies_full.md",
        "version": "NMPA-GLP-Official",
        "sections": [
            {
                "section_id": "glp_sec1_sd_qau_governance",
                "section_title": "第一章：组织机构与关键法定职责：专题负责人（SD）制度与质量保证部门（QAU）",
                "section_title_en": "Chapter 1: Study Director (SD) & Quality Assurance Unit (QAU) Mandates",
                "pages": [1],
                "content_zh": (
                    "国家药品监督管理局《药物非临床研究质量管理规范》（GLP）：\n\n"
                    "一、核心组织机构与人员职责规定：\n"
                    "非临床安全性评价研究机构必须建立完善的组织机构，明确机构负责人（Test Facility Management, TFM）、专题负责人（Study Director, SD）及质量保证部门（Quality Assurance Unit, QAU）的法定职责：\n"
                    "1. 专题负责人（SD）法定专职责任制度：\n"
                    "   - 每一项非临床研究必须且只能指定一名专职技术人员担任专题负责人（SD）；\n"
                    "   - SD全面负责该试验的研究设计、方案制定、现场执行、数据分析、偏差处理及最终总结报告撰写；\n"
                    "   - SD对试验数据的真实性、完整性、准确性及研究全过程符合GLP规范承担终身技术与法定责任。\n"
                    "2. 质量保证部门（QAU）独立监督职责：\n"
                    "   - QAU直接对机构负责人（TFM）负责，必须完全独立于试验具体操作人员及SD；\n"
                    "   - 质量检查类型包括：基于方案的研究检查（Study-based inspection）、基于设施的检查（Facility-based inspection）和基于操作过程的检查（Process-based inspection）；\n"
                    "   - QAU必须对每一项试验方案、原始记录及总结报告进行独立核查，并在总结报告中签署《质量保证声明》（QA Statement），确认报告真实完整地反映了原始试验数据。"
                ),
                "content_en": (
                    "NMPA Good Laboratory Practice (GLP) Regulations:\n\n"
                    "Chapter 1: Organizational Governance, Study Director (SD) & QAU Mandates:\n"
                    "1. Study Director (SD) Ultimate Responsibility:\n"
                    "   - For each non-clinical safety study, management must designate a single individual as Study Director.\n"
                    "   - The SD holds overall technical and statutory responsibility for study protocol development, execution, data verification, deviation handling, and final report compilation in strict accordance with GLP.\n"
                    "2. Quality Assurance Unit (QAU) Independence:\n"
                    "   - QAU reports directly to Test Facility Management (TFM) and operates completely independent of study personnel and SDs.\n"
                    "   - QAU conducts study-based, facility-based, and process-based inspections.\n"
                    "   - QAU inspects all protocols, raw data, and final reports, appending a signed QA Statement certifying report authenticity."
                )
            },
            {
                "section_id": "glp_sec2_facilities_sop_animals",
                "section_title": "第二章：实验设施、标准操作规程（SOP）与实验动物管理",
                "section_title_en": "Chapter 2: Animal Care, Test Facility Infrastructure & SOP System",
                "pages": [2],
                "content_zh": (
                    "国家药品监督管理局《药物非临床研究质量管理规范》（GLP）：\n\n"
                    "二、设施环境、SOP与实验动物技术规范：\n"
                    "1. 设施布局与隔离要求：\n"
                    "   - 研究机构应当具备不同功能区域的物理隔离：实验动物饲养区、检疫隔离区、供试品与对照品配制与分析区、病理尸检与取材区、组织病理制片区、档案资料室；\n"
                    "   - 动物房环境控制：屏障系统温湿度（通常温度 20~26℃，相对湿度 40%~70%）、气压梯度、换气次数（10~15次/小时）及光照周期（12小时明/12小时暗）必须连续自动监测并记录。\n"
                    "2. 标准操作规程（SOP）覆盖范围：\n"
                    "   - 机构必须制定覆盖所有实验环节的现行有效SOP体系：供试品管理、动物饲养与检疫、仪器使用校准、生化病理检测、原始数据记录与修改、废弃物处理；\n"
                    "   - SOP的制定、修改、审核与批准必须经QAU审查并由机构负责人正式签署生效，任何操作偏离SOP均须记录为偏差。\n"
                    "3. 供试品与对照品管理：供试品必须明确批号、纯度、含量、稳定性及保存条件，接收、分装、配制及给药必须有完整天平称量打印条与双人复核凭证，每批供试品必须留存足够数量的备样至法定归档期限。"
                ),
                "content_en": (
                    "NMPA Good Laboratory Practice (GLP) Regulations:\n\n"
                    "Chapter 2: Facilities, Standard Operating Procedures (SOPs) & Animal Welfare:\n"
                    "1. Physical Separation of Facility Zones: Independent animal housing, quarantine facilities, dosing formulation suites, necropsy rooms, histology labs, and secure archive vaults.\n"
                    "2. Animal Environment Control: Continuous monitoring of temperature (20-26°C), humidity (40-70%), air exchange (10-15 cycles/hr), and lighting cycles (12h light/12h dark).\n"
                    "3. Standard Operating Procedures (SOPs): Comprehensive SOPs approved by TFM and verified by QAU covering dosing, assays, calibrations, and raw data entries; all protocol/SOP deviations documented.\n"
                    "4. Test Item Accountability: Purity, stability, batch certificates, formulation verification, balance printouts, and sample reserves retained throughout statutory archive periods."
                )
            },
            {
                "section_id": "glp_sec3_toxicology_battery",
                "section_title": "第三章：非临床安全性评价核心试验与毒理学技术规范",
                "section_title_en": "Chapter 3: Non-Clinical Safety Evaluation Battery & Toxicology Protocols",
                "pages": [3],
                "content_zh": (
                    "国家药品监督管理局《药物非临床研究质量管理规范》（GLP）及 ICH M3(R2) 非临床安全性指导原则：\n\n"
                    "三、支持新药临床申报（IND）的核心非临床毒理学试验组合：\n\n"
                    "1. 单次给药毒性试验（急性毒性）：\n"
                    "   - 目的：评估单次或24小时内多次高剂量给药后的急性中毒反应、靶器官毒性及无明显毒性反应剂量（NOAEL）或致死剂量范围；通常采用两种哺乳动物（啮齿类与非啮齿类）。\n"
                    "2. 重复给药毒性试验（长期毒性）：\n"
                    "   - 给药期限：啮齿类（大鼠）和非啮齿类（比格犬/食蟹猴）给药持续时间通常为2周、4周、13周（3个月）、26周（6个月）至39周（9个月），必须包含停药后恢复期（通常2~4周）；\n"
                    "   - 伴随毒代动力学（TK）：测定系统暴露量（AUC、Cmax）与毒性反应的剂量-暴露量-效应相关性，确定临床试验首剂安全起始剂量（HED与安全系数转换）。\n"
                    "3. 遗传毒性标准电池试验（Genotoxicity Battery）：\n"
                    "   - 试验一：细菌回复突变试验（Ames试验，鼠伤寒沙门氏菌与大肠埃希菌株）；\n"
                    "   - 试验二：体外哺乳动物细胞染色体畸变试验或小鼠淋巴瘤细胞基因突变试验（MLA）；\n"
                    "   - 试验三：体内啮齿类动物骨髓微核试验（Micronucleus Assay）或染色体畸变试验。\n"
                    "4. 安全药理学核心组合（Safety Pharmacology）：必须系统评估药物对生命关键系统（中枢神经系统、心血管系统——包括体外 hERG 钾通道阻断试验及体内心电图 QT 间期、呼吸系统）的潜在不良生理效应。\n"
                    "5. 生殖毒性与致癌性试验：生育力与早期胚胎发育毒性（Seg I）、胚胎-胎仔发育毒性（Seg II 胚胎致畸试验）、产前产后发育毒性（Seg III）；致癌性试验根据长期用药适应症开展（通常为2年啮齿动物生物分析）。"
                ),
                "content_en": (
                    "NMPA Good Laboratory Practice (GLP) & ICH M3(R2) Guidance:\n\n"
                    "Chapter 3: Standard Non-Clinical Safety Evaluation Battery:\n\n"
                    "1. Acute / Single-Dose Toxicity: Evaluates acute qualitative/quantitative toxic effects and NOAEL in two mammalian species (rodent and non-rodent).\n"
                    "2. Repeated-Dose Toxicity (Chronic): Durations ranging from 2-4 weeks to 3, 6, or 9 months in rodents (rats) and non-rodents (dogs/monkeys), including a 2-4 week recovery phase to assess reversibility. Accompanied by Toxicokinetics (TK) exposure profiling (AUC, Cmax).\n"
                    "3. Standard Genotoxicity Battery:\n"
                    "   - Bacterial reverse mutation test (Ames test across Salmonella and E. coli strains);\n"
                    "   - In vitro mammalian chromosome aberration test or mouse lymphoma assay (MLA);\n"
                    "   - In vivo rodent bone marrow erythrocyte micronucleus test.\n"
                    "4. Safety Pharmacology Core Battery: Central nervous system (CNS), cardiovascular system (in vitro hERG potassium channel assay & in vivo ECG QT interval), and respiratory function.\n"
                    "5. Reproductive & Carcinogenicity Studies: Segment I (fertility), Segment II (teratogenicity/embryo-fetal development), Segment III (pre/post-natal development), and 2-year rodent carcinogenicity bioassays when indicated."
                )
            },
            {
                "section_id": "glp_sec4_archive_retention_10yrs",
                "section_title": "第四章：原始记录、数据完整性与资料档案保存期（≥10年法定标准）",
                "section_title_en": "Chapter 4: Raw Data Integrity & Statutory Archive Retention (>=10 Years)",
                "pages": [4],
                "content_zh": (
                    "国家药品监督管理局《药物非临床研究质量管理规范》（GLP）：\n\n"
                    "四、原始数据定义、归档管理与法定保存期限：\n"
                    "1. 原始记录（Raw Data）法定定义：\n"
                    "   - 原始记录是指在非临床安全性研究过程中记载原始观察、原始测量与原始操作活动的初始记录文件；\n"
                    "   - 包含：手工填写的纸质试验记录本、电子仪器自动输出的打印条（天平称量单、生化分析仪打印联、病理显微照片）、原始色谱图、电子数据文件及计算机化系统审计追踪日志；\n"
                    "   - 原始记录任何涂改均须保持原有记录清晰可辨，并由修改人签字、注明修改日期和修改理由。\n"
                    "2. 资料档案库与档案管理员：\n"
                    "   - 机构必须设立独立的防火、防潮、防虫、防盗的专用档案资料室，指定专职档案管理员，实行严格的出入库借阅审批登记制度；\n"
                    "   - 归档内容：试验方案、原始数据、标本（石蜡包埋组织块、病理切片）、供试品留样、总结报告正本、QAU核查报告及SOP历史版本。\n"
                    "3. 法定档案保存期限要求（强制性标准）：\n"
                    "   - 用于支持药物注册申请的非临床研究档案资料，总结报告完成后的法定保存期限：自总结报告签署之日起至少保存 10 年，或者保存至该药品获准上市后至少 5 年（以两者较长者为准）；\n"
                    "   - 未获批准上市的新药研究资料，档案保存期同样不得少于 10 年。"
                ),
                "content_en": (
                    "NMPA Good Laboratory Practice (GLP) Regulations:\n\n"
                    "Chapter 4: Raw Data Definition, Archiving & Mandatory Retention (>=10 Years):\n"
                    "1. Raw Data Definition & Traceability: Includes original observation worksheets, instrument printouts, chromatograms, histology slides, tissue blocks, digital records, and computerized system audit trails. Errors corrected with single strike-through, explanation, signature, and timestamp.\n"
                    "2. Archive Facility Governance: Fireproof, humidity-controlled, secure archive vaults managed by dedicated archivists under strict chain-of-custody borrowing logs.\n"
                    "3. Mandatory Retention Periods:\n"
                    "   - Regulatory non-clinical study documentation, specimens, paraffin blocks, and reports must be archived for at least 10 years following final study report completion, or at least 5 years after marketing approval, whichever is longer.\n"
                    "   - Unapproved drug archives must also be retained for a statutory minimum of 10 years."
                )
            }
        ]
    })

    # =========================================================================
    # 3. ICH Q2(R2) Validation of Analytical Procedures
    # =========================================================================
    docs.append({
        "doc_id": "ich_q2_r2_validation",
        "doc_title": "ICH Q2(R2) 分析方法验证指导原则（ICH Harmonised Guideline）",
        "doc_title_zh": "ICH Q2(R2) 分析方法验证指导原则（ICH Harmonised Guideline）",
        "doc_title_en": "ICH Q2(R2) Guideline: Validation of Analytical Procedures",
        "jurisdiction": "ICH",
        "source_file": "ich_q2_r2_analytical_validation_full.md",
        "version": "ICH-Q2(R2)-2023-Official",
        "sections": [
            {
                "section_id": "ich_q2_sec1_specificity_linearity",
                "section_title": "第一章：验证特性与判定标准：专属性/特异度（Specificity）与线性（Linearity）",
                "section_title_en": "Chapter 1: Validation Characteristics: Specificity & Linearity",
                "pages": [1],
                "content_zh": (
                    "国际人用药品注册技术协调会 ICH Q2(R2) 分析方法验证指导原则：\n\n"
                    "一、方法验证法定特性与评价准则：\n"
                    "1. 专属性 / 特异度（Specificity / Selectivity）：\n"
                    "   - 定义：指在可能存在干扰组分（如赋形剂辅料、降解产物、杂质、合成中间体或共存活性物质）的情况下，分析方法能够准确、特异地区分和测定被分析物的能力。\n"
                    "   - 鉴别试验：必须证明该方法能够区分结构相似的化合物或阴性对照；\n"
                    "   - 杂质测定与含量测定（色谱法）：必须证明目标分析物色谱峰与相邻杂质峰之间的分离度（Resolution, R）必须符合规定（通常要求 $R \\ge 1.5$ 达到基线分离）；采用二极管阵列检测器（DAD）或质谱（MS）确认光谱纯度，证明主峰中无共洗脱的隐性杂质。\n"
                    "2. 线性（Linearity）：\n"
                    "   - 定义：指在设计的测定范围内，分析测试响应信号与样品中被分析物浓度（或量）成正比关系的能力。\n"
                    "   - 试验要求：至少制备 5 个浓度梯度的对照品溶液进行测定；\n"
                    "   - 范围跨度：\n"
                    "     * 含量测定（Assay）：通常应覆盖标示浓度的 80% ~ 120%（或 70% ~ 130%）；\n"
                    "     * 含量均匀度（CU）：应覆盖标示浓度的 70% ~ 130%；\n"
                    "     * 溶出度测定：应覆盖标示浓度的 $\\pm 20\\%$（从低点至标示量 120%）；\n"
                    "     * 杂质定量分析：通常从定量限（LOQ）至杂质控制限度的 120%（或 150%）；\n"
                    "   - 统计判定指标：线性回归方程相关系数（r）必须满足 $r \\ge 0.999$（或决定系数 $R^2 \\ge 0.998$）；截距（y-intercept）应当接近零且经统计学假设检验与零无显著差异；绘制残差图，残差应当围绕零线呈随机正态分布，无系统性弯曲趋势。"
                ),
                "content_en": (
                    "ICH Harmonised Guideline Q2(R2) Validation of Analytical Procedures:\n\n"
                    "Chapter 1: Specificity & Linearity Specifications:\n"
                    "1. Specificity / Selectivity: Assesses unambiguous assessment of the analyte in the presence of components expected to be present (excipients, degradants, impurities, synthetic intermediates).\n"
                    "   - For chromatographic assays/impurities: Resolution between analyte and adjacent peaks must meet criteria ($R \\ge 1.5$ baseline separation). DAD peak purity index or MS confirms lack of co-eluting species.\n"
                    "2. Linearity: Ability to elicit test results directly proportional to analyte concentration within a given range.\n"
                    "   - Minimum 5 concentration levels across the analytical range.\n"
                    "   - Assay Range: 80% to 120% of target concentration (or 70%-130% for content uniformity); Impurities: LOQ to 120% of specification limit.\n"
                    "   - Acceptance Criteria: Correlation coefficient $r \\ge 0.999$ (or $R^2 \\ge 0.998$); y-intercept statistically indistinguishable from zero; residual plot demonstrating random normal scatter without curvature."
                )
            },
            {
                "section_id": "ich_q2_sec2_accuracy_precision",
                "section_title": "第二章：准确度（Accuracy / 回收率）与精密度（Precision）多级评价标准",
                "section_title_en": "Chapter 2: Accuracy (Recovery) & Precision Multi-Tier Acceptance Criteria",
                "pages": [2],
                "content_zh": (
                    "国际人用药品注册技术协调会 ICH Q2(R2) 分析方法验证指导原则：\n\n"
                    "二、准确度与精密度评价规程：\n"
                    "1. 准确度 / 回收率（Accuracy / Recovery）：\n"
                    "   - 定义：指该方法测得的分析结果与公认的真实值或参考标准值之间的一致程度。\n"
                    "   - 试验设计：采用已知量的杂质或活性物质加入到辅料空白基质中（标准加入回收法）；必须在规定的线性范围内至少选取 3 个不同浓度水平（低、中、高，如 80%、100%、120%），每个浓度水平至少独立制备并测定 3 份样品（共 9 次独立测定数据）；\n"
                    "   - 法定回收率（Recovery Rate）计算公式：$\\text{Recovery (\\%)} = \\frac{\\text{测得量} - \\text{基质未加标量}}{\\text{加入标准品理论量}} \\times 100\\%$\n"
                    "   - 合格判定限度：原料药及制剂含量测定平均回收率通常应在 98.0% ~ 102.0% 之间（或 97.0% ~ 103.0%）；微量杂质定量测定平均回收率通常要求在 80.0% ~ 120.0%（高灵敏度要求下 85.0% ~ 115.0%）范围内。\n"
                    "2. 精密度（Precision）：\n"
                    "   - 重复性（Repeatability）：在相同操作条件、同一分析人员、同一仪器系统下，短时间内进行的多次测定。要求：独立制备 6 份 100% 浓度的样品测定，或 3 个浓度水平各制备 3 份样品测定；主含量测定相对标准偏差（RSD）通常要求 $\\le 1.0\\%$ 或 $\\le 2.0\\%$；\n"
                    "   - 中间精密度（Intermediate Precision）：同一实验室内不同分析人员、不同检测日期、使用不同仪器设备进行对比考察，RSD 限度通常要求 $\\le 2.0\\% \\sim 3.0\\%$；\n"
                    "   - 重现性（Reproducibility）：不同实验室间（协作标定）的精密度考察，通常用于国家标准制定或药典方法协作审定。"
                ),
                "content_en": (
                    "ICH Harmonised Guideline Q2(R2) Validation of Analytical Procedures:\n\n"
                    "Chapter 2: Accuracy & Precision Evaluation:\n"
                    "1. Accuracy (Recovery):\n"
                    "   - Evaluated across 3 concentration levels (e.g. 80%, 100%, 120% of target) with a minimum of 3 replicates per level (9 independent measurements total) via spiking studies.\n"
                    "   - Recovery formula: $\\text{Recovery (\\%)} = \\frac{\\text{Measured Concentration} - \\text{Blank}}{\\text{Theoretical Added Concentration}} \\times 100\\%$\n"
                    "   - Acceptance Criteria: Drug substance/product assay mean recovery typically 98.0% - 102.0%; Impurities quantification typically 80.0% - 120.0%.\n"
                    "2. Precision:\n"
                    "   - Repeatability: Evaluated with 6 determinations at 100% test concentration or 3 replicates across 3 levels; Assay RSD $\\le 1.0\\%$ or $\\le 2.0\\%$.\n"
                    "   - Intermediate Precision: Within-laboratory variations across different analysts, days, and instrument systems; Assay RSD $\\le 2.0\\% - 3.0\\%$.\n"
                    "   - Reproducibility: Inter-laboratory collaborative testing for compendial or standardized regulatory methods."
                )
            },
            {
                "section_id": "ich_q2_sec3_lod_loq_robustness",
                "section_title": "第三章：检测限（LOD）、定量限（LOQ）与耐用性（Robustness）评价规范",
                "section_title_en": "Chapter 3: Detection Limit (LOD), Quantitation Limit (LOQ) & Robustness",
                "pages": [3],
                "content_zh": (
                    "国际人用药品注册技术协调会 ICH Q2(R2) 分析方法验证指导原则：\n\n"
                    "三、检测限、定量限与耐用性标准：\n"
                    "1. 检测限（Limit of Detection, LOD）：\n"
                    "   - 定义：样品中被分析物能够被检出的最低量，但不必定量测定其确切数值（用于限度检查）。\n"
                    "   - 信噪比法（S/N法）：对于基线有噪音的仪器分析方法（如HPLC、GC），信号峰高与基线噪声之比满足 $S/N \\ge 3:1$；\n"
                    "   - 基于响应标准差和斜率法公式：$\\text{LOD} = \\frac{3.3 \\times \\sigma}{S}$ （其中 $\\sigma$ 为响应的标准差，$S$ 为校正曲线的斜率）。\n"
                    "2. 定量限（Limit of Quantitation, LOQ）：\n"
                    "   - 定义：样品中被分析物能够被定量测定的最低量，其测定结果必须具有符合要求的精密度和准确度。\n"
                    "   - 信噪比法（S/N法）：信号峰高与基线噪声之比满足 $S/N \\ge 10:1$；\n"
                    "   - 基于标准差和斜率法公式：$\\text{LOQ} = \\frac{10 \\times \\sigma}{S}$；\n"
                    "   - 定量限验证要求：在 LOQ 浓度下配制样品进行独立测定（通常 $n \\ge 6$），测定结果的相对标准偏差 RSD 通常要求 $\\le 10.0\\%$，且平均回收率在 80.0% ~ 120.0% 之间。\n"
                    "3. 耐用性（Robustness）：\n"
                    "   - 定义：衡量在故意对分析参数引入微小合理变动时，分析结果不受影响的可靠性能力（反映日常使用稳定性）。\n"
                    "   - 考察变量（以高效液相色谱 HPLC 为例）：\n"
                    "     * 流动相 pH 值微变（$\\pm 0.2$ 单位）；\n"
                    "     * 流动相有机溶剂比例微变（$\\pm 2\\% \\sim \\pm 5\\%$）；\n"
                    "     * 色谱柱柱温微变（$\\pm 5^\\circ\\text{C}$）；\n"
                    "     * 流动相流速微变（$\\pm 10\\%$）；\n"
                    "     * 更换不同批号或不同品牌但相同填料规格的色谱柱；\n"
                    "     * 供试品溶液在室温及冷藏条件下的稳定性时限（0h, 4h, 8h, 12h, 24h, 48h，主峰面积变化 $\\le 2.0\\%$）。"
                ),
                "content_en": (
                    "ICH Harmonised Guideline Q2(R2) Validation of Analytical Procedures:\n\n"
                    "Chapter 3: LOD, LOQ & Robustness Criteria:\n"
                    "1. Limit of Detection (LOD): Lowest amount of analyte detectable but not necessarily quantitated. S/N $\\ge 3:1$ or calculated as $\\text{LOD} = \\frac{3.3\\sigma}{S}$.\n"
                    "2. Limit of Quantitation (LOQ): Lowest amount quantitated with suitable precision and accuracy. S/N $\\ge 10:1$ or $\\text{LOQ} = \\frac{10\\sigma}{S}$. At LOQ level, repeatability RSD must be $\\le 10.0\\%$ with recovery 80.0% - 120.0%.\n"
                    "3. Robustness: Evaluates capacity to remain unaffected by small, deliberate parameter variations:\n"
                    "   - Mobile phase pH variation ($\\pm 0.2$ pH units);\n"
                    "   - Organic solvent ratio variation ($\\pm 2\\% - 5\\%$);\n"
                    "   - Column temperature variation ($\\pm 5^\\circ\\text{C}$);\n"
                    "   - Flow rate variation ($\\pm 10\\%$);\n"
                    "   - Column batch-to-batch and manufacturer equivalency;\n"
                    "   - Autosampler solution stability across 24-48 hours (peak change $\\le 2.0\\%$)."
                )
            }
        ]
    })

    # =========================================================================
    # 4. ChP 2020 Vol IV General Chapter 0941: Uniformity of Dosage Units
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_0941_uniformity",
        "doc_title": "《中华人民共和国药典》2020年版四部 通则 0941 含量均匀度检查法",
        "doc_title_zh": "《中华人民共和国药典》2020年版四部 通则 0941 含量均匀度检查法",
        "doc_title_en": "ChP 2020 Vol IV General Chapter 0941: Uniformity of Dosage Units",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol4_general_chapter_0941_uniformity_full.md",
        "version": "2020-ChP-Official",
        "sections": [
            {
                "section_id": "0941_sec1_scope_sampling",
                "section_title": "通则 0941 第一节：方法原理、适用剂型范围与取样规定",
                "section_title_en": "Section 1: Principle, Dosage Form Scope & Sampling Rules",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0941 含量均匀度检查法\n\n"
                    "1. 适用剂型与法定标准范围：\n"
                    "含量均匀度系指单剂型固体、半固体和非均相液体制剂中各治疗单位主药含量的均匀程度。\n"
                    "下列制剂除另有规定外，必须进行含量均匀度检查：\n"
                    "- 小剂量固体制剂：片剂、胶囊剂、口服混悬剂或颗粒剂中，每片（粒）标示量小于 25 mg，或者主药含量按重量比小于该制剂总重量 25% 的单剂量固体制剂；\n"
                    "- 注射用无菌粉末：每支（瓶）标示量小于 25 mg，或者主药重量小于单支装量 25% 的注射用无菌制剂；\n"
                    "- 贴剂、透皮贴剂、眼用半固体制剂及栓剂等特定靶向控释剂型；\n"
                    "- 凡已规定进行含量均匀度检查的制剂，通常不再进行重量差异检查。\n\n"
                    "2. 抽样规程：\n"
                    "从检验批中随机抽取 10 个单位（初试），分别按照品种项下规定的定量分析方法逐个测定每个单位中主药的实际含量，并计算出各单位含量相当于标示量的百分比（$X_1, X_2, \\dots, X_{10}$）。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0941: Uniformity of Dosage Units\n\n"
                    "1. Dosage Form Scope & Compendial Mandate:\n"
                    "Assesses the degree of uniformity in the amount of the drug substance among individual dosage units.\n"
                    "Mandatory testing scope:\n"
                    "- Low-dose solid dosage forms: Tablets, capsules, granules containing active substance $< 25\\text{ mg}$ or active substance $< 25\\%$ of total dosage unit mass;\n"
                    "- Sterile dry powder injections containing active substance $< 25\\text{ mg}$ or active substance $< 25\\%$ of total dry fill weight;\n"
                    "- Transdermal patches, ophthalmic ointments, and suppositories;\n"
                    "- Dosage units subjected to content uniformity testing are generally exempt from weight variation testing.\n\n"
                    "2. Sampling: Randomly sample 10 individual units (initial test), assay active content of each unit, and express as percentage of label claim ($X_1, \\dots, X_{10}$)."
                )
            },
            {
                "section_id": "0941_sec2_formula_acceptance",
                "section_title": "通则 0941 第二节：法定判定参数公式与判定准则（A + 1.80S <= 15.0）",
                "section_title_en": "Section 2: Formula, Acceptance Value (A + 1.80S <= 15.0) & Retest Rules",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0941 含量均匀度检查法\n\n"
                    "1. 法定计算参数与公式：\n"
                    "设各单位测定值（占标示量百分比）为 $X_i$（$i = 1, 2, \\dots, n$），计算如下统计参数：\n"
                    "- 平均值 $\\bar{X}$：$\\bar{X} = \\frac{1}{n} \\sum_{i=1}^n X_i$\n"
                    "- 标准差 $S$：$S = \\sqrt{\\frac{\\sum_{i=1}^n (X_i - \\bar{X})^2}{n - 1}}$\n"
                    "- 标示量差值绝对值 $A$：$A = |100 - \\bar{X}|$\n"
                    "- 判定值（Acceptance Value, AV）：初试（$n=10$）按 $A + 1.80S$ 计算；复试（$n=30$）按 $A + 1.45S$ 计算。\n\n"
                    "2. 初试合格判定标准（$n = 10$）：\n"
                    "- 当 $A + 1.80S \\le 15.0$ 时，且每个单位的含量都在 $100 \\pm 15.0\\%$（即 85.0% ~ 115.0%）范围之内，判定该批制剂符合规定；\n"
                    "- 当 $A + 1.80S > 15.0$ 但 $\\le 25.0$ 时，或者虽 $A + 1.80S \\le 15.0$ 但有 1 个单位含量超出 $100 \\pm 15.0\\%$ 但在 $100 \\pm 25.0\\%$（即 75.0% ~ 125.0%）范围以内时，应另取 20 个单位进行复试；\n"
                    "- 若初试中 $A + 1.80S > 25.0$，或者有任何 1 个单位含量超出 $100 \\pm 25.0\\%$ 范围，直接判定为不符合规定，不得复试。\n\n"
                    "3. 复试合格判定标准（$n = 30$）：\n"
                    "- 根据全部 30 个单位的测定结果重新计算平均值 $\\bar{X}$、标准差 $S$ 及 $A$ 值；\n"
                    "- 若 $A + 1.45S \\le 15.0$，且在 30 个单位中超出 $100 \\pm 15.0\\%$ 但在 $100 \\pm 25.0\\%$ 范围以内的单位数不超过 1 个，且没有任何 1 个单位超出 $100 \\pm 25.0\\%$，判定该批制剂符合规定；否则判定不符合规定。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0941: Uniformity of Dosage Units\n\n"
                    "1. Mathematical Parameters & Formulas:\n"
                    "- Mean $\\bar{X} = \\frac{1}{n} \\sum X_i$\n"
                    "- Standard Deviation $S = \\sqrt{\\frac{\\sum (X_i - \\bar{X})^2}{n - 1}}$\n"
                    "- Mean deviation from label claim $A = |100 - \\bar{X}|$\n"
                    "- Acceptance Value (AV): Initial test ($n=10$): $A + 1.80S$; Retest ($n=30$): $A + 1.45S$.\n\n"
                    "2. Initial Test Acceptance Criteria ($n = 10$):\n"
                    "- Complies if $A + 1.80S \\le 15.0$ and all 10 individual units fall within $100 \\pm 15.0\\%$ (85.0% - 115.0%).\n"
                    "- Retest triggered if $A + 1.80S > 15.0$ but $\\le 25.0$, or if 1 unit falls outside $100 \\pm 15.0\\%$ but within $100 \\pm 25.0\\%$.\n"
                    "- Fails immediately if $A + 1.80S > 25.0$ or if any unit deviates beyond $100 \\pm 25.0\\%$ (75.0% - 125.0%).\n\n"
                    "3. Retest Acceptance Criteria ($n = 30$):\n"
                    "- Recalculate parameters across all 30 units: Complies if $A + 1.45S \\le 15.0$, no more than 1 unit deviates outside $100 \\pm 15.0\\%$ (while remaining within $100 \\pm 25.0\\%$), and zero units exceed $100 \\pm 25.0\\%$."
                )
            }
        ]
    })

    # =========================================================================
    # 5. ChP 2020 Vol IV General Chapter 0401: UV-Vis Spectrophotometry
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_0401_uv_vis",
        "doc_title": "《中华人民共和国药典》2020年版四部 通则 0401 紫外-可见分光光度法",
        "doc_title_zh": "《中华人民共和国药典》2020年版四部 通则 0401 紫外-可见分光光度法",
        "doc_title_en": "ChP 2020 Vol IV General Chapter 0401: Ultraviolet-Visible Spectrophotometry",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol4_general_chapter_0401_uv_vis_full.md",
        "version": "2020-ChP-Official",
        "sections": [
            {
                "section_id": "0401_sec1_calibration",
                "section_title": "通则 0401 第一节：仪器校正与检定指标（波长、吸光度准确度、杂散光）",
                "section_title_en": "Section 1: Calibration (Wavelength, Photometric Accuracy, Stray Light)",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0401 紫外-可见分光光度法\n\n"
                    "1. 仪器法定校正与检定标准：\n"
                    "紫外-可见分光光度计用于药品检验前，必须定期检定并符合下列法定技术指标：\n"
                    "- 波长校正（Wavelength Accuracy）：采用氧化钬玻璃滤光片或汞灯特征谱线检定。氧化钬特征吸收峰为 241.15 nm、287.15 nm、361.5 nm、445.6 nm、536.3 nm 等，波长示值误差在紫外区不得超过 $\\pm 1\\text{ nm}$，可见光区不得超过 $\\pm 2\\text{ nm}$；\n"
                    "- 吸光度准确度（Photometric Accuracy）：采用在特定波长经国家标准物质认证的重铬酸钾硫酸溶液（按药典规程精准配制并在 $120^\\circ\\text{C}$ 干燥恒重）检定：\n"
                    "  * 在 235 nm、257 nm、313 nm 和 350 nm 测定比吸收系数（$E_{1\\text{cm}}^{1\\%}$），测定值与药典标准值比吸收相对误差必须在 $\\pm 0.5\\%$ 范围之内；\n"
                    "- 杂散光（Stray Light）检查：采用特定截止滤光液检查，如采用 10 g/L 碘化钠溶液在 220 nm 处，或 50 g/L 亚硝酸钠溶液在 340 nm 处测定，透光率必须小于 0.5%（吸光度必须大于 2.0）；\n"
                    "- 狭缝宽度（Spectral Bandwidth）：为保证测量准确度，仪器的狭缝宽度应当小于供试品吸收带半峰宽的 1/10。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0401: Ultraviolet-Visible Spectrophotometry\n\n"
                    "1. Calibration & Qualification Requirements:\n"
                    "- Wavelength Verification: Calibrated using holmium oxide glass filter (absorption lines at 241.15 nm, 287.15 nm, 361.5 nm, 445.6 nm, 536.3 nm) or low-pressure mercury lamp. Permissible tolerance $\\pm 1\\text{ nm}$ in UV region and $\\pm 2\\text{ nm}$ in visible region.\n"
                    "- Photometric Accuracy: Calibrated using potassium dichromate in 0.005 mol/L sulfuric acid solution at 235 nm, 257 nm, 313 nm, and 350 nm. Specific absorbance $E_{1\\text{cm}}^{1\\%}$ relative error must be within $\\pm 0.5\\%$.\n"
                    "- Stray Radiant Energy: Evaluated with cut-off filters/solutions (e.g., 10 g/L NaI at 220 nm or 50 g/L NaNO2 at 340 nm). Transmittance must be $< 0.5\\%$ (absorbance $> 2.0$).\n"
                    "- Slit Width: Slit width should not exceed 1/10 of the half-bandwidth of the analyte absorption band."
                )
            },
            {
                "section_id": "0401_sec2_photometric_range_methods",
                "section_title": "通则 0401 第二节：吸收度最佳读数区间（0.2 ~ 0.8）与定量测定方法",
                "section_title_en": "Section 2: Photometric Optimum Range (0.2 ~ 0.8) & Quantitation Methods",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0401 紫外-可见分光光度法\n\n"
                    "1. 比尔-朗伯定律与最佳读数区间：\n"
                    "- 吸收定律：$A = \\log_{10}(1/T) = E \\cdot c \\cdot l$（$A$ 为吸收度，$T$ 为透光率，$c$ 为浓度，$l$ 为液层厚度）；\n"
                    "- 最佳读数区间（法定要求）：为了避免光电转换系统的非线性偏差和仪器读数误差增大，供试品溶液的吸光度读数 $A$ 通常应当控制在 0.2 ~ 0.8（或 0.3 ~ 0.7）区间内；当 $A < 0.2$ 时读数相对误差显著上升，当 $A > 0.8$ 时杂散光干扰显著剧增。\n\n"
                    "2. 常用定量分析测定法：\n"
                    "- 对照品比较法：在相同溶剂、同波长和相同温度下分别测定供试品与对照品溶液的吸光度，$C_{\\text{样}} = \\frac{A_{\\text{样}}}{A_{\\text{对}}} \\times C_{\\text{对}}$，对照品与供试品吸光度均应落在最佳区间且浓度相近；\n"
                    "- 吸收系数法（$E_{1\\text{cm}}^{1\\%}$ 法）：指在特定波长下，100 mL 溶液中含有 1 g 溶质在 1 cm 光路吸收池中的吸光度。该法必须使用《中国药典》各品种项下法定载明的比吸收系数，且必须配制同一仪器系统下的合格对照品校正；\n"
                    "- 比色皿配对要求：紫外区必须使用石英比色皿，两只装有相同溶剂的比色皿在测定波长处的吸光度差值不得大于 0.005。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0401: Ultraviolet-Visible Spectrophotometry\n\n"
                    "1. Beer-Lambert Law & Photometric Range:\n"
                    "- Law: $A = \\log_{10}(1/T) = E \\cdot c \\cdot l$.\n"
                    "- Optimum Absorbance Range: The absorbance $A$ of analyte solutions should strictly be maintained between 0.2 and 0.8 (or 0.3 to 0.7). Absorbance $< 0.2$ magnifies relative instrumental reading error, while $A > 0.8$ exacerbates stray light deviations.\n\n"
                    "2. Quantitative Assay Methods:\n"
                    "- Reference Standard Comparison: $C_{\\text{sample}} = \\frac{A_{\\text{sample}}}{A_{\\text{ref}}} \\times C_{\\text{ref}}$, ensuring both solutions have matched concentrations and absorbance values within the linear optimal range.\n"
                    "- Specific Absorbance Method ($E_{1\\text{cm}}^{1\\%}$): Uses compendially certified specific absorption coefficients under rigorous qualification.\n"
                    "- Cuvette Matching: Quartz cells required for UV measurements; matched pair absorbance differential in solvent must be $\\le 0.005$."
                )
            }
        ]
    })

    # =========================================================================
    # 6. ChP 2020 Vol IV General Chapter 0861: Residual Solvents Determination
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_0861_residual_solvents",
        "doc_title": "《中华人民共和国药典》2020年版四部 通则 0861 残留溶剂测定法（ICH Q3C 对照标准）",
        "doc_title_zh": "《中华人民共和国药典》2020年版四部 通则 0861 残留溶剂测定法（ICH Q3C 对照标准）",
        "doc_title_en": "ChP 2020 Vol IV General Chapter 0861: Residual Solvents Determination (ICH Q3C Harmonized)",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol4_general_chapter_0861_residual_solvents_full.md",
        "version": "2020-ChP-Official",
        "sections": [
            {
                "section_id": "0861_sec1_solvent_classification_limits",
                "section_title": "通则 0861 第一节：残留溶剂三级分类体系与法定限度对照表（Class 1 / 2 / 3）",
                "section_title_en": "Section 1: Three-Class Solvent Categorization & Permitted Daily Exposure (PDE)",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0861 残留溶剂测定法（全面接轨 ICH Q3C）：\n\n"
                    "一、残留溶剂分类原则与法定浓度限度：\n"
                    "在原料药、辅料和制剂生产过程中使用或产生的有机挥发性溶剂划分为三类：\n\n"
                    "1. 第一类溶剂（Class 1：应当避免使用）：已知的人类致癌物、强烈可疑的人类致癌物或对环境造成严重公害的溶剂：\n"
                    "   - 苯（Benzene）：法定限度 2 ppm（0.0002%）；\n"
                    "   - 四氯化碳（Carbon tetrachloride）：法定限度 4 ppm；\n"
                    "   - 1,2-二氯乙烷（1,2-Dichloroethane）：法定限度 5 ppm；\n"
                    "   - 1,1-二氯乙烯（1,1-Dichloroethene）：法定限度 8 ppm；\n"
                    "   - 1,1,1-三氯乙烷（1,1,1-Trichloroethane）：法定限度 1500 ppm。\n\n"
                    "2. 第二类溶剂（Class 2：应当限制使用）：具有非遗传毒性致癌作用或其他不可逆毒性、显著可逆毒性的溶剂（法定每日允许暴露量 PDE）：\n"
                    "   - 乙腈（Acetonitrile）：PDE 4.1 mg/day，法定限度 410 ppm；\n"
                    "   - 三氯甲烷 / 氯仿（Chloroform）：PDE 0.6 mg/day，法定限度 60 ppm；\n"
                    "   - 二氯甲烷（Dichloromethane）：PDE 6.0 mg/day，法定限度 600 ppm；\n"
                    "   - 甲醇（Methanol）：PDE 30.0 mg/day，法定限度 3000 ppm；\n"
                    "   - 甲苯（Toluene）：PDE 8.9 mg/day，法定限度 890 ppm；\n"
                    "   - N,N-二甲基甲酰胺（DMF）：PDE 8.8 mg/day，法定限度 880 ppm；\n"
                    "   - N-甲基吡咯烷酮（NMP）：PDE 5.3 mg/day，法定限度 530 ppm；\n"
                    "   - 正己烷（Hexane）：PDE 2.9 mg/day，法定限度 290 ppm。\n\n"
                    "3. 第三类溶剂（Class 3：低毒性溶剂）：人体毒性低，每日允许摄入量（PDE）$\\ge 50\\text{ mg/day}$。包含乙醇、丙酮、乙酸乙酯、异丙醇、二甲基亚砜（DMSO）等，法定通用限度统一为 5000 ppm（0.5%）。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0861 & ICH Q3C Guidelines:\n\n"
                    "Section 1: Solvent Classification & Permitted Limits:\n"
                    "1. Class 1 Solvents (Solvents to be avoided): Known human carcinogens or environmental hazards:\n"
                    "   - Benzene: Limit 2 ppm (0.0002%);\n"
                    "   - Carbon tetrachloride: Limit 4 ppm;\n"
                    "   - 1,2-Dichloroethane: Limit 5 ppm;\n"
                    "   - 1,1-Dichloroethene: Limit 8 ppm;\n"
                    "   - 1,1,1-Trichloroethane: Limit 1500 ppm.\n\n"
                    "2. Class 2 Solvents (Solvents to be limited): Non-genotoxic animal carcinogens or significant toxicity (PDE basis):\n"
                    "   - Acetonitrile: PDE 4.1 mg/day, Limit 410 ppm;\n"
                    "   - Chloroform: PDE 0.6 mg/day, Limit 60 ppm;\n"
                    "   - Dichloromethane: PDE 6.0 mg/day, Limit 600 ppm;\n"
                    "   - Methanol: PDE 30.0 mg/day, Limit 3000 ppm;\n"
                    "   - Toluene: PDE 8.9 mg/day, Limit 890 ppm;\n"
                    "   - N,N-Dimethylformamide (DMF): PDE 8.8 mg/day, Limit 880 ppm;\n"
                    "   - N-Methylpyrrolidone (NMP): PDE 5.3 mg/day, Limit 530 ppm;\n"
                    "   - Hexane: PDE 2.9 mg/day, Limit 290 ppm.\n\n"
                    "3. Class 3 Solvents (Low toxic potential): PDE $\\ge 50\\text{ mg/day}$ (Ethanol, Acetone, Ethyl acetate, IPA, DMSO); compendial limit set at 5000 ppm (0.5%)."
                )
            },
            {
                "section_id": "0861_sec2_headspace_gc_conditions",
                "section_title": "通则 0861 第二节：顶空气相色谱法（HS-GC）检测规程与系统适用性",
                "section_title_en": "Section 2: Headspace Gas Chromatography (HS-GC) & System Suitability",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版四部 通则 0861 残留溶剂测定法：\n\n"
                    "二、分析仪器条件与系统适用性试验（HS-GC）：\n"
                    "1. 顶空气相色谱（HS-GC）仪器系统配置：\n"
                    "   - 顶空进样器条件：顶空瓶平衡温度通常设定为 $80^\\circ\\text{C} \\sim 85^\\circ\\text{C}$，平衡时间通常为 30 ~ 45 分钟，进样针与传输线温度高于平衡温度 $10^\\circ\\text{C} \\sim 15^\\circ\\text{C}$ 以防冷凝；\n"
                    "   - 色谱柱选用：通常采用中等极性或极性毛细管柱（如 6% 氰丙基苯基 - 94% 二甲基聚硅氧烷，DB-624 / HP-624，规格 30 m × 0.32 mm × 1.8 μm，或聚乙二醇 PEG-20M / DB-WAX）；\n"
                    "   - 检测器：通常采用氢火焰离子化检测器（FID）或气相色谱-质谱联用仪（GC-MS）；\n"
                    "   - 载气：高纯氮气或高纯氦气（纯度 $\\ge 99.999\\%$）。\n\n"
                    "2. 系统适用性试验指标（强制性标准）：\n"
                    "   - 分离度（Resolution, R）：各残留溶剂色谱峰之间，以及溶剂峰与样品溶剂峰（如水、DMF、DMSO）之间的分离度必须 $\\ge 1.5$；\n"
                    "   - 理论板数（n）：按各品种项下溶剂峰计算，通常不得低于 5000；\n"
                    "   - 重复性精密度（RSD）：对照品溶液连续进样 5 次或 6 次，待测溶剂峰面积的相对标准偏差 RSD：定量分析方法不得过 5.0%；限度检查方法不得过 10.0%。"
                ),
                "content_en": (
                    "ChP 2020 Volume IV General Chapter 0861: Residual Solvents Determination:\n\n"
                    "Section 2: Headspace Gas Chromatography (HS-GC) Instrumentation & SST:\n"
                    "1. HS-GC Conditions:\n"
                    "   - Headspace sampler: Equilibration temperature typically $80^\\circ\\text{C} - 85^\\circ\\text{C}$; equilibration duration 30-45 min; transfer line temperature maintained $+10^\\circ\\text{C} - 15^\\circ\\text{C}$ above vial temperature.\n"
                    "   - Capillary column: Intermediate polarity 6% cyanopropylphenyl - 94% dimethylpolysiloxane (DB-624, 30 m × 0.32 mm × 1.8 μm) or polyethylene glycol (DB-WAX).\n"
                    "   - Detector: Flame Ionization Detector (FID) or GC-MS; carrier gas high-purity N2 or He ($\\ge 99.999\\%$).\n\n"
                    "2. System Suitability Test (SST) Criteria:\n"
                    "   - Resolution: Chromatographic resolution between adjacent solvent peaks and sample matrix solvents must be $R \\ge 1.5$.\n"
                    "   - Theoretical Plates: Not less than 5000 for critical analyte peaks.\n"
                    "   - Precision (RSD): Peak area RSD across 5-6 replicate injections of reference solutions $\\le 5.0\\%$ for quantitative assays; $\\le 10.0\\%$ for limit tests."
                )
            }
        ]
    })

    # =========================================================================
    # 7. ChP 2020 Vol III & ICH Q6B: Monoclonal Antibodies & Biologics
    # =========================================================================
    docs.append({
        "doc_id": "chp_2020_vol3_biologics_mab",
        "doc_title": "《中华人民共和国药典》2020年版三部 重组单克隆抗体生物制品通则与质量控制规范",
        "doc_title_zh": "《中华人民共和国药典》2020年版三部 重组单克隆抗体生物制品通则与质量控制规范",
        "doc_title_en": "ChP 2020 Vol III & ICH Q6B: Recombinant Monoclonal Antibodies Quality Control Standards",
        "jurisdiction": "ChP",
        "source_file": "chp_2020_vol3_recombinant_mab_quality_standards_full.md",
        "version": "2020-ChP-Biologics-Official",
        "sections": [
            {
                "section_id": "mab_sec1_size_charge_variants",
                "section_title": "第一章：单抗纯度与异质性分析：分子排阻色谱（SEC-HPLC）与电荷变异体（iCIEF/CEX）",
                "section_title_en": "Chapter 1: Purity & Heterogeneity: SEC-HPLC Aggregates & Charge Variants",
                "pages": [1],
                "content_zh": (
                    "《中国药典》2020年版三部 重组单克隆抗体生物制品制造及检定通则（接轨 ICH Q6B）：\n\n"
                    "一、分子大小变异体与电荷变异体法定纯度标准：\n"
                    "重组单克隆抗体（mAb）属于大分子糖蛋白，其多聚体聚集物可能引发严重免疫原性反应，必须采用正交分析方法严控其纯度：\n"
                    "1. 分子排阻高效液相色谱法（SEC-HPLC）：\n"
                    "   - 测定目的：依据水动力学体积差异定量分离单抗分子的高分子量聚合物（HMWS / 聚集体）、主峰单体（Monomer）及低分子量碎片（LMWS）；\n"
                    "   - 法定质量标准限度：\n"
                    "     * 单体主峰纯度（Monomer Purity）：通常要求 $\\ge 95.0\\%$（许多商业化抗体放行限度要求 $\\ge 97.0\\% \\sim 98.0\\%$）；\n"
                    "     * 高分子量聚合物（HMWS）：通常严格控制在 $\\le 1.0\\% \\sim 2.0\\%$；\n"
                    "     * 低分子量片段（LMWS）：通常要求 $\\le 1.0\\% \\sim 2.0\\%$。\n"
                    "2. 毛细管电泳十二烷基硫酸钠（CE-SDS）：\n"
                    "   - 非还原型 CE-SDS（完整单抗分子量 ~150 kDa）：完整抗体纯度通常 $\\ge 90.0\\% \\sim 95.0\\%$；\n"
                    "   - 还原型 CE-SDS（重链 ~50 kDa，轻链 ~25 kDa）：重链与轻链总纯度通常要求 $\\ge 95.0\\%$。\n"
                    "3. 电荷变异体分析（WCX-HPLC 弱阳离子交换色谱 / iCIEF 成像毛细管等电聚焦）：\n"
                    "   - 分析脱酰胺化、C端赖氨酸脱除不完全、赖氨酸糖基化等电荷异构体；\n"
                    "   - 明确主峰（Main Peak）、酸性变异体（Acidic Peaks）和碱性变异体（Basic Peaks）的批间一致性分布范围（通常主峰纯度 $\\ge 60\\% \\sim 70\\%$）。"
                ),
                "content_en": (
                    "ChP 2020 Volume III & ICH Q6B Biopharmaceutical Specifications:\n\n"
                    "Chapter 1: Molecular Size & Charge Heterogeneity Profiling:\n"
                    "1. Size Exclusion Chromatography (SEC-HPLC):\n"
                    "   - Quantifies High Molecular Weight Species (HMWS / aggregates), Monomer, and Low Molecular Weight Species (LMWS / fragments).\n"
                    "   - Release Specification Limits:\n"
                    "     * Monomer Purity: $\\ge 95.0\\%$ (routinely set at $\\ge 97.0\\% - 98.0\\%$ for commercial release);\n"
                    "     * Aggregates (HMWS): $\\le 1.0\\% - 2.0\\%$;\n"
                    "     * Fragments (LMWS): $\\le 1.0\\% - 2.0\\%$.\n"
                    "2. Capillary Electrophoresis SDS (CE-SDS):\n"
                    "   - Non-reduced CE-SDS (intact IgG ~150 kDa): Intact monomer purity $\\ge 90.0\\% - 95.0\\%$.\n"
                    "   - Reduced CE-SDS (Heavy chain ~50 kDa, Light chain ~25 kDa): Sum of HC + LC $\\ge 95.0\\%$.\n"
                    "3. Charge Heterogeneity (CEX-HPLC / iCIEF): Identifies deamidation, C-terminal Lysine truncation, and sialylation variants. Demonstrates lot-to-lot comparability for acidic, main, and basic isoforms."
                )
            },
            {
                "section_id": "mab_sec2_process_impurities_hcp_dna",
                "section_title": "第二章：工艺相关杂质法定限度：宿主细胞蛋白（HCP）、残余DNA与脱落Protein A",
                "section_title_en": "Chapter 2: Process Impurity Limits: Host Cell Protein (HCP), resDNA & Protein A",
                "pages": [2],
                "content_zh": (
                    "《中国药典》2020年版三部 重组单克隆抗体生物制品制造及检定通则：\n\n"
                    "二、生物制品工艺残留杂质法定检测与限量标准（必须逐批严格检定）：\n\n"
                    "1. 宿主细胞蛋白（Host Cell Protein, HCP）残留量：\n"
                    "   - 来源与风险：来自宿主生产细胞株（如 CHO 细胞）的杂蛋白，进入人体具有极高免疫原性；\n"
                    "   - 检测方法：采用针对生产宿主菌株特异性开发并经过充分验证的双抗体夹心 ELISA 法；\n"
                    "   - 法定限度标准：通常要求成品中 HCP 残留量不得过蛋白质总量的 $0.005\\%$（即 $\\le 50\\text{ ng/mg}$ 或 $\\le 100\\text{ ng/mg}$，即 $\\le 100\\text{ ppm}$）；高端单抗放行标准通常严格控制在 $\\le 10\\text{ ng/mg}$。\n\n"
                    "2. 宿主细胞残余 DNA（Residual Host Cell DNA, resDNA）：\n"
                    "   - 风险控制：残余DNA片段具有潜在致癌性或感染性；\n"
                    "   - 检测方法：采用荧光染料结合法或特异性荧光定量 PCR 法（qPCR 法）；\n"
                    "   - 法定限度标准：中国药典与 WHO 规定，每单次人用剂量的纯化产品中，宿主细胞残余 DNA 含量必须严格低于 100 pg（即 $\\le 100\\text{ pg/剂}$）；对于连续多次高频给药的抗体制剂，企业内控标准通常严格限定为 $\\le 10\\text{ pg/剂}$，且残余 DNA 片段大小通常要求在 200 bp 以下。\n\n"
                    "3. 亲和层析脱落 Protein A 残留量：\n"
                    "   - 来源：下游纯化捕获阶段从 Protein A 亲和填料上脱落的配体；\n"
                    "   - 检测方法：特异性 ELISA 法测定；\n"
                    "   - 法定限度：通常要求成品中游离 Protein A 残留量 $\\le 5\\text{ ng/mg} \\sim 10\\text{ ng/mg}$。"
                ),
                "content_en": (
                    "ChP 2020 Volume III & WHO Guidelines for Biopharmaceuticals:\n\n"
                    "Chapter 2: Mandatory Process-Related Impurity Limits (Batch Release):\n\n"
                    "1. Host Cell Protein (HCP) Clearance:\n"
                    "   - Derived from host expression systems (e.g. CHO cells); high immunogenicity risk.\n"
                    "   - Analytical Method: Validated multi-polyclonal sandwich ELISA specific to the expression host.\n"
                    "   - Compendial Limits: Residual HCP must not exceed 0.005% of active protein content ($\\le 50\\text{ ng/mg}$ to $100\\text{ ng/mg}$ / 100 ppm); advanced commercial release specs mandate $\\le 10\\text{ ng/mg}$.\n\n"
                    "2. Residual Host Cell DNA (resDNA):\n"
                    "   - Potential oncogenic/infectivity hazard.\n"
                    "   - Analytical Method: Quantitative PCR (qPCR) or fluorescent dye binding.\n"
                    "   - Compendial Limits: ChP and WHO mandate residual host cell DNA $\\le 100\\text{ pg/dose}$ (strict internal release standard $\\le 10\\text{ pg/dose}$), with fragment lengths predominantly under 200 base pairs.\n\n"
                    "3. Leached Protein A:\n"
                    "   - Traced to affinity chromatography resin ligand leaching.\n"
                    "   - Analytical Method: High-sensitivity ELISA.\n"
                    "   - Specification Limit: Residual Protein A $\\le 5\\text{ ng/mg} - 10\\text{ ng/mg}$."
                )
            }
        ]
    })

    # =========================================================================
    # 8. FDA 21 CFR Part 312 & Part 314 (IND & NDA)
    # =========================================================================
    docs.append({
        "doc_id": "fda_21cfr_part312_part314_ind_nda",
        "doc_title": "FDA 21 CFR Part 312 (IND) & Part 314 (NDA): 新药临床申请与上市许可核心规程",
        "doc_title_zh": "FDA 21 CFR Part 312 (IND) & Part 314 (NDA): 新药临床申请与上市许可核心规程",
        "doc_title_en": "FDA 21 CFR Part 312 (IND) & Part 314 (NDA): Investigational New Drug & Marketing Approval",
        "jurisdiction": "FDA",
        "source_file": "fda_21cfr_part312_part314_ind_nda_official_full.md",
        "version": "21-CFR-312-314-Official",
        "sections": [
            {
                "section_id": "ind_sec1_content_format_312_23",
                "section_title": "21 CFR § 312.23: IND 申请资料法定架构（Form FDA 1571、CMC与方案）",
                "section_title_en": "21 CFR § 312.23: IND Application Dossier Architecture & Form 1571/1572",
                "pages": [1],
                "content_zh": (
                    "美国联邦法规法典 FDA 21 CFR Part 312（新药临床试验申请 Investigational New Drug Application）：\n\n"
                    "§ 312.23：IND 申报资料法定内容与格式标准：\n"
                    "申办者在启动人体临床试验前必须向 FDA 提交 IND 申请。法定申请卷宗必须按下列模块编排：\n"
                    "1. 封面表单 Form FDA 1571：由申办者或其法定代理人签署，包含试验药物名称、适应症、申办者法律承诺与监管联系人；\n"
                    "2. 试验方案概况与研究者声明 Form FDA 1572：明确每位主要研究者的姓名、执业资质、试验基地地址、评审伦理委员会（IRB）以及研究者遵守法规的法定签署承诺；\n"
                    "3. 研究者手册（Investigator's Brochure, IB）：汇总试验药物的化学、药理、毒理、药物代谢动力学及以往人体临床试验全部已知安全性和有效性数据；\n"
                    "4. 临床试验方案（Clinical Protocol）：详述试验目的、受试者入组/排除标准、给药剂量设计、安全终点监测、破盲程序及统计分析计划；\n"
                    "5. 药学与生产控制信息（Chemistry, Manufacturing, and Control, CMC）：提供原料药与制剂的化学结构确证、生产工艺、质量标准、分析方法验证及稳定性试验数据，证明试验药品质控符合 cGMP 标准且批间一致；\n"
                    "6. 药理学与毒理学数据：充分的非临床体内外安全性数据，支持人体试验起始剂量的合理性；\n"
                    "7. 法定审查时限（30天审评时钟）：FDA 自正式接收完整的 IND 申请之日起计算 30 个日历日。若 FDA 在 30 日内未发出暂停试验（Clinical Hold）指令，IND 自动合法生效，申办者即可启动临床试验。"
                ),
                "content_en": (
                    "FDA 21 CFR Part 312 Investigational New Drug Application (IND):\n\n"
                    "21 CFR § 312.23: Mandatory IND Application Content and Format:\n"
                    "1. Form FDA 1571: Signed contractual commitment by sponsor including administrative, drug, and indication declarations.\n"
                    "2. Form FDA 1572: Investigator's Statement documenting PI qualifications, clinical sites, IRB affiliation, and statutory commitment to GCP.\n"
                    "3. Investigator's Brochure (IB): Compilation of chemical, pharmacological, toxicological, and clinical safety profiles.\n"
                    "4. Clinical Protocol: Complete study design, inclusion/exclusion criteria, safety monitoring, stopping rules, and statistical plan.\n"
                    "5. Chemistry, Manufacturing, and Control (CMC): Synthetic route, drug substance/product specifications, analytical validation, and stability profiles.\n"
                    "6. Pharmacology & Toxicology: Comprehensive in vitro and animal in vivo safety data demonstrating acceptable safety margin for human dosing.\n"
                    "7. Statutory 30-Day Review Clock: Clinical investigation may legally commence 30 calendar days after FDA receives the IND submission unless placed on Clinical Hold."
                )
            },
            {
                "section_id": "ind_sec2_safety_reports_clinical_hold",
                "section_title": "21 CFR § 312.32 & § 312.42: IND 安全报告时限与临床试验暂停（Clinical Hold）法定情形",
                "section_title_en": "21 CFR § 312.32 & § 312.42: Safety Reporting Timelines & Clinical Hold Grounds",
                "pages": [2],
                "content_zh": (
                    "美国联邦法规法典 FDA 21 CFR Part 312：\n\n"
                    "一、§ 312.32 IND 安全性报告（IND Safety Reports）法定提交时限：\n"
                    "1. 7天快速报告（7-Day Alert）：\n"
                    "   - 针对非预期的、致命的或危及生命（Fatal or Life-Threatening）的疑似不良反应；\n"
                    "   - 申办者必须在首次获知信息后不迟于 7 个日历日内通知 FDA（电话、传真或电子快速提交），并在其后 8 天内提交书面详细报告。\n"
                    "2. 15天书面安全报告（15-Day Written Report）：\n"
                    "   - 针对所有严重且非预期的疑似不良反应（Serious and Unexpected Suspected Adverse Reaction）、非临床试验中观察到的严重致癌性/致畸性风险或实验室发现的重大安全性信号；\n"
                    "   - 申办者必须在获知信息后不迟于 15 个日历日内向 FDA 及所有参与试验的研究者提交书面报告。\n\n"
                    "二、§ 312.42 临床暂停（Clinical Hold）法定触发情形与复查程序：\n"
                    "临床暂停是 FDA 签发的强制性指令，要求申办者暂缓启动或立即停止正在进行的临床试验：\n"
                    "1. I期临床法定暂停理由：受试者面临不合理的重大健康安全风险；研究者缺乏胜任资质；研究者手册存在严重误导或重大缺陷；\n"
                    "2. II/III期临床法定暂停理由：除上述风险外，试验方案设计存在严重缺陷无法达成试验科学目的；\n"
                    "3. 解除程序：申办者针对 FDA 提出的缺陷项提交书面完整答辩整改报告后，FDA 具有 30 个日历日的法定复审期，FDA 发出书面解除通知后方可恢复试验。"
                ),
                "content_en": (
                    "FDA 21 CFR Part 312 Investigational New Drug Application (IND):\n\n"
                    "1. 21 CFR § 312.32 IND Safety Reporting Mandates:\n"
                    "   - 7-Day Alert: Any unexpected fatal or life-threatening suspected adverse reaction must be reported to FDA no later than 7 calendar days after sponsor awareness.\n"
                    "   - 15-Day Report: Any serious and unexpected suspected adverse reaction, clinically important animal toxicity finding, or safety signal must be submitted in writing within 15 calendar days.\n\n"
                    "2. 21 CFR § 312.42 Clinical Hold Grounds & Resumption:\n"
                    "   - Phase 1 Grounds: Unreasonable and significant risk of illness or injury to human subjects; unqualified investigators; deficient/misleading Investigator's Brochure.\n"
                    "   - Phase 2/3 Grounds: Above criteria plus clinical design flaw rendering the investigation incapable of demonstrating efficacy/safety.\n"
                    "   - Resumption: FDA has 30 calendar days to review the sponsor's complete written response and must issue formal authorization prior to study resumption."
                )
            },
            {
                "section_id": "nda_sec3_nda_structure_314_50",
                "section_title": "21 CFR § 314.50: 新药上市许可申请（NDA）法定架构与 CTD 模块对应关系",
                "section_title_en": "21 CFR § 314.50: NDA Dossier Structure & Common Technical Document (CTD)",
                "pages": [3],
                "content_zh": (
                    "美国联邦法规法典 FDA 21 CFR Part 314（新药上市申请 Applications for FDA Approval to Market a New Drug）：\n\n"
                    "§ 314.50：NDA 上市申报资料法定架构与通用技术文档（CTD）模块对照：\n"
                    "新药申请人必须提交足以证明药物安全性和有效性的完整临床与药学证据，法定申报模块包括：\n"
                    "1. 模块 1（Module 1 - 行政与区域信息）：Form FDA 356h、说明书样稿、快速通道或优先审评认定凭证、儿科评估计划（PREA）；\n"
                    "2. 模块 2（Module 2 - 通用技术文档概述）：CTD 质量概述（QOS）、非临床综述与总结、临床综述与总结（利益/风险综合评价）；\n"
                    "3. 模块 3（Module 3 - 质量 / CMC）：原料药与制剂的化学结构确证、全套生产工艺流程、工艺验证数据、关键质量属性（CQA）控制、杂质谱分析及长期稳定性数据；\n"
                    "4. 模块 4（Module 4 - 非临床研究报告）：完整的药理、毒理、毒代动力学及致癌性非临床试验原始报告；\n"
                    "5. 模块 5（Module 5 - 临床研究报告）：所有I、II、III期临床试验报告（CSR，符合 ICH E3 规程）、生物等效性/生物利用度研究报告、集成安全性分析（ISS）与集成有效性分析（ISE）；\n"
                    "6. 处方药用户付费法案（PDUFA）审评周期：标准审评（Standard Review）周期通常为 10 个月；优先审评（Priority Review）针对重大临床未满足需求疾病缩短至 6 个月。"
                ),
                "content_en": (
                    "FDA 21 CFR Part 314 New Drug Marketing Applications (NDA):\n\n"
                    "21 CFR § 314.50: Content & Format of an NDA (Common Technical Document Alignment):\n"
                    "1. Module 1 (Administrative): Form FDA 356h, draft prescribing information, user fee payment, pediatric assessment (PREA).\n"
                    "2. Module 2 (CTD Summaries): Quality Overall Summary (QOS), Nonclinical Overviews/Summaries, Clinical Overviews/Summaries (Integrated Benefit-Risk Analysis).\n"
                    "3. Module 3 (Quality / CMC): Synthesis, process validation, Critical Quality Attributes (CQA), impurity profiling, and commercial batch stability data.\n"
                    "4. Module 4 (Nonclinical Reports): Complete pharmacology, safety pharmacology, toxicology, and carcinogenicity study reports.\n"
                    "5. Module 5 (Clinical Study Reports): All Phase 1-3 Clinical Study Reports (ICH E3 compliant), Integrated Summary of Safety (ISS), Integrated Summary of Efficacy (ISE), and PK/PD reports.\n"
                    "6. PDUFA Review Timelines: 10 months for Standard Review; 6 months for Priority Review designations."
                )
            }
        ]
    })

    return docs
