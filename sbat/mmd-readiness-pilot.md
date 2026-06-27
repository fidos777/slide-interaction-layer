# MMD readiness pilot — three convergence samples

A small, human-readable companion to the three SBAT planning records under
[`samples/`](samples/). It explains what each record represents, why each decision gate was
chosen, and how the records map to MMD production readiness. Decision recorded in
[`../decisions/SBAT-ADR-002.md`](../decisions/SBAT-ADR-002.md).

> **Where richer language is allowed.** This document may use readable readiness phrasing
> (e.g. *"blocked — awaiting SB"*, *"in review"*). The JSON records do **not**: they carry only
> the committed M1 enum values from [`m1-screen-c.html`](m1-screen-c.html). Any label here that is
> not a committed enum stays here, in prose, and never enters the JSON.

## The three samples

| Sample | `convergence_type` | `pattern` | `decision_gate` (enum) | `provenance` (enum) | Readiness (prose label) |
| ------ | ------------------ | --------- | ---------------------- | ------------------- | ----------------------- |
| [`pl1t3-s2`](samples/pl1t3-s2-character-swap.sample.json) | `character-swap` | `P0` (Static) | `BLOCKED_PENDING_SB` | `confirmed-from-file` | Blocked — presenter swap awaiting SB |
| [`pl3t1-s28`](samples/pl3t1-s28-quiz-gap.sample.json) | `quiz-gap` | `P6` (Quiz) | `BLOCKED_PENDING_SB` | `confirmed-from-file` | Blocked — quiz items awaiting SB |
| [`pl5t3-s4`](samples/pl5t3-s4-visual-asset.sample.json) | `asset-gap` | `P11` (Drag-Match) | `REVIEW` | `confirmed-from-file` | In review — imagery to be examined |

The "Readiness (prose label)" column is illustrative phrasing for humans only. It is **not** a field
in the record and must not be copied into the JSON.

## Why each gate

**`pl1t3-s2` — character swap (blocked, awaiting SB).** The on-screen presenter does not match the
approved character bank. The mismatch is read directly from the storyboard, so provenance is
`confirmed-from-file`; but the correct persona is a human-ratified input from SB Bariah, so the finding
stays open at `BLOCKED_PENDING_SB`. A static slide (`P0`) carries no completion rule (`none`).

**`pl3t1-s28` — quiz gap (blocked, awaiting SB).** The quiz screen is empty/placeholder: no stem,
options, correct-answer mark, or feedback in the approved source. The gap is confirmed from the deck
(`confirmed-from-file`), but only SB-ratified question content can clear it, so it holds at
`BLOCKED_PENDING_SB`. As a quiz (`P6`), its completion rule is `answered_correctly`.

**`pl5t3-s4` — asset gap (in review, not blocked-on-asset).** The storyboard *requires* real
photographic images for each drag-match pair. That requirement is confirmed from the file
(`confirmed-from-file`) — but a confirmed *requirement* is not a confirmed *absence* of an approved
asset. Using `BLOCKED_PENDING_ASSET` would over-claim a missing-asset finding we do not have. So the
gate is `REVIEW`: available imagery still has to be examined before any block is asserted. As a
drag-match (`P11`), its completion rule is `all_pairs_matched_correctly`.

## The distinction this pilot records

The asset case is the reason the pilot exists. SBAT must not turn *"the source asks for real images"*
into *"approved real images are confirmed missing."* The first is a requirement read from the file and
belongs in `REVIEW`; the second would be a `BLOCKED_PENDING_ASSET` finding, and we do not have the
evidence for it. Keeping that line clean is the governance value here.

## Scope note

These are anonymized illustration records — no full CIDB content. The pilot adds no schema, taxonomy,
validator, importer, parser, loader, or UI; it rides on the committed M1 vocabulary only. See
[`../decisions/SBAT-ADR-002.md`](../decisions/SBAT-ADR-002.md) for the recorded decision.
