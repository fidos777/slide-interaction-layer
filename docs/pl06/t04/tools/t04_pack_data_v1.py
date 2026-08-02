# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.5 — the ONE controlled data source for the T04 pre-storyboard decision pack.

Everything here is a PROPOSAL. Nothing here is approved instructional content.

ROLE OWNERSHIP, enforced by gate throughout:
    CAIR / Claude Code   source analysis, source-to-screen mapping, draft preparation,
                         traceability, technical validation
    Bariah               SOLE Instructional Designer — instructional author and approval
                         authority; confirms treatment, approves or edits Rumusan, authors
                         or approves quiz content, approves narration and interaction
    Firdaus              project owner — delivery and scope authority

No CAIR-generated text may be labelled ID_AUTHORED, BARIAH_APPROVED or
FINAL_INSTRUCTIONAL_CONTENT. The only permitted labels are CAIR_ASSISTED_DRAFT and
PENDING_BARIAH_REVIEW.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import t04_data_v1 as SRC

STAGE = "4.2F-B0.5"
UNIT_ID = "K5-PL06-T04-B01"
GENERATED_BY = "docs/pl06/t04/tools/t04_pack_emit_v1.py"

CONTENT_STATUS = "CAIR_ASSISTED_DRAFT"
APPROVAL_STATUS = "PENDING_BARIAH_REVIEW"
INSTRUCTIONAL_AUTHORITY = "BARIAH"
FORBIDDEN_LABELS = ["ID_AUTHORED", "BARIAH_APPROVED", "FINAL_INSTRUCTIONAL_CONTENT",
                    "APPROVED", "FINAL"]

ROLES = dict(
    CAIR=["source analysis", "source-to-screen mapping", "draft preparation", "traceability",
          "technical validation"],
    BARIAH=["sole Instructional Designer", "instructional author and approval authority",
            "confirms screen treatment", "approves or edits Rumusan",
            "authors, edits or approves quiz content",
            "approves narration and interaction treatment"],
    FIRDAUS=["project owner", "delivery and scope authority",
             "confirms operational decisions where required"])

TREATMENT_STATUSES = ["PROPOSED", "PENDING_BARIAH_REVIEW", "SOURCE_BOUND",
                      "TECHNICALLY_SUPPORTED", "NEW_TREATMENT_REQUIRED"]

BY_ID = SRC.BY_ID


def _rows(*ids):
    missing = [i for i in ids if i not in BY_ID]
    if missing:
        raise RuntimeError(f"source rows not in the controlled extract: {missing}")
    return list(ids)


def _under(h2, kind=None):
    return [r["row_id"] for r in SRC.ROWS
            if len(r["heading_path"]) > 1 and r["heading_path"][1] == h2
            and (kind is None or r["content_type"] == kind)]


# The three Landskap Lembut operations and the four Landskap Kejur groups, bound by row id.
OP_SIRAM, OP_BAJA, OP_RACUN = "T04-ROW-006", "T04-ROW-026", "T04-ROW-046"
KEJUR_GROUPS = ["T04-ROW-081", "T04-ROW-086", "T04-ROW-091", "T04-ROW-096"]
LEGAL_ROWS = _rows("T04-ROW-065", "T04-ROW-066", "T04-ROW-067", "T04-ROW-068", "T04-ROW-069",
                   "T04-ROW-071", "T04-ROW-073", "T04-ROW-075", "T04-ROW-076", "T04-ROW-077",
                   "T04-ROW-078")

