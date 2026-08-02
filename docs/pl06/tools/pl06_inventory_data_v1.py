# -*- coding: utf-8 -*-
"""The ONE controlled data source for the PL06 scale-out inventory.

Stage 4.2F-A. Both the Markdown and the CSV inventory are emitted from here, and the QA
suite reads the same structures — so a divergence between the two documents is a bug in the
emitter, never a difference of opinion between two hand-maintained files.

DOCTRINE ENFORCED HERE
----------------------
Every unit carries a `source_reference` naming a frozen artifact on disk. A unit that cannot
name one does not get a row. No Bahagian is created because a number suggests it should
exist: the only Bahagian in this inventory are the delivered B02 and one whose existence a
human attested in writing, and that one is recorded WITHOUT a number because none was given.

The ratified decision key is `(course_code, pl, topik)` — SBAT-ADR-004 §1 explicitly rejected
per-Bahagian rows because they collide on the unique constraint. This inventory is therefore
modelled at Topik granularity, with Bahagian as an unresolved sub-boundary, which is both the
ratified shape and the honest one.
"""

STAGE = "4.2F-A"
GENERATED_BY = "docs/pl06/tools/pl06_emit_v1.py"

# ==========================================================================================
# 0. FROZEN EVIDENCE REGISTER — every claim below cites one of these
# ==========================================================================================
EVIDENCE = [
    dict(ref="M1", kind="FROZEN_ARTIFACT_PPTX",
         path="reviews/storyboard-bariah/v0_3_bariah_review/SB_K5_montaj_v1.pptx",
         bytes=61292,
         sha256="79a07b460ddb940de9dec0c1f92147beeb9ccf7af2b0ba35aab720369b393076",
         establishes="K5 course title and the eight Pakej Latihan, PL01-PL08, slide 2",
         authority_class="BARIAH_SUPPLIED_UPSTREAM_ARTIFACT"),
    dict(ref="M2", kind="FROZEN_ARTIFACT_PPTX",
         path="reviews/storyboard-bariah/v0_3_bariah_review/SB_K5PL6_montaj_v1.pptx",
         bytes=70656,
         sha256="97ccab1c2aef889145ff416d2058a1ed848a5e0315a42308d9792ae845260390",
         establishes="the seven PL06 Topik and their titles, slide 3; PL06 objectives, slide 2",
         authority_class="BARIAH_SUPPLIED_UPSTREAM_ARTIFACT"),
    dict(ref="A2", kind="FROZEN_ARTIFACT_DOCX",
         path="reviews/storyboard-bariah/v0_3_bariah_review/"
              "Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx",
         bytes=43342,
         sha256="c15ae05e20358eda17b8e272f5dd9a5ef85831016976a926346371ea5790bcf3",
         establishes="Bariah's answered review guide: Tamat destination = the NEXT BAHAGIAN in "
                     "Topik 3; character names to apply across the whole of PL06",
         authority_class="BARIAH_DIRECT_WRITTEN_CONFIRMATION"),
    dict(ref="A3", kind="FROZEN_ARTIFACT_DOCX",
         path="reviews/storyboard-bariah/v0_3_bariah_review/K5_PL06_T03_B02_UPDATED_SG_v0.3.docx",
         bytes=56475,
         sha256="f3166e42f84d4b1f1c792c28fdc0278cc1c56a061b1598bfcce0efde91ad429d",
         establishes="executable Style and Guidelines v0.3; the shell/Rumusan/quiz/Tamat grammar "
                     "the B02 build implements",
         authority_class="CONSOLIDATED_EXECUTABLE_SG"),
    dict(ref="P1", kind="SOURCE_EXTRACT_PDF_NOT_IN_REPOSITORY",
         path="K5_PL06_T03_B02_pages_256269.pdf",
         bytes=429918,
         sha256="30a6903dacbd7e8bce60dc1aa32026fc4ed98439054aeced9e895b5df828a3f4",
         establishes="the ONLY module content ever received: modul ms 238-249 / physical 256-269, "
                     "14 pages, covering K5 PL06 T03 B02 alone. Identity is recorded in "
                     "B02_ASSET_MANIFEST.md; the file itself is NOT in this repository, only the "
                     "14 JPEGs extracted from it",
         authority_class="SOURCE_ATTESTED_EXTRACT"),
    dict(ref="D1", kind="RATIFIED_DECISION",
         path="reviews/stage-0a/STAGE_0A_EVIDENCE_INVENTORY.md",
         bytes=None, sha256=None,
         establishes="SBAT-ADR-004 §1 decision granularity = TOPIK, key (course_code, pl, topik); "
                     "per-Bahagian rows REJECTED. §3 K2/K3/K5 are LOCKED courses, "
                     "OPEN_COURSES = [\"K4\"]",
         authority_class="RATIFIED_ARCHITECTURE_DECISION"),
    dict(ref="D2", kind="RATIFIED_CHARACTER_BANK",
         path="sbat/cair-decision-desk.html",
         bytes=None, sha256=None,
         establishes="Hilmi LOCKED course narrator, VO-only; Haziq and Encik Roslan CANONICAL; "
                     "eight further names OFF-CANON. All 16 K5 decision rows are EMPTY",
         authority_class="RATIFIED_CHARACTER_BANK"),
    dict(ref="C1", kind="SOURCE_CUSTODY_FINDING",
         path="reviews/sample-19slides/SOURCE_CUSTODY_AND_COVERAGE.md",
         bytes=None, sha256=None,
         establishes="F2, MEASURED_FACT: the approved K5 module is not present in the repository — "
                     "no module PDF, no extracted source nodes, no screen-to-source binding table "
                     "beyond the B02 slice",
         authority_class="MEASURED_FACT"),
    dict(ref="B1", kind="DELIVERED_ARTIFACT",
         path="reviews/source-completion/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4_1.pptx",
         bytes=471881,
         sha256="faef6c85745d2750236ffdf23fb7d14b81d26ed37c7db58ed274cb8d0f0178e5",
         establishes="the delivered and call-approved B02 storyboard, 100 review pages",
         authority_class="DELIVERED_REVIEW_CANDIDATE"),
]

# Source anomalies found while reading the evidence. Recorded, not silently corrected.
SOURCE_ANOMALIES = [
    dict(id="SRC-ANOM-001", evidence="M2",
         locus="SB_K5PL6_montaj_v1.pptx slide 3, shape 'Senarai Pakej Latihan'",
         verbatim="PL01: Pengurusan Operasi Pembinaan Landskap",
         finding="The header on the PL06 topic-list slide is numbered PL01 while carrying PL06's "
                 "title. Slide 2 of the same deck numbers it PL06 correctly. The seven topic "
                 "titles themselves are unaffected.",
         impact="Cosmetic in the montage; would be visible to a learner if the montage ships as "
                "is. Not ours to correct — the montage is a Bariah-supplied upstream artifact.",
         owner="BARIAH", status="OPEN_NOT_OURS"),
    dict(id="SRC-ANOM-002", evidence="M2",
         locus="SB_K5PL6_montaj_v1.pptx slide 3, shape names",
         verbatim="shape names 'Pengurusan Tender', 'Pelaksanaan Pengurusan Kontrak', "
                  "'Perancangan Dan Penjadualan Projek' carry PL06 topic text",
         finding="Shape names are recycled from another Pakej Latihan's deck; the montage is "
                 "template-instantiated. Consistent with the decision-desk finding that the 16 K5 "
                 "prompts are template-instantiated.",
         impact="None on content. It does mean shape names must never be used as a semantic key "
                "when reading montage or template-derived decks.",
         owner="NONE", status="RECORDED_NO_ACTION"),
    dict(id="SRC-ANOM-003", evidence="D2",
         locus="ratified character bank vs the delivered B02 cast",
         verbatim="Haziq (CANONICAL) / Encik Roslan (CANONICAL) vs Alya / Encik Rahman (B02)",
         finding="B02 ships Alya and Encik Rahman. The ratified K5 character bank marks Haziq and "
                 "Encik Roslan CANONICAL and eight other names OFF-CANON. Bariah approved the B02 "
                 "pair in writing and separately ruled that character names should apply across "
                 "the whole of PL06 'bergantung kepada kesesuaian'. Whether that promotes Alya and "
                 "Encik Rahman over the ratified pair, or the reverse, is NOT settled.",
         impact="Blocks cast binding for every non-B02 PL06 unit. Does not block B02.",
         owner="BARIAH_AND_CAIR", status="OPEN_BLOCKING_SCALE_OUT"),
]

