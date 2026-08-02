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
    # ---- Stage 4.2F-A2 ----
    dict(ref="F1", kind="PRIMARY_SOURCE_ARTIFACT_EXTERNAL",
         path="[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx",
         bytes=16832861,
         sha256="5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7",
         establishes="the complete CE14 module, PL01-PL08. PL06 spans module pages 162-309; "
                     "PL07 begins at 310. Held externally by identity, Drive file ID "
                     "16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4 — not in this repository",
         authority_class="PROOFREAD_FINAL_MODULE_SOURCE"),
    dict(ref="F2", kind="FROZEN_BOUNDARY_MAP",
         path="docs/pl06/source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json",
         bytes=12977,
         sha256="aa02cd3c784113b00c056280fb236f6ae56a48b013fb388bb47011ba6e31c073",
         establishes="the 14-unit PL06 lesson boundary map: per-unit module and rendered-PDF "
                     "page ranges, DOCX paragraph anchors, start and end heading anchors, and "
                     "shared-page flags. Ingested byte-identically from the verified freeze",
         authority_class="DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING"),
]

# ==========================================================================================
# 0A. STAGE 4.2F-A2 — INGEST, CUSTODY AND GROUPING AUTHORITY
# ==========================================================================================
FREEZE_DIR = "docs/pl06/source-freeze"

# Every file ingested from the freeze, with the identity it must still hash to. The QA gate
# INGESTED_FILES_MATCH_FREEZE_HASHES re-hashes each one against FREEZE_MANIFEST.json.
# `manifest_path` is the path the frozen manifest knows it by; None means the hash register
# itself, which cannot contain its own hash.
INGESTED_FILES = [
    ("SOURCE_CUSTODY_RECORD.md", "records/SOURCE_CUSTODY_RECORD.md"),
    ("BOUNDARY_EVIDENCE_REGISTER.md", "records/BOUNDARY_EVIDENCE_REGISTER.md"),
    ("FREEZE_MANIFEST.json", "records/FREEZE_MANIFEST.json"),
    ("SHA256SUMS.txt", None),
    ("PL06_LESSON_BOUNDARY_MAP_v1.md", "derived/PL06_LESSON_BOUNDARY_MAP_v1.md"),
    ("PL06_LESSON_BOUNDARY_MAP_v1.csv", "derived/PL06_LESSON_BOUNDARY_MAP_v1.csv"),
    ("PL06_LESSON_BOUNDARY_MAP_v1.json", "derived/PL06_LESSON_BOUNDARY_MAP_v1.json"),
    ("PACKAGE_README.md", "README.md"),
    ("tools/verify_freeze.sh", "tools/verify_freeze.sh"),
    ("tools/verify_manifest.py", "tools/verify_manifest.py"),
    ("PL06_TOPIK_LIST_USER_SCREENSHOT_2026-08-02.png",
     "derived/PL06_TOPIK_LIST_USER_SCREENSHOT_2026-08-02.png"),
    ("boundary_pages/p294.png", "derived/boundary_pages/p294.png"),
    ("boundary_pages/p302.png", "derived/boundary_pages/p302.png"),
]

# Paths that must NEVER appear in the Git index, by decision.
FORBIDDEN_TRACKED_PATTERNS = [
    ("FULL_DOCX", ".docx", "SKP 2025 PEMBINAAN LANDSKAP LUAR"),
    ("RENDERED_PDF", ".pdf", "SKP 2025 PEMBINAAN LANDSKAP LUAR"),
    ("TRANSPORT_ZIP", ".zip", "PL06_SOURCE_BOUNDARY_EVIDENCE_FREEZE"),
]

# The 14-lesson grouping is anchored to DOCX body headings, but the human authority behind
# THOSE PARTICULAR GROUPINGS is referenced by the map and is not held anywhere we can reach.
# Searched the whole repository for all four identifiers: zero hits outside the freeze
# package's own metadata, which is a reference, not the artifact.
GROUPING_AUTHORITY = dict(
    status="REFERENCED_NOT_FROZEN",
    referenced_identifiers=["SMC-CIDB-K5-DAFTAR-KEPUTUSAN-BARIAH-KONSOLIDASI_v1.0",
                            "K5-STR-004", "K5-STR-006", "K5-STR-005"],
    referenced_from=["docs/pl06/source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json "
                     "-> metadata.lesson_grouping_authority",
                     "docs/pl06/source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.md "
                     "-> K5-STR-005 governs the canonical Topik 4 title",
                     "docs/pl06/source-freeze/SOURCE_CUSTODY_RECORD.md "
                     "-> dependency disclosure"],
    search_result="0 occurrences anywhere in the repository outside the freeze package's own "
                  "metadata",
    what_is_established="the boundaries themselves — every unit's start and end anchor is a "
                        "named DOCX body heading with a paragraph index, independently checkable "
                        "against the source",
    what_is_not_established="why these particular 14 groupings. Two adjacent subtopics being one "
                            "lesson rather than two is a human decision, and the artifact "
                            "recording it is not here",
    canonical_authority_claimed=False,
    blocks_extraction=False,
    blocks_canonical_freeze=True,
    note="Not a blocker for T04 extraction, by explicit instruction and on the merits: the T04 "
         "boundary is a single Topik with a single lesson, so no grouping judgement is involved "
         "in it at all. It matters most for Topik 1, 2 and 3, where 3 + 2 + 5 lessons were "
         "grouped out of subtopics that could have been split differently.")

