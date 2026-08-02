# PL06_STORYBOARD_PRODUCTION_INVENTORY — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py` — do not hand-edit this file; edit the controlled data source and re-emit.

```
UNITS = 14
TOPIK_ENUMERATED = 7 of 7
BAHAGIAN_ENUMERATED = 14 of 14
TOPOLOGY = 3 / 2 / 5 / 1 / 1 / 1 / 1
COMPLETED = 1   REMAINING = 13
GROUPING_AUTHORITY = REFERENCED_NOT_FROZEN
VERDICT = PL06_SOURCE_BOUNDARY_INGEST_COMPLETE_READY_FOR_T04_EXTRACTION
```

> **Stage 4.2F-A2 replaced this inventory's foundation.** The previous version listed **8** units at Topik granularity with every Bahagian unresolved, because the only artifact describing PL06 was a montage slide that enumerates Topik and nothing else. The source ingest supplies the complete module by identity and a frozen boundary map with a named DOCX heading anchor for all **14** lesson units. Every row below is now read from that map, not asserted here.

# 1. What the evidence establishes

| Level | Established | Evidence |
|---|---|---|
| Course | K5 — Kursus Kerja Bangunan – Pembinaan Landskap Luar | M1 |
| Pakej Latihan | eight, PL01–PL08, named | M1 slide 2 |
| PL06 Topik | **seven, named** | M2 slide 3, corroborated by F1 body headings |
| PL06 Bahagian | **fourteen**, topology 3 / 2 / 5 / 1 / 1 / 1 / 1 | F2 boundary map |
| PL06 module span | pages 162–309; PL07 begins at 310 | F1 / F2 |
| Per-unit boundary | named DOCX heading anchor + paragraph index | F2 |
| T03 B02 content | 26 source rows, 14 assets, modul ms 237–250 | P1, F2 |
| Any other unit's content | **not yet extracted** | — |

# 1.1 What it does not establish

The lesson **grouping** authority is `REFERENCED_NOT_FROZEN`. The boundaries themselves — every unit's start and end anchor is a named docx body heading with a paragraph index, independently checkable against the source. What is not established: why these particular 14 groupings. Two adjacent subtopics being one lesson rather than two is a human decision, and the artifact recording it is not here. Referenced as `SMC-CIDB-K5-DAFTAR-KEPUTUSAN-BARIAH-KONSOLIDASI_v1.0`, `K5-STR-004`, `K5-STR-006`, `K5-STR-005` — 0 occurrences anywhere in the repository outside the freeze package's own metadata.

Not a blocker for T04 extraction, by explicit instruction and on the merits: the T04 boundary is a single Topik with a single lesson, so no grouping judgement is involved in it at all. It matters most for Topik 1, 2 and 3, where 3 + 2 + 5 lessons were grouped out of subtopics that could have been split differently.

The seven Topik titles, as carried by the frozen boundary map:

1. **Topik 1: Proses Memula Kerja** — 3 lessons
2. **Topik 2: Elemen Pembinaan Landskap** — 2 lessons
3. **Topik 3: Komponen Landskap** — 5 lessons
4. **Topik 4: Penjagaan dan Penyelenggaraan** — 1 lesson
5. **Topik 5: Pengurusan Kualiti Projek** — 1 lesson
6. **Topik 6: Perlindungan dan Penambahbaikan Alam Sekitar** — 1 lesson
7. **Topik 7: Demobilisasi** — 1 lesson

# 2. Unit inventory

