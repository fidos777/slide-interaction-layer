# -*- coding: utf-8 -*-
"""Stage 4.2F-D — scoped source locations, the granular status model, T04 page
reconciliation, the K5 PL01-PL08 inventory, four-deck readiness and the production queue.

    python3 docs/source/tools/src_run2_v1.py

The status change is the point of this module. `SOURCE_READY` was one word covering four
very different situations — a file nobody has found, a file the connector can name, a file on
local disk, and a file whose content has been read. A queue built on that word cannot say
which units could be worked on this afternoon. The granular states below can, and
IMMEDIATELY_EXECUTABLE_UNITS is the number that follows from them.
"""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
DOCS = os.path.dirname(SRC_DIR)
PL06 = os.path.join(DOCS, "pl06")
REPO = os.path.dirname(DOCS)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(PL06, "tools"))
import src_authority_v1 as A       # noqa: E402
import src_inventory_v1 as INV     # noqa: E402
import pl06_extract_v1 as EX       # noqa: E402
import pl06_extract_rest_v1 as R   # noqa: E402
import pl06_batch1_data_v1 as B    # noqa: E402
import src_k3_v1 as K3             # noqa: E402

STAGE = "4.2F-D"
AUTHORITY = "SRC-AUTH-01"
SUITE_ID = "PROJECT_SOURCE_READINESS_QA_v1"
PENDING_PACKAGE = "K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2.docx"

# ==========================================================================================
# LANE 0 — scoped location statuses. No unqualified "missing".
# ==========================================================================================
SCOPED_STATUSES = [
    "NOT_FOUND_IN_REPOSITORY",
    "FOUND_IN_UPLOADED_ARCHIVE",
    "LOCATED_BY_CONNECTOR_BINARY_NOT_LOCAL",
    "NOT_FOUND_IN_LOCATIONS_SEARCHED",
]

LOCATIONS_SEARCHED = [
    dict(location="the repository working tree",
         method="find over every .pdf and .zip", result="no PDF or ZIP of any kind"),
    dict(location="/root/.claude/uploads/<session>",
         method="directory listing", result="4 ZIPs and 1 PDF; sizes read"),
    dict(location="every ZIP on the filesystem",
         method="enumerated each archive's members for .pdf",
         result="one PDF — the K5 module render, inside the PL06 freeze package"),
    dict(location="/mnt/attach, /mnt/user-data, /media",
         method="directory listing", result="/mnt/attach empty; /mnt/user-data/working "
                                            "empty; /media empty"),
    dict(location="whole filesystem by name",
         method="find -iname '*LANDASAN*'", result="no match"),
    dict(location="whole filesystem by exact size",
         method="find for a file of exactly 25,043,306 bytes", result="no match"),
    dict(location="the Hermes connector",
         method="list_dir on ~/Hermes, ~/Hermes/00_inbox and ~/Hermes/inbox",
         result="reachable; scoped to ~/Hermes; inbox empty, 00_inbox holds one 0-byte "
                "markdown file. No course source in it."),
    dict(location="Google Drive",
         method="connector search under the official source root",
         result="K2 monolith located: metadata and byte size returned, binary not "
                "transferable through a text channel"),
]

LOCATIONS_NOT_SEARCHED = [
    dict(location="the wider Google Drive outside the official source root",
         reason="SRC-AUTH-01 scopes processing to the official project source packages; "
                "searching a user's whole Drive is outside it."),
    dict(location="Hermes paths above ~/Hermes",
         reason="the connector is scoped to ~/Hermes and refuses paths above it."),
    dict(location="any location requiring credentials this session does not hold",
         reason="none were attempted, so none is reported as empty."),
]

CONNECTOR_STATUS = [
    dict(connector="Google Drive", reachable=True,
         capability="metadata, folder listing, whole-file text extraction",
         cannot="return a binary to local disk, or return a bounded page range"),
    dict(connector="Hermes (ngrok)", reachable=True,
         capability="list, stat and read files under ~/Hermes",
         cannot="reach anything outside ~/Hermes"),
]


