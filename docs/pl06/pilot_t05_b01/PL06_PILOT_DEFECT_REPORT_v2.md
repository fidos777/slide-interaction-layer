# PL06 Pilot — Defect Report v2 — non-B03 generation blocked (empirically verified)

> INTERNAL_GENERATION_DRAFT
> NOT_BARIAH_REVIEW_READY
> NOT_INSTRUCTIONALLY_APPROVED
>
> Machine-authored engineering record. Not reviewed, not Bariah-approved. No Bariah
> readiness is claimed. No state is invented in this document.

**Supersedes** `PL06_PILOT_DEFECT_REPORT_v1.md`. v1 is preserved as prior Lane P evidence.
This v2 corrects v1's defect **D-3** (which claimed the generator has no STEP grammar — it
does) and adds empirically-OBSERVED evidence and a new defect **D-4**. See §5 Reconciliation.

## Lane identity (OBSERVED)

| field | value |
|---|---|
| worktree | `/Users/firdausismail/Projects/SBAT/pl06-cc-lanes/pilot-isolated` |
| branch | `cc/pl06-pilot-isolated` |
| HEAD / pilot checkpoint | `9c05cf2b090f368c0839a2703159106bd1409ca3` |
| base (ancestor) | `ebd6d81cf9c3b9e842d01d0b571ee16e32b5fb18` |
| unit under test | `K5-PL06-T05-B01` — Pengurusan Kualiti Projek |

## Verdict

The existing shared generator **cannot emit a defensible T05-B01 Storyboard or Lampiran
Keadaan without a shared-code change.** Per the pilot brief the lane stops here, records the
missing capability, does not patch shared code, and does not invent states. No Storyboard,
Lampiran, or preview artifact is produced.

Every claim below is sourced to command output at report time. Legend: **OBSERVED** = printed
by a command this session; **INFERRED** = read from source that did not execute here;
**TARGET** = a capability the shared code itself declares as not-yet-built.

---

## D-1 — Generator identity is hardcoded to B03 (OBSERVED)

- `k5_calib_model_v1.py:91` — `UNIT_ID = "K5-PL06-T03-B03"`; `:92` `SHORT = "T03B03"`.
- No CLI/unit parameter: `grep -cE "argparse|add_argument" k5_calib_model_v1.py` → **0**.
- Build emits B03-literal filenames: `k5_calib_build_v1.py:22-24`
  `K5PL06T03B03_STORYBOARD_KALIBRASI_DRAF_v0_1.pptx`, `…_LAMPIRAN_KEADAAN_…_{2,3}panel.pptx`.
- Runtime confirmation (OBSERVED): probe printed `UNIT_ID = K5-PL06-T03-B03`.

**Consequence:** producing a T05-B01 deck requires editing the shared generator — forbidden.

## D-2 — T05-B01 treatment/state set is NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY (OBSERVED)

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

**Authority decisions are NOT pending on this unit.** The F3 treatment rules
(`SEQUENTIAL_PROCESS`, `EXPLICIT_SYMMETRIC_COMPARISON`, `LAYERED_NON_PROCESS_NON_COMPARISON`,
`OTHERWISE`) are authority-named and already present in `pl06_authority_v1.treatment_rules()`.
No further Bariah decision is being waited on. The per-unit treatment/state set is determined
by those rules applied to the controlled source — it is simply **not computable with the
current shared capability**, which cannot classify or extract it per unit.

- OBSERVED — F4 authority overrides are B03-only:
  - `overrides("K5-PL06-T03-B03") = {'subsoildrainage': 'Langkah demi langkah', 'swalenaturaldrain': 'Click-to-Reveal'}`
  - `overrides("K5-PL06-T05-B01") = {}`
- OBSERVED — the calibration lane supplies no per-unit F3 classification: it calls
  `TR.resolve(UNIT_ID, group, TR.LAYERED, …)` with the F3 case hardcoded to `LAYERED`, forcing
  every T05-B01 group to click-to-reveal (§D-3). The per-unit classifier the resolver header
  declares — `resolve_for_group(unit_id, screen_name, controlled_group_evidence)` — is not built.
