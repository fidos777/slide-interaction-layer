# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.9 — T04 authority decision ingestion and content freeze.

WHAT THIS MODULE IS
-------------------
The single controlled source for every decision Bariah recorded in the annotated review
package `T04_Pakej_Semakan_Bariah_v3_vBariah.docx`, plus the three WhatsApp confirmations
Firdaus relayed. Every artifact this stage emits is projected from here. Nothing is typed
into a Markdown file that does not exist as a record in this module.

WHAT IT IS NOT
--------------
It is not an approval of anything Bariah did not decide. Three classes of content are
explicitly NOT frozen and say so in their own records:

  * the Q5 option set E/F, which Bariah instructed be changed but did not write;
  * the quiz answer key, which remains a proposal;
  * the "Q3" WhatsApp line, whose referent is ambiguous and is recorded as ambiguous.

AUTHORITY WORDING
-----------------
Where Bariah's written wording is carried into a controlled record it is quoted verbatim in
`authority_quote`. Where a correction was applied, `AUTHORITY_WORDING_CORRECTIONS` records
the correction as-written, as-applied, its basis and its confirmation status. No correction
is applied silently.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)

import t04_content_data_v1 as C          # noqa: E402  Stage 4.2F-B0.8 controlled content
import t04_final_rulings_data_v1 as F    # noqa: E402  Stage 4.2F-B0.7 structural rulings

STAGE = "4.2F-B0.9"
SUITE_ID = "T04_AUTHORITY_DECISION_INGESTION_QA_v1"
GENERATED_BY = "docs/pl06/t04/tools/t04_authority_emit_v1.py"

# ==========================================================================================
# UNIT IDENTITY — Bariah ruled that Topik 4 has no Bahagian. The internal ID is unchanged;
# only what the learner is shown changes.
# ==========================================================================================
INTERNAL_UNIT_ID = "K5-PL06-T04-B01"
LEARNER_DISPLAY_UNIT = "Topik 4"
LEARNER_DISPLAY_UNIT_TITLE = "Penjagaan dan Penyelenggaraan"
UNIT_LABEL_RULING = dict(
    ruling_id="T04-LBL-01",
    authority_quote=("Tiada Bahagian bagi Topik 4. Kesemua subtopik di bawah Topik 4 – "
                     "Landskap Lembut dan Landskap Kejur – di dalam 1 storyboard."),
    source_artifact="AUTH-EV-01 §A, keputusan T04-S01",
    internal_unit_id=INTERNAL_UNIT_ID,
    learner_display_unit=LEARNER_DISPLAY_UNIT,
    interpretation=(
        "The learner-facing label is Topik 4 with no Bahagian. The internal unit ID "
        "K5-PL06-T04-B01 is a repository and build identifier and is retained unchanged — "
        "Bariah ruled on what the learner sees, not on internal identifiers."),
    scope="T04 only. No other Topik is affected by this ruling.",
    closes_screen_labels=["T04-S01", "T04-S22"])

# ==========================================================================================
# PART 1 — EVIDENCE HIERARCHY
# ==========================================================================================
EVIDENCE_DIR = "reviews/storyboard-bariah/t04_bariah_review"

EVIDENCE_CLASSES = [
    "PRIMARY_AUTHORITY_EVIDENCE",
    "SUPPLEMENTARY_AUTHORITY_EVIDENCE",
    "CONTROLLED_DECISION_SOURCE",
    "FINAL_BUILD_INPUT",
]

# The primary artifact's identity was verified at ingestion. These values are asserted by a
# gate against the file on disk, not merely recorded here.
PRIMARY_DOCX_NAME = "T04_Pakej_Semakan_Bariah_v3_vBariah.docx"
PRIMARY_DOCX_BYTES = 36105
PRIMARY_DOCX_SHA256 = "2eea2101e8976b17137e3607aa3817aefd56b09bc2f2c397ca0fffef9bb4bd59"

EVIDENCE = [
    dict(
        evidence_id="AUTH-EV-01",
        evidence_class="PRIMARY_AUTHORITY_EVIDENCE",
        filename=PRIMARY_DOCX_NAME,
        frozen_path=EVIDENCE_DIR + "/" + PRIMARY_DOCX_NAME,
        supplied_in_this_run=True,
        byte_size=PRIMARY_DOCX_BYTES,
        sha256=PRIMARY_DOCX_SHA256,
        dimensions_or_extent="16 pages, 4881 words as reported by the package's app.xml",
        authority="Bariah Ahmad — Instructional Designer",
        authored_with="Microsoft Office Word",
        date_authority_recorded="2026-08-03",
        date_review_started="2026-08-02",
        scope=("Every T04 decision in sections A to F: screen sequence, visual scope, Slide 2 "
               "dialogue, Rumusan, quiz and the overall review verdict."),
        authority_quote=("Secara keseluruhan, pakej semakan ini memenuhi keperluan dan boleh "
                         "diluluskan tertakluk kepada pindaan yang telah dinyatakan di setiap "
                         "bahagian."),
        interpretation=(
            "A conditional approval. The package is approved subject to the amendments stated "
            "in each section — so the amendments are part of the approval, not a separate "
            "open question."),
        limitations=(
            "Contains no tracked changes and no Word comments. Every decision is expressed as "
            "a ticked box or as typed text inside the document's own decision fields, which "
            "is how the document was designed to be completed. Handwriting, signature image "
            "and the final written signature field are absent — the signature line is blank; "
            "the reviewer's name and date are typed."),
        provenance_chain=(
            "CAIR generated v2 (12,571 bytes) in Stage 4.2F-B0.8A. Firdaus produced v3 from "
            "v2 in Microsoft Word and issued it to Bariah. Bariah annotated v3. v3 is the "
            "authority artifact; v2 is superseded and is retained only as the generated "
            "predecessor."),
    ),
    dict(
        evidence_id="AUTH-EV-02",
        evidence_class="SUPPLEMENTARY_AUTHORITY_EVIDENCE",
        filename="WhatsApp screenshot dated 3 August 2026",
        frozen_path=None,
        supplied_in_this_run=False,
        byte_size="NOT_SUPPLIED",
        sha256="NOT_SUPPLIED",
        dimensions_or_extent="NOT_SUPPLIED",
        authority="Bariah Ahmad — Instructional Designer, relayed by Firdaus",
        authored_with="WhatsApp",
        date_authority_recorded="2026-08-03",
        date_review_started="2026-08-03",
        scope=("Three short confirmations that sit alongside the DOCX: acceptance of both "
               "screenshot items, the Q5 multiple-response treatment, and one line whose "
               "referent is ambiguous."),
        authority_quote=("Yes to both screenshots | Q5 multiple response - yes, ok | "
                         "Q3 tu nnt u pilih ya"),
        interpretation=(
            "Treated as authority wording, but at a degraded evidence grade. The wording is "
            "second-hand: it reaches this stage as text transcribed into the stage brief, not "
            "as an image this run could open, hash and read."),
        limitations=(
            "THE IMAGE FILE WAS NOT SUPPLIED TO THIS RUN. No byte size, no SHA-256, no pixel "
            "dimensions and no visible message timestamps can be recorded, because there is "
            "no file to measure. They are recorded as NOT_SUPPLIED and are not estimated, "
            "reconstructed or inferred. Any decision resting on this evidence carries "
            "evidence_grade DEGRADED_TRANSCRIBED_NOT_IMAGE_VERIFIED."),
        provenance_chain=(
            "Bariah wrote the messages in WhatsApp. Firdaus transcribed them into the Stage "
            "4.2F-B0.9 brief. This run read the transcription. The image itself was never "
            "available to this run."),
    ),
    dict(
        evidence_id="AUTH-EV-03",
        evidence_class="CONTROLLED_DECISION_SOURCE",
        filename="T04_AUTHORITY_DECISION_REGISTER_v1.json",
        frozen_path="docs/pl06/t04/T04_AUTHORITY_DECISION_REGISTER_v1.json",
        supplied_in_this_run=True,
        byte_size="DERIVED_AT_EMIT",
        sha256="DERIVED_AT_EMIT",
        dimensions_or_extent="DERIVED_AT_EMIT",
        authority="CAIR — derivation only, no independent authority",
        authored_with=GENERATED_BY,
        date_authority_recorded="2026-08-03",
        date_review_started=None,
        scope="Every decision read out of AUTH-EV-01 and AUTH-EV-02, typed and traceable.",
        authority_quote=None,
        interpretation=(
            "A derived artifact. It carries no authority of its own — every record in it "
            "names the evidence object and the quoted wording it came from."),
        limitations=(
            "A derivation can be wrong. Each record therefore carries the verbatim authority "
            "quote it was derived from, so the derivation can be checked against the source "
            "without opening the DOCX."),
        provenance_chain="Projected from t04_authority_data_v1 by " + GENERATED_BY + ".",
    ),
    dict(
        evidence_id="AUTH-EV-04",
        evidence_class="FINAL_BUILD_INPUT",
        filename="T04_FINAL_CONTENT_MODEL_v1.json",
        frozen_path="docs/pl06/t04/T04_FINAL_CONTENT_MODEL_v1.json",
        supplied_in_this_run=True,
        byte_size="DERIVED_AT_EMIT",
        sha256="DERIVED_AT_EMIT",
        dimensions_or_extent="DERIVED_AT_EMIT",
        authority="CAIR — assembly only, under the decisions in AUTH-EV-03",
        authored_with=GENERATED_BY,
        date_authority_recorded="2026-08-03",
        date_review_started=None,
        scope="The content the T04 storyboard build consumes: 22 screens, dialogue, Rumusan, "
              "quiz, visual scope and unit labelling.",
        authority_quote=None,
        interpretation=(
            "The build input. Ten named final states declare, per content class, exactly how "
            "settled that class is — three of them are not settled and say so."),
        limitations=(
            "Frozen means 'no further CAIR change without a new authority decision'. It does "
            "not mean every element is Bariah-approved: the Q5 E/F options and the answer key "
            "are explicitly not."),
        provenance_chain="Projected from t04_authority_data_v1 by " + GENERATED_BY + ".",
    ),
]

EVIDENCE_FIELDS = ["evidence_id", "evidence_class", "filename", "frozen_path",
                   "supplied_in_this_run", "byte_size", "sha256", "dimensions_or_extent",
                   "authority", "authored_with", "date_authority_recorded", "scope",
                   "authority_quote", "interpretation", "limitations", "provenance_chain"]

# What the primary artifact does NOT contain. Stated so no downstream reader assumes a
# review mechanism that was never used.
PRIMARY_ARTIFACT_MECHANISM = dict(
    tracked_changes_present=False,
    tracked_change_element_count=0,
    word_comments_present=False,
    word_comment_count=0,
    comments_part_present=False,
    decision_mechanism="TICKED_DECISION_BOXES_AND_TYPED_TEXT_IN_DOCUMENT_FIELDS",
    note=("The document carries no <w:ins>, <w:del>, <w:rPrChange> or <w:pPrChange> elements "
          "and no word/comments.xml part. Bariah recorded every decision by ticking the "
          "decision boxes and typing into the comment fields the document provides. That is "
          "the mechanism the document was built for, and it is a complete record — but it is "
          "not tracked changes, and this stage does not describe it as tracked changes."),
    counting_trap=("A naive substring count of '<w:ins' returns 12 on this file because it "
                   "also matches the <w:insideH> and <w:insideV> table border elements. The "
                   "count above uses '<w:ins[ >]' and returns 0."))

# ==========================================================================================
# PART 2 — WHATSAPP CONFIRMATION RECORDS
# ==========================================================================================
CONFIRMATION_STATUSES = [
    "CONFIRMED_BY_AUTHORITY",
    "DELEGATED_TO_CAIR_PENDING_BARIAH_CONFIRMATION",
    "AMBIGUOUS_REFERENT_NOT_ACTIONABLE",
    # Added in Stage 4.2F-B0.9.1 when visual inspection showed one recorded "confirmation"
    # was not an authority statement at all.
    "NOT_AN_AUTHORITY_STATEMENT_MISATTRIBUTED_IN_B0_9",
    "RETAINED_FOR_TRACEABILITY_NOT_ACTIONABLE",
]

