# PL06 Pilot — Layout-Stress Selection (Lane P)

> **INTERNAL_GENERATION_DRAFT** — machine-authored engineering record. Not reviewed, not
> Bariah-approved, not a production template. Nothing here is instructionally approved.

- **Lane:** P — one committed non-B03 pilot
- **Base commit:** `ebd6d81`
- **Branch:** `cc/pl06-pilot`
- **Selected unit:** `K5-PL06-T05-B01` — *Pengurusan Kualiti Projek* (Topik 5, modul ms 284–293)
- **Selection criterion:** highest layout stress among the three committed non-B03 units

## 1. Candidate set

The three committed non-B03 units of `PL06-HARVEST-BATCH-1` (B03 excluded as the calibration
reference). Each carries a committed provisional model in
`docs/pl06/batch1_extract/` and a committed unit model in `docs/pl06/tools/pl06_unit_model_v1.py`.

## 2. Layout-stress evidence

All figures are read from the committed provisional models
(`K5_PL06_{unit}_PROVISIONAL_MODEL_v1.json`) and the batch package
(`PL06_HARVEST_BATCH1_PACKAGE_v1.md`). No figure is asserted here.

| layout-stress signal | T03-B04 | **T05-B01** | T06-B01 | source field |
|---|---:|---:|---:|---|
| module pages | 6 | **10** | 8 | page_range / package |
| source paragraphs | 136 | **183** | 162 | package |
| heading-tree nodes | 36 | **44** | 37 | `heading_tree.tree` |
| prose-styled-as-heading | 2 | **20** | 18 | `prose_styled_as_heading.count` |
| subtopics / content groups | 1 | **4** | 3 | `grouping.groups` |
| minimum learner screens | 10 | **10** | 8 | `screen_sequence.arithmetic.minimum_total_screens` |
| base-states floor | 10 | **10** | 8 | `runtime_state_estimate.base_states_floor` |
| Rumusan beats (montage density) | 3 | **5** | 4 | `rumusan.beat_count` |
| compliance-sensitive statements | 2 | **4** | 4 | `compliance_sensitive.count` |
| interaction candidates | 5 | 4 | 3 | `interaction_candidates.candidates` |
| auto-detected components | 2 | 0 | 0 | `components.count` |

## 3. Verdict

`K5-PL06-T05-B01` is the highest-layout-stress candidate. It leads or ties on every
layout-relevant dimension — most paragraphs (183), most heading-tree nodes (44), most
prose-styled-as-heading rows (20, the strongest pagination-pressure signal), most content
groups (4), the joint-highest learner-screen count (10) and base-states floor (10), and the
densest Rumusan montage (5 beats). It trails only on interaction-candidate count and
component detection, neither of which is a layout-stress signal — both describe interaction
complexity, and both are dominated on T03-B04 precisely because that unit is the smallest by
content volume (6 pages, 1 subtopic, 136 paragraphs).

This agrees with the repository's own governance characterisation in
`PL06_FIRST_SCALE_OUT_SELECTION_v1.md`, which describes T05-B01 as "10 module pages, four
subtopics … larger and more procedural than T04" and the "strong second choice … but 10
pages and four subtopics against T04's 8 pages and two."

## 4. What this selection is not

This selection commits the pilot to *attempt* generic generation on T05-B01. It does not
assert that generation succeeded. The outcome of that attempt — a hard stop at the Lampiran
Keadaan state inventory — is recorded in `PL06_PILOT_UNIT_MANIFEST_v1.md` and
`PL06_PILOT_DEFECT_REPORT_v1.md`. No Bariah readiness is claimed.