# ==========================================================================================
# PART 1 — SOURCE-TO-SCREEN MAPPING
# ==========================================================================================
MAPPING = [
    dict(screen_candidate_id="T04-SC-01", working_title="Aliran proses penjagaan dan penyelenggaraan",
         source_row_ids=_rows("T04-ROW-001", "T04-ROW-002", "T04-ROW-003"),
         source_heading_path=["PENJAGAAN DAN PENYELENGGARAAN"],
         instructional_purpose="Orient the learner to the six supervisory activities the "
                               "module names as the maintenance process, before any single "
                               "operation is taught.",
         learner_outcome="The learner can name the six activities and place them in order.",
         proposed_treatment="PROCESS_FLOW",
         source_visual_dependency="T04-DGM-01 — the unit's only visual",
         text_dependency="one introductory sentence, T04-ROW-002",
         interaction_dependency="none proposed for the base state",
         narration_dependency="one screen-level VO; the six node labels are the spoken spine",
         technical_claim_dependency="none",
         bariah_decision_required="D-05 SmartArt production",
         unresolved_issue="how a vector SmartArt part becomes a storyboard visual",
         reusable_capability="shell, production panel, Notes schema, screen-level VO",
         new_capability_required="PROCESS_FLOW screen type — B02 has none",
         treatment_status="NEW_TREATMENT_REQUIRED"),
    dict(screen_candidate_id="T04-SC-02", working_title="Landskap Lembut — tiga operasi penyelenggaraan",
         source_row_ids=_rows("T04-ROW-004", "T04-ROW-005", OP_SIRAM, OP_BAJA, OP_RACUN),
         source_heading_path=["PENJAGAAN DAN PENYELENGGARAAN", "Landskap Lembut"],
         instructional_purpose="Establish that soft-landscape maintenance is three named "
                               "operations, and let the learner take them one at a time.",
         learner_outcome="The learner can name Siram, Baja and Racun and state what each is for.",
         proposed_treatment="CLICK_TO_REVEAL",
         source_visual_dependency="NONE — no source visual exists for any of the three",
         text_dependency="section intro T04-ROW-005 plus one definition per operation",
         interaction_dependency="three reveals, one per operation; all-viewed completion",
         narration_dependency="screen-level instruction only",
         technical_claim_dependency="none on this screen — the compliance load routes to T04-SC-03",
         bariah_decision_required="D-01 visual treatment",
         unresolved_issue="whether three items justify a selection screen or three sequential screens",
         reusable_capability="completion-state treatment, all-viewed state, screen-level VO",
         new_capability_required="none",
         treatment_status="PROPOSED"),
    dict(screen_candidate_id="T04-SC-03", working_title="Racun — perundangan, HSE dan pengurusan risiko",
         source_row_ids=LEGAL_ROWS,
         source_heading_path=["PENJAGAAN DAN PENYELENGGARAAN", "Landskap Lembut", "Racun"],
         instructional_purpose="Carry the unit's entire compliance load — statute, licensing, "
                               "PPE, storage, SDS, spray conditions, notification, reporting.",
         learner_outcome="The learner can state the contractor's legal and HSE obligations "
                         "before pesticide work begins.",
         proposed_treatment="SEQUENTIAL_STEPS",
         source_visual_dependency="NONE",
         text_dependency="eleven source rows, verbatim",
         interaction_dependency="stepped progression; NO obligation gated behind an optional reveal",
         narration_dependency="high — this is the most assessable material in the unit",
         technical_claim_dependency="T04-CLM-01 Akta Racun Makhluk Perosak 1974, "
                                    "T04-CLM-02 licensed operator, T04-CLM-03 PPE, "
                                    "T04-CLM-04 SDS, T04-CLM-05 spray drift",
         bariah_decision_required="D-04 legislative content",
         unresolved_issue="whether legislative content may be reveal-gated at all",
         reusable_capability="Notes typed-block schema, production-instruction blocks",
         new_capability_required="none",
         treatment_status="PROPOSED"),
    dict(screen_candidate_id="T04-SC-04", working_title="Landskap Lembut berbanding Landskap Kejur",
         source_row_ids=_rows("T04-ROW-004", "T04-ROW-005", "T04-ROW-079", "T04-ROW-080",
                              "T04-ROW-100"),
         source_heading_path=["PENJAGAAN DAN PENYELENGGARAAN"],
         instructional_purpose="Make the unit's organising contrast explicit — living "
                               "horticultural elements against permanent built elements.",
         learner_outcome="The learner can distinguish soft from hard landscape and say why "
                         "each is maintained differently.",
         proposed_treatment="COMPARISON",
         source_visual_dependency="NONE",
         text_dependency="the two section definitions plus the source's own closing contrast "
                         "statement, T04-ROW-100",
         interaction_dependency="none proposed",
         narration_dependency="low",
         technical_claim_dependency="none",
         bariah_decision_required="D-01 visual treatment",
         unresolved_issue="whether the contrast earns a screen or is better left implicit",
         reusable_capability="shell and Notes only",
         new_capability_required="COMPARISON screen type — B02 has none",
         treatment_status="NEW_TREATMENT_REQUIRED"),
    dict(screen_candidate_id="T04-SC-05", working_title="Landskap Kejur — empat kumpulan fungsi",
         source_row_ids=_rows("T04-ROW-079", "T04-ROW-080", *KEJUR_GROUPS),
         source_heading_path=["PENJAGAAN DAN PENYELENGGARAAN", "Landskap Kejur"],
         instructional_purpose="Present the four functions hard landscape performs, each with "
                               "its two source sub-items.",
         learner_outcome="The learner can name the four functions and give an example of each.",
         proposed_treatment="CLICK_TO_REVEAL",
         source_visual_dependency="NONE",
         text_dependency="section intro plus four group headings and eight sub-items",
         interaction_dependency="four reveals; all-viewed completion",
         narration_dependency="screen-level instruction",
         technical_claim_dependency="none",
         bariah_decision_required="D-01 visual treatment",
         unresolved_issue="none anticipated",
         reusable_capability="completion-state treatment, all-viewed state",
         new_capability_required="none",
         treatment_status="PROPOSED"),
    dict(screen_candidate_id="T04-SC-06", working_title="Rumusan dan kuiz",
         source_row_ids=[],
         source_heading_path=[],
         instructional_purpose="Recap the unit and assess it.",
         learner_outcome="pending — depends on the assessment Bariah authors.",
         proposed_treatment="PENDING_HUMAN",
         source_visual_dependency="NONE",
         text_dependency="NONE IN SOURCE — the module contains no Rumusan and no quiz",
         interaction_dependency="quiz interaction structure exists in the shell",
         narration_dependency="follows the authored content",
         technical_claim_dependency="none",
         bariah_decision_required="D-02 quiz structure; Rumusan approval",
         unresolved_issue="content must be authored; 4+1 and 60% unconfirmed for PL06",
         reusable_capability="Rumusan and quiz-review STRUCTURES (RP-007, RP-008, RP-011)",
         new_capability_required="none — the structures exist, the content does not",
         treatment_status="PENDING_BARIAH_REVIEW"),
]

