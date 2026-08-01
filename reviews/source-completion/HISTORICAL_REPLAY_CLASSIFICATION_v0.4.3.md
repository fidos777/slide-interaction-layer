# HISTORICAL_REPLAY_CLASSIFICATION — v0.4.3

> **A failure count is not a quality score.**
>
> Every earlier deck is run against **today's** gates, including gates written to enforce
> rulings that did not exist when it was built. A deck can be fully compliant with the
> authority in force on the day it was generated and still fail here. Reading these numbers
> as a ranking would reward the deck that happened to be built closest to the last ruling,
> not the deck that was most correct.

Suite: `generator/v0_4/b02_governance_qa_v0_4_3.py`, 307 gates.

---

# 1. Categories

| Category | Meaning |
|---|---|
| `TRUE_HISTORICAL_REGRESSION` | The deck violated the authoritative ruling **available at its own build time**. |
| `LATER_ORACLE_SUPERSESSION` | The deck was compliant with the then-current ruling; a later Bariah ruling made it obsolete. |
| `PREVIOUSLY_UNTESTED_SHAPE` | The defect came from an input shape not represented in the three-family proof. |
| `ARTIFACT_CONFORMANCE_FAILURE` | The model or decision was right; the generated artifact did not implement it. |
| `LATEST_EVIDENCE_NONCONFORMANCE` | The deck fails only against the current latest oracle — no ruling existed for it earlier. |

The categories are about **why** a gate fires, not how serious it is. A single deck usually
carries several, and one gate can only be classified against the deck it fired on.

---

# 2. `…v0_4.pptx` — 61 gates failing

**Oracle effective at build time:** the annotated v0.3 deck, the review guide, the S&G v0.3
and the correction exemplars. None of the 1 August WhatsApp rulings existed.

| Category | Gates | What they are |
|---|---:|---|
| `TRUE_HISTORICAL_REGRESSION` | 22 | The generic visual fallback (`PROMENADE_GENERIC_FALLBACK_GONE`, `GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES`, `FAMILY_S_GENERIC_VISUAL_FALLBACKS`, `VISUAL_DIRECTION_WRONG_SOURCE_BINDING`, `EXAMPLE_POPUPS_WITH_GENERIC_FALLBACK`…), technical metadata on the learner canvas, and the missing Notes italic runs. All three violated an exemplar Bariah had **already** supplied. |
| `ARTIFACT_CONFORMANCE_FAILURE` | 14 | `PERABOT_COMPONENT_NAMES_*`, `PERABOT_OVERVIEW_VISUAL_CARDS`, `TAMAT_*`, `ANSWER_KEY_SOURCE_MISMATCH`, `MCQ_ANSWER_KEYS_WITH_LETTER_AND_TEXT`. The decisions were recorded correctly; the generator did not render them. |
| `LATER_ORACLE_SUPERSESSION` | 13 | The whole `S01_*` family, `SHOT_S01_PACKAGE_NOTES_EXACT`, `SHOT_PERSISIR_*`, `SUPERSEDED_*`. v0.4 said "Pakej Latihan 06" and carried the orientation sentence because that is what the model then specified. Bariah changed it on 1 August. |
| `PREVIOUSLY_UNTESTED_SHAPE` | 8 | `EXAMPLE_POPUPS_WITHOUT_VISUAL`, `FAMILY_S_VISUAL_PANEL_MISSING`, `VISUAL_PANEL_HEADING_MISSING`, `REQUIRED_VISUAL_*`, `ACTION_INSTRUCTION_*`. The three-family proof covered one component per family; these shapes first appeared when all nine were propagated. |
| `LATEST_EVIDENCE_NONCONFORMANCE` | 4 | `EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED`, `EXAMPLE_SELECTION_*`, `MODAL_OCCLUDED_*`. Nothing required per-example card visuals until the 4:37 PM message. |

**Latest-oracle differences:** all three 1 August rulings post-date this deck. 17 of its 61
failures are unreachable by any decision available on the day it was built.

---

# 3. `…v0_4_1.pptx` — 16 gates failing

**Oracle effective at build time:** the above, plus the 1 August transcript rulings as
`TASK_TRANSCRIPT_ONLY`. No screenshot was frozen.

