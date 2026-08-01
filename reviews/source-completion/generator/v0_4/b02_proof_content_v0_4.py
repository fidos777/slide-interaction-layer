# -*- coding: utf-8 -*-
"""Controlled content data for the K5 PL06 T03 B02 v0.4 three-family proof.

Frame-screen copy only. Component copy is NOT duplicated here — it is read from the
preserved v0.3 source data (b02_content_v0_3.json), which is the frozen 26-row source
matrix. Architecture, controls, parents, return targets, Notes policy, character
assignment and source locators all come from the frozen model, never from this file.
"""

PL = "PL06: Pengurusan Operasi Pembinaan Landskap"
TOPIC = "Topik 3 Bahagian 2: Komponen Landskap"
COURSE = "KURSUS KERJA BANGUNAN – PEMBINAAN LANDSKAP LUAR"

# ---------------------------------------------------------------- S01
# Spoken transcript is model-owned (spoken_transcript_elements). This is canvas copy only.
S01 = dict(
    canvas_title="Komponen Landskap",
    canvas=[COURSE, PL, TOPIC],
    visual=["ARAHAN VISUAL — SPESIFIKASI SAHAJA",
            "[Visual: Imej pembuka bahagian — foto tapak landskap siap yang",
            "memaparkan struktur taman dan perabot taman dalam satu bingkai.",
            "Tidak dibenamkan.]"],
    button="MULA",
)

# ---------------------------------------------------------------- S02
# Bariah-reviewed dialogue structure. Speakers are the confirmed cast. The MS2680
# sentence is omitted (U-01) and NOT replaced by any other standards claim: Encik
# Rahman's confirmation restates what Alya has already said and adds no new fact.
S02 = dict(
    canvas_title="Pengenalan",
    visual=["ARAHAN VISUAL — SPESIFIKASI SAHAJA",
            "[Visual: Latar tapak landskap dalam pembinaan. Dua watak berdiri di",
            "kawasan yang sudah ditanam, struktur taman di latar belakang.]"],
    cast=[("Alya", "Kontraktor Junior"), ("Encik Rahman", "Mentor / Kontraktor Senior")],
    canvas_note="Dialog penuh dimainkan sebagai video watak. Teks dialog berada dalam Notes.",
    dialogue=[
        ("Alya", "Encik Rahman, lepas kerja tanaman, seterusnya struktur taman dan "
                 "perabot taman. Saya nak sahkan skop sebelum susun jadual."),
        ("Encik Rahman", "Apa yang kamu faham setakat ini?"),
        ("Alya", "Untuk struktur taman, binaan tetap macam gazebo, dek kayu, boardwalk. "
                 "Perabot taman pula, kelengkapan macam kerusi, papan tanda, tong sampah. "
                 "Semuanya ada fungsi, reka bentuk dan spesifikasi bahan tersendiri."),
        ("Encik Rahman", "Betul. Sebab itulah spesifikasi setiap komponen perlu disemak "
                         "dahulu sebelum jadual kerja disusun."),
        ("Alya", "Faham. Saya semak spesifikasi setiap item sebelum mula kerja."),
    ],
)

# ---------------------------------------------------------------- S03
S03 = dict(
    canvas_title="Pengenalan",
    narrator="Hilmi",
    narrator_role="Narator kursus",
    visual=["ARAHAN VISUAL", "[Visual: Kad narator Hilmi — potret separuh badan,",
            "pakaian kerja lapangan, latar tapak landskap kabur.]"],
    groups=["Struktur Taman: Struktur Persisir Air, Struktur Teduhan, Kemudahan Awam, Water Feature",
            "Perabot Taman: Kerusi Taman, Papan Tanda, Tong Sampah, Drinking Fountain, BBQ Pit"],
    mindmap=["ARAHAN VISUAL — MIND MAP (SPESIFIKASI TEKS SAHAJA)",
             "[Visual: Mind Map — nod pusat 'Komponen Landskap' bercabang kepada dua",
             "kumpulan. Cabang 1 – Struktur Taman: Struktur Persisir Air, Struktur",
             "Teduhan, Kemudahan Awam, Water Feature. Cabang 2 – Perabot Taman: Kerusi",
             "Taman, Papan Tanda, Tong Sampah, Drinking Fountain, BBQ Pit. Spesifikasi",
             "teks sahaja — aset Mind Map TIDAK dihasilkan pada peringkat ini.]"],
    reflection=("Jika anda ditugaskan memasang kerusi taman di tepi tasik, apakah jenis "
                "bahan yang anda akan pilih, dan mengapa?"),
    # Hilmi continues the narration established by the Course Montage. No self-introduction.
    vo=("Hilmi: Seperti yang dilihat di halaman sebelum ini, adalah penting untuk anda "
        "memahami tentang struktur taman dan perabot taman yang menjadi sebahagian "
        "daripada kerja pembinaan landskap luar. Anda akan mempelajari tentang struktur "
        "taman, termasuk struktur persisir air, struktur teduhan, kemudahan awam, dan "
        "water feature, serta perabot taman, termasuk kerusi taman, papan tanda, tong "
        "sampah, drinking fountain, dan BBQ pit."),
    vo2="Jika anda ditugaskan memasang kerusi taman di tepi tasik, apakah jenis bahan yang anda akan pilih, dan mengapa?",
)