# Screen count is NOT claimed. Six candidates is not six screens.
SCREEN_COUNT_CLAIM = dict(
    final_screen_count="NOT_CLAIMED",
    reason="Six candidates are six treatments, not a sequence. T04-SC-04 may be dropped, "
           "T04-SC-02 may become three screens, and T04-SC-06 is two screens or none "
           "depending on what Bariah authors. A number here would be invented, and it would "
           "not be derived from B02 either — B02's 29 learner screens describe a different "
           "unit with a different structure.",
    derived_from_b02=False)

# ==========================================================================================
# PART 2 — SIX CANDIDATE SCREEN CONTRACTS
# ==========================================================================================
def _contract(cid, ctype, rows, purpose, base, states, completion, visual, text, vo, notes,
              access, fallback, authority, open_decision, **kw):
    d = dict(contract_id=cid, candidate_type=ctype, source_rows=rows,
             learner_facing_purpose=purpose, base_state=base, interaction_states=states,
             completion_condition=completion, visual_treatment=visual, text_treatment=text,
             vo_proposal=vo, speaker_notes_proposal=notes, accessibility_consideration=access,
             fallback_behaviour=fallback, source_authority=authority,
             open_decision=open_decision,
             bariah_approval=dict(status=APPROVAL_STATUS, decision=None, comment=None))
    d.update(kw)
    return d


