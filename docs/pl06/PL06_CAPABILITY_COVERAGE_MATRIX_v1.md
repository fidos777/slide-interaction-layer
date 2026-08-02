# PL06_CAPABILITY_COVERAGE_MATRIX — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py`.

```
LANE_A_EXISTING_SUPPORTED_PATTERN = 1
LANE_B_SUPPORTED_WITH_SOURCE_MAPPING = 0
LANE_C_NEW_TREATMENT_OR_DECISION_REQUIRED = 0
LANE_D_SOURCE_INCOMPLETE = 7
```

> One unit is Lane A and it is the one already delivered. Every remaining unit is Lane D. That is not a statement about our generator — the shell, the Notes schema, the geometry registry and the identity discipline are all ready. It is a statement about custody: there is no source to point them at.

# Lane assignment

| unit_id | lane | effort | source-authority dependency |
|---|---|---|---|
| `K5-PL06-T03-B02` | LANE_A_EXISTING_SUPPORTED_PATTERN | 0 — delivered | MS2680, B02-CAIR-INT-001 |
| `K5-PL06-T04` | LANE_D_SOURCE_INCOMPLETE | NOT_EVIDENCED — cannot be estimated without source | STOP-001, STOP-002 |
| `K5-PL06-T02` | LANE_D_SOURCE_INCOMPLETE | NOT_EVIDENCED — cannot be estimated without source | STOP-001, STOP-002 |
| `K5-PL06-T03-BNEXT` | LANE_D_SOURCE_INCOMPLETE | NOT_EVIDENCED — cannot be estimated without source | STOP-001, STOP-002 |
| `K5-PL06-T01` | LANE_D_SOURCE_INCOMPLETE | NOT_EVIDENCED — cannot be estimated without source | STOP-001, STOP-002 |
| `K5-PL06-T05` | LANE_D_SOURCE_INCOMPLETE | NOT_EVIDENCED — cannot be estimated without source | STOP-001, STOP-002 |
| `K5-PL06-T06` | LANE_D_SOURCE_INCOMPLETE | NOT_EVIDENCED — cannot be estimated without source | STOP-001, STOP-002 |
| `K5-PL06-T07` | LANE_D_SOURCE_INCOMPLETE | NOT_EVIDENCED — cannot be estimated without source | STOP-001, STOP-002 |

# Detail

## `K5-PL06-T03-B02`

| field | value |
|---|---|
| lane | LANE_A_EXISTING_SUPPORTED_PATTERN |
| supported_screen_types | TOPIC_ENTRY; DIALOG; ORIENTATION; GROUP_MASTER; GROUP_VISUAL_GATEWAY; COMPONENT_MAIN; EXAMPLE_SELECTION; EXAMPLE_DETAIL; EXAMPLE_POPUP; SPECIFICATION_POPUP; COMPLETION_STATE; RUMUSAN; QUIZ; TAMAT |
| unsupported_screen_types |  |
| supported_interaction_types | FAMILY_S; FAMILY_P1; FAMILY_P2 |
| missing_generator_capability |  |
| missing_package_oracle |  |
| missing_mutation_fixture |  |
| missing_visual_binding |  |
| missing_notes_handling |  |
| missing_quiz_handling |  |
| source_authority_dependency | MS2680, B02-CAIR-INT-001 |
| estimated_implementation_effort | 0 — delivered |

## `K5-PL06-T04`

| field | value |
|---|---|
| lane | LANE_D_SOURCE_INCOMPLETE |
| supported_screen_types | TOPIC_ENTRY; DIALOG; ORIENTATION; RUMUSAN; QUIZ; TAMAT |
| unsupported_screen_types | UNKNOWN — the unit's screen inventory cannot be derived without its source |
| supported_interaction_types | none proven — the B02 families are not transferable |
| missing_generator_capability | content model for this unit |
| missing_package_oracle | no frozen artifact to hash |
| missing_mutation_fixture | all unit-specific fixtures |
| missing_visual_binding | all — no assets extracted |
| missing_notes_handling | unit VO content |
| missing_quiz_handling | questions, options and answer key |
| source_authority_dependency | STOP-001, STOP-002 |
| estimated_implementation_effort | NOT_EVIDENCED — cannot be estimated without source |

## `K5-PL06-T02`

| field | value |
|---|---|
| lane | LANE_D_SOURCE_INCOMPLETE |
| supported_screen_types | TOPIC_ENTRY; DIALOG; ORIENTATION; RUMUSAN; QUIZ; TAMAT |
| unsupported_screen_types | UNKNOWN — the unit's screen inventory cannot be derived without its source |
| supported_interaction_types | none proven — the B02 families are not transferable |
| missing_generator_capability | content model for this unit |
| missing_package_oracle | no frozen artifact to hash |
| missing_mutation_fixture | all unit-specific fixtures |
| missing_visual_binding | all — no assets extracted |
| missing_notes_handling | unit VO content |
| missing_quiz_handling | questions, options and answer key |
| source_authority_dependency | STOP-001, STOP-002 |
| estimated_implementation_effort | NOT_EVIDENCED — cannot be estimated without source |

