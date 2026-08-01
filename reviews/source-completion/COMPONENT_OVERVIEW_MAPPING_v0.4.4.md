# COMPONENT_OVERVIEW_MAPPING — v0.4.4

Source-bound overview subjects for all nine component-main learner screens.

> ## ⛔ Generation is blocked

> `COMPONENT_OVERVIEW_MAPPING_REQUIRES_HUMAN_LAYOUT_RULING`

> **2 of 9 components** cannot supply a defensible source-bound overview without inventing a selection rule: **BBQ_PIT, PAPAN_TANDA**. Details in §4.

# 1. Authority — requirement and treatment are hers, subjects are not

| Field | Value |
|---|---|
| `VISUAL_REQUIREMENT_AUTHORITY` | `BARIAH_DIRECT_SCREENSHOT` — D2, 6:52 PM |
| `VISUAL_TREATMENT_AUTHORITY` | `BARIAH_DIRECT_SCREENSHOT` — D2, 6:52 PM |
| `VISUAL_SUBJECT_DIRECTLY_NAMED_BY_BARIAH` | **false for every subject in this file** |

Requirement, verbatim: *"Soalan 1: Component-main - Visual diperlukan"*

Treatment, verbatim: *"Soalan 2: Pop up - visual diperlukan. Kemungkinan visual di component main, saiznya lebih kecil dan ada banyak visual lain. Jadi di pop up, visual nya lebih besar dan fokus. Kan?"*

She confirmed **that** component mains need a visual and **how** it should look. She named no subject for any of the nine. Every subject below is therefore `MODULE_SOURCE_ATTESTED`, read from the frozen 26-row matrix.

## Selection rules applied

- one overview subject per distinct source row bound to the component
- exact-deduplicate on resolved visual-direction text
- no subject generated from the component name
- no subject borrowed from another component
- no generic subject
- DECISION_SUMMARY.md not used as a visual oracle

# 2. Totals

| Metric | Value |
|---|---:|
| `COMPONENTS_MAPPED` | 9 |
| `INVENTED_VISUAL_SUBJECTS` | 0 |
| `CROSS_COMPONENT_SUBJECT_REUSE_WITHOUT_AUTHORITY` | 0 |
| `UNEXPLAINED_OVERVIEW_COUNTS` | 0 |
| `AMBIGUOUS_OVERVIEW_MAPPINGS` | 2 |
| `COMPONENTS_RESOLVED` | 7 |
| `GENERATION_PERMITTED` | False |

# 3. The nine components

| Component | Family | Rows | Assets | Overview subjects | Count | Status |
|---|---|---:|---:|---|---:|---|
| Struktur Persisir Air | `FAMILY_S` | 5 | 1 | Promenade<br>Jeti<br>Dek Kayu<br>Boardwalk<br>Footbridge | 5 | `RESOLVED` |
| Struktur Teduhan | `FAMILY_S` | 5 | 1 | Gazebo<br>Wakaf<br>Pergola<br>Canopy<br>Struktur Teduhan Moden | 5 | `RESOLVED` |
| Kemudahan Awam | `FAMILY_S` | 3 | 0 | Tandas Awam<br>Surau<br>Bangunan Interpretatif | 3 | `RESOLVED` |
| Water Feature | `FAMILY_S` | 3 | 0 | Air Pancut (Fountain)<br>Kolam (Pond)<br>Kolam Renang / Kolam Hiasan Besar (Pool) | 3 | `RESOLVED` |
| Kerusi Taman | `FAMILY_P1` | 3 | 3 | Kerusi Kayu Keras<br>Kerusi Konkrit<br>Kerusi Komposit | 3 | `RESOLVED` |
| Papan Tanda | `FAMILY_P2` | 1 | 2 | Papan Tanda Arah / Papan Tanda Interpretatif | 1 | `AMBIGUOUS` |
| Tong Sampah | `FAMILY_P1` | 3 | 4 | Tong Sampah Logam<br>Tong Sampah Konkrit/Batu<br>Tong Sampah Plastik Kitar Semula (HDPE) | 3 | `RESOLVED` |
| Drinking Fountain | `FAMILY_P1` | 2 | 2 | Pancutan Air Minum Keluli Tahan Karat<br>Pancutan Air Minum Konkrit/Batu | 2 | `RESOLVED` |
| BBQ Pit | `FAMILY_P2` | 1 | 1 | BBQ Pit Struktur Kekal | 1 | `AMBIGUOUS` |

**`overview_visual_count` is not a constant.** It is one subject per distinct source row bound to that component, exact-deduplicated on the resolved direction text — 5, 5, 3, 3, 3, 3, 2 for the seven resolved components. No universal number was imposed.

