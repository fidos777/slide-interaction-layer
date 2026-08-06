# PL06 Pilot — Defect Report — missing shared capability for non-B03 generation

> **INTERNAL_GENERATION_DRAFT** — machine-authored engineering record. Not reviewed, not
> Bariah-approved.

- **Unit under test:** `K5-PL06-T05-B01` (highest-layout-stress committed non-B03 unit)
- **Base commit:** `ebd6d81`
- **Attempt outcome:** `STOPPED_AT_LAMPIRAN_STATE_INVENTORY`
- **Constraint honoured:** shared generator code was not modified; no state was invented.

## Summary

Generic generation cannot produce a defensible Lampiran Keadaan state inventory for a
committed non-B03 unit at commit `ebd6d81`. Three distinct shared-capability gaps each
independently block it. Gaps D-1 and D-3 are code capabilities; D-2 is an authority input the
generator depends on. All three must be closed before this pilot can resume.

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

## D-2 — The per-unit pattern family is undecided (authority input pending)

**Severity:** BLOCKS_LAMPIRAN_STATE_INVENTORY

- `docs/pl06/batch1_extract/K5_PL06_T05_B01_PROVISIONAL_MODEL_v1.json` —
  `pattern_family.cls = "PENDING_BARIAH_PATTERN_DECISION"`; primary candidate "progressive
  process", secondary candidate "comparison"; note: *"The pattern package that would settle
  this is still with Bariah."* Pending doc: `K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2.docx`.
- `docs/pl06/tools/k5_policy_apply_v1.py:200–256` — for the calibration units the resolved
  `screen_pattern_plan.primary` is `pf.get("primary_candidate")` (an unratified *candidate*),
  and `maximum_total` and `state_model_implications.total_runtime_states` both resolve to
  `"UNKNOWN_STILL_NOT_FROZEN"`.
- `docs/pl06/tools/k5_pattern_policy_v1.py` — ruling **B2 (Kepadatan Lampiran Keadaan) status
  = TEST_REQUIRED**: *"NO density is approved … the same state set must be shown before any
  density is fixed."* A fixed state set is a precondition B2 does not yet have.

**Consequence:** the triggered-state set (the substance of the Lampiran) is undetermined.
Producing it would require inventing the pattern decision — forbidden.

**Missing capability:** ingestion of the Bariah pattern-decision package into
`k5_pattern_policy_v1` so that `screen_pattern_plan.primary` for `T05-B01` is a **decision**,
not a candidate, and `total_runtime_states` is frozen. This is an authority input, not code.

## D-3 — The shared state grammar implements click-to-reveal only

**Severity:** BLOCKS_LAMPIRAN_STATE_INVENTORY (independent of D-2)

- `docs/pl06/tools/k5_calib_model_v1.py:489` —
  `STATE_KINDS = ["BASE", "REVEAL", "QUIZ_ITEM", "QUIZ_RESULT", "COMPLETION"]`.
- `_states_uncached()` (`k5_calib_model_v1.py:528`) builds content-screen states purely from
  `sc["reveals"]` — i.e. the click-to-reveal grammar. There is no state kind for a
  sequential/stepped pattern (no STEP / PROGRESS / SEQUENCE).

**Why it bites T05-B01 specifically:** the unit's committed primary pattern is *progressive
process* over two genuine sequences (NCR workflow, ITP inspection stages). Even if D-2 were
closed with a "progressive process" decision, the shared builder has no grammar to emit those
states. The B03 calibration succeeded only because B03 resolved to the ratified click-to-reveal
default and the builder *deliberately declined* B03's unratified secondary pattern
(`k5_calib_model_v1.py:297` A4_COMPARISON — *"Promoting it is Bariah's call, not this
builder's"*).

**Missing capability:** a progressive-process (sequential-step) state grammar in the shared
state builder — new `STATE_KINDS`, ID shape, trigger and return-behaviour vocabulary, and
panel-field mapping — before any unit whose ratified pattern is "progressive process" can be
generated. Without it, generation would force sequential content into REVEAL states,
misrepresenting the source.

---

## Dependency and unblock order

```
D-1 (unit-parameterised generator)          — code; unblocks running the pipeline at all
D-2 (Bariah pattern decision ingested)      — authority; unblocks a *decided* pattern
D-3 (progressive-process state grammar)     — code; unblocks emitting the decided pattern
```

D-1 alone lets the pipeline *run* for T05-B01, but it would run into D-2/D-3 at the Lampiran.
All three are required for a defensible T05-B01 Lampiran Keadaan. No partial artifact
(storyboard, Lampiran, preview, structural/XML QA, overflow/placeholder scan) is emitted in
this pilot, because each depends on the state set that D-2 and D-3 leave undetermined.

## Non-goals / guardrails observed

- No shared generator file was modified.
- No state, pattern, density, cast, or visual subject was invented.
- No Bariah readiness is claimed for `T05-B01` or any unit.
