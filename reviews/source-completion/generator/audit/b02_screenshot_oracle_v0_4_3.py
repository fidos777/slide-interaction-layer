# -*- coding: utf-8 -*-
"""Stage 4.2C screenshot oracle — expected values tied to the frozen Bariah screenshots.

This module deliberately imports NOTHING from the generator, the visual policy, the
glossary or the instruction registry, so no gate built on it compares a value with itself.

The three screenshots are raster images; there is no text layer to parse. The expected
values below are therefore TRANSCRIBED from the frozen bytes, and each record names the
pixel crop it was read from so the reading can be re-checked independently.

The coupling to the evidence is enforced, not asserted: every accessor first re-hashes the
file on disk and raises if it does not match the digest recorded at freeze time. If the
evidence is edited, replaced or removed, every gate built on this module fails closed
rather than silently validating against a stale transcription.

Evidence class for all three: BARIAH_DIRECT_SCREENSHOT.
Provenance: WhatsApp thread, 1 August 2026, 4:37 PM / 4:39 PM / 4:40 PM.
"""
import hashlib, os

HERE = os.path.dirname(os.path.abspath(__file__))
EVID = os.path.abspath(os.path.join(HERE, "..", "..", "..",
                                    "storyboard-bariah", "v0_3_bariah_review"))

S01_JPG = os.path.join(EVID, "B02_BARIAH_S01_EVIDENCE.jpg")
PERSISIR_JPG = os.path.join(EVID, "B02_BARIAH_STRUKTUR_PERSISIR_EVIDENCE.jpg")
POLICY_PNG = os.path.join(EVID, "B02_BARIAH_VISUAL_POLICY_EVIDENCE.png")

FROZEN = {
    S01_JPG: ("7e59a0e882c1de063f9e86ee16ea1ed079ad6bdbf95ce4998d76636b943bbff0", 96289,
              "PHOTO-2026-08-01-16-39-06.jpg", "2026-08-01 16:39"),
    PERSISIR_JPG: ("936b78c270274874bfa4921a35205e4ca1d679959ebf6f1880e7c76e6f890ab7", 53895,
                   "PHOTO-2026-08-01-16-40-33.jpg", "2026-08-01 16:40"),
    POLICY_PNG: ("feb29e86228b7f240379b9830bbd59f3e30db2fae03389a68e1ba1bd32ef867b", 655935,
                 "Screenshot 2026-08-01 at 5.21.12 PM.png", "2026-08-01 16:37"),
}

EVIDENCE_CLASS = "BARIAH_DIRECT_SCREENSHOT"


class ScreenshotEvidenceError(RuntimeError):
    """Frozen screenshot bytes are missing or no longer match. Fail closed."""


def verify(path):
    """Re-hash the evidence and return its frozen identity. Raises if anything differs."""
    want, size, original, captured = FROZEN[path]
    if not os.path.exists(path):
        raise ScreenshotEvidenceError(f"frozen screenshot missing: {path}")
    data = open(path, "rb").read()
    got = hashlib.sha256(data).hexdigest()
    if len(data) != size or got != want:
        raise ScreenshotEvidenceError(
            f"{os.path.basename(path)}: expected {size} B / {want}, found {len(data)} B / {got}")
    return dict(path=path, sha256=got, bytes=len(data), original_filename=original,
                captured=captured, evidence_class=EVIDENCE_CLASS)


def verify_all():
    return [verify(p) for p in (S01_JPG, PERSISIR_JPG, POLICY_PNG)]


# ---------------------------------------------------------------- 4:37 PM — visual policy
def visual_policy_ruling():
    verify(POLICY_PNG)
    return dict(
        crop="(40,10)-(720,120) of B02_BARIAH_VISUAL_POLICY_EVIDENCE.png",
        text="Semua contoh ada visual. Semua pop up ada visual, "
             "KECUALI pop up Spesifikasi (bahan, dimensi etc)",
        # The ruling names two populations and one exception. It carries no qualifier such as
        # "where an example visual is presented"; the Stage 4.2B qualifier is superseded.
        examples_require_visual=True,
        popups_require_visual=True,
        specification_popup_excepted=True,
        qualifier=None,
    )


