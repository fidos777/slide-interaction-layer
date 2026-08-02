# -*- coding: utf-8 -*-
"""Negative mutations for the Stage 4.2F-B0.7 gates.

Each fixture patches the controlled data source in memory, runs the suite, and requires the
designated gate to fire. Every patch is reverted in a `finally`; nothing on disk is touched.

A fixture proves a gate is SENSITIVE to a defect. It proves nothing about correctness.

    python3 docs/pl06/t04/tools/t04_final_rulings_mutations_v1.py
"""
import copy, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_final_rulings_data_v1 as D
import t04_final_rulings_qa_v1 as QA


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


def _dec(fn):
    def apply():
        d = copy.deepcopy(D.DECISIONS)
        fn(d)
        return dict(DECISIONS=d)
    return apply


def _split(**kw):
    def apply():
        s = copy.deepcopy(D.D04_SPLIT)
        s.update(kw)
        return dict(D04_SPLIT=s)
    return apply


FIXTURES = [
    # ---- 1. threshold ----
    dict(fid="W-01", title="the 60 percent pass mark is narrowed to T04 only",
         gates=["D02B_SCOPE_ALL_PLS_IN_KURSUS"],
         patch=lambda: dict(D02B=dict(D.D02B, scope="THIS_UNIT_ONLY"))),
    dict(fid="W-02", title="the confirmed threshold is dropped back to unresolved",
         gates=["D02B_CONFIRMED_60_PERCENT", "D02B_NO_LONGER_UNRESOLVED",
                "ALL_STRUCTURAL_DECISIONS_RESOLVED_OR_CONDITIONAL"],
         patch=_dec(lambda d: _find(d, "decision_id", "D-02B").update(
             status="UNRESOLVED", structural_status="UNRESOLVED"))),

    # ---- 2. legal split ----
    dict(fid="W-03", title="D-04 is restored to unresolved",
         gates=["D04_CONFIRMED", "ALL_STRUCTURAL_DECISIONS_RESOLVED_OR_CONDITIONAL"],
         patch=_dec(lambda d: _find(d, "decision_id", "D-04").update(
             status="CLARIFICATION_REQUIRED", structural_status="UNRESOLVED"))),
    dict(fid="W-04", title="the statute is moved off the base screen and behind a reveal",
         gates=["D04_BASE_CONTAINS_STATUTE_OPERATOR_AND_PPE", "D04_REVEAL_SET_MATCHES_RULING",
                "D04_SPLIT_APPLIED_TO_CONTRACT"],
         patch=_split(base_visible_rows=[r for r in D.BASE_VISIBLE_ROWS
                                         if r != "T04-ROW-066"],
                      reveal_eligible_rows=D.REVEAL_ELIGIBLE_ROWS + ["T04-ROW-066"])),
    dict(fid="W-05", title="PPE is moved off the base screen and behind a reveal",
         gates=["D04_BASE_CONTAINS_STATUTE_OPERATOR_AND_PPE", "D04_REVEAL_SET_MATCHES_RULING",
                "D04_SPLIT_APPLIED_TO_CONTRACT"],
         patch=_split(base_visible_rows=[r for r in D.BASE_VISIBLE_ROWS
                                         if r not in ("T04-ROW-069", "T04-ROW-070")],
                      reveal_eligible_rows=D.REVEAL_ELIGIBLE_ROWS + ["T04-ROW-069",
                                                                    "T04-ROW-070"])),
    dict(fid="W-06", title="a base row is ALSO listed as reveal-eligible",
         gates=["D04_BASE_ROWS_NEVER_REVEAL_ELIGIBLE", "D04_REVEAL_SET_MATCHES_RULING",
                "D04_SPLIT_APPLIED_TO_CONTRACT"],
         patch=_split(reveal_eligible_rows=D.REVEAL_ELIGIBLE_ROWS + ["T04-ROW-067"])),
    dict(fid="W-07", title="the confirmed split is marked applied but the contract is not "
                           "changed",
         gates=["D04_SPLIT_APPLIED_TO_CONTRACT"],
         patch=lambda: dict(CONTRACTS_V3=[
             {k: v for k, v in c.items() if k != "base_visible_rows"}
             if c["contract_id"] == "T04-CT-04" else c for c in D.CONTRACTS_V3])),

    # ---- 3. SmartArt ----
    dict(fid="W-08", title="two SmartArt nodes are swapped",
         gates=["SIX_NODES_AND_ORDER_PRESERVED", "SIX_NODES_MATCH_THE_SOURCE_ASSET"],
         patch=lambda: dict(D05=dict(
             D.D05, six_nodes_in_order=[D.D05["six_nodes_in_order"][i]
                                        for i in (0, 2, 1, 3, 4, 5)]))),
    dict(fid="W-09", title="a seventh node is added to the diagram contract",
         gates=["SIX_NODES_AND_ORDER_PRESERVED", "SIX_NODES_MATCH_THE_SOURCE_ASSET"],
         patch=lambda: dict(D05=dict(
             D.D05, six_nodes_in_order=D.D05["six_nodes_in_order"] + ["Penyeliaan Kualiti"]))),
    dict(fid="W-10", title="MMD production is marked started",
         gates=["MMD_PRODUCTION_NOT_STARTED", "NO_MMD_PRODUCTION_STARTED"],
         patch=lambda: dict(D05=dict(D.D05, mmd_production_status="IN_PROGRESS"),
                            MMD_PRODUCTION_STARTED=1,
                            READINESS=dict(D.READINESS, mmd_status="IN_PROGRESS"))),
    dict(fid="W-11", title="an asset row reports production as started",
         gates=["NO_ASSET_PRODUCTION_STARTED"],
         patch=lambda: dict(
             ASSET_PLAN=[dict(r, production_status="IN_PROGRESS") if i == 0 else r
                         for i, r in enumerate(D.ASSET_PLAN)])),

    # ---- 4. cast ----
    dict(fid="W-12", title="Alya and Encik Rahman are marked final with the contextual "
                           "assessment skipped",
         gates=["D03_POLICY_STATUS_CONDITIONAL", "CHARACTER_INSTANCE_MAPPING_NOT_COMPLETE"],
         patch=lambda: dict(D03_POLICY=dict(
             D.D03_POLICY, policy_status="CONFIRMED_BARIAH_DIRECT",
             character_instance_mapping="COMPLETE"))),
    dict(fid="W-13", title="the CAIR fit assessment is relabelled as a Bariah ruling",
         gates=["CONTEXTUAL_ASSESSMENT_IS_NOT_A_BARIAH_RULING"],
         patch=lambda: dict(CONTEXTUAL_FIT=dict(
             D.CONTEXTUAL_FIT, authority="BARIAH_DIRECT_SCREENSHOT",
             status="CONFIRMED_BARIAH_DIRECT"))),
    dict(fid="W-14", title="the fit assessment returns a result outside the allowed set",
         gates=["CONTEXTUAL_ASSESSMENT_EXISTS_AND_IS_ALLOWED"],
         patch=lambda: dict(CONTEXTUAL_FIT=dict(
             D.CONTEXTUAL_FIT, recommendation="CAST_APPROVED"))),
    dict(fid="W-15", title="a character line states a statutory obligation",
         gates=["NO_COMPLIANCE_CONTENT_IN_ANY_CHARACTER_LINE"],
         patch=lambda: dict(SLIDE2_DIALOGUE=dict(
             D.SLIDE2_DIALOGUE,
             beats=[dict(b, draft_line="Ingat, semburan racun mesti dibuat oleh pengendali "
                                       "berlesen.") if b["beat"] == 4 else b
                    for b in D.SLIDE2_DIALOGUE["beats"]]))),
    dict(fid="W-16", title="the Slide 2 dialogue is marked approved",
         gates=["SLIDE_2_DIALOGUE_PENDING_REVIEW"],
         patch=lambda: dict(SLIDE2_DIALOGUE=dict(
             D.SLIDE2_DIALOGUE, approval_status="BARIAH_APPROVED",
             cast_status="FINAL",
             bariah_approval=dict(status="BARIAH_APPROVED", decision="ok", comment=None)))),
    dict(fid="W-17", title="a dialogue beat cites a row the contract does not declare",
         gates=["SLIDE_2_BEATS_BIND_TO_DECLARED_ROWS"],
         patch=lambda: dict(SLIDE2_DIALOGUE=dict(
             D.SLIDE2_DIALOGUE,
             beats=[dict(b, source_row_ids=b["source_row_ids"] + ["T04-ROW-066"])
                    if b["beat"] == 2 else b for b in D.SLIDE2_DIALOGUE["beats"]]))),

    # ---- 5. obligations vs assets ----
    dict(fid="W-18", title="46 obligations are equated to 46 unique MMD assets",
         gates=["UNIQUE_ASSET_COUNT_NOT_DETERMINED", "UNIQUE_ASSET_COUNT_IS_NOT_NUMERIC",
                "ASSET_JSON_MATCHES_DATA"],
         patch=lambda: dict(UNIQUE_ASSET_COUNT="46",
                            ASSET_TOTALS=dict(D.ASSET_TOTALS, UNIQUE_ASSET_COUNT="46"))),
    dict(fid="W-19", title="an asset-planning row asserts a unique asset count in prose",
         gates=["OBLIGATION_COUNT_NOT_ASSERTED_AS_UNIQUE_ASSET_COUNT"],
         patch=lambda: dict(ASSET_TOTALS=dict(
             D.ASSET_TOTALS,
             slide_2_visual_note="Production estimate: UNIQUE_MMD_ASSETS = 46."))),
    dict(fid="W-20", title="unique asset IDs are assigned before the grouping is decided",
         gates=["NO_UNIQUE_ASSET_ID_ASSIGNED_YET"],
         patch=lambda: dict(
             ASSET_PLAN=[dict(r, unique_asset_candidate_id="UA-001") if i == 0 else r
                         for i, r in enumerate(D.ASSET_PLAN)])),
    dict(fid="W-21", title="the coverage status claims coverage already exists",
         gates=["VISUAL_COVERAGE_STATUS"],
         patch=lambda: dict(VISUAL_COVERAGE_STATUS="VISUAL_COVERAGE_COMPLETE")),
    dict(fid="W-22", title="two near-duplicate PPE subjects are marked reusable",
         gates=["NEAR_DUPLICATE_SUBJECTS_MARKED_DO_NOT_REUSE",
                "ASSET_TOTALS_AGREE_WITH_THE_LIVE_PLAN"],
         patch=lambda: dict(
             ASSET_PLAN=[dict(r, reuse_allowed="REUSE_ALLOWED")
                         if r["reuse_allowed"] == "SIMILAR_SUBJECT_DO_NOT_REUSE" else r
                         for r in D.ASSET_PLAN])),

    # ---- 6. approval accounting ----
    dict(fid="W-23", title="every decision is reported as unapproved",
         gates=["CONFIRMED_POLICY_DECISIONS", "CONFIRMED_POLICY_DECISIONS_NOT_ZERO",
                "CONDITIONALLY_CONFIRMED_DECISIONS"],
         patch=lambda: dict(APPROVAL_TOTALS=dict(
             D.APPROVAL_TOTALS, CONFIRMED_POLICY_DECISIONS=0,
             CONDITIONALLY_CONFIRMED_DECISIONS=0,
             confirmed_policy_decision_ids=[], conditionally_confirmed_decision_ids=[]))),
    dict(fid="W-24", title="the Rumusan is reported as approved final content",
         gates=["NO_FINAL_INSTRUCTIONAL_CONTENT_APPROVED", "EVERY_PENDING_REVIEW_IS_PENDING",
                "PENDING_CONTENT_REVIEWS", "ONLY_RUMUSAN_QUIZ_DIALOGUE_AND_CAST_REMAIN"],
         patch=lambda: dict(
             APPROVAL_TOTALS=dict(D.APPROVAL_TOTALS,
                                  APPROVED_FINAL_INSTRUCTIONAL_CONTENT_ITEMS=4,
                                  PENDING_BARIAH_CONTENT_REVIEWS=3),
             PENDING_CONTENT_REVIEWS=[r for r in D.PENDING_CONTENT_REVIEWS
                                      if r["review_id"] != "CR-3"])),
    dict(fid="W-25", title="quiz content is reported as approved",
         gates=["NO_FINAL_INSTRUCTIONAL_CONTENT_APPROVED", "EVERY_PENDING_REVIEW_IS_PENDING"],
         patch=lambda: dict(
             APPROVAL_TOTALS=dict(D.APPROVAL_TOTALS,
                                  APPROVED_FINAL_INSTRUCTIONAL_CONTENT_ITEMS=5),
             PENDING_CONTENT_REVIEWS=[dict(r, status="BARIAH_APPROVED")
                                      if r["review_id"] == "CR-4" else r
                                      for r in D.PENDING_CONTENT_REVIEWS])),
    dict(fid="W-26", title="the storyboard is claimed approved",
         gates=["STORYBOARD_NOT_CLAIMED_APPROVED"],
         patch=lambda: dict(READINESS=dict(
             D.READINESS, storyboard_status="GENERATED",
             storyboard_approval="APPROVED_BY_BARIAH"))),

    # ---- 7. evidence and D-05 bookkeeping ----
    dict(fid="W-27", title="an evidence SHA-256 no longer matches the frozen bytes",
         gates=["ALL_EVIDENCE_BYTE_IDENTICAL"],
         patch=lambda: dict(EVIDENCE_NEW=[dict(e, sha256="0" * 64) for e in D.EVIDENCE_NEW],
                            EVIDENCE_ALL=[dict(e, sha256="0" * 64)
                                          if e["evidence_id"] == "T04-EV-03" else e
                                          for e in D.EVIDENCE_ALL])),
    dict(fid="W-28", title="the three-versus-one delivery discrepancy is hidden",
         gates=["EVIDENCE_DELIVERY_DISCREPANCY_DECLARED"],
         patch=lambda: dict(EVIDENCE_DELIVERY=dict(
             D.EVIDENCE_DELIVERY, expected_by_instruction=1))),
    dict(fid="W-29", title="the illegible Akta line is attributed to the screenshot",
         gates=["ILLEGIBLE_ELEMENTS_NOT_ATTRIBUTED_TO_SCREENSHOT"],
         patch=lambda: dict(EVIDENCE_LEGIBILITY=[
             dict(L, authority="BARIAH_DIRECT_SCREENSHOT") for L in D.EVIDENCE_LEGIBILITY])),
    dict(fid="W-30", title="D-05 reappears in the pending content reviews",
         gates=["D05_ABSENT_FROM_UNRESOLVED_LISTS", "PENDING_CONTENT_REVIEWS",
                "ONLY_RUMUSAN_QUIZ_DIALOGUE_AND_CAST_REMAIN"],
         patch=lambda: dict(PENDING_CONTENT_REVIEWS=D.PENDING_CONTENT_REVIEWS + [
             dict(review_id="CR-5", title="SmartArt treatment", decision="D-05",
                  what="confirm", cair_position="", status="PENDING_BARIAH_REVIEW")])),
    dict(fid="W-31", title="the Slide 2 candidate is dropped from the mapping",
         gates=["MAPPING_CANDIDATES", "SLIDE_2_CANDIDATE_ADDED",
                "CONTRACT_AND_CANDIDATE_IDS_UNIQUE", "MAPPING_JSON_MATCHES_DATA"],
         patch=lambda: dict(MAPPING_V3=[m for m in D.MAPPING_V3
                                        if m["screen_candidate_id"] != "T04-SC-07"])),
    dict(fid="W-32", title="a final screen count is claimed",
         gates=["FINAL_SCREEN_COUNT_NOT_CLAIMED", "MAPPING_JSON_MATCHES_DATA"],
         patch=lambda: dict(FINAL_SCREEN_COUNT="19",
                            MAPPING_IMPACT_V3=dict(D.MAPPING_IMPACT_V3,
                                                   final_screen_count="19"))),
]


def run_fixture(f):
    patch = f["patch"]()
    saved = {k: getattr(D, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(D, k, v)
        return {r["gate_id"]: r["ok"] for r in QA.run()}
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(D, k, v)


def main():
    good = {r["gate_id"]: r["ok"] for r in QA.run()}
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], title=f["title"], designated_gates=f["gates"],
                        detected=det, fired=fired))
    return dict(baseline_pass=sum(1 for v in good.values() if v), baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out), detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if r["missed"] or r["baseline_false_failures"] else 0)
