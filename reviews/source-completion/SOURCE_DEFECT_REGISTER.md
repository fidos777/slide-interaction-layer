# SOURCE_DEFECT_REGISTER

**Authority split:** DOCX = text · PDF = rendered pagination, heading numbering and visuals.

Text source: `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx`
Rendered source: `K5_PL06_T03_B02_pages_256269.pdf` (`sha256 30a6903d…f828a3f4`, 14 pp)
Scope: module pages 237–250 = physical 256–269, **offset +19 measured on all 14 pages**.

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

## D-2 — repeated `3.4.1` numbering — **`CONFIRMED_IN_RENDERED_PDF`**

**Corrected.** The DOCX text extraction reported this `NOT_DETERMINABLE` because Word's heading
numbering does not survive text export — sub-headings appeared as `###` with no numeric prefix. The
rendered PDF carries the numbering, and the defect is real.

### Measured sequence — `MEASURED_FACT`

| Rendered number | Heading | Module page | Physical page |
|---|---|---:|---:|
| **`3.4.1`** | Kerusi Taman | **242** | 261 |
| **`3.4.1`** | Papan Tanda | **243** | 262 |
| **`3.4.1`** | Tong Sampah | **245** | 264 |
| `3.4.2` | Drinking Fountain | 247 | 266 |
| `3.4.3` | BBQ pit | 249 | 268 |

**`3.4.1` is used three times.** The sequence runs **1, 1, 1, 2, 3** where it should run 1–5. Two
distinct subsections are unreachable by number, and any cross-reference to "3.4.1" is ambiguous
between three targets.

### Section 3.3 is *not* affected — `MEASURED_FACT`

| Number | Heading | Module page |
|---|---|---:|
| `3.3.1` | Struktur Persisir Air (Promenande, Jeti, Dek, Boardwalk, footbridge) | 238 |
| `3.3.2` | Struktur Teduhan | 239 |
| `3.3.3` | Kemudahan Awam | 240 |
| `3.3.4` | Water Feature (Fountain, Pond, Pool) | 241 |

Correctly sequential. **The defect is confined to 3.4.**

### Effect

None on this gate — the nine screens are mapped by heading *title*, which is unique, and all nine
verified with no mismatch. It is a **module defect** for the owner: cross-references and any generated
navigation will be wrong. Classification: **numbering defect**, confirmed, three-way collision.

### On the earlier report

The DOCX finding — that `3.3.` repeats three times across the module (p23, p75, p237) — **also stands**
and is a separate, real observation. It is not what this item refers to. The `3.4.1` collision was
simply invisible to text extraction; the earlier `NOT_DETERMINABLE` was correct for the evidence then
held, and is now superseded by the rendered document.

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

## D-6 — `fitnesss` — **NEW, adjacent to scope**

Rendered heading on module p237:

> `3.2.6  Outdoor gym & fitnesss stations`

`fitnesss` carries three `s`. The heading sits at `3.2.6`, immediately **before** `3.3` on the same
page — inside the extract, outside B02's scope, which begins at `3.3`.

Classification: **source typo**. Reported for the module owner; no B02 screen uses it.

---

## Summary

| ID | Item | Status | Blocks the gate? |
|---|---|---|---|
| D-1 | `Promenande` typo | **CONFIRMED** — 1 wrong, 2 right | no |
| D-2 | repeated `3.4.1` | **`CONFIRMED_IN_RENDERED_PDF`** — `3.4.1` used 3×; sequence 1,1,1,2,3 | no |
| D-3 | English-term styling | **CONFIRMED** — 42 terms vs a 3-term lexicon | **`OPEN_DECISION`** |
| D-4 | `reka bentuk` variant | **CONFIRMED** — spaced dominates 131:8 | no |
| D-5 | heading levels on body text | **NEW** (DOCX) | no |
| D-6 | `fitnesss` typo at 3.2.6 | **NEW** (PDF) — adjacent, outside scope | no |

## Carried forward — already settled elsewhere

`BBQ pit` lowercase `p` is now **confirmed at source**: the heading reads `### BBQ pit` and the body
`BBQ pit atau kawasan barbeku…`. The sample's source form was right. The normalisation-policy question
(list-internal consistency vs exact source reproduction) remains an `OPEN_DECISION` for a human.
