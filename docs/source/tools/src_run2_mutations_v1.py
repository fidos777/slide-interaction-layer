# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-D — only the paths this run introduced.

    SUITE_ID = STAGE_4_2F_D_RELEASE_FACTS_QA_v1
    python3 docs/source/tools/src_run2_mutations_v1.py

No historical fixture is refactored and no historical gate is touched. The Stage 4.2F-C
fixtures keep their own file, their own suite and their own totals.

The defects attacked here are the ones this run actually created the opportunity for:

  * a package described without being read, or a read count quietly inflated;
  * a module code defaulting to M01 again, so the queue and the K3 model name the same
    unit two different ways;
  * a question count asserted uniform when the sources are not;
  * PL03's marking rubric passed off as a model answer;
  * the K5 assessment rule leaking into K3;
  * connector-read text counted as extracted rows;
  * a connector-located record promoted to immediately executable;
  * the retired 97.8 percent metric creeping back as a live number;
  * the frozen boundary map losing or gaining a unit without the hash noticing.
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
DOCS = os.path.dirname(SRC_DIR)
PL06 = os.path.join(DOCS, "pl06")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(PL06, "tools"))
import src_authority_v1 as A       # noqa: E402
import src_k3_v1 as K3             # noqa: E402
import src_run2_v1 as R2           # noqa: E402
import src_run2_qa_v1 as QA        # noqa: E402
import pl06_extract_rest_v1 as RE  # noqa: E402
import src_historical_freeze_v1 as FREEZE     # noqa: E402

TARGETS = {"K3": K3, "R2": R2, "RE": RE, "A": A, "QA": QA}

_BASE_INV = _BASE_MODELS = _BASE_QUEUE = None


def _inv(fn):
    """Patch k3_inventory's return value, leaving the rest of the module alone."""
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_INV)
            fn(d)
            return d
        return dict(k3_inventory=patched)
    return apply


def _models(fn):
    def apply():
        def patched():
            m = copy.deepcopy(_BASE_MODELS)
            fn(m)
            return m
        return dict(k3_models=patched)
    return apply


def _queue(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_QUEUE)
            fn(d)
            return d
        return dict(queue_summary=patched)
    return apply


def _row(q, uid):
    return next(r for r in q["rows"] if r["unit_or_candidate_id"] == uid)


