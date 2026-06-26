# P1 — Reveal Cards

Use when a slide has **3–6 short parallel ideas** revealed one at a time: frameworks, benefits,
steps, myths-vs-facts.

**Avoid for:** long paragraphs, or info that must all be visible immediately.

- **Completion rule:** `all_cards_revealed` (sets `data-complete="true"` on the container).
- **Theme vars:** `--sil-ink --sil-muted --sil-accent --sil-panel --sil-line --sil-bg`.
- **A11y:** cards are `<button>`s, Enter/Space reveal, visible focus ring.
- **Fallback:** cards render dimmed-but-readable; uncomment the last JS line to force-show all.

Open `reveal-card.html` to see it run. Copy the `.sil-reveal` block + its `<script>` into a slide.
