# SBAT-ADR-002 — MMD readiness pilot: three convergence samples on the M1 record

**Status:** Accepted
**Date:** 2026-06-27
**Owner:** Firdaus (technical custody)
**Type:** Architecture Decision Record — *not a PRD, not a system blueprint*
**Supersedes:** —
**Related:** [`SBAT-ADR-001`](SBAT-ADR-001.md) (SBAT architecture & placement); `sbat/m1-screen-c.html`; `sbat/mmd-readiness-pilot.md`

---

## What this document is (and is not)

This ADR records a small, bounded decision: to **pilot the M1 governance record against three real MMD
convergence cases** — a character swap, a quiz gap, and a visual-asset gap — by capturing each as a
committed-enum SBAT planning record. It exists so the next reviewer can see *why* these three slides were
encoded the way they were, and why one of them is deliberately **not** treated as a blocked asset.

It is **not** a schema change, a code change, or a roadmap. It adds no enums, no fields, and no validator.
It rides entirely on the M1 vocabulary already committed in `sbat/m1-screen-c.html` (ADR-001 Decision 6).
Anything beyond these three records is out of scope here.

Guiding principle, carried from ADR-001: *demand-pull over build-ahead.* These three samples are pulled by
three real convergence patterns the registers keep producing; nothing is generalized ahead of them.

---

## Background — three convergence patterns worth proving

The AMEND-K1 × Laila register work keeps surfacing the same three shapes of cross-register convergence.
Each maps cleanly to a committed `convergence_type` and to one M1 interaction pattern:

- **Character swap** — the on-screen presenter on a slide does not match the approved character bank.
  Static slide; the governance action is to swap the persona before lock. (`character-swap`, `P0`.)
- **Quiz gap** — a quiz screen is empty or placeholder; stem, options, correct-answer mark and feedback are
  not in the approved source. (`quiz-gap`, `P6`.)
- **Asset gap** — the storyboard *requires* a real photographic asset that has not yet been selected or
  produced. (`asset-gap`, `P11`.)

These are exactly the categories SBAT must carry without inventing new structure.

---

## Decision 1 — Encode the three pilot slides on the unchanged M1 record

**Decision.** Capture three planning records — `pl1t3-s2`, `pl3t1-s28`, `pl5t3-s4` — using only the M1
record shape and only the enum values committed in `sbat/m1-screen-c.html`. No schema, taxonomy, validator,
importer, parser, or UI is added or modified.

**Why.** The point of the pilot is to prove the *existing* M1 vocabulary already carries these convergence
cases end-to-end. Introducing new structure would defeat the test and re-open the overbuild risk ADR-001
closed.

**Consequence.** The three samples live under `sbat/samples/` as illustration records. They are anonymized;
no full CIDB content is stored. Richer, human-readable readiness language lives only in the companion
`sbat/mmd-readiness-pilot.md`, never inside the JSON.

---

## Decision 2 — The two confirmed blockers are `BLOCKED_PENDING_SB`

**Decision.** `pl1t3-s2` (`character-swap`, `P0`) and `pl3t1-s28` (`quiz-gap`, `P6`) take
`decision_gate: BLOCKED_PENDING_SB`.

**Why.** In both cases the gap is confirmed from the approved source file, but the *resolution* requires a
human-ratified input from SB Bariah — the correct presenter persona, and the ratified quiz items. Per
ADR-001 Decision 5, AI never closes such a finding by edit; it stays open, pending the source owner.

**Consequence.** Both records carry `provenance: confirmed-from-file` (the blocker itself is read from the
deck) and `source_status: needs-review` (the content that would clear it is not yet ratified).

---

## Decision 3 — The asset case is `REVIEW`, **not** `BLOCKED_PENDING_ASSET`

**Decision.** `pl5t3-s4` (`asset-gap`, `P11`) takes `decision_gate: REVIEW` with
`provenance: confirmed-from-file`. It does **not** take `BLOCKED_PENDING_ASSET`.

**Why.** The source proves that real images are *required / requested* — that is a confirmed requirement read
from the storyboard. It does **not** prove that an *approved* real image is confirmed missing. `BLOCKED_PENDING_ASSET`
would over-claim a confirmed absence we do not have; `REVIEW` correctly states that available imagery still
has to be looked at. The provenance is `confirmed-from-file` because the requirement (not the absence) is what
the file confirms.

**Consequence.** The asset case moves through review rather than sitting behind a blocker that asserts more than
the evidence supports. This distinction — *requirement confirmed* vs *absence confirmed* — is the substantive
governance call this ADR exists to record.

---

## Non-Goals (explicitly out of scope, now)

- **No schema / taxonomy / validator change.** The M1 enums are used as-is; none are added or edited.
- **No code, importer, parser, batch, CSV/XLSX loader, or multi-slide UI.** The pilot is three static records
  plus two docs.
- **No change to `sbat/m1-screen-c.html`** or to any CIDB repo file.
- **No richer readiness labels inside JSON.** Labels beyond the committed enums appear only in prose, in
  `sbat/mmd-readiness-pilot.md`.
- **No tag, release, or push.** This ADR records a decision; shipping is a separate, human-gated step.

---

## Decision summary

| # | Decision | One-line |
|---|----------|----------|
| 1 | Encode on M1 | Three samples on the unchanged M1 record, committed enums only |
| 2 | Confirmed blockers | `character-swap` and `quiz-gap` → `BLOCKED_PENDING_SB` |
| 3 | Asset case | `asset-gap` → `REVIEW` (requirement confirmed, not absence) — never `BLOCKED_PENDING_ASSET` |

**Verdict:** `Prove the three convergence shapes on the existing M1 vocabulary; let the asset case stay in REVIEW until imagery is actually examined.`
