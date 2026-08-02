# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.6 — the ONE controlled data source for Bariah's partial rulings on T04.

Everything downstream of this module (Markdown, CSV, JSON) is emitted from here, so the
three representations cannot drift.

AUTHORITY MODEL, enforced by gate throughout
--------------------------------------------
Two different authorities are carried on every visual obligation and must never be merged:

    treatment_authority  BARIAH_DIRECT_SCREENSHOT
                         Bariah ruled that a visual is REQUIRED here. That ruling is
                         evidenced by the two frozen screenshots.

    subject_authority    MODULE_SOURCE_ATTESTED
                         WHAT the visual shows comes from the module, not from Bariah.
                         Bariah required a visual; she did not specify its content.

Labelling a module-derived subject BARIAH_DIRECT would invent a ruling she never gave.
Gate SUBJECT_AUTHORITY_NEVER_BARIAH_DIRECT holds this.

Bariah is the sole Instructional Designer. CAIR / Claude Code performs source analysis,
traceability, visual-direction proposals and drafting. Nothing here is approved content.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_data_v1 as SRC
import t04_pack_data_v1 as PACK

STAGE = "4.2F-B0.6"
UNIT_ID = "K5-PL06-T04-B01"
LESSON_TITLE = "Penjagaan dan Penyelenggaraan"
GENERATED_BY = "docs/pl06/t04/tools/t04_rulings_emit_v1.py"

CONTENT_STATUS = "CAIR_ASSISTED_DRAFT"
APPROVAL_STATUS = "PENDING_BARIAH_REVIEW"
INSTRUCTIONAL_AUTHORITY = "BARIAH"
FINAL_SCREEN_COUNT = "NOT_CLAIMED"

FORBIDDEN_LABELS = ["ID_AUTHORED", "BARIAH_APPROVED", "FINAL_INSTRUCTIONAL_CONTENT",
                    "APPROVED", "FINAL"]

TREATMENT_AUTHORITY = "BARIAH_DIRECT_SCREENSHOT"
SUBJECT_AUTHORITY = "MODULE_SOURCE_ATTESTED"
SOURCE_AUTHORITY = "MODULE_SOURCE_ATTESTED"

ALLOWED_VISUAL_CLASSES = [
    "SOURCE_SMARTART", "PROCESS_DIAGRAM", "PROCEDURAL_ILLUSTRATION", "CONCEPTUAL_DIAGRAM",
    "COMPARISON_VISUAL", "EQUIPMENT_OR_ACTIVITY_VISUAL", "SAFETY_OR_COMPLIANCE_VISUAL",
    "SOURCE_GROUNDED_PHOTO_DIRECTION", "PENDING_HUMAN",
]

NEW_ASSET = "NEW_MMD_ASSET_REQUIRED"
NO_SOURCE_IMAGE = "NONE_IN_SOURCE"
SMARTART_LABEL_ONLY = "SOURCE_SMARTART_NODE_LABEL_ONLY"

BY_ID = SRC.BY_ID
ROWS = SRC.ROWS

# ==========================================================================================
# PART 1 — FROZEN BARIAH EVIDENCE
# ==========================================================================================
# Both files were written byte-for-byte from the bytes delivered with the Stage 4.2F-B0.6
# instruction. Nothing was cropped, recompressed, rotated or annotated.
#
# LIMITATION, recorded rather than papered over: the original uploaded filenames are not
# recoverable. The images arrived as inline image blocks on the instruction message, not as
# named files in the upload area, and no filename is carried anywhere in the session record.
# The frozen names below were assigned by CAIR following the existing B02 evidence naming
# pattern in the same directory. The BYTES are the evidence; the names are not.
EVIDENCE_DIR = "reviews/storyboard-bariah/t04_bariah_review"

EVIDENCE = [
    dict(evidence_id="T04-EV-01",
         frozen_filename="T04_BARIAH_VISUAL_REQUIREMENT_SHEET_20260802.jpg",
         frozen_path=EVIDENCE_DIR + "/T04_BARIAH_VISUAL_REQUIREMENT_SHEET_20260802.jpg",
         original_uploaded_filename="NOT_RECOVERABLE_FROM_SESSION_TRANSPORT",
         byte_size=75362,
         sha256="95f84819c70b6ef89fb8fe29ddd8ac19850014790de18587a0cfe850637a2008",
         media_type="image/jpeg", dimensions_px="772 x 697", colour_mode="RGB",
         evidence_date="2026-08-02",
         received_utc="2026-08-02T08:52:01Z",
         reviewer="BARIAH",
         evidence_class="BARIAH_DIRECT_SCREENSHOT",
         scope=UNIT_ID,
         modification="NONE — byte-identical",
         description="Bariah's marked-up T04 visual requirement sheet, titled 'PL06 Topik 4'. "
                     "A three-row table: the module's opening process diagram, Landskap "
                     "Lembut, and Landskap Kejur, each with a handwritten-style requirement "
                     "in the right-hand cell.",
         ruling_locators=["BR-L1", "BR-L2", "BR-L3", "BR-L4", "BR-L5", "BR-L6"]),
    dict(evidence_id="T04-EV-02",
         frozen_filename="T04_BARIAH_QUIZ_RUMUSAN_WHATSAPP_20260802.webp",
         frozen_path=EVIDENCE_DIR + "/T04_BARIAH_QUIZ_RUMUSAN_WHATSAPP_20260802.webp",
         original_uploaded_filename="NOT_RECOVERABLE_FROM_SESSION_TRANSPORT",
         byte_size=121162,
         sha256="0ae2aa29a05640495f42863b9c5e7daa2a1adaa1961f925951b9e393fd2154e9",
         media_type="image/webp", dimensions_px="1076 x 1338", colour_mode="RGB",
         evidence_date="2026-08-02",
         received_utc="2026-08-02T08:52:01Z",
         reviewer="BARIAH",
         evidence_class="BARIAH_DIRECT_SCREENSHOT",
         scope=UNIT_ID,
         modification="NONE — byte-identical",
         description="WhatsApp conversation 'Bariah eLearning'. Carries the same requirement "
                     "sheet shared at 4:41 PM captioned '1. Visual', then two written "
                     "messages at 4:44 PM and 4:45 PM giving the quiz, Rumusan and "
                     "Kandungan Akta rulings.",
         ruling_locators=["BR-W1", "BR-W2", "BR-W3", "BR-W4", "BR-W5"]),
]

# Every ruling quoted verbatim from the frozen evidence, with where to find it.
RULING_LOCATORS = [
    dict(locator="BR-L1", evidence_id="T04-EV-01",
         position="requirement sheet, row 1 (process diagram), right cell",
         verbatim="Perlu visual juga untuk setiap langkah",
         reading="A visual is required for EVERY step of the six-step process, in addition "
                 "to the existing diagram."),
    dict(locator="BR-L2", evidence_id="T04-EV-01",
         position="requirement sheet, row 2 (Landskap Lembut), right cell, line 1",
         verbatim="Penerangan utama – perlu visual",
         reading="The Landskap Lembut main explanation requires a visual."),
    dict(locator="BR-L3", evidence_id="T04-EV-01",
         position="requirement sheet, row 2 (Landskap Lembut), right cell, line 2",
         verbatim="Siram, Baja, Racun, - penerangan utama perlu visual",
         reading="Each of the three named operations requires a visual for its main "
                 "explanation."),
    dict(locator="BR-L4", evidence_id="T04-EV-01",
         position="requirement sheet, row 2 (Landskap Lembut), right cell, line 3",
         verbatim="Their sub – perlu visual",
         reading="Every source subtopic beneath Siram, Baja and Racun requires a visual. "
                 "Bariah did not enumerate them; this inventory enumerates them from the "
                 "controlled extract so that 'their sub' is never carried forward as a "
                 "vague phrase."),
    dict(locator="BR-L5", evidence_id="T04-EV-01",
         position="requirement sheet, row 3 (Landskap Kejur), right cell, line 1",
         verbatim="Penerangan utama – perlu visual",
         reading="The Landskap Kejur main explanation requires a visual."),
    dict(locator="BR-L6", evidence_id="T04-EV-01",
         position="requirement sheet, row 3 (Landskap Kejur), right cell, line 2",
         verbatim="Pengurusan Ruang dan Sirkulasi, Fungsi Struktur dan Kejuruteraan, "
                  "Kebolehgunaan dan Kemudahan, Estetika dan Reka Bentuk – perlu visual",
         reading="The four named Landskap Kejur groups each require a visual. Bariah named "
                 "these four explicitly and did NOT extend the requirement to their "
                 "sub-items — see SCOPE_ASYMMETRY below."),
    dict(locator="BR-W1", evidence_id="T04-EV-02", position="WhatsApp, 4:44 PM, line 1",
         verbatim="Kuiz & Rumusan - Yes. please draft. I will check.",
         reading="CAIR is authorised to prepare drafts of both. Bariah reviews them. "
                 "Drafting authorisation is not approval."),
    dict(locator="BR-W2", evidence_id="T04-EV-02", position="WhatsApp, 4:44 PM, line 2",
         verbatim="Kuiz - 4 MCQ, 1 Multiple Response - Apply to ALL PLs in Kursus",
         reading="Quiz composition is confirmed and its scope is the whole Kursus, not T04 "
                 "and not PL06 alone."),
    dict(locator="BR-W3", evidence_id="T04-EV-02", position="WhatsApp, 4:44 PM, line 3",
         verbatim="Rumusan - Follow writing style Topik 3 Bahagian 2",
         reading="A STYLE instruction. It governs how the Rumusan is written, not what it "
                 "says. T04 facts only."),
    dict(locator="BR-W4", evidence_id="T04-EV-02", position="WhatsApp, 4:44 PM, line 4",
         verbatim="Kandungan Akta - Tak pasti ni yang di mana?",
         reading="Bariah is asking which content the legislative question referred to. This "
                 "is a question back to us, not a ruling."),
    dict(locator="BR-W5", evidence_id="T04-EV-02", position="WhatsApp, 4:45 PM",
         verbatim="4. Kandungan Akta - tak pasti penerangan tambahan yang mana? Click to "
                  "reveal jika diperlukan",
         reading="Bariah asks which supplementary explanation was meant, and indicates that "
                 "click-to-reveal is acceptable IF needed. That is a conditional, not a "
                 "confirmed split."),
]

