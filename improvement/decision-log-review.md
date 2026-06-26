# Decision log review

Keeps the ADRs (`decisions/`) honest and complete. Run during **REVIEW** before any user-facing
release.

## Checks

- [ ] **Decision recorded** — this release either adds an ADR for its decision, or carries an explicit
      "no architectural decision needed" note in the CHANGELOG entry.
- [ ] **Numbering contiguous** — ADR files are `ADR-0001…ADR-NNNN` with no gaps or duplicates.
- [ ] **Status valid** — each ADR is `Proposed`, `Accepted`, or `Superseded by ADR-NNNN`.
- [ ] **Superseding is explicit** — a reversed decision marks the old ADR `Superseded by …` rather
      than deleting it (history is preserved).
- [ ] **Required fields present** — every ADR has Status, Date, Context, Decision, Consequences.
- [ ] **No orphans** — each ADR maps to a real capability/decision in the repo.
- [ ] **Links resolve** — ADRs referenced from `docs/compound-engineering.md`, README, MAINTAINER all
      resolve.

## When is an ADR required?

Write an ADR when a change sets or reverses a **durable direction** — a public contract (IDs,
file layout), a default (opt-in vs required), a deferral, or a cross-cutting convention. Routine
docs/example/patch work does **not** need an ADR; note "no decision needed" in the changelog instead.

## Output
Review notes + any gaps to fill before release. A missing-but-required ADR is a **blocker**.
