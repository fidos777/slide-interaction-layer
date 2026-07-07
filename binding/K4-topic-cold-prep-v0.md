# K4 Topic-Level Cold-Prep Pass v0 — Pusingan 1 (draf AI)
**Sasaran repo:** `binding/K4-topic-cold-prep-v0.md` · **BUKAN full slide cold-coverage pass** — lihat §2.

## 1. Metadata

| Medan | Nilai |
|---|---|
| Pass | **K4 Topic-Level Cold-Prep v0** — pusingan 1 (draf AI, belum semakan Firdaus) |
| Sumber utama | `k4_topik_data.json` · md5 `420e1a63e153b36213af5b1cab025748` |
| Sumber DOCX asal | `K4__PROOFREAD_FINAL__SKP_2025_LIF__ESKALATOR___LALUAN_GERAK_300426.docx` · md5 `f8a58d5ffe172be66102a0b99df23c5b` (dari medan `source_md5` JSON) |
| CSV | 04: md5 `212c8724…` · 05: md5 `f713859a…` — **kedua-dua supplementary sahaja; 05 ROSAK, lihat OPEN-K4-a** |
| Taxonomy | v0.2 salinan kanon · md5 `<isi selepas fix salinan kanon di mesin Firdaus>` |
| Reviewer | Firdaus |
| Tarikh | 5 Julai 2026 |
| Gate PRD Bariah | **Andaian direkod, belum disahkan:** pass ini klasifikasi pra-kerja, bukan penciptaan kandungan K4 → dianggap terkecuali dari gate GET-DOC PRD. Firdaus sahkan atau batalkan (OPEN-K4-c). GET-DOC PRD kekal WAJIB sebelum kerja kandungan K4 sebenar |
| Nota ambang | PL dipilih atas decision density — ambiguity dijangka tinggi secara reka bentuk; interpretasi stop condition dengan konteks ini |

## 2. Skop — apa pass ini boleh dan tak boleh claim

| ✓ Boleh claim | ✗ TAK boleh claim |
|---|---|
| K4 source discovery (source wujud: DOCX + md5 + 20 topik) | coverage % taxonomy atas deck sebenar |
| Coverage **proxy** atas topic-level interaction demand | binding table produksi tahap slide |
| Pilihan PL/topik untuk full slide pass | keputusan tracking SCORM muktamad |
| Kad ambiguity untuk Bariah | arahan build |

**Nota token:** `sb_token` dalam jadual ini ialah **cadangan sistem** (JSON sendiri: "SISTEM CADANG SAHAJA, Bariah boleh tolak/tukar/tambah") — **BUKAN token SB/Bariah**. Jangan sesekali layan sebagai requirement SME. Provenance maksimum baris = confirmed-from-file terhadap fail cadangan, bukan terhadap kehendak Bariah.

## 3. Jadual kerja — 5 topik prioriti × 2 token = 10 baris

