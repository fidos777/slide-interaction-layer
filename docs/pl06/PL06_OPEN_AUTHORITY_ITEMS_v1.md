# PL06_OPEN_AUTHORITY_ITEMS — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py`.

```
STOP_CONDITIONS = 14
BLOCKS_THIS_UNIT = 6
BLOCKS_CANONICAL_FREEZE_ONLY = 4
BLOCKS_MMD_ONLY = 1
BLOCKS_FINAL_RELEASE_ONLY = 3
```

> A global open item does not block an unrelated ready unit. That is why `scope` is a typed field: `BLOCKS_THIS_UNIT` stops a build, the other three do not.

# Stop conditions

| id | condition | scope | applies to | description | resolver | evidence |
|---|---|---|---|---|---|---|
| `STOP-001` | MISSING_APPROVED_SOURCE | **BLOCKS_THIS_UNIT** |  | No approved source document for the unit is in custody. | FIRDAUS / CAIR | CLOSED at Stage 4.2F-A2. The complete module DOCX is in custody by identity (F1, 16,832,861 B, sha 5a9142cd…78df7, Drive 16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4). This is the item that had blocked every remaining unit since 31 July. |
| `STOP-002` | MISSING_BAHAGIAN_BOUNDARY | **BLOCKS_THIS_UNIT** |  | The unit's Bahagian boundaries are not established by any source. | BARIAH / CAIR | CLOSED at Stage 4.2F-A2. All 14 boundaries carry a named DOCX body heading and a paragraph index (F2). Stage 4.2F-A recorded 7 Topik and 1 named Bahagian; the map gives 14 units with start and stop anchors. |
| `STOP-003` | VISUAL_INVENTORY_NOT_EXTRACTED | **BLOCKS_THIS_UNIT** | K5-PL06-T04-B01, K5-PL06-T01-B01, K5-PL06-T01-B02, K5-PL06-T01-B03, K5-PL06-T02-B01, K5-PL06-T02-B02, K5-PL06-T03-B01, K5-PL06-T03-B03, K5-PL06-T03-B04, K5-PL06-T03-B05, K5-PL06-T05-B01, K5-PL06-T06-B01, K5-PL06-T07-B01 | No figure or table photograph has been extracted or hashed for the unit, so no visual subject can be named without inventing one. | CC — extract from the module page range now that it is known | RP-104, RP-209; B02_ASSET_MANIFEST.md is the precedent for what this produces |
| `STOP-004` | CONTROLLED_CONTENT_NOT_EXTRACTED | **BLOCKS_THIS_UNIT** | K5-PL06-T04-B01, K5-PL06-T01-B01, K5-PL06-T01-B02, K5-PL06-T01-B03, K5-PL06-T02-B01, K5-PL06-T02-B02, K5-PL06-T03-B01, K5-PL06-T03-B03, K5-PL06-T03-B04, K5-PL06-T03-B05, K5-PL06-T05-B01, K5-PL06-T06-B01, K5-PL06-T07-B01 | The unit's controlled content model has not been derived, so its screen inventory and interaction pattern cannot be determined. The B02 families must not be assumed. | CC — extract by heading anchor, then BARIAH if the structure is novel | RP-201 to RP-203 |
| `STOP-005` | NO_QUIZ_SOURCE | **BLOCKS_THIS_UNIT** | K5-PL06-T04-B01, K5-PL06-T01-B01, K5-PL06-T01-B02, K5-PL06-T01-B03, K5-PL06-T02-B01, K5-PL06-T02-B02, K5-PL06-T03-B01, K5-PL06-T03-B03, K5-PL06-T03-B04, K5-PL06-T03-B05, K5-PL06-T05-B01, K5-PL06-T06-B01, K5-PL06-T07-B01 | No quiz source or answer key exists for the unit. | CC extraction, then SME sign-off on the key | RP-108 |
| `STOP-006` | CAST_BINDING_UNRESOLVED | **BLOCKS_THIS_UNIT** | K5-PL06-T04-B01, K5-PL06-T01-B01, K5-PL06-T01-B02, K5-PL06-T01-B03, K5-PL06-T02-B01, K5-PL06-T02-B02, K5-PL06-T03-B01, K5-PL06-T03-B03, K5-PL06-T03-B04, K5-PL06-T03-B05, K5-PL06-T05-B01, K5-PL06-T06-B01, K5-PL06-T07-B01 | The ratified character bank marks Haziq and Encik Roslan CANONICAL; B02 ships Alya and Encik Rahman; Bariah's PL06-wide instruction names neither. | BARIAH + CAIR | SRC-ANOM-003, RP-106, RP-215 |
| `STOP-007` | PL06_PRONUNCIATION_PRECEDENCE_UNRATIFIED | **BLOCKS_MMD_ONLY** | ALL | The PL06 pronunciation rule ('PL satu', not 'PL kosong satu') appears in both montage decks as a Note to MMD but is not a ratified contract. | source governance | M1 and M2 Note to MMD; PRONUNCIATION_REGISTER_PL06_v0.4.4.json |
| `STOP-008` | MS2680_VERIFICATION | **BLOCKS_FINAL_RELEASE_ONLY** | K5-PL06-T03-B02 | A standards citation in the B02 source is unverified. | source authority | B02_OPEN_DECISION_INVENTORY_v0.4.4 |
| `STOP-009` | B02_CAIR_INT_001 | **BLOCKS_CANONICAL_FREEZE_ONLY** | ALL | The canonical module DOCX had an identity pinned but no hash. Stage 4.2F-A2 now supplies a hashed module DOCX; whether THIS document is the canonical one B02 was built against has not been established. | FIRDAUS / CAIR | B02_V0_4_INPUT_FREEZE.md §1 input E; now checkable against F1 |
| `STOP-010` | K5_COURSE_LOCKED | **BLOCKS_CANONICAL_FREEZE_ONLY** | ALL | SBAT-ADR-004 §3 locks K2, K3 and K5 in the CAIR decision desk; OPEN_COURSES = ["K4"]. Governs where DECISIONS may be written, not whether storyboards may be produced. | CAIR | D1 |
| `STOP-011` | POWERPOINT_SMOKE_NOT_RECORDED | **BLOCKS_FINAL_RELEASE_ONLY** | ALL | No Microsoft PowerPoint smoke test has been executed or recorded in this environment for any unit. | FIRDAUS | APPROVAL_RECORD.powerpoint_smoke_status |
| `STOP-012` | SOURCE_CONTRADICTION | **BLOCKS_FINAL_RELEASE_ONLY** | ALL | The PL06 montage numbers its own topic-list header PL01 while carrying PL06's title; the module body carries two heading typos. | BARIAH | SRC-ANOM-001, SRC-ANOM-004, SRC-ANOM-005 |
| `STOP-013` | GROUPING_AUTHORITY_NOT_FROZEN | **BLOCKS_CANONICAL_FREEZE_ONLY** | ALL | The human authority behind the 14-lesson grouping is referenced by the boundary map and held nowhere we can reach. The BOUNDARIES are anchored to named DOCX headings and are independently checkable; WHY these particular groupings is not. | CAIR — supply SMC-CIDB-K5-DAFTAR-KEPUTUSAN-BARIAH-KONSOLIDASI_v1.0 | GROUPING_AUTHORITY = REFERENCED_NOT_FROZEN. Explicitly NOT a blocker for T04 extraction: T04 is one Topik with one lesson, so no grouping judgement enters it. |
| `STOP-014` | FREEZE_PACKAGE_DURABLE_CUSTODY_PENDING | **BLOCKS_CANONICAL_FREEZE_ONLY** | ALL | No durable location has been supplied for the 25.1 MB freeze ZIP. Thirteen of its files are ingested; the rendered PDF, fifteen boundary images and the contact sheet survive only as identities. | FIRDAUS — supply the Drive location | EXTERNAL_CUSTODY.freeze_package.custody = DURABLE_CUSTODY_PENDING |

