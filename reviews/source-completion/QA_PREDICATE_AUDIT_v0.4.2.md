# QA_PREDICATE_AUDIT — v0.4.2

```
TOTAL_PREDICATES_AUDITED       = 189
PRESENCE_ONLY_CHECKS           = 32
SINGLE_AXIS_CHECKS             = 0
COUNT_WITHOUT_IDENTITY_CHECKS  = 13
MODEL_ONLY_CHECKS              = 60
SHARED_DERIVATION_CHECKS       = 21
VISIBILITY_BLIND_CHECKS        = 124
FAIL_OPEN_CHECKS               = 5
SELF_RESOLVED_JUDGMENT_CHECKS  = 2
CHECKS_REQUIRING_REPLACEMENT   = 27
```

# 1. Layers

| Layer | Checks | What it can and cannot prove |
|---|---:|---|
| `MODEL` | 60 | Proves the model is self-consistent. Proves **nothing** about the generated deck. |
| `PACKAGE_XML` | 110 | Proves text and shapes exist in the package. Blind to whether they are visible, clipped or covered. |
| `RENDERED_GEOMETRY` | 5 | Proves position and containment. |
| `ORACLE_CONFORMANCE` | 14 | Proves the value matches an independent expected value. Only **5** registry records have a frozen artifact oracle at all. |
| `MUTATION_SENSITIVITY` | 12 | Proves the gate fires. Says nothing about correctness. |

**Only 14 of 189 predicates compare
against an independently-derived expected value.** The rest test internal consistency or presence.

# 2. Weakness classes

| Class | Count | Reading |
|---|---:|---|
| A `PRESENCE_ONLY` | 32 | asserts something exists, not that it is the right something |
| B `SINGLE_AXIS_GEOMETRY` | 0 | closed in Stage 4.1 by `CANVAS_SHAPES_OUTSIDE_STAGE` |
| C `COUNT_WITHOUT_IDENTITY` | 13 | counts objects without checking which |
| D `MODEL_ONLY_ASSERTION` | 60 | the model agrees with itself; the package is not read |
| E `SHARED_DERIVATION` | 21 | generator and validator import the same helper |
| F `VISIBILITY_BLIND` | 124 | text is in the XML but may be clipped, covered or off-stage |
| G `FAIL_OPEN` | 5 | a degenerate or empty result satisfies the gate |
| H `SELF_RESOLVED_JUDGMENT` | 2 | CC resolved a CONDITIONAL to turn the gate green |

## 2.1 Class E is the structural one

21 predicates import `b02_visual_policy_v0_4`, `b02_glossary_v0_4`,
`b02_visual_directions_v0_4` or `b02_instructions_v0_4` — **the very modules the generator uses to
produce the values under test**. `GLOSSARY_IS_SINGLE_SOURCE` is the extreme case: it asserts that
the generator's splitter equals the glossary's, which is true by construction and can never fail.

These gates detect *drift between model and package*. They cannot detect a wrong shared rule. If
the glossary omits a term, both the deck and the validator omit it and the suite stays green. Only
an oracle extracted from frozen Bariah OOXML can catch that, and there are
2 such records.

## 2.2 Class H — the two self-resolving gates

`CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED = 0` passes because
`b02_visual_policy_v0_4.classify()` applies Bariah's Struktur Persisir Air pattern to **all nine**
component-main screens. Bariah supplied that pattern for **one**. The gate is green because CC
resolved the condition, not because Bariah did. `COMPONENT_MAIN_SCREENS_WITH_SPECIFIC_VISUAL`
inherits the same flaw.

`VISUAL_REQUIREMENT_REGISTER_v0.4.2.json` records the honest position:
**8 screens carry a generator-applied
direction with no direct authority for that individual screen.**

# 3. Checks requiring replacement

