# -*- coding: utf-8 -*-
"""Stage 4.2F-D Lane 3-4 — K3 package inventory, provisional models, course decision.

    python3 docs/source/tools/src_k3_v1.py

READ STATUS, STATED PLAINLY
---------------------------
All nine are read in full. PL01 and PL03 in Stage 4.2F-C; PL02, PL04, PL05, PL06, PL07,
PL08 and PL09 in this run. Nothing in the K3 inventory is described from a template or
inferred from a sibling.

WHAT THE NINE PACKAGES SHOW
---------------------------
The nine PDFs are NOT one module. They span six:

    M01 BUSINESS OPERATION MANAGEMENT ......... PL01, PL02, PL03
    M02 TENDERING MANAGEMENT .................. PL04
    M03 CONTRACT IMPLEMENTATION & MANAGEMENT .. PL05
    M04 PROJECT PLANNING AND SCHEDULING ....... PL06
    M05 CONSTRUCTION OPERATION MANAGEMENT ..... PL07, PL08
    M06 PROJECT HANDOVER ...................... PL09

Stage 4.2F-C recorded a single module code from PL01 and PL03 alone. PL05 disproved it, and
the five read here settled the real shape. Any K3 unit map has to respect six modules.

Every one of the nine carries its own LATIHAN and its own SKEMA JAWAPAN. That is a
source-authored assessment, and it is why the K5 rule is not applied here.

The question count is NOT uniform. Seven packages carry five questions; PL01 and PL03 carry
three. Forty-one questions in total, counted from the nine sources, not assumed.

The nine answer keys take four different structural shapes under six different labels, and
one of them — PL03 — is not a model answer at all but a marking rubric with explicit mark
allocations. Whatever K3-COURSE-01 decides, a single pipeline has to cope with that spread.
It is put in front of the decision rather than smoothed over.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import src_authority_v1 as A     # noqa: E402
import src_inventory_v1 as INV   # noqa: E402

STAGE = "4.2F-D"
AUTHORITY = "SRC-AUTH-01"
NOT_READ = "IDENTIFIED_NOT_READ"
UNKNOWN = "UNKNOWN_NOT_MEASURED"

K5_RULE_NOT_APPLIED = dict(
    rule="4 Multiple Choice + 1 Multiple Response, 60 percent threshold",
    applies_to="K5",
    applied_to_k3=False,
    why=("K3 packages ship their own LATIHAN and SKEMA JAWAPAN. Imposing K5's composition "
         "would discard a source-authored assessment with model answers and mark "
         "allocations. Every K3 model classifies assessment as "
         "PENDING_K3_COURSE_ASSESSMENT_RULE."))

K3_ASSESSMENT_CLASS = "PENDING_K3_COURSE_ASSESSMENT_RULE"

# Read in this run, added to the two from the previous one.
READ_THIS_RUN = {
    "PL02": dict(
        module_code="M01", module_title="BUSINESS OPERATION MANAGEMENT",
        pages=28, page_marker_style="Page: n/28",
        tajuk="PENGURUSAN PEMATUHAN KERJA PENSTABILAN TANAH",
        header_self_title="Pengurusan Pematuhan Kerja Penstabilan Tanah",
        top_sections=["PENGURUSAN PEMATUHAN UNDANG-UNDANG DAN PERATURAN TEMPATAN",
                      "PENGURUSAN SUMBER MANUSIA",
                      "PENGURUSAN ASET SYARIKAT"],
        sub_sections=["1.1 Kelulusan Pihak Berkuasa Tempatan (PBT)",
                      "1.2 Keperluan Undang-Undang Kontrak – Akta 520 (CIDB)",
                      "1.3 Permit Alam Sekitar berkaitan Disposal – DOE",
                      "2.1 Keperluan Pekerja Pakar", "2.2 Rekod Kehadiran dan Gaji",
                      "2.3 Permit Pekerja Asing", "2.4 Latihan Keselamatan",
                      "2.5 Pengurusan Keselamatan di Tapak",
                      "2.6 Dokumentasi Pengurusan Sumber",
                      "3.1 Mesin dan Peralatan", "3.2 Penyelenggaraan Mesin",
                      "3.3 Pengurusan Inventori Bahan"],
        lettered_descendants=True,
        lettered_note="1.1 fans into a) JPS, b) JKR, c) JMG, d) JKKP — four named agencies",
        tables=0, figures=10,
        figure_note=("Rajah 1 to Rajah 13 are referenced but the numbering skips — no Rajah 4 "
                     "or 9, and Rajah 6 is used twice for different subjects. Recorded, not "
                     "corrected."),
        latihan=True, latihan_questions=5, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=5,
        classification="SOURCE_READY_CLEAN", candidate_units=1,
        boundary="Self-contained: own header, own page numbering 1/28 to 28/28, own LATIHAN "
                 "and SKEMA JAWAPAN.",
        complexity=("HIGH — three top sections, twelve sub-sections, four named regulatory "
                    "agencies with distinct duties, and ten figures. The heaviest of the "
                    "four read so far."),
        compliance_heavy=True,
        named_authorities=["PBT", "JPS", "JKR", "JMG", "JKKP", "CIDB (Akta 520)", "DOE/JAS",
                           "LHDN", "Jabatan Imigresen", "Jabatan Tenaga Kerja"]),
    "PL05": dict(
        module_code="M03", module_title="CONTRACT IMPLEMENTATION & MANAGEMENT",
        pages=18, page_marker_style="Muka Surat: n/18",
        tajuk="PERLAKSANAAN DAN PENGURUSAN KONTRAK PENSTABILAN TANAH",
        header_self_title="Pelaksanaan dan Pengurusan Kontrak Penstabilan Tanah",
        top_sections=["PENGURUSAN ANUGERAH KONTRAK PROJEK PENSTABILAN TANAH",
                      "KEPERLUAN KONTRAK BERKENAAN KERJA PENSTABILAN TANAH",
                      "PENGURUSAN PENSIJILAN DAN PEMBAYARAN KONTRAK",
                      "PENGURUSAN PENAMATAN KONTRAK PROJEK PENSTABILAN TANAH",
                      "PENGURUSAN PENYELESAIAN PERTIKAIAN DALAM PROJEK PENSTABILAN TANAH"],
        sub_sections=["1.1 Perkaitan dengan Main Contract",
                      "1.2 Penyediaan Dokumen Kontrak", "1.3 Pengurusan Lampiran Teknikal",
                      "2.1 Method of Statement", "2.2 Garis Panduan",
                      "2.3 Unsuitable Material", "2.4 Justifikasi melalui Pengesahan Tapak",
                      "3.1 Pensijilan Interim", "3.2 Laporan Progress Kerja",
                      "3.3 Tuntutan Interim Payment (IPC)",
                      "3.4 Pengurusan Tuntutan Variation Order",
                      "3.5 Dokumentasi Sokongan", "4.1 Lawful Termination",
                      "4.2 Sebab Penamatan", "4.3 Impak kepada Kos", "4.4 Re-mobilisation",
                      "4.5 Pengurusan Dokumen", "5.1 ADR, Arbitration, Litigation",
                      "5.2 Dokumen Pertikaian", "5.3 Rundingan Kos",
                      "5.4 Without Prejudice Communication", "5.5 Langkah Elak Pertikaian"],
        lettered_descendants=True,
        lettered_note="2.1 carries a) to d) — a four-step worked method statement",
        tables=0, figures=1,
        figure_note="Rajah 1: Contoh Method Statement JKR",
        latihan=True, latihan_questions=5, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=5,
        classification="SOURCE_READY_CLEAN", candidate_units=1,
        boundary="Self-contained, 18 pages, own LATIHAN and SKEMA JAWAPAN.",
        complexity=("HIGH — five top sections and twenty-two sub-sections, the widest "
                    "structure of the four. Heavily worked-example driven, with named "
                    "monetary figures throughout."),
        compliance_heavy=True,
        named_authorities=["JKR", "DOE", "FIDIC", "P.W.D. 203A", "CIDB", "BCA"]),
    "PL04": dict(
        module_code="M02", module_title="TENDERING MANAGEMENT",
        pages=27, page_marker_style="Muka Surat: n/27",
        tajuk="PENGURUSAN TENDER PENSTABILAN TANAH",
        header_self_title="PL04 Pengurusan Tender Penstabilan Tanah",
        top_sections=["JENIS PROJEK BERKAITAN KERJA PENSTABILAN TANAH",
                      "SKOP PROJEK PENSTABILAN TANAH",
                      "PENYEDIAAN DATA KOS, PENGANGGARAN DAN PENENTUAN HARGA PROJEK "
                      "PENSTABILAN TANAH",
                      "BAJET PROJEK SOIL STABILISATION",
                      "PROSES TENDER PROJEK SOIL STABILISATION"],
        sub_sections=["1.1 Projek Membina Bangunan",
                      "1.2 Projek Pembinaan Jambatan di bahagian Tembok Landas atau "
                      "Abutment, Embankment atau Approach Fill dan Asas Struktur",
                      "1.3 Projek Infrastruktur",
                      "2.1 Komponen Skop Kerja Penstabilan Tanah",
                      "2.2 Komponen Skop Kerja Penyiasatan Tapak",
                      "2.3 Site Investigation (SI) untuk Projek Soil Stabilisation",
                      "2.4 Keperluan Spesifikasi Projek (JKR, MS Standards)",
                      "2.5 Keperluan Regulatory Projek Soil Stabilisation",
                      "2.6 Penyediaan Ringkasan Skop Kerja untuk Dokumen Tender",
                      "2.7 Risiko Skop Projek: Air Table Tinggi, Jenis Tanah, Lokasi Tapak",
                      "3.1 Komponen Kos Projek Penstabilan Tanah",
                      "3.2 Pengiraan Kos: Lime/Cement Stabilisation vs Chemical Grouting",
                      "3.3 Penyediaan Bill of Quantities (BQ) Kerja Soil Stabilisation",
                      "3.4 Analisis Harga Unit (Unit Rate Analysis)",
                      "3.5 Penggunaan Data Harga Semasa (Jadual Kadar Harga)",
                      "3.6 Pengiraan Margin Untung dan Risiko Projek",
                      "4.1 Komponen Kos", "4.2 Pengiraan Kos Mengikut Kaedah",
                      "4.3 Penyediaan Laporan Kewangan", "4.4 Risiko Kewangan",
                      "4.5 Penilaian Kewangan Tender",
                      "5.1 Proses Tender (Kerajaan & Swasta)",
                      "5.2 Penyediaan Dokumen Tender", "5.3 Jadual Tender",
                      "5.4 Lawatan Tapak", "5.5 Penilaian Tender", "5.6 Rundingan Harga",
                      "5.7 Dokumen Penyerahan"],
        lettered_descendants=True,
        lettered_note="3.1 fans into a) Bahan Kimia, b) Mesin, c) Buruh, d) Logistik; 3.6 "
                      "carries a) to d) as a four-line worked margin calculation",
        tables=5, figures=4,
        figure_note=("Labels read Rajah 1, Rajah 3, Rajah 4 (infografik) and Rajah 4 "
                     "(Standard Specification JKR). There is no Rajah 2, and Rajah 4 is "
                     "used twice for different subjects. Recorded, not corrected."),
        rujukan=True, rujukan_entries=6,
        latihan=True, latihan_questions=5, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=5, skema_format="numbered prose, 1. to 5.",
        classification="SOURCE_READY_CLEAN", candidate_units=1,
        boundary="Self-contained, 27 pages, own RUJUKAN, own LATIHAN and SKEMA JAWAPAN.",
        complexity=("HIGH — five top sections and twenty-eight sub-sections. Numeric "
                    "throughout: a BQ worked example, a unit-rate build-up, a July 2025 "
                    "rate table and a margin/risk calculation."),
        compliance_heavy=True,
        named_authorities=["JKR", "MOF", "CIDB", "DOE", "PBT", "SPAN", "JKKP", "SIRIM",
                           "Jabatan Perangkaan Malaysia"]),
    "PL06": dict(
        module_code="M04", module_title="PROJECT PLANNING AND SCHEDULING",
        pages=33, page_marker_style="Muka Surat: n/33",
        tajuk="PERANCANGAN DAN PENJADUALAN PROJEK PENSTABILAN TANAH",
        header_self_title="PL06 Perancangan dan Penjadualan Projek Penstabilan Tanah",
        top_sections=["PENYEDIAAN WORK BREAKDOWN STRUCTURE (WBS)",
                      "PENYEDIAAN JADUAL KERJA PROJEK PENSTABILAN TANAH",
                      "PENGURUSAN RISIKO PENJADUALAN BAGI KERJA PENSTABILAN TANAH"],
        sub_sections=["1.1 Konsep Asas WBS dalam Projek Kerja Penstabilan Tanah",
                      "1.2 Penyusunan Skop Kerja Penstabilan Tanah",
                      "1.3 Contoh Template WBS Untuk Projek Penstabilan Tanah",
                      "1.4 Integrasi WBS dengan Dokumen Tender",
                      "1.5 Elemen Utama dalam Integrasi",
                      "1.6 Kesan Ketiadaan Integrasi WBS dengan Dokumen Tender",
                      "2.1 Kepentingan Jadual Kerja dalam Projek Penstabilan Tanah",
                      "2.2 Kaedah Penyediaan Jadual Kerja",
                      "2.3 Penentuan Aktiviti Kritikal", "3.1 Risiko Kelewatan Projek",
                      "3.2 Strategi Pemulihan Projek (Catch-Up Plan)",
                      "3.3 Senarai Semak Risiko Penjadualan",
                      "3.4 Penyediaan Delay Notification",
                      "3.5 Penyelarasan Jadual Kerja dengan Aktiviti Pihak Ketiga",
                      "3.6 Pengurusan Konflik Zon Kerja Antara Tred Berbeza"],
        lettered_descendants=True,
        lettered_note="37 lettered items; 1.2 fans into a) to e) as the five project "
                      "phases, and 2.3 carries a roman-numbered penalty sub-list",
        tables=5, figures=7,
        figure_note="Rajah 1 to Rajah 7 and Jadual 1 to Jadual 5, numbered without gaps.",
        rujukan=False, rujukan_entries=0,
        latihan=True, latihan_questions=5, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=5,
        skema_format="two-column table; each answer restates its question beside it",
        classification="SOURCE_READY_CLEAN", candidate_units=1,
        boundary="Self-contained, 33 pages, own LATIHAN and SKEMA JAWAPAN. No RUJUKAN "
                 "section — unlike PL04, PL08 and PL09.",
        complexity=("MEDIUM-HIGH — only three top sections but fifteen sub-sections and a "
                    "worked WBS, Gantt chart and float calculation running through them."),
        compliance_heavy=False,
        named_authorities=["JKR"]),
    "PL07": dict(
        module_code="M05", module_title="CONSTRUCTION OPERATION MANAGEMENT",
        pages=43, page_marker_style="Muka Surat: n/43",
        tajuk="PENGURUSAN OPERASI PEMBINAAN BAGI KERJA PENSTABILAN TANAH",
        header_self_title="PL07 Pengurusan Operasi Pembinaan Bagi Penstabilan Tanah",
        top_sections=["PENGURUSAN KUALITI PROJEK KERJA PENSTABILAN TANAH",
                      "PENGURUSAN KESELAMATAN DAN KESIHATAN (OSH) TAPAK PENSTABILAN",
                      "PENGURUSAN PERLINDUNGAN ALAM SEKITAR DALAM PROJEK KERJA-KERJA "
                      "PENSTABILAN TANAH",
                      "PENGURUSAN TRAFIK TAPAK DALAM PROJEK KERJA-KERJA PENYIASATAN DAN "
                      "PENSTABILAN TANAH",
                      "PENGURUSAN MOBILISASI FIZIKAL TAPAK PROJEK BAGI KERJA-KERJA "
                      "PENSTABILAN TANAH",
                      "PELAKSANAAN DAN PEMANTAUAN KERJA BAGI KERJA-KERJA PENYIASATAN DAN "
                      "PENSTABILAN TANAH",
                      "PENGURUSAN PENAMATAN TAPAK PROJEK (DEMOBILISATION) BAGI KERJA "
                      "PENSTABILAN TANAH"],
        sub_sections=["1.1 Kepentingan Pengurusan Kualiti", "1.2 Penyediaan Inspection "
                      "Test Plan (ITP)", "1.3 Kawalan Kualiti Bahan Binaan",
                      "1.4 Kawalan Kualiti Kaedah Kerja", "1.5 Pengurusan Rekod Kualiti",
                      "1.6 Penyediaan Mock-Up atau Trial Section",
                      "2.1 Pengenalan OSH", "2.2 Risiko Keselamatan Lime Stabilisation",
                      "2.3 Risiko Keselamatan Grouting", "2.4 Penyediaan HIRARC",
                      "2.5 Penyediaan Emergency Response Plan (ERP)",
                      "2.6 Kawalan Kebersihan dan Kekemasan Tapak (Housekeeping)",
                      "3.1 Pematuhan Undang-Undang dan Peraturan Alam Sekitar",
                      "3.2 Kawalan Hakisan dan Sedimentasi",
                      "3.3 Kawalan Air Larian Permukaan", "3.4 Kawalan Debu",
                      "3.5 Pengurusan Sisa Terjadual", "3.6 Pemantauan dan Audit Alam "
                      "Sekitar oleh Pihak Berkuasa (DOE, PBT)",
                      "4.1 Pelan Pengurusan Trafik (TMP)",
                      "4.2 Laluan Kenderaan Berat", "4.3 Penyelarasan Waktu Penghantaran",
                      "4.4 Kawalan Trafik Tapak oleh Flagmen", "4.5 Pengurusan Haul Road",
                      "4.6 Komunikasi dengan Pihak Berkuasa Tempatan",
                      "5.1 Penyediaan Pelan Mobilisasi Tapak",
                      "5.2 Penyediaan Kawasan Penyimpanan Bahan",
                      "5.3 Penubuhan Pejabat Tapak dan Stor Bahan Kimia",
                      "5.4 Penyediaan Kemudahan Utiliti Sementara",
                      "5.5 Penandaan Zon Kerja", "5.6 Penyediaan Laluan Kerja dan Signage",
                      "6.1 Penyelarasan Aktiviti Tapak",
                      "6.2 Pemantauan Kemajuan Kerja", "6.3 Penyediaan Laporan Tapak",
                      "6.4 Pelaksanaan Pemeriksaan Kerja dan Permintaan Pemeriksaan",
                      "6.5 Pengurusan Isu Teknikal Semasa Pelaksanaan Kerja",
                      "6.6 Penyediaan dan Kelulusan Method Statement",
                      "7.1 Penyediaan Pelan Penamatan Tapak",
                      "7.2 Kerja Pembersihan Tapak Mengikut Spesifikasi Pihak Berkuasa",
                      "7.3 Pengurusan Pengeluaran Mesin, Peralatan dan Baki Bahan Kimia",
                      "7.4 Penyediaan Tapak untuk Penyerahan kepada Pemilik Projek",
                      "7.5 Penyediaan Laporan Penamatan Tapak",
                      "7.6 Penyediaan Rekod As-Built berkaitan Penstabilan Tanah"],
        lettered_descendants=True,
        lettered_note="174 lettered items, by far the most of the nine; many fan again "
                      "into roman-numbered sub-lists",
        tables=3, figures=6,
        figure_note=("Labels read Rajah 1, 2, 3, 4, then Rajah 3 and Rajah 4 again for "
                     "different subjects. The numbering restarts mid-document. Recorded, "
                     "not corrected."),
        rujukan=False, rujukan_entries=0,
        latihan=True, latihan_questions=5, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=5, skema_format="'Soalan N:' prose",
        classification="SOURCE_READY_CLEAN", candidate_units=1,
        boundary="Self-contained, 43 pages — the longest of the nine. No RUJUKAN section.",
        complexity=("VERY HIGH — seven top sections, forty-two sub-sections and 174 "
                    "lettered items. The largest single K3 package by every structural "
                    "measure, and the strongest candidate for splitting into more than one "
                    "production unit."),
        compliance_heavy=True,
        named_authorities=["DOE", "PBT", "JKKP", "DOSH", "JKR", "CIDB"]),
    "PL08": dict(
        module_code="M05", module_title="CONSTRUCTION OPERATION MANAGEMENT",
        pages=13, page_marker_style="Muka Surat: n/13",
        tajuk="PENGURUSAN TEKNIKAL DAN DOKUMENTASI UJIAN PENSTABILAN TANAH",
        header_self_title="PL08 Pengurusan Teknikal & Dokumentasi Ujian Penstabilan Tanah",
        top_sections=["PENGENALAN UJIAN TAPAK PENSTABILAN TANAH DAN PROSES VERIFIKASI",
                      "DOKUMENTASI DAN REKOD UJIAN TAPAK",
                      "PENGURUSAN ISU TEKNIKAL BERKAITAN UJIAN PENSTABILAN TANAH"],
        sub_sections=["1.1 Jenis Ujian Tapak Penstabilan Tanah",
                      "1.2 Peranan Confirmatory Site Investigation (SI)",
                      "1.3 Mackintosh Probe (MP) dan JKR Probe",
                      "1.4 Ujian Lanjutan Selepas MP",
                      "1.5 Rawatan Tanah Untuk Asas Cetek",
                      "2.1 Penyediaan Borang Rekod Ujian Tapak (Daily Test Report)",
                      "2.2 Penyimpanan Data Ujian untuk Tujuan Tuntutan Projek",
                      "2.3 Keperluan Consultant / Client untuk Dokumen Ujian",
                      "2.4 Pengurusan Isu Data Hilang atau Tidak Lengkap",
                      "3.1 Tindakan Remedial Work",
                      "3.2 Pengurusan Kos Kerja Ulangan (Rework Cost)",
                      "3.3 Komunikasi dengan Konsultan jika Ujian Tidak Memenuhi "
                      "Spesifikasi",
                      "3.4 Hubungan Data Ujian dengan Pembayaran Interim Certificate"],
        lettered_descendants=True,
        lettered_note="1.3 fans into a) to g) — seven distinct Mackintosh Probe "
                      "propositions; 1.4 into a) to g) as seven named tests",
        tables=2, figures=4,
        figure_note="Rajah 1 to Rajah 4 and Jadual 1 to Jadual 2, numbered without gaps.",
        rujukan=True, rujukan_entries=8,
        latihan=True, latihan_questions=5, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=5, skema_format="'Skema N:' bulleted",
        classification="SOURCE_READY_CLEAN", candidate_units=1,
        boundary="Self-contained, 13 pages — the shortest of the nine.",
        complexity=("MEDIUM — three top sections and thirteen sub-sections, but dense in "
                    "named field tests (MP, JKR Probe, SPT, CPT, FDT, CBR, Plate Load)."),
        compliance_heavy=False,
        named_authorities=["JKR", "CIDB", "BSI", "ASTM"]),
    "PL09": dict(
        module_code="M06", module_title="PROJECT HANDOVER",
        pages=28, page_marker_style="Muka Surat: n/28",
        tajuk="PENYERAHAN PROJEK PENSTABILAN TANAH",
        header_self_title="PL09 Penyerahan Projek Penstabilan Tanah",
        top_sections=["PENYERAHAN PROJEK PENSTABILAN TANAH",
                      "PENGURUSAN LIABILITI KECACATAN DAN CMGD",
                      "PENYEDIAAN DOKUMEN AKAUN AKHIR PROJEK"],
        sub_sections=["1.1 Jenis Dokumen Penyerahan Projek (As-Built, Test Reports, O&M)",
                      "1.2 Penyediaan Dokumen Handover Mengikut Spesifikasi Kontrak",
                      "1.3 Senarai Semak Dokumen Penyerahan (Handover Checklist)",
                      "1.4 Penyediaan Laporan Ujian (Test Result Reports)",
                      "1.5 Proses Serahan Tapak kepada Pemilik Projek",
                      "2.1 Definisi Liabiliti Kecacatan (Defect Liability)",
                      "2.2 Proses Pemeriksaan Pra-Penyerahan",
                      "2.3 Penyediaan Senarai Defect (Defect List)",
                      "2.4 Pengurusan Membetulkan Kecacatan (Making Good Defects)",
                      "2.5 Proses Mendapatkan Certificate of Making Good Defects (CMGD)",
                      "2.6 Tempoh Defect Liability Period (DLP) Mengikut Kontrak",
                      "2.7 Dokumentasi dan Pengesahan Pembaikan Defect",
                      "3.1 Komponen Akaun Akhir Projek (Final Account Components)",
                      "3.2 Penyediaan Laporan Final Account Mengikut Format Kontrak",
                      "3.3 Pengurusan Variation Orders (VO) dalam Final Account",
                      "3.4 Penyediaan Supporting Documents untuk Final Account",
                      "3.5 Rundingan Kos Akhir dengan Client atau Konsultan Projek",
                      "3.6 Penyediaan Final Statement of Account",
                      "3.7 Penyerahan Final Account kepada Pihak Berkuasa atau Client"],
        lettered_descendants=True,
        lettered_note="1.1 d) fans again into i) Kontraktor Utama, ii) Jurutera Perunding, "
                      "iii) Pemilik Projek — a three-role responsibility split",
        tables=0, figures=4,
        figure_note="Rajah 1 to Rajah 4, all four the same subject: contoh Borang "
                    "Penyerahan Projek JKR, occupying pages 5 to 8 one per page.",
        rujukan=True, rujukan_entries=6,
        latihan=True, latihan_questions=5, latihan_format="soalan esei pendek, 15 minit",
        skema_jawapan=True, skema_answers=5, skema_format="'Jawapan N:' prose",
        classification="SOURCE_READY_CLEAN", candidate_units=1,
        boundary="Self-contained, 28 pages, own RUJUKAN, own LATIHAN and SKEMA JAWAPAN.",
        complexity=("HIGH — three top sections but nineteen sub-sections, and the whole "
                    "package is a contractual close-out chain: handover, DLP, CMGD, "
                    "retention release, final account."),
        compliance_heavy=True,
        named_authorities=["JKR", "DOE", "BSI", "NRECC"]),
}

STILL_NOT_READ = []

READ_BUDGET_NOTE = (
    "All nine read in full: PL01 and PL03 in Stage 4.2F-C, and PL02, PL04, PL05, PL06, "
    "PL07, PL08 and PL09 in Stage 4.2F-D. No K3 package is described from a sibling's "
    "template or from an inferred pattern.")

# ==========================================================================================
# SKEMA JAWAPAN FORM — four structural shapes, six labels, one rubric that is not a key
# ==========================================================================================
# Read from each package's own SKEMA JAWAPAN section in this run. Two axes are recorded
# separately on purpose: `family` is what a parser has to cope with, `label` is only what
# the heading says. Collapsing them would hide that PL07, PL08 and PL09 differ in wording
# but not in structure — and would hide that PL03 differs in kind, not in wording.
SKEMA_SHAPES = {
    "PL01": dict(family="TABLE_QUESTION_RESTATED", label="No. Soalan / Jawapan",
                 questions=3, carries_marks=False,
                 note="Two-column table; the answer cell lists numbered alternatives."),
    "PL02": dict(family="TABLE_QUESTION_RESTATED", label="Soalan / Jawapan",
                 questions=5, carries_marks=False,
                 note="Two-column table; answers offer alternatives, one marked "
                      "'(pilih satu)'."),
    "PL03": dict(family="RUBRIC_WITH_MARK_ALLOCATION", label="SOALAN N",
                 questions=3, carries_marks=True,
                 note="Not a model answer. Lettered marking criteria a), b), c) with "
                      "explicit allocations — 2 markah + 4 markah + 4 markah, ten marks "
                      "per question, thirty for the package. The only one of the nine "
                      "that states marks anywhere."),
    "PL04": dict(family="PROSE_PER_QUESTION", label="1. to 5.",
                 questions=5, carries_marks=False,
                 note="Flowing prose, one numbered paragraph block per question."),
    "PL05": dict(family="BULLETED_PER_QUESTION", label="Skema Jawapan N:",
                 questions=5, carries_marks=False,
                 note="Bulleted points; question 2 adds a parenthetical acceptance rule "
                      "('mana-mana 3 dokumen ... diterima')."),
    "PL06": dict(family="TABLE_QUESTION_RESTATED", label="(no per-answer label)",
                 questions=5, carries_marks=False,
                 note="Two-column table; the question is restated in the left cell."),
    "PL07": dict(family="PROSE_PER_QUESTION", label="Soalan N:",
                 questions=5, carries_marks=False,
                 note="One prose paragraph per question."),
    "PL08": dict(family="BULLETED_PER_QUESTION", label="Skema N:",
                 questions=5, carries_marks=False,
                 note="Bulleted points; question 5 is a bare list of test names."),
    "PL09": dict(family="PROSE_PER_QUESTION", label="Jawapan N:",
                 questions=5, carries_marks=False,
                 note="Prose, except question 2 which is bulleted."),
}


# Reviewer-facing names. The document Bariah reads is in Malay; a structural family named
# only in English would make her decode the evidence before she can weigh it.
SKEMA_FAMILY_MS = {
    "TABLE_QUESTION_RESTATED": "jadual dua lajur",
    "RUBRIC_WITH_MARK_ALLOCATION": "rubrik bermarkah",
    "PROSE_PER_QUESTION": "prosa",
    "BULLETED_PER_QUESTION": "senarai berbutir",
}


def _skema_families():
    fams = {}
    for pl, s in SKEMA_SHAPES.items():
        fams.setdefault(s["family"], []).append(pl)
    return {k: sorted(v) for k, v in sorted(fams.items())}


SKEMA_FORM_FINDING = dict(
    observation_id="K3-SRC-OBS-02",
    subject="the shape of SKEMA JAWAPAN across the nine packages",
    evidence="Each package's own SKEMA JAWAPAN (UNTUK PENGAJAR) section, read in full.",
    uniform=dict(every_package_has_latihan=True, every_package_has_skema=True,
                 format="soalan esei pendek, 15 minit",
                 heading="SKEMA JAWAPAN (UNTUK PENGAJAR)"),
    not_uniform=dict(
        question_count=dict(five=["PL02", "PL04", "PL05", "PL06", "PL07", "PL08", "PL09"],
                            three=["PL01", "PL03"], total=41),
        structural_families=_skema_families(),
        distinct_labels=6,
        packages_carrying_marks=["PL03"]),
    sharpest_point=("PL03 is the outlier that matters. Its SKEMA is a marking rubric — "
                    "lettered criteria with mark allocations totalling ten per question — "
                    "not a model answer. The other eight supply answers a learner could be "
                    "shown; PL03 supplies instructions to a human marker. No automated "
                    "scoring can consume it as-is, and no learner can be shown it."),
    why_it_matters=("Whichever way K3-COURSE-01 is decided, one pipeline has to cope with "
                    "four answer-key structures, six labels, two question counts and one "
                    "rubric. Under option A the spread reaches the learner and the "
                    "inconsistency becomes visible; under option B it is discarded anyway "
                    "and PL03's marks are the only thing worth salvaging. The variance is "
                    "a cost input to the decision, not a defect to normalise quietly."),
    requires_instructional_decision=False,
    feeds_decision="K3-COURSE-01")

# ==========================================================================================
# PAGE-MARKER STYLE — two conventions across the nine
# ==========================================================================================
PAGE_MARKER_STYLE_FINDING = dict(
    observation_id="K3-SRC-OBS-03",
    subject="the footer convention across the nine packages",
    values=[dict(style="KOD PL <PL> Page: n/m", packages=["PL01", "PL02"]),
            dict(style="KOD PL <PL> Muka Surat: n/m",
                 packages=["PL03", "PL04", "PL05", "PL06", "PL07", "PL08", "PL09"])],
    finding=("Seven packages use the Malay 'Muka Surat'; PL01 and PL02 use the English "
             "'Page'. Both are the same field in the same position."),
    classification="TYPOGRAPHICAL",
    requires_instructional_decision=False,
    routed_to="FIRDAUS",
    route_type="CUSTODY_OR_METADATA_CORRECTION",
    in_bariah_addendum=False,
    production_impact=("A page-attribution oracle over K3 must accept both spellings. A "
                       "regex anchored on 'Muka Surat' alone silently returns zero pages "
                       "for PL01 and PL02 — the same class of failure as matching a "
                       "boolean against the string 'True'."))

# ==========================================================================================
# PL08 PAGE-MARKER DEFECT — a source typo, routed to Firdaus
# ==========================================================================================
PL08_PAGE_MARKER_DEFECT = dict(
    observation_id="K3-SRC-OBS-01",
    subject="the footer on the last page of K3 PL08",
    exact_value_observed="KOD PL PL08 Muka Surat: 1/13",
    expected_by_the_document_s_own_scheme="KOD PL PL08 Muka Surat: 13/13",
    where="the final page, the one carrying SKEMA JAWAPAN (UNTUK PENGAJAR)",
    evidence=("Pages 1 through 12 run 1/13 to 12/13 without a gap. The thirteenth and last "
              "page repeats 1/13. No page in the file is labelled 13/13."),
    classification="TYPOGRAPHICAL",
    requires_instructional_decision=False,
    routed_to="FIRDAUS",
    route_type="CUSTODY_OR_METADATA_CORRECTION",
    in_bariah_addendum=False,
    production_impact=("None on content. It does mean a page-reference oracle keyed on the "
                       "PL08 footer cannot resolve its last page, so PL08 page attribution "
                       "must use ordinal position, not the printed marker."))

# ==========================================================================================
# THE PL02 TITLE CONFLICT — resolved with the exact conflicting values
# ==========================================================================================
PL02_TITLE_INVESTIGATION = dict(
    conflict_id="K3-SRC-CONFLICT-01",
    subject="the title of K3 PL02",
    values=[
        dict(source="filename", exact_value="PAKEJ LATIHAN_PL02.pdf",
             carries_a_title=False,
             note="The filename carries the PL number and no title, so it cannot arbitrate."),
        dict(source="PL02's own package header (front matter, page 1)",
             exact_value="PL02 Pengurusan Pematuhan Kerja Penstabilan Tanah",
             carries_a_title=True),
        dict(source="PL02's own body heading (TAJUK, page 1)",
             exact_value="PENGURUSAN PEMATUHAN KERJA PENSTABILAN TANAH",
             carries_a_title=True),
        dict(source="PL03's package header (front matter)",
             exact_value="PL02 Pengurusan Pematuhan Kerja penstabilan Tanah",
             carries_a_title=True,
             note="Agrees on the words; differs only in the lower-case 'p' in 'penstabilan'."),
        dict(source="PL01's package header (front matter)",
             exact_value="PL02 Pengenalan Pengurusan Kerja Penstabilan Tanah",
             carries_a_title=True,
             note="The outlier, and the error is bigger than one row — see shift_diagnosis "
                  "below."),
    ],
    shift_diagnosis=dict(
        established_by="reading PL03 in full, which fixed PL03's true title",
        pl01_front_matter_as_printed=[
            "PL01 Pengenalan Pengurusan Kerja Penstabilan Tanah",
            "PL02 Pengenalan Pengurusan Kerja Penstabilan Tanah",
            "PL03 Pengurusan Pematuhan Kerja Penstabilan Tanah"],
        correct_titles=[
            "PL01 Pengenalan Pengurusan Kerja Penstabilan Tanah",
            "PL02 Pengurusan Pematuhan Kerja Penstabilan Tanah",
            "PL03 Inovasi Teknologi Digital dan Automasi Dalam Penstabilan Tanah"],
        finding=("Two rows are wrong, not one. PL01's row is right; PL02's row duplicates "
                 "PL01's title; PL03's row carries PL02's title. The list is shifted one "
                 "row down from the second entry, and PL03's real title does not appear "
                 "anywhere in it. The previous record described only the PL02 row because "
                 "PL03 had not yet been read."),
        corroboration=("PL02's own front matter and PL03's own front matter both list all "
                       "three correctly, so the shift is confined to PL01's copy.")),
    finding=("Three independent sources agree that PL02 is 'Pengurusan Pematuhan Kerja "
             "Penstabilan Tanah' — PL02's own front matter, PL02's own body TAJUK heading, "
             "and PL03's front matter. One source disagrees: PL01's front matter, whose "
             "second and third rows are shifted one place down. A package's own body "
             "heading outranks another package's front-matter list, and two further "
             "sources agree with it."),
    classification="TYPOGRAPHICAL",
    classification_reasoning=(
        "Not METADATA_ONLY, because a front-matter list is content a learner could read. "
        "Not SOURCE_AUTHORITY_CONFLICT, because the sources are not of equal weight — a "
        "package's own body heading is the stronger authority and it is corroborated twice. "
        "Not INSTRUCTIONAL_TITLE_DECISION_REQUIRED, because nobody has to choose a title: "
        "the correct one is evidenced three times over. It is a copy-paste error in PL01's "
        "front matter."),
    requires_instructional_decision=False,
    routed_to="FIRDAUS",
    route_type="CUSTODY_OR_METADATA_CORRECTION",
    in_bariah_addendum=False,
    action=("Report to Firdaus as a source-metadata correction against PL01's front matter. "
            "It does not go into the Bariah addendum, because putting a copy-paste error in "
            "front of the Instructional Designer as a decision would waste her attention."),
    secondary_note=("PL03's lower-case 'penstabilan' is a separate, smaller typographical "
                    "inconsistency in the same family. Recorded here, not raised separately."))

# ==========================================================================================
# K3-COURSE-01 — the one thing that IS a Bariah decision
# ==========================================================================================
K3_COURSE_DECISION = dict(
    decision_id="K3-COURSE-01",
    subject_ms="Rawatan penilaian bagi kursus K3",
    subject_en="assessment treatment for the K3 course",
    context_ms=("Kesembilan-sembilan pakej K3 telah dibaca sepenuhnya. Setiap satu "
                "membawa LATIHAN dan SKEMA JAWAPAN tersendiri, semuanya soalan esei "
                "pendek, 15 minit. Tetapi kandungannya tidak seragam:\n"
                "• Bilangan soalan: tujuh pakej ada 5 soalan; PL01 dan PL03 ada 3. "
                "Jumlah keseluruhan 41 soalan.\n"
                "• Bentuk skema: empat struktur berbeza — jadual dua lajur (PL01, PL02, "
                "PL06), prosa (PL04, PL07, PL09), senarai berbutir (PL05, PL08), dan "
                "rubrik pemarkahan (PL03) — di bawah enam label berbeza.\n"
                "• PL03 bukan jawapan model. Ia rubrik dengan peruntukan markah "
                "(2 + 4 + 4 = 10 markah setiap soalan). Ia arahan kepada pemeriksa, "
                "bukan jawapan yang boleh ditunjukkan kepada pelajar.\n"
                "Kursus K5 pula menggunakan 4 MCQ + 1 Multiple Response dengan ambang 60 "
                "peratus. Format-format ini tidak sama."),
    evidence_note_ms=("Semua angka di atas dikira daripada kesembilan-sembilan fail "
                      "sumber yang telah dibaca, bukan dianggarkan."),
    options=[
        dict(key="A", label_ms="Kekalkan format LATIHAN dan SKEMA JAWAPAN asal.",
             consequence_ms=("Tiada penulisan item baharu; skema sumber digunakan terus. "
                             "Tetapi esei tidak boleh dinilai automatik dalam LMS, jadi "
                             "setiap jawapan perlu disemak manusia dan tiada skor automatik "
                             "atau ambang lulus. Ketidakseragaman sumber turut sampai "
                             "kepada pelajar: sesetengah unit 5 soalan, dua unit 3 soalan, "
                             "dan PL03 tiada jawapan model langsung — hanya rubrik "
                             "pemeriksa yang tidak boleh dipaparkan."),
             production_cost_ms="RENDAH untuk pengarangan, TINGGI untuk penyemakan"),
        dict(key="B",
             label_ms="Transform latihan asal kepada 4 MCQ + 1 Multiple Response.",
             consequence_ms=("Boleh dinilai automatik dan sejajar dengan K5, dan "
                             "menyeragamkan kesemua sembilan unit kepada satu bentuk. "
                             "Tetapi 41 soalan esei perlu ditulis semula menjadi 45 item "
                             "objektif, dan pengganggu (distractor) perlu dikarang kerana "
                             "tiada satu pun sumber membekalkannya. Skema asal menjadi "
                             "bahan kunci, bukan item siap."),
             production_cost_ms="TINGGI untuk pengarangan, RENDAH untuk penyemakan"),
        dict(key="C", label_ms="Kekalkan latihan asal dan tambah kuiz modul.",
             consequence_ms=("Pelajar menghadapi dua penilaian. Latihan esei kekal sebagai "
                             "refleksi; kuiz baharu memberi skor. Kos pengarangan sama "
                             "seperti B, ditambah masa pelajar yang lebih panjang, dan "
                             "ketidakseragaman sumber tetap kelihatan dalam bahagian esei."),
             production_cost_ms="TINGGI — kedua-dua kos digabungkan"),
        dict(key="D", label_ms="Tentukan mengikut setiap PL.",
             consequence_ms=("Fleksibel, dan mengiktiraf bahawa sumber memang sudah "
                             "berbeza — PL03 khususnya membawa rubrik bermarkah yang tiada "
                             "pada lapan yang lain. Tetapi setiap PL memerlukan keputusan "
                             "berasingan dan kursus K3 tidak lagi mempunyai satu bentuk "
                             "penilaian yang seragam. Sembilan keputusan menggantikan "
                             "satu."),
             production_cost_ms="BERUBAH-UBAH — bergantung kepada campuran"),
    ],
    cair_recommendation=None,
    cair_note_ms=("Tiada cadangan CAIR. Lapan pakej membekalkan jawapan model yang boleh "
                  "terus digunakan; PL03 hanya rubrik bermarkah. Memilih tanpa keputusan "
                  "Bariah akan membazirkan lapan skema itu atau menyembunyikan jurang "
                  "PL03."),
    blocks=["K3 assessment modelling"],
    blocks_ms=["pemodelan penilaian K3"],
    does_not_block=["source reading", "content extraction", "visual modelling",
                    "screen modelling"],
    does_not_block_ms=["pembacaan sumber", "pengekstrakan kandungan", "pemodelan visual",
                       "pemodelan skrin"])


def k3_inventory():
    """The nine packages, with the four read filled in and five named as not read."""
    prev = INV.K3_READ
    rows = []
    for p in A.K3_PDFS:
        pl = p["pl"]
        r = dict(course="K3", pl=pl, filename=p["filename"], drive_id=p["drive_id"],
                 bytes=p["bytes"], bytes_source="DRIVE_METADATA", sha256=A.NOT_COMPUTED,
                 binary_local=False, authority_inherited=AUTHORITY)
        if pl in READ_THIS_RUN:
            r.update(read_status="CONNECTOR_TEXT_READ_IN_FULL", read_in="STAGE_4_2F_D",
                     **READ_THIS_RUN[pl])
        elif pl in prev:
            r.update(read_status="CONNECTOR_TEXT_READ_IN_FULL", read_in="STAGE_4_2F_C",
                     module_code="M01", module_title="BUSINESS OPERATION MANAGEMENT",
                     **prev[pl])
        else:
            r.update(read_status=NOT_READ, read_in=None, module_code=UNKNOWN,
                     pages=UNKNOWN, top_sections=UNKNOWN, tables=UNKNOWN, figures=UNKNOWN,
                     latihan=UNKNOWN, skema_jawapan=UNKNOWN, candidate_units=UNKNOWN,
                     classification="SOURCE_READY_PENDING_INVENTORY", complexity=UNKNOWN,
                     note=READ_BUDGET_NOTE)
        # Overlay the answer-key shape, read from each package's own SKEMA section in this
        # run. It is kept in one place so PL01 and PL03 — inventoried in Stage 4.2F-C,
        # before the shape was recorded — carry it too.
        shape = SKEMA_SHAPES.get(pl)
        if shape:
            r["skema_shape"] = shape
            r["skema_format"] = f"{shape['family']} ({shape['label']})"
            # Independent agreement check: the shape record and the package record count
            # questions separately. They must not be allowed to drift apart silently.
            if r.get("latihan_questions") not in (None, UNKNOWN):
                r["question_count_agrees"] = (r["latihan_questions"] == shape["questions"])
            else:
                r["question_count_agrees"] = None
        # Normalise the two enumerations Stage 4.2F-C and this run used for sub-sections.
        if "sub_sections" in r:
            r["sub_section_count"] = len(r["sub_sections"])
        rows.append(r)
    read = [r for r in rows if r["read_status"] == "CONNECTOR_TEXT_READ_IN_FULL"]
    modules = sorted({r["module_code"] for r in read})
    return dict(
        course="K3", course_title=A.K3_COURSE_TITLE, field_code=A.K3_FIELD_CODE,
        folder_id=A.K3_FOLDER_ID, pdfs=len(rows),
        read_in_full=len(read), read_pls=[r["pl"] for r in read],
        identified_not_read=len(rows) - len(read), not_read_pls=STILL_NOT_READ,
        read_budget_note=READ_BUDGET_NOTE,
        modules_evidenced=modules,
        module_map={m: sorted(r["pl"] for r in read if r["module_code"] == m)
                    for m in modules},
        module_finding=("The nine PDFs span six modules, every one of them read from the "
                        "package's own KOD MODUL front matter: M01 BUSINESS OPERATION "
                        "MANAGEMENT (PL01, PL02, PL03), M02 TENDERING MANAGEMENT (PL04), "
                        "M03 CONTRACT IMPLEMENTATION & MANAGEMENT (PL05), M04 PROJECT "
                        "PLANNING AND SCHEDULING (PL06), M05 CONSTRUCTION OPERATION "
                        "MANAGEMENT (PL07, PL08) and M06 PROJECT HANDOVER (PL09). Stage "
                        "4.2F-C recorded one module code from PL01 and PL03 alone; that is "
                        "now superseded by the full read."),
        every_read_package_has_own_assessment=all(r["latihan"] and r["skema_jawapan"]
                                                  for r in read),
        total_source_pages=sum(r["pages"] for r in read),
        total_source_questions=sum(r["latihan_questions"] for r in read),
        question_counts_all_agree=all(r["question_count_agrees"] for r in read),
        k5_rule_not_applied=K5_RULE_NOT_APPLIED,
        title_conflict=PL02_TITLE_INVESTIGATION,
        observations=[PL08_PAGE_MARKER_DEFECT, SKEMA_FORM_FINDING,
                      PAGE_MARKER_STYLE_FINDING],
        skema_form_finding=SKEMA_FORM_FINDING,
        rows=rows)


def k3_models():
    """Provisional models for every package read in full."""
    inv = k3_inventory()
    prev = {m["pl"]: m for m in INV.k3_models()}
    out = []
    for r in inv["rows"]:
        if r["read_status"] != "CONNECTOR_TEXT_READ_IN_FULL":
            continue
        if r["pl"] in prev:
            m = dict(prev[r["pl"]])
            # Stage 4.2F-C built these before the module code was known per package, so
            # their `source` block has no module fields. Fill them from the row rather
            # than leaving two model shapes for a consumer to branch on.
            m["source"] = dict(m["source"], module_code=r["module_code"],
                               module_title=r["module_title"])
            m["unit_id"] = f"K3-{r['module_code']}-{r['pl']}"
            m["skema_shape"] = r["skema_shape"]
            m["source_assessment"] = dict(m["source_assessment"],
                                          cls=K3_ASSESSMENT_CLASS)
            m["assessment_format_conflict"] = K3_COURSE_DECISION
            m["k5_rule_not_applied"] = K5_RULE_NOT_APPLIED
            out.append(m)
            continue
        groups = [dict(group_id=f"G{i + 1}", covers=s)
                  for i, s in enumerate(r["top_sections"])]
        shell, closing = 2, 3
        out.append(dict(
            course="K3", pl=r["pl"], unit_id=f"K3-{r['module_code']}-{r['pl']}",
            title=r["tajuk"], stage=STAGE, authority_inherited=AUTHORITY,
            source=dict(cls="SOURCE_DERIVED", pages=r["pages"],
                        module_code=r["module_code"], module_title=r["module_title"],
                        top_sections=len(r["top_sections"]),
                        sub_sections=len(r["sub_sections"]),
                        tables=r["tables"], figures=r["figures"],
                        drive_id=r["drive_id"]),
            body_content_boundary=dict(cls="SOURCE_DERIVED",
                                       starts_at="TAJUK", ends_at="SKEMA JAWAPAN",
                                       page_anchors=f"1/{r['pages']} to "
                                                    f"{r['pages']}/{r['pages']}",
                                       contiguous=True),
            heading_hierarchy=dict(cls="SOURCE_DERIVED",
                                   top=r["top_sections"], sub=r["sub_sections"],
                                   lettered_descendants=r["lettered_descendants"],
                                   lettered_note=r.get("lettered_note")),
            grouping=dict(cls="CAIR_PROPOSAL", basis="TOP_LEVEL_NUMBERED_SECTION",
                          groups=groups),
            screen_sequence=dict(cls="CAIR_PROPOSAL", arithmetic=dict(
                shell_screens=shell, content_groups=len(groups), closing_screens=closing,
                minimum_total_screens=shell + len(groups) + closing,
                maximum_total_screens="UNKNOWN_PENDING_PATTERN_DECISION")),
            pattern_family=dict(cls="PENDING_BARIAH_PATTERN_DECISION",
                                primary_candidate="click-to-reveal",
                                secondary_candidate="progressive process",
                                reason=("Numbered sections each fanning into sub-sections; "
                                        "PL05's contract lifecycle and PL02's approval "
                                        "chain both also read as sequences.")),
            interaction_candidates=dict(cls="CAIR_PROPOSAL",
                                        candidates=[dict(group_id=g["group_id"],
                                                         covers=g["covers"],
                                                         candidate="reveal per sub-section")
                                                    for g in groups]),
            dialogue=dict(cls="PENDING_UNIT_EXCEPTION_REVIEW", verdict="NOT_ASSESSED",
                          cast="NO_CHARACTER_PROPOSED_STOP_006_OPEN"),
            runtime_state_estimate=dict(cls="CAIR_PROPOSAL",
                                        base_states_floor=shell + len(groups) + closing,
                                        triggered_states="UNKNOWN_PENDING_PATTERN_DECISION",
                                        total_runtime_states=
                                        "UNKNOWN_PENDING_PATTERN_DECISION"),
            mandatory_content=dict(cls="SOURCE_DERIVED",
                                   named_authorities=r.get("named_authorities", []),
                                   compliance_heavy=r.get("compliance_heavy", False)),
            visual_subjects=dict(cls="SOURCE_DERIVED", count=r["figures"],
                                 source_attested=r["figures"],
                                 note=r.get("figure_note"),
                                 rule="RP-104 — read from the source's own figure"),
            skema_shape=r["skema_shape"],
            source_assessment=dict(cls=K3_ASSESSMENT_CLASS,
                                   questions=r["latihan_questions"],
                                   model_answers=r["skema_answers"],
                                   format=r["latihan_format"],
                                   shape=r["skema_shape"]["family"],
                                   carries_marks=r["skema_shape"]["carries_marks"],
                                   key_status="SOURCE_AUTHORED_NOT_STORYBOARD_APPROVED"),
            assessment_format_conflict=K3_COURSE_DECISION,
            k5_rule_not_applied=K5_RULE_NOT_APPLIED,
            rumusan=dict(cls="PENDING_UNIT_EXCEPTION_REVIEW",
                         beat_count="UNKNOWN_NOT_AUTHORED"),
            frozen_nothing=["screen count", "sequence", "dialogue", "Rumusan form",
                            "pattern family", "assessment key", "visual reuse"]))
    return out


if __name__ == "__main__":
    inv = k3_inventory()
    print(f"K3: {inv['pdfs']} PDFs, {inv['read_in_full']} read "
          f"({', '.join(inv['read_pls'])}), {inv['identified_not_read']} not read "
          f"({', '.join(inv['not_read_pls'])})")
    print("modules evidenced:", inv["modules_evidenced"])
    print("module map:", inv["module_map"])
    print("every read package has its own assessment:",
          inv["every_read_package_has_own_assessment"])
    print("question counts agree between shape and package records:",
          inv["question_counts_all_agree"])
    print(f"total source pages: {inv['total_source_pages']}, "
          f"total source questions: {inv['total_source_questions']}")
    print("SKEMA structural families:", inv["skema_form_finding"]
          ["not_uniform"]["structural_families"])
    t = inv["title_conflict"]
    print(f"\n{t['conflict_id']}: {t['classification']} — "
          f"instructional decision required: {t['requires_instructional_decision']}, "
          f"routed to {t['routed_to']}, in Bariah addendum: {t['in_bariah_addendum']}")
    print(f"models: {len(k3_models())}")
