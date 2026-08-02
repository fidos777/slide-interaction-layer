# STAGE_4_2F_A_QA_REPORT

Stage 4.2F-A — PL06 scale-out inventory and first proof selection.

Suite: `docs/pl06/tools/pl06_inventory_qa_v1.py`
Mutations: `docs/pl06/tools/pl06_inventory_mutations_v1.py`

# 1. Test accounting

| Metric | Value |
|---|---:|
| `ACTIVE_TEST_GATES_PASSING` | **82 / 82** |
| `SUPERSESSION_MARKERS_PRESENT` | **0** |
| `TOTAL_EMITTED_GATE_RECORDS` | **82** |

**Every gate record carries an explicit `gate_type` field.** Nothing in this suite infers a
gate's kind from a substring in its ID. That rule exists because of a measured failure one
stage ago: the v0.4.4 supersession-marker count was taken by matching `SUPERSEDED` in the
gate ID and swept in six ordinary live tests, understating the active suite by six.

`SUPERSESSION_MARKERS_PRESENT = 0` is not a rounding of anything. This is a new suite with
no retired rulings in it yet.

## 1.1 Distribution by declared type

| `gate_type` | Gates |
|---|---:|
| `INVENTORY_INTEGRITY` | 18 |
| `ARTIFACT_AGREEMENT` | 15 |
| `SELECTION_INTEGRITY` | 12 |
| `AUTHORITY_DISCIPLINE` | 10 |
| `RULE_PORTABILITY` | 9 |
| `PLAN_INTEGRITY` | 9 |
| `STOP_CONDITION` | 7 |
| `ACCOUNTING` | 2 |

# 2. Mutation sensitivity

| | |
|---|---:|
| Fixtures | **32** |
| Detected | **32** |
| `MUTATION_FIXTURES_MISSED` | **0** |
| `BASELINE_FALSE_FAILURES` | **0** |

Every fixture patches the controlled data source in memory and reverts it in a `finally`.
No fixture artifact is written to disk and the committed data is never touched.

| Fixture | Injected defect | Rule it attacks |
|---|---|---|
| `N-01` | a unit loses its source reference | every unit must trace to frozen evidence |
| `N-02` | a unit id is duplicated | unique unit identity |
| `N-03` | a Topik/Bahagian pair is duplicated under a new id | unique unit boundary |
| `N-04` | an invalid readiness value | typed readiness vocabulary |
| `N-05` | a source-blocked unit is marked READY | readiness must respect blockers |
| `N-06` | an undeterminable interaction pattern is marked ready | unsupported ≠ ready |
| `N-07` | a unit with no Rumusan is marked fully complete | completeness requires Rumusan |
| `N-08` | a unit with no quiz source is marked fully complete | completeness requires a quiz |
| `N-09` | a montage-attested unit claims direct Bariah authority | authority-class inflation |
| `N-10` | a Bahagian number is invented | no boundary from numbering |
| `N-11` | an existence-only unit claims source rows | evidence scope |
| `N-12` | a unit with no source document claims a Rumusan | evidence scope |
| `N-13` | a B02-specific rule is promoted to PL06 global | rule portability |
| `N-14` | a B02-specific rule gets a PL06-wide destination | rule portability |
| `N-15` | a mandatory B02-specific rule is deleted | the brief's mandatory local list |
| `N-16` | an unoracled rule drops its human-authority requirement | authority discipline |
| `N-17` | the selected proof unit is not in the inventory | selection traceability |
| `N-18` | a blocked selection is declared unconditional | selection honesty |
| `N-19` | a blocked selection drops its preconditions | selection honesty |
| `N-20` | B02 itself is selected as the first non-B02 proof | selection validity |
| `N-21` | a sourceless candidate is scored on visual availability | scoring honesty |
| `N-22` | a plan row names a unit absent from the inventory | plan traceability |
| `N-23` | a held unit is given an invented duration | no invented capacity |
| `N-24` | a PowerPoint smoke duration is estimated | no invented capacity |
| `N-25` | a global open item is scoped to block an unrelated unit | scope discipline |
| `N-26` | a unit names a blocker in no stop register | blocker traceability |
| `N-27` | the call approval is reclassified as a direct screenshot | authority discipline |
| `N-28` | the call approval is marked written-confirmed | authority discipline |
| `N-29` | the call approval is read as authorising canonical freeze | authority discipline |
| `N-30` | a forbidden verdict is declared | verdict discipline |
| `N-31` | a COMPLETE verdict while units are source-blocked | verdict discipline |
| `N-32` | the CSV diverges from the controlled data source | one-source emission |

# 3. The B02 toolchain, re-run unchanged

Stage 4.2F-A modified nothing in `reviews/source-completion/`. Re-run to prove it:

| | |
|---|---:|
| B02 governance suite, v0.4.4.1 | **461 / 461 PASS** |
| B02 mutation fixtures | **51 / 51 detected, 0 missed** |
| B02 baseline false failures | **0** |
| v0.4.4.1 SHA-256 | `faef6c85745d2750236ffdf23fb7d14b81d26ed37c7db58ed274cb8d0f0178e5` — unchanged |

# 4. What this suite checks, and what it cannot

It checks that the **inventory is internally honest**: that every unit traces to frozen
evidence, that no readiness claim outruns its blockers, that no B02 rule is promoted without
evidence, that no authority class is inflated above the evidence it cites, that the selected
proof unit exists and declares its blockers, that no duration is invented, and that the
Markdown and CSV cannot disagree because they are emitted from one list of dicts.

It cannot check that the inventory is **complete**. Eighty-two green gates say the eight
units listed are described truthfully. They say nothing about a ninth unit nobody has told
us exists — and given that no artifact in this repository enumerates PL06 Bahagian at all,
a ninth unit almost certainly does exist. That gap is the stage verdict, not a gate failure.

It also cannot check the **judgement** in the selection. `SOURCELESS_CANDIDATE_SCORED_ON_CONTENT`
forces the zeros to be honest; it has nothing to say about whether Topik 4 is the right
first proof. That part is argued in prose and can be wrong.

# 5. Verdict

```
PL06_SCALE_OUT_BLOCKED_BY_UNRESOLVED_UNIT_BOUNDARIES
```

Not claimed: `PL06_STORYBOARDS_COMPLETE`, `PL06_READY_FOR_MMD`, `PL06_CANONICALLY_FROZEN`,
`PL06_PRODUCTION_RELEASED`.

**No storyboard was generated in this stage.**
