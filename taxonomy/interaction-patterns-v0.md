# Interaction Patterns — Taxonomy v0
## SMC-CIDB-TAXONOMY-INTERAKSI-001

| | |
|---|---|
| **Dokumen** | SMC-CIDB-TAXONOMY-INTERAKSI-001 |
| **Versi** | 0.4 — draf untuk commit. v0.3→v0.4 (07/07): entry 3.5A Reflection, prasyarat P12. v0.2→v0.3 (05/07, hasil pass K4 topic-level): +entry Scenario with Questions (jurang entry, pattern G6-proven tercicir), +registry μB tertutup, +paksi topology diserap dari template binding, +glosari vocabulary kontrak SnG |
| **Tarikh** | 5 Julai 2026 |
| **Disediakan** | Firdaus Ismail — SME Cloud |
| **Sasaran repo** | `slide-interaction-layer/taxonomy/interaction-patterns-v0.md` |
| **Status commit** | ⏳ TERTAHAN — disk Mac merah. Commit dalam batch dokumen selepas M2.1 + I-rename (rujuk urutan CONTEXT SYNC 03–05 Jul) |
| **Bergantung pada** | ADR-005 (namespace E/I/P/R), ADR-006 (Cost of Asking) |

> **Nota penggunaan:** Fail ini ialah sumber untuk label dropdown CAIR Desk dan
> untuk kontrak transform layer. View Bariah TIDAK menunjukkan kelas P/R atau
> jargon composition — dia nampak nama pattern sahaja (prinsip sama dengan
> pembuangan INTENT_MAP, ADR-005).

---

## 1. Prinsip teras (tiga trace convergent, 05/07/2026)

**Interaction ≠ template. Interaction = behaviour composition.**

Tiga lapisan, tiga bahasa:

```
Lapisan 1  SB / Bariah        →  behaviour spec (apa learner alami)
Lapisan 2  Taxonomy (fail ni) →  named compositions (gabungan micro-behaviour)
Lapisan 3  React player       →  implementation (komponen, state, render)
```

Bukti empirik: sesi WhatsApp 16/06/2026 — Bariah spec keperluan dia sebagai
micro-behaviours (klik bebas order, hover merah, tick, unlock selepas semua),
bukan sebagai widget. Rujuk ADR-005 Addendum A untuk nota validation penuh.

**Peraturan penamaan (WAJIB):**

1. **Jangan guna perkataan "Branching" sendirian tanpa qualifier** — dalam
   dokumen, dropdown, kod, dan komunikasi. Dua bentuk sah sahaja:
   **"Branching Scenario"** = pedagogi decision/consequence (Tier-2);
   **"Detail Screen + Kembali (Bariah: branching out)"** = navigation.
   Nota: kita tak polis vocabulary Bariah — dia bebas sebut "branching out";
   peraturan ni mengikat pihak kita. Sebab: collision tiga-maksud dikesan
   05/07 — navigation Bariah vs pedagogi K4 vs leaf Reveal.
2. Nama pattern dalam view Bariah = bahasa behaviour BM/EN campuran yang dia
   sendiri guna (Click & Reveal, Drag & Drop). Tiada istilah widget
   (Modal, Dialog, Accordion, Overlay) dalam view dia.
3. Popup = perkataan SB bermaksud "paparkan layer tambahan" — JANGAN bind
   ke PopupModal React secara automatik. [inferred — sahkan bila Bariah
   hantar recommendation SB popup]
4. **Vocabulary kontrak SnG tidak boleh di-rename-away.** Jenis sah SnG
   ("Scenario with Questions", "Click and Show", "Drag and Drop") ialah
   bahasa tender — taxonomy WAJIB serap istilah ini sebagai nama kanon
   atau glosari padanan, bukan menggantikannya. Jurang antara vocabulary
   kontrak dan taxonomy = hutang binding (dikesan pass K4 topic-level
   05/07: 5/10 baris tak-covered berpunca dari satu istilah kontrak
   yang tercicir dari taxonomy).

