# PL06 Pilot — Defect Report — missing shared capability for non-B03 generation

> **INTERNAL_GENERATION_DRAFT** — machine-authored engineering record. Not reviewed, not
> Bariah-approved.

> ⚠️ **SUPERSEDED_BY `PL06_PILOT_DEFECT_REPORT_v2.md` — status: `INTERNAL_GENERATION_DRAFT` ·
> `NOT_BARIAH_REVIEW_READY` · `NOT_INSTRUCTIONALLY_APPROVED`.** The body below has been
> **rewritten** to the accurate distinction — `AUTHORITY_STATUS: CONFIRMED` /
> `IMPLEMENTATION_STATUS: NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`. The original
> checkpoint wording (which implied a pending Bariah/pattern decision and an unfrozen state
> set) remains auditable in parent commit `9c05cf2`; it is no longer active here. Two
> corrections were applied:
> (1) **D-3** — the shared generator *does* have a STEP grammar (`STATE_KINDS` includes `STEP`
> at `k5_calib_model_v1.py:568`); the real defect is that STEP is B03-bound (B03-only F4
> override + `subsoil_sequence()`), so non-B03 units are forced to click-to-reveal.
> (2) **D-2** — **authority decisions are NOT pending**; the F3 treatment rules are already
> authority-named in `pl06_authority_v1.treatment_rules()`. The state set is
> `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`, not an authority-pending input. The blocked
> *outcome* recorded here still holds. Full corrected report: `PL06_PILOT_DEFECT_REPORT_v2.md`.

- **Unit under test:** `K5-PL06-T05-B01` (highest-layout-stress committed non-B03 unit)
- **Base commit:** `ebd6d81`
- **Attempt outcome:** `STOPPED_AT_LAMPIRAN_STATE_INVENTORY`
- **Constraint honoured:** shared generator code was not modified; no state was invented.

## Summary

Generic generation cannot produce a defensible Lampiran Keadaan state inventory for a
committed non-B03 unit at commit `ebd6d81`.

```
AUTHORITY_STATUS:       CONFIRMED
IMPLEMENTATION_STATUS:  NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY
```

The block is entirely a shared-implementation gap, not an authority decision. All three
defects (D-1, D-2, D-3) are shared-capability gaps and must be closed before this pilot can
resume.

---

## D-1 — The calibration generator is single-unit hardcoded (no unit parameter)

**Severity:** BLOCKS_ALL_NON_B03_GENERATION

- `docs/pl06/tools/k5_calib_model_v1.py:51` — `UNIT_ID = "K5-PL06-T03-B03"` is a module
  constant. There is no `argparse`, no `sys.argv`, no function parameter for unit selection.
- `docs/pl06/tools/k5_calib_build_v1.py` builds `M.UNIT_ID` throughout (lines 179, 246, 279,
  364, 452, 477, 612, 614, 714); the storyboard and both Lampiran filenames are B03 literals
  (`k5_calib_model_v1.py:56–57`).
- `_policy_unit()` (`k5_calib_model_v1.py:142`) selects the policy record by the hardcoded
  `UNIT_ID`.

**Consequence:** emitting a storyboard or Lampiran for `T05-B01` requires editing the shared
generator — forbidden by the pilot brief ("Do not modify shared generator code").

**Missing capability:** a unit-parameterised entry point — `k5_calib_model_v1` /
`k5_calib_build_v1` must accept a `unit_id` (CLI arg or function parameter) and resolve the
committed unit model, the policy record, and the output filenames from it, so a non-B03 unit
can be projected without editing shared code.

## D-2 — Per-unit treatment/state set is NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY

**Severity:** BLOCKS_LAMPIRAN_STATE_INVENTORY

```
AUTHORITY_STATUS:       CONFIRMED
IMPLEMENTATION_STATUS:  NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY
BLOCKERS:
  - unit-parameterised generator unavailable
  - unit-specific source binding unavailable
  - shared resolve_for_group implementation incomplete
  - per-unit state-inventory extraction unavailable
  - required source binary unavailable
```

