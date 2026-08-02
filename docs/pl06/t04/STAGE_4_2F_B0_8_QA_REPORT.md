# STAGE_4_2F_B0_8_QA_REPORT

```
STAGE             = 4.2F-B0.8 — T04 CONTENT AND INSTANCE-MAPPING CLOSURE
SUITE_ID          = T04_CONTENT_QA_v1
SUITE             = docs/pl06/t04/tools/t04_content_qa_v1.py
FIXTURES          = docs/pl06/t04/tools/t04_content_mutations_v1.py
ACTIVE_GATE_COUNT = 138
RESULT            = 138/138 active gates PASS · 0 supersession markers · 138 emitted records
VACUOUS_GATES     = 0
FIXTURES          = 53/53 detected · 0 missed · 0 baseline false failures
SKIPPED_FIXTURES  = none in this suite
```

**A green suite measures the suite, not the artifact.** 138/138 means the gates I wrote agree
with the data I wrote. It does not mean the quiz questions are good questions or that the
dialogue reads well in Malay. The `NOT_CHECKED` list below is the honest boundary of the
claim.

# 1. Two harness rules are new, and both exist because of earlier defects

**Every gate declares the population it examined.** A gate that reports "0 bad records" over
0 records is vacuous. Two gates went vacuous unnoticed at Stage 4.2F-A2 when a population
emptied from under them, and nothing in the harness noticed. Every record in this suite now
carries `population`.

**A population of 0 fails unless the gate declares `empty_by_design` with a reason.** Silence
is not a licence. Two gates in this suite are legitimately declared empty:
`EMPTY_ASSET_GROUPS_ARE_DECLARED` and `EMPTY_BY_DESIGN_GATES_CARRY_A_REASON`. Fixture `V-52`
proves the rule fires when a population empties unexpectedly.

# 2. Gate accounting

| Gate type | Count |
|---|---:|
| `SOURCE_AUTHORITY` | 13 |
| `OBLIGATION_CLOSURE` | 15 |
| `ASSET_ACCOUNTING` | 12 |
| `SEQUENCE_INTEGRITY` | 18 |
| `DIALOGUE_DISCIPLINE` | 11 |
| `RUMUSAN_DISCIPLINE` | 9 |
| `ASSESSMENT_INTEGRITY` | 23 |
| `MMD_GUARD` | 6 |
| `PRODUCTION_GUARD` | 8 |
| `ARTIFACT_AGREEMENT` | 16 |
| `REPORTING` | 5 |
| `ACCOUNTING` | 2 |
| **TOTAL** | **138** |

# 3. Gate-ID diff against the prior suite

```
prior suite   T04_FINAL_RULINGS_QA_v1   (Stage 4.2F-B0.7)
this suite    T04_CONTENT_QA_v1         (Stage 4.2F-B0.8)

added          126
carried over    12
superseded      93
```

**Superseded is not deleted.** The 93 gate IDs absent from this suite are still enforced by
`t04_final_rulings_qa_v1`, which still runs and still governs the Stage 4.2F-B0.7 data. This
suite governs Stage 4.2F-B0.8 data only. Comparing raw totals across the two would be
meaningless, which is why every total in this report carries its `SUITE_ID`.

The 12 carried over are the cross-stage invariants: `NO_PPTX_GENERATED`,
`NO_PRODUCTION_GENERATOR_MODIFIED`, `MMD_PRODUCTION_NOT_STARTED`, `B02_FAMILIES_PROPAGATED`,
`WHATSAPP_DRAFT_NOT_SENT`, `VERDICT_IS_ALLOWED`, `DUPLICATE_GATE_IDS`,
`EVERY_GATE_CARRIES_A_TYPE`, `GIT_INDEX_READ`, `ALL_CONTROLLED_ARTIFACTS_PRESENT`,
`ASSET_JSON_MATCHES_DATA`, `FIT_ASSESSMENT_ROWS_IN_EXTRACT`.

# 4. Two gates failed on first run

## 4.1 `INSTANCE_MAPPING_COMPLETE_NOT_CLAIMED` — a false positive of mine

Fired on `READINESS["forbidden_term"] = "INSTANCE_MAPPING_COMPLETE"` — the field whose entire
job is to *declare the term forbidden*. A declaration of a prohibition read as the prohibited
claim.

