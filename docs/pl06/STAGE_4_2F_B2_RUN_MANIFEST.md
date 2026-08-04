# Stage 4.2F-B2 — Lane B run manifest

**PL06 authority-harvest batch 1**

```
BATCH_ID   = PL06-HARVEST-BATCH-1
UNITS      = K5-PL06-T03-B03, K5-PL06-T03-B04, K5-PL06-T05-B01, K5-PL06-T06-B01
BRANCH     = claude/verify-powerpoint-file-vpfzkg
STAGE      = 4.2F-B2
SUITE_ID   = PL06_AUTHORITY_HARVEST_BATCH1_QA_v1
STATUS     = CAIR_PREFILLED_AWAITING_BARIAH_DECISIONS
```

No storyboard PPTX was generated for any Lane B unit. No MMD, React, SCORM or LMS artifact
was generated anywhere in this stage.

---

## 1. What this package can and cannot ask

The four units' **boundaries** are frozen, hash-verified and anchored to named DOCX headings.
Their **content** is not extracted. `PL06_OPEN_AUTHORITY_ITEMS_v1` records STOP-003
(visual inventory), STOP-004 (controlled content) and STOP-005 (quiz source) against all four,
and the module DOCX itself is held externally by identity — 16,832,861 bytes,
`5a9142cd…78df7` — and is not in this repository.

So every card is prefilled wherever the frozen evidence reaches, and records
`PENDING_EXTRACTION` wherever it does not. **No quiz stem, learning outcome or visual subject
is written for a unit whose text nobody has read.** A prefilled card that invented those
would be asking Bariah to approve CAIR's imagination, which is the thing this governance
chain exists to prevent.

The decision that unblocks the rest is **PL06-B1-D-25**, the extraction authorisation.

## 2. The four unit boundaries

| Unit | Topik | Module pages | Paragraphs | Named subtopics | Shared boundary | Boundary image |
| --- | --- | --- | ---: | ---: | --- | --- |
| K5-PL06-T03-B03 | 3 · Infrastruktur | 250–255 | 111 | 1 | **start + end** | p268 — identity only |
| K5-PL06-T03-B04 | 3 · Badan Air (Water Body) | 255–261 | 136 | 1 | **start** | none for pdf 273 |
| K5-PL06-T05-B01 | 5 · Pengurusan Kualiti Projek | 284–293 | 183 | 4 | clean | p302 — **ingested** |
| K5-PL06-T06-B01 | 6 · Perlindungan dan Penambahbaikan Alam Sekitar | 294–302 | 162 | 3 | clean | p312 — identity only |

Anchors, paragraph indices and shared-page flags all come from
`PL06_LESSON_BOUNDARY_MAP_v1.json`, verified against its pinned SHA-256
`aa02cd3c…6e31c073` before it is read. Paragraph spans are a controlled magnitude, not a row
count — extraction turns paragraphs into typed content records and that ratio is not fixed.

Only T05-B01's start page image is in this repository, and it was opened and read: module
page 284 carries `5.0 PENGURUSAN KUALITI PROJEK` at the top of the page with `5.1 Project
Quality Plan (PQP)` beneath it. One page image is boundary evidence, not an extraction, and
no content proposal is derived from it.

## 3. Screen-count arithmetic, exposed

No unit is given a screen count. Each is given a **floor** with its terms shown:

```
screens ≥ shell (2, +1 if the unit opens with a dialogue)
        + one content screen per NAMED subtopic
        + 3 closing (Rumusan, quiz, Tamat)
```

| Unit | Shell | Content floor | Closing | Minimum | Maximum |
| --- | ---: | ---: | ---: | ---: | --- |
| T03-B03 | 2 | 1 | 3 | **6** | UNKNOWN_PENDING_EXTRACTION |
| T03-B04 | 2 | 1 | 3 | **6** | UNKNOWN_PENDING_EXTRACTION |
| T05-B01 | 3 | 4 | 3 | **10** | UNKNOWN_PENDING_EXTRACTION |
| T06-B01 | 2 | 3 | 3 | **8** | UNKNOWN_PENDING_EXTRACTION |

T04's 22 screens are not carried over. Neither are its 65 runtime states: base states follow
the screen floor, triggered and total states are `UNKNOWN_PENDING_EXTRACTION` for all four,
because triggered states depend on how many records each screen reveals — which is what
extraction produces.

