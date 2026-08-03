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
MESSAGES = [
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
    dict(msg_id="WA-05", position=5, time_shown="7:21 AM",
         sender="BARIAH", direction="INCOMING",
         bubble="white, left-aligned, quoting her own 'Yes to both'",
         summary=("Bariah confirms the scope of her earlier acceptance and separately answers "
                  "the third question."),
         verbatim_fragments=["Yes to both screenshots. Q5 multiple response - yes, ok"]),
]

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
        actual_status="CONTENT_CONFIRMED_CUSTODY_UNVERIFIED",
        evidence_class=EVIDENCE_CLASS,
        mapping_basis=("Firdaus's proposition in WA-01 item 1 plus Bariah's bundled "
                       "acceptance in WA-02, whose scope she confirmed in WA-05."),
        not_claimed=(
            "Bariah did not write the corrected sentence. She answered a yes/no question that "
            "Firdaus phrased. The corrected wording is a CAIR-authored sentence the authority "
            "assented to, and it is not recorded as a standalone Bariah-originated sentence."),
        upgrade_blocked_by="CUSTODY_FAILED_NO_BINARY"),
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
        actual_status="CONTENT_CONFIRMED_CUSTODY_UNVERIFIED",
        evidence_class=EVIDENCE_CLASS,
        origin="CAIR production proposal confirmed by the authority.",
        not_claimed=(
            "41 is not an idea Bariah originated, and the AG-06 reuse is not a "
            "Bariah-authored design. Both are CAIR production proposals she assented to."),
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
    frozen_model_unchanged=True,
    resolution_required_from="Bariah — one line stating which six-option set stands.",
    tracked_as="E-07",
    blocking_storyboard_layout=False,
    blocking_scored_quiz=True)

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
PART_A_RESULT = "BLOCKED"
PART_A_BLOCKER = dict(
    blocker_id="B091-BLOCK-01",
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
RELEASE_RECORD_NOT_ISSUED = dict(
    would_be_verdict="T04_CONTENT_APPROVED_READY_FOR_STORYBOARD_BUILD",
    issued=False,
    why_not_issued="Custody failed. See B091-BLOCK-01.",
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
    dict(open_id="E-07", subject="Which Q5 six-option set stands — the one put to Bariah in "
                                 "WhatsApp, or the one frozen in the content model",
         owner="BARIAH", raised_by="T04-DIV-01"),
    dict(open_id="E-08", subject="Supplementary screenshot binary custody",
         owner="FIRDAUS", raised_by="B091-BLOCK-01"),
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
