# Kekangan Reka Bentuk Sistem — Skala ke Ribuan Pengalaman Pembelajaran
**Sasaran repo:** `slide-interaction-layer/reviews/SCALING-CONSTRAINTS-v0.md` · Tarikh: 5 Julai 2026
**Seni bina:** Studio Courseware (keputusan produksi ID/MMD) · slide-interaction-layer (taxonomy/ADR/rules/templates) · React SCORM Player (laksana kontrak RESOLVED/LOCKED sahaja)
**Prinsip skala:** pada ribuan pengalaman, **taxonomy kekal O(puluhan), binding tumbuh O(ribuan)** — sistem scale jika dan hanya jika kos per-binding hampir sifar untuk kes biasa, dan perhatian manusia dibelanjakan HANYA pada ambiguity tulen.

---

## 1. Interfaces — lima sempadan, setiap satu satu dokumen kecil (semua SUDAH wujud)

| IF | Sempadan | Kontrak | Arah |
|---|---|---|---|
| IF-1 | Studio/CAIR → taxonomy | CAIR-OUTPUT-CONTRACT: enum tertutup `jenis_taxonomy` + `TIADA-PADANAN` + objek atomik | Studio **mencadang, tak pernah menamakan** |
| IF-2 | slide-interaction-layer → permukaan keputusan Studio/SME | Projection melalui galeri/kad SAHAJA (`sme_visible`); kelas dalaman tak pernah dipapar sebagai beban keputusan; **kad = satu-satunya saluran soalan** ke SME, satu artifak satu keputusan | Taxonomy menterjemah TURUN, bukan SME belajar NAIK |
| IF-3 | binding → player config | `{pattern, variant, row_id}` dengan status ∈ {RESOLVED, LOCKED}; config bawa rujukan `row_id` | Player **laksana, tak pernah mentafsir** |
| IF-4 | player → LMS | `lms_emit` eksplisit; hanya μB `score-report-LMS` / `completion-report-LMS` menulis ke cmi; segala gate lain = state lokal | Emisi diisytihar, tak pernah dianggap |
| IF-5 | versi taxonomy → semua artifak | Setiap artifak pin `taxonomy_version + md5`; tiada artifak sah terhadap "taxonomy" — hanya terhadap "taxonomy@md5" | Kanon mengalir ke bawah sahaja |

Penemuan penting (diperhalusi): **skala tidak memerlukan sempadan interface baru** — kelima-lima sempadan wujud. IF-1/3/4/5 disokong dokumen penuh; **IF-2 lengkap hanya selepas dua artifak kecil stabil: Alias Glossary (`lexicon/ALIAS-GLOSSARY-v0.md`) + Pattern Gallery.** SME tak pernah consume dokumen taxonomy — laluan sebenar: taxonomy → galeri/kad → permukaan keputusan SME. Kerja skala = menguatkuasakan dan melengkapkan yang sedia ada, bukan menambah.

## 2. Invariants — mesti kekal benar pada SEBARANG saiz

| INV | Kenyataan | Bentuk operasi |
|---|---|---|
| INV-1 | **Entri tumbuh sublinear terhadap pengalaman** | Entri baru HANYA jika topology baru atau kelas μB baru (ujian keahlian); varian = koordinat, bukan entri. N behaviour × M presentation = N+M, bukan N×M |
| INV-2 | **Registry μB tertutup** | Penambahan = mini-ADR sahaja. Registry ~20–30 μB ialah aset skala sebenar — bukan senarai pattern |
| INV-3 | **Satu kanon per versi** | Satu fail, satu md5; edit taxonomy = batch berversi (cth v0.2→v0.3), bukan titisan harian |
| INV-4 | **Provenance monotonik** | Status hanya naik (DRAFT→RESOLVED→LOCKED) melalui aktor manusia direkod (`decided_by`); RESOLVED ≠ LOCKED; demosi tak pernah senyap |
| INV-5 | **Nama tak mengalir ke belakang** | Vocabulary implementasi (nama komponen) tak pernah muncul dalam lapisan SME/binding; lapisan `alias_kontrak` menyerap bahasa client/kontrak |
| INV-6 | **Traceability dua hala** | Setiap elemen config player → satu `row_id` binding; setiap baris binding → fail sumber + md5. Rantai putus = BLOCKED |
| INV-7 | **Siling kognitif SME** | Pilihan SME-visible ≤ ~10–12; satu artifak satu keputusan. Bandwidth manusia ialah sumber TETAP — taxonomy mesti memampat ke arahnya, bukan mengembang |
| INV-8 | **Emisi LMS eksplisit** | `tracking` dalam binding = calon; emisi sebenar = config `lms_emit` + bukti G6. Gate ≠ emisi, selamanya |

## 3. Trade-offs — kos jujur kekangan ini

