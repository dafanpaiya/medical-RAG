import re
from typing import Tuple, List, Dict

class ProfessionalTermMasker:
    """
    Professional Term Masker & Unspaced Query Segmenter for Medical/Regulatory NLP.
    Protects specialized pharmaceutical, medical device, and statutory acronyms
    from being distorted during word segmentation, spell-checking, or translation.

    Examples:
    'iwannaknowfdaknowledge' -> 'i wanna know fda knowledge' -> preserves 'FDA'
    'nmpasamdrules' -> 'nmpa samd rules' -> preserves 'NMPA', 'SaMD'
    """

    # High-priority domain terminology and statutory abbreviations that must NEVER be mutated
    DOMAIN_TERMS = [
        # Regulatory agencies & standards bodies
        "fda", "nmpa", "pmda", "ema", "anvisa", "who", "ich", "iso", "iec", "eumdr", "eu",
        # Medical device & software classifications
        "samd", "simd", "aiml", "ai", "qmsr", "mdr", "ivdr", "ce", "gmp", "gcp", "glp",
        # Statutory frameworks & identifiers
        "510k", "510(k)", "524b", "de novo", "pma", "pccp", "sbom", "spdx", "cyclonedx",
        "21 cfr", "21cfr", "part 820", "part820", "part 11", "part11", "rule 11", "rule11", "gspr",
        # Pharmaceutical & clinical terms
        "be", "pk", "pd", "rld", "auc", "cmax", "ind", "nda", "bla", "cqa", "cpp", "qbd", "tcm"
    ]

    # Canonical representation of domain terms
    CANONICAL_TERMS: Dict[str, str] = {
        "fda": "FDA", "nmpa": "NMPA", "pmda": "PMDA", "ema": "EMA", "anvisa": "ANVISA", "who": "WHO", "ich": "ICH",
        "iso": "ISO", "iec": "IEC", "eu": "EU", "eumdr": "EU MDR", "mdr": "MDR", "ivdr": "IVDR", "ce": "CE",
        "samd": "SaMD", "simd": "SiMD", "aiml": "AI/ML", "ai": "AI", "qmsr": "QMSR", "gmp": "GMP", "gcp": "GCP", "glp": "GLP",
        "510k": "510(k)", "510(k)": "510(k)", "524b": "524B", "de novo": "De Novo", "pma": "PMA", "pccp": "PCCP",
        "sbom": "SBOM", "spdx": "SPDX", "cyclonedx": "CycloneDX", "21 cfr": "21 CFR", "21cfr": "21 CFR",
        "part 820": "Part 820", "part820": "Part 820", "part 11": "Part 11", "part11": "Part 11",
        "rule 11": "Rule 11", "rule11": "Rule 11", "gspr": "GSPR",
        "be": "BE", "pk": "PK", "pd": "PD", "rld": "RLD", "auc": "AUC", "cmax": "Cmax",
        "ind": "IND", "nda": "NDA", "bla": "BLA", "cqa": "CQA", "cpp": "CPP", "qbd": "QbD", "tcm": "TCM"
    }

    # Common English words used to segment continuous unspaced strings
    COMMON_ENGLISH_WORDS = {
        "i", "me", "my", "a", "an", "the", "in", "on", "at", "to", "for", "of", "and", "or", "with", "by",
        "is", "are", "was", "were", "be", "do", "does", "did", "can", "could", "should", "would",
        "wanna", "want", "know", "see", "get", "find", "look", "tell", "give", "show", "help",
        "about", "what", "which", "how", "why", "when", "where", "who", "whom",
        "knowledge", "rule", "rules", "regulation", "regulations", "law", "laws",
        "guideline", "guidelines", "guidance", "standard", "standards", "requirement", "requirements",
        "submission", "submissions", "device", "devices", "drug", "drugs", "medicine", "medical",
        "software", "system", "clinical", "trial", "trials", "evaluation", "approval", "clearance",
        "review", "process", "document", "documents", "data", "safety", "risk", "security", "cyber",
        "cybersecurity", "table", "class", "content", "information", "details", "policy", "policies",
        "prepare", "prepares", "preparing"
    }

    def __init__(self):
        # Sort terms by length descending to match longest acronyms first
        self.sorted_domain_terms = sorted(self.DOMAIN_TERMS, key=len, reverse=True)

    def mask_and_segment_unspaced_query(self, query: str) -> Tuple[str, Dict[str, str]]:
        """
        Detects unspaced English strings, masks domain entities, segments common words,
        and unmasks domain entities into a clean, properly spaced string.
        """
        # If the query already has multiple spaces, or is predominantly CJK characters, skip full unspaced segmentation
        has_spaces = " " in query.strip()
        cjk_count = len(re.findall(r"[\u4e00-\u9fff]", query))
        total_len = len(query.strip())

        # If it's already spaced or mostly CJK, just ensure acronyms are spaced
        if has_spaces or (total_len > 0 and cjk_count / total_len > 0.4):
            return query, {}

        # Check if the query is a continuous alphanumeric string (e.g. 'iwannaknowfdaknowledge')
        clean_q = query.strip().lower()
        if not re.match(r"^[a-z0-9_]+$", clean_q):
            return query, {}

        # Step 1: Detect and mask domain terms
        term_map: Dict[str, str] = {}
        masked_text = clean_q
        mask_counter = 0

        for term in self.sorted_domain_terms:
            pattern = re.compile(re.escape(term))
            if pattern.search(masked_text):
                placeholder = f"__TERM_{mask_counter}__"
                term_map[placeholder] = self.CANONICAL_TERMS.get(term, term.upper())
                masked_text = pattern.sub(f" {placeholder} ", masked_text)
                mask_counter += 1

        # Step 2: Segment remaining English continuous parts
        tokens = masked_text.split()
        segmented_tokens: List[str] = []

        for token in tokens:
            if token.startswith("__TERM_") and token.endswith("__"):
                segmented_tokens.append(token)
            else:
                # Segment continuous unspaced letters using max-matching / DP segmenter
                segmented_subwords = self._segment_unspaced_english(token)
                segmented_tokens.extend(segmented_subwords)

        # Step 3: Unmask domain terms
        final_tokens = []
        for token in segmented_tokens:
            if token in term_map:
                final_tokens.append(term_map[token])
            else:
                final_tokens.append(token)

        reconstructed_query = " ".join(final_tokens)
        return reconstructed_query, term_map

    def _segment_unspaced_english(self, s: str) -> List[str]:
        """
        Segments a continuous unspaced English string (e.g. 'iwannaknow' -> ['i', 'wanna', 'know'])
        using longest-matching dynamic programming against common vocabulary.
        """
        n = len(s)
        if n <= 3:
            return [s]

        # Dynamic programming: find word boundaries that maximize matching common English words
        # dp[i] stores list of words for s[0:i]
        dp: Dict[int, List[str]] = {0: []}

        for i in range(1, n + 1):
            best_words = None
            for j in range(max(0, i - 15), i):
                sub = s[j:i]
                if j in dp and (sub in self.COMMON_ENGLISH_WORDS or len(sub) == 1):
                    candidate = dp[j] + [sub]
                    if best_words is None or len(candidate) < len(best_words):
                        best_words = candidate
            if best_words is not None:
                dp[i] = best_words
            else:
                # Fallback: append current char to previous or as new chunk
                prev = dp.get(i - 1, [s[:i-1]])
                dp[i] = prev + [s[i-1]]

        result = dp.get(n, [s])
        return result if result else [s]
