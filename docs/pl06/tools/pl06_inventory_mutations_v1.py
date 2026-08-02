# -*- coding: utf-8 -*-
"""Negative mutations for the PL06 inventory gates.

Each fixture injects one defect into the controlled data source in memory, runs the suite,
and requires the designated gate to fire. The patch is reverted in a `finally` before the
next fixture runs, so the committed data is never touched and no fixture artifact is written
to disk.

A fixture proves GATE SENSITIVITY only. It does not prove the inventory is correct — that is
what the evidence register is for.

    python3 docs/pl06/tools/pl06_inventory_mutations_v1.py
"""
import copy, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import pl06_inventory_data_v1 as D
import pl06_inventory_qa_v1 as QA
import pl06_emit_v1 as EMIT


def _units_patch(fn):
    """Return a patcher that deep-copies UNITS, applies fn, and installs it."""
    def apply():
        u = copy.deepcopy(D.UNITS)
        fn(u)
        return dict(UNITS=u)
    return apply


def _find(units, uid):
    return next(u for u in units if u["unit_id"] == uid)


# ------------------------------------------------------------------ fixtures
def _f_source_ref(u):
    _find(u, "K5-PL06-T04-B01")["source_reference"] = ""


def _f_dup_unit(u):
    u.append(copy.deepcopy(_find(u, "K5-PL06-T04-B01")))


def _f_dup_topik_bahagian(u):
    d = copy.deepcopy(_find(u, "K5-PL06-T03-B02"))
    d["unit_id"] = "K5-PL06-T03-B02-CLONE"
    u.append(d)


def _f_bad_readiness(u):
    _find(u, "K5-PL06-T04-B01")["readiness_status"] = "ALMOST_READY"


def _f_ready_but_blocked(u):
    t = _find(u, "K5-PL06-T04-B01")
    t["readiness_status"] = "READY"


def _f_unsupported_interaction_ready(u):
    t = _find(u, "K5-PL06-T04-B01")
    t["readiness_status"] = "READY_WITH_HOLDS"


def _f_no_rumusan_complete(u):
    t = _find(u, "K5-PL06-T04-B01")
    t["readiness_status"] = "READY"
    t["blocking_conditions"] = []
    t["interaction_pattern_candidate"] = "SOME_PATTERN"
    t["quiz_mcq_available"] = True
    t["quiz_mr_available"] = True
    t["lane"] = "LANE_A_EXISTING_SUPPORTED_PATTERN"


def _f_no_quiz_complete(u):
    t = _find(u, "K5-PL06-T04-B01")
    t["readiness_status"] = "READY"
    t["blocking_conditions"] = []
    t["interaction_pattern_candidate"] = "SOME_PATTERN"
    t["rumusan_available"] = True
    t["lane"] = "LANE_A_EXISTING_SUPPORTED_PATTERN"


def _f_authority_inflation(u):
    _find(u, "K5-PL06-T04-B01")["source_authority_class"] = "BARIAH_DIRECT_WRITTEN_CONFIRMATION"


def _f_invented_bahagian(u):
    # A numbered Bahagian whose evidence does not establish a boundary — the defect the gate
    # exists to catch. Injecting a number where the boundary map already attests one is not a
    # defect at all, which is why this fixture had to be rewritten at Stage 4.2F-A2.
    t = _find(u, "K5-PL06-T04-B01")
    t["source_attests"] = "TOPIK_EXISTENCE_AND_TITLE_ONLY"


def _f_existence_only_claims_content(u):
    _find(u, "K5-PL06-T04-B01")["source_rows_count"] = 12


def _f_content_without_source_document(u):
    _find(u, "K5-PL06-T04-B01")["rumusan_available"] = True


