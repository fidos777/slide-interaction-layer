# -*- coding: utf-8 -*-
"""Negative mutations for the T04 decision-pack gates.

Each fixture patches the controlled data source in memory, runs the suite, and requires the
designated gate to fire. Every patch is reverted in a `finally`; nothing on disk is touched.

    python3 docs/pl06/t04/tools/t04_pack_mutations_v1.py
"""
import copy, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_pack_data_v1 as P
import t04_pack_qa_v1 as QA


def _m(fn):
    def apply():
        m = copy.deepcopy(P.MAPPING); fn(m); return dict(MAPPING=m)
    return apply


def _c(fn):
    def apply():
        c = copy.deepcopy(P.CONTRACTS); fn(c); return dict(CONTRACTS=c)
    return apply


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


FIXTURES = [
    # ---- source bindings ----
    dict(fid="Y-01", title="a proposed screen loses its source-row binding",
         gates=["SCREEN_WITHOUT_SOURCE_ROWS", "EVERY_NON_PENDING_SCREEN_HAS_ROWS"],
         patch=_m(lambda m: _find(m, "screen_candidate_id", "T04-SC-02").update(
             source_row_ids=[]))),
    dict(fid="Y-02", title="a screen cites a source row that does not exist",
         gates=["SCREEN_ROWS_NOT_IN_EXTRACT"],
         patch=_m(lambda m: _find(m, "screen_candidate_id", "T04-SC-05")["source_row_ids"]
                  .append("T04-ROW-999"))),
    dict(fid="Y-03", title="a contract cites a source row that does not exist",
         gates=["CONTRACT_ROWS_NOT_IN_EXTRACT"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-05")["source_rows"]
                  .append("T04-ROW-998"))),
    dict(fid="Y-04", title="a screen candidate is dropped from the mapping",
         gates=["SCREEN_CANDIDATES", "ALL_SIX_B0_CANDIDATES_REPRESENTED",
                "MAPPING_TREATMENTS"],
         patch=_m(lambda m: m.pop())),

    # ---- B02 propagation ----
    dict(fid="Y-05", title="a B02 execution family is added to a screen's reusable capability",
         gates=["B02_PROPAGATION_FAMILY_S"],
         patch=_m(lambda m: _find(m, "screen_candidate_id", "T04-SC-02").update(
             reusable_capability="FAMILY_S selection screen reused wholesale"))),
    dict(fid="Y-06", title="a B02 family label enters a contract",
         gates=["B02_FAMILY_IN_CONTRACTS"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-02").update(
             text_treatment="as FAMILY_P1 specification popups in B02"))),
    dict(fid="Y-07", title="a final screen count is claimed",
         gates=["FINAL_SCREEN_COUNT_NOT_CLAIMED"],
         patch=lambda: dict(SCREEN_COUNT_CLAIM=dict(P.SCREEN_COUNT_CLAIM,
                                                    final_screen_count=9))),
    dict(fid="Y-08", title="the screen count is declared derived from B02",
         gates=["SCREEN_COUNT_NOT_DERIVED_FROM_B02"],
         patch=lambda: dict(SCREEN_COUNT_CLAIM=dict(P.SCREEN_COUNT_CLAIM,
                                                    derived_from_b02=True))),

    # ---- SmartArt fidelity ----
    dict(fid="Y-09", title="the SmartArt node order is changed",
         gates=["SMARTART_NODES_EXACT_AND_ORDERED", "SMARTART_NODES_MATCH_EXTRACT"],
         patch=lambda: dict(SMARTART=dict(
             P.SMARTART, nodes=[P.SMARTART["nodes"][1], P.SMARTART["nodes"][0]]
             + P.SMARTART["nodes"][2:]))),
    dict(fid="Y-10", title="a seventh SmartArt node is added",
         gates=["SMARTART_NODE_COUNT", "SMARTART_NODES_EXACT_AND_ORDERED",
                "SMARTART_NODES_MATCH_EXTRACT"],
         patch=lambda: dict(SMARTART=dict(
             P.SMARTART, node_count=7,
             nodes=P.SMARTART["nodes"] + ["Penyeliaan Kualiti Taman"]))),
    dict(fid="Y-11", title="a hierarchy is introduced into the flat diagram",
         gates=["SMARTART_HIERARCHY_FLAT"],
         patch=lambda: dict(SMARTART=dict(
             P.SMARTART, hierarchy="Two-level: node 1 is parent of nodes 2-6"))),
    dict(fid="Y-12", title="SmartArt asset production is declared started",
         gates=["SMARTART_ASSET_PRODUCTION_NOT_STARTED"],
         patch=lambda: dict(SMARTART=dict(
             P.SMARTART,
             review_storyboard_treatment=dict(P.SMARTART["review_storyboard_treatment"],
                                              asset_production="COMPLETE")))),
    dict(fid="Y-13", title="the SmartArt treatment is marked approved",
         gates=["SMARTART_TREATMENT_STATUS"],
         patch=lambda: dict(SMARTART=dict(P.SMARTART, treatment_status="BARIAH_APPROVED"))),

    # ---- authorship ----
    dict(fid="Y-14", title="the Rumusan is labelled BARIAH_APPROVED",
         gates=["RUMUSAN_APPROVAL_STATUS", "FORBIDDEN_LABEL_BARIAH_APPROVED"],
         patch=lambda: dict(RUMUSAN=dict(P.RUMUSAN, approval_status="BARIAH_APPROVED"))),
    dict(fid="Y-15", title="the Rumusan is labelled final instructional content",
         gates=["RUMUSAN_CONTENT_STATUS", "FORBIDDEN_LABEL_FINAL_INSTRUCTIONAL_CONTENT"],
         patch=lambda: dict(RUMUSAN=dict(P.RUMUSAN,
                                         content_status="FINAL_INSTRUCTIONAL_CONTENT"))),
    dict(fid="Y-16", title="CAIR is named as instructional author",
         gates=["INSTRUCTIONAL_AUTHORITY_IS_BARIAH"],
         patch=lambda: dict(RUMUSAN=dict(P.RUMUSAN, instructional_authority="CAIR"))),
    dict(fid="Y-17", title="CAIR's role list claims instructional authorship",
         gates=["CAIR_CLAIMS_INSTRUCTIONAL_AUTHORSHIP"],
         patch=lambda: dict(ROLES=dict(
             P.ROLES, CAIR=P.ROLES["CAIR"] + ["instructional authoring"]))),
    dict(fid="Y-18", title="a decision is pre-approved on Bariah's behalf",
         gates=["DECISIONS_PRE_APPROVED"],
         patch=lambda: dict(DECISIONS=[
             dict(d, approval="accepted") if d["decision_id"] == "D-01" else d
             for d in copy.deepcopy(P.DECISIONS)])),
    dict(fid="Y-19", title="a screen contract is pre-approved",
         gates=["CONTRACTS_PRE_APPROVED", "CONTRACTS_NOT_PENDING_APPROVAL"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-01").update(
             bariah_approval=dict(status="BARIAH_APPROVED", decision="accept", comment=None)))),

    # ---- Rumusan invention ----
    dict(fid="Y-20", title="a Rumusan statement loses its source binding",
         gates=["RUMUSAN_STATEMENTS_WITHOUT_SOURCE_ROWS"],
         patch=lambda: dict(RUMUSAN=dict(P.RUMUSAN, statements=[
             dict(s, source_row_ids=[]) if s["statement_id"] == "T04-RUM-02" else s
             for s in copy.deepcopy(P.RUMUSAN["statements"])]))),
    dict(fid="Y-21", title="a Rumusan statement cites a row that does not exist",
         gates=["RUMUSAN_ROWS_NOT_IN_EXTRACT"],
         patch=lambda: dict(RUMUSAN=dict(P.RUMUSAN, statements=[
             dict(s, source_row_ids=s["source_row_ids"] + ["T04-ROW-997"])
             if s["statement_id"] == "T04-RUM-01" else s
             for s in copy.deepcopy(P.RUMUSAN["statements"])]))),
    dict(fid="Y-22", title="the Rumusan claims it came from the module",
         gates=["RUMUSAN_CLAIMS_MODULE_ORIGIN"],
         patch=lambda: dict(RUMUSAN=dict(
             P.RUMUSAN, provenance="Extracted directly from the module's own summary."))),

    # ---- quiz invention ----
    dict(fid="Y-23", title="a final quiz question is written into the blueprint",
         gates=["FINAL_QUIZ_QUESTION_PRESENT"],
         patch=lambda: dict(QUIZ=dict(P.QUIZ, blueprint=[
             dict(b, learning_point="Apakah tiga operasi penyelenggaraan landskap lembut?")
             if b["blueprint_id"] == "T04-QB-01" else b
             for b in copy.deepcopy(P.QUIZ["blueprint"])]))),
    dict(fid="Y-24", title="a final answer key is added to the blueprint",
         gates=["FINAL_ANSWER_KEY_PRESENT"],
         patch=lambda: dict(QUIZ=dict(P.QUIZ, blueprint=[
             dict(b, answer_key="B") if b["blueprint_id"] == "T04-QB-03" else b
             for b in copy.deepcopy(P.QUIZ["blueprint"])]))),
    dict(fid="Y-25", title="the quiz structure is marked resolved",
         gates=["QUIZ_STRUCTURE_UNRESOLVED"],
         patch=lambda: dict(QUIZ=dict(P.QUIZ, quiz_structure="CONFIRMED_4_MCQ_1_MR"))),
    dict(fid="Y-26", title="the 60 percent threshold is treated as confirmed",
         gates=["PASS_THRESHOLD_TREATED_AS_CONFIRMED"],
         patch=lambda: dict(DECISIONS=[
             dict(d, recommendation="Apply the confirmed 60 percent threshold to T04.")
             if d["decision_id"] == "D-02" else d
             for d in copy.deepcopy(P.DECISIONS)])),
    dict(fid="Y-27", title="the not-produced list drops the confirmed-structure entries",
         gates=["CONFIRMED_STRUCTURE_LISTED_AS_NOT_PRODUCED"],
         patch=lambda: dict(QUIZ=dict(P.QUIZ, not_produced=["final stems"]))),
    dict(fid="Y-28", title="the quiz content is upgraded beyond a blueprint",
         gates=["QUIZ_CONTENT_BLUEPRINT_ONLY"],
         patch=lambda: dict(QUIZ=dict(P.QUIZ, quiz_content="FINAL_QUESTIONS"))),

    # ---- safety disclosure ----
    dict(fid="Y-29", title="a legal obligation is moved onto an optional reveal screen",
         gates=["LEGAL_ROWS_NOT_GATED_BEHIND_OPTIONAL_REVEAL", "LEGAL_ROWS_CARRIED_BY_A_CONTRACT"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-02")["source_rows"]
                  .append("T04-ROW-066"))),
    dict(fid="Y-30", title="the compliance screen stops showing obligations in the base state",
         gates=["LEGAL_OBLIGATIONS_VISIBLE_IN_BASE_STATE"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-04").update(
             base_state="Screen title only; obligations revealed on click."))),
    dict(fid="Y-31", title="hidden reveal content is reclassified as mandatory",
         gates=["REVEAL_HIDDEN_CONTENT_CLASSIFIED"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-03").update(
             hidden_content_classification="MANDATORY"))),
    dict(fid="Y-32", title="a reveal contract drops its justification",
         gates=["REVEAL_JUSTIFICATION_PRESENT"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-02").update(
             hidden_content_justification=""))),

    # ---- cast propagation ----
    dict(fid="Y-33", title="the cast decision is widened to PL06",
         gates=["CAST_DECISION_SCOPE", "CAST_NOT_PROPAGATED_PL06_WIDE"],
         patch=lambda: dict(DECISIONS=[
             dict(d, scope="PL06_WIDE") if d["decision_id"] == "D-03" else d
             for d in copy.deepcopy(P.DECISIONS)])),
    dict(fid="Y-34", title="the B02 cast pair is proposed for T04",
         gates=["B02_CAST_NAMES_PROPOSED"],
         patch=lambda: dict(DECISIONS=[
             dict(d, recommendation="Use Alya and Encik Rahman as the PL06 cast.")
             if d["decision_id"] == "D-03" else d
             for d in copy.deepcopy(P.DECISIONS)])),

    # ---- decisions and PENDING_HUMAN ----
    dict(fid="Y-35", title="a decision is dropped from the pack",
         gates=["DECISION_COUNT", "DECISION_IDS"],
         patch=lambda: dict(DECISIONS=copy.deepcopy(P.DECISIONS)[:-1])),
    dict(fid="Y-36", title="PENDING_HUMAN silently picks a treatment",
         gates=["PENDING_HUMAN_SILENTLY_CHOSE_A_TREATMENT"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-06").update(
             base_state="Rumusan screen with five statements, then a 5-item quiz."))),
    dict(fid="Y-37", title="PENDING_HUMAN is given more than three options",
         gates=["PENDING_HUMAN_OPTION_COUNT"],
         patch=_c(lambda c: _find(c, "contract_id", "T04-CT-06")["options"].append(
             dict(option="D", label="extra", grounding="none", tradeoff="none")))),

    # ---- portability template ----
    dict(fid="Y-38", title="portability hours are populated without a run",
         gates=["PORTABILITY_FABRICATED_MEASUREMENTS"],
         patch=lambda: dict(PORTABILITY_TEMPLATE=dict(
             P.PORTABILITY_TEMPLATE,
             rows=[dict(r, value="2h30m") if r["metric"] == "total working time" else r
                   for r in copy.deepcopy(P.PORTABILITY_TEMPLATE["rows"])]))),
    dict(fid="Y-39", title="a portability score is calculated before any measurement",
         gates=["PORTABILITY_SCORE_NOT_CALCULATED", "PORTABILITY_STATUS"],
         patch=lambda: dict(PORTABILITY_TEMPLATE=dict(
             P.PORTABILITY_TEMPLATE, score="82%", status="MEASURED"))),
]


def run_fixture(f):
    patch = f["patch"]()
    saved = {k: getattr(P, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(P, k, v)
        return {r["gate_id"]: r["ok"] for r in QA.run()}
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(P, k, v)


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
