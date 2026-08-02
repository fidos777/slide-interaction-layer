# -*- coding: utf-8 -*-
"""Stage 4.2F-B0.8A — the ONE governed review model for the Bariah review artifact.

    CONTROLLED_CONTENT_SOURCE_OF_TRUTH   this model, emitted as
                                         T04_BARIAH_REVIEW_MODEL_v1.json
    GENERATED_REFERENCE_VIEW             T04_BARIAH_CONTENT_REVIEW_PACK_v2.md
    HUMAN_APPROVAL_ARTIFACT              T04_Pakej_Semakan_Bariah_v2.docx

The DOCX is what Bariah reads and signs. Every substantive string in it is generated from
this model — no instruction, question, note, decision term, provenance label, dependency,
total, constraint or approval field may exist only in the DOCX.

WHY THIS STAGE EXISTS
---------------------
A manually produced DOCX and the Stage 4.2F-B0.8 Markdown pack were semantically different
documents: the DOCX carried reviewer instructions, a summary line and TWO different final
verdict blocks that appeared nowhere in the Markdown, used ☐ A ☐ E ☐ M ☐ R abbreviations, and
offered MERGE with no target field. That divergence is a last-mile governance defect — the
thing the reviewer actually signs was not the thing that had been validated. One model now
feeds all three representations.
"""
import hashlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
T04 = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(os.path.dirname(T04)))
sys.path.insert(0, HERE)

STAGE = "4.2F-B0.8A"
MODEL_VERSION = "T04_BARIAH_REVIEW_MODEL_v1"
GENERATOR_VERSION = "t04_review_render_v1"
UNIT_ID = "K5-PL06-T04-B01"
LESSON_TITLE = "Penjagaan dan Penyelenggaraan"

CONTENT_STATUS = "CAIR_ASSISTED_DRAFT"
INSTRUCTIONAL_AUTHORITY = "BARIAH"
APPROVAL_STATUS = "PENDING_BARIAH_REVIEW"

ARTIFACT_HIERARCHY = dict(
    CONTROLLED_CONTENT_SOURCE_OF_TRUTH="docs/pl06/t04/T04_BARIAH_REVIEW_MODEL_v1.json",
    GENERATED_REFERENCE_VIEW="docs/pl06/t04/T04_BARIAH_CONTENT_REVIEW_PACK_v2.md",
    HUMAN_APPROVAL_ARTIFACT="reviews/storyboard-bariah/t04_bariah_review/"
                            "T04_Pakej_Semakan_Bariah_v2.docx",
    rule="Every substantive item in the DOCX is generated from the model. Nothing substantive "
         "may exist only in the DOCX, and no reviewable item may exist only in the Markdown.")

# The non-governed reference that prompted this stage. Recorded, never treated as data.
EXTERNAL_MANUAL_DOCX = dict(
    filename="T04_Pakej_Semakan_Bariah_v1.docx",
    byte_size=46676,
    sha256="9c354b0e39e8667401b70a675775ce990169e8dbbb3f403e7d7bd57d32f24873",
    declared_pages_in_docprops=1,
    declared_pages_reliable=False,
    page_count_note="docProps/app.xml declares Pages=1 and Words=0, which Word writes when a "
                    "document has never been repaginated by the application. The real page "
                    "count is not readable from the package, and no renderer is available to "
                    "determine it.",
    non_empty_paragraphs=296,
    status="NON_GOVERNED_REFERENCE",
    delivery_status="WITHDRAWN_NOT_FOR_BARIAH",
    used_as_authority=False,
    copied_into_evidence=False,
    divergences_observed=[
        "reviewer instructions ('Cara semak') present in the DOCX, absent from the Markdown",
        "a 'Ringkasan cadangan' totals line present only in the DOCX",
        "TWO different final-verdict vocabularies in one document — 'Lulus / Lulus dengan "
        "pindaan / Perlu dibaiki' near the top and 'Lulus untuk generate storyboard / Lulus "
        "dengan pindaan / Belum lulus' at the end",
        "decision checkboxes abbreviated to A / E / M / R, which a reviewer cannot expand "
        "without the legend",
        "MERGE offered with no target-ID field, so a merge decision could not be recorded",
        "'Arahan selepas semakan' instructions present only in the DOCX",
    ],
    conclusion="It is a competent human document. It is not a governed one: six classes of "
               "substantive content existed only inside it.")


def _load(name):
    with open(os.path.join(T04, name), encoding="utf-8") as f:
        return json.load(f)


SEQ = _load("T04_PROPOSED_SCREEN_SEQUENCE_v1.json")
CLOSURE = _load("T04_VISUAL_OBLIGATION_CLOSURE_v1.json")
ASSETS = _load("T04_VISUAL_ASSET_GROUPING_PLAN_v2.json")
DIALOGUE_SRC = _load("T04_SLIDE_2_DIALOGUE_CAIR_DRAFT_v1.json")
RUMUSAN_SRC = _load("T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v3.json")
QUIZ_SRC = _load("T04_QUIZ_CAIR_ASSISTED_DRAFT_v1.json")