| order | unit_id | lesson title | modul ms | boundary | scope | readiness | lane |
|---|---|---|---|---|---|---|---|
| 0 | `K5-PL06-T03-B02` | Struktur Taman dan Perabot Taman | 237-250 | shared | DELIVERED_BASELINE | `READY_WITH_HOLDS` | A |
| 1 | `K5-PL06-T04-B01` | Penjagaan dan Penyelenggaraan | 276-283 | clean | REMAINING | `SOURCE_INCOMPLETE` | D |
| 2 | `K5-PL06-T01-B01` | Proses Memula Kerja - Penyediaan Tapak | 162-181 | shared | REMAINING | `SOURCE_INCOMPLETE` | D |
| 3 | `K5-PL06-T01-B02` | Jadual Kerja dan Perlaksanaan Pembinaan Landskap | 181-188 | shared | REMAINING | `SOURCE_INCOMPLETE` | D |
| 4 | `K5-PL06-T01-B03` | Sumber-Sumber yang Diperlukan Untuk Memulakan Projek Landskap | 188-200 | shared | REMAINING | `SOURCE_INCOMPLETE` | D |
| 5 | `K5-PL06-T02-B01` | Elemen Landskap Kejur dan Elemen Landskap Lembut/Penanaman | 201-215 | shared | REMAINING | `SOURCE_INCOMPLETE` | D |
| 6 | `K5-PL06-T02-B02` | Kerja-Kerja Berkaitan dengan Mekanikal & Elektrikal (M&E) | 215-225 | shared | REMAINING | `SOURCE_INCOMPLETE` | D |
| 7 | `K5-PL06-T03-B01` | Kawasan Berturap dan Gelanggang Sukan & Permainan | 226-237 | shared | REMAINING | `SOURCE_INCOMPLETE` | D |
| 8 | `K5-PL06-T03-B03` | Infrastruktur | 250-255 | shared | REMAINING | `SOURCE_INCOMPLETE` | D |
| 9 | `K5-PL06-T03-B04` | Badan Air (Water Body) | 255-261 | shared | REMAINING | `SOURCE_INCOMPLETE` | D |
| 10 | `K5-PL06-T03-B05` | Pencahayaan dan Pengairan | 262-275 | clean | REMAINING | `SOURCE_INCOMPLETE` | D |
| 11 | `K5-PL06-T05-B01` | Pengurusan Kualiti Projek | 284-293 | clean | REMAINING | `SOURCE_INCOMPLETE` | D |
| 12 | `K5-PL06-T06-B01` | Perlindungan dan Penambahbaikan Alam Sekitar | 294-302 | clean | REMAINING | `SOURCE_INCOMPLETE` | D |
| 13 | `K5-PL06-T07-B01` | Demobilisasi | 303-309 | clean | REMAINING | `SOURCE_INCOMPLETE` | D |

Six of the fourteen units start or end on a **shared** module page (181, 188, 215, 237, 250, 255) and must be split by heading anchor, never by page extraction.


# 3. Per-unit detail

## `K5-PL06-T03-B02` — Komponen Landskap, Bahagian 2

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 3 |
| topik_title | Komponen Landskap |
| bahagian_number | 2 |
| bahagian_title | Struktur Taman dan Perabot Taman |
| unit_scope | DELIVERED_BASELINE |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 237-250 / rendered PDF 255-268 |
| source_reference | F2 — frozen boundary map, K5-PL06-T03-B02: start anchor '3.3 Struktur Taman', stop before '3.5 Infrastruktur', DOCX paragraph 4631 to before 4704 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
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
| qa_support_status | FULLY_SUPPORTED — 461 gate records, 51 mutation fixtures |
| lane | LANE_A_EXISTING_SUPPORTED_PATTERN |
| readiness_status | READY_WITH_HOLDS |
| blocker_reason | Delivered and call-approved. Holds are source-authority only and none blocks this unit's review candidacy: MS2680, B02-CAIR-INT-001, and the LMS navigation ruling. Microsoft PowerPoint smoke is not recorded. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 0 |

## `K5-PL06-T04-B01` — Penjagaan dan Penyelenggaraan, Bahagian 1

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 4 |
| topik_title | Penjagaan dan Penyelenggaraan |
| bahagian_number | 1 |
| bahagian_title | Penjagaan dan Penyelenggaraan |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 276-283 / rendered PDF 294-301 |
| source_reference | F2 — frozen boundary map, K5-PL06-T04-B01: start anchor '4.0 PENJAAGAAN DAN PENYELENGGARAAN (body typo; canonical title from TOC)', stop before '5.0 PENGURUSAN KUALITI PROJEK', DOCX paragraph 5220 to before 5360 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Page boundary is clean. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 1 |

## `K5-PL06-T01-B01` — Proses Memula Kerja, Bahagian 1

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 1 |
| topik_title | Proses Memula Kerja |
| bahagian_number | 1 |
| bahagian_title | Proses Memula Kerja - Penyediaan Tapak |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 162-181 / rendered PDF 180-199 |
| source_reference | F2 — frozen boundary map, K5-PL06-T01-B01: start anchor '1.0 PROSES MEMULA KERJA', stop before '1.2 Jadual Kerja', DOCX paragraph 3375 to before 3743 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Boundary needs heading-anchor extraction, not page slicing: end page 181 shared with the next lesson. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 2 |

