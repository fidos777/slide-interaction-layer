# STORYBOARD_QA_REPORT — K5 PL06 T03 B02 v0.4

```
REVIEW_READY · BARIAH_FEEDBACK_IMPLEMENTED · PENDING_TARGETED_CONFIRMATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED

CHECKABLE = 105 · PASS = 105 · FAIL = 0
REVIEW_PAGES = 100 · LEARNER_SCREENS = 29 · RUNTIME_STATES = 100
INTERACTION_ITEMS = 54 (S 16 · P1 30 · P2 8)
SOURCE_ROWS = 26 · SOURCE_ASSETS = 14 · SOURCE_ROWS_CREATED = 0
COMPONENTS = 9 (S 4 · P1 3 · P2 2)
```

Deck: `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4.pptx` — 439,329 B,
`sha256 8cb0abe5cb393f3bafd613220683939faa8a3a7014547af08b9392fbc540d108`.

**105 checkable gates all pass. 15 items are PENDING_HUMAN and none is marked PASS.**

---

# 1. Three distinct things, never conflated

| | Count | What it is |
|---|---:|---|
| physical learner screen | **29** | a page the learner navigates to |
| runtime state | **100** | a variable the player holds; a popup is a state, not a page |
| PowerPoint review page | **100** | an artefact of the review build so Bariah can *see* a state |

The review-page count was not chosen. It is one page per runtime state, and the generator
**raises** if the two ever disagree. Review-page roles:

| role | pages |
|---|---:|
| `SPECIFICATION_POPUP` | 22 |
| `COMPONENT_EXAMPLE_POPUP` | 16 |
| `EXAMPLE_DETAIL_BASE` | 8 |
| `EXAMPLE_DETAIL_ALL_VIEWED` | 8 |
| `SPECIFICATION_CATEGORY_POPUP` | 8 |
| `COMPONENT_MAIN_BASE` | 4 |
| `COMPONENT_EXAMPLES_BASE` | 4 |
| `COMPONENT_EXAMPLES_ALL_VIEWED` | 4 |
| `COMPONENT_EXPLANATION_LIST_BASE` | 3 |
| `COMPONENT_EXPLANATION_LIST_ALL_VIEWED` | 3 |
| `COMPONENT_SPEC_LIST_BASE` | 2 |
| `COMPONENT_SPEC_LIST_ALL_VIEWED` | 2 |
| `TOPIC_SECTION_ENTRY_BASE` | 1 |
| `FRAME_SCENARIO_BASE` | 1 |
| `FRAME_NARRATOR_BASE` | 1 |
| `GROUP_MASTER_BASE` | 1 |
| `GROUP_MASTER_GROUP_COMPLETE` | 1 |
| `GROUP_OVERVIEW_BASE` | 1 |
| `FRAME_SUMMARY_BASE` | 1 |
| `QUIZ_INTRO` | 1 |
| `QUIZ_QUESTION_1` | 1 |
| `QUIZ_QUESTION_2` | 1 |
| `QUIZ_QUESTION_3` | 1 |
| `QUIZ_QUESTION_4` | 1 |
| `QUIZ_QUESTION_5` | 1 |
| `QUIZ_RESULT` | 1 |
| `QUIZ_REVIEW` | 1 |
| `FRAME_END_BASE` | 1 |

---

# 2. CHECKABLE

## 2.1 Source QA

```
PASS  SOURCE_ROWS_EXPECTED                             26
PASS  SOURCE_ROWS_ACCOUNTED                            26
PASS  SOURCE_ROWS_CREATED                              0
PASS  DUPLICATE_SOURCE_ROW_UID                         0
PASS  SOURCE_ASSETS_EXPECTED                           14
PASS  SOURCE_ASSETS_ACCOUNTED                          14
PASS  ORPHAN_SOURCE_ASSETS                             0
PASS  INTERACTION_ITEMS_WITHOUT_SOURCE_BINDING         0
PASS  INTERACTION_ITEMS_WITHOUT_LOCATOR                0
PASS  INTERACTION_ITEMS_WITHOUT_FAMILY                 0
PASS  STATES_WITHOUT_DECISION_ID                       0
PASS  SOURCE_ROWS_WITHOUT_A_REVIEW_PAGE                0
PASS  SOURCE_ROW_LOCATOR_IN_PANEL                      0
```

Every source row is bound, every asset is accounted for, and **no interaction decomposition created
a source row**. Papan Tanda and BBQ Pit each hold one row and yield four interaction categories.

## 2.2 Family QA