SOURCE_ARTIFACTS = {
    "screen_sequence": "T04_PROPOSED_SCREEN_SEQUENCE_v1.json",
    "visual_asset_grouping": "T04_VISUAL_ASSET_GROUPING_PLAN_v2.json",
    "visual_obligation_closure": "T04_VISUAL_OBLIGATION_CLOSURE_v1.json",
    "slide_2_dialogue": "T04_SLIDE_2_DIALOGUE_CAIR_DRAFT_v1.json",
    "rumusan": "T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v3.json",
    "quiz": "T04_QUIZ_CAIR_ASSISTED_DRAFT_v1.json",
}

# ==========================================================================================
# PART 2 — DECISION VOCABULARY, DIFFERENTIATED BY ITEM CLASS
# ==========================================================================================
DECISIONS_CONTENT = ["ACCEPT", "EDIT", "REMOVE"]
DECISIONS_STRUCTURAL = ["ACCEPT", "EDIT", "REMOVE", "MERGE"]
REUSE_DECISIONS = ["REUSE_ALLOWED", "REUSE_NOT_ALLOWED", "REUSE_WITH_CONDITIONS"]

DECISION_LABELS_MS = {"ACCEPT": "TERIMA", "EDIT": "PINDA", "REMOVE": "BUANG",
                      "MERGE": "GABUNG"}
REUSE_LABELS_MS = {"REUSE_ALLOWED": "Boleh dikongsi",
                   "REUSE_NOT_ALLOWED": "Tidak boleh dikongsi",
                   "REUSE_WITH_CONDITIONS": "Boleh dikongsi dengan syarat"}

MERGE_RULE = dict(
    applies_to=["screen_sequence", "visual_asset_grouping"],
    forbidden_for=["slide_2_dialogue", "rumusan", "quiz"],
    required_fields=["merge_source_id", "merge_target_id", "merge_reason",
                     "proposed_resulting_title_or_group"],
    constraint="MERGE is a relationship, not a standalone checkbox. A MERGE with no target ID "
               "is not a decision — it records that the reviewer wanted something merged "
               "without saying with what, which cannot be actioned.",
    source_target_must_differ=True,
    not_the_same_as_reuse="MERGE combines two proposed items into one. REUSE shares one "
                          "produced asset across more than one screen. Conflating them would "
                          "let a reuse answer silently delete a screen.",
    docx_fields_ms=["☐ TERIMA", "☐ PINDA", "☐ BUANG", "☐ GABUNG DENGAN ID: __________",
                    "Sebab / cadangan susunan baharu: ____________________________________"])

# ==========================================================================================
# PART 3 — TREATMENT LABELS IN CLEAR MALAY
# ==========================================================================================
TREATMENT_MS = {
    "TITLE": "Skrin tajuk",
    "DIALOGUE_SCENARIO": "Senario perbualan",
    "PROCESS_FLOW_STEPPED": "Aliran proses berperingkat",
    "CONTENT_STATIC": "Kandungan statik",
    "CLICK_TO_REVEAL": "Klik untuk paparkan maklumat",
    "CONTENT_WITH_CONFIRMED_REVEAL": "Kandungan utama dengan maklumat tambahan boleh dibuka",
    "RUMUSAN": "Rumusan",
    "QUIZ": "Kuiz",
    "CLOSING": "Skrin penutup",
}

# Short learner-purpose lines in Malay, one per screen. Modelled, not typed into the DOCX.
SCREEN_PURPOSE_MS = {
    "T04-S01": "Membuka topik dan menyatakan Topik serta Bahagian.",
    "T04-S02": "Membuka dari tapak — apa yang perlu diuruskan selepas kerja pembinaan siap.",
    "T04-S03": "Memperkenalkan enam aktiviti penyeliaan mengikut turutan.",
    "T04-S04": "Menetapkan kategori landskap lembut sebelum tiga operasinya diajar.",
    "T04-S05": "Menerangkan tujuan penyiraman.",
    "T04-S06": "Membezakan penyiraman manual dengan sistem pengairan automatik.",
    "T04-S07": "Empat aspek pengurusan penyiraman untuk kontraktor.",
    "T04-S08": "Menerangkan tujuan pembajaan.",
    "T04-S09": "Membezakan tiga kaedah pembajaan.",
    "T04-S10": "Lima aspek pengurusan pembajaan untuk kontraktor.",
    "T04-S11": "Menetapkan tiga masalah yang dikawal oleh racun.",
    "T04-S12": "Susunan keutamaan IPM — kawalan kimia bukan tindakan pertama.",
    "T04-S13": "Memadankan jenis racun dengan sasarannya.",
    "T04-S14": "Kawalan perundangan dan keperluan pengendali berlesen.",
    "T04-S15": "PPE lengkap, dengan penyimpanan dan SDS sebagai maklumat tambahan.",
    "T04-S16": "Pengurusan risiko semburan.",
    "T04-S17": "Menetapkan kategori landskap kejur dan bezanya dengan landskap lembut.",
    "T04-S18": "Empat kumpulan fungsi landskap kejur.",
    "T04-S19": "Rumusan empat ayat.",
    "T04-S20": "Kuiz lima soalan.",
    "T04-S21": "Menutup Bahagian.",
}

