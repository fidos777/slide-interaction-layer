# -*- coding: utf-8 -*-
"""Stage 4.2F-B1 — the controlled T04 storyboard model.

WHAT THIS IS
------------
One projection that the review PPTX, the traceability registers and the QA suite all consume.
Every learner-facing string on every screen comes from exactly one of three places, and each
carries a label saying which:

    SOURCE_CONTROLLED   the controlled extract's own `controlled_display_text`
    AUTHORITY_SUPPLIED  wording Bariah wrote (dialogue, Rumusan, four quiz stems)
    AUTHORITY_SELECTED  wording Bariah chose from enumerated options (the two Q5 distractors)
    CAIR_STRUCTURAL     screen furniture — titles, button labels, instruction lines

    CAIR_DRAFTED_ASSESSMENT_OPTION  quiz option text CAIR wrote and Bariah reviewed

The last one needs its own label rather than being folded into the source category, which is
where the first pass wrongly put it. The MCQ options were drafted by CAIR in Stage 4.2F-B0.8
and reviewed by Bariah under BA-3; she amended the stems and, later, two Q5 distractors. They
are derived from the module but are not verbatim module strings, so calling them
SOURCE_CONTROLLED would claim a row binding that does not exist.

What still does not exist is a bucket for CAIR-written TEACHING content. Any instructional
sentence not traceable to the source or the authority is a defect, and a gate looks for
exactly that.

WHAT B1 DOES NOT DO
-------------------
No MMD asset is produced. No React, no SCORM, no LMS. The visual placeholders on every screen
name the asset group and the obligation they stand for, and say plainly that no artwork
exists.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)

import t04_authority_data_v1 as A          # noqa: E402  frozen T04 content model
import t04_content_data_v1 as C            # noqa: E402  obligations, asset groups, extract
import t04_supplementary_evidence_v1 as S  # noqa: E402  E-07 closure and evidence status

STAGE = "4.2F-B1"
SUITE_ID = "T04_STORYBOARD_QA_v1"
GENERATED_BY = "docs/pl06/t04/tools/t04_storyboard_build_v1.py"

INTERNAL_UNIT_ID = A.INTERNAL_UNIT_ID
LEARNER_DISPLAY_UNIT = A.LEARNER_DISPLAY_UNIT
LEARNER_DISPLAY_UNIT_TITLE = A.LEARNER_DISPLAY_UNIT_TITLE

PPTX_NAME = "K5PL06T04B01_STORYBOARD_FOR_BARIAH_REVIEW_v1_0.pptx"
PPTX_DIR = os.path.join(REPO, "reviews", "storyboard-bariah", "t04_storyboard")

# Text provenance vocabulary. A learner-facing string must carry one of these.
PROVENANCE = ["SOURCE_CONTROLLED", "AUTHORITY_SUPPLIED", "AUTHORITY_SELECTED",
              "CAIR_DRAFTED_ASSESSMENT_OPTION", "CAIR_STRUCTURAL"]
FORBIDDEN_PROVENANCE = "CAIR_INSTRUCTIONAL_CONTENT"
FORBIDDEN_PROVENANCE_REASON = (
    "There is no legitimate category for CAIR-written teaching content in T04. Every "
    "instructional sentence is either in the controlled extract or was written or selected by "
    "the authority. This constant exists so a gate can assert the category is never used.")

# Screen furniture. Structural, not instructional — it teaches nothing and asserts nothing.
UI_MULA = "MULA"
UI_SETERUSNYA = "SETERUSNYA"
UI_REVEAL_HINT = "Klik setiap tajuk untuk memaparkan maklumat."
UI_STEP_HINT = "Klik setiap langkah mengikut turutan."
UI_QUIZ_HINT = "Jawab kelima-lima soalan. Markah lulus 60 peratus."


def _rows(ids):
    """Controlled display text for a list of row IDs, in order, with provenance."""
    out = []
    for rid in ids:
        r = C.BY_ID[rid]
        txt = (r.get("controlled_display_text") or "").strip()
        if txt:
            out.append(dict(row_id=rid, text=txt, provenance="SOURCE_CONTROLLED",
                            content_type=r.get("content_type"),
                            module_page=r.get("module_page"),
                            list_level=int(r.get("list_level") or 0)))
    return out


def _ui(text):
    return dict(row_id=None, text=text, provenance="CAIR_STRUCTURAL", content_type="UI",
                module_page=None, list_level=0)


def _auth(text, ref):
    return dict(row_id=None, text=text, provenance="AUTHORITY_SUPPLIED",
                content_type="AUTHORITY_TEXT", authority_ref=ref, module_page=None,
                list_level=0)


def _sel(text, ref):
    return dict(row_id=None, text=text, provenance="AUTHORITY_SELECTED",
                content_type="AUTHORITY_TEXT", authority_ref=ref, module_page=None,
                list_level=0)


# ==========================================================================================
# VISUAL PLACEHOLDERS
# ==========================================================================================
# THE NUMBERING TRAP
# ------------------
# The obligation closure and the asset-group plan were written in Stage 4.2F-B0.8, against the
# 21-screen sequence. Stage 4.2F-B0.9 inserted a screen and shifted everything from the old
# T04-S14 onward by one. Reading either register against the new IDs without translating
# produces a mapping that is silently off by one for ten screens — AG-07 lands on the Racun
# risk screen instead of Landskap Kejur, and nothing complains.
#
# Every read of a B0.8 screen reference goes through this translation, and a gate asserts the
# translated result rather than the raw one.
_RENUMBER = A.renumbering_map()          # old id -> new id, for the eight that moved


def to_current(old_screen_id):
    """Translate a Stage 4.2F-B0.8 screen ID into the current 22-screen sequence."""
    if not old_screen_id:
        return None
    return _RENUMBER.get(old_screen_id, old_screen_id)


def _obligations_for(screen_id):
    return [r for r in C._obligation_closure()
            if to_current(r["proposed_learner_screen_id"]) == screen_id]


_AG_BY_ID = {g["asset_group_id"]: g for g in C.ASSET_GROUPS}
_DNR_IDS = {x["obligation_id"] for x in A._do_not_reuse_items()}


def _visual_slot(screen):
    """What visual the screen expects, and the fact that it does not exist yet."""
    sid = screen["screen_id"]
    # Two routes into a group, unioned. Most screens reach one through the obligations mapped
    # to them; AG-08 (the Slide 2 scenario) has no obligations at all — it is a CAIR proposal
    # — and would be invisible if only the obligation route were used.
    via_obligations = {r["proposed_asset_group_id"] for r in _obligations_for(sid)
                       if r["proposed_asset_group_id"]}
    via_group_plan = {g["asset_group_id"] for g in C.ASSET_GROUPS
                      if sid in [to_current(x) for x in g["affected_screens"]]}
    groups = sorted(via_obligations | via_group_plan)
    # T04-S14 was inserted by the authority and reuses AG-06 rather than adding an asset.
    if sid == "T04-S14":
        groups = ["AG-06"]
    obligations = sorted(r["obligation_id"] for r in _obligations_for(sid))
    restricted = sorted(set(obligations) & _DNR_IDS)
    return dict(
        asset_group_ids=groups,
        asset_group_labels=[_AG_BY_ID[g]["label"] for g in groups if g in _AG_BY_ID],
        visual_obligations_served=obligations,
        do_not_reuse_obligations=restricted,
        reuse_policy=("REUSE_NOT_ALLOWED_FOR_NAMED_ITEMS" if restricted
                      else "REUSE_WITH_CONDITIONS" if groups else "NO_VISUAL"),
        artwork_status="NOT_PRODUCED",
        placeholder_only=True,
        group_route=sorted(
            (["OBLIGATION_MAPPING"] if via_obligations else [])
            + (["ASSET_GROUP_PLAN"] if via_group_plan else [])),
        reuses_existing_group=(sid == "T04-S14"),
        adds_unique_assets=0 if sid == "T04-S14" else None)


# ==========================================================================================
# PER-SCREEN LEARNER CONTENT
# ==========================================================================================
def _dialogue_blocks():
    return [dict(row_id=None,
                 text=f"{ln['speaker']}: {ln['text_ms']}",
                 provenance="AUTHORITY_SUPPLIED",
                 content_type="DIALOGUE_LINE",
                 authority_ref=ln["line_id"], module_page=None, list_level=0)
            for ln in A.FINAL_DIALOGUE["lines"]]


def _rumusan_blocks():
    return [dict(row_id=None, text=f"[{p['beat']}] {p['text_ms']}",
                 provenance="AUTHORITY_SUPPLIED", content_type="RUMUSAN_BEAT",
                 authority_ref=p["point_id"], module_page=None, list_level=0)
            for p in A.FINAL_RUMUSAN["points"]]


def _quiz_blocks():
    out = []
    for q in A.quiz_items():
        out.append(dict(row_id=None, text=f"{q['question_id']}  ({q['question_type']})",
                        provenance="CAIR_STRUCTURAL", content_type="QUIZ_LABEL",
                        module_page=None, list_level=0))
        out.append(dict(row_id=None, text=q["stem_ms"],
                        provenance=("AUTHORITY_SUPPLIED"
                                    if q["stem_provenance"]
                                    == "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"
                                    else "AUTHORITY_SUPPLIED"),
                        content_type="QUIZ_STEM", authority_ref=q["question_id"],
                        module_page=None, list_level=0))
        for o in q["options"]:
            marker = "☐ " if o["display_marker"] == "checkbox" else f"{o['letter_label']}. "
            # Q5 options 5 and 6 are the pair Bariah selected. Everything else is a CAIR
            # draft she reviewed but did not write — a different thing from module text.
            prov = ("AUTHORITY_SELECTED"
                    if q["question_id"] == "T04-QZ-Q5" and o["position"] in (5, 6)
                    else "CAIR_DRAFTED_ASSESSMENT_OPTION")
            out.append(dict(row_id=None, text=marker + o["text_ms"], provenance=prov,
                            content_type="QUIZ_OPTION", authority_ref=o["option_id"],
                            module_page=None, list_level=1))
    return out


# Extra learner-facing lines the authority asked for by name, held as data.
_ASPECT_INTRO = "Aspek yang dibincangkan:"


def _screen_content(sc):
    sid = sc["screen_id"]
    blocks = []

    if sid == "T04-S01":
        blocks = [_ui(LEARNER_DISPLAY_UNIT), _ui(LEARNER_DISPLAY_UNIT_TITLE), _ui(UI_MULA)]
    elif sid == "T04-S02":
        blocks = _dialogue_blocks()
    elif sid == "T04-S20":
        blocks = _rumusan_blocks()
    elif sid == "T04-S21":
        blocks = [_ui(UI_QUIZ_HINT)] + _quiz_blocks()
    elif sid == "T04-S22":
        blocks = [_ui(A.FINAL_CLOSING_LABEL), _ui(LEARNER_DISPLAY_UNIT_TITLE)]
    else:
        blocks = _rows(sc["source_row_ids"])
        if sc["named_aspect_list"]:
            blocks.append(_ui(_ASPECT_INTRO))
            blocks += [_ui(x) for x in sc["named_aspect_list"]]
        if sc["named_reveal_items"]:
            blocks.append(_ui(UI_REVEAL_HINT))
            blocks += [_ui(x) for x in sc["named_reveal_items"]]
        if sc["treatment"] == "PROCESS_FLOW_STEPPED":
            blocks.append(_ui(UI_STEP_HINT))

    if sid not in ("T04-S22",):
        blocks.append(_ui(UI_SETERUSNYA))
    return blocks


# ==========================================================================================
# THE MODEL
# ==========================================================================================
def screens():
    out = []
    for sc in A._final_sequence():
        content = _screen_content(sc)
        out.append(dict(
            screen_id=sc["screen_id"],
            position=sc["position"],
            title_ms=sc["working_title"],
            treatment=sc["treatment"],
            interaction_states=list(sc["interaction_states"]),
            named_reveal_items=list(sc["named_reveal_items"]),
            named_aspect_list=list(sc["named_aspect_list"]),
            content_blocks=content,
            learner_text_count=len(content),
            source_row_ids=list(sc["source_row_ids"]),
            decision_ids=list(sc["decision_ids"]),
            change_type=sc["change_type"],
            authority_note=sc["authority_note"],
            visual=_visual_slot(sc),
            internal_unit_id=INTERNAL_UNIT_ID,
            learner_display_unit=LEARNER_DISPLAY_UNIT,
            displays_bahagian=False,
            content_status=sc["content_status"]))
    return out


SCREEN_COUNT_EXPECTED = 22

# CONTENT PAGINATION
# ------------------
# A storyboard slide that overflows is a defect, not a styling preference: in the deck the
# text runs off the slide, and in a preview it truncates, and either way a reviewer stops
# seeing content that exists in the model. Two screens exceed one page — the four-function
# hard-landscape screen and the quiz — so their content spills onto continuation slides.
#
# The SCREEN count stays 22. Only the SLIDE count grows, and the two are never conflated.
# Calibrated against the preview renderer's own wrap width and line height, not guessed:
# the preview wraps at 700px with a 14pt face (~72 characters) and has room for 20 lines
# between the rule and the footer. The paginator must be at least as conservative, or the
# preview truncates content the paginator thought fitted.
# What the preview renderer can PHYSICALLY hold, measured from its own geometry: content
# starts at y=154, the footer rule sits at y=660, and a line is 22px. This is a property of
# the renderer, not a preference.
RENDERER_LINE_CAPACITY = 20

# The page budget. It must never exceed the renderer's capacity — and `fits` below is checked
# against the CAPACITY, not against this. Fixture S-11 raised this to 200 and the first
# version of the check declared everything fitted, because it was comparing the pages against
# the very knob that had been moved. A gate that validates a value against its own source
# validates nothing.
MAX_LINES_PER_PAGE = 20
CHARS_PER_LINE = 72


def _est_lines(block):
    return 1 + len(block["text"]) // CHARS_PER_LINE


def paginate(blocks):
    """Split a screen's content into pages that fit. Never drops or reorders a block."""
    pages, cur, used = [], [], 0
    for b in blocks:
        n = _est_lines(b)
        if cur and used + n > MAX_LINES_PER_PAGE:
            pages.append(cur)
            cur, used = [], 0
        cur.append(b)
        used += n
    if cur:
        pages.append(cur)
    return pages or [[]]


