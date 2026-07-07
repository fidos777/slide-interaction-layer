# Semakan Pusingan-1 — K4 Topic-Level Cold-Prep Pass v0
**Sasaran repo:** `binding/K4-topic-cold-prep-v0-review-r1.md` · Reviewer: Firdaus (via sesi Claude 05/07/2026)
**Status:** pass DITERIMA sebagai lane-opener, dengan rebaseline metrik di bawah. Angka mentah pusingan-1 JANGAN dipetik tanpa nota ini.

---

## 1. Pembetulan utama: arah authority vocabulary TERBALIK

Pusingan-1 membaca "Scenario with Questions" sebagai vocabulary liar enjin CAIR
→ cadang paksa CAIR guna nama taxonomy. **Salah arah.** Verifikasi fail
(HANDOFF v3, project files):

- "SnG Cycle 7 perlu minimum 2 interaktiviti per topik. Jenis sah:
  **Scenario with Questions, Click and Show, Drag and Drop**."
- s15 = "[Interaktiviti #3 — Scenario w/ Questions]", **G6-proven** SCORM Cloud.

"Scenario with Questions" = **bahasa kontrak SnG**, sudah terbina dan terbukti
dalam player. Yang tercicir ialah entry taxonomy. Pembetulan yang betul:
taxonomy serap vocabulary kontrak (→ v0.3 §3.5 + peraturan penamaan #4),
bukan CAIR tukar bahasa. Separuh penemuan asal kekal sah: alignment
vocabulary wajib — mekanismenya glosari padanan.

## 2. Rebaseline metrik (atas taxonomy v0.3, md5 `f9deab7c07f57e7986d20ed19816661b`)

| Metrik | Pusingan-1 (v0.2) | Rebaseline (v0.3) | Nota |
|---|---|---|---|
| coverage proxy | 50% | **~100%** (10/10 map ke entry sedia ada) | 5 baris tertutup oleh satu entry §3.5 |
| new-pattern demand | 1 | **0** | Jurang entry, bukan jurang pattern/capability |
| ambiguity | 50% | **20%** (2/10) | Baki tulen: baris 001 (scenario-vs-branching → CARD-K4-001) + baris 006 (gate on/off → CARD-K4-002) |
| tracking-required | 100% | 100% — **dengan caveat WAJIB** | 9× `completion` = gate local, covered casis, TIADA event LMS; 1× `interaction-path` = satu-satunya kerja player belum wujud. Jangan baca 100% sebagai backlog |
| load | 2 kad | 2 kad | Kekal — dua-dua ambiguity tulen |

**Verdict ambang:** coverage ✓ · demand ✓ · ambiguity ✓ · load ✓ — taxonomy
v0.3 menampung K4 topic-level sepenuhnya. Ujian sebenar seterusnya = full
slide pass (sasaran dicadang: set SB_K1PL1 v2, wujud & segar dalam Drive).

## 3. Status item OPEN selepas semakan

| ID | Status | Asas |
|---|---|---|
| OPEN-K4-a (CSV 05 rosak) | **KEKAL — milik Firdaus** | Siasat bug penjana; JSON = kanon tunggal. CSV 04 turut disyaki (lihat -b) |
| OPEN-K4-b (Pak Mail) | **DITUTUP: OFF-CANON** | Kanon K4 locked 03/07 [PRD md5 0bc926fe + meeting]: Amir/Encik Zul/Maya + Danial/Sarah. "Pak Mail" tiada → CSV 04 pra-lock atau tercemar |
| OPEN-K4-c (gate PRD) | **KEKAL — keputusan Firdaus** | Cadangan reviewer: pengecualian wajar (pass atas JSON BEKU commit 7f34d33 = klasifikasi, bukan penciptaan kandungan). Rekod keputusan, jangan kekal andaian |
| OPEN-K4-d (quiz capability) | **DITUTUP: RESOLVED** | HANDOFF v3 (fail, bukan ingatan): s15 quiz G6-proven, `completeQuiz()` synchronous. ADR-mini-002 gate (i) selesai — kelas P sedia ada tanpa entry, kini §3.5 v0.3. Gate (ii) diturun taraf: vocabulary kontrak, tak perlu kad |
| OPEN-K4-e (md5 taxonomy) | **DITUTUP** | v0.3 kanon: `f9deab7c07f57e7986d20ed19816661b` |
| OPEN-K4-f (P2→I2) | **DITUTUP: jangkaan dipenuhi** | I-rename deployed (commit live); CSV 04 = export pra-rename, stale by definition |

## 4. ADR-mini-002 — disposisi

**DILUPUSKAN sebagai P-baru; diganti oleh entry v0.3 §3.5.** Pattern bukan
baru — G6-proven, tercicir dari taxonomy sahaja. Varian MR/TF kekal parked
menunggu PRD (μB baru `multiple-response-select` / `truefalse-select` →
mini-ADR bila fail sampai).

## 5. Kad — saluran & giliran

- CARD-K4-001 (PL04 T2 A/B) + CARD-K4-002 (PL05 T1 gate): format binary ✓,
  tapi jawapan mesti mendarat dalam `cair_decisions` — masukkan pilihan
  sebagai `suggest[]` kad desk masing-masing (jadual kosong = edit percuma);
  WhatsApp = notifikasi sahaja. One decision one place.
- Giliran: mesej PRD + consent DULU (masih belum hantar; blocking lebih
  banyak). Kad K4 selepas itu. Tiga keputusan serentak = "Ha pening".

## 6. Pengajaran proses (calon ADR-006)

Pusingan-1 patuh semua peraturan mekanikal (tiada auto-bind, tiada nama
generik, verbatim ✓) tetapi terbalik arah pada tafsiran penemuan — dan
pembetulan datang dari **grep fail dalam sesi semakan**, bukan dari peraturan
pass. Menunjukkan: checklist menghalang kesilapan komisen; kesilapan tafsiran
memerlukan lapisan semakan berasingan dengan akses sumber. Selaras operating
rule ADR-006 langkah 2 ("Build sekarang — verified, bukan ingatan").
