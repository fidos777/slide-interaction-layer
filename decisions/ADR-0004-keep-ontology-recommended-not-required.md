# ADR-0004 — Keep the ontology recommended, not required

- **Status:** Accepted
- **Date:** 2026-06-26
- **Deciders:** maintainer (fidos777)
- **Related:** ADR-0003

## Context

The Element Ontology (ADR-0003) is valuable for learning/courseware, but forcing every deck to
classify content first would add friction to everyday presentation decks and risk turning a
lightweight tool into a heavyweight process.

## Decision

Position the ontology as **recommended for learning/courseware, optional for everyday decks**. The
`SKILL.md` ontology-first flow (Classify → Map → Select → Gate) explicitly says non-learning decks
may skip Classify/Map and go straight to the taxonomy. The core stays lightweight by default.

## Consequences

- **Positive:** courseware gets rigor; casual decks stay fast; adoption is opt-in and low-risk.
- **Constraint:** governance checks that assume ontology annotations apply only to decks that opt in;
  they must not flag everyday decks for "missing" elements.
- **Trade-off:** consistency is not enforced globally — accepted, because the alternative (mandatory
  classification) harms the common case. Revisit if courseware becomes the dominant use.