SCREEN_POPULATION_MS = {
    "T04-S01": "Tajuk unit",
    "T04-S02": "Aliran proses dan dua kategori landskap",
    "T04-S03": "Enam aktiviti penyeliaan",
    "T04-S04": "Definisi landskap lembut",
    "T04-S05": "Definisi dan tujuan siram",
    "T04-S06": "Penyiraman manual, sistem semburan, sistem titis",
    "T04-S07": "Jadual penyiraman, sumber air, pemantauan, kecekapan kos",
    "T04-S08": "Definisi dan tujuan baja",
    "T04-S09": "Pembajaan tabur, poket, semburan folia",
    "T04-S10": "Program, pematuhan spesifikasi, stok, keselamatan pekerja, dokumentasi",
    "T04-S11": "Perosak, penyakit dan rumpai",
    "T04-S12": "Kawalan kultur, fizikal, biologi dan kimia",
    "T04-S13": "Racun serangga, racun kulat, racun rumpai",
    "T04-S14": "Akta, pengendali berlesen",
    "T04-S15": "PPE lengkap, penyimpanan berkunci, SDS",
    "T04-S16": "Cuaca semburan, notifikasi, pelaporan",
    "T04-S17": "Definisi landskap kejur",
    "T04-S18": "Ruang dan sirkulasi, struktur dan kejuruteraan, kebolehgunaan, estetika",
    "T04-S19": "Empat ayat rumusan",
    "T04-S20": "Lima soalan kuiz",
    "T04-S21": "Penutup Bahagian",
}

SCREEN_VISUAL_MS = {
    "T04-S03": "Rajah enam langkah, satu visual bagi setiap langkah",
    "T04-S06": "Visual perbandingan kaedah penyiraman",
    "T04-S09": "Visual perbandingan tiga kaedah pembajaan",
    "T04-S12": "Rajah susunan keutamaan IPM",
    "T04-S13": "Visual perbandingan jenis racun dan sasarannya",
    "T04-S18": "Empat visual fungsi landskap kejur",
}


def _screens():
    out = []
    for s in SEQ["screens"]:
        sid = s["screen_id"]
        n_vo = len(s["visual_obligations_served"])
        vis = SCREEN_VISUAL_MS.get(
            sid, (f"{n_vo} visual dicadangkan" if n_vo else "Tiada visual khusus"))
        out.append(dict(
            item_id=sid,
            item_class="screen_sequence",
            display_title=s["working_title"],
            treatment_code=s["treatment"],
            treatment_ms=TREATMENT_MS[s["treatment"]],
            purpose_ms=SCREEN_PURPOSE_MS[sid],
            population_ms=SCREEN_POPULATION_MS[sid],
            visual_ms=vis,
            visual_obligation_count=n_vo,
            content_status=CONTENT_STATUS,
            instructional_authority=INSTRUCTIONAL_AUTHORITY,
            approval_status=APPROVAL_STATUS,
            allowed_decisions=list(DECISIONS_STRUCTURAL),
            merge=dict(merge_source_id=None, merge_target_id=None, merge_reason=None,
                       proposed_resulting_title_or_group=None),
            decision=None, comment=None,
            source_artifact=SOURCE_ARTIFACTS["screen_sequence"],
            internal_provenance="CAIR proposal derived from the controlled T04 extract"))
    return out


SCREENS = _screens()

# ==========================================================================================
# PART 4-6 — VISUAL AND ASSET-GROUP REVIEW
# ==========================================================================================
ORIGIN_LABELS = ["KEPERLUAN_VISUAL_BARIAH", "CADANGAN_PELAKSANAAN_CAIR_DARIPADA_RULING_BARIAH",
                 "CADANGAN_CAIR_UNTUK_SENARIO", "SUMBER_MODUL",
                 "GABUNGAN_BEBERAPA_KEPERLUAN_VISUAL"]

ORIGIN_MS = {
    "KEPERLUAN_VISUAL_BARIAH": "Keperluan visual yang ditetapkan oleh Bariah",
    "CADANGAN_PELAKSANAAN_CAIR_DARIPADA_RULING_BARIAH":
        "Cadangan pelaksanaan CAIR berdasarkan ruling Bariah",
    "CADANGAN_CAIR_UNTUK_SENARIO": "Cadangan CAIR untuk senario",
    "SUMBER_MODUL": "Daripada modul",
    "GABUNGAN_BEBERAPA_KEPERLUAN_VISUAL": "Gabungan beberapa keperluan visual",
}

_AG_ORIGIN = {
    "AG-01": "KEPERLUAN_VISUAL_BARIAH",
    "AG-02": "KEPERLUAN_VISUAL_BARIAH",
    "AG-03": "GABUNGAN_BEBERAPA_KEPERLUAN_VISUAL",
    "AG-04": "GABUNGAN_BEBERAPA_KEPERLUAN_VISUAL",
    "AG-05": "GABUNGAN_BEBERAPA_KEPERLUAN_VISUAL",
    "AG-06": "KEPERLUAN_VISUAL_BARIAH",
    "AG-07": "KEPERLUAN_VISUAL_BARIAH",
    "AG-08": "CADANGAN_CAIR_UNTUK_SENARIO",
}

