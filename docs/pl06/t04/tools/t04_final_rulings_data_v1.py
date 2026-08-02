# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.7 — the ONE controlled data source for Bariah's FINAL structural rulings.

This stage closes the five structural decisions D-01 … D-05. What remains after it is
CONTENT review, not structure.

APPROVAL VOCABULARY, corrected in this stage
--------------------------------------------
Stage 4.2F-B0.6 reported a single ambiguous `APPROVED_ITEMS = 0`. That was true of final
instructional content and false of policy: Bariah had already confirmed the visual ruling and
the quiz composition. Reporting one number for two different things understated her decisions.
This stage replaces it with four typed totals:

    CONFIRMED_POLICY_DECISIONS               structure Bariah has settled
    CONDITIONALLY_CONFIRMED_DECISIONS        settled, subject to a stated condition
    APPROVED_FINAL_INSTRUCTIONAL_CONTENT_ITEMS   learner-facing text she has approved
    PENDING_BARIAH_CONTENT_REVIEWS           content still waiting on her

OBLIGATIONS ARE NOT ASSETS
--------------------------
46 visual obligations is a count of PLACES a visual is required. It is not a count of images
to produce — one composite may serve several obligations, and one obligation may need more
than one state. `UNIQUE_ASSET_COUNT` stays `NOT_YET_DETERMINED` until the grouping is decided.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_data_v1 as SRC
import t04_rulings_data_v1 as B06

STAGE = "4.2F-B0.7"
UNIT_ID = "K5-PL06-T04-B01"
LESSON_TITLE = "Penjagaan dan Penyelenggaraan"
GENERATED_BY = "docs/pl06/t04/tools/t04_final_rulings_emit_v1.py"

CONTENT_STATUS = "CAIR_ASSISTED_DRAFT"
APPROVAL_STATUS = "PENDING_BARIAH_REVIEW"
INSTRUCTIONAL_AUTHORITY = "BARIAH"
FINAL_SCREEN_COUNT = "NOT_CLAIMED"
EVIDENCE_DIR = B06.EVIDENCE_DIR

# ==========================================================================================
# PART 1 — NEW EVIDENCE
# ==========================================================================================
# DISCREPANCY, recorded rather than smoothed over. The stage instruction says three
# screenshots are attached. Exactly ONE image arrived on the instruction message; I checked
# the message payload, the session upload area and the transcript. That one image carries all
# three confirmations the instruction describes, so nothing is missing in substance — but it
# is one evidence item, not three, and it is registered as one.
EVIDENCE_DELIVERY = dict(
    expected_by_instruction=3,
    actually_received=1,
    status="ONE_IMAGE_CARRIES_ALL_THREE_CONFIRMATIONS",
    checked=["the instruction message image blocks",
             "/root/.claude/uploads/<session>/ — no new files since the Stage 4.2F-A2 ZIP",
             "the session transcript"],
    consequence="No ruling is missing. The three confirmations the instruction lists are all "
                "legible in T04-EV-03. Only the evidence-item count differs.")

EVIDENCE_NEW = [
    dict(evidence_id="T04-EV-03",
         frozen_filename="T04_BARIAH_FINAL_STRUCTURAL_CONFIRMATIONS_20260802.webp",
         frozen_path=EVIDENCE_DIR + "/T04_BARIAH_FINAL_STRUCTURAL_CONFIRMATIONS_20260802.webp",
         original_uploaded_filename="NOT_RECOVERABLE_FROM_SESSION_TRANSPORT",
         byte_size=138074,
         sha256="9cf3842e70b24d304bb32e5e3947ece0db2b3bbc826727a3915be80ab068c353",
         media_type="image/webp", dimensions_px="1194 x 1520", colour_mode="RGB",
         evidence_date="2026-08-02",
         received_utc="2026-08-02T09:22:55Z",
         reviewer="BARIAH",
         evidence_class="BARIAH_DIRECT_SCREENSHOT",
         scope=UNIT_ID,
         modification="NONE — byte-identical",
         description="WhatsApp conversation 'Bariah eLearning', 4:56 PM to 4:59 PM. Carries "
                     "four separate confirmations: the legal base/reveal split, the 60 "
                     "percent pass mark for all PLs, an additional character in a dialogue "
                     "scenario on Slide 2, and the six-step diagram treatment — plus the "
                     "condition on reusing Alya and Encik Rahman.",
         ruling_locators=["BR-C1", "BR-C2", "BR-C3", "BR-C4", "BR-C5"]),
]

EVIDENCE_ALL = list(B06.EVIDENCE) + EVIDENCE_NEW

RULING_LOCATORS_NEW = [
    dict(locator="BR-C1", evidence_id="T04-EV-03", position="WhatsApp, 4:56 PM",
         verbatim="yes ok, confirmed",
         replying_to="…rator berlesen dan PPE dipaparkan terus pada skrin; …S, penyimpanan, "
                     "penyemburan, notifikasi dan laporan boleh guna cli… …n cadangan ini.",
         reading="D-04 confirmed. The base screen carries the statute, the licensed-operator "
                 "requirement and PPE; SDS, storage, spraying conditions, notification and "
                 "reporting may use click-to-reveal.",
         decision="D-04"),
    dict(locator="BR-C2", evidence_id="T04-EV-03", position="WhatsApp, 4:58 PM, line 1",
         verbatim="1. Markah lulus 60% semua PL",
         replying_to="…ah lulus 60% juga terpakai kepada semua PL?",
         reading="D-02B confirmed. 60 percent, and the scope is all PLs — not T04, not PL06.",
         decision="D-02B"),
    dict(locator="BR-C3", evidence_id="T04-EV-03", position="WhatsApp, 4:58 PM, line 2",
         verbatim="2. Guna watak tambahan di Slide 2 (perbualan dialog senario)",
         replying_to="…oleh guna Hilmi sebagai narrator sahaja, tanpa wata…",
         reading="D-03 answered, and answered AGAINST the narrator-only option that was put "
                 "to her. Slide 2 takes an additional character in a dialogue scenario.",
         decision="D-03"),
    dict(locator="BR-C4", evidence_id="T04-EV-03", position="WhatsApp, 4:58 PM",
         verbatim="yes ok, confirmed",
         replying_to="…guna diagram enam langkah d… …ohon confirm juga.",
         reading="D-05 confirmed — the six-step source diagram is used, redrawn later, order "
                 "unchanged.",
         decision="D-05"),
    dict(locator="BR-C5", evidence_id="T04-EV-03", position="WhatsApp, 4:59 PM",
         verbatim="jika Alya & Encik Rahman, sesuai, boleh guna semula. Jika tidak, guna "
                  "watak baru",
         replying_to="1. Markah lulus 60% semua PL / 2. Guna watak tambahan di Slide 2 "
                     "(perbualan dialog senario)",
         reading="The cast is confirmed WITH A CONDITION. Reuse the existing pair if they "
                 "suit; create a new character if they do not. Judging the fit is the work, "
                 "and it cannot be skipped by simply naming them.",
         decision="D-03"),
]

