# -*- coding: utf-8 -*-
"""Stage 4.2F-E — K2 custody, source-internal structure conflict, and partial hierarchy.

    python3 docs/source/tools/src_k2_v1.py

WHAT THIS RUN WAS ASKED FOR, AND WHAT IT COULD ACTUALLY DO
----------------------------------------------------------
The brief states that a local K2 binary is available at

    /mnt/data/2. PENGURUSAN PEMBINAAN LANDASAN.pdf

It is not there, and it is nowhere else on this box. Every location searched is listed in
LOCATIONS_SEARCHED with its result, and the locations NOT searched are named too. The
status is therefore NOT_FOUND_IN_LOCATIONS_SEARCHED — scoped, not an unqualified absence.

Because the binary is absent, none of these could be done, and none of them is faked:

    * SHA-256, PDF validity, encryption status, page-count verification  (needs the file)
    * the 346-page decomposition with per-PL page spans                  (needs the file)
    * image and table counts                                            (needs the file)
    * the rendered-PDF page-number oracle                               (needs the file)
    * the table-heavy extraction paths exercised against K2              (needs the file)
    * the first two clean controlled extractions and models             (needs the file)

WHAT WAS DONE INSTEAD, AND ON WHAT EVIDENCE
-------------------------------------------
The Drive identifier was resolved through the connector. Its metadata reports exactly the
byte count the brief expects, which binds the identifier to the intended file — but
metadata is not a binary, and a byte count is not a hash.

The connector also returned document text. That text is TRUNCATED: 62,638 characters for a
346-page document, ending mid-sentence inside teaching plan PT09. It covers the front
matter and the nine teaching plans; it contains ZERO pages of the PL packages themselves
(no `KOD PL PLxx Muka Surat` marker appears anywhere in it). So the state is
SOURCE_CONTENT_PARTIALLY_READ, and the parts not read are named rather than described.

What that truncated text DOES contain, in full and quotable, is every controlling table
for the course structure — which is precisely what K2-SOURCE-CONFLICT-01 needed.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import src_authority_v1 as A   # noqa: E402

STAGE = "4.2F-E"
AUTHORITY = "SRC-AUTH-01"
UNKNOWN = "UNKNOWN_NOT_MEASURED"
NOT_READ = "NOT_READ_BINARY_UNAVAILABLE"

# ==========================================================================================
# 1. BINARY CUSTODY
# ==========================================================================================
EXPECTED_IDENTITY = dict(
    source="the Stage 4.2F-E brief",
    filename="2. PENGURUSAN PEMBINAAN LANDASAN.pdf",
    stated_runtime_path="/mnt/data/2. PENGURUSAN PEMBINAAN LANDASAN.pdf",
    bytes=25043306,
    sha256="0b2d81dda46eaf4fb018a20a78f7f9b2870129c61125768e4438937f3f405680",
    pages=346)

# Read from the Google Drive connector this run. Metadata only — the tool returns file
# facts, not the bytes.
DRIVE_METADATA = dict(
    drive_id="1BW-OibYv3sDyordi0YIQkb5vXeAdOtMn",
    title="2. PENGURUSAN PEMBINAAN LANDASAN.pdf",
    file_size=25043306,
    mime_type="application/pdf",
    file_extension="pdf",
    created_time="2026-06-16T02:38:52.120Z",
    modified_time="2026-04-30T18:15:43Z",
    parent_id="1OHB-x0zOPEOLHYSxtJDyJVG5FmEECUBp",
    evidence_class="CONNECTOR_IDENTIFIED")

DRIVE_TO_EXPECTED_BINDING = dict(
    binding_id="K2-BIND-01",
    drive_id=DRIVE_METADATA["drive_id"],
    filename_matches=DRIVE_METADATA["title"] == EXPECTED_IDENTITY["filename"],
    bytes_match=DRIVE_METADATA["file_size"] == EXPECTED_IDENTITY["bytes"],
    sha256_verified=False,
    sha256_verifiable=False,
    why_not=("A hash requires the bytes. The connector returns metadata and an extracted "
             "text rendering, never the binary, so the SHA-256 in the brief could not be "
             "confirmed or refuted."),
    conclusion=("The Drive identifier resolves to a file whose name and byte count both "
                "equal the brief's expected identity. That is a strong binding and it is "
                "NOT proof of content: two files can share a size. The binding is recorded "
                "at CONNECTOR_IDENTIFIED, one class below "
                "LOCAL_BINARY_HASH_VERIFIED."))

# Exact locations searched this run, each with its result.
LOCATIONS_SEARCHED = [
    dict(location="/mnt/data/2. PENGURUSAN PEMBINAAN LANDASAN.pdf",
         method="direct stat of the path named in the brief", found=False,
         note="The path does not exist. /mnt/data is not a directory on this box."),
    dict(location="/mnt (attach, user-data, skills)", method="recursive listing",
         found=False, note="/mnt/attach is empty; /mnt/user-data holds only 'working'."),
    dict(location="whole filesystem, by exact byte size",
         method="find / -type f -size 25043306c", found=False,
         note="No file of exactly 25,043,306 bytes exists anywhere on the box."),
    dict(location="whole filesystem, by name",
         method="find / -iname '*LANDASAN*'", found=False, note="No match."),
    dict(location="whole filesystem, large PDFs",
         method="find / -iname '*.pdf' -size +20M", found=False,
         note="No PDF over 20 MB exists. The largest PDF present is 9,039,981 bytes and "
              "is the K5 rendered module."),
    dict(location="session upload directory",
         method="listing /root/.claude/uploads/<session>/", found=False,
         note="21 files present, newest 2026-08-03 02:28. Nothing was uploaded for this "
              "run, and no member is the K2 PDF."),
    dict(location="every ZIP archive on the box",
         method="enumerating members of all *.zip over 1 MB", found=False,
         note="No member is named LANDASAN and no member is 25,043,306 bytes. The only "
              "large archive is the PL06 freeze at 25,142,903 bytes — a similar size, a "
              "different file, and its members are the K5 module."),
    dict(location="all runtime mounts",
         method="findmnt over every target", found=False,
         note="Mounts are /proc, /sys, /dev, cgroups, /opt/rclone, /opt/claude-code, "
              "/opt/env-runner and /mnt/skills. None carries user data."),
    dict(location="recently written files",
         method="find / -newermt '-3 hours' -size +1M", found=False,
         note="Only logs, the session transcript, and files this session itself wrote."),
    dict(location="rclone remotes", method="/opt/rclone/rclone listremotes", found=False,
         note="The rclone binary is not present at that path; only a "
              "'rclone-filestore' directory entry exists. No remote could be listed."),
    dict(location="Google Drive, by the known identifier",
         method="connector get_file_metadata + read_file_content", found="METADATA_AND_"
                                                                        "PARTIAL_TEXT",
         note="Metadata resolved and matched the expected name and byte count. Text "
              "returned but truncated. The binary itself is never returned by this tool."),
]

LOCATIONS_NOT_SEARCHED = [
    "any machine other than this container — there is no route to the operator's disk",
    "Google Drive folders other than the parent of the known identifier",
    "any CIDB internal system, SharePoint or shared drive",
    "email attachments or chat transcripts outside this session",
]

CUSTODY = dict(
    record_id="K2-CUSTODY-02",
    supersedes="K2-CUSTODY-01 (Stage 4.2F-C/D scoped blocker report)",
    supersession_note=("The earlier blocker report is PRESERVED_UNCHANGED as historical "
                       "evidence. It was correct when written and it is still correct: "
                       "the binary was not retrievable then and is not retrievable now. "
                       "This record adds the Drive binding and the partial text read."),
    status="NOT_FOUND_IN_LOCATIONS_SEARCHED",
    binary_local=False,
    binary_readable=False,
    content_read="PARTIAL",
    evidence_class="CONNECTOR_TEXT_READABLE_PARTIAL",
    states_claimed=["SOURCE_LOCATED_BY_CONNECTOR", "SOURCE_CONTENT_PARTIALLY_READ"],
    states_not_claimed=["SOURCE_BINARY_LOCAL", "SOURCE_BINARY_READABLE",
                        "SOURCE_CONTENT_READ", "BOUNDARY_CONFIRMED", "EXTRACTED"],
    states_not_claimed_why=("The brief asked for the live status to move to "
                            "SOURCE_BINARY_LOCAL / SOURCE_BINARY_READABLE / "
                            "SOURCE_CONTENT_READ. Two of those three are false and the "
                            "third is only partly true, so none is claimed. Moving the "
                            "status because a run expected it to move is the exact "
                            "failure this register exists to prevent."),
    unverifiable=dict(
        sha256=NOT_READ, pdf_validity=NOT_READ, encryption_status=NOT_READ,
        page_count_verified=NOT_READ, image_readability=NOT_READ,
        table_readability=NOT_READ, pdf_metadata=NOT_READ,
        note="Each of these requires the bytes. The brief's stated values are recorded as "
             "EXPECTED, never as OBSERVED."))

# ==========================================================================================
# 2. WHAT THE CONNECTOR TEXT ACTUALLY COVERS
# ==========================================================================================
CONNECTOR_READ = dict(
    read_id="K2-READ-01",
    chars=62638,
    document_pages_declared_by_brief=346,
    chars_per_page_if_complete=round(62638 / 346, 1),
    complete=False,
    truncation_evidence=[
        "The text ends mid-document inside teaching plan PT09, at the marker "
        "'NO. KOD PT PT09 Muka Surat: 2/6' — PT09 declares six pages and only two appear.",
        "62,638 characters over 346 pages is about 181 characters a page. The K3 packages, "
        "read through the same connector, ran 1,500 to 2,000 characters a page.",
        "Not one 'KOD PL PLxx Muka Surat' marker appears. The PL packages are the bulk of "
        "the document and none of their pages came back.",
    ],
    covers=["front matter", "KANDUNGAN MODUL DAN PAKEJ LATIHAN summary table",
            "section 1.5 Silibus Modul Latihan and its table",
            "section 1.6 Tempoh Latihan and its hour tables",
            "teaching plans PT01 to PT08 in full",
            "teaching plan PT09, first two of six pages"],
    does_not_cover=["every PL package body (PL01 to PL09)",
                    "all LATIHAN sections", "all SKEMA JAWAPAN sections",
                    "appendices and supporting material",
                    "any image or table beyond those in the front matter"],
    consequence=("Course-level structure is fully evidenced. Unit-level decomposition is "
                 "not evidenced at all, and is not attempted."))

# ==========================================================================================
# 3. K2-SOURCE-CONFLICT-01 — the module count
# ==========================================================================================
# Five independent places in the source enumerate the structure. Four agree. One does not.
CONFLICT = dict(
    conflict_id="K2-SOURCE-CONFLICT-01",
    subject="how many training modules the K2 course contains",
    evidence=[
        dict(source="narrative prose, section 1.5 Silibus Modul Latihan",
             exact_value="Panduan ini mengandungi lapan (8) modul latihan yang "
                         "dibangunkan oleh panel-panel Jawatankuasa Pembangunan Modul "
                         "dilantik hasil.",
             asserts_module_count=8, kind="PROSE"),
        dict(source="the silibus table, printed immediately below that sentence",
             exact_value="01. Business Operation Management M01-LP01 M01-LP02 M01-LP03 "
                         "M01-LP04 | 02. Tendering Management M01-LP05 | 03. Contract "
                         "Implementation & Management M01-LP06 | 04. Project Planning & "
                         "Scheduling M01-LP07 | 05. Construction Operation Management "
                         "M01-LP08 | 06. Project Handover M01-LP09",
             asserts_module_count=6, asserts_package_count=9, kind="TABLE"),
        dict(source="KANDUNGAN MODUL DAN PAKEJ LATIHAN, front matter",
             exact_value="module rows numbered 1 to 6; package codes PL01 to PL09",
             asserts_module_count=6, asserts_package_count=9, kind="TABLE"),
        dict(source="section 1.6 Tempoh Latihan, module-hours table",
             exact_value="LP01 LP02 LP03 LP04 LP05 LP06 LP07 LP08 LP09",
             asserts_package_count=9, kind="TABLE"),
        dict(source="the nine teaching plans, each carrying its own module header",
             exact_value="PT01-PT04 -> M01; PT05 -> M02; PT06 -> M03; PT07 -> M04; "
                         "PT08 -> M05; PT09 -> M06",
             asserts_module_count=6, asserts_package_count=9, kind="REPEATED_SECTION"),
    ],
    finding=("Four independent enumerations — two front-matter tables, an hours table and "
             "nine separately-headed teaching plans — agree on six modules and nine "
             "packages. One prose sentence says eight. The eight matches nothing in the "
             "document: not the six named modules, not the nine LP codes, not the nine PL "
             "codes, not the nine teaching plans. It is contradicted by the table printed "
             "directly beneath it."),
    narrative_module_count=8,
    syllabus_table_module_count=6,
    module_codes_present=["M01", "M02", "M03", "M04", "M05", "M06"],
    pl_codes_present=[f"PL0{i}" for i in range(1, 10)],
    pt_codes_present=[f"PT0{i}" for i in range(1, 10)],
    lp_codes_present=[f"M01-LP0{i}" for i in range(1, 10)],
    classification="TYPOGRAPHICAL",
    classification_reasoning=(
        "Not METADATA_ONLY: the sentence is body prose a learner could read. "
        "Not SOURCE_AUTHORITY_CONFLICT: the sources are not of equal weight — one "
        "unsupported prose count against four enumerations, one of which is on the same "
        "page. "
        "Not INSTRUCTIONAL_STRUCTURE_DECISION_REQUIRED: nobody has to choose a structure. "
        "Six modules and nine packages are consistently supported, so there is nothing to "
        "decide — only something to correct."),
    requires_instructional_decision=False,
    routed_to="FIRDAUS",
    route_type="SOURCE_CONTENT_CORRECTION",
    in_bariah_register=False,
    silently_corrected=False,
    correction_note=("The source is not altered. The provisional structure used for "
                     "decomposition is six modules and nine packages, as the brief "
                     "permits when that structure is consistently supported, and this "
                     "record travels with it."),
    secondary_defect=dict(
        defect_id="K2-SOURCE-OBS-01",
        subject="the KOD column of the silibus table",
        exact_value="M01-LP01 through M01-LP09",
        finding=("All nine package codes are prefixed M01-, including those belonging to "
                 "modules 02 through 06. The teaching plans independently assign PT05 to "
                 "M02, PT06 to M03, PT07 to M04, PT08 to M05 and PT09 to M06, so the "
                 "prefix is wrong for five of the nine rows."),
        classification="TYPOGRAPHICAL", routed_to="FIRDAUS",
        production_impact=("A parser keyed on the KOD column would file every package "
                           "under M01 — the same defect the K3 queue carried until "
                           "Stage 4.2F-D corrected it. K2 unit IDs must be built from the "
                           "teaching-plan headers, not from this column.")))

# ==========================================================================================
# 4. PROVISIONAL HIERARCHY — course -> module -> PL, as far as the evidence reaches
# ==========================================================================================
COURSE = dict(course="K2", title="PENGURUSAN PEMBINAAN LANDASAN",
              programme="MODUL PENGURUSAN KONTRAKTOR", field_code="CE07",
              job_code="CE07")

# Module titles are taken from each teaching plan's own header, which is the strongest
# available source: nine separate sections that agree with each other.
MODULES = [
    dict(code="M01", title_ms="PENGURUSAN OPERASI PERNIAGAAN",
         title_en="Business Operation Management", teaching_plans=["PT01", "PT02", "PT03",
                                                                   "PT04"]),
    dict(code="M02", title_ms="PENGURUSAN TENDER", title_en="Tendering Management",
         teaching_plans=["PT05"]),
    dict(code="M03", title_ms="PENGURUSAN DAN PELAKSANAAN KONTRAK",
         title_en="Contract Implementation & Management", teaching_plans=["PT06"]),
    dict(code="M04", title_ms="PERANCANGAN DAN PENJADUALAN PROJEK",
         title_en="Project Planning & Scheduling", teaching_plans=["PT07"]),
    dict(code="M05", title_ms="PENGURUSAN OPERASI PEMBINAAN",
         title_en="Construction Operation Management", teaching_plans=["PT08"]),
    dict(code="M06", title_ms="PENYERAHAN PROJEK", title_en="Project Handover",
         teaching_plans=["PT09"]),
]

# One row per teaching plan. `pages` is the plan's OWN declared length from its footer
# (Muka Surat: n/N) — that is a real measurement of the teaching plan, and it is NOT the
# length of the corresponding PL package, which was not read.
TEACHING_PLANS = [
    dict(pt="PT01", module="M01", pages=8,
         tajuk="PENGENALAN MODUL PEMBINAAN LANDASAN (TRACKWORKS)"),
    dict(pt="PT02", module="M01", pages=6,
         tajuk="PENGURUSAN OPERASI PERNIAGAAN DALAM PEMBINAAN LANDASAN"),
    dict(pt="PT03", module="M01", pages=7,
         tajuk="REGULASI DAN PEMATUHAN INDUSTRI REL DALAM PEMBINAAN"),
    dict(pt="PT04", module="M01", pages=7,
         tajuk="INOVASI DAN TEKNOLOGI DIGITAL SERTA AUTOMASI DALAM"),
    dict(pt="PT05", module="M02", pages=7,
         tajuk="PENGURUSAN TENDER DALAM PEMBINAAN LANDASAN"),
    dict(pt="PT06", module="M03", pages=7,
         tajuk="PELAKSANAAN DAN PENGURUSAN KONTRAK PEMBINAAN LANDASAN"),
    dict(pt="PT07", module="M04", pages=6,
         tajuk="PERANCANGAN DAN PENJADUALAN PEMBINAAN LANDASAN"),
    dict(pt="PT08", module="M05", pages=8,
         tajuk="PENGURUSAN OPERASI PEMBINAAN LANDASAN"),
    dict(pt="PT09", module="M06", pages=6,
         tajuk="PENYERAHAN PROJEK PEMBINAAN LANDASAN",
         note="Only pages 1 and 2 of 6 were returned; the declared total is read from the "
              "footer of the pages that did arrive."),
]

# The nine PL packages. Every field that needs the binary is UNKNOWN_NOT_MEASURED, not 0
# and not guessed.
PL_PACKAGES = [
    dict(pl="PL01", module="M01", pt="PT01"),
    dict(pl="PL02", module="M01", pt="PT02"),
    dict(pl="PL03", module="M01", pt="PT03"),
    dict(pl="PL04", module="M01", pt="PT04"),
    dict(pl="PL05", module="M02", pt="PT05"),
    dict(pl="PL06", module="M03", pt="PT06"),
    dict(pl="PL07", module="M04", pt="PT07"),
    dict(pl="PL08", module="M05", pt="PT08"),
    dict(pl="PL09", module="M06", pt="PT09"),
]

# The PL-to-module map above is derived from the teaching plans, which are numbered in the
# same order as the packages and each carry a module header. Where a teaching plan names
# its package explicitly, that naming is recorded here as direct corroboration.
PL_DIRECTLY_NAMED_BY_ITS_PLAN = {
    "PL06": "PL06: Pelaksanaan dan Pengurusan Kontrak",
    "PL07": "PL07: Perancangan dan Penjadualan Pembinaan",
    "PL09": "PL09: Penyerahan Projek Pembinaan Landasan",
}

PL_MAP_CONFIDENCE = dict(
    directly_named=sorted(PL_DIRECTLY_NAMED_BY_ITS_PLAN),
    inferred_by_ordinal_position=["PL01", "PL02", "PL03", "PL04", "PL05", "PL08"],
    basis=("Three teaching plans name their package outright. The other six are mapped by "
           "ordinal position — PT0n to PL0n — which the three named cases confirm holds. "
           "That is an inference, it is labelled as one, and it is exactly the kind of "
           "thing the missing binary would settle in one pass."))


def hierarchy():
    """course -> module -> PL, with every unmeasurable field left unmeasured."""
    rows = []
    for p in PL_PACKAGES:
        pt = next(t for t in TEACHING_PLANS if t["pt"] == p["pt"])
        mod = next(m for m in MODULES if m["code"] == p["module"])
        rows.append(dict(
            course="K2", pl=p["pl"], module_code=mod["code"],
            module_title=mod["title_ms"], teaching_plan=p["pt"],
            teaching_plan_pages=pt["pages"], teaching_plan_tajuk=pt["tajuk"],
            official_title=PL_DIRECTLY_NAMED_BY_ITS_PLAN.get(p["pl"], UNKNOWN),
            title_source=("TEACHING_PLAN_HEADER"
                          if p["pl"] in PL_DIRECTLY_NAMED_BY_ITS_PLAN
                          else "NOT_READ_BINARY_UNAVAILABLE"),
            pdf_start_page=UNKNOWN, pdf_end_page=UNKNOWN,
            controlling_heading=UNKNOWN, page_footer_anchor=UNKNOWN,
            topic_hierarchy=UNKNOWN, assessment_location=UNKNOWN,
            answer_scheme_location=UNKNOWN, image_count=UNKNOWN, table_count=UNKNOWN,
            shared_page_boundary_risk=UNKNOWN, source_completeness="NOT_ASSESSED",
            record_type="CANDIDATE_STRUCTURE",
            record_type_why=("A PL code with a module and a teaching plan is a structure, "
                             "not a unit. Nothing about its page span, granularity or "
                             "internal boundaries is known, so it cannot be confirmed."),
            authority_inherited=AUTHORITY))
    return dict(
        course=COURSE, modules=len(MODULES), pl_packages=len(rows),
        teaching_plans=len(TEACHING_PLANS),
        teaching_plan_pages_total=sum(t["pages"] for t in TEACHING_PLANS),
        module_map={m["code"]: [r["pl"] for r in rows if r["module_code"] == m["code"]]
                    for m in MODULES},
        pl_map_confidence=PL_MAP_CONFIDENCE,
        confirmed_units=0,
        candidate_structures=len(rows),
        unmapped_source_regions=1,
        unmapped_note=("The entire PL package body of the document — the bulk of its 346 "
                       "pages — is one unmapped region. Its exact page span is "
                       "UNKNOWN_NOT_MEASURED because the binary was not available to "
                       "measure it."),
        decomposition_completed=False,
        decomposition_blocked_by="K2 binary not present in any searched location",
        rows=rows)


def custody():
    return dict(record=CUSTODY, expected=EXPECTED_IDENTITY, drive=DRIVE_METADATA,
                binding=DRIVE_TO_EXPECTED_BINDING, connector_read=CONNECTOR_READ,
                locations_searched=LOCATIONS_SEARCHED,
                locations_not_searched=LOCATIONS_NOT_SEARCHED,
                authority_inherited=AUTHORITY, stage=STAGE)


def queue_rows():
    """K2's rows for the live queue: nine candidate structures, no unresolved-source row.

    The old single K2-MONOLITH-UNRESOLVED row is retired. It said one true thing — the
    binary is missing — and hid nine structures that are now evidenced. The binary is
    still missing, and that fact now travels on every row as its exact blocker instead of
    standing in for the whole course.
    """
    h = hierarchy()
    out = []
    for r in h["rows"]:
        out.append(dict(
            course="K2", pl=r["pl"],
            unit_or_candidate_id=f"K2-{r['module_code']}-{r['pl']}",
            record_type="CANDIDATE_STRUCTURE",
            source_located=True, binary_local=False, binary_readable=False,
            content_read=False, boundary_confirmed=False,
            extraction_status="SOURCE_LOCATED_BY_CONNECTOR",
            model_status="NOT_STARTED",
            authority_dependency="none — this is a source-access blocker, not an "
                                 "authority one",
            immediately_executable=False, ready_to_emit_pptx=False,
            blocker_owner="FIRDAUS",
            exact_blocker=(f"K2 binary not present in any searched location; Drive "
                           f"{DRIVE_METADATA['drive_id']}, "
                           f"{DRIVE_METADATA['file_size']:,} bytes, connector returns "
                           f"metadata and truncated text only"),
            next_executable_action="place the 25,043,306-byte PDF on local disk, then "
                                   "decompose its 346 pages"))
    return out


if __name__ == "__main__":
    c = custody()
    h = hierarchy()
    print(f"K2 custody: {c['record']['status']}")
    print(f"  binary_local={c['record']['binary_local']} "
          f"binary_readable={c['record']['binary_readable']} "
          f"content_read={c['record']['content_read']}")
    print(f"  drive binding: name={c['binding']['filename_matches']} "
          f"bytes={c['binding']['bytes_match']} "
          f"sha256_verified={c['binding']['sha256_verified']}")
    print(f"  locations searched: {len(c['locations_searched'])}, "
          f"not searched: {len(c['locations_not_searched'])}")
    print(f"  connector text: {c['connector_read']['chars']:,} chars, "
          f"complete={c['connector_read']['complete']}")
    print(f"\n{CONFLICT['conflict_id']}: {CONFLICT['classification']} — "
          f"narrative says {CONFLICT['narrative_module_count']}, tables say "
          f"{CONFLICT['syllabus_table_module_count']}; "
          f"instructional decision required: "
          f"{CONFLICT['requires_instructional_decision']}, routed to "
          f"{CONFLICT['routed_to']}")
    print(f"\nhierarchy: {h['modules']} modules, {h['pl_packages']} PL, "
          f"{h['teaching_plans']} teaching plans "
          f"({h['teaching_plan_pages_total']} plan pages)")
    print("  module map:", h["module_map"])
    print(f"  confirmed units={h['confirmed_units']}, "
          f"candidates={h['candidate_structures']}, "
          f"unmapped regions={h['unmapped_source_regions']}")
    print(f"  queue rows: {len(queue_rows())}")
