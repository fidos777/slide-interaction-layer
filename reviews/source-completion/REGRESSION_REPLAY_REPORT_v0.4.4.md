# REGRESSION_REPLAY_REPORT — v0.4.4

Harness `generator/audit/b02_replay_v0_4_4.py`. Every fixture is built in a temp directory from the committed deck and discarded; **no committed artifact is mutated**.

| Metric | Value |
|---|---:|
| gates evaluated on the good deck | 386 |
| `CORRECTED_V0_4_4_FALSE_FAILURES` | 0 |
| `MUTATION_FIXTURES_DETECTED` | 39 / 39 |
| `MUTATION_FIXTURES_MISSED` | 0 |

# 1. Fixtures

R-001…R-017 are the inherited defect-shape fixtures, rebased onto v0.4.4. C-01…C-21 are new at this stage and target the rulings it implements.

| ID | Injected defect | Designated gate(s) fired | Other gates newly failing |
|---|---|---|---:|
| `R-001` | Promenade direction replaced by the generic fallback | `GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES` | 5 |
| `R-002` | FAMILY_P1 injected into the learner canvas | `TECHNICAL_METADATA_ON_LEARNER_CANVAS` | 2 |
| `R-003` | italic property stripped from a Notes run | `NOTES_GLOSSARY_ITALIC_MISSES` | 2 |
| `R-004` | sixth card removed from a six-item grid | `CARDS_DROPPED_OR_INVENTED` | 1 |
| `R-005` | one quiz answer key removed | `QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY` | 5 |
| `R-006` | superseded Tamat close-window copy restored | `TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT` | 4 |
| `R-007` | confirmed screen-level Klik instruction removed from spoken VO | `ACTION_INSTRUCTIONS_MISSING_FROM_NOTES` | 4 |
| `R-008` | uncompleted sibling marked as ticked (Family S base page) | `COMPLETION_TICKS_NOT_MATCHING_PATH` | 2 |
| `R-008b` | uncompleted component marked as ticked (Struktur group master) | `COMPLETION_TICKS_NOT_MATCHING_PATH` | 1 |
| `R-009` | forced visual panel added to a specification popup | `SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL` | 3 |
| `R-010` | S01 duplicated standalone component title re-introduced | `S01_DUPLICATE_STANDALONE_COMPONENT_TITLE` | 4 |
| `R-011` | canvas object moved below the stage boundary | `CANVAS_SHAPES_OUTSIDE_STAGE` | 2 |
| `R-012` | removed S01 orientation sentence restored to the spoken VO | `SHOT_S01_PACKAGE_NOTES_EXACT`<br>`S01_ORIENTATION_SENTENCE_REMOVED` | 5 |
| `R-013` | S01 PL06 title reverted to the superseded long form | `SHOT_S01_PACKAGE_NOTES_EXACT`<br>`S01_PL06_TITLE_SPOKEN`<br>`S01_PL06_TITLE_LONG_FORM_WITHDRAWN` | 6 |
| `R-014` | S01 Mula instruction reverted to the superseded wording | `SHOT_S01_PACKAGE_NOTES_EXACT`<br>`S01_MULA_INSTRUCTION_SPOKEN`<br>`S01_MULA_INSTRUCTION_OLD_WORDING_WITHDRAWN` | 5 |
| `R-015` | an example card loses its per-example visual direction | `EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED` | 2 |
| `R-016` | an example card is given another example's visual direction | `EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED` | 2 |
| `R-017` | superseded Rajah 23 component-main direction restored as active | `SHOT_PERSISIR_ACTIVE_DIRECTION_RENDERED`<br>`SHOT_PERSISIR_SUPERSEDED_DIRECTION_NOT_ON_CANVAS`<br>`SUPERSEDED_DIRECTION_RENDERED_AS_ACTIVE` | 3 |
| `C-01` | Papan Tanda overview reduced from two subjects to one | `PAPAN_TANDA_OVERVIEW_VISUAL_COUNT`<br>`OVERVIEW_CARDINALITY_MAPPING_MISMATCHES` | 9 |
| `C-02` | a Papan Tanda subject replaced with an invented subject | `PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT`<br>`UNAUTHORISED_OVERVIEW_SUBJECTS` | 6 |
| `C-03` | a Papan Tanda subject replaced with a cross-component subject | `PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT`<br>`UNAUTHORISED_OVERVIEW_SUBJECTS` | 6 |
| `C-04` | BBQ Pit given a duplicated second visual | `BBQ_PIT_OVERVIEW_VISUAL_COUNT` | 8 |
| `C-05` | BBQ Pit given an invented second subject | `BBQ_PIT_OVERVIEW_VISUAL_COUNT`<br>`OVERVIEW_COUNTS_BY_COMPONENT` | 9 |
| `C-06` | the sole BBQ Pit overview visual removed | `BBQ_PIT_OVERVIEW_VISUAL_COUNT`<br>`COMPONENT_MAIN_OVERVIEWS_RENDERED` | 10 |
| `C-07` | Papan Tanda subject bindings swapped onto unrelated figures, count preserved | `PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT`<br>`UNAUTHORISED_OVERVIEW_SUBJECTS` | 6 |
| `C-08` | overview removed from an all-viewed state | `BASE_TO_ALL_VIEWED_OVERVIEW_IDENTITY_MISMATCHES`<br>`PERSISTENCE_TARGET_PAGES_MISSING_VISUALS` | 2 |
| `C-09` | overview removed from a specification-popup state outside base classification | `BASE_TO_RETURN_OVERVIEW_IDENTITY_MISMATCHES`<br>`PERSISTENCE_TARGET_PAGES_MISSING_VISUALS` | 2 |
| `C-10` | a Slide 5 bullet changed | `SLIDE5_BULLET_2_EXACT` | 1 |
| `C-11` | trailing full stops added to the Slide 5 bullets | `SLIDE5_BULLET_TRAILING_PERIODS` | 1 |
| `C-12` | Slide 5 content removed from the spoken VO | `SLIDE5_VO_IN_PACKAGE_NOTES` | 2 |
| `C-13` | the two S01 trailing periods restored | `S01_LINE_1_TRAILING_PERIOD`<br>`SHOT_S01_PACKAGE_NOTES_EXACT` | 5 |
| `C-14` | detailed rationale inserted into Speaker Notes | `QUIZ_RATIONALE_IN_SPEAKER_NOTES` | 2 |
| `C-15` | a quiz feedback string changed | `QUIZ_CORRECT_FEEDBACK_EXACT_MATCH` | 2 |
| `C-16` | a micro-control instruction added to spoken VO | `MICRO_CONTROL_INSTRUCTIONS_IN_PACKAGE_NOTES` | 1 |
| `C-17` | a confirmed screen-level Klik instruction removed from VO | `ACTION_INSTRUCTIONS_MISSING_FROM_NOTES` | 4 |
| `C-18` | Alya inserted into an unrelated screen | `CAST_NAMES_ON_UNRELATED_SCREENS` | 3 |
| `C-19` | automatic Tamat navigation claimed | `TAMAT_MECHANISM_ON_LEARNER_CANVAS` | 3 |
| `C-20` | spoken_as PL enam activated | `UNRATIFIED_PL06_PRONUNCIATION_IMPLEMENTED` | 5 |
| `C-21` | a specification popup given a visual panel | `SPECIFICATION_POPUPS_WITH_FORCED_VISUAL_PANEL`<br>`SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL` | 3 |