---

## 2. Skema entry

| Medan | Keterangan |
|---|---|
| `pattern` | Nama dalam view Bariah |
| `kelas` | P (interaksi) / R (primitive player) / T2 (kandidat Tier-2 bernama) — ikut ADR-005 |
| `composition` | Senarai micro-behaviour (object + state + trigger + feedback) |
| `varian` | Varian presentation/behaviour yang TIDAK menjadikan ia P baru (ujian keahlian ADR-005) |
| `provenance` | confirmed-written / confirmed-from-file / confirmed-verbal / inferred |
| `status` | LOCKED / DEFERRED / KANDIDAT / OPEN |

### 2.1 Registry μB — set tertutup v0.3

Rujukan untuk Q3/Q5 checklist AI worker. "Dalam set" = disenaraikan di sini.
**Tambah μB baru = mini-ADR + semakan Firdaus, bukan edit senyap.**

| Kategori | μB |
|---|---|
| Interaction | `clickable-any-order` · `reveal-content` · `hover-highlight` · `active-highlight` · `visited-tick` · `draggable-items` · `drop-zones` · `single-choice-select` · `answer-feedback` (correct-green / wrong-red) |
| Gate | `nav-lock-until-complete` · `unlock-on-all-visited` · `gate-until-all-correct` · `pass-threshold-gate` |
| Tracking (LMS emission) | `score-report-LMS` · `completion-report-LMS` — **hanya dua ini emit ke SCORM**; semua gate lain = local state sahaja (caveat bacaan metrik tracking) |

### 2.2 Paksi topology — set tertutup (diserap dari template binding, 05/07)

Template binding dan taxonomy kini berkongsi paksi yang sama — template
tidak lagi lebih ekspresif daripada kanon yang ia uji.

| Topology | Entry taxonomy |
|---|---|
| `flat-set` | Gated Click & Reveal · Scenario with Questions |
| `hub-spoke` | Detail Screen + Kembali |
| `mapping` | Drag & Drop |
| `dag-with-history` | Branching Scenario (T2) |
| `timeline-coupled` | overlay-maintain-VO (T2) |

Topology baru yang tak muat set ini = calon entry baru → mini-ADR, bukan
regangan definisi sedia ada.

---

## 3. Entries

### 3.1 Gated Click & Reveal (3-state) — ⭐ komposisi bernama pertama

| | |
|---|---|
| **kelas** | P — komposisi atas Reveal |
| **status** | 🟢 **LOCKED** — "standard untuk propose ke client" ⇒ terpakai kursus-wide, termasuk K4 |
| **provenance** | **[confirmed-written WhatsApp Bariah 16/06/2026, 6:28–6:33 PM]** + status board L-1/L-2/L-3. Mesej kunci: "For now, on my end, ni yg standard lah. Kita propose to client mcm ni." → Firdaus: "ok cun, i lock ya" → Bariah: "Okay" |

**composition:**

| # | Micro-behaviour | Spec Bariah (verbatim/parafrasa) | Build status |
|---|---|---|---|
| 1 | `clickable-any-order` | Semua item boleh diklik, bukan ikut turutan | ✅ ada |
| 2 | `nav-lock-until-complete` | Sebelum: butang Seterusnya LOCK | ✅ `next_locked_until_complete: true` — **gate KEKAL, jangan buang** |
| 3 | `hover-highlight` | "Mouse over pun boleh buat highlight merah?" + "Yg hover tu kalau boleh add" | ⚠️ delta — satu-satunya kerja kod dari sesi 16/06 |
| 4 | `active-highlight` | Semasa klik: highlight **merah** | ⚠️ build = `#C2410C` burnt-orange, spec bertulis = "merah" ×2 → OPEN-a |
| 5 | `visited-tick` | Selepas klik: tick icon muncul | ✅ ada (tick hijau) |
| 6 | `unlock-on-all-visited` | Semua diklik → unlock Seterusnya | ✅ `allVisited → nextUnlocked` |
| — | ~~highlight turutan "klik dulu"~~ | Bariah buang **di SB sendiri** — "tade related coding" | N/A — bukan kod |

