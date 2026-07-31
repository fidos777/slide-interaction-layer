# SOURCE_DEFECT_REGISTER

Source: `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx`
Scope: module pages 237–250. All counts measured on the extracted scope unless stated.

---

## D-1 — `Promenande` / `Promenade` — **CONFIRMED**

| Form | Count in scope | Location |
|---|---:|---|
| **`Promenande`** ❌ | **1** | section heading: `Struktur Persisir Air (Promenande, Jeti, Dek, Boardwalk, footbridge)` |
| `Promenade` ✅ | **2** | table row label, and example `Promenade Tasik Titiwangsa, KL` |

**Verdict: typo in the heading; the table is correct.** The intended form is `Promenade` — it carries
the row definition *and* a real place name. The heading's parenthetical list is the only wrong instance.

**Treatment:** use `Promenade` in display and VO. Do not reproduce the heading's spelling.
Classification: **source typo**, isolated, unambiguous.

## D-2 — repeated `3.4.1` numbering — **NOT CONFIRMED AS STATED**

Searched the TOC and the scope text. Reporting what is there, not what was expected.

| Finding | Detail |
|---|---|
| `3.4.1` in the TOC | **absent** — no such entry exists |
| Sub-headings within 3.3 / 3.4 | **unnumbered** in this text representation — rendered as `###`, no numeric prefix |
| Numbering that *does* repeat | **`3.3.` appears three times** across the module: p23 `Kawasan Hijau dan Zon Penampan` · p75 `Akta, Undang-Undang Kecil, Peraturan dan Garis Panduan` · **p237 `Struktur Taman`** |

Two readings, and the evidence does not choose between them:

1. **The observation refers to the `3.3` repetition** — which is real and measured above, and does
   touch B02 because `3.3 Struktur Taman` is one of the three colliding entries.
2. **The numbering is Word auto-numbering** applied to sub-headings and **dropped by text extraction**.
   In that case a repeated `3.4.1` could exist in the rendered document and be invisible here.

**Status: `NOT_DETERMINABLE` from the text representation.** Resolving it needs the rendered document —
the PDF, or a look at the DOCX numbering definitions. It does **not** block the nine screens: their
headings are unambiguous by title, and §3 of `B02_PAGE_AND_NODE_MAP.md` verifies all nine against the
directed mapping with no mismatch.

## D-3 — English-origin term styling — **CONFIRMED, and much larger than the current lexicon**

**42 distinct English-origin terms in scope.** The accepted lexicon holds **three**.

| Tier | Terms |
|---|---|
| **Learner-facing type names** (already in the sample or its labels) | `Water Feature` · `Drinking Fountain` · `BBQ pit` · `Promenade` · `Boardwalk` · `Footbridge` · `Gazebo` · `Pergola` · `Canopy` · `Fountain` · `Pond` · `Pool` |
| **Technical / specification vocabulary** (in tables) | `stainless steel` · `pressure-treated` · `mortise and tenon joints` · `outdoor sealant` · `wood oil` · `precast concrete` · `expansion joints` · `exposed aggregate` · `self-cleaning` · `push-button valve` · `shut-off valve` · `fade-resistant` · `firebrick` · `cast iron` · `liner` · `faucet` · `basin` · `galvanized and powder-coated steel` |
| **Acronyms / product designations** | `WPC` · `Wood-Plastic Composite` · `HDPE` · `ACP` · `HPL` · `High-Pressure Laminate` · `FRC` · `Fiber-Reinforced Concrete` · `UV` (×7) · `Universal Design` |

**The module itself applies no italic styling to any of them** — they appear in plain text throughout.

**This is a scope decision, not a formatting one.** Italicising all 42 would put half the specification
tables in italic. The tiers above are offered as a cut-line, not chosen:

- Tier 1 only → extends the lexicon 3 → 12, keeps italic meaningful on learner-facing type names
- Tier 1 + 2 → 30 terms, italic becomes the dominant style in tables
- All → 42, italic loses signal

**`OPEN_DECISION`.** The current 3-term lexicon is demonstrably too small for this scope; the right
size is a human call. Nothing is added by inference — the sample's closed 3-term list stands until
directed.

## D-4 — `reka bentuk` / `rekabentuk` — **CONFIRMED**

| Form | In scope | Whole module |
|---|---:|---:|
| **`reka bentuk`** (spaced) ✅ | **10** | **131** |
| `rekabentuk` (joined) ❌ | **1** | 8 |
| `Reka Bentuk` (title case) | 1 | 10 |
| `Rekaan` | 2 | 3 |

**Verdict: the spaced form dominates 131 : 8 — a 94 % majority.** The single in-scope joined instance is:

> `Pastikan elemen struktur mempunyai kemasan anti-gelincir, rintangan cuaca, dan **rekabentuk** mesra OKU.`

**Treatment:** use `reka bentuk` in display and VO. Classification: **terminology variant**, dominant
form clear, low risk.

## D-5 — heading levels misapplied to body text — **NEW, found during extraction**

At the end of 3.3, four consecutive lines are marked as `####` headings, but three of them are
**sentences, not headings**:

```
#### Tips Penting untuk Kontraktor                                    ← genuine heading
#### Setiap struktur mesti mematuhi Standard Kod Amalan Landskap Malaysia (MS2680).   ← body text
#### Pastikan elemen struktur mempunyai kemasan anti-gelincir…        ← body text
#### Keperluan kelulusan Pihak Berkuasa Tempatan (PBT)…               ← body text
```

The three body lines are the **content of** the Tips block and should be list items beneath it.

**Effect on this gate:** they are correctly read as content, not as structure — the map is unaffected.
**Effect on the module:** they will appear in any generated table of contents and at heading weight in
navigation. Classification: **structural defect**. Reported for the module owner; not something this
gate fixes.

Note this block sits inside `3.3` but reads as advice for *all* structures — it is not specific to
Water Feature, which is the subsection it visually follows.

---

## Summary

| ID | Item | Status | Blocks the gate? |
|---|---|---|---|
| D-1 | `Promenande` typo | **CONFIRMED** — 1 wrong, 2 right | no |
| D-2 | repeated `3.4.1` | **NOT CONFIRMED AS STATED** — no `3.4.1` exists; `3.3.` repeats 3× | no |
| D-3 | English-term styling | **CONFIRMED** — 42 terms vs a 3-term lexicon | **`OPEN_DECISION`** |
| D-4 | `reka bentuk` variant | **CONFIRMED** — spaced dominates 131:8 | no |
| D-5 | heading levels on body text | **NEW** | no |

## Carried forward — already settled elsewhere

`BBQ pit` lowercase `p` is now **confirmed at source**: the heading reads `### BBQ pit` and the body
`BBQ pit atau kawasan barbeku…`. The sample's source form was right. The normalisation-policy question
(list-internal consistency vs exact source reproduction) remains an `OPEN_DECISION` for a human.
