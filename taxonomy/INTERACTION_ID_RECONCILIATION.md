# INTERACTION_ID_RECONCILIATION

- **Status:** reference / reconciliation record — docs-only
- **Sprint:** M1.12A
- **Authoritative source:** live SBAT/MMD-0 register at current HEAD
- **Draft under review:** uploaded candidate taxonomy / `interactivity-taxonomy-sbat.html`
- **Doctrine:** AI suggests; humans ratify. **No production mapping until ratified** — no candidate ID becomes a production `P#` until reconciled and ratified.

---

## 0. Why this file exists

- **Two P-numbering systems exist.** The live SBAT/MMD-0 register has one set of `P#` IDs; the uploaded candidate taxonomy draft has a different set.
- **They conflict.** The same `P#` token means different things in each system.
- **The dangerous conflict is `P11`.** Live = `Drag-Match` (`PL5T3-s4`); uploaded draft = `Timeline Navigation`. Treating the draft as authoritative would silently re-point `P11` and mis-handoff `PL5T3-s4` to MMD.
- **The live MMD-0 register already shipped**, therefore the **live register namespace wins**. It is the authoritative production namespace.
- The **candidate taxonomy must not enter the repo as authoritative production mapping** until reconciled and ratified.
- This file exists to **prevent fake certainty / wrong MMD handoff** — to stop a draft numbering scheme from being mistaken for the shipped one.

## 1. Authoritative namespace — LIVE

These are the **only** production IDs that are live today. They are frozen here as the authoritative reference.

| Live ID | Meaning live        | Used by record | Source                                   |
| ------- | ------------------- | -------------- | ---------------------------------------- |
| `P0`    | Static / Presenter  | `PL1T3-s2`     | MMD-0 register / UI label if confirmed   |
| `P6`    | Quiz / Visited-Gate | `PL3T1-s28`    | MMD-0 register                           |
| `P11`   | Drag-Match          | `PL5T3-s4`     | MMD-0 register / UI label if confirmed   |

**Only these production IDs are live today. Everything else is draft / candidate unless separately ratified.**

## 2. Collision table

Live register meaning vs uploaded candidate-taxonomy meaning:

| ID    | LIVE register meaning | Candidate-taxonomy meaning | Verdict                                                |
| ----- | --------------------- | -------------------------- | ------------------------------------------------------ |
| `P0`  | Static / Presenter    | Static Slide / Navigation  | Match / safe                                           |
| `P6`  | Quiz / Visited-Gate   | Visited Gate               | Partial / modelling conflict                           |
| `P7`  | not used live         | Drag & Drop                | Conflict-risk because live drag-match is `P11`         |
| `P8`  | not used live         | Quiz                       | Conflict-risk because live quiz-related record uses `P6` |
| `P11` | Drag-Match            | Timeline Navigation        | **HARD CONFLICT**                                      |

Also note:

- `P12`–`P25` exist **only** in the uploaded taxonomy draft, **not** in the live register.
- **Do not use the uploaded draft P-numbering as production mapping.**

## 3. Resolution — re-namespace the draft taxonomy

Namespace rule (frozen) — in short: **P# = live, T-Name = draft**:

- **Bare `P#` = live** / ratified / production register-backed pattern only.
- **`T-Name` = draft / candidate** taxonomy concept.
- The candidate taxonomy **must use the `T-` namespace** until ratified.
- Draft `T-` IDs **must never be written into the MMD register** as production-ready values.

Proposed reconciliation mapping (reconciliation only — **not** a production taxonomy):

