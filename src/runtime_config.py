# -*- coding: utf-8 -*-
"""Runtime configuration helpers and startup diagnostics for the RAG application.

The approved unified enterprise + ChP 2025 knowledge base is the only startup path
(`src/app.py::_build_engine`); `RAG_UNIFIED_KB_ENABLED` is no longer consulted at startup
and no corpus switch exists.

`parse_unified_kb_enabled` is retained as a documented utility with its own contract
(only the documented boolean spellings are accepted; anything else raises
ConfigurationError). It is not read during application startup.
"""

import logging
from typing import Optional

_TRUE_VALUES = frozenset({"1", "true", "yes"})
_FALSE_VALUES = frozenset({"0", "false"})
ENGINE_LOGGER_NAME = "uvicorn.error"


class ConfigurationError(RuntimeError):
    """Explicit invalid runtime configuration; startup must abort."""


def parse_unified_kb_enabled(raw: Optional[str]) -> bool:
    if raw is None:
        return False
    normalized = raw.strip().lower()
    if normalized in _TRUE_VALUES:
        return True
    if normalized in _FALSE_VALUES:
        return False
    raise ConfigurationError(
        "Invalid RAG_UNIFIED_KB_ENABLED value %r. Unset means disabled. "
        "Accepted values: 1, true, yes (enable) and 0, false (disable), "
        "case-insensitive with surrounding whitespace ignored. Explicit empty or "
        "whitespace-only values are rejected; refusing to start with an ambiguous "
        "activation configuration." % (raw,)
    )


def log_engine_selection(engine, kb_mode: str,
                         logger_name: str = ENGINE_LOGGER_NAME) -> None:
    verification = getattr(engine, "candidate_verification", None)
    logger = logging.getLogger(logger_name)
    if isinstance(verification, dict) and verification:
        logger.info(
            "RAG engine initialized: engine_class=%s kb_mode=%s candidate_sha256=%s "
            "documents=%s enterprise=%s chp=%s",
            type(engine).__name__, kb_mode, verification.get("candidate_sha256"),
            verification.get("total"), verification.get("enterprise"),
            verification.get("chp"))
        return
    logger.info(
        "RAG engine initialized: engine_class=%s kb_mode=%s",
        type(engine).__name__, kb_mode)