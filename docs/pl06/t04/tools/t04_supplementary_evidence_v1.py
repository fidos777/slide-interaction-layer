# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.9.1 — supplementary WhatsApp evidence: custody attempt and visual reading.

TWO SEPARATE QUESTIONS, ANSWERED SEPARATELY
-------------------------------------------
1. CUSTODY — is there a file to hash, measure, copy and freeze?  **NO.**
2. CONTENT — can the exchange be read?                            **YES**, from the rendered
   image, by visual inspection.

Those are not the same question and this stage does not let one stand in for the other. The
screenshot reached this run as a rendered image in the conversation, not as a file on disk.
An exhaustive filesystem search found no PNG, JPG or WEBP anywhere newer than the previous
stage's DOCX upload. So every field that can only come from a binary — byte size, SHA-256,
MIME type, pixel dimensions, format validation, byte-identity of a custody copy — is
`NOT_AVAILABLE_NO_BINARY`. None of them is estimated, reconstructed or inferred.

WHAT THIS MEANS FOR THE STATUS UPGRADE
--------------------------------------
Stage 4.2F-B0.9.1 conditions the upgrade to `AUTHORITY_DIRECT_SCREENSHOT` on the PNG identity
passing verification. It cannot pass. The three confirmations therefore keep an evidence class
that describes what actually happened, and the `NOT_SUPPLIED` custody state stands.

WHAT THE VISUAL READING DID ESTABLISH
-------------------------------------
Something the transcript-only reading in Stage 4.2F-B0.9 got wrong: **"Q3 tu nnt u pilih ya"
was sent by Firdaus, not by Bariah.** It is green, right-aligned and carries the sent/read
double tick. Stage 4.2F-B0.9 recorded it as a Bariah delegation. That is a misattribution of
authorship in a governance record and it is corrected here.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)

import t04_authority_data_v1 as A   # noqa: E402

STAGE = "4.2F-B0.9.1"
SUITE_ID = "T04_SUPPLEMENTARY_EVIDENCE_QA_v1"
GENERATED_BY = "docs/pl06/t04/tools/t04_supplementary_evidence_emit_v1.py"

# ==========================================================================================
# PART A.1 — CUSTODY ATTEMPT
# ==========================================================================================
CUSTODY_OUTCOME = "FAILED_NO_BINARY_SUPPLIED"
CUSTODY_ATTEMPTS = 2

# SECOND INTAKE ATTEMPT — Stage 4.2F-B0.9.1 re-run
# ------------------------------------------------
# The follow-up brief supplies an expected identity for the PNG. Those values are recorded as
# EXPECTED, supplied by Firdaus. They are NOT measurements: there is still no file to measure,
# so nothing here was read from a binary and nothing here is verified. The distinction is the
# whole point — a recorded expectation that later turns out to match is evidence; a recorded
# expectation presented as a measurement is a fabrication.
EXPECTED_IDENTITY = dict(
    supplied_by="FIRDAUS_IN_THE_STAGE_BRIEF",
    verified=False,
    verification_outcome="CANNOT_VERIFY_NO_BINARY",
    filename="Screenshot 2026-08-03 at 12.46.32 PM.png",
    byte_size=804017,
    sha256="3f992b274decb4ac46b6a2a6193bdadadeffbd99bdd101341cb4dad4f3e90301",
    image_format="PNG",
    pixel_width=1150,
    pixel_height=1536,
    note=("Fail-closed was requested if byte size, SHA-256, format or dimensions differ. "
          "None of the four could be compared, because there is no file. The stage fails "
          "closed on the stronger ground that the comparison was impossible, not that it "
          "disagreed."))

INTENDED_CUSTODY_PATH = (A.EVIDENCE_DIR
                         + "/T04_BARIAH_WHATSAPP_CONFIRMATION_2026-08-03.png")

SEARCH_LOCATIONS = [
    dict(location="/mnt/data",
         result="DOES_NOT_EXIST",
         note="Named in the stage brief. This environment has no such mount, as was already "
              "recorded in Stage 4.2F-B0.9."),
    dict(location="/root/.claude/uploads/12837c42-b6ab-597b-8301-85c5b457471b/",
         result="NO_IMAGE_NEWER_THAN_THE_PREVIOUS_STAGE",
         note="21 files. The newest is 698bf575-T04_Pakej_Semakan_Bariah_v3_vBariah.docx at "
              "2026-08-03 02:28. No PNG, JPG or WEBP was added for this stage."),
    dict(location="whole filesystem, one device, modified after 2026-08-03 02:29",
         result="NO_MATCHING_IMAGE",
         note="find over png/webp/jpg excluding system and vendor trees returned nothing."),
    dict(location="/root/.claude/projects/<session>/tool-results/",
         result="NO_IMAGE",
         note="Two cached tool-result text files, neither an image."),
    dict(location="/root/.claude/uploads/… — SECOND ATTEMPT after the follow-up brief",
         result="DIRECTORY_UNCHANGED",
         note="Re-checked after the follow-up brief declared the PNG a real binary file. The "
              "uploads directory is byte-for-byte the same as at the previous attempt: 21 "
              "files, newest still the 02:28 authority DOCX. A second whole-filesystem sweep "
              "for images newer than 02:29 also returned nothing."),
]