def source_locations():
    k2 = A.K2_MONOLITH
    return dict(
        stage=STAGE, scoped_statuses=SCOPED_STATUSES,
        locations_searched=LOCATIONS_SEARCHED,
        locations_not_searched=LOCATIONS_NOT_SEARCHED,
        connector_status=CONNECTOR_STATUS,
        packages=[
            dict(package="K5 module DOCX", course="K5",
                 status="FOUND_IN_UPLOADED_ARCHIVE",
                 detail="inside 0ded4af4-PL06_SOURCE_BOUNDARY_EVIDENCE_FREEZE_v1.zip",
                 binary_or_metadata="BINARY", sha256=A.K5_DOCX_SHA256,
                 bytes=A.K5_DOCX_BYTES),
            dict(package="K5 module rendered PDF", course="K5",
                 status="FOUND_IN_UPLOADED_ARCHIVE",
                 detail="same archive, derived/ folder",
                 binary_or_metadata="BINARY", sha256=A.K5_PDF_SHA256,
                 bytes=A.K5_PDF_BYTES),
            dict(package="K3 nine PL PDFs", course="K3",
                 status="LOCATED_BY_CONNECTOR_BINARY_NOT_LOCAL",
                 detail=f"Drive folder {A.K3_FOLDER_ID}; text readable through the "
                        f"connector, binaries not on local disk",
                 binary_or_metadata="METADATA_PLUS_TEXT", sha256=A.NOT_COMPUTED,
                 bytes=sum(p["bytes"] for p in A.K3_PDFS)),
            dict(package="K2 monolith PDF", course="K2",
                 status="LOCATED_BY_CONNECTOR_BINARY_NOT_LOCAL",
                 also="NOT_FOUND_IN_REPOSITORY, NOT_FOUND_IN_LOCATIONS_SEARCHED",
                 detail=f"Drive file {k2['drive_id']}; every local location above was "
                        f"searched and none holds it",
                 binary_or_metadata="METADATA_ONLY", sha256=A.NOT_COMPUTED,
                 bytes=k2["bytes"]),
        ],
        uploaded_archives=[
            dict(name="0ded4af4-PL06_SOURCE_BOUNDARY_EVIDENCE_FREEZE_v1.zip",
                 bytes=25142903, contains_source=True,
                 note="the K5 module DOCX and its rendered PDF, both hash-verified"),
            dict(name="f28cd846-B02_BARIAH_DECISIONS_20260801_1906.zip", bytes=960602,
                 contains_source=False, note="B02 decision evidence, no PDF members"),
            dict(name="07818d39-B02_BARIAH_EVIDENCE_20260801.zip", bytes=772667,
                 contains_source=False, note="no PDF members"),
            dict(name="b9e81ee5-B02_OVERVIEW_CARDINALITY_EVIDENCE_20260802.zip",
                 bytes=744564, contains_source=False, note="no PDF members"),
            dict(name="6a5c03ec-K5_PL06_T03_B02_pages_256269.pdf", bytes=429918,
                 contains_source=True,
                 note="B02's own source page slice, already delivered"),
        ])


# ==========================================================================================
# LANE 1 — the granular source-status model
# ==========================================================================================
STATES = ["SOURCE_NOT_LOCATED", "SOURCE_LOCATED_BY_CONNECTOR", "SOURCE_BINARY_LOCAL",
          "SOURCE_BINARY_READABLE", "SOURCE_CONTENT_READ", "BOUNDARY_CONFIRMED",
          "EXTRACTED", "MODEL_READY", "WAITING_AUTHORITY", "READY_TO_EMIT_PPTX",
          "STORYBOARD_GENERATED", "QA_PASSED", "FROZEN", "PACKAGED"]

SOURCE_READY_ALIAS = dict(
    retired_status="SOURCE_READY",
    why=("One word covered four different situations: a file nobody had found, a file the "
         "connector could name, a file on local disk, and a file whose content had been "
         "read. A queue built on it cannot answer which units could be worked on this "
         "afternoon, which is the only question the queue exists to answer."),
    interpretation=[
        dict(old="SOURCE_READY on a K5 PL06 row",
             new="SOURCE_BINARY_READABLE + BOUNDARY_CONFIRMED",
             because="the module DOCX is local and hash-verified and the unit's anchors "
                     "resolve in it"),
        dict(old="SOURCE_READY on a K5 PL01-PL08 candidate row",
             new="SOURCE_BINARY_READABLE",
             because="the binary is readable but no frozen unit boundary exists for it"),
        dict(old="SOURCE_READY on a K3 row",
             new="SOURCE_LOCATED_BY_CONNECTOR, or SOURCE_CONTENT_READ where the PDF was "
                 "actually read",
             because="no K3 binary is on local disk; text came through the connector"),
        dict(old="SOURCE_BLOCKED on the K2 row",
             new="SOURCE_LOCATED_BY_CONNECTOR",
             because="the file is located and identified; it is the binary that is not "
                     "local, and 'blocked' hid that distinction"),
    ],
    retired_metric=dict(
        metric="97.8 percent source-ready",
        why_retired=("It counted a located K2 monolith and 30 unmapped K5 candidates as "
                     "ready. It was arithmetically correct and practically meaningless."),
        replaced_by="IMMEDIATELY_EXECUTABLE_UNITS"))

