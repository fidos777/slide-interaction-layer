# QA_SCOPE_AND_LIMITS — v0.4.3

> **303 of 303 mechanical checks passing does not mean the deck is approved.**
> It means every check that exists passed. Stage 4.2A found a defect class that passed 188/188.
> **Stage 4.2C found another that passed 216/216** — see §3.1. The number measures the suite,
> not the artifact.

# 1. Totals

| Layer | Checks |
|---|---:|
| Stage 4 full suite | 114 |
| Stage 4.1 regression layer | 102 |
| Stage 4.2B governance layer | 49 |
| Stage 4.2C screenshot-oracle layer | 38 |
| **Total** | **303** |
| Passing | 303 |
| Failing | 0 |
| Mutation-sensitivity fixtures | 18 detected / 18 injected |
| Historical replay artifacts | 3 committed decks |

# 2. What changed at Stage 4.2C

Before this stage, **every 1 August 2026 ruling was `TASK_TRANSCRIPT_ONLY`** — asserted in a task
message with no artifact behind it. Three of them now have a frozen `BARIAH_DIRECT_SCREENSHOT` oracle, and 30 gates are
named against it:

| Ruling | Was | Now |
|---|---|---|
| S01 title, duplicate removal, visual direction, Speaker Notes | `TASK_TRANSCRIPT_ONLY` | `BARIAH_DIRECT_SCREENSHOT` |
| Subtype visual policy (`Semua contoh ada visual…`) | `TASK_TRANSCRIPT_ONLY` | `BARIAH_DIRECT_SCREENSHOT` |
| Struktur Persisir Air component-main direction | `TASK_TRANSCRIPT_ONLY`, in conflict | `BARIAH_DIRECT_SCREENSHOT`, conflict closed |

The oracle module re-hashes each screenshot before returning any value, so these gates fail
closed if the evidence is edited or removed — they cannot pass against a stale transcription.

# 3. What the suite still does not establish

## 3.1 The defect this stage's gates did not catch

The per-example card visuals were derived from the **runtime state** rather than the **learner
screen**. A selection screen has three kinds of state — base, popup, all-viewed — and only the base
state classifies as `EXAMPLE_SELECTION_SCREEN`. The popup and all-viewed states of the same screen
rendered **without any card visuals at all**, and the suite reported 216/216 because every
visual gate was scoped to pages that classify as that subtype.

It was caught by looking at a rendered page, not by a predicate. `EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS`
now measures all 24 state pages of those 4 screens. The general lesson stands: **a gate scoped by
classification cannot see the pages its classification excludes.**

## 3.2 Transcription, not extraction

The three screenshots are raster images with no text layer. Their expected values were **read by
eye** from named pixel crops. That is a weaker link than the OOXML oracle, which parses the frozen
package. One limit is recorded in the oracle itself: a trailing full stop on two Speaker-Notes lines
is at the raster limit and is carried over from the unambiguous "before" block.

## 3.3 Model-only assertions remain model-only

`SHOT_S01_SPOKEN_BLOCKS_EXACT` reads the model's notes blocks and cannot see a package-level edit —
mutation R-012 proved it. It is backed by `SHOT_S01_PACKAGE_NOTES_EXACT`, which reads the generated
Notes XML and does fire. Where a gate is model-derived, a package-reading twin exists; where it does
not, treat the gate as evidence about the model only.

## 3.4 Not checked at all

- **Microsoft PowerPoint rendering.** LibreOffice in this container has no Impress import filter
  (`Error: source file could not be loaded`). Rendering uses the package parser with Liberation
  Sans metrics. `MICROSOFT_POWERPOINT_EQUIVALENCE` is **not** claimed and no smoke test has run.
- **Whether the content is pedagogically right.** Every check is structural or textual identity.
- **Eight component-main visual decisions.** `PENDING_HUMAN`, awaiting Bariah. Nothing in the suite
  can close them and `PENDING_HUMAN_ITEMS_CLOSED_BY_CC = 0`.
- **`B02-CAIR-INT-001`.** Still open; still blocks canonical freeze.

# 4. Evidence classes in force

| Class | Count of registry records | Meaning |
|---|---:|---|
| `BARIAH_DIRECT_SCREENSHOT` | 3 | frozen image, hash-verified on every run, values transcribed from named crops |
| `FROZEN_ARTIFACT_OOXML` | 1 | parsed out of the annotated v0.3 deck |
| `SOURCE_ATTESTED` | 26 rows / 14 assets | read from the frozen source matrix |
| `MODEL_DERIVED` | — | asserts the model, not the artifact; each has a package twin |
| `TASK_TRANSCRIPT_ONLY` | remaining 1 Aug rulings | no artifact behind it; still disclosed as such |
