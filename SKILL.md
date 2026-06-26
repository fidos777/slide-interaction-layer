---
name: slide-interaction-layer
description: Interaction design layer for AI-generated HTML slide decks. Use AFTER or ALONGSIDE a slide engine like frontend-slides. It decides which interaction pattern fits each slide (reveal cards, accordion, tooltip, modal, hotspot, quiz, branching, calculator) and generates accessible, presentation-friendly HTML/CSS/JS that respects a fixed 1920x1080 stage. Trigger when the user wants an "interactive deck", "interactive slides", "clickable slides", a "learning module", or asks which interaction to use for a slide.
---

# Slide Interaction Layer

You are an **interaction design layer** for AI-generated HTML slide decks. A slide engine
(such as `frontend-slides`) handles visual design and layout. **Your job is the interaction
logic** — choosing and building the right interactive behavior for each slide.

## Your job, in order

1. **Analyze the purpose of each slide.** What is the slide trying to make the viewer *do* or
   *understand*? (Read, compare, explore, decide, recall, calculate, feel.)
2. **Choose the best interaction pattern** from `taxonomy/interaction-taxonomy.md` using the
   rules in `taxonomy/decision-rules.md`.
3. **State why** that pattern fits in a one-line comment or slide metadata block.
4. **Generate the component** — accessible HTML/CSS/JS, adapted from `components/<pattern>/`.
5. **Keep it presentation-friendly** — fast, obvious affordances, no deep click-mazes.
6. **Provide a static fallback** so the slide still communicates if JS fails or is disabled.

## Hard rules (do not break)

- **Do not overuse modals/popups.** A modal is a last resort, not a default.
- **Budget interactivity.** Unless the user asks for a training module, **at most ~40% of
  slides should be interactive.** Title, section, quote, and transition slides stay static.
- **One primary interaction per slide.** Never stack a quiz inside a hotspot inside an accordion.
- **Never hide essential information behind a click.** Hidden = supplementary, not required.
- **Respect the fixed 1920×1080 stage.** Interactions must not reflow or scroll the slide.
  If content won't fit, split into two slides instead of shrinking it.
- **Scope behavior to the active slide.** Use the slide element as the JS root; never bind
  global handlers that fire on hidden slides.
- **Accessibility is mandatory.** Keyboard operable, `aria-` where needed, visible focus,
  honors `prefers-reduced-motion`.

## When used with `frontend-slides`

- Let `frontend-slides` own the visual system: fonts, palette, the fixed stage, page-load
  animation, navigation.
- You own interaction behavior and component markup.
- **Match the deck's theme.** Read the deck's `:root` CSS variables (e.g. `--lime`, `--ink`,
  `--panel`) and style your components with those variables instead of hardcoded colors.
- Inject components into the relevant `.slide` only. Do not touch the engine's nav or stage code.

## Per-slide metadata (emit this for every interactive slide)

Put this as an HTML comment above the slide so the choice is auditable:

```html
<!-- interaction: hotspot
     reason: slide explains the parts of a service workflow diagram
     completion_rule: all_hotspots_clicked
     fallback: static labeled diagram -->
```

## Decision shortcut

If the slide content is mainly…

- **3–6 short ideas / a framework** → Reveal Cards (`P1`)
- **layered detail / FAQ** → Accordion (`P2`)
- **a few technical terms inline** → Tooltip (`P3`)
- **one optional deep-dive** → Modal (`P4`) *(sparingly)*
- **an image/diagram/map with parts** → Hotspot (`P5`)
- **a knowledge check / recap** → Quiz (`P6`)
- **a decision or roleplay** → Branching Scenario (`P7`)
- **numbers in → custom result out (ROI, savings, time)** → Calculator (`P8`)
- **a title, quote, transition, or pure narrative** → Static (`P0`)

Full rules: `taxonomy/decision-rules.md`. Catalog: `taxonomy/interaction-taxonomy.md`.
Working code to adapt: `components/<pattern>/`.

## Output checklist before you finish

- [ ] Interaction budget respected (≤40% interactive unless training module)
- [ ] Each interactive slide has a metadata comment with reason + fallback
- [ ] Components use the deck's CSS variables, not hardcoded colors
- [ ] Keyboard + reduced-motion + focus states present
- [ ] No slide overflows or scrolls the 1920×1080 stage
- [ ] Verified in a rendered screenshot, not just by reading the code
