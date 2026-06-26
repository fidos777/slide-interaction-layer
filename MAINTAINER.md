# Maintainer Operating Loop

This file tells an AI maintainer (Cowork / Claude Code) how to work on this repository like a
steady team member, not a blur intern. Pair it with the **Maintainer Mode** section in `SKILL.md`.

## Goal

Make **Slide Interaction Layer** the best open interaction-design system for AI-generated HTML
slide decks — clear taxonomy, dependable components, and examples that prove it works.

Current target: progress the repo toward **v0.2** (completion-gating + per-slide metadata polish,
then additional patterns).

## Loop

```
PLAN → IMPLEMENT → VERIFY → CRITIQUE → IMPROVE → COMMIT → (RELEASE only if user-facing)
```

Each pass: pick the single highest-impact change, make the smallest safe version of it, verify it,
then commit. Prefer many small correct commits over one big risky one.

## CORD Method (Compound Engineering)

Run each loop so it compounds — every change leaves behind a reusable asset. CORD is the cycle:

1. **Classify** — name what the work *is* before acting (area, element/pattern, kind of change).
2. **Operationalize** — make the smallest safe change, with a verification step and, if shipping, a
   repeatable push script.
3. **Reuse** — extend existing patterns/components/scripts/conventions; add capability opt-in and
   additive so nothing it touches must change.
4. **Document** — record what changed and *why* (CHANGELOG; an ADR in `decisions/` for real
   decisions; README/SKILL updates).

CORD is the "how"; the Loop above is the "when". Full model: [`docs/compound-engineering.md`](docs/compound-engineering.md).
Decision records: [`decisions/`](decisions/).

## Definition of Done (per loop)

A change is "done" only when all of these hold:

- No broken links in README / SKILL.md / docs.
- No temp files committed (e.g. `ziIs4QgH`, `.DS_Store`, editor scratch).
- No nested archives committed (`.zip`, `.bundle`, `.tar`, `.gz`, `.7z`, `.rar`).
- Every example still opens and its interactions still fire (verify, don't assume).
- README matches the actual implementation (no stale claims).
- `SKILL.md` remains agent-usable (frontmatter intact, decision rules consistent).
- `.claude-plugin/plugin.json` version bumped if the change is user-facing.
- Release notes updated if a tag is cut.

## Guardrails (never do without explicit user approval)

- Push to a remote, create/delete releases or tags, or change repo visibility.
- Touch credentials, tokens, or the org admin console.
- Force-push or rewrite published history.
- Delete user data or existing release assets.

When the next step crosses a guardrail, stop and produce a handoff (what to run, e.g. a push
script) instead of doing it.

## Report format (end of every loop)

- **Changed:** what was modified.
- **Why:** the impact toward the goal.
- **Verified:** the exact checks run and their results.
- **Risks:** anything to watch.
- **Next:** the next highest-value task.

## E-learning Governance Mode

When the task is producing **regulated e-learning / courseware** (not everyday slides), operate in
this mode in addition to the base loop. It is defined by the optional extension
`extensions/mmd-elearning/` — load that folder and follow its specs.

- **Loop:** `REVIEW → SCAN → ROUTE → ASSEMBLE → QC → GATE → EVIDENCE → REPORT`
  (see `extensions/mmd-elearning/cowork-operating-loop.md`).
- **Tighter defaults:** completion-gating ON, required interactions tracked, fallbacks mandatory
  (see `extensions/mmd-elearning/interaction-decision-sop.md`).
- **Tracking surface:** the S0 readiness board, routed **dry-run / read-only**
  (see `extensions/mmd-elearning/s0-board-governance.md`).
- **Extra guardrails:** never publish/upload to an LMS, never write to a live board or system of
  record, and never alter the **core** taxonomy/components from inside the extension — hand off
  instead. (These add to, never relax, the base guardrails above.)

This mode is **opt-in**. For normal decks, ignore it and use the base loop only.

## Pre-release RRI gate (run before cutting any tag)

Recursive Repository Improvement: every release measures itself and the result prioritizes the next.
Run this loop before each release; full artifacts in [`improvement/`](improvement/).

```
LOAD   → improvement/repo-memory-loading-checklist.md   (state; live vs local freshness)
AUDIT  → improvement/release-audit-checklist.md          (HARD gate; blockers stop the release)
SCORE  → improvement/compound-scorecard.md               (8 axes, 1–10; deltas vs previous)
VERIFY → improvement/ontology-mapping-verifier.md + improvement/example-quality-score.md
REVIEW → improvement/decision-log-review.md              (ADR present if user-facing)
ROUTE  → record the weakest axis as the NEXT release's candidate priority
DECIDE → READY or BLOCKED (only READY proceeds to the push script)
```

- **AUDIT is fail-closed** (a red audit never ships); **SCORE/VERIFY are advisory** but a regression
  needs a written reason.
- **ROUTE closes the loop:** the weakest axis becomes the next loop's CORD *Classify* input.
- Save a filled scorecard per release in `improvement/scorecards/<version>.md`.

## Roadmap reference

- **v0.2** — completion-gating (block "next" until e.g. all hotspots clicked), per-slide metadata.
- **v0.3** — more patterns: timeline, before/after slider, drag-match, ranking.
- **v1.0** — installable plugin distribution; theme-aware component styling.
