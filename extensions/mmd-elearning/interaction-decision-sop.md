# Interaction Decision SOP — governed e-learning (spec)

How to apply the **core** interaction taxonomy when the deck is regulated courseware. This does not
change any pattern IDs (`P0`–`P8`) or the base decision rules — it **tightens the defaults** for the
governed context. Guidance only; no runtime here.

## What changes vs. a normal deck

| Aspect | Normal deck (core default) | Governed e-learning (this SOP) |
| ------ | -------------------------- | ------------------------------ |
| Interactivity budget | ≤ ~40% | up to ~70% (it's a training module) |
| Completion gating | off by default | **on** for required screens |
| Interaction status | optional | often **required** + tracked |
| Fallback | recommended | **mandatory** (accessibility + audit) |

## Choosing the pattern

Use the same core selection logic (intent → pattern). Typical governed mappings:

- **Concept screens** → `P1` Reveal Cards or `P0` Static.
- **Diagram / process / equipment** → `P5` Hotspot, gated `all_hotspots_clicked`.
- **Decision / scenario / "what would you do"** → `P7` Branching, gated `reached_an_ending`.
- **Knowledge check / end-of-topic** → `P6` Quiz, gated `answered_correctly`, with a recorded score.

Keep **one primary interaction per screen**. Do not stack. Do not hide *required* content behind a
click — hidden content stays supplementary.

## Required vs optional interactions

- **Required:** must be completed to progress; contributes to completion/score. Gate the "next"
  control on its completion rule.
- **Optional:** enrichment; never blocks progress; not tracked for compliance.

Mark each interaction's status explicitly in the screen's metadata comment (extend the core
`interaction / reason / completion_rule / fallback` with `required: true|false`).

## Mapping completion rules → trackable states (spec)

For a future SCORM/xAPI wrapper, the existing completion rules map cleanly:

| Core completion rule | Governed meaning | LMS field (target) |
| -------------------- | ---------------- | ------------------ |
| `all_hotspots_clicked` | screen explored | progress / completion |
| `answered_correctly` | check passed | success_status + score |
| `reached_an_ending` | scenario resolved | progress / completion |
| all required screens done | module complete | completion_status = completed |
| score ≥ pass threshold | module passed | success_status = passed |

This table is a **specification** for a later runtime loop; nothing computes it yet.

## Accessibility & audit (non-negotiable in governance)

Keyboard-operable, visible focus, `prefers-reduced-motion` honored, and a **static fallback** for
every interaction (so the content is provable even if JS fails). Each required interaction must be
auditable: its completion rule and status are stated in the screen metadata.