CONFIRMATIONS = [
    dict(
        confirmation_id="T04-CNF-01",
        evidence_id="AUTH-EV-02",
        authority_quote="Yes to both screenshots",
        also_recorded_as="Yes to both",
        subject="Acceptance of both structural screenshot items put to Bariah",
        status="CONFIRMED_BY_AUTHORITY",
        evidence_grade="DEGRADED_TRANSCRIBED_NOT_IMAGE_VERIFIED",
        interpretation=(
            "Bariah accepted both items she was shown. The confirmation is unambiguous in "
            "polarity — 'yes' — and its scope is 'both screenshots'."),
        what_this_does_not_establish=(
            "Which two screenshots. This run cannot see the WhatsApp thread, so the referents "
            "are named by Firdaus's brief and not independently verified. No T04 content is "
            "changed on the strength of this record alone; every content change in this stage "
            "is carried by the DOCX."),
        applied_to_content=False,
        blocking=False),
    dict(
        confirmation_id="T04-CNF-02",
        evidence_id="AUTH-EV-02",
        authority_quote="Q5 multiple response - yes, ok",
        also_recorded_as=None,
        subject="Q5 remains a Multiple Response item",
        status="CONFIRMED_BY_AUTHORITY",
        evidence_grade="DEGRADED_TRANSCRIBED_NOT_IMAGE_VERIFIED",
        interpretation=(
            "Q5 stays a Multiple Response question. This corroborates — it does not replace — "
            "the DOCX ruling on Q5, which is the operative authority for the item type, the "
            "checkbox presentation and the stem."),
        what_this_does_not_establish=(
            "Anything about the Q5 option set or the answer key. Both are governed by the "
            "DOCX instruction and remain unconfirmed."),
        applied_to_content=True,
        applied_to="QUIZ-Q5 item_type",
        blocking=False),
    dict(
        confirmation_id="T04-CNF-03",
        evidence_id="AUTH-EV-02",
        authority_quote="Q3 tu nnt u pilih ya",
        also_recorded_as=None,
        # CORRECTED IN STAGE 4.2F-B0.9.1 (T04-COR-02). This line was recorded here as a
        # Bariah message and a delegation from the authority to CAIR. Visual inspection of
        # the rendered WhatsApp screenshot shows it is FIRDAUS'S message — green,
        # right-aligned, sent/read ticks. Stage 4.2F-B0.9 had no image and read the line from
        # an unattributed transcription. It is not an authority statement at all.
        subject="A line recorded here in error as Bariah's; it is Firdaus deferring his own "
                "third confirmation request",
        author="FIRDAUS",
        is_authority_statement=False,
        status="NOT_AN_AUTHORITY_STATEMENT_MISATTRIBUTED_IN_B0_9",
        secondary_status="RETAINED_FOR_TRACEABILITY_NOT_ACTIONABLE",
        correction_id="T04-COR-02",
        evidence_grade="DEGRADED_TRANSCRIBED_NOT_IMAGE_VERIFIED",
        ambiguous_label_as_written="Q3",
        label_not_used_as_decision_id=True,
        candidate_referents=[
            "Quiz item Q3 in Section E of the review package (Pendekatan IPM).",
            "The third question or third item in the WhatsApp exchange itself, which this run "
            "cannot see.",
        ],
        interpretation=(
            "Firdaus deferred his own third confirmation request. Bariah answered that "
            "request explicitly three minutes later. There is no delegation from the "
            "authority to CAIR anywhere in this exchange, and this record produces no "
            "content change."),
        what_this_does_not_establish=(
            "What 'Q3' refers to, and what the choice is between. Quiz Q3 already has a "
            "specific, complete PINDA instruction in the DOCX, which makes the quiz-item "
            "reading redundant and therefore suspect. The referent stays open."),
        applied_to_content=False,
        blocking=False,
        resolution_required_from="Bariah — one line naming what Q3 refers to and what the "
                                 "choice is between.",
        why_the_raw_label_is_not_an_id=(
            "'Q3' is already the identifier of a quiz item in the same review package. Using "
            "it as the identifier of this confirmation would silently assert the quiz reading "
            "is correct, which is exactly the thing that is unknown.")),
]

CONFIRMATION_FIELDS = ["confirmation_id", "evidence_id", "authority_quote", "subject",
                       "status", "evidence_grade", "interpretation",
                       "what_this_does_not_establish", "applied_to_content", "blocking"]

# ==========================================================================================
# PART 3 — DECISION REGISTER
# ==========================================================================================
DECISION_CLASSES = [
    "ACCEPTED_AS_PROPOSED",
    "AMENDED_WITH_AUTHORITY_SUPPLIED_REPLACEMENT_TEXT",
    "AMENDED_WITH_AUTHORITY_INSTRUCTION_EXECUTED_BY_CAIR",
    "STRUCTURAL_INSERTION",
    "STRUCTURAL_RENUMBERING",
    "GLOBAL_COURSE_RULE",
    "DELEGATED_PENDING_AUTHORITY_CONFIRMATION",
]

# A generic "accepted" bucket would erase the difference between "Bariah wrote the replacement
# herself" and "Bariah told CAIR to change it and CAIR chose the wording". Those are not the
# same decision and are not allowed to share a status.
DECISION_CLASS_MEANING = {
    "ACCEPTED_AS_PROPOSED":
        "Bariah ticked TERIMA. The proposed item stands unchanged.",
    "AMENDED_WITH_AUTHORITY_SUPPLIED_REPLACEMENT_TEXT":
        "Bariah ticked PINDA and wrote the replacement wording herself. The wording is hers "
        "and is carried verbatim.",
    "AMENDED_WITH_AUTHORITY_INSTRUCTION_EXECUTED_BY_CAIR":
        "Bariah ticked PINDA and stated what must change, without writing the replacement. "
        "CAIR executed the instruction; the result is NOT Bariah-authored and is marked "
        "pending her confirmation.",
    "STRUCTURAL_INSERTION":
        "Bariah added an item that did not exist in the proposal.",
    "STRUCTURAL_RENUMBERING":
        "A consequence of an insertion. Carries no content change of its own.",
    "GLOBAL_COURSE_RULE":
        "Bariah stated the rule applies beyond T04, to the whole Kursus.",
    "DELEGATED_PENDING_AUTHORITY_CONFIRMATION":
        "Bariah handed the choice to CAIR, or the referent is ambiguous. Not settled.",
}

_SCOPE_T04 = "T04_ONLY"
_SCOPE_ALL = "ALL_PLS_IN_KURSUS"

_A = "ACCEPTED_AS_PROPOSED"
_RT = "AMENDED_WITH_AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"
_IX = "AMENDED_WITH_AUTHORITY_INSTRUCTION_EXECUTED_BY_CAIR"
_SI = "STRUCTURAL_INSERTION"
_SR = "STRUCTURAL_RENUMBERING"
_GC = "GLOBAL_COURSE_RULE"
_DP = "DELEGATED_PENDING_AUTHORITY_CONFIRMATION"

