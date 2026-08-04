# -*- coding: utf-8 -*-
"""K5 — applying the ingested Bariah policy: impact matrix, calibration units, structures.

    python3 docs/pl06/tools/k5_policy_apply_v1.py

Everything here is derived from `k5_pattern_policy_v1` (the ruling) applied to artifacts
already committed (the units and structures). Nothing re-reads the K5 DOCX or PDF.

Section B is now closed by Bariah's second return. B1 fixes two-file packaging, B3 fixes
one unit per 90-minute slot, B4 gives conditional availability. B2 is the exception: no
panel density is approved and a 2-panel/3-panel test is required first, so nothing here
records a density as settled.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(HERE)), "source", "tools"))
import k5_pattern_policy_v1 as P     # noqa: E402
import pl06_unit_model_v1 as UM      # noqa: E402
import pl06_batch1_data_v1 as B      # noqa: E402

STAGE = P.STAGE
CALIBRATION_UNITS = ["K5-PL06-T03-B03", "K5-PL06-T03-B04",
                     "K5-PL06-T05-B01", "K5-PL06-T06-B01"]

# Bariah names T04 — a Topik carrying a single Bahagian in the frozen map — as the
# "Topik tiada Bahagian" case. That is her own worked example, so a Topik with exactly one
# Bahagian takes the no-label / "Tamat Topik" treatment. This is read off her example, not
# inferred from the map alone.
SINGLE_BAHAGIAN_IS_NO_BAHAGIAN = dict(
    rule="A Topik with exactly one Bahagian is treated as 'Topik tiada Bahagian'.",
    # Two independent inputs, and the derivation needs BOTH. Neither alone decides it.
    derivation="BARIAH_WORKED_EXAMPLE + FROZEN_SEGMENTATION_MAP",
    input_1_bariah=("D4's comment names T04 explicitly as the no-Bahagian case: 'Default "
                    "ini (tiada label Bahagian + penutup \"Tamat Topik\") hanya terpakai "
                    "untuk Topik tiada Bahagian, seperti T04.' That fixes T04's "
                    "treatment but says nothing about how many Bahagian T04 has."),
    input_2_map=("The frozen PL06 boundary map shows T04 carrying exactly one Bahagian, "
                 "K5-PL06-T04-B01. That is what supplies the arithmetic Bariah's "
                 "sentence does not."),
    conclusion=("Together they establish that a Topik of exactly one Bahagian is the "
                "no-Bahagian case. T05, T06 and T07 each carry exactly one Bahagian in "
                "the same map, so they take the same treatment as T04."),
    what_this_is_not=("Not an inference from the map alone — the map cannot say which "
                      "treatment applies. Not an inference from Bariah alone — her "
                      "sentence names one Topik, not a rule about counts. The rule exists "
                      "only where the two meet, and is labelled accordingly."),
    evidence_class="BARIAH_WORKED_EXAMPLE_PLUS_FROZEN_MAP")


def _segmentation():
    """Topik -> ordered Bahagian, straight from the frozen boundary map."""
    import json
    m = json.load(open(B.BOUNDARY_MAP_PATH, encoding="utf-8"))
    seg = {}
    for u in m["lessons"]:
        seg.setdefault(u["topik"], []).append((u["bahagian"], u["unit_id"]))
    return {k: sorted(v) for k, v in sorted(seg.items())}


def closing_for(unit_id):
    """The D4 closing screen for one unit, with the reasoning that produced it."""
    seg = _segmentation()
    topik = int(unit_id.split("-T")[1].split("-")[0])
    bah = int(unit_id.rsplit("-B", 1)[1])
    members = seg[topik]
    total = len(members)
    if total == 1:
        return dict(unit_id=unit_id, topik=topik, bahagian_in_topik=total,
                    segmentation="TOPIK_WITHOUT_BAHAGIAN",
                    bahagian_label_shown=False,
                    closing_text=P.CLOSING_FINAL,
                    basis="D4, resolved by " + SINGLE_BAHAGIAN_IS_NO_BAHAGIAN[
                        "derivation"],
                    derivation=SINGLE_BAHAGIAN_IS_NO_BAHAGIAN)
    is_final = bah == max(b for b, _ in members)
    return dict(unit_id=unit_id, topik=topik, bahagian_in_topik=total,
                segmentation="TOPIK_WITH_MULTIPLE_BAHAGIAN",
                bahagian_label_shown=True,
                is_final_bahagian=is_final,
                closing_text=(P.CLOSING_FINAL if is_final
                              else P.CLOSING_INTERMEDIATE.replace("X", str(bah))),
                own_storyboard_summary_quiz=True,
                basis="D4 — each Bahagian carries its own storyboard, Rumusan and Kuiz; "
                      "only the final Bahagian closes with 'Tamat Topik'.")


# ==========================================================================================
# DECISION-IMPACT MATRIX
# ==========================================================================================
def impact_matrix():
    rows = []

    def row(did, rule_or_generator, units, scope, status, section_b, note=""):
        d = next(x for x in P.DECISIONS if x["id"] == did)
        rows.append(dict(
            decision=did, title=d["title"], status_of_ruling=d["status"],
            affected_rule_or_generator=rule_or_generator, affected_units=units,
            scope=scope, implementation_status=status,
            section_b_affects_it=section_b, note=note))

    row("A1", "pl06_unit_model_v1 component rendering; storyboard generator screen build",
        "ALL_K5_UNITS", P.GLOBAL, "POLICY_RECORDED_GENERATOR_NOT_YET_BUILT", False,
        "Enforceable as a screen-visibility rule once the storyboard generator exists.")
    row("A2", "pl06_unit_model_v1 interaction_candidates (click-to-reveal)",
        "ALL_K5_UNITS", P.GLOBAL, "ALREADY_CONSISTENT", False,
        "Accepted unamended; the existing model already proposes this pattern.")
    row("A3", "pl06_unit_model_v1 screen_sequence + interaction_candidates",
        "UNITS_WITH_STEPWISE_PROCESS", P.GLOBAL, "POLICY_RECORDED_MODEL_UPDATED", False,
        "One step at a time with its visual; click a step for further detail where the "
        "source carries it. Two CAIR sub-points remain unanswered.")
    row("A4", "pl06_unit_model_v1 pattern_family secondary candidates",
        "UNITS_PROPOSING_COMPARISON", P.SOURCE_CONDITIONAL,
        "RE_TEST_REQUIRED_PER_UNIT", False,
        "Every unit currently proposing Comparison must be re-tested against whether its "
        "source explicitly compares.")
    row("A5", "pl06_unit_model_v1 dialogue; screen_sequence shell",
        "ALL_K5_UNITS", P.GLOBAL, "MODEL_UPDATED_SHELL_RECOMPUTED", False,
        "Prose overrides the tick. Every unit gains a scenario screen; three of the four "
        "calibration units previously had none.")
    row("A6", "pl06_unit_model_v1 rumusan (beats + visual obligation)",
        "ALL_K5_UNITS", P.GLOBAL, "MODEL_UPDATED", False,
        "Three beats and a supporting visual. Two calibration units carried a different "
        "beat count and all four carried no Rumusan visual.")
    row("A7", "pl06_unit_model_v1 assessment; PL06 rule-portability RP-009 / RP-010",
        "ALL_K5_UNITS", P.GLOBAL, "CONFIRMED_PREVIOUSLY_FLAGGED_AS_VERIFY", False,
        "Resolves the RP-009 and RP-010 VERIFY flags at K5 scope; answer keys stay "
        "unapproved.")
    row("B1", "calibration package emitter — file split per unit", "CALIBRATION_UNITS",
        P.GLOBAL, "APPROVED_TWO_FILES_PER_UNIT", False,
        "One Storyboard file plus one Lampiran Keadaan file per unit. The definition of "
        "Lampiran Keadaan that B1 was blocked on is now supplied.")
    row("B2", "Lampiran Keadaan renderer — panels per page", "CALIBRATION_UNITS",
        P.GLOBAL, "TEST_REQUIRED_NO_DENSITY_APPROVED", False,
        "The ONE Section B item not approved. A 2-panel and a 3-panel example of the same "
        "unit and the same state set must be shown before any density is frozen.")
    row("B3", "review scheduling — no generator", "REVIEW_PROCESS", P.GLOBAL,
        "APPROVED_ONE_UNIT_PER_90_MINUTE_SLOT", False,
        "One slot = one unit = one Storyboard + one Lampiran Keadaan. Never compressed.")
    row("B4", "review scheduling — no generator", "REVIEW_PROCESS", P.GLOBAL,
        "APPROVED_AVAILABILITY_CONDITIONAL", False,
        "Working days except Cyberjaya meeting days; weekends optional. Actual dates and "
        "slot counts require Firdaus confirmation and are never invented.")
    row("C1", "T04 visual-group record AG-01..AG-08", "T04_ONLY", P.GLOBAL,
        "RECORD_CONFIRMED_NO_CHANGE", False, "Must not reopen T04 decisions.")
    row("C2", "T04 three non-shareable items", "T04_ONLY", P.GLOBAL,
        "RECORD_CONFIRMED_NO_CHANGE", False, "Must not reopen T04 decisions.")
    row("D1", "pl06_unit_model_v1 dialogue.cast", "ALL_K5_UNITS", P.UNIT_SPECIFIC,
        "POLICY_RECORDED_CAST_STAYS_OPEN", False,
        "No K5-wide cast. STOP-006 stays open legitimately, now as a per-unit choice.")
    row("D2", "storyboard generator narrator field", "ALL_K5_UNITS", P.GLOBAL,
        "MODEL_UPDATED", False,
        "Hilmi for K5. The cross-course K1/K2/K3/K4 assignment is ingested but not applied "
        "here.")
    row("D3", "pl06_unit_model_v1 dialogue obligation", "ALL_K5_UNITS", P.GLOBAL,
        "MODEL_UPDATED", False, "The ruling A5's prose defers to.")
    row("D4", "closing-screen rule; per-Bahagian Rumusan and Kuiz",
        "ALL_K5_UNITS", P.SOURCE_CONDITIONAL, "MODEL_UPDATED", False,
        "Segmentation-dependent; resolved per unit from the frozen map.")
    return dict(stage=STAGE, rows=rows, total=len(rows),
                affected_by_section_b=[r["decision"] for r in rows
                                       if r["section_b_affects_it"]])


# ==========================================================================================
# CALIBRATION UNITS
# ==========================================================================================
def calibration_units():
    models, _ = UM.all_models()
    out = []
    for uid in CALIBRATION_UNITS:
        m = models[uid]
        d = m.get("dialogue", {})
        r = m.get("rumusan", {})
        arith = dict(m["screen_sequence"]["arithmetic"])
        pf = m.get("pattern_family", {})

        had_scenario = bool(arith.get("shell_includes_dialogue"))
        scenario_change = ("ALREADY_PRESENT" if had_scenario
                           else "SCENARIO_SCREEN_ADDED")
        new_shell = arith["shell_screens"] + (0 if had_scenario else 1)
        new_min = new_shell + arith["content_groups"] + arith["closing_screens"]

        beats_before = r.get("beat_count")
        beats_change = ("ALREADY_THREE_BEAT" if beats_before == 3
                        else f"RESTRUCTURE_{beats_before}_BEATS_TO_3")

        proposes_comparison = "comparison" in (
            str(pf.get("primary_candidate", "")) + " "
            + str(pf.get("secondary_candidate", "")))

        out.append(dict(
            unit_id=uid, lesson_title=m.get("lesson_title"),
            controlled_source_rows=dict(
                cls="SOURCE_DERIVED", status="COMMITTED_UNCHANGED",
                note="Extraction is unaffected by the pattern ruling; the committed rows "
                     "stand and were not re-extracted."),
            screen_pattern_plan=dict(
                cls="CAIR_PROPOSAL_UNDER_APPROVED_POLICY",
                primary=pf.get("primary_candidate"),
                secondary=pf.get("secondary_candidate"),
                shell_screens_before=arith["shell_screens"],
                shell_screens_after=new_shell,
                content_groups=arith["content_groups"],
                closing_screens=arith["closing_screens"],
                minimum_total_before=arith["minimum_total_screens"],
                minimum_total_after=new_min,
                maximum_total="UNKNOWN_STILL_NOT_FROZEN",
                a3_applies=("progressive process" in str(pf.get("primary_candidate", ""))
                            or "progressive process"
                            in str(pf.get("secondary_candidate", ""))),
                a3_rule="steps one at a time with their visuals; click a step for detail "
                        "where the source carries it"),
            scenario_obligation=dict(
                cls="COURSE_RULE_ALREADY_APPROVED", basis=["D3", "A5"],
                required=True, previous_cair_verdict=d.get("verdict"),
                change=scenario_change,
                note=("The previous verdict was a CAIR proposal. D3 makes the screen "
                      "mandatory regardless, so a NOT_JUSTIFIED or UNCERTAIN verdict no "
                      "longer removes the screen — it only means the scenario's content "
                      "must still be sourced.")),
            summary_visual_obligation=dict(
                cls="COURSE_RULE_ALREADY_APPROVED", basis=["A6"],
                structure=P.POLICY["summary_structure"],
                beats_before=beats_before, beats_required=3, change=beats_change,
                visual_required=True, visual_before="ABSENT",
                visual_change="SUMMARY_VISUAL_ADDED",
                visual_subject="PENDING_UNIT_EXCEPTION_REVIEW — the obligation is set, the "
                               "subject is not invented here"),
            quiz_structure=dict(
                cls="COURSE_RULE_ALREADY_APPROVED", basis=["A7"],
                mcq=4, multiple_response=1, pass_percent=60,
                key_status="SOURCE_AUTHORED_NOT_BARIAH_APPROVED",
                note="Composition and threshold are authorised; no answer key is approved."),
            narrator=dict(cls="COURSE_RULE_ALREADY_APPROVED", basis=["D2"], name="Hilmi"),
            characters=dict(cls="PENDING_UNIT_EXCEPTION_REVIEW", basis=["D1"],
                            cast=d.get("cast"),
                            note="D1 rules characters are chosen per unit, so the open "
                                 "cast is now the correct state, not a gap."),
            closing_screen=closing_for(uid),
            comparison_retest=dict(
                cls="SOURCE_CONDITIONAL", basis=["A4"],
                currently_proposes_comparison=proposes_comparison,
                required_action=("re-test against explicit source comparison before use"
                                 if proposes_comparison else "none — no Comparison "
                                                             "proposed"),
                status=("RE_TEST_REQUIRED" if proposes_comparison else "NOT_APPLICABLE")),
            state_model_implications=dict(
                added_states="one scenario screen and its runtime state"
                             if not had_scenario else "none",
                summary_visual_state="the Rumusan screen gains a visual element; whether "
                                     "it adds a runtime state depends on the pattern, "
                                     "which is not frozen",
                total_runtime_states="UNKNOWN_STILL_NOT_FROZEN"),
            ambiguities_and_exceptions=[
                a for a in [
                    ("A3 sub-points 2 and 3 were not answered by Bariah, so source order "
                     "and the overview diagram remain CAIR proposals."),
                    ("Comparison is proposed and must be re-tested against A4."
                     if proposes_comparison else None),
                    ("The Rumusan visual subject is not chosen here; inventing one would "
                     "breach the no-invented-visual-subject rule."),
                    ("Section B is undecided, so this unit's review packaging and panel "
                     "density are not settled."),
                ] if a],
            readiness=dict(
                policy_applied=True,
                source_extraction="COMPLETE",
                blocked_on_section_b_for_packaging=True,
                ready_to_emit_pptx=False,
                ready_reason="Section B undecided; unit exceptions and the Rumusan visual "
                             "subject still require Bariah review."),
        ))
    return dict(stage=STAGE, units=out, count=len(out))


# ==========================================================================================
# STRUCTURES OUTSIDE PL06
# ==========================================================================================
def outside_pl06():
    """K5 structures OUTSIDE PL06 — and the PL06 rows that were being counted with them.

    THE COUNT CONTRADICTION THIS FUNCTION EXISTS TO KILL
    ----------------------------------------------------
    An earlier version of this artifact reported "7 confirmed units" and "all 22 remain
    non-confirmed production units" on the same page. Both numbers were real and neither
    described the same population:

      * the seven CONFIRMED_UNIT rows are PL06's OWN seven sub-modul (Topik 1-7). They are
        INSIDE PL06, and they are Topik-level SOURCE structures carrying a frozen boundary
        map — not storyboard production units. PL06's production units are the FOURTEEN
        Bahagian-level entries in that map, not seven.
      * the 22 candidates are the genuinely outside-PL06 population.

    So `confirmed_units` was never an outside-PL06 count and is renamed
    `pl06_topik_with_frozen_boundary_map`, reported separately as context. The
    outside-PL06 confirmed storyboard production-unit count is ZERO and stays open.

    Three different sevens sit in this data and that is exactly why the contradiction was
    easy to miss: 7 PL06 Topik, 7 non-PL06 Pakej Latihan (the "unmapped source regions"),
    and 7 Topik in the frozen segmentation. Each now carries its own named roll.
    """
    import src_run2_v1 as R2
    k5 = R2.k5_structures()
    seg = _segmentation()

    pl06_rows = [r for r in k5["rows"] if r["pl"] == "PL06"]
    outside_rows = [r for r in k5["rows"] if r["pl"] != "PL06"]

    # Named roll for PL06's seven Topik. candidate_id is null on these rows, so a stable
    # identifier is built from the sub-modul heading they are actually anchored on.
    pl06_topik = [
        dict(ordinal=i + 1, topik_id=f"K5-PL06-T{i + 1:02d}",
             sub_modul_heading=r["subtopic"],
             source_page_span=r["source_page_span"],
             source_page_span_basis=r["source_page_span_basis"],
             granularity=r["granularity"],
             record_type="PL06_TOPIK_WITH_FROZEN_BOUNDARY_MAP",
             bahagian_in_this_topik=len(seg.get(i + 1, [])),
             is_storyboard_production_unit=False,
             why_not=("A Topik is a source structure. PL06's storyboard production units "
                      "are the Bahagian entries beneath it — fourteen in total across the "
                      "seven Topik."))
        for i, r in enumerate(pl06_rows)]

    rows = []
    for r in outside_rows:
        rows.append(dict(
            candidate_id=r["candidate_id"], pl=r["pl"], topic=r["topic"],
            subtopic=r["subtopic"],
            record_type=r["record_type"], status=r["status"],
            granularity=r["granularity"],
            d4_applies="UNKNOWN_SEGMENTATION_NOT_ASSESSED",
            d4_note=("No frozen boundary map exists for this Pakej Latihan, so its "
                     "Topik/Bahagian segmentation is not known and D4 cannot be resolved "
                     "for it."),
            still_not_a_confirmed_production_unit=True))

    pls_outside = sorted({r["pl"] for r in outside_rows})
    clean = [r["candidate_id"] for r in outside_rows if r["status"] == "CLEAN"]
    amber = [r["candidate_id"] for r in outside_rows if r["status"] == "AMBER"]

    return dict(
        stage=STAGE,
        population="K5 Pakej Latihan other than PL06",
        pakej_latihan_in_module=k5["pakej_latihan"],
        pakej_latihan_outside_pl06=len(pls_outside),

        # ---- the corrected headline counts, each with a named roll ----
        confirmed_storyboard_production_units_outside_pl06=0,
        confirmed_storyboard_production_units_outside_pl06_roll=[],
        confirmed_storyboard_production_units_outside_pl06_note=(
            "ZERO, and it stays open. No structure outside PL06 has a frozen boundary "
            "map, so none can be confirmed as a storyboard production unit. This is not a "
            "claim that the final count IS zero — it is a statement that none is proven."),

        candidate_structures=len(outside_rows),
        candidate_structures_roll=[r["candidate_id"] for r in outside_rows],
        clean_candidates=len(clean), clean_candidates_roll=clean,
        amber_candidates=len(amber), amber_candidates_roll=amber,

        unmapped_source_regions=len(pls_outside),
        unmapped_source_regions_roll=pls_outside,
        unmapped_source_regions_definition=(
            "One region per Pakej Latihan outside PL06 that carries no frozen unit "
            "boundary map. The count is the number of such Pakej Latihan, not a count of "
            "arbitrary page ranges."),
        unmapped_pages=k5["unmapped_pages"],

        # ---- PL06's own rows, reported separately and NOT as an outside-PL06 count ----
        pl06_topik_with_frozen_boundary_map=len(pl06_topik),
        pl06_topik_roll=[t["topik_id"] for t in pl06_topik],
        pl06_topik=pl06_topik,
        pl06_topik_note=("These seven were previously counted as 'confirmed units' in an "
                         "outside-PL06 artifact. They are inside PL06 and they are Topik, "
                         "not production units. Renamed and separated."),
        pl06_storyboard_production_units=sum(len(v) for v in seg.values()),
        pl06_storyboard_production_units_roll=[u for v in seg.values() for _, u in v],

        renamed_counts=[dict(
            was="confirmed_units = 7",
            was_read_as="seven confirmed storyboard production units outside PL06",
            actually="PL06's seven sub-modul (Topik 1-7), inside PL06, carrying a frozen "
                     "boundary map",
            now="pl06_topik_with_frozen_boundary_map = 7, reported separately",
            outside_pl06_equivalent="confirmed_storyboard_production_units_outside_pl06 = 0")],

        confirmed_segmentation=dict(
            source="the frozen PL06 boundary map — the ONLY K5 segmentation that is "
                   "confirmed",
            pl="PL06",
            topics={f"T{k:02d}": dict(bahagian=len(v),
                                      segmentation=("TOPIK_WITHOUT_BAHAGIAN"
                                                    if len(v) == 1
                                                    else "TOPIK_WITH_MULTIPLE_BAHAGIAN"),
                                      units=[u for _, u in v])
                    for k, v in seg.items()}),
        structures_affected_by_d4=dict(
            resolved=[f"T{k:02d}" for k, v in seg.items()],
            resolved_scope="PL06 only",
            unresolved_count=len(rows),
            unresolved_roll=[r["candidate_id"] for r in rows],
            unresolved_note=("Every structure outside PL06 is affected by D4 in principle "
                             "and resolvable for none of them: D4 keys on Topik/Bahagian "
                             "segmentation, and no segmentation is confirmed outside "
                             "PL06.")),
        still_not_confirmed_production_units=[r["candidate_id"] for r in rows],
        rows=rows)


# ==========================================================================================
# FORECAST
# ==========================================================================================
FORECAST_STATUS = "FORECAST_NOT_COMMITMENT"

# Section B is CLOSED. The old three scenarios were keyed on "when does Section B arrive",
# and that question is answered: 4 Ogos 2026, a day inside the 5 Ogos deadline. Keeping
# those scenarios would forecast a risk that no longer exists.
#
# The binding variable is now different and smaller: Bariah gave a rate (one unit per
# 90-minute slot) and a conditional availability (working days except Cyberjaya meeting
# days, weekends optional, several slots possible on an available day). What she did NOT
# give is how many slots land on which days — and she said so. That is Firdaus's to
# confirm, so it is the axis the scenarios now turn on.
SECTION_B_RESOLVED = dict(
    date="4 Ogos 2026", deadline="5 Ogos 2026", met_deadline=True,
    status="APPROVED_WITH_AMENDMENTS_FOR_CALIBRATION",
    what_it_unblocked=["two-file packaging (B1)", "calibration generation of four units",
                       "a known review rate (B3)"],
    what_it_did_not_unblock=["B2 panel density — test required first",
                             "actual review dates and slot counts — Firdaus to confirm",
                             "mass generation of the remaining K5 units"])

# The one number Bariah fixed, and the one she explicitly did not.
REVIEW_CONSTRAINT = dict(
    slot_minutes=90, units_per_slot=1, basis="B3",
    calibration_units=4,
    total_review_minutes_required=4 * 90,
    total_review_hours_required=6.0,
    slots_required=4,
    slots_per_day="NOT_CONFIRMED — Bariah allows several on an available day; the actual "
                  "count is Firdaus's to confirm",
    available_days="NOT_CONFIRMED — working days except Cyberjaya meeting days; weekends "
                   "optional and not fixed",
    note=("Four calibration units need four full slots — six hours of Bariah's attention "
          "— and they cannot be compressed. That is a floor set by the ruling, not an "
          "estimate."))

CONDITIONAL_ASSUMPTIONS = [
    "A1 — engineering generation of a deck from an approved model is machine work in "
    "minutes; it is not the constraint.",
    "A2 — the constraint is Bariah's review throughput, now bounded below by B3 at one "
    "unit per 90-minute slot.",
    "A3 — a correction cycle is one pass of feedback plus regeneration; a cycle changing a "
    "GLOBAL pattern costs materially more than one changing a unit exception.",
    "A4 — B2's density test rides along with the calibration package; it does not add a "
    "review slot of its own, because the alternate-density file shows the same unit and "
    "the same states.",
    "A5 — no availability date or slot count is assumed anywhere below.",
    "A6 — PL06 carries 14 storyboard production units; outside PL06 no production-unit "
    "count is proven, so no full-K5 date can be computed at all.",
]

FORECAST = dict(
    stage=STAGE,
    status=FORECAST_STATUS,
    status_note=("Forecasts under stated conditions, not commitments. Section B is "
                 "resolved, so the remaining variance is availability — which is "
                 "Firdaus's to confirm and is never assumed here."),
    basis=("Recomputed against the real review constraint Bariah gave: one unit per "
           "90-minute slot, several slots possible on an available day, availability "
           "conditional. No slot count and no date is invented."),
    section_b_resolved=SECTION_B_RESOLVED,
    review_constraint=REVIEW_CONSTRAINT,
    open_variables=dict(
        slots_per_available_day="UNCONFIRMED — requires Firdaus",
        available_dates="UNCONFIRMED — working days minus Cyberjaya meeting days",
        b2_density_outcome="UNKNOWN until Bariah sees the 2-panel and 3-panel examples",
        consequence=("Every review-completion range below is expressed in SLOTS, which is "
                     "knowable, and converted to days only as a conditional band.")),
    assumptions=CONDITIONAL_ASSUMPTIONS,
    fixed_inputs=dict(
        section_b_decision_date="4 Ogos 2026",
        bariah_feedback_deadline="5 Ogos 2026 — met",
        internal_storyboard_target="9 Ogos 2026",
        calibration_units=len(CALIBRATION_UNITS),
        review_slots_required_for_calibration=4,
        review_hours_required_for_calibration=6.0,
        pl06_storyboard_production_units=14,
        outside_pl06_production_units="NOT_PROVEN — 22 candidate structures, 0 confirmed"),
    scenarios=[
        dict(
            id="A", name="Two or more review slots per available day",
            section_b_decision_date="4 Ogos 2026",
            slots_per_day_assumed="2 or more — CONDITIONAL, requires Firdaus confirmation",
            calibration_completion_range=(
                "generation and internal QA: same day as authorisation; calibration "
                "package ready for review immediately"),
            batch_generation_start_range=(
                "after the single calibration review round closes — 2 available days at "
                "2 slots/day"),
            engineering_generation_completion_range=(
                "PL06's remaining 10 units: machine work, hours not days, once the "
                "calibration pattern is frozen"),
            bariah_review_freeze_completion_range=(
                "4 slots over 2 available days, PLUS one correction cycle. If both "
                "available days fall on 5-6 Ogos, freeze lands 6-7 Ogos."),
            full_k5_package_completion_range=(
                "NOT_COMPUTABLE — PL06 could complete inside the window; full K5 requires "
                "the 22 outside-PL06 candidates resolved into production units first, and "
                "that count is not proven."),
            assumptions=["A1", "A2", "A3", "A4", "A5", "A6"],
            principal_blockers=["Firdaus to confirm available days and slot counts",
                                "B2 density outcome",
                                "22 outside-PL06 candidates unresolved"],
            target_9_aug="ACHIEVABLE_FOR_PL06", confidence="MODERATE"),
        dict(
            id="B", name="One review slot per available day",
            section_b_decision_date="4 Ogos 2026",
            slots_per_day_assumed="1 — CONDITIONAL, requires Firdaus confirmation",
            calibration_completion_range=(
                "generation and internal QA: same day; package ready immediately"),
            batch_generation_start_range="after 4 available days of review",
            engineering_generation_completion_range=(
                "PL06's remaining 10 units: hours once the pattern is frozen"),
            bariah_review_freeze_completion_range=(
                "4 slots over 4 available days, plus a correction cycle. On consecutive "
                "working days from 5 Ogos that lands 8-9 Ogos — with no slack."),
            full_k5_package_completion_range="NOT_COMPUTABLE — same reason",
            assumptions=["A1", "A2", "A3", "A4", "A5", "A6"],
            principal_blockers=["review throughput is the critical path at this rate",
                                "any Cyberjaya meeting day removes a slot outright",
                                "a global-pattern correction would push past 9 Ogos",
                                "22 outside-PL06 candidates unresolved"],
            target_9_aug="AT_RISK_FOR_PL06", confidence="LOW_TO_MODERATE"),
        dict(
            id="C", name="Availability interrupted — Cyberjaya meetings or unconfirmed days",
            section_b_decision_date="4 Ogos 2026",
            slots_per_day_assumed="fewer than 1 per working day on average — CONDITIONAL",
            calibration_completion_range="generation and internal QA still complete "
                                         "immediately; only review is delayed",
            batch_generation_start_range="OPEN — gated on calibration review closing",
            engineering_generation_completion_range=(
                "OPEN as a reviewed package. Modelling and generation are NOT blocked: "
                "the pattern policy is approved, so work continues."),
            bariah_review_freeze_completion_range="OPEN — unbounded without confirmed days",
            full_k5_package_completion_range="NOT_COMPUTABLE",
            assumptions=["A1", "A2", "A3", "A4", "A5", "A6"],
            principal_blockers=["Bariah availability is the sole critical path",
                                "22 outside-PL06 candidates unresolved"],
            target_9_aug="NOT_ACHIEVABLE_WITHOUT_CONFIRMED_SLOTS",
            confidence="HIGH that 9 Ogos fails if fewer than 4 slots land before 8 Ogos",
            mitigation=("The bottleneck is review, not production. Confirming which days "
                        "are Cyberjaya-free is the single highest-value action available, "
                        "and it costs nothing to produce the calibration package first so "
                        "no slot is ever spent waiting on generation.")),
    ],
    what_is_not_forecast=[
        "actual available dates — Bariah gave a rule, not a calendar; Firdaus confirms",
        "slots per day — several are possible on an available day, the number is not fixed",
        "the B2 density outcome — the test has not been shown to Bariah yet",
        "any full-K5 completion date — the outside-PL06 production-unit count is not "
        "proven, so the denominator does not exist",
    ])


if __name__ == "__main__":
    im = impact_matrix()
    cu = calibration_units()
    op = outside_pl06()
    print(f"impact matrix: {im['total']} rows, "
          f"{len(im['affected_by_section_b'])} affected by Section B "
          f"{im['affected_by_section_b']}")
    print(f"\ncalibration units: {cu['count']}")
    for u in cu["units"]:
        s = u["scenario_obligation"]
        sv = u["summary_visual_obligation"]
        print(f"  {u['unit_id']}: scenario={s['change']} "
              f"(was {s['previous_cair_verdict']}), rumusan={sv['change']}, "
              f"screens {u['screen_pattern_plan']['minimum_total_before']}"
              f"->{u['screen_pattern_plan']['minimum_total_after']}, "
              f"closing='{u['closing_screen']['closing_text']}'")
    print(f"\noutside PL06: {op['candidate_structures']} candidates, "
          f"{op['confirmed_units']} confirmed, {op['clean_candidates']} clean, "
          f"{op['amber_candidates']} amber, {op['unmapped_source_regions']} unmapped "
          f"regions ({op['unmapped_pages']} pages)")
    print(f"  D4 resolved only for PL06: "
          f"{list(op['confirmed_segmentation']['topics'])}")
    print(f"  still not confirmed production units: "
          f"{len(op['still_not_confirmed_production_units'])}")
