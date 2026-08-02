# STAGE_4_2F_B0_5_QA_REPORT

Stage 4.2F-B0.5 — T04 pre-storyboard decision pack.

Suite: `docs/pl06/t04/tools/t04_pack_qa_v1.py` · Mutations: `docs/pl06/t04/tools/t04_pack_mutations_v1.py`

# 1. Test accounting

| Metric | Value |
|---|---:|
| `ACTIVE_TEST_GATES_PASSING` | **107 / 107** |
| `SUPERSESSION_MARKERS_PRESENT` | **0** |
| `TOTAL_EMITTED_GATE_RECORDS` | **107** |

Every record carries an explicit `gate_type`.

| `gate_type` | Gates |
|---|---:|
| `ARTIFACT_AGREEMENT` | 20 |
| `INVENTION_GUARD` | 16 |
| `AUTHORSHIP_GUARD` | 11 |
| `DECISION_INTEGRITY` | 11 |
| `PROPAGATION_GUARD` | 11 |
| `CONTRACT_INTEGRITY` | 10 |
| `MAPPING_INTEGRITY` | 10 |
| `SMARTART_FIDELITY` | 9 |
| `SAFETY_DISCLOSURE` | 7 |
| `ACCOUNTING` | 2 |

# 2. Mutation sensitivity

| | |
|---|---:|
| Fixtures | **39** |
| Detected | **39** |
| Missed | **0** |
| Baseline false failures | **0** |

The fixtures cover every prohibition this stage rests on: dropped source bindings, B02 family propagation, SmartArt node reorder and a seventh node, a `BARIAH_APPROVED` label on CAIR text, CAIR claiming instructional authorship, a pre-approved decision, an invented quiz question, an invented answer key, a confirmed 60 percent threshold, a PL06-wide cast, a legal obligation moved behind an optional reveal, and portability hours populated without a run.

## 2.1 One gate the fixtures caught first

`PASS_THRESHOLD_TREATED_AS_CONFIRMED` fired on the pack's own `not_produced` list — the entry that exists precisely to say *"confirmed 60 percent threshold"* is a thing we did **not** produce. Matching a prohibition as if it were a claim is the same false positive that hit `INVENTED_QUIZ_TEXT` at Stage 4.2F-B0. The scan now excludes the not-produced list, and a separate gate asserts that list still contains both entries.

# 3. The load-bearing gate

`LEGAL_ROWS_NOT_GATED_BEHIND_OPTIONAL_REVEAL`. All eleven legal, safety and compliance rows sit on `T04-CT-04`, visible in the base state. No `CLICK_TO_REVEAL` contract may contain one. Fixture `Y-29` moves a single row — the Akta citation — onto a reveal screen, and the gate fires.

# 4. What this suite cannot check

**Whether the proposals are instructionally right.** 107 green gates say every proposal traces to a source row, nothing is pre-approved, no B02 rule was propagated and no content was invented. They say nothing about whether `CLICK_TO_REVEAL` is the right treatment for three maintenance operations. That is Bariah's call and the pack exists to put it in front of her.

# 5. Verdict

```
T04_PRE_STORYBOARD_DECISION_PACK_READY_FOR_BARIAH
```

**No PPTX was generated in this stage.**

# 6. Full gate output

