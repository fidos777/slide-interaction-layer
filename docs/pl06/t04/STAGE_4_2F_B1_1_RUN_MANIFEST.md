# Stage 4.2F-B1.1 — Lane A run manifest

**T04 post-B1 interaction-state coverage verification**

```
UNIT (internal)  = K5-PL06-T04-B01
UNIT (learner)   = Topik 4
BRANCH           = claude/verify-powerpoint-file-vpfzkg
CONTINUES FROM   = 0a0eb72
STAGE            = 4.2F-B1.1
SUITE_ID         = T04_STATE_COVERAGE_QA_v1
STATUS CARRIED   = T04_LAYOUT_STORYBOARD_BUILT
```

The Stage 4.2F-B1 artifact is treated throughout as a **layout storyboard**. It is not
`T04_INTERACTION_REVIEW_COMPLETE`, not `T04_STORYBOARD_FROZEN` and not
`T04_CANONICAL_PRODUCTION_TEMPLATE`; those three strings are declared as forbidden claims in
the model and a gate reads the appendix deck back off disk to prove none of them appears in it.

---

## 1. Runtime-state inventory

Derived from the controlled model, never from the deck's page count.

| Measure | Count |
| --- | --- |
| Learner screens | 22 |
| Base states (one per screen) | 22 |
| Triggered states (reveal / step / quiz item / quiz result) | 35 |
| Completion flags | 8 |
| **Total runtime states** | **65** |
| Interactions | 35 |
| B1 review pages | 26 (4 of them continuations) |

The five quiz items are the quiz screen's own states — that screen has no separate base
state, because Q1 *is* what a learner sees on arrival. That is why 22 + 35 + 8 = 65 rather
than 66.

## 2. Coverage before and after the appendix

Coverage is judged against five criteria, all five of which must be met. A state is not
counted as review-visible merely because its text sits in Notes or in a JSON file.

| Representation | Before the appendix | After the appendix |
| --- | ---: | ---: |
| FULL_PAGE_VISIBLE | 13 | 13 |
| MULTI_PANEL_VISIBLE | 0 | 52 |
| NOTES_ONLY | 0 | 0 |
| METADATA_ONLY | 52 | 0 |
| NOT_REPRESENTED | 0 | 0 |

```
DECISION BEFORE = T04_LAYOUT_READY_STATE_REVIEW_APPENDIX_REQUIRED
DECISION AFTER  = T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN
```

The B1 deck alone did **not** cover the state model: 52 of 65 states existed only as
metadata. That is the finding, and the appendix exists because of it.

## 3. The appendix

```
reviews/storyboard-bariah/t04_storyboard/K5PL06T04B01_STATE_REVIEW_APPENDIX_v1_0.pptx
83,234 bytes · 29 slides (1 cover + 28 pages) · 28 preview PNGs · 0 overflowed
```

Two state panels per page, never mixing two screens on one page, written in Malay for a
Malay-reading reviewer. Every panel answers the same five questions: trigger, what is shown,
how it differs from the base state, how the learner returns or continues, and which source
rows and decisions bind it. The B1 deck was **not** touched — the appendix is a separate
file, and a gate asserts the B1 deck still has its own 27 slides.

The appendix was generated, never hand-patched. All 28 preview pages were rendered and
visually inspected as a contact sheet.

## 4. Brief source-row audit

`T04-ROW-074`, `T04-ROW-076`, `T04-ROW-077` — all three **FOUND** in the controlled extract.
No replacement binding was manufactured for any of them, and the
`BRIEF_REFERENCE_NOT_FOUND_IN_CONTROLLED_EXTRACT` token was not needed.

| Row | Relation to the quiz options it touches |
| --- | --- |
| T04-ROW-074 | **Supports** live Set B option 4 (the proposed key: SDS kept on site). **Contradicts** rejected Set A option 6. |
| T04-ROW-076 | **Supports** live Set B option 3. **Contradicts** live Set B option 5 — which is the property a correct distractor needs. |
| T04-ROW-077 | **Contradicts** rejected Set A option 5. |

