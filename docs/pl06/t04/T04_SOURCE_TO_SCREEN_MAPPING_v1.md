# T04_SOURCE_TO_SCREEN_MAPPING — v1

Stage 4.2F-B0.5. Generated from `docs/pl06/t04/tools/t04_pack_emit_v1.py`.

```
UNIT               = K5-PL06-T04-B01
SCREEN CANDIDATES  = 6
FINAL SCREEN COUNT = NOT_CLAIMED
CONTENT STATUS     = CAIR_ASSISTED_DRAFT
APPROVAL STATUS    = PENDING_BARIAH_REVIEW
B02_FAMILIES_PROPAGATED = 0
```

> **Every proposal below is `CAIR_ASSISTED_DRAFT` / `PENDING_BARIAH_REVIEW`.** Bariah is the sole Instructional Designer and the only approval authority. CAIR prepared the source analysis, the mapping and the drafts; none of it is approved instructional content and none of it may be treated as an ID decision.

# Role ownership

| role | owns |
|---|---|
| CAIR | source analysis; source-to-screen mapping; draft preparation; traceability; technical validation |
| BARIAH | sole Instructional Designer; instructional author and approval authority; confirms screen treatment; approves or edits Rumusan; authors, edits or approves quiz content; approves narration and interaction treatment |
| FIRDAUS | project owner; delivery and scope authority; confirms operational decisions where required |

# Why no screen count is claimed

Six candidates are six treatments, not a sequence. T04-SC-04 may be dropped, T04-SC-02 may become three screens, and T04-SC-06 is two screens or none depending on what Bariah authors. A number here would be invented, and it would not be derived from B02 either — B02's 29 learner screens describe a different unit with a different structure.

# Mapping

| candidate | working title | treatment | status | source rows | visual dep | Bariah decision |
|---|---|---|---|---|---|---|
| `T04-SC-01` | Aliran proses penjagaan dan penyelenggaraan | PROCESS_FLOW | `NEW_TREATMENT_REQUIRED` | 3 | T04-DGM-01 — the unit's  | D-05 SmartArt production |
| `T04-SC-02` | Landskap Lembut — tiga operasi penyelenggaraan | CLICK_TO_REVEAL | `PROPOSED` | 5 | NONE — no source visual  | D-01 visual treatment |
| `T04-SC-03` | Racun — perundangan, HSE dan pengurusan risiko | SEQUENTIAL_STEPS | `PROPOSED` | 11 | NONE | D-04 legislative content |
| `T04-SC-04` | Landskap Lembut berbanding Landskap Kejur | COMPARISON | `NEW_TREATMENT_REQUIRED` | 5 | NONE | D-01 visual treatment |
| `T04-SC-05` | Landskap Kejur — empat kumpulan fungsi | CLICK_TO_REVEAL | `PROPOSED` | 6 | NONE | D-01 visual treatment |
| `T04-SC-06` | Rumusan dan kuiz | PENDING_HUMAN | `PENDING_BARIAH_REVIEW` | 0 | NONE | D-02 quiz structure; Rumusan approval |

# Detail

## `T04-SC-01` — Aliran proses penjagaan dan penyelenggaraan

| field | value |
|---|---|
| working_title | Aliran proses penjagaan dan penyelenggaraan |
| source_row_ids | T04-ROW-001; T04-ROW-002; T04-ROW-003 |
| source_heading_path | PENJAGAAN DAN PENYELENGGARAAN |
| instructional_purpose | Orient the learner to the six supervisory activities the module names as the maintenance process, before any single operation is taught. |
| learner_outcome | The learner can name the six activities and place them in order. |
| proposed_treatment | PROCESS_FLOW |
| source_visual_dependency | T04-DGM-01 — the unit's only visual |
| text_dependency | one introductory sentence, T04-ROW-002 |
| interaction_dependency | none proposed for the base state |
| narration_dependency | one screen-level VO; the six node labels are the spoken spine |
| technical_claim_dependency | none |
| bariah_decision_required | D-05 SmartArt production |
| unresolved_issue | how a vector SmartArt part becomes a storyboard visual |
| reusable_capability | shell, production panel, Notes schema, screen-level VO |
| new_capability_required | PROCESS_FLOW screen type — B02 has none |
| treatment_status | NEW_TREATMENT_REQUIRED |

## `T04-SC-02` — Landskap Lembut — tiga operasi penyelenggaraan

| field | value |
|---|---|
| working_title | Landskap Lembut — tiga operasi penyelenggaraan |
| source_row_ids | T04-ROW-004; T04-ROW-005; T04-ROW-006; T04-ROW-026; T04-ROW-046 |
| source_heading_path | PENJAGAAN DAN PENYELENGGARAAN; Landskap Lembut |
| instructional_purpose | Establish that soft-landscape maintenance is three named operations, and let the learner take them one at a time. |
| learner_outcome | The learner can name Siram, Baja and Racun and state what each is for. |
| proposed_treatment | CLICK_TO_REVEAL |
| source_visual_dependency | NONE — no source visual exists for any of the three |
| text_dependency | section intro T04-ROW-005 plus one definition per operation |
| interaction_dependency | three reveals, one per operation; all-viewed completion |
| narration_dependency | screen-level instruction only |
| technical_claim_dependency | none on this screen — the compliance load routes to T04-SC-03 |
| bariah_decision_required | D-01 visual treatment |
| unresolved_issue | whether three items justify a selection screen or three sequential screens |
| reusable_capability | completion-state treatment, all-viewed state, screen-level VO |
| new_capability_required | none |
| treatment_status | PROPOSED |

