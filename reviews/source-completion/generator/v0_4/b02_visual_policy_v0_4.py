# -*- coding: utf-8 -*-
"""Visual requirement by SEMANTIC SUBTYPE, not by execution family.

Bariah, 1 August 2026:

    "Semua contoh ada visual. Semua pop up ada visual,
     KECUALI pop up Spesifikasi (bahan, dimensi etc)."

This supersedes the earlier reading that every popup needs a visual panel. A
specification popup is text-led by design and must NOT be given a panel to satisfy a
generic gate.

Every screen and state resolves to:
    semantic_screen_subtype
    popup_subtype          (popups only)
    visual_requirement     REQUIRED | NOT_REQUIRED | CONDITIONAL
    visual_direction / visual_authority / visual_status
"""
import b02_visual_directions_v0_4 as VD

REQUIRED, NOT_REQUIRED, CONDITIONAL = "REQUIRED", "NOT_REQUIRED", "CONDITIONAL"

EXAMPLE_POPUP = "EXAMPLE_POPUP"
SPECIFICATION_POPUP = "SPECIFICATION_POPUP"

# Bariah's reviewed component-main treatment, supplied for Struktur Persisir Air and
# instructed to apply "the same principle to other component-main screens".
# The Stage 4.1 "Pelbagai {name}" pattern is RETIRED as a propagated rule: Bariah supplied it
# for one screen and it was applied to nine. It survives only as the literal BARIAH_DIRECT
# value for Struktur Persisir Air below.
BARIAH_MAIN = "BARIAH_APPROVED_COMPONENT_MAIN"

# S01 opening visual, verbatim from Bariah's reviewed example.
S01_VISUAL = ("[Visual: Imej pembuka bahagian — foto tapak landskap siap yang memaparkan "
              "struktur taman dan perabot taman dalam satu bingkai. Tidak dibenamkan.]")
BARIAH_EXEMPLAR = "BARIAH_REVIEWED_EXEMPLAR"


class VisualGovernanceError(RuntimeError):
    """A CONFIRMED BARIAH_DIRECT field is missing its value. Fail closed, never fill in."""


# Screens with direct 1 Aug 2026 authority naming the exact string.
BARIAH_DIRECT = {
    "SCR_S01": S01_VISUAL,
    "SCR_STRUKTUR_PERSISIR_AIR_MAIN": "[Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]",
}
BARIAH_DIRECT_AUTH = "BARIAH_DIRECT"

# Where the frozen corrected exemplar disagrees with the later transcript instruction, both
# are recorded and Bariah is asked to choose. CC does not pick silently.
EVIDENCE_CONFLICT = {
    "SCR_STRUKTUR_PERSISIR_AIR_MAIN": dict(
        rendered="[Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]",
        rendered_authority="BARIAH_DIRECT transcript, 1 August 2026 (explicit instruction)",
        frozen_alternative="[Visual: Rajah 23 — Contoh Boardwalk dalam Taman Paya Bakau, "
                           "modul ms 239. Tidak dibenamkan.]",
        frozen_locator="annotated deck slide 10, Bariah's own corrected component-main exemplar",
        note="The transcript says 'follow the reviewed treatment' and then gives a string that the "
             "reviewed slide does not contain. Both are disclosed; the transcript instruction is "
             "rendered because it is the later explicit direction. PENDING_BARIAH_CONFIRMATION."),
}