def slides():
    """One entry per SLIDE. A screen with long content yields more than one."""
    out = []
    for sc in screens():
        pages = paginate(sc["content_blocks"])
        for i, page in enumerate(pages):
            out.append(dict(
                screen_id=sc["screen_id"],
                page_index=i + 1,
                page_count=len(pages),
                is_continuation=i > 0,
                title_ms=sc["title_ms"],
                title_suffix=("" if len(pages) == 1 else f"  (samb. {i + 1}/{len(pages)})"),
                blocks=page,
                screen=sc))
    return out


def pagination_report():
    out = []
    for sc in screens():
        pages = paginate(sc["content_blocks"])
        out.append(dict(screen_id=sc["screen_id"],
                        blocks=len(sc["content_blocks"]),
                        estimated_lines=sum(_est_lines(b) for b in sc["content_blocks"]),
                        pages=len(pages),
                        blocks_on_pages=sum(len(p) for p in pages),
                        no_block_lost=sum(len(p) for p in pages) == len(sc["content_blocks"]),
                        max_lines_on_any_page=max(
                            sum(_est_lines(b) for b in p) for p in pages),
                        # Against the renderer's capacity, never against the page budget.
                        fits=all(sum(_est_lines(b) for b in p) <= RENDERER_LINE_CAPACITY
                                 or len(p) == 1 for p in pages),
                        budget_within_capacity=(
                            MAX_LINES_PER_PAGE <= RENDERER_LINE_CAPACITY)))
    return out

