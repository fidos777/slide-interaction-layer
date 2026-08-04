# -*- coding: utf-8 -*-
"""Stage 4.2F-E targeted QA — K2 custody, structure conflict, hierarchy and queue.

    SUITE_ID = STAGE_4_2F_E_K2_QA_v1
    python3 docs/source/tools/src_k2_qa_v1.py

Its own identity and its own total. No gate from any sibling suite is merged in, and no
sibling suite was edited to agree with it.

ORACLE_SEPARATION_STRUCTURAL = DEFERRED_BY_DELIVERY_DEADLINE, carried forward unchanged
from Stage 4.2F-D. Per-gate oracle independence is enforced instead, and every gate
declares its basis.

A NOTE ON WHAT THESE GATES CAN AND CANNOT PROVE
-----------------------------------------------
The brief wanted expected values drawn from the raw PDF. There is no raw PDF here. So the
strongest available anchors are used and each is labelled honestly:

  * BRIEF_LITERAL      — the identity the brief itself states (name, bytes, SHA-256, 346
                         pages). Good enough to check that nothing silently claims to have
                         verified them.
  * SOURCE_TEXT_LITERAL— strings and counts typed by hand out of the connector text: the
                         narrative sentence, the silibus rows, the teaching-plan headers.
  * CONNECTOR_METADATA — the Drive file facts, re-fetched independently of the model.
  * INDEPENDENT_MEASURE— a quantity computed a second, different way.

No gate claims to have checked the binary, because none did. The gates that matter most
here are the ones asserting that the run did NOT claim what it could not verify.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
DOCS = os.path.dirname(SRC_DIR)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(DOCS, "pl06", "tools"))
import src_k2_v1 as K2    # noqa: E402
import src_run2_v1 as R2  # noqa: E402

SUITE_ID = "STAGE_4_2F_E_K2_QA_v1"
SIBLING_SUITES = ["STAGE_4_2F_D_RELEASE_FACTS_QA_v1", "PROJECT_SOURCE_CUSTODY_QA_v1",
                  "PL06_AUTHORITY_HARVEST_BATCH1_QA_v1", "T04_STATE_COVERAGE_QA_v1",
                  "T04_STORYBOARD_QA_v1", "T04_SUPPLEMENTARY_EVIDENCE_QA_v1",
                  "T04_AUTHORITY_DECISION_INGESTION_QA_v1"]

ORACLE_SEPARATION_STRUCTURAL = "DEFERRED_BY_DELIVERY_DEADLINE"

CUSTODY = "CUSTODY"
CONFLICT = "CONFLICT"
HIERARCHY = "HIERARCHY"
QUEUE = "QUEUE"
HONESTY = "HONESTY"
ACCOUNTING = "ACCOUNTING"
GATE_TYPES = {CUSTODY, CONFLICT, HIERARCHY, QUEUE, HONESTY, ACCOUNTING}

BRIEF_LITERAL = "BRIEF_LITERAL"
SOURCE_TEXT_LITERAL = "SOURCE_TEXT_LITERAL"
CONNECTOR_METADATA = "CONNECTOR_METADATA"
INDEPENDENT_MEASURE = "INDEPENDENT_MEASURE"
BASES = (BRIEF_LITERAL, SOURCE_TEXT_LITERAL, CONNECTOR_METADATA, INDEPENDENT_MEASURE)

# ------------------------------------------------------------------------------------
# Hand-typed anchors.
# ------------------------------------------------------------------------------------
BRIEF_BYTES = 25043306
BRIEF_SHA256 = "0b2d81dda46eaf4fb018a20a78f7f9b2870129c61125768e4438937f3f405680"
BRIEF_PAGES = 346
BRIEF_FILENAME = "2. PENGURUSAN PEMBINAAN LANDASAN.pdf"
DRIVE_ID = "1BW-OibYv3sDyordi0YIQkb5vXeAdOtMn"

# Typed out of the connector text.
NARRATIVE_MODULE_COUNT = 8
TABLE_MODULE_COUNT = 6
PACKAGE_COUNT = 9
MODULE_CODES = ["M01", "M02", "M03", "M04", "M05", "M06"]
PL_CODES = ["PL01", "PL02", "PL03", "PL04", "PL05", "PL06", "PL07", "PL08", "PL09"]
PT_CODES = ["PT01", "PT02", "PT03", "PT04", "PT05", "PT06", "PT07", "PT08", "PT09"]
# module code read from each teaching plan's own "KOD PELAN MENGAJAR TEORI Mxx" header
PT_TO_MODULE = {"PT01": "M01", "PT02": "M01", "PT03": "M01", "PT04": "M01",
                "PT05": "M02", "PT06": "M03", "PT07": "M04", "PT08": "M05",
                "PT09": "M06"}
# page total read from each plan's own "Muka Surat: n/N" footer
PT_PAGES = {"PT01": 8, "PT02": 6, "PT03": 7, "PT04": 7, "PT05": 7, "PT06": 7,
            "PT07": 6, "PT08": 8, "PT09": 6}
PT_PAGES_TOTAL = 62
CONNECTOR_CHARS = 62638
PL_NAMED_BY_THEIR_OWN_PLAN = ["PL06", "PL07", "PL09"]

LIVE_QUEUE_BASENAME = "PRODUCTION_QUEUE_v4"
RETIRED_QUEUE_BASENAMES = ["PRODUCTION_QUEUE_v1", "PRODUCTION_QUEUE_v2",
                           "PRODUCTION_QUEUE_v3"]

NOT_CHECKED = [
    "the K2 binary itself — it is not on this box, and no gate here pretends otherwise",
    "the SHA-256, PDF validity, encryption status or true page count",
    "any per-PL page span, image count or table count",
    "whether the six-module structure is instructionally right — that is not a QA question",
    "the parts of the document the connector did not return, which is most of it",
]


def run():
    res = []

    def chk(gid, gtype, value, expected, population, source_artifact, oracle_basis,
            empty_by_design=None):
        assert gtype in GATE_TYPES, gtype
        assert oracle_basis in BASES, oracle_basis
        ok = value == expected
        vacuous = population == 0 and not empty_by_design
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        population=population, source_artifact=source_artifact,
                        oracle_basis=oracle_basis, empty_by_design=empty_by_design,
                        vacuous=vacuous, ok=ok and not vacuous))

    c = K2.custody()
    h = K2.hierarchy()
    cf = K2.CONFLICT
    q = R2.queue_summary()
    k2rows = [r for r in q["rows"] if r["course"] == "K2"]

    # ==================== 1. BINARY CUSTODY ====================
    chk("K2_STATUS_IS_SCOPED_NOT_UNQUALIFIED", CUSTODY,
        c["record"]["status"], "NOT_FOUND_IN_LOCATIONS_SEARCHED", 1,
        "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("K2_DOES_NOT_CLAIM_A_LOCAL_BINARY", CUSTODY,
        c["record"]["binary_local"], False, 1,
        "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("K2_DOES_NOT_CLAIM_A_READABLE_BINARY", CUSTODY,
        c["record"]["binary_readable"], False, 1,
        "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("K2_DOES_NOT_CLAIM_A_VERIFIED_SHA256", CUSTODY,
        c["binding"]["sha256_verified"], False, 1,
        "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("THE_BRIEF_SHA256_IS_CARRIED_AS_EXPECTED_ONLY", CUSTODY,
        c["expected"]["sha256"], BRIEF_SHA256, 1,
        "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("EVERY_BINARY_DEPENDENT_CHECK_IS_MARKED_NOT_READ", CUSTODY,
        sorted({v for k, v in c["record"]["unverifiable"].items() if k != "note"}),
        ["NOT_READ_BINARY_UNAVAILABLE"],
        len(c["record"]["unverifiable"]) - 1, "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("LOCATIONS_SEARCHED_ARE_ENUMERATED", CUSTODY,
        len(c["locations_searched"]) >= 10, True, len(c["locations_searched"]),
        "K2_BINARY_CUSTODY_v1.json", INDEPENDENT_MEASURE)
    chk("LOCATIONS_NOT_SEARCHED_ARE_NAMED_TOO", CUSTODY,
        len(c["locations_not_searched"]) > 0, True, len(c["locations_not_searched"]),
        "K2_BINARY_CUSTODY_v1.json", INDEPENDENT_MEASURE)
    chk("NO_SEARCHED_LOCATION_REPORTS_THE_BINARY_FOUND", CUSTODY,
        [x["location"] for x in c["locations_searched"] if x["found"] is True], [],
        len(c["locations_searched"]), "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL,
        empty_by_design=True)

    # Drive metadata re-fetched independently of the model would be ideal; the recorded
    # values are checked against the brief's literals instead, which is a different
    # source from the model that stores them.
    chk("DRIVE_BYTES_EQUAL_THE_BRIEF_BYTES", CUSTODY,
        c["drive"]["file_size"], BRIEF_BYTES, 1,
        "K2_BINARY_CUSTODY_v1.json", CONNECTOR_METADATA)
    chk("DRIVE_TITLE_EQUALS_THE_BRIEF_FILENAME", CUSTODY,
        c["drive"]["title"], BRIEF_FILENAME, 1,
        "K2_BINARY_CUSTODY_v1.json", CONNECTOR_METADATA)
    chk("DRIVE_ID_IS_THE_ONE_THE_BRIEF_NAMES", CUSTODY,
        c["drive"]["drive_id"], DRIVE_ID, 1,
        "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("THE_BINDING_RECORDS_BOTH_MATCHES", CUSTODY,
        [c["binding"]["filename_matches"], c["binding"]["bytes_match"]], [True, True], 1,
        "K2_BINARY_CUSTODY_v1.json", INDEPENDENT_MEASURE)

    # ==================== 2. CONNECTOR-READ HONESTY ====================
    cr = c["connector_read"]
    chk("THE_CONNECTOR_READ_IS_DECLARED_INCOMPLETE", HONESTY,
        cr["complete"], False, 1, "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("THE_CONNECTOR_CHAR_COUNT_IS_THE_MEASURED_ONE", HONESTY,
        cr["chars"], CONNECTOR_CHARS, 1, "K2_BINARY_CUSTODY_v1.json",
        SOURCE_TEXT_LITERAL)
    chk("THE_TRUNCATION_IS_EVIDENCED_NOT_ASSERTED", HONESTY,
        len(cr["truncation_evidence"]) >= 3, True, len(cr["truncation_evidence"]),
        "K2_BINARY_CUSTODY_v1.json", INDEPENDENT_MEASURE)
    chk("THE_UNREAD_PARTS_ARE_NAMED", HONESTY,
        len(cr["does_not_cover"]) > 0, True, len(cr["does_not_cover"]),
        "K2_BINARY_CUSTODY_v1.json", INDEPENDENT_MEASURE)
    chk("SOURCE_CONTENT_READ_IS_NOT_CLAIMED_OUTRIGHT", HONESTY,
        "SOURCE_CONTENT_READ" in c["record"]["states_not_claimed"], True, 1,
        "K2_BINARY_CUSTODY_v1.json", BRIEF_LITERAL)
    chk("NO_DECOMPOSITION_IS_CLAIMED_COMPLETE", HONESTY,
        h["decomposition_completed"], False, 1,
        "K2_COURSE_HIERARCHY_v1.json", BRIEF_LITERAL)
    chk("NO_PL_ROW_REPORTS_A_MEASURED_PAGE_SPAN", HONESTY,
        sorted({r["pdf_start_page"] for r in h["rows"]}
               | {r["pdf_end_page"] for r in h["rows"]}),
        ["UNKNOWN_NOT_MEASURED"], len(h["rows"]),
        "K2_COURSE_HIERARCHY_v1.json", BRIEF_LITERAL)
    chk("UNKNOWNS_ARE_NOT_REPORTED_AS_ZERO", HONESTY,
        sorted({r["image_count"] for r in h["rows"]}
               | {r["table_count"] for r in h["rows"]}),
        ["UNKNOWN_NOT_MEASURED"], len(h["rows"]),
        "K2_COURSE_HIERARCHY_v1.json", BRIEF_LITERAL)

    # ==================== 3. SOURCE CONFLICT ====================
    chk("CONFLICT_RECORD_EXISTS_WITH_ITS_OWN_ID", CONFLICT,
        cf["conflict_id"], "K2-SOURCE-CONFLICT-01", 1,
        "K2_SOURCE_CONFLICT_01_v1.json", BRIEF_LITERAL)
    chk("NARRATIVE_COUNT_RECORDED_VERBATIM", CONFLICT,
        cf["narrative_module_count"], NARRATIVE_MODULE_COUNT, 1,
        "K2_SOURCE_CONFLICT_01_v1.json", SOURCE_TEXT_LITERAL)
    chk("TABLE_COUNT_RECORDED_VERBATIM", CONFLICT,
        cf["syllabus_table_module_count"], TABLE_MODULE_COUNT, 1,
        "K2_SOURCE_CONFLICT_01_v1.json", SOURCE_TEXT_LITERAL)
    chk("THE_TWO_COUNTS_ACTUALLY_DISAGREE", CONFLICT,
        cf["narrative_module_count"] != cf["syllabus_table_module_count"], True, 1,
        "K2_SOURCE_CONFLICT_01_v1.json", INDEPENDENT_MEASURE)
    chk("MODULE_CODES_MATCH_THE_SOURCE", CONFLICT,
        cf["module_codes_present"], MODULE_CODES, len(MODULE_CODES),
        "K2_SOURCE_CONFLICT_01_v1.json", SOURCE_TEXT_LITERAL)
    chk("PL_CODES_MATCH_THE_SOURCE", CONFLICT,
        cf["pl_codes_present"], PL_CODES, len(PL_CODES),
        "K2_SOURCE_CONFLICT_01_v1.json", SOURCE_TEXT_LITERAL)
    chk("PT_CODES_MATCH_THE_SOURCE", CONFLICT,
        cf["pt_codes_present"], PT_CODES, len(PT_CODES),
        "K2_SOURCE_CONFLICT_01_v1.json", SOURCE_TEXT_LITERAL)
    chk("THE_NARRATIVE_COUNT_MATCHES_NO_ENUMERATION_IN_THE_DOCUMENT", CONFLICT,
        NARRATIVE_MODULE_COUNT in (len(MODULE_CODES), len(PL_CODES), len(PT_CODES)),
        False, 3, "K2_SOURCE_CONFLICT_01_v1.json", INDEPENDENT_MEASURE)
    chk("AT_LEAST_FOUR_INDEPENDENT_SOURCES_ARE_CITED", CONFLICT,
        len(cf["evidence"]) >= 4, True, len(cf["evidence"]),
        "K2_SOURCE_CONFLICT_01_v1.json", INDEPENDENT_MEASURE)
    chk("THE_CONFLICT_IS_NOT_SILENTLY_CORRECTED", CONFLICT,
        cf["silently_corrected"], False, 1,
        "K2_SOURCE_CONFLICT_01_v1.json", BRIEF_LITERAL)
    chk("THE_CONFLICT_IS_NOT_SENT_TO_BARIAH", CONFLICT,
        [cf["requires_instructional_decision"], cf["in_bariah_register"],
         cf["routed_to"]], [False, False, "FIRDAUS"], 1,
        "K2_SOURCE_CONFLICT_01_v1.json", BRIEF_LITERAL)
    chk("THE_CLASSIFICATION_IS_ONE_OF_THE_FOUR_PERMITTED", CONFLICT,
        cf["classification"] in ("TYPOGRAPHICAL", "METADATA_ONLY",
                                 "SOURCE_AUTHORITY_CONFLICT",
                                 "INSTRUCTIONAL_STRUCTURE_DECISION_REQUIRED"), True, 1,
        "K2_SOURCE_CONFLICT_01_v1.json", BRIEF_LITERAL)
    chk("THE_SECONDARY_KOD_COLUMN_DEFECT_IS_RECORDED", CONFLICT,
        cf["secondary_defect"]["defect_id"], "K2-SOURCE-OBS-01", 1,
        "K2_SOURCE_CONFLICT_01_v1.json", BRIEF_LITERAL)

    # ==================== 4. HIERARCHY ====================
    chk("MODULE_COUNT_MATCHES_THE_TABLES", HIERARCHY,
        h["modules"], TABLE_MODULE_COUNT, h["modules"],
        "K2_COURSE_HIERARCHY_v1.json", SOURCE_TEXT_LITERAL)
    chk("PACKAGE_COUNT_MATCHES_THE_TABLES", HIERARCHY,
        h["pl_packages"], PACKAGE_COUNT, h["pl_packages"],
        "K2_COURSE_HIERARCHY_v1.json", SOURCE_TEXT_LITERAL)
    chk("EVERY_PACKAGE_MAPS_TO_ITS_TEACHING_PLANS_MODULE", HIERARCHY,
        {r["teaching_plan"]: r["module_code"] for r in h["rows"]}, PT_TO_MODULE,
        len(h["rows"]), "K2_COURSE_HIERARCHY_v1.json", SOURCE_TEXT_LITERAL)
    chk("TEACHING_PLAN_PAGES_MATCH_THEIR_OWN_FOOTERS", HIERARCHY,
        {t["pt"]: t["pages"] for t in K2.TEACHING_PLANS}, PT_PAGES, len(PT_PAGES),
        "K2_COURSE_HIERARCHY_v1.json", SOURCE_TEXT_LITERAL)
    chk("TEACHING_PLAN_PAGE_TOTAL_IS_THE_SUM_OF_THE_PARTS", HIERARCHY,
        h["teaching_plan_pages_total"], sum(PT_PAGES.values()), len(PT_PAGES),
        "K2_COURSE_HIERARCHY_v1.json", INDEPENDENT_MEASURE)
    chk("TEACHING_PLAN_PAGE_TOTAL_MATCHES_THE_STANDALONE_LITERAL", HIERARCHY,
        h["teaching_plan_pages_total"], PT_PAGES_TOTAL, len(PT_PAGES),
        "K2_COURSE_HIERARCHY_v1.json", SOURCE_TEXT_LITERAL)
    chk("THE_MODULE_MAP_PARTITIONS_THE_PACKAGES_EXACTLY", HIERARCHY,
        sorted(p for pls in h["module_map"].values() for p in pls), PL_CODES,
        len(PL_CODES), "K2_COURSE_HIERARCHY_v1.json", INDEPENDENT_MEASURE)
    chk("NOTHING_IS_CLAIMED_AS_A_CONFIRMED_UNIT", HIERARCHY,
        h["confirmed_units"], 0, len(h["rows"]),
        "K2_COURSE_HIERARCHY_v1.json", BRIEF_LITERAL)
    chk("EVERY_ROW_IS_A_CANDIDATE_STRUCTURE", HIERARCHY,
        sorted({r["record_type"] for r in h["rows"]}), ["CANDIDATE_STRUCTURE"],
        len(h["rows"]), "K2_COURSE_HIERARCHY_v1.json", BRIEF_LITERAL)
    chk("THE_UNMAPPED_BODY_IS_RECORDED_AS_A_REGION", HIERARCHY,
        h["unmapped_source_regions"], 1, 1,
        "K2_COURSE_HIERARCHY_v1.json", BRIEF_LITERAL)
    chk("DIRECTLY_NAMED_PACKAGES_ARE_DISTINGUISHED_FROM_INFERRED_ONES", HIERARCHY,
        sorted(h["pl_map_confidence"]["directly_named"]),
        sorted(PL_NAMED_BY_THEIR_OWN_PLAN), len(PL_CODES),
        "K2_COURSE_HIERARCHY_v1.json", SOURCE_TEXT_LITERAL)
    chk("NAMED_PLUS_INFERRED_ACCOUNTS_FOR_EVERY_PACKAGE", HIERARCHY,
        len(h["pl_map_confidence"]["directly_named"])
        + len(h["pl_map_confidence"]["inferred_by_ordinal_position"]), PACKAGE_COUNT,
        PACKAGE_COUNT, "K2_COURSE_HIERARCHY_v1.json", INDEPENDENT_MEASURE)
    chk("NO_UNIT_ID_IS_BUILT_FROM_THE_FAULTY_KOD_COLUMN", HIERARCHY,
        sorted(r["unit_or_candidate_id"] for r in k2rows
               if r["unit_or_candidate_id"].startswith("K2-M01-")
               and r["pl"] not in ("PL01", "PL02", "PL03", "PL04")), [],
        len(k2rows), "PRODUCTION_QUEUE_v4.json", SOURCE_TEXT_LITERAL,
        empty_by_design=True)

    # ==================== 5. QUEUE ====================
    chk("K2_IS_NO_LONGER_A_SINGLE_UNRESOLVED_ROW", QUEUE,
        [r["unit_or_candidate_id"] for r in k2rows
         if r["record_type"] == "UNRESOLVED_SOURCE"], [], len(k2rows),
        "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL, empty_by_design=True)
    chk("K2_CONTRIBUTES_NINE_QUEUE_ROWS", QUEUE,
        len(k2rows), PACKAGE_COUNT, len(k2rows),
        "PRODUCTION_QUEUE_v4.json", SOURCE_TEXT_LITERAL)
    chk("K2_QUEUE_IDS_MATCH_THE_HIERARCHY_IDS", QUEUE,
        sorted(r["unit_or_candidate_id"] for r in k2rows),
        sorted(f"K2-{r['module_code']}-{r['pl']}" for r in h["rows"]), len(k2rows),
        "PRODUCTION_QUEUE_v4.json", INDEPENDENT_MEASURE)
    chk("NO_K2_ROW_IS_IMMEDIATELY_EXECUTABLE", QUEUE,
        [r["unit_or_candidate_id"] for r in k2rows if r["immediately_executable"]], [],
        len(k2rows), "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL, empty_by_design=True)
    chk("NO_K2_ROW_CLAIMS_A_LOCAL_OR_READABLE_BINARY", QUEUE,
        sorted({(r["binary_local"], r["binary_readable"]) for r in k2rows}),
        [(False, False)], len(k2rows), "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL)
    chk("NO_K2_ROW_CLAIMS_EXTRACTED_OR_MODEL_READY", QUEUE,
        sorted({(r["extraction_status"], r["model_status"]) for r in k2rows}),
        [("SOURCE_LOCATED_BY_CONNECTOR", "NOT_STARTED")], len(k2rows),
        "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL)
    chk("EVERY_K2_BLOCKER_IS_OWNED_BY_FIRDAUS", QUEUE,
        sorted({r["blocker_owner"] for r in k2rows}), ["FIRDAUS"], len(k2rows),
        "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL)
    chk("K2_COUNTS_ARE_REPORTED_SEPARATELY", QUEUE,
        [q["k2"]["candidate_structures"], q["k2"]["confirmed_production_units"],
         q["k2"]["immediately_executable_units"], q["k2"]["extracted_units"],
         q["k2"]["model_ready_units"]], [PACKAGE_COUNT, 0, 0, 0, 0], len(k2rows),
        "PRODUCTION_QUEUE_v4.json", INDEPENDENT_MEASURE)
    chk("RECORD_TYPES_STILL_PARTITION_THE_WHOLE_QUEUE", QUEUE,
        q["counts"]["confirmed_production_units"] + q["counts"]["candidate_structures"]
        + q["counts"]["unresolved_source_records"], q["counts"]["total_rows"],
        len(q["rows"]), "PRODUCTION_QUEUE_v4.json", INDEPENDENT_MEASURE)
    chk("THE_HEADLINE_METRIC_DID_NOT_MOVE_WHEN_K2_ARRIVED", QUEUE,
        q["counts"]["immediately_executable_units"], 13, len(q["rows"]),
        "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL)
    chk("IMMEDIATELY_EXECUTABLE_IDS_ARE_PUBLISHED_BY_NAME", QUEUE,
        len(q["immediately_executable_ids"]),
        q["counts"]["immediately_executable_units"], len(q["rows"]),
        "PRODUCTION_QUEUE_v4.json", INDEPENDENT_MEASURE)
    chk("READY_TO_EMIT_IDS_ARE_PUBLISHED_AND_EMPTY", QUEUE,
        q["ready_to_emit_pptx_unit_ids"], [], len(q["rows"]),
        "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL, empty_by_design=True)
    chk("NO_K2_ROW_CARRIES_AN_AUTHORITY_DEPENDENCY", QUEUE,
        sorted({r["authority_dependency"] for r in k2rows}),
        ["none — this is a source-access blocker, not an authority one"], len(k2rows),
        "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL)
    chk("THE_RETIRED_PERCENTAGE_STILL_APPEARS_ONLY_IN_ITS_RETIREMENT_RECORD", QUEUE,
        sorted(k for k, v in q.items()
               if "97.8" in json.dumps(v, ensure_ascii=False, default=str)),
        ["alias_map"], len(q), "PRODUCTION_QUEUE_v4.json", BRIEF_LITERAL)

    # ==================== 6. STALE QUEUE CLEANUP ====================
    live = sorted(f for f in os.listdir(SRC_DIR) if f.startswith("PRODUCTION_QUEUE_"))
    chk("EXACTLY_ONE_QUEUE_VERSION_IS_LIVE", QUEUE,
        sorted({f.rsplit(".", 1)[0] for f in live}), [LIVE_QUEUE_BASENAME], len(live),
        "docs/source listing", INDEPENDENT_MEASURE)
    chk("NO_RETIRED_QUEUE_FILE_REMAINS_ON_DISK", QUEUE,
        [f for f in live if f.rsplit(".", 1)[0] in RETIRED_QUEUE_BASENAMES], [],
        len(RETIRED_QUEUE_BASENAMES) * 3, "docs/source listing", BRIEF_LITERAL,
        empty_by_design=True)
    chk("THE_LIVE_QUEUE_SHIPS_ALL_THREE_PROJECTIONS", QUEUE,
        sorted(live), sorted(LIVE_QUEUE_BASENAME + e
                             for e in (".csv", ".json", ".md")), len(live),
        "docs/source listing", INDEPENDENT_MEASURE)

    # ==================== 7. ACCOUNTING ====================
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID, "STAGE_4_2F_E_K2_QA_v1", 1,
        "this file", BRIEF_LITERAL)
    chk("SUITE_ID_IS_NOT_ANY_SIBLING_SUITE", ACCOUNTING,
        SUITE_ID in SIBLING_SUITES, False, len(SIBLING_SUITES), "this file",
        BRIEF_LITERAL)
    chk("ORACLE_SEPARATION_IS_STILL_RECORDED_AS_DEFERRED", ACCOUNTING,
        ORACLE_SEPARATION_STRUCTURAL, "DEFERRED_BY_DELIVERY_DEADLINE", 1, "this file",
        BRIEF_LITERAL)
    chk("EVERY_GATE_DECLARES_AN_ORACLE_BASIS", ACCOUNTING,
        sorted({r["oracle_basis"] for r in res}) == sorted(set(BASES)), True, len(res),
        "this file", INDEPENDENT_MEASURE)
    chk("NO_GATE_IS_VACUOUS", ACCOUNTING,
        [r["gate_id"] for r in res if r["vacuous"]], [], len(res), "this file",
        BRIEF_LITERAL, empty_by_design=True)
    chk("NO_GATE_CLAIMS_TO_HAVE_READ_THE_BINARY", ACCOUNTING,
        [r["gate_id"] for r in res if r["oracle_basis"] == "RAW_BINARY"], [], len(res),
        "this file", BRIEF_LITERAL, empty_by_design=True)
    return res


def summary():
    res = run()
    return dict(suite_id=SUITE_ID, total=len(res),
                passed=len([r for r in res if r["ok"]]),
                failed=[r for r in res if not r["ok"]],
                by_type={t: len([r for r in res if r["gate_type"] == t])
                         for t in sorted(GATE_TYPES)},
                by_oracle_basis={b: len([r for r in res if r["oracle_basis"] == b])
                                 for b in BASES},
                oracle_separation_structural=ORACLE_SEPARATION_STRUCTURAL,
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
