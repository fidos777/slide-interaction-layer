# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-F — the binary-dependent K2 continuation.

    SUITE_ID = STAGE_4_2F_F_K2_QA_v1
    docs/source/.venv-k2/bin/python docs/source/tools/src_k2f_mutations_v1.py

No historical fixture is refactored and no sibling suite is touched.

4.2F-E's defect was claiming the binary was seen when it was not. 4.2F-F's defect is the
MIRROR: now that the binary IS seen, over-claiming — moving a status further than the
bytes support, promoting a source-ready package to a confirmed or executable unit, calling
a detector's table count a measurement, silently resolving a source anomaly, marking all
nine modelled when only two are. Each fixture injects one such over-claim into the model
and confirms the suite catches it.

Every fixture patches a src_k2f_v1 function in memory, runs the live suite, and asserts the
named gate(s) flip to failing. Nothing on disk is mutated; the emitted artifacts are left
exactly as published.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import src_k2f_v1 as F      # noqa: E402
import src_k2f_qa_v1 as QA  # noqa: E402

SUITE_ID = "STAGE_4_2F_F_K2_QA_v1"

_ORIG = {name: getattr(F, name) for name in
         ("custody", "page_boundary_map", "hierarchy", "assessment_inventory",
          "image_table_inventory", "provisional_models", "decision_register",
          "queue_rows")}


def _restore():
    for name, fn in _ORIG.items():
        setattr(F, name, fn)


def _wrap(name, mutate):
    """Return a function that produces the original value then mutates it in place."""
    orig = _ORIG[name]

    def patched():
        d = orig()
        mutate(d)
        return d
    return patched


# Each fixture: (id, what it breaks, model fn, mutation, gates that must fire)
def _fx(fid, desc, fn, mutate, gates):
    return dict(id=fid, desc=desc, fn=fn, mutate=mutate, gates=gates)


def _first_pl_row(h, pl="PL01"):
    return next(r for r in h["rows"] if r["pl"] == pl)


