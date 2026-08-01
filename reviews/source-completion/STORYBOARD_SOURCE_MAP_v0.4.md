# STORYBOARD_SOURCE_MAP — K5 PL06 T03 B02 v0.4

```
SOURCE_ROW_COUNT = 26 · ALL BOUND
SOURCE_ASSET_COUNT = 14 · ALL BOUND
SOURCE_ROWS_CHANGED = 0 · DUPLICATE_SOURCE_ROW_UID = 0
INTERACTION_ITEMS = 54 · INTERACTION_ITEMS_WITHOUT_SOURCE_BINDING = 0
DOCS_ONLY · GENERATOR_UNTOUCHED · NO_POWERPOINT_GENERATED
```

Binds every module source row and every extracted source asset to the v0.4 model. The direction of
travel is one-way: **source → interaction item → runtime state**. Nothing in the model creates,
renames or renumbers a source row.

---

# 0. Upstream narrative context — not source

Two Bariah-supplied montages precede B02: `SB_K5_montaj_v1.pptx` (Course Montage) and
`SB_K5PL6_montaj_v1.pptx` (PL06 Montage). They are classified `UPSTREAM_NARRATIVE_CONTEXT`.

**They contribute no source rows and no source assets.** They are prerequisites to the learner flow,
not module content: the 26 rows and 14 assets below are unchanged by them, and neither montage appears
as a screen, a state, an interaction item or a source binding anywhere in this map.

What they do change is what B02 may *say*: the course introduction, the eight Pakej Latihan, the PL06
objectives, the seven PL06 topics and Hilmi's self-introduction are all already delivered upstream and
must not be repeated here. Recorded as `B02-D-25`.

Their byte freeze is outstanding — see `B02_V0_4_INPUT_FREEZE.md` §2B and `B02-D-27`.


---

# 1. Source-row binding — all 26

| # | source_row_uid | component | family | label | locator | interaction items | states |
|---:|---|---|---|---|---|---:|---:|
| 1 | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-01` | Struktur Persisir Air | `FAMILY_S` | Promenade | modul ms 238 | 1 | 1 |
| 2 | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-02` | Struktur Persisir Air | `FAMILY_S` | Jeti | modul ms 238 | 1 | 1 |
| 3 | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-03` | Struktur Persisir Air | `FAMILY_S` | Dek Kayu | modul ms 238 | 1 | 1 |
| 4 | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-04` | Struktur Persisir Air | `FAMILY_S` | Boardwalk | modul ms 238 | 1 | 1 |
| 5 | `K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-05` | Struktur Persisir Air | `FAMILY_S` | Footbridge | modul ms 238 | 1 | 1 |
| 6 | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-01` | Struktur Teduhan | `FAMILY_S` | Gazebo | modul ms 239 | 1 | 1 |
| 7 | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-02` | Struktur Teduhan | `FAMILY_S` | Wakaf | modul ms 239 | 1 | 1 |
| 8 | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-03` | Struktur Teduhan | `FAMILY_S` | Pergola | modul ms 239 | 1 | 1 |
| 9 | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-04` | Struktur Teduhan | `FAMILY_S` | Canopy | modul ms 239 | 1 | 1 |
| 10 | `K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-05` | Struktur Teduhan | `FAMILY_S` | Struktur Teduhan Moden | modul ms 239 | 1 | 1 |
| 11 | `K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-01` | Kemudahan Awam | `FAMILY_S` | Tandas Awam | modul ms 240 | 1 | 1 |
| 12 | `K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-02` | Kemudahan Awam | `FAMILY_S` | Surau | modul ms 240 | 1 | 1 |
| 13 | `K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-03` | Kemudahan Awam | `FAMILY_S` | Bangunan Interpretatif | modul ms 240 | 1 | 1 |
| 14 | `K5-PL06-T03-B02-WATER-FEATURE-ROW-01` | Water Feature | `FAMILY_S` | Air Pancut (Fountain) | modul ms 241 | 1 | 1 |
| 15 | `K5-PL06-T03-B02-WATER-FEATURE-ROW-02` | Water Feature | `FAMILY_S` | Kolam (Pond) | modul ms 241 | 1 | 1 |
| 16 | `K5-PL06-T03-B02-WATER-FEATURE-ROW-03` | Water Feature | `FAMILY_S` | Kolam Renang / Kolam Hiasan Besar (Pool) | modul ms 241 | 1 | 1 |
| 17 | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-01` | Kerusi Taman | `FAMILY_P1` | Kerusi Kayu Keras | modul ms 242 | 5 | 4 |
| 18 | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-02` | Kerusi Taman | `FAMILY_P1` | Kerusi Konkrit | modul ms 243 | 3 | 2 |
| 19 | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-03` | Kerusi Taman | `FAMILY_P1` | Kerusi Komposit | modul ms 243 | 3 | 2 |
| 20 | `K5-PL06-T03-B02-PAPAN-TANDA-ROW-01` | Papan Tanda | `FAMILY_P2` | Papan Tanda Arah / Papan Tanda Interpretatif | modul ms 244 | 4 | 4 |
| 21 | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-01` | Tong Sampah | `FAMILY_P1` | Tong Sampah Logam | modul ms 246 | 3 | 2 |
| 22 | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-02` | Tong Sampah | `FAMILY_P1` | Tong Sampah Konkrit/Batu | modul ms 246 | 3 | 2 |
| 23 | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-03` | Tong Sampah | `FAMILY_P1` | Tong Sampah Plastik Kitar Semula (HDPE) | modul ms 247 | 3 | 2 |
| 24 | `K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-01` | Drinking Fountain | `FAMILY_P1` | Pancutan Air Minum Keluli Tahan Karat | modul ms 248 | 7 | 6 |
| 25 | `K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-02` | Drinking Fountain | `FAMILY_P1` | Pancutan Air Minum Konkrit/Batu | modul ms 248 | 3 | 2 |
| 26 | `K5-PL06-T03-B02-BBQ-PIT-ROW-01` | BBQ Pit | `FAMILY_P2` | BBQ Pit Struktur Kekal | modul ms 249 | 4 | 4 |