# ---------------------------------------------------------------- Rumusan
RUMUSAN = dict(
    canvas_title="Rumusan",
    visual=["ARAHAN VISUAL", "[Visual: Papan rumusan — dua kumpulan komponen bersebelahan,",
            "empat dan lima item. Tidak dibenamkan.]"],
    lines=["Mengenal pasti struktur dan elemen landskap - kerja pembinaan, penyeliaan dan "
           "penyelenggaraan dirancang dengan tepat",
           "Struktur Taman - Struktur Persisir Air, Struktur Teduhan, Kemudahan Awam, Water Feature",
           "Perabot Taman - Kerusi Taman, Papan Tanda, Tong Sampah, Drinking Fountain dan BBQ Pit",
           "Kontraktor dapat merancang, melaksana dan menyelenggara setiap komponen landskap "
           "mengikut fungsinya di tapak"],
    vo=("Mengenal pasti struktur dan elemen landskap membolehkan kerja pembinaan, penyeliaan "
        "dan penyelenggaraan dirancang dengan tepat. Struktur taman merangkumi Struktur "
        "Persisir Air, Struktur Teduhan, Kemudahan Awam dan Water Feature, manakala perabot "
        "taman merangkumi Kerusi Taman, Papan Tanda, Tong Sampah, Drinking Fountain dan BBQ "
        "Pit. Dengan memahami komponen-komponen ini, kontraktor dapat merancang, melaksana "
        "dan menyelenggara setiap komponen landskap mengikut fungsinya di tapak."),
)

# ---------------------------------------------------------------- Kuiz
KUIZ_INTRO = dict(
    canvas_title="Kuiz",
    strap="5 soalan — 4 MCQ + 1 Multiple Response   ·   Lulus: 3/5 = 60%",
    purpose=["Tujuan kuiz ini adalah untuk menguji kefahaman semata-mata dan bukan "
             "sebahagian daripada peperiksaan akhir kursus.",
             "Markah tidak akan dinilai sebagai gred peperiksaan akhir kursus."],
    instruction=["Jawab semua soalan dengan pilihan jawapan yang betul.",
                 "Klik butang “MULA KUIZ” untuk mula."],
    button="MULA KUIZ",
    result_controls=["Semak Jawapan", "Ulang Kuiz"],
)

FEEDBACK = dict(
    correct=dict(text="Pilihan jawapan tepat.", sfx="SFX_CORRECT", vo="Pilihan jawapan tepat."),
    incorrect=dict(text="Pilihan jawapan tidak tepat.", sfx="SFX_WRONG", vo="Pilihan jawapan tidak tepat."),
)

Q1 = dict(n=1, kind="MCQ", src="modul ms 238 (3.3.1)",
          stem=("Struktur persisir air dibina di tepi badan air seperti tasik, sungai atau "
                "pantai. Apakah keperluan pembinaan yang paling kritikal bagi struktur ini?"),
          options=[("A", "Warna permukaan yang menarik"),
                   ("B", "Asas yang stabil dan rata dengan saliran permukaan yang berkesan"),
                   ("C", "Ketinggian struktur melebihi dua meter"),
                   ("D", "Penggunaan bahan import")],
          answer="B",
          rationale=("Modul ms 238 menyatakan asas yang sangat stabil dan rata dengan sistem "
                     "saliran permukaan yang berkesan untuk mengelakkan genangan air."))

