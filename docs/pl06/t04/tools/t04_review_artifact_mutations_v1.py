# -*- coding: utf-8 -*-
"""Negative mutations for SUITE_ID = T04_BARIAH_REVIEW_ARTIFACT_QA_v1.

Three patch targets, because the defects this stage guards against live in three places:

    M   the governed review model
    R   the renderer / block list — where a DOCX-only sentence would be injected
    QA  the reporting harness itself

Artifact-level fixtures (a sentence added only to the DOCX, an option changed only in the
DOCX) rewrite the file on disk inside the fixture and restore the byte-identical original in
`finally`. Everything else is patched in memory.

    python3 docs/pl06/t04/tools/t04_review_artifact_mutations_v1.py
"""
import copy, json, os, re, shutil, sys, tempfile, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_review_model_v1 as M
import t04_review_render_v1 as R
import t04_review_semantic_v1 as SEM
import t04_review_artifact_qa_v1 as QA

TARGETS = {"M": M, "R": R, "QA": QA, "SEM": SEM}


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


def _model(fn):
    """Patch a deep copy of MODEL."""
    def apply():
        m = copy.deepcopy(M.MODEL)
        fn(m)
        return dict(MODEL=m)
    return apply


def _blocks(fn):
    """Patch a deep copy of the render block list."""
    def apply():
        b = copy.deepcopy(R.BLOCKS)
        fn(b)
        return dict(BLOCKS=b)
    return apply


# ---- artifact-level file mutations ------------------------------------------------------
def _docx_patch(fn):
    """Rewrite word/document.xml on disk, then restore the original bytes."""
    def apply():
        return dict(__docx__=fn)
    return apply


def _md_patch(fn):
    def apply():
        return dict(__md__=fn)
    return apply


def _inject_docx_sentence(xml):
    extra = ('<w:p><w:r><w:t xml:space="preserve">Nota tambahan yang hanya wujud dalam '
             'DOCX ini.</w:t></w:r></w:p>')
    return xml.replace("</w:body>", extra + "</w:body>")


def _alter_docx_quiz_option(xml):
    return xml.replace("Sistem Titis (Drip Irrigation System)",
                       "Sistem Titis (Drip) untuk kawasan rumput luas")


def _inject_docx_repo_path(xml):
    extra = ('<w:p><w:r><w:t xml:space="preserve">Dijana daripada '
             'docs/pl06/t04/tools/t04_review_render_v1.py</w:t></w:r></w:p>')
    return xml.replace("</w:body>", extra + "</w:body>")


def _inject_docx_english_section_f(xml):
    return xml.replace("Keputusan keseluruhan", "Overall Decision — Approve")


def _drop_docx_verdict(xml):
    return xml.replace("LULUS TANPA PINDAAN", "")


def _drop_docx_signature(xml):
    return xml.replace("Tandatangan / pengesahan bertulis", "Catatan")


def _remove_md_item(text):
    return "\n".join(ln for ln in text.splitlines()
                     if "T04-RUM2-03" not in ln)


