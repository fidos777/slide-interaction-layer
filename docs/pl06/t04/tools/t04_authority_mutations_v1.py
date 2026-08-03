# -*- coding: utf-8 -*-
"""Negative mutations for Stage 4.2F-B0.9.

    SUITE_ID = T04_AUTHORITY_DECISION_INGESTION_QA_v1
    python3 docs/pl06/t04/tools/t04_authority_mutations_v1.py

Each fixture injects a defect the stage exists to prevent — a fabricated hash, an authority
quote dropped, a CAIR decision dressed as Bariah's, a stale claim revived — runs the suite,
and requires the designated gate to fire. Every patch is reverted in a `finally`.

Three fixtures rewrite the emitted artifact ON DISK rather than patching memory. That is the
only honest way to model "a stale claim exists only in the Markdown": a memory patch would
not reach the file the reconciliation gates read. The originals are restored byte-for-byte
and `post_run_restored` confirms it.

A fixture proves a gate is SENSITIVE to a defect. It proves nothing about correctness.
"""
import copy
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import t04_authority_data_v1 as D    # noqa: E402
import t04_authority_qa_v1 as QA     # noqa: E402

TARGETS = {"D": D, "QA": QA}


def _find(seq, key, val):
    return next(x for x in seq if x[key] == val)


def _dec(fn):
    """Patch the decision TUPLE list, so the live register recomputes from the mutation."""
    def apply():
        d = [list(x) for x in D._DECISIONS]
        fn(d)
        return dict(_DECISIONS=[tuple(x) for x in d])
    return apply


def _seq(fn):
    def apply():
        s = [list(x) for x in D._SEQ]
        fn(s)
        return dict(_SEQ=[tuple(x) for x in s])
    return apply


def _quiz(fn):
    def apply():
        q = copy.deepcopy(D._QUIZ)
        fn(q)
        return dict(_QUIZ=q)
    return apply


def _ev(fn):
    def apply():
        e = copy.deepcopy(D.EVIDENCE)
        fn(e)
        return dict(EVIDENCE=e)
    return apply


def _cnf(fn):
    def apply():
        c = copy.deepcopy(D.CONFIRMATIONS)
        fn(c)
        return dict(CONFIRMATIONS=c)
    return apply


def _dlg(fn):
    def apply():
        g = copy.deepcopy(D.FINAL_DIALOGUE)
        fn(g)
        return dict(FINAL_DIALOGUE=g)
    return apply


def _rum(fn):
    def apply():
        r = copy.deepcopy(D.FINAL_RUMUSAN)
        fn(r)
        return dict(FINAL_RUMUSAN=r)
    return apply


def _vis(fn):
    def apply():
        v = copy.deepcopy(D.FINAL_VISUAL_SCOPE)
        fn(v)
        return dict(FINAL_VISUAL_SCOPE=v)
    return apply


def _disk(name, replace, with_, count=1):
    """Rewrite an emitted artifact on disk. Restored byte-for-byte in the finally."""
    return dict(_disk=(name, replace, with_, count))


def _reg(fn):
    """Patch the derivation function itself, for defects that live in the derivation."""
    base = D._decision_register

    def apply():
        def patched():
            rows = base()
            fn(rows)
            return rows
        return dict(_decision_register=patched)
    return apply