# An observation, recorded because it is material — NOT turned into a seventh question.
SCOPE_ASYMMETRY = dict(
    observation="Under Landskap Lembut, Bariah wrote 'Their sub – perlu visual' (BR-L4). "
                "Under Landskap Kejur she named four groups and stopped (BR-L6); the eight "
                "source sub-items beneath those four groups are not covered by her ruling.",
    handling="The inventory covers exactly what she named. No obligation was created for the "
             "eight Landskap Kejur sub-items. The asymmetry may be deliberate — the Kejur "
             "sub-items are one-line examples, whereas the Lembut sub-items are full "
             "management topics.",
    status="RECORDED_NOT_ESCALATED",
    reason="Part 9 restricts the follow-up to the six genuinely unresolved items, and asking "
           "Bariah to restate a ruling she gave clearly would be exactly the reconfirmation "
           "the brief prohibits.",
    kejur_sub_items_not_covered=["T04-ROW-082", "T04-ROW-084", "T04-ROW-087", "T04-ROW-089",
                                 "T04-ROW-092", "T04-ROW-094", "T04-ROW-097", "T04-ROW-099"])

# ==========================================================================================
# PART 2 — EXACT DECISION STATUS
# ==========================================================================================
DECISION_STATUSES = ["CONFIRMED_BARIAH_DIRECT", "CONFIRMED_WITH_EXPANSION",
                     "DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW", "PARTIALLY_RESOLVED",
                     "CLARIFICATION_REQUIRED", "UNRESOLVED"]

DECISIONS = [
    dict(decision_id="D-01", title="Visual treatment",
         status="CONFIRMED_WITH_EXPANSION",
         ruling="VISUAL_REQUIRED_FOR_BARIAH_NAMED_POPULATION",
         evidence=["BR-L1", "BR-L2", "BR-L3", "BR-L4", "BR-L5", "BR-L6"],
         superseded_recommendation="TEXT_AND_DIAGRAM_LED",
         supersession_note="The Stage 4.2F-B0.5 recommendation was TEXT_AND_DIAGRAM_LED — "
                           "that photographs were unnecessary and the SmartArt plus text "
                           "layouts would carry the unit. Bariah did not accept that as the "
                           "final ruling. It is recorded here as SUPERSEDED and must not be "
                           "carried forward as though it were confirmed.",
         what_bariah_required=[
             "A. a visual for every step in the main six-step process",
             "B. Landskap Lembut — main explanation; Siram, Baja and Racun main "
             "explanations; and every source subtopic beneath each of the three",
             "C. Landskap Kejur — main explanation, plus Pengurusan Ruang dan Sirkulasi, "
             "Fungsi Struktur dan Kejuruteraan, Kebolehgunaan dan Kemudahan, and Estetika "
             "dan Reka Bentuk"],
         what_bariah_did_not_specify="The SUBJECT of any visual. Every subject in the "
                                     "inventory is derived from the module and carries "
                                     "subject_authority = MODULE_SOURCE_ATTESTED.",
         scope="THIS_UNIT_ONLY",
         open_points=["visual subject and style approval for all 46 obligations",
                      "whether the eight Landskap Kejur sub-items are in or out — see "
                      "SCOPE_ASYMMETRY"]),
    dict(decision_id="D-02A", title="Quiz composition",
         status="CONFIRMED_BARIAH_DIRECT",
         ruling="4 MCQ + 1 MULTIPLE_RESPONSE",
         evidence=["BR-W2"],
         superseded_recommendation="Structure options A and B offered in Stage 4.2F-B0.5",
         supersession_note="Option A is confirmed. Option B is closed.",
         what_bariah_required=["exactly four MCQ items", "exactly one Multiple Response item"],
         what_bariah_did_not_specify="Any question content, stem, option, key or rationale.",
         scope="ALL_PLS_IN_KURSUS",
         open_points=["none on composition — the composition itself is settled"]),
    dict(decision_id="D-02B", title="Passing threshold",
         status="UNRESOLVED",
         ruling=None,
         evidence=[],
         superseded_recommendation=None,
         supersession_note="Bariah's message settles composition and says nothing about a "
                           "pass mark. The 60 percent figure comes from A3, which is the B02 "
                           "slice of the Style and Guidelines. It remains UNCONFIRMED for "
                           "T04 and for the Kursus.",
         what_bariah_required=[],
         what_bariah_did_not_specify="The pass threshold.",
         scope="POTENTIALLY_ALL_PLS_IN_KURSUS",
         open_points=["confirm or set the pass mark"]),
    dict(decision_id="D-02C", title="Rumusan",
         status="DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW",
         ruling="FOLLOW_WRITING_STYLE_TOPIK_3_BAHAGIAN_2",
         evidence=["BR-W1", "BR-W3"],
         superseded_recommendation=None,
         supersession_note="'Yes. please draft. I will check.' authorises drafting and "
                           "reserves approval. Drafting authorisation is NOT approval, and "
                           "the draft stays CAIR_ASSISTED_DRAFT.",
         what_bariah_required=["a draft she can check",
                               "the writing style of Topik 3 Bahagian 2"],
         what_bariah_did_not_specify="Any T04 content. Style was specified; facts were not. "
                                     "No B02 fact is copied into the T04 Rumusan.",
         scope="THIS_UNIT_ONLY",
         open_points=["review, edit or approve the four drafted statements",
                      "confirm the four-point consolidation"]),
    dict(decision_id="D-03", title="T04 cast",
         status="UNRESOLVED",
         ruling=None,
         evidence=[],
         superseded_recommendation="HILMI_NARRATOR_LED",
         supersession_note="The Stage 4.2F-B0.5 recommendation named Hilmi as narrator. "
                           "Bariah's rulings say nothing about cast. Hilmi must NOT be "
                           "carried forward as approved treatment.",
         what_bariah_required=[],
         what_bariah_did_not_specify="Anything about narrator or characters for T04.",
         scope="THIS_UNIT_ONLY",
         open_points=["choose narrator/cast treatment for T04"]),
    dict(decision_id="D-04", title="Legislative content",
         status="CLARIFICATION_REQUIRED",
         ruling=None,
         evidence=["BR-W4", "BR-W5"],
         superseded_recommendation="Core legal obligations on the base screen; supplementary "
                                   "explanation may use reveal",
         supersession_note="Bariah asked two questions rather than confirming: which content "
                           "was meant, and which supplementary explanation was meant. She "
                           "added that click-to-reveal is acceptable 'jika diperlukan' — a "
                           "conditional. The prior recommendation is NOT approved.",
         what_bariah_required=[],
         what_bariah_did_not_specify="Which rows are mandatory-visible and which may reveal.",
         scope="THIS_UNIT_ONLY",
         open_points=["identify the affected rows precisely, then confirm the base/reveal "
                      "split row by row"]),
    dict(decision_id="D-05", title="SmartArt production treatment",
         status="PARTIALLY_RESOLVED",
         ruling="EVERY_PROCESS_STEP_REQUIRES_A_VISUAL",
         evidence=["BR-L1"],
         superseded_recommendation=None,
         supersession_note="BR-L1 settles one part of D-05 and leaves three parts open.",
         what_bariah_required=["a visual for each of the six process steps"],
         what_bariah_did_not_specify="Whether the review storyboard uses the source-bound "
                                     "six-step diagram; how MMD redraws it; and what "
                                     "mechanism preserves the six-node identity and order.",
         scope="THIS_UNIT_ONLY",
         open_points=["source-bound diagram in the review storyboard — not confirmed",
                      "MMD redraw treatment — not confirmed",
                      "six-node sequence preservation mechanism — not confirmed"]),
]

# ==========================================================================================
# PART 3 — VISUAL OBLIGATION INVENTORY
# ==========================================================================================
# The population is DERIVED from the controlled extract, not typed by hand, so a gate can
# check that every source descendant is present.

_SEQ = {r["row_id"]: i for i, r in enumerate(ROWS)}


def _row(rid):
    if rid not in BY_ID:
        raise RuntimeError(f"row not in the controlled extract: {rid}")
    return BY_ID[rid]


def _is_heading(r):
    return r["content_type"].startswith("HEADING")


def _span_after(head_rid, stop_pred):
    """Rows strictly after head_rid up to the next row satisfying stop_pred."""
    out = []
    for r in ROWS[_SEQ[head_rid] + 1:]:
        if stop_pred(r):
            break
        out.append(r)
    return out


def _operation_span(op_rid):
    """Rows belonging to a Landskap Lembut operation (Siram / Baja / Racun).

    An operation ends at the next Heading-3 carrying list_level 2 (the next operation) or
    at the next Heading-2 (Landskap Kejur).
    """
    def stop(r):
        if r["content_type"] == "HEADING_2":
            return True
        return r["content_type"] == "HEADING_3" and r.get("list_level") == 2
    return _span_after(op_rid, stop)


def _descendant_headings(op_rid):
    return [r["row_id"] for r in _operation_span(op_rid) if _is_heading(r)]


def _body_rows_for(head_rid, universe):
    """Rows following head_rid inside `universe` up to the next heading."""
    ids = [r["row_id"] for r in universe]
    if head_rid not in ids:
        return []
    out = []
    for r in universe[ids.index(head_rid) + 1:]:
        if _is_heading(r):
            break
        out.append(r["row_id"])
    return out


OP_SIRAM, OP_BAJA, OP_RACUN = "T04-ROW-006", "T04-ROW-026", "T04-ROW-046"
LEMBUT_MAIN, KEJUR_MAIN = "T04-ROW-004", "T04-ROW-079"
KEJUR_GROUPS = ["T04-ROW-081", "T04-ROW-086", "T04-ROW-091", "T04-ROW-096"]

SIRAM_DESCENDANTS = _descendant_headings(OP_SIRAM)
BAJA_DESCENDANTS = _descendant_headings(OP_BAJA)
RACUN_DESCENDANTS = _descendant_headings(OP_RACUN)

PROCESS_NODES = list(SRC.ASSETS[0]["source_subject_nodes"])
SMARTART_ASSET_ID = SRC.ASSETS[0]["asset_id"]

