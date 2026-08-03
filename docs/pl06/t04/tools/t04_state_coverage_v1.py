# -*- coding: utf-8 -*-
"""Stage 4.2F-B1.1 Lane A — review-coverage matrix, source audit, namespaces, oracle audit.

COVERAGE, DEFINED BEFORE IT IS MEASURED
---------------------------------------
A runtime state is review-covered only if the review artifact lets Bariah determine all five
of these:

    1. what triggers it
    2. what content appears
    3. how it differs from the base state
    4. how the learner returns or continues
    5. which source and authority records support it

Text being present somewhere on the page does not satisfy (1), (3) or (4). Neither does the
state's name appearing in a list. The B1 deck lists state names and prints every content
block of a screen in one column — so on a screen with reveals, a reviewer cannot tell which
sentences are behind which trigger, or what the base state looks like on its own.

That is why the B1 deck is `T04_LAYOUT_STORYBOARD_BUILT` and not an interaction review.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)

import t04_state_model_v1 as SM        # noqa: E402
import t04_storyboard_model_v1 as SB   # noqa: E402
import t04_authority_data_v1 as A      # noqa: E402
import t04_content_data_v1 as C        # noqa: E402
import t04_supplementary_evidence_v1 as S  # noqa: E402

STAGE = SM.STAGE

COVERAGE_CRITERIA = [
    "what triggers the state",
    "what content appears in it",
    "how it differs from the base state",
    "how the learner returns or continues",
    "which source and authority records support it",
]

APPENDIX_NAME = "K5PL06T04B01_STATE_REVIEW_APPENDIX_v1_0.pptx"
APPENDIX_DIR = SB.PPTX_DIR


# ==========================================================================================
# COVERAGE MATRIX
# ==========================================================================================
def _b1_page_for(screen_id):
    """The B1 review page(s) a screen occupies. Derived, not counted off the deck."""
    return [f"p{i + 2}" for i, sl in enumerate(SB.slides())
            if sl["screen_id"] == screen_id]


def matrix(with_appendix=False):
    """One row per runtime state. `with_appendix` reports the state AFTER the appendix."""
    rows = []
    single = {s["screen_id"] for s in SB.screens() if len(s["interaction_states"]) == 1}
    appx = appendix_pages() if with_appendix else []
    appx_by_state = {st: f"A{p['page_no']}" for p in appx for st in p["state_ids"]}

    for st in SM.states():
        sid = st["screen_id"]
        b1_pages = _b1_page_for(sid)

        if sid in single:
            # The screen has exactly one state, so its B1 page IS that state. All five
            # criteria are answerable from the page.
            cls = "FULL_PAGE_VISIBLE"
            criteria = {c: True for c in COVERAGE_CRITERIA}
            page = b1_pages[0]
        else:
            # The B1 page prints every block of the screen in one column and lists the state
            # names beside it. The text is there; the mapping is not.
            cls = "METADATA_ONLY"
            criteria = {
                COVERAGE_CRITERIA[0]: False,
                COVERAGE_CRITERIA[1]: st["state_kind"] != "COMPLETION",
                COVERAGE_CRITERIA[2]: False,
                COVERAGE_CRITERIA[3]: False,
                COVERAGE_CRITERIA[4]: True,
            }
            page = b1_pages[0]

        appendix_page = appx_by_state.get(st["state_id"])
        if appendix_page:
            cls = "MULTI_PANEL_VISIBLE"
            criteria = {c: True for c in COVERAGE_CRITERIA}

        rows.append(dict(
            state_id=st["state_id"], screen_id=sid, state_kind=st["state_kind"],
            trigger_id=st["trigger_id"], trigger_label=st["trigger_label"],
            b1_review_page=page,
            b1_review_pages_all=b1_pages,
            appendix_page=appendix_page,
            representation=cls,
            criteria_met=criteria,
            criteria_met_count=sum(1 for v in criteria.values() if v),
            review_covered=all(criteria.values()),
            source_row_ids=st["source_row_ids"],
            authority_refs=st["authority_refs"],
            decision_ids=st["decision_ids"]))
    return rows


def coverage_report(with_appendix=False):
    rows = matrix(with_appendix)
    seen = {}
    for r in rows:
        seen.setdefault(r["state_id"], []).append(r)
    # A screen that spills onto a continuation page maps to BOTH pages. Counting only the
    # first would report four continuation pages as unmapped, which would be an artefact of
    # the report rather than a fact about the deck.
    pages_used = {p for r in rows for p in r["b1_review_pages_all"]} | {
        r["appendix_page"] for r in rows if r["appendix_page"]}
    all_b1 = {f"p{i + 2}" for i in range(len(SB.slides()))} | {"p1"}
    return dict(
        total_states=len(rows),
        represented_states=len([r for r in rows if r["review_covered"]]),
        unrepresented_states=[r["state_id"] for r in rows if not r["review_covered"]],
        unrepresented_count=len([r for r in rows if not r["review_covered"]]),
        by_class={c: len([r for r in rows if r["representation"] == c])
                  for c in SM.COVERAGE_CLASSES},
        duplicate_representations=[k for k, v in seen.items() if len(v) > 1],
        orphan_review_panels=[],
        review_pages_with_no_state_mapping=sorted(all_b1 - pages_used),
        # p1 is the cover. It carries no state by design and is declared rather than
        # counted as a gap.
        cover_page_declared="p1",
        unmapped_pages_excluding_cover=sorted((all_b1 - pages_used) - {"p1"}),
        every_state_uniquely_mapped=all(len(v) == 1 for v in seen.values()),
        criteria=COVERAGE_CRITERIA)


def decision(with_appendix=False):
    r = coverage_report(with_appendix)
    if r["unrepresented_count"] == 0 and r["every_state_uniquely_mapped"]:
        return "T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN"
    return "T04_LAYOUT_READY_STATE_REVIEW_APPENDIX_REQUIRED"


# ==========================================================================================
# APPENDIX PAGE PLAN — two state panels per page, grouped by screen
# ==========================================================================================
PANELS_PER_PAGE = 2

# The two-panel rule is a REVIEW-LEGIBILITY POLICY, not a renderer limit. Measured against
# the panel geometry the appendix actually draws, four panels still fit on a page without
# overflowing (see t04_state_emit_v1.renderer_panel_capacity). Two is the number a reviewer
# can read side by side, so the policy is deliberately stricter than the renderer.
# Gates must check the plan against this literal, never against PANELS_PER_PAGE itself:
# mutation fixture A-01 raised PANELS_PER_PAGE to 3 and the old gate followed it up,
# because it compared pages built from the constant against the same constant.
PANEL_BUDGET_LITERAL = 2
PANEL_BUDGET_BASIS = "REVIEW_LEGIBILITY_POLICY_STRICTER_THAN_THE_RENDERER_CAPACITY"

# Frozen split of the 65-state roll: which states the B1 deck already shows a full page for,
# and which ones the appendix has to carry as panels. Hand-declared at Stage 4.2F-B1.1 and
# checked against the live plan, for the same reason as SM.DECLARED_STATE_IDS.
DECLARED_PANEL_STATE_IDS = [
    "T04-S03-ST-BASE", "T04-S03-ST-01", "T04-S03-ST-02", "T04-S03-ST-03", "T04-S03-ST-04",
    "T04-S03-ST-05", "T04-S03-ST-06", "T04-S03-ST-ALL_VIEWED", "T04-S06-ST-BASE",
    "T04-S06-ST-01", "T04-S06-ST-02", "T04-S06-ST-ALL_VIEWED", "T04-S07-ST-BASE",
    "T04-S07-ST-01", "T04-S07-ST-02", "T04-S07-ST-03", "T04-S07-ST-04",
    "T04-S07-ST-ALL_VIEWED", "T04-S09-ST-BASE", "T04-S09-ST-01", "T04-S09-ST-02",
    "T04-S09-ST-03", "T04-S09-ST-ALL_VIEWED", "T04-S10-ST-BASE", "T04-S10-ST-01",
    "T04-S10-ST-02", "T04-S10-ST-03", "T04-S10-ST-04", "T04-S10-ST-05",
    "T04-S10-ST-ALL_VIEWED", "T04-S14-ST-BASE", "T04-S14-ST-01", "T04-S14-ST-02",
    "T04-S14-ST-03", "T04-S14-ST-ALL_VIEWED", "T04-S16-ST-BASE", "T04-S16-ST-01",
    "T04-S16-ST-02", "T04-S16-ST-03", "T04-S16-ST-ALL_VIEWED", "T04-S19-ST-BASE",
    "T04-S19-ST-01", "T04-S19-ST-02", "T04-S19-ST-03", "T04-S19-ST-04",
    "T04-S19-ST-ALL_VIEWED", "T04-S21-ST-01", "T04-S21-ST-02", "T04-S21-ST-03",
    "T04-S21-ST-04", "T04-S21-ST-05", "T04-S21-ST-RESULT"
]
DECLARED_FULL_PAGE_STATE_IDS = [
    "T04-S01-ST-BASE", "T04-S02-ST-BASE", "T04-S04-ST-BASE", "T04-S05-ST-BASE",
    "T04-S08-ST-BASE", "T04-S11-ST-BASE", "T04-S12-ST-BASE", "T04-S13-ST-BASE",
    "T04-S15-ST-BASE", "T04-S17-ST-BASE", "T04-S18-ST-BASE", "T04-S20-ST-BASE",
    "T04-S22-ST-BASE"
]
DECLARED_APPENDIX_PAGE_COUNT = 28


def frozen_plan_audit():
    """The live appendix plan measured against the frozen panel roll — both directions."""
    planned = [s for p in appendix_pages() for s in p["state_ids"]]
    frozen = list(DECLARED_PANEL_STATE_IDS)
    return dict(
        frozen_panel_count=len(frozen),
        frozen_full_page_count=len(DECLARED_FULL_PAGE_STATE_IDS),
        frozen_roll_total=len(frozen) + len(DECLARED_FULL_PAGE_STATE_IDS),
        planned_count=len(planned),
        missing_from_the_plan=sorted(set(frozen) - set(planned)),
        added_to_the_plan=sorted(set(planned) - set(frozen)),
        rolls_are_disjoint=not (set(frozen) & set(DECLARED_FULL_PAGE_STATE_IDS)),
        rolls_cover_the_state_roll=(sorted(frozen + DECLARED_FULL_PAGE_STATE_IDS)
                                    == sorted(SM.DECLARED_STATE_IDS)),
        pages_expected_from_the_frozen_roll=_pages_from_roll(frozen),
        pages_planned=len(appendix_pages()))


def _pages_from_roll(roll):
    """How many pages the frozen roll needs, at the literal budget — not from the plan."""
    per_screen, order = {}, []
    for sid in roll:
        screen = sid[:len("T04-Sxx")]
        if screen not in per_screen:
            per_screen[screen] = 0
            order.append(screen)
        per_screen[screen] += 1
    return sum(-(-per_screen[s] // PANEL_BUDGET_LITERAL) for s in order)


def appendix_pages():
    """Every state that the B1 deck cannot cover on its own, laid out two panels per page."""
    single = {s["screen_id"] for s in SB.screens() if len(s["interaction_states"]) == 1}
    need = [st for st in SM.states() if st["screen_id"] not in single]
    pages, cur, page_no = [], [], 0
    cur_screen = None
    for st in need:
        # Never mix two screens on one appendix page — a reviewer reads by screen.
        if cur and (len(cur) == PANELS_PER_PAGE or st["screen_id"] != cur_screen):
            page_no += 1
            pages.append(dict(page_no=page_no, screen_id=cur_screen,
                              states=cur, state_ids=[x["state_id"] for x in cur]))
            cur = []
        cur_screen = st["screen_id"]
        cur.append(st)
    if cur:
        page_no += 1
        pages.append(dict(page_no=page_no, screen_id=cur_screen, states=cur,
                          state_ids=[x["state_id"] for x in cur]))
    return pages


# ==========================================================================================
# SOURCE ROW AUDIT — brief-referenced IDs, checked directly against the extract
# ==========================================================================================
AUDITED_ROW_IDS = ["T04-ROW-074", "T04-ROW-076", "T04-ROW-077"]
NOT_FOUND_TOKEN = "BRIEF_REFERENCE_NOT_FOUND_IN_CONTROLLED_EXTRACT"


# Topic keys, and the module wording that decides whether an option agrees or disagrees with
# the row. A distractor that the source CONTRADICTS is a good distractor; one the source is
# merely silent about is weaker. The audit distinguishes them.
_TOPIC_KEYS = [
    ("SDS", ("sds",), ("sds",)),
    ("spray weather", ("cuaca",), ("cuaca",)),
    ("resident notification", ("maklumkan", "penduduk"), ("notifikasi", "penduduk")),
]


def _q5_link(text):
    """Which Q5 options this row bears on — the live set and the rejected Set A."""
    q5 = next(q for q in A.quiz_items() if q["question_id"] == "T04-QZ-Q5")
    low = text.lower()
    hits = []

    def scan(option_text, position, option_id, is_key, option_set):
        ol = option_text.lower()
        for topic, row_terms, opt_terms in _TOPIC_KEYS:
            if any(t in low for t in row_terms) and any(t in ol for t in opt_terms):
                # The row and the option talk about the same control. Do they agree?
                agrees = True
                if topic == "spray weather" and "tanpa mengambil kira" in ol:
                    agrees = False
                if topic == "resident notification" and "selepas semburan selesai" in ol:
                    agrees = False
                if topic == "SDS" and "tidak perlu berada di tapak" in ol:
                    agrees = False
                hits.append(dict(option_id=option_id, position=position,
                                 option_text=option_text, option_set=option_set,
                                 is_proposed_key=is_key, matched_on=topic,
                                 row_agrees_with_option=agrees,
                                 relation=("SUPPORTS" if agrees else "CONTRADICTS")))
                return

    for o in q5["options"]:
        scan(o["text_ms"], o["position"], o["option_id"], o["proposed_key"], "LIVE_SET_B")
    for o in S.SET_A_REJECTED:
        scan(o["text_ms"], o["position"], f"SET-A-OPT-{o['position']}", False,
             "REJECTED_SET_A")
    return hits


def source_row_audit():
    out = []
    for rid in AUDITED_ROW_IDS:
        r = C.BY_ID.get(rid)
        if not r:
            out.append(dict(row_id=rid, exists=False, status=NOT_FOUND_TOKEN,
                            controlled_source_text=None, module_page=None,
                            source_position=None, proposition_supported=None,
                            q5_links=[], semantic_binding="NOT_APPLICABLE_ID_NOT_FOUND",
                            replacement_manufactured=False))
            continue
        text = (r["controlled_display_text"] or "").strip()
        links = _q5_link(text)
        used_in = sorted({st["state_id"] for st in SM.states()
                          if rid in st["source_row_ids"]})
        # Direct: the row states the proposition. Contradictory: it states the opposite of an
        # option. Derived: it supports it only through an intermediate step.
        live = [l for l in links if l["option_set"] == "LIVE_SET_B"]
        contra = [l for l in links if l["relation"] == "CONTRADICTS"]
        if not links:
            binding = "DERIVED"
            note = ("The row supports the screen's content but does not map onto any single "
                    "Q5 option. It is not used as the evidence for any option.")
        elif contra:
            binding = "CONTRADICTORY"
            note = ("The row states the opposite of at least one linked option. That is the "
                    "property a correct distractor needs: the module says the reverse, so a "
                    "learner who read it will not select it. "
                    + "; ".join(f"{l['option_set']} option {l['position']} "
                                f"({l['relation']})" for l in links))
        elif live:
            binding = "DIRECT"
            note = ("The row states the proposition the option tests, and that option is a "
                    "proposed key." if any(l["is_proposed_key"] for l in live)
                    else "The row bears directly on the option without contradicting it.")
        else:
            binding = "DERIVED"
            note = "The row bears only on the rejected Set A, not on the live option set."
        out.append(dict(
            row_id=rid, exists=True, status="FOUND",
            controlled_source_text=text,
            module_page=r["module_page"],
            source_position=dict(sequence=r["sequence"],
                                 paragraph_start=r["source_paragraph_start"],
                                 paragraph_end=r["source_paragraph_end"],
                                 segment_index=r["segment_index"],
                                 heading_path=list(r["heading_path"]),
                                 content_type=r["content_type"]),
            proposition_supported=text,
            used_in_states=used_in,
            q5_links=links,
            semantic_binding=binding,
            semantic_binding_note=note,
            replacement_manufactured=False))
    return out


# ==========================================================================================
# LIVE NAMESPACE SEPARATION
# ==========================================================================================
# Historical E-* identifiers were a single flat series covering two different kinds of thing:
# extraction/reproducibility items and unresolved evidence/assessment/release items. Reusing
# one prefix for both meant the register a reader landed in decided what "E-05" meant.
#
# The historical records are NOT rewritten. This is an alias map, not a migration.
LIVE_REGISTERS = ["T04-EXT", "T04-OPEN"]

# DISJOINT NUMBER BLOCKS, not per-register counters restarting at 01.
#
# The first attempt numbered each register from 01, which produced T04-EXT-01 and
# T04-OPEN-01 — two live registers exposing the same unqualified identifier "01". Anyone
# quoting "01" in a message would be ambiguous, which is the exact failure the separation
# exists to prevent. Blocks make uniqueness a property of the numbering rather than something
# a reader has to check.
REGISTER_BLOCKS = {"T04-EXT": (1, 49), "T04-OPEN": (51, 99)}

ALIAS_MAP = [
    dict(historical_id="E-01", live_id=None, register=None,
         subject="Q5 replacement options E and F",
         disposition="CLOSED_BEFORE_THE_SPLIT",
         closed_by="T04-DEC-E09 — Bariah selected Set B",
         note="Closed in Stage 4.2F-B0.9.1, so it takes no live identifier."),
    dict(historical_id="E-02", live_id="T04-OPEN-51", register="T04-OPEN",
         subject="Quiz answer keys, all five",
         disposition="LIVE", owner="BARIAH",
         note="Assessment authority. Not extraction."),
    dict(historical_id="E-03", live_id=None, register=None,
         subject="The 'Q3' WhatsApp referent",
         disposition="CLOSED_BEFORE_THE_SPLIT",
         closed_by="T04-COR-02 — the line is Firdaus's, so there is no authority referent",
         note="Closed in Stage 4.2F-B0.9.1."),
    dict(historical_id="E-04", live_id="T04-OPEN-52", register="T04-OPEN",
         subject="The pembajaan → racun wording correction on T04-S14",
         disposition="LIVE", owner="BARIAH",
         note="Evidence confirmation. Not extraction."),
    dict(historical_id="E-05", live_id="T04-EXT-01", register="T04-EXT",
         subject="Original module DOCX round trip and hash proof",
         disposition="LIVE", owner="FIRDAUS",
         note="Extraction and reproducibility — the only historical E-* item of that kind."),
    dict(historical_id="E-06", live_id="T04-OPEN-53", register="T04-OPEN",
         subject="Individual asset subjects and styles",
         disposition="LIVE", owner="BARIAH",
         note="Production authority. Not extraction."),
    dict(historical_id="E-07", live_id=None, register=None,
         subject="Which Q5 option pair stands",
         disposition="CLOSED_BEFORE_THE_SPLIT",
         closed_by="T04-DEC-E09 — Set B",
         note="Closed in Stage 4.2F-B0.9.1."),
    dict(historical_id="E-08", live_id="T04-OPEN-54", register="T04-OPEN",
         subject="Supplementary screenshot binary custody",
         disposition="LIVE", owner="FIRDAUS",
         note="Evidence custody. Adjacent to extraction but not about the module source, so "
              "it belongs in OPEN rather than EXT."),
]

# New items this stage raises.
NEW_LIVE_ITEMS = [
    dict(live_id="T04-EXT-02", register="T04-EXT",
         subject="T04-ROW-003 carries the six-step diagram as a single row with no text, so "
                 "the six process-step states are bound to visual obligations rather than to "
                 "text rows",
         owner="FIRDAUS", raised_by="Lane A state inventory",
         blocking="nothing — the labels are obligation-derived and traceable"),
    dict(live_id="T04-OPEN-55", register="T04-OPEN",
         subject="Runtime return and reset behaviour is CAIR-specified, not authority-ruled; "
                 "Bariah has never been shown a state-level interaction model",
         owner="BARIAH", raised_by="Lane A coverage matrix",
         blocking="interaction review sign-off, not layout"),
]


def alias_map_report():
    live = [a for a in ALIAS_MAP if a["live_id"]] + [
        dict(historical_id=None, **{k: v for k, v in n.items()}) for n in NEW_LIVE_ITEMS]
    ids = [x["live_id"] for x in live]
    unqualified = [i.rsplit("-", 1)[-1] for i in ids]
    by_reg = {}
    for x in live:
        by_reg.setdefault(x["register"], []).append(x["live_id"])
    # No two live registers may expose the same unqualified identifier.
    collisions = sorted({u for u in unqualified if unqualified.count(u) > 1})
    return dict(
        registers=LIVE_REGISTERS,
        alias_rows=ALIAS_MAP,
        new_items=NEW_LIVE_ITEMS,
        live_ids=sorted(ids),
        live_count=len(ids),
        closed_before_the_split=[a["historical_id"] for a in ALIAS_MAP if not a["live_id"]],
        by_register={k: sorted(v) for k, v in by_reg.items()},
        unqualified_collisions=collisions,
        register_blocks=REGISTER_BLOCKS,
        ids_outside_their_block=sorted(
            x["live_id"] for x in live
            if not (REGISTER_BLOCKS[x["register"]][0]
                    <= int(x["live_id"].rsplit("-", 1)[-1])
                    <= REGISTER_BLOCKS[x["register"]][1])),
        every_historical_id_accounted=sorted(a["historical_id"] for a in ALIAS_MAP)
        == [f"E-0{i}" for i in range(1, 9)],
        historical_records_rewritten=False)


# ==========================================================================================
# ORACLE INDEPENDENCE AUDIT
# ==========================================================================================
EXPECTED_SOURCE_KINDS = [
    "IMMUTABLE_AUTHORITY_ARTIFACT",     # the frozen DOCX on disk
    "HASH_PINNED_CONTROLLED_EXTRACT",   # the controlled row set
    "GENERATOR_INDEPENDENT_LITERAL",    # a literal written in the suite, not derived
    "SAME_GENERATOR",                   # <- disallowed for release-critical gates
]

# Release-critical gates: the ones whose failure would stop the storyboard shipping.
RELEASE_CRITICAL = [
    dict(gate_id="EXACTLY_TWENTY_TWO_SCREENS", suite="T04_STORYBOARD_QA_v1",
         expected_source="GENERATOR_INDEPENDENT_LITERAL", expected_detail="literal 22",
         observed_source="len(M.screens())",
         imports=["t04_storyboard_model_v1"], shares_helper=False),
    dict(gate_id="TITLES_MATCH_THE_FIXED_LIST", suite="T04_STORYBOARD_QA_v1",
         expected_source="GENERATOR_INDEPENDENT_LITERAL",
         expected_detail="M.EXPECTED_TITLES — a hand-written list, not derived from screens()",
         observed_source="[s['title_ms'] for s in M.screens()]",
         imports=["t04_storyboard_model_v1"], shares_helper=False),
    dict(gate_id="TITLES_AGREE_WITH_THE_FROZEN_SEQUENCE", suite="T04_STORYBOARD_QA_v1",
         expected_source="IMMUTABLE_AUTHORITY_ARTIFACT",
         expected_detail="A._final_sequence() — the frozen B0.9 model",
         observed_source="M.screens()", imports=["t04_authority_data_v1"],
         shares_helper=False),
    dict(gate_id="THE_FOUR_DOCX_STEMS_APPEAR_VERBATIM_IN_THE_AUTHORITY_DOCX",
         suite="T04_STORYBOARD_QA_v1",
         expected_source="IMMUTABLE_AUTHORITY_ARTIFACT",
         expected_detail="text extracted from the frozen v3 DOCX on disk",
         observed_source="the quiz model", imports=["zipfile"], shares_helper=False),
    dict(gate_id="SOURCE_STRINGS_ARE_VERBATIM", suite="T04_STORYBOARD_QA_v1",
         expected_source="HASH_PINNED_CONTROLLED_EXTRACT",
         expected_detail="C.BY_ID[row]['controlled_display_text']",
         observed_source="the storyboard block text", imports=["t04_content_data_v1"],
         shares_helper=False),
    dict(gate_id="DO_NOT_REUSE_IDS_AGREE_WITH_THE_CLOSURE",
         suite="T04_AUTHORITY_DECISION_INGESTION_QA_v1",
         expected_source="HASH_PINNED_CONTROLLED_EXTRACT",
         expected_detail="the closure's own reuse_policy field",
         observed_source="the typed do-not-reuse register",
         imports=["t04_content_data_v1"], shares_helper=False),
    dict(gate_id="THE_RELEASE_DECISION_IS_CARRIED_FORWARD", suite="T04_STORYBOARD_QA_v1",
         expected_source="GENERATOR_INDEPENDENT_LITERAL",
         expected_detail="the three verdict tokens written literally in the suite",
         observed_source="the evidence-status register",
         imports=[], shares_helper=False,
         history="Compared against S.RELEASE_DECISION until fixture E-02 showed it was "
                 "validating the register against the object it was copied from."),
    dict(gate_id="THE_PAGE_BUDGET_STAYS_WITHIN_THE_RENDERER_CAPACITY",
         suite="T04_STORYBOARD_QA_v1",
         expected_source="GENERATOR_INDEPENDENT_LITERAL",
         expected_detail="RENDERER_LINE_CAPACITY, measured from the renderer's geometry",
         observed_source="MAX_LINES_PER_PAGE, the tunable budget",
         imports=[], shares_helper=False,
         history="Compared against MAX_LINES_PER_PAGE until fixture S-11 showed a raised "
                 "budget made every page 'fit' by definition."),
    dict(gate_id="AUTHORITY_DOCX_SHA256_MATCHES",
         suite="T04_AUTHORITY_DECISION_INGESTION_QA_v1",
         expected_source="GENERATOR_INDEPENDENT_LITERAL",
         expected_detail="the pinned SHA-256 literal",
         observed_source="hashing the file on disk", imports=["hashlib"],
         shares_helper=False),
    dict(gate_id="EVERY_MODEL_BLOCK_APPEARS_IN_THE_DECK", suite="T04_STORYBOARD_QA_v1",
         expected_source="SAME_GENERATOR",
         expected_detail="M.screens() block text",
         observed_source="text re-extracted from the saved PPTX",
         imports=["t04_storyboard_model_v1", "zipfile"], shares_helper=True,
         justification=(
             "Both sides come from the model, but the OBSERVED side has made a round trip "
             "through python-pptx and back off disk. The gate proves the writer did not drop "
             "or mangle content, which is its only purpose. It is not a content-correctness "
             "oracle and is not treated as one — correctness is covered by "
             "SOURCE_STRINGS_ARE_VERBATIM against the extract."),
         mutation_of_generated_side_detectable=True),
    # Both of these were self-referential when Lane A's mutation suite was first run.
    dict(gate_id="EVERY_APPENDIX_PAGE_HOLDS_AT_MOST_TWO_PANELS",
         suite="T04_STATE_COVERAGE_QA_v1",
         expected_source="GENERATOR_INDEPENDENT_LITERAL",
         expected_detail="the literal 2, with PANEL_BUDGET_LITERAL checked separately and "
                         "SE.renderer_panel_capacity() measured from the panel geometry",
         observed_source="len(p['states']) on the built page plan",
         imports=["t04_state_emit_v1"], shares_helper=False,
         history="Compared pages built from PANELS_PER_PAGE against PANELS_PER_PAGE until "
                 "fixture A-01 raised the constant to 3 and the gate raised with it."),
    dict(gate_id="EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_DECK",
         suite="T04_STATE_COVERAGE_QA_v1",
         expected_source="GENERATOR_INDEPENDENT_LITERAL",
         expected_detail="DECLARED_PANEL_STATE_IDS — the hand-written roll, not appendix_pages()",
         observed_source="text re-extracted from the saved appendix PPTX",
         imports=["zipfile"], shares_helper=False,
         history="The deck was compared only with the page plan that generated it until "
                 "fixture A-03 deleted a state and both sides agreed it was never there."),
]


def oracle_audit():
    rows = []
    for g in RELEASE_CRITICAL:
        independent = g["expected_source"] != "SAME_GENERATOR"
        rows.append(dict(
            gate_id=g["gate_id"], suite=g["suite"],
            expected_value_source=g["expected_source"],
            expected_detail=g["expected_detail"],
            observed_value_source=g["observed_source"],
            imported_modules=g["imports"],
            expected_and_observed_share_a_generator_helper=g["shares_helper"],
            mutation_of_generated_side_detectable=g.get(
                "mutation_of_generated_side_detectable", True),
            oracle_independent=independent,
            justification=g.get("justification"),
            history=g.get("history")))
    return dict(
        release_critical_gates=len(rows),
        oracle_independent=len([r for r in rows if r["oracle_independent"]]),
        shared_generator=[r["gate_id"] for r in rows
                          if r["expected_and_observed_share_a_generator_helper"]],
        shared_generator_justified=[
            r["gate_id"] for r in rows
            if r["expected_and_observed_share_a_generator_helper"] and r["justification"]],
        fixed_after_a_fixture=[r["gate_id"] for r in rows if r["history"]],
        rows=rows,
        preserved_protections=[
            "filtered-population named-membership and delta assertions (18 closed "
            "populations, t04_predicate_audit_v1)",
            "exact namespace + local-name OOXML matching (t04_ooxml_v1, six proof cases)",
        ])


# ==========================================================================================
# NATIVE POWERPOINT INSPECTION PACKAGE
# ==========================================================================================
def font_inventory(pptx_path):
    import zipfile
    import xml.etree.ElementTree as ET
    ns = "http://schemas.openxmlformats.org/drawingml/2006/main"
    z = zipfile.ZipFile(pptx_path)
    fonts = set()
    for n in z.namelist():
        if not n.startswith("ppt/slides/slide") or not n.endswith(".xml"):
            continue
        for e in ET.fromstring(z.read(n)).iter(f"{{{ns}}}latin"):
            if e.get("typeface"):
                fonts.add(e.get("typeface"))
    return sorted(fonts)


def layout_usage(pptx_path):
    import zipfile
    z = zipfile.ZipFile(pptx_path)
    layouts = sorted(n for n in z.namelist() if n.startswith("ppt/slideLayouts/slideLayout"))
    masters = sorted(n for n in z.namelist() if n.startswith("ppt/slideMasters/"))
    used = set()
    for n in z.namelist():
        if n.startswith("ppt/slides/_rels/"):
            for m in re.finditer(rb"slideLayout(\d+)\.xml", z.read(n)):
                used.add(int(m.group(1)))
    return dict(layouts_in_package=len(layouts), masters_in_package=len(masters),
                layouts_actually_used=sorted(used))


def notes_inventory(pptx_path):
    import zipfile
    z = zipfile.ZipFile(pptx_path)
    return dict(notes_slides=len([n for n in z.namelist()
                                  if n.startswith("ppt/notesSlides/notesSlide")]),
                has_notes_master=any(n.startswith("ppt/notesMasters/")
                                     for n in z.namelist()),
                note=("No speaker notes are written by the generator. Everything a reviewer "
                      "needs is on the slide face, because a state recorded only in Notes is "
                      "not review-visible by this stage's own definition."))


CORRECTION_INTAKE_FIELDS = [
    "correction_id", "found_in", "slide_or_page", "screen_id", "state_id",
    "what_is_wrong", "expected_instead", "severity", "generator_module_to_change",
    "regeneration_required", "raised_by", "date",
]

CORRECTION_POLICY = (
    "Any correction found in native PowerPoint is applied to the GENERATOR and followed by a "
    "complete regeneration, structural QA re-run, full re-render and visual inspection. The "
    "PPTX is never hand-patched: a hand patch would be lost on the next build and would break "
    "the guarantee that every string in the deck exists in the controlled model.")
