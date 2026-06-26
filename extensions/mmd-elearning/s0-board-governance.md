# S0 Board Governance (spec)

The **S0 board** is the single tracking surface for a governed module's readiness. It turns review
findings into accountable tasks. This document specifies how it works; it does not write to any real
board (routing is **dry-run / read-only** until a human approves).

## Lanes

| Lane | Holds |
| ---- | ----- |
| Content | storyboard, on-screen text, VO scripts |
| Interaction | required/optional interactions, completion rules |
| Media | VO master, EDL, B-roll, plates, QC |
| Assessment | quizzes, pass threshold, scoring |
| Packaging | delivery files, SCORM/xAPI package, size |
| Evidence | audit artifacts, sign-off |

## Task status

`open → in_progress → blocked → done`. Every task carries: lane, owner, the source finding
(deck + screen + rule), and a blocker flag.

## Blocker taxonomy

- **Character/consistency** — drifting names/roles vs the character bank.
- **Quiz completeness** — empty/placeholder quiz, missing correct answer or feedback, bad naming.
- **VO/script** — spoken-number rule broken ("PL kosong satu"), VO/text mismatch.
- **Navigation** — missing/inconsistent back/next/menu.
- **Stale naming** — leftover module/PL/topic codes from a copied deck.
- **Media** — master/derivative confusion, failed QC, stale package.

## From findings to tasks (routing rules)

1. A deck scan produces structured **findings** (deck, screen, rule_id, severity).
2. Dedupe: same deck + screen + rule_id collapses into **one** task (merge provenance).
3. Exclude PASS findings. Keep interaction cues as **pending** notes, not active tasks.
4. Map each finding → lane + owner + blocker flag. Leave every task `status=open`.
5. **Read-only:** produce a draft (markdown/CSV) for human review. Never write to a live board or
   spreadsheet automatically.

## Definition of done (per module)

- No open blockers in any lane.
- All required interactions have completion rules + fallbacks.
- Media QC passed; package gate green; delivery files current.
- Evidence assembled (statuses, checklist, screenshots/logs).
- Naming hygiene clean (see `mmd-process-terms.md`).

## Why read-only first

Governance must be auditable and reversible. The board draft is a recommendation a human accepts;
the AI maintainer prepares it but does not mutate systems of record without approval
(see `cowork-operating-loop.md`).
