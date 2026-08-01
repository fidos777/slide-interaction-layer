# STORYBOARD_QA_REPORT — K5 PL06 T03 B02 v0.4.1

```
REVIEW_READY · BARIAH_LATEST_FEEDBACK_IMPLEMENTED · PENDING_TARGETED_CONFIRMATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED

ORIGINAL_STAGE_4_CHECKS = 105 · PASS = 105 · FAIL = 0
EXPANDED_CHECKS = 188 · PASS = 188 · FAIL = 0
REVIEW_PAGES = 100 · LEARNER_SCREENS = 29 · RUNTIME_STATES = 100 · INTERACTION_ITEMS = 54
SOURCE_ROWS = 26 · SOURCE_ASSETS = 14 · SOURCE_ROWS_CREATED = 0 · COMPONENTS = 9
SLIDES_MANUALLY_PATCHED = 0 · V0_3_GENERATOR_FILES_CHANGED = 0
```

Deck `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_1.pptx` — 453,859 B,
`sha256 247eadb10bde4e7f227c6df947b1821c55faad140b212465ae774bd2c932f59a`. The v0.4 deck is retained and marked `SUPERSEDED_BY_v0_4_1`.

Every Stage 4 check still runs. Nothing was removed or weakened; five Tamat checks were replaced
1:1 because Bariah superseded the ruling they encoded, and one over-broad popup-visual gate was
replaced by subtype-aware gates because Bariah's clarification made it wrong.

---

# 1. Visual directions and subtype policy

```
PASS  GENERIC_ONE_ITEM_PAPAN_TANDA_SCREEN                  0
PASS  GENERIC_ONE_ITEM_BBQ_PIT_SCREEN                      0
PASS  S01_SPOKEN_ELEMENTS                                  4
PASS  PROMENADE_PRESENT                                    True
PASS  VISUAL_DIRECTIONS_AUDITED                            26
PASS  VISUAL_DIRECTIONS_PENDING                            0
PASS  GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES            0
PASS  SOURCE_ROW_VISUAL_DIRECTIONS_MISSING                 0
PASS  POPUP_PAGES                                          46
PASS  REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL               0
PASS  REQUIRED_VISUAL_POPUPS_WITHOUT_VISUAL                0
PASS  SPECIFICATION_POPUPS_TOTAL                           30
PASS  SPECIFICATION_POPUPS_REQUIRING_VISUAL                0
PASS  SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL   0
PASS  SPECIFICATION_POPUPS_WITH_FORCED_GENERIC_VISUAL      0
PASS  NOT_REQUIRED_VISUAL_POPUPS_FORCED_TO_HAVE_VISUAL     0
PASS  CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED           0
PASS  EXAMPLE_POPUPS_TOTAL                                 16
PASS  EXAMPLE_POPUPS_WITH_SPECIFIC_VISUAL                  16
PASS  EXAMPLE_POPUPS_WITHOUT_VISUAL                        0
PASS  EXAMPLE_POPUPS_WITH_GENERIC_FALLBACK                 0
PASS  EXAMPLE_SCREENS_TOTAL                                12
PASS  EXAMPLE_SCREENS_WITH_SPECIFIC_VISUAL                 12
PASS  EXAMPLE_SCREENS_WITHOUT_VISUAL                       0
PASS  COMPONENT_MAIN_SCREENS_WITH_SPECIFIC_VISUAL          9
PASS  S01_DISPLAY_TITLE                                    True
PASS  S01_DUPLICATE_STANDALONE_COMPONENT_TITLE             0
PASS  S01_SPECIFIC_VISUAL_DIRECTION_PRESENT                True
PASS  REQUIRED_VISUAL_PANEL_MISSING                        0
PASS  VISUAL_PANEL_HEADING_MISSING                         0
PASS  VISUAL_PANEL_CONTENT_OVERRUN                         0
PASS  VISUAL_PANEL_CLOSE_ICON_COLLISION                    0
PASS  VISUAL_DIRECTION_WRONG_SOURCE_BINDING                0
PASS  VISUAL_DIRECTION_WRONG_COMPONENT_BINDING             0
PASS  VISUAL_DIRECTIONS_WITHOUT_SOURCE_OR_BARIAH_BINDING   0
PASS  FAMILY_S_GENERIC_VISUAL_FALLBACKS                    0
PASS  FAMILY_P1_GENERIC_VISUAL_FALLBACKS                   0
PASS  FAMILY_P2_GENERIC_VISUAL_FALLBACKS                   0
PASS  FAMILY_S_POPUPS_WITH_SPECIFIC_VISUAL_DIRECTION       16
PASS  FAMILY_S_VISUAL_PANEL_MISSING                        0
PASS  PROMENADE_SPECIFIC_VISUAL_DIRECTION                  True
PASS  PROMENADE_GENERIC_FALLBACK_GONE                      False
```

