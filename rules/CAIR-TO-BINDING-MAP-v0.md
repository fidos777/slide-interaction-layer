# CAIR → Binding Table Map v0
**Sasaran repo:** `rules/CAIR-TO-BINDING-MAP-v0.md` · Peta medan deterministik: satu objek cadangan CAIR = satu baris binding. Peta, BUKAN skrip.

## 1. Peta medan

| Medan CAIR | → Kolum binding | Peraturan |
|---|---|---|
| `jenis_taxonomy` (nama sah) | `proposed_binding` | Terus, verbatim |
| `jenis_taxonomy = TIADA-PADANAN` | `proposed_binding` = senarai calon (jika ada) atau `—` | + peraturan §2.2 |
| `jenis_asal_sistem` | `sb_token` | Verbatim dalam `"..."` — dengan nota tetap: **cadangan sistem, BUKAN token SB/SME** |
| `alias_kontrak` | `notes` (rujukan glosari) | Sah HANYA jika wujud dalam `lexicon/ALIAS-GLOSSARY-v0.md` (exact match); kekalkan sebagai `alias: <nilai>`; `proposed_binding` sentiasa nama kanon. Alias luar glosari = layan sebagai `jenis_asal_sistem` biasa |
| `variant_koordinat` | `grammar` + `proposed_binding` | Koordinat sahaja; koordinat tak dikenali = baris AMBIGUOUS |
| `rasional` | `sb_context` | Verbatim |
| `status` ("cadangan — Bariah putus…") | `notes` | Kekalkan — peringatan bahawa ini belum kehendak SME |
| `taxonomy_version` + `taxonomy_md5` | metadata fail binding | **v0.4 · `d6cf96061bbbfddde6829074930eea98`** — mesti sepadan salinan kanon; tak sepadan = JANGAN mula pass |
| `source_file` + `source_md5` | `prov_ref` | Wajib — provenance mesti resolve ke fail |
| — | `provenance` | Sentiasa `confirmed-from-file` — terhadap **fail cadangan**, bukan terhadap kehendak Bariah |
| — | `decided_by` | Sentiasa `AI-draft` |
| — | `row_disposition` | `INTERACTION` (cadangan interaktiviti sentiasa learner-facing) |
| — | `tracking` | Default per pattern (§3), strictest-wins — **CALON sahaja** |

## 2. Peraturan status (v0.3)

**2.1 Nama taxonomy sah + kelas LOCKED/VARIAN/base pattern** → `binding_status: DRAFT`.
Contoh: `Scenario with Questions` (entri kanon v0.3, G6-proven) → DRAFT, tunggu semakan Firdaus. Contoh alias: `Click and Show` → binding kanon `Gated Click & Reveal`, alias direkod di `notes` (preseden BIND-K4-PL04T2-002).

**2.2 `TIADA-PADANAN`** → `binding_status: AMBIGUOUS` + `ambiguity_reason: token-tak-dalam-taxonomy` + `sb_token` = `jenis_asal_sistem`.
Contoh: `Reflection` → AMBIGUOUS — kekal TIADA-PADANAN sehingga diverifikasi di tempat lain.

**2.3 Nama sah tetapi kelas T2/KANDIDAT dalam taxonomy** → `binding_status: AMBIGUOUS` + nota gate.
Contoh: `Branching Scenario` → AMBIGUOUS, gate demand belum dipenuhi.

**2.4 DUA entri sah bersaing pada satu topik** → `binding_status: AMBIGUOUS` + `ambiguity_reason: pattern-vs-pattern` + kad.
Contoh: PL04 T2 — ambiguity BUKAN lagi "token tak dalam taxonomy"; ia **`Scenario with Questions` vs `Branching Scenario`** (dua nama sah, satu bergate) → CARD-K4-001.

**2.5 DRAFT vs AMBIGUOUS, ringkas:** DRAFT = satu padanan kanon munasabah, tunggu semakan manusia. AMBIGUOUS = tiada padanan / ≥2 calon (termasuk pattern-vs-pattern) / padanan bergate. AI worker tak boleh menaikkan mana-mana ke RESOLVED/LOCKED.

## 3. Tracking — calon, bukan emisi

`tracking` diisi dari default pattern (Gated C&R → `completion`; Drag & Drop → `completion`; Branching Scenario → `interaction-path`; strictest-wins bila ragu) dan bermaksud **calon `lms_emit`** SAHAJA. `tracking: completion` TIDAK bermaksud player akan menulis ke cmi — pemisahan `gate` vs `lms_emit` diputuskan di peringkat config dan diuji G6 (rujuk patch release gate). Catat di `notes` jika nilai bergantung pada calon yang belum diputus.

## 4. Bila kad klarifikasi WAJIB

- Baris AMBIGUOUS yang **blocking build**, ATAU kos-jika-salah tinggi (verb ASK ikut ADR-006).
- Contoh hidup: PL04 T2 scenario-vs-branching → CARD-K4-001 (blocking, prioriti 1).
- Baris AMBIGUOUS tak blocking → masuk queue, verb WAIT/PROPOSE, kad ikut giliran sesi.

## 5. Bila mini-ADR WAJIB

- `jenis_asal_sistem` yang sama muncul TIADA-PADANAN pada **≥2 baris** → SATU mini-ADR pada tahap pattern (bukan satu per baris). Contoh generik: `Reflection` ×≥2 → satu mini-ADR sahaja *(kiraan sebenar dari pass penuh, belum diverifikasi)*. Nota sejarah: ADR-mini-002 (`Scenario with Questions`) SUPERSEDED oleh entri kanon taxonomy v0.3 — rekod, jangan padam.
- Sebarang cadangan yang, jika diterima, menjadi P-baru / T2-baru / μB-baru. **Registry μB kini TERTUTUP dalam v0.3** — sebarang μB baru wajib mini-ADR, tiada pengecualian.
- Mini-ADR = cadangan; keputusan milik manusia; masuk dropdown hanya selepas LOCKED.

## 6. Sumber kanon

JSON keluaran CAIR (dengan `source_md5`) = kanon topic-level. Export CSV = terbitan sahaja, sah HANYA jika diserialize ikut peraturan objek atomik (CAIR-OUTPUT-CONTRACT §4). Preseden: CSV 05/07 REJECTED — label↔rasional bergeser; jangan bind dari CSV yang belum lulus semakan objek-demi-objek terhadap JSON.

## 7. Trigger untuk skrip transform (belum sekarang)

Peta ini kekal manual sehingga volume melebihi **~3 deck** dalam satu kitaran. Trigger direkod di sini; sebelum itu, skrip = overbuild.