# Editorial layer: proposed class, learner-facing subject and purpose. Every subject is a
# restatement of the row's own source text. Nothing here is a Bariah instruction.
_NODE_EDIT = [
    ("PROCEDURAL_ILLUSTRATION",
     "A supervisor briefing and demonstrating a maintenance task to a work crew on site",
     "Show that the first activity is instruction and demonstration, not the work itself."),
    ("EQUIPMENT_OR_ACTIVITY_VISUAL",
     "A supervisor observing and checking garden maintenance work in progress",
     "Distinguish supervision of maintenance from performing maintenance."),
    ("EQUIPMENT_OR_ACTIVITY_VISUAL",
     "Nursery operations — seedling beds, potting and plant holding areas under supervision",
     "Make the nursery visible as a distinct place of work, not an abstraction."),
    ("EQUIPMENT_OR_ACTIVITY_VISUAL",
     "Maintenance tools and machinery being checked and accounted for",
     "Anchor tool and machine supervision to physical objects the learner recognises."),
    ("EQUIPMENT_OR_ACTIVITY_VISUAL",
     "Garden inventory being recorded — stock, plants and materials counted against a list",
     "Show inventory supervision as a recording activity with an artefact."),
    ("CONCEPTUAL_DIAGRAM",
     "Workforce planning and worker welfare — shift or duty allocation and welfare provision",
     "Give the least concrete of the six steps something the learner can picture."),
]

# keyed by row_id -> (visual_class, learner_facing_subject, visual_purpose, unresolved_issue)
_EDIT = {
    # --- Landskap Lembut, main explanation -------------------------------------------------
    "T04-ROW-004": ("CONCEPTUAL_DIAGRAM",
        "The living elements the source names as soft landscape — trees, palms, shrubs and "
        "ground cover shown together as one category",
        "Establish the category before its three maintenance operations are taught.", None),
    # --- Siram -----------------------------------------------------------------------------
    "T04-ROW-006": ("EQUIPMENT_OR_ACTIVITY_VISUAL",
        "Watering in progress, supplying water to plants at the root zone",
        "Give the operation a concrete image before its methods are broken down.", None),
    "T04-ROW-008": ("COMPARISON_VISUAL",
        "The two implementation routes the source names — manual watering beside automatic "
        "irrigation",
        "Frame the methods as a choice before either is described.", None),
    "T04-ROW-009": ("EQUIPMENT_OR_ACTIVITY_VISUAL",
        "A rubber hose with a spray nozzle in use",
        "Show the equipment the source names for manual watering.", None),
    "T04-ROW-011": ("COMPARISON_VISUAL",
        "Sprinkler system beside drip irrigation — broad turf coverage against emitters at "
        "individual root zones",
        "Carry the distinction the source draws between the two automatic systems.",
        "The two systems are LIST_ITEM rows (T04-ROW-012 and T04-ROW-014), not headings. "
        "They are bound to this obligation rather than given obligations of their own."),
    "T04-ROW-016": ("PENDING_HUMAN",
        "PENDING — this heading groups four unrelated management topics and has no subject "
        "of its own in the source",
        "PENDING — whether a grouping heading earns its own visual is Bariah's call.",
        "Grouping heading with no body text. A visual here would have to be invented."),
    "T04-ROW-017": ("CONCEPTUAL_DIAGRAM",
        "A watering schedule showing early-morning and late-afternoon slots, with midday "
        "excluded",
        "Make the timing rule the source gives readable at a glance.", None),
    "T04-ROW-020": ("CONCEPTUAL_DIAGRAM",
        "Water supply and pressure across a site — source, delivery and the pump and timer "
        "the contractor maintains",
        "Show that water management is a site-wide system, not a tap.", None),
    "T04-ROW-022": ("COMPARISON_VISUAL",
        "The signs the source names — wilted dry leaves for under-watering against yellowed "
        "leaves and root rot for over-watering",
        "Both failure directions must be distinguishable, which is what the source teaches.",
        None),
    "T04-ROW-024": ("CONCEPTUAL_DIAGRAM",
        "Water cost against watering method on a large project",
        "Attach the cost point to something measurable.", None),
    # --- Baja ------------------------------------------------------------------------------
    "T04-ROW-026": ("EQUIPMENT_OR_ACTIVITY_VISUAL",
        "Fertiliser being applied to supply nutrients to plants",
        "Give the operation a concrete image before its methods are broken down.", None),
    "T04-ROW-028": ("COMPARISON_VISUAL",
        "The three application methods the source names, side by side",
        "Frame the methods as a set before each is described.", None),
    "T04-ROW-029": ("PROCEDURAL_ILLUSTRATION",
        "Granular fertiliser spread evenly around the root zone or across turf",
        "Show the spreading action that defines broadcasting.", None),
    "T04-ROW-031": ("PROCEDURAL_ILLUSTRATION",
        "Small holes dug around a tree's root zone, fertiliser placed in and covered back",
        "Show the three-step action the source describes.", None),
    "T04-ROW-033": ("PROCEDURAL_ILLUSTRATION",
        "Liquid fertiliser sprayed directly onto foliage",
        "Distinguish leaf application from soil application.", None),
    "T04-ROW-035": ("PENDING_HUMAN",
        "PENDING — grouping heading with no subject of its own",
        "PENDING — Bariah's call.",
        "Grouping heading with no body text."),
    "T04-ROW-036": ("CONCEPTUAL_DIAGRAM",
        "A fertilising programme sheet showing fertiliser type, NPK rate, quantity and "
        "schedule",
        "Show the programme as a document with named fields, as the source describes it.",
        None),
    "T04-ROW-038": ("SAFETY_OR_COMPLIANCE_VISUAL",
        "Fertiliser checked against the contract specification and the S.O.'s approval",
        "Make the approval step visible as a gate, not a formality.", None),
    "T04-ROW-040": ("SAFETY_OR_COMPLIANCE_VISUAL",
        "Fertiliser stored dry, secured and away from any water source",
        "The three storage conditions the source names must be readable in one image.", None),
    "T04-ROW-042": ("SAFETY_OR_COMPLIANCE_VISUAL",
        "A worker handling chemical fertiliser wearing gloves and a face mask",
        "Show the PPE the source names for this specific task.", None),
    "T04-ROW-044": ("CONCEPTUAL_DIAGRAM",
        "A fertilising record showing date, fertiliser type, quantity and area treated",
        "Show the record as evidence for a payment claim, which is the reason the source "
        "gives.", None),
    # --- Racun -----------------------------------------------------------------------------
    "T04-ROW-046": ("CONCEPTUAL_DIAGRAM",
        "The three threats the source names — insect pests, fungal disease and weeds",
        "Establish that pest control covers three different problems, not one.", None),
    "T04-ROW-048": ("CONCEPTUAL_DIAGRAM",
        "The IPM priority order — cultural, physical and biological control ahead of chemical",
        "The ORDER is the teaching point; a flat list would lose it.", None),
    "T04-ROW-049": ("PROCEDURAL_ILLUSTRATION",
        "Good maintenance practice as prevention — correct watering and balanced fertilising",
        "Connect cultural control back to the two operations already taught.", None),
    "T04-ROW-051": ("PROCEDURAL_ILLUSTRATION",
        "Diseased plant material removed by hand and weeds pulled out",
        "Show physical control as manual work.", None),
    "T04-ROW-053": ("CONCEPTUAL_DIAGRAM",
        "A pest's natural enemy used against it",
        "Biological control has no obvious image; a relationship diagram carries it.", None),
    "T04-ROW-055": ("PROCEDURAL_ILLUSTRATION",
        "Controlled, targeted pesticide application rather than blanket spraying",
        "The words the source stresses are 'terkawal' and 'bersasar'.", None),
    "T04-ROW-057": ("COMPARISON_VISUAL",
        "The three pesticide types the source names, side by side with their targets",
        "Type and target must be paired, which is exactly what the three rows state.", None),
    "T04-ROW-058": ("EQUIPMENT_OR_ACTIVITY_VISUAL",
        "Insecticide and the insect pests it controls",
        "Bind the type to its target.", None),
    "T04-ROW-060": ("EQUIPMENT_OR_ACTIVITY_VISUAL",
        "Fungicide and the fungal disease it controls",
        "Bind the type to its target.", None),
    "T04-ROW-062": ("EQUIPMENT_OR_ACTIVITY_VISUAL",
        "Herbicide and the weed growth it controls",
        "Bind the type to its target.", None),
    "T04-ROW-064": ("PENDING_HUMAN",
        "PENDING — grouping heading with no subject of its own",
        "PENDING — Bariah's call.",
        "Grouping heading with no body text."),
    "T04-ROW-065": ("SAFETY_OR_COMPLIANCE_VISUAL",
        "Pesticide use under statutory control, and a licensed operator's credential",
        "This is the unit's highest-consequence content and carries D-04.",
        "D-04 — the base/reveal split for this row group is not confirmed."),
    "T04-ROW-068": ("SAFETY_OR_COMPLIANCE_VISUAL",
        "Full PPE for pesticide work — respirator, safety goggles, chemical gloves and "
        "protective suit; locked labelled ventilated store; Safety Data Sheet on file",
        "The three HSE obligations the source groups here must all be visible.",
        "D-04 — the base/reveal split for this row group is not confirmed."),
    "T04-ROW-075": ("SAFETY_OR_COMPLIANCE_VISUAL",
        "Calm-weather spraying with no drift, warning signage posted, and a spray record",
        "Risk management is three separate obligations, not one.",
        "D-04 — the base/reveal split for this row group is not confirmed."),
    # --- Landskap Kejur --------------------------------------------------------------------
    "T04-ROW-079": ("CONCEPTUAL_DIAGRAM",
        "The permanent built elements the source names as hard landscape, shown as one "
        "category against the soft-landscape category",
        "Establish the second half of the unit and its contrast with the first.", None),
    "T04-ROW-081": ("CONCEPTUAL_DIAGRAM",
        "Walls, fences and level changes dividing outdoor space into distinct areas, with "
        "pathways, driveways and steps as movement routes",
        "Space-making and circulation are one function group in the source.", None),
    "T04-ROW-086": ("CONCEPTUAL_DIAGRAM",
        "A retaining wall holding a slope, with drains and graded surfaces carrying run-off",
        "Both engineering roles the source names belong in one image.", None),
    "T04-ROW-091": ("EQUIPMENT_OR_ACTIVITY_VISUAL",
        "Patios, decks and plazas in use, with gazebos, benches and landscape lighting",
        "Usability is shown by people using the space, which the source implies.", None),
    "T04-ROW-096": ("COMPARISON_VISUAL",
        "Stone, timber and concrete adding texture, colour and pattern, and the contrast "
        "hard elements make against planting",
        "The source's own point is contrast, which needs two things in one frame.", None),
}