EXTERNAL_CUSTODY = dict(
    primary_docx=dict(
        filename="[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx",
        bytes=16832861,
        sha256="5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7",
        drive_file_id="16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4",
        drive_folder="https://drive.google.com/drive/folders/1p18qHATFfn0oLHyCvYOfA8rQQlxkwJXS",
        custody="EXTERNAL_DURABLE_SOURCE_BY_IDENTITY",
        tracked_in_git=False),
    freeze_package=dict(
        filename="PL06_SOURCE_BOUNDARY_EVIDENCE_FREEZE_v1.zip",
        bytes=25142903,
        sha256="c32f9bee73f9044f3b041417d6a8955854bc6c1e62045fd5fa96d37b56cd3927",
        durable_location="NOT_YET_SUPPLIED",
        custody="DURABLE_CUSTODY_PENDING",
        shared_team_custody_claimed=False,
        tracked_in_git=False),
    rendered_pdf=dict(
        filename="[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.pdf",
        bytes=9039981,
        sha256="295a1749cf3fce16d9dfd8c3b45b2e3b5c64c1c9a6073ccc26235f81ec6fbb4b",
        pages=350,
        classification="DERIVED_ARTIFACT_PRESERVED_INSIDE_FREEZE_PACKAGE",
        tracked_in_git=False),
    git_lfs="NOT_CONFIGURED",
    record="docs/pl06/source-freeze/PL06_EXTERNAL_CUSTODY_RECORD_v1.md")

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
    # ---- carried in from the freeze package, which recorded rather than corrected them ----
    dict(id="SRC-ANOM-004", evidence="F1",
         locus="module body heading, Topik 4, module page 276",
         verbatim="4.0 PENJAAGAAN DAN PENYELENGGARAAN",
         finding="The body heading of the selected first-proof unit is misspelled in the source. "
                 "The canonical title 'Penjagaan dan Penyelenggaraan' comes from the Table of "
                 "Contents under K5-STR-005. Extraction anchors on the body string as written; "
                 "the learner-facing label uses the canonical form.",
         impact="Directly affects T04-B01 extraction. An anchor search for the correctly spelled "
                "heading finds nothing.",
         owner="BARIAH", status="RECORDED_NOT_SILENTLY_CORRECTED"),
    dict(id="SRC-ANOM-005", evidence="F1",
         locus="module body heading, section 7.2, Topik 7",
         verbatim="Proses Demoblisasi",
         finding="Misspelled in the source body; governed label is 'Proses Demobilisasi'.",
         impact="Affects T07-B01 extraction only.",
         owner="BARIAH", status="RECORDED_NOT_SILENTLY_CORRECTED"),
    dict(id="SRC-ANOM-006", evidence="F1",
         locus="module Table of Contents vs body heading positions",
         verbatim="Several TOC offsets differ from body starts",
         finding="The TOC and the body disagree on where sections begin. The freeze package "
                 "resolves this by BODY_ANCHOR_PRECEDENCE: body heading anchors govern "
                 "extraction, the TOC is cross-check only.",
         impact="Any extraction driven from the TOC would land on the wrong page. This is the "
                "reason the boundary map carries DOCX paragraph indices as well as page ranges.",
         owner="NONE", status="RESOLVED_BY_BODY_ANCHOR_PRECEDENCE"),
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
# Stage 4.2F-B0 typed readiness. "SOURCE_INCOMPLETE" says a unit is not ready; it does not
# say whether that is because nobody has read it, because the treatment is unsettled, or
# because the content is genuinely absent from the module. Those have different owners.
INSTRUCTIONAL_READINESS_VALUES = ["READY_WITH_HOLDS", "SOURCE_PRESENT_CONTENT_NOT_EXTRACTED",
                                  "CONTENT_ASSESSMENT_PENDING", "SOURCE_GAP_CONFIRMED"]

READINESS_VALUES = ["READY", "READY_WITH_HOLDS", "SOURCE_INCOMPLETE",
                    "REQUIRES_BARIAH_DECISION", "UNSUPPORTED_INTERACTION",
                    "SOURCE_AUTHORITY_UNRESOLVED"]

LANE_VALUES = ["LANE_A_EXISTING_SUPPORTED_PATTERN", "LANE_B_SUPPORTED_WITH_SOURCE_MAPPING",
               "LANE_C_NEW_TREATMENT_OR_DECISION_REQUIRED", "LANE_D_SOURCE_INCOMPLETE"]

UNIT_SCOPE_VALUES = ["DELIVERED_BASELINE", "REMAINING"]

# The seven Topik titles are quoted verbatim from M2 slide 3.
# The seven Topik titles and the fourteen lesson units are no longer asserted here. They are
# READ from the frozen boundary map ingested at Stage 4.2F-A2, so this inventory cannot drift
# from the source evidence: change the map and the inventory changes with it, or the hash gate
# fails and nothing is emitted at all.
import json as _json, os as _os

_HERE = _os.path.dirname(_os.path.abspath(__file__))
_DOCS = _os.path.dirname(_HERE)
BOUNDARY_MAP = _os.path.join(_DOCS, "source-freeze", "PL06_LESSON_BOUNDARY_MAP_v1.json")


class BoundaryMapError(RuntimeError):
    """The frozen boundary map is missing or internally inconsistent. Fail closed."""


def _load_map():
    if not _os.path.exists(BOUNDARY_MAP):
        raise BoundaryMapError(f"frozen boundary map missing: {BOUNDARY_MAP}")
    m = _json.load(open(BOUNDARY_MAP, encoding="utf-8"))
    meta, rows = m["metadata"], m["lessons"]
    if len(rows) != meta["lesson_count"]:
        raise BoundaryMapError(f"{len(rows)} rows but lesson_count={meta['lesson_count']}")
    if len({r["topik"] for r in rows}) != meta["topic_count"]:
        raise BoundaryMapError("distinct topik does not equal topic_count")
    return meta, rows


BOUNDARY_META, BOUNDARY_ROWS = _load_map()
_TOPIK = sorted({(r["topik"], r["topik_title"]) for r in BOUNDARY_ROWS})

# Status in the frozen map -> what this inventory records.
DELIVERED_UNIT = "K5-PL06-T03-B02"
PREFERRED_PROOF_UNIT = "K5-PL06-T04-B01"

# Blockers that survive the source ingest. STOP-001 and STOP-002 are closed by it; what
# remains is everything that needs the CONTENT read, plus the cast question.
_REMAINING_BLOCKERS = [
    "CONTROLLED_CONTENT_NOT_EXTRACTED",
    "NO_RUMUSAN_SOURCE",
    "NO_QUIZ_SOURCE",
    "VISUAL_INVENTORY_NOT_EXTRACTED",
    "CAST_BINDING_UNRESOLVED",
]


