# -*- coding: utf-8 -*-
"""Negative mutations for the Stage 4.2F-B0.8 gates (SUITE_ID = T04_CONTENT_QA_v1).

Each fixture patches the controlled data source — or, where the defect is in the reporting
harness itself, the QA module — runs the suite, and requires the designated gate to fire.
Every patch is reverted in a `finally`; nothing on disk is touched.

A fixture proves a gate is SENSITIVE to a defect. It proves nothing about correctness.

    python3 docs/pl06/t04/tools/t04_content_mutations_v1.py
"""
import copy, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_content_data_v1 as D
import t04_content_qa_v1 as QA

TARGETS = {"D": D, "QA": QA}


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


def _closure(fn):
    def apply():
        c = copy.deepcopy(D.OBLIGATION_CLOSURE)
        fn(c)
        return dict(OBLIGATION_CLOSURE=c)
    return apply


def _quiz(fn):
    def apply():
        q = copy.deepcopy(D.QUIZ)
        fn(q)
        return dict(QUIZ=q)
    return apply


def _rum(fn):
    def apply():
        r = copy.deepcopy(D.RUMUSAN)
        fn(r)
        return dict(RUMUSAN=r)
    return apply


def _dlg(fn):
    def apply():
        g = copy.deepcopy(D.DIALOGUE)
        fn(g)
        return dict(DIALOGUE=g)
    return apply


