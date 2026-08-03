# PL06 STATUS AFTER STAGE 4.2F-B0.9

```
STAGE            = 4.2F-B0.9 — T04 authority decision ingestion and content freeze
PLANNED_UNITS    = 14
PROOF_UNIT       = K5-PL06-T03-B02 — delivered and call-approved
NEWLY_FROZEN     = K5-PL06-T04-B01 — content frozen under authority decision
REMAINING_UNITS  = 12
PPTX_GENERATED_THIS_STAGE = 0
```

This is a status snapshot, not a completion claim. **No percentage is derived from file
counts.** Two of fourteen units have reached a defined state and twelve have not; what those
twelve need is described below, not scored.

# 1. Where the fourteen units stand

| Unit state | Count | Units |
|---|---:|---|
| Delivered baseline, call-approved | 1 | `K5-PL06-T03-B02` |
| Content frozen under authority decision, storyboard not built | 1 | `K5-PL06-T04-B01` |
| Source in custody by identity, content not extracted | 12 | the remainder of the fourteen |

The unit inventory, boundaries and heading anchors are unchanged from
`PL06_STORYBOARD_PRODUCTION_INVENTORY_v1.md`. Nothing in this stage touched any unit other
than T04.

# 2. What T04-B01 now has

| Element | State |
|---|---|
| Screen sequence | 22 screens, frozen — one screen inserted by the authority, eight renumbered |
| Unit labelling | Learner sees `Topik 4`; internal ID `K5-PL06-T04-B01` unchanged; closing screen reads *Tamat Topik* |
| Slide 2 dialogue | 4 lines, written by the authority, carried verbatim |
| Rumusan | 3 beats — Kepentingan · Skop/Isi Utama · Manfaat — written by the authority, carried verbatim |
| Quiz | 5 items, all stems written by the authority; 4 MCQ + 1 Multiple Response with checkbox options |
| Quiz answer keys | **proposed, not final** |
| Q5 options 5 and 6 | **CAIR-drafted under authority instruction, pending confirmation** |
| Visual scope | Accepted as a set with conditions — 41 proposed unique assets across 8 groups |
| Source bindings | Present and resolving; original-DOCX round trip open and non-blocking |
| Storyboard PPTX | **not built** |
| MMD assets | **none produced** |

# 3. Two rules that now apply beyond T04

Bariah issued both while reviewing T04 and marked both *Global keseluruhan kursus*. They are
recorded as course-wide because she said so.

| ID | Rule | Scope |
|---|---|---|
| `QUIZ-GLOBAL-01` | A quiz stem asks its question directly and never attributes its content to the module | every PL in the Kursus |
| `QUIZ-GLOBAL-02` | Multiple Response options are presented as checkboxes; letter labels are reserved for single-answer items | every PL in the Kursus |

**Only their T04 application has been executed.** No other unit's quiz has been examined
against them, and none was modified by this stage. When any of the twelve remaining units
reaches quiz drafting, both rules bind it.

A third rule was **not** inferred. The three-beat Rumusan structure was issued while amending
the T04 Rumusan and was not marked course-wide, so its scope is recorded as `T04_ONLY`.

# 4. What T04-B01 does not have

| ID | Open item | Owner |
|---|---|---|
| E-01 | Confirmation of the two CAIR-written Q5 distractors | Bariah |
| E-02 | Final answer keys for all five quiz items | Bariah |
| E-03 | The referent of the "Q3" WhatsApp line | Bariah |
| E-04 | Confirmation of the `pembajaan` → `racun` wording correction on the inserted screen | Bariah |
| E-05 | Original module DOCX round trip and hash proof | Firdaus |
| E-06 | Individual asset subjects and styles | Bariah |

None of the six blocks laying out the storyboard. E-01 and E-02 block publishing a scored
quiz; E-06 blocks MMD production; E-05 is a bounded, repairable source risk carrying the token
`SOURCE_REPRODUCIBILITY_OPEN_NONBLOCKING_FOR_T04_STORYBOARD_BUILD`.

# 5. What the twelve remaining units still need

Every one of them needs the same chain T04 has just completed, and none of it has been started
for any of them:

1. controlled content extraction from the module, by heading anchor rather than page slice
2. a visual obligation inventory and an asset grouping plan
3. a proposed screen sequence, dialogue, Rumusan and quiz draft
4. a governed review artifact for Bariah
5. authority decision ingestion and a content freeze

T03-B02 proved the chain end to end; T04-B01 has now run it as far as the freeze. The two
units together establish the pattern, and the twelve that follow are the work.

# 6. Reproducibility posture, stated once

Source custody for all fourteen units is **by identity** — a named DOCX heading anchor and
paragraph index per unit — which is what Stage 4.2F-A2 closed. What remains open for T04, and
untouched for the other twelve, is re-retrieving the original module DOCX and proving its hash
against the extracts taken from it. That is one task, not fourteen, and closing it closes E-05
for every unit at once.
