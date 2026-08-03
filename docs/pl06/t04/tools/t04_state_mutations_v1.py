# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-B1.1 Lane A.

    SUITE_ID = T04_STATE_COVERAGE_QA_v1
    python3 docs/pl06/t04/tools/t04_state_mutations_v1.py

The defects this suite exists to catch are all forms of *claiming coverage that does not
exist*: a state silently dropped from the inventory, a panel that never reached the deck, a
"NOTES_ONLY" state counted as visible, a missing source row papered over with a substitute,
two registers quietly sharing an identifier, or an oracle re-pointed at its own generator.

Fixtures marked `rebuild` regenerate the appendix from the mutated model and leave the
corrupted deck on disk for the suite to re-read. The real appendix is rebuilt clean in the
`finally` and `appendix_rebuilt_clean` compares its extracted text back to the baseline.
"""
import copy
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import t04_state_model_v1 as SM       # noqa: E402
import t04_state_coverage_v1 as CV    # noqa: E402
import t04_state_emit_v1 as SE        # noqa: E402
import t04_storyboard_model_v1 as SB  # noqa: E402
import t04_content_data_v1 as C       # noqa: E402
import t04_state_qa_v1 as QA          # noqa: E402

TARGETS = {"SM": SM, "CV": CV, "SE": SE, "SB": SB, "C": C, "QA": QA}

_BASE_STATES = _BASE_MATRIX = _BASE_AUDIT = _BASE_ALIAS = _BASE_ORACLE = None
_BASE_PAGES = None


def _states_base():
    return _BASE_STATES


def _st(fn):
    """Patch the state projection so every consumer sees the mutation."""
    def apply():
        def patched():
            rows = copy.deepcopy(_states_base())
            fn(rows)
            return rows
        return dict(states=patched)
    return apply


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


FIXTURES = [
    # ================= state inventory =================
    dict(fid="I-01", title="a runtime state is dropped from the inventory",
         gates=["SIXTY_FIVE_RUNTIME_STATES", "TOTAL_EQUALS_THE_DECLARED_STATE_LABELS"],
         patch=_st(lambda r: r.remove(_find(r, "state_id", "T04-S16-ST-02")))),
    dict(fid="I-02", title="a 66th state is invented",
         gates=["SIXTY_FIVE_RUNTIME_STATES", "TOTAL_EQUALS_THE_DECLARED_STATE_LABELS"],
         patch=_st(lambda r: r.append(dict(r[-1], state_id="T04-S22-ST-99")))),
    dict(fid="I-03", title="two states share an ID",
         gates=["STATE_IDS_ARE_UNIQUE"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S07-ST-02")
                   .update(state_id="T04-S07-ST-01"))),
    dict(fid="I-04", title="a triggered state loses its trigger",
         gates=["EVERY_NON_BASE_STATE_HAS_A_TRIGGER",
                "INTERACTION_COUNT_EQUALS_TRIGGERED_STATES"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S10-ST-03").update(trigger_id=None))),
    dict(fid="I-05", title="a state points at a parent that does not exist",
         gates=["EVERY_PARENT_RESOLVES"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S06-ST-01")
                   .update(parent_state_id="T04-S06-ST-ZZ"))),
    dict(fid="I-06", title="a state loses its return behaviour",
         gates=["EVERY_STATE_STATES_ITS_RETURN_BEHAVIOUR"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S16-ST-01")
                   .update(return_behaviour=""))),
    dict(fid="I-07", title="a panel loses its reviewer-facing Malay",
         gates=["EVERY_STATE_HAS_REVIEWER_FACING_MALAY"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S19-ST-02")
                   .update(return_behaviour_ms=""))),
    dict(fid="I-08", title="a content state is emptied without being a completion flag",
         gates=["ONLY_COMPLETION_FLAGS_ARE_CONTENTLESS"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S09-ST-02")
                   .update(content_record_count=0, content_block_texts=[]))),
    dict(fid="I-09", title="a state cites a source row that does not exist",
         gates=["EVERY_SOURCE_ROW_IN_A_STATE_RESOLVES"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S07-ST-01")
                   .update(source_row_ids=["T04-ROW-999"]))),
    dict(fid="I-10", title="a state cites a decision that does not exist",
         gates=["EVERY_DECISION_IN_A_STATE_RESOLVES"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S14-ST-01")
                   .update(decision_ids=["T04-DEC-ZZ"]))),
    dict(fid="I-11", title="a state is given an undeclared kind",
         gates=["EVERY_STATE_IS_TYPED"],
         patch=_st(lambda r: _find(r, "state_id", "T04-S03-ST-01")
                   .update(state_kind="MYSTERY"))),
    dict(fid="I-12", title="the diagram-step binding limitation is erased",
         gates=["THE_DIAGRAM_STEP_LIMITATION_IS_DECLARED"],
         patch=_st(lambda r: [x.update(binding_kind="SOURCE_ROWS") for x in r
                              if x["binding_kind"]
                              == "DIAGRAM_OBLIGATION_NOT_A_TEXT_ROW"])),
    dict(fid="I-13", title="a reveal target is pointed at another screen's row",
         target="SM",
         gates=["NO_REVEAL_TARGET_ROW_BELONGS_TO_ANOTHER_SCREEN"],
         patch=lambda: dict(_REVEAL_TARGETS=dict(
             SM._REVEAL_TARGETS,
             **{"T04-S06": [("T04-ROW-009", ["T04-ROW-010"]),
                            ("T04-ROW-011", ["T04-ROW-041"])]}))),
    dict(fid="I-14", title="a reveal target count stops matching the frozen states",
         target="SM",
         gates=["REVEAL_TARGET_COUNTS_AGREE_WITH_THE_FROZEN_STATES"],
         patch=lambda: dict(_REVEAL_TARGETS=dict(
             SM._REVEAL_TARGETS,
             **{"T04-S07": SM._REVEAL_TARGETS["T04-S07"][:3]}))),
    dict(fid="I-15", title="a trigger is pointed at a body paragraph rather than a heading",
         target="SM",
         gates=["EVERY_TRIGGER_IS_A_HEADING_OR_LIST_ROW"],
         patch=lambda: dict(_REVEAL_TARGETS=dict(
             SM._REVEAL_TARGETS,
             **{"T04-S09": [("T04-ROW-030", ["T04-ROW-030"]),
                            ("T04-ROW-031", ["T04-ROW-032"]),
                            ("T04-ROW-033", ["T04-ROW-034"])]}))),

    # ================= coverage =================
    dict(fid="C-01", title="a metadata-only state is counted as review-covered",
         target="CV",
         gates=["THE_B1_DECK_ALONE_DOES_NOT_COVER_THE_STATES",
                "THE_DECISION_BEFORE_THE_APPENDIX_REQUIRED_ONE"],
         patch=lambda: dict(matrix=lambda with_appendix=False: [
             dict(r, review_covered=True, criteria_met_count=5,
                  representation="FULL_PAGE_VISIBLE") for r in _BASE_MATRIX])),
    dict(fid="C-02", title="a state is declared covered on four of the five criteria",
         target="CV",
         gates=["EVERY_STATE_MEETS_ALL_FIVE_CRITERIA"],
         patch=lambda: dict(matrix=lambda with_appendix=False: [
             dict(r, criteria_met_count=4) if r["state_id"] == "T04-S16-ST-01" else r
             for r in _BASE_MATRIX])),
    dict(fid="C-03", title="a coverage criterion is dropped from the definition",
         target="CV", gates=["FIVE_COVERAGE_CRITERIA_DECLARED"],
         patch=lambda: dict(COVERAGE_CRITERIA=CV.COVERAGE_CRITERIA[:4])),
    dict(fid="C-04", title="states are parked in NOTES_ONLY and counted",
         target="CV",
         gates=["NOTHING_IS_COUNTED_AS_NOTES_ONLY", "EVERY_STATE_MEETS_ALL_FIVE_CRITERIA"],
         patch=lambda: dict(matrix=lambda with_appendix=False: [
             dict(r, representation="NOTES_ONLY", review_covered=True, criteria_met_count=4)
             if r["state_id"].endswith("ST-02") else r for r in _BASE_MATRIX])),
    dict(fid="C-05", title="a state appears twice in the matrix",
         target="CV",
         gates=["EVERY_STATE_IS_UNIQUELY_MAPPED", "NO_DUPLICATE_REPRESENTATIONS"],
         patch=lambda: dict(matrix=lambda with_appendix=False:
                            _BASE_MATRIX + [_BASE_MATRIX[5]])),

    # ================= appendix =================
    # A-01 walked past the suite on its first run. EVERY_APPENDIX_PAGE_HOLDS_AT_MOST_TWO
    # _PANELS compared pages built from PANELS_PER_PAGE against PANELS_PER_PAGE, so raising
    # the constant raised the gate with it. It now checks the literal budget.
    dict(fid="A-01", title="an appendix page carries three panels",
         target="CV", gates=["EVERY_APPENDIX_PAGE_HOLDS_AT_MOST_TWO_PANELS",
                             "THE_PANEL_BUDGET_MATCHES_THE_DECLARED_REVIEW_POLICY"],
         patch=lambda: dict(PANELS_PER_PAGE=3)),
    dict(fid="A-02", title="an appendix page mixes two screens",
         target="CV",
         gates=["NO_APPENDIX_PAGE_MIXES_TWO_SCREENS"],
         patch=lambda: dict(appendix_pages=lambda: [
             dict(page_no=1, screen_id="T04-S03",
                  states=[SM.states()[1], SM.states()[10]],
                  state_ids=[SM.states()[1]["state_id"], SM.states()[10]["state_id"]])])),
    # A-03 also walked past on its first run. Deleting a state removed it from the page plan
    # and from the deck at the same time, so every plan-versus-deck gate stayed consistent
    # about a state that no longer existed. The designated gates are now the frozen-roll
    # ones, which no generator can rewrite.
    dict(fid="A-03", title="a state panel never reaches the appendix deck",
         gates=["THE_LIVE_STATE_INVENTORY_AGREES_WITH_THE_FROZEN_ROLL",
                "EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_PLAN",
                "EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_DECK",
                "THE_APPENDIX_SLIDE_COUNT_MATCHES_THE_FROZEN_ROLL"],
         rebuild=True,
         patch=_st(lambda r: r.remove(_find(r, "state_id", "T04-S10-ST-04")))),
    dict(fid="A-04", title="a trigger label is dropped from the panel",
         target="SE", gates=["EVERY_APPENDIX_TRIGGER_LABEL_IS_IN_THE_DECK"],
         rebuild=True, patch=lambda: dict(_state_panel=_panel_without("Pencetus"))),
    dict(fid="A-05", title="the return-behaviour line is dropped from the panel",
         target="SE", gates=["EVERY_APPENDIX_RETURN_BEHAVIOUR_IS_IN_THE_DECK"],
         rebuild=True, patch=lambda: dict(_state_panel=_panel_without_return())),
    dict(fid="A-06", title="the difference-from-base line is dropped from the panel",
         target="SE", gates=["EVERY_APPENDIX_DIFFERENCE_LINE_IS_IN_THE_DECK"],
         rebuild=True, patch=lambda: dict(_state_panel=_panel_without_diff())),
    dict(fid="A-07", title="the panel reverts to English",
         target="SM", gates=["THE_APPENDIX_IS_IN_MALAY_NOT_ENGLISH"],
         rebuild=True,
         patch=lambda: dict(RETURN_BEHAVIOURS_MS=dict(
             SM.RETURN_BEHAVIOURS_MS, REVEAL=SM.RETURN_BEHAVIOURS["REVEAL"]))),
    dict(fid="A-08", title="a repository path is printed into the appendix",
         target="SE", gates=["NO_REPOSITORY_PATH_IN_THE_APPENDIX"],
         rebuild=True,
         patch=lambda: dict(BANNER="docs/pl06/t04/tools",
                            KIND_LABEL_MS=dict(SM.__dict__.get("x", {}),
                                               **{k: "docs/pl06 " + v
                                                  for k, v in SE.KIND_LABEL_MS.items()}))),
    dict(fid="A-09", title="the appendix is written over the B1 deck",
         target="CV", gates=["THE_B1_DECK_IS_A_SEPARATE_FILE"],
         patch=lambda: dict(APPENDIX_NAME=SB.PPTX_NAME)),
    # A-10 to A-14 attack the repairs themselves: an anchor nobody can move is no anchor.
    dict(fid="A-10", title="the frozen roll is quietly shortened to match a smaller model",
         target="SM",
         gates=["THE_FROZEN_STATE_ROLL_HOLDS_SIXTY_FIVE_IDS",
                "THE_LIVE_STATE_INVENTORY_AGREES_WITH_THE_FROZEN_ROLL",
                "THE_TWO_FROZEN_ROLLS_PARTITION_THE_STATE_ROLL"],
         patch=lambda: dict(DECLARED_STATE_IDS=SM.DECLARED_STATE_IDS[:-1])),
    dict(fid="A-11", title="the declared total is edited instead of the roll",
         target="SM", gates=["THE_FROZEN_STATE_ROLL_HOLDS_SIXTY_FIVE_IDS"],
         patch=lambda: dict(DECLARED_TOTAL_RUNTIME_STATES=64)),
    dict(fid="A-12", title="the literal panel budget is relaxed to three",
         target="CV", gates=["THE_PANEL_BUDGET_MATCHES_THE_DECLARED_REVIEW_POLICY"],
         patch=lambda: dict(PANEL_BUDGET_LITERAL=3)),
    dict(fid="A-13", title="a panel state is reclassified as already full-page visible",
         target="CV",
         # The union is unchanged, so the partition gate cannot see this one — it takes the
         # plan-membership pair, which is why both directions of the delta are checked.
         gates=["EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_PLAN",
                "EVERY_FROZEN_FULL_PAGE_STATE_IS_IN_THE_B1_DECK_NOT_THE_APPENDIX"],
         patch=lambda: dict(
             DECLARED_PANEL_STATE_IDS=[i for i in CV.DECLARED_PANEL_STATE_IDS
                                       if i != "T04-S16-ST-03"],
             DECLARED_FULL_PAGE_STATE_IDS=CV.DECLARED_FULL_PAGE_STATE_IDS
             + ["T04-S16-ST-03"])),
    dict(fid="A-14", title="a whole screen's panels are dropped from the page plan",
         target="CV",
         gates=["EVERY_FROZEN_PANEL_STATE_IS_IN_THE_APPENDIX_PLAN",
                "APPENDIX_SLIDE_COUNT_MATCHES_THE_PLAN"],
         patch=lambda: dict(appendix_pages=lambda: [
             p for p in _BASE_PAGES if p["screen_id"] != "T04-S14"])),
    dict(fid="A-15", title="the measured renderer capacity is replaced by an assertion",
         target="SE",
         gates=["THE_RENDERER_CAPACITY_IS_MEASURED_NOT_ASSERTED",
                "THE_PANEL_BUDGET_STAYS_WITHIN_THE_RENDERER_CAPACITY"],
         patch=lambda: dict(renderer_panel_capacity=lambda: 1)),

    # ================= source audit =================
    dict(fid="S-01", title="a missing row ID is silently given a replacement binding",
         target="CV",
         gates=["NO_REPLACEMENT_BINDING_WAS_MANUFACTURED",
                "ALL_THREE_EXIST_IN_THE_CONTROLLED_EXTRACT"],
         patch=lambda: dict(source_row_audit=lambda: [
             dict(r, exists=False, replacement_manufactured=True,
                  status="SUBSTITUTED_WITH_T04-ROW-075")
             if r["row_id"] == "T04-ROW-077" else r for r in _BASE_AUDIT])),
    dict(fid="S-02", title="an audited row loses its quoted source text",
         target="CV", gates=["EVERY_AUDITED_ROW_QUOTES_ITS_SOURCE_TEXT"],
         patch=lambda: dict(source_row_audit=lambda: [
             dict(r, controlled_source_text=None) for r in _BASE_AUDIT])),
    dict(fid="S-03", title="an audited row loses its page and position",
         target="CV", gates=["EVERY_AUDITED_ROW_REPORTS_ITS_PAGE_AND_POSITION"],
         patch=lambda: dict(source_row_audit=lambda: [
             dict(r, module_page=None, source_position=None) for r in _BASE_AUDIT])),
    dict(fid="S-04", title="the not-found token is renamed to something softer",
         target="CV", gates=["THE_NOT_FOUND_TOKEN_IS_DECLARED"],
         patch=lambda: dict(NOT_FOUND_TOKEN="ROW_PENDING")),
    dict(fid="S-05", title="the audit list is narrowed to two rows",
         target="CV", gates=["THREE_ROWS_AUDITED", "THE_AUDITED_IDS_ARE_THE_BRIEFS_IDS"],
         patch=lambda: dict(AUDITED_ROW_IDS=CV.AUDITED_ROW_IDS[:2])),
    dict(fid="S-06", title="the contradiction against the live Set B distractor is erased",
         target="CV", gates=["ROW_076_CONTRADICTS_THE_LIVE_SET_B_DISTRACTOR"],
         patch=lambda: dict(source_row_audit=lambda: [
             dict(r, q5_links=[l for l in r["q5_links"]
                               if l["relation"] != "CONTRADICTS"])
             for r in _BASE_AUDIT])),

    # ================= namespace =================
    dict(fid="N-01", title="two live registers reuse the same unqualified number",
         target="CV",
         gates=["NO_TWO_REGISTERS_SHARE_AN_UNQUALIFIED_ID",
                "EVERY_LIVE_ID_SITS_INSIDE_ITS_REGISTER_BLOCK"],
         patch=lambda: dict(ALIAS_MAP=[
             dict(a, live_id="T04-OPEN-01") if a["historical_id"] == "E-02" else a
             for a in CV.ALIAS_MAP])),
    dict(fid="N-02", title="a live ID escapes its register block",
         target="CV", gates=["EVERY_LIVE_ID_SITS_INSIDE_ITS_REGISTER_BLOCK"],
         patch=lambda: dict(ALIAS_MAP=[
             dict(a, live_id="T04-EXT-77") if a["historical_id"] == "E-05" else a
             for a in CV.ALIAS_MAP])),
    dict(fid="N-03", title="the blocks are made to overlap",
         target="CV", gates=["THE_BLOCKS_DO_NOT_OVERLAP"],
         patch=lambda: dict(REGISTER_BLOCKS={"T04-EXT": (1, 60), "T04-OPEN": (51, 99)})),
    dict(fid="N-04", title="a historical E-* identifier is dropped from the alias map",
         target="CV",
         gates=["EVERY_HISTORICAL_E_ID_IS_ACCOUNTED_FOR"],
         patch=lambda: dict(ALIAS_MAP=CV.ALIAS_MAP[:-1])),
    dict(fid="N-05", title="a closed alias stops naming what closed it",
         target="CV", gates=["EVERY_CLOSED_ALIAS_NAMES_WHAT_CLOSED_IT"],
         patch=lambda: dict(ALIAS_MAP=[
             {k: v for k, v in a.items() if k != "closed_by"} if not a["live_id"] else a
             for a in CV.ALIAS_MAP])),
    dict(fid="N-06", title="an assessment item is filed in the extraction register",
         target="CV", gates=["THE_ONLY_EXTRACTION_ITEM_INHERITED_IS_E05"],
         patch=lambda: dict(ALIAS_MAP=[
             dict(a, register="T04-EXT", live_id="T04-EXT-03")
             if a["historical_id"] == "E-02" else a for a in CV.ALIAS_MAP])),
    dict(fid="N-07", title="the historical records are marked as rewritten",
         target="CV", gates=["HISTORICAL_RECORDS_WERE_NOT_REWRITTEN"],
         patch=lambda: dict(alias_map_report=lambda: dict(
             _BASE_ALIAS, historical_records_rewritten=True))),

    # ================= oracle independence =================
    dict(fid="O-01", title="a release-critical gate is re-pointed at its own generator",
         target="CV",
         gates=["AT_MOST_ONE_GATE_SHARES_A_GENERATOR",
                "EVERY_SHARED_GENERATOR_GATE_IS_JUSTIFIED"],
         patch=lambda: dict(RELEASE_CRITICAL=[
             dict(g, expected_source="SAME_GENERATOR", shares_helper=True,
                  justification=None)
             if g["gate_id"] == "TITLES_MATCH_THE_FIXED_LIST" else g
             for g in CV.RELEASE_CRITICAL])),
    dict(fid="O-02", title="the one shared-generator gate loses its justification",
         target="CV", gates=["EVERY_SHARED_GENERATOR_GATE_IS_JUSTIFIED"],
         patch=lambda: dict(RELEASE_CRITICAL=[
             dict(g, justification=None) if g["shares_helper"] else g
             for g in CV.RELEASE_CRITICAL])),
    dict(fid="O-03", title="an expected-value source outside the declared set appears",
         target="CV", gates=["EVERY_EXPECTED_SOURCE_IS_FROM_THE_DECLARED_SET"],
         patch=lambda: dict(RELEASE_CRITICAL=[
             dict(g, expected_source="WHATEVER_THE_MODEL_SAYS")
             if g["gate_id"] == "AUTHORITY_DOCX_SHA256_MATCHES" else g
             for g in CV.RELEASE_CRITICAL])),
    dict(fid="O-04", title="a gate can no longer see a mutation of the generated side",
         target="CV",
         gates=["EVERY_GATE_CAN_SEE_A_MUTATION_OF_THE_GENERATED_SIDE"],
         patch=lambda: dict(RELEASE_CRITICAL=[
             dict(g, mutation_of_generated_side_detectable=False)
             if g["gate_id"] == "SOURCE_STRINGS_ARE_VERBATIM" else g
             for g in CV.RELEASE_CRITICAL])),
    dict(fid="O-05", title="the audit forgets the gates a fixture already fixed",
         target="CV",
         gates=["EVERY_SELF_REFERENTIAL_GATE_IS_RECORDED_AS_FIXED",
                "THE_TWO_LANE_A_ORACLE_DEFECTS_ARE_ATTRIBUTED_TO_THEIR_FIXTURES"],
         patch=lambda: dict(RELEASE_CRITICAL=[
             {k: v for k, v in g.items() if k != "history"} for g in CV.RELEASE_CRITICAL])),
    dict(fid="O-06", title="the filtered-population protection is dropped from the record",
         target="CV",
         gates=["THE_FILTERED_POPULATION_PROTECTION_IS_PRESERVED"],
         patch=lambda: dict(oracle_audit=lambda: dict(
             _BASE_ORACLE, preserved_protections=[
                 p for p in _BASE_ORACLE["preserved_protections"]
                 if "filtered-population" not in p]))),
    dict(fid="O-07", title="the exact-XML-element protection is dropped from the record",
         target="CV",
         gates=["THE_EXACT_XML_ELEMENT_PROTECTION_IS_PRESERVED"],
         patch=lambda: dict(oracle_audit=lambda: dict(
             _BASE_ORACLE, preserved_protections=[
                 p for p in _BASE_ORACLE["preserved_protections"]
                 if "exact namespace" not in p]))),

    # ================= status guard =================
    dict(fid="G-01", title="the B1 artifact is upgraded to interaction-review-complete",
         target="SM", gates=["THE_B1_ARTIFACT_IS_A_LAYOUT_STORYBOARD"],
         patch=lambda: dict(CURRENT_STATUS="T04_INTERACTION_REVIEW_COMPLETE")),
    dict(fid="G-02", title="the storyboard is declared frozen",
         target="SM", gates=["THE_B1_ARTIFACT_IS_A_LAYOUT_STORYBOARD"],
         patch=lambda: dict(CURRENT_STATUS="T04_STORYBOARD_FROZEN")),
    dict(fid="G-03", title="the forbidden-claim list is emptied",
         target="SM", gates=["THREE_FORBIDDEN_CLAIMS_ARE_DECLARED"],
         patch=lambda: dict(FORBIDDEN_STATUS_CLAIMS=[])),
    dict(fid="G-04", title="the no-hand-patching policy is softened",
         target="CV", gates=["THE_INSPECTION_PACKAGE_FORBIDS_HAND_PATCHING"],
         patch=lambda: dict(CORRECTION_POLICY="Small fixes may be applied directly.")),
    dict(fid="G-05", title="the correction intake template is gutted",
         target="CV", gates=["THE_CORRECTION_TEMPLATE_HAS_ITS_FIELDS"],
         patch=lambda: dict(CORRECTION_INTAKE_FIELDS=["note"])),
    dict(fid="G-06", title="MMD production is recorded as started",
         target="SB", gates=["NO_MMD_REACT_SCORM_OR_LMS"],
         patch=lambda: dict(MMD_PRODUCTION_STARTED=1)),

    # ================= reporting =================
    dict(fid="R-01", title="the suite loses its identity", target="QA",
         gates=["SUITE_ID_DECLARED"], patch=lambda: dict(SUITE_ID="")),
    dict(fid="R-02", title="the suite adopts the storyboard suite identity", target="QA",
         gates=["SUITE_ID_DECLARED", "SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE"],
         patch=lambda: dict(SUITE_ID=QA.PRIOR_SUITE_ID)),
    dict(fid="R-03", title="the NOT_CHECKED list is emptied", target="QA",
         gates=["NOT_CHECKED_IS_PUBLISHED"], patch=lambda: dict(NOT_CHECKED=[])),
]


def _panel_without(marker):
    base = SE._state_panel

    def patched(slide, st, x, y, w, h):
        orig = SE.BB._p

        def filtered(tf, text, *a, **k):
            if marker in str(text):
                return None
            return orig(tf, text, *a, **k)
        SE.BB._p = filtered
        try:
            return base(slide, st, x, y, w, h)
        finally:
            SE.BB._p = orig
    return patched


def _panel_without_return():
    base = SE._state_panel

    def patched(slide, st, x, y, w, h):
        drop = st["return_behaviour_ms"]
        orig = SE.BB._p

        def filtered(tf, text, *a, **k):
            if str(text) == drop:
                return None
            return orig(tf, text, *a, **k)
        SE.BB._p = filtered
        try:
            return base(slide, st, x, y, w, h)
        finally:
            SE.BB._p = orig
    return patched


def _panel_without_diff():
    base = SE._state_panel

    def patched(slide, st, x, y, w, h):
        drop = st["differs_from_base_ms"]
        orig = SE.BB._p

        def filtered(tf, text, *a, **k):
            if str(text) == drop:
                return None
            return orig(tf, text, *a, **k)
        SE.BB._p = filtered
        try:
            return base(slide, st, x, y, w, h)
        finally:
            SE.BB._p = orig
    return patched


def _run_suite():
    return {r["gate_id"]: r["ok"] for r in QA.run()}


def _appendix_digest():
    p = os.path.join(CV.APPENDIX_DIR, CV.APPENDIX_NAME)
    if not os.path.exists(p):
        return None
    return hashlib.sha256(
        json.dumps(QA._appendix_texts(), ensure_ascii=False).encode()).hexdigest()


def run_fixture(f):
    tgt = TARGETS[f.get("target", "SM")]
    patch = f["patch"]()
    saved = {k: getattr(tgt, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(tgt, k, v)
        if f.get("rebuild"):
            SE.build_appendix()
        return _run_suite()
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(tgt, k, v)
        if f.get("rebuild"):
            SE.build_appendix()


def main():
    global _BASE_STATES, _BASE_MATRIX, _BASE_AUDIT, _BASE_ALIAS, _BASE_ORACLE, _BASE_PAGES
    _BASE_STATES = SM.states()
    _BASE_PAGES = CV.appendix_pages()
    _BASE_MATRIX = CV.matrix(True)
    _BASE_AUDIT = CV.source_row_audit()
    _BASE_ALIAS = CV.alias_map_report()
    _BASE_ORACLE = CV.oracle_audit()
    before = _appendix_digest()
    good = _run_suite()
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], title=f["title"],
                        target=f.get("target", "SM"),
                        rebuilds_appendix=bool(f.get("rebuild")),
                        designated_gates=f["gates"], detected=det, fired=fired,
                        note=res.get("__MSG__")))
    after = _appendix_digest()
    return dict(suite_id=QA.SUITE_ID,
                baseline_pass=sum(1 for v in good.values() if v),
                baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out),
                detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                appendix_rebuilt_clean=(before == after),
                rebuild_fixtures=len([r for r in out if r["rebuilds_appendix"]]),
                by_target={t: sum(1 for r in out if r["target"] == t)
                           for t in sorted({r["target"] for r in out})},
                fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if (r["missed"] or r["baseline_false_failures"]
                   or not r["appendix_rebuilt_clean"]) else 0)
