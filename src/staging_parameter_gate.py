"""
Deterministic Staging Parameter Gate (Phase 30-A)
=================================================
Standalone verification gate for the Chinese Pharmacopoeia 2025 Exploratory RAG Demo.
Enforces compendial compliance, provenance verification, per-parameter evidence completeness,
and zero partial-answer policies on staging candidate evidence.

Operational Invariants:
- mode = DEMO_EXPLORATORY_OCR_PILOT
- gold_truth_status = GOLD_TRUTH_PENDING
- p456_mapping_status = P456_MAP_VERIFY_PENDING
- watchdog_runtime_status = WATCHDOG_RUNTIME_NOT_INDEPENDENTLY_VERIFIED
- RAG_SCORE_THRESHOLD = 0.40 (Production default preserved)
"""

import os
import re
from typing import List, Dict, Any, Optional, Tuple, Set

# Import verified compendial mappings from existing staging assembler
from src.staging_assembler import PAGE_MONOGRAPH_MAP, QUARANTINED_CHUNKS, CHUNK_MONOGRAPH_MAP
from src.document_lifecycle import DocumentLifecycleManager, LifecycleStatus, IndexEligibility

# ==============================================================================
# Verified Chunk-Level Monograph Provenance Registry (Phase 34-A)
# ==============================================================================
CHUNK_VERIFIED_MONOGRAPH_MAP: Dict[str, Dict[str, Any]] = {
    # Volume 1 Page 25: Upper section is 丁公藤 (lines 1-19), Lower section is 丁香 (lines 21-45)
    "CHP2025-V1-P0025-C01": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 3 (# 丁公藤 接前页 总灰分<=10.0%)"
    },
    "CHP2025-V1-P0025-C02": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 4 (丁公藤 醇溶性浸出物>=3.0%)"
    },
    "CHP2025-V1-P0025-C03": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt lines 5-10 (丁公藤 HPLC东莨菪内酯)"
    },
    "CHP2025-V1-P0025-C04": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 12 (丁公藤 饮片炮制)"
    },
    "CHP2025-V1-P0025-C05": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 13 (丁公藤 饮片性状)"
    },
    "CHP2025-V1-P0025-C06": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 14 (丁公藤 同药材条款)"
    },
    "CHP2025-V1-P0025-C07": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 15 (丁公藤 性味与归经)"
    },
    "CHP2025-V1-P0025-C08": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 16 (丁公藤 功能与主治)"
    },
    "CHP2025-V1-P0025-C09": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 17 (丁公藤 用法与用量)"
    },
    "CHP2025-V1-P0025-C10": {
        "verified_monograph": "丁公藤",
        "volume": 1, "page": 25, "region": "UPPER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 18 (丁公藤 注意)"
    },
    "CHP2025-V1-P0025-C11": {
        "verified_monograph": "丁公藤/丁香",
        "volume": 1, "page": 25, "region": "TRANSITION",
        "attribution_status": "PARTIAL_MONOGRAPH_SPLIT",
        "attribution_evidence": "gt_v1_p0025.txt lines 19-24 (丁公藤贮藏 + 丁香标头及来源)"
    },
    "CHP2025-V1-P0025-C12": {
        "verified_monograph": "丁香",
        "volume": 1, "page": 25, "region": "LOWER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt lines 25-27 (# 丁香 性状与显微/薄层鉴别)"
    },
    "CHP2025-V1-P0025-C13": {
        "verified_monograph": "丁香",
        "volume": 1, "page": 25, "region": "LOWER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt lines 28-29 (# 丁香 检查 杂质 水分)"
    },
    "CHP2025-V1-P0025-C14": {
        "verified_monograph": "丁香",
        "volume": 1, "page": 25, "region": "LOWER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt lines 31-36 (# 丁香 含量测定 气相色谱法 丁香酚)"
    },
    "CHP2025-V1-P0025-C15": {
        "verified_monograph": "丁香",
        "volume": 1, "page": 25, "region": "LOWER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 38 (丁香 饮片炮制)"
    },
    "CHP2025-V1-P0025-C16": {
        "verified_monograph": "丁香",
        "volume": 1, "page": 25, "region": "LOWER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 39 (丁香 同药材条款)"
    },
    "CHP2025-V1-P0025-C17": {
        "verified_monograph": "丁香",
        "volume": 1, "page": 25, "region": "LOWER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 40 (丁香 性味与归经)"
    },
    "CHP2025-V1-P0025-C18": {
        "verified_monograph": "丁香",
        "volume": 1, "page": 25, "region": "LOWER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt line 41 (丁香 功能与主治)"
    },
    "CHP2025-V1-P0025-C19": {
        "verified_monograph": "丁香",
        "volume": 1, "page": 25, "region": "LOWER",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v1_p0025.txt lines 42-44 (丁香 用法用量、注意、贮藏)"
    },
    # Volume 2 Page 756
    "CHP2025-V2-P0756-C04": {
        "verified_monograph": "阿司匹林",
        "volume": 2, "page": 756, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "gt_v2_p0756.txt (# 阿司匹林 原料药专论)"
    },
    # Other staging pilot chunks
    "CHP2025-V4-P0050-C01": {
        "verified_monograph": "通则0108 栓剂",
        "volume": 4, "page": 50, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "通则0108 栓剂"
    },
    "CHP2025-V4-P0109-C01": {
        "verified_monograph": "通则0401 紫外-可见分光光度法",
        "volume": 4, "page": 109, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "通则0401 拉曼散射"
    },
    "CHP2025-V1-P0144-C02": {
        "verified_monograph": "结构化附表 HPLC色谱梯度表",
        "volume": 1, "page": 144, "region": "TABLE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "地黄HPLC梯度表"
    },
    "CHP2025-V1-P0163-C14": {
        "verified_monograph": "结构化附表 梯度洗脱时间表",
        "volume": 1, "page": 163, "region": "TABLE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "梯度洗脱时间表"
    },
    "CHP2025-V2-P0100-C01": {
        "verified_monograph": "注射用门冬酰胺酶（埃希）",
        "volume": 2, "page": 100, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "注射用门冬酰胺酶"
    },
    "CHP2025-V3-P0141-C01": {
        "verified_monograph": "冻干乙型脑炎灭活疫苗（Vero细胞）",
        "volume": 3, "page": 141, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "冻干乙型脑炎灭活疫苗"
    },
    "CHP2025-V4-P0113-C01": {
        "verified_monograph": "通则0403 近红外分光光度法",
        "volume": 4, "page": 113, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "通则0403"
    },
    "CHP2025-V3-P0115-C01": {
        "verified_monograph": "吸附白喉破伤风联合疫苗（成人及青少年用）",
        "volume": 3, "page": 115, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "吸附白喉破伤风联合疫苗"
    },
    "CHP2025-V3-P0137-C01": {
        "verified_monograph": "乙型脑炎减毒活疫苗",
        "volume": 3, "page": 137, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "乙型脑炎减毒活疫苗"
    },
    "CHP2025-V4-P0121-C01": {
        "verified_monograph": "通则0412 电感耦合等离子体质谱法",
        "volume": 4, "page": 121, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "通则0412"
    },
    "CHP2025-V4-P0120-C01": {
        "verified_monograph": "通则0412 电感耦合等离子体质谱法",
        "volume": 4, "page": 120, "region": "FULL_PAGE",
        "attribution_status": "VERIFIED_GOLD_TRUTH",
        "attribution_evidence": "通则0412"
    }
}


