# Changelog

All notable changes to **Slide Interaction Layer** are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). Releases through the `0.1.x`
line are patch-level: additive documentation and packaging, with **no changes to the core taxonomy
IDs (`P0`–`P8`), components, or runtime behavior**.

## [Unreleased]

### Planned
- **v0.3.1** — optional machine-readable `ontology.json` sidecar (schema designed against real decks).
- **patterns** — timeline, before/after slider, drag-match, ranking.
- **v1.0** — installable plugin distribution; theme-aware component styling.

## [0.3.0] — 2026-06-26
### Added
- **Element Ontology** semantic layer in `ontology/` (docs only) — classifies *what* content is
  (`E1`–`E15`) before choosing *how* to present it (`P0`–`P8`):
  `README.md`, `element-ontology.md` (15 element types), `element-to-pattern-map.md`
  (mapping + gating justification), `metadata-format.md`, `audit-checks.md`.
- `SKILL.md` gains an **Ontology-first** flow (recommended for learning/courseware, optional for
  everyday decks): classify → map → select (taxonomy) → gate.
- README **Element ontology** section + roadmap update.
### Notes
- Element IDs are `E`-prefixed and do not collide with `P0`–`P8`. Docs only — **no runtime, no
  components, no taxonomy ID changes**. Optional; core decks are unaffected. The `ontology.json`
  sidecar is deferred to v0.3.1.

## [0.2.0] — 2026-06-26
### Added
- **Optional completion-gating runtime** `gating/gate.js` — blocks forward navigation on a slide
  until its required interaction is complete. **Opt-in** (`data-sil-gating="on" | "training"`),
  **off by default**, **fail-open** (no JS → fully navigable), engine-agnostic, accessible
  (`aria-disabled` next control, focus to the incomplete activity, polite live hint), backward
  navigation always allowed. Reads existing component signals — **no component changes**.
- `gating/README.md` — how to enable, modes, gateable patterns, overrides, a11y, fail-open.
- `examples/gated-training-demo.html` — a gated deck exercising all five gateable patterns
  (reveal cards, hotspot, quiz, branching, calculator) in `training` mode.
- README **Completion gating** section + gallery entry; roadmap marks v0.2 delivered.
### Notes
- Calculator uses strict `user_changed` (does not count the on-load worked example); quiz training
  default is `answered_correctly`. No core taxonomy ID changes; core decks remain ungated.
### Compatibility
- Backward compatible. Decks without `data-sil-gating` (and without `gate.js`) behave exactly as
  v0.1.6 — verified.

## [0.1.6] — 2026-06-26
### Added
- `CHANGELOG.md` (this file) documenting the full `0.1.x` history.
- README pointer to the changelog.

## [0.1.5] — 2026-06-26
### Added
- Optional `extensions/mmd-elearning/` — **spec-only** governance layer for regulated e-learning:
  `README.md`, `mmd-process-terms.md`, `media-assembly-sop.md`, `interaction-decision-sop.md`,
  `s0-board-governance.md`, `cowork-operating-loop.md`.
- README **Extensions** section; MAINTAINER **E-learning Governance Mode** section.
### Notes
- No runtime, no component changes, no core taxonomy ID changes. Extension is opt-in.

## [0.1.4] — 2026-06-26
### Added
- `INSTALL.md` with three beginner-friendly install paths (local agent, Claude plugin, org
  marketplace) and a README pointer to it.

## [0.1.3] — 2026-06-26
### Added
- Top-of-README **Quickstart (under 5 minutes)** with a 3-step path and an at-a-glance pattern
  cheat-sheet.
### Changed
- Renamed the lower "Quick start" to **Example prompt (fuller)** so there is one clear entry point.

## [0.1.2] — 2026-06-26
### Added
- `MAINTAINER.md` (maintainer operating loop + Definition of Done).
- **Maintainer Mode** section in `SKILL.md`.
- `.claude-plugin/plugin.json` manifest, making the repo an installable plugin.

## [0.1.1] — 2026-06-26
### Added
- Second demo deck `examples/ai-workflow-for-smes.html` (taxonomy applied to a real use case).
- README **Demo Gallery** section linking both example decks.

## [0.1.0] — 2026-06-26
### Added
- Initial release: interaction **taxonomy** (`P0`–`P8`) and **decision rules**.
- Eight working **components** (reveal-card, accordion, tooltip, modal, hotspot, quiz, branching,
  calculator), each with a static fallback.
- `examples/demo-deck.html` (one slide per pattern), `prompts/use-with-frontend-slides.md`,
  `README.md`, `SKILL.md`.

[Unreleased]: https://github.com/fidos777/slide-interaction-layer/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/fidos777/slide-interaction-layer/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/fidos777/slide-interaction-layer/compare/v0.1.6...v0.2.0
[0.1.6]: https://github.com/fidos777/slide-interaction-layer/compare/v0.1.5...v0.1.6
[0.1.5]: https://github.com/fidos777/slide-interaction-layer/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/fidos777/slide-interaction-layer/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/fidos777/slide-interaction-layer/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/fidos777/slide-interaction-layer/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/fidos777/slide-interaction-layer/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/fidos777/slide-interaction-layer/releases/tag/v0.1.0
