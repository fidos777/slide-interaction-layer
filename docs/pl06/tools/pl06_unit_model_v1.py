# -*- coding: utf-8 -*-
"""Stage 4.2F-C Lanes 2-3 — analysis over the controlled extracts, and provisional models.

    python3 docs/pl06/tools/pl06_unit_model_v1.py

The extraction layer is verbatim and says nothing. This layer is where anything is claimed,
so every claim carries one of five classifications and nothing is frozen.

    SOURCE_DERIVED                    read off the extract, with the row IDs to check it
    CAIR_PROPOSAL                     ours; reject it freely
    COURSE_RULE_ALREADY_APPROVED      a rule that already applies course-wide
    PENDING_BARIAH_PATTERN_DECISION   waits on the pattern package now under review
    PENDING_UNIT_EXCEPTION_REVIEW     this unit does not fit the general shape

THE PATTERN PACKAGE IS NOT AUTHORITY
------------------------------------
K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2.docx is PENDING_BARIAH_REVIEW. Nothing here
reads it or applies a default from it. Screen count, sequence, dialogue, Rumusan form,
pattern family, assessment key and visual reuse are all left unfrozen on purpose, so that
when the package comes back these models can be projected rather than rewritten.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PL06 = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import pl06_extract_v1 as EX   # noqa: E402

STAGE = "4.2F-C"
AUTHORITY = "SRC-AUTH-01"

CLASSES = ["SOURCE_DERIVED", "CAIR_PROPOSAL", "COURSE_RULE_ALREADY_APPROVED",
           "PENDING_BARIAH_PATTERN_DECISION", "PENDING_UNIT_EXCEPTION_REVIEW"]

FROZEN_NOTHING = ["screen count", "sequence", "dialogue", "Rumusan form", "pattern family",
                  "assessment key", "visual reuse"]

PENDING_PACKAGE = "K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2.docx"

# SETTLED 2026-08-04 by A7 at K5 scope, and re-confirmed by F2(a) on 2026-08-05: the
# RP-009 / RP-010 VERIFY flags are no longer open.
# Course-wide rules already in force. Carried, not re-decided. RP-009 / RP-010 keep the
# VERIFY flag they have carried since the portability matrix.
COURSE_RULES = [
    dict(rule_id="AR-01", rule="4 Multiple Choice + 1 Multiple Response",
         flag="RP-009 human_authority_required = VERIFY"),
    dict(rule_id="AR-02", rule="60 percent pass threshold",
         flag="RP-010 human_authority_required = VERIFY"),
    dict(rule_id="AR-03",
         rule="no learner-facing 'dalam modul' / 'mengikut modul' / 'modul menyenaraikan'",
         flag=None),
    dict(rule_id="AR-04", rule="Multiple Response uses checkboxes, no A/B/C labels",
         flag=None),
    dict(rule_id="AR-05", rule="instructional clarity overrides production optimisation",
         flag=None),
    dict(rule_id="AR-06",
         rule=("supported treatment vocabulary: static content, click-to-reveal, "
               "progressive process, comparison, scenario/dialogue only where justified"),
         flag=None),
]
SUPPORTED_TREATMENTS = ["static content", "click-to-reveal", "progressive process",
                        "comparison", "scenario/dialogue only where justified"]

# ==========================================================================================
# HEADING STRUCTURE — the module styles bullets as Heading 3
#
# Stage 4.2F-B0 already found this in T04: most numbered paragraphs are Heading3 runs that
# Word numbered, not list items. It is worse in these four units, where whole sentences carry
# Heading3. A style-derived heading count is therefore not a heading count, and the criterion
# used to tell them apart is written down so it can be disagreed with.
STRUCTURAL_MAX_CHARS = 55
STRUCTURAL_CRITERION = (
    f"A Heading3 row counts as a structural heading when its text is at most "
    f"{STRUCTURAL_MAX_CHARS} characters and does not end in a full stop. Heading1 and "
    f"Heading2 always count. This is a CAIR reading of the module's styling, not a source "
    f"fact — the extract keeps the style verbatim either way, and every row the criterion "
    f"reclassifies is counted in the ambiguity register.")


def is_structural(row):
    t = (row["raw_source_text"] or "").strip()
    if row["content_type"] in ("HEADING_1", "HEADING_2"):
        return True
    if row["content_type"] != "HEADING_3":
        return False
    return len(t) <= STRUCTURAL_MAX_CHARS and not t.endswith(".")


def heading_tree(ex):
    out = []
    for r in ex["rows"]:
        if r["content_type"].startswith("HEADING") and is_structural(r):
            out.append(dict(row_id=r["row_id"], level=int(r["content_type"][-1]),
                            text=r["raw_source_text"], module_page=r["module_page"],
                            heading_path=r["heading_path"]))
    return out


def prose_styled_as_heading(ex):
    return [dict(row_id=r["row_id"], text=r["raw_source_text"][:120],
                 module_page=r["module_page"], style=r["paragraph_style"])
            for r in ex["rows"]
            if r["content_type"].startswith("HEADING") and not is_structural(r)]


# ==========================================================================================
# PER-UNIT ANALYSIS — hand-written, every claim citing rows
# ==========================================================================================
# Component structure that the module itself repeats. SOURCE_DERIVED: the marker headings
# ("Fungsi", "Fokus Utama Kontraktor") are the module's own, not ours.
COMPONENT_MARKERS = ["Fungsi", "Fokus Utama Kontraktor", "Fokus Utama Kontraktor:",
                     "Aspek Kritikal Kontraktor:"]


def components(ex):
    """A component is a level-3 heading followed by the module's own Fungsi/Fokus markers."""
    heads = [r for r in ex["rows"] if r["content_type"] == "HEADING_3" and is_structural(r)]
    texts = [h["raw_source_text"].strip() for h in heads]
    out, i = [], 0
    while i < len(texts):
        if texts[i] not in COMPONENT_MARKERS:
            nxt = texts[i + 1] if i + 1 < len(texts) else None
            if nxt in COMPONENT_MARKERS:
                out.append(dict(name=texts[i], row_id=heads[i]["row_id"],
                                module_page=heads[i]["module_page"],
                                marker=nxt))
        i += 1
    return out


