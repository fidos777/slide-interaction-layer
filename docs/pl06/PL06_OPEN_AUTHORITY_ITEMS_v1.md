# PL06_OPEN_AUTHORITY_ITEMS — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py`.

```
STOP_CONDITIONS = 12
BLOCKS_THIS_UNIT = 6
BLOCKS_CANONICAL_FREEZE_ONLY = 2
BLOCKS_MMD_ONLY = 1
BLOCKS_FINAL_RELEASE_ONLY = 3
```

> A global open item does not block an unrelated ready unit. That is why `scope` is a typed field: `BLOCKS_THIS_UNIT` stops a build, the other three do not.

# Stop conditions

| id | condition | scope | applies to | description | resolver | evidence |
|---|---|---|---|---|---|---|
| `STOP-001` | MISSING_APPROVED_SOURCE | **BLOCKS_THIS_UNIT** | K5-PL06-T01, K5-PL06-T02, K5-PL06-T03-BNEXT, K5-PL06-T04, K5-PL06-T05, K5-PL06-T06, K5-PL06-T07 | No approved source document for the unit is in custody. | FIRDAUS / CAIR — deliver the module extract for the unit | C1 F2 MEASURED_FACT |
| `STOP-002` | MISSING_BAHAGIAN_BOUNDARY | **BLOCKS_THIS_UNIT** | K5-PL06-T01, K5-PL06-T02, K5-PL06-T03-BNEXT, K5-PL06-T04, K5-PL06-T05, K5-PL06-T06, K5-PL06-T07 | The unit's Bahagian boundaries are not established by any source. Numbering alone is not evidence. | BARIAH / CAIR — confirm the Bahagian list per Topik | M2 attests Topik only; no artifact enumerates Bahagian |
| `STOP-003` | MISSING_VISUAL_SUBJECT_AUTHORITY | **BLOCKS_THIS_UNIT** | K5-PL06-T01, K5-PL06-T02, K5-PL06-T03-BNEXT, K5-PL06-T04, K5-PL06-T05, K5-PL06-T06, K5-PL06-T07 | No source figure or table photograph is bound, so no visual subject can be named without inventing one. | follows STOP-001 | RP-104, RP-209 |
| `STOP-004` | MISSING_INTERACTION_RULING | **BLOCKS_THIS_UNIT** | K5-PL06-T01, K5-PL06-T02, K5-PL06-T03-BNEXT, K5-PL06-T04, K5-PL06-T05, K5-PL06-T06, K5-PL06-T07 | The unit's interaction pattern cannot be derived without its source structure. The B02 families must not be assumed. | follows STOP-001, then BARIAH ruling if the structure is novel | RP-201 to RP-203 |
| `STOP-005` | MISSING_QUIZ_ANSWER_KEY | **BLOCKS_THIS_UNIT** | K5-PL06-T01, K5-PL06-T02, K5-PL06-T03-BNEXT, K5-PL06-T04, K5-PL06-T05, K5-PL06-T06, K5-PL06-T07 | No quiz source or answer key exists for the unit. | follows STOP-001; SME sign-off on the key | RP-108 |
| `STOP-006` | CAST_BINDING_UNRESOLVED | **BLOCKS_THIS_UNIT** | K5-PL06-T01, K5-PL06-T02, K5-PL06-T03-BNEXT, K5-PL06-T04, K5-PL06-T05, K5-PL06-T06, K5-PL06-T07 | The ratified character bank marks Haziq and Encik Roslan CANONICAL; B02 ships Alya and Encik Rahman; Bariah's PL06-wide instruction names neither. | BARIAH + CAIR | SRC-ANOM-003, RP-106, RP-215 |
| `STOP-007` | PL06_PRONUNCIATION_PRECEDENCE_UNRATIFIED | **BLOCKS_MMD_ONLY** | ALL | The PL06 pronunciation rule ('PL satu', not 'PL kosong satu') is present in both montage decks as a Note to MMD but is not a ratified narration contract. | source governance | M1 and M2 Note to MMD; PRONUNCIATION_REGISTER_PL06_v0.4.4.json RESERVED_NOT_ACTIVE |
| `STOP-008` | MS2680_VERIFICATION | **BLOCKS_FINAL_RELEASE_ONLY** | K5-PL06-T03-B02 | A standards citation in the B02 source is unverified. | source authority | B02_OPEN_DECISION_INVENTORY_v0.4.4 |
| `STOP-009` | B02_CAIR_INT_001 | **BLOCKS_CANONICAL_FREEZE_ONLY** | ALL | The canonical module DOCX has an identity pinned but no hash; integrity is unverified. | FIRDAUS / CAIR | B02_V0_4_INPUT_FREEZE.md §1 input E |
| `STOP-010` | K5_COURSE_LOCKED | **BLOCKS_CANONICAL_FREEZE_ONLY** | ALL | SBAT-ADR-004 §3 locks K2, K3 and K5 in the CAIR decision desk; OPEN_COURSES = ["K4"]. This governs where DECISIONS may be written, not whether storyboards may be produced — but no PL06 decision may be recorded in cair_decisions while it holds. | CAIR — the lock lifts when the per-course source drill is complete | D1 |
| `STOP-011` | POWERPOINT_SMOKE_NOT_RECORDED | **BLOCKS_FINAL_RELEASE_ONLY** | ALL | No Microsoft PowerPoint smoke test has been executed or recorded in this environment for any unit. Bariah's call reports the deck opened acceptably on her machine; that is a human observation, not a recorded test. | FIRDAUS — run and record the smoke test | APPROVAL_RECORD.powerpoint_smoke_status |
| `STOP-012` | SOURCE_CONTRADICTION | **BLOCKS_FINAL_RELEASE_ONLY** | ALL | The PL06 montage numbers its own topic-list header PL01 while carrying PL06's title. | BARIAH — the montage is hers | SRC-ANOM-001 |