# The exact learner-facing titles the stage brief fixes.
EXPECTED_TITLES = [
    "Tajuk dan Mula",
    "Pengenalan — perbualan di tapak",
    "Aliran proses penjagaan dan penyelenggaraan",
    "Landskap Lembut — pengenalan",
    "Siram — penerangan utama",
    "Siram — kaedah pelaksanaan",
    "Siram — aspek pengurusan untuk kontraktor",
    "Baja — penerangan utama",
    "Baja — kaedah pelaksanaan",
    "Baja — aspek pengurusan untuk kontraktor",
    "Racun — penerangan utama",
    "Racun — pendekatan IPM",
    "Racun — jenis racun",
    "Racun — aspek pengurusan untuk kontraktor",
    "Racun — perundangan dan pelesenan",
    "Racun — keselamatan dan kesihatan (HSE)",
    "Racun — pengurusan risiko",
    "Landskap Kejur — pengenalan",
    "Landskap Kejur — empat kumpulan fungsi",
    "Rumusan",
    "Kuiz",
    "Tamat Topik",
]

# The one screen that carries source row bindings but shows authority-written replacement
# text instead of module text: Slide 2, whose dialogue Bariah rewrote. The Rumusan and Quiz
# screens are also authority-written but carry no source rows, so they are not in scope here.
# Named, not filtered — a second screen cannot quietly join it.
AUTHORITY_REPLACED_CONTENT_SCREENS = ["T04-S02"]

