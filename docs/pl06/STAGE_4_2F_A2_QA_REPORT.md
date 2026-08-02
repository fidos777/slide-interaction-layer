# STAGE_4_2F_A2_QA_REPORT

Stage 4.2F-A2 — controlled PL06 source ingest.

Suite: `docs/pl06/tools/pl06_inventory_qa_v1.py`  ·  Mutations: `docs/pl06/tools/pl06_inventory_mutations_v1.py`

# 1. Test accounting

| Metric | Value |
|---|---:|
| `ACTIVE_TEST_GATES_PASSING` | **136 / 136** |
| `SUPERSESSION_MARKERS_PRESENT` | **0** |
| `TOTAL_EMITTED_GATE_RECORDS` | **136** |

Every record carries an explicit `gate_type`. Nothing is classified by ID substring.

| `gate_type` | Gates |
|---|---:|
| `BOUNDARY_INTEGRITY` | 23 |
| `AUTHORITY_DISCIPLINE` | 22 |
| `INVENTORY_INTEGRITY` | 18 |
| `ARTIFACT_AGREEMENT` | 17 |
| `SELECTION_INTEGRITY` | 13 |
| `SOURCE_CUSTODY` | 13 |
| `STOP_CONDITION` | 10 |
| `PLAN_INTEGRITY` | 9 |
| `RULE_PORTABILITY` | 9 |
| `ACCOUNTING` | 2 |

# 2. Mutation sensitivity

| | |
|---|---:|
| Fixtures | **54** |
| Detected | **54** |
| `MUTATION_FIXTURES_MISSED` | **0** |
| Baseline false failures | **0** |

Twenty-two fixtures are new to this stage. They found **five gates that the inventory rewrite had silently switched off** — four matching literals or populations that no longer existed, and one that could be deleted along with its own guard entry. All five were fixed at the gate. See `STAGE_4_2F_A2_RUN_MANIFEST.md` §8.1.

# 3. What this suite checks

That the inventory is internally honest and that the ingest is faithful: every unit traces to frozen evidence; the 14 units, the 3/2/5/1/1/1/1 topology and the six shared boundary pages match the frozen map; B02's bahagian title is not its Topik title; `T03-B03` is resolved and no placeholder survives; T04's range is 276–283 with its two boundary images present; all thirteen ingested files still hash to the freeze; no DOCX, PDF or ZIP is in the Git index; Git LFS is not configured; the grouping authority and every custody status is explicit; exactly two stop conditions are resolved; and the frozen map's JSON, CSV and Markdown agree.

# 4. What it cannot check

**That the fourteen units are the right fourteen.** The boundaries are anchored to named DOCX headings and are checkable; the grouping behind them is `REFERENCED_NOT_FROZEN`. 136 green gates say the map was ingested faithfully and the inventory reads it correctly. They say nothing about whether Topik 1 should have been three lessons.

**Any unit's content.** Nobody has read a page. Rumusan, quiz, visual inventory and interaction treatment are unknown for all thirteen remaining units — that is precisely what this stage left open, and `SOURCE_INCOMPLETE` says so.

# 5. Verdict

```
PL06_SOURCE_BOUNDARY_INGEST_COMPLETE_READY_FOR_T04_EXTRACTION
```

Not claimed: `PL06_STORYBOARDS_COMPLETE`, `PL06_READY_FOR_MMD`, `PL06_CANONICALLY_FROZEN`, `PL06_PRODUCTION_RELEASED`.

**No PPTX was generated in this stage.**

# 6. Full gate output

