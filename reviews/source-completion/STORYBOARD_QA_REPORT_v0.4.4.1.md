# STORYBOARD_QA_REPORT — v0.4.4.1

Deck: `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4_1.pptx` — 100 review pages.

Suite: `generator/v0_4/b02_governance_qa_v0_4_4_1.py`, chaining the Stage 4.2E-B, 4.2C,
4.2B, 4.1 and Stage 4 suites.

Stage 4.2E-C is a metadata and governance correction. Learner-facing instructional delta
from v0.4.4: **zero**, proved shape by shape in §6.

# 1. Test accounting

| Metric | Value |
|---|---:|
| `ACTIVE_TEST_GATES_PASSING` | **441 / 441** |
| `SUPERSESSION_MARKERS_PRESENT` | **20** |
| `TOTAL_EMITTED_GATE_RECORDS` | **461** |

A supersession marker is an **inert self-assertion**: expected and actual are both the
constant `SUPERSEDED`. It exists so a retired ruling stays visible instead of vanishing from
the suite. Twenty of them are not twenty passing checks.

## 1.1 A correction to the v0.4.4 figures

The v0.4.4 artifacts reported 367 active / 19 markers / 386 records. The 19 came from
substring-matching `SUPERSEDED` in the **gate ID**, which swept in six ordinary live tests —
`SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL`, `SUPERSEDED_DIRECTION_RENDERED_AS_ACTIVE`,
`SUPERSEDED_RULINGS_EVALUATED`, `SHOT_S01_SUPERSEDED_SPOKEN_LINES_GONE`,
`SHOT_PERSISIR_SUPERSEDED_DIRECTION_NOT_ON_CANVAS`,
`SHOT_PERSISIR_SUPERSEDED_STATUS_RECORDED`.

By the definition above, v0.4.4 had **13** markers and **373** active passing gates. The
published figures understated the live suite by six. `accounting()` in the Stage 4.2E-C
suite now computes all three from the definition rather than from a name. The v0.4.4
artifacts are left as published — they record what was reported at the time — and the
correction is filed under B02-META-REG-001.

Seven of this release's twenty markers are new: six retire the CONDITIONAL / PENDING_HUMAN /
PROVISIONAL component-main position (§3), and one retires the gate that conflated
requirement authority with subject authority.

# 2. B02-META-REG-001 — artifact version and status drift

Confirmed by direct package inspection: **100 of 100** pages of v0.4.4 carried the version
line written for v0.4 and the Stage 4 release tokens. Verbatim strings, the emitting source
and the full analysis of why the suite could not see it are in
`B02_DEFECT_REGISTER_v0.4.4.1.md`.

The short version of the failure: one gate forbade only the *previous* version number and
never asked what the version should be, so it stayed green through four releases of drift.
The other **required** the retired tokens to be present on every page — the suite did not
tolerate the wrong release status, it mandated it, and correcting the panel would have turned
three gates red.

Corrected by one controlled identity source, `b02_artifact_identity_v0_4_4_1.py`, read by the
panel, the run manifest, the QA suite, the checklist and this report. Results:

| | |
|---|---:|
| `ACTIVE_PANEL_VERSION` | `v0.4.4.1` |
| `PANEL_VERSION_MANIFEST_MISMATCHES` | 0 |
| `PANEL_STATUS_MANIFEST_MISMATCHES` | 0 |
| `STALE_RELEASE_TOKENS` | 0 |
| `SUPERSEDED_VERSION_LINES_IN_PACKAGE` | 0 |
| `PANEL_STATUS_TOKEN_SET_MISMATCHES` | 0 |

Comparison is by exact token set, recovered by splitting the panel line on its separator.
Two substring traps made that necessary and both would have gone the wrong way:
`CANONICALLY_FROZEN` is contained in the active `NOT_CANONICALLY_FROZEN`, and
`… PAPAN CERITA v0.4` is a prefix of `… PAPAN CERITA v0.4.4.1`.

# 3. Component-main visual governance

Nine component-main pages, population pinned to `learner_screen_id` through the frozen
overview mapping and cross-checked against what the package itself declares — 22 bound pages
evaluated, 9 carrying the `COMPONENT_MAIN_SCREEN` block, covering all nine screens.

| | |
|---|---:|
| `COMPONENT_MAIN_PAGES` | 9 |
| `COMPONENT_MAIN_VISUAL_REQUIREMENT_REQUIRED` | 9 |
| `COMPONENT_MAIN_MAPPING_STATUS_RESOLVED` | 9 |
| `COMPONENT_MAIN_MAPPING_COMPLETE` | 9 |
| `COMPONENT_MAIN_PENDING_HUMAN` | 0 |
| `COMPONENT_MAIN_PROVISIONAL_VISUAL_PROPOSALS` | 0 |
| `UNAUTHORISED_SUBJECT_AUTHORITY_PROMOTIONS` | 0 |

**The authority split is the point of this section.** D2 (6:52 PM) settles the *requirement*
and the *treatment* for all nine; it names a *subject* for none of them. So:

- requirement authority — `BARIAH_DIRECT_SCREENSHOT`, all nine;
- treatment authority — `BARIAH_DIRECT_SCREENSHOT`, all nine;
- subject provenance — `MODULE_SOURCE_ATTESTED`, all 27 subjects, of which the two Papan
  Tanda figures are additionally recorded as directly named in D4;
- direction authority on the page — unchanged from v0.4.4: `BARIAH_DIRECT` for Struktur
  Persisir Air, `SOURCE_ATTESTED_COMPONENT_VISUAL` for the other eight.

The gate `COMPONENT_MAIN_RESOLVED_WITHOUT_BARIAH_AUTHORITY` had to be superseded rather than
carried forward, and this is worth stating plainly. It required the *direction's* authority to
be `BARIAH_DIRECT` wherever the status was RESOLVED. That was serviceable while only one
component main was resolved. Read forward unchanged against nine resolved screens, it would
have demanded exactly the promotion this stage forbids — it would have forced eight
module-attested directions to claim Bariah named them. It is replaced by
`COMPONENT_MAIN_REQUIREMENT_WITHOUT_BARIAH_AUTHORITY` (requirement and treatment) and
`COMPONENT_MAIN_DIRECTION_AUTHORITIES` (the two-value direction authority set), which assert
the same discipline without collapsing the two.

Lineage is preserved in `COMPONENT_MAIN_VISUAL_GOVERNANCE_v0.4.4.1.json`, per component,
under `superseded_lineage` — not printed as the live status of a settled question.

# 4. `Title 1` — outcome **B**, `UNREGISTERED_GEOMETRY_EXEMPTION`

| Question | Finding |
|---|---|
| Placeholder type | real `<p:ph type="title"/>`, `<a:spLocks noGrp="1"/>`, written by `title_ph_rt` |
| Page population | all 100 slides, one per slide |
| Intentional? | yes — PowerPoint outline pane, accessibility name, slide navigator, Ctrl+F |
| Learner-facing? | no — `y = -0.631 in`, bottom `-0.059 in`, entirely above the stage, never in Slide Show |
| Did the gate exclude it? | yes, but by `if s["y"] < -0.66` — a bare number, not a rule |
| Exclusion mechanism | **none registered** |

Outcome A required the exclusion to be "explicit and named". A numeric threshold chosen to
clear one shape is neither: any ordinary shape parked between `-0.66` and `0` passed with it,
and nothing recorded that this was deliberate. **Outcome B.**

The audit found a second, larger instance of the same class. The four-edge gate iterated the
package reader's `canvas` partition, and the reader routes any shape with `(x + w) <= 0` into
`panel` instead. `ProdPanel` at `x = -6.90 in` was therefore never evaluated on any edge — and
neither would anything else pushed fully left of the stage.