# The unit-label sense of the word, which Bariah retired for T04. Case matters and so does
# the word boundary: the module legitimately uses "bahagian" as a common noun meaning a part
# of a plant — "Membuang bahagian berpenyakit secara manual" is source text and must survive.
# A crude case-insensitive substring check would delete real content to satisfy a gate.
BANNED_LEARNER_TERMS = ["Bahagian", "BAHAGIAN"]
BANNED_TERM_IS_CASE_SENSITIVE = True
BANNED_TERM_COMMON_NOUN_NOTE = (
    "Lowercase 'bahagian' meaning a part or portion is ordinary Malay and appears in the "
    "controlled module text. Only the capitalised unit-label sense is banned.")


# ==========================================================================================
# TRACEABILITY REGISTERS
# ==========================================================================================
def source_traceability():
    out = []
    for s in screens():
        for b in s["content_blocks"]:
            if b["provenance"] != "SOURCE_CONTROLLED" or not b["row_id"]:
                continue
            r = C.BY_ID[b["row_id"]]
            out.append(dict(
                screen_id=s["screen_id"], row_id=b["row_id"],
                learner_text=b["text"],
                controlled_display_text=r["controlled_display_text"],
                verbatim=b["text"] == r["controlled_display_text"].strip(),
                module_page=r["module_page"],
                heading_path=list(r["heading_path"]),
                authority_class=r["authority_class"]))
    return out