| check | layer | weaknesses |
|---|---|---|
| `GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `SOURCE_ROW_VISUAL_DIRECTIONS_MISSING` | MODEL | A_PRESENCE_ONLY, D_MODEL_ONLY_ASSERTION, G_FAIL_OPEN |
| `REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL` | PACKAGE_XML | A_PRESENCE_ONLY, E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `REQUIRED_VISUAL_POPUPS_WITHOUT_VISUAL` | PACKAGE_XML | A_PRESENCE_ONLY, E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `SPECIFICATION_POPUPS_WITH_FORCED_GENERIC_VISUAL` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `NOT_REQUIRED_VISUAL_POPUPS_FORCED_TO_HAVE_VISUAL` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED` | MODEL | D_MODEL_ONLY_ASSERTION, E_SHARED_DERIVATION, H_SELF_RESOLVED_JUDGMENT |
| `EXAMPLE_POPUPS_WITHOUT_VISUAL` | PACKAGE_XML | A_PRESENCE_ONLY, E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `EXAMPLE_POPUPS_WITH_GENERIC_FALLBACK` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `EXAMPLE_SCREENS_WITHOUT_VISUAL` | PACKAGE_XML | A_PRESENCE_ONLY, E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `COMPONENT_MAIN_SCREENS_WITH_SPECIFIC_VISUAL` | PACKAGE_XML | A_PRESENCE_ONLY, C_COUNT_WITHOUT_IDENTITY, F_VISIBILITY_BLIND, H_SELF_RESOLVED_JUDGMENT |
| `VISUAL_DIRECTION_WRONG_SOURCE_BINDING` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `VISUAL_DIRECTION_WRONG_COMPONENT_BINDING` | PACKAGE_XML | F_VISIBILITY_BLIND, G_FAIL_OPEN |
| `VISUAL_DIRECTIONS_WITHOUT_SOURCE_OR_BARIAH_BINDING` | MODEL | D_MODEL_ONLY_ASSERTION, E_SHARED_DERIVATION |
| `FAMILY_S_GENERIC_VISUAL_FALLBACKS` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `FAMILY_P1_GENERIC_VISUAL_FALLBACKS` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `FAMILY_P2_GENERIC_VISUAL_FALLBACKS` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `PROMENADE_GENERIC_FALLBACK_GONE` | ORACLE_CONFORMANCE | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `NOTES_GLOSSARY_ITALIC_MISSES` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `NOTES_RICH_TEXT_PACKAGE_ROUNDTRIP_FAILURES` | PACKAGE_XML | F_VISIBILITY_BLIND, G_FAIL_OPEN |
| `CANVAS_GLOSSARY_ITALIC_MISSES` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `GLOSSARY_IS_SINGLE_SOURCE` | MODEL | D_MODEL_ONLY_ASSERTION, E_SHARED_DERIVATION |
| `ANSWER_KEY_VISIBLE_DURING_LEARNER_PRE_SUBMISSION_STATE` | PACKAGE_XML | F_VISIBILITY_BLIND, G_FAIL_OPEN |
| `ACTION_INSTRUCTIONS_MISSING_FROM_NOTES` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `ACTION_INSTRUCTION_CANVAS_VO_MISMATCHES` | PACKAGE_XML | E_SHARED_DERIVATION, F_VISIBILITY_BLIND |
| `NOTES_CONTEXT_ACCIDENTALLY_MARKED_SPOKEN` | PACKAGE_XML | F_VISIBILITY_BLIND, G_FAIL_OPEN |

# 4. Recommended actions for Stage 4.2B

1. Replace class-E gates with oracle-conformance gates wherever a frozen artifact exists.
2. Split `CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED` into *resolved-by-authority* and
   *pending-human*, and stop treating pending as a failure to be engineered away.
3. Give class-C gates identity: assert *which* items are ticked, not how many.
4. Add a visibility layer: a shape whose text is covered by an opaque shape above it should fail.
5. Promote the glossary and the denylist to ratified artifacts rather than CC-authored lists.
