# -*- coding: utf-8 -*-
"""Stage 4.2F-C targeted QA — release-critical and extraction-critical protections only.

    SUITE_ID = PROJECT_SOURCE_CUSTODY_QA_v1
    python3 docs/source/tools/src_qa_v1.py

This is deliberately narrow. It covers the ten protections the run was asked to verify and
the new source and queue paths, and it refactors nothing that already exists. The PL06 and
T04 suites keep their own gates and their own totals; nothing here is added to them.
"""
import json
import os
import re
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
import pl06_batch1_data_v1 as B  # noqa: E402  — owns and verifies the frozen map path
import pl06_extract_v1 as EX     # noqa: E402
import pl06_unit_model_v1 as UM  # noqa: E402

SUITE_ID = "PROJECT_SOURCE_CUSTODY_QA_v1"
PRIOR_SUITE_ID = "PL06_AUTHORITY_HARVEST_BATCH1_QA_v1"

AUTHORITY = "AUTHORITY"
CUSTODY = "CUSTODY"
ORACLE = "ORACLE"
EXTRACTION = "EXTRACTION"
BOUNDARY = "BOUNDARY"
QUEUE = "QUEUE"
PENDING = "PENDING"
ACCOUNTING = "ACCOUNTING"
GATE_TYPES = {AUTHORITY, CUSTODY, ORACLE, EXTRACTION, BOUNDARY, QUEUE, PENDING, ACCOUNTING}

NOT_CHECKED = [
    "the K2 monolith's structure — the binary is not local and the lane records that",
    "seven of the nine K3 PDFs — identified, not read, and recorded as not read",
    "whether any provisional model is instructionally sound — that is Bariah's, and the "
    "pattern package is still with her",
    "how any artifact renders in Microsoft Word or PowerPoint — still no Writer or Impress "
    "filter here",
    "whether the unmapped K5 Pakej Latihan really contain the candidate units their "
    "sub-modul headings suggest",
]

BATCH1_DIR = os.path.join(PL06, "batch1_extract")


