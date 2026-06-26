# Element → Interaction map (+ gating justification)

Maps each element (`E1`–`E15`) to a **primary** `P0`–`P8` pattern and acceptable alternates. This
**narrows** the choice; the taxonomy decision rules (`../taxonomy/decision-rules.md`) still make the
final call (interactivity budget, "one primary interaction", "don't overuse modals", fallback).

All targets are existing patterns — **no new pattern IDs are introduced**.

## Mapping

| Element | Primary | Acceptable alternates |
| ------- | ------- | --------------------- |
| `E1` Concept | `P1` Reveal Cards | `P3` Tooltip (inline term), `P0` Static |
| `E2` Principle / Rule | `P1` Reveal Cards | `P0` Static, `P2` Accordion |
| `E3` Process / Procedure | `P5` Hotspot (on a diagram) | `P1` Reveal Cards (step build) |
| `E4` Structure / Anatomy | `P5` Hotspot | `P0` labeled static (fallback) |
| `E5` Classification | `P2` Accordion | `P1` Reveal Cards |
| `E6` Comparison | `P0` Static (table) | `P1` Reveal Cards |
| `E7` Cause & Effect | `P7` Branching (if choice-driven) | `P5` Hotspot, `P0` Static |
| `E8` Example / Case | `P4` Modal (sparingly) | `P0` Static |
| `E9` Fact / Data | `P0` Static | `P3` Tooltip |
| `E10` Decision / Judgment | `P7` Branching | — |
| `E11` Assessment / Check | `P6` Quiz | — |
| `E12` Calculation | `P8` Calculator | — |
| `E13` Warning / Critical | `P0` Static (**always visible**) | none |
| `E14` Motivation / Framing | `P0` Static | — |
| `E15` Summary / Recap | `P1` Reveal Cards | `P6` Quiz (recap) |

> Roadmap note: `E3` and `E6` would also suit future patterns (timeline, before/after slider). Until
> those exist, use the current patterns above — the ontology requires no new patterns.

## When gating is justified (per element)

Gating (see `../gating/`) is opt-in and applies **only** to elements whose pattern is gateable
**and** that are marked `required`.

| Stance | Elements | Why |
| ------ | -------- | --- |
| **Justified** — gate in `training` | `E3`, `E4` (hotspot · `all_hotspots_clicked`), `E10` (branching · `reached_an_ending`), `E11` (quiz · `answered_correctly`), `E12` (calculator · `user_changed`) | engagement *is* the learning; completion is meaningful |
| **Conditional** — gate only if required reading | `E1`, `E2`, `E5`, `E15` (reveal/accordion) | gate sparingly; never trap on enrichment |
| **Never gate / never hide** | `E13` Warning, essential `E9` Fact/Data, `E14` Framing | safety/critical info must always be visible |

Hard rules carried from v0.2: gating is **fail-open**, and **`E13` must never sit behind an
interaction or gate**. The audit checks enforce this (`audit-checks.md`).