IMMEDIATELY_EXECUTABLE_DEFINITION = dict(
    name="IMMEDIATELY_EXECUTABLE_UNITS",
    conditions=["binary readable", "project processing authority inherited",
                "boundary confirmed", "no technical source blocker"],
    excludes=["units whose source is only located by a connector",
              "candidate structures with no frozen boundary",
              "anything whose binary is not readable in this environment"],
    note="A located record is not an executable unit. That distinction is the whole reason "
         "for the state list.")


# ==========================================================================================
# LANE 7 — T04 page-reference reconciliation
# ==========================================================================================
def t04_page_reconciliation():
    idx = EX.pdf_page_index()
    path = os.path.join(PL06, "t04", "T04_SOURCE_EXTRACT_v1.json")
    if not os.path.exists(path):
        return dict(ran=False, reason="T04 extract not on disk")
    d = json.load(open(path, encoding="utf-8"))
    lo, hi = d["boundary"]["module_pages"]
    window = [p for p in range(lo, hi + 1) if p in idx]
    flat = {p: " ".join(idx[p].split()) for p in window}
    rows, unresolved, cur = [], [], lo
    for r in d["rows"]:
        t = " ".join((r["raw_source_text"] or "").split())[:60]
        if len(t) < 12:
            unresolved.append(r["row_id"])
            continue
        hit = next((p for p in window if p >= cur and t in flat[p]), None)
        if hit is None:
            unresolved.append(r["row_id"])
            continue
        cur = hit
        if hit != r["module_page"]:
            rows.append(dict(row_id=r["row_id"], old_module_page=r["module_page"],
                             old_rendered_pdf_page=r["module_page"] + 18,
                             pdf_oracle_module_page=hit,
                             pdf_oracle_rendered_page=hit + 18,
                             delta=hit - r["module_page"],
                             status="CORRECTED_IN_THIS_RECORD",
                             text=t[:60]))
    pages = [r["module_page"] for r in d["rows"]]
    return dict(
        ran=True, record_id="T04_PAGE_REFERENCE_RECONCILIATION",
        unit_id="K5-PL06-T04-B01",
        oracle="rendered PDF, hash-verified, footer-numbered; searched inside the unit's own "
               "page window, forward-only",
        rows_total=len(d["rows"]), rows_resolved=len(d["rows"]) - len(unresolved),
        rows_unresolved=len(unresolved), unresolved_row_ids=unresolved,
        mismatches=len(rows), corrections=rows,
        old_span=[min(pages), max(pages)], frozen_map_span=[lo, hi],
        oracle_span=[lo, max([r["pdf_oracle_module_page"] for r in rows] + [max(pages)])],
        cause=("The committed T04 extract attributed pages by counting Word's cached "
               "<w:lastRenderedPageBreak>. That method drifts, and here it drifts by one "
               "from module page 281 onward, ending the unit on 282 while the frozen map "
               "says 283. It is the same defect Stage 4.2F-C found in the batch 1 units, "
               "present in T04's own extract."),
        learner_or_reviewer_facing=dict(
            module_page_appears_in_storyboard_pptx=False,
            module_page_appears_in_state_appendix_pptx=False,
            method="both decks re-opened from disk, slide text extracted, searched for page "
                   "phrases and for bare numbers 276-283",
            finding="no module page number reaches either deck"),
        regeneration_decision=dict(
            regenerate=False,
            reason="The brief regenerates only when a page-reference error is embedded in a "
                   "learner-facing or reviewer-facing artifact. It is not: the drift lives "
                   "in internal JSON registers. Regenerating the storyboard to fix a number "
                   "nobody can see would churn a reviewed artifact for nothing."),
        affected_artifacts=["docs/pl06/t04/T04_SOURCE_EXTRACT_v1.json",
                            "any register projected from its module_page field"],
        scope_note="This record reconciles page references only. No T04 content, interaction "
                   "or authority decision is reopened.")