## 3.1 Struktur Persisir Air — the one Bariah-direct string

Its component-main screen carries her own direction `[Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]`. *Pelbagai* means *several*, so her string and the overview treatment agree: the direction stays as the overview heading and the five source rows supply the several smaller visuals. Nothing is overwritten.

# 4. Why generation is blocked

## Papan Tanda (`PAPAN_TANDA`) — `SCR_PAPAN_TANDA_MAIN`

- source rows: **1**
- row label: `Papan Tanda Arah / Papan Tanda Interpretatif`
- distinct source assets: 2 — `K5PL06T03-B02-IMG-p245-x37`, `K5PL06T03-B02-IMG-p245-x38`
- row visual direction: `[Visual: Rajah 25 — Lukisan Spesifikasi Papan Tanda Informasi, dan Rajah 26 — Spesifikasi Papan Tanda Penunjuk Arah, kedua-duanya modul ms 245. Aset K5PL06T03-B02-IMG-p245-x37 dan K5PL06T03-B02-IMG-p245-x38. Tidak dibenamkan.]`
- row contoh: —

| Reading | Subjects | Count |
|---|---|---:|
| **A** — one overview subject = the single source row | Papan Tanda Arah / Papan Tanda Interpretatif | 1 |
| **B** — two overview subjects = the two separately named and separately asset-bound figures inside the single row's visual direction… | [Visual: Rajah 25 — Lukisan Spesifikasi Papan Tanda Informasi, Rajah 26 — Spesifikasi Papan Tanda Penunjuk Arah, kedua-duanya modul ms 245. Aset K5PL06T03-B02-IMG-p245-x37 | 2 |

**Why CC will not choose.** Choosing between these readings is a selection rule, and Part 1 forbids inventing one. Reading B for PAPAN_TANDA is defensible because both figures are separately named with separate asset IDs in the frozen source; but the row label names 'Papan Tanda Arah / Papan Tanda Interpretatif' while the figures name 'Papan Tanda Informasi' and 'Papan Tanda Penunjuk Arah', so even pairing label to figure is interpretive.

Specification categories were considered and rejected as overview subjects — Bahan Panel, Bahan Struktur/Tiang, Grafik, Rekaan — because specification popups are ruled `NOT_REQUIRED` for visuals, so promoting them here would contradict a frozen ruling.

> **Question:** Papan Tanda: overview shows ONE subject (the single source row) or TWO (Rajah 25 Papan Tanda Informasi and Rajah 26 Papan Tanda Penunjuk Arah)?

## BBQ Pit (`BBQ_PIT`) — `SCR_BBQ_PIT_MAIN`

- source rows: **1**
- row label: `BBQ Pit Struktur Kekal`
- distinct source assets: 1 — `K5PL06T03-B02-IMG-p249-x57`
- row visual direction: `[Visual: Foto jadual spesifikasi BBQ Pit Struktur Kekal, modul ms 249. Aset K5PL06T03-B02-IMG-p249-x57. Tidak dibenamkan.]`
- row contoh: `Lubang barbeku yang dibina tetap di taman perumahan, tapak perkhemahan awam, atau kawasan rekreasi keluarga seperti di Taman Rekreasi Bukit Jalil, Kuala Lumpur.`

| Reading | Subjects | Count |
|---|---|---:|
| **A** — one overview subject = the single source row | BBQ Pit Struktur Kekal | 1 |
| **B** — two overview subjects = the spec-table figure plus the row's contoh location. This elevates a FALLBACK direction source to a co-equal overview subject… | — | 0 |

**Why CC will not choose.** BBQ Pit has exactly one source row, one source asset and one figure. There is no second distinct source-bound subject. A second could only come from the row's contoh text (a location, semantically unlike a spec-table photo) or from the four specification categories — and specification popups are ruled NOT_REQUIRED for visuals, so using them as overview subjects would contradict a frozen ruling.

Specification categories were considered and rejected as overview subjects — Bahan Pembinaan, Dimensi, Gril, Keselamatan — because specification popups are ruled `NOT_REQUIRED` for visuals, so promoting them here would contradict a frozen ruling.

> **Question:** BBQ Pit has only ONE source-bound visual subject. Does 'several smaller visuals as an overview' permit a single-visual overview here, or is another subject authorised?

# 5. What would unblock this

One ruling per component, from whoever owns the layout decision:

1. **Papan Tanda** — one overview subject or two?
2. **BBQ Pit** — is a single-visual overview acceptable, or is a second subject authorised (and if so, which)?

Neither is answerable from the frozen evidence. D2 settles the requirement and the treatment; it does not settle how a one-row component supplies *several* visuals. Guessing would put an invented subject on a learner screen, which Part 1 and Part 4 both forbid.
