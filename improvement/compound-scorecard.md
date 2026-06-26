# Compound scorecard (template + guide)

Score the repo on **8 axes, 1–10, unweighted**, each release. Copy the table into
`scorecards/<version>.md`, fill it, compute deltas vs the previous scorecard, and record the
**weakest axis as the candidate priority for the next release**.

## Axes (what each means)

| Axis | Score when high |
| ---- | --------------- |
| **Clarity** | a newcomer understands the repo's purpose fast |
| **Usefulness** | breadth/depth of what it actually does |
| **Installability** | easy to install/use across the documented paths |
| **Demo quality** | examples are polished, correct, and verified |
| **Agent usability** | SKILL.md + docs let an agent act correctly first try |
| **Documentation** | accurate, complete, no stale claims |
| **Roadmap** | clear direction; promises tracked |
| **Release readiness** | clean releases, changelog, decision records, repeatable shipping |

## Scoring guide (anchors)

- **9–10** — exemplary; nothing material to add this release.
- **7–8** — solid; minor gaps.
- **5–6** — usable but a clear weakness.
- **≤4** — blocking weakness; likely the next priority.

## Template

```md
# Scorecard — v<version>  (<date>)

| Axis | Score | Δ vs prev | Note |
| ---- | ----- | --------- | ---- |
| Clarity            |  /10 |  | |
| Usefulness         |  /10 |  | |
| Installability     |  /10 |  | |
| Demo quality       |  /10 |  | |
| Agent usability    |  /10 |  | |
| Documentation      |  /10 |  | |
| Roadmap            |  /10 |  | |
| Release readiness  |  /10 |  | |

Weakest axis: <axis> (<score>)
Next-release candidate priority: <one line>
Regressions (with reason): <none | …>
```

## Rules
- A **regression** on any axis is allowed only with a written reason in the "Regressions" line.
- The **weakest axis** drives the next loop's CORD *Classify* step (this is the recursion).
- Keep every filled scorecard in `scorecards/` so trends are traceable over time.