# ==========================================================================================
# LANE 6 — K5 PL01-PL08, confirmed or revised
# ==========================================================================================
def k5_structures():
    """Candidate structures re-derived, not carried forward from the previous queue."""
    base = INV.k5_remaining_inventory()
    idx = EX.pdf_page_index()
    out = []
    for r in base["rows"]:
        is_pl06 = r["pl"] == "PL06"
        subs = r["sub_modul"]
        pages = [s["page"] for s in subs]
        dupes = sorted({p for p in pages if pages.count(p) > 1})
        for i, s in enumerate(subs, 1):
            nxt = subs[i]["page"] if i < len(subs) else r["module_pages"][1] + 1
            shared = s["page"] in dupes or (i < len(subs) and subs[i]["page"] == s["page"])
            out.append(dict(
                course="K5", pl=r["pl"], topic=r["title"], subtopic=s["text"],
                record_type=("CONFIRMED_UNIT" if is_pl06 else "CANDIDATE_STRUCTURE"),
                candidate_id=(None if is_pl06 else f"{r['pl']}-CAND-{i:02d}"),
                source_page_span=[s["page"], max(s["page"], nxt - 1)],
                source_page_span_basis="rendered PDF footer",
                docx_heading_anchor=s["text"], paragraph_start=s["paragraph"],
                paragraph_span_note=("exact span needs the next heading's paragraph; "
                                     "recorded per sub-modul, not per unit"),
                shared_boundary_risk=shared,
                source_completeness="COMPLETE_BODY_TEXT_PRESENT",
                assessment_available=False,
                assessment_note="K5 carries no LATIHAN or SKEMA JAWAPAN anywhere in the "
                                "module",
                granularity=("frozen unit boundary map" if is_pl06
                             else "one sub-modul heading — granularity NOT decided"),
                status=("CONFIRMED" if is_pl06 else "AMBER" if shared else "CLEAN")))
    cand = [r for r in out if r["record_type"] == "CANDIDATE_STRUCTURE"]
    return dict(
        pakej_latihan=len(base["rows"]),
        scope_requested=["PL01", "PL02", "PL03", "PL04", "PL05", "PL07", "PL08"],
        previous_candidate_count=22,
        recomputed_candidate_count=len(cand),
        count_confirmed=len(cand) == 22,
        recount_note=("Re-derived from the module's own syllabus and body headings rather "
                      "than carried forward. The number is the same, and it is the same "
                      "because the evidence is the same, not because it was inherited."),
        confirmed_units=len([r for r in out if r["record_type"] == "CONFIRMED_UNIT"]),
        clean_candidates=len([r for r in cand if r["status"] == "CLEAN"]),
        amber_candidates=len([r for r in cand if r["status"] == "AMBER"]),
        unmapped_source_regions=len({r["pl"] for r in cand}),
        unmapped_pages=sum(r["page_count"] for r in base["rows"] if r["pl"] != "PL06"),
        rows=out,
        extraction_decision=dict(
            performed=False,
            reason=("A CANDIDATE_STRUCTURE is a sub-modul heading, not a unit. Extracting "
                    "one would fix a unit granularity nobody has decided — how many units a "
                    "55-page PL03 becomes is exactly the judgement the frozen boundary map "
                    "encodes for PL06 and does not encode for any other PL. Boundary "
                    "evidence is prepared; the grouping decision is not invented."),
            what_is_prepared="heading anchor, paragraph start and PDF page span for every "
                             "candidate structure",
            what_is_needed="a unit boundary map for PL01-PL05, PL07 and PL08, of the kind "
                           "that already exists for PL06"),
        findings=base["findings"])


# ==========================================================================================
# LANE 9 — four-deck calibration readiness
# ==========================================================================================
CALIBRATION_UNITS = ["K5-PL06-T03-B03", "K5-PL06-T03-B04",
                     "K5-PL06-T05-B01", "K5-PL06-T06-B01"]

