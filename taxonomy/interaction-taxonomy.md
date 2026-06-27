# Interaction Taxonomy (v0.1)

The catalog of interaction patterns this layer knows how to build. Each pattern has a stable ID
(`P0`–`P8`) so prompts and metadata can reference it precisely. The v0.1 MVP intentionally ships
**9 patterns** — enough to cover ~80% of learning, sales, and workshop decks.

The categories below map cleanly to *what the viewer is being asked to do*.

| Category | Patterns |
| -------- | -------- |
| Read / narrate | P0 Static |
| Reveal | P1 Reveal Cards · P2 Accordion · P3 Tooltip · P4 Modal |
| Explore | P5 Hotspot |
| Assess | P6 Quiz |
| Decide | P7 Branching Scenario |
| Simulate | P8 Calculator |

---

## P0 — Static Slide
- **Verb:** read / feel
- **Use when:** the slide is a title, section break, quote, transition, or pure narrative.
- **Avoid when:** the content genuinely rewards exploration or recall.
- **Completion rule:** none.
- **Component:** none (engine handles it).
- **PPT support:** full.

## P1 — Reveal Cards
- **Verb:** absorb in sequence
- **Use when:** explaining 3–6 short, parallel ideas — a framework, benefits, steps, myths-vs-facts.
- **Avoid when:** content is long-form paragraphs, or all points must be visible at once.
- **Completion rule:** `all_cards_revealed` (optional).
- **Component:** `components/reveal-card/`.
- **PPT support:** good (maps to click-to-appear builds).

## P2 — Accordion
- **Verb:** drill into chosen detail
- **Use when:** content has layered or optional detail — FAQ, "expand to learn more," 4–6 topics
  where the viewer self-selects depth.
- **Avoid when:** every item must be read (don't hide required content).
- **Completion rule:** `at_least_one_opened` (optional).
- **Component:** `components/accordion/`.
- **PPT support:** limited.

## P3 — Tooltip / Glossary
- **Verb:** clarify a term in place
- **Use when:** a few technical terms or labels need a short definition without leaving the flow.
- **Avoid when:** the definition is essential — then put it on the slide, not behind a hover.
- **Completion rule:** none.
- **Component:** `components/tooltip/`.
- **PPT support:** none.

## P4 — Modal (Deep Dive)
- **Verb:** open one optional layer
- **Use when:** a single slide needs one optional deep-dive (a case study, a long quote, a detailed
  chart) that would otherwise clutter the slide.
- **Avoid when:** you're tempted to use it on every slide. **Hard cap: rare.**
- **Completion rule:** none.
- **Component:** `components/modal/`.
- **PPT support:** none.

## P5 — Hotspot Discovery
- **Verb:** explore parts of a whole
- **Use when:** an image, diagram, map, screenshot, anatomy, or workflow has parts worth labeling
  and exploring one at a time.
- **Avoid when:** the content is purely linear or has no spatial structure.
- **Completion rule:** `all_hotspots_clicked` (great for learning gates).
- **Component:** `components/hotspot/`.
- **PPT support:** limited.

## P6 — Quiz / Knowledge Check
- **Verb:** recall & confirm
- **Use when:** checking understanding, a recap slide, or end-of-section reinforcement.
- **Avoid when:** there is no prior content to test, or it would interrupt a persuasive flow.
- **Completion rule:** `answered_correctly` or `attempted`.
- **Component:** `components/quiz/`.
- **PPT support:** none.

## P7 — Branching Scenario
- **Verb:** decide & see consequence
- **Use when:** the viewer should make a decision and see its outcome — roleplay, "what would you
  do," customer-service or sales training, decision trees.
- **Avoid when:** there is one correct linear path with no meaningful choice.
- **Completion rule:** `reached_an_ending`.
- **Component:** `components/branching/`.
- **PPT support:** none.

## P8 — Calculator / Simulation
- **Verb:** input numbers, get a tailored result
- **Use when:** the value is personalized math — ROI, savings, pricing, time saved, budget, payback.
- **Avoid when:** there are no meaningful inputs, or a single static number tells the story.
- **Completion rule:** `produced_a_result`.
- **Component:** `components/calculator/`.
- **PPT support:** none.

---

## Pattern Expansion v1 (added in v0.6.0 — append-only, see ADR-0006)

## P9 — Timeline
- **Verb:** advance through an ordered sequence
- **Use when:** events/steps are chronological or staged — history, project phases, a process over time.
- **Avoid when:** the items are parallel/unordered (use `P1`) or spatial (use `P5`).
- **Completion rule:** `all_points_visited`.
- **Component:** `components/timeline/`.
- **PPT support:** limited.

## P10 — Before/After Slider
- **Verb:** wipe between two states of one frame
- **Use when:** comparing two states of the *same* thing — before/after, old/new, problem/solution.
- **Avoid when:** comparing many items or non-visual attributes (use `P0` table / `P1`).
- **Completion rule:** `moved_past_threshold` (strict — does not auto-complete on load).
- **Component:** `components/before-after/`.
- **PPT support:** none.

## P11 — Drag-Match / Matching
- **Verb:** pair items across two sets
- **Use when:** matching term↔definition, cause↔effect, tool↔use, item↔category.
- **Avoid when:** it's a single-answer check (use `P6`).
- **Completion rule:** `all_pairs_matched_correctly` (or `all_pairs_matched`).
- **Component:** `components/drag-match/`.
- **PPT support:** none.

---

## Pattern selection at a glance

```
Is it a title/quote/section/transition?         → P0 Static
3–6 short parallel ideas?                        → P1 Reveal Cards
Optional/layered detail, FAQ?                    → P2 Accordion
Inline terms needing a quick definition?         → P3 Tooltip
One optional deep dive?                          → P4 Modal (rare)
Image/diagram/map with labeled parts?            → P5 Hotspot
Recall / knowledge check / recap?                → P6 Quiz
A decision with consequences / roleplay?         → P7 Branching
Numbers in → personalized result out?            → P8 Calculator
Ordered / chronological sequence?                → P9 Timeline
Two states of one frame (before/after)?          → P10 Before/After Slider
Pair items across two sets (matching)?           → P11 Drag-Match
```
