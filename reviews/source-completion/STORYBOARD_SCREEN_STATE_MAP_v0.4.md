# STORYBOARD_SCREEN_STATE_MAP — K5 PL06 T03 B02 v0.4

```
B02_V0_4_SCREEN_STATE_MODEL_DEFINED
LEARNER_SCREENS = 29 · RUNTIME_STATES = 100 · INTERACTION_ITEMS = 54
SOURCE_ROW_COUNT = 26 · SOURCE_ASSET_COUNT = 14 · SOURCE_ROWS_CHANGED = 0
EXECUTION_FAMILIES = 3 · UNKNOWN_COMPONENT_FAMILY = 0
INTERACTION_SELECTION_DEPTH_MAX = 2
FAMILY_P1_SCREEN_PATH_LAYER_COUNT_FROM_GROUP_MASTER = 3
REVIEW_PAGE_NUMBERS_NOT_ASSIGNED
DOCS_ONLY · GENERATOR_UNTOUCHED · NO_POWERPOINT_GENERATED · NO_MULTIMEDIA · NO_ASSET_BOUND
```

The machine-readable form is `STORYBOARD_SCREEN_STATE_MAP_v0.4.json`; the governing rules are in
`B02_V0_4_MODEL_CONTRACT.json`. This document is the human-readable view of the same records — it
does not restate them, it indexes them.

**No PowerPoint review-page numbers are assigned.** Each record carries a stable semantic
`review_page_role` instead. Page numbers are a rendering concern and belong to the regeneration stage.

---

# 1. What the model separates

Six identifier spaces, none derived by counting another:

| Space | Owner | Count in v0.4 |
|---|---|---|
| `source_row_uid` | the module source table | **26 — invariant** |
| `source_asset_id` | the extracted PDF asset register | **14 — invariant** |
| `interaction_item_id` | the execution family | 54 |
| `learner_screen_id` | a physical learner screen | 29 |
| `runtime_state_id` | a runtime state of a screen | 100 |
| `review_page_role` | the eventual PowerPoint rendering | semantic roles only — **not numbered** |

> A source row is a fact about the module. An interaction item is a decision about the courseware.
> A popup is a runtime state. None of them is a PowerPoint page.

---

# 2. Depth semantics — two separate metrics

The model records no single field named `navigation_depth`.

| Metric | Meaning | S | P1 | P2 |
|---|---|:-:|:-:|:-:|
| `INTERACTION_SELECTION_DEPTH_MAX` | learner selection levels inside a component interaction | 1 | **2** | 1 |
| `SCREEN_PATH_LAYER_COUNT_FROM_GROUP_MASTER` | screen layers traversed from the group master to the deepest content state | 3 | **3** | 2 |

Family P1's two selection levels are Bariah's own: *"klik contoh - level 1"* and *"klik spesifikasi -
level 2"*. The component overview is an **entry screen, not a selection level**.

```
FAMILY_P1 screen path
  layer 0   Perabot Taman overview
  layer 1   component overview + example list
  layer 2   example full slide
  layer 3   specification popup state
```

Invariants: a popup is a runtime state, never a navigation destination; **a popup must never open
another popup**.

---

# 3. Screen inventory

| Family | Screens | States | Interaction items |
|---|---:|---:|---:|
| `FRAME` | 6 | 13 | 0 |
| `FAMILY_S` | 9 | 30 | 16 |
| `FAMILY_P1` | 11 | 44 | 30 |
| `FAMILY_P2` | 2 | 12 | 8 |
| `FAMILY_P1+FAMILY_P2` | 1 | 1 | 0 |
| **Total** | **29** | **100** | **54** |

## 3.1 Every learner screen

