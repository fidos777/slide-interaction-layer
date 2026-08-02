# QA_SCOPE_AND_LIMITS — v0.4.4

> **No single number here means "approved".** The three counts below are reported separately
> on purpose, and supersession markers are not tests.

# 1. Test accounting

| Metric | Value |
|---|---:|
| `ACTIVE_TEST_GATES_PASSING` | **367 / 367** |
| `SUPERSESSION_MARKERS_PRESENT` | **19** |
| `TOTAL_EMITTED_GATE_RECORDS` | **386** |

A supersession marker asserts the constant `SUPERSEDED` against itself. It exists so a
retired ruling stays visible rather than vanishing from the suite. Nineteen of them are not
nineteen passing checks.

# 2. Layered totals

| Layer | Checks | What it reads |
|---|---:|---|
| `MODEL` | 251 | the frozen model and the policy derived from it — **not the artifact** |
| `PACKAGE_XML` | 78 | the generated `.pptx` read back out of its own bytes |
| `ORACLE_CONFORMANCE` | 49 | expected values from modules that import nothing from the generator and re-hash their evidence |
| `RENDERED_GEOMETRY` | 8 | positions and extents in inches on the stage |
| `CLASSIFICATION_POPULATION` | 12 | populations pinned to `learner_screen_id`, not to review-page class |
| `MUTATION_SENSITIVITY` | 39 fixtures | 39 detected, 0 missed, 0 false failures |
| `SUPERSESSION` markers | 19 | not tests |
| `PENDING_SOURCE_AUTHORITY` | 3 | MS2680, `B02-CAIR-INT-001`, OD-10 / L-01 |
| `NOT_CHECKED` | see §4 | |

Layer counts are approximate attributions of gates that often read more than one surface;
the exact per-obligation position is in `OBLIGATION_COVERAGE_MATRIX_v0.4.4.json`, which
records, per obligation, whether it is checked at model, package, rendered page, independent
oracle and negative mutation. **`MODEL_ONLY_ROWS = 0`** — every release-critical obligation
is checked in the generated package, not only in the plan.

# 3. What this build does establish

- All nine component-main overviews render their frozen source-bound subjects, in the
  cardinalities Bariah ruled: 5, 5, 3, 3, 3, **2**, 3, 2, **1**.
- The overview persists across all 22 component-main runtime states, compared by **subject
  identity**, not by shape count.
- Specification popups remain text-led; example popups carry a focused panel measurably wider
  than any overview card (4.14 in vs 2.60 in).
- Every final Bariah and LMS decision frozen at Stage 4.2E-A is implemented and gated.
- 39 injected defects all fire, including six that attack the two new cardinality rulings
  directly.
- 100 pages rendered and visually inspected: 0 text overflow, 0 shapes outside the stage,
  0 unintended non-modal overlaps.

# 4. What it does **not** prove

- **Microsoft PowerPoint equivalence.** LibreOffice here has no Impress import filter
  (`Error: source file could not be loaded`). Rendering uses the package parser with
  Liberation Sans metrics. **No smoke test has run** — that is the next stage, and this deck
  is its candidate.
- **Instructional correctness.** Nothing checks whether the teaching is right.
- **Visual suitability.** Directions are text. No image is embedded or assessed.
- **Actual LMS navigation.** The Tamat mechanism is recorded as LMS-owner metadata with
  `automatic_next_route` and `LMS_shell_next` both marked NOT PROVEN.
- **Final multimedia suitability.** Nothing has been through MMD.
- **Completeness of classifications outside the fixture set.** 39 fixtures cover the shapes
  we have thought of, and that is all they cover.

## 4.1 Three limits found in this stage's own gates

Recorded because they are the pattern most likely to recur:

- **`C-12` and `C-16` were missed on first run.** Both gates read the model's notes blocks,
  so a package-level Notes edit was invisible — `MODEL_ONLY_ASSERTION`. Package-reading twins
  were added and both fixtures now fire.
- **A two-line component direction ran into the overview heading on two screens** and no
  geometry gate saw it: the render check measures overflow *inside* a box, not collision
  *between* two boxes it considers legal. Found by looking at a rendered page. Fixed at
  source and pinned by `COMPONENT_VISUAL_OVERLAPS_OVERVIEW_HEADING`.
- **Transcription, not extraction.** All five frozen decision screenshots are raster images
  with no text layer. A matching SHA-256 proves the bytes are hers; it proves nothing about
  the reading. Every transcribed value names the crop it came from.

# 5. Historical replay is not a ranking

| Deck | Gates failing |
|---|---:|
| `…v0_4.pptx` | 91 |
| `…v0_4_1.pptx` | 41 |
| `…v0_4_2.pptx` | 42 |
| `…v0_4_3.pptx` | 25 |
| `…v0_4_4.pptx` | **0** |

v0.4.3 was READY under its own oracle and is not defective. Its 25 failures are
`LATEST_EVIDENCE_NONCONFORMANCE` — decisions frozen after it was built. See
`REGRESSION_REPLAY_REPORT_v0.4.4.md`.

# 6. Standing

`REVIEW_CANDIDATE` · `FINAL_BARIAH_DECISIONS_IMPLEMENTED` · `INSTANCE_MAPPING_COMPLETE` ·
`READY_FOR_MICROSOFT_POWERPOINT_SMOKE` · `NOT_FOR_MMD_BUILD` · `NOT_CANONICALLY_FROZEN` ·
`MULTIMEDIA_NOT_PRODUCED`

Not asserted: `PRODUCTION_APPROVED`, `CANONICAL_FREEZE`, `MMD_BUILD_READY`,
`SOURCE_INTEGRITY_FULLY_VERIFIED`, `MICROSOFT_POWERPOINT_EQUIVALENCE`,
**`SOURCE_GOVERNANCE_COMPLETE`**.