FIXTURES = [
    # ---- custody: over-claiming identity / status ----
    _fx("FF-01", "status left un-moved (not hash-verified)", "custody",
        lambda d: d["record"].update(status="NOT_FOUND_IN_LOCATIONS_SEARCHED"),
        ["STATUS_IS_NOW_HASH_VERIFIED"]),
    _fx("FF-02", "binary falsely still not local", "custody",
        lambda d: d["record"].update(binary_local=False),
        ["BINARY_IS_CLAIMED_LOCAL_AND_READABLE"]),
    _fx("FF-03", "observed sha256 altered away from the brief", "custody",
        lambda d: d["record"]["verified"]["sha256"].update(observed="deadbeef"),
        ["OBSERVED_SHA256_EQUALS_THE_BRIEF"]),
    _fx("FF-04", "sha256 reported unverified", "custody",
        lambda d: d["binding"].update(sha256_verified=False),
        ["SHA256_IS_VERIFIED_TRUE"]),
    _fx("FF-05", "observed page count wrong", "custody",
        lambda d: d["record"]["verified"]["pages"].update(observed=999),
        ["OBSERVED_PAGES_EQUAL_THE_BRIEF"]),
    _fx("FF-06", "encryption misreported", "custody",
        lambda d: d["record"]["verified"].update(encryption_status="ENCRYPTED"),
        ["PDF_IS_NOT_ENCRYPTED"]),
    _fx("FF-07", "granularity claimed already decided", "custody",
        lambda d: d["record"]["states_still_not_claimed"].remove(
            "UNIT_GRANULARITY_DECIDED"),
        ["GRANULARITY_IS_STILL_NOT_CLAIMED_DECIDED"]),
    # ---- page map ----
    _fx("FF-08", "the 346-page partition claimed clean when broken", "page_boundary_map",
        lambda d: d["accounting"].update(clean_partition=False, unassigned_pages=[200]),
        ["THE_346_PAGES_FORM_A_CLEAN_PARTITION", "NO_PAGE_IS_UNASSIGNED"]),
    _fx("FF-09", "a PL span drifts from the hand-typed span", "page_boundary_map",
        lambda d: [r.update(pdf_end_page=130) for r in d["regions"]
                   if r["region"] == "PL01"],
        ["EVERY_PL_SPAN_MATCHES_THE_HAND_TYPED_SPAN"]),
    _fx("FF-10", "region pages stop summing to 346", "page_boundary_map",
        lambda d: [r.update(pages=r["pages"] + 5) for r in d["regions"]
                   if r["region"] == "PL01"],
        ["REGION_PAGES_SUM_TO_346"]),
    # ---- hierarchy ----
    _fx("FF-11", "decomposition claimed incomplete", "hierarchy",
        lambda d: d.update(decomposition_completed=False),
        ["DECOMPOSITION_IS_NOW_COMPLETE"]),
    _fx("FF-12", "a package filed under the wrong module", "hierarchy",
        lambda d: _first_pl_row(d).update(module_code="M06"),
        ["PL_TO_MODULE_MAP_IS_CONFIRMED_FROM_EACH_HEADER"]),
    _fx("FF-13", "a PL promoted to a confirmed unit", "hierarchy",
        lambda d: d.update(confirmed_units=1),
        ["STILL_NO_PL_IS_A_CONFIRMED_UNIT"]),
    _fx("FF-14", "an unknown span reintroduced", "hierarchy",
        lambda d: _first_pl_row(d).update(pdf_start_page="UNKNOWN_NOT_MEASURED"),
        ["EVERY_ROW_HAS_AN_OBSERVED_PAGE_SPAN", "NO_ROW_STILL_CARRIES_AN_UNKNOWN_SPAN"]),
    # ---- assessment ----
    _fx("FF-15", "the KT paper count is wrong", "assessment_inventory",
        lambda d: d.update(kt_paper_count=7),
        ["NINE_KT_TASK_PAPERS_ARE_INVENTORIED"]),
    _fx("FF-16", "the KT numbering break is dropped", "assessment_inventory",
        lambda d: [o.update(numbering_break_codes=[]) for o in d["observations"]
                   if o["defect_id"] == "K2-SOURCE-OBS-02"],
        ["THE_KT_NUMBERING_BREAK_IS_RECORDED"]),
    _fx("FF-17", "the KT06 collision silently resolved (OBS-03 removed)",
        "assessment_inventory",
        lambda d: d.__setitem__("observations",
                                [o for o in d["observations"]
                                 if o["defect_id"] != "K2-SOURCE-OBS-03"]),
        ["THE_KT06_COLLISION_IS_RECORDED_NOT_RESOLVED"]),
    _fx("FF-18", "a source anomaly escalated to Bariah", "assessment_inventory",
        lambda d: d["observations"][0].update(routed_to="BARIAH"),
        ["SOURCE_ANOMALIES_STAY_WITH_FIRDAUS_NOT_BARIAH"]),
    # ---- image/table honesty ----
    _fx("FF-19", "a detector table count renamed a plain table count",
        "image_table_inventory",
        lambda d: [r.__setitem__("table_count", r.pop("table_detector_count"))
                   for r in d["per_pl"]],
        ["TABLE_COUNTS_ARE_LABELLED_DETECTOR_NOT_MEASURED",
         "NO_TABLE_FIELD_IS_CALLED_A_PLAIN_TABLE_COUNT"]),
    # ---- models: over-claiming ----
    _fx("FF-20", "all nine claimed modelled", "provisional_models",
        lambda d: d.update(count=9),
        ["EXACTLY_TWO_MODELS_WERE_PRODUCED", "ALL_NINE_ARE_NOT_OVERCLAIMED_AS_MODELLED"]),
    _fx("FF-21", "a model marked final rather than provisional", "provisional_models",
        lambda d: d["models"][0].update(confidence="FINAL"),
        ["MODELS_ARE_MARKED_PROVISIONAL_NOT_FINAL"]),
    # ---- decisions ----
    _fx("FF-22", "granularity dropped as the first decision", "decision_register",
        lambda d: d["decisions"].pop(0),
        ["GRANULARITY_IS_THE_FIRST_DECISION"]),
    # ---- queue rows: over-promotion ----
    _fx("FF-23", "a K2 row made immediately executable", "queue_rows",
        lambda rows: rows[0].update(immediately_executable=True),
        ["NO_K2_ROW_IS_IMMEDIATELY_EXECUTABLE_YET"]),
    _fx("FF-24", "a K2 row promoted to a confirmed unit", "queue_rows",
        lambda rows: rows[0].update(record_type="CONFIRMED_PRODUCTION_UNIT"),
        ["NO_K2_ROW_IS_A_CONFIRMED_UNIT"]),
    _fx("FF-25", "all nine K2 rows claimed model-ready", "queue_rows",
        lambda rows: [r.update(model_status="MODEL_READY") for r in rows],
        ["EXACTLY_TWO_K2_ROWS_ARE_MODEL_READY"]),
    _fx("FF-26", "the KT06 exception cleared from PL06's blocker and it is modelled",
        "queue_rows",
        lambda rows: [r.update(exact_blocker="K2-DEC-01 only", model_status="MODEL_READY")
                      for r in rows if r["pl"] == "PL06"],
        ["KT06_EXCEPTION_PLS_ARE_HELD_AND_NOT_MODEL_READY"]),
    _fx("FF-27", "a K2 row marked ready to emit", "queue_rows",
        lambda rows: rows[0].update(ready_to_emit_pptx=True),
        ["EVERY_K2_ROW_IS_READY_TO_EMIT_FALSE"]),
    # ---- KT06 distinct-consequence collapses ----
    _fx("FF-28", "PL06 and PL08 given the same KT06 consequence", "assessment_inventory",
        lambda d: [c.update(consequence="SAME") for o in d["observations"]
                   if o["defect_id"] == "K2-SOURCE-OBS-03"
                   for c in o["consequences"]],
        ["KT06_RECORDS_DISTINCT_CONSEQUENCES_FOR_PL06_AND_PL08",
         "PL06_AND_PL08_CONSEQUENCES_ARE_NOT_THE_SAME"]),
    _fx("FF-29", "the per-package KT06 consequences dropped entirely",
        "assessment_inventory",
        lambda d: [o.__setitem__("consequences", []) for o in d["observations"]
                   if o["defect_id"] == "K2-SOURCE-OBS-03"],
        ["KT06_RECORDS_DISTINCT_CONSEQUENCES_FOR_PL06_AND_PL08"]),
]


