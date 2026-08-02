# T04_SCREEN_CONTRACTS_DRAFT — v1

Stage 4.2F-B0.5. Generated from `docs/pl06/t04/tools/t04_pack_emit_v1.py`.

```
CONTRACTS = 6
PROCESS_FLOW 1 · CLICK_TO_REVEAL 2 · SEQUENTIAL_STEPS 1 · COMPARISON 1 · PENDING_HUMAN 1
APPROVAL  = PENDING_BARIAH_REVIEW
```

> **Every proposal below is `CAIR_ASSISTED_DRAFT` / `PENDING_BARIAH_REVIEW`.** Bariah is the sole Instructional Designer and the only approval authority. CAIR prepared the source analysis, the mapping and the drafts; none of it is approved instructional content and none of it may be treated as an ID decision.

# The reveal rule

Both `CLICK_TO_REVEAL` contracts hide **supplementary description only**. Every legal, safety and compliance obligation in this unit — all eleven source rows — sits on `T04-CT-04` and is **visible in the base state**. A learner who never interacts with anything still sees every obligation. That separation is deliberate and is held by the gate `LEGAL_ROWS_NOT_GATED_BEHIND_OPTIONAL_REVEAL`.

# `T04-CT-01` — PROCESS_FLOW

| field | value |
|---|---|
| source_rows | T04-ROW-001; T04-ROW-002; T04-ROW-003 |
| learner_facing_purpose | Show the six supervisory activities the module names as the maintenance process. |
| base_state | Screen title, the source's introductory sentence, and the six-node process flow rendered in source order, all visible. |
| interaction_states | BASE only — no interaction proposed |
| completion_condition | screen viewed |
| visual_treatment | Source-bound reference to T04-DGM-01. Either a controlled redraw preserving the six nodes and their order, or a readable placeholder carrying the same six labels. No node invented, reordered or reworded. |
| text_treatment | Introductory sentence verbatim; six node labels verbatim. |
| vo_proposal | One screen-level VO introducing the flow and naming the six activities in order. CAIR_ASSISTED_DRAFT — wording is Bariah's to set. |
| speaker_notes_proposal | NON_SPOKEN_CONTEXT: unit and page provenance. SPOKEN_CONTENT_VO: the introduction. PRODUCTION_INSTRUCTION_NOT_SPOKEN: SmartArt redraw instruction, six nodes, linear. |
| accessibility_consideration | The six labels must exist as selectable text, not only inside an image, so a screen reader can reach them. A flattened bitmap of the diagram would fail this. |
| fallback_behaviour | If the redraw is not ready, the screen still carries the six labels as an ordered text list — the meaning survives without the graphic. |
| source_authority | MODULE_SOURCE_ATTESTED — T04-DGM-01, six nodes measured from word/diagrams/data1.xml |
| open_decision | D-05 SmartArt production |

| Bariah approval | value |
|---|---|
| status | PENDING_BARIAH_REVIEW |
| decision | ☐ accept  ☐ amend  ☐ reject |
| comment | _________________________ |

# `T04-CT-02` — CLICK_TO_REVEAL

| field | value |
|---|---|
| source_rows | T04-ROW-004; T04-ROW-005; T04-ROW-006; T04-ROW-026; T04-ROW-046 |
| learner_facing_purpose | Introduce the three soft-landscape maintenance operations. |
| base_state | Section title, section definition, and three cards labelled Siram, Baja and Racun — all three LABELS visible before any interaction. |
| interaction_states | BASE; SIRAM_REVEALED; BAJA_REVEALED; RACUN_REVEALED; ALL_VIEWED |
| completion_condition | all three revealed |
| visual_treatment | NONE — no source visual exists for any of the three. Text-led. |
| text_treatment | One definition per operation, verbatim from its source row. |
| vo_proposal | Screen-level instruction only, in the B02 pattern. CAIR_ASSISTED_DRAFT. |
| speaker_notes_proposal | SPOKEN_INTERACTION_INSTRUCTION for the screen-level instruction; SPOKEN_CONTENT_VO per revealed definition. |
| accessibility_consideration | Reveals must be keyboard reachable and their state announced. The all-viewed state must not be the only route to the next screen. |
| fallback_behaviour | If reveal is not available, the three definitions render stacked. Nothing is lost. |
| source_authority | MODULE_SOURCE_ATTESTED |
| open_decision | D-01 visual treatment |
| hidden_content_classification | SUPPLEMENTARY |
| hidden_content_justification | What is hidden is the DEFINITION of each operation — descriptive expansion of a label already on screen. No legal, safety or compliance obligation is behind any reveal on this screen: all eleven of those rows sit on T04-CT-04, where they are visible in the base state. This separation is deliberate and is gated by LEGAL_ROWS_NOT_GATED_BEHIND_OPTIONAL_REVEAL. |

