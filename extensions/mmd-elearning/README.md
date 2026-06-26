# MMD E-learning Governance Extension (optional)

> **This is an optional extension, not the universal default.** The core Slide Interaction Layer
> (taxonomy + components + decision rules) stays general-purpose and unchanged. This folder adds a
> **governance layer** for teams producing **regulated / compliance e-learning and courseware**
> (e.g. MMD-style modules) where completion, evidence, and consistency must be provable.
>
> If you are just making slides, ignore this folder entirely. Nothing here changes the base behavior.

## What this extension adds (spec only, in this release)

This is **documentation/specification only** — there is no new runtime code, no new components, and
no change to the core taxonomy IDs (`P0`–`P8`). It defines *how* to apply the existing layer under
governance, and the operating SOPs around it.

| Doc | Purpose |
| --- | ------- |
| [`mmd-process-terms.md`](mmd-process-terms.md) | Shared vocabulary: module/PL/topic naming, storyboard, voice-over, quiz, completion, SCORM/evidence terms. |
| [`media-assembly-sop.md`](media-assembly-sop.md) | SOP for turning a storyboard + assets into verified media (VO master, EDL, B-roll, QC, canonical masters). |
| [`interaction-decision-sop.md`](interaction-decision-sop.md) | How to choose interactions in governed e-learning (gating defaults ON, required vs optional, trackable states). |
| [`s0-board-governance.md`](s0-board-governance.md) | The S0 governance board: lanes, statuses, blocker taxonomy, how scan findings become tasks. |
| [`cowork-operating-loop.md`](cowork-operating-loop.md) | The end-to-end loop for an AI maintainer running e-learning governance, with guardrails. |

## How it relates to the core

- It **reuses** the core patterns (`P5` Hotspot, `P6` Quiz, `P7` Branching, etc.) and their existing
  completion rules — it does **not** add or rename pattern IDs.
- It **tightens defaults** for the governed context (e.g. completion-gating ON, higher interactivity
  budget for training) — as guidance, not as code, in this release.
- Runtime (actual gating components, a governance manifest) is intentionally **out of scope here**
  and reserved for a later loop, so the universal core stays stable.

## How to "opt in"

Point your agent at this folder *in addition to* the core skill, only when you are producing
governed e-learning:

```
Read ./slide-interaction-layer/SKILL.md as a skill.
Also read ./slide-interaction-layer/extensions/mmd-elearning/ for e-learning governance.
Operate in E-learning Governance Mode (see MAINTAINER.md).
```

For everyday slide decks, do **not** load this folder.

## Status

- **v0.1.5 (this):** spec docs only.
- **Later (proposed):** opt-in completion-gating runtime, a per-deck governance manifest, and a
  SCORM/xAPI mapping — each as its own additive patch, never altering the universal core.
