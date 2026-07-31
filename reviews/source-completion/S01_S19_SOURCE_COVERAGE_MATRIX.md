# S01_S19_SOURCE_COVERAGE_MATRIX

Source: `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx`, module pages 237–250.

```
TEXT COVERAGE:  13 of 19 VERIFIED  (preserved unchanged from the DOCX gate)
ASSET COVERAGE: 7 of 9 mapped screens now carry extracted source imagery
AUTHORITY: DOCX = text · PDF = pagination, numbering, visuals
```

---

## 1. Matrix

| # | Screen | Before | **After** | Module page | Source heading | Text | Figure | Table |
|---|---|---|---|---|---|---|---|---|
| S01 | TAJUK | PARTIAL | PARTIAL | — | — | course/topic strings only | — | — |
| S02 | DIALOG | MISSING | **MISSING — held** | — | — | none | — | — |
| S03 | OVERVIEW | MISSING | **MISSING — held** | — | — | none | — | — |
| S04 | CR_BASE Struktur Taman | VERIFIED | **VERIFIED ++** | **237** | `Struktur Taman` | ✅ intro **verbatim-matches probe VO** | — | — |
| S05 | FULL Struktur Persisir Air | PARTIAL | ✅ **VERIFIED** | **238** | `Struktur Persisir Air (…)` | ✅ intro + aspek + 5-row table | **Rajah 23** — 1 asset | ✅ |
| S06 | FULL Struktur Teduhan | PARTIAL | ✅ **VERIFIED** | **239** | `Struktur Teduhan` | ✅ intro + 5-row table | **Rajah 24** — 1 asset | ✅ |
| S07 | FULL Kemudahan Awam | PARTIAL | ✅ **VERIFIED** | **240** | `Kemudahan Awam` | ✅ intro + aspek + 3-row table | — none | ✅ |
| S08 | FULL Water Feature | PARTIAL | ✅ **VERIFIED** | **241** | `Water Feature (…)` | ✅ intro + aspek + 3-row table | — none | ✅ |
| S09 | TICK Struktur Taman | VERIFIED | VERIFIED | 237 | *(completion state)* | ✅ VO verified empty | — | — |
| S10 | CR_BASE Perabot Taman | PARTIAL | ✅ **VERIFIED** | **242** | `Perabot Taman` | ✅ section intro now available | — none | — |
| S11 | FULL Kerusi Taman | PARTIAL | ✅ **VERIFIED** | **242** | `Kerusi Taman` | ✅ intro + 3-row table | — none | ✅ |
| S12 | FULL Papan Tanda | VERIFIED | **VERIFIED ++** | **243** | `Papan Tanda` | ✅ **verbatim-matches accepted sample** | **Rajah 25 + 26** — 2 assets | ✅ |
| S13 | FULL Tong Sampah | PARTIAL | ✅ **VERIFIED** | **245** | `Tong Sampah` | ✅ intro + 3-row table | — none | ✅ |
| S14 | FULL Drinking Fountain | PARTIAL | ✅ **VERIFIED** | **247** | `Drinking Fountain` | ✅ intro + 2-row table | — none | ✅ |
| S15 | FULL BBQ pit | PARTIAL | ✅ **VERIFIED** | **249** | `BBQ pit` | ✅ intro + 1-row table | — none | ✅ |
| S16 | TICK Perabot Taman | PARTIAL | **PARTIAL** | 242 | *(completion state)* | inherits S10 | — | — |
| S17 | RUMUSAN | VERIFIED | VERIFIED | — | *(derived)* | ✅ accepted treatment | — | — |
| S18 | KUIZ | MISSING | **MISSING — held** | — | — | none | — | — |
| S19 | TAMAT | MISSING | **MISSING — held** | — | — | none | — | — |

**All module pages are now MEASURED from the rendered PDF folio** (`Mukasurat NNN`), offset +19. The `~` interpolation markers are retired; three had been wrong by one page (S05, S08, S12) — see `B02_PAGE_AND_NODE_MAP.md` §3.

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

## 4. Asset coverage — SUPERSEDED and now largely closed

**Text coverage 13/19 (preserved) · asset coverage 7 of 9 mapped screens.**

| Screen | Assets | Kind |
|---|---:|---|
| S05 · S06 | 1 each | numbered figure (Rajah 23, 24) |
| S11 | 3 | table photographs, p242–243 |
| S12 | 2 | numbered figures (Rajah 25, 26), p245 |
| S13 | 4 | table photographs, p246–247 |
| S14 | 2 | table photographs, p248–249 |
| S15 | 1 | table photograph, p249 |
| **S07 · S08** | **0** | **`NO_DEDICATED_SOURCE_IMAGE`** |

**14 assets extracted**, 408 KB, each with crop boundary, dimensions and SHA-256.

**The earlier "six screens have no figure" finding is withdrawn.** It was an artefact of text
extraction — only captioned `Rajah` figures survive text export, and the module carries 10 further
unnumbered photographs inside specification tables. Only **S07 and S08** genuinely have none, confirmed
by position in the rendered PDF.

## 5. What each remaining gap needs

| Gap | Needs |
|---|---|
| ~~Figure binaries~~ | ✅ **closed** — 14 extracted |
| Visual for **S07, S08 only** | **nothing will supply one** — Option A (native typology diagram) or B (cropped table); `DEC-1` |
| ~~Measured per-screen module pages~~ | ✅ **closed** — measured, offset +19 |
| S02 / S03 | ratified casting and reflection decisions — **not** source |
| S18 | quiz source |
| D-2, D-3 | rendered document; a lexicon scope decision |
