# STAGE_4_2F_B0_QA_REPORT

Stage 4.2F-B0 — T04-B01 controlled source extraction.

Suite: `docs/pl06/t04/tools/t04_qa_v1.py` · Mutations: `docs/pl06/t04/tools/t04_mutations_v1.py`

# 1. Test accounting

| Metric | Value |
|---|---:|
| `ACTIVE_TEST_GATES_PASSING` | **109 / 109** |
| `SUPERSESSION_MARKERS_PRESENT` | **0** |
| `TOTAL_EMITTED_GATE_RECORDS` | **109** |

Every record carries an explicit `gate_type`.

| `gate_type` | Gates |
|---|---:|
| `AUTHORITY_DISCIPLINE` | 22 |
| `BOUNDARY_INTEGRITY` | 20 |
| `EXTRACT_COMPLETENESS` | 19 |
| `ARTIFACT_AGREEMENT` | 15 |
| `INVENTION_GUARD` | 14 |
| `PROPAGATION_GUARD` | 9 |
| `CUSTODY` | 8 |
| `ACCOUNTING` | 2 |

# 2. Mutation sensitivity

| | |
|---|---:|
| Fixtures | **34** |
| `DATA_MUTATION` | 30 |
| `EXTRACTION_MUTATION` | 4 |
| Detected | **34** |
| Missed | **0** |
| Skipped | **0** |
| Baseline false failures | **0** |

The four `EXTRACTION_MUTATION` fixtures call the extractor with a corrupted anchor or index and require it to **fail closed**. All four raised `ExtractionError` rather than silently extracting a wrong span:

```
E-01  anchor on the canonical spelling  -> raw start anchor not found: 'PENJAGAAN DAN PENYELENGGARAAN'
E-02  expected start changed to 5219    -> anchors resolve to 5220/5360, map says 5219/5360
E-03  expected stop changed to 5370     -> anchors resolve to 5220/5360, map says 5220/5370
E-04  stop anchor changed to DEMOBILISASI -> anchors resolve to 5220/5705, map says 5220/5360
```

**E-01 is the one that matters.** It proves the misspelled body heading is load-bearing: an extraction driven from the correctly spelled label finds nothing at all.

These four need the DOCX, which is deleted at the end of the stage. They ran here and are reported as `SKIPPED_NO_DOCX` afterwards — a skipped fixture is not a passing one, and the harness says so rather than dropping them.

## 2.1 Two gates the fixtures caught before they shipped

Both were mine, and both were over-broad rather than wrong-in-spirit:

- **`INVENTED_QUIZ_TEXT`** listed bare `a)`, `b)`, `c)`, `d)` as quiz-option markers. Those match ordinary Malay prose — *jenis baja (organik atau kimia)* and *(serangga), penyakit (kulat)* both contain `a)`. Option markers are now anchored to the start of a row.
- **`EXTRACT_FREE_OF_B02_CONTENT`** scanned the extracted source text for B02 component names and fired on *papan tanda amaran* — a warning sign at a spray site, ordinary Malay. That was a category error: rows are lifted verbatim from the module, so they cannot be propagation. Propagation enters through the **analysis** layer, and that is what is now scanned.

# 3. What this suite checks

DOCX identity as recorded; the raw anchor found and the canonical spelling proven unusable; start 5220 and stop 5360 under a disclosed enumeration; 140 elements fully accounted for; T03 and T05 content excluded; every list, table, visual and page attributed; no duplicate row or asset IDs; exactly one authorised normalisation; every row `MODULE_SOURCE_ATTESTED`; no invented Rumusan, quiz, answer key or visual subject; no B02 propagation; and Markdown/JSON/CSV totals in agreement.

# 4. What it cannot check

**That the extraction is instructionally right.** 109 green gates say the 140-element span was read faithfully and nothing was invented. They say nothing about whether Siram, Baja and Racun should be three screens or one.

**That the page attribution is typeset truth.** It comes from Word's cached `lastRenderedPageBreak` markers, which are advisory. Eight distinct pages falling exactly on 276–283 is corroboration of the frozen map, not independent authority — and the extract records it as `ADVISORY_CACHED_LAYOUT` for that reason.