## 4. Rules applied without asking, and rules deliberately not

Six auto-applied course-wide rules: 4 MCQ + 1 Multiple Response; 60 percent threshold; no
learner-facing "dalam modul" / "mengikut modul" / "modul menyenaraikan"; Multiple Response as
checkboxes with no A/B/C labels; instructional clarity over production optimisation; the
five-item treatment vocabulary.

AR-01 and AR-02 are applied **and flagged**: RP-009 and RP-010 classify them GLOBAL on the
strength of a Style and Guidelines document that is itself the B02 slice, and both carry
`human_authority_required = VERIFY`. PL06-B1-D-28 asks rather than letting the flag disappear.

Seven no-reuse exceptions carried from T04 — NR-01 three-beat Rumusan, NR-02 Alya and Encik
Rahman, NR-03 the four-line dialogue pattern, NR-04 the screen count, NR-05 asset groups,
NR-06 visual totals, NR-07 the runtime-state page format. NR-07 is the one that changed
state: Lane A closed at `T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN`, so the two-panel
state-appendix **format** is released as a mechanism. The per-unit state **counts** are not.

No character name is proposed anywhere. STOP-006 is open, and T05-B01 — the only unit
proposing a dialogue — is the only one it immediately blocks.

## 5. Decisions requested

**29 decisions**, all bounded, all numbered `PL06-B1-D-01` … `PL06-B1-D-29`, each with an
answer field and a free-note field in section H and an evidence reference back to its card.

- 24 unit-level (6 each): boundary, grouping, dialogue, treatment, Rumusan beat count, quiz
  slot binding.
- 5 batch-level: extraction authorisation (D-25), the T03-B03 + T03-B04 merge (D-26), the
  cast binding (D-27), the 4+1 / 60 percent confirmation (D-28), the language policy (D-29).

Five decisions offer `GABUNG`, and every one of them requires a target ID
(`ID sasaran`) printed on the page — D-02, D-08, D-14, D-20, D-26.

D-27 is a **restatement** of the existing STOP-006 / SRC-ANOM-003, not a new register entry.
The package references the four blocking stop conditions; it does not re-mint them.

## 6. Traceability

41 rows. 8 carry the pinned boundary-map hash. **16 are recorded as
`BLOCKED_NOT_EXTRACTED`** — four per unit, one each for controlled rows, quiz stems, answer
keys and visual obligations. A claim that could point at nothing is recorded as blocked
rather than dropped, which is why a third of the table says NOT_EXTRACTED.

Visual obligations are `UNKNOWN`, deliberately not `0`: a unit with no extracted assets
cannot satisfy RP-104 and must not be given placeholder subjects to make a count.

Answer keys are `NOT_DRAFTED`, which is weaker than `PENDING_APPROVAL` — there is nothing to
approve.

## 7. Where a green suite hid a defect

**The shared-boundary flags were all reading False.** `PL06_LESSON_BOUNDARY_MAP_v1.json`
stores `shared_start` and `shared_end` as real JSON booleans; the CSV projection stores them
as the strings `"True"`/`"False"`. The model tested `lesson["shared_start"] == "True"`, which
against a boolean is silently always False. Every unit in the first build of this package
reported its boundary as **clean**, including T03-B03, which shares *both* its start and end
pages with neighbouring lessons.

That is the single most damaging thing this package could have got wrong: it would have told
Bariah that a boundary needing a heading-anchor split was safe to extract page-wise.

It was caught by `THE_TWO_SHARED_BOUNDARY_UNITS_ARE_NAMED`, which checks a literal list of
which two units share a boundary rather than asking the model whether it thinks any do. The
companion gate `SHARED_BOUNDARY_RISK_AGREES_WITH_THE_FROZEN_MAP` did **not** catch it —
it compared the map against itself using the same faulty test on both sides. It now reads the
raw JSON with `json.load` and plain Python truthiness, independent of the model's parser, and
`THE_FLAG_READER_HANDLES_BOTH_MAP_PROJECTIONS` pins the reader against both shapes.

**Four more self-referential oracles** were found by this lane's own fixtures and repaired:

| Fixture | The gate compared… | Now anchored on |
| --- | --- | --- |
| C-15 | `screen_arithmetic()` against itself, while the card's printed copy was corrupted | the arithmetic as carried on the card, plus a card-versus-live agreement gate |
| D-11 | the page against `B.GABUNG_TARGET_FIELD` — blanked to `""`, which is in every string | the literal `"ID sasaran"` |
| P-03 / P-04 | the exposure and exception lists against the document those same lists generated | literal ID sets `EX-01…EX-07` and `XU-01…XU-05` |
| D-22 | the page against `LANGUAGE_POLICY["statement_ms"]`, which the fixture had rewritten | literal Malay fragments |

**And one rendering defect**: the preview wrapper broke only on spaces, so
`T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN` was drawn straight through a table border and
the page read as clean when the layout was not. The wrapper now character-breaks an
over-long token the way Word breaks an unbreakable run. Fixed in the generator; the package
was regenerated, never hand-patched.

## 8. Artifacts

| Artifact | What it is |
| --- | --- |
| `docs/pl06/tools/pl06_batch1_data_v1.py` | the one controlled batch model |
| `docs/pl06/tools/pl06_docx_v1.py` | governed OOXML writer, mechanism only |
| `docs/pl06/tools/pl06_batch1_emit_v1.py` | one block list → DOCX + Markdown + traceability |
| `reviews/storyboard-bariah/pl06_harvest_batch1/PL06_Pakej_Keputusan_Bariah_Kelompok1_v1_0.docx` | the review DOCX, 29,360 bytes, 26 pages |
| `docs/pl06/PL06_HARVEST_BATCH1_PACKAGE_v1.md` | Markdown projection of the same block list |
| `docs/pl06/PL06_HARVEST_BATCH1_MODEL_v1.json` | the model, serialised |
| `docs/pl06/PL06_HARVEST_BATCH1_TRACEABILITY_v1.{json,md}` | source and authority traceability |
| `docs/pl06/PL06_HARVEST_BATCH1_DECISION_INDEX_v1.{json,md}` | the 29 decisions and where each is answered |
| `docs/pl06/PL06_HARVEST_BATCH1_QA_REPORT_v1.md` | QA report |
| `docs/pl06/PL06_HARVEST_BATCH1_MUTATION_REPORT_v1.md` | mutation report |
| `docs/pl06/harvest_batch1_preview/` | 26 deterministic page previews |

Sections A–H are all present: A batch overview, B reusable course-wide rules, C–F the four
decision cards, G cross-unit exceptions, H the consolidated decision sheet.

## 9. Suite

```
SUITE_ID = PL06_AUTHORITY_HARVEST_BATCH1_QA_v1
132/132 active gates PASS, 0 vacuous
```

Gate types: CARDS 24, DECISIONS 24, DOCX 23, RULES 20, BOUNDARY 11, ACCOUNTING 8, GUARD 8,
BATCH 7, TRACE 7.

**Mutations: 104 fixtures, 104 detected, 0 missed**, baseline 132/132 with no false failures,
`docx_rebuilt_clean = true` — the 18 rebuild fixtures corrupt the DOCX on disk and the real
package is restored byte-for-byte in text afterwards.

This total is never added to another suite's. The Lane A suite is
`T04_STATE_COVERAGE_QA_v1` (108) and its gates are its own.

## 10. Rendering

26 pages rendered as deterministic layout approximations at 96 DPI with Liberation Sans, and
every page was visually inspected as a contact sheet. LibreOffice in this environment has no
Writer filter, so **no native Microsoft Word render was performed and none is claimed**.

## 11. Not checked

- how the DOCX renders in Microsoft Word;
- whether the four units' content supports the proposed treatments — none of them is
  extracted, which is the whole reason this package exists;
- whether Bariah agrees with any CAIR proposal in it — that is what the package asks;
- whether the merge candidate T03-B03 + T03-B04 is instructionally sound;
- whether 4 MCQ + 1 MR and the 60 percent threshold are genuinely course-wide;
- whether an English rationale layer under a Malay decision surface is acceptable to the
  reviewer.

---

## Verdict

```
PL06_HARVEST_BATCH1_PREFILLED_AWAITING_BARIAH_DECISIONS
```

Four units carded, 29 bounded decisions requested, every one with somewhere to be answered.
Nothing in this package is approved, and nothing in it was invented to look complete.
