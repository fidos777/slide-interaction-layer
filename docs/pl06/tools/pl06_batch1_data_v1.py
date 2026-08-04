# -*- coding: utf-8 -*-
"""Stage 4.2F-B2 — the ONE controlled data source for PL06 authority-harvest batch 1.

    BATCH_ID = PL06-HARVEST-BATCH-1
    UNITS    = K5-PL06-T03-B03, K5-PL06-T03-B04, K5-PL06-T05-B01, K5-PL06-T06-B01

Every string in the review DOCX, the Markdown projection and the traceability tables is
projected from this module. Nothing may be written into one representation and not the other.

WHAT THIS PACKAGE CAN AND CANNOT ASK
------------------------------------
The four units' boundaries are frozen, hash-verified and anchored to named DOCX headings.
Their CONTENT is not extracted — `PL06_OPEN_AUTHORITY_ITEMS_v1` records STOP-003, STOP-004
and STOP-005 against all four, and the module DOCX itself is held externally by identity and
is not in this repository.

So this package prefills every decision the frozen evidence actually reaches — boundaries,
shared-page risks, grouping at heading level, screen-count arithmetic, treatment vocabulary,
reuse and no-reuse — and it records `PENDING_EXTRACTION` everywhere it does not. It does not
write quiz stems, learning outcomes, visual subjects or screen content for units whose source
text nobody has read. A prefilled card that invented those would be asking Bariah to approve
CAIR's imagination, which is the one thing this whole governance chain exists to prevent.

The single decision that unblocks the rest is the extraction authorisation, PL06-B1-D-25.
"""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PL06 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(PL06))
FREEZE = os.path.join(PL06, "source-freeze")

STAGE = "4.2F-B2"
LANE = "LANE_B_PL06_AUTHORITY_HARVEST_BATCH_1"
BATCH_ID = "PL06-HARVEST-BATCH-1"
SUITE_ID = "PL06_AUTHORITY_HARVEST_BATCH1_QA_v1"
GENERATED_BY = "docs/pl06/tools/pl06_batch1_emit_v1.py"

# This package proposes. It approves nothing.
BATCH_STATUS = "CAIR_PREFILLED_AWAITING_BARIAH_DECISIONS"
FORBIDDEN_STATUS_CLAIMS = [
    "BATCH_APPROVED",
    "UNITS_READY_FOR_STORYBOARD_BUILD",
    "CONTENT_EXTRACTED",
    "ANSWER_KEYS_APPROVED",
]

BATCH_UNITS = ["K5-PL06-T03-B03", "K5-PL06-T03-B04",
               "K5-PL06-T05-B01", "K5-PL06-T06-B01"]

# ==========================================================================================
# FROZEN SOURCE — verified before it is read, not after
# ==========================================================================================
BOUNDARY_MAP_PATH = os.path.join(FREEZE, "PL06_LESSON_BOUNDARY_MAP_v1.json")
BOUNDARY_MAP_SHA256 = "aa02cd3c784113b00c056280fb236f6ae56a48b013fb388bb47011ba6e31c073"

MODULE_DOCX_NAME = "[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx"
MODULE_DOCX_BYTES = 16832861
MODULE_DOCX_SHA256 = "5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7"
MODULE_DOCX_CUSTODY = "EXTERNAL_DURABLE_SOURCE_BY_IDENTITY"
MODULE_DOCX_IN_THIS_REPOSITORY = False


class FrozenSourceMissing(RuntimeError):
    """Fail closed rather than harvest from an unverified boundary map."""


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_boundary_map():
    if not os.path.exists(BOUNDARY_MAP_PATH):
        raise FrozenSourceMissing(f"frozen boundary map missing: {BOUNDARY_MAP_PATH}")
    got = _sha256(BOUNDARY_MAP_PATH)
    if got != BOUNDARY_MAP_SHA256:
        raise FrozenSourceMissing(
            f"boundary map hash mismatch: expected {BOUNDARY_MAP_SHA256}, got {got}")
    return json.load(open(BOUNDARY_MAP_PATH, encoding="utf-8"))


_MAP = _load_boundary_map()
_LESSONS = {l["unit_id"]: l for l in _MAP["lessons"]}

# Boundary page images named in the freeze package. Only two were ingested into this
# repository; the rest survive as identities under STOP-014, and the difference is a real
# difference in evidence strength that the cards report per unit.
BOUNDARY_IMAGES_IN_PACKAGE = ["p180", "p199", "p206", "p207", "p219", "p233", "p244",
                              "p255", "p268", "p269", "p274", "p280", "p294", "p302",
                              "p312", "p321", "p328"]
BOUNDARY_IMAGES_INGESTED = ["p294", "p302"]
BOUNDARY_IMAGE_DIR = os.path.join(FREEZE, "boundary_pages")