RULING_LOCATORS_ALL = list(B06.RULING_LOCATORS) + RULING_LOCATORS_NEW

# One element of the D-04 base list is NOT legible in the screenshot, and is recorded as
# inference rather than as something Bariah is on record as writing.
EVIDENCE_LEGIBILITY = [
    dict(item="The word 'Akta' in the D-04 base-screen list",
         legible_in_screenshot=False,
         what_is_legible="The quoted proposal is cropped at the left margin. The line reads "
                         "'…rator berlesen dan PPE dipaparkan terus pada skrin' — the item "
                         "before 'operator berlesen' is cut off.",
         authority="INFERRED_FROM_CROPPED_LINE_PLUS_FIRDAUS_STAGE_INSTRUCTION",
         basis="The Stage 4.2F-B0.7 instruction states the base screen must show Akta Racun "
               "Makhluk Perosak 1974, the licensed operator requirement and PPE. The cropped "
               "line is consistent with that and 'rator' is the tail of 'operator'. Bariah's "
               "'yes ok, confirmed' applies to the whole proposal she was sent.",
         note="Recorded here so that the statute's place on the base screen is traceable to "
              "an inference plus a stage instruction, not misattributed to a legible "
              "screenshot line."),
]

# ==========================================================================================
# PART 2-5 — FINAL DECISION STATE
# ==========================================================================================
DECISION_STATUSES = ["CONFIRMED_BARIAH_DIRECT", "CONFIRMED_WITH_EXPANSION",
                     "CONFIRMED_WITH_CONDITION", "DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW",
                     "PARTIALLY_RESOLVED", "CLARIFICATION_REQUIRED", "UNRESOLVED"]

DECISIONS = [
    dict(decision_id="D-01", title="Visual treatment",
         status="CONFIRMED_WITH_EXPANSION",
         ruling="VISUAL_REQUIRED_FOR_BARIAH_NAMED_POPULATION",
         evidence=["BR-L1", "BR-L2", "BR-L3", "BR-L4", "BR-L5", "BR-L6"],
         changed_this_stage=False,
         scope="THIS_UNIT_ONLY",
         structural_status="RESOLVED",
         open_content_points=["visual subject and style approval for all 46 obligations"]),
    dict(decision_id="D-02A", title="Quiz composition",
         status="CONFIRMED_BARIAH_DIRECT",
         ruling="4 MCQ + 1 MULTIPLE_RESPONSE",
         evidence=["BR-W2"],
         changed_this_stage=False,
         scope="ALL_PLS_IN_KURSUS",
         structural_status="RESOLVED",
         open_content_points=["what each slot tests; the questions themselves"]),
    dict(decision_id="D-02B", title="Passing threshold",
         status="CONFIRMED_BARIAH_DIRECT",
         ruling="60_PERCENT",
         evidence=["BR-C2"],
         changed_this_stage=True,
         previous_status="UNRESOLVED",
         change_note="Stage 4.2F-B0.6 held this open and refused to carry 60 percent forward "
                     "as a default. Bariah has now confirmed it directly, and confirmed the "
                     "scope is all PLs in the Kursus. The A3 figure and her ruling agree, but "
                     "it is her ruling that authorises it.",
         scope="ALL_PLS_IN_KURSUS",
         structural_status="RESOLVED",
         open_content_points=[]),
    dict(decision_id="D-02C", title="Rumusan",
         status="DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW",
         ruling="FOLLOW_WRITING_STYLE_TOPIK_3_BAHAGIAN_2",
         evidence=["BR-W1", "BR-W3"],
         changed_this_stage=False,
         scope="THIS_UNIT_ONLY",
         structural_status="RESOLVED",
         open_content_points=["review, edit or approve the four drafted statements"]),
    dict(decision_id="D-03", title="T04 cast and Slide 2 treatment",
         status="CONFIRMED_WITH_CONDITION",
         ruling="SLIDE_2_DIALOGUE_SCENARIO_WITH_ADDITIONAL_CHARACTER",
         evidence=["BR-C3", "BR-C5"],
         changed_this_stage=True,
         previous_status="UNRESOLVED",
         change_note="Bariah was asked whether Hilmi alone, as narrator with no characters, "
                     "would do. She answered against that: an additional character in a "
                     "dialogue scenario on Slide 2. Reuse of Alya and Encik Rahman is "
                     "permitted ONLY if they suit; otherwise a new character. The condition "
                     "is the ruling — naming them without assessing fit would ignore half of "
                     "what she wrote.",
         scope="THIS_UNIT_ONLY",
         structural_status="CONDITIONALLY_RESOLVED",
         open_content_points=["character instance mapping", "Slide 2 dialogue review"]),
    dict(decision_id="D-04", title="Legislative content base/reveal split",
         status="CONFIRMED_BARIAH_DIRECT",
         ruling="BASE_STATUTE_OPERATOR_PPE__REVEAL_ELIGIBLE_SDS_STORAGE_SPRAY_NOTIFY_REPORT",
         evidence=["BR-C1"],
         changed_this_stage=True,
         previous_status="CLARIFICATION_REQUIRED",
         change_note="Confirmed, and BROADER than the proposal CAIR recommended. Stage "
                     "4.2F-B0.6 marked only three rows as reveal candidates and held spraying "
                     "conditions, notification and reporting as base-visible obligations. "
                     "Bariah's confirmed split makes those three reveal-eligible too. Her "
                     "ruling is implemented as written; the delta is recorded so the change "
                     "is visible rather than absorbed.",
         scope=UNIT_ID,
         structural_status="RESOLVED",
         open_content_points=[]),
    dict(decision_id="D-05", title="SmartArt production treatment",
         status="CONFIRMED_BARIAH_DIRECT",
         ruling="SOURCE_BOUND_IN_REVIEW__CONTROLLED_REDRAW_IN_MMD__SIX_NODE_ORDER_INVARIANT",
         evidence=["BR-L1", "BR-C4"],
         changed_this_stage=True,
         previous_status="PARTIALLY_RESOLVED",
         change_note="All three outstanding confirmations are given. D-05 is removed from "
                     "every unresolved list.",
         scope="THIS_UNIT_ONLY",
         structural_status="RESOLVED",
         open_content_points=[]),
]

