# -*- coding: utf-8 -*-
"""Negative mutations for the Stage 4.2F-B0.6 gates.

Each fixture patches the controlled data source in memory, runs the suite, and requires the
designated gate to fire. Every patch is reverted in a `finally`; nothing on disk is touched.

A fixture proves the gate is SENSITIVE to a defect. It proves nothing about correctness.

    python3 docs/pl06/t04/tools/t04_rulings_mutations_v1.py
"""
import copy, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_rulings_data_v1 as D
import t04_rulings_qa_v1 as QA


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


def _vo(fn):
    def apply():
        v = copy.deepcopy(D.VISUAL_OBLIGATIONS)
        fn(v)
        return dict(VISUAL_OBLIGATIONS=v)
    return apply


def _dec(fn):
    def apply():
        d = copy.deepcopy(D.DECISIONS)
        fn(d)
        return dict(DECISIONS=d)
    return apply


def _quiz(fn):
    def apply():
        q = copy.deepcopy(D.QUIZ_V2)
        fn(q)
        return dict(QUIZ_V2=q)
    return apply


def _first(group):
    return next(v for v in D.VISUAL_OBLIGATIONS if v["population_group"] == group)


SIRAM_FIRST = next(v for v in D.VISUAL_OBLIGATIONS
                   if v["population_group"] == "B_OPERATION_DESCENDANT"
                   and v["parent_topic"] == "Siram")