def _unit_from_map(r, order):
    delivered = r["unit_id"] == DELIVERED_UNIT
    shared = []
    if r["shared_start"]:
        shared.append(f"start page {r['module_start']} shared with the preceding lesson")
    if r["shared_end"]:
        shared.append(f"end page {r['module_end']} shared with the next lesson")
    return dict(
        unit_id=r["unit_id"],
        pl="PL06", topik_number=r["topik"], topik_title=r["topik_title"],
        bahagian_number=r["bahagian"], bahagian_title=r["lesson_title"],
        unit_scope="DELIVERED_BASELINE" if delivered else "REMAINING",
        source_document="[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx",
        source_page_range=f"modul ms {r['module_page_range']} / rendered PDF {r['pdf_page_range']}",
        source_reference=f"F2 — frozen boundary map, {r['unit_id']}: start anchor "
                         f"'{r['start_anchor']}', stop before '{r['end_before']}', "
                         f"DOCX paragraph {r['docx_para_start']} to before {r['docx_para_end_before']}",
        source_authority_class="DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING",
        # The boundary map attests every unit's BOUNDARY. Only B02's CONTENT has additionally
        # been extracted and bound — 26 source rows and 14 assets in STORYBOARD_SOURCE_MAP_v0.4.
        # Claiming FULL_UNIT_CONTENT for a unit nobody has read is the promotion this
        # inventory exists to prevent.
        source_attests="FULL_UNIT_CONTENT" if delivered else "UNIT_BOUNDARY_AND_PAGE_RANGE",
        controlled_content_available=delivered,
        existing_id_input_available=delivered,
        storyboard_input_available=delivered,
        source_rows_count=26 if delivered else None,
        source_figures_count=4 if delivered else None,
        source_tables_count=10 if delivered else None,
        source_assets_count=14 if delivered else None,
        rumusan_available=delivered, quiz_mcq_available=delivered, quiz_mr_available=delivered,
        interaction_requirement="REQUIRED" if delivered else "UNKNOWN",
        interaction_pattern_candidate=(
            "FAMILY_S / FAMILY_P1 / FAMILY_P2 (B02-specific taxonomy)" if delivered
            else "NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION"),
        visual_requirement=("REQUIRED — source-bound overview, 9/9 mapped" if delivered
                            else "UNKNOWN"),
        narration_requirement=("A3 shell grammar, three spoken S01 blocks, screen-level VO only"
                               if delivered else "PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown"),
        terminology_risks=("PL06 pronunciation precedence RESERVED_NOT_ACTIVE; 'BBQ pit' "
                           "lowercase source form measured" if delivered
                           else "PL06 pronunciation precedence unratified; the English-term "
                                "italics list is B02-derived and must be re-derived per unit"),
        standards_or_external_claims=("MS2680 cited in source, verification open" if delivered
                                      else "UNKNOWN — content not read"),
        open_human_decisions=(["MS2680", "B02-CAIR-INT-001", "OD-10 / L-01 LMS navigation"]
                              if delivered else ["CAST_BINDING_PL06_SCOPE"]),
        generator_support_status=("FULLY_SUPPORTED" if delivered
                                  else "SHELL_SUPPORTED_CONTENT_UNSUPPORTED"),
        qa_support_status=("FULLY_SUPPORTED — 461 gate records, 51 mutation fixtures" if delivered
                           else "SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT"),
        lane=("LANE_A_EXISTING_SUPPORTED_PATTERN" if delivered else "LANE_D_SOURCE_INCOMPLETE"),
        readiness_status=("READY_WITH_HOLDS" if delivered else "SOURCE_INCOMPLETE"),
        # Stage 4.2F-B0. SOURCE_INCOMPLETE conflated three states with three different owners.
        # The typed field carries the real one; readiness_status keeps its Stage 4.2F-A
        # vocabulary so the existing gates stay meaningful rather than being renamed away.
        instructional_readiness=(
            "READY_WITH_HOLDS" if delivered
            else "CONTENT_ASSESSMENT_PENDING" if r["unit_id"] == PREFERRED_PROOF_UNIT
            else "SOURCE_PRESENT_CONTENT_NOT_EXTRACTED"),
        blocker_reason=(
            "Delivered and call-approved. Holds are source-authority only and none blocks this "
            "unit's review candidacy: MS2680, B02-CAIR-INT-001, and the LMS navigation ruling. "
            "Microsoft PowerPoint smoke is not recorded."
            if delivered else
            "Source document and unit boundary are now in custody by identity — that is what "
            "Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no "
            "controlled content, no visual inventory, no Rumusan and no quiz source for this "
            "unit."
            + (" Boundary needs heading-anchor extraction, not page slicing: " + "; ".join(shared)
               + "." if shared else " Page boundary is clean.")),
        blocking_conditions=list(_REMAINING_BLOCKERS),
        recommended_execution_order=order,
    )


# Order: 0 = the delivered unit. 1 = the human-designated first scale-out proof. Everything
# else follows MODULE PAGE ORDER, which is mechanical and traceable rather than a judgement.
_rest = sorted((r for r in BOUNDARY_ROWS
                if r["unit_id"] not in (DELIVERED_UNIT, PREFERRED_PROOF_UNIT)),
               key=lambda r: r["module_start"])
_ORDER = {DELIVERED_UNIT: 0, PREFERRED_PROOF_UNIT: 1}
for _i, _r in enumerate(_rest, start=2):
    _ORDER[_r["unit_id"]] = _i

UNITS = [_unit_from_map(r, _ORDER[r["unit_id"]]) for r in BOUNDARY_ROWS]
UNITS.sort(key=lambda u: u["recommended_execution_order"])

# Topology asserted by the frozen boundary evidence register, checked against the map.
TOPOLOGY = {t: sum(1 for r in BOUNDARY_ROWS if r["topik"] == t) for t, _ in _TOPIK}
SHARED_BOUNDARY_PAGES = sorted({r["module_start"] for r in BOUNDARY_ROWS if r["shared_start"]}
                               | {r["module_end"] for r in BOUNDARY_ROWS if r["shared_end"]})

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
    "instructional_readiness",
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
# ==========================================================================================
# 4. PART 6 — STOP CONDITIONS
# ==========================================================================================
STOP_SCOPES = ["BLOCKS_THIS_UNIT", "BLOCKS_CANONICAL_FREEZE_ONLY", "BLOCKS_MMD_ONLY",
               "BLOCKS_FINAL_RELEASE_ONLY"]
STOP_STATUSES = ["OPEN", "RESOLVED"]

_ALL_REMAINING = [u["unit_id"] for u in UNITS if u["unit_scope"] == "REMAINING"]