CUSTODY_FIELDS = [
    dict(field="original_runtime_path", value="NOT_AVAILABLE_NO_BINARY",
         why="The image was rendered into the conversation, not written to disk."),
    dict(field="repository_custody_path", value="NOT_CREATED",
         why="Nothing to copy. An empty or reconstructed file would be a forgery, not "
             "custody."),
    dict(field="byte_size", value="NOT_AVAILABLE_NO_BINARY", why="No file to measure."),
    dict(field="sha256", value="NOT_AVAILABLE_NO_BINARY", why="No bytes to hash."),
    dict(field="mime_type", value="NOT_AVAILABLE_NO_BINARY",
         why="No file header to read. The conversation labels it a PNG; that is a label, not "
             "a measurement, and it is not recorded as one."),
    dict(field="pixel_width", value="NOT_AVAILABLE_NO_BINARY", why="No image header."),
    dict(field="pixel_height", value="NOT_AVAILABLE_NO_BINARY", why="No image header."),
    dict(field="file_format_validation", value="NOT_PERFORMED_NO_BINARY",
         why="Nothing to validate."),
    dict(field="intake_time", value="NOT_APPLICABLE_NO_INTAKE",
         why="No file was taken in, so there is no intake event to timestamp."),
    dict(field="byte_identity_vs_source", value="NOT_VERIFIABLE_NO_BINARY",
         why="A custody copy can only be compared against a source that exists."),
]

# The three timestamp classes the brief requires be kept apart. Only the first has any value.
TIMESTAMP_CLASSES = [
    dict(timestamp_class="VISIBLE_IN_SCREENSHOT",
         available=True,
         values=["7:17 AM", "7:18 AM", "7:20 AM", "7:20 AM", "7:21 AM"],
         date_shown="Today (the thread's own date separator; the calendar date is not "
                    "rendered in the captured region)",
         basis="read from the rendered pixels",
         note="These are the times WhatsApp displays beside each bubble. They are evidence "
              "of message ordering within the conversation, nothing more. They are not file "
              "timestamps and are not treated as any."),
    dict(timestamp_class="RUNTIME_FILESYSTEM",
         available=False,
         values="NOT_AVAILABLE_NO_BINARY",
         basis=None,
         note="There is no file, so there is no mtime, ctime or atime."),
    dict(timestamp_class="IMAGE_METADATA_EXIF",
         available=False,
         values="NOT_AVAILABLE_NO_BINARY",
         basis=None,
         note="No EXIF was read and none is asserted. WhatsApp screenshots frequently carry "
              "none at all, but that is a general remark and not a finding about this file."),
]

# ==========================================================================================
# PART A.2 — VISUAL READING OF THE EXCHANGE
# ==========================================================================================
READING_METHOD = dict(
    method="DIRECT_VISUAL_INSPECTION_OF_THE_RENDERED_IMAGE",
    ocr_used=False,
    ocr_as_sole_evidence=False,
    speaker_attribution_basis=(
        "WhatsApp bubble geometry and colour: outgoing messages are green, right-aligned and "
        "carry the sent/read tick pair; incoming messages are white and left-aligned under "
        "the contact header 'Bariah eLearning'."),
    limitations=[
        "Read from a rendered image, with no binary to hash — so the reading cannot be tied "
        "to a file identity, and a second run cannot re-derive it from custody.",
        "The calendar date is not rendered in the captured region; the thread shows only the "
        "'Today' separator. The date 3 August 2026 comes from the stage brief, not from the "
        "pixels.",
        "The captured region begins mid-message. The top of Firdaus's 7:17 message is cut "
        "off, though its content is separately visible in the two companion images.",
    ])