**Totals: 26 rows · 54 interaction items · 46 popup states.**

---

# 2. Interaction decomposition — where one row yields many items

Three components decompose a single source row into several interaction items. In every case the
row's UID, order and count are untouched.

## Papan Tanda — 1 source row → 4 interaction categories

`K5-PL06-T03-B02-PAPAN-TANDA-ROW-01` · modul ms 244

| # | interaction_item_id | category label | source-attested label | runtime_state_id |
|---:|---|---|---|---|
| 1 | `II_PAPAN_TANDA_CAT01` | **Bahan Panel** | Bahan panel | `ST_PAPAN_TANDA_CAT01` |
| 2 | `II_PAPAN_TANDA_CAT02` | **Bahan Struktur/Tiang** | Bahan struktur/tiang | `ST_PAPAN_TANDA_CAT02` |
| 3 | `II_PAPAN_TANDA_CAT03` | **Grafik** | Grafik | `ST_PAPAN_TANDA_CAT03` |
| 4 | `II_PAPAN_TANDA_CAT04` | **Rekaan** | Rekaan | `ST_PAPAN_TANDA_CAT04` |

> `TECHNICAL_DECOMPOSITION_FROM_SOURCE` — each category is a labelled specification line of the
> module's own fungsi cell for this row. **Papan Tanda source rows created: 0.**

## BBQ Pit — 1 source row → 4 interaction categories

`K5-PL06-T03-B02-BBQ-PIT-ROW-01` · modul ms 249

| # | interaction_item_id | category label | source-attested label | runtime_state_id |
|---:|---|---|---|---|
| 1 | `II_BBQ_PIT_CAT01` | **Bahan Pembinaan** | Bahan pembinaan | `ST_BBQ_PIT_CAT01` |
| 2 | `II_BBQ_PIT_CAT02` | **Dimensi** | Dimensi | `ST_BBQ_PIT_CAT02` |
| 3 | `II_BBQ_PIT_CAT03` | **Gril** | Gril | `ST_BBQ_PIT_CAT03` |
| 4 | `II_BBQ_PIT_CAT04` | **Keselamatan** | Keselamatan | `ST_BBQ_PIT_CAT04` |

> `TECHNICAL_DECOMPOSITION_FROM_SOURCE` — each category is a labelled specification line of the
> module's own fungsi cell for this row. **Bbq Pit source rows created: 0.**

## Family P1 — one row per material, then specification items

