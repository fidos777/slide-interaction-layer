# ADR-0003 — Add the Element Ontology layer

- **Status:** Accepted
- **Date:** 2026-06-26
- **Deciders:** maintainer (fidos777)
- **Related:** ADR-0001, ADR-0004

## Context

Choosing an interaction pattern without first naming *what the content is* leads to inconsistent and
hard-to-audit decks. Learning/courseware especially benefits from classifying content (concept,
process, assessment, etc.) before deciding how to present it.

## Decision

Add an **Element Ontology** semantic layer (`ontology/`, shipped in v0.3.0): 15 element types
**`E1`–`E15`** with definitions, an element→pattern map, a metadata format, and governance audit
checks. Element IDs use an `E` prefix so they never collide with `P0`–`P8`. It renders nothing — it
is classification/metadata, not UI.

## Consequences

- **Positive:** consistent, explainable pattern choices; a basis for governance checks; reusable
  across the e-learning extension.
- **Constraint:** the ontology must stay a semantic layer (no UI, no runtime) and must not redefine
  `P` IDs. `E13` Warning must never be hidden behind an interaction or gate.
- **Follow-ups:** ADR-0004 (recommended-not-required), ADR-0005 (sidecar deferral).
