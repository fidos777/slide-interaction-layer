# QA_POPULATION_AUDIT — v0.4.3

Every gate the active suite emits, audited for **CLASSIFICATION_SCOPED_POPULATION** — the
weakness class defined in `QA_WEAKNESS_TAXONOMY_v0.4.3.md` §I.

Harness: `generator/audit/b02_population_audit_v0_4_3.py`. It does not read gate code alone.
It runs the suite under a return-trace, captures the real local variables each gate's
expression references, resolves them to concrete review-page IDs against the v0.4.3 deck and
model, and computes the excluded set. Per-gate detail is in `QA_POPULATION_AUDIT_v0.4.3.json`.

# 1. Required totals

| Metric | Value |
|---|---:|
| `GATES_EMITTED_BY_SUITE` | 307 |
| `GATES_RESOLVED_TO_SOURCE` | 307 |
| `GATES_UNBOUND_TO_SOURCE` | 0 |
| `DUPLICATE_GATE_IDS` | 0 |
| `SUPERSEDED_MARKERS` (inactive placeholders) | 16 |
| **`ACTIVE_GATES_AUDITED`** | **291** |
| **`CLASSIFICATION_SCOPED_GATES`** | **84** |
| **`GATES_WITH_SEMANTIC_POPULATION_GAPS`** | **13** |
| **`RECORDS_WRONGLY_EXCLUDED`** | **260** |
| **`GATES_REQUIRING_PINNED_POPULATION`** | **13** |
| **`GATES_WITH_COMPLETE_POPULATION`** | **134** |
| `GATES_WITHOUT_A_PAGE_POPULATION` (global/model assertions) | 144 |

## 1.1 On the expected count of 303

The stage brief expected 303 active gates. The suite emitted **307** after
the additive gates required by Part 4 (§4). Two corrections to that figure:

- **16 of them are `SUPERSEDED` markers**, not tests. They assert the constant
  string `SUPERSEDED` against itself so a reader sees that a ruling changed rather than finding a
  check quietly absent. Counting them as live checks overstates coverage, so the audited active
  population is **291**.
- 18 gate IDs are built by f-string inside loops (`SHAPES_BEYOND_{e}_EDGE`, `PACKAGE_TOKEN_{tok}`,
  `FORBIDDEN_TOKEN_{tok}`). A purely static pass misses them. Each emitted ID is bound back to its
  source template, so `GATES_UNBOUND_TO_SOURCE = 0`.
- `DUPLICATE_GATE_IDS = 0`. One duplicate existed before Stage 4.2C and was
  renamed then; the harness re-checks on every run because a duplicate ID silently collapses when
  results are indexed by gate.

# 2. Distribution

| Layer | Active gates |
|---|---:|
| `STAGE_4_FULL` | 109 |
| `STAGE_4_1_REGRESSION` | 99 |
| `STAGE_4_2B_GOVERNANCE` | 44 |
| `STAGE_4_2C_SCREENSHOT_ORACLE` | 39 |

| Obligation scope (the one authored field) | Gates |
|---|---:|
| `GLOBAL_OR_MODEL` | 141 |
| `SCREEN_LEVEL` | 73 |
| `PAGE_LEVEL` | 71 |
| `ITEM_LEVEL` | 6 |

| Classification field used to select a population | Gates |
|---|---:|
| `screen_role` | 34 |
| `execution_family` | 21 |
| `component_id` | 16 |
| `learner_screen_id` | 13 |
| `semantic_screen_subtype` | 13 |
| `visual_requirement` | 12 |
| `popup_subtype` | 9 |
| `visual_status` | 8 |
| `notes_policy` | 6 |
| `source_row_uid` | 5 |
| `runtime_state_id` | 5 |
| `next_control_type` | 3 |

`screen_role` leads the list, and it is worth separating: `rec_of[pid]["screen_role"]` is a
**screen** attribute, constant across a screen's states, and is safe. `st_of[pid]["screen_role"]`
is a **runtime state** attribute and is exactly the axis that produces this weakness. The audit
resolves the actual values, so the distinction is made on what the gate really selected, not on
the field name.

# 3. The gaps

**13 gates, 260 record-exclusions.**
They fall into three families with identical signatures.

## Family: selects 9 pages, obligation spans 22 — 13 excluded

