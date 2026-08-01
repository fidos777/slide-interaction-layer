# -*- coding: utf-8 -*-
"""Stage 4.2E-A decision oracle — the three frozen Bariah decision screenshots of
1 August 2026, 6:48 PM / 6:52 PM / 7:03 PM.

Same contract as b02_screenshot_oracle_v0_4_3: imports nothing from the generator, the
model, the visual policy, the glossary or the instruction registry; re-hashes each image
before returning a value; raises rather than passing if the evidence changes.

These are raster images with no text layer. Every value below is TRANSCRIBED from the frozen
bytes and names the crop it was read from.

The package also shipped DECISION_SUMMARY.md. It is recorded here as SUPPLEMENTARY
NAVIGATION ONLY and is NOT an oracle. Where it differs from the screenshots the screenshots
govern; one such difference is recorded in SUMMARY_DIVERGENCES.
"""
import hashlib, os

HERE = os.path.dirname(os.path.abspath(__file__))
EVID = os.path.abspath(os.path.join(HERE, "..", "..", "..",
                                    "storyboard-bariah", "v0_3_bariah_review"))

TAMBAHAN = os.path.join(EVID, "B02_BARIAH_DECISION_TAMBAHAN_TEXT.png")
PERSISTENCE = os.path.join(EVID, "B02_BARIAH_DECISION_VISUAL_PERSISTENCE.png")
CAST_QUIZ = os.path.join(EVID, "B02_BARIAH_DECISION_CAST_QUIZ_VO_PUNCTUATION.png")

EVIDENCE_CLASS = "BARIAH_DIRECT_SCREENSHOT"

FROZEN = {
    TAMBAHAN: ("e425f5ae00dd556e0295913e8837e5784bf8ff1fb53a208ae88dbc0756a92016", 213065,
               "Screenshot 2026-08-01 at 6.48.45 PM.png", "2026-08-01 18:48", "D1"),
    PERSISTENCE: ("8b4defe1eecb67c2438acb01b1204a025a64ebe848356715b94116d12f7bc3f2", 205072,
                  "Screenshot 2026-08-01 at 6.53.55 PM.png", "2026-08-01 18:52", "D2"),
    CAST_QUIZ: ("d855d5f8e53679beb78feb8aacd4e231b9fde0f52148501acd518039da2eb26b", 567168,
                "Screenshot 2026-08-01 at 7.06.09 PM.png", "2026-08-01 19:03", "D3"),
}

TRANSPORT_ZIP = dict(name="B02_BARIAH_DECISIONS_20260801_1906.zip", bytes=960602,
                     sha256="0eaf79fa3bf57a1685f9a0982a43f9c147d28f8fd1fb12bcf244c1317ddd0b92")

SUMMARY_IS_ORACLE = False
SUMMARY_DIVERGENCES = [dict(
    field="Slide 5 Asas Pembinaan bullets",
    screenshot="no trailing full stop on either bullet",
    summary="both bullets end in a full stop",
    resolution="the screenshot governs; bullets carry no trailing full stop",
    locator="B02_BARIAH_DECISION_TAMBAHAN_TEXT.png crop (30,560)-(800,670)")]


class DecisionEvidenceError(RuntimeError):
    """Frozen decision screenshot missing or changed. Fail closed."""


def verify(path):
    want, size, original, captured, eid = FROZEN[path]
    if not os.path.exists(path):
        raise DecisionEvidenceError(f"frozen decision screenshot missing: {path}")
    data = open(path, "rb").read()
    got = hashlib.sha256(data).hexdigest()
    if len(data) != size or got != want:
        raise DecisionEvidenceError(
            f"{os.path.basename(path)}: expected {size} B / {want}, found {len(data)} B / {got}")
    return dict(evidence_id=eid, path=path, sha256=got, bytes=len(data),
                original_filename=original, captured=captured,
                evidence_class=EVIDENCE_CLASS)


def verify_all():
    return [verify(p) for p in (TAMBAHAN, PERSISTENCE, CAST_QUIZ)]


# ------------------------------------------------------- D1, 6:48 PM — Tambahan Text
def tambahan_text_ruling():
    verify(TAMBAHAN)
    return dict(
        evidence_id="D1", captured="2026-08-01 18:48",
        crop_question="(30,20)-(820,190)", crop_answer="(30,490)-(800,670)",
        question_ms=("Label “Skrin: Tambahan Text” bermaksud tambahan kandungan pada skrin yang "
                     "sama, atau perlu diwujudkan satu skrin learner baharu?"),
        answer_verbatim="Slide 5 (tambahan text pada skrin sama, to follow VO) - yg ni:",
        target_screen_label="Slide 5",
        new_learner_screen=False,
        content_follows_vo=True,
        heading="Asas Pembinaan",
        bullets=["Asas stabil dan rata, dengan sistem saliran permukaan berkesan untuk "
                 "mengelakkan genangan air",
                 "Pemilihan bahan permukaan bergantung pada fungsi utama"],
        bullets_carry_trailing_full_stop=False,
        transcription_confidence="HIGH",
        punctuation_confidence="HIGH",
    )