D02B = dict(decision_id="D-02B", status="CONFIRMED_BARIAH_DIRECT",
            pass_threshold="60_PERCENT", scope="ALL_PLS_IN_KURSUS", evidence="BR-C2")

D05 = dict(decision_id="D-05", status="CONFIRMED_BARIAH_DIRECT",
           review_storyboard="USE_SOURCE_BOUND_SIX_STEP_DIAGRAM",
           future_mmd="CONTROLLED_REDRAW",
           invariant="PRESERVE_SIX_NODE_IDENTITY_AND_ORDER",
           mmd_production_status="NOT_STARTED",
           six_nodes_in_order=list(SRC.ASSETS[0]["source_subject_nodes"]),
           asset_id=SRC.ASSETS[0]["asset_id"],
           asset_sha256=SRC.ASSETS[0]["sha256"],
           hierarchy="NONE — flat; a redraw must not introduce a tree, cycle or grouping",
           evidence=["BR-L1", "BR-C4"])

# ------------------------------------------------------------------------------------------
# D-03 — cast policy and contextual fit
# ------------------------------------------------------------------------------------------
D03_POLICY = dict(
    decision_id="D-03",
    slide="SLIDE_2",
    treatment="DIALOGUE_SCENARIO_WITH_ADDITIONAL_CHARACTER",
    policy_status="CONFIRMED_WITH_CONDITION",
    preferred_existing_cast=["ALYA", "ENCIK_RAHMAN"],
    reuse_condition="USE_IF_CONTEXTUALLY_APPROPRIATE",
    fallback="CREATE_NEW_CHARACTER_IF_EXISTING_PAIR_IS_NOT_CONTEXTUALLY_APPROPRIATE",
    character_instance_mapping="NOT_COMPLETE",
    evidence=["BR-C3", "BR-C5"],
    prior_b02_policy=dict(
        source="reviews/source-completion/generator/audit/b02_decision_oracle_v0_4_4.py — D3",
        verbatim="Yes lulus. Boleh diguna pakai di Bahagian/Topik/PL lain jika bersesuaian",
        reuse_policy="APPROVED_WHERE_CONTEXTUALLY_APPROPRIATE",
        consistency="BR-C5 restates the same conditional policy for T04. The two rulings "
                    "agree; neither makes the reuse automatic."),
    roles_as_established_in_b02=[("Alya", "Kontraktor Junior"),
                                 ("Encik Rahman", "Mentor / Kontraktor Senior")],
    roles_source="reviews/source-completion/generator/v0_4/b02_proof_content_v0_4.py, S02 cast")

CONTEXTUAL_FIT = dict(
    assessment_id="T04-CFA-01",
    scope=UNIT_ID,
    slide="SLIDE_2",
    dialogue_purpose="Open the unit from the site, at the moment construction ends and "
                     "maintenance begins, so the learner meets the six supervisory activities "
                     "as work someone is about to do rather than as a diagram.",
    source_row_bindings=["T04-ROW-001", "T04-ROW-002", "T04-ROW-003", "T04-ROW-004",
                         "T04-ROW-005", "T04-ROW-079", "T04-ROW-080"],
    roles_required=[
        dict(role="ENQUIRER",
             function="A practitioner who has finished the construction phase and asks what "
                      "the maintenance phase requires. Carries the learner's question.",
             source_basis="T04-ROW-002 frames the unit as the process flow that follows "
                          "landscape construction work."),
        dict(role="EXPLAINER",
             function="A senior practitioner who names the six supervisory activities and the "
                      "soft/hard split, without teaching any regulated content.",
             source_basis="T04-ROW-003 (six nodes), T04-ROW-005 and T04-ROW-080 (the two "
                          "categories)."),
    ],
    alya_fit=dict(
        character="Alya", established_role="Kontraktor Junior",
        fits=True,
        reasoning="The ENQUIRER role is the same shape she already plays in B02 S02, where "
                  "she asks what remains after planting work is done. T04 opens on exactly "
                  "that hinge — what follows construction. No new competence is attributed "
                  "to her; she asks, she does not assert.",
        risk="LOW"),
    encik_rahman_fit=dict(
        character="Encik Rahman", established_role="Mentor / Kontraktor Senior",
        fits=True,
        conditional_on="the dialogue staying at process-overview level",
        reasoning="Naming the six supervisory activities and distinguishing soft from hard "
                  "landscape is ordinary senior-contractor knowledge and is exactly the "
                  "register he uses in B02 S02, where he confirms scope and points at "
                  "specifications. Nothing in that requires a credential.",
        risk="MEDIUM_IF_UNSCOPED"),
    specialist_expertise_required=dict(
        for_slide_2=False,
        for_the_unit=True,
        detail="The unit as a whole contains regulated content: pesticide use under statute, "
               "a licensed-operator requirement, SDS handling and spray-drift control. That "
               "material genuinely needs a licensed pesticide operator's competence. Slide 2 "
               "does not touch it."),
    unsupported_expertise_risk=dict(
        level="MEDIUM",
        description="If the Slide 2 dialogue is later extended into the Racun material, Encik "
                    "Rahman would be voicing statutory and licensing obligations that no "
                    "source attributes to him. A mentor character stating a legal requirement "
                    "converts a source citation into a character's word — and the source "
                    "itself says the person who sprays must be a licensed operator, which is "
                    "a competence the character bank does not give him.",
        mitigation="Bind Slide 2 to the seven process-and-category rows listed above and to "
                   "nothing else. All compliance content stays on T04-CT-04, quoted from the "
                   "source rather than spoken by a character. A gate holds this: no character "
                   "line may contain a compliance obligation.",
        residual_after_mitigation="LOW"),
    recommendation="ALYA_ENCIK_RAHMAN_CONTEXTUALLY_SUITABLE",
    recommendation_condition="Suitable FOR SLIDE 2 ONLY, with the dialogue scoped to the "
                             "process overview and the two landscape categories. This is not "
                             "a finding that the pair suits the whole unit — they are not "
                             "proposed anywhere near the Racun compliance screens.",
    new_character_required=False,
    new_character_would_be_required_if="Bariah wants the dialogue to carry pesticide "
                                       "licensing, PPE or spray-safety content, in which case "
                                       "the honest move is a licensed-operator character "
                                       "rather than putting regulated claims in a mentor's "
                                       "mouth.",
    status="PENDING_BARIAH_REVIEW",
    authority="CAIR_ASSESSMENT_NOT_A_BARIAH_RULING")

