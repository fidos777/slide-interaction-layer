# Cowork Operating Loop — E-learning Governance (spec)

How an AI maintainer (Cowork / Claude Code) should operate when running governance for a regulated
module. This is the governed counterpart to the repo's base `MAINTAINER.md` loop. Spec only — it
describes behavior; it does not grant the agent permission to publish.

## The loop

```
REVIEW → SCAN → ROUTE → ASSEMBLE → QC → GATE → EVIDENCE → REPORT
```

1. **Review** — read the storyboard decks and the module's current state.
2. **Scan** — detect blockers (character/consistency, quiz completeness, VO rule, navigation, stale
   naming). Output structured findings.
3. **Route** — turn findings into a **dry-run** S0 board draft (see `s0-board-governance.md`).
4. **Assemble** — follow `media-assembly-sop.md` to build/verify media from masters.
5. **QC** — run the media QC checklist; nothing advances on a failed check.
6. **Gate** — run the packaging/release gate (delivery files current, package valid + under limit).
7. **Evidence** — assemble the audit pack (statuses, checklist, screenshots/logs).
8. **Report** — what changed, why, verification, risks, next highest-value task.

Repeat per module/topic. Prefer many small verified steps over one big change.

## Definition of done (per loop)

Tie to `s0-board-governance.md`'s module DoD: no open blockers, required interactions gated with
fallbacks, media QC + package gate green, evidence assembled, naming clean.

## Guardrails (never without explicit human approval)

- Do **not** publish, upload to an LMS, push, tag, or create releases.
- Do **not** write to a live board, spreadsheet, or system of record — produce drafts only.
- Do **not** touch credentials or admin consoles.
- Do **not** alter the **core** taxonomy, components, or pattern IDs from inside this extension.
- When a step crosses a guardrail, **stop and hand off** (e.g. provide a script or a draft to run),
  exactly as the base `MAINTAINER.md` requires.

## Reporting format

Every governance report includes: **changed · why it matters · verified · risks · next**.
Keep evidence reproducible (record fingerprints, checklist results, and the exact checks run).