# (decision_id, class, subject, authority_quote, section, applies_to, scope, effect)
_DECISIONS = [
    # ---- Section A: screen sequence -----------------------------------------------------
    ("T04-DEC-A01", _A, "T04-S01 accepted, with the Bahagian label removed",
     "Tiada Bahagian bagi Topik 4. Kesemua subtopik di bawah Topik 4 – Landskap Lembut dan "
     "Landskap Kejur – di dalam 1 storyboard.",
     "A", ["T04-S01"], _SCOPE_T04,
     "Title screen shows Topik 4 with no Bahagian. All T04 subtopics stay in one storyboard."),
    ("T04-DEC-A02", _A, "T04-S02 kept in sequence; its dialogue replaced under Section C",
     "Rujuk Bahagian C. Perbualan Slide 2",
     "A", ["T04-S02"], _SCOPE_T04,
     "The screen is not removed or moved. Its content is replaced by the Section C ruling."),
    ("T04-DEC-A03", _A, "T04-S03 accepted unchanged", "TERIMA",
     "A", ["T04-S03"], _SCOPE_T04, "Six-step process flow stands as proposed."),
    ("T04-DEC-A04", _A, "T04-S04 accepted, framing corrected",
     "Ia bukan kategori landskap lembut, tetapi tanggungjawab kritikal dalam tempoh "
     "penyelenggaraan semasa pembinaan dan DLP - Siram, Baja, Racun. Refer module content.",
     "A", ["T04-S04"], _SCOPE_T04,
     "Siram, Baja and Racun are presented as critical contractor responsibilities during the "
     "construction maintenance period and the DLP — not as a taxonomy of soft landscape."),
    ("T04-DEC-A05", _A, "T04-S05 accepted, aspect list added",
     "Dan menyenaraikan aspek penyiraman [Kaedah Pelaksanaan, Aspek Pengurusan Untuk "
     "Kontraktor]",
     "A", ["T04-S05"], _SCOPE_T04,
     "The main-explanation screen also lists the two watering aspects that follow it."),
    ("T04-DEC-A06", _A, "T04-S06 accepted unchanged", "TERIMA",
     "A", ["T04-S06"], _SCOPE_T04, "Watering methods stand as proposed."),
    ("T04-DEC-A07", _A, "T04-S07 accepted unchanged", "TERIMA",
     "A", ["T04-S07"], _SCOPE_T04, "Watering management aspects stand as proposed."),
    ("T04-DEC-A08", _A, "T04-S08 accepted, aspect list added",
     "Dan menyenaraikan aspek pembajaan [Kaedah Pelaksanaan, Aspek Pengurusan Untuk "
     "Kontraktor]",
     "A", ["T04-S08"], _SCOPE_T04,
     "The main-explanation screen also lists the two fertilising aspects that follow it."),
    ("T04-DEC-A09", _A, "T04-S09 accepted unchanged", "TERIMA",
     "A", ["T04-S09"], _SCOPE_T04, "Fertilising methods stand as proposed."),
    ("T04-DEC-A10", _A, "T04-S10 accepted unchanged", "TERIMA",
     "A", ["T04-S10"], _SCOPE_T04, "Fertilising management aspects stand as proposed."),
    ("T04-DEC-A11", _A, "T04-S11 accepted, aspect list added",
     "Dan menyenaraikan aspek kawalan racun [Pendekatan IPM, Jenis Racun, Aspek Pengurusan "
     "Untuk Kontraktor]",
     "A", ["T04-S11"], _SCOPE_T04,
     "The main-explanation screen also lists the three pest-control aspects that follow it."),
    ("T04-DEC-A12", _IX, "T04-S12 treatment changed to static content",
     "Layanan – Kandungan statik.",
     "A", ["T04-S12"], _SCOPE_T04,
     "IPM priority order is presented as static content. The four controls are base-visible; "
     "no click-to-reveal."),
    ("T04-DEC-A13", _IX, "T04-S13 treatment changed to static content",
     "Layanan – Kandungan statik. Kandungan pendek.",
     "A", ["T04-S13"], _SCOPE_T04,
     "Pesticide types are presented as short static content. All three types base-visible."),
    ("T04-DEC-A14", _SI, "A new screen is inserted as T04-S14",
     "Layanan – Klik untuk paparkan maklumat. Tiga aspek pengurusan pembajaan untuk "
     "kontraktor. [Perundangan Dan Pelesenan, Keselamatan Dan Kesihatan (HSE), Pengurusan "
     "Risiko]",
     "A", ["T04-S14"], _SCOPE_T04,
     "A click-to-reveal hub screen for the three pesticide management aspects, sitting before "
     "the three screens that carry them in detail. See T04-COR-01 for the wording "
     "normalisation applied to this quote."),
    ("T04-DEC-A15", _SR, "Former T04-S14 becomes T04-S15",
     "Urutan Skrin bertukar ke S15",
     "A", ["T04-S15"], _SCOPE_T04, "Renumbering only. Content and treatment unchanged."),
    ("T04-DEC-A16", _IX, "Former T04-S15 becomes T04-S16 and gains click-to-reveal",
     "1. Urutan Skrin bertukar ke S16 2. Layanan – Klik untuk paparkan maklumat. [PPE "
     "Lengkap, Penyimpanan Dan Pelupusan, Helaian Data Keselamatan (SDS)]",
     "A", ["T04-S16"], _SCOPE_T04,
     "Three named reveal items. This supersedes the D-04 placement of PPE Lengkap on the base "
     "state — see T04-SUP-01."),
    ("T04-DEC-A17", _IX, "Former T04-S16 becomes T04-S17 and becomes fully static",
     "1. Urutan Skrin bertukar ke S17 2. Layanan – Kandungan statik (semua kandungan)",
     "A", ["T04-S17"], _SCOPE_T04,
     "All risk-management content is base-visible. This supersedes the D-04 reveal-eligible "
     "classification for this screen — see T04-SUP-02."),
    ("T04-DEC-A18", _IX, "Former T04-S17 becomes T04-S18; the soft/hard contrast is removed",
     "1. Urutan Skrin bertukar ke S18 Nota Bariah: Dan menetapkan empat fungsi utama landskap "
     "kejur. Saya tidak rasa ia membezakan antara landskap kejur dan lembut (Refer module)",
     "A", ["T04-S18"], _SCOPE_T04,
     "The screen establishes hard landscape and names its four main functions. The framing "
     "that contrasts hard with soft landscape is removed — the module does not draw that "
     "comparison."),
    ("T04-DEC-A19", _SR, "Former T04-S18 becomes T04-S19",
     "1. Urutan Skrin bertukar ke S19",
     "A", ["T04-S19"], _SCOPE_T04, "Renumbering only."),
    ("T04-DEC-A20", _SR, "Former T04-S19 becomes T04-S20; content replaced under Section D",
     "1. Urutan Skrin bertukar ke S20 2. Rujuk Bahagian D. Rumusan",
     "A", ["T04-S20"], _SCOPE_T04,
     "Renumbering, plus the Rumusan content is replaced by the Section D ruling."),
    ("T04-DEC-A21", _SR, "Former T04-S20 becomes T04-S21; content replaced under Section E",
     "1. Urutan Skrin bertukar ke S21 2. Rujuk Bahagian E. Kuiz",
     "A", ["T04-S21"], _SCOPE_T04,
     "Renumbering, plus the quiz content is replaced by the Section E ruling."),
    ("T04-DEC-A22", _IX, "Former T04-S21 becomes T04-S22 and closes the Topik, not a Bahagian",
     "1. Tamat Topik. Menutup Topik 2. Urutan Skrin bertukar ke S22",
     "A", ["T04-S22"], _SCOPE_T04,
     "The closing screen reads Tamat Topik and closes the Topik. Tamat Bahagian is retired "
     "for T04, consistent with T04-DEC-A01."),
    # ---- Section B: visual scope --------------------------------------------------------
    ("T04-DEC-B01", _A, "The 46 to 41 derivation is accepted as production scope",
     "Kaedah kiraan 46 → 41 diterima sebagai skop produksi.",
     "B", ["T04-VIS-GOV-01"], _SCOPE_T04,
     "41 proposed unique assets across 8 groups is the accepted production scope for T04."),
    ("T04-DEC-B02", _A, "Visual coverage is instructionally sufficient",
     "Sudut instruksional: liputan visual mencukupi; setiap operasi (Siram/Baja/Racun) "
     "mempunyai sokongan visual.",
     "B", ["AG-01", "AG-02", "AG-03", "AG-04", "AG-05", "AG-06", "AG-07", "AG-08"],
     _SCOPE_T04, "Every operation has visual support. No coverage gap is raised."),
    ("T04-DEC-B03", _A, "Conditional sharing across AG-01 to AG-08 is reasonable",
     "cadangan perkongsian bersyarat (AG-01–AG-08) munasabah untuk pengoptimuman produksi",
     "B", ["AG-01", "AG-02", "AG-03", "AG-04", "AG-05", "AG-06", "AG-07", "AG-08"],
     _SCOPE_T04,
     "Conditional sharing is accepted as a set. Individual group conditions still apply."),
    ("T04-DEC-B04", _A, "The three do-not-reuse items are confirmed on both grounds",
     "Saya sahkan item \"tidak boleh dikongsi\" (PPE baja, PPE racun, stok baja vs stok "
     "racun) memang memerlukan aset berasingan kerana visualnya berbeza secara ketara.",
     "B", ["T04-VO-025", "T04-VO-026", "T04-VO-040"], _SCOPE_T04,
     "Each of the three keeps a separate asset, confirmed instructionally and for "
     "production."),
    ("T04-DEC-B05", _A, "Instructional judgement overrides production optimisation",
     "Di mana dua sudut bertembung (jika ada): keputusan instruksional mengatasi "
     "pengoptimuman produksi. Jika sesuatu gabungan aset menjimatkan produksi tetapi "
     "mengaburkan perbezaan yang learner perlu faham, aset tersebut TIDAK boleh digabung.",
     "B", ["T04-VIS-GOV-01"], _SCOPE_T04,
     "A standing precedence rule for T04 asset decisions: where the two lenses conflict, the "
     "instructional decision wins and the assets are not merged."),
    ("T04-DEC-B06", _IX, "Each do-not-reuse item must carry a decision-basis line",
     "tambah satu baris asas keputusan pada setiap \"tidak boleh dikongsi\" — sama ada atas "
     "alasan instruksional, produksi, atau kedua-dua — supaya jejak keputusan jelas",
     "B", ["T04-VO-025", "T04-VO-026", "T04-VO-040"], _SCOPE_T04,
     "Every do-not-reuse item now carries decision_basis. All three are "
     "BOTH_INSTRUCTIONAL_AND_PRODUCTION, following T04-DEC-B04."),
    # ---- Section C: dialogue ------------------------------------------------------------
    ("T04-DEC-C01", _RT, "All five proposed dialogue lines are amended and replaced by four",
     "Cadangan Pindaan: [four replacement lines supplied verbatim by Bariah]",
     "C", ["T04-DLG-F01", "T04-DLG-F02", "T04-DLG-F03", "T04-DLG-F04"], _SCOPE_T04,
     "The five-line CAIR draft is replaced by Bariah's four-line dialogue, carried verbatim."),
    ("T04-DEC-C02", _A, "Alya and Encik Rahman are retained as the Slide 2 characters",
     "Watak | Alya (Kontraktor Junior); Encik Rahman (Mentor / Kontraktor Senior)",
     "C", ["T04-S02"], _SCOPE_T04,
     "The cast is unchanged. Bariah's critique is of how they were written, not of who they "
     "are — her replacement text uses both characters by name."),
    ("T04-DEC-C03", _IX, "The soft-versus-hard contrast is banned from the dialogue",
     "elak framing \"beza lembut vs kejur\" — modul cuma terangkan dua-dua secara "
     "berasingan, tak buat perbandingan",
     "C", ["T04-S02", "T04-S18"], _SCOPE_T04,
     "No dialogue line may frame soft and hard landscape as a comparison. The module "
     "describes them separately."),
    # ---- Section D: Rumusan -------------------------------------------------------------
    ("T04-DEC-D01", _RT, "The four-point Rumusan is replaced by a three-beat Rumusan",
     "Cadangan Pindaan: [Kepentingan] … [Skop/Isi Utama] … [Manfaat] …",
     "D", ["T04-RUM-F01", "T04-RUM-F02", "T04-RUM-F03"], _SCOPE_T04,
     "Three beats — Kepentingan, Skop/Isi Utama, Manfaat — carried verbatim."),
    ("T04-DEC-D02", _A, "Rumusan point 04 is removed with it",
     "☐ TERIMA ✓ PINDA ☐ BUANG",
     "D", ["T04-RUM2-04"], _SCOPE_T04,
     "The over-broad contractor-responsibility generalisation does not survive into the "
     "three-beat replacement. The open question raised against it is closed."),
    # ---- Section E: quiz ----------------------------------------------------------------
    ("T04-DEC-E01", _RT, "Q1 stem replaced",
     "Apakah tiga tanggungjawab kritikal dalam tempoh penyelenggaraan semasa pembinaan dan "
     "DLP bagi landskap lembut?",
     "E", ["T04-QZ-Q1"], _SCOPE_T04, "Bariah's stem is carried verbatim."),
    ("T04-DEC-E02", _RT, "Q2 stem replaced",
     "Sebuah projek memerlukan pengairan automatik bagi kawasan rumput yang luas. Antara "
     "sistem berikut, yang manakah paling sesuai?",
     "E", ["T04-QZ-Q2"], _SCOPE_T04, "Bariah's stem is carried verbatim."),
    ("T04-DEC-E03", _RT, "Q3 stem replaced",
     "Mengikut susunan keutamaan IPM, kaedah kawalan yang manakah disenaraikan paling akhir?",
     "E", ["T04-QZ-Q3"], _SCOPE_T04, "Bariah's stem is carried verbatim."),
    ("T04-DEC-E04", _RT, "Q4 stem replaced",
     "Antara fungsi berikut, yang manakah merangkumi kerja menstabilkan tanah dan menguruskan "
     "aliran air?",
     "E", ["T04-QZ-Q4"], _SCOPE_T04, "Bariah's stem is carried verbatim."),
    ("T04-DEC-E05", _RT, "Q5 stem replaced",
     "Pilih SEMUA kawalan yang mesti dipatuhi oleh kontraktor semasa aktiviti semburan racun.",
     "E", ["T04-QZ-Q5"], _SCOPE_T04, "Bariah's stem is carried verbatim."),
    ("T04-DEC-E06", _GC, "Module-attribution phrasing is banned course-wide",
     "Global keseluruhan kursus – buang \"yang dinyatakan dalam modul\"",
     "E", ["QUIZ-GLOBAL-01"], _SCOPE_ALL,
     "No quiz stem in the Kursus may attribute its content to the module. Applied to T04 Q1 "
     "to Q5; issued as a standing rule for every PL."),
    ("T04-DEC-E07", _GC, "Multiple Response items use checkboxes, never A/B/C letters",
     "Global keseluruhan kursus. Jangan gunakan A B C .. untuk pilihan, kerana ini ialah "
     "multiple response question. Cadangan - Gunakan kotak.",
     "E", ["QUIZ-GLOBAL-02"], _SCOPE_ALL,
     "Letter labels are reserved for single-answer items. Multiple Response options are "
     "presented as checkboxes."),
    ("T04-DEC-E08", _IX, "Q5 options E and F must be changed",
     "Tukar pilihan 5 dan 6 (E dan F), kerana jelas ia pilihan yang salah. (kerana ia tentang "
     "baja) ATAU tukar soalan.",
     "E", ["T04-QZ-Q5"], _SCOPE_T04,
     "Bariah gave two routes and did not choose between them. CAIR took the first — change "
     "the options, keep the question — because Bariah separately supplied replacement wording "
     "for the Q5 stem, which settles the question. The two replacement distractors are "
     "CAIR-drafted and are NOT Bariah-approved."),
    ("T04-DEC-E09", _A, "Q5 incorrect options: Set B selected from an enumerated forced "
                        "choice",
     "Set B. Better distractors",
     "WHATSAPP", ["T04-QZ-Q5"], _SCOPE_T04,
     "The two incorrect Q5 options are Set B, verbatim: 'Semburan dijadualkan pada waktu "
     "petang tanpa mengambil kira keadaan cuaca' and 'Semua racun dibeli daripada satu "
     "pembekal tunggal'. Set A is REJECTED_NOT_SELECTED. This closes E-07 and supersedes the "
     "CAIR-drafted wording from Stage 4.2F-B0.9."),
    # ---- Section F: overall verdict -----------------------------------------------------
    ("T04-DEC-F01", _A, "BA-1 to BA-4 all marked complete", "✓",
     "F", ["BA-1", "BA-2", "BA-3", "BA-4"], _SCOPE_T04,
     "All four required review actions are recorded as done."),
    ("T04-DEC-F02", _A, "Overall verdict: approved with the stated amendments",
     "✓ LULUS DENGAN PINDAAN DINYATAKAN",
     "F", ["T04-VIS-GOV-01"], _SCOPE_T04,
     "Conditional approval. The amendments named in each section are part of the approval."),
    # ---- Delegated / unresolved ---------------------------------------------------------
    ("T04-DEC-X01", _DP, "The 'Q3' WhatsApp line — misattributed in Stage 4.2F-B0.9, "
                          "corrected to Firdaus authorship",
     "Q3 tu nnt u pilih ya",
     "WHATSAPP", ["T04-CNF-03"], _SCOPE_T04,
     "No content change, and no authority act. Stage 4.2F-B0.9 recorded this as a Bariah "
     "delegation; the rendered screenshot shows it is Firdaus's own message. See T04-COR-02. "
     "The record is retained so the correction is traceable, not because it decides "
     "anything."),
    ("T04-DEC-X02", _DP, "The Q5 answer key remains a proposal",
     "Jawapan | Cadangan jawapan sahaja — belum muktamad.",
     "E", ["T04-QZ-Q1", "T04-QZ-Q2", "T04-QZ-Q3", "T04-QZ-Q4", "T04-QZ-Q5"], _SCOPE_T04,
     "Bariah did not mark any answer key final. All five keys stay PROPOSED_NOT_FINAL."),
]


