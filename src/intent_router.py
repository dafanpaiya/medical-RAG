import re
from typing import Tuple

class IntentRouter:
    """
    Intelligent Intent Classifier and Domain Boundary Guard for Enterprise Regulatory RAG.
    Categorizes incoming queries into:
    1. GREETING_OR_META: Natural greetings, identity inquiries, and capability explanations.
    2. OUT_OF_SCOPE: Queries completely outside medicine/healthcare/regulatory domains.
    3. REGULATORY_DOMAIN_QUERY: Professional medical and regulatory inquiries.
    """

    GREETING_PATTERNS = [
        r"^(hi|hello|hey|greetings|good\s*(morning|afternoon|evening|day))[\s!.,?]*$",
        r"^(你好|您好|哈喽|嗨|早安|午安|晚安|打扰了)[\s!.,?~]*$",
        r"(你是谁|你叫什么|你能做(什么|啥)|你有什么功能|介绍(一下)?你自己|你的职责|你的作用)",
        r"(who\s+are\s+you|what\s+can\s+you\s+do|introduce\s+yourself|help\s*me)"
    ]

    # Explicit domain keywords that indicate a medical/pharma/regulatory inquiry
    DOMAIN_KEYWORDS = [
        # General Medical & Pharma
        "疾病", "治疗", "药理", "症状", "患者", "临床", "用药", "不良反应", "处方", "药效",
        "诊断", "病理", "生理", "解剖", "病症", "疫苗", "抗体", "靶向", "代谢", "毒理",
        "disease", "treatment", "symptom", "clinical", "patient", "drug", "pharma",
        # Devices & Regulatory (Legacy scope included)
        "器械", "医疗", "软件", "samd", "注册", "审查", "安全性", "级别", "网络安全", "fda", "nmpa", "mdr",
        "中药", "化学药", "仿制药", "原研", "新药", "人用经验", "生物等效", "be", "溶出度"
    ]

    # Non-medical topic indicators to catch out-of-scope requests
    OUT_OF_SCOPE_PATTERNS = [
        r"(写.*?(诗|歌|作文|故事|散文|检讨书|周报|文案|情书))",
        r"(做.*?(红烧肉|番茄炒蛋|蛋糕|菜|饭|面条)|菜谱|烹饪|厨艺)",
        r"(天气|气温|下雨|穿什么衣服)",
        r"(股票|比特币|以太坊|黄金走势|炒股|行情|基金走势)",
        r"(编写|写一个|生成|运行)?.*?(贪吃蛇|扫雷|计算器|爬虫代码|javascript代码|python代码)",
        r"(数学题|解方程|求导|几何证明|相对论|量子力学|宇宙飞船|火箭推进)",
        r"(推荐.*?(电影|电视剧|游戏|动漫|小说|餐厅|景点|手机|电脑))",
        r"(聊天|讲个笑话|讲故事|八卦|明星绯闻|旅游攻略)"
    ]

    GREETING_RESPONSE = (
        "您好！我是**医药与生命科学智能问答助手**。\n\n"
        "我可以为您提供专业的医药知识、疾病机理、药理作用、临床试验设计以及医疗器械/药品注册法规等方面的解答。\n"
        "请问您今天想了解哪方面的医药知识？"
    )

    OUT_OF_SCOPE_RESPONSE = (
        "您好，我是专注于**医药、医疗器械与生命科学领域**的专业智能问答系统。\n\n"
        "您提出的问题超出了我的专业服务范畴。我的核心功能包括解答疾病诊断治疗基础知识、药物作用机制、临床试验标准以及行业法规要求。\n"
        "建议您提出与医药健康或生命科学相关的专业问题，我将为您调取知识库进行解答。"
    )

    @classmethod
    def route_query(cls, query: str) -> Tuple[str, str]:
        """
        Classifies query intent.
        Returns (intent, response_text)
        - intent: 'GREETING', 'OUT_OF_SCOPE', or 'REGULATORY_DOMAIN_QUERY'
        """
        clean_q = query.strip()
        q_lower = clean_q.lower()

        # 1. Check for Greetings or Meta queries
        for pattern in cls.GREETING_PATTERNS:
            if re.search(pattern, q_lower):
                return "GREETING", cls.GREETING_RESPONSE

        # 2. Check for explicit Out-of-Scope triggers
        for pattern in cls.OUT_OF_SCOPE_PATTERNS:
            if re.search(pattern, q_lower):
                return "OUT_OF_SCOPE", cls.OUT_OF_SCOPE_RESPONSE

        # 3. Check domain presence
        has_domain_keywords = any(kw in q_lower for kw in cls.DOMAIN_KEYWORDS)

        # If the query is completely devoid of medical/regulatory terms and looks like casual chat
        if not has_domain_keywords and len(clean_q) > 4:
            # Check if it looks like a non-medical casual question
            casual_markers = ["怎么做", "如何做", "介绍一下", "有哪些好玩的", "吃什么", "去哪里", "算一下", "代码怎么写"]
            if any(m in clean_q for m in casual_markers):
                return "OUT_OF_SCOPE", cls.OUT_OF_SCOPE_RESPONSE

        return "REGULATORY_DOMAIN_QUERY", ""
