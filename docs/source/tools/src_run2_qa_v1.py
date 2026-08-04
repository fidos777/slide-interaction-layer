# -*- coding: utf-8 -*-
"""Stage 4.2F-D targeted QA — only the release-critical facts this run introduced.

    SUITE_ID = STAGE_4_2F_D_RELEASE_FACTS_QA_v1
    python3 docs/source/tools/src_run2_qa_v1.py

SCOPE, AND WHAT IS DELIBERATELY OUT OF IT
-----------------------------------------
Seven areas, named by the brief: source existence, page references, unit boundaries, unit
counts, K3 assessment composition, queue readiness, extracted-row membership. Nothing else
is touched. The Stage 4.2F-C suite PROJECT_SOURCE_CUSTODY_QA_v1 keeps its own gates and its
own total; the PL06 and T04 suites keep theirs. No gate total from any of them is merged
into this one, and no historical suite is edited to agree with this one.

ORACLE SEPARATION
-----------------
ORACLE_SEPARATION_STRUCTURAL = DEFERRED_BY_DELIVERY_DEADLINE. The gates below and the code
they check still live in the same repository and the same process. What IS enforced here is
oracle INDEPENDENCE per gate: an expected value is a literal written by hand, a raw file
re-read from disk, or a quantity measured a second way — never the same function call that
produced the observed value. Seven self-referential gates have been caught in this project
so far, so each gate below names its oracle basis in `oracle_basis` and a gate whose basis
would be the value's own producer is not written at all.
"""
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
import pl06_batch1_data_v1 as B    # noqa: E402
import pl06_extract_rest_v1 as RE  # noqa: E402

SUITE_ID = "STAGE_4_2F_D_RELEASE_FACTS_QA_v1"
SIBLING_SUITES = ["PROJECT_SOURCE_CUSTODY_QA_v1", "PL06_AUTHORITY_HARVEST_BATCH1_QA_v1",
                  "T04_STATE_COVERAGE_QA_v1", "T04_STORYBOARD_QA_v1",
                  "T04_SUPPLEMENTARY_EVIDENCE_QA_v1",
                  "T04_AUTHORITY_DECISION_INGESTION_QA_v1"]

ORACLE_SEPARATION_STRUCTURAL = "DEFERRED_BY_DELIVERY_DEADLINE"
ORACLE_SEPARATION_NOTE = (
    "Gates and generators share a process. Per-gate oracle independence is enforced "
    "instead: every gate declares whether its expected value came from a hand-written "
    "LITERAL, a RAW_FILE re-read from disk, or an INDEPENDENT_MEASURE computed a different "
    "way. No gate compares a function against itself.")

EXISTENCE = "EXISTENCE"
PAGES = "PAGES"
BOUNDARY = "BOUNDARY"
COUNTS = "COUNTS"
ASSESSMENT = "ASSESSMENT"
QUEUE = "QUEUE"
MEMBERSHIP = "MEMBERSHIP"
ACCOUNTING = "ACCOUNTING"
GATE_TYPES = {EXISTENCE, PAGES, BOUNDARY, COUNTS, ASSESSMENT, QUEUE, MEMBERSHIP,
              ACCOUNTING}

LITERAL = "LITERAL"
RAW_FILE = "RAW_FILE"
INDEPENDENT_MEASURE = "INDEPENDENT_MEASURE"

# ------------------------------------------------------------------------------------
# HAND-WRITTEN ANCHORS. Typed from the nine source PDFs and the frozen map, not computed.
# If a generator changes shape, these do not move with it — that is the whole point.
# ------------------------------------------------------------------------------------
K3_MODULE_BY_PL = {"PL01": "M01", "PL02": "M01", "PL03": "M01", "PL04": "M02",
                   "PL05": "M03", "PL06": "M04", "PL07": "M05", "PL08": "M05",
                   "PL09": "M06"}
K3_PAGES_BY_PL = {"PL01": 17, "PL02": 28, "PL03": 9, "PL04": 27, "PL05": 18,
                  "PL06": 33, "PL07": 43, "PL08": 13, "PL09": 28}
K3_QUESTIONS_BY_PL = {"PL01": 3, "PL02": 5, "PL03": 3, "PL04": 5, "PL05": 5,
                      "PL06": 5, "PL07": 5, "PL08": 5, "PL09": 5}
K3_PACKAGES_LITERAL = 9
K3_MODULES_LITERAL = 6
K3_PAGES_LITERAL = 216
K3_QUESTIONS_LITERAL = 41
K3_MARK_CARRYING_PL_LITERAL = ["PL03"]

