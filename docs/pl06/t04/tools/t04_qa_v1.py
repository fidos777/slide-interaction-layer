# -*- coding: utf-8 -*-
"""Stage 4.2F-B0 QA — typed gates over the T04 controlled extraction.

Every record carries an explicit `gate_type`. Nothing is classified by ID substring.

Two populations:
  * gates over the frozen extract and the emitted artifacts — permanent, they run forever
  * gates over the DOCX itself — `EXTRACTION_TIME_ONLY`. The DOCX is deleted at the end of
    the stage, so those record their result in the extract's `docx_probe` block and this
    suite verifies the recorded evidence. That is disclosed, not glossed: after cleanup the
    DOCX-dependent claims are checked against a record, not against the document.

    python3 docs/pl06/t04/tools/t04_qa_v1.py
"""
import csv, io, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
DOCS = os.path.dirname(T04)
REPO = os.path.dirname(os.path.dirname(DOCS))
sys.path.insert(0, HERE)
import t04_data_v1 as D
import t04_emit_v1 as EMIT

BOUNDARY_INTEGRITY = "BOUNDARY_INTEGRITY"
EXTRACT_COMPLETENESS = "EXTRACT_COMPLETENESS"
AUTHORITY_DISCIPLINE = "AUTHORITY_DISCIPLINE"
INVENTION_GUARD = "INVENTION_GUARD"
PROPAGATION_GUARD = "PROPAGATION_GUARD"
ARTIFACT_AGREEMENT = "ARTIFACT_AGREEMENT"
CUSTODY = "CUSTODY"
ACCOUNTING = "ACCOUNTING"
SUPERSESSION_MARKER = "SUPERSESSION_MARKER"

GATE_TYPES = {BOUNDARY_INTEGRITY, EXTRACT_COMPLETENESS, AUTHORITY_DISCIPLINE, INVENTION_GUARD,
              PROPAGATION_GUARD, ARTIFACT_AGREEMENT, CUSTODY, ACCOUNTING, SUPERSESSION_MARKER}

DELIVERABLES = [n for n, _ in EMIT.FILES] + ["T04_SOURCE_EXTRACT_v1.json"]

# Text that would betray an invented Rumusan or quiz if it appeared in a controlled row.
# Bare "a)" / "b)" were in this list and matched ordinary Malay prose — "jenis baja (organik
# atau kimia)" and "(serangga), penyakit (kulat)" both contain "a)". Option markers are now
# matched only where an option marker can actually be: at the start of a row.
QUIZ_WORDS = ("soalan", "kuiz", "jawapan", "rumusan", "kesimpulan", "pilih satu",
              "pilih semua", "markah lulus")
OPTION_MARKER = re.compile(r"^\s*[a-dA-D][).]\s")


