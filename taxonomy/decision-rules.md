# Decision Rules (v0.1)

This is the **brain** of the layer. It turns "make it interactive" into specific, defensible
choices. Apply these rules per slide.

## Step 1 — Classify the slide's intent

Ask: *what is the viewer being asked to do on this slide?*

| Intent signal in the content | Pattern |
| ---------------------------- | ------- |
| Title, quote, section break, transition, pure narrative/emotional beat | **P0 Static** |
| 3–6 short, parallel concepts (framework, benefits, steps, myths/facts) | **P1 Reveal Cards** |
| Layered or optional detail; FAQ; "expand to learn more" | **P2 Accordion** |
| A few technical terms/labels needing a one-line definition | **P3 Tooltip** |
| Exactly one optional deep dive that would clutter the slide | **P4 Modal** |
| Image, diagram, map, screenshot, anatomy, or workflow with parts | **P5 Hotspot** |
| Recall, recap, end-of-section reinforcement | **P6 Quiz** |
| A decision with consequences; roleplay; "what would you do?" | **P7 Branching** |
| ROI, pricing, savings, time saved, budget, payback, any "numbers in → result out" | **P8 Calculator** |

If two patterns seem to fit, pick the one whose **verb** matches the slide's real goal
(read / reveal / explore / assess / decide / simulate). When still tied, prefer the **simpler**
pattern (a Reveal Card over a Modal; a Tooltip over a Modal).

## Step 2 — Apply the interaction budget

- **Default decks (sales, pitch, talk, internal):** at most **~40% of slides interactive.**
  The rest stay P0. Persuasion needs flow; constant clicking kills momentum.
- **Training / e-learning modules:** budget can rise to ~70%, and completion gates are encouraged.
- **Title, section, quote, and closing slides are always P0.**

## Step 3 — Avoid the common failure modes

```
DON'T put a modal on every slide.            → most "more detail" belongs in P1/P2 inline.
DON'T hide essential info behind a click.    → hidden content must be supplementary only.
DON'T stack interactions.                     → one primary interaction per slide.
DON'T add interaction that slows a talk.       → if it doesn't aid understanding, use P0.
DON'T require hover on touch devices.          → P3 tooltips must also work on tap.
DON'T reflow the slide to fit a widget.        → respect the fixed 1920×1080 stage; split instead.
```

## Step 4 — Decide the completion rule

For learning decks, an interaction can **gate navigation** (block "next" until done). Use the
completion rule from the taxonomy:

| Pattern | Typical completion rule | Gate next slide? |
| ------- | ----------------------- | ---------------- |
| P1 Reveal Cards | `all_cards_revealed` | optional |
| P2 Accordion | `at_least_one_opened` | rarely |
| P5 Hotspot | `all_hotspots_clicked` | yes, for learning |
| P6 Quiz | `answered_correctly` | yes, for learning |
| P7 Branching | `reached_an_ending` | yes |
| P8 Calculator | `produced_a_result` | optional |

Gating is **off by default** for sales/talk decks and **on by default** for training modules.

## Step 5 — Always define the fallback

Every interactive slide must degrade gracefully:

| Pattern | Static fallback |
| ------- | --------------- |
| P1 Reveal Cards | all cards shown |
| P2 Accordion | all sections expanded |
| P3 Tooltip | term + definition shown inline |
| P4 Modal | summary visible; deep-dive appended below |
| P5 Hotspot | labeled static diagram |
| P6 Quiz | question + correct answer shown |
| P7 Branching | linear summary of the recommended path |
| P8 Calculator | a worked example with default numbers |

## Worked examples

> **Slide:** "The 4 pillars of our AI strategy."
> Intent = 4 short parallel ideas → **P1 Reveal Cards.** Reason: framework, reveal builds focus.

> **Slide:** A diagram of the order-fulfilment pipeline.
> Intent = parts of a whole → **P5 Hotspot.** completion_rule: all_hotspots_clicked.
> Fallback: labeled static diagram.

> **Slide:** "How much could you save with automation?"
> Intent = numbers in → result out → **P8 Calculator.** completion_rule: produced_a_result.

> **Slide:** "A customer is angry about a late delivery. What do you do?"
> Intent = decide & see consequence → **P7 Branching.**

> **Slide:** Opening title.
> Intent = set the tone → **P0 Static.** Never make the title slide interactive.