Q5 = dict(n=5, kind="MULTIPLE_RESPONSE", src="modul ms 242-249 (3.4.1-3.4.3)",
          stem="Pilih SEMUA perabot yang tergolong dalam Perabot Taman.",
          options=["Kerusi Taman", "Papan Tanda", "Boardwalk", "Tong Sampah",
                   "Drinking Fountain", "BBQ Pit", "Gazebo"],
          answers=["Kerusi Taman", "Papan Tanda", "Tong Sampah", "Drinking Fountain", "BBQ Pit"],
          rationale=("Boardwalk ialah struktur persisir air dan Gazebo ialah struktur teduhan; "
                     "kedua-duanya tergolong dalam Struktur Taman, bukan Perabot Taman."))

RESULT = dict(canvas_title="Kuiz — Keputusan",
              sample_score="4 / 5",
              verdicts=["Lulus", "Tidak Lulus"],
              pass_mark="Lulus: 3/5 = 60%",
              controls=["Semak Jawapan", "Ulang Kuiz"],
              vo=("Anda telah melengkapkan kuiz semakan pengetahuan. Anda boleh menyemak "
                  "jawapan atau mengulang kuiz ini."))

Q2 = dict(n=2, kind="MCQ", src="modul ms 239 (3.3.2)",
          stem=("Manakah antara berikut merupakan struktur teduhan tradisional Melayu yang "
                "digunakan sebagai tempat berehat?"),
          options=[("A", "Pergola"), ("B", "Canopy"), ("C", "Wakaf"), ("D", "Gazebo")],
          answer="C",
          rationale=("Modul ms 239 menyenaraikan Wakaf sebagai struktur teduhan tradisional "
                     "Melayu. Pergola, Canopy dan Gazebo turut disenaraikan sebagai struktur "
                     "teduhan, tetapi bukan sebagai bentuk tradisional Melayu."))

Q3 = dict(n=3, kind="MCQ", src="modul ms 240 (3.3.3)",
          stem=("Apakah pertimbangan utama dalam pemilihan bahan bagi kemudahan awam seperti "
                "tandas dan surau di taman?"),
          options=[("A", "Bahan yang tahan vandalisme dan cuaca"),
                   ("B", "Bahan yang paling murah di pasaran"),
                   ("C", "Bahan yang perlu dicat semula setiap bulan"),
                   ("D", "Bahan yang seragam dengan perabot taman")],
          answer="A",
          rationale=("Modul ms 240 menetapkan ketahanan terhadap vandalisme dan cuaca sebagai "
                     "pertimbangan utama bagi kemudahan awam."))

Q4 = dict(n=4, kind="MCQ", src="modul ms 241 (3.3.4)",
          stem=("Dalam pembinaan water feature, apakah aspek kawalan kualiti air yang "
                "dinyatakan dalam modul?"),
          options=[("A", "Penambahan garam"), ("B", "Pencegahan alga"),
                   ("C", "Pemanasan air"), ("D", "Pewarnaan air")],
          answer="B",
          rationale=("Modul ms 241 menyatakan pencegahan alga sebagai aspek kawalan kualiti air "
                     "bagi water feature."))

QUESTIONS = {1: Q1, 2: Q2, 3: Q3, 4: Q4, 5: Q5}

REVIEW = dict(canvas_title="Semak Jawapan",
              intro="Semakan jawapan bagi kelima-lima soalan.",
              note=("Rasional terperinci bagi setiap soalan kekal sebagai metadata produksi "
                    "sehingga penempatan akhirnya disahkan."),
              vo="")

# ---------------------------------------------------------------- Tamat
TAMAT = dict(
    canvas_title="Tamat Topik 3 Bahagian 2: Komponen Landskap",
    canvas=[COURSE, PL],
    status="Bahagian ini telah selesai.",
    instruction="Tutup tetingkap pelajaran untuk keluar.",
    vo=("Tamat Topik 3 Bahagian 2: Komponen Landskap. Bahagian ini telah selesai. "
        "Tutup tetingkap pelajaran untuk keluar."),
)

# ---------------------------------------------------------------- rich text
# Approved English-origin terms italicised on canvas, Notes, popups, Rumusan, Kuiz, Tamat.
# Longest-first so "Wood-Plastic Composite" wins over any shorter overlap.
ITALIC_TERMS = ["Wood-Plastic Composite", "Drinking Fountain", "Water Feature", "BBQ Pit"]

# Never italicised even though they are English-looking: production IDs and metadata.
NEVER_ITALIC_PREFIXES = ("K5-PL06", "K5PL06", "SCR_", "ST_", "II_", "RP-", "B02-", "SFX_")
