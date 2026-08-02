# PL06_STORYBOARD_PRODUCTION_INVENTORY — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py` — do not hand-edit this file; edit the controlled data source and re-emit.

```
UNITS = 8
TOPIK_ENUMERATED = 7 of 7
BAHAGIAN_ENUMERATED = 1 of unknown
VERDICT = PL06_SCALE_OUT_BLOCKED_BY_UNRESOLVED_UNIT_BOUNDARIES
```

> **Read the Bahagian column before anything else.** Exactly one Bahagian in the whole of PL06 is named by a source: `B02`, the one already delivered. One more is attested to exist without a number or a title. The other six Topik have no Bahagian enumeration of any kind, and none has been invented here.

# 1. What the evidence actually establishes

| Level | Established | Evidence |
|---|---|---|
| Course | K5 — Kursus Kerja Bangunan – Pembinaan Landskap Luar | M1 |
| Pakej Latihan | eight, PL01–PL08, named | M1 slide 2 |
| PL06 Topik | **seven, named** | M2 slide 3 |
| PL06 Bahagian | **not enumerated for any Topik** | — no artifact carries it |
| T03 B02 content | 26 source rows, 14 assets, modul ms 238–249 | P1 |
| Any other unit's content | **nothing** | C1 F2 `MEASURED_FACT` |

The seven Topik titles, verbatim from M2 slide 3:

1. **Topik 1: Proses Memula Kerja**
2. **Topik 2: Elemen Pembinaan Landskap**
3. **Topik 3: Komponen Landskap**
4. **Topik 4: Penjagaan Dan Penyelenggaraan**
5. **Topik 5: Pengurusan Kualiti Projek**
6. **Topik 6: Perlindungan Dan Penambahbaikan Alam Sekitar**
7. **Topik 7: Demobilisasi**

# 2. Unit inventory

| order | unit_id | Topik | Bahagian | scope | source | readiness | lane |
|---|---|---|---|---|---|---|---|
| 0 | `K5-PL06-T03-B02` | T03 Komponen Landskap | 2 | DELIVERED_BASELINE | K5_PL06_T03_B02_pages_256269.pdf | `READY_WITH_HOLDS` | A |
| 1 | `K5-PL06-T04` | T04 Penjagaan Dan Penyelenggaraan | **unresolved** | REMAINING | NONE_IN_CUSTODY | `SOURCE_AUTHORITY_UNRESOLVED` | D |
| 2 | `K5-PL06-T02` | T02 Elemen Pembinaan Landskap | **unresolved** | REMAINING | NONE_IN_CUSTODY | `SOURCE_AUTHORITY_UNRESOLVED` | D |
| 3 | `K5-PL06-T03-BNEXT` | T03 Komponen Landskap | **unresolved** | REMAINING | NONE_IN_CUSTODY | `SOURCE_AUTHORITY_UNRESOLVED` | D |
| 4 | `K5-PL06-T01` | T01 Proses Memula Kerja | **unresolved** | REMAINING | NONE_IN_CUSTODY | `SOURCE_AUTHORITY_UNRESOLVED` | D |
| 5 | `K5-PL06-T05` | T05 Pengurusan Kualiti Projek | **unresolved** | REMAINING | NONE_IN_CUSTODY | `SOURCE_AUTHORITY_UNRESOLVED` | D |
| 6 | `K5-PL06-T06` | T06 Perlindungan Dan Penambahbaikan Alam Sekitar | **unresolved** | REMAINING | NONE_IN_CUSTODY | `SOURCE_AUTHORITY_UNRESOLVED` | D |
| 7 | `K5-PL06-T07` | T07 Demobilisasi | **unresolved** | REMAINING | NONE_IN_CUSTODY | `SOURCE_AUTHORITY_UNRESOLVED` | D |

# 3. Per-unit detail

