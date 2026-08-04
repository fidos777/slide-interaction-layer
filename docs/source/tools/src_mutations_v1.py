# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-C — new source, extraction and queue paths only.

    SUITE_ID = PROJECT_SOURCE_CUSTODY_QA_v1
    python3 docs/source/tools/src_mutations_v1.py

Only the paths this run introduced are attacked. No historical fixture is refactored.

The defects these exist to catch are all forms of *a source claim that is stronger than the
evidence behind it*: an unread file given a page count, a missing binary that looks extracted,
an unknown that becomes zero, a boundary that goes quiet, one unit inheriting another's rows,
a pending pattern package that hardens into a rule, a percentage typed rather than counted,
and an oracle reading the same parser it is checking.
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
import src_authority_v1 as A     # noqa: E402
import src_inventory_v1 as INV   # noqa: E402
import src_queue_v1 as Q         # noqa: E402
import src_qa_v1 as QA           # noqa: E402
import pl06_extract_v1 as EX     # noqa: E402
import pl06_unit_model_v1 as UM  # noqa: E402

TARGETS = {"A": A, "INV": INV, "Q": Q, "EX": EX, "UM": UM, "QA": QA}

_BASE_INV = _BASE_QUEUE = _BASE_MODELS = _BASE_EXTRACTS = None


def _inv(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_INV)
            fn(d)
            return d
        return dict(inventory=patched)
    return apply


def _queue(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_QUEUE)
            fn(d)
            return d
        return dict(summary=patched)
    return apply


def _models(fn):
    def apply():
        def patched():
            m = copy.deepcopy(_BASE_MODELS)
            fn(m)
            return m, copy.deepcopy(_BASE_EXTRACTS)
        return dict(all_models=patched)
    return apply


def _extracts(fn):
    def apply():
        def patched():
            e = copy.deepcopy(_BASE_EXTRACTS)
            fn(e)
            return e
        return dict(extract_all=patched)
    return apply