# 2. Speaker Notes rich text

```
PASS  NOTES_GLOSSARY_OCCURRENCES_FOUND                     40
PASS  NOTES_GLOSSARY_OCCURRENCES_ITALICISED                40
PASS  NOTES_GLOSSARY_ITALIC_MISSES                         0
PASS  NOTES_FALSE_ITALICS_ON_TECHNICAL_IDS                 0
PASS  NOTES_MARKDOWN_ITALIC_MARKERS                        0
PASS  NOTES_RICH_TEXT_PACKAGE_ROUNDTRIP_FAILURES           0
PASS  NOTES_ITALIC_RUNS_IN_PACKAGE                         True
PASS  CANVAS_GLOSSARY_ITALIC_MISSES                        0
PASS  GLOSSARY_IS_SINGLE_SOURCE                            True
PASS  NOTES_CONTEXT_ACCIDENTALLY_MARKED_SPOKEN             0
```

# 3. Quiz answer key

```
PASS  QUIZ_QUESTIONS_WITHOUT_BOTH_FEEDBACK_VARIANTS        0
PASS  QUIZ_QUESTIONS                                       5
PASS  QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY            5
PASS  QUIZ_REVIEW_PAGES_WITHOUT_ANSWER_KEY                 0
PASS  MCQ_ANSWER_KEYS_WITH_LETTER_AND_TEXT                 4
PASS  MULTIPLE_RESPONSE_ANSWER_KEY_USES_FULL_OPTION_TEXT   True
PASS  ANSWER_KEY_SOURCE_MISMATCH                           0
PASS  MULTIPLE_RESPONSE_LEARNER_OPTIONS_WITH_LETTER_LABELS 0
PASS  ANSWER_KEY_LABELLED_AS_REVIEWER_INFO                 0
PASS  ANSWER_KEY_VISIBLE_DURING_LEARNER_PRE_SUBMISSION_STATE 0
PASS  ANSWER_KEY_READ_IN_VO                                0
```

# 4. Tamat

```
PASS  TAMAT_COPY_STATUS                                    'CONFIRMED_BARIAH'
PASS  TAMAT_LOGICAL_DESTINATION                            'NEXT_BAHAGIAN'
PASS  TAMAT_PHYSICAL_NAVIGATION_STATUS                     'PENDING_FIRDAUS_OR_LMS_CONFIRMATION'
PASS  TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT               False
PASS  TAMAT_UNVERIFIED_PHYSICAL_NAVIGATION_CLAIM           0
PASS  TAMAT_NO_CANVAS_NEXT_BUTTON                          0
PASS  TAMAT_TITLE_MATCHES_BARIAH_EXEMPLAR                  True
PASS  TAMAT_LEARNER_INSTRUCTION_MATCHES_BARIAH_EXEMPLAR    True
PASS  TAMAT_HIERARCHY_COMPLETE                             6
PASS  TAMAT_SPOKEN_TRANSCRIPT_MATCHES                      True
PASS  TAMAT_NON_SPOKEN_CONTEXT_RETAINED                    True
```

# 5. Perabot gateway and metadata denylist

```
PASS  PERABOT_OVERVIEW_VISUAL_CARDS                        5
PASS  PERABOT_COMPONENT_NAMES_PRESENT                      5
PASS  PERABOT_COMPONENTS_WITH_VISUAL_DIRECTION             5
PASS  PERABOT_COMPONENT_NAMES_CORRECT                      ['BBQ Pit', 'Drinking Fountain', 'Kerusi Taman', 'Papan Tanda', 'Tong Sampah']
PASS  PERABOT_OVERVIEW_INTERNAL_MAPPING_UNCHANGED          {'KERUSI_TAMAN': 'FAMILY_P1', 'TONG_SAMPAH': 'FAMILY_P1', 'DRINKING_FOUNTAIN': 'FAMILY_P1', 'PAPAN_TANDA': 'FAMILY_P2', 'BBQ_PIT': 'FAMILY_P2'}
PASS  PERABOT_OVERVIEW_NAVIGATION_MODEL_UNCHANGED          True
PASS  PERABOT_FAMILY_MAPPING_IN_PANEL                      2
PASS  BASE_STATE_FALSE_COMPLETION_TICKS                    0
PASS  FAMILY_LABELS_ON_LEARNER_CANVAS                      0
PASS  TECHNICAL_METADATA_ON_LEARNER_CANVAS                 0
```