# ==========================================================================================
# SECTION B — RULES THAT MAY BE AUTO-APPLIED
#
# Auto-applied means: applied without asking, because the rule is course-wide or generic and
# not a T04 instructional decision. Each one still carries its evidence and its own caveat.
# ==========================================================================================
AUTO_APPLIED_RULES = [
    dict(rule_id="AR-01",
         rule="Quiz composition: 4 Multiple Choice + 1 Multiple Response.",
         scope="ALL_PL06_UNITS",
         evidence="Course-wide rule carried forward from the B02 Style and Guidelines "
                  "(RP-009) and applied in T04.",
         caveat="RP-009 classifies this GLOBAL on the strength of a Style and Guidelines "
                "document that is itself the B02 slice, and flags it "
                "human_authority_required = VERIFY. It is applied here as instructed and "
                "the flag is reported, not quietly dropped."),
    dict(rule_id="AR-02",
         rule="Pass threshold: 60 percent.",
         scope="ALL_PL06_UNITS",
         evidence="RP-010, same Style and Guidelines source as AR-01.",
         caveat="Same VERIFY flag as AR-01."),
    dict(rule_id="AR-03",
         rule="No learner-facing 'dalam modul', 'mengikut modul' or 'modul menyenaraikan'.",
         scope="ALL_PL06_UNITS",
         evidence="Generic learner-language rule. A learner is reading the course, not "
                  "being told about a document.",
         caveat="None. This is a phrasing rule, not an instructional decision."),
    dict(rule_id="AR-04",
         rule="Multiple Response items use checkboxes with no A/B/C option labels.",
         scope="ALL_PL06_UNITS",
         evidence="Generic assessment-mechanics rule; applied to T04 Q5.",
         caveat="None."),
    dict(rule_id="AR-05",
         rule="Instructional clarity overrides production optimisation.",
         scope="ALL_PL06_UNITS",
         evidence="Standing principle. Where a cheaper treatment would obscure the "
                  "instruction, the clearer treatment wins.",
         caveat="None."),
    dict(rule_id="AR-06",
         rule="Supported treatment vocabulary: static content, click-to-reveal, "
              "progressive process, comparison, scenario/dialogue only where justified.",
         scope="ALL_PL06_UNITS",
         evidence="The vocabulary these units may be described in. A treatment outside it "
                  "is an escalation, not a proposal.",
         caveat="'Only where justified' is doing real work in the last item: a dialogue "
                "needs a reason, not a habit."),
]

BANNED_LEARNER_PHRASES = ["dalam modul", "mengikut modul", "modul menyenaraikan"]

SUPPORTED_TREATMENTS = ["static content", "click-to-reveal", "progressive process",
                        "comparison", "scenario/dialogue only where justified"]

# ==========================================================================================
# NO-REUSE — T04 decisions that are T04's, and stay T04's
# ==========================================================================================
NO_REUSE = [
    dict(item_id="NR-01", item="T04 three-beat Rumusan",
         reason="Bariah ruled the beat count for T04's content. No course-wide Rumusan "
                "length rule was ever stated, and Stage 4.2F-B0.9 was explicitly forbidden "
                "to infer one.",
         what_is_portable="RP-007 — the Rumusan TREATMENT: this Bahagian only, contractor "
                          "perspective, no Kepentingan / Isi Utama / Manfaat labels."),
    dict(item_id="NR-02", item="Alya and Encik Rahman",
         reason="The ratified K5 character bank marks Haziq and Encik Roslan CANONICAL "
                "while B02 ships Alya and Encik Rahman. Bariah's PL06-wide instruction "
                "names neither pair and is conditional on 'kesesuaian'.",
         what_is_portable="Nothing until STOP-006 / SRC-ANOM-003 is resolved. RP-106 is "
                          "the one rule in the portability matrix with oracle = no."),
    dict(item_id="NR-03", item="The T04 four-line dialogue pattern",
         reason="Four lines was a shape chosen for T04's opening, not a course grammar.",
         what_is_portable="Whether a unit opens with a dialogue at all is a per-unit "
                          "question — point 9 on every card."),
    dict(item_id="NR-04", item="The T04 screen count (22)",
         reason="A screen count is a function of the unit's own content. Reusing it would "
                "make four different units the same length by coincidence.",
         what_is_portable="The screen-count ARITHMETIC, exposed per unit in section C-F."),
    dict(item_id="NR-05", item="T04 asset groups (8)",
         reason="Asset groups were derived from T04's own visual obligations.",
         what_is_portable="RP-104 — the binding RULE: a visual direction is read from the "
                          "source row's own figure or table, never composed from a name."),
    dict(item_id="NR-06", item="T04 visual totals (46 obligations, 41 proposed assets)",
         reason="Derived from T04's heading hierarchy and Bariah's three ruled groups. "
                "These four units have no extracted visual inventory at all (STOP-003).",
         what_is_portable="The three-field authority split: requirement authority, "
                          "population derivation, subject authority."),
    dict(item_id="NR-07", item="The T04 runtime-state page format",
         reason="Held back until Lane A resolved whether that format proves review "
                "coverage.",
         status="RELEASED_BY_LANE_A",
         what_is_portable="Lane A closed at T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN, "
                          "so the two-panel state-appendix FORMAT is now available as a "
                          "mechanism. The per-unit state COUNTS are not — they need "
                          "content. See point 8 on every card."),
]