## `K5-PL06-T03-B02` — Komponen Landskap, Bahagian 2

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 3 |
| topik_title | Komponen Landskap |
| bahagian_number | 2 |
| bahagian_title | Komponen Landskap |
| unit_scope | DELIVERED_BASELINE |
| source_document | K5_PL06_T03_B02_pages_256269.pdf |
| source_page_range | modul ms 238-249 / physical 256-269 |
| source_reference | P1 — sha256 30a6903d…, identity recorded in B02_ASSET_MANIFEST.md; 26 source rows bound in STORYBOARD_SOURCE_MAP_v0.4.md |
| source_authority_class | SOURCE_ATTESTED_EXTRACT |
| source_attests | FULL_UNIT_CONTENT |
| controlled_content_available | true |
| existing_id_input_available | true |
| storyboard_input_available | true |
| source_rows_count | 26 |
| source_figures_count | 4 |
| source_tables_count | 10 |
| source_assets_count | 14 |
| rumusan_available | true |
| quiz_mcq_available | true |
| quiz_mr_available | true |
| interaction_requirement | REQUIRED |
| interaction_pattern_candidate | FAMILY_S / FAMILY_P1 / FAMILY_P2 (B02-specific taxonomy) |
| visual_requirement | REQUIRED — source-bound overview, 9/9 mapped |
| narration_requirement | A3 shell grammar, three spoken S01 blocks, screen-level VO only |
| terminology_risks | PL06 pronunciation precedence RESERVED_NOT_ACTIVE; 'BBQ pit' lowercase source form measured |
| standards_or_external_claims | MS2680 cited in source, verification open |
| open_human_decisions | MS2680; B02-CAIR-INT-001; OD-10 / L-01 LMS navigation |
| generator_support_status | FULLY_SUPPORTED |
| qa_support_status | FULLY_SUPPORTED — 441 active gates, 51 mutation fixtures |
| lane | LANE_A_EXISTING_SUPPORTED_PATTERN |
| readiness_status | READY_WITH_HOLDS |
| blocker_reason | Delivered and call-approved. Holds are source-authority only and none of them blocks this unit's review candidacy: MS2680, B02-CAIR-INT-001, and the LMS navigation ruling. Microsoft PowerPoint smoke is not recorded. |
| blocking_conditions | MS2680_VERIFICATION; B02_CAIR_INT_001; LMS_NAVIGATION_RULING; POWERPOINT_SMOKE_NOT_RECORDED |
| recommended_execution_order | 0 |

## `K5-PL06-T04` — Penjagaan Dan Penyelenggaraan

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 4 |
| topik_title | Penjagaan Dan Penyelenggaraan |
| bahagian_number |  |
| bahagian_title |  |
| unit_scope | REMAINING |
| source_document | NONE_IN_CUSTODY |
| source_page_range | UNKNOWN |
| source_reference | M2 — SB_K5PL6_montaj_v1.pptx slide 3, verbatim 'Topik 4: Penjagaan Dan Penyelenggaraan' |
| source_authority_class | BARIAH_SUPPLIED_UPSTREAM_ARTIFACT |
| source_attests | TOPIK_EXISTENCE_AND_TITLE_ONLY |
| controlled_content_available | false |
| existing_id_input_available | false |
| storyboard_input_available | false |
| source_rows_count |  |
| source_figures_count |  |
| source_tables_count |  |
| source_assets_count |  |
| rumusan_available | false |
| quiz_mcq_available | false |
| quiz_mr_available | false |
| interaction_requirement | UNKNOWN |
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_SOURCE |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — no source read |
| open_human_decisions | BAHAGIAN_BOUNDARY; CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_AUTHORITY_UNRESOLVED |
| blocker_reason | No approved source document for this Topik is in custody. Its existence and title are attested by the PL06 montage; nothing else about it is. |
| blocking_conditions | NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY; BAHAGIAN_BOUNDARY_UNRESOLVED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 1 |

## `K5-PL06-T02` — Elemen Pembinaan Landskap

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 2 |
| topik_title | Elemen Pembinaan Landskap |
| bahagian_number |  |
| bahagian_title |  |
| unit_scope | REMAINING |
| source_document | NONE_IN_CUSTODY |
| source_page_range | UNKNOWN |
| source_reference | M2 — SB_K5PL6_montaj_v1.pptx slide 3, verbatim 'Topik 2: Elemen Pembinaan Landskap' |
| source_authority_class | BARIAH_SUPPLIED_UPSTREAM_ARTIFACT |
| source_attests | TOPIK_EXISTENCE_AND_TITLE_ONLY |
| controlled_content_available | false |
| existing_id_input_available | false |
| storyboard_input_available | false |
| source_rows_count |  |
| source_figures_count |  |
| source_tables_count |  |
| source_assets_count |  |
| rumusan_available | false |
| quiz_mcq_available | false |
| quiz_mr_available | false |
| interaction_requirement | UNKNOWN |
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_SOURCE |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — no source read |
| open_human_decisions | BAHAGIAN_BOUNDARY; CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_AUTHORITY_UNRESOLVED |
| blocker_reason | No approved source document for this Topik is in custody. Its existence and title are attested by the PL06 montage; nothing else about it is. |
| blocking_conditions | NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY; BAHAGIAN_BOUNDARY_UNRESOLVED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 2 |