| component | source_row_uid | example label | example detail screen | specification items |
|---|---|---|---|---:|
| Kerusi Taman | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-01` | Kerusi Kayu Keras | `SCR_KERUSI_TAMAN_EX01_DETAIL` | 4 |
| Kerusi Taman | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-02` | Kerusi Konkrit | `SCR_KERUSI_TAMAN_EX02_DETAIL` | 2 |
| Kerusi Taman | `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-03` | Kerusi Komposit | `SCR_KERUSI_TAMAN_EX03_DETAIL` | 2 |
| Tong Sampah | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-01` | Tong Sampah Logam | `SCR_TONG_SAMPAH_EX01_DETAIL` | 2 |
| Tong Sampah | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-02` | Tong Sampah Konkrit/Batu | `SCR_TONG_SAMPAH_EX02_DETAIL` | 2 |
| Tong Sampah | `K5-PL06-T03-B02-TONG-SAMPAH-ROW-03` | Tong Sampah Plastik Kitar Semula (HDPE) | `SCR_TONG_SAMPAH_EX03_DETAIL` | 2 |
| Drinking Fountain | `K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-01` | Pancutan Air Minum Keluli Tahan Karat | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | 6 |
| Drinking Fountain | `K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-02` | Pancutan Air Minum Konkrit/Batu | `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` | 2 |

Each specification item names the labelled line it came from, so a reviewer can walk from a popup back
to the exact line of the module table without leaving this document.

---

# 3. Source-asset binding — all 14

