# SOP — Cold-Coverage Pass v0
**Sasaran repo:** `sop/COLD-COVERAGE-PASS-v0.md` · Skop: SATU deck / SATU PL per pass.

## Tujuan
Uji secara empirik sama ada taxonomy v0 "scale tanpa explode": bolehkah setiap momen interaksi dalam satu deck sebenar diungkap sebagai komposisi/varian sedia ada, tanpa entri baru? Output: jadual binding terisi + enam metrik + laporan satu muka.

## Langkah 0 — Precondition keras (JANGAN mula tanpa semua ✓)
- [ ] PR-001 wujud dalam repo DAN dimuat oleh AI worker — **jika tidak, jangan mula: risiko table tercemar klasifikasi generik dari baris pertama**
- [ ] Taxonomy v0.2 salinan kanon dipilih (footer "mesti berqualifier"), md5 direkod dalam metadata jadual
- [ ] Fail binding dicipta dari `binding/BINDING-TABLE-TEMPLATE-v0.md`, seksyen contoh dipadam
- [ ] Deck sasaran dipilih oleh Firdaus (AMEND-K1 atau satu PL K4)

## Input
1. Taxonomy v0.2 kanon (md5 direkod)
2. Deck sasaran (PPTX + nota mentah)
3. Menu konversi POP UP + glosari/lexicon Bariah
4. PR-001
5. `templates/CLARIFICATION-CARDS-v0.md`

## Peranan
| Peranan | Buat | TIDAK buat |
|---|---|---|
| AI worker | Enumerasi, draf, klasifikasi, metrik, stub kad | Binding muktamad token ambiguous; sentuh taxonomy |
| Firdaus | Semak, RESOLVED, pilih verb ADR-006, jalankan kad | Isi draf pukal (kerja AI) |
| Bariah | Jawab kad sahaja | Tak nampak jadual, kelas, atau jargon |

## Aliran kerja
| # | Langkah | Siapa | Output |
|---|---|---|---|
| 1 | Enumerasi: satu baris per token SB interaktif per slide; `sb_token` verbatim; momen enjin tanpa token SB → baris IMPL-ONLY | AI | jadual tanpa status |
| 2 | Draf: isi `grammar`, `sb_context`, `kelas`, `proposed_binding` melalui checklist klasifikasi; semua → `DRAFT`; token ambiguous → `AMBIGUOUS` + calon + `ambiguity_reason` + stub kad | AI | jadual DRAFT |
| 3 | Kira metrik pusingan-1 (formula bawah) | AI | blok metrik terisi |
| 4 | Semakan penuh: DRAFT → RESOLVED / betulkan / sahkan AMBIGUOUS; pilih verb per baris AMBIGUOUS (ASK / PROPOSE / WAIT) | Firdaus | jadual disemak + queue |
| 5 | Sesi kad dengan Bariah — satu artifak satu keputusan, ikut queue (blocking dulu); jawapan verbatim → `prov_ref`; baris → LOCKED | Firdaus + Bariah | baris LOCKED |
| 6 | Metrik pusingan-2 + laporan coverage satu muka (enam nombor + verdict ambang) | AI draf, Firdaus sah | laporan |

## Sempadan inferens AI worker
**BOLEH infer:** koordinat grammar dari deskripsi SB · senarai calon dari menu konversi · ciri kandungan (panjang teks, VO) · IMPL-ONLY untuk perkara tak nampak learner · padanan DUPLICATE.

**TIDAK BOLEH infer (hard stop):**
1. Binding muktamad token ambiguous (POP UP tanpa qualifier, "branching" tanpa qualifier, kata kerja tak dikenali)
2. Niat SME melebihi teks verbatim
3. Penciptaan pattern/μB baru — hanya CADANG melalui mini-ADR
4. Perubahan pada entri LOCKED atau komponen G6-proven
5. Ketiadaan sebutan = ketiadaan requirement (guard Bitumen-Sheet)

**Wajib pengesahan manusia:** AMBIGUOUS→RESOLVED (Firdaus) · RESOLVED→LOCKED (jawapan Bariah bertulis) · setiap cadangan P/T2/μB baru · setiap baris sentuh G6-proven · REJECTED yang melibatkan token SB sebenar.

## Metrik & formula
Asas: `N_total` = SEMUA baris jadual kerja termasuk baris audit; `N_int` = N_total − (IMPL-ONLY + REJECTED + DUPLICATE). Formula penuh + nota coverage: rujuk blok metrik template — **template ialah sumber kanon formula; jika fail ini dan template bercanggah, template menang.**

| Metrik | Formula | Ambang |
|---|---|---|
| Coverage % | baris INTERACTION map ke komposisi/varian SUDAH WUJUD dalam taxonomy v0.2, tanpa calon P-baru/T2-baru ÷ N_int. DEFERRED covered hanya jika binding wujud dalam v0.2. Coverage ≠ buildability | ≥ 80% |
| New-pattern demand | baris P-baru/T2 belum dalam taxonomy | ≤ 2 |
| Ambiguity rate | AMBIGUOUS ÷ N_int, selepas draf AI sebelum kad | ≤ 30% |
| Implementation-only rate | IMPL-ONLY ÷ N_total | kalibrasi sahaja |
| Tracking-required rate | (tracking ≠ none) ÷ N_int | input G6 sahaja |
| SME-clarification load | bilangan kad dihantar | ≤ 2 sesi |

## Stop conditions — mana-mana satu = BERHENTI, nilai semula, jangan tambah entri untuk "lulus"
- Coverage < 80% → paksi grammar salah / set μB kecil — masalah struktur
- Demand > 2 → grammar hilang satu topology — semak sebelum terima pattern baru
- Ambiguity > 50% → lexicon nipis — kerja hulu G1–G3, bukan kerja taxonomy
- Bariah balas "pening" pada mana-mana kad → format kad gagal — baiki kad, bukan Bariah
- IMPL-ONLY tinggi tak dijangka → kriteria enumerasi kabur — perjelas Langkah 1

## Output
1. `binding/<DECK>-binding-v0.md` terisi (jadual + metrik + log RS)
2. Kad klarifikasi terhantar + jawapan direkod
3. Laporan coverage satu muka (enam nombor, verdict ambang, senarai baris LOCKED baru)

## Definition of done
- [ ] Setiap baris ada `binding_status` + `row_disposition`
- [ ] Sifar baris `DRAFT` tinggal (semua RESOLVED / LOCKED / DEFERRED / dilupuskan)
- [ ] Semua AMBIGUOUS sama ada di-LOCK melalui kad ATAU direkod sebagai kelas WAIT dengan sebab
- [ ] Enam metrik dikira dua pusingan
- [ ] Log RS lengkap
- [ ] Laporan satu muka disahkan Firdaus
- [ ] Fail taxonomy TIDAK berubah (md5 sama seperti metadata)