# ==========================================================================================
# 1. PART 1 — THE B02 APPROVAL EVENT
# ==========================================================================================
APPROVAL_RECORD = dict(
    record_id="B02-APPROVAL-001",
    project="K5 PL06 T03 B02",
    artifact="K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4_1.pptx",
    artifact_bytes=471881,
    artifact_sha256="faef6c85745d2750236ffdf23fb7d14b81d26ed37c7db58ed274cb8d0f0178e5",
    approval_channel="PHONE_CALL",
    reported_by="FIRDAUS",
    reviewer="BARIAH",
    reported_result="NO INSTRUCTIONAL OR POWERPOINT ISSUES REPORTED",
    direction="PROCEED_WITH_REMAINING_PL06",
    authority_class="FIRDAUS_ATTESTED_BARIAH_CALL",
    written_confirmation="PENDING",
    # What this record may and may not be used for.
    may_authorise=[
        "planning and inventory work for the remaining PL06 units",
        "treating B02 as the reference implementation for rule-portability analysis",
    ],
    may_not_authorise=[
        "reclassifying any B02 ruling from FIRDAUS_ATTESTED_BARIAH_CALL to "
        "BARIAH_DIRECT_SCREENSHOT or BARIAH_DIRECT_WRITTEN_CONFIRMATION",
        "canonical freeze of B02",
        "MMD readiness or production release",
        "closing MS2680, B02-CAIR-INT-001 or the PL06 pronunciation precedence",
        "promoting any B02-specific rule to PL06-global scope",
    ],
    forbidden_classifications=["BARIAH_DIRECT_SCREENSHOT", "BARIAH_DIRECT_WRITTEN_CONFIRMATION"],
    evidence_status="NO_ARTIFACT — a phone call leaves no frozen bytes. This record is Firdaus's "
                    "attestation of what was said, and is the weakest authority class in use on "
                    "this project. It is superseded the moment written confirmation arrives.",
    supersedes_nothing=True,
    powerpoint_smoke_status="NOT RUN IN THIS ENVIRONMENT — Bariah's call reports that the deck "
                            "opened acceptably on her machine. That is a human observation of a "
                            "real PowerPoint, not a smoke test we executed or recorded. "
                            "MICROSOFT_POWERPOINT_EQUIVALENCE remains unclaimed.",
)

# ==========================================================================================
# 2. PART 2 — THE UNIT INVENTORY
# ==========================================================================================
READINESS_VALUES = ["READY", "READY_WITH_HOLDS", "SOURCE_INCOMPLETE",
                    "REQUIRES_BARIAH_DECISION", "UNSUPPORTED_INTERACTION",
                    "SOURCE_AUTHORITY_UNRESOLVED"]

LANE_VALUES = ["LANE_A_EXISTING_SUPPORTED_PATTERN", "LANE_B_SUPPORTED_WITH_SOURCE_MAPPING",
               "LANE_C_NEW_TREATMENT_OR_DECISION_REQUIRED", "LANE_D_SOURCE_INCOMPLETE"]

UNIT_SCOPE_VALUES = ["DELIVERED_BASELINE", "REMAINING"]

# The seven Topik titles are quoted verbatim from M2 slide 3.
_TOPIK = [
    (1, "Proses Memula Kerja"),
    (2, "Elemen Pembinaan Landskap"),
    (3, "Komponen Landskap"),
    (4, "Penjagaan Dan Penyelenggaraan"),
    (5, "Pengurusan Kualiti Projek"),
    (6, "Perlindungan Dan Penambahbaikan Alam Sekitar"),
    (7, "Demobilisasi"),
]

_NO_SOURCE_BLOCKERS = [
    "NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY",
    "BAHAGIAN_BOUNDARY_UNRESOLVED",
    "NO_RUMUSAN_SOURCE",
    "NO_QUIZ_SOURCE",
    "CAST_BINDING_UNRESOLVED",
]


def _unresolved_topik(n, title, order):
    """A Topik whose existence and title are source-attested and whose content is not."""
    return dict(
        unit_id=f"K5-PL06-T{n:02d}",
        pl="PL06", topik_number=n, topik_title=title,
        bahagian_number=None, bahagian_title=None,
        unit_scope="REMAINING",
        source_document="NONE_IN_CUSTODY",
        source_page_range="UNKNOWN",
        source_reference="M2 — SB_K5PL6_montaj_v1.pptx slide 3, "
                         f"verbatim 'Topik {n}: {title}'",
        source_authority_class="BARIAH_SUPPLIED_UPSTREAM_ARTIFACT",
        source_attests="TOPIK_EXISTENCE_AND_TITLE_ONLY",
        controlled_content_available=False,
        existing_id_input_available=False,
        storyboard_input_available=False,
        source_rows_count=None, source_figures_count=None,
        source_tables_count=None, source_assets_count=None,
        rumusan_available=False, quiz_mcq_available=False, quiz_mr_available=False,
        interaction_requirement="UNKNOWN",
        interaction_pattern_candidate="NOT_DETERMINABLE_WITHOUT_SOURCE",
        visual_requirement="UNKNOWN",
        narration_requirement="PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown",
        terminology_risks="PL06 pronunciation precedence unratified; English-term italics list is "
                          "B02-derived and must be re-derived per unit",
        standards_or_external_claims="UNKNOWN — no source read",
        open_human_decisions=["BAHAGIAN_BOUNDARY", "CAST_BINDING_PL06_SCOPE"],
        generator_support_status="SHELL_SUPPORTED_CONTENT_UNSUPPORTED",
        qa_support_status="SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT",
        lane="LANE_D_SOURCE_INCOMPLETE",
        readiness_status="SOURCE_AUTHORITY_UNRESOLVED",
        blocker_reason="No approved source document for this Topik is in custody. Its existence "
                       "and title are attested by the PL06 montage; nothing else about it is.",
        blocking_conditions=list(_NO_SOURCE_BLOCKERS),
        recommended_execution_order=order,
    )