# 6. Instruction parity

```
PASS  LEARNER_SCREENS_WITH_ACTION_INSTRUCTION              25
PASS  ACTION_INSTRUCTIONS_PRESENT_ON_CANVAS                25
PASS  ACTION_INSTRUCTIONS_PRESENT_IN_SPOKEN_TRANSCRIPT     25
PASS  ACTION_INSTRUCTIONS_MISSING_FROM_NOTES               0
PASS  ACTION_INSTRUCTION_CANVAS_VO_MISMATCHES              0
PASS  SILENT_STATES_RECEIVING_NEW_VO                       0
PASS  REVIEW_ONLY_ANSWER_KEYS_INCLUDED_IN_VO               0
PASS  TECHNICAL_CONTROLS_READ_AS_VO                        0
PASS  NOTES_CONTEXT_ACCIDENTALLY_MARKED_SPOKEN             0
```

# 7. Layout

```
TEXT_OVERFLOW = 0        LINE_CLIPPING = 0        PANEL_CONTENT_OVERRUN = 0
OFF_CANVAS_LEAKAGE = 0   UNINTENDED_NON_MODAL_OVERLAPS = 0
CLOSE_ICON_TITLE_COLLISIONS = 0   VISUAL_PANEL_CLOSE_ICON_COLLISION = 0
CANVAS_SHAPES_OUTSIDE_STAGE = 0   VISUAL_PANEL_CONTENT_OVERRUN = 0
```

`CANVAS_SHAPES_OUTSIDE_STAGE` is new. The Stage 4 suite classified shapes by the left edge only,
so a card overflowing the bottom of the stage was invisible to it. It now tests all four edges,
and it caught a second defect immediately after the one that prompted it.

# 8. Full Stage 4 suite, re-run unchanged

