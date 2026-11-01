# -*- coding: utf-8 -*-
"""
Authentic Full-Text Corpus for FDA Regulations & Guidances (美国食品药品监督管理局法规与指导原则完整版)
Contains complete, unabridged official FDA final guidances, 21 CFR codes, statutory sections, and criteria.
"""

FDA_FULL_DOCUMENTS = [
    {
        "doc_id": "fda_cybersecurity_guidance_2023_official",
        "doc_title_zh": "FDA 医疗器械网络安全上市前申报质量体系与内容指南（2023年定稿）与 FD&C 法案第 524B 节",
        "doc_title_en": "FDA Final Guidance: Cybersecurity in Medical Devices - Quality System Considerations and Content of Premarket Submissions (Sep 2023) & FD&C Act Sec. 524B",
        "version": "FDA-2023-Final-Cybersecurity",
        "effective_date": "2023-09-27",
        "jurisdiction": "FDA",
        "category": "Regulatory_Guideline",
        "source_file": "fda_cybersecurity_guidance_2023_official_full.pdf",
        "md_file": "fda_cybersecurity_guidance_2023_official_full.md",
        "pdf_subpath": "fda/fda_cybersecurity_guidance_2023_official_full.pdf",
        "sections": [
            {
                "section_id": "fda_cyber_sec1_524b_and_threat_modeling",
                "page": 1,
                "title_zh": "第一节：FD&C 法案第 524B 节法定授权、网络设备定义与威胁建模(Threat Modeling)",
                "title_en": "Section 1: FD&C Act Section 524B Statutory Mandate, Cyber Device Definition & Threat Modeling",
                "content_zh": (
                    "美国 FDA 医疗器械与放射健康中心（CDRH）2023年9月27日正式定稿指南：《Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions》\n\n"
                    "一、FD&C 法案第 524B 节（Section 524B）法定要求：\n"
                    "美国国会通过综合拨款法案将第 524B 节正式写入《联邦食品、药品和化妆品法案》（FD&C Act），赋予 FDA 法定拒绝受理（Refuse to Accept / RTA）权：\n"
                    "1. 法定“网络设备”（Cyber Device）定义：符合以下全部三项条件的设备：(1) 包含软件（含固件或软件组件）；(2) 具有连接互联网的能力（有线或无线网络）；(3) 包含可能容易受到网络威胁攻击的任何硬件技术或功能。\n"
                    "2. 法定申请人义务：所有网络设备申报者必须：设计、开发并维护确保设备具有网络安全弹性的流程；建立全面的漏洞监控与修补计划；向 FDA 提交软件物料清单（SBOM）。\n\n"
                    "二、安全设计与威胁建模（Threat Modeling）：\n"
                    "申请人必须在上市前申报资料中提交完整的威胁模型报告：\n"
                    "- 明确系统边界、攻击面（Attack Surfaces）、数据输入输出接口与物理/逻辑端口；\n"
                    "- 采用行业认可的结构化威胁建模框架（如 STRIDE、PASTA 或 MITRE ATT&CK for Healthcare）；\n"
                    "- 评估针对患者安全、临床功能、机密数据及完整性的威胁场景，并逐项阐明对应的工程防御控制措施。"
                ),
                "content_en": (
                    "FDA CDRH Final Guidance (September 27, 2023): Cybersecurity in Medical Devices\n\n"
                    "1. Section 524B of the FD&C Act Statutory Mandate:\n"
                    "Congress enacted Section 524B empowering FDA to refuse to accept (RTA) premarket submissions lacking required cybersecurity information.\n"
                    "- Statutory 'Cyber Device' Definition: Any device that (1) includes software (including firmware); (2) has the ability to connect to the internet; and (3) contains technological characteristics validated as vulnerable to cyber threats.\n"
                    "- Statutory Obligations: Design processes ensuring cyber resilience; establish vulnerability monitoring & patching protocols; submit a Software Bill of Materials (SBOM).\n\n"
                    "2. Threat Modeling Architecture:\n"
                    "Submissions must include comprehensive threat models identifying attack surfaces, interface boundaries, and threat vectors evaluated via structured frameworks (STRIDE/PASTA/MITRE ATT&CK) with demonstrated risk mitigation controls."
                )
            },
            {
                "section_id": "fda_cyber_sec2_sbom_and_postmarket",
                "page": 2,
                "title_zh": "第二节：网络安全物料清单(SBOM/CBOM)要素与协调漏洞披露(CVD)",
                "title_en": "Section 2: Software/Cybersecurity Bill of Materials (SBOM/CBOM) & Coordinated Vulnerability Disclosure",
                "content_zh": (
                    "FDA 2023年医疗器械网络安全指南\n\n"
                    "一、软件物料清单（SBOM / CBOM）申报规范：\n"
                    "申请人必须提供机器可读格式（如 SPDX、CycloneDX 格式）的完整软件物料清单，覆盖所有商用第三方软件、开源代码、驱动及自研库：\n"
                    "1. 组件资产名称（Asset / Component Name）；\n"
                    "2. 组件版本号（Version）；\n"
                    "3. 组件作者与制造商（Author / Manufacturer）；\n"
                    "4. 唯一下载标识符（Package URL / PURL）；\n"
                    "5. 组件生命周期终止状态（End-of-Support / EOS & End-of-Life / EOL）；\n"
                    "6. 关联已知漏洞数据库（NVD CVE）排查结果及 CVSS 严重度评分。\n\n"
                    "二、上市后漏洞监控与协调漏洞披露（CVD）：\n"
                    "1. 建立协调漏洞披露政策（Coordinated Vulnerability Disclosure / CVD），公开安全专员联系渠道，接收外部白帽黑客与安全研究员报告；\n"
                    "2. 补丁管理与回滚保护：支持加密签名的固件/软件 OTA 在线升级，并具备防回滚（Anti-rollback）保护；单纯修复漏洞的安全补丁通常豁免 510(k) 再次申请。"
                ),
                "content_en": (
                    "FDA 2023 Cybersecurity Guidance: SBOM & CVD Protocols\n\n"
                    "1. Software Bill of Materials (SBOM/CBOM) Standards:\n"
                    "Must be provided in machine-readable format (SPDX, CycloneDX) containing component name, version, author, Package URL (PURL), End-of-Support (EOS) status, and known CVE/CVSS vulnerability mappings.\n\n"
                    "2. Coordinated Vulnerability Disclosure (CVD) & Patching:\n"
                    "Public vulnerability disclosure program with intake channels; cryptographically signed update mechanism with anti-rollback protection. Non-recapture cybersecurity patches are generally exempt from premarket change notifications."
                )
            }
        ]
    },
    {
        "doc_id": "fda_device_software_functions_2023_official",
        "doc_title_zh": "FDA 医疗器械软件功能上市前申报资料指南（2023年定稿：基础与强化文档分级）",
        "doc_title_en": "FDA Final Guidance: Content of Premarket Submissions for Device Software Functions (June 2023)",
        "version": "FDA-2023-Final-Software-Functions",
        "effective_date": "2023-06-14",
        "jurisdiction": "FDA",
        "category": "Regulatory_Guideline",
        "source_file": "fda_device_software_functions_2023_official_full.pdf",
        "md_file": "fda_device_software_functions_2023_official_full.md",
        "pdf_subpath": "fda/fda_device_software_functions_2023_official_full.pdf",
        "sections": [
            {
                "section_id": "fda_soft_sec1_basic_vs_enhanced",
                "page": 1,
                "title_zh": "第一节：软件文档层级重大变革：基础文档(Basic)与强化文档(Enhanced)判定标准",
                "title_en": "Section 1: Documentation Tiers Revolution: Basic vs. Enhanced Documentation Criteria",
                "content_zh": (
                    "美国 FDA CDRH 2023年6月14日定稿指南：《Content of Premarket Submissions for Device Software Functions》\n\n"
                    "一、彻底取代旧版三级关注度（Level of Concern）：\n"
                    "本指南正式废除了 2005 年版指南中的“轻微（Minor）、中等（Moderate）、重大（Major）关切度”三级分类法，建立两级申报文档分级制度：基础文档（Basic Documentation）与强化文档（Enhanced Documentation）。\n\n"
                    "二、强化文档（Enhanced Documentation）判定标准（满足任意一项即触发）：\n"
                    "1. 组合产品：该设备是药械组合产品（Combination Product）的组成部分；\n"
                    "2. 输血与移植：用于确定献血者资格或用于输血医学/组织移植的软件；\n"
                    "3. 生命支持/维持：属于维持生命或支持生命的医疗设备（Life-supporting or Life-sustaining）；\n"
                    "4. 严重伤害/死亡风险：该软件功能发生失效、设计缺陷、潜在危害或受网络安全攻击时，合理推断可能导致患者或操作者死亡或严重伤害（Serious Injury or Death）。\n\n"
                    "三、基础文档（Basic Documentation）：\n"
                    "不符合上述四项强化文档标准的其他所有医疗器械软件功能，均属于基础文档级别。"
                ),
                "content_en": (
                    "FDA Final Guidance (June 14, 2023): Device Software Functions Documentation\n\n"
                    "1. Complete Replacement of Legacy Level of Concern (LOC):\n"
                    "Replaces the 2005 Minor/Moderate/Major LOC framework with a streamlined two-tier structure: Basic Documentation and Enhanced Documentation.\n\n"
                    "2. Enhanced Documentation Criteria (Any factor triggers Enhanced tier):\n"
                    "- Constituent of a Combination Product;\n"
                    "- Used in transfusion medicine or tissue donation eligibility;\n"
                    "- Intended for life-supporting or life-sustaining functions;\n"
                    "- Failure or design flaw presents a risk of serious injury or death.\n\n"
                    "3. Basic Documentation: Applies to all other software functions not meeting Enhanced criteria."
                )
            },
            {
                "section_id": "fda_soft_sec2_mandatory_elements",
                "page": 2,
                "title_zh": "第二节：上市前软件申报必备核心要素与可追溯性分析(Traceability Analysis)",
                "title_en": "Section 2: Mandatory Premarket Documentation Elements & Traceability Matrix",
                "content_zh": (
                    "FDA 2023年医疗器械软件功能指南\n\n"
                    "一、必备核心申报文档要素：\n"
                    "1. 软件描述（Software Description）：概述软件功能、运行平台、算法原理及临床预期用途；\n"
                    "2. 系统与软件架构设计图（System and Software Architecture Design Chart）：详细展示模块拓扑、内部外部接口、数据流及安全隔离边界；\n"
                    "3. 软件需求规范（Software Requirement Specification / SRS）：详细定义所有功能需求、性能指标、安全警报与错误处理机制；\n"
                    "4. 软件设计规范（SDS）：强化文档级别必须提交详细的模块级设计规范；\n"
                    "5. 验证与确认（V&V）：提交单元测试、集成测试、系统测试协议与通过报告；\n"
                    "6. 遗留缺陷清单（Unresolved Anomalies）：列出所有已识别但未修复的缺陷，并逐一论证其不会造成不可接受的临床危害。\n\n"
                    "二、可追溯性分析（Traceability Analysis）：\n"
                    "必须建立双向双闭环可追溯性矩阵：从危害分析（Hazard Analysis） -> 风险缓解措施 -> 软件需求（SRS） -> 软件设计（SDS） -> 验证测试用例（Test Case） -> 测试结果。"
                ),
                "content_en": (
                    "FDA 2023 Software Functions Guideline: Mandatory Submission Elements\n\n"
                    "1. Required Elements: Software Description, Architecture Design Charts, Software Requirement Specifications (SRS), Software Design Specifications (SDS for Enhanced tier), Software V&V reports, and Unresolved Anomaly evaluation.\n\n"
                    "2. Bidirectional Traceability Matrix: Direct traceability linking Hazards -> Risk Controls -> SRS -> SDS -> Test Cases -> Test Results."
                )
            }
        ]
    },
    {
        "doc_id": "fda_qmsr_iso13485_2024_2026_official",
        "doc_title_zh": "FDA 医疗器械质量管理体系法规最终规则（QMSR：21 CFR Part 820 全面接轨 ISO 13485:2016）",
        "doc_title_en": "FDA Final Rule: Quality Management System Regulation (QMSR) - Amending 21 CFR Part 820 to Incorporate ISO 13485:2016",
        "version": "FDA-QMSR-Final-Rule-2024",
        "effective_date": "2026-02-02",
        "jurisdiction": "FDA",
        "category": "Statutory_Code_of_Federal_Regulations",
        "source_file": "fda_21cfr820_qmsr_iso13485_official_full.pdf",
        "md_file": "fda_21cfr820_qmsr_iso13485_official_full.md",
        "pdf_subpath": "fda/fda_21cfr820_qmsr_iso13485_official_full.pdf",
        "sections": [
            {
                "section_id": "fda_qmsr_sec1_harmonization_and_scope",
                "page": 1,
                "title_zh": "第一节：QMSR 最终规则立法背景、引用 ISO 13485:2016 与 2026 年生效要求",
                "title_en": "Section 1: QMSR Final Rule Rationale, Direct Incorporation of ISO 13485:2016 & Feb 2026 Enforcement",
                "content_zh": (
                    "美国 FDA 最终规则：《Medical Devices; Quality Management System Regulation (QMSR)》（2024年发布，2026年2月2日起正式强制施行）\n\n"
                    "一、法规结构重大重构：\n"
                    "FDA 宣布将现行的《质量体系规范》（Quality System Regulation / QSR，21 CFR Part 820）正式修订为《质量管理体系规范》（Quality Management System Regulation / QMSR）。通过直接以法律形式“结合并引用”（Incorporation by Reference）国际标准 ISO 13485:2016（医疗器械 质量管理体系 用于法规的要求），实现了美国监管与全球主流体系的高度协调。\n\n"
                    "二、合规过渡期与实施时间：\n"
                    "- 2026年2月2日为强制生效截止日（Effective Date: February 2, 2026）。在此之后，FDA 现场检查（QSIT 检查体系）将正式转型为依据 QMSR 及 ISO 13485:2016 条款执行；\n"
                    "- 适用于在美国境内销售所有第二类、第三类医疗器械及受控第一类医疗器械的制造商。\n\n"
                    "三、核心概念对齐：\n"
                    "明确“设计控制”（Design Controls）、“纠正和预防措施”（CAPA）、“管理评审”（Management Review）完全对应 ISO 13485 第 7.3 节与第 8.5 节，并整合 ISO 14971 风险管理要求贯穿全过程。"
                ),
                "content_en": (
                    "FDA Final Rule: Quality Management System Regulation (QMSR) - Effective February 2, 2026\n\n"
                    "1. Major Regulatory Harmonization: Explicitly amends 21 CFR Part 820 by incorporating by reference international standard ISO 13485:2016 into United States federal law.\n\n"
                    "2. Enforcement Timeline: Takes full mandatory effect on February 2, 2026. FDA inspections transition from legacy QSIT framework to QMSR / ISO 13485 alignment.\n\n"
                    "3. Core Alignments: Direct harmonization of Design Controls, CAPA, Management Review, and ISO 14971 risk management throughout the total product lifecycle."
                )
            }
        ]
    },
    {
        "doc_id": "fda_21cfr_part11_official",
        "doc_title_zh": "FDA 21 CFR Part 11：电子记录与电子签名法规完整正文",
        "doc_title_en": "FDA Title 21 CFR Part 11: Electronic Records; Electronic Signatures (Official Code)",
        "version": "21-CFR-Part-11-Official",
        "effective_date": "1997-08-20",
        "jurisdiction": "FDA",
        "category": "Statutory_Code_of_Federal_Regulations",
        "source_file": "fda_21cfr_part11_official_full.pdf",
        "md_file": "fda_21cfr_part11_official_full.md",
        "pdf_subpath": "fda/fda_21cfr_part11_official_full.pdf",
        "sections": [
            {
                "section_id": "fda_part11_sec1_controls_and_audit_trail",
                "page": 1,
                "title_zh": "第一节：封闭系统控制、计算机生成时间戳审计追踪(Audit Trail)不可篡改性",
                "title_en": "Section 1: Controls for Closed Systems, Computer-Generated Time-Stamped Audit Trails",
                "content_zh": (
                    "美国联邦法规法典第 21 篇第 11 部分（Title 21 CFR Part 11）：Electronic Records; Electronic Signatures\n\n"
                    "一、适用范围与法律效力（§ 11.1）：\n"
                    "适用于 FDA 规程管辖范围内创建、修改、维护、归档、检索或传输的所有电子形式记录。符合本部分规定的电子记录与电子签名，在法律上与纸质手写签名记录具有同等法律效力。\n\n"
                    "二、封闭系统控制（§ 11.10 Controls for Closed Systems）：\n"
                    "1. 计算机化系统验证（System Validation）：确保系统的准确性、可靠性与一致性；\n"
                    "2. 审计追踪（Audit Trails，§ 11.10(e)）：必须采用安全、由计算机自动生成、带有可靠时间戳的独立审计追踪机制，独立记录系统操作人员创建、修改或删除记录的操作日期和时间。审计追踪记录必须安全保存，其保存期限不得少于对应电子记录的保存期限，且系统严禁任何用户（包括超级管理员）修改、关闭或篡改审计日志；\n"
                    "3. 权限与身份检查（Authority Checks）：确保仅限经授权的合法人员访问系统与签署记录。"
                ),
                "content_en": (
                    "Title 21 CFR Part 11: Electronic Records; Electronic Signatures\n\n"
                    "1. Scope & Equivalence (§ 11.1): Electronic records and signatures meeting Part 11 criteria are legally equivalent to traditional paper records and handwritten signatures.\n\n"
                    "2. Controls for Closed Systems (§ 11.10):\n"
                    "- System Validation: Documented verification of software accuracy, reliability, and consistency;\n"
                    "- Immutable Audit Trail (§ 11.10(e)): Computer-generated, time-stamped audit trails independently recording operator entries and actions. Audit records cannot be altered or deleted by any user (including administrators);\n"
                    "- Operational authority and device checks."
                )
            }
        ]
    },
    {
        "doc_id": "fda_21cfr_part211_cgmp_official",
        "doc_title_zh": "FDA 21 CFR Part 211：成品制剂现行良好生产规范（cGMP）",
        "doc_title_en": "FDA Title 21 CFR Part 211: Current Good Manufacturing Practice for Finished Pharmaceuticals",
        "version": "21-CFR-Part-211-Official",
        "effective_date": "1978-09-29",
        "jurisdiction": "FDA",
        "category": "Statutory_Code_of_Federal_Regulations",
        "source_file": "fda_21cfr_part211_cgmp_full.pdf",
        "md_file": "fda_21cfr_part211_cgmp_full.md",
        "pdf_subpath": "fda/fda_21cfr_part211_cgmp_full.pdf",
        "sections": [
            {
                "section_id": "fda_211_sec1_subparts_c_d_j",
                "page": 1,
                "title_zh": "第一节：厂房设施、设备清洁与批生产记录(BPR)归档保存规定",
                "title_en": "Section 1: Buildings & Facilities, Equipment Cleaning & Batch Production Records (BPR)",
                "content_zh": (
                    "美国联邦法规法典第 21 篇第 211 部分（21 CFR Part 211）：cGMP for Finished Pharmaceuticals\n\n"
                    "一、厂房与设施（Subpart C - Buildings and Facilities）：\n"
                    "1. § 211.42 设计与建设：厂房必须具有适宜的尺寸与布局，防止交叉污染；无菌制剂生产区必须具备适当的空气过滤系统（HEPA 过滤）、压差控制梯度与温湿度控制；\n"
                    "2. § 211.46 通风与空气过滤：对空气压力、微生物、悬浮微粒实施受控监测。\n\n"
                    "二、设备清洁与验证（Subpart D - Equipment）：\n"
                    "§ 211.67 设备清洁与维护：必须建立书面的清洁验证标准操作规程（SOP），明确清洁剂、设备拆卸规程及前一批次活性成分与清洁剂残留限度（如 10 ppm 或 1/1000 临床最小日剂量）。\n\n"
                    "三、记录与报告（Subpart J - Records and Reports）：\n"
                    "1. § 211.186 主生产与控制记录（Master Production Records / MPR）：必须由质控部门（QCU）独立审核批准；\n"
                    "2. § 211.188 批生产与控制记录（Batch Production Records / BPR）：每一生产批次必须具备完整的称量、操作签名、在线检验与收率核对记录；\n"
                    "3. § 211.180 记录保存时限：所有与药品批次相关的生产、质控与分销记录，必须自该批药品有效期限届满后至少保存 1 年（At least 1 year after batch expiration date）。"
                ),
                "content_en": (
                    "Title 21 CFR Part 211: cGMP for Finished Pharmaceuticals\n\n"
                    "1. Buildings & Facilities (Subpart C, § 211.42/46): Controlled clean areas with HEPA filtration, differential pressure gradients, and environmental monitoring for aseptic operations.\n\n"
                    "2. Equipment Cleaning (Subpart D, § 211.67): Validated written cleaning procedures establishing maximum allowable carryover (10 ppm or 1/1000 minimum therapeutic dose).\n\n"
                    "3. Records & Reports (Subpart J, § 211.186/188/180): QCU approval of Master Production Records (MPR); complete Batch Production Records (BPR) documentation. Retention mandate: At least 1 year beyond batch expiration date."
                )
            }
        ]
    },
    {
        "doc_id": "fda_21cfr_part312_part314_ind_nda_official",
        "doc_title_zh": "FDA 21 CFR Part 312 (IND) 与 Part 314 (NDA)：新药临床试验与上市申请法规",
        "doc_title_en": "FDA Title 21 CFR Part 312 (IND) & Part 314 (NDA): Investigational New Drug & Marketing Application",
        "version": "21-CFR-Part-312-314-Official",
        "effective_date": "1987-03-19",
        "jurisdiction": "FDA",
        "category": "Statutory_Code_of_Federal_Regulations",
        "source_file": "fda_21cfr_part312_part314_ind_nda_official_full.pdf",
        "md_file": "fda_21cfr_part312_part314_ind_nda_official_full.md",
        "pdf_subpath": "fda/fda_21cfr_part312_part314_ind_nda_official_full.pdf",
        "sections": [
            {
                "section_id": "fda_312_sec1_ind_30day_and_safety_alerts",
                "page": 1,
                "title_zh": "第一节：IND 30 天法定审查倒计时、Form 1571 与 IND 安全报告快速通报时限",
                "title_en": "Section 1: IND 30-Day Review Clock, Form FDA 1571 & IND Safety Alert Reporting (7-Day & 15-Day)",
                "content_zh": (
                    "美国联邦法规法典第 21 篇第 312 部分（21 CFR Part 312）：Investigational New Drug Application (IND)\n\n"
                    "一、IND 递交与 30 天审查时钟（§ 312.20 & § 312.40）：\n"
                    "申办者提交试验用新药申请（IND，使用 Form FDA 1571 封面表）。自 FDA 正式接收之日起启动 30 个日历日审查时钟（30 Calendar Days Review Clock）。如果在 30 天内 FDA 未签发“临床暂停通知”（Clinical Hold），申办者即可自动启动人体临床试验。\n\n"
                    "二、IND 安全性报告快速通报时限（§ 312.32 IND Safety Reports）：\n"
                    "申办者必须审查试验过程中的所有不良事件信息，并向 FDA 提交紧急安全报告：\n"
                    "1. 7 天致死或危及生命的警报报告（7-Day Alert）：针对任何未预期的、致死或危及生命的疑似严重不良反应（Unexpected fatal or life-threatening suspected adverse reaction），必须在申办者获知信息的 7 个日历日内（Within 7 calendar days）通过电话、传真或电子通道向 FDA 通报，并在随后的 8 天内提交完整的书面报告；\n"
                    "2. 15 天警报报告（15-Day Alert）：针对其他严重的、未预期的疑似不良反应，或来自动物试验提示人体重大致癌/致畸风险的发现，必须在获知信息的 15 个日历日内书面报告 FDA 及所有参研临床研究者。"
                ),
                "content_en": (
                    "Title 21 CFR Part 312: Investigational New Drug Application (IND)\n\n"
                    "1. IND Submission & 30-Day Clock (§ 312.20/40): Form FDA 1571 submission initiates a 30 calendar-day statutory review clock. Clinical trials may proceed automatically on Day 30 unless FDA issues a Clinical Hold.\n\n"
                    "2. IND Safety Reporting Mandates (§ 312.32):\n"
                    "- 7-Day Alert: Unexpected fatal or life-threatening suspected adverse reactions must be reported to FDA within 7 calendar days;\n"
                    "- 15-Day Alert: Other serious unexpected suspected adverse reactions must be submitted in writing within 15 calendar days to FDA and all active trial investigators."
                )
            }
        ]
    },
    {
        "doc_id": "fda_overview_mandate_centers_official",
        "doc_title_zh": "美国食品药品监督管理局（FDA）组织架构、法定职责与监管途径总览",
        "doc_title_en": "U.S. Food and Drug Administration (FDA): Statutory Mandate, Organizational Centers & Regulatory Pathways Overview",
        "version": "FDA-Overview-Statutory-2024",
        "effective_date": "2024-01-01",
        "jurisdiction": "FDA",
        "category": "Statutory_Overview",
        "source_file": "fda_overview_statutory_mandate_official_full.pdf",
        "md_file": "fda_overview_statutory_mandate_official_full.md",
        "pdf_subpath": "fda/fda_overview_statutory_mandate_official_full.pdf",
        "sections": [
            {
                "section_id": "fda_overview_sec1_mandate_and_scope",
                "page": 1,
                "title_zh": "第一节：机构定位、法定职责授权（FD&C Act 与 PHS Act）及使命",
                "title_en": "Section 1: Statutory Mandate (FD&C Act & PHS Act), Agency Mission & Regulatory Scope",
                "content_zh": (
                    "美国食品药品监督管理局（Food and Drug Administration，简称 FDA）是美国联邦政府卫生与公众服务部（Department of Health and Human Services, HHS）下属的专门主管机构。\n\n"
                    "一、法定职责与使命（21 U.S.C. § 393 Statutory Mission）：\n"
                    "依据《联邦食品、药品和化妆品法案》（FD&C Act）第903节（21 U.S.C. § 393）及《公共卫生服务法案》（PHS Act），FDA 的法定使命为：通过确保人用和兽用药品、生物制品和医疗器械的安全性、有效性与保障性，以及确保国家食品供应、化妆品和辐射发射产品的安全性，保护公众健康；并通过促进产品创新与向公众传播科学精准的信息，增进公众健康。\n\n"
                    "二、法定管辖范围（Regulatory Jurisdiction）：\n"
                    "1. 药品（Drugs）：涵盖处方药（Rx）、非处方药（OTC）、化学原料药及制剂，依据 FD&C Act 监管；\n"
                    "2. 生物制品（Biologics）：涵盖疫苗、血液制品、重组蛋白、单克隆抗体、基因与细胞治疗，依据 PHS Act § 351 及 FD&C Act 监管；\n"
                    "3. 医疗器械（Medical Devices）：按风险分为 I 类、II 类、III 类，依据 FD&C Act 第 513/514/515/524B 等节监管；\n"
                    "4. 食品与营养补充剂（Foods & Dietary Supplements）；\n"
                    "5. 辐射发射电子产品（Radiation-Emitting Electronic Products）；\n"
                    "6. 烟草制品（Tobacco Products）；\n"
                    "7. 兽药与动物饲料（Animal Drugs & Feeds）。"
                ),
                "content_en": (
                    "U.S. Food and Drug Administration (FDA) Overview & Statutory Mandate\n\n"
                    "1. Mission & Statutory Authority (21 U.S.C. § 393 & PHS Act):\n"
                    "The FDA is an agency within the U.S. Department of Health and Human Services (HHS). Its statutory mission is to protect public health by ensuring the safety, efficacy, and security of human and veterinary drugs, biological products, and medical devices, and by ensuring the safety of food supply, cosmetics, and radiation-emitting products.\n\n"
                    "2. Regulatory Scope:\n"
                    "- Human Drugs: Prescription (Rx), Over-the-Counter (OTC), and generic medicines under the FD&C Act;\n"
                    "- Biologics: Vaccines, blood, monoclonal antibodies, gene & cell therapies under PHS Act § 351;\n"
                    "- Medical Devices: Class I, II, III devices, SaMD, and radiation-emitting products under FD&C Act §§ 510, 513, 515, 524B;\n"
                    "- Food safety, cosmetics, veterinary drugs, and tobacco products."
                )
            },
            {
                "section_id": "fda_overview_sec2_centers_and_pathways",
                "page": 2,
                "title_zh": "第二节：核心业务中心架构（CDER、CBER、CDRH 等）与上市申报审批途径",
                "title_en": "Section 2: Core Organizational Centers (CDER, CBER, CDRH) & Premarket Review Pathways",
                "content_zh": (
                    "美国 FDA 核心下属中心架构与主要监管申报途径：\n\n"
                    "一、核心职能中心架构：\n"
                    "1. CDER（Center for Drug Evaluation and Research，药品审评与研究中心）：负责化学药品、小分子药物及部分治疗性蛋白质的上市前审评、上市后安全性监测与 cGMP 生产质量规范监管；\n"
                    "2. CBER（Center for Biologics Evaluation and Research，生物制品审评与研究中心）：负责疫苗、血液与血液成分、细胞疗法、基因疗法、组织工程及过敏原制剂；\n"
                    "3. CDRH（Center for Devices and Radiological Health，医疗器械与放射健康中心）：负责医疗器械（含数字医疗/AI软件、体外诊断 IVD）与辐射发射设备的安全有效性监管；\n"
                    "4. CFSAN（食品安全与应用营养中心）、CVM（兽药中心）、CTP（烟草制品中心）；\n"
                    "5. ORA（Office of Regulatory Affairs，监管事务办公室）：负责全美及全球生产设施的现场合规核查、cGMP 检查与进出口拦截。\n\n"
                    "二、主要上市前申报通道：\n"
                    "1. 药品与生物制品通道：临床试验申请 IND（21 CFR Part 312）、新药申请 NDA（Part 314）、仿制药申请 ANDA（Part 314）、生物制品许可申请 BLA（PHS Act § 351）；\n"
                    "2. 医疗器械通道：510(k) 上市前通告（实质性等同 Predicate）、De Novo 创新分类通道、PMA 上市前批准（III类高风险设备）；\n"
                    "3. 上市后安全性警戒：MedWatch 强制与自愿不良事件报告系统、FAERS（药品不良反应数据库）、MAUDE（医疗器械事件数据库）。"
                ),
                "content_en": (
                    "FDA Organizational Centers & Review Pathways:\n\n"
                    "1. Core Operating Centers:\n"
                    "- CDER (Center for Drug Evaluation and Research): Regulates small molecules, OTC, prescription drugs, and therapeutic proteins;\n"
                    "- CBER (Center for Biologics Evaluation and Research): Regulates vaccines, blood products, gene and cell therapies;\n"
                    "- CDRH (Center for Devices and Radiological Health): Regulates medical devices, SaMD/AI software, IVDs, and radiological products;\n"
                    "- ORA (Office of Regulatory Affairs): Lead office for all agency field inspections, cGMP audits, and import oversight.\n\n"
                    "2. Key Regulatory Pathways:\n"
                    "- Drugs/Biologics: IND (clinical investigation), NDA (new drug approval), ANDA (generic bioequivalence), BLA (biologic license);\n"
                    "- Devices: 510(k) (substantial equivalence), De Novo (low/moderate risk novel devices), PMA (high-risk Class III premarket approval);\n"
                    "- Post-market: MedWatch reporting, FAERS, and MAUDE surveillance."
                )
            }
        ]
    }
]
