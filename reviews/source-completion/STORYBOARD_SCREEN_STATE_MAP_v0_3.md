# STORYBOARD_SCREEN_STATE_MAP — K5 PL06 T03 B02 v0.3

```
REVIEW_READY · PROVISIONAL_CAIR_EXECUTION
CAIR_INTEGRITY_EXCEPTION_FOR_REVIEW_BUILD_ONLY · PENDING_FINAL_BARIAH_CONFIRMATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
Generated from b02_model_v0_3.py — do not hand-edit.
```

## 0. Three things this map keeps separate

| Term | Meaning | Count |
|---|---|---:|
| **Physical learner screen** | a page the learner navigates to | **26** |
| **Runtime state** | a variable the player holds — not a page | **46** |
| **Resolved PowerPoint review page** | a page produced so the state can be *seen* during review | **63** |

A **popup is a runtime state of its example screen**. It is never a Level 3 destination.
**Maximum learner navigation depth = 2** (Level 1 group master → Level 2 example screen).

Review pages exist only for this review build. They are not learner screens and they
do not change the learner's navigation depth.

## 1. Physical learner screens

| # | Screen ID | Kind | Learner title | Level | Parent | Navigation target |
|---:|---|---|---|:-:|---|---|
| 1 | `S01` | FRAME | Komponen Landskap | — | — | `S02` |
| 2 | `S02` | FRAME | Pengenalan / Komponen Landskap | — | — | `S03` |
| 3 | `S03` | FRAME | Gambaran Keseluruhan | — | — | `STRUKTUR_TAMAN_MASTER` |
| 4 | `STRUKTUR_TAMAN_MASTER` | GROUP_MASTER | Struktur Taman | 1 | — | `PERABOT_TAMAN_MASTER` |
| 5 | `STRUKTUR_PERSISIR_AIR_MAIN` | MAIN | Struktur Persisir Air | 1 child | `STRUKTUR_TAMAN_MASTER` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` |
| 6 | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | EXAMPLES | Contoh Struktur Persisir Air | 2 | `STRUKTUR_TAMAN_MASTER` | `STRUKTUR_TAMAN_MASTER` |
| 7 | `STRUKTUR_TEDUHAN_MAIN` | MAIN | Struktur Teduhan | 1 child | `STRUKTUR_TAMAN_MASTER` | `STRUKTUR_TEDUHAN_EXAMPLES` |
| 8 | `STRUKTUR_TEDUHAN_EXAMPLES` | EXAMPLES | Contoh Struktur Teduhan | 2 | `STRUKTUR_TAMAN_MASTER` | `STRUKTUR_TAMAN_MASTER` |
| 9 | `KEMUDAHAN_AWAM_MAIN` | MAIN | Kemudahan Awam | 1 child | `STRUKTUR_TAMAN_MASTER` | `KEMUDAHAN_AWAM_EXAMPLES` |
| 10 | `KEMUDAHAN_AWAM_EXAMPLES` | EXAMPLES | Contoh Kemudahan Awam | 2 | `STRUKTUR_TAMAN_MASTER` | `STRUKTUR_TAMAN_MASTER` |
| 11 | `WATER_FEATURE_MAIN` | MAIN | Water Feature | 1 child | `STRUKTUR_TAMAN_MASTER` | `WATER_FEATURE_EXAMPLES` |
| 12 | `WATER_FEATURE_EXAMPLES` | EXAMPLES | Contoh Water Feature | 2 | `STRUKTUR_TAMAN_MASTER` | `STRUKTUR_TAMAN_MASTER` |
| 13 | `PERABOT_TAMAN_MASTER` | GROUP_MASTER | Perabot Taman | 1 | — | `RUMUSAN` |
| 14 | `KERUSI_TAMAN_MAIN` | MAIN | Kerusi Taman | 1 child | `PERABOT_TAMAN_MASTER` | `KERUSI_TAMAN_EXAMPLES` |
| 15 | `KERUSI_TAMAN_EXAMPLES` | EXAMPLES | Contoh Kerusi Taman | 2 | `PERABOT_TAMAN_MASTER` | `PERABOT_TAMAN_MASTER` |
| 16 | `PAPAN_TANDA_MAIN` | MAIN | Papan Tanda | 1 child | `PERABOT_TAMAN_MASTER` | `PAPAN_TANDA_EXAMPLES` |
| 17 | `PAPAN_TANDA_EXAMPLES` | EXAMPLES | Contoh Papan Tanda | 2 | `PERABOT_TAMAN_MASTER` | `PERABOT_TAMAN_MASTER` |
| 18 | `TONG_SAMPAH_MAIN` | MAIN | Tong Sampah | 1 child | `PERABOT_TAMAN_MASTER` | `TONG_SAMPAH_EXAMPLES` |
| 19 | `TONG_SAMPAH_EXAMPLES` | EXAMPLES | Contoh Tong Sampah | 2 | `PERABOT_TAMAN_MASTER` | `PERABOT_TAMAN_MASTER` |
| 20 | `DRINKING_FOUNTAIN_MAIN` | MAIN | Drinking Fountain | 1 child | `PERABOT_TAMAN_MASTER` | `DRINKING_FOUNTAIN_EXAMPLES` |
| 21 | `DRINKING_FOUNTAIN_EXAMPLES` | EXAMPLES | Contoh Drinking Fountain | 2 | `PERABOT_TAMAN_MASTER` | `PERABOT_TAMAN_MASTER` |
| 22 | `BBQ_PIT_MAIN` | MAIN | BBQ Pit | 1 child | `PERABOT_TAMAN_MASTER` | `BBQ_PIT_EXAMPLES` |
| 23 | `BBQ_PIT_EXAMPLES` | EXAMPLES | Contoh BBQ Pit | 2 | `PERABOT_TAMAN_MASTER` | `PERABOT_TAMAN_MASTER` |
| 24 | `RUMUSAN` | FRAME | Rumusan | — | — | `KUIZ` |
| 25 | `KUIZ` | FRAME | Kuiz | — | — | `TAMAT` |
| 26 | `TAMAT` | FRAME | Tamat Bahagian | — | — | `[route pending — production metadata only]` |

## 2. Runtime states

| State ID | Kind | Owning screen | Derived rule | Enables | Persistent |
|---|---|---|---|---|:-:|
| `main_vo_complete[STRUKTUR_PERSISIR_AIR]` | VO_GATE | `STRUKTUR_PERSISIR_AIR_MAIN` | true when the main explanation VO ends | Seterusnya -> STRUKTUR_PERSISIR_AIR_EXAMPLES | yes |
| `item_viewed[STRUKTUR_PERSISIR_AIR_EXAMPLE_01]` | ITEM_VIEWED | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | true once popup STRUKTUR_PERSISIR_AIR_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `item_viewed[STRUKTUR_PERSISIR_AIR_EXAMPLE_02]` | ITEM_VIEWED | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | true once popup STRUKTUR_PERSISIR_AIR_EXAMPLE_02 has been viewed | Level 2 tick | yes |
| `item_viewed[STRUKTUR_PERSISIR_AIR_EXAMPLE_03]` | ITEM_VIEWED | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | true once popup STRUKTUR_PERSISIR_AIR_EXAMPLE_03 has been viewed | Level 2 tick | yes |
| `item_viewed[STRUKTUR_PERSISIR_AIR_EXAMPLE_04]` | ITEM_VIEWED | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | true once popup STRUKTUR_PERSISIR_AIR_EXAMPLE_04 has been viewed | Level 2 tick | yes |
| `item_viewed[STRUKTUR_PERSISIR_AIR_EXAMPLE_05]` | ITEM_VIEWED | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | true once popup STRUKTUR_PERSISIR_AIR_EXAMPLE_05 has been viewed | Level 2 tick | yes |
| `component_complete[STRUKTUR_PERSISIR_AIR]` | COMPONENT_COMPLETE | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `main_vo_complete[STRUKTUR_TEDUHAN]` | VO_GATE | `STRUKTUR_TEDUHAN_MAIN` | true when the main explanation VO ends | Seterusnya -> STRUKTUR_TEDUHAN_EXAMPLES | yes |
| `item_viewed[STRUKTUR_TEDUHAN_EXAMPLE_01]` | ITEM_VIEWED | `STRUKTUR_TEDUHAN_EXAMPLES` | true once popup STRUKTUR_TEDUHAN_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `item_viewed[STRUKTUR_TEDUHAN_EXAMPLE_02]` | ITEM_VIEWED | `STRUKTUR_TEDUHAN_EXAMPLES` | true once popup STRUKTUR_TEDUHAN_EXAMPLE_02 has been viewed | Level 2 tick | yes |
| `item_viewed[STRUKTUR_TEDUHAN_EXAMPLE_03]` | ITEM_VIEWED | `STRUKTUR_TEDUHAN_EXAMPLES` | true once popup STRUKTUR_TEDUHAN_EXAMPLE_03 has been viewed | Level 2 tick | yes |
| `item_viewed[STRUKTUR_TEDUHAN_EXAMPLE_04]` | ITEM_VIEWED | `STRUKTUR_TEDUHAN_EXAMPLES` | true once popup STRUKTUR_TEDUHAN_EXAMPLE_04 has been viewed | Level 2 tick | yes |
| `item_viewed[STRUKTUR_TEDUHAN_EXAMPLE_05]` | ITEM_VIEWED | `STRUKTUR_TEDUHAN_EXAMPLES` | true once popup STRUKTUR_TEDUHAN_EXAMPLE_05 has been viewed | Level 2 tick | yes |
| `component_complete[STRUKTUR_TEDUHAN]` | COMPONENT_COMPLETE | `STRUKTUR_TEDUHAN_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `main_vo_complete[KEMUDAHAN_AWAM]` | VO_GATE | `KEMUDAHAN_AWAM_MAIN` | true when the main explanation VO ends | Seterusnya -> KEMUDAHAN_AWAM_EXAMPLES | yes |
| `item_viewed[KEMUDAHAN_AWAM_EXAMPLE_01]` | ITEM_VIEWED | `KEMUDAHAN_AWAM_EXAMPLES` | true once popup KEMUDAHAN_AWAM_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `item_viewed[KEMUDAHAN_AWAM_EXAMPLE_02]` | ITEM_VIEWED | `KEMUDAHAN_AWAM_EXAMPLES` | true once popup KEMUDAHAN_AWAM_EXAMPLE_02 has been viewed | Level 2 tick | yes |
| `item_viewed[KEMUDAHAN_AWAM_EXAMPLE_03]` | ITEM_VIEWED | `KEMUDAHAN_AWAM_EXAMPLES` | true once popup KEMUDAHAN_AWAM_EXAMPLE_03 has been viewed | Level 2 tick | yes |
| `component_complete[KEMUDAHAN_AWAM]` | COMPONENT_COMPLETE | `KEMUDAHAN_AWAM_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `main_vo_complete[WATER_FEATURE]` | VO_GATE | `WATER_FEATURE_MAIN` | true when the main explanation VO ends | Seterusnya -> WATER_FEATURE_EXAMPLES | yes |
| `item_viewed[WATER_FEATURE_EXAMPLE_01]` | ITEM_VIEWED | `WATER_FEATURE_EXAMPLES` | true once popup WATER_FEATURE_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `item_viewed[WATER_FEATURE_EXAMPLE_02]` | ITEM_VIEWED | `WATER_FEATURE_EXAMPLES` | true once popup WATER_FEATURE_EXAMPLE_02 has been viewed | Level 2 tick | yes |
| `item_viewed[WATER_FEATURE_EXAMPLE_03]` | ITEM_VIEWED | `WATER_FEATURE_EXAMPLES` | true once popup WATER_FEATURE_EXAMPLE_03 has been viewed | Level 2 tick | yes |
| `component_complete[WATER_FEATURE]` | COMPONENT_COMPLETE | `WATER_FEATURE_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `main_vo_complete[KERUSI_TAMAN]` | VO_GATE | `KERUSI_TAMAN_MAIN` | true when the main explanation VO ends | Seterusnya -> KERUSI_TAMAN_EXAMPLES | yes |
| `item_viewed[KERUSI_TAMAN_EXAMPLE_01]` | ITEM_VIEWED | `KERUSI_TAMAN_EXAMPLES` | true once popup KERUSI_TAMAN_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `item_viewed[KERUSI_TAMAN_EXAMPLE_02]` | ITEM_VIEWED | `KERUSI_TAMAN_EXAMPLES` | true once popup KERUSI_TAMAN_EXAMPLE_02 has been viewed | Level 2 tick | yes |
| `item_viewed[KERUSI_TAMAN_EXAMPLE_03]` | ITEM_VIEWED | `KERUSI_TAMAN_EXAMPLES` | true once popup KERUSI_TAMAN_EXAMPLE_03 has been viewed | Level 2 tick | yes |
| `component_complete[KERUSI_TAMAN]` | COMPONENT_COMPLETE | `KERUSI_TAMAN_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `main_vo_complete[PAPAN_TANDA]` | VO_GATE | `PAPAN_TANDA_MAIN` | true when the main explanation VO ends | Seterusnya -> PAPAN_TANDA_EXAMPLES | yes |
| `item_viewed[PAPAN_TANDA_EXAMPLE_01]` | ITEM_VIEWED | `PAPAN_TANDA_EXAMPLES` | true once popup PAPAN_TANDA_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `component_complete[PAPAN_TANDA]` | COMPONENT_COMPLETE | `PAPAN_TANDA_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `main_vo_complete[TONG_SAMPAH]` | VO_GATE | `TONG_SAMPAH_MAIN` | true when the main explanation VO ends | Seterusnya -> TONG_SAMPAH_EXAMPLES | yes |
| `item_viewed[TONG_SAMPAH_EXAMPLE_01]` | ITEM_VIEWED | `TONG_SAMPAH_EXAMPLES` | true once popup TONG_SAMPAH_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `item_viewed[TONG_SAMPAH_EXAMPLE_02]` | ITEM_VIEWED | `TONG_SAMPAH_EXAMPLES` | true once popup TONG_SAMPAH_EXAMPLE_02 has been viewed | Level 2 tick | yes |
| `item_viewed[TONG_SAMPAH_EXAMPLE_03]` | ITEM_VIEWED | `TONG_SAMPAH_EXAMPLES` | true once popup TONG_SAMPAH_EXAMPLE_03 has been viewed | Level 2 tick | yes |
| `component_complete[TONG_SAMPAH]` | COMPONENT_COMPLETE | `TONG_SAMPAH_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `main_vo_complete[DRINKING_FOUNTAIN]` | VO_GATE | `DRINKING_FOUNTAIN_MAIN` | true when the main explanation VO ends | Seterusnya -> DRINKING_FOUNTAIN_EXAMPLES | yes |
| `item_viewed[DRINKING_FOUNTAIN_EXAMPLE_01]` | ITEM_VIEWED | `DRINKING_FOUNTAIN_EXAMPLES` | true once popup DRINKING_FOUNTAIN_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `item_viewed[DRINKING_FOUNTAIN_EXAMPLE_02]` | ITEM_VIEWED | `DRINKING_FOUNTAIN_EXAMPLES` | true once popup DRINKING_FOUNTAIN_EXAMPLE_02 has been viewed | Level 2 tick | yes |
| `component_complete[DRINKING_FOUNTAIN]` | COMPONENT_COMPLETE | `DRINKING_FOUNTAIN_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `main_vo_complete[BBQ_PIT]` | VO_GATE | `BBQ_PIT_MAIN` | true when the main explanation VO ends | Seterusnya -> BBQ_PIT_EXAMPLES | yes |
| `item_viewed[BBQ_PIT_EXAMPLE_01]` | ITEM_VIEWED | `BBQ_PIT_EXAMPLES` | true once popup BBQ_PIT_EXAMPLE_01 has been viewed | Level 2 tick | yes |
| `component_complete[BBQ_PIT]` | COMPONENT_COMPLETE | `BBQ_PIT_EXAMPLES` | all item_viewed for this component are true | Kembali; on return, Level 1 card tick | yes |
| `group_complete[STRUKTUR_TAMAN]` | GROUP_COMPLETE | `STRUKTUR_TAMAN_MASTER` | all component_complete for STRUKTUR_PERSISIR_AIR, STRUKTUR_TEDUHAN, KEMUDAHAN_AWAM, WATER_FEATURE are true | global Seterusnya | yes |
| `group_complete[PERABOT_TAMAN]` | GROUP_COMPLETE | `PERABOT_TAMAN_MASTER` | all component_complete for KERUSI_TAMAN, PAPAN_TANDA, TONG_SAMPAH, DRINKING_FOUNTAIN, BBQ_PIT are true | global Seterusnya | yes |