NEXT_STAGE_TRIGGER = dict(
    trigger="BARIAH_K5_PATTERN_PACKAGE_INGESTED AND UNIT_EXCEPTION_BLOCKERS_RESOLVED",
    steps=["ingest Bariah v1.2", "apply approved defaults", "mark exceptions",
           "generate four storyboard decks", "read back PPTX", "render and inspect",
           "submit one-touch review", "measure cycle time and correction rate"])


def calibration_readiness():
    b1 = os.path.join(PL06, "batch1_extract")
    summary_path = os.path.join(b1, "PL06_BATCH1_EXTRACTION_SUMMARY_v1.json")
    summary = json.load(open(summary_path, encoding="utf-8")) if os.path.exists(
        summary_path) else dict(units=[])
    by = {u["unit_id"]: u for u in summary["units"]}
    rows = []
    for uid in CALIBRATION_UNITS:
        stem = uid.replace("-", "_")
        ex_p = os.path.join(b1, f"{stem}_SOURCE_EXTRACT_v1.json")
        md_p = os.path.join(b1, f"{stem}_PROVISIONAL_MODEL_v1.json")
        m = json.load(open(md_p, encoding="utf-8")) if os.path.exists(md_p) else {}
        u = by.get(uid, {})
        rows.append(dict(
            unit_id=uid,
            source_verified=True,
            source_verification="module DOCX hash-verified; anchors resolved in the binary",
            extraction_complete=os.path.exists(ex_p),
            extraction_rows=u.get("rows"),
            provisional_model_complete=os.path.exists(md_p),
            unresolved_pattern_decisions=[
                "pattern family — PENDING_BARIAH_PATTERN_DECISION",
                "screen count ceiling — UNKNOWN_PENDING_PATTERN_DECISION",
                "Rumusan beat count — proposed, not approved",
                "dialogue verdict — proposed, not approved",
            ],
            unresolved_unit_exceptions=(
                [x["item"] for x in m.get("ambiguity_register", {}).get("items", [])]),
            assessment_readiness=dict(
                items_drafted=len(m.get("assessment", {}).get("items", [])),
                key_status=m.get("assessment", {}).get("key_status"),
                blocker="no approved answer key"),
            visual_obligation_readiness=dict(
                subjects=m.get("visual_obligations", {}).get("count"),
                source_attested=m.get("visual_obligations", {}).get("source_attested"),
                blocker=("no source figure behind the proposed subjects"
                         if not m.get("visual_obligations", {}).get("source_attested")
                         else "one subject is source-attested; the rest are text readings")),
            cast_blocker="STOP-006 open — no character may be named",
            emit_entry_point=dict(
                command=("python3 docs/pl06/tools/pl06_storyboard_emit_v1.py "
                         f"--unit {uid}"),
                exists_yet=False,
                note=("The emitter is not written and deliberately so — its inputs are the "
                      "pattern decisions that have not arrived. What exists is the model it "
                      "will read: "
                      f"docs/pl06/batch1_extract/{stem}_PROVISIONAL_MODEL_v1.json")),
            ready_to_emit=False,
            what_would_make_it_ready=NEXT_STAGE_TRIGGER["trigger"]))
    return dict(units=rows, trigger=NEXT_STAGE_TRIGGER,
                all_source_verified=all(r["source_verified"] for r in rows),
                all_extracted=all(r["extraction_complete"] for r in rows),
                all_modelled=all(r["provisional_model_complete"] for r in rows),
                any_ready_to_emit=any(r["ready_to_emit"] for r in rows))


# ==========================================================================================
# LANE 10 — the granular queue
# ==========================================================================================
COLUMNS = ["course", "pl", "unit_or_candidate_id", "record_type", "source_located",
           "binary_local", "binary_readable", "content_read", "boundary_confirmed",
           "extraction_status", "model_status", "authority_dependency",
           "immediately_executable", "ready_to_emit_pptx", "blocker_owner",
           "exact_blocker", "next_executable_action"]

RECORD_TYPES = ["CONFIRMED_PRODUCTION_UNIT", "CANDIDATE_STRUCTURE", "UNRESOLVED_SOURCE"]


def _row(**kw):
    r = {c: kw.get(c) for c in COLUMNS}
    return r