def _decision_register():
    out = []
    for did, cls, subject, quote, section, applies, scope, effect in _DECISIONS:
        if cls not in DECISION_CLASSES:
            raise RuntimeError(f"{did}: unknown decision class {cls}")
        out.append(dict(
            decision_id=did,
            decision_class=cls,
            decision_class_meaning=DECISION_CLASS_MEANING[cls],
            subject=subject,
            # T04-DEC-X01 is retained for traceability only and is NOT a Bariah act — see
            # T04-COR-02. Every other decision in this register is hers.
            authority=("FIRDAUS_NOT_AN_AUTHORITY_ACT" if did == "T04-DEC-X01"
                       else "BARIAH_AHMAD"),
            authority_quote=quote,
            source_artifact=("AUTH-EV-02" if section == "WHATSAPP" else "AUTH-EV-01"),
            source_section=section,
            # Three grades, because three different things happened. The DOCX was opened and
            # hashed. The E-07 selection was read from a rendered image whose binary could not
            # be taken into custody. The earliest WhatsApp lines reached Stage 4.2F-B0.9 only
            # as text transcribed into a brief.
            evidence_grade=(
                "READ_FROM_RENDERED_IMAGE_CUSTODY_UNVERIFIED" if did == "T04-DEC-E09"
                else "DEGRADED_TRANSCRIBED_NOT_IMAGE_VERIFIED" if section == "WHATSAPP"
                else "VERIFIED_PRIMARY_ARTIFACT"),
            applies_to=list(applies),
            scope=scope,
            effect=effect,
            authored_by_authority=(cls in (_A, _RT, _SI, _SR, _GC)),
            settled=(cls != _DP)))
    return out


DECISION_REGISTER = _decision_register()
DECISION_FIELDS = ["decision_id", "decision_class", "subject", "authority_quote",
                   "source_artifact", "source_section", "evidence_grade", "applies_to",
                   "scope", "effect", "authored_by_authority", "settled"]


def decisions_by_class():
    """Live derivation. A cached dict here would go stale the moment a decision changed."""
    return {c: [d["decision_id"] for d in _decision_register() if d["decision_class"] == c]
            for c in DECISION_CLASSES}


def course_wide_decisions():
    return [d["decision_id"] for d in _decision_register() if d["scope"] == _SCOPE_ALL]


def unsettled_decisions():
    return [d["decision_id"] for d in _decision_register() if not d["settled"]]


# ==========================================================================================
# AUTHORITY WORDING CORRECTIONS — applied, never silent
# ==========================================================================================
# A typed-identifier correction, distinct from the wording corrections below: nothing the
# authority wrote was changed, only an internal ID that pointed at the wrong obligation.
IDENTIFIER_CORRECTIONS = [
    dict(
        correction_id="T04-COR-05",
        field="do-not-reuse register, HSE item obligation ID",
        as_recorded="T04-VO-039",
        as_corrected="T04-VO-040",
        found_in_stage="4.2F-B1",
        introduced_in_stage="4.2F-B0.9",
        basis=(
            "T04-VO-039 is the Perundangan dan Pelesenan obligation (rows 65-67). The "
            "obligation whose subject is the pesticide PPE set is T04-VO-040 (rows 68-74), "
            "and the Stage 4.2F-B0.8 closure already carries reuse_policy = DO_NOT_REUSE on "
            "it. The register had a hand-typed ID that was never cross-checked."),
        authority_wording_changed=False,
        what_it_would_have_broken=(
            "The storyboard would have shown the do-not-reuse restriction on the legal screen "
            "and not on the PPE screen — the exact confusion Bariah's ruling exists to "
            "prevent."),
        detection="Cross-checking the typed list against the closure's own reuse_policy while "
                  "building the B1 visual mapping.",
        status="APPLIED",
        recurrence_note=(
            "Second occurrence of this defect class. Stage 4.2F-B0.6 had five hand-typed "
            "obligation IDs in the legal sheet, fixed then by deriving from an index. The "
            "lesson did not carry across to this register. It does now: a gate derives the "
            "do-not-reuse ID set from the closure and compares."),
    ),
]

AUTHORITY_WORDING_CORRECTIONS = [
    dict(
        correction_id="T04-COR-01",
        decision_id="T04-DEC-A14",
        field="new screen T04-S14 purpose line",
        as_written_by_authority="Tiga aspek pengurusan pembajaan untuk kontraktor.",
        as_applied="Tiga aspek pengurusan racun untuk kontraktor.",
        correction_type="TERM_SUBSTITUTION",
        basis=(
            "The screen Bariah is inserting sits inside the Racun sequence, is titled 'Racun "
            "— aspek pengurusan untuk kontraktor', and enumerates three pesticide-specific "
            "aspects: Perundangan Dan Pelesenan, Keselamatan Dan Kesihatan (HSE), Pengurusan "
            "Risiko. 'Pembajaan' is fertilising. The Baja equivalent screen in the same table "
            "reads 'Lima aspek pengurusan pembajaan untuk kontraktor', which is where the "
            "word came from. The count also differs — three here, five there."),
        confidence="HIGH",
        status="APPLIED_PENDING_BARIAH_CONFIRMATION",
        reversible=True,
        what_happens_if_wrong=(
            "If Bariah meant fertilising, the inserted screen belongs in the Baja sequence "
            "rather than the Racun sequence and the whole insertion point moves. The original "
            "wording is preserved above so the correction can be undone from this record "
            "alone."),
        confirmation_required_from="Bariah — one line confirming the screen is about racun."),
]

# Prior rulings this stage supersedes. Recorded, not argued.
SUPERSESSIONS = [
    dict(
        supersession_id="T04-SUP-01",
        superseded_ruling="D-04 — PPE Lengkap placed on the base state of the HSE screen, not "
                          "behind a reveal",
        superseded_in_stage="4.2F-B0.6",
        superseded_by="T04-DEC-A16",
        new_position=("PPE Lengkap is one of three named click-to-reveal items on T04-S16, "
                      "alongside Penyimpanan Dan Pelupusan and Helaian Data Keselamatan "
                      "(SDS)."),
        authority="BARIAH_AHMAD",
        authority_quote="Layanan – Klik untuk paparkan maklumat. [PPE Lengkap, Penyimpanan "
                        "Dan Pelupusan, Helaian Data Keselamatan (SDS)]",
        residual_risk=(
            "A learner who does not interact will not see the PPE list. D-04 had placed PPE "
            "on the base state precisely to avoid that. Bariah has now ruled directly on this "
            "screen and her later direct ruling governs. The risk is recorded here and in the "
            "screen record; it is not re-argued."),
        risk_owner="BARIAH_AHMAD"),
    dict(
        supersession_id="T04-SUP-02",
        superseded_ruling="D-04 — spray conditions, notification and reporting classified as "
                          "reveal-eligible on the risk-management screen",
        superseded_in_stage="4.2F-B0.6",
        superseded_by="T04-DEC-A17",
        new_position="All risk-management content on T04-S17 is base-visible static content.",
        authority="BARIAH_AHMAD",
        authority_quote="Layanan – Kandungan statik (semua kandungan)",
        residual_risk=(
            "None introduced. This change removes a residual risk: the three obligations that "
            "a non-interacting learner would previously have missed are now base-visible."),
        risk_owner="NONE_REMOVED_BY_THIS_DECISION"),
]

# ==========================================================================================
# PART 4 — FINAL SCREEN SEQUENCE v2 (22 screens)
# ==========================================================================================
def _rows(a, b):
    return [f"T04-ROW-{i:03d}" for i in range(a, b + 1)]


_PREV = {s["screen_id"]: s for s in C.SCREEN_SEQUENCE}

# (new_id, prev_id, title, treatment, states, source_rows, decision_ids, change_type, note)
_SEQ = [
    ("T04-S01", "T04-S01", "Tajuk dan Mula", "TITLE", ["BASE only"], [],
     ["T04-DEC-A01"], "AMENDED",
     "Shows Topik 4 and the unit title. No Bahagian label — Bariah ruled T04 has none."),
    ("T04-S02", "T04-S02", "Pengenalan — perbualan di tapak", "DIALOGUE_SCENARIO",
     ["BASE — dialogue plays"],
     ["T04-ROW-001", "T04-ROW-002", "T04-ROW-003", "T04-ROW-004", "T04-ROW-005",
      "T04-ROW-079", "T04-ROW-080"],
     ["T04-DEC-A02", "T04-DEC-C01", "T04-DEC-C02", "T04-DEC-C03"], "AMENDED",
     "Carries the four-line replacement dialogue. The soft-versus-hard contrast is banned "
     "from the dialogue."),
    ("T04-S03", "T04-S03", "Aliran proses penjagaan dan penyelenggaraan",
     "PROCESS_FLOW_STEPPED",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ST-05", "ST-06", "ALL_VIEWED"],
     ["T04-ROW-001", "T04-ROW-002", "T04-ROW-003"], ["T04-DEC-A03"], "UNCHANGED",
     "Accepted as proposed."),
    ("T04-S04", "T04-S04", "Landskap Lembut — pengenalan", "CONTENT_STATIC", ["BASE only"],
     _rows(4, 5), ["T04-DEC-A04"], "AMENDED",
     "Presents Siram, Baja and Racun as critical contractor responsibilities during the "
     "construction maintenance period and the DLP, not as a soft-landscape taxonomy."),
    ("T04-S05", "T04-S05", "Siram — penerangan utama", "CONTENT_STATIC", ["BASE only"],
     _rows(6, 7), ["T04-DEC-A05"], "AMENDED",
     "Also lists the watering aspects: Kaedah Pelaksanaan, Aspek Pengurusan Untuk Kontraktor."),
    ("T04-S06", "T04-S06", "Siram — kaedah pelaksanaan", "CLICK_TO_REVEAL",
     ["BASE", "ST-01", "ST-02", "ALL_VIEWED"], _rows(8, 15), ["T04-DEC-A06"], "UNCHANGED",
     "Accepted as proposed."),
    ("T04-S07", "T04-S07", "Siram — aspek pengurusan untuk kontraktor", "CLICK_TO_REVEAL",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ALL_VIEWED"], _rows(16, 25),
     ["T04-DEC-A07"], "UNCHANGED", "Accepted as proposed."),
    ("T04-S08", "T04-S08", "Baja — penerangan utama", "CONTENT_STATIC", ["BASE only"],
     _rows(26, 27), ["T04-DEC-A08"], "AMENDED",
     "Also lists the fertilising aspects: Kaedah Pelaksanaan, Aspek Pengurusan Untuk "
     "Kontraktor."),
    ("T04-S09", "T04-S09", "Baja — kaedah pelaksanaan", "CLICK_TO_REVEAL",
     ["BASE", "ST-01", "ST-02", "ST-03", "ALL_VIEWED"], _rows(28, 34), ["T04-DEC-A09"],
     "UNCHANGED", "Accepted as proposed."),
    ("T04-S10", "T04-S10", "Baja — aspek pengurusan untuk kontraktor", "CLICK_TO_REVEAL",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ST-05", "ALL_VIEWED"], _rows(35, 45),
     ["T04-DEC-A10"], "UNCHANGED", "Accepted as proposed."),
    ("T04-S11", "T04-S11", "Racun — penerangan utama", "CONTENT_STATIC", ["BASE only"],
     _rows(46, 47), ["T04-DEC-A11"], "AMENDED",
     "Also lists the pest-control aspects: Pendekatan IPM, Jenis Racun, Aspek Pengurusan "
     "Untuk Kontraktor."),
    ("T04-S12", "T04-S12", "Racun — pendekatan IPM", "CONTENT_STATIC", ["BASE only"],
     _rows(48, 56), ["T04-DEC-A12"], "TREATMENT_CHANGED",
     "Was CLICK_TO_REVEAL. All four IPM controls are now base-visible; the priority order is "
     "read, not revealed."),
    ("T04-S13", "T04-S13", "Racun — jenis racun", "CONTENT_STATIC", ["BASE only"],
     _rows(57, 63), ["T04-DEC-A13"], "TREATMENT_CHANGED",
     "Was CLICK_TO_REVEAL. Short static content — all three pesticide types base-visible."),
    ("T04-S14", None, "Racun — aspek pengurusan untuk kontraktor", "CLICK_TO_REVEAL",
     ["BASE", "ST-01", "ST-02", "ST-03", "ALL_VIEWED"], ["T04-ROW-064"],
     ["T04-DEC-A14"], "INSERTED",
     "New screen inserted by Bariah. A click-to-reveal hub for the three pesticide management "
     "aspects — Perundangan Dan Pelesenan, Keselamatan Dan Kesihatan (HSE), Pengurusan Risiko "
     "— each of which is then carried in full on T04-S15, T04-S16 and T04-S17."),
    ("T04-S15", "T04-S14", "Racun — perundangan dan pelesenan", "CONTENT_STATIC",
     ["BASE only"], _rows(65, 67), ["T04-DEC-A15"], "RENUMBERED",
     "Renumbering only. Legal content stays base-visible and verbatim."),
    ("T04-S16", "T04-S15", "Racun — keselamatan dan kesihatan (HSE)", "CLICK_TO_REVEAL",
     ["BASE", "REVEAL_PPE_LENGKAP", "REVEAL_PENYIMPANAN_DAN_PELUPUSAN", "REVEAL_SDS",
      "ALL_VIEWED"], _rows(68, 74), ["T04-DEC-A16"], "RENUMBERED_AND_TREATMENT_CHANGED",
     "Three named reveals. Supersedes D-04's base-visible PPE placement — see T04-SUP-01. A "
     "non-interacting learner will not see the PPE list; that residual risk sits with the "
     "authority who made the ruling."),
    ("T04-S17", "T04-S16", "Racun — pengurusan risiko", "CONTENT_STATIC", ["BASE only"],
     _rows(75, 78), ["T04-DEC-A17"], "RENUMBERED_AND_TREATMENT_CHANGED",
     "All content base-visible. Supersedes D-04's reveal-eligible classification — see "
     "T04-SUP-02. This removes a residual risk rather than creating one."),
    ("T04-S18", "T04-S17", "Landskap Kejur — pengenalan", "CONTENT_STATIC", ["BASE only"],
     _rows(79, 80), ["T04-DEC-A18"], "RENUMBERED_AND_AMENDED",
     "Establishes hard landscape and names its four main functions. The contrast with soft "
     "landscape is removed — the module describes the two separately and draws no comparison."),
    ("T04-S19", "T04-S18", "Landskap Kejur — empat kumpulan fungsi", "CLICK_TO_REVEAL",
     ["BASE", "ST-01", "ST-02", "ST-03", "ST-04", "ALL_VIEWED"], _rows(81, 100),
     ["T04-DEC-A19"], "RENUMBERED", "Renumbering only."),
    ("T04-S20", "T04-S19", "Rumusan", "RUMUSAN", ["BASE only"], [],
     ["T04-DEC-A20", "T04-DEC-D01", "T04-DEC-D02"], "RENUMBERED_AND_AMENDED",
     "Carries the three-beat Rumusan. Four points became three."),
    ("T04-S21", "T04-S20", "Kuiz", "QUIZ", ["Q1", "Q2", "Q3", "Q4", "Q5", "RESULT"], [],
     ["T04-DEC-A21", "T04-DEC-E01", "T04-DEC-E02", "T04-DEC-E03", "T04-DEC-E04",
      "T04-DEC-E05", "T04-DEC-E06", "T04-DEC-E07", "T04-DEC-E08"],
     "RENUMBERED_AND_AMENDED",
     "Five items with Bariah's replacement stems. Q5 is Multiple Response with checkbox "
     "options."),
    ("T04-S22", "T04-S21", "Tamat Topik", "CLOSING", ["BASE only"], [],
     ["T04-DEC-A22"], "RENUMBERED_AND_AMENDED",
     "Closes the Topik. 'Tamat Bahagian' is retired for T04."),
]