FIXTURES = [
    # ---------------- source existence ----------------
    dict(fid="DX-01", title="a K3 package is dropped from the inventory", target="K3",
         gates=["K3_PACKAGE_COUNT_MATCHES_THE_LITERAL"],
         patch=_inv(lambda d: d.update(pdfs=8))),
    dict(fid="DX-02", title="a package is described without being read", target="K3",
         gates=["EVERY_K3_PACKAGE_IS_READ_IN_FULL"],
         patch=_inv(lambda d: d.update(identified_not_read=1))),
    dict(fid="DX-03", title="a K3 row claims a local binary it does not have",
         target="K3", gates=["NO_K3_PACKAGE_CLAIMS_A_LOCAL_BINARY"],
         patch=_inv(lambda d: d["rows"][0].update(binary_local=True))),
    dict(fid="DX-04", title="a K2 candidate is promoted to a production unit",
         target="R2", gates=["NO_K2_ROW_IS_A_CONFIRMED_PRODUCTION_UNIT"],
         patch=_queue(lambda q: next(r for r in q["rows"] if r["course"] == "K2").update(
             record_type="CONFIRMED_PRODUCTION_UNIT"))),
    dict(fid="DX-05", title="an unqualified absence status comes back", target="R2",
         gates=["NO_ROW_USES_AN_UNQUALIFIED_ABSENCE_STATUS"],
         patch=_queue(lambda q: next(r for r in q["rows"] if r["course"] == "K2").update(
             extraction_status="SOURCE_MISSING"))),

    # ---------------- page references ----------------
    dict(fid="DP-01", title="PL07's page count is inflated", target="K3",
         gates=["K3_PL07_PAGE_COUNT", "K3_TOTAL_PAGES_MATCHES_THE_STANDALONE_LITERAL",
                "K3_TOTAL_PAGES_AGREES_WITH_THE_SUM_OF_THE_LITERALS"],
         patch=_inv(lambda d: [r.update(pages=50) for r in d["rows"]
                               if r["pl"] == "PL07"])),
    dict(fid="DP-02", title="the page total is typed rather than summed", target="K3",
         gates=["K3_TOTAL_PAGES_MATCHES_THE_STANDALONE_LITERAL",
                "K3_TOTAL_PAGES_AGREES_WITH_THE_SUM_OF_THE_LITERALS"],
         patch=_inv(lambda d: d.update(total_source_pages=200))),
    dict(fid="DP-03", title="PL08's short package is given a sibling's length",
         target="K3", gates=["K3_PL08_PAGE_COUNT"],
         patch=_inv(lambda d: [r.update(pages=28) for r in d["rows"]
                               if r["pl"] == "PL08"])),
    dict(fid="DP-04", title="T04 rows stop accounting for themselves", target="R2",
         gates=["T04_ROWS_ACCOUNT_FOR_THEMSELVES"],
         patch=lambda: dict(t04_page_reconciliation=lambda: dict(
             R2.t04_page_reconciliation(), rows_unresolved=0))),
    dict(fid="DP-05", title="T04 is quietly scheduled for regeneration", target="R2",
         gates=["T04_PAGE_RECONCILIATION_STILL_SAYS_DO_NOT_REGENERATE"],
         patch=lambda: dict(t04_page_reconciliation=lambda: dict(
             R2.t04_page_reconciliation(),
             regeneration_decision=dict(regenerate=True, reason="")))),
    dict(fid="DP-06", title="the T04 mismatch count is massaged downward", target="R2",
         gates=["T04_MISMATCH_COUNT_UNCHANGED_BY_THIS_RUN"],
         patch=lambda: dict(t04_page_reconciliation=lambda: dict(
             R2.t04_page_reconciliation(), mismatches=0))),

    # ---------------- unit boundaries ----------------
    dict(fid="DB-01", title="a unit is added to the remaining list out of thin air",
         target="RE",
         gates=["REMAINING_PLUS_REPRESENTED_ACCOUNTS_FOR_EVERY_FROZEN_UNIT",
                "REMAINING_UNITS_EQUAL_FROZEN_MAP_MINUS_THE_REPRESENTED_LITERAL",
                "REMAINING_PL06_UNIT_COUNT_IS_NOT_AN_ASSUMED_8_10_OR_12"],
         patch=lambda: dict(remaining_units=lambda: RE.remaining_units()
                            + [dict(unit_id="K5-PL06-T09-B01")])),
    dict(fid="DB-02", title="a unit is both remaining and already represented",
         target="RE", gates=["REMAINING_UNITS_EQUAL_FROZEN_MAP_MINUS_THE_REPRESENTED_LITERAL",
                             "THE_REPRESENTED_SET_MATCHES_THE_HAND_TYPED_LITERAL"],
         patch=lambda: dict(ALREADY_REPRESENTED=dict(
             RE.ALREADY_REPRESENTED, **{"K5-PL06-T01-B01": "double counted"}))),
    dict(fid="DB-03", title="the represented set shrinks so the remainder looks bigger",
         target="RE",
         gates=["REMAINING_PLUS_REPRESENTED_ACCOUNTS_FOR_EVERY_FROZEN_UNIT",
                "REMAINING_UNITS_EQUAL_FROZEN_MAP_MINUS_THE_REPRESENTED_LITERAL",
                "REMAINING_PL06_UNIT_COUNT_IS_NOT_AN_ASSUMED_8_10_OR_12"],
         patch=lambda: dict(ALREADY_REPRESENTED={
             k: v for k, v in list(RE.ALREADY_REPRESENTED.items())[:5]})),

    # ---------------- unit counts and identity ----------------
    dict(fid="DC-01", title="a K3 model goes missing", target="K3",
         gates=["K3_MODEL_COUNT_EQUALS_PACKAGES_READ",
                "THE_QUEUE_AND_THE_K3_MODEL_NAME_EVERY_UNIT_THE_SAME_WAY"],
         patch=_models(lambda m: m.pop())),
    dict(fid="DC-02", title="every K3 unit is stamped M01 again", target="K3",
         gates=["EVERY_K3_MODULE_CODE_MATCHES_ITS_SOURCE_FRONT_MATTER",
                "K3_MODULE_COUNT_MATCHES_THE_LITERAL"],
         patch=_inv(lambda d: [r.update(module_code="M01") for r in d["rows"]])),
    dict(fid="DC-03", title="one package's module code drifts from its front matter",
         target="K3", gates=["EVERY_K3_MODULE_CODE_MATCHES_ITS_SOURCE_FRONT_MATTER"],
         patch=_inv(lambda d: [r.update(module_code="M02") for r in d["rows"]
                               if r["pl"] == "PL09"])),
    dict(fid="DC-04", title="the queue names a K3 unit differently from the model",
         target="R2", gates=["NO_K3_UNIT_ID_IS_STILL_STAMPED_M01_BY_DEFAULT",
                             "THE_QUEUE_AND_THE_K3_MODEL_NAME_EVERY_UNIT_THE_SAME_WAY"],
         patch=_queue(lambda q: _row(q, "K3-M06-PL09").update(
             unit_or_candidate_id="K3-M01-PL09"))),
    dict(fid="DC-05", title="the module count is claimed without the codes agreeing",
         target="K3", gates=["K3_MODULE_COUNT_MATCHES_THE_LITERAL"],
         patch=_inv(lambda d: d.update(modules_evidenced=["M01"]))),

    # ---------------- K3 assessment composition ----------------
    dict(fid="DA-01", title="a K3 model resolves assessment on its own", target="K3",
         gates=["EVERY_K3_MODEL_DEFERS_ASSESSMENT_TO_THE_COURSE_RULE"],
         patch=_models(lambda m: m[0]["source_assessment"].update(
             cls="COURSE_RULE_ALREADY_APPROVED"))),
    dict(fid="DA-02", title="the K5 rule is applied to K3", target="K3",
         gates=["THE_K5_RULE_IS_NOT_APPLIED_TO_K3"],
         patch=_inv(lambda d: d["k5_rule_not_applied"].update(applied_to_k3=True))),
    dict(fid="DA-03", title="a source answer key is marked approved", target="K3",
         gates=["NO_K3_ANSWER_KEY_IS_MARKED_APPROVED"],
         patch=_models(lambda m: m[0]["source_assessment"].update(
             key_status="BARIAH_APPROVED"))),
    dict(fid="DA-04", title="PL01's three questions are rounded up to five", target="K3",
         gates=["EVERY_K3_QUESTION_COUNT_MATCHES_ITS_SOURCE",
                "K3_TOTAL_QUESTIONS_MATCHES_THE_LITERAL"],
         patch=_inv(lambda d: [r.update(latihan_questions=5) for r in d["rows"]
                               if r["pl"] == "PL01"])),
    dict(fid="DA-05", title="the question count is asserted uniform", target="K3",
         gates=["SHAPE_AND_PACKAGE_QUESTION_COUNTS_AGREE"],
         patch=lambda: dict(SKEMA_SHAPES={
             pl: dict(s, questions=5) for pl, s in K3.SKEMA_SHAPES.items()})),
    dict(fid="DA-06", title="PL03's marking rubric is passed off as a model answer",
         target="K3", gates=["ONLY_PL03_CARRIES_MARK_ALLOCATIONS"],
         patch=lambda: dict(SKEMA_SHAPES=dict(
             K3.SKEMA_SHAPES,
             PL03=dict(K3.SKEMA_SHAPES["PL03"], carries_marks=False)))),
    dict(fid="DA-07", title="a second package is credited with marks it does not carry",
         target="K3", gates=["ONLY_PL03_CARRIES_MARK_ALLOCATIONS"],
         patch=lambda: dict(SKEMA_SHAPES=dict(
             K3.SKEMA_SHAPES,
             PL05=dict(K3.SKEMA_SHAPES["PL05"], carries_marks=True)))),
    dict(fid="DA-08", title="CAIR quietly picks an option for Bariah", target="K3",
         gates=["THE_DECISION_OFFERS_FOUR_OPTIONS_AND_NO_CAIR_PICK"],
         patch=lambda: dict(K3_COURSE_DECISION=dict(K3.K3_COURSE_DECISION,
                                                    cair_recommendation="B"))),
    dict(fid="DA-09", title="an option is dropped from the decision", target="K3",
         gates=["THE_DECISION_OFFERS_FOUR_OPTIONS_AND_NO_CAIR_PICK"],
         patch=lambda: dict(K3_COURSE_DECISION=dict(
             K3.K3_COURSE_DECISION,
             options=K3.K3_COURSE_DECISION["options"][:3]))),
    dict(fid="DA-10", title="the decision starts blocking source reading", target="K3",
         gates=["THE_DECISION_DOES_NOT_BLOCK_SOURCE_OR_VISUAL_WORK"],
         patch=lambda: dict(K3_COURSE_DECISION=dict(
             K3.K3_COURSE_DECISION,
             does_not_block=["visual modelling", "screen modelling"]))),

    # ---------------- queue readiness ----------------
    dict(fid="DQ-01", title="a connector-located record becomes immediately executable",
         target="R2", gates=["NO_CONNECTOR_ONLY_ROW_IS_IMMEDIATELY_EXECUTABLE",
                             "NO_IMMEDIATELY_EXECUTABLE_UNIT_LACKS_A_READABLE_BINARY",
                             "IMMEDIATELY_EXECUTABLE_MATCHES_THE_LITERAL"],
         patch=_queue(lambda q: (
             _row(q, "K2-MONOLITH-UNRESOLVED").update(immediately_executable=True),
             q["counts"].update(
                 immediately_executable_units=q["counts"]
                 ["immediately_executable_units"] + 1)))),
    dict(fid="DQ-02", title="the headline count is inflated", target="R2",
         gates=["IMMEDIATELY_EXECUTABLE_MATCHES_THE_LITERAL"],
         patch=_queue(lambda q: q["counts"].update(immediately_executable_units=22))),
    dict(fid="DQ-03", title="something claims it is ready to emit PPTX", target="R2",
         gates=["NOTHING_IS_READY_TO_EMIT_PPTX_YET"],
         patch=_queue(lambda q: q["counts"].update(ready_to_emit_units=4))),
    dict(fid="DQ-04", title="connector-read text is counted as extracted rows",
         target="R2", gates=["EXTRACTED_COUNT_EQUALS_THE_FROZEN_PL06_UNIT_COUNT"],
         patch=_queue(lambda q: q["counts"].update(extracted_units=23))),
    dict(fid="DQ-05", title="the read and extracted counters are merged again",
         target="R2", gates=["EXTRACTED_IS_NOT_CONFLATED_WITH_CONNECTOR_READ",
                             "SOURCE_CONTENT_READ_COUNT_EQUALS_THE_K3_PACKAGE_COUNT"],
         patch=_queue(lambda q: q["counts"].update(source_content_read_units=0))),
    dict(fid="DQ-06", title="the record types stop partitioning the queue", target="R2",
         gates=["RECORD_TYPES_PARTITION_THE_QUEUE_EXACTLY"],
         patch=_queue(lambda q: q["counts"].update(candidate_structures=30))),
    dict(fid="DQ-07", title="every unresolved row is relabelled a candidate unit",
         target="R2", gates=["NOT_EVERY_UNRESOLVED_ROW_IS_CALLED_A_CANDIDATE_UNIT",
                             "RECORD_TYPES_PARTITION_THE_QUEUE_EXACTLY"],
         patch=_queue(lambda q: q["counts"].update(
             candidate_structures=q["counts"]["total_rows"]))),
    dict(fid="DQ-08", title="the retired percentage returns as a live metric",
         target="R2",
         gates=["THE_RETIRED_97_8_PERCENT_METRIC_APPEARS_ONLY_IN_ITS_"
                "RETIREMENT_RECORD",
                "NO_LIVE_COUNT_OR_HEADLINE_CARRIES_A_TYPED_PERCENTAGE"],
         patch=_queue(lambda q: q["counts"].update(source_ready="97.8 percent"))),
    dict(fid="DQ-09", title="a row claims PRODUCTION_APPROVED", target="R2",
         gates=["NO_ROW_CLAIMS_PRODUCTION_APPROVED_OR_CANONICAL_FREEZE"],
         patch=_queue(lambda q: _row(q, "K5-PL06-T04-B01").update(
             model_status="PRODUCTION_APPROVED"))),
    dict(fid="DQ-10", title="a row claims CANONICAL_FREEZE", target="R2",
         gates=["NO_ROW_CLAIMS_PRODUCTION_APPROVED_OR_CANONICAL_FREEZE"],
         patch=_queue(lambda q: _row(q, "K5-PL06-T04-B01").update(
             extraction_status="CANONICAL_FREEZE"))),

    # ---------------- extracted-row membership ----------------
    dict(fid="DM-01", title="an extracted row names a unit the frozen map does not have",
         target="R2", gates=["EVERY_EXTRACTED_QUEUE_ROW_IS_A_FROZEN_MAP_UNIT"],
         patch=_queue(lambda q: _row(q, "K5-PL06-T04-B01").update(
             unit_or_candidate_id="K5-PL06-T99-B01"))),
    dict(fid="DM-02", title="a frozen-map unit loses its extracted status", target="R2",
         gates=["EVERY_FROZEN_MAP_UNIT_APPEARS_AS_AN_EXTRACTED_QUEUE_ROW",
                "EXTRACTED_COUNT_EQUALS_THE_FROZEN_PL06_UNIT_COUNT"],
         patch=_queue(lambda q: _row(q, "K5-PL06-T01-B01").update(
             extraction_status="SOURCE_CONTENT_READ"))),
    dict(fid="DM-03", title="a K3 row claims rows were extracted from it", target="R2",
         gates=["NO_K3_ROW_CLAIMS_EXTRACTED_STATUS",
                "EXTRACTED_COUNT_EQUALS_THE_FROZEN_PL06_UNIT_COUNT"],
         patch=_queue(lambda q: _row(q, "K3-M04-PL06").update(
             extraction_status="EXTRACTED"))),

    # ---------------- suite accounting ----------------
    dict(fid="DS-01", title="the suite adopts a sibling suite's identity", target="QA",
         gates=["SUITE_ID_DECLARED", "SUITE_ID_IS_NOT_ANY_SIBLING_SUITE"],
         patch=lambda: dict(SUITE_ID="PROJECT_SOURCE_CUSTODY_QA_v1")),
    dict(fid="DS-02", title="oracle separation is claimed rather than deferred",
         target="QA", gates=["ORACLE_SEPARATION_IS_RECORDED_AS_DEFERRED"],
         patch=lambda: dict(ORACLE_SEPARATION_STRUCTURAL="ENFORCED")),
]