ALLOWED_FIT_RESULTS = ["ALYA_ENCIK_RAHMAN_CONTEXTUALLY_SUITABLE",
                       "NEW_CHARACTER_REQUIRED_WITH_REASON"]

SLIDE2_DIALOGUE = dict(
    contract_id="T04-CT-07",
    screen_candidate_id="T04-SC-07",
    slide_position="SLIDE_2",
    candidate_type="DIALOGUE_SCENARIO",
    content_status=CONTENT_STATUS,
    approval_status=APPROVAL_STATUS,
    instructional_authority=INSTRUCTIONAL_AUTHORITY,
    source_rows=["T04-ROW-001", "T04-ROW-002", "T04-ROW-003", "T04-ROW-004", "T04-ROW-005",
                 "T04-ROW-079", "T04-ROW-080"],
    cast=[("Alya", "Kontraktor Junior"), ("Encik Rahman", "Mentor / Kontraktor Senior")],
    cast_status="PROPOSED_SUBJECT_TO_D03_CONDITION",
    learner_facing_purpose="Introduce the maintenance phase from the site, and let the six "
                           "supervisory activities arrive as work rather than as a list.",
    base_state="Site visual with both characters present; dialogue plays as character video, "
               "full text in Notes — the B02 S02 pattern.",
    interaction_states=["BASE — dialogue plays"],
    completion_condition="dialogue complete",
    visual_treatment="Site setting showing a completed planting area with built landscape "
                     "elements visible. Subject is module-derived; the visual itself is "
                     "NEW_MMD_ASSET_REQUIRED and is NOT one of the 46 obligations — Bariah's "
                     "visual ruling covers content headings, not this scenario screen.",
    vo_proposal="Dialogue is the audio. No separate narrator VO on this screen.",
    speaker_notes_proposal="NON_SPOKEN_CONTEXT: unit and page provenance. SPOKEN_CONTENT_VO: "
                           "the dialogue turns. PRODUCTION_INSTRUCTION_NOT_SPOKEN: character "
                           "video direction and the compliance-exclusion rule.",
    accessibility_consideration="The full dialogue must exist as text, not only as audio, and "
                                "speaker attribution must be readable.",
    fallback_behaviour="If character video is unavailable, the dialogue renders as attributed "
                       "text. Nothing is lost — no fact lives only in the audio.",
    source_authority="MODULE_SOURCE_ATTESTED",
    compliance_content_excluded=True,
    compliance_exclusion_rule="No character line may state a legal, licensing, PPE, storage, "
                              "SDS, spraying, notification or reporting obligation. Those "
                              "belong to T04-CT-04, quoted from the source.",
    beats=[
        dict(beat=1, speaker="Alya", intent="Ask what follows once the construction and "
                                            "planting work is finished.",
             source_row_ids=["T04-ROW-002"],
             draft_line="Encik Rahman, kerja pembinaan dan tanaman di tapak ini dah siap. "
                        "Selepas ini apa yang perlu diuruskan?"),
        dict(beat=2, speaker="Encik Rahman",
             intent="Name the maintenance phase and point at its process flow.",
             source_row_ids=["T04-ROW-001", "T04-ROW-002", "T04-ROW-003"],
             draft_line="Sekarang masuk fasa penjagaan dan penyelenggaraan. Ada enam aktiviti "
                        "penyeliaan yang perlu berjalan, daripada koordinasi kerja sampailah "
                        "kepada perancangan sumber manusia."),
        dict(beat=3, speaker="Alya",
             intent="Ask whether maintenance is the same for everything on site.",
             source_row_ids=["T04-ROW-005", "T04-ROW-080"],
             draft_line="Semua elemen di tapak diselenggara sama caranya?"),
        dict(beat=4, speaker="Encik Rahman",
             intent="Draw the soft/hard distinction that organises the unit.",
             source_row_ids=["T04-ROW-004", "T04-ROW-005", "T04-ROW-079", "T04-ROW-080"],
             draft_line="Tidak. Landskap lembut itu elemen hidup — pokok, rumput, tanaman. "
                        "Landskap kejur pula elemen binaan yang kekal. Keperluan "
                        "penyelenggaraannya berbeza."),
        dict(beat=5, speaker="Alya",
             intent="Close on the learner's own next step.",
             source_row_ids=["T04-ROW-002"],
             draft_line="Jadi saya kena faham keperluan kedua-duanya sebelum susun jadual "
                        "penyelenggaraan."),
    ],
    drafting_basis="Bariah authorised drafting for the Rumusan and quiz (BR-W1). She did not "
                   "separately authorise dialogue drafting, but she did rule that Slide 2 "
                   "takes a dialogue scenario, and the stage instruction asks for a proposed "
                   "contract. The lines below are therefore CAIR_ASSISTED_DRAFT on the same "
                   "footing as the Rumusan — proposed, not approved, and hers to rewrite.",
    bariah_approval=dict(status=APPROVAL_STATUS, decision=None, comment=None))

# ------------------------------------------------------------------------------------------
# D-04 — the confirmed legal split
# ------------------------------------------------------------------------------------------
BASE_VISIBLE_ROWS = ["T04-ROW-065", "T04-ROW-066", "T04-ROW-067", "T04-ROW-068",
                     "T04-ROW-069", "T04-ROW-070", "T04-ROW-075"]
REVEAL_ELIGIBLE_ROWS = ["T04-ROW-071", "T04-ROW-072", "T04-ROW-073", "T04-ROW-074",
                        "T04-ROW-076", "T04-ROW-077", "T04-ROW-078"]
# Compliance rows outside the Racun section. Bariah's ruling addressed the Racun population
# she was asked about; these were not in scope and stay base-visible.
BAJA_COMPLIANCE_ROWS = ["T04-ROW-037", "T04-ROW-039", "T04-ROW-041", "T04-ROW-043",
                        "T04-ROW-045"]