CHANGE_TYPES = ["UNCHANGED", "AMENDED", "TREATMENT_CHANGED", "INSERTED", "RENUMBERED",
                "RENUMBERED_AND_AMENDED", "RENUMBERED_AND_TREATMENT_CHANGED"]

# The three named reveal items Bariah wrote for the inserted hub screen and for the HSE
# screen. Held as data so the screen record and the reconciliation gates read the same list.
NAMED_REVEAL_ITEMS = {
    "T04-S14": ["Perundangan Dan Pelesenan", "Keselamatan Dan Kesihatan (HSE)",
                "Pengurusan Risiko"],
    "T04-S16": ["PPE Lengkap", "Penyimpanan Dan Pelupusan",
                "Helaian Data Keselamatan (SDS)"],
}

# Aspect lists Bariah asked to be shown on the three main-explanation screens.
NAMED_ASPECT_LISTS = {
    "T04-S05": ["Kaedah Pelaksanaan", "Aspek Pengurusan Untuk Kontraktor"],
    "T04-S08": ["Kaedah Pelaksanaan", "Aspek Pengurusan Untuk Kontraktor"],
    "T04-S11": ["Pendekatan IPM", "Jenis Racun", "Aspek Pengurusan Untuk Kontraktor"],
}


def _final_sequence():
    out = []
    for i, (sid, prev, title, treatment, states, rows, decs, change, note) in enumerate(_SEQ):
        if change not in CHANGE_TYPES:
            raise RuntimeError(f"{sid}: unknown change type {change}")
        for r in rows:
            if r not in C.BY_ID:
                raise RuntimeError(f"{sid}: row not in the controlled extract: {r}")
        for d in decs:
            if d not in {x["decision_id"] for x in _decision_register()}:
                raise RuntimeError(f"{sid}: unknown decision {d}")
        prev_rec = _PREV.get(prev) if prev else None
        out.append(dict(
            screen_id=sid,
            position=i + 1,
            previous_screen_id=prev,
            previous_treatment=(prev_rec["treatment"] if prev_rec else None),
            working_title=title,
            treatment=treatment,
            interaction_states=list(states),
            named_reveal_items=list(NAMED_REVEAL_ITEMS.get(sid, [])),
            named_aspect_list=list(NAMED_ASPECT_LISTS.get(sid, [])),
            source_row_ids=list(rows),
            source_binding_present=bool(rows) or treatment in ("TITLE", "RUMUSAN", "QUIZ",
                                                              "CLOSING", "DIALOGUE_SCENARIO"),
            decision_ids=list(decs),
            change_type=change,
            authority_note=note,
            internal_unit_id=INTERNAL_UNIT_ID,
            learner_display_unit=LEARNER_DISPLAY_UNIT,
            content_status="FROZEN_UNDER_AUTHORITY_DECISION"))
    return out


FINAL_SCREEN_SEQUENCE = _final_sequence()
FINAL_SCREEN_FIELDS = ["screen_id", "position", "previous_screen_id", "working_title",
                       "treatment", "previous_treatment", "interaction_states",
                       "named_reveal_items", "source_row_ids", "decision_ids", "change_type",
                       "authority_note", "content_status"]


def final_screen_count():
    return len(_final_sequence())


def renumbering_map():
    """old -> new for every screen that moved. Derived live from the sequence."""
    return {s["previous_screen_id"]: s["screen_id"] for s in _final_sequence()
            if s["previous_screen_id"] and s["previous_screen_id"] != s["screen_id"]}


def inserted_screens():
    return [s["screen_id"] for s in _final_sequence() if s["change_type"] == "INSERTED"]


SUPERSEDED_SCREEN_COUNT = C.PROPOSED_LEARNER_SCREEN_COUNT   # 21
SUPERSEDED_CLOSING_LABEL = "Tamat Bahagian"
FINAL_CLOSING_LABEL = "Tamat Topik"

# ==========================================================================================
# PART 5 — FINAL SLIDE 2 DIALOGUE
# ==========================================================================================
DIALOGUE_SUPERSEDED_LINE_COUNT = 5

_DIALOGUE = [
    ("T04-DLG-F01", "Alya",
     "Encik Rahman, projek dah siap dibina. Kenapa kita masih perlu jaga taman ni setiap "
     "minggu?"),
    ("T04-DLG-F02", "Encik Rahman",
     "Sebab membina dan mengekalkan landskap dua benda berbeza, Alya. Tumbuhan kena disiram, "
     "dibaja dan dikawal perosak. Guna IPM, dan racun kimia pilihan terakhir. Struktur pula "
     "perlu dipantau supaya kekal berfungsi."),
    ("T04-DLG-F03", "Alya", "Dan semua kena direkod untuk tempoh DLP?"),
    ("T04-DLG-F04", "Encik Rahman",
     "Ya. Penyelenggaraan berjadual dan dokumentasi lengkap, itu yang melindungi kerja "
     "pembinaan kita dan mencerminkan kualiti kontraktor."),
]

# The Stage 4.2F-B0.8 compliance exclusions still bind: the dialogue must not place a legal
# duty on a character, must not present Encik Rahman as a licensed pesticide operator, and
# must not carry PPE, SDS or chemical-storage instructions. Bariah's replacement text is
# checked against all four by a gate rather than assumed to comply.
DIALOGUE_BOUNDARY_RULES = list(C.DIALOGUE["compliance_exclusions"]) \
    if isinstance(C.DIALOGUE.get("compliance_exclusions"), list) else list(
        C.COMPLIANCE_EXCLUSIONS)

FINAL_DIALOGUE = dict(
    dialogue_id="T04-DLG-FINAL",
    screen_id="T04-S02",
    decision_id="T04-DEC-C01",
    authority="BARIAH_AHMAD",
    authorship="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT",
    source_artifact="AUTH-EV-01 §C, Cadangan Pindaan",
    characters=["Alya (Kontraktor Junior)", "Encik Rahman (Mentor / Kontraktor Senior)"],
    cast_decision_id="T04-DEC-C02",
    line_count=len(_DIALOGUE),
    superseded_line_count=DIALOGUE_SUPERSEDED_LINE_COUNT,
    lines=[dict(line_id=lid, speaker=spk, text_ms=txt, position=i + 1,
                authorship="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT",
                content_status="FROZEN_UNDER_AUTHORITY_DECISION")
           for i, (lid, spk, txt) in enumerate(_DIALOGUE)],
    authority_critique_addressed=[
        "Alya was too passive — she now opens with a challenge rather than a blank question.",
        "Encik Rahman was reading a list — he now gives the principle and the reason.",
        "The core learning was missing — watering, fertilising and IPM with chemical control "
        "last are now in the dialogue.",
        "The close was passive — it now lands on impact: protecting the construction work and "
        "reflecting contractor quality.",
    ],
    banned_framing=dict(
        rule="No soft-versus-hard landscape comparison in the dialogue.",
        decision_id="T04-DEC-C03",
        authority_quote="elak framing \"beza lembut vs kejur\" — modul cuma terangkan dua-dua "
                        "secara berasingan, tak buat perbandingan"),
    content_status="FROZEN_UNDER_AUTHORITY_DECISION")

# ==========================================================================================
# PART 6 — FINAL RUMUSAN
# ==========================================================================================
RUMUSAN_SUPERSEDED_POINT_COUNT = 4

_RUMUSAN = [
    ("T04-RUM-F01", "Kepentingan",
     "Penjagaan dan penyelenggaraan memastikan landskap yang telah dibina kekal sihat, "
     "berfungsi dan selamat dalam jangka masa panjang. Membina dan mengekalkan landskap "
     "adalah dua tanggungjawab berbeza."),
    ("T04-RUM-F02", "Skop/Isi Utama",
     "Penjagaan dan penyelenggaraan merangkumi landskap lembut dan landskap kejur. Landskap "
     "lembut memfokuskan kepada penyiraman, pembajaan dan kawalan racun, manakala landskap "
     "kejur memfokuskan kepada memastikan elemen binaan kekal berfungsi dan selamat."),
    ("T04-RUM-F03", "Manfaat",
     "Dengan melaksanakan penjagaan dan penyelenggaraan yang berjadual dan terancang, "
     "kontraktor dapat memelihara kualiti landskap sepanjang DLP, memenuhi kewajipan "
     "kontrak, dan memastikan ruang luaran kekal lestari dan bernilai untuk pengguna."),
]

FINAL_RUMUSAN = dict(
    rumusan_id="T04-RUM-FINAL",
    screen_id="T04-S20",
    decision_id="T04-DEC-D01",
    authority="BARIAH_AHMAD",
    authorship="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT",
    source_artifact="AUTH-EV-01 §D, Cadangan Pindaan",
    structure="THREE_BEAT",
    beats=["Kepentingan", "Skop/Isi Utama", "Manfaat"],
    point_count=len(_RUMUSAN),
    superseded_point_count=RUMUSAN_SUPERSEDED_POINT_COUNT,
    points=[dict(point_id=pid, beat=beat, text_ms=txt, position=i + 1,
                 authorship="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT",
                 content_status="FROZEN_UNDER_AUTHORITY_DECISION")
            for i, (pid, beat, txt) in enumerate(_RUMUSAN)],
    authority_critique_addressed=[
        "The draft was a four-item list, not a flowing recap.",
        "It was too technical and repeated detail the learner had just covered.",
        "It had no importance beat to open with and no benefit beat to close on.",
    ],
    scope_of_the_three_beat_structure=dict(
        applies_to="T04_ONLY",
        why=("Bariah issued this structure while amending the T04 Rumusan and did not mark it "
             "'Global keseluruhan kursus' — the phrase she used twice, in the same document, "
             "for the two quiz rules she did mean course-wide. Reading a course-wide Rumusan "
             "rule out of a T04 amendment would be an inference, not a decision, so it is not "
             "made."),
        what_would_be_needed="An explicit statement from Bariah that the three-beat structure "
                             "applies beyond T04."),
    content_status="FROZEN_UNDER_AUTHORITY_DECISION")