# 5. Verdict

```
T04_SOURCE_COMPLETE_PENDING_TARGETED_INSTRUCTIONAL_DECISIONS
```

**No PPTX was generated in this stage.**

# 6. Full gate output

```
PASS  CUSTODY               DOCX_IDENTITY_RECORDED                                   True
PASS  CUSTODY               DOCX_BYTES                                               16832861
PASS  CUSTODY               DOCX_SHA256                                              '5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7'
PASS  CUSTODY               DOCX_FILENAME                                            '[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx'
PASS  CUSTODY               GIT_INDEX_READ                                           True
PASS  CUSTODY               SOURCE_DOCX_TRACKED                                      []
PASS  CUSTODY               PPTX_ADDED_THIS_STAGE                                    []
PASS  CUSTODY               DOCX_STAGING_NOT_IN_REPO                                 False
PASS  BOUNDARY_INTEGRITY    RAW_START_ANCHOR_FOUND                                   1
PASS  BOUNDARY_INTEGRITY    RAW_START_ANCHOR_STRING                                  'PENJAAGAAN DAN PENYELENGGARAAN'
PASS  BOUNDARY_INTEGRITY    CANONICAL_ONLY_ANCHOR_NOT_USED                           []
PASS  BOUNDARY_INTEGRITY    RAW_STOP_ANCHOR_FOUND                                    1
PASS  BOUNDARY_INTEGRITY    RAW_STOP_ANCHOR_STRING                                   'PENGURUSAN KUALITI PROJEK'
PASS  BOUNDARY_INTEGRITY    START_PARAGRAPH_IS_5220                                  5220
PASS  BOUNDARY_INTEGRITY    STOP_BEFORE_PARAGRAPH_5360                               5360
PASS  BOUNDARY_INTEGRITY    START_MATCHES_FROZEN_MAP                                 True
PASS  BOUNDARY_INTEGRITY    STOP_MATCHES_FROZEN_MAP                                  True
PASS  BOUNDARY_INTEGRITY    PARAGRAPH_SPAN                                           140
PASS  BOUNDARY_INTEGRITY    ENUMERATION_DISCLOSED                                    True
PASS  BOUNDARY_INTEGRITY    ALTERNATE_ENUMERATION_RECORDED                           1314
PASS  BOUNDARY_INTEGRITY    MODULE_PAGES                                             [276, 283]
PASS  BOUNDARY_INTEGRITY    PAGE_ATTRIBUTION_MATCHES_FROZEN_MAP                      True
PASS  BOUNDARY_INTEGRITY    DISTINCT_MODULE_PAGES                                    [276, 277, 278, 279, 280, 281, 282, 283]
PASS  BOUNDARY_INTEGRITY    PAGE_ATTRIBUTION_AUTHORITY_DISCLOSED                     'ADVISORY_CACHED_LAYOUT'
PASS  BOUNDARY_INTEGRITY    T05_CONTENT_EXCLUDED                                     []
PASS  BOUNDARY_INTEGRITY    T03_CONTENT_EXCLUDED                                     []
PASS  BOUNDARY_INTEGRITY    FIRST_ROW_IS_THE_START_ANCHOR                            'PENJAAGAAN DAN PENYELENGGARAAN'
PASS  BOUNDARY_INTEGRITY    STOP_ANCHOR_NOT_IN_ROWS                                  []
PASS  AUTHORITY_DISCIPLINE  NORMALISATION_STATUS                                     'RECORDED_NOT_SILENTLY_CORRECTED'
PASS  AUTHORITY_DISCIPLINE  RAW_AND_GOVERNED_HELD_SEPARATELY                         True
PASS  AUTHORITY_DISCIPLINE  H1_RAW_TEXT_PRESERVED                                    'PENJAAGAAN DAN PENYELENGGARAAN'
PASS  AUTHORITY_DISCIPLINE  H1_DISPLAY_TEXT_GOVERNED                                 'PENJAGAAN DAN PENYELENGGARAAN'
PASS  AUTHORITY_DISCIPLINE  H1_NORMALISATION_RECORDED                                'RECORDED_NOT_SILENTLY_CORRECTED'
PASS  AUTHORITY_DISCIPLINE  NORMALISED_ROWS                                          ['T04-ROW-001']
PASS  AUTHORITY_DISCIPLINE  UNSUPPORTED_NORMALISATION                                []
PASS  EXTRACT_COMPLETENESS  BODY_ELEMENTS_IN_SPAN                                    140
PASS  EXTRACT_COMPLETENESS  EVERY_ELEMENT_ACCOUNTED                                  140
PASS  EXTRACT_COMPLETENESS  CONTENT_ROWS                                             100
PASS  EXTRACT_COMPLETENESS  CONTENT_TYPE_TOTALS_SUM                                  100
PASS  EXTRACT_COMPLETENESS  HEADINGS                                                 49
PASS  EXTRACT_COMPLETENESS  NUMBERED_PARAGRAPHS                                      61
PASS  EXTRACT_COMPLETENESS  LIST_INVENTORY_MATCHES_TOTAL                             61
PASS  EXTRACT_COMPLETENESS  EVERY_LIST_ITEM_BINDS_TO_A_ROW                           []
PASS  EXTRACT_COMPLETENESS  TABLES                                                   0
PASS  EXTRACT_COMPLETENESS  TABLE_INVENTORY_MATCHES_TOTAL                            0
PASS  EXTRACT_COMPLETENESS  DIAGRAMS                                                 1
PASS  EXTRACT_COMPLETENESS  RASTER_IMAGES                                            0
PASS  EXTRACT_COMPLETENESS  ASSET_INVENTORY_MATCHES_TOTAL                            1
PASS  EXTRACT_COMPLETENESS  EVERY_VISUAL_ROW_BINDS_TO_AN_ASSET                       []
PASS  EXTRACT_COMPLETENESS  SEQUENCE_IS_CONTIGUOUS                                   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
PASS  EXTRACT_COMPLETENESS  DUPLICATE_ROW_IDS                                        []
PASS  EXTRACT_COMPLETENESS  DUPLICATE_ASSET_IDS                                      []
PASS  EXTRACT_COMPLETENESS  ROWS_WITHOUT_A_PAGE                                      []
PASS  EXTRACT_COMPLETENESS  ROWS_OUTSIDE_THE_PAGE_RANGE                              []
PASS  AUTHORITY_DISCIPLINE  ALL_ROWS_MODULE_SOURCE_ATTESTED                          ['MODULE_SOURCE_ATTESTED']
PASS  AUTHORITY_DISCIPLINE  SOURCE_DERIVED_PROMOTED_TO_BARIAH_DIRECT                 []
PASS  AUTHORITY_DISCIPLINE  ASSET_SUBJECTS_NOT_BARIAH_DIRECT                         []
PASS  AUTHORITY_DISCIPLINE  ASSET_SOURCE_BOUND_STATUS_VALID                          ['SOURCE_BOUND_CAPTIONLESS']
PASS  INVENTION_GUARD       INVENTED_RUMUSAN                                         []
PASS  INVENTION_GUARD       INVENTED_QUIZ_TEXT                                       []
PASS  INVENTION_GUARD       INVENTED_QUIZ_OPTION_MARKERS                             []
PASS  INVENTION_GUARD       RUMUSAN_STATUS                                           'NOT_FOUND'
PASS  INVENTION_GUARD       QUIZ_STATUS                                              'NOT_FOUND'
PASS  INVENTION_GUARD       ANSWER_KEY_STATUS                                        'NOT_FOUND'
PASS  INVENTION_GUARD       QUIZ_COMPOSITION_NOT_ASSUMED                             'AUTHORITY_UNRESOLVED'
PASS  INVENTION_GUARD       PASS_THRESHOLD_NOT_ASSUMED                               'AUTHORITY_UNRESOLVED'
PASS  INVENTION_GUARD       INVALID_COVERAGE_STATUSES                                []
PASS  INVENTION_GUARD       INVENTED_VISUAL_SUBJECTS                                 []
PASS  INVENTION_GUARD       DIAGRAM_NODE_COUNT                                       6
PASS  INVENTION_GUARD       CANDIDATE_ROWS_NOT_IN_EXTRACT                            []
PASS  INVENTION_GUARD       CANDIDATE_WITH_NO_ROWS_IS_PENDING_HUMAN                  []
PASS  INVENTION_GUARD       INVALID_CANDIDATE_TYPES                                  []
PASS  PROPAGATION_GUARD     B02_PROPAGATION_FAMILY_S                                 []
PASS  PROPAGATION_GUARD     B02_PROPAGATION_FAMILY_P1                                []
PASS  PROPAGATION_GUARD     B02_PROPAGATION_FAMILY_P2                                []
PASS  PROPAGATION_GUARD     B02_PROPAGATION_PAPAN_TANDA                              []
PASS  PROPAGATION_GUARD     B02_PROPAGATION_BBQ_PIT                                  []
PASS  PROPAGATION_GUARD     B02_PROPAGATION_ALYA                                     []
PASS  PROPAGATION_GUARD     B02_PROPAGATION_ENCIK_RAHMAN                             []
PASS  PROPAGATION_GUARD     B02_CARDINALITIES_IN_CANDIDATES                          []
PASS  PROPAGATION_GUARD     B02_COMPONENTS_IN_ANALYSIS                               []
PASS  AUTHORITY_DISCIPLINE  INVALID_CLAIM_STATUSES                                   []
PASS  AUTHORITY_DISCIPLINE  CLAIM_ROWS_NOT_IN_EXTRACT                                []
PASS  AUTHORITY_DISCIPLINE  CLAIMS_BLOCKING_THIS_UNIT                                []
PASS  AUTHORITY_DISCIPLINE  MS2680_PRESENT_IN_T04                                    False
PASS  AUTHORITY_DISCIPLINE  LEGISLATION_CLAIM_FLAGGED                                ['T04-CLM-01']
PASS  AUTHORITY_DISCIPLINE  INSTRUCTIONAL_STATUS                                     'CONTENT_ASSESSMENT_PENDING'
PASS  AUTHORITY_DISCIPLINE  READINESS_TYPE_VALID                                     True
PASS  AUTHORITY_DISCIPLINE  SOURCE_INCOMPLETE_RETIRED                                True
PASS  AUTHORITY_DISCIPLINE  FORBIDDEN_VERDICT_CLAIMED                                []
PASS  AUTHORITY_DISCIPLINE  VERDICT_IS_ALLOWED                                       True
PASS  AUTHORITY_DISCIPLINE  READY_VERDICT_WITH_BLOCKING_GAPS                         False
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_CONTROLLED_CONTENT_v1.md        True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_VISUAL_INVENTORY_v1.csv         True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_TABLE_INVENTORY_v1.csv          True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_LIST_INVENTORY_v1.csv           True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_RUMUSAN_AND_QUIZ_MAP_v1.md      True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_EXTERNAL_CLAIMS_REGISTER_v1.md  True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_SCREEN_CANDIDATE_MAP_v1.md      True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_SOURCE_GAPS_v1.md               True
PASS  ARTIFACT_AGREEMENT    DELIVERABLE_PRESENT::T04_SOURCE_EXTRACT_v1.json          True
PASS  ARTIFACT_AGREEMENT    EMITTED_DELIVERABLES_STALE                               []
PASS  ARTIFACT_AGREEMENT    VISUAL_CSV_MATCHES_JSON                                  1
PASS  ARTIFACT_AGREEMENT    TABLE_CSV_MATCHES_JSON                                   0
PASS  ARTIFACT_AGREEMENT    LIST_CSV_MATCHES_JSON                                    61
PASS  ARTIFACT_AGREEMENT    EVERY_ROW_IN_MARKDOWN                                    []
PASS  ARTIFACT_AGREEMENT    MARKDOWN_ROW_COUNT_STATED                                True
PASS  ACCOUNTING            DUPLICATE_GATE_IDS                                       []
PASS  ACCOUNTING            EVERY_GATE_CARRIES_A_TYPE                                []

109/109 active gates PASS  ·  0 supersession markers  ·  109 emitted records
```
