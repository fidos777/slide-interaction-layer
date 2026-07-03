# FINDING — Percanggahan PRD Bariah vs Storyboard M1 K4
### Direkod, BELUM diselesaikan. Jana semula DITANGGUH sehingga arahan lanjut.

---

## PROVENANS

- **PRD sumber:** `PRD_ELearning_Storyboard_Process.docx`, md5 `0bc926fe41089e90e6da34956e30aa33`
- **Status:** Draft v1.0, rekod proses SEBENAR — Bariah + sesi Claude lain, PL01 Topik 1-4 dah dihasilkan
- **Storyboard M1 sesi ini:** `SB_K4PL1T1_DRAF_v1.pptx`, `SB_K4PL1T2T3_DRAF_v1.pptx` — dijana SEBELUM PRD didedahkan

---

## KEPUTUSAN DIREKOD (03/07/2026, sesi ini)

1. ✅ **Watak K4 Suresh/Danish DITARIK BALIK.** Kanon K4 ikut PRD Bariah:
   - **Amir** — perantis (dari Haziq), mula muncul Topik 3
   - **Encik Zul** — mentor/OK (dari Roslan), mula muncul Topik 3
   - **Maya** — narrator dedicated, muncul dari Topik 1
   - **Encik Danial** — komersial/tender (sekunder, ikut keperluan topik)
   - **Puan Sarah** — HR/safety (sekunder, ikut keperluan topik)

2. ✅ **QA file-integrity (checklist PRD Seksyen 9.3) — DITANGGUH.** Tidak dijalankan pada 3 pptx M1 sekarang. PRD kekal rujukan.

3. ✅ **Jana semula 3 storyboard — DITANGGUH.** Percanggahan direkod dulu (dokumen ini), tiada pembetulan fail dijalankan sekarang.

---

## STATUS ARTIFAK SEDIA ADA (SELEPAS keputusan #1 di atas)

| Fail | Status |
|---|---|
| `SB_K4PL1T1_DRAF_v1.pptx` | ⚠️ **BASI** — scenario slide 2 guna Suresh+Danish (ditarik balik). Struktur 8-slide tak padan corak PRD (2-slide Pengenalan). |
| `SB_K4PL1T2T3_DRAF_v1.pptx` | ⚠️ **BASI** — sama isu, T2 & T3. Tambahan: PRD kata Topik 1-2 = **Maya sahaja** (tiada watak scene) — T2 storyboard M1 ada watak scene, ini juga tak padan. |
| `konsep_id_desk_slides.html` | ✅ Selamat — tiada nama watak spesifik disebut |
| ASCII map / visualizer inline (sesi terdahulu) | ✅ Selamat — tiada nama watak spesifik disebut |

**Jangan hantar `SB_K4PL1T1_DRAF_v1.pptx` atau `SB_K4PL1T2T3_DRAF_v1.pptx` ke Bariah dalam keadaan sekarang** — watak & struktur tak padan proses rasmi dia sendiri. Ini boleh mengelirukan atau nampak tak profesional (dia akan nampak sistem "tak baca" kerja dia sendiri).

---

## PERCANGGAHAN PENUH — PRD Bariah vs Rekod Sesi Ini

| Perkara | Rekod sesi ini (SEBELUM PRD) | PRD Bariah (verified, proses sebenar) | Status |
|---|---|---|---|
| Watak mentor K4 | Encik Suresh (India) | **Encik Zul** | ✅ Diselesaikan — ikut PRD |
| Watak perantis K4 | Danish (Melayu) | **Amir** | ✅ Diselesaikan — ikut PRD |
| Narrator K4 | Hilmi / Maya (dua sumber bercanggah) | **Maya** (dedicated, bukan Hilmi) | ✅ Diselesaikan — ikut PRD |
| Watak sekunder | Tak dibincang | **Encik Danial** (komersial), **Puan Sarah** (HR/safety) | Baru — belum masuk mana-mana storyboard |
| Struktur Pengenalan | 8 slide (T1/T2/T3 storyboard M1) | **2 slide**: Video Situasi + Narrator gabung (reflection+overview) | ⬜ **BELUM diselesaikan** |
| Watak scene Topik 1-2 | Ada (Suresh+Danish dalam T1, T2) | **TIADA** — Maya narration sahaja, sebab "tiada konflik tempat kerja semula jadi untuk didramakan" | ⬜ **BELUM diselesaikan** |
| Watak scene mula Topik | Semua topik ada scenario watak | Mula **Topik 3** (Orang Kompeten) — "hook organik: status OK = siapa layak buat kerja" | ⬜ **BELUM diselesaikan** |
| Bilangan Topik PL01 | 20 Topik (dari jadual SUB MODUL, md5-lock, sesi lalu) | "Topik 1 through Topik 4" (skop in-scope PRD) | ⬜ **BELUM di-drill** — tak pasti 4 ini sepadan 4 daripada 5/20 SUB MODUL, atau skema lain |
| Format kuiz | 5 soalan (draf umum) | **5 soalan spesifik**: 4 single-answer + 1 multiple-response ("pilih SEMUA jawapan betul") | ⬜ **BELUM diselesaikan** |
| Kaedah QA fail | Render soffice + tengok imej (QA visual) | **QA dua lapisan**: content QA + file-integrity QA (schema, creationId, app.xml, custom tag part) | ⬜ **BELUM dijalankan** — checklist PRD Seksyen 9.3 tak pernah run pada fail M1 |
| Kaedah jana pptx | `pptxgenjs` (fresh-build dari kod) | `python-pptx` atas OOXML unpack/duplicate/repack sumber Waterproofing | Beza kaedah asas — tak semestinya isu sama (pptxgenjs elak deep-copy shape), tapi belum disahkan selamat |