UNITS = [
    # ---- the delivered baseline ----
    dict(
        unit_id="K5-PL06-T03-B02",
        pl="PL06", topik_number=3, topik_title="Komponen Landskap",
        bahagian_number=2, bahagian_title="Komponen Landskap",
        unit_scope="DELIVERED_BASELINE",
        source_document="K5_PL06_T03_B02_pages_256269.pdf",
        source_page_range="modul ms 238-249 / physical 256-269",
        source_reference="P1 — sha256 30a6903d…, identity recorded in B02_ASSET_MANIFEST.md; "
                         "26 source rows bound in STORYBOARD_SOURCE_MAP_v0.4.md",
        source_authority_class="SOURCE_ATTESTED_EXTRACT",
        source_attests="FULL_UNIT_CONTENT",
        controlled_content_available=True,
        existing_id_input_available=True,
        storyboard_input_available=True,
        source_rows_count=26, source_figures_count=4,
        source_tables_count=10, source_assets_count=14,
        rumusan_available=True, quiz_mcq_available=True, quiz_mr_available=True,
        interaction_requirement="REQUIRED",
        interaction_pattern_candidate="FAMILY_S / FAMILY_P1 / FAMILY_P2 (B02-specific taxonomy)",
        visual_requirement="REQUIRED — source-bound overview, 9/9 mapped",
        narration_requirement="A3 shell grammar, three spoken S01 blocks, screen-level VO only",
        terminology_risks="PL06 pronunciation precedence RESERVED_NOT_ACTIVE; 'BBQ pit' lowercase "
                          "source form measured",
        standards_or_external_claims="MS2680 cited in source, verification open",
        open_human_decisions=["MS2680", "B02-CAIR-INT-001", "OD-10 / L-01 LMS navigation"],
        generator_support_status="FULLY_SUPPORTED",
        qa_support_status="FULLY_SUPPORTED — 441 active gates, 51 mutation fixtures",
        lane="LANE_A_EXISTING_SUPPORTED_PATTERN",
        readiness_status="READY_WITH_HOLDS",
        blocker_reason="Delivered and call-approved. Holds are source-authority only and none of "
                       "them blocks this unit's review candidacy: MS2680, B02-CAIR-INT-001, and "
                       "the LMS navigation ruling. Microsoft PowerPoint smoke is not recorded.",
        blocking_conditions=["MS2680_VERIFICATION", "B02_CAIR_INT_001",
                             "LMS_NAVIGATION_RULING", "POWERPOINT_SMOKE_NOT_RECORDED"],
        recommended_execution_order=0,
    ),
    # ---- the one non-B02 Bahagian a human has attested ----
    dict(
        unit_id="K5-PL06-T03-BNEXT",
        pl="PL06", topik_number=3, topik_title="Komponen Landskap",
        # Both null, deliberately. A human attested that this Bahagian exists; nobody gave it a
        # number or a title, and a descriptor such as "the next one" is not a title. The
        # attestation itself is carried verbatim in source_reference below.
        bahagian_number=None, bahagian_title=None,
        unit_scope="REMAINING",
        source_document="NONE_IN_CUSTODY",
        source_page_range="UNKNOWN — the B02 extract ends at modul ms 249",
        source_reference="A2 — Bariah's answered review guide, Tamat destination question, "
                         "verbatim '✓ A. Bahagian seterusnya dalam Topik 3.'; corroborated by A3 "
                         "'Logical next destination is the next Bahagian in Topik 3'",
        source_authority_class="BARIAH_DIRECT_WRITTEN_CONFIRMATION",
        source_attests="EXISTENCE_ONLY — no number, no title, no page range was given",
        controlled_content_available=False,
        existing_id_input_available=False,
        storyboard_input_available=False,
        source_rows_count=None, source_figures_count=None,
        source_tables_count=None, source_assets_count=None,
        rumusan_available=False, quiz_mcq_available=False, quiz_mr_available=False,
        interaction_requirement="UNKNOWN",
        interaction_pattern_candidate="NOT_DETERMINABLE_WITHOUT_SOURCE",
        visual_requirement="UNKNOWN",
        narration_requirement="PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown",
        terminology_risks="Same Topik as B02, so the B02 glossary is likely but not proven to apply",
        standards_or_external_claims="UNKNOWN — no source read",
        open_human_decisions=["BAHAGIAN_NUMBER_AND_TITLE", "CAST_BINDING_PL06_SCOPE"],
        generator_support_status="SHELL_SUPPORTED_CONTENT_UNSUPPORTED",
        qa_support_status="SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT",
        lane="LANE_D_SOURCE_INCOMPLETE",
        readiness_status="SOURCE_AUTHORITY_UNRESOLVED",
        blocker_reason="A human attested that this unit exists and that the B02 learner navigates "
                       "to it. Nobody has said what number it carries, what it is called, or "
                       "which module pages it occupies. No source is in custody.",
        blocking_conditions=list(_NO_SOURCE_BLOCKERS),
        # Third, not second: the strongest existence evidence of any remaining unit, but the
        # weakest proof value. Building it before the portability question is answered would
        # tell us least about whether the capability travels.
        recommended_execution_order=3,
    ),
]

# Topik 1, 2, 4, 5, 6, 7 — existence and title attested, nothing else.
# 1 = the Wave 0 selection, 2 = first runner-up, then the remainder.
_ORDER = {4: 1, 2: 2, 1: 4, 5: 5, 6: 6, 7: 7}
for _n, _t in _TOPIK:
    if _n == 3:
        continue
    UNITS.append(_unresolved_topik(_n, _t, _ORDER[_n]))

UNITS.sort(key=lambda u: u["recommended_execution_order"])

# The CSV column order. Also the field-completeness contract the QA suite enforces.
CSV_COLUMNS = [
    "unit_id", "pl", "topik_number", "topik_title", "bahagian_number", "bahagian_title",
    "unit_scope", "source_document", "source_page_range", "source_reference",
    "source_authority_class", "source_attests", "controlled_content_available",
    "existing_id_input_available", "storyboard_input_available", "source_rows_count",
    "source_figures_count", "source_tables_count", "source_assets_count", "rumusan_available",
    "quiz_mcq_available", "quiz_mr_available", "interaction_requirement",
    "interaction_pattern_candidate", "visual_requirement", "narration_requirement",
    "terminology_risks", "standards_or_external_claims", "open_human_decisions",
    "generator_support_status", "qa_support_status", "lane", "readiness_status",
    "blocker_reason", "blocking_conditions", "recommended_execution_order",
]

# ==========================================================================================
# 3. PART 3 — RULE PORTABILITY
# ==========================================================================================
PORTABILITY_CLASSES = ["PL06_GLOBAL_REUSABLE", "REUSABLE_WITH_SOURCE_SPECIFIC_BINDING",
                       "B02_SPECIFIC_DO_NOT_PROPAGATE"]

GLOBAL = "PL06_GLOBAL_REUSABLE"
BOUND = "REUSABLE_WITH_SOURCE_SPECIFIC_BINDING"
LOCAL = "B02_SPECIFIC_DO_NOT_PROPAGATE"


def _r(rid, desc, cls, evidence, scope, human, oracle, risk):
    return dict(rule_id=rid, rule_description=desc, portability_class=cls, evidence=evidence,
                destination_scope=scope, human_authority_required=human,
                automated_oracle_available=oracle, propagation_risk=risk)