# Every message visible in the captured region, in order.
_MESSAGES_UNSORTED = [
    dict(msg_id="WA-01", position=1, time_shown="7:17 AM",
         sender="FIRDAUS", direction="OUTGOING",
         bubble="green, right-aligned, sent/read ticks",
         summary=("A forwarded decision summary plus three numbered confirmation requests. "
                  "The summary restates the Stage 4.2F-B0.9 outcome: 22 skrin with the new "
                  "Racun screen before Perundangan dan Pelesenan, Tamat Topik, the four-line "
                  "dialogue, the three-beat Rumusan, Q1–Q4 wording, the two course-wide quiz "
                  "rules, and 46 keperluan → 41 aset dalam 8 kumpulan with instructional "
                  "clarity over production optimisation."),
         verbatim_fragments=[
             "Mohon sahkan tiga perkara terakhir:",
             "1. Skrin baharu Racun",
             "Dalam nota tertulis \"Tiga aspek pengurusan pembajaan untuk kontraktor\". Kami "
             "faham perkataan yang dimaksudkan ialah racun. Betul?",
             "2. Jumlah visual",
             "Kami cadangkan skrin baharu itu menggunakan semula tiga aset AG-06 sebagai "
             "skrin overview, tanpa aset unik baharu. Dengan itu jumlah kekal 41 aset. Mohon "
             "sahkan.",
             "3. Cadangan akhir Q5 — Multiple Response",
             "Cadangan jawapan betul ialah empat pilihan pertama. Mohon sahkan sama ada Q5 "
             "ini boleh digunakan atau perlu dipinda lagi.",
         ]),
    dict(msg_id="WA-02", position=2, time_shown="7:18 AM",
         sender="BARIAH", direction="INCOMING",
         bubble="white, left-aligned",
         summary="A bundled acceptance with no item enumerated.",
         verbatim_fragments=["Yes to both"]),
    dict(msg_id="WA-03", position=3, time_shown="7:20 AM",
         sender="FIRDAUS", direction="OUTGOING",
         bubble="green, right-aligned, sent/read ticks",
         summary=("Firdaus defers his own third question. This is NOT a Bariah message and "
                  "NOT an authority statement."),
         verbatim_fragments=["Q3 tu nnt u pilih ya"]),
    dict(msg_id="WA-04", position=4, time_shown="7:20 AM",
         sender="FIRDAUS", direction="OUTGOING",
         bubble="green, right-aligned, sent/read ticks, quoting Bariah's 'Yes to both'",
         summary=("Firdaus asks Bariah to confirm the scope of her bundled acceptance — "
                  "whether it covered his first two questions."),
         verbatim_fragments=["Ni for first 2 Q kan"]),
    dict(msg_id="WA-06", position=6, time_shown="12:38 PM",
         sender="FIRDAUS", direction="OUTGOING",
         bubble="green, right-aligned, sent/read ticks, quoted block",
         summary=("A forced-choice request to close E-07. It fixes the stem, states that the "
                  "four correct answers are unchanged, and asks Bariah to pick between two "
                  "enumerated pairs of incorrect options. It closes 'Boleh jawab Set A atau "
                  "Set B sahaja' — answer Set A or Set B only."),
         verbatim_fragments=[
             "Salam Bariah, nak tutup satu perkara kecil untuk Q5 Topik 4.",
             "Stem kekal:",
             "\u201cPilih SEMUA pernyataan yang tepat tentang kawalan semasa aktiviti "
             "semburan racun.\u201d",
             "Empat jawapan betul kekal seperti yang telah dicadangkan. Untuk dua pilihan "
             "salah terakhir, yang mana satu kita patut kekalkan?",
             "Set A",
             "Notifikasi kepada penduduk dibuat hanya selepas semburan selesai",
             "SDS hanya perlu disimpan di pejabat projek dan tidak perlu berada di tapak",
             "Set B",
             "Semburan dijadualkan pada waktu petang tanpa mengambil kira keadaan cuaca",
             "Semua racun dibeli daripada satu pembekal tunggal",
             "Boleh jawab Set A atau Set B sahaja.",
         ]),
    dict(msg_id="WA-07", position=7, time_shown="12:40 PM",
         sender="BARIAH", direction="INCOMING",
         bubble="white, left-aligned, below the '1 unread message' separator",
         summary=("An explicit selection from two enumerated options, with a one-phrase "
                  "reason. This is the strongest evidence class in the whole exchange: the "
                  "choice set was closed, the options were written out in full, and the reply "
                  "names one of them."),
         verbatim_fragments=["Set B. Better distractors"]),
    dict(msg_id="WA-05", position=5, time_shown="7:21 AM",
         sender="BARIAH", direction="INCOMING",
         bubble="white, left-aligned, quoting her own 'Yes to both'",
         summary=("Bariah confirms the scope of her earlier acceptance and separately answers "
                  "the third question."),
         verbatim_fragments=["Yes to both screenshots. Q5 multiple response - yes, ok"]),
]

MESSAGES = sorted(_MESSAGES_UNSORTED, key=lambda m: m["position"])

# The correction this reading forces on the Stage 4.2F-B0.9 record.
ATTRIBUTION_CORRECTIONS = [
    dict(
        correction_id="T04-COR-02",
        subject="Authorship of \"Q3 tu nnt u pilih ya\"",
        recorded_in_stage="4.2F-B0.9",
        recorded_as="A Bariah message; a delegation from the authority to CAIR "
                     "(T04-CNF-03 / T04-DEC-X01, authority BARIAH_AHMAD).",
        actually="A Firdaus message (WA-03). Green, right-aligned, sent/read ticks.",
        basis=("Visual inspection of the rendered screenshot. Stage 4.2F-B0.9 had no image "
               "and read the line from a transcription in the stage brief, which carried no "
               "speaker attribution."),
        consequence=(
            "There is no Bariah delegation of a choice to CAIR anywhere in this exchange. "
            "T04-DEC-X01 must not be described as an authority act of any kind — it is "
            "Firdaus deferring his own question, and Bariah answered that question three "
            "minutes later in WA-05."),
        severity="MATERIAL_MISATTRIBUTION_OF_AUTHORSHIP",
        status="CORRECTED_IN_THIS_STAGE"),
    dict(
        correction_id="T04-COR-03",
        subject="Referent of \"Q3\"",
        recorded_in_stage="4.2F-B0.9",
        recorded_as="Ambiguous between quiz item Q3 and an unseen third item.",
        actually=("Supported reading: the THIRD of Firdaus's three numbered confirmation "
                  "requests — the Q5 Multiple Response proposal. His message enumerates "
                  "exactly three items and he wrote both messages."),
        basis="WA-01 enumerates items 1, 2, 3; WA-03 and WA-04 are both Firdaus's; WA-04 "
              "explicitly speaks of 'first 2 Q', which only makes sense against that same "
              "three-item enumeration.",
        consequence=(
            "The ambiguity is now moot rather than resolved by assertion: whichever item "
            "'Q3' named, Bariah answered the third request explicitly in WA-05. The quiz-item "
            "reading is retained as the weaker alternative and is not selected."),
        severity="INTERPRETATION_NARROWED_NOT_ASSERTED",
        status="RECORDED_IN_THIS_STAGE"),
]

