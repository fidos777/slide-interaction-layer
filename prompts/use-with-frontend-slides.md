# Prompts: using the layer with `frontend-slides`

Copy-paste these into Claude Code, Codex, Cursor, or any agent that can read local files.

## 1. Build a new interactive deck

```
Read ./slide-interaction-layer/SKILL.md as a skill.
Then use frontend-slides to create a 10-slide interactive HTML deck about:
"How small businesses can use AI to cut admin work."

For each slide:
- classify its intent and choose a pattern from the Slide Interaction Layer taxonomy
- add the per-slide metadata comment (interaction / reason / completion_rule / fallback)
- implement the interaction in accessible HTML/CSS/JS using the matching components/ folder
- keep at most ~40% of slides interactive (this is a sales-style deck, not a training module)
- do not overuse modals
```

## 2. Add interactivity to an existing deck

```
Read ./slide-interaction-layer/SKILL.md as a skill.
Here is an existing frontend-slides HTML deck: ./my-deck.html
Audit each slide, propose the best interaction pattern (or P0 Static), then implement the
top 3 highest-value interactions only. Match my deck's :root CSS variables. Keep the fixed
1920x1080 stage intact and verify with a screenshot.
```

## 3. Turn a deck into a training module (gating on)

```
Read ./slide-interaction-layer/SKILL.md as a skill.
Build a 12-slide TRAINING module on customer-service basics with frontend-slides.
This is a training module: interactivity budget up to ~70%, and turn completion gating ON.
Use hotspots for the service-flow diagram (gate: all_hotspots_clicked), a branching scenario
for the angry-customer slide, and a quiz recap at the end (gate: answered_correctly).
```

## 4. Ask only for the decision (no code yet)

```
Read ./slide-interaction-layer/taxonomy/ as reference.
Here is my slide outline (titles + 1-line summaries). For each slide, tell me the best
interaction pattern ID, a one-line reason, and the completion rule. Don't write code yet.
```

## Tips

- Tell the agent the **deck type** up front (sales / talk / training) so it sets the right
  interaction budget and gating default.
- If the output is over-interactive, add: `Reduce interactive slides to no more than 40%.`
- If you want auditability, add: `Emit the per-slide interaction metadata comments.`