| Trade-off | Kos diterima | Kenapa berbaloi |
|---|---|---|
| Cukai binding eksplisit vs drift | Setiap token ambiguous = satu keputusan manusia SEKARANG | Alternatif (auto-bind) = rework + hakisan trust KEMUDIAN. Laluan amortisasi sudah ditulis: lexicon terkumpul → PROPOSE-by-default (trigger ≥30 baris LOCKED stabil) — keselamatan dulu, automasi kemudian, tak pernah kedua-dua serentak |
| Registry tertutup vs ekspresif | Idea pedagogi baru kadang-kadang lewat di belakang mini-ADR | Latency sekali-sekala < letupan kekal. Terima latency |
| Kanon-per-versi vs kelincahan | Bump versi ada upacara (md5, batch, re-pin) | Tanpa upacara: divergence kelas footer-v0.2 / CSV-05 berulang pada skala ribuan — tak boleh pulih |
| Projection vs pemahaman kongsi | SME tak pernah belajar model dalaman → seluruh beban terjemahan di sisi desk | Sengaja: kerja Bariah = pedagogi, bukan taxonomy. Akibat: desk = bottleneck → UKUR minit-dokumentasi per kad, jangan andaikan murah |
| Golden fixture G6 per pattern vs kelajuan | Kos setup fixture per entri LOCKED | Satu-satunya pertahanan regression pada komponen G6-proven bila volume naik |
| Komponen hardcoded vs composition engine | Setiap pattern baru = kerja komponen manual | Hardcoded menang sehingga demand pattern berulang kali melebihi kapasiti — itulah gate v2, bukan tarikh |

## 4. Failure modes — dengan isyarat pengesanan yang SUDAH diukur

| FM | Mod kegagalan | Isyarat (dari metrik/log sedia ada) | Nota |
|---|---|---|---|
| FM-1 | Letupan taxonomy | New-pattern demand >2 per deck BERULANG; dropdown SME >12 | Punca lazim: ujian keahlian tak dikuatkuasa, atau presentation jadi entri |
| FM-2 | Bypass vocabulary oleh tooling sendiri | Nama bukan-kanon muncul TANPA baris log RS. **Isyarat TIADA-PADANAN ada DUA bacaan — jangan campur:** (a) TIADA-PADANAN atas **vocabulary kontrak yang sah** = jurang kanon → ubat: patch taxonomy (preseden: "Scenario with Questions", review r1 — penjana TIDAK bersalah); (b) TIADA-PADANAN atas **vocabulary liar/tak diverifikasi** = FM-2 sebenar → ubat: polis penjana (contoh hidup: "Reflection") | Kiraan insiden dikoreksi: **1× confirmed pada kategori (b)** [skill generik P0–P8 — inferred, fail insiden belum dijumpai dalam repo; sahkan atau turunkan]. Insiden "penjana CAIR" DIKELUARKAN dari FM-2 — ia kategori (a), kesilapan kanon kita sendiri. Kelas ancaman #1 kekal tooling dalaman, tetapi tindakbalas mesti ikut bacaan yang betul — polis penjana atas jurang kanon = tindakan salah |
| FM-3 | Inflasi status senyap | `decided_by` tak sepadan aktor; baris LOCKED tanpa kad/prov_ref | Audit kolum, bukan audit ingatan |
| FM-4 | Beban SME melimpah | Load kad per sesi naik; kadar pembalikan naik; peristiwa "pening" | "Pening" = kegagalan format artifak, bukan kegagalan SME |
| FM-5 | Ambiguity SCORM | Config `lms_emit` tak sepadan cmi yang diperhatikan dalam G6; dakwaan completion tanpa bukti traversal | INV-8 dilanggar |
| FM-6 | Divergence kanon | md5 tak sepadan pada mula pass; export tak lulus banding objek-demi-objek dengan JSON | **Sudah berlaku 2×** (footer taxonomy ×2 salinan; CSV 05) — semakan md5 langkah-0 ialah pengesan termurah dalam sistem |
| FM-7 | Bottleneck compiler-manusia | Baris AMBIGUOUS berusia dalam queue; satu pelulus untuk semua binding | Laluan mitigasi sudah ditulis (checklist boleh-delegasi + trigger pelulus kedua) — jangan bina awal, tapi JEJAK usia queue dari sekarang |

## 5. Anti-overbuild rules

**Meta-peraturan:** bina di sesuatu sempadan HANYA selepas mod kegagalan di sempadan itu benar-benar menyala, dengan bukti trigger direkod. Set kekangan §1–§2 sengaja **scale-invariant** — sebab itulah tiada apa perlu pra-bina untuk "ribuan".