## `K5-PL06-T01-B02` — Proses Memula Kerja, Bahagian 2

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 1 |
| topik_title | Proses Memula Kerja |
| bahagian_number | 2 |
| bahagian_title | Jadual Kerja dan Perlaksanaan Pembinaan Landskap |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 181-188 / rendered PDF 199-206 |
| source_reference | F2 — frozen boundary map, K5-PL06-T01-B02: start anchor '1.2 Jadual Kerja', stop before '1.4 Sumber-Sumber yang Diperlukan Untuk Memulakan Projek Landskap', DOCX paragraph 3743 to before 3887 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Boundary needs heading-anchor extraction, not page slicing: start page 181 shared with the preceding lesson; end page 188 shared with the next lesson. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 3 |

## `K5-PL06-T01-B03` — Proses Memula Kerja, Bahagian 3

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 1 |
| topik_title | Proses Memula Kerja |
| bahagian_number | 3 |
| bahagian_title | Sumber-Sumber yang Diperlukan Untuk Memulakan Projek Landskap |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 188-200 / rendered PDF 206-218 |
| source_reference | F2 — frozen boundary map, K5-PL06-T01-B03: start anchor '1.4 Sumber-Sumber yang Diperlukan Untuk Memulakan Projek Landskap', stop before '2.0 ELEMEN PEMBINAAN LANDSKAP', DOCX paragraph 3887 to before 4085 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Boundary needs heading-anchor extraction, not page slicing: start page 188 shared with the preceding lesson. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 4 |

## `K5-PL06-T02-B01` — Elemen Pembinaan Landskap, Bahagian 1

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 2 |
| topik_title | Elemen Pembinaan Landskap |
| bahagian_number | 1 |
| bahagian_title | Elemen Landskap Kejur dan Elemen Landskap Lembut/Penanaman |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 201-215 / rendered PDF 219-233 |
| source_reference | F2 — frozen boundary map, K5-PL06-T02-B01: start anchor '2.0 ELEMEN PEMBINAAN LANDSKAP', stop before '2.3 Kerja-Kerja berkaitan dengan Mekanikal & Elektrikal (M&E)', DOCX paragraph 4085 to before 4340 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Boundary needs heading-anchor extraction, not page slicing: end page 215 shared with the next lesson. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 5 |

## `K5-PL06-T02-B02` — Elemen Pembinaan Landskap, Bahagian 2

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 2 |
| topik_title | Elemen Pembinaan Landskap |
| bahagian_number | 2 |
| bahagian_title | Kerja-Kerja Berkaitan dengan Mekanikal & Elektrikal (M&E) |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 215-225 / rendered PDF 233-243 |
| source_reference | F2 — frozen boundary map, K5-PL06-T02-B02: start anchor '2.3 Kerja-Kerja berkaitan dengan Mekanikal & Elektrikal (M&E)', stop before '3.0 KOMPONEN LANDSKAP', DOCX paragraph 4340 to before 4463 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Boundary needs heading-anchor extraction, not page slicing: start page 215 shared with the preceding lesson. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 6 |

## `K5-PL06-T03-B01` — Komponen Landskap, Bahagian 1

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 3 |
| topik_title | Komponen Landskap |
| bahagian_number | 1 |
| bahagian_title | Kawasan Berturap dan Gelanggang Sukan & Permainan |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 226-237 / rendered PDF 244-255 |
| source_reference | F2 — frozen boundary map, K5-PL06-T03-B01: start anchor '3.0 KOMPONEN LANDSKAP', stop before '3.3 Struktur Taman', DOCX paragraph 4463 to before 4631 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Boundary needs heading-anchor extraction, not page slicing: end page 237 shared with the next lesson. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 7 |

## `K5-PL06-T03-B03` — Komponen Landskap, Bahagian 3

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 3 |
| topik_title | Komponen Landskap |
| bahagian_number | 3 |
| bahagian_title | Infrastruktur |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 250-255 / rendered PDF 268-273 |
| source_reference | F2 — frozen boundary map, K5-PL06-T03-B03: start anchor '3.5 Infrastruktur', stop before '3.6 Badan Air (Water Body)', DOCX paragraph 4704 to before 4815 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Boundary needs heading-anchor extraction, not page slicing: start page 250 shared with the preceding lesson; end page 255 shared with the next lesson. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 8 |