_AG_LABEL_MS = {
    "AG-01": "Aliran proses enam langkah",
    "AG-02": "Landskap Lembut — kategori",
    "AG-03": "Siram — operasi dan sub-topik",
    "AG-04": "Baja — operasi dan sub-topik",
    "AG-05": "Racun — IPM, kawalan dan jenis racun",
    "AG-06": "Racun — perundangan, HSE dan risiko",
    "AG-07": "Landskap Kejur — kategori dan empat fungsi",
    "AG-08": "Slide 2 — senario pengenalan",
}

# Provenance disclosures the brief requires verbatim in the model, not only in the DOCX.
AG01_SEVENTH_ASSET = dict(
    asset_group_id="AG-01",
    six_step_visuals_origin="KEPERLUAN_VISUAL_BARIAH",
    seventh_asset="Lukisan semula terkawal rajah proses enam langkah",
    seventh_asset_origin="CADANGAN_PELAKSANAAN_CAIR_DARIPADA_D05",
    disclosure_ms="Enam visual langkah ialah keperluan visual yang ditetapkan oleh Bariah. "
                  "Aset ketujuh — lukisan semula rajah proses enam langkah — ialah cadangan "
                  "pelaksanaan CAIR berdasarkan keputusan D-05, bukan item yang dinamakan "
                  "secara langsung oleh Bariah.")

AG08_SCENARIO = dict(
    asset_group_id="AG-08",
    origin="CADANGAN_CAIR_UNTUK_SENARIO",
    asset_count=2,
    part_of_46_obligations=False,
    disclosure_ms="Dua aset senario Slide 2 ialah cadangan CAIR untuk senario perbualan. Ia "
                  "BUKAN sebahagian daripada 46 keperluan visual yang ditetapkan oleh "
                  "Bariah, kerana ruling visual Bariah meliputi tajuk kandungan, bukan skrin "
                  "senario.")

AUTHORITY_STATEMENT_MS = (
    "Bariah menetapkan bahawa kandungan yang dinyatakan memerlukan layanan visual. "
    "Hierarki tajuk dalam modul digunakan untuk menyenaraikan populasi terperinci. "
    "CAIR mencadangkan pengumpulan aset dan pendekatan penghasilan.")

_T = ASSETS["totals"]
VISUAL_TOTALS = dict(
    visual_obligations=_T["visual_obligation_count"],
    asset_groups=_T["asset_group_count"],
    proposed_unique_assets=_T["proposed_unique_assets"],
    status="PROPOSED_NOT_APPROVED",
    composite_covered=len([o for o in CLOSURE["obligations"]
                           if o["closure_outcome"] == "COVERED_BY_COMPOSITE_ASSET_GROUP"]),
    no_separate_asset=len([o for o in CLOSURE["obligations"]
                           if o["closure_outcome"] == "NOT_A_SEPARATE_ASSET_WITH_REASON"]),
    additional_assets=sum(g.get("additional_assets", 0) for g in ASSETS["asset_groups"]),
    do_not_reuse_groups=_T["do_not_reuse_group_count"],
    do_not_reuse_obligations=_T["do_not_reuse_obligation_count"])

ARITHMETIC_MS = [
    f"{VISUAL_TOTALS['visual_obligations']} keperluan visual",
    f"tolak {VISUAL_TOTALS['composite_covered']} keperluan yang dipenuhi oleh visual gabungan",
    f"tolak {VISUAL_TOTALS['no_separate_asset']} tajuk pengelompokan yang tidak memerlukan "
    "visual berasingan",
    f"tambah {VISUAL_TOTALS['additional_assets']} aset tambahan yang bukan keperluan visual: "
    "1 lukisan semula rajah enam langkah dan 2 aset senario Slide 2",
    f"bersamaan {VISUAL_TOTALS['proposed_unique_assets']} visual berasingan yang dicadangkan",
]
ARITHMETIC_CHECK = (VISUAL_TOTALS["visual_obligations"] - VISUAL_TOTALS["composite_covered"]
                    - VISUAL_TOTALS["no_separate_asset"] + VISUAL_TOTALS["additional_assets"])

COMPOSITE_DISCLOSURE_MS = (
    "Lima keperluan visual dipenuhi oleh satu visual gabungan yang telah pun menyokong "
    "keperluan lain yang berkaitan. Setiap satu tetap mendapat layanan visual — sebagai panel "
    "berlabel di dalam visual gabungan itu.")
NO_SEPARATE_ASSET_DISCLOSURE_MS = (
    "Tiga tajuk berfungsi sebagai pengelompokan kandungan sahaja dan tidak memerlukan imej "
    "tersendiri. Tajuk-tajuk ini tiada teks kandungan di bawahnya dalam modul.")


# The reviewer gets a CLEAR LABEL, not an internal obligation ID. The brief permits either;
# a label is what a person can act on. The ID stays in the model for traceability.
_GROUP_TOPIC_MS = {"AG-01": "Aliran proses", "AG-02": "Landskap Lembut", "AG-03": "Siram",
                   "AG-04": "Baja", "AG-05": "Racun", "AG-06": "Racun — pematuhan",
                   "AG-07": "Landskap Kejur", "AG-08": "Slide 2"}