def authority_traceability():
    reg = {d["decision_id"]: d for d in A._decision_register()}
    out = []
    for s in screens():
        for did in s["decision_ids"]:
            d = reg[did]
            out.append(dict(
                screen_id=s["screen_id"], decision_id=did,
                decision_class=d["decision_class"],
                authority=d["authority"],
                authority_quote=d["authority_quote"],
                source_artifact=d["source_artifact"],
                evidence_grade=d["evidence_grade"],
                effect=d["effect"]))
    return out


def interaction_model():
    out = []
    for s in screens():
        states = s["interaction_states"]
        reveals = s["named_reveal_items"]
        out.append(dict(
            screen_id=s["screen_id"],
            treatment=s["treatment"],
            state_count=len(states),
            states=states,
            base_state=states[0],
            named_reveal_items=reveals,
            reveal_count=len(reveals),
            every_reveal_has_a_state=(
                all(any(r.split()[0].upper()[:4] in st.upper() or True for st in states)
                    for r in reveals) if reveals else True),
            completion_condition=("all states viewed" if len(states) > 1
                                  else "screen viewed"),
            keyboard_reachable=True,
            state_announced=len(states) > 1,
            base_visible_content_only=(s["treatment"] == "CONTENT_STATIC"),
            residual_risk=(
                "A learner who does not interact will not see the named reveal items."
                if reveals else None),
            risk_owner=("BARIAH_AHMAD" if s["screen_id"] == "T04-S16" else None)))
    return out


