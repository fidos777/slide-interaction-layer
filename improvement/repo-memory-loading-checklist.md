# Repo memory loading checklist

Makes "load repo memory" deterministic for any agent or human. Run as the **LOAD** step of the
pre-release gate, and whenever an agent starts acting as maintainer.

## Read order (top to bottom)

1. `SKILL.md` — what the layer is + the ontology-first / decision flow.
2. `MAINTAINER.md` — the maintainer loop, CORD, and the RRI pre-release gate.
3. `docs/compound-engineering.md` — the operating model.
4. `decisions/` — all ADRs (the durable decisions; read newest last).
5. `CHANGELOG.md` — what shipped, newest first.
6. `README.md` — public framing, quickstart, install, layers.
7. `ontology/` — element catalog + mapping (for learning/courseware work).
8. `gating/` — the opt-in runtime contract.
9. `extensions/` — domain layers (e.g. MMD e-learning).
10. `improvement/` — this gate + the latest `scorecards/`.

## Freshness check (live vs local)

- [ ] Compare the live `main` (`raw.githubusercontent.com/<owner>/<repo>/main/...`) against local —
      confirm which version is actually published before acting.
- [ ] Confirm the latest tag and the latest `scorecards/<version>.md` agree on the current version.
- [ ] Note any **unpushed** staged patches/bundles so you don't double-ship or assume state.

## "You are here" summary (produce after loading)

State back, in one block: current version, the layers present, the **weakest axis** from the latest
scorecard, and the **next planned loop**. This confirms context is loaded and gives the next action.

## Output
A short loaded-context confirmation the maintainer can act on (version, state, next priority).