FIXTURES = [
    # ---- obligation closure ----
    dict(fid="V-01", title="one visual obligation loses its screen mapping",
         gates=["MAPPED_OUTCOMES_CARRY_A_SCREEN", "ORPHAN_OBLIGATIONS",
                "EVERY_MAPPED_OBLIGATION_APPEARS_ON_ITS_SCREEN"],
         patch=_closure(lambda c: _find(c, "obligation_id", "T04-VO-013").update(
             proposed_learner_screen_id=None, proposed_runtime_state_id=None))),
    dict(fid="V-02", title="an obligation is left orphaned with the forbidden outcome",
         gates=["EVERY_OBLIGATION_HAS_A_LEGAL_OUTCOME", "FORBIDDEN_OUTCOME_ABSENT",
                "VISUAL_OBLIGATIONS_CLOSED"],
         patch=_closure(lambda c: _find(c, "obligation_id", "T04-VO-020").update(
             closure_outcome="UNMAPPED_WITHOUT_REASON"))),
    dict(fid="V-03", title="an obligation is dropped from the closure entirely",
         gates=["VISUAL_OBLIGATIONS_TOTAL", "VISUAL_OBLIGATIONS_CLOSED",
                "CLOSURE_TOTALS_DERIVED_LIVE", "CLOSURE_JSON_MATCHES_DATA"],
         patch=_closure(lambda c: c.remove(_find(c, "obligation_id", "T04-VO-046")))),
    dict(fid="V-04", title="a non-resolving obligation ID is hand-typed into a rationale",
         gates=["NO_HAND_TYPED_OBLIGATION_ID_FAILS_TO_RESOLVE"],
         patch=_closure(lambda c: _find(c, "obligation_id", "T04-VO-007").update(
             rationale="Covered together with T04-VO-099, which does not exist."))),
    dict(fid="V-05", title="a NOT_A_SEPARATE_ASSET outcome loses its reason",
         gates=["NON_ASSET_OUTCOMES_CARRY_A_REASON", "EVERY_CLOSURE_ROW_HAS_A_RATIONALE"],
         patch=_closure(lambda c: _find(c, "obligation_id", "T04-VO-012").update(
             rationale=""))),
    dict(fid="V-06", title="a runtime-state outcome loses its state id",
         gates=["RUNTIME_STATE_OUTCOMES_CARRY_A_STATE"],
         patch=_closure(lambda c: _find(c, "obligation_id", "T04-VO-030").update(
             proposed_runtime_state_id=None))),
    dict(fid="V-07", title="a visual subject is promoted to Bariah-direct authority",
         gates=["SUBJECT_AUTHORITY_NEVER_BARIAH_DIRECT"],
         patch=_closure(lambda c: _find(c, "obligation_id", "T04-VO-019").update(
             subject_authority="BARIAH_DIRECT_SCREENSHOT"))),
    dict(fid="V-08", title="the population derivation is attributed to Bariah",
         gates=["POPULATION_DERIVATION_IS_THE_MODULE_HIERARCHY"],
         patch=_closure(lambda c: _find(c, "obligation_id", "T04-VO-011").update(
             population_derivation_authority="BARIAH_DIRECT_SCREENSHOT"))),
    dict(fid="V-09", title="the retired policy rule name is restored as the live rule",
         gates=["SUPERSEDED_RULE_NAME_NOT_USED_AS_THE_LIVE_RULE"],
         patch=lambda: dict(DECISIONS=[
             dict(d, ruling=D.SUPERSEDED_POLICY_RULE) if d["decision_id"] == "D-01" else d
             for d in D.DECISIONS])),
    dict(fid="V-10", title="the Akta placement is upgraded to a legible Bariah statement",
         gates=["D04_MIXED_PROVENANCE_EXPLICIT", "AKTA_NOT_CLASSIFIED_AS_LEGIBLE_BARIAH_TEXT"],
         patch=lambda: dict(D04_PROVENANCE=dict(
             D.D04_PROVENANCE, akta_base_screen_placement="BARIAH_DIRECT_SCREENSHOT"))),

    # ---- asset accounting ----
    dict(fid="V-11", title="46 obligations are equated with 46 unique assets",
         gates=["OBLIGATION_COUNT_NOT_EQUATED_TO_UNIQUE_ASSET_COUNT",
                "ASSET_TOTALS_DERIVED_LIVE"],
         patch=lambda: dict(ASSET_TOTALS=dict(D.ASSET_TOTALS, proposed_unique_assets=46))),
    dict(fid="V-12", title="the unique asset count becomes a bare number",
         gates=["UNIQUE_ASSET_COUNT_STATUS", "UNIQUE_ASSET_COUNT_NOT_A_BARE_NUMBER",
                "ASSET_JSON_MATCHES_DATA"],
         patch=lambda: dict(UNIQUE_ASSET_COUNT="41")),
    dict(fid="V-13", title="an asset-group total is edited after the cached calculation",
         gates=["ASSET_TOTALS_DERIVED_LIVE", "FORECAST_TOTALS_DERIVED_LIVE"],
         patch=lambda: dict(ASSET_GROUPS=[
             dict(g, proposed_unique_assets=g["proposed_unique_assets"] + 5)
             if g["asset_group_id"] == "AG-04" else g for g in D.ASSET_GROUPS])),
    dict(fid="V-14", title="the do-not-reuse group and obligation counts are collapsed",
         gates=["DO_NOT_REUSE_GROUP_AND_OBLIGATION_COUNTS_ARE_DISTINCT",
                "ASSET_TOTALS_DERIVED_LIVE"],
         patch=_closure(lambda c: _find(c, "obligation_id", "T04-VO-040").update(
             reuse_policy="NOT_YET_ASSESSED"))),
    dict(fid="V-15", title="a unique asset count is asserted in prose",
         gates=["NO_UNIQUE_ASSET_COUNT_ASSERTED_IN_PROSE"],
         patch=lambda: dict(ASSET_TOTALS=dict(
             D.ASSET_TOTALS,
             obligations_are_not_assets="Production plan: UNIQUE_MMD_ASSETS = 41."))),
    dict(fid="V-16", title="an empty asset group loses its by-design declaration",
         gates=["EMPTY_ASSET_GROUPS_ARE_DECLARED"],
         patch=lambda: dict(ASSET_GROUPS=[
             {k: v for k, v in g.items()
              if k not in ("obligations_covered_empty_by_design", "empty_reason")}
             if g["asset_group_id"] == "AG-08" else g for g in D.ASSET_GROUPS])),

    # ---- screen sequence ----
    dict(fid="V-17", title="a controlled source population is omitted from the sequence",
         gates=["EVERY_SOURCE_ROW_APPEARS_ON_A_SCREEN", "SEQUENCE_JSON_MATCHES_DATA",
                "PROPOSED_LEARNER_SCREEN_COUNT"],
         patch=lambda: dict(SCREEN_SEQUENCE=[s for s in D.SCREEN_SEQUENCE
                                             if s["screen_id"] != "T04-S18"])),
    dict(fid="V-18", title="a required population is left with no screens",
         gates=["EVERY_REQUIRED_POPULATION_HAS_SCREENS"],
         patch=lambda: dict(REQUIRED_POPULATIONS=[
             dict(p, screens=[]) if p["population"] == "quiz" else p
             for p in D.REQUIRED_POPULATIONS])),
    dict(fid="V-19", title="the proposed screen count is presented as final",
         gates=["FINAL_SCREEN_COUNT_PENDING_APPROVAL", "NO_FINAL_SCREEN_COUNT_CLAIMED",
                "PROPOSED_AND_FINAL_COUNTS_ARE_DISTINCT_FIELDS",
                "SEQUENCE_JSON_MATCHES_DATA"],
         patch=lambda: dict(FINAL_LEARNER_SCREEN_COUNT="21")),
    dict(fid="V-20", title="a B02 family label is added to a screen",
         gates=["NO_B02_FAMILY_LABEL"],
         patch=lambda: dict(SCREEN_SEQUENCE=[
             dict(s, base_state="Reuse the B02 FAMILY_S selection screen wholesale.")
             if s["screen_id"] == "T04-S06" else s for s in D.SCREEN_SEQUENCE])),
    dict(fid="V-21", title="the B02 screen count is declared inherited",
         gates=["B02_SCREEN_COUNT_NOT_INHERITED"],
         patch=lambda: dict(B02_SCREEN_COUNT_INHERITED=True)),
    dict(fid="V-22", title="a content screen loses its source binding",
         gates=["EVERY_CONTENT_SCREEN_HAS_SOURCE_ROWS", "STRUCTURAL_SCREENS_DECLARED",
                "EVERY_SOURCE_ROW_APPEARS_ON_A_SCREEN"],
         patch=lambda: dict(SCREEN_SEQUENCE=[
             dict(s, source_row_ids=[]) if s["screen_id"] == "T04-S12" else s
             for s in D.SCREEN_SEQUENCE])),
    dict(fid="V-23", title="a screen is pre-marked as reviewed",
         gates=["EVERY_SCREEN_PENDING_BARIAH_REVIEW"],
         patch=lambda: dict(SCREEN_SEQUENCE=[
             dict(s, bariah_review_status="BARIAH_APPROVED")
             if s["screen_id"] == "T04-S03" else s for s in D.SCREEN_SEQUENCE])),

    # ---- dialogue ----
    dict(fid="V-24", title="Alya and Encik Rahman are marked final without Bariah approval",
         gates=["NO_FINAL_CAST_APPROVAL_CLAIMED"],
         patch=_dlg(lambda g: g.update(cast_status="FINAL_CAST_CONFIRMED"))),
    dict(fid="V-25", title="the fit assessment is relabelled as a Bariah ruling",
         gates=["FIT_ASSESSMENT_IS_CAIR_NOT_BARIAH"],
         patch=lambda: dict(CONTEXTUAL_FIT=dict(
             D.CONTEXTUAL_FIT, authority="BARIAH_DIRECT_SCREENSHOT",
             status="BARIAH_APPROVED"))),
    dict(fid="V-26", title="a licensed-operator obligation is put in Encik Rahman's mouth",
         gates=["NO_COMPLIANCE_OBLIGATION_IN_DIALOGUE"],
         patch=_dlg(lambda g: _find(g["lines"], "dialogue_line_id", "T04-DLG-04").update(
             text="Dan ingat, semburan racun mesti dibuat oleh pengendali berlesen sahaja."))),
    dict(fid="V-27", title="a dialogue line loses its source binding",
         gates=["EVERY_DIALOGUE_LINE_HAS_SOURCE_ROWS",
                "EVERY_SUBSTANTIVE_DRAFT_LINE_HAS_SOURCE_ROWS"],
         patch=_dlg(lambda g: _find(g["lines"], "dialogue_line_id", "T04-DLG-02").update(
             source_row_ids=[]))),
    dict(fid="V-28", title="Slide 2 is escalated beyond process-overview level",
         gates=["SLIDE_2_REMAINS_PROCESS_OVERVIEW"],
         patch=_dlg(lambda g: g.update(level="FULL_COMPLIANCE_BRIEFING"))),

    # ---- Rumusan ----
    dict(fid="V-29", title="a fifth Rumusan point is added",
         gates=["RUMUSAN_POINT_COUNT", "RUMUSAN_JSON_MATCHES_DATA"],
         patch=_rum(lambda r: r["points"].append(dict(
             point_id="T04-RUM2-05", draft_text="Ayat tambahan.",
             source_row_ids=["T04-ROW-002"], source_heading="x",
             style_rule_applied=["SR-03"], style_deviation=None,
             factual_risk_status="LOW",
             bariah_review=dict(accept=None, edit=None, remove=None, comment=None))))),
    dict(fid="V-30", title="a Rumusan point loses its source binding",
         gates=["EVERY_RUMUSAN_POINT_HAS_SOURCE_ROWS",
                "EVERY_SUBSTANTIVE_DRAFT_LINE_HAS_SOURCE_ROWS"],
         patch=_rum(lambda r: _find(r["points"], "point_id", "T04-RUM2-02").update(
             source_row_ids=[]))),
    dict(fid="V-31", title="the Rumusan is marked BARIAH_APPROVED",
         gates=["RUMUSAN_REMAINS_A_DRAFT", "FORBIDDEN_LABELS_ABSENT"],
         patch=_rum(lambda r: r.update(content_status="BARIAH_APPROVED",
                                       approval_status="BARIAH_APPROVED"))),
    dict(fid="V-32", title="the medium-risk generalisation flag is removed",
         gates=["MEDIUM_RISK_GENERALISATION_DISCLOSED"],
         patch=_rum(lambda r: _find(r["points"], "point_id", "T04-RUM2-04").update(
             factual_risk_status="LOW"))),
    dict(fid="V-33", title="a Rumusan point is pre-accepted on Bariah's behalf",
         gates=["NO_RUMUSAN_POINT_PRE_ACCEPTED"],
         patch=_rum(lambda r: _find(r["points"], "point_id", "T04-RUM2-01")["bariah_review"]
                    .update(accept=True))),

    # ---- quiz ----
    dict(fid="V-34", title="quiz composition is changed to five MCQ",
         gates=["QUIZ_COMPOSITION_4_MCQ_1_MR", "MR_HAS_MORE_THAN_ONE_CORRECT_ANSWER"],
         patch=_quiz(lambda q: _find(q["items"], "question_id", "Q5").update(
             question_type="MCQ", proposed_correct_answer=["A"]))),
    dict(fid="V-35", title="the pass threshold is changed to another value",
         gates=["PASS_THRESHOLD_60_PERCENT", "QUIZ_JSON_MATCHES_DATA"],
         patch=_quiz(lambda q: q.update(pass_threshold="70_PERCENT"))),
    dict(fid="V-36", title="the threshold scope is reduced to T04 only",
         gates=["QUIZ_SCOPE_ALL_PLS_IN_KURSUS"],
         patch=_quiz(lambda q: q.update(scope="THIS_UNIT_ONLY"))),
    dict(fid="V-37", title="an item loses its correct-answer evidence",
         gates=["EVERY_ITEM_HAS_CORRECT_ANSWER_EVIDENCE",
                "CORRECT_ANSWER_EVIDENCE_CITES_CONTROLLED_ROWS"],
         patch=_quiz(lambda q: _find(q["items"], "question_id", "Q3").update(
             correct_answer_evidence=""))),
    dict(fid="V-38", title="an item's evidence cites no controlled row",
         gates=["CORRECT_ANSWER_EVIDENCE_CITES_CONTROLLED_ROWS"],
         patch=_quiz(lambda q: _find(q["items"], "question_id", "Q2").update(
             correct_answer_evidence="Everyone in the industry knows sprinklers suit turf."))),
    dict(fid="V-39", title="the answer key is marked final",
         gates=["ANSWER_KEY_NOT_FINAL", "QUIZ_JSON_MATCHES_DATA"],
         patch=_quiz(lambda q: q.update(answer_key_status="FINAL_ANSWER_KEY",
                                        answer_key_approval="APPROVED"))),
    dict(fid="V-40", title="an item requires knowledge from outside the controlled source",
         gates=["NO_EXTERNAL_KNOWLEDGE_REQUIRED", "EVERY_DRAFT_SOURCE_ROW_EXISTS",
                "EVIDENCE_ROWS_EXIST_AND_ARE_DECLARED"],
         patch=_quiz(lambda q: _find(q["items"], "question_id", "Q4").update(
             source_row_ids=["T04-ROW-999"]))),
    dict(fid="V-41", title="a proposed answer is not among the offered options",
         gates=["EVERY_PROPOSED_ANSWER_IS_AN_OFFERED_OPTION"],
         patch=_quiz(lambda q: _find(q["items"], "question_id", "Q1").update(
             proposed_correct_answer=["E"]))),
    dict(fid="V-42", title="a coverage point is silently discarded",
         gates=["NO_COVERAGE_POINT_DISCARDED"],
         patch=_quiz(lambda q: q["coverage_accounting"].update(
             discarded=1, blueprint_points=["T04-QB-01", "T04-QB-02", "T04-QB-05",
                                            "T04-QB-06"]))),
    dict(fid="V-43", title="the merged coverage disclosure is removed",
         gates=["MERGED_COVERAGE_DISCLOSED"],
         patch=_quiz(lambda q: q["coverage_accounting"]["merged"].update(
             disclosure="", cost=""))),
    dict(fid="V-44", title="a quiz option names the Act",
         gates=["NO_QUIZ_OPTION_NAMES_THE_ACT"],
         patch=_quiz(lambda q: _find(q["items"], "question_id", "Q5")["draft_options"]
                     .append(("G", "Akta Racun Makhluk Perosak 1974 mesti dipamerkan")))),
    dict(fid="V-45", title="the quiz is marked approved content",
         gates=["QUIZ_REMAINS_A_DRAFT", "FORBIDDEN_LABELS_ABSENT"],
         patch=_quiz(lambda q: q.update(content_status="FINAL_INSTRUCTIONAL_CONTENT",
                                        approval_status="BARIAH_APPROVED"))),

    # ---- MMD ----
    dict(fid="V-46", title="MMD production is marked started",
         gates=["MMD_PRODUCTION_NOT_STARTED", "EVERY_FORECAST_GROUP_NOT_STARTED"],
         patch=lambda: dict(
             MMD_PRODUCTION_STARTED=1,
             MMD_FORECAST=dict(D.MMD_FORECAST, production_status="IN_PROGRESS",
                               groups=[dict(g, mmd_production_status="IN_PROGRESS")
                                       for g in D.MMD_FORECAST["groups"]]))),
    dict(fid="V-47", title="the preliminary forecast is converted into a production commitment",
         gates=["FORECAST_LABELLED_PRELIMINARY"],
         patch=lambda: dict(MMD_FORECAST=dict(
             D.MMD_FORECAST, status="PRODUCTION_PLAN",
             commitment="COMMITTED_PRODUCTION_SCOPE", gate="APPROVED"))),
    dict(fid="V-48", title="production hours are invented without a measured baseline",
         gates=["NO_PRODUCTION_HOURS_WITHOUT_A_BASELINE"],
         patch=lambda: dict(MMD_FORECAST=dict(
             D.MMD_FORECAST,
             hours_note="Estimated 164 hours across the eight groups."))),

    # ---- readiness ----
    dict(fid="V-49", title="instance mapping is claimed complete rather than proposed",
         gates=["INSTANCE_MAPPING_COMPLETE_NOT_CLAIMED", "READINESS_SEMANTICS"],
         patch=lambda: dict(READINESS=dict(
             D.READINESS, INSTANCE_MAPPING_PROPOSED_COMPLETE="INSTANCE_MAPPING_COMPLETE"))),
    dict(fid="V-50", title="the storyboard build is declared authorised",
         gates=["READINESS_SEMANTICS"],
         patch=lambda: dict(READINESS=dict(D.READINESS,
                                           STORYBOARD_BUILD_AUTHORISED="YES",
                                           FINAL_CONTENT_APPROVED="YES"))),

    # ---- reporting harness ----
    dict(fid="V-51", title="the NOT_CHECKED list is removed", target="QA",
         gates=["NOT_CHECKED_LIST_PRESENT"],
         patch=lambda: dict(NOT_CHECKED=[])),
    dict(fid="V-52", title="a gate population empties out unexpectedly",
         gates=["NO_UNDECLARED_EMPTY_POPULATION", "EVERY_REQUIRED_POPULATION_HAS_SCREENS"],
         patch=lambda: dict(REQUIRED_POPULATIONS=[])),
    dict(fid="V-53", title="the suite identity is lost", target="QA",
         gates=["SUITE_ID_PRESENT"],
         patch=lambda: dict(SUITE_ID="")),
]


def run_fixture(f):
    tgt = TARGETS[f.get("target", "D")]
    patch = f["patch"]()
    saved = {k: getattr(tgt, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(tgt, k, v)
        return {r["gate_id"]: r["ok"] for r in QA.run()}
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(tgt, k, v)


def main():
    good = {r["gate_id"]: r["ok"] for r in QA.run()}
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], title=f["title"],
                        target=f.get("target", "D"), designated_gates=f["gates"],
                        detected=det, fired=fired))
    return dict(suite_id=QA.SUITE_ID,
                baseline_pass=sum(1 for v in good.values() if v), baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out), detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                skipped=[], fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if r["missed"] or r["baseline_false_failures"] else 0)