| screen_id | semantic name | role | family | component | parent | layer | sel. level |
|---|---|---|---|---|---|:-:|:-:|
| `SCR_S01` | Tajuk / Mula Bahagian | `FRAME_TITLE` | `FRAME` | — | `—` | 0 | 0 |
| `SCR_S02` | Pengenalan — senario tapak | `FRAME_SCENARIO` | `FRAME` | — | `—` | 0 | 0 |
| `SCR_S03` | Pengenalan — gambaran keseluruhan (Hilmi) | `FRAME_NARRATOR` | `FRAME` | — | `—` | 0 | 0 |
| `SCR_GM_STRUKTUR` | Struktur Taman — papan kumpulan | `GROUP_MASTER` | `FAMILY_S` | — | `—` | 0 | 0 |
| `SCR_PERABOT_OVERVIEW` | Perabot Taman — gambaran keseluruhan | `GROUP_OVERVIEW_NON_INTERACTIVE` | `FAMILY_P1+FAMILY_P2` | — | `—` | 0 | 0 |
| `SCR_STRUKTUR_PERSISIR_AIR_MAIN` | Struktur Persisir Air — penerangan | `COMPONENT_MAIN_EXPLANATION` | `FAMILY_S` | STRUKTUR_PERSISIR_AIR | `SCR_GM_STRUKTUR` | 1 | 0 |
| `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | Contoh Struktur Persisir Air | `COMPONENT_EXAMPLE_SELECTION` | `FAMILY_S` | STRUKTUR_PERSISIR_AIR | `SCR_STRUKTUR_PERSISIR_AIR_MAIN` | 2 | 0 |
| `SCR_STRUKTUR_TEDUHAN_MAIN` | Struktur Teduhan — penerangan | `COMPONENT_MAIN_EXPLANATION` | `FAMILY_S` | STRUKTUR_TEDUHAN | `SCR_GM_STRUKTUR` | 1 | 0 |
| `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | Contoh Struktur Teduhan | `COMPONENT_EXAMPLE_SELECTION` | `FAMILY_S` | STRUKTUR_TEDUHAN | `SCR_STRUKTUR_TEDUHAN_MAIN` | 2 | 0 |
| `SCR_KEMUDAHAN_AWAM_MAIN` | Kemudahan Awam — penerangan | `COMPONENT_MAIN_EXPLANATION` | `FAMILY_S` | KEMUDAHAN_AWAM | `SCR_GM_STRUKTUR` | 1 | 0 |
| `SCR_KEMUDAHAN_AWAM_EXAMPLES` | Contoh Kemudahan Awam | `COMPONENT_EXAMPLE_SELECTION` | `FAMILY_S` | KEMUDAHAN_AWAM | `SCR_KEMUDAHAN_AWAM_MAIN` | 2 | 0 |
| `SCR_WATER_FEATURE_MAIN` | Water Feature — penerangan | `COMPONENT_MAIN_EXPLANATION` | `FAMILY_S` | WATER_FEATURE | `SCR_GM_STRUKTUR` | 1 | 0 |
| `SCR_WATER_FEATURE_EXAMPLES` | Contoh Water Feature | `COMPONENT_EXAMPLE_SELECTION` | `FAMILY_S` | WATER_FEATURE | `SCR_WATER_FEATURE_MAIN` | 2 | 0 |
| `SCR_KERUSI_TAMAN_MAIN` | Kerusi Taman — penerangan + senarai contoh | `COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST` | `FAMILY_P1` | KERUSI_TAMAN | `SCR_PERABOT_OVERVIEW` | 1 | 0 |
| `SCR_KERUSI_TAMAN_EX01_DETAIL` | Kerusi Taman — Kerusi Kayu Keras | `EXAMPLE_DETAIL_FULL_SLIDE` | `FAMILY_P1` | KERUSI_TAMAN | `SCR_KERUSI_TAMAN_MAIN` | 2 | 1 |
| `SCR_KERUSI_TAMAN_EX02_DETAIL` | Kerusi Taman — Kerusi Konkrit | `EXAMPLE_DETAIL_FULL_SLIDE` | `FAMILY_P1` | KERUSI_TAMAN | `SCR_KERUSI_TAMAN_MAIN` | 2 | 1 |
| `SCR_KERUSI_TAMAN_EX03_DETAIL` | Kerusi Taman — Kerusi Komposit | `EXAMPLE_DETAIL_FULL_SLIDE` | `FAMILY_P1` | KERUSI_TAMAN | `SCR_KERUSI_TAMAN_MAIN` | 2 | 1 |
| `SCR_PAPAN_TANDA_MAIN` | Papan Tanda — penerangan + senarai spesifikasi | `COMPONENT_EXPLANATION_WITH_SPEC_LIST` | `FAMILY_P2` | PAPAN_TANDA | `SCR_PERABOT_OVERVIEW` | 1 | 0 |
| `SCR_TONG_SAMPAH_MAIN` | Tong Sampah — penerangan + senarai contoh | `COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST` | `FAMILY_P1` | TONG_SAMPAH | `SCR_PERABOT_OVERVIEW` | 1 | 0 |
| `SCR_TONG_SAMPAH_EX01_DETAIL` | Tong Sampah — Tong Sampah Logam | `EXAMPLE_DETAIL_FULL_SLIDE` | `FAMILY_P1` | TONG_SAMPAH | `SCR_TONG_SAMPAH_MAIN` | 2 | 1 |
| `SCR_TONG_SAMPAH_EX02_DETAIL` | Tong Sampah — Tong Sampah Konkrit/Batu | `EXAMPLE_DETAIL_FULL_SLIDE` | `FAMILY_P1` | TONG_SAMPAH | `SCR_TONG_SAMPAH_MAIN` | 2 | 1 |
| `SCR_TONG_SAMPAH_EX03_DETAIL` | Tong Sampah — Tong Sampah Plastik Kitar Semula (HDPE) | `EXAMPLE_DETAIL_FULL_SLIDE` | `FAMILY_P1` | TONG_SAMPAH | `SCR_TONG_SAMPAH_MAIN` | 2 | 1 |
| `SCR_DRINKING_FOUNTAIN_MAIN` | Drinking Fountain — penerangan + senarai contoh | `COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST` | `FAMILY_P1` | DRINKING_FOUNTAIN | `SCR_PERABOT_OVERVIEW` | 1 | 0 |
| `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | Drinking Fountain — Pancutan Air Minum Keluli Tahan Karat | `EXAMPLE_DETAIL_FULL_SLIDE` | `FAMILY_P1` | DRINKING_FOUNTAIN | `SCR_DRINKING_FOUNTAIN_MAIN` | 2 | 1 |
| `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` | Drinking Fountain — Pancutan Air Minum Konkrit/Batu | `EXAMPLE_DETAIL_FULL_SLIDE` | `FAMILY_P1` | DRINKING_FOUNTAIN | `SCR_DRINKING_FOUNTAIN_MAIN` | 2 | 1 |
| `SCR_BBQ_PIT_MAIN` | BBQ Pit — penerangan + senarai spesifikasi | `COMPONENT_EXPLANATION_WITH_SPEC_LIST` | `FAMILY_P2` | BBQ_PIT | `SCR_PERABOT_OVERVIEW` | 1 | 0 |
| `SCR_RUMUSAN` | Rumusan | `FRAME_SUMMARY` | `FRAME` | — | `—` | 0 | 0 |
| `SCR_KUIZ` | Kuiz — semakan pengetahuan | `FRAME_QUIZ` | `FRAME` | — | `—` | 0 | 0 |
| `SCR_TAMAT` | Tamat Topik 3 Bahagian 2 | `FRAME_END` | `FRAME` | — | `—` | 0 | 0 |

---

# 4. Per-screen detail

## `SCR_S01` — Tajuk / Mula Bahagian

| Field | Value |
|---|---|
| `screen_role` | FRAME_TITLE |
| `execution_family` | FRAME |
| `group_id` | — |
| `component_id` | — |
| `parent_screen_id` | — |
| `review_page_role` | FRAME_TITLE_BASE |
| `content_source_locator` | storyboard frame — not a module source row |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | MULA_BUTTON |
| `next_enabled_condition` | always_enabled — no auto-advance |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 0 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Komponen Landskap |
| `decision_ids` | `B02-D-06` |

> VO PL satu, bukan PL kosong satu, dan seterusnya

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_S01_BASE` | `STATE_BASE` | `FRAME_TITLE_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_S02` — Pengenalan — senario tapak

| Field | Value |
|---|---|
| `screen_role` | FRAME_SCENARIO |
| `execution_family` | FRAME |
| `group_id` | — |
| `component_id` | — |
| `parent_screen_id` | — |
| `review_page_role` | FRAME_SCENARIO_BASE |
| `content_source_locator` | storyboard frame — Bariah-reviewed dialogue structure, exemplar slide 4 |
| `notes_policy` | DIALOGUE_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | dialogue_video_complete |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 0 |
| `unresolved_status` | U-01 — MS2680 sentence omitted from learner-facing dialogue; retained in production metadata as PENDING_SOURCE_VERIFICATION |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Pengenalan — senario tapak |
| `decision_ids` | `B02-D-06`, `B02-D-17`, `B02-D-18`, `B02-D-19` |

**Characters**

| character_id | character_name | canonical_role | scene_role |
|---|---|---|---|
| `ALYA` | **Alya** | Kontraktor Junior | learner proxy — junior contractor who confirms her understanding of the work scope |
| `ENCIK_RAHMAN` | **Encik Rahman** | Mentor / Kontraktor Senior Berpengalaman Landskap | Penyelia Tapak / mentor who validates and extends Alya’s understanding |

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_S02_BASE` | `STATE_BASE` | `FRAME_SCENARIO_BASE` | `DIALOGUE_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_S03` — Pengenalan — gambaran keseluruhan (Hilmi)

| Field | Value |
|---|---|
| `screen_role` | FRAME_NARRATOR |
| `execution_family` | FRAME |
| `group_id` | — |
| `component_id` | — |
| `parent_screen_id` | — |
| `review_page_role` | FRAME_NARRATOR_BASE |
| `content_source_locator` | storyboard frame — exemplar slide 6 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | vo_complete |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 0 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Pengenalan — gambaran keseluruhan |
| `decision_ids` | `B02-D-06`, `B02-D-20` |

**Characters**

| character_id | character_name | canonical_role | scene_role |
|---|---|---|---|
| `HILMI` | **Hilmi** | Narator kursus | course narrator; not part of the Alya–Encik Rahman scenario cast |

> "Hilmi:" speaker prefix appears on S03 only; it must not appear on any other screen

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_S03_BASE` | `STATE_BASE` | `FRAME_NARRATOR_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_GM_STRUKTUR` — Struktur Taman — papan kumpulan

| Field | Value |
|---|---|
| `screen_role` | GROUP_MASTER |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | — |
| `parent_screen_id` | — |
| `review_page_role` | GROUP_MASTER_BASE |
| `content_source_locator` | modul ms 237 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | group_complete[STRUKTUR_TAMAN] |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | GROUP |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 0 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman |
| `decision_ids` | `B02-D-01`, `B02-D-04` |