## `K5-PL06-T03-B04` — Komponen Landskap, Bahagian 4

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 3 |
| topik_title | Komponen Landskap |
| bahagian_number | 4 |
| bahagian_title | Badan Air (Water Body) |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 255-261 / rendered PDF 273-279 |
| source_reference | F2 — frozen boundary map, K5-PL06-T03-B04: start anchor '3.6 Badan Air (Water Body)', stop before '3.7 Pencahayaan / Lighting', DOCX paragraph 4815 to before 4951 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Boundary needs heading-anchor extraction, not page slicing: start page 255 shared with the preceding lesson. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 9 |

## `K5-PL06-T03-B05` — Komponen Landskap, Bahagian 5

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 3 |
| topik_title | Komponen Landskap |
| bahagian_number | 5 |
| bahagian_title | Pencahayaan dan Pengairan |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 262-275 / rendered PDF 280-293 |
| source_reference | F2 — frozen boundary map, K5-PL06-T03-B05: start anchor '3.7 Pencahayaan / Lighting', stop before '4.0 PENJAAGAAN DAN PENYELENGGARAAN', DOCX paragraph 4951 to before 5220 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Page boundary is clean. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 10 |

## `K5-PL06-T05-B01` — Pengurusan Kualiti Projek, Bahagian 1

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 5 |
| topik_title | Pengurusan Kualiti Projek |
| bahagian_number | 1 |
| bahagian_title | Pengurusan Kualiti Projek |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 284-293 / rendered PDF 302-311 |
| source_reference | F2 — frozen boundary map, K5-PL06-T05-B01: start anchor '5.0 PENGURUSAN KUALITI PROJEK', stop before '6.0 PERLINDUNGAN DAN PENAMBAHBAIKAN ALAM SEKITAR', DOCX paragraph 5360 to before 5543 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Page boundary is clean. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 11 |

## `K5-PL06-T06-B01` — Perlindungan dan Penambahbaikan Alam Sekitar, Bahagian 1

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 6 |
| topik_title | Perlindungan dan Penambahbaikan Alam Sekitar |
| bahagian_number | 1 |
| bahagian_title | Perlindungan dan Penambahbaikan Alam Sekitar |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 294-302 / rendered PDF 312-320 |
| source_reference | F2 — frozen boundary map, K5-PL06-T06-B01: start anchor '6.0 PERLINDUNGAN DAN PENAMBAHBAIKAN ALAM SEKITAR', stop before '7.0 DEMOBILISASI', DOCX paragraph 5543 to before 5705 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Page boundary is clean. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 12 |

## `K5-PL06-T07-B01` — Demobilisasi, Bahagian 1

