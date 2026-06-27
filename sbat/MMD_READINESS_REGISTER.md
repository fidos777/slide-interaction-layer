# MMD Readiness Register

> Companion to `sbat/MMD_READINESS_REGISTER.csv`. Seeded from the three verified SBAT M1 pilot records.

## Status

- MMD-0 register only.
- Documentation / data bridge only.
- Not an app.
- Not an importer.
- Not final MMD build.
- Seeded with 3 verified SBAT M1 pilot records only.

## Purpose

This register is a small bridge from the SBAT M1 pilot records to MMD planning. It tells the MMD team, per slide:

- **what can be built now** (final production allowed);
- **what can be shell-only** (structure/layout/container allowed, not final content);
- **what is blocked** (no final build until a human decision clears it);
- **who must decide** (the owner who must ratify);
- **what must not be finalised yet** (the explicitly blocked work).

It does not import data, does not build slides, and does not approve anything. AI suggests; humans ratify.

## Readiness States

- **READY_FOR_MMD** — fully cleared; final MMD production may proceed.
- **READY_FOR_SHELL_ONLY** — the interaction shell / layout / container may be built, but **not** the final content.
- **REVIEW_REQUIRED** — discussion, shell concept, and requirement listing only; **no** final lock until reviewed.
- **BLOCKED_PENDING_SB** — no final build; awaiting SB (subject-matter) ratification.
- **BLOCKED_PENDING_ASSET** — no final build; awaiting a **confirmed** missing approved asset. (Not applied to any pilot record in this register — see PL5T3 note.)

## Build Policy

1. No final MMD without an SBAT gate.
2. `BLOCKED_PENDING_SB` means no final build.
3. `REVIEW_REQUIRED` allows discussion / shell only, not final lock.
4. `READY_FOR_SHELL_ONLY` allows structure, not final content.
5. `READY_FOR_MMD` allows final production.
6. Production-only notes may proceed only if no governance blocker exists.
7. Every final slide must trace to a source note or an approved decision.

## Register

| record_id | deck | slide | pattern | gate | readiness_state | owner | MMD action | build_status |
|-----------|------|-------|---------|------|-----------------|-------|------------|--------------|
| PL1T3-s2 | T3 | s2 | P0 | BLOCKED_PENDING_SB | BLOCKED_PENDING_SB | Bariah | prepare static shell only; wait for SB/persona confirmation | NOT_STARTED |
| PL3T1-s28 | T1 | s28 | P6 | BLOCKED_PENDING_SB | READY_FOR_SHELL_ONLY | Bariah | prepare quiz shell only; wait for quiz content | NOT_STARTED |
| PL5T3-s4 | T3 | s4 | P11 | REVIEW | REVIEW_REQUIRED | Laila + Bariah | prepare drag-match treatment discussion; do not mark asset as missing unless confirmed | NOT_STARTED |

## Pilot Record Notes

- **PL1T3 s2 — character swap (P0).** The on-screen presenter does not match the approved character bank. Gate is `BLOCKED_PENDING_SB`. MMD may prepare a **static shell / placeholder treatment only**; the final character lock and final VO/persona lock are blocked until SB confirms the ratified persona. Owner: Bariah.

- **PL3T1 s28 — quiz gap (P6).** The quiz screen is an empty/placeholder. Gate is `BLOCKED_PENDING_SB`; readiness is `READY_FOR_SHELL_ONLY`. MMD may prepare the **quiz shell / layout / interaction container**, but the final stem, options, correct answer, feedback and scoring are blocked until ratified quiz content is supplied. Owner: Bariah.

- **PL5T3 s4 — visual asset / drag-match review (P11).** The storyboard specifies real photographic images per drag-match pair; imagery is not yet selected. Gate is `REVIEW`; readiness is `REVIEW_REQUIRED`. MMD may prepare the **drag-match treatment discussion, shell concept, and asset requirement list**. **PL5T3 remains REVIEW_REQUIRED / REVIEW and is not BLOCKED_PENDING_ASSET, because missing approved assets have not been confirmed** — the real-image *requirement* is confirmed from file, but the *absence of an approved asset* is not. Owner: Laila + Bariah.

## Next Step

- Use this register in **Bariah / Laila validation** of the SBAT M1 pilot flow.
- **Do not expand to all AMEND / Laila rows** until the source-lane schema is ratified.
- After validation, **MMD-1** may expand the register **batch by batch** under the ratified schema.