def _mk(vo_id, locator, rows, raw_heading, gov_heading, group, parent, edit,
        existing=NO_SOURCE_IMAGE, asset_id=None, extra_rows=()):
    cls, subject, purpose, unresolved = edit
    if cls not in ALLOWED_VISUAL_CLASSES:
        raise RuntimeError(f"{vo_id}: visual class not in the allowed vocabulary: {cls}")
    all_rows = list(rows) + list(extra_rows)
    for rid in all_rows:
        _row(rid)
    return dict(
        visual_obligation_id=vo_id,
        bariah_ruling_locator=locator,
        source_row_ids=all_rows,
        raw_source_heading=raw_heading,
        governed_display_heading=gov_heading,
        learner_facing_subject=subject,
        visual_purpose=purpose,
        proposed_visual_class=cls,
        existing_source_asset_available=existing,
        source_asset_id=asset_id,
        production_requirement=NEW_ASSET,
        source_authority=SOURCE_AUTHORITY,
        treatment_authority=TREATMENT_AUTHORITY,
        subject_authority=SUBJECT_AUTHORITY,
        mmd_dependency="MMD_ASSET_PRODUCTION_NOT_STARTED",
        approval_status=APPROVAL_STATUS,
        unresolved_issue=unresolved,
        population_group=group,
        parent_topic=parent)


def _gov(raw):
    """Governed display heading: repair the source's H1 typo and drop a trailing colon."""
    if raw == "PENJAAGAAN DAN PENYELENGGARAAN":
        return "PENJAGAAN DAN PENYELENGGARAAN"
    return raw.rstrip(":").strip()


def _build_obligations():
    out, n = [], 0

    def nxt():
        nonlocal n
        n += 1
        return f"T04-VO-{n:03d}"

    # A — one obligation per source process node, in source order. No seventh step.
    for i, label in enumerate(PROCESS_NODES):
        cls, subject, purpose = _NODE_EDIT[i]
        out.append(_mk(nxt(), "BR-L1", ["T04-ROW-003"], label, label,
                       "A_PROCESS_NODES", "PENJAGAAN DAN PENYELENGGARAAN",
                       (cls, subject, purpose, None),
                       existing=SMARTART_LABEL_ONLY, asset_id=SMARTART_ASSET_ID))

    # B — Landskap Lembut
    r = _row(LEMBUT_MAIN)
    out.append(_mk(nxt(), "BR-L2", [LEMBUT_MAIN, "T04-ROW-005"], r["raw_source_text"],
                   _gov(r["raw_source_text"]), "B_LEMBUT_MAIN", "Landskap Lembut",
                   _EDIT[LEMBUT_MAIN]))

    for op, descendants in ((OP_SIRAM, SIRAM_DESCENDANTS), (OP_BAJA, BAJA_DESCENDANTS),
                            (OP_RACUN, RACUN_DESCENDANTS)):
        opr = _row(op)
        span = _operation_span(op)
        out.append(_mk(nxt(), "BR-L3", [op] + _body_rows_for(op, [opr] + span),
                       opr["raw_source_text"], _gov(opr["raw_source_text"]),
                       "B_OPERATION_MAIN", opr["raw_source_text"], _EDIT[op]))
        for d in descendants:
            dr = _row(d)
            out.append(_mk(nxt(), "BR-L4", [d] + _body_rows_for(d, span),
                           dr["raw_source_text"], _gov(dr["raw_source_text"]),
                           "B_OPERATION_DESCENDANT", opr["raw_source_text"], _EDIT[d]))

    # C — Landskap Kejur: the main explanation and exactly the four groups Bariah named.
    kr = _row(KEJUR_MAIN)
    out.append(_mk(nxt(), "BR-L5", [KEJUR_MAIN, "T04-ROW-080"], kr["raw_source_text"],
                   _gov(kr["raw_source_text"]), "C_KEJUR_MAIN", "Landskap Kejur",
                   _EDIT[KEJUR_MAIN]))
    kejur_span = _span_after(KEJUR_MAIN, lambda r: False)
    for g in KEJUR_GROUPS:
        gr = _row(g)
        sub = _body_rows_for(g, kejur_span)
        # the group's own two sub-headings and their body, bound for traceability only
        idx = [x["row_id"] for x in kejur_span].index(g)
        tail = []
        for x in kejur_span[idx + 1:]:
            if x["row_id"] in KEJUR_GROUPS:
                break
            tail.append(x["row_id"])
        out.append(_mk(nxt(), "BR-L6", [g] + tail, gr["raw_source_text"],
                       _gov(gr["raw_source_text"]), "C_KEJUR_GROUP", "Landskap Kejur",
                       _EDIT[g]))
        del sub
    return out


VISUAL_OBLIGATIONS = _build_obligations()

VISUAL_OBLIGATION_FIELDS = [
    "visual_obligation_id", "bariah_ruling_locator", "source_row_ids", "raw_source_heading",
    "governed_display_heading", "learner_facing_subject", "visual_purpose",
    "proposed_visual_class", "existing_source_asset_available", "source_asset_id",
    "production_requirement", "source_authority", "treatment_authority", "subject_authority",
    "mmd_dependency", "approval_status", "unresolved_issue",
]

VOCABULARY_NOTE = (
    "SOURCE_SMARTART and PROCESS_DIAGRAM are in the allowed class list but are not used as a "
    "per-obligation proposal. They describe the EXISTING aggregate diagram T04-DGM-01, whose "
    "treatment is governed by D-05, not by any single step obligation. Bariah's BR-L1 asks "
    "for a visual per step, which is a different asset from the diagram that contains the "
    "steps.")

VISUAL_TOTALS = dict(
    total_obligations=len(VISUAL_OBLIGATIONS),
    process_nodes=len([v for v in VISUAL_OBLIGATIONS if v["population_group"] == "A_PROCESS_NODES"]),
    lembut_main=len([v for v in VISUAL_OBLIGATIONS if v["population_group"] == "B_LEMBUT_MAIN"]),
    operation_mains=len([v for v in VISUAL_OBLIGATIONS if v["population_group"] == "B_OPERATION_MAIN"]),
    operation_descendants=len([v for v in VISUAL_OBLIGATIONS if v["population_group"] == "B_OPERATION_DESCENDANT"]),
    kejur_main=len([v for v in VISUAL_OBLIGATIONS if v["population_group"] == "C_KEJUR_MAIN"]),
    kejur_groups=len([v for v in VISUAL_OBLIGATIONS if v["population_group"] == "C_KEJUR_GROUP"]),
    siram_descendants=len(SIRAM_DESCENDANTS),
    baja_descendants=len(BAJA_DESCENDANTS),
    racun_descendants=len(RACUN_DESCENDANTS),
    pending_human=len([v for v in VISUAL_OBLIGATIONS if v["proposed_visual_class"] == "PENDING_HUMAN"]),
    new_assets_required=len([v for v in VISUAL_OBLIGATIONS if v["production_requirement"] == NEW_ASSET]),
    existing_raster_source_images=0,
    existing_source_assets=len(SRC.ASSETS))

# ==========================================================================================
# PART 4 — SOURCE-TO-SCREEN MAPPING v2
# ==========================================================================================
_BY_ROW = {}
for _v in VISUAL_OBLIGATIONS:
    for _r in _v["source_row_ids"]:
        _BY_ROW.setdefault(_r, []).append(_v["visual_obligation_id"])


def _vo_for(*row_ids):
    seen, out = set(), []
    for rid in row_ids:
        for vid in _BY_ROW.get(rid, []):
            if vid not in seen:
                seen.add(vid)
                out.append(vid)
    return out


SC01_VO = [v["visual_obligation_id"] for v in VISUAL_OBLIGATIONS
           if v["population_group"] == "A_PROCESS_NODES"]
SC02_VO = [v["visual_obligation_id"] for v in VISUAL_OBLIGATIONS
           if v["population_group"] in ("B_LEMBUT_MAIN", "B_OPERATION_MAIN")]
SC03_VO = [v["visual_obligation_id"] for v in VISUAL_OBLIGATIONS
           if v["raw_source_heading"] in ("Perundangan dan Pelesenan",
                                          "Keselamatan dan Kesihatan (HSE)",
                                          "Pengurusan Risiko")]
SC05_VO = [v["visual_obligation_id"] for v in VISUAL_OBLIGATIONS
           if v["population_group"] in ("C_KEJUR_MAIN", "C_KEJUR_GROUP")]

_MAPPED = set(SC01_VO) | set(SC02_VO) | set(SC03_VO) | set(SC05_VO)
UNMAPPED_VO = [v["visual_obligation_id"] for v in VISUAL_OBLIGATIONS
               if v["visual_obligation_id"] not in _MAPPED]

