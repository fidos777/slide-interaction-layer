# Binding Table v0 — Template
**Sasaran repo:** `binding/BINDING-TABLE-TEMPLATE-v0.md` — salin ke `binding/<DECK>-binding-v0.md` per deck.

## 1. Metadata (isi SEBELUM mula)

| Medan | Nilai |
|---|---|
| Deck | `<nama deck / PL>` |
| Fail sumber | `<path PPTX / raw notes>` |
| Versi taxonomy | v0.2 — salinan kanon |
| md5 taxonomy | `<md5>` ← WAJIB. Freeze sebelum pass; jangan jalan atas salinan divergent |
| Reviewer | Firdaus |
| Tarikh | |
| Pass | 1 (draf AI) / 2 (selepas sesi kad) |

## 2. Nota guna

- AI worker isi baris `DRAFT`/`AMBIGUOUS` ikut `instructions/AI-WORKER-COLD-PASS-INSTRUCTIONS-v0.md`.
- Firdaus semak setiap `DRAFT`/`AMBIGUOUS` → `RESOLVED` / kad / betulkan.
- **Bariah TIDAK nampak jadual ini.** Dia terima kad klarifikasi yang dijana dari baris `AMBIGUOUS` sahaja.
- PR-001 mesti dimuat sebelum sebarang skill interaksi generik disentuh.

## 3. Peraturan status (faham dulu, isi kemudian)

**`binding_status` — kitaran hayat keputusan:**

| Nilai | Maksud |
|---|---|
| `DRAFT` | AI cadang, belum disemak manusia |
| `AMBIGUOUS` | ≥2 calon. `ambiguity_reason` + senarai calon + `card_id` WAJIB |
| `RESOLVED` | Keputusan produksi Firdaus. Cukup untuk build **risiko rendah sahaja** — risiko rendah = (a) tak sentuh pattern LOCKED / komponen G6-proven DAN (b) boleh patah balik pra-commit |
| `LOCKED` | Disahkan Bariah; pertukaran lock direkod di `prov_ref`. **WAJIB sebelum** (a) promosi apa-apa ke taxonomy, (b) diguna sebagai bukti dalam ADR |
| `DEFERRED` | Sah wujud, binding ditangguh. JANGAN padam — guard Bitumen-Sheet |
| `—` | Tidak applicable — untuk baris `row_disposition` IMPL-ONLY / REJECTED / DUPLICATE sahaja |

`AMBIGUOUS → RESOLVED` memerlukan `decided_by: Firdaus`. `RESOLVED → LOCKED` memerlukan jawapan Bariah bertulis (`decided_by: Bariah`, kad di `card_id`).

**`row_disposition` — jenis baris:**

| Nilai | Maksud |
|---|---|
| `INTERACTION` | Momen interaksi sebenar — sahaja yang masuk `N_int` |
| `IMPL-ONLY` | Tak nampak pada learner. Kekal untuk audit, keluar dari metrik, tak masuk taxonomy |
| `REJECTED` | Bukan interaksi / cadangan generik ditolak (log RS wajib) |
| `DUPLICATE` | Token+slide sudah ada baris — pautkan `row_id` asal di `notes` |

## 4. Kolum & nilai dibenarkan

| Kolum | Nilai dibenarkan |
|---|---|
| `row_id` | `BIND-<DECK>-###` |
| `slide` | verbatim dari fail sumber |
| `sb_token` | petikan tepat dalam `"..."` — JANGAN parafrasa |
| `sb_context` | teks minimal/sederhana/padat · VO ada/tiada · imej/diagram |
| `grammar` | μB-set · Gate · Topology{flat-set, hub-spoke, mapping, dag-with-history, timeline-coupled} · Presentation{inline, overlay(close), overlay(vo-timed), detail-screen(Kembali)} |
| `kelas` | P / R / T2 / VARIAN / μB / — |
| `proposed_binding` | nama dropdown-sah SAHAJA; token ambiguous → senarai calon `{...}` |
| `binding_status` | DRAFT / AMBIGUOUS / RESOLVED / LOCKED / DEFERRED / — (tidak applicable: IMPL-ONLY / REJECTED / DUPLICATE) |
| `row_disposition` | INTERACTION / IMPL-ONLY / REJECTED / DUPLICATE |
| `provenance` | confirmed-written / confirmed-from-file / confirmed-verbal / inferred |
| `prov_ref` | fail SS + tarikh / `deck:slide` / `card_id` — mesti resolve ke fail, bukan ingatan |
| `tracking` | none / completion / interaction-path / — · `—` untuk REJECTED/DUPLICATE sahaja; IMPL-ONLY guna `none` (jelas ia tiada kesan learner/LMS, bukan obscure). Baris AMBIGUOUS: isi ikut calon paling strict (strictest-wins), catat di `notes` jika tak pasti |
| `ambiguity_reason` | token-tanpa-qualifier / spec-vs-build-bercanggah / kata-kerja-tak-dikenali / lain (nyatakan) / — |
| `card_id` | `CARD-###` / — |
| `decided_by` | AI-draft / Firdaus / Bariah / — · audit-critical: siapa tetapkan status semasa |
| `notes` | bebas — rujukan OPEN-x, pautan DUP, dll |

