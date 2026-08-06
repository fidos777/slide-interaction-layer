# -*- coding: utf-8 -*-
"""Stage 4.2F-J — the single reader for the K5 instructional authority declaration.

Every instructional value used by packet generation comes through here. Nothing downstream
may re-declare a rule as a literal: if a value is worth gating, it is worth having one
authority, and a second copy is a second place for the two to disagree.

Status vocabulary is an ENUM compared by equality, never by substring. `DRAFTED_NOT_APPROVED`
contains the characters of `APPROVED`, and this project has already been bitten twice by a
membership test that could not tell a negation from an assertion.

CITATION
--------
A status is a claim about who said something and where. Since Stage 4.2F-J every record that
asserts an authority said something must name three things: an artifact in the registry, a
locus inside it, and a human. A citation that resolves to nothing is not a weak warrant; it
is no warrant, and `warrant_audit` in the declaration records five places where this repo had
exactly that.
"""
import hashlib
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
ASSERTED_PRIOR = "ASSERTED_PRIOR_BARIAH_DECISION_REPEATED_IN_RETURNED_DOCUMENT"
PROPOSED_NOT_APPROVED = "PROPOSED_NOT_APPROVED"
DRAFTED_NOT_APPROVED = "DRAFTED_NOT_APPROVED"
NOT_INSTRUCTIONALLY_APPROVED = "NOT_INSTRUCTIONALLY_APPROVED"
NO_KEY_PENDING_AUTHORING = "NO_KEY_PENDING_AUTHORING"
APPROVED = "APPROVED"

# The only statuses that mean "an authority has said yes, plainly, to this".
POSITIVE_STATUSES = frozenset({WRITTEN_CONFIRMED, APPROVED})

# An authority said something, but not in the plain form a positive status claims. An
# assertion of a prior decision repeated in a returned document belongs here; it does not
# satisfy `is_approved`.
QUALIFIED_STATUSES = frozenset({ASSERTED_PRIOR})

# HOW a record was confirmed is a separate axis from WHAT status it carries. Inventing a
# status per confirmation route grows the enum without bound and makes every membership test
# a place to get it wrong; C5 was briefly recorded that way and is not any more.
PATH_A_TO_F = "A_TO_F_OPTION_MARK"
PATH_SECTION_G_ONLY = "SECTION_G_ONLY"
PATH_ASSERTED_PRIOR = "ASSERTED_PRIOR_DECISION"
PATH_OWNER_ARTIFACT = "OWNER_ENGINEERING_ARTIFACT"
CONFIRMATION_PATHS = [PATH_A_TO_F, PATH_SECTION_G_ONLY, PATH_ASSERTED_PRIOR,
                      PATH_OWNER_ARTIFACT]

NEGATIVE_STATUSES = frozenset({PROPOSED_NOT_APPROVED, DRAFTED_NOT_APPROVED,
                               NOT_INSTRUCTIONALLY_APPROVED, NO_KEY_PENDING_AUTHORING})

STATUS_ENUM = sorted(POSITIVE_STATUSES | QUALIFIED_STATUSES | NEGATIVE_STATUSES)

# Any record carrying one of these claims that a named human said something, so it must cite
# an artifact, a locus and that human.
CITATION_REQUIRED = frozenset({WRITTEN_CONFIRMED, APPROVED, ASSERTED_PRIOR})

# A record carrying one of these is a drafting basis, never a claim that anybody confirmed
# anything, so it owes no citation. The suite reconciles the two sets against the total.
CITATION_EXEMPT = frozenset(NEGATIVE_STATUSES)


def is_approved(status):
    """Enum equality. NEVER `"APPROVED" in status` — that is true of every negation."""
    return status in POSITIVE_STATUSES


def is_not_approved(status):
    return status in NEGATIVE_STATUSES


def is_qualified(status):
    return status in QUALIFIED_STATUSES


def known_status(status):
    return status in STATUS_ENUM


def status_tier(status):
    if status in POSITIVE_STATUSES:
        return "POSITIVE"
    if status in QUALIFIED_STATUSES:
        return "QUALIFIED"
    if status in NEGATIVE_STATUSES:
        return "NEGATIVE"
    return "UNKNOWN"


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
        node = node[int(k)] if isinstance(node, list) else node[k]
    return node


def value(*path):
    return rule(*path)["value"]


def status(*path):
    return rule(*path)["authority_status"]


# ================================================================== artifacts and citation
# The tension dispositions, the T02-B02 source-scope verification and the ROW-058 row-use
# disposition used to sit in this declaration. They are ANALYSIS records about the work, not
# instructional decisions that govern generation, and they now live in pl06_packet_model_v1.
NON_RULE_SECTIONS = ("artifacts", "crosswalk", "warrant_audit", "supersessions",
                     "named_authorities", "ingestion")


def confirmation_path(record):
    """How this record was confirmed. Declared when it is not the artifact's default route."""
    p = record.get("confirmation_path")
    if p:
        return p
    aid = record.get("authority_artifact")
    if aid == "RETURNED_AUTHORITY_v0_2":
        return PATH_A_TO_F
    return PATH_OWNER_ARTIFACT if aid else None


def rules_by_confirmation_path():
    out = {}
    for path, rec in all_rules():
        if rec["authority_status"] in CITATION_REQUIRED:
            out.setdefault(confirmation_path(rec) or "NO_PATH", []).append(".".join(path))
    return {k: sorted(v) for k, v in sorted(out.items())}


