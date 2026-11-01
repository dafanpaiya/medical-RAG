import os
import json
import datetime
from typing import Dict, Any, Optional

AUDIT_LOG_FILE = r"d:\医药RAG\data\audit_trail.jsonl"

# Process-scoped override for the audit destination. Used to isolate a diagnostic or a test
# run from the production audit trail. Deliberately an environment variable rather than a
# parameter threaded through query handling, so it can never be influenced by user input.
AUDIT_LOG_PATH_ENV = "RAG_AUDIT_LOG_PATH"


class AuditLogPathError(RuntimeError):
    """Raised when the configured audit destination is unusable."""


def resolve_audit_log_path(log_path: Optional[str] = None) -> str:
    """Resolve the audit destination deterministically.

    Order: explicit argument > RAG_AUDIT_LOG_PATH > AUDIT_LOG_FILE.
    An unusable override raises: it must never silently fall back to the production trail.
    """
    if log_path:
        return log_path
    override = os.environ.get(AUDIT_LOG_PATH_ENV)
    if override is None or override == "":
        return AUDIT_LOG_FILE
    if not override.strip():
        raise AuditLogPathError(
            f"{AUDIT_LOG_PATH_ENV} is set but contains only whitespace")
    return override


class AuditLogger:
    """
    GxP / 21 CFR Part 11 compliant audit logging utility.
    Guarantees immutable, timestamped records of:
    - Document ingestion & version changes.
    - User content modifications / enrichments.
    - Query audit trails and human escalation triggers.
    """

    def __init__(self, log_path: Optional[str] = None):
        resolved = resolve_audit_log_path(log_path)
        parent = os.path.dirname(os.path.abspath(resolved))
        if not parent:
            raise AuditLogPathError(f"audit log path has no parent directory: {resolved!r}")
        try:
            os.makedirs(parent, exist_ok=True)
        except OSError as exc:
            raise AuditLogPathError(
                f"cannot create audit log directory {parent!r}: {exc}") from exc
        if not os.path.isdir(parent):
            raise AuditLogPathError(f"audit log directory is not a directory: {parent!r}")
        self.log_path = resolved

    def log_event(
        self,
        event_type: str,
        user_id: str,
        details: Dict[str, Any],
        doc_id: Optional[str] = None
    ):
        event_record = {
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "event_type": event_type,
            "user_id": user_id,
            "doc_id": doc_id,
            "details": details
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(event_record, ensure_ascii=False) + "\n")
        return event_record

    def get_recent_logs(self, limit: int = 50):
        if not os.path.exists(self.log_path):
            return []
        logs = []
        with open(self.log_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    logs.append(json.loads(line))
        return logs[-limit:]