| row_id | slide | sb_token | sb_context | grammar | kelas | proposed_binding | binding_status | row_disp. | provenance | prov_ref | tracking | ambiguity_reason | card_id | decided_by | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BIND-K4-PL04T2-001 | PL04 T2 (topic) | "Scenario with Questions" | rajah 10 · sub 21 · 4,803 aksara | jika Q&A selepas situasi: flat + quiz-feedback; jika tindakan→akibat: **dag-with-history** | — | {Scenario-with-Questions *(P-baru, tiada dalam taxonomy)*, Branching Scenario *(T2 sedia bernama)*} | **AMBIGUOUS** | INTERACTION | confirmed-from-file | json md5 420e… | **interaction-path** *(strictest calon)* | scenario-vs-branching + token-tak-dalam-taxonomy | CARD-K4-001 | AI-draft | Topik ujian utama hipotesis decision topology |
| BIND-K4-PL04T2-002 | PL04 T2 (topic) | "Click-and-Show" | "kad rujukan pantas selepas scenario" | flat-set · gate? · inline · reveal | VARIAN? | Gated Click & Reveal *(gate: strictest-wins ON, sahkan)* | DRAFT | INTERACTION | confirmed-from-file | json md5 420e… | completion | — | — | AI-draft | Mapping Click-and-Show→C&R = inferens, perlu semakan Firdaus |
| BIND-K4-PL04T1-003 | PL04 T1 (topic) | "Scenario with Questions" | **rajah 18** · sub 32 · 7,585 aksara — "situasi bergambar" | flat + quiz-feedback; visual tinggi → presentation kaya imej | — | Scenario-with-Questions *(P-baru)* | **AMBIGUOUS** | INTERACTION | confirmed-from-file | json md5 420e… | completion | token-tak-dalam-taxonomy | — *(ikut keputusan ADR-mini-002)* | AI-draft | Pemasangan = urutan langkah, bukan decision chain — calon branching LEMAH di sini |
| BIND-K4-PL04T1-004 | PL04 T1 (topic) | "Click-and-Show" | sub 32 | flat-set · gate? · inline | VARIAN? | Gated Click & Reveal | DRAFT | INTERACTION | confirmed-from-file | json md5 420e… | completion | — | — | AI-draft | |
| BIND-K4-PL05T1-005 | PL05 T1 (topic) | "Scenario with Questions" | rajah 12 · **sub 70** · 8,606 aksara | flat + quiz-feedback | — | Scenario-with-Questions *(P-baru)* | **AMBIGUOUS** | INTERACTION | confirmed-from-file | json md5 420e… | completion | token-tak-dalam-taxonomy | — | AI-draft | Dokumen serahan — lihat CARD-K4-002 |
| BIND-K4-PL05T1-006 | PL05 T1 (topic) | "Click-and-Show" | sub 70 — struktur amat padat | flat-set · **gate?** · inline | VARIAN? | {C&R bebas-klik, C&R bergate *(checklist serahan)*} | **AMBIGUOUS** | INTERACTION | confirmed-from-file | json md5 420e… | completion | gate-on-atau-off (dua varian sah, konteks dokumen serahan) | CARD-K4-002 | AI-draft | Test 2: reveal biasa vs verification/gated completion |
| BIND-K4-PL05T2-007 | PL05 T2 (topic) | "Click-and-Show" | **sub 106** · 9,337 aksara | flat-set · gate? · inline — skala 106 item = isu presentation | VARIAN? | Gated Click & Reveal *(catatan skala)* | DRAFT | INTERACTION | confirmed-from-file | json md5 420e… | completion | — | — | AI-draft | 106 sub-bahagian dalam satu skrin C&R tak realistik — kemungkinan perlu Detail Screen + Kembali (hub-spoke) sebagai presentation. Calon binding kedua, semakan Firdaus |
| BIND-K4-PL05T2-008 | PL05 T2 (topic) | "Scenario with Questions" | liabiliti kecacatan & CMGD | flat + quiz-feedback | — | Scenario-with-Questions *(P-baru)* | **AMBIGUOUS** | INTERACTION | confirmed-from-file | json md5 420e… | completion | token-tak-dalam-taxonomy | — | AI-draft | |
| BIND-K4-PL03T2-009 | PL03 T2 (topic) | "Click-and-Show" | **sub 53** · 13,007 aksara | flat-set · gate? · inline — isu skala sama baris 007 | VARIAN? | Gated Click & Reveal *(catatan skala)* | DRAFT | INTERACTION | confirmed-from-file | json md5 420e… | completion | — | — | AI-draft | |
| BIND-K4-PL03T2-010 | PL03 T2 (topic) | "Scenario with Questions" | pengurusan risiko | flat + quiz-feedback; risiko = calon decision kedua selepas PL04T2 | — | Scenario-with-Questions *(P-baru)* | **AMBIGUOUS** | INTERACTION | confirmed-from-file | json md5 420e… | completion | token-tak-dalam-taxonomy | — | AI-draft | Jika CARD-K4-001 jawab (B), topik ini calon branching kedua |

## 4. Blok metrik — PROXY (topic-level, bukan coverage sebenar)

```
N_total_rows            = 10
N_int                   = 10  (IMPL-ONLY 0 · REJECTED 0 · DUPLICATE 0)
coverage PROXY          = 5/10 = 50%   ← baris Click-and-Show map ke Gated Click &
                          Reveal (sedia ada); SEMUA baris tak-covered berpunca dari
                          SATU token: "Scenario with Questions" tiada dalam taxonomy
new-pattern demand      = 1   (Scenario-with-Questions, dikira sekali pada tahap
                          pattern; Branching Scenario TAK dikira — sudah bernama
                          dalam taxonomy sebagai T2)
ambiguity rate          = 5/10 = 50%  (selepas draf AI, sebelum kad)
implementation-only rate= 0/10
tracking-required rate  = 10/10 = 100% (asas strictest-wins; 9 completion,
                          1 interaction-path calon)
SME-clarification load  = 2 kad (CARD-K4-001 blocking, CARD-K4-002 prioriti 2)
```