> No custom learner-canvas Seterusnya. Progression is the LMS shell control.

**Runtime states — 2**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_GM_STRUKTUR_BASE` | `STATE_BASE` | `GROUP_MASTER_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `GROUP` |
| `ST_GM_STRUKTUR_GROUP_COMPLETE` | `STATE_GROUP_COMPLETE` | `GROUP_MASTER_GROUP_COMPLETE` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `—` | `GROUP` |

## `SCR_PERABOT_OVERVIEW` — Perabot Taman — gambaran keseluruhan

| Field | Value |
|---|---|
| `screen_role` | GROUP_OVERVIEW_NON_INTERACTIVE |
| `execution_family` | FAMILY_P1+FAMILY_P2 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | — |
| `parent_screen_id` | — |
| `review_page_role` | GROUP_OVERVIEW_BASE |
| `content_source_locator` | modul ms 242 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | vo_complete |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 0 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman |
| `decision_ids` | `B02-D-02`, `B02-D-03`, `B02-D-04` |

> No click and no interaction level. Learners enter each component through shell navigation.

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_PERABOT_OVERVIEW_BASE` | `STATE_BASE` | `GROUP_OVERVIEW_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_STRUKTUR_PERSISIR_AIR_MAIN` — Struktur Persisir Air — penerangan

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_MAIN_EXPLANATION |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | STRUKTUR_PERSISIR_AIR |
| `parent_screen_id` | SCR_GM_STRUKTUR |
| `review_page_role` | COMPONENT_MAIN_BASE |
| `content_source_locator` | modul ms 238 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | vo_complete |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman — Struktur Persisir Air |
| `decision_ids` | `B02-D-01`, `B02-D-04` |

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_STRUKTUR_PERSISIR_AIR_MAIN_BASE` | `STATE_BASE` | `COMPONENT_MAIN_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` — Contoh Struktur Persisir Air

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXAMPLE_SELECTION |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | STRUKTUR_PERSISIR_AIR |
| `parent_screen_id` | SCR_STRUKTUR_PERSISIR_AIR_MAIN |
| `review_page_role` | COMPONENT_EXAMPLES_BASE |
| `content_source_locator` | modul ms 238 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | component_complete[STRUKTUR_PERSISIR_AIR] — all examples viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_GM_STRUKTUR |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 5 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p239-x20` |
| `interaction_item_ids` | 5 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman — Struktur Persisir Air / Contoh — arahan interaksi |
| `decision_ids` | `B02-D-01`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap contoh untuk penjelasan lanjut.**

**Runtime states — 7**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_STRUKTUR_PERSISIR_AIR_EXAMPLES_BASE` | `STATE_BASE` | `COMPONENT_EXAMPLES_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_GM_STRUKTUR` | `COMPONENT` |
| `ST_STRUKTUR_PERSISIR_AIR_POPUP_01` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_PERSISIR_AIR_POPUP_02` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_PERSISIR_AIR_POPUP_03` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_PERSISIR_AIR_POPUP_04` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_PERSISIR_AIR_POPUP_05` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_PERSISIR_AIR_ALL_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_EXAMPLES_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_GM_STRUKTUR` | `COMPONENT` |

## `SCR_STRUKTUR_TEDUHAN_MAIN` — Struktur Teduhan — penerangan

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_MAIN_EXPLANATION |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | STRUKTUR_TEDUHAN |
| `parent_screen_id` | SCR_GM_STRUKTUR |
| `review_page_role` | COMPONENT_MAIN_BASE |
| `content_source_locator` | modul ms 239 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | vo_complete |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman — Struktur Teduhan |
| `decision_ids` | `B02-D-01`, `B02-D-04` |

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_STRUKTUR_TEDUHAN_MAIN_BASE` | `STATE_BASE` | `COMPONENT_MAIN_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_STRUKTUR_TEDUHAN_EXAMPLES` — Contoh Struktur Teduhan

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXAMPLE_SELECTION |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | STRUKTUR_TEDUHAN |
| `parent_screen_id` | SCR_STRUKTUR_TEDUHAN_MAIN |
| `review_page_role` | COMPONENT_EXAMPLES_BASE |
| `content_source_locator` | modul ms 239 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | component_complete[STRUKTUR_TEDUHAN] — all examples viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_GM_STRUKTUR |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 5 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p240-x23` |
| `interaction_item_ids` | 5 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman — Struktur Teduhan / Contoh — arahan interaksi |
| `decision_ids` | `B02-D-01`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap contoh untuk penjelasan lanjut.**

**Runtime states — 7**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_STRUKTUR_TEDUHAN_EXAMPLES_BASE` | `STATE_BASE` | `COMPONENT_EXAMPLES_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_GM_STRUKTUR` | `COMPONENT` |
| `ST_STRUKTUR_TEDUHAN_POPUP_01` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_TEDUHAN_POPUP_02` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_TEDUHAN_POPUP_03` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_TEDUHAN_POPUP_04` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_TEDUHAN_POPUP_05` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | `ITEM` |
| `ST_STRUKTUR_TEDUHAN_ALL_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_EXAMPLES_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_GM_STRUKTUR` | `COMPONENT` |

## `SCR_KEMUDAHAN_AWAM_MAIN` — Kemudahan Awam — penerangan

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_MAIN_EXPLANATION |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | KEMUDAHAN_AWAM |
| `parent_screen_id` | SCR_GM_STRUKTUR |
| `review_page_role` | COMPONENT_MAIN_BASE |
| `content_source_locator` | modul ms 240 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | vo_complete |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman — Kemudahan Awam |
| `decision_ids` | `B02-D-01`, `B02-D-04` |

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_KEMUDAHAN_AWAM_MAIN_BASE` | `STATE_BASE` | `COMPONENT_MAIN_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_KEMUDAHAN_AWAM_EXAMPLES` — Contoh Kemudahan Awam

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXAMPLE_SELECTION |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | KEMUDAHAN_AWAM |
| `parent_screen_id` | SCR_KEMUDAHAN_AWAM_MAIN |
| `review_page_role` | COMPONENT_EXAMPLES_BASE |
| `content_source_locator` | modul ms 240 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | component_complete[KEMUDAHAN_AWAM] — all examples viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_GM_STRUKTUR |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 3 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 3 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman — Kemudahan Awam / Contoh — arahan interaksi |
| `decision_ids` | `B02-D-01`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap contoh untuk penjelasan lanjut.**

**Runtime states — 5**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_KEMUDAHAN_AWAM_EXAMPLES_BASE` | `STATE_BASE` | `COMPONENT_EXAMPLES_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_GM_STRUKTUR` | `COMPONENT` |
| `ST_KEMUDAHAN_AWAM_POPUP_01` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KEMUDAHAN_AWAM_EXAMPLES` | `ITEM` |
| `ST_KEMUDAHAN_AWAM_POPUP_02` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KEMUDAHAN_AWAM_EXAMPLES` | `ITEM` |
| `ST_KEMUDAHAN_AWAM_POPUP_03` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KEMUDAHAN_AWAM_EXAMPLES` | `ITEM` |
| `ST_KEMUDAHAN_AWAM_ALL_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_EXAMPLES_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_GM_STRUKTUR` | `COMPONENT` |

## `SCR_WATER_FEATURE_MAIN` — Water Feature — penerangan

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_MAIN_EXPLANATION |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | WATER_FEATURE |
| `parent_screen_id` | SCR_GM_STRUKTUR |
| `review_page_role` | COMPONENT_MAIN_BASE |
| `content_source_locator` | modul ms 241 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | vo_complete |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman — Water Feature |
| `decision_ids` | `B02-D-01`, `B02-D-04` |

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_WATER_FEATURE_MAIN_BASE` | `STATE_BASE` | `COMPONENT_MAIN_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_WATER_FEATURE_EXAMPLES` — Contoh Water Feature

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXAMPLE_SELECTION |
| `execution_family` | FAMILY_S |
| `group_id` | STRUKTUR_TAMAN |
| `component_id` | WATER_FEATURE |
| `parent_screen_id` | SCR_WATER_FEATURE_MAIN |
| `review_page_role` | COMPONENT_EXAMPLES_BASE |
| `content_source_locator` | modul ms 241 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | component_complete[WATER_FEATURE] — all examples viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_GM_STRUKTUR |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 3 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 3 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Struktur Taman — Water Feature / Contoh — arahan interaksi |
| `decision_ids` | `B02-D-01`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap contoh untuk penjelasan lanjut.**

