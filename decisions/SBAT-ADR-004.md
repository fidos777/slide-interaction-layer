# SBAT-ADR-004 — CAIR Desk topik-level schema (one-row-per-topic)

- **Status:** Accepted
- **Date:** 2026-07-03
- **Scope:** `sbat/cair-decision-desk.html` (CAIR Decision Desk) + Supabase `cair_decisions`

## 1. Keputusan — bentuk skema topik-level

Granulariti keputusan CAIR = **TOPIK** (T1–TX per PL), bukan slaid. Bariah sahkan ini.

- **Satu topik = satu baris** dalam `cair_decisions`.
- Kunci upsert = **`UNIQUE(course_code, pl, topik)`** (migrasi via connector; `slide_ref` dibiar **nullable** untuk keserasian, tidak dibuang).
- `decision_type = "topik-card"` — **label statik**, BUKAN sebahagian kunci.
- `choice` = satu **JSON string** yang memegang seluruh kad topik:
  `{ intent(P1..P7|null), watak, scenario_hook, reflection, interaktiviti:[ {jenis, rasional, sumber} ] }` (interaktiviti min 2 untuk kad dikira siap).

### Kenapa satu-baris-per-topik (bukan satu-baris-per-bahagian)
Kalau casting / reflection / interaktiviti disimpan sebagai baris berasingan di bawah kunci `(course_code, pl, topik)`, ketiga-tiganya akan **saling tindih** pada constraint unik yang sama (upsert satu memadam yang lain). Menyatukan semua bahagian dalam satu `choice` JSON mengelak tindihan constraint dan memastikan satu kad = satu keadaan atomik.

## 2. Pengajaran — skema + kod = satu unit deploy

Insiden **03/07**: bila constraint DB diubah tanpa deploy kod yang sepadan (atau sebaliknya), `upsert` **patah** kerana `onConflict` merujuk constraint yang tidak lagi wujud / belum wujud. 

**Peraturan:** perubahan skema dan perubahan kod yang bergantung padanya mesti dianggap **satu unit deploy** — jangan pisahkan antara tangan/tetingkap/sesi. Sebab itu M2.0 mengubah `onConflict`, payload `saveCard`, dan pemetaan `loadFromSupabase` (baca **dan** tulis) serentak dalam satu commit.

## 3. Lock K2/K3/K5

K4 sahaja terbuka. K2/K3/K5 **dikunci** (dua lapis: UI tidak render + `saveCard` guard `OPEN_COURSES`) sehingga **drill sumber per-kursus** siap (extract topik dari dokumen sumber masing-masing). Data K2/K3/K5 lama kekal dalam `BARIAH_DATA` sebagai artifak, tidak dirender.

## 4. Provenans

- Data K4: `sbat/data/k4-topik.json` (BEKU, `source_md5=f8a58d5ffe172be66102a0b99df23c5b`).
- Layer `INTENT_MAP` P1–P7 diport dari lineage `Meja-Keputusan-CAIR-Bariah.html` (md5 `8cce12c60255c6b009b0b791da22636b`) — diarkib di `sbat/archive/`. `suggest[]` dikosongkan untuk K4 (watak belum diratifikasi).
