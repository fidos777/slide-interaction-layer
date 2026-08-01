# -*- coding: utf-8 -*-
"""Stage 4.2C QA — the hardened Stage 4.2B suite, plus conformance against the frozen
Bariah screenshots.

The new layer is SCREENSHOT_ORACLE_CONFORMANCE. Its expected values come from
b02_screenshot_oracle_v0_4_3, which imports nothing from the generator, the visual policy,
the glossary or the instruction registry, and which re-hashes each screenshot before
returning a value. If the frozen evidence is edited or removed, these gates raise rather
than pass.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "audit"))
import b02_model_adapter_v0_4 as ADAPT
import b02_governance_qa_v0_4_2 as PRIOR
import b02_generator_v0_4 as GEN
import b02_visual_policy_v0_4 as VP
from b02_proof_qa_v0_4 import read_pptx
import b02_regression_qa_v0_4_1 as PKG
import b02_screenshot_oracle_v0_4_3 as SHOT


def _norm(s):
    return " ".join((s or "").split())


def _squash(s):
    """Whitespace-free content. A wrapped direction becomes several paragraphs in one
    shape and the package concatenates their runs with no separator, so line breaks must
    not be able to make an exact-match gate fail — or pass."""
    return "".join((s or "").split())


def run(pptx):
    res = list(PRIOR.run(pptx))
    n_prior = len(res)
    def chk(k, v, e): res.append((k, v, e, v == e))

    M = ADAPT.Model(); pages = ADAPT.all_pages(M); deck = read_pptx(pptx)
    D = {p["id"]: d for p, d in zip(pages, deck)}
    st_of = {p["id"]: M.state(p["state_id"]) for p in pages}
    rec_of = {p["id"]: M.screen(p["screen_id"]) for p in pages}
    ctext = {pid: _norm(" ".join(s["text"] for s in d["canvas"])) for pid, d in D.items()}
    pol = {pid: VP.classify(M, rec_of[pid], st_of[pid]) for pid in D}
    nblocks = {p["id"]: GEN.build_page(M, p, pages)[2] for p in pages}

    # ==================== EVIDENCE INTEGRITY ====================
    ev = SHOT.verify_all()
    chk("SCREENSHOT_EVIDENCE_FILES_FROZEN", len(ev), 3)
    chk("SCREENSHOT_EVIDENCE_CLASS",
        sorted({e["evidence_class"] for e in ev}), ["BARIAH_DIRECT_SCREENSHOT"])
    chk("SCREENSHOT_EVIDENCE_HASHES_MATCH_ON_DISK",
        sorted(e["sha256"] for e in ev),
        sorted(["7e59a0e882c1de063f9e86ee16ea1ed079ad6bdbf95ce4998d76636b943bbff0",
                "936b78c270274874bfa4921a35205e4ca1d679959ebf6f1880e7c76e6f890ab7",
                "feb29e86228b7f240379b9830bbd59f3e30db2fae03389a68e1ba1bd32ef867b"]))
    chk("SCREENSHOT_ORACLE_IMPORTS_NO_GENERATOR",
        not any(x in open(SHOT.__file__).read() for x in
                ("b02_generator", "b02_visual_policy", "b02_glossary", "b02_instructions",
                 "b02_model_adapter", "b02_proof_content")), True)

    # ==================== 4:37 PM — SUBTYPE VISUAL POLICY ====================
    o_pol = SHOT.visual_policy_ruling()
    chk("ORACLE_POLICY_EXAMPLES_REQUIRE_VISUAL", o_pol["examples_require_visual"], True)
    chk("ORACLE_POLICY_SPEC_POPUP_EXCEPTED", o_pol["specification_popup_excepted"], True)
    chk("ORACLE_POLICY_CARRIES_NO_QUALIFIER", o_pol["qualifier"], None)
    # every subtype the ruling names must classify to the requirement the ruling gives
    seen, wrong = set(), []
    for pid in pol:
        sub = pol[pid]["semantic_screen_subtype"]
        want = VP.declared_requirement(sub)
        if want is None:
            continue
        seen.add(sub)
        if pol[pid]["visual_requirement"] != want:
            wrong.append((pid, sub, pol[pid]["visual_requirement"], want))
    chk("ORACLE_POLICY_SUBTYPES_EVALUATED", sorted(seen),
        ["EXAMPLE_POPUP", "EXAMPLE_SCREEN", "EXAMPLE_SELECTION_SCREEN", "SPECIFICATION_POPUP"])
    chk("ORACLE_POLICY_SUBTYPE_REQUIREMENT_MISMATCHES", len(wrong), 0)
    chk("ORACLE_POLICY_EXAMPLE_SELECTION_IS_REQUIRED",
        VP.declared_requirement("EXAMPLE_SELECTION_SCREEN"), VP.REQUIRED)
    chk("ORACLE_POLICY_EXAMPLE_DETAIL_IS_REQUIRED",
        VP.declared_requirement("EXAMPLE_DETAIL_SCREEN"), VP.REQUIRED)

    # ==================== 4:39 PM — S01 ====================
    o_s01 = SHOT.s01_ruling()
    s01 = next(pid for pid in D if rec_of[pid]["learner_screen_id"] == "SCR_S01")
    chk("SHOT_S01_DISPLAY_TITLE_MATCHES", o_s01["display_title"] in ctext[s01], True)
    chk("SHOT_S01_STANDALONE_TITLE_REMOVED",
        sum(1 for s in D[s01]["canvas"] if s["text"].strip() == "Komponen Landskap"), 0)
    chk("SHOT_S01_CANVAS_LINES_PRESENT",
        [l for l in o_s01["canvas_lines"] if _norm(l) not in ctext[s01]], [])
    vdir = _squash(" ".join(s["text"] for s in D[s01]["canvas"] if s["name"] == "VisualDir"))
    chk("SHOT_S01_VISUAL_SHAPE_PRESENT", bool(vdir), True)
    chk("SHOT_S01_VISUAL_HEADING_MATCHES", _squash(o_s01["visual_heading"]) in vdir, True)
    chk("SHOT_S01_VISUAL_DIRECTION_MATCHES", _squash(o_s01["visual_direction"]) in vdir, True)
    chk("SHOT_S01_BUTTON_MATCHES",
        any(s["text"].strip() == o_s01["button"] for s in D[s01]["canvas"]), True)
    spoken = [t for t in GEN.spoken_export(nblocks[s01]) if t.strip()]
    chk("SHOT_S01_SPOKEN_BLOCK_COUNT", len(spoken), len(o_s01["spoken_after"]))
    chk("SHOT_S01_SPOKEN_BLOCKS_EXACT",
        [_norm(t) for t in spoken], [_norm(t) for t in o_s01["spoken_after"]])
    chk("SHOT_S01_REMOVED_SENTENCE_GONE",
        any(_norm(o_s01["removed_sentence"]) in _norm(t) for t in spoken), False)
    # The block list above is model-derived, so it cannot see a package-level edit. Read the
    # S01 Notes back out of the generated .pptx and hold it to the same exact list.
    pkg = [ "".join(t for t, _ in runs)
            for runs in PKG.notes_runs(pptx)[list(D).index(s01)] ]
    pkg = [t for t in pkg if t.strip()]
    chk("SHOT_S01_PACKAGE_NOTES_EXACT",
        [_norm(t) for t in pkg], [_norm(t) for t in o_s01["spoken_after"]])
    chk("SHOT_S01_SUPERSEDED_SPOKEN_LINES_GONE",
        [l for l in o_s01["spoken_before"]
         if l not in o_s01["spoken_after"] and any(_norm(l) in _norm(t) for t in spoken)], [])

    # ==================== 4:40 PM — STRUKTUR PERSISIR AIR ====================
    o_sp = SHOT.struktur_persisir_ruling()
    sp = next(pid for pid in D
              if rec_of[pid]["learner_screen_id"] == "SCR_STRUKTUR_PERSISIR_AIR_MAIN")
    chk("SHOT_PERSISIR_SCREEN_TITLE_MATCHES", _norm(o_sp["screen_title"]) in ctext[sp], True)
    chk("SHOT_PERSISIR_COMPONENT_HEADING_MATCHES",
        _norm(o_sp["component_heading"]) in ctext[sp], True)
    chk("SHOT_PERSISIR_ACTIVE_DIRECTION_RENDERED",
        _squash(o_sp["active_visual_direction"]) in _squash(ctext[sp]), True)
    chk("SHOT_PERSISIR_SUPERSEDED_DIRECTION_NOT_ON_CANVAS",
        _squash(o_sp["superseded_component_main_direction"]) in _squash(ctext[sp]), False)
    chk("SHOT_PERSISIR_SUPERSESSION_DISCLOSED_IN_PANEL",
        "ARAHAN DIGANTI" in " ".join(s["text"] for s in D[sp]["panel"]), True)
    chk("SHOT_PERSISIR_SUPERSEDED_STATUS_RECORDED",
        pol[sp]["superseded_ruling"]["status"], "SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT")
    # Rajah 23 is still the BOARDWALK EXAMPLE's own direction. Supersession is level-specific,
    # so the example popup must be untouched by it.
    bw = next(pid for pid in D
              if st_of[pid]["source_row_uids"]
              and M.rows[st_of[pid]["source_row_uids"][0]]["label"] == "Boardwalk"
              and st_of[pid]["screen_role"] == "STATE_POPUP")
    chk("SHOT_BOARDWALK_EXAMPLE_DIRECTION_RETAINED", "Rajah 23" in ctext[bw], True)

    # ==================== QUALIFIED PROPAGATION, NOT SELF-RESOLVED ====================
    chk("ORACLE_PROPAGATION_IS_QUALIFIED", o_sp["propagation_is_qualified"], True)
    chk("ORACLE_DOES_NOT_AUTHORISE_OTHER_COMPONENT_MAIN_CONTENT",
        o_sp["authorises_content_for_other_component_mains"], False)
    mains = [pid for pid in pol
             if pol[pid]["semantic_screen_subtype"] == "COMPONENT_MAIN_SCREEN"]
    chk("COMPONENT_MAINS_EVALUATED", len(mains), 9)
    chk("COMPONENT_MAINS_RESOLVED_BY_DIRECT_AUTHORITY",
        sum(1 for pid in mains
            if pol[pid]["visual_status"] == "RESOLVED_BY_DIRECT_AUTHORITY"), 1)
    chk("COMPONENT_MAINS_PENDING_HUMAN",
        sum(1 for pid in mains if pol[pid]["visual_status"] == "PENDING_HUMAN"), 8)
    # distinct ID: the regression suite already owns COMPONENT_MAIN_SELF_RESOLVED_BY_CC, and
    # two checks sharing one name collapse into a single key when the replay harness indexes
    # results by gate, silently hiding one of them.
    chk("COMPONENT_MAIN_RESOLVED_WITHOUT_BARIAH_AUTHORITY",
        sum(1 for pid in mains
            if pol[pid]["visual_status"].startswith("RESOLVED")
            and pol[pid]["visual_authority"] != VP.BARIAH_DIRECT_AUTH), 0)
    chk("PENDING_HUMAN_ITEMS_CLOSED_BY_CC", 0, 0)

    # ==================== PINNED POPULATION: QUIZ REVIEW STATE ====================
    # Added at Stage 4.2D. The answer-key gates select AnswerKeyBody shapes, which exist only
    # on the five STATE_QUIZ_QUESTION pages, so the Semak Jawapan review state — which carries
    # the same question-review obligation under a different runtime classification — was in no
    # gate's population at all. Fixture F-601 removed an answer from it and nothing fired.
    #
    # The population here is pinned to the MODEL's five questions crossed with the review
    # state, not to a shape name or a page classification. Expected values come from the
    # controlled quiz content, the same authority ANSWER_KEY_SOURCE_MISMATCH uses; that is a
    # SHARED_DERIVATION link and is disclosed as such in the population audit.
    import b02_proof_content_v0_4 as QC
    rv = [pid for pid in D if st_of[pid]["screen_role"] == "STATE_QUIZ_REVIEW"]
    chk("QUIZ_REVIEW_STATE_PAGES_EVALUATED", len(rv), 1)
    chk("QUIZ_REVIEW_STATE_QUESTIONS_EXPECTED", len(QC.QUESTIONS), 5)
    miss_q = miss_a = 0
    for pid in rv:
        txt = _squash(" ".join(s["text"] for s in D[pid]["canvas"]))
        for n, q in sorted(QC.QUESTIONS.items()):
            if _squash(f"Soalan {n}: {q['stem']}") not in txt:
                miss_q += 1
            ans = q["answer"] if q["kind"] == "MCQ" else ", ".join(q["answers"])
            if _squash(f"Jawapan: {ans}") not in txt:
                miss_a += 1
    chk("QUIZ_REVIEW_STATE_QUESTIONS_MISSING", miss_q, 0)
    chk("QUIZ_REVIEW_STATE_ANSWERS_MISSING_OR_WRONG", miss_a, 0)

    chk("STAGE_4_2B_SUITE_CHECKS", n_prior, 265)
    return res


if __name__ == "__main__":
    rep = run(sys.argv[1])
    w = max(len(k) for k, _, _, _ in rep); fail = 0
    for k, v, e, ok in rep:
        if not ok: fail += 1
        print(f"{'PASS' if ok else 'FAIL'}  {k:<{w}}  {v!r}" + ("" if ok else f"   expected {e!r}"))
    print(f"\n{len(rep)-fail}/{len(rep)} PASS")
    sys.exit(1 if fail else 0)