FIXTURES = [
    dict(fid="N-01", title="a unit loses its source reference",
         gates=["UNITS_WITHOUT_SOURCE_REFERENCE",
                "UNITS_WITHOUT_EVIDENCE_REF_IN_SOURCE_REFERENCE"],
         patch=_units_patch(_f_source_ref)),
    dict(fid="N-02", title="a unit id is duplicated",
         gates=["DUPLICATE_UNIT_IDS"], patch=_units_patch(_f_dup_unit)),
    dict(fid="N-03", title="a Topik/Bahagian combination is duplicated under a new unit id",
         gates=["DUPLICATE_TOPIK_BAHAGIAN_COMBINATIONS"],
         patch=_units_patch(_f_dup_topik_bahagian)),
    dict(fid="N-04", title="an invalid readiness value is introduced",
         gates=["INVALID_READINESS_VALUES"], patch=_units_patch(_f_bad_readiness)),
    dict(fid="N-05", title="a source-blocked unit is marked READY",
         gates=["READY_UNIT_WITH_UNRESOLVED_BLOCKING_SOURCE",
                "LANE_D_UNIT_NOT_MARKED_SOURCE_BLOCKED"],
         patch=_units_patch(_f_ready_but_blocked)),
    dict(fid="N-06", title="a unit whose interaction pattern is undeterminable is marked ready",
         gates=["UNSUPPORTED_INTERACTION_CLASSIFIED_READY"],
         patch=_units_patch(_f_unsupported_interaction_ready)),
    dict(fid="N-07", title="a unit with no Rumusan source is marked fully complete",
         gates=["UNIT_WITHOUT_RUMUSAN_MARKED_FULLY_COMPLETE"],
         patch=_units_patch(_f_no_rumusan_complete)),
    dict(fid="N-08", title="a unit with no quiz source is marked fully complete",
         gates=["UNIT_WITHOUT_QUIZ_SOURCE_MARKED_FULLY_COMPLETE"],
         patch=_units_patch(_f_no_quiz_complete)),
    dict(fid="N-09", title="a montage-attested unit claims direct Bariah authority",
         gates=["AUTHORITY_CLASS_INFLATION", "SOURCE_DERIVED_SUBJECT_LABELLED_BARIAH_DIRECT"],
         patch=_units_patch(_f_authority_inflation)),
    dict(fid="N-10", title="a Bahagian number is invented for a unit with no unit content",
         gates=["BAHAGIAN_NUMBERS_INVENTED"], patch=_units_patch(_f_invented_bahagian)),
    dict(fid="N-11", title="an existence-only unit claims source rows",
         gates=["EXISTENCE_ONLY_EVIDENCE_CLAIMING_CONTENT"],
         patch=_units_patch(_f_existence_only_claims_content)),
    dict(fid="N-12", title="a unit with no source document claims a Rumusan",
         gates=["UNIT_CLAIMING_CONTENT_WITHOUT_SOURCE_DOCUMENT"],
         patch=_units_patch(_f_content_without_source_document)),

    # ---- rule portability ----
    dict(fid="N-13", title="a B02-specific rule is promoted to PL06 global",
         gates=["B02_SPECIFIC_RULE_PROMOTED_GLOBALLY", "GLOBAL_RULE_WITH_NARROW_DESTINATION"],
         patch=lambda: dict(RULES=[
             dict(r, portability_class="PL06_GLOBAL_REUSABLE") if r["rule_id"] == "RP-205" else r
             for r in copy.deepcopy(D.RULES)])),
    dict(fid="N-14", title="a B02-specific rule is given a PL06-wide destination scope",
         gates=["B02_SPECIFIC_RULE_WITH_WIDE_DESTINATION"],
         patch=lambda: dict(RULES=[
             dict(r, destination_scope="ALL_PL06_UNITS") if r["rule_id"] == "RP-201" else r
             for r in copy.deepcopy(D.RULES)])),
    dict(fid="N-15", title="a mandatory B02-specific rule is deleted from the matrix",
         gates=["MANDATORY_B02_SPECIFIC_RULES_PRESENT"],
         patch=lambda: dict(RULES=[r for r in copy.deepcopy(D.RULES)
                                   if r["rule_id"] != "RP-206"])),
    dict(fid="N-16", title="a rule with no automated oracle drops its human-authority requirement",
         gates=["UNORACLED_RULE_WITHOUT_HUMAN_AUTHORITY"],
         patch=lambda: dict(RULES=[
             dict(r, human_authority_required="NONE") if r["rule_id"] == "RP-106" else r
             for r in copy.deepcopy(D.RULES)])),

    # ---- selection ----
    dict(fid="N-17", title="the selected proof unit is not in the inventory",
         gates=["SELECTED_PROOF_UNIT_PRESENT_IN_INVENTORY"],
         patch=lambda: dict(SELECTION=dict(D.SELECTION, selected_unit_id="K5-PL06-T09-B01"))),
    dict(fid="N-18", title="a blocked selection is declared unconditional",
         gates=["BLOCKED_SELECTION_DECLARED_UNCONDITIONAL", "SELECTION_STATUS_DECLARED"],
         patch=lambda: dict(SELECTION=dict(D.SELECTION, selection_is_unconditional=True,
                                           selection_status="SELECTED_READY"))),
    dict(fid="N-19", title="a blocked selection drops its preconditions",
         gates=["BLOCKED_SELECTION_WITHOUT_PRECONDITIONS"],
         patch=lambda: dict(SELECTION=dict(D.SELECTION, required_preconditions=[]))),
    dict(fid="N-20", title="B02 itself is selected as the first non-B02 proof",
         gates=["SELECTED_PROOF_UNIT_IS_NOT_B02"],
         patch=lambda: dict(SELECTION=dict(D.SELECTION,
                                           selected_unit_id="K5-PL06-T03-B02"))),
    dict(fid="N-21", title="a sourceless candidate is scored above zero on visual availability",
         gates=["SOURCELESS_CANDIDATE_SCORED_ON_CONTENT"],
         patch=lambda: dict(CANDIDATE_SCORES=[
             dict(c, scores=dict(c["scores"], visual_availability=4))
             if c["unit_id"] == "K5-PL06-T04-B01" else c
             for c in copy.deepcopy(D.CANDIDATE_SCORES)])),

    # ---- plan and stop conditions ----
    dict(fid="N-22", title="an execution-plan row names a unit absent from the inventory",
         gates=["EXECUTION_ORDER_UNIT_ABSENT_FROM_INVENTORY",
                "PLAN_ROWS_COVER_EVERY_REMAINING_UNIT"],
         patch=lambda: dict(PLAN_ROWS=copy.deepcopy(D.PLAN_ROWS) + [
             dict(D.PLAN_ROWS[-1], unit_id="K5-PL06-T99")])),
    dict(fid="N-23", title="a held unit is given an invented duration",
         gates=["PLAN_DURATION_WITHOUT_BASIS"],
         patch=lambda: dict(PLAN_ROWS=[
             dict(r, controlled_model="2h") if r["unit_id"] == "K5-PL06-T01-B01" else r
             for r in copy.deepcopy(D.PLAN_ROWS)])),
    dict(fid="N-24", title="a PowerPoint smoke duration is estimated",
         gates=["POWERPOINT_SMOKE_ESTIMATED_WITHOUT_EVIDENCE"],
         patch=lambda: dict(PLAN_ROWS=[
             dict(r, powerpoint_smoke="15m") if r["unit_id"] == "K5-PL06-T04-B01" else r
             for r in copy.deepcopy(D.PLAN_ROWS)])),
    dict(fid="N-25", title="a global open item is scoped to block an unrelated unit",
         gates=["GLOBAL_ITEM_BLOCKING_UNRELATED_UNIT"],
         patch=lambda: dict(STOP_CONDITIONS=[
             dict(c, scope="BLOCKS_THIS_UNIT") if c["id"] == "STOP-009" else c
             for c in copy.deepcopy(D.STOP_CONDITIONS)])),
    dict(fid="N-26", title="a unit names a blocker that is in no stop register",
         gates=["UNIT_BLOCKER_NOT_IN_STOP_REGISTER"],
         patch=_units_patch(lambda u: _find(u, "K5-PL06-T04-B01")["blocking_conditions"].append(
             "WAITING_FOR_SOMETHING"))),

    # ---- approval authority ----
    dict(fid="N-27", title="the call approval is reclassified as a direct Bariah screenshot",
         gates=["CALL_APPROVAL_AUTHORITY_CLASS", "CALL_APPROVAL_NOT_CLASSIFIED_AS_DIRECT"],
         patch=lambda: dict(APPROVAL_RECORD=dict(
             D.APPROVAL_RECORD, authority_class="BARIAH_DIRECT_SCREENSHOT"))),
    dict(fid="N-28", title="the call approval is marked as written confirmation received",
         gates=["CALL_APPROVAL_WRITTEN_CONFIRMATION_PENDING"],
         patch=lambda: dict(APPROVAL_RECORD=dict(
             D.APPROVAL_RECORD, written_confirmation="RECEIVED"))),
    dict(fid="N-29", title="the call approval is read as authorising canonical freeze",
         gates=["CALL_APPROVAL_DOES_NOT_AUTHORISE_FREEZE"],
         patch=lambda: dict(APPROVAL_RECORD=dict(
             D.APPROVAL_RECORD,
             may_not_authorise=["MMD readiness", "production release"]))),

    # ---- verdict and artifact agreement ----
    dict(fid="N-30", title="a forbidden verdict is declared",
         gates=["VERDICT_IS_ALLOWED", "FORBIDDEN_VERDICT_CLAIMED"],
         patch=lambda: dict(VERDICT="PL06_STORYBOARDS_COMPLETE")),
    dict(fid="N-31", title="a COMPLETE verdict is declared while units are source-blocked",
         gates=["COMPLETE_VERDICT_WITH_UNRESOLVED_UNITS"],
         patch=lambda: dict(
             VERDICT="PL06_SCALE_OUT_INVENTORY_COMPLETE_READY_FOR_FIRST_NON_B02_PROOF")),
    dict(fid="N-32", title="the CSV diverges from the controlled data source",
         gates=["MARKDOWN_CSV_INVENTORY_DIVERGENCE", "EMITTED_DELIVERABLES_STALE"],
         patch=_units_patch(lambda u: _find(u, "K5-PL06-T04-B01").update(
             topik_title="Penjagaan Dan Penyelenggaraan Tapak"))),
]