def run():
    res = []

    def chk(gid, gtype, value, expected, population, source_artifact, empty_by_design=None):
        assert gtype in GATE_TYPES, gtype
        ok = value == expected
        vacuous = population == 0 and not empty_by_design
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        population=population, source_artifact=source_artifact,
                        empty_by_design=empty_by_design, vacuous=vacuous,
                        ok=ok and not vacuous))

    custody = A.custody_manifest()
    inv = INV.inventory()
    queue = Q.summary()
    extracts = EX.extract_all()
    models, _ = UM.all_models()
    k5 = custody["rows"][0]

    # ==================== 1. AUTHORITY ====================
    chk("SRC_AUTH_01_IS_OWNED_AND_APPROVED", AUTHORITY,
        [A.AUTHORITY["authority_id"], A.AUTHORITY["owner"], A.AUTHORITY["status"]],
        ["SRC-AUTH-01", "FIRDAUS_PROJECT_DELIVERY_AUTHORITY", "APPROVED"], 1,
        "SRC_AUTH_01_v1.json")
    chk("THE_AUTHORITY_IS_PACKAGE_LEVEL_NOT_PER_UNIT", AUTHORITY,
        [A.AUTHORITY["granularity"], A.AUTHORITY["applied_at"]],
        ["SOURCE_PACKAGE", "SOURCE_PACKAGE_LEVEL_NOT_PER_UNIT"], 1, "SRC_AUTH_01_v1.json")
    chk("SIX_PERMITTED_OPERATIONS", AUTHORITY, len(A.AUTHORITY["permitted_operations"]), 6,
        len(A.AUTHORITY["permitted_operations"]), "SRC_AUTH_01_v1.json")
    chk("SIX_EXPLICIT_EXCLUSIONS", AUTHORITY, len(A.AUTHORITY["explicit_exclusions"]), 6,
        len(A.AUTHORITY["explicit_exclusions"]), "SRC_AUTH_01_v1.json")
    chk("THE_EXCLUSIONS_NAME_EVERY_THING_NOT_AUTHORISED", AUTHORITY,
        [x for x in ("instructional approval", "grouping or treatment", "answer key",
                     "visual direction", "client release", "Bariah decision")
         if not any(x in e for e in A.AUTHORITY["explicit_exclusions"])], [], 6,
        "SRC_AUTH_01_v1.json")
    chk("D25_IS_SUPERSEDED_NOT_REWRITTEN", AUTHORITY,
        [A.SUPERSESSION["historical_id"], A.SUPERSESSION["relationship"],
         A.SUPERSESSION["live_id"], A.SUPERSESSION["historical_record_status"]],
        ["PL06-B1-D-25", "SUPERSEDED_FOR_LIVE_PROCESSING_BY", "SRC-AUTH-01",
         "PRESERVED_UNCHANGED"], 1, "SRC_AUTH_01_v1.json")
    # The historical artifact must still say what it said.
    d25_path = os.path.join(PL06, "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")
    d25 = (json.load(open(d25_path, encoding="utf-8")) if os.path.exists(d25_path) else {})
    chk("THE_HISTORICAL_D25_RECORD_IS_STILL_ON_DISK_UNCHANGED", AUTHORITY,
        [d["point_key"] for d in d25.get("decisions", [])
         if d["decision_id"] == "PL06-B1-D-25"], ["extraction"],
        len(d25.get("decisions", [])) or 1, "PL06_HARVEST_BATCH1_DECISION_INDEX_v1.json")

    # ==================== 2. PENDING v1.2 CANNOT BECOME A RULE ====================
    # Supersedes THE_PATTERN_PACKAGE_IS_PENDING_NOT_AUTHORITY, which asserted the WHOLE
    # v1.2 package was still pending with is_authority False and may_be_auto_applied
    # False. Bariah returned it on 4/8/2026 and Sections A, C and D are now live K5
    # policy, so that assertion is simply false — it would fail on a true fact.
    #
    # The intent has not changed: nothing may be auto-applied that Bariah has not
    # approved. What changed is that "not approved" is now a per-section question rather
    # than a whole-package one. Section B is the part that must never default, so the
    # replacement proves all three of the things that matter.
    pp = A.PENDING_PATTERN_PACKAGE
    chk("AUTHORITY_IS_PARTITIONED_BY_SECTION_NOT_A_SINGLE_FLAG", PENDING,
        [pp["status"], pp["is_authority"]],
        ["RETURNED_BY_BARIAH_AND_INGESTED", None], 1, "SRC_AUTH_01_v1.json")
    chk("SECTIONS_A_C_D_ARE_INGESTED_AUTHORITY", PENDING,
        [pp["authority_by_section"][s] for s in ("A", "C", "D")],
        ["APPROVED_WITH_AMENDMENTS", "APPROVED", "APPROVED_WITH_AMENDMENTS"], 3,
        "SRC_AUTH_01_v1.json")
    # Section B closed on 4/8/2026 in a second Bariah return, so the earlier
    # "B is pending" assertions would now fail on a true fact. The intent survives intact:
    # the thing that may not be auto-applied is B2, which is TEST_REQUIRED, not approved.
    chk("SECTION_B_IS_CLOSED", PENDING,
        pp["authority_by_section"]["B"], "APPROVED_WITH_AMENDMENTS_FOR_CALIBRATION", 1,
        "SRC_AUTH_01_v1.json")
    chk("B2_MAY_NOT_BE_AUTO_APPLIED", PENDING,
        pp["section_b_items"]["B2"]["may_be_auto_applied"], False, 4,
        "SRC_AUTH_01_v1.json")
    chk("B2_IS_THE_ONLY_SECTION_B_ITEM_BLOCKED", PENDING,
        sorted(k for k, v in pp["section_b_items"].items()
               if not v["may_be_auto_applied"]), ["B2"], 4, "SRC_AUTH_01_v1.json")
    chk("CALIBRATION_AUTHORIZED_MASS_GENERATION_NOT", PENDING,
        [pp["calibration_generation_authorized"], pp["mass_generation_authorized"]],
        [True, False], 1, "SRC_AUTH_01_v1.json")
    chk("NO_MODEL_TREATS_THE_PATTERN_PACKAGE_AS_A_RULE", PENDING,
        [uid for uid, m in models.items()
         if m["pattern_family"]["cls"] != "PENDING_BARIAH_PATTERN_DECISION"], [],
        len(models), "*_PROVISIONAL_MODEL_v1.json")
    chk("EVERY_MODEL_FREEZES_NOTHING", PENDING,
        [uid for uid, m in models.items()
         if sorted(m["frozen_nothing"]) != sorted(UM.FROZEN_NOTHING)], [], len(models),
        "*_PROVISIONAL_MODEL_v1.json")
    chk("SEVEN_THINGS_ARE_DECLARED_UNFROZEN", PENDING, sorted(UM.FROZEN_NOTHING),
        sorted(["screen count", "sequence", "dialogue", "Rumusan form", "pattern family",
                "assessment key", "visual reuse"]), 7,
        "PL06_BATCH1_EXTRACTION_SUMMARY_v1.json")
    chk("NO_MODEL_CLAIMS_A_MAXIMUM_SCREEN_COUNT", PENDING,
        [uid for uid, m in models.items()
         if m["screen_sequence"]["arithmetic"]["maximum_total_screens"]
         != "UNKNOWN_PENDING_PATTERN_DECISION"], [], len(models),
        "*_PROVISIONAL_MODEL_v1.json")
    chk("NO_ANSWER_KEY_IS_APPROVED", PENDING,
        sorted({m["assessment"]["key_status"] for m in models.values()}),
        ["DRAFTED_NOT_APPROVED"], len(models), "*_PROVISIONAL_MODEL_v1.json")
    chk("NO_K3_SOURCE_ANSWER_SCHEME_IS_CALLED_APPROVED", PENDING,
        sorted({m["source_assessment"]["key_status"] for m in inv["k3_models"]}),
        ["SOURCE_AUTHORED_NOT_STORYBOARD_APPROVED"], len(inv["k3_models"]),
        "K3_PROVISIONAL_MODELS_v1.json")
    chk("NO_CHARACTER_IS_PROPOSED_WHILE_STOP_006_IS_OPEN", PENDING,
        [uid for uid, m in models.items()
         if m["dialogue"]["cast"] != "NO_CHARACTER_PROPOSED_STOP_006_OPEN"], [],
        len(models), "*_PROVISIONAL_MODEL_v1.json")

    # ==================== 3. ORACLE INDEPENDENCE ====================
    # Expected and observed must not come through the same mutable parser.
    raw = json.load(open(B.BOUNDARY_MAP_PATH, encoding="utf-8"))["lessons"]
    raw_by = {l["unit_id"]: l for l in raw}
    chk("SHARED_BOUNDARY_TRUTH_IS_READ_FROM_THE_RAW_MANIFEST", ORACLE,
        [u["unit_id"] for u in EX.UNITS
         if bool(u["shared_start"]) is not bool(raw_by[u["unit_id"]]["shared_start"])
         or bool(u["shared_end"]) is not bool(raw_by[u["unit_id"]]["shared_end"])], [],
        len(EX.UNITS), "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")
    # Raw booleans must never be compared as strings. The batch 1 package was caught doing
    # exactly this, and the check is kept here because the same map feeds this run.
    chk("RAW_BOOLEANS_ARE_NOT_COMPARED_AS_STRINGS", ORACLE,
        [l["unit_id"] for l in raw
         if not isinstance(l["shared_start"], bool)
         or not isinstance(l["shared_end"], bool)], [], len(raw),
        "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")
    chk("THE_STRING_COMPARISON_WOULD_HAVE_BEEN_WRONG", ORACLE,
        len([l for l in raw if (l["shared_start"] == "True") != bool(l["shared_start"])]),
        len([l for l in raw if l["shared_start"] is True]), len(raw),
        "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")
    # The page oracle is the typeset PDF; the model being checked is the DOCX. Two artifacts.
    chk("PAGE_ATTRIBUTION_USES_A_DIFFERENT_ARTIFACT_FROM_THE_EXTRACTION", ORACLE,
        sorted({e["page_attribution_primary"] for e in extracts.values()}), ["TYPESET_PDF"],
        len(extracts), "*_SOURCE_EXTRACT_v1.json")
    chk("THE_CACHED_LAYOUT_SECOND_OPINION_IS_STILL_RECORDED", ORACLE,
        [uid for uid, e in extracts.items()
         if not e.get("page_attribution_secondary")], [], len(extracts),
        "*_SOURCE_EXTRACT_v1.json")
    chk("THE_TWO_PAGE_ORACLES_ARE_RECORDED_AS_DISAGREEING", ORACLE,
        [uid for uid, e in extracts.items()
         if e["page_attribution_divergence"]["cached_layout_agrees_with_frozen"]], [],
        len(extracts), "*_SOURCE_EXTRACT_v1.json")
    chk("THE_TYPESET_ORACLE_AGREES_WITH_THE_FROZEN_MAP", ORACLE,
        [uid for uid, e in extracts.items()
         if not e["page_attribution_divergence"]["typeset_agrees_with_frozen"]], [],
        len(extracts), "*_SOURCE_EXTRACT_v1.json")
    # A generalised reader checked against the reader it generalises.
    eq = EX.t04_equivalence()
    chk("THE_NEW_READER_REPRODUCES_THE_FROZEN_T04_EXTRACT", ORACLE,
        [eq.get("equivalent"), len(eq.get("text_mismatches", [])),
         len(eq.get("type_mismatches", [])),
         len(eq.get("paragraph_index_mismatches", []))],
        [True, 0, 0, 0], eq.get("frozen_row_count", 0), "T04_SOURCE_EXTRACT_v1.json")
    # Unit counts must not come from the queue that is being validated.
    chk("UNIT_COUNTS_ARE_NOT_DERIVED_FROM_THE_QUEUE_BEING_VALIDATED", ORACLE,
        [inv["k5"]["totals"]["confirmed_units"], len(raw)], [14, 14], len(raw),
        "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")

    # ==================== 4. CUSTODY ====================
    chk("THE_K5_BINARY_IS_HASH_VERIFIED", CUSTODY,
        [k5["available"], k5["bytes_match"], k5["sha256_match"], k5["format_valid"]],
        [True, True, True, True], 1, "SOURCE_CUSTODY_MANIFEST_v1.json")
    chk("EVERY_ANCHOR_PROBE_LANDS_ON_ITS_HEADING", CUSTODY,
        [p["paragraph_index"] for p in k5["anchor_probes"] if not p["matches"]], [],
        len(k5["anchor_probes"]), "SOURCE_CUSTODY_MANIFEST_v1.json")
    chk("EVERY_PACKAGE_CARRIES_A_DECLARED_EVIDENCE_CLASS", CUSTODY,
        [r["package"] for r in custody["rows"]
         if r["evidence_class"] not in A.EVIDENCE_CODES], [], len(custody["rows"]),
        "SOURCE_CUSTODY_MANIFEST_v1.json")
    # A derived record must never be counted as binary readability.
    chk("NO_PACKAGE_CLAIMS_HASH_VERIFICATION_WITHOUT_A_HASH", CUSTODY,
        [r["package"] for r in custody["rows"]
         if r["evidence_class"] == "LOCAL_BINARY_HASH_VERIFIED"
         and r.get("sha256") in (None, A.NOT_COMPUTED)], [], len(custody["rows"]),
        "SOURCE_CUSTODY_MANIFEST_v1.json")
    chk("EVERY_UNHASHED_PACKAGE_SAYS_SO_EXPLICITLY", CUSTODY,
        [r["package"] for r in custody["rows"]
         if r["evidence_class"] != "LOCAL_BINARY_HASH_VERIFIED"
         and r.get("sha256") != A.NOT_COMPUTED], [], len(custody["rows"]),
        "SOURCE_CUSTODY_MANIFEST_v1.json")

    # ==================== 5. UNKNOWN CANNOT BECOME ZERO OR FALSE ====================
    k2 = inv["k2"]
    unknown_fields = ["page_count", "heading_tree", "module_pl_hierarchy", "descendant_map",
                      "latihan_locations", "skema_jawapan_locations", "image_inventory",
                      "table_inventory", "candidate_unit_boundaries", "shared_page_risks",
                      "candidate_clean_units", "estimated_total_units"]
    chk("EVERY_UNMEASURED_K2_FIELD_IS_UNKNOWN_NOT_ZERO", EXTRACTION,
        [f for f in unknown_fields if k2[f] != INV.UNKNOWN], [], len(unknown_fields),
        "K2_MONOLITH_DECOMPOSITION_v1.json")
    chk("NO_UNREAD_K3_PDF_IS_GIVEN_A_PAGE_COUNT", EXTRACTION,
        [r["pl"] for r in inv["k3"]["rows"]
         if r["read_status"] == INV.NOT_READ and r["pages"] != INV.UNKNOWN], [],
        len(inv["k3"]["rows"]), "K3_SOURCE_INVENTORY_v1.json")
    chk("NO_UNREAD_K3_PDF_IS_CLASSIFIED_CLEAN", EXTRACTION,
        [r["pl"] for r in inv["k3"]["rows"]
         if r["read_status"] == INV.NOT_READ
         and r["classification"] in INV.CANDIDATE_CLASSES], [], len(inv["k3"]["rows"]),
        "K3_SOURCE_INVENTORY_v1.json")
    chk("UNKNOWN_VISUAL_COUNTS_ARE_NOT_RENDERED_AS_ZERO", EXTRACTION,
        [uid for uid, m in models.items()
         if m["visual_obligations"]["source_attested"]
         > m["visual_obligations"]["count"]], [], len(models),
        "*_PROVISIONAL_MODEL_v1.json")

    # ==================== 6. MISSING SOURCE CANNOT LOOK EXTRACTED ====================
    chk("K2_IS_NOT_MARKED_EXTRACTED_ANYWHERE_IN_THE_QUEUE", EXTRACTION,
        [r["unit_id"] for r in queue["rows"]
         if r["course"] == "K2" and r["extraction_status"] != "SOURCE_BLOCKED"], [],
        len([r for r in queue["rows"] if r["course"] == "K2"]),
        "PRODUCTION_QUEUE_v1.json")
    chk("NO_UNREAD_K3_ROW_IS_MARKED_EXTRACTED", EXTRACTION,
        [r["unit_id"] for r in queue["rows"]
         if r["course"] == "K3" and r["extraction_status"] == "CONNECTOR_TEXT_READ"
         and r["pl"] not in ("PL01", "PL03")], [],
        len([r for r in queue["rows"] if r["course"] == "K3"]),
        "PRODUCTION_QUEUE_v1.json")
    chk("EVERY_EXTRACTED_ROW_HAS_A_FILE_ON_DISK", EXTRACTION,
        [r["unit_id"] for r in queue["rows"]
         if r["extraction_status"] == "EXTRACTED"
         and not os.path.exists(os.path.join(
             BATCH1_DIR, r["unit_id"].replace("-", "_") + "_SOURCE_EXTRACT_v1.json"))
         and r["unit_id"] not in ("K5-PL06-T03-B02", "K5-PL06-T04-B01")], [],
        len(queue["rows"]), "docs/pl06/batch1_extract/")

    # ==================== 7. BOUNDARY AND LEAK ====================
    leak = EX.leak_report(extracts)
    chk("NO_UNIT_INHERITS_ANOTHER_UNITS_SOURCE_ROWS", BOUNDARY,
        [u["unit_id"] for u in leak["units"]
         if u["rows_landing_in_another_units_span"]], [], len(leak["units"]),
        "PL06_BATCH1_EXTRACTION_SUMMARY_v1.json")
    chk("NO_ROW_FALLS_OUTSIDE_ITS_OWN_SPAN", BOUNDARY,
        [u["unit_id"] for u in leak["units"]
         if u["paragraph_indices_outside_own_span"]], [], len(leak["units"]),
        "PL06_BATCH1_EXTRACTION_SUMMARY_v1.json")
    chk("THE_SHARED_PAGE_UNITS_ABUT_EXACTLY", BOUNDARY,
        [leak["adjacency"]["contiguous"], leak["adjacency"]["gap"]], [True, 0], 2,
        "PL06_BATCH1_EXTRACTION_SUMMARY_v1.json")
    chk("EVERY_UNIT_EMITS_ITS_EXCLUDED_NEIGHBOURS", BOUNDARY,
        [uid for uid, e in extracts.items()
         if not e["boundary_proof"]["excluded_before"]
         or not e["boundary_proof"]["excluded_after"]], [], len(extracts),
        "*_SOURCE_EXTRACT_v1.json")
    chk("EXTRACTION_WAS_NEVER_BY_PAGE_RANGE", BOUNDARY,
        sorted({e["boundary"]["extraction_method"] for e in extracts.values()}),
        ["HEADING_ANCHOR_BODY_CHILD_SLICE_NEVER_PAGE_RANGE"], len(extracts),
        "*_SOURCE_EXTRACT_v1.json")
    chk("EVERY_EXTRACT_RECORDS_ITS_ANCHOR_HIT_COUNT", BOUNDARY,
        [uid for uid, e in extracts.items()
         if e["boundary"]["anchor_search"]["start_hit_count"] < 1], [], len(extracts),
        "*_SOURCE_EXTRACT_v1.json")
    chk("EVERY_UNIT_ROW_CARRIES_ITS_OWN_UNIT_ID", BOUNDARY,
        [uid for uid, m in models.items()
         if not m["extraction_qa"]["every_row_carries_the_unit_id"]], [], len(models),
        "*_PROVISIONAL_MODEL_v1.json")

    # ==================== 8. QUEUE ====================
    chk("THE_QUEUE_HAS_ALL_FOURTEEN_COLUMNS", QUEUE, Q.COLUMNS,
        ["course", "pl", "unit_id", "source_binary_verified",
         "source_authority_inherited", "boundary_status", "extraction_status",
         "model_status", "pattern_decision_dependency", "storyboard_readiness",
         "qa_readiness", "bariah_review_dependency", "blocker", "next_executable_action"],
        14, "PRODUCTION_QUEUE_v1.json")
    chk("EVERY_QUEUE_ROW_HAS_EVERY_COLUMN", QUEUE,
        [r["unit_id"] for r in queue["rows"] if sorted(r) != sorted(Q.COLUMNS)], [],
        len(queue["rows"]), "PRODUCTION_QUEUE_v1.json")
    chk("EVERY_QUEUE_ROW_INHERITS_THE_AUTHORITY", QUEUE,
        [r["unit_id"] for r in queue["rows"]
         if r["source_authority_inherited"] != "SRC-AUTH-01"], [], len(queue["rows"]),
        "PRODUCTION_QUEUE_v1.json")
    chk("EVERY_QUEUE_ROW_NAMES_A_NEXT_ACTION", QUEUE,
        [r["unit_id"] for r in queue["rows"] if not r["next_executable_action"]], [],
        len(queue["rows"]), "PRODUCTION_QUEUE_v1.json")
    chk("EVERY_QUEUE_ROW_NAMES_A_BLOCKER_OR_SAYS_NONE", QUEUE,
        [r["unit_id"] for r in queue["rows"] if not r["blocker"]], [], len(queue["rows"]),
        "PRODUCTION_QUEUE_v1.json")
    chk("NO_QUEUE_ID_IS_DUPLICATED", QUEUE,
        len({r["unit_id"] for r in queue["rows"]}), len(queue["rows"]), len(queue["rows"]),
        "PRODUCTION_QUEUE_v1.json")
    # Percentages must be counted, not typed. Recompute independently and compare.
    n = len(queue["rows"])
    ext = len([r for r in queue["rows"]
               if r["extraction_status"] in ("EXTRACTED", "CONNECTOR_TEXT_READ")])
    chk("THE_EXTRACTED_PERCENTAGE_IS_COUNTED_NOT_TYPED", QUEUE,
        queue["extracted_percent"], round(100.0 * ext / n, 1), n,
        "PRODUCTION_QUEUE_v1.json")
    mr = len([r for r in queue["rows"] if r["model_status"] in ("MODEL_READY", "PACKAGED")])
    chk("THE_MODEL_READY_PERCENTAGE_IS_COUNTED_NOT_TYPED", QUEUE,
        queue["model_ready_percent"], round(100.0 * mr / n, 1), n,
        "PRODUCTION_QUEUE_v1.json")
    chk("EVERY_BLOCKER_HAS_A_NAMED_OWNER", QUEUE,
        [k for k in queue["blockers_by_owner"]
         if k not in ("BARIAH", "CAIR", "FIRDAUS", "none")], [],
        len(queue["blockers_by_owner"]), "PRODUCTION_QUEUE_v1.json")

    # ==================== 9. REGENERATION CANNOT REWRITE ANCHORS ====================
    # Every anchor is compared against the RAW frozen map, not against a second call of the
    # same generator. Fixture OR-07 moved an anchor and a re-run comparison saw nothing,
    # because both sides came through the patched extractor — the same self-referential
    # shape this project has now found five times.
    again = EX.extract_all()
    chk("REGENERATION_DOES_NOT_MOVE_A_FROZEN_ANCHOR", ORACLE,
        [uid for uid in extracts
         if (extracts[uid]["boundary"]["frozen_start_paragraph"],
             extracts[uid]["boundary"]["frozen_stop_paragraph"])
         != (raw_by[uid]["docx_para_start"], raw_by[uid]["docx_para_end_before"])], [],
        len(extracts), "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")
    chk("THE_ANCHORS_STILL_RESOLVE_TO_THE_SAME_HEADING_TEXT", ORACLE,
        [p["paragraph_index"] for p in k5["anchor_probes"] if not p["matches"]], [],
        len(k5["anchor_probes"]), "SOURCE_CUSTODY_MANIFEST_v1.json")
    chk("REGENERATION_IS_ROW_FOR_ROW_IDENTICAL", ORACLE,
        [uid for uid in extracts
         if [r["raw_source_text"] for r in extracts[uid]["rows"]]
         != [r["raw_source_text"] for r in again[uid]["rows"]]], [], len(extracts),
        "*_SOURCE_EXTRACT_v1.json")
    chk("THE_FROZEN_BOUNDARY_MAP_IS_UNMODIFIED", ORACLE,
        B._sha256(B.BOUNDARY_MAP_PATH), B.BOUNDARY_MAP_SHA256, 1,
        "source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json")

    # ==================== 10. ACCOUNTING ====================
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID, "PROJECT_SOURCE_CUSTODY_QA_v1", 1,
        "SOURCE_QA_REPORT_v1.md")
    chk("SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE", ACCOUNTING, SUITE_ID != PRIOR_SUITE_ID,
        True, 2, "SOURCE_QA_REPORT_v1.md")
    chk("NOT_CHECKED_IS_PUBLISHED", ACCOUNTING, len(NOT_CHECKED) >= 5, True,
        len(NOT_CHECKED), "SOURCE_QA_REPORT_v1.md")
    chk("EVERY_GATE_IS_TYPED", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [], len(res),
        "SOURCE_QA_REPORT_v1.md")
    chk("EVERY_GATE_NAMES_ITS_SOURCE_ARTIFACT", ACCOUNTING,
        [r["gate_id"] for r in res if not r["source_artifact"]], [], len(res),
        "SOURCE_QA_REPORT_v1.md")
    chk("NO_DUPLICATE_GATE_IDS", ACCOUNTING, len({r["gate_id"] for r in res}), len(res),
        len(res), "SOURCE_QA_REPORT_v1.md")
    chk("NO_VACUOUS_GATES", ACCOUNTING, [r["gate_id"] for r in res if r["vacuous"]], [],
        len(res), "SOURCE_QA_REPORT_v1.md")
    return res