RULES = [
    # ---------------- A. PL06_GLOBAL_REUSABLE ----------------
    _r("RP-001", "Review storyboard shell: 13.3333x7.5in stage, navigation band at 6.92in, "
                 "off-canvas production panel, one review page per runtime state",
       GLOBAL, "A3 §2.1 global flow; implemented and gated in B02 across 100 pages",
       "ALL_PL06_UNITS", "NONE — mechanical", True, "LOW"),
    _r("RP-002", "S01 / S02 / S03 screen grammar: topic-entry, dialog, orientation",
       GLOBAL, "A3 §2.1; A2 answered; B02 S01 spoken-block ruling frozen in D3",
       "ALL_PL06_UNITS", "NONE for the grammar; the CONTENT of S02/S03 is per-unit", True,
       "LOW for structure. The S01 spoken text is unit-specific and must be re-derived — "
       "reusing B02's three blocks verbatim would state the wrong Topik and Bahagian."),
    _r("RP-003", "Production-panel treatment: off-canvas at x=-6.90in, model-quoted metadata, "
                 "never hand-restated",
       GLOBAL, "b02_generator_v0_4.prodpanel_v4; GEX-002 registered exemption",
       "ALL_PL06_UNITS", "NONE", True, "LOW"),
    _r("RP-004", "Speaker Notes typed-block schema: NON_SPOKEN_CONTEXT / SPOKEN_CONTENT_VO / "
                 "SPOKEN_INTERACTION_INSTRUCTION / PRODUCTION_INSTRUCTION_NOT_SPOKEN, each with "
                 "an explicit spoken boolean",
       GLOBAL, "NOTES_BLOCK_SCHEMA_v0.4.2.json; gated by NOTES_BLOCKS_WITHOUT_TYPE and "
               "NOTES_BLOCKS_WITHOUT_SPOKEN_FLAG",
       "ALL_PL06_UNITS", "NONE", True, "LOW"),
    _r("RP-005", "English-term italics mechanism: run-level <a:rPr i=\"1\"/> applied through one "
                 "controlled glossary shared by canvas and Notes writers",
       GLOBAL, "b02_glossary_v0_4; APPROVED_TERMS_NOT_ITALICISED gate",
       "ALL_PL06_UNITS", "The TERM LIST is per-unit and needs SME sign-off; the mechanism does not",
       True, "MEDIUM — the mechanism is global, the B02 term list is not. Propagating the list "
             "would italicise words a different unit never uses and miss the ones it does."),
    _r("RP-006", "Completion-state treatment: all-viewed and group-complete states re-render the "
                 "base screen with completion marks, never a new screen",
       GLOBAL, "A3; B02 22 component-main state pages; PERSISTENCE_TARGET gates",
       "ALL_PL06_UNITS", "NONE", True, "LOW"),
    _r("RP-007", "Rumusan treatment: summarises THIS Bahagian only, contractor/site perspective, "
                 "no Kepentingan / Isi Utama / Manfaat labels",
       GLOBAL, "A2 answered verbatim: 'Rumusan perlu merumuskan Bahagian 2 sahaja dan menggunakan "
               "perspektif kontraktor. Ia tidak memaparkan label Kepentingan, Isi Utama atau Manfaat.'",
       "ALL_PL06_UNITS", "NONE for the rule; the CONTENT is per-unit", True, "LOW"),
    _r("RP-008", "Quiz review structure: question -> answer -> review state, answer key visible "
                 "in the review state, rationale in the production panel only",
       GLOBAL, "A3; B02 five questions; QUIZ_REVIEW_STATE_* gates",
       "ALL_PL06_UNITS", "NONE for the structure", True, "LOW"),
    _r("RP-009", "Quiz composition: 4 MCQ + 1 MR",
       GLOBAL, "A3; implemented in B02 and gated",
       "ALL_PL06_UNITS",
       "VERIFY — A3 is the B02 slice of the S&G. Whether 4+1 is a PL06 standard or a B02 "
       "instantiation has NOT been confirmed by anyone.", True,
       "MEDIUM — classified GLOBAL on the strength of a Style and Guidelines document, not on a "
       "statement that it applies to every unit. Flagged for confirmation, not assumed."),
    _r("RP-010", "60 percent pass threshold",
       GLOBAL, "A3", "ALL_PL06_UNITS",
       "VERIFY — same caveat as RP-009", True, "MEDIUM"),
    _r("RP-011", "Correct / incorrect feedback wording: 'Pilihan jawapan tepat.' and "
                 "'Pilihan jawapan tidak tepat.', not spoken",
       GLOBAL, "D3 frozen screenshot ruling, Stage 4.2E-A; QUIZ_FEEDBACK_REGISTER_v0.4.4.json",
       "ALL_PL06_UNITS", "NONE — Bariah ruled the wording directly", True, "LOW"),
    _r("RP-012", "Tamat and close-window behaviour: learner closes the window, shell next "
                 "disabled, route recorded as LMS-owner metadata with both claims NOT PROVEN",
       GLOBAL, "A3; Firdaus/LMS ruling recorded at Stage 4.2E-A",
       "ALL_PL06_UNITS",
       "The DESTINATION is per-unit — B02's is 'next Bahagian in Topik 3' and no other unit's is "
       "known", True, "LOW for behaviour, HIGH for destination text"),
    _r("RP-013", "Off-canvas registered geometry treatment: an off-stage shape passes only if a "
                 "registry entry matches its placeholder type, name and all four coordinates",
       GLOBAL, "GEOMETRY_EXEMPTION_REGISTRY_v0.4.4.1.json; fixtures M-08 to M-11",
       "ALL_PL06_UNITS", "NONE", True, "LOW"),
    _r("RP-014", "Artifact identity and exact release-token validation: one controlled identity "
                 "source, token comparison by exact set, panel vs manifest agreement",
       GLOBAL, "b02_artifact_identity_v0_4_4_1.py; defect B02-META-REG-001",
       "ALL_PL06_UNITS", "NONE", True,
       "LOW — and this one is the highest-value rule to propagate first. It is the rule whose "
       "absence let four B02 releases ship mis-stamped."),
    _r("RP-015", "Three-way separation of physical learner screen, runtime state and review page",
       GLOBAL, "B02 model contract 29 / 100 / 100; gated",
       "ALL_PL06_UNITS", "NONE", True, "LOW"),
    _r("RP-016", "Oracle contract: an oracle module imports nothing from the generator and "
                 "re-hashes its evidence before returning a value",
       GLOBAL, "generator/audit/*; *_ORACLE_IMPORTS_NO_GENERATOR gates",
       "ALL_PL06_UNITS", "NONE", True, "LOW"),
    _r("RP-017", "Population pinning: a gate's population is pinned to learner_screen_id and its "
                 "bound runtime states, never to review-page classification",
       GLOBAL, "class I CLASSIFICATION_SCOPED_POPULATION, Stage 4.2D",
       "ALL_PL06_UNITS", "NONE", True, "LOW"),

    # ---------------- B. REUSABLE_WITH_SOURCE_SPECIFIC_BINDING ----------------
    _r("RP-101", "Visual overview treatment: a component-main screen carries several smaller "
                 "source-bound visuals as an overview",
       BOUND, "D2 6:52 PM screenshot — 'Component-main - Visual diperlukan' and the overview "
              "treatment",
       "PL06 units that HAVE component-main screens",
       "Per unit: whether the unit even has component-main screens, and what the subjects are",
       True,
       "HIGH — D2 was given while reviewing B02. It is written generally enough to read as a "
       "treatment rule, but every subject in it is bound to a B02 source row. A unit with no "
       "component structure has nothing for this rule to attach to."),
    _r("RP-102", "Example popup treatment: one large focused visual panel, measurably wider than "
                 "any overview card",
       BOUND, "D2; B02 4.14in panel vs 2.60in card, gated",
       "PL06 units with example popups", "Per unit: whether example popups exist", True, "MEDIUM"),
    _r("RP-103", "Specification popups are text-led and carry NO visual",
       BOUND, "Bariah 4:37 PM verbatim: 'Semua contoh ada visual. Semua pop up ada visual, KECUALI "
              "pop up Spesifikasi (bahan, dimensi etc)'",
       "PL06 units with specification popups", "Per unit: whether spec popups exist", True, "LOW"),
    _r("RP-104", "Source figure binding: a visual direction is read from the source row's own "
                 "figure or table photograph, never composed from the component name",
       BOUND, "B02_ASSET_MANIFEST.md 14 assets; EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED gate",
       "ALL_PL06_UNITS with extracted assets",
       "None for the rule; the ASSETS must be extracted and hashed per unit", True,
       "MEDIUM — the rule is portable, the asset register is not. A unit with no extracted assets "
       "cannot satisfy it and must not be given placeholder subjects to pass."),
    _r("RP-105", "Learner-screen persistence: base identity persists across all bound runtime "
                 "states, compared by SUBJECT IDENTITY not by shape count",
       BOUND, "D2 persistence ruling; B02 22 state pages",
       "PL06 units with multi-state screens", "Per unit: which screens have states", True, "LOW"),
    _r("RP-106", "Character use: named cast appears only on screens with an explicit cast binding",
       BOUND, "Bariah A2 answer: 'Gunakan nama watak untuk keseluruhan PL06. Gunakan nama watak "
              "yang sama bergantung kepada kesesuaian.' — PL06 SCOPE, conditional on suitability",
       "ALL_PL06_UNITS",
       "REQUIRED — and unresolved. See SRC-ANOM-003: the ratified bank marks Haziq and Encik "
       "Roslan CANONICAL while B02 ships Alya and Encik Rahman. Bariah's PL06-wide instruction "
       "does not say WHICH pair.", False,
       "HIGH — this is the single rule most likely to be propagated wrongly. Bariah's answer is "
       "PL06-scoped, which makes it look global; it is conditional on 'kesesuaian' and it conflicts "
       "with a ratified character bank that nobody has reconciled."),
    _r("RP-107", "Screen-level VO instructions only: 'Klik pada setiap…' is spoken; Tutup, "
                 "Kembali, Semak Jawapan and Ulang Kuiz are not",
       BOUND, "D3 frozen ruling; MICRO_CONTROL_INSTRUCTIONS_IN_PACKAGE_NOTES gate",
       "ALL_PL06_UNITS",
       "The micro-control LIST is B02's control vocabulary; a unit with different controls needs "
       "its own list", True, "LOW"),
    _r("RP-108", "Question and answer mapping: every quiz option maps to a source row and the "
                 "answer key is derived from controlled content",
       BOUND, "ANSWER_KEY_SOURCE_MISMATCH gate; B02 five questions",
       "ALL_PL06_UNITS", "SME sign-off on each unit's answer key", True, "LOW"),

    # ---------------- C. B02_SPECIFIC_DO_NOT_PROPAGATE ----------------
    _r("RP-201", "FAMILY_S execution family — 4 components, selection screen with example cards",
       LOCAL, "B02_INTERACTION_FAMILY_TAXONOMY_v0_4.md; derived from B02's 26 source rows",
       "K5-PL06-T03-B02 ONLY", "Any reuse needs a fresh derivation from the target unit's source",
       True, "HIGH — the three families are a reading of B02's table structure. They are not a "
             "PL06 interaction taxonomy and were never presented to anyone as one."),
    _r("RP-202", "FAMILY_P1 execution family — 3 components, per-example specification popups",
       LOCAL, "same", "K5-PL06-T03-B02 ONLY", "same", True, "HIGH"),
    _r("RP-203", "FAMILY_P2 execution family — 2 components, category-level popups",
       LOCAL, "same", "K5-PL06-T03-B02 ONLY", "same", True, "HIGH"),
    _r("RP-204", "The nine B02 component names — Struktur Persisir Air, Struktur Teduhan, "
                 "Kemudahan Awam, Water Feature, Kerusi Taman, Papan Tanda, Tong Sampah, "
                 "Drinking Fountain, BBQ Pit",
       LOCAL, "modul ms 238-249", "K5-PL06-T03-B02 ONLY", "N/A", True, "HIGH"),
    _r("RP-205", "The nine B02 overview cardinalities 5, 5, 3, 3, 3, 2, 3, 2, 1",
       LOCAL, "COMPONENT_OVERVIEW_MAPPING_v0.4.4.json; D4 for the 2 and the 1",
       "K5-PL06-T03-B02 ONLY",
       "N/A — and note the frozen rule UNIVERSAL_FIXED_CARD_COUNT = False, which forbids treating "
       "any of these as a template", True,
       "HIGH — a fixed card count is exactly the kind of rule that looks reusable and is not. "
       "The mapping contract records MINIMUM_OVERVIEW_CARDINALITY = 1 and nothing above it."),
    _r("RP-206", "Papan Tanda ruling — two visuals, Pilihan A, the figures Informasi and "
                 "Penunjuk Arah",
       LOCAL, "D4 8:24 AM verbatim 'Yup, papan tanda Pilihan A, ok bbq pit 1 gamba'",
       "K5-PL06-T03-B02 ONLY", "N/A", True,
       "HIGH — and the frozen ruling explicitly records "
       "informasi_equals_interpretatif_global_rule = False. It is not a naming rule."),
    _r("RP-207", "BBQ Pit ruling — exactly one visual, five alternatives rejected",
       LOCAL, "D4", "K5-PL06-T03-B02 ONLY", "N/A", True, "HIGH"),
    _r("RP-208", "The 26 B02 source rows and their UIDs",
       LOCAL, "STORYBOARD_SOURCE_MAP_v0.4.md", "K5-PL06-T03-B02 ONLY", "N/A", True, "HIGH"),
    _r("RP-209", "The 27 B02 visual subjects",
       LOCAL, "COMPONENT_OVERVIEW_MAPPING_v0.4.4.json", "K5-PL06-T03-B02 ONLY", "N/A", True,
       "HIGH — INVENTED_VISUAL_SUBJECTS = 0 is a per-unit obligation, not a transferable result."),
    _r("RP-210", "B02 learner-screen count 29", LOCAL, "B02_V0_4_MODEL_CONTRACT.json",
       "K5-PL06-T03-B02 ONLY", "N/A", True, "HIGH"),
    _r("RP-211", "B02 runtime-state count 100", LOCAL, "B02_V0_4_MODEL_CONTRACT.json",
       "K5-PL06-T03-B02 ONLY", "N/A", True, "HIGH"),
    _r("RP-212", "B02 interaction-item count 54", LOCAL, "B02_V0_4_MODEL_CONTRACT.json",
       "K5-PL06-T03-B02 ONLY", "N/A", True, "HIGH"),
    _r("RP-213", "B02-specific text and factual claims, including the MS2680 citation and the "
                 "Slide 5 Asas Pembinaan bullets",
       LOCAL, "controlled content b02_proof_content_v0_4.py", "K5-PL06-T03-B02 ONLY", "N/A", True,
       "HIGH"),
    _r("RP-214", "The B02 glossary term list and its italic set",
       LOCAL, "b02_glossary_v0_4.py", "K5-PL06-T03-B02 ONLY",
       "Per-unit SME derivation", True,
       "MEDIUM — see RP-005: the MECHANISM is global, this LIST is not."),
    _r("RP-215", "The Alya / Encik Rahman cast pair",
       LOCAL, "B02 S02 binding; approved by Bariah for B02",
       "K5-PL06-T03-B02 ONLY until SRC-ANOM-003 is resolved",
       "REQUIRED — conflicts with the ratified CANONICAL pair Haziq / Encik Roslan", False,
       "HIGH — Bariah's 'keseluruhan PL06' answer is about the PRACTICE of naming characters, not "
       "an instruction to use these two names everywhere. Reading it the other way would override "
       "a ratified character bank on the strength of an answer to a different question."),
]