def _run_suite():
    return {r["gate_id"]: r["ok"] for r in QA.run()}


def run_fixture(f):
    tgt = TARGETS[f["target"]]
    patch = dict(f["patch"]())
    saved = {k: getattr(tgt, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(tgt, k, v)
        return _run_suite()
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": f"{type(exc).__name__}: {exc}"}
    finally:
        for k, v in saved.items():
            setattr(tgt, k, v)


def main():
    global _BASE_INV, _BASE_MODELS, _BASE_QUEUE
    _BASE_INV = K3.k3_inventory()
    _BASE_MODELS = K3.k3_models()
    _BASE_QUEUE = R2.queue_summary()
    good = _run_suite()
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], title=f["title"], target=f["target"],
                        designated_gates=f["gates"], detected=det, fired=fired,
                        note=res.get("__MSG__")))
    return dict(suite_id=QA.SUITE_ID,
                baseline_pass=sum(1 for v in good.values() if v),
                baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out),
                detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                by_target={t: sum(1 for r in out if r["target"] == t)
                           for t in sorted({r["target"] for r in out})},
                fixtures=out)


def emit_report(r):
    # See src_historical_freeze_v1: this path is Stage 4.2F-D's frozen evidence.
    FREEZE.guard("STAGE_4_2F_D_MUTATION_REPORT_v1.md")
    md = ["<!-- GENERATED by docs/source/tools/src_run2_mutations_v1.py -->", "",
          "# Mutation report — Stage 4.2F-D release facts", "", "```",
          f"SUITE_ID  = {r['suite_id']}",
          f"FIXTURES  = {r['fixture_count']}",
          f"DETECTED  = {r['detected']}",
          f"MISSED    = {len(r['missed'])}",
          f"BASELINE  = {r['baseline_pass']}/{r['baseline_total']}", "```", "",
          "Only the paths this run introduced are attacked. The Stage 4.2F-C fixtures "
          "keep their own file, their own suite and their own totals; nothing here is "
          "added to them.", "",
          "| fixture | what it breaks | target | gates that fired |", "|---|---|---|---|"]
    md += [f"| `{f['fixture_id']}` | {f['title']} | {f['target']} | "
           f"{', '.join('`' + g + '`' for g in f['fired']) or '**NONE — MISSED**'} |"
           for f in r["fixtures"]]
    md += [""]
    path = os.path.join(SRC_DIR, "STAGE_4_2F_D_MUTATION_REPORT_v1.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    return path


if __name__ == "__main__":
    r = main()
    print(json.dumps({k: v for k, v in r.items() if k != "fixtures"},
                     ensure_ascii=False, indent=1))
    for f in r["fixtures"]:
        if not f["detected"]:
            print("MISS", f["fixture_id"], "|", f["title"], "|", f["designated_gates"],
                  "|", f["note"])
    try:
        print("report   :", emit_report(r))
    except FREEZE.HistoricalReportFrozen as exc:
        # Expected once Stage 4.2F-D closed. The fixtures still run and still report;
        # only the frozen report is protected from being rewritten.
        print("report   : NOT REWRITTEN —", exc)
    sys.exit(1 if (r["missed"] or r["baseline_false_failures"]) else 0)