PL06_FROZEN_UNITS_LITERAL = 14
# Typed by hand from the six units delivered before this run. T02-B02 is NOT here: it is
# one of the eight extracted in this run. An earlier draft of this list included it, and
# the literal-anchored count gate below is what caught the mistake — which is the reason
# these anchors are typed rather than read back from the module they check.
PL06_ALREADY_REPRESENTED_LITERAL = ["K5-PL06-T03-B02", "K5-PL06-T03-B03",
                                    "K5-PL06-T03-B04", "K5-PL06-T04-B01",
                                    "K5-PL06-T05-B01", "K5-PL06-T06-B01"]
IMMEDIATELY_EXECUTABLE_LITERAL = 13

NOT_CHECKED = [
    "the K2 monolith's structure — the binary is still not local and the lane says so",
    "whether any provisional model is instructionally sound — that is Bariah's",
    "how the K3 decision DOCX renders in Microsoft Word — still no Writer filter here, so "
    "the one-page claim rests on the PIL preview and the OOXML parts, not on Word",
    "whether the 22 K5 candidate structures really contain the units their headings "
    "suggest — no frozen boundary map exists for them",
    "the correctness of any source content — only its structure and custody",
]


def run():
    res = []

    def chk(gid, gtype, value, expected, population, source_artifact, oracle_basis,
            empty_by_design=None):
        assert gtype in GATE_TYPES, gtype
        assert oracle_basis in (LITERAL, RAW_FILE, INDEPENDENT_MEASURE), oracle_basis
        ok = value == expected
        vacuous = population == 0 and not empty_by_design
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        population=population, source_artifact=source_artifact,
                        oracle_basis=oracle_basis, empty_by_design=empty_by_design,
                        vacuous=vacuous, ok=ok and not vacuous))

    inv = K3.k3_inventory()
    models = K3.k3_models()
    q = R2.queue_summary()
    rows = q["rows"]

    # ==================== 1. SOURCE EXISTENCE ====================
    chk("K3_PACKAGE_COUNT_MATCHES_THE_LITERAL", EXISTENCE,
        inv["pdfs"], K3_PACKAGES_LITERAL, len(A.K3_PDFS),
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    chk("EVERY_K3_PACKAGE_IS_READ_IN_FULL", EXISTENCE,
        inv["identified_not_read"], 0, inv["pdfs"],
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    chk("NO_K3_PACKAGE_CLAIMS_A_LOCAL_BINARY", EXISTENCE,
        sorted({r["binary_local"] for r in inv["rows"]}), [False], len(inv["rows"]),
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    chk("K2_REMAINS_AN_UNRESOLVED_SOURCE_RECORD_NOT_A_UNIT", EXISTENCE,
        [r["record_type"] for r in rows if r["course"] == "K2"], ["UNRESOLVED_SOURCE"],
        len([r for r in rows if r["course"] == "K2"]),
        "PRODUCTION_QUEUE_v3.json", LITERAL)
    chk("NO_ROW_USES_AN_UNQUALIFIED_ABSENCE_STATUS", EXISTENCE,
        [r["unit_or_candidate_id"] for r in rows
         if r["extraction_status"] in ("NOT_IN_CUSTODY", "SOURCE_MISSING")], [],
        len(rows), "PRODUCTION_QUEUE_v3.json", LITERAL, empty_by_design=True)

    # ==================== 2. PAGE REFERENCES ====================
    # Expected sides are typed from each PDF's own footer, not read back from the model.
    for pl, pages in sorted(K3_PAGES_BY_PL.items()):
        got = next(r["pages"] for r in inv["rows"] if r["pl"] == pl)
        chk(f"K3_{pl}_PAGE_COUNT", PAGES, got, pages, 1,
            "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    # Summed a different way from the per-package literals above.
    chk("K3_TOTAL_PAGES_AGREES_WITH_THE_SUM_OF_THE_LITERALS", PAGES,
        inv["total_source_pages"], sum(K3_PAGES_BY_PL.values()), len(K3_PAGES_BY_PL),
        "K3_SOURCE_INVENTORY_v2.json", INDEPENDENT_MEASURE)
    chk("K3_TOTAL_PAGES_MATCHES_THE_STANDALONE_LITERAL", PAGES,
        inv["total_source_pages"], K3_PAGES_LITERAL, len(K3_PAGES_BY_PL),
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    recon = R2.t04_page_reconciliation()
    chk("T04_PAGE_RECONCILIATION_STILL_SAYS_DO_NOT_REGENERATE", PAGES,
        recon["regeneration_decision"]["regenerate"], False, recon["rows_total"],
        "T04_PAGE_REFERENCE_RECONCILIATION_v1.json", LITERAL)
    chk("T04_MISMATCH_COUNT_UNCHANGED_BY_THIS_RUN", PAGES,
        recon["mismatches"], 32, recon["rows_total"],
        "T04_PAGE_REFERENCE_RECONCILIATION_v1.json", LITERAL)
    chk("T04_ROWS_ACCOUNT_FOR_THEMSELVES", PAGES,
        recon["rows_resolved"] + recon["rows_unresolved"], recon["rows_total"],
        recon["rows_total"], "T04_PAGE_REFERENCE_RECONCILIATION_v1.json",
        INDEPENDENT_MEASURE)

    # ==================== 3. UNIT BOUNDARIES ====================
    # Re-read from the frozen JSON on disk, not from the extractor that consumes it.
    with open(B.BOUNDARY_MAP_PATH, encoding="utf-8") as fh:
        raw_map = json.load(fh)
    raw_units = raw_map["lessons"]
    chk("FROZEN_BOUNDARY_MAP_STILL_HOLDS_FOURTEEN_UNITS", BOUNDARY,
        len(raw_units), PL06_FROZEN_UNITS_LITERAL, len(raw_units),
        os.path.basename(B.BOUNDARY_MAP_PATH), RAW_FILE)
    chk("FROZEN_BOUNDARY_MAP_HASH_UNCHANGED", BOUNDARY,
        B._sha256(B.BOUNDARY_MAP_PATH), B.BOUNDARY_MAP_SHA256, 1,
        os.path.basename(B.BOUNDARY_MAP_PATH), LITERAL)
    remaining = RE.remaining_units()
    represented = sorted(RE.ALREADY_REPRESENTED)
    chk("REMAINING_PLUS_REPRESENTED_ACCOUNTS_FOR_EVERY_FROZEN_UNIT", BOUNDARY,
        len(remaining) + len(represented), PL06_FROZEN_UNITS_LITERAL,
        len(raw_units), "pl06_extract_rest_v1.remaining_units", LITERAL)
    # This gate replaces an earlier one that asked whether the remaining set and the
    # represented set overlapped. They never can: remaining is DEFINED as frozen minus
    # represented, so the gate was comparing a derivation against its own input and
    # could not fail — fixture DB-02 walked straight past it. The expected side is now
    # built from the raw frozen map on disk and the hand-typed represented list, neither
    # of which moves when the module does.
    frozen_unit_ids = sorted(u["unit_id"] for u in raw_units)
    chk("REMAINING_UNITS_EQUAL_FROZEN_MAP_MINUS_THE_REPRESENTED_LITERAL", BOUNDARY,
        sorted(u["unit_id"] for u in remaining),
        [i for i in frozen_unit_ids if i not in PL06_ALREADY_REPRESENTED_LITERAL],
        len(frozen_unit_ids), "pl06_extract_rest_v1.remaining_units", RAW_FILE)
    chk("THE_REPRESENTED_SET_MATCHES_THE_HAND_TYPED_LITERAL", BOUNDARY,
        sorted(represented), sorted(PL06_ALREADY_REPRESENTED_LITERAL),
        len(PL06_ALREADY_REPRESENTED_LITERAL),
        "pl06_extract_rest_v1.ALREADY_REPRESENTED", LITERAL)

    # ==================== 4. UNIT COUNTS ====================
    chk("K3_MODEL_COUNT_EQUALS_PACKAGES_READ", COUNTS,
        len(models), K3_PACKAGES_LITERAL, K3_PACKAGES_LITERAL,
        "K3_PROVISIONAL_MODELS_v2.json", LITERAL)
    chk("K3_MODULE_COUNT_MATCHES_THE_LITERAL", COUNTS,
        len(inv["modules_evidenced"]), K3_MODULES_LITERAL, inv["pdfs"],
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    # Per-package module code, typed from each PDF's own KOD MODUL line.
    chk("EVERY_K3_MODULE_CODE_MATCHES_ITS_SOURCE_FRONT_MATTER", COUNTS,
        {r["pl"]: r["module_code"] for r in inv["rows"]}, K3_MODULE_BY_PL, inv["pdfs"],
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    chk("NO_K3_UNIT_ID_IS_STILL_STAMPED_M01_BY_DEFAULT", COUNTS,
        sorted(r["unit_or_candidate_id"] for r in rows
               if r["course"] == "K3" and r["unit_or_candidate_id"]
               != f"K3-{K3_MODULE_BY_PL[r['pl']]}-{r['pl']}"), [],
        len([r for r in rows if r["course"] == "K3"]),
        "PRODUCTION_QUEUE_v3.json", LITERAL, empty_by_design=True)
    chk("THE_QUEUE_AND_THE_K3_MODEL_NAME_EVERY_UNIT_THE_SAME_WAY", COUNTS,
        sorted(r["unit_or_candidate_id"] for r in rows if r["course"] == "K3"),
        sorted(m["unit_id"] for m in models), len(models),
        "PRODUCTION_QUEUE_v3.json", INDEPENDENT_MEASURE)
    chk("REMAINING_PL06_UNIT_COUNT_IS_NOT_AN_ASSUMED_8_10_OR_12", COUNTS,
        len(remaining), PL06_FROZEN_UNITS_LITERAL - len(PL06_ALREADY_REPRESENTED_LITERAL),
        PL06_FROZEN_UNITS_LITERAL, "pl06_extract_rest_v1.remaining_units",
        INDEPENDENT_MEASURE)

    # ==================== 5. K3 ASSESSMENT COMPOSITION ====================
    chk("EVERY_K3_MODEL_DEFERS_ASSESSMENT_TO_THE_COURSE_RULE", ASSESSMENT,
        sorted({m["source_assessment"]["cls"] for m in models}),
        ["PENDING_K3_COURSE_ASSESSMENT_RULE"], len(models),
        "K3_PROVISIONAL_MODELS_v2.json", LITERAL)
    chk("THE_K5_RULE_IS_NOT_APPLIED_TO_K3", ASSESSMENT,
        inv["k5_rule_not_applied"]["applied_to_k3"], False, len(models),
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    chk("NO_K3_ANSWER_KEY_IS_MARKED_APPROVED", ASSESSMENT,
        sorted({m["source_assessment"]["key_status"] for m in models}),
        ["SOURCE_AUTHORED_NOT_STORYBOARD_APPROVED"], len(models),
        "K3_PROVISIONAL_MODELS_v2.json", LITERAL)
    chk("EVERY_K3_QUESTION_COUNT_MATCHES_ITS_SOURCE", ASSESSMENT,
        {r["pl"]: r["latihan_questions"] for r in inv["rows"]}, K3_QUESTIONS_BY_PL,
        inv["pdfs"], "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    chk("K3_TOTAL_QUESTIONS_MATCHES_THE_LITERAL", ASSESSMENT,
        inv["total_source_questions"], K3_QUESTIONS_LITERAL, inv["pdfs"],
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    # Also replaces a self-referential predecessor. The old gate asked whether this
    # file's own K3_QUESTIONS_BY_PL constant held more than one distinct value, which is
    # a property of the QA file and nothing else — fixture DA-05 flattened the model to a
    # uniform five and the gate never noticed. Both sides now come from the model, with
    # the expected count taken from the literals.
    chk("THE_MODEL_DOES_NOT_CLAIM_A_UNIFORM_QUESTION_COUNT", ASSESSMENT,
        len({r["latihan_questions"] for r in inv["rows"]}),
        len(set(K3_QUESTIONS_BY_PL.values())), inv["pdfs"],
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    # The shape record and the package record count questions by different routes. If
    # either is edited alone they stop agreeing, and that is the failure worth catching.
    chk("SHAPE_AND_PACKAGE_QUESTION_COUNTS_AGREE", ASSESSMENT,
        inv["question_counts_all_agree"], True, inv["pdfs"],
        "K3_SOURCE_INVENTORY_v2.json", INDEPENDENT_MEASURE)
    chk("ONLY_PL03_CARRIES_MARK_ALLOCATIONS", ASSESSMENT,
        sorted(pl for pl, s in K3.SKEMA_SHAPES.items() if s["carries_marks"]),
        K3_MARK_CARRYING_PL_LITERAL, len(K3.SKEMA_SHAPES),
        "K3_SOURCE_INVENTORY_v2.json", LITERAL)
    chk("THE_DECISION_OFFERS_FOUR_OPTIONS_AND_NO_CAIR_PICK", ASSESSMENT,
        [[o["key"] for o in K3.K3_COURSE_DECISION["options"]],
         K3.K3_COURSE_DECISION["cair_recommendation"]],
        [["A", "B", "C", "D"], None], 1, "K3_COURSE_DECISION_v1.json", LITERAL)
    chk("THE_DECISION_DOES_NOT_BLOCK_SOURCE_OR_VISUAL_WORK", ASSESSMENT,
        sorted(K3.K3_COURSE_DECISION["does_not_block"]),
        sorted(["source reading", "content extraction", "visual modelling",
                "screen modelling"]), 4, "K3_COURSE_DECISION_v1.json", LITERAL)

    # ==================== 6. QUEUE READINESS ====================
    c = q["counts"]
    chk("IMMEDIATELY_EXECUTABLE_MATCHES_THE_LITERAL", QUEUE,
        c["immediately_executable_units"], IMMEDIATELY_EXECUTABLE_LITERAL, len(rows),
        "PRODUCTION_QUEUE_v3.json", LITERAL)
    chk("NOTHING_IS_READY_TO_EMIT_PPTX_YET", QUEUE,
        c["ready_to_emit_units"], 0, len(rows), "PRODUCTION_QUEUE_v3.json", LITERAL)
    chk("NO_IMMEDIATELY_EXECUTABLE_UNIT_LACKS_A_READABLE_BINARY", QUEUE,
        sorted(r["unit_or_candidate_id"] for r in rows
               if r["immediately_executable"] and not r["binary_readable"]), [],
        len(rows), "PRODUCTION_QUEUE_v3.json", LITERAL, empty_by_design=True)
    chk("NO_CONNECTOR_ONLY_ROW_IS_IMMEDIATELY_EXECUTABLE", QUEUE,
        sorted(r["unit_or_candidate_id"] for r in rows
               if r["immediately_executable"]
               and r["extraction_status"] == "SOURCE_LOCATED_BY_CONNECTOR"), [],
        len(rows), "PRODUCTION_QUEUE_v3.json", LITERAL, empty_by_design=True)
    chk("EXTRACTED_IS_NOT_CONFLATED_WITH_CONNECTOR_READ", QUEUE,
        c["extracted_units"] + c["source_content_read_units"] > c["extracted_units"],
        True, len(rows), "PRODUCTION_QUEUE_v3.json", INDEPENDENT_MEASURE)
    chk("EXTRACTED_COUNT_EQUALS_THE_FROZEN_PL06_UNIT_COUNT", QUEUE,
        c["extracted_units"], PL06_FROZEN_UNITS_LITERAL, len(rows),
        "PRODUCTION_QUEUE_v3.json", LITERAL)
    chk("SOURCE_CONTENT_READ_COUNT_EQUALS_THE_K3_PACKAGE_COUNT", QUEUE,
        c["source_content_read_units"], K3_PACKAGES_LITERAL, len(rows),
        "PRODUCTION_QUEUE_v3.json", LITERAL)
    chk("RECORD_TYPES_PARTITION_THE_QUEUE_EXACTLY", QUEUE,
        c["confirmed_production_units"] + c["candidate_structures"]
        + c["unresolved_source_records"], c["total_rows"], len(rows),
        "PRODUCTION_QUEUE_v3.json", INDEPENDENT_MEASURE)
    chk("NOT_EVERY_UNRESOLVED_ROW_IS_CALLED_A_CANDIDATE_UNIT", QUEUE,
        c["candidate_structures"] < len(rows), True, len(rows),
        "PRODUCTION_QUEUE_v3.json", LITERAL)
    # The retired 97.8 percent figure must not be usable as a live number, but the record
    # that RETIRES it has to be free to name it — otherwise the queue would quietly drop
    # the evidence that it was ever wrong. So the gate asks where it appears, not whether.
    chk("THE_RETIRED_97_8_PERCENT_METRIC_APPEARS_ONLY_IN_ITS_RETIREMENT_RECORD", QUEUE,
        sorted(k for k, v in q.items()
               if "97.8" in json.dumps(v, ensure_ascii=False, default=str)),
        ["alias_map"], len(q), "PRODUCTION_QUEUE_v3.json", LITERAL)
    chk("NO_LIVE_COUNT_OR_HEADLINE_CARRIES_A_TYPED_PERCENTAGE", QUEUE,
        [k for k in ("counts", "headline", "rows")
         if "%" in json.dumps(q[k], ensure_ascii=False, default=str)
         or "percent" in json.dumps(q[k], ensure_ascii=False, default=str).lower()], [],
        3, "PRODUCTION_QUEUE_v3.json", LITERAL, empty_by_design=True)
    chk("NO_ROW_CLAIMS_PRODUCTION_APPROVED_OR_CANONICAL_FREEZE", QUEUE,
        [t for t in ("PRODUCTION_APPROVED", "CANONICAL_FREEZE", "SOURCE_UNSUPPORTED",
                     "BARIAH_ORIGINATED_RULE")
         if t in json.dumps(q, ensure_ascii=False, default=str)], [],
        len(rows), "PRODUCTION_QUEUE_v3.json", LITERAL, empty_by_design=True)

    # ==================== 7. EXTRACTED-ROW MEMBERSHIP ====================
    # The queue's K3 ids are checked against the model's ids above; here the PL06 side is
    # checked against the frozen map re-read from disk.
    frozen_ids = sorted(u["unit_id"] for u in raw_units)
    queue_pl06_ids = sorted(r["unit_or_candidate_id"] for r in rows
                            if r["course"] == "K5" and r["extraction_status"]
                            == "EXTRACTED")
    chk("EVERY_EXTRACTED_QUEUE_ROW_IS_A_FROZEN_MAP_UNIT", MEMBERSHIP,
        [i for i in queue_pl06_ids if i not in frozen_ids], [], len(queue_pl06_ids),
        "PRODUCTION_QUEUE_v3.json", RAW_FILE, empty_by_design=True)
    chk("EVERY_FROZEN_MAP_UNIT_APPEARS_AS_AN_EXTRACTED_QUEUE_ROW", MEMBERSHIP,
        [i for i in frozen_ids if i not in queue_pl06_ids], [], len(frozen_ids),
        "PRODUCTION_QUEUE_v3.json", RAW_FILE, empty_by_design=True)
    chk("NO_K3_ROW_CLAIMS_EXTRACTED_STATUS", MEMBERSHIP,
        sorted(r["unit_or_candidate_id"] for r in rows
               if r["course"] == "K3" and r["extraction_status"] == "EXTRACTED"), [],
        len([r for r in rows if r["course"] == "K3"]),
        "PRODUCTION_QUEUE_v3.json", LITERAL, empty_by_design=True)

    # ==================== 8. ACCOUNTING ====================
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID,
        "STAGE_4_2F_D_RELEASE_FACTS_QA_v1", 1, "this file", LITERAL)
    chk("SUITE_ID_IS_NOT_ANY_SIBLING_SUITE", ACCOUNTING,
        SUITE_ID in SIBLING_SUITES, False, len(SIBLING_SUITES), "this file", LITERAL)
    chk("ORACLE_SEPARATION_IS_RECORDED_AS_DEFERRED", ACCOUNTING,
        ORACLE_SEPARATION_STRUCTURAL, "DEFERRED_BY_DELIVERY_DEADLINE", 1,
        "this file", LITERAL)
    chk("EVERY_GATE_DECLARES_AN_ORACLE_BASIS", ACCOUNTING,
        sorted({r["oracle_basis"] for r in res}),
        sorted([LITERAL, RAW_FILE, INDEPENDENT_MEASURE]), len(res), "this file",
        INDEPENDENT_MEASURE)
    chk("NO_GATE_IS_VACUOUS", ACCOUNTING,
        [r["gate_id"] for r in res if r["vacuous"]], [], len(res), "this file", LITERAL,
        empty_by_design=True)
    return res


def summary():
    res = run()
    return dict(suite_id=SUITE_ID, total=len(res),
                passed=len([r for r in res if r["ok"]]),
                failed=[r for r in res if not r["ok"]],
                by_type={t: len([r for r in res if r["gate_type"] == t])
                         for t in sorted(GATE_TYPES)},
                by_oracle_basis={b: len([r for r in res if r["oracle_basis"] == b])
                                 for b in (LITERAL, RAW_FILE, INDEPENDENT_MEASURE)},
                oracle_separation_structural=ORACLE_SEPARATION_STRUCTURAL,
                oracle_separation_note=ORACLE_SEPARATION_NOTE,
                not_checked=NOT_CHECKED, gates=res)


if __name__ == "__main__":
    s = summary()
    print(f"SUITE_ID = {s['suite_id']}")
    print(f"{s['passed']}/{s['total']} passed")
    print("by type:", s["by_type"])
    print("by oracle basis:", s["by_oracle_basis"])
    print("ORACLE_SEPARATION_STRUCTURAL =", s["oracle_separation_structural"])
    for f in s["failed"]:
        print(f"  FAIL {f['gate_id']}: {f['value']!r} != {f['expected']!r} "
              f"(population {f['population']}, vacuous={f['vacuous']})")
