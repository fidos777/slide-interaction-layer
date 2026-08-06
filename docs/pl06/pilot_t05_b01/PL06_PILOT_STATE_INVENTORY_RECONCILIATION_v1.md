# PL06 Pilot — State Inventory Reconciliation — `K5-PL06-T05-B01`

> **INTERNAL_GENERATION_DRAFT** — machine-authored engineering record. Not reviewed, not
> Bariah-approved. **No state is invented in this document.** Where the runtime state set is
> not computable with the current shared capability, it is recorded as such, not filled in.

> ⚠️ **SUPERSEDE / RECONCILE banner — status: `INTERNAL_GENERATION_DRAFT` ·
> `NOT_BARIAH_REVIEW_READY` · `NOT_INSTRUCTIONALLY_APPROVED`.** The body below has been
> **rewritten** to the accurate distinction — `AUTHORITY_STATUS: CONFIRMED` /
> `IMPLEMENTATION_STATUS: NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`. The core claim — no
> states invented — still holds. The original checkpoint wording (which implied a pending
> Bariah/pattern decision and an unfrozen set) remains auditable in parent commit `9c05cf2`;
> it is no longer active here. Two corrections were applied:
> (1) §4's "no STEP grammar exists" is wrong — a STEP grammar exists but is B03-bound, and the
> shared resolver forces all four T05-B01 groups to click-to-reveal (OBSERVED).
> (2) **Authority decisions are NOT pending**; the F3 treatment rules are already
> authority-named. Full corrected report: `PL06_PILOT_DEFECT_REPORT_v2.md`.

## 0. Purpose

The Lampiran Keadaan (3-panel) enumerates the unit's **runtime states** — one panel per state
on any screen that carries more than one state. This document reconciles what the committed
source establishes about that state set against what the Lampiran renderer would require. It
is the artifact that surfaces why generation halted.

## 1. What is known (source-derived, defensible)

The base learner-screen sequence is fixed by the committed provisional model
(`screen_sequence.sequence`, `runtime_state_estimate.base_states_floor = 10`). Each learner
screen contributes one BASE state:

| # | learner screen | screen kind | contributes |
|---:|---|---|---|
| 1 | S01 Topik entry | shell | 1 BASE |
| 2 | S02 Dialog | shell | 1 BASE |
| 3 | S0x Orientasi | shell | 1 BASE |
| 4 | G1: Project Quality Plan (PQP) | content | 1 BASE + **N₁ triggered (NOT_COMPUTABLE)** |
| 5 | G2: Jaminan Kualiti (QA) | content | 1 BASE + **N₂ triggered (NOT_COMPUTABLE)** |
| 6 | G3: Inspection and Testing for Quality Control | content | 1 BASE + **N₃ triggered (NOT_COMPUTABLE)** |
| 7 | G4: Penyata Kaedah Kerja (Method Statement) | content | 1 BASE + **N₄ triggered (NOT_COMPUTABLE)** |
| 8 | Rumusan | closing | 1 BASE (+ visual state NOT_COMPUTABLE) |
| 9 | Kuiz | assessment | 5 QUIZ_ITEM + 1 QUIZ_RESULT (key drafted, approved by nobody) |
| 10 | Tamat | closing | 1 BASE |

- **base_states_floor = 10** — one per learner screen. This is a *floor*, established.
- The four content groups G1–G4 are the interaction surface; the Lampiran panels live here.

## 2. What the current shared capability cannot compute (recorded, not invented)

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

| quantity | operative status | field |
|---|---|---|
| triggered states per content screen (N₁…N₄) | `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` | `runtime_state_estimate.triggered_states` |
| total runtime states | `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` | `runtime_state_estimate.total_runtime_states` |
| maximum total screens | `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` | `screen_sequence.arithmetic.maximum_total_screens` |
| primary treatment (per unit) | `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` — candidate "progressive process"; F3 rule present, per-unit classifier not built | `pattern_family.cls` |
| Rumusan visual → runtime state? | `NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` — per-unit classification not built | `state_model_implications` (k5_policy_apply) |

The triggered-state count is fixed by the authority-named F3 rules applied to the controlled
source; **authority decisions are CONFIRMED — none pending.** It is not produced because the
shared code cannot classify or extract it per unit. The parent implementation emits a stale
`"UNKNOWN_STILL_NOT_FROZEN"` token for these quantities; that token is a defect artefact of the
parent code, **not** the document status. The normative status is
`NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`.

## 3. Why the base states cannot simply be carried as the Lampiran set

The Lampiran Keadaan carries **every state on a screen with more than one state**
(`k5_calib_model_v1.py :: _panel_states_uncached`). A screen with only its BASE state
contributes **no** Lampiran panel. Therefore the Lampiran set is composed *entirely* of the
triggered states on G1–G4 (plus quiz items) — precisely the quantities that are
`NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY`. The known floor (10 BASE states) contributes
almost nothing to the Lampiran; the not-computed part *is* the Lampiran.

## 4. Why the triggered states are not computed by the shared grammar

T05-B01's committed primary treatment candidate is **"progressive process"** — the source
states two genuine sequences (the NCR workflow and the ITP inspection stages;
`pattern_family.reason`). A STEP state kind **exists** in the shared builder:

```
STATE_KINDS = ["BASE", "REVEAL", "STEP", "QUIZ_ITEM", "QUIZ_RESULT", "COMPLETION"]
```

(`k5_calib_model_v1.py:568`) — but its content is **B03-bound**: the only step sequence is
`subsoil_sequence()` over `SUBSOIL_STEP_ROWS` (B03 rows), and STEP is reached only through a
B03-only F4 override. For T05-B01, `overrides("K5-PL06-T05-B01") = {}` and the lane hardcodes
the F3 case to `LAYERED`, so all four groups resolve to click-to-reveal (OBSERVED). Producing
the Lampiran from this would force a choice between two forbidden moves:

1. **Force the content into click-to-reveal states** — misrepresents a source sequence as
   independent panels (a fabrication of interaction semantics), or
2. **Hand-author STEP states from B03's rows or invented rows** — inventing states.

Both violate the standing instruction "Do not invent states." The set is therefore
`NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY` until the per-unit F3 classifier and per-unit
sequence extraction exist (Lane G).

## 5. Reconciliation result

```
KNOWN_FLOOR              = 10 BASE states (source-derived)
QUIZ_STATES              = 5 QUIZ_ITEM + 1 QUIZ_RESULT (key drafted, unapproved)
LAMPIRAN_PANEL_STATES    = NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY  (triggered states on G1–G4)
TOTAL_RUNTIME_STATES     = NOT_COMPUTABLE_WITH_CURRENT_SHARED_CAPABILITY
AUTHORITY_STATUS         = CONFIRMED (no authority decision pending)
RECONCILIATION_STATUS    = HALTED_AT_LAMPIRAN_STATE_INVENTORY — no states invented
```

Missing shared capability is recorded in `PL06_PILOT_DEFECT_REPORT_v1.md`.