D04_SPLIT = dict(
    decision_id="D-04",
    status="CONFIRMED_BARIAH_DIRECT",
    evidence=["BR-C1"],
    scope=UNIT_ID,
    applied_to_contracts=True,
    base_screen_must_show=[
        dict(item="Akta Racun Makhluk Perosak 1974", rows=["T04-ROW-066"],
             legibility="INFERRED — see EVIDENCE_LEGIBILITY"),
        dict(item="licensed operator requirement", rows=["T04-ROW-067"],
             legibility="LEGIBLE — 'rator berlesen … dipaparkan terus pada skrin'"),
        dict(item="PPE", rows=["T04-ROW-069", "T04-ROW-070"],
             legibility="LEGIBLE — 'dan PPE dipaparkan terus pada skrin'"),
    ],
    reveal_may_contain=[
        dict(item="SDS", rows=["T04-ROW-073", "T04-ROW-074"]),
        dict(item="safe or locked storage", rows=["T04-ROW-071", "T04-ROW-072"]),
        dict(item="spraying conditions", rows=["T04-ROW-076"]),
        dict(item="notification", rows=["T04-ROW-077"]),
        dict(item="reporting", rows=["T04-ROW-078"]),
    ],
    headings_always_visible=["T04-ROW-065", "T04-ROW-068", "T04-ROW-075"],
    base_visible_rows=BASE_VISIBLE_ROWS,
    reveal_eligible_rows=REVEAL_ELIGIBLE_ROWS,
    out_of_scope_rows_unchanged=BAJA_COMPLIANCE_ROWS,
    reveal_is_permissive="'boleh guna click to reveal' permits reveal; it does not require "
                         "it. A build that shows all seven on the base screen still complies.",
    delta_from_cair_proposal=dict(
        cair_proposed_reveal=["T04-ROW-070", "T04-ROW-072", "T04-ROW-074"],
        bariah_confirmed_reveal=REVEAL_ELIGIBLE_ROWS,
        moved_to_base=["T04-ROW-070"],
        newly_reveal_eligible=["T04-ROW-071", "T04-ROW-073", "T04-ROW-076", "T04-ROW-077",
                               "T04-ROW-078"],
        note="Two changes, in opposite directions. PPE detail moves ONTO the base screen — "
             "Bariah put PPE there explicitly. Spraying conditions, notification and "
             "reporting become reveal-eligible, which Stage 4.2F-B0.6 had argued against on "
             "the grounds that a learner who never interacts should still see them. She is "
             "the Instructional Designer and she has ruled; the ruling is implemented as "
             "written and the disagreement is recorded here rather than quietly re-litigated "
             "in a contract."),
    residual_risk="A learner who never interacts will not see the spray-drift limit, the "
                  "notification duty or the reporting duty. Worth one sentence to Bariah at "
                  "some future point; NOT worth re-asking now, since she answered the exact "
                  "question that was put to her.")

# ==========================================================================================
# PART 6 — TYPED APPROVAL TOTALS
# ==========================================================================================
_CONFIRMED = [d for d in DECISIONS if d["structural_status"] == "RESOLVED"]
_CONDITIONAL = [d for d in DECISIONS if d["structural_status"] == "CONDITIONALLY_RESOLVED"]

PENDING_CONTENT_REVIEWS = [
    dict(review_id="CR-1", title="Character instance mapping",
         decision="D-03",
         what="Confirm Alya and Encik Rahman for Slide 2, or name a replacement.",
         cair_position="Contextual fit assessed as suitable for Slide 2 only, conditional on "
                       "the dialogue staying at process-overview level.",
         status="PENDING_BARIAH_REVIEW"),
    dict(review_id="CR-2", title="Slide 2 dialogue review",
         decision="D-03",
         what="Review, edit or replace the five drafted dialogue turns.",
         cair_position="Drafted as CAIR_ASSISTED_DRAFT, bound to seven source rows, with all "
                       "compliance content deliberately excluded.",
         status="PENDING_BARIAH_REVIEW"),
    dict(review_id="CR-3", title="Rumusan v2 review",
         decision="D-02C",
         what="Accept, edit or remove the four drafted statements; confirm the four-point "
              "consolidation.",
         cair_position="Drafted to the Topik 3 Bahagian 2 style; T04-RUM2-04 carries a MEDIUM "
                       "factual-risk flag.",
         status="PENDING_BARIAH_REVIEW"),
    dict(review_id="CR-4", title="Five-slot quiz authoring, editing and approval",
         decision="D-02A",
         what="Author or approve the five items. Composition and pass mark are settled; the "
              "questions are not written.",
         cair_position="Blueprint only — five slots, six coverage points consolidated into "
                       "five with the merge named. No stem, option, key or rationale.",
         status="PENDING_BARIAH_REVIEW"),
]

APPROVAL_TOTALS = dict(
    CONFIRMED_POLICY_DECISIONS=len(_CONFIRMED),
    CONDITIONALLY_CONFIRMED_DECISIONS=len(_CONDITIONAL),
    APPROVED_FINAL_INSTRUCTIONAL_CONTENT_ITEMS=0,
    PENDING_BARIAH_CONTENT_REVIEWS=len(PENDING_CONTENT_REVIEWS),
    confirmed_policy_decision_ids=[d["decision_id"] for d in _CONFIRMED],
    conditionally_confirmed_decision_ids=[d["decision_id"] for d in _CONDITIONAL],
    superseded_field="APPROVED_ITEMS",
    supersession_note="Stage 4.2F-B0.6 reported APPROVED_ITEMS = 0. That single number "
                      "conflated policy with content: it was true of learner-facing text and "
                      "false of structure, since Bariah had already confirmed the visual "
                      "ruling and the quiz composition. Four typed totals replace it. "
                      "APPROVED_ITEMS is not emitted by this stage.")

# ==========================================================================================
# PART 7 — ASSET PLANNING LAYER
# ==========================================================================================
VISUAL_OBLIGATIONS = B06.VISUAL_OBLIGATIONS
VISUAL_OBLIGATION_COUNT = len(VISUAL_OBLIGATIONS)
UNIQUE_ASSET_COUNT = "NOT_YET_DETERMINED"
VISUAL_COVERAGE_STATUS = "NEW_MMD_VISUAL_COVERAGE_REQUIRED"

OBLIGATIONS_ARE_NOT_ASSETS = (
    f"{VISUAL_OBLIGATION_COUNT} obligations is a count of PLACES a visual is required. It is "
    "not a count of images to produce. One composite panel may discharge several obligations "
    "— the three fertiliser application methods are a single comparison in the source — and "
    "one obligation may need more than one state. Asserting UNIQUE_MMD_ASSETS = "
    f"{VISUAL_OBLIGATION_COUNT} would turn a requirement count into a production estimate "
    "that nobody has made.")

