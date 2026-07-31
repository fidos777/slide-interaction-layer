# S01_S19_SOURCE_COVERAGE_MATRIX

Source: `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx`, module pages 237–250.

```
TEXT COVERAGE: 15 of 19 screens now source-backed  (was 4)
ASSET COVERAGE: 0 of 19 — no image binary obtainable this session
```

---

## 1. Matrix

| # | Screen | Before | **After** | Module page | Source heading | Text | Figure | Table |
|---|---|---|---|---|---|---|---|---|
| S01 | TAJUK | PARTIAL | PARTIAL | — | — | course/topic strings only | — | — |
| S02 | DIALOG | MISSING | **MISSING — held** | — | — | none | — | — |
| S03 | OVERVIEW | MISSING | **MISSING — held** | — | — | none | — | — |
| S04 | CR_BASE Struktur Taman | VERIFIED | **VERIFIED ++** | **237** | `Struktur Taman` | ✅ intro **verbatim-matches probe VO** | — | — |
| S05 | FULL Struktur Persisir Air | PARTIAL | ✅ **VERIFIED** | ~237 | `Struktur Persisir Air (…)` | ✅ intro + aspek + 5-row table | **Rajah 23** | ✅ |
| S06 | FULL Struktur Teduhan | PARTIAL | ✅ **VERIFIED** | ~239 | `Struktur Teduhan` | ✅ intro + 5-row table | **Rajah 24** | ✅ |
| S07 | FULL Kemudahan Awam | PARTIAL | ✅ **VERIFIED** | ~240 | `Kemudahan Awam` | ✅ intro + aspek + 3-row table | — none | ✅ |
| S08 | FULL Water Feature | PARTIAL | ✅ **VERIFIED** | ~240 | `Water Feature (…)` | ✅ intro + aspek + 3-row table | — none | ✅ |
| S09 | TICK Struktur Taman | VERIFIED | VERIFIED | 237 | *(completion state)* | ✅ VO verified empty | — | — |
| S10 | CR_BASE Perabot Taman | PARTIAL | ✅ **VERIFIED** | **242** | `Perabot Taman` | ✅ section intro now available | — none | — |
| S11 | FULL Kerusi Taman | PARTIAL | ✅ **VERIFIED** | ~242 | `Kerusi Taman` | ✅ intro + 3-row table | — none | ✅ |
| S12 | FULL Papan Tanda | VERIFIED | **VERIFIED ++** | ~244 | `Papan Tanda` | ✅ **verbatim-matches accepted sample** | **Rajah 25 + 26** | ✅ |
| S13 | FULL Tong Sampah | PARTIAL | ✅ **VERIFIED** | ~245 | `Tong Sampah` | ✅ intro + 3-row table | — none | ✅ |
| S14 | FULL Drinking Fountain | PARTIAL | ✅ **VERIFIED** | ~247 | `Drinking Fountain` | ✅ intro + 2-row table | — none | ✅ |
| S15 | FULL BBQ pit | PARTIAL | ✅ **VERIFIED** | ~249 | `BBQ pit` | ✅ intro + 1-row table | — none | ✅ |
| S16 | TICK Perabot Taman | PARTIAL | **PARTIAL** | 242 | *(completion state)* | inherits S10 | — | — |
| S17 | RUMUSAN | VERIFIED | VERIFIED | — | *(derived)* | ✅ accepted treatment | — | — |
| S18 | KUIZ | MISSING | **MISSING — held** | — | — | none | — | — |
| S19 | TAMAT | MISSING | **MISSING — held** | — | — | none | — | — |

`~` = module page interpolated from measured section anchors, not read off the page.

## 2. Movement

| Status | Before | After | Change |
|---|---:|---:|---|
| `VERIFIED` | 4 | **13** | **+9** |
| `PARTIAL` | 11 | **2** | −9 |
| `MISSING` | 4 | **4** | held |

**Nine screens moved from `PARTIAL` to `VERIFIED` on text.** All nine directed mappings matched a real
source heading, in source order, with **no mismatch**.

## 3. Screens held open — unchanged and deliberate

| Screen | Why the module cannot close it |
|---|---|
| **S02** DIALOG | needs a **casting decision**; slot `(K5, PL06, s02)` is empty and the current B02 cast is not provable. The module has no scenario or character content |
| **S03** OVERVIEW | needs a **reflection question**; slot `(K5, PL06, s03)` is empty |
| **S18** KUIZ | **no assessment material of any kind** was found in scope — no question, option, answer key or routing. None is constructed |
| **S19** TAMAT | no closing content in scope |

These are **decision gaps, not source gaps** for S02/S03. The module could not close them even if it
were complete, because what is missing is a ratified decision.

## 4. The asset gap — now the only material blocker

**Text coverage 13/19 · figure coverage 0/19.**

Four figures exist in scope (`Rajah 23`–`26`) covering three screens; **six of the nine mapped screens
have no figure at all**, and no image binary could be extracted this session
(`B02_ASSET_MANIFEST.md` §3).

**Six screens will have no visual regardless of extraction** — the module simply does not provide one.
That is recorded, not filled.

## 5. What each remaining gap needs

| Gap | Needs |
|---|---|
| Figure binaries for S05, S06, S12 | the PDF, or four exported images, or a page-237–250 DOCX |
| Visual for S07, S08, S11, S13, S14, S15 | **nothing will supply one** — decide whether the specification table carries the region |
| Measured per-screen module pages | rendered pagination |
| S02 / S03 | ratified casting and reflection decisions — **not** source |
| S18 | quiz source |
| D-2, D-3 | rendered document; a lexicon scope decision |