# ==========================================================================================
# PROVENANCE — every line in the package carries one of these, visibly
# ==========================================================================================
PROVENANCE_CLASSES = [
    dict(code="AUTO", label="AUTO-APPLIED COURSE RULE",
         meaning="Applied without asking, because the rule is course-wide or generic."),
    dict(code="SRC", label="SOURCE-DERIVED FACT",
         meaning="Read from a frozen, hash-verified artifact. Not a proposal."),
    dict(code="CAIR", label="CAIR PROPOSAL",
         meaning="Ours. Reject it freely — nothing downstream depends on it yet."),
    dict(code="BARIAH", label="BARIAH DECISION REQUIRED",
         meaning="Cannot be settled by evidence in this repository."),
    dict(code="OPEN", label="OPEN SOURCE ISSUE",
         meaning="The source itself is missing, ambiguous or contradictory."),
]
PROVENANCE_CODES = [p["code"] for p in PROVENANCE_CLASSES]

RESPONSE_OPTIONS = [
    dict(option="TERIMA", meaning="Accept as prefilled.", requires_target_id=False),
    dict(option="PINDA", meaning="Accept with the amendment written in the response box.",
         requires_target_id=False),
    dict(option="BUANG", meaning="Remove this item entirely.", requires_target_id=False),
    dict(option="GABUNG", meaning="Merge into another unit or screen group.",
         requires_target_id=True),
    dict(option="ESCALATE", meaning="Source or instructional ambiguity — do not proceed.",
         requires_target_id=False),
]
GABUNG_TARGET_FIELD = "ID sasaran"

# ==========================================================================================
# THE SIXTEEN CARD POINTS — the same sixteen, in the same order, on every card
# ==========================================================================================
CARD_POINTS = [
    dict(no=1, key="boundary", title="Sempadan sumber dan julat muka surat"),
    dict(no=2, key="shared_page_risk", title="Risiko sempadan muka surat dikongsi"),
    dict(no=3, key="controlled_rows", title="Baris sumber terkawal"),
    dict(no=4, key="mandatory_content", title="Kandungan instruksi yang wajib"),
    dict(no=5, key="grouping", title="Cadangan pengumpulan"),
    dict(no=6, key="screen_sequence", title="Cadangan urutan skrin pelajar"),
    dict(no=7, key="treatment", title="Rawatan bagi setiap kumpulan skrin"),
    dict(no=8, key="runtime_states", title="Jangkaan bilangan keadaan runtime"),
    dict(no=9, key="dialogue", title="Dialog: perlu / tidak perlu / belum pasti"),
    dict(no=10, key="rumusan", title="Cadangan struktur Rumusan"),
    dict(no=11, key="quiz_stems", title="Lima batang soalan kuiz"),
    dict(no=12, key="answer_keys", title="Status kunci jawapan dan sokongan sumber"),
    dict(no=13, key="visual_obligations", title="Obligasi visual"),
    dict(no=14, key="reuse", title="Calon guna semula"),
    dict(no=15, key="no_reuse", title="Pengecualian tidak boleh guna semula"),
    dict(no=16, key="open_questions", title="Soalan kuasa yang belum selesai"),
]

PENDING = "PENDING_EXTRACTION"
NOT_EXTRACTED = "SOURCE_PRESENT_CONTENT_NOT_EXTRACTED"
UNKNOWN = "UNKNOWN_PENDING_EXTRACTION"

# The blocking stop conditions already on the PL06 register. Referenced, never re-minted.
BLOCKING_STOPS = [
    dict(stop_id="STOP-003", condition="VISUAL_INVENTORY_NOT_EXTRACTED",
         register="PL06_OPEN_AUTHORITY_ITEMS_v1"),
    dict(stop_id="STOP-004", condition="CONTROLLED_CONTENT_NOT_EXTRACTED",
         register="PL06_OPEN_AUTHORITY_ITEMS_v1"),
    dict(stop_id="STOP-005", condition="NO_QUIZ_SOURCE",
         register="PL06_OPEN_AUTHORITY_ITEMS_v1"),
    dict(stop_id="STOP-006", condition="CAST_BINDING_UNRESOLVED",
         register="PL06_OPEN_AUTHORITY_ITEMS_v1"),
]

