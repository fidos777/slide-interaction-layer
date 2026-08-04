# -*- coding: utf-8 -*-
"""Negative mutations for the K5 Bariah policy.

    SUITE_ID = K5_BARIAH_POLICY_QA_v1
    python3 docs/pl06/tools/k5_policy_mutations_v1.py

The defect this ingestion could most easily have committed is reading a ticked box and
stopping there — shipping CAIR's original wording as if Bariah had accepted it, when her
prose says the opposite. A5 is the live case; the fixtures below attack it and every
sibling failure mode the ruling creates, including the one that matters most for
governance: a Section B choice quietly acquiring an answer.
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import k5_pattern_policy_v1 as P   # noqa: E402
import k5_policy_apply_v1 as AP    # noqa: E402
import k5_policy_qa_v1 as QA       # noqa: E402
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "source", "tools"))
import src_authority_v1 as AUTH    # noqa: E402

TARGETS = {"P": P, "AP": AP, "QA": QA, "AUTH": AUTH}
_BASE_UNITS = _BASE_MATRIX = _BASE_OUTSIDE = None


def _units(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_UNITS)
            fn(d)
            return d
        return dict(calibration_units=patched)
    return apply


def _outside(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_OUTSIDE)
            fn(d)
            return d
        return dict(outside_pl06=patched)
    return apply


def _matrix(fn):
    def apply():
        def patched():
            d = copy.deepcopy(_BASE_MATRIX)
            fn(d)
            return d
        return dict(impact_matrix=patched)
    return apply


def _dec(did, **kw):
    """Replace one decision in P.DECISIONS."""
    return lambda: dict(DECISIONS=[dict(d, **kw) if d["id"] == did else d
                                   for d in P.DECISIONS])


def _u(d, uid):
    return next(u for u in d["units"] if u["unit_id"] == uid)


FIXTURES = [
    # ---------------- missing scenario ----------------
    dict(fid="KS-01", title="the scenario obligation is switched off globally", target="P",
         gates=["SCENARIO_IS_REQUIRED_BY_POLICY", "A5_AND_D3_BOTH_CITED_AS_THE_BASIS"],
         patch=lambda: dict(POLICY=dict(P.POLICY, scenario_screen_required=False,
                                        scenario_basis=["D3"]))),
    dict(fid="KS-02", title="one unit loses its scenario requirement", target="AP",
         gates=["EVERY_CALIBRATION_UNIT_REQUIRES_A_SCENARIO",
                "SCENARIO_SURVIVES_A_NOT_JUSTIFIED_CAIR_VERDICT"],
         patch=_units(lambda d: _u(d, "K5-PL06-T03-B03")["scenario_obligation"].update(
             required=False))),
    dict(fid="KS-03", title="a NOT_JUSTIFIED CAIR verdict is allowed to remove the screen",
         target="AP", gates=["SCENARIO_SURVIVES_A_NOT_JUSTIFIED_CAIR_VERDICT",
                             "EVERY_CALIBRATION_UNIT_REQUIRES_A_SCENARIO"],
         patch=_units(lambda d: [u["scenario_obligation"].update(required=False)
                                 for u in d["units"]
                                 if u["scenario_obligation"]["previous_cair_verdict"]
                                 == "NOT_JUSTIFIED"])),
    dict(fid="KS-04", title="the shell is not grown for a unit that gained a scenario",
         target="AP", gates=["THE_SHELL_GREW_FOR_UNITS_THAT_HAD_NO_SCENARIO"],
         patch=_units(lambda d: _u(d, "K5-PL06-T06-B01")["screen_pattern_plan"].update(
             shell_screens_after=2))),
    dict(fid="KS-05", title="A5 is recorded as plain acceptance of the CAIR wording",
         target="P", gates=["A5_IS_NOT_RECORDED_AS_PLAIN_ACCEPTANCE",
                            "A5_IS_RECORDED_AS_A_PROSE_OVERRIDE"],
         patch=_dec("A5", status=P.APPROVED, prose_overrides_checkbox=False)),

    # ---------------- missing Summary visual ----------------
    dict(fid="KV-01", title="the Summary visual obligation is switched off", target="P",
         gates=["SUMMARY_VISUAL_IS_REQUIRED_BY_POLICY"],
         patch=lambda: dict(POLICY=dict(P.POLICY, summary_visual_required=False))),
    dict(fid="KV-02", title="one unit's Summary visual becomes optional", target="AP",
         gates=["EVERY_CALIBRATION_UNIT_REQUIRES_A_SUMMARY_VISUAL"],
         patch=_units(lambda d: _u(d, "K5-PL06-T05-B01")[
             "summary_visual_obligation"].update(visual_required=False))),
    dict(fid="KV-03", title="the three-beat structure is replaced", target="P",
         gates=["SUMMARY_STRUCTURE_IS_THE_THREE_BEAT"],
         patch=lambda: dict(POLICY=dict(
             P.POLICY, summary_structure=["Kepentingan", "Isi Utama"]))),
    dict(fid="KV-04", title="a unit is allowed to keep five beats", target="AP",
         gates=["EVERY_UNIT_TARGETS_THREE_BEATS"],
         patch=_units(lambda d: _u(d, "K5-PL06-T05-B01")[
             "summary_visual_obligation"].update(beats_required=5))),
    dict(fid="KV-05", title="a Rumusan visual subject is invented", target="AP",
         gates=["NO_SUMMARY_VISUAL_SUBJECT_IS_INVENTED"],
         patch=_units(lambda d: _u(d, "K5-PL06-T03-B04")[
             "summary_visual_obligation"].update(
                 visual_subject="montaj enam komponen landskap"))),

    # ---------------- forced Comparison ----------------
    dict(fid="KC-01", title="Comparison stops requiring an explicit source comparison",
         target="P", gates=["COMPARISON_REQUIRES_EXPLICIT_SOURCE_COMPARISON"],
         patch=lambda: dict(POLICY=dict(
             P.POLICY, comparison_requires_explicit_source_comparison=False))),
    dict(fid="KC-02", title="A4 is promoted from source-conditional to global", target="P",
         gates=["A4_IS_SOURCE_CONDITIONAL_NOT_GLOBAL"],
         patch=_dec("A4", scope=P.GLOBAL)),
    dict(fid="KC-03", title="a unit proposing Comparison is silently cleared", target="AP",
         gates=["EVERY_UNIT_PROPOSING_COMPARISON_IS_FLAGGED_FOR_RETEST",
                "NO_UNIT_IS_SILENTLY_CLEARED_FOR_COMPARISON"],
         patch=_units(lambda d: [u["comparison_retest"].update(status="CLEARED")
                                 for u in d["units"]
                                 if u["comparison_retest"][
                                     "currently_proposes_comparison"]])),

    # ---------------- wrong narrator ----------------
    dict(fid="KN-01", title="the K5 narrator is changed", target="P",
         gates=["K5_NARRATOR_IS_HILMI"],
         patch=lambda: dict(POLICY=dict(P.POLICY, narrator="Maya"))),
    dict(fid="KN-02", title="one unit names a different narrator", target="AP",
         gates=["EVERY_CALIBRATION_UNIT_NAMES_HILMI"],
         patch=_units(lambda d: _u(d, "K5-PL06-T06-B01")["narrator"].update(name="Maya"))),
    dict(fid="KN-03", title="the cross-course narrator note is applied here", target="P",
         gates=["THE_CROSS_COURSE_NARRATOR_NOTE_IS_INGESTED_NOT_APPLIED"],
         patch=_dec("D2", cross_course_note="Applied across K1-K5 in this run.")),
    dict(fid="KN-04", title="T04's cast hardens into a K5-wide cast", target="P",
         gates=["NO_K5_WIDE_CAST_IS_CLAIMED"],
         patch=lambda: dict(POLICY=dict(P.POLICY,
                                        characters="Alya dan Encik Rahman"))),

    # ---------------- incorrect Tamat Topik on an intermediate Bahagian ----------------
    dict(fid="KT-01", title="an intermediate Bahagian closes with Tamat Topik",
         target="AP", gates=["NO_INTERMEDIATE_BAHAGIAN_CLOSES_WITH_TAMAT_TOPIK",
                             "INTERMEDIATE_CLOSINGS_CARRY_THEIR_OWN_BAHAGIAN_NUMBER"],
         patch=_units(lambda d: _u(d, "K5-PL06-T03-B03")["closing_screen"].update(
             closing_text="Tamat Topik"))),
    dict(fid="KT-02", title="the intermediate wording loses its Bahagian number",
         target="AP", gates=["INTERMEDIATE_CLOSINGS_CARRY_THEIR_OWN_BAHAGIAN_NUMBER"],
         patch=_units(lambda d: _u(d, "K5-PL06-T03-B04")["closing_screen"].update(
             closing_text="Tamat Bahagian X. Teruskan pembelajaran ke bahagian "
                          "seterusnya"))),
    dict(fid="KT-03", title="a single-Bahagian topic stops closing with Tamat Topik",
         target="AP", gates=["SINGLE_BAHAGIAN_TOPICS_CLOSE_WITH_TAMAT_TOPIK"],
         patch=_units(lambda d: _u(d, "K5-PL06-T05-B01")["closing_screen"].update(
             closing_text="Tamat Bahagian 1. Teruskan pembelajaran ke bahagian "
                          "seterusnya"))),
    dict(fid="KT-04", title="Bariah's intermediate wording is paraphrased", target="P",
         gates=["INTERMEDIATE_CLOSING_TEXT_IS_BARIAHS_WORDING"],
         patch=lambda: dict(CLOSING_INTERMEDIATE="Tamat Bahagian X. Sila teruskan.")),
    dict(fid="KT-05", title="a single-Bahagian topic starts showing a Bahagian label",
         target="AP", gates=["SINGLE_BAHAGIAN_TOPICS_SHOW_NO_BAHAGIAN_LABEL"],
         patch=_units(lambda d: _u(d, "K5-PL06-T06-B01")["closing_screen"].update(
             bahagian_label_shown=True))),
    dict(fid="KT-06", title="a multi-Bahagian unit loses its own Summary and Quiz",
         target="AP", gates=["EVERY_MULTI_BAHAGIAN_UNIT_OWNS_ITS_SUMMARY_AND_QUIZ"],
         patch=_units(lambda d: _u(d, "K5-PL06-T03-B03")["closing_screen"].update(
             own_storyboard_summary_quiz=False))),

    # ---------------- false approval of a Section B choice ----------------
    dict(fid="KB-01", title="B2 density is approved without the test", target="P",
         gates=["B2_IS_TEST_REQUIRED_NOT_APPROVED", "B2_IS_NOT_IN_THE_APPROVED_LIST"],
         patch=_dec("B2", status=P.APPROVED,
                    effective_rule="2 panels per page.")),
    dict(fid="KB-02", title="a panel density is recorded as approved", target="P",
         gates=["NO_PANEL_DENSITY_IS_APPROVED"],
         patch=lambda: dict(POLICY=dict(P.POLICY, lampiran_panel_density=2))),
    dict(fid="KB-03", title="only one density is produced for the test", target="P",
         gates=["BOTH_DENSITIES_MUST_BE_PRODUCED_FOR_THE_TEST"],
         patch=lambda: dict(POLICY=dict(P.POLICY, lampiran_densities_to_test=[2]))),
    dict(fid="KB-04", title="the density test changes unit as well as density", target="P",
         gates=["THE_DENSITY_TEST_HOLDS_UNIT_AND_STATES_CONSTANT"],
         patch=_dec("B2", test_requirement=dict(densities_to_produce=[2, 3],
                                                same_unit=False, same_state_set=True,
                                                why=""))),
    dict(fid="KB-05", title="B2 is auto-appliable in the authority record", target="AUTH",
         gates=["B2_MAY_NOT_BE_AUTO_APPLIED", "B2_IS_THE_ONLY_SECTION_B_ITEM_BLOCKED"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE,
             section_b_items=dict(
                 AUTH.PENDING_PATTERN_PACKAGE["section_b_items"],
                 B2=dict(AUTH.PENDING_PATTERN_PACKAGE["section_b_items"]["B2"],
                         may_be_auto_applied=True))))),
    dict(fid="KB-06", title="the two-file packaging collapses to one file", target="P",
         gates=["TWO_FILES_PER_UNIT"],
         patch=lambda: dict(POLICY=dict(P.POLICY, files_per_unit=1,
                                        files_per_unit_names=["Storyboard"]))),
    dict(fid="KB-07", title="two units are packed into one review slot", target="P",
         gates=["ONE_UNIT_PER_NINETY_MINUTE_SLOT"],
         patch=lambda: dict(POLICY=dict(P.POLICY, units_per_review_slot=2))),
    dict(fid="KB-08", title="the slot length is shortened", target="P",
         gates=["ONE_UNIT_PER_NINETY_MINUTE_SLOT"],
         patch=lambda: dict(POLICY=dict(P.POLICY, review_slot_minutes=60))),
    dict(fid="KB-09", title="availability dates are invented", target="P",
         gates=["AVAILABILITY_DATES_ARE_NOT_INVENTED"],
         patch=lambda: dict(POLICY=dict(P.POLICY,
                                        availability_dates="5-8 Ogos 2026"))),
    dict(fid="KB-10", title="a slot count per day is invented", target="P",
         gates=["SLOTS_PER_DAY_ARE_NOT_INVENTED"],
         patch=lambda: dict(POLICY=dict(P.POLICY, slots_per_day=2))),
    dict(fid="KB-11", title="B4 availability stops being conditional", target="P",
         gates=["B4_AVAILABILITY_IS_MARKED_CONDITIONAL"],
         patch=_dec("B4", availability_is_conditional=False)),
    dict(fid="KB-12", title="mass generation is declared authorized", target="P",
         gates=["MASS_GENERATION_IS_NOT_AUTHORIZED"],
         patch=lambda: dict(MASS_GENERATION_AUTHORIZED=True)),
    dict(fid="KB-13", title="the authorized unit list is widened beyond calibration",
         target="P", gates=["ONLY_THE_FOUR_CALIBRATION_UNITS_ARE_AUTHORIZED"],
         patch=lambda: dict(CALIBRATION_UNITS_AUTHORIZED=P.CALIBRATION_UNITS_AUTHORIZED
                            + ["K5-PL06-T01-B01"])),
    dict(fid="KB-14", title="calibration generation is withdrawn", target="P",
         gates=["CALIBRATION_GENERATION_IS_AUTHORIZED"],
         patch=lambda: dict(CALIBRATION_GENERATION_AUTHORIZED=False)),
    dict(fid="KB-15", title="Section B reverts to pending", target="P",
         gates=["SECTION_B_IS_CLOSED"],
         patch=lambda: dict(SECTION_B_STATUS="PENDING_BARIAH_DECISION")),
    dict(fid="KB-16", title="a decision is left pending after the second return",
         target="P", gates=["NOTHING_REMAINS_PENDING",
                            "THE_FOUR_BUCKETS_PARTITION_ALL_SEVENTEEN",
                            "EVERY_BUCKET_TOGETHER_ACCOUNTS_FOR_ALL_SEVENTEEN"],
         patch=_dec("B3", status=P.PENDING)),
    dict(fid="KB-17", title="the Section B source hash drifts", target="P",
         gates=["SECTION_B_SOURCE_HASH_RECORDED"],
         patch=lambda: dict(SOURCE_DOCUMENT_B=dict(P.SOURCE_DOCUMENT_B,
                                                   sha256="0" * 64))),
    dict(fid="KB-18", title="the Lampiran is described as a learner deck", target="P",
         gates=["LAMPIRAN_IS_NOT_A_SECOND_LEARNER_DECK"],
         patch=lambda: dict(LAMPIRAN_KEADAAN_DEFINITION=dict(
             P.LAMPIRAN_KEADAAN_DEFINITION,
             what_it_is_not=["aset MMD"]))),
    dict(fid="KB-19", title="the authority record marks Section B pending", target="AUTH",
         gates=["SECTION_B_IS_CLOSED_IN_THE_AUTHORITY_RECORD",
                "THE_AUTHORITY_RECORD_AGREES_NOTHING_IS_PENDING"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE,
             authority_by_section=dict(
                 AUTH.PENDING_PATTERN_PACKAGE["authority_by_section"],
                 B="PENDING_BARIAH_DECISION")))),
    dict(fid="KB-20", title="the authority record authorizes mass generation",
         target="AUTH", gates=["THE_AUTHORITY_RECORD_AUTHORIZES_CALIBRATION_NOT_MASS"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE, mass_generation_authorized=True))),
    dict(fid="KB-21", title="the forecast invents availability", target="AP",
         gates=["AVAILABILITY_IS_NEVER_GIVEN_A_VALUE_IN_THE_FORECAST"],
         patch=lambda: dict(FORECAST=dict(
             AP.FORECAST,
             open_variables=dict(AP.FORECAST["open_variables"],
                                 slots_per_available_day=2)))),
    dict(fid="KB-22", title="the forecast drops the real review constraint", target="AP",
         gates=["THE_FORECAST_USES_THE_REAL_REVIEW_CONSTRAINT"],
         patch=lambda: dict(FORECAST=dict(
             AP.FORECAST,
             review_constraint=dict(AP.FORECAST["review_constraint"],
                                    units_per_slot=2)))),
    dict(fid="KB-23", title="a scenario presents its slot rate as confirmed", target="AP",
         gates=["EVERY_SCENARIO_MARKS_ITS_SLOT_ASSUMPTION_CONDITIONAL"],
         patch=lambda: dict(FORECAST=dict(
             AP.FORECAST,
             scenarios=[dict(s2, slots_per_day_assumed="2") if s2["id"] == "A" else s2
                        for s2 in AP.FORECAST["scenarios"]]))),
    dict(fid="KB-24", title="the forecast forgets Section B was resolved", target="AP",
         gates=["SECTION_B_IS_RECORDED_AS_RESOLVED_IN_THE_FORECAST"],
         patch=lambda: dict(FORECAST=dict(
             AP.FORECAST,
             section_b_resolved=dict(AP.FORECAST["section_b_resolved"],
                                     status="PENDING_BARIAH_DECISION")))),

    # ---------------- ingestion integrity ----------------
    dict(fid="KI-01", title="a decision goes missing from the roll", target="P",
         gates=["MODELLED_TOTAL_EQUALS_THE_DECLARED_TOTAL",
                "SECTION_COUNTS_MATCH_THE_DOCUMENTS_OWN_TABLE",
                "APPROVED_PLUS_PENDING_ACCOUNTS_FOR_EVERY_DECISION"],
         patch=lambda: dict(DECISIONS=[d for d in P.DECISIONS if d["id"] != "A2"])),
    dict(fid="KI-02", title="the document hash drifts", target="P",
         gates=["DOCUMENT_HASH_RECORDED"],
         patch=lambda: dict(SOURCE_DOCUMENT=dict(P.SOURCE_DOCUMENT, sha256="0" * 64))),
    dict(fid="KI-03", title="the quiz default is altered", target="P",
         gates=["QUIZ_IS_FOUR_MCQ_ONE_MR_AT_SIXTY_PERCENT"],
         patch=lambda: dict(POLICY=dict(P.POLICY, quiz_pass_percent=50))),
    dict(fid="KI-04", title="an answer key is marked Bariah-approved", target="AP",
         gates=["NO_ANSWER_KEY_IS_APPROVED"],
         patch=_units(lambda d: _u(d, "K5-PL06-T03-B03")["quiz_structure"].update(
             key_status="BARIAH_APPROVED"))),
    dict(fid="KI-05", title="an unanswered CAIR sub-point is marked approved", target="P",
         gates=["UNANSWERED_CAIR_SUBPOINTS_ARE_NAMED_NOT_ASSUMED"],
         patch=lambda: dict(UNRESOLVED_SUBPOINTS=[
             dict(s, status="APPROVED") for s in P.UNRESOLVED_SUBPOINTS])),
    dict(fid="KI-06", title="a unit claims it is ready to emit PPTX", target="AP",
         gates=["NOTHING_IS_READY_TO_EMIT_PPTX"],
         patch=_units(lambda d: _u(d, "K5-PL06-T03-B03")["readiness"].update(
             ready_to_emit_pptx=True))),
    dict(fid="KI-07", title="the suite adopts a sibling identity", target="QA",
         gates=["SUITE_ID_DECLARED", "SUITE_ID_IS_NOT_ANY_SIBLING_SUITE"],
         patch=lambda: dict(SUITE_ID="STAGE_4_2F_F_K2_QA_v1")),

    # ---------------- authority partition ----------------
    dict(fid="KA-01", title="authority collapses back to a single True boolean",
         target="AUTH", gates=["AUTHORITY_IS_NOT_A_SINGLE_BOOLEAN"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE, is_authority=True))),
    dict(fid="KA-02", title="the authority record marks B2 approved, contradicting the "
                             "ingestion", target="AUTH",
         gates=["THE_AUTHORITY_RECORD_AND_THE_INGESTION_AGREE_ON_B2",
                "B2_IS_THE_ONLY_SECTION_B_ITEM_BLOCKED"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE,
             section_b_items=dict(
                 AUTH.PENDING_PATTERN_PACKAGE["section_b_items"],
                 B2=dict(status="APPROVED_AS_K5_DEFAULT",
                         may_be_auto_applied=True))))),
    dict(fid="KA-03", title="an approved Section B item is wrongly blocked", target="AUTH",
         gates=["B2_IS_THE_ONLY_SECTION_B_ITEM_BLOCKED"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE,
             section_b_items=dict(
                 AUTH.PENDING_PATTERN_PACKAGE["section_b_items"],
                 B1=dict(AUTH.PENDING_PATTERN_PACKAGE["section_b_items"]["B1"],
                         may_be_auto_applied=False))))),
    dict(fid="KA-04", title="Sections A/C/D lose their ingested status", target="AUTH",
         gates=["SECTIONS_A_C_D_ARE_INGESTED_AUTHORITY"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE,
             authority_by_section=dict(
                 AUTH.PENDING_PATTERN_PACKAGE["authority_by_section"],
                 A="PENDING_BARIAH_DECISION")))),
    dict(fid="KA-05", title="Section C loses its ingested-authority status", target="AUTH",
         gates=["SECTIONS_A_C_D_ARE_INGESTED_AUTHORITY"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE,
             authority_by_section=dict(AUTH.PENDING_PATTERN_PACKAGE[
                 "authority_by_section"], C="PENDING_BARIAH_DECISION")))),
    dict(fid="KA-06", title="the package reverts to wholly pending", target="AUTH",
         gates=["AUTHORITY_RECORD_SHOWS_THE_PACKAGE_RETURNED"],
         patch=lambda: dict(PENDING_PATTERN_PACKAGE=dict(
             AUTH.PENDING_PATTERN_PACKAGE, status="PENDING_BARIAH_REVIEW"))),
    dict(fid="KA-07", title="the generic suite's crash is claimed as this run's fault",
         target="QA", gates=["THE_GENERIC_SUITE_CRASH_IS_RECORDED_AS_PRE_EXISTING"],
         patch=lambda: dict(GENERIC_SUITE_BASELINE_DEFECT=dict(
             QA.GENERIC_SUITE_BASELINE_DEFECT, caused_by_this_run=True))),

    # ---------------- outside-PL06 counts ----------------
    dict(fid="KO-01", title="a confirmed production unit is claimed outside PL06",
         target="AP", gates=["NO_CONFIRMED_PRODUCTION_UNIT_IS_CLAIMED_OUTSIDE_PL06"],
         patch=_outside(lambda s: s.update(
             confirmed_storyboard_production_units_outside_pl06=7))),
    dict(fid="KO-02", title="PL06 rows leak back into the outside-PL06 population",
         target="AP", gates=["THE_OUTSIDE_PL06_POPULATION_EXCLUDES_PL06",
                             "CANDIDATE_ROLL_LENGTH_MATCHES_ITS_COUNT"],
         patch=_outside(lambda s: s["rows"].append(
             dict(s["rows"][0], pl="PL06", candidate_id="PL06-LEAK")))),
    dict(fid="KO-03", title="the candidate roll drifts from its count", target="AP",
         gates=["CANDIDATE_ROLL_LENGTH_MATCHES_ITS_COUNT"],
         patch=_outside(lambda s: s.update(
             candidate_structures_roll=s["candidate_structures_roll"][:10]))),
    dict(fid="KO-04", title="clean and amber stop accounting for every candidate",
         target="AP", gates=["CLEAN_PLUS_AMBER_ACCOUNTS_FOR_EVERY_CANDIDATE",
                             "ESTABLISHED_FACTS_PRESERVED"],
         patch=_outside(lambda s: s.update(clean_candidates=18))),
    dict(fid="KO-05", title="an established fact is quietly changed", target="AP",
         gates=["ESTABLISHED_FACTS_PRESERVED"],
         patch=_outside(lambda s: s.update(unmapped_source_regions=5))),
    dict(fid="KO-06", title="a headline count loses its named roll", target="AP",
         gates=["EVERY_HEADLINE_COUNT_HAS_A_NAMED_ROLL"],
         patch=_outside(lambda s: s.pop("amber_candidates_roll"))),
    dict(fid="KO-07", title="a PL06 Topik is relabelled a production unit", target="AP",
         gates=["THE_SEVEN_PL06_TOPIK_ARE_NOT_COUNTED_AS_PRODUCTION_UNITS"],
         patch=_outside(lambda s: s["pl06_topik"][0].update(
             is_storyboard_production_unit=True))),
    dict(fid="KO-08", title="PL06's production-unit count reverts to seven", target="AP",
         gates=["PL06_PRODUCTION_UNITS_ARE_THE_FOURTEEN_BAHAGIAN"],
         patch=_outside(lambda s: s.update(pl06_storyboard_production_units=7))),
    dict(fid="KO-09", title="the rename is dropped so the change looks silent",
         target="AP", gates=["THE_RENAME_IS_RECORDED_NOT_SILENT"],
         patch=_outside(lambda s: s.update(renamed_counts=[]))),
    dict(fid="KO-10", title="the PL06 Topik roll loses a member", target="AP",
         gates=["PL06_TOPIK_ROLL_IS_SEVEN_NAMED_MEMBERS"],
         patch=_outside(lambda s: s.update(pl06_topik_roll=s["pl06_topik_roll"][:6]))),

    # ---------------- forecast completeness ----------------
    dict(fid="KF-01", title="the forecast is presented as a commitment", target="AP",
         gates=["FORECAST_IS_LABELLED_NOT_A_COMMITMENT"],
         patch=lambda: dict(FORECAST=dict(AP.FORECAST, status="COMMITTED_SCHEDULE"))),
    dict(fid="KF-02", title="a scenario is dropped", target="AP",
         gates=["THREE_SCENARIOS_ARE_PRESENT", "EVERY_SCENARIO_REPORTS_ALL_SIX_RANGES",
                "EVERY_SCENARIO_NAMES_ASSUMPTIONS_AND_BLOCKERS", "NO_FULL_K5_DATE_IS_"
                "COMPUTED"],
         patch=lambda: dict(FORECAST=dict(AP.FORECAST,
                                          scenarios=AP.FORECAST["scenarios"][:2]))),
    dict(fid="KF-03", title="a scenario loses one of its six ranges", target="AP",
         gates=["EVERY_SCENARIO_REPORTS_ALL_SIX_RANGES"],
         patch=lambda: dict(FORECAST=dict(
             AP.FORECAST,
             scenarios=[{k: v for k, v in s.items()
                         if k != "batch_generation_start_range"}
                        if s["id"] == "B" else s for s in AP.FORECAST["scenarios"]]))),
    dict(fid="KF-04", title="a scenario stops naming its blockers", target="AP",
         gates=["EVERY_SCENARIO_NAMES_ASSUMPTIONS_AND_BLOCKERS"],
         patch=lambda: dict(FORECAST=dict(
             AP.FORECAST,
             scenarios=[dict(s, principal_blockers=[]) if s["id"] == "C" else s
                        for s in AP.FORECAST["scenarios"]]))),
    dict(fid="KF-05", title="the forecast invents specific available dates", target="AP",
         gates=["AVAILABILITY_IS_NEVER_GIVEN_A_VALUE_IN_THE_FORECAST"],
         patch=lambda: dict(FORECAST=dict(
             AP.FORECAST,
             open_variables=dict(AP.FORECAST["open_variables"],
                                 available_dates="5, 6, 7 and 8 Ogos 2026")))),
    dict(fid="KF-06", title="a full-K5 completion date is computed", target="AP",
         gates=["NO_FULL_K5_DATE_IS_COMPUTED"],
         patch=lambda: dict(FORECAST=dict(
             AP.FORECAST,
             scenarios=[dict(s, full_k5_package_completion_range="20 Ogos 2026")
                        if s["id"] == "A" else s for s in AP.FORECAST["scenarios"]]))),

    # ---------------- D4 derivation ----------------
    dict(fid="KD-01", title="the D4 single-Bahagian rule cites only the map", target="AP",
         gates=["D4_SINGLE_BAHAGIAN_RULE_CITES_BOTH_INPUTS"],
         patch=lambda: dict(SINGLE_BAHAGIAN_IS_NO_BAHAGIAN=dict(
             AP.SINGLE_BAHAGIAN_IS_NO_BAHAGIAN,
             derivation="FROZEN_SEGMENTATION_MAP"))),
    dict(fid="KD-02", title="the derivation stops saying what it is not", target="AP",
         gates=["D4_DERIVATION_NAMES_WHAT_IT_IS_NOT"],
         patch=lambda: dict(SINGLE_BAHAGIAN_IS_NO_BAHAGIAN={
             k: v for k, v in AP.SINGLE_BAHAGIAN_IS_NO_BAHAGIAN.items()
             if k != "what_this_is_not"})),
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
    global _BASE_UNITS, _BASE_MATRIX, _BASE_OUTSIDE
    _BASE_UNITS = AP.calibration_units()
    _BASE_MATRIX = AP.impact_matrix()
    _BASE_OUTSIDE = AP.outside_pl06()
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


if __name__ == "__main__":
    r = main()
    print(json.dumps({k: v for k, v in r.items() if k != "fixtures"},
                     ensure_ascii=False, indent=1))
    for f in r["fixtures"]:
        if not f["detected"]:
            print("MISS", f["fixture_id"], "|", f["title"], "|", f["designated_gates"],
                  "|", f["note"])
    sys.exit(1 if (r["missed"] or r["baseline_false_failures"]) else 0)