**Runtime states — 5**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_WATER_FEATURE_EXAMPLES_BASE` | `STATE_BASE` | `COMPONENT_EXAMPLES_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_GM_STRUKTUR` | `COMPONENT` |
| `ST_WATER_FEATURE_POPUP_01` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_WATER_FEATURE_EXAMPLES` | `ITEM` |
| `ST_WATER_FEATURE_POPUP_02` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_WATER_FEATURE_EXAMPLES` | `ITEM` |
| `ST_WATER_FEATURE_POPUP_03` | `STATE_POPUP` | `COMPONENT_EXAMPLE_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_WATER_FEATURE_EXAMPLES` | `ITEM` |
| `ST_WATER_FEATURE_ALL_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_EXAMPLES_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_GM_STRUKTUR` | `COMPONENT` |

## `SCR_KERUSI_TAMAN_MAIN` — Kerusi Taman — penerangan + senarai contoh

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | KERUSI_TAMAN |
| `parent_screen_id` | SCR_PERABOT_OVERVIEW |
| `review_page_role` | COMPONENT_EXPLANATION_LIST_BASE |
| `content_source_locator` | modul ms 242 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | component_complete[KERUSI_TAMAN] — all examples viewed |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 3 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 3 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Kerusi Taman |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap contoh untuk penjelasan lanjut.**

**Runtime states — 2**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_KERUSI_TAMAN_MAIN_BASE` | `STATE_BASE` | `COMPONENT_EXPLANATION_LIST_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |
| `ST_KERUSI_TAMAN_ALL_EXAMPLES_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_EXPLANATION_LIST_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |

## `SCR_KERUSI_TAMAN_EX01_DETAIL` — Kerusi Taman — Kerusi Kayu Keras

| Field | Value |
|---|---|
| `screen_role` | EXAMPLE_DETAIL_FULL_SLIDE |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | KERUSI_TAMAN |
| `parent_screen_id` | SCR_KERUSI_TAMAN_MAIN |
| `review_page_role` | EXAMPLE_DETAIL_BASE |
| `content_source_locator` | modul ms 242 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | example_complete[K5-PL06-T03-B02-KERUSI-TAMAN-ROW-01] — all specification items viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_KERUSI_TAMAN_MAIN |
| `completion_scope` | EXAMPLE |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 1 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p242-x28` |
| `interaction_item_ids` | 4 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Kerusi Taman / Contoh: Kerusi Kayu Keras |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

**Runtime states — 6**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_KERUSI_TAMAN_EX01_BASE` | `STATE_BASE` | `EXAMPLE_DETAIL_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_KERUSI_TAMAN_MAIN` | `EXAMPLE` |
| `ST_KERUSI_TAMAN_R01_SPEC01` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ITEM` |
| `ST_KERUSI_TAMAN_R01_SPEC02` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ITEM` |
| `ST_KERUSI_TAMAN_R01_SPEC03` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ITEM` |
| `ST_KERUSI_TAMAN_R01_SPEC04` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ITEM` |
| `ST_KERUSI_TAMAN_EX01_ALL_SPEC_VIEWED` | `STATE_ALL_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_KERUSI_TAMAN_MAIN` | `EXAMPLE` |

## `SCR_KERUSI_TAMAN_EX02_DETAIL` — Kerusi Taman — Kerusi Konkrit

| Field | Value |
|---|---|
| `screen_role` | EXAMPLE_DETAIL_FULL_SLIDE |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | KERUSI_TAMAN |
| `parent_screen_id` | SCR_KERUSI_TAMAN_MAIN |
| `review_page_role` | EXAMPLE_DETAIL_BASE |
| `content_source_locator` | modul ms 243 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | example_complete[K5-PL06-T03-B02-KERUSI-TAMAN-ROW-02] — all specification items viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_KERUSI_TAMAN_MAIN |
| `completion_scope` | EXAMPLE |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 1 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p243-x31` |
| `interaction_item_ids` | 2 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Kerusi Taman / Contoh: Kerusi Konkrit |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

**Runtime states — 4**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_KERUSI_TAMAN_EX02_BASE` | `STATE_BASE` | `EXAMPLE_DETAIL_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_KERUSI_TAMAN_MAIN` | `EXAMPLE` |
| `ST_KERUSI_TAMAN_R02_SPEC01` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KERUSI_TAMAN_EX02_DETAIL` | `ITEM` |
| `ST_KERUSI_TAMAN_R02_SPEC02` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KERUSI_TAMAN_EX02_DETAIL` | `ITEM` |
| `ST_KERUSI_TAMAN_EX02_ALL_SPEC_VIEWED` | `STATE_ALL_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_KERUSI_TAMAN_MAIN` | `EXAMPLE` |

## `SCR_KERUSI_TAMAN_EX03_DETAIL` — Kerusi Taman — Kerusi Komposit

| Field | Value |
|---|---|
| `screen_role` | EXAMPLE_DETAIL_FULL_SLIDE |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | KERUSI_TAMAN |
| `parent_screen_id` | SCR_KERUSI_TAMAN_MAIN |
| `review_page_role` | EXAMPLE_DETAIL_BASE |
| `content_source_locator` | modul ms 243 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | example_complete[K5-PL06-T03-B02-KERUSI-TAMAN-ROW-03] — all specification items viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_KERUSI_TAMAN_MAIN |
| `completion_scope` | EXAMPLE |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 1 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p243-x32` |
| `interaction_item_ids` | 2 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Kerusi Taman / Contoh: Kerusi Komposit |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

**Runtime states — 4**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_KERUSI_TAMAN_EX03_BASE` | `STATE_BASE` | `EXAMPLE_DETAIL_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_KERUSI_TAMAN_MAIN` | `EXAMPLE` |
| `ST_KERUSI_TAMAN_R03_SPEC01` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KERUSI_TAMAN_EX03_DETAIL` | `ITEM` |
| `ST_KERUSI_TAMAN_R03_SPEC02` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_KERUSI_TAMAN_EX03_DETAIL` | `ITEM` |
| `ST_KERUSI_TAMAN_EX03_ALL_SPEC_VIEWED` | `STATE_ALL_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_KERUSI_TAMAN_MAIN` | `EXAMPLE` |