# ==========================================================================================
# PER-UNIT PROPOSALS — only the parts the frozen evidence reaches
# ==========================================================================================
_UNIT_NOTES = {
    "K5-PL06-T03-B03": dict(
        display="Topik 3 · Infrastruktur",
        start_pdf_page=268,
        dialogue_proposal="UNCERTAIN",
        dialogue_reason=(
            "Infrastruktur is a component section inside the same Topik as B02. Whether it "
            "opens with a scenario or goes straight to the component content depends on "
            "whether the section is written as a catalogue or as a decision the contractor "
            "makes. That cannot be read from a heading."),
        treatment_proposal="click-to-reveal",
        treatment_reason=(
            "A single named subtopic covering infrastructure components is the shape "
            "click-to-reveal fits — but this is a guess from the heading, and the extraction "
            "may show a process, in which case progressive process is correct instead."),
        merge_candidate="K5-PL06-T03-B04",
        merge_reason=(
            "T03-B03 (6 pages, 1 subtopic) and T03-B04 (7 pages, 1 subtopic) are adjacent "
            "single-subtopic lessons in the same Topik and share module page 255. Two short "
            "units or one ordinary one is a real choice, and it is cheaper to make it now "
            "than after both are extracted.")),
    "K5-PL06-T03-B04": dict(
        display="Topik 3 · Badan Air (Water Body)",
        start_pdf_page=273,
        dialogue_proposal="NOT_REQUIRED",
        dialogue_reason=(
            "A water-body section is component description. Nothing in the boundary "
            "suggests a decision scenario. Proposed as no dialogue, which is the cheaper "
            "and quieter default — overturn it freely if the content says otherwise."),
        treatment_proposal="click-to-reveal",
        treatment_reason=(
            "Same reasoning and the same caveat as T03-B03."),
        merge_candidate="K5-PL06-T03-B03",
        merge_reason="The other half of the same merge question."),
    "K5-PL06-T05-B01": dict(
        display="Topik 5 · Pengurusan Kualiti Projek",
        start_pdf_page=302,
        dialogue_proposal="REQUIRED",
        dialogue_reason=(
            "Quality management is where a contractor's habits and the specification "
            "collide, and the frozen boundary image for this unit shows the section opening "
            "on measurable quality objectives with worked landscape examples. A short "
            "opening scenario has something concrete to be about. This is the one unit in "
            "the batch where a dialogue is proposed rather than questioned."),
        treatment_proposal="progressive process",
        treatment_reason=(
            "Four named subtopics that read as a sequence — plan, assure, inspect and test, "
            "method statement. If extraction confirms that ordering, progressive process "
            "fits; if the four are independent, comparison or click-to-reveal is better."),
        merge_candidate=None, merge_reason=None),
    "K5-PL06-T06-B01": dict(
        display="Topik 6 · Perlindungan dan Penambahbaikan Alam Sekitar",
        start_pdf_page=312,
        dialogue_proposal="UNCERTAIN",
        dialogue_reason=(
            "6.2 is named 'Contoh Aplikasi dalam Landskap' — worked examples, which "
            "sometimes carry a scenario and sometimes are a gallery. The heading does not "
            "say which."),
        treatment_proposal="comparison",
        treatment_reason=(
            "A management plan, then applications, then management practice reads like a "
            "before-and-after or plan-versus-practice comparison. Weakly held."),
        merge_candidate=None, merge_reason=None),
}


def flag(value):
    """Read a boundary-map flag whatever shape it arrives in.

    The CSV projection stores these as the strings "True"/"False"; the JSON stores real
    booleans. Comparing the JSON value against "True" is silently always False, which is
    how every shared-boundary risk in the first build of this package came out as "none" —
    the one statement that would have been most damaging to get wrong.
    """
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() == "true"


def _subtopics(lesson):
    """The named subtopics, split on the map's own '+' separator. Nothing invented."""
    return [s.strip() for s in lesson["subtopics"].split("+") if s.strip()]


# Screen-count arithmetic, with every term's provenance attached. The numbers below are a
# FLOOR derived from the named subtopics, not a proposed screen count.
SHELL_SCREENS_ALWAYS = 2          # topic entry, orientation
SHELL_SCREENS_IF_DIALOGUE = 1     # the dialogue screen, when a unit has one
CLOSING_SCREENS = 3               # Rumusan, quiz, Tamat
SHELL_BASIS = "RP-002 screen grammar and RP-007 / RP-008 / RP-012 closing grammar"


def screen_arithmetic(unit_id):
    lesson = _LESSONS[unit_id]
    note = _UNIT_NOTES[unit_id]
    subs = _subtopics(lesson)
    dialogue = note["dialogue_proposal"] == "REQUIRED"
    shell = SHELL_SCREENS_ALWAYS + (SHELL_SCREENS_IF_DIALOGUE if dialogue else 0)
    return dict(
        unit_id=unit_id,
        named_subtopics=len(subs),
        shell_screens=shell,
        shell_includes_dialogue=dialogue,
        shell_basis=SHELL_BASIS,
        content_screens_floor=len(subs),
        content_screens_ceiling=UNKNOWN,
        closing_screens=CLOSING_SCREENS,
        minimum_total_screens=shell + len(subs) + CLOSING_SCREENS,
        maximum_total_screens=UNKNOWN,
        floor_basis="one content screen per NAMED subtopic — the fewest that can carry the "
                    "headings the boundary map lists",
        why_no_single_number="A screen count is a function of how many records each "
                             "subtopic holds. None of these units is extracted, so the "
                             "ceiling is not knowable and is not guessed.")