## `K5-PL06-T03-BNEXT` — Komponen Landskap

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 3 |
| topik_title | Komponen Landskap |
| bahagian_number |  |
| bahagian_title |  |
| unit_scope | REMAINING |
| source_document | NONE_IN_CUSTODY |
| source_page_range | UNKNOWN — the B02 extract ends at modul ms 249 |
| source_reference | A2 — Bariah's answered review guide, Tamat destination question, verbatim '✓ A. Bahagian seterusnya dalam Topik 3.'; corroborated by A3 'Logical next destination is the next Bahagian in Topik 3' |
| source_authority_class | BARIAH_DIRECT_WRITTEN_CONFIRMATION |
| source_attests | EXISTENCE_ONLY — no number, no title, no page range was given |
| controlled_content_available | false |
| existing_id_input_available | false |
| storyboard_input_available | false |
| source_rows_count |  |
| source_figures_count |  |
| source_tables_count |  |
| source_assets_count |  |
| rumusan_available | false |
| quiz_mcq_available | false |
| quiz_mr_available | false |
| interaction_requirement | UNKNOWN |
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_SOURCE |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | Same Topik as B02, so the B02 glossary is likely but not proven to apply |
| standards_or_external_claims | UNKNOWN — no source read |
| open_human_decisions | BAHAGIAN_NUMBER_AND_TITLE; CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_AUTHORITY_UNRESOLVED |
| blocker_reason | A human attested that this unit exists and that the B02 learner navigates to it. Nobody has said what number it carries, what it is called, or which module pages it occupies. No source is in custody. |
| blocking_conditions | NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY; BAHAGIAN_BOUNDARY_UNRESOLVED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 3 |

## `K5-PL06-T01` — Proses Memula Kerja

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 1 |
| topik_title | Proses Memula Kerja |
| bahagian_number |  |
| bahagian_title |  |
| unit_scope | REMAINING |
| source_document | NONE_IN_CUSTODY |
| source_page_range | UNKNOWN |
| source_reference | M2 — SB_K5PL6_montaj_v1.pptx slide 3, verbatim 'Topik 1: Proses Memula Kerja' |
| source_authority_class | BARIAH_SUPPLIED_UPSTREAM_ARTIFACT |
| source_attests | TOPIK_EXISTENCE_AND_TITLE_ONLY |
| controlled_content_available | false |
| existing_id_input_available | false |
| storyboard_input_available | false |
| source_rows_count |  |
| source_figures_count |  |
| source_tables_count |  |
| source_assets_count |  |
| rumusan_available | false |
| quiz_mcq_available | false |
| quiz_mr_available | false |
| interaction_requirement | UNKNOWN |
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_SOURCE |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — no source read |
| open_human_decisions | BAHAGIAN_BOUNDARY; CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_AUTHORITY_UNRESOLVED |
| blocker_reason | No approved source document for this Topik is in custody. Its existence and title are attested by the PL06 montage; nothing else about it is. |
| blocking_conditions | NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY; BAHAGIAN_BOUNDARY_UNRESOLVED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 4 |

## `K5-PL06-T05` — Pengurusan Kualiti Projek

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 5 |
| topik_title | Pengurusan Kualiti Projek |
| bahagian_number |  |
| bahagian_title |  |
| unit_scope | REMAINING |
| source_document | NONE_IN_CUSTODY |
| source_page_range | UNKNOWN |
| source_reference | M2 — SB_K5PL6_montaj_v1.pptx slide 3, verbatim 'Topik 5: Pengurusan Kualiti Projek' |
| source_authority_class | BARIAH_SUPPLIED_UPSTREAM_ARTIFACT |
| source_attests | TOPIK_EXISTENCE_AND_TITLE_ONLY |
| controlled_content_available | false |
| existing_id_input_available | false |
| storyboard_input_available | false |
| source_rows_count |  |
| source_figures_count |  |
| source_tables_count |  |
| source_assets_count |  |
| rumusan_available | false |
| quiz_mcq_available | false |
| quiz_mr_available | false |
| interaction_requirement | UNKNOWN |
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_SOURCE |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — no source read |
| open_human_decisions | BAHAGIAN_BOUNDARY; CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_AUTHORITY_UNRESOLVED |
| blocker_reason | No approved source document for this Topik is in custody. Its existence and title are attested by the PL06 montage; nothing else about it is. |
| blocking_conditions | NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY; BAHAGIAN_BOUNDARY_UNRESOLVED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 5 |