**Bacaan metrik (penting — jangan salah tafsir):**
- Coverage proxy 50% NAMPAK gagal ambang 80%, tetapi puncanya **satu jurang vocabulary**, bukan lima jurang pattern: sistem cadangan CAIR bercakap bahasa bukan-taxonomy ("Scenario with Questions", "Click-and-Show", "Reflection"). Satu keputusan (ADR-mini-002 + satu kad) menutup 5 baris serentak → coverage proxy melonjak ke ~90–100%.
- Ambiguity 50% = tepat di sempadan, TIDAK melepasi >50%; dan nota ambang metadata terpakai (pemilihan decision-dense + jurang vocabulary tunggal). **Bukan** isyarat lexicon rosak.
- Penemuan struktur sebenar pass ini: **enjin cadangan CAIR sendiri perlu bercakap nama taxonomy** — jika tidak, setiap output CAIR mencipta hutang binding. Ini isu kelas PR-001 arah dalaman (tooling sendiri menjana vocabulary luar taxonomy).

## 5. Kad klarifikasi — stub (draf, BELUM dihantar; melalui Firdaus sahaja)

### CARD-K4-001 · PL04 T2 Pengujian & Pentauliahan — *blocking, prioriti 1*
> **CARD-K4-001 · K4 PL04 T2**
> Untuk topik Pengujian & Pentauliahan, pelajar patut:
> (A) Baca situasi ujian, jawab soalan, dapat feedback — guna player sedia ada, boleh masuk montaj ikut jadual
> (B) Pilih tindakan pengujian → nampak akibat kat tapak → keputusan seterusnya berubah ikut pilihan — lebih dekat dengan kerja sebenar, tapi kena bina baru + montaj lambat
> Kalau tak sempat jawab: kami hold, tak build apa-apa dulu.
> Reply "A" atau "B" je cukup 👍

*Nota dalaman (bukan untuk Bariah):* (B) = Branching Scenario, T2, gate demand — jawapan (B) + lock = gate ≥1 kad LOCKED dipenuhi buat kali pertama. Jawapan (A) = Scenario-with-Questions, masuk ADR-mini-002.

### CARD-K4-002 · PL05 T1 Dokumen Serahan — *prioriti 2, tak blocking*
> **CARD-K4-002 · K4 PL05 T1**
> Untuk kad senarai dokumen serahan tu:
> (A) Pelajar boleh klik mana-mana kad, bila-bila — rujukan bebas
> (B) Pelajar kena buka SEMUA kad dulu baru boleh next — macam checklist serahan sebenar
> Dua-dua boleh buat sekarang, tak ada kos tambahan. Ikut mana yang u rasa sesuai untuk konteks serahan dokumen.
> Reply "A" atau "B" je cukup 👍

*Nota dalaman:* dua-dua varian koordinat sedia ada (gate off/on atas Gated Click & Reveal) — ini kad murah; sesuai juga sebagai probe galeri-vs-teks jika Firdaus mahu jalankan Test §7 pack.

## 6. Mini-ADR draf

> **ADR-mini-002 · Scenario with Questions** *(draf AI — keputusan milik manusia)*
> Topology: flat/linear + quiz-feedback · Tracking: completion
> Bukti: BIND-K4 baris 001, 003, 005, 008, 010 (5 baris, satu deck) — syarat "≥2 kad menuntut bundle sama" DIPENUHI pada tahap cadangan sistem, BELUM pada tahap SME
> Bukan varian kerana: tiada komposisi sedia ada dengan quiz/scenario feedback — μB kelas feedback-jawapan tiada dalam set tertutup semasa
> Jurang player: **dijangka TIADA** — quiz capability wujud dalam build K1 (bukti G6 K1PL1T1: "the quiz scores") → kelas P, bukan T2. TETAPI ini inferens: **grep sahkan sebelum lulus** (OPEN-K4-d)
> Gate: menunggu (i) grep capability, (ii) pengesahan Bariah bahawa "Scenario with Questions" memang bentuk yang dia mahu (kad selepas CARD-K4-001)
> **Keputusan: KANDIDAT — jangan masukkan dropdown lagi.** Provenance: inferred + confirmed-from-file (cadangan sistem)