def run():
    res = []

    def chk(gid, gtype, value, expected):
        res.append(dict(gate_id=gid, gate_type=gtype, value=value, expected=expected,
                        ok=value == expected))

    P = D.PROBE
    B = D.BOUNDARY
    ROWS, ASSETS, LISTS, TABLES, T = D.ROWS, D.ASSETS, D.LISTS, D.TABLES, D.TOTALS

    # ==================== 1. DOCX IDENTITY (recorded evidence) ====================
    chk("DOCX_IDENTITY_RECORDED", CUSTODY, P["identity_matches_expected"], True)
    chk("DOCX_BYTES", CUSTODY, P["bytes"], 16832861)
    chk("DOCX_SHA256", CUSTODY, P["sha256"],
        "5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7")
    chk("DOCX_FILENAME", CUSTODY, P["filename"],
        "[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx")
    # The DOCX must not be in the repository, in any form.
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True,
                                 text=True, timeout=60).stdout.split("\n")
    except Exception:
        tracked = []
    chk("GIT_INDEX_READ", CUSTODY, len(tracked) > 100, True)
    chk("SOURCE_DOCX_TRACKED", CUSTODY,
        [t for t in tracked if t.lower().endswith(".docx") and "SKP 2025" in t], [])
    chk("PPTX_ADDED_THIS_STAGE", CUSTODY,
        [t for t in tracked if t.lower().endswith(".pptx") and "/t04/" in t], [])
    chk("DOCX_STAGING_NOT_IN_REPO", CUSTODY,
        os.path.exists(os.path.join(REPO, "tmp")), False)

    # ==================== 2. BOUNDARY ====================
    A = P["anchor_search"]
    chk("RAW_START_ANCHOR_FOUND", BOUNDARY_INTEGRITY, len(A["raw_start_hits"]), 1)
    chk("RAW_START_ANCHOR_STRING", BOUNDARY_INTEGRITY, A["raw_start_anchor"],
        "PENJAAGAAN DAN PENYELENGGARAAN")
    # The canonical spelling must NOT be usable as an extraction anchor.
    chk("CANONICAL_ONLY_ANCHOR_NOT_USED", BOUNDARY_INTEGRITY, A["governed_label_body_hits"], [])
    chk("RAW_STOP_ANCHOR_FOUND", BOUNDARY_INTEGRITY, len(A["raw_stop_hits"]), 1)
    chk("RAW_STOP_ANCHOR_STRING", BOUNDARY_INTEGRITY, A["raw_stop_anchor"],
        "PENGURUSAN KUALITI PROJEK")
    E = P["paragraph_enumeration"]
    chk("START_PARAGRAPH_IS_5220", BOUNDARY_INTEGRITY, E["start_index"], 5220)
    chk("STOP_BEFORE_PARAGRAPH_5360", BOUNDARY_INTEGRITY, E["stop_index"], 5360)
    chk("START_MATCHES_FROZEN_MAP", BOUNDARY_INTEGRITY, E["start_matches_expected"], True)
    chk("STOP_MATCHES_FROZEN_MAP", BOUNDARY_INTEGRITY, E["stop_matches_expected"], True)
    chk("PARAGRAPH_SPAN", BOUNDARY_INTEGRITY, E["span"], 140)
    chk("ENUMERATION_DISCLOSED", BOUNDARY_INTEGRITY,
        E["enumeration_used"].startswith("DIRECT_W_P_CHILDREN_OF_W_BODY"), True)
    chk("ALTERNATE_ENUMERATION_RECORDED", BOUNDARY_INTEGRITY,
        E["alternate_enumeration"]["offset_from_used"], 1314)
    chk("MODULE_PAGES", BOUNDARY_INTEGRITY,
        [B["module_pages"][0], B["module_pages"][1]], [276, 283])
    chk("PAGE_ATTRIBUTION_MATCHES_FROZEN_MAP", BOUNDARY_INTEGRITY,
        P["page_attribution"]["matches_frozen_map"], True)
    chk("DISTINCT_MODULE_PAGES", BOUNDARY_INTEGRITY,
        P["page_attribution"]["distinct_pages"], [276, 277, 278, 279, 280, 281, 282, 283])
    chk("PAGE_ATTRIBUTION_AUTHORITY_DISCLOSED", BOUNDARY_INTEGRITY,
        P["page_attribution"]["authority"], "ADVISORY_CACHED_LAYOUT")
    # T03 and T05 content must be outside the boundary.
    txt = " ".join(r["raw_source_text"] for r in ROWS)
    chk("T05_CONTENT_EXCLUDED", BOUNDARY_INTEGRITY,
        [s for s in ("PENGURUSAN KUALITI PROJEK", "Project Quality Plan", "PQP",
                     "Jaminan Kualiti") if s in txt], [])
    chk("T03_CONTENT_EXCLUDED", BOUNDARY_INTEGRITY,
        [s for s in ("Pencahayaan / Lighting", "Pengairan (Irrigation)", "Badan Air",
                     "Struktur Taman", "Perabot Taman", "Infrastruktur") if s in txt], [])
    chk("FIRST_ROW_IS_THE_START_ANCHOR", BOUNDARY_INTEGRITY,
        ROWS[0]["raw_source_text"], "PENJAAGAAN DAN PENYELENGGARAAN")
    chk("STOP_ANCHOR_NOT_IN_ROWS", BOUNDARY_INTEGRITY,
        [r["row_id"] for r in ROWS
         if r["raw_source_text"] == "PENGURUSAN KUALITI PROJEK"], [])

    # ==================== 3. NORMALISATION ====================
    chk("NORMALISATION_STATUS", AUTHORITY_DISCIPLINE, B["normalisation_status"],
        "RECORDED_NOT_SILENTLY_CORRECTED")
    chk("RAW_AND_GOVERNED_HELD_SEPARATELY", AUTHORITY_DISCIPLINE,
        B["raw_start_anchor"] != B["governed_start_label"], True)
    h1 = ROWS[0]
    chk("H1_RAW_TEXT_PRESERVED", AUTHORITY_DISCIPLINE, h1["raw_source_text"],
        "PENJAAGAAN DAN PENYELENGGARAAN")
    chk("H1_DISPLAY_TEXT_GOVERNED", AUTHORITY_DISCIPLINE, h1["controlled_display_text"],
        "PENJAGAAN DAN PENYELENGGARAAN")
    chk("H1_NORMALISATION_RECORDED", AUTHORITY_DISCIPLINE, h1["normalisation_status"],
        "RECORDED_NOT_SILENTLY_CORRECTED")
    # Exactly one normalisation is authorised. Any other rewrite is unsupported.
    norm = [r["row_id"] for r in ROWS if r["normalisation_status"] != "NOT_NORMALISED"]
    chk("NORMALISED_ROWS", AUTHORITY_DISCIPLINE, norm, ["T04-ROW-001"])
    chk("UNSUPPORTED_NORMALISATION", AUTHORITY_DISCIPLINE,
        [r["row_id"] for r in ROWS
         if r["normalisation_status"] == "NOT_NORMALISED"
         and r["raw_source_text"] != r["controlled_display_text"]
         and r["content_type"] not in ("DIAGRAM", "TABLE")], [])

    # ==================== 4. COMPLETENESS ====================
    chk("BODY_ELEMENTS_IN_SPAN", EXTRACT_COMPLETENESS, T["body_elements_in_span"], 140)
    chk("EVERY_ELEMENT_ACCOUNTED", EXTRACT_COMPLETENESS,
        T["content_rows"] + T["empty_spacing_paragraphs"], T["body_elements_in_span"])
    chk("CONTENT_ROWS", EXTRACT_COMPLETENESS, T["content_rows"], 100)
    chk("CONTENT_TYPE_TOTALS_SUM", EXTRACT_COMPLETENESS,
        T["headings"] + T["paragraphs"] + T["list_item_rows"] + T["tables"] + T["diagrams"],
        T["content_rows"])
    chk("HEADINGS", EXTRACT_COMPLETENESS, T["headings"], 49)
    chk("NUMBERED_PARAGRAPHS", EXTRACT_COMPLETENESS, T["numbered_paragraphs"], 61)
    chk("LIST_INVENTORY_MATCHES_TOTAL", EXTRACT_COMPLETENESS, len(LISTS),
        T["numbered_paragraphs"])
    chk("EVERY_LIST_ITEM_BINDS_TO_A_ROW", EXTRACT_COMPLETENESS,
        [l["list_item_id"] for l in LISTS if l["row_id"] not in D.BY_ID], [])
    chk("TABLES", EXTRACT_COMPLETENESS, T["tables"], 0)
    chk("TABLE_INVENTORY_MATCHES_TOTAL", EXTRACT_COMPLETENESS, len(TABLES), T["tables"])
    chk("DIAGRAMS", EXTRACT_COMPLETENESS, T["diagrams"], 1)
    chk("RASTER_IMAGES", EXTRACT_COMPLETENESS, T["raster_images"], 0)
    chk("ASSET_INVENTORY_MATCHES_TOTAL", EXTRACT_COMPLETENESS, len(ASSETS), T["assets"])
    chk("EVERY_VISUAL_ROW_BINDS_TO_AN_ASSET", EXTRACT_COMPLETENESS,
        [r["row_id"] for r in ROWS if r["content_type"] == "DIAGRAM"
         and r["visual_relationship"] not in {a["asset_id"] for a in ASSETS}], [])
    chk("SEQUENCE_IS_CONTIGUOUS", EXTRACT_COMPLETENESS,
        [r["sequence"] for r in ROWS], list(range(1, len(ROWS) + 1)))
    ids = [r["row_id"] for r in ROWS]
    chk("DUPLICATE_ROW_IDS", EXTRACT_COMPLETENESS,
        sorted({i for i in ids if ids.count(i) > 1}), [])
    aids = [a["asset_id"] for a in ASSETS]
    chk("DUPLICATE_ASSET_IDS", EXTRACT_COMPLETENESS,
        sorted({i for i in aids if aids.count(i) > 1}), [])
    chk("ROWS_WITHOUT_A_PAGE", EXTRACT_COMPLETENESS,
        [r["row_id"] for r in ROWS if not r["module_page"]], [])
    chk("ROWS_OUTSIDE_THE_PAGE_RANGE", EXTRACT_COMPLETENESS,
        [r["row_id"] for r in ROWS if not 276 <= r["module_page"] <= 283], [])

    # ==================== 5. AUTHORITY ====================
    chk("ALL_ROWS_MODULE_SOURCE_ATTESTED", AUTHORITY_DISCIPLINE,
        sorted({r["authority_class"] for r in ROWS}), ["MODULE_SOURCE_ATTESTED"])
    chk("SOURCE_DERIVED_PROMOTED_TO_BARIAH_DIRECT", AUTHORITY_DISCIPLINE,
        [r["row_id"] for r in ROWS if "BARIAH" in str(r["authority_class"])], [])
    chk("ASSET_SUBJECTS_NOT_BARIAH_DIRECT", AUTHORITY_DISCIPLINE,
        [a["asset_id"] for a in ASSETS if "BARIAH" in str(a.get("source_bound_status"))], [])
    chk("ASSET_SOURCE_BOUND_STATUS_VALID", AUTHORITY_DISCIPLINE,
        sorted({a["source_bound_status"] for a in ASSETS}), ["SOURCE_BOUND_CAPTIONLESS"])

    # ==================== 6. INVENTION GUARDS ====================
    chk("INVENTED_RUMUSAN", INVENTION_GUARD,
        [r["row_id"] for r in ROWS
         if any(w in r["controlled_display_text"].lower() for w in ("rumusan", "kesimpulan"))],
        [])
    chk("INVENTED_QUIZ_TEXT", INVENTION_GUARD,
        [r["row_id"] for r in ROWS
         if any(w in r["controlled_display_text"].lower() for w in QUIZ_WORDS)], [])
    chk("INVENTED_QUIZ_OPTION_MARKERS", INVENTION_GUARD,
        [r["row_id"] for r in ROWS
         if OPTION_MARKER.match(r["controlled_display_text"])], [])
    chk("RUMUSAN_STATUS", INVENTION_GUARD,
        next(q["status"] for q in D.QUIZ_COVERAGE if q["item"] == "Rumusan"), "NOT_FOUND")
    chk("QUIZ_STATUS", INVENTION_GUARD,
        next(q["status"] for q in D.QUIZ_COVERAGE if q["item"] == "MCQ questions"), "NOT_FOUND")
    chk("ANSWER_KEY_STATUS", INVENTION_GUARD,
        next(q["status"] for q in D.QUIZ_COVERAGE if q["item"] == "Answer keys"), "NOT_FOUND")
    chk("QUIZ_COMPOSITION_NOT_ASSUMED", INVENTION_GUARD,
        next(q["status"] for q in D.QUIZ_COVERAGE
             if q["item"] == "4 MCQ + 1 MR composition"), "AUTHORITY_UNRESOLVED")
    chk("PASS_THRESHOLD_NOT_ASSUMED", INVENTION_GUARD,
        next(q["status"] for q in D.QUIZ_COVERAGE
             if q["item"] == "60 percent pass threshold"), "AUTHORITY_UNRESOLVED")
    chk("INVALID_COVERAGE_STATUSES", INVENTION_GUARD,
        sorted({q["status"] for q in D.QUIZ_COVERAGE
                if q["status"] not in D.COVERAGE_STATUSES}), [])
    # Every asset subject must come from the diagram's own nodes.
    chk("INVENTED_VISUAL_SUBJECTS", INVENTION_GUARD,
        [a["asset_id"] for a in ASSETS
         if not a.get("source_subject_nodes") or a["node_count"] != len(a["source_subject_nodes"])],
        [])
    chk("DIAGRAM_NODE_COUNT", INVENTION_GUARD, ASSETS[0]["node_count"], 6)
    # A candidate that names source rows must name rows that exist.
    chk("CANDIDATE_ROWS_NOT_IN_EXTRACT", INVENTION_GUARD,
        sorted({r for c in D.SCREEN_CANDIDATES for r in c["source_rows"]
                if r not in D.BY_ID}), [])
    chk("CANDIDATE_WITH_NO_ROWS_IS_PENDING_HUMAN", INVENTION_GUARD,
        [c["candidate_id"] for c in D.SCREEN_CANDIDATES
         if not c["source_rows"] and c["candidate"] != "PENDING_HUMAN"], [])
    chk("INVALID_CANDIDATE_TYPES", INVENTION_GUARD,
        sorted({c["candidate"] for c in D.SCREEN_CANDIDATES
                if c["candidate"] not in D.CANDIDATE_TYPES}), [])

    # ==================== 7. B02 PROPAGATION GUARD ====================
    blob = json.dumps([D.SCREEN_CANDIDATES, D.SOURCE_GAPS, D.QUIZ_COVERAGE,
                       D.EXTERNAL_CLAIMS], ensure_ascii=False)
    for token in D.B02_FORBIDDEN:
        # A named mention inside an explicit prohibition is the point; an ASSERTION is not.
        # Candidates are checked field by field, which is where propagation would live.
        chk(f"B02_PROPAGATION_{token.replace(' ', '_').upper()}", PROPAGATION_GUARD,
            [c["candidate_id"] for c in D.SCREEN_CANDIDATES
             if token.lower() in (c["candidate"] + c["reusable_capability"]).lower()], [])
    chk("B02_CARDINALITIES_IN_CANDIDATES", PROPAGATION_GUARD,
        [c["candidate_id"] for c in D.SCREEN_CANDIDATES
         if "5, 5, 3" in json.dumps(c, ensure_ascii=False)], [])
    # This gate previously scanned the extracted SOURCE TEXT for B02 component names, which
    # was a category error: the rows are lifted verbatim from the module by construction, and
    # "papan tanda" is an ordinary Malay noun — T04 uses it for a warning sign at a spray site.
    # Propagation can only enter through the ANALYSIS layer, so that is what is scanned. The
    # question of whether the extract strayed into another unit is answered by the T03/T05
    # exclusion and page-range gates, which is where it belongs.
    _analysis = json.dumps([D.SCREEN_CANDIDATES, D.SOURCE_GAPS], ensure_ascii=False).lower()
    chk("B02_COMPONENTS_IN_ANALYSIS", PROPAGATION_GUARD,
        [t for t in ("struktur persisir air", "struktur teduhan", "kemudahan awam",
                     "water feature", "kerusi taman", "tong sampah", "drinking fountain")
         if t in _analysis], [])

    # ==================== 8. CLAIMS ====================
    chk("INVALID_CLAIM_STATUSES", AUTHORITY_DISCIPLINE,
        sorted({c["status"] for c in D.EXTERNAL_CLAIMS
                if c["status"] not in D.CLAIM_STATUSES}), [])
    chk("CLAIM_ROWS_NOT_IN_EXTRACT", AUTHORITY_DISCIPLINE,
        sorted({r for c in D.EXTERNAL_CLAIMS for r in c["row_ids"] if r not in D.BY_ID}), [])
    chk("CLAIMS_BLOCKING_THIS_UNIT", AUTHORITY_DISCIPLINE,
        [c["claim_id"] for c in D.EXTERNAL_CLAIMS if c["scope"] == "BLOCKS_THIS_UNIT"], [])
    chk("MS2680_PRESENT_IN_T04", AUTHORITY_DISCIPLINE, "MS2680" in txt or "MS 2680" in txt, False)
    chk("LEGISLATION_CLAIM_FLAGGED", AUTHORITY_DISCIPLINE,
        [c["claim_id"] for c in D.EXTERNAL_CLAIMS
         if c["kind"] == "LEGISLATION" and c["status"] == "EXTERNAL_VERIFICATION_REQUIRED"],
        ["T04-CLM-01"])

    # ==================== 9. READINESS ====================
    chk("INSTRUCTIONAL_STATUS", AUTHORITY_DISCIPLINE, D.READINESS["instructional_status"],
        "CONTENT_ASSESSMENT_PENDING")
    chk("READINESS_TYPE_VALID", AUTHORITY_DISCIPLINE,
        D.READINESS["instructional_status"] in D.READINESS_TYPES, True)
    chk("SOURCE_INCOMPLETE_RETIRED", AUTHORITY_DISCIPLINE,
        "SOURCE_INCOMPLETE" in D.READINESS["other_units"]
        and "retired" in D.READINESS["other_units"], True)
    chk("FORBIDDEN_VERDICT_CLAIMED", AUTHORITY_DISCIPLINE,
        [v for v in D.FORBIDDEN_VERDICT_CLAIMS if v == D.VERDICT], [])
    chk("VERDICT_IS_ALLOWED", AUTHORITY_DISCIPLINE,
        D.VERDICT in ("T04_SOURCE_COMPLETE_READY_FOR_STORYBOARD_MODEL",
                      "T04_SOURCE_COMPLETE_PENDING_TARGETED_INSTRUCTIONAL_DECISIONS",
                      "T04_BLOCKED_BY_SOURCE_GAPS"), True)
    # A "READY_FOR_STORYBOARD_MODEL" verdict is incompatible with an open unit blocker.
    chk("READY_VERDICT_WITH_BLOCKING_GAPS", AUTHORITY_DISCIPLINE,
        D.VERDICT.endswith("READY_FOR_STORYBOARD_MODEL")
        and any(g["severity"] == "BLOCKS_THIS_UNIT" for g in D.SOURCE_GAPS), False)

    # ==================== 10. ARTIFACT AGREEMENT ====================
    for name in DELIVERABLES:
        chk(f"DELIVERABLE_PRESENT::{name}", ARTIFACT_AGREEMENT,
            os.path.exists(os.path.join(T04, name)), True)
    stale = []
    for name, fn in EMIT.FILES:
        p = os.path.join(T04, name)
        if not os.path.exists(p):
            stale.append(name); continue
        b = fn()
        if not b.endswith("\n"):
            b += "\n"
        if open(p, encoding="utf-8").read() != b:
            stale.append(name)
    chk("EMITTED_DELIVERABLES_STALE", ARTIFACT_AGREEMENT, stale, [])
    # CSV totals must equal JSON totals.
    def _rows(name):
        p = os.path.join(T04, name)
        if not os.path.exists(p):
            return None
        body = "".join(l for l in open(p, encoding="utf-8") if not l.startswith("#"))
        return list(csv.DictReader(io.StringIO(body)))
    chk("VISUAL_CSV_MATCHES_JSON", ARTIFACT_AGREEMENT,
        len(_rows("T04_VISUAL_INVENTORY_v1.csv") or []), T["assets"])
    chk("TABLE_CSV_MATCHES_JSON", ARTIFACT_AGREEMENT,
        len(_rows("T04_TABLE_INVENTORY_v1.csv") or []), T["tables"])
    chk("LIST_CSV_MATCHES_JSON", ARTIFACT_AGREEMENT,
        len(_rows("T04_LIST_INVENTORY_v1.csv") or []), T["numbered_paragraphs"])
    md = open(os.path.join(T04, "T04_CONTROLLED_CONTENT_v1.md"), encoding="utf-8").read()
    chk("EVERY_ROW_IN_MARKDOWN", ARTIFACT_AGREEMENT,
        [r["row_id"] for r in ROWS if r["row_id"] not in md], [])
    chk("MARKDOWN_ROW_COUNT_STATED", ARTIFACT_AGREEMENT, f"CONTENT ROWS    = {T['content_rows']}" in md, True)

    # ==================== 11. ACCOUNTING ====================
    g = [r["gate_id"] for r in res]
    chk("DUPLICATE_GATE_IDS", ACCOUNTING, sorted({x for x in g if g.count(x) > 1}), [])
    chk("EVERY_GATE_CARRIES_A_TYPE", ACCOUNTING,
        [r["gate_id"] for r in res if r["gate_type"] not in GATE_TYPES], [])
    return res


