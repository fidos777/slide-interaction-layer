# COMPONENT_OVERVIEW_MAPPING — v0.4.4

Source-bound overview subjects for all nine component-main learner screens.

> ## ✅ Closed

> `INSTANCE_MAPPING_COMPLETE = 9/9` · `AMBIGUOUS_OVERVIEW_MAPPINGS = 0` · `PENDING_BARIAH_OVERVIEW_QUESTIONS = 0`

The two blocking components were closed by Bariah's reply of 2 August 2026, 8:24 AM, frozen as `B02_BARIAH_DECISION_OVERVIEW_CARDINALITY_20260802.png`:

> *"Yup, papan tanda Pilihan A, ok bbq pit 1 gamba"*

# 1. Authority

| Field | Value |
|---|---|
| `VISUAL_REQUIREMENT_AUTHORITY` | `BARIAH_DIRECT_SCREENSHOT` — D2, 1 Aug 6:52 PM |
| `VISUAL_TREATMENT_AUTHORITY` | `BARIAH_DIRECT_SCREENSHOT` — D2, 1 Aug 6:52 PM |
| `CARDINALITY_AUTHORITY` | `BARIAH_DIRECT_SCREENSHOT` — D4, 2 Aug 8:24 AM |

Subjects are `MODULE_SOURCE_ATTESTED` throughout, **except** the two Papan Tanda figures, which D4 names directly in its option block. Nothing else is named by Bariah and nothing else is invented.

# 2. Totals

| Metric | Value |
|---|---:|
| `COMPONENTS_MAPPED` | 9 |
| `INVENTED_VISUAL_SUBJECTS` | 0 |
| `CROSS_COMPONENT_SUBJECT_REUSE_WITHOUT_AUTHORITY` | 0 |
| `UNEXPLAINED_OVERVIEW_COUNTS` | 0 |
| `AMBIGUOUS_OVERVIEW_MAPPINGS` | 0 |
| `COMPONENTS_RESOLVED` | 9 |
| `GENERATION_PERMITTED` | True |
| `POLICY_RESOLVED` | True |
| `INSTANCE_MAPPING_COMPLETE` | 9/9 |
| `IMPLEMENTATION_CONTRACT_COMPLETE` | True |
| `PENDING_BARIAH_OVERVIEW_QUESTIONS` | 0 |
| `TOTAL_OVERVIEW_SUBJECTS` | 27 |

# 3. Final counts — all nine

| Component | Family | Rows | Overview subjects | Count | Source |
|---|---|---:|---|---:|---|
| Struktur Persisir Air | `FAMILY_S` | 5 | Promenade<br>Jeti<br>Dek Kayu<br>Boardwalk<br>Footbridge | **5** | MODULE_SOURCE_ATTESTED |
| Struktur Teduhan | `FAMILY_S` | 5 | Gazebo<br>Wakaf<br>Pergola<br>Canopy<br>Struktur Teduhan Moden | **5** | MODULE_SOURCE_ATTESTED |
| Kemudahan Awam | `FAMILY_S` | 3 | Tandas Awam<br>Surau<br>Bangunan Interpretatif | **3** | MODULE_SOURCE_ATTESTED |
| Water Feature | `FAMILY_S` | 3 | Air Pancut (Fountain)<br>Kolam (Pond)<br>Kolam Renang / Kolam Hiasan Besar (Pool) | **3** | MODULE_SOURCE_ATTESTED |
| Kerusi Taman | `FAMILY_P1` | 3 | Kerusi Kayu Keras<br>Kerusi Konkrit<br>Kerusi Komposit | **3** | MODULE_SOURCE_ATTESTED |
| Papan Tanda | `FAMILY_P2` | 1 | Papan Tanda Informasi<br>Papan Tanda Penunjuk Arah | **2** | BARIAH_DIRECT (figures named in D4) |
| Tong Sampah | `FAMILY_P1` | 3 | Tong Sampah Logam<br>Tong Sampah Konkrit/Batu<br>Tong Sampah Plastik Kitar Semula (HDPE) | **3** | MODULE_SOURCE_ATTESTED |
| Drinking Fountain | `FAMILY_P1` | 2 | Pancutan Air Minum Keluli Tahan Karat<br>Pancutan Air Minum Konkrit/Batu | **2** | MODULE_SOURCE_ATTESTED |
| BBQ Pit | `FAMILY_P2` | 1 | BBQ Pit Struktur Kekal | **1** | MODULE_SOURCE_ATTESTED |

Counts are 5, 5, 3, 3, 3, **2**, 3, 2, **1** — derived per component, never a fixed number.

# 4. The source-aware cardinality rule

```
If a component has multiple distinct source-bound visual subjects,
  display the approved multiple subjects as smaller overview visuals.
If a component has only one defensible source-bound visual subject,
  a single-visual component-main overview is permitted.
No additional visual may be invented merely to satisfy the word 'several'.
```

| Assertion | Value |
|---|---|
| `MINIMUM_OVERVIEW_CARDINALITY` | 1 |
| `CARDINALITY_SOURCE_DERIVED` | true |
| `INVENTED_SUBJECTS_TO_REACH_MINIMUM` | 0 |
| `UNIVERSAL_FIXED_CARD_COUNT` | false |

This is **not** permission to reduce a component that already has multiple approved source-bound subjects. The seven previously resolved counts are unchanged.

# 5. The two closures

## Papan Tanda — Pilihan A, two visuals

Bariah selected `A. Paparkan kedua-dua visual`. Both figures are displayed:

| # | Subject | Figure | Asset |
|---|---|---|---|
| 1 | Papan Tanda Informasi | Rajah 25 | `K5PL06T03-B02-IMG-p245-x37` |
| 2 | Papan Tanda Penunjuk Arah | Rajah 26 | `K5PL06T03-B02-IMG-p245-x38` |

**Terminology guard.** The source row's LABEL reads *Papan Tanda Arah / Papan Tanda Interpretatif*; the FIGURES read *Informasi* and *Penunjuk Arah*. The ruling names the figures, so the figure-bound names are used on the overview. **No global equivalence between *Informasi* and *Interpretatif* is created** — the row label is untouched and still appears as the screen's sub-heading.

## BBQ Pit — one image

Bariah's option A: *satu visual dibenarkan kerana source hanya satu*. One card, one source-bound subject, `BBQ Pit Struktur Kekal` / `K5PL06T03-B02-IMG-p249-x57`.

Explicitly rejected and gate-checked: duplicating the visual, inventing a second subject, promoting the four specification categories to visual subjects, using the row's *contoh* location text as a second subject, and borrowing from another component.