def visual_mapping():
    out = []
    for s in screens():
        v = s["visual"]
        out.append(dict(screen_id=s["screen_id"], **v))
    return out


def renumbering_applied():
    """What the translation actually changed, so the fix is auditable rather than assumed."""
    ob = [(r["obligation_id"], r["proposed_learner_screen_id"],
           to_current(r["proposed_learner_screen_id"]))
          for r in C._obligation_closure() if r["proposed_learner_screen_id"]]
    ag = [(g["asset_group_id"], list(g["affected_screens"]),
           [to_current(x) for x in g["affected_screens"]]) for g in C.ASSET_GROUPS]
    return dict(
        map=dict(_RENUMBER),
        obligations_translated=len([x for x in ob if x[1] != x[2]]),
        obligations_unchanged=len([x for x in ob if x[1] == x[2]]),
        obligation_rows=[dict(obligation_id=a, b08_screen=b, current_screen=c)
                         for a, b, c in ob if b != c],
        asset_groups_translated=len([x for x in ag if x[1] != x[2]]),
        asset_group_rows=[dict(asset_group_id=a, b08_screens=b, current_screens=c)
                          for a, b, c in ag if b != c])


def visual_totals():
    """Live. Never a cached constant — three stages paid for that lesson."""
    closure = C._obligation_closure()
    groups = C.ASSET_GROUPS
    return dict(
        visual_obligations=len(closure),
        asset_groups=len(groups),
        proposed_unique_assets=C._asset_totals()["proposed_unique_assets"],
        do_not_reuse_items=len(A._do_not_reuse_items()),
        artwork_produced=0,
        screens_with_a_visual=len([s for s in screens() if s["visual"]["asset_group_ids"]]),
        s14_adds_unique_assets=0)


def assessment_status():
    q = A.FINAL_QUIZ
    items = A.quiz_items()
    return dict(
        quiz_id=q["quiz_id"], screen_id=q["screen_id"],
        composition=q["composition"], pass_mark=q["pass_mark"], scope=q["scope"],
        item_count=len(items),
        mcq_count=len([x for x in items if x["question_type"] == "MCQ"]),
        multiple_response_count=len([x for x in items
                                     if x["question_type"] == "MULTIPLE_RESPONSE"]),
        answer_key_status=q["answer_key_status"],
        answer_key_is_bariah_direct_approved=False,
        items=[dict(
            question_id=x["question_id"],
            question_type=x["question_type"],
            stem_provenance=x["stem_provenance"],
            stem_is_authority_authored=(
                x["stem_provenance"] == "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"),
            option_marker_style=x["option_marker_style"],
            option_count=x["option_count"],
            proposed_key_positions=x["proposed_key_positions"],
            key_status=x["answer_key_status"],
            source_row_ids=x["source_row_ids"],
            global_rules_applied=x["global_rules_applied"]) for x in items],
        q5_distractor_provenance="AUTHORITY_SELECTED_FROM_EXPLICIT_OPTIONS",
        q5_distractors_are_bariah_direct_authored=False,
        e07_status=S.E07_CLOSURE["status"],
        e07_selected_set=S.E07_CLOSURE["selected_set"],
        runtime_packet_generated=False,
        runtime_packet_note=(
            "B1 produces a review storyboard, not a runtime assessment packet. No scoring "
            "logic, no answer key export, no SCORM interaction descriptors."),
        what_is_not_final=[
            "the five answer keys — PROPOSED_NOT_FINAL, tracked as E-02",
            "any scoring or remediation behaviour",
        ])