# ---------------------------------------------------------------- 4:39 PM — S01
def s01_ruling():
    verify(S01_JPG)
    return dict(
        crop_titles="(60,135)-(580,245)",
        crop_visual="(60,275)-(580,345)",
        crop_notes_after="(580,510)-(977,580)",
        crop_annotations="(580,285)-(977,360)",
        # (1) the page title band becomes the full Topik/Bahagian line
        display_title="Topik 3 Bahagian 2: Komponen Landskap",
        # (2) the standalone in-slide "Komponen Landskap" heading is struck out: "Remove"
        standalone_component_title_removed=True,
        annotations=["(1) Komponen Landskap – Tukar kepada "
                     "Topik 3 Bahagian 2: Komponen Landskap",
                     "(2) Komponen Landskap - Remove"],
        # body copy, in order, on her corrected canvas
        canvas_lines=["KURSUS KERJA BANGUNAN – PEMBINAAN LANDSKAP LUAR",
                      "PL06: Pengurusan Operasi Pembinaan Landskap",
                      "Topik 3 Bahagian 2: Komponen Landskap"],
        visual_heading="ARAHAN VISUAL — SPESIFIKASI SAHAJA",
        visual_direction="[Visual: Imej pembuka bahagian — foto tapak landskap siap yang "
                         "memaparkan struktur taman dan perabot taman dalam satu bingkai. "
                         "Tidak dibenamkan.]",
        button="MULA",
        # Speaker Notes: the grey block is the current build, the boxed block is the target.
        spoken_before=["Pakej Latihan 06: Pengurusan Operasi Pembinaan Landskap.",
                       "Topik 3 Bahagian 2: Komponen Landskap.",
                       "Dalam bahagian ini, anda akan mempelajari tentang komponen landskap.",
                       "Klik Mula untuk meneruskan."],
        spoken_after=["PL06: Pengurusan Operasi Pembinaan Landskap.",
                      "Topik 3 Bahagian 2: Komponen Landskap.",
                      "Klik butang “Mula” untuk memulakan pembelajaran."],
        removed_sentence="Dalam bahagian ini, anda akan mempelajari tentang komponen landskap.",
        # SUPERSEDED at Stage 4.2E-B. spoken_after above remains the faithful transcription of
        # THIS image, whose lines 1-2 were read as ending in a full stop at MEDIUM punctuation
        # confidence. Bariah's later ruling (D3, 1 Aug 7:03 PM, "Buang noktah") removes them.
        # The transcription is not rewritten; the current expected form is carried separately.
        spoken_after_current=["PL06: Pengurusan Operasi Pembinaan Landskap",
                              "Topik 3 Bahagian 2: Komponen Landskap",
                              "Klik butang “Mula” untuk memulakan pembelajaran."],
        spoken_after_superseded_by="D3 — B02_BARIAH_DECISION_CAST_QUIZ_VO_PUNCTUATION.png",
        # Reading limit, recorded rather than hidden: at the resolution of the boxed block a
        # trailing full stop on lines 1 and 2 is consistent with the pixels but not separable
        # from the spell-check underline beneath it. The sentence-final period is carried over
        # from the unambiguous "before" block, whose every line ends in one.
        transcription_limits=["trailing '.' on spoken_after lines 1-2 is at raster limit"],
    )


# ---------------------------------------------------------------- 4:40 PM — Struktur Persisir
def struktur_persisir_ruling():
    verify(PERSISIR_JPG); verify(POLICY_PNG)
    return dict(
        crop_visual="(60,425)-(600,480) of B02_BARIAH_STRUKTUR_PERSISIR_EVIDENCE.jpg",
        crop_caption="(40,1200)-(850,1245) of B02_BARIAH_VISUAL_POLICY_EVIDENCE.png",
        screen_title="Struktur Taman",
        component_heading="Struktur Persisir Air",
        annotation="Skrin: Tambahan Text",
        active_visual_direction="[Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]",
        # Her corrected component-main shows this direction and no other. The Rajah 23 /
        # Boardwalk string that the annotated v0.3 deck carried at component-main level is
        # therefore superseded AT THAT LEVEL. It remains the Boardwalk example row's own
        # source-attested direction, which this screenshot does not touch.
        superseded_component_main_direction=(
            "[Visual: Rajah 23 — Contoh Boardwalk dalam Taman Paya Bakau, "
            "modul ms 239. Tidak dibenamkan.]"),
        # The caption is qualified. It authorises the PRINCIPLE for other component mains,
        # not the CONTENT of any of them, so the other eight stay a human decision.
        propagation_caption="Slide 5 - apply to yang lain where applicable/necessary",
        propagation_is_qualified=True,
        authorises_content_for_other_component_mains=False,
    )


if __name__ == "__main__":
    import json
    print(json.dumps(dict(evidence=verify_all(),
                          visual_policy=visual_policy_ruling(),
                          s01=s01_ruling(),
                          struktur_persisir=struktur_persisir_ruling()),
                     ensure_ascii=False, indent=1))