def runtime_state_note(unit_id):
    a = screen_arithmetic(unit_id)
    return dict(
        unit_id=unit_id,
        provenance="OPEN",
        method="base states = learner screens; triggered states = one per reveal, step or "
               "quiz item; completion flags = one per screen that gates SETERUSNYA",
        method_source="Lane A T04 state model, released for reuse as a METHOD by "
                      "T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN",
        base_states_floor=a["minimum_total_screens"],
        triggered_states=UNKNOWN,
        total_runtime_states=UNKNOWN,
        why="Triggered states depend on how many records each screen reveals, which is "
            "exactly what extraction produces. Reusing T04's 65 would be reusing T04's "
            "content, which NR-04 and NR-07 forbid.")


def unit_card(unit_id):
    lesson = _LESSONS[unit_id]
    note = _UNIT_NOTES[unit_id]
    subs = _subtopics(lesson)
    arith = screen_arithmetic(unit_id)
    pages = lesson["module_page_range"]
    p_start, p_end = (int(x) for x in pages.split("-"))
    para_span = int(lesson["docx_para_end_before"]) - int(lesson["docx_para_start"])
    img = f"p{note['start_pdf_page']}"
    return dict(
        unit_id=unit_id,
        display_title=note["display"],
        topik=lesson["topik"], bahagian=lesson["bahagian"],
        topik_title=lesson["topik_title"], lesson_title=lesson["lesson_title"],
        points={
            "boundary": dict(
                provenance="SRC",
                module_page_range=pages, module_pages=p_end - p_start + 1,
                pdf_page_range=lesson["pdf_page_range"],
                start_anchor=lesson["start_anchor"], end_before=lesson["end_before"],
                docx_para_start=int(lesson["docx_para_start"]),
                docx_para_end_before=int(lesson["docx_para_end_before"]),
                paragraph_span=para_span,
                map_status=lesson["status"],
                boundary_image=img,
                boundary_image_custody=(
                    "INGESTED_IN_THIS_REPOSITORY" if img in BOUNDARY_IMAGES_INGESTED
                    else "NAMED_IN_THE_FREEZE_PACKAGE_BY_IDENTITY_ONLY"
                    if img in BOUNDARY_IMAGES_IN_PACKAGE
                    else "NO_IMAGE_FOR_THIS_START_PAGE")),
            "shared_page_risk": dict(
                provenance="SRC",
                shared_start=flag(lesson["shared_start"]),
                shared_end=flag(lesson["shared_end"]),
                note=lesson["boundary_note"],
                risk=("A shared page must be split by heading anchor, never by page "
                      "extraction. Extracting page-wise would pull the neighbouring "
                      "lesson's text into this unit."
                      if (flag(lesson["shared_start"]) or flag(lesson["shared_end"]))
                      else "None. Both boundaries fall on unshared pages.")),
            "controlled_rows": dict(
                provenance="OPEN",
                status=NOT_EXTRACTED, row_count=UNKNOWN,
                paragraph_span=para_span,
                blocking_stop="STOP-004",
                note=f"{para_span} DOCX body paragraphs lie between the anchors. That is a "
                     f"controlled magnitude, not a row count — extraction turns paragraphs "
                     f"into typed content records and the ratio is not fixed."),
            "mandatory_content": dict(
                provenance="SRC",
                named_subtopics=subs,
                status="HEADING_LEVEL_ONLY",
                note="The named subtopics are mandatory because the module names them. "
                     "What is mandatory BELOW heading level cannot be known before "
                     "extraction, and no learning outcome is written here for a unit whose "
                     "text nobody has read."),
            "grouping": dict(
                provenance="CAIR",
                proposal=[dict(group_id=f"G{i + 1}", covers=s) for i, s in enumerate(subs)],
                rule="One screen group per named subtopic.",
                note="A floor, not a ceiling. Extraction may show a subtopic that needs "
                     "two groups; it will not show one that needs none."),
            "screen_sequence": dict(
                provenance="CAIR",
                sequence=(["S01 Topik entry (AUTO — RP-002)"]
                          + (["S02 Dialog (CAIR — see point 9)"]
                             if arith["shell_includes_dialogue"] else [])
                          + ["S0x Orientasi (AUTO — RP-002)"]
                          + [f"Kumpulan {i + 1}: {s}" for i, s in enumerate(subs)]
                          + ["Rumusan (AUTO treatment RP-007, length BARIAH)",
                             "Kuiz (AUTO — AR-01, AR-02)",
                             "Tamat (AUTO — RP-012 behaviour; destination per unit)"]),
                arithmetic=arith),
            "treatment": dict(
                provenance="CAIR",
                proposal=note["treatment_proposal"],
                reason=note["treatment_reason"],
                vocabulary=SUPPORTED_TREATMENTS,
                confidence="LOW — read from a heading, not from content"),
            "runtime_states": runtime_state_note(unit_id),
            "dialogue": dict(
                provenance="CAIR",
                proposal=note["dialogue_proposal"],
                reason=note["dialogue_reason"],
                constraint="The T04 four-line pattern is NOT carried over (NR-03), and no "
                           "character name is proposed while STOP-006 is open (NR-02)."),
            "rumusan": dict(
                provenance="AUTO",
                treatment="Summarises THIS Bahagian only, contractor and site perspective, "
                          "no Kepentingan / Isi Utama / Manfaat labels (RP-007).",
                beat_count="BARIAH",
                note="T04's three beats are NOT reused (NR-01). No course-wide Rumusan "
                     "length rule exists and Stage 4.2F-B0.9 was forbidden to infer one."),
            "quiz_stems": dict(
                provenance="OPEN",
                composition="4 Multiple Choice + 1 Multiple Response (AUTO — AR-01)",
                slots=[dict(slot=f"Q{i + 1}",
                            kind="MULTIPLE_RESPONSE" if i == 4 else "MULTIPLE_CHOICE",
                            draws_from=subs[i % len(subs)],
                            stem=PENDING)
                       for i in range(5)],
                blocking_stop="STOP-005",
                note="Five slots with their composition and their subtopic binding are "
                     "prefilled. The stems are not. Writing five questions about pages "
                     "nobody has read would be inventing assessment content, and the "
                     "slot-to-subtopic binding shown here is itself provisional until the "
                     "content behind each heading is known."),
            "answer_keys": dict(
                provenance="OPEN",
                status="NOT_DRAFTED",
                authority="NONE — no key exists, so none is approved",
                source_support="NONE_YET",
                blocking_stop="STOP-005",
                note="RP-108 requires every option to map to a source row and the key to be "
                     "derived from controlled content. Neither is possible yet. This field "
                     "says NOT_DRAFTED rather than PENDING_APPROVAL, because there is "
                     "nothing to approve."),
            "visual_obligations": dict(
                provenance="OPEN",
                count=UNKNOWN,
                status="NOT_EXTRACTED",
                blocking_stop="STOP-003",
                rule="RP-104 — a visual direction is read from the source row's own figure "
                     "or table photograph, never composed from a component name.",
                note="UNKNOWN, not zero. A unit with no extracted assets cannot satisfy "
                     "RP-104 and must not be given placeholder subjects to pass."),
            "reuse": dict(
                provenance="AUTO",
                candidates=[
                    "RP-001 review storyboard shell",
                    "RP-002 S01 / S02 / S03 screen grammar (structure only)",
                    "RP-003 off-canvas production panel",
                    "RP-004 Speaker Notes typed-block schema",
                    "RP-005 English-term italics MECHANISM (not the B02 term list)",
                    "RP-006 completion-state treatment",
                    "RP-007 Rumusan treatment (not the beat count)",
                    "RP-008 quiz review structure",
                    "RP-011 correct / incorrect feedback wording",
                    "RP-013 off-canvas geometry registry",
                    "RP-014 artifact identity and exact release-token validation",
                    "RP-015 screen / state / page three-way separation",
                    "RP-016 oracle contract",
                    "RP-017 population pinning",
                    "Lane A state-appendix FORMAT (mechanism only — NR-07)"]),
            "no_reuse": dict(
                provenance="BARIAH",
                exceptions=[n["item_id"] for n in NO_REUSE],
                unit_specific=("RP-201 to RP-208 — the B02 execution families, component "
                               "names and cardinalities — are B02's and do not travel, "
                               "including into T03-B03 and T03-B04, which sit in B02's own "
                               "Topik and are the likeliest place for them to be assumed."
                               if unit_id.startswith("K5-PL06-T03")
                               else "RP-201 to RP-208 do not apply; this unit is in a "
                                    "different Topik from B02.")),
            "open_questions": dict(
                provenance="OPEN",
                items=[s["stop_id"] + " " + s["condition"] for s in BLOCKING_STOPS]
                + ([f"Merge with {note['merge_candidate']}? — {note['merge_reason']}"]
                   if note["merge_candidate"] else [])),
        })