FIXTURES = [
    # ================= evidence integrity =================
    dict(fid="A-01", title="a hash is fabricated for the screenshot that was never supplied",
         gates=["NO_FABRICATED_HASH_FOR_UNSUPPLIED_EVIDENCE",
                "SUPPLEMENTARY_HASH_IS_NOT_SUPPLIED_NOT_A_VALUE"],
         patch=_ev(lambda e: _find(e, "evidence_id", "AUTH-EV-02").update(
             sha256=hashlib.sha256(b"invented").hexdigest()))),
    dict(fid="A-02", title="the unsupplied screenshot is marked as supplied",
         gates=["SUPPLEMENTARY_EVIDENCE_MARKED_NOT_SUPPLIED"],
         patch=_ev(lambda e: _find(e, "evidence_id", "AUTH-EV-02").update(
             supplied_in_this_run=True))),
    dict(fid="A-03", title="pixel dimensions are invented for the missing screenshot",
         gates=["SUPPLEMENTARY_HASH_IS_NOT_SUPPLIED_NOT_A_VALUE"],
         patch=_ev(lambda e: _find(e, "evidence_id", "AUTH-EV-02").update(
             dimensions_or_extent="1080 × 2400"))),
    dict(fid="A-04", title="the primary artifact's recorded hash drifts from the file",
         gates=["AUTHORITY_DOCX_SHA256_MATCHES"],
         patch=lambda: dict(PRIMARY_DOCX_SHA256="0" * 64)),
    dict(fid="A-05", title="the primary artifact's recorded byte size drifts from the file",
         gates=["AUTHORITY_DOCX_BYTE_SIZE_MATCHES"],
         patch=lambda: dict(PRIMARY_DOCX_BYTES=36104)),
    dict(fid="A-06", title="tracked changes are claimed in a document that has none",
         gates=["TRACKED_CHANGES_NOT_CLAIMED"],
         patch=lambda: dict(PRIMARY_ARTIFACT_MECHANISM=dict(
             D.PRIMARY_ARTIFACT_MECHANISM, tracked_changes_present=True,
             tracked_change_element_count=12))),
    dict(fid="A-07", title="Word comments are claimed in a document that has none",
         gates=["TRACKED_CHANGES_NOT_CLAIMED"],
         patch=lambda: dict(PRIMARY_ARTIFACT_MECHANISM=dict(
             D.PRIMARY_ARTIFACT_MECHANISM, word_comments_present=True,
             word_comment_count=9))),
    dict(fid="A-08", title="the substring counting trap is dropped from the disclosure",
         gates=["SUBSTRING_COUNTING_TRAP_DISCLOSED"],
         patch=lambda: dict(PRIMARY_ARTIFACT_MECHANISM=dict(
             D.PRIMARY_ARTIFACT_MECHANISM,
             counting_trap="Twelve tracked insertions were counted."))),
    dict(fid="A-09", title="an evidence record loses its limitations",
         gates=["EVERY_EVIDENCE_RECORD_STATES_ITS_LIMITATIONS"],
         patch=_ev(lambda e: _find(e, "evidence_id", "AUTH-EV-01").update(limitations=""))),
    dict(fid="A-10", title="an evidence record loses its provenance chain",
         gates=["EVERY_EVIDENCE_RECORD_STATES_ITS_PROVENANCE"],
         patch=_ev(lambda e: _find(e, "evidence_id", "AUTH-EV-03").update(
             provenance_chain=""))),
    dict(fid="A-11", title="the evidence hierarchy loses a level",
         gates=["EVIDENCE_HIERARCHY_HAS_FOUR_LEVELS"],
         patch=_ev(lambda e: e.pop())),
    dict(fid="A-12", title="the superseded v2 DOCX is presented as an authority artifact",
         gates=["V2_RECORDED_AS_SUPERSEDED_NOT_AUTHORITY"],
         patch=lambda: dict(SUPERSEDED_ARTIFACTS=[
             s for s in D.SUPERSEDED_ARTIFACTS if "v2.docx" not in s["path"]])),

    # ================= confirmation discipline =================
    dict(fid="B-01", title="the Firdaus-authored Q3 line is re-presented as a Bariah confirmation",
         gates=["Q3_LINE_RECORDED_AS_FIRDAUS_NOT_AUTHORITY", "Q3_CHANGES_NO_CONTENT"],
         patch=_cnf(lambda c: _find(c, "confirmation_id", "T04-CNF-03").update(
             status="CONFIRMED_BY_AUTHORITY", author="BARIAH", is_authority_statement=True,
             applied_to_content=True))),
    dict(fid="B-02", title="the Q3 delegation is relabelled a Bariah-originated rule",
         gates=["Q3_NOT_LABELLED_AN_AUTHORITY_ORIGINATED_RULE"],
         patch=_cnf(lambda c: _find(c, "confirmation_id", "T04-CNF-03").update(
             secondary_status="BARIAH_ORIGINATED_RULE"))),
    dict(fid="B-03", title="one of the two Q3 candidate referents is quietly dropped",
         gates=["Q3_CANDIDATE_REFERENTS_BOTH_LISTED"],
         patch=_cnf(lambda c: _find(c, "confirmation_id", "T04-CNF-03")[
             "candidate_referents"].pop())),
    dict(fid="B-04", title="the WhatsApp evidence is upgraded to a verified grade",
         gates=["EVERY_CONFIRMATION_IS_GRADED_DEGRADED"],
         patch=_cnf(lambda c: _find(c, "confirmation_id", "T04-CNF-01").update(
             evidence_grade="VERIFIED_PRIMARY_ARTIFACT"))),
    dict(fid="B-05", title="a confirmation loses the quoted wording it rests on",
         gates=["EVERY_CONFIRMATION_CARRIES_ITS_QUOTE"],
         patch=_cnf(lambda c: _find(c, "confirmation_id", "T04-CNF-02").update(
             authority_quote=""))),
    dict(fid="B-06", title="a confirmation stops declaring what it does not establish",
         gates=["EVERY_CONFIRMATION_STATES_ITS_LIMIT"],
         patch=_cnf(lambda c: _find(c, "confirmation_id", "T04-CNF-01").update(
             what_this_does_not_establish=""))),
    dict(fid="B-07", title="the screenshot acceptance is used to change T04 content",
         gates=["ONLY_Q5_TYPE_IS_APPLIED_FROM_WHATSAPP"],
         patch=_cnf(lambda c: _find(c, "confirmation_id", "T04-CNF-01").update(
             applied_to_content=True))),
    dict(fid="B-08", title="'Q3' is adopted verbatim as a decision identifier",
         gates=["Q3_IS_NOT_USED_AS_A_DECISION_ID"],
         patch=_cnf(lambda c: _find(c, "confirmation_id", "T04-CNF-03").update(
             confirmation_id="Q3"))),

    # ================= decision typing =================
    dict(fid="C-01", title="every decision is flattened into one accepted status",
         gates=["DECISIONS_NOT_FLATTENED_INTO_ONE_CLASS", "EVERY_DECISION_CLASS_IS_POPULATED"],
         patch=_dec(lambda d: [x.__setitem__(1, "ACCEPTED_AS_PROPOSED") for x in d])),
    dict(fid="C-02", title="a CAIR-executed amendment is recorded as authority-authored",
         gates=["CAIR_EXECUTED_DECISIONS_ARE_NOT_AUTHORITY_AUTHORED"],
         patch=_reg(lambda r: _find(r, "decision_id", "T04-DEC-E08").update(
             authored_by_authority=True))),
    dict(fid="C-03", title="a decision loses the authority wording it was derived from",
         gates=["EVERY_DECISION_CARRIES_ITS_AUTHORITY_QUOTE"],
         patch=_dec(lambda d: _find_row(d, "T04-DEC-C01").__setitem__(3, ""))),
    dict(fid="C-04", title="a WhatsApp decision is upgraded to the verified evidence grade",
         gates=["WHATSAPP_RECORDS_ARE_GRADED_BY_HOW_THEY_WERE_READ"],
         patch=_dec(lambda d: _find_row(d, "T04-DEC-X01").__setitem__(4, "A"))),
    dict(fid="C-05", title="the delegated Q3 decision is marked settled",
         gates=["THE_TWO_NAMED_DELEGATIONS_REMAIN_UNSETTLED",
                "THE_Q3_DELEGATION_KEEPS_ITS_DELEGATED_CLASS"],
         patch=_dec(lambda d: _find_row(d, "T04-DEC-X01").__setitem__(
             1, "ACCEPTED_AS_PROPOSED"))),
    dict(fid="C-06", title="the pembajaan wording is corrected silently",
         gates=["NO_CORRECTION_IS_SILENT", "PEMBAJAAN_CORRECTION_PRESENT"],
         patch=lambda: dict(AUTHORITY_WORDING_CORRECTIONS=[
             dict(c, as_written_by_authority=c["as_applied"])
             for c in D.AUTHORITY_WORDING_CORRECTIONS])),
    dict(fid="C-07", title="the wording correction is presented as Bariah-confirmed",
         gates=["CORRECTIONS_ARE_PENDING_NOT_APPROVED"],
         patch=lambda: dict(AUTHORITY_WORDING_CORRECTIONS=[
             dict(c, status="CONFIRMED_BY_BARIAH")
             for c in D.AUTHORITY_WORDING_CORRECTIONS])),
    dict(fid="C-08", title="the wording correction record is removed entirely",
         gates=["PEMBAJAAN_CORRECTION_PRESENT", "EVERY_WORDING_CORRECTION_IS_RECORDED"],
         patch=lambda: dict(AUTHORITY_WORDING_CORRECTIONS=[])),
    dict(fid="C-09", title="the D-04 PPE supersession drops its residual-risk owner",
         gates=["EVERY_SUPERSESSION_NAMES_ITS_RISK_OWNER",
                "D04_PPE_SUPERSESSION_RECORDED_WITH_ITS_RISK"],
         patch=lambda: dict(SUPERSESSIONS=[dict(s, risk_owner="")
                                           for s in D.SUPERSESSIONS])),
    dict(fid="C-10", title="a supersession points at a decision that does not exist",
         gates=["EVERY_SUPERSESSION_RESOLVES_TO_A_REAL_DECISION"],
         patch=lambda: dict(SUPERSESSIONS=[dict(s, superseded_by="T04-DEC-ZZ")
                                           for s in D.SUPERSESSIONS])),
    dict(fid="C-11", title="a decision class is left with no decisions in it",
         gates=["EVERY_DECISION_CLASS_IS_POPULATED"],
         patch=_dec(lambda d: [x.__setitem__(1, "ACCEPTED_AS_PROPOSED")
                               for x in d if x[1] == "GLOBAL_COURSE_RULE"])),
    dict(fid="C-12", title="a decision stops naming what it applies to",
         gates=["EVERY_DECISION_APPLIES_TO_SOMETHING"],
         patch=_dec(lambda d: _find_row(d, "T04-DEC-B05").__setitem__(5, []))),

    # ================= sequence integrity =================
    dict(fid="D-01", title="the inserted screen is dropped and the sequence reverts to 21",
         gates=["FINAL_SCREEN_COUNT_IS_TWENTY_TWO", "EXACTLY_ONE_SCREEN_INSERTED",
                "SCREEN_IDS_ARE_CONTIGUOUS"],
         patch=_seq(lambda s: s.pop(13))),
    dict(fid="D-02", title="the closing screen reverts to Tamat Bahagian",
         gates=["CLOSING_SCREEN_READS_TAMAT_TOPIK",
                "NO_SCREEN_TITLE_SAYS_TAMAT_BAHAGIAN"],
         patch=_seq(lambda s: s[-1].__setitem__(2, "Tamat Bahagian"))),
    dict(fid="D-03", title="the inserted screen loses its source binding",
         gates=["INSERTED_SCREEN_IS_SOURCE_BOUND",
                "THE_INSERTED_SCREENS_ROW_WAS_REASSIGNED_NOT_DUPLICATED",
                "SOURCE_BINDINGS_NOT_REMOVED_FROM_THE_MODEL"],
         patch=_seq(lambda s: s[13].__setitem__(5, []))),
    dict(fid="D-04", title="a renumbered screen keeps its old number",
         gates=["SCREEN_IDS_ARE_CONTIGUOUS", "RENUMBERING_IS_A_PLUS_ONE_SHIFT"],
         patch=_seq(lambda s: s[15].__setitem__(0, "T04-S15"))),
    dict(fid="D-05", title="two screens claim the same predecessor",
         gates=["NO_PRIOR_SCREEN_MAPS_TWICE", "EVERY_PRIOR_SCREEN_SURVIVES"],
         patch=_seq(lambda s: s[16].__setitem__(1, "T04-S15"))),
    dict(fid="D-06", title="a prior screen disappears from the mapping altogether",
         gates=["EVERY_PRIOR_SCREEN_SURVIVES"],
         patch=_seq(lambda s: s[19].__setitem__(1, None))),
    dict(fid="D-07", title="PPE Lengkap is quietly removed from the S16 reveal list",
         gates=["PPE_LENGKAP_IS_A_NAMED_REVEAL_ON_S16",
                "NAMED_REVEAL_ITEMS_PRESENT_ON_BOTH_SCREENS"],
         patch=lambda: dict(NAMED_REVEAL_ITEMS=dict(
             D.NAMED_REVEAL_ITEMS,
             **{"T04-S16": ["Penyimpanan Dan Pelupusan",
                            "Helaian Data Keselamatan (SDS)"]}))),
    dict(fid="D-08", title="a treatment change is recorded that changes nothing",
         gates=["EVERY_TREATMENT_CHANGE_ACTUALLY_CHANGES_THE_TREATMENT"],
         patch=_seq(lambda s: s[11].__setitem__(3, "CLICK_TO_REVEAL"))),
    dict(fid="D-09", title="a renumber-only screen silently changes treatment too",
         gates=["RENUMBER_ONLY_SCREENS_KEEP_THEIR_TREATMENT"],
         patch=_seq(lambda s: s[14].__setitem__(3, "CLICK_TO_REVEAL"))),
    dict(fid="D-10", title="a static screen keeps reveal states it should no longer have",
         gates=["STATIC_SCREENS_HAVE_NO_REVEAL_STATES"],
         patch=_seq(lambda s: s[16].__setitem__(
             4, ["BASE", "REVEAL_SPRAY_CONDITIONS", "ALL_VIEWED"]))),
    dict(fid="D-11", title="the internal unit ID is renamed to match the learner label",
         gates=["INTERNAL_UNIT_ID_UNCHANGED", "INTERNAL_ID_AND_DISPLAY_LABEL_ARE_DISTINCT"],
         patch=lambda: dict(INTERNAL_UNIT_ID="Topik 4")),
    dict(fid="D-12", title="the learner display unit reintroduces a Bahagian",
         gates=["LEARNER_DISPLAY_UNIT_IS_TOPIK_4"],
         patch=lambda: dict(LEARNER_DISPLAY_UNIT="Topik 4 Bahagian 1")),
    dict(fid="D-13", title="a screen stops naming the decision that governs it",
         gates=["EVERY_SCREEN_NAMES_ITS_DECISIONS"],
         patch=_seq(lambda s: s[3].__setitem__(6, []))),
    dict(fid="D-14", title="a screen cites a decision that does not exist",
         gates=["EVERY_SCREEN_DECISION_RESOLVES"],
         patch=_seq(lambda s: s[4].__setitem__(6, ["T04-DEC-A99"]))),
    dict(fid="D-15", title="an aspect list is removed from a main-explanation screen",
         gates=["ASPECT_LISTS_ON_THE_THREE_MAIN_EXPLANATION_SCREENS"],
         patch=lambda: dict(NAMED_ASPECT_LISTS={
             k: v for k, v in D.NAMED_ASPECT_LISTS.items() if k != "T04-S11"})),

    # ================= content fidelity =================
    dict(fid="E-01", title="a fifth dialogue line is restored",
         gates=["DIALOGUE_HAS_FOUR_LINES", "DIALOGUE_IDS_ARE_THE_FINAL_SERIES"],
         patch=_dlg(lambda g: g["lines"].append(dict(
             g["lines"][0], line_id="T04-DLG-F05", position=5,
             text_ms="Alya: Jadi saya kena faham keperluan kedua-duanya dulu.")))),
    dict(fid="E-02", title="a dialogue line is paraphrased away from Bariah's wording",
         gates=["EVERY_DIALOGUE_LINE_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX"],
         patch=_dlg(lambda g: g["lines"][0].update(
             text_ms="Encik Rahman, projek sudah siap. Mengapa taman masih perlu dijaga?"))),
    dict(fid="E-03", title="a compliance duty is written into character dialogue",
         gates=["NO_COMPLIANCE_DUTY_IN_THE_DIALOGUE",
                "EVERY_DIALOGUE_LINE_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX"],
         patch=_dlg(lambda g: g["lines"][3].update(
             text_ms="Ya. Pengendali mesti berlesen dan PPE lengkap wajib dipakai."))),
    dict(fid="E-04", title="the banned soft-versus-hard contrast returns to the dialogue",
         gates=["NO_SOFT_VERSUS_HARD_CONTRAST_IN_THE_DIALOGUE",
                "EVERY_DIALOGUE_LINE_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX"],
         patch=_dlg(lambda g: g["lines"][2].update(
             text_ms="Apa bezanya antara landskap lembut dan landskap kejur?"))),
    dict(fid="E-05", title="dialogue is relabelled CAIR-authored",
         gates=["DIALOGUE_IS_AUTHORITY_AUTHORED"],
         patch=_dlg(lambda g: [x.update(authorship="CAIR_DRAFT") for x in g["lines"]])),
    dict(fid="E-06", title="the Rumusan reverts to four points",
         gates=["RUMUSAN_HAS_THREE_BEATS", "RUMUSAN_BEATS_ARE_THE_NAMED_THREE"],
         patch=_rum(lambda r: r["points"].append(dict(
             r["points"][0], point_id="T04-RUM-F04", beat="Tambahan",
             text_ms="Kontraktor dapat merancang, melaksana dan mendokumentasikan setiap "
                     "operasi mengikut spesifikasi.")))),
    dict(fid="E-07", title="a Rumusan beat is paraphrased away from Bariah's wording",
         gates=["EVERY_RUMUSAN_BEAT_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX"],
         patch=_rum(lambda r: r["points"][2].update(
             text_ms="Penjagaan berjadual memelihara kualiti landskap sepanjang DLP."))),
    dict(fid="E-08", title="the over-broad point 04 generalisation is restored",
         gates=["RUMUSAN_04_GENERALISATION_IS_GONE",
                "EVERY_RUMUSAN_BEAT_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX"],
         patch=_rum(lambda r: r["points"][2].update(
             text_ms="Kontraktor mendokumentasikan setiap operasi dengan pengendali "
                     "berlesen dan penyimpanan berkunci."))),
    dict(fid="E-09", title="a course-wide Rumusan rule is inferred from a T04 amendment",
         gates=["THREE_BEAT_RULE_IS_NOT_INFERRED_COURSE_WIDE"],
         patch=_rum(lambda r: r["scope_of_the_three_beat_structure"].update(
             applies_to="ALL_PLS_IN_KURSUS"))),
    dict(fid="E-10", title="the archived DEP-RUM04-Q5 dependency is deleted rather than archived",
         gates=["DEP_RUM04_Q5_IS_ARCHIVED_NOT_DELETED",
                "ARCHIVED_DEPENDENCY_STATES_ITS_REOPEN_CONDITION"],
         patch=lambda: dict(ARCHIVED_DEPENDENCIES=[])),
    dict(fid="E-11", title="the archived dependency cites a decision that does not exist",
         gates=["ARCHIVED_DEPENDENCY_NAMES_WHAT_RESOLVED_IT"],
         patch=lambda: dict(ARCHIVED_DEPENDENCIES=[
             dict(d, resolved_by=["T04-DEC-ZZ"]) for d in D.ARCHIVED_DEPENDENCIES])),

    # ================= assessment integrity =================
    dict(fid="F-01", title="a quiz stem is paraphrased away from Bariah's wording",
         gates=["THE_FOUR_DOCX_STEMS_APPEAR_VERBATIM_IN_THE_AUTHORITY_DOCX"],
         patch=_quiz(lambda q: q[0].update(
             stem="Apakah tiga tanggungjawab utama bagi landskap lembut?"))),
    dict(fid="F-02", title="a stem keeps its module attribution after the global rule",
         gates=["NO_MODULE_ATTRIBUTION_IN_ANY_STEM",
                "THE_FOUR_DOCX_STEMS_APPEAR_VERBATIM_IN_THE_AUTHORITY_DOCX"],
         patch=_quiz(lambda q: q[2].update(
             stem="Mengikut susunan keutamaan IPM dalam modul, kaedah kawalan yang manakah "
                  "disenaraikan paling akhir?"))),
    dict(fid="F-03", title="Q5 options revert to letter labels",
         gates=["MULTIPLE_RESPONSE_OPTIONS_USE_CHECKBOXES",
                "MULTIPLE_RESPONSE_OPTIONS_CARRY_NO_LETTER"],
         patch=_quiz(lambda q: q[4].update(qtype="MCQ"))),
    dict(fid="F-04", title="the two fertiliser distractors are restored to Q5",
         gates=["SUPERSEDED_FERTILISER_DISTRACTORS_ARE_GONE",
                "REPLACEMENT_DISTRACTORS_ARE_IN_THE_LIVE_OPTION_SET"],
         patch=_quiz(lambda q: q[4]["options"].__setitem__(
             slice(4, 6),
             ["Baja disimpan di tempat yang kering dan jauh dari sumber air",
              "Rekod pembajaan disimpan sebagai bukti kerja untuk tuntutan bayaran"]))),
    dict(fid="F-17", title="the Set A pair Bariah rejected is restored to the live model",
         gates=["REPLACEMENT_DISTRACTORS_ARE_IN_THE_LIVE_OPTION_SET"],
         patch=_quiz(lambda q: q[4]["options"].__setitem__(
             slice(4, 6),
             ["Notifikasi kepada penduduk dibuat hanya selepas semburan selesai",
              "SDS hanya perlu disimpan di pejabat projek dan tidak perlu berada di tapak"]))),
    dict(fid="F-18", title="the Q5 stem is relabelled as authority-authored",
         gates=["THE_Q5_STEM_CARRIES_THE_WEAKER_PROVENANCE",
                "EXACTLY_ONE_STEM_IS_NOT_DOCX_SOURCED_AND_IT_IS_NAMED"],
         patch=_quiz(lambda q: q[4].update(
             stem_provenance="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"))),
    dict(fid="F-19", title="a second stem quietly stops being DOCX-sourced",
         gates=["EXACTLY_ONE_STEM_IS_NOT_DOCX_SOURCED_AND_IT_IS_NAMED",
                "THE_FOUR_DOCX_STEMS_ARE_AUTHORITY_AUTHORED"],
         patch=_quiz(lambda q: q[1].update(stem_provenance="FIRDAUS_DIRECTED"))),
    dict(fid="F-20", title="the Bariah-written Q5 stem is erased from the record",
         gates=["THE_BARIAH_WRITTEN_Q5_STEM_IS_STILL_ON_RECORD"],
         patch=_quiz(lambda q: q[4].update(superseded_stem_b09=None))),
    dict(fid="F-21", title="the superseded CAIR draft wording is erased",
         gates=["THE_SUPERSEDED_CAIR_DRAFT_WORDING_IS_RETAINED"],
         patch=lambda: dict(QUIZ_Q5_OPTION_SUBSTITUTIONS=[
             {k: v for k, v in s.items() if k != "cair_draft_superseded_by_e07"}
             for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS])),
    dict(fid="F-22", title="a closure is recorded with no closing record",
         gates=["EVERY_CLOSURE_NAMES_WHAT_CLOSED_IT"],
         patch=lambda: dict(CLOSED_SINCE_B0_9=[
             dict(c, closed_by="", closing_record="") for c in D.CLOSED_SINCE_B0_9])),
    dict(fid="F-23", title="a fourth item is claimed closed since B0.9",
         gates=["THREE_ITEMS_CLOSED_SINCE_B0_9"],
         patch=lambda: dict(CLOSED_SINCE_B0_9=D.CLOSED_SINCE_B0_9 + [
             dict(open_id="E-02", subject="answer keys", closed_by="nothing",
                  closing_record="none")])),
    dict(fid="F-05", title="a replacement distractor is written about baja again",
         gates=["REPLACEMENT_DISTRACTORS_ARE_NOT_ABOUT_BAJA"],
         patch=lambda: dict(QUIZ_Q5_OPTION_SUBSTITUTIONS=[
             dict(D.QUIZ_Q5_OPTION_SUBSTITUTIONS[0],
                  replacement_text="Baja cecair disimpan berasingan daripada racun"),
             D.QUIZ_Q5_OPTION_SUBSTITUTIONS[1]])),
    dict(fid="F-06", title="the CAIR-written distractors are presented as Bariah's",
         gates=["REPLACEMENT_DISTRACTORS_ARE_NEVER_MARKED_AUTHORITY_WRITTEN",
                "REPLACEMENT_DISTRACTORS_ARE_SELECTED_NOT_AUTHORED"],
         patch=lambda: dict(QUIZ_Q5_OPTION_SUBSTITUTIONS=[
             dict(s, authorship="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT")
             for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS])),
    dict(fid="F-07", title="the CAIR-written distractors are marked approved",
         gates=["REPLACEMENT_DISTRACTORS_ARE_CLOSED_BY_E07"],
         patch=lambda: dict(QUIZ_Q5_OPTION_SUBSTITUTIONS=[
             dict(s, approval_status="BARIAH_APPROVED")
             for s in D.QUIZ_Q5_OPTION_SUBSTITUTIONS])),
    dict(fid="F-08", title="the route choice between Bariah's two options is attributed to her",
         gates=["THE_ROUTE_CHOICE_IS_ATTRIBUTED_TO_CAIR"],
         patch=lambda: dict(QUIZ_Q5_ROUTE_CHOICE=dict(
             D.QUIZ_Q5_ROUTE_CHOICE, chosen_by="BARIAH_AHMAD"))),
    dict(fid="F-09", title="the answer key is declared final",
         gates=["ANSWER_KEY_IS_NOT_FINAL", "EVERY_OPTION_KEY_FLAG_IS_MARKED_PROPOSED"],
         patch=lambda: dict(ANSWER_KEY_STATUS="FINAL_APPROVED")),
    dict(fid="F-10", title="an MCQ item is given two correct answers",
         gates=["MCQ_ITEMS_HAVE_EXACTLY_ONE_KEY"],
         patch=_quiz(lambda q: q[1].update(key=[0, 1]))),
    dict(fid="F-11", title="the multiple-response item is reduced to one key",
         gates=["MULTIPLE_RESPONSE_HAS_MORE_THAN_ONE_KEY"],
         patch=_quiz(lambda q: q[4].update(key=[0]))),
    dict(fid="F-12", title="Q5 loses two options and is no longer a six-option set",
         gates=["Q5_HAS_SIX_OPTIONS", "REPLACEMENT_DISTRACTORS_ARE_IN_THE_LIVE_OPTION_SET"],
         patch=_quiz(lambda q: q[4].__setitem__("options", q[4]["options"][:4]))),
    dict(fid="F-13", title="a quiz item loses its source binding",
         gates=["EVERY_QUIZ_ITEM_IS_SOURCE_BOUND"],
         patch=_quiz(lambda q: q[3].update(source_rows=[]))),
    dict(fid="F-14", title="a quiz item cites a source row that does not exist",
         gates=["EVERY_QUIZ_SOURCE_ROW_RESOLVES"],
         patch=_quiz(lambda q: q[0].update(source_rows=["T04-ROW-999"]))),
    dict(fid="F-15", title="a quiz option names the Act directly",
         gates=["NO_QUIZ_OPTION_NAMES_THE_ACT"],
         patch=_quiz(lambda q: q[4]["options"].__setitem__(
             0, "Pengendali mematuhi Akta Racun Makhluk Perosak 1974"))),
    dict(fid="F-16", title="the pass mark is changed without an authority decision",
         gates=["PASS_MARK_UNCHANGED"],
         patch=lambda: dict(QUIZ_PASS_MARK="70 peratus",
                            FINAL_QUIZ=dict(D.FINAL_QUIZ, pass_mark="70 peratus"))),

    # ================= global rule scope =================
    dict(fid="G-01", title="a global rule is narrowed to T04 only",
         gates=["BOTH_GLOBAL_RULES_SCOPE_ALL_PLS"],
         patch=lambda: dict(QUIZ_GLOBAL_RULES=[
             dict(D.QUIZ_GLOBAL_RULES[0], scope="T04_ONLY"), D.QUIZ_GLOBAL_RULES[1]])),
    dict(fid="G-02", title="a global rule loses the wording that makes it course-wide",
         gates=["BOTH_GLOBAL_RULES_QUOTE_GLOBAL_KESELURUHAN_KURSUS"],
         patch=lambda: dict(QUIZ_GLOBAL_RULES=[
             dict(D.QUIZ_GLOBAL_RULES[0], authority_quote="buang kata dalam modul"),
             D.QUIZ_GLOBAL_RULES[1]])),
    dict(fid="G-03", title="a dialogue decision is promoted to course-wide scope",
         gates=["NO_DIALOGUE_DECISION_IS_COURSE_WIDE", "ONLY_TWO_DECISIONS_ARE_COURSE_WIDE"],
         patch=_dec(lambda d: _find_row(d, "T04-DEC-C03").__setitem__(
             6, "ALL_PLS_IN_KURSUS"))),
    dict(fid="G-04", title="a Rumusan decision is promoted to course-wide scope",
         gates=["NO_RUMUSAN_DECISION_IS_COURSE_WIDE", "ONLY_TWO_DECISIONS_ARE_COURSE_WIDE"],
         patch=_dec(lambda d: _find_row(d, "T04-DEC-D01").__setitem__(
             6, "ALL_PLS_IN_KURSUS"))),
    dict(fid="G-05", title="a global rule targets an item that does not exist",
         gates=["GLOBAL_RULE_TARGETS_RESOLVE_TO_REAL_ITEMS"],
         patch=lambda: dict(QUIZ_GLOBAL_RULES=[
             dict(D.QUIZ_GLOBAL_RULES[0], applied_to_t04_items=["T04-QZ-Q9"]),
             D.QUIZ_GLOBAL_RULES[1]])),
    dict(fid="G-06", title="a global rule stops saying how it is enforced",
         gates=["GLOBAL_RULES_STATE_THEIR_ENFORCEMENT"],
         patch=lambda: dict(QUIZ_GLOBAL_RULES=[
             dict(r, enforcement="") for r in D.QUIZ_GLOBAL_RULES])),

    # ================= visual scope =================
    dict(fid="H-01", title="the visual set is upgraded to unconditional approval",
         gates=["VISUAL_SCOPE_STATUS_IS_ACCEPTED_WITH_CONDITIONS"],
         patch=_vis(lambda v: v.update(status="APPROVED"))),
    dict(fid="H-02", title="46 obligations are reported as 46 unique assets",
         gates=["FORTY_SIX_IS_NOT_FORTY_ONE", "ACCEPTED_PRODUCTION_SCOPE_IS_FORTY_ONE",
                "ASSET_TOTALS_DERIVED_LIVE_FROM_THE_CONTENT_MODEL"],
         patch=_vis(lambda v: v.update(proposed_unique_assets=46,
                                       accepted_production_scope=46))),
    dict(fid="H-03", title="a do-not-reuse item loses its decision-basis line",
         gates=["EVERY_DO_NOT_REUSE_ITEM_CARRIES_A_DECISION_BASIS",
                "ALL_THREE_BASES_ARE_BOTH_LENSES",
                "DO_NOT_REUSE_SNAPSHOT_AGREES_WITH_LIVE"],
         patch=lambda: dict(FINAL_VISUAL_SCOPE=dict(
             D.FINAL_VISUAL_SCOPE,
             do_not_reuse_items=[dict(x, decision_basis="UNSTATED")
                                 for x in D._do_not_reuse_items()]))),
    dict(fid="H-04", title="a do-not-reuse restriction is widened to the whole group",
         gates=["DO_NOT_REUSE_SNAPSHOT_AGREES_WITH_LIVE"],
         patch=lambda: dict(FINAL_VISUAL_SCOPE=dict(
             D.FINAL_VISUAL_SCOPE,
             do_not_reuse_items=[dict(x, restriction_scope="WHOLE_GROUP")
                                 for x in D._do_not_reuse_items()]))),
    dict(fid="H-05", title="a do-not-reuse item is dropped from the three",
         gates=["THREE_DO_NOT_REUSE_ITEMS", "RESTRICTED_ITEMS_MAP_TO_THEIR_GROUPS"],
         patch=lambda: dict(_DO_NOT_REUSE=D._DO_NOT_REUSE[:2])),
    dict(fid="H-06", title="the instructional-over-production precedence rule is dropped",
         gates=["PRECEDENCE_RULE_IS_INSTRUCTIONAL_OVER_PRODUCTION"],
         patch=_vis(lambda v: v["precedence_rule"].update(
             authority_quote="Cadangan perkongsian munasabah untuk pengoptimuman produksi."))),
    dict(fid="H-07", title="the precedence rule is made advisory rather than binding",
         gates=["PRECEDENCE_RULE_IS_BINDING_NOT_ADVISORY"],
         patch=_vis(lambda v: v["precedence_rule"].update(binding_on=""))),
    dict(fid="H-08", title="the inserted screen is credited with a new unique asset",
         gates=["THE_INSERTED_SCREEN_ADDS_NO_ASSET"],
         patch=_vis(lambda v: v["new_screen_asset_impact"].update(new_unique_assets=1))),
    dict(fid="H-09", title="proposed assets are described as approved artwork",
         gates=["NO_ARTWORK_IS_APPROVED"],
         patch=_vis(lambda v: v.update(
             what_is_not_approved="Bariah approved the full asset set including artwork."))),
    dict(fid="H-10", title="MMD production is marked started for a group",
         gates=["ASSET_GROUP_SNAPSHOT_AGREES_WITH_LIVE"],
         patch=lambda: dict(FINAL_VISUAL_SCOPE=dict(
             D.FINAL_VISUAL_SCOPE,
             asset_groups=[dict(g, mmd_production_status="IN_PROGRESS")
                           for g in D.asset_group_scope()]))),

    # ================= source status =================
    dict(fid="J-01", title="the open round trip is reported as closed",
         gates=["ROUND_TRIP_REPRODUCIBILITY_OPEN"],
         patch=lambda: dict(SOURCE_STATUS=dict(
             D.SOURCE_STATUS, ORIGINAL_DOCX_ROUND_TRIP_REPRODUCIBILITY="VERIFIED"))),
    dict(fid="J-02", title="the hash proof is reported as complete",
         gates=["RETRIEVAL_AND_HASH_PROOF_OPEN"],
         patch=lambda: dict(SOURCE_STATUS=dict(
             D.SOURCE_STATUS, SOURCE_DOCX_RETRIEVAL_AND_HASH_PROOF="PROVEN"))),
    dict(fid="J-03", title="source bindings are reported absent when they are present",
         gates=["SOURCE_BINDINGS_PRESENT"],
         patch=lambda: dict(SOURCE_STATUS=dict(
             D.SOURCE_STATUS, CONTROLLED_EXTRACT_SOURCE_BINDINGS="ABSENT"))),
    dict(fid="J-04", title="the final content is marked SOURCE_UNSUPPORTED",
         gates=["FINAL_CONTENT_IS_NOT_MARKED_SOURCE_UNSUPPORTED"],
         patch=_vis(lambda v: v.update(status="SOURCE_UNSUPPORTED"))),
    dict(fid="J-05", title="the open source risk is escalated to blocking",
         gates=["OPEN_RISK_IS_NON_BLOCKING"],
         patch=lambda: dict(SOURCE_STATUS_DETAIL=dict(
             D.SOURCE_STATUS_DETAIL, blocking=True))),
    dict(fid="J-06", title="the risk token is replaced with a blocking token",
         gates=["RISK_TOKEN_IS_THE_DECLARED_ONE"],
         patch=lambda: dict(SOURCE_RISK_TOKEN="SOURCE_REPRODUCIBILITY_BLOCKING")),

    # ================= freeze honesty =================
    dict(fid="K-01", title="the Q5 options are recorded as authority-approved",
         gates=["Q5_OPTIONS_STATE_IS_SELECTED_BY_THE_AUTHORITY",
                "FINAL_STATES_SNAPSHOT_AGREES_WITH_LIVE"],
         patch=lambda: dict(_FINAL_STATES=[
             (s[0], s[1], "APPROVED_WITH_SPECIFIED_AMENDMENTS", s[3], s[4], True)
             if s[0] == "FS-07" else s for s in D._FINAL_STATES])),
    dict(fid="K-02", title="the answer key state is upgraded to final",
         gates=["ANSWER_KEY_STATE_IS_PROPOSED_NOT_FINAL",
                "ONE_CLASS_IS_FROZEN_BUT_NOT_SETTLED"],
         patch=lambda: dict(_FINAL_STATES=[
             (s[0], s[1], "APPROVED_WITH_SPECIFIED_AMENDMENTS", s[3], s[4], True)
             if s[0] == "FS-08" else s for s in D._FINAL_STATES])),
    dict(fid="K-03", title="a final state is dropped so nine remain",
         gates=["TEN_FINAL_STATES"],
         patch=lambda: dict(_FINAL_STATES=D._FINAL_STATES[:-1])),
    dict(fid="K-04", title="E-01 to E-04 are closed without authority",
         gates=["E02_AND_E04_ARE_NOT_CLOSED", "FOUR_ITEMS_STAY_OPEN_AFTER_THIS_STAGE"],
         patch=lambda: dict(OPEN_AFTER_THIS_STAGE=[
             o for o in D.OPEN_AFTER_THIS_STAGE
             if o["open_id"] not in ("E-02", "E-04")])),
    dict(fid="K-05", title="an open item is left with no owner",
         gates=["EVERY_OPEN_ITEM_NAMES_AN_OWNER"],
         patch=lambda: dict(OPEN_AFTER_THIS_STAGE=[
             dict(o, owner="") for o in D.OPEN_AFTER_THIS_STAGE])),
    dict(fid="K-06", title="a forbidden production label is applied to a live record",
         gates=["FORBIDDEN_LABELS_ABSENT_FROM_EVERY_RECORD"],
         patch=_vis(lambda v: v.update(status="PRODUCTION_APPROVED"))),
    dict(fid="K-07", title="the forbidden-label declaration is emptied",
         gates=["FORBIDDEN_LABEL_DECLARATION_INTACT"],
         patch=lambda: dict(FORBIDDEN_LABELS=[])),
    dict(fid="K-08", title="a verdict outside the allowed set is adopted",
         gates=["VERDICT_IS_FROM_THE_ALLOWED_SET"],
         patch=lambda: dict(VERDICT="T04_PRODUCTION_APPROVED")),
    dict(fid="K-09", title="CAIR is named the Instructional Designer",
         gates=["CAIR_NOT_NAMED_INSTRUCTIONAL_DESIGNER"],
         patch=_vis(lambda v: v.update(
             what_is_not_approved="CAIR acts as instructional designer for the asset set."))),
    dict(fid="K-10", title="a deciding record is attributed to someone other than Bariah",
         gates=["EVERY_AUTHORITY_ACT_IS_BARIAHS"],
         patch=_reg(lambda r: _find(r, "decision_id", "T04-DEC-B05").update(
             authority="FIRDAUS"))),

    # ================= production guards =================
    dict(fid="L-01", title="a PPTX is recorded as generated in this stage",
         gates=["NO_PPTX_GENERATED"], patch=lambda: dict(PPTX_GENERATED=1)),
    dict(fid="L-02", title="the production generator is recorded as touched",
         gates=["PRODUCTION_GENERATOR_UNTOUCHED"], patch=lambda: dict(GENERATOR_TOUCHED=1)),
    dict(fid="L-03", title="MMD production is recorded as started",
         gates=["NO_MMD_PRODUCTION_STARTED"], patch=lambda: dict(MMD_PRODUCTION_STARTED=1)),
    dict(fid="L-04", title="an authority artifact is recorded as modified",
         gates=["AUTHORITY_ARTIFACTS_NOT_MODIFIED"],
         patch=lambda: dict(AUTHORITY_ARTIFACTS_MODIFIED=1)),

    # ================= reconciliation and reporting =================
    dict(fid="M-01", title="a stale fact loses the decision that superseded it",
         gates=["EVERY_STALE_FACT_NAMES_ITS_DECISION"],
         patch=lambda: dict(SUPERSEDED_FACTS=[
             dict(f, decision_id="T04-DEC-ZZ") for f in D.SUPERSEDED_FACTS])),
    dict(fid="M-02", title="a stale fact is removed from the reconciliation list",
         gates=["SEVEN_STALE_FACTS_NAMED"],
         patch=lambda: dict(SUPERSEDED_FACTS=D.SUPERSEDED_FACTS[:-1])),
    dict(fid="M-03", title="a superseded artifact stops pointing at its replacement",
         gates=["EVERY_SUPERSEDED_ARTIFACT_POINTS_AT_ITS_REPLACEMENT"],
         patch=lambda: dict(SUPERSEDED_ARTIFACTS=[
             dict(s, superseded_by="") for s in D.SUPERSEDED_ARTIFACTS])),
    dict(fid="M-04", title="a superseded artifact names a replacement that does not exist",
         gates=["EVERY_REPLACEMENT_ARTIFACT_EXISTS"],
         patch=lambda: dict(SUPERSEDED_ARTIFACTS=[
             dict(s, superseded_by="docs/pl06/t04/T04_DOES_NOT_EXIST.json")
             for s in D.SUPERSEDED_ARTIFACTS])),
    dict(fid="M-05", title="a declared artifact is never emitted",
         gates=["EVERY_DECLARED_ARTIFACT_WAS_EMITTED", "TWENTY_FOUR_ARTIFACTS_DECLARED"],
         patch=lambda: dict(NEW_ARTIFACTS=D.NEW_ARTIFACTS + ["T04_PHANTOM_v1.json"])),
    dict(fid="M-06", title="the NOT_CHECKED list is emptied", target="QA",
         gates=["NOT_CHECKED_IS_PUBLISHED", "NOT_CHECKED_NAMES_THE_UNRESOLVED_Q3",
                "NOT_CHECKED_NAMES_THE_OPEN_ROUND_TRIP"],
         patch=lambda: dict(NOT_CHECKED=[])),
    dict(fid="M-07", title="the suite identity is lost", target="QA",
         gates=["SUITE_ID_DECLARED"], patch=lambda: dict(SUITE_ID="")),
    dict(fid="M-08", title="the suite adopts the prior suite's identity", target="QA",
         gates=["SUITE_ID_DECLARED", "SUITE_ID_DIFFERS_FROM_THE_PRIOR_SUITE"],
         patch=lambda: dict(SUITE_ID=QA.PRIOR_SUITE_ID)),
    dict(fid="M-09", title="the supersession marker set is emptied so any stale claim passes",
         target="QA",
         gates=["SUPERSESSION_MARKER_SET_IS_NOT_EMPTY",
                "NO_EMITTED_ARTIFACT_ASSERTS_A_STALE_FACT_AS_CURRENT"],
         patch=lambda: dict(SUPERSESSION_MARKERS=())),

    # ================= on-disk artifact mutations =================
    dict(fid="N-01", title="a stale 21-screen claim is written into the emitted sequence",
         gates=["NO_EMITTED_ARTIFACT_ASSERTS_A_STALE_FACT_AS_CURRENT"],
         **_disk("T04_FINAL_SCREEN_SEQUENCE_v2.md",
                 "# 2. The sequence",
                 "# 2. The sequence\n\nJumlah akhir ialah 21 skrin.")),
    dict(fid="N-02", title="the old fertiliser distractor is reinstated in the emitted quiz",
         gates=["NO_EMITTED_ARTIFACT_ASSERTS_A_STALE_FACT_AS_CURRENT"],
         **_disk("T04_FINAL_QUIZ_v2.md",
                 "# 3. Which route was taken, and who chose",
                 "Pilihan tambahan: Baja disimpan di tempat yang kering dan jauh dari "
                 "sumber air.\n\n# 3. Which route was taken, and who chose")),
    dict(fid="N-03", title="the NOT_SUPPLIED disclosure is deleted from the emitted register",
         gates=["SUPPLEMENTARY_LIMITATION_STATED_IN_THE_MARKDOWN"],
         **_disk("T04_AUTHORITY_EVIDENCE_REGISTER_v1.md", "NOT_SUPPLIED",
                 "tidak berkenaan", count=0)),
]


