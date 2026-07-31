# SOURCE_COMPLETION_IMPLEMENTATION_PLAN — K5 PL06 T3 B02

```
GATE STATUS: TEXT COMPLETE (13/19, preserved) · ASSETS EXTRACTED (14, 7 of 9 screens)
AUTHORITY: DOCX = text · PDF = rendered pagination, heading numbering, visuals
No PPTX generated. Accepted visual sample unmodified.
```

---

## 1. What this gate achieved

| Step | Result |
|---|---|
| Source acquired | via Google Drive after three failed attachments — **DOCX, 16.8 MB** |
| Scope confirmed | module pages **237–250**, exactly as specified (TOC-measured) |
| Sections mapped | 3.3 @ p237, 3.4 @ p242, boundary 3.5 @ p251 |
| Screens mapped | **9 of 9**, every directed assignment matching a real heading, **no mismatch** |
| Text extracted | all nine, plus the 3.4 section intro for S10 |
| Figures identified | ~~4 covering 3 screens~~ → **14 assets extracted, 7 of 9 screens** (PDF) |
| Pagination | **measured**, offset +19 on all 14 pages; 3 interpolations corrected |
| Heading numbering | **measured** — D-2 confirmed, `3.4.1` used three times |
| Defects | D-1 confirmed · D-2 **not confirmed as stated** · D-3 confirmed and much larger than expected · D-4 confirmed · **D-5 new** |
| Drafts | display + VO for all 8 outstanding screens, all within budget |
| Probe corroborated | S04 and S12 source text **matches probe v0.1 verbatim** |

## 2. What remains

| # | Gap | Blocking | Needs |
|---|---|---|---|
| ~~G-1~~ | ~~Figure binaries~~ | — | ✅ **CLOSED** — 14 extracted with crop boundaries and hashes |
| **G-2** | **Two screens have no source image** — S07, S08 only | their visual regions | **a decision, not a file** — `DEC-1` |
| **G-3** | D-3 lexicon scope — 42 terms vs a 3-term list | italic treatment | a human cut-line — see §4 |
| ~~G-4~~ | ~~D-2 numbering~~ | — | ✅ **CLOSED** — `CONFIRMED_IN_RENDERED_PDF` |
| **G-5** | S02 / S03 / S18 / S19 | 4 screens | ratified decisions and quiz source — **not** the module |
| ~~G-6~~ | ~~Measured module pages~~ | — | ✅ **CLOSED** — measured; S05, S08, S12 corrected by one page |

**Only G-2 and G-3 remain, and both are decisions rather than missing files.** G-2 covers two screens;
G-3 affects styling, not content.

## 3. Next steps, in order

### ~~Step 1 — close G-1~~ ✅ DONE
14 assets extracted to `source-assets/` with asset_id, source component, module page, physical page,
crop boundary, file type, dimensions, SHA-256, intended screen and usage status.

### Step 2 — resolve G-2 for **S07 and S08 only** *(decision required)*
Both confirmed `NO_DEDICATED_SOURCE_IMAGE` by position in the rendered PDF. Two source-bound options,
**prepared but not selected and not implemented**:

| Option | Effect |
|---|---|
| **A — source-derived native typology diagram** | native shapes built from the screen's own specification table; every label verbatim. Fills the panel, matches the deck's native-geometry approach, scales cleanly. It is a *rendering of* the source, not an image *from* it — provenance must say so |
| **B — cropped source table** | crop the specification table from the rendered PDF. Unambiguously a module artefact, zero interpretive step. But small type in a 5.8621 × 5.1387 in panel — legibility needs testing, and it duplicates content the display already carries |

Neither invents imagery; no external image is sourced. **Not selected.**

### Step 3 — resolve G-3 *(decision required)*
Pick the lexicon cut-line: Tier 1 (12 terms) · Tier 1+2 (30) · all (42). **Tier 1 recommended** — it
keeps italic on learner-facing type names and out of specification tables. Not decided.

### Step 4 — build the source-bound deck
Only after 1–3. Apply the **accepted v0.2 treatment geometry unchanged**; fill display and VO from
`DISPLAY_VO_DRAFT_MATRIX.md`; bind assets; keep S02/S03/S18/S19 as `SOURCE PENDING`.
Output would be `…SOURCE_BOUND_v0_1.pptx` — a **new artifact**, not an edit of the accepted sample.

### Step 5 — re-run checks
Package + rule suite, plus new source-fidelity checks: every display proposition traceable to a page;
`Promenade` not `Promenande`; `reka bentuk` not `rekabentuk`; `BBQ pit` lowercase.

## 4. Decisions needed before Step 4

| # | Decision | Recommendation |
|---|---|---|
| **DEC-1** | Visual region for **S07 and S08** | Option **A** (native typology diagram) or **B** (cropped table) — **not selected** |
| **DEC-2** | Italic lexicon scope | **Tier 1**, 12 terms |
| **DEC-3** | `Promenande` → `Promenade` in display/VO | **yes** — heading typo, table is correct |
| **DEC-4** | `rekabentuk` → `reka bentuk` | **yes** — 131:8 majority |
| **DEC-5** | Report D-5 heading defect to the module owner | **yes** — affects their TOC, not our deck |
| **DEC-6** | Report **D-2** `3.4.1` three-way collision to the module owner | **yes** — cross-references and generated navigation are ambiguous |
| **DEC-7** | Confirm the S14 asset-page refinement (§3 of the manifest) | asset positions put Drinking Fountain images on p248–249, not p247–248 |

All five are recommendations. None is applied.

## 5. Constraints held

| Constraint | Status |
|---|---|
| Do not generate the source-bound PPTX yet | ✅ none generated |
| Do not modify the accepted visual sample | ✅ `8d93e2ce…646a982b` unchanged |
| Do not unlock K5 | ✅ |
| Do not issue canonical IDs | ✅ proposed asset IDs key to the module's own `Rajah` numbering, and are proposals |
| Do not fabricate a visual where the module provides none | ✅ six screens recorded as having none; `source-assets/` empty |
| Keep S02, S03, S18, S19 open | ✅ all four held |

## 6. Honest position on the two sources

The split works. The DOCX gave clean, complete text for nine screens; the PDF gave the three things
text cannot carry — fixed pagination, Word heading numbering, and embedded images.

**What the reconciliation changed:**

| Finding | Was | Now |
|---|---|---|
| D-2 `3.4.1` | `NOT_DETERMINABLE` | **`CONFIRMED_IN_RENDERED_PDF`** — three-way collision |
| Screens without imagery | 6 | **2** (S07, S08) |
| Module pages | interpolated | **measured**; S05, S08, S12 each off by one |
| `IMG-05` / ms 243 | "within interpolation error" | **exactly confirmed** — the probe was right |

**What it did not change:** the text extraction, the display and VO drafts, and the 13/19 text-coverage
result — all preserved. The DOCX-era `NOT_DETERMINABLE` on D-2 was correct for the evidence then held;
it did not need to be right, it needed to be honest, and it was superseded rather than overturned.