# ==========================================================================================
# PART A.3 — WHAT THE EXCHANGE CONFIRMS, AT WHAT PRECISION
# ==========================================================================================
CONFIRMATION_MODES = [
    "EXPLICITLY_WORDED_INDIVIDUAL_DECISION",
    "BUNDLED_ACCEPTANCE_OF_TWO_PROPOSITIONS",
    "CAIR_PROPOSAL_CONFIRMED_BY_AUTHORITY",
    "NOT_AN_AUTHORITY_STATEMENT",
]

# Evidence class. NOT `AUTHORITY_DIRECT_SCREENSHOT` — that class asserts a verified screenshot
# artifact, and no artifact was verified. This class says exactly what happened instead.
EVIDENCE_CLASS = "AUTHORITY_EXCHANGE_READ_FROM_RENDERED_IMAGE_WITHOUT_BINARY_CUSTODY"
BLOCKED_EVIDENCE_CLASS = "AUTHORITY_DIRECT_SCREENSHOT"

# ID COLLISION, DECLARED RATHER THAN SILENTLY RESOLVED
# ----------------------------------------------------
# The stage brief re-scopes T04-CNF-01/02/03 onto three different subjects from the ones
# Stage 4.2F-B0.9 committed under those same IDs. That re-scoping is the intended end state,
# but it is conditional on the custody upgrade, which failed. Renumbering live governance
# records under a blocked premise would be worse than the collision, so nothing is renumbered:
# each reading below carries BOTH the proposed ID and the B0.9 ID it corresponds to.
CONFIRMATION_ID_MAPPING = dict(
    status="PROPOSED_NOT_APPLIED",
    applied=False,
    blocked_by="B091-BLOCK-01",
    rows=[
        dict(proposed_id="T04-CNF-01", proposed_subject="pembajaan → racun correction",
             b09_id="T04-CNF-01", b09_subject="acceptance of both screenshot items",
             relationship="NARROWED — the B0.9 record is the bundled acceptance itself; the "
                          "proposed record is one of the two propositions it accepted"),
        dict(proposed_id="T04-CNF-02", proposed_subject="S14 reuses AG-06; scope stays 41",
             b09_id="T04-CNF-01", b09_subject="acceptance of both screenshot items",
             relationship="NARROWED — the second of the two propositions"),
        dict(proposed_id="T04-CNF-03", proposed_subject="Q5 item type",
             b09_id="T04-CNF-02", b09_subject="Q5 multiple response",
             relationship="SAME SUBJECT, DIFFERENT ID — a straight renumbering"),
        dict(proposed_id=None, proposed_subject=None,
             b09_id="T04-CNF-03", b09_subject='the "Q3 tu nnt u pilih ya" line',
             relationship="RETIRED AS AN AUTHORITY RECORD — the line is Firdaus's, not "
                          "Bariah's (T04-COR-02). It has no place in a confirmation register "
                          "at all once authorship is corrected."),
    ])