This is now the fourth appearance of this exact category error in this workstream: Stage
4.2F-B0 (`EXTRACT_FREE_OF_B02_CONTENT` matched a verbatim source row), Stage 4.2F-B0.5
(`PASS_THRESHOLD_TREATED_AS_CONFIRMED` matched the pack's own withheld-items list), Stage
4.2F-B0.6 (`NO_VAGUE_SUBTOPIC_PHRASE` matched Bariah's own quoted words), and now this. The
pattern is always the same: a text scan cannot distinguish a claim from a disclaimer of that
claim. Fixed structurally — the declaring fields are excluded and
`FORBIDDEN_TERM_DECLARATION_INTACT` asserts the declaration still exists, so the exclusion
cannot become a hole.

## 4.2 `REVIEW_PACK_FREE_OF_TECHNICAL_VOCABULARY` — a real artifact defect

The human-facing Bariah review pack carried the generator banner, which contains a repository
path. The brief forbids repository paths in that pack, and it was right to: nothing in
`docs/pl06/t04/tools/...` means anything to the reviewer.

Fixed in the artifact, not the gate — the review pack no longer emits the banner. Its
provenance lives in the run manifest instead.

# 5. A fixture caught a defect the suite could not

`V-03` drops an obligation from the closure list entirely. **The suite did not notice.**

`VISUAL_OBLIGATIONS_TOTAL`, `VISUAL_OBLIGATIONS_CLOSED` and `ORPHAN_OBLIGATIONS` were reading
module-level constants computed once at import, not the live list. Delete a record and the
constants keep reporting the old numbers.

This is the *same* defect fixture `W-22` found in the Stage 4.2F-B0.7 suite one stage ago. I
fixed it there for the asset totals, wrote a dedicated `ASSET_TOTALS_DERIVED_LIVE` gate for
this suite — and then left the obligation totals reading cached constants in the very same
file. The lesson did not generalise on its own.

Fixed: all three now derive live from `OBLIGATION_CLOSURE`, plus a new
`CLOSURE_TOTALS_DERIVED_LIVE` gate that fails if the module constants and the live list ever
disagree. `FORECAST_TOTALS_DERIVED_LIVE` covers the same ground for the MMD numbers.

**Worth stating plainly: every precomputed total in a data module is a blind spot for any gate
that reads it instead of recomputing.** This suite now has three explicit live-derivation
gates for exactly that reason.

# 6. Mutation fixtures

53 fixtures, **53 detected, 0 missed, 0 baseline false failures**. All 24 mutations named in
the brief are covered; 29 more were added.

| Named in the brief | Fixture |
|---|---|
| remove one visual obligation mapping | `V-01` |
| create one orphan obligation | `V-02` |
| hand-type a non-resolving obligation ID | `V-04` |
| equate 46 obligations with 46 unique assets | `V-11` |
| change an asset-group total after cached calculation | `V-13` |
| omit one controlled source population from the screen sequence | `V-17` |
| mark proposed screen count as final | `V-19` |
| add a B02 family label | `V-20` |
| mark Alya and Encik Rahman final without Bariah approval | `V-24` |
| place a licensed-operator obligation in Encik Rahman dialogue | `V-26` |
| remove a dialogue source binding | `V-27` |
| add a fifth Rumusan point | `V-29` |
| remove a Rumusan source binding | `V-30` |
| mark Rumusan BARIAH_APPROVED | `V-31` |
| change quiz composition to five MCQ | `V-34` |
| change pass threshold to another value | `V-35` |
| scope the threshold to T04 only | `V-36` |
| remove correct-answer evidence | `V-37` |
| mark the answer key final | `V-39` |
| require external knowledge for a correct answer | `V-40` |
| mark MMD production started | `V-46` |
| convert preliminary MMD forecast into a production commitment | `V-47` |
| remove NOT_CHECKED | `V-51` |
| allow an unexpected empty gate population to pass | `V-52` |

Added beyond the brief: `V-03` obligation dropped · `V-05` closure reason removed · `V-06`
runtime state removed · `V-07` subject authority promoted · `V-08` population derivation
attributed to Bariah · `V-09` retired rule name restored · `V-10` Akta upgraded to legible ·
`V-12` bare asset number · `V-14` do-not-reuse counts collapsed · `V-15` asset count asserted
in prose · `V-16` empty group undeclared · `V-18` required population left screenless · `V-21`
B02 count inherited · `V-22` content screen unbound · `V-23` screen pre-reviewed · `V-25` fit
assessment relabelled · `V-28` Slide 2 escalated · `V-32` medium-risk flag removed · `V-33`
Rumusan pre-accepted · `V-38` evidence cites no row · `V-41` answer not among options · `V-42`
coverage point discarded · `V-43` merge disclosure removed · `V-44` option names the Act ·
`V-45` quiz marked approved · `V-48` production hours invented · `V-49` mapping claimed
complete · `V-50` storyboard build authorised · `V-53` suite identity lost.

Three fixtures (`V-51`, `V-53` and the harness half of `V-52`) patch the **QA module** rather
than the data module, because the defect they model lives in the reporting harness itself.

# 7. `NOT_CHECKED`

- whether any quiz item is a good question, or discriminates between learners
- whether the proposed correct answers are the answers Bariah would choose
- whether the Malay in the dialogue, Rumusan or quiz reads naturally
- whether Alya and Encik Rahman are the right characters for T04
- whether 21 screens is the right length for this unit
- whether the eight asset groups are the right groupings
- whether 41 proposed unique assets is achievable at any particular effort
- whether the D-04 reveal split is instructionally sound — Bariah ruled it, the gates enforce
  it, they do not judge it
- any rendered output — no PPTX exists for T04 and none was generated

# 8. Chain status, each with its own suite identity

| Suite ID | Stage | Gates | Fixtures |
|---|---|---|---|
| `T04_CONTENT_QA_v1` | 4.2F-B0.8 | **138 / 138** | **53 / 53 detected** |
| `T04_FINAL_RULINGS_QA_v1` | 4.2F-B0.7 | 105 / 105 | 32 / 32 detected |
| `T04_RULINGS_QA_v1` | 4.2F-B0.6 | 130 / 130 | 26 / 26 detected |
| `T04_PACK_QA_v1` | 4.2F-B0.5 | 107 / 107 | 39 / 39 detected |
| `T04_EXTRACTION_QA_v1` | 4.2F-B0 | 109 / 109 | 30 ran, 30 detected · **4 `SKIPPED_NO_DOCX`, not counted as passing** |
| `PL06_INVENTORY_QA_v1` | 4.2F-A2 | 140 / 140 | 54 / 54 detected |

The four skipped fixtures are `E-01`…`E-04`. They require the primary DOCX, deleted at the end
of Stage 4.2F-B0 by that stage's cleanup rule. **They are reported as skipped, never as
passed.**