# The B0.8 dependency between Rumusan point 04 and quiz Q5 is discharged, not deleted.
ARCHIVED_DEPENDENCIES = [
    dict(
        dependency_id="DEP-RUM04-Q5",
        raised_in_stage="4.2F-B0.8",
        original_statement=(
            "If Rumusan point 04 is amended or removed for over-generalisation, the Q5 "
            "wording must be re-checked so it stays specific to the pesticide controls the "
            "module states."),
        status="ARCHIVED_RESOLVED",
        resolved_by=["T04-DEC-D01", "T04-DEC-D02", "T04-DEC-E05", "T04-DEC-E08"],
        how_resolved=(
            "Both halves of the dependency fired. Rumusan point 04 did not survive into the "
            "three-beat replacement, and Q5 was independently amended by Bariah — the stem "
            "was rewritten and the two fertiliser-based distractors ordered changed. The "
            "condition the dependency was watching for has occurred and been handled."),
        residual="The Q5 answer key is still PROPOSED_NOT_FINAL, which is tracked by "
                 "T04-DEC-X02 and is not part of this dependency.",
        reopens_if="A future decision restores a general contractor-responsibility statement "
                   "to the Rumusan."),
]

# ==========================================================================================
# PART 7 — COURSE-WIDE QUIZ RULES
# ==========================================================================================
QUIZ_GLOBAL_RULES = [
    dict(
        rule_id="QUIZ-GLOBAL-01",
        decision_id="T04-DEC-E06",
        title_ms="Buang atribusi 'yang dinyatakan dalam modul' daripada soalan kuiz",
        title_en="Remove module-attribution phrasing from quiz stems",
        authority="BARIAH_AHMAD",
        authority_quote="Global keseluruhan kursus – buang \"yang dinyatakan dalam modul\"",
        source_artifact="AUTH-EV-01 §E, Q1 komen/pindaan",
        scope="ALL_PLS_IN_KURSUS",
        rule=("A quiz stem must ask the question directly. It must not attribute its content "
              "to the module — no 'yang dinyatakan dalam modul', no 'mengikut modul', no "
              "'Modul menyenaraikan'."),
        banned_phrases=["yang dinyatakan dalam modul", "mengikut modul", "dalam modul",
                        "Modul menyenaraikan"],
        rationale_authority_supplied=True,
        applied_to_t04_items=["T04-QZ-Q1", "T04-QZ-Q2", "T04-QZ-Q3", "T04-QZ-Q4",
                             "T04-QZ-Q5"],
        applies_beyond_t04=True,
        enforcement="Every T04 stem is checked against the banned phrases by a gate. Units "
                    "outside T04 are out of this stage's scope and are not modified here.",
        status="AUTHORITY_ISSUED_COURSE_WIDE"),
    dict(
        rule_id="QUIZ-GLOBAL-02",
        decision_id="T04-DEC-E07",
        title_ms="Gunakan kotak, bukan A B C, bagi soalan Multiple Response",
        title_en="Multiple Response options use checkboxes, not letter labels",
        authority="BARIAH_AHMAD",
        authority_quote="Global keseluruhan kursus. Jangan gunakan A B C .. untuk pilihan, "
                        "kerana ini ialah multiple response question. Cadangan - Gunakan "
                        "kotak.",
        source_artifact="AUTH-EV-01 §E, Q5 komen/pindaan",
        scope="ALL_PLS_IN_KURSUS",
        rule=("A Multiple Response item presents its options as checkboxes. Letter labels "
              "A, B, C … are reserved for single-answer items, where they signal that exactly "
              "one option is chosen."),
        banned_option_marker_pattern="^[A-Z]\\.\\s",
        required_option_marker="checkbox",
        rationale_authority_supplied=True,
        applied_to_t04_items=["T04-QZ-Q5"],
        applies_beyond_t04=True,
        enforcement="A gate asserts no Multiple Response option in T04 carries a letter "
                    "label, and that all four MCQ items keep theirs.",
        status="AUTHORITY_ISSUED_COURSE_WIDE"),
]

# ==========================================================================================
# PART 8 — FINAL QUIZ v2
# ==========================================================================================
QUIZ_PASS_MARK = "60 peratus"
QUIZ_SCOPE = "ALL_PLS_IN_KURSUS"
ANSWER_KEY_STATUS = "PROPOSED_NOT_FINAL"

_LETTER = ["A", "B", "C", "D", "E", "F"]

_QUIZ = [
    dict(
        qid="T04-QZ-Q1", n=1, qtype="MCQ", decision="T04-DEC-E01",
        stem=("Apakah tiga tanggungjawab kritikal dalam tempoh penyelenggaraan semasa "
              "pembinaan dan DLP bagi landskap lembut?"),
        superseded_stem=("Apakah tiga operasi utama penyelenggaraan landskap lembut yang "
                         "dinyatakan dalam modul?"),
        options=["Siram, baja dan racun", "Siram, potong dan tanam",
                 "Baja, racun dan turap", "Racun, siram dan pembinaan"],
        options_authorship="CAIR_DRAFT_UNCHANGED_BY_AUTHORITY",
        key=[0], source_rows=_rows(4, 5) + _rows(6, 7) + _rows(26, 27) + _rows(46, 47)),
    dict(
        qid="T04-QZ-Q2", n=2, qtype="MCQ", decision="T04-DEC-E02",
        stem=("Sebuah projek memerlukan pengairan automatik bagi kawasan rumput yang luas. "
              "Antara sistem berikut, yang manakah paling sesuai?"),
        superseded_stem=("Sebuah projek memerlukan pengairan automatik bagi kawasan rumput "
                         "yang luas. Mengikut modul, sistem manakah yang paling sesuai?"),
        options=["Sistem Semburan (Sprinkler System)", "Sistem Titis (Drip Irrigation System)",
                 "Penyiraman manual menggunakan hos getah",
                 "Semburan folia menggunakan baja cecair"],
        options_authorship="CAIR_DRAFT_UNCHANGED_BY_AUTHORITY",
        key=[0], source_rows=_rows(8, 15)),
    dict(
        qid="T04-QZ-Q3", n=3, qtype="MCQ", decision="T04-DEC-E03",
        stem=("Mengikut susunan keutamaan IPM, kaedah kawalan yang manakah disenaraikan "
              "paling akhir?"),
        superseded_stem=("Mengikut susunan keutamaan IPM dalam modul, kaedah kawalan manakah "
                         "yang disenaraikan paling akhir?"),
        options=["Kawalan Kultur", "Kawalan Fizikal", "Kawalan Biologi", "Kawalan Kimia"],
        options_authorship="CAIR_DRAFT_UNCHANGED_BY_AUTHORITY",
        key=[3], source_rows=_rows(48, 56)),
    dict(
        qid="T04-QZ-Q4", n=4, qtype="MCQ", decision="T04-DEC-E04",
        stem=("Antara fungsi berikut, yang manakah merangkumi kerja menstabilkan tanah dan "
              "menguruskan aliran air?"),
        superseded_stem=("Modul menyenaraikan empat kumpulan fungsi landskap kejur. Kumpulan "
                         "manakah yang merangkumi kerja menstabilkan tanah dan menguruskan "
                         "aliran air?"),
        options=["Pengurusan Ruang dan Sirkulasi", "Fungsi Struktur dan Kejuruteraan",
                 "Kebolehgunaan dan Kemudahan", "Estetika dan Reka Bentuk"],
        options_authorship="CAIR_DRAFT_UNCHANGED_BY_AUTHORITY",
        key=[1], source_rows=_rows(81, 100)),
    dict(
        qid="T04-QZ-Q5", n=5, qtype="MULTIPLE_RESPONSE", decision="T04-DEC-E05",
        # Stem provenance downgraded in Stage 4.2F-B0.9.1 — see T04-COR-04. Bariah wrote the
        # superseded_stem_b09 below in AUTH-EV-01 §E; this wording was put to her as a fixed
        # premise ("Stem kekal") in the E-07 forced choice and was not contested.
        stem=("Pilih SEMUA pernyataan yang tepat tentang kawalan semasa aktiviti semburan "
              "racun."),
        superseded_stem=("Pilih SEMUA kawalan yang mesti dipatuhi oleh kontraktor semasa "
                         "aktiviti semburan racun, mengikut modul."),
        superseded_stem_b09=("Pilih SEMUA kawalan yang mesti dipatuhi oleh kontraktor semasa "
                             "aktiviti semburan racun."),
        stem_provenance="FIRDAUS_DIRECTED_PRESENTED_AS_FIXED_NOT_CONTESTED_BY_AUTHORITY",
        options=["Pengendali semburan mesti berlesen atau telah menerima latihan",
                 "Pekerja mesti memakai PPE yang lengkap dan bersesuaian",
                 "Semburan hanya dilakukan semasa cuaca tenang",
                 "Salinan Helaian Data Keselamatan (SDS) disimpan di tapak",
                 # E-07 SET B, selected by Bariah. Verbatim from the enumerated choice.
                 "Semburan dijadualkan pada waktu petang tanpa mengambil kira keadaan cuaca",
                 "Semua racun dibeli daripada satu pembekal tunggal"],
        options_authorship="AUTHORITY_SELECTED_FROM_EXPLICIT_OPTIONS",
        key=[0, 1, 2, 3], source_rows=_rows(65, 67) + _rows(68, 74) + _rows(75, 78)),
]

# The two options Bariah ordered changed, and what finally replaced them.
#
# THREE GENERATIONS, ALL KEPT. `superseded_text` is the original fertiliser distractor she
# rejected in the DOCX. `cair_draft_superseded_by_e07` is the wording CAIR wrote under her
# instruction in Stage 4.2F-B0.9 — never approved. `replacement_text` is Set B, which she
# selected explicitly in the E-07 forced choice, verbatim. Only the last one is in force.
QUIZ_Q5_OPTION_SUBSTITUTIONS = [
    dict(position=5, previous_letter="E",
         e07_status="SELECTED_AS_SET_B",
         superseded_text="Baja disimpan di tempat yang kering dan jauh dari sumber air",
         replacement_text=("Semburan dijadualkan pada waktu petang tanpa mengambil kira "
                           "keadaan cuaca"),
         cair_draft_superseded_by_e07=("Semburan dijadualkan pada waktu petang selepas waktu "
                                       "kerja tapak tamat"),
         why_superseded=("Bariah: the option is obviously wrong because it is about "
                         "fertiliser, not about controls during pesticide spraying."),
         why_the_replacement_works=(
             "It is about pesticide spraying, so it no longer gives itself away by subject, "
             "and it is not a control the module states as mandatory. Bariah chose this "
             "wording over the Set A alternative and called the pair 'better distractors'."),
         authorship="AUTHORITY_SELECTED_FROM_EXPLICIT_OPTIONS",
         approval_status="CLOSED_BY_E07_SET_B_SELECTION"),
    dict(position=6, previous_letter="F",
         e07_status="SELECTED_AS_SET_B",
         superseded_text="Rekod pembajaan disimpan sebagai bukti kerja untuk tuntutan bayaran",
         replacement_text="Semua racun dibeli daripada satu pembekal tunggal",
         cair_draft_superseded_by_e07=("Semua racun dibeli daripada satu pembekal tunggal "
                                       "yang dilantik projek"),
         why_superseded=("Bariah: same defect — a fertiliser record, obviously outside the "
                         "scope of pesticide spraying controls."),
         why_the_replacement_works=(
             "A procurement condition, phrased about pesticide. A learner has to reason about "
             "what the control is for rather than about what the option mentions. Selected by "
             "Bariah as part of Set B."),
         authorship="AUTHORITY_SELECTED_FROM_EXPLICIT_OPTIONS",
         approval_status="CLOSED_BY_E07_SET_B_SELECTION"),
]