def units():
    return [unit_card(u) for u in BATCH_UNITS]


# ==========================================================================================
# DECISIONS — every one bounded, numbered, and given a place to be answered
# ==========================================================================================
_UNIT_DECISIONS = [
    ("boundary", "Terima sempadan beku unit ini seperti dinyatakan?",
     ["TERIMA", "PINDA", "ESCALATE"], "SRC"),
    ("grouping", "Terima satu kumpulan skrin bagi setiap subtopik bernama?",
     ["TERIMA", "PINDA", "GABUNG", "ESCALATE"], "CAIR"),
    ("dialogue", "Terima cadangan dialog bagi unit ini?",
     ["TERIMA", "PINDA", "BUANG", "ESCALATE"], "CAIR"),
    ("treatment", "Terima rawatan yang dicadangkan bagi kumpulan kandungan?",
     ["TERIMA", "PINDA", "ESCALATE"], "CAIR"),
    ("rumusan", "Berapa bilangan beat Rumusan bagi unit ini?",
     ["PINDA", "ESCALATE"], "BARIAH"),
    ("quiz_slots", "Terima pengikatan lima slot kuiz kepada subtopik bernama?",
     ["TERIMA", "PINDA", "ESCALATE"], "CAIR"),
]

# ==========================================================================================
# LANGUAGE — stated, not assumed
#
# T04's state appendix shipped in English before anyone noticed it was going to a Malay
# reader. That is not repeated silently here: the surface a reviewer must read to answer —
# every question, option, card heading and table header — is Malay. The rationale layer,
# which explains to CAIR and Firdaus why a proposal exists, is English, because that is the
# language every governance record in this repository is already written in. Whether that
# split is acceptable is PL06-B1-D-29, not our decision to make.
LANGUAGE_POLICY = dict(
    decision_surface="MALAY",
    rationale_layer="ENGLISH",
    statement_ms=("Permukaan keputusan — setiap soalan, pilihan, tajuk kad dan pengepala "
                  "jadual — dalam Bahasa Melayu. Lapisan rasional yang menerangkan asal "
                  "usul setiap cadangan kekal dalam Bahasa Inggeris, sama seperti semua "
                  "rekod tadbir urus lain dalam repositori ini. Jika lapisan rasional "
                  "perlu diterjemahkan juga, sila jawab PL06-B1-D-29."))

