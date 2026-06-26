# ADR-0005 — Defer the ontology.json sidecar

- **Status:** Accepted
- **Date:** 2026-06-26
- **Deciders:** maintainer (fidos777)
- **Related:** ADR-0003

## Context

A machine-readable per-deck `ontology.json` (slide → element/objective/pattern/gating) would enable
tooling and automated audits. But locking a schema before there are real annotated decks risks
designing the wrong shape and then having to break it.

## Decision

Ship v0.3.0 **docs-only** for the ontology and **defer** the `ontology.json` sidecar to **v0.3.1**.
For v0.3.0 the per-slide annotation comment (`ontology/metadata-format.md`) is the source of truth.
The sidecar schema will be designed against at least one real annotated deck first.

## Consequences

- **Positive:** avoids premature schema lock-in; keeps v0.3.0 simple and low-risk; gives the future
  schema real examples to fit.
- **Constraint:** automated ontology audits that need a machine-readable file wait until v0.3.1; until
  then, audits parse the annotation comments.
- **Follow-up:** v0.3.1 introduces `ontology.json` with a worked example deck (planned).