| field | value |
|---|---|
| pl | PL06 |
| topik_number | 7 |
| topik_title | Demobilisasi |
| bahagian_number | 1 |
| bahagian_title | Demobilisasi |
| unit_scope | REMAINING |
| source_document | [PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx |
| source_page_range | modul ms 303-309 / rendered PDF 321-327 |
| source_reference | F2 — frozen boundary map, K5-PL06-T07-B01: start anchor '7.0 DEMOBILISASI', stop before 'PL07: PENYERAHAN PROJEK', DOCX paragraph 5705 to before 5804 |
| source_authority_class | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
| source_attests | UNIT_BOUNDARY_AND_PAGE_RANGE |
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
| interaction_pattern_candidate | NOT_DETERMINABLE_WITHOUT_CONTENT_EXTRACTION |
| visual_requirement | UNKNOWN |
| narration_requirement | PL06_SHELL_GRAMMAR_APPLIES (A3) — content unknown |
| terminology_risks | PL06 pronunciation precedence unratified; the English-term italics list is B02-derived and must be re-derived per unit |
| standards_or_external_claims | UNKNOWN — content not read |
| open_human_decisions | CAST_BINDING_PL06_SCOPE |
| generator_support_status | SHELL_SUPPORTED_CONTENT_UNSUPPORTED |
| qa_support_status | SHELL_GATES_REUSABLE_CONTENT_GATES_ABSENT |
| lane | LANE_D_SOURCE_INCOMPLETE |
| readiness_status | SOURCE_INCOMPLETE |
| blocker_reason | Source document and unit boundary are now in custody by identity — that is what Stage 4.2F-A2 closed. What remains is that the CONTENT has not been extracted: no controlled content, no visual inventory, no Rumusan and no quiz source for this unit. Page boundary is clean. |
| blocking_conditions | CONTROLLED_CONTENT_NOT_EXTRACTED; NO_RUMUSAN_SOURCE; NO_QUIZ_SOURCE; VISUAL_INVENTORY_NOT_EXTRACTED; CAST_BINDING_UNRESOLVED |
| recommended_execution_order | 13 |

# 4. Source anomalies found while reading the evidence

Recorded, not silently corrected.

| id | locus | finding | impact | owner | status |
|---|---|---|---|---|---|
| SRC-ANOM-001 | SB_K5PL6_montaj_v1.pptx slide 3, shape 'Senarai Pakej Latihan' | The header on the PL06 topic-list slide is numbered PL01 while carrying PL06's title. Slide 2 of the same deck numbers it PL06 correctly. The seven topic titles themselves are unaffected. | Cosmetic in the montage; would be visible to a learner if the montage ships as is. Not ours to correct — the montage is a Bariah-supplied upstream artifact. | BARIAH | OPEN_NOT_OURS |
| SRC-ANOM-002 | SB_K5PL6_montaj_v1.pptx slide 3, shape names | Shape names are recycled from another Pakej Latihan's deck; the montage is template-instantiated. Consistent with the decision-desk finding that the 16 K5 prompts are template-instantiated. | None on content. It does mean shape names must never be used as a semantic key when reading montage or template-derived decks. | NONE | RECORDED_NO_ACTION |
| SRC-ANOM-003 | ratified character bank vs the delivered B02 cast | B02 ships Alya and Encik Rahman. The ratified K5 character bank marks Haziq and Encik Roslan CANONICAL and eight other names OFF-CANON. Bariah approved the B02 pair in writing and separately ruled that character names should apply across the whole of PL06 'bergantung kepada kesesuaian'. Whether that promotes Alya and Encik Rahman over the ratified pair, or the reverse, is NOT settled. | Blocks cast binding for every non-B02 PL06 unit. Does not block B02. | BARIAH_AND_CAIR | OPEN_BLOCKING_SCALE_OUT |
| SRC-ANOM-004 | module body heading, Topik 4, module page 276 | The body heading of the selected first-proof unit is misspelled in the source. The canonical title 'Penjagaan dan Penyelenggaraan' comes from the Table of Contents under K5-STR-005. Extraction anchors on the body string as written; the learner-facing label uses the canonical form. | Directly affects T04-B01 extraction. An anchor search for the correctly spelled heading finds nothing. | BARIAH | RECORDED_NOT_SILENTLY_CORRECTED |
| SRC-ANOM-005 | module body heading, section 7.2, Topik 7 | Misspelled in the source body; governed label is 'Proses Demobilisasi'. | Affects T07-B01 extraction only. | BARIAH | RECORDED_NOT_SILENTLY_CORRECTED |
| SRC-ANOM-006 | module Table of Contents vs body heading positions | The TOC and the body disagree on where sections begin. The freeze package resolves this by BODY_ANCHOR_PRECEDENCE: body heading anchors govern extraction, the TOC is cross-check only. | Any extraction driven from the TOC would land on the wrong page. This is the reason the boundary map carries DOCX paragraph indices as well as page ranges. | NONE | RESOLVED_BY_BODY_ANCHOR_PRECEDENCE |

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
| F1 | PRIMARY_SOURCE_ARTIFACT_EXTERNAL | `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx` | 16832861 | 5a9142cdfa1a8090… | the complete CE14 module, PL01-PL08. PL06 spans module pages 162-309; PL07 begins at 310. Held externally by identity, Drive file ID 16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4 — not in this repository | PROOFREAD_FINAL_MODULE_SOURCE |
| F2 | FROZEN_BOUNDARY_MAP | `docs/pl06/source-freeze/PL06_LESSON_BOUNDARY_MAP_v1.json` | 12977 | aa02cd3c784113b0… | the 14-unit PL06 lesson boundary map: per-unit module and rendered-PDF page ranges, DOCX paragraph anchors, start and end heading anchors, and shared-page flags. Ingested byte-identically from the verified freeze | DOCX_BODY_HEADINGS_PLUS_REFERENCED_LESSON_GROUPING |