- `AUTHORITY_STATUS: CONFIRMED` — the F3 treatment rules (`SEQUENTIAL_PROCESS`,
  `EXPLICIT_SYMMETRIC_COMPARISON`, `LAYERED_NON_PROCESS_NON_COMPARISON`, `OTHERWISE`) are
  authority-named and present in `pl06_authority_v1.treatment_rules()`. No Bariah decision is
  outstanding for this unit. The per-unit treatment/state set is fixed by those rules applied
  to the controlled source.
- `IMPLEMENTATION_STATUS: NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` — the shared code
  cannot classify or extract that set per unit. `k5_policy_apply_v1.py:200–256` fills
  `screen_pattern_plan.primary` from `pf.get("primary_candidate")` and emits `maximum_total` /
  `state_model_implications.total_runtime_states` = `"UNKNOWN_STILL_NOT_FROZEN"`.
  **Defect note:** `"UNKNOWN_STILL_NOT_FROZEN"` is a stale status token the parent
  implementation emits when it cannot compute the set per unit; it is **not** the document
  status. The normative status is `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`.
- The provisional model's `pattern_family.cls` label and the package name it cites are not
  operative; the gate is shared capability, not an authority decision.

**Consequence:** the triggered-state set (the substance of the Lampiran) is not computed here.
Producing it would require inventing groups, states, or mappings — forbidden.

**Missing capability:** the declared-but-unbuilt per-unit F3 classifier
(`resolve_for_group(unit_id, screen_name, controlled_group_evidence)`) plus per-unit
state-inventory extraction, so the set is computed from the existing authority rules. This is
shared code (Lane G), not an authority input.

## D-3 — The shared state grammar implements click-to-reveal only

**Severity:** BLOCKS_LAMPIRAN_STATE_INVENTORY (independent of D-2)

- `docs/pl06/tools/k5_calib_model_v1.py:489` —
  `STATE_KINDS = ["BASE", "REVEAL", "QUIZ_ITEM", "QUIZ_RESULT", "COMPLETION"]`.
- `_states_uncached()` (`k5_calib_model_v1.py:528`) builds content-screen states purely from
  `sc["reveals"]` — i.e. the click-to-reveal grammar. There is no state kind for a
  sequential/stepped pattern (no STEP / PROGRESS / SEQUENCE).

**Why it bites T05-B01 specifically:** the unit's committed primary pattern candidate is
*progressive process* over two genuine sequences (NCR workflow, ITP inspection stages).
Independently of D-2, the shared builder cannot emit those per unit — the STEP content is
B03-bound (corrected detail in v2 §D-3). B03 generates only because its treatments come from
B03-specific F4 overrides in the shared code; `overrides("K5-PL06-T05-B01")` is empty, so
every T05-B01 group is forced to click-to-reveal.

**Missing capability:** per-unit sequence emission in the shared state builder — STEP states
built from the unit's own rows, not B03's `subsoil_sequence()` — so a non-B03 unit's sequences
can be emitted. Without it, generation would force sequential content into click-to-reveal,
misrepresenting the source.

---

## Dependency and unblock order

```
D-1 (unit-parameterised generator)          — code; lets the pipeline run for a non-B03 unit
D-2 (per-unit F3 classifier + extraction)   — code; computes the treatment/state set from the
                                              existing authority rules (no authority input)
D-3 (per-unit sequence emission)            — code; emits non-B03 sequences from their own rows
```

D-1 alone lets the pipeline *run* for T05-B01, but it would run into D-2/D-3 at the Lampiran.
All three are shared-code gaps required for a defensible T05-B01 Lampiran Keadaan. No partial
artifact (storyboard, Lampiran, preview, structural/XML QA, overflow/placeholder scan) is
emitted in this pilot, because each depends on the state set that is
`NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`.

## Non-goals / guardrails observed

- No shared generator file was modified.
- No state, pattern, density, cast, or visual subject was invented.
- No Bariah readiness is claimed for `T05-B01` or any unit.
