# -*- coding: utf-8 -*-
"""K5 Kelompok 0 v1.2 — Bariah decision ingestion and the K5 pattern policy it produces.

    python3 docs/pl06/tools/k5_pattern_policy_v1.py

WHAT THIS IS
------------
`K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2_vBariah.docx` is Bariah Ahmad's returned
decision package. Until this run it was PENDING_BARIAH_REVIEW and nothing read it. It has
now been read in full and is ingested here.

Bariah is the sole instructional authority. Sections A, C and D are approved as K5 defaults
subject to her stated amendments, from the Kelompok 0 v1.2 package.

Section B was undecided in that package and is now closed by a SECOND return,
`K5_Pengesahan_Seksyen_B_Bariah_v0_1_vBariah.docx`: B1 approved (two files per unit),
B2 TEST_REQUIRED_BEFORE_FINAL_FREEZE (no density approved — a 2-panel and a 3-panel
example must be shown first), B3 approved with amendment (one 90-minute slot = one unit),
B4 approved with conditional availability (working days except Cyberjaya meeting days;
actual dates still need Firdaus). Section B overall:
APPROVED_WITH_AMENDMENTS_FOR_CALIBRATION.

That authorises generation of the FOUR calibration units. It does not authorise mass
generation, and it does not freeze a panel density.

TWO THINGS THIS MODULE IS CAREFUL ABOUT
---------------------------------------
1. A TICKED BOX IS NOT THE WHOLE RULING. A5 carries a TERIMA tick and a prose amendment
   that overrides CAIR's point 1 outright. Recording A5 as plain acceptance would ship the
   opposite of what Bariah wrote. Every decision therefore stores `checkbox` and
   `bariah_prose` separately, plus `effective_rule` — what actually governs — and
   `prose_overrides_checkbox` where the two diverge.

2. THE DOCUMENT SAYS MORE THAN ANY SUMMARY OF IT. A1 carries an amendment and D2 carries a
   cross-course note that no briefing of this package mentioned. Both are ingested from the
   document, because the document is the authority and a summary of it is not.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

STAGE = "4.2F-G"
COURSE = "K5"

# ==========================================================================================
# PROVENANCE
# ==========================================================================================
SOURCE_DOCUMENT = dict(
    filename="K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2_vBariah.docx",
    bytes=33406,
    sha256="d22f6315a9bdec2c00d376aee710aacb301d97b2587ca82ee2ce0adcb8d964ce",
    paragraphs=209, tables=5,
    tracked_changes=False, word_comments=False,
    tracked_changes_basis="No comment or revision part exists in the OOXML package; the "
                          "answers are typed into the form's own fields.",
    read_in_full=True, read_at_stage=STAGE,
    covers="Sections A, C and D. Section B was left undecided in this package.")

# Bariah's second return, closing Section B.
SOURCE_DOCUMENT_B = dict(
    filename="K5_Pengesahan_Seksyen_B_Bariah_v0_1_vBariah.docx",
    bytes=36913,
    sha256="c3cd395d35b9f763cb849f3b5162517a30d029330f1b654fe944f3e6f4fc3012",
    paragraphs=19, tables=10, version="v0.1", date="4 Ogos 2026",
    tracked_changes=False, word_comments=False,
    read_in_full=True, read_at_stage=STAGE,
    covers="Section B only. It explicitly does not reopen A, C or D.",
    scope_note_verbatim=("Keputusan A, C dan D yang telah diluluskan kekal sebagai "
                         "default; borang ini tidak membuka semula keputusan tersebut."),
    calibration_note_verbatim=("Keputusan di bawah digunakan dahulu untuk fasa "
                               "kalibrasi. Kapasiti boleh dilaras selepas satu pusingan "
                               "semakan sebenar."))

# The definition B1 was blocked on. Bariah supplies it here for the first time.
LAMPIRAN_KEADAAN_DEFINITION = dict(
    what_it_is="bahan semakan teknikal — technical review material",
    what_it_is_not=["kandungan pembelajaran kedua (a second learner deck)",
                    "deck learner-facing", "aset MMD",
                    "storyboard tambahan yang perlu ditulis semula"],
    shows=("all interaction states for one storyboard — initial state, after a click, "
           "after every item is opened, quiz feedback, and the end state"),
    panel_rule="one panel represents one screen state",
    used_to_check=["interaction coverage", "state accuracy", "on-screen instructions",
                   "that no essential content is hidden"],
    source="K5_Pengesahan_Seksyen_B_Bariah_v0_1_vBariah.docx, section 1",
    note=("B1 and B2 were both blocked on this definition in the Kelompok 0 package. It "
          "is now given, and it is what makes the two-file split meaningful: the "
          "storyboard stays readable, the Lampiran Keadaan is the QA/technical evidence "
          "opened when needed."))

# What Bariah will and will not re-examine during calibration review.
CALIBRATION_REVIEW_SCOPE = dict(
    does_not_review="perkara standard yang telah diluluskan — approved standards are not "
                    "re-reviewed",
    reviews=["source fidelity and whether the important propositions are complete",
             "fit of the primary/supporting pattern, marking unit exceptions only",
             "scenario/dialogue, Rumusan, quiz and visual obligations that are "
             "unit-specific",
             "Lampiran Keadaan — that every learner-facing state is clear and no "
             "important state is missing"],
    source="K5_Pengesahan_Seksyen_B_Bariah_v0_1_vBariah.docx, section 3")

REVIEWER = dict(
    name="Bariah Ahmad", role="Instructional Designer",
    course="K5 — Pembinaan Landskap Luar",
    document_scope="Semua PL dan semua unit dalam K5",
    document_version="Kelompok 0, v1.2",
    date_in_closing_block="4/8/2026",
    review_date_field_in_header_table="BLANK",
    signature_line="BLANK",
    provenance_note=("Name, role and closing-block date are filled. The header table's "
                     "'Tarikh semakan' field and the signature line are both left blank. "
                     "Recorded exactly as found — the package is treated as Bariah's "
                     "authored response, and the unsigned signature line is reported "
                     "rather than described as a signature."))

OVERALL_VERDICT = dict(
    ticked="LULUS DENGAN PINDAAN DINYATAKAN",
    not_ticked=["LULUS TANPA PINDAAN", "PERLU BINCANG SEBELUM DILULUSKAN"],
    closing_note_verbatim=(
        "Seksyen A, C dan D diluluskan sebagai default, tertakluk pada pindaan yang saya "
        "nyatakan. Setiap unit masih perlu ikut sumber, dan sebarang pengecualian akan "
        "ditunjukkan untuk semakan. Seksyen B belum dapat diputuskan - perlu bincang "
        "dahulu tentang definisi \"Lampiran Keadaan\" dan skop kerja sebenar sebelum "
        "storyboarding bermula."))

DEADLINES = dict(
    bariah_feedback_required_before="5 OGOS 2026",
    internal_k5_storyboard_target="9 OGOS 2026",
    caveat_verbatim=("Sasaran bergantung pada ketersediaan semua sumber, kapasiti semakan "
                     "dan kelulusan corak. B3 dan B4 paling mendesak dari sudut kapasiti "
                     "semakan Bariah."))

SECTION_COUNTS = {"A": 7, "B": 4, "C": 2, "D": 4}
DECLARED_TOTAL = 17

APPROVED = "APPROVED_AS_K5_DEFAULT"
APPROVED_AMENDED = "APPROVED_WITH_BARIAH_AMENDMENT"
PENDING = "PENDING_BARIAH_DECISION"
# B2 is neither approved nor pending: Bariah ruled HOW it will be decided and made a test
# a prerequisite. Collapsing it into either bucket would be wrong in both directions.
TEST_REQUIRED = "TEST_REQUIRED_BEFORE_FINAL_FREEZE"
# B4 is approved, but its availability is conditional and its dates are not Bariah's to
# fix alone.
APPROVED_CONDITIONAL = "APPROVED_WITH_CONDITIONAL_AVAILABILITY"

SECTION_B_STATUS = "APPROVED_WITH_AMENDMENTS_FOR_CALIBRATION"
CALIBRATION_GENERATION_AUTHORIZED = True
MASS_GENERATION_AUTHORIZED = False
CALIBRATION_UNITS_AUTHORIZED = ["K5-PL06-T03-B03", "K5-PL06-T03-B04",
                                "K5-PL06-T05-B01", "K5-PL06-T06-B01"]
AUTHORIZATION_NOTE = (
    "Section B authorises generation of the FOUR calibration units only. Bariah's own "
    "framing is 'fasa kalibrasi', and her closing line is that after B1-B4 are confirmed "
    "the four calibration decks may be generated, audited and sent for ONE round of "
    "review. Nothing authorises the remaining K5 units.")

GLOBAL = "GLOBAL"
SOURCE_CONDITIONAL = "SOURCE_CONDITIONAL"
UNIT_SPECIFIC = "UNIT_SPECIFIC"

# ==========================================================================================
# THE SEVENTEEN DECISIONS
# ==========================================================================================
DECISIONS = [
    # ---------------- Section A ----------------
    dict(id="A1", section="A", title="Kandungan statik",
         t04_reference="S04, S05, S08, S11, S15, S17",
         checkbox="TERIMA sebagai corak default merentas K5",
         bariah_prose="Kandungan penting mesti kelihatan pada skrin, tidak boleh wujud "
                      "hanya dalam Speaker Notes.",
         prose_overrides_checkbox=False,
         status=APPROVED_AMENDED, scope=GLOBAL,
         effective_rule=("Static-content screens are a K5 default. Bariah's amendment "
                         "hardens CAIR point 3 into a prohibition: essential content must "
                         "be visible ON THE SCREEN and must never exist only in Speaker "
                         "Notes."),
         note_for_summaries=("This amendment is easy to lose. It converts a 'no essential "
                             "content only in Notes' guideline into an enforceable "
                             "screen-visibility rule.")),
    dict(id="A2", section="A", title="Klik untuk paparkan maklumat",
         t04_reference="S06, S07, S09, S10, S14, S16, S19",
         checkbox="TERIMA sebagai corak default merentas K5",
         bariah_prose=None, prose_overrides_checkbox=False,
         status=APPROVED, scope=GLOBAL,
         effective_rule=("Click-to-reveal is a K5 default exactly as CAIR proposed: one "
                         "clear proposition and matching VO per item; visual where it aids "
                         "comprehension or the source requires it; on-screen instruction "
                         "also spoken; every item must be opened before Seterusnya "
                         "activates."),
         note_for_summaries="Accepted with no amendment. The amendment field is blank."),
    dict(id="A3", section="A", title="Aliran proses berperingkat",
         t04_reference="S03",
         checkbox="PINDA — ikut catatan di atas",
         bariah_prose="Langkah ditunjukkan satu persatu, bersama visual nya.\n"
                      "Jika terdapat penerangan lanjut bagi setiap langkah - Klik pada "
                      "setiap langkah untuk penjelasan lanjut.",
         prose_overrides_checkbox=False,
         status=APPROVED_AMENDED, scope=GLOBAL,
         effective_rule=("Steps appear ONE AT A TIME, each with its own visual. Where the "
                         "source carries further explanation for a step, the learner "
                         "clicks that step to reveal it. This replaces any all-steps-"
                         "visible-at-once treatment."),
         note_for_summaries=("Bariah did not answer CAIR's overview-diagram point (3) or "
                             "the source-order point (2). Those remain CAIR proposals, not "
                             "rulings, and are recorded as UNRESOLVED_SUBPOINTS.")),
    dict(id="A4", section="A", title="Perbandingan",
         t04_reference="S06, S09, S13",
         checkbox="PINDA — ikut catatan di atas",
         bariah_prose="Terima framing CAIR (visual berpanel atau berasingan).\n"
                      "Corak Perbandingan hanya digunakan apabila sumber benar-benar "
                      "membandingkan dua atau lebih perkara secara eksplisit. Jika sumber "
                      "hanya menerangkan item secara berasingan, gunakan Klik untuk "
                      "Paparkan atau Kandungan Statik — jangan paksa framing perbandingan. "
                      "Rujuk T04 landskap lembut vs kejur: modul menerangkan berasingan, "
                      "tidak membandingkan.",
         prose_overrides_checkbox=False,
         status=APPROVED_AMENDED, scope=SOURCE_CONDITIONAL,
         effective_rule=("Comparison is permitted ONLY where the source explicitly "
                         "compares two or more things. Where the source merely explains "
                         "items separately, use Click-to-Reveal or Static Content. "
                         "Comparison framing must not be forced."),
         worked_example=("Bariah names T04 landskap lembut vs kejur as a case where the "
                         "module explains separately and does NOT compare — so Comparison "
                         "would be wrong there."),
         note_for_summaries=("The panel-versus-separate visual framing IS accepted; it is "
                             "the TRIGGER for using Comparison at all that is narrowed.")),
    dict(id="A5", section="A", title="Senario / dialog",
         t04_reference="S02",
         checkbox="TERIMA sebagai corak default merentas K5",
         bariah_prose="Merujuk D3, skrin senario/dialog wajib bagi semua unit K5 — bukan "
                      "sekadar \"hanya digunakan apabila ada justifikasi instruksional\". "
                      "Ayat justifikasi dalam cadangan CAIR (poin 1) tidak terpakai; "
                      "sebaliknya, setiap unit mesti mempunyai skrin senario/dialog.",
         prose_overrides_checkbox=True,
         status=APPROVED_AMENDED, scope=GLOBAL,
         effective_rule=("EVERY K5 unit must contain a scenario/dialogue screen. CAIR's "
                         "point 1 justification clause — 'only used where there is "
                         "instructional justification' — is explicitly disapplied. Points "
                         "2 and 3 (source-backed technical detail; no unsupported "
                         "authority for characters) stand."),
         override_note=("THE TICK SAYS TERIMA AND THE PROSE SAYS OTHERWISE. Recording A5 "
                        "as plain acceptance of CAIR's wording would ship the opposite of "
                        "Bariah's ruling: it would make the scenario screen optional when "
                        "she made it mandatory. The prose governs."),
         cross_reference="D3"),
    dict(id="A6", section="A", title="Rumusan",
         t04_reference="S20",
         checkbox="DEFAULT SEMUA UNIT K5 — guna struktur di atas kecuali ada pengecualian",
         bariah_prose="Terima struktur tiga-beat (Kepentingan / Skop dan Isi Utama / "
                      "Manfaat).\nPindaan pada poin visual: Rumusan sepatutnya mempunyai "
                      "visual sokongan (contoh montaj ringkas yang mengimbau isi utama), "
                      "selaras dengan amalan T04 dan pendirian visual A3. Visual adalah "
                      "elemen standard Rumusan untuk mengukuhkan ingatan, bukan sekadar "
                      "\"digunakan apabila membantu\".",
         prose_overrides_checkbox=False,
         status=APPROVED_AMENDED, scope=GLOBAL,
         effective_rule=("Every K5 Rumusan uses the three-beat structure Kepentingan / "
                         "Skop dan Isi Utama / Manfaat, AND carries a supporting visual. "
                         "CAIR point 3 ('visual not required') is amended: the visual is a "
                         "standard element of Rumusan, not an optional aid."),
         note_for_summaries=("Bariah gives an example of the visual — 'montaj ringkas yang "
                             "mengimbau isi utama' — but does not mandate that form. The "
                             "obligation is a supporting visual; the montage is her "
                             "illustration, recorded as such and not as a specification.")),
    dict(id="A7", section="A", title="Kuiz",
         t04_reference="S21",
         checkbox="DEFAULT SEMUA PL K5 — terpakai kecuali pengecualian unit dinyatakan",
         bariah_prose=None, prose_overrides_checkbox=False,
         status=APPROVED, scope=GLOBAL,
         effective_rule=("Default K5 quiz is 4 MCQ + 1 Multiple Response with a 60 percent "
                         "pass mark, applying to all PL in K5 unless a unit exception is "
                         "stated. Stems must not use 'dalam modul' / 'mengikut modul' / "
                         "'modul menyenaraikan'. Multiple Response uses checkboxes with no "
                         "A/B/C labels; stems and answers stay unit-specific and "
                         "source-backed."),
         note_for_summaries=("This also settles the RP-009 / RP-010 VERIFY flags in the "
                             "PL06 rule-portability matrix, which recorded 4+1 and 60 "
                             "percent as unconfirmed. They are now confirmed by the "
                             "instructional authority, at K5 scope.")),

    # ---------------- Section B — DECIDED in the v0.1 confirmation form ----------------
    dict(id="B1", section="B", title="Bilangan fail bagi setiap unit",
         checkbox="TERIMA — dua fail berasingan: Storyboard + Lampiran Keadaan",
         bariah_prose=None, prose_overrides_checkbox=False,
         status=APPROVED, scope=GLOBAL,
         decided_in="K5_Pengesahan_Seksyen_B_Bariah_v0_1_vBariah.docx",
         effective_rule=("Two separate files per unit: one Storyboard file and one "
                         "Lampiran Keadaan file. The storyboard stays readable; the "
                         "Lampiran Keadaan is the QA/technical review evidence, opened "
                         "when needed."),
         previously="PENDING — blocked on a definition of Lampiran Keadaan, which this "
                    "form supplies",
         note_for_summaries=("Bariah frames it as 'Cadangan operasi untuk fasa "
                             "kalibrasi', so it is a calibration-phase rule, not an "
                             "irreversible course-wide freeze.")),
    dict(id="B2", section="B", title="Kepadatan Lampiran Keadaan",
         checkbox="UJI DULU — lihat satu contoh 2 panel dan satu contoh 3 panel sebelum "
                  "putuskan",
         bariah_prose=None, prose_overrides_checkbox=False,
         status=TEST_REQUIRED, scope=GLOBAL,
         decided_in="K5_Pengesahan_Seksyen_B_Bariah_v0_1_vBariah.docx",
         effective_rule=("NO density is approved. Bariah must be shown one 2-panel and "
                         "one 3-panel example of the SAME Lampiran Keadaan before any "
                         "density is fixed. The proposal to start at 2 panels was NOT "
                         "accepted — the 'TERIMA — 2 panel' option was left unticked."),
         must_not="record any panel density as approved, including 2",
         test_requirement=dict(densities_to_produce=[2, 3], same_unit=True,
                               same_state_set=True,
                               why="density must be the only variable between the two"),
         previously="PENDING — blocked on B1's definition",
         note_for_summaries=("The one Section B item that is NOT approved. Bariah ruled "
                             "HOW to decide it; the test result is a prerequisite, not a "
                             "formality.")),
    dict(id="B3", section="B", title="Kapasiti semakan bagi satu sesi",
         checkbox="PINDA — 1 unit sahaja",
         bariah_prose="Satu slot = satu unit sahaja. Setiap unit (1 storyboard + Lampiran "
                      "Keadaan) perlu satu slot penuh untuk semakan teliti; jangan "
                      "padatkan lebih satu unit dalam satu slot.",
         prose_overrides_checkbox=False,
         status=APPROVED_AMENDED, scope=GLOBAL,
         decided_in="K5_Pengesahan_Seksyen_B_Bariah_v0_1_vBariah.docx",
         effective_rule=("One review slot = one unit, where a unit is one Storyboard plus "
                         "one Lampiran Keadaan. A slot runs 90 minutes. More than one "
                         "unit must never be packed into a slot."),
         slot_minutes=90, units_per_slot=1,
         previously="PENDING",
         note_for_summaries=("CAIR proposed 2 units for the first session; Bariah halved "
                             "it. The 90-minute figure comes from her B4 note, not from "
                             "the 60-90 range in the question.")),
    dict(id="B4", section="B", title="Slot semakan harian",
         checkbox="PINDA — ikut hari tertentu sahaja",
         bariah_prose="Ikut hari tertentu - semua hari bekerja kecuali hari ada meeting "
                      "di Cyberjaya. Sabtu/Ahad boleh jika tiada urusan (tidak tetap). "
                      "Pada hari yang tersedia, boleh komit beberapa slot sehari; setiap "
                      "slot 90 minit, satu unit (1 SB + Lampiran Keadaan) satu slot.",
         prose_overrides_checkbox=False,
         status=APPROVED_CONDITIONAL, scope=GLOBAL,
         decided_in="K5_Pengesahan_Seksyen_B_Bariah_v0_1_vBariah.docx",
         effective_rule=("Working days are POTENTIALLY available except days with a "
                         "Cyberjaya meeting. Weekends are optional and not fixed. On an "
                         "available day several 90-minute slots may be committed, each "
                         "carrying exactly one unit."),
         availability_is_conditional=True,
         requires_firdaus_confirmation=["the actual available dates",
                                        "the actual slot count per day"],
         must_not="treat 'potentially available' as a schedule, or invent dates or slot "
                  "counts",
         previously="PENDING — the earlier package ticked 'Perlu bincang', not a "
                    "decision"),

    # ---------------- Section C ----------------
    dict(id="C1", section="C", title="Lapan kumpulan visual AG-01 hingga AG-08",
         checkbox="REKOD TEPAT — tiada pindaan diperlukan",
         bariah_prose=None, prose_overrides_checkbox=False,
         status=APPROVED, scope=GLOBAL,
         effective_rule=("The existing T04 record is confirmed accurate: AG-01 to AG-08 "
                         "accepted at set level with conditions, individual cards not "
                         "ticked, production count 46 visual requirements to 41 proposed "
                         "unique assets. No amendment."),
         must_not="reopen the completed T04 decisions"),
    dict(id="C2", section="C", title="Asas tiga item yang tidak boleh dikongsi",
         checkbox="SAHKAN kedua-dua asas bagi ketiga-tiga item",
         bariah_prose=None, prose_overrides_checkbox=False,
         status=APPROVED, scope=GLOBAL,
         effective_rule=("Both bases — instructional and production — are confirmed for "
                         "all three non-shareable items: Baja Pengurusan Stok dan "
                         "Penyimpanan, Baja Keselamatan Pekerja, and Racun Keselamatan dan "
                         "Kesihatan (HSE)."),
         must_not="reopen the completed T04 decisions"),

    # ---------------- Section D ----------------
    dict(id="D1", section="D", title="Watak",
         checkbox="Ikut kes semasa semakan unit",
         bariah_prose=None, prose_overrides_checkbox=False,
         status=APPROVED, scope=UNIT_SPECIFIC,
         effective_rule=("Characters are chosen case by case at unit review. Alya and "
                         "Encik Rahman are NOT approved as a K5-wide cast; T04's use of "
                         "them does not carry forward automatically."),
         note_for_summaries=("This is an approved decision whose content is 'decide per "
                             "unit'. It is not pending — the ruling is that no global cast "
                             "exists.")),
    dict(id="D2", section="D", title="Narator",
         checkbox="Ya",
         bariah_prose="K1, K3, K5 – Hilmi dan K2, K4 – Maya",
         prose_overrides_checkbox=False,
         status=APPROVED_AMENDED, scope=GLOBAL,
         effective_rule="Hilmi is the narrator across all K5 units.",
         cross_course_note=("Bariah's comment also assigns narrators beyond K5: Hilmi for "
                            "K1, K3 and K5; Maya for K2 and K4. Recorded verbatim as "
                            "authority, but NOT applied here — this run is scoped to K5 "
                            "and is instructed not to touch K2 or K3. The K1/K2/K3/K4 "
                            "assignments are carried as INGESTED_NOT_APPLIED for whichever "
                            "course run picks them up."),
         note_for_summaries=("The cross-course sentence is additional authority that a "
                             "summary of this package would not necessarily carry.")),
    dict(id="D3", section="D", title="Skrin senario / dialog",
         checkbox="Wajib bagi semua unit",
         bariah_prose=None, prose_overrides_checkbox=False,
         status=APPROVED, scope=GLOBAL,
         effective_rule="A scenario/dialogue screen is mandatory in every K5 unit.",
         cross_reference="A5",
         note_for_summaries="D3 is the ruling A5's prose amendment defers to."),
    dict(id="D4", section="D", title="Struktur Bahagian dan skrin penutup",
         checkbox="Ikut kes",
         bariah_prose="Default ini (tiada label Bahagian + penutup \"Tamat Topik\") hanya "
                      "terpakai untuk Topik tiada Bahagian, seperti T04.\n"
                      "Bagi Topik yang mempunyai beberapa Bahagian - Contohnya Topik 3 "
                      "Bahagian 2 (B02) yang telah dibuat. Setiap Bahagian mempunyai "
                      "storyboard, Rumusan dan Kuiz tersendiri. Skrin penutup Bahagian "
                      "yang masih ada Bahagian seterusnya berbunyi \"Tamat Bahagian X. "
                      "Teruskan pembelajaran ke bahagian seterusnya\". \"Tamat Topik\" "
                      "hanya pada penutup Bahagian terakhir.\n"
                      "Oleh itu default ini ikut kes - bergantung sama ada Topik itu tiada "
                      "Bahagian, atau berbilang Bahagian, mengikut penilaian segmentasi.",
         prose_overrides_checkbox=False,
         status=APPROVED_AMENDED, scope=SOURCE_CONDITIONAL,
         effective_rule=("Segmentation-dependent. Topic WITHOUT Bahagian: no Bahagian "
                         "label on learner-facing screens; close with 'Tamat Topik'. Topic "
                         "WITH multiple Bahagian: each Bahagian gets its own storyboard, "
                         "its own Rumusan and its own Kuiz; a Bahagian that has a "
                         "successor closes with 'Tamat Bahagian X. Teruskan pembelajaran "
                         "ke bahagian seterusnya'; only the FINAL Bahagian closes with "
                         "'Tamat Topik'."),
         depends_on="the Topic/Bahagian segmentation assessment for each structure"),
]

CLOSING_INTERMEDIATE = "Tamat Bahagian X. Teruskan pembelajaran ke bahagian seterusnya"
CLOSING_FINAL = "Tamat Topik"

# Sub-points CAIR proposed that Bariah did not answer. They are not rulings and are not
# applied as defaults; they are named so nobody mistakes silence for approval.
UNRESOLVED_SUBPOINTS = [
    dict(decision="A3", subpoint="CAIR point 2 — keep source order unless Bariah approves "
                                 "a clearer instructional order",
         status="NOT_ADDRESSED_BY_BARIAH"),
    dict(decision="A3", subpoint="CAIR point 3 — show a whole-process diagram before the "
                                 "first step where the source provides one",
         status="NOT_ADDRESSED_BY_BARIAH"),
]

# ==========================================================================================
# THE POLICY THE DECISIONS PRODUCE
# ==========================================================================================
POLICY = dict(
    scenario_screen_required=True, scenario_basis=["D3", "A5"],
    summary_structure=["Kepentingan", "Skop dan Isi Utama", "Manfaat"],
    summary_visual_required=True, summary_basis=["A6"],
    quiz_mcq=4, quiz_multiple_response=1, quiz_pass_percent=60, quiz_basis=["A7"],
    narrator="Hilmi", narrator_basis=["D2"],
    characters="PER_UNIT_AT_REVIEW", characters_basis=["D1"],
    comparison_requires_explicit_source_comparison=True, comparison_basis=["A4"],
    stepwise_one_at_a_time=True, stepwise_click_for_detail=True, stepwise_basis=["A3"],
    essential_content_must_be_on_screen=True, essential_content_basis=["A1"],
    closing_intermediate=CLOSING_INTERMEDIATE, closing_final=CLOSING_FINAL,
    closing_basis=["D4"],
    per_bahagian_storyboard_summary_quiz=True, per_bahagian_basis=["D4"],

    # ---- Section B, now closed ----
    files_per_unit=2, files_per_unit_names=["Storyboard", "Lampiran Keadaan"],
    files_per_unit_basis=["B1"],
    lampiran_panel_density="NOT_APPROVED_TEST_REQUIRED",
    lampiran_densities_to_test=[2, 3], lampiran_density_basis=["B2"],
    review_slot_minutes=90, units_per_review_slot=1, review_capacity_basis=["B3"],
    availability="CONDITIONAL_WORKING_DAYS_EXCEPT_CYBERJAYA_MEETINGS",
    availability_basis=["B4"],
    availability_dates="REQUIRES_FIRDAUS_CONFIRMATION",
    slots_per_day="REQUIRES_FIRDAUS_CONFIRMATION",

    still_pending=[],
    still_not_frozen=["B2 panel density — a test result is required before any density "
                      "is approved"])


def decisions_by_section(section):
    return [d for d in DECISIONS if d["section"] == section]


def approved():
    """Decisions that authorise action. B4 is included: it is approved, with conditions
    on availability, not withheld. B2 is NOT here — a test is a prerequisite, not a
    condition on an approval that already exists."""
    return [d for d in DECISIONS
            if d["status"] in (APPROVED, APPROVED_AMENDED, APPROVED_CONDITIONAL)]


def test_required():
    return [d for d in DECISIONS if d["status"] == TEST_REQUIRED]


def conditional():
    return [d for d in DECISIONS if d["status"] == APPROVED_CONDITIONAL]


def pending():
    return [d for d in DECISIONS if d["status"] == PENDING]


def overrides():
    return [d for d in DECISIONS if d.get("prose_overrides_checkbox")]


def amended():
    return [d for d in DECISIONS if d["status"] == APPROVED_AMENDED]


def ingestion_record():
    return dict(
        stage=STAGE, course=COURSE,
        source_document=SOURCE_DOCUMENT, reviewer=REVIEWER,
        overall_verdict=OVERALL_VERDICT, deadlines=DEADLINES,
        declared_total=DECLARED_TOTAL, section_counts=SECTION_COUNTS,
        modelled_total=len(DECISIONS),
        modelled_by_section={s: len(decisions_by_section(s)) for s in "ABCD"},
        approved_ids=[d["id"] for d in approved()],
        amended_ids=[d["id"] for d in amended()],
        pending_ids=[d["id"] for d in pending()],
        conditional_ids=[d["id"] for d in conditional()],
        # The four buckets partition all 17 exactly once. TEST_REQUIRED is its own bucket
        # precisely so B2 cannot be quietly counted as approved.
        partition=dict(approved=len(approved()), test_required=len(test_required()),
                       pending=len(pending()),
                       total=len(approved()) + len(test_required()) + len(pending())),
        prose_override_ids=[d["id"] for d in overrides()],
        section_b_status=SECTION_B_STATUS,
        section_b_note=("Section B is closed by a second Bariah return. B1 approved, B2 "
                        "TEST_REQUIRED_BEFORE_FINAL_FREEZE, B3 approved with amendment, "
                        "B4 approved with conditional availability. No panel density is "
                        "approved and no availability date or slot count is invented."),
        section_b_source=SOURCE_DOCUMENT_B,
        lampiran_keadaan_definition=LAMPIRAN_KEADAAN_DEFINITION,
        calibration_review_scope=CALIBRATION_REVIEW_SCOPE,
        calibration_generation_authorized=CALIBRATION_GENERATION_AUTHORIZED,
        mass_generation_authorized=MASS_GENERATION_AUTHORIZED,
        calibration_units_authorized=CALIBRATION_UNITS_AUTHORIZED,
        authorization_note=AUTHORIZATION_NOTE,
        test_required_ids=[d["id"] for d in DECISIONS if d["status"] == TEST_REQUIRED],
        unresolved_subpoints=UNRESOLVED_SUBPOINTS,
        policy=POLICY, decisions=DECISIONS)


if __name__ == "__main__":
    r = ingestion_record()
    print(f"K5 Kelompok 0 v1.2 ingestion — stage {r['stage']}")
    print(f"  document: {r['source_document']['filename']}")
    print(f"  sha256:   {r['source_document']['sha256'][:16]}…  "
          f"({r['source_document']['bytes']:,} bytes)")
    print(f"  reviewer: {r['reviewer']['name']} — signature line "
          f"{r['reviewer']['signature_line']}")
    print(f"  verdict:  {r['overall_verdict']['ticked']}")
    print(f"\n  declared {r['declared_total']} decisions, modelled {r['modelled_total']} "
          f"{r['modelled_by_section']}")
    print(f"  approved: {len(r['approved_ids'])} {r['approved_ids']}")
    print(f"  test-required (NOT approved): {r['test_required_ids']}")
    print(f"  conditional: {r['conditional_ids']}")
    print(f"  partition: {r['partition']}")
    print(f"  Section B: {r['section_b_status']}")
    print(f"  calibration generation authorized: "
          f"{r['calibration_generation_authorized']} | mass generation: "
          f"{r['mass_generation_authorized']}")
    print(f"  amended:  {len(r['amended_ids'])} {r['amended_ids']}")
    print(f"  pending:  {len(r['pending_ids'])} {r['pending_ids']}")
    print(f"  prose overrides the tick: {r['prose_override_ids']}")
    print(f"  unresolved CAIR sub-points: {len(r['unresolved_subpoints'])}")