QUIZ_Q5_ROUTE_CHOICE = dict(
    resolved_by="E-07 forced choice — see E07_CLOSURE in t04_supplementary_evidence_v1",
    resolution="The route question is moot. Bariah was later shown two explicit option pairs "
               "against a fixed stem and selected one, which settles both the route and the "
               "wording.",
    authority_gave_two_routes=True,
    authority_quote="Tukar pilihan 5 dan 6 (E dan F), kerana jelas ia pilihan yang salah. "
                    "(kerana ia tentang baja) ATAU tukar soalan.",
    route_taken="CHANGE_THE_TWO_OPTIONS",
    route_not_taken="CHANGE_THE_QUESTION",
    why=("Bariah supplied a replacement Q5 stem in the same comment field. Changing the "
         "question as well would discard wording she wrote herself, so the option route is "
         "the only one consistent with the rest of her decision."),
    chosen_by="CAIR",
    approval_status="PENDING_BARIAH_CONFIRMATION")


def _quiz_items():
    out = []
    for q in _QUIZ:
        mr = q["qtype"] == "MULTIPLE_RESPONSE"
        opts = []
        for i, text in enumerate(q["options"]):
            opts.append(dict(
                option_id=f"{q['qid']}-OPT-{i + 1}",
                position=i + 1,
                # QUIZ-GLOBAL-02: letter labels only on single-answer items.
                display_marker=("checkbox" if mr else _LETTER[i]),
                letter_label=(None if mr else _LETTER[i]),
                text_ms=text,
                proposed_key=(i in q["key"]),
                key_status=ANSWER_KEY_STATUS))
        out.append(dict(
            question_id=q["qid"],
            position=q["n"],
            question_type=q["qtype"],
            stem_ms=q["stem"],
            superseded_stem_ms=q["superseded_stem"],
            superseded_stem_b09=q.get("superseded_stem_b09"),
            stem_provenance=q.get("stem_provenance", "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"),
            stem_authorship=q.get("stem_provenance", "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT"),
            stem_decision_id=q["decision"],
            options=opts,
            option_count=len(opts),
            options_authorship=q["options_authorship"],
            option_marker_style=("CHECKBOX" if mr else "LETTER"),
            proposed_key_positions=[i + 1 for i in q["key"]],
            answer_key_status=ANSWER_KEY_STATUS,
            source_row_ids=list(q["source_rows"]),
            global_rules_applied=[r["rule_id"] for r in QUIZ_GLOBAL_RULES
                                  if q["qid"] in r["applied_to_t04_items"]],
            content_status="FROZEN_UNDER_AUTHORITY_DECISION"))
    return out


FINAL_QUIZ = dict(
    quiz_id="T04-QZ-FINAL",
    screen_id="T04-S21",
    version="v2",
    composition="4 MCQ dan 1 Multiple Response",
    pass_mark=QUIZ_PASS_MARK,
    scope=QUIZ_SCOPE,
    answer_key_status=ANSWER_KEY_STATUS,
    answer_key_status_reason=("Bariah's own review package states 'Cadangan jawapan sahaja — "
                              "belum muktamad' and she did not mark any key final."),
    items=_quiz_items(),
    item_count=len(_QUIZ),
    global_rules=[r["rule_id"] for r in QUIZ_GLOBAL_RULES],
    q5_option_substitutions=QUIZ_Q5_OPTION_SUBSTITUTIONS,
    q5_route_choice=QUIZ_Q5_ROUTE_CHOICE,
    content_status="FROZEN_UNDER_AUTHORITY_DECISION")

QUIZ_ITEM_FIELDS = ["question_id", "position", "question_type", "stem_ms",
                    "superseded_stem_ms", "stem_authorship", "options", "option_marker_style",
                    "proposed_key_positions", "answer_key_status", "source_row_ids",
                    "global_rules_applied", "content_status"]


def quiz_items():
    return _quiz_items()


# ==========================================================================================
# PART 9 — FINAL VISUAL SCOPE
# ==========================================================================================
VISUAL_SCOPE_STATUS = "ACCEPTED_AS_A_SET_WITH_CONDITIONS"
DECISION_BASIS_VALUES = ["INSTRUCTIONAL_ONLY", "PRODUCTION_ONLY",
                         "BOTH_INSTRUCTIONAL_AND_PRODUCTION"]

# CORRECTED IN STAGE 4.2F-B1 (T04-COR-05). The HSE item was typed here as T04-VO-039, which
# is actually "Perundangan dan Pelesenan". The obligation whose subject is the pesticide PPE
# set — and which the closure itself already marks DO_NOT_REUSE — is T04-VO-040. The IDs are
# now cross-checked against the closure by a gate rather than trusted as typed.
_DO_NOT_REUSE = [
    ("T04-VO-025", "Pengurusan Stok dan Penyimpanan (Baja)", "AG-04",
     "Penyimpanan baja (kering, selamat, jauh dari air) berbeza daripada penyimpanan racun "
     "(berkunci, berlabel, berpengudaraan)."),
    ("T04-VO-026", "Keselamatan Pekerja (Baja)", "AG-04",
     "PPE untuk baja (sarung tangan, topeng muka) berbeza daripada PPE untuk racun (topeng "
     "pernafasan, cermin mata, sarung tangan kimia, sut pelindung)."),
    ("T04-VO-040", "Keselamatan dan Kesihatan (HSE) (Racun — pematuhan)", "AG-06",
     "Set PPE racun jauh lebih berat dan tidak boleh dikongsi dengan skrin baja."),
]


def _do_not_reuse_items():
    return [dict(
        obligation_id=oid,
        label=label,
        asset_group_id=ag,
        restriction="REUSE_NOT_ALLOWED",
        restriction_scope="NAMED_ITEM_NOT_WHOLE_GROUP",
        visual_difference=diff,
        # Bariah asked for this line on every do-not-reuse item, and confirmed all three from
        # both lenses in the same comment.
        decision_basis="BOTH_INSTRUCTIONAL_AND_PRODUCTION",
        decision_basis_source_decision="T04-DEC-B04",
        decision_basis_requirement_decision="T04-DEC-B06",
        instructional_ground=("Learners must not confuse the two PPE sets or the two storage "
                              "regimes; a shared visual would blur a distinction the learner "
                              "is expected to make."),
        production_ground=("The two visuals differ substantially in content, so a shared "
                           "asset would not in fact save production effort."),
        confirmed_by_authority=True) for oid, label, ag, diff in _DO_NOT_REUSE]


DO_NOT_REUSE_ITEMS = _do_not_reuse_items()


def _asset_group_scope():
    out = []
    for g in C.ASSET_GROUPS:
        gid = g["asset_group_id"]
        restricted = [x for x in _do_not_reuse_items() if x["asset_group_id"] == gid]
        out.append(dict(
            asset_group_id=gid,
            label=g["label"],
            proposed_unique_assets=g["proposed_unique_assets"],
            affected_screens=list(g["affected_screens"]),
            reuse_decision="REUSE_WITH_CONDITIONS",
            reuse_decision_id="T04-DEC-B03",
            item_level_restrictions=[x["obligation_id"] for x in restricted],
            item_level_restriction_labels=[x["label"] for x in restricted],
            restriction_applies_to_whole_group=False,
            mmd_production_status="NOT_STARTED"))
    return out


def asset_group_scope():
    return _asset_group_scope()


FINAL_VISUAL_SCOPE = dict(
    governance_id="T04-VIS-GOV-01",
    status=VISUAL_SCOPE_STATUS,
    decision_ids=["T04-DEC-B01", "T04-DEC-B02", "T04-DEC-B03", "T04-DEC-B04", "T04-DEC-B05",
                  "T04-DEC-B06"],
    authority="BARIAH_AHMAD",
    source_artifact="AUTH-EV-01 §B, KOMEN KESELURUHAN",
    visual_obligation_count=C.ASSET_TOTALS["visual_obligation_count"],
    asset_group_count=C.ASSET_TOTALS["asset_group_count"],
    proposed_unique_assets=C.ASSET_TOTALS["proposed_unique_assets"],
    accepted_production_scope=41,
    accepted_production_scope_quote="Kaedah kiraan 46 → 41 diterima sebagai skop produksi.",
    obligations_are_not_assets=C.ASSET_TOTALS["obligations_are_not_assets"],
    review_lenses=["INSTRUCTIONAL", "MULTIMEDIA_PRODUCTION"],
    precedence_rule=dict(
        rule_id="T04-VIS-PREC-01",
        decision_id="T04-DEC-B05",
        rule="Where the instructional and production lenses conflict, the instructional "
             "decision governs and the assets are not merged.",
        authority_quote=("Di mana dua sudut bertembung (jika ada): keputusan instruksional "
                         "mengatasi pengoptimuman produksi."),
        binding_on="every subsequent T04 asset merge or reuse decision"),
    do_not_reuse_items=DO_NOT_REUSE_ITEMS,
    do_not_reuse_count=len(_DO_NOT_REUSE),
    asset_groups=asset_group_scope(),
    what_is_not_approved=(
        "Individual asset subjects, styles and the MMD production plan. Bariah accepted the "
        "grouping, the 46→41 derivation and the three do-not-reuse rulings as a set; she did "
        "not approve any specific artwork, and no asset has been produced."),
    new_screen_asset_impact=dict(
        screen_id="T04-S14",
        new_unique_assets=0,
        why=("The inserted screen realises T04-VO-038, a grouping heading already closed as "
             "NOT_A_SEPARATE_ASSET_WITH_REASON. Bariah asked for a navigation screen listing "
             "three aspects, not for a new picture. The accepted production scope stays 41."),
        obligation_id="T04-VO-038",
        obligation_closure_outcome_unchanged=True),
    content_status="FROZEN_UNDER_AUTHORITY_DECISION")

# ==========================================================================================
# PART 10 — SOURCE STATUS
# ==========================================================================================
SOURCE_STATUS = dict(
    CONTROLLED_EXTRACT_SOURCE_BINDINGS="PRESENT",
    ORIGINAL_DOCX_ROUND_TRIP_REPRODUCIBILITY="OPEN",
    SOURCE_DOCX_RETRIEVAL_AND_HASH_PROOF="OPEN",
)

SOURCE_RISK_TOKEN = "SOURCE_REPRODUCIBILITY_OPEN_NONBLOCKING_FOR_T04_STORYBOARD_BUILD"

SOURCE_STATUS_DETAIL = dict(
    bindings_present_evidence=(
        "Every content screen in the final sequence names the controlled-extract rows it "
        "rests on, and every named row resolves in the extract. A gate asserts both."),
    what_is_open=(
        "The original module DOCX has not been re-retrieved in this session and its hash has "
        "not been re-proven against the extract that was taken from it. So the extract is "
        "internally consistent and fully bound, but its fidelity to the original file is "
        "asserted from an earlier stage rather than re-demonstrated here."),
    why_non_blocking=(
        "The storyboard build consumes the controlled extract, not the original DOCX. Every "
        "row it needs is present and bound. If the round trip later shows a discrepancy, the "
        "affected rows are identifiable by ID and the screens that use them are listed — so "
        "the risk is bounded and repairable rather than open-ended."),
    what_would_close_it=(
        "Retrieve the original module DOCX, hash it, re-run the extraction and compare the "
        "row set to T04_SOURCE_EXTRACT_v1.json."),
    must_not_be_recorded_as="SOURCE_UNSUPPORTED",
    why_not=("The final content is source-bound: the bindings exist, resolve and are checked. "
             "SOURCE_UNSUPPORTED would assert the opposite of what the gates observe."),
    risk_owner="FIRDAUS",
    blocking=False)

# ==========================================================================================
# PART 11 — FINAL CONTENT MODEL STATES
# ==========================================================================================
FINAL_STATE_VALUES = [
    "APPROVED_WITH_SPECIFIED_AMENDMENTS",
    "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT_FROZEN",
    "CAIR_EXECUTED_UNDER_AUTHORITY_INSTRUCTION_PENDING_CONFIRMATION",
    "PROPOSED_NOT_FINAL",
    "ACCEPTED_AS_A_SET_WITH_CONDITIONS",
    "AUTHORITY_ISSUED_COURSE_WIDE",
    "PRESENT_WITH_OPEN_REPRODUCIBILITY_RISK",
    "AUTHORITY_SELECTED_FROM_EXPLICIT_OPTIONS_FROZEN",
]