| | |
|---|---|
| gates | `COMPONENT_MAINS_EVALUATED`, `COMPONENT_MAINS_PENDING_HUMAN`, `COMPONENT_MAINS_RESOLVED_BY_DIRECT_AUTHORITY`, `COMPONENT_MAIN_RESOLVED_WITHOUT_BARIAH_AUTHORITY`, `COMPONENT_MAIN_SCREENS_WITH_SPECIFIC_VISUAL` |
| excluded pages by runtime-state role | STATE_ALL_VIEWED × 5, STATE_POPUP × 8 |

## Family: selects 4 pages, obligation spans 24 — 20 excluded

| | |
|---|---|
| gates | `EXAMPLE_SELECTION_SCREENS_TOTAL`, `EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL`, `EXAMPLE_SELECTION_SCREENS_WITH_PER_EXAMPLE_VISUAL`, `EXAMPLE_SELECTION_SCREEN_LEVEL_INVENTED_DIRECTION` |
| excluded pages by runtime-state role | STATE_ALL_VIEWED × 4, STATE_POPUP × 16 |

## Family: selects 29 pages, obligation spans 63 — 34 excluded

| | |
|---|---|
| gates | `REQUIRED_VISUAL_PANEL_MISSING`, `REQUIRED_VISUAL_POPUPS_WITHOUT_VISUAL`, `REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL` |
| excluded pages by runtime-state role | STATE_ALL_VIEWED × 12, STATE_POPUP × 22 |

## Family: selects 10 pages, obligation spans 23 — 13 excluded

| | |
|---|---|
| gates | `COMPONENT_MAINS_MARKED_PROVISIONAL` |
| excluded pages by runtime-state role | STATE_ALL_VIEWED × 5, STATE_POPUP × 8 |

## 3.1 What the exclusions mean, measured rather than argued

An independent check walked every learner screen and asked whether a visual direction present on
its base page survives to its other states. It found the same 13 pages the population audit
flagged for the component-main family — two methods, one answer:

```
SCR_KERUSI_TAMAN_MAIN        COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST  1/1 non-base states lose it
SCR_TONG_SAMPAH_MAIN         COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST  1/1
SCR_DRINKING_FOUNTAIN_MAIN   COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST  1/1
SCR_PAPAN_TANDA_MAIN         COMPONENT_EXPLANATION_WITH_SPEC_LIST     5/5
SCR_BBQ_PIT_MAIN             COMPONENT_EXPLANATION_WITH_SPEC_LIST     5/5
                                                    total 13 pages
```

The four `COMPONENT_EXAMPLE_SELECTION` screens lose **nothing** — the Stage 4.2C parity fix holds
across all 24 of their state pages. The eight `EXAMPLE_DETAIL_FULL_SLIDE` screens lose nothing.

**This is a real rendering inconsistency and it is not being resolved here.** The direction that
disappears on those 13 pages belongs to a component-main screen whose visual is `CONDITIONAL /
PENDING_HUMAN` — a `PROVISIONAL_VISUAL_PROPOSAL` awaiting Bariah. Whether it *ought* to persist
behind a specification modal is downstream of a decision she has not made. So the population gap
is recorded as REAL and the obligation is recorded as UNCONFIRMED, and the fix is scheduled, not
performed. Regenerating the deck is outside this stage in any case.

## 3.2 One gap is already compensated

`EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL` and its three siblings still select 4 pages. They are
listed as gaps because their own population is incomplete — but
`EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS`, added at Stage 4.2C, measures all 24 and fires on
every fixture in §4 group 1. The audit reports the narrow population honestly rather than
crediting a sibling gate, because the day the sibling is edited the narrow ones go quiet again.
`EXAMPLE_SELECTION_SCREEN_LEVEL_INVENTED_DIRECTION` has **no** such compensation: an invented
screen-level direction on a popup or all-viewed state is currently unmeasured.

# 4. Additive gate created by this audit

Part 4 fixture **F-601** removed one answer from the `Semak Jawapan` review state and **nothing
fired**. Traced: the answer-key gates select shapes named `AnswerKeyBody`, which exist only on the
five `STATE_QUIZ_QUESTION` pages. `STATE_QUIZ_REVIEW` carries the same question-review obligation
under a different runtime classification and was in no gate's population at all.

Four gates were added to the Stage 4.2C layer, population pinned to the model's five questions
crossed with the review state rather than to any shape name or page class:

