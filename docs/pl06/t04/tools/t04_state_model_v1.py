# -*- coding: utf-8 -*-
"""Stage 4.2F-B1.1 Lane A — the T04 runtime-state inventory, derived from the controlled model.

WHY THIS EXISTS
---------------
The Stage 4.2F-B1 deck shows, per screen, a LIST of state names. A reviewer can read
"ST-01, ST-02, ST-03" and learn nothing about what triggers each one, what appears when it
fires, how it differs from the base state, or how the learner gets back. That is a layout
storyboard, not an interaction review.

This module derives every runtime state as a record with its trigger, its content, its
difference from the base state, its return behaviour and its bindings — so the question
"is this state review-visible?" has an answer that is checkable rather than asserted.

DERIVED, NOT COUNTED
--------------------
Nothing here is inferred from the PPTX page count. Reveal targets are declared per screen and
then VERIFIED against the screen's own controlled rows: every declared target must be a
heading or list row belonging to that screen, and the count must equal the number of ST states
the frozen sequence already carries. A gate fails if either drifts.

ONE HONEST GAP, STATED UP FRONT
-------------------------------
T04-S03's six process steps have NO per-step source rows. The six activities live inside the
SmartArt diagram T04-DGM-01, which the extract carries as a single row (T04-ROW-003) with no
text. Their labels come from the six visual obligations derived from that diagram. Those six
states are therefore bound to an obligation, not to a text row, and they say so.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)

import t04_storyboard_model_v1 as SB   # noqa: E402
import t04_authority_data_v1 as A      # noqa: E402
import t04_content_data_v1 as C        # noqa: E402

STAGE = "4.2F-B1.1"
SUITE_ID = "T04_STATE_COVERAGE_QA_v1"
GENERATED_BY = "docs/pl06/t04/tools/t04_state_emit_v1.py"

# The current B1 artifact status. Deliberately not the stronger labels.
CURRENT_STATUS = "T04_LAYOUT_STORYBOARD_BUILT"
FORBIDDEN_STATUS_CLAIMS = [
    "T04_INTERACTION_REVIEW_COMPLETE",
    "T04_STORYBOARD_FROZEN",
    "T04_CANONICAL_PRODUCTION_TEMPLATE",
]

STATE_KINDS = ["BASE", "REVEAL", "STEP", "QUIZ_ITEM", "QUIZ_RESULT", "COMPLETION"]
COVERAGE_CLASSES = ["FULL_PAGE_VISIBLE", "MULTI_PANEL_VISIBLE", "NOTES_ONLY",
                    "METADATA_ONLY", "NOT_REPRESENTED"]

# Reviewer-facing Malay. The appendix is read by Bariah, so every string on a panel is in
# Malay; the English texts below stay in the JSON register as the analytic record.
RETURN_BEHAVIOURS_MS = {
    "REVEAL": "Panel tertutup apabila ditekan sekali lagi atau apabila panel lain dibuka. "
              "Keadaan asas kembali dan sentiasa boleh dicapai. Tiada navigasi berlaku.",
    "STEP": "Langkah kekal ditandakan. Pelajar meneruskan ke langkah berikutnya atau kembali "
            "ke pandangan aliran. Tiada navigasi keluar dari skrin.",
    "BASE": "Keadaan masuk. Pelajar meneruskan dengan SETERUSNYA setelah syarat selesai "
            "dipenuhi.",
    "QUIZ_ITEM": "Menghantar jawapan membawa pelajar ke item berikutnya. Tiada navigasi "
                 "kembali antara item kuiz.",
    "QUIZ_RESULT": "Keadaan akhir bagi skrin ini. Pelajar meneruskan dengan SETERUSNYA.",
    "COMPLETION": "Bukan keadaan yang dipaparkan. Penanda yang menjadi benar setelah semua "
                  "pendedahan atau langkah dilihat, dan inilah yang membuka SETERUSNYA.",
}

RETURN_BEHAVIOURS = {
    "REVEAL": "Panel closes on a second activation or on opening another panel; the base "
              "state is restored and remains reachable throughout. No navigation occurs.",
    "STEP": "The step stays highlighted; the learner advances to the next step or returns to "
            "the flow overview. No navigation away from the screen.",
    "BASE": "Entry state. The learner continues with SETERUSNYA once the completion "
            "condition is met.",
    "QUIZ_ITEM": "Submitting the item advances to the next item. There is no back navigation "
                 "between quiz items.",
    "QUIZ_RESULT": "Terminal state for the screen. The learner continues with SETERUSNYA.",
    "COMPLETION": "Not a displayed state. A flag that becomes true once every reveal or step "
                  "has been viewed, which is what unlocks SETERUSNYA.",
}

# ==========================================================================================
# REVEAL / STEP TARGETS — declared, then verified against the controlled rows
# ==========================================================================================
# (screen_id, [(trigger_label_row_or_none, [content_row_ids])])
_REVEAL_TARGETS = {
    "T04-S06": [("T04-ROW-009", ["T04-ROW-010"]),
                ("T04-ROW-011", ["T04-ROW-012", "T04-ROW-013",
                                 "T04-ROW-014", "T04-ROW-015"])],
    "T04-S07": [("T04-ROW-017", ["T04-ROW-018", "T04-ROW-019"]),
                ("T04-ROW-020", ["T04-ROW-021"]),
                ("T04-ROW-022", ["T04-ROW-023"]),
                ("T04-ROW-024", ["T04-ROW-025"])],
    "T04-S09": [("T04-ROW-029", ["T04-ROW-030"]),
                ("T04-ROW-031", ["T04-ROW-032"]),
                ("T04-ROW-033", ["T04-ROW-034"])],
    "T04-S10": [("T04-ROW-036", ["T04-ROW-037"]),
                ("T04-ROW-038", ["T04-ROW-039"]),
                ("T04-ROW-040", ["T04-ROW-041"]),
                ("T04-ROW-042", ["T04-ROW-043"]),
                ("T04-ROW-044", ["T04-ROW-045"])],
    "T04-S16": [("T04-ROW-069", ["T04-ROW-070"]),
                ("T04-ROW-071", ["T04-ROW-072"]),
                ("T04-ROW-073", ["T04-ROW-074"])],
    "T04-S19": [("T04-ROW-081", ["T04-ROW-082", "T04-ROW-083",
                                 "T04-ROW-084", "T04-ROW-085"]),
                ("T04-ROW-086", ["T04-ROW-087", "T04-ROW-088",
                                 "T04-ROW-089", "T04-ROW-090"]),
                ("T04-ROW-091", ["T04-ROW-092", "T04-ROW-093",
                                 "T04-ROW-094", "T04-ROW-095"]),
                ("T04-ROW-096", ["T04-ROW-097", "T04-ROW-098",
                                 "T04-ROW-099", "T04-ROW-100"])],
}

# T04-S14 was inserted by the authority. Its three reveal panels are navigation hubs pointing
# at the three screens that carry the detail; the labels are Bariah's, not module rows.
_AUTHORITY_REVEAL_TARGETS = {
    "T04-S14": [("Perundangan Dan Pelesenan", "T04-S15"),
                ("Keselamatan Dan Kesihatan (HSE)", "T04-S16"),
                ("Pengurusan Risiko", "T04-S17")],
}

# T04-S03's six steps come from the diagram, which carries no per-step text row.
_DIAGRAM_STEP_OBLIGATIONS = ["T04-VO-001", "T04-VO-002", "T04-VO-003",
                             "T04-VO-004", "T04-VO-005", "T04-VO-006"]
_DIAGRAM_ROW = "T04-ROW-003"

_OB_BY_ID = {r["obligation_id"]: r for r in C._obligation_closure()}


def _row_text(rid):
    return (C.BY_ID[rid]["controlled_display_text"] or "").strip()


def _screen(sid):
    return next(s for s in SB.screens() if s["screen_id"] == sid)


def _base_blocks(sc):
    """What the base state shows: everything not behind a reveal."""
    hidden = set()
    for trig, rows in _REVEAL_TARGETS.get(sc["screen_id"], []):
        hidden.update(rows)
    return [b for b in sc["content_blocks"]
            if not (b.get("row_id") and b["row_id"] in hidden)]


# ==========================================================================================
def states():
    out = []
    for sc in SB.screens():
        sid = sc["screen_id"]
        declared = list(sc["interaction_states"])
        base_blocks = _base_blocks(sc)
        base_id = f"{sid}-ST-BASE"

        # The quiz screen has no separate entry state: it opens ON Q1. Emitting a generic
        # BASE here would invent a 66th state that the frozen sequence does not declare, and
        # would label it "Q1" twice.
        quiz_screen = sid == "T04-S21"
        if quiz_screen:
            base_id = f"{sid}-ST-01"

        if not quiz_screen:
            out.append(dict(
                state_id=base_id, screen_id=sid, position=sc["position"],
                state_kind="BASE", declared_state_label=declared[0],
                trigger_id=None, trigger_label="screen entry",
                parent_state_id=None,
                resulting_state_id=base_id,
                return_behaviour=RETURN_BEHAVIOURS["BASE"],
                return_behaviour_ms=RETURN_BEHAVIOURS_MS["BASE"],
                content_block_texts=[b["text"] for b in base_blocks],
                content_record_count=len(base_blocks),
                differs_from_base="— this is the base state —",
                differs_from_base_ms="— ini keadaan asas —",
                source_row_ids=[b["row_id"] for b in base_blocks if b.get("row_id")],
                authority_refs=[b["authority_ref"] for b in base_blocks
                                if b.get("authority_ref")],
                decision_ids=list(sc["decision_ids"]),
                visual_obligations=list(sc["visual"]["visual_obligations_served"]),
                binding_kind="SOURCE_ROWS" if sc["source_row_ids"] else "STRUCTURAL"))

        # --- reveal panels bound to module rows -------------------------------------------
        for i, (trig_row, rows) in enumerate(_REVEAL_TARGETS.get(sid, []), start=1):
            sid_st = f"{sid}-ST-{i:02d}"
            out.append(dict(
                state_id=sid_st, screen_id=sid, position=sc["position"],
                state_kind="REVEAL", declared_state_label=declared[i],
                trigger_id=f"{sid}-TRG-{i:02d}", trigger_label=_row_text(trig_row),
                parent_state_id=base_id, resulting_state_id=sid_st,
                return_behaviour=RETURN_BEHAVIOURS["REVEAL"],
                return_behaviour_ms=RETURN_BEHAVIOURS_MS["REVEAL"],
                content_block_texts=[_row_text(r) for r in rows if _row_text(r)],
                content_record_count=len([r for r in rows if _row_text(r)]),
                differs_from_base=(f"Adds the body of \"{_row_text(trig_row)}\" — "
                                   f"{len(rows)} record(s) not shown in the base state."),
                differs_from_base_ms=(f"Menambah kandungan \"{_row_text(trig_row)}\" — "
                                      f"{len(rows)} rekod yang tidak dipaparkan dalam "
                                      "keadaan asas."),
                source_row_ids=[trig_row] + list(rows),
                authority_refs=[], decision_ids=list(sc["decision_ids"]),
                visual_obligations=list(sc["visual"]["visual_obligations_served"]),
                binding_kind="SOURCE_ROWS"))

        # --- reveal panels declared by the authority (T04-S14) ----------------------------
        for i, (label, target) in enumerate(_AUTHORITY_REVEAL_TARGETS.get(sid, []), start=1):
            sid_st = f"{sid}-ST-{i:02d}"
            out.append(dict(
                state_id=sid_st, screen_id=sid, position=sc["position"],
                state_kind="REVEAL", declared_state_label=declared[i],
                trigger_id=f"{sid}-TRG-{i:02d}", trigger_label=label,
                parent_state_id=base_id, resulting_state_id=sid_st,
                return_behaviour=RETURN_BEHAVIOURS["REVEAL"],
                return_behaviour_ms=RETURN_BEHAVIOURS_MS["REVEAL"],
                content_block_texts=[
                    f"Ringkasan aspek: {label}",
                    f"Butiran penuh dibentangkan pada skrin {target}."],
                content_record_count=2,
                differs_from_base=(f"Adds a short overview panel for \"{label}\" and names "
                                   f"the screen that carries it in full ({target})."),
                differs_from_base_ms=(f"Menambah panel ringkasan bagi \"{label}\" dan "
                                      f"menyatakan skrin yang membentangkannya secara penuh "
                                      f"({target})."),
                source_row_ids=["T04-ROW-064"],
                authority_refs=["T04-DEC-A14"], decision_ids=list(sc["decision_ids"]),
                visual_obligations=list(sc["visual"]["visual_obligations_served"]),
                binding_kind="AUTHORITY_DECLARED_NAVIGATION_HUB",
                navigation_target=target))

        # --- diagram steps (T04-S03) ------------------------------------------------------
        if sid == "T04-S03":
            for i, ob in enumerate(_DIAGRAM_STEP_OBLIGATIONS, start=1):
                sid_st = f"{sid}-ST-{i:02d}"
                heading = _OB_BY_ID[ob]["source_heading"]
                out.append(dict(
                    state_id=sid_st, screen_id=sid, position=sc["position"],
                    state_kind="STEP", declared_state_label=declared[i],
                    trigger_id=f"{sid}-TRG-{i:02d}", trigger_label=heading,
                    parent_state_id=base_id, resulting_state_id=sid_st,
                    return_behaviour=RETURN_BEHAVIOURS["STEP"],
                    return_behaviour_ms=RETURN_BEHAVIOURS_MS["STEP"],
                    content_block_texts=[heading],
                    content_record_count=1,
                    differs_from_base=(f"Highlights step {i} of six, \"{heading}\". The six "
                                       "labels are already visible in the base state; the "
                                       "step state marks position, it does not disclose new "
                                       "text."),
                    differs_from_base_ms=(f"Menandakan langkah {i} daripada enam, "
                                          f"\"{heading}\". Keenam-enam label sudah kelihatan "
                                          "dalam keadaan asas; keadaan langkah menandakan "
                                          "kedudukan, ia tidak mendedahkan teks baharu."),
                    source_row_ids=[_DIAGRAM_ROW],
                    authority_refs=[], decision_ids=list(sc["decision_ids"]),
                    visual_obligations=[ob],
                    binding_kind="DIAGRAM_OBLIGATION_NOT_A_TEXT_ROW",
                    binding_limitation_ms=(
                        "Enam aktiviti berada di dalam rajah SmartArt T04-DGM-01. Ekstrak "
                        "terkawal membawa rajah itu sebagai satu baris tanpa teks, jadi "
                        "keadaan ini terikat kepada keperluan visual dan bukan kepada baris "
                        "teks."),
                    binding_limitation=(
                        "The six activities live inside the SmartArt diagram T04-DGM-01. The "
                        "controlled extract carries that diagram as one row with no text, so "
                        "this state is bound to a visual obligation rather than to a text "
                        "row. The label is the obligation's source heading.")))

        # --- quiz items -------------------------------------------------------------------
        if sid == "T04-S21":
            for i, q in enumerate(A.quiz_items(), start=1):
                sid_st = f"{sid}-ST-{i:02d}"
                opts = [("☐ " if o["display_marker"] == "checkbox"
                         else f"{o['letter_label']}. ") + o["text_ms"]
                        for o in q["options"]]
                out.append(dict(
                    state_id=sid_st, screen_id=sid, position=sc["position"],
                    state_kind=("BASE" if i == 1 else "QUIZ_ITEM"),
                    declared_state_label=declared[i - 1],
                    trigger_id=(None if i == 1 else f"{sid}-TRG-{i:02d}"),
                    trigger_label=("screen entry" if i == 1
                                   else f"submitting {A.quiz_items()[i - 2]['question_id']}"),
                    parent_state_id=(None if i == 1 else f"{sid}-ST-{i - 1:02d}"),
                    resulting_state_id=sid_st,
                    return_behaviour=(RETURN_BEHAVIOURS["BASE"] if i == 1
                                      else RETURN_BEHAVIOURS["QUIZ_ITEM"]),
                    return_behaviour_ms=(RETURN_BEHAVIOURS_MS["BASE"] if i == 1
                                         else RETURN_BEHAVIOURS_MS["QUIZ_ITEM"]),
                    content_block_texts=[q["stem_ms"]] + opts,
                    content_record_count=1 + len(opts),
                    differs_from_base=("— this is the base state; the screen opens on Q1 —"
                                       if i == 1 else
                                       f"Presents {q['question_id']} and replaces the "
                                       "previous item. Only one item is on screen at a "
                                       "time."),
                    differs_from_base_ms=("— ini keadaan asas; skrin bermula pada Q1 —"
                                          if i == 1 else
                                          f"Memaparkan {q['question_id']} dan menggantikan "
                                          "item sebelumnya. Hanya satu item dipaparkan pada "
                                          "satu masa."),
                    source_row_ids=list(q["source_row_ids"]),
                    authority_refs=[q["question_id"]],
                    decision_ids=[q["stem_decision_id"]],
                    visual_obligations=[], binding_kind="SOURCE_ROWS"))
            out.append(dict(
                state_id=f"{sid}-ST-RESULT", screen_id=sid, position=sc["position"],
                state_kind="QUIZ_RESULT", declared_state_label="RESULT",
                trigger_id=f"{sid}-TRG-RESULT", trigger_label="submitting Q5",
                parent_state_id=f"{sid}-ST-05", resulting_state_id=f"{sid}-ST-RESULT",
                return_behaviour=RETURN_BEHAVIOURS["QUIZ_RESULT"],
                return_behaviour_ms=RETURN_BEHAVIOURS_MS["QUIZ_RESULT"],
                content_block_texts=[f"Markah lulus {A.FINAL_QUIZ['pass_mark']}",
                                     "Keputusan kuiz dipaparkan."],
                content_record_count=2,
                differs_from_base="Shows the outcome against the pass mark. No item is shown.",
                differs_from_base_ms=("Memaparkan keputusan berbanding markah lulus. Tiada "
                                      "item kuiz dipaparkan."),
                source_row_ids=[], authority_refs=[],
                decision_ids=["T04-DEC-A21"], visual_obligations=[],
                binding_kind="STRUCTURAL",
                binding_limitation=("Scoring behaviour is not specified in B1 and no answer "
                                    "key is final — see T04-OPEN-51."),
                binding_limitation_ms=("Kelakuan pemarkahan tidak ditetapkan dalam B1 dan "
                                       "tiada kunci jawapan yang muktamad — lihat "
                                       "T04-OPEN-01.")))

        # --- completion flag ---------------------------------------------------------------
        if declared and declared[-1] == "ALL_VIEWED":
            out.append(dict(
                state_id=f"{sid}-ST-ALL_VIEWED", screen_id=sid, position=sc["position"],
                state_kind="COMPLETION", declared_state_label="ALL_VIEWED",
                trigger_id=f"{sid}-TRG-ALL",
                trigger_label="every reveal or step viewed",
                parent_state_id=base_id, resulting_state_id=f"{sid}-ST-ALL_VIEWED",
                return_behaviour=RETURN_BEHAVIOURS["COMPLETION"],
                return_behaviour_ms=RETURN_BEHAVIOURS_MS["COMPLETION"],
                content_block_texts=[], content_record_count=0,
                content_empty_by_design=True,
                differs_from_base=("Displays nothing of its own. It is the completion flag "
                                   "that unlocks SETERUSNYA."),
                differs_from_base_ms=("Tidak memaparkan apa-apa kandungan sendiri. Ia "
                                      "penanda selesai yang membuka SETERUSNYA."),
                source_row_ids=[], authority_refs=[],
                decision_ids=list(sc["decision_ids"]), visual_obligations=[],
                binding_kind="STRUCTURAL"))
    return out


STATE_FIELDS = ["state_id", "screen_id", "state_kind", "trigger_id", "trigger_label",
                "parent_state_id", "resulting_state_id", "return_behaviour",
                "content_block_texts", "content_record_count", "differs_from_base",
                "source_row_ids", "authority_refs", "decision_ids", "binding_kind"]

# ==========================================================================================
# FROZEN STATE ROLL — the independent anchor for every coverage and appendix count.
#
# Why this exists. Mutation fixture A-03 removed one state from states() and rebuilt the
# appendix. Every appendix gate still passed, because the plan and the deck were both
# projected from the same mutated inventory: they agreed with each other about a state that
# had silently ceased to exist. A gate that compares a generated artifact with the generator
# that produced it cannot see a record leave the population.
#
# The roll below is the reviewed inventory written down once, by hand, at Stage 4.2F-B1.1.
# It is not derived from states(). Gates check the live inventory against it, so a state
# that disappears from the model fails loudly instead of vanishing from both sides at once.
# When the inventory legitimately changes, this roll must be updated in the same commit —
# THE_LIVE_STATE_INVENTORY_AGREES_WITH_THE_FROZEN_ROLL makes forgetting impossible to miss.
DECLARED_TOTAL_RUNTIME_STATES = 65
DECLARED_STATE_IDS = [
    "T04-S01-ST-BASE", "T04-S02-ST-BASE", "T04-S03-ST-BASE", "T04-S03-ST-01",
    "T04-S03-ST-02", "T04-S03-ST-03", "T04-S03-ST-04", "T04-S03-ST-05", "T04-S03-ST-06",
    "T04-S03-ST-ALL_VIEWED", "T04-S04-ST-BASE", "T04-S05-ST-BASE", "T04-S06-ST-BASE",
    "T04-S06-ST-01", "T04-S06-ST-02", "T04-S06-ST-ALL_VIEWED", "T04-S07-ST-BASE",
    "T04-S07-ST-01", "T04-S07-ST-02", "T04-S07-ST-03", "T04-S07-ST-04",
    "T04-S07-ST-ALL_VIEWED", "T04-S08-ST-BASE", "T04-S09-ST-BASE", "T04-S09-ST-01",
    "T04-S09-ST-02", "T04-S09-ST-03", "T04-S09-ST-ALL_VIEWED", "T04-S10-ST-BASE",
    "T04-S10-ST-01", "T04-S10-ST-02", "T04-S10-ST-03", "T04-S10-ST-04", "T04-S10-ST-05",
    "T04-S10-ST-ALL_VIEWED", "T04-S11-ST-BASE", "T04-S12-ST-BASE", "T04-S13-ST-BASE",
    "T04-S14-ST-BASE", "T04-S14-ST-01", "T04-S14-ST-02", "T04-S14-ST-03",
    "T04-S14-ST-ALL_VIEWED", "T04-S15-ST-BASE", "T04-S16-ST-BASE", "T04-S16-ST-01",
    "T04-S16-ST-02", "T04-S16-ST-03", "T04-S16-ST-ALL_VIEWED", "T04-S17-ST-BASE",
    "T04-S18-ST-BASE", "T04-S19-ST-BASE", "T04-S19-ST-01", "T04-S19-ST-02",
    "T04-S19-ST-03", "T04-S19-ST-04", "T04-S19-ST-ALL_VIEWED", "T04-S20-ST-BASE",
    "T04-S21-ST-01", "T04-S21-ST-02", "T04-S21-ST-03", "T04-S21-ST-04", "T04-S21-ST-05",
    "T04-S21-ST-RESULT", "T04-S22-ST-BASE"
]


def roll_audit():
    """The live inventory measured against the frozen roll — population delta, both ways."""
    live = [s["state_id"] for s in states()]
    frozen = list(DECLARED_STATE_IDS)
    return dict(
        frozen_count=len(frozen),
        declared_total=DECLARED_TOTAL_RUNTIME_STATES,
        live_count=len(live),
        missing_from_live=sorted(set(frozen) - set(live)),
        added_to_live=sorted(set(live) - set(frozen)),
        duplicate_live_ids=sorted({i for i in live if live.count(i) > 1}),
        agrees=sorted(live) == sorted(frozen))


def totals():
    st = states()
    return dict(
        learner_screens=len(SB.screens()),
        base_states=len([x for x in st if x["state_kind"] == "BASE"]),
        triggered_states=len([x for x in st if x["state_kind"] in
                              ("REVEAL", "STEP", "QUIZ_ITEM", "QUIZ_RESULT")]),
        completion_flags=len([x for x in st if x["state_kind"] == "COMPLETION"]),
        total_runtime_states=len(st),
        interactions=len([x for x in st if x["trigger_id"]
                          and x["state_kind"] != "COMPLETION"]),
        review_pages_b1=len(SB.slides()),
        continuation_pages_b1=len([s for s in SB.slides() if s["is_continuation"]]))


def verification():
    """Declared reveal targets checked against the screens' own controlled rows."""
    out = []
    for sid, targets in _REVEAL_TARGETS.items():
        sc = _screen(sid)
        own = set(sc["source_row_ids"])
        declared_st = len([x for x in sc["interaction_states"]
                           if x.startswith("ST-") or x.startswith("REVEAL_")])
        used = [t for t, rows in targets] + [r for _, rows in targets for r in rows]
        out.append(dict(
            screen_id=sid,
            declared_reveal_states=declared_st,
            declared_targets=len(targets),
            counts_agree=declared_st == len(targets),
            rows_outside_the_screen=sorted(set(used) - own),
            triggers_are_heading_or_list_rows=[
                t for t, _ in targets
                if C.BY_ID[t]["content_type"] not in ("HEADING_3", "HEADING_2", "LIST_ITEM")],
            all_rows_resolve=all(r in C.BY_ID for r in used)))
    return out