## 1.1 Two fixtures found gates of mine that were model-only

`C-12` (Slide 5 content removed from the VO) and `C-16` (a micro-control instruction added to the VO) were **missed on first run**. Both gates read the model's notes blocks, so a package-level Notes edit was invisible to them — the `MODEL_ONLY_ASSERTION` weakness. `SLIDE5_VO_IN_PACKAGE_NOTES` and `MICRO_CONTROL_INSTRUCTIONS_IN_PACKAGE_NOTES` now read the generated Notes parts, and both fixtures fire.

# 2. Historical replay

Every committed deck against the **current** suite. **These counts are not a quality ranking** — a deck compliant with the authority in force on its build day still fails gates written for rulings that did not yet exist.

| Deck | Gates failing | Dominant category |
|---|---:|---|
| `…v0_4.pptx` | 91 | `TRUE_HISTORICAL_REGRESSION` + `PREVIOUSLY_UNTESTED_SHAPE` |
| `…v0_4_1.pptx` | 41 | `LATER_ORACLE_SUPERSESSION` + `LATEST_EVIDENCE_NONCONFORMANCE` |
| `…v0_4_2.pptx` | 42 | `LATEST_EVIDENCE_NONCONFORMANCE` |
| `…v0_4_3.pptx` | 25 | `LATEST_EVIDENCE_NONCONFORMANCE` — every one is a decision frozen at 4.2E-A and implemented only now |
| `…v0_4_4.pptx` | 0 | — |

`V0_4_4_ACTIVE_GATE_FAILURES = 0`.

## 2.1 Why v0.4.3 fails 25 gates

v0.4.3 was the artifact this project called READY at Stage 4.2C, and it is not defective against its own oracle. It fails here because the final Bariah decisions — component-main overviews, the two Papan Tanda figures, the single BBQ Pit visual, state persistence, the Slide 5 block, the S01 punctuation, the Tamat metadata — were frozen after it was built. That is `LATEST_EVIDENCE_NONCONFORMANCE`, and it is the direct measure of what this stage implemented.

```
BBQ_PIT_OVERVIEW_SUBJECT_NOT_DUPLICATED
BBQ_PIT_OVERVIEW_VISUAL_COUNT
COMPONENT_MAIN_OVERVIEWS_RENDERED
INVENTED_OVERVIEW_SUBJECTS
OVERVIEW_CARDINALITY_MAPPING_MISMATCHES
OVERVIEW_COUNTS_BY_COMPONENT
PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT
PAPAN_TANDA_OVERVIEW_VISUAL_COUNT
S01_LINE_1_EXACT
S01_LINE_1_TRAILING_PERIOD
S01_LINE_2_EXACT
S01_LINE_2_TRAILING_PERIOD
S01_PL06_TITLE_SPOKEN_WITH_TRAILING_PERIOD
SHOT_S01_PACKAGE_NOTES_EXACT
SLIDE5_ASAS_PEMBINAAN_HEADING_EXACT
SLIDE5_BULLETS_IN_PACKAGE_NOTES
SLIDE5_BULLET_1_EXACT
SLIDE5_BULLET_2_EXACT
SLIDE5_VO_IN_PACKAGE_NOTES
SPOKEN_BLOCKS_MISSING_FROM_NOTES
TAMAT_AUTOMATIC_ROUTE_CLAIM
TAMAT_LEARNER_ACTION_RECORDED
TAMAT_LMS_SHELL_NEXT_CLAIM
TAMAT_NAVIGATION_OUTCOME_RECORDED
UNAUTHORISED_OVERVIEW_SUBJECTS
```