# ==========================================================================================
# 4. PART 6 — STOP CONDITIONS
# ==========================================================================================
STOP_SCOPES = ["BLOCKS_THIS_UNIT", "BLOCKS_CANONICAL_FREEZE_ONLY", "BLOCKS_MMD_ONLY",
               "BLOCKS_FINAL_RELEASE_ONLY"]

STOP_CONDITIONS = [
    dict(id="STOP-001", condition="MISSING_APPROVED_SOURCE",
         description="No approved source document for the unit is in custody.",
         scope="BLOCKS_THIS_UNIT",
         applies_to=["K5-PL06-T01", "K5-PL06-T02", "K5-PL06-T03-BNEXT", "K5-PL06-T04",
                     "K5-PL06-T05", "K5-PL06-T06", "K5-PL06-T07"],
         resolver="FIRDAUS / CAIR — deliver the module extract for the unit",
         evidence="C1 F2 MEASURED_FACT"),
    dict(id="STOP-002", condition="MISSING_BAHAGIAN_BOUNDARY",
         description="The unit's Bahagian boundaries are not established by any source. "
                     "Numbering alone is not evidence.",
         scope="BLOCKS_THIS_UNIT",
         applies_to=["K5-PL06-T01", "K5-PL06-T02", "K5-PL06-T03-BNEXT", "K5-PL06-T04",
                     "K5-PL06-T05", "K5-PL06-T06", "K5-PL06-T07"],
         resolver="BARIAH / CAIR — confirm the Bahagian list per Topik",
         evidence="M2 attests Topik only; no artifact enumerates Bahagian"),
    dict(id="STOP-003", condition="MISSING_VISUAL_SUBJECT_AUTHORITY",
         description="No source figure or table photograph is bound, so no visual subject can be "
                     "named without inventing one.",
         scope="BLOCKS_THIS_UNIT",
         applies_to=["K5-PL06-T01", "K5-PL06-T02", "K5-PL06-T03-BNEXT", "K5-PL06-T04",
                     "K5-PL06-T05", "K5-PL06-T06", "K5-PL06-T07"],
         resolver="follows STOP-001", evidence="RP-104, RP-209"),
    dict(id="STOP-004", condition="MISSING_INTERACTION_RULING",
         description="The unit's interaction pattern cannot be derived without its source "
                     "structure. The B02 families must not be assumed.",
         scope="BLOCKS_THIS_UNIT",
         applies_to=["K5-PL06-T01", "K5-PL06-T02", "K5-PL06-T03-BNEXT", "K5-PL06-T04",
                     "K5-PL06-T05", "K5-PL06-T06", "K5-PL06-T07"],
         resolver="follows STOP-001, then BARIAH ruling if the structure is novel",
         evidence="RP-201 to RP-203"),
    dict(id="STOP-005", condition="MISSING_QUIZ_ANSWER_KEY",
         description="No quiz source or answer key exists for the unit.",
         scope="BLOCKS_THIS_UNIT",
         applies_to=["K5-PL06-T01", "K5-PL06-T02", "K5-PL06-T03-BNEXT", "K5-PL06-T04",
                     "K5-PL06-T05", "K5-PL06-T06", "K5-PL06-T07"],
         resolver="follows STOP-001; SME sign-off on the key", evidence="RP-108"),
    dict(id="STOP-006", condition="CAST_BINDING_UNRESOLVED",
         description="The ratified character bank marks Haziq and Encik Roslan CANONICAL; B02 "
                     "ships Alya and Encik Rahman; Bariah's PL06-wide instruction names neither.",
         scope="BLOCKS_THIS_UNIT",
         applies_to=["K5-PL06-T01", "K5-PL06-T02", "K5-PL06-T03-BNEXT", "K5-PL06-T04",
                     "K5-PL06-T05", "K5-PL06-T06", "K5-PL06-T07"],
         resolver="BARIAH + CAIR", evidence="SRC-ANOM-003, RP-106, RP-215"),
    dict(id="STOP-007", condition="PL06_PRONUNCIATION_PRECEDENCE_UNRATIFIED",
         description="The PL06 pronunciation rule ('PL satu', not 'PL kosong satu') is present in "
                     "both montage decks as a Note to MMD but is not a ratified narration contract.",
         scope="BLOCKS_MMD_ONLY", applies_to=["ALL"],
         resolver="source governance",
         evidence="M1 and M2 Note to MMD; PRONUNCIATION_REGISTER_PL06_v0.4.4.json "
                  "RESERVED_NOT_ACTIVE"),
    dict(id="STOP-008", condition="MS2680_VERIFICATION",
         description="A standards citation in the B02 source is unverified.",
         scope="BLOCKS_FINAL_RELEASE_ONLY", applies_to=["K5-PL06-T03-B02"],
         resolver="source authority", evidence="B02_OPEN_DECISION_INVENTORY_v0.4.4"),
    dict(id="STOP-009", condition="B02_CAIR_INT_001",
         description="The canonical module DOCX has an identity pinned but no hash; integrity is "
                     "unverified.",
         scope="BLOCKS_CANONICAL_FREEZE_ONLY", applies_to=["ALL"],
         resolver="FIRDAUS / CAIR", evidence="B02_V0_4_INPUT_FREEZE.md §1 input E"),
    dict(id="STOP-010", condition="K5_COURSE_LOCKED",
         description="SBAT-ADR-004 §3 locks K2, K3 and K5 in the CAIR decision desk; "
                     "OPEN_COURSES = [\"K4\"]. This governs where DECISIONS may be written, not "
                     "whether storyboards may be produced — but no PL06 decision may be recorded "
                     "in cair_decisions while it holds.",
         scope="BLOCKS_CANONICAL_FREEZE_ONLY", applies_to=["ALL"],
         resolver="CAIR — the lock lifts when the per-course source drill is complete",
         evidence="D1"),
    dict(id="STOP-011", condition="POWERPOINT_SMOKE_NOT_RECORDED",
         description="No Microsoft PowerPoint smoke test has been executed or recorded in this "
                     "environment for any unit. Bariah's call reports the deck opened acceptably "
                     "on her machine; that is a human observation, not a recorded test.",
         scope="BLOCKS_FINAL_RELEASE_ONLY", applies_to=["ALL"],
         resolver="FIRDAUS — run and record the smoke test",
         evidence="APPROVAL_RECORD.powerpoint_smoke_status"),
    dict(id="STOP-012", condition="SOURCE_CONTRADICTION",
         description="The PL06 montage numbers its own topic-list header PL01 while carrying "
                     "PL06's title.",
         scope="BLOCKS_FINAL_RELEASE_ONLY", applies_to=["ALL"],
         resolver="BARIAH — the montage is hers", evidence="SRC-ANOM-001"),
]