## `SCR_PAPAN_TANDA_MAIN` — Papan Tanda — penerangan + senarai spesifikasi

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXPLANATION_WITH_SPEC_LIST |
| `execution_family` | FAMILY_P2 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | PAPAN_TANDA |
| `parent_screen_id` | SCR_PERABOT_OVERVIEW |
| `review_page_role` | COMPONENT_SPEC_LIST_BASE |
| `content_source_locator` | modul ms 243 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | component_complete[PAPAN_TANDA] — all specification categories viewed |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p245-x37`, `K5PL06T03-B02-IMG-p245-x38` |
| `interaction_item_ids` | 4 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Papan Tanda |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

> No generic one-item Contoh screen exists for this component.

**Runtime states — 6**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_PAPAN_TANDA_MAIN_BASE` | `STATE_BASE` | `COMPONENT_SPEC_LIST_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |
| `ST_PAPAN_TANDA_CAT01` | `STATE_POPUP` | `SPECIFICATION_CATEGORY_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_PAPAN_TANDA_MAIN` | `ITEM` |
| `ST_PAPAN_TANDA_CAT02` | `STATE_POPUP` | `SPECIFICATION_CATEGORY_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_PAPAN_TANDA_MAIN` | `ITEM` |
| `ST_PAPAN_TANDA_CAT03` | `STATE_POPUP` | `SPECIFICATION_CATEGORY_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_PAPAN_TANDA_MAIN` | `ITEM` |
| `ST_PAPAN_TANDA_CAT04` | `STATE_POPUP` | `SPECIFICATION_CATEGORY_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_PAPAN_TANDA_MAIN` | `ITEM` |
| `ST_PAPAN_TANDA_ALL_CATEGORIES_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_SPEC_LIST_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |

## `SCR_TONG_SAMPAH_MAIN` — Tong Sampah — penerangan + senarai contoh

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | TONG_SAMPAH |
| `parent_screen_id` | SCR_PERABOT_OVERVIEW |
| `review_page_role` | COMPONENT_EXPLANATION_LIST_BASE |
| `content_source_locator` | modul ms 245 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | component_complete[TONG_SAMPAH] — all examples viewed |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 3 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 3 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Tong Sampah |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap contoh untuk penjelasan lanjut.**

**Runtime states — 2**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_TONG_SAMPAH_MAIN_BASE` | `STATE_BASE` | `COMPONENT_EXPLANATION_LIST_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |
| `ST_TONG_SAMPAH_ALL_EXAMPLES_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_EXPLANATION_LIST_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |

## `SCR_TONG_SAMPAH_EX01_DETAIL` — Tong Sampah — Tong Sampah Logam

| Field | Value |
|---|---|
| `screen_role` | EXAMPLE_DETAIL_FULL_SLIDE |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | TONG_SAMPAH |
| `parent_screen_id` | SCR_TONG_SAMPAH_MAIN |
| `review_page_role` | EXAMPLE_DETAIL_BASE |
| `content_source_locator` | modul ms 246 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | example_complete[K5-PL06-T03-B02-TONG-SAMPAH-ROW-01] — all specification items viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_TONG_SAMPAH_MAIN |
| `completion_scope` | EXAMPLE |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 1 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p246-x41` |
| `interaction_item_ids` | 2 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Tong Sampah / Contoh: Tong Sampah Logam |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

**Runtime states — 4**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_TONG_SAMPAH_EX01_BASE` | `STATE_BASE` | `EXAMPLE_DETAIL_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_TONG_SAMPAH_MAIN` | `EXAMPLE` |
| `ST_TONG_SAMPAH_R01_SPEC01` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_TONG_SAMPAH_EX01_DETAIL` | `ITEM` |
| `ST_TONG_SAMPAH_R01_SPEC02` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_TONG_SAMPAH_EX01_DETAIL` | `ITEM` |
| `ST_TONG_SAMPAH_EX01_ALL_SPEC_VIEWED` | `STATE_ALL_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_TONG_SAMPAH_MAIN` | `EXAMPLE` |

## `SCR_TONG_SAMPAH_EX02_DETAIL` — Tong Sampah — Tong Sampah Konkrit/Batu

| Field | Value |
|---|---|
| `screen_role` | EXAMPLE_DETAIL_FULL_SLIDE |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | TONG_SAMPAH |
| `parent_screen_id` | SCR_TONG_SAMPAH_MAIN |
| `review_page_role` | EXAMPLE_DETAIL_BASE |
| `content_source_locator` | modul ms 246 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | example_complete[K5-PL06-T03-B02-TONG-SAMPAH-ROW-02] — all specification items viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_TONG_SAMPAH_MAIN |
| `completion_scope` | EXAMPLE |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 1 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p247-x44` |
| `interaction_item_ids` | 2 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Tong Sampah / Contoh: Tong Sampah Konkrit/Batu |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

**Runtime states — 4**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_TONG_SAMPAH_EX02_BASE` | `STATE_BASE` | `EXAMPLE_DETAIL_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_TONG_SAMPAH_MAIN` | `EXAMPLE` |
| `ST_TONG_SAMPAH_R02_SPEC01` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_TONG_SAMPAH_EX02_DETAIL` | `ITEM` |
| `ST_TONG_SAMPAH_R02_SPEC02` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_TONG_SAMPAH_EX02_DETAIL` | `ITEM` |
| `ST_TONG_SAMPAH_EX02_ALL_SPEC_VIEWED` | `STATE_ALL_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_TONG_SAMPAH_MAIN` | `EXAMPLE` |

## `SCR_TONG_SAMPAH_EX03_DETAIL` — Tong Sampah — Tong Sampah Plastik Kitar Semula (HDPE)

| Field | Value |
|---|---|
| `screen_role` | EXAMPLE_DETAIL_FULL_SLIDE |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | TONG_SAMPAH |
| `parent_screen_id` | SCR_TONG_SAMPAH_MAIN |
| `review_page_role` | EXAMPLE_DETAIL_BASE |
| `content_source_locator` | modul ms 247 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | example_complete[K5-PL06-T03-B02-TONG-SAMPAH-ROW-03] — all specification items viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_TONG_SAMPAH_MAIN |
| `completion_scope` | EXAMPLE |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 1 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p247-x45`, `K5PL06T03-B02-IMG-p247-x46` |
| `interaction_item_ids` | 2 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Tong Sampah / Contoh: Tong Sampah Plastik Kitar Semula (HDPE) |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

**Runtime states — 4**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_TONG_SAMPAH_EX03_BASE` | `STATE_BASE` | `EXAMPLE_DETAIL_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_TONG_SAMPAH_MAIN` | `EXAMPLE` |
| `ST_TONG_SAMPAH_R03_SPEC01` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_TONG_SAMPAH_EX03_DETAIL` | `ITEM` |
| `ST_TONG_SAMPAH_R03_SPEC02` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_TONG_SAMPAH_EX03_DETAIL` | `ITEM` |
| `ST_TONG_SAMPAH_EX03_ALL_SPEC_VIEWED` | `STATE_ALL_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_TONG_SAMPAH_MAIN` | `EXAMPLE` |

## `SCR_DRINKING_FOUNTAIN_MAIN` — Drinking Fountain — penerangan + senarai contoh

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | DRINKING_FOUNTAIN |
| `parent_screen_id` | SCR_PERABOT_OVERVIEW |
| `review_page_role` | COMPONENT_EXPLANATION_LIST_BASE |
| `content_source_locator` | modul ms 247 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | component_complete[DRINKING_FOUNTAIN] — all examples viewed |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 2 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 2 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Drinking Fountain |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap contoh untuk penjelasan lanjut.**

**Runtime states — 2**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_DRINKING_FOUNTAIN_MAIN_BASE` | `STATE_BASE` | `COMPONENT_EXPLANATION_LIST_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |
| `ST_DRINKING_FOUNTAIN_ALL_EXAMPLES_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_EXPLANATION_LIST_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |

## `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` — Drinking Fountain — Pancutan Air Minum Keluli Tahan Karat

| Field | Value |
|---|---|
| `screen_role` | EXAMPLE_DETAIL_FULL_SLIDE |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | DRINKING_FOUNTAIN |
| `parent_screen_id` | SCR_DRINKING_FOUNTAIN_MAIN |
| `review_page_role` | EXAMPLE_DETAIL_BASE |
| `content_source_locator` | modul ms 248 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | example_complete[K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-01] — all specification items viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_DRINKING_FOUNTAIN_MAIN |
| `completion_scope` | EXAMPLE |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 1 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p248-x49` |
| `interaction_item_ids` | 6 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Drinking Fountain / Contoh: Pancutan Air Minum Keluli Tahan Karat |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

**Runtime states — 8**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_DRINKING_FOUNTAIN_EX01_BASE` | `STATE_BASE` | `EXAMPLE_DETAIL_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_DRINKING_FOUNTAIN_MAIN` | `EXAMPLE` |
| `ST_DRINKING_FOUNTAIN_R01_SPEC01` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | `ITEM` |
| `ST_DRINKING_FOUNTAIN_R01_SPEC02` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | `ITEM` |
| `ST_DRINKING_FOUNTAIN_R01_SPEC03` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | `ITEM` |
| `ST_DRINKING_FOUNTAIN_R01_SPEC04` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | `ITEM` |
| `ST_DRINKING_FOUNTAIN_R01_SPEC05` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | `ITEM` |
| `ST_DRINKING_FOUNTAIN_R01_SPEC06` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | `ITEM` |
| `ST_DRINKING_FOUNTAIN_EX01_ALL_SPEC_VIEWED` | `STATE_ALL_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_DRINKING_FOUNTAIN_MAIN` | `EXAMPLE` |

## `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` — Drinking Fountain — Pancutan Air Minum Konkrit/Batu

| Field | Value |
|---|---|
| `screen_role` | EXAMPLE_DETAIL_FULL_SLIDE |
| `execution_family` | FAMILY_P1 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | DRINKING_FOUNTAIN |
| `parent_screen_id` | SCR_DRINKING_FOUNTAIN_MAIN |
| `review_page_role` | EXAMPLE_DETAIL_BASE |
| `content_source_locator` | modul ms 248 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | NO_CONTROL |
| `next_enabled_condition` | none |
| `back_control_type` | KEMBALI_BUTTON |
| `back_enabled_condition` | example_complete[K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-02] — all specification items viewed |
| `close_control_type` | NO_CONTROL |
| `return_target` | SCR_DRINKING_FOUNTAIN_MAIN |
| `completion_scope` | EXAMPLE |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 1 |
| `screen_path_layer` | 2 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p249-x56` |
| `interaction_item_ids` | 2 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — Drinking Fountain / Contoh: Pancutan Air Minum Konkrit/Batu |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

**Runtime states — 4**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_DRINKING_FOUNTAIN_EX02_BASE` | `STATE_BASE` | `EXAMPLE_DETAIL_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `SCR_DRINKING_FOUNTAIN_MAIN` | `EXAMPLE` |
| `ST_DRINKING_FOUNTAIN_R02_SPEC01` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` | `ITEM` |
| `ST_DRINKING_FOUNTAIN_R02_SPEC02` | `STATE_POPUP` | `SPECIFICATION_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` | `ITEM` |
| `ST_DRINKING_FOUNTAIN_EX02_ALL_SPEC_VIEWED` | `STATE_ALL_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `SCR_DRINKING_FOUNTAIN_MAIN` | `EXAMPLE` |

## `SCR_BBQ_PIT_MAIN` — BBQ Pit — penerangan + senarai spesifikasi

| Field | Value |
|---|---|
| `screen_role` | COMPONENT_EXPLANATION_WITH_SPEC_LIST |
| `execution_family` | FAMILY_P2 |
| `group_id` | PERABOT_TAMAN |
| `component_id` | BBQ_PIT |
| `parent_screen_id` | SCR_PERABOT_OVERVIEW |
| `review_page_role` | COMPONENT_SPEC_LIST_BASE |
| `content_source_locator` | modul ms 249 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | component_complete[BBQ_PIT] — all specification categories viewed |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | COMPONENT |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 1 |
| `unresolved_status` | NONE |
| `source_row_uids` | 1 |
| `source_asset_ids` | `K5PL06T03-B02-IMG-p249-x57` |
| `interaction_item_ids` | 4 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Perabot Taman — BBQ Pit |
| `decision_ids` | `B02-D-03`, `B02-D-05` |

> Interaction instruction: **Klik pada setiap spesifikasi untuk penjelasan lanjut.**

> No generic one-item Contoh screen exists for this component.

**Runtime states — 6**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_BBQ_PIT_MAIN_BASE` | `STATE_BASE` | `COMPONENT_SPEC_LIST_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |
| `ST_BBQ_PIT_CAT01` | `STATE_POPUP` | `SPECIFICATION_CATEGORY_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_BBQ_PIT_MAIN` | `ITEM` |
| `ST_BBQ_PIT_CAT02` | `STATE_POPUP` | `SPECIFICATION_CATEGORY_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_BBQ_PIT_MAIN` | `ITEM` |
| `ST_BBQ_PIT_CAT03` | `STATE_POPUP` | `SPECIFICATION_CATEGORY_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_BBQ_PIT_MAIN` | `ITEM` |
| `ST_BBQ_PIT_CAT04` | `STATE_POPUP` | `SPECIFICATION_CATEGORY_POPUP` | `CONTENT_VO_NOTES` | `CLOSE_ICON` | `SCR_BBQ_PIT_MAIN` | `ITEM` |
| `ST_BBQ_PIT_ALL_CATEGORIES_VIEWED` | `STATE_ALL_VIEWED` | `COMPONENT_SPEC_LIST_ALL_VIEWED` | `SILENT_STATE_NOTES` | `NO_CONTROL` | `—` | `COMPONENT` |

## `SCR_RUMUSAN` — Rumusan

| Field | Value |
|---|---|
| `screen_role` | FRAME_SUMMARY |
| `execution_family` | FRAME |
| `group_id` | — |
| `component_id` | — |
| `parent_screen_id` | — |
| `review_page_role` | FRAME_SUMMARY_BASE |
| `content_source_locator` | storyboard frame — exemplar slide 71, wording LULUS |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | vo_complete |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 0 |
| `unresolved_status` | NONE |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Rumusan |
| `decision_ids` | `B02-D-09`, `B02-D-08` |

> Forbidden displayed labels: `Kepentingan`, `Isi Utama`, `Apa Yang Dipelajari`, `Manfaat`

> VO omits the redundant opening label "Komponen Landskap — Struktur Taman dan Perabot Taman."

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_RUMUSAN_BASE` | `STATE_BASE` | `FRAME_SUMMARY_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

## `SCR_KUIZ` — Kuiz — semakan pengetahuan

| Field | Value |
|---|---|
| `screen_role` | FRAME_QUIZ |
| `execution_family` | FRAME |
| `group_id` | — |
| `component_id` | — |
| `parent_screen_id` | — |
| `review_page_role` | QUIZ_INTRO |
| `content_source_locator` | modul ms 238 (3.3.1); modul ms 239 (3.3.2); modul ms 240 (3.3.3); modul ms 241 (3.3.4); modul ms 242-249 (3.4.1-3.4.3) |
| `notes_policy` | QUIZ_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | MULA_KUIZ_BUTTON |
| `next_enabled_condition` | always_enabled |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | QUIZ |
| `persistence_rule` | PERSIST_ON_REVISIT_AND_LMS_RESUME |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 0 |
| `unresolved_status` | U-05 — detailed rationale retained in production metadata only, pending Bariah confirmation of its final placement |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Kuiz |
| `decision_ids` | `B02-D-11`, `B02-D-12`, `B02-D-13`, `B02-D-23` |

**Runtime states — 8**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_KUIZ_INTRO` | `STATE_QUIZ_INTRO` | `QUIZ_INTRO` | `QUIZ_NOTES` | `NO_CONTROL` | `—` | `QUIZ` |
| `ST_KUIZ_Q1` | `STATE_QUIZ_QUESTION` | `QUIZ_QUESTION_1` | `QUIZ_NOTES` | `NO_CONTROL` | `—` | `ITEM` |
| `ST_KUIZ_Q2` | `STATE_QUIZ_QUESTION` | `QUIZ_QUESTION_2` | `QUIZ_NOTES` | `NO_CONTROL` | `—` | `ITEM` |
| `ST_KUIZ_Q3` | `STATE_QUIZ_QUESTION` | `QUIZ_QUESTION_3` | `QUIZ_NOTES` | `NO_CONTROL` | `—` | `ITEM` |
| `ST_KUIZ_Q4` | `STATE_QUIZ_QUESTION` | `QUIZ_QUESTION_4` | `QUIZ_NOTES` | `NO_CONTROL` | `—` | `ITEM` |
| `ST_KUIZ_Q5` | `STATE_QUIZ_QUESTION` | `QUIZ_QUESTION_5` | `QUIZ_NOTES` | `NO_CONTROL` | `—` | `ITEM` |
| `ST_KUIZ_RESULT` | `STATE_QUIZ_RESULT` | `QUIZ_RESULT` | `QUIZ_NOTES` | `NO_CONTROL` | `—` | `QUIZ` |
| `ST_KUIZ_REVIEW` | `STATE_QUIZ_REVIEW` | `QUIZ_REVIEW` | `QUIZ_NOTES` | `NO_CONTROL` | `ST_KUIZ_RESULT` | `QUIZ` |