| Concept                 | UX family               | Live ID if any | Draft ID        | Status                               |
| ----------------------- | ----------------------- | -------------- | --------------- | ------------------------------------ |
| Static / Presenter      | Navigation              | `P0`           | —               | RATIFIED                             |
| Quiz                    | Assessment              | `P6` bundled   | `T-Quiz`        | RATIFIED live as P6 / modelling note |
| Visited-Gate            | Navigation / Completion | `P6` bundled   | `T-VisitedGate` | RATIFIED live as P6 / modelling note |
| Drag-Match              | Interaction             | `P11`          | `T-DragMatch`   | RATIFIED live as P11                 |
| Click-to-Reveal         | Reveal                  | —              | `T-Reveal`      | CANDIDATE                            |
| Flip Card / Card Reveal | Reveal                  | —              | `T-Reveal.flip` | REQUESTED                            |
| Modal / Popup           | Reveal                  | —              | `T-Modal`       | CANDIDATE                            |
| Tooltip                 | Reveal                  | —              | `T-Tooltip`     | CANDIDATE                            |
| Accordion               | Reveal                  | —              | `T-Accordion`   | CANDIDATE                            |
| Hotspot                 | Exploration             | —              | `T-Hotspot`     | CANDIDATE                            |
| Branching               | Navigation              | —              | `T-Branch`      | CANDIDATE                            |
| Timeline                | Navigation              | —              | `T-Timeline`    | CANDIDATE                            |
| Matching / Connect      | Interaction             | —              | `T-Matching`    | CANDIDATE                            |
| Sort / Ranking          | Interaction             | —              | `T-Sort`        | CANDIDATE                            |

This is a **reconciliation mapping only**, not a production taxonomy.

## 4. Flip card handling

- Flip **should not** be created as `P12 Flip` now. (Mentioned here only as a thing **not** to do — `P12 Flip` is not to be minted as a production ID in this sprint.)
- The current safest status is **`T-Reveal.flip`**.
- It is **REQUESTED**, not RATIFIED.
- Rationale:
  - Bariah's governance wording is "click-to-reveal".
  - Laila's production wording is "flip interaction".
  - Therefore it likely belongs to the **Reveal** family until ratified otherwise.
- It may later become its own pattern **only if** Bariah/Laila ratify that flip behavior is materially different from click-to-reveal.

Open ratification questions:

1. Is the flip visual mandatory, or is any click-to-reveal acceptable?
2. Must all cards be flipped before completion?
3. How many cards?
4. What is the front/back content per card?
5. Is iSpring implementation feasible?
6. What is the keyboard/touch/accessibility fallback?

## 5. P6 modelling note

- Live `P6` currently **bundles** quiz / visited-gate usage.
- The uploaded taxonomy **separates** Visited Gate and Quiz.
- This is a **modelling decision, not a silent correction**.
- **Do not silently repoint `P6`.**
- If `P6` is split later, do it through a **ratified schema/version decision** and a **new ID** if needed — never by quietly changing what `P6` means.

## 6. Non-goals

This sprint does **not**:

- modify `sbat/MMD_READINESS_REGISTER.csv`
- modify `sbat/MMD_READINESS_REGISTER.md`
- modify `sbat/m1-screen-c.html`
- modify `sbat/m1-reviewer-entry.html`
- modify ADRs
- modify `vercel.json`
- activate a scanner
- implement components
- create a candidate backlog
- create new production `P#` IDs
- mark the taxonomy draft as MMD-ready

## 7. Promotion path

How a draft taxonomy concept becomes production:

```
T-Name CANDIDATE
  → real Cycle 7 source/evidence found
  → T-Name REQUESTED
  → Bariah confirms learning intent
  → Laila confirms MMD/iSpring feasibility
  → behavior, required fields, completion rule, accessibility fallback, QA rule defined
  → s06 / human ratification
  → assigned next free live P#
  → enters production taxonomy and may be used in MMD handoff
```

**Important:** do not reuse or repoint existing live `P0`, `P6`, or `P11`.

## 8. Next step

1. Firdaus ratifies this reconciliation rule.
2. Then create `taxonomy/INTERACTION_CANDIDATE_BACKLOG.md` in a later sprint.
3. Then map edge cases into the `T-` taxonomy.
4. **Do not proceed to the backlog until this reconciliation is committed.**
