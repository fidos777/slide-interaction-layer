# REGRESSION_REPLAY_REPORT — v0.4.4.1

Harness: `generator/audit/b02_replay_v0_4_4_1.py`. Fixtures are written to a temp directory
and deleted; no mutated artifact is committed.

A mutation fixture proves **gate sensitivity** only. It never proves the corrected value is
right — that is the oracle's and the frozen contract's job.

# 1. The corrected artifact

| | |
|---|---:|
| Gate records emitted against `…v0_4_4_1.pptx` | 461 |
| Passing | **461** |
| `CORRECTED_V0_4_4_1_FALSE_FAILURES` | **0** |

# 2. Mutation sensitivity

| | |
|---|---:|
| Fixtures run | **51** |
| Detected | **51** |
| `MUTATION_FIXTURES_MISSED` | **0** |

39 are the Stage 4.2E-B fixtures rebased onto v0.4.4.1 — every one still fires, so nothing
this stage changed blunted an existing gate. Twelve are new.

| Fixture | Kind | Injected defect | Designated gates that fired |
|---|---|---|---|
| `M-01` | package | panel version line reverted to v0.4 | `PANEL_VERSION_MANIFEST_MISMATCHES`, `SUPERSEDED_VERSION_LINES_IN_PANEL`, `PANEL_VERSION_EQUALS_RUN_MANIFEST_VERSION` |
| `M-02` | package | a panel status token reverted to the retired one | `PANEL_STATUS_MANIFEST_MISMATCHES`, `PANEL_STATUS_EQUALS_ACTIVE_PACKAGE_STATUS`, the stale-token gate |
| `M-03` | package | retired confirmation token reinserted on one page | `STALE_RELEASE_TOKENS_ANYWHERE_IN_PANEL`, its stale-token gate |
| `M-04` | package | a component main set back to `CONDITIONAL` | `COMPONENT_MAIN_VISUAL_REQUIREMENT_REQUIRED`, `…_ACTIVE_VISUAL_GOVERNANCE_CURRENT`, `…_STALE_GOVERNANCE_STRINGS_IN_VISUAL_BLOCK` |
| `M-05` | package | a component-main mapping status set back to pending | `COMPONENT_MAIN_MAPPING_STATUS_RESOLVED` + the two above |
| `M-06` | package | provisional-proposal class reinserted | `COMPONENT_MAIN_PROVISIONAL_VISUAL_PROPOSALS`, `…_ACTIVE_VISUAL_GOVERNANCE_CURRENT` |
| `M-07` | package | subject provenance promoted to `BARIAH_DIRECT` on the page | `COMPONENT_MAIN_SUBJECT_PROVENANCE_ON_PAGE` |
| `M-08` | registry | the `GEX-001` exemption entry removed | `OFF_CANVAS_PLACEHOLDER_EXEMPTION_REGISTERED`, `SHAPES_BEYOND_TOP_EDGE`, `UNREGISTERED_OFF_CANVAS_EXEMPTIONS` |
| `M-09` | package | ordinary text box at the placeholder's exact negative coordinates | `SHAPES_BEYOND_TOP_EDGE`, `UNREGISTERED_OFF_CANVAS_EXEMPTIONS`, `ORDINARY_OFF_CANVAS_SHAPES_ALLOWED` |
| `M-10` | package | ordinary box renamed `Title 1`, no placeholder type | the three above + `TITLE_PLACEHOLDER_IS_A_REAL_PLACEHOLDER` |
| `M-11` | package | the registered placeholder moved to a different y | `SHAPES_BEYOND_TOP_EDGE`, `UNREGISTERED_OFF_CANVAS_EXEMPTIONS`, `EXEMPTED_SHAPES_EVALUATED` |
| `M-12` | contract | a subject promoted to `BARIAH_DIRECT` in the frozen mapping | fail-closed: `component_main_governance()` raises |

`M-09` and `M-10` are the two fixtures Part 4 requires for a registered exemption: an
ordinary shape at the same coordinates must fail, and only the exact registered placeholder
class may pass. `M-11` adds the third direction — moving the registered shape revokes its own
exemption, so the entry cannot be used as a licence for a band of coordinates.

`M-08`, `M-11` and `M-12` do not mutate the package. `M-08` swaps the exemption registry,
`M-12` swaps the frozen mapping contract, and the harness reverts each patch in a `finally`
before the next fixture runs. `M-12` is detected as a raise rather than a red gate, which is
the intended behaviour: a promoted provenance is refused at source rather than reported.

# 3. Historical replay — **not** a quality ranking

Earlier committed decks run against the *current* suite.

| Deck | Gates failing |
|---|---:|
| `…v0_4.pptx` | 121 |
| `…v0_4_1.pptx` | 72 |
| `…v0_4_2.pptx` | 74 |
| `…v0_4_3.pptx` | 58 |
| `…v0_4_4.pptx` | **33** |
| `…v0_4_4_1.pptx` | **0** |

Every one of these decks was READY under the oracle in force when it was built. The numbers
rise because the suite grew, not because the decks decayed.

## 3.1 All 33 v0.4.4 failures, classified

v0.4.4 is the accepted `B02_V0_4_4_CONSOLIDATED_BUILD_READY_FOR_POWERPOINT_SMOKE` build, and
its 33 failures are the defect this stage corrected — measured by the gates this stage added.
There is no third category.

**`ARTIFACT_METADATA_DRIFT` — 20 gates.** `ACTIVE_PANEL_VERSION`, `PANEL_VERSION_MISMATCHES`,
`PANEL_VERSION_MANIFEST_MISMATCHES`, `PANEL_VERSION_EQUALS_RUN_MANIFEST_VERSION`,
`SUPERSEDED_VERSION_LINES_IN_PANEL`, `SUPERSEDED_VERSION_LINES_IN_PACKAGE`,
`PANEL_STATUS_TOKEN_SET_MISMATCHES`, `PANEL_STATUS_MANIFEST_MISMATCHES`,
`PANEL_STATUS_EQUALS_ACTIVE_PACKAGE_STATUS`, `STALE_RELEASE_TOKENS`,
`STALE_RELEASE_TOKENS_ANYWHERE_IN_PANEL`, the three `STALE_STATUS_TOKEN_*`, the five
`PACKAGE_TOKEN_*` for tokens v0.4.4 does not carry, and
`MANIFEST_DECK_FILENAME_MATCHES_ARTIFACT`. This is B02-META-REG-001 measured directly.

**`SUPERSEDED_GOVERNANCE_POSITION` — 13 gates.** The whole `COMPONENT_MAIN_*` family. v0.4.4's
component-main blocks state `CONDITIONAL` / pending / provisional, which was the correct
position *before* the requirement and treatment were settled and the 9/9 mapping frozen —
and which v0.4.4 continued to print after they were. The visuals themselves are present and
correct in v0.4.4; only the metadata describing them was stale.

20 + 13 = 33. There is no third group, and the absence of one is the interesting part: **no
geometry gate fails on v0.4.4.** It passes `UNREGISTERED_OFF_CANVAS_EXEMPTIONS`,
`ORDINARY_OFF_CANVAS_SHAPES_ALLOWED` and all four edge gates, because its two off-stage
shapes are the same two the registry now covers, at the same coordinates. The geometry defect
was in the **rule**, not in the artifact — which is why correcting it moved no shape and
changed no byte on any page.

No v0.4.4 failure is a `TRUE_HISTORICAL_REGRESSION`. No learner-facing gate fails on v0.4.4
under this suite, which is the same statement as §6 of the release report from the other
direction: the two decks are identical everywhere a learner can see.
