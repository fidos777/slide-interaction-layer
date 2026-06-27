<!-- Placed verbatim from uploaded SBAT-ADR-001.md on 2026-06-27. Accepted; source of truth for SBAT Phase 1. -->

# SBAT-ADR-001 — SBAT Architecture & Placement

**Status:** Accepted
**Date:** 2026-06-27
**Owner:** Firdaus (technical custody)
**Type:** Architecture Decision Record — *not a PRD, not a system blueprint*
**Supersedes:** —
**Related:** Cycle 7 / Courseware.my deck series; SBAT UX Proposal — Screen C / M1

---

## What this document is (and is not)

This ADR records **decisions already made** about where SBAT lives and what role it plays. It exists so these questions stop being relitigated, not to specify the system to build.

It is **not** a product spec, a roadmap, or a description of the future app. Anything not yet decided is left out on purpose. Where a tempting generalization exists, it is named in **Non-Goals** and explicitly deferred.

Guiding principle, applied to this document itself: *demand-pull over build-ahead.* Prove one slide (M1) first; let system design emerge from real need. A document that designs the whole system ahead of M1 would be the same overbuild error in Markdown — so this one deliberately stops at what is decided.

---

## The mental model (shared reference)

```
   slide-interaction-layer   =  the pattern factory   (reusable engine)
   SBAT                      =  the factory control panel (authoring + governance)
   cidb-k1pl1t1-prototype    =  the first customer order  (CIDB delivery + test target)
```

Equivalently, in pipeline terms:

```
   Repo = the machine that builds courseware.
   SBAT = the review desk before material enters the machine.
```

Everything below follows from keeping these three things separate.

---

## Decision 1 — SBAT belongs in `slide-interaction-layer`, not `cidb-k1pl1t1-prototype`

**Decision.** SBAT is developed inside `slide-interaction-layer`, the home of reusable patterns, taxonomy, schema, and validators. It is not developed inside `cidb-k1pl1t1-prototype`.

**Why.** `cidb-k1pl1t1-prototype` is saturated with one customer and one module (CIDB, K1PL1T1, waterproofing, specific assets, specific SCORM package). Building SBAT there would bind it to a single customer and cause **architecture drift** — SBAT would become "a tool for K1PL1T1" instead of "a tool for authoring courseware." The things SBAT must manage (interaction patterns, slide taxonomy, JSON schema, validators, source-backed flags, patch preview) are not CIDB-specific and belong with the reusable layer.

**Consequence.** SBAT work happens in `slide-interaction-layer`. CIDB is one customer output, not SBAT's home.

---

## Decision 2 — `cidb-k1pl1t1-prototype` remains a CIDB delivery / test target

**Decision.** `cidb-k1pl1t1-prototype` stays a delivery and proof repo for CIDB Cycle 7: the place where SBAT output is proven to compile, render, build to SCORM, and pass audit. It is a downstream test bed, not the product core.

**Why.** The repo is already an audit-grade production ledger — every change carries finding → instruction → diff → verification → commit. That value is delivery-specific and should stay that way. Making it the product core would re-introduce the drift Decision 1 avoids.

**Consequence.** The repo answers four questions for any SBAT output: *Does it compile? Does the JSON render? Does SCORM build? Does the audit pass?* It is not touched except for Cycle 7 delivery fixes.

---

## Decision 3 — SBAT's role is **pre-commit authoring governor**

**Decision.** SBAT sits *before* the repo as the authoring and validation layer. It is not a replacement for the repo and does not build or render runtime.

**Why.** The valuable problem is not coding — it is **traceability**: confirming that every text, quiz option, interaction, asset, and slide scope came from an approved source (SB Bariah / ID-approved) rather than being session-fabricated. That governance belongs in a layer that runs before material reaches the build machine.

**Target pipeline.**

```
   Storyboard evidence
        ↓
   SBAT extracts slide intent
        ↓
   SBAT maps to interaction pattern
        ↓
   SBAT validates source-backed content
        ↓
   SBAT generates repo-ready JSON patch
        ↓
   human approves
        ↓
   repo commit
```

**Consequence.** SBAT = decision, evidence, pattern, and QA layer. Repo = runtime / build layer. Clean separation; neither absorbs the other.

---

## Decision 4 — Repo remains the build/runtime layer and audit-grade production ledger

**Decision.** The repo keeps two jobs: (a) render content JSON into the running React/Vite player, and (b) hold the traceable commit history that lets any change be defended under audit.

**Why.** The repo has already proven it can carry interaction logic as canonical, reusable components (e.g. the visited-gate menu pattern: stateful buttons, popup detail, visited tracking, completion gate, next-unlock). And it has proven it can answer "why did Q2 change?" with a commit, not a verbal account. Both jobs are real and worth preserving as-is.

**Consequence.** SBAT does not rebuild runtime. It generates output the repo can validate. Future modules reuse the repo's interaction components and swap only content (slides, items, popup blocks, quiz options, assets, unlock rules).