**Glosari padanan:** SnG kontrak = "Click and Show" · Bariah = "Click & Reveal"
· satu pattern, tiga nama — glosari, bukan entry berasingan.

**Nota skala:** Variasi masa depan (cth K4 minta "sama tapi tanpa tick") =
komposisi tolak/tambah micro-behaviour, **bukan pattern baru**. Itu cara
taxonomy ni scale tanpa explode.

---

### 3.2 Reveal — family + varian presentation

| | |
|---|---|
| **kelas** | P |
| **status** | Family LOCKED sebagai konsep; varian popup **DEFERRED** |
| **provenance** | Inline/detail: confirmed-written 16/06. Varian popup: **[confirmed-from-file — raw notes AMEND-K1]** |

**varian presentation** (semua = Reveal, bukan P berasingan — ujian ADR-005):

| Varian | Sumber | Status |
|---|---|---|
| `inline` — detail ganti/masuk skrin utama | WhatsApp 16/06 ("display on main screen") | sedia |
| `overlay-with-close` — "POP UP + close button" | AMEND-K1 (cth PL06T3 s7) | **DEFERRED** |
| `overlay-maintain-VO` — "POP UP + maintain, NO close button, with VO" | AMEND-K1 structural finding | **DEFERRED** + kandidat player (bawah) |

**⛔ JANGAN:** encode "popup bukan requirement" — popup ialah pattern sebenar
dalam SB Bariah ("Selalunya kalau text minimal... I akan buat pop up";
"I ada pop up untuk SB lain.. nanti i baca, and recommend"). Yang open cuma
*binding implementation* dan *disposisi menyeluruh*. Padam popup = ralat kelas
Bitumen-Sheet arah terbalik (delete requirement, bukan invent).

**Implikasi player (kandidat bernama, JANGAN bina — demand-pull):**
`overlay-maintain-VO` memerlukan layer yang dismiss ikut **audio timeline**,
bukan klik. Behaviour ni tiada dalam player sekarang. Duduk sebelah P14
In-Video sebagai kandidat Tier-2 bernama.

**🔒 Peraturan konversi POP UP (guardrail anti-drift — WAJIB):**
Jika storyboard tulis `POP UP`, JANGAN auto-convert kepada PopupModal.
Perkataan tu behaviour SB ("paparkan layer tambahan"), bukan komponen.
Mesti pilih variant secara eksplisit, dengan provenance pilihan:

```
POP UP dalam SB → pilih SATU:
  - overlay-with-close
  - overlay-maintain-VO
  - inline-reveal
  - detail-screen-kembali   ← preseden: sample cementitious 16/06
```

Preseden drift yang peraturan ni halang: build K1 bind popup→PopupModal
secara automatik; SB Bariah rupanya maksudkan branching out full screen
(kos: satu petang penyelarasan, 16/06).

**Skema simpanan (bila kad diisi):**

```json
{ "pattern": "reveal", "variant": "overlay_maintain_no_close_with_vo" }
```

---

### 3.3 Detail Screen + Kembali *(Bariah: "branching out")*

| | |
|---|---|
| **kelas** | **P — navigation pattern** (primitive implementasi: screen transition, kelas R) |
| **status** | LOCKED sebagai konsep; implementasi s06 UNVERIFIED → OPEN-b |
| **provenance** | [confirmed-written 16/06: "Branching out (full screen).. Kembali"; "Yang interactivity sample.. cementitious tu Branching out full screen, butang Kembali"] |

Flow: klik item → skrin detail (inline penuh / berasingan) → butang **Kembali**
→ balik ke menu. Tiada decision, tiada consequence — navigasi hub→leaf→hub.