ASSET_GROUPS = [
    dict(group_id="AG-01", label="Six-step maintenance process",
         parent="PENJAGAAN DAN PENYELENGGARAAN",
         composite_rationale="The six steps are one linear flow in the source. They could be "
                             "six separate illustrations, one six-panel composite, or a "
                             "sequence of states over the redrawn diagram."),
    dict(group_id="AG-02", label="Landskap Lembut — category",
         parent="Landskap Lembut",
         composite_rationale="A single category-establishing visual."),
    dict(group_id="AG-03", label="Siram — operation and subtopics",
         parent="Siram",
         composite_rationale="Two natural composites sit inside this group: the implementation "
                             "methods, and the monitoring signs. The management subtopics are "
                             "more likely individual."),
    dict(group_id="AG-04", label="Baja — operation and subtopics",
         parent="Baja",
         composite_rationale="The three application methods are presented together in the "
                             "source and are a strong composite candidate."),
    dict(group_id="AG-05", label="Racun — IPM, control types and pesticide types",
         parent="Racun",
         composite_rationale="The IPM priority order and the three pesticide types are each "
                             "inherently comparative and would lose meaning split apart."),
    dict(group_id="AG-06", label="Racun — legal, HSE and risk compliance",
         parent="Racun",
         composite_rationale="Safety and compliance visuals. These interact with the D-04 "
                             "base/reveal split, so their grouping is not purely a production "
                             "question."),
    dict(group_id="AG-07", label="Landskap Kejur — category and four functions",
         parent="Landskap Kejur",
         composite_rationale="Five visuals whose subjects are architectural; a shared visual "
                             "language matters more here than elsewhere."),
]

_GROUP_FOR = {}
for _v in VISUAL_OBLIGATIONS:
    g = _v["population_group"]
    p = _v["parent_topic"]
    if g == "A_PROCESS_NODES":
        _GROUP_FOR[_v["visual_obligation_id"]] = "AG-01"
    elif g == "B_LEMBUT_MAIN":
        _GROUP_FOR[_v["visual_obligation_id"]] = "AG-02"
    elif p == "Siram":
        _GROUP_FOR[_v["visual_obligation_id"]] = "AG-03"
    elif p == "Baja":
        _GROUP_FOR[_v["visual_obligation_id"]] = "AG-04"
    elif p == "Racun":
        _GROUP_FOR[_v["visual_obligation_id"]] = (
            "AG-06" if _v["raw_source_heading"] in ("Perundangan dan Pelesenan",
                                                    "Keselamatan dan Kesihatan (HSE)",
                                                    "Pengurusan Risiko",
                                                    "Aspek Pengurusan untuk Kontraktor:")
            else "AG-05")
    else:
        _GROUP_FOR[_v["visual_obligation_id"]] = "AG-07"

# Composite candidates the SOURCE itself presents as a set. Anything not listed stays
# UNDETERMINED — a guess dressed as a plan is worse than an open field.
_COMPOSITE_CANDIDATES = {
    "Kaedah Pelaksanaan": "COMPOSITE_CANDIDATE — the source presents the methods as a set",
    "Sistem Pengairan Automatik": "COMPOSITE_CANDIDATE — sprinkler against drip, one frame",
    "Pemantauan & Pelaporan": "COMPOSITE_CANDIDATE — both failure directions in one frame",
    "IPM memberi keutamaan kepada:": "COMPOSITE_CANDIDATE — the order is the teaching point",
    "Jenis Racun": "COMPOSITE_CANDIDATE — type paired with target",
    "Estetika dan Reka Bentuk": "COMPOSITE_CANDIDATE — contrast needs two things in frame",
}

# Subjects that recur across the unit and look reusable but are NOT.
_NEAR_DUPLICATES = {
    "T04-ROW-042": ("SIMILAR_SUBJECT_DO_NOT_REUSE",
                    "PPE appears here (gloves and face mask for chemical fertiliser) and "
                    "again under Racun HSE (respirator, goggles, chemical gloves, protective "
                    "suit). Different equipment for different hazards — one asset would "
                    "misstate one of them."),
    "T04-ROW-068": ("SIMILAR_SUBJECT_DO_NOT_REUSE",
                    "See T04-ROW-042. The pesticide PPE set is materially heavier."),
    "T04-ROW-040": ("SIMILAR_SUBJECT_DO_NOT_REUSE",
                    "Fertiliser storage is dry, secure and away from water. Pesticide storage "
                    "is locked, labelled and ventilated. Reusing one for the other would "
                    "understate the pesticide requirement."),
}

_SC_FOR_GROUP = {"AG-01": "T04-SC-01", "AG-02": "T04-SC-02", "AG-03": "T04-SC-02",
                 "AG-04": "T04-SC-02", "AG-05": "T04-SC-02", "AG-06": "T04-SC-03",
                 "AG-07": "T04-SC-05"}


def _asset_plan():
    out = []
    for v in VISUAL_OBLIGATIONS:
        vid = v["visual_obligation_id"]
        gid = _GROUP_FOR[vid]
        head = v["raw_source_heading"]
        first_row = v["source_row_ids"][0]
        composite = _COMPOSITE_CANDIDATES.get(head, "UNDETERMINED_PENDING_BARIAH")
        reuse, reuse_note = _NEAR_DUPLICATES.get(first_row, ("NOT_YET_ASSESSED", ""))
        if v["proposed_visual_class"] == "PENDING_HUMAN":
            composite = "NOT_APPLICABLE — no subject proposed"
        out.append(dict(
            obligation_id=vid,
            proposed_asset_group_id=gid,
            unique_asset_candidate_id="NOT_YET_ASSIGNED",
            composite_or_individual=composite,
            reuse_allowed=reuse,
            reuse_note=reuse_note,
            screens_or_states_served=_SC_FOR_GROUP[gid] + " — state count not yet decided",
            production_status="NOT_STARTED",
            bariah_approval_requirement="SUBJECT_AND_STYLE_APPROVAL_REQUIRED"))
    return out


ASSET_PLAN = _asset_plan()
ASSET_PLAN_FIELDS = ["obligation_id", "proposed_asset_group_id", "unique_asset_candidate_id",
                     "composite_or_individual", "reuse_allowed", "screens_or_states_served",
                     "production_status", "bariah_approval_requirement"]

