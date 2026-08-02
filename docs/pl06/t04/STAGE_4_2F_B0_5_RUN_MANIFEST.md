# STAGE_4_2F_B0_5_RUN_MANIFEST

```
STAGE   = 4.2F-B0.5 — T04 PRE-STORYBOARD DECISION PACK
SCOPE   = PROPOSALS, CONTRACTS AND REVIEW MATERIAL ONLY
PPTX_GENERATED    = 0
GENERATOR_TOUCHED = 0
APPROVED_ITEMS    = 0
VERDICT = T04_PRE_STORYBOARD_DECISION_PACK_READY_FOR_BARIAH
```

# 1. Pre-flight

| Check | Result |
|---|---|
| Repository / branch | `/home/user/slide-interaction-layer` · `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at start | `efa46b8794febd112ee4c418aad11c2630daa924` — matches |
| Working tree | clean |
| Stage 4.2F-B0 commit | present |
| T04 QA | **109/109** |
| PL06 QA | **140/140** |
| T04 source rows | **100** |
| Spacing elements | **40** |
| SmartArt assets | **1** |
| Raster images | **0** |
| Tables | **0** |
| Screen candidates | **6** |
| B02 families propagated | **0** |

## 1.1 Mutation status, reported separately

| Population | Result |
|---|---|
| **Pre-cleanup, Stage 4.2F-B0** | 34 / 34 detected — 30 data fixtures + 4 extraction fixtures with the DOCX present |
| **Clean-repository replay, this stage** | 30 source-independent fixtures ran, **30 detected, 0 missed** |
| | 4 DOCX-dependent fixtures **`SKIPPED_NO_DOCX`** — `E-01`, `E-02`, `E-03`, `E-04` |

**The four skipped fixtures are not reported as passed.** They require the primary DOCX,
which was deleted at the end of Stage 4.2F-B0 by that stage's own cleanup rule. Their result
is recorded from the run in which they executed; in a clean checkout they can only be
re-run by re-obtaining the source.

# 2. Role ownership, applied throughout

| Role | Owns |
|---|---|
| **CAIR / Claude Code** | source analysis · source-to-screen mapping · draft preparation · traceability · technical validation |
| **Bariah** | **sole Instructional Designer** · instructional author and approval authority · confirms screen treatment · approves or edits Rumusan · authors or approves quiz content · approves narration and interaction |
| **Firdaus** | project owner · delivery and scope authority · confirms operational decisions |

Every artifact in this pack is `CAIR_ASSISTED_DRAFT` / `PENDING_BARIAH_REVIEW`. The labels
`ID_AUTHORED`, `BARIAH_APPROVED` and `FINAL_INSTRUCTIONAL_CONTENT` appear nowhere, and five
gates plus five fixtures hold that.

# 3. Source-to-screen mapping

Six candidates, all six carried forward from Stage 4.2F-B0 with the same IDs. Every
non-`PENDING_HUMAN` screen binds to source rows that exist in the controlled extract.

| Candidate | Treatment | Status | Rows | Visual dep |
|---|---|---|---:|---|
| `T04-SC-01` | PROCESS_FLOW | `NEW_TREATMENT_REQUIRED` | 3 | T04-DGM-01 |
| `T04-SC-02` | CLICK_TO_REVEAL | `PROPOSED` | 5 | NONE |
| `T04-SC-03` | SEQUENTIAL_STEPS | `PROPOSED` | 11 | NONE |
| `T04-SC-04` | COMPARISON | `NEW_TREATMENT_REQUIRED` | 5 | NONE |
| `T04-SC-05` | CLICK_TO_REVEAL | `PROPOSED` | 6 | NONE |
| `T04-SC-06` | PENDING_HUMAN | `PENDING_BARIAH_REVIEW` | 0 | NONE |

**`FINAL_SCREEN_COUNT = NOT_CLAIMED`.** Six candidates are six treatments, not a sequence.
`T04-SC-04` may be dropped, `T04-SC-02` may become three screens, and `T04-SC-06` is two
screens or none depending on what Bariah authors. The count is also **not** derived from
B02 — B02's 29 learner screens describe a different unit.

# 4. Six candidate contracts

`T04-CT-01` … `T04-CT-06`, one per treatment, each carrying all sixteen required fields plus
an unfilled Bariah approval block.

**The reveal rule.** Both `CLICK_TO_REVEAL` contracts hide `SUPPLEMENTARY` content only —
definitions and examples expanding a label already on screen. All **eleven** legal, safety
and compliance rows sit on `T04-CT-04` and are **visible in the base state**: the Akta Racun
Makhluk Perosak 1974 citation, the licensed-operator requirement, PPE, locked storage, SDS
retention, spray conditions, notification and reporting. A learner who never interacts still
sees every one of them. Stepping on that contract adds pacing and gates nothing.

**`T04-CT-06` chooses nothing.** Three source-grounded options with trade-offs: B02-shaped
Rumusan + quiz; assessment sized to T04's coverage; or Rumusan only with assessment deferred
to Topik level, since Topik 4 has exactly one Bahagian.

# 5. SmartArt six-node contract

| | |
|---|---|
| Asset | `T04-DGM-01`, `f88edf2d305a546d…` |
| Part | `word/diagrams/data1.xml`, rIds dm=rId64 lo=rId65 qs=rId66 cs=rId67 |
| Source | modul ms 276, paragraph 5223, row `T04-ROW-003` |
| Dimensions | 6.79 × 3.92 in |
| Nodes | **6**, order preserved exactly |
| Flow | **`LINEAR_LEFT_TO_RIGHT`** — layout `process2`, algorithms `lin` + `conn` |
| Connectors | 6 `sibTrans` sibling transitions |
| Hierarchy | **NONE — flat.** All six are `parOf` the doc root; zero `parOf` links between text nodes |
| Caption | none in source |

The flat structure is load-bearing: nothing in the source subordinates one activity to
another, so a redraw must not introduce a tree, a cycle or a grouping.

Two treatments defined — source-bound reference for the review storyboard, controlled redraw
for MMD. **Asset production not started in either.**
`SMARTART_TREATMENT_STATUS = PENDING_BARIAH_REVIEW`.

# 6. Rumusan — CAIR-assisted draft

Five statements, one per structural block, every one bound to source rows that exist.

```
content_status          = CAIR_ASSISTED_DRAFT
instructional_authority = BARIAH
approval_status         = PENDING_BARIAH_REVIEW
```

**The module has no Rumusan** — zero hits across all 6,167 body paragraphs. This draft is a
compression of rows already extracted; it did not come from the module, and the provenance
field says so in those words.

One statement is flagged **`MEDIUM` factual risk**: `T04-RUM-03` states as a general rule the
contractor-responsibility pattern the source repeats three times but never generalises. It is
marked so Bariah can cut or narrow it rather than discovering it later.

Review table supplied with accept / edit / remove / comment.

# 7. Quiz — blueprint only

```
QUIZ_STRUCTURE = AUTHORITY_UNRESOLVED
QUIZ_CONTENT   = BLUEPRINT_ONLY
FINAL_AUTHOR   = BARIAH
```

Six coverage points, each with source rows, cognitive demand, the misconception it would
test, and the source evidence for a correct answer. **No stem, option, key, rationale or
feedback was written.**

Two structures offered: **A** 4 MCQ + 1 MR, **B** sized to T04's coverage. The tension is
stated rather than resolved — six blueprint points against a five-item quiz means Option A
requires cutting one, and the compliance cluster would carry the same weight as a recall item.

# 8. Five targeted decisions

| | Decision | Recommendation | Scope |
|---|---|---|---|
| `D-01` | Visual treatment | **TEXT_AND_DIAGRAM_LED** — no photographs needed | this unit |
| `D-02` | Quiz structure | confirm whether 4+1 and 60% are PL06-wide or B02-specific | **potentially PL06-wide** |
| `D-03` | Cast | **HILMI_NARRATOR_LED**, no additional characters | **this unit only** |
| `D-04` | Legislative content | obligations on base screen; supplementary may reveal | this unit |
| `D-05` | SmartArt | source-bound now, controlled redraw by MMD, order unchanged | this unit |

`D-03` is deliberately scoped to T04 alone. T04 is procedural content with no dialogue
scenario in the source, which makes it a poor place to settle a cast question for the whole
Pakej Latihan — and the ratified bank still conflicts with B02's pair.

# 9. Bariah message

Malay, WhatsApp-ready, no QA jargon. States that extraction is complete, that the five items
are not answered by the module, that the Rumusan is a draft only and the quiz is a blueprint
only, and asks for confirmation or amendment. **Not sent** — sending is Firdaus's call.

# 10. Portability template

Sixteen metrics, every value `NOT_MEASURED`, `SCORE = NOT_CALCULATED`, four score bands
recorded. Nothing is filled in — including the two metrics that already have honest values
from earlier stages, so the template cannot be mistaken for a result.

One prediction is written down **as a prediction**: visual-treatment reuse is likely to be
the lowest row, because T04 has one visual against B02's fourteen.

# 11. QA and mutations

| | |
|---|---:|
| Decision-pack gates | **107 / 107**, 0 markers |
| Decision-pack fixtures | **39 / 39 detected**, 0 missed, 0 false failures |
| T04 extraction gates | 109 / 109 |
| PL06 inventory gates | 140 / 140 |

One of my own gates fired on the pack's own prohibition list and was fixed at the gate — see
the QA report §2.1.

# 12. Constraints honoured

- **No PPTX generated.**
- No generator or validator under `reviews/source-completion/` modified — 0 changed files.
- No MMD, React or SCORM work.
- No final Rumusan, no final quiz question, no answer key.
- No decision marked approved — `APPROVED_ITEMS = 0`.
- CAIR is not named as instructional author anywhere.
- `efa46b8` not amended.