# Source anomalies

| id | locus | verbatim | finding | owner | status |
|---|---|---|---|---|---|
| SRC-ANOM-001 | SB_K5PL6_montaj_v1.pptx slide 3, shape 'Senarai Pakej Latihan' | `PL01: Pengurusan Operasi Pembinaan Landskap` | The header on the PL06 topic-list slide is numbered PL01 while carrying PL06's title. Slide 2 of the same deck numbers it PL06 correctly. The seven topic titles themselves are unaffected. | BARIAH | OPEN_NOT_OURS |
| SRC-ANOM-002 | SB_K5PL6_montaj_v1.pptx slide 3, shape names | `shape names 'Pengurusan Tender', 'Pelaksanaan Pengurusan Kontrak', 'Perancangan Dan Penjadualan Projek' carry PL06 topic text` | Shape names are recycled from another Pakej Latihan's deck; the montage is template-instantiated. Consistent with the decision-desk finding that the 16 K5 prompts are template-instantiated. | NONE | RECORDED_NO_ACTION |
| SRC-ANOM-003 | ratified character bank vs the delivered B02 cast | `Haziq (CANONICAL) / Encik Roslan (CANONICAL) vs Alya / Encik Rahman (B02)` | B02 ships Alya and Encik Rahman. The ratified K5 character bank marks Haziq and Encik Roslan CANONICAL and eight other names OFF-CANON. Bariah approved the B02 pair in writing and separately ruled that character names should apply across the whole of PL06 'bergantung kepada kesesuaian'. Whether that promotes Alya and Encik Rahman over the ratified pair, or the reverse, is NOT settled. | BARIAH_AND_CAIR | OPEN_BLOCKING_SCALE_OUT |

# Who owns what

| Owner | Items |
|---|---|
| **FIRDAUS / CAIR** | source delivery for every remaining unit (STOP-001), canonical module integrity (STOP-009), running and recording the PowerPoint smoke (STOP-011) |
| **BARIAH** | Bahagian boundaries (STOP-002), cast binding (STOP-006), the montage numbering anomaly (SRC-ANOM-001), written confirmation of the call approval |
| **source governance** | PL06 pronunciation precedence (STOP-007), MS2680 (STOP-008) |
| **CAIR** | the K5 course lock (STOP-010) |
| **CC** | nothing on this list. Every item here needs a human. |