CONTRACTS = [
    _contract(
        "T04-CT-01", "PROCESS_FLOW", _rows("T04-ROW-001", "T04-ROW-002", "T04-ROW-003"),
        "Show the six supervisory activities the module names as the maintenance process.",
        "Screen title, the source's introductory sentence, and the six-node process flow "
        "rendered in source order, all visible.",
        ["BASE only — no interaction proposed"],
        "screen viewed",
        "Source-bound reference to T04-DGM-01. Either a controlled redraw preserving the six "
        "nodes and their order, or a readable placeholder carrying the same six labels. No "
        "node invented, reordered or reworded.",
        "Introductory sentence verbatim; six node labels verbatim.",
        "One screen-level VO introducing the flow and naming the six activities in order. "
        "CAIR_ASSISTED_DRAFT — wording is Bariah's to set.",
        "NON_SPOKEN_CONTEXT: unit and page provenance. SPOKEN_CONTENT_VO: the introduction. "
        "PRODUCTION_INSTRUCTION_NOT_SPOKEN: SmartArt redraw instruction, six nodes, linear.",
        "The six labels must exist as selectable text, not only inside an image, so a screen "
        "reader can reach them. A flattened bitmap of the diagram would fail this.",
        "If the redraw is not ready, the screen still carries the six labels as an ordered "
        "text list — the meaning survives without the graphic.",
        "MODULE_SOURCE_ATTESTED — T04-DGM-01, six nodes measured from word/diagrams/data1.xml",
        "D-05 SmartArt production"),
    _contract(
        "T04-CT-02", "CLICK_TO_REVEAL",
        _rows("T04-ROW-004", "T04-ROW-005", OP_SIRAM, OP_BAJA, OP_RACUN),
        "Introduce the three soft-landscape maintenance operations.",
        "Section title, section definition, and three cards labelled Siram, Baja and Racun — "
        "all three LABELS visible before any interaction.",
        ["BASE", "SIRAM_REVEALED", "BAJA_REVEALED", "RACUN_REVEALED", "ALL_VIEWED"],
        "all three revealed",
        "NONE — no source visual exists for any of the three. Text-led.",
        "One definition per operation, verbatim from its source row.",
        "Screen-level instruction only, in the B02 pattern. CAIR_ASSISTED_DRAFT.",
        "SPOKEN_INTERACTION_INSTRUCTION for the screen-level instruction; "
        "SPOKEN_CONTENT_VO per revealed definition.",
        "Reveals must be keyboard reachable and their state announced. The all-viewed state "
        "must not be the only route to the next screen.",
        "If reveal is not available, the three definitions render stacked. Nothing is lost.",
        "MODULE_SOURCE_ATTESTED",
        "D-01 visual treatment",
        hidden_content_classification="SUPPLEMENTARY",
        hidden_content_justification=
        "What is hidden is the DEFINITION of each operation — descriptive expansion of a "
        "label already on screen. No legal, safety or compliance obligation is behind any "
        "reveal on this screen: all eleven of those rows sit on T04-CT-04, where they are "
        "visible in the base state. This separation is deliberate and is gated by "
        "LEGAL_ROWS_NOT_GATED_BEHIND_OPTIONAL_REVEAL."),
    _contract(
        "T04-CT-03", "CLICK_TO_REVEAL",
        _rows("T04-ROW-079", "T04-ROW-080", *KEJUR_GROUPS),
        "Present the four functions hard landscape performs.",
        "Section title, section definition, and four group labels — all visible.",
        ["BASE", "GROUP_1_REVEALED", "GROUP_2_REVEALED", "GROUP_3_REVEALED",
         "GROUP_4_REVEALED", "ALL_VIEWED"],
        "all four revealed",
        "NONE — text-led.",
        "Two source sub-items per group, verbatim.",
        "Screen-level instruction only. CAIR_ASSISTED_DRAFT.",
        "SPOKEN_INTERACTION_INSTRUCTION plus per-group SPOKEN_CONTENT_VO.",
        "As T04-CT-02.",
        "Stacked rendering; nothing lost.",
        "MODULE_SOURCE_ATTESTED",
        "D-01 visual treatment",
        hidden_content_classification="SUPPLEMENTARY",
        hidden_content_justification=
        "Purely descriptive expansion — examples of walls, pathways, retaining walls, "
        "drainage, patios, decks, gazebos. No obligation of any kind is on this screen."),
    _contract(
        "T04-CT-04", "SEQUENTIAL_STEPS", LEGAL_ROWS,
        "Carry the contractor's legal, HSE and risk obligations for pesticide work.",
        "ALL obligation headings visible in the base state: Perundangan dan Pelesenan, "
        "Keselamatan dan Kesihatan (HSE), Pengurusan Risiko. The Akta Racun Makhluk Perosak "
        "1974 citation and the licensed-operator requirement are on the base state, not "
        "behind an interaction.",
        ["BASE (all obligations visible)", "STEP_DETAIL_1", "STEP_DETAIL_2", "STEP_DETAIL_3",
         "ALL_VIEWED"],
        "all steps stepped through; the base state already discharges the disclosure",
        "NONE.",
        "Eleven source rows verbatim. No paraphrase of a legal obligation.",
        "Screen-level instruction; each obligation spoken. CAIR_ASSISTED_DRAFT.",
        "PRODUCTION_INSTRUCTION_NOT_SPOKEN recording that this screen carries legal content "
        "and must not be abbreviated in MMD.",
        "Legal content must be reachable without interaction and must not depend on colour or "
        "hover alone.",
        "If stepping is unavailable, every obligation still renders. That is the point of "
        "putting them in the base state.",
        "MODULE_SOURCE_ATTESTED — verbatim; the 1974 Act citation is "
        "EXTERNAL_VERIFICATION_REQUIRED and is quoted, not asserted",
        "D-04 legislative content",
        hidden_content_classification="NOT_APPLICABLE_NOTHING_MANDATORY_IS_HIDDEN",
        hidden_content_justification=
        "Stepping adds emphasis and pacing. It gates nothing: every obligation is in the base "
        "state. A learner who never interacts still sees all of them."),
    _contract(
        "T04-CT-05", "COMPARISON",
        _rows("T04-ROW-004", "T04-ROW-005", "T04-ROW-079", "T04-ROW-080", "T04-ROW-100"),
        "Make explicit the contrast the source itself draws between soft and hard landscape.",
        "Two columns, one per section, each carrying its source definition, with the source's "
        "own closing contrast statement beneath.",
        ["BASE only"],
        "screen viewed",
        "NONE.",
        "Two section definitions and T04-ROW-100 verbatim.",
        "One short screen-level VO. CAIR_ASSISTED_DRAFT.",
        "NON_SPOKEN_CONTEXT plus one SPOKEN_CONTENT_VO block.",
        "A two-column layout must linearise in reading order, not column-by-column visually.",
        "Single-column stack, soft then hard.",
        "MODULE_SOURCE_ATTESTED",
        "D-01 visual treatment — and whether this screen is wanted at all"),
    _contract(
        "T04-CT-06", "PENDING_HUMAN", [],
        "Recap and assess the unit.",
        "NOT PROPOSED — no treatment is chosen here.",
        ["PENDING"],
        "PENDING",
        "NONE.",
        "NONE IN SOURCE.",
        "PENDING.",
        "PENDING.",
        "PENDING.",
        "PENDING.",
        "NO_SOURCE — the module contains no Rumusan and no assessment items anywhere",
        "D-02 quiz structure; Rumusan approval",
        options=[
            dict(option="A", label="Rumusan screen + quiz block, B02 shape",
                 grounding="The A3 Style and Guidelines defines both treatments and B02 "
                           "implements them. Structure is proven; only content is missing.",
                 tradeoff="Fastest and most consistent with B02. But it imports the 4 MCQ + "
                          "1 MR shape and the 60% threshold, both of which are A3-scoped to "
                          "B02 and unconfirmed for PL06. Choosing this settles D-02 by "
                          "default rather than deliberately."),
            dict(option="B", label="Rumusan screen + assessment sized to T04's coverage",
                 grounding="T04 has a countable set of assessable learning points — three "
                           "soft-landscape operations, four hard-landscape functions, and one "
                           "compliance cluster. The blueprint counts them from source rows.",
                 tradeoff="Assessment matches what the unit actually teaches, and the "
                          "compliance material gets weight proportional to its risk. But it "
                          "breaks uniformity across PL06 units unless Bariah sets a rule, and "
                          "it needs a threshold decision that A3 does not supply."),
            dict(option="C", label="Rumusan screen only, assessment deferred to Topik level",
                 grounding="Topik 4 has exactly one Bahagian, so a unit quiz and a topic quiz "
                           "would assess the same content twice.",
                 tradeoff="Avoids duplicate assessment and is defensible for a single-lesson "
                          "Topik. But it makes T04 structurally different from B02, and no "
                          "artifact establishes that a Topik-level assessment exists or is "
                          "planned."),
        ]),
]