def queue_rows():
    rows = []
    b1 = os.path.join(PL06, "batch1_extract")
    rest = os.path.join(PL06, "rest_extract")
    inv = INV.inventory()
    k5 = k5_structures()

    def have(d, stem, suffix):
        return os.path.exists(os.path.join(d, f"{stem}{suffix}"))

    # ---- PL06: all 14 mapped units ----
    lessons = json.load(open(B.BOUNDARY_MAP_PATH, encoding="utf-8"))["lessons"]
    for l in lessons:
        uid = l["unit_id"]
        stem = uid.replace("-", "_")
        in_b1 = have(b1, stem, "_SOURCE_EXTRACT_v1.json")
        in_rest = have(rest, stem, "_SOURCE_EXTRACT_v1.json")
        modelled = (have(b1, stem, "_PROVISIONAL_MODEL_v1.json")
                    or have(rest, stem, "_PROVISIONAL_MODEL_v1.json"))
        delivered = uid == "K5-PL06-T03-B02"
        t04 = uid == "K5-PL06-T04-B01"
        extracted = in_b1 or in_rest or delivered or t04
        rows.append(_row(
            course="K5", pl="PL06", unit_or_candidate_id=uid,
            record_type="CONFIRMED_PRODUCTION_UNIT",
            source_located=True, binary_local=True, binary_readable=True,
            content_read=extracted, boundary_confirmed=True,
            extraction_status="EXTRACTED" if extracted else "SOURCE_BINARY_READABLE",
            model_status=("PACKAGED" if delivered else
                          "MODEL_READY" if (modelled or t04) else "SOURCE_BINARY_READABLE"),
            authority_dependency=("NONE" if delivered else PENDING_PACKAGE),
            immediately_executable=not delivered,
            ready_to_emit_pptx=False,
            blocker_owner=("none" if delivered else "BARIAH"),
            exact_blocker=("none — delivered" if delivered else
                           "pattern package under review; STOP-006 cast binding open"),
            next_executable_action=("none" if delivered else
                                    "await pattern decisions, then project the model")))

    # ---- K5 candidate structures ----
    for c in k5["rows"]:
        if c["record_type"] != "CANDIDATE_STRUCTURE":
            continue
        rows.append(_row(
            course="K5", pl=c["pl"], unit_or_candidate_id=c["candidate_id"],
            record_type="CANDIDATE_STRUCTURE",
            source_located=True, binary_local=True, binary_readable=True,
            content_read=False, boundary_confirmed=False,
            extraction_status="SOURCE_BINARY_READABLE",
            model_status="NOT_STARTED",
            authority_dependency="unit boundary map for this Pakej Latihan",
            immediately_executable=False,
            ready_to_emit_pptx=False, blocker_owner="CAIR",
            exact_blocker="no frozen unit boundary map for this Pakej Latihan; "
                          "unit granularity undecided",
            next_executable_action="map unit boundaries for this PL the way PL06's "
                                   "fourteen were mapped"))

    # ---- K3 ----
    # Sourced from the Stage 4.2F-D K3 model, not the Stage 4.2F-C inventory. Two things
    # were wrong while the older source was in use and both are corrected here:
    #
    #   * every K3 row was stamped K3-M01-<PL>, because M01 was the only module code known
    #     when two of nine packages had been read. Seven of the nine are not M01. The queue
    #     and the K3 model were therefore naming the same unit two different ways.
    #   * rows were split BARIAH / CAIR on read-versus-unread. All nine are now read, so
    #     that split has no members on the CAIR side and the real blocker is the same for
    #     every K3 row: K3-COURSE-01.
    k3 = K3.k3_inventory()
    modelled_pls = {m["pl"] for m in K3.k3_models()}
    for r in k3["rows"]:
        read = r["read_status"] == "CONNECTOR_TEXT_READ_IN_FULL"
        rows.append(_row(
            course="K3", pl=r["pl"],
            unit_or_candidate_id=f"K3-{r['module_code']}-{r['pl']}",
            record_type=("CONFIRMED_PRODUCTION_UNIT" if read else "CANDIDATE_STRUCTURE"),
            source_located=True, binary_local=False, binary_readable=False,
            content_read=read, boundary_confirmed=read,
            extraction_status="SOURCE_CONTENT_READ" if read
            else "SOURCE_LOCATED_BY_CONNECTOR",
            model_status="MODEL_READY" if r["pl"] in modelled_pls else "NOT_STARTED",
            authority_dependency="K3-COURSE-01 assessment treatment",
            immediately_executable=False,
            ready_to_emit_pptx=False,
            blocker_owner="BARIAH" if read else "CAIR",
            exact_blocker=("K3-COURSE-01 assessment treatment undecided" if read
                           else "PDF located but not read"),
            next_executable_action=("await K3-COURSE-01" if read
                                    else "read the PDF through the connector")))

    # ---- K2 ----
    rows.append(_row(
        course="K2", pl="MONOLITH", unit_or_candidate_id="K2-MONOLITH-UNRESOLVED",
        record_type="UNRESOLVED_SOURCE",
        source_located=True, binary_local=False, binary_readable=False,
        content_read=False, boundary_confirmed=False,
        extraction_status="SOURCE_LOCATED_BY_CONNECTOR",
        model_status="NOT_STARTED",
        authority_dependency="none — this is a source-access blocker, not an authority one",
        immediately_executable=False, ready_to_emit_pptx=False,
        blocker_owner="FIRDAUS",
        exact_blocker=f"binary not local: Drive {A.K2_MONOLITH['drive_id']}, "
                      f"{A.K2_MONOLITH['bytes']:,} bytes, searched in every local location "
                      f"and not found",
        next_executable_action="place the PDF on local disk; PyMuPDF is already available"))
    return rows


