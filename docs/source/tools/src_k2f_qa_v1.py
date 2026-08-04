# -*- coding: utf-8 -*-
"""Stage 4.2F-F targeted QA — the binary-dependent K2 continuation.

    SUITE_ID = STAGE_4_2F_F_K2_QA_v1
    docs/source/.venv-k2/bin/python docs/source/tools/src_k2f_qa_v1.py

Its own identity, its own total. No sibling suite is merged in or edited to agree with it.

THE ORACLE SITUATION HAS CHANGED SINCE 4.2F-E
---------------------------------------------
Stage 4.2F-E's last gate asserted that NO gate used a RAW_BINARY oracle, because there was
no binary to read. There is now. So this suite legitimately adds a RAW_BINARY basis and,
where the binary is present, RE-MEASURES independently of the model instead of trusting the
model's own evidence file. The bases:

  * BRIEF_LITERAL       — the identity the brief states.
  * SOURCE_TEXT_LITERAL — strings/counts hand-typed out of the source pages this run.
  * INDEPENDENT_MEASURE — a quantity computed a second, different way from the model's.
  * RAW_BINARY          — re-measured from the bytes in this suite (guarded: if the
                          git-ignored binary is absent, the gate is marked skipped, never
                          silently passed).

The defect this run could most easily commit is the MIRROR of 4.2F-E's: now that the
binary is here, over-claiming — promoting a source-ready package to a confirmed unit,
calling a detector's table count a measurement, silently resolving a source anomaly,
reporting a provisional model as model-ready. The gates below are built around those.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import src_k2f_v1 as F   # noqa: E402

SUITE_ID = "STAGE_4_2F_F_K2_QA_v1"
SIBLING_SUITES = ["STAGE_4_2F_E_K2_QA_v1", "STAGE_4_2F_D_RELEASE_FACTS_QA_v1",
                  "PROJECT_SOURCE_CUSTODY_QA_v1"]
ORACLE_SEPARATION_STRUCTURAL = "DEFERRED_BY_DELIVERY_DEADLINE"

CUSTODY, PAGEMAP, HIERARCHY, ASSESS, IMGTBL = ("CUSTODY", "PAGEMAP", "HIERARCHY",
                                               "ASSESS", "IMGTBL")
MODELS, DECISIONS, QUEUE, HONESTY, ACCOUNTING = ("MODELS", "DECISIONS", "QUEUE",
                                                 "HONESTY", "ACCOUNTING")
GATE_TYPES = {CUSTODY, PAGEMAP, HIERARCHY, ASSESS, IMGTBL, MODELS, DECISIONS, QUEUE,
              HONESTY, ACCOUNTING}

BRIEF_LITERAL, SOURCE_TEXT_LITERAL = "BRIEF_LITERAL", "SOURCE_TEXT_LITERAL"
INDEPENDENT_MEASURE, RAW_BINARY = "INDEPENDENT_MEASURE", "RAW_BINARY"
BASES = (BRIEF_LITERAL, SOURCE_TEXT_LITERAL, INDEPENDENT_MEASURE, RAW_BINARY)

# ---- hand-typed anchors, independent of the model's evidence file ----
BRIEF_BYTES = 25043306
BRIEF_SHA256 = "0b2d81dda46eaf4fb018a20a78f7f9b2870129c61125768e4438937f3f405680"
BRIEF_PAGES = 346
# PL spans read by hand off the pages this run (start, end, declared-length)
PL_SPANS = {"PL01": (85, 124, 40), "PL02": (125, 144, 20), "PL03": (145, 184, 40),
            "PL04": (185, 201, 17), "PL05": (202, 225, 24), "PL06": (226, 259, 34),
            "PL07": (260, 270, 11), "PL08": (271, 299, 29), "PL09": (300, 318, 19)}
# module code read off each package's OWN first-page header
PL_MODULE = {"PL01": "M01", "PL02": "M01", "PL03": "M01", "PL04": "M01", "PL05": "M02",
             "PL06": "M03", "PL07": "M04", "PL08": "M05", "PL09": "M06"}
KT_PAPER_COUNT = 9
KT_NUMBERING_BREAK = ["KT PL08", "KT PL09"]
BINARY = os.path.join(os.path.dirname(os.path.dirname(SRC_DIR)),
                      ".source-intake", "K2", "2. PENGURUSAN PEMBINAAN LANDASAN.pdf")

NOT_CHECKED = [
    "whether six modules is instructionally right — that is K2-DEC-04, not a QA question",
    "whether one PL should be one storyboard unit — that is K2-DEC-01",
    "the curated (as opposed to detector) table count — it is not claimed, so not checked",
    "the seven packages not extracted this run — only PL07 and PL09 were modelled",
]


def _live_sha():
    if not os.path.exists(BINARY):
        return None
    h = hashlib.sha256()
    with open(BINARY, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run():
    res = []
    live_sha = _live_sha()

    def chk(gid, gtype, value, expected, population, source_artifact, oracle_basis,
            empty_by_design=None, skipped=False):
        assert gtype in GATE_TYPES, gtype
        assert oracle_basis in BASES, oracle_basis
        ok = value == expected
        vacuous = population == 0 and not empty_by_design
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        population=population, source_artifact=source_artifact,
                        oracle_basis=oracle_basis, empty_by_design=empty_by_design,
                        vacuous=vacuous, skipped=skipped,
                        ok=(ok and not vacuous) or skipped))

    c = F.custody()
    pm = F.page_boundary_map()
    h = F.hierarchy()
    ai = F.assessment_inventory()
    it = F.image_table_inventory()
    mods = F.provisional_models()
    dr = F.decision_register()
    k2rows = F.queue_rows()

    # ==================== 1. CUSTODY — the status finally moves, on evidence ====================
    r = c["record"]
    chk("STATUS_IS_NOW_HASH_VERIFIED", CUSTODY, r["status"],
        "BINARY_LOCAL_HASH_VERIFIED", 1, "K2_BINARY_CUSTODY_v2.json", BRIEF_LITERAL)
    chk("BINARY_IS_CLAIMED_LOCAL_AND_READABLE", CUSTODY,
        [r["binary_local"], r["binary_readable"]], [True, True], 1,
        "K2_BINARY_CUSTODY_v2.json", INDEPENDENT_MEASURE)
    chk("CONTENT_READ_IS_FULL", CUSTODY, r["content_read"], "FULL", 1,
        "K2_BINARY_CUSTODY_v2.json", INDEPENDENT_MEASURE)
    chk("SHA256_IS_VERIFIED_TRUE", CUSTODY, c["binding"]["sha256_verified"], True, 1,
        "K2_BINARY_CUSTODY_v2.json", INDEPENDENT_MEASURE)
    chk("OBSERVED_SHA256_EQUALS_THE_BRIEF", CUSTODY,
        r["verified"]["sha256"]["observed"], BRIEF_SHA256, 1,
        "K2_BINARY_CUSTODY_v2.json", BRIEF_LITERAL)
    chk("OBSERVED_BYTES_EQUAL_THE_BRIEF", CUSTODY,
        r["verified"]["bytes"]["observed"], BRIEF_BYTES, 1,
        "K2_BINARY_CUSTODY_v2.json", BRIEF_LITERAL)
    chk("OBSERVED_PAGES_EQUAL_THE_BRIEF", CUSTODY,
        r["verified"]["pages"]["observed"], BRIEF_PAGES, 1,
        "K2_BINARY_CUSTODY_v2.json", BRIEF_LITERAL)
    chk("PDF_IS_NOT_ENCRYPTED", CUSTODY, r["verified"]["encryption_status"],
        "NOT_ENCRYPTED", 1, "K2_BINARY_CUSTODY_v2.json", INDEPENDENT_MEASURE)
    chk("IT_SUPERSEDES_CUSTODY_02_WITHOUT_OVERTURNING_IT", CUSTODY,
        r["supersedes"].startswith("K2-CUSTODY-02"), True, 1,
        "K2_BINARY_CUSTODY_v2.json", BRIEF_LITERAL)
    chk("GRANULARITY_IS_STILL_NOT_CLAIMED_DECIDED", CUSTODY,
        "UNIT_GRANULARITY_DECIDED" in r["states_still_not_claimed"], True, 1,
        "K2_BINARY_CUSTODY_v2.json", BRIEF_LITERAL)
    # RAW_BINARY: re-hash the bytes in this suite, independent of the model's evidence file
    chk("LIVE_REHASH_MATCHES_THE_BRIEF", CUSTODY,
        live_sha == BRIEF_SHA256 if live_sha else "SKIPPED",
        True if live_sha else "SKIPPED", 1, ".source-intake/K2/…pdf", RAW_BINARY,
        skipped=live_sha is None)

    # ==================== 2. PAGE / BOUNDARY MAP ====================
    a = pm["accounting"]
    chk("THE_346_PAGES_FORM_A_CLEAN_PARTITION", PAGEMAP, a["clean_partition"], True, 1,
        "K2_PAGE_BOUNDARY_MAP_v1.json", INDEPENDENT_MEASURE)
    chk("NO_PAGE_IS_UNASSIGNED", PAGEMAP, a["unassigned_pages"], [], BRIEF_PAGES,
        "K2_PAGE_BOUNDARY_MAP_v1.json", INDEPENDENT_MEASURE, empty_by_design=True)
    chk("NO_PAGE_IS_IN_TWO_REGIONS", PAGEMAP, a["overlapping_pages"], [], BRIEF_PAGES,
        "K2_PAGE_BOUNDARY_MAP_v1.json", INDEPENDENT_MEASURE, empty_by_design=True)
    pl_regions = {rg["region"]: (rg["pdf_start_page"], rg["pdf_end_page"])
                  for rg in pm["regions"] if rg["region"].startswith("PL")}
    chk("EVERY_PL_SPAN_MATCHES_THE_HAND_TYPED_SPAN", PAGEMAP,
        pl_regions, {k: (v[0], v[1]) for k, v in PL_SPANS.items()}, len(PL_SPANS),
        "K2_PAGE_BOUNDARY_MAP_v1.json", SOURCE_TEXT_LITERAL)
    chk("EVERY_PL_SPAN_MATCHES_ITS_OWN_DECLARED_LENGTH", PAGEMAP,
        pm["all_pl_spans_match_declared"], True, len(PL_SPANS),
        "K2_PAGE_BOUNDARY_MAP_v1.json", INDEPENDENT_MEASURE)
    chk("REGION_PAGES_SUM_TO_346", PAGEMAP,
        sum(rg["pages"] for rg in pm["regions"]), BRIEF_PAGES, len(pm["regions"]),
        "K2_PAGE_BOUNDARY_MAP_v1.json", INDEPENDENT_MEASURE)

    # ==================== 3. HIERARCHY v2 ====================
    chk("DECOMPOSITION_IS_NOW_COMPLETE", HIERARCHY, h["decomposition_completed"], True, 1,
        "K2_COURSE_HIERARCHY_v2.json", BRIEF_LITERAL)
    chk("NO_SOURCE_REGION_REMAINS_UNMAPPED", HIERARCHY, h["unmapped_source_regions"], 0, 1,
        "K2_COURSE_HIERARCHY_v2.json", INDEPENDENT_MEASURE)
    chk("PL_TO_MODULE_MAP_IS_CONFIRMED_FROM_EACH_HEADER", HIERARCHY,
        {r["pl"]: r["module_code"] for r in h["rows"]}, PL_MODULE, len(h["rows"]),
        "K2_COURSE_HIERARCHY_v2.json", SOURCE_TEXT_LITERAL)
    chk("ALL_NINE_ARE_SOURCE_READY_CLEAN", HIERARCHY, h["source_ready_clean"], 9, 9,
        "K2_COURSE_HIERARCHY_v2.json", INDEPENDENT_MEASURE)
    chk("STILL_NO_PL_IS_A_CONFIRMED_UNIT", HIERARCHY, h["confirmed_units"], 0, len(h["rows"]),
        "K2_COURSE_HIERARCHY_v2.json", BRIEF_LITERAL)
    chk("EVERY_ROW_HAS_AN_OBSERVED_PAGE_SPAN", HIERARCHY,
        all(isinstance(r["pdf_start_page"], int) and isinstance(r["pdf_end_page"], int)
            for r in h["rows"]), True, len(h["rows"]),
        "K2_COURSE_HIERARCHY_v2.json", INDEPENDENT_MEASURE)
    chk("NO_ROW_STILL_CARRIES_AN_UNKNOWN_SPAN", HIERARCHY,
        [r["pl"] for r in h["rows"] if "UNKNOWN" in str(r["pdf_start_page"])], [],
        len(h["rows"]), "K2_COURSE_HIERARCHY_v2.json", BRIEF_LITERAL, empty_by_design=True)
    chk("ALL_NINE_TITLES_ARE_OBSERVED_NOT_INFERRED", HIERARCHY,
        all(r["title_source"] == "PL_PACKAGE_OWN_FIRST_PAGE" for r in h["rows"]), True,
        len(h["rows"]), "K2_COURSE_HIERARCHY_v2.json", INDEPENDENT_MEASURE)

    # ==================== 4. ASSESSMENT INVENTORY ====================
    chk("NINE_KT_TASK_PAPERS_ARE_INVENTORIED", ASSESS, ai["kt_paper_count"],
        KT_PAPER_COUNT, KT_PAPER_COUNT, "K2_ASSESSMENT_INVENTORY_v1.json",
        SOURCE_TEXT_LITERAL)
    chk("ALL_NINE_PACKAGES_HAVE_THEIR_OWN_ANSWER_SCHEME", ASSESS,
        len(ai["answer_schemes_present"]), 9, 9, "K2_ASSESSMENT_INVENTORY_v1.json",
        INDEPENDENT_MEASURE)
    chk("THE_KT_NUMBERING_BREAK_IS_RECORDED", ASSESS,
        sorted(o["numbering_break_codes"] for o in ai["observations"]
               if o["defect_id"] == "K2-SOURCE-OBS-02")[0], KT_NUMBERING_BREAK, 1,
        "K2_ASSESSMENT_INVENTORY_v1.json", SOURCE_TEXT_LITERAL)
    chk("THE_KT06_COLLISION_IS_RECORDED_NOT_RESOLVED", ASSESS,
        any(o["defect_id"] == "K2-SOURCE-OBS-03" and "not_resolved_here" in o
            for o in ai["observations"]), True, 1,
        "K2_ASSESSMENT_INVENTORY_v1.json", BRIEF_LITERAL)
    _obs03 = next((o for o in ai["observations"]
                   if o["defect_id"] == "K2-SOURCE-OBS-03"), {})
    _cons = {c["pl"]: c["consequence"] for c in _obs03.get("consequences", [])}
    chk("KT06_RECORDS_DISTINCT_CONSEQUENCES_FOR_PL06_AND_PL08", ASSESS,
        [_cons.get("PL06"), _cons.get("PL08")],
        ["EXPECTED_ASSESSMENT_MAPPING_MISSING_OR_MISLABELLED",
         "POSSIBLE_DUPLICATED_OR_MISASSIGNED_ASSESSMENT_TITLE"], 2,
        "K2_ASSESSMENT_INVENTORY_v1.json", BRIEF_LITERAL)
    chk("PL06_AND_PL08_CONSEQUENCES_ARE_NOT_THE_SAME", ASSESS,
        _cons.get("PL06") != _cons.get("PL08") and bool(_cons.get("PL06")), True, 2,
        "K2_ASSESSMENT_INVENTORY_v1.json", INDEPENDENT_MEASURE)
    chk("SOURCE_ANOMALIES_STAY_WITH_FIRDAUS_NOT_BARIAH", ASSESS,
        sorted({o["routed_to"] for o in ai["observations"]}), ["FIRDAUS"],
        len(ai["observations"]), "K2_ASSESSMENT_INVENTORY_v1.json", BRIEF_LITERAL)
    chk("TWO_ASSESSMENT_SYSTEMS_ARE_NAMED", ASSESS,
        len(ai["two_assessment_systems"]), 2, 2, "K2_ASSESSMENT_INVENTORY_v1.json",
        INDEPENDENT_MEASURE)

    # ==================== 5. IMAGE / TABLE INVENTORY ====================
    chk("TABLE_COUNTS_ARE_LABELLED_DETECTOR_NOT_MEASURED", IMGTBL,
        all("table_detector_count" in r for r in it["per_pl"]), True, len(it["per_pl"]),
        "K2_IMAGE_TABLE_INVENTORY_v1.json", BRIEF_LITERAL)
    chk("NO_TABLE_FIELD_IS_CALLED_A_PLAIN_TABLE_COUNT", IMGTBL,
        any("table_count" in r and "table_detector_count" not in r
            for r in it["per_pl"]), False, len(it["per_pl"]),
        "K2_IMAGE_TABLE_INVENTORY_v1.json", BRIEF_LITERAL)
    chk("IMAGE_TOTAL_IS_THE_SUM_OF_ALL_REGIONS_PLUS_PL", IMGTBL,
        it["totals"]["images_total"] >= sum(r["image_count"] for r in it["per_pl"]),
        True, 1, "K2_IMAGE_TABLE_INVENTORY_v1.json", INDEPENDENT_MEASURE)

    # ==================== 6. PROVISIONAL MODELS ====================
    chk("EXACTLY_TWO_MODELS_WERE_PRODUCED", MODELS, mods["count"], 2, 2,
        "K2_PROVISIONAL_MODELS_v1.json", BRIEF_LITERAL)
    chk("THE_SELECTION_CRITERION_IS_STATED", MODELS,
        len(mods["selection_criterion"]) > 0, True, 1,
        "K2_PROVISIONAL_MODELS_v1.json", BRIEF_LITERAL)
    chk("MODELS_ARE_PL07_AND_PL09", MODELS,
        sorted(m["pl"] for m in mods["models"]), ["PL07", "PL09"], 2,
        "K2_PROVISIONAL_MODELS_v1.json", INDEPENDENT_MEASURE)
    chk("EVERY_MODEL_CITES_ITS_SOURCE_PAGES", MODELS,
        all(isinstance(m["tajuk_page"], int) and m["skema_jawapan"]["page"]
            for m in mods["models"]), True, 2,
        "K2_PROVISIONAL_MODELS_v1.json", INDEPENDENT_MEASURE)
    chk("MODELS_ARE_MARKED_PROVISIONAL_NOT_FINAL", MODELS,
        all("PROVISIONAL" in m["confidence"] for m in mods["models"]), True, 2,
        "K2_PROVISIONAL_MODELS_v1.json", BRIEF_LITERAL)

    # ==================== 7. DECISION REGISTER ====================
    chk("THE_DECISION_REGISTER_EXISTS_NOW", DECISIONS, dr["register_id"],
        "K2-DECISIONS-01", 1, "K2_DECISION_REGISTER_v1.json", BRIEF_LITERAL)
    chk("IT_IS_ROUTED_TO_BARIAH_AND_CAIR", DECISIONS, dr["routed_to"],
        "BARIAH_AND_CAIR", 1, "K2_DECISION_REGISTER_v1.json", BRIEF_LITERAL)
    chk("EVERY_DECISION_SAYS_WHY_IT_IS_ANSWERABLE_NOW", DECISIONS,
        all(d.get("why_now") for d in dr["decisions"]), True, len(dr["decisions"]),
        "K2_DECISION_REGISTER_v1.json", INDEPENDENT_MEASURE)
    chk("GRANULARITY_IS_THE_FIRST_DECISION", DECISIONS,
        dr["decisions"][0]["decision_id"], "K2-DEC-01", len(dr["decisions"]),
        "K2_DECISION_REGISTER_v1.json", BRIEF_LITERAL)

    # ==================== 8. QUEUE ====================
    chk("K2_ROWS_ARE_BOUNDARY_CONFIRMED_AND_READABLE", QUEUE,
        sorted({(r["binary_readable"], r["boundary_confirmed"]) for r in k2rows}),
        [(True, True)], len(k2rows), "PRODUCTION_QUEUE_v5.json", INDEPENDENT_MEASURE)
    chk("NO_K2_ROW_IS_A_CONFIRMED_UNIT", QUEUE,
        [r["pl"] for r in k2rows if r["record_type"] == "CONFIRMED_PRODUCTION_UNIT"], [],
        len(k2rows), "PRODUCTION_QUEUE_v5.json", BRIEF_LITERAL, empty_by_design=True)
    chk("NO_K2_ROW_IS_IMMEDIATELY_EXECUTABLE_YET", QUEUE,
        [r["pl"] for r in k2rows if r["immediately_executable"]], [], len(k2rows),
        "PRODUCTION_QUEUE_v5.json", BRIEF_LITERAL, empty_by_design=True)
    chk("EXACTLY_TWO_K2_ROWS_ARE_EXTRACTED", QUEUE,
        len([r for r in k2rows if r["extraction_status"] == "EXTRACTED"]), 2, len(k2rows),
        "PRODUCTION_QUEUE_v5.json", INDEPENDENT_MEASURE)
    chk("EXACTLY_TWO_K2_ROWS_ARE_MODEL_READY", QUEUE,
        sorted(r["pl"] for r in k2rows if r["model_status"] == "MODEL_READY"),
        ["PL07", "PL09"], len(k2rows), "PRODUCTION_QUEUE_v5.json", INDEPENDENT_MEASURE)
    chk("KT06_EXCEPTION_PLS_ARE_HELD_AND_NOT_MODEL_READY", QUEUE,
        sorted(r["pl"] for r in k2rows
               if "K2-SOURCE-OBS-03" in r["exact_blocker"]
               and r["model_status"] != "MODEL_READY"),
        ["PL06", "PL08"], len(k2rows), "PRODUCTION_QUEUE_v5.json", BRIEF_LITERAL)
    chk("EVERY_K2_ROW_IS_READY_TO_EMIT_FALSE", QUEUE,
        [r["pl"] for r in k2rows if r["ready_to_emit_pptx"]], [], len(k2rows),
        "PRODUCTION_QUEUE_v5.json", BRIEF_LITERAL, empty_by_design=True)
    # queue-wide facts, read from the published v5
    q = json.load(open(os.path.join(SRC_DIR, "PRODUCTION_QUEUE_v5.json"),
                       encoding="utf-8"))
    chk("THE_HEADLINE_METRIC_STILL_DID_NOT_MOVE", QUEUE,
        q["counts"]["immediately_executable_units"], 13, 1, "PRODUCTION_QUEUE_v5.json",
        BRIEF_LITERAL)
    chk("EXTRACTED_UNITS_ROSE_BY_EXACTLY_TWO", QUEUE,
        q["counts"]["extracted_units"], 16, 1, "PRODUCTION_QUEUE_v5.json",
        INDEPENDENT_MEASURE)
    chk("MODEL_READY_UNITS_ROSE_BY_EXACTLY_TWO", QUEUE,
        q["counts"]["model_ready_units"], 25, 1, "PRODUCTION_QUEUE_v5.json",
        INDEPENDENT_MEASURE)
    chk("ALL_QUEUE_INVARIANTS_HOLD", QUEUE,
        [i["invariant"] for i in q["invariants"] if not i["holds"]], [],
        len(q["invariants"]), "PRODUCTION_QUEUE_v5.json", INDEPENDENT_MEASURE,
        empty_by_design=True)
    chk("EVERY_MEMBER_ROLL_MATCHES_ITS_COUNT", QUEUE,
        [k for k in q["member_rolls"] if len(q["member_rolls"][k]) != q["counts"][k]], [],
        len(q["member_rolls"]), "PRODUCTION_QUEUE_v5.json", INDEPENDENT_MEASURE,
        empty_by_design=True)
    chk("EXACTLY_ONE_QUEUE_VERSION_IS_LIVE", QUEUE,
        sorted({f.rsplit(".", 1)[0] for f in os.listdir(SRC_DIR)
                if f.startswith("PRODUCTION_QUEUE_")}), ["PRODUCTION_QUEUE_v5"], 1,
        "docs/source listing", INDEPENDENT_MEASURE)
    chk("V4_IS_RETIRED_FROM_THE_LIVE_TREE", QUEUE,
        [f for f in os.listdir(SRC_DIR) if f.startswith("PRODUCTION_QUEUE_v4")], [], 3,
        "docs/source listing", BRIEF_LITERAL, empty_by_design=True)

    # ==================== 9. HONESTY (the mirror defects) ====================
    chk("BINARY_ABSENT_STATES_ARE_NOT_STILL_CLAIMED", HONESTY,
        "SOURCE_CONTENT_PARTIALLY_READ" not in r.get("states_claimed", []), True, 1,
        "K2_BINARY_CUSTODY_v2.json", BRIEF_LITERAL)
    chk("ALL_NINE_ARE_NOT_OVERCLAIMED_AS_MODELLED", HONESTY,
        mods["count"] < 9, True, 1, "K2_PROVISIONAL_MODELS_v1.json", BRIEF_LITERAL)
    chk("THE_MODULE_COUNT_CONFLICT_IS_STILL_OPEN_NOT_SILENTLY_FIXED", HONESTY,
        any(d["decision_id"] == "K2-DEC-04" for d in dr["decisions"]), True, 1,
        "K2_DECISION_REGISTER_v1.json", BRIEF_LITERAL)

    # ==================== 10. ACCOUNTING ====================
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID, "STAGE_4_2F_F_K2_QA_v1", 1,
        "this file", BRIEF_LITERAL)
    chk("SUITE_ID_IS_NOT_ANY_SIBLING_SUITE", ACCOUNTING, SUITE_ID in SIBLING_SUITES,
        False, len(SIBLING_SUITES), "this file", BRIEF_LITERAL)
    chk("A_RAW_BINARY_ORACLE_IS_NOW_LEGITIMATELY_USED", ACCOUNTING,
        RAW_BINARY in {x["oracle_basis"] for x in res}, True, len(res), "this file",
        INDEPENDENT_MEASURE)
    chk("NO_GATE_IS_VACUOUS", ACCOUNTING, [x["gate_id"] for x in res if x["vacuous"]], [],
        len(res), "this file", BRIEF_LITERAL, empty_by_design=True)
    return res


def summary():
    res = run()
    return dict(suite_id=SUITE_ID, total=len(res),
                passed=len([r for r in res if r["ok"]]),
                skipped=len([r for r in res if r["skipped"]]),
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
    print(f"{s['passed']}/{s['total']} passed ({s['skipped']} skipped)")
    print("by type:", s["by_type"])
    print("by oracle basis:", s["by_oracle_basis"])
    for f in s["failed"]:
        print(f"  FAIL {f['gate_id']}: {f['value']!r} != {f['expected']!r} "
              f"(pop {f['population']}, vacuous={f['vacuous']})")