| Bariah approval | value |
|---|---|
| status | PENDING_BARIAH_REVIEW |
| decision | ☐ accept  ☐ amend  ☐ reject |
| comment | _________________________ |

# `T04-CT-03` — CLICK_TO_REVEAL

| field | value |
|---|---|
| source_rows | T04-ROW-079; T04-ROW-080; T04-ROW-081; T04-ROW-086; T04-ROW-091; T04-ROW-096 |
| learner_facing_purpose | Present the four functions hard landscape performs. |
| base_state | Section title, section definition, and four group labels — all visible. |
| interaction_states | BASE; GROUP_1_REVEALED; GROUP_2_REVEALED; GROUP_3_REVEALED; GROUP_4_REVEALED; ALL_VIEWED |
| completion_condition | all four revealed |
| visual_treatment | NONE — text-led. |
| text_treatment | Two source sub-items per group, verbatim. |
| vo_proposal | Screen-level instruction only. CAIR_ASSISTED_DRAFT. |
| speaker_notes_proposal | SPOKEN_INTERACTION_INSTRUCTION plus per-group SPOKEN_CONTENT_VO. |
| accessibility_consideration | As T04-CT-02. |
| fallback_behaviour | Stacked rendering; nothing lost. |
| source_authority | MODULE_SOURCE_ATTESTED |
| open_decision | D-01 visual treatment |
| hidden_content_classification | SUPPLEMENTARY |
| hidden_content_justification | Purely descriptive expansion — examples of walls, pathways, retaining walls, drainage, patios, decks, gazebos. No obligation of any kind is on this screen. |

| Bariah approval | value |
|---|---|
| status | PENDING_BARIAH_REVIEW |
| decision | ☐ accept  ☐ amend  ☐ reject |
| comment | _________________________ |

# `T04-CT-04` — SEQUENTIAL_STEPS

| field | value |
|---|---|
| source_rows | T04-ROW-065; T04-ROW-066; T04-ROW-067; T04-ROW-068; T04-ROW-069; T04-ROW-071; T04-ROW-073; T04-ROW-075; T04-ROW-076; T04-ROW-077; T04-ROW-078 |
| learner_facing_purpose | Carry the contractor's legal, HSE and risk obligations for pesticide work. |
| base_state | ALL obligation headings visible in the base state: Perundangan dan Pelesenan, Keselamatan dan Kesihatan (HSE), Pengurusan Risiko. The Akta Racun Makhluk Perosak 1974 citation and the licensed-operator requirement are on the base state, not behind an interaction. |
| interaction_states | BASE (all obligations visible); STEP_DETAIL_1; STEP_DETAIL_2; STEP_DETAIL_3; ALL_VIEWED |
| completion_condition | all steps stepped through; the base state already discharges the disclosure |
| visual_treatment | NONE. |
| text_treatment | Eleven source rows verbatim. No paraphrase of a legal obligation. |
| vo_proposal | Screen-level instruction; each obligation spoken. CAIR_ASSISTED_DRAFT. |
| speaker_notes_proposal | PRODUCTION_INSTRUCTION_NOT_SPOKEN recording that this screen carries legal content and must not be abbreviated in MMD. |
| accessibility_consideration | Legal content must be reachable without interaction and must not depend on colour or hover alone. |
| fallback_behaviour | If stepping is unavailable, every obligation still renders. That is the point of putting them in the base state. |
| source_authority | MODULE_SOURCE_ATTESTED — verbatim; the 1974 Act citation is EXTERNAL_VERIFICATION_REQUIRED and is quoted, not asserted |
| open_decision | D-04 legislative content |
| hidden_content_classification | NOT_APPLICABLE_NOTHING_MANDATORY_IS_HIDDEN |
| hidden_content_justification | Stepping adds emphasis and pacing. It gates nothing: every obligation is in the base state. A learner who never interacts still sees all of them. |

