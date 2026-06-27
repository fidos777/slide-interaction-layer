# SBAT — Phase 1 planning notes

> **Internal planning only — not runtime, not plugin behavior.** These documents are Phase 1
> authoring/governance *notes* under [`SBAT-ADR-001`](../../decisions/SBAT-ADR-001.md). They describe
> a pre-commit authoring governor that does **not** ship as part of this plugin and is **not**
> executed by any deck at runtime. This repo is distributed downstream as a plugin/marketplace
> package; nothing in `docs/sbat/` is plugin/runtime code. No code, schema, or validator exists yet.

> **M1 prototype now exists:** the first implementation surface lives at
> [`../../sbat/m1-screen-c.html`](../../sbat/m1-screen-c.html) (one-slide MMD planning). These docs
> remain the planning record behind it.

## What SBAT is

SBAT is a **pre-commit authoring governor** (per ADR Decision 3): it sits *before* the build/runtime
repo and confirms that every text, quiz option, interaction, asset, and slide scope came from an
approved source rather than being session-fabricated.

```
slide-interaction-layer = the pattern factory   (reusable engine — this repo)
SBAT                    = the factory control panel (authoring + governance — these notes)
cidb-k1pl1t1-prototype  = the first customer order  (CIDB delivery/test — NOT touched here)
```

## The governed remediation loop (operating model, ADR Decision 5)

```
audit finding → source check → limited edit → diff → validation → commit → unresolved items stay open
```
AI accelerates; humans decide. Unresolved items stay open rather than being silently closed.

## The six M1 governance fields (ADR Decision 6)

Screen C / M1 carries only these — nothing more:

1. Slide implementation status
2. Interaction pattern
3. Source-backed content flag
4. Quiz option governance
5. Repo patch preview
6. Human decision gate

Field-level notes: [`m1-schema-notes.md`](m1-schema-notes.md).

## These notes

| File | Purpose |
| ---- | ------- |
| [`m1-schema-notes.md`](m1-schema-notes.md) | Draft governance contract for the six M1 fields (notes, **not** a JSON Schema). |
| [`validator-notes.md`](validator-notes.md) | The two ADR-proven checks + the report-only doctrine (notes, **not** code). |
| [`remediation-example.md`](remediation-example.md) | Q2 and `demo_scope` worked examples of the loop (illustration only). |

## Boundaries (from the ADR non-goals)

No full LMS · no Courseware.my wrapper · no multi-client platform · no automated final ID/QA
decision · **no CIDB content/assets in this repo** · **`cidb-k1pl1t1-prototype` is not touched** ·
no `/sbat` app. Only ADR Phase 1 (docs + schema notes) is in motion; Phases 2–4 are direction only.