# ==========================================================================================
# 5. PART 5 — FIRST SCALE-OUT SELECTION
# ==========================================================================================
SELECTION_CRITERIA = [
    "source_completeness", "source_authority", "visual_availability",
    "interaction_representativeness", "quiz_completeness", "generator_compatibility",
    "qa_compatibility", "b02_coupling_exposure", "expected_proof_value", "estimated_duration",
]

# Scores are 0-5. A criterion nobody has evidence for scores 0 — not a midpoint.
CANDIDATE_SCORES = [
    dict(unit_id="K5-PL06-T04", label="Topik 4 — Penjagaan Dan Penyelenggaraan",
         scores=dict(source_completeness=0, source_authority=2, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=3, qa_compatibility=3, b02_coupling_exposure=5,
                     expected_proof_value=5, estimated_duration=3),
         note="Different Topik, so a successful build proves portability rather than repeating "
              "B02's grammar. Adjacent to the only page range whose custody chain is proven, so "
              "one contiguous extraction request covers it."),
    dict(unit_id="K5-PL06-T03-BNEXT", label="Topik 3 — the next Bahagian after B02",
         scores=dict(source_completeness=0, source_authority=4, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=4, qa_compatibility=4, b02_coupling_exposure=1,
                     expected_proof_value=2, estimated_duration=4),
         note="Strongest existence evidence of any non-B02 unit — a human ruled in writing that "
              "the B02 learner navigates to it. But it sits in the same Topik as B02 and would "
              "very likely reuse B02's component grammar, so a green build would prove almost "
              "nothing about portability."),
    dict(unit_id="K5-PL06-T01", label="Topik 1 — Proses Memula Kerja",
         scores=dict(source_completeness=0, source_authority=2, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=2, qa_compatibility=2, b02_coupling_exposure=5,
                     expected_proof_value=4, estimated_duration=2),
         note="A process topic is structurally furthest from B02's component catalogue, which is "
              "high coupling exposure but also the highest chance of needing new treatment. "
              "Not a first proof."),
    dict(unit_id="K5-PL06-T02", label="Topik 2 — Elemen Pembinaan Landskap",
         scores=dict(source_completeness=0, source_authority=2, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=3, qa_compatibility=3, b02_coupling_exposure=4,
                     expected_proof_value=4, estimated_duration=3),
         note="An element catalogue is plausibly close to B02's structure. Reasonable runner-up "
              "to T04 on the same evidence footing."),
    dict(unit_id="K5-PL06-T07", label="Topik 7 — Demobilisasi",
         scores=dict(source_completeness=0, source_authority=2, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=2, qa_compatibility=2, b02_coupling_exposure=5,
                     expected_proof_value=3, estimated_duration=2),
         note="Likely the smallest unit and likely process-shaped. 'Likely' is doing all the work "
              "in that sentence — nobody has read it."),
]