def run():
    # baseline must be green first
    base = QA.summary()
    baseline_ok = base["passed"] == base["total"]
    results = []
    for fx in FIXTURES:
        setattr(F, fx["fn"], _wrap(fx["fn"], fx["mutate"]))
        try:
            res = QA.run()
        finally:
            _restore()
        failed = {g["gate_id"] for g in res if not g["ok"] and not g["skipped"]}
        detected = set(fx["gates"]) & failed
        results.append(dict(id=fx["id"], desc=fx["desc"], target=fx["fn"],
                            expected_gates=fx["gates"],
                            gates_fired=sorted(detected),
                            detected=bool(detected)))
    return dict(suite_id=SUITE_ID, baseline_ok=baseline_ok,
                baseline=f"{base['passed']}/{base['total']}",
                fixtures=len(results),
                detected=len([r for r in results if r["detected"]]),
                missed=[r for r in results if not r["detected"]],
                results=results)


BANNER = "<!-- GENERATED by docs/source/tools/src_k2f_mutations_v1.py -->"


def emit():
    s = run()
    md = [BANNER, "", "# Mutation report — Stage 4.2F-F K2", "", "```",
          f"SUITE_ID  = {s['suite_id']}",
          f"FIXTURES  = {s['fixtures']}",
          f"DETECTED  = {s['detected']}",
          f"MISSED    = {len(s['missed'])}",
          f"BASELINE  = {s['baseline']}", "```", "",
          "Every fixture is a version of the same defect this run could most easily have "
          "committed: over-claiming now that the binary is readable. No sibling suite is "
          "touched; no artifact on disk is mutated.", "",
          "| fixture | what it breaks | target | gate(s) that fired |",
          "|---|---|---|---|"]
    for r in s["results"]:
        fired = ", ".join(f"`{g}`" for g in r["gates_fired"]) or "**NONE — MISSED**"
        md.append(f"| `{r['id']}` | {r['desc']} | {r['target']} | {fired} |")
    md += [""]
    p = os.path.join(SRC_DIR, "STAGE_4_2F_F_MUTATION_REPORT_v1.md")
    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    return p, s


if __name__ == "__main__":
    p, s = emit()
    print(f"baseline {s['baseline']} (ok={s['baseline_ok']})")
    print(f"{s['detected']}/{s['fixtures']} fixtures detected")
    for m in s["missed"]:
        print("  MISSED", m["id"], m["desc"], "expected", m["expected_gates"])
    print("wrote", os.path.basename(p))
