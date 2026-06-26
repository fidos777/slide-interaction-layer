# Example quality score (rubric, 0–100)

Holds each example deck to a measurable bar. Run during **VERIFY**. Score every example; a deck below
the threshold is a must-fix before release.

## Rubric (10 points each)

| # | Criterion | 10 pts when… |
| - | --------- | ------------ |
| 1 | Interactions fire | every interaction verified working (not assumed) |
| 2 | Per-slide metadata | each interactive slide has the interaction-metadata comment |
| 3 | Static fallback | every interaction degrades gracefully with no JS |
| 4 | Keyboard operable | all controls reachable + visible focus |
| 5 | Reduced motion | honors `prefers-reduced-motion` |
| 6 | Fixed stage | 1920×1080 respected; no overflow/scroll/reflow |
| 7 | No console errors | clean load + interaction, no thrown errors |
| 8 | Budget/intent fit | interactivity level matches deck type (talk vs training) |
| 9 | Gating correctness | if gated: forward blocks until complete, backward always works |
| 10 | Theming | components use deck CSS variables, not hardcoded colors |

**Score = sum (0–100). Threshold to ship: ≥ 80**, with criteria 1 and 3 mandatory (a deck that
fails "interactions fire" or "static fallback" is an automatic must-fix regardless of total).

## How to verify (suggested)

- Render + drive the deck headlessly (e.g. jsdom or a browser) and assert completion state changes.
- For gated decks, assert `SILGate.canLeave(i)` flips false→true as activities complete.
- Capture a screenshot at 1280×720 + one phone viewport to confirm the fixed stage.

## Output
Per-example: score `/100`, the criteria failed, and a must-fix list. Record alongside the release
scorecard.