## `K5-PL06-T03-BNEXT`

| field | value |
|---|---|
| lane | LANE_D_SOURCE_INCOMPLETE |
| supported_screen_types | TOPIC_ENTRY; DIALOG; ORIENTATION; RUMUSAN; QUIZ; TAMAT |
| unsupported_screen_types | UNKNOWN — the unit's screen inventory cannot be derived without its source |
| supported_interaction_types | none proven — the B02 families are not transferable |
| missing_generator_capability | content model for this unit |
| missing_package_oracle | no frozen artifact to hash |
| missing_mutation_fixture | all unit-specific fixtures |
| missing_visual_binding | all — no assets extracted |
| missing_notes_handling | unit VO content |
| missing_quiz_handling | questions, options and answer key |
| source_authority_dependency | STOP-001, STOP-002 |
| estimated_implementation_effort | NOT_EVIDENCED — cannot be estimated without source |

## `K5-PL06-T01`

| field | value |
|---|---|
| lane | LANE_D_SOURCE_INCOMPLETE |
| supported_screen_types | TOPIC_ENTRY; DIALOG; ORIENTATION; RUMUSAN; QUIZ; TAMAT |
| unsupported_screen_types | UNKNOWN — the unit's screen inventory cannot be derived without its source |
| supported_interaction_types | none proven — the B02 families are not transferable |
| missing_generator_capability | content model for this unit |
| missing_package_oracle | no frozen artifact to hash |
| missing_mutation_fixture | all unit-specific fixtures |
| missing_visual_binding | all — no assets extracted |
| missing_notes_handling | unit VO content |
| missing_quiz_handling | questions, options and answer key |
| source_authority_dependency | STOP-001, STOP-002 |
| estimated_implementation_effort | NOT_EVIDENCED — cannot be estimated without source |

## `K5-PL06-T05`

| field | value |
|---|---|
| lane | LANE_D_SOURCE_INCOMPLETE |
| supported_screen_types | TOPIC_ENTRY; DIALOG; ORIENTATION; RUMUSAN; QUIZ; TAMAT |
| unsupported_screen_types | UNKNOWN — the unit's screen inventory cannot be derived without its source |
| supported_interaction_types | none proven — the B02 families are not transferable |
| missing_generator_capability | content model for this unit |
| missing_package_oracle | no frozen artifact to hash |
| missing_mutation_fixture | all unit-specific fixtures |
| missing_visual_binding | all — no assets extracted |
| missing_notes_handling | unit VO content |
| missing_quiz_handling | questions, options and answer key |
| source_authority_dependency | STOP-001, STOP-002 |
| estimated_implementation_effort | NOT_EVIDENCED — cannot be estimated without source |

## `K5-PL06-T06`

| field | value |
|---|---|
| lane | LANE_D_SOURCE_INCOMPLETE |
| supported_screen_types | TOPIC_ENTRY; DIALOG; ORIENTATION; RUMUSAN; QUIZ; TAMAT |
| unsupported_screen_types | UNKNOWN — the unit's screen inventory cannot be derived without its source |
| supported_interaction_types | none proven — the B02 families are not transferable |
| missing_generator_capability | content model for this unit |
| missing_package_oracle | no frozen artifact to hash |
| missing_mutation_fixture | all unit-specific fixtures |
| missing_visual_binding | all — no assets extracted |
| missing_notes_handling | unit VO content |
| missing_quiz_handling | questions, options and answer key |
| source_authority_dependency | STOP-001, STOP-002 |
| estimated_implementation_effort | NOT_EVIDENCED — cannot be estimated without source |

## `K5-PL06-T07`

| field | value |
|---|---|
| lane | LANE_D_SOURCE_INCOMPLETE |
| supported_screen_types | TOPIC_ENTRY; DIALOG; ORIENTATION; RUMUSAN; QUIZ; TAMAT |
| unsupported_screen_types | UNKNOWN — the unit's screen inventory cannot be derived without its source |
| supported_interaction_types | none proven — the B02 families are not transferable |
| missing_generator_capability | content model for this unit |
| missing_package_oracle | no frozen artifact to hash |
| missing_mutation_fixture | all unit-specific fixtures |
| missing_visual_binding | all — no assets extracted |
| missing_notes_handling | unit VO content |
| missing_quiz_handling | questions, options and answer key |
| source_authority_dependency | STOP-001, STOP-002 |
| estimated_implementation_effort | NOT_EVIDENCED — cannot be estimated without source |

# What is portable today, independent of any unit

The capability that would survive contact with a new unit right now:

- the review shell and its stage geometry (RP-001)
- the S01/S02/S03 grammar as *structure* (RP-002)
- the production panel and the artifact-identity discipline (RP-003, RP-014)
- the typed Notes block schema (RP-004)
- the italics *mechanism*, not the term list (RP-005)
- completion-state, Rumusan, quiz-review and Tamat treatments (RP-006 – RP-012)
- the registered off-canvas geometry treatment (RP-013)
- the oracle contract and population-pinning discipline (RP-016, RP-017)

What is not portable is everything that touches content: the families, the components, the cardinalities, the subjects, the counts and the glossary.
