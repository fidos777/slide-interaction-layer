# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-E — K2 custody, conflict, hierarchy and queue.

    SUITE_ID = STAGE_4_2F_E_K2_QA_v1
    python3 docs/source/tools/src_k2_mutations_v1.py

No historical fixture is refactored and no sibling suite is touched.

The defect this run could most easily have committed is a single one, in many costumes:
CLAIMING THE BINARY WAS SEEN. The brief said the file was local; it was not. Every
fixture below is some version of a record quietly asserting more than the evidence
supports — a status upgraded because a run expected it to upgrade, an unknown that becomes
a number, a truncated read described as complete, a candidate promoted to a unit, a
typographical slip escalated into a decision for Bariah.
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
DOCS = os.path.dirname(SRC_DIR)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(DOCS, "pl06", "tools"))
import src_k2_v1 as K2      # noqa: E402
import src_k2_qa_v1 as QA   # noqa: E402
import src_run2_v1 as R2    # noqa: E402

TARGETS = {"K2": K2, "R2": R2, "QA": QA}

_BASE_CUSTODY = _BASE_HIER = _BASE_QUEUE = None


def _custody(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_CUSTODY)
            fn(d)
            return d
        return dict(custody=patched)
    return apply


def _hier(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_HIER)
            fn(d)
            return d
        return dict(hierarchy=patched)
    return apply


def _queue(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_QUEUE)
            fn(d)
            return d
        return dict(queue_summary=patched)
    return apply


def _k2rows(q):
    return [r for r in q["rows"] if r["course"] == "K2"]