ROW-076 contradicting a *live* option is the intended state of affairs for a distractor, not
a defect; it is recorded as `CONTRADICTORY` with the reasoning written out, so nobody later
reads the flag as an error.

## 5. Live namespace separation

Two live registers, on disjoint number blocks so that no two live registers can ever expose
the same unqualified identifier: `T04-EXT` takes 1–49, `T04-OPEN` takes 51–99.

| Historical | Live ID | Subject |
| --- | --- | --- |
| E-01 | — | Q5 replacement options E and F — CLOSED_BEFORE_THE_SPLIT |
| E-02 | T04-OPEN-51 | Quiz answer keys, all five |
| E-03 | — | The "Q3" WhatsApp referent — CLOSED_BEFORE_THE_SPLIT |
| E-04 | T04-OPEN-52 | The pembajaan → racun wording correction on T04-S14 |
| E-05 | T04-EXT-01 | Original module DOCX round trip and hash proof |
| E-06 | T04-OPEN-53 | Individual asset subjects and styles |
| E-07 | — | Which Q5 option pair stands — CLOSED_BEFORE_THE_SPLIT |
| E-08 | T04-OPEN-54 | Supplementary screenshot binary custody |
| new | T04-EXT-02 | T04-ROW-003 carries the six-step diagram as one row with no text |
| new | T04-OPEN-55 | Runtime behaviour has never been shown to Bariah |

```
unqualified_collisions    = []
ids_outside_their_block   = []
```

The collision check found a real defect while this lane was being built: the first numbering
put `T04-EXT-01` and `T04-OPEN-01` in the same live namespace. The blocks were made disjoint
in response.

## 6. Oracle independence

12 release-critical gates audited. 11 are fully independent — the expected value comes from a
literal, a hash-pinned extract or an immutable authority artifact, not from the generator that
produced the observed value.

One gate, `EVERY_MODEL_BLOCK_APPEARS_IN_THE_DECK`, deliberately shares a generator: both sides
originate in the model, but the observed side has made a round trip through python-pptx and
back off disk. It proves the writer dropped nothing. It is not treated as a content-correctness
oracle; correctness is `SOURCE_STRINGS_ARE_VERBATIM` against the extract.

**Four gates are on record as having been self-referential and repaired after a fixture
walked past them.** Two came from earlier stages. Two were found by this lane's own mutation
suite and are described in section 7.

Both prior protections are preserved and asserted:

- filtered-population named-membership and delta assertions — 18 closed populations
  (`t04_predicate_audit_v1`);
- exact namespace + local-name OOXML matching — six proof cases (`t04_ooxml_v1`).

## 7. Where a green suite hid a defect

The state suite passed 97/97 with zero vacuous gates before the mutation suite was run. Two
fixtures then walked straight past it.

**A-01 — "an appendix page carries three panels."** The gate
`EVERY_APPENDIX_PAGE_HOLDS_AT_MOST_TWO_PANELS` compared pages built from `PANELS_PER_PAGE`
against `PANELS_PER_PAGE`. Raising the constant to 3 raised the gate with it, so a
three-panel page was "at most two panels" by definition. This is the same self-referential
shape as S-11 and E-02 in earlier stages — the third occurrence of the class.

The repair has three parts, because one literal alone would not have said anything true:

1. the gate now checks the literal `2`;
2. `THE_PANEL_BUDGET_MATCHES_THE_DECLARED_REVIEW_POLICY` pins both `PANELS_PER_PAGE` and
   `PANEL_BUDGET_LITERAL` to `2`;
3. `renderer_panel_capacity()` lays every state's panel out at each candidate width using the
   font the previews render with, and reports the widest arrangement in which nothing
   overflows. **It measures 4.**

