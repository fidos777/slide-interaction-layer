# ADR-0001 — Use the P0–P8 interaction taxonomy

- **Status:** Accepted
- **Date:** 2026-06-26
- **Deciders:** maintainer (fidos777)

## Context

AI agents asked to "make an interactive deck" tend to either over-use modals/popups or ship static
text. The project needed a small, stable vocabulary of interaction patterns plus rules for when each
applies, so pattern choice is consistent and auditable across decks and agents.

## Decision

Adopt a fixed catalog of nine interaction patterns with stable IDs **`P0`–`P8`** (Static, Reveal
Cards, Accordion, Tooltip, Modal, Hotspot, Quiz, Branching, Calculator), documented in `taxonomy/`
with decision rules. IDs are stable identifiers that later layers may reference but must not redefine.

## Consequences

- **Positive:** a shared language for humans, agents, gating, and the ontology; predictable output;
  enables governance.
- **Constraint:** pattern IDs are now part of the public contract — they must not be renamed or
  renumbered (only added to, as `P9+`). Breaking this requires a new ADR and a major version.
- **Follow-ups:** the gating runtime (ADR-0002) and ontology (ADR-0003) build directly on these IDs.
