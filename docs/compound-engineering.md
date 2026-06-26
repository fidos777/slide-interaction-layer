# Compound Engineering — operating model

How this repository is built so that **each change makes the next one easier**. Compound
engineering treats improvements as deposits that accrue: every loop leaves behind reusable assets
(specs, scripts, decision records, audit checks) rather than one-off work. This document is the
operating model; it changes no code.

## The principle

> Optimize for the *slope*, not the *point*. A slightly slower change that leaves a reusable artifact
> beats a fast change that leaves nothing behind.

Concretely, in this repo every loop tends to produce: a small scoped commit, a verification it
passed, a push script (so shipping is repeatable), and — when a real decision was made — an ADR.
Over time these compound: the taxonomy, the gating runtime, the ontology, the e-learning extension,
and the maintainer loop all build on each other without rewrites.

## The CORD Method

The repeatable cycle the maintainer runs (see `../MAINTAINER.md`):

1. **Classify** — name what the work *is* before acting (which area, which element/pattern, what kind
   of change). Naming first prevents random improvements.
2. **Operationalize** — make the smallest safe change that delivers it, with a verification step and,
   if shipping, a repeatable push script.
3. **Reuse** — prefer existing patterns, components, scripts, and conventions; extend rather than
   duplicate. New capability is additive and opt-in so nothing it touches has to change.
4. **Document** — record what changed and *why* (CHANGELOG entry; ADR for real decisions; README/
   SKILL updates) so the next agent or human inherits the context.

CORD is the "how"; the `MAINTAINER.md` loop (PLAN → IMPLEMENT → VERIFY → CRITIQUE → IMPROVE →
COMMIT → RELEASE) is the "when". They run together: classify in PLAN, operationalize in
IMPLEMENT/VERIFY, reuse throughout, document before COMMIT/RELEASE.

## Compounding assets in this repo

| Asset | Why it compounds |
| ----- | ---------------- |
| Taxonomy `P0`–`P8` | a stable vocabulary every later layer references |
| Gating runtime (`gating/`) | opt-in, reads existing signals — added zero cost to existing decks |
| Element Ontology (`ontology/`) | classifies content once; improves every pattern choice |
| Push scripts (`push-*.sh`) | shipping becomes a one-command, guarded, repeatable step |
| Decision records (`decisions/`) | decisions are remembered, not relitigated |
| Governance audit checks | quality is enforced by a checklist, not by memory |

## Decision records (ADRs)

Architecture Decision Records capture a decision, its context, and its consequences so future work
doesn't repeat the debate. They live in [`../decisions/`](../decisions/):

- [ADR-0001 — Use the P0–P8 interaction taxonomy](../decisions/ADR-0001-use-p0-p8-taxonomy.md)
- [ADR-0002 — Add the completion-gating runtime](../decisions/ADR-0002-add-completion-gating-runtime.md)
- [ADR-0003 — Add the Element Ontology layer](../decisions/ADR-0003-add-element-ontology.md)
- [ADR-0004 — Keep the ontology recommended, not required](../decisions/ADR-0004-keep-ontology-recommended-not-required.md)
- [ADR-0005 — Defer the ontology.json sidecar](../decisions/ADR-0005-defer-ontology-json-sidecar.md)

New decisions get the next number; superseded ones are marked `Superseded by ADR-NNNN` rather than
deleted.

## Definition of done (compound)

A loop is compound-complete when it leaves: a scoped commit, a passed verification, docs updated
(CHANGELOG + any README/SKILL), an ADR if a real decision was made, and — if user-facing — a push
script. If a loop leaves none of these reusable, it wasn't compound; reconsider the approach.