def _obl_label(o):
    topic = _GROUP_TOPIC_MS.get(o["proposed_asset_group_id"], "")
    return f"{o['source_heading']} ({topic})" if topic else o["source_heading"]


COMPOSITE_ITEMS = [_obl_label(o) for o in CLOSURE["obligations"]
                   if o["closure_outcome"] == "COVERED_BY_COMPOSITE_ASSET_GROUP"]
NO_SEPARATE_ITEMS = [_obl_label(o) for o in CLOSURE["obligations"]
                     if o["closure_outcome"] == "NOT_A_SEPARATE_ASSET_WITH_REASON"]
DO_NOT_REUSE_ITEMS = [dict(item=_obl_label(o), reason_ms=r)
                      for o, r in ((o, {
                          "T04-VO-025": "Penyimpanan baja (kering, selamat, jauh dari air) "
                                        "berbeza daripada penyimpanan racun (berkunci, "
                                        "berlabel, berpengudaraan).",
                          "T04-VO-026": "PPE untuk baja (sarung tangan, topeng muka) berbeza "
                                        "daripada PPE untuk racun (topeng pernafasan, cermin "
                                        "mata, sarung tangan kimia, sut pelindung).",
                          "T04-VO-040": "Set PPE racun jauh lebih berat dan tidak boleh "
                                        "dikongsi dengan skrin baja.",
                      }.get(o["obligation_id"]))
                          for o in CLOSURE["obligations"] if o["reuse_policy"] == "DO_NOT_REUSE")]

REUSE_QUESTION_MS = ("Selain visual yang telah ditandakan tidak boleh digunakan semula, "
                     "adakah visual lain boleh dikongsi antara lebih daripada satu skrin?")
REUSE_QUESTION_RULE = ("The question must name the known constraints first. An unrestricted "
                       "'adakah visual tertentu boleh digunakan semula?' hides three items "
                       "that are already known not to be shareable.")


_OBL_BY_ID = {o["obligation_id"]: o for o in CLOSURE["obligations"]}


def _asset_groups():
    out = []
    for g in ASSETS["asset_groups"]:
        gid = g["asset_group_id"]
        dnr = g.get("do_not_reuse_obligations", [])
        dnr_labels = [_obl_label(_OBL_BY_ID[x]) for x in dnr]
        out.append(dict(
            item_id=gid,
            item_class="visual_asset_grouping",
            display_title=_AG_LABEL_MS[gid],
            origin_label=_AG_ORIGIN[gid],
            origin_label_ms=ORIGIN_MS[_AG_ORIGIN[gid]],
            obligations_covered=len(g["obligations_covered"]),
            proposed_unique_assets=g["proposed_unique_assets"],
            affected_screens=list(g["affected_screens"]),
            reuse_status=("REUSE_NOT_ALLOWED" if dnr else "REUSE_WITH_CONDITIONS"),
            reuse_status_ms=REUSE_LABELS_MS["REUSE_NOT_ALLOWED" if dnr
                                            else "REUSE_WITH_CONDITIONS"],
            known_restriction_ms=(
                "Tidak boleh dikongsi: " + ", ".join(dnr_labels) if dnr
                else "Tiada sekatan diketahui setakat ini; menunggu pengesahan Bariah."),
            do_not_reuse_obligations=list(dnr),
            content_status=CONTENT_STATUS,
            instructional_authority=INSTRUCTIONAL_AUTHORITY,
            approval_status=APPROVAL_STATUS,
            allowed_decisions=list(DECISIONS_STRUCTURAL),
            allowed_reuse_decisions=list(REUSE_DECISIONS),
            merge=dict(merge_source_id=None, merge_target_id=None, merge_reason=None,
                       proposed_resulting_title_or_group=None),
            reuse_decision=None, decision=None, comment=None,
            source_artifact=SOURCE_ARTIFACTS["visual_asset_grouping"],
            internal_provenance="CAIR grouping proposal over the Bariah-ruled obligation "
                                "population"))
    return out


ASSET_GROUPS = _asset_groups()

# ==========================================================================================
# PART 7 — SLIDE 2 DIALOGUE
# ==========================================================================================
_D = DIALOGUE_SRC["dialogue"]
_F = DIALOGUE_SRC["contextual_fit"]

DIALOGUE_BOUNDARIES = dict(
    level="PROCESS_OVERVIEW_ONLY",
    rules=[
        "process overview only",
        "no statutory obligation in character dialogue",
        "Encik Rahman is not represented as a licensed pesticide operator",
        "no PPE, SDS or chemical-storage instruction in the dialogue",
    ],
    rules_ms=[
        "Perbualan hanya di peringkat gambaran keseluruhan proses.",
        "Tiada kewajipan undang-undang diletakkan dalam dialog watak.",
        "Encik Rahman tidak digambarkan sebagai pengendali racun berlesen.",
        "Tiada arahan PPE, SDS atau penyimpanan bahan kimia dalam dialog.",
    ],
    enforced_in="controlled review model and generated DOCX, not the DOCX alone")