MAPPING_V2 = [
    dict(screen_candidate_id="T04-SC-01",
         working_title="Aliran proses penjagaan dan penyelenggaraan",
         previous_visual_assumption="One source-bound diagram carried the whole screen. "
                                    "T04-DGM-01 was described as 'the unit's only visual'.",
         new_bariah_visual_obligation="BR-L1 — a visual for EVERY one of the six steps, in "
                                      "addition to the diagram.",
         visual_obligation_ids=SC01_VO,
         required_visual_states=6,
         available_source_visual="T04-DGM-01 — a vector SmartArt carrying the six node "
                                 "LABELS. It is not six step illustrations.",
         missing_production_asset="6 × NEW_MMD_ASSET_REQUIRED",
         possible_screen_expansion="1 overview screen plus up to 6 step screens, or 1 screen "
                                   "with a 6-state stepper. Not decided.",
         popup_reveal_implications="If the six live on one screen, each step visual becomes a "
                                   "state. Nothing mandatory is hidden — the six labels stay "
                                   "in the base state.",
         learner_screen_count_impact="+0 to +6",
         runtime_state_count_impact="+6 minimum",
         decision_still_required="D-05 — diagram treatment and node preservation"),
    dict(screen_candidate_id="T04-SC-02",
         working_title="Landskap Lembut — tiga operasi penyelenggaraan",
         previous_visual_assumption="NONE — 'no source visual exists for any of the three'. "
                                    "The screen was text-led with three reveals.",
         new_bariah_visual_obligation="BR-L2 and BR-L3 — the section main explanation and "
                                      "each of Siram, Baja and Racun require a visual.",
         visual_obligation_ids=SC02_VO,
         required_visual_states=4,
         available_source_visual="NONE",
         missing_production_asset="4 × NEW_MMD_ASSET_REQUIRED",
         possible_screen_expansion="The three-reveal screen still works, but each reveal now "
                                   "carries a visual as well as a definition. A split into "
                                   "three screens becomes more attractive.",
         popup_reveal_implications="Reveal content grows from one line to line-plus-image. "
                                   "The hidden material stays SUPPLEMENTARY.",
         learner_screen_count_impact="+0 to +3",
         runtime_state_count_impact="+4",
         decision_still_required="visual subject and style approval"),
    dict(screen_candidate_id="T04-SC-03",
         working_title="Racun — perundangan, HSE dan pengurusan risiko",
         previous_visual_assumption="NONE. Eleven compliance rows, text only, all visible in "
                                    "the base state.",
         new_bariah_visual_obligation="BR-L4 — the three Aspek Pengurusan headings under "
                                      "Racun are source subtopics and each requires a visual.",
         visual_obligation_ids=SC03_VO,
         required_visual_states=3,
         available_source_visual="NONE",
         missing_production_asset="3 × NEW_MMD_ASSET_REQUIRED (safety and compliance)",
         possible_screen_expansion="Three obligation blocks, each now with a visual — this "
                                   "screen is the most likely to split.",
         popup_reveal_implications="D-04 governs this screen. No obligation may end up behind "
                                   "an optional reveal, and adding visuals must not become a "
                                   "reason to move text into a popup.",
         learner_screen_count_impact="+0 to +2",
         runtime_state_count_impact="+3",
         decision_still_required="D-04 — precise base/reveal split"),
    dict(screen_candidate_id="T04-SC-04",
         working_title="Landskap Lembut berbanding Landskap Kejur",
         previous_visual_assumption="NONE. A text comparison; candidate for deletion.",
         new_bariah_visual_obligation="No obligation of its own. It reuses the two section "
                                      "main-explanation visuals required by BR-L2 and BR-L5.",
         visual_obligation_ids=[],
         required_visual_states=0,
         available_source_visual="NONE",
         missing_production_asset="none beyond the two section visuals already counted",
         possible_screen_expansion="none",
         popup_reveal_implications="none",
         learner_screen_count_impact="0",
         runtime_state_count_impact="0",
         decision_still_required="whether this screen is wanted at all — unchanged from v1"),
    dict(screen_candidate_id="T04-SC-05",
         working_title="Landskap Kejur — empat kumpulan fungsi",
         previous_visual_assumption="NONE. Four reveals, text only.",
         new_bariah_visual_obligation="BR-L5 and BR-L6 — the section main explanation and "
                                      "each of the four named groups require a visual.",
         visual_obligation_ids=SC05_VO,
         required_visual_states=5,
         available_source_visual="NONE",
         missing_production_asset="5 × NEW_MMD_ASSET_REQUIRED",
         possible_screen_expansion="+0 to +4",
         popup_reveal_implications="Same shape as T04-SC-02 — reveals now carry images.",
         learner_screen_count_impact="+0 to +4",
         runtime_state_count_impact="+5",
         decision_still_required="visual subject and style approval; and whether the eight "
                                 "Kejur sub-items are in scope — see SCOPE_ASYMMETRY"),
    dict(screen_candidate_id="T04-SC-06",
         working_title="Rumusan dan kuiz",
         previous_visual_assumption="NONE. Treatment PENDING_HUMAN, structure unresolved.",
         new_bariah_visual_obligation="None — Bariah's visual ruling does not reach the "
                                      "Rumusan or the quiz.",
         visual_obligation_ids=[],
         required_visual_states=0,
         available_source_visual="NONE",
         missing_production_asset="none",
         possible_screen_expansion="Composition is now fixed at 4 MCQ + 1 MR, so the quiz "
                                   "block has a known shape for the first time.",
         popup_reveal_implications="none",
         learner_screen_count_impact="0",
         runtime_state_count_impact="quiz states now bounded by 5 items",
         decision_still_required="D-02B pass threshold; Rumusan approval; quiz authoring"),
]

MAPPING_IMPACT = dict(
    final_screen_count=FINAL_SCREEN_COUNT,
    reason="Bariah's ruling multiplies the visual load without settling how the visuals are "
           "distributed across screens. Until that is decided, any number would be invented.",
    derived_from_b02=False,
    b02_families_propagated=0,
    b02_family_note="B02's Family S / P1 / P2 overview structure is NOT applied to T04. That "
                    "structure exists to organise 14 extracted source photographs into "
                    "overview cardinalities. T04 has zero raster source images, so there is "
                    "nothing for it to organise, and forcing it would invent a grouping the "
                    "source does not have.",
    obligations_total=len(VISUAL_OBLIGATIONS),
    obligations_mapped_to_existing_candidates=len(_MAPPED),
    obligations_with_no_home=len(UNMAPPED_VO),
    unmapped_obligation_ids=UNMAPPED_VO,
    headline="The six-candidate map from Stage 4.2F-B0.5 cannot hold Bariah's ruling. "
             f"{len(_MAPPED)} of {len(VISUAL_OBLIGATIONS)} obligations land on an existing "
             f"candidate; {len(UNMAPPED_VO)} have no screen at all. Those "
             f"{len(UNMAPPED_VO)} are the Siram, Baja and Racun subtopics, which the v1 map "
             "never surfaced because it treated the three operations as three reveals on one "
             "screen. T04 is now substantially more visual-intensive than the v1 proposal "
             "assumed, and the map must expand before a screen count means anything.",
    prior_visual_count_claim="T04 has 1 visual against B02's 14 — the Stage 4.2F-B0.5 "
                             "portability prediction",
    revised_visual_count_claim=f"T04 has 1 SOURCE visual and "
                               f"{len(VISUAL_OBLIGATIONS)} REQUIRED visuals. The portability "
                               "prediction inverts: visual-treatment reuse is not merely low, "
                               "it is the largest single production item in the unit.")

# ==========================================================================================
# PART 5 — RUMUSAN v2
# ==========================================================================================
# Style characteristics extracted from the APPROVED Topik 3 Bahagian 2 Rumusan treatment.
# Style only. No B02 fact appears in any T04 statement.
RUMUSAN_STYLE_RULES = [
    dict(rule_id="SR-01", characteristic="heading",
         observed="One heading line naming the topic and its two structural halves, joined "
                  "by an em dash.",
         applied_as="Penjagaan dan Penyelenggaraan — Landskap Lembut dan Landskap Kejur"),
    dict(rule_id="SR-02", characteristic="number of recap points",
         observed="Exactly four.",
         applied_as="Four. Stage 4.2F-B0.5 drafted five; the consolidation is shown in full "
                    "in RUMUSAN_V1_TO_V2 so nothing is dropped silently."),
    dict(rule_id="SR-03", characteristic="sentence pattern",
         observed="'<Label> - <expansion>' with a spaced hyphen, not a colon. One clause per "
                  "point.",
         applied_as="Same pattern in all four points."),
    dict(rule_id="SR-04", characteristic="opening point",
         observed="A capability statement joined to its consequence — 'Mengenal pasti … - … "
                  "dirancang dengan tepat'.",
         applied_as="PARTIALLY. T04's opening point enumerates the six process activities "
                    "instead, because the module opens on that flow and Bariah requires a "
                    "visual for each step. Recorded as a deliberate adaptation, not an "
                    "oversight."),
    dict(rule_id="SR-05", characteristic="middle points",
         observed="The two structural groups, each enumerating its named members.",
         applied_as="Landskap Lembut with its three operations; Landskap Kejur with its four "
                    "function groups."),
    dict(rule_id="SR-06", characteristic="closing point",
         observed="A contractor-outcome statement opening 'Kontraktor dapat …'.",
         applied_as="Same opener. This is also where the medium-risk generalisation sits."),
    dict(rule_id="SR-07", characteristic="terminology treatment",
         observed="English technical terms kept in English and given emphasis; Malay terms "
                  "left in Malay.",
         applied_as="T04's technical terms are Malay throughout, so no term needed the "
                    "English treatment. The rule is recorded as applicable-but-unused rather "
                    "than dropped."),
    dict(rule_id="SR-08", characteristic="punctuation treatment",
         observed="No terminal full stop on any bullet.",
         applied_as="Same."),
    dict(rule_id="SR-09", characteristic="tone",
         observed="Impersonal and declarative. No direct address to the learner in the "
                  "Rumusan bullets.",
         applied_as="Same. 'Anda' does not appear."),
    dict(rule_id="SR-10", characteristic="length",
         observed="Single clauses, roughly 12 to 28 words each.",
         applied_as="Same range."),
]

RUMUSAN_STYLE_SOURCE = dict(
    unit="K5 PL06 T03 B02 — Komponen Landskap",
    artifact="reviews/source-completion/generator/b02_content_v0_3.py, FRAMES['rumusan']",
    authority="APPROVED_B02_TREATMENT — style reference only",
    prohibition="No B02 fact, component name, group name or example may appear in the T04 "
                "Rumusan. Style was instructed; content was not.")