## `SCR_TAMAT` — Tamat Topik 3 Bahagian 2

| Field | Value |
|---|---|
| `screen_role` | FRAME_END |
| `execution_family` | FRAME |
| `group_id` | — |
| `component_id` | — |
| `parent_screen_id` | — |
| `review_page_role` | FRAME_END_BASE |
| `content_source_locator` | storyboard frame — exemplar slide 75 |
| `notes_policy` | CONTENT_VO_NOTES |
| `spoken_transcript_required` | True |
| `next_control_type` | LMS_SHELL_NEXT |
| `next_enabled_condition` | DISABLED on this screen |
| `back_control_type` | NO_CONTROL |
| `back_enabled_condition` | none |
| `close_control_type` | NO_CONTROL |
| `return_target` | — |
| `completion_scope` | NONE |
| `persistence_rule` | NOT_APPLICABLE |
| `interaction_selection_level` | 0 |
| `screen_path_layer` | 0 |
| `unresolved_status` | U-03 — physical LMS exit behaviour is PENDING_FIRDAUS_CONFIRMATION |
| `source_row_uids` | 0 |
| `source_asset_ids` | — |
| `interaction_item_ids` | 0 |
| `notes_context_headers` | PL06: Pengurusan Operasi Pembinaan Landskap / Topik 3 Bahagian 2: Komponen Landskap / Tamat |
| `decision_ids` | `B02-D-14`, `B02-D-15` |

**Runtime states — 1**

| runtime_state_id | role | review_page_role | notes_policy | close | return_target | completion |
|---|---|---|---|---|---|---|
| `ST_TAMAT_BASE` | `STATE_BASE` | `FRAME_END_BASE` | `CONTENT_VO_NOTES` | `NO_CONTROL` | `—` | `NONE` |

---

# 5. Control semantics

| Plane | Controls | Owner |
|---|---|---|
| learner canvas | `MULA_BUTTON`, `MULA_KUIZ_BUTTON`, `KEMBALI_BUTTON` | authored in the deck |
| LMS shell | `LMS_SHELL_NEXT` | the player; gated by completion state, never redrawn on canvas |
| runtime state | `CLOSE_ICON` | closes a popup state and returns to its owning screen |

Contextual return targets — **no single Kembali target is hard-coded across families**:

| Family | Control | Return target |
|---|---|---|
| S | `KEMBALI_BUTTON` | example screen → Struktur Taman group master |
| P1 | `CLOSE_ICON` | specification popup → current example detail |
| P1 | `KEMBALI_BUTTON` | example detail → component overview/list |
| P2 | `CLOSE_ICON` | specification popup → component specification list |
| group master | `LMS_SHELL_NEXT` | progression controlled by the shell |

---

# 6. Notes policy distribution

| notes_policy | Screens | States | Headers | Spoken transcript |
|---|---:|---:|---|:-:|
| `CONTENT_VO_NOTES` | 27 | 73 | PL + Topic + context | yes |
| `DIALOGUE_NOTES` | 1 | 1 | PL + Topic + context | yes |
| `QUIZ_NOTES` | 1 | 8 | PL + Topic + context | yes |
| `SILENT_STATE_NOTES` | 0 | 18 | **none — genuinely empty** | no |

`notes_context_headers` and `spoken_transcript` are separate model fields. The PL and Topic headers
are **non-spoken production context** — MMD and TTS never have to infer which part of Notes is spoken.

---

# 7. Cast

| character | canonical role | B02 function | status | screens |
|---|---|---|---|---|
| **Alya** | Kontraktor Junior | learner character who confirms her understanding of the work scope | `CONFIRMED_CANON` | `SCR_S02` |
| **Encik Rahman** | Mentor / Kontraktor Senior Berpengalaman Landskap | Penyelia Tapak / mentor who validates and extends Alya’s understanding | `CONFIRMED_CANON` | `SCR_S02` |
| **Hilmi** | Narator kursus | narrator; NOT part of the Alya–Encik Rahman scenario cast | `CONFIRMED_NARRATOR` | `SCR_S03` |
| **Puan Nadia** | Pegawai Kewangan / Pengurus Kontrak | NOT REQUIRED IN B02 — no screen carries a genuine financial or contractual instructional function | `CONFIRMED_CANON · NOT_REQUIRED_IN_B02` | — |
| *(name open)* | Pengurus Projek | not used in B02 | `PENDING_CHARACTER_NAME` | — |

```
B02_CHARACTER_NAMES_CONFIRMED    = true
B02_CAST_PAIR                    = ALYA + ENCIK_RAHMAN
B02_NARRATOR                     = HILMI
PL06_CAST_REUSE_POLICY_CONFIRMED = true
PUAN_NADIA_CANON_CONFIRMED       = true
PROJECT_MANAGER_NAME_PENDING     = true
```

