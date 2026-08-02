# -*- coding: utf-8 -*-
"""Stage 4.2E-B cardinality oracle — the frozen Bariah overview-cardinality ruling,
2 August 2026, 8:24 AM.

Same contract as the other oracles: imports nothing from the generator, the model, the
visual policy, the glossary or the instruction registry; re-hashes the evidence before
returning a value; raises rather than passing if the bytes change.

Raster image, no text layer. Every value is TRANSCRIBED from a named pixel crop.
MANIFEST.txt is supplementary only and is not an oracle.

The reply is read ONLY against the two option blocks visible in the same screenshot.
"""
import hashlib, os

HERE = os.path.dirname(os.path.abspath(__file__))
EVID = os.path.abspath(os.path.join(HERE, "..", "..", "..",
                                    "storyboard-bariah", "v0_3_bariah_review"))
CARD = os.path.join(EVID, "B02_BARIAH_DECISION_OVERVIEW_CARDINALITY_20260802.png")

EVIDENCE_CLASS = "BARIAH_DIRECT_SCREENSHOT"
FROZEN = {CARD: ("f46c2a371b93ebadc6e4bf99c619bf52621d7bc29421ebd36205f6ed6ec5ef64", 757585,
                 "Screenshot 2026-08-02 at 9.04.34 AM.png", "2026-08-02 08:24",
                 (1172, 1538), "D4")}
TRANSPORT_ZIP = dict(name="B02_OVERVIEW_CARDINALITY_EVIDENCE_20260802.zip", bytes=744564,
                     sha256="d45f0b2e45c7b6efc73334f20f895ac0046ee954524fee2a0ce7997effc418c9")
SUMMARY_IS_ORACLE = False


class CardinalityEvidenceError(RuntimeError):
    """Frozen cardinality screenshot missing or changed. Fail closed."""


def verify(path=CARD):
    want, size, original, captured, dims, eid = FROZEN[path]
    if not os.path.exists(path):
        raise CardinalityEvidenceError(f"frozen cardinality screenshot missing: {path}")
    data = open(path, "rb").read()
    got = hashlib.sha256(data).hexdigest()
    if len(data) != size or got != want:
        raise CardinalityEvidenceError(
            f"{os.path.basename(path)}: expected {size} B / {want}, found {len(data)} B / {got}")
    return dict(evidence_id=eid, path=path, sha256=got, bytes=len(data),
                original_filename=original, captured=captured, dimensions=list(dims),
                evidence_class=EVIDENCE_CLASS)


def verify_all():
    return [verify(CARD)]


def reply():
    verify()
    return dict(evidence_id="D4", captured="2026-08-02 08:24",
                crop="(40,1355)-(780,1415)",
                verbatim="Yup, papan tanda Pilihan A, ok bbq pit 1 gamba",
                note=("The final word renders as 'gamba' — colloquial Malay for 'gambar'. "
                      "It is transcribed exactly as shown and is unambiguous in meaning: "
                      "one image."),
                transcription_confidence="HIGH", punctuation_confidence="HIGH")


def papan_tanda_ruling():
    verify()
    return dict(
        evidence_id="D4", captured="2026-08-02 08:24",
        crop_options="(370,420)-(960,800)", crop_reply="(40,1355)-(780,1415)",
        question_ms=("Untuk skrin utama Papan Tanda, ada dua visual sumber: 1. Papan Tanda "
                     "Informasi 2. Papan Tanda Penunjuk Arah. Adakah kedua-dua visual ini "
                     "perlu dipaparkan sebagai overview pada skrin utama, atau gunakan satu "
                     "visual sahaja?"),
        options={"A": "Paparkan kedua-dua visual", "B": "Paparkan satu visual sahaja"},
        selected_option="A",
        selected_option_text="Paparkan kedua-dua visual",
        overview_visual_count=2,
        overview_subjects=["Papan Tanda Informasi", "Papan Tanda Penunjuk Arah"],
        subject_names_are_figure_bound=True,
        # Guard: the row LABEL uses "Interpretatif"; the FIGURES use "Informasi". The ruling
        # selects the figure-bound names. No global terminology equivalence is created.
        informasi_equals_interpretatif_global_rule=False,
        collapse_into_one_subject_permitted=False,
        status="RESOLVED_BY_BARIAH",
        transcription_confidence="HIGH")


def bbq_pit_ruling():
    verify()
    return dict(
        evidence_id="D4", captured="2026-08-02 08:24",
        crop_options="(370,820)-(990,1200)", crop_reply="(40,1355)-(780,1415)",
        question_ms=("Untuk skrin utama BBQ Pit, modul hanya mempunyai satu visual sumber. "
                     "Adakah dibenarkan skrin overview menggunakan satu visual sahaja untuk "
                     "komponen ini?"),
        options={"A": "Ya, satu visual dibenarkan kerana source hanya satu",
                 "B": "Perlu visual kedua — nyatakan subject yang dikehendaki"},
        selected_option="A",
        selected_option_text="Ya, satu visual dibenarkan kerana source hanya satu",
        reply_fragment="ok bbq pit 1 gamba",
        overview_visual_count=1,
        overview_subject="existing frozen source-bound BBQ Pit figure",
        duplicate_visual_permitted=False,
        invented_second_subject_permitted=False,
        specification_categories_as_visuals_permitted=False,
        location_text_as_visual_subject_permitted=False,
        cross_component_borrow_permitted=False,
        status="RESOLVED_BY_BARIAH",
        transcription_confidence="HIGH")


def cardinality_rule():
    verify()
    return dict(
        rule=("If a component has multiple distinct source-bound visual subjects, display the "
              "approved multiple subjects as smaller overview visuals. If a component has only "
              "one defensible source-bound visual subject, a single-visual component-main "
              "overview is permitted. No additional visual may be invented merely to satisfy "
              "the word 'several'."),
        supported_by=["D2 6:52 PM overview-treatment ruling",
                      "D4 Papan Tanda Pilihan A selection",
                      "D4 BBQ Pit one-image exception"],
        MINIMUM_OVERVIEW_CARDINALITY=1,
        CARDINALITY_SOURCE_DERIVED=True,
        INVENTED_SUBJECTS_TO_REACH_MINIMUM=0,
        UNIVERSAL_FIXED_CARD_COUNT=False,
        not_a_licence_to_reduce=("This does not permit reducing a component that already has "
                                 "multiple approved source-bound subjects."))


if __name__ == "__main__":
    import json
    print(json.dumps(dict(evidence=verify_all(), transport=TRANSPORT_ZIP,
                          summary_is_oracle=SUMMARY_IS_ORACLE, reply=reply(),
                          papan_tanda=papan_tanda_ruling(), bbq_pit=bbq_pit_ruling(),
                          cardinality_rule=cardinality_rule()),
                     ensure_ascii=False, indent=1))