_CROSS_DECISIONS = [
    dict(key="extraction", provenance="OPEN",
         question="Beri kebenaran mengekstrak kandungan terkawal bagi keempat-empat unit "
                  "ini daripada DOCX modul beku?",
         options=["TERIMA", "PINDA", "ESCALATE"],
         why="STOP-003, STOP-004 and STOP-005 block all four units. Nothing below heading "
             "level in this package can be settled until extraction runs. This is the one "
             "decision that unblocks the other twenty-four."),
    dict(key="merge_t03", provenance="BARIAH",
         question="Gabungkan K5-PL06-T03-B03 dengan K5-PL06-T03-B04 menjadi satu unit?",
         options=["TERIMA", "BUANG", "GABUNG", "ESCALATE"],
         why="Both are single-subtopic lessons in the same Topik, 6 and 7 module pages, "
             "sharing module page 255. Deciding before extraction avoids extracting twice."),
    dict(key="cast", provenance="BARIAH",
         question="Pasangan watak mana yang digunakan apabila sesebuah unit memerlukan "
                  "dialog?",
         options=["PINDA", "ESCALATE"],
         why="A restatement of the existing STOP-006 / SRC-ANOM-003, not a new register "
             "entry. No unit in this batch can carry a dialogue until it is answered, which "
             "is why T05-B01's dialogue proposal is blocked behind it."),
    dict(key="quiz_rules_verify", provenance="BARIAH",
         question="Sahkan bahawa 4 MCQ + 1 MR dan ambang 60 peratus ialah peraturan seluruh "
                  "kursus, bukan hanya amalan B02?",
         options=["TERIMA", "PINDA", "ESCALATE"],
         why="AR-01 and AR-02 are auto-applied as instructed, but RP-009 and RP-010 carry "
             "human_authority_required = VERIFY. They are applied and flagged, not applied "
             "and forgotten."),
    dict(key="language", provenance="BARIAH",
         question="Adakah lapisan rasional Bahasa Inggeris boleh diterima, atau perlu "
                  "diterjemahkan ke Bahasa Melayu sepenuhnya?",
         options=["TERIMA", "PINDA", "ESCALATE"],
         why="The decision surface is already Malay. The rationale layer is English "
             "because every governance record here is. T04's state appendix went out in "
             "English before anyone noticed who was reading it; this asks instead of "
             "assuming."),
]


def decisions():
    out, n = [], 0
    for u in BATCH_UNITS:
        card = unit_card(u)
        for key, question, options, prov in _UNIT_DECISIONS:
            n += 1
            out.append(dict(
                decision_id=f"PL06-B1-D-{n:02d}",
                unit_id=u, unit_display=card["display_title"],
                scope="UNIT", point_key=key, provenance=prov,
                question=question, options=list(options),
                requires_target_id="GABUNG" in options,
                # Where the ANSWER is written — section H — not where the question is
                # discussed. The card reference is kept separately so a reviewer can get
                # back to the evidence without the two being confused.
                response_location=f"H · PL06-B1-D-{n:02d}",
                card_reference=f"{_section_letter(u)}.{key}",
                why=None))
    for d in _CROSS_DECISIONS:
        n += 1
        out.append(dict(
            decision_id=f"PL06-B1-D-{n:02d}",
            unit_id=None, unit_display="SEMUA UNIT",
            scope="BATCH", point_key=d["key"], provenance=d["provenance"],
            question=d["question"], options=list(d["options"]),
            requires_target_id="GABUNG" in d["options"],
            response_location=f"H · PL06-B1-D-{n:02d}",
            card_reference="G",
            why=d["why"]))
    return out


_SECTION_LETTER = {"K5-PL06-T03-B03": "C", "K5-PL06-T03-B04": "D",
                   "K5-PL06-T05-B01": "E", "K5-PL06-T06-B01": "F"}


