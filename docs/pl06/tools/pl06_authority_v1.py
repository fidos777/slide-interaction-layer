# -*- coding: utf-8 -*-
"""Stage 4.2F-I — the single reader for the K5 instructional authority declaration.

Every instructional value used by packet generation comes through here. Nothing downstream
may re-declare a rule as a literal: if a value is worth gating, it is worth having one
authority, and a second copy is a second place for the two to disagree.

Status vocabulary is an ENUM compared by equality, never by substring. `DRAFTED_NOT_APPROVED`
contains the characters of `APPROVED`, and this project has already been bitten twice by a
membership test that could not tell a negation from an assertion.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
CONTRACT_PATH = os.path.join(os.path.dirname(HERE), "contracts",
                             "k5_instructional_authority_v1.json")

# ---------------------------------------------------------------------------- status enum
WRITTEN_CONFIRMED = "WRITTEN_CONFIRMED"
PROPOSED_NOT_APPROVED = "PROPOSED_NOT_APPROVED"
DRAFTED_NOT_APPROVED = "DRAFTED_NOT_APPROVED"
NOT_INSTRUCTIONALLY_APPROVED = "NOT_INSTRUCTIONALLY_APPROVED"
NO_KEY_PENDING_AUTHORING = "NO_KEY_PENDING_AUTHORING"
APPROVED = "APPROVED"

STATUS_ENUM = [WRITTEN_CONFIRMED, PROPOSED_NOT_APPROVED, DRAFTED_NOT_APPROVED,
               NOT_INSTRUCTIONALLY_APPROVED, NO_KEY_PENDING_AUTHORING, APPROVED]

# The only statuses that mean "an authority has said yes".
POSITIVE_STATUSES = frozenset({WRITTEN_CONFIRMED, APPROVED})
NEGATIVE_STATUSES = frozenset({PROPOSED_NOT_APPROVED, DRAFTED_NOT_APPROVED,
                               NOT_INSTRUCTIONALLY_APPROVED, NO_KEY_PENDING_AUTHORING})


def is_approved(status):
    """Enum equality. NEVER `"APPROVED" in status` — that is true of every negation."""
    return status in POSITIVE_STATUSES


def is_not_approved(status):
    return status in NEGATIVE_STATUSES


def known_status(status):
    return status in STATUS_ENUM


_C = None


def contract():
    global _C
    if _C is None:
        with open(CONTRACT_PATH, encoding="utf-8") as f:
            _C = json.load(f)
    return _C


def rule(*path):
    """A rule record: {'value': ..., 'authority_status': ..., ...}."""
    node = contract()
    for k in path:
        node = node[k]
    return node


def value(*path):
    return rule(*path)["value"]


def status(*path):
    return rule(*path)["authority_status"]


# ------------------------------------------------------------------------ convenience reads
def quiz_shape():
    return dict(mcq=value("quiz", "mcq_count"),
                mr=value("quiz", "multiple_response_count"),
                pass_percent=value("quiz", "pass_percent"),
                key_status=value("quiz", "answer_key_approval"))


def rumusan_beats():
    return list(value("rumusan", "internal_beats"))


def forbidden_phrase():
    return value("rumusan", "forbidden_phrase")


def approved_characters():
    return list(contract()["characters"]["approved"])


def character_by_family(family):
    return next((c for c in approved_characters() if c["role_family"] == family), None)


def legacy_units():
    return {e["unit_id"]: e for e in rule("effective_scope")["exceptions"]}


def legacy_artifacts():
    return list(contract()["legacy_artifacts"])


def package_shape():
    return {k: v["value"] for k, v in contract()["package_shape"].items()}


def all_rules():
    """(path, record) for every rule carrying an authority status."""
    out = []
    for sec, body in contract().items():
        if not isinstance(body, dict):
            continue
        if body.get("authority_status"):
            out.append(((sec,), body))
            continue
        for k, v in body.items():
            if isinstance(v, dict) and v.get("authority_status"):
                out.append(((sec, k), v))
    return out