# ==========================================================================================
# PART 3 — SMARTART SIX-NODE CONTRACT
# ==========================================================================================
_A = SRC.ASSETS[0]
SMARTART = dict(
    asset_id=_A["asset_id"],
    asset_sha256=_A["sha256"],
    relationship_id=_A["relationship_id"],
    embedded_part=_A["embedded_filename"],
    source_page=_A["module_page"],
    source_paragraph=_A["source_paragraph"],
    source_row="T04-ROW-003",
    original_dimensions_in=_A["dimensions_in"],
    node_count=_A["node_count"],
    nodes=list(_A["source_subject_nodes"]),
    node_sequence="document order in word/diagrams/data1.xml, preserved exactly",
    directional_flow="LINEAR_LEFT_TO_RIGHT",
    flow_evidence="layout1.xml declares urn:microsoft.com/office/officeart/2005/8/layout/"
                  "process2 with algorithms lin (linear) and conn (connector)",
    connectors="6 sibTrans sibling transitions — the connectors a process2 layout draws "
               "between consecutive nodes",
    hierarchy="NONE — flat. All six nodes are parOf the single doc root; zero parOf links "
              "exist between text nodes, so no node is subordinate to another.",
    source_authority="MODULE_SOURCE_ATTESTED",
    caption="NONE — the diagram carries no caption in the source",
    treatment_status="PENDING_BARIAH_REVIEW",
    review_storyboard_treatment=dict(
        approach="SOURCE_BOUND_DIAGRAM_REFERENCE",
        rules=["reference T04-DGM-01 by asset id and SHA-256",
               "render either a controlled redraw or a readable placeholder carrying all six "
               "labels",
               "no invented nodes", "no reordered nodes", "no altered meaning",
               "the six labels must be reachable as text"],
        asset_production="NOT_STARTED"),
    future_mmd_treatment=dict(
        approach="CONTROLLED_REDRAW",
        rules=["redraw as a controlled process diagram",
               "preserve the six-node sequence exactly",
               "preserve the linear directional relationship",
               "no hierarchy may be introduced — the source has none"],
        asset_production="NOT_STARTED_IN_THIS_STAGE"))