- OBSERVED — `k5_policy_apply_v1.py:210,256` emit `maximum_total` and `total_runtime_states`
  = `"UNKNOWN_STILL_NOT_FROZEN"`. **Defect note:** that literal is a stale status token the
  parent implementation emits when it cannot compute the set per unit; it is **not** the
  document status. The normative status is `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` —
  not an authority hold.

Note — the provisional model carries its own `pattern_family.cls` authority-decision label and
names a package `K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2.docx`. Per lane governance that
framing is **superseded**: the operative gate is shared capability, not an authority decision.

**Consequence:** the triggered/total runtime-state set is
`NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`; it is not produced here, and no group, state,
or mapping is invented to fill it.

## D-3 — STEP grammar EXISTS but is B03-bound; non-B03 units are silently forced to click-to-reveal (OBSERVED) — CORRECTS v1

v1 wrongly stated the generator has no STEP/sequential grammar. It does. The real defect is
narrower and empirically demonstrated:

- OBSERVED — `STATE_KINDS = ["BASE", "REVEAL", "STEP", "QUIZ_ITEM", "QUIZ_RESULT",
  "COMPLETION"]` (`k5_calib_model_v1.py:568`). A STEP state kind is present (reused from the
  approved T04 STEP contract).
- **STEP content is hardwired to B03.** `SUBSOIL_STEP_ROWS = ["T03B03-ROW-024", …]`
  (`:57`); the screen builder uses `seq = subsoil_sequence() if
  TR.is_step_by_step(res["treatment"]) else None` (`:493`) — the *only* step sequence
  available is B03's sub-soil rows. There is no per-unit sequence extraction.
- **STEP is reachable only via an F4 override, and only B03 has one.** The calibration lane
  calls `res = TR.resolve(UNIT_ID, g["covers"], TR.LAYERED, …)` (`:491`), hardcoding the F3
  fallback case to `LAYERED` (click-to-reveal). A group becomes stepped only when
  `overrides(unit_id)` names it — and `k5_treatment_resolver_v1.py:110` returns `{}` for any
  `unit_id != "K5-PL06-T03-B03"` (`# TODO(0b): move to pl06_authority_v1`).
- OBSERVED — driving the shared resolver on T05-B01's four real groups:

  ```
  Project Quality Plan (PQP)              -> Click-to-Reveal  basis=F3_RULE_APPLIED_TO_CONTROLLED_ROWS  step=False
  Jaminan Kualiti (QA)…                    -> Click-to-Reveal  basis=F3_RULE_APPLIED_TO_CONTROLLED_ROWS  step=False
  Inspection and Testing for Quality Ctrl -> Click-to-Reveal  basis=F3_RULE_APPLIED_TO_CONTROLLED_ROWS  step=False
  Penyata Kaedah Kerja (Method Statement) -> Click-to-Reveal  basis=F3_RULE_APPLIED_TO_CONTROLLED_ROWS  step=False
  ```

**Consequence:** the shared generator would emit **all four** T05-B01 groups as
click-to-reveal, misrepresenting the unit's genuinely sequential content (NCR workflow, ITP
inspection stages) — the exact defect class the resolver's own header names ("leaving
Sub-soil Drainage on click-to-reveal against F4(a)"). Producing a *correct* T05-B01 state
inventory would require either inventing an F4 override or authoring per-unit sequences —
both forbidden.