STOP_CONDITIONS = [
    dict(id="STOP-001", condition="MISSING_APPROVED_SOURCE", status="RESOLVED",
         description="No approved source document for the unit is in custody.",
         scope="BLOCKS_THIS_UNIT", applies_to=[],
         resolver="FIRDAUS / CAIR",
         evidence="CLOSED at Stage 4.2F-A2. The complete module DOCX is in custody by identity "
                  "(F1, 16,832,861 B, sha 5a9142cd…78df7, Drive 16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4). "
                  "This is the item that had blocked every remaining unit since 31 July."),
    dict(id="STOP-002", condition="MISSING_BAHAGIAN_BOUNDARY", status="RESOLVED",
         description="The unit's Bahagian boundaries are not established by any source.",
         scope="BLOCKS_THIS_UNIT", applies_to=[],
         resolver="BARIAH / CAIR",
         evidence="CLOSED at Stage 4.2F-A2. All 14 boundaries carry a named DOCX body heading "
                  "and a paragraph index (F2). Stage 4.2F-A recorded 7 Topik and 1 named "
                  "Bahagian; the map gives 14 units with start and stop anchors."),
    dict(id="STOP-003", condition="VISUAL_INVENTORY_NOT_EXTRACTED", status="OPEN",
         description="No figure or table photograph has been extracted or hashed for the unit, "
                     "so no visual subject can be named without inventing one.",
         scope="BLOCKS_THIS_UNIT", applies_to=list(_ALL_REMAINING),
         resolver="CC — extract from the module page range now that it is known",
         evidence="RP-104, RP-209; B02_ASSET_MANIFEST.md is the precedent for what this produces"),
    dict(id="STOP-004", condition="CONTROLLED_CONTENT_NOT_EXTRACTED", status="OPEN",
         description="The unit's controlled content model has not been derived, so its screen "
                     "inventory and interaction pattern cannot be determined. The B02 families "
                     "must not be assumed.",
         scope="BLOCKS_THIS_UNIT", applies_to=list(_ALL_REMAINING),
         resolver="CC — extract by heading anchor, then BARIAH if the structure is novel",
         evidence="RP-201 to RP-203"),
    dict(id="STOP-005", condition="NO_QUIZ_SOURCE", status="OPEN",
         description="No quiz source or answer key exists for the unit.",
         scope="BLOCKS_THIS_UNIT", applies_to=list(_ALL_REMAINING),
         resolver="CC extraction, then SME sign-off on the key", evidence="RP-108"),
    dict(id="STOP-006", condition="CAST_BINDING_UNRESOLVED", status="OPEN",
         description="The ratified character bank marks Haziq and Encik Roslan CANONICAL; B02 "
                     "ships Alya and Encik Rahman; Bariah's PL06-wide instruction names neither.",
         scope="BLOCKS_THIS_UNIT", applies_to=list(_ALL_REMAINING),
         resolver="BARIAH + CAIR", evidence="SRC-ANOM-003, RP-106, RP-215"),
    dict(id="STOP-007", condition="PL06_PRONUNCIATION_PRECEDENCE_UNRATIFIED", status="OPEN",
         description="The PL06 pronunciation rule ('PL satu', not 'PL kosong satu') appears in "
                     "both montage decks as a Note to MMD but is not a ratified contract.",
         scope="BLOCKS_MMD_ONLY", applies_to=["ALL"], resolver="source governance",
         evidence="M1 and M2 Note to MMD; PRONUNCIATION_REGISTER_PL06_v0.4.4.json"),
    dict(id="STOP-008", condition="MS2680_VERIFICATION", status="OPEN",
         description="A standards citation in the B02 source is unverified.",
         scope="BLOCKS_FINAL_RELEASE_ONLY", applies_to=["K5-PL06-T03-B02"],
         resolver="source authority", evidence="B02_OPEN_DECISION_INVENTORY_v0.4.4"),
    dict(id="STOP-009", condition="B02_CAIR_INT_001", status="OPEN",
         description="The canonical module DOCX had an identity pinned but no hash. Stage "
                     "4.2F-A2 now supplies a hashed module DOCX; whether THIS document is the "
                     "canonical one B02 was built against has not been established.",
         scope="BLOCKS_CANONICAL_FREEZE_ONLY", applies_to=["ALL"], resolver="FIRDAUS / CAIR",
         evidence="B02_V0_4_INPUT_FREEZE.md §1 input E; now checkable against F1"),
    dict(id="STOP-010", condition="K5_COURSE_LOCKED", status="OPEN",
         description="SBAT-ADR-004 §3 locks K2, K3 and K5 in the CAIR decision desk; "
                     "OPEN_COURSES = [\"K4\"]. Governs where DECISIONS may be written, not "
                     "whether storyboards may be produced.",
         scope="BLOCKS_CANONICAL_FREEZE_ONLY", applies_to=["ALL"], resolver="CAIR", evidence="D1"),
    dict(id="STOP-011", condition="POWERPOINT_SMOKE_NOT_RECORDED", status="OPEN",
         description="No Microsoft PowerPoint smoke test has been executed or recorded in this "
                     "environment for any unit.",
         scope="BLOCKS_FINAL_RELEASE_ONLY", applies_to=["ALL"], resolver="FIRDAUS",
         evidence="APPROVAL_RECORD.powerpoint_smoke_status"),
    dict(id="STOP-012", condition="SOURCE_CONTRADICTION", status="OPEN",
         description="The PL06 montage numbers its own topic-list header PL01 while carrying "
                     "PL06's title; the module body carries two heading typos.",
         scope="BLOCKS_FINAL_RELEASE_ONLY", applies_to=["ALL"], resolver="BARIAH",
         evidence="SRC-ANOM-001, SRC-ANOM-004, SRC-ANOM-005"),
    dict(id="STOP-013", condition="GROUPING_AUTHORITY_NOT_FROZEN", status="OPEN",
         description="The human authority behind the 14-lesson grouping is referenced by the "
                     "boundary map and held nowhere we can reach. The BOUNDARIES are anchored to "
                     "named DOCX headings and are independently checkable; WHY these particular "
                     "groupings is not.",
         scope="BLOCKS_CANONICAL_FREEZE_ONLY", applies_to=["ALL"],
         resolver="CAIR — supply SMC-CIDB-K5-DAFTAR-KEPUTUSAN-BARIAH-KONSOLIDASI_v1.0",
         evidence="GROUPING_AUTHORITY = REFERENCED_NOT_FROZEN. Explicitly NOT a blocker for T04 "
                  "extraction: T04 is one Topik with one lesson, so no grouping judgement enters "
                  "it."),
    dict(id="STOP-014", condition="FREEZE_PACKAGE_DURABLE_CUSTODY_PENDING", status="OPEN",
         description="No durable location has been supplied for the 25.1 MB freeze ZIP. Thirteen "
                     "of its files are ingested; the rendered PDF, fifteen boundary images and "
                     "the contact sheet survive only as identities.",
         scope="BLOCKS_CANONICAL_FREEZE_ONLY", applies_to=["ALL"],
         resolver="FIRDAUS — supply the Drive location",
         evidence="EXTERNAL_CUSTODY.freeze_package.custody = DURABLE_CUSTODY_PENDING"),
]