DIALOGUE = dict(
    item_class="slide_2_dialogue",
    screen_id="T04-S02",
    cast=[dict(name="Alya", role_ms="Kontraktor Junior"),
          dict(name="Encik Rahman", role_ms="Mentor / Kontraktor Senior")],
    cast_status="PROPOSED_SUBJECT_TO_BARIAH_APPROVAL",
    cast_status_ms="Draf CAIR untuk semakan Bariah",
    contextual_fit_result=_F["recommendation"],
    contextual_fit_scope_ms="Alya dan Encik Rahman dicadangkan sesuai untuk Slide 2 sahaja.",
    boundaries=DIALOGUE_BOUNDARIES,
    allowed_decisions=list(DECISIONS_CONTENT),
    lines=[dict(item_id=L["dialogue_line_id"], item_class="slide_2_dialogue",
                speaker=L["speaker"], display_text=L["text"],
                content_status=CONTENT_STATUS,
                instructional_authority=INSTRUCTIONAL_AUTHORITY,
                approval_status=APPROVAL_STATUS,
                allowed_decisions=list(DECISIONS_CONTENT),
                decision=None, comment=None,
                source_artifact=SOURCE_ARTIFACTS["slide_2_dialogue"],
                internal_provenance="source rows " + ", ".join(L["source_row_ids"]))
           for L in _D["lines"]])

# ==========================================================================================
# PART 8 — RUMUSAN AND THE CROSS-ITEM DEPENDENCY
# ==========================================================================================
_R = RUMUSAN_SRC["rumusan"]

RUMUSAN = dict(
    item_class="rumusan",
    heading=_R["heading"],
    allowed_decisions=list(DECISIONS_CONTENT),
    points=[dict(item_id=p["point_id"], item_class="rumusan",
                 display_text=p["draft_text"],
                 content_status=CONTENT_STATUS,
                 instructional_authority=INSTRUCTIONAL_AUTHORITY,
                 approval_status=APPROVAL_STATUS,
                 allowed_decisions=list(DECISIONS_CONTENT),
                 risk_flag=("MEDIUM_FACTUAL_RISK"
                            if p["factual_risk_status"].startswith("MEDIUM") else None),
                 risk_flag_secondary=("GENERALISATION_REQUIRES_BARIAH_DECISION"
                                      if p["factual_risk_status"].startswith("MEDIUM")
                                      else None),
                 decision=None, comment=None,
                 source_artifact=SOURCE_ARTIFACTS["rumusan"],
                 internal_provenance="source rows " + ", ".join(p["source_row_ids"]))
            for p in _R["points"]],
    risk_note_item_id="T04-RUM2-04",
    risk_note_ms="Ayat 04 merumuskan corak tanggungjawab kontraktor sebagai satu kenyataan "
                 "umum. Modul menyebut corak ini dalam beberapa bahagian tetapi tidak "
                 "menyatakannya sebagai satu peraturan umum. Mohon Bariah terima, sempitkan "
                 "atau buang ayat ini.")

CROSS_ITEM_DEPENDENCIES = [dict(
    dependency_id="DEP-RUM04-Q5",
    trigger="RUMUSAN_04_EDITED_OR_REMOVED_DUE_TO_OVER_GENERALISATION",
    effect="Q5_REQUIRES_CONSISTENCY_REVIEW",
    from_item="T04-RUM2-04", to_item="Q5",
    automatic_invalidation=False,
    note_ms="Jika ayat 04 dipinda atau dibuang kerana generalisasi terlalu luas, wording Q5 "
            "perlu disemak semula supaya kekal khusus kepada kawalan racun yang dinyatakan "
            "dalam modul.",
    internal_note="Editing or removing Rumusan 04 does NOT invalidate Q5. It triggers a "
                  "consistency review, because both express how broadly contractor duties "
                  "are stated.")]

# ==========================================================================================
# PART 9-10 — QUIZ
# ==========================================================================================
_Q = QUIZ_SRC["quiz"]
try:
    import t04_content_data_v1 as CONTENT
    Q5_DISTRACTOR_REVIEW = CONTENT.Q5_DISTRACTOR_REVIEW
except Exception:  # pragma: no cover
    Q5_DISTRACTOR_REVIEW = None

QUIZ = dict(
    item_class="quiz",
    composition=_Q["composition"],
    composition_ms="4 MCQ dan 1 Multiple Response",
    pass_threshold=_Q["pass_threshold"],
    pass_threshold_ms="Markah lulus 60 peratus",
    scope=_Q["scope"],
    scope_ms="Terpakai kepada semua PL dalam Kursus",
    answer_key_status=_Q["answer_key_status"],
    answer_key_approval=_Q["answer_key_approval"],
    answer_key_ms="Cadangan jawapan sahaja — belum muktamad.",
    allowed_decisions=list(DECISIONS_CONTENT),
    source_evidence_status="SUPPORTED_BY_CONTROLLED_EXTRACT",
    source_evidence_caveat="ORIGINAL_DOCX_ROUND_TRIP_NOT_REPROVEN",
    source_evidence_caveat_placement="internal run manifest and QA report only — not shown to "
                                     "Bariah, where it would read as doubt about the "
                                     "questions rather than a custody note",
    distractor_review=Q5_DISTRACTOR_REVIEW,
    items=[dict(item_id=i["question_id"], item_class="quiz",
                question_type=i["question_type"],
                display_text=i["draft_stem"],
                options=[dict(key=k, text=v,
                              proposed_correct=k in i["proposed_correct_answer"])
                         for k, v in i["draft_options"]],
                proposed_correct_answer=list(i["proposed_correct_answer"]),
                content_status=CONTENT_STATUS,
                instructional_authority=INSTRUCTIONAL_AUTHORITY,
                approval_status=APPROVAL_STATUS,
                allowed_decisions=list(DECISIONS_CONTENT),
                decision=None, comment=None,
                source_artifact=SOURCE_ARTIFACTS["quiz"],
                internal_provenance="source rows " + ", ".join(i["source_row_ids"]),
                internal_answer_evidence=i["correct_answer_evidence"])
           for i in _Q["items"]])