Senarai gate sedia ada kekal berkuat kuasa (rujuk RELEASE-GATE-PATCH-AND-OPS §3): auto-mapper (tiada trigger — fix di punca) · validator berskrip/servis (>~3 deck per kitaran DAN ralat kontrak berulang) · penguatkuasaan keras player (pelulus kedua ATAU gate manual gagal 1× sebenar) · sidecar YAML (pengguna mesin pertama) · composition engine (gate v2: ≥2 instance berbayar) · dashboard (Branching LOCKED + client minta laporan laluan) · registry penuh (>2 pattern baru dari coverage sebenar, atau vertical kedua) · SaaS (≥2 instance berbayar × ≥2 vertical — Kad Tangkap-Pattern).

Tambahan khusus skala: **jangan bina untuk "ribuan" semasa berjalan pada "puluhan"** — bukti bahawa kekangan bertahan pada 1 deck (pass K4) → 3 deck → 1 kursus penuh ialah tangga naiknya, bukan lompatan seni bina.

## 6. Next smallest production artifact

**`lexicon/ALIAS-GLOSSARY-v0.md` — satu muka.**

Sebab ia yang seterusnya, bukan pilihan lain: patch v0.3 baru sahaja memperkenalkan medan `alias_kontrak` yang ditakrifkan sebagai "vocabulary kontrak SnG **yang diluluskan**" — tetapi **tiada senarai kanon alias yang diluluskan wujud di mana-mana**. Itu rujukan tergantung dalam kontrak yang baru dipatch. Artifak terkecil seterusnya menutupnya:

```
| alias_kontrak (SnG)   | nama kanon taxonomy    | jenis_asal_sistem dikenali | provenance |
|-----------------------|------------------------|-----------------------------|------------|
| Click and Show        | Gated Click & Reveal   | Click-and-Show              | v0.3       |
| Drag and Drop         | Drag & Drop            | Drag-and-Drop               | v0.3       |
| Scenario with Questions| Scenario with Questions| Scenario with Questions     | v0.3       |
```

Ia juga instrumen skala IF-1/IF-2: ribuan pengalaman = berbilang kontrak (SnG sekarang, lain kemudian), setiap satu dengan vocabulary sendiri — glosari per-kontrak ialah cara lapisan-2 tumbuh tanpa menyentuh kanon lapisan-1. Dan ia bahan mentah langsung untuk PROPOSE-by-default kelak: automasi binding dibina atas glosari yang terbukti, bukan atas tekaan.

## 7. Log penolakan governance (semakan 05/07/2026)

*Tolak-tanpa-log = tak berlaku — peraturan sama dengan log RS binding, diangkat ke peringkat governance.*

| GRS-id | Cadangan | Sumber | Keputusan & sebab |
|---|---|---|---|
| GRS-001 | `interaction-spec.md` — artifak "hasil akhir CAIR" (Pattern/Intent/Evidence/Tracking/Player/Fallback) sebagai input terus ke React generator/QA | Dokumen falsafah "contract artifact" 05/07 §8 | **DITOLAK.** Tiga pelanggaran terhadap invariant sistem sendiri: (1) medan `Player: Branching Player` = nama implementasi dalam lapisan spec → langgar INV-5; (2) medan `Fallback` pra-mengizinkan substitusi pattern tanpa keputusan SME → demosi senyap, langgar INV-4; (3) duplikasi IF-3 (binding → player config) → langgar one-decision-one-place, dan meta-peraturan §5 (IF-3 belum pernah gagal — belum pernah berjalan pun). Bahagian yang DISIMPAN dari dokumen sama: ayat doktrin di bawah |

**Doktrin diterima (dari sumber sama, diasingkan dari cadangan yang ditolak):**
*Moat bukan pada artifact tunggal — moat ialah rangkaian artifact yang saling
menguatkuasakan. Salin satu fail belum dapat sistem; sistem ialah keseluruhan
rangkaian kontrak.* Corollary penguatkuasaan: rangkaian yang merujuk nod hantu
bukan rangkaian — setiap rujukan mesti resolve ke fail dalam repo (PR-001 kini
dirujuk 4 fail tanpa wujud: wujudkan atau isytihar mati).

**Status governance (direkod, keputusan milik Firdaus):** cadangan reviewer =
**governance freeze** — tiada fail rules/contract/constraints baharu sehingga
(a) full slide pass pertama siap DAN (b) ≥1 baris binding mencapai LOCKED
melalui kad sebenar. Rasional: nisbah artifak-governance kepada bukti-empirik
kini ±13 : 1-pass-proxy : 0-LOCKED — peraturan mesti tumbuh sublinear terhadap
pass (aplikasi §5 pada governance sendiri). Patch pembetulan pada fail sedia
ada dikecualikan dari freeze; fail BARU tidak.

---
*Lima interface (sempadan wujud; IF-2 menunggu galeri) · lapan invariant ·
tujuh mod kegagalan berisyarat · log penolakan governance aktif.
Skala ialah penguatkuasaan, bukan pembinaan. Finish. Package. Close.*