RUMUSAN_V2 = dict(
    content_status=CONTENT_STATUS,
    instructional_authority=INSTRUCTIONAL_AUTHORITY,
    approval_status=APPROVAL_STATUS,
    heading="Penjagaan dan Penyelenggaraan — Landskap Lembut dan Landskap Kejur",
    provenance="Every statement compresses rows already in the controlled T04 extract. The "
               "module contains no Rumusan — zero hits across all 6,167 body paragraphs — so "
               "this is drafted, not extracted. Bariah authorised the drafting (BR-W1) and "
               "instructed the style (BR-W3). She has not seen the text.",
    statements=[
        dict(statement_id="T04-RUM2-01",
             draft_text="Aliran proses penjagaan dan penyelenggaraan merangkumi enam aktiviti "
                        "penyeliaan - koordinasi dan demonstrasi, penyelenggaraan taman, "
                        "operasi nurseri, alatan dan mesin, inventori taman, serta sumber "
                        "manusia dan kebajikan pekerja",
             source_row_ids=["T04-ROW-002", "T04-ROW-003"],
             source_heading="PENJAGAAN DAN PENYELENGGARAAN",
             style_rule_applied=["SR-03", "SR-05", "SR-08", "SR-09", "SR-10"],
             style_deviation="SR-04 not applied — see the rule's applied_as note.",
             factual_risk_status="LOW — the six activities and their order are measured from "
                                 "T04-DGM-01",
             bariah_review=dict(decision=None, edit=None, comment=None)),
        dict(statement_id="T04-RUM2-02",
             draft_text="Landskap Lembut - elemen hortikultur dan hidupan yang diselenggara "
                        "melalui tiga operasi utama, iaitu siram, baja dan racun",
             source_row_ids=["T04-ROW-005", OP_SIRAM, OP_BAJA, OP_RACUN],
             source_heading="Landskap Lembut",
             style_rule_applied=["SR-03", "SR-05", "SR-08", "SR-09", "SR-10"],
             style_deviation=None,
             factual_risk_status="LOW",
             bariah_review=dict(decision=None, edit=None, comment=None)),
        dict(statement_id="T04-RUM2-03",
             draft_text="Landskap Kejur - elemen binaan kekal yang menyumbang kepada "
                        "pengurusan ruang dan sirkulasi, fungsi struktur dan kejuruteraan, "
                        "kebolehgunaan dan kemudahan, serta estetika dan reka bentuk",
             source_row_ids=["T04-ROW-080"] + KEJUR_GROUPS,
             source_heading="Landskap Kejur",
             style_rule_applied=["SR-03", "SR-05", "SR-08", "SR-09", "SR-10"],
             style_deviation=None,
             factual_risk_status="LOW",
             bariah_review=dict(decision=None, edit=None, comment=None)),
        dict(statement_id="T04-RUM2-04",
             draft_text="Kontraktor dapat merancang, melaksana dan mendokumentasikan setiap "
                        "operasi mengikut spesifikasi, dengan penggunaan racun tertakluk "
                        "kepada perundangan, pengendali berlesen, PPE lengkap dan "
                        "penyimpanan berkunci",
             source_row_ids=["T04-ROW-016", "T04-ROW-035", "T04-ROW-064", "T04-ROW-066",
                             "T04-ROW-067", "T04-ROW-069", "T04-ROW-071"],
             source_heading="Aspek Pengurusan untuk Kontraktor",
             style_rule_applied=["SR-06", "SR-08", "SR-09", "SR-10"],
             style_deviation=None,
             factual_risk_status="MEDIUM — the contractor-responsibility pattern is repeated "
                                 "under all three operations but the source never states it "
                                 "as a general rule. This is the same generalisation flagged "
                                 "at Stage 4.2F-B0.5 as T04-RUM-03, preserved deliberately "
                                 "so Bariah can narrow or cut it rather than discover it "
                                 "later. Note that the approved B02 Rumusan ends on the same "
                                 "'Kontraktor dapat …' shape, so the style rule invites the "
                                 "generalisation — that does not make the source support it.",
             bariah_review=dict(decision=None, edit=None, comment=None)),
    ],
    review_table_columns=["accept", "edit", "remove", "comment"],
    medium_risk_statement_id="T04-RUM2-04")

RUMUSAN_V1_TO_V2 = [
    dict(v1="T04-RUM-01", v1_topic="six supervisory activities", v2="T04-RUM2-01",
         change="Retained. v1 named only the first and last node to stay short; v2 names all "
                "six, because Bariah now requires a visual per step and the recap should not "
                "under-report the population."),
    dict(v1="T04-RUM-02", v1_topic="Landskap Lembut and its three operations",
         v2="T04-RUM2-02", change="Retained, reworded to the SR-03 pattern."),
    dict(v1="T04-RUM-03", v1_topic="contractor responsibility across operations",
         v2="T04-RUM2-04",
         change="MERGED with T04-RUM-04. The medium factual-risk flag travels with it."),
    dict(v1="T04-RUM-04", v1_topic="pesticide legal and safety obligations",
         v2="T04-RUM2-04",
         change="MERGED into the contractor-outcome point. Nothing was dropped: statute, "
                "licensed operator, PPE and locked storage are all still named. What changed "
                "is that they now sit inside the closing point instead of having one of "
                "their own — the cost of applying SR-02's four-point rule to a unit with "
                "five structural blocks."),
    dict(v1="T04-RUM-05", v1_topic="Landskap Kejur and its four function groups",
         v2="T04-RUM2-03", change="Retained, reworded to the SR-03 pattern."),
]

RUMUSAN_CONSOLIDATION_NOTE = (
    "Five statements became four because SR-02 — the Topik 3 Bahagian 2 four-point rule — is "
    "part of the writing style Bariah instructed. T04 has five structural blocks (process, "
    "soft landscape, hard landscape, compliance, contractor responsibility) against B02's "
    "four, so exactly one merge was unavoidable. Compliance was merged into the "
    "contractor-outcome point because compliance IS a contractor obligation and B02's own "
    "fourth point is the contractor-outcome point. If Bariah prefers compliance to stand "
    "alone, the fix is a five-point Rumusan, which departs from SR-02 — that trade is hers "
    "to make, not ours.")

# ==========================================================================================
# PART 6 — QUIZ BLUEPRINT v2
# ==========================================================================================
QUIZ_V2 = dict(
    quiz_composition="CONFIRMED_BARIAH_DIRECT",
    composition_rule="4 MCQ + 1 MULTIPLE_RESPONSE",
    scope="ALL_PLS_IN_KURSUS",
    pass_threshold="UNRESOLVED",
    quiz_content="BLUEPRINT_ONLY",
    final_instructional_authority="BARIAH",
    approval_status=APPROVAL_STATUS,
    mcq_count=4,
    mr_count=1,
    not_produced=["final stems", "final answer options", "final answer key", "final rationale",
                  "approved feedback", "a pass mark"],
    threshold_note="The 60 percent figure in A3 is the B02 slice of the Style and Guidelines. "
                   "Bariah's message settles composition and is silent on the threshold, so "
                   "it stays UNRESOLVED. It is not carried forward as a default.",
    slots=[
        dict(slot="Q1", item_type="MCQ", from_blueprint=["T04-QB-01"],
             source_learning_point="The three soft-landscape maintenance operations",
             source_row_ids=[OP_SIRAM, OP_BAJA, OP_RACUN],
             cognitive_demand="RECALL",
             misconception_to_assess="that soft-landscape maintenance is only watering",
             correct_answer_evidence="Three named Heading-3 operations sit under Landskap "
                                     "Lembut: Siram, Baja, Racun.",
             visual_dependency="T04-VO-008, T04-VO-017, T04-VO-028 — if the learner met each "
                               "operation through a visual, the item may key on it",
             why_this_type="MCQ once Q5 takes the multiple-response slot; asking for one "
                           "operation out of three is a clean one-best-answer form.",
             content_overlap="Feeds Q2 — Q2 assumes Siram is known.",
             bariah_decision_required="whether recall of the three names is worth a whole slot"),
        dict(slot="Q2", item_type="MCQ", from_blueprint=["T04-QB-02"],
             source_learning_point="Irrigation method selection",
             source_row_ids=["T04-ROW-012", "T04-ROW-013", "T04-ROW-014", "T04-ROW-015"],
             cognitive_demand="APPLICATION",
             misconception_to_assess="that sprinkler and drip irrigation are interchangeable",
             correct_answer_evidence="The source states sprinkler suits large turf areas and "
                                     "drip suits individual trees and shrubs by delivering "
                                     "water to the root zone.",
             visual_dependency="T04-VO-011 — the sprinkler-versus-drip comparison visual. If "
                               "the item shows a scenario image, this is the asset.",
             why_this_type="MCQ — the source gives a clear one-best-answer distinction.",
             content_overlap="Depends on Q1's operation set.",
             bariah_decision_required="whether an application-level item belongs in a "
                                      "five-item quiz"),
        dict(slot="Q3", item_type="MCQ", from_blueprint=["T04-QB-05"],
             source_learning_point="IPM control priority order",
             source_row_ids=["T04-ROW-048", "T04-ROW-049", "T04-ROW-051", "T04-ROW-053",
                             "T04-ROW-055"],
             cognitive_demand="UNDERSTANDING",
             misconception_to_assess="that chemical control is the first response to a pest "
                                     "problem",
             correct_answer_evidence="The source lists cultural, physical and biological "
                                     "control before chemical control.",
             visual_dependency="T04-VO-029 — the IPM priority-order diagram",
             why_this_type="MCQ — the answer is an ordering judgement with one best option.",
             content_overlap="Sits beside Q5; Q3 is about what comes BEFORE chemical use, Q5 "
                             "about the controls that apply WHEN chemicals are used.",
             bariah_decision_required="none anticipated"),
        dict(slot="Q4", item_type="MCQ", from_blueprint=["T04-QB-06"],
             source_learning_point="The four functions of hard landscape",
             source_row_ids=list(KEJUR_GROUPS),
             cognitive_demand="RECALL",
             misconception_to_assess="that hard landscape is decorative only",
             correct_answer_evidence="Four named function groups, one of which is explicitly "
                                     "structural and engineering.",
             visual_dependency="T04-VO-043 to T04-VO-046 — the four group visuals",
             why_this_type="MCQ — the multiple-response slot is spent on Q5, and asking for "
                           "the non-decorative function is a clean single-answer item.",
             content_overlap="none",
             bariah_decision_required="whether to key on the engineering function specifically"),
        dict(slot="Q5", item_type="MULTIPLE_RESPONSE",
             from_blueprint=["T04-QB-03", "T04-QB-04"],
             source_learning_point="Pesticide legal, licensing and HSE obligations — the "
                                   "CONSOLIDATION of the two compliance blueprint points",
             source_row_ids=["T04-ROW-066", "T04-ROW-067", "T04-ROW-069", "T04-ROW-071",
                             "T04-ROW-073", "T04-ROW-076"],
             cognitive_demand="RECALL",
             misconception_to_assess="that PPE alone, or a licence alone, is sufficient "
                                     "compliance",
             correct_answer_evidence="Six co-required controls in the source: statutory "
                                     "control, licensed operator, full PPE, locked labelled "
                                     "ventilated storage, SDS retention, and calm-weather "
                                     "spraying.",
             visual_dependency="T04-VO-039, T04-VO-040, T04-VO-041 — the three compliance "
                               "visuals",
             why_this_type="MR — the source presents these as controls that apply together, "
                           "not alternatives. Forcing them into MCQ would teach that one of "
                           "them is the answer.",
             content_overlap="Absorbs the whole compliance cluster; no other slot touches it.",
             bariah_decision_required="whether to name Akta Racun Makhluk Perosak 1974 in the "
                                      "stem, given that T04-CLM-01 is "
                                      "EXTERNAL_VERIFICATION_REQUIRED"),
    ],
    consolidation=dict(
        situation="Stage 4.2F-B0.5 produced six coverage points. Bariah's confirmed "
                  "composition allows exactly five slots.",
        rule="No coverage point is discarded. One consolidation is made and named.",
        merged=dict(into="Q5", from_points=["T04-QB-03", "T04-QB-04"],
                    justification="QB-03 (statute and licensing) and QB-04 (PPE, storage, "
                                  "SDS, spray conditions) are the same compliance cluster "
                                  "split by heading, not by concept. As one MR item they "
                                  "test what the source actually says — that these controls "
                                  "co-apply. As two items they would have consumed 40 "
                                  "percent of a five-item quiz on one topic.",
                    cost="The statute's NAME no longer has a stem of its own. If Bariah wants "
                         "the Act tested by name, it has to displace another slot."),
        unmerged=[dict(point="T04-QB-01", slot="Q1"), dict(point="T04-QB-02", slot="Q2"),
                  dict(point="T04-QB-05", slot="Q3"), dict(point="T04-QB-06", slot="Q4")],
        accounting="6 coverage points in, 5 slots out, 0 discarded."))

