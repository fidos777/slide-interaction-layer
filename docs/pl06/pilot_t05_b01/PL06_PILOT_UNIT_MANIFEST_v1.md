# PL06 Pilot — Unit Manifest — `K5-PL06-T05-B01`

> **INTERNAL_GENERATION_DRAFT** — machine-authored engineering record. Not reviewed, not
> Bariah-approved, not a production template. **No Bariah readiness is claimed.**

## 1. Identity

| field | value |
|---|---|
| unit_id | `K5-PL06-T05-B01` |
| lesson_title | Pengurusan Kualiti Projek |
| topik | Topik 5 — Pengurusan Kualiti Projek |
| modul page range | ms 284–293 (rendered PDF 302–311) |
| boundary | clean (no shared start/end page) |
| lane | P — one committed non-B03 pilot |
| base_commit | `ebd6d81` |
| branch | `cc/pl06-pilot` |
| selection_basis | highest layout stress of the three committed non-B03 units — see `PL06_PILOT_SELECTION_v1.md` |

## 2. Source provenance (committed inputs only)

| input | path | role |
|---|---|---|
| provisional model | `docs/pl06/batch1_extract/K5_PL06_T05_B01_PROVISIONAL_MODEL_v1.json` | screens, base-state floor, pattern candidacy |
| source extract | `docs/pl06/batch1_extract/K5_PL06_T05_B01_SOURCE_EXTRACT_v1.json` | source rows |
| committed unit model | `docs/pl06/tools/pl06_unit_model_v1.py` (key `K5-PL06-T05-B01`, line 406) | mandatory propositions, assessment, rumusan |
| pattern policy | `docs/pl06/tools/k5_pattern_policy_v1.py` | Bariah rulings A–D; B2 = TEST_REQUIRED |
| policy application | `docs/pl06/tools/k5_policy_apply_v1.py` | per-unit `screen_pattern_plan` (candidate-only for T05-B01) |

The DOCX module source itself is held outside the repository by identity (SHA-256
`5a9142cdfa1a8090…`, 16,832,861 bytes). No figure or table object exists in this unit's source
span (`missing_source_register`).

## 3. Requested artifacts — production status

| # | requested artifact | status | reason |
|---:|---|---|---|
| 1 | Storyboard (PPTX) | **BLOCKED — not produced** | requires the B03-hardcoded generator (D-1) and a decided pattern (D-2) |
| 2 | Lampiran Keadaan 3-panel (PPTX) | **BLOCKED — not produced** | triggered-state set is `UNKNOWN_PENDING_PATTERN_DECISION`; producing it would invent states (D-2, D-3) |
| 3 | previews (PNG) | **BLOCKED — not produced** | nothing defensible to render (depends on #1/#2) |
| 4 | structural / XML QA | **BLOCKED — not produced** | no PPTX exists to inspect |
| 5 | overflow & placeholder scan | **BLOCKED — not produced** | no rendered artifact exists to scan |
| 6 | state inventory reconciliation | **PRODUCED** | `PL06_PILOT_STATE_INVENTORY_RECONCILIATION_v1.md` — records known floor vs undetermined triggered set; no states invented |
| 7 | unit manifest | **PRODUCED** | this document |
| — | defect report | **PRODUCED** | `PL06_PILOT_DEFECT_REPORT_v1.md` |
| — | selection record | **PRODUCED** | `PL06_PILOT_SELECTION_v1.md` |

## 4. Halt record

The pipeline was halted at the Lampiran Keadaan state inventory, as instructed by the pilot
brief ("If generic generation cannot produce a defensible Lampiran state inventory, stop and
record the exact missing shared capability. Do not invent states."). The three blocking
capability gaps are D-1, D-2, D-3 in `PL06_PILOT_DEFECT_REPORT_v1.md`.

Artifacts #1–#5 are intentionally absent. Their absence is the correct outcome, not an
incomplete run: producing any of them at commit `ebd6d81` would require either modifying the
shared generator or inventing the runtime state set — both forbidden.

## 5. Guardrails observed

- Shared generator code (`docs/pl06/tools/*`) was **not modified**.
- No state, pattern, density, cast, or visual subject was invented.
- Every produced artifact carries `INTERNAL_GENERATION_DRAFT`.
- No Bariah readiness is asserted for this unit.
- No PR is opened; artifacts live only on branch `cc/pl06-pilot`.