def accounting(rows):
    m = [r for r in rows if r["gate_type"] == SUPERSESSION_MARKER]
    a = [r for r in rows if r["gate_type"] != SUPERSESSION_MARKER]
    by = {}
    for r in a:
        by[r["gate_type"]] = by.get(r["gate_type"], 0) + 1
    return dict(TOTAL_EMITTED_GATE_RECORDS=len(rows), SUPERSESSION_MARKERS_PRESENT=len(m),
                ACTIVE_TEST_GATES=len(a), ACTIVE_TEST_GATES_PASSING=sum(1 for r in a if r["ok"]),
                BY_TYPE=dict(sorted(by.items())),
                FAILING=[r["gate_id"] for r in rows if not r["ok"]])


if __name__ == "__main__":
    rows = run(); a = accounting(rows)
    w = max(len(r["gate_id"]) for r in rows); t = max(len(r["gate_type"]) for r in rows)
    for r in rows:
        print(f"{'PASS' if r['ok'] else 'FAIL'}  {r['gate_type']:<{t}}  {r['gate_id']:<{w}}  "
              f"{r['value']!r}" + ("" if r["ok"] else f"   expected {r['expected']!r}"))
    print()
    print(f"{a['ACTIVE_TEST_GATES_PASSING']}/{a['ACTIVE_TEST_GATES']} active gates PASS  ·  "
          f"{a['SUPERSESSION_MARKERS_PRESENT']} supersession markers  ·  "
          f"{a['TOTAL_EMITTED_GATE_RECORDS']} emitted records")
    for k, v in a["BY_TYPE"].items():
        print(f"    {k:<24} {v}")
    sys.exit(1 if a["FAILING"] else 0)
