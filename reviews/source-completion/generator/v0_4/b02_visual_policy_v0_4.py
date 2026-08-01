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

# ---------------------------------------------------------------------------------------
# Stage 4.2C — latest evidence, frozen at reviews/storyboard-bariah/v0_3_bariah_review/.
#
#   B02_BARIAH_VISUAL_POLICY_EVIDENCE.png   WhatsApp 4:37 PM, verbatim:
#       "Semua contoh ada visual. Semua pop up ada visual,
#        KECUALI pop up Spesifikasi (bahan, dimensi etc)"
#
# "Semua contoh ada visual" is unqualified. The Stage 4.2B reading — that Family S Contoh
# screens are CONDITIONAL because the corrected slide 12 shows no screen-level direction —
# is SUPERSEDED: the requirement attaches to each example, and on a selection screen every
# example is a card. Each card therefore carries its own source-attested direction. No
# screen-level composite is invented.
LATEST_EVIDENCE_DATE = "2026-08-01"
PER_EXAMPLE_CARD = "RESOLVED_PER_EXAMPLE_CARD"
PROVISIONAL = "PROVISIONAL_VISUAL_PROPOSAL"

# The requirement table the 4:37 PM ruling defines. EXAMPLE_DETAIL_SCREEN is the Family P1
# full-slide example; it has carried the subtype string EXAMPLE_SCREEN since Stage 4, so the
# alias is declared rather than renamed — renaming would silently retire live gate IDs.
SUBTYPE_ALIASES = {"EXAMPLE_DETAIL_SCREEN": "EXAMPLE_SCREEN"}
SUBTYPE_REQUIREMENT = {
    "EXAMPLE_SCREEN":           REQUIRED,
    "EXAMPLE_DETAIL_SCREEN":    REQUIRED,
    "EXAMPLE_SELECTION_SCREEN": REQUIRED,
    "EXAMPLE_POPUP":            REQUIRED,
    "SPECIFICATION_POPUP":      NOT_REQUIRED,
}


def declared_requirement(subtype):
    """The ruling's requirement for a subtype, or None if the ruling does not name it."""
    return SUBTYPE_REQUIREMENT.get(SUBTYPE_ALIASES.get(subtype, subtype))

# S01 opening visual, verbatim from Bariah's reviewed example.
S01_VISUAL = ("[Visual: Imej pembuka bahagian — foto tapak landskap siap yang memaparkan "
              "struktur taman dan perabot taman dalam satu bingkai. Tidak dibenamkan.]")
BARIAH_EXEMPLAR = "BARIAH_REVIEWED_EXEMPLAR"


class VisualGovernanceError(RuntimeError):
    """A CONFIRMED BARIAH_DIRECT field is missing its value. Fail closed, never fill in."""


def example_card_visuals(M, rec):
    """One record per example card on a Family S selection screen.

    Each direction is read from that example's OWN source row, so a card can never show
    another example's visual and no direction is generated from the component name.
    """
    out = []
    for it in M.items_of(rec["learner_screen_id"]):
        uid = it["source_row_uid"]
        row = M.rows[uid]
        d = VD.for_row(row)
        out.append(dict(interaction_item_id=it["interaction_item_id"], source_row_uid=uid,
                        label=row["label"], text=d["text"], authority=d["authority"],
                        status=d["status"]))
    return out


# Screens with direct 1 Aug 2026 authority naming the exact string.
BARIAH_DIRECT = {
    "SCR_S01": S01_VISUAL,
    "SCR_STRUKTUR_PERSISIR_AIR_MAIN": "[Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]",
}
BARIAH_DIRECT_AUTH = "BARIAH_DIRECT"

# Stage 4.2B disclosed an unresolved conflict here: the annotated v0.3 deck's corrected
# component-main carried the Rajah 23 / Boardwalk direction, while the transcript gave
# "Pelbagai Struktur Persisir Air". Bariah's 4:40 PM screenshot settles it — her corrected
# component-main shows "Pelbagai Struktur Persisir Air. Tidak dibenamkan." and nothing else.
# The conflict is therefore CLOSED, not carried. The losing direction is retained here as
# superseded evidence, never as a second active instruction.
EVIDENCE_CONFLICT = {}          # ACTIVE_EVIDENCE_CONFLICTS = 0

SUPERSEDED_ID = "SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT"
SUPERSEDED_RULINGS = {
    "SCR_STRUKTUR_PERSISIR_AIR_MAIN": dict(
        superseded_direction="[Visual: Rajah 23 — Contoh Boardwalk dalam Taman Paya Bakau, "
                             "modul ms 239. Tidak dibenamkan.]",
        superseded_locator="annotated Bariah review deck, slide 10, component-main exemplar",
        active_direction="[Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]",
        superseding_evidence="B02_BARIAH_STRUKTUR_PERSISIR_EVIDENCE.jpg",
        superseding_sha256="936b78c270274874bfa4921a35205e4ca1d679959ebf6f1880e7c76e6f890ab7",
        status=SUPERSEDED_ID,
        note="Rajah 23 remains the source-attested direction of the Boardwalk EXAMPLE row. "
             "What is superseded is its use as the COMPONENT-MAIN screen direction."),
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
               evidence_conflict=EVIDENCE_CONFLICT.get(sid),
               superseded_ruling=SUPERSEDED_RULINGS.get(sid),
               example_card_visuals=None)

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
    # SUPERSEDED at Stage 4.2C. The 4:37 PM screenshot says "Semua contoh ada visual" with no
    # qualifier, so this screen is REQUIRED. Every example on it is a card, and each card takes
    # its OWN source-attested direction — the same string its example popup shows. Nothing is
    # composed at screen level, so no subject is invented for the screen as a whole.
    if srole == "COMPONENT_EXAMPLE_SELECTION":
        out.update(semantic_screen_subtype="EXAMPLE_SELECTION_SCREEN",
                   visual_requirement=REQUIRED)
        cards = example_card_visuals(M, rec)
        out["example_card_visuals"] = cards
        if cards and all(c["status"] == "RESOLVED" for c in cards):
            out.update(visual_status=PER_EXAMPLE_CARD, visual_authority=VD.ASSET)
        else:
            out["visual_status"] = VD.PENDING
        return out

    # ---- component main / explanation screens ----
    if srole in ("COMPONENT_MAIN_EXPLANATION", "COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST",
                 "COMPONENT_EXPLANATION_WITH_SPEC_LIST"):
        out.update(semantic_screen_subtype="COMPONENT_MAIN_SCREEN", visual_requirement=CONDITIONAL)
        if sid in BARIAH_DIRECT:
            resolved(bariah_direct(sid), BARIAH_DIRECT_AUTH, "RESOLVED_BY_DIRECT_AUTHORITY")
            return out
        # No per-screen ruling. Bariah's 4:40 PM caption is "Slide 5 – apply to yang lain where
        # applicable/necessary" — a qualified instruction, not a blanket mandate naming content
        # for the other eight. So each retains the module's OWN visual direction, flagged as a
        # PROVISIONAL_VISUAL_PROPOSAL awaiting her decision. CC does not decide "applicable".
        c = M.comps[rec["component_id"]]
        vis = VD.normalise_display((c.get("visual") or "").strip())
        out["proposal_class"] = PROVISIONAL
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
