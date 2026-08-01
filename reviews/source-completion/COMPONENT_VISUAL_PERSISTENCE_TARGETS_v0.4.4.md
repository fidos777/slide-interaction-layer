# COMPONENT_VISUAL_PERSISTENCE_TARGETS — v0.4.4

Recomputed from the frozen model for all nine component-main learner screens.

# 1. How this population was built

| Step | |
|---|---|
| 1 | pin to `learner_screen_id` where `screen_role` is a component-main role |
| 2 | enumerate **every** runtime state bound to that screen, from the model |
| 3 | record the review page for each state |
| 4 | classify the required visual treatment per state |

`POPULATION_PINNED_BY_LEARNER_SCREEN_ID = true` · `CLASSIFICATION_PRIMARY_SELECTOR = false` · `OLD_13_PAGE_TARGET_LIST_REUSED = 0`

## 1.1 The recomputation changed the answer — and prevented an error

The Stage 4.2E-A list said **13 pages need change**. That list was built by diffing the v0.4.3 *deck*, so it enumerated pages that merely *differed*: 5 all-viewed states **and 8 specification popups**.

Under the confirmed treatment rules those 8 specification popups must stay **text-led with no visual panel**. Reusing the old list would have pushed component-main overview visuals onto them — precisely what Part 12A forbids. The obligation population is:

| Treatment | Pages |
|---|---:|
| overview persistence targets (all-viewed / return) | **5** |
| focused popup targets on component-main screens | 0 |
| specification popups — **no visual** | 8 |
| base states carrying the overview | 9 |
| **total runtime states bound** | **22** |

`FOCUSED_POPUP_TARGET_PAGES = 0` on component-main screens is correct, not an omission: example popups belong to the selection screens and the Family P1 example-detail screens, not to the component mains.

# 2. Totals

| Metric | Value |
|---|---:|
| `COMPONENT_MAIN_SCREENS_REQUIRED` | 9 |
| `COMPONENT_MAIN_RUNTIME_STATES_BOUND` | 22 |
| `OVERVIEW_PERSISTENCE_TARGET_PAGES` | 5 |
| `FOCUSED_POPUP_TARGET_PAGES` | 0 |
| `SPECIFICATION_POPUP_TARGET_PAGES` | 8 |
| `OLD_13_PAGE_TARGET_LIST_REUSED` | 0 |
| `POPULATION_PINNED_BY_LEARNER_SCREEN_ID` | True |
| `CLASSIFICATION_PRIMARY_SELECTOR` | False |

# 3. Per screen

| Learner screen | States | Base | Overview persistence | Focused popup | Spec popup |
|---|---:|---:|---:|---:|---:|
| `SCR_BBQ_PIT_MAIN` | 6 | 1 | 1 | 0 | 4 |
| `SCR_DRINKING_FOUNTAIN_MAIN` | 2 | 1 | 1 | 0 | 0 |
| `SCR_KEMUDAHAN_AWAM_MAIN` | 1 | 1 | 0 | 0 | 0 |
| `SCR_KERUSI_TAMAN_MAIN` | 2 | 1 | 1 | 0 | 0 |
| `SCR_PAPAN_TANDA_MAIN` | 6 | 1 | 1 | 0 | 4 |
| `SCR_STRUKTUR_PERSISIR_AIR_MAIN` | 1 | 1 | 0 | 0 | 0 |
| `SCR_STRUKTUR_TEDUHAN_MAIN` | 1 | 1 | 0 | 0 | 0 |
| `SCR_TONG_SAMPAH_MAIN` | 2 | 1 | 1 | 0 | 0 |
| `SCR_WATER_FEATURE_MAIN` | 1 | 1 | 0 | 0 | 0 |

# 4. Treatment rules in force

| State | Required treatment |
|---|---|
| `COMPONENT_MAIN_BASE` | several smaller source-bound overview visuals |
| `EXAMPLE_OR_INFORMATION_POPUP` | one larger focused visual for the selected item |
| `SPECIFICATION_POPUP` | no visual panel required |
| `ALL_VIEWED` | same component-main overview visuals as the base state |
| `RETURN_STATE` | same component-main overview visuals as the base state |

# 5. Standing

This population is complete and independent of the overview-subject question. It is **not implemented**: `COMPONENT_OVERVIEW_MAPPING_v0.4.4` is blocked on two components, so no v0.4.4 deck was generated and the v0.4.3 deck is unchanged.
