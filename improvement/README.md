# Recursive Repository Improvement (RRI)

A repo-improvement layer that **closes the loop between releases**: each release measures itself
(audit + scores + reviews), stores the results, and the weakest result becomes the input that
prioritizes the next release.

```
Release N → measure (audit + score + review) → artifacts → prioritize → Release N+1
   ▲                                                                         │
   └───────────────────────────── repeats ───────────────────────────────────┘
```

This is **docs/manual** in v0.4.0 (automation deferred to v0.4.1). It governs the whole repo, so it
lives top-level alongside `gating/` and `ontology/`.

## How it relates to Compound Engineering

- **CORD (compound engineering)** makes each change leave reusable assets (the "how").
- **RRI (this)** measures whether changes improved things and routes the next loop (the closed loop).
- RRI *consumes* CORD's artifacts (ADRs, CHANGELOG, push-script checks) and *produces* the next
  release's priority. See [`../docs/compound-engineering.md`](../docs/compound-engineering.md).

## The pre-release gate (run before cutting any tag)

```
LOAD   → repo-memory-loading-checklist.md   (read state; live vs local freshness)
AUDIT  → release-audit-checklist.md          (HARD gate; blockers stop the release)
SCORE  → compound-scorecard.md               (8 axes, 1–10; deltas vs previous)
VERIFY → ontology-mapping-verifier.md + example-quality-score.md
REVIEW → decision-log-review.md              (ADR present if user-facing)
ROUTE  → record weakest axis as next release's candidate priority
DECIDE → READY or BLOCKED (only READY proceeds to the push script)
```

Safety checks (AUDIT) are **fail-closed**; scores (SCORE/VERIFY) are advisory but a regression needs
a written reason. The full loop is also documented in [`../MAINTAINER.md`](../MAINTAINER.md).

## Artifacts

| File | Role |
| ---- | ---- |
| [`release-audit-checklist.md`](release-audit-checklist.md) | mechanical pre-release safety (hard gate) |
| [`compound-scorecard.md`](compound-scorecard.md) | 8-axis scoring template + guide |
| [`ontology-mapping-verifier.md`](ontology-mapping-verifier.md) | ontology E/P integrity checks |
| [`example-quality-score.md`](example-quality-score.md) | per-example deck rubric (0–100) |
| [`decision-log-review.md`](decision-log-review.md) | ADR hygiene review |
| [`repo-memory-loading-checklist.md`](repo-memory-loading-checklist.md) | deterministic context load order |
| [`scorecards/`](scorecards/) | one filled scorecard per release (traceable over time) |

## Status

- **v0.4.0 (this):** docs/manual gate + the first real scorecard (`scorecards/v0.4.0.md`).
- **v0.4.1 (planned):** `run-gate.sh` to automate the mechanical AUDIT checks + scaffold a blank
  scorecard.
