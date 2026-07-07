# ALIAS-GLOSSARY-v0
**Sasaran repo:** `slide-interaction-layer/lexicon/ALIAS-GLOSSARY-v0.md` · Status: **v0 draf**
**Tujuan:** Senarai kanon alias kontrak/client yang DILULUSKAN, dipetakan ke nama kanon taxonomy. Alias membantu terjemahan sahaja — nama kanon kekal satu-satunya nilai `jenis_taxonomy`.
**Pin taxonomy:** v0.3 · md5 `f9deab7c07f57e7986d20ed19816661b` *(working)* — **WAJIB re-pin selepas v0.3 muktamad jika md5 berubah.**

## Jadual alias diluluskan

| alias_kontrak | `jenis_taxonomy` kanon | `jenis_asal_sistem` dikenali | status | provenance | nota |
|---|---|---|---|---|---|
| Click and Show | Gated Click & Reveal | Click-and-Show | APPROVED | Kontrak SnG / v0.3 | Alias sahaja; kanon kekal Gated Click & Reveal |
| Drag and Drop | Drag & Drop | Drag-and-Drop | APPROVED | Kontrak SnG / v0.3 | Ejaan alias guna "and"; kanon guna "&" |
| Scenario with Questions | Scenario with Questions | Scenario with Questions | APPROVED | Kontrak SnG / G6-proven / v0.3 | Alias dan kanon nama sama |

## Peraturan

1. `alias_kontrak` mesti dipilih dari glosari ini ATAU dibiarkan kosong. **Kosong sentiasa sah** — alias optional, bukan gate.
2. **Padanan alias = exact string match SAHAJA.** "Click & Show", "Scenario with Question" (singular), atau mana-mana varian ejaan yang tiada dalam jadual = BUKAN padanan. Tiada fuzzy match, tiada padanan ihsan.
3. Varian ejaan mentah yang baru dikesan → tambah ke kolum `jenis_asal_sistem` melalui semakan (provenance direkod), bukan melalui tekaan penjana.
4. Istilah client-facing yang tak dikenali TIDAK mencipta alias secara automatik. Alias baru = provenance + semakan.
5. Alias tak pernah mengatasi taxonomy — arah terjemahan sentiasa alias → kanon, tak pernah sebaliknya.
6. Nama implementasi/komponen BUKAN alias (INV-5).

## Contoh BUKAN-alias

| Istilah | Sebab |
|---|---|
| Reflection | `TIADA-PADANAN` sehingga diverifikasi — bukan alias, bukan kanon |
| PopupModal | Nama komponen/implementasi |
| Modal / Accordion / Tooltip / Tabs | Nama UI generik terlarang (PR-001.3) |
| Branching | Tak sah tanpa qualifier (peraturan penamaan #1) |

## Pertumbuhan (rujukan, bukan pra-bina)

Vocabulary kontrak masa depan (client lain, alias dalaman CIDB, bahasa colloquial SME) = **jadual tambahan dalam fail lexicon berasingan per-kontrak**, semua memetakan ke kanon yang sama — lapisan-2 tumbuh tanpa menyentuh lapisan-1. Jangan cipta fail kedua sebelum kontrak kedua wujud.

---
*Tiga baris hari ini. Kanon tak berubah. Exact match sahaja. Finish. Package. Close.*
