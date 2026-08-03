# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-B1.

    SUITE_ID = T04_STORYBOARD_QA_v1
    python3 docs/pl06/t04/tools/t04_storyboard_mutations_v1.py

Some fixtures patch the model in memory. Others REBUILD THE DECK from a mutated model and
leave the corrupted PPTX on disk for the suite to re-read, because gates that re-open the
package cannot be exercised any other way. The real deck is rebuilt from the clean model in
the `finally`, and `post_run_restored` compares its text back to the baseline.
"""
import copy
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import t04_storyboard_model_v1 as M    # noqa: E402
import t04_storyboard_build_v1 as B    # noqa: E402
import t04_authority_data_v1 as A      # noqa: E402
import t04_supplementary_evidence_v1 as S  # noqa: E402
import t04_storyboard_qa_v1 as QA      # noqa: E402

TARGETS = {"M": M, "B": B, "A": A, "S": S, "QA": QA}


def _screens(fn):
    """Patch the screen projection function, so every consumer sees the mutation."""
    base = M.screens

    def apply():
        def patched():
            rows = copy.deepcopy(base())
            fn(rows)
            return rows
        return dict(screens=patched)
    return apply


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


FIXTURES = [
    # ================= sequence =================
    dict(fid="S-01", title="a screen is dropped and the deck falls to 21",
         gates=["EXACTLY_TWENTY_TWO_SCREENS", "SCREEN_IDS_ARE_CONTIGUOUS",
                "SCREENS_AGREE_WITH_THE_FROZEN_SEQUENCE"],
         patch=_screens(lambda r: r.pop(13))),
    dict(fid="S-02", title="a 23rd screen is invented",
         gates=["EXACTLY_TWENTY_TWO_SCREENS", "TITLES_MATCH_THE_FIXED_LIST"],
         patch=_screens(lambda r: r.append(dict(r[-1], screen_id="T04-S23",
                                                title_ms="Tambahan")))),
    dict(fid="S-03", title="the closing screen reverts to Tamat Bahagian",
         gates=["THE_FINAL_SCREEN_IS_TAMAT_TOPIK", "TITLES_MATCH_THE_FIXED_LIST",
                "NO_LEARNER_FACING_BAHAGIAN"],
         patch=_screens(lambda r: r[-1].update(title_ms="Tamat Bahagian"))),
    dict(fid="S-04", title="a screen title drifts from the fixed list",
         gates=["TITLES_MATCH_THE_FIXED_LIST", "TITLES_AGREE_WITH_THE_FROZEN_SEQUENCE"],
         patch=_screens(lambda r: r[13].update(title_ms="Racun — pengurusan"))),
    dict(fid="S-05", title="the learner display unit reintroduces a Bahagian",
         gates=["LEARNER_DISPLAY_UNIT_IS_TOPIK_4"],
         patch=_screens(lambda r: [x.update(learner_display_unit="Topik 4 Bahagian 1")
                                   for x in r])),
    dict(fid="S-06", title="the internal traceability ID is lost",
         gates=["INTERNAL_UNIT_ID_IS_TRACEABLE"],
         patch=_screens(lambda r: [x.update(internal_unit_id="T04") for x in r])),
    dict(fid="S-07", title="a Bahagian label is written into learner content",
         gates=["NO_LEARNER_FACING_BAHAGIAN"],
         patch=_screens(lambda r: r[0]["content_blocks"].append(
             dict(row_id=None, text="Bahagian 1", provenance="CAIR_STRUCTURAL",
                  content_type="UI", module_page=None, list_level=0)))),
    dict(fid="S-08", title="the case-sensitivity of the ban is removed",
         target="M", gates=["THE_BAN_IS_CASE_SENSITIVE"],
         patch=lambda: dict(BANNED_TERM_IS_CASE_SENSITIVE=False)),
    dict(fid="S-09", title="the common-noun exception loses its documentation",
         target="M", gates=["THE_COMMON_NOUN_EXCEPTION_IS_DOCUMENTED"],
         patch=lambda: dict(BANNED_TERM_COMMON_NOUN_NOTE="")),
    dict(fid="S-10", title="pagination drops a block instead of spilling it",
         target="M", gates=["PAGINATION_LOSES_NOTHING", "SLIDE_COUNT_IS_THE_SUM_OF_PAGES"],
         patch=lambda: dict(paginate=lambda blocks: [blocks[:M.MAX_LINES_PER_PAGE]])),
    dict(fid="S-11", title="the page budget is raised past what the renderer can hold",
         target="M", gates=["EVERY_PAGE_FITS"],
         patch=lambda: dict(MAX_LINES_PER_PAGE=200)),

    # ================= text provenance =================
    dict(fid="P-01", title="a block loses its provenance label",
         gates=["EVERY_BLOCK_CARRIES_A_PROVENANCE"],
         patch=_screens(lambda r: r[3]["content_blocks"][0].update(provenance="UNKNOWN"))),
    dict(fid="P-02", title="CAIR teaching content is introduced under its own category",
         gates=["NO_CAIR_INSTRUCTIONAL_CONTENT_CATEGORY", "EVERY_BLOCK_CARRIES_A_PROVENANCE"],
         patch=_screens(lambda r: r[4]["content_blocks"].append(
             dict(row_id=None,
                  text="Penyiraman perlu dilakukan dua kali sehari untuk hasil terbaik.",
                  provenance=M.FORBIDDEN_PROVENANCE, content_type="BODY",
                  module_page=None, list_level=0)))),
    dict(fid="P-03", title="a source block loses its row binding",
         gates=["SOURCE_BLOCKS_CARRY_A_ROW_ID"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S05")["content_blocks"][0]
                        .update(row_id=None))),
    dict(fid="P-04", title="an authority block loses its reference",
         gates=["AUTHORITY_BLOCKS_CARRY_A_REFERENCE"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S02")["content_blocks"][0]
                        .update(authority_ref=None))),
    dict(fid="P-05", title="a quiz option is relabelled as module text",
         gates=["ASSESSMENT_OPTIONS_ARE_NOT_CLAIMED_AS_MODULE_TEXT",
                "SOURCE_BLOCKS_CARRY_A_ROW_ID"],
         patch=_screens(lambda r: [b.update(provenance="SOURCE_CONTROLLED")
                                   for b in _find(r, "screen_id", "T04-S21")["content_blocks"]
                                   if b["content_type"] == "QUIZ_OPTION"])),
    dict(fid="P-06", title="teaching prose is smuggled in as structural furniture",
         gates=["STRUCTURAL_FURNITURE_STAYS_SHORT"],
         patch=_screens(lambda r: r[5]["content_blocks"].append(
             dict(row_id=None,
                  text="Sistem pengairan automatik sentiasa lebih baik daripada penyiraman "
                       "manual dalam semua keadaan tapak.",
                  provenance="CAIR_STRUCTURAL", content_type="UI",
                  module_page=None, list_level=0)))),
    dict(fid="P-07", title="a provenance category falls out of use entirely",
         gates=["ALL_FIVE_PROVENANCES_ARE_USED"],
         patch=_screens(lambda r: [b.update(provenance="CAIR_STRUCTURAL")
                                   for x in r for b in x["content_blocks"]
                                   if b["provenance"] == "AUTHORITY_SELECTED"])),

    # ================= source and authority traceability =================
    dict(fid="T-01", title="a source string is paraphrased away from the module",
         gates=["SOURCE_STRINGS_ARE_VERBATIM"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S05")["content_blocks"][0]
                        .update(text="Penyiraman tanaman"))),
    dict(fid="T-02", title="a screen cites a row that does not exist",
         gates=["EVERY_TRACED_ROW_EXISTS"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S05")["content_blocks"][0]
                        .update(row_id="T04-ROW-999"))),
    dict(fid="T-03", title="a screen's row set drifts from the frozen sequence",
         gates=["SCREEN_ROW_SETS_MATCH_THE_FROZEN_SEQUENCE"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S06")
                        .update(source_row_ids=["T04-ROW-008"]))),
    dict(fid="T-04", title="a second screen quietly becomes authority-replaced",
         gates=["THE_AUTHORITY_REPLACED_SCREENS_ARE_NAMED",
                "EVERY_CONTENT_SCREEN_HAS_SOURCE_STRINGS"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S13")
                        .update(content_blocks=[
                            dict(row_id=None, text="Teks pengganti", provenance="CAIR_STRUCTURAL",
                                 content_type="UI", module_page=None, list_level=0)]))),
    dict(fid="T-05", title="a screen loses its authority binding",
         gates=["EVERY_SCREEN_HAS_AN_AUTHORITY_BINDING"],
         patch=_screens(lambda r: r[6].update(decision_ids=[]))),
    dict(fid="T-06", title="a screen cites a decision that does not exist",
         gates=["EVERY_BOUND_DECISION_EXISTS"],
         patch=_screens(lambda r: r[7].update(decision_ids=["T04-DEC-ZZ"]))),
    dict(fid="T-07", title="a learner screen is bound to the non-authority X01 record",
         gates=["NO_SCREEN_IS_BOUND_TO_A_NON_AUTHORITY_RECORD",
                "EVERY_BINDING_CARRIES_AN_EVIDENCE_GRADE"],
         patch=_screens(lambda r: r[8].update(decision_ids=["T04-DEC-X01"]))),

    # ================= the renumbering translation =================
    dict(fid="R-01", title="the B0.8 to B0.9 screen translation is switched off",
         target="M",
         gates=["THE_RENUMBERING_TRANSLATION_WAS_APPLIED",
                "HARD_LANDSCAPE_GROUP_LANDS_ON_HARD_LANDSCAPE_SCREENS",
                "RACUN_COMPLIANCE_GROUP_LANDS_ON_THE_RACUN_COMPLIANCE_SCREENS"],
         patch=lambda: dict(to_current=lambda x: x)),
    dict(fid="R-02", title="the translation map is emptied",
         target="M",
         gates=["THE_RENUMBERING_TRANSLATION_WAS_APPLIED"],
         patch=lambda: dict(_RENUMBER={})),

    # ================= interaction =================
    dict(fid="I-01", title="a static screen gains reveal states",
         gates=["STATIC_SCREENS_HAVE_ONE_STATE", "STATES_AGREE_WITH_THE_FROZEN_SEQUENCE"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S17")
                        .update(interaction_states=["BASE", "ST-01", "ALL_VIEWED"]))),
    dict(fid="I-02", title="a reveal screen is flattened to one state",
         gates=["REVEAL_SCREENS_HAVE_MORE_THAN_ONE_STATE",
                "STATES_AGREE_WITH_THE_FROZEN_SEQUENCE"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S06")
                        .update(interaction_states=["BASE only"]))),
    dict(fid="I-03", title="the HSE reveal risk loses its owner",
         target="M",
         gates=["THE_HSE_REVEAL_RISK_IS_CARRIED_WITH_ITS_OWNER"],
         patch=lambda: dict(interaction_model=lambda: [
             dict(x, risk_owner=None) for x in _im_base()])),
    dict(fid="I-04", title="a reveal screen stops declaring its residual risk",
         target="M",
         gates=["EVERY_REVEAL_SCREEN_STATES_ITS_RESIDUAL_RISK"],
         patch=lambda: dict(interaction_model=lambda: [
             dict(x, residual_risk=None) for x in _im_base()])),

    # ================= visual scope =================
    dict(fid="V-01", title="artwork is claimed to exist",
         gates=["NO_ARTWORK_WAS_PRODUCED", "EVERY_VISUAL_SLOT_IS_A_PLACEHOLDER"],
         patch=_screens(lambda r: [x["visual"].update(artwork_status="PRODUCED",
                                                      placeholder_only=False)
                                   for x in r if x["visual"]["asset_group_ids"]])),
    dict(fid="V-02", title="the inserted screen is credited with a unique asset",
         gates=["S14_REUSES_AG06_AND_ADDS_NOTHING"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S14")["visual"]
                        .update(adds_unique_assets=1, reuses_existing_group=False))),
    dict(fid="V-03", title="a do-not-reuse restriction is dropped from its screen",
         gates=["DO_NOT_REUSE_RESTRICTIONS_APPEAR_ON_THEIR_SCREENS",
                "EVERY_DO_NOT_REUSE_ITEM_LANDS_SOMEWHERE"],
         patch=_screens(lambda r: _find(r, "screen_id", "T04-S16")["visual"]
                        .update(do_not_reuse_obligations=[]))),
    dict(fid="V-04", title="the 41-asset total drifts",
         target="M",
         gates=["FORTY_ONE_PROPOSED_UNIQUE_ASSETS"],
         patch=lambda: dict(visual_totals=lambda: dict(_vt_base(),
                                                       proposed_unique_assets=42))),
    dict(fid="V-05", title="the 46 obligations drift",
         target="M", gates=["FORTY_SIX_VISUAL_OBLIGATIONS"],
         patch=lambda: dict(visual_totals=lambda: dict(_vt_base(),
                                                       visual_obligations=41))),
    dict(fid="V-06", title="a ninth asset group appears",
         target="M", gates=["EIGHT_ASSET_GROUPS"],
         patch=lambda: dict(visual_totals=lambda: dict(_vt_base(), asset_groups=9))),

    # ================= assessment =================
    dict(fid="Q-01", title="the pass mark is changed",
         target="A", gates=["PASS_MARK_IS_SIXTY_PERCENT"],
         patch=lambda: dict(FINAL_QUIZ=dict(A.FINAL_QUIZ, pass_mark="70 peratus"))),
    dict(fid="Q-02", title="Q5 reverts to letter labels",
         target="A",
         gates=["Q5_USES_CHECKBOXES_NOT_LETTERS", "FOUR_MCQ_AND_ONE_MULTIPLE_RESPONSE"],
         patch=lambda: dict(_QUIZ=[dict(q, qtype="MCQ") if q["qid"] == "T04-QZ-Q5" else q
                                   for q in A._QUIZ])),
    dict(fid="Q-03", title="the rejected Set A returns to the quiz",
         target="A",
         gates=["THE_REJECTED_SET_A_IS_NOT_IN_THE_DECK",
                "THE_FINAL_SET_B_DISTRACTORS_ARE_IN_THE_DECK"],
         rebuild=True,
         patch=lambda: dict(_QUIZ=[
             dict(q, options=q["options"][:4] + [x["text_ms"] for x in S.SET_A_REJECTED])
             if q["qid"] == "T04-QZ-Q5" else q for q in A._QUIZ])),
    dict(fid="Q-04", title="the superseded CAIR draft returns to the quiz",
         target="A",
         gates=["THE_SUPERSEDED_CAIR_DRAFT_IS_NOT_IN_THE_DECK"],
         rebuild=True,
         patch=lambda: dict(_QUIZ=[
             dict(q, options=q["options"][:4]
                  + [x["superseded_b09_text"] for x in S.SET_B_FROZEN])
             if q["qid"] == "T04-QZ-Q5" else q for q in A._QUIZ])),
    dict(fid="Q-05", title="the answer keys are declared Bariah-approved",
         target="M",
         gates=["ANSWER_KEYS_ARE_NOT_BARIAH_DIRECT_APPROVED"],
         patch=lambda: dict(assessment_status=lambda: dict(
             _as_base(), answer_key_is_bariah_direct_approved=True,
             answer_key_status="BARIAH_APPROVED"))),
    dict(fid="Q-06", title="the Q5 distractors are declared Bariah-authored",
         target="M",
         gates=["Q5_DISTRACTORS_ARE_NOT_BARIAH_DIRECT_AUTHORED"],
         patch=lambda: dict(assessment_status=lambda: dict(
             _as_base(), q5_distractors_are_bariah_direct_authored=True,
             q5_distractor_provenance="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"))),
    dict(fid="Q-07", title="the Q5 stem is claimed as authority-authored",
         target="A",
         gates=["EXACTLY_ONE_STEM_IS_NOT_AUTHORITY_AUTHORED"],
         patch=lambda: dict(_QUIZ=[
             dict(q, stem_provenance="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT")
             if q["qid"] == "T04-QZ-Q5" else q for q in A._QUIZ])),
    dict(fid="Q-08", title="a runtime assessment packet is declared generated",
         target="M",
         gates=["NO_RUNTIME_ASSESSMENT_PACKET_WAS_GENERATED"],
         patch=lambda: dict(assessment_status=lambda: dict(
             _as_base(), runtime_packet_generated=True))),
    dict(fid="Q-09", title="a quiz item loses its source bindings",
         target="A", gates=["EVERY_ITEM_KEEPS_ITS_SOURCE_BINDINGS"],
         patch=lambda: dict(_QUIZ=[dict(q, source_rows=[]) if q["qid"] == "T04-QZ-Q3" else q
                                   for q in A._QUIZ])),
    dict(fid="Q-10", title="E-07 is reported as still open in the assessment register",
         target="S", gates=["E07_IS_REFLECTED_IN_THE_ASSESSMENT_REGISTER"],
         patch=lambda: dict(E07_CLOSURE=dict(S.E07_CLOSURE, status="OPEN"))),

    # ================= evidence =================
    dict(fid="E-01", title="the supplementary screenshot is reported as verified",
         target="M", gates=["SUPPLEMENTARY_EVIDENCE_IS_STILL_UNVERIFIED"],
         patch=lambda: dict(evidence_status=lambda: dict(
             _ev_base(),
             supplementary_authority_evidence=dict(
                 _ev_base()["supplementary_authority_evidence"],
                 verified=True, sha256="b" * 64)))),
    dict(fid="E-02", title="the release decision is overstated to full approval",
         target="S", gates=["THE_RELEASE_DECISION_IS_CARRIED_FORWARD"],
         patch=lambda: dict(RELEASE_DECISION=dict(
             S.RELEASE_DECISION,
             verdict_tokens=["T04_CONTENT_APPROVED_READY_FOR_STORYBOARD_BUILD"]))),
    dict(fid="E-03", title="an open item is dropped on the way into B1",
         target="A", gates=["OPEN_ITEMS_ARE_CARRIED_FORWARD"],
         patch=lambda: dict(OPEN_AFTER_THIS_STAGE=A.OPEN_AFTER_THIS_STAGE[:2])),
    dict(fid="E-04", title="the source risk token is changed to a blocking one",
         target="A", gates=["THE_SOURCE_RISK_TOKEN_IS_UNCHANGED"],
         patch=lambda: dict(SOURCE_RISK_TOKEN="SOURCE_BLOCKING")),
    dict(fid="E-05", title="the primary evidence hash drifts",
         target="A", gates=["PRIMARY_EVIDENCE_IS_VERIFIED",
                            "THE_AUTHORITY_DOCX_IS_STILL_BYTE_IDENTICAL"],
         patch=lambda: dict(PRIMARY_DOCX_SHA256="c" * 64, PRIMARY_DOCX_BYTES=1)),

    # ================= deck structure, rebuilt on disk =================
    dict(fid="D-01", title="a screen title never reaches the deck",
         gates=["EVERY_TITLE_APPEARS_IN_THE_DECK", "TITLES_MATCH_THE_FIXED_LIST"],
         rebuild=True,
         patch=_screens(lambda r: r[9].update(title_ms="Tajuk hilang"))),
    dict(fid="D-02", title="a repository path is printed onto a slide",
         target="B", gates=["NO_REPOSITORY_PATH_LEAKS_INTO_THE_DECK"],
         rebuild=True,
         patch=lambda: dict(LEGEND="Dijana dari docs/pl06/t04/tools")),
    dict(fid="D-03", title="a SHA-256 is printed onto a slide",
         target="B", gates=["NO_SHA256_LEAKS_INTO_THE_DECK"],
         rebuild=True,
         patch=lambda: dict(LEGEND=A.PRIMARY_DOCX_SHA256)),
    dict(fid="D-04", title="the do-not-reuse warning is removed from the deck",
         target="B", gates=["THE_DO_NOT_REUSE_WARNING_IS_IN_THE_DECK"],
         rebuild=True,
         patch=lambda: dict(_screen_slide=_slide_without("TIDAK BOLEH DIKONGSI"))),
    dict(fid="D-05", title="the no-artwork notice is removed from the deck",
         target="B", gates=["THE_NO_ARTWORK_NOTICE_IS_IN_THE_DECK"],
         rebuild=True,
         patch=lambda: dict(_screen_slide=_slide_without("ASET BELUM DIHASILKAN"))),
    dict(fid="D-06", title="the deck loses a slide relative to the model",
         target="B", gates=["SLIDE_COUNT_MATCHES_THE_MODEL"],
         rebuild=True, patch=lambda: dict(build_pptx=_build_short)),

    # ================= render honesty =================
    dict(fid="N-01", title="a native PowerPoint render is claimed",
         target="B", gates=["NATIVE_RENDER_IS_DECLARED_NOT_CHECKED"],
         patch=lambda: dict(RENDER_STATUS="RENDERED_IN_MICROSOFT_POWERPOINT")),
    dict(fid="N-02", title="PowerPoint equivalence is claimed",
         target="B", gates=["NO_POWERPOINT_EQUIVALENCE_IS_CLAIMED",
                            "NATIVE_RENDER_IS_DECLARED_NOT_CHECKED"],
         patch=lambda: dict(RENDER_STATUS="MICROSOFT_POWERPOINT_EQUIVALENCE")),
    dict(fid="N-03", title="the preview's limitation note is removed",
         target="B", gates=["THE_RENDER_LIMITATION_IS_STATED"],
         patch=lambda: dict(RENDER_NOTE="The preview shows the deck.")),

    # ================= production guards =================
    dict(fid="G-01", title="MMD production is recorded as started",
         target="M", gates=["NO_MMD_PRODUCTION"],
         patch=lambda: dict(MMD_PRODUCTION_STARTED=1)),
    dict(fid="G-02", title="React work is recorded as started",
         target="M", gates=["NO_REACT_WORK"], patch=lambda: dict(REACT_STARTED=1)),
    dict(fid="G-03", title="SCORM work is recorded as started",
         target="M", gates=["NO_SCORM_WORK"], patch=lambda: dict(SCORM_STARTED=1)),
    dict(fid="G-04", title="an LMS upload is recorded",
         target="M", gates=["NO_LMS_UPLOAD"], patch=lambda: dict(LMS_UPLOAD_STARTED=1)),
    dict(fid="G-05", title="another PL is touched",
         target="M", gates=["NO_OTHER_PL_TOUCHED"], patch=lambda: dict(OTHER_PL_TOUCHED=1)),
    dict(fid="G-06", title="the production generator is recorded as touched",
         target="M", gates=["PRODUCTION_GENERATOR_UNTOUCHED"],
         patch=lambda: dict(PRODUCTION_GENERATOR_TOUCHED=1)),
    dict(fid="G-07", title="an artifact outside T04 is declared",
         target="M", gates=["ONLY_T04_ARTIFACTS_WERE_EMITTED",
                            "EVERY_DECLARED_ARTIFACT_EXISTS"],
         patch=lambda: dict(NEW_ARTIFACTS=M.NEW_ARTIFACTS + ["T03_SOMETHING_v1.json"])),
    dict(fid="G-08", title="a verdict outside the allowed set is adopted",
         target="M", gates=["VERDICT_IS_FROM_THE_ALLOWED_SET"],
         patch=lambda: dict(VERDICT="T04_PRODUCTION_APPROVED")),

    # ================= reporting =================
    dict(fid="A-01", title="the suite loses its identity",
         target="QA", gates=["SUITE_ID_DECLARED"], patch=lambda: dict(SUITE_ID="")),
    dict(fid="A-02", title="the suite adopts the prior suite identity",
         target="QA", gates=["SUITE_ID_DECLARED", "SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE"],
         patch=lambda: dict(SUITE_ID=QA.PRIOR_SUITE_ID)),
    dict(fid="A-03", title="the NOT_CHECKED list is emptied",
         target="QA", gates=["NOT_CHECKED_IS_PUBLISHED"], patch=lambda: dict(NOT_CHECKED=[])),
]

_IM_BASE = _VT_BASE = _AS_BASE = _EV_BASE = None


def _im_base():
    return _IM_BASE


def _vt_base():
    return _VT_BASE


def _as_base():
    return _AS_BASE


def _ev_base():
    return _EV_BASE


def _slide_without(marker):
    """Wrap the slide builder so one specific string is never emitted."""
    base = B._screen_slide

    def patched(prs, sl):
        orig = B._p

        def filtered(tf, text, *a, **k):
            if marker in str(text):
                return None
            return orig(tf, text, *a, **k)
        B._p = filtered
        try:
            return base(prs, sl)
        finally:
            B._p = orig
    return patched


def _build_short():
    """Build the deck one slide short of the model."""
    from pptx import Presentation
    prs = Presentation()
    prs.slide_width = B.SLIDE_W
    prs.slide_height = B.SLIDE_H
    B._title_slide(prs)
    for sl in M.slides()[:-1]:
        B._screen_slide(prs, sl)
    os.makedirs(M.PPTX_DIR, exist_ok=True)
    path = os.path.join(M.PPTX_DIR, M.PPTX_NAME)
    prs.save(path)
    return path


def _run_suite():
    return {r["gate_id"]: r["ok"] for r in QA.run()}


def _deck_digest():
    p = os.path.join(M.PPTX_DIR, M.PPTX_NAME)
    if not os.path.exists(p):
        return None
    # Compare TEXT, not bytes: python-pptx writes non-deterministic package metadata.
    return hashlib.sha256(
        json.dumps(QA._pptx_slide_texts(), ensure_ascii=False).encode()).hexdigest()


def run_fixture(f):
    tgt = TARGETS[f.get("target", "M")]
    patch = f["patch"]()
    saved = {k: getattr(tgt, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(tgt, k, v)
        if f.get("rebuild"):
            B.build_pptx()
        return _run_suite()
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(tgt, k, v)
        if f.get("rebuild"):
            B.build_pptx()


def main():
    global _IM_BASE, _VT_BASE, _AS_BASE, _EV_BASE
    _IM_BASE = M.interaction_model()
    _VT_BASE = M.visual_totals()
    _AS_BASE = M.assessment_status()
    _EV_BASE = M.evidence_status()
    before = _deck_digest()
    good = _run_suite()
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], title=f["title"],
                        target=f.get("target", "M"),
                        rebuilds_deck=bool(f.get("rebuild")),
                        designated_gates=f["gates"], detected=det, fired=fired,
                        note=res.get("__MSG__")))
    after = _deck_digest()
    return dict(suite_id=QA.SUITE_ID,
                baseline_pass=sum(1 for v in good.values() if v),
                baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out),
                detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                deck_rebuilt_clean=(before == after),
                rebuild_fixtures=len([r for r in out if r["rebuilds_deck"]]),
                by_target={t: sum(1 for r in out if r["target"] == t)
                           for t in sorted({r["target"] for r in out})},
                fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if (r["missed"] or r["baseline_false_failures"]
                   or not r["deck_rebuilt_clean"]) else 0)