FIXTURES = [
    # ---------------- authority ----------------
    dict(fid="AU-01", title="the authority loses its owner", target="A",
         gates=["SRC_AUTH_01_IS_OWNED_AND_APPROVED"],
         patch=lambda: dict(AUTHORITY=dict(A.AUTHORITY, owner="CAIR"))),
    dict(fid="AU-02", title="the authority becomes per-unit again", target="A",
         gates=["THE_AUTHORITY_IS_PACKAGE_LEVEL_NOT_PER_UNIT"],
         patch=lambda: dict(AUTHORITY=dict(A.AUTHORITY, granularity="UNIT",
                                           applied_at="PER_UNIT"))),
    dict(fid="AU-03", title="an exclusion is quietly dropped", target="A",
         gates=["SIX_EXPLICIT_EXCLUSIONS",
                "THE_EXCLUSIONS_NAME_EVERY_THING_NOT_AUTHORISED"],
         patch=lambda: dict(AUTHORITY=dict(
             A.AUTHORITY, explicit_exclusions=[e for e in A.AUTHORITY["explicit_exclusions"]
                                               if "answer key" not in e]))),
    dict(fid="AU-04", title="the instructional-approval exclusion is removed", target="A",
         gates=["THE_EXCLUSIONS_NAME_EVERY_THING_NOT_AUTHORISED",
                "SIX_EXPLICIT_EXCLUSIONS"],
         patch=lambda: dict(AUTHORITY=dict(
             A.AUTHORITY, explicit_exclusions=[e for e in A.AUTHORITY["explicit_exclusions"]
                                               if "instructional approval" not in e]))),
    dict(fid="AU-05", title="a permitted operation is added without record", target="A",
         gates=["SIX_PERMITTED_OPERATIONS"],
         patch=lambda: dict(AUTHORITY=dict(
             A.AUTHORITY,
             permitted_operations=A.AUTHORITY["permitted_operations"]
             + ["approve instructional treatment"]))),
    dict(fid="AU-06", title="D-25 is recorded as deleted rather than superseded", target="A",
         gates=["D25_IS_SUPERSEDED_NOT_REWRITTEN"],
         patch=lambda: dict(SUPERSESSION=dict(A.SUPERSESSION,
                                              relationship="DELETED_AND_REPLACED_BY",
                                              historical_record_status="REWRITTEN"))),

    # ---------------- the pending pattern package ----------------
    dict(fid="PP-01", title="the pattern package is promoted to authority", target="A",
         gates=["THE_PATTERN_PACKAGE_IS_PENDING_NOT_AUTHORITY"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(A.PENDING_PATTERN_PACKAGE,
                                                         is_authority=True))),
    dict(fid="PP-02", title="the pattern package becomes auto-appliable", target="A",
         gates=["THE_PATTERN_PACKAGE_IS_PENDING_NOT_AUTHORITY"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(A.PENDING_PATTERN_PACKAGE,
                                                         may_be_auto_applied=True))),
    dict(fid="PP-03", title="a unit's pattern family hardens into a course rule",
         target="UM", gates=["NO_MODEL_TREATS_THE_PATTERN_PACKAGE_AS_A_RULE"],
         patch=_models(lambda m: m["K5-PL06-T05-B01"]["pattern_family"].update(
             cls="COURSE_RULE_ALREADY_APPROVED"))),
    dict(fid="PP-04", title="a model starts freezing things", target="UM",
         gates=["EVERY_MODEL_FREEZES_NOTHING"],
         patch=_models(lambda m: m["K5-PL06-T03-B03"].update(
             frozen_nothing=["visual reuse"]))),
    dict(fid="PP-05", title="the unfrozen list is shortened at source", target="UM",
         gates=["SEVEN_THINGS_ARE_DECLARED_UNFROZEN", "EVERY_MODEL_FREEZES_NOTHING"],
         patch=lambda: dict(FROZEN_NOTHING=UM.FROZEN_NOTHING[:-1])),
    dict(fid="PP-06", title="a maximum screen count is guessed", target="UM",
         gates=["NO_MODEL_CLAIMS_A_MAXIMUM_SCREEN_COUNT"],
         patch=_models(lambda m: m["K5-PL06-T06-B01"]["screen_sequence"]
                       ["arithmetic"].update(maximum_total_screens=12))),
    dict(fid="PP-07", title="a drafted answer key is called approved", target="UM",
         gates=["NO_ANSWER_KEY_IS_APPROVED"],
         patch=_models(lambda m: m["K5-PL06-T05-B01"]["assessment"].update(
             key_status="APPROVED"))),
    dict(fid="PP-08", title="the K3 source scheme is promoted to a storyboard key",
         target="INV", gates=["NO_K3_SOURCE_ANSWER_SCHEME_IS_CALLED_APPROVED"],
         patch=_inv(lambda d: [x["source_assessment"].update(key_status="APPROVED")
                               for x in d["k3_models"]])),
    dict(fid="PP-09", title="a character is proposed while STOP-006 is open", target="UM",
         gates=["NO_CHARACTER_IS_PROPOSED_WHILE_STOP_006_IS_OPEN"],
         patch=_models(lambda m: m["K5-PL06-T05-B01"]["dialogue"].update(
             cast="Alya dan Encik Rahman"))),

    # ---------------- oracle independence ----------------
    dict(fid="OR-01", title="a shared boundary goes quiet in the extractor", target="EX",
         gates=["SHARED_BOUNDARY_TRUTH_IS_READ_FROM_THE_RAW_MANIFEST"],
         patch=lambda: dict(UNITS=[dict(u, shared_start=False, shared_end=False)
                                   for u in EX.UNITS])),
    dict(fid="OR-02", title="one unit's shared-end flag is flipped", target="EX",
         gates=["SHARED_BOUNDARY_TRUTH_IS_READ_FROM_THE_RAW_MANIFEST"],
         patch=lambda: dict(UNITS=[dict(u, shared_end=False)
                                   if u["unit_id"] == "K5-PL06-T03-B03" else u
                                   for u in EX.UNITS])),
    dict(fid="OR-03", title="page attribution falls back to Word's cached layout",
         target="EX",
         gates=["PAGE_ATTRIBUTION_USES_A_DIFFERENT_ARTIFACT_FROM_THE_EXTRACTION"],
         patch=_extracts(lambda e: [x.update(page_attribution_primary="WORD_CACHED_LAYOUT")
                                    for x in e.values()])),
    dict(fid="OR-04", title="the second-opinion oracle is dropped", target="EX",
         gates=["THE_CACHED_LAYOUT_SECOND_OPINION_IS_STILL_RECORDED"],
         patch=_extracts(lambda e: [x.pop("page_attribution_secondary")
                                    for x in e.values()])),
    dict(fid="OR-05", title="the typeset oracle stops agreeing with the frozen map",
         target="EX", gates=["THE_TYPESET_ORACLE_AGREES_WITH_THE_FROZEN_MAP"],
         patch=_extracts(lambda e: e["K5-PL06-T05-B01"]["page_attribution_divergence"]
                         .update(typeset_agrees_with_frozen=False))),
    dict(fid="OR-06", title="the two page oracles are recorded as agreeing", target="EX",
         gates=["THE_TWO_PAGE_ORACLES_ARE_RECORDED_AS_DISAGREEING"],
         patch=_extracts(lambda e: [x["page_attribution_divergence"].update(
             cached_layout_agrees_with_frozen=True) for x in e.values()])),
    # OR-07 walked past the suite on its first run. The gate compared two calls of the same
    # patched extractor, so both sides carried the mutation. It now reads the raw frozen map.
    dict(fid="OR-07", title="a frozen anchor is moved", target="EX",
         gates=["REGENERATION_DOES_NOT_MOVE_A_FROZEN_ANCHOR"],
         patch=_extracts(lambda e: e["K5-PL06-T03-B03"]["boundary"].update(
             frozen_start_paragraph=4700))),
    dict(fid="OR-08", title="the generalised reader stops matching the frozen T04 extract",
         target="EX", gates=["THE_NEW_READER_REPRODUCES_THE_FROZEN_T04_EXTRACT"],
         patch=lambda: dict(t04_equivalence=lambda: dict(
             ran=True, equivalent=False, frozen_row_count=100, got_row_count=99,
             text_mismatches=[dict(sequence=5)], type_mismatches=[],
             paragraph_index_mismatches=[]))),
    dict(fid="OR-09", title="unit counts are taken from the queue being validated",
         target="INV", gates=["UNIT_COUNTS_ARE_NOT_DERIVED_FROM_THE_QUEUE_BEING_VALIDATED"],
         patch=_inv(lambda d: d["k5"]["totals"].update(confirmed_units=46))),

    # ---------------- custody ----------------
    dict(fid="CU-01", title="an unhashed package claims local verification", target="A",
         gates=["NO_PACKAGE_CLAIMS_HASH_VERIFICATION_WITHOUT_A_HASH",
                "EVERY_UNHASHED_PACKAGE_SAYS_SO_EXPLICITLY"],
         patch=lambda: dict(k2_custody=lambda: dict(
             A.k2_custody(), evidence_class="LOCAL_BINARY_HASH_VERIFIED"))),
    dict(fid="CU-02", title="an undeclared evidence class appears", target="A",
         gates=["EVERY_PACKAGE_CARRIES_A_DECLARED_EVIDENCE_CLASS"],
         patch=lambda: dict(k2_custody=lambda: dict(
             A.k2_custody(), evidence_class="PROBABLY_FINE"))),
    dict(fid="CU-03", title="a K3 file is given a plausible-looking hash", target="A",
         gates=["EVERY_UNHASHED_PACKAGE_SAYS_SO_EXPLICITLY"],
         patch=lambda: dict(k3_custody=lambda: [dict(r, sha256="a" * 64)
                                                for r in A.k3_custody()])),

    # ---------------- unknown cannot become zero ----------------
    dict(fid="UK-01", title="the K2 page count becomes zero", target="INV",
         gates=["EVERY_UNMEASURED_K2_FIELD_IS_UNKNOWN_NOT_ZERO"],
         patch=_inv(lambda d: d["k2"].update(page_count=0))),
    dict(fid="UK-02", title="the K2 unit count is estimated", target="INV",
         gates=["EVERY_UNMEASURED_K2_FIELD_IS_UNKNOWN_NOT_ZERO"],
         patch=_inv(lambda d: d["k2"].update(estimated_total_units=12))),
    dict(fid="UK-03", title="an unread K3 PDF is given a page count from the template",
         target="INV", gates=["NO_UNREAD_K3_PDF_IS_GIVEN_A_PAGE_COUNT"],
         patch=_inv(lambda d: [r.update(pages=17) for r in d["k3"]["rows"]
                               if r["read_status"] == INV.NOT_READ])),
    dict(fid="UK-04", title="an unread K3 PDF is classified SOURCE_READY_CLEAN",
         target="INV", gates=["NO_UNREAD_K3_PDF_IS_CLASSIFIED_CLEAN"],
         patch=_inv(lambda d: [r.update(classification="SOURCE_READY_CLEAN")
                               for r in d["k3"]["rows"]
                               if r["read_status"] == INV.NOT_READ])),
    dict(fid="UK-05", title="more visuals are attested than exist", target="UM",
         gates=["UNKNOWN_VISUAL_COUNTS_ARE_NOT_RENDERED_AS_ZERO"],
         patch=_models(lambda m: m["K5-PL06-T03-B03"]["visual_obligations"].update(
             source_attested=9))),

    # ---------------- missing source cannot look extracted ----------------
    dict(fid="MS-01", title="K2 is marked extracted in the queue", target="Q",
         gates=["K2_IS_NOT_MARKED_EXTRACTED_ANYWHERE_IN_THE_QUEUE"],
         patch=_queue(lambda d: [r.update(extraction_status="EXTRACTED")
                                 for r in d["rows"] if r["course"] == "K2"])),
    dict(fid="MS-02", title="an unread K3 row is marked as text-read", target="Q",
         gates=["NO_UNREAD_K3_ROW_IS_MARKED_EXTRACTED"],
         patch=_queue(lambda d: [r.update(extraction_status="CONNECTOR_TEXT_READ")
                                 for r in d["rows"] if r["course"] == "K3"])),
    dict(fid="MS-03", title="a queue row claims an extract file that is not on disk",
         target="Q", gates=["EVERY_EXTRACTED_ROW_HAS_A_FILE_ON_DISK"],
         patch=_queue(lambda d: [r.update(extraction_status="EXTRACTED")
                                 for r in d["rows"]
                                 if r["unit_id"] == "K5-PL06-T01-B01"])),

    # ---------------- boundary and leak ----------------
    dict(fid="BD-01", title="one unit inherits another unit's source rows", target="EX",
         gates=["NO_UNIT_INHERITS_ANOTHER_UNITS_SOURCE_ROWS"],
         patch=_extracts(lambda e: e["K5-PL06-T03-B03"]["rows"].append(
             dict(e["K5-PL06-T03-B04"]["rows"][3])))),
    dict(fid="BD-02", title="a row falls outside its own span", target="EX",
         gates=["NO_ROW_FALLS_OUTSIDE_ITS_OWN_SPAN"],
         patch=_extracts(lambda e: e["K5-PL06-T05-B01"]["rows"][2].update(
             source_paragraph_start=99))),
    dict(fid="BD-03", title="the shared-page units stop abutting", target="EX",
         gates=["THE_SHARED_PAGE_UNITS_ABUT_EXACTLY"],
         patch=_extracts(lambda e: e["K5-PL06-T03-B03"]["boundary_proof"].update(
             last_included_paragraph_index=4800))),
    dict(fid="BD-04", title="a unit stops emitting its excluded neighbours", target="EX",
         gates=["EVERY_UNIT_EMITS_ITS_EXCLUDED_NEIGHBOURS"],
         patch=_extracts(lambda e: e["K5-PL06-T03-B04"]["boundary_proof"].update(
             excluded_before=[]))),
    dict(fid="BD-05", title="extraction reverts to a page range", target="EX",
         gates=["EXTRACTION_WAS_NEVER_BY_PAGE_RANGE"],
         patch=_extracts(lambda e: e["K5-PL06-T06-B01"]["boundary"].update(
             extraction_method="PAGE_RANGE_SLICE"))),
    dict(fid="BD-06", title="an anchor search records no hits", target="EX",
         gates=["EVERY_EXTRACT_RECORDS_ITS_ANCHOR_HIT_COUNT"],
         patch=_extracts(lambda e: e["K5-PL06-T03-B03"]["boundary"]["anchor_search"]
                         .update(start_hit_count=0))),
    dict(fid="BD-07", title="a row carries another unit's unit_id", target="UM",
         gates=["EVERY_UNIT_ROW_CARRIES_ITS_OWN_UNIT_ID"],
         patch=_models(lambda m: m["K5-PL06-T03-B04"]["extraction_qa"].update(
             every_row_carries_the_unit_id=False))),

    # ---------------- queue ----------------
    dict(fid="QU-01", title="a queue column is dropped", target="Q",
         gates=["THE_QUEUE_HAS_ALL_FOURTEEN_COLUMNS"],
         patch=lambda: dict(COLUMNS=[c for c in Q.COLUMNS if c != "blocker"])),
    dict(fid="QU-02", title="a queue row loses a column", target="Q",
         gates=["EVERY_QUEUE_ROW_HAS_EVERY_COLUMN"],
         patch=_queue(lambda d: d["rows"][0].pop("qa_readiness"))),
    dict(fid="QU-03", title="a queue row stops inheriting the authority", target="Q",
         gates=["EVERY_QUEUE_ROW_INHERITS_THE_AUTHORITY"],
         patch=_queue(lambda d: d["rows"][5].update(source_authority_inherited="NONE"))),
    dict(fid="QU-04", title="a queue row has no next action", target="Q",
         gates=["EVERY_QUEUE_ROW_NAMES_A_NEXT_ACTION"],
         patch=_queue(lambda d: d["rows"][7].update(next_executable_action=""))),
    dict(fid="QU-05", title="a queue row has no blocker field", target="Q",
         gates=["EVERY_QUEUE_ROW_NAMES_A_BLOCKER_OR_SAYS_NONE"],
         patch=_queue(lambda d: d["rows"][9].update(blocker=""))),
    dict(fid="QU-06", title="two queue rows share an id", target="Q",
         gates=["NO_QUEUE_ID_IS_DUPLICATED"],
         patch=_queue(lambda d: d["rows"][3].update(
             unit_id=d["rows"][2]["unit_id"]))),
    # The percentage must be counted from the rows, not carried alongside them.
    dict(fid="QU-07", title="the extracted percentage is typed rather than counted",
         target="Q", gates=["THE_EXTRACTED_PERCENTAGE_IS_COUNTED_NOT_TYPED"],
         patch=_queue(lambda d: d.update(extracted_percent=95.0))),
    dict(fid="QU-08", title="the model-ready percentage is typed rather than counted",
         target="Q", gates=["THE_MODEL_READY_PERCENTAGE_IS_COUNTED_NOT_TYPED"],
         patch=_queue(lambda d: d.update(model_ready_percent=88.0))),
    dict(fid="QU-09", title="a blocker is attributed to nobody", target="Q",
         gates=["EVERY_BLOCKER_HAS_A_NAMED_OWNER"],
         patch=_queue(lambda d: d.update(
             blockers_by_owner=dict(d["blockers_by_owner"],
                                    SOMEONE=dict(count=1, units=["X"]))))),

    # ---------------- accounting ----------------
    dict(fid="AC-01", title="the suite loses its identity", target="QA",
         gates=["SUITE_ID_DECLARED"], patch=lambda: dict(SUITE_ID="")),
    dict(fid="AC-02", title="the suite adopts the prior suite identity", target="QA",
         gates=["SUITE_ID_DECLARED", "SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE"],
         patch=lambda: dict(SUITE_ID="PL06_AUTHORITY_HARVEST_BATCH1_QA_v1")),
    dict(fid="AC-03", title="the NOT_CHECKED list is emptied", target="QA",
         gates=["NOT_CHECKED_IS_PUBLISHED"], patch=lambda: dict(NOT_CHECKED=[])),
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
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(tgt, k, v)


def main():
    global _BASE_INV, _BASE_QUEUE, _BASE_MODELS, _BASE_EXTRACTS
    _BASE_INV = INV.inventory()
    _BASE_QUEUE = Q.summary()
    _BASE_MODELS, _BASE_EXTRACTS = UM.all_models()
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
    md = ["<!-- GENERATED by docs/source/tools/src_mutations_v1.py -->", "",
          "# Mutation report — source, extraction and queue", "", "```",
          f"SUITE_ID  = {r['suite_id']}",
          f"FIXTURES  = {r['fixture_count']}",
          f"DETECTED  = {r['detected']}",
          f"MISSED    = {len(r['missed'])}",
          f"BASELINE  = {r['baseline_pass']}/{r['baseline_total']}", "```", "",
          "Only the paths this run introduced are attacked. No historical fixture is "
          "refactored and no historical gate is touched.", "",
          "| fixture | what it breaks | target | gates that fired |", "|---|---|---|---|"]
    md += [f"| `{f['fixture_id']}` | {f['title']} | {f['target']} | "
           f"{', '.join('`' + g + '`' for g in f['fired']) or '**NONE — MISSED**'} |"
           for f in r["fixtures"]]
    md += [""]
    path = os.path.join(SRC_DIR, "SOURCE_MUTATION_REPORT_v1.md")
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
