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
COMPONENT_MAIN_PATTERN = "[Visual: Pelbagai {name}. Tidak dibenamkan.]"
BARIAH_MAIN = "BARIAH_APPROVED_COMPONENT_MAIN"

# S01 opening visual, verbatim from Bariah's reviewed example.
S01_VISUAL = ("[Visual: Imej pembuka bahagian — foto tapak landskap siap yang memaparkan "
              "struktur taman dan perabot taman dalam satu bingkai. Tidak dibenamkan.]")
BARIAH_EXEMPLAR = "BARIAH_REVIEWED_EXEMPLAR"


def classify(M, rec, st):
    """Semantic subtype + visual requirement + resolved direction for one review page."""
    sid = rec["learner_screen_id"]
    srole, strole = rec["screen_role"], st["screen_role"]
    out = dict(semantic_screen_subtype=None, popup_subtype=None,
               visual_requirement=NOT_REQUIRED, visual_direction=None,
               visual_authority=None, visual_status="NOT_REQUIRED")

    def resolved(text, authority):
        out.update(visual_direction=text, visual_authority=authority, visual_status="RESOLVED")

    # ---- popups: the subtype decides, never the family ----
    if strole == "STATE_POPUP":
        rpr = st["review_page_role"]
        if rpr == "COMPONENT_EXAMPLE_POPUP":
            out.update(semantic_screen_subtype="EXAMPLE_POPUP", popup_subtype=EXAMPLE_POPUP,
                       visual_requirement=REQUIRED)
            row = M.rows[st["source_row_uids"][0]]
            d = VD.for_row(row)
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
        out["semantic_screen_subtype"] = "COMPLETION_STATE"
        return out
    if sid == "SCR_KUIZ":
        out["semantic_screen_subtype"] = "QUIZ_" + strole.replace("STATE_QUIZ_", "")
        return out

    if sid == "SCR_S01":
        out.update(semantic_screen_subtype="TOPIC_ENTRY_SCREEN", visual_requirement=REQUIRED)
        resolved(S01_VISUAL, BARIAH_EXEMPLAR)
        return out
    if sid in ("SCR_S02", "SCR_S03", "SCR_RUMUSAN", "SCR_TAMAT"):
        out["semantic_screen_subtype"] = "FRAME_SCREEN"
        return out
    if srole == "GROUP_MASTER":
        out["semantic_screen_subtype"] = "GROUP_MASTER"
        return out
    if srole == "GROUP_OVERVIEW_NON_INTERACTIVE":
        out.update(semantic_screen_subtype="GROUP_VISUAL_GATEWAY", visual_requirement=CONDITIONAL,
                   visual_status="RESOLVED_PER_COMPONENT_CARD", visual_authority=VD.ASSET)
        return out

    # ---- example screens: always required ----
    if srole in ("COMPONENT_EXAMPLE_SELECTION", "EXAMPLE_DETAIL_FULL_SLIDE"):
        out.update(semantic_screen_subtype="EXAMPLE_SCREEN", visual_requirement=REQUIRED)
        if srole == "EXAMPLE_DETAIL_FULL_SLIDE":
            row = M.rows[rec["source_row_uids"][0]]
            d = VD.for_row(row)
            resolved(d["text"], d["authority"]) if d["status"] == "RESOLVED" else None
        else:
            c = M.comps[rec["component_id"]]
            resolved(COMPONENT_MAIN_PATTERN.format(name=c["name"]), BARIAH_MAIN)
        return out

    # ---- component main / explanation screens: conditional, resolved for every one ----
    if srole in ("COMPONENT_MAIN_EXPLANATION", "COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST",
                 "COMPONENT_EXPLANATION_WITH_SPEC_LIST"):
        c = M.comps[rec["component_id"]]
        out.update(semantic_screen_subtype="COMPONENT_MAIN_SCREEN", visual_requirement=CONDITIONAL)
        resolved(COMPONENT_MAIN_PATTERN.format(name=c["name"]), BARIAH_MAIN)
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