```
QUIZ_REVIEW_STATE_PAGES_EVALUATED            = 1
QUIZ_REVIEW_STATE_QUESTIONS_EXPECTED         = 5
QUIZ_REVIEW_STATE_QUESTIONS_MISSING          = 0
QUIZ_REVIEW_STATE_ANSWERS_MISSING_OR_WRONG   = 0
```

They read the generated package, pass on the unmodified v0.4.3 deck, and F-601 now fails
`QUIZ_REVIEW_STATE_ANSWERS_MISSING_OR_WRONG`. Expected values come from the controlled quiz
content — the same authority `ANSWER_KEY_SOURCE_MISMATCH` already uses — so they carry class E
`SHARED_DERIVATION` and that is disclosed rather than hidden. The deck was not touched.

# 5. Classification-scope fixtures

**11 / 11 detected, 0 missed, 0 false failures on the good deck.**

Every fixture mutates a record **outside** the classification-selected population of the gate that
owns the property and **inside** the true semantic population.

| ID | Group | Mutation | Detected by |
|---|---|---|---|
| `F-101` | EXAMPLE_SELECTION_STATE_PERSISTENCE | card visual removed from a POPUP state of a selection screen | `EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS` |
| `F-102` | EXAMPLE_SELECTION_STATE_PERSISTENCE | card visual removed from the ALL_VIEWED state of a selection screen | `EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS` |
| `F-103` | EXAMPLE_SELECTION_STATE_PERSISTENCE | card visual removed from the return/completion state of a second selection screen | `EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS` |
| `F-201` | FAMILY_S_COMPLETION_TICKS | false tick injected into an example POPUP state | `COMPLETION_TICKS_NOT_MATCHING_PATH` |
| `F-202` | FAMILY_S_COMPLETION_TICKS | extra tick injected into an ALL_VIEWED state where every item is already ticked | `COMPLETION_TICKS_NOT_MATCHING_PATH` |
| `F-203` | FAMILY_S_COMPLETION_TICKS | extra tick injected into the Struktur Taman group-master return state | `COMPLETION_TICKS_NOT_MATCHING_PATH` |
| `F-301` | NOTES_POLICY_POPULATION | spoken-looking Notes inserted into a SILENT_STATE_NOTES completion state | `SILENT_STATES_RECEIVING_NEW_VO`<br>`SILENT_STATES_WITH_NONEMPTY_NOTES` |
| `F-401` | INTERNAL_METADATA_DENYLIST | FAMILY_P1 injected into a DERIVED state page, not the base Perabot overview | `FAMILY_LABELS_ON_LEARNER_CANVAS`<br>`TECHNICAL_METADATA_ON_LEARNER_CANVAS` |
| `F-501` | VISUAL_SUBTYPE_PERSISTENCE | example-card visual removed from a popup-state rendering of a selection screen | `EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS`<br>`MODAL_OCCLUDED_SHAPES_EVALUATED` |
| `F-502` | VISUAL_SUBTYPE_PERSISTENCE | example-card visual removed from a state whose review_page_role differs from base | `EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS` |
| `F-601` | QUIZ_REVIEW_OVERLAY | one answer removed from the Semak Jawapan review state | `QUIZ_REVIEW_STATE_ANSWERS_MISSING_OR_WRONG` |

Two results worth naming:

- **F-202 / F-203** inject a *duplicate* tick onto completion states where every item is already
  ticked. `TICK_IDENTITY_MISMATCHES` maps a tick to a card by geometry, so a duplicate lands on an
  already-ticked card and is invisible to it. `COMPLETION_TICKS_NOT_MATCHING_PATH` counts, and
  catches both. The identity gate and the count gate are each blind where the other sees — that is
  why both are kept, and neither should be retired as redundant.
- **F-301** inserted a spoken-looking paragraph into a `SILENT_STATE_NOTES` completion state.
  `SILENT_STATES_WITH_NOTES_BLOCKS` is model-derived and could not see it; two package-reading
  gates did. The model-only gate is not removed, but it is not evidence about the artifact.

# 6. What this audit does not establish

- The `obligation_scope` of each gate is **authored**, not derived. Everything else — populations,
  exclusions, counts — is computed against the deck. A wrong scope judgement would mis-file a gate
  in either direction, and the fixtures in §5 are the check on that.
- A gate with a complete population can still be weak in the other eight ways. Population
  completeness is one axis, added at Stage 4.2D; the Stage 4.2A audit of classes A–H stands.
- 141 gates assert something global or model-level and have no page population. They are not
  "complete"; they are simply not the kind of gate this audit can measure.