**Persistence rule (all states):** once true, a state stays true. Once `Kembali` or the
global `Seterusnya` is enabled it **must not relock** on revisit or LMS resume.

## 3. Popup states — one per source row

| Popup state ID | Parent example screen | Source row UID | Source locator | Item label | VO locator |
|---|---|---|---|---|---|
| `STRUKTUR_PERSISIR_AIR_EXAMPLE_01` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-01` | modul ms 238 (fizikal 257) | Promenade | Notes of review page for `STRUKTUR_PERSISIR_AIR_EXAMPLE_01` |
| `STRUKTUR_PERSISIR_AIR_EXAMPLE_02` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-02` | modul ms 238 (fizikal 257) | Jeti | Notes of review page for `STRUKTUR_PERSISIR_AIR_EXAMPLE_02` |
| `STRUKTUR_PERSISIR_AIR_EXAMPLE_03` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-03` | modul ms 238 (fizikal 257) | Dek Kayu | Notes of review page for `STRUKTUR_PERSISIR_AIR_EXAMPLE_03` |
| `STRUKTUR_PERSISIR_AIR_EXAMPLE_04` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-04` | modul ms 238 (fizikal 257) | Boardwalk | Notes of review page for `STRUKTUR_PERSISIR_AIR_EXAMPLE_04` |
| `STRUKTUR_PERSISIR_AIR_EXAMPLE_05` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-05` | modul ms 238 (fizikal 257) | Footbridge | Notes of review page for `STRUKTUR_PERSISIR_AIR_EXAMPLE_05` |
| `STRUKTUR_TEDUHAN_EXAMPLE_01` | `STRUKTUR_TEDUHAN_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-01` | modul ms 239 (fizikal 258) | Gazebo | Notes of review page for `STRUKTUR_TEDUHAN_EXAMPLE_01` |
| `STRUKTUR_TEDUHAN_EXAMPLE_02` | `STRUKTUR_TEDUHAN_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-02` | modul ms 239 (fizikal 258) | Wakaf | Notes of review page for `STRUKTUR_TEDUHAN_EXAMPLE_02` |
| `STRUKTUR_TEDUHAN_EXAMPLE_03` | `STRUKTUR_TEDUHAN_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-03` | modul ms 239 (fizikal 258) | Pergola | Notes of review page for `STRUKTUR_TEDUHAN_EXAMPLE_03` |
| `STRUKTUR_TEDUHAN_EXAMPLE_04` | `STRUKTUR_TEDUHAN_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-04` | modul ms 239 (fizikal 258) | Canopy | Notes of review page for `STRUKTUR_TEDUHAN_EXAMPLE_04` |
| `STRUKTUR_TEDUHAN_EXAMPLE_05` | `STRUKTUR_TEDUHAN_EXAMPLES` | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-05` | modul ms 239 (fizikal 258) | Struktur Teduhan Moden | Notes of review page for `STRUKTUR_TEDUHAN_EXAMPLE_05` |
| `KEMUDAHAN_AWAM_EXAMPLE_01` | `KEMUDAHAN_AWAM_EXAMPLES` | `K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-01` | modul ms 240 (fizikal 259) | Tandas Awam | Notes of review page for `KEMUDAHAN_AWAM_EXAMPLE_01` |
| `KEMUDAHAN_AWAM_EXAMPLE_02` | `KEMUDAHAN_AWAM_EXAMPLES` | `K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-02` | modul ms 240 (fizikal 259) | Surau | Notes of review page for `KEMUDAHAN_AWAM_EXAMPLE_02` |
| `KEMUDAHAN_AWAM_EXAMPLE_03` | `KEMUDAHAN_AWAM_EXAMPLES` | `K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-03` | modul ms 240 (fizikal 259) | Bangunan Interpretatif | Notes of review page for `KEMUDAHAN_AWAM_EXAMPLE_03` |
| `WATER_FEATURE_EXAMPLE_01` | `WATER_FEATURE_EXAMPLES` | `K5-PL06-T03-B02-WATER-FEATURE-ROW-01` | modul ms 241 (fizikal 260) | Air Pancut (Fountain) | Notes of review page for `WATER_FEATURE_EXAMPLE_01` |
| `WATER_FEATURE_EXAMPLE_02` | `WATER_FEATURE_EXAMPLES` | `K5-PL06-T03-B02-WATER-FEATURE-ROW-02` | modul ms 241 (fizikal 260) | Kolam (Pond) | Notes of review page for `WATER_FEATURE_EXAMPLE_02` |
| `WATER_FEATURE_EXAMPLE_03` | `WATER_FEATURE_EXAMPLES` | `K5-PL06-T03-B02-WATER-FEATURE-ROW-03` | modul ms 241 (fizikal 260) | Kolam Renang / Kolam Hiasan Besar (Pool) | Notes of review page for `WATER_FEATURE_EXAMPLE_03` |
| `KERUSI_TAMAN_EXAMPLE_01` | `KERUSI_TAMAN_EXAMPLES` | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-01` | modul ms 242 (fizikal 261) | Kerusi Kayu Keras | Notes of review page for `KERUSI_TAMAN_EXAMPLE_01` |
| `KERUSI_TAMAN_EXAMPLE_02` | `KERUSI_TAMAN_EXAMPLES` | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-02` | modul ms 243 (fizikal 262) | Kerusi Konkrit | Notes of review page for `KERUSI_TAMAN_EXAMPLE_02` |
| `KERUSI_TAMAN_EXAMPLE_03` | `KERUSI_TAMAN_EXAMPLES` | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-03` | modul ms 243 (fizikal 262) | Kerusi Komposit | Notes of review page for `KERUSI_TAMAN_EXAMPLE_03` |
| `PAPAN_TANDA_EXAMPLE_01` | `PAPAN_TANDA_EXAMPLES` | `K5-PL06-T03-B02-PAPAN-TANDA-ROW-01` | modul ms 244 (fizikal 263) | Papan Tanda Arah / Papan Tanda Interpretatif | Notes of review page for `PAPAN_TANDA_EXAMPLE_01` |
| `TONG_SAMPAH_EXAMPLE_01` | `TONG_SAMPAH_EXAMPLES` | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-01` | modul ms 246 (fizikal 265) | Tong Sampah Logam | Notes of review page for `TONG_SAMPAH_EXAMPLE_01` |
| `TONG_SAMPAH_EXAMPLE_02` | `TONG_SAMPAH_EXAMPLES` | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-02` | modul ms 246 (fizikal 265) | Tong Sampah Konkrit/Batu | Notes of review page for `TONG_SAMPAH_EXAMPLE_02` |
| `TONG_SAMPAH_EXAMPLE_03` | `TONG_SAMPAH_EXAMPLES` | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-03` | modul ms 247 (fizikal 266) | Tong Sampah Plastik Kitar Semula (HDPE) | Notes of review page for `TONG_SAMPAH_EXAMPLE_03` |
| `DRINKING_FOUNTAIN_EXAMPLE_01` | `DRINKING_FOUNTAIN_EXAMPLES` | `K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-01` | modul ms 248 (fizikal 267) | Pancutan Air Minum Keluli Tahan Karat | Notes of review page for `DRINKING_FOUNTAIN_EXAMPLE_01` |
| `DRINKING_FOUNTAIN_EXAMPLE_02` | `DRINKING_FOUNTAIN_EXAMPLES` | `K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-02` | modul ms 248 (fizikal 267) | Pancutan Air Minum Konkrit/Batu | Notes of review page for `DRINKING_FOUNTAIN_EXAMPLE_02` |
| `BBQ_PIT_EXAMPLE_01` | `BBQ_PIT_EXAMPLES` | `K5-PL06-T03-B02-BBQ-PIT-ROW-01` | modul ms 249 (fizikal 268) | BBQ Pit Struktur Kekal | Notes of review page for `BBQ_PIT_EXAMPLE_01` |