```
PASS  INVENTORY_INTEGRITY   INVENTORY_UNITS_EVALUATED                                         True
PASS  INVENTORY_INTEGRITY   UNITS_WITHOUT_SOURCE_REFERENCE                                    []
PASS  INVENTORY_INTEGRITY   UNITS_WITHOUT_EVIDENCE_REF_IN_SOURCE_REFERENCE                    []
PASS  INVENTORY_INTEGRITY   DUPLICATE_UNIT_IDS                                                []
PASS  INVENTORY_INTEGRITY   DUPLICATE_TOPIK_BAHAGIAN_COMBINATIONS                             []
PASS  INVENTORY_INTEGRITY   INVALID_READINESS_VALUES                                          []
PASS  INVENTORY_INTEGRITY   INVALID_LANE_VALUES                                               []
PASS  INVENTORY_INTEGRITY   INVALID_UNIT_SCOPE_VALUES                                         []
PASS  INVENTORY_INTEGRITY   UNITS_MISSING_A_CSV_FIELD                                         []
PASS  INVENTORY_INTEGRITY   ALL_SEVEN_TOPIK_REPRESENTED                                       [1, 2, 3, 4, 5, 6, 7]
PASS  INVENTORY_INTEGRITY   BAHAGIAN_NUMBER_WITHOUT_TITLE                                     []
PASS  INVENTORY_INTEGRITY   BAHAGIAN_NUMBERS_INVENTED                                         []
PASS  STOP_CONDITION        BLOCKING_STOP_CONDITIONS_EVALUATED                                True
PASS  INVENTORY_INTEGRITY   READY_UNIT_WITH_UNRESOLVED_BLOCKING_SOURCE                        []
PASS  INVENTORY_INTEGRITY   UNSUPPORTED_INTERACTION_CLASSIFIED_READY                          []
PASS  INVENTORY_INTEGRITY   UNIT_WITHOUT_RUMUSAN_MARKED_FULLY_COMPLETE                        []
PASS  INVENTORY_INTEGRITY   UNIT_WITHOUT_QUIZ_SOURCE_MARKED_FULLY_COMPLETE                    []
PASS  INVENTORY_INTEGRITY   LANE_D_UNIT_NOT_MARKED_SOURCE_BLOCKED                             []
PASS  INVENTORY_INTEGRITY   UNIT_CLAIMING_CONTENT_WITHOUT_SOURCE_DOCUMENT                     []
PASS  AUTHORITY_DISCIPLINE  EVIDENCE_REGISTER_EVALUATED                                       True
PASS  AUTHORITY_DISCIPLINE  UNKNOWN_AUTHORITY_CLASSES                                         []
PASS  AUTHORITY_DISCIPLINE  UNIT_AUTHORITY_CLASSES_KNOWN                                      []
PASS  AUTHORITY_DISCIPLINE  AUTHORITY_CLASS_INFLATION                                         []
PASS  AUTHORITY_DISCIPLINE  CALL_APPROVAL_AUTHORITY_CLASS                                     'FIRDAUS_ATTESTED_BARIAH_CALL'
PASS  AUTHORITY_DISCIPLINE  CALL_APPROVAL_NOT_CLASSIFIED_AS_DIRECT                            []
PASS  AUTHORITY_DISCIPLINE  CALL_APPROVAL_WRITTEN_CONFIRMATION_PENDING                        'PENDING'
PASS  AUTHORITY_DISCIPLINE  CALL_APPROVAL_DOES_NOT_AUTHORISE_FREEZE                           True
PASS  AUTHORITY_DISCIPLINE  SOURCE_DERIVED_SUBJECT_LABELLED_BARIAH_DIRECT                     []
PASS  AUTHORITY_DISCIPLINE  EXISTENCE_ONLY_EVIDENCE_CLAIMING_CONTENT                          []
PASS  RULE_PORTABILITY      RULES_EVALUATED                                                   True
PASS  RULE_PORTABILITY      DUPLICATE_RULE_IDS                                                []
PASS  RULE_PORTABILITY      INVALID_PORTABILITY_CLASSES                                       []
PASS  RULE_PORTABILITY      RULES_WITHOUT_EVIDENCE                                            []
PASS  RULE_PORTABILITY      MANDATORY_B02_SPECIFIC_RULES_PRESENT                              []
PASS  RULE_PORTABILITY      B02_SPECIFIC_RULE_PROMOTED_GLOBALLY                               []
PASS  RULE_PORTABILITY      GLOBAL_RULE_WITH_NARROW_DESTINATION                               []
PASS  RULE_PORTABILITY      B02_SPECIFIC_RULE_WITH_WIDE_DESTINATION                           []
PASS  RULE_PORTABILITY      UNORACLED_RULE_WITHOUT_HUMAN_AUTHORITY                            []
PASS  SELECTION_INTEGRITY   SELECTED_PROOF_UNIT_PRESENT_IN_INVENTORY                          True
PASS  SELECTION_INTEGRITY   SELECTED_PROOF_UNIT_IS_NOT_B02                                    True
PASS  SELECTION_INTEGRITY   SELECTED_PROOF_UNIT_BLOCKING_CONDITIONS                           True
PASS  SELECTION_INTEGRITY   BLOCKED_SELECTION_DECLARED_UNCONDITIONAL                          False
PASS  SELECTION_INTEGRITY   BLOCKED_SELECTION_WITHOUT_PRECONDITIONS                           False
PASS  SELECTION_INTEGRITY   SELECTION_STATUS_DECLARED                                         True
PASS  SELECTION_INTEGRITY   SELECTION_STATUS_VALUE                                            'SELECTED_CONDITIONAL_PENDING_CONTENT_EXTRACTION'
PASS  SELECTION_INTEGRITY   REJECTED_CANDIDATES_RECORDED                                      True
PASS  SELECTION_INTEGRITY   REJECTED_CANDIDATES_NOT_IN_INVENTORY                              []
PASS  SELECTION_INTEGRITY   SCORED_CANDIDATES_NOT_IN_INVENTORY                                []
PASS  SELECTION_INTEGRITY   CANDIDATE_SCORES_OUT_OF_RANGE                                     []
PASS  SELECTION_INTEGRITY   CANDIDATE_SCORES_MISSING_A_CRITERION                              []
PASS  SELECTION_INTEGRITY   SOURCELESS_CANDIDATE_SCORED_ON_CONTENT                            []
PASS  PLAN_INTEGRITY        PLAN_ROWS_EVALUATED                                               True
PASS  PLAN_INTEGRITY        EXECUTION_ORDER_UNIT_ABSENT_FROM_INVENTORY                        []
PASS  PLAN_INTEGRITY        WAVE_UNIT_ABSENT_FROM_INVENTORY                                   []
PASS  PLAN_INTEGRITY        PLAN_ROWS_COVER_EVERY_REMAINING_UNIT                              ['K5-PL06-T01-B01', 'K5-PL06-T01-B02', 'K5-PL06-T01-B03', 'K5-PL06-T02-B01', 'K5-PL06-T02-B02', 'K5-PL06-T03-B01', 'K5-PL06-T03-B03', 'K5-PL06-T03-B04', 'K5-PL06-T03-B05', 'K5-PL06-T04-B01', 'K5-PL06-T05-B01', 'K5-PL06-T06-B01', 'K5-PL06-T07-B01']
PASS  PLAN_INTEGRITY        WAVE_0_UNIT_IS_THE_SELECTION                                      ['K5-PL06-T04-B01']
PASS  PLAN_INTEGRITY        DUPLICATE_EXECUTION_ORDER                                         []
PASS  PLAN_INTEGRITY        MEASURED_BASIS_RECORDED                                           True
PASS  PLAN_INTEGRITY        PLAN_DURATION_WITHOUT_BASIS                                       []
PASS  PLAN_INTEGRITY        POWERPOINT_SMOKE_ESTIMATED_WITHOUT_EVIDENCE                       []
PASS  STOP_CONDITION        INVALID_STOP_SCOPES                                               []
PASS  STOP_CONDITION        DUPLICATE_STOP_IDS                                                []
PASS  STOP_CONDITION        STOP_APPLIES_TO_UNKNOWN_UNIT                                      []
PASS  STOP_CONDITION        STOP_CONDITION_WITHOUT_RESOLVER                                   []
PASS  STOP_CONDITION        GLOBAL_ITEM_BLOCKING_UNRELATED_UNIT                               []
PASS  STOP_CONDITION        UNIT_BLOCKER_NOT_IN_STOP_REGISTER                                 []
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.md   True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.csv  True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::PL06_RULE_PORTABILITY_MATRIX_v1.md           True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::PL06_CAPABILITY_COVERAGE_MATRIX_v1.md        True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::PL06_FIRST_SCALE_OUT_SELECTION_v1.md         True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::PL06_EXECUTION_PLAN_v1.md                    True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::PL06_OPEN_AUTHORITY_ITEMS_v1.md              True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::B02_BARIAH_CALL_APPROVAL_RECORD_v1.md        True
PASS  ARTIFACT_AGREEMENT    CSV_ROW_COUNT_EQUALS_INVENTORY                                    14
PASS  ARTIFACT_AGREEMENT    MARKDOWN_CSV_INVENTORY_DIVERGENCE                                 []
PASS  ARTIFACT_AGREEMENT    UNIT_ABSENT_FROM_MARKDOWN_INVENTORY                               []
PASS  ARTIFACT_AGREEMENT    EMITTED_DELIVERABLES_STALE                                        []
PASS  ARTIFACT_AGREEMENT    VERDICT_IS_ALLOWED                                                True
PASS  ARTIFACT_AGREEMENT    FORBIDDEN_VERDICT_CLAIMED                                         []
PASS  ARTIFACT_AGREEMENT    INGEST_COMPLETE_VERDICT_WITH_UNRESOLVED_SOURCE_AUTHORITY          False
PASS  ARTIFACT_AGREEMENT    COMPLETE_VERDICT_WITH_UNRESOLVED_UNITS                            False
PASS  ARTIFACT_AGREEMENT    SOURCE_FREEZE_DIRECTORY_PRESENT                                   True
PASS  SOURCE_CUSTODY        FREEZE_MANIFEST_ARTIFACTS                                         29
PASS  SOURCE_CUSTODY        FREEZE_HASH_REGISTER_LINES                                        30
PASS  SOURCE_CUSTODY        INGESTED_FILES_EVALUATED                                          13
PASS  SOURCE_CUSTODY        INGESTED_FILES_MISSING                                            []
PASS  SOURCE_CUSTODY        INGESTED_FILES_MATCH_FREEZE_HASHES                                []
PASS  SOURCE_CUSTODY        T04_BOUNDARY_EVIDENCE_IMAGES_PRESENT                              ['boundary_pages/p294.png', 'boundary_pages/p302.png']
PASS  SOURCE_CUSTODY        GIT_INDEX_READ                                                    True
PASS  SOURCE_CUSTODY        FORBIDDEN_TRACKED_PATTERNS_COMPLETE                               ['FULL_DOCX', 'RENDERED_PDF', 'TRANSPORT_ZIP']
PASS  SOURCE_CUSTODY        FORBIDDEN_TRACKED_FULL_DOCX                                       []
PASS  SOURCE_CUSTODY        FORBIDDEN_TRACKED_RENDERED_PDF                                    []
PASS  SOURCE_CUSTODY        FORBIDDEN_TRACKED_TRANSPORT_ZIP                                   []
PASS  SOURCE_CUSTODY        GIT_LFS_NOT_CONFIGURED                                            False
PASS  SOURCE_CUSTODY        NO_INCOMING_RESIDUE_TRACKED                                       []
PASS  BOUNDARY_INTEGRITY    BOUNDARY_MAP_LESSONS                                              14
PASS  BOUNDARY_INTEGRITY    BOUNDARY_MAP_UNIQUE_UNIT_IDS                                      14
PASS  BOUNDARY_INTEGRITY    INVENTORY_UNIT_COUNT                                              14
PASS  BOUNDARY_INTEGRITY    INVENTORY_UNIQUE_UNIT_IDS                                         14
PASS  BOUNDARY_INTEGRITY    PL06_TOPOLOGY                                                     [3, 2, 5, 1, 1, 1, 1]
PASS  BOUNDARY_INTEGRITY    COMPLETED_UNITS                                                   ['K5-PL06-T03-B02']
PASS  BOUNDARY_INTEGRITY    REMAINING_UNITS                                                   13
PASS  BOUNDARY_INTEGRITY    B02_BAHAGIAN_TITLE                                                'Struktur Taman dan Perabot Taman'
PASS  BOUNDARY_INTEGRITY    B02_BAHAGIAN_TITLE_IS_NOT_TOPIK_TITLE                             False
PASS  BOUNDARY_INTEGRITY    UNITS_WHOSE_BAHAGIAN_TITLE_EQUALS_TOPIK_TITLE                     []
PASS  BOUNDARY_INTEGRITY    UNRESOLVED_PLACEHOLDER_UNITS                                      []
PASS  BOUNDARY_INTEGRITY    T03_B03_PRESENT                                                   True
PASS  BOUNDARY_INTEGRITY    T03_B03_TITLE                                                     'Infrastruktur'
PASS  BOUNDARY_INTEGRITY    T03_B03_PAGE_RANGE                                                True
PASS  BOUNDARY_INTEGRITY    UNITS_WITH_NULL_BAHAGIAN_NUMBER                                   []
PASS  BOUNDARY_INTEGRITY    T04_MODULE_PAGE_RANGE                                             '276-283'
PASS  BOUNDARY_INTEGRITY    T04_PDF_PAGE_RANGE                                                '294-301'
PASS  BOUNDARY_INTEGRITY    T04_START_ANCHOR_IS_BODY_STRING                                   True
PASS  BOUNDARY_INTEGRITY    T04_END_BEFORE_ANCHOR                                             '5.0 PENGURUSAN KUALITI PROJEK'
PASS  BOUNDARY_INTEGRITY    T04_BOUNDARY_IS_CLEAN                                             (False, False)
PASS  BOUNDARY_INTEGRITY    SHARED_BOUNDARY_PAGES                                             [181, 188, 215, 237, 250, 255]
PASS  BOUNDARY_INTEGRITY    BOUNDARY_MAP_JSON_CSV_DIVERGENCE                                  []
PASS  BOUNDARY_INTEGRITY    BOUNDARY_MAP_UNITS_ABSENT_FROM_MARKDOWN                           []
PASS  AUTHORITY_DISCIPLINE  GROUPING_AUTHORITY_STATUS_EXPLICIT                                'REFERENCED_NOT_FROZEN'
PASS  AUTHORITY_DISCIPLINE  GROUPING_AUTHORITY_NOT_CLAIMED_CANONICAL                          False
PASS  AUTHORITY_DISCIPLINE  GROUPING_AUTHORITY_DOES_NOT_BLOCK_EXTRACTION                      False
PASS  AUTHORITY_DISCIPLINE  GROUPING_AUTHORITY_ARTIFACT_ABSENT                                []
PASS  AUTHORITY_DISCIPLINE  PRIMARY_DOCX_CUSTODY_EXPLICIT                                     'EXTERNAL_DURABLE_SOURCE_BY_IDENTITY'
PASS  AUTHORITY_DISCIPLINE  PRIMARY_DOCX_NOT_TRACKED                                          False
PASS  AUTHORITY_DISCIPLINE  PRIMARY_DOCX_IDENTITY_RECORDED                                    (16832861, '5a9142cd')
PASS  AUTHORITY_DISCIPLINE  FREEZE_PACKAGE_CUSTODY_EXPLICIT                                   'DURABLE_CUSTODY_PENDING'
PASS  AUTHORITY_DISCIPLINE  SHARED_TEAM_CUSTODY_NOT_CLAIMED                                   False
PASS  AUTHORITY_DISCIPLINE  RENDERED_PDF_CLASSIFICATION                                       'DERIVED_ARTIFACT_PRESERVED_INSIDE_FREEZE_PACKAGE'
PASS  AUTHORITY_DISCIPLINE  RENDERED_PDF_NOT_TRACKED_SEPARATELY                               False
PASS  AUTHORITY_DISCIPLINE  GIT_LFS_STATUS_EXPLICIT                                           'NOT_CONFIGURED'
PASS  STOP_CONDITION        RESOLVED_STOP_CONDITIONS                                          ['STOP-001', 'STOP-002']
PASS  STOP_CONDITION        RESOLVED_STOP_WITH_UNITS_STILL_ATTACHED                           []
PASS  STOP_CONDITION        INVALID_STOP_STATUSES                                             []
PASS  ACCOUNTING            DUPLICATE_GATE_IDS                                                []
PASS  ACCOUNTING            EVERY_GATE_CARRIES_A_TYPE                                         []

136/136 active gates PASS  ·  0 supersession markers  ·  136 emitted records
```