```
PASS  FAMILY_S_COMPONENTS                              4
PASS  FAMILY_P1_COMPONENTS                             3
PASS  FAMILY_P2_COMPONENTS                             2
PASS  UNKNOWN_COMPONENT_FAMILY                         0
PASS  COMPONENTS_GENERATED                             9
PASS  PAPAN_TANDA_SPEC_CATEGORIES                      4
PASS  BBQ_PIT_SPEC_CATEGORIES                          4
PASS  BBQ_PIT_CATEGORY_LABELS                          ['Bahan Pembinaan', 'Dimensi', 'Gril', 'Keselamatan']
PASS  GENERIC_ONE_ITEM_PAPAN_TANDA_SCREEN              0
PASS  GENERIC_ONE_ITEM_BBQ_PIT_SCREEN                  0
PASS  PAPAN_TANDA_SOURCE_ROWS_CREATED_BY_SPLIT         0
PASS  BBQ_PIT_SOURCE_ROWS_CREATED_BY_SPLIT             0
PASS  CARDS_DROPPED_OR_INVENTED                        0
PASS  BBQ_PIT_LOWERCASE_P_ON_CANVAS                    0
```

`CARDS_DROPPED_OR_INVENTED` compares the cards actually drawn on each base page against the model's
interaction items for that screen. It is the gate that would have caught defect 1 below.

## 2.3 State and control QA

```
PASS  RUNTIME_STATES_WITHOUT_PARENT                    0
PASS  RETURN_TARGET_MISSING                            0
PASS  POPUP_PARENT_IS_POPUP                            0
PASS  UNKNOWN_CONTROL_TYPE                             0
PASS  REVIEW_PAGES_EQUAL_RUNTIME_STATES                100
PASS  FAMILY_S_PREMATURE_KEMBALI                       0
PASS  FAMILY_P1_FALSE_SIBLING_TICKS                    0
PASS  FAMILY_P1_PREMATURE_EXAMPLE_COMPLETION           0
PASS  FAMILY_P2_PREMATURE_COMPONENT_COMPLETION         0
PASS  DUPLICATE_CUSTOM_SETERUSNYA                      0
PASS  TEXT_TUTUP_BUTTON                                0
PASS  POPUPS_WITHOUT_CLOSE_ICON                        0
PASS  CLOSE_ICON_TITLE_COLLISIONS                      0
```

The completion gates are read from the **rendered ticks**, not from the model. For every page the
expected tick count is derived from what the learner path has actually completed by that point, and
the drawn count must equal it exactly.

## 2.4 Frame QA

```
PASS  S01_NOTES_POLICY                                 'SPOKEN_ENTRY_TITLES_PLUS_ORIENTATION'
PASS  S01_SPOKEN_ELEMENTS                              4
PASS  S01_PL06_TITLE_SPOKEN                            True
PASS  S01_TOPIC_TITLE_SPOKEN                           True
PASS  S01_ORIENTATION_SPOKEN                           True
PASS  S01_MULA_INSTRUCTION_SPOKEN                      True
PASS  S01_COURSE_INTRO_REPEATED                        False
PASS  S01_PL06_OBJECTIVES_REPEATED                     False
PASS  S01_TOPIC_LIST_REPEATED                          False
PASS  S01_HILMI_REINTRODUCED                           False
PASS  S01_COURSE_TITLE_NOT_SPOKEN                      False
PASS  S02_CAST                                         ['Alya', 'Encik Rahman']
PASS  S02_CAST_IN_TRANSCRIPT                           True
PASS  S02_MS2680_LEARNER_CLAIMS                        0
PASS  S02_MS2680_IN_PRODUCTION_PANEL                   True
PASS  S02_GENERIC_ROLE_NAMES_AS_FINAL_NAMES            0
PASS  S03_NARRATOR                                     ['Hilmi']
PASS  S03_HILMI_REINTRODUCED_AS_NEW                    False
PASS  S03_MIND_MAP_DIRECTION_PRESENT                   True
PASS  S03_BOTH_GROUPS_PRESENT                          True
PASS  S03_ALL_NINE_COMPONENTS                          9
PASS  HILMI_LABEL_OUTSIDE_S03                          0
PASS  RUMUSAN_FORBIDDEN_LABELS_DISPLAYED               0
PASS  QUIZ_ITEMS                                       5
PASS  QUIZ_MCQ                                         4
PASS  QUIZ_MULTIPLE_RESPONSE                           1
PASS  QUIZ_MR_LETTER_LABELS                            0
PASS  QUIZ_IMMEDIATE_FEEDBACK_VARIANTS                 2
PASS  QUIZ_QUESTIONS_WITHOUT_BOTH_FEEDBACK_VARIANTS    0
PASS  QUIZ_DETAILED_RATIONALE_LEARNER_FACING           0
PASS  QUIZ_RATIONALE_IN_PRODUCTION_PANEL               0
PASS  QUIZ_RESULT_ELEMENTS                             True
PASS  QUIZ_REVIEW_STATE_PRESENT                        1
PASS  TAMAT_SHELL_NEXT_DISABLED                        True
PASS  TAMAT_NO_CANVAS_NEXT_BUTTON                      0
PASS  TAMAT_UNVERIFIED_ROUTE_ON_CANVAS                 False
PASS  TAMAT_CLOSE_INSTRUCTION                          True
PASS  TAMAT_LOGICAL_DESTINATION_IN_PANEL               True
PASS  TAMAT_EXIT_PENDING_RECORDED                      True
PASS  S02_ONWARDS_PL_TITLE_REANNOUNCEMENTS             0
PASS  S02_ONWARDS_TOPIC_TITLE_REANNOUNCEMENTS          0
```

