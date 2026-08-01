# REGRESSION_REPLAY_REPORT — v0.4.2

```
HISTORICAL_BAD_ARTIFACT_REPLAYS    = 1   (the superseded v0.4 deck, 40 gates fail)
MUTATION_SENSITIVITY_TESTS         = 12
BAD_FIXTURES_DETECTED              = 12
BAD_FIXTURES_NOT_DETECTED          = 0
CORRECTED_ARTIFACT_FALSE_FAILURES  = 0
```

A mutation fixture proves **gate sensitivity only**. It does not prove the corrected value is
right — that is the oracle's job, and where no frozen oracle exists the registry says so. All
fixtures are built in a temp directory; no committed deck was modified.

---

# 1. Historical bad-artifact replay

The **superseded v0.4 deck** is a genuine known-bad artifact, still in the repository. Replayed
against the current suite it fails **40** gates, including:

- `ACTION_INSTRUCTIONS_MISSING_FROM_NOTES`
- `ACTION_INSTRUCTIONS_PRESENT_IN_SPOKEN_TRANSCRIPT`
- `ACTION_INSTRUCTIONS_PRESENT_ON_CANVAS`
- `ACTION_INSTRUCTION_CANVAS_VO_MISMATCHES`
- `ANSWER_KEY_SOURCE_MISMATCH`
- `CANVAS_GLOSSARY_ITALIC_MISSES`
- `EXAMPLE_POPUPS_WITHOUT_VISUAL`
- `EXAMPLE_POPUPS_WITH_GENERIC_FALLBACK`
- `EXAMPLE_POPUPS_WITH_SPECIFIC_VISUAL`
- `EXAMPLE_SCREENS_WITHOUT_VISUAL`
- `EXAMPLE_SCREENS_WITH_SPECIFIC_VISUAL`
- `FAMILY_LABELS_ON_LEARNER_CANVAS`
- `FAMILY_S_GENERIC_VISUAL_FALLBACKS`
- `FAMILY_S_POPUPS_WITH_SPECIFIC_VISUAL_DIRECTION`

This is artifact-backed, not synthetic. It is however a *single* pre-fix deck: it does not contain
every historical defect, because several were fixed inside Stage 4 before that deck was written.
Those defects have no committed bad artifact and are covered by mutation only — which is why each
registry record names its evidence class rather than implying uniform artifact backing.

---

# 2. Mutation sensitivity

| ID | Fixture | Designated gate | Bad fixture | Corrected v0.4.1 | Backing |
|---|---|---|---|---|---|
| `R-001` | Promenade direction replaced by the generic fallback | `GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-002` | FAMILY_P1 injected into the learner canvas | `TECHNICAL_METADATA_ON_LEARNER_CANVAS` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-003` | italic property stripped from a Notes run | `NOTES_GLOSSARY_ITALIC_MISSES` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-004` | sixth card removed from a six-item grid | `CARDS_DROPPED_OR_INVENTED` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-005` | one quiz answer key removed | `QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-006` | superseded Tamat close-window copy restored | `TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-007` | confirmed screen-level Klik instruction removed from spoken VO | `ACTION_INSTRUCTIONS_MISSING_FROM_NOTES` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-008` | uncompleted sibling marked as ticked (Family S base page) | `COMPLETION_TICKS_NOT_MATCHING_PATH` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-008b` | uncompleted component marked as ticked (Struktur group master) | `COMPLETION_TICKS_NOT_MATCHING_PATH` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-009` | forced visual panel added to a specification popup | `SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-010` | S01 duplicated standalone component title re-introduced | `S01_DUPLICATE_STANDALONE_COMPONENT_TITLE` | ✅ FAILS | ✅ PASSES | MUTATION |
| `R-011` | canvas object moved below the stage boundary | `CANVAS_SHAPES_OUTSIDE_STAGE` | ✅ FAILS | ✅ PASSES | MUTATION |

---

# 3. The one that was missed, and what it exposed

`R-008` was **not detected on its first attempt**. The initial fixture cloned an `ItemCard` on the
group master; nothing failed. Investigating that produced the substantive finding of this stage:

> **No gate in the 188-check suite verified completion ticks on Family S screens or on the Struktur
> Taman group master.** Tick identity was checked for Family P1 and Family P2 only. A false
> completion tick on any of the 30 Family S pages, or on either group-master page, passed 188/188.

Two direct injections confirmed it — a real `Tick` shape added to a Family S examples base page and
to the group-master base page, both undetected.

`COMPLETION_TICKS_NOT_MATCHING_PATH` was added to the regression suite. It derives the expected
tick count for **every** page from the ordered path — including group-master component cards, which
are not model interaction items and were therefore invisible to the item-based gates. The suite is
now **189** checks; the corrected deck passes all of them, and both injections are detected.

**The deck itself was not regenerated and its bytes are unchanged.** Only the validator changed.

---

# 4. Why this matters more than the count

The suite reported 188/188 while a whole class of completion-state defect was unguarded. That is
the honest reading of Stage 4.1's headline number: it measured the checks that existed, not the
correctness of the deck. Two of the three defects found in Stage 4.1 were caught by *visual
inspection*, not by the suite, and this one needed a deliberate sensitivity test to surface.

`27` of the 189 predicates are flagged
for replacement in `QA_PREDICATE_AUDIT_v0.4.2.md`.