---

## SOALAN TERBUKA — perlu keputusan sebelum jana semula (bila diarah)

1. **20 Topik (SUB MODUL) vs "Topik 1-4" PRD** — adakah 4 ini subset dari 5 SUB MODUL PL01 yang sama, atau PRD guna skema pembahagian berbeza? Perlu drill-baca PRD lawan jadual SUB MODUL K4 sebelum jana apa-apa lagi. **Belum dibuat dalam sesi ini.**

2. **Granularity keseluruhan** — PRD ni tulis untuk PL01 sahaja ("PL02 dan modul seterusnya... tidak bermula lagi"). Jadi PRD **tidak** jawab soalan granularity K4 keseluruhan (5 vs 20) yang masih tergantung dari sesi CAIR desk. Ini kekal soalan Bariah berasingan.

3. **Struktur 2-slide vs 8-slide** — kalau diputuskan ikut PRD, storyboard M1 T1/T2/T3 kena dibina semula dari asas (bukan sekadar tukar nama watak dalam fail sedia ada).

4. **Topik 1-2 tanpa watak scene** — kalau ikut PRD, slide "Pengenalan Scenario" untuk T1 (Definisi) dan T2 (Akta) sepatutnya **buang** dialog Amir/Zul, gantikan dengan narration Maya sahaja. Ini ubah nada & pendekatan storyboard, bukan sekadar label watak.

---

## TINDAKAN SETERUSNYA (menunggu arahan)

Tiada tindakan automatik. Pilihan yang masih terbuka untuk sesi akan datang:

- **A** — Drill PRD lawan jadual SUB MODUL K4 dulu (soalan terbuka #1), sebelum apa-apa jana semula.
- **B** — Jana semula penuh (watak + struktur 2-slide + T1/T2 tanpa watak scene) ikut PRD, terima 4-Topik PRD sebagai skop semasa tanpa drill lanjut dulu.
- **C** — Bawa percanggahan ni terus ke Bariah/Firdaus sebagai satu set soalan binary, tunggu arahan sebelum sentuh fail.

*Dokumen ini snapshot keputusan & percanggahan setakat 03/07/2026. Tiada fail storyboard diubah selepas rekod ini dibuat.*

---
## ADDENDUM (03/07/2026, selepas meeting Bariah)
- Keputusan #1 (kanon watak) DISAHKAN Bariah secara lisan dalam meeting 03/07 — status: ratified.
- Storyboard M1 (2 pptx) diisytihar SUPERSEDED oleh lane produksi Bariah (PL01 T1-T4 siap ikut PRD). TIDAK dijana semula.
- Sasaran pipeline seterusnya: T5 + PL02-05, mematuhi struktur PRD.
- PRD asal belum dalam simpanan kita — menunggu dari Bariah (peringatan aktif). Lokasi pptx superseded: lihat bawah.

**Lokasi arkib pptx superseded:** `~/Archive/CIDB_superseded_20260703/` (di luar git — binari mati, tidak di-commit).
**Nota ketepatan (03/07):** hanya **1 daripada 2** pptx dijumpai & diarkib — `SB_K4PL1T1_DRAF_v1.pptx`. `SB_K4PL1T2T3_DRAF_v1.pptx` **tidak wujud** di ~/Downloads, ~/Documents, ~/Desktop mahupun mana-mana dalam ~ (disahkan grep 03/07). Jika ia muncul kemudian, arkibkan ke folder sama.