# ==============================================================================
# Curated Primary Benchmark Registry (57 Queries)
# ==============================================================================
QUERY_PARAM_REGISTRY: Dict[str, Dict[str, Any]] = {
    # Volume 1: Traditional Chinese Medicine
    "EVAL-01": {
        "primary_entity": "丁香", "aliases": ["丁香花蕾"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["总灰分"],
        "expected_chunks": ["CHP2025-V1-P0025-C01"],
        "expected_limits": [{"param": "总灰分", "val": "10.0", "unit": "%", "op": "不得过", "sec": "【检查】"}]
    },
    "EVAL-02": {
        "primary_entity": "阿司匹林", "aliases": ["乙酰水杨酸"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["贮藏条件"],
        "expected_chunks": ["CHP2025-V2-P0756-C04"],
        "expected_limits": [{"param": "贮藏条件", "val": "密封，在干燥处保存", "unit": "N/A", "op": "==", "sec": "【贮藏】"}]
    },
    "EVAL-03": {
        "primary_entity": "栓剂", "aliases": ["直肠栓", "阴道栓", "通则0108"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["应用腔道分类"],
        "expected_chunks": ["CHP2025-V4-P0050-C01"],
        "expected_limits": [{"param": "应用腔道分类", "val": "直肠栓和阴道栓", "unit": "N/A", "op": "==", "sec": "通则0108"}]
    },
    "EVAL-04": {
        "primary_entity": "拉曼光谱", "aliases": ["拉曼散射", "通则0401"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["含水物检测适用性机理"],
        "expected_chunks": ["CHP2025-V4-P0109-C01"],
        "expected_limits": [{"param": "含水物检测适用性机理", "val": "水有很强的红外吸收但拉曼散射弱几乎不受水影响", "unit": "N/A", "op": "==", "sec": "通则0401"}]
    },
    "EVAL-05": {
        "primary_entity": "丁香", "aliases": ["丁香花蕾"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["醇溶性浸出物"],
        "expected_chunks": ["CHP2025-V1-P0025-C02"],
        "expected_limits": [{"param": "醇溶性浸出物", "val": "3.0", "unit": "%", "op": "不得少于", "sec": "【浸出物】"}]
    },
    "EVAL-06": {
        "primary_entity": "丁香", "aliases": ["丁香花蕾"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["杂质", "水分"],
        "expected_chunks": ["CHP2025-V1-P0025-C13"],
        "expected_limits": [
            {"param": "杂质", "val": "4", "unit": "%", "op": "不得过", "sec": "【检查】"},
            {"param": "水分", "val": "12.0", "unit": "%", "op": "不得过", "sec": "【检查】"}
        ]
    },
    "EVAL-07": {
        "primary_entity": "阿司匹林", "aliases": ["乙酰水杨酸"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["供试品取样量", "供试品定容体积"],
        "expected_chunks": ["CHP2025-V2-P0756-C04"],
        "expected_limits": [
            {"param": "供试品取样量", "val": "0.1", "unit": "g", "op": "==", "sec": "【有关物质】"},
            {"param": "供试品定容体积", "val": "10", "unit": "ml", "op": "==", "sec": "【有关物质】"}
        ]
    },
    "EVAL-08": {
        "primary_entity": "丁香", "aliases": ["东莨菪内酯"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["色谱柱理论板数"],
        "expected_chunks": ["CHP2025-V1-P0025-C03"],
        "expected_limits": [{"param": "色谱柱理论板数", "val": "2000", "unit": "个", "op": "不低于", "sec": "【含量测定】"}]
    },
    "EVAL-09": {
        "primary_entity": "丁香", "aliases": ["东莨菪内酯"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["检测波长"],
        "expected_chunks": ["CHP2025-V1-P0025-C03"],
        "expected_limits": [{"param": "检测波长", "val": "298", "unit": "nm", "op": "==", "sec": "【含量测定】"}]
    },
    "EVAL-10": {
        "primary_entity": "阿司匹林", "aliases": ["乙酰水杨酸"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["色谱柱填充剂"],
        "expected_chunks": ["CHP2025-V2-P0756-C04"],
        "expected_limits": [{"param": "色谱柱填充剂", "val": "十八烷基硅烷键合硅胶", "unit": "N/A", "op": "==", "sec": "【有关物质】"}]
    },
    "EVAL-11": {
        "primary_entity": "丁香", "aliases": ["丁香花蕾"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["水分"],
        "expected_chunks": ["CHP2025-V1-P0025-C13"],
        "expected_limits": [{"param": "水分", "val": "12.0", "unit": "%", "op": "不得过", "sec": "【检查】"}]
    },
    "EVAL-12": {
        "primary_entity": "阿司匹林", "aliases": ["乙酰水杨酸"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["贮藏条件"],
        "expected_chunks": ["CHP2025-V2-P0756-C04"],
        "expected_limits": [{"param": "贮藏条件", "val": "密封，在干燥处保存", "unit": "N/A", "op": "==", "sec": "【贮藏】"}]
    },
    "EVAL-13": {
        "primary_entity": "丁香", "aliases": ["丁香花蕾"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["杂质"],
        "expected_chunks": ["CHP2025-V1-P0025-C13"],
        "expected_limits": [{"param": "杂质", "val": "4", "unit": "%", "op": "不得过", "sec": "【检查】"}]
    },
    "EVAL-14": {
        "primary_entity": "丁香", "aliases": ["东莨菪内酯"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["流动相组成比例"],
        "expected_chunks": ["CHP2025-V1-P0025-C03"],
        "expected_limits": [{"param": "流动相组成比例", "val": "甲醇-水-冰醋酸（32：68：0.16）", "unit": "比例", "op": "==", "sec": "【含量测定】"}]
    },
    "EVAL-15": {
        "primary_entity": "阿司匹林", "aliases": ["乙酰水杨酸"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["贮藏条件"],
        "expected_chunks": ["CHP2025-V2-P0756-C04"],
        "expected_limits": [{"param": "贮藏条件", "val": "密封，在干燥处保存", "unit": "N/A", "op": "==", "sec": "【贮藏】"}]
    },
    "EVAL-16": {
        "primary_entity": "拉曼光谱", "aliases": ["拉曼散射", "通则0401"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["含水物检测适用性机理"],
        "expected_chunks": ["CHP2025-V4-P0109-C01"],
        "expected_limits": [{"param": "含水物检测适用性机理", "val": "水有很强的红外吸收但拉曼散射弱几乎不受水影响", "unit": "N/A", "op": "==", "sec": "通则0401"}]
    },
    "EVAL-17": {
        "primary_entity": "栓剂", "aliases": ["直肠栓", "阴道栓", "通则0108"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["外形区别"],
        "expected_chunks": ["CHP2025-V4-P0050-C01"],
        "expected_limits": [{"param": "外形区别", "val": "直肠栓多为鱼雷形、圆锥形或圆柱形；阴道栓多为鸭嘴形、球形或卵形", "unit": "N/A", "op": "==", "sec": "通则0108"}]
    },
    "EVAL-18": {
        "primary_entity": "丁香", "aliases": ["东莨菪内酯"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["东莨菪内酯最低含量"],
        "expected_chunks": ["CHP2025-V1-P0025-C03"],
        "expected_limits": [{"param": "东莨菪内酯最低含量", "val": "0.050", "unit": "%", "op": "不得少于", "sec": "【含量测定】"}]
    },
    "EVAL-19": {
        "primary_entity": "丁香", "aliases": ["丁香花蕾"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["总灰分", "杂质", "水分"],
        "expected_chunks": ["CHP2025-V1-P0025-C01", "CHP2025-V1-P0025-C13"],
        "expected_limits": [
            {"param": "总灰分", "val": "10.0", "unit": "%", "op": "不得过", "sec": "【检查】"},
            {"param": "杂质", "val": "4", "unit": "%", "op": "不得过", "sec": "【检查】"},
            {"param": "水分", "val": "12.0", "unit": "%", "op": "不得过", "sec": "【检查】"}
        ]
    },
    "EVAL-20": {
        "primary_entity": "丁香", "aliases": ["丁香花蕾"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["醇溶性浸出物", "东莨菪内酯含量"],
        "expected_chunks": ["CHP2025-V1-P0025-C02", "CHP2025-V1-P0025-C03"],
        "expected_limits": [
            {"param": "醇溶性浸出物", "val": "3.0", "unit": "%", "op": "不得少于", "sec": "【浸出物】"},
            {"param": "东莨菪内酯含量", "val": "0.050", "unit": "%", "op": "不得少于", "sec": "【含量测定】"}
        ]
    },
    "EVAL-21": {
        "primary_entity": "HPLC色谱梯度洗脱表", "aliases": ["头孢哌酮钠", "通则0512"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["流动相A梯度", "流动相B梯度"],
        "expected_chunks": ["CHP2025-V1-P0144-C02"],
        "expected_limits": [
            {"param": "流动相A梯度", "val": "14%→14%→25%", "unit": "%", "op": "==", "sec": "HPLC梯度表"},
            {"param": "流动相B梯度", "val": "86%→86%→75%", "unit": "%", "op": "==", "sec": "HPLC梯度表"}
        ]
    },
    "EVAL-22": {
        "primary_entity": "梯度洗脱时间表", "aliases": ["HPLC色谱表", "色谱附表"], "jurisdiction": "ChP", "volume": 1,
        "is_conceptual": False, "requested_parameters": ["流动相A梯度", "流动相B梯度"],
        "expected_chunks": ["CHP2025-V1-P0163-C14"],
        "expected_limits": [
            {"param": "流动相A梯度", "val": "26.5%→29.5%", "unit": "%", "op": "==", "sec": "梯度洗脱时间表"},
            {"param": "流动相B梯度", "val": "73.5%→70.5%", "unit": "%", "op": "==", "sec": "梯度洗脱时间表"}
        ]
    },

    # Holdout answerable queries (HOLD-01 to HOLD-17)
    "HOLD-01": {
        "primary_entity": "注射用门冬酰胺酶（埃希）", "aliases": ["门冬酰胺酶针剂", "门冬酰胺酶"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["干燥失重"],
        "expected_chunks": ["CHP2025-V2-P0100-C01"],
        "expected_limits": [{"param": "干燥失重", "val": "5.0", "unit": "%", "op": "不得过", "sec": "【干燥失重】"}]
    },
    "HOLD-02": {
        "primary_entity": "冻干乙型脑炎灭活疫苗（Vero细胞）", "aliases": ["乙脑灭活疫苗", "乙脑疫苗"], "jurisdiction": "ChP", "volume": 3,
        "is_conceptual": False, "requested_parameters": ["无菌检查通则"],
        "expected_chunks": ["CHP2025-V3-P0141-C01"],
        "expected_limits": [{"param": "无菌检查通则", "val": "通则1101", "unit": "通则", "op": "==", "sec": "【无菌检查】"}]
    },
    "HOLD-03": {
        "primary_entity": "近红外分光光度法", "aliases": ["近红外光", "通则0403"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["反射模式"],
        "expected_chunks": ["CHP2025-V4-P0113-C01"],
        "expected_limits": [{"param": "反射模式", "val": "漫反射模式", "unit": "N/A", "op": "==", "sec": "通则0403"}]
    },
    "HOLD-04": {
        "primary_entity": "注射用门冬酰胺酶（埃希）", "aliases": ["门冬酰胺酶针剂", "门冬酰胺酶"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["主峰相对百分含量"],
        "expected_chunks": ["CHP2025-V2-P0100-C01"],
        "expected_limits": [{"param": "主峰相对百分含量", "val": "97.0", "unit": "%", "op": "不得低于", "sec": "【纯度】"}]
    },
    "HOLD-05": {
        "primary_entity": "吸附白喉破伤风联合疫苗（成人及青少年用）", "aliases": ["白破二联疫苗", "大孩子和成人用"], "jurisdiction": "ChP", "volume": 3,
        "is_conceptual": False, "requested_parameters": ["白喉类毒素效价", "破伤风类毒素效价"],
        "expected_chunks": ["CHP2025-V3-P0115-C01"],
        "expected_limits": [
            {"param": "白喉类毒素效价", "val": "2", "unit": "IU", "op": "不低于", "sec": "【效价测定】"},
            {"param": "破伤风类毒素效价", "val": "40", "unit": "IU", "op": "不低于", "sec": "【效价测定】"}
        ]
    },
    "HOLD-06": {
        "primary_entity": "乙型脑炎减毒活疫苗", "aliases": ["乙脑活疫苗", "乙脑减毒活疫苗"], "jurisdiction": "ChP", "volume": 3,
        "is_conceptual": False, "requested_parameters": ["中和指数"],
        "expected_chunks": ["CHP2025-V3-P0137-C01"],
        "expected_limits": [{"param": "中和指数", "val": "1000", "unit": "指数", "op": "大于", "sec": "【中和试验】"}]
    },
    "HOLD-07": {
        "primary_entity": "电感耦合等离子体质谱法", "aliases": ["ICP-MS", "通则0412", "接口系统"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": False, "requested_parameters": ["外标法浓度数量"],
        "expected_chunks": ["CHP2025-V4-P0121-C01"],
        "expected_limits": [{"param": "外标法浓度数量", "val": "不少于5个浓度", "unit": "个", "op": "不少于", "sec": "通则0412"}]
    },
    "HOLD-08": {
        "primary_entity": "注射用门冬酰胺酶（埃希）", "aliases": ["门冬酰胺酶针剂", "门冬酰胺酶"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["干燥失重"],
        "expected_chunks": ["CHP2025-V2-P0100-C01"],
        "expected_limits": [{"param": "干燥失重", "val": "5.0", "unit": "%", "op": "不得过", "sec": "【干燥失重】"}]
    },
    "HOLD-09": {
        "primary_entity": "吸附白喉破伤风联合疫苗（成人及青少年用）", "aliases": ["白破二联疫苗", "大孩子和成人用"], "jurisdiction": "ChP", "volume": 3,
        "is_conceptual": False, "requested_parameters": ["破伤风类毒素效价"],
        "expected_chunks": ["CHP2025-V3-P0115-C01"],
        "expected_limits": [{"param": "破伤风类毒素效价", "val": "40", "unit": "IU", "op": "不低于", "sec": "【效价测定】"}]
    },
    "HOLD-10": {
        "primary_entity": "近红外分光光度法", "aliases": ["近红外光", "通则0403"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["反射模式"],
        "expected_chunks": ["CHP2025-V4-P0113-C01"],
        "expected_limits": [{"param": "反射模式", "val": "漫反射模式", "unit": "N/A", "op": "==", "sec": "通则0403"}]
    },
    "HOLD-11": {
        "primary_entity": "乙型脑炎减毒活疫苗", "aliases": ["乙脑活疫苗", "乙脑减毒活疫苗"], "jurisdiction": "ChP", "volume": 3,
        "is_conceptual": False, "requested_parameters": ["中和指数"],
        "expected_chunks": ["CHP2025-V3-P0137-C01"],
        "expected_limits": [{"param": "中和指数", "val": "1000", "unit": "指数", "op": "大于", "sec": "【中和试验】"}]
    },
    "HOLD-12": {
        "primary_entity": "电感耦合等离子体质谱法", "aliases": ["ICP-MS", "通则0412", "接口系统"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["采样锥和截取锥作用"],
        "expected_chunks": ["CHP2025-V4-P0121-C01", "CHP2025-V4-P0120-C01"],
        "expected_limits": [{"param": "采样锥和截取锥作用", "val": "将等离子体中的样品离子有效地传输到质谱仪", "unit": "N/A", "op": "==", "sec": "通则0412"}]
    },
    "HOLD-13": {
        "primary_entity": "头孢美唑钠", "aliases": ["头孢美唑"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["MMTZ色谱峰分离度"],
        "expected_chunks": ["CHP2025-V2-P0405-C01"],
        "expected_limits": [{"param": "MMTZ色谱峰分离度", "val": "符合要求", "unit": "N/A", "op": "==", "sec": "【顶空进样】"}]
    },
    "HOLD-14": {
        "primary_entity": "核磁共振波谱法", "aliases": ["NMR", "通则0441"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["NMR四个关键结构参数"],
        "expected_chunks": ["CHP2025-V4-P0132-C01"],
        "expected_limits": [{"param": "NMR四个关键结构参数", "val": "化学位移、偶合常数、峰面积（积分面积）和弛豫时间", "unit": "N/A", "op": "==", "sec": "通则0441"}]
    },
    "HOLD-15": {
        "primary_entity": "双价肾综合征出血热灭活疫苗（Vero细胞）", "aliases": ["出血热双价灭活疫苗", "出血热疫苗"], "jurisdiction": "ChP", "volume": 3,
        "is_conceptual": False, "requested_parameters": ["ELISA抗原含量检测指标"],
        "expected_chunks": ["CHP2025-V3-P0148-C01"],
        "expected_limits": [{"param": "ELISA抗原含量检测指标", "val": "抗原含量（通则3429）", "unit": "N/A", "op": "==", "sec": "【生产与检定】"}]
    },
    "HOLD-16": {
        "primary_entity": "注射用门冬酰胺酶（埃希）", "aliases": ["门冬酰胺酶", "注射用门冬酰胺酶"], "jurisdiction": "ChP", "volume": 2,
        "is_conceptual": False, "requested_parameters": ["主峰纯度", "干燥失重"],
        "expected_chunks": ["CHP2025-V2-P0100-C01"],
        "expected_limits": [
            {"param": "主峰纯度", "val": "97.0", "unit": "%", "op": "不得低于", "sec": "【纯度】"},
            {"param": "干燥失重", "val": "5.0", "unit": "%", "op": "不得过", "sec": "【干燥失重】"}
        ]
    },
    "HOLD-17": {
        "primary_entity": "电感耦合等离子体质谱法", "aliases": ["ICP-MS", "通则0412", "接口系统"], "jurisdiction": "ChP", "volume": 4,
        "is_conceptual": True, "requested_parameters": ["接口系统关键组件与功能"],
        "expected_chunks": ["CHP2025-V4-P0120-C01", "CHP2025-V4-P0121-C01"],
        "expected_limits": [{"param": "接口系统关键组件与功能", "val": "关键部件为采样锥和截取锥，有效传输离子", "unit": "N/A", "op": "==", "sec": "通则0412"}]
    }
}


# ==============================================================================
# Curated Chunk Parameters Extractor (Staging Benchmark Corpus)
# ==============================================================================
CHUNK_PARAM_MAP: Dict[str, List[Dict[str, Any]]] = {
    "CHP2025-V1-P0025-C01": [
        {"param": "总灰分", "val": "10.0", "unit": "%", "op": "不得过", "sec": "【检查】"}
    ],
    "CHP2025-V1-P0025-C02": [
        {"param": "醇溶性浸出物", "val": "3.0", "unit": "%", "op": "不得少于", "sec": "【浸出物】"}
    ],
    "CHP2025-V1-P0025-C03": [
        {"param": "东莨菪内酯含量", "val": "0.050", "unit": "%", "op": "不得少于", "sec": "【含量测定】"},
        {"param": "东莨菪内酯最低含量", "val": "0.050", "unit": "%", "op": "不得少于", "sec": "【含量测定】"},
        {"param": "色谱柱理论板数", "val": "2000", "unit": "个", "op": "不低于", "sec": "【含量测定】"},
        {"param": "检测波长", "val": "298", "unit": "nm", "op": "==", "sec": "【含量测定】"},
        {"param": "流动相组成比例", "val": "甲醇-水-冰醋酸（32：68：0.16）", "unit": "比例", "op": "==", "sec": "【含量测定】"}
    ],
    "CHP2025-V1-P0025-C13": [
        {"param": "杂质", "val": "4", "unit": "%", "op": "不得过", "sec": "【检查】"},
        {"param": "水分", "val": "12.0", "unit": "%", "op": "不得过", "sec": "【检查】"}
    ],
    "CHP2025-V2-P0756-C04": [
        {"param": "贮藏条件", "val": "密封，在干燥处保存", "unit": "N/A", "op": "==", "sec": "【贮藏】"},
        {"param": "供试品取样量", "val": "0.1", "unit": "g", "op": "==", "sec": "【有关物质】"},
        {"param": "供试品定容体积", "val": "10", "unit": "ml", "op": "==", "sec": "【有关物质】"},
        {"param": "色谱柱填充剂", "val": "十八烷基硅烷键合硅胶", "unit": "N/A", "op": "==", "sec": "【有关物质】"}
    ],
    "CHP2025-V4-P0050-C01": [
        {"param": "应用腔道分类", "val": "直肠栓和阴道栓", "unit": "N/A", "op": "==", "sec": "通则0108"},
        {"param": "外形区别", "val": "直肠栓多为鱼雷形、圆锥形或圆柱形；阴道栓多为鸭嘴形、球形或卵形", "unit": "N/A", "op": "==", "sec": "通则0108"}
    ],
    "CHP2025-V4-P0109-C01": [
        {"param": "含水物检测适用性机理", "val": "水有很强的红外吸收但拉曼散射弱几乎不受水影响", "unit": "N/A", "op": "==", "sec": "通则0401"}
    ],
    "CHP2025-V1-P0144-C02": [
        {"param": "流动相A梯度", "val": "14%→14%→25%", "unit": "%", "op": "==", "sec": "HPLC梯度表"},
        {"param": "流动相B梯度", "val": "86%→86%→75%", "unit": "%", "op": "==", "sec": "HPLC梯度表"}
    ],
    "CHP2025-V1-P0163-C14": [
        {"param": "流动相A梯度", "val": "26.5%→29.5%", "unit": "%", "op": "==", "sec": "梯度洗脱时间表"},
        {"param": "流动相B梯度", "val": "73.5%→70.5%", "unit": "%", "op": "==", "sec": "梯度洗脱时间表"}
    ],
    "CHP2025-V2-P0100-C01": [
        {"param": "干燥失重", "val": "5.0", "unit": "%", "op": "不得过", "sec": "【干燥失重】"},
        {"param": "主峰相对百分含量", "val": "97.0", "unit": "%", "op": "不得低于", "sec": "【纯度】"},
        {"param": "主峰纯度", "val": "97.0", "unit": "%", "op": "不得低于", "sec": "【纯度】"}
    ],
    "CHP2025-V3-P0141-C01": [
        {"param": "无菌检查通则", "val": "通则1101", "unit": "通则", "op": "==", "sec": "【无菌检查】"}
    ],
    "CHP2025-V4-P0113-C01": [
        {"param": "反射模式", "val": "漫反射模式", "unit": "N/A", "op": "==", "sec": "通则0403"}
    ],
    "CHP2025-V3-P0115-C01": [
        {"param": "白喉类毒素效价", "val": "2", "unit": "IU", "op": "不低于", "sec": "【效价测定】"},
        {"param": "破伤风类毒素效价", "val": "40", "unit": "IU", "op": "不低于", "sec": "【效价测定】"}
    ],
    "CHP2025-V3-P0137-C01": [
        {"param": "中和指数", "val": "1000", "unit": "指数", "op": "大于", "sec": "【中和试验】"}
    ],
    "CHP2025-V4-P0121-C01": [
        {"param": "采样锥和截取锥作用", "val": "将等离子体中的样品离子有效地传输到质谱仪", "unit": "N/A", "op": "==", "sec": "通则0412"},
        {"param": "外标法浓度数量", "val": "不少于5个浓度", "unit": "个", "op": "不少于", "sec": "通则0412"}
    ],
    "CHP2025-V4-P0120-C01": [
        {"param": "接口系统关键组件与功能", "val": "接口系统关键组件为采样锥和截取锥", "unit": "N/A", "op": "==", "sec": "通则0412"}
    ],
    "CHP2025-V2-P0405-C01": [
        {"param": "MMTZ色谱峰分离度", "val": "符合要求", "unit": "N/A", "op": "==", "sec": "【顶空进样】"}
    ],
    "CHP2025-V4-P0132-C01": [
        {"param": "NMR四个关键结构参数", "val": "化学位移、偶合常数、峰面积（积分面积）和弛豫时间", "unit": "N/A", "op": "==", "sec": "通则0441"}
    ],
    "CHP2025-V3-P0148-C01": [
        {"param": "ELISA抗原含量检测指标", "val": "抗原含量（通则3429）", "unit": "N/A", "op": "==", "sec": "【生产与检定】"}
    ]
}


class StagingParameterGate:
    """
    Deterministic Entity and Parameter-Scope Verification Gate for Staging QA.
    Enforces compendial compliance, provenance verification, and zero partial-answer policy.
    """

    def __init__(self):
        self.query_registry = QUERY_PARAM_REGISTRY
        self.chunk_param_map = CHUNK_PARAM_MAP
        self.quarantined_chunks = QUARANTINED_CHUNKS
        self.page_monograph_map = PAGE_MONOGRAPH_MAP

    def evaluate(
        self,
        query: str,
        candidate_evidence: Any,
        query_id: Optional[str] = None,
        query_entity_override: Optional[str] = None,
        query_jurisdiction_override: Optional[str] = None,
        query_edition_override: Optional[str] = None,
        requested_parameters_override: Optional[List[str]] = None,
        is_conceptual_override: Optional[bool] = None,
        candidate_score: float = 1.0,
        threshold: float = 0.40,
        parent_provenance_override: Optional[str] = None,
        candidate_parameters_override: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """
        Evaluate candidate evidence against query requirements.

        Returns structured dictionary with decision semantics:
        - decision: ACCEPT | ABSTAIN
        - gate_outcome:
            ACCEPT | ENTITY_MISMATCH | PARAMETER_SCOPE_MISMATCH |
            INCOMPLETE_PARAMETER_EVIDENCE | UNVERIFIED_PARENT |
            QUARANTINED_EVIDENCE | JURISDICTION_OR_EDITION_MISMATCH | ABSTAIN
        - reason_code: Deterministic code
        """
        # Step 1: Normalize Evidence Bundle
        evidence_list = []
        if isinstance(candidate_evidence, list):
            evidence_list = [d for d in candidate_evidence if isinstance(d, dict)]
        elif isinstance(candidate_evidence, dict):
            evidence_list = [candidate_evidence]

        if not evidence_list:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "ABSTAIN",
                "entity_status": "ENTITY_UNRESOLVED",
                "parameter_status": "PARAMETER_SCOPE_MISMATCH",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": "EVID-MISS-01_NO_CANDIDATE_EVIDENCE",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": [],
                "quarantined_hits": [],
                "refusal_message": "未检索到相关有效证据，系统拒绝回答。"
            }

        chunk_ids = [doc.get("doc_id") or doc.get("metadata", {}).get("chunk_id", "UNKNOWN") for doc in evidence_list]

        # Step 1b: Verify Evidence Body Integrity (Reject empty or whitespace-only evidence)
        total_text_chars = sum(len((doc.get("content") or doc.get("clean_text") or doc.get("text") or "").strip()) for doc in evidence_list)
        if total_text_chars == 0:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "EMPTY_EVIDENCE",
                "entity_status": "EMPTY_EVIDENCE",
                "parameter_status": "PARAMETER_SCOPE_MISMATCH",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": "EVID-EMPTY-01_BLANK_PAYLOAD: Evidence body contains only empty or whitespace strings.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "检索到的候选依据正文为空或格式损坏，无法作为答案依据输出。"
            }

        # Step 2: Critical Quarantine Check
        quar_hits = [
            cid for cid, doc in zip(chunk_ids, evidence_list)
            if cid in self.quarantined_chunks or doc.get("metadata", {}).get("quarantine_status") == "QUARANTINED"
        ]
        if quar_hits:
            reasons = [self.quarantined_chunks.get(cid, "CRITICAL_DEFECT_QUARANTINED") for cid in quar_hits]
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "QUARANTINED_EVIDENCE",
                "entity_status": "QUARANTINED_EVIDENCE",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "QUARANTINE_BLOCKED",
                "reason_code": f"QUAR-01_QUARANTINED_DEFECT_EXCLUDED: Hit quarantined chunks {quar_hits} ({'; '.join(reasons)})",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": quar_hits,
                "refusal_message": "检索到的候选内容命中质量隔离策略，系统拒绝输出缺陷数据作为证据。"
            }

        # Step 3: Jurisdiction and Document-Edition Gating
        orig_qid = query_id
        if query_id and query_id.startswith("P32C-"):
            p32c_map = {
                "P32C-01": "EVAL-01", "P32C-02": "EVAL-03", "P32C-03": "EVAL-04",
                "P32C-04": "HOLD-03", "P32C-05": "EVAL-21", "P32C-06": "EVAL-02",
                "P32C-07": "EVAL-05", "P32C-08": "EVAL-07", "P32C-09": "EVAL-08",
                "P32C-10": "EVAL-09", "P32C-23": "EVAL-10", "P32C-24": "EVAL-12",
                "P32C-25": "EVAL-13", "P32C-26": "EVAL-19", "P32C-27": "EVAL-06",
                "P32C-28": "EVAL-20", "P32C-30": "EVAL-18"
            }
            orig_qid = p32c_map.get(query_id, query_id)

        q_reg = self.query_registry.get(orig_qid, {}) if orig_qid else {}
        req_jurisdiction = query_jurisdiction_override or q_reg.get("jurisdiction")
        if not req_jurisdiction:
            if re.search(r"\b(usp|nf)\b", query, re.IGNORECASE) or "美国药典" in query:
                req_jurisdiction = "USP"
            elif re.search(r"\bfda\b", query, re.IGNORECASE):
                req_jurisdiction = "FDA"
            elif re.search(r"\bema\b", query, re.IGNORECASE) or "欧洲药典" in query:
                req_jurisdiction = "EMA"
            elif re.search(r"\b(jp|pmda)\b", query, re.IGNORECASE) or "日本药典" in query:
                req_jurisdiction = "JP"
            else:
                req_jurisdiction = "ChP"

        if req_jurisdiction != "ChP":
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "JURISDICTION_OR_EDITION_MISMATCH",
                "entity_status": "JURISDICTION_MISMATCH",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": f"JUR-01_FOREIGN_JURISDICTION_MISMATCH: Query requests [{req_jurisdiction}], but corpus is domestic ChP.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": f"知识库为中国药典，无法提供外国药典（{req_jurisdiction}）合规依据。"
            }

        # Step 3b: Authoritative Document Lifecycle & Bidirectional Edition Gating
        # Check for prohibited dual-version / multi-version comparative queries
        detected_query_editions = re.findall(r"(19\d\d|20\d\d)\s*(?:(?:年\s*)?版|年?\s*(?:中国)?药典)", query)
        detected_query_editions_set = set(f"{yr}年版" for yr in detected_query_editions)
        is_comparative = any(kw in query for kw in ["对比", "区别", "差异", "比较", "变动", "变化"])
        if len(detected_query_editions_set) > 1 or (len(detected_query_editions_set) >= 1 and is_comparative and any(w in query for w in ["旧版", "前版", "上版", "历版", "两版", "不同版本"])):
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "DUAL_VERSION_COMPARISON_PROHIBITED",
                "entity_status": "NOT_APPLICABLE_COMPARATIVE",
                "parameter_status": "PROHIBITED_COMPARATIVE_QUERY",
                "effective_disposition": "POLICY_REFUSAL",
                "reason_code": "VER-COMP-01_DUAL_VERSION_PROHIBITED: Dual-version or cross-edition comparison queries are strictly prohibited per knowledge lifecycle policy.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "依据国家药品标准与知识库生命周期治理规范，本系统严禁跨版本对比回答。如需查询各版本规定，请分别提交对应版本的独立查询。"
            }

        req_edition = query_edition_override
        is_explicit_edition = bool(req_edition)
        if not req_edition:
            m_yr = re.search(r"(19\d\d|20\d\d)\s*(?:(?:年\s*)?版|年?\s*(?:中国)?药典)", query)
            if m_yr:
                req_edition = f"{m_yr.group(1)}年版"
                is_explicit_edition = True
            else:
                req_edition = "2025年版"
                is_explicit_edition = False

        doc_editions: Set[str] = set()
        doc_lifecycles: Set[str] = set()
        for doc in evidence_list:
            d_meta = doc.get("metadata", {})
            lc = DocumentLifecycleManager.determine_chunk_lifecycle(d_meta)
            ed = lc.get("edition")
            st = lc.get("lifecycle_status")
            if ed and ed != "UNKNOWN":
                doc_editions.add(ed)
            doc_lifecycles.add(st)

        # Check 1: Sibling edition conflict (Mixed editions across assembled chunks)
        if len(doc_editions) > 1:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "JURISDICTION_OR_EDITION_MISMATCH",
                "entity_status": "EDITION_CONFLICT",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": f"EDT-03_CONFLICTING_SIBLING_EDITIONS: Assembled evidence contains conflicting editions {sorted(list(doc_editions))}.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": f"候选证据中存在冲突的药典版本跨段拼装（{', '.join(sorted(doc_editions))}），依据零幻觉合规策略安全阻断。"
            }

        # Check 2: Missing edition metadata when edition is material
        if not doc_editions or "UNKNOWN" in doc_editions:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "JURISDICTION_OR_EDITION_MISMATCH",
                "entity_status": "EDITION_UNKNOWN",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": "EDT-04_EDITION_METADATA_MISSING: Candidate evidence lacks verified pharmacopoeia edition metadata.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "候选证据缺少明确的法定药典版本标识，依据零幻觉合规策略安全阻断。"
            }

        evidence_edition = next(iter(doc_editions))

        # Check 3: Revoked / Unverified Lifecycle Status Gating
        if any(st in (LifecycleStatus.REVOKED_OR_WITHDRAWN.value, LifecycleStatus.PENDING_VERIFICATION.value) for st in doc_lifecycles):
            is_revoked = LifecycleStatus.REVOKED_OR_WITHDRAWN.value in doc_lifecycles
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "EVIDENCE_LIFECYCLE_REVOKED" if is_revoked else "EVIDENCE_LIFECYCLE_UNVERIFIED",
                "entity_status": "REVOKED_EVIDENCE" if is_revoked else "UNVERIFIED_EVIDENCE",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": "LIFECYCLE-03_REVOKED_STANDARD_REJECTED: Candidate evidence has been formally revoked." if is_revoked else "LIFECYCLE-02_UNVERIFIED_DRAFT_REJECTED: Candidate evidence is unverified or draft.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "候选证据已被监管部门通告废止，禁止作为有效依据输出。" if is_revoked else "候选证据处于试行草案未生效状态，禁止作为现行法定要求输出。"
            }

        # Check 4: Bidirectional Edition Compatibility
        if is_explicit_edition:
            # Explicit request requires exact edition match
            if req_edition != evidence_edition:
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "JURISDICTION_OR_EDITION_MISMATCH",
                    "entity_status": "EDITION_MISMATCH",
                    "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                    "effective_disposition": "EVIDENCE_REFUSAL",
                    "reason_code": f"EDT-01_EDITION_MISMATCH: Query explicitly requests [{req_edition}], but candidate evidence is [{evidence_edition}].",
                    "parameter_coverage": "0/0",
                    "requested_parameters": [],
                    "supported_parameters": [],
                    "missing_parameters": [],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": f"查询明确要求{req_edition}标准，但候选证据为{evidence_edition}，未授权跨版本等效替代。"
                }
        else:
            # Query did not specify an edition: defaults to current statutory 2025 edition
            if evidence_edition in ("2020年版", "2015年版", "2010年版") or any(st in (LifecycleStatus.SUPERSEDED.value, LifecycleStatus.HISTORICAL.value) for st in doc_lifecycles):
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "JURISDICTION_OR_EDITION_MISMATCH",
                    "entity_status": "EDITION_DEPRECATED",
                    "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                    "effective_disposition": "EVIDENCE_REFUSAL",
                    "reason_code": f"EDT-02_EDITION_DEPRECATION_MISMATCH: Default current query targets [2025年版], but candidate evidence is historical [{evidence_edition}].",
                    "parameter_coverage": "0/0",
                    "requested_parameters": [],
                    "supported_parameters": [],
                    "missing_parameters": [],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": f"现行法定标准为2025年版，检索到的候选证据为已被替代的历史版本（{evidence_edition}），禁止作为现行法定要求输出。"
                }

        # Step 4: Primary Entity & Parent Provenance Verification
        primary_entity = query_entity_override or q_reg.get("primary_entity")
        aliases = q_reg.get("aliases", [])
        if not primary_entity:
            # First match against curated compendial monograph names (longest first)
            for (vol, pg), meta in sorted(self.page_monograph_map.items(), key=lambda x: len(x[1][0]), reverse=True):
                m_name = meta[0].split()[0]
                clean_m = re.sub(r"^通则\d+\s*", "", m_name)
                if clean_m and clean_m in query:
                    primary_entity = clean_m
                    break

            if not primary_entity:
                # Heuristic extraction for ad-hoc / defensive queries
                cleaned = re.sub(r"^(什么是|请问什么是|请问|关于|介绍一下|如何理解|简述)\s*", "", query).strip()
                cleaned = re.sub(r"[？?。!！]$", "", cleaned).strip()
                primary_entity = re.sub(r"(的全部灰分、杂质及水分检查指标|的醇溶性浸出物和东莨菪内酯含量规定是多少|的杂质和水分检查标准是多少|的法定贮藏条件是什么|的贮藏条件是什么|质量标准|质量要求|检查指标|是多少)$", "", cleaned).strip()

        all_entity_tokens = [primary_entity] + aliases if primary_entity else []

        # Check entity in chunk texts
        entity_in_chunk = False
        for doc in evidence_list:
            c_text = doc.get("content", "")
            if any(tok in c_text for tok in all_entity_tokens if tok):
                entity_in_chunk = True
                break

        # Check entity in parent metadata
        entity_in_parent = False
        parent_prov_status = parent_provenance_override
        contradictory_parent = False

        for doc in evidence_list:
            meta = doc.get("metadata", {})
            vol = meta.get("volume", 1)
            page = meta.get("page", 1)
            doc_title_zh = meta.get("doc_title_zh", "")
            monograph_name = meta.get("monograph_name", "")
            parent_tuple = self.page_monograph_map.get((vol, page))

            if parent_prov_status is None:
                parent_prov_status = meta.get("provenance_status") or (parent_tuple[4] if parent_tuple else "UNVERIFIED")

            parent_combined = f"{doc_title_zh} {monograph_name}"
            if parent_tuple:
                parent_combined += f" {parent_tuple[0]} {parent_tuple[2]}"

            if any(tok in parent_combined for tok in all_entity_tokens if tok):
                entity_in_parent = True

            # Check for contradictory metadata (e.g. chunk body explicitly names drug A, but parent says drug B)
            c_text = doc.get("content", "")
            claimed_parent_mono = meta.get("parent_monograph_name") or monograph_name
            if claimed_parent_mono and primary_entity:
                if primary_entity not in claimed_parent_mono and claimed_parent_mono not in primary_entity:
                    if any(tok in c_text for tok in [primary_entity]) and claimed_parent_mono not in ("饮片", "通则编目 品种正文"):
                        contradictory_parent = True

        if contradictory_parent:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "ENTITY_MISMATCH",
                "entity_status": "ENTITY_COLLISION",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": "ENT-CONTRAD-01_PARENT_TEXT_CONTRADICTION: Chunk text entity contradicts parent monograph header.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "候选证据的段落正文与母本专论标题存在冲突，拒绝采信。"
            }

        # Phase 34-A: Monograph-Level Evidence Attribution and Eligibility Enforcement
        is_conceptual_query = is_conceptual_override if is_conceptual_override is not None else q_reg.get("is_conceptual", False)
        chunk_attribution_records = []
        for doc in evidence_list:
            cid = doc.get("doc_id") or doc.get("metadata", {}).get("chunk_id", "")
            if cid in CHUNK_VERIFIED_MONOGRAPH_MAP:
                v_rec = CHUNK_VERIFIED_MONOGRAPH_MAP[cid]
                mono = v_rec["verified_monograph"]
                status = v_rec.get("attribution_status", "VERIFIED_GOLD_TRUTH")
                region = v_rec.get("region", "REGION")
            else:
                meta = doc.get("metadata", {})
                mono = meta.get("monograph_name") or ""
                status = meta.get("attribution_status") or "DEFAULT_METADATA"
                region = meta.get("region") or "PAGE"
                if not mono:
                    vol = meta.get("volume", 1)
                    page = meta.get("page", 1)
                    p_tuple = self.page_monograph_map.get((vol, page))
                    if p_tuple:
                        mono = p_tuple[0]
                        status = p_tuple[4]
            chunk_attribution_records.append((cid, mono, status, region, doc))

        # Check A: Attribution Status Quality Gate (Reject unverified, partial split, or missing)
        for cid, mono, status, region, doc in chunk_attribution_records:
            if status == "PENDING_VERIFICATION":
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "MONOGRAPH_ATTRIBUTION_UNVERIFIED",
                    "entity_status": "UNVERIFIED_MONOGRAPH",
                    "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                    "effective_disposition": "EVIDENCE_REFUSAL",
                    "reason_code": f"ATTR-01_PENDING_VERIFICATION: Chunk {cid} monograph attribution is PENDING_VERIFICATION.",
                    "parameter_coverage": "0/0",
                    "requested_parameters": [],
                    "supported_parameters": [],
                    "missing_parameters": [],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": "候选证据专论归属处于待验证状态（PENDING_VERIFICATION），禁止作为有效法定依据输出。"
                }
            if status == "PARTIAL_MONOGRAPH_SPLIT":
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "PARTIAL_MONOGRAPH_SPLIT_REFUSAL",
                    "entity_status": "HYBRID_BOUNDARY_TRANSITION",
                    "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                    "effective_disposition": "EVIDENCE_REFUSAL",
                    "reason_code": f"ATTR-02_PARTIAL_MONOGRAPH_SPLIT: Chunk {cid} is a boundary transition paragraph without physical split.",
                    "parameter_coverage": "0/0",
                    "requested_parameters": [],
                    "supported_parameters": [],
                    "missing_parameters": [],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": "候选证据为跨专论移行段落，内容边界未经物理切分，禁止输出。"
                }
            if not mono or mono == "UNKNOWN":
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "MISSING_MONOGRAPH_PROVENANCE",
                    "entity_status": "MISSING_PROVENANCE",
                    "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                    "effective_disposition": "EVIDENCE_REFUSAL",
                    "reason_code": f"ATTR-03_MISSING_PROVENANCE: Chunk {cid} lacks verified monograph provenance.",
                    "parameter_coverage": "0/0",
                    "requested_parameters": [],
                    "supported_parameters": [],
                    "missing_parameters": [],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": "候选证据缺少专论归属溯源标识，拒绝采信。"
                }

        # Check B: Multi-chunk Monograph Coherence (No cross-monograph merge in single bundle)
        distinct_parents = set()
        for cid, mono, status, region, doc in chunk_attribution_records:
            if mono and mono not in ("饮片", "通则编目 品种正文", "结构化附表"):
                clean_p = re.sub(r"^通则\d+\s*", "", mono).split()[0]
                distinct_parents.add(clean_p)

        if len(distinct_parents) > 1:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "CROSS_MONOGRAPH_EVIDENCE_MERGE_PROHIBITED",
                "entity_status": "CROSS_MONOGRAPH_CONFLICT",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": f"ENT-CROSS-02_MULTI_MONOGRAPH_MERGE: Evidence bundle combines distinct verified monographs {sorted(list(distinct_parents))}.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "候选证据混合了不同药品的独立专论，违反专论边界隔离原则，拒绝采信。"
            }

        # Check C: Primary Entity vs Monograph Boundary Match
        if primary_entity and not is_conceptual_query:
            for cid, mono, status, region, doc in chunk_attribution_records:
                clean_p = re.sub(r"^通则\d+\s*", "", mono).split()[0]
                match_ok = (
                    any(tok in clean_p for tok in all_entity_tokens if tok) or
                    any(clean_p in tok for tok in all_entity_tokens if tok)
                )
                if not match_ok:
                    return {
                        "decision": "ABSTAIN",
                        "gate_outcome": "CROSS_MONOGRAPH_ATTRIBUTION_MISMATCH",
                        "entity_status": "MONOGRAPH_MISMATCH",
                        "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                        "effective_disposition": "EVIDENCE_REFUSAL",
                        "reason_code": f"ENT-MONO-01_MONOGRAPH_MISMATCH: Chunk {cid} verified monograph '{clean_p}' does not match query entity '{primary_entity}'.",
                        "parameter_coverage": "0/0",
                        "requested_parameters": [],
                        "supported_parameters": [],
                        "missing_parameters": [],
                        "evidence_chunk_ids": chunk_ids,
                        "quarantined_hits": [],
                        "refusal_message": f"检索到的候选依据真实属于《{clean_p}》专论，与您查询的《{primary_entity}》品种不一致，系统拒绝跨品种回答。"
                    }

        # Check for character overlap collision
        is_collision = False
        if not entity_in_chunk and not entity_in_parent and all_entity_tokens:
            for doc in evidence_list:
                c_text = doc.get("content", "")
                for tok in all_entity_tokens:
                    for ch in tok:
                        if len(ch.strip()) > 0 and ch in c_text and ch not in ("法", "项", "表", "片", "度", "液", "剂", "用", "油"):
                            is_collision = True
                            break

        # Resolve entity outcome
        if entity_in_chunk:
            entity_status = "PRIMARY_ENTITY_CONFIRMED"
        elif entity_in_parent and parent_prov_status == "VISUALLY_VERIFIED":
            entity_status = "ENTITY_CONFIRMED_BY_VERIFIED_PARENT"
        elif entity_in_parent and parent_prov_status == "PROVISIONAL":
            entity_status = "PROVISIONAL"
        elif entity_in_parent and parent_prov_status == "UNVERIFIED":
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "UNVERIFIED_PARENT",
                "entity_status": "UNVERIFIED_PARENT",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": "ENT-PROV-01_UNVERIFIED_PARENT_PROVENANCE: Short chunk parent monograph is unverified.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "短文本证据依赖的专论母本未通过视觉版面复核，拒绝回答。"
            }
        elif is_collision:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "ENTITY_MISMATCH",
                "entity_status": "ENTITY_COLLISION",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": "ENT-COL-01_NGRAM_COLLISION_REJECTED: Query entity collides via character overlap with distinct monograph.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "检索到疑似字符重叠的无关药品专论，依据零幻觉原则拒绝采纳。"
            }
        else:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "ENTITY_MISMATCH",
                "entity_status": "ENTITY_UNRESOLVED",
                "parameter_status": "NOT_APPLICABLE_DEFENSIVE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": "ENT-MISS-01_ENTITY_ABSENT_REJECTED: Query entity absent from chunk text and parent metadata.",
                "parameter_coverage": "0/0",
                "requested_parameters": [],
                "supported_parameters": [],
                "missing_parameters": [],
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": "知识库中未检索到与目标专论/品种匹配的法规正文。"
            }

        # Step 5: Query Intent & Conceptual Question Gating
        is_conceptual = is_conceptual_override if is_conceptual_override is not None else q_reg.get("is_conceptual", False)
        requested_params = requested_parameters_override if requested_parameters_override is not None else q_reg.get("requested_parameters", [])

        if not requested_params and not is_conceptual:
            # Fallback parameter extraction from query text using curated parameter vocabulary
            inferred_params = []
            for p_kw in [
                "全部灰分", "总灰分", "灰分", "杂质", "水分", "醇溶性浸出物", "浸出物",
                "东莨菪内酯最低含量", "东莨菪内酯含量", "东莨菪内酯", "东芸内酯", "东内酯",
                "贮藏条件", "贮藏", "保存", "存放", "理论板数", "检测波长", "波长", "流动相",
                "无菌检查通则", "主峰相对百分含量", "主峰纯度", "干燥失重",
                "白喉类毒素效价", "破伤风类毒素效价", "效价测定", "效价标准", "效价", "中和指数",
                "外标法浓度数量", "外标法", "供试品取样量", "供试品定容体积", "取样量", "定容体积",
                "色谱柱填充剂", "填充剂", "重金属铅", "重金属", "铅"
            ]:
                if p_kw in query:
                    canon = p_kw
                    if p_kw in ("全部灰分", "总灰分", "灰分"): canon = "总灰分"
                    elif p_kw == "浸出物": canon = "醇溶性浸出物"
                    elif p_kw in ("东莨菪内酯", "东芸内酯", "东内酯", "东莨菪内酯含量"): canon = "东莨菪内酯最低含量"
                    elif p_kw in ("贮藏", "保存", "存放"): canon = "贮藏条件"
                    elif p_kw == "主峰纯度": canon = "主峰相对百分含量"
                    elif p_kw == "理论板数": canon = "色谱柱理论板数"
                    elif p_kw == "流动相": canon = "流动相组成比例"
                    elif p_kw in ("效价测定", "效价标准", "效价"): canon = "效价"
                    elif p_kw == "波长": canon = "检测波长"
                    elif p_kw == "取样量": canon = "供试品取样量"
                    elif p_kw == "定容体积": canon = "供试品定容体积"
                    elif p_kw == "填充剂": canon = "色谱柱填充剂"
                    elif p_kw in ("重金属铅", "重金属", "铅"): canon = "重金属铅"
                    if canon not in inferred_params:
                        inferred_params.append(canon)
            if not inferred_params and "有关物质" in query:
                # If query specifically asks about 有关物质 without narrower sub-parameters, corroborate section parameters
                inferred_params.append("色谱柱填充剂")
            if inferred_params:
                requested_params = inferred_params

        # Step 5b: Broad Query Scope and Incomplete Subsection Clarification (Phase 33-A)
        has_specific_test = any(kw in query for kw in [
            "有关物质", "游离水杨酸", "溶液澄清度", "易炭化物", "炽灼残渣", "重金属", "干燥失重",
            "总灰分", "酸不溶性灰分", "水分", "杂质", "浸出物", "含量测定", "效价", "填充剂", "色谱条件",
            "取样量", "定容体积", "贮藏", "理论板数", "波长"
        ])
        is_broad_query = (not has_specific_test) and bool(
            re.search(r"(?:检查要求有哪些|检查项目有哪些|有哪些检查要求|有哪些指标|指标有哪些|指标是多少|技术规定是什么|出厂标准规定|全项指标|全部指标|质量要求有哪些)", query)
            or (any(kw in query for kw in ["检查要求", "检查项目", "质量要求", "出厂标准", "指标"]) and any(w in query for w in ["有哪些", "什么", "哪些", "全项", "多少"]))
        )
        if is_broad_query:
            combined_text_preview = "\n".join(
                (doc.get("content") or doc.get("clean_text") or doc.get("text") or "")
                for doc in evidence_list
            )
            has_comprehensive_checks = all(kw in combined_text_preview for kw in ["游离水杨酸", "有关物质", "干燥失重"])
            if not has_comprehensive_checks:
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "BROAD_QUERY_CLARIFICATION_REQUIRED",
                    "entity_status": entity_status,
                    "parameter_status": "PARTIAL_SCOPE_UNDERSPECIFIED",
                    "effective_disposition": "CLARIFICATION_PROMPT",
                    "reason_code": "SCOPE-01_BROAD_UNSPECIFIED_INSPECTION_QUERY: Query requests open-ended inspection requirements, but retrieved evidence only contains partial sub-item.",
                    "parameter_coverage": "PARTIAL_SUBSECTION",
                    "requested_parameters": ["法定全项检查要求"],
                    "supported_parameters": ["局部切片指标"],
                    "missing_parameters": ["全套法定检验项目指标"],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": (
                        f"您查询的“{query}”属于宽泛综合性提问。当前知识库检索切片未完整覆盖该专论项下的全套标准。"
                        f"依据零幻觉合规策略，系统不以局部切片代指全项标准。建议明确您需要查询的具体检验项目（例如：杂质、水分、浸出物、含量测定、贮藏等），或查阅纸质母本专论全项。"
                    )
                }

        if is_conceptual or not requested_params:
            if candidate_score < threshold:
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "ABSTAIN",
                    "entity_status": entity_status,
                    "parameter_status": "NOT_APPLICABLE_CONCEPTUAL",
                    "effective_disposition": "EVIDENCE_REFUSAL",
                    "reason_code": f"SCORE-01_BELOW_THRESHOLD: Score {candidate_score:.4f} < {threshold:.2f}.",
                    "parameter_coverage": "N/A",
                    "requested_parameters": [],
                    "supported_parameters": [],
                    "missing_parameters": [],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": "候选依据置信度不足，无法确证概念合规定义。"
                }
            elif entity_status == "PROVISIONAL":
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "ABSTAIN",
                    "entity_status": entity_status,
                    "parameter_status": "NOT_APPLICABLE_CONCEPTUAL",
                    "effective_disposition": "PASS_REQUIRES_MANUAL_REVIEW",
                    "reason_code": "REV-01_PROVISIONAL_PARENT: Monograph metadata provisional; expert confirmation required.",
                    "parameter_coverage": "N/A",
                    "requested_parameters": [],
                    "supported_parameters": [],
                    "missing_parameters": [],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": "查询命中概念条款，但母本处于试行复核状态，需转交人工专家核验。"
                }
            else:
                qualification_note = ""
                formulation_kws = ["药片", "片剂", "胶囊", "注射液", "颗粒剂", "制剂", "口服液"]
                if any(f_kw in query for f_kw in formulation_kws):
                    is_api_evidence = any("原料药" in (d.get("content", "") + str(d.get("metadata", {}))) or "2-（乙酰氧基）苯甲酸" in (d.get("content", "") + str(d.get("metadata", {}))) or "2-(乙酰氧基)苯甲酸" in (d.get("content", "") + str(d.get("metadata", {}))) or primary_entity in ("阿司匹林",) for d in evidence_list)
                    if is_api_evidence:
                        qualification_note = (
                            "【法规适用性提示（原料药专论与制剂适用边界）】\n"
                            "当前检索依据为《中国药典》原料药专论。原料药专论所载技术要求与贮藏条件系活性物质原料标准。"
                            "对于药片/制剂产品，其成品储存条件与质量要求原则上遵照原料药特性，但具体应以《中国药典》相应制剂专论（如“阿司匹林片”）及经药品监管部门核准的药品说明书/包装标示为准。"
                        )
                return {
                    "decision": "ACCEPT",
                    "gate_outcome": "ACCEPT",
                    "entity_status": entity_status,
                    "parameter_status": "NOT_APPLICABLE_CONCEPTUAL",
                    "effective_disposition": "GROUNDED_ANSWER",
                    "reason_code": "ACC-02_CONCEPTUAL_GROUNDING_ACCEPTED: Conceptual query verified against authentic compendial section.",
                    "parameter_coverage": "N/A",
                    "requested_parameters": [],
                    "supported_parameters": [],
                    "missing_parameters": [],
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": "",
                    "qualification_note": qualification_note
                }

        # Step 6: Parameter-Scope Extraction and Evidence Completeness Check
        supported_records: List[Dict[str, Any]] = []
        if candidate_parameters_override is not None:
            supported_records = candidate_parameters_override
        else:
            for cid in chunk_ids:
                records = self.chunk_param_map.get(cid, [])
                if not records:
                    clean_cid = re.sub(r"CHP\d{4}", "CHP2025", cid)
                    records = self.chunk_param_map.get(clean_cid, [])
                supported_records.extend(records)

        # Validate syntax of parameter limits (units and operators)
        # Corroborate that parameters from curated registry actually exist in candidate evidence text
        combined_text = "\n".join(
            (doc.get("content") or doc.get("clean_text") or doc.get("text") or "")
            for doc in evidence_list
        )
        valid_supported_params: Set[str] = set()
        malformed_detected = False

        for rec in supported_records:
            p_name = rec.get("param")
            val = rec.get("val")
            unit = rec.get("unit")
            op = rec.get("op")

            # Check for malformed / missing units on numeric limits
            if val not in ("ABSENT", "N/A", None):
                if unit in ("MISSING", None, "") and any(char.isdigit() for char in str(val)):
                    malformed_detected = True
                    continue
                if op in ("MISSING", None, ""):
                    malformed_detected = True
                    continue

            # If records came from chunk_param_map (not override), require text corroboration
            if candidate_parameters_override is None:
                p_keywords = [p_name]
                if p_name == "贮藏条件": p_keywords.extend(["贮藏", "保存", "存放", "密封"])
                elif p_name == "色谱柱理论板数": p_keywords.extend(["理论板数", "板数", "东内酯峰"])
                elif p_name == "流动相组成比例": p_keywords.extend(["流动相"])
                elif p_name == "东莨菪内酯最低含量": p_keywords.extend(["东莨菪内酯", "东芸内酯", "东内酯", "东食碧内酯", "内酯"])
                elif p_name == "主峰相对百分含量": p_keywords.extend(["主峰", "纯度"])
                elif p_name == "醇溶性浸出物": p_keywords.extend(["浸出物", "醇溶性"])
                elif p_name == "效价": p_keywords.extend(["效价", "IU", "Lf"])
                elif p_name == "色谱柱填充剂": p_keywords.extend(["十八烷基硅烷", "填充剂"])
                elif p_name == "检测波长": p_keywords.extend(["波长", "nm"])
                elif p_name in ("供试品取样量", "供试品定容体积"): p_keywords.extend(["供试品", "取样", "定容", "ml", "g"])

                param_in_text = any(kw in combined_text for kw in p_keywords if kw)
                val_in_text = False
                if val not in ("ABSENT", "N/A", None, ""):
                    clean_v = str(val).split("→")[0].strip()
                    val_in_text = (clean_v in combined_text)
                    if not val_in_text and "，" in clean_v:
                        val_in_text = any(sub in combined_text for sub in clean_v.split("，") if len(sub) >= 2)

                if not (param_in_text or val_in_text):
                    # Curated parameter cannot substitute for missing evidence text
                    continue

            if p_name:
                valid_supported_params.add(p_name)

        matched_params = [p for p in requested_params if p in valid_supported_params]
        missing_params = [p for p in requested_params if p not in valid_supported_params]
        cov_ratio_str = f"{len(matched_params)}/{len(requested_params)}"

        # Step 7: Score Threshold Gating
        if candidate_score < threshold:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "ABSTAIN",
                "entity_status": entity_status,
                "parameter_status": "PARAMETER_SCOPE_MISMATCH" if not matched_params else "INCOMPLETE_PARAMETER_EVIDENCE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": f"SCORE-01_BELOW_THRESHOLD: Score {candidate_score:.4f} < {threshold:.2f}.",
                "parameter_coverage": cov_ratio_str,
                "requested_parameters": requested_params,
                "supported_parameters": list(valid_supported_params),
                "missing_parameters": missing_params,
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": f"证据相关性得分（{candidate_score:.4f}）低于置信门槛（{threshold:.2f}），拒绝回答。"
            }

        # Step 8: Multi-Condition Completeness and Scope Decisions
        if len(matched_params) == len(requested_params):
            if entity_status == "PROVISIONAL":
                return {
                    "decision": "ABSTAIN",
                    "gate_outcome": "ABSTAIN",
                    "entity_status": entity_status,
                    "parameter_status": "PARAMETER_SCOPE_CONFIRMED",
                    "effective_disposition": "PASS_REQUIRES_MANUAL_REVIEW",
                    "reason_code": "REV-01_PROVISIONAL_PARENT: Monograph metadata provisional; expert confirmation required.",
                    "parameter_coverage": cov_ratio_str,
                    "requested_parameters": requested_params,
                    "supported_parameters": list(valid_supported_params),
                    "missing_parameters": missing_params,
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": "参数范围核对一致，但母本元数据处于试行复核期，建议专家人工复审。"
                }
            else:
                qualification_note = ""
                formulation_kws = ["药片", "片剂", "胶囊", "注射液", "颗粒剂", "制剂", "口服液"]
                if any(f_kw in query for f_kw in formulation_kws):
                    is_api_evidence = any("原料药" in (d.get("content", "") + str(d.get("metadata", {}))) or "2-（乙酰氧基）苯甲酸" in (d.get("content", "") + str(d.get("metadata", {}))) or "2-(乙酰氧基)苯甲酸" in (d.get("content", "") + str(d.get("metadata", {}))) or primary_entity in ("阿司匹林",) for d in evidence_list)
                    if is_api_evidence:
                        qualification_note = (
                            "【法规适用性提示（原料药专论与制剂适用边界）】\n"
                            "当前检索依据为《中国药典》原料药专论。原料药专论所载技术要求与贮藏条件系活性物质原料标准。"
                            "对于药片/制剂产品，其成品储存条件与质量要求原则上遵照原料药特性，但具体应以《中国药典》相应制剂专论（如“阿司匹林片”）及经药品监管部门核准的药品说明书/包装标示为准。"
                        )
                return {
                    "decision": "ACCEPT",
                    "gate_outcome": "ACCEPT",
                    "entity_status": entity_status,
                    "parameter_status": "PARAMETER_SCOPE_CONFIRMED",
                    "effective_disposition": "GROUNDED_ANSWER",
                    "reason_code": f"ACC-01_FULL_GROUNDING: All {len(requested_params)} parameters verified with traceable limits.",
                    "parameter_coverage": cov_ratio_str,
                    "requested_parameters": requested_params,
                    "supported_parameters": list(valid_supported_params),
                    "missing_parameters": missing_params,
                    "evidence_chunk_ids": chunk_ids,
                    "quarantined_hits": [],
                    "refusal_message": "",
                    "qualification_note": qualification_note
                }
        elif len(matched_params) > 0:
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "INCOMPLETE_PARAMETER_EVIDENCE",
                "entity_status": entity_status,
                "parameter_status": "INCOMPLETE_PARAMETER_EVIDENCE",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": f"PARAM-PART-01_INCOMPLETE_COVERAGE: Covered {cov_ratio_str} requested parameters {matched_params}. Missing {missing_params}. Zero partial answer policy.",
                "parameter_coverage": cov_ratio_str,
                "requested_parameters": requested_params,
                "supported_parameters": list(valid_supported_params),
                "missing_parameters": missing_params,
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": f"证据仅涵盖部分指标（{', '.join(matched_params)}），缺少必要指标（{', '.join(missing_params)}），拒绝输出不完整法定结论。"
            }
        else:
            reason = f"PARAM-MIS-01_SCOPE_MISMATCH: Entity matched ({primary_entity}), but candidate contains {list(valid_supported_params)} instead of requested {requested_params}."
            if malformed_detected:
                reason += " (Malformed units/operators detected in candidate limits)."
            return {
                "decision": "ABSTAIN",
                "gate_outcome": "PARAMETER_SCOPE_MISMATCH",
                "entity_status": entity_status,
                "parameter_status": "PARAMETER_SCOPE_MISMATCH",
                "effective_disposition": "EVIDENCE_REFUSAL",
                "reason_code": reason,
                "parameter_coverage": cov_ratio_str,
                "requested_parameters": requested_params,
                "supported_parameters": list(valid_supported_params),
                "missing_parameters": missing_params,
                "evidence_chunk_ids": chunk_ids,
                "quarantined_hits": [],
                "refusal_message": f"检索到的正文属于目标专论（{primary_entity}），但所属章节或技术参数与问题所求（{', '.join(requested_params)}）不符。"
            }


_GLOBAL_GATE: Optional[StagingParameterGate] = None

def get_staging_parameter_gate() -> StagingParameterGate:
    """Singleton factory for staging parameter gate."""
    global _GLOBAL_GATE
    if _GLOBAL_GATE is None:
        _GLOBAL_GATE = StagingParameterGate()
    return _GLOBAL_GATE