## `T04-SC-03` — Racun — perundangan, HSE dan pengurusan risiko

| field | value |
|---|---|
| working_title | Racun — perundangan, HSE dan pengurusan risiko |
| source_row_ids | T04-ROW-065; T04-ROW-066; T04-ROW-067; T04-ROW-068; T04-ROW-069; T04-ROW-071; T04-ROW-073; T04-ROW-075; T04-ROW-076; T04-ROW-077; T04-ROW-078 |
| source_heading_path | PENJAGAAN DAN PENYELENGGARAAN; Landskap Lembut; Racun |
| instructional_purpose | Carry the unit's entire compliance load — statute, licensing, PPE, storage, SDS, spray conditions, notification, reporting. |
| learner_outcome | The learner can state the contractor's legal and HSE obligations before pesticide work begins. |
| proposed_treatment | SEQUENTIAL_STEPS |
| source_visual_dependency | NONE |
| text_dependency | eleven source rows, verbatim |
| interaction_dependency | stepped progression; NO obligation gated behind an optional reveal |
| narration_dependency | high — this is the most assessable material in the unit |
| technical_claim_dependency | T04-CLM-01 Akta Racun Makhluk Perosak 1974, T04-CLM-02 licensed operator, T04-CLM-03 PPE, T04-CLM-04 SDS, T04-CLM-05 spray drift |
| bariah_decision_required | D-04 legislative content |
| unresolved_issue | whether legislative content may be reveal-gated at all |
| reusable_capability | Notes typed-block schema, production-instruction blocks |
| new_capability_required | none |
| treatment_status | PROPOSED |

## `T04-SC-04` — Landskap Lembut berbanding Landskap Kejur

| field | value |
|---|---|
| working_title | Landskap Lembut berbanding Landskap Kejur |
| source_row_ids | T04-ROW-004; T04-ROW-005; T04-ROW-079; T04-ROW-080; T04-ROW-100 |
| source_heading_path | PENJAGAAN DAN PENYELENGGARAAN |
| instructional_purpose | Make the unit's organising contrast explicit — living horticultural elements against permanent built elements. |
| learner_outcome | The learner can distinguish soft from hard landscape and say why each is maintained differently. |
| proposed_treatment | COMPARISON |
| source_visual_dependency | NONE |
| text_dependency | the two section definitions plus the source's own closing contrast statement, T04-ROW-100 |
| interaction_dependency | none proposed |
| narration_dependency | low |
| technical_claim_dependency | none |
| bariah_decision_required | D-01 visual treatment |
| unresolved_issue | whether the contrast earns a screen or is better left implicit |
| reusable_capability | shell and Notes only |
| new_capability_required | COMPARISON screen type — B02 has none |
| treatment_status | NEW_TREATMENT_REQUIRED |

## `T04-SC-05` — Landskap Kejur — empat kumpulan fungsi

| field | value |
|---|---|
| working_title | Landskap Kejur — empat kumpulan fungsi |
| source_row_ids | T04-ROW-079; T04-ROW-080; T04-ROW-081; T04-ROW-086; T04-ROW-091; T04-ROW-096 |
| source_heading_path | PENJAGAAN DAN PENYELENGGARAAN; Landskap Kejur |
| instructional_purpose | Present the four functions hard landscape performs, each with its two source sub-items. |
| learner_outcome | The learner can name the four functions and give an example of each. |
| proposed_treatment | CLICK_TO_REVEAL |
| source_visual_dependency | NONE |
| text_dependency | section intro plus four group headings and eight sub-items |
| interaction_dependency | four reveals; all-viewed completion |
| narration_dependency | screen-level instruction |
| technical_claim_dependency | none |
| bariah_decision_required | D-01 visual treatment |
| unresolved_issue | none anticipated |
| reusable_capability | completion-state treatment, all-viewed state |
| new_capability_required | none |
| treatment_status | PROPOSED |

## `T04-SC-06` — Rumusan dan kuiz

| field | value |
|---|---|
| working_title | Rumusan dan kuiz |
| source_row_ids | — |
| source_heading_path | — |
| instructional_purpose | Recap the unit and assess it. |
| learner_outcome | pending — depends on the assessment Bariah authors. |
| proposed_treatment | PENDING_HUMAN |
| source_visual_dependency | NONE |
| text_dependency | NONE IN SOURCE — the module contains no Rumusan and no quiz |
| interaction_dependency | quiz interaction structure exists in the shell |
| narration_dependency | follows the authored content |
| technical_claim_dependency | none |
| bariah_decision_required | D-02 quiz structure; Rumusan approval |
| unresolved_issue | content must be authored; 4+1 and 60% unconfirmed for PL06 |
| reusable_capability | Rumusan and quiz-review STRUCTURES (RP-007, RP-008, RP-011) |
| new_capability_required | none — the structures exist, the content does not |
| treatment_status | PENDING_BARIAH_REVIEW |
