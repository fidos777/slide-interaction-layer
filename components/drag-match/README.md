# P11 — Drag-Match / Matching

Use to **pair items across two sets**: term↔definition, cause↔effect, tool↔use, item↔category.
**Avoid** for single-answer checks (`P6`).

- **Completion rule:** `all_pairs_matched_correctly` (sets `data-complete="true"` when every source is
  correctly matched).
- **a11y first:** **drag is an enhancement, not the only path.** The primary path is keyboard/click —
  select a source (`aria-grabbed`), then select its target; correct locks, incorrect bounces with a
  polite `aria-live` message. Visible focus throughout.
- **Theme vars:** `--sil-*`. **Fallback:** with JS off, the correct pairs are present as a readable list.
- **Gating:** gateable in training mode via `all_pairs_matched_correctly`.