---

## Decision 5 — The governed remediation loop is the operating model (proven, not theoretical)

**Decision.** The adopted operating model is the governed remediation loop:

```
   audit finding
        ↓
   source check
        ↓
   limited edit
        ↓
   diff
        ↓
   validation
        ↓
   commit
        ↓
   unresolved items stay open
```

**Why — it is already proven by two real cases:**

- **Q2 Polystyrene fix.** Q2's distractor read "Bitumen Sheet Waterproofing," but SB Bariah's source used "Polystyrene Waterproofing." Bitumen is a *valid* waterproofing material, so leaving it risked an AI-plausible distractor passing as official training fact. The fix changed only `q2_d` text to the source-backed value; `is_correct` stayed false. Source beat plausibility — exactly the check SBAT must enforce.
- **`demo_scope` 6-vs-7 correction.** `demo_scope` declared 6 slides while `slide_navigation_order` carried 7 (including `s13`). Trivial as code, serious as governance. Corrected to a consistent count. This is the `SCOPE_CONSISTENCY_CHECK` SBAT should run: declared count vs implemented IDs vs excluded IDs vs storyboard total.

A third pattern from the same work — **report-only when no source exists** (Q5's two suspected-fabricated distractors were *reported, not edited*, because no SB-sourced replacement was available) — confirms the doctrine: **AI accelerates; humans decide.**

**Consequence.** SBAT productizes this loop; it does not replace the repo or the human. Unresolved items stay open rather than being silently closed by edit.

---

## Decision 6 — Screen C / M1 carries only the six MVP governance fields

**Decision.** The first build (Screen C / M1) is scoped to six governance fields and nothing more. These are the fields the remediation cases above proved are necessary.

1. **Slide implementation status** — storyboard exists? implemented in repo? in navigation? declared in `demo_scope`?
2. **Interaction pattern** — static / video / visited-gate menu / popup modal / subtopic detail / drag-drop / quiz single / quiz multi / end screen.
3. **Source-backed content flag** — SB-sourced / ID-approved / AI-suggested / repo-existing / needs-review.
4. **Quiz option governance** — `option_id`, text, `is_correct`, source, risk (valid distractor / fabricated / misleading / pending).
5. **Repo patch preview** — show the diff (`- old` / `+ new`); never edit silently.
6. **Human decision gate** — REPORT_ONLY / READY_TO_PATCH / PATCHED_NOT_COMMITTED / COMMITTED / BLOCKED_PENDING_SB / BLOCKED_PENDING_ASSET.

**Why.** Each field is demand-pulled by a real finding, not invented for completeness. M1 proves the screen carries them end-to-end for one slide before anything scales.

**Consequence.** Screen C / M1 is a thin authoring surface over existing patterns. It is not a full editor, dashboard, or app.

---

## Non-Goals (explicitly out of scope, now)

These are deferred on purpose. Each is a plausible future need; none is decided, and building any of them now would be premature.

- **No full LMS.** SBAT is a pre-commit governor, not a learning-management system.
- **No Courseware.my commercial wrapper now.** The commercial layer (landing, dashboard, offers) waits until delivery proof exists; it is not built alongside M1.
- **No generalized multi-client platform now.** SBAT is proven against one customer (CIDB) first. Multi-client generalization is a Phase-later question, not an M1 one.
- **No automated final ID/QA decision.** AI suggests, classifies, and drafts patches; humans (Bariah / Laila / ID) ratify facts, quiz content, and interactions. The final decision is never automated.
- **No moving CIDB-specific content into `slide-interaction-layer`.** The reusable layer holds patterns, schema, and validators — not customer content, assets, or SCORM specifics. Content stays in the CIDB repo.

---

## Staging (recorded for direction only — not a commitment to build ahead)

```
   Phase 1   slide-interaction-layer gains SBAT authoring/validator docs + schema
   Phase 2   connect SBAT output to cidb-k1pl1t1-prototype JSON
   Phase 3   extract common renderer / patterns only if real need appears
   Phase 4   commercialize as a Courseware.my authoring workflow
```

Only Phase 1 is in motion. Everything from Phase 2 onward is listed for direction, not authorized for build. `cidb-k1pl1t1-prototype` is not touched except for Cycle 7 delivery fixes.

---

## Decision summary

| # | Decision | One-line |
|---|----------|----------|
| 1 | SBAT placement | Develop in `slide-interaction-layer`, not the CIDB repo |
| 2 | CIDB repo role | Stays a CIDB delivery / SCORM / audit test target |
| 3 | SBAT role | Pre-commit authoring governor, not a repo replacement |
| 4 | Repo role | Build/runtime layer + audit-grade production ledger |
| 5 | Operating model | Governed remediation loop — proven by Q2 + demo_scope |
| 6 | M1 scope | Screen C carries only the six governance fields |

**Verdict:** `SBAT core → slide-interaction-layer · CIDB implementation → cidb-k1pl1t1-prototype · commercial packaging → courseware.my later.`
