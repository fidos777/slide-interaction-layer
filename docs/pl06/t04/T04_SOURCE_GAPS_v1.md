# T04_SOURCE_GAPS — v1

Stage 4.2F-B0. Generated from `docs/pl06/t04/tools/t04_emit_v1.py`.

```
GAPS = 6
BLOCKS_THIS_UNIT = 4
INSTRUCTIONAL_STATUS = CONTENT_ASSESSMENT_PENDING
```

# Readiness semantics

`SOURCE_INCOMPLETE` is retired for these units. It conflated three different states with three different owners:

| state | meaning | who clears it |
|---|---|---|
| `SOURCE_PRESENT_CONTENT_NOT_EXTRACTED` | source and boundary in custody, nobody has read it | us, by working |
| `CONTENT_ASSESSMENT_PENDING` | read and modelled, instructional treatment not settled | us to propose, a human to approve |
| `SOURCE_GAP_CONFIRMED` | read, and the content is genuinely not in the module | **nobody, by reading** — it must be authored |

**T04-B01 is `CONTENT_ASSESSMENT_PENDING`.** COMPLETE — 100 controlled rows, 1 asset, 0 tables, 61 numbered paragraphs, 8 module pages, every element in the 140-element body span accounted for.

The other twelve units stay `SOURCE_PRESENT_CONTENT_NOT_EXTRACTED`. The distinction matters because the three states have different owners. SOURCE_PRESENT_CONTENT_NOT_EXTRACTED is ours to clear by working. CONTENT_ASSESSMENT_PENDING is ours to propose and a human's to approve. SOURCE_GAP_CONFIRMED cannot be cleared by anyone reading the module, because the content is not in it.

# Gaps

| id | item | severity | finding | owner |
|---|---|---|---|---|
| `T04-GAP-01` | Rumusan | **BLOCKS_THIS_UNIT** | Not in T04 and not anywhere in the module DOCX — zero hits for 'Rumusan' across all 6,167 body paragraphs. | CC to author under A3 treatment, Bariah to approve |
| `T04-GAP-02` | Quiz items and answer key | **BLOCKS_THIS_UNIT** | Zero hits for 'Soalan', 'Kuiz' or 'Jawapan' across the module. | CC to draft, SME to sign the key |
| `T04-GAP-03` | Visual subjects for the body content | **BLOCKS_THIS_UNIT** | The unit contains ONE visual — a SmartArt process diagram at the opening. There are zero raster images. Siram, Baja, Racun and all four Landskap Kejur function groups have no source visual at all. | BARIAH — visual requirement and treatment for a unit with no photographs |
| `T04-GAP-04` | Cast binding | **BLOCKS_THIS_UNIT** | Unchanged from Stage 4.2F-A2: the ratified bank marks Haziq and Encik Roslan CANONICAL, B02 ships Alya and Encik Rahman, and Bariah's PL06-wide answer names neither. | BARIAH + CAIR |
| `T04-GAP-05` | SmartArt rendering path | **BLOCKS_MMD_ONLY** | The only visual is a vector SmartArt part (word/diagrams/data1.xml), not an image file. It cannot be extracted as a JPEG the way B02's 14 assets were. | MMD / Bariah |
| `T04-GAP-06` | Lesson grouping authority | **BLOCKS_CANONICAL_FREEZE_ONLY** | Carried forward: GROUPING_AUTHORITY = REFERENCED_NOT_FROZEN. | CAIR |

# Notes

- **`T04-GAP-01`** — This retro-explains B02: its Rumusan was authored, not extracted. No storyboard in this project has ever had a source-supplied Rumusan.
- **`T04-GAP-02`** — Composition (4 MCQ + 1 MR) and the 60% threshold are A3-scoped to B02 and must be confirmed before being applied here.
- **`T04-GAP-03`** — This is the single most important portability finding of the stage. B02's component-main treatment is a source-bound overview of photographs, backed by 14 extracted assets. T04 has none. Applying B02's treatment here would require inventing subjects, which is prohibited. RP-101 is REUSABLE_WITH_SOURCE_SPECIFIC_BINDING and there is nothing here to bind it to.
- **`T04-GAP-04`** — STOP-006, SRC-ANOM-003.
- **`T04-GAP-05`** — Does not block the review storyboard, which carries visual DIRECTIONS as text.
- **`T04-GAP-06`** — Does not touch T04 — Topik 4 has one lesson, so no grouping judgement applies.

# Targeted decisions

Five, and none of them is ours to close:

| id | question | owner | blocks | evidence |
|---|---|---|---|---|
| `T04-DEC-01` | A unit with no photographs — what is the visual treatment for a component with no source visual? | BARIAH | storyboard model | T04-GAP-03 |
| `T04-DEC-02` | Is 4 MCQ + 1 MR with a 60% threshold a PL06 standard or a B02 instantiation? | BARIAH / source governance | quiz screens | RP-009, RP-010 |
| `T04-DEC-03` | Which cast pair applies outside B02? | BARIAH + CAIR | S02 dialog screen | SRC-ANOM-003 |
| `T04-DEC-04` | May legislative and HSE content be reveal-gated, or must it be shown in full? | BARIAH | T04-SC-03 | T04-CLM-01, T04-CLM-02 |
| `T04-DEC-05` | How is the opening SmartArt process flow to be produced — re-drawn, exported, or rebuilt as sequential reveals? | BARIAH / MMD | T04-SC-01 | T04-GAP-05 |