That third number changed what could honestly be claimed. Three panels physically fit. The
two-panel rule is therefore recorded as
`REVIEW_LEGIBILITY_POLICY_STRICTER_THAN_THE_RENDERER_CAPACITY` — a reviewing decision, not a
renderer limit — and the manifest says so rather than implying the renderer forced it.

**A-03 — "a state panel never reaches the appendix deck."** One runtime state was deleted
from the model and the appendix was rebuilt. Every appendix gate still passed. The page plan
and the deck were both projected from the mutated inventory, so they agreed with each other
about a state that had ceased to exist. A gate that compares a generated artifact against the
generator that produced it cannot see a record leave the population — the same lesson as the
C-05 filtered-population class, arriving by a different route.

The repair is an anchor no generator can rewrite: `DECLARED_STATE_IDS`, the 65 state IDs
written down by hand, plus the frozen split into 52 panel states and 13 already-full-page
states. Six new gates check the live inventory and the live page plan against that roll in
both directions, and one of them re-reads the saved deck and looks for all 52 frozen panel
IDs in it. Fixtures A-10 to A-15 attack the repair itself — shortening the roll, editing the
declared total, relaxing the literal budget, reclassifying a state between the two rolls,
dropping a screen from the page plan, and replacing the measured capacity with an assertion —
because an anchor anyone can move is not an anchor.

## 8. Suites

Gate counts are never merged across suites.

| Suite | Result |
| --- | --- |
| **T04_STATE_COVERAGE_QA_v1** (this lane) | **108/108 PASS**, 0 vacuous |
| T04_STORYBOARD_QA_v1 | 114/114 PASS |
| T04_SUPPLEMENTARY_EVIDENCE_QA_v1 | 133/133 PASS |
| T04_AUTHORITY_DECISION_INGESTION_QA_v1 | 251/251 PASS |
| t04_predicate_audit_v1 | 18 closed populations, 5 documented exclusions, 0 failing |
| t04_ooxml_v1 | 6/6 proof cases OK |

Lane A gate types: APPENDIX 27, STATE_INVENTORY 22, COVERAGE 13, NAMESPACE 11, SOURCE_AUDIT
11, ORACLE 9, STATUS_GUARD 8, ACCOUNTING 7.

**Mutation suite: 64 fixtures, 64 detected, 0 missed.** Baseline 108/108, no false failures,
`appendix_rebuilt_clean = true` — the six rebuild fixtures corrupt the deck on disk and the
real appendix is restored byte-for-byte in text afterwards.

## 9. Native PowerPoint

`T04_NATIVE_POWERPOINT_INSPECTION_PACKAGE_v1` is generated for a human to open both decks in
Microsoft PowerPoint. It is an instruction package with a correction-intake form, not a
result. LibreOffice here still has no Impress filter, so no native render was performed and
none is claimed. Any correction found in native PowerPoint goes into the generator and is
followed by complete regeneration — the package states this and a gate asserts the
no-hand-patching clause is present.

## 10. Not checked

- whether the interaction design is instructionally sound — Bariah has never been shown a
  state-level model, which is `T04-OPEN-55`;
- whether the reveal and reset behaviours match what the runtime will actually do — they are
  CAIR-specified, not authority-ruled;
- how either deck renders in Microsoft PowerPoint;
- whether the six process-step labels match the SmartArt artwork, which carries no
  extractable text (`T04-EXT-02`);
- whether Bariah agrees the appendix format is readable.

---

## Verdict

```
T04_INTERACTION_STATE_REVIEW_COVERAGE_PROVEN
```

All 65 runtime states are review-visible: 13 as full pages in the B1 deck, 52 as panels in
the state review appendix. Nothing is counted from Notes or JSON, nothing is duplicated,
there are no orphan panels, and only the cover page carries no state.

This is a statement about **review coverage**, not about approval. The interaction design
itself remains unreviewed by the authority.
