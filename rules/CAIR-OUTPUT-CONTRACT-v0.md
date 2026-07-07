# CAIR Output Contract v0
**Sasaran repo:** `rules/CAIR-OUTPUT-CONTRACT-v0.md` · Terpakai pada SEMUA output cadangan interaktiviti CAIR (JSON dan sebarang export terbitan).

## 1. Objek cadangan minimum yang sah

```json
{
  "jenis_taxonomy": "Gated Click & Reveal",
  "alias_kontrak": "Click and Show",
  "variant_koordinat": "gate:on",
  "jenis_asal_sistem": "Click-and-Show",
  "rasional": "Fakta sokongan (21 sub-bahagian) — kad rujukan pantas selepas scenario",
  "status": "cadangan — Bariah putus/tolak/tambah"
}
```

Header fail (sekali per fail output):

```json
{
  "taxonomy_version": "v0.4",
  "taxonomy_md5": "d6cf96061bbbfddde6829074930eea98",
  "source_file": "<nama fail sumber>",
  "source_md5": "<md5 sumber>"
}
```

## 2. Medan & nilai dibenarkan

| Medan | Wajib | Nilai dibenarkan |
|---|---|---|
| `jenis_taxonomy` | ✅ | **Enum tertutup:** nama entri taxonomy **v0.3** sahaja — `Gated Click & Reveal` · `Reveal` (+ koordinat) · `Detail Screen + Kembali` · `Drag & Drop` · **`Scenario with Questions`** · `Branching Scenario` · nama KANDIDAT bernama (`Hidden Objects`, `Image Swap`) · **`TIADA-PADANAN`** |
| `alias_kontrak` | disyorkan | **Dari `lexicon/ALIAS-GLOSSARY-v0.md` SAHAJA (exact match), atau kosong — kosong sentiasa sah.** Vocabulary kontrak SnG yang diluluskan (cth `Click and Show`, `Drag and Drop`) — lapisan #2, lihat §3 |
| `variant_koordinat` | jika relevan | Koordinat sedia ada sahaja (cth `gate:on`, `-visited-tick`, `presentation:overlay-with-close`) — koordinat BUKAN tempat mencipta nama baru |
| `jenis_asal_sistem` | ✅ | Label bebas penjana — DIKEKALKAN, bukan dibuang. Wajib bila `TIADA-PADANAN`; digalakkan sentiasa |
| `rasional` | ✅ | Teks bebas — WAJIB dalam objek yang sama dengan labelnya (§4) |
| `status` | ✅ | Verbatim: `"cadangan — Bariah putus/tolak/tambah"` — baris provenance ini tak boleh digugurkan |

## 3. Tiga lapisan label + makna `TIADA-PADANAN`

| Lapisan | Medan | Maksud |
|---|---|---|
| 1 — Kanon | `jenis_taxonomy` | Nama entri taxonomy v0.3, ATAU `TIADA-PADANAN`. Satu-satunya lapisan yang binding table baca sebagai padanan |
| 2 — Kontrak | `alias_kontrak` | Vocabulary kontrak SnG yang diluluskan (cth "Click and Show" ↔ `Gated Click & Reveal`, "Drag and Drop" ↔ `Drag & Drop`). Bahasa client/kontrak — DIKEKALKAN, tak pernah menggantikan lapisan 1 |
| 3 — Mentah | `jenis_asal_sistem` | Label bebas yang penjana/sistem emit — dikekalkan untuk audit + lexicon |

- `jenis_taxonomy` kekal **dakwaan padanan** sahaja — BUKAN kelulusan binding. Binding kekal kerja binding table; RESOLVED/LOCKED milik manusia.
- `TIADA-PADANAN` ialah **pengakuan jujur** penjana bahawa cadangannya tiada nama taxonomy. Kesan hiliran (ikut CAIR-TO-BINDING-MAP): baris `AMBIGUOUS` automatik. Hutang binding jadi **nampak**, bukan senyap.
- Penjana DILARANG "menyelesaikan" TIADA-PADANAN dengan mencipta nama sendiri, meminjam alias, atau meminjam nama generik.

## 4. Peraturan objek atomik — label + rasional tak boleh dipisah

Label dan rasionalnya WAJIB hidup dalam satu objek. Sebab (preseden sebenar): CSV export 05/07 menggeser label terhadap rasional kerana kedua-duanya dicantum secara **kedudukan** semasa serialize — "Click-and-Show" membawa rasional Scenario, "Drag-and-Drop" membawa rasional Reflection. CSV 05 REJECTED untuk binding; JSON kekal kanon topic-level.

**Peraturan export:** sebarang CSV/jadual terbitan mesti serialize **dari objek atomik yang sama** — medan demi medan, satu objek satu baris. JANGAN sesekali cantum label dan rasional melalui indeks/kedudukan senarai berasingan.

## 5. Contoh sah (v0.3)

```json
{ "jenis_taxonomy": "Scenario with Questions",
  "jenis_asal_sistem": "Scenario with Questions", "rasional": "…", "status": "cadangan — …" }
  // ✅ entri kanon v0.3 — SnG contract vocabulary, G6-proven sebagai base player pattern

{ "jenis_taxonomy": "Gated Click & Reveal", "alias_kontrak": "Click and Show",
  "jenis_asal_sistem": "Click-and-Show", "rasional": "…", "status": "cadangan — …" }
  // ✅ alias dikekalkan; binding kanon = Gated Click & Reveal

{ "jenis_taxonomy": "Drag & Drop", "alias_kontrak": "Drag and Drop",
  "jenis_asal_sistem": "Drag-and-Drop", "rasional": "…", "status": "cadangan — …" }
  // ✅ ejaan kanon dengan '&'

{ "jenis_taxonomy": "TIADA-PADANAN",
  "jenis_asal_sistem": "Reflection", "rasional": "…", "status": "cadangan — …" }
  // ✅ Reflection kekal TIADA-PADANAN sehingga diverifikasi

{ "jenis_taxonomy": "Branching Scenario",
  "jenis_asal_sistem": "decision-consequence", "rasional": "…", "status": "cadangan — …" }
  // ✅ nama T2 sah — padanan sah ≠ kebenaran build (gate demand kekal)
```

## 6. Contoh TERLARANG

```json
{ "jenis_taxonomy": "Modal" }        ❌  PR-001.3
{ "jenis_taxonomy": "Accordion" }    ❌  PR-001.3
{ "jenis_taxonomy": "Tooltip" }      ❌
{ "jenis_taxonomy": "Tabs" }         ❌
{ "jenis_taxonomy": "PopupCard" }    ❌  nama komponen generik — mana-mana pun
```

Nama komponen UI generik tak boleh muncul dalam `jenis_taxonomy` — walau penjana yakin, walau "sementara". Jika penjana rasa Modal sesuai → itu `TIADA-PADANAN` + `jenis_asal_sistem` + rasional, dan menu konversi POP UP berjalan di peringkat binding.

## 7. Apa yang v0 TIDAK ada — sengaja

Tiada confidence score · tiada medan tracking/analitik · tiada medan automasi · tiada versioning per cadangan. Ditambah hanya bila trigger bertulis berlaku.