_FINAL_STATES = [
    ("FS-01", "FINAL_SCREEN_SEQUENCE", "APPROVED_WITH_SPECIFIED_AMENDMENTS",
     "22 screens, one inserted and eight renumbered, each carrying its decision IDs.",
     ["T04-DEC-A01", "T04-DEC-A14", "T04-DEC-A22"], True),
    ("FS-02", "FINAL_SCREEN_TREATMENTS", "APPROVED_WITH_SPECIFIED_AMENDMENTS",
     "Four treatments changed by direct authority instruction: T04-S12, T04-S13, T04-S16, "
     "T04-S17.",
     ["T04-DEC-A12", "T04-DEC-A13", "T04-DEC-A16", "T04-DEC-A17"], True),
    ("FS-03", "FINAL_UNIT_LABELLING", "APPROVED_WITH_SPECIFIED_AMENDMENTS",
     "Learner sees Topik 4 with no Bahagian; internal ID K5-PL06-T04-B01 unchanged; the "
     "closing screen reads Tamat Topik.",
     ["T04-DEC-A01", "T04-DEC-A22"], True),
    ("FS-04", "FINAL_DIALOGUE", "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT_FROZEN",
     "Four lines, written by Bariah, carried verbatim. Five became four.",
     ["T04-DEC-C01", "T04-DEC-C02", "T04-DEC-C03"], True),
    ("FS-05", "FINAL_RUMUSAN", "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT_FROZEN",
     "Three beats, written by Bariah, carried verbatim. Four points became three.",
     ["T04-DEC-D01", "T04-DEC-D02"], True),
    ("FS-06", "FINAL_QUIZ_STEMS", "AUTHORITY_SUPPLIED_REPLACEMENT_TEXT_FROZEN",
     "All five stems replaced with Bariah's wording, carried verbatim.",
     ["T04-DEC-E01", "T04-DEC-E02", "T04-DEC-E03", "T04-DEC-E04", "T04-DEC-E05"], True),
    ("FS-07", "FINAL_QUIZ_Q5_OPTIONS", "AUTHORITY_SELECTED_FROM_EXPLICIT_OPTIONS_FROZEN",
     "Options 5 and 6 are Set B, selected by Bariah from an enumerated forced choice and "
     "carried verbatim. The CAIR draft that stood here in Stage 4.2F-B0.9 is superseded.",
     ["T04-DEC-E08", "T04-DEC-E09"], True),
    ("FS-08", "FINAL_QUIZ_ANSWER_KEY", "PROPOSED_NOT_FINAL",
     "No answer key was marked final by the authority. All five remain proposals.",
     ["T04-DEC-X02"], False),
    ("FS-09", "FINAL_VISUAL_SCOPE", "ACCEPTED_AS_A_SET_WITH_CONDITIONS",
     "41 proposed unique assets across 8 groups, conditional sharing, three named "
     "do-not-reuse items, instructional precedence.",
     ["T04-DEC-B01", "T04-DEC-B03", "T04-DEC-B04", "T04-DEC-B05", "T04-DEC-B06"], True),
    ("FS-10", "FINAL_SOURCE_BINDINGS", "PRESENT_WITH_OPEN_REPRODUCIBILITY_RISK",
     "Bindings present and resolving; original-DOCX round trip and hash proof remain open and "
     "non-blocking.",
     [], True),
]


def final_states():
    out = []
    for sid, name, state, note, decs, settled in _FINAL_STATES:
        if state not in FINAL_STATE_VALUES:
            raise RuntimeError(f"{sid}: unknown final state {state}")
        out.append(dict(state_id=sid, content_class=name, final_state=state, note=note,
                        decision_ids=list(decs), settled=settled))
    return out


FINAL_STATES = final_states()
COURSE_WIDE_STATE = dict(
    state_id="FS-11-GLOBAL",
    content_class="COURSE_WIDE_QUIZ_RULES",
    final_state="AUTHORITY_ISSUED_COURSE_WIDE",
    note="QUIZ-GLOBAL-01 and QUIZ-GLOBAL-02 apply to every PL in the Kursus. Only their T04 "
         "application is executed in this stage.",
    decision_ids=["T04-DEC-E06", "T04-DEC-E07"],
    settled=True)

# ==========================================================================================
# PART 12 — RECONCILIATION TARGETS
# ==========================================================================================
# Facts that are now false. Any artifact still asserting one of these is stale. The QA suite
# scans the emitted artifact set for each, and every occurrence must be inside an explicitly
# superseded-history context.
SUPERSEDED_FACTS = [
    dict(fact_id="SF-01", stale_claim="21 screens",
         detect=["21 skrin", "21 screens", "21-screen"],
         now="22 screens", decision_id="T04-DEC-A14"),
    dict(fact_id="SF-02", stale_claim="the closing screen is Tamat Bahagian",
         detect=["Tamat Bahagian"], now="Tamat Topik", decision_id="T04-DEC-A22"),
    dict(fact_id="SF-03", stale_claim="five dialogue lines",
         detect=["lima baris perbualan", "five dialogue lines"],
         now="four dialogue lines", decision_id="T04-DEC-C01"),
    dict(fact_id="SF-04", stale_claim="four Rumusan points",
         detect=["empat ayat rumusan", "empat ayat", "four Rumusan points"],
         now="three Rumusan beats", decision_id="T04-DEC-D01"),
    dict(fact_id="SF-05", stale_claim="the old Q5 option set with fertiliser distractors",
         detect=["Baja disimpan di tempat yang kering",
                 "Rekod pembajaan disimpan sebagai bukti kerja"],
         now="the amended Q5 option set", decision_id="T04-DEC-E08"),
    dict(fact_id="SF-06", stale_claim="the inserted screen adds a new unique asset",
         detect=["new S14 asset", "aset baharu untuk S14"],
         now="the inserted screen adds no unique asset; scope stays 41",
         decision_id="T04-DEC-B01"),
    dict(fact_id="SF-07", stale_claim="the old T04-S14 to T04-S21 numbering",
         detect=["T04-S21 — Tamat Bahagian", "T04-S20 | Kuiz", "T04-S19 | Rumusan"],
         now="T04-S15 to T04-S22", decision_id="T04-DEC-A15"),
]

# Artifacts written before this stage that describe the superseded position. They are not
# rewritten — they are the record of what was true then — but every one is listed here with
# the artifact that supersedes it, so nothing downstream reads a stale file as current.
SUPERSEDED_ARTIFACTS = [
    dict(path="docs/pl06/t04/T04_PROPOSED_SCREEN_SEQUENCE_v1.json",
         superseded_by="docs/pl06/t04/T04_FINAL_SCREEN_SEQUENCE_v2.json",
         stale_facts=["SF-01", "SF-02", "SF-07"]),
    dict(path="docs/pl06/t04/T04_PROPOSED_SCREEN_SEQUENCE_v1.md",
         superseded_by="docs/pl06/t04/T04_FINAL_SCREEN_SEQUENCE_v2.md",
         stale_facts=["SF-01", "SF-02", "SF-07"]),
    dict(path="docs/pl06/t04/T04_SLIDE_2_DIALOGUE_CAIR_DRAFT_v1.json",
         superseded_by="docs/pl06/t04/T04_FINAL_DIALOGUE_v1.json",
         stale_facts=["SF-03"]),
    dict(path="docs/pl06/t04/T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v3.json",
         superseded_by="docs/pl06/t04/T04_FINAL_RUMUSAN_v1.json",
         stale_facts=["SF-04"]),
    dict(path="docs/pl06/t04/T04_QUIZ_CAIR_ASSISTED_DRAFT_v1.json",
         superseded_by="docs/pl06/t04/T04_FINAL_QUIZ_v2.json",
         stale_facts=["SF-05"]),
    dict(path="docs/pl06/t04/T04_BARIAH_REVIEW_MODEL_v1.json",
         superseded_by="docs/pl06/t04/T04_AUTHORITY_DECISION_REGISTER_v1.json",
         stale_facts=["SF-01", "SF-02", "SF-03", "SF-04", "SF-05", "SF-07"]),
    dict(path="reviews/storyboard-bariah/t04_bariah_review/T04_Pakej_Semakan_Bariah_v2.docx",
         superseded_by="reviews/storyboard-bariah/t04_bariah_review/"
                       + PRIMARY_DOCX_NAME,
         stale_facts=["SF-01", "SF-02", "SF-03", "SF-04", "SF-05", "SF-07"]),
]

# Artifacts this stage emits. These MUST be free of every superseded fact except where the
# fact is quoted inside an explicit supersession record.
NEW_ARTIFACTS = [
    "T04_AUTHORITY_EVIDENCE_REGISTER_v1.json",
    "T04_AUTHORITY_EVIDENCE_REGISTER_v1.md",
    "T04_AUTHORITY_CONFIRMATIONS_v1.json",
    "T04_AUTHORITY_CONFIRMATIONS_v1.md",
    "T04_AUTHORITY_DECISION_REGISTER_v1.json",
    "T04_AUTHORITY_DECISION_REGISTER_v1.md",
    "T04_FINAL_SCREEN_SEQUENCE_v2.json",
    "T04_FINAL_SCREEN_SEQUENCE_v2.md",
    "T04_FINAL_DIALOGUE_v1.json",
    "T04_FINAL_DIALOGUE_v1.md",
    "T04_FINAL_RUMUSAN_v1.json",
    "T04_FINAL_RUMUSAN_v1.md",
    "T04_QUIZ_GLOBAL_RULES_v1.json",
    "T04_QUIZ_GLOBAL_RULES_v1.md",
    "T04_FINAL_QUIZ_v2.json",
    "T04_FINAL_QUIZ_v2.md",
    "T04_FINAL_VISUAL_SCOPE_v1.json",
    "T04_FINAL_VISUAL_SCOPE_v1.md",
    "T04_SOURCE_STATUS_v1.json",
    "T04_SOURCE_STATUS_v1.md",
    "T04_FINAL_CONTENT_MODEL_v1.json",
    "T04_FINAL_CONTENT_MODEL_v1.md",
    "T04_AUTHORITY_RECONCILIATION_v1.json",
    "T04_AUTHORITY_RECONCILIATION_v1.md",
]

# ==========================================================================================
# PRODUCTION GUARDS
# ==========================================================================================
PPTX_GENERATED = 0
GENERATOR_TOUCHED = 0
MMD_PRODUCTION_STARTED = 0
REACT_OR_SCORM_STARTED = 0
AUTHORITY_ARTIFACTS_MODIFIED = 0

FORBIDDEN_LABELS = [
    "PRODUCTION_APPROVED", "CANONICAL_FREEZE", "MMD_BUILD_READY",
    "SOURCE_INTEGRITY_FULLY_VERIFIED", "MICROSOFT_POWERPOINT_EQUIVALENCE",
    "SOURCE_GOVERNANCE_COMPLETE", "SOURCE_UNSUPPORTED", "BARIAH_ORIGINATED_RULE",
]
FORBIDDEN_LABEL_DECLARATION = (
    "These strings must not be applied to any record in this stage. This list is the "
    "declaration that they are forbidden; it is not a use of them.")

# Open items that this stage does NOT close.
OPEN_AFTER_THIS_STAGE = [
    dict(open_id="E-02", subject="Quiz answer key for all five items",
         owner="BARIAH", why_open="Recorded as 'cadangan jawapan sahaja' in the package. The "
                                  "E-07 forced choice explicitly left the four correct "
                                  "answers untouched and asked only about the two incorrect "
                                  "options, so it does not close this."),
    dict(open_id="E-04", subject="The pembajaan-to-racun wording correction on T04-S14",
         owner="BARIAH", why_open="Correction applied and recorded; confirmation outstanding."),
    dict(open_id="E-05", subject="Original module DOCX round trip and hash proof",
         owner="FIRDAUS", why_open="Not re-run in this session; non-blocking."),
    dict(open_id="E-06", subject="Individual asset subjects and styles",
         owner="BARIAH", why_open="The set was accepted; no artwork has been approved."),
]

# Items closed since Stage 4.2F-B0.9, each naming what closed it.
CLOSED_SINCE_B0_9 = [
    dict(open_id="E-01", subject="Q5 replacement options E and F",
         closed_by="E-07 forced choice — Bariah selected Set B",
         closing_record="T04-DEC-E09"),
    dict(open_id="E-03", subject="The 'Q3' WhatsApp referent",
         closed_by="T04-COR-02 — the line is Firdaus's, so there is no authority referent to "
                   "resolve",
         closing_record="T04-COR-02"),
    dict(open_id="E-07", subject="Which Q5 six-option set stands",
         closed_by="E-07 forced choice — Set B, verbatim",
         closing_record="T04-DEC-E09"),
]

VERDICT = "T04_CONTENT_APPROVED_READY_FOR_STORYBOARD_BUILD"
ALLOWED_VERDICTS = [VERDICT, "T04_AUTHORITY_DECISION_INGESTION_BLOCKED"]
