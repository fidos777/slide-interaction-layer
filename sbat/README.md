# SBAT — M1 prototype (one-slide MMD planning)

A tiny, single-file **authoring/planning surface** for SBAT (the pre-commit authoring governor from
[`SBAT-ADR-001`](../decisions/SBAT-ADR-001.md)). M1 plans **one slide** end-to-end for MMD
production and produces a handoff record. Planning notes live in [`../docs/sbat/`](../docs/sbat/).

> **Not runtime / not plugin behavior.** This is an internal planning tool. It is not wired to any
> deck build, not part of the distributed plugin, and does **not** touch `cidb-k1pl1t1-prototype`.
> Single file, no framework, no backend, no localStorage — export-to-JSON only.

## Files

| File | Purpose |
| ---- | ------- |
| [`m1-screen-c.html`](m1-screen-c.html) | The whole prototype — open in any browser. Screen C, 8 fields, live JSON, export, sample-load. |
| [`sample-slide.json`](sample-slide.json) | One seed slide record (illustration; no CIDB content). |

## Use it

Open `m1-screen-c.html` in a browser. Fill the eight fields → watch the live JSON record build →
**Export JSON** for handoff, or **Load sample** to see a populated example.

## Screen C — the eight fields

1. Slide identity / implementation status (with a derived status badge)
2. Voice-over (VO)
3. On-screen text *(AI-derived — pasted/edited by a human in M1)*
4. MMD graphics / production notes
5. Interaction metadata — **M1 selectable patterns** P0–P11 (auto-fills the completion rule)
6. Source / review status
7. Owner + decision gate
8. Handoff / PDF preview — **placeholder** (use Export JSON for now)

**Register Cross-Reference** *(AMEND-K1 × Laila convergence — one slide carries both)*:

- `amend_note` — AMEND-K1 governance / blocker note
- `laila_note` — Laila production / visual direction
- `convergence_type` — `none` · `production-only` · `governance-only` · `both-registers` · `character-swap` · `quiz-gap` · `asset-gap` · `interaction-spec`
- `provenance` — `confirmed-from-file` · `inferred` · `review` · `provisional`

Sample data is lightly anonymized — no full CIDB content is stored here.

## First-class uncertainty

**REVIEW** and **PROVISIONAL** are real choices for status, source, and decision gate, so an
unratified slide (e.g. `s06`) keeps moving instead of being blocked by old workshop gates.

## Not in M1 (deferred)

No multi-slide list, batch, AI generation/video, PDF library, repo-commit wiring, LMS, Courseware.my
wrapper, marketplace, or multi-client dashboard. Only Phase-1 (ADR) is in motion.