## 2.5 Notes QA

```
PASS  CONTENT_SLIDES_WITHOUT_NOTES                     0
PASS  S02_ONWARDS_PL_TITLE_REANNOUNCEMENTS             0
PASS  S02_ONWARDS_TOPIC_TITLE_REANNOUNCEMENTS          0
PASS  CONTEXT_BLOCK_MISSING_ON_CONTENT_SLIDES          0
PASS  SILENT_STATES_WITH_NONEMPTY_NOTES                0
PASS  TECHNICAL_IDS_IN_FINAL_NOTES                     0
```

## 2.6 Clean-deck QA

```
PASS  BARIAH_REVIEW_ANNOTATIONS_IN_DECK                0
PASS  BARIAH_ANNOTATIONS_IN_NOTES                      0
PASS  V0_3_TOKENS_IN_PANEL                             0
PASS  PACKAGE_TOKEN_REVIEW_READY                       True
PASS  PACKAGE_TOKEN_BARIAH_FEEDBACK_IMPLEMENTED        True
PASS  PACKAGE_TOKEN_PENDING_TARGETED_CONFIRMATION      True
PASS  PACKAGE_TOKEN_NOT_FOR_MMD_BUILD                  True
PASS  PACKAGE_TOKEN_MULTIMEDIA_NOT_PRODUCED            True
PASS  FORBIDDEN_TOKEN_PRODUCTION_APPROVED              0
PASS  FORBIDDEN_TOKEN_CANONICAL_FREEZE                 0
PASS  FORBIDDEN_TOKEN_MMD_BUILD_READY                  0
PASS  FORBIDDEN_TOKEN_SOURCE_INTEGRITY_FULLY_VERIFIED  0
```

No `Changes made`, `Refer next slide`, `Apply changes`, `Bariah:` marker or v0.3 annotation survives
anywhere in the deck or its Notes. The four forbidden status tokens appear nowhere.

## 2.7 Rich text and production panels

```
PASS  APPROVED_TERMS_NOT_ITALICISED                    0
PASS  APPROVED_TERMS_ITALICISED_AT_LEAST               True
PASS  PRODUCTION_IDS_ITALICISED                        0
PASS  BBQ_PIT_LOWERCASE_P_ON_CANVAS                    0
PASS  WPC_NORMALISATION_PRESENT                        True
PASS  PROMENADE_PRESENT                                True
PASS  PAGES_WITHOUT_PRODUCTION_PANEL                   0
PASS  PRODUCTION_PANEL_ON_CANVAS                       0
PASS  PRODUCTION_PANEL_MISSING_FIELD                   0
```

## 2.8 Layout QA

```
TEXT_OVERFLOW                  = 0
LINE_CLIPPING                  = 0
PANEL_CONTENT_OVERRUN          = 0
OFF_CANVAS_LEAKAGE             = 0
UNINTENDED_NON_MODAL_OVERLAPS  = 0
CLOSE_ICON_TITLE_COLLISIONS    = 0
```

Measured across all 100 rendered pages. The renderer reports
207 `BOX_OVERLAP` events, every one a modal deliberately
covering the screen beneath it; overlaps between non-modal shapes: **0**.

---

# 3. Defects found and fixed at source

All fixed in the grid, the generator or the adapter, with the **complete deck regenerated** after
each. No slide was edited by hand.