def report(res):
    lines = []
    for r in res:
        flag = "PASS" if r["ok"] else ("VACUOUS" if r["vacuous"] else "FAIL")
        lines.append(f"{flag:5} {r['gate_type']:<11} {r['gate_id']:<58} "
                     f"n={r['population']:<5} {r['value']!r}")
    active = [r for r in res if not r["vacuous"]]
    lines += ["", f"SUITE_ID = {SUITE_ID}",
              f"{sum(1 for r in active if r['ok'])}/{len(active)} active gates PASS",
              f"VACUOUS_GATES = {[r['gate_id'] for r in res if r['vacuous']]}"]
    by = {}
    for r in res:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    for k in sorted(by):
        lines.append(f"    {k:<14} {by[k]}")
    return "\n".join(lines)


def emit_report(res):
    active = [r for r in res if not r["vacuous"]]
    by = {}
    for r in res:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    md = ["<!-- GENERATED by docs/source/tools/src_qa_v1.py -->", "",
          "# Targeted QA — source, extraction and queue", "", "```",
          f"SUITE_ID = {SUITE_ID}",
          f"GATES    = {len(res)}",
          f"PASS     = {sum(1 for r in active if r['ok'])}",
          f"FAIL     = {sum(1 for r in active if not r['ok'])}",
          f"VACUOUS  = {len(res) - len(active)}", "```", "",
          "Deliberately narrow. This suite covers the ten protections the run was asked to "
          "verify plus the new source and queue paths, and refactors nothing that already "
          f"exists. The prior suite is {PRIOR_SUITE_ID}; its gates and its total are its "
          "own and are never added to these.", "",
          "| type | gates |", "|---|---|"]
    md += [f"| {k} | {by[k]} |" for k in sorted(by)]
    md += ["", "| gate | type | population | source artifact | result |",
           "|---|---|---|---|---|"]
    md += [f"| `{r['gate_id']}` | {r['gate_type']} | {r['population']} | "
           f"`{r['source_artifact']}` | {'PASS' if r['ok'] else 'FAIL'} |" for r in res]
    md += ["", "## Not checked", ""] + [f"- {x}" for x in NOT_CHECKED] + [""]
    path = os.path.join(SRC_DIR, "SOURCE_QA_REPORT_v1.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    return path


if __name__ == "__main__":
    r = run()
    print(report(r))
    print("\nreport   :", emit_report(r))
    sys.exit(0 if all(x["ok"] for x in r if not x["vacuous"])
             and not any(x["vacuous"] for x in r) else 1)