UNIT_ANALYSIS = {
    # ---------------------------------------------------------------- T03-B03
    "K5-PL06-T03-B03": dict(
        mandatory_propositions=[
            dict(proposition="Busut tanah dibina berlapis, setiap lapisan tidak melebihi "
                             "300mm tebal, dan setiap lapisan dipadatkan.",
                 rows=["T03B03-ROW-013"], cls="SOURCE_DERIVED"),
            dict(proposition="Kecerunan busut dibentuk mengikut nisbah yang ditetapkan dalam "
                             "lukisan, contohnya 1:3.",
                 rows=["T03B03-ROW-015"], cls="SOURCE_DERIVED"),
            dict(proposition="Bahan timbus mesti bebas daripada sisa binaan, akar kayu dan "
                             "batu besar.",
                 rows=["T03B03-ROW-011"], cls="SOURCE_DERIVED"),
            dict(proposition="Dinding penahan mesti dibina mematuhi sepenuhnya lukisan "
                             "struktur jurutera bertauliah; tapak asas adalah komponen paling "
                             "kritikal.",
                 rows=["T03B03-ROW-037", "T03B03-ROW-039"], cls="SOURCE_DERIVED"),
            dict(proposition="Kegagalan dinding penahan selalunya berpunca daripada tekanan "
                             "air, jadi sistem perparitan di belakang dinding adalah wajib.",
                 rows=["T03B03-ROW-041"], cls="SOURCE_DERIVED"),
            dict(proposition="Jajaran pagar mesti ditanda mengikut Pelan Ukur Sempadan untuk "
                             "mengelakkan pencerobohan tanah.",
                 rows=["T03B03-ROW-048"], cls="SOURCE_DERIVED"),
            dict(proposition="Swale ialah parit cetek dan lebar yang ditanami tumbuhan, "
                             "alternatif kepada longkang konkrit, yang memperlahankan aliran "
                             "dan menggalakkan penyerapan.",
                 rows=["T03B03-ROW-056", "T03B03-ROW-058"], cls="SOURCE_DERIVED"),
            dict(proposition="Permukaan jalan akses dibina dengan kamber — kecerunan melintang "
                             "dari tengah ke tepi — supaya air tidak bertakung.",
                 rows=["T03B03-ROW-076"], cls="SOURCE_DERIVED"),
            dict(proposition="Sistem saliran bawah tanah mesti disambungkan ke saluran keluar "
                             "yang berfungsi.",
                 rows=["T03B03-ROW-031"], cls="SOURCE_DERIVED"),
        ],
        terminology=[
            dict(term="Setting Out / Penandaan Tapak", rows=["T03B03-ROW-008"]),
            dict(term="Sub soil drainage", rows=["T03B03-ROW-017"]),
            dict(term="Retaining Wall / Dinding Penahan", rows=["T03B03-ROW-032"]),
            dict(term="Swale / Natural Drain", rows=["T03B03-ROW-055"]),
            dict(term="Kerb / Bebendul", rows=["T03B03-ROW-071"]),
            dict(term="Camber / Kamber", rows=["T03B03-ROW-075"]),
        ],
        compliance_sensitive=[
            dict(statement="Dinding penahan mesti mematuhi lukisan struktur jurutera "
                           "bertauliah (Ir.) — a professional-liability boundary, not a "
                           "contractor preference.",
                 rows=["T03B03-ROW-037"], why="NAMED_PROFESSIONAL_AUTHORITY"),
            dict(statement="Jajaran pagar mengikut Pelan Ukur Sempadan — a land-encroachment "
                           "exposure.",
                 rows=["T03B03-ROW-048"], why="LEGAL_BOUNDARY_EXPOSURE"),
            dict(statement="Kemasan anti-karat tergalvani panas untuk komponen keluli.",
                 rows=["T03B03-ROW-054"], why="MATERIAL_SPECIFICATION"),
        ],
        assessment=[
            dict(stem="Apakah ketebalan maksimum setiap lapisan semasa membina busut tanah "
                      "(earthmound)?",
                 kind="MULTIPLE_CHOICE",
                 correct="Tidak melebihi 300mm setiap lapisan, dan setiap lapisan dipadatkan.",
                 correct_rows=["T03B03-ROW-013"],
                 distractors=["Tidak melebihi 600mm, dipadatkan sekali pada akhir",
                              "Tiada had ketebalan selagi jentera boleh memadat",
                              "Satu lapisan penuh sehingga ketinggian puncak"]),
            dict(stem="Mengapakah sistem perparitan di belakang dinding penahan adalah wajib?",
                 kind="MULTIPLE_CHOICE",
                 correct="Kerana kegagalan dinding penahan selalunya berpunca daripada "
                         "tekanan air (hydrostatic pressure).",
                 correct_rows=["T03B03-ROW-041"],
                 distractors=["Kerana ia mengurangkan kos konkrit dinding",
                              "Kerana ia diperlukan untuk kemasan estetik belakang dinding",
                              "Kerana ia menggantikan keperluan tapak asas"]),
            dict(stem="Pelan manakah yang menentukan jajaran pagar di tapak?",
                 kind="MULTIPLE_CHOICE",
                 correct="Pelan Ukur Sempadan.",
                 correct_rows=["T03B03-ROW-048"],
                 distractors=["Pelan Saliran", "Lukisan Struktur Jurutera",
                              "Pelan Susun Atur Tanaman"]),
            dict(stem="Apakah fungsi kamber (camber) pada permukaan jalan akses?",
                 kind="MULTIPLE_CHOICE",
                 correct="Memberikan kecerunan melintang dari tengah ke tepi supaya air "
                         "tidak bertakung di permukaan.",
                 correct_rows=["T03B03-ROW-076"],
                 distractors=["Menambah ketebalan lapisan permukaan di bahagian tengah",
                              "Menandakan sempadan jalan untuk pemandu",
                              "Menahan lapisan permukaan daripada bergerak ke tepi"]),
            dict(stem="Pilih SEMUA ciri yang menepati swale sebagai alternatif kepada "
                      "longkang konkrit.",
                 kind="MULTIPLE_RESPONSE",
                 correct=["Parit yang cetek dan lebar",
                          "Ditanami rumput atau tumbuhan tahan air",
                          "Memperlahankan aliran air larian permukaan",
                          "Menggalakkan penyerapan air ke dalam tanah"],
                 correct_rows=["T03B03-ROW-056", "T03B03-ROW-058", "T03B03-ROW-063"],
                 distractors=["Dilapisi konkrit di seluruh permukaannya",
                              "Direka untuk mempercepatkan aliran ke saluran keluar"]),
        ],
        visual_subjects=[
            dict(subject="Busut tanah berlapis 300mm dengan kecerunan 1:3",
                 rows=["T03B03-ROW-013", "T03B03-ROW-015"], has_source_figure=False),
            dict(subject="Keratan rentas dinding penahan dengan sistem perparitan di belakang",
                 rows=["T03B03-ROW-039", "T03B03-ROW-041"], has_source_figure=False),
            dict(subject="Keratan rentas swale bertanam",
                 rows=["T03B03-ROW-056", "T03B03-ROW-061"], has_source_figure=False),
            dict(subject="Susunan lapisan jalan akses: sub-base, bebendul, permukaan, kamber",
                 rows=["T03B03-ROW-070", "T03B03-ROW-072", "T03B03-ROW-074",
                       "T03B03-ROW-076"], has_source_figure=False),
        ],
        dialogue=dict(verdict="NOT_JUSTIFIED",
                      reason=("Six construction components, each with a function and a list "
                              "of contractor focus points. There is no decision, conflict or "
                              "judgement call in the source for a scenario to be about. "
                              "AR-06 allows a dialogue only where justified, and nothing here "
                              "justifies one.")),
        pattern=dict(primary="click-to-reveal", secondary="comparison",
                     reason=("Six parallel components with the same internal shape — Fungsi, "
                             "then Fokus Utama Kontraktor. That is the shape click-to-reveal "
                             "fits; comparison is the alternative if the six are better read "
                             "side by side than one at a time.")),
        rumusan_beats=[
            "Enam komponen infrastruktur landskap dan fungsi setiap satu.",
            "Titik kegagalan yang paling kerap bagi setiap komponen.",
            "Dokumen kawalan yang mengikat kontraktor: lukisan struktur, pelan ukur, "
            "pelan saliran.",
        ],
        ambiguities=[
            dict(item="The heading 'Fokus Utama Kontraktor' appears once per component but "
                      "twice with a trailing colon and once without, so a naive equality "
                      "match on the marker misses one component.",
                 rows=["T03B03-ROW-059"], resolution="COMPONENT_MARKERS lists both forms"),
            dict(item="Sub soil drainage carries an installation sequence introduced by "
                      "'Proses pemasangan yang betul adalah kunci kejayaan sistem ini:' but "
                      "the steps that follow are styled as headings, so their count is a "
                      "reading rather than a fact.",
                 rows=["T03B03-ROW-023"], resolution="PENDING_UNIT_EXCEPTION_REVIEW"),
        ]),

    # ---------------------------------------------------------------- T03-B04
    "K5-PL06-T03-B04": dict(
        # The automatic component detector under-reads this unit. It looks for a level-3
        # heading immediately followed by one of the module's own Fungsi / Fokus markers,
        # which is exactly how T03-B03 is written — and it finds all six components there.
        # T03-B04 is written differently: its five water-body types are named as headings and
        # only some carry a marker beneath. Rather than loosen the detector until it happens
        # to agree, the five types are listed here explicitly, the detector's own answer is
        # kept beside it, and the divergence is reported.
        grouping_override=dict(
            reason=("automatic component detection found 2 of 5 water-body types, because "
                    "this unit does not repeat the Fungsi / Fokus marker under every type"),
            groups=[dict(covers="Kolam", row_id="T03B04-ROW-003"),
                    dict(covers="Tasik", row_id="T03B04-ROW-011"),
                    dict(covers="Tali Air (Canal)", row_id="T03B04-ROW-022"),
                    dict(covers="Alur Air", row_id="T03B04-ROW-034"),
                    dict(covers="Sungai", row_id="T03B04-ROW-063")]),
        mandatory_propositions=[
            dict(proposition="Kolam ikan hiasan (koi pond) memerlukan sistem penapisan yang "
                             "efisien.",
                 rows=["T03B04-ROW-006"], cls="SOURCE_DERIVED"),
            dict(proposition="Kolam reflektif biasanya cetek dengan permukaan air tenang, "
                             "direka untuk memantulkan imej.",
                 rows=["T03B04-ROW-008"], cls="SOURCE_DERIVED"),
            dict(proposition="Kecerunan alur air adalah aspek paling kritikal — ia mengawal "
                             "kelajuan aliran.",
                 rows=["T03B04-ROW-039"], cls="SOURCE_DERIVED"),
            dict(proposition="Pelapik fleksibel EPDM atau PVC adalah pilihan utama kerana "
                             "mudah dibentuk mengikut kontur; konkrit kurang fleksibel dan "
                             "digunakan untuk alur formal.",
                 rows=["T03B04-ROW-044", "T03B04-ROW-046"], cls="SOURCE_DERIVED"),
            dict(proposition="Sistem kitaran air adalah kitaran tertutup: air yang sama "
                             "digunakan berterusan.",
                 rows=["T03B04-ROW-080"], cls="SOURCE_DERIVED"),
            dict(proposition="Pam ialah 'jantung' sistem, dan saiznya mesti sepadan dengan "
                             "ketinggian (head height) dan kadar aliran.",
                 rows=["T03B04-ROW-053", "T03B04-ROW-085"], cls="SOURCE_DERIVED"),
            dict(proposition="Bentuk berliku-liku, bukan laluan lurus, adalah kunci rupa "
                             "bentuk semula jadi sungai buatan.",
                 rows=["T03B04-ROW-071"], cls="SOURCE_DERIVED"),
            dict(proposition="Kecerunan yang terlalu curam menyebabkan hakisan; terlalu "
                             "landai menyebabkan air bertakung.",
                 rows=["T03B04-ROW-069"], cls="SOURCE_DERIVED"),
        ],
        terminology=[
            dict(term="Koi Pond / Kolam Ikan Hiasan", rows=["T03B04-ROW-005"]),
            dict(term="Reflecting Pool / Kolam Reflektif", rows=["T03B04-ROW-007"]),
            dict(term="Canal / Tali Air", rows=["T03B04-ROW-022"]),
            dict(term="Lining System / Sistem Pelapisan", rows=["T03B04-ROW-042"]),
            dict(term="Header pool / takungan tersembunyi", rows=["T03B04-ROW-049"]),
            dict(term="Sump / Takungan Bawah", rows=["T03B04-ROW-050"]),
            dict(term="Head height", rows=["T03B04-ROW-053"]),
        ],
        compliance_sensitive=[
            dict(statement="Pam mesti dipadankan dengan head height dan kadar aliran — an "
                           "undersized pump is a specification failure, not a preference.",
                 rows=["T03B04-ROW-053", "T03B04-ROW-085"], why="MATERIAL_SPECIFICATION"),
            dict(statement="Lapisan pelindung (underlayment) di bawah pelapik fleksibel.",
                 rows=["T03B04-ROW-076"], why="MATERIAL_SPECIFICATION"),
        ],
        assessment=[
            dict(stem="Apakah aspek paling kritikal dalam pembinaan alur air?",
                 kind="MULTIPLE_CHOICE",
                 correct="Kecerunan, kerana ia mengawal kelajuan aliran air.",
                 correct_rows=["T03B04-ROW-039"],
                 distractors=["Warna batu yang digunakan di tebing",
                              "Jenis tumbuhan yang ditanam di sepanjang alur",
                              "Kedalaman takungan bawah"]),
            dict(stem="Mengapakah pelapik fleksibel seperti EPDM atau PVC menjadi pilihan "
                      "utama bagi alur air?",
                 kind="MULTIPLE_CHOICE",
                 correct="Kerana ia mudah dibentuk mengikut kontur alur.",
                 correct_rows=["T03B04-ROW-044"],
                 distractors=["Kerana ia lebih murah daripada semua bahan lain",
                              "Kerana ia tidak memerlukan lapisan pelindung",
                              "Kerana ia lebih kukuh daripada konkrit"]),
            dict(stem="Bagaimanakah sistem kitaran air bagi sungai buatan berfungsi?",
                 kind="MULTIPLE_CHOICE",
                 correct="Sebagai kitaran tertutup — air yang sama digunakan berterusan.",
                 correct_rows=["T03B04-ROW-080"],
                 distractors=["Air baharu dibekalkan berterusan dari sumber bandar",
                              "Air dilepaskan ke longkang selepas setiap kitaran",
                              "Air hanya dipam semasa waktu operasi taman"]),
            dict(stem="Apakah kesan kecerunan yang terlalu landai pada laluan aliran sungai "
                      "buatan?",
                 kind="MULTIPLE_CHOICE",
                 correct="Air bertakung.",
                 correct_rows=["T03B04-ROW-069"],
                 distractors=["Hakisan tebing yang berlebihan",
                              "Aliran menjadi terlalu laju",
                              "Pam bekerja pada kadar yang lebih rendah"]),
            dict(stem="Pilih SEMUA komponen yang membentuk sistem kitaran air.",
                 kind="MULTIPLE_RESPONSE",
                 correct=["Punca air di titik tertinggi",
                          "Takungan bawah (sump) di titik terendah",
                          "Pam air",
                          "Sistem perpaipan"],
                 correct_rows=["T03B04-ROW-049", "T03B04-ROW-051", "T03B04-ROW-053",
                               "T03B04-ROW-055"],
                 distractors=["Bebendul konkrit di tepi alur",
                              "Sistem penapisan wajib untuk semua badan air"]),
        ],
        visual_subjects=[
            dict(subject="Empat jenis kolam landskap: koi, reflektif, taman air, tasik",
                 rows=["T03B04-ROW-005", "T03B04-ROW-007", "T03B04-ROW-009",
                       "T03B04-ROW-011"], has_source_figure=False),
            dict(subject="Rajah kitaran air tertutup: punca air, sump, pam, perpaipan",
                 rows=["T03B04-ROW-049", "T03B04-ROW-051", "T03B04-ROW-053",
                       "T03B04-ROW-055"], has_source_figure=False),
            dict(subject="Perbandingan pelapik fleksibel dan pelapik konkrit",
                 rows=["T03B04-ROW-044", "T03B04-ROW-046"], has_source_figure=False),
        ],
        dialogue=dict(verdict="NOT_JUSTIFIED",
                      reason=("Component description again, with a technical system inside "
                              "it. The batch 1 harvest package proposed NOT_REQUIRED for this "
                              "unit from the heading alone; the extract confirms it rather "
                              "than overturning it.")),
        pattern=dict(primary="progressive process", secondary="click-to-reveal",
                     reason=("The water-circulation system is a genuine sequence — source, "
                             "sump, pump, pipework, back to source — and reads as a process. "
                             "The pond and canal types around it are click-to-reveal.")),
        rumusan_beats=[
            "Jenis badan air dan fungsi reka bentuk setiap satu.",
            "Sistem kitaran air tertutup dan peranan pam sebagai jantung sistem.",
            "Kawalan kecerunan dan pilihan pelapik sebagai dua titik kegagalan utama.",
        ],
        ambiguities=[
            dict(item="'Sistem Pelapisan (Lining System)' appears twice as a structural "
                      "heading, once under Alur Air and once under Sungai, with different "
                      "content beneath each.",
                 rows=["T03B04-ROW-042"], resolution="Both retained; heading_path "
                                                     "disambiguates them"),
            dict(item="The pump description is repeated almost verbatim for Alur Air and for "
                      "Sungai. Whether that is one teaching point or two is an instructional "
                      "judgement.",
                 rows=["T03B04-ROW-053", "T03B04-ROW-085"],
                 resolution="PENDING_UNIT_EXCEPTION_REVIEW"),
        ]),

    # ---------------------------------------------------------------- T05-B01
    "K5-PL06-T05-B01": dict(
        mandatory_propositions=[
            dict(proposition="Dokumen kontrak adalah sumber rujukan kualiti yang paling utama "
                             "dan mengatasi semua sumber lain.",
                 rows=["T05B01-ROW-041"], cls="SOURCE_DERIVED"),
            dict(proposition="QA ialah proses proaktif untuk memberi keyakinan bahawa kualiti "
                             "akan dicapai; QC ialah aspek praktikal yang mengesan kecacatan.",
                 rows=["T05B01-ROW-038", "T05B01-ROW-056", "T05B01-ROW-057"],
                 cls="SOURCE_DERIVED"),
            dict(proposition="ITP menyenaraikan setiap aktiviti kerja dan peringkat "
                             "pemeriksaan, dan menetapkan kriteria penerimaan yang jelas.",
                 rows=["T05B01-ROW-059", "T05B01-ROW-066"], cls="SOURCE_DERIVED"),
            dict(proposition="Aliran kerja NCR mempunyai lima peringkat: pengenalpastian, "
                             "pengeluaran NCR, analisis punca dan cadangan pembetulan, "
                             "kelulusan, pelaksanaan.",
                 rows=["T05B01-ROW-082", "T05B01-ROW-084", "T05B01-ROW-086",
                       "T05B01-ROW-088", "T05B01-ROW-090"], cls="SOURCE_DERIVED"),
            dict(proposition="Objektif kualiti mesti jelas, spesifik dan boleh diukur "
                             "(measurable).",
                 rows=["T05B01-ROW-006"], cls="SOURCE_DERIVED"),
            dict(proposition="Sampel dan mock-up yang diluluskan menjadi piawaian fizikal di "
                             "tapak dan rujukan utama untuk semua kerja seterusnya.",
                 rows=["T05B01-ROW-053", "T05B01-ROW-054"], cls="SOURCE_DERIVED"),
            dict(proposition="Penyata Kaedah Kerja mesti disertakan dengan pelan HSE yang "
                             "mengenal pasti bahaya dalam jujukan kerja dan langkah "
                             "kawalannya.",
                 rows=["T05B01-ROW-119", "T05B01-ROW-121"], cls="SOURCE_DERIVED"),
            dict(proposition="Penyata Kaedah Kerja adalah keperluan mandatori dalam "
                             "kebanyakan dokumen kontrak pembinaan.",
                 rows=["T05B01-ROW-104"], cls="SOURCE_DERIVED"),
        ],
        terminology=[
            dict(term="PQP — Project Quality Plan / Pelan Kualiti Projek",
                 rows=["T05B01-ROW-004"]),
            dict(term="ITP — Inspection and Test Plan", rows=["T05B01-ROW-020"]),
            dict(term="NCR — Non-Conformance Report", rows=["T05B01-ROW-036"]),
            dict(term="QA — Jaminan Kualiti", rows=["T05B01-ROW-038"]),
            dict(term="QC — Quality Control / Kawalan Kualiti", rows=["T05B01-ROW-056"]),
            dict(term="Method Statement / Penyata Kaedah Kerja", rows=["T05B01-ROW-092"]),
            dict(term="HSE — Health, Safety & Environment", rows=["T05B01-ROW-119"]),
            dict(term="PPE", rows=["T05B01-ROW-123"]),
        ],
        compliance_sensitive=[
            dict(statement="Piawaian Malaysia (MS) dan JKR Standard Specification for Road "
                           "Works are named standards.",
                 rows=["T05B01-ROW-046", "T05B01-ROW-047"], why="NAMED_EXTERNAL_STANDARD"),
            dict(statement="PBT and ILAM guidelines are named authority bodies.",
                 rows=["T05B01-ROW-050", "T05B01-ROW-051"], why="NAMED_AUTHORITY_BODY"),
            dict(statement="Method Statement as a mandatory contract requirement.",
                 rows=["T05B01-ROW-104"], why="CONTRACTUAL_OBLIGATION"),
            dict(statement="PPE obligations named for all involved workers.",
                 rows=["T05B01-ROW-123"], why="STATUTORY_SAFETY_EXPOSURE"),
        ],
        assessment=[
            dict(stem="Dalam hierarki rujukan kualiti, dokumen manakah yang mengatasi semua "
                      "sumber lain?",
                 kind="MULTIPLE_CHOICE",
                 correct="Dokumen kontrak.",
                 correct_rows=["T05B01-ROW-041"],
                 distractors=["Piawaian Malaysia (MS)",
                              "Garis panduan Pihak Berkuasa Tempatan (PBT)",
                              "Garis panduan ILAM"]),
            dict(stem="Apakah perbezaan utama antara Jaminan Kualiti (QA) dan Kawalan Kualiti "
                      "(QC)?",
                 kind="MULTIPLE_CHOICE",
                 correct="QA ialah proses proaktif untuk memberi keyakinan bahawa kualiti "
                         "akan dicapai; QC ialah aspek praktikal yang mengesan kecacatan.",
                 correct_rows=["T05B01-ROW-038", "T05B01-ROW-056", "T05B01-ROW-057"],
                 distractors=["QA dijalankan oleh kontraktor, QC oleh perunding sahaja",
                              "QA hanya untuk bahan, QC hanya untuk kerja tapak",
                              "QA dilakukan selepas siap, QC sebelum kerja bermula"]),
            dict(stem="Apakah langkah PERTAMA dalam proses aliran kerja NCR?",
                 kind="MULTIPLE_CHOICE",
                 correct="Pengenalpastian ketidakpatuhan oleh penyelia tapak atau perunding "
                         "semasa pemeriksaan.",
                 correct_rows=["T05B01-ROW-082"],
                 distractors=["Kelulusan cadangan pembetulan oleh perunding",
                              "Pelaksanaan kerja pembaikan oleh kontraktor",
                              "Analisis punca masalah oleh kontraktor"]),
            dict(stem="Objektif kualiti dalam PQP mesti mempunyai satu ciri yang membezakannya "
                      "daripada kenyataan hasrat. Apakah ciri itu?",
                 kind="MULTIPLE_CHOICE",
                 correct="Ia mesti boleh diukur (measurable).",
                 correct_rows=["T05B01-ROW-006"],
                 distractors=["Ia mesti diluluskan oleh PBT",
                              "Ia mesti ditulis dalam dua bahasa",
                              "Ia mesti disertakan dengan anggaran kos"]),
            dict(stem="Pilih SEMUA tujuan utama Pelan Pemeriksaan dan Ujian (ITP).",
                 kind="MULTIPLE_RESPONSE",
                 correct=["Memastikan tiada peringkat kritikal tertinggal",
                          "Mengklarifikasi tanggungjawab pemeriksaan dan kelulusan",
                          "Menjadi rujukan standard dengan kriteria penerimaan yang jelas",
                          "Mewujudkan rekod formal bahawa pemeriksaan telah dijalankan"],
                 correct_rows=["T05B01-ROW-062", "T05B01-ROW-064", "T05B01-ROW-066",
                               "T05B01-ROW-068"],
                 distractors=["Menetapkan harga kontrak bagi setiap aktiviti kerja",
                              "Menggantikan keperluan Penyata Kaedah Kerja"]),
        ],
        visual_subjects=[
            dict(subject="Hierarki rujukan kualiti: dokumen kontrak di atas, kemudian MS/JKR, "
                         "PBT/ILAM, sampel dan mock-up",
                 rows=["T05B01-ROW-041", "T05B01-ROW-046", "T05B01-ROW-050",
                       "T05B01-ROW-053"], has_source_figure=False),
            dict(subject="Aliran kerja NCR lima peringkat",
                 rows=["T05B01-ROW-082", "T05B01-ROW-084", "T05B01-ROW-086",
                       "T05B01-ROW-088", "T05B01-ROW-090"], has_source_figure=False),
            dict(subject="Kandungan Penyata Kaedah Kerja yang lengkap",
                 rows=["T05B01-ROW-112", "T05B01-ROW-114", "T05B01-ROW-116",
                       "T05B01-ROW-119"], has_source_figure=False),
        ],
        dialogue=dict(verdict="JUSTIFIED",
                      reason=("The NCR workflow is a five-party sequence — supervisor finds "
                              "it, contractor investigates, consultant approves, contractor "
                              "repairs — and quality management is exactly where a "
                              "contractor's habits meet the specification. That is a decision "
                              "with stakes, which is what AR-06 means by justified. The "
                              "batch 1 package proposed REQUIRED from the heading; the "
                              "extract supports it.")),
        pattern=dict(primary="progressive process", secondary="comparison",
                     reason=("Two genuine sequences — the NCR workflow and the ITP inspection "
                             "stages. Comparison carries the QA-versus-QC distinction, which "
                             "is a contrast rather than a sequence.")),
        rumusan_beats=[
            "PQP sebagai dokumen induk kualiti dan empat komponennya.",
            "Hierarki rujukan: dokumen kontrak mengatasi semua sumber lain.",
            "QA proaktif berbanding QC yang mengesan kecacatan.",
            "NCR sebagai rekod formal, dan lima peringkat aliran kerjanya.",
            "Penyata Kaedah Kerja sebagai keperluan kontrak, lengkap dengan pelan HSE.",
        ],
        ambiguities=[
            dict(item="'Contoh dalam Landskap:' appears twice as a structural heading under "
                      "PQP with different examples beneath each.",
                 rows=["T05B01-ROW-007", "T05B01-ROW-013"],
                 resolution="Both retained; heading_path disambiguates them"),
            dict(item="The ITP example table for tree planting is described in prose "
                      "('Contoh ITP untuk Kerja Penanaman Pokok Teduhan:') but the extract "
                      "found no table object in this unit, so the example is text only.",
                 rows=["T05B01-ROW-026"], resolution="MISSING_SOURCE_REGISTER"),
        ]),

    # ---------------------------------------------------------------- T06-B01
    "K5-PL06-T06-B01": dict(
        mandatory_propositions=[
            dict(proposition="EMP bermula dengan mengenal pasti potensi impak negatif dan "
                             "positif projek terhadap alam sekitar.",
                 rows=["T06B01-ROW-005"], cls="SOURCE_DERIVED"),
            dict(proposition="EMP merangka langkah pencegahan, mitigasi dan pemulihan, dan "
                             "menetapkan prosedur pemantauan, pelaporan dan tindakan "
                             "pembetulan.",
                 rows=["T06B01-ROW-006", "T06B01-ROW-007"], cls="SOURCE_DERIVED"),
            dict(proposition="Pengurusan alam sekitar meliputi enam aspek: air, udara, bunyi, "
                             "getaran, bau, serta flora dan fauna.",
                 rows=["T06B01-ROW-023", "T06B01-ROW-041", "T06B01-ROW-059",
                       "T06B01-ROW-072", "T06B01-ROW-083", "T06B01-ROW-094"],
                 cls="SOURCE_DERIVED"),
            dict(proposition="Air bilasan pencampuran konkrit mesti dikumpul dalam tangki "
                             "atau kawasan tadahan khusus, bukan dilepaskan terus.",
                 rows=["T06B01-ROW-038"], cls="SOURCE_DERIVED"),
            dict(proposition="Lori yang membawa tanah atau bahan binaan mesti ditutup dengan "
                             "kanvas untuk mengelakkan habuk bertebaran.",
                 rows=["T06B01-ROW-051"], cls="SOURCE_DERIVED"),
            dict(proposition="Pemangkasan pokok yang dikekalkan mesti dilakukan oleh arborist "
                             "bertauliah.",
                 rows=["T06B01-ROW-104"], cls="SOURCE_DERIVED"),
            dict(proposition="Sisa tapak tidak boleh dibakar kerana ia memusnahkan habitat "
                             "dan mengancam hidupan liar.",
                 rows=["T06B01-ROW-118"], cls="SOURCE_DERIVED"),
            dict(proposition="Kerja bising dijadualkan pada waktu yang kurang sensitif, dan "
                             "kerja bising dielakkan semasa musim pembiakan haiwan.",
                 rows=["T06B01-ROW-069", "T06B01-ROW-116"], cls="SOURCE_DERIVED"),
        ],
        terminology=[
            dict(term="EMP — Environmental Management Plan", rows=["T06B01-ROW-004"]),
            dict(term="Silt fence / halangan geotekstil", rows=["T06B01-ROW-031"]),
            dict(term="Kolam takungan sedimen", rows=["T06B01-ROW-033"]),
            dict(term="Noise barrier / pembatas bunyi", rows=["T06B01-ROW-067"]),
            dict(term="Translokasi spesies", rows=["T06B01-ROW-106"]),
            dict(term="Native species / spesies asli", rows=["T06B01-ROW-109"]),
        ],
        compliance_sensitive=[
            dict(statement="Pematuhan kepada had bunyi yang ditetapkan oleh pihak berkuasa.",
                 rows=["T06B01-ROW-062"], why="STATUTORY_LIMIT"),
            dict(statement="Spesies tumbuhan yang dilindungi may require translocation before "
                           "development proceeds.",
                 rows=["T06B01-ROW-106"], why="PROTECTED_SPECIES_EXPOSURE"),
            dict(statement="Tiada pembakaran sisa tapak.",
                 rows=["T06B01-ROW-118"], why="ENVIRONMENTAL_PROHIBITION"),
            dict(statement="Pemangkasan oleh arborist bertauliah — a named professional "
                           "competency.",
                 rows=["T06B01-ROW-104"], why="NAMED_PROFESSIONAL_AUTHORITY"),
        ],
        assessment=[
            dict(stem="Apakah langkah PERTAMA dalam Environmental Management Plan (EMP)?",
                 kind="MULTIPLE_CHOICE",
                 correct="Mengenal pasti potensi impak negatif dan positif projek terhadap "
                         "alam sekitar.",
                 correct_rows=["T06B01-ROW-005"],
                 distractors=["Merangka pelan pemulihan kawasan yang terganggu",
                              "Menetapkan prosedur pemantauan dan pelaporan",
                              "Memasang pagar perlindungan pokok"]),
            dict(stem="Bagaimanakah air bilasan daripada pencampuran konkrit mesti diuruskan?",
                 kind="MULTIPLE_CHOICE",
                 correct="Dikumpul dalam tangki atau kawasan tadahan khusus.",
                 correct_rows=["T06B01-ROW-038"],
                 distractors=["Dilepaskan terus ke sistem saliran tapak",
                              "Disembur ke kawasan tanah kosong untuk mengurangkan habuk",
                              "Dibiarkan meresap ke dalam tanah di sekitar tapak"]),
            dict(stem="Siapakah yang perlu melakukan pemangkasan pokok matang yang dikekalkan "
                      "di tapak?",
                 kind="MULTIPLE_CHOICE",
                 correct="Arborist bertauliah.",
                 correct_rows=["T06B01-ROW-104"],
                 distractors=["Mana-mana pekerja am yang berpengalaman",
                              "Penyelia tapak kontraktor",
                              "Pengendali jentera yang memasang pagar perlindungan"]),
            dict(stem="Mengapakah pembakaran sisa tapak dilarang?",
                 kind="MULTIPLE_CHOICE",
                 correct="Kerana ia boleh memusnahkan habitat atau mengancam hidupan liar.",
                 correct_rows=["T06B01-ROW-118"],
                 distractors=["Kerana ia meningkatkan kos pelupusan sisa",
                              "Kerana ia memerlukan kelulusan bertulis daripada perunding",
                              "Kerana abu sisa merosakkan lapisan pelapik kolam"]),
            dict(stem="Pilih SEMUA langkah kawalan habuk yang dinyatakan bagi pengurusan "
                      "kualiti udara.",
                 kind="MULTIPLE_RESPONSE",
                 correct=["Menyiram air secara berkala di laluan kenderaan dan kawasan kerja",
                          "Menutup lori pembawa tanah dengan kanvas",
                          "Memasang jaring debu di sekeliling kawasan kerja"],
                 correct_rows=["T06B01-ROW-049", "T06B01-ROW-051", "T06B01-ROW-053"],
                 distractors=["Memasang pembatas bunyi di sempadan tapak",
                              "Menggunakan sistem pengairan titisan",
                              "Memasang monitor getaran berhampiran struktur kritikal"]),
        ],
        visual_subjects=[
            dict(subject="Rajah 26: EMP Untuk Landskap",
                 rows=["T06B01-ROW-010"], has_source_figure=True,
                 note="The only unit in this batch with a raster figure in the source, and "
                      "it carries its own caption."),
            dict(subject="Enam aspek pengurusan alam sekitar dan contoh kawalan bagi setiap "
                         "satu",
                 rows=["T06B01-ROW-023", "T06B01-ROW-041", "T06B01-ROW-059",
                       "T06B01-ROW-072", "T06B01-ROW-083", "T06B01-ROW-094"],
                 has_source_figure=False),
            dict(subject="Kawalan hakisan dan sedimen: silt fence, kolam takungan, penanaman "
                         "penutup bumi",
                 rows=["T06B01-ROW-031", "T06B01-ROW-033", "T06B01-ROW-035"],
                 has_source_figure=False),
        ],
        dialogue=dict(verdict="UNCERTAIN",
                      reason=("'Contoh Aplikasi dalam Landskap' walks through one public-park "
                              "project across four EMP stages, which is scenario-shaped. But "
                              "the rest of the unit is a control catalogue, and whether one "
                              "worked example earns a dialogue is an instructional judgement "
                              "this run will not make. The batch 1 package also said "
                              "UNCERTAIN; the extract does not settle it either way.")),
        pattern=dict(primary="click-to-reveal", secondary="progressive process",
                     reason=("Six environmental aspects, each with its own control list — "
                             "click-to-reveal. The EMP itself is a four-stage process and "
                             "reads as one.")),
        rumusan_beats=[
            "EMP sebagai dokumen strategik dan empat peringkatnya.",
            "Enam aspek pengurusan alam sekitar di tapak landskap.",
            "Kawalan yang paling kerap diperlukan bagi setiap aspek.",
            "Perlindungan flora dan fauna, termasuk larangan pembakaran sisa.",
        ],
        ambiguities=[
            dict(item="'Contoh' appears as a bare structural heading six times, once per "
                      "environmental aspect, with different examples beneath each.",
                 rows=["T06B01-ROW-028", "T06B01-ROW-046", "T06B01-ROW-063",
                       "T06B01-ROW-076", "T06B01-ROW-087", "T06B01-ROW-099"],
                 resolution="Both retained; heading_path disambiguates them"),
            dict(item="'Perlindungan Poko Sedia Ada:' is misspelled in the source — 'Poko' "
                      "for 'Pokok'.",
                 rows=["T06B01-ROW-101"],
                 resolution="RECORDED_NOT_SILENTLY_CORRECTED"),
        ]),
}


