# QA_SCOPE_AND_LIMITS — v0.4.3A

Supersedes the totals in `QA_SCOPE_AND_LIMITS_v0.4.3.md` after the Stage 4.2D population
audit. The deck is unchanged; only the suite and what is known about it have moved.

> **There is no single number here that means "approved".**
>
> The suite validates **known mechanical and evidence-backed obligations**. It does not
> establish that the courseware is correct, and the totals below are reported separately on
> purpose so that no one of them can be read as an overall verdict.

---

# 1. Totals, disaggregated

| Category | Count | What it means |
|---|---:|---|
| `MODEL` checks | 207 | assert the frozen model or the policy derived from it — **not the artifact** |
| `PACKAGE_XML` checks | 43 | read the generated `.pptx` back out and assert against its own bytes |
| `ORACLE_CONFORMANCE` checks | 38 | expected value comes from a module that imports nothing from the generator |
| `RENDERED_GEOMETRY` checks | 3 | measure position and extent in inches on the stage |
| `SUPERSEDED` markers | 16 | assert the constant `SUPERSEDED`; **not tests** — retained so a retired ruling is visible |
| **Total emitted** | **307** | |
| **Active (excluding markers)** | **291** | the number the population audit audited |
| Passing | 307 | |
| Failing | 0 | |

| Sensitivity and population | Count |
|---|---:|
| `MUTATION_SENSITIVITY` — replay fixtures | 18 detected / 18 injected |
| `MUTATION_SENSITIVITY` — classification-scope fixtures | 11 detected / 11 injected |
| `CLASSIFICATION_POPULATION` — gates with a pinned, state-independent population | 8 |
| Gates with a **complete** population for their obligation | 134 |
| Gates with a population **narrower** than their obligation | **13** |
| Records those 13 gates never look at | **260** |
| Gates with no page population (global or model-level assertions) | 144 |

| Human judgement | Count |
|---|---:|
| `PENDING_HUMAN` open decisions | 9 |
| ↳ awaiting Bariah | 6 |
| ↳ awaiting Firdaus / LMS owner | 1 |
| ↳ awaiting source authority | 2 |
| Resolved by CC in this stage | **0** |

## 1.1 The most important line in that table

**207 of 307 checks assert the model, not the artifact.** They are useful — the model is
where corrections are made — but a green `MODEL` check is evidence that the *plan* is right,
not that the *deck* implements it. Only 43 package-reading checks and 3 geometry checks look
at what was actually produced. Where a model gate matters, a package-reading twin exists
(`SHOT_S01_SPOKEN_BLOCKS_EXACT` → `SHOT_S01_PACKAGE_NOTES_EXACT`); where it does not, the
gate is evidence about the model only.

---

# 2. What the suite does establish

- The generated package is internally consistent with the frozen model.
- Source identity holds: 26 rows, 14 assets, 9 components, 0 created.
- Every one of the three frozen Bariah screenshots is byte-verified on every run, and 38
  gates are named against their transcribed values.
- No known regression shape is present: 29 injected defects across two harnesses all fire.
- The Semak Jawapan review state is now measured — it was in no gate's population until
  fixture F-601 exposed that at this stage.

---

# 3. What it does **not** prove

## 3.1 Stated as required

The QA suite **does not prove**:

- **complete instructional correctness** — no predicate reads for pedagogy;
- **complete visual suitability** — directions are text; no image is embedded or assessed;
- **Microsoft PowerPoint equivalence** — LibreOffice here has no Impress import filter
  (`Error: source file could not be loaded`); rendering uses the package parser with
  Liberation Sans metrics, and **no smoke test has run**;
- **actual LMS navigation** — the shell's behaviour at Tamat is unverified (OD-07);
- **final multimedia suitability** — nothing has been through MMD;
- **correctness of unresolved human judgments** — 9 open decisions, 0 closed by CC;
- **completeness of classifications not represented in the current mutation suite** — 29
  fixtures cover the shapes we have thought of, and that is all they cover.

## 3.2 Three specific, measured limits

**A population gap that is still open.** 13 gates select fewer records than their obligation
covers. Measured separately: **13 review pages lose the visual direction their screen's base
page carries** — the specification-popup and all-viewed states of five component mains. The
fix is planned (`QA_PINNED_POPULATION_PLAN_v0.4.3.json`) and **not applied**, because the
direction in question is a `PROVISIONAL_VISUAL_PROPOSAL` awaiting Bariah (OD-01). A gate
asserting persistence would be asserting an obligation nobody has confirmed.

**Transcription, not extraction.** The screenshots are raster with no text layer. A matching
SHA-256 proves the bytes are hers; it proves nothing about the reading. Two S01 trailing full
stops are `MEDIUM` punctuation confidence with `PUNCTUATION_CONFIRMATION = PENDING_BARIAH`
(OD-05).

**A pronunciation contract that exists only on paper.** `PL06` must be voiced *"PL enam"*,
never *"PL kosong enam"*. The generic course rule is present in the S01 production panel; the
PL06-specific spoken form is written **nowhere in the deck or model** —
`IMPLEMENTATION_REQUIRED_NEXT_STAGE`. It cannot go into the S01 Speaker Notes, which Bariah's
screenshot fixes at exactly three spoken blocks.

## 3.3 How the suite has been wrong before

| Stage | Suite said | What was actually wrong |
|---|---|---|
| 4.2A | 188/188 | no gate checked completion ticks at all |
| 4.2C | 216/216 | popup and all-viewed states rendered with no card visuals |
| 4.2D | 303/303 | the quiz review state was in no gate's population |

Each was found by looking — at a rendered page, or at a population — not by a predicate.
That is the reason this document exists and the reason no aggregate is published as a
verdict.

---

# 4. Evidence classes in force

| Class | Records | Meaning |
|---|---:|---|
| `BARIAH_DIRECT_SCREENSHOT` | 3 images / 10 transcribed rulings | frozen, hash-verified each run; values read by eye from named crops |
| `FROZEN_ARTIFACT_OOXML` | 1 | parsed out of the annotated v0.3 deck |
| `SOURCE_ATTESTED` | 26 rows / 14 assets | read from the frozen source matrix |
| `SOURCE_ATTESTED_COURSE_RULE` | 1 | the K5 PL pronunciation rule |
| `MODEL_DERIVED` | 207 gates | asserts the model; a package twin exists where it matters |
| `SHARED_DERIVATION` | quiz answer gates | expected value and artifact come from one controlled source; disclosed, not hidden |
| `TASK_TRANSCRIPT_ONLY` | remaining 1 Aug rulings | no artifact behind it |

---

# 5. Standing

`REVIEW_READY` · `NOT_FOR_MMD_BUILD` · `MULTIMEDIA_NOT_PRODUCED`

Not asserted: `PRODUCTION_APPROVED`, `CANONICAL_FREEZE`, `MMD_BUILD_READY`,
`SOURCE_INTEGRITY_FULLY_VERIFIED`, `MICROSOFT_POWERPOINT_EQUIVALENCE`.

Nothing in the open-decision inventory blocks the PowerPoint smoke test. Seven items block
the MMD build; all nine block canonical freeze and production.
