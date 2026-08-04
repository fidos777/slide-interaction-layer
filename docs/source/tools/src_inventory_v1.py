# -*- coding: utf-8 -*-
"""Stage 4.2F-C Lanes 4-6 — K3 inventory, K2 decomposition, remaining-K5 inventory.

    python3 docs/source/tools/src_inventory_v1.py

Three lanes, three very different evidence positions, and the difference is the point:

    K5   the binary is on local disk and hash-verified, so every number here is measured.
    K3   the connector opens the PDFs and returns their text. Two of nine were read in
         full; the other seven are identified and not read, and say so.
    K2   the connector identifies the monolith but a 25 MB PDF cannot be brought into this
         environment through a text channel. Decomposition is NOT_PERFORMED and the exact
         missing capability is named.

Nothing is inferred from a template. PL02 is not given PL01's page count because the two
files look alike.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
DOCS = os.path.dirname(SRC_DIR)
sys.path.insert(0, HERE)
import src_authority_v1 as A   # noqa: E402

STAGE = "4.2F-C"
AUTHORITY = "SRC-AUTH-01"

NOT_READ = "IDENTIFIED_NOT_READ"
NOT_PERFORMED = "NOT_PERFORMED_LOCAL_BINARY_UNAVAILABLE"
UNKNOWN = "UNKNOWN_NOT_MEASURED"

CANDIDATE_CLASSES = ["SOURCE_READY_CLEAN", "SOURCE_READY_BOUNDARY_AMBER",
                     "SOURCE_INCOMPLETE", "SOURCE_CONFLICT"]

# ==========================================================================================
# LANE 4 — K3, nine PL packages
#
# The template these files share is real and visible in the two that were read: a header
# block, a "KOD PL PLxx Page: n/N" footer on every page, OBJEKTIF, PENERANGAN, numbered
# sections with x.y sub-sections and a) b) c) descendants, RUJUKAN, LATIHAN, and
# SKEMA JAWAPAN (UNTUK PENGAJAR). It is NOT used to fill in the seven that were not read.
# ==========================================================================================
K3_TEMPLATE_SPINE = ["PAKEJ LATIHAN header with KOD BIDANG and KOD MODUL",
                     "TAJUK", "OBJEKTIF", "PENERANGAN",
                     "numbered sections 1) 2) 3) with x.y sub-sections and a) b) c) items",
                     "RUJUKAN", "LATIHAN", "SKEMA JAWAPAN (UNTUK PENGAJAR)",
                     "per-page footer: KOD PL PLxx Page|Muka Surat: n/N"]

K3_READ = {
    "PL01": dict(
        pages=17, page_marker_style="Page: n/17", page_anchors_contiguous=True,
        tajuk="PENGENALAN PENGURUSAN KERJA PENSTABILAN TANAH",
        top_sections=["ASAS KONSEP PENYIASATAN DAN PENSTABILAN TANAH",
                      "KEPENTINGAN PENYIASATAN TANAH",
                      "KEPENTINGAN PENSTABILAN TANAH",
                      "KAEDAH PENYIASATAN TANAH",
                      "KAEDAH PENSTABILAN TANAH",
                      "FAKTOR PEMILIHAN KAEDAH PENYIASATAN TANAH",
                      "FAKTOR PEMILIHAN KAEDAH PENSTABILAN TANAH"],
        sub_section_count=17, lettered_descendants=False,
        tables=2, table_titles=["Jadual 1: Kepentingan Penyiasatan Tanah",
                                "Jadual 2: Kepentingan Penstabilan Tanah"],
        figures=7, figure_titles=["Rajah 1: Surface Reconnaissance",
                                  "Rajah 2: Dynamic Cone Penetrometer",
                                  "Rajah 3: Boring",
                                  "Rajah 4: Standard Penetration Test – SPT",
                                  "Rajah 5: Soil Laboratory Testing",
                                  "Rajah 6: Pemilihan Kaedah Penyiasatan Tanah",
                                  "Rajah 7: Faktor-Faktor Pemilihan Kaedah Penstabilan Tanah"],
        latihan=True, latihan_questions=3, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=3,
        classification="SOURCE_READY_CLEAN",
        candidate_units=1,
        boundary="Self-contained file. Starts at its own header and ends at SKEMA JAWAPAN. "
                 "No page is shared with another PL.",
        complexity="MEDIUM — seven top sections, two comparison tables and seven figures, "
                   "no branching or scenario structure.",
        header_anomaly=("The header block lists PL01 and PL02 with the SAME title, "
                        "'Pengenalan Pengurusan Kerja Penstabilan Tanah'. PL03's header "
                        "gives PL02 a different title, 'Pengurusan Pematuhan Kerja "
                        "penstabilan Tanah'. The two headers disagree about PL02.")),
    "PL03": dict(
        pages=9, page_marker_style="Muka Surat: n/9", page_anchors_contiguous=True,
        tajuk="INOVASI TEKNOLOGI DIGITAL DAN AUTOMASI DALAM PENSTABILAN TANAH",
        top_sections=["PENGENALAN KEPADA DIGITAL DAN INOVASI",
                      "TEKNOLOGI DIGITAL DALAM PENSTABILAN TANAH",
                      "CABARAN DAN STRATEGI PELAKSANAAN INOVASI DALAM PENSTABILAN TANAH"],
        sub_section_count=3, lettered_descendants=True,
        lettered_descendant_note="2.1 Peralatan, 2.2 Bahan and 2.3 Mesin each carry four "
                                 "a) to d) items — twelve lettered descendants in all.",
        tables=1, table_titles=["Jadual 1: Cabaran dan Strategi Pelaksanaan Inovasi dalam "
                                "Penstabilan Tanah"],
        figures=0, figure_titles=[],
        latihan=True, latihan_questions=3, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=3,
        classification="SOURCE_READY_CLEAN",
        candidate_units=1,
        boundary="Self-contained file, nine pages, no shared page.",
        complexity="LOW-MEDIUM — three top sections, one of which fans into three "
                   "categories of four items each. A clean click-to-reveal shape.",
        header_anomaly=("Its own header block numbers a table 'Jadual 2' in the body text "
                        "while the table's caption reads 'Jadual 1'. Recorded, not "
                        "corrected.")),
}

K3_NOT_READ = ["PL02", "PL04", "PL05", "PL06", "PL07", "PL08", "PL09"]

K3_READ_BUDGET_NOTE = (
    "Two of the nine PDFs were read in full through the connector. The other seven were "
    "identified — Drive id, filename and exact byte size — and not read, because each full "
    "text read costs a large fixed amount of this run's working context and reading all nine "
    "would have left the remaining lanes undone. They are recorded as IDENTIFIED_NOT_READ "
    "rather than being described from the template the two read files share. A file that "
    "looks like another file is not evidence about its page count.")


def k3_inventory():
    rows = []
    for p in A.K3_PDFS:
        pl = p["pl"]
        r = dict(course="K3", pl=pl, filename=p["filename"], drive_id=p["drive_id"],
                 bytes=p["bytes"], bytes_source="DRIVE_METADATA",
                 sha256=A.NOT_COMPUTED, authority_inherited=AUTHORITY)
        if pl in K3_READ:
            k = K3_READ[pl]
            r.update(read_status="CONNECTOR_TEXT_READ_IN_FULL", **k)
        else:
            r.update(read_status=NOT_READ, pages=UNKNOWN,
                     page_anchors_contiguous=UNKNOWN, top_sections=UNKNOWN,
                     sub_section_count=UNKNOWN, lettered_descendants=UNKNOWN,
                     tables=UNKNOWN, figures=UNKNOWN, latihan=UNKNOWN,
                     skema_jawapan=UNKNOWN, candidate_units=UNKNOWN,
                     classification="SOURCE_READY_PENDING_INVENTORY",
                     boundary=UNKNOWN, complexity=UNKNOWN,
                     note=K3_READ_BUDGET_NOTE)
        rows.append(r)
    read = [r for r in rows if r["read_status"] == "CONNECTOR_TEXT_READ_IN_FULL"]
    return dict(
        course="K3", course_title=A.K3_COURSE_TITLE, field_code=A.K3_FIELD_CODE,
        module_code=A.K3_MODULE_CODE, folder_id=A.K3_FOLDER_ID,
        pdfs=len(rows), read_in_full=len(read), identified_not_read=len(rows) - len(read),
        template_spine=K3_TEMPLATE_SPINE,
        template_note=("The spine is observed in both files that were read. It is not "
                       "projected onto the seven that were not."),
        one_pdf_equals_one_unit=dict(
            assumption_made=False,
            finding=("Both files that were read are self-contained: own header, own page "
                     "numbering starting at 1, own LATIHAN and own SKEMA JAWAPAN. On that "
                     "evidence each is one candidate unit. Whether a nine-page PL and a "
                     "seventeen-page PL should both become single storyboard units is an "
                     "instructional question, not a source one, and it is not answered "
                     "here.")),
        candidate_units_evidenced=sum(r["candidate_units"] for r in read),
        rows=rows,
        header_conflict=dict(
            id="K3-SRC-CONFLICT-01",
            finding=("PL01's header block and PL03's header block disagree about PL02's "
                     "title. PL01 says 'PL02 Pengenalan Pengurusan Kerja Penstabilan Tanah', "
                     "repeating PL01's own title; PL03 says 'PL02 Pengurusan Pematuhan Kerja "
                     "penstabilan Tanah'."),
            classification="SOURCE_CONFLICT",
            affects=["PL02"], owner="FIRDAUS_OR_SOURCE_GOVERNANCE",
            note="Recorded, not resolved. PL02 was not read, so which header is right is not "
                 "determined here."))


# ==========================================================================================
# LANE 5 — K2 monolith
# ==========================================================================================
def k2_decomposition():
    m = A.K2_MONOLITH
    return dict(
        course="K2", course_title=A.K2_COURSE_TITLE, folder_id=A.K2_FOLDER_ID,
        file=dict(filename=m["filename"], drive_id=m["drive_id"], bytes=m["bytes"],
                  bytes_source="DRIVE_METADATA", sha256=A.NOT_COMPUTED,
                  format="PDF", format_basis="DRIVE_MIME_TYPE"),
        outcome=NOT_PERFORMED,
        page_count=UNKNOWN, heading_tree=UNKNOWN, module_pl_hierarchy=UNKNOWN,
        descendant_map=UNKNOWN, latihan_locations=UNKNOWN,
        skema_jawapan_locations=UNKNOWN, image_inventory=UNKNOWN,
        table_inventory=UNKNOWN, candidate_unit_boundaries=UNKNOWN,
        shared_page_risks=UNKNOWN, candidate_clean_units=UNKNOWN,
        estimated_total_units=UNKNOWN,
        first_clean_candidate_unit=None,
        first_clean_candidate_model=NOT_PERFORMED,
        missing_capability=dict(
            what_is_missing="the monolith as a local file, or a page-bounded connector read",
            exact_identifier=f"Drive file {m['drive_id']} — {m['filename']}",
            folder=f"Drive folder {A.K2_FOLDER_ID} — 2_Kursus Pengurusan Pembinaan Landasan",
            why=("The connector returns whole-file text and warns it may be incomplete for "
                 "very large files. At 25,043,306 bytes this is by far the largest source in "
                 "the project — roughly 28 times the largest K3 PDF that was read. Pulling "
                 "it through a text channel would consume the remainder of this run's "
                 "working context and would still not give a page count, an image inventory "
                 "or a table inventory, because those need the binary."),
            what_would_unblock_it=[
                "the PDF placed on local disk in this environment, where PyMuPDF is already "
                "available and gives page count, heading tree, images and tables directly",
                "or a connector that can return a named page range rather than the whole "
                "file"]),
        uncertainty_register=[
            dict(item="Page count", status=UNKNOWN,
                 note="Not estimated from byte size. A 25 MB PDF may be 100 image-heavy "
                      "pages or 900 text pages, and guessing would put a number into the "
                      "production queue that nobody measured."),
            dict(item="Whether the monolith contains PL packages at all",
                 status="LIKELY_BUT_UNVERIFIED",
                 note="The K3 folder holds nine PL PDFs and the K5 folder holds one module "
                      "DOCX covering eight PLs, so both shapes exist in this project. Which "
                      "shape K2 has was not verified."),
            dict(item="Candidate unit count", status=UNKNOWN,
                 note="Cannot be derived without the heading tree."),
        ],
        authority_inherited=AUTHORITY,
        note=("Recorded as not performed, with the exact identifier named, rather than "
              "filled in from the shape of the other two courses. Every other lane in this "
              "run continued."))


# ==========================================================================================
# LANE 6 — remaining K5, measured from the verified binary
#
# The module's own syllabus table (module page xvii-xviii) names EIGHT Pakej Latihan, not
# seven. Every heading below was located in the DOCX body and its printed page read off the
# typeset PDF footer, so these are measurements, not estimates.
# ==========================================================================================
K5_SYLLABUS = [
    dict(pl="PL01", title="Pengenalan Dan Latar Belakang Industri Landskap Luar",
         module_pages=(1, 32),
         sub_modul=[dict(text="PENGENALAN DAN LATAR BELAKANG INDUSTRI LANDSKAP LUAR",
                         paragraph=152, page=1),
                    dict(text="KONSEP SENI BINA LANDSKAP", paragraph=264, page=9),
                    dict(text="KATEGORI LANDSKAP LUAR", paragraph=359, page=16),
                    dict(text="SKOP KERJA UTAMA LANDSKAP LUAR BANGUNAN",
                         paragraph=505, page=27)]),
    dict(pl="PL02", title="Pengurusan Operasi Perniagaan", module_pages=(33, 76),
         sub_modul=[dict(text="PASUKAN PELAKSANA PROJEK PEMBINAAN LANDSKAP LUAR",
                         paragraph=582, page=33),
                    dict(text="PASUKAN PERUNDING TEKNIKAL DAN PAKAR",
                         paragraph=979, page=49),
                    dict(text="ORGANISASI PROJEK LANDSKAP LUAR", paragraph=1327, page=64)]),
    dict(pl="PL03", title="Pengurusan Tender", module_pages=(77, 131),
         sub_modul=[dict(text="TENDER", paragraph=1569, page=77),
                    dict(text="SEBUT HARGA", paragraph=1597, page=80),
                    dict(text="LUKISAN TENDER", paragraph=1600, page=80),
                    dict(text="KOMPONEN SENARAI KUANTITI LANDSKAP / BILLS OF QUANTITIES",
                         paragraph=1673, page=84),
                    dict(text="SPESIFIKASI", paragraph=1790, page=89),
                    dict(text="PENYEDIAAN DATA KOS, ANGGARAN DAN TENDER LANDSKAP",
                         paragraph=1902, page=94),
                    dict(text="PENYEDIAAN DOKUMENTASI TENDER", paragraph=2491, page=120),
                    dict(text="STRUKTUR PELAPORAN TEKNIKAL DAN DOKUMENTASI PROJEK",
                         paragraph=2598, page=124)]),
    dict(pl="PL04", title="Pelaksanaan Dan Pengurusan Kontrak", module_pages=(132, 155),
         sub_modul=[dict(text="PENGURUSAN KEPERLUAN DAN DOKUMENTASI KONTRAK",
                         paragraph=2744, page=132),
                    dict(text="PENGURUSAN PENENTUAN ATAU PENAMATAN KONTRAK",
                         paragraph=3123, page=151)]),
    dict(pl="PL05", title="Perancangan Dan Penjadualan Projek", module_pages=(156, 161),
         sub_modul=[dict(text="PENYEDIAAN WORK BREAKDOWN STRUCTRUE (WBS) UNTUK LANDSKAP "
                              "KEJUR DAN LEMBUT", paragraph=3238, page=156),
                    dict(text="PENYEDIAAN PROGRAM KERJA (WORK PROGRAM) DAN PENJADUALAN "
                              "PEMBINAAN LANDSKAP", paragraph=3310, page=159)]),
    dict(pl="PL06", title="Pengurusan Operasi Pembinaan Landskap", module_pages=(162, 309),
         sub_modul=[dict(text="PROSES MEMULA KERJA", paragraph=3375, page=162),
                    dict(text="ELEMEN PEMBINAAN LANDSKAP", paragraph=4085, page=201),
                    dict(text="KOMPONEN LANDSKAP", paragraph=4463, page=226),
                    dict(text="PENJAAGAAN DAN PENYELENGGARAAN", paragraph=5220, page=276),
                    dict(text="PENGURUSAN KUALITI PROJEK", paragraph=5360, page=284),
                    dict(text="PERLINDUNGAN DAN PENAMBAHBAIKAN ALAM SEKITAR",
                         paragraph=5543, page=294),
                    dict(text="DEMOBILISASI", paragraph=5705, page=303)]),
    dict(pl="PL07", title="Penyerahan Projek", module_pages=(310, 315),
         sub_modul=[dict(text="PENYEDIAAN DOKUMEN SERAHAN", paragraph=5813, page=310),
                    dict(text="MENGURUS LIABILITI KECACATAN DAN CMGD",
                         paragraph=5866, page=312)]),
    dict(pl="PL08", title="Inovasi & Teknologi Landskap", module_pages=(316, 332),
         sub_modul=[dict(text="APLIKASI TEKNOLOGI DAN INOVASI DALAM PEMBINAAN",
                         paragraph=5949, page=316)]),
]

LANE_6_SCOPE = ["PL01", "PL02", "PL03", "PL04", "PL05", "PL07"]

K5_FINDINGS = [
    dict(id="K5-INV-01", severity="SCOPE",
         finding=("The module contains EIGHT Pakej Latihan. Its own syllabus table on module "
                  "pages xvii-xviii lists PL01 to PL08, and every one of them has body "
                  "headings in the DOCX. This lane was scoped to PL01-PL05 and PL07; PL08 "
                  "'Inovasi & Teknologi Landskap' exists, occupies module pages 316 onward, "
                  "and is inventoried here rather than left unmentioned.")),
    dict(id="K5-INV-02", severity="SOURCE_ANOMALY",
         finding=("The syllabus table gives PL07 three sub-modul, the third being "
                  "'Organisasi Landskap Projek Luar' — which is PL02's third sub-modul, "
                  "repeated. The body has only two headings between module pages 310 and "
                  "315. Recorded, not corrected; the body-anchor precedence rule already "
                  "governs extraction.")),
    dict(id="K5-INV-03", severity="BOUNDARY_RISK",
         finding=("PL03 carries two top-level headings on the same printed page: SEBUT HARGA "
                  "and LUKISAN TENDER both begin on module page 80. Any unit split between "
                  "them is a shared-page boundary and must be split by heading anchor, "
                  "exactly as T03-B03 and T03-B04 were.")),
    dict(id="K5-INV-04", severity="SCALE",
         finding=("PL05 is six module pages with two sub-modul, and PL07 is six pages with "
                  "two. PL03 is fifty-five pages with eight. Unit counts cannot be spread "
                  "evenly across PLs, and the previous planning estimate of roughly 33 units "
                  "is not carried forward as a production fact.")),
]

PRIOR_ESTIMATE_NOT_CARRIED = dict(
    prior_estimate="approximately 33 units",
    status="NOT_CARRIED_FORWARD_AS_A_PRODUCTION_FACT",
    reason=("It was a planning estimate. This lane publishes what is evidenced instead: "
            "confirmed units, candidate units, and source regions nobody has mapped."))


def k5_remaining_inventory():
    out = []
    for pl in K5_SYLLABUS:
        in_scope = pl["pl"] in LANE_6_SCOPE
        is_pl06 = pl["pl"] == "PL06"
        lo, hi = pl["module_pages"]
        pages = hi - lo + 1
        # PL06 is the only PL with a frozen 14-unit boundary map. Its units are CONFIRMED
        # because a frozen artifact names each one; every other PL has sub-modul headings and
        # no unit map, so its sub-modul are CANDIDATE units and nothing more.
        out.append(dict(
            course="K5", pl=pl["pl"], title=pl["title"],
            in_lane_6_scope=in_scope,
            module_pages=[lo, hi], page_count=pages,
            sub_modul_count=len(pl["sub_modul"]),
            sub_modul=pl["sub_modul"],
            source_availability="LOCAL_BINARY_HASH_VERIFIED",
            quiz_available=False,
            quiz_note=("The K5 module carries no LATIHAN or SKEMA JAWAPAN section anywhere. "
                       "K3's packages do. Every K5 quiz to date has been drafted from "
                       "content, and that remains true for every PL here."),
            confirmed_units=(14 if is_pl06 else 0),
            candidate_units=(0 if is_pl06 else len(pl["sub_modul"])),
            unit_basis=("FROZEN_BOUNDARY_MAP" if is_pl06
                        else "SUB_MODUL_HEADING_ONE_CANDIDATE_EACH"),
            shared_boundary_risk=_shared_risk(pl),
            source_completeness="COMPLETE_BODY_TEXT_PRESENT",
            unmapped=not is_pl06))
    return dict(
        course="K5", scope_requested=LANE_6_SCOPE,
        pakej_latihan_in_module=len(K5_SYLLABUS),
        syllabus_authority="module's own syllabus table, module pages xvii-xviii",
        prior_estimate=PRIOR_ESTIMATE_NOT_CARRIED,
        findings=K5_FINDINGS,
        rows=out,
        totals=dict(
            confirmed_units=sum(r["confirmed_units"] for r in out),
            candidate_units=sum(r["candidate_units"] for r in out),
            unmapped_source_regions=len([r for r in out if r["unmapped"]]),
            unmapped_pages=sum(r["page_count"] for r in out if r["unmapped"]),
            total_module_pages=sum(r["page_count"] for r in out)))


def _shared_risk(pl):
    pages = [s["page"] for s in pl["sub_modul"]]
    dupes = sorted({p for p in pages if pages.count(p) > 1})
    if dupes:
        return dict(risk=True, shared_pages=dupes,
                    note="Two sub-modul begin on the same printed page.")
    return dict(risk=False, shared_pages=[],
                note="No two sub-modul in this PL begin on the same printed page. Whether a "
                     "unit boundary inside a sub-modul shares a page is not determined until "
                     "that unit is mapped.")


# ==========================================================================================
# LANE 4 (second half) — provisional models for the first two SOURCE_READY_CLEAN K3 units
#
# Same five classifications as the PL06 batch 1 models. One thing differs sharply and is
# worth saying plainly: a K3 package ships with its OWN assessment. LATIHAN carries the
# questions and SKEMA JAWAPAN (UNTUK PENGAJAR) carries the model answers. K5 has neither
# anywhere in its module, which is why every K5 quiz so far has been drafted from content.
# That is a source-supplied answer scheme — still not an approved storyboard answer key, and
# still in the wrong format for the course-wide 4 MCQ + 1 MR rule.
# ==========================================================================================
K3_ASSESSMENT_FINDING = dict(
    id="K3-ASSESS-01",
    finding=("Both K3 units carry a source-authored LATIHAN and a SKEMA JAWAPAN. The "
             "questions are short-essay with a 15-minute allowance and three model answers "
             "each. The course-wide rule AR-01 is 4 Multiple Choice + 1 Multiple Response. "
             "The source assessment and the course format do not match."),
    classification="PENDING_BARIAH_PATTERN_DECISION",
    options_not_chosen=[
        "convert the three source essay questions into the 4+1 format, keeping the SKEMA "
        "answers as the key material",
        "keep the source essay assessment as-is for K3 and treat 4+1 as K5-shaped",
        "run both — source LATIHAN as a reflection, 4+1 as the scored quiz"],
    note=("Not chosen here. This is exactly the kind of format decision the pattern package "
          "under review exists to settle, and the source answers are strong enough that "
          "guessing would waste them."))

K3_MODELS = {
    "PL01": dict(
        unit_id="K3-M01-PL01", title="Pengenalan Pengurusan Kerja Penstabilan Tanah",
        groups=[dict(group_id="G1", covers="Asas konsep penyiasatan dan penstabilan tanah"),
                dict(group_id="G2", covers="Kepentingan penyiasatan tanah"),
                dict(group_id="G3", covers="Kepentingan penstabilan tanah"),
                dict(group_id="G4", covers="Kaedah penyiasatan tanah"),
                dict(group_id="G5", covers="Kaedah penstabilan tanah"),
                dict(group_id="G6", covers="Faktor pemilihan kaedah penyiasatan"),
                dict(group_id="G7", covers="Faktor pemilihan kaedah penstabilan")],
        grouping_basis="TOP_LEVEL_NUMBERED_SECTION",
        pattern=dict(primary="click-to-reveal", secondary="comparison",
                     reason=("Two eight-row importance tables and two five-method lists sit "
                             "in parallel — penyiasatan against penstabilan — which is a "
                             "comparison; the method lists themselves are reveals.")),
        dialogue=dict(verdict="NOT_JUSTIFIED",
                      reason="A concepts-and-methods package with no decision scenario in "
                             "the source."),
        visual_subjects=[
            dict(subject="Rajah 1: Surface Reconnaissance", has_source_figure=True),
            dict(subject="Rajah 2: Dynamic Cone Penetrometer", has_source_figure=True),
            dict(subject="Rajah 3: Boring", has_source_figure=True),
            dict(subject="Rajah 4: Standard Penetration Test – SPT", has_source_figure=True),
            dict(subject="Rajah 5: Soil Laboratory Testing", has_source_figure=True),
            dict(subject="Rajah 6: Pemilihan Kaedah Penyiasatan Tanah",
                 has_source_figure=True),
            dict(subject="Rajah 7: Faktor-Faktor Pemilihan Kaedah Penstabilan Tanah",
                 has_source_figure=True)],
        source_assessment=dict(
            questions=["Jelaskan kepentingan penyiasatan tanah dalam pembinaan.",
                       "Huraikan dua kaedah penstabilan tanah dan situasi penggunaannya.",
                       "Apakah faktor yang mempengaruhi pemilihan kaedah penyiasatan tanah?"],
            model_answers=[
                ["Menentukan sifat dan keadaan tanah tapak",
                 "Mengurangkan risiko kegagalan struktur",
                 "Menyediakan data teknikal untuk reka bentuk asas"],
                ["Penstabilan mekanikal", "Penstabilan kimia",
                 "Penstabilan melalui penggantian tanah (soil replacement)"],
                ["Jenis tanah (liat, pasir, gambut)", "Akses dan keadaan tapak",
                 "Tujuan projek dan jenis struktur"]],
            cls="SOURCE_DERIVED", key_status="SOURCE_AUTHORED_NOT_STORYBOARD_APPROVED"),
        rumusan_beats=["Penyiasatan tanah dan penstabilan tanah sebagai dua proses yang "
                       "saling melengkapi.",
                       "Lima kaedah penyiasatan dan lima kaedah penstabilan.",
                       "Faktor yang menentukan pemilihan kaedah di tapak."]),
    "PL03": dict(
        unit_id="K3-M01-PL03",
        title="Inovasi Teknologi Digital dan Automasi dalam Penstabilan Tanah",
        groups=[dict(group_id="G1", covers="Pengenalan kepada digital dan inovasi"),
                dict(group_id="G2", covers="Teknologi digital: peralatan, bahan, mesin"),
                dict(group_id="G3", covers="Cabaran dan strategi pelaksanaan")],
        grouping_basis="TOP_LEVEL_NUMBERED_SECTION",
        pattern=dict(primary="click-to-reveal", secondary="comparison",
                     reason=("Section 2 fans into three categories of four lettered items "
                             "each — twelve reveals in a three-way structure. Section 3 is a "
                             "challenge-against-strategy table, which is a comparison.")),
        dialogue=dict(verdict="NOT_JUSTIFIED",
                      reason="A technology catalogue. No scenario in the source."),
        visual_subjects=[
            dict(subject="Twelve digital technologies across peralatan, bahan and mesin",
                 has_source_figure=False),
            dict(subject="Jadual: cabaran against strategi mengatasi",
                 has_source_figure=False)],
        source_assessment=dict(
            questions=["Terangkan dua contoh teknologi peralatan digital yang digunakan "
                       "dalam kerja penyiasatan tanah serta huraikan bagaimana ia membantu "
                       "kontraktor mengesahkan reka bentuk yang diberi oleh perunding.",
                       "Jelaskan peranan bahan teknologi baharu seperti Smart Polymer, "
                       "Nano-Silika atau MICP dalam meningkatkan keberkesanan kerja "
                       "penstabilan tanah oleh kontraktor.",
                       "Huraikan 2 contoh mesin yang digunakan dalam kerja penstabilan tanah "
                       "dan jelaskan bagaimana teknologi automasi membantu meningkatkan "
                       "kawalan kualiti di tapak pembinaan."],
            model_answers=[
                ["GPR AI-Enhanced", "UAV LiDAR Hybrid", "IoT Geotechnical Sensors",
                 "Cloud-based GIS & Automated Data Logger"],
                ["Smart Polymer Soil Stabiliser", "Nano-Silika dan Geopolimer",
                 "Biopolimer dan Enzim Stabiliser", "MICP Industri"],
                ["Automated Drilling Rig & Digital CPTu",
                 "Jet Grouting Machine Digital dengan Flow Control",
                 "Deep Soil Mixing GPS Integrated",
                 "Vibro-Compaction 4.0 & Dynamic Compaction AI-Controlled"]],
            cls="SOURCE_DERIVED", key_status="SOURCE_AUTHORED_NOT_STORYBOARD_APPROVED",
            marks_note="The SKEMA allocates marks per part — 2 + 4 + 4 for each question."),
        rumusan_beats=["Teknologi digital sebagai pengganti dan pelengkap kaedah "
                       "tradisional.",
                       "Tiga kategori inovasi: peralatan, bahan dan mesin.",
                       "Tiga cabaran pelaksanaan dan strategi mengatasinya."]),
}

SHELL_ALWAYS = 2
CLOSING = 3


def k3_models():
    out = []
    for pl, m in K3_MODELS.items():
        read = K3_READ[pl]
        dialogue_used = m["dialogue"]["verdict"] == "JUSTIFIED"
        shell = SHELL_ALWAYS + (1 if dialogue_used else 0)
        groups = m["groups"]
        out.append(dict(
            course="K3", pl=pl, unit_id=m["unit_id"], title=m["title"],
            authority_inherited=AUTHORITY, stage=STAGE,
            source=dict(cls="SOURCE_DERIVED", pages=read["pages"],
                        top_sections=len(read["top_sections"]),
                        tables=read["tables"], figures=read["figures"],
                        drive_id=next(p["drive_id"] for p in A.K3_PDFS if p["pl"] == pl)),
            grouping=dict(cls="CAIR_PROPOSAL", basis=m["grouping_basis"], groups=groups),
            screen_sequence=dict(cls="CAIR_PROPOSAL", arithmetic=dict(
                shell_screens=shell, shell_includes_dialogue=dialogue_used,
                content_groups=len(groups), closing_screens=CLOSING,
                minimum_total_screens=shell + len(groups) + CLOSING,
                maximum_total_screens="UNKNOWN_PENDING_PATTERN_DECISION")),
            pattern_family=dict(cls="PENDING_BARIAH_PATTERN_DECISION",
                                primary_candidate=m["pattern"]["primary"],
                                secondary_candidate=m["pattern"]["secondary"],
                                reason=m["pattern"]["reason"]),
            dialogue=dict(cls="CAIR_PROPOSAL", verdict=m["dialogue"]["verdict"],
                          reason=m["dialogue"]["reason"],
                          cast="NO_CHARACTER_PROPOSED_STOP_006_OPEN"),
            runtime_state_estimate=dict(cls="CAIR_PROPOSAL",
                                        base_states_floor=shell + len(groups) + CLOSING,
                                        triggered_states="UNKNOWN_PENDING_PATTERN_DECISION",
                                        total_runtime_states=
                                        "UNKNOWN_PENDING_PATTERN_DECISION"),
            rumusan=dict(cls="CAIR_PROPOSAL", beat_count=len(m["rumusan_beats"]),
                         beats=m["rumusan_beats"],
                         treatment_cls="COURSE_RULE_ALREADY_APPROVED"),
            source_assessment=m["source_assessment"],
            assessment_format_conflict=K3_ASSESSMENT_FINDING,
            visual_obligations=dict(
                cls="CAIR_PROPOSAL", count=len(m["visual_subjects"]),
                source_attested=len([v for v in m["visual_subjects"]
                                     if v["has_source_figure"]]),
                subjects=m["visual_subjects"],
                note=("Unlike every K5 unit in this run, PL01's visual subjects are named "
                      "and captioned in the source itself. RP-104 is satisfiable here in a "
                      "way it is not for K5 batch 1.")),
            frozen_nothing=["screen count", "sequence", "dialogue", "Rumusan form",
                            "pattern family", "assessment key", "visual reuse"]))
    return out


def inventory():
    return dict(stage=STAGE, authority=AUTHORITY,
                k3=k3_inventory(), k3_models=k3_models(),
                k2=k2_decomposition(), k5=k5_remaining_inventory())


if __name__ == "__main__":
    inv = inventory()
    k3, k2, k5 = inv["k3"], inv["k2"], inv["k5"]
    print(f"K3: {k3['pdfs']} PDFs, {k3['read_in_full']} read in full, "
          f"{k3['identified_not_read']} identified not read, "
          f"{k3['candidate_units_evidenced']} candidate units evidenced")
    print(f"K2: {k2['outcome']} — {k2['missing_capability']['exact_identifier']}")
    t = k5["totals"]
    print(f"K5: {k5['pakej_latihan_in_module']} Pakej Latihan, "
          f"confirmed {t['confirmed_units']}, candidate {t['candidate_units']}, "
          f"unmapped regions {t['unmapped_source_regions']} "
          f"({t['unmapped_pages']} pages of {t['total_module_pages']})")