ASSET_TOTALS = dict(
    VISUAL_OBLIGATIONS=VISUAL_OBLIGATION_COUNT,
    UNIQUE_ASSET_COUNT=UNIQUE_ASSET_COUNT,
    VISUAL_COVERAGE_STATUS=VISUAL_COVERAGE_STATUS,
    asset_groups=len(ASSET_GROUPS),
    composite_candidates=len([r for r in ASSET_PLAN
                              if r["composite_or_individual"].startswith("COMPOSITE")]),
    undetermined=len([r for r in ASSET_PLAN
                      if r["composite_or_individual"].startswith("UNDETERMINED")]),
    do_not_reuse=len([r for r in ASSET_PLAN
                      if r["reuse_allowed"] == "SIMILAR_SUBJECT_DO_NOT_REUSE"]),
    production_started=0,
    slide_2_visual_note="The Slide 2 dialogue scenario needs a visual too, and it is NOT one "
                        "of the 46. Bariah's visual ruling covers content headings; the "
                        "scenario screen arrives from a separate ruling (BR-C3).")

# ==========================================================================================
# PART 8 — READINESS
# ==========================================================================================
READINESS = dict(
    structural_decisions_status="CLOSED",
    structural_decisions=[dict(decision_id=d["decision_id"], title=d["title"],
                               status=d["status"], structural_status=d["structural_status"])
                          for d in DECISIONS],
    remaining_work=[r["title"] for r in PENDING_CONTENT_REVIEWS],
    storyboard_status="NOT_GENERATED",
    storyboard_approval="NOT_APPROVED — no storyboard exists for T04",
    mmd_status="NOT_STARTED",
    what_is_not_claimed=[
        "that the final storyboard is approved — none has been generated",
        "a final screen count",
        "a unique MMD asset count",
        "that any learner-facing text is approved",
        "that the character instance mapping is complete",
    ])

# ==========================================================================================
# MAPPING v3 AND CONTRACTS v3
# ==========================================================================================
_LEGAL_SC = "T04-SC-03"

MAPPING_V3 = []
for _m in B06.MAPPING_V2:
    _d = dict(_m)
    _d["revision"] = "v3"
    _d["slide_position"] = "NOT_ASSIGNED"
    if _m["screen_candidate_id"] == _LEGAL_SC:
        _d["d04_split_applied"] = True
        _d["base_visible_rows"] = list(BASE_VISIBLE_ROWS)
        _d["reveal_eligible_rows"] = list(REVEAL_ELIGIBLE_ROWS)
        _d["popup_reveal_implications"] = (
            "D-04 is CONFIRMED and applied. Statute, licensed operator and PPE are base-"
            "visible and may not be moved. SDS, storage, spraying conditions, notification "
            "and reporting are reveal-eligible — permitted, not required.")
        _d["decision_still_required"] = "visual subject and style approval for three assets"
    elif _m["screen_candidate_id"] == "T04-SC-01":
        _d["d04_split_applied"] = False
        _d["decision_still_required"] = ("none structural — D-05 confirmed; visual subject "
                                         "and style approval for six assets")
    else:
        _d["d04_split_applied"] = False
    MAPPING_V3.append(_d)

MAPPING_V3.append(dict(
    screen_candidate_id="T04-SC-07",
    working_title="Slide 2 — perbualan senario penjagaan dan penyelenggaraan",
    revision="v3",
    slide_position="SLIDE_2",
    previous_visual_assumption="DID NOT EXIST — Stage 4.2F-B0.6 proposed no dialogue screen "
                               "and D-03 was unresolved.",
    new_bariah_visual_obligation="BR-C3 — an additional character in a dialogue scenario on "
                                 "Slide 2. This is a NEW screen, not a revision of one.",
    visual_obligation_ids=[],
    required_visual_states=0,
    available_source_visual="NONE",
    missing_production_asset="1 scenario visual plus character video — counted separately "
                             "from the 46 content obligations",
    possible_screen_expansion="none — one screen",
    popup_reveal_implications="none — dialogue plays in the base state",
    learner_screen_count_impact="+1",
    runtime_state_count_impact="+1",
    d04_split_applied=False,
    decision_still_required="CR-1 character instance mapping; CR-2 dialogue review"))

MAPPING_IMPACT_V3 = dict(
    B06.MAPPING_IMPACT,
    final_screen_count=FINAL_SCREEN_COUNT,
    candidates=len(MAPPING_V3),
    new_candidate_this_stage="T04-SC-07",
    headline="D-01 through D-05 are now closed, so the mapping's open questions are content "
             "questions rather than structural ones. One screen was ADDED — the Slide 2 "
             "dialogue scenario Bariah ruled for in BR-C3. The 28 unmapped visual obligations "
             "from Stage 4.2F-B0.6 are unchanged: closing the structural decisions did not "
             "give them a home, and a screen count still cannot be claimed.")

_CT_TO_SC = {"T04-CT-01": "T04-SC-01", "T04-CT-02": "T04-SC-02", "T04-CT-03": "T04-SC-05",
             "T04-CT-04": "T04-SC-03", "T04-CT-05": "T04-SC-04", "T04-CT-06": "T04-SC-06"}

CONTRACTS_V3 = []
for _c in B06.CONTRACTS_V2:
    _d = dict(_c)
    _d["revision"] = "v3"
    _d["bariah_approval"] = dict(status=APPROVAL_STATUS, decision=None, comment=None)
    if _c["contract_id"] == "T04-CT-04":
        _d["superseded_base_state"] = _c["base_state"]
        _d["base_state"] = (
            "D-04 CONFIRMED SPLIT APPLIED. Base state carries, and may not hide: the heading "
            "Perundangan dan Pelesenan; Akta Racun Makhluk Perosak 1974 (T04-ROW-066); the "
            "licensed-operator requirement (T04-ROW-067); the heading Keselamatan dan "
            "Kesihatan (HSE); PPE Lengkap and its item list (T04-ROW-069, T04-ROW-070); and "
            "the heading Pengurusan Risiko. Reveal-eligible: storage (T04-ROW-071, "
            "T04-ROW-072), SDS (T04-ROW-073, T04-ROW-074), spraying conditions "
            "(T04-ROW-076), notification (T04-ROW-077), reporting (T04-ROW-078).")
        _d["interaction_states"] = ["BASE (statute, licensed operator, PPE visible)",
                                    "REVEAL_STORAGE", "REVEAL_SDS", "REVEAL_SPRAY_CONDITIONS",
                                    "REVEAL_NOTIFICATION", "REVEAL_REPORTING", "ALL_VIEWED"]
        _d["hidden_content_classification"] = "BARIAH_CONFIRMED_REVEAL_ELIGIBLE"
        _d["hidden_content_justification"] = (
            "What may be hidden is hidden on Bariah's direct confirmation (BR-C1), not on "
            "CAIR's judgement. Stage 4.2F-B0.6 argued that spraying conditions, notification "
            "and reporting should stay base-visible; she ruled otherwise and her ruling is "
            "implemented. The residual risk — a non-interacting learner does not see those "
            "three — is recorded in D04_SPLIT.residual_risk rather than silently designed "
            "around.")
        _d["base_visible_rows"] = list(BASE_VISIBLE_ROWS)
        _d["reveal_eligible_rows"] = list(REVEAL_ELIGIBLE_ROWS)
        _d["open_decision"] = "D-01 subject approval for three assets"
    elif _c["contract_id"] == "T04-CT-01":
        _d["open_decision"] = "D-01 subject approval for six step assets"
        _d["d05_status"] = "CONFIRMED_BARIAH_DIRECT"
    CONTRACTS_V3.append(_d)