| # | Defect | Why it only appeared at propagation | Fix |
|---|---|---|---|
| 1 | **`item_grid(6)` returned five positions and silently dropped the sixth card.** Drinking Fountain's stainless-steel example carries six specification items — Bahan, Injap, Kepala pancutan, Penapisan (pilihan), Perpaipan, Aksesibiliti — so one interaction would have vanished from the deck with no error | the proof exercised 3, 4 and 5 items only; six never occurred | new `grid_n` lays out any count (1–8), and `CARDS_DROPPED_OR_INVENTED` now compares drawn cards against model items on every page |
| 2 | The `Contoh:` line on Family P1 example details overflowed its fixed 0.40in box on 12 pages | the proof's single example had a short `contoh`; Tong Sampah and Drinking Fountain have long ones | the box is measured from the wrapped text and the following content is offset by the measured height |
| 3 | The PowerPoint title placeholder carried approved English terms without italics — 9 occurrences across `Water Feature`, `Drinking Fountain` and `BBQ Pit` | the proof had one such title; propagation multiplied it | `title_ph_rt` emits italic-aware runs, so the outline pane matches the canvas |

Two QA gates of my own were also wrong and were **corrected toward strictness**, not relaxed:

- `FAMILY_P1_PREMATURE_EXAMPLE_COMPLETION` and `FAMILY_P2_PREMATURE_COMPONENT_COMPLETION` flagged
  the *last* popup of a set, where ticking every item is correct. They now require the drawn tick
  count to **equal** the path-derived expectation exactly, which is a tighter test than the one that
  was failing.
- `S03_ALL_NINE_COMPONENTS` compared against text joined without paragraph separators, so
  `Struktur Teduhan` wrapped across two lines read as absent. The comparison is now whitespace-
  normalised; a genuinely missing component still fails.

---

# 4. Rendering

The normal path was attempted first and failed again, exactly as at v0.3 and Stage 3:

```
$ soffice --headless --convert-to pdf K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4.pptx
Error: source file could not be loaded
```

No Impress import filter is installed, so LibreOffice cannot open a `.pptx` at all. Rendering used
the established package parser with Liberation Sans. **Microsoft PowerPoint equivalence is not
proven.** All 100 pages were rendered and inspected, individually and through six
contact sheets grouped by frame screens, Family S, Family P1, Family P2, quiz/result and completion
states. Page images are internal QA and are not committed.

---

# 5. PENDING_HUMAN — none marked PASS

## 5.1 Visual judgment

| # | Item | What to look at |
|---|---|---|
| 1 | Family P1 density and readability | specification cards are deliberately shorter than example cards so the example detail reads as primary. On two-item examples (Kerusi Konkrit, Tong Sampah) the two cards span the full band and may still read as prominent |
| 2 | Family P2 category-card treatment | Papan Tanda and BBQ Pit both show four categories from a single source row. Do the labels read as facets of one specification rather than as separate products? |
| 3 | Close-icon clarity | filled white cross on a solid disc, 0.42in, top-right of every popup. Hit area, contrast and consistency of position |
| 4 | Alya / Encik Rahman visual treatment | S02 currently specifies name and role as text; the character-video treatment is a direction only |
| 5 | S01 VO naturalness | two spoken titles, an orientation sentence and a Mula instruction read consecutively |
| 6 | S03 reflection wording | carried forward from the Bariah exemplar |
| 7 | Rumusan visual treatment | four unlabelled statements; Bariah approved the wording, not this layout |
| 8 | Quiz presentation | option spacing, and whether showing both feedback variants side by side is the right storyboard convention |
| 9 | Tamat instruction clarity | "Tutup tetingkap pelajaran untuk keluar" with no visible next control |
| 10 | Microsoft PowerPoint font wrapping | every measured line, re-checked in the real application |

## 5.2 Open decisions, unchanged by this build

| Item | Status |
|---|---|
| U-01 MS2680 source verification | `PENDING_SOURCE_VERIFICATION` — excluded from learner content, retained in the S02 production panel |
| U-02b Pengurus Projek name | `PENDING_CHARACTER_NAME` — not used in B02 |
| U-03 physical LMS exit | `PENDING_FIRDAUS_CONFIRMATION` — shell Next disabled on Tamat, logical destination in metadata only |
| U-05 quiz rationale placement | `PENDING_BARIAH_CONFIRMATION` — rationale is production metadata only |
| `B02-CAIR-INT-001` module DOCX integrity | open. `SOURCE_INTEGRITY_FULLY_VERIFIED` is **not** claimed |

---

# 6. Standing

Clean review build implementing Bariah's latest rulings. The v0.3 toolchain and deck are unchanged
and hash-identical. No slide was manually patched, no multimedia was created, no final visual asset
was bound, no canonical `P#` was minted. Production approval, canonical freeze, MMD build readiness
and complete module-DOCX integrity are **not** claimed.
