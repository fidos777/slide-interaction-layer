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

## Deferred: machine-readable sidecar (`ontology.json`)

A per-deck `ontology.json` (slide → element/objective/pattern/gating) is **planned for v0.3.1**. It
is intentionally **not** specified here yet, so its schema can be designed against real decks. For
v0.3.0, the annotation comment above is the source of truth.