# ==========================================================================================
# PART 7 — D-04 LEGAL AND COMPLIANCE CLARIFICATION
# ==========================================================================================
def _txt(rid):
    return _row(rid)["raw_source_text"]


def _vis_for(rid):
    """The visual obligation covering this row, derived — never typed by hand.

    Hand-typed obligation ids were wrong in five of nineteen rows on the first pass, because
    the ids are assigned during inventory construction and cannot be predicted. Gate
    LEGAL_VISUAL_REFERENCES_RESOLVE holds this permanently.
    """
    ids = _BY_ROW.get(rid, [])
    if not ids:
        return "NONE — this row sits under no visual obligation"
    v = next(v for v in VISUAL_OBLIGATIONS if v["visual_obligation_id"] == ids[0])
    return f"{v['visual_obligation_id']} ({v['governed_display_heading']})"


def _leg(rid, base, reveal, why, mandatory):
    return dict(source_row_id=rid, source_wording=_txt(rid),
                proposed_base_screen_treatment=base,
                proposed_optional_reveal_treatment=reveal,
                mandatory_or_supplementary=mandatory, why=why,
                visual_requirement=_vis_for(rid),
                bariah_confirmation=dict(decision=None, comment=None))


_M = "MANDATORY"
_S = "SUPPLEMENTARY"

LEGAL_GROUPS = [
    dict(group_id="LG-1", group="Akta Racun Makhluk Perosak 1974", rows=[
        _leg("T04-ROW-065", "heading visible", "none", "Names the obligation group.", _M),
        _leg("T04-ROW-066", "visible verbatim in the base state", "none",
             "A statutory control. A learner who never interacts must still see it.", _M)]),
    dict(group_id="LG-2", group="Licensed operator requirement", rows=[
        _leg("T04-ROW-067", "visible verbatim in the base state", "none",
             "Determines who may legally perform the work.", _M)]),
    dict(group_id="LG-3", group="PPE", rows=[
        _leg("T04-ROW-068", "heading visible", "none", "Names the HSE obligation group.", _M),
        _leg("T04-ROW-069", "label visible in the base state", "none",
             "The requirement itself is mandatory.", _M),
        _leg("T04-ROW-070", "recommended visible", "acceptable as a reveal",
             "The ITEM LIST — respirator, goggles, chemical gloves, protective suit — is "
             "implementation detail expanding a label already on screen. This is the "
             "strongest candidate in the unit for Bariah's 'click to reveal jika diperlukan'.",
             _S),
        _leg("T04-ROW-043", "visible in the base state", "none",
             "PPE for chemical fertiliser handling — a different task, same class of "
             "obligation. Sits on the Baja screen, not the Racun screen.", _M)]),
    dict(group_id="LG-4", group="Safety Data Sheet (SDS)", rows=[
        _leg("T04-ROW-073", "label visible in the base state", "none",
             "A record-keeping duty stated as 'wajib' in the source.", _M),
        _leg("T04-ROW-074", "recommended visible", "acceptable as a reveal",
             "Explains what keeping the SDS means in practice.", _S)]),
    dict(group_id="LG-5", group="Locked or safe storage", rows=[
        _leg("T04-ROW-071", "label visible in the base state", "none",
             "Storage and disposal duty.", _M),
        _leg("T04-ROW-072", "recommended visible", "acceptable as a reveal",
             "The conditions — locked, labelled, ventilated, no reuse of empty containers — "
             "are the substance of the duty. Bariah may judge these too important to hide; "
             "marked SUPPLEMENTARY only because the duty itself is already stated.", _S),
        _leg("T04-ROW-041", "visible in the base state", "none",
             "Fertiliser storage — dry, secure and away from water sources. Sits on the Baja "
             "screen.", _M)]),
    dict(group_id="LG-6", group="Spraying conditions", rows=[
        _leg("T04-ROW-075", "heading visible", "none", "Names the risk-management group.", _M),
        _leg("T04-ROW-076", "visible verbatim in the base state", "none",
             "A hard operational limit — spraying only in calm weather, to prevent drift.",
             _M)]),
    dict(group_id="LG-7", group="Notification", rows=[
        _leg("T04-ROW-077", "visible verbatim in the base state", "none",
             "A duty owed to third parties: notify building management or residents and post "
             "warning signage.", _M)]),
    dict(group_id="LG-8", group="Reporting", rows=[
        _leg("T04-ROW-078", "visible verbatim in the base state", "none",
             "Record-keeping for every spraying activity, with named fields.", _M),
        _leg("T04-ROW-045", "visible in the base state", "none",
             "Fertiliser records as evidence for payment claims. Sits on the Baja screen.",
             _M)]),
    dict(group_id="LG-9", group="Other compliance instructions found in T04", rows=[
        _leg("T04-ROW-037", "visible in the base state", "none",
             "The fertilising programme must comply with the contract specification.", _M),
        _leg("T04-ROW-039", "visible in the base state", "none",
             "Fertiliser must match the contract document or be approved by the S.O.; "
             "unapproved substitution is a compliance failure.", _M)]),
]

LEGAL_CLARIFICATION = dict(
    decision_id="D-04",
    status="PENDING_BARIAH_CONFIRMATION",
    bariah_question=["BR-W4 — Kandungan Akta - Tak pasti ni yang di mana?",
                     "BR-W5 — 4. Kandungan Akta - tak pasti penerangan tambahan yang mana? "
                     "Click to reveal jika diperlukan"],
    answer_to_bariah="The legislative content is in the Racun section, pages 280 of the "
                     "module. It is not one paragraph — it is nineteen source rows across "
                     "nine obligation groups, and four more compliance rows sit in the Baja "
                     "section. Every row is listed below individually so the question 'which "
                     "content' has a concrete answer.",
    groups=LEGAL_GROUPS,
    recommended_option="Core legal and safety obligations visible on the base screen; "
                       "supplementary implementation detail may use click-to-reveal.",
    recommendation_status="PROPOSED_NOT_APPROVED",
    applied_to_a_contract=False,
    application_note="This split is NOT applied to any screen contract. T04-CT-04 still "
                     "carries every row in its base state, which is the safe position until "
                     "Bariah confirms.",
    supplementary_candidates=["T04-ROW-070", "T04-ROW-072", "T04-ROW-074"],
    supplementary_note="Exactly three rows are proposed as reveal candidates, and all three "
                       "are expansions of a duty already stated on the base screen. No duty "
                       "is proposed for hiding.")

LEGAL_TOTALS = dict(
    groups=len(LEGAL_GROUPS),
    rows=sum(len(g["rows"]) for g in LEGAL_GROUPS),
    mandatory=sum(1 for g in LEGAL_GROUPS for r in g["rows"]
                  if r["mandatory_or_supplementary"] == _M),
    supplementary=sum(1 for g in LEGAL_GROUPS for r in g["rows"]
                      if r["mandatory_or_supplementary"] == _S),
    v1_row_count=11,
    growth_note="Stage 4.2F-B0.5 counted 11 legal rows, all inside the Racun section. "
                "Answering Bariah's 'which content' question properly meant sweeping the "
                "whole unit for compliance instructions, which found four more in the Baja "
                "section (PPE, storage, specification compliance, documentation) and four "
                "structural heading rows. The population is larger than the v1 pack stated.")

# ==========================================================================================
# PART 8 — D-03 AND D-05 FOLLOW-UP
# ==========================================================================================
D03_FOLLOWUP = dict(
    decision_id="D-03", status="UNRESOLVED", scope="THIS_UNIT_ONLY",
    scope_guard="This is a T04 question. It is NOT a PL06-global cast decision and must not "
                "be recorded as one.",
    question="For T04, should the lesson use:",
    options=[
        dict(option="A", label="Hilmi as narrator only",
             note="Voice-over narration with no on-screen character interaction. T04 is "
                  "procedural content and the source contains no dialogue scenario."),
        dict(option="B", label="Hilmi plus an existing character",
             note="Adds a second voice. Which existing character is Bariah's choice — the "
                  "ratified bank and B02's shipped pair do not agree, and this stage does "
                  "not resolve that."),
        dict(option="C", label="Another treatment specified by Bariah", note="Open."),
    ],
    prior_recommendation_status="SUPERSEDED_NOT_APPROVED",
    prior_recommendation="Stage 4.2F-B0.5 recommended HILMI_NARRATOR_LED. Bariah's rulings "
                         "say nothing about cast, so that recommendation is not carried "
                         "forward as a decision. Option A is listed because it was the "
                         "recommendation, not because it is chosen.")

