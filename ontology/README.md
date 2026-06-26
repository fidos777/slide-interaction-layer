# Element Ontology (optional, recommended for learning/courseware)

A **semantic layer that sits above the taxonomy.** It names *what a piece of learning content is*
**before** any interaction is chosen. It renders nothing — it is metadata/decision guidance, **not a
UI layer**.

```
Element Ontology  (WHAT is this content?)   ← this folder (semantic)
        ↓
Taxonomy P0–P8    (HOW do we present it?)    ← /taxonomy
        ↓
Gating runtime    (SHOULD progression wait?) ← /gating (v0.2, opt-in)
```

- **Optional but recommended** for learning/courseware decks. Everyday presentation decks can skip it
  and go straight to the taxonomy — the core stays lightweight.
- Element IDs use an **`E`** prefix (`E1`–`E15`) so they never collide with the `P` pattern IDs.
- Adds **no runtime, no components, no taxonomy ID changes**.

## Why classify first

Choosing an interaction without first naming the content is how decks drift into "popup everything."
Classifying the element makes pattern choice consistent, explainable, and auditable, and it gives the
e-learning governance checks something concrete to verify.

## What's inside

| Doc | Purpose |
| --- | ------- |
| [`element-ontology.md`](element-ontology.md) | The catalog of 15 element types (definitions, signals, examples). |
| [`element-to-pattern-map.md`](element-to-pattern-map.md) | Element → `P0`–`P8` mapping + when gating is justified. |
| [`metadata-format.md`](metadata-format.md) | How to annotate slides/blocks (semantic comment + `data-sil-element`). |
| [`audit-checks.md`](audit-checks.md) | Governance audit checks for courseware decks. |
| [`schema.json`](schema.json) | JSON Schema for the optional machine-readable sidecar (`<deck>.ontology.json`). |
| [`validate.py`](validate.py) · [`README-validate.md`](README-validate.md) | Stdlib validator: checks a sidecar against the schema + its deck. |

## How to use it (ontology-first flow)

For a learning/courseware deck, classify each slide before picking a pattern:

```
A. CLASSIFY (ontology)     — name the element type (E1–E15) + the learning objective.
B. MAP (ontology→taxonomy) — get candidate pattern(s) for that element.
C. SELECT (taxonomy)       — apply the existing decision rules to pick the final pattern.
D. GATE (gating, opt-in)   — if courseware + required + gateable, set the gating rule.
```

See the **"Ontology-first" section in [`../SKILL.md`](../SKILL.md)**. For non-learning decks, skip
A–B and use the taxonomy directly.

## Machine-readable sidecar

A deck may carry an optional `<deck>.ontology.json` sidecar (same fields, deterministic JSON) for
tooling. Schema: [`schema.json`](schema.json); worked example:
[`../examples/ai-workflow-for-smes.ontology.json`](../examples/ai-workflow-for-smes.ontology.json).
Generated **from** the HTML comments (one-way); the runtime does not read it. See
[`metadata-format.md`](metadata-format.md).

## Status

- **v0.3.0:** docs — ontology, mapping, metadata guide, audit checks.
- **v0.5.0:** optional machine-readable sidecar — `schema.json` + a worked example. **Recommended,
  not required.**
- **v0.5.1 (this):** stdlib validator `validate.py` (+ `README-validate.md`) that enforces the
  schema/rules and deck-mirror; wired into the RRI release audit.
