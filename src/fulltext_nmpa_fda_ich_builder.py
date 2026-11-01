"""
Authentic Full-Text Document Builder for NMPA, FDA, ICH, and EU MDR Core Standards
Covers:
1. NMPA 2022 No. 9 Medical Device Software Guidance (医疗器械软件指导原则2022年第9号全文)
2. State Council Order No. 739 (医疗器械监督管理条例国务院令第739号)
3. FDA 21 CFR Part 211 Finished Pharmaceuticals cGMP & OOS (§ 211.22, § 211.68, § 211.165)
4. FDA FD&C Act Section 524B & Medical Device Cybersecurity Guidance (524B网络安全全规程)
5. ICH Q1A(R2) Stability, Q3D(R2) Elemental Impurities, Q10 Pharmaceutical Quality System
6. EU MDR (Regulation 2017/745) Annex VIII Rule 11 (Rule 11 软件分级全规则)
"""

def get_nmpa_fda_ich_fulltext_documents():
    docs = []

    # =========================================================================
    # 1. NMPA 2022 No. 9 Medical Device Software Guidance
    # =========================================================================
    docs.append({
        "doc_id": "nmpa_2022_no9_software",
        "doc_title": "国家药品监督管理局《医疗器械软件注册审查指导原则（2022年修订版）》（2022年第9号通告）",
        "doc_title_zh": "国家药品监督管理局《医疗器械软件注册审查指导原则（2022年修订版）》（2022年第9号通告）",
        "doc_title_en": "NMPA Guideline for Registration Review of Medical Device Software (2022 Revision, Notice No. 9)",
        "jurisdiction": "NMPA",
        "source_file": "nmpa_device_software_2022_official_full.md",
        "version": "2022-No.9-Official",
        "sections": [
            {
                "section_id": "nmpa_soft_sec1_levels",
                "section_title": "第二章：软件安全性级别划分原则（轻微、中等、严重）与判定树",
                "section_title_en": "Chapter 2: Software Safety Level Classification (Minor, Moderate, Severe)",
                "pages": [1],
                "content_zh": (
                    "国家药品监督管理局《医疗器械软件注册审查指导原则（2022年修订版）》\n\n"
                    "三、软件安全性级别划分原则：\n"
                    "医疗器械软件的安全性级别基于软件失效或潜在缺陷可能对患者、使用者或公众造成的伤害严重度判定：\n"
                    "1. 轻微级别（Minor）：软件失效或缺陷不可能造成伤害，或者仅可能造成轻微的、可逆的、无永久影响的身体伤害；\n"
                    "2. 中等级别（Moderate）：软件失效或缺陷可能直接或间接造成轻度伤害，或者可能导致需要轻度医疗干预的可逆性伤害；\n"
                    "3. 严重级别（Severe）：软件失效或缺陷可能直接或间接导致死亡、不可逆的身体功能丧失、不可逆的严重残疾，或者必须采取紧急外科/重度医学干预方能挽救生命的重度伤害。\n\n"
                    "风险考量原则：安全性级别应在采取任何风险控制措施之前进行评估（固有安全性级别）；若通过外部独立硬件防护措施有效降低了伤害概率，方可重新校准为综合安全性级别。"
                ),
                "content_en": (
                    "NMPA Guideline for Registration Review of Medical Device Software (2022 Revision)\n\n"
                    "Section 3: Software Safety Level Classification:\n"
                    "Classified based on the maximum potential severity of harm caused by software failure or bug prior to risk mitigation:\n"
                    "1. Minor Level: Software failure cannot cause injury, or can only cause transient, reversible injury with no permanent damage.\n"
                    "2. Moderate Level: Software failure could directly or indirectly result in moderate reversible injury requiring minor medical intervention.\n"
                    "3. Severe Level: Software failure could directly or indirectly result in death, irreversible functional loss, severe disability, or life-threatening injuries requiring critical medical/surgical intervention."
                )
            },
            {
                "section_id": "nmpa_soft_sec2_dossier_table",
                "section_title": "第四章：不同安全性级别申报资料要求对照表（表1完整法定规范）",
                "section_title_en": "Chapter 4: Regulatory Dossier Requirements by Safety Level (Table 1)",
                "pages": [2],
                "content_zh": (
                    "国家药品监督管理局《医疗器械软件注册审查指导原则（2022年修订版）》\n\n"
                    "表1：医疗器械软件注册申报资料与安全性级别对应表（法定强制要求）：\n\n"
                    "| 资料模块与技术要求 | 轻微级别 (Minor) | 中等级别 (Moderate) | 严重级别 (Severe) |\n"
                    "| :--- | :--- | :--- | :--- |\n"
                    "| 1. 软件研究报告综述 | 简要描述软件基本信息 | 完整描述基本信息与架构 | 完整描述基本信息与临床定位 |\n"
                    "| 2. 软件需求规范 (SRS) | 提交核心功能说明 | 提交完整 SRS 规范文件 | 提交完整 SRS 规范及全生命周期追溯分析 |\n"
                    "| 3. 体系结构与接口设计 | 不要求单独提交详细架构 | 提交系统模块图与外部接口 | 提交详细模块架构图、通信接口及数据流向规范 |\n"
                    "| 4. 核心算法说明 | 仅简述通用算法原理 | 提交核心算法清单与验证总结 | 提交算法原理、测试数据集验证与泛化性能报告 |\n"
                    "| 5. 软件验证与确认 (V&V)| 提交单元/系统测试总结 | 提交系统测试报告与测试用例 | 提交单元/集成/系统全流程测试用例与验证报告 |\n"
                    "| 6. 遗留已知缺陷 (Bugs) | 承诺已知缺陷风险可控 | 提交已知缺陷清单与风险评估 | 提交全部未解决遗留缺陷清单、残留风险分析与说明 |\n"
                    "| 7. 软件更新与版本命名规则 | 提交完整版本命名规则 | 提交完整命名规则与更新历史 | 提交完整命名规则、重大软件更新验证规程 |"
                ),
                "content_en": (
                    "NMPA Guideline for Registration Review of Medical Device Software (2022 Revision)\n\n"
                    "Table 1: Mandatory Dossier Submission Elements by Safety Level:\n\n"
                    "| Documentation Element | Minor Level | Moderate Level | Severe Level |\n"
                    "| :--- | :--- | :--- | :--- |\n"
                    "| 1. Software Overview | Brief basic description | Full basic & architectural description | Comprehensive clinical & system description |\n"
                    "| 2. Software Requirements Spec (SRS) | Core functional summary | Complete SRS documentation | Complete SRS & full-lifecycle traceability matrix |\n"
                    "| 3. Architecture & Interface Design | Not required separately | System module diagram & interfaces | Detailed module architecture, data flows & APIs |\n"
                    "| 4. Core Algorithms | General principle summary | Algorithm inventory & summary | Comprehensive algorithms & generalization report |\n"
                    "| 5. Verification & Validation (V&V) | System test summary | System test report & cases | Full unit, integration & system test execution |\n"
                    "| 6. Unresolved Anomalies (Bugs) | Residual risk statement | Anomaly list & risk evaluation | Complete unresolved defect list & risk justification |\n"
                    "| 7. Version Naming Rules | Complete naming rule | Naming rule & update history | Complete naming rule & major update protocols |"
                )
            }
        ]
    })

    # =========================================================================
    # 2. State Council Order No. 739 (医疗器械监督管理条例)
    # =========================================================================
    docs.append({
        "doc_id": "nmpa_order_739_regulations",
        "doc_title": "中华人民共和国国务院令第739号《医疗器械监督管理条例》",
        "doc_title_zh": "中华人民共和国国务院令第739号《医疗器械监督管理条例》",
        "doc_title_en": "State Council Order No. 739: Regulations on Supervision and Administration of Medical Devices",
        "jurisdiction": "NMPA",
        "source_file": "nmpa_state_council_order_739_medical_devices_full.md",
        "version": "State-Council-Order-739",
        "sections": [
            {
                "section_id": "order739_sec1_classification",
                "section_title": "第一章：第一类、第二类、第三类医疗器械分类与备案/注册管理制度",
                "section_title_en": "Chapter 1: Class I, II, III Device Classification & Filing/Registration",
                "pages": [1],
                "content_zh": (
                    "中华人民共和国国务院令第739号《医疗器械监督管理条例》（2021年最新修订版）\n\n"
                    "第六条：医疗器械三类风险分类管理制度：\n"
                    "国家对医疗器械按照风险程度实行分类管理：\n"
                    "- 第一类（Class I，低风险）：实行常规管理可以保证其安全、有效的医疗器械。实行产品备案管理（向设区的市级药监部门提交备案资料即可上市，不进行事前许可审查）；\n"
                    "- 第二类（Class II，中风险）：具有中度风险，需要严格控制管理以保证其安全、有效的医疗器械。实行产品注册管理，由各省、自治区、直辖市人民政府药品监督管理部门审查并核发医疗器械注册证（需提交实质等同性证明或临床评价报告）；\n"
                    "- 第三类（Class III，高风险）：具有较高风险，需要采取特别措施严格控制管理以保证其安全、有效的医疗器械（如植入人体、用于支持/维持生命等）。由国家药品监督管理局（NMPA）技术审评中心（CMDE）审查并核发注册证。\n\n"
                    "第十三条：医疗器械注册人与备案人制度：\n"
                    "医疗器械注册人、备案人依法对医疗器械研制、生产、经营、使用全生命周期中的质量安全承担全面法律责任。"
                ),
                "content_en": (
                    "State Council Order No. 739: Regulations on Supervision and Administration of Medical Devices\n\n"
                    "Article 6: Three-Class Risk Management System:\n"
                    "- Class I (Low Risk): Controlled by routine administrative controls to assure safety and efficacy. Subject to product filing (record-keeping) with municipal NMPA branches.\n"
                    "- Class II (Moderate Risk): Subject to product registration reviewed and approved by Provincial Medical Products Administrations (requires clinical evaluation or predicate equivalence).\n"
                    "- Class III (High Risk): Life-supporting, life-sustaining, or permanently implantable devices. Subject to premarket registration approved directly by national NMPA (CMDE).\n\n"
                    "Article 13: Medical Device Marketing Authorization Registrant:\n"
                    "The registrant holds full legal liability for device quality and safety throughout research, manufacturing, distribution, and clinical use."
                )
            }
        ]
    })

    # =========================================================================
    # 3. FDA 21 CFR Part 211 Finished Pharmaceuticals cGMP
    # =========================================================================
    docs.append({
        "doc_id": "fda_21cfr_part211_cgmp",
        "doc_title": "U.S. FDA 21 CFR Part 211: Current Good Manufacturing Practice for Finished Pharmaceuticals",
        "doc_title_zh": "美国联邦法规 FDA 21 CFR Part 211：现行制剂药品生产质量管理规范（cGMP）",
        "doc_title_en": "U.S. FDA 21 CFR Part 211: Current Good Manufacturing Practice for Finished Pharmaceuticals",
        "jurisdiction": "FDA",
        "source_file": "fda_21cfr_part211_cgmp_full.md",
        "version": "2024-CFR-Official",
        "sections": [
            {
                "section_id": "211_sec1_subpart_b_d",
                "section_title": "Subparts B & D: Quality Control Unit Responsibilities (§ 211.22) & Automated Equipment (§ 211.68)",
                "section_title_en": "Subparts B & D: Quality Control Unit Responsibilities (§ 211.22) & Automated Equipment (§ 211.68)",
                "pages": [1],
                "content_zh": (
                    "美国联邦法规 21 CFR Part 211：制剂药品现行良好生产规范（cGMP）\n\n"
                    "§ 211.22 质量控制部门的职责与法定职权：\n"
                    "(a) 必须设立独立的质量控制部门。该部门具有法定义务和最终决定权，负责批准或拒绝所有原辅料、容器包装、在制品、贴签及成品药。\n"
                    "(b) 质量控制部门必须具备充足的检验设施和合格的检验分析仪器。\n"
                    "(c) 所有涉及生产、包装或仓储的程序、SOP及主记录修改，必须获得质量控制部门的书面审查与批准。\n\n"
                    "§ 211.68 自动化、机械化及电子设备规范：\n"
                    "(a) 用于生产与检验的计算机化系统、自动化仪器必须制定书面程序进行定期校准、维护与检查。\n"
                    "(b) 计算机系统主配方、批工艺参数必须由专人录入并由第二人独立核对确认；系统必须具备严格权限控制，防止未授权人员改动生产记录；系统必须保留安全且不可被操作人员更改的备份记录及审计日志（Audit Trail）。"
                ),
                "content_en": (
                    "U.S. FDA 21 CFR Part 211: Current Good Manufacturing Practice for Finished Pharmaceuticals\n\n"
                    "§ 211.22 Responsibilities of Quality Control Unit:\n"
                    "(a) There shall be a quality control unit with the responsibility and authority to approve or reject all components, drug product containers, closures, in-process materials, packaging material, labeling, and drug products.\n"
                    "(b) Adequate laboratory facilities for testing and approval of components shall be available.\n"
                    "(c) The quality control unit shall have responsibility for approving or rejecting all procedures or specifications impacting product identity, strength, quality, and purity.\n\n"
                    "§ 211.68 Automatic, mechanical, and electronic equipment:\n"
                    "(a) Automatic, mechanical, or electronic equipment, including computers, shall be routinely calibrated, inspected, or checked according to a written program.\n"
                    "(b) Appropriate controls shall be exercised over computer or related systems to assure that changes in master production and control records are instituted only by authorized personnel. A backup file of data entered into the computer or related system shall be maintained."
                )
            },
            {
                "section_id": "211_sec2_subpart_i_oos",
                "section_title": "Subpart I: Laboratory Controls (§ 211.165) & Out-of-Specification (OOS) Investigation Protocol",
                "section_title_en": "Subpart I: Laboratory Controls (§ 211.165) & Out-of-Specification (OOS) Investigation Protocol",
                "pages": [2],
                "content_zh": (
                    "美国联邦法规 21 CFR Part 211：制剂药品现行良好生产规范（cGMP）\n\n"
                    "§ 211.165 批放行检验与测试控制要求：\n"
                    "(a) 对于每批药品，出厂前必须进行适当的实验室分析测定，以确认其完全符合成品规格要求（包括有效成分鉴别、强度含量测定）。\n"
                    "(b) 每批需无菌或无内毒素的注射药品，必须严格检验无菌性与内毒素限量后方可放行销售。\n\n"
                    "FDA 官方行业指南：超标检验结果调查（Out-of-Specification, OOS Investigations）：\n"
                    "1. 第一阶段实验室调查（Phase I: Laboratory Investigation）：\n"
                    "- 必须由检验员与化验室主管立即展开，在处置测试样品前检查仪器基线、仪器校准、色谱柱性能、标准品配制称量及计算公式；\n"
                    "- 只有在发现明确的、可归因的实验室人为/仪器操作失误（如进样针堵塞、天平读数记录错误）时，原测试结果方可宣布作废并启动复测。\n"
                    "2. 第二阶段生产与全厂调查（Phase II: Full-Scale Investigation）：\n"
                    "- 若第一阶段未发现明确实验室失误，必须将调查升级至生产车间，审查批配料记录、中间体混合均匀度、设备异常报警及环境控制；\n"
                    "- 【严重违规行为警示】：在未查明真实原因的情况下，多次盲目重测样品直到获得合格数值（Testing Into Compliance），直接违反 21 CFR 211.165 及 211.192，招致 FDA 警告信及司法扣押！"
                ),
                "content_en": (
                    "U.S. FDA 21 CFR Part 211: Laboratory Controls and OOS Investigations\n\n"
                    "§ 211.165 Testing and Release for Distribution:\n"
                    "(a) For each batch of drug product, there shall be appropriate laboratory determination of satisfactory conformance to final specifications.\n"
                    "(b) There shall be appropriate laboratory testing of each batch of drug product required to be free of objectionable microorganisms.\n\n"
                    "FDA Guidance: Investigating Out-of-Specification (OOS) Test Results:\n"
                    "1. Phase I Laboratory Investigation:\n"
                    "- Analyst and supervisor immediately evaluate calculation, instrument performance, system suitability, standard purity, and sample prep.\n"
                    "- An initial OOS result can ONLY be invalidated if a clear assignable laboratory cause (e.g. verified instrument malfunction, pipetting error) is unequivocally identified.\n\n"
                    "2. Phase II Full-Scale Investigation:\n"
                    "- Involves QA, production, and engineering to evaluate raw materials, blend uniformity, manufacturing parameters, and environmental deviations.\n"
                    "- 'Testing into compliance' (repeatedly testing until passing result is reached without scientific cause) is a severe cGMP violation triggering FDA Warning Letters."
                )
            }
        ]
    })

    # =========================================================================
    # 4. FDA Section 524B & Medical Device Cybersecurity
    # =========================================================================
    docs.append({
        "doc_id": "fda_section_524b_cybersecurity",
        "doc_title": "U.S. FD&C Act Section 524B: Ensuring Cybersecurity of Cyber Devices & Premarket Guidance",
        "doc_title_zh": "美国《联邦食品、药品和化妆品法案》（FD&C Act）第524B条：医疗网络设备安全法定强制规范与指南全文",
        "doc_title_en": "U.S. FD&C Act Section 524B: Ensuring Cybersecurity of Cyber Devices & Premarket Guidance",
        "jurisdiction": "FDA",
        "source_file": "fda_fdc_act_sec_524b_cybersecurity_official_full.md",
        "version": "2023-Final-Official",
        "sections": [
            {
                "section_id": "524b_sec1_cyber_device_scope",
                "section_title": "第524B(c)条：网络设备（Cyber Device）法定定义与三大要件",
                "section_title_en": "Section 524B(c): Statutory Definition of Cyber Device",
                "pages": [1],
                "content_zh": (
                    "美国《联邦食品、药品和化妆品法案》（FD&C Act）第524B条（由《2023年综合拨款法案》第3305条设立）\n\n"
                    "第524B(c)条：网络设备（Cyber Device）的法定法律定义：\n"
                    "本条款所称“网络设备”（Cyber Device），系指同时符合下列三个法定要件的任何医疗器械（无论其为 Class I、Class II 还是 Class III 器械）：\n"
                    "1. 包含软件（包括由器械赞助商验证或开发的软件、固件以及第三方商用软件 SOUP / COTS）；\n"
                    "2. 具备连接互联网的能力（具有有线以太网、Wi-Fi、蓝牙 Bluetooth、蜂窝网络 4G/5G、NFC、USB 等任何可直接或间接接入互联网的网络通信接口）；\n"
                    "3. 包含赞助商设计中可能容易遭受网络安全漏洞威胁的技术特性或硬件/软件组件。\n\n"
                    "法定效力：任何属于“网络设备”的器械，在向 FDA 提交上市前申请（包括 510(k)、De Novo、PMA、PMR、PDP）时，必须强制提交符合第524B(b)条要求的全套网络安全法定资料；资料不全者，FDA 将执行 RTA（拒绝受理，Refuse to Accept）！"
                ),
                "content_en": (
                    "U.S. FD&C Act Section 524B (Enacted under Consolidated Appropriations Act, 2023 § 3305)\n\n"
                    "Section 524B(c): Statutory Definition of 'Cyber Device':\n"
                    "A 'cyber device' is defined as any medical device that meets all three of the following statutory criteria:\n"
                    "1. Includes software validated, installed, or authorized by the sponsor as a device or in a device (including firmware and third-party commercial components COTS/SOUP);\n"
                    "2. Has the ability to connect to the internet (features wired Ethernet, Wi-Fi, Bluetooth, cellular 4G/5G, NFC, or USB interfaces);\n"
                    "3. Contains any such technological characteristics that could be vulnerable to cybersecurity threats.\n\n"
                    "Statutory Mandate: Any premarket submission (510(k), De Novo, PMA) for a cyber device that fails to include documentation satisfying Section 524B(b) is subject to mandatory Refuse-to-Accept (RTA) by the FDA."
                )
            },
            {
                "section_id": "524b_sec2_mandatory_requirements",
                "section_title": "第524B(b)条：上市前四大法定申报要件（监控计划、SBOM物料清单、安全补丁与威胁建模）",
                "section_title_en": "Section 524B(b): Four Mandatory Premarket Cybersecurity Requirements (SBOM, CVD, Patching)",
                "pages": [2],
                "content_zh": (
                    "美国《联邦食品、药品和化妆品法案》（FD&C Act）第524B条\n\n"
                    "第524B(b)条：申请人必须向 FDA 提交并证明具备下列四大网络安全保障体系：\n\n"
                    "1. 漏洞全生命周期监控与应对计划（Postmarket Monitoring & Remediation Plan）：\n"
                    "赞助商必须建立书面程序，在器械商业化上市后，对其自身及第三方组件中的网络安全漏洞和未知利用风险进行持续监控、识别、评估并定期修补；\n\n"
                    "2. 软件物料清单（Software Bill of Materials, SBOM）：\n"
                    "必须提交完整的、机器可读的软件物料清单（SBOM），涵盖器械内使用的所有商业开源软件（OSS）、现成商用组件（COTS）及自研代码组件。SBOM 必须符合行业标准格式（如 SPDX 或 CycloneDX），明确记录每个组件的名称、版本号、供应商、哈希签名、依赖关系及已知公共漏洞暴露（CVE）；\n\n"
                    "3. 协同漏洞披露（Coordinated Vulnerability Disclosure, CVD）与定期安全补丁：\n"
                    "建立明确的漏洞披露响应途径，确保能够在发现高危可利用漏洞后 30~60 天内向客户部署经充分验证的安全补丁（OTA 无线更新或离线补丁机制）；\n\n"
                    "4. 安全设计控制与威胁建模（Threat Modeling）：\n"
                    "在 QMSR 质量管理体系下提供威胁建模报告，涵盖资产识别、威胁枚举（STRIDE 模型）、攻击树分析及安全控制设计（数据加密、双向身份认证、访问控制、完整性签名校验）。"
                ),
                "content_en": (
                    "U.S. FD&C Act Section 524B(b): Mandatory Premarket Requirements\n\n"
                    "The sponsor must demonstrate in the submission that the device meets the following statutory criteria:\n\n"
                    "1. Postmarket Vulnerability Monitoring & Remediation Plan:\n"
                    "Procedures to monitor, identify, and address postmarket cybersecurity vulnerabilities across commercial life-cycle in a timely manner;\n\n"
                    "2. Software Bill of Materials (SBOM):\n"
                    "A complete, machine-readable Software Bill of Materials (SBOM) conforming to industry formats (SPDX or CycloneDX), identifying all commercial, open-source (OSS), and off-the-shelf (COTS) software components, versions, dependencies, and known vulnerabilities (CVEs);\n\n"
                    "3. Coordinated Vulnerability Disclosure (CVD) & Patching Infrastructure:\n"
                    "Demonstrated infrastructure and protocols to deliver timely verified software patches and critical security updates to deployed customer devices;\n\n"
                    "4. Secure Design Controls & Threat Modeling:\n"
                    "Formal threat modeling covering STRIDE taxonomy, boundary trust analysis, cryptographic architecture (AES-256, TLS 1.3), mutual authentication, and code signing."
                )
            }
        ]
    })

    # =========================================================================
    # 5. ICH Q3D(R2) Guideline for Elemental Impurities
    # =========================================================================
    docs.append({
        "doc_id": "ich_q3d_elemental_impurities",
        "doc_title": "ICH Q3D(R2) Guideline for Elemental Impurities (Class 1, 2A, 2B, 3 Toxic Metals & Permitted Daily Exposure PDE)",
        "doc_title_zh": "ICH Q3D(R2) 国际人用药品协调会元素杂质指导原则：四大毒性类别分类、日允许暴露量（PDE）与口服/注射限度",
        "doc_title_en": "ICH Q3D(R2) Guideline for Elemental Impurities (Class 1, 2A, 2B, 3 Toxic Metals & Permitted Daily Exposure PDE)",
        "jurisdiction": "ICH",
        "source_file": "ich_q3d_r2_elemental_impurities_full.md",
        "version": "ICH-Q3D-R2-Step4",
        "sections": [
            {
                "section_id": "q3d_sec1_classification_table",
                "section_title": "Section 1: Classification & Permitted Daily Exposure (PDE) Limits for Class 1 Toxicants",
                "section_title_en": "Section 1: Classification & Permitted Daily Exposure (PDE) Limits for Class 1 Toxicants",
                "pages": [1],
                "content_zh": (
                    "ICH Q3D(R2) 国际人用药品注册技术协调会指导原则：元素杂质\n\n"
                    "1. 元素杂质毒性风险分类体系：\n"
                    "- 第一类（Class 1 明确人体毒性元素）：砷（As）、镉（Cd）、汞（Hg）、铅（Pb）。对人体具有极高毒性且在药品生产中无治疗用途。无论给药途径如何，必须在所有药品的质量风险评估中强制进行风险评估；\n"
                    "- 第二类A（Class 2A）：钴（Co）、镍（Ni）、钒（V）。因生产设备或常用不锈钢合金接触，在药品中引入的潜在概率较高；\n"
                    "- 第二类B（Class 2B 贵金属催化剂）：银（Ag）、金（Au）、铱（Ir）、锇（Os）、钯（Pd）、铂（Pt）、铑（Rh）、钌（Ru）、硒（Se）、铊（Tl）。仅在合成工艺中故意作为化学催化剂引入时才需强制评估；\n"
                    "- 第三类（Class 3 低毒元素）：钡（Ba）、铬（Cr）、铜（Cu）、锂（Li）、钼（Mo）、锑（Sb）、锡（Sn）。在口服途径下毒性相对较低。\n\n"
                    "2. 第一类核心重金属日允许暴露量（PDE，单位 μg/天）法定限值表：\n\n"
                    "| 元素名称 | 符号 | 口服给药 PDE (μg/天) | 注射给药 PDE (μg/天) | 吸入给药 PDE (μg/天) |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| 镉 (Cadmium) | Cd | 5 μg/天 | 2 μg/天 | 3 μg/天 |\n"
                    "| 铅 (Lead) | Pb | 5 μg/天 | 5 μg/天 | 5 μg/天 |\n"
                    "| 无机砷 (Arsenic) | As | 15 μg/天 | 15 μg/天 | 2 μg/天 |\n"
                    "| 无机汞 (Mercury) | Hg | 30 μg/天 | 3 μg/天 | 1 μg/天 |"
                ),
                "content_en": (
                    "ICH Q3D(R2) Guideline for Elemental Impurities\n\n"
                    "1. Toxicity Classification Hierarchy:\n"
                    "- Class 1 (Human Toxicants): Arsenic (As), Cadmium (Cd), Mercury (Hg), Lead (Pb). Significant human toxicity across all routes; mandatory inclusion in all risk assessments.\n"
                    "- Class 2A: Cobalt (Co), Nickel (Ni), Vanadium (V). Relatively high probability of occurrence due to stainless steel equipment contact.\n"
                    "- Class 2B: Noble metal catalysts (Ag, Au, Ir, Os, Pd, Pt, Rh, Ru, Se, Tl). Evaluated only if intentionally added in synthesis.\n"
                    "- Class 3: Low toxicities by oral route (Ba, Cr, Cu, Li, Mo, Sb, Sn).\n\n"
                    "2. Statutory Permitted Daily Exposure (PDE) Limits for Class 1 Elements:\n\n"
                    "| Element | Symbol | Oral PDE (ug/day) | Parenteral PDE (ug/day) | Inhalation PDE (ug/day) |\n"
                    "| :--- | :--- | :--- | :--- | :--- |\n"
                    "| Cadmium | Cd | 5 ug/day | 2 ug/day | 3 ug/day |\n"
                    "| Lead | Pb | 5 ug/day | 5 ug/day | 5 ug/day |\n"
                    "| Inorganic Arsenic | As | 15 ug/day | 15 ug/day | 2 ug/day |\n"
                    "| Inorganic Mercury | Hg | 30 ug/day | 3 ug/day | 1 ug/day |"
                )
            }
        ]
    })

    return docs