**26 popup states, 26 distinct source rows, every parent an example screen.** No source row maps to two popups; no popup lacks a parent.

## 4. Enable / disable conditions

| Control | Screen | Starts | Enables when | Target |
|---|---|---|---|---|
| `Seterusnya` | main explanation | disabled | `main_vo_complete[component]` | example screen |
| `Tutup` | popup state | enabled | always | back to the same example screen |
| `Kembali` | example screen | **disabled** | all `item_viewed` for the component | Level 1 group master |
| `Seterusnya` (global) | group master | **disabled** | `group_complete[group]` | next group / Rumusan |
| `MULA` | S01 | enabled | always | S02 |

## 5. Review page index

| Review page | Screen | Variant | Shows |
|---|---|---|---|
| `RP-001` | `S01` | BASE | skrin tajuk |
| `RP-002` | `S02` | BASE | senario tapak |
| `RP-003` | `S03` | BASE | narator + mind map |
| `RP-004` | `STRUKTUR_TAMAN_MASTER` | BASE | Level 1 — tiada kad selesai |
| `RP-005` | `STRUKTUR_PERSISIR_AIR_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-006` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-007` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | POPUP | popup — Promenade |
| `RP-008` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | POPUP | popup — Jeti |
| `RP-009` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | POPUP | popup — Dek Kayu |
| `RP-010` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | POPUP | popup — Boardwalk |
| `RP-011` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | POPUP | popup — Footbridge |
| `RP-012` | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-013` | `STRUKTUR_TEDUHAN_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-014` | `STRUKTUR_TEDUHAN_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-015` | `STRUKTUR_TEDUHAN_EXAMPLES` | POPUP | popup — Gazebo |
| `RP-016` | `STRUKTUR_TEDUHAN_EXAMPLES` | POPUP | popup — Wakaf |
| `RP-017` | `STRUKTUR_TEDUHAN_EXAMPLES` | POPUP | popup — Pergola |
| `RP-018` | `STRUKTUR_TEDUHAN_EXAMPLES` | POPUP | popup — Canopy |
| `RP-019` | `STRUKTUR_TEDUHAN_EXAMPLES` | POPUP | popup — Struktur Teduhan Moden |
| `RP-020` | `STRUKTUR_TEDUHAN_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-021` | `KEMUDAHAN_AWAM_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-022` | `KEMUDAHAN_AWAM_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-023` | `KEMUDAHAN_AWAM_EXAMPLES` | POPUP | popup — Tandas Awam |
| `RP-024` | `KEMUDAHAN_AWAM_EXAMPLES` | POPUP | popup — Surau |
| `RP-025` | `KEMUDAHAN_AWAM_EXAMPLES` | POPUP | popup — Bangunan Interpretatif |
| `RP-026` | `KEMUDAHAN_AWAM_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-027` | `WATER_FEATURE_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-028` | `WATER_FEATURE_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-029` | `WATER_FEATURE_EXAMPLES` | POPUP | popup — Air Pancut (Fountain) |
| `RP-030` | `WATER_FEATURE_EXAMPLES` | POPUP | popup — Kolam (Pond) |
| `RP-031` | `WATER_FEATURE_EXAMPLES` | POPUP | popup — Kolam Renang / Kolam Hiasan Besar (Pool) |
| `RP-032` | `WATER_FEATURE_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-033` | `STRUKTUR_TAMAN_MASTER` | GROUP_COMPLETE | Level 1 — semua kad selesai, Seterusnya dibuka |
| `RP-034` | `PERABOT_TAMAN_MASTER` | BASE | Level 1 — tiada kad selesai |
| `RP-035` | `KERUSI_TAMAN_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-036` | `KERUSI_TAMAN_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-037` | `KERUSI_TAMAN_EXAMPLES` | POPUP | popup — Kerusi Kayu Keras |
| `RP-038` | `KERUSI_TAMAN_EXAMPLES` | POPUP | popup — Kerusi Konkrit |
| `RP-039` | `KERUSI_TAMAN_EXAMPLES` | POPUP | popup — Kerusi Komposit |
| `RP-040` | `KERUSI_TAMAN_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-041` | `PAPAN_TANDA_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-042` | `PAPAN_TANDA_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-043` | `PAPAN_TANDA_EXAMPLES` | POPUP | popup — Papan Tanda Arah / Papan Tanda Interpretatif |
| `RP-044` | `PAPAN_TANDA_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-045` | `TONG_SAMPAH_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-046` | `TONG_SAMPAH_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-047` | `TONG_SAMPAH_EXAMPLES` | POPUP | popup — Tong Sampah Logam |
| `RP-048` | `TONG_SAMPAH_EXAMPLES` | POPUP | popup — Tong Sampah Konkrit/Batu |
| `RP-049` | `TONG_SAMPAH_EXAMPLES` | POPUP | popup — Tong Sampah Plastik Kitar Semula (HDPE) |
| `RP-050` | `TONG_SAMPAH_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-051` | `DRINKING_FOUNTAIN_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-052` | `DRINKING_FOUNTAIN_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-053` | `DRINKING_FOUNTAIN_EXAMPLES` | POPUP | popup — Pancutan Air Minum Keluli Tahan Karat |
| `RP-054` | `DRINKING_FOUNTAIN_EXAMPLES` | POPUP | popup — Pancutan Air Minum Konkrit/Batu |
| `RP-055` | `DRINKING_FOUNTAIN_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-056` | `BBQ_PIT_MAIN` | BASE | penerangan utama — Seterusnya dikunci sehingga VO tamat |
| `RP-057` | `BBQ_PIT_EXAMPLES` | BASE | Level 2 — tiada item dilihat |
| `RP-058` | `BBQ_PIT_EXAMPLES` | POPUP | popup — BBQ Pit Struktur Kekal |
| `RP-059` | `BBQ_PIT_EXAMPLES` | ALL_VIEWED | Level 2 — semua item dilihat, Kembali dibuka |
| `RP-060` | `PERABOT_TAMAN_MASTER` | GROUP_COMPLETE | Level 1 — semua kad selesai, Seterusnya dibuka |
| `RP-061` | `RUMUSAN` | BASE | rumusan bahagian |
| `RP-062` | `KUIZ` | BASE | 5 item — 4 MCQ + 1 Multiple Response |
| `RP-063` | `TAMAT` | BASE | penutup bahagian |

## 6. Reconciliation

```
PHYSICAL_LEARNER_SCREENS      = 26
RUNTIME_STATES                = 46
REVIEW_PAGES                  = 63
POPUP_STATES                  = 26
SOURCE_ROWS                   = 26
MAX_LEARNER_NAVIGATION_DEPTH  = 2
```