# ==========================================================================================
# PART 4 — CAIR-ASSISTED RUMUSAN DRAFT
# ==========================================================================================
RUMUSAN = dict(
    content_status=CONTENT_STATUS,
    instructional_authority=INSTRUCTIONAL_AUTHORITY,
    approval_status=APPROVAL_STATUS,
    provenance="Every statement below is a compression of rows already in the controlled "
               "extract. No fact is added, no external source is consulted, and nothing "
               "generalises beyond what the module states. This did NOT come from the "
               "module — the module has no Rumusan.",
    statements=[
        dict(statement_id="T04-RUM-01",
             draft_text="Penjagaan dan penyelenggaraan landskap merangkumi enam aktiviti "
                        "penyeliaan, daripada koordinasi dan demonstrasi sehingga perancangan "
                        "sumber manusia.",
             source_row_ids=_rows("T04-ROW-002", "T04-ROW-003"),
             source_heading="PENJAGAAN DAN PENYELENGGARAAN",
             reason_for_inclusion="Frames the unit with the process the source opens on.",
             simplification_applied="Names the first and last of the six nodes rather than "
                                    "listing all six, to keep the recap short.",
             factual_risk_status="LOW — the six nodes and their order are in T04-DGM-01"),
        dict(statement_id="T04-RUM-02",
             draft_text="Landskap lembut merujuk kepada elemen hortikultur dan hidupan, dan "
                        "diselenggara melalui tiga operasi utama: siram, baja dan racun.",
             source_row_ids=_rows("T04-ROW-005", OP_SIRAM, OP_BAJA, OP_RACUN),
             source_heading="Landskap Lembut",
             reason_for_inclusion="The organising structure of the unit's first half.",
             simplification_applied="States the three operations as a set; the source "
                                    "presents them sequentially with full definitions.",
             factual_risk_status="LOW"),
        dict(statement_id="T04-RUM-03",
             draft_text="Bagi setiap operasi, kontraktor bertanggungjawab ke atas kaedah "
                        "pelaksanaan, jadual kerja, pematuhan spesifikasi, keselamatan "
                        "pekerja dan dokumentasi.",
             source_row_ids=_rows("T04-ROW-016", "T04-ROW-017", "T04-ROW-035", "T04-ROW-038",
                                  "T04-ROW-042", "T04-ROW-044", "T04-ROW-064"),
             source_heading="Aspek Pengurusan untuk Kontraktor",
             reason_for_inclusion="The recurring contractor-responsibility frame appears "
                                  "under all three operations.",
             simplification_applied="Collapses the three separate Aspek Pengurusan blocks "
                                    "into one statement of the shared pattern.",
             factual_risk_status="MEDIUM — this is a pattern the source repeats but never "
                                 "states as a general rule. Bariah should confirm the "
                                 "generalisation is acceptable."),
        dict(statement_id="T04-RUM-04",
             draft_text="Penggunaan racun dikawal oleh perundangan dan memerlukan pengendali "
                        "berlesen, PPE yang lengkap, penyimpanan berkunci, Helaian Data "
                        "Keselamatan dan rekod semburan.",
             source_row_ids=_rows("T04-ROW-066", "T04-ROW-067", "T04-ROW-069", "T04-ROW-071",
                                  "T04-ROW-073", "T04-ROW-078"),
             source_heading="Racun › Aspek Pengurusan untuk Kontraktor",
             reason_for_inclusion="The unit's highest-consequence content; a recap that "
                                  "omitted it would misrepresent the lesson.",
             simplification_applied="Does not name the statute. The Act and its year stay on "
                                    "the screen that carries them, where the citation is "
                                    "verbatim and flagged for verification.",
             factual_risk_status="LOW as worded — deliberately says 'perundangan' rather than "
                                 "naming an Act in a recap"),
        dict(statement_id="T04-RUM-05",
             draft_text="Landskap kejur merujuk kepada elemen binaan kekal, dan menyumbang "
                        "kepada pengurusan ruang, fungsi struktur, kebolehgunaan dan estetika.",
             source_row_ids=_rows("T04-ROW-080", *KEJUR_GROUPS),
             source_heading="Landskap Kejur",
             reason_for_inclusion="The organising structure of the unit's second half.",
             simplification_applied="Names the four function groups without their eight "
                                    "sub-items.",
             factual_risk_status="LOW"),
    ],
    review_table_columns=["accept", "edit", "remove", "comment"],
    length_note="Five statements, one per structural block. Short enough to read as a recap "
                "rather than a second lesson.")