def classify(M, rec, st):
    """Semantic subtype + visual requirement + resolved direction for one review page.

    Nothing here invents a visual subject. A CONDITIONAL screen without direct authority
    keeps its source-attested direction and stays PENDING_HUMAN; it is never promoted to
    RESOLVED to make a gate green.
    """
    sid = rec["learner_screen_id"]
    srole, strole = rec["screen_role"], st["screen_role"]
    out = dict(semantic_screen_subtype=None, popup_subtype=None,
               visual_requirement=NOT_REQUIRED, visual_direction=None,
               visual_authority=None, visual_status="NOT_REQUIRED",
               evidence_conflict=EVIDENCE_CONFLICT.get(sid))

    def resolved(text, authority, status="RESOLVED"):
        out.update(visual_direction=text, visual_authority=authority, visual_status=status)

    def bariah_direct(sid_):
        val = BARIAH_DIRECT.get(sid_)
        if val is None or not val.strip():
            raise VisualGovernanceError(
                f"{sid_}: authority=BARIAH_DIRECT status=CONFIRMED but no value is present. "
                "Refusing to generate filler.")
        return val

    # ---- popups: the subtype decides, never the family ----
    if strole == "STATE_POPUP":
        if st["review_page_role"] == "COMPONENT_EXAMPLE_POPUP":
            out.update(semantic_screen_subtype="EXAMPLE_POPUP", popup_subtype=EXAMPLE_POPUP,
                       visual_requirement=REQUIRED)
            d = VD.for_row(M.rows[st["source_row_uids"][0]])
            if d["status"] == "RESOLVED":
                resolved(d["text"], d["authority"])
            else:
                out["visual_status"] = VD.PENDING
            return out
        out.update(semantic_screen_subtype="SPECIFICATION_POPUP",
                   popup_subtype=SPECIFICATION_POPUP, visual_requirement=NOT_REQUIRED,
                   visual_status="NOT_REQUIRED_BY_BARIAH_RULING")
        return out

    if strole in ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE"):
        out["semantic_screen_subtype"] = "COMPLETION_STATE"; return out
    if sid == "SCR_KUIZ":
        out["semantic_screen_subtype"] = "QUIZ_" + strole.replace("STATE_QUIZ_", ""); return out

    if sid == "SCR_S01":
        out.update(semantic_screen_subtype="TOPIC_ENTRY_SCREEN", visual_requirement=REQUIRED)
        resolved(bariah_direct(sid), BARIAH_DIRECT_AUTH)
        return out
    if sid in ("SCR_S02", "SCR_S03", "SCR_RUMUSAN", "SCR_TAMAT"):
        out["semantic_screen_subtype"] = "FRAME_SCREEN"; return out
    if srole == "GROUP_MASTER":
        out["semantic_screen_subtype"] = "GROUP_MASTER"; return out
    if srole == "GROUP_OVERVIEW_NON_INTERACTIVE":
        out.update(semantic_screen_subtype="GROUP_VISUAL_GATEWAY", visual_requirement=CONDITIONAL,
                   visual_status="RESOLVED_PER_COMPONENT_CARD", visual_authority=VD.ASSET)
        return out

    # ---- Family P1 full-slide example detail: REQUIRED, resolved from its own source row ----
    if srole == "EXAMPLE_DETAIL_FULL_SLIDE":
        out.update(semantic_screen_subtype="EXAMPLE_SCREEN", visual_requirement=REQUIRED)
        d = VD.for_row(M.rows[rec["source_row_uids"][0]])
        if d["status"] == "RESOLVED":
            resolved(d["text"], d["authority"])
        else:
            out["visual_status"] = VD.PENDING
        return out

    # ---- Family S Contoh screen ----
    # Bariah's corrected exemplar (annotated deck slide 12) carries NO visual direction, and the
    # transcript rule is qualified: "where an example visual is presented". That qualifier is not
    # resolved for these screens, so they stay CONDITIONAL and no direction is invented.
    if srole == "COMPONENT_EXAMPLE_SELECTION":
        out.update(semantic_screen_subtype="EXAMPLE_SELECTION_SCREEN",
                   visual_requirement=CONDITIONAL, visual_status="PENDING_HUMAN",
                   visual_authority="frozen exemplar slide 12 shows none; transcript rule is "
                                    "qualified 'where an example visual is presented'")
        return out

    # ---- component main / explanation screens ----
    if srole in ("COMPONENT_MAIN_EXPLANATION", "COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST",
                 "COMPONENT_EXPLANATION_WITH_SPEC_LIST"):
        out.update(semantic_screen_subtype="COMPONENT_MAIN_SCREEN", visual_requirement=CONDITIONAL)
        if sid in BARIAH_DIRECT:
            resolved(bariah_direct(sid), BARIAH_DIRECT_AUTH, "RESOLVED_BY_DIRECT_AUTHORITY")
            return out
        # No per-screen ruling: retain the module's OWN visual direction. No generic pattern is
        # generated from the component name, and the record stays PENDING_HUMAN.
        c = M.comps[rec["component_id"]]
        vis = VD.normalise_display((c.get("visual") or "").strip())
        if vis:
            resolved(vis, "SOURCE_ATTESTED_COMPONENT_VISUAL", "PENDING_HUMAN")
        else:
            out["visual_status"] = "PENDING_SPECIFIC_VISUAL_DIRECTION"
        return out

    out["semantic_screen_subtype"] = srole
    return out


def audit(M, pages):
    rows = []
    for p in pages:
        rec, st = M.screen(p["screen_id"]), M.state(p["state_id"])
        rows.append(dict(page=p["id"], screen=p["screen_id"], state=p["state_id"],
                         family=p["execution_family"], component=p.get("component_id"),
                         **classify(M, rec, st)))
    return rows