FIXTURES = [
    # ---- artifact-level: content in one representation only ----
    dict(fid="X-01", target="DOCX", title="a sentence is added only to the DOCX",
         gates=["NO_DOCX_ONLY_SUBSTANTIVE_CONTENT", "ALL_THREE_SEMANTIC_DIGESTS_AGREE"],
         patch=_docx_patch(_inject_docx_sentence)),
    dict(fid="X-02", target="MD", title="a reviewable item is removed from the Markdown",
         gates=["MODEL_FULLY_PRESENT_IN_MARKDOWN", "ALL_THREE_SEMANTIC_DIGESTS_AGREE",
                "ITEM_IDS_AGREE"],
         patch=_md_patch(_remove_md_item)),
    dict(fid="X-03", target="DOCX", title="one quiz option is altered only in the DOCX",
         gates=["QUIZ_OPTIONS_AGREE", "QUIZ_OPTIONS_MATCH_THE_MODEL",
                "ALL_THREE_SEMANTIC_DIGESTS_AGREE"],
         patch=_docx_patch(_alter_docx_quiz_option)),
    dict(fid="X-04", target="DOCX", title="a repository path is injected into the DOCX",
         gates=["NO_TECHNICAL_LEAK_IN_DOCX", "NO_DOCX_ONLY_SUBSTANTIVE_CONTENT"],
         patch=_docx_patch(_inject_docx_repo_path)),
    dict(fid="X-05", target="DOCX", title="English instructions appear in Section F",
         gates=["NO_ENGLISH_DECISION_WORDS_IN_DOCX", "NO_DOCX_ONLY_SUBSTANTIVE_CONTENT"],
         patch=_docx_patch(_inject_docx_english_section_f)),
    dict(fid="X-06", target="DOCX", title="the final reviewer verdict is removed",
         gates=["FINAL_VERDICT_BLOCK_PRESENT", "VERDICT_OPTIONS_AGREE",
                "EXACTLY_ONE_VERDICT_VOCABULARY"],
         patch=_docx_patch(_drop_docx_verdict)),
    dict(fid="X-07", target="DOCX", title="the signature / written-confirmation field is removed",
         gates=["SIGNATURE_FIELD_PRESENT", "MODEL_FULLY_PRESENT_IN_DOCX"],
         patch=_docx_patch(_drop_docx_signature)),

    # ---- visual reporting ----
    dict(fid="X-08", target="M", title="41 proposed assets is changed to 46",
         gates=["OBLIGATIONS_NOT_REPRESENTED_AS_ASSETS", "ARITHMETIC_RECONCILES",
                "SEMANTIC_TOTALS_DERIVED_LIVE"],
         patch=_model(lambda m: m["visual_asset_grouping"]["totals"].update(
             proposed_unique_assets=46))),
    dict(fid="X-09", target="M", title="the five composite-covered cases are no longer disclosed",
         gates=["COMPOSITE_COUNT_DISCLOSED", "COMPOSITE_ITEMS_LISTED_IN_DOCX"],
         patch=_model(lambda m: m["visual_asset_grouping"].update(composite_items=[]))),
    dict(fid="X-10", target="M",
         title="the three no-separate-asset cases are no longer disclosed",
         gates=["NO_SEPARATE_ASSET_COUNT_DISCLOSED", "NO_SEPARATE_ASSET_ITEMS_LISTED_IN_DOCX"],
         patch=_model(lambda m: m["visual_asset_grouping"].update(
             no_separate_asset_items=[]))),
    dict(fid="X-11", target="M", title="AG-08 is classified as a Bariah visual ruling",
         gates=["AG08_IS_A_CAIR_SCENARIO_PROPOSAL", "AG08_NOT_LABELLED_A_BARIAH_RULING"],
         patch=_model(lambda m: (
             m["visual_asset_grouping"]["ag08_scenario"].update(
                 origin="KEPERLUAN_VISUAL_BARIAH"),
             _find(m["visual_asset_grouping"]["groups"], "item_id", "AG-08").update(
                 origin_label="KEPERLUAN_VISUAL_BARIAH")))),
    dict(fid="X-12", target="M",
         title="AG-08 is folded into the 46-obligation population",
         gates=["AG08_EXCLUDED_FROM_THE_46"],
         patch=_model(lambda m: m["visual_asset_grouping"]["ag08_scenario"].update(
             part_of_46_obligations=True))),
    dict(fid="X-13", target="M",
         title="the AG-01 seventh asset is claimed as directly named by Bariah",
         gates=["AG01_SEVENTH_ASSET_IS_A_CAIR_PROPOSAL"],
         patch=_model(lambda m: m["visual_asset_grouping"]["ag01_seventh_asset"].update(
             seventh_asset_origin="KEPERLUAN_VISUAL_BARIAH"))),
    dict(fid="X-14", target="M", title="a do-not-reuse constraint is hidden",
         gates=["DO_NOT_REUSE_OBLIGATION_COUNT_DISCLOSED", "DO_NOT_REUSE_ITEMS_SHOWN_IN_DOCX"],
         patch=_model(lambda m: m["visual_asset_grouping"].update(
             do_not_reuse_items=m["visual_asset_grouping"]["do_not_reuse_items"][:2]))),
    dict(fid="X-15", target="M",
         title="the reuse question is asked without naming the known constraints",
         gates=["REUSE_QUESTION_RESPECTS_CONSTRAINTS"],
         patch=_model(lambda m: m["visual_asset_grouping"].update(
             reuse_question_ms="Adakah visual tertentu boleh digunakan semula?"))),
    dict(fid="X-16", target="M", title="proposed assets are presented as approved",
         gates=["PROPOSED_ASSETS_LABELLED_PROPOSED"],
         patch=_model(lambda m: m["visual_asset_grouping"]["totals"].update(
             status="APPROVED"))),

    # ---- MERGE ----
    dict(fid="X-17", target="M", title="a MERGE is recorded with no target ID",
         gates=["NO_ORPHAN_MERGE_DECISION"],
         patch=_model(lambda m: _find(m["screen_sequence"]["screens"], "item_id",
                                      "T04-S06")["merge"].update(
             merge_source_id="T04-S06", merge_target_id=None))),
    dict(fid="X-18", target="M", title="an item is merged with itself",
         gates=["MERGE_SOURCE_AND_TARGET_DIFFER"],
         patch=_model(lambda m: _find(m["screen_sequence"]["screens"], "item_id",
                                      "T04-S07")["merge"].update(
             merge_source_id="T04-S07", merge_target_id="T04-S07"))),
    dict(fid="X-19", target="M", title="a MERGE points at an ID that does not exist",
         gates=["MERGE_TARGET_RESOLVES"],
         patch=_model(lambda m: _find(m["screen_sequence"]["screens"], "item_id",
                                      "T04-S09")["merge"].update(
             merge_source_id="T04-S09", merge_target_id="T04-S99"))),
    dict(fid="X-20", target="M", title="MERGE is offered on a quiz item",
         gates=["CONTENT_ITEMS_DO_NOT_OFFER_MERGE"],
         patch=_model(lambda m: _find(m["quiz"]["items"], "item_id", "Q3").update(
             allowed_decisions=["ACCEPT", "EDIT", "REMOVE", "MERGE"]))),
    dict(fid="X-21", target="M", title="MERGE and REUSE are collapsed into one vocabulary",
         gates=["MERGE_IS_NOT_REUSE"],
         patch=_model(lambda m: m["decision_vocabulary"].update(
             reuse=["ACCEPT", "EDIT", "REMOVE", "MERGE"], structural=["ACCEPT", "EDIT",
                                                                     "REMOVE", "MERGE"]))),
    dict(fid="X-22", target="M", title="a structural item loses its MERGE option",
         gates=["STRUCTURAL_ITEMS_OFFER_MERGE"],
         patch=_model(lambda m: _find(m["visual_asset_grouping"]["groups"], "item_id",
                                      "AG-03").update(
             allowed_decisions=["ACCEPT", "EDIT", "REMOVE"]))),

    # ---- content boundaries ----
    dict(fid="X-23", target="M", title="the Slide 2 content boundary is removed",
         gates=["SLIDE_2_BOUNDARIES_IN_MODEL", "SLIDE_2_BOUNDARIES_IN_DOCX"],
         patch=_model(lambda m: m["slide_2_dialogue"]["boundaries"].update(
             rules=[], rules_ms=[], level="UNRESTRICTED"))),
    dict(fid="X-24", target="M",
         title="a licensed-operator duty is placed in Encik Rahman's dialogue",
         gates=["NO_STATUTORY_DUTY_IN_DIALOGUE"],
         patch=_model(lambda m: _find(m["slide_2_dialogue"]["lines"], "item_id",
                                      "T04-DLG-04").update(
             display_text="Ingat, semburan racun mesti dibuat oleh pengendali berlesen."))),
    dict(fid="X-25", target="M", title="the cast is marked final",
         gates=["CAST_NOT_FINAL"],
         patch=_model(lambda m: m["slide_2_dialogue"].update(
             cast_status="FINAL_CAST_CONFIRMED"))),
    dict(fid="X-26", target="M", title="the Rumusan 04 risk note is removed",
         gates=["RUMUSAN_04_RISK_FLAGGED", "RUMUSAN_04_SECOND_FLAG"],
         patch=_model(lambda m: _find(m["rumusan"]["points"], "item_id",
                                      "T04-RUM2-04").update(
             risk_flag=None, risk_flag_secondary=None))),
    dict(fid="X-27", target="M", title="DEP-RUM04-Q5 is removed",
         gates=["DEP_RUM04_Q5_EXISTS", "DEP_TRIGGER_AND_EFFECT", "Q5_NOT_AUTOMATICALLY_INVALIDATED"],
         patch=_model(lambda m: m.update(cross_item_dependencies=[]))),
    dict(fid="X-28", target="M",
         title="removing Rumusan 04 is declared to delete Q5 automatically",
         gates=["Q5_NOT_AUTOMATICALLY_INVALIDATED"],
         patch=_model(lambda m: m["cross_item_dependencies"][0].update(
             automatic_invalidation=True))),
    dict(fid="X-29", target="M", title="the answer key is marked final",
         gates=["ANSWER_KEY_NOT_FINAL"],
         patch=_model(lambda m: m["quiz"].update(answer_key_status="FINAL_ANSWER_KEY",
                                                 answer_key_approval="APPROVED"))),
    dict(fid="X-30", target="M", title="quiz composition is changed",
         gates=["QUIZ_COMPOSITION_UNCHANGED"],
         patch=_model(lambda m: _find(m["quiz"]["items"], "item_id", "Q5").update(
             question_type="MCQ"))),
    dict(fid="X-31", target="M", title="the pass threshold is changed",
         gates=["PASS_THRESHOLD_60"],
         patch=_model(lambda m: m["quiz"].update(pass_threshold="50_PERCENT"))),
    dict(fid="X-32", target="M", title="source evidence is removed from one quiz item",
         gates=["EVERY_QUIZ_ITEM_KEEPS_SOURCE_EVIDENCE_INTERNALLY"],
         patch=_model(lambda m: _find(m["quiz"]["items"], "item_id", "Q2").update(
             internal_answer_evidence=""))),
    dict(fid="X-33", target="M", title="the quiz is declared source-unsupported",
         gates=["QUIZ_SOURCE_STATUS_IS_SUPPORTED_NOT_UNSUPPORTED"],
         patch=_model(lambda m: m["quiz"].update(
             source_evidence_status="SOURCE_UNSUPPORTED"))),
    dict(fid="X-34", target="M",
         title="the custody caveat is pushed into the Bariah-facing document",
         gates=["CUSTODY_CAVEAT_KEPT_OUT_OF_THE_BARIAH_DOCUMENT",
                "MODEL_FULLY_PRESENT_IN_DOCX"],
         patch=_model(lambda m: m["quiz"].update(
             answer_key_ms="Cadangan jawapan sahaja. "
                           "ORIGINAL_DOCX_ROUND_TRIP_NOT_REPROVEN"))),
    dict(fid="X-35", target="M", title="the Q5 distractor review record is removed",
         gates=["Q5_DISTRACTOR_REVIEW_RECORDED", "Q5_OPTION_MAPPING_RECORDED",
                "Q5_CORRECT_ANSWER_COUNT_PRESERVED"],
         patch=_model(lambda m: m["quiz"].update(distractor_review=None))),
    dict(fid="X-36", target="M", title="a reviewable item is marked approved",
         gates=["EVERY_REVIEWABLE_ITEM_IS_A_DRAFT"],
         patch=_model(lambda m: _find(m["rumusan"]["points"], "item_id",
                                      "T04-RUM2-01").update(
             approval_status="BARIAH_APPROVED"))),

    # ---- artifact authority ----
    dict(fid="X-37", target="M", title="the manual v1 DOCX is marked ready for delivery",
         gates=["MANUAL_DOCX_IS_NON_GOVERNED_REFERENCE"],
         patch=_model(lambda m: m["external_manual_docx"].update(
             status="GOVERNED", delivery_status="READY_FOR_BARIAH_DELIVERY"))),
    dict(fid="X-38", target="M", title="the manual v1 DOCX is treated as an authority source",
         gates=["MANUAL_DOCX_NOT_USED_AS_AUTHORITY"],
         patch=_model(lambda m: m["external_manual_docx"].update(used_as_authority=True))),
    dict(fid="X-39", target="M", title="the Markdown is declared the human approval artifact",
         gates=["DOCX_IS_HUMAN_APPROVAL_ARTIFACT"],
         patch=_model(lambda m: m["artifact_hierarchy"].update(
             HUMAN_APPROVAL_ARTIFACT="docs/pl06/t04/T04_BARIAH_CONTENT_REVIEW_PACK_v2.md"))),

    # ---- reporting harness ----
    dict(fid="X-40", target="QA", title="native rendering is claimed to have passed",
         gates=["NATIVE_RENDER_STATUS_DECLARED", "NATIVE_RENDER_NOT_CLAIMED_PASSED",
                "DELIVERY_STATUS_MATCHES_RENDER_STATUS"],
         patch=lambda: dict(NATIVE_RENDER_STATUS="RENDERED_AND_INSPECTED")),
    dict(fid="X-41", target="QA",
         title="delivery is upgraded to Bariah while the renderer is unavailable",
         gates=["DELIVERY_STATUS_MATCHES_RENDER_STATUS"],
         patch=lambda: dict(DELIVERY_STATUS="READY_FOR_BARIAH_DELIVERY")),
    dict(fid="X-42", target="QA", title="the NOT_CHECKED list is removed",
         gates=["NOT_CHECKED_PUBLISHED"],
         patch=lambda: dict(NOT_CHECKED=[])),
    dict(fid="X-43", target="QA", title="the suite identity is lost",
         gates=["SUITE_ID_PRESENT", "SUITE_NOT_MERGED_WITH_CONTENT_SUITE"],
         patch=lambda: dict(SUITE_ID="T04_CONTENT_QA_v1")),
    dict(fid="X-44", target="M",
         title="a total is edited after the cached constant is computed",
         gates=["SEMANTIC_TOTALS_DERIVED_LIVE", "ASSET_GROUP_COUNTS_AGREE"],
         patch=_model(lambda m: m["visual_asset_grouping"]["totals"].update(
             asset_groups=9))),
    dict(fid="X-45", target="M", title="a gate population empties out unexpectedly",
         gates=["NO_UNDECLARED_EMPTY_POPULATION"],
         patch=_model(lambda m: m.update(sections=[]))),
]


