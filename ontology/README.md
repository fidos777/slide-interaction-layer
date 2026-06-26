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

## Status

- **v0.3.0 (this):** docs only — the ontology, mapping, metadata guide, and audit checks.
- **v0.3.1 (planned):** optional machine-readable `ontology.json` sidecar (deferred so its schema can
  be designed against real decks).