Registered, not weakened:

- `GEX-001` `Title 1` — requires a real title placeholder, exempts the **top** edge only;
- `GEX-002` `ProdPanel` — requires a non-placeholder shape, exempts the **left** edge only.

An entry matches only on placeholder-ness, placeholder type, shape name **and all four
coordinates to 0.001 in**, and clears only the edges it names. The top threshold is back to
`-0.01`, and the gate now iterates every shape on the slide, not the canvas partition.

| | |
|---|---:|
| `UNREGISTERED_OFF_CANVAS_EXEMPTIONS` | `[]` |
| `ORDINARY_OFF_CANVAS_SHAPES_ALLOWED` | 0 |
| `EXEMPTED_SHAPES_EVALUATED` | 200 (100 `Title 1` + 100 `ProdPanel`) |
| `SHAPES_BEYOND_{LEFT,RIGHT,TOP,BOTTOM}_EDGE` | 0, 0, 0, 0 |
| `GEOMETRY_SHAPES_EVALUATED_INCLUDING_OFF_CANVAS` | 1,813 shapes |

Neither shape was moved or deleted. Deleting the title placeholder would leave every slide
untitled in the outline pane and in the accessibility tree; it is not proven unnecessary.

Four fixtures hold the registry shut — see §5, `M-08` to `M-11`.

# 5. Mutation sensitivity

`generator/audit/b02_replay_v0_4_4_1.py` — the 39 Stage 4.2E-B fixtures rebased onto
v0.4.4.1, plus twelve new ones.

| | |
|---|---:|
| Fixtures | 51 |
| Detected | 51 |
| `MUTATION_FIXTURES_MISSED` | **0** |
| `CORRECTED_V0_4_4_1_FALSE_FAILURES` | **0** |

The twelve new fixtures, and what each attacks:

| | Fixture | Attacks |
|---|---|---|
| `M-01` | panel version reverted to v0.4 | the drift that caused this stage |
| `M-02` | a status token reverted to the retired one | release-status claim |
| `M-03` | a retired confirmation token reinserted | release-status claim |
| `M-04` | a component main set back to `CONDITIONAL` | §3 |
| `M-05` | a component-main mapping status set back to pending | §3 |
| `M-06` | the provisional-proposal class reinserted | §3 |
| `M-07` | subject provenance promoted on the page | authority split |
| `M-08` | the `GEX-001` registry entry removed | §4 |
| `M-09` | an ordinary shape at the placeholder's exact coordinates | §4 |
| `M-10` | an ordinary shape renamed `Title 1`, no placeholder type | §4 |
| `M-11` | the registered placeholder moved | §4 |
| `M-12` | a subject promoted in the frozen mapping contract itself | authority split |

`M-08`, `M-11` and `M-12` do not mutate the package — they mutate the registry and the frozen
contract, and the harness reverts each patch before the next fixture runs. `M-12` is a
fail-closed check: `component_main_governance()` raises rather than emitting a promoted
provenance.

# 6. Learner-facing delta — zero

Read back out of both packages and compared shape by shape:

| | |
|---|---:|
| Pages with any learner-canvas difference (name, text, x, y, w, h) | **0 / 100** |
| Pages with any Speaker Notes difference | **0 / 100** |
| Notes italic runs, v0.4.4 → v0.4.4.1 | 40 → **40** |
| Pages with a production-panel difference | 100 / 100 (the intended change) |
| `EMBEDDED_MEDIA` | 0 |
| Overview cardinalities | 5, 5, 3, 3, 3, **2**, 3, 2, **1** |

Structural invariants: `REVIEW_PAGES` 100, `LEARNER_SCREENS` 29, `RUNTIME_STATES` 100,
`INTERACTION_ITEMS` 54, `SOURCE_ROWS` 26, `SOURCE_ASSETS` 14, `COMPONENTS` 9,
`SLIDES_MANUALLY_PATCHED` 0.

# 7. Rendered inspection

All 100 pages rendered with the frozen `generator/b02_render_check.py` and inspected.

| | |
|---|---:|
| `TEXT_OVERFLOW` | 0 |
| `SHAPES_OUTSIDE_STAGE` (unregistered) | 0 |
| `UNINTENDED_OVERLAPS` | 0 |
| Box overlaps reported | 202, all modal overlays (`PopupPanel` / `VisualPanel` over the screen behind) |
| Render report vs v0.4.4 | **byte-identical**, page for page |

The render report being identical to v0.4.4's is the strongest single statement available
here: the layout did not drift, because nothing on the canvas moved.

Pages inspected individually: S01 (1), Slide 5 / Struktur Persisir Air main (5), all nine
component mains, Papan Tanda (51–56), BBQ Pit (85–90), a page carrying the off-canvas title
placeholder (all 100 carry it; 1 and 5 inspected directly), the five quiz pages, and Tamat.
The production panel is a shared layout element, so all 100 pages were rendered and their
reports compared, not a sample.

# 8. What this build does **not** prove

- **Microsoft PowerPoint equivalence.** This container has no Impress import filter, so
  `soffice --convert-to pdf` fails outright. Rendering is a package parser with Liberation
  Sans metrics. **No smoke test has run.** That is the next stage and this deck is its
  candidate.
- **Instructional correctness.** Nothing checks whether the teaching is right.
- **Visual suitability.** Directions are text. No image is embedded or assessed.
- **Actual LMS navigation.** The Tamat mechanism stays LMS-owner metadata, both route claims
  marked NOT PROVEN.
- **Completeness outside the fixture set.** 51 fixtures cover the defects we have thought of.

# 9. Open, and not ours to close

- **MS2680** — source authority.
- **`B02-CAIR-INT-001`**, canonical module DOCX integrity — Firdaus / CAIR.
- **PL06 pronunciation precedence** — source governance; `RESERVED_NOT_ACTIVE`, implemented
  nowhere.

# 10. Standing

`REVIEW_CANDIDATE` · `FINAL_BARIAH_DECISIONS_IMPLEMENTED` · `INSTANCE_MAPPING_COMPLETE` ·
`READY_FOR_MICROSOFT_POWERPOINT_SMOKE` · `NOT_FOR_MMD_BUILD` · `NOT_CANONICALLY_FROZEN` ·
`MULTIMEDIA_NOT_PRODUCED`

Not asserted: `PRODUCTION_APPROVED`, `CANONICAL_FREEZE`, `MMD_BUILD_READY`,
`SOURCE_INTEGRITY_FULLY_VERIFIED`, `MICROSOFT_POWERPOINT_EQUIVALENCE`,
`SOURCE_GOVERNANCE_COMPLETE`.

# 11. Full gate output

