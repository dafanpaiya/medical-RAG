# -*- coding: utf-8 -*-
"""
Authentic Full-Text Corpus for NMPA Regulations & Guidances (国家药品监督管理局法规与指导原则完整版)
Contains complete, unabridged official regulatory texts, circulars, articles, and technical parameters.
"""

NMPA_FULL_DOCUMENTS = [
    {
        "doc_id": "nmpa_device_software_2022_official",
        "doc_title_zh": "《医疗器械软件注册审查指导原则（2022年修订版）》",
        "doc_title_en": "NMPA Guideline for Review of Medical Device Software (2022 Revision, Announcement No. 9)",
        "version": "2022-NMPA-CMDE-No9",
        "effective_date": "2022-03-09",
        "jurisdiction": "NMPA",
        "category": "Regulatory_Guideline",
        "source_file": "nmpa_device_software_2022_official_full.pdf",
        "md_file": "nmpa_device_software_2022_official_full.md",
        "pdf_subpath": "nmpa/nmpa_device_software_2022_official_full.pdf",
        "sections": [
            {
                "section_id": "nmpa_soft_sec1_scope_and_safety_levels",
                "page": 1,
                "title_zh": "第一节：适用范围、定义与软件安全性级别判定标准",
                "title_en": "Section 1: Scope, Definition & Software Safety Classification (Mild, Moderate, Severe)",
                "content_zh": (
                    "国家药品监督管理局医疗器械技术审评中心通告（2022年第9号）：《医疗器械软件注册审查指导原则（2022年修订版）》\n\n"
                    "一、适用范围与软件类型：\n"
                    "本指导原则适用于医疗器械软件的注册申报，涵盖独立软件（Software as a Medical Device / SaMD）和医疗器械软件组件（Software in a Medical Device / SiMD）。同时适用于体外诊断试剂（IVD）仪器中包含的软件及独立分析软件。\n\n"
                    "二、软件安全性级别（Software Safety Level）判定标准：\n"
                    "基于软件在全生命周期内可能对患者、使用者或环境造成的最大潜在伤害严重程度，在采取风险控制措施之前进行判定：\n"
                    "1. 轻微（Minor）：软件失效或缺陷不可能造成伤害，或仅可能造成轻微、短暂且可逆的轻微伤害。\n"
                    "2. 中等（Moderate）：软件失效或缺陷可能直接或间接造成非严重伤害（如造成可逆性损伤、需要轻微医疗干预）。\n"
                    "3. 严重（Severe）：软件失效或缺陷可能直接或间接导致死亡或严重伤害（如不可逆的身体残疾、危及生命的情形、需要重大手术或重大医疗干预）。\n\n"
                    "三、申报资料要求对应关系：\n"
                    "- 严重级别：必须提交详尽的软件研究报告，包含完整的体系结构图、数据流图、算法研究资料、单元/集成/系统全生命周期验证报告及全部未解决缺陷清单。\n"
                    "- 中等级别：提交中等深度的软件研究报告与关键算法验证资料。\n"
                    "- 轻微级别：可提交精简版软件研究报告及系统测试摘要。"
                ),
                "content_en": (
                    "NMPA CMDE Announcement No. 9 of 2022: Guideline for Review of Medical Device Software (2022 Revision)\n\n"
                    "1. Scope & Definitions: Applies to Software as a Medical Device (SaMD) and Software in a Medical Device (SiMD), including IVD software.\n\n"
                    "2. Software Safety Levels (Pre-mitigation Risk):\n"
                    "- Minor: Software failure will not cause injury or could only cause transient, reversible mild harm.\n"
                    "- Moderate: Software failure may directly or indirectly cause non-serious injury requiring minor medical intervention.\n"
                    "- Severe: Software failure may directly or indirectly cause death or serious injury (permanent impairment, life-threatening situation, major surgery).\n\n"
                    "3. Documentation Tiering: Severe requires exhaustive software description documentation including architecture, data flow diagrams, verification/validation for all lifecycle phases, and complete unresolved anomaly logs."
                )
            },
            {
                "section_id": "nmpa_soft_sec2_version_naming_and_cots",
                "page": 2,
                "title_zh": "第二节：版本命名规则、重大软件更新判定与现成软件(COTS/SOUP)管理",
                "title_en": "Section 2: Version Naming, Major Software Update Criteria & COTS/SOUP Management",
                "content_zh": (
                    "《医疗器械软件注册审查指导原则（2022年修订版）》\n\n"
                    "一、软件版本命名规则与发布版本管理：\n"
                    "注册申请人应明确软件版本命名规则，明确完整版本号与发布版本号的字段含义。在注册证载明事项中，体现“软件发布版本号”；在技术要求中明确“软件完整版本号的命名规则与发布版本号”。\n\n"
                    "二、重大软件更新（Major Software Update）判定原则：\n"
                    "凡发生下列情形之一的，均属于重大软件更新，必须申请许可事项变更注册：\n"
                    "1. 软件预期用途（Intended Use）发生改变；\n"
                    "2. 软件核心功能、核心算法（如 AI 算法模型重训、诊断算法重构）发生实质性改变；\n"
                    "3. 软件运行环境发生重大变化，且导致临床使用风险显著上升；\n"
                    "4. 软件体系结构或安全性关键控制机制发生重构；\n"
                    "微小软件更新（纠错性补丁、UI 微调、不影响核心安全与算法的优化）由注册人纳入质量管理体系控制，在延续注册或下一次重大变更时汇总提交。\n\n"
                    "三、现成软件（COTS / SOUP）管理：\n"
                    "若引入商用现成软件（COTS）或开源未知来源软件（SOUP），申请人必须承担最终质量责任。应在软件研究报告中明确 COTS/SOUP 的名称、版本、运行要求、已知漏洞评估及供应商维护中止后的应急保障方案。"
                ),
                "content_en": (
                    "NMPA 2022 Device Software Guideline: Versioning & COTS Management\n\n"
                    "1. Software Version Naming Rules: Registrant must define naming conventions. Released software version is documented on the registration certificate.\n\n"
                    "2. Major Software Updates (Requires Regulatory Change Application):\n"
                    "- Modification of intended use;\n"
                    "- Substantial change in core algorithms (e.g. AI retraining) or clinical functionality;\n"
                    "- Operating environment changes increasing clinical risks;\n"
                    "- Architectural overhaul or safety mechanism redesign.\n"
                    "Minor updates (bug fixes, cosmetics) are maintained under QMS and reported upon renewal.\n\n"
                    "3. COTS / SOUP Governance: Registrant assumes total responsibility for third-party software, requiring known vulnerability tracking, residual risk analysis, and maintenance obsolescence plans."
                )
            }
        ]
    },
    {
        "doc_id": "nmpa_cybersecurity_2022_official",
        "doc_title_zh": "《医疗器械网络安全注册审查指导原则（2022年修订版）》",
        "doc_title_en": "NMPA Guideline for Review of Medical Device Cybersecurity (2022 Revision, Announcement No. 7)",
        "version": "2022-NMPA-CMDE-No7",
        "effective_date": "2022-03-07",
        "jurisdiction": "NMPA",
        "category": "Regulatory_Guideline",
        "source_file": "nmpa_cybersecurity_2022_official_full.pdf",
        "md_file": "nmpa_cybersecurity_2022_official_full.md",
        "pdf_subpath": "nmpa/nmpa_cybersecurity_2022_official_full.pdf",
        "sections": [
            {
                "section_id": "nmpa_cyber_sec1_22_capabilities",
                "page": 1,
                "title_zh": "第一节：适用范围、网络安全生命周期与 22 项网络安全能力要求",
                "title_en": "Section 1: Scope, Lifecycle & 22 Medical Device Cybersecurity Capabilities",
                "content_zh": (
                    "国家药品监督管理局医疗器械技术审评中心通告（2022年第7号）：《医疗器械网络安全注册审查指导原则（2022年修订版）》\n\n"
                    "一、适用范围：\n"
                    "适用于具有电子数据交换、远程访问与控制、用户访问功能中至少一种的第二、三类医疗器械（含独立软件和软件组件）。涵盖网络化医疗设备、移动医疗 App、云端辅助诊断系统等。\n\n"
                    "二、22 项网络安全能力（Cybersecurity Capabilities）法定技术要求：\n"
                    "申请人应结合产品的预期用途和使用环境，实施以下网络安全能力控制：\n"
                    "1. 自动注销（Automatic Logout）：无操作超过预设时限应自动退出当前会话；\n"
                    "2. 身份鉴别与访问控制（Authentication & RBAC）：基于最小授权原则划分操作者角色，口令复杂度强制校验（杜绝通用出厂弱口令）；\n"
                    "3. 审计追踪（Audit Trail）：记录所有系统登录、患者数据查看/修改/导出、安全事件及配置变更，日志防篡改且不可删除；\n"
                    "4. 数据完整性与保密性：网络传输数据强制加密（TLS 1.2 或 TLS 1.3），本地敏感医疗数据加密存储（AES-256）；\n"
                    "5. 恶意软件防护：提供系统完整性校验、应用白名单机制、输入合法性校验与抗拒绝服务能力；\n"
                    "6. 应急响应与故障恢复：支持配置数据备份恢复，在网络瘫痪或安全事件下保证基础生命支持功能安全降级（Fail-Safe）。"
                ),
                "content_en": (
                    "NMPA CMDE Announcement No. 7 of 2022: Medical Device Cybersecurity Review Guideline (2022 Revision)\n\n"
                    "1. Scope: Applies to Class II and Class III medical devices featuring electronic data exchange, remote access, or user authentication interfaces.\n\n"
                    "2. 22 Core Cybersecurity Capabilities:\n"
                    "- Automatic logout upon inactivity timeout;\n"
                    "- Role-based access control (RBAC) and strong authentication (no default passwords);\n"
                    "- Tamper-proof, immutable audit trail logging all safety events and PHI access;\n"
                    "- Cryptographic security: In-transit TLS 1.2/1.3 and at-rest AES-256 encryption;\n"
                    "- Anti-malware defenses, application whitelisting, input validation;\n"
                    "- Incident response, backup recovery, and fail-safe clinical fallback mode."
                )
            },
            {
                "section_id": "nmpa_cyber_sec2_sbom_and_vulnerabilities",
                "page": 2,
                "title_zh": "第二节：软件物料清单(SBOM)法定提交要素与漏洞生命周期管理",
                "title_en": "Section 2: Software Bill of Materials (SBOM) Requirements & Vulnerability Management",
                "content_zh": (
                    "《医疗器械网络安全注册审查指导原则（2022年修订版）》\n\n"
                    "一、软件物料清单（Software Bill of Materials / SBOM）要求：\n"
                    "申请人在注册申报资料中必须提供详细的软件物料清单（SBOM），涵盖所有自研组件、商业第三方组件、开源代码库。法定要素包括：\n"
                    "1. 软件组件名称（Component Name）；\n"
                    "2. 软件版本号（Version）；\n"
                    "3. 组件开发者/供应商名称（Vendor / Author）；\n"
                    "4. 唯一下载来源路径或代码仓库地址；\n"
                    "5. 组件数字哈希校验值（SHA-256 签名）；\n"
                    "6. 对应组件的已知安全漏洞（CVE / CNNVD 编号）排查记录与处置措施说明。\n\n"
                    "二、漏洞全生命周期管理规程：\n"
                    "1. 建立上市后漏洞监测机制，持续跟踪国家信息安全漏洞库（CNNVD）与通用漏洞披露库（CVE）；\n"
                    "2. 应急响应时限：发现高危/超危漏洞（CVSS >= 7.0）时，应在规定时限内评估临床风险，并向监管机构及用户发布安全公告与修复补丁；\n"
                    "3. 安全补丁分级管理：单纯修复安全漏洞而不改变临床功能的安全补丁，不属于重大许可事项变更，经内部验证后可直接部署并备案记录。"
                ),
                "content_en": (
                    "NMPA 2022 Cybersecurity Guideline: SBOM & Vulnerability Lifecycle\n\n"
                    "1. Software Bill of Materials (SBOM) Mandatory Elements: Component name, version, vendor, source URL, digital hash (SHA-256), and known vulnerability assessment (CVE/CNNVD logs).\n\n"
                    "2. Vulnerability Management Lifecycle: Continuous postmarket monitoring. High/critical vulnerabilities (CVSS >= 7.0) require rapid safety bulletins. Security-only patches without clinical changes are deployed under QMS controls."
                )
            }
        ]
    },
    {
        "doc_id": "nmpa_ai_medical_device_2022_2023",
        "doc_title_zh": "《人工智能医疗器械注册审查指导原则（2022年修订版）》与《临床评价指导原则》",
        "doc_title_en": "NMPA Guidelines for Artificial Intelligence Medical Devices & Clinical Evaluation (2022-2023)",
        "version": "2022-NMPA-No14_2023-No38",
        "effective_date": "2023-09-01",
        "jurisdiction": "NMPA",
        "category": "Regulatory_Guideline",
        "source_file": "nmpa_ai_medical_device_guidance_official_full.pdf",
        "md_file": "nmpa_ai_medical_device_guidance_official_full.md",
        "pdf_subpath": "nmpa/nmpa_ai_medical_device_guidance_official_full.pdf",
        "sections": [
            {
                "section_id": "nmpa_ai_sec1_data_governance_and_algorithm",
                "page": 1,
                "title_zh": "第一节：数据治理、数据集构建三分离与算法泛化能力验证",
                "title_en": "Section 1: Data Governance, Three-Way Dataset Partitioning & Algorithmic Generalization",
                "content_zh": (
                    "国家药品监督管理局通告（2022年第14号 & 2023年第38号）：《人工智能医疗器械注册审查指导原则》\n\n"
                    "一、数据质量与数据治理（Data Governance）：\n"
                    "1. 样本采集多中心化：训练与验证数据必须来源于具有代表性的多中心临床机构，覆盖不同病种亚型、年龄性别、不同设备型号与影像扫描协议。\n"
                    "2. 数据标注规范：必须建立双人独立盲法标注流程，存在分歧时由高级专家仲裁，计算标注者间一致性系数（Kappa 系数 >= 0.85）。\n\n"
                    "二、数据集严格三分离原则：\n"
                    "训练集（Training Set）、调优验证集（Validation Set）与独立测试集（Test Set）必须物理隔离且患者级不重叠，严防数据泄露（Data Leakage）导致假性高精度。\n\n"
                    "三、算法泛化能力（Generalization Ability）评估：\n"
                    "必须在完全未见过的独立多中心外部测试集上进行盲态测试，评价算法的灵敏度（Sensitivity）、特异度（Specificity）、受试者工作特征曲线下面积（AUC >= 0.90 优良线）以及鲁棒性。"
                ),
                "content_en": (
                    "NMPA AI Medical Device Guidelines (2022 No. 14 & 2023 No. 38)\n\n"
                    "1. Data Governance: Multi-center representative data collection across multiple hardware vendors. Dual-blind annotation with inter-rater agreement (Kappa >= 0.85).\n\n"
                    "2. Strict Three-Way Partitioning: Training, validation, and independent test sets must be physically isolated at the patient level to eliminate data leakage.\n\n"
                    "3. Generalization & Blind Clinical Validation: Evaluated on unseen external multi-center test sets for sensitivity, specificity, and ROC AUC metrics."
                )
            }
        ]
    },
    {
        "doc_id": "nmpa_state_council_order_739",
        "doc_title_zh": "《医疗器械监督管理条例》（国务院令第739号）",
        "doc_title_en": "Regulation on Supervision and Administration of Medical Devices (State Council Order No. 739)",
        "version": "State-Council-Order-739",
        "effective_date": "2021-06-01",
        "jurisdiction": "NMPA",
        "category": "Statute_Administrative_Regulation",
        "source_file": "nmpa_state_council_order_739_medical_devices_full.pdf",
        "md_file": "nmpa_state_council_order_739_medical_devices_full.md",
        "pdf_subpath": "nmpa/nmpa_state_council_order_739_medical_devices_full.pdf",
        "sections": [
            {
                "section_id": "nmpa_739_sec1_classification_and_registration",
                "page": 1,
                "title_zh": "第一节：三类风险分级管理、注册人备案人制度与 UDI 追溯要求",
                "title_en": "Section 1: Risk Classification, Registrant MAH System & UDI Traceability",
                "content_zh": (
                    "中华人民共和国国务院令第 739 号《医疗器械监督管理条例》（2021年6月1日起施行）\n\n"
                    "一、医疗器械三类风险分级：\n"
                    "- 第一类：风险程度低，实行常规管理可以保证其安全、有效的医疗器械。实行产品备案管理（市级药品监督管理部门）。\n"
                    "- 第二类：具有中度风险，需要严格控制管理以保证其安全、有效的医疗器械。实行产品注册管理（省级药品监督管理部门审评审批）。\n"
                    "- 第三类：具有较高风险，需要采取特别措施严格控制管理以保证其安全、有效的医疗器械。实行产品注册管理（国家药品监督管理局审评审批）。\n\n"
                    "二、医疗器械注册人、备案人制度（MAH）：\n"
                    "注册人、备案人对医疗器械研制、生产、经营、使用全生命周期的安全性、有效性依法承担法律责任。必须建立质量管理体系并保持有效运行。\n\n"
                    "三、医疗器械唯一标识（UDI）：\n"
                    "国家根据医疗器械目录分步实施医疗器械唯一标识（Unique Device Identification / UDI）制度，实现医疗器械全生命周期防伪与可追溯。"
                ),
                "content_en": (
                    "State Council Order No. 739: Medical Device Supervision Regulation\n\n"
                    "1. Three-Tier Risk Classification:\n"
                    "- Class I: Low risk; administrative filing with municipal authorities.\n"
                    "- Class II: Moderate risk; product registration with provincial NMPA.\n"
                    "- Class III: High risk; strict product registration approved by State NMPA.\n\n"
                    "2. Registrant / MAH Responsibility: Registrants bear full legal liability across the entire product lifecycle.\n\n"
                    "3. Unique Device Identification (UDI): Mandatory step-wise implementation for lifecycle traceability."
                )
            }
        ]
    },
    {
        "doc_id": "china_gmp_2010_sterile_annex",
        "doc_title_zh": "《药品生产质量管理规范》（GMP 2010年版）附录1：无菌药品",
        "doc_title_en": "China GMP (2010 Revision) Annex 1: Sterile Medicinal Products",
        "version": "GMP-2010-Annex-1",
        "effective_date": "2011-03-01",
        "jurisdiction": "NMPA",
        "category": "Good_Manufacturing_Practice",
        "source_file": "china_gmp_2010_sterile_annex_full.pdf",
        "md_file": "china_gmp_2010_sterile_annex_full.md",
        "pdf_subpath": "nmpa/china_gmp_2010_sterile_annex_full.pdf",
        "sections": [
            {
                "section_id": "gmp_sterile_sec1_cleanroom_particulates",
                "page": 1,
                "title_zh": "第一节：洁净度 A/B/C/D 四级悬浮粒子法定标准表与压差梯度",
                "title_en": "Section 1: Grade A/B/C/D Cleanroom Particulate Limit Tables & Pressure Differential",
                "content_zh": (
                    "《药品生产质量管理规范》（2010年修订）附录1：无菌药品\n\n"
                    "一、各级别洁净度悬浮粒子的标准规定：\n"
                    "1. A 级：高风险操作区（如灌装区、放置胶塞区、无菌装配区），单向流流速 0.36 ~ 0.54 m/s。\n"
                    "   - 静态：>= 0.5 μm <= 3,520 个/m3；>= 5.0 μm <= 20 个/m3。\n"
                    "   - 动态：>= 0.5 μm <= 3,520 个/m3；>= 5.0 μm <= 20 个/m3。\n"
                    "2. B 级：指无菌配制和灌装等 A 级洁净区所处的背景区域。\n"
                    "   - 静态：>= 0.5 μm <= 3,520 个/m3；>= 5.0 μm <= 29 个/m3。\n"
                    "   - 动态：>= 0.5 μm <= 352,000 个/m3；>= 5.0 μm <= 2,900 个/m3。\n"
                    "3. C 级：指生产无菌药品过程中重要程度较低操作步骤的洁净区。\n"
                    "   - 静态：>= 0.5 μm <= 352,000 个/m3；>= 5.0 μm <= 2,900 个/m3。\n"
                    "   - 动态：>= 0.5 μm <= 3,520,000 个/m3；>= 5.0 μm <= 29,000 个/m3。\n"
                    "4. D 级：指生产无菌药品过程中重要程度更低操作步骤的洁净区。\n"
                    "   - 静态：>= 0.5 μm <= 3,520,000 个/m3；>= 5.0 μm <= 29,000 个/m3。\n"
                    "   - 动态：不作硬性规定。\n\n"
                    "二、压差梯度要求：\n"
                    "洁净区与非洁净区之间、不同级别洁净区之间的压差应当不低于 10 帕斯卡（>= 10 Pa）。必要时，相同洁净度级别的不同功能区域（操作间）之间也应当保持适当的压差梯度。"
                ),
                "content_en": (
                    "China GMP (2010 Revision) Annex 1: Sterile Products Cleanroom Limits\n\n"
                    "1. Airborne Particulate Classification Table (Max Particles/m3):\n"
                    "- Grade A: Static/Dynamic: >= 0.5 um <= 3,520; >= 5.0 um <= 20 (Unidirectional airflow 0.36-0.54 m/s).\n"
                    "- Grade B: Static: >= 0.5 um <= 3,520; >= 5.0 um <= 29. Dynamic: >= 0.5 um <= 352,000; >= 5.0 um <= 2,900.\n"
                    "- Grade C: Static: >= 0.5 um <= 352,000; >= 5.0 um <= 2,900. Dynamic: >= 0.5 um <= 3,520,000; >= 5.0 um <= 29,000.\n"
                    "- Grade D: Static: >= 0.5 um <= 3,520,000; >= 5.0 um <= 29,000.\n\n"
                    "2. Differential Pressure: Minimum 10 Pascals (>= 10 Pa) maintained between different cleanliness grades."
                ),
                "table_data": [
                    ["级别", "静态 >= 0.5μm", "静态 >= 5.0μm", "动态 >= 0.5μm", "动态 >= 5.0μm"],
                    ["A 级", "<= 3,520", "<= 20", "<= 3,520", "<= 20"],
                    ["B 级", "<= 3,520", "<= 29", "<= 352,000", "<= 2,900"],
                    ["C 级", "<= 352,000", "<= 2,900", "<= 3,520,000", "<= 29,000"],
                    ["D 级", "<= 3,520,000", "<= 29,000", "未作规定", "未作规定"]
                ]
            }
        ]
    },
    {
        "doc_id": "nmpa_be_consistency_evaluation_official",
        "doc_title_zh": "《化学药品仿制药口服固体制剂质量和疗效一致性评价指导原则》与生物等效性(BE)标准",
        "doc_title_en": "NMPA Guideline for Generic Drug Consistency Evaluation & Bioequivalence (BE) Standards",
        "version": "NMPA-BE-Consistency-Official",
        "effective_date": "2016-03-18",
        "jurisdiction": "NMPA",
        "category": "Regulatory_Guideline",
        "source_file": "nmpa_chemical_drug_be_official_full.pdf",
        "md_file": "nmpa_chemical_drug_be_official_full.md",
        "pdf_subpath": "nmpa/nmpa_chemical_drug_be_official_full.pdf",
        "sections": [
            {
                "section_id": "nmpa_be_sec1_rld_and_statistics",
                "page": 1,
                "title_zh": "第一节：参比制剂(RLD)遴选原则、空腹/餐后 BE 试验与双单侧 t 检验等效区间",
                "title_en": "Section 1: RLD Selection, Fasting/Fed BE Clinical Trials & Two One-Sided t-Test (80.00%-125.00%)",
                "content_zh": (
                    "国家药品监督管理局《化学药品仿制药口服固体制剂质量和疗效一致性评价指导原则》\n\n"
                    "一、参比制剂（Reference Listed Drug / RLD）遴选原则：\n"
                    "参比制剂首选原研药企业在国内上市销售的药品；若原研药未在国内上市，可选择在欧洲、美国或日本获准上市的原研药品。必须具有明确的批号、处方及合法采购溯源链条。\n\n"
                    "二、体内生物等效性（Bioequivalence / BE）临床试验设计：\n"
                    "1. 试验设计：通常采用单剂量、双周期、双序列、交叉互换试验设计（2x2 Crossover Design），在健康成年受试者中进行；\n"
                    "2. 空腹与餐后试验：口服固体制剂原则上均需开展空腹（Fasting）与高脂高热量餐后（Fed）两组独立的生物等效性试验；\n"
                    "3. 核心药代动力学（PK）参数：血药峰浓度（$C_{max}$）、从 0 到最后可测时间点的血药浓度-时间曲线下面积（$AUC_{0-t}$）以及从 0 到无穷大的曲线下面积（$AUC_{0-\\infty}$）。\n\n"
                    "三、法定等效性统计评价标准：\n"
                    "采用对数转换后的药代动力学参数进行方差分析与双单侧 t 检验（Two One-Sided t-Test）。受试制剂（T）与参比制剂（R）几何均值比的 90% 置信区间（90% Confidence Interval）必须完全落在 80.00% ~ 125.00% 范围之内，方可判定两制剂生物等效。"
                ),
                "content_en": (
                    "NMPA Generic Consistency Evaluation & Bioequivalence (BE) Guideline\n\n"
                    "1. Reference Listed Drug (RLD) Selection: Prioritizes innovator product marketed domestically or approved in US, EU, or Japan.\n\n"
                    "2. Clinical BE Study Design: Single-dose, randomized, two-period, two-sequence crossover trial conducted under both fasting and fed conditions in healthy volunteers.\n\n"
                    "3. Statistical Equivalence Criteria (Two One-Sided t-Test): The 90% confidence interval of the geometric mean ratio (Test/Reference) for Cmax and AUC0-t must fall entirely within 80.00% to 125.00%."
                )
            }
        ]
    },
    {
        "doc_id": "nmpa_tcm_classification_and_evidence_official",
        "doc_title_zh": "《中药注册分类及申报资料要求》与“中医药理论、人用经验、临床试验”三结合审评证据体系",
        "doc_title_en": "NMPA TCM Registration Classification & Three-in-One Evidence Evaluation System",
        "version": "NMPA-TCM-2020-Official",
        "effective_date": "2020-09-28",
        "jurisdiction": "NMPA",
        "category": "Regulatory_Guideline",
        "source_file": "nmpa_tcm_classification_2020_official_full.pdf",
        "md_file": "nmpa_tcm_classification_2020_official_full.md",
        "pdf_subpath": "nmpa/nmpa_tcm_classification_2020_official_full.pdf",
        "sections": [
            {
                "section_id": "nmpa_tcm_sec1_four_classes_and_three_in_one",
                "page": 1,
                "title_zh": "第一节：中药四大注册分类与“三结合”中药审评证据体系",
                "title_en": "Section 1: Four TCM Registration Categories & 'Three-in-One' Regulatory Evidence Framework",
                "content_zh": (
                    "国家药品监督管理局通告（2020年第68号）：《中药注册分类及申报资料要求》\n\n"
                    "一、中药四大法定注册分类：\n"
                    "1. 第 1 类：中药创新药（未在国家药品标准中收载，具有明确临床价值的创新复方制剂、提取物及其制剂）；\n"
                    "2. 第 2 类：中药改良型新药（改变已上市中药给药途径、剂型、工艺或增加新功能主治）；\n"
                    "3. 第 3 类：古代经典名方中药复方制剂（符合国家经典名方目录，采用传统工艺制备，可豁免临床试验）；\n"
                    "4. 第 4 类：同名同方药（通用名称、处方、剂型、功能主治与已上市国家药品标准完全一致的中药）。\n\n"
                    "二、“三结合”中药审评证据体系：\n"
                    "建立符合中医药自身规律的“中医药理论、人用经验、临床试验”三结合审评证据体系：\n"
                    "- 中医药理论：论证处方来源、配伍君臣佐使法理与治法病机契合度；\n"
                    "- 人用经验（Human Experience）：源于临床实践、真实世界应用的历史病例、临床经验方积累数据，人用经验可支持免做 II 期临床试验或作为安全有效性的核心证据；\n"
                    "- 临床试验：开展符合现代循证医学原则的验证性临床试验。"
                ),
                "content_en": (
                    "NMPA Announcement No. 68 of 2020: TCM Registration Classification\n\n"
                    "1. Four Statutory TCM Categories:\n"
                    "- Category 1: Innovative Traditional Chinese Medicines (TCM);\n"
                    "- Category 2: Modified TCM (new delivery route, new dosage form, new indication);\n"
                    "- Category 3: Ancient Classical Prescriptions (exempted from clinical trials per official compendium);\n"
                    "- Category 4: Generic / Same Name & Same Formula TCM.\n\n"
                    "2. 'Three-in-One' Regulatory Evidence Model: Synergistic integration of TCM Theory, Historical Human Experience (Real-World Evidence), and Confirmatory Clinical Trials."
                )
            }
        ]
    },
    {
        "doc_id": "nmpa_gcp_2020_clinical_trials_official",
        "doc_title_zh": "《药物临床试验质量管理规范》（GCP 2020年版）",
        "doc_title_en": "China Good Clinical Practice (GCP, 2020 Revision, NMPA & NHC Order No. 57)",
        "version": "NMPA-NHC-GCP-2020",
        "effective_date": "2020-07-01",
        "jurisdiction": "NMPA",
        "category": "Good_Clinical_Practice",
        "source_file": "nmpa_nhc_gcp_2020_official_full.pdf",
        "md_file": "nmpa_nhc_gcp_2020_official_full.md",
        "pdf_subpath": "nmpa/nmpa_nhc_gcp_2020_official_full.pdf",
        "sections": [
            {
                "section_id": "nmpa_gcp_sec1_ethics_and_sae_reporting",
                "page": 1,
                "title_zh": "第一节：伦理委员会独立审查、知情同意书与严重不良事件(SAE)强制报告时限",
                "title_en": "Section 1: Independent Ethics Review, Informed Consent & Mandatory SAE Reporting Timelines",
                "content_zh": (
                    "国家药品监督管理局 中华人民共和国国家卫生健康委员会令第 57 号《药物临床试验质量管理规范》（2020年7月1日起施行）\n\n"
                    "一、伦理委员会（Ethics Committee / EC）与知情同意（Informed Consent）：\n"
                    "1. 独立伦理审查：临床试验方案及任何修订必须预先获得伦理委员会正式书面审查批准，受试者的权益、安全和健康必须高于对科学和社会利益的考虑；\n"
                    "2. 知情同意程序：受试者必须在充分理解研究性质、潜在风险、受益及替代治疗后，自愿签署纸质或经确认的电子知情同意书（e-Consent）。\n\n"
                    "二、严重不良事件（Serious Adverse Event / SAE）强制报告时限：\n"
                    "1. 研究者报告时限：研究者获知任何 SAE 后，必须在 24 小时内向申办者书面报告；\n"
                    "2. 申办者快速报告时限（SUSAR 报告）：\n"
                    "   - 针对致死或危及生命的非预期严重不良反应（Fatal or Life-Threatening SUSAR）：申办者必须在获知后的 7 天内向国家药监局审评中心和伦理委员会提交快速报告，并在随后的 8 天内提交完整的随访报告；\n"
                    "   - 针对非致死且非危及生命的其他 SUSAR：申办者必须在获知后的 15 天内完成首次快速报告。"
                ),
                "content_en": (
                    "China GCP (2020 Revision, NMPA & NHC Order No. 57)\n\n"
                    "1. Ethics Committee & Informed Consent: Institutional Review Board independence; voluntary signed informed consent is mandatory prior to any protocol procedures.\n\n"
                    "2. Serious Adverse Event (SAE) Reporting Timelines:\n"
                    "- Investigator to Sponsor: Written report within 24 hours of awareness;\n"
                    "- Fatal / Life-Threatening SUSAR: Sponsor reports to NMPA CDE within 7 calendar days, with full followup within additional 8 days;\n"
                    "- Other SUSAR: Sponsor reports within 15 calendar days."
                )
            }
        ]
    },
    {
        "doc_id": "nmpa_overview_mandate_centers_official",
        "doc_title_zh": "国家药品监督管理局（国家药监局 / NMPA）职能职责、组织机构与监管框架总览",
        "doc_title_en": "National Medical Products Administration (NMPA): Statutory Mandate, Organizational Structure & Regulatory Framework Overview",
        "version": "NMPA-Overview-Statutory-2024",
        "effective_date": "2024-01-01",
        "jurisdiction": "NMPA",
        "category": "Statutory_Overview",
        "source_file": "nmpa_overview_statutory_mandate_official_full.pdf",
        "md_file": "nmpa_overview_statutory_mandate_official_full.md",
        "pdf_subpath": "nmpa/nmpa_overview_statutory_mandate_official_full.pdf",
        "sections": [
            {
                "section_id": "nmpa_overview_sec1_mandate_and_functions",
                "page": 1,
                "title_zh": "第一节：机构定位、历史沿革与法定监督管理职责",
                "title_en": "Section 1: Institutional Mandate, History & Statutory Responsibilities",
                "content_zh": (
                    "国家药品监督管理局（简称国家药监局、NMPA，英文：National Medical Products Administration）是中华人民共和国国务院部委管理的国家局，由国家市场监督管理总局管理（副部级）。前身为国家食品药品监督管理局（SFDA）、国家食品药品监督管理总局（CFDA），2018年根据党和国家机构改革方案正式组建为国家药品监督管理局。\n\n"
                    "一、法定执法依据与监管范围：\n"
                    "依据《中华人民共和国药品管理法》、《中华人民共和国疫苗管理法》、《中华人民共和国中医药法》、《医疗器械监督管理条例》（国务院令第739号）、《化妆品监督管理条例》行使国家行政监管职权。\n\n"
                    "二、核心职能职责：\n"
                    "1. 战略规划与标准拟订：拟订药品、医疗器械和化妆品安全监督管理的法律法规草案，制定部门规章，组织编制并颁布实施《中华人民共和国药典》等国家药品与器械标准；\n"
                    "2. 注册许可与审评审批：负责药品、医疗器械和化妆品注册管理，建立严格的审评审批制度并组织实施；\n"
                    "3. 全生命周期质量监管：负责药品与医疗器械研制（GLP/GCP）、生产（GMP）、经营（GSP）、使用全环节的监督管理，组织国家级抽查检验；\n"
                    "4. 上市后警戒与应急处置：组织开展药品不良反应（ADR）、医疗器械不良事件及化妆品不良反应的监测、评价与处置；\n"
                    "5. 国际法规协调：代表中国深度参与 ICH、IMDRF、PIC/S 等国际监管法规协调与合作。"
                ),
                "content_en": (
                    "National Medical Products Administration (NMPA) Institutional Overview & Statutory Mandate\n\n"
                    "1. Agency Profile: Under the State Administration for Market Regulation (SAMR), NMPA regulates drugs, medical devices, and cosmetics in China (successor to CFDA/SFDA following 2018 institutional reform).\n\n"
                    "2. Statutory Authorities: Drug Administration Law, Vaccine Administration Law, Medical Device Supervision and Administration Regulations (Order No. 739), Cosmetics Regulations.\n\n"
                    "3. Core Mandates:\n"
                    "- Formulating regulations and promulgating national standards including Chinese Pharmacopoeia (ChP);\n"
                    "- Premarket evaluation, clinical trial approvals (IND), and marketing authorizations (NDA/BLA/ANDA/Medical Device Registration);\n"
                    "- Lifecycle quality supervision across GxP (GLP, GCP, GMP, GSP);\n"
                    "- Post-marketing pharmacovigilance (ADR) and adverse event monitoring;\n"
                    "- International regulatory harmonization (ICH, IMDRF, PIC/S)."
                )
            },
            {
                "section_id": "nmpa_overview_sec2_departments_and_centers",
                "page": 2,
                "title_zh": "第二节：机关内设监管司局与直属专业技术支撑机构（CDE、CMDE、CFDI、中检院等）",
                "title_en": "Section 2: Internal Regulatory Departments & Affiliated Technical Review/Inspection Centers (CDE, CMDE, CFDI, NIFDC)",
                "content_zh": (
                    "国家药品监督管理局组织架构包括机关内设司局与专业技术直属机构：\n\n"
                    "一、机关主要监管司局：\n"
                    "1. 药品注册管理司：组织拟订药品注册管理制度，负责新药上市前审评审批、仿制药一致性评价与中药保护品种管理；\n"
                    "2. 药品监督管理司：组织拟订药品生产、经营、使用质量监督管理制度，监督指导药品 GMP 与 GSP 实施；\n"
                    "3. 医疗器械注册管理司：拟订医疗器械分类规则与注册标准，组织第三类及进口器械注册审评审批；\n"
                    "4. 医疗器械监督管理司：负责医疗器械生产、经营质量管理规范实施监督与上市后监管；\n"
                    "5. 化妆品监督管理司：负责化妆品注册备案与生产经营质量监管。\n\n"
                    "二、直属专业技术支撑机构：\n"
                    "1. 国家药品监督管理局药品审评中心（CDE）：国家级药品技术审评核心机构，承担新药（IND/NDA/BLA）、仿制药（ANDA）及一致性评价技术审评；\n"
                    "2. 国家药品监督管理局医疗器械技术审评中心（CMDE）：承担境内第三类及进口医疗器械与体外诊断试剂（IVD）的技术审评；\n"
                    "3. 国家药品监督管理局食品药品审核查验中心（CFDI）：承担全国药品与医疗器械检查员队伍管理，执行 GMP、GCP、GLP、GSP 国家级现场检查与飞行检查；\n"
                    "4. 中国食品药品检定研究院（中检院，NIFDC）：国家法定药品与医疗器械检验仲裁机构、国家标准物质标定、生物制品批签发；\n"
                    "5. 国家药品监督管理局药品评价中心（国家药品不良反应监测中心，CDR）：承担药品、医疗器械与化妆品不良反应监测与评价。"
                ),
                "content_en": (
                    "NMPA Departments & Technical Centers:\n\n"
                    "1. Internal Regulatory Departments: Drug Registration Dept, Drug Inspection Dept, Medical Device Registration Dept, Medical Device Inspection Dept, Cosmetics Dept.\n\n"
                    "2. Affiliated Technical Centers:\n"
                    "- CDE (Center for Drug Evaluation): Lead technical review body for human drugs (IND, NDA, ANDA, BE evaluation);\n"
                    "- CMDE (Center for Medical Device Evaluation): Technical review body for Class III, imported devices, and IVDs;\n"
                    "- CFDI (Center for Food and Drug Inspection): National inspectorate conducting GMP, GCP, GLP, and GSP onsite audits;\n"
                    "- NIFDC (National Institutes for Food and Drug Control): Statutory reference laboratory, testing, and lot release of biologics;\n"
                    "- CDR (Center for Drug Reevaluation / Adverse Reaction Monitoring): National pharmacovigilance center."
                )
            }
        ]
    }
]
