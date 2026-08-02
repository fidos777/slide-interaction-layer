# T04_EXTERNAL_CLAIMS_REGISTER — v1

Stage 4.2F-B0. Generated from `docs/pl06/t04/tools/t04_emit_v1.py`.

```
CLAIMS = 9
EXTERNAL_VERIFICATION_REQUIRED = 2
SAFE_FOR_REVIEW_DECK = 7
BLOCKS_THIS_UNIT = 0
MS2680_IN_T04 = false
```

> **No claim in T04 blocks this unit.** Two require external verification before canonical freeze; the rest are source statements that render safely in a review deck. MS2680 — the open B02 standards item — appears **nowhere** in T04, so it does not touch this unit. A global open item must not block unrelated content.

# Claims

| id | kind | quote | status | scope | rows |
|---|---|---|---|---|---|
| `T04-CLM-01` | LEGISLATION | Penggunaan racun kimia dikawal oleh Akta Racun Makhluk Perosak 1974. | **EXTERNAL_VERIFICATION_REQUIRED** | BLOCKS_CANONICAL_FREEZE | T04-ROW-066 |
| `T04-CLM-02` | LICENSING | Kontraktor mesti memastikan pekerja yang menjalankan semburan racun adalah pengendali racun berlesen … | **EXTERNAL_VERIFICATION_REQUIRED** | BLOCKS_CANONICAL_FREEZE | T04-ROW-067 |
| `T04-CLM-03` | SAFETY_PROCEDURE | PPE requirements for fertiliser and pesticide handling — gloves, face mask, respirator, safety glasses. | **SOURCE_STATEMENT_ONLY** | SAFE_FOR_REVIEW_DECK | T04-ROW-043, T04-ROW-069, T04-ROW-070 |
| `T04-CLM-04` | SAFETY_DOCUMENT | Kontraktor wajib menyimpan Salinan SDS untuk setiap racun yang digunakan di tapak … | **SOURCE_STATEMENT_ONLY** | SAFE_FOR_REVIEW_DECK | T04-ROW-073, T04-ROW-074 |
| `T04-CLM-05` | CHEMICAL_HANDLING | Semburan hanya boleh dilakukan semasa cuaca tenang (tidak berangin) untuk mengelakkan spray drift. | **SOURCE_STATEMENT_ONLY** | SAFE_FOR_REVIEW_DECK | T04-ROW-076 |
| `T04-CLM-06` | MAINTENANCE_FREQUENCY | Amalan terbaik adalah menyiram pada awal pagi atau lewat petang … | **SOURCE_STATEMENT_ONLY** | SAFE_FOR_REVIEW_DECK | T04-ROW-018 |
| `T04-CLM-07` | TECHNICAL_FRAMEWORK | IPM — Integrated Pest Management, prioritising cultural, physical, biological and then chemical control. | **SOURCE_STATEMENT_ONLY** | SAFE_FOR_REVIEW_DECK | T04-ROW-047, T04-ROW-048 |
| `T04-CLM-08` | CONTRACT_AUTHORITY | … seperti yang ditetapkan dalam dokumen kontrak atau diluluskan oleh Pegawai Penguasa. | **SOURCE_STATEMENT_ONLY** | SAFE_FOR_REVIEW_DECK | T04-ROW-039 |
| `T04-CLM-09` | STANDARDS_REFERENCE | No Malaysian Standard is cited anywhere in T04. | **SOURCE_STATEMENT_ONLY** | SAFE_FOR_REVIEW_DECK | — |

# Notes

- **`T04-CLM-01` LEGISLATION** — A named statute with a year. The module states it; we have not verified that the 1974 Act is still the governing instrument or that it has not been amended. Safe to render in a review deck as a source statement; not safe to freeze as canonical fact.
- **`T04-CLM-02` LICENSING** — A licensing obligation placed on the contractor. Same treatment as CLM-01.
- **`T04-CLM-03` SAFETY_PROCEDURE** — Generic protective-equipment guidance, stated by the module, carrying no numeric threshold or standard reference. Renders as source content.
- **`T04-CLM-04` SAFETY_DOCUMENT** — An SDS-retention obligation. Stated as module content; no external document is cited by number.
- **`T04-CLM-05` CHEMICAL_HANDLING** — A qualitative operating condition with no measured wind threshold. Note for the storyboard: do not tighten 'cuaca tenang' into a number.
- **`T04-CLM-06` MAINTENANCE_FREQUENCY** — A timing practice, not a frequency figure. The module explicitly defers the actual frequency to plant type, weather and growth stage rather than stating a number.
- **`T04-CLM-07` TECHNICAL_FRAMEWORK** — A named industry framework used descriptively. The four-tier priority order is the module's own statement.
- **`T04-CLM-08` CONTRACT_AUTHORITY** — A contractual role reference, internal to the module's own frame.
- **`T04-CLM-09` STANDARDS_REFERENCE** — Recorded as a NEGATIVE finding, deliberately. MS2680 belongs to B02 and appears nowhere in this unit, so the open MS2680 item does not touch T04. A global open item must not block unrelated content.

# Two cautions for the storyboard model

- **Do not tighten a qualitative condition into a number.** The source says spraying may only happen in *cuaca tenang (tidak berangin)*. It states no wind speed. Writing one would be inventing a technical threshold.
- **Do not state a watering frequency.** The source gives a timing practice — early morning or late afternoon — and then explicitly defers frequency to plant type, weather and growth stage. That deferral is the content.
