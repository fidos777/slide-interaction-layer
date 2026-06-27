# P10 — Before/After Slider

Use to compare **two states of the same frame**: before/after, old/new, problem/solution.
**Avoid** for many-item or non-visual comparisons (`P0` table / `P1`).

- **Completion rule:** `moved_past_threshold` — **strict**: the worked position renders on load but
  completion fires only after the user moves the handle past a small threshold (mirrors the
  calculator's `user_changed`). Never auto-completes.
- **Theme vars:** `--sil-*`. **a11y:** the divider is a native `<input type="range">` (keyboard
  arrows work), endpoints labeled "Before"/"After", visible focus.
- **Fallback:** with JS off, both states are present and labeled.
- **Gating:** gateable in training mode via `moved_past_threshold`.
