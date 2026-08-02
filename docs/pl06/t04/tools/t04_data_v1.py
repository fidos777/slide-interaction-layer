# -*- coding: utf-8 -*-
"""Stage 4.2F-B0 — the analysis layer over the frozen T04 extract.

`T04_SOURCE_EXTRACT_v1.json` is the controlled data source; this module reads it and adds
only what analysis can defend: external-claim classification, Rumusan/quiz coverage, screen
candidates, source gaps and readiness. It asserts no content of its own — every claim below
points at a row id that exists in the extract.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
EXTRACT = os.path.join(T04, "T04_SOURCE_EXTRACT_v1.json")

STAGE = "4.2F-B0"
UNIT_ID = "K5-PL06-T04-B01"
GENERATED_BY = "docs/pl06/t04/tools/t04_emit_v1.py"


class ExtractMissing(RuntimeError):
    """Fail closed rather than analyse an absent source."""


def _load():
    if not os.path.exists(EXTRACT):
        raise ExtractMissing(f"controlled extract missing: {EXTRACT}")
    return json.load(open(EXTRACT, encoding="utf-8"))


EX = _load()
ROWS = EX["rows"]
ASSETS = EX["assets"]
LISTS = EX["lists"]
TABLES = EX["tables"]
TOTALS = EX["totals"]
BOUNDARY = EX["boundary"]
PROBE = EX["docx_probe"]

BY_ID = {r["row_id"]: r for r in ROWS}


def rows_matching(*needles):
    out = []
    for r in ROWS:
        t = r["raw_source_text"]
        if any(n.lower() in t.lower() for n in needles):
            out.append(r["row_id"])
    return out


# ==========================================================================================
# PART 6 — RUMUSAN AND QUIZ COVERAGE
# ==========================================================================================
COVERAGE_STATUSES = ["SOURCE_AVAILABLE", "SOURCE_AVAILABLE_ELSEWHERE", "NOT_FOUND",
                     "AUTHORITY_UNRESOLVED"]

# Measured across the WHOLE module DOCX at extraction time, not only inside T04:
#   "Rumusan"  0 hits    "Kuiz"  0 hits    "Soalan"  0 hits
MODULE_WIDE_SEARCH = dict(
    scope="entire module DOCX body, all 6,167 body-level paragraphs",
    terms={"Rumusan": 0, "Kuiz": 0, "Soalan": 0},
    within_t04={"rumusan": False, "kesimpulan": False, "soalan": False, "kuiz": False,
                "jawapan": False, "penilaian": False})

QUIZ_COVERAGE = [
    dict(item="Rumusan", status="NOT_FOUND",
         evidence="Zero occurrences of 'Rumusan' or 'Kesimpulan' inside T04, and zero "
                  "occurrences of 'Rumusan' anywhere in the module DOCX.",
         implication="B02's Rumusan was never module content. It was authored under the "
                     "Style and Guidelines, which specifies the TREATMENT — summarise this "
                     "Bahagian only, contractor perspective, no Kepentingan/Isi Utama/Manfaat "
                     "labels — and supplies no text. The same will be true for T04.",
         authority="A3 Updated S&G v0.3 governs the treatment; the CONTENT has no source",
         blocks="BLOCKS_THIS_UNIT until authored and signed off"),
    dict(item="Key takeaways", status="NOT_FOUND",
         evidence="No summary, bullet recap or takeaway block in the 100 extracted rows.",
         implication="Same position as Rumusan.",
         authority="none", blocks="BLOCKS_THIS_UNIT"),
    dict(item="MCQ questions", status="NOT_FOUND",
         evidence="Zero occurrences of 'Soalan' or 'Kuiz' anywhere in the module DOCX.",
         implication="The module carries no assessment items of any kind, for any unit.",
         authority="none", blocks="BLOCKS_THIS_UNIT"),
    dict(item="Multiple-response question", status="NOT_FOUND",
         evidence="As above.", implication="As above.", authority="none",
         blocks="BLOCKS_THIS_UNIT"),
    dict(item="Answer keys", status="NOT_FOUND",
         evidence="Zero occurrences of 'Jawapan' inside T04 and no answer construct anywhere.",
         implication="Nothing to derive a key from. Inventing one is prohibited.",
         authority="none", blocks="BLOCKS_THIS_UNIT"),
    dict(item="Feedback wording", status="SOURCE_AVAILABLE_ELSEWHERE",
         evidence="'Pilihan jawapan tepat.' / 'Pilihan jawapan tidak tepat.' were ruled "
                  "directly by Bariah at Stage 4.2E-A (decision D3) and are recorded in "
                  "QUIZ_FEEDBACK_REGISTER_v0.4.4.json.",
         implication="Portable as rule RP-011, PL06_GLOBAL_REUSABLE. Nothing to author.",
         authority="BARIAH_DIRECT_SCREENSHOT", blocks="none"),
    dict(item="4 MCQ + 1 MR composition", status="AUTHORITY_UNRESOLVED",
         evidence="Specified in A3, which is the B02 slice of the Style and Guidelines. No "
                  "artifact states that the composition applies to every PL06 unit.",
         implication="Recorded as rules RP-009 with human_authority_required = VERIFY. It must "
                     "NOT be assumed for T04.",
         authority="A3, scope unconfirmed", blocks="BLOCKS_THIS_UNIT until confirmed"),
    dict(item="60 percent pass threshold", status="AUTHORITY_UNRESOLVED",
         evidence="Same as above — A3 only.",
         implication="Same as above. RP-010.",
         authority="A3, scope unconfirmed", blocks="BLOCKS_THIS_UNIT until confirmed"),
]

# ==========================================================================================
# PART 7 — EXTERNAL AND TECHNICAL CLAIMS
# ==========================================================================================
CLAIM_STATUSES = ["SOURCE_STATEMENT_ONLY", "EXTERNAL_VERIFICATION_REQUIRED",
                  "BARIAH_CONFIRMATION_REQUIRED", "SAFE_FOR_REVIEW_DECK",
                  "BLOCKS_CANONICAL_FREEZE", "BLOCKS_THIS_UNIT"]


def _c(cid, kind, rows, quote, status, scope, note):
    return dict(claim_id=cid, kind=kind, row_ids=rows, quote=quote, status=status,
                scope=scope, note=note)


EXTERNAL_CLAIMS = [
    _c("T04-CLM-01", "LEGISLATION", rows_matching("Akta Racun Makhluk Perosak"),
       "Penggunaan racun kimia dikawal oleh Akta Racun Makhluk Perosak 1974.",
       "EXTERNAL_VERIFICATION_REQUIRED", "BLOCKS_CANONICAL_FREEZE",
       "A named statute with a year. The module states it; we have not verified that the 1974 "
       "Act is still the governing instrument or that it has not been amended. Safe to render "
       "in a review deck as a source statement; not safe to freeze as canonical fact."),
    _c("T04-CLM-02", "LICENSING", rows_matching("pengendali racun berlesen"),
       "Kontraktor mesti memastikan pekerja yang menjalankan semburan racun adalah pengendali "
       "racun berlesen …",
       "EXTERNAL_VERIFICATION_REQUIRED", "BLOCKS_CANONICAL_FREEZE",
       "A licensing obligation placed on the contractor. Same treatment as CLM-01."),
    _c("T04-CLM-03", "SAFETY_PROCEDURE", rows_matching("PPE"),
       "PPE requirements for fertiliser and pesticide handling — gloves, face mask, "
       "respirator, safety glasses.",
       "SOURCE_STATEMENT_ONLY", "SAFE_FOR_REVIEW_DECK",
       "Generic protective-equipment guidance, stated by the module, carrying no numeric "
       "threshold or standard reference. Renders as source content."),
    _c("T04-CLM-04", "SAFETY_DOCUMENT", rows_matching("Helaian Data Keselamatan", "SDS"),
       "Kontraktor wajib menyimpan Salinan SDS untuk setiap racun yang digunakan di tapak …",
       "SOURCE_STATEMENT_ONLY", "SAFE_FOR_REVIEW_DECK",
       "An SDS-retention obligation. Stated as module content; no external document is cited "
       "by number."),
    _c("T04-CLM-05", "CHEMICAL_HANDLING", rows_matching("spray drift", "cuaca tenang"),
       "Semburan hanya boleh dilakukan semasa cuaca tenang (tidak berangin) untuk mengelakkan "
       "spray drift.",
       "SOURCE_STATEMENT_ONLY", "SAFE_FOR_REVIEW_DECK",
       "A qualitative operating condition with no measured wind threshold. Note for the "
       "storyboard: do not tighten 'cuaca tenang' into a number."),
    _c("T04-CLM-06", "MAINTENANCE_FREQUENCY", rows_matching("awal pagi atau lewat petang"),
       "Amalan terbaik adalah menyiram pada awal pagi atau lewat petang …",
       "SOURCE_STATEMENT_ONLY", "SAFE_FOR_REVIEW_DECK",
       "A timing practice, not a frequency figure. The module explicitly defers the actual "
       "frequency to plant type, weather and growth stage rather than stating a number."),
    _c("T04-CLM-07", "TECHNICAL_FRAMEWORK", rows_matching("IPM"),
       "IPM — Integrated Pest Management, prioritising cultural, physical, biological and "
       "then chemical control.",
       "SOURCE_STATEMENT_ONLY", "SAFE_FOR_REVIEW_DECK",
       "A named industry framework used descriptively. The four-tier priority order is the "
       "module's own statement."),
    _c("T04-CLM-08", "CONTRACT_AUTHORITY", rows_matching("Pegawai Penguasa"),
       "… seperti yang ditetapkan dalam dokumen kontrak atau diluluskan oleh Pegawai Penguasa.",
       "SOURCE_STATEMENT_ONLY", "SAFE_FOR_REVIEW_DECK",
       "A contractual role reference, internal to the module's own frame."),
    _c("T04-CLM-09", "STANDARDS_REFERENCE", [],
       "No Malaysian Standard is cited anywhere in T04.",
       "SOURCE_STATEMENT_ONLY", "SAFE_FOR_REVIEW_DECK",
       "Recorded as a NEGATIVE finding, deliberately. MS2680 belongs to B02 and appears "
       "nowhere in this unit, so the open MS2680 item does not touch T04. A global open item "
       "must not block unrelated content."),
]

# ==========================================================================================
# PART 8 — SCREEN AND INTERACTION CANDIDATES
# ==========================================================================================
CANDIDATE_TYPES = ["STATIC_CONTENT", "SEQUENTIAL_STEPS", "CLICK_TO_REVEAL", "COMPARISON",
                   "PROCESS_FLOW", "TABLE_PRESENTATION", "VISUAL_FOCUS", "EXAMPLE_SELECTION",
                   "PENDING_HUMAN"]

B02_FORBIDDEN = ["FAMILY_S", "FAMILY_P1", "FAMILY_P2", "Papan Tanda", "BBQ Pit",
                 "Alya", "Encik Rahman"]


def _h3_under(h2):
    return [r["row_id"] for r in ROWS
            if r["content_type"] == "HEADING_3" and len(r["heading_path"]) > 1
            and r["heading_path"][1] == h2]


SCREEN_CANDIDATES = [
    dict(candidate_id="T04-SC-01", candidate="PROCESS_FLOW",
         title="Aliran proses penjagaan dan penyelenggaraan",
         source_rows=[r["row_id"] for r in ROWS if r["content_type"] == "DIAGRAM"]
                     + rows_matching("aliran proses penjagaan"),
         reason="The unit opens with a sentence introducing a process flow and a SmartArt "
                "diagram carrying six named nodes. The flow is source-drawn, not inferred.",
         reusable_capability="the B02 shell, Notes schema and production panel carry it; the "
                             "six nodes are source-bound subjects",
         new_treatment_required="YES — B02 has no process-flow screen type. Its visual "
                                "treatment is a source-bound overview of PHOTOGRAPHS; this is "
                                "a vector diagram with ordered nodes.",
         human_decision_required="how a SmartArt diagram is rendered for MMD — re-drawn, "
                                 "exported, or rebuilt as six sequential reveals",
         visual_dependency="T04-DGM-01 — the only visual in the unit",
         narration_dependency="one screen-level VO; the six node labels are the spoken spine"),
    dict(candidate_id="T04-SC-02", candidate="CLICK_TO_REVEAL",
         title="Landskap Lembut — tiga operasi penyelenggaraan",
         source_rows=[r["row_id"] for r in ROWS
                      if r["heading_path"] and len(r["heading_path"]) > 1
                      and r["heading_path"][1] == "Landskap Lembut"][:3],
         reason="Landskap Lembut decomposes into exactly three named operations — Siram, Baja, "
                "Racun — each with its own definition, Kaedah Pelaksanaan and Aspek "
                "Pengurusan untuk Kontraktor. Three peers with parallel internal structure is "
                "the shape a reveal pattern fits.",
         reusable_capability="completion-state treatment, all-viewed state, screen-level VO",
         new_treatment_required="NO — structurally similar to a B02 selection screen, but the "
                                "similarity must be re-derived, not imported",
         human_decision_required="whether three items warrant a selection screen or read "
                                 "better as three sequential screens",
         visual_dependency="NONE — no source visual exists for Siram, Baja or Racun",
         narration_dependency="screen-level 'Klik pada setiap …' instruction if reveal is chosen"),
    dict(candidate_id="T04-SC-03", candidate="SEQUENTIAL_STEPS",
         title="Racun — Perundangan, HSE dan Pengurusan Risiko",
         source_rows=rows_matching("Akta Racun", "pengendali racun berlesen", "PPE Lengkap",
                                   "Penyimpanan & Pelupusan", "Helaian Data Keselamatan",
                                   "spray drift"),
         reason="The Racun subsection carries the unit's entire compliance load — statute, "
                "licensing, PPE, storage, SDS, spray conditions, reporting. It is ordered "
                "obligation, not a menu.",
         reusable_capability="Notes typed-block schema; production-instruction blocks",
         new_treatment_required="NO",
         human_decision_required="whether legislative content may be reveal-gated at all, or "
                                 "must be shown in full — a compliance question, not a design one",
         visual_dependency="NONE",
         narration_dependency="high — this is the material a learner is most likely to be "
                              "assessed on"),
    dict(candidate_id="T04-SC-04", candidate="COMPARISON",
         title="Landskap Lembut vs Landskap Kejur",
         source_rows=[r["row_id"] for r in ROWS if r["content_type"] == "HEADING_2"],
         reason="The unit is built on exactly two Heading-2 blocks that are explicit "
                "counterparts — living horticultural elements against permanent built "
                "elements. The source itself frames the second as contrast to the first "
                "('Elemen kejur memberikan kontras yang menarik kepada kelembutan elemen "
                "tumbuhan').",
         reusable_capability="shell and Notes only",
         new_treatment_required="YES — B02 has no comparison screen type",
         human_decision_required="whether to spend a screen on the contrast or let the two "
                                 "sections stand alone",
         visual_dependency="NONE",
         narration_dependency="low"),
    dict(candidate_id="T04-SC-05", candidate="CLICK_TO_REVEAL",
         title="Landskap Kejur — empat kumpulan fungsi",
         source_rows=_h3_under("Landskap Kejur")[:4],
         reason="Landskap Kejur decomposes into four function groups — Pengurusan Ruang dan "
                "Sirkulasi, Fungsi Struktur dan Kejuruteraan, Kebolehgunaan dan Kemudahan, "
                "Estetika dan Reka Bentuk — each with exactly two sub-items.",
         reusable_capability="completion-state treatment, all-viewed state",
         new_treatment_required="NO",
         human_decision_required="none anticipated",
         visual_dependency="NONE — and this is the finding that matters most for portability",
         narration_dependency="screen-level instruction"),
    dict(candidate_id="T04-SC-06", candidate="PENDING_HUMAN",
         title="Rumusan and quiz screens",
         source_rows=[],
         reason="The module contains no Rumusan and no assessment items, for this unit or any "
                "other. Both screens exist in the B02 shell and have no source to fill them.",
         reusable_capability="the Rumusan and quiz-review STRUCTURES are portable (RP-007, "
                             "RP-008, RP-011)",
         new_treatment_required="NO — the structures exist",
         human_decision_required="REQUIRED — the CONTENT must be authored and signed off, and "
                                 "the 4+1 composition and 60% threshold must be confirmed as "
                                 "PL06-wide rather than B02-specific",
         visual_dependency="NONE",
         narration_dependency="follows the authored content"),
]

# ==========================================================================================
# PART 9 — READINESS SEMANTICS
# ==========================================================================================
READINESS_TYPES = ["SOURCE_PRESENT_CONTENT_NOT_EXTRACTED", "CONTENT_ASSESSMENT_PENDING",
                   "SOURCE_GAP_CONFIRMED"]

READINESS = dict(
    unit_id=UNIT_ID,
    content_extraction="COMPLETE — 100 controlled rows, 1 asset, 0 tables, 61 numbered "
                       "paragraphs, 8 module pages, every element in the 140-element body span "
                       "accounted for",
    instructional_status="CONTENT_ASSESSMENT_PENDING",
    source_gaps=["SOURCE_GAP_CONFIRMED — Rumusan",
                 "SOURCE_GAP_CONFIRMED — quiz items and answer key",
                 "SOURCE_GAP_CONFIRMED — no visual for any Landskap Lembut or Landskap Kejur "
                 "subject; the unit's only visual is the opening process diagram"],
    other_units="SOURCE_PRESENT_CONTENT_NOT_EXTRACTED — the twelve remaining units keep this "
                "status. Their source and boundaries are in custody; nobody has read them. "
                "SOURCE_INCOMPLETE was the wrong word for that state and is retired here.",
    note="The distinction matters because the three states have different owners. "
         "SOURCE_PRESENT_CONTENT_NOT_EXTRACTED is ours to clear by working. "
         "CONTENT_ASSESSMENT_PENDING is ours to propose and a human's to approve. "
         "SOURCE_GAP_CONFIRMED cannot be cleared by anyone reading the module, because the "
         "content is not in it.")

# ==========================================================================================
# SOURCE GAPS
# ==========================================================================================
SOURCE_GAPS = [
    dict(gap_id="T04-GAP-01", item="Rumusan", severity="BLOCKS_THIS_UNIT",
         finding="Not in T04 and not anywhere in the module DOCX — zero hits for 'Rumusan' "
                 "across all 6,167 body paragraphs.",
         owner="CC to author under A3 treatment, Bariah to approve",
         note="This retro-explains B02: its Rumusan was authored, not extracted. No storyboard "
              "in this project has ever had a source-supplied Rumusan."),
    dict(gap_id="T04-GAP-02", item="Quiz items and answer key", severity="BLOCKS_THIS_UNIT",
         finding="Zero hits for 'Soalan', 'Kuiz' or 'Jawapan' across the module.",
         owner="CC to draft, SME to sign the key",
         note="Composition (4 MCQ + 1 MR) and the 60% threshold are A3-scoped to B02 and must "
              "be confirmed before being applied here."),
    dict(gap_id="T04-GAP-03", item="Visual subjects for the body content",
         severity="BLOCKS_THIS_UNIT",
         finding="The unit contains ONE visual — a SmartArt process diagram at the opening. "
                 "There are zero raster images. Siram, Baja, Racun and all four Landskap Kejur "
                 "function groups have no source visual at all.",
         owner="BARIAH — visual requirement and treatment for a unit with no photographs",
         note="This is the single most important portability finding of the stage. B02's "
              "component-main treatment is a source-bound overview of photographs, backed by "
              "14 extracted assets. T04 has none. Applying B02's treatment here would require "
              "inventing subjects, which is prohibited. RP-101 is REUSABLE_WITH_SOURCE_"
              "SPECIFIC_BINDING and there is nothing here to bind it to."),
    dict(gap_id="T04-GAP-04", item="Cast binding", severity="BLOCKS_THIS_UNIT",
         finding="Unchanged from Stage 4.2F-A2: the ratified bank marks Haziq and Encik Roslan "
                 "CANONICAL, B02 ships Alya and Encik Rahman, and Bariah's PL06-wide answer "
                 "names neither.",
         owner="BARIAH + CAIR", note="STOP-006, SRC-ANOM-003."),
    dict(gap_id="T04-GAP-05", item="SmartArt rendering path", severity="BLOCKS_MMD_ONLY",
         finding="The only visual is a vector SmartArt part (word/diagrams/data1.xml), not an "
                 "image file. It cannot be extracted as a JPEG the way B02's 14 assets were.",
         owner="MMD / Bariah",
         note="Does not block the review storyboard, which carries visual DIRECTIONS as text."),
    dict(gap_id="T04-GAP-06", item="Lesson grouping authority", severity="BLOCKS_CANONICAL_FREEZE_ONLY",
         finding="Carried forward: GROUPING_AUTHORITY = REFERENCED_NOT_FROZEN.",
         owner="CAIR",
         note="Does not touch T04 — Topik 4 has one lesson, so no grouping judgement applies."),
]

TARGETED_DECISIONS = [
    dict(decision_id="T04-DEC-01", question="A unit with no photographs — what is the visual "
         "treatment for a component with no source visual?", owner="BARIAH",
         blocks="storyboard model", evidence="T04-GAP-03"),
    dict(decision_id="T04-DEC-02", question="Is 4 MCQ + 1 MR with a 60% threshold a PL06 "
         "standard or a B02 instantiation?", owner="BARIAH / source governance",
         blocks="quiz screens", evidence="RP-009, RP-010"),
    dict(decision_id="T04-DEC-03", question="Which cast pair applies outside B02?",
         owner="BARIAH + CAIR", blocks="S02 dialog screen", evidence="SRC-ANOM-003"),
    dict(decision_id="T04-DEC-04", question="May legislative and HSE content be reveal-gated, "
         "or must it be shown in full?", owner="BARIAH", blocks="T04-SC-03",
         evidence="T04-CLM-01, T04-CLM-02"),
    dict(decision_id="T04-DEC-05", question="How is the opening SmartArt process flow to be "
         "produced — re-drawn, exported, or rebuilt as sequential reveals?",
         owner="BARIAH / MMD", blocks="T04-SC-01", evidence="T04-GAP-05"),
]

VERDICT = "T04_SOURCE_COMPLETE_PENDING_TARGETED_INSTRUCTIONAL_DECISIONS"
FORBIDDEN_VERDICT_CLAIMS = ["T04_READY_FOR_MMD", "T04_CANONICALLY_FROZEN",
                            "T04_PRODUCTION_RELEASED"]
