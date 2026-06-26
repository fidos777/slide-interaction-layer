# Ontology governance audit checks

Read-only checks a maintainer or the S0 board runs on a **learning/courseware** deck that uses the
ontology. They extend — never relax — the existing S0 board checks
(`../extensions/mmd-elearning/s0-board-governance.md`). Output is a dry-run draft for human review.

| # | Check | Pass condition |
| - | ----- | -------------- |
| 1 | **Coverage** | Every required slide has an `element` + `objective`. |
| 2 | **Mapping fidelity** | The chosen `pattern` is the element's primary or an allowed alternate (`element-to-pattern-map.md`). Flag mismatches (e.g. `E11` not using `P6`). |
| 3 | **Critical visibility** | No `E13` Warning (or essential `E9`) is hidden behind an interaction or gate. |
| 4 | **Gating correctness** | Gating is present only on `required` + gateable elements; required gateable elements in `training` mode are actually gated. |
| 5 | **No orphans** | Every interaction maps to an element/objective — no interaction without a stated purpose. |
| 6 | **One primary element** | At most one primary element per slide. |
| 7 | **Vocabulary integrity** | Every `element` used is defined in `element-ontology.md`; any `bloom` value is from the allowed set. |
| 8 | **Objective traceability** | Each module learning objective is covered by ≥ 1 element (gap report). |

## Severity guidance

- **Blocker:** #3 (critical info hidden), #2 for assessments (`E11`/`E12` mis-mapped), #1 on a
  required slide.
- **Warning:** #4, #5, #6, #8.
- **Info:** #7 vocabulary nits.

## How it runs

1. Parse each slide's element annotation (`metadata-format.md`).
2. Apply checks 1–8; collect findings (slide, check, severity, note).
3. Emit a dry-run report (markdown/CSV) and route to the S0 board as draft tasks. **Never** mutate a
   live board or the deck automatically.

This keeps ontology adoption auditable without adding any runtime to the deck itself.