# ---------------------------------------------------------------- 4.2F-A2 fixtures
def _f_unit_count(u):
    u.pop()                                              # drop a lesson unit


def _f_b02_title_regression(u):
    _find(u, "K5-PL06-T03-B02")["bahagian_title"] = "Komponen Landskap"


def _f_b03_placeholder(u):
    t = _find(u, "K5-PL06-T03-B03")
    t["unit_id"] = "K5-PL06-T03-BNEXT"
    t["bahagian_number"] = None
    t["bahagian_title"] = None


def _f_t04_pages(u):
    t = _find(u, "K5-PL06-T04-B01")
    t["source_page_range"] = "modul ms 276-284 / rendered PDF 294-302"


FIXTURES += [
    # ---- boundary and topology ----
    dict(fid="N-33", title="a lesson unit is dropped from the inventory",
         gates=["INVENTORY_UNIT_COUNT", "PL06_TOPOLOGY", "REMAINING_UNITS"],
         patch=_units_patch(_f_unit_count)),
    dict(fid="N-34", title="B02's bahagian title regresses to the Topik title",
         gates=["B02_BAHAGIAN_TITLE", "B02_BAHAGIAN_TITLE_IS_NOT_TOPIK_TITLE",
                "UNITS_WHOSE_BAHAGIAN_TITLE_EQUALS_TOPIK_TITLE"],
         patch=_units_patch(_f_b02_title_regression)),
    dict(fid="N-35", title="T03-B03 reverts to the unresolved BNEXT placeholder",
         gates=["UNRESOLVED_PLACEHOLDER_UNITS", "T03_B03_PRESENT", "T03_B03_TITLE",
                "UNITS_WITH_NULL_BAHAGIAN_NUMBER"],
         patch=_units_patch(_f_b03_placeholder)),
    dict(fid="N-36", title="the T04 page range is widened past its stop anchor",
         gates=["T04_MODULE_PAGE_RANGE", "T03_B03_PAGE_RANGE"],
         patch=lambda: dict(BOUNDARY_ROWS=[
             dict(r, module_page_range="276-284") if r["unit_id"] == "K5-PL06-T04-B01" else r
             for r in copy.deepcopy(D.BOUNDARY_ROWS)])),
    dict(fid="N-37", title="the T04 stop anchor is changed",
         gates=["T04_END_BEFORE_ANCHOR"],
         patch=lambda: dict(BOUNDARY_ROWS=[
             dict(r, end_before="6.0 PERLINDUNGAN") if r["unit_id"] == "K5-PL06-T04-B01" else r
             for r in copy.deepcopy(D.BOUNDARY_ROWS)])),
    dict(fid="N-38", title="the T04 boundary is silently marked shared",
         gates=["T04_BOUNDARY_IS_CLEAN"],
         patch=lambda: dict(BOUNDARY_ROWS=[
             dict(r, shared_start=True) if r["unit_id"] == "K5-PL06-T04-B01" else r
             for r in copy.deepcopy(D.BOUNDARY_ROWS)])),
    dict(fid="N-39", title="a shared boundary page is dropped from the register",
         gates=["SHARED_BOUNDARY_PAGES"],
         patch=lambda: dict(SHARED_BOUNDARY_PAGES=[181, 188, 215, 237, 250])),
    dict(fid="N-40", title="the topology is altered without altering the map",
         gates=["PL06_TOPOLOGY"],
         patch=lambda: dict(TOPOLOGY={1: 3, 2: 2, 3: 4, 4: 2, 5: 1, 6: 1, 7: 1})),
    dict(fid="N-41", title="a second unit claims to be the completed baseline",
         gates=["COMPLETED_UNITS", "REMAINING_UNITS"],
         patch=_units_patch(lambda u: _find(u, "K5-PL06-T04-B01").update(
             unit_scope="DELIVERED_BASELINE"))),

    # ---- custody and ingest ----
    dict(fid="N-42", title="the primary DOCX is declared tracked in Git",
         gates=["PRIMARY_DOCX_NOT_TRACKED"],
         patch=lambda: dict(EXTERNAL_CUSTODY=dict(
             D.EXTERNAL_CUSTODY,
             primary_docx=dict(D.EXTERNAL_CUSTODY["primary_docx"], tracked_in_git=True)))),
    dict(fid="N-43", title="shared team custody is claimed before a Drive location exists",
         gates=["SHARED_TEAM_CUSTODY_NOT_CLAIMED", "FREEZE_PACKAGE_CUSTODY_EXPLICIT"],
         patch=lambda: dict(EXTERNAL_CUSTODY=dict(
             D.EXTERNAL_CUSTODY,
             freeze_package=dict(D.EXTERNAL_CUSTODY["freeze_package"],
                                 shared_team_custody_claimed=True,
                                 custody="SHARED_TEAM_CUSTODY")))),
    dict(fid="N-44", title="the rendered PDF is reclassified as separately tracked",
         gates=["RENDERED_PDF_NOT_TRACKED_SEPARATELY", "RENDERED_PDF_CLASSIFICATION"],
         patch=lambda: dict(EXTERNAL_CUSTODY=dict(
             D.EXTERNAL_CUSTODY,
             rendered_pdf=dict(D.EXTERNAL_CUSTODY["rendered_pdf"], tracked_in_git=True,
                               classification="TRACKED_DERIVED_ARTIFACT")))),
    dict(fid="N-45", title="the primary DOCX identity is altered",
         gates=["PRIMARY_DOCX_IDENTITY_RECORDED"],
         patch=lambda: dict(EXTERNAL_CUSTODY=dict(
             D.EXTERNAL_CUSTODY,
             primary_docx=dict(D.EXTERNAL_CUSTODY["primary_docx"], bytes=16832860)))),
    dict(fid="N-46", title="an ingested file is dropped from the verification set",
         gates=["INGESTED_FILES_EVALUATED"],
         patch=lambda: dict(INGESTED_FILES=list(D.INGESTED_FILES)[:-1])),
    dict(fid="N-47", title="a forbidden-tracked pattern is removed from the guard list",
         gates=["FORBIDDEN_TRACKED_PATTERNS_COMPLETE"],
         patch=lambda: dict(FORBIDDEN_TRACKED_PATTERNS=[
             t for t in D.FORBIDDEN_TRACKED_PATTERNS if t[0] != "FULL_DOCX"])),

    # ---- grouping authority ----
    dict(fid="N-48", title="the grouping authority is upgraded to canonical",
         gates=["GROUPING_AUTHORITY_STATUS_EXPLICIT", "GROUPING_AUTHORITY_NOT_CLAIMED_CANONICAL"],
         patch=lambda: dict(GROUPING_AUTHORITY=dict(
             D.GROUPING_AUTHORITY, status="FROZEN_CANONICAL",
             canonical_authority_claimed=True))),
    dict(fid="N-49", title="the grouping authority is made a blocker for extraction",
         gates=["GROUPING_AUTHORITY_DOES_NOT_BLOCK_EXTRACTION"],
         patch=lambda: dict(GROUPING_AUTHORITY=dict(
             D.GROUPING_AUTHORITY, blocks_extraction=True))),

    # ---- stop-condition discipline ----
    dict(fid="N-50", title="a third stop condition is marked resolved by the source ingest",
         gates=["RESOLVED_STOP_CONDITIONS"],
         patch=lambda: dict(STOP_CONDITIONS=[
             dict(c, status="RESOLVED") if c["id"] == "STOP-006" else c
             for c in copy.deepcopy(D.STOP_CONDITIONS)])),
    dict(fid="N-51", title="a resolved stop condition keeps units attached to it",
         gates=["RESOLVED_STOP_WITH_UNITS_STILL_ATTACHED"],
         patch=lambda: dict(STOP_CONDITIONS=[
             dict(c, applies_to=["K5-PL06-T04-B01"]) if c["id"] == "STOP-001" else c
             for c in copy.deepcopy(D.STOP_CONDITIONS)])),
    dict(fid="N-52", title="an invalid stop status is introduced",
         gates=["INVALID_STOP_STATUSES"],
         patch=lambda: dict(STOP_CONDITIONS=[
             dict(c, status="PARTIALLY_RESOLVED") if c["id"] == "STOP-003" else c
             for c in copy.deepcopy(D.STOP_CONDITIONS)])),

    # ---- verdict ----
    dict(fid="N-53", title="the ingest-complete verdict is claimed while source authority is open",
         gates=["INGEST_COMPLETE_VERDICT_WITH_UNRESOLVED_SOURCE_AUTHORITY"],
         patch=_units_patch(lambda u: _find(u, "K5-PL06-T04-B01").update(
             readiness_status="SOURCE_AUTHORITY_UNRESOLVED"))),
    dict(fid="N-54", title="the selection is declared ready rather than conditional",
         gates=["SELECTION_STATUS_DECLARED", "SELECTION_STATUS_VALUE"],
         patch=lambda: dict(SELECTION=dict(D.SELECTION,
                                           selection_status="SELECTED_READY"))),
]


def run_fixture(f):
    patch = f["patch"]()
    saved = {k: getattr(D, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(D, k, v)
        return {r["gate_id"]: r["ok"] for r in QA.run()}
    except Exception as exc:                       # a fixture may break a reader outright
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(D, k, v)


def main():
    good = {r["gate_id"]: r["ok"] for r in QA.run()}
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        detected = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<reader exception>"] if "__EXCEPTION__" in res else [])
        newly = [g for g, ok in res.items() if not ok and good.get(g, True)]
        out.append(dict(fixture_id=f["fid"], title=f["title"], designated_gates=f["gates"],
                        detected=detected, fired=fired, total_newly_failing=len(newly)))
    return dict(baseline_pass=sum(1 for v in good.values() if v), baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out), detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if r["missed"] or r["baseline_false_failures"] else 0)