def _find_row(rows, did):
    return next(r for r in rows if r[0] == did)


def _run_suite():
    return {r["gate_id"]: r["ok"] for r in QA.run()}


def run_fixture(f):
    if "_disk" in f:
        name, old, new, count = f["_disk"]
        path = os.path.join(T04, name)
        with open(path, "rb") as fh:
            original = fh.read()
        text = original.decode("utf-8")
        if old not in text:
            return {"__EXCEPTION__": False, "__MSG__": f"anchor not found in {name}"}
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text.replace(old, new) if count == 0
                         else text.replace(old, new, count))
            return _run_suite()
        except Exception as exc:
            return {"__EXCEPTION__": False, "__MSG__": str(exc)}
        finally:
            with open(path, "wb") as fh:
                fh.write(original)

    tgt = TARGETS[f.get("target", "D")]
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


def _digests():
    out = {}
    for n in D.NEW_ARTIFACTS:
        p = os.path.join(T04, n)
        if os.path.exists(p):
            with open(p, "rb") as f:
                out[n] = hashlib.sha256(f.read()).hexdigest()
    return out


def main():
    before = _digests()
    good = _run_suite()
    out = []
    for f in FIXTURES:
        res = run_fixture(f)
        det = ("__EXCEPTION__" in res) or any(res.get(g) is False for g in f["gates"])
        fired = [g for g in f["gates"] if res.get(g) is False] or (
            ["<suite exception>"] if "__EXCEPTION__" in res else [])
        out.append(dict(fixture_id=f["fid"], title=f["title"],
                        target=("DISK" if "_disk" in f else f.get("target", "D")),
                        designated_gates=f["gates"], detected=det, fired=fired,
                        note=res.get("__MSG__")))
    after = _digests()
    return dict(suite_id=QA.SUITE_ID,
                baseline_pass=sum(1 for v in good.values() if v),
                baseline_total=len(good),
                baseline_false_failures=sorted(g for g, ok in good.items() if not ok),
                fixture_count=len(out),
                detected=sum(1 for r in out if r["detected"]),
                missed=sorted(r["fixture_id"] for r in out if not r["detected"]),
                skipped=[],
                post_run_restored=(before == after),
                by_target={t: sum(1 for r in out if r["target"] == t)
                           for t in sorted({r["target"] for r in out})},
                fixtures=out)


if __name__ == "__main__":
    r = main()
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(1 if (r["missed"] or r["baseline_false_failures"]
                   or not r["post_run_restored"]) else 0)