FIXTURES = [
    # ---------------- the central defect: claiming the binary ----------------
    dict(fid="EK-01", title="the status is upgraded because the brief expected it to be",
         target="K2", gates=["K2_STATUS_IS_SCOPED_NOT_UNQUALIFIED"],
         patch=_custody(lambda c: c["record"].update(status="SOURCE_BINARY_LOCAL"))),
    dict(fid="EK-02", title="a local binary is claimed", target="K2",
         gates=["K2_DOES_NOT_CLAIM_A_LOCAL_BINARY"],
         patch=_custody(lambda c: c["record"].update(binary_local=True))),
    dict(fid="EK-03", title="the binary is claimed readable", target="K2",
         gates=["K2_DOES_NOT_CLAIM_A_READABLE_BINARY"],
         patch=_custody(lambda c: c["record"].update(binary_readable=True))),
    dict(fid="EK-04", title="the brief's SHA-256 is reported as verified", target="K2",
         gates=["K2_DOES_NOT_CLAIM_A_VERIFIED_SHA256"],
         patch=_custody(lambda c: c["binding"].update(sha256_verified=True))),
    dict(fid="EK-05", title="a binary-dependent check quietly reports a result",
         target="K2", gates=["EVERY_BINARY_DEPENDENT_CHECK_IS_MARKED_NOT_READ"],
         patch=_custody(lambda c: c["record"]["unverifiable"].update(
             pdf_validity="VALID"))),
    dict(fid="EK-06", title="the page count is reported as observed", target="K2",
         gates=["EVERY_BINARY_DEPENDENT_CHECK_IS_MARKED_NOT_READ"],
         patch=_custody(lambda c: c["record"]["unverifiable"].update(
             page_count_verified=346))),
    dict(fid="EK-07", title="an unqualified absence status replaces the scoped one",
         target="K2", gates=["K2_STATUS_IS_SCOPED_NOT_UNQUALIFIED"],
         patch=_custody(lambda c: c["record"].update(status="SOURCE_MISSING"))),
    dict(fid="EK-08", title="a searched location is marked as having found the file",
         target="K2", gates=["NO_SEARCHED_LOCATION_REPORTS_THE_BINARY_FOUND"],
         patch=_custody(lambda c: c["locations_searched"][0].update(found=True))),
    dict(fid="EK-09", title="the not-searched list is emptied so absence looks total",
         target="K2", gates=["LOCATIONS_NOT_SEARCHED_ARE_NAMED_TOO"],
         patch=_custody(lambda c: c.update(locations_not_searched=[]))),
    dict(fid="EK-10", title="the search is thinned to a couple of places", target="K2",
         gates=["LOCATIONS_SEARCHED_ARE_ENUMERATED"],
         patch=_custody(lambda c: c.update(
             locations_searched=c["locations_searched"][:2]))),

    # ---------------- connector-read honesty ----------------
    dict(fid="EC-01", title="the truncated read is described as complete", target="K2",
         gates=["THE_CONNECTOR_READ_IS_DECLARED_INCOMPLETE"],
         patch=_custody(lambda c: c["connector_read"].update(complete=True))),
    dict(fid="EC-02", title="SOURCE_CONTENT_READ is claimed outright", target="K2",
         gates=["SOURCE_CONTENT_READ_IS_NOT_CLAIMED_OUTRIGHT"],
         patch=_custody(lambda c: c["record"].update(
             states_not_claimed=["SOURCE_BINARY_LOCAL", "SOURCE_BINARY_READABLE"]))),
    dict(fid="EC-03", title="the truncation evidence is reduced to an assertion",
         target="K2", gates=["THE_TRUNCATION_IS_EVIDENCED_NOT_ASSERTED"],
         patch=_custody(lambda c: c["connector_read"].update(
             truncation_evidence=["it looked short"]))),
    dict(fid="EC-04", title="the unread parts stop being named", target="K2",
         gates=["THE_UNREAD_PARTS_ARE_NAMED"],
         patch=_custody(lambda c: c["connector_read"].update(does_not_cover=[]))),
    dict(fid="EC-05", title="the character count is inflated toward plausibility",
         target="K2", gates=["THE_CONNECTOR_CHAR_COUNT_IS_THE_MEASURED_ONE"],
         patch=_custody(lambda c: c["connector_read"].update(chars=600000))),

    # ---------------- unknowns becoming numbers ----------------
    dict(fid="EU-01", title="decomposition is declared complete", target="K2",
         gates=["NO_DECOMPOSITION_IS_CLAIMED_COMPLETE"],
         patch=_hier(lambda h: h.update(decomposition_completed=True))),
    dict(fid="EU-02", title="a PL row is given a page span", target="K2",
         gates=["NO_PL_ROW_REPORTS_A_MEASURED_PAGE_SPAN"],
         patch=_hier(lambda h: h["rows"][0].update(pdf_start_page=1, pdf_end_page=38))),
    dict(fid="EU-03", title="an unknown image count becomes zero", target="K2",
         gates=["UNKNOWNS_ARE_NOT_REPORTED_AS_ZERO"],
         patch=_hier(lambda h: h["rows"][0].update(image_count=0))),
    dict(fid="EU-04", title="an unknown table count becomes a guess", target="K2",
         gates=["UNKNOWNS_ARE_NOT_REPORTED_AS_ZERO"],
         patch=_hier(lambda h: h["rows"][2].update(table_count=5))),
    dict(fid="EU-05", title="a candidate structure is promoted to a confirmed unit",
         target="K2", gates=["NOTHING_IS_CLAIMED_AS_A_CONFIRMED_UNIT",
                             "EVERY_ROW_IS_A_CANDIDATE_STRUCTURE"],
         patch=_hier(lambda h: (h["rows"][0].update(
             record_type="CONFIRMED_UNIT"), h.update(confirmed_units=1)))),
    dict(fid="EU-06", title="the unmapped body region is dropped", target="K2",
         gates=["THE_UNMAPPED_BODY_IS_RECORDED_AS_A_REGION"],
         patch=_hier(lambda h: h.update(unmapped_source_regions=0))),
    dict(fid="EU-07", title="an inferred PL mapping is presented as directly named",
         target="K2", gates=["DIRECTLY_NAMED_PACKAGES_ARE_DISTINGUISHED_FROM_INFERRED_"
                             "ONES", "NAMED_PLUS_INFERRED_ACCOUNTS_FOR_EVERY_PACKAGE"],
         patch=_hier(lambda h: h["pl_map_confidence"].update(
             directly_named=["PL01", "PL06", "PL07", "PL09"]))),

    # ---------------- the source conflict ----------------
    dict(fid="EF-01", title="the narrative count is silently corrected to match",
         target="K2", gates=["NARRATIVE_COUNT_RECORDED_VERBATIM",
                             "THE_TWO_COUNTS_ACTUALLY_DISAGREE"],
         patch=lambda: dict(CONFLICT=dict(K2.CONFLICT, narrative_module_count=6))),
    dict(fid="EF-02", title="the conflict is marked silently corrected", target="K2",
         gates=["THE_CONFLICT_IS_NOT_SILENTLY_CORRECTED"],
         patch=lambda: dict(CONFLICT=dict(K2.CONFLICT, silently_corrected=True))),
    dict(fid="EF-03", title="a typographical slip is escalated to Bariah", target="K2",
         gates=["THE_CONFLICT_IS_NOT_SENT_TO_BARIAH"],
         patch=lambda: dict(CONFLICT=dict(K2.CONFLICT, routed_to="BARIAH",
                                          in_bariah_register=True,
                                          requires_instructional_decision=True))),
    dict(fid="EF-04", title="the classification leaves the permitted set", target="K2",
         gates=["THE_CLASSIFICATION_IS_ONE_OF_THE_FOUR_PERMITTED"],
         patch=lambda: dict(CONFLICT=dict(K2.CONFLICT, classification="MINOR"))),
    dict(fid="EF-05", title="the evidence is thinned to a single source", target="K2",
         gates=["AT_LEAST_FOUR_INDEPENDENT_SOURCES_ARE_CITED"],
         patch=lambda: dict(CONFLICT=dict(K2.CONFLICT,
                                          evidence=K2.CONFLICT["evidence"][:1]))),
    dict(fid="EF-06", title="a module code is dropped from the roll", target="K2",
         gates=["MODULE_CODES_MATCH_THE_SOURCE"],
         patch=lambda: dict(CONFLICT=dict(
             K2.CONFLICT, module_codes_present=["M01", "M02", "M03", "M04", "M05"]))),
    dict(fid="EF-07", title="a PL code is invented", target="K2",
         gates=["PL_CODES_MATCH_THE_SOURCE"],
         patch=lambda: dict(CONFLICT=dict(
             K2.CONFLICT, pl_codes_present=K2.CONFLICT["pl_codes_present"] + ["PL10"]))),
    dict(fid="EF-08", title="the secondary KOD-column defect is dropped", target="K2",
         gates=["THE_SECONDARY_KOD_COLUMN_DEFECT_IS_RECORDED"],
         patch=lambda: dict(CONFLICT=dict(
             K2.CONFLICT,
             secondary_defect=dict(K2.CONFLICT["secondary_defect"], defect_id="NONE")))),

    # ---------------- hierarchy rolls ----------------
    dict(fid="EH-01", title="the module count follows the narrative instead of the tables",
         target="K2", gates=["MODULE_COUNT_MATCHES_THE_TABLES"],
         patch=_hier(lambda h: h.update(modules=8))),
    dict(fid="EH-02", title="a package disappears from the roll", target="K2",
         gates=["PACKAGE_COUNT_MATCHES_THE_TABLES",
                "THE_MODULE_MAP_PARTITIONS_THE_PACKAGES_EXACTLY",
                "K2_QUEUE_IDS_MATCH_THE_HIERARCHY_IDS"],
         patch=_hier(lambda h: (h["rows"].pop(), h.update(pl_packages=8)))),
    dict(fid="EH-03", title="a package is filed under the wrong module", target="K2",
         gates=["EVERY_PACKAGE_MAPS_TO_ITS_TEACHING_PLANS_MODULE",
                "K2_QUEUE_IDS_MATCH_THE_HIERARCHY_IDS"],
         patch=_hier(lambda h: h["rows"][8].update(module_code="M01"))),
    dict(fid="EH-04", title="every package is filed under M01 as the KOD column says",
         target="K2", gates=["EVERY_PACKAGE_MAPS_TO_ITS_TEACHING_PLANS_MODULE"],
         patch=_hier(lambda h: [r.update(module_code="M01") for r in h["rows"]])),
    dict(fid="EH-05", title="a teaching plan's page count drifts from its footer",
         target="K2", gates=["TEACHING_PLAN_PAGES_MATCH_THEIR_OWN_FOOTERS"],
         patch=lambda: dict(TEACHING_PLANS=[
             dict(t, pages=99) if t["pt"] == "PT05" else t
             for t in K2.TEACHING_PLANS])),
    dict(fid="EH-06", title="the plan-page total is typed rather than summed", target="K2",
         gates=["TEACHING_PLAN_PAGE_TOTAL_IS_THE_SUM_OF_THE_PARTS",
                "TEACHING_PLAN_PAGE_TOTAL_MATCHES_THE_STANDALONE_LITERAL"],
         patch=_hier(lambda h: h.update(teaching_plan_pages_total=70))),

    # ---------------- queue ----------------
    dict(fid="EQ-01", title="K2 reverts to one unresolved-source row", target="R2",
         gates=["K2_IS_NO_LONGER_A_SINGLE_UNRESOLVED_ROW", "K2_CONTRIBUTES_NINE_QUEUE_"
                "ROWS", "K2_COUNTS_ARE_REPORTED_SEPARATELY"],
         patch=_queue(lambda q: [r.update(record_type="UNRESOLVED_SOURCE")
                                 for r in _k2rows(q)])),
    dict(fid="EQ-02", title="a K2 row claims to be immediately executable", target="R2",
         gates=["NO_K2_ROW_IS_IMMEDIATELY_EXECUTABLE"],
         patch=_queue(lambda q: _k2rows(q)[0].update(immediately_executable=True))),
    dict(fid="EQ-03", title="a K2 row claims a readable binary", target="R2",
         gates=["NO_K2_ROW_CLAIMS_A_LOCAL_OR_READABLE_BINARY"],
         patch=_queue(lambda q: _k2rows(q)[3].update(binary_readable=True))),
    dict(fid="EQ-04", title="a K2 row claims rows were extracted from it", target="R2",
         gates=["NO_K2_ROW_CLAIMS_EXTRACTED_OR_MODEL_READY",
                "K2_COUNTS_ARE_REPORTED_SEPARATELY"],
         patch=_queue(lambda q: _k2rows(q)[1].update(extraction_status="EXTRACTED"))),
    dict(fid="EQ-05", title="a K2 row claims a finished model", target="R2",
         gates=["NO_K2_ROW_CLAIMS_EXTRACTED_OR_MODEL_READY",
                "K2_COUNTS_ARE_REPORTED_SEPARATELY"],
         patch=_queue(lambda q: _k2rows(q)[2].update(model_status="MODEL_READY"))),
    dict(fid="EQ-06", title="a K2 blocker is reassigned away from Firdaus", target="R2",
         gates=["EVERY_K2_BLOCKER_IS_OWNED_BY_FIRDAUS"],
         patch=_queue(lambda q: _k2rows(q)[4].update(blocker_owner="BARIAH"))),
    dict(fid="EQ-07", title="a K2 row acquires an authority dependency", target="R2",
         gates=["NO_K2_ROW_CARRIES_AN_AUTHORITY_DEPENDENCY"],
         patch=_queue(lambda q: _k2rows(q)[5].update(
             authority_dependency="K2-COURSE-01 assessment treatment"))),
    dict(fid="EQ-08", title="the headline metric absorbs the new K2 rows", target="R2",
         gates=["THE_HEADLINE_METRIC_DID_NOT_MOVE_WHEN_K2_ARRIVED"],
         patch=_queue(lambda q: q["counts"].update(
             immediately_executable_units=22))),
    dict(fid="EQ-09", title="the record types stop partitioning the queue", target="R2",
         gates=["RECORD_TYPES_STILL_PARTITION_THE_WHOLE_QUEUE"],
         patch=_queue(lambda q: q["counts"].update(candidate_structures=99))),
    dict(fid="EQ-10", title="the named executable list drifts from its count",
         target="R2", gates=["IMMEDIATELY_EXECUTABLE_IDS_ARE_PUBLISHED_BY_NAME"],
         patch=_queue(lambda q: q.update(
             immediately_executable_ids=q["immediately_executable_ids"][:5]))),
    dict(fid="EQ-11", title="something appears in the ready-to-emit list", target="R2",
         gates=["READY_TO_EMIT_IDS_ARE_PUBLISHED_AND_EMPTY"],
         patch=_queue(lambda q: q.update(
             ready_to_emit_pptx_unit_ids=["K5-PL06-T03-B03"]))),
    dict(fid="EQ-12", title="the retired percentage returns as a live count", target="R2",
         gates=["THE_RETIRED_PERCENTAGE_STILL_APPEARS_ONLY_IN_ITS_RETIREMENT_RECORD"],
         patch=_queue(lambda q: q["counts"].update(source_ready="97.8 percent"))),
    dict(fid="EQ-13", title="a K2 unit id is rebuilt from the faulty KOD column",
         target="R2", gates=["NO_UNIT_ID_IS_BUILT_FROM_THE_FAULTY_KOD_COLUMN",
                             "K2_QUEUE_IDS_MATCH_THE_HIERARCHY_IDS"],
         patch=_queue(lambda q: [r.update(
             unit_or_candidate_id=f"K2-M01-{r['pl']}") for r in _k2rows(q)])),

    # ---------------- suite accounting ----------------
    dict(fid="ES-01", title="the suite adopts a sibling suite's identity", target="QA",
         gates=["SUITE_ID_DECLARED", "SUITE_ID_IS_NOT_ANY_SIBLING_SUITE"],
         patch=lambda: dict(SUITE_ID="STAGE_4_2F_D_RELEASE_FACTS_QA_v1")),
    dict(fid="ES-02", title="oracle separation is claimed rather than deferred",
         target="QA", gates=["ORACLE_SEPARATION_IS_STILL_RECORDED_AS_DEFERRED"],
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
    global _BASE_CUSTODY, _BASE_HIER, _BASE_QUEUE
    _BASE_CUSTODY = K2.custody()
    _BASE_HIER = K2.hierarchy()
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
    md = ["<!-- GENERATED by docs/source/tools/src_k2_mutations_v1.py -->", "",
          "# Mutation report — Stage 4.2F-E K2", "", "```",
          f"SUITE_ID  = {r['suite_id']}",
          f"FIXTURES  = {r['fixture_count']}",
          f"DETECTED  = {r['detected']}",
          f"MISSED    = {len(r['missed'])}",
          f"BASELINE  = {r['baseline_pass']}/{r['baseline_total']}", "```", "",
          "Every fixture is a version of the same defect this run could most easily have "
          "committed: claiming the binary was seen. No sibling suite is touched.", "",
          "| fixture | what it breaks | target | gates that fired |", "|---|---|---|---|"]
    md += [f"| `{f['fixture_id']}` | {f['title']} | {f['target']} | "
           f"{', '.join('`' + g + '`' for g in f['fired']) or '**NONE — MISSED**'} |"
           for f in r["fixtures"]]
    md += [""]
    path = os.path.join(SRC_DIR, "STAGE_4_2F_E_MUTATION_REPORT_v1.md")
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
    print("report   :", emit_report(r))
    sys.exit(1 if (r["missed"] or r["baseline_false_failures"]) else 0)