```
PASS  MAPPING_INTEGRITY   SCREEN_CANDIDATES                                                6
PASS  MAPPING_INTEGRITY   ALL_SIX_B0_CANDIDATES_REPRESENTED                                ['T04-SC-01', 'T04-SC-02', 'T04-SC-03', 'T04-SC-04', 'T04-SC-05', 'T04-SC-06']
PASS  MAPPING_INTEGRITY   MAPPING_TREATMENTS                                               ['CLICK_TO_REVEAL', 'CLICK_TO_REVEAL', 'COMPARISON', 'PENDING_HUMAN', 'PROCESS_FLOW', 'SEQUENTIAL_STEPS']
PASS  MAPPING_INTEGRITY   INVALID_TREATMENT_STATUSES                                       []
PASS  MAPPING_INTEGRITY   DUPLICATE_SCREEN_CANDIDATE_IDS                                   []
PASS  MAPPING_INTEGRITY   SCREEN_ROWS_NOT_IN_EXTRACT                                       []
PASS  MAPPING_INTEGRITY   SCREEN_WITHOUT_SOURCE_ROWS                                       []
PASS  MAPPING_INTEGRITY   EVERY_NON_PENDING_SCREEN_HAS_ROWS                                True
PASS  MAPPING_INTEGRITY   FINAL_SCREEN_COUNT_NOT_CLAIMED                                   'NOT_CLAIMED'
PASS  MAPPING_INTEGRITY   SCREEN_COUNT_NOT_DERIVED_FROM_B02                                False
PASS  CONTRACT_INTEGRITY  CONTRACTS                                                        6
PASS  CONTRACT_INTEGRITY  CONTRACT_TYPES                                                   ['CLICK_TO_REVEAL', 'CLICK_TO_REVEAL', 'COMPARISON', 'PENDING_HUMAN', 'PROCESS_FLOW', 'SEQUENTIAL_STEPS']
PASS  CONTRACT_INTEGRITY  DUPLICATE_CONTRACT_IDS                                           []
PASS  CONTRACT_INTEGRITY  CONTRACTS_MISSING_A_REQUIRED_FIELD                               []
PASS  CONTRACT_INTEGRITY  CONTRACT_ROWS_NOT_IN_EXTRACT                                     []
PASS  CONTRACT_INTEGRITY  CONTRACTS_NOT_PENDING_APPROVAL                                   []
PASS  CONTRACT_INTEGRITY  CONTRACTS_PRE_APPROVED                                           []
PASS  CONTRACT_INTEGRITY  PENDING_HUMAN_OPTION_COUNT                                       3
PASS  CONTRACT_INTEGRITY  PENDING_HUMAN_OPTIONS_HAVE_TRADEOFFS                             []
PASS  CONTRACT_INTEGRITY  PENDING_HUMAN_SILENTLY_CHOSE_A_TREATMENT                         True
PASS  SAFETY_DISCLOSURE   CLICK_TO_REVEAL_CONTRACTS                                        2
PASS  SAFETY_DISCLOSURE   REVEAL_HIDDEN_CONTENT_CLASSIFIED                                 ['SUPPLEMENTARY']
PASS  SAFETY_DISCLOSURE   REVEAL_JUSTIFICATION_PRESENT                                     []
PASS  SAFETY_DISCLOSURE   LEGAL_ROWS_NOT_GATED_BEHIND_OPTIONAL_REVEAL                      []
PASS  SAFETY_DISCLOSURE   LEGAL_ROWS_CARRIED_BY_A_CONTRACT                                 ['T04-ROW-065', 'T04-ROW-066', 'T04-ROW-067', 'T04-ROW-068', 'T04-ROW-069', 'T04-ROW-071', 'T04-ROW-073', 'T04-ROW-075', 'T04-ROW-076', 'T04-ROW-077', 'T04-ROW-078']
PASS  SAFETY_DISCLOSURE   LEGAL_OBLIGATIONS_VISIBLE_IN_BASE_STATE                          True
PASS  SAFETY_DISCLOSURE   COMPLIANCE_CONTRACT_HIDES_NOTHING_MANDATORY                      'NOT_APPLICABLE_NOTHING_MANDATORY_IS_HIDDEN'
PASS  SMARTART_FIDELITY   SMARTART_NODE_COUNT                                              6
PASS  SMARTART_FIDELITY   SMARTART_NODES_EXACT_AND_ORDERED                                 ['Koordinasi dan Demonstrasi Penyelenggaraan Taman', 'Penyeliaan Penyelenggaraan Taman', 'Penyeliaan Operasi Nurseri', 'Penyeliaan Alatan dan Mesin Penyelenggaraan Taman', 'Penyeliaan Inventori Taman', 'Perancangan Sumber Manusia dan Kebajikan Pekerja']
PASS  SMARTART_FIDELITY   SMARTART_NODES_MATCH_EXTRACT                                     ['Koordinasi dan Demonstrasi Penyelenggaraan Taman', 'Penyeliaan Penyelenggaraan Taman', 'Penyeliaan Operasi Nurseri', 'Penyeliaan Alatan dan Mesin Penyelenggaraan Taman', 'Penyeliaan Inventori Taman', 'Perancangan Sumber Manusia dan Kebajikan Pekerja']
PASS  SMARTART_FIDELITY   SMARTART_ASSET_SHA256                                            'f88edf2d305a546dfd05e45b9306503fbe7963bdd7ea1bcfe1ff9d74a1516e43'
PASS  SMARTART_FIDELITY   SMARTART_HIERARCHY_FLAT                                          True
PASS  SMARTART_FIDELITY   SMARTART_FLOW_DIRECTIONAL                                        'LINEAR_LEFT_TO_RIGHT'
PASS  SMARTART_FIDELITY   SMARTART_TREATMENT_STATUS                                        'PENDING_BARIAH_REVIEW'
PASS  SMARTART_FIDELITY   SMARTART_ASSET_PRODUCTION_NOT_STARTED                            ['NOT_STARTED', 'NOT_STARTED_IN_THIS_STAGE']
PASS  SMARTART_FIDELITY   SMARTART_BOTH_TREATMENTS_DEFINED                                 True
PASS  AUTHORSHIP_GUARD    RUMUSAN_CONTENT_STATUS                                           'CAIR_ASSISTED_DRAFT'
PASS  AUTHORSHIP_GUARD    RUMUSAN_APPROVAL_STATUS                                          'PENDING_BARIAH_REVIEW'
PASS  AUTHORSHIP_GUARD    INSTRUCTIONAL_AUTHORITY_IS_BARIAH                                ['BARIAH', 'BARIAH', 'BARIAH']
PASS  AUTHORSHIP_GUARD    BARIAH_IS_SOLE_ID                                                True
PASS  AUTHORSHIP_GUARD    CAIR_CLAIMS_INSTRUCTIONAL_AUTHORSHIP                             []
PASS  AUTHORSHIP_GUARD    FORBIDDEN_LABEL_ID_AUTHORED                                      False
PASS  AUTHORSHIP_GUARD    FORBIDDEN_LABEL_BARIAH_APPROVED                                  False
PASS  AUTHORSHIP_GUARD    FORBIDDEN_LABEL_FINAL_INSTRUCTIONAL_CONTENT                      False
PASS  AUTHORSHIP_GUARD    FORBIDDEN_LABEL_APPROVED                                         False
PASS  AUTHORSHIP_GUARD    FORBIDDEN_LABEL_FINAL                                            False
PASS  AUTHORSHIP_GUARD    DECISIONS_PRE_APPROVED                                           []
PASS  INVENTION_GUARD     RUMUSAN_STATEMENTS                                               5
PASS  INVENTION_GUARD     RUMUSAN_STATEMENTS_WITHOUT_SOURCE_ROWS                           []
PASS  INVENTION_GUARD     RUMUSAN_ROWS_NOT_IN_EXTRACT                                      []
PASS  INVENTION_GUARD     RUMUSAN_STATEMENTS_WITHOUT_RISK_STATUS                           []
PASS  INVENTION_GUARD     RUMUSAN_CLAIMS_MODULE_ORIGIN                                     True
PASS  INVENTION_GUARD     RUMUSAN_REVIEW_TABLE_COLUMNS                                     ['accept', 'edit', 'remove', 'comment']
PASS  INVENTION_GUARD     QUIZ_STRUCTURE_UNRESOLVED                                        'AUTHORITY_UNRESOLVED'
PASS  INVENTION_GUARD     QUIZ_CONTENT_BLUEPRINT_ONLY                                      'BLUEPRINT_ONLY'
PASS  INVENTION_GUARD     FINAL_QUIZ_QUESTION_PRESENT                                      []
PASS  INVENTION_GUARD     FINAL_ANSWER_KEY_PRESENT                                         []
PASS  INVENTION_GUARD     QUIZ_BLUEPRINT_ROWS_NOT_IN_EXTRACT                               []
PASS  INVENTION_GUARD     QUIZ_BLUEPRINT_WITHOUT_SOURCE_ROWS                               []
PASS  INVENTION_GUARD     QUIZ_STRUCTURE_OPTIONS                                           2
PASS  INVENTION_GUARD     PASS_THRESHOLD_TREATED_AS_CONFIRMED                              []
PASS  INVENTION_GUARD     QUIZ_COMPOSITION_TREATED_AS_CONFIRMED                            []
PASS  INVENTION_GUARD     CONFIRMED_STRUCTURE_LISTED_AS_NOT_PRODUCED                       ['confirmed 4 MCQ + 1 MR structure', 'confirmed 60 percent threshold']
PASS  PROPAGATION_GUARD   B02_PROPAGATION_FAMILY_S                                         []
PASS  PROPAGATION_GUARD   B02_PROPAGATION_FAMILY_P1                                        []
PASS  PROPAGATION_GUARD   B02_PROPAGATION_FAMILY_P2                                        []
PASS  PROPAGATION_GUARD   B02_PROPAGATION_PAPAN_TANDA                                      []
PASS  PROPAGATION_GUARD   B02_PROPAGATION_BBQ_PIT                                          []
PASS  PROPAGATION_GUARD   B02_PROPAGATION_ALYA                                             []
PASS  PROPAGATION_GUARD   B02_PROPAGATION_ENCIK_RAHMAN                                     []
PASS  PROPAGATION_GUARD   B02_FAMILY_IN_CONTRACTS                                          []
PASS  PROPAGATION_GUARD   CAST_DECISION_SCOPE                                              True
PASS  PROPAGATION_GUARD   CAST_NOT_PROPAGATED_PL06_WIDE                                    True
PASS  PROPAGATION_GUARD   B02_CAST_NAMES_PROPOSED                                          []
PASS  DECISION_INTEGRITY  DECISION_COUNT                                                   5
PASS  DECISION_INTEGRITY  DECISION_IDS                                                     ['D-01', 'D-02', 'D-03', 'D-04', 'D-05']
PASS  DECISION_INTEGRITY  DECISIONS_MISSING_A_FIELD                                        []
PASS  DECISION_INTEGRITY  DECISION_SCREENS_NOT_IN_CONTRACTS                                []
PASS  DECISION_INTEGRITY  D01_RECOMMENDATION                                               True
PASS  DECISION_INTEGRITY  D03_RECOMMENDATION                                               True
PASS  DECISION_INTEGRITY  PORTABILITY_STATUS                                               'TEMPLATE_NOT_YET_MEASURED'
PASS  DECISION_INTEGRITY  PORTABILITY_SCORE_NOT_CALCULATED                                 'NOT_CALCULATED'
PASS  DECISION_INTEGRITY  PORTABILITY_METRIC_COUNT                                         16
PASS  DECISION_INTEGRITY  PORTABILITY_FABRICATED_MEASUREMENTS                              []
PASS  DECISION_INTEGRITY  PORTABILITY_BANDS                                                4
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_SOURCE_TO_SCREEN_MAPPING_v1.md          True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_SOURCE_TO_SCREEN_MAPPING_v1.json        True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_SCREEN_CONTRACTS_DRAFT_v1.md            True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_SCREEN_CONTRACTS_DRAFT_v1.json          True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_SMARTART_SIX_NODE_CONTRACT_v1.md        True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_RUMUSAN_CAIR_ASSISTED_DRAFT_v1.md       True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_QUIZ_BLUEPRINT_v1.md                    True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_BARIAH_DECISION_PACK_v1.md              True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_BARIAH_WHATSAPP_DRAFT_v1.md             True
PASS  ARTIFACT_AGREEMENT  DELIVERABLE_PRESENT::T04_PORTABILITY_MEASUREMENT_TEMPLATE_v1.md  True
PASS  ARTIFACT_AGREEMENT  EMITTED_DELIVERABLES_STALE                                       []
PASS  ARTIFACT_AGREEMENT  MAPPING_JSON_MATCHES_DATA                                        ['T04-SC-01', 'T04-SC-02', 'T04-SC-03', 'T04-SC-04', 'T04-SC-05', 'T04-SC-06']
PASS  ARTIFACT_AGREEMENT  CONTRACTS_JSON_MATCHES_DATA                                      ['T04-CT-01', 'T04-CT-02', 'T04-CT-03', 'T04-CT-04', 'T04-CT-05', 'T04-CT-06']
PASS  ARTIFACT_AGREEMENT  MAPPING_MD_JSON_DIVERGENCE                                       []
PASS  ARTIFACT_AGREEMENT  CONTRACTS_MD_JSON_DIVERGENCE                                     []
PASS  ARTIFACT_AGREEMENT  WHATSAPP_DRAFT_NOT_SENT                                          True
PASS  ARTIFACT_AGREEMENT  WHATSAPP_DRAFT_STATES_DRAFT_STATUS                               True
PASS  ARTIFACT_AGREEMENT  GIT_INDEX_READ                                                   True
PASS  ARTIFACT_AGREEMENT  PPTX_GENERATED                                                   []
PASS  ARTIFACT_AGREEMENT  GENERATOR_MODIFIED                                               ''
PASS  ACCOUNTING          DUPLICATE_GATE_IDS                                               []
PASS  ACCOUNTING          EVERY_GATE_CARRIES_A_TYPE                                        []

107/107 active gates PASS  ·  0 supersession markers  ·  107 emitted records
```
