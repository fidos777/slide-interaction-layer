# STORYBOARD_QA_REPORT — v0.4.2

```
REVIEW_READY · BARIAH_LATEST_FEEDBACK_IMPLEMENTED · GOVERNANCE_HARDENED
PENDING_TARGETED_CONFIRMATION · NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

Deck `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_2.pptx` — 452,752 B,
`sha256 09bb08f2e391326a9e87cdee797b6ea3197c54373201b010e54096a1ec57ea1e`. v0.4 and v0.4.1 are retained as superseded audit artifacts.

# 1. Totals by layer — no single aggregate

| Layer | Checks | What it proves |
|---|---:|---|
| `MODEL` | 39 | the model is self-consistent |
| `PACKAGE_XML` | 173 | the generated package contains what the model says |
| `RENDERED_GEOMETRY` | 15 | position, containment, four edges, tick identity, visibility |
| `ORACLE_CONFORMANCE` | 9 | the value matches frozen Bariah OOXML, extracted by a module that imports nothing from the generator |
| `HISTORICAL_REPLAY` | 2 artifacts | v0.4 fails 44 gates; v0.4.1 fails 2 |
| `MUTATION_SENSITIVITY` | 12 | every gate fires on its own defect |
| **TOTAL** | **236 / 236 pass** | — |

**236/236 is not approval.** It is the count of checks that exist and pass.

# 2. Predicate hardening applied

| Weakness | Action |
|---|---|
| `SELF_RESOLVED_JUDGMENT` | `CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED` superseded (ID retained) by `CONDITIONAL_RESOLVED_BY_DIRECT_AUTHORITY`, `CONDITIONAL_PENDING_HUMAN`, `CONDITIONAL_SELF_RESOLVED_BY_CC`, `CONDITIONAL_WITH_GENERIC_FALLBACK_FILLER` |
| `COUNT_WITHOUT_IDENTITY` | `TICK_IDENTITY_MISMATCHES` matches each tick to the card it sits on and compares the ITEM SET, not the count |
| `SINGLE_AXIS_GEOMETRY` | `SHAPES_BEYOND_{LEFT,RIGHT,TOP,BOTTOM}_EDGE`, all four, every canvas shape |
| `VISIBILITY_BLIND` | `TEXT_COVERED_BY_OPAQUE_SHAPE`, `ANSWER_KEYS_COVERED`, `ANSWER_KEYS_OUTSIDE_STAGE` |
| `SHARED_DERIVATION` | 9 `ORACLE_*` gates take expected values from `b02_oracle_extract_v0_4_2`, asserted to import no generator module (`ORACLE_MODULE_IMPORTS_NO_GENERATOR`) |
| `FAIL_OPEN` | `*_EVALUATED` companions assert each population is non-empty, so no gate can pass vacuously |
| `PRESENCE_ONLY` | visual gates now compare against oracle/policy and reject the known fallback shape |
| `MODEL_ONLY` | typed-Notes and tick gates read the final package XML |

No check was removed. Two were superseded with their IDs retained and the reason recorded:
`CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED__SUPERSEDED_BY_CONDITIONAL_PENDING_HUMAN` and
`EXAMPLE_SCREENS_TOTAL__SUPERSEDED_BY_SUBTYPE_SPLIT`.

# 3. Replay

| ID | Fixture | Gate | Bad | v0.4.2 |
|---|---|---|---|---|
| `R-001` | Promenade direction replaced by the generic fallback | `GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES` | ✅ FAILS | ✅ PASSES |
| `R-002` | FAMILY_P1 injected into the learner canvas | `TECHNICAL_METADATA_ON_LEARNER_CANVAS` | ✅ FAILS | ✅ PASSES |
| `R-003` | italic property stripped from a Notes run | `NOTES_GLOSSARY_ITALIC_MISSES` | ✅ FAILS | ✅ PASSES |
| `R-004` | sixth card removed from a six-item grid | `CARDS_DROPPED_OR_INVENTED` | ✅ FAILS | ✅ PASSES |
| `R-005` | one quiz answer key removed | `QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY` | ✅ FAILS | ✅ PASSES |
| `R-006` | superseded Tamat close-window copy restored | `TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT` | ✅ FAILS | ✅ PASSES |
| `R-007` | confirmed screen-level Klik instruction removed from spoken VO | `ACTION_INSTRUCTIONS_MISSING_FROM_NOTES` | ✅ FAILS | ✅ PASSES |
| `R-008` | uncompleted sibling marked as ticked (Family S base page) | `COMPLETION_TICKS_NOT_MATCHING_PATH` | ✅ FAILS | ✅ PASSES |
| `R-008b` | uncompleted component marked as ticked (Struktur group master) | `COMPLETION_TICKS_NOT_MATCHING_PATH` | ✅ FAILS | ✅ PASSES |
| `R-009` | forced visual panel added to a specification popup | `SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL` | ✅ FAILS | ✅ PASSES |
| `R-010` | S01 duplicated standalone component title re-introduced | `S01_DUPLICATE_STANDALONE_COMPONENT_TITLE` | ✅ FAILS | ✅ PASSES |
| `R-011` | canvas object moved below the stage boundary | `CANVAS_SHAPES_OUTSIDE_STAGE` | ✅ FAILS | ✅ PASSES |

```
BAD_FIXTURES_DETECTED             = 12 / 12
BAD_FIXTURES_NOT_DETECTED         = 0
CORRECTED_ARTIFACT_FALSE_FAILURES = 0
v0.4  (superseded) failing gates  = 44
v0.4.1 (prior)     failing gates  = 2  ->  `EVIDENCE_CONFLICTS_IN_PRODUCTION_PANEL`, `EXAMPLE_SELECTION_SCREENS_WITH_INVENTED_VISUAL`
```

The v0.4.1 result matters: the hardened suite **discriminates the previous good deck from this one**,
because v0.4.1 rendered an invented visual on the four Family S Contoh screens and did not disclose
the Struktur Persisir Air evidence conflict.

# 4. Visual governance — nothing self-resolved

```
REQUIRED                                 25   all resolved
NOT_REQUIRED                             61   30 specification popups + completion/quiz/frames
CONDITIONAL                              14
  resolved by direct authority            1
  PENDING_HUMAN                          12