D05_FOLLOWUP = dict(
    decision_id="D-05", status="PARTIALLY_RESOLVED",
    confirmed=dict(ruling="EVERY_PROCESS_STEP_REQUIRES_A_VISUAL", evidence="BR-L1"),
    confirmations_required=[
        dict(item="A", ask="The review storyboard uses the six-step source diagram.",
             why="T04-DGM-01 is vector SmartArt, not a raster image. It cannot be extracted "
                 "as a JPEG the way B02's fourteen assets were, so how it appears in a review "
                 "deck is a decision, not a given.",
             status="NOT_CONFIRMED"),
        dict(item="B", ask="MMD later redraws each step visually.",
             why="BR-L1 requires a visual per step. Six new assets have to be produced by "
                 "someone, and nothing has confirmed that MMD owns that work.",
             status="NOT_CONFIRMED"),
        dict(item="C", ask="The six-node identity and order must remain unchanged.",
             why="The source diagram is flat and linear — all six nodes are children of the "
                 "document root, with zero parent-child links between them. A redraw that "
                 "introduces a tree, a cycle or a grouping would assert a relationship the "
                 "source does not contain.",
             status="NOT_CONFIRMED"),
    ],
    six_nodes_in_order=[dict(position=i + 1, label=lbl) for i, lbl in enumerate(PROCESS_NODES)],
    node_evidence=dict(asset_id=SMARTART_ASSET_ID,
                       part=SRC.ASSETS[0]["embedded_filename"],
                       sha256=SRC.ASSETS[0]["sha256"],
                       layout="urn:microsoft.com/office/officeart/2005/8/layout/process2",
                       hierarchy="NONE — flat", node_count=6),
    production_status="NOT_STARTED")

# ==========================================================================================
# PART 9 — REMAINING DECISIONS AND WHATSAPP FOLLOW-UP
# ==========================================================================================
REMAINING = [
    dict(item=1, decision_id="D-02B", title="Passing threshold",
         status="UNRESOLVED",
         ask="What is the pass mark for the five-item quiz?",
         why_unresolved="Composition is confirmed; the threshold was not mentioned. The 60 "
                        "percent figure exists only in the B02 slice of the Style and "
                        "Guidelines."),
    dict(item=2, decision_id="D-03", title="T04 cast / narrator",
         status="UNRESOLVED",
         ask="Narrator only, narrator plus an existing character, or something else?",
         why_unresolved="Bariah's rulings do not mention cast."),
    dict(item=3, decision_id="D-04", title="Legal content base/reveal split",
         status="CLARIFICATION_REQUIRED",
         ask="Confirm which of the listed rows must stay visible and which may reveal.",
         why_unresolved="Bariah asked which content was meant. The rows are now listed "
                        "individually, so the question can be answered concretely."),
    dict(item=4, decision_id="D-05", title="SmartArt review and MMD treatment",
         status="PARTIALLY_RESOLVED",
         ask="Confirm A, B and C in the D-05 follow-up.",
         why_unresolved="A visual per step is confirmed; the diagram's own treatment is not."),
    dict(item=5, decision_id="D-02C", title="Rumusan draft review",
         status="DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW",
         ask="Review the four drafted statements, and confirm the four-point consolidation.",
         why_unresolved="Drafting was authorised; approval was reserved."),
    dict(item=6, decision_id="D-02A", title="Five-slot quiz blueprint review",
         status="BLUEPRINT_PENDING_REVIEW",
         ask="Review the five slots and the QB-03 + QB-04 consolidation.",
         why_unresolved="Composition is settled. What each slot tests is not, and no question "
                        "has been written."),
]

NOT_ASKED_AGAIN = ["D-01 visual requirement — given clearly in the requirement sheet",
                   "D-02A quiz composition — 4 MCQ + 1 MR, given clearly",
                   "D-02C drafting authorisation — given clearly",
                   "Rumusan writing style — given clearly"]

WHATSAPP = dict(
    language="Malay",
    channel="WhatsApp",
    status="DRAFT_NOT_SENT",
    sending_authority="FIRDAUS",
    audience="BARIAH",
    text="""Terima kasih Bariah atas maklum balas untuk Topik 4.

Sudah direkodkan:
• Visual — setiap langkah dalam aliran proses perlu visual; Landskap Lembut (penerangan utama, Siram, Baja, Racun dan setiap sub-topik di bawahnya) perlu visual; Landskap Kejur (penerangan utama dan empat kumpulan yang Bariah senaraikan) perlu visual. Semuanya sudah disenaraikan satu per satu — 46 visual diperlukan.
• Kuiz — 4 MCQ dan 1 Multiple Response, untuk semua PL dalam Kursus.
• Rumusan — draf disediakan mengikut gaya penulisan Topik 3 Bahagian 2.

Ada 6 perkara yang masih memerlukan pengesahan Bariah:
1. Markah lulus kuiz — berapa peratus?
2. Topik 4 guna narator sahaja, narator bersama watak sedia ada, atau cara lain?
3. Kandungan Akta — kandungan berkaitan undang-undang ada di bahagian Racun (dan beberapa di bahagian Baja). Kami sudah senaraikan setiap baris satu per satu. Cadangan kami: semua kewajipan undang-undang dan keselamatan kekal kelihatan di skrin utama, dan hanya penerangan tambahan (contohnya senarai penuh PPE) guna click to reveal. Mohon Bariah sahkan.
4. Rajah enam langkah — mohon sahkan sama ada rajah asal digunakan dalam papan cerita, sama ada setiap langkah dilukis semula kemudian, dan sama ada susunan enam langkah itu perlu kekal sama.
5. Draf Rumusan — 4 ayat, mohon Bariah semak, ubah atau tolak.
6. Rangka kuiz 5 soalan — mohon Bariah semak apa yang diuji setiap soalan.

Untuk makluman:
• Papan cerita Topik 4 belum dijana lagi.
• Rumusan dan kuiz masih draf sahaja — belum ada soalan penuh dan belum ada jawapan. Semuanya menunggu semakan Bariah.

Terima kasih.""",
    constraints_honoured=["thanks Bariah", "summarises what is already recorded",
                          "asks only the six remaining items",
                          "no QA or engineering terminology",
                          "states that no storyboard has been generated",
                          "states that Rumusan and quiz remain drafts"])

# ==========================================================================================
# CONTRACTS v2 — the six candidate contracts, revised for the visual ruling
# ==========================================================================================
_CT_TO_SC = {"T04-CT-01": "T04-SC-01", "T04-CT-02": "T04-SC-02", "T04-CT-03": "T04-SC-05",
             "T04-CT-04": "T04-SC-03", "T04-CT-05": "T04-SC-04", "T04-CT-06": "T04-SC-06"}
_SC_MAP = {m["screen_candidate_id"]: m for m in MAPPING_V2}


def _contracts_v2():
    out = []
    for c in PACK.CONTRACTS:
        sc = _SC_MAP[_CT_TO_SC[c["contract_id"]]]
        d = dict(c)
        d["revision"] = "v2"
        d["superseded_visual_treatment"] = c["visual_treatment"]
        d["visual_obligation_ids"] = list(sc["visual_obligation_ids"])
        d["required_visual_states"] = sc["required_visual_states"]
        d["visual_treatment"] = _CT_VISUAL_V2[c["contract_id"]]
        d["visual_ruling_authority"] = TREATMENT_AUTHORITY
        d["visual_subject_authority"] = SUBJECT_AUTHORITY
        d["missing_production_asset"] = sc["missing_production_asset"]
        d["open_decision"] = _CT_OPEN_V2[c["contract_id"]]
        d["bariah_approval"] = dict(status=APPROVAL_STATUS, decision=None, comment=None)
        out.append(d)
    return out


_CT_VISUAL_V2 = {
    "T04-CT-01":
        "REVISED under BR-L1. The source-bound reference to T04-DGM-01 is retained for the "
        "overview, and SIX additional step visuals are now required — one per node, none of "
        "which exists. All six are NEW_MMD_ASSET_REQUIRED. Node identity and order stay "
        "exactly as measured; no seventh step.",
    "T04-CT-02":
        "REVISED under BR-L2 and BR-L3. The v1 treatment was 'NONE — text-led'. That is "
        "superseded: the section main explanation and each of Siram, Baja and Racun now "
        "require a visual. Four NEW_MMD_ASSET_REQUIRED. Subjects are module-derived.",
    "T04-CT-03":
        "REVISED under BR-L5 and BR-L6. The v1 treatment was 'NONE — text-led'. The section "
        "main explanation and the four named groups now require a visual. Five "
        "NEW_MMD_ASSET_REQUIRED. Bariah did not extend the ruling to the eight sub-items "
        "beneath the four groups; none was created.",
    "T04-CT-04":
        "REVISED under BR-L4. The v1 treatment was 'NONE'. The three Aspek Pengurusan "
        "headings under Racun are source subtopics, so each requires a safety-or-compliance "
        "visual. Three NEW_MMD_ASSET_REQUIRED. Adding visuals must not become a reason to "
        "move any obligation off the base state.",
    "T04-CT-05":
        "UNCHANGED in substance. This screen reuses the two section main-explanation visuals "
        "required by BR-L2 and BR-L5; it creates no obligation of its own.",
    "T04-CT-06":
        "UNCHANGED — Bariah's visual ruling does not reach the Rumusan or the quiz.",
}

_CT_OPEN_V2 = {
    "T04-CT-01": "D-05 — three confirmations outstanding; and visual subject approval for the "
                 "six step assets",
    "T04-CT-02": "D-01 subject approval for four assets",
    "T04-CT-03": "D-01 subject approval for five assets; Kejur sub-item scope",
    "T04-CT-04": "D-04 base/reveal split, and D-01 subject approval for three assets",
    "T04-CT-05": "whether this screen is wanted at all",
    "T04-CT-06": "D-02B pass threshold; Rumusan approval; quiz authoring",
}

CONTRACTS_V2 = _contracts_v2()

# ==========================================================================================
PPTX_GENERATED = 0
GENERATOR_TOUCHED = 0
APPROVED_ITEMS = 0
B02_FAMILIES_PROPAGATED = 0

VERDICT = "T04_PARTIAL_RULINGS_INCORPORATED_READY_FOR_FINAL_BARIAH_CLARIFICATIONS"
ALLOWED_VERDICTS = [VERDICT, "T04_PARTIAL_RULINGS_INCORPORATION_BLOCKED"]

if __name__ == "__main__":
    print(json.dumps(dict(obligations=VISUAL_TOTALS, legal=LEGAL_TOTALS,
                          unmapped=len(UNMAPPED_VO),
                          decisions={d["decision_id"]: d["status"] for d in DECISIONS}),
                     ensure_ascii=False, indent=1))