**⚠️ Nota klasifikasi [keputusan 05/07, semak masa penomboran final]:**
Secara struktur ADR-005, pattern ni tiada feedback/assessment → hujah kelas R
tulen wujud. Ia dinaikkan ke P atas sebab **Bariah-facing**: dia classify
sample cementitious sebagai "branching out" sendiri, maka ia mesti wujud
sebagai pilihan pattern dalam dropdown, bukan tersembunyi sebagai primitive.
Kalau penomboran final terhadap fail taxonomy repo mendedahkan konflik,
resolusi = tambah medan `dropdown_visible` berasingan dari kelas, BUKAN
turunkan balik ke R secara senyap.

**Glosari padanan:** Bariah = "branching out" · Rise 360 ≈ nested content block ·
label taxonomy = Detail Screen + Kembali.

---

### 3.4 Drag & Drop

| | |
|---|---|
| **kelas** | P — pattern berasingan (Bariah treat ia sendiri: "Ada branching out Kembali & drag and drop") |
| **status** | LOCKED — G6-proven (s13 K1PL1T1) |
| **provenance** | confirmed-written 16/06 + AMEND-K1 (PL05T1 s5, PL05T3 s4) + G6 evidence 31/05 |

composition: `draggable-items` + `drop-zones` + `wrong=red / correct=green` +
`gate-until-all-correct`.

---

### 3.5 Scenario with Questions — ⭐ nama kontrak SnG, entry ditambah v0.3

| | |
|---|---|
| **kelas** | P — komposisi |
| **status** | 🟢 **LOCKED** — jenis sah kontrak SnG + G6-proven (s15 K1PL1T1: fail→pass transition disahkan dalam SCORM Cloud) |
| **provenance** | [confirmed-from-file — HANDOFF v3: "Jenis sah: Scenario with Questions, Click and Show, Drag and Drop" + s15 "[Interaktiviti #3 — Scenario w/ Questions]"] + G6 evidence 31/05 |

**Sejarah entry:** pattern ini wujud dan terbukti SEBELUM taxonomy ditulis;
v0.2 terciciriannya kerana dibina dari trace 16/06 + AMEND-K1 yang tak
menyentuh kuiz. Pass K4 topic-level (05/07) mendedahkan jurang: 5/10 baris
"tak-covered" sebenarnya map ke pattern ini. Pengajaran → peraturan
penamaan #4.

**composition:**

| # | Micro-behaviour | Build status |
|---|---|---|
| 1 | `situation-stem` (situasi/scenario sebelum soalan) | ✅ s15 |
| 2 | `single-choice-select` ×n soalan | ✅ s15 (5 soalan) |
| 3 | `answer-feedback` | ✅ |
| 4 | `pass-threshold-gate` (70% / masteryScore 0.7) | ✅ |
| 5 | `score-report-LMS` (`completeQuiz()` synchronous → `reportQuizResult`) | ✅ G6-proven |

**topology:** `flat-set` + quiz-feedback · **tracking:** completion + score —
satu-satunya pattern dengan LMS emission sedia terbina.

**Varian menunggu PRD [JANGAN bina dulu]:** format K4 "4 single + 1
multiple-response" [PRD md5 0bc926fe — fail belum diterima]. MR dan TF =
varian komposisi (+`multiple-response-select` / +`truefalse-select`, μB baru
→ mini-ADR bila PRD sampai), BUKAN P baru. Delta ini juga pembawa
`cmi.interactions` (asas tracking `interaction-path`).

---