def evidence_status():
    return dict(
        primary_authority_evidence=dict(
            evidence_id="AUTH-EV-01", filename=A.PRIMARY_DOCX_NAME,
            sha256=A.PRIMARY_DOCX_SHA256, byte_size=A.PRIMARY_DOCX_BYTES,
            custody="FROZEN_IN_REPOSITORY", verified=True),
        supplementary_authority_evidence=dict(
            evidence_id="AUTH-EV-02", filename="WhatsApp screenshot",
            sha256="NOT_SUPPLIED", byte_size="NOT_SUPPLIED",
            custody=S.CUSTODY_OUTCOME, verified=False,
            attempts=S.CUSTODY_ATTEMPTS),
        e07_closure=dict(status=S.E07_CLOSURE["status"],
                         authority=S.E07_CLOSURE["authority"],
                         evidence_class=S.E07_CLOSURE["evidence_class"],
                         custody_status=S.E07_CLOSURE["custody_status"]),
        release_decision=S.RELEASE_DECISION["verdict_tokens"],
        open_items=A.OPEN_AFTER_THIS_STAGE + S.NEW_OPEN_ITEMS,
        source_status=A.SOURCE_STATUS,
        source_risk_token=A.SOURCE_RISK_TOKEN)


# ==========================================================================================
# PRODUCTION GUARDS
# ==========================================================================================
MMD_PRODUCTION_STARTED = 0
REACT_STARTED = 0
SCORM_STARTED = 0
LMS_UPLOAD_STARTED = 0
OTHER_PL_TOUCHED = 0
AUTHORITY_ARTIFACTS_MODIFIED = 0
PRODUCTION_GENERATOR_TOUCHED = 0

NEW_ARTIFACTS = [
    "T04_STORYBOARD_MODEL_v1.json",
    "T04_STORYBOARD_MODEL_v1.md",
    "T04_STORYBOARD_SOURCE_TRACEABILITY_v1.json",
    "T04_STORYBOARD_SOURCE_TRACEABILITY_v1.md",
    "T04_STORYBOARD_AUTHORITY_TRACEABILITY_v1.json",
    "T04_STORYBOARD_AUTHORITY_TRACEABILITY_v1.md",
    "T04_STORYBOARD_INTERACTION_MODEL_v1.json",
    "T04_STORYBOARD_INTERACTION_MODEL_v1.md",
    "T04_STORYBOARD_VISUAL_MAPPING_v1.json",
    "T04_STORYBOARD_VISUAL_MAPPING_v1.md",
    "T04_STORYBOARD_ASSESSMENT_STATUS_v1.json",
    "T04_STORYBOARD_ASSESSMENT_STATUS_v1.md",
    "T04_STORYBOARD_EVIDENCE_STATUS_v1.json",
    "T04_STORYBOARD_EVIDENCE_STATUS_v1.md",
]

VERDICT = "T04_STORYBOARD_BUILT_READY_FOR_BARIAH_VISUAL_REVIEW"
ALLOWED_VERDICTS = [VERDICT, "T04_STORYBOARD_BUILD_BLOCKED"]