# ==========================================================================================
# PART 5 — QUIZ BLUEPRINT ONLY
# ==========================================================================================
QUIZ = dict(
    quiz_structure="AUTHORITY_UNRESOLVED",
    quiz_content="BLUEPRINT_ONLY",
    final_author="BARIAH",
    approval_status=APPROVAL_STATUS,
    not_produced=["final stems", "final answer options", "final answer key", "final rationale",
                  "approved feedback", "confirmed 4 MCQ + 1 MR structure",
                  "confirmed 60 percent threshold"],
    blueprint=[
        dict(blueprint_id="T04-QB-01",
             learning_point="The three soft-landscape maintenance operations",
             source_rows=_rows(OP_SIRAM, OP_BAJA, OP_RACUN),
             proposed_question_type="MCQ or MR", cognitive_demand="RECALL",
             misconception_to_test="that maintenance is only watering",
             evidence_for_correct_answer="three named Heading-3 operations under Landskap Lembut",
             suitability="MR if all three must be identified; MCQ if one is asked for",
             bariah_decision_required="which form"),
        dict(blueprint_id="T04-QB-02",
             learning_point="Irrigation method selection",
             source_rows=_rows("T04-ROW-012", "T04-ROW-013", "T04-ROW-014", "T04-ROW-015"),
             proposed_question_type="MCQ", cognitive_demand="APPLICATION",
             misconception_to_test="that sprinkler and drip are interchangeable",
             evidence_for_correct_answer="the source states sprinkler suits large turf areas "
                                         "and drip suits individual trees and shrubs",
             suitability="MCQ — the source gives a clear one-best-answer distinction",
             bariah_decision_required="whether application-level demand is appropriate here"),
        dict(blueprint_id="T04-QB-03",
             learning_point="Pesticide legal and licensing obligations",
             source_rows=_rows("T04-ROW-066", "T04-ROW-067"),
             proposed_question_type="MCQ", cognitive_demand="RECALL",
             misconception_to_test="that any worker may spray pesticide",
             evidence_for_correct_answer="the source states spraying requires a licensed "
                                         "operator and is governed by statute",
             suitability="MCQ",
             bariah_decision_required="whether to name the Act in a question stem given that "
                                      "T04-CLM-01 is EXTERNAL_VERIFICATION_REQUIRED"),
        dict(blueprint_id="T04-QB-04",
             learning_point="HSE controls for pesticide work",
             source_rows=_rows("T04-ROW-069", "T04-ROW-071", "T04-ROW-073", "T04-ROW-076"),
             proposed_question_type="MR", cognitive_demand="RECALL",
             misconception_to_test="that PPE alone is sufficient compliance",
             evidence_for_correct_answer="four distinct controls: PPE, locked storage, SDS "
                                         "retention, calm-weather spraying",
             suitability="MR — the source gives several co-required controls",
             bariah_decision_required="none anticipated"),
        dict(blueprint_id="T04-QB-05",
             learning_point="IPM control priority order",
             source_rows=_rows("T04-ROW-048", "T04-ROW-049", "T04-ROW-051", "T04-ROW-053",
                               "T04-ROW-055"),
             proposed_question_type="MCQ", cognitive_demand="UNDERSTANDING",
             misconception_to_test="that chemical control is the first response",
             evidence_for_correct_answer="the source lists cultural, physical and biological "
                                         "control before chemical",
             suitability="MCQ",
             bariah_decision_required="none anticipated"),
        dict(blueprint_id="T04-QB-06",
             learning_point="The four functions of hard landscape",
             source_rows=list(KEJUR_GROUPS),
             proposed_question_type="MCQ or MR", cognitive_demand="RECALL",
             misconception_to_test="that hard landscape is decorative only",
             evidence_for_correct_answer="four named function groups, one of which is "
                                         "explicitly structural and engineering",
             suitability="either",
             bariah_decision_required="which form"),
    ],
    structure_options=[
        dict(option="A", label="4 MCQ + 1 MR",
             advantages="Identical to B02, so the shell, the quiz-review structure and the "
                        "feedback wording carry across with nothing to decide. Consistent "
                        "learner experience across PL06.",
             constraints="A3 specifies it for B02 and no artifact extends it to PL06. Six "
                         "blueprint points would have to be cut to five, and the compliance "
                         "cluster — the unit's highest-risk material — would get the same "
                         "weight as a recall item."),
        dict(option="B", label="Structure sized to T04's actual coverage",
             advantages="Assessment matches what the unit teaches. The compliance material "
                        "(QB-03, QB-04) can carry the weight its risk warrants, and the two "
                        "natural MR points are not forced into MCQ.",
             constraints="Breaks uniformity unless Bariah sets a rule for how structure is "
                         "derived per unit. Needs a pass-threshold decision A3 does not "
                         "supply for a variable-length quiz."),
    ])