# ==========================================================================================
def missing_source(ex, analysis):
    """What a storyboard will need and the source does not supply."""
    out = []
    if ex["totals"]["raster_images"] == 0:
        out.append(dict(item="No figure or photograph in this unit's source span.",
                        consequence="Every visual subject below is a CAIR reading of the "
                                    "text. None is a source-attested figure, and RP-104 "
                                    "forbids composing a subject from a component name.",
                        severity="BLOCKS_VISUAL_DIRECTION"))
    if ex["totals"]["tables"] == 0:
        out.append(dict(item="No table object in this unit's source span.",
                        consequence="Any comparison treatment must be built from prose, not "
                                    "lifted from a source table.",
                        severity="AFFECTS_TREATMENT_CHOICE"))
    for a in analysis["ambiguities"]:
        if a.get("resolution") == "MISSING_SOURCE_REGISTER":
            out.append(dict(item=a["item"], consequence="Recorded, not filled in.",
                            severity="RECORDED"))
    return out


def extraction_qa(ex):
    rows = ex["rows"]
    pages = [r["module_page"] for r in rows]
    idx = [r["source_paragraph_start"] for r in rows
           if r["source_paragraph_start"] is not None]
    bp = ex["boundary_proof"]
    return dict(
        unit_id=ex["unit_id"],
        rows=len(rows),
        every_row_has_a_row_id=all(r["row_id"] for r in rows),
        row_ids_unique=len({r["row_id"] for r in rows}) == len(rows),
        every_row_carries_the_unit_id=all(r["unit_id"] == ex["unit_id"] for r in rows),
        sequence_is_contiguous=[r["sequence"] for r in rows] == list(range(1, len(rows) + 1)),
        pages_monotonic=all(b >= a for a, b in zip(pages, pages[1:])),
        page_range=[min(pages), max(pages)] if pages else None,
        page_range_matches_frozen=(([min(pages), max(pages)]
                                    == ex["boundary"]["module_pages"]) if pages else False),
        paragraph_indices_monotonic=all(b >= a for a, b in zip(idx, idx[1:])),
        paragraph_indices_inside_span=all(
            bp["first_included_paragraph_index"] <= i <= bp["last_included_paragraph_index"]
            for i in idx),
        typeset_attributed_rows=sum(1 for r in rows
                                    if r.get("module_page_basis") == "TYPESET_PDF_FOOTER"),
        carried_forward_rows=sum(
            1 for r in rows
            if r.get("module_page_basis") == "CARRIED_FORWARD_FROM_PREVIOUS_ROW"),
        anchors_resolved=ex["boundary"]["anchor_search"]["frozen_start_is_a_hit"]
        and ex["boundary"]["anchor_search"]["frozen_stop_is_a_hit"],
        extraction_method=ex["boundary"]["extraction_method"])