CONFIRMATION_READINGS = [
    dict(
        confirmation_id="T04-CNF-01",
        subject="The pembajaan → racun wording correction on the inserted screen T04-S14",
        proposition_put_by="FIRDAUS",
        proposition_msg="WA-01 item 1",
        proposition_verbatim=("Dalam nota tertulis \"Tiga aspek pengurusan pembajaan untuk "
                              "kontraktor\". Kami faham perkataan yang dimaksudkan ialah "
                              "racun. Betul?"),
        authority_response_msg="WA-02, scope clarified by WA-05",
        authority_response_verbatim="Yes to both  ·  Yes to both screenshots.",
        confirmation_mode="BUNDLED_ACCEPTANCE_OF_TWO_PROPOSITIONS",
        original_wording="Tiga aspek pengurusan pembajaan untuk kontraktor",
        controlled_correction="Tiga aspek pengurusan racun untuk kontraktor",
        would_be_status_if_custody_passed="CONFIRMED_THROUGH_BUNDLED_SCREENSHOT_ACCEPTANCE",
        actual_status="CONTENT_CONFIRMED_CUSTODY_MAPPING_INCOMPLETE",
        evidence_class=EVIDENCE_CLASS,
        mapping_basis=("Firdaus's proposition in WA-01 item 1 plus Bariah's bundled "
                       "acceptance in WA-02, whose scope she confirmed in WA-05."),
        not_claimed=(
            "Bariah did not write the corrected sentence. She answered a yes/no question that "
            "Firdaus phrased. The corrected wording is a CAIR-authored sentence the authority "
            "assented to, and it is not recorded as a standalone Bariah-originated sentence."),
        upgrade_blocked_by="CUSTODY_FAILED_NO_BINARY",
        unseen_screenshot_limit=(
            "A visible message reading 'Yes to both screenshots' is not proof of what those "
            "screenshots contained. The referenced images are not themselves rendered in the "
            "capture; what is rendered is Firdaus's own quoted request. The mapping from her "
            "'yes' to this specific proposition is an inference from message order, and it is "
            "labelled as one.")),
    dict(
        confirmation_id="T04-CNF-02",
        subject="T04-S14 reuses three AG-06 assets; no new unique asset; scope stays 41",
        proposition_put_by="FIRDAUS",
        proposition_msg="WA-01 item 2",
        proposition_verbatim=("Kami cadangkan skrin baharu itu menggunakan semula tiga aset "
                              "AG-06 sebagai skrin overview, tanpa aset unik baharu. Dengan "
                              "itu jumlah kekal 41 aset. Mohon sahkan."),
        authority_response_msg="WA-02, scope clarified by WA-05",
        authority_response_verbatim="Yes to both  ·  Yes to both screenshots.",
        confirmation_mode="CAIR_PROPOSAL_CONFIRMED_BY_AUTHORITY",
        production_consequence="new unique assets = 0",
        final_unique_asset_scope=41,
        would_be_status_if_custody_passed="CONFIRMED_BARIAH_ON_CAIR_PROPOSAL",
        actual_status="CONTENT_CONFIRMED_CUSTODY_MAPPING_INCOMPLETE",
        evidence_class=EVIDENCE_CLASS,
        origin="CAIR production proposal confirmed by the authority.",
        not_claimed=(
            "41 is not an idea Bariah originated, and the AG-06 reuse is not a "
            "Bariah-authored design. Both are CAIR production proposals she assented to."),
        unseen_screenshot_limit=(
            "As for CNF-01: the acceptance is visible, the accepted screenshots are not."),
        mutability=(
            "41 is not immutable. If MMD production later demonstrates a genuine new asset "
            "requirement, the change to 42 must be recorded as a new scope-change decision "
            "with its own authority, never absorbed silently into the existing total."),
        upgrade_blocked_by="CUSTODY_FAILED_NO_BINARY"),
    dict(
        confirmation_id="T04-CNF-03",
        subject="Q5 item type",
        proposition_put_by="FIRDAUS",
        proposition_msg="WA-01 item 3",
        proposition_verbatim=("3. Cadangan akhir Q5 — Multiple Response … Mohon sahkan sama "
                              "ada Q5 ini boleh digunakan atau perlu dipinda lagi."),
        authority_response_msg="WA-05",
        authority_response_verbatim="Q5 multiple response - yes, ok",
        confirmation_mode="EXPLICITLY_WORDED_INDIVIDUAL_DECISION",
        confirms="Q5 item type = MULTIPLE_RESPONSE",
        would_be_status_if_custody_passed="EXPLICITLY_CONFIRMED",
        actual_status="CONTENT_CONFIRMED_CUSTODY_UNVERIFIED",
        why_this_one_is_stronger=(
            "Unlike CNF-01 and CNF-02 this does not depend on mapping a bundled 'yes' onto an "
            "unseen proposition. The words 'Q5 multiple response' name their own subject."),
        evidence_class=EVIDENCE_CLASS,
        does_not_confirm=[
            "all five answer keys",
            "the exact two replacement distractors",
            "every source-row binding",
            "a general delegation to approve assessment content",
        ],
        not_claimed=(
            "This is a confirmation of item type. It is not a blanket approval of the "
            "assessment, and the answer keys stay PROPOSED_NOT_FINAL."),
        upgrade_blocked_by="CUSTODY_FAILED_NO_BINARY"),
]

# ==========================================================================================
# PART A.4 — A DIVERGENCE THE SCREENSHOT EXPOSES
# ==========================================================================================
# Firdaus put a six-option Q5 to Bariah. It is not the Q5 that Stage 4.2F-B0.9 froze. Both
# option sets are recorded; neither is quietly swapped for the other.
Q5_DIVERGENCE = dict(
    finding_id="T04-DIV-01",
    severity="MATERIAL_UNRESOLVED_DIVERGENCE",
    subject="The Q5 put to Bariah is not the Q5 in the frozen content model",
    stem_put_to_authority=("Pilih SEMUA pernyataan yang tepat tentang kawalan semasa "
                           "aktiviti semburan racun."),
    stem_in_frozen_model=("Pilih SEMUA kawalan yang mesti dipatuhi oleh kontraktor semasa "
                          "aktiviti semburan racun."),
    stem_source_of_frozen_model="AUTH-EV-01 §E — Bariah's own written replacement stem",
    options_put_to_authority=[
        "Pengendali semburan mesti berlesen atau telah menerima latihan",
        "Pekerja mesti memakai PPE yang lengkap dan bersesuaian",
        "Semburan hanya dilakukan semasa cuaca tenang",
        "Salinan Helaian Data Keselamatan (SDS) disimpan di tapak",
        "Notifikasi kepada penduduk dibuat hanya selepas semburan selesai",
        "SDS hanya perlu disimpan di pejabat projek dan tidak perlu berada di tapak",
    ],
    options_in_frozen_model=[
        "Pengendali semburan mesti berlesen atau telah menerima latihan",
        "Pekerja mesti memakai PPE yang lengkap dan bersesuaian",
        "Semburan hanya dilakukan semasa cuaca tenang",
        "Salinan Helaian Data Keselamatan (SDS) disimpan di tapak",
        "Semburan dijadualkan pada waktu petang selepas waktu kerja tapak tamat",
        "Semua racun dibeli daripada satu pembekal tunggal yang dilantik projek",
    ],
    agreeing_positions=[1, 2, 3, 4],
    diverging_positions=[5, 6],
    proposed_key_agrees=True,
    proposed_key="the first four options, in both versions",
    what_this_means=(
        "Positions 1 to 4 are identical in both versions and are not in question. Positions 5 "
        "and 6 are not: Firdaus put two distractors to Bariah that differ from the two Stage "
        "4.2F-B0.9 froze. Bariah's 'Q5 multiple response - yes, ok' was written against "
        "Firdaus's set, not against the frozen set."),
    why_it_is_not_resolved_here=(
        "Resolving it would mean either overwriting Bariah's frozen stem with Firdaus's "
        "wording, or asserting that her 'yes, ok' reaches option text she was never shown. "
        "Both are decisions for the authority, not for CAIR, and neither is taken."),
    # CLOSED in the Stage 4.2F-B0.9.1 re-run. Neither of the two divergent sets survived: the
    # forced choice offered a THIRD pair (Set B) against a fixed stem, and Bariah picked it.
    status="CLOSED",
    closed_by="E-07 forced choice — WA-06 / WA-07",
    closing_record="T04-DEC-E09",
    resolution=("Set B, verbatim. Neither the Stage 4.2F-B0.9 CAIR draft nor the earlier "
                "WhatsApp pair is in force; the selected pair supersedes both."),
    frozen_model_unchanged=False,
    frozen_model_now_carries="SET_B",
    resolution_required_from=None,
    tracked_as="E-07",
    blocking_storyboard_layout=False,
    blocking_scored_quiz=False)