def queue_summary():
    rows = queue_rows()
    imm = [r for r in rows if r["immediately_executable"]]
    return dict(
        stage=STAGE, columns=COLUMNS, states=STATES, record_types=RECORD_TYPES,
        alias_map=SOURCE_READY_ALIAS,
        headline=IMMEDIATELY_EXECUTABLE_DEFINITION,
        counts=dict(
            confirmed_production_units=len([r for r in rows
                                            if r["record_type"]
                                            == "CONFIRMED_PRODUCTION_UNIT"]),
            candidate_structures=len([r for r in rows
                                      if r["record_type"] == "CANDIDATE_STRUCTURE"]),
            unresolved_source_records=len([r for r in rows
                                           if r["record_type"] == "UNRESOLVED_SOURCE"]),
            immediately_executable_units=len(imm),
            # Kept apart on purpose. EXTRACTED means rows were cut from a frozen boundary
            # in a local binary; SOURCE_CONTENT_READ means text came back through a
            # connector and nothing has been cut yet. Counting them together made the
            # figure jump from 16 to 23 the moment nine K3 packages became "read", which
            # would have read as seven more units ready to work on when none were.
            extracted_units=len([r for r in rows
                                 if r["extraction_status"] == "EXTRACTED"]),
            source_content_read_units=len([r for r in rows if r["extraction_status"]
                                           == "SOURCE_CONTENT_READ"]),
            model_ready_units=len([r for r in rows if r["model_status"]
                                   in ("MODEL_READY", "PACKAGED")]),
            waiting_authority_units=len([r for r in rows
                                         if r["authority_dependency"] not in
                                         ("NONE", "none — this is a source-access blocker, "
                                          "not an authority one")]),
            ready_to_emit_units=len([r for r in rows if r["ready_to_emit_pptx"]]),
            total_rows=len(rows)),
        immediately_executable_ids=[r["unit_or_candidate_id"] for r in imm],
        blockers_by_owner={o: dict(
            count=len([r for r in rows if r["blocker_owner"] == o]),
            ids=[r["unit_or_candidate_id"] for r in rows if r["blocker_owner"] == o])
            for o in sorted({r["blocker_owner"] for r in rows})},
        derivation="Every row and count is computed from artifacts on disk — the frozen "
                   "boundary map, the extract and model files, the custody manifest and the "
                   "inventory. No percentage is typed.",
        rows=rows)


if __name__ == "__main__":
    q = queue_summary()
    c = q["counts"]
    print("IMMEDIATELY_EXECUTABLE_UNITS =", c["immediately_executable_units"])
    for k, v in c.items():
        print(f"  {k:<32} {v}")
    print("blockers:", {k: v["count"] for k, v in q["blockers_by_owner"].items()})
    k5 = k5_structures()
    print(f"K5 candidates recomputed={k5['recomputed_candidate_count']} "
          f"(previous 22, confirmed={k5['count_confirmed']}) "
          f"clean={k5['clean_candidates']} amber={k5['amber_candidates']}")
    t = t04_page_reconciliation()
    print(f"T04 reconciliation: {t['mismatches']} mismatches, regenerate="
          f"{t['regeneration_decision']['regenerate']}")
