# P9 — Timeline

Use for an **ordered / chronological sequence**: history, project phases, a process over time.
**Avoid** for parallel/unordered items (`P1`) or spatial parts (`P5`).

- **Completion rule:** `all_points_visited` (sets `data-complete="true"`).
- **Theme vars:** `--sil-*`. **a11y:** points are `<button>`s, `aria-current="step"` on the active
  point, ←/→ move focus between points, visible focus ring.
- **Fallback:** with JS off, all points + details remain readable.
- **Gating:** gateable in training mode via `all_points_visited`.