CONDITIONAL_SELF_RESOLVED_BY_CC           0
EVIDENCE_CONFLICTS disclosed              1
```

The Stage 4.1 `Pelbagai {name}` pattern is **retired as a propagated rule**. Bariah supplied it for
one screen; it had been applied to nine. Component-main screens now carry the module's own
source-attested direction and stay `PENDING_HUMAN`.

**One evidence conflict is disclosed rather than resolved.** For Struktur Persisir Air the transcript
says *"follow the reviewed treatment"* and then gives `[Visual: Pelbagai Struktur Persisir Air…]`,
but Bariah's own corrected slide 10 carries `[Visual: Rajah 23 — Contoh Boardwalk…]`. The transcript
value is rendered as the later explicit instruction; both are printed in the production panel and
flagged `PENDING_BARIAH_CONFIRMATION`.

# 5. Typed Notes blocks

```
NOTES_BLOCKS_TOTAL                 869
  NON_SPOKEN_CONTEXT               735
  SPOKEN_CONTENT_VO                109
  SPOKEN_INTERACTION_INSTRUCTION   25
  PRODUCTION_INSTRUCTION_NOT_SPOKEN 0
NOTES_BLOCKS_WITHOUT_TYPE          0
NOTES_BLOCKS_WITHOUT_SPOKEN_FLAG   0
NON_SPOKEN_BLOCKS_IN_SPOKEN_EXPORT 0
SPOKEN_BLOCKS_MISSING_FROM_NOTES   0
SILENT_STATES_WITH_NOTES_BLOCKS    0
SPOKEN_EXPORT_LINES                134
```

TTS export filters on `spoken == true`. Order is never used to infer speech.

# 6. Bounded parity

```
CONFIRMED_SCREEN_LEVEL_CLICK_MISMATCHES = 0
MICRO_CONTROL_SCOPE_SELF_RESOLVED       = 0
REVIEW_ONLY_ANSWER_KEYS_IN_SPOKEN_VO    = 0
INSTRUCTIONS_WITH_UNCLASSIFIED_AUTHORITY = 0
```

The CC-invented quiz-result instruction (*"Klik Semak Jawapan…"*) has been **withdrawn** from canvas
and VO and marked `PENDING_BARIAH_CONFIRMATION`. Close icons, Kembali and completion controls are
deliberately not given spoken instructions.

# 7. Counts unchanged

```
REVIEW_PAGES 100 · LEARNER_SCREENS 29 · RUNTIME_STATES 100
INTERACTION_ITEMS 54 · SOURCE_ROWS 26 · SOURCE_ASSETS 14 · COMPONENTS 9
SLIDES_MANUALLY_PATCHED 0
```

# 8. NOT CHECKED

Microsoft PowerPoint font wrapping · PowerPoint Notes appearance · Slide Show behaviour · LMS
navigation · human visual suitability · the 12 CONDITIONAL visual decisions · final multimedia
suitability · complete module DOCX integrity · glossary completeness · denylist completeness.

LibreOffice retested: still no Impress import filter. **Microsoft PowerPoint equivalence is not
claimed.**