# ------------------------------------------------- D2 + D3, 6:52 / 7:03 PM — visuals
def visual_ruling():
    verify(PERSISTENCE); verify(CAST_QUIZ)
    return dict(
        evidence_id="D2 (+ D3 for persistence)", captured="2026-08-01 18:52 / 19:03",
        crop_answer="(30,470)-(830,590) of B02_BARIAH_DECISION_VISUAL_PERSISTENCE.png",
        crop_persistence="(40,1120)-(860,1400) of "
                         "B02_BARIAH_DECISION_CAST_QUIZ_VO_PUNCTUATION.png",
        answer_1_verbatim="Soalan 1: Component-main - Visual diperlukan",
        answer_2_verbatim=("Soalan 2: Pop up - visual diperlukan. Kemungkinan visual di "
                           "component main, saiznya lebih kecil dan ada banyak visual lain. "
                           "Jadi di pop up, visual nya lebih besar dan fokus. Kan?"),
        persistence_verbatim=("Untuk all-viewed dan return state, kita kekalkan semula visual "
                              "overview component-main yang sama - ya, betul"),
        persistence_message_direction=("incoming — left-aligned white bubble in the "
                                       "'Bariah eLearning' thread, replying to a quoted "
                                       "'You' message"),
        component_main_visual="REQUIRED",
        component_main_treatment="SEVERAL_SMALLER_VISUALS_AS_OVERVIEW",
        example_or_information_popup_visual="REQUIRED",
        popup_visual_treatment="LARGE_FOCUSED",
        specification_popup_visual="NOT_REQUIRED",
        specification_popup_authority=("unchanged from the 4:37 PM ruling 'KECUALI pop up "
                                       "Spesifikasi'; D2 does not reopen it"),
        all_viewed_persistence="REQUIRED",
        return_state_persistence="REQUIRED",
        transcription_confidence="HIGH",
        punctuation_confidence="HIGH",
    )


# ------------------------------------------------- D3, 7:03 PM — cast / quiz / VO / S01
def cast_ruling():
    verify(CAST_QUIZ)
    return dict(evidence_id="D3", captured="2026-08-01 19:03", crop="(60,750)-(900,830)",
                question_ms="Adakah pasangan watak B02 yang diluluskan ialah Alya dan "
                            "Encik Rahman?",
                answer_verbatim="Yes lulus. Boleh diguna pakai di Bahagian/Topik/PL lain jika "
                                "bersesuaian",
                approved=True, pair=["Alya", "Encik Rahman"],
                reuse_policy="APPROVED_WHERE_CONTEXTUALLY_APPROPRIATE",
                reuse_scope=["Bahagian", "Topik", "PL"],
                reuse_is_conditional=True,
                transcription_confidence="HIGH")


def quiz_ruling():
    verify(CAST_QUIZ)
    return dict(evidence_id="D3", captured="2026-08-01 19:03", crop="(60,830)-(900,960)",
                question_ms="Rationale jawapan perlu diletakkan dalam production metadata, "
                            "Speaker Notes, atau learner feedback selepas penghantaran?",
                answer_verbatim=("Rationale jawapan, hanya maklum balas: Pilihan jawapan tepat. "
                                 "/ Pilihan jawapan tidak tepat. - production metadata, learner "
                                 "feedback selepas penghantaran. Speaker Notes tidak perlu."),
                correct_feedback="Pilihan jawapan tepat.",
                incorrect_feedback="Pilihan jawapan tidak tepat.",
                feedback_strings_carry_trailing_full_stop=True,
                production_metadata=True,
                learner_feedback_after_submission=True,
                speaker_notes=False,
                transcription_confidence="HIGH", punctuation_confidence="HIGH")


def micro_control_vo_ruling():
    verify(CAST_QUIZ)
    return dict(evidence_id="D3", captured="2026-08-01 19:03", crop="(60,960)-(900,1000)",
                question_ms=("Selain arahan screen-level “Klik pada setiap…”, adakah arahan "
                             "untuk Tutup, Kembali, Semak Jawapan dan Ulang Kuiz juga perlu "
                             "disebut dalam VO?"),
                answer_verbatim='Tidak. VO cuma arahan screen level "Klik pada setiap ...',
                screen_level_click_vo="REQUIRED",
                micro_control_vo="NOT_REQUIRED",
                micro_controls=["Tutup", "Kembali", "Semak Jawapan", "Ulang Kuiz",
                                "close icon instructions", "other micro-controls"],
                transcription_confidence="HIGH")


def s01_punctuation_ruling():
    verify(CAST_QUIZ)
    return dict(evidence_id="D3", captured="2026-08-01 19:03", crop="(60,1000)-(900,1090)",
                question_ms="Mohon sahkan penggunaan tanda noktah pada dua baris Speaker "
                            "Notes S01.",
                answer_verbatim="Buang noktah - yang ni kan -",
                lines_quoted_without_full_stop=["PL06: Pengurusan Operasi Pembinaan Landskap",
                                                "Topik 3 Bahagian 2: Komponen Landskap"],
                line_1_trailing_period=False,
                line_2_trailing_period=False,
                line_3_unchanged="Klik butang “Mula” untuk memulakan pembelajaran.",
                line_3_trailing_period=True,
                line_3_note="not mentioned in the ruling; the earlier HIGH-confidence reading "
                            "of S1-e stands and its full stop is retained",
                notes_block_count=3,
                transcription_confidence="HIGH", punctuation_confidence="HIGH")


if __name__ == "__main__":
    import json
    print(json.dumps(dict(evidence=verify_all(), transport=TRANSPORT_ZIP,
                          summary_is_oracle=SUMMARY_IS_ORACLE,
                          summary_divergences=SUMMARY_DIVERGENCES,
                          tambahan_text=tambahan_text_ruling(), visual=visual_ruling(),
                          cast=cast_ruling(), quiz=quiz_ruling(),
                          micro_control_vo=micro_control_vo_ruling(),
                          s01_punctuation=s01_punctuation_ruling()),
                     ensure_ascii=False, indent=1))