def citation_population():
    """(required, exempt, total) — every rule must land in exactly one of the first two."""
    rs = all_rules()
    req = [".".join(p) for p, r in rs if r["authority_status"] in CITATION_REQUIRED]
    ex = [".".join(p) for p, r in rs if r["authority_status"] in CITATION_EXEMPT]
    return sorted(req), sorted(ex), len(rs)


def artifacts():
    return dict(contract()["artifacts"])


def artifact(artifact_id):
    return artifacts().get(artifact_id)


def named_authorities():
    return dict(contract()["named_authorities"])


def artifact_path(artifact_id):
    a = artifact(artifact_id)
    return os.path.join(REPO, a["path"]) if a else None


def artifact_integrity():
    """(artifact_id, problem) for every registry entry that does not resolve to real bytes.

    Hashes are re-read from disk here. Only entries that declare a `sha256` are hash-checked;
    a Markdown artifact under active generation carries a date and a path, not a frozen hash.
    """
    out = []
    for aid, a in sorted(artifacts().items()):
        fp = os.path.join(REPO, a["path"])
        if not os.path.exists(fp):
            out.append((aid, "PATH_DOES_NOT_EXIST"))
            continue
        if a.get("sha256"):
            h = hashlib.sha256(open(fp, "rb").read()).hexdigest()
            if h != a["sha256"]:
                out.append((aid, "SHA256_MISMATCH"))
        if a.get("bytes") and os.path.getsize(fp) != a["bytes"]:
            out.append((aid, "BYTE_LENGTH_MISMATCH"))
        if not a.get("date"):
            out.append((aid, "NO_DATE"))
        if a.get("named_authority") not in named_authorities():
            out.append((aid, "AUTHORITY_NOT_IN_THE_DECLARED_ROSTER"))
    return out


def citation_defects(record):
    """Why this record's citation does not resolve. Empty list means it does.

    Deliberately strict about each field separately: a record that names an artifact but no
    human, or a human but no locus, is a PARTIAL citation, and a partial citation reads as a
    warrant to anyone skimming. All four must land.
    """
    st = record.get("authority_status")
    if st not in CITATION_REQUIRED:
        return []
    bad = []
    aid = record.get("authority_artifact")
    if not aid:
        bad.append("NO_ARTIFACT")
    elif aid not in artifacts():
        bad.append("ARTIFACT_NOT_IN_REGISTRY")
    if not (record.get("authority_locus") or "").strip():
        bad.append("NO_LOCUS")
    who = (record.get("named_authority") or "").strip()
    if not who:
        bad.append("NO_NAMED_AUTHORITY")
    elif who not in named_authorities():
        # A placeholder such as "SEE_ABOVE" or a department name is not a human who can be
        # asked what they meant.
        bad.append("NAMED_AUTHORITY_NOT_IN_THE_DECLARED_ROSTER")
    d = (record.get("authority_date") or "").strip()
    if not d:
        bad.append("NO_DATE")
    elif aid in artifacts() and d != artifacts()[aid].get("date"):
        bad.append("DATE_DISAGREES_WITH_THE_ARTIFACT_REGISTRY")
    return bad


def _walk(node, path, out):
    if isinstance(node, dict):
        if node.get("authority_status"):
            out.append((tuple(path), node))
            return
        for k, v in node.items():
            _walk(v, path + [str(k)], out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _walk(v, path + [str(i)], out)


def all_rules():
    """(path, record) for every record carrying an authority status, at any depth.

    The approved-character entries live inside a list, and before Stage 4.2F-J they were
    invisible to every status gate for exactly that reason.
    """
    out = []
    for sec, body in contract().items():
        if sec in NON_RULE_SECTIONS:
            continue
        _walk(body, [sec], out)
    return out


def uncited_rules():
    """(path, status, defects) for every record whose citation does not resolve."""
    out = []
    for path, rec in all_rules():
        bad = citation_defects(rec)
        if bad:
            out.append((".".join(path), rec.get("authority_status"), bad))
    return out


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


def replaced_characters():
    return [c["name"] for c in contract()["characters"]["replaced"]]


def legacy_units():
    return {e["unit_id"]: e for e in rule("effective_scope")["exceptions"]}


def legacy_artifacts():
    return list(contract()["legacy_artifacts"])


def package_shape():
    return {k: v["value"] for k, v in contract()["package_shape"].items()}


def lampiran_production_density():
    return value("lampiran", "production_panel_density")


def lampiran_calibration_densities():
    return list(value("lampiran", "calibration_densities_retained"))


def treatment_rules():
    return list(value("interaction", "treatment_rules"))

def treatment_overrides(unit_id):
    """Return F4 treatment records explicitly named for one unit.

    Unit-specific authority routing belongs here, not in the shared resolver. An empty
    list means F4 names no screen for that unit, so the resolver must apply F3.
    """
    field_by_unit = {
        "K5-PL06-T03-B03": "b03_treatments",
    }
    field = field_by_unit.get(unit_id)
    return list(value("interaction", field)) if field else []




def c2_claims():
    return list(contract()["dialogue"]["c2_claims"])


def crosswalk():
    return list(contract()["crosswalk"]["records"])


def warrant_findings():
    return list(contract()["warrant_audit"]["findings"])


def supersessions():
    return list(contract()["supersessions"])


def paraphrase_contract():
    return rule("dialogue", "paraphrase_contract")


def escalation_markers():
    return list(paraphrase_contract()["escalation_markers"])


def line_classes():
    return list(paraphrase_contract()["line_classes"])


def tension_is_human_verified():
    """E2's own clause: no gate here may report that a dialogue satisfies the tension rule."""
    return value("dialogue", "tension_verification") == "HUMAN_REVIEW_NOT_AN_AUTOMATED_CHECKER"