## `K5-PL06-T06` — Perlindungan Dan Penambahbaikan Alam Sekitar

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 6 |
| topik_title | Perlindungan Dan Penambahbaikan Alam Sekitar |
| bahagian_number |  |
| bahagian_title |  |
| unit_scope | REMAINING |
| source_document | NONE_IN_CUSTODY |
| source_page_range | UNKNOWN |
| source_reference | M2 — SB_K5PL6_montaj_v1.pptx slide 3, verbatim 'Topik 6: Perlindungan Dan Penambahbaikan Alam Sekitar' |
| source_authority_class | BARIAH_SUPPLIED_UPSTREAM_ARTIFACT |
| source_attests | TOPIK_EXISTENCE_AND_TITLE_ONLY |
| controlled_content_available | false |
| existing_id_input_available | false |
| storyboard_input_available | false |
| source_rows_count |  |
| source_figures_count |  |
| source_tables_count |  |
| source_assets_count |  |
| rumusan_available | false |
| quiz_mcq_available | false |
| quiz_mr_available | false |
| interaction_requirement | UNKNOWN |
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_SOURCE |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — no source read |
| open_human_decisions | BAHAGIAN_BOUNDARY; CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_AUTHORITY_UNRESOLVED |
| blocker_reason | No approved source document for this Topik is in custody. Its existence and title are attested by the PL06 montage; nothing else about it is. |
| blocking_conditions | NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY; BAHAGIAN_BOUNDARY_UNRESOLVED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 6 |

## `K5-PL06-T07` — Demobilisasi

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 7 |
| topik_title | Demobilisasi |
| bahagian_number |  |
| bahagian_title |  |
| unit_scope | REMAINING |
| source_document | NONE_IN_CUSTODY |
| source_page_range | UNKNOWN |
| source_reference | M2 — SB_K5PL6_montaj_v1.pptx slide 3, verbatim 'Topik 7: Demobilisasi' |
| source_authority_class | BARIAH_SUPPLIED_UPSTREAM_ARTIFACT |
| source_attests | TOPIK_EXISTENCE_AND_TITLE_ONLY |
| controlled_content_available | false |
| existing_id_input_available | false |
| storyboard_input_available | false |
| source_rows_count |  |
| source_figures_count |  |
| source_tables_count |  |
| source_assets_count |  |
| rumusan_available | false |
| quiz_mcq_available | false |
| quiz_mr_available | false |
| interaction_requirement | UNKNOWN |
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_SOURCE |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — no source read |
| open_human_decisions | BAHAGIAN_BOUNDARY; CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_AUTHORITY_UNRESOLVED |
| blocker_reason | No approved source document for this Topik is in custody. Its existence and title are attested by the PL06 montage; nothing else about it is. |
| blocking_conditions | NO_APPROVED_SOURCE_DOCUMENT_IN_CUSTODY; BAHAGIAN_BOUNDARY_UNRESOLVED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 7 |

# 4. Source anomalies found while reading the evidence

Recorded, not silently corrected.

| id | locus | finding | impact | owner | status |
|---|---|---|---|---|---|
| SRC-ANOM-001 | SB_K5PL6_montaj_v1.pptx slide 3, shape 'Senarai Pakej Latihan' | The header on the PL06 topic-list slide is numbered PL01 while carrying PL06's title. Slide 2 of the same deck numbers it PL06 correctly. The seven topic titles themselves are unaffected. | Cosmetic in the montage; would be visible to a learner if the montage ships as is. Not ours to correct — the montage is a Bariah-supplied upstream artifact. | BARIAH | OPEN_NOT_OURS |
| SRC-ANOM-002 | SB_K5PL6_montaj_v1.pptx slide 3, shape names | Shape names are recycled from another Pakej Latihan's deck; the montage is template-instantiated. Consistent with the decision-desk finding that the 16 K5 prompts are template-instantiated. | None on content. It does mean shape names must never be used as a semantic key when reading montage or template-derived decks. | NONE | RECORDED_NO_ACTION |
| SRC-ANOM-003 | ratified character bank vs the delivered B02 cast | B02 ships Alya and Encik Rahman. The ratified K5 character bank marks Haziq and Encik Roslan CANONICAL and eight other names OFF-CANON. Bariah approved the B02 pair in writing and separately ruled that character names should apply across the whole of PL06 'bergantung kepada kesesuaian'. Whether that promotes Alya and Encik Rahman over the ratified pair, or the reverse, is NOT settled. | Blocks cast binding for every non-B02 PL06 unit. Does not block B02. | BARIAH_AND_CAIR | OPEN_BLOCKING_SCALE_OUT |