def _section_letter(unit_id):
    return _SECTION_LETTER[unit_id]


SECTIONS = [
    dict(letter="A", title="Gambaran keseluruhan kelompok", key="overview"),
    dict(letter="B", title="Peraturan seluruh kursus yang boleh diguna semula", key="rules"),
    dict(letter="C", title="Kad keputusan — K5-PL06-T03-B03", key="K5-PL06-T03-B03"),
    dict(letter="D", title="Kad keputusan — K5-PL06-T03-B04", key="K5-PL06-T03-B04"),
    dict(letter="E", title="Kad keputusan — K5-PL06-T05-B01", key="K5-PL06-T05-B01"),
    dict(letter="F", title="Kad keputusan — K5-PL06-T06-B01", key="K5-PL06-T06-B01"),
    dict(letter="G", title="Pengecualian merentas unit", key="exceptions"),
    dict(letter="H", title="Helaian keputusan Bariah", key="decision_sheet"),
]

# ==========================================================================================
# EXPOSED BEFORE APPROVAL — the seven things the reviewer must see first
# ==========================================================================================
def exposures():
    arith = [screen_arithmetic(u) for u in BATCH_UNITS]
    return [
        dict(exposure_id="EX-01", subject="Screen-count arithmetic",
             statement="Every unit's screen count is given as a floor with its terms shown, "
                       "never as a single number. Floors: "
                       + "; ".join(f"{a['unit_id']} ≥ {a['minimum_total_screens']}"
                                   for a in arith)
                       + ". Ceilings are UNKNOWN_PENDING_EXTRACTION."),
        dict(exposure_id="EX-02", subject="Proposal origin",
             statement="Every line carries one of five visible provenance labels. Nothing "
                       "marked CAIR PROPOSAL has any evidence behind it beyond a heading."),
        dict(exposure_id="EX-03", subject="Source limitations",
             statement="The module DOCX is held externally by identity and is not in this "
                       "repository. No unit in this batch has extracted content, visuals or "
                       "quiz source. STOP-003, STOP-004 and STOP-005 are open on all four."),
        dict(exposure_id="EX-04", subject="Shared-boundary uncertainty",
             statement="T03-B03 shares both its start and end pages; T03-B04 shares its "
                       "start. Those boundaries must be split by heading anchor. T05-B01 "
                       "and T06-B01 have clean boundaries on both sides."),
        dict(exposure_id="EX-05", subject="Visual reuse restrictions",
             statement="No visual subject is proposed for any unit. T04's 46 obligations "
                       "and 8 asset groups do not travel (NR-05, NR-06), and RP-104 forbids "
                       "composing a subject from a component name."),
        dict(exposure_id="EX-06", subject="Answer keys not authority-approved",
             statement="No answer key exists for any unit in this batch. The status is "
                       "NOT_DRAFTED, which is weaker than PENDING_APPROVAL: there is "
                       "nothing to approve."),
        dict(exposure_id="EX-07", subject="Anticipated interaction-state complexity",
             statement="Base states follow the screen floor. Triggered and total runtime "
                       "states are UNKNOWN_PENDING_EXTRACTION for every unit. T04's 65 "
                       "states are not carried over."),
    ]


def cross_unit_exceptions():
    return [
        dict(exception_id="XU-01", subject="B02 execution families",
             applies_to=["K5-PL06-T03-B03", "K5-PL06-T03-B04"],
             statement="Both units sit in Topik 3, B02's own Topik. RP-201 to RP-203 are "
                       "readings of B02's table structure, not a PL06 taxonomy, and "
                       "proximity is the reason they are most likely to be assumed here."),
        dict(exception_id="XU-02", subject="Shared module page 255",
             applies_to=["K5-PL06-T03-B03", "K5-PL06-T03-B04"],
             statement="Module page 255 carries the end of T03-B03 and the start of "
                       "T03-B04. Whichever unit is extracted first must stop at the named "
                       "heading, not at the page break."),
        dict(exception_id="XU-03", subject="Character cast",
             applies_to=BATCH_UNITS,
             statement="STOP-006 is open. T05-B01 is the only unit proposing a dialogue, "
                       "so it is the only one this immediately blocks — but any PINDA that "
                       "adds a dialogue elsewhere inherits the same block."),
        dict(exception_id="XU-04", subject="Boundary image custody",
             applies_to=BATCH_UNITS,
             statement="Only T05-B01's start page image (p302) is ingested in this "
                       "repository and was visually checked. T03-B03 (p268) and T06-B01 "
                       "(p312) are named in the freeze package by identity only. T03-B04's "
                       "start PDF page 273 has no image of its own in the package at all."),
        dict(exception_id="XU-05", subject="Stale unit lists on the open-items register",
             applies_to=["K5-PL06-T04-B01"],
             statement="STOP-003, STOP-004 and STOP-005 still list K5-PL06-T04-B01, which "
                       "has since been extracted. The register is a historical run artifact "
                       "and is not rewritten here; the divergence is recorded instead."),
    ]
