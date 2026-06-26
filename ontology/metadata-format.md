# Element metadata format (semantic, additive — no UI)

How to record an element classification on a slide or content block. This is **metadata only** — it
changes nothing visually and runs no code. Both forms below are optional.

## (a) Per-slide annotation comment

Extends the existing interaction-metadata comment. Place it above the slide:

```html
<!-- element: E4 structure
     objective: "Identify the four stages of the fulfilment workflow"
     bloom: understand            (optional: remember|understand|apply|analyze|evaluate|create)
     required: true               (governance: must be engaged)
     pattern: P5 hotspot          (chosen interaction, from element-to-pattern-map.md)
     gating: all_hotspots_clicked (only if required + gateable)
     rationale: "parts of a whole → explore each part" -->
```

Field notes:
- `element` — one of `E1`–`E15` (see `element-ontology.md`). **One primary element per slide.**
- `objective` — the learning objective in plain language.
- `bloom` — optional cognitive level.
- `required` — governance flag; drives whether gating applies.
- `pattern` — the `P0`–`P8` pattern actually used.
- `gating` — the completion rule, only when `required` and the pattern is gateable.
- `rationale` — one line explaining the choice (auditable).

## (b) Block-level hook (finer granularity)

A content block may carry a semantic attribute for tooling. It has **no styling or behavior**
attached — it's a hook only:

```html
<section class="slide" data-sil-element="E4"> … </section>
```

Use the per-slide comment for the primary element; use `data-sil-element` on secondary blocks if a
slide genuinely contains more than one element.

## Relationship to interaction metadata

The element comment is the *semantic* layer; the existing interaction comment
(`interaction / reason / completion_rule / fallback`) is the *mechanics* layer. For courseware, write
the element comment first (it explains the pattern choice), then the interaction comment.

## Machine-readable sidecar (`<deck>.ontology.json`)

A per-deck sidecar carries the same fields in a deterministic JSON form for tooling (validators,
course compilers, agents). The HTML comments stay the **human source of truth**; the sidecar is
generated **from** them (one-way) and is **optional but recommended** for learning/courseware.

- Schema (validation contract): [`schema.json`](schema.json)
- Worked example: [`../examples/ai-workflow-for-smes.ontology.json`](../examples/ai-workflow-for-smes.ontology.json)
- Convention: name it `<deck-basename>.ontology.json` next to the deck; keep `slideCount` and each
  `index` in sync with the deck.

The runtime does **not** read the sidecar; it is for tooling only. A validator CLI is planned for
v0.5.1 — for now, validate against `schema.json` with any JSON Schema (draft 2020-12) tool.