def _restore_docx():
    R.render_docx()


def _restore_md():
    R.render_md()


def run_fixture(f):
    tgt_name = f.get("target", "M")
    patch = f["patch"]()
    if "__docx__" in patch:
        z = zipfile.ZipFile(SEM.DOCX_PATH)
        parts = {n: z.read(n) for n in z.namelist()}
        z.close()
        parts["word/document.xml"] = patch["__docx__"](
            parts["word/document.xml"].decode("utf-8")).encode("utf-8")
        try:
            with zipfile.ZipFile(SEM.DOCX_PATH, "w", zipfile.ZIP_DEFLATED) as out:
                for n, d in parts.items():
                    out.writestr(n, d)
            return {r["gate_id"]: r["ok"] for r in QA.run()}
        except Exception as exc:
            return {"__EXCEPTION__": False, "__MSG__": str(exc)}
        finally:
            _restore_docx()
    if "__md__" in patch:
        with open(SEM.MD_PATH, encoding="utf-8") as fh:
            original = fh.read()
        try:
            with open(SEM.MD_PATH, "w", encoding="utf-8") as fh:
                fh.write(patch["__md__"](original))
            return {r["gate_id"]: r["ok"] for r in QA.run()}
        except Exception as exc:
            return {"__EXCEPTION__": False, "__MSG__": str(exc)}
        finally:
            _restore_md()
    tgt = TARGETS[tgt_name]
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
                        target=f.get("target", "M"), designated_gates=f["gates"],
                        detected=det, fired=fired))
    after = {r["gate_id"]: r["ok"] for r in QA.run()}
    return dict(suite_id=QA.SUITE_ID,
                baseline_pass=sum(1 for v in good.values() if v), baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                post_run_restored=sorted(g for g, ok in after.items() if not ok) == [],
                fixture_count=len(out), detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                skipped=[], fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if r["missed"] or r["baseline_false_failures"]
             or not r["post_run_restored"] else 0)
