# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-B0.9.1.

    SUITE_ID = T04_SUPPLEMENTARY_EVIDENCE_QA_v1
    python3 docs/pl06/t04/tools/t04_supplementary_mutations_v1.py

The defect this suite exists to catch is not a red gate. It is a **quietly filled-in field**:
a hash where there is no file, a pixel dimension nobody measured, a supplied-flag flipped
because the conversation showed an image. Fixtures A-01 to A-03 model exactly that.

One fixture writes a real file into the evidence directory and deletes it again, because
"somebody creates a placeholder at the custody path" cannot be modelled in memory.
"""
import copy
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)
import t04_supplementary_evidence_v1 as S   # noqa: E402
import t04_authority_data_v1 as D           # noqa: E402
import t04_predicate_audit_v1 as P          # noqa: E402
import t04_ooxml_v1 as X                    # noqa: E402
import t04_supplementary_qa_v1 as QA        # noqa: E402

TARGETS = {"S": S, "D": D, "P": P, "X": X, "QA": QA}


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


def _fields(fn):
    def apply():
        f = copy.deepcopy(S.CUSTODY_FIELDS)
        fn(f)
        return dict(CUSTODY_FIELDS=f)
    return apply


def _msgs(fn):
    def apply():
        m = copy.deepcopy(S.MESSAGES)
        fn(m)
        return dict(MESSAGES=m)
    return apply


def _read(fn):
    def apply():
        r = copy.deepcopy(S.CONFIRMATION_READINGS)
        fn(r)
        return dict(CONFIRMATION_READINGS=r)
    return apply


def _ts(fn):
    def apply():
        t = copy.deepcopy(S.TIMESTAMP_CLASSES)
        fn(t)
        return dict(TIMESTAMP_CLASSES=t)
    return apply


def _div(fn):
    def apply():
        d = copy.deepcopy(S.Q5_DIVERGENCE)
        fn(d)
        return dict(Q5_DIVERGENCE=d)
    return apply


FIXTURES = [
    # ============ A-01 … A-03: the fields that must never be invented ============
    dict(fid="A-01",
         title="a SHA-256 is invented for a screenshot that has no binary",
         gates=["NO_CUSTODY_FIELD_HOLDS_A_HASH_SHAPED_VALUE",
                "EVERY_CUSTODY_FIELD_IS_MARKED_UNAVAILABLE"],
         patch=_fields(lambda f: _find(f, "field", "sha256").update(
             value=hashlib.sha256(b"there is no file").hexdigest()))),
    dict(fid="A-01b",
         title="a byte size is invented",
         gates=["NO_CUSTODY_FIELD_HOLDS_A_BYTE_COUNT",
                "EVERY_CUSTODY_FIELD_IS_MARKED_UNAVAILABLE"],
         patch=_fields(lambda f: _find(f, "field", "byte_size").update(value="482913"))),
    dict(fid="A-01c",
         title="pixel dimensions are invented",
         gates=["NO_CUSTODY_FIELD_HOLDS_PIXEL_DIMENSIONS",
                "EVERY_CUSTODY_FIELD_IS_MARKED_UNAVAILABLE"],
         patch=_fields(lambda f: _find(f, "field", "pixel_width").update(
             value="1150 × 1416"))),
    dict(fid="A-01d",
         title="format validation is claimed without a file",
         gates=["EVERY_CUSTODY_FIELD_IS_MARKED_UNAVAILABLE"],
         patch=_fields(lambda f: _find(f, "field", "file_format_validation").update(
             value="VALID_PNG"))),
    dict(fid="A-01e",
         title="a MIME type is asserted from the conversation label",
         gates=["EVERY_CUSTODY_FIELD_IS_MARKED_UNAVAILABLE"],
         patch=_fields(lambda f: _find(f, "field", "mime_type").update(value="image/png"))),
    dict(fid="A-02",
         title="the custody outcome is flipped to success while nothing was taken in",
         gates=["CUSTODY_OUTCOME_IS_FAILURE",
                "NOT_SUPPLIED_CANNOT_BE_CLEARED_WITHOUT_CUSTODY"],
         patch=lambda: dict(CUSTODY_OUTCOME="REGISTERED_BYTE_IDENTICAL")),
    dict(fid="A-02b",
         title="a placeholder file is created at the custody path",
         gates=["NO_CUSTODY_FILE_WAS_CREATED",
                "NO_IMAGE_IN_THE_EVIDENCE_DIR_CLAIMS_TO_BE_THIS_SCREENSHOT"],
         disk_create=S.INTENDED_CUSTODY_PATH),
    dict(fid="A-02c",
         title="byte-identity against the source is claimed",
         gates=["EVERY_CUSTODY_FIELD_IS_MARKED_UNAVAILABLE"],
         patch=_fields(lambda f: _find(f, "field", "byte_identity_vs_source").update(
             value="VERIFIED_IDENTICAL"))),
    dict(fid="A-03",
         title="the B0.9 evidence record is flipped to supplied",
         target="D",
         gates=["B09_NOT_SUPPLIED_STATE_STILL_STANDS",
                "NOT_SUPPLIED_CANNOT_BE_CLEARED_WITHOUT_CUSTODY"],
         patch=lambda: dict(EVIDENCE=[
             dict(r, supplied_in_this_run=True) if r["evidence_id"] == "AUTH-EV-02" else r
             for r in D.EVIDENCE])),
    dict(fid="A-03b",
         title="the B0.9 evidence record is given a hash",
         target="D",
         gates=["B09_NOT_SUPPLIED_STATE_STILL_STANDS"],
         patch=lambda: dict(EVIDENCE=[
             dict(r, sha256="a" * 64) if r["evidence_id"] == "AUTH-EV-02" else r
             for r in D.EVIDENCE])),
    dict(fid="A-03c",
         title="a reading claims the blocked AUTHORITY_DIRECT_SCREENSHOT class",
         gates=["NO_READING_CLAIMS_THE_BLOCKED_EVIDENCE_CLASS",
                "EVERY_READING_CARRIES_THE_UNVERIFIED_CUSTODY_STATUS"],
         patch=_read(lambda r: [x.update(
             evidence_class="AUTHORITY_DIRECT_SCREENSHOT",
             actual_status="EXPLICITLY_CONFIRMED") for x in r])),
    dict(fid="A-03d",
         title="a filesystem timestamp is asserted for a file that does not exist",
         gates=["NO_FILESYSTEM_TIMESTAMP_IS_ASSERTED",
                "ONLY_THE_VISIBLE_TIMESTAMPS_ARE_AVAILABLE"],
         patch=_ts(lambda t: _find(t, "timestamp_class", "RUNTIME_FILESYSTEM").update(
             available=True, values=["2026-08-03T07:21:00Z"]))),
    dict(fid="A-03e",
         title="EXIF metadata is asserted",
         gates=["NO_EXIF_IS_ASSERTED", "ONLY_THE_VISIBLE_TIMESTAMPS_ARE_AVAILABLE"],
         patch=_ts(lambda t: _find(t, "timestamp_class", "IMAGE_METADATA_EXIF").update(
             available=True, values=["DateTimeOriginal 2026:08:03 07:21:00"]))),

    # ============ attribution ============
    dict(fid="B-01", title="the Q3 line is re-attributed to Bariah",
         gates=["THE_Q3_LINE_IS_ATTRIBUTED_TO_FIRDAUS", "SENDER_AND_DIRECTION_AGREE"],
         patch=_msgs(lambda m: _find(m, "msg_id", "WA-03").update(sender="BARIAH"))),
    dict(fid="B-02", title="a Bariah message is re-attributed to Firdaus",
         gates=["BARIAH_SENT_EXACTLY_TWO_MESSAGES", "SENDER_AND_DIRECTION_AGREE"],
         patch=_msgs(lambda m: _find(m, "msg_id", "WA-05").update(sender="FIRDAUS"))),
    dict(fid="B-03", title="sender and bubble direction are made to disagree",
         gates=["SENDER_AND_DIRECTION_AGREE"],
         patch=_msgs(lambda m: _find(m, "msg_id", "WA-02").update(direction="OUTGOING"))),
    dict(fid="B-04", title="the correction record is deleted",
         gates=["THE_MISATTRIBUTION_IS_RECORDED_AS_A_CORRECTION"],
         patch=lambda: dict(ATTRIBUTION_CORRECTIONS=[])),
    dict(fid="B-05", title="the correction loses its severity and consequence",
         gates=["THE_CORRECTION_STATES_ITS_SEVERITY_AND_CONSEQUENCE"],
         patch=lambda: dict(ATTRIBUTION_CORRECTIONS=[
             dict(c, severity="", consequence="") for c in S.ATTRIBUTION_CORRECTIONS])),
    dict(fid="B-06", title="the B0.9 record reverts to Bariah authorship",
         target="D",
         gates=["B09_RECORD_CARRIES_THE_CORRECTED_AUTHORSHIP"],
         patch=lambda: dict(CONFIRMATIONS=[
             dict(c, author="BARIAH", is_authority_statement=True)
             if c["confirmation_id"] == "T04-CNF-03" else c for c in D.CONFIRMATIONS])),
    dict(fid="B-07", title="a message loses its verbatim text",
         gates=["EVERY_MESSAGE_CARRIES_VERBATIM_TEXT"],
         patch=_msgs(lambda m: _find(m, "msg_id", "WA-05").update(verbatim_fragments=[]))),
    dict(fid="B-08", title="a Bariah line is silently reworded",
         gates=["THE_THREE_BARIAH_LINES_ARE_PRESENT"],
         patch=_msgs(lambda m: _find(m, "msg_id", "WA-05").update(
             verbatim_fragments=["Yes to everything, Q5 approved"]))),
    dict(fid="B-09", title="OCR is declared the sole evidence",
         gates=["READING_METHOD_IS_VISUAL_NOT_OCR"],
         patch=lambda: dict(READING_METHOD=dict(
             S.READING_METHOD, ocr_used=True, ocr_as_sole_evidence=True))),
    dict(fid="B-10", title="the reading drops its limitations",
         gates=["READING_STATES_ITS_LIMITATIONS"],
         patch=lambda: dict(READING_METHOD=dict(S.READING_METHOD, limitations=[]))),

    # ============ confirmation precision ============
    dict(fid="C-01", title="the bundled acceptance is re-presented as individual wording",
         gates=["CNF01_IS_BUNDLED_ACCEPTANCE_NOT_INDIVIDUAL_WORDING"],
         patch=_read(lambda r: _find(r, "confirmation_id", "T04-CNF-01").update(
             confirmation_mode="EXPLICITLY_WORDED_INDIVIDUAL_DECISION"))),
    dict(fid="C-02", title="the CAIR proposal is re-presented as a Bariah-authored design",
         gates=["CNF02_IS_A_CAIR_PROPOSAL_CONFIRMED"],
         patch=_read(lambda r: _find(r, "confirmation_id", "T04-CNF-02").update(
             confirmation_mode="EXPLICITLY_WORDED_INDIVIDUAL_DECISION"))),
    dict(fid="C-03", title="CNF-01 claims Bariah wrote the corrected sentence",
         gates=["CNF01_DOES_NOT_CLAIM_BARIAH_WROTE_THE_SENTENCE"],
         patch=_read(lambda r: _find(r, "confirmation_id", "T04-CNF-01").update(
             not_claimed="Bariah authored the corrected wording herself."))),
    dict(fid="C-04", title="41 is presented as Bariah's own idea",
         gates=["CNF02_DOES_NOT_CLAIM_41_ORIGINATED_WITH_BARIAH"],
         patch=_read(lambda r: _find(r, "confirmation_id", "T04-CNF-02").update(
             not_claimed="Bariah set the figure of 41 herself."))),
    dict(fid="C-05", title="41 is presented as immutable",
         gates=["FORTY_ONE_IS_RECORDED_AS_MUTABLE"],
         patch=_read(lambda r: _find(r, "confirmation_id", "T04-CNF-02").update(
             mutability="41 is fixed and cannot change."))),
    dict(fid="C-06", title="CNF-03 is widened past the item type",
         gates=["CNF03_CONFIRMS_ITEM_TYPE_ONLY", "CNF03_LISTS_WHAT_IT_DOES_NOT_CONFIRM"],
         patch=_read(lambda r: _find(r, "confirmation_id", "T04-CNF-03").update(
             confirms="the whole Q5 item including options and answer key",
             does_not_confirm=[]))),
    dict(fid="C-07", title="a reading stops naming what blocks its upgrade",
         gates=["EVERY_READING_NAMES_WHAT_BLOCKS_ITS_UPGRADE"],
         patch=_read(lambda r: [x.update(upgrade_blocked_by="") for x in r])),
    dict(fid="C-08", title="the answer keys are relabelled Bariah-direct-approved",
         target="D",
         gates=["ANSWER_KEYS_NOT_RELABELLED_BARIAH_DIRECT_APPROVED"],
         patch=lambda: dict(ANSWER_KEY_STATUS="BARIAH_DIRECT_APPROVED")),
    dict(fid="C-09", title="the Q5 distractors are relabelled Bariah-direct-authored",
         target="D",
         gates=["Q5_DISTRACTORS_NOT_RELABELLED_BARIAH_DIRECT_AUTHORED"],
         patch=lambda: dict(QUIZ_Q5_OPTION_SUBSTITUTIONS=[
             dict(s, authorship="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT")
             for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS])),
    dict(fid="C-10", title="the Q5 distractors are marked approved",
         target="D",
         gates=["Q5_DISTRACTORS_STILL_PENDING_CONFIRMATION"],
         patch=lambda: dict(QUIZ_Q5_OPTION_SUBSTITUTIONS=[
             dict(s, approval_status="BARIAH_APPROVED")
             for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS])),

    # ============ the Q5 divergence ============
    dict(fid="E-01", title="the divergence finding is deleted",
         gates=["Q5_DIVERGENCE_IS_RECORDED", "DIVERGENCE_IS_AT_POSITIONS_FIVE_AND_SIX"],
         patch=_div(lambda d: d.update(finding_id="NONE", severity="NONE",
                                       diverging_positions=[]))),
    dict(fid="E-02", title="the divergence is downgraded to cosmetic",
         gates=["Q5_DIVERGENCE_IS_RECORDED"],
         patch=_div(lambda d: d.update(severity="COSMETIC"))),
    dict(fid="E-03", title="the WhatsApp options are silently adopted into the frozen model",
         target="D",
         gates=["THE_FROZEN_MODEL_WAS_NOT_SILENTLY_OVERWRITTEN",
                "THE_WHATSAPP_OPTIONS_WERE_NOT_ADOPTED"],
         patch=lambda: dict(_QUIZ=[
             dict(q, options=list(S.Q5_DIVERGENCE["options_put_to_authority"]))
             if q["qid"] == "T04-QZ-Q5" else q for q in D._QUIZ])),
    dict(fid="E-04", title="the divergence is declared non-blocking for a scored quiz",
         gates=["DIVERGENCE_DOES_NOT_BLOCK_LAYOUT_BUT_BLOCKS_A_SCORED_QUIZ"],
         patch=_div(lambda d: d.update(blocking_scored_quiz=False))),
    dict(fid="E-05", title="the divergence stops being tracked as an open item",
         gates=["DIVERGENCE_IS_TRACKED_AS_AN_OPEN_ITEM"],
         patch=lambda: dict(NEW_OPEN_ITEMS=[])),

    # ============ AG register ============
    dict(fid="F-01", title="the eight groups are shown as individual acceptances",
         gates=["NO_GROUP_IS_SHOWN_AS_AN_INDIVIDUAL_ACCEPTANCE"],
         patch=lambda: dict(ag_register_audit=lambda: [
             dict(g, represented_as_individual_acceptance=True)
             for g in _base_ag()])),
    dict(fid="F-02", title="the eight groups are shown as unanswered",
         gates=["NO_GROUP_IS_SHOWN_AS_UNANSWERED"],
         patch=lambda: dict(ag_register_audit=lambda: [
             dict(g, represented_as_unanswered=True) for g in _base_ag()])),
    dict(fid="F-03", title="the eight groups become pending-human blockers",
         gates=["NO_GROUP_IS_A_PENDING_HUMAN_BLOCKER"],
         patch=lambda: dict(ag_register_audit=lambda: [
             dict(g, represented_as_pending_human_blocker=True) for g in _base_ag()])),
    dict(fid="F-04", title="the set-level status is upgraded to unconditional acceptance",
         gates=["EVERY_GROUP_IS_SET_LEVEL_ACCEPTED_WITH_CONDITIONS"],
         patch=lambda: dict(AG_SET_STATUS="ACCEPTED")),
    dict(fid="F-05", title="the individual cards are recorded as marked",
         gates=["INDIVIDUAL_CARDS_RECORDED_AS_UNMARKED"],
         patch=lambda: dict(AG_INDIVIDUAL_CARD_STATUS="INDIVIDUALLY_MARKED")),
    dict(fid="F-06", title="the authority basis is upgraded past set-level narrative",
         gates=["AUTHORITY_BASIS_IS_SET_LEVEL_NARRATIVE"],
         patch=lambda: dict(AG_AUTHORITY_BASIS="BARIAH_DIRECT_PER_GROUP_TICK")),
    dict(fid="F-07", title="a distinction layer is collapsed",
         gates=["FOUR_DISTINCTION_LAYERS_HELD_APART"],
         patch=lambda: dict(AG_DISTINCTION_LAYERS=S.AG_DISTINCTION_LAYERS[:3])),
    dict(fid="F-08", title="the no-reuse basis is claimed as per-item ticking",
         gates=["NO_REUSE_EVIDENCE_PRECISION_IS_DERIVED_NOT_TICKED",
                "PER_ITEM_TICKING_IS_EXPLICITLY_NOT_CLAIMED"],
         patch=lambda: dict(
             NO_REUSE_EVIDENCE_PRECISION="BARIAH_TICKED_EACH_ITEM",
             NO_REUSE_NOT_CLAIMED="Bariah ticked a basis field on each item.")),
    dict(fid="F-09", title="a no-reuse decision is dropped",
         gates=["THREE_NO_REUSE_DECISIONS_STAY_CLOSED"],
         patch=lambda: dict(NO_REUSE_CLOSED=S.NO_REUSE_CLOSED[:2])),
    dict(fid="F-10", title="the no-reuse basis is narrowed to one lens",
         gates=["NO_REUSE_BASIS_IS_BOTH_LENSES"],
         patch=lambda: dict(NO_REUSE_DECISION_BASIS="PRODUCTION_ONLY")),
    dict(fid="F-11", title="the forbidden-representation list is emptied",
         gates=["THREE_FORBIDDEN_REPRESENTATIONS_DECLARED"],
         patch=lambda: dict(AG_FORBIDDEN_REPRESENTATIONS=[])),
    dict(fid="F-12", title="S14 is credited with a new unique asset",
         target="D",
         gates=["S14_STILL_ADDS_ZERO_UNIQUE_ASSETS", "FINAL_UNIQUE_ASSET_SCOPE_REMAINS_41"],
         patch=lambda: dict(FINAL_VISUAL_SCOPE=dict(
             D.FINAL_VISUAL_SCOPE, accepted_production_scope=42,
             new_screen_asset_impact=dict(
                 D.FINAL_VISUAL_SCOPE["new_screen_asset_impact"], new_unique_assets=1)))),

    # ============ predicate audit ============
    dict(fid="G-01", title="a closed population loses a named member",
         target="P",
         gates=["PREDICATE_AUDIT_HAS_NO_FAILING_POPULATION",
                "NO_UNEXPECTED_POPULATION_ADDITIONS"],
         patch=lambda: dict(CLOSED_POPULATIONS=[
             dict(p, expected=p["expected"][:-1]) if p["population_id"] == "POP-01" else p
             for p in P.CLOSED_POPULATIONS])),
    dict(fid="G-02", title="a closed population gains a member that is not there",
         target="P",
         gates=["PREDICATE_AUDIT_HAS_NO_FAILING_POPULATION",
                "NO_UNEXPECTED_POPULATION_REMOVALS"],
         patch=lambda: dict(CLOSED_POPULATIONS=[
             dict(p, expected=p["expected"] + ["T04-DEC-ZZ"])
             if p["population_id"] == "POP-03" else p for p in P.CLOSED_POPULATIONS])),
    dict(fid="G-03", title="the C-05 site loses its guard",
         target="P",
         gates=["THE_C05_SITE_IS_STILL_GUARDED", "EIGHTEEN_CLOSED_POPULATIONS_AUDITED"],
         patch=lambda: dict(CLOSED_POPULATIONS=[
             p for p in P.CLOSED_POPULATIONS if p["origin_fixture"] != "C-05"])),
    dict(fid="G-04", title="a population stops naming its members",
         target="P",
         gates=["EVERY_CLOSED_POPULATION_NAMES_ITS_MEMBERS",
                "PREDICATE_AUDIT_HAS_NO_FAILING_POPULATION"],
         patch=lambda: dict(CLOSED_POPULATIONS=[
             dict(p, expected=[]) if p["population_id"] == "POP-05" else p
             for p in P.CLOSED_POPULATIONS])),
    dict(fid="G-05", title="an exclusion loses its documented reason",
         target="P",
         gates=["EVERY_EXCLUSION_IS_DOCUMENTED_WITH_A_REASON"],
         patch=lambda: dict(EXCLUDED_POPULATIONS=[
             dict(x, why="", delta_guard="") for x in P.EXCLUDED_POPULATIONS])),
    dict(fid="G-06", title="the audit is narrowed back to the single C-05 site",
         target="P",
         gates=["THE_C05_RULE_REACHES_BEYOND_ITS_ORIGINAL_SITE",
                "EIGHTEEN_CLOSED_POPULATIONS_AUDITED"],
         patch=lambda: dict(CLOSED_POPULATIONS=[
             p for p in P.CLOSED_POPULATIONS if p["origin_fixture"] == "C-05"])),

    # ============ XML identity ============
    dict(fid="H-01", title="the insideH confusion case is deleted",
         target="X",
         gates=["INSIDEH_IS_NOT_INS", "SUBSTRING_MATCHING_WOULD_HAVE_BEEN_WRONG"],
         patch=lambda: dict(PROOF_CASES=[
             c for c in X.PROOF_CASES if c["case_id"] != "XML-01"])),
    dict(fid="H-02", title="the tcPr confusion case is deleted",
         target="X",
         gates=["TCPR_IS_NOT_T", "SUBSTRING_MATCHING_WOULD_HAVE_BEEN_WRONG"],
         patch=lambda: dict(PROOF_CASES=[
             c for c in X.PROOF_CASES if c["case_id"] != "XML-03"])),
    dict(fid="H-03", title="the positive control is removed so zero-for-everything passes",
         target="X",
         gates=["A_POSITIVE_CONTROL_EXISTS", "A_REAL_INS_IS_STILL_FOUND"],
         patch=lambda: dict(PROOF_CASES=[
             c for c in X.PROOF_CASES if c["case_id"] != "XML-04"])),
    dict(fid="H-04", title="a proof case expects the wrong exact count",
         target="X",
         gates=["ALL_XML_PROOF_CASES_PASS", "INSIDEH_IS_NOT_INS"],
         patch=lambda: dict(PROOF_CASES=[
             dict(c, expected_exact=1) if c["case_id"] == "XML-01" else c
             for c in X.PROOF_CASES])),

    # ============ release guard ============
    dict(fid="J-01", title="Part A is declared passed while custody failed",
         gates=["PART_A_RESULT_IS_BLOCKED"],
         patch=lambda: dict(PART_A_RESULT="PASSED")),
    dict(fid="J-02", title="a superseding release record is issued anyway",
         gates=["NO_SUPERSEDING_RELEASE_RECORD_WAS_ISSUED"],
         patch=lambda: dict(RELEASE_RECORD_NOT_ISSUED=dict(
             S.RELEASE_RECORD_NOT_ISSUED, issued=True, superseding=True))),
    dict(fid="J-03", title="the blocker loses its owner and remedy",
         gates=["THE_BLOCKER_NAMES_AN_OWNER_AND_A_REMEDY"],
         patch=lambda: dict(PART_A_BLOCKER=dict(
             S.PART_A_BLOCKER, owner="", what_would_unblock=""))),
    dict(fid="J-04", title="Part B is recorded as started",
         gates=["PART_B_DID_NOT_START"], patch=lambda: dict(PART_B_STARTED=1)),
    dict(fid="J-05", title="a PPTX is recorded as generated",
         gates=["NO_PPTX_GENERATED"], patch=lambda: dict(PPTX_GENERATED=1)),
    dict(fid="J-06", title="MMD or SCORM work is recorded as started",
         gates=["NO_MMD_REACT_SCORM_OR_LMS_WORK"],
         patch=lambda: dict(MMD_PRODUCTION_STARTED=1, LMS_WORK_STARTED=1)),
    dict(fid="J-07", title="the CNF renumbering is applied under a blocked premise",
         gates=["CNF_RENUMBERING_WAS_NOT_APPLIED"],
         patch=lambda: dict(CONFIRMATION_ID_MAPPING=dict(
             S.CONFIRMATION_ID_MAPPING, applied=True))),
    dict(fid="J-08", title="the ID collision is hidden instead of declared",
         gates=["THE_ID_COLLISION_IS_DECLARED_NOT_HIDDEN"],
         patch=lambda: dict(CONFIRMATION_ID_MAPPING=dict(
             S.CONFIRMATION_ID_MAPPING, rows=[]))),
    dict(fid="J-09", title="the suite loses its identity", target="QA",
         gates=["SUITE_ID_DECLARED"], patch=lambda: dict(SUITE_ID="")),
    dict(fid="J-10", title="the suite adopts the B0.9 suite identity", target="QA",
         gates=["SUITE_ID_DECLARED", "SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE"],
         patch=lambda: dict(SUITE_ID=QA.PRIOR_SUITE_ID)),
    dict(fid="J-11", title="the NOT_CHECKED list is emptied", target="QA",
         gates=["NOT_CHECKED_IS_PUBLISHED"], patch=lambda: dict(NOT_CHECKED=[])),
]

_BASE_AG = None


def _base_ag():
    return _BASE_AG


def _run_suite():
    return {r["gate_id"]: r["ok"] for r in QA.run()}


def run_fixture(f):
    if "disk_create" in f:
        path = os.path.join(REPO, f["disk_create"])
        try:
            with open(path, "wb") as fh:
                fh.write(b"\x89PNG\r\n\x1a\n placeholder, not the evidence")
            return _run_suite()
        except Exception as exc:
            return {"__EXCEPTION__": False, "__MSG__": str(exc)}
        finally:
            if os.path.exists(path):
                os.remove(path)

    tgt = TARGETS[f.get("target", "S")]
    patch = f["patch"]()
    saved = {k: getattr(tgt, k) for k in patch}
    try:
        for k, v in patch.items():
            setattr(tgt, k, v)
        return _run_suite()
    except Exception as exc:
        return {"__EXCEPTION__": False, "__MSG__": str(exc)}
    finally:
        for k, v in saved.items():
            setattr(tgt, k, v)


def main():
    global _BASE_AG
    _BASE_AG = S.ag_register_audit()
    good = _run_suite()
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], title=f["title"],
                        target=("DISK" if "disk_create" in f else f.get("target", "S")),
                        designated_gates=f["gates"], detected=det, fired=fired,
                        note=res.get("__MSG__")))
    return dict(suite_id=QA.SUITE_ID,
                baseline_pass=sum(1 for v in good.values() if v),
                baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out),
                detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                custody_path_clean=not os.path.exists(
                    os.path.join(REPO, S.INTENDED_CUSTODY_PATH)),
                by_target={t: sum(1 for r in out if r["target"] == t)
                           for t in sorted({r["target"] for r in out})},
                fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if (r["missed"] or r["baseline_false_failures"]
                   or not r["custody_path_clean"]) else 0)