# ==========================================================================================
# PART 6 — TARGETED DECISION PACK
# ==========================================================================================
DECISIONS = [
    dict(decision_id="D-01", title="Visual treatment",
         current_source_evidence="T04 contains ONE visual — the opening SmartArt process "
                                 "diagram — and ZERO raster images. B02 had 14 extracted "
                                 "photographs bound to source rows.",
         recommendation="TEXT_AND_DIAGRAM_LED — photographs are unnecessary for this unit; "
                        "the SmartArt is the primary visual; text, process and comparison "
                        "layouts carry the rest.",
         alternative="Commission photographs for the soft- and hard-landscape operations.",
         consequence_recommended="The unit ships without photographs. B02's source-bound "
                                 "overview treatment does not apply here, so no subject has "
                                 "to be invented to satisfy it.",
         consequence_alternative="New assets must be sourced or produced, and every subject "
                                 "would be chosen by a human rather than bound to a source "
                                 "row — a different authority model from B02.",
         scope="THIS_UNIT_ONLY", affected_screens=["T04-CT-01", "T04-CT-02", "T04-CT-03",
                                                   "T04-CT-05"],
         approval=None, comments=None),
    dict(decision_id="D-02", title="Quiz structure",
         current_source_evidence="Zero quiz items anywhere in the module — 0 hits for "
                                 "'Soalan', 'Kuiz' and 'Jawapan' across all 6,167 body "
                                 "paragraphs. 4 MCQ + 1 MR and the 60% threshold appear only "
                                 "in A3, which is the B02 slice of the Style and Guidelines.",
         recommendation="Confirm explicitly whether 4 MCQ + 1 MR and 60% are PL06-wide rules "
                        "or were B02-specific. No default is applied here.",
         alternative="Structure sized to T04's coverage — see the blueprint's Option B.",
         consequence_recommended="One answer settles the shape of every remaining PL06 quiz.",
         consequence_alternative="Per-unit variation, which needs a derivation rule so it "
                                 "does not become arbitrary.",
         scope="POTENTIALLY_PL06_WIDE — that is precisely what is being asked",
         affected_screens=["T04-CT-06"], approval=None, comments=None),
    dict(decision_id="D-03", title="Cast",
         current_source_evidence="The ratified character bank marks Hilmi LOCKED course "
                                 "narrator (VO-only) and Haziq / Encik Roslan CANONICAL. B02 "
                                 "ships Alya and Encik Rahman. Bariah's PL06-wide answer names "
                                 "neither pair.",
         recommendation="HILMI_NARRATOR_LED and NO_ADDITIONAL_CHARACTERS_FOR_T04 — T04 is "
                        "procedural content with no dialogue scenario in the source.",
         alternative="Introduce a named pair for T04, either B02's or the ratified pair.",
         consequence_recommended="T04 needs no cast decision to proceed, and the PL06-wide "
                                 "cast question stays open rather than being settled by "
                                 "default on a unit that does not need it.",
         consequence_alternative="Settles the cast question on the wrong evidence — a unit "
                                 "with no dialogue is a poor place to choose a cast for PL06.",
         scope="THIS_UNIT_ONLY — explicitly NOT a PL06-global cast decision",
         affected_screens=["all"], approval=None, comments=None),
    dict(decision_id="D-04", title="Legislative content",
         current_source_evidence="Eleven source rows carry statute, licensing, PPE, storage, "
                                 "SDS, spray conditions, notification and reporting "
                                 "obligations.",
         recommendation="Core legal obligations visible on the base screen; supplementary "
                        "explanation may use reveal interaction.",
         alternative="Gate the obligations behind reveals for pacing.",
         consequence_recommended="A learner who never interacts still sees every obligation. "
                                 "T04-CT-04 is built this way.",
         consequence_alternative="Compliance content becomes optional in practice, which is "
                                 "a risk the storyboard should not take on Bariah's behalf.",
         scope="THIS_UNIT_ONLY, with an obvious read-across to any unit carrying regulated "
               "content",
         affected_screens=["T04-CT-04"], approval=None, comments=None),
    dict(decision_id="D-05", title="SmartArt production",
         current_source_evidence="One SmartArt part, six nodes, flat, linear process2 layout. "
                                 "It is vector XML, not an image, so it cannot be extracted as "
                                 "a JPEG the way B02's 14 assets were.",
         recommendation="Source-bound diagram reference in the review storyboard; controlled "
                        "redraw by MMD later; six-node sequence unchanged.",
         alternative="Screenshot the rendered diagram and embed it as an image.",
         consequence_recommended="The six labels stay as text — reachable, translatable and "
                                 "checkable against the source.",
         consequence_alternative="A flattened image loses text reachability and cannot be "
                                 "verified against the source without re-rendering.",
         scope="THIS_UNIT_ONLY", affected_screens=["T04-CT-01"], approval=None, comments=None),
]

# ==========================================================================================
# PART 8 — PORTABILITY MEASUREMENT TEMPLATE
# ==========================================================================================
PORTABILITY_METRICS = [
    "source extraction time", "source reconciliation time", "B02 shell reuse percentage",
    "Notes grammar reuse percentage", "interaction component reuse percentage",
    "visual-treatment reuse percentage", "QA gate reuse percentage", "new gate count",
    "new component count", "new human-decision count", "generator adaptation time",
    "QA and mutation time", "render inspection time", "PowerPoint smoke time",
    "Bariah review time", "total working time",
]
PORTABILITY_BANDS = [
    ("80–100%", "high reuse, possible 2–3 lessons per day"),
    ("60–79%", "moderate reuse, likely 1–2 lessons per day"),
    ("40–59%", "low reuse, approximately 1 lesson per day"),
    ("below 40%", "each lesson requires substantial adaptation"),
]
PORTABILITY_TEMPLATE = dict(
    status="TEMPLATE_NOT_YET_MEASURED",
    score="NOT_CALCULATED",
    rows=[dict(metric=m, value="NOT_MEASURED", basis="") for m in PORTABILITY_METRICS],
    rule="Every value stays NOT_MEASURED until a real T04 storyboard run produces it. Two of "
         "these — source extraction time and PowerPoint smoke time — already have honest "
         "positions from earlier stages, and even those are left blank here so the template "
         "cannot be mistaken for a result.")

VERDICT = "T04_PRE_STORYBOARD_DECISION_PACK_READY_FOR_BARIAH"
