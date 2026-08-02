# STAGE_4_2F_A_RUN_MANIFEST

```
STAGE = 4.2F-A — PL06 SCALE-OUT INVENTORY AND FIRST PROOF SELECTION
SCOPE = INVENTORY_AND_PLANNING_ONLY
STORYBOARDS_GENERATED = 0
VERDICT = PL06_SCALE_OUT_BLOCKED_BY_UNRESOLVED_UNIT_BOUNDARIES
```

# 1. Pre-flight

| Check | Result |
|---|---|
| Repository | `/home/user/slide-interaction-layer` |
| Branch | `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at start | `788e178` — matches expected |
| Working tree at start | clean |
| Stage 4.2E-C commit | present — `788e178 fix(storyboard): align B02 v0.4.4 artifact metadata with release status` |
| v0.4.4.1 artifact | present |
| Artifact bytes | **471,881** — matches expected |
| Artifact SHA-256 | `faef6c85745d2750236ffdf23fb7d14b81d26ed37c7db58ed274cb8d0f0178e5` — matches expected |
| B02 QA suite reproduces | **461 / 461 PASS** |
| B02 mutation fixtures reproduce | **51 / 51 detected, 0 missed, 0 false failures** |
| Uncommitted generated artifacts | none |

Historical replay reproduced unchanged: v0.4 = 121, v0.4.1 = 72, v0.4.2 = 74, v0.4.3 = 58,
v0.4.4 = 33, v0.4.4.1 = 0.

# 2. Source located

## 2.1 PL06 source documents

**None.** There is no PL06 module DOCX, PDF or extract anywhere in this repository.

The only module content this project has ever held is a **14-page extract of Topik 3
Bahagian 2** — `K5_PL06_T03_B02_pages_256269.pdf`, sha256 `30a6903d…`, 429,918 B, covering
modul ms 238–249 — and that file is itself absent; only the 14 JPEGs extracted from it
survive, in `reviews/source-completion/source-assets/`.

This is a re-confirmation of a finding already on record:
`reviews/sample-19slides/SOURCE_CUSTODY_AND_COVERAGE.md` F2, `MEASURED_FACT` —
*"The approved K5 module is not present."*

## 2.2 Existing PL06 storyboard inputs

| Artifact | Scope |
|---|---|
| `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_1 … v0_4_4_1.pptx` (8 decks) | T03 B02 only |
| `K5PL06T03B02_19SLIDE_VISUAL_TREATMENT_SAMPLE_v0_1/2.pptx` | T03 B02 only |
| `K5PL06T03B02_3SCREEN_IMPLEMENTATION_PREFLIGHT_v0_1/2/3.pptx` | T03 B02 only |
| `K5PL06T03B02_v0_4_THREE_FAMILY_PROOF.pptx` | T03 B02 only |

Every storyboard input in the repository is B02.

## 2.3 Bariah-provided PL inputs

| Ref | Artifact | Bytes | SHA-256 |
|---|---|---:|---|
| M1 | `SB_K5_montaj_v1.pptx` | 61,292 | `79a07b460ddb940d…` |
| M2 | `SB_K5PL6_montaj_v1.pptx` | 70,656 | `97ccab1c2aef8891…` |
| A1 | `…v0_3_vBariah.pptx` | 365,773 | `cdfc78e639561…` |
| A2 | `Panduan_Semakan_Bariah_…v0.3_vBariah.docx` | 43,342 | `c15ae05e20358…` |
| A3 | `K5_PL06_T03_B02_UPDATED_SG_v0.3.docx` | 56,475 | `f3166e42f84d4…` |
| — | 7 decision screenshots | — | frozen, Stage 4.2C / 4.2E-A / 4.2E-B |

**M2 is the only artifact in the repository that describes PL06 above the B02 slice.** It
carries the seven Topik and their titles on slide 3. It carries no Bahagian.

## 2.4 Source mappings

`STORYBOARD_SOURCE_MAP_v0.4.md` (26 rows), `TABLE_ROW_TO_POPUP_MATRIX.md`,
`COMPONENT_OVERVIEW_MAPPING_v0.4.4.json`, `B02_ASSET_MANIFEST.md` — all B02-scoped.

## 2.5 Figures, tables and extracted assets

14 JPEGs in `reviews/source-completion/source-assets/`, all `K5PL06T03-B02-IMG-p2xx-xNN`.
**Zero extracted assets exist for any other PL06 unit.**

## 2.6 Quiz and Rumusan sources

B02 only, in `b02_proof_content_v0_4.py` and `QUIZ_FEEDBACK_REGISTER_v0.4.4.json`.
No quiz or Rumusan source exists for any other unit.

## 2.7 B02-specific generators and validators

Everything under `reviews/source-completion/generator/` is B02-scoped by content, though
much of it is portable by structure — see `PL06_RULE_PORTABILITY_MATRIX_v1.md`:

`v0_4/` — `b02_generator_v0_4`, `b02_model_adapter_v0_4`, `b02_proof_content_v0_4`,
`b02_visual_policy_v0_4`, `b02_visual_directions_v0_4`, `b02_glossary_v0_4`,
`b02_instructions_v0_4`, `b02_overview_mapping_v0_4_4`, `b02_artifact_identity_v0_4_4_1`,
`b02_geometry_exemptions_v0_4_4_1`, `b02_release_artifacts_v0_4_4_1`, and five chained QA
suites. `audit/` — four oracle modules, four replay harnesses, one population auditor.
`generator/` root — the frozen v0.3 toolchain, hash-verified again this stage.

# 3. What this stage produced

| Artifact | Kind |
|---|---|
| `PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.md` | emitted |
| `PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.csv` | emitted from the same pass |
| `PL06_RULE_PORTABILITY_MATRIX_v1.md` | emitted |
| `PL06_CAPABILITY_COVERAGE_MATRIX_v1.md` | emitted |
| `PL06_FIRST_SCALE_OUT_SELECTION_v1.md` | emitted |
| `PL06_EXECUTION_PLAN_v1.md` | emitted |
| `PL06_OPEN_AUTHORITY_ITEMS_v1.md` | emitted |
| `B02_BARIAH_CALL_APPROVAL_RECORD_v1.md` | emitted |
| `STAGE_4_2F_A_RUN_MANIFEST.md` | this file |
| `STAGE_4_2F_A_QA_REPORT.md` | hand-written from measured runs |
| `tools/pl06_inventory_data_v1.py` | the one controlled data source |
| `tools/pl06_emit_v1.py` | emitter — Markdown and CSV in one pass |
| `tools/pl06_inventory_qa_v1.py` | 82 typed gates |
| `tools/pl06_inventory_mutations_v1.py` | 32 negative fixtures |

No new registry was created. The inventory, the rule matrix, the stop register and the plan
all live in one controlled data module because no existing controlled structure holds
PL06-scope planning data — every existing register in this repository is B02-scoped by
construction.

# 4. Totals

| Metric | Value |
|---|---:|
| PL06 Topik enumerated | **7 of 7** |
| PL06 Bahagian enumerated | **1** (B02, delivered) + **1** attested without a number |
| Inventory units | **8** |
| Units delivered | 1 |
| Units remaining | 7 |
| Units `READY` | **0** |
| Units `READY_WITH_HOLDS` | 1 — the delivered B02 |
| Units `SOURCE_AUTHORITY_UNRESOLVED` | **7** |
| `LANE_A` | 1 · `LANE_B` 0 · `LANE_C` 0 · `LANE_D` **7** |
| Rules classified | 40 — global 17, source-bound 8, B02-specific 15 |
| Stop conditions | 12 — `BLOCKS_THIS_UNIT` 6, freeze-only 2, MMD-only 1, release-only 3 |
| Source anomalies | 3 |
| QA gates | **82 / 82** |
| Mutation fixtures | **32 / 32 detected** |
| Storyboards generated | **0** |

# 5. Constraints honoured

- The B02 approved deck was not modified; its hash is unchanged.
- No PPTX was generated, manually patched, or opened.
- No MMD, React or SCORM work was begun.
- No remaining storyboard was generated.
- `788e178` was not amended.
- The frozen v0.3 toolchain hashes were verified unchanged.
- No canonical freeze, MMD readiness or production release is claimed.
- The call approval is classified `FIRDAUS_ATTESTED_BARIAH_CALL` and nothing stronger.
