# SBAT validator notes (planning — no code)

> **Notes, not code.** No validator script is created in Phase 1. This records only the checks the
> ADR explicitly demands (Decision 5), each demand-pulled by a real finding. No speculative
> validators. This is independent of `ontology/validate.py`, which is **not** touched.

The governed remediation loop these checks serve:
```
audit finding → source check → limited edit → diff → validation → commit → unresolved items stay open
```

## Check 1 — SCOPE_CONSISTENCY_CHECK
**Demand:** the `demo_scope` 6-vs-7 finding (declared count disagreed with the implemented IDs).
**What it compares (per module):** declared scope count · implemented slide IDs · explicitly excluded
IDs · storyboard total. These four must reconcile.
**Result:** consistent → pass; any mismatch → a finding routed to the human decision gate
(`BLOCKED_PENDING_*` or `READY_TO_PATCH`). Trivial as code, serious as governance.

## Check 2 — Source-backed content / quiz-option governance
**Demand:** the Q2 Polystyrene finding (a plausible distractor that wasn't the source-backed value).
**What it checks:** every content unit and every quiz option carries a `source` (field 3 / 4); a unit
flagged `AI-suggested` or `needs-review`, or an option with `risk` ∈ { fabricated · misleading }, may
not be committed as fact without a human-ratified source.
**Result:** source present → may proceed to patch preview; missing/unverifiable → finding stays open.

## Doctrine — report-only when no source exists
**Demand:** Q5's two suspected-fabricated distractors were **reported, not edited**, because no
SB-sourced replacement existed.
**Rule:** when a fix cannot be source-backed, the validator's output is `REPORT_ONLY` — the item stays
open; it is never auto-edited or silently closed. *AI accelerates; humans decide.*

## Explicitly out of scope (now)
No code/CLI · no JSON-Schema enforcement · no rendering/build checks (those remain the downstream
repo's job: compiles? JSON renders? SCORM builds? audit passes?) · no validators beyond the two
above. Anything else is a future-phase question, not an M1 one.