```
PASS  SOURCE_ROWS_EXPECTED                                 26
PASS  SOURCE_ROWS_ACCOUNTED                                26
PASS  SOURCE_ROWS_CREATED                                  0
PASS  DUPLICATE_SOURCE_ROW_UID                             0
PASS  SOURCE_ASSETS_EXPECTED                               14
PASS  SOURCE_ASSETS_ACCOUNTED                              14
PASS  ORPHAN_SOURCE_ASSETS                                 0
PASS  INTERACTION_ITEMS_WITHOUT_SOURCE_BINDING             0
PASS  INTERACTION_ITEMS_WITHOUT_LOCATOR                    0
PASS  INTERACTION_ITEMS_WITHOUT_FAMILY                     0
PASS  STATES_WITHOUT_DECISION_ID                           0
PASS  SOURCE_ROWS_WITHOUT_A_REVIEW_PAGE                    0
PASS  FAMILY_S_COMPONENTS                                  4
PASS  FAMILY_P1_COMPONENTS                                 3
PASS  FAMILY_P2_COMPONENTS                                 2
PASS  UNKNOWN_COMPONENT_FAMILY                             0
PASS  COMPONENTS_GENERATED                                 9
PASS  PAPAN_TANDA_SPEC_CATEGORIES                          4
PASS  BBQ_PIT_SPEC_CATEGORIES                              4
PASS  BBQ_PIT_CATEGORY_LABELS                              ['Bahan Pembinaan', 'Dimensi', 'Gril', 'Keselamatan']
PASS  GENERIC_ONE_ITEM_PAPAN_TANDA_SCREEN                  0
PASS  GENERIC_ONE_ITEM_BBQ_PIT_SCREEN                      0
PASS  PAPAN_TANDA_SOURCE_ROWS_CREATED_BY_SPLIT             0
PASS  BBQ_PIT_SOURCE_ROWS_CREATED_BY_SPLIT                 0
PASS  CARDS_DROPPED_OR_INVENTED                            0
PASS  RUNTIME_STATES_WITHOUT_PARENT                        0
PASS  RETURN_TARGET_MISSING                                0
PASS  POPUP_PARENT_IS_POPUP                                0
PASS  UNKNOWN_CONTROL_TYPE                                 0
PASS  REVIEW_PAGES_EQUAL_RUNTIME_STATES                    100
PASS  FAMILY_S_PREMATURE_KEMBALI                           0
PASS  FAMILY_P1_FALSE_SIBLING_TICKS                        0
PASS  FAMILY_P1_PREMATURE_EXAMPLE_COMPLETION               0
PASS  FAMILY_P2_PREMATURE_COMPONENT_COMPLETION             0
PASS  DUPLICATE_CUSTOM_SETERUSNYA                          0
PASS  TEXT_TUTUP_BUTTON                                    0
PASS  POPUPS_WITHOUT_CLOSE_ICON                            0
PASS  S02_CAST                                             ['Alya', 'Encik Rahman']
PASS  S02_CAST_IN_TRANSCRIPT                               True
PASS  S02_MS2680_LEARNER_CLAIMS                            0
PASS  S02_MS2680_IN_PRODUCTION_PANEL                       True
PASS  S02_GENERIC_ROLE_NAMES_AS_FINAL_NAMES                0
PASS  S03_NARRATOR                                         ['Hilmi']
PASS  S03_HILMI_REINTRODUCED_AS_NEW                        False
PASS  S03_MIND_MAP_DIRECTION_PRESENT                       True
PASS  S03_BOTH_GROUPS_PRESENT                              True
PASS  S03_ALL_NINE_COMPONENTS                              9
PASS  HILMI_LABEL_OUTSIDE_S03                              0
PASS  RUMUSAN_FORBIDDEN_LABELS_DISPLAYED                   0
PASS  CONTENT_SLIDES_WITHOUT_NOTES                         0
PASS  S02_ONWARDS_PL_TITLE_REANNOUNCEMENTS                 0
PASS  S02_ONWARDS_TOPIC_TITLE_REANNOUNCEMENTS              0
PASS  CONTEXT_BLOCK_MISSING_ON_CONTENT_SLIDES              0
PASS  SILENT_STATES_WITH_NONEMPTY_NOTES                    0
PASS  TECHNICAL_IDS_IN_FINAL_NOTES                         0
PASS  BARIAH_REVIEW_ANNOTATIONS_IN_DECK                    0
PASS  BARIAH_ANNOTATIONS_IN_NOTES                          0
PASS  V0_3_TOKENS_IN_PANEL                                 0
PASS  PACKAGE_TOKEN_REVIEW_READY                           True
PASS  PACKAGE_TOKEN_BARIAH_FEEDBACK_IMPLEMENTED            True
PASS  PACKAGE_TOKEN_PENDING_TARGETED_CONFIRMATION          True
PASS  PACKAGE_TOKEN_NOT_FOR_MMD_BUILD                      True
PASS  PACKAGE_TOKEN_MULTIMEDIA_NOT_PRODUCED                True
PASS  FORBIDDEN_TOKEN_PRODUCTION_APPROVED                  0
PASS  FORBIDDEN_TOKEN_CANONICAL_FREEZE                     0
PASS  FORBIDDEN_TOKEN_MMD_BUILD_READY                      0
PASS  FORBIDDEN_TOKEN_SOURCE_INTEGRITY_FULLY_VERIFIED      0
PASS  APPROVED_TERMS_NOT_ITALICISED                        0
PASS  APPROVED_TERMS_ITALICISED_AT_LEAST                   True
PASS  PRODUCTION_IDS_ITALICISED                            0
PASS  BBQ_PIT_LOWERCASE_P_ON_CANVAS                        0
PASS  WPC_NORMALISATION_PRESENT                            True
PASS  PROMENADE_PRESENT                                    True
PASS  PAGES_WITHOUT_PRODUCTION_PANEL                       0
PASS  PRODUCTION_PANEL_ON_CANVAS                           0
PASS  PRODUCTION_PANEL_MISSING_FIELD                       0
PASS  ORIGINAL_STAGE_4_CHECKS                              105
```

---

# 9. PENDING_HUMAN — none marked PASS

Family P1 density · Family P2 category treatment · close-icon clarity · Alya / Encik Rahman visual
treatment · S01 VO naturalness · S03 reflection wording · Rumusan visual treatment · quiz
presentation · Tamat visual treatment · Microsoft PowerPoint font wrapping.

Open decisions unchanged: **U-01** MS2680 · **U-02b** Pengurus Projek name · **U-03** physical LMS
navigation · **U-05** quiz rationale placement · `B02-CAIR-INT-001`.