### 3.5A Reflection (kurus) — entry ditambah v0.4 (prasyarat kod P12)
| | |
|---|---|
| **kelas** | P — komposisi minimum |
| **status** | KANDIDAT-DIBINA — diluluskan untuk montaj K4 pertama sahaja (backlog v1 delta 1) |
| **provenance** | [inferred — ADR-005 backlog P12 "kurus"; wargame 05/07 §1; BELUM disahkan Bariah — naik LOCKED hanya melalui kad/desk] |
**composition:** `prompt-display` + `free-text-input (optional)`. TIADA gate (Next bebas), TIADA skor,
TIADA lms_emit, TIADA persistence v1 (local state sahaja — Laluan A wargame).
**topology:** flat-set · **tracking:** none.
**Sempadan keras:** medan evaluation/rubric/evidence-chain = FORBIDDEN dalam JSON (produk Q4, bukan pattern ni).
**Nota lexicon:** "Reflection" kekal TIADA-PADANAN untuk cadangan CAIR sedia ada SEHINGGA entry ini LOCKED —
status glosari dikemaskini hanya selepas pengesahan Bariah.

---

### 3.6 Branching Scenario — ⚠️ sentiasa dengan qualifier "Scenario" (peraturan penamaan #1)

| | |
|---|---|
| **kelas** | **T2 — kandidat Tier-2 bernama** (kategori sama P14 In-Video) |
| **status** | KANDIDAT — ⛔ JANGAN bina sehingga ≥1 kad K4 lock dengan pattern ni |
| **provenance** | [inferred — analisis K4 05/07; BELUM dibawa ke Bariah] |

Flow: scenario → decision → consequence → decision (loop). Ikut ujian keahlian
ADR-005 ia P **baru**, bukan varian — consequence-chain + path-tracking tak
boleh digubah dari P sedia ada.

**Kekuatan strategik:** asymmetri tracking = moat (REF-001/002 — branching
hyperlink iSpring = kotak hitam SCORM; player kita boleh report laluan
keputusan penuh via `cmi.interactions`).

**Cara bawa ke Bariah:** binary-with-cost per kad K4, BUKAN jadual reclassification
13 baris. Contoh: "PL04 T2 Pengujian — (A) Scenario-with-Questions [kos: player
sedia ada] atau (B) Branching Scenario [kos: pattern baru + tracking + montaj
lambat]?"

---

### 3.7 Kandidat lain dari raw notes AMEND-K1 (confirmed-from-file, belum spec)

| Pattern | Bukti | Status |
|---|---|---|
| Hidden Objects / Hotspot | PL01T5 s4 "Ala ala hidden objects" | KANDIDAT — tunggu kad CAIR minta |
| Image Swap / Changing Images | PL01T1 s10–11, PL05T1 s6–7 | KANDIDAT |
| Tabs / Accordion / Timeline / Process | — | ❌ SPEKULASI SAHAJA — tiada bukti dalam SS/fail. Jangan masukkan dropdown |

---

## 4. Item OPEN (tindakan Firdaus — jangan beku fail ni tanpa nota status ini)

| ID | Item | Tindakan |
|---|---|---|
| OPEN-a | Hover/active = "merah" bertulis vs build `#C2410C` | Binary ke Bariah: tukar merah penuh ATAU tunjuk `#C2410C`, dia accept sebagai "merah". Strictest-wins: default ikut perkataan dia |
| OPEN-b | s06 branch `s0-remediation-a2a7` masih PopupModal atau dah inline (Tafsiran A)? | **Grep bila disk hijau** — jangan assume. Kalau belum selaras: build delta + G6 revalidate |
| OPEN-c | Follow-up popup "we talk bout it tmrw" (17 Jun) | Berlaku ke tak? Kalau tak: kelas WAIT — Bariah sendiri kata dia nak baca SB dan recommend |
| OPEN-d | Namespace B-1…B-7 (sesi Jun) vs B1–B4 (context sync Jul) | Rename set Jun → `K1DEMO-B1…B7` sebelum commit dokumen sesi Jun |
| OPEN-e | K1DEMO-B1/B3 (provenans imej Haziq AI) | Migrate ke decision log, bersebelahan finding C2PA 6 PNG |

---

*Doktrin: behaviour dahulu, widget kemudian. Komposisi, bukan template.
"Branching" mesti berqualifier. Popup deferred, bukan deleted.
Finish. Package. Close.*
