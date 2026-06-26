# Completion Gating (`gate.js`) — optional runtime

`gate.js` can block forward navigation on a slide until its **required** interactions are complete.
It is **opt-in**, **off by default**, **fail-open**, and needs **no component changes**.

> Core decks stay ungated. Only decks that explicitly opt in are affected.

## Enable it (two steps)

1. Include the runtime once, after your deck's navigation script:
   ```html
   <script src="../gating/gate.js"></script>
   ```
2. Turn it on, on the stage wrapper:
   ```html
   <div id="stage" data-sil-gating="training">   <!-- off (default) | on | training -->
   ```

If either step is missing, the deck behaves exactly as before.

## Modes

| Mode | Effect |
| ---- | ------ |
| `off` / absent | Runtime is inert. (Default for all core decks.) |
| `on` | Block forward nav only on slides marked `data-sil-gate="required"` (or interactions marked `data-required="true"`). |
| `training` | Block forward nav on **every** slide with a gateable interaction, unless that interaction is `data-required="false"`. (E-learning default.) |

## Gateable patterns & completion signal

| Pattern (`data-sil`) | Default rule | Source |
| -------------------- | ------------ | ------ |
| `reveal-cards` | `all_cards_revealed` | component `data-complete` |
| `hotspot` | `all_hotspots_clicked` | component `data-complete` |
| `quiz` | `answered_correctly` | component `data-complete` |
| `branching` | `reached_an_ending` | component `data-complete` |
| `calculator` | `user_changed` (**strict**) | runtime listens for a real input/click — **does not** count the on-load example |

Non-gateable: `tooltip`, `modal`, static slides. `accordion` is not gated by default.

### Per-interaction overrides
- `data-required="true|false"` — force-include/exclude this interaction from the gate.
- `data-gate="<rule>"` — override the rule, e.g. a non-training deck may set
  `data-gate="attempted"` on a quiz to accept any answer.

## How navigation is controlled

A slide is **satisfied** when all its required interactions are complete. While unsatisfied, the
runtime blocks forward moves (→, PageDown, forward Space, an on-screen `[data-sil-next]`, and forward
jumps on `#dots`/`.dots` buttons), shows a polite hint, and focuses the first incomplete activity.
**Backward navigation is always allowed.** If your engine exposes navigation, it can also call
`window.SILGate.canLeave(index)` instead of relying on interception.

## Accessibility

Next controls become `aria-disabled` (not `disabled`, so they stay focusable and announce why);
focus moves to the incomplete activity; the hint uses `role="status"` / `aria-live="polite"`; no
keyboard trap; honors `prefers-reduced-motion` (no motion in the hint).

## Fail-open (important)

With JS disabled or on any runtime error, the gate does nothing and the deck is fully navigable with
all content visible via each component's static fallback. Gating is a UX/compliance-flow aid, **not a
security boundary** — proof of completion for audit must come from an LMS/SCORM/xAPI layer.

## Test/engine hooks

`window.SILGate.canLeave(i)`, `.isSatisfied(i)`, `.refresh()`, `.mode`, `._state`.

See [`../examples/gated-training-demo.html`](../examples/gated-training-demo.html) for a working
gated deck.