FIXTURES = [
    # ---- visual obligation population ----
    dict(fid="Z-01", title="one of the six process-node visual obligations is removed",
         gates=["VISUAL_OBLIGATIONS_TOTAL", "ALL_SIX_PROCESS_NODES_HAVE_SEPARATE_OBLIGATIONS",
                "NO_SEVENTH_PROCESS_STEP", "PROCESS_NODE_ORDER_PRESERVED"],
         patch=_vo(lambda v: v.remove(_find(v, "visual_obligation_id", "T04-VO-004")))),
    dict(fid="Z-02", title="a Siram descendant obligation is removed",
         gates=["VISUAL_OBLIGATIONS_TOTAL", "ALL_SIRAM_DESCENDANTS_REPRESENTED"],
         patch=_vo(lambda v: v.remove(_find(v, "visual_obligation_id",
                                            SIRAM_FIRST["visual_obligation_id"])))),
    dict(fid="Z-03", title="a Baja descendant obligation is removed",
         gates=["VISUAL_OBLIGATIONS_TOTAL", "ALL_BAJA_DESCENDANTS_REPRESENTED"],
         patch=_vo(lambda v: v.remove(_find(v, "visual_obligation_id", "T04-VO-019")))),
    dict(fid="Z-04", title="a Racun descendant obligation is removed",
         gates=["VISUAL_OBLIGATIONS_TOTAL", "ALL_RACUN_DESCENDANTS_REPRESENTED"],
         patch=_vo(lambda v: v.remove(_find(v, "visual_obligation_id", "T04-VO-035")))),
    dict(fid="Z-05", title="one of the four named Landskap Kejur groups is removed",
         gates=["VISUAL_OBLIGATIONS_TOTAL", "ALL_FOUR_NAMED_KEJUR_SUBTOPICS_REPRESENTED"],
         patch=_vo(lambda v: v.remove(_find(v, "visual_obligation_id", "T04-VO-045")))),
    dict(fid="Z-06", title="an enumerated descendant is replaced by the vague phrase "
                           "'their subtopics'",
         gates=["NO_VAGUE_SUBTOPIC_PHRASE_IN_CONTROLLED_RECORDS"],
         patch=_vo(lambda v: _find(v, "visual_obligation_id", "T04-VO-013").update(
             learner_facing_subject="Siram and their subtopics, shown together"))),

    # ---- authority ----
    dict(fid="Z-07", title="a visual SUBJECT is promoted to Bariah-direct authority",
         gates=["SUBJECT_AUTHORITY_NEVER_BARIAH_DIRECT"],
         patch=_vo(lambda v: _find(v, "visual_obligation_id", "T04-VO-010").update(
             subject_authority="BARIAH_DIRECT_SCREENSHOT"))),

    # ---- invention ----
    dict(fid="Z-08", title="a non-existent source photograph is claimed to exist",
         gates=["MISSING_SOURCE_IMAGE_NOT_REPORTED_AS_EXISTING",
                "SOURCE_ASSET_ID_ONLY_WHERE_AN_ASSET_EXISTS",
                "SMARTART_REFERENCE_ONLY_ON_PROCESS_NODES"],
         patch=_vo(lambda v: _find(v, "visual_obligation_id", "T04-VO-019").update(
             existing_source_asset_available="YES_RASTER_IMAGE_IN_SOURCE",
             source_asset_id="T04-IMG-01"))),
    dict(fid="Z-09", title="a required new asset is no longer labelled NEW_MMD_ASSET_REQUIRED",
         gates=["NEW_ASSETS_LABELLED_NEW_MMD_ASSET_REQUIRED"],
         patch=_vo(lambda v: _find(v, "visual_obligation_id", "T04-VO-021").update(
             production_requirement="REUSE_EXISTING_ASSET"))),

    # ---- assessment ----
    dict(fid="Z-10", title="the 60 percent threshold is marked confirmed",
         gates=["PASS_THRESHOLD_UNRESOLVED", "SIXTY_PERCENT_NOT_CONFIRMED"],
         patch=_quiz(lambda q: q.update(
             pass_threshold="60_PERCENT",
             threshold_note="The 60 percent pass mark is confirmed for the Kursus."))),
    dict(fid="Z-11", title="quiz composition is changed to five MCQ",
         gates=["QUIZ_COMPOSITION_EXACTLY_4_MCQ_1_MR"],
         patch=_quiz(lambda q: (q["slots"][4].update(item_type="MCQ"),
                                q.update(mcq_count=5, mr_count=0)))),
    dict(fid="Z-12", title="quiz scope is reduced to T04 only",
         gates=["QUIZ_SCOPE_ALL_PLS_IN_KURSUS"],
         patch=_quiz(lambda q: q.update(scope="THIS_UNIT_ONLY"))),
    dict(fid="Z-13", title="a final question stem is written into a slot",
         gates=["NO_FINAL_QUIZ_STEM"],
         patch=_quiz(lambda q: q["slots"][0].update(
             source_learning_point="Apakah tiga operasi penyelenggaraan landskap lembut?"))),
    dict(fid="Z-14", title="a final answer key is written into a slot",
         gates=["NO_FINAL_ANSWER_KEY"],
         patch=_quiz(lambda q: q["slots"][2].update(
             correct_answer_evidence="Answer key: kawalan kultur."))),

    # ---- authorship and decision status ----
    dict(fid="Z-15", title="the Rumusan is marked Bariah-approved",
         gates=["RUMUSAN_REMAINS_CAIR_ASSISTED_DRAFT", "FORBIDDEN_AUTHORSHIP_LABELS"],
         patch=lambda: dict(RUMUSAN_V2=dict(
             D.RUMUSAN_V2, content_status="BARIAH_APPROVED",
             approval_status="BARIAH_APPROVED"))),
    dict(fid="Z-16", title="the legal base/reveal split is marked confirmed",
         gates=["LEGAL_SPLIT_REMAINS_PENDING_CONFIRMATION"],
         patch=lambda: dict(LEGAL_CLARIFICATION=dict(
             D.LEGAL_CLARIFICATION, status="CONFIRMED_BARIAH_DIRECT",
             recommendation_status="APPROVED", applied_to_a_contract=True))),
    dict(fid="Z-17", title="the cast decision is marked approved",
         gates=["D03_UNRESOLVED", "CAST_REMAINS_UNRESOLVED", "D03_CARRIES_NO_RULING"],
         patch=_dec(lambda d: _find(d, "decision_id", "D-03").update(
             status="CONFIRMED_BARIAH_DIRECT", ruling="HILMI_NARRATOR_LED"))),
    dict(fid="Z-18", title="the SmartArt MMD treatment is marked approved",
         gates=["D05_THREE_ITEMS_STILL_UNCONFIRMED"],
         patch=lambda: dict(D05_FOLLOWUP=dict(
             D.D05_FOLLOWUP,
             confirmations_required=[dict(c, status="CONFIRMED")
                                     for c in D.D05_FOLLOWUP["confirmations_required"]]))),
    dict(fid="Z-19", title="the old blanket TEXT_AND_DIAGRAM_LED ruling is presented as final",
         gates=["D01_NEW_RULING", "TEXT_AND_DIAGRAM_LED_NOT_PRESENTED_AS_FINAL"],
         patch=_dec(lambda d: _find(d, "decision_id", "D-01").update(
             ruling="TEXT_AND_DIAGRAM_LED"))),

    # ---- screen count and propagation ----
    dict(fid="Z-20", title="a final screen count is claimed",
         gates=["FINAL_SCREEN_COUNT_NOT_CLAIMED"],
         patch=lambda: dict(FINAL_SCREEN_COUNT="18",
                            MAPPING_IMPACT=dict(D.MAPPING_IMPACT, final_screen_count="18"))),
    dict(fid="Z-21", title="a B02 execution family is propagated onto a T04 screen",
         gates=["NO_B02_FAMILY_TOKEN_IN_CONTROLLED_RECORDS"],
         patch=lambda: dict(MAPPING_V2=[
             dict(m, possible_screen_expansion="reuse the B02 FAMILY_S selection screen")
             if m["screen_candidate_id"] == "T04-SC-02" else m
             for m in D.MAPPING_V2])),
    dict(fid="Z-22", title="B02 factual content is copied into the Rumusan",
         gates=["NO_B02_FACT_IN_RUMUSAN"],
         patch=lambda: dict(RUMUSAN_V2=dict(
             D.RUMUSAN_V2,
             statements=[dict(s, draft_text=s["draft_text"] + ", termasuk Water Feature "
                                                              "dan BBQ Pit")
                         if s["statement_id"] == "T04-RUM2-03" else s
                         for s in D.RUMUSAN_V2["statements"]]))),

    # ---- evidence ----
    dict(fid="Z-23", title="an evidence SHA-256 no longer matches the frozen bytes",
         gates=["EVIDENCE_FROZEN_BYTE_IDENTICALLY"],
         patch=lambda: dict(EVIDENCE=[dict(e, sha256="0" * 64) if e["evidence_id"] == "T04-EV-01"
                                      else e for e in D.EVIDENCE])),
    dict(fid="Z-24", title="an evidence item is downgraded from BARIAH_DIRECT_SCREENSHOT",
         gates=["EVIDENCE_CLASS"],
         patch=lambda: dict(EVIDENCE=[dict(e, evidence_class="FIRDAUS_ATTESTED_BARIAH_CALL")
                                      if e["evidence_id"] == "T04-EV-02" else e
                                      for e in D.EVIDENCE])),
    dict(fid="Z-25", title="a coverage point is silently discarded from the blueprint",
         gates=["ALL_SIX_COVERAGE_POINTS_CARRIED", "CONSOLIDATION_DECLARED_NOT_SILENT"],
         patch=_quiz(lambda q: q["slots"][4].update(from_blueprint=["T04-QB-04"]))),
    dict(fid="Z-26", title="a mandatory legal row is moved behind an optional reveal",
         gates=["NO_MANDATORY_ROW_PROPOSED_FOR_REVEAL_ONLY",
                "SUPPLEMENTARY_CANDIDATES_ARE_DECLARED"],
         patch=lambda: dict(LEGAL_GROUPS=[
             dict(g, rows=[dict(r, proposed_optional_reveal_treatment="hidden until clicked")
                           if r["source_row_id"] == "T04-ROW-066" else r
                           for r in g["rows"]])
             if g["group_id"] == "LG-1" else g for g in D.LEGAL_GROUPS])),
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