# ==========================================================================================
# PART 1 — DOCUMENT METADATA, INSTRUCTIONS, APPROVALS, FINAL RECORD
# ==========================================================================================
DOCUMENT_METADATA = dict(
    title_ms="PAKEJ SEMAKAN BARIAH",
    subtitle_ms=f"Topik 4: {LESSON_TITLE}",
    unit_line_ms="K5 · PL06 · T04-B01",
    version="v2",
    model_version=MODEL_VERSION,
    stage=STAGE,
    content_status=CONTENT_STATUS,
    instructional_authority=INSTRUCTIONAL_AUTHORITY,
    approval_status=APPROVAL_STATUS,
    opening_disclosure_ms=(
        "Semua kandungan dalam dokumen ini ialah draf CAIR untuk semakan Bariah. "
        "Bariah kekal sebagai satu-satunya Instructional Designer dan pihak yang menyemak, "
        "meminda serta meluluskan kandungan. Storyboard PowerPoint dan aset MMD belum "
        "dihasilkan."),
    status_lines_ms=[
        "Storyboard PowerPoint belum dijana.",
        "Aset visual MMD belum dihasilkan.",
        f"{VISUAL_TOTALS['proposed_unique_assets']} visual dicadangkan — belum diluluskan.",
        "Kelulusan diperlukan bagi perbualan, Rumusan, kuiz, susunan skrin dan kumpulan "
        "visual.",
    ],
    reviewer_name_ms="Bariah",
    reviewer_role_ms="Instructional Designer",
    reviewer_date_field_ms="Tarikh semakan: ____________________________")

REVIEWER_INSTRUCTIONS = dict(
    lines_ms=[
        "Tandakan TERIMA jika item boleh dikekalkan seperti yang dicadangkan.",
        "Tandakan PINDA dan tulis pindaan yang dikehendaki dalam ruang komen.",
        "Tandakan BUANG jika item tidak sepatutnya digunakan.",
        "Tandakan GABUNG hanya untuk skrin atau kumpulan visual, dan WAJIB tulis ID item yang "
        "hendak digabungkan serta sebabnya. Tanpa ID, gabungan tidak boleh dilaksanakan.",
        "GABUNG bermaksud dua item dijadikan satu. Ia berbeza daripada perkongsian visual, "
        "yang mempunyai ruangan tersendiri.",
        "Bagi perbualan, Rumusan dan kuiz, pilihan hanya TERIMA, PINDA atau BUANG.",
    ],
    merge_rule_ms="GABUNG memerlukan ID sasaran. Kotak GABUNG tanpa ID tidak boleh diterima "
                  "sebagai keputusan.")

REMAINING_APPROVALS = [
    dict(item_id="BA-1", title_ms="Watak dan perbualan Slide 2",
         what_ms="Sahkan Alya dan Encik Rahman, kemudian terima, pinda atau ganti lima baris "
                 "perbualan."),
    dict(item_id="BA-2", title_ms="Rumusan — empat ayat",
         what_ms="Terima, pinda atau buang setiap ayat; sahkan penggabungan kepada empat "
                 "ayat."),
    dict(item_id="BA-3", title_ms="Kuiz — lima soalan",
         what_ms="Terima, pinda atau tulis semula soalan, pilihan dan cadangan jawapan."),
    dict(item_id="BA-4", title_ms="Susunan skrin dan kumpulan visual",
         what_ms="Sahkan bentuk 21 skrin dan lapan kumpulan visual, atau cadangkan susunan "
                 "baharu."),
]

FINAL_VERDICT_OPTIONS_MS = ["LULUS TANPA PINDAAN", "LULUS DENGAN PINDAAN DINYATAKAN",
                            "PERLU SEMAKAN SEMULA"]

FINAL_REVIEW_RECORD = dict(
    verdict_options_ms=list(FINAL_VERDICT_OPTIONS_MS),
    single_verdict_block=True,
    single_verdict_note="One verdict block only. The non-governed v1 DOCX carried two "
                        "different verdict vocabularies in one document, which is "
                        "unsignable — a reviewer could tick both and mean different things.",
    reviewer_name_field_ms="Nama penyemak: ____________________________________",
    reviewer_date_field_ms="Tarikh: ____________________________________",
    signature_field_ms="Tandatangan / pengesahan bertulis: "
                       "____________________________________",
    closing_note_ms="Catatan akhir: "
                    "________________________________________________________________")