## 5. Jadual kerja — mula di sini

| row_id | slide | sb_token | sb_context | grammar | kelas | proposed_binding | binding_status | row_disposition | provenance | prov_ref | tracking | ambiguity_reason | card_id | decided_by | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | | | | |

## 6. Contoh rujukan — PADAM seksyen ini sebelum commit data sebenar

| row_id | sb_token | kelas | proposed_binding | binding_status | row_disposition | tracking | ambiguity_reason |
|---|---|---|---|---|---|---|---|
| CONTOH-1 | "POP UP + close button" (PL06T3 s7) | VARIAN | reveal / overlay-with-close | DEFERRED | INTERACTION | none | — |
| CONTOH-2 | "POP UP" *(tanpa qualifier)* | — | {overlay-with-close, overlay-maintain-VO, inline-reveal, detail-screen-kembali} | AMBIGUOUS | INTERACTION | none | token-tanpa-qualifier → CARD-### |
| CONTOH-3 | "pelajar pilih tindakan, nampak akibat" | T2 | Branching Scenario *(qualifier wajib)* | AMBIGUOUS | INTERACTION | interaction-path | gate demand belum dipenuhi → kad binary A/B |
| CONTOH-4 | "Branching out (full screen).. Kembali" | P *(sme_visible: true)* | Detail Screen + Kembali | LOCKED *(konsep; build s06 → OPEN-b)* | INTERACTION | none | — |
| CONTOH-5 | "macam Click & Reveal tapi tanpa tick" | VARIAN | Gated Click & Reveal, koordinat −visited-tick | RESOLVED | INTERACTION | completion | — |
| CONTOH-6 | "POP UP + maintain, NO close button, with VO" | T2 | overlay-maintain-VO — coupling audio timeline | DEFERRED | INTERACTION | none | — |
| CONTOH-7 | *(tiada token SB)* preload imej drag items | — | — | — | IMPL-ONLY | none | — |
| CONTOH-8 | cadangan skill generik "Accordion (P2)" | — | — | — | REJECTED | — | PR-001 → log RS |

## 7. Blok metrik

```
N_total_rows            = SEMUA baris dalam jadual kerja, termasuk baris audit
                          (IMPL-ONLY, REJECTED, DUPLICATE) =
N_int                   = N_total − (IMPL-ONLY + REJECTED + DUPLICATE) =
coverage %              = baris INTERACTION yang map kepada komposisi/varian
                          yang SUDAH WUJUD dalam taxonomy v0.2, tanpa calon
                          P-baru/T2-baru, ÷ N_int =
new-pattern demand      = kiraan baris kelas P-baru / T2 BELUM dalam taxonomy =
ambiguity rate          = AMBIGUOUS ÷ N_int  (ukur selepas draf AI, SEBELUM sesi kad) =
implementation-only rate= IMPL-ONLY ÷ N_total =
tracking-required rate  = (tracking ≠ none) ÷ N_int
                          (baris AMBIGUOUS: nilai strictest-wins dari calon) =
SME-clarification load  = bilangan kad SEBENAR dihantar =

NOTA COVERAGE:
- DEFERRED dikira covered HANYA jika proposed_binding sudah wujud dalam
  taxonomy v0.2 (cth overlay-with-close ✓; topology baru tanpa entri ✗).
- Coverage ukur EKSPRESIF taxonomy, BUKAN buildability — baris yang map ke
  T2 parked (cth overlay-maintain-VO) covered tetapi TAK BOLEH SHIP
  sehingga gate demand dipenuhi. Jangan laporkan coverage sebagai "% siap".

AMBANG: coverage ≥ 80% · demand ≤ 2 · ambiguity ≤ 30% · load muat ≤ 2 sesi WhatsApp
Mana-mana gagal → BERHENTI, rujuk stop conditions SOP. Jangan tambah entri untuk "lulus".
```

## 8. Log RS — Rejected Suggestions

| RS-id | tarikh | deck:slide | cadangan generik | tindakan diambil | row_id |
|---|---|---|---|---|---|
| | | | | | |

*Tolak-tanpa-log = tak berlaku.*
