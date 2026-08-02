# -*- coding: utf-8 -*-
"""The ONE controlled artifact-identity source for the B02 storyboard package.

Stage 4.2E-C, defect B02-META-REG-001 (ARTIFACT_VERSION_AND_STATUS_DRIFT).

Before this module the production panel carried a hand-written version line and a
hand-written token list inside the generator. Both drifted: v0.4.1, v0.4.2, v0.4.3 and
v0.4.4 were all stamped "PAPAN CERITA v0.4" with the Stage 4 release tokens, on all 100
pages, while the filename, the run manifest, the decision register and the accepted verdict
had moved on four times. Two gates actively protected the drift — one forbade only the
literal "v0.3", the other REQUIRED the stale tokens to be present on every page.

Everything that states the package's identity or release standing now reads from here:

    production-panel identity   b02_generator_v0_4.prodpanel_v4
    run manifest version        RUN_MANIFEST_<version>.json
    QA expected values          b02_full_qa_v0_4, b02_governance_qa_v0_4_4_1
    checklist identity          BARIAH_REVIEW_CHECKLIST_<version>.md
    release report              STORYBOARD_QA_REPORT_<version>.md

A token is a token, never a substring. NOT_CANONICALLY_FROZEN contains CANONICALLY_FROZEN,
so every comparison in this module and in the gates that use it splits the panel line on the
separator and compares exact sets.
"""

VERSION = "v0.4.4.1"
VERSION_LINE = f"K5 PL06 T03 B02 — PAPAN CERITA {VERSION}"
DECK_FILENAME = f"K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_{VERSION.replace('.', '_')}.pptx"

# The active package-status contract. Order is significant: it is the order the panel,
# the manifest, the checklist and the release report all print.
STATUS_TOKENS = [
    "REVIEW_CANDIDATE",
    "FINAL_BARIAH_DECISIONS_IMPLEMENTED",
    "INSTANCE_MAPPING_COMPLETE",
    "READY_FOR_MICROSOFT_POWERPOINT_SMOKE",
    "NOT_FOR_MMD_BUILD",
    "NOT_CANONICALLY_FROZEN",
    "MULTIMEDIA_NOT_PRODUCED",
]

# Retired release-status claims. Present in v0.4 – v0.4.4 panels; prohibited from v0.4.4.1.
# BARIAH_FEEDBACK_IMPLEMENTED is prohibited as a CURRENT release-status claim: it was true of
# the Stage 4.1 feedback round and says nothing about the final 2 August decisions, which
# FINAL_BARIAH_DECISIONS_IMPLEMENTED states precisely.
STALE_STATUS_TOKENS = [
    "REVIEW_READY",
    "PENDING_TARGETED_CONFIRMATION",
    "BARIAH_FEEDBACK_IMPLEMENTED",
]

# Never assertable as a status token. Checked against the panel's recovered TOKEN SET, not
# by substring: CANONICALLY_FROZEN is a substring of the active NOT_CANONICALLY_FROZEN, and a
# substring test would either fire on every page or have to be weakened to let it through.
FORBIDDEN_STATUS_TOKENS = [
    "PRODUCTION_READY",
    "MMD_READY",
    "CANONICALLY_FROZEN",
]

# Never assertable anywhere in the panel. No collision with any active token, so these are
# checked as substrings across the whole panel text.
FORBIDDEN_CLAIM_STRINGS = [
    "PRODUCTION_APPROVED",
    "CANONICAL_FREEZE",
    "MMD_BUILD_READY",
    "SOURCE_INTEGRITY_FULLY_VERIFIED",
    "MICROSOFT_POWERPOINT_EQUIVALENCE",
    "SOURCE_GOVERNANCE_COMPLETE",
]

# Every version line this package has ever stamped, other than the active one. A panel that
# still carries one of these is stale by definition.
SUPERSEDED_VERSION_LINES = [
    "K5 PL06 T03 B02 — PAPAN CERITA v0.3",
    "K5 PL06 T03 B02 — PAPAN CERITA v0.4",
]

SEP = " · "
# Four lines so no single panel line exceeds the width the 9 pt panel renders cleanly, and
# so no token is ever split across lines. Grouping is presentational only — the contract is
# STATUS_TOKENS, and status_tokens_from_lines() is the inverse of this function.
STATUS_LINE_GROUPS = [(0, 2), (2, 4), (4, 5), (5, 7)]


def status_lines():
    return [SEP.join(STATUS_TOKENS[a:b]) for a, b in STATUS_LINE_GROUPS]


def panel_head_lines():
    """The identity block every production panel opens with."""
    return [VERSION_LINE] + status_lines()


def status_tokens_from_lines(lines):
    """Recover the token set a panel actually carries. Splits on the separator, so a
    prohibited token can never be matched by accident inside a longer token."""
    out = []
    for ln in lines:
        for tok in ln.split(SEP):
            tok = tok.strip()
            if tok:
                out.append(tok)
    return out


def panel_identity_from_text(lines):
    """(version_line, [tokens]) read back out of a package's panel paragraphs.

    Returns (None, []) when the panel carries no recognised version line — which is itself
    a failure for the gates, never a pass.
    """
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("K5 PL06 T03 B02 — PAPAN CERITA"):
            n = len(STATUS_LINE_GROUPS)
            return s, status_tokens_from_lines(lines[i + 1:i + 1 + n])
    return None, []


def manifest_identity():
    """The identity fields the run manifest must carry, generated here, not restated."""
    return dict(artifact_version=VERSION,
                artifact_version_line=VERSION_LINE,
                deck_filename=DECK_FILENAME,
                status_tokens=list(STATUS_TOKENS),
                stale_status_tokens_prohibited=list(STALE_STATUS_TOKENS),
                forbidden_status_tokens=list(FORBIDDEN_STATUS_TOKENS),
                forbidden_claim_strings=list(FORBIDDEN_CLAIM_STRINGS),
                superseded_version_lines=list(SUPERSEDED_VERSION_LINES))