SECTIONS = [
    dict(section_id="A", title_ms="Cadangan susunan skrin", item_class="screen_sequence"),
    dict(section_id="B", title_ms="Cadangan visual dan kumpulan aset",
         item_class="visual_asset_grouping"),
    dict(section_id="C", title_ms="Perbualan Slide 2", item_class="slide_2_dialogue"),
    dict(section_id="D", title_ms="Rumusan", item_class="rumusan"),
    dict(section_id="E", title_ms="Kuiz", item_class="quiz"),
    dict(section_id="F", title_ms="Keputusan dan pindaan Bariah", item_class="approvals"),
]

PROPOSED_LEARNER_SCREEN_COUNT = SEQ["proposed_learner_screen_count"]
FINAL_LEARNER_SCREEN_COUNT = SEQ["final_learner_screen_count"]

PPTX_GENERATED = 0
GENERATOR_TOUCHED = 0
MMD_PRODUCTION_STARTED = 0


def build():
    return dict(
        model_version=MODEL_VERSION, stage=STAGE, unit_id=UNIT_ID,
        lesson_title=LESSON_TITLE,
        artifact_hierarchy=ARTIFACT_HIERARCHY,
        external_manual_docx=EXTERNAL_MANUAL_DOCX,
        source_artifacts=SOURCE_ARTIFACTS,
        document_metadata=DOCUMENT_METADATA,
        reviewer_instructions=REVIEWER_INSTRUCTIONS,
        decision_vocabulary=dict(content=DECISIONS_CONTENT, structural=DECISIONS_STRUCTURAL,
                                 reuse=REUSE_DECISIONS, labels_ms=DECISION_LABELS_MS,
                                 reuse_labels_ms=REUSE_LABELS_MS, merge_rule=MERGE_RULE),
        sections=SECTIONS,
        screen_sequence=dict(
            proposed_learner_screen_count=PROPOSED_LEARNER_SCREEN_COUNT,
            final_learner_screen_count=FINAL_LEARNER_SCREEN_COUNT,
            treatment_labels_ms=TREATMENT_MS, screens=SCREENS),
        visual_asset_grouping=dict(
            totals=VISUAL_TOTALS, arithmetic_ms=ARITHMETIC_MS,
            arithmetic_check=ARITHMETIC_CHECK,
            authority_statement_ms=AUTHORITY_STATEMENT_MS,
            origin_labels=ORIGIN_LABELS, origin_labels_ms=ORIGIN_MS,
            ag01_seventh_asset=AG01_SEVENTH_ASSET, ag08_scenario=AG08_SCENARIO,
            composite_disclosure_ms=COMPOSITE_DISCLOSURE_MS,
            composite_items=COMPOSITE_ITEMS,
            no_separate_asset_disclosure_ms=NO_SEPARATE_ASSET_DISCLOSURE_MS,
            no_separate_asset_items=NO_SEPARATE_ITEMS,
            do_not_reuse_items=DO_NOT_REUSE_ITEMS,
            reuse_question_ms=REUSE_QUESTION_MS, reuse_question_rule=REUSE_QUESTION_RULE,
            groups=ASSET_GROUPS),
        slide_2_dialogue=DIALOGUE,
        rumusan=RUMUSAN,
        quiz=QUIZ,
        cross_item_dependencies=CROSS_ITEM_DEPENDENCIES,
        remaining_approvals=REMAINING_APPROVALS,
        final_review_record=FINAL_REVIEW_RECORD,
        production_guards=dict(PPTX_GENERATED=PPTX_GENERATED,
                               GENERATOR_TOUCHED=GENERATOR_TOUCHED,
                               MMD_PRODUCTION_STARTED=MMD_PRODUCTION_STARTED))


MODEL = build()


def model_json_text():
    return json.dumps(MODEL, ensure_ascii=False, indent=1) + "\n"


def model_hash():
    return hashlib.sha256(model_json_text().encode("utf-8")).hexdigest()


def reviewable_item_ids():
    """Every item the reviewer can make a decision on, in document order."""
    ids = [s["item_id"] for s in SCREENS]
    ids += [g["item_id"] for g in ASSET_GROUPS]
    ids += [L["item_id"] for L in DIALOGUE["lines"]]
    ids += [p["item_id"] for p in RUMUSAN["points"]]
    ids += [i["item_id"] for i in QUIZ["items"]]
    ids += [a["item_id"] for a in REMAINING_APPROVALS]
    return ids


def emit():
    p = os.path.join(T04, "T04_BARIAH_REVIEW_MODEL_v1.json")
    with open(p, "w", encoding="utf-8") as f:
        f.write(model_json_text())
    return "T04_BARIAH_REVIEW_MODEL_v1.json"


if __name__ == "__main__":
    n = emit()
    print("wrote", n)
    print("model sha256 :", model_hash())
    print("sections     :", len(SECTIONS))
    print("reviewable   :", len(reviewable_item_ids()))
    print("screens      :", len(SCREENS))
    print("asset groups :", len(ASSET_GROUPS))
    print("arithmetic   :", ARITHMETIC_CHECK, "==", VISUAL_TOTALS["proposed_unique_assets"])