| Bariah approval | value |
|---|---|
| status | PENDING_BARIAH_REVIEW |
| decision | ☐ accept  ☐ amend  ☐ reject |
| comment | _________________________ |

# `T04-CT-05` — COMPARISON

| field | value |
|---|---|
| source_rows | T04-ROW-004; T04-ROW-005; T04-ROW-079; T04-ROW-080; T04-ROW-100 |
| learner_facing_purpose | Make explicit the contrast the source itself draws between soft and hard landscape. |
| base_state | Two columns, one per section, each carrying its source definition, with the source's own closing contrast statement beneath. |
| interaction_states | BASE only |
| completion_condition | screen viewed |
| visual_treatment | NONE. |
| text_treatment | Two section definitions and T04-ROW-100 verbatim. |
| vo_proposal | One short screen-level VO. CAIR_ASSISTED_DRAFT. |
| speaker_notes_proposal | NON_SPOKEN_CONTEXT plus one SPOKEN_CONTENT_VO block. |
| accessibility_consideration | A two-column layout must linearise in reading order, not column-by-column visually. |
| fallback_behaviour | Single-column stack, soft then hard. |
| source_authority | MODULE_SOURCE_ATTESTED |
| open_decision | D-01 visual treatment — and whether this screen is wanted at all |

| Bariah approval | value |
|---|---|
| status | PENDING_BARIAH_REVIEW |
| decision | ☐ accept  ☐ amend  ☐ reject |
| comment | _________________________ |

# `T04-CT-06` — PENDING_HUMAN

| field | value |
|---|---|
| source_rows | — |
| learner_facing_purpose | Recap and assess the unit. |
| base_state | NOT PROPOSED — no treatment is chosen here. |
| interaction_states | PENDING |
| completion_condition | PENDING |
| visual_treatment | NONE. |
| text_treatment | NONE IN SOURCE. |
| vo_proposal | PENDING. |
| speaker_notes_proposal | PENDING. |
| accessibility_consideration | PENDING. |
| fallback_behaviour | PENDING. |
| source_authority | NO_SOURCE — the module contains no Rumusan and no assessment items anywhere |
| open_decision | D-02 quiz structure; Rumusan approval |

**Options — no treatment is chosen here.**

| option | proposal | source grounding | trade-off |
|---|---|---|---|
| A | Rumusan screen + quiz block, B02 shape | The A3 Style and Guidelines defines both treatments and B02 implements them. Structure is proven; only content is missing. | Fastest and most consistent with B02. But it imports the 4 MCQ + 1 MR shape and the 60% threshold, both of which are A3-scoped to B02 and unconfirmed for PL06. Choosing this settles D-02 by default rather than deliberately. |
| B | Rumusan screen + assessment sized to T04's coverage | T04 has a countable set of assessable learning points — three soft-landscape operations, four hard-landscape functions, and one compliance cluster. The blueprint counts them from source rows. | Assessment matches what the unit actually teaches, and the compliance material gets weight proportional to its risk. But it breaks uniformity across PL06 units unless Bariah sets a rule, and it needs a threshold decision that A3 does not supply. |
| C | Rumusan screen only, assessment deferred to Topik level | Topik 4 has exactly one Bahagian, so a unit quiz and a topic quiz would assess the same content twice. | Avoids duplicate assessment and is defensible for a single-lesson Topik. But it makes T04 structurally different from B02, and no artifact establishes that a Topik-level assessment exists or is planned. |

| Bariah approval | value |
|---|---|
| status | PENDING_BARIAH_REVIEW |
| decision | ☐ accept  ☐ amend  ☐ reject |
| comment | _________________________ |