`Pelatih` and `Penyelia Tapak` survive only as production-metadata role labels. They are never final
learner-facing character names. No name is invented for the Pengurus Projek.

---

# 8. Open-item execution policies

| Item | Status | Execution policy in v0.4 | Blocks review build |
|---|---|---|:-:|
| **U-01** MS2680 applicability | `PENDING_SOURCE_VERIFICATION` | The MS2680 claim is excluded from learner-facing dialogue on S02. It is retained in production metadata only. No substitute standards claim is invented. The remaining dialogue keeps logical continuity without adding new facts. | no |
| **U-02** Character casting | `RESOLVED_FOR_B02` | Alya, Encik Rahman and Hilmi are the confirmed B02 cast. Generic role labels Pelatih / Penyelia Tapak are production metadata only and are never final learner-facing names. Only the Pengurus Projek name remains open at the wider PL06 canon level. | no |
| **U-03** Tamat / LMS exit | `PENDING_FIRDAUS_CONFIRMATION` | logical_destination = next Bahagian in Topik 3 (production metadata only, never displayed on the learner canvas); physical_exit_behaviour = learner closes the lesson/window; shell_next_state = disabled on Tamat. | no |
| **U-04** BBQ Pit specification categories | `TECHNICAL_DECOMPOSITION_FROM_SOURCE` | Four source-attested categories: Bahan Pembinaan, Dimensi, Gril, Keselamatan. Derived from the labelled specification lines of the single BBQ Pit source row. The BBQ Pit source-row count remains one; no new source_row_uid is created. | no |
| **U-05** Quiz rationale placement | `PENDING_BARIAH_RATIONALE_PLACEMENT_CONFIRMATION` | Immediate feedback is exactly two variants — "Pilihan jawapan tepat." and "Pilihan jawapan tidak tepat." — each with SFX, VO and on-screen text. Detailed per-question rationale is retained in production metadata, the source mapping and QA evidence, and is NOT exposed to the learner until Bariah confirms its final placement. | no |
| **U-06** Module DOCX integrity | `B02-CAIR-INT-001 — OPEN` | The unresolved module DOCX SHA-256 is covered only by B02-CAIR-INT-001. It does not block this review-build model stage. It remains a blocker for canonical freeze, production approval and MMD build authority. SOURCE_INTEGRITY_FULLY_VERIFIED is NOT claimed. | no |

---

# 9. Model totals

```
LEARNER_SCREENS   = 29
RUNTIME_STATES    = 100
INTERACTION_ITEMS = 54   (S 16 · P1 30 · P2 8)
SOURCE_ROW_COUNT  = 26   bound = 26   changed = 0
SOURCE_ASSET_COUNT= 14   bound = 14
```

## 9.1 Model validation — 93 of 93 structural checks pass

Validated **structurally against the model records**, not by whole-document search.

```
SOURCE_ROW_COUNT = 26                          SOURCE_ASSET_COUNT = 14
SOURCE_ROWS_CHANGED = 0                        DUPLICATE_SOURCE_ROW_UID = 0
SOURCE_ROWS_WITHOUT_MODEL_BINDING = 0

EXECUTION_FAMILIES = 3                         UNKNOWN_COMPONENT_FAMILY = 0
FAMILY_S_COMPONENTS = 4  FAMILY_P1_COMPONENTS = 3  FAMILY_P2_COMPONENTS = 2

INTERACTION_SELECTION_DEPTH_MAX = 2
FAMILY_P1_SCREEN_PATH_LAYER_COUNT_FROM_GROUP_MASTER = 3

INTERACTION_ITEMS_WITHOUT_SOURCE_BINDING = 0   INTERACTION_ITEMS_WITHOUT_PARENT = 0
RUNTIME_STATES_WITHOUT_PARENT = 0              RETURN_TARGET_MISSING = 0
UNKNOWN_CONTROL_TYPE = 0                       POPUP_PARENT_IS_POPUP = 0

CONTENT_VO_SCREENS_WITHOUT_NOTES_POLICY = 0    DIALOGUE_SCREENS_WITHOUT_SPEAKER_MAPPING = 0
SILENT_STATES_WITH_NONEMPTY_NOTES_POLICY = 0

B02_CHARACTER_NAMES_CONFIRMED = true           B02_CAST_PAIR = ALYA + ENCIK_RAHMAN
B02_NARRATOR = HILMI                           GENERIC_ROLE_LABELS_USED_AS_FINAL_NAMES = 0
PUAN_NADIA_IN_B02_WITHOUT_INSTRUCTIONAL_REASON = 0   PROJECT_MANAGER_NAME_INVENTED = false

PAPAN_TANDA_SPEC_CATEGORIES = 4                BBQ_PIT_SPEC_CATEGORIES = 4
PAPAN_TANDA_SOURCE_ROWS_CREATED = 0            BBQ_PIT_SOURCE_ROWS_CREATED = 0

MS2680_LEARNER_CLAIMS = 0                      MS2680_PENDING_METADATA_RECORDS = 2
MULTIPLE_RESPONSE_OPTIONS_WITH_LETTER_LABELS = 0
QUIZ_IMMEDIATE_FEEDBACK_VARIANTS = 2

GENERATOR_FILES_CHANGED = 0                    POWERPOINT_FILES_GENERATED = 0
COMPONENTS_PROPAGATED = 0                      NEW_CANONICAL_PATTERN_IDS_MINTED = 0
```

Beyond the required totals, the harness also asserts the model's own graph invariants:

| Check | Why it exists |
|---|---|
| `POPUP_PARENT_IS_POPUP = 0` | walks every popup's `parent_screen_id` **and** `return_target` against the set of popup state IDs — a popup that opened another popup would be caught from either direction |
| `RETURN_TARGET_UNRESOLVED = 0` | every `return_target` must resolve to a real screen or state ID, not a plausible-looking string |
| `POPUP_WITHOUT_CLOSE_ICON` / `NON_POPUP_WITH_CLOSE_ICON` | the close icon belongs to popup states and nowhere else |
| `DUPLICATE_CANVAS_NEXT = 0` | no record may declare a canvas-authored next control where the shell owns progression |
| family return-target contracts | Family S `Kembali` → group master; P1 close → example detail; P1 `Kembali` → component list; P2 close → specification list — each asserted by ID suffix across every matching record |
| `ALL_VIEWED_STATES_NOT_SILENT = 0` | every completion and all-viewed state must carry `SILENT_STATE_NOTES` |
| `FORBIDDEN_TOKENS_IN_NOTES_HEADERS = 0` | no `VO PENUH:`, `PERINCIAN`, `ST_` or `RP-` token may leak into a modelled Notes header |
| `PLACEHOLDER_NAMA_TOKEN_REMAINS = 0` | the retired `[Nama]` placeholder appears nowhere in the model |
| `REVIEW_PAGE_NUMBERS_ASSIGNED = 0` | no record carries an `RP-nnn` page number — roles only |


---

# 10. Standing

Documentation only. No generator modified, no PowerPoint generated or edited, no component
propagated, no multimedia created, no final visual asset bound, no canonical `P#` minted. MMD
readiness, production approval and canonical approval are **not** claimed. `B02-CAIR-INT-001` remains
open; `SOURCE_INTEGRITY_FULLY_VERIFIED` is not asserted.
