# Slide Interaction Layer

An interaction design system for AI-generated HTML slide decks.

It teaches AI coding agents (Claude Code, Codex, Cursor, and others) **when** to use which
interaction pattern for a slide — reveal cards, accordions, tooltips, hotspots, quizzes,
branching scenarios, calculators — and **how** to build them as accessible, presentation-friendly
HTML/CSS/JS.

> **It is not a slide generator.** It is the *interaction layer* that sits on top of one.
> Works best with [`frontend-slides`](https://github.com/zarazhangrui/frontend-slides) and any other
> HTML slide engine.

---

## Quickstart (under 5 minutes)

**1 · See it work (30s).** Open a demo in any browser, then use ← → / Space and click the interactions:

- [`examples/demo-deck.html`](examples/demo-deck.html) — one slide per interaction pattern, each labeled.
- [`examples/ai-workflow-for-smes.html`](examples/ai-workflow-for-smes.html) — the taxonomy applied to a real topic.

**2 · Use it (1 prompt).** Point any AI coding agent at this folder and paste:

```
Read ./slide-interaction-layer/SKILL.md as a skill.
Then use frontend-slides to build an interactive HTML deck about <your topic>.
Apply the taxonomy to pick the right interaction per slide. Don't overuse popups.
```

**3 · Know the choices (at a glance).** The agent picks one pattern per slide:

| If the slide is mainly… | Pattern |
| ----------------------- | ------- |
| a title, quote, or pure narrative | **P0** Static |
| 3–6 short parallel ideas | **P1** Reveal Cards |
| layered / optional detail, FAQ | **P2** Accordion |
| a few inline terms to define | **P3** Tooltip |
| one optional deep dive (rare) | **P4** Modal |
| an image/diagram with parts | **P5** Hotspot |
| a recall / knowledge check | **P6** Quiz |
| a decision with consequences | **P7** Branching |
| numbers in → tailored result | **P8** Calculator |

That's the whole idea. Everything below is depth: the rules, the components, and how it plugs into `frontend-slides`.

---

## The problem it solves

When you ask an AI to "make an interactive deck," it usually does one of two bad things:

1. Makes everything a popup/modal until the deck is unusable, or
2. Makes nothing interactive and ships static text on a dark background.

The missing piece is a **decision system**: a taxonomy of interaction patterns plus rules for
*when each one is appropriate* and *when it is not*. That is what this layer provides.

```
content intent  →  choose interaction pattern  →  generate component  →  inject HTML/CSS/JS  →  validate usability
```

## Positioning

| Layer | Job | Example |
| ----- | --- | ------- |
| Slide engine (`frontend-slides`) | Visual design, layout, animation, fixed 16:9 stage | The "car" |
| **Slide Interaction Layer (this)** | Decide & build the right interaction per slide | The "driving mode" |

The engine makes beautiful decks. This layer makes them **interactive, structured, and
learning-ready** — without overusing popups.

## What's inside

```
slide-interaction-layer/
  README.md              ← you are here
  SKILL.md               ← the instruction an AI agent reads
  taxonomy/
    interaction-taxonomy.md   ← the 8-pattern catalog (the "dictionary")
    decision-rules.md         ← when to use / avoid each pattern (the "brain")
  components/            ← real, working HTML/CSS/JS for each pattern
    reveal-card/  accordion/  tooltip/  modal/
    hotspot/      quiz/       branching/ calculator/
  examples/
    demo-deck.html       ← a full deck that uses the layer (proof it works)
  prompts/
    use-with-frontend-slides.md  ← copy-paste prompts
```

## Example prompt (fuller)

A more complete prompt than the Quickstart one above:

```
Read ./slide-interaction-layer/SKILL.md as a skill.
Then use frontend-slides to create a 10-slide interactive HTML deck about
"How small businesses can use AI to cut admin work."
Apply the Slide Interaction Layer taxonomy to decide which slides are static,
reveal cards, accordions, hotspots, quiz, branching, or calculator.
Do not overuse popups.
```

See [`prompts/use-with-frontend-slides.md`](prompts/use-with-frontend-slides.md) for more recipes
(add interactivity to an existing deck, build a gated training module, decision-only mode).

## Demo Gallery

Open these single-file decks in any browser (← → / Space to navigate; click the interactions):

- [`examples/demo-deck.html`](examples/demo-deck.html) — a tour of the layer itself: one slide per
  interaction pattern (reveal cards, hotspot, accordion + tooltip, branching, calculator, quiz),
  each labeled with the pattern it uses.
- [`examples/ai-workflow-for-smes.html`](examples/ai-workflow-for-smes.html) — the taxonomy applied
  to a **real use case**: an "AI Workflow for SMEs" teaching deck. It shows the decision system in
  practice — picking the right interaction per slide for a genuine business topic, with static
  intro/closing slides and ~67% interactive (teaching-deck budget), every interactive slide carrying
  its `interaction / reason / completion_rule / fallback` metadata. **It is also ontology-annotated**:
  each slide has an `element` (E1–E15) + objective + pattern + gating + rationale comment, so it
  doubles as a worked example of the ontology-first flow (see [`ontology/`](ontology/)).
- [`examples/gated-training-demo.html`](examples/gated-training-demo.html) — the **optional
  completion-gating** runtime in action: forward navigation is blocked on each slide until its
  activity is finished (reveal/hotspot/quiz/branching/calculator). Backward always works.

## Completion gating (optional)

By default decks are **ungated** — nothing blocks navigation. For training / e-learning you can opt
in to **completion gating**: forward navigation waits until a slide's required activity is complete.

```html
<script src="gating/gate.js"></script>
<div id="stage" data-sil-gating="training">…</div>   <!-- off (default) | on | training -->
```

It's opt-in, **fail-open** (no JS → fully navigable), accessible, and needs no component changes.
Full details and per-interaction overrides: [`gating/README.md`](gating/README.md).

## Element ontology (optional, recommended for learning)

A semantic layer **above** the taxonomy: it names *what* a piece of content is (`E1`–`E15`) before
you pick *how* to present it (`P0`–`P8`). It renders nothing — pure classification that makes pattern
choice consistent and auditable. Recommended for learning/courseware; skippable for everyday decks.

```
Element Ontology (WHAT) → Taxonomy P0–P8 (HOW) → Gating (SHOULD progression wait)
```

Catalog, mapping, metadata format, and governance checks: [`ontology/`](ontology/). Element IDs are
`E`-prefixed and never collide with the `P` patterns.

## Design constraints (so it stays compatible with `frontend-slides`)

- Single self-contained HTML files. No npm, no build step.
- Respects the fixed **1920×1080** stage — interactions never reflow the slide.
- Every interactive pattern has a **static fallback** if JS is disabled or fails.
- Keyboard-accessible and `prefers-reduced-motion` aware.
- Interactions are scoped to the active slide only.

## Installation & compatibility

> **New here?** [`INSTALL.md`](INSTALL.md) walks through three beginner-friendly install paths:
> local agent usage, Claude plugin (local/manual), and the org-wide private marketplace.

The skill entrypoint is **`SKILL.md`** (uppercase) — the convention used by Claude Code /
Anthropic skills and by `frontend-slides` itself.

- **Claude Code / Cowork / Anthropic skills:** point the agent at this folder; `SKILL.md` is
  read automatically. No rename needed.
- **Case-insensitive filesystems (macOS, Windows):** do **not** add a second `skill.md` — it
  collides with `SKILL.md`. Keep one file.
- **An installer that strictly expects lowercase `skill.md`:** on a case-sensitive filesystem
  (most Linux) run `cp SKILL.md skill.md`; on macOS/Windows just rename `SKILL.md` → `skill.md`.
- **Other agents (Codex, Cursor):** there's no install step — just tell the agent to read
  `SKILL.md` and the `taxonomy/` folder as context (see `prompts/`).

## Extensions (optional)

The core layer stays universal. Optional, namespaced extensions add domain-specific governance
**without changing** the core taxonomy, components, or pattern IDs — load them only when relevant.

- [`extensions/mmd-elearning/`](extensions/mmd-elearning/) — **MMD E-learning Governance** (spec):
  SOPs and vocabulary for producing regulated courseware (completion gating defaults, media
  assembly, an S0 readiness board, and an AI maintainer loop). Ignore it for everyday decks.

## Roadmap

- **v0.1** — 8 MVP patterns, taxonomy, decision rules, working components, demo decks.
- **v0.2** — ✅ optional completion-gating runtime (`gating/gate.js`) + gated example.
- **v0.3** — ✅ Element Ontology semantic layer (`ontology/`).
- **v0.4** — ✅ Recursive Repository Improvement (`improvement/`): pre-release gate + scorecards.
- **v0.5 (current)** — ✅ machine-readable ontology sidecar (`ontology/schema.json` + example).
  Next: validator CLI (v0.5.1) and more patterns (timeline, before/after slider, drag-match).
- **v1.0** — packaged as an installable skill/plugin; theme-aware component styling.

## Maintainer & philosophy

This repo is maintained by **compound engineering** — every change leaves behind a reusable asset
(spec, script, decision record) so the next change is easier. The maintainer runs the **CORD**
cycle: **C**lassify → **O**perationalize → **R**euse → **D**ocument.

- Operating model: [`docs/compound-engineering.md`](docs/compound-engineering.md)
- Maintainer loop + CORD: [`MAINTAINER.md`](MAINTAINER.md)
- Decision records (ADRs): [`decisions/`](decisions/)
- Recursive Repository Improvement (pre-release gate + scorecards): [`improvement/`](improvement/)

Every release runs an RRI gate (LOAD → AUDIT → SCORE → VERIFY → REVIEW → ROUTE → DECIDE), so each
release's weakest area becomes the next release's priority.

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md) for the full release history (v0.1.0 → today).

## License

MIT — use it, fork it, ship it.
