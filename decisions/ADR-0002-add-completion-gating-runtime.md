# ADR-0002 — Add the completion-gating runtime

- **Status:** Accepted
- **Date:** 2026-06-26
- **Deciders:** maintainer (fidos777)
- **Related:** ADR-0001

## Context

Learning/courseware decks need to block progression until a required activity is completed, but
ordinary presentation decks must stay free-flowing. Any gating had to avoid breaking existing decks
and avoid becoming a content barrier.

## Decision

Add an **optional, opt-in** runtime `gating/gate.js` (shipped in v0.2.0). It activates only when a
stage sets `data-sil-gating="on" | "training"` *and* the script is included (double opt-in). It reads
the completion signals components already emit (`data-complete`), blocks only forward navigation,
keeps backward navigation, and is **fail-open** (no JS → fully navigable). Calculator uses strict
`user_changed`; quiz training default is `answered_correctly`.

## Consequences

- **Positive:** courseware gets real gating; core decks are untouched and behave identically; no
  component changes were required.
- **Constraint:** gating is a UX/compliance-flow aid, **not a security boundary** — audit proof must
  come from an LMS/SCORM/xAPI layer. Critical info (`E13`) must never sit behind a gate.
- **Follow-ups:** the ontology (ADR-0003) defines per-element gating justification.
