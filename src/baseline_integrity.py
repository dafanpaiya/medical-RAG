# -*- coding: utf-8 -*-
"""Approved-baseline and supersession-ledger validation.

Fail-closed by design: every anomaly raises. This module contains no writer functions.
The baseline and the ledger are authored by hand under an explicit authorization and are
never regenerated from the working tree.
"""

import hashlib
import json
import os
import re

_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BASELINE_PATH = os.path.join(_BASE_DIR, "data", "staging", "baseline", "approved_source_baseline.json")
LEDGER_PATH = os.path.join(_BASE_DIR, "data", "staging", "baseline", "supersession_ledger.json")
ANCHORS_PATH = os.path.join(_BASE_DIR, "data", "staging", "baseline", "anchor_records.json")

_HEX64 = re.compile(r"^[0-9a-f]{64}$")

# Absolute paths opened through this module, in order. A historical sentinel asserts that
# the current baseline never appears here, which makes the historical/current separation
# testable rather than merely intended.
OPENED = []


class BaselineIntegrityError(RuntimeError):
    pass


def _fail(msg):
    raise BaselineIntegrityError(msg)


def _read_json(path):
    if not os.path.exists(path):
        _fail("required file missing: %s" % path)
    OPENED.append(os.path.abspath(path))
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError) as exc:
        _fail("unreadable or malformed JSON: %s: %s" % (path, exc))


def canonical_path(raw):
    """Repository-relative POSIX path; the only permitted normalisation is backslash -> slash."""
    if not isinstance(raw, str) or not raw:
        _fail("path must be a non-empty string: %r" % (raw,))
    p = raw.replace("\\", "/")
    if p.startswith("/"):
        _fail("absolute or UNC path rejected: %r" % (raw,))
    if re.match(r"^[A-Za-z]:", p):
        _fail("drive-letter path rejected: %r" % (raw,))
    if p.startswith("./"):
        _fail("leading './' rejected: %r" % (raw,))
    if p.endswith("/"):
        _fail("trailing separator rejected: %r" % (raw,))
    if "//" in p:
        _fail("duplicate separator rejected: %r" % (raw,))
    if p != p.strip():
        _fail("surrounding whitespace rejected: %r" % (raw,))
    if any(seg in ("", ".", "..") for seg in p.split("/")):
        _fail("'.' or '..' segment rejected: %r" % (raw,))
    return p


def _require_hex64(value, field):
    if not isinstance(value, str) or not _HEX64.match(value):
        _fail("%s must be exactly 64 lowercase hex characters, got %r" % (field, value))
    return value


_ANCHOR_FIELDS = {"anchor_id", "object_path", "sha256", "observed_at",
                  "evidence_source", "trust_basis", "limitation"}


def load_anchors(path=ANCHORS_PATH):
    doc = _read_json(path)
    extra = set(doc) - {"schema_version", "anchors"}
    if extra:
        _fail("unknown keys in anchors file: %s" % sorted(extra))
    anchors = {}
    for i, a in enumerate(doc.get("anchors", [])):
        missing = _ANCHOR_FIELDS - set(a)
        if missing:
            _fail("anchor[%d] missing %s" % (i, sorted(missing)))
        unknown = set(a) - _ANCHOR_FIELDS
        if unknown:
            _fail("anchor[%d] has unknown keys %s" % (i, sorted(unknown)))
        p = canonical_path(a["object_path"])
        if p in anchors:
            _fail("duplicate anchor for %s" % p)
        anchors[p] = _require_hex64(a["sha256"], "anchor[%d].sha256" % i)
    return anchors


def verify_anchor(object_path, anchors):
    p = canonical_path(object_path)
    expected = anchors.get(p)
    if expected is None:
        _fail("no anchor recorded for %s" % p)
    full = os.path.join(_BASE_DIR, p)
    if not os.path.exists(full):
        _fail("anchored object missing: %s" % p)
    with open(full, "rb") as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    return actual == expected


_LEDGER_FIELDS = {"asset_path", "historical_hash", "current_hash", "approval_id",
                  "approval_evidence", "approved_at", "authorized_scope", "diff_path",
                  "recorded_by_phase"}


def load_ledger(path=LEDGER_PATH):
    doc = _read_json(path)
    extra = set(doc) - {"schema_version", "entries"}
    if extra:
        _fail("unknown keys in ledger: %s" % sorted(extra))
    entries = doc.get("entries")
    if not isinstance(entries, list):
        _fail("ledger 'entries' must be a list")
    seen = set()
    for i, e in enumerate(entries):
        missing = _LEDGER_FIELDS - set(e)
        if missing:
            _fail("ledger[%d] missing %s" % (i, sorted(missing)))
        unknown = set(e) - _LEDGER_FIELDS
        if unknown:
            _fail("ledger[%d] has unknown keys %s" % (i, sorted(unknown)))
        triple = (canonical_path(e["asset_path"]),
                  _require_hex64(e["historical_hash"], "ledger[%d].historical_hash" % i),
                  _require_hex64(e["current_hash"], "ledger[%d].current_hash" % i))
        if triple in seen:
            _fail("duplicate ledger triple at index %d: %r" % (i, triple))
        seen.add(triple)
        for fld in ("approval_id", "authorized_scope", "recorded_by_phase", "approved_at"):
            if not isinstance(e[fld], str) or not e[fld].strip():
                _fail("ledger[%d].%s must be a non-empty string" % (i, fld))
        canonical_path(e["approval_evidence"])
        canonical_path(e["diff_path"])
    return entries


def lookup_supersession(entries, asset_path, historical_hash, current_hash):
    """Exact triple lookup. Returns None on no match; raises on ambiguity."""
    p = canonical_path(asset_path)
    h = _require_hex64(historical_hash, "historical_hash")
    c = _require_hex64(current_hash, "current_hash")
    matches = []
    for e in entries:
        if (canonical_path(e["asset_path"]) == p
                and e["historical_hash"] == h
                and e["current_hash"] == c):
            matches.append(e)
    if not matches:
        return None
    if len(matches) > 1:
        _fail("ambiguous supersession: %d records match %s" % (len(matches), p))
    return matches[0]


def verify_approval_evidence(record):
    ev = canonical_path(record["approval_evidence"])
    diff = canonical_path(record["diff_path"])
    ev_full = os.path.join(_BASE_DIR, ev)
    diff_full = os.path.join(_BASE_DIR, diff)
    if not os.path.exists(ev_full):
        _fail("approval_evidence missing: %s" % ev)
    if not os.path.exists(diff_full):
        _fail("diff_path missing: %s" % diff)
    with open(ev_full, "r", encoding="utf-8", errors="replace") as f:
        body = f.read()
    if record["current_hash"] not in body:
        _fail("approval_evidence %s does not contain current_hash" % ev)
    return True


_BASELINE_FIELDS = {"schema_version", "generated_by", "generated_at", "current", "manifest_anchors"}


def load_baseline(path=BASELINE_PATH):
    """The CURRENT approved source baseline. Historical sentinels must never call this."""
    doc = _read_json(path)
    extra = set(doc) - _BASELINE_FIELDS
    if extra:
        _fail("unknown keys in baseline file: %s" % sorted(extra))
    cur = doc.get("current")
    if not isinstance(cur, dict):
        _fail("baseline 'current' must be an object")
    out = {}
    for raw, rec in cur.items():
        p = canonical_path(raw)
        out[p] = _require_hex64(rec.get("sha256"), "current[%s].sha256" % p)
    return out
