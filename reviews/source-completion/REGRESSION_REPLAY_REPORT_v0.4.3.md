# REGRESSION_REPLAY_REPORT — v0.4.3

Two harnesses. Every fixture is built in a temp directory from the committed deck and discarded; **no committed artifact is mutated**.

| Harness | Purpose |
|---|---|
| `generator/audit/b02_replay_v0_4_3.py` | 18 defect-shape fixtures + historical replay |
| `generator/audit/b02_classification_scope_fixtures_v0_4_3.py` | 11 fixtures that mutate records **outside** a gate's classified population but **inside** its semantic one |

A fixture proves GATE SENSITIVITY only. It does not prove the corrected value is right — that is the oracle's job.

# 1. Good artifact

| Metric | Value |
|---|---:|
| gates evaluated | 307 |
| passing | 307 |
| false failures | 0 |

# 2. Defect-shape fixtures

**18 / 18 detected, 0 missed.**

| ID | Injected defect | Designated gate(s) fired | Other gates newly failing |
|---|---|---|---:|
| `R-001` | Promenade direction replaced by the generic fallback | `GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES` | 5 |
| `R-002` | FAMILY_P1 injected into the learner canvas | `TECHNICAL_METADATA_ON_LEARNER_CANVAS` | 2 |
| `R-003` | italic property stripped from a Notes run | `NOTES_GLOSSARY_ITALIC_MISSES` | 2 |
| `R-004` | sixth card removed from a six-item grid | `CARDS_DROPPED_OR_INVENTED` | 1 |
| `R-005` | one quiz answer key removed | `QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY` | 5 |
| `R-006` | superseded Tamat close-window copy restored | `TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT` | 2 |
| `R-007` | confirmed screen-level Klik instruction removed from spoken VO | `ACTION_INSTRUCTIONS_MISSING_FROM_NOTES` | 4 |
| `R-008` | uncompleted sibling marked as ticked (Family S base page) | `COMPLETION_TICKS_NOT_MATCHING_PATH` | 2 |
| `R-008b` | uncompleted component marked as ticked (Struktur group master) | `COMPLETION_TICKS_NOT_MATCHING_PATH` | 1 |
| `R-009` | forced visual panel added to a specification popup | `SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL` | 2 |
| `R-010` | S01 duplicated standalone component title re-introduced | `S01_DUPLICATE_STANDALONE_COMPONENT_TITLE` | 4 |
| `R-011` | canvas object moved below the stage boundary | `CANVAS_SHAPES_OUTSIDE_STAGE` | 2 |
| `R-012` | removed S01 orientation sentence restored to the spoken VO | `SHOT_S01_PACKAGE_NOTES_EXACT`<br>`S01_ORIENTATION_SENTENCE_REMOVED` | 3 |
| `R-013` | S01 PL06 title reverted to the superseded long form | `SHOT_S01_PACKAGE_NOTES_EXACT`<br>`S01_PL06_TITLE_SPOKEN`<br>`S01_PL06_TITLE_LONG_FORM_WITHDRAWN` | 4 |
| `R-014` | S01 Mula instruction reverted to the superseded wording | `SHOT_S01_PACKAGE_NOTES_EXACT`<br>`S01_MULA_INSTRUCTION_SPOKEN`<br>`S01_MULA_INSTRUCTION_OLD_WORDING_WITHDRAWN` | 4 |
| `R-015` | an example card loses its per-example visual direction | `EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED` | 2 |
| `R-016` | an example card is given another example's visual direction | `EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED` | 2 |
| `R-017` | superseded Rajah 23 component-main direction restored as active | `SHOT_PERSISIR_ACTIVE_DIRECTION_RENDERED`<br>`SHOT_PERSISIR_SUPERSEDED_DIRECTION_NOT_ON_CANVAS`<br>`SUPERSEDED_DIRECTION_RENDERED_AS_ACTIVE` | 3 |

# 3. Classification-scope fixtures *(new at Stage 4.2D)*

**11 / 11 detected, 0 missed, 0 false failures.**

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

`F-601` was **missed on first run** — the Semak Jawapan review state was in no gate's population. Four `QUIZ_REVIEW_STATE_*` gates with a pinned population were added, the deck was not touched, and it is now caught by `QUIZ_REVIEW_STATE_ANSWERS_MISSING_OR_WRONG`.

# 4. Historical replay

Earlier committed decks against the v0.4.3 suite. **These counts are not a quality ranking** — see `HISTORICAL_REPLAY_CLASSIFICATION_v0.4.3.md`, which sorts every failure into `TRUE_HISTORICAL_REGRESSION`, `LATER_ORACLE_SUPERSESSION`, `PREVIOUSLY_UNTESTED_SHAPE`, `ARTIFACT_CONFORMANCE_FAILURE` or `LATEST_EVIDENCE_NONCONFORMANCE`.

| Deck | Gates failing | True regression against its own oracle |
|---|---:|---:|
| `…v0_4.pptx` | 61 | 22 |
| `…v0_4_1.pptx` | 16 | 0 |
| `…v0_4_2.pptx` | 18 | 0 |
| `…v0_4_3.pptx` | 0 | 0 |

v0.4.2 fails more gates than v0.4.1 **and is the better deck**: 9 of its 18 failures are things it got right under the evidence it had — leaving a CONDITIONAL item unresolved and disclosing a conflict rather than guessing.