SELECTION = dict(
    selected_unit_id="K5-PL06-T04",
    selection_status="SELECTED_CONDITIONAL_PENDING_SOURCE_DELIVERY",
    selection_is_unconditional=False,
    rationale=[
        "It is a different Topik from B02, which is the only way a first scale-out proof can "
        "distinguish portable capability from B02-shaped capability. A build inside Topik 3 that "
        "went green would not tell us which of the two we have.",
        "Its existence and title are source-attested by the frozen PL06 montage — the same class "
        "of evidence available for every other Topik, and the best available for any of them.",
        "It is adjacent to modul ms 238-249, the only page range whose custody chain this project "
        "has ever completed, so the extraction request that unblocks it is a contiguous "
        "continuation rather than a new acquisition.",
        "It scores highest on expected proof value among candidates that are not inside Topik 3.",
    ],
    honest_caveat=
        "This selection is NOT a readiness statement. Every candidate scored ZERO on source "
        "completeness, visual availability, interaction representativeness and quiz completeness, "
        "because no source document exists in custody for any of them. T04 wins a comparison "
        "between units we cannot yet build. The differentiators that decided it — proof value and "
        "extraction adjacency — are planning judgements, not measurements, and the ranking should "
        "be re-run the moment any unit's source actually arrives, because a single page of real "
        "content will outweigh all of it.",
    rejected=[
        dict(unit_id="K5-PL06-T03-BNEXT",
             reason="Same Topik as B02. Highest existence evidence, lowest proof value — a green "
                    "build would most likely be B02's grammar succeeding at B02's shape."),
        dict(unit_id="K5-PL06-T02",
             reason="Equal evidence footing with T04, slightly lower expected proof value. "
                    "Retained as first runner-up."),
        dict(unit_id="K5-PL06-T01",
             reason="A process topic is the most likely to require new treatment, which makes it "
                    "a poor FIRST proof and a good second one."),
        dict(unit_id="K5-PL06-T07",
             reason="Everything asserted about its size and shape is guesswork."),
        dict(unit_id="K5-PL06-T05",
             reason="Not scored separately — same zero source footing, no differentiator."),
        dict(unit_id="K5-PL06-T06",
             reason="Not scored separately — same zero source footing, no differentiator."),
    ],
    required_preconditions=[
        "PRE-01 — the approved module extract covering Topik 4 is delivered, with byte size and "
        "SHA-256, and frozen in the repository (resolves STOP-001)",
        "PRE-02 — the Bahagian boundaries of Topik 4 are stated by a human with authority, "
        "including how many there are and what each is called (resolves STOP-002)",
        "PRE-03 — figures and table photographs are extracted from the delivered range and "
        "hashed into an asset manifest (resolves STOP-003)",
        "PRE-04 — the quiz source and answer key for the selected Bahagian are supplied and "
        "SME-signed (resolves STOP-005)",
        "PRE-05 — the cast binding for non-B02 PL06 units is settled against the ratified "
        "character bank (resolves STOP-006, SRC-ANOM-003)",
        "PRE-06 — written confirmation of Bariah's call approval is received and frozen, "
        "upgrading APPROVAL_RECORD from FIRDAUS_ATTESTED_BARIAH_CALL",
    ],
    expected_end_to_end_path=[
        "1. freeze the delivered source extract and its hash",
        "2. extract and hash figures and table photographs into an asset manifest",
        "3. derive the controlled content module from the source — no content invented",
        "4. derive the screen / state / interaction-item model and its counts from that content",
        "5. re-derive the interaction pattern from the unit's own structure; do NOT import "
        "FAMILY_S / P1 / P2",
        "6. generate the review deck through the shared shell, with the artifact-identity source "
        "carrying the new unit's version line",
        "7. run the portable gate set, then add unit-specific content gates",
        "8. build mutation fixtures for every unit-specific rule",
        "9. render and inspect every page",
        "10. Microsoft PowerPoint smoke — and record it this time",
        "11. Bariah review",
    ],
)

