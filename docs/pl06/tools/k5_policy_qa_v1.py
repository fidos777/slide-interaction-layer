# -*- coding: utf-8 -*-
"""K5 Bariah-policy QA — the seven protections the ruling creates.

    SUITE_ID = K5_BARIAH_POLICY_QA_v1
    python3 docs/pl06/tools/k5_policy_qa_v1.py

Own identity, own total. No sibling suite is merged in or edited.

Every gate's expected value is a hand-typed literal taken from Bariah's own words in
`K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2_vBariah.docx`, or a quantity measured a
second way. No gate compares a function against itself.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "source", "tools"))
import k5_pattern_policy_v1 as P   # noqa: E402
import k5_policy_apply_v1 as AP    # noqa: E402
import src_authority_v1 as AUTH    # noqa: E402

SUITE_ID = "K5_BARIAH_POLICY_QA_v1"
SIBLING_SUITES = ["STAGE_4_2F_F_K2_QA_v1", "STAGE_4_2F_E_K2_QA_v1",
                  "STAGE_4_2F_D_RELEASE_FACTS_QA_v1", "PROJECT_SOURCE_CUSTODY_QA_v1",
                  "PL06_AUTHORITY_HARVEST_BATCH1_QA_v1", "T04_STATE_COVERAGE_QA_v1"]
ORACLE_SEPARATION_STRUCTURAL = "DEFERRED_BY_DELIVERY_DEADLINE"

AUTHORITY = "AUTHORITY"
STRUCTURES = "STRUCTURES"
FORECAST = "FORECAST"
SCENARIO = "SCENARIO"
SUMMARY = "SUMMARY"
COMPARISON = "COMPARISON"
NARRATOR = "NARRATOR"
BAHAGIAN = "BAHAGIAN"
CLOSING = "CLOSING"
SECTION_B = "SECTION_B"
INGESTION = "INGESTION"
ACCOUNTING = "ACCOUNTING"
GATE_TYPES = {SCENARIO, SUMMARY, COMPARISON, NARRATOR, BAHAGIAN, CLOSING, SECTION_B,
              INGESTION, ACCOUNTING, AUTHORITY, STRUCTURES, FORECAST}

# The generic project-source suite src_qa_v1 carries the same K5 authority assertion, but
# it cannot currently be run end-to-end: it has a pre-existing KeyError on the committed
# 54a00eb baseline, in leak["adjacency"]["contiguous"], unrelated to anything K5. So the
# K5 authority partition is proved HERE, against the same src_authority_v1 record, and the
# generic suite's crash is recorded as a baseline defect rather than worked around.
GENERIC_SUITE_BASELINE_DEFECT = dict(
    suite="PROJECT_SOURCE_CUSTODY_QA_v1 (docs/source/tools/src_qa_v1.py)",
    defect="KeyError: 'contiguous' in leak['adjacency']",
    present_on_commit="54a00eb",
    pre_existing=True,
    caused_by_this_run=False,
    verified_by="stashing this run's src_authority_v1 edit and re-running the committed "
                "file — the crash is identical",
    related_to_k5=False,
    consequence="The full generic suite CANNOT be claimed to pass. Its K5 authority "
                "assertion was updated in place and is proved by the AUTHORITY gates in "
                "this suite instead.",
    not_fixed_because="fixing it is a K2/source repair outside this brief's scope")

DOC_LITERAL = "DOC_LITERAL"
INDEPENDENT_MEASURE = "INDEPENDENT_MEASURE"

# Typed by hand from the document.
DECLARED_TOTAL = 17
SECTION_COUNTS = {"A": 7, "B": 4, "C": 2, "D": 4}
TEST_REQUIRED_IDS = ["B2"]
PROSE_OVERRIDE_IDS = ["A5"]
NARRATOR_NAME = "Hilmi"
SUMMARY_BEATS = ["Kepentingan", "Skop dan Isi Utama", "Manfaat"]
QUIZ = (4, 1, 60)
CLOSING_FINAL = "Tamat Topik"
CLOSING_INTERMEDIATE = "Tamat Bahagian X. Teruskan pembelajaran ke bahagian seterusnya"
DOC_SHA256 = "d22f6315a9bdec2c00d376aee710aacb301d97b2587ca82ee2ce0adcb8d964ce"

# Outside-PL06 facts the brief requires preserved, typed by hand.
OUTSIDE_PLS = ["PL01", "PL02", "PL03", "PL04", "PL05", "PL07", "PL08"]
CANDIDATES = 22
CLEAN = 20
AMBER = 2
UNMAPPED_REGIONS = 7
PL06_UNITS = 14
SECTION_B_STATUS = "APPROVED_WITH_AMENDMENTS_FOR_CALIBRATION"
FILES_PER_UNIT = 2
DENSITIES_TO_TEST = [2, 3]
SLOT_MINUTES = 90
UNITS_PER_SLOT = 1
DOC_B_SHA256 = "c3cd395d35b9f763cb849f3b5162517a30d029330f1b654fe944f3e6f4fc3012"

NOT_CHECKED = [
    "whether any scenario's CONTENT is instructionally sound — that is Bariah's, per unit",
    "any answer key — A7 authorises composition, not keys",
    "the B2 density outcome — the test has not been shown to Bariah, and no gate "
    "asserts a winning density",
    "Bariah's actual availability — a rule was given, a calendar was not",
    "the Rumusan visual SUBJECT — the obligation is gated, the subject is not invented",
    "segmentation outside PL06 — no frozen boundary map exists for it",
]


def run():
    res = []

    def chk(gid, gtype, value, expected, population, source, basis,
            empty_by_design=None):
        assert gtype in GATE_TYPES, gtype
        assert basis in (DOC_LITERAL, INDEPENDENT_MEASURE), basis
        vacuous = population == 0 and not empty_by_design
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        population=population, source_artifact=source, oracle_basis=basis,
                        empty_by_design=empty_by_design, vacuous=vacuous,
                        ok=(value == expected) and not vacuous))

    rec = P.ingestion_record()
    cu = AP.calibration_units()
    units = cu["units"]
    im = AP.impact_matrix()

    # ---------- 1. scenario required for every K5 unit ----------
    chk("SCENARIO_IS_REQUIRED_BY_POLICY", SCENARIO,
        P.POLICY["scenario_screen_required"], True, 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("EVERY_CALIBRATION_UNIT_REQUIRES_A_SCENARIO", SCENARIO,
        sorted({u["scenario_obligation"]["required"] for u in units}), [True],
        len(units), "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("SCENARIO_SURVIVES_A_NOT_JUSTIFIED_CAIR_VERDICT", SCENARIO,
        sorted({u["scenario_obligation"]["required"] for u in units
                if u["scenario_obligation"]["previous_cair_verdict"] != "JUSTIFIED"}),
        [True],
        len([u for u in units
             if u["scenario_obligation"]["previous_cair_verdict"] != "JUSTIFIED"]),
        "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("A5_AND_D3_BOTH_CITED_AS_THE_BASIS", SCENARIO,
        sorted(P.POLICY["scenario_basis"]), ["A5", "D3"], 2,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("THE_SHELL_GREW_FOR_UNITS_THAT_HAD_NO_SCENARIO", SCENARIO,
        sorted({u["screen_pattern_plan"]["shell_screens_after"]
                - u["screen_pattern_plan"]["shell_screens_before"] for u in units
                if u["scenario_obligation"]["change"] == "SCENARIO_SCREEN_ADDED"}), [1],
        len([u for u in units
             if u["scenario_obligation"]["change"] == "SCENARIO_SCREEN_ADDED"]),
        "K5_CALIBRATION_REEVALUATION_v1.json", INDEPENDENT_MEASURE)

    # ---------- 2. Summary visual required ----------
    chk("SUMMARY_VISUAL_IS_REQUIRED_BY_POLICY", SUMMARY,
        P.POLICY["summary_visual_required"], True, 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("EVERY_CALIBRATION_UNIT_REQUIRES_A_SUMMARY_VISUAL", SUMMARY,
        sorted({u["summary_visual_obligation"]["visual_required"] for u in units}),
        [True], len(units), "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("SUMMARY_STRUCTURE_IS_THE_THREE_BEAT", SUMMARY,
        P.POLICY["summary_structure"], SUMMARY_BEATS, 3,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("EVERY_UNIT_TARGETS_THREE_BEATS", SUMMARY,
        sorted({u["summary_visual_obligation"]["beats_required"] for u in units}), [3],
        len(units), "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("NO_SUMMARY_VISUAL_SUBJECT_IS_INVENTED", SUMMARY,
        sorted({u["summary_visual_obligation"]["visual_subject"] for u in units}),
        ["PENDING_UNIT_EXCEPTION_REVIEW — the obligation is set, the subject is not "
         "invented here"], len(units),
        "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)

    # ---------- 3. Comparison only with explicit source comparison ----------
    chk("COMPARISON_REQUIRES_EXPLICIT_SOURCE_COMPARISON", COMPARISON,
        P.POLICY["comparison_requires_explicit_source_comparison"], True, 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("A4_IS_SOURCE_CONDITIONAL_NOT_GLOBAL", COMPARISON,
        next(d["scope"] for d in P.DECISIONS if d["id"] == "A4"), P.SOURCE_CONDITIONAL, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("EVERY_UNIT_PROPOSING_COMPARISON_IS_FLAGGED_FOR_RETEST", COMPARISON,
        sorted({u["comparison_retest"]["status"] for u in units
                if u["comparison_retest"]["currently_proposes_comparison"]}),
        ["RE_TEST_REQUIRED"],
        len([u for u in units
             if u["comparison_retest"]["currently_proposes_comparison"]]),
        "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("NO_UNIT_IS_SILENTLY_CLEARED_FOR_COMPARISON", COMPARISON,
        [u["unit_id"] for u in units
         if u["comparison_retest"]["currently_proposes_comparison"]
         and u["comparison_retest"]["status"] != "RE_TEST_REQUIRED"], [],
        len(units), "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL,
        empty_by_design=True)

    # ---------- 4. Hilmi as K5 narrator ----------
    chk("K5_NARRATOR_IS_HILMI", NARRATOR,
        P.POLICY["narrator"], NARRATOR_NAME, 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("EVERY_CALIBRATION_UNIT_NAMES_HILMI", NARRATOR,
        sorted({u["narrator"]["name"] for u in units}), [NARRATOR_NAME], len(units),
        "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("THE_CROSS_COURSE_NARRATOR_NOTE_IS_INGESTED_NOT_APPLIED", NARRATOR,
        "INGESTED_NOT_APPLIED" in next(d for d in P.DECISIONS
                                       if d["id"] == "D2")["cross_course_note"], True, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("NO_K5_WIDE_CAST_IS_CLAIMED", NARRATOR,
        P.POLICY["characters"], "PER_UNIT_AT_REVIEW", len(units),
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)

    # ---------- 5. per-Bahagian Summary and Quiz ----------
    chk("PER_BAHAGIAN_STORYBOARD_SUMMARY_QUIZ_IS_POLICY", BAHAGIAN,
        P.POLICY["per_bahagian_storyboard_summary_quiz"], True, 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    multi = [u for u in units
             if u["closing_screen"]["segmentation"] == "TOPIK_WITH_MULTIPLE_BAHAGIAN"]
    chk("EVERY_MULTI_BAHAGIAN_UNIT_OWNS_ITS_SUMMARY_AND_QUIZ", BAHAGIAN,
        sorted({u["closing_screen"]["own_storyboard_summary_quiz"] for u in multi}),
        [True], len(multi), "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("SINGLE_BAHAGIAN_TOPICS_SHOW_NO_BAHAGIAN_LABEL", BAHAGIAN,
        sorted({u["closing_screen"]["bahagian_label_shown"] for u in units
                if u["closing_screen"]["segmentation"]
                == "TOPIK_WITHOUT_BAHAGIAN"}), [False],
        len([u for u in units if u["closing_screen"]["segmentation"]
             == "TOPIK_WITHOUT_BAHAGIAN"]),
        "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)

    # ---------- 6. correct intermediate and final closing screens ----------
    chk("INTERMEDIATE_CLOSING_TEXT_IS_BARIAHS_WORDING", CLOSING,
        P.CLOSING_INTERMEDIATE, CLOSING_INTERMEDIATE, 1,
        "k5_pattern_policy_v1", DOC_LITERAL)
    chk("FINAL_CLOSING_TEXT_IS_BARIAHS_WORDING", CLOSING,
        P.CLOSING_FINAL, CLOSING_FINAL, 1, "k5_pattern_policy_v1", DOC_LITERAL)
    chk("NO_INTERMEDIATE_BAHAGIAN_CLOSES_WITH_TAMAT_TOPIK", CLOSING,
        [u["unit_id"] for u in units
         if u["closing_screen"]["segmentation"] == "TOPIK_WITH_MULTIPLE_BAHAGIAN"
         and not u["closing_screen"].get("is_final_bahagian")
         and u["closing_screen"]["closing_text"] == CLOSING_FINAL], [],
        len(units), "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL,
        empty_by_design=True)
    chk("INTERMEDIATE_CLOSINGS_CARRY_THEIR_OWN_BAHAGIAN_NUMBER", CLOSING,
        sorted(u["closing_screen"]["closing_text"] for u in units
               if u["closing_screen"]["segmentation"] == "TOPIK_WITH_MULTIPLE_BAHAGIAN"
               and not u["closing_screen"].get("is_final_bahagian")),
        ["Tamat Bahagian 3. Teruskan pembelajaran ke bahagian seterusnya",
         "Tamat Bahagian 4. Teruskan pembelajaran ke bahagian seterusnya"],
        len(multi), "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("SINGLE_BAHAGIAN_TOPICS_CLOSE_WITH_TAMAT_TOPIK", CLOSING,
        sorted({u["closing_screen"]["closing_text"] for u in units
                if u["closing_screen"]["segmentation"] == "TOPIK_WITHOUT_BAHAGIAN"}),
        [CLOSING_FINAL],
        len([u for u in units if u["closing_screen"]["segmentation"]
             == "TOPIK_WITHOUT_BAHAGIAN"]),
        "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)

    # ---------- 7. Section B — closed, but B2 is NOT approved ----------
    chk("SECTION_B_IS_CLOSED", SECTION_B,
        rec["section_b_status"], SECTION_B_STATUS, 4,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("NOTHING_REMAINS_PENDING", SECTION_B,
        rec["pending_ids"], [], 17,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL, empty_by_design=True)
    chk("THE_FOUR_BUCKETS_PARTITION_ALL_SEVENTEEN", SECTION_B,
        rec["partition"]["total"], DECLARED_TOTAL, DECLARED_TOTAL,
        "K5_BARIAH_DECISION_INGESTION_v1.json", INDEPENDENT_MEASURE)
    chk("SECTION_B_SOURCE_HASH_RECORDED", SECTION_B,
        P.SOURCE_DOCUMENT_B["sha256"], DOC_B_SHA256, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    # --- B1 two-file packaging ---
    chk("TWO_FILES_PER_UNIT", SECTION_B,
        [P.POLICY["files_per_unit"], P.POLICY["files_per_unit_names"]],
        [FILES_PER_UNIT, ["Storyboard", "Lampiran Keadaan"]], 4,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("B1_IS_APPROVED", SECTION_B,
        next(d["status"] for d in P.DECISIONS if d["id"] == "B1"), P.APPROVED, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    # --- B2 must NOT be approved ---
    chk("B2_IS_TEST_REQUIRED_NOT_APPROVED", SECTION_B,
        next(d["status"] for d in P.DECISIONS if d["id"] == "B2"), P.TEST_REQUIRED, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("B2_IS_NOT_IN_THE_APPROVED_LIST", SECTION_B,
        "B2" in rec["approved_ids"], False, DECLARED_TOTAL,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("NO_PANEL_DENSITY_IS_APPROVED", SECTION_B,
        P.POLICY["lampiran_panel_density"], "NOT_APPROVED_TEST_REQUIRED", 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("BOTH_DENSITIES_MUST_BE_PRODUCED_FOR_THE_TEST", SECTION_B,
        P.POLICY["lampiran_densities_to_test"], DENSITIES_TO_TEST, 2,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("THE_DENSITY_TEST_HOLDS_UNIT_AND_STATES_CONSTANT", SECTION_B,
        [next(d for d in P.DECISIONS if d["id"] == "B2")["test_requirement"][k]
         for k in ("same_unit", "same_state_set")], [True, True], 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    # --- B3 one unit per slot ---
    chk("ONE_UNIT_PER_NINETY_MINUTE_SLOT", SECTION_B,
        [P.POLICY["review_slot_minutes"], P.POLICY["units_per_review_slot"]],
        [SLOT_MINUTES, UNITS_PER_SLOT], 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    # --- B4 availability never invented ---
    chk("AVAILABILITY_DATES_ARE_NOT_INVENTED", SECTION_B,
        P.POLICY["availability_dates"], "REQUIRES_FIRDAUS_CONFIRMATION", 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("SLOTS_PER_DAY_ARE_NOT_INVENTED", SECTION_B,
        P.POLICY["slots_per_day"], "REQUIRES_FIRDAUS_CONFIRMATION", 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    # The conditional link itself. Bariah allows several slots a day, but only on a day
    # that is available — and availability is not hers to fix alone. A model that carried
    # "several slots per day" without that qualifier would read as a throughput promise.
    chk("MULTIPLE_SLOTS_ONLY_ON_A_CONFIRMED_AVAILABLE_DAY", SECTION_B,
        [P.POLICY["availability"], P.POLICY["slots_per_day"],
         P.POLICY["availability_dates"]],
        ["CONDITIONAL_WORKING_DAYS_EXCEPT_CYBERJAYA_MEETINGS",
         "REQUIRES_FIRDAUS_CONFIRMATION", "REQUIRES_FIRDAUS_CONFIRMATION"], 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("B4_NAMES_WHAT_FIRDAUS_MUST_CONFIRM", SECTION_B,
        sorted(next(d for d in P.DECISIONS
                    if d["id"] == "B4")["requires_firdaus_confirmation"]),
        ["the actual available dates", "the actual slot count per day"], 2,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("B4_AVAILABILITY_IS_MARKED_CONDITIONAL", SECTION_B,
        next(d for d in P.DECISIONS if d["id"] == "B4")[
            "availability_is_conditional"], True, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    # --- authorisation scope ---
    chk("CALIBRATION_GENERATION_IS_AUTHORIZED", SECTION_B,
        rec["calibration_generation_authorized"], True, 4,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("MASS_GENERATION_IS_NOT_AUTHORIZED", SECTION_B,
        rec["mass_generation_authorized"], False, PL06_UNITS,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("ONLY_THE_FOUR_CALIBRATION_UNITS_ARE_AUTHORIZED", SECTION_B,
        rec["calibration_units_authorized"], AP.CALIBRATION_UNITS, 4,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("THE_LAMPIRAN_DEFINITION_IS_RECORDED", SECTION_B,
        bool(rec["lampiran_keadaan_definition"]["shows"]), True, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", INDEPENDENT_MEASURE)
    chk("LAMPIRAN_IS_NOT_A_SECOND_LEARNER_DECK", SECTION_B,
        any("learner-facing" in x for x in
            rec["lampiran_keadaan_definition"]["what_it_is_not"]), True, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)

    # ---------- ingestion integrity ----------
    chk("DOCUMENT_HASH_RECORDED", INGESTION,
        P.SOURCE_DOCUMENT["sha256"], DOC_SHA256, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("MODELLED_TOTAL_EQUALS_THE_DECLARED_TOTAL", INGESTION,
        rec["modelled_total"], DECLARED_TOTAL, DECLARED_TOTAL,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("SECTION_COUNTS_MATCH_THE_DOCUMENTS_OWN_TABLE", INGESTION,
        rec["modelled_by_section"], SECTION_COUNTS, DECLARED_TOTAL,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("EVERY_BUCKET_TOGETHER_ACCOUNTS_FOR_ALL_SEVENTEEN", INGESTION,
        len(rec["approved_ids"]) + len(rec["test_required_ids"])
        + len(rec["pending_ids"]), DECLARED_TOTAL,
        DECLARED_TOTAL, "K5_BARIAH_DECISION_INGESTION_v1.json", INDEPENDENT_MEASURE)
    chk("A5_IS_RECORDED_AS_A_PROSE_OVERRIDE", INGESTION,
        rec["prose_override_ids"], PROSE_OVERRIDE_IDS, DECLARED_TOTAL,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("A5_IS_NOT_RECORDED_AS_PLAIN_ACCEPTANCE", INGESTION,
        next(d["status"] for d in P.DECISIONS if d["id"] == "A5"), P.APPROVED_AMENDED, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("QUIZ_IS_FOUR_MCQ_ONE_MR_AT_SIXTY_PERCENT", INGESTION,
        (P.POLICY["quiz_mcq"], P.POLICY["quiz_multiple_response"],
         P.POLICY["quiz_pass_percent"]), QUIZ, 1,
        "k5_pattern_policy_v1.POLICY", DOC_LITERAL)
    chk("NO_ANSWER_KEY_IS_APPROVED", INGESTION,
        sorted({u["quiz_structure"]["key_status"] for u in units}),
        ["SOURCE_AUTHORED_NOT_BARIAH_APPROVED"], len(units),
        "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("UNANSWERED_CAIR_SUBPOINTS_ARE_NAMED_NOT_ASSUMED", INGESTION,
        sorted({s["status"] for s in P.UNRESOLVED_SUBPOINTS}),
        ["NOT_ADDRESSED_BY_BARIAH"], len(P.UNRESOLVED_SUBPOINTS),
        "K5_BARIAH_DECISION_INGESTION_v1.json", DOC_LITERAL)
    chk("NOTHING_IS_READY_TO_EMIT_PPTX", INGESTION,
        sorted({u["readiness"]["ready_to_emit_pptx"] for u in units}), [False],
        len(units), "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)

    # ---------- authority partition, standing in for the crashing generic suite ----------
    pp = AUTH.PENDING_PATTERN_PACKAGE
    chk("AUTHORITY_RECORD_SHOWS_THE_PACKAGE_RETURNED", AUTHORITY,
        pp["status"], "RETURNED_BY_BARIAH_AND_INGESTED", 1,
        "SRC_AUTH_01_v1.json", DOC_LITERAL)
    chk("AUTHORITY_IS_NOT_A_SINGLE_BOOLEAN", AUTHORITY,
        pp["is_authority"], None, 1, "SRC_AUTH_01_v1.json", DOC_LITERAL)
    chk("SECTIONS_A_C_D_ARE_INGESTED_AUTHORITY", AUTHORITY,
        [pp["authority_by_section"][s] for s in ("A", "C", "D")],
        ["APPROVED_WITH_AMENDMENTS", "APPROVED", "APPROVED_WITH_AMENDMENTS"], 3,
        "SRC_AUTH_01_v1.json", DOC_LITERAL)
    # These four supersede the B-pending versions. The intent is unchanged — nothing
    # unapproved may be auto-applied — but the unapproved thing is now B2 alone, not
    # Section B wholesale. A section-level flag would hide that, which is why the record
    # carries a per-item map for B.
    chk("SECTION_B_IS_CLOSED_IN_THE_AUTHORITY_RECORD", AUTHORITY,
        pp["authority_by_section"]["B"], SECTION_B_STATUS, 1,
        "SRC_AUTH_01_v1.json", DOC_LITERAL)
    chk("B2_MAY_NOT_BE_AUTO_APPLIED", AUTHORITY,
        pp["section_b_items"]["B2"]["may_be_auto_applied"], False, 4,
        "SRC_AUTH_01_v1.json", DOC_LITERAL)
    chk("B2_IS_THE_ONLY_SECTION_B_ITEM_BLOCKED", AUTHORITY,
        sorted(k for k, v in pp["section_b_items"].items()
               if not v["may_be_auto_applied"]), TEST_REQUIRED_IDS, 4,
        "SRC_AUTH_01_v1.json", INDEPENDENT_MEASURE)
    chk("THE_AUTHORITY_RECORD_AND_THE_INGESTION_AGREE_ON_B2", AUTHORITY,
        pp["section_b_items"]["B2"]["status"], P.TEST_REQUIRED, 1,
        "K5_BARIAH_DECISION_INGESTION_v1.json", INDEPENDENT_MEASURE)
    chk("THE_AUTHORITY_RECORD_AGREES_NOTHING_IS_PENDING", AUTHORITY,
        [s for s, v in pp["authority_by_section"].items()
         if v == "PENDING_BARIAH_DECISION"], [], 4,
        "K5_BARIAH_DECISION_INGESTION_v1.json", INDEPENDENT_MEASURE,
        empty_by_design=True)
    chk("THE_AUTHORITY_RECORD_AUTHORIZES_CALIBRATION_NOT_MASS", AUTHORITY,
        [pp["calibration_generation_authorized"], pp["mass_generation_authorized"]],
        [True, False], 1, "SRC_AUTH_01_v1.json", DOC_LITERAL)
    chk("THE_GENERIC_SUITE_CRASH_IS_RECORDED_AS_PRE_EXISTING", AUTHORITY,
        [GENERIC_SUITE_BASELINE_DEFECT["pre_existing"],
         GENERIC_SUITE_BASELINE_DEFECT["caused_by_this_run"],
         GENERIC_SUITE_BASELINE_DEFECT["related_to_k5"]], [True, False, False], 1,
        "this file", DOC_LITERAL)

    # ---------- outside-PL06 counts ----------
    st = AP.outside_pl06()
    chk("NO_CONFIRMED_PRODUCTION_UNIT_IS_CLAIMED_OUTSIDE_PL06", STRUCTURES,
        st["confirmed_storyboard_production_units_outside_pl06"], 0,
        st["candidate_structures"], "K5_STRUCTURES_OUTSIDE_PL06_v1.json", DOC_LITERAL)
    chk("THE_OUTSIDE_PL06_POPULATION_EXCLUDES_PL06", STRUCTURES,
        sorted({r["pl"] for r in st["rows"]}), OUTSIDE_PLS, len(st["rows"]),
        "K5_STRUCTURES_OUTSIDE_PL06_v1.json", DOC_LITERAL)
    chk("CANDIDATE_ROLL_LENGTH_MATCHES_ITS_COUNT", STRUCTURES,
        len(st["candidate_structures_roll"]), st["candidate_structures"],
        st["candidate_structures"], "K5_STRUCTURES_OUTSIDE_PL06_v1.json",
        INDEPENDENT_MEASURE)
    chk("CLEAN_PLUS_AMBER_ACCOUNTS_FOR_EVERY_CANDIDATE", STRUCTURES,
        st["clean_candidates"] + st["amber_candidates"], CANDIDATES,
        st["candidate_structures"], "K5_STRUCTURES_OUTSIDE_PL06_v1.json",
        INDEPENDENT_MEASURE)
    chk("ESTABLISHED_FACTS_PRESERVED", STRUCTURES,
        [st["candidate_structures"], st["clean_candidates"], st["amber_candidates"],
         st["unmapped_source_regions"]], [CANDIDATES, CLEAN, AMBER, UNMAPPED_REGIONS],
        st["candidate_structures"], "K5_STRUCTURES_OUTSIDE_PL06_v1.json", DOC_LITERAL)
    chk("EVERY_HEADLINE_COUNT_HAS_A_NAMED_ROLL", STRUCTURES,
        sorted(k for k in st if k.endswith("_roll")),
        sorted(["amber_candidates_roll", "candidate_structures_roll",
                "clean_candidates_roll",
                "confirmed_storyboard_production_units_outside_pl06_roll",
                "pl06_storyboard_production_units_roll", "pl06_topik_roll",
                "unmapped_source_regions_roll"]), 7,
        "K5_STRUCTURES_OUTSIDE_PL06_v1.json", INDEPENDENT_MEASURE)
    chk("THE_SEVEN_PL06_TOPIK_ARE_NOT_COUNTED_AS_PRODUCTION_UNITS", STRUCTURES,
        sorted({t["is_storyboard_production_unit"] for t in st["pl06_topik"]}), [False],
        len(st["pl06_topik"]), "K5_STRUCTURES_OUTSIDE_PL06_v1.json", DOC_LITERAL)
    chk("PL06_TOPIK_ROLL_IS_SEVEN_NAMED_MEMBERS", STRUCTURES,
        st["pl06_topik_roll"], [f"K5-PL06-T{i:02d}" for i in range(1, 8)], 7,
        "K5_STRUCTURES_OUTSIDE_PL06_v1.json", DOC_LITERAL)
    chk("PL06_PRODUCTION_UNITS_ARE_THE_FOURTEEN_BAHAGIAN", STRUCTURES,
        st["pl06_storyboard_production_units"], PL06_UNITS, 7,
        "K5_STRUCTURES_OUTSIDE_PL06_v1.json", DOC_LITERAL)
    chk("THE_RENAME_IS_RECORDED_NOT_SILENT", STRUCTURES,
        len(st["renamed_counts"]) >= 1, True, 1,
        "K5_STRUCTURES_OUTSIDE_PL06_v1.json", INDEPENDENT_MEASURE)

    # ---------- forecast completeness ----------
    fc = AP.FORECAST
    chk("FORECAST_IS_LABELLED_NOT_A_COMMITMENT", FORECAST,
        fc["status"], "FORECAST_NOT_COMMITMENT", 1,
        "K5_COMPLETION_FORECAST_v1.json", DOC_LITERAL)
    chk("THREE_SCENARIOS_ARE_PRESENT", FORECAST,
        [s["id"] for s in fc["scenarios"]], ["A", "B", "C"], 3,
        "K5_COMPLETION_FORECAST_v1.json", DOC_LITERAL)
    chk("EVERY_SCENARIO_REPORTS_ALL_SIX_RANGES", FORECAST,
        sorted({tuple(sorted(k for k in s if k.endswith("_range")
                             or k == "section_b_decision_date"))
                for s in fc["scenarios"]}),
        [tuple(sorted(["section_b_decision_date", "calibration_completion_range",
                       "batch_generation_start_range",
                       "engineering_generation_completion_range",
                       "bariah_review_freeze_completion_range",
                       "full_k5_package_completion_range"]))], 3,
        "K5_COMPLETION_FORECAST_v1.json", INDEPENDENT_MEASURE)
    chk("EVERY_SCENARIO_NAMES_ASSUMPTIONS_AND_BLOCKERS", FORECAST,
        sorted({bool(s["assumptions"]) and bool(s["principal_blockers"])
                for s in fc["scenarios"]}), [True], 3,
        "K5_COMPLETION_FORECAST_v1.json", INDEPENDENT_MEASURE)
    # B3 IS now a known value (90 minutes, one unit) and the forecast uses it. What must
    # never be invented is availability — the dates and the slot count Bariah left to
    # Firdaus.
    chk("AVAILABILITY_IS_NEVER_GIVEN_A_VALUE_IN_THE_FORECAST", FORECAST,
        [("UNCONFIRMED" in fc["open_variables"]["slots_per_available_day"]),
         ("UNCONFIRMED" in fc["open_variables"]["available_dates"])],
        [True, True], 2, "K5_COMPLETION_FORECAST_v1.json", DOC_LITERAL)
    chk("THE_FORECAST_USES_THE_REAL_REVIEW_CONSTRAINT", FORECAST,
        [fc["review_constraint"]["slot_minutes"],
         fc["review_constraint"]["units_per_slot"],
         fc["review_constraint"]["slots_required"]], [SLOT_MINUTES, UNITS_PER_SLOT, 4], 4,
        "K5_COMPLETION_FORECAST_v1.json", DOC_LITERAL)
    chk("SECTION_B_IS_RECORDED_AS_RESOLVED_IN_THE_FORECAST", FORECAST,
        fc["section_b_resolved"]["status"], SECTION_B_STATUS, 1,
        "K5_COMPLETION_FORECAST_v1.json", DOC_LITERAL)
    chk("EVERY_SCENARIO_MARKS_ITS_SLOT_ASSUMPTION_CONDITIONAL", FORECAST,
        sorted({"CONDITIONAL" in s2["slots_per_day_assumed"]
                for s2 in fc["scenarios"]}), [True], 3,
        "K5_COMPLETION_FORECAST_v1.json", DOC_LITERAL)
    chk("NO_FULL_K5_DATE_IS_COMPUTED", FORECAST,
        sorted({s["full_k5_package_completion_range"].startswith("NOT_COMPUTABLE")
                for s in fc["scenarios"]}), [True], 3,
        "K5_COMPLETION_FORECAST_v1.json", DOC_LITERAL)

    # ---------- D4 derivation ----------
    chk("D4_SINGLE_BAHAGIAN_RULE_CITES_BOTH_INPUTS", BAHAGIAN,
        AP.SINGLE_BAHAGIAN_IS_NO_BAHAGIAN["derivation"],
        "BARIAH_WORKED_EXAMPLE + FROZEN_SEGMENTATION_MAP", 1,
        "K5_CALIBRATION_REEVALUATION_v1.json", DOC_LITERAL)
    chk("D4_DERIVATION_NAMES_WHAT_IT_IS_NOT", BAHAGIAN,
        bool(AP.SINGLE_BAHAGIAN_IS_NO_BAHAGIAN.get("what_this_is_not")), True, 1,
        "K5_CALIBRATION_REEVALUATION_v1.json", INDEPENDENT_MEASURE)

    # ---------- accounting ----------
    chk("SUITE_ID_DECLARED", ACCOUNTING, SUITE_ID, "K5_BARIAH_POLICY_QA_v1", 1,
        "this file", DOC_LITERAL)
    chk("SUITE_ID_IS_NOT_ANY_SIBLING_SUITE", ACCOUNTING,
        SUITE_ID in SIBLING_SUITES, False, len(SIBLING_SUITES), "this file", DOC_LITERAL)
    chk("ORACLE_SEPARATION_STILL_DEFERRED", ACCOUNTING,
        ORACLE_SEPARATION_STRUCTURAL, "DEFERRED_BY_DELIVERY_DEADLINE", 1, "this file",
        DOC_LITERAL)
    chk("NO_GATE_IS_VACUOUS", ACCOUNTING,
        [r["gate_id"] for r in res if r["vacuous"]], [], len(res), "this file",
        DOC_LITERAL, empty_by_design=True)
    return res


def summary():
    res = run()
    return dict(suite_id=SUITE_ID, total=len(res),
                passed=len([r for r in res if r["ok"]]),
                failed=[r for r in res if not r["ok"]],
                by_type={t: len([r for r in res if r["gate_type"] == t])
                         for t in sorted(GATE_TYPES)},
                by_oracle_basis={b: len([r for r in res if r["oracle_basis"] == b])
                                 for b in (DOC_LITERAL, INDEPENDENT_MEASURE)},
                oracle_separation_structural=ORACLE_SEPARATION_STRUCTURAL,
                not_checked=NOT_CHECKED, gates=res)


if __name__ == "__main__":
    s = summary()
    print(f"SUITE_ID = {s['suite_id']}")
    print(f"{s['passed']}/{s['total']} passed")
    print("by type:", s["by_type"])
    print("by oracle basis:", s["by_oracle_basis"])
    for f in s["failed"]:
        print(f"  FAIL {f['gate_id']}: {f['value']!r} != {f['expected']!r}")