# ==========================================================================================
# 5. PART 5 — FIRST SCALE-OUT SELECTION
# ==========================================================================================
SELECTION_CRITERIA = [
    "source_completeness", "source_authority", "visual_availability",
    "interaction_representativeness", "quiz_completeness", "generator_compatibility",
    "qa_compatibility", "b02_coupling_exposure", "expected_proof_value", "estimated_duration",
]

# Scores are 0-5. A criterion nobody has evidence for still scores 0 — the source ingest moved
# source_completeness and source_authority for every unit, and moved nothing else, because
# nobody has read the content yet.
CANDIDATE_SCORES = [
    dict(unit_id="K5-PL06-T04-B01", label="Topik 4 Bahagian 1 — Penjagaan dan Penyelenggaraan",
         scores=dict(source_completeness=4, source_authority=4, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=3, qa_compatibility=3, b02_coupling_exposure=5,
                     expected_proof_value=5, estimated_duration=4),
         note="Designated PREFERRED_FIRST_SCALE_OUT_PROOF by the freeze package itself. Different "
              "Topik from B02; clean page boundary on both sides — no shared page, no heading "
              "split; the smallest remaining unit at 8 module pages; and the only unit whose "
              "boundary carries frozen visual evidence in this repository (p294, p302)."),
    dict(unit_id="K5-PL06-T03-B03", label="Topik 3 Bahagian 3 — Infrastruktur",
         scores=dict(source_completeness=4, source_authority=4, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=4, qa_compatibility=4, b02_coupling_exposure=1,
                     expected_proof_value=2, estimated_duration=5),
         note="This is what Stage 4.2F-A called T03-BNEXT — the unit Bariah's Tamat ruling sends "
              "the B02 learner to. Smallest of all at 6 module pages, but it sits in B02's own "
              "Topik and both its boundaries are shared pages. A green build here would most "
              "likely be B02's grammar succeeding at B02's shape."),
    dict(unit_id="K5-PL06-T07-B01", label="Topik 7 Bahagian 1 — Demobilisasi",
         scores=dict(source_completeness=4, source_authority=4, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=2, qa_compatibility=2, b02_coupling_exposure=5,
                     expected_proof_value=3, estimated_duration=4),
         note="7 module pages, clean boundaries, three subtopics. Structurally furthest from a "
              "component catalogue, which is high coupling exposure and also the highest chance "
              "of needing new treatment."),
    dict(unit_id="K5-PL06-T05-B01", label="Topik 5 Bahagian 1 — Pengurusan Kualiti Projek",
         scores=dict(source_completeness=4, source_authority=4, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=2, qa_compatibility=2, b02_coupling_exposure=5,
                     expected_proof_value=4, estimated_duration=3),
         note="10 module pages, four subtopics, clean boundaries. Good proof value; larger and "
              "more procedural than T04."),
    dict(unit_id="K5-PL06-T02-B02", label="Topik 2 Bahagian 2 — Mekanikal & Elektrikal (M&E)",
         scores=dict(source_completeness=4, source_authority=4, visual_availability=0,
                     interaction_representativeness=0, quiz_completeness=0,
                     generator_compatibility=3, qa_compatibility=3, b02_coupling_exposure=4,
                     expected_proof_value=4, estimated_duration=3),
         note="11 module pages with a shared start page, so it also exercises heading-anchor "
              "extraction. Worth doing early, but not first — one new variable at a time."),
]