def model(unit_id, ex):
    a = UNIT_ANALYSIS[unit_id]
    tree = heading_tree(ex)
    comps = components(ex)
    h2 = [h for h in tree if h["level"] == 2]
    # Grouping: one group per level-2 heading where the unit has them, otherwise one per
    # component the module itself repeats.
    override = a.get("grouping_override")
    if override:
        groups = [dict(group_id=f"G{i + 1}", covers=g["covers"], row_id=g["row_id"],
                       basis="DECLARED_OVERRIDE")
                  for i, g in enumerate(override["groups"])]
        basis = "DECLARED_OVERRIDE"
    elif len(h2) > 1:
        groups = [dict(group_id=f"G{i + 1}", covers=h["text"], row_id=h["row_id"],
                       basis="LEVEL_2_HEADING") for i, h in enumerate(h2)]
        basis = "LEVEL_2_HEADING"
    else:
        groups = [dict(group_id=f"G{i + 1}", covers=c["name"], row_id=c["row_id"],
                       basis="MODULE_REPEATED_COMPONENT_BLOCK")
                  for i, c in enumerate(comps)]
        basis = "MODULE_REPEATED_COMPONENT_BLOCK"

    dialogue_used = a["dialogue"]["verdict"] == "JUSTIFIED"
    shell = 2 + (1 if dialogue_used else 0)
    closing = 3
    seq = (["S01 Topik entry"] + (["S02 Dialog"] if dialogue_used else [])
           + ["S0x Orientasi"] + [f"{g['group_id']}: {g['covers']}" for g in groups]
           + ["Rumusan", "Kuiz", "Tamat"])
    return dict(
        unit_id=unit_id, lesson_title=ex["lesson_title"], stage=STAGE,
        authority_inherited=AUTHORITY,
        pending_pattern_package=PENDING_PACKAGE,
        frozen_nothing=FROZEN_NOTHING,
        heading_tree=dict(cls="SOURCE_DERIVED", criterion=STRUCTURAL_CRITERION,
                          structural_headings=len(tree), tree=tree),
        prose_styled_as_heading=dict(cls="SOURCE_DERIVED",
                                     count=len(prose_styled_as_heading(ex)),
                                     rows=prose_styled_as_heading(ex)),
        components=dict(cls="SOURCE_DERIVED", count=len(comps), components=comps),
        grouping=dict(cls="CAIR_PROPOSAL", basis=basis, groups=groups,
                      automatic_component_detection=[c["name"] for c in comps],
                      override_declared=bool(override),
                      override_reason=override["reason"] if override else None,
                      note="A floor, not a ceiling. Extraction shows what exists; how many "
                           "screens each group needs is not settled here. Where a declared "
                           "override is used, the automatic detector's own answer is kept "
                           "beside it so the two can be compared."),
        screen_sequence=dict(cls="CAIR_PROPOSAL", sequence=seq,
                             arithmetic=dict(
                                 shell_screens=shell, shell_includes_dialogue=dialogue_used,
                                 content_groups=len(groups), closing_screens=closing,
                                 minimum_total_screens=shell + len(groups) + closing,
                                 maximum_total_screens="UNKNOWN_PENDING_PATTERN_DECISION",
                                 basis="one content screen per proposed group — a floor")),
        pattern_family=dict(cls="PENDING_BARIAH_PATTERN_DECISION",
                            primary_candidate=a["pattern"]["primary"],
                            secondary_candidate=a["pattern"]["secondary"],
                            reason=a["pattern"]["reason"],
                            vocabulary=SUPPORTED_TREATMENTS,
                            note="Named as candidates only. The pattern package that would "
                                 "settle this is still with Bariah."),
        interaction_candidates=dict(
            cls="CAIR_PROPOSAL",
            candidates=[dict(group_id=g["group_id"], covers=g["covers"],
                             candidate="reveal per component detail")
                        for g in groups],
            note="Interaction shape follows the pattern family, which is undecided."),
        runtime_state_estimate=dict(
            cls="CAIR_PROPOSAL",
            base_states_floor=shell + len(groups) + closing,
            triggered_states="UNKNOWN_PENDING_PATTERN_DECISION",
            total_runtime_states="UNKNOWN_PENDING_PATTERN_DECISION",
            method="base states = learner screens; triggered states depend on the pattern "
                   "family, which is undecided",
            note="T04's 65 states are not carried over."),
        rumusan=dict(cls="CAIR_PROPOSAL", beat_count=len(a["rumusan_beats"]),
                     beats=a["rumusan_beats"],
                     treatment="RP-007 — this Bahagian only, contractor perspective, no "
                               "Kepentingan / Isi Utama / Manfaat labels",
                     treatment_cls="COURSE_RULE_ALREADY_APPROVED",
                     note="The beat COUNT is a proposal derived from this unit's own content, "
                          "not carried from T04's three."),
        dialogue=dict(cls="CAIR_PROPOSAL", verdict=a["dialogue"]["verdict"],
                      reason=a["dialogue"]["reason"],
                      cast="NO_CHARACTER_PROPOSED_STOP_006_OPEN",
                      cast_cls="PENDING_BARIAH_PATTERN_DECISION"),
        mandatory_propositions=dict(cls="SOURCE_DERIVED",
                                    count=len(a["mandatory_propositions"]),
                                    propositions=a["mandatory_propositions"]),
        assessment=dict(
            composition="4 Multiple Choice + 1 Multiple Response",
            composition_cls="COURSE_RULE_ALREADY_APPROVED",
            key_status="DRAFTED_NOT_APPROVED",
            key_authority="NONE — drafted by CAIR from source rows, approved by nobody",
            items=[dict(
                slot=f"Q{i + 1}", kind=q["kind"], stem=q["stem"], stem_cls="CAIR_PROPOSAL",
                correct=q["correct"], correct_cls="SOURCE_DERIVED",
                correct_rows=q["correct_rows"],
                distractors=q["distractors"], distractors_cls="CAIR_PROPOSAL")
                for i, q in enumerate(a["assessment"])],
            note="Every stem and every correct response cites the rows it came from. The "
                 "distractors are ours and are labelled ours. Nothing here is an approved "
                 "answer key."),
        visual_obligations=dict(
            cls="CAIR_PROPOSAL",
            count=len(a["visual_subjects"]),
            source_attested=len([v for v in a["visual_subjects"] if v["has_source_figure"]]),
            subjects=a["visual_subjects"],
            rule="RP-104 — a visual direction is read from the source row's own figure or "
                 "table, never composed from a component name",
            rule_cls="COURSE_RULE_ALREADY_APPROVED",
            note="These are candidate SUBJECTS derived from text, not approved visual "
                 "directions. Only a subject with has_source_figure=true has a figure behind "
                 "it."),
        reuse_candidates=dict(
            cls="COURSE_RULE_ALREADY_APPROVED",
            candidates=["RP-001 review storyboard shell", "RP-002 screen grammar",
                        "RP-003 production panel", "RP-004 Notes block schema",
                        "RP-006 completion-state treatment", "RP-007 Rumusan treatment",
                        "RP-008 quiz review structure", "RP-011 feedback wording",
                        "RP-013 geometry registry", "RP-014 artifact identity",
                        "RP-015 screen/state/page separation", "RP-016 oracle contract",
                        "RP-017 population pinning"]),
        terminology=dict(cls="SOURCE_DERIVED", count=len(a["terminology"]),
                         terms=a["terminology"]),
        compliance_sensitive=dict(cls="SOURCE_DERIVED",
                                  count=len(a["compliance_sensitive"]),
                                  statements=a["compliance_sensitive"]),
        ambiguity_register=dict(cls="SOURCE_DERIVED", count=len(a["ambiguities"]),
                                items=a["ambiguities"]),
        missing_source_register=dict(cls="SOURCE_DERIVED",
                                     items=missing_source(ex, a)),
        extraction_qa=extraction_qa(ex))


def all_models():
    ex = EX.extract_all()
    return {uid: model(uid, e) for uid, e in ex.items()}, ex


if __name__ == "__main__":
    models, ex = all_models()
    for uid, m in models.items():
        a = m["screen_sequence"]["arithmetic"]
        print(f"{uid}: groups={len(m['grouping']['groups'])} "
              f"min_screens={a['minimum_total_screens']} "
              f"props={m['mandatory_propositions']['count']} "
              f"quiz={len(m['assessment']['items'])} "
              f"visuals={m['visual_obligations']['count']}"
              f"({m['visual_obligations']['source_attested']} attested) "
              f"dialogue={m['dialogue']['verdict']} "
              f"amb={m['ambiguity_register']['count']}")