# Source anomalies

| id | locus | verbatim | finding | owner | status |
|---|---|---|---|---|---|
| SRC-ANOM-001 | SB_K5PL6_montaj_v1.pptx slide 3, shape 'Senarai Pakej Latihan' | `PL01: Pengurusan Operasi Pembinaan Landskap` | The header on the PL06 topic-list slide is numbered PL01 while carrying PL06's title. Slide 2 of the same deck numbers it PL06 correctly. The seven topic titles themselves are unaffected. | BARIAH | OPEN_NOT_OURS |
| SRC-ANOM-002 | SB_K5PL6_montaj_v1.pptx slide 3, shape names | `shape names 'Pengurusan Tender', 'Pelaksanaan Pengurusan Kontrak', 'Perancangan Dan Penjadualan Projek' carry PL06 topic text` | Shape names are recycled from another Pakej Latihan's deck; the montage is template-instantiated. Consistent with the decision-desk finding that the 16 K5 prompts are template-instantiated. | NONE | RECORDED_NO_ACTION |
| SRC-ANOM-003 | ratified character bank vs the delivered B02 cast | `Haziq (CANONICAL) / Encik Roslan (CANONICAL) vs Alya / Encik Rahman (B02)` | B02 ships Alya and Encik Rahman. The ratified K5 character bank marks Haziq and Encik Roslan CANONICAL and eight other names OFF-CANON. Bariah approved the B02 pair in writing and separately ruled that character names should apply across the whole of PL06 'bergantung kepada kesesuaian'. Whether that promotes Alya and Encik Rahman over the ratified pair, or the reverse, is NOT settled. | BARIAH_AND_CAIR | OPEN_BLOCKING_SCALE_OUT |
| SRC-ANOM-004 | module body heading, Topik 4, module page 276 | `4.0 PENJAAGAAN DAN PENYELENGGARAAN` | The body heading of the selected first-proof unit is misspelled in the source. The canonical title 'Penjagaan dan Penyelenggaraan' comes from the Table of Contents under K5-STR-005. Extraction anchors on the body string as written; the learner-facing label uses the canonical form. | BARIAH | RECORDED_NOT_SILENTLY_CORRECTED |
| SRC-ANOM-005 | module body heading, section 7.2, Topik 7 | `Proses Demoblisasi` | Misspelled in the source body; governed label is 'Proses Demobilisasi'. | BARIAH | RECORDED_NOT_SILENTLY_CORRECTED |
| SRC-ANOM-006 | module Table of Contents vs body heading positions | `Several TOC offsets differ from body starts` | The TOC and the body disagree on where sections begin. The freeze package resolves this by BODY_ANCHOR_PRECEDENCE: body heading anchors govern extraction, the TOC is cross-check only. | NONE | RESOLVED_BY_BODY_ANCHOR_PRECEDENCE |

# Who owns what

| Owner | Items |
|---|---|
| **FIRDAUS / CAIR** | source delivery for every remaining unit (STOP-001), canonical module integrity (STOP-009), running and recording the PowerPoint smoke (STOP-011) |
| **BARIAH** | Bahagian boundaries (STOP-002), cast binding (STOP-006), the montage numbering anomaly (SRC-ANOM-001), written confirmation of the call approval |
| **source governance** | PL06 pronunciation precedence (STOP-007), MS2680 (STOP-008) |
| **CAIR** | the K5 course lock (STOP-010) |
| **CC** | nothing on this list. Every item here needs a human. |