SELECTION = dict(
    selected_unit_id="K5-PL06-T04-B01",
    selection_status="SELECTED_CONDITIONAL_PENDING_CONTENT_EXTRACTION",
    selection_is_unconditional=False,
    rationale=[
        "The freeze package designates it PREFERRED_FIRST_SCALE_OUT_PROOF in the frozen boundary "
        "map — this is no longer only our judgement.",
        "It is a different Topik from B02, which is the only way a first scale-out proof can "
        "distinguish portable capability from B02-shaped capability.",
        "Its boundary is clean on both sides: shared_start and shared_end are both false, and "
        "the map records 'page boundary is clean'. Six of the fourteen units start or end on a "
        "shared page; this one does not, so extraction is not also a test of heading-anchor "
        "splitting.",
        "At 8 module pages (276-283) it is among the smallest units, and it is the only unit "
        "whose start and stop headings are backed by frozen page images in this repository — "
        "p294 for '4.0 PENJAAGAAN DAN PENYELENGGARAAN' and p302 for the '5.0 PENGURUSAN KUALITI "
        "PROJEK' heading that defines its stop.",
        "The 14-lesson grouping authority being unfrozen does not touch it: Topik 4 has exactly "
        "one lesson, so no grouping judgement is involved.",
    ],
    honest_caveat=
        "Stage 4.2F-A2 moved two of ten scoring columns and left eight where they were. Source "
        "completeness and source authority went from 0 to 4 for every unit, because the module "
        "and the boundaries are now in custody. Visual availability, interaction "
        "representativeness and quiz completeness are still ZERO for all fourteen — nobody has "
        "read a single page of content. What changed is that these are now questions we can "
        "answer by working, rather than questions blocked on someone else sending a file. The "
        "selection still cannot be called ready, and the ranking should be re-run the moment T04's "
        "content is extracted, because the first real look at a unit's structure will outweigh "
        "every proxy above it.",
    rejected=[
        dict(unit_id="K5-PL06-T03-B03",
             reason="Same Topik as B02 and both boundaries are shared pages. Was Stage 4.2F-A's "
                    "T03-BNEXT; now fully identified as Infrastruktur, module 250-255."),
        dict(unit_id="K5-PL06-T05-B01",
             reason="Strong second choice — clean boundaries, high proof value — but 10 pages and "
                    "four subtopics against T04's 8 pages and two."),
        dict(unit_id="K5-PL06-T02-B02",
             reason="Shared start page adds heading-anchor extraction as a second new variable."),
        dict(unit_id="K5-PL06-T07-B01",
             reason="Most likely of all to need new treatment, which makes it a poor first proof "
                    "and a useful second."),
        dict(unit_id="K5-PL06-T01-B01",
             reason="Not scored — Topik 1 groups 3 lessons out of 4 subtopics, so it leans "
                    "hardest on the grouping authority that is REFERENCED_NOT_FROZEN."),
        dict(unit_id="K5-PL06-T01-B02", reason="As T01-B01; shared on both boundaries."),
        dict(unit_id="K5-PL06-T01-B03", reason="As T01-B01; shared start page."),
        dict(unit_id="K5-PL06-T02-B01", reason="Shared end page; 15 module pages, the largest."),
        dict(unit_id="K5-PL06-T03-B01", reason="Same Topik as B02; shared end page."),
        dict(unit_id="K5-PL06-T03-B04", reason="Same Topik as B02; shared start page."),
        dict(unit_id="K5-PL06-T03-B05", reason="Same Topik as B02; 14 module pages."),
        dict(unit_id="K5-PL06-T06-B01", reason="Clean boundaries and 9 pages — a reasonable "
                                               "third proof, no differentiator over T04."),
    ],
    required_preconditions=[
        "PRE-01 — CLOSED at Stage 4.2F-A2: the module source is in custody by identity",
        "PRE-02 — CLOSED at Stage 4.2F-A2: the Topik 4 boundary is stated by named heading "
        "anchor, module 276-283, DOCX paragraph 5220 to before 5360",
        "PRE-03 — extract and hash figures and table photographs from module 276-283 into an "
        "asset manifest (resolves STOP-003)",
        "PRE-04 — extract the controlled content model by heading anchor; determine the "
        "interaction pattern from this unit's own structure, not B02's (resolves STOP-004)",
        "PRE-05 — establish Rumusan and quiz source with an SME-signed answer key "
        "(resolves STOP-005)",
        "PRE-06 — settle the cast binding against the ratified character bank (resolves STOP-006)",
        "PRE-07 — written confirmation of Bariah's call approval, upgrading APPROVAL_RECORD from "
        "FIRDAUS_ATTESTED_BARIAH_CALL",
    ],
    expected_end_to_end_path=[
        "1. extract module pages 276-283 from the external DOCX by heading anchor, "
        "paragraph 5220 to before 5360 — not by page slicing",
        "2. extract and hash figures and table photographs into an asset manifest",
        "3. derive the controlled content module from that extract — no content invented",
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
    dict(wave="Wave 0", title="First non-B02 proof", units=["K5-PL06-T04-B01"],
         entry_condition="PRE-03 through PRE-06 satisfied. PRE-01 and PRE-02 closed by the "
                         "Stage 4.2F-A2 source ingest."),
    dict(wave="Wave 1", title="Lane A units", units=[],
         entry_condition="a unit is Lane A only once its content is extracted and its structure "
                         "matches an already-supported pattern. No unit qualifies yet."),
    dict(wave="Wave 2", title="Lane B units", units=[],
         entry_condition="content extracted, treatment portable with per-unit binding. None yet."),
    dict(wave="Wave 3", title="Lane C units after human ruling", units=[],
         entry_condition="new treatment or Bariah ruling obtained. None yet."),
    dict(wave="Hold", title="Lane D units",
         units=[u for u in _ALL_REMAINING if u != "K5-PL06-T04-B01"],
         entry_condition="held until content extraction, which is now unblocked for every one of "
                         "them — the source and the boundaries are in custody"),
]

PLAN_ROWS = [
    dict(unit_id="K5-PL06-T04-B01", wave="Wave 0", owner="CC",
         dependencies="PRE-03, PRE-04, PRE-05, PRE-06",
         source_extraction="25m", controlled_model="1h41m", generation="5m",
         automated_qa="5m", rendered_inspection="30m",
         powerpoint_smoke="NOT_EVIDENCED", bariah_review="14h15m calendar",
         expected_output_version="v0.1 review candidate",
         blocker="STOP-003, STOP-004, STOP-005, STOP-006"),
]
for _u in [u for u in _ALL_REMAINING if u != "K5-PL06-T04-B01"]:
    PLAN_ROWS.append(dict(
        unit_id=_u, wave="Hold", owner="CC — after the Wave 0 proof",
        dependencies="STOP-003, STOP-004, STOP-005, STOP-006",
        source_extraction="NOT_EVIDENCED", controlled_model="NOT_EVIDENCED",
        generation="NOT_EVIDENCED", automated_qa="NOT_EVIDENCED",
        rendered_inspection="NOT_EVIDENCED", powerpoint_smoke="NOT_EVIDENCED",
        bariah_review="NOT_EVIDENCED", expected_output_version="none",
        blocker="content not extracted"))

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
    unsupported_screen_types=["UNKNOWN — the unit's screen inventory cannot be derived until its "
                              "content is extracted from the now-available source"],
    supported_interaction_types=["none proven — the B02 families are not transferable"],
    missing_generator_capability=["content model for this unit"],
    missing_package_oracle=["no generated artifact to hash yet"],
    missing_mutation_fixture=["all unit-specific fixtures"],
    missing_visual_binding=["all — no assets extracted from the unit's page range"],
    missing_notes_handling=["unit VO content"],
    missing_quiz_handling=["questions, options and answer key"],
    source_authority_dependency="STOP-003, STOP-004, STOP-005, STOP-006",
    estimated_implementation_effort="NOT_EVIDENCED — estimable only after extraction")
for _u in UNITS:
    if _u["unit_id"] == "K5-PL06-T03-B02":
        continue
    CAPABILITY.append(dict(unit_id=_u["unit_id"], **_UNKNOWN_CAP))

VERDICT = "PL06_SOURCE_BOUNDARY_INGEST_COMPLETE_READY_FOR_T04_EXTRACTION"
FORBIDDEN_VERDICTS = ["PL06_STORYBOARDS_COMPLETE", "PL06_READY_FOR_MMD",
                      "PL06_CANONICALLY_FROZEN", "PL06_PRODUCTION_RELEASED"]