# ==========================================================================================
# PART A.4b — E-07 CLOSURE
# ==========================================================================================
# The forced choice is the cleanest authority act in this whole exchange: a closed option set,
# both alternatives written out in full, an instruction to answer with one of them, and a
# reply that names one. There is nothing to interpret.
E07_CLOSURE = dict(
    open_id="E-07",
    status="CLOSED",
    decision_type="DIRECT_SELECTION_FROM_EXPLICIT_OPTIONS",
    authority="BARIAH_DIRECT_SELECTION",
    selected_set="SET_B",
    rejected_set="SET_A",
    rejected_set_status="REJECTED_NOT_SELECTED",
    request_msg="WA-06",
    response_msg="WA-07",
    authority_quote="Set B. Better distractors",
    request_quote="Boleh jawab Set A atau Set B sahaja.",
    sets_were_mutually_exclusive=True,
    sets_combined=False,
    both_sets_retained_active=False,
    # Custody is still unverified. That weakens the ARTIFACT, not the CLARITY of the choice.
    evidence_class=EVIDENCE_CLASS,
    custody_status="CUSTODY_UNVERIFIED_NO_BINARY",
    why_closure_is_still_sound=(
        "The reply selects from a set the requester enumerated in the same thread. Unlike a "
        "bundled 'yes to both', there is no scope question: 'Set B' can only mean the two "
        "options written under the heading Set B. The missing binary means the artifact "
        "cannot be frozen and re-verified later; it does not make the sentence ambiguous."),
    what_this_does_not_approve=[
        "the five quiz answer keys — the request said the four correct answers were unchanged "
        "and asked only about the two incorrect options",
        "any other quiz item",
        "the source-row bindings",
        "a general delegation to CAIR over assessment content",
    ],
    supersedes_finding="T04-DIV-01")

# The exact wording Bariah selected. Copied from the enumerated Set B in WA-06, character for
# character. Stage 4.2F-B0.9 had frozen two DIFFERENT sentences under the same intent, and the
# difference is not cosmetic — one of them named a reason ("selepas waktu kerja tapak tamat")
# that Set B does not.
SET_B_FROZEN = [
    dict(position=5,
         text_ms="Semburan dijadualkan pada waktu petang tanpa mengambil kira keadaan cuaca",
         superseded_b09_text=("Semburan dijadualkan pada waktu petang selepas waktu kerja "
                              "tapak tamat"),
         wording_source="WA-06 Set B, first option",
         paraphrased=False),
    dict(position=6,
         text_ms="Semua racun dibeli daripada satu pembekal tunggal",
         superseded_b09_text=("Semua racun dibeli daripada satu pembekal tunggal yang "
                              "dilantik projek"),
         wording_source="WA-06 Set B, second option",
         paraphrased=False),
]

SET_A_REJECTED = [
    dict(position=5,
         text_ms="Notifikasi kepada penduduk dibuat hanya selepas semburan selesai",
         status="REJECTED_NOT_SELECTED"),
    dict(position=6,
         text_ms="SDS hanya perlu disimpan di pejabat projek dan tidak perlu berada di tapak",
         status="REJECTED_NOT_SELECTED"),
]

# The stem changed provenance, and that has to be visible rather than absorbed.
STEM_PROVENANCE_CHANGE = dict(
    correction_id="T04-COR-04",
    subject="The Q5 stem now in force is not the one Bariah wrote in the authority DOCX",
    b09_stem=("Pilih SEMUA kawalan yang mesti dipatuhi oleh kontraktor semasa aktiviti "
              "semburan racun."),
    b09_stem_provenance="AUTHORITY_SUPPLIED_REPLACEMENT_TEXT — Bariah wrote it in AUTH-EV-01 "
                        "§E",
    final_stem=("Pilih SEMUA pernyataan yang tepat tentang kawalan semasa aktiviti semburan "
                "racun."),
    final_stem_provenance="FIRDAUS_DIRECTED_PRESENTED_AS_FIXED_NOT_CONTESTED_BY_AUTHORITY",
    how_it_was_presented=("WA-06 shows it under the heading 'Stem kekal' — the stem stands. "
                          "It was put to Bariah as a fixed premise of the forced choice, not "
                          "as something to decide."),
    what_bariah_actually_answered="the two incorrect options, not the stem",
    therefore=(
        "The stem in force is a Firdaus-directed wording that the authority saw and did not "
        "contest. That is weaker than the DOCX stem it replaces, which she wrote herself. It "
        "is recorded at the weaker grade rather than inheriting the stronger one."),
    status="APPLIED_PROVENANCE_DOWNGRADED",
    reversible=True,
    confirmation_would_close="a one-line confirmation from Bariah that the stem wording is "
                             "hers to keep")


