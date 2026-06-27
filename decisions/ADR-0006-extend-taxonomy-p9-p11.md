# ADR-0006 — Extend the taxonomy with P9–P11 (append-only)

- **Status:** Accepted
- **Date:** 2026-06-27
- **Deciders:** maintainer (fidos777)
- **Related:** ADR-0001 (P0–P8 taxonomy)

## Context

The interaction taxonomy has been a stable 9-pattern contract (`P0`–`P8`) since v0.1. Three
recurring needs are not well served by the existing patterns: ordered/temporal sequences, continuous
two-state visual comparison, and many-to-many pairing. Adding patterns touches a public contract that
later layers (gating, ontology map, sidecar schema, validator) depend on, so the change must be made
without breaking any of them.

## Decision

Extend the taxonomy by **appending** three new patterns — `P9` Timeline, `P10` Before/After Slider,
`P11` Drag-Match — in v0.6.0. Pattern IDs are **append-only**: existing IDs `P0`–`P8` are never
renamed, renumbered, or repurposed (this reaffirms ADR-0001). New patterns are additive and optional;
no existing deck, component, gating rule, ontology mapping, or sidecar is required to change.

Downstream, additive-only edits accompany the new IDs: the sidecar `pattern` regex widens from
`^P[0-8]$` to `^P(?:[0-9]|1[01])$` (P0–P11), the gating `GATEABLE` set and the ontology map gain the
new patterns, and the validator's `RE_P`/`ALLOWED` widen to match.

## Consequences

- **Positive:** richer coverage (timelines, before/after, matching) with zero disruption to existing
  decks; the established component/gating/ontology contracts absorb the new patterns additively.
- **Constraint:** the taxonomy is now an append-only series through `P11`; any future pattern is
  `P12+`. Renumbering would be a breaking change requiring a new ADR + major version.
- **Schema impact:** the one cross-cutting edit is the sidecar `pattern` regex; the existing example
  sidecar must continue to validate (enforced by the RRI release audit's `validate.py --all`).
- **Follow-ups:** v0.6.0 ships docs, components, gating, schema/validator, and a dedicated showcase
  deck + sidecar; the RRI gate must pass before release.