## 7. Item OPEN pass ini

| ID | Item | Tindakan | Siapa |
|---|---|---|---|
| OPEN-K4-a | **CSV 05 ROSAK**: label interaktiviti bergeser terhadap rasional sendiri (PL01 T1: "Click-and-Show" membawa rasional Scenario; "Drag-and-Drop" membawa rasional Reflection) DAN bercanggah dengan JSON BEKU pada topik sama | Jangan guna CSV 05 untuk interaktiviti. Jana semula dari JSON atau siasat mapping bug penjana CSV. JSON = kanon topic-level | Firdaus |
| OPEN-K4-b | Watak: CSV 04 guna "Pak Mail (Penyelia Lif Berpengalaman)", CSV 05 guna "Maya (narasi sahaja)" | Semak terhadap dokumen casting canon K4 — "Pak Mail" tidak dikenali dalam canon setakat ingatan sesi; sahkan terhadap dokumen, bukan ingatan | Firdaus |
| OPEN-K4-c | Gate PRD Bariah (GET-DOC + md5) — pass ini berjalan atas andaian pengecualian klasifikasi-pra-kerja | Sahkan pengecualian ATAU batalkan dan jadualkan GET-DOC dahulu | Firdaus |
| OPEN-K4-d | Quiz capability player = inferens dari bukti G6 K1 | Grep build bila disk hijau — SEBELUM ADR-mini-002 dilulus | Firdaus |
| OPEN-K4-e | md5 taxonomy kanon belum diisi dalam metadata | Isi selepas fix salinan kanon | Firdaus |
| OPEN-K4-f | Pola namespace P2→I2 antara CSV 04→05 | Sahkan ini I-rename yang dirancang (bukan corruption kedua) — jika ya, rekod sebagai jangkaan dipenuhi | Firdaus |

**Nota anti-drift (dari `nota_penting` JSON, verbatim):** "K4 TIADA Jadual perbandingan literal dalam mana-mana topik (jadual_literal=0 semua 20 topik)... Pairing = 0 untuk seluruh K4." → **Jangan cadang Pairing/Compare untuk mana-mana topik K4 kecuali Bariah sendiri minta.**

## 8. Shortlist untuk full slide cold-coverage pass (bila deck/SB wujud)

1. **PL04 T2** — Pengujian & Pentauliahan (keputusan CARD-K4-001 menentukan topology)
2. **PL05 T1** — Dokumen Serahan (isu gate + skala 70 sub-bahagian)
3. PL05 T2 — hanya jika isu skala 106-item (baris 007) memerlukan keputusan presentation berasingan

## 9. Checklist serah-balik AI worker

- [x] Setiap baris ada `binding_status` + `row_disposition`
- [x] Setiap baris saya isi: `decided_by: AI-draft` — tiada Firdaus/Bariah ditulis
- [x] Sifar nama generik terlarang (Modal/Accordion/Tooltip/Tabs/Timeline/Process) dalam `proposed_binding` — log RS kosong, tiada cadangan generik diterima masuk
- [x] Setiap AMBIGUOUS ada `ambiguity_reason` + calon (+ kad untuk yang blocking)
- [x] Sifar auto-bind token ambiguous — "Scenario with Questions" TIDAK di-bind, dinaikkan sebagai calon P-baru melalui mini-ADR
- [x] Semua `sb_token` verbatim dalam `"..."` — dengan nota bahawa ia cadangan sistem, bukan token SME
- [x] Enam metrik pusingan-1 dikira, dilabel PROXY
- [x] Fail taxonomy tidak disentuh
- [x] Tiada RESOLVED/LOCKED ditanda oleh AI

---
*Pass ini membuka lane K4 tanpa overclaim. Satu jurang vocabulary, satu kad blocking, enam item OPEN.
Seterusnya milik manusia: sahkan OPEN-K4-a/c, hantar CARD-K4-001. Finish. Package. Close.*

<!-- PROVENANCE NOTE (ditambah semasa staging batch 06/07/2026, bukan sebahagian pass asal):
Fail ini di-re-serialize verbatim dari rekod perbualan sesi arkitek (dokumen pass pusingan-1
yang dipaste penuh). Kandungan tidak diubah. Angka mentah pusingan-1 di sini SUPERSEDED oleh
binding/K4-topic-cold-prep-v0-review-r1.md — baca bersama, jangan petik metrik mentah tanpa review r1. -->