# ==========================================================================================
# 6. PART 7 — EXECUTION PLAN
# ==========================================================================================
# Durations below are split by basis. MEASURED values come from this repository: machine
# runtimes timed in Stage 4.2E-C, and elapsed working blocks read off the commit history.
# Anything with no basis is NOT_EVIDENCED and is not given a number.
MEASURED_BASIS = [
    dict(metric="source acquisition to bound asset manifest", value="25m",
         basis="commit history 31 Jul 04:07 (intake BLOCKED) to 04:32 (14 assets extracted)"),
    dict(metric="controlled model to first complete generated deck", value="1h41m",
         basis="commit history 1 Aug 05:02 (freeze inputs) to 06:43 (regenerate complete v0.4)"),
    dict(metric="ingest to first storyboard, whole first block", value="3h18m",
         basis="commit history 31 Jul 01:39 to 04:57"),
    dict(metric="a full governance correction stage", value="42m",
         basis="commit history 2 Aug 01:37 to 02:19, Stage 4.2E-C"),
    dict(metric="generate 100-page deck", value="under 5s", basis="timed, Stage 4.2E-C"),
    dict(metric="full QA suite, 461 gate records", value="5s", basis="timed, Stage 4.2E-C"),
    dict(metric="mutation replay, 51 fixtures + 5 historical decks", value="3m20s",
         basis="timed, Stage 4.2E-C"),
    dict(metric="render and inspect 100 pages", value="25s", basis="timed, Stage 4.2E-C"),
    dict(metric="Bariah review turnaround", value="14h15m mean of two",
         basis="commit history: 31 Jul 14:34 to 1 Aug 05:02 (14h28m); "
               "1 Aug 11:36 to 2 Aug 01:37 (14h01m). CALENDAR time, not working time."),
    dict(metric="Microsoft PowerPoint smoke", value="NOT_EVIDENCED",
         basis="never executed in this environment"),
]

WAVES = [
    dict(wave="Wave 0", title="First non-B02 proof", units=["K5-PL06-T04"],
         entry_condition="PRE-01 through PRE-05 satisfied"),
    dict(wave="Wave 1", title="Lane A units", units=[],
         entry_condition="a unit is Lane A only after its source is in custody and its structure "
                         "matches an already-supported pattern. No unit qualifies today."),
    dict(wave="Wave 2", title="Lane B units", units=[],
         entry_condition="source mapped, treatment portable with per-unit binding. None today."),
    dict(wave="Wave 3", title="Lane C units after human ruling", units=[],
         entry_condition="new treatment or Bariah ruling obtained. None today."),
    dict(wave="Hold", title="Lane D units", units=["K5-PL06-T01", "K5-PL06-T02",
                                                   "K5-PL06-T03-BNEXT", "K5-PL06-T05",
                                                   "K5-PL06-T06", "K5-PL06-T07"],
         entry_condition="held until source is delivered — this is every remaining unit "
                         "except the Wave 0 selection, which is itself held on PRE-01"),
]

PLAN_ROWS = [
    dict(unit_id="K5-PL06-T04", wave="Wave 0", owner="CC, with FIRDAUS on source delivery",
         dependencies="PRE-01, PRE-02, PRE-03, PRE-04, PRE-05",
         source_extraction="25m", controlled_model="1h41m", generation="5m",
         automated_qa="5m", rendered_inspection="30m",
         powerpoint_smoke="NOT_EVIDENCED", bariah_review="14h15m calendar",
         expected_output_version="v0.1 review candidate",
         blocker="STOP-001, STOP-002, STOP-003, STOP-005, STOP-006"),
]
for _u in ["K5-PL06-T03-BNEXT", "K5-PL06-T01", "K5-PL06-T02", "K5-PL06-T05",
           "K5-PL06-T06", "K5-PL06-T07"]:
    PLAN_ROWS.append(dict(
        unit_id=_u, wave="Hold", owner="FIRDAUS / CAIR — source delivery",
        dependencies="STOP-001, STOP-002",
        source_extraction="NOT_EVIDENCED", controlled_model="NOT_EVIDENCED",
        generation="NOT_EVIDENCED", automated_qa="NOT_EVIDENCED",
        rendered_inspection="NOT_EVIDENCED", powerpoint_smoke="NOT_EVIDENCED",
        bariah_review="NOT_EVIDENCED", expected_output_version="none",
        blocker="no source in custody"))

# Wave 0's working-time total, machine + measured human blocks only. Excludes the Bariah
# review turnaround, which is calendar time and not ours to spend.
WAVE0_WORKING_TIME = "2h46m"
WAVE0_WORKING_TIME_BASIS = ("25m source extraction + 1h41m controlled model + 5m generation + "
                            "5m automated QA + 30m rendered inspection. Every component is a "
                            "measured B02 figure. PowerPoint smoke is excluded because it has "
                            "never been run and no honest number exists for it.")

# ==========================================================================================
# 7. PART 4 — CAPABILITY COVERAGE
# ==========================================================================================
CAPABILITY = [
    dict(unit_id="K5-PL06-T03-B02", lane="LANE_A_EXISTING_SUPPORTED_PATTERN",
         supported_screen_types=["TOPIC_ENTRY", "DIALOG", "ORIENTATION", "GROUP_MASTER",
                                 "GROUP_VISUAL_GATEWAY", "COMPONENT_MAIN", "EXAMPLE_SELECTION",
                                 "EXAMPLE_DETAIL", "EXAMPLE_POPUP", "SPECIFICATION_POPUP",
                                 "COMPLETION_STATE", "RUMUSAN", "QUIZ", "TAMAT"],
         unsupported_screen_types=[],
         supported_interaction_types=["FAMILY_S", "FAMILY_P1", "FAMILY_P2"],
         missing_generator_capability=[], missing_package_oracle=[],
         missing_mutation_fixture=[], missing_visual_binding=[],
         missing_notes_handling=[], missing_quiz_handling=[],
         source_authority_dependency="MS2680, B02-CAIR-INT-001",
         estimated_implementation_effort="0 — delivered"),
]
_UNKNOWN_CAP = dict(
    lane="LANE_D_SOURCE_INCOMPLETE",
    supported_screen_types=["TOPIC_ENTRY", "DIALOG", "ORIENTATION", "RUMUSAN", "QUIZ", "TAMAT"],
    unsupported_screen_types=["UNKNOWN — the unit's screen inventory cannot be derived without "
                              "its source"],
    supported_interaction_types=["none proven — the B02 families are not transferable"],
    missing_generator_capability=["content model for this unit"],
    missing_package_oracle=["no frozen artifact to hash"],
    missing_mutation_fixture=["all unit-specific fixtures"],
    missing_visual_binding=["all — no assets extracted"],
    missing_notes_handling=["unit VO content"],
    missing_quiz_handling=["questions, options and answer key"],
    source_authority_dependency="STOP-001, STOP-002",
    estimated_implementation_effort="NOT_EVIDENCED — cannot be estimated without source")
for _u in UNITS:
    if _u["unit_id"] == "K5-PL06-T03-B02":
        continue
    CAPABILITY.append(dict(unit_id=_u["unit_id"], **_UNKNOWN_CAP))

VERDICT = "PL06_SCALE_OUT_BLOCKED_BY_UNRESOLVED_UNIT_BOUNDARIES"
FORBIDDEN_VERDICTS = ["PL06_STORYBOARDS_COMPLETE", "PL06_READY_FOR_MMD",
                      "PL06_CANONICALLY_FROZEN", "PL06_PRODUCTION_RELEASED"]