| asset_id | module p | bound to | screen |
|---|---:|---|---|
| `K5PL06T03-B02-IMG-p239-x20` | 239 | Rajah 23 — Contoh Boardwalk dalam Taman Paya Bakau | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` |
| `K5PL06T03-B02-IMG-p240-x23` | 240 | Rajah 24 — Contoh Pergola | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` |
| `K5PL06T03-B02-IMG-p242-x28` | 242 | Kerusi Taman — foto jadual spesifikasi (Kerusi Kayu Keras) | `SCR_KERUSI_TAMAN_EX01_DETAIL` |
| `K5PL06T03-B02-IMG-p243-x31` | 243 | Kerusi Taman — foto jadual spesifikasi (Kerusi Konkrit) | `SCR_KERUSI_TAMAN_EX02_DETAIL` |
| `K5PL06T03-B02-IMG-p243-x32` | 243 | Kerusi Taman — foto jadual spesifikasi (Kerusi Komposit/WPC) | `SCR_KERUSI_TAMAN_EX03_DETAIL` |
| `K5PL06T03-B02-IMG-p245-x37` | 245 | Rajah 25 — Contoh Lukisan Spesifikasi Papan Tanda Informasi | `SCR_PAPAN_TANDA_MAIN` |
| `K5PL06T03-B02-IMG-p245-x38` | 245 | Rajah 26 — Contoh Spesifikasi Papan Tanda Penunjuk Arah | `SCR_PAPAN_TANDA_MAIN` |
| `K5PL06T03-B02-IMG-p246-x41` | 246 | Tong Sampah — foto jadual spesifikasi (Logam) | `SCR_TONG_SAMPAH_EX01_DETAIL` |
| `K5PL06T03-B02-IMG-p247-x44` | 247 | Tong Sampah — foto jadual spesifikasi (Konkrit/Batu) | `SCR_TONG_SAMPAH_EX02_DETAIL` |
| `K5PL06T03-B02-IMG-p247-x45` | 247 | Tong Sampah — foto jadual spesifikasi (Plastik HDPE, kiri) | `SCR_TONG_SAMPAH_EX03_DETAIL` |
| `K5PL06T03-B02-IMG-p247-x46` | 247 | Tong Sampah — foto jadual spesifikasi (Plastik HDPE, kanan) | `SCR_TONG_SAMPAH_EX03_DETAIL` |
| `K5PL06T03-B02-IMG-p248-x49` | 248 | Drinking Fountain — foto jadual spesifikasi (Keluli Tahan Karat) | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` |
| `K5PL06T03-B02-IMG-p249-x56` | 249 | Drinking Fountain — foto jadual spesifikasi (Konkrit/Batu) | `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` |
| `K5PL06T03-B02-IMG-p249-x57` | 249 | BBQ pit — foto jadual spesifikasi (Struktur Kekal) | `SCR_BBQ_PIT_MAIN` |

`ORPHAN_SOURCE_ASSETS = 0`. Assets remain **specified, not embedded** — no visual asset is bound to a
rendered deck at this stage.

Two Family S components carry `NO_DEDICATED_SOURCE_IMAGE` in the module (Kemudahan Awam, Water
Feature). That is a source fact, not a gap in this map: their visual direction is a native-diagram
specification, not an extracted asset.

---

# 4. Full interaction-item register — 54 items

| interaction_item_id | kind | family | component | label | source_row_uid | parent screen | sel. level |
|---|---|---|---|---|---|---|:-:|
| `II_STRUKTUR_PERSISIR_AIR_EX01` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Persisir Air | Promenade | `SIR-AIR-ROW-01` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | 1 |
| `II_STRUKTUR_PERSISIR_AIR_EX02` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Persisir Air | Jeti | `SIR-AIR-ROW-02` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | 1 |
| `II_STRUKTUR_PERSISIR_AIR_EX03` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Persisir Air | Dek Kayu | `SIR-AIR-ROW-03` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | 1 |
| `II_STRUKTUR_PERSISIR_AIR_EX04` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Persisir Air | Boardwalk | `SIR-AIR-ROW-04` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | 1 |
| `II_STRUKTUR_PERSISIR_AIR_EX05` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Persisir Air | Footbridge | `SIR-AIR-ROW-05` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | 1 |
| `II_STRUKTUR_TEDUHAN_EX01` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Teduhan | Gazebo | `TEDUHAN-ROW-01` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | 1 |
| `II_STRUKTUR_TEDUHAN_EX02` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Teduhan | Wakaf | `TEDUHAN-ROW-02` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | 1 |
| `II_STRUKTUR_TEDUHAN_EX03` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Teduhan | Pergola | `TEDUHAN-ROW-03` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | 1 |
| `II_STRUKTUR_TEDUHAN_EX04` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Teduhan | Canopy | `TEDUHAN-ROW-04` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | 1 |
| `II_STRUKTUR_TEDUHAN_EX05` | `EXAMPLE_POPUP` | `FAMILY_S` | Struktur Teduhan | Struktur Teduhan Moden | `TEDUHAN-ROW-05` | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | 1 |
| `II_KEMUDAHAN_AWAM_EX01` | `EXAMPLE_POPUP` | `FAMILY_S` | Kemudahan Awam | Tandas Awam | `AN-AWAM-ROW-01` | `SCR_KEMUDAHAN_AWAM_EXAMPLES` | 1 |
| `II_KEMUDAHAN_AWAM_EX02` | `EXAMPLE_POPUP` | `FAMILY_S` | Kemudahan Awam | Surau | `AN-AWAM-ROW-02` | `SCR_KEMUDAHAN_AWAM_EXAMPLES` | 1 |
| `II_KEMUDAHAN_AWAM_EX03` | `EXAMPLE_POPUP` | `FAMILY_S` | Kemudahan Awam | Bangunan Interpretatif | `AN-AWAM-ROW-03` | `SCR_KEMUDAHAN_AWAM_EXAMPLES` | 1 |
| `II_WATER_FEATURE_EX01` | `EXAMPLE_POPUP` | `FAMILY_S` | Water Feature | Air Pancut (Fountain) | `FEATURE-ROW-01` | `SCR_WATER_FEATURE_EXAMPLES` | 1 |
| `II_WATER_FEATURE_EX02` | `EXAMPLE_POPUP` | `FAMILY_S` | Water Feature | Kolam (Pond) | `FEATURE-ROW-02` | `SCR_WATER_FEATURE_EXAMPLES` | 1 |
| `II_WATER_FEATURE_EX03` | `EXAMPLE_POPUP` | `FAMILY_S` | Water Feature | Kolam Renang / Kolam Hiasan Besar (Pool) | `FEATURE-ROW-03` | `SCR_WATER_FEATURE_EXAMPLES` | 1 |
| `II_KERUSI_TAMAN_R01_SPEC01` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Kerusi Taman | Bahan | `I-TAMAN-ROW-01` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | 2 |
| `II_KERUSI_TAMAN_R01_SPEC02` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Kerusi Taman | Dimensi | `I-TAMAN-ROW-01` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | 2 |
| `II_KERUSI_TAMAN_R01_SPEC03` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Kerusi Taman | Penyambungan | `I-TAMAN-ROW-01` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | 2 |
| `II_KERUSI_TAMAN_R01_SPEC04` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Kerusi Taman | Kemasan | `I-TAMAN-ROW-01` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | 2 |
| `II_KERUSI_TAMAN_EX01` | `EXAMPLE_SELECTION` | `FAMILY_P1` | Kerusi Taman | Kerusi Kayu Keras | `I-TAMAN-ROW-01` | `SCR_KERUSI_TAMAN_MAIN` | 1 |
| `II_KERUSI_TAMAN_R02_SPEC01` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Kerusi Taman | Bahan | `I-TAMAN-ROW-02` | `SCR_KERUSI_TAMAN_EX02_DETAIL` | 2 |
| `II_KERUSI_TAMAN_R02_SPEC02` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Kerusi Taman | Kemasan | `I-TAMAN-ROW-02` | `SCR_KERUSI_TAMAN_EX02_DETAIL` | 2 |
| `II_KERUSI_TAMAN_EX02` | `EXAMPLE_SELECTION` | `FAMILY_P1` | Kerusi Taman | Kerusi Konkrit | `I-TAMAN-ROW-02` | `SCR_KERUSI_TAMAN_MAIN` | 1 |
| `II_KERUSI_TAMAN_R03_SPEC01` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Kerusi Taman | Bahan | `I-TAMAN-ROW-03` | `SCR_KERUSI_TAMAN_EX03_DETAIL` | 2 |
| `II_KERUSI_TAMAN_R03_SPEC02` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Kerusi Taman | Kemasan | `I-TAMAN-ROW-03` | `SCR_KERUSI_TAMAN_EX03_DETAIL` | 2 |
| `II_KERUSI_TAMAN_EX03` | `EXAMPLE_SELECTION` | `FAMILY_P1` | Kerusi Taman | Kerusi Komposit | `I-TAMAN-ROW-03` | `SCR_KERUSI_TAMAN_MAIN` | 1 |
| `II_PAPAN_TANDA_CAT01` | `SPECIFICATION_CATEGORY_POPUP` | `FAMILY_P2` | Papan Tanda | Bahan Panel | `N-TANDA-ROW-01` | `SCR_PAPAN_TANDA_MAIN` | 1 |
| `II_PAPAN_TANDA_CAT02` | `SPECIFICATION_CATEGORY_POPUP` | `FAMILY_P2` | Papan Tanda | Bahan Struktur/Tiang | `N-TANDA-ROW-01` | `SCR_PAPAN_TANDA_MAIN` | 1 |
| `II_PAPAN_TANDA_CAT03` | `SPECIFICATION_CATEGORY_POPUP` | `FAMILY_P2` | Papan Tanda | Grafik | `N-TANDA-ROW-01` | `SCR_PAPAN_TANDA_MAIN` | 1 |
| `II_PAPAN_TANDA_CAT04` | `SPECIFICATION_CATEGORY_POPUP` | `FAMILY_P2` | Papan Tanda | Rekaan | `N-TANDA-ROW-01` | `SCR_PAPAN_TANDA_MAIN` | 1 |
| `II_TONG_SAMPAH_R01_SPEC01` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Tong Sampah | Bahan | `-SAMPAH-ROW-01` | `SCR_TONG_SAMPAH_EX01_DETAIL` | 2 |
| `II_TONG_SAMPAH_R01_SPEC02` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Tong Sampah | Ciri-ciri | `-SAMPAH-ROW-01` | `SCR_TONG_SAMPAH_EX01_DETAIL` | 2 |
| `II_TONG_SAMPAH_EX01` | `EXAMPLE_SELECTION` | `FAMILY_P1` | Tong Sampah | Tong Sampah Logam | `-SAMPAH-ROW-01` | `SCR_TONG_SAMPAH_MAIN` | 1 |
| `II_TONG_SAMPAH_R02_SPEC01` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Tong Sampah | Bahan | `-SAMPAH-ROW-02` | `SCR_TONG_SAMPAH_EX02_DETAIL` | 2 |
| `II_TONG_SAMPAH_R02_SPEC02` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Tong Sampah | Ciri-ciri | `-SAMPAH-ROW-02` | `SCR_TONG_SAMPAH_EX02_DETAIL` | 2 |
| `II_TONG_SAMPAH_EX02` | `EXAMPLE_SELECTION` | `FAMILY_P1` | Tong Sampah | Tong Sampah Konkrit/Batu | `-SAMPAH-ROW-02` | `SCR_TONG_SAMPAH_MAIN` | 1 |
| `II_TONG_SAMPAH_R03_SPEC01` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Tong Sampah | Bahan | `-SAMPAH-ROW-03` | `SCR_TONG_SAMPAH_EX03_DETAIL` | 2 |
| `II_TONG_SAMPAH_R03_SPEC02` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Tong Sampah | Ciri-ciri | `-SAMPAH-ROW-03` | `SCR_TONG_SAMPAH_EX03_DETAIL` | 2 |
| `II_TONG_SAMPAH_EX03` | `EXAMPLE_SELECTION` | `FAMILY_P1` | Tong Sampah | Tong Sampah Plastik Kitar Semula (HDPE) | `-SAMPAH-ROW-03` | `SCR_TONG_SAMPAH_MAIN` | 1 |
| `II_DRINKING_FOUNTAIN_R01_SPEC01` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Drinking Fountain | Bahan | `OUNTAIN-ROW-01` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | 2 |
| `II_DRINKING_FOUNTAIN_R01_SPEC02` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Drinking Fountain | Injap | `OUNTAIN-ROW-01` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | 2 |
| `II_DRINKING_FOUNTAIN_R01_SPEC03` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Drinking Fountain | Kepala pancutan | `OUNTAIN-ROW-01` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | 2 |
| `II_DRINKING_FOUNTAIN_R01_SPEC04` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Drinking Fountain | Penapisan (pilihan) | `OUNTAIN-ROW-01` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | 2 |
| `II_DRINKING_FOUNTAIN_R01_SPEC05` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Drinking Fountain | Perpaipan | `OUNTAIN-ROW-01` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | 2 |
| `II_DRINKING_FOUNTAIN_R01_SPEC06` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Drinking Fountain | Aksesibiliti | `OUNTAIN-ROW-01` | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | 2 |
| `II_DRINKING_FOUNTAIN_EX01` | `EXAMPLE_SELECTION` | `FAMILY_P1` | Drinking Fountain | Pancutan Air Minum Keluli Tahan Karat | `OUNTAIN-ROW-01` | `SCR_DRINKING_FOUNTAIN_MAIN` | 1 |
| `II_DRINKING_FOUNTAIN_R02_SPEC01` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Drinking Fountain | Bahan | `OUNTAIN-ROW-02` | `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` | 2 |
| `II_DRINKING_FOUNTAIN_R02_SPEC02` | `SPECIFICATION_POPUP` | `FAMILY_P1` | Drinking Fountain | Piawaian kesihatan | `OUNTAIN-ROW-02` | `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` | 2 |
| `II_DRINKING_FOUNTAIN_EX02` | `EXAMPLE_SELECTION` | `FAMILY_P1` | Drinking Fountain | Pancutan Air Minum Konkrit/Batu | `OUNTAIN-ROW-02` | `SCR_DRINKING_FOUNTAIN_MAIN` | 1 |
| `II_BBQ_PIT_CAT01` | `SPECIFICATION_CATEGORY_POPUP` | `FAMILY_P2` | BBQ Pit | Bahan Pembinaan | `BBQ-PIT-ROW-01` | `SCR_BBQ_PIT_MAIN` | 1 |
| `II_BBQ_PIT_CAT02` | `SPECIFICATION_CATEGORY_POPUP` | `FAMILY_P2` | BBQ Pit | Dimensi | `BBQ-PIT-ROW-01` | `SCR_BBQ_PIT_MAIN` | 1 |
| `II_BBQ_PIT_CAT03` | `SPECIFICATION_CATEGORY_POPUP` | `FAMILY_P2` | BBQ Pit | Gril | `BBQ-PIT-ROW-01` | `SCR_BBQ_PIT_MAIN` | 1 |
| `II_BBQ_PIT_CAT04` | `SPECIFICATION_CATEGORY_POPUP` | `FAMILY_P2` | BBQ Pit | Keselamatan | `BBQ-PIT-ROW-01` | `SCR_BBQ_PIT_MAIN` | 1 |

---

# 5. What this map does not claim

- **No PowerPoint review-page numbers.** `review_page_role` is semantic; numbering belongs to the
  regeneration stage.
- **No asset binding.** `usage_status` for all 14 assets remains `EXTRACTED — not yet bound`.
- **No source-integrity closure.** The module DOCX SHA-256 is still unobtained under
  `B02-CAIR-INT-001`; `SOURCE_INTEGRITY_FULLY_VERIFIED` is not asserted.

---

# 6. Standing

Documentation only. No generator modified, no PowerPoint generated, no component propagated, no
multimedia produced, no canonical `P#` minted.