| Category | Gates | What they are |
|---|---:|---|
| `LATER_ORACLE_SUPERSESSION` | 9 | `S01_PL06_TITLE_*`, `S01_MULA_INSTRUCTION_*`, `S01_ORIENTATION_SENTENCE_REMOVED`, `SHOT_S01_PACKAGE_NOTES_EXACT`, `SPOKEN_BLOCKS_MISSING_FROM_NOTES`. The 4-block S01 transcript was correct under the model in force. |
| `LATEST_EVIDENCE_NONCONFORMANCE` | 5 | `EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED`, `EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS`, `MODAL_OCCLUDED_*`, `SHOT_PERSISIR_SUPERSESSION_DISCLOSED_IN_PANEL`, `SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL`. All follow from screenshots that did not exist. |
| `ARTIFACT_CONFORMANCE_FAILURE` | 2 | `S01_TOPIC_LINE_ON_CANVAS`, `S01_VISUAL_HEADING_ON_CANVAS`. **The one genuinely instructive pair.** Bariah's corrected S01 already showed the Topik body line and the `ARAHAN VISUAL — SPESIFIKASI SAHAJA` heading; the generator dropped both, and no gate looked until Stage 4.2C read the screenshot line by line. |
| `TRUE_HISTORICAL_REGRESSION` | 0 | — |
| `PREVIOUSLY_UNTESTED_SHAPE` | 0 | — |

**Fewer failures than v0.4.2 does not make v0.4.1 better.** It fails fewer gates mainly
because v0.4.2 was the deck that first asserted `EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL`
in the classified-population form that Stage 4.2C then widened.

---

# 4. `…v0_4_2.pptx` — 18 gates failing

**Oracle effective at build time:** the same as v0.4.1 plus the Stage 4.2B governance
hardening. Still no frozen screenshot.

| Category | Gates | What they are |
|---|---:|---|
| `LATER_ORACLE_SUPERSESSION` | 7 | The `S01_*` transcript family again. |
| `LATEST_EVIDENCE_NONCONFORMANCE` | 9 | `EXAMPLE_SELECTION_*`, `EXAMPLE_CARD_VISUALS_*`, `REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL`, `MODAL_OCCLUDED_*`, `SHOT_PERSISIR_SUPERSESSION_DISCLOSED_IN_PANEL`, `SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL`. v0.4.2 deliberately left the Contoh screens without visuals — that was the **correct** reading of the evidence it had, and it disclosed the Struktur Persisir conflict instead of resolving it. |
| `ARTIFACT_CONFORMANCE_FAILURE` | 2 | `S01_TOPIC_LINE_ON_CANVAS`, `S01_VISUAL_HEADING_ON_CANVAS`, carried forward from v0.4.1. |
| `TRUE_HISTORICAL_REGRESSION` | 0 | — |
| `PREVIOUSLY_UNTESTED_SHAPE` | 0 | — |

**v0.4.2 fails more gates than v0.4.1 and is the better deck.** 9 of its 18 failures are
things it got *right* under the evidence available — leaving a CONDITIONAL item unresolved
and a conflict disclosed rather than guessed. That is the clearest demonstration that the
count is not a ranking.

---

# 5. `…v0_4_3.pptx` — 0 gates failing

**Oracle effective at build time:** current, including the three frozen screenshots.

0 failures is a statement about *today's* gates, not about the deck's correctness. The
population audit run in the same stage found **13 gates whose population is narrower than
the obligation they test**, and a measured rendering inconsistency on 13 pages that no gate
currently sees. A deck at 0/307 can still carry defects the suite has no predicate for —
Stage 4.2C's own defect passed 216/216.

---

# 6. Summary — read the categories, not the totals

| Deck | Total | True regression | Later supersession | Untested shape | Artifact conformance | Latest-evidence |
|---|---:|---:|---:|---:|---:|---:|
| `…v0_4.pptx` | 61 | 22 | 13 | 8 | 14 | 4 |
| `…v0_4_1.pptx` | 16 | 0 | 9 | 0 | 2 | 5 |
| `…v0_4_2.pptx` | 18 | 0 | 7 | 0 | 2 | 9 |
| `…v0_4_3.pptx` | 0 | 0 | 0 | 0 | 0 | 0 |

**`TRUE_HISTORICAL_REGRESSION` is the only column that measures a build failing its own
standard**, and it reaches zero after v0.4. The rest measures how far the rulings have
moved since — which is a property of the review process, not of the artifact.
