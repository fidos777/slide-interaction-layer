# COMPONENT_VISUAL_PERSISTENCE_TARGETS — v0.4.4

Recomputed from the frozen model for all nine component-main learner screens, then verified against the generated v0.4.4 deck.

# 1. Population

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

`OLD_13_PAGE_TARGET_LIST_REUSED = 0`. The Stage 4.2E-A figure of 13 pages came from diffing the v0.4.3 **deck** and conflated two obligations: 5 all-viewed states that must carry the overview and 8 specification popups that must stay text-led. Reusing it would have pushed overview visuals onto specification popups.

# 2. Implementation result

| Metric | Value |
|---|---:|
| `deck` | K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4.pptx |
| `state_pages_with_base_identity_overview` | 22 |
| `state_pages_total` | 22 |
| `BASE_TO_ALL_VIEWED_OVERVIEW_IDENTITY_MISMATCHES` | 0 |
| `BASE_TO_RETURN_OVERVIEW_IDENTITY_MISMATCHES` | 0 |
| `PERSISTENCE_TARGET_PAGES_MISSING_VISUALS` | 0 |
| `SPECIFICATION_POPUPS_REMAIN_TEXT_LED` | True |
| `OLD_13_PAGE_TARGET_LIST_REUSED` | 0 |
| `comparison_basis` | subject identity, not shape count |

All 22 component-main state pages carry the **same subject identities** as their base page. The comparison is by subject, not by shape count, so a page with the right number of wrong cards fails.

# 3. Per screen

| Learner screen | Overview count | States | Base | All-viewed | Spec popups | Identity matches |
|---|---:|---:|---:|---:|---:|---:|
| `SCR_BBQ_PIT_MAIN` | 1 | 6 | 1 | 1 | 4 | 6/6 |
| `SCR_DRINKING_FOUNTAIN_MAIN` | 2 | 2 | 1 | 1 | 0 | 2/2 |
| `SCR_KEMUDAHAN_AWAM_MAIN` | 3 | 1 | 1 | 0 | 0 | 1/1 |
| `SCR_KERUSI_TAMAN_MAIN` | 3 | 2 | 1 | 1 | 0 | 2/2 |
| `SCR_PAPAN_TANDA_MAIN` | 2 | 6 | 1 | 1 | 4 | 6/6 |
| `SCR_STRUKTUR_PERSISIR_AIR_MAIN` | 5 | 1 | 1 | 0 | 0 | 1/1 |
| `SCR_STRUKTUR_TEDUHAN_MAIN` | 5 | 1 | 1 | 0 | 0 | 1/1 |
| `SCR_TONG_SAMPAH_MAIN` | 3 | 2 | 1 | 1 | 0 | 2/2 |
| `SCR_WATER_FEATURE_MAIN` | 3 | 1 | 1 | 0 | 0 | 1/1 |

# 4. Treatment rules in force

| State | Required treatment |
|---|---|
| `COMPONENT_MAIN_BASE` | several smaller source-bound overview visuals |
| `EXAMPLE_OR_INFORMATION_POPUP` | one larger focused visual for the selected item |
| `SPECIFICATION_POPUP` | no visual panel required |
| `ALL_VIEWED` | same component-main overview visuals as the base state |
| `RETURN_STATE` | same component-main overview visuals as the base state |

Population selector: `learner_screen_id` plus every bound runtime state. Review-page classification is reported as an attribute, never used as the selector.
