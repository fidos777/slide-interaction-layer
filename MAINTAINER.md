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

## Roadmap reference

- **v0.2** — completion-gating (block "next" until e.g. all hotspots clicked), per-slide metadata.
- **v0.3** — more patterns: timeline, before/after slider, drag-match, ranking.
- **v1.0** — installable plugin distribution; theme-aware component styling.