CONTRACTS_V3.append(dict(
    contract_id=SLIDE2_DIALOGUE["contract_id"],
    candidate_type=SLIDE2_DIALOGUE["candidate_type"],
    revision="v3",
    source_rows=list(SLIDE2_DIALOGUE["source_rows"]),
    learner_facing_purpose=SLIDE2_DIALOGUE["learner_facing_purpose"],
    base_state=SLIDE2_DIALOGUE["base_state"],
    interaction_states=list(SLIDE2_DIALOGUE["interaction_states"]),
    completion_condition=SLIDE2_DIALOGUE["completion_condition"],
    visual_treatment=SLIDE2_DIALOGUE["visual_treatment"],
    superseded_visual_treatment="NONE — new contract",
    text_treatment="Five dialogue turns, CAIR_ASSISTED_DRAFT, bound to seven source rows.",
    vo_proposal=SLIDE2_DIALOGUE["vo_proposal"],
    speaker_notes_proposal=SLIDE2_DIALOGUE["speaker_notes_proposal"],
    accessibility_consideration=SLIDE2_DIALOGUE["accessibility_consideration"],
    fallback_behaviour=SLIDE2_DIALOGUE["fallback_behaviour"],
    source_authority=SLIDE2_DIALOGUE["source_authority"],
    visual_obligation_ids=[],
    required_visual_states=0,
    visual_ruling_authority="BARIAH_DIRECT_SCREENSHOT",
    visual_subject_authority="MODULE_SOURCE_ATTESTED",
    missing_production_asset="1 scenario visual plus character video",
    open_decision="CR-1 character instance mapping; CR-2 dialogue review",
    hidden_content_classification="NOT_APPLICABLE_NOTHING_IS_HIDDEN",
    hidden_content_justification="The dialogue plays in the base state and carries no "
                                 "compliance obligation.",
    bariah_approval=dict(status=APPROVAL_STATUS, decision=None, comment=None)))

# ==========================================================================================
# WHATSAPP — CONTENT REVIEW REQUEST
# ==========================================================================================
WHATSAPP = dict(
    language="Malay", channel="WhatsApp", status="DRAFT_NOT_SENT",
    sending_authority="FIRDAUS", audience="BARIAH",
    text="""Terima kasih Bariah. Semua keputusan struktur untuk Topik 4 sudah lengkap dan direkodkan:

• Visual — setiap langkah proses, Landskap Lembut dan sub-topiknya, Landskap Kejur dan empat kumpulannya. 46 visual disenaraikan satu per satu.
• Kuiz — 4 MCQ dan 1 Multiple Response, markah lulus 60%, untuk semua PL dalam Kursus.
• Kandungan Akta — Akta, operator berlesen dan PPE kekal pada skrin utama. SDS, penyimpanan, penyemburan, notifikasi dan laporan boleh guna click to reveal.
• Rajah enam langkah — guna rajah asal dalam papan cerita, dilukis semula kemudian, susunan enam langkah kekal sama.
• Slide 2 — perbualan dialog senario dengan watak tambahan.

Tinggal 4 perkara yang perlu semakan Bariah, semuanya berkaitan kandungan:

1. Watak Slide 2 — kami dapati Alya & Encik Rahman sesuai untuk Slide 2, kerana perbualan itu hanya mengenai aliran proses dan perbezaan landskap lembut dengan landskap kejur. Kami sengaja tidak letak kandungan racun atau undang-undang dalam perbualan itu. Mohon Bariah sahkan.
2. Draf perbualan Slide 2 — 5 baris dialog. Mohon semak, ubah atau ganti.
3. Draf Rumusan — 4 ayat mengikut gaya Topik 3 Bahagian 2. Mohon semak.
4. Rangka kuiz 5 soalan — struktur sudah muktamad, tetapi soalan belum ditulis. Mohon Bariah semak apa yang diuji setiap soalan, atau tulis sendiri.

Untuk makluman:
• Papan cerita Topik 4 masih belum dijana.
• Belum ada aset visual dihasilkan.
• Rumusan, dialog dan kuiz semuanya masih draf — belum diluluskan.

Terima kasih.""",
    constraints_honoured=["thanks Bariah",
                          "summarises the five structural decisions now closed",
                          "asks only the four remaining content reviews",
                          "no QA or engineering terminology",
                          "states that no storyboard has been generated",
                          "states that no visual asset has been produced",
                          "states that Rumusan, dialogue and quiz remain drafts"],
    not_asked_again=["D-01 visual population", "D-02A quiz composition",
                     "D-02B pass threshold", "D-04 legal split",
                     "D-05 diagram treatment"])

# ==========================================================================================
PPTX_GENERATED = 0
GENERATOR_TOUCHED = 0
MMD_PRODUCTION_STARTED = 0
B02_FAMILIES_PROPAGATED = 0

VERDICT = "T04_STRUCTURAL_RULINGS_CLOSED_READY_FOR_CONTENT_APPROVAL"
ALLOWED_VERDICTS = [VERDICT, "T04_STRUCTURAL_RULINGS_CONSOLIDATION_BLOCKED"]

if __name__ == "__main__":
    print(json.dumps(dict(
        decisions={d["decision_id"]: d["status"] for d in DECISIONS},
        approval_totals={k: v for k, v in APPROVAL_TOTALS.items() if isinstance(v, int)},
        assets={k: v for k, v in ASSET_TOTALS.items() if not isinstance(v, str) or k in
                ("UNIQUE_ASSET_COUNT", "VISUAL_COVERAGE_STATUS")},
        d04=dict(base=len(BASE_VISIBLE_ROWS), reveal=len(REVEAL_ELIGIBLE_ROWS)),
        fit=CONTEXTUAL_FIT["recommendation"],
        candidates=len(MAPPING_V3), contracts=len(CONTRACTS_V3)),
        ensure_ascii=False, indent=1))