# 5. Frozen evidence register

| ref | kind | path | bytes | sha256 | establishes | authority |
|---|---|---|---|---|---|---|
| M1 | FROZEN_ARTIFACT_PPTX | `reviews/storyboard-bariah/v0_3_bariah_review/SB_K5_montaj_v1.pptx` | 61292 | 79a07b460ddb940d… | K5 course title and the eight Pakej Latihan, PL01-PL08, slide 2 | BARIAH_SUPPLIED_UPSTREAM_ARTIFACT |
| M2 | FROZEN_ARTIFACT_PPTX | `reviews/storyboard-bariah/v0_3_bariah_review/SB_K5PL6_montaj_v1.pptx` | 70656 | 97ccab1c2aef8891… | the seven PL06 Topik and their titles, slide 3; PL06 objectives, slide 2 | BARIAH_SUPPLIED_UPSTREAM_ARTIFACT |
| A2 | FROZEN_ARTIFACT_DOCX | `reviews/storyboard-bariah/v0_3_bariah_review/Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx` | 43342 | c15ae05e20358eda… | Bariah's answered review guide: Tamat destination = the NEXT BAHAGIAN in Topik 3; character names to apply across the whole of PL06 | BARIAH_DIRECT_WRITTEN_CONFIRMATION |
| A3 | FROZEN_ARTIFACT_DOCX | `reviews/storyboard-bariah/v0_3_bariah_review/K5_PL06_T03_B02_UPDATED_SG_v0.3.docx` | 56475 | f3166e42f84d4b1f… | executable Style and Guidelines v0.3; the shell/Rumusan/quiz/Tamat grammar the B02 build implements | CONSOLIDATED_EXECUTABLE_SG |
| P1 | SOURCE_EXTRACT_PDF_NOT_IN_REPOSITORY | `K5_PL06_T03_B02_pages_256269.pdf` | 429918 | 30a6903dacbd7e8b… | the ONLY module content ever received: modul ms 238-249 / physical 256-269, 14 pages, covering K5 PL06 T03 B02 alone. Identity is recorded in B02_ASSET_MANIFEST.md; the file itself is NOT in this repository, only the 14 JPEGs extracted from it | SOURCE_ATTESTED_EXTRACT |
| D1 | RATIFIED_DECISION | `reviews/stage-0a/STAGE_0A_EVIDENCE_INVENTORY.md` | — | — | SBAT-ADR-004 §1 decision granularity = TOPIK, key (course_code, pl, topik); per-Bahagian rows REJECTED. §3 K2/K3/K5 are LOCKED courses, OPEN_COURSES = ["K4"] | RATIFIED_ARCHITECTURE_DECISION |
| D2 | RATIFIED_CHARACTER_BANK | `sbat/cair-decision-desk.html` | — | — | Hilmi LOCKED course narrator, VO-only; Haziq and Encik Roslan CANONICAL; eight further names OFF-CANON. All 16 K5 decision rows are EMPTY | RATIFIED_CHARACTER_BANK |
| C1 | SOURCE_CUSTODY_FINDING | `reviews/sample-19slides/SOURCE_CUSTODY_AND_COVERAGE.md` | — | — | F2, MEASURED_FACT: the approved K5 module is not present in the repository — no module PDF, no extracted source nodes, no screen-to-source binding table beyond the B02 slice | MEASURED_FACT |
| B1 | DELIVERED_ARTIFACT | `reviews/source-completion/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4_1.pptx` | 471881 | faef6c85745d2750… | the delivered and call-approved B02 storyboard, 100 review pages | DELIVERED_REVIEW_CANDIDATE |