# ==========================================================================================
# PART A.5 — AG-01 … AG-08 REGISTER AUDIT
# ==========================================================================================
AG_SET_STATUS = "ACCEPTED_AS_A_SET_WITH_CONDITIONS"
AG_AUTHORITY_BASIS = "BARIAH_DIRECT_SET_LEVEL_NARRATIVE"
AG_INDIVIDUAL_CARD_STATUS = "NOT_INDIVIDUALLY_MARKED"

AG_FORBIDDEN_REPRESENTATIONS = [
    "eight direct individual acceptances",
    "eight fully unanswered decisions",
    "eight pending-human blockers",
]

AG_DISTINCTION_LAYERS = [
    dict(layer=1, name="SET_LEVEL_ACCEPTANCE",
         value=AG_SET_STATUS,
         basis=AG_AUTHORITY_BASIS,
         quote=("cadangan perkongsian bersyarat (AG-01–AG-08) munasabah untuk pengoptimuman "
                "produksi"),
         source="AUTH-EV-01 §B KOMEN KESELURUHAN"),
    dict(layer=2, name="INDIVIDUAL_CARD_MARKINGS",
         value=AG_INDIVIDUAL_CARD_STATUS,
         basis="OBSERVED_IN_THE_AUTHORITY_DOCX",
         quote=None,
         source=("AUTH-EV-01 §B, the eight per-group decision cards. Every TERIMA / PINDA / "
                 "BUANG / GABUNG box and every sharing box is blank.")),
    dict(layer=3, name="ITEM_LEVEL_NO_REUSE_RESTRICTIONS",
         value="THREE_ITEMS_CLOSED",
         basis="DERIVED_FROM_BARIAH_SECTION_LEVEL_NARRATIVE",
         quote=("Saya sahkan item \"tidak boleh dikongsi\" (PPE baja, PPE racun, stok baja "
                "vs stok racun) memang memerlukan aset berasingan kerana visualnya berbeza "
                "secara ketara."),
         source="AUTH-EV-01 §B KOMEN KESELURUHAN"),
    dict(layer=4, name="S14_SPECIFIC_AG06_REUSE",
         value="CONFIRMED_ON_CAIR_PROPOSAL",
         basis=EVIDENCE_CLASS,
         quote="Yes to both screenshots.",
         source="WA-01 item 2 + WA-02 + WA-05"),
]

# The three no-reuse decisions stay closed. Their basis is section-level narrative — Bariah
# did not tick a basis field on each item, and this stage does not pretend she did.
NO_REUSE_CLOSED = [
    dict(obligation_id="T04-VO-025", label="Baja — Pengurusan Stok dan Penyimpanan",
         asset_group_id="AG-04"),
    dict(obligation_id="T04-VO-026", label="Baja — Keselamatan Pekerja",
         asset_group_id="AG-04"),
    dict(obligation_id="T04-VO-039", label="Racun — Keselamatan dan Kesihatan (HSE)",
         asset_group_id="AG-06"),
]
NO_REUSE_DECISION_BASIS = "BOTH_INSTRUCTIONAL_AND_PRODUCTION"
NO_REUSE_EVIDENCE_PRECISION = "DERIVED_FROM_BARIAH_SECTION_LEVEL_NARRATIVE"
NO_REUSE_NOT_CLAIMED = ("Bariah did not individually tick a decision-basis field for each of "
                        "the three items. She stated both grounds once, at section level, "
                        "covering all three. The basis is derived from that statement and is "
                        "labelled as derived.")

SECTION_LEVEL_NARRATIVE_CONTENTS = [
    "AG-01 to AG-08 conditional sharing is reasonable for production optimisation.",
    "The distinct PPE and storage requirements genuinely need separate assets.",
    "The 46 → 41 calculation is accepted as production scope.",
    "Instructional clarity overrides production optimisation where the two conflict.",
]


def ag_register_audit():
    """Read the committed register live and report what it actually says per group."""
    rows = []
    for g in A.asset_group_scope():
        rows.append(dict(
            asset_group_id=g["asset_group_id"],
            label=g["label"],
            set_level_status=AG_SET_STATUS,
            authority_basis=AG_AUTHORITY_BASIS,
            individual_card_status=AG_INDIVIDUAL_CARD_STATUS,
            reuse_decision_in_register=g["reuse_decision"],
            item_level_restrictions=list(g["item_level_restrictions"]),
            restriction_applies_to_whole_group=g["restriction_applies_to_whole_group"],
            represented_as_individual_acceptance=False,
            represented_as_unanswered=False,
            represented_as_pending_human_blocker=False))
    return rows