```
PASS  SOURCE_ROWS_EXPECTED                                                                    26
PASS  SOURCE_ROWS_ACCOUNTED                                                                   26
PASS  SOURCE_ROWS_CREATED                                                                     0
PASS  DUPLICATE_SOURCE_ROW_UID                                                                0
PASS  SOURCE_ASSETS_EXPECTED                                                                  14
PASS  SOURCE_ASSETS_ACCOUNTED                                                                 14
PASS  ORPHAN_SOURCE_ASSETS                                                                    0
PASS  INTERACTION_ITEMS_WITHOUT_SOURCE_BINDING                                                0
PASS  INTERACTION_ITEMS_WITHOUT_LOCATOR                                                       0
PASS  INTERACTION_ITEMS_WITHOUT_FAMILY                                                        0
PASS  STATES_WITHOUT_DECISION_ID                                                              0
PASS  SOURCE_ROWS_WITHOUT_A_REVIEW_PAGE                                                       0
PASS  SOURCE_ROW_LOCATOR_IN_PANEL                                                             0
PASS  FAMILY_S_COMPONENTS                                                                     4
PASS  FAMILY_P1_COMPONENTS                                                                    3
PASS  FAMILY_P2_COMPONENTS                                                                    2
PASS  UNKNOWN_COMPONENT_FAMILY                                                                0
PASS  COMPONENTS_GENERATED                                                                    9
PASS  PAPAN_TANDA_SPEC_CATEGORIES                                                             4
PASS  BBQ_PIT_SPEC_CATEGORIES                                                                 4
PASS  BBQ_PIT_CATEGORY_LABELS                                                                 ['Bahan Pembinaan', 'Dimensi', 'Gril', 'Keselamatan']
PASS  GENERIC_ONE_ITEM_PAPAN_TANDA_SCREEN                                                     0
PASS  GENERIC_ONE_ITEM_BBQ_PIT_SCREEN                                                         0
PASS  PAPAN_TANDA_SOURCE_ROWS_CREATED_BY_SPLIT                                                0
PASS  BBQ_PIT_SOURCE_ROWS_CREATED_BY_SPLIT                                                    0
PASS  CARDS_DROPPED_OR_INVENTED                                                               0
PASS  RUNTIME_STATES_WITHOUT_PARENT                                                           0
PASS  RETURN_TARGET_MISSING                                                                   0
PASS  POPUP_PARENT_IS_POPUP                                                                   0
PASS  UNKNOWN_CONTROL_TYPE                                                                    0
PASS  REVIEW_PAGES_EQUAL_RUNTIME_STATES                                                       100
PASS  FAMILY_S_PREMATURE_KEMBALI                                                              0
PASS  FAMILY_P1_FALSE_SIBLING_TICKS                                                           0
PASS  FAMILY_P1_PREMATURE_EXAMPLE_COMPLETION                                                  0
PASS  FAMILY_P2_PREMATURE_COMPONENT_COMPLETION                                                0
PASS  DUPLICATE_CUSTOM_SETERUSNYA                                                             0
PASS  TEXT_TUTUP_BUTTON                                                                       0
PASS  POPUPS_WITHOUT_CLOSE_ICON                                                               0
PASS  CLOSE_ICON_TITLE_COLLISIONS                                                             0
PASS  S01_NOTES_POLICY__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT                                'SUPERSEDED'
PASS  S01_NOTES_POLICY                                                                        'SPOKEN_ENTRY_TITLES_PLUS_START_INSTRUCTION'
PASS  S01_SPOKEN_ELEMENTS__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT                             'SUPERSEDED'
PASS  S01_SPOKEN_ELEMENTS                                                                     3
PASS  S01_PL06_TITLE_SPOKEN__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT                           'SUPERSEDED'
PASS  S01_PL06_TITLE_SPOKEN__SUPERSEDED_BY_D3_PUNCTUATION_RULING                              'SUPERSEDED'
PASS  S01_PL06_TITLE_SPOKEN                                                                   True
PASS  S01_PL06_TITLE_SPOKEN_WITH_TRAILING_PERIOD                                              False
PASS  S01_PL06_TITLE_LONG_FORM_WITHDRAWN                                                      False
PASS  S01_TOPIC_TITLE_SPOKEN                                                                  True
PASS  S01_ORIENTATION_SPOKEN__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT                          'SUPERSEDED'
PASS  S01_ORIENTATION_SENTENCE_REMOVED                                                        False
PASS  S01_MULA_INSTRUCTION_SPOKEN__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT                     'SUPERSEDED'
PASS  S01_MULA_INSTRUCTION_SPOKEN                                                             True
PASS  S01_MULA_INSTRUCTION_OLD_WORDING_WITHDRAWN                                              False
PASS  S01_TOPIC_LINE_ON_CANVAS                                                                True
PASS  S01_VISUAL_HEADING_ON_CANVAS                                                            True
PASS  S01_COURSE_INTRO_REPEATED                                                               False
PASS  S01_PL06_OBJECTIVES_REPEATED                                                            False
PASS  S01_TOPIC_LIST_REPEATED                                                                 False
PASS  S01_HILMI_REINTRODUCED                                                                  False
PASS  S01_COURSE_TITLE_NOT_SPOKEN                                                             False
PASS  S02_CAST                                                                                ['Alya', 'Encik Rahman']
PASS  S02_CAST_IN_TRANSCRIPT                                                                  True
PASS  S02_MS2680_LEARNER_CLAIMS                                                               0
PASS  S02_MS2680_IN_PRODUCTION_PANEL                                                          True
PASS  S02_GENERIC_ROLE_NAMES_AS_FINAL_NAMES                                                   0
PASS  S03_NARRATOR                                                                            ['Hilmi']
PASS  S03_HILMI_REINTRODUCED_AS_NEW                                                           False
PASS  S03_MIND_MAP_DIRECTION_PRESENT                                                          True
PASS  S03_BOTH_GROUPS_PRESENT                                                                 True
PASS  S03_ALL_NINE_COMPONENTS                                                                 9
PASS  HILMI_LABEL_OUTSIDE_S03                                                                 0
PASS  RUMUSAN_FORBIDDEN_LABELS_DISPLAYED                                                      0
PASS  QUIZ_ITEMS                                                                              5
PASS  QUIZ_MCQ                                                                                4
PASS  QUIZ_MULTIPLE_RESPONSE                                                                  1
PASS  QUIZ_MR_LETTER_LABELS                                                                   0
PASS  QUIZ_IMMEDIATE_FEEDBACK_VARIANTS                                                        2
PASS  QUIZ_QUESTIONS_WITHOUT_BOTH_FEEDBACK_VARIANTS                                           0
PASS  QUIZ_DETAILED_RATIONALE_LEARNER_FACING                                                  0
PASS  QUIZ_RATIONALE_IN_PRODUCTION_PANEL                                                      0
PASS  QUIZ_RESULT_ELEMENTS                                                                    True
PASS  QUIZ_REVIEW_STATE_PRESENT                                                               1
PASS  TAMAT_COPY_STATUS                                                                       'CONFIRMED_BARIAH'
PASS  TAMAT_LOGICAL_DESTINATION                                                               'NEXT_BAHAGIAN'
PASS  TAMAT_PHYSICAL_NAVIGATION_STATUS                                                        'PENDING_FIRDAUS_OR_LMS_CONFIRMATION'
PASS  TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT                                                  False
PASS  TAMAT_UNVERIFIED_PHYSICAL_NAVIGATION_CLAIM                                              0
PASS  TAMAT_NO_CANVAS_NEXT_BUTTON                                                             0
PASS  CONTENT_SLIDES_WITHOUT_NOTES                                                            0
PASS  S02_ONWARDS_PL_TITLE_REANNOUNCEMENTS                                                    0
PASS  S02_ONWARDS_TOPIC_TITLE_REANNOUNCEMENTS                                                 0
PASS  CONTEXT_BLOCK_MISSING_ON_CONTENT_SLIDES                                                 0
PASS  SILENT_STATES_WITH_NONEMPTY_NOTES                                                       0
PASS  TECHNICAL_IDS_IN_FINAL_NOTES                                                            0
PASS  BARIAH_REVIEW_ANNOTATIONS_IN_DECK                                                       0
PASS  BARIAH_ANNOTATIONS_IN_NOTES                                                             0
PASS  V0_3_TOKENS_IN_PANEL                                                                    0
PASS  PANEL_VERSION_LINES_READ                                                                100
PASS  ACTIVE_PANEL_VERSION                                                                    ['v0.4.4.1']
PASS  PANEL_VERSION_MISMATCHES                                                                0
PASS  SUPERSEDED_VERSION_LINES_IN_PANEL                                                       0
PASS  PANEL_STATUS_TOKEN_SET_MISMATCHES                                                       0
PASS  PACKAGE_TOKEN_REVIEW_CANDIDATE                                                          True
PASS  PACKAGE_TOKEN_FINAL_BARIAH_DECISIONS_IMPLEMENTED                                        True
PASS  PACKAGE_TOKEN_INSTANCE_MAPPING_COMPLETE                                                 True
PASS  PACKAGE_TOKEN_READY_FOR_MICROSOFT_POWERPOINT_SMOKE                                      True
PASS  PACKAGE_TOKEN_NOT_FOR_MMD_BUILD                                                         True
PASS  PACKAGE_TOKEN_NOT_CANONICALLY_FROZEN                                                    True
PASS  PACKAGE_TOKEN_MULTIMEDIA_NOT_PRODUCED                                                   True
PASS  STALE_STATUS_TOKEN_REVIEW_READY                                                         0
PASS  STALE_STATUS_TOKEN_PENDING_TARGETED_CONFIRMATION                                        0
PASS  STALE_STATUS_TOKEN_BARIAH_FEEDBACK_IMPLEMENTED                                          0
PASS  STALE_RELEASE_TOKENS                                                                    0
PASS  FORBIDDEN_STATUS_TOKEN_PRODUCTION_READY                                                 0
PASS  FORBIDDEN_STATUS_TOKEN_MMD_READY                                                        0
PASS  FORBIDDEN_STATUS_TOKEN_CANONICALLY_FROZEN                                               0
PASS  FORBIDDEN_TOKEN_PRODUCTION_APPROVED                                                     0
PASS  FORBIDDEN_TOKEN_CANONICAL_FREEZE                                                        0
PASS  FORBIDDEN_TOKEN_MMD_BUILD_READY                                                         0
PASS  FORBIDDEN_TOKEN_SOURCE_INTEGRITY_FULLY_VERIFIED                                         0
PASS  FORBIDDEN_TOKEN_MICROSOFT_POWERPOINT_EQUIVALENCE                                        0
PASS  FORBIDDEN_TOKEN_SOURCE_GOVERNANCE_COMPLETE                                              0
PASS  APPROVED_TERMS_NOT_ITALICISED                                                           0
PASS  APPROVED_TERMS_ITALICISED_AT_LEAST                                                      True
PASS  PRODUCTION_IDS_ITALICISED                                                               0
PASS  BBQ_PIT_LOWERCASE_P_ON_CANVAS                                                           0
PASS  WPC_NORMALISATION_PRESENT                                                               True
PASS  PROMENADE_PRESENT                                                                       True
PASS  PAGES_WITHOUT_PRODUCTION_PANEL                                                          0
PASS  PRODUCTION_PANEL_ON_CANVAS                                                              0
PASS  PRODUCTION_PANEL_MISSING_FIELD                                                          0
PASS  VISUAL_DIRECTIONS_AUDITED                                                               26
PASS  VISUAL_DIRECTIONS_PENDING                                                               0
PASS  GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES                                               0
PASS  SOURCE_ROW_VISUAL_DIRECTIONS_MISSING                                                    0
PASS  POPUP_PAGES                                                                             46
PASS  REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL                                                  0
PASS  REQUIRED_VISUAL_POPUPS_WITHOUT_VISUAL                                                   0
PASS  SPECIFICATION_POPUPS_TOTAL                                                              30
PASS  SPECIFICATION_POPUPS_REQUIRING_VISUAL                                                   0
PASS  SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL                                      0
PASS  SPECIFICATION_POPUPS_WITH_FORCED_GENERIC_VISUAL                                         0
PASS  NOT_REQUIRED_VISUAL_POPUPS_FORCED_TO_HAVE_VISUAL                                        0
PASS  CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED__SUPERSEDED_BY_CONDITIONAL_PENDING_HUMAN     'SUPERSEDED'
PASS  CONDITIONAL_RESOLVED_BY_DIRECT_AUTHORITY__SUPERSEDED_BY_D2_COMPONENT_MAIN_RULING        'SUPERSEDED'
PASS  CONDITIONAL_PENDING_HUMAN__SUPERSEDED_BY_D2_COMPONENT_MAIN_RULING                       'SUPERSEDED'
PASS  CONDITIONAL_PENDING_HUMAN_ARE_COMPONENT_MAINS__SUPERSEDED_BY_D2_COMPONENT_MAIN_RULING   'SUPERSEDED'
PASS  COMPONENT_MAINS_MARKED_PROVISIONAL__SUPERSEDED_BY_D2_COMPONENT_MAIN_RULING              'SUPERSEDED'
PASS  COMPONENT_MAIN_SELF_RESOLVED_BY_CC                                                      0
PASS  COMPONENT_MAINS_STILL_CONDITIONAL                                                       0
PASS  COMPONENT_MAINS_STILL_PENDING_HUMAN                                                     0
PASS  COMPONENT_MAINS_STILL_PROVISIONAL                                                       0
PASS  CONDITIONAL_SELF_RESOLVED_BY_CC                                                         0
PASS  CONDITIONAL_WITH_GENERIC_FALLBACK_FILLER                                                0
PASS  EXAMPLE_POPUPS_TOTAL                                                                    16
PASS  EXAMPLE_POPUPS_WITH_SPECIFIC_VISUAL                                                     16
PASS  EXAMPLE_POPUPS_WITHOUT_VISUAL                                                           0
PASS  EXAMPLE_POPUPS_WITH_GENERIC_FALLBACK                                                    0
PASS  EXAMPLE_SCREENS_TOTAL__SUPERSEDED_BY_SUBTYPE_SPLIT                                      'SUPERSEDED'
PASS  EXAMPLE_DETAIL_SCREENS_TOTAL                                                            8
PASS  EXAMPLE_SELECTION_SCREENS_TOTAL                                                         4
PASS  EXAMPLE_SELECTION_SCREENS_WITH_INVENTED_VISUAL__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT  'SUPERSEDED'
PASS  EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL                                                0
PASS  EXAMPLE_SELECTION_SCREENS_WITH_PER_EXAMPLE_VISUAL                                       4
PASS  EXAMPLE_CARD_VISUALS_EVALUATED                                                          16
PASS  EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED                                                0
PASS  EXAMPLE_SELECTION_SCREENS_IDENTIFIED                                                    4
PASS  EXAMPLE_SELECTION_STATE_PAGES_EVALUATED                                                 24
PASS  EXAMPLE_SELECTION_STATES_MISSING_CARD_VISUALS                                           0
PASS  EXAMPLE_SELECTION_SCREEN_LEVEL_INVENTED_DIRECTION                                       0
PASS  EXAMPLE_SCREENS_WITH_SPECIFIC_VISUAL                                                    8
PASS  EXAMPLE_SCREENS_WITHOUT_VISUAL                                                          0
PASS  COMPONENT_MAIN_SCREENS_WITH_SPECIFIC_VISUAL                                             9
PASS  S01_DISPLAY_TITLE                                                                       True
PASS  S01_DUPLICATE_STANDALONE_COMPONENT_TITLE                                                0
PASS  S01_SPECIFIC_VISUAL_DIRECTION_PRESENT                                                   True
PASS  REQUIRED_VISUAL_PANEL_MISSING                                                           0
PASS  VISUAL_PANEL_HEADING_MISSING                                                            0
PASS  VISUAL_PANEL_CONTENT_OVERRUN                                                            0
PASS  VISUAL_PANEL_CLOSE_ICON_COLLISION                                                       0
PASS  VISUAL_DIRECTION_WRONG_SOURCE_BINDING                                                   0
PASS  VISUAL_DIRECTION_WRONG_COMPONENT_BINDING                                                0
PASS  VISUAL_DIRECTIONS_WITHOUT_SOURCE_OR_BARIAH_BINDING                                      0
PASS  FAMILY_S_GENERIC_VISUAL_FALLBACKS                                                       0
PASS  FAMILY_P1_GENERIC_VISUAL_FALLBACKS                                                      0
PASS  FAMILY_P2_GENERIC_VISUAL_FALLBACKS                                                      0
PASS  FAMILY_S_POPUPS_WITH_SPECIFIC_VISUAL_DIRECTION                                          16
PASS  FAMILY_S_VISUAL_PANEL_MISSING                                                           0
PASS  PROMENADE_SPECIFIC_VISUAL_DIRECTION                                                     True
PASS  PROMENADE_GENERIC_FALLBACK_GONE                                                         False
PASS  NOTES_GLOSSARY_OCCURRENCES_FOUND                                                        40
PASS  NOTES_GLOSSARY_OCCURRENCES_ITALICISED                                                   40
PASS  NOTES_GLOSSARY_ITALIC_MISSES                                                            0
PASS  NOTES_FALSE_ITALICS_ON_TECHNICAL_IDS                                                    0
PASS  NOTES_MARKDOWN_ITALIC_MARKERS                                                           0
PASS  NOTES_RICH_TEXT_PACKAGE_ROUNDTRIP_FAILURES                                              0
PASS  NOTES_ITALIC_RUNS_IN_PACKAGE                                                            True
PASS  CANVAS_GLOSSARY_ITALIC_MISSES                                                           0
PASS  GLOSSARY_IS_SINGLE_SOURCE                                                               True
PASS  QUIZ_QUESTIONS                                                                          5
PASS  QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY                                               5
PASS  QUIZ_REVIEW_PAGES_WITHOUT_ANSWER_KEY                                                    0
PASS  MCQ_ANSWER_KEYS_WITH_LETTER_AND_TEXT                                                    4
PASS  MULTIPLE_RESPONSE_ANSWER_KEY_USES_FULL_OPTION_TEXT                                      True
PASS  ANSWER_KEY_SOURCE_MISMATCH                                                              0
PASS  MULTIPLE_RESPONSE_LEARNER_OPTIONS_WITH_LETTER_LABELS                                    0
PASS  ANSWER_KEY_LABELLED_AS_REVIEWER_INFO                                                    0
PASS  ANSWER_KEY_VISIBLE_DURING_LEARNER_PRE_SUBMISSION_STATE                                  0
PASS  ANSWER_KEY_READ_IN_VO                                                                   0
PASS  TAMAT_TITLE_MATCHES_BARIAH_EXEMPLAR                                                     True
PASS  TAMAT_LEARNER_INSTRUCTION_MATCHES_BARIAH_EXEMPLAR                                       True
PASS  TAMAT_HIERARCHY_COMPLETE                                                                6
PASS  TAMAT_SPOKEN_TRANSCRIPT_MATCHES                                                         True
PASS  TAMAT_NON_SPOKEN_CONTEXT_RETAINED                                                       True
PASS  PERABOT_OVERVIEW_VISUAL_CARDS                                                           5
PASS  PERABOT_COMPONENT_NAMES_PRESENT                                                         5
PASS  PERABOT_COMPONENTS_WITH_VISUAL_DIRECTION                                                5
PASS  PERABOT_COMPONENT_NAMES_CORRECT                                                         ['BBQ Pit', 'Drinking Fountain', 'Kerusi Taman', 'Papan Tanda', 'Tong Sampah']
PASS  PERABOT_OVERVIEW_INTERNAL_MAPPING_UNCHANGED                                             {'KERUSI_TAMAN': 'FAMILY_P1', 'TONG_SAMPAH': 'FAMILY_P1', 'DRINKING_FOUNTAIN': 'FAMILY_P1', 'PAPAN_TANDA': 'FAMILY_P2', 'BBQ_PIT': 'FAMILY_P2'}
PASS  PERABOT_OVERVIEW_NAVIGATION_MODEL_UNCHANGED                                             True
PASS  PERABOT_FAMILY_MAPPING_IN_PANEL                                                         2
PASS  BASE_STATE_FALSE_COMPLETION_TICKS                                                       0
PASS  FAMILY_LABELS_ON_LEARNER_CANVAS                                                         0
PASS  TECHNICAL_METADATA_ON_LEARNER_CANVAS                                                    0
PASS  LEARNER_SCREENS_WITH_ACTION_INSTRUCTION                                                 24
PASS  ACTION_INSTRUCTIONS_PRESENT_ON_CANVAS                                                   24
PASS  ACTION_INSTRUCTIONS_PRESENT_IN_SPOKEN_TRANSCRIPT                                        24
PASS  ACTION_INSTRUCTIONS_MISSING_FROM_NOTES                                                  0
PASS  ACTION_INSTRUCTION_CANVAS_VO_MISMATCHES                                                 0
PASS  SILENT_STATES_RECEIVING_NEW_VO                                                          0
PASS  REVIEW_ONLY_ANSWER_KEYS_INCLUDED_IN_VO                                                  0
PASS  TECHNICAL_CONTROLS_READ_AS_VO                                                           0
PASS  NOTES_CONTEXT_ACCIDENTALLY_MARKED_SPOKEN                                                0
PASS  CANVAS_SHAPES_OUTSIDE_STAGE                                                             0
PASS  COMPLETION_TICKS_NOT_MATCHING_PATH                                                      0
PASS  ORIGINAL_STAGE_4_CHECKS                                                                 132
PASS  ORACLE_SOURCE_IS_FROZEN_BARIAH_PPTX                                                     True
PASS  ORACLE_MODULE_IMPORTS_NO_GENERATOR                                                      True
PASS  ORACLE_PROMENADE_SUBJECT_MATCHES                                                        True
PASS  ORACLE_PROMENADE_HEADING_MATCHES                                                        True
PASS  ORACLE_S01_TITLE_MATCHES_FROZEN                                                         True
PASS  ORACLE_S01_NO_STANDALONE_TITLE_IN_FROZEN                                                0
PASS  ORACLE_S01_NO_STANDALONE_TITLE_IN_BUILD                                                 0
PASS  ORACLE_KLIK_WORDING_PRESENT                                                             True
PASS  ORACLE_KLIK_WORDING_UNMODIFIED                                                          True
PASS  TICK_IDENTITY_MISMATCHES                                                                0
PASS  TICK_IDENTITY_PAGES_EVALUATED                                                           True
PASS  TEXT_COVERED_BY_OPAQUE_SHAPE                                                            0
PASS  MODAL_OCCLUDED_SHAPES_EVALUATED                                                         16
PASS  MODAL_OCCLUDED_SHAPE_NAMES                                                              ['VisualDir']
PASS  MODAL_OCCLUSION_ON_NON_POPUP_PAGES                                                      0
PASS  NON_MODAL_OCCLUSIONS                                                                    []
PASS  ANSWER_KEYS_EVALUATED                                                                   5
PASS  ANSWER_KEYS_OUTSIDE_STAGE                                                               0
PASS  ANSWER_KEYS_COVERED                                                                     0
PASS  SHAPES_BEYOND_LEFT_EDGE                                                                 0
PASS  SHAPES_BEYOND_RIGHT_EDGE                                                                0
PASS  SHAPES_BEYOND_TOP_EDGE                                                                  0
PASS  SHAPES_BEYOND_BOTTOM_EDGE                                                               0
PASS  GEOMETRY_SHAPES_EVALUATED                                                               True
PASS  GEOMETRY_SHAPES_EVALUATED_INCLUDING_OFF_CANVAS                                          True
PASS  UNREGISTERED_OFF_CANVAS_EXEMPTIONS                                                      []
PASS  NOTES_BLOCKS_TOTAL_EVALUATED                                                            True
PASS  NOTES_BLOCKS_WITHOUT_TYPE                                                               0
PASS  NOTES_BLOCKS_WITHOUT_SPOKEN_FLAG                                                        0
PASS  NOTES_BLOCKS_WITH_UNKNOWN_TYPE                                                          0
PASS  NON_SPOKEN_BLOCKS_IN_SPOKEN_EXPORT                                                      0
PASS  SPOKEN_BLOCKS_MISSING_FROM_NOTES                                                        0
PASS  NOTES_PARAGRAPHS_RECONSTRUCTED                                                          True
PASS  SILENT_STATES_WITH_NOTES_BLOCKS                                                         0
PASS  SPOKEN_EXPORT_DRIVEN_BY_FLAG_NOT_ORDER                                                  True
PASS  SCREEN_LEVEL_CLICK_INSTRUCTIONS_EVALUATED                                               True
PASS  CONFIRMED_SCREEN_LEVEL_CLICK_MISMATCHES                                                 0
PASS  MICRO_CONTROL_SCOPE_SELF_RESOLVED                                                       0
PASS  REVIEW_ONLY_ANSWER_KEYS_IN_SPOKEN_VO                                                    0
PASS  INSTRUCTIONS_WITH_UNCLASSIFIED_AUTHORITY                                                0
PASS  BARIAH_DIRECT_FIELDS_WITH_MISSING_VALUE                                                 0
PASS  REQUIRED_VISUALS_EVALUATED                                                              True
PASS  REQUIRED_VISUALS_UNRESOLVED                                                             0
PASS  EVIDENCE_CONFLICTS_DISCLOSED__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT                    'SUPERSEDED'
PASS  ACTIVE_EVIDENCE_CONFLICTS                                                               0
PASS  EVIDENCE_CONFLICTS_IN_PRODUCTION_PANEL__SUPERSEDED_BY_SUPERSEDED_RULING_DISCLOSURE      'SUPERSEDED'
PASS  EVIDENCE_CONFLICTS_IN_PRODUCTION_PANEL                                                  0
PASS  SUPERSEDED_RULINGS_EVALUATED                                                            True
PASS  SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL                                        0
PASS  SUPERSEDED_DIRECTION_RENDERED_AS_ACTIVE                                                 0
PASS  PRIOR_SUITE_CHECKS                                                                      237
PASS  SCREENSHOT_EVIDENCE_FILES_FROZEN                                                        3
PASS  SCREENSHOT_EVIDENCE_CLASS                                                               ['BARIAH_DIRECT_SCREENSHOT']
PASS  SCREENSHOT_EVIDENCE_HASHES_MATCH_ON_DISK                                                ['7e59a0e882c1de063f9e86ee16ea1ed079ad6bdbf95ce4998d76636b943bbff0', '936b78c270274874bfa4921a35205e4ca1d679959ebf6f1880e7c76e6f890ab7', 'feb29e86228b7f240379b9830bbd59f3e30db2fae03389a68e1ba1bd32ef867b']
PASS  SCREENSHOT_ORACLE_IMPORTS_NO_GENERATOR                                                  True
PASS  ORACLE_POLICY_EXAMPLES_REQUIRE_VISUAL                                                   True
PASS  ORACLE_POLICY_SPEC_POPUP_EXCEPTED                                                       True
PASS  ORACLE_POLICY_CARRIES_NO_QUALIFIER                                                      None
PASS  ORACLE_POLICY_SUBTYPES_EVALUATED                                                        ['EXAMPLE_POPUP', 'EXAMPLE_SCREEN', 'EXAMPLE_SELECTION_SCREEN', 'SPECIFICATION_POPUP']
PASS  ORACLE_POLICY_SUBTYPE_REQUIREMENT_MISMATCHES                                            0
PASS  ORACLE_POLICY_EXAMPLE_SELECTION_IS_REQUIRED                                             'REQUIRED'
PASS  ORACLE_POLICY_EXAMPLE_DETAIL_IS_REQUIRED                                                'REQUIRED'
PASS  SHOT_S01_DISPLAY_TITLE_MATCHES                                                          True
PASS  SHOT_S01_STANDALONE_TITLE_REMOVED                                                       0
PASS  SHOT_S01_CANVAS_LINES_PRESENT                                                           []
PASS  SHOT_S01_VISUAL_SHAPE_PRESENT                                                           True
PASS  SHOT_S01_VISUAL_HEADING_MATCHES                                                         True
PASS  SHOT_S01_VISUAL_DIRECTION_MATCHES                                                       True
PASS  SHOT_S01_BUTTON_MATCHES                                                                 True
PASS  SHOT_S01_SPOKEN_BLOCK_COUNT                                                             3
PASS  SHOT_S01_SPOKEN_BLOCKS_EXACT__SUPERSEDED_BY_D3_PUNCTUATION_RULING                       'SUPERSEDED'
PASS  SHOT_S01_SPOKEN_BLOCKS_EXACT                                                            ['PL06: Pengurusan Operasi Pembinaan Landskap', 'Topik 3 Bahagian 2: Komponen Landskap', 'Klik butang “Mula” untuk memulakan pembelajaran.']
PASS  SHOT_S01_REMOVED_SENTENCE_GONE                                                          False
PASS  SHOT_S01_PACKAGE_NOTES_EXACT__SUPERSEDED_BY_D3_PUNCTUATION_RULING                       'SUPERSEDED'
PASS  SHOT_S01_PACKAGE_NOTES_EXACT                                                            ['PL06: Pengurusan Operasi Pembinaan Landskap', 'Topik 3 Bahagian 2: Komponen Landskap', 'Klik butang “Mula” untuk memulakan pembelajaran.']
PASS  SHOT_S01_SUPERSEDED_SPOKEN_LINES_GONE                                                   []
PASS  SHOT_PERSISIR_SCREEN_TITLE_MATCHES                                                      True
PASS  SHOT_PERSISIR_COMPONENT_HEADING_MATCHES                                                 True
PASS  SHOT_PERSISIR_ACTIVE_DIRECTION_RENDERED                                                 True
PASS  SHOT_PERSISIR_SUPERSEDED_DIRECTION_NOT_ON_CANVAS                                        False
PASS  SHOT_PERSISIR_SUPERSESSION_DISCLOSED_IN_PANEL                                           True
PASS  SHOT_PERSISIR_SUPERSEDED_STATUS_RECORDED                                                'SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT'
PASS  SHOT_BOARDWALK_EXAMPLE_DIRECTION_RETAINED                                               True
PASS  ORACLE_PROPAGATION_IS_QUALIFIED                                                         True
PASS  ORACLE_DOES_NOT_AUTHORISE_OTHER_COMPONENT_MAIN_CONTENT                                  False
PASS  COMPONENT_MAINS_EVALUATED                                                               9
PASS  COMPONENT_MAINS_RESOLVED_BY_DIRECT_AUTHORITY__SUPERSEDED_BY_D2_COMPONENT_MAIN_RULING    'SUPERSEDED'
PASS  COMPONENT_MAINS_PENDING_HUMAN__SUPERSEDED_BY_D2_COMPONENT_MAIN_RULING                   'SUPERSEDED'
PASS  COMPONENT_MAIN_RESOLVED_WITHOUT_BARIAH_AUTHORITY__SUPERSEDED_BY_AUTHORITY_SPLIT         'SUPERSEDED'
PASS  COMPONENT_MAIN_REQUIREMENT_WITHOUT_BARIAH_AUTHORITY                                     0
PASS  COMPONENT_MAIN_DIRECTION_AUTHORITIES                                                    ['BARIAH_DIRECT', 'SOURCE_ATTESTED_COMPONENT_VISUAL']
PASS  PENDING_HUMAN_ITEMS_CLOSED_BY_CC                                                        0
PASS  QUIZ_REVIEW_STATE_PAGES_EVALUATED                                                       1
PASS  QUIZ_REVIEW_STATE_QUESTIONS_EXPECTED                                                    5
PASS  QUIZ_REVIEW_STATE_QUESTIONS_MISSING                                                     0
PASS  QUIZ_REVIEW_STATE_ANSWERS_MISSING_OR_WRONG                                              0
PASS  STAGE_4_2B_SUITE_CHECKS                                                                 288
PASS  CARDINALITY_EVIDENCE_FROZEN                                                             1
PASS  CARDINALITY_EVIDENCE_HASH                                                               'f46c2a371b93ebadc6e4bf99c619bf52621d7bc29421ebd36205f6ed6ec5ef64'
PASS  CARDINALITY_EVIDENCE_CLASS                                                              'BARIAH_DIRECT_SCREENSHOT'
PASS  CARDINALITY_ORACLE_IMPORTS_NO_GENERATOR                                                 True
PASS  CARDINALITY_SUMMARY_IS_NOT_ORACLE                                                       False
PASS  COMPONENT_MAIN_SCREENS_IDENTIFIED                                                       9
PASS  COMPONENT_MAIN_STATE_PAGES_EVALUATED                                                    22
PASS  COMPONENT_MAIN_OVERVIEWS_RENDERED                                                       9
PASS  PAPAN_TANDA_OVERVIEW_VISUAL_COUNT                                                       2
PASS  PAPAN_TANDA_OVERVIEW_SUBJECTS_EXACT                                                     ['PapanTandaInformasi', 'PapanTandaPenunjukArah']
PASS  BBQ_PIT_OVERVIEW_VISUAL_COUNT                                                           1
PASS  BBQ_PIT_OVERVIEW_SUBJECT_NOT_DUPLICATED                                                 1
PASS  INFORMASI_INTERPRETATIF_GLOBAL_RULE_CREATED                                             False
PASS  OVERVIEW_CARDINALITY_MAPPING_MISMATCHES                                                 0
PASS  UNAUTHORISED_OVERVIEW_SUBJECTS                                                          0
PASS  INVENTED_OVERVIEW_SUBJECTS                                                              0
PASS  OVERVIEW_COUNTS_BY_COMPONENT                                                            {'BBQ_PIT': 1, 'DRINKING_FOUNTAIN': 2, 'KEMUDAHAN_AWAM': 3, 'KERUSI_TAMAN': 3, 'PAPAN_TANDA': 2, 'STRUKTUR_PERSISIR_AIR': 5, 'STRUKTUR_TEDUHAN': 5, 'TONG_SAMPAH': 3, 'WATER_FEATURE': 3}
PASS  GENERIC_OVERVIEW_FALLBACKS                                                              0
PASS  UNIVERSAL_FIXED_CARD_COUNT                                                              False
PASS  MINIMUM_OVERVIEW_CARDINALITY                                                            1
PASS  COMPONENT_VISUAL_OVERLAPS_OVERVIEW_HEADING                                              0
PASS  BASE_TO_ALL_VIEWED_OVERVIEW_IDENTITY_MISMATCHES                                         0
PASS  BASE_TO_RETURN_OVERVIEW_IDENTITY_MISMATCHES                                             0
PASS  PERSISTENCE_TARGET_PAGES_MISSING_VISUALS                                                0
PASS  PERSISTENCE_POPULATION_PINNED_BY_LEARNER_SCREEN_ID                                      True
PASS  EXAMPLE_INFORMATION_POPUPS_EVALUATED                                                    16
PASS  SPECIFICATION_POPUPS_EVALUATED                                                          30
PASS  EXAMPLE_INFORMATION_POPUPS_WITH_FOCUSED_VISUAL                                          16
PASS  EXAMPLE_INFORMATION_POPUPS_WITHOUT_FOCUSED_VISUAL                                       0
PASS  POPUPS_USING_OVERVIEW_LAYOUT_INSTEAD_OF_FOCUSED_LAYOUT                                  0
PASS  FOCUSED_POPUP_PANEL_LARGER_THAN_OVERVIEW_CARD                                           True
PASS  SPECIFICATION_POPUPS_WITH_FORCED_VISUAL_PANEL                                           0
PASS  FOCUSED_POPUP_SUBJECT_MISMATCHES                                                        0
PASS  SLIDE5_NEW_LEARNER_SCREEN                                                               29
PASS  SLIDE5_ASAS_PEMBINAAN_HEADING_EXACT                                                     True
PASS  SLIDE5_BULLET_1_EXACT                                                                   True
PASS  SLIDE5_BULLET_2_EXACT                                                                   True
PASS  SLIDE5_BULLET_TRAILING_PERIODS                                                          0
PASS  SLIDE5_CANVAS_VO_MISMATCHES                                                             0
PASS  SLIDE5_VO_DERIVED_FROM_CONTROLLED_FIELD                                                 True
PASS  SLIDE5_VO_IN_PACKAGE_NOTES                                                              True
PASS  SLIDE5_BULLETS_IN_PACKAGE_NOTES                                                         0
PASS  QUIZ_QUESTION_PAGES_EVALUATED                                                           5
PASS  QUIZ_CORRECT_FEEDBACK_EXACT_MATCH                                                       True
PASS  QUIZ_INCORRECT_FEEDBACK_EXACT_MATCH                                                     True
PASS  QUIZ_RATIONALE_IN_SPEAKER_NOTES                                                         0
PASS  QUIZ_RATIONALE_IN_SPOKEN_EXPORT                                                         0
PASS  QUIZ_RATIONALE_RETAINED_IN_PRODUCTION_PANEL                                             5
PASS  QUIZ_FEEDBACK_IN_SPOKEN_EXPORT                                                          0
PASS  MICRO_CONTROL_INSTRUCTIONS_IN_SPOKEN_VO                                                 0
PASS  MICRO_CONTROL_INSTRUCTIONS_IN_PACKAGE_NOTES                                             0
PASS  MICRO_CONTROL_BEHAVIOUR_METADATA_MISSING                                                0
PASS  S01_SPOKEN_BLOCK_COUNT                                                                  3
PASS  S01_LINE_1_TRAILING_PERIOD                                                              False
PASS  S01_LINE_2_TRAILING_PERIOD                                                              False
PASS  S01_INTERACTION_LINE_TRAILING_PERIOD                                                    True
PASS  S01_LINE_1_EXACT                                                                        'PL06: Pengurusan Operasi Pembinaan Landskap'
PASS  S01_LINE_2_EXACT                                                                        'Topik 3 Bahagian 2: Komponen Landskap'
PASS  S01_LINE_3_EXACT                                                                        'Klik butang “Mula” untuk memulakan pembelajaran.'
PASS  TAMAT_LEARNER_COPY_EXACT_MATCH                                                          True
PASS  TAMAT_NAVIGATION_OUTCOME_RECORDED                                                       True
PASS  TAMAT_LEARNER_ACTION_RECORDED                                                           True
PASS  TAMAT_AUTOMATIC_ROUTE_CLAIM                                                             False
PASS  TAMAT_LMS_SHELL_NEXT_CLAIM                                                              False
PASS  TAMAT_MECHANISM_ON_LEARNER_CANVAS                                                       0
PASS  CAST_PAIR_APPROVED                                                                      True
PASS  B02_CAST_PAIR_STATUS                                                                    ['Alya', 'Encik Rahman']
PASS  CAST_REUSE_IS_CONDITIONAL                                                               True
PASS  HILMI_BINDING_UNCHANGED                                                                 ['SCR_S03']
PASS  CAST_NAMES_ON_UNRELATED_SCREENS                                                         0
PASS  UNAUTHORISED_CAST_INSERTIONS                                                            0
PASS  CONTEXT_FREE_CAST_REUSE                                                                 0
PASS  UNRATIFIED_PL06_PRONUNCIATION_IMPLEMENTED                                               0
PASS  SOURCE_GOVERNANCE_COMPLETE                                                              False
PASS  STAGE_4_2C_SUITE_CHECKS                                                                 334
PASS  RUN_MANIFEST_PRESENT                                                                    True
PASS  PANEL_VERSION_EQUALS_RUN_MANIFEST_VERSION                                               True
PASS  PANEL_VERSION_MANIFEST_MISMATCHES                                                       0
PASS  PANEL_STATUS_EQUALS_ACTIVE_PACKAGE_STATUS                                               True
PASS  PANEL_STATUS_MANIFEST_MISMATCHES                                                        0
PASS  MANIFEST_DECK_FILENAME_MATCHES_ARTIFACT                                                 'K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4_1.pptx'
PASS  STALE_RELEASE_TOKENS_ANYWHERE_IN_PANEL                                                  0
PASS  STALE_RELEASE_TOKENS_IN_NOTES                                                           0
PASS  SUPERSEDED_VERSION_LINES_IN_PACKAGE                                                     0
PASS  CHECKLIST_PRESENT                                                                       True
PASS  CHECKLIST_NAMES_ACTIVE_DECK                                                             True
PASS  CHECKLIST_CARRIES_FULL_STATUS_CONTRACT                                                  True
PASS  CHECKLIST_FREE_OF_STALE_STATUS_CLAIMS                                                   0
PASS  CHECKLIST_STALE_TOKENS_ONLY_IN_QUOTED_BLOCKS                                            True
PASS  QA_REPORT_PRESENT                                                                       True
PASS  QA_REPORT_NAMES_ACTIVE_DECK                                                             True
PASS  QA_REPORT_CARRIES_FULL_STATUS_CONTRACT                                                  True
PASS  QA_REPORT_FREE_OF_STALE_STATUS_CLAIMS                                                   0
PASS  QA_REPORT_STALE_TOKENS_ONLY_IN_QUOTED_BLOCKS                                            True
PASS  DEFECT_RECORD_PRESENT                                                                   True
PASS  DEFECT_RECORD_ID                                                                        True
PASS  DEFECT_RECORD_CARRIES_VERBATIM_STALE_STRINGS                                            []
PASS  COMPONENT_MAIN_LEARNER_SCREENS                                                          9
PASS  COMPONENT_MAIN_BOUND_PAGES_EVALUATED                                                    22
PASS  COMPONENT_MAIN_PAGES                                                                    9
PASS  COMPONENT_MAIN_PAGES_COVER_EVERY_SCREEN                                                 ['SCR_BBQ_PIT_MAIN', 'SCR_DRINKING_FOUNTAIN_MAIN', 'SCR_KEMUDAHAN_AWAM_MAIN', 'SCR_KERUSI_TAMAN_MAIN', 'SCR_PAPAN_TANDA_MAIN', 'SCR_STRUKTUR_PERSISIR_AIR_MAIN', 'SCR_STRUKTUR_TEDUHAN_MAIN', 'SCR_TONG_SAMPAH_MAIN', 'SCR_WATER_FEATURE_MAIN']
PASS  COMPONENT_MAIN_VISUAL_REQUIREMENT_REQUIRED                                              9
PASS  COMPONENT_MAIN_REQUIREMENT_AUTHORITY                                                    ['BARIAH_DIRECT_SCREENSHOT']
PASS  COMPONENT_MAIN_TREATMENT                                                                ['SOURCE_BOUND_OVERVIEW']
PASS  COMPONENT_MAIN_TREATMENT_AUTHORITY                                                      ['BARIAH_DIRECT_SCREENSHOT']
PASS  COMPONENT_MAIN_MAPPING_STATUS_RESOLVED                                                  9
PASS  COMPONENT_MAIN_MAPPING_COMPLETE                                                         9
PASS  COMPONENT_MAIN_STATUS_RESOLVED                                                          9
PASS  COMPONENT_MAIN_PENDING_HUMAN                                                            0
PASS  COMPONENT_MAIN_PROVISIONAL_VISUAL_PROPOSALS                                             0
PASS  COMPONENT_MAIN_ACTIVE_VISUAL_GOVERNANCE_CURRENT                                         True
PASS  COMPONENT_MAIN_STALE_GOVERNANCE_STRINGS_IN_VISUAL_BLOCK                                 0
PASS  UNAUTHORISED_SUBJECT_AUTHORITY_PROMOTIONS                                               0
PASS  SUBJECTS_DIRECTLY_NAMED_BY_BARIAH                                                       2
PASS  COMPONENT_MAIN_SUBJECT_PROVENANCE_ON_PAGE                                               9
PASS  COMPONENT_MAIN_SUBJECT_COUNT_MATCHES_MAPPING                                            0
PASS  GEOMETRY_EXEMPTION_REGISTRY_PRESENT                                                     True
PASS  GEOMETRY_EXEMPTION_REGISTRY_MATCHES_CODE                                                [{'exemption_id': 'GEX-001', 'shape_name': 'Title 1', 'requires_placeholder': True, 'ph_type': 'title', 'x': 0.0, 'y': -0.6311001749781278, 'w': 13.333300524934383, 'h': 0.5722003499562555, 'edges_exempted': ['top'], 'page_population': 'ALL_REVIEW_PAGES', 'learner_facing': False, 'visible_in_slide_show': False, 'purpose': "PowerPoint slide-title identity: outline pane, accessibility name, slide navigator and search. Off the top edge so it never paints on the learner canvas while remaining the slide's programmatic title.", 'why_not_deleted': 'Deleting it would leave every slide untitled in the outline pane and in the accessibility tree. It is not proven unnecessary.', 'enforcement_gate': 'OFF_CANVAS_PLACEHOLDER_EXEMPTION_REGISTERED', 'registered_at': 'Stage 4.2E-C'}, {'exemption_id': 'GEX-002', 'shape_name': 'ProdPanel', 'requires_placeholder': False, 'ph_type': None, 'x': -6.9, 'y': 0.0, 'w': 6.6, 'h': 7.5, 'edges_exempted': ['left'], 'page_population': 'ALL_REVIEW_PAGES', 'learner_facing': False, 'visible_in_slide_show': False, 'purpose': 'Review-only production metadata panel. Deliberately parked left of the stage so a reviewer reads it in Normal view and a learner never sees it.', 'why_not_deleted': 'It is the review surface this whole storyboard exists to carry.', 'enforcement_gate': 'OFF_CANVAS_PRODUCTION_PANEL_EXEMPTION_REGISTERED', 'registered_at': 'Stage 4.2E-C'}]
PASS  OFF_CANVAS_PLACEHOLDER_EXEMPTION_REGISTERED                                             True
PASS  OFF_CANVAS_PRODUCTION_PANEL_EXEMPTION_REGISTERED                                        True
PASS  EXEMPTED_SHAPES_EVALUATED                                                               200
PASS  EXEMPTED_SHAPE_NAMES                                                                    ['ProdPanel', 'Title 1']
PASS  TITLE_PLACEHOLDER_IS_A_REAL_PLACEHOLDER                                                 True
PASS  TITLE_PLACEHOLDER_PAGE_POPULATION                                                       100
PASS  ORDINARY_OFF_CANVAS_SHAPES_ALLOWED                                                      0
PASS  DUPLICATE_GATE_IDS                                                                      []
PASS  STAGE_4_2E_B_SUITE_CHECKS                                                               409

441/441 active gates PASS  ·  20 supersession markers  ·  461 emitted records
```
