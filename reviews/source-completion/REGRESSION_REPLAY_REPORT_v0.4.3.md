# REGRESSION_REPLAY_REPORT — v0.4.3

Harness: `generator/audit/b02_replay_v0_4_3.py`. Every fixture is built in a temp directory from the committed deck and discarded; **no committed artifact is mutated**.

A fixture proves GATE SENSITIVITY only. It does not prove the corrected value is right — that is the oracle's job.

# 1. Good artifact

| Metric | Value |
|---|---:|
| gates evaluated | 303 |
| passing | 303 |
| false failures | 0 |

# 2. Mutation sensitivity

**18 / 18 detected, 0 missed.** R-001…R-011 are the Stage 4.2B fixtures, rebuilt from the v0.4.3 deck. R-012…R-017 are new at Stage 4.2C and each attacks one thing the latest screenshots settled.

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

# 3. Historical replay

Earlier committed decks, run against the v0.4.3 suite. These are real artifacts, not fixtures: the counts show what the current gates would have caught.

| Deck | Gates failing |
|---|---:|
| `…v0_4.pptx` | 61 |
| `…v0_4_1.pptx` | 16 |
| `…v0_4_2.pptx` | 18 |

The 18 gates the immediately preceding deck fails are exactly the Stage 4.2C rulings:

```
EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED
EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL
EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS
MODAL_OCCLUDED_SHAPES_EVALUATED
MODAL_OCCLUDED_SHAPE_NAMES
REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL
S01_MULA_INSTRUCTION_OLD_WORDING_WITHDRAWN
S01_MULA_INSTRUCTION_SPOKEN
S01_ORIENTATION_SENTENCE_REMOVED
S01_PL06_TITLE_LONG_FORM_WITHDRAWN
S01_PL06_TITLE_SPOKEN
S01_TOPIC_LINE_ON_CANVAS
S01_VISUAL_HEADING_ON_CANVAS
SHOT_PERSISIR_SUPERSESSION_DISCLOSED_IN_PANEL
SHOT_S01_PACKAGE_NOTES_EXACT
SHOT_S01_VISUAL_HEADING_MATCHES
SPOKEN_BLOCKS_MISSING_FROM_NOTES
SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL
```