# ==========================================================================================
# PART A.6 — RELEASE STATUS
# ==========================================================================================
PART_A_RESULT = "PARTIAL_CUSTODY_BLOCKED_CONTENT_CLOSED"
PART_A_BLOCKER = dict(
    blocker_id="B091-BLOCK-01",
    still_open=True,
    scope_after_the_rerun=("Narrowed. It no longer blocks content decisions — the E-07 "
                           "selection is unambiguous on its face. What it still blocks is "
                           "canonical evidence closure: no artifact can be frozen, hashed or "
                           "re-verified later."),
    subject="Supplementary screenshot custody",
    required="A PNG binary to hash, measure, validate and freeze.",
    observed="No image file exists in this environment.",
    consequence=(
        "The evidence class cannot be upgraded to AUTHORITY_DIRECT_SCREENSHOT, the "
        "NOT_SUPPLIED custody state cannot be cleared, and no superseding release record is "
        "issued. Stage 4.2F-B1 does not start."),
    what_would_unblock=(
        "Re-send the screenshot as a file attachment so it lands in the uploads directory. "
        "Everything else in this stage is already done and will not need repeating."),
    owner="FIRDAUS")

# The release record that would be issued if custody passed. Held as a template, explicitly
# NOT issued, so the difference between "ready to state" and "stated" stays visible.
# ==========================================================================================
# RELEASE DECISION
# ==========================================================================================
# The brief's own decision tree has two branches. The first requires the CNF-01/CNF-02
# propositions to be verified FROM A SUPPLIED BINARY. There is no binary, so that branch is
# unavailable regardless of what the pixels show. The second branch is the one that fits.
RELEASE_DECISION = dict(
    verdict_tokens=[
        "T04_ASSESSMENT_DIVERGENCE_CLOSED",
        "STORYBOARD_LAYOUT_READY",
        "SUPPLEMENTARY_CNF_MAPPING_PARTIALLY_OPEN",
    ],
    issued=True,
    branch_taken="E07_CLOSED_CNF_BINARY_MAPPING_INCOMPLETE",
    branch_not_taken="T04_CONTENT_APPROVED_READY_FOR_STORYBOARD_BUILD",
    why_branch_not_taken=(
        "That branch requires the CNF-01 and CNF-02 propositions to be verified from a "
        "supplied binary. No binary was supplied, so the condition is not met — not because "
        "the propositions are doubtful, but because the verification route does not exist."),
    what_the_open_mapping_blocks="CANONICAL_EVIDENCE_CLOSURE_ONLY",
    blocks_storyboard_layout=False,
    why_layout_is_not_blocked=(
        "Nothing the storyboard lays out depends on CNF-01 or CNF-02 being image-verified. "
        "The pembajaan → racun correction is already recorded as T04-COR-01, applied and "
        "pending confirmation, and the screen it affects is bound to T04-ROW-064 in the "
        "controlled extract. The S14 AG-06 reuse and the 41-asset total are CAIR production "
        "proposals held as proposals, and no asset is produced in B1. Both would have to be "
        "re-opened only if Bariah reversed them, which nothing suggests."),
    supersedes="STAGE_4_2F_B0_9_RUN_MANIFEST.md §16",
    prior_release_record_status="SUPERSEDED_BY_THIS_RECORD")

RELEASE_RECORD_NOT_ISSUED = dict(
    would_be_verdict="T04_CONTENT_APPROVED_READY_FOR_STORYBOARD_BUILD",
    issued=False,
    why_not_issued="Custody failed for a second time. See B091-BLOCK-01.",
    superseding=False,
    prior_release_record_stands="STAGE_4_2F_B0_9_RUN_MANIFEST.md §16")

PPTX_GENERATED = 0
GENERATOR_TOUCHED = 0
MMD_PRODUCTION_STARTED = 0
REACT_OR_SCORM_STARTED = 0
LMS_WORK_STARTED = 0
AUTHORITY_ARTIFACTS_MODIFIED = 0
PART_B_STARTED = 0

NEW_OPEN_ITEMS = [
    dict(open_id="E-08", subject="Supplementary screenshot binary custody",
         owner="FIRDAUS", raised_by="B091-BLOCK-01",
         status="OPEN_SECOND_ATTEMPT_FAILED"),
]

CLOSED_IN_THE_RERUN = [
    dict(open_id="E-07", subject="Which Q5 option pair stands",
         closed_by="Bariah selected Set B from an enumerated forced choice",
         closing_record="T04-DEC-E09"),
    dict(open_id="E-01", subject="Q5 replacement options E and F",
         closed_by="the same selection — the CAIR draft is superseded",
         closing_record="T04-DEC-E09"),
    dict(open_id="E-03", subject="The 'Q3' referent",
         closed_by="T04-COR-02 — the line is Firdaus's, so no authority referent exists",
         closing_record="T04-COR-02"),
]

NEW_ARTIFACTS = [
    "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.json",
    "T04_SUPPLEMENTARY_EVIDENCE_CUSTODY_v1.md",
    "T04_AUTHORITY_EXCHANGE_READING_v1.json",
    "T04_AUTHORITY_EXCHANGE_READING_v1.md",
    "T04_AG_REGISTER_AUDIT_v1.json",
    "T04_AG_REGISTER_AUDIT_v1.md",
    "T04_PREDICATE_AND_XML_AUDIT_v1.json",
    "T04_PREDICATE_AND_XML_AUDIT_v1.md",
]