- TARGET (declared by shared code, not built): `k5_treatment_resolver_v1.py:11` — "INCOMPLETE
  AS OF 2026-08-05 (f082dd2)"; the intended API is `resolve_for_group(unit_id, screen_name,
  controlled_group_evidence)` with per-unit F3 classification **inside** the module and no
  caller-supplied `f3_case`.

## D-4 — Frozen source binary unavailable in this worktree; no unit is generable end-to-end (OBSERVED)

- OBSERVED — driving the B03 baseline (`M.screens()`) raised
  `pl06_extract_v1.ExtractionError: SOURCE_BINARY_NOT_AVAILABLE`
  (`pl06_extract_v1.py:135`, `_open_module`). The same error blocked
  `k5_policy_apply_v1.calibration_units()`.
- The module DOCX is held outside the repository by identity (SHA-256 `5a9142cdfa1a8090…`,
  16,832,861 bytes; recorded in the freeze manifest).

**Consequence:** even B03 — the generator's own bound unit — cannot be built in this
environment. Storyboard/Lampiran/preview emission is blocked at extraction, independent of
D-1–D-3. This is an environment/custody gap, not a design defect.

---

## Minimum capability required to unblock (not performed here)

1. **D-1** unit-parameterise `k5_calib_model_v1` / `k5_calib_build_v1` (accept `unit_id`;
   resolve model, policy, filenames from it).
2. **D-3** land the declared resolver refactor: per-unit F3 evidence classification inside
   `k5_treatment_resolver_v1`, per-unit F4 overrides via `pl06_authority_v1`, and per-unit
   sequence extraction (not `subsoil_sequence()`), so a non-B03 sequential group can emit STEP
   states from its own rows.
3. **D-2** build the declared per-unit F3 evidence classifier (`resolve_for_group(...)`) so
   T05-B01's treatment and `total_runtime_states` are computed from the existing authority
   rules — no new authority decision is required.
4. **D-4** make the frozen source binary available to the extract layer in the lane.

All four are shared-code / custody changes (Lane G) outside this lane's write scope.

## 5. Reconciliation with v1 (prior Lane P evidence)

| v1 claim | v2 status |
|---|---|
| D-3: "state grammar implements click-to-reveal only; no STEP kind" (`k5_calib_model_v1.py:489`) | **CORRECTED.** STEP kind exists at `:568`. v1's cited line/content did not match the committed code at `ebd6d81`. Real defect is D-3 above (STEP is B03-bound). |
| D-1 generator hardcoded to B03 | **CONFIRMED** (OBSERVED `UNIT_ID`, 0 argparse). |
| D-2 framed as "authority input pending" | **REFRAMED.** Authority decisions are NOT pending; the F3 rules are already authority-named. The set is `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` (OBSERVED empty overrides; hardcoded `TR.LAYERED`). |
| Outcome: generation blocked without shared-code change | **CONFIRMED**, and strengthened with runtime evidence + new D-4. |
| Selection of T05-B01 as highest-layout-stress | **UNCHANGED** — see `PL06_PILOT_SELECTION_v1.md`. |

The selection and manifest are unchanged. The v1 defect report and the state-inventory
reconciliation have had their bodies **rewritten** to the accurate distinction
(`AUTHORITY_STATUS: CONFIRMED` / `IMPLEMENTATION_STATUS:
NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`); their original checkpoint wording remains
auditable in parent commit `9c05cf2`. The reconciliation's core claim — the triggered-state
set is `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`, no states invented — still holds.

## Guardrails observed

- Shared generator/authority/resolver/packet-model/unit-analysis/golden-map code **not
  modified** (verified: `git status` clean after the read-only probe).
- No state, pattern, density, cast, or visual subject invented.
- B03 used only as a renderer/geometry/grammar reference, never as a treatment,
  state-correctness or readiness oracle.
- Writes confined to `docs/pl06/pilot_t05_b01/`.

## Appendix — OBSERVED probe method

Read-only, no files written (`git status` clean afterward). The probe added the tools dirs to
`sys.path` and called shared public APIs: `k5_calib_model_v1` (identity, `STATE_KINDS`,
`screens()`), `k5_treatment_resolver_v1.overrides()` / `.resolve()`, and
`k5_policy_apply_v1.calibration_units()`. No shared file was edited; `UNIT_ID` was not
monkeypatched (the resolver evidence uses its public `resolve(unit_id, …)` signature).
