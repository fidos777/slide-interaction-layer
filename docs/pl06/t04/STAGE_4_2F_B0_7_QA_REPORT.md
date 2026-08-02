# STAGE_4_2F_B0_7_QA_REPORT

```
STAGE    = 4.2F-B0.7 — CONSOLIDATE FINAL BARIAH STRUCTURAL RULINGS
SUITE    = docs/pl06/t04/tools/t04_final_rulings_qa_v1.py
FIXTURES = docs/pl06/t04/tools/t04_final_rulings_mutations_v1.py
RESULT   = 105/105 active gates PASS · 0 supersession markers · 105 emitted records
FIXTURES = 32/32 detected · 0 missed · 0 baseline false failures
```

**A green suite measures the suite, not the artifact.** These gates hold that Bariah's
confirmations were transcribed exactly, that the split she confirmed is the split the
contracts implement, that a confirmed policy is not reported as unapproved content and an
unapproved content item is not reported as confirmed, and that a requirement count is never
published as a production count. They cannot tell you whether the dialogue is good Malay or
whether Alya is the right character.

# 1. Gate accounting

| Gate type | Count | Holds |
|---|---:|---|
| `EVIDENCE_INTEGRITY` | 12 | all three images byte-identical; the 3-vs-1 delivery gap declared; the illegible Akta line not attributed to the screenshot |
| `DECISION_INTEGRITY` | 13 | seven decisions, all resolved or conditionally resolved; every change records its previous status |
| `CAST_DISCIPLINE` | 14 | D-03 stays conditional; instance mapping not complete; no compliance content in any character line |
| `SAFETY_DISCLOSURE` | 11 | statute, licensed operator and PPE base-visible; the reveal set matches the ruling exactly; the split is applied to a contract |
| `SMARTART_FIDELITY` | 5 | six nodes and their order; asset hash unchanged; MMD not started |
| `ASSET_ACCOUNTING` | 12 | 46 obligations retained, unique asset count not determined, nothing in production |
| `APPROVAL_ACCOUNTING` | 10 | four typed totals; confirmed policy is not zero; no final content approved |
| `MAPPING_INTEGRITY` | 8 | seven candidates including the new Slide 2; screen count not claimed |
| `PRODUCTION_GUARD` | 5 | no PPTX, no generator change, no MMD |
| `ARTIFACT_AGREEMENT` | 13 | Markdown / CSV / JSON agree with the data module |
| `ACCOUNTING` | 2 | no duplicate gate IDs; every record typed |
| **TOTAL** | **105** | |

`SUPERSESSION_MARKER` records: **0**.

# 2. The suite passed on first run. The fixtures did not.

105/105 on the first execution. That is not evidence of correctness — the fixtures are what
test the gates, and one of them failed.

## 2.1 `W-22` was missed — the gate was reading a cached number

The fixture marks the three near-duplicate PPE and storage subjects as reusable. The gate
`NEAR_DUPLICATE_SUBJECTS_MARKED_DO_NOT_REUSE` did not fire.

The cause: the gate read `ASSET_TOTALS["do_not_reuse"]`, which is computed **once at module
import** from `ASSET_PLAN`. Patching the plan left the cached total untouched, so the gate
kept reporting 3 while the live plan said 0. A gate that reads a derived constant instead of
the data it derives from tests nothing — it tests that the constant is still the constant.

Two fixes, both at the gate:

- the check now counts from `ASSET_PLAN` directly;
- a new gate `ASSET_TOTALS_AGREE_WITH_THE_LIVE_PLAN` asserts the cached totals still match the
  live plan, so this staleness class fires on sight rather than hiding a blind gate.

This is worth generalising: every precomputed total in a data module is a potential blind spot
for any gate that reads it instead of recomputing. The other cached total in use here —
`production_started` — was already paired with a live check, which is why `W-11` detected.

# 3. Mutation fixtures

32 fixtures, **32 detected, 0 missed, 0 baseline false failures**. All ten mutations named in
the stage brief are covered; twenty-two more were added.

| Fixture | Defect injected | Named in brief |
|---|---|---|
| `W-01` | 60 percent narrowed to T04 only | ✓ |
| `W-02` | confirmed threshold dropped back to unresolved | |
| `W-03` | D-04 restored to unresolved | ✓ |
| `W-04` | the statute moved off the base screen | ✓ |
| `W-05` | PPE moved off the base screen | ✓ |
| `W-06` | a base row also listed as reveal-eligible | |
| `W-07` | split marked applied but the contract not changed | |
| `W-08` | two SmartArt nodes swapped | ✓ |
| `W-09` | a seventh node added | |
| `W-10` | MMD production marked started | ✓ |
| `W-11` | an asset row reports production started | |
| `W-12` | Alya / Encik Rahman marked final, assessment skipped | ✓ |
| `W-13` | the CAIR fit assessment relabelled a Bariah ruling | |
| `W-14` | fit result outside the allowed set | |
| `W-15` | a character line states a statutory obligation | |
| `W-16` | the Slide 2 dialogue marked approved | |
| `W-17` | a beat cites a row the contract does not declare | |
| `W-18` | 46 obligations equated to 46 unique assets | ✓ |
| `W-19` | a unique asset count asserted in prose | |
| `W-20` | unique asset IDs assigned before grouping | |
| `W-21` | coverage status claims coverage exists | |
| `W-22` | near-duplicate subjects marked reusable | |
| `W-23` | all decisions reported as unapproved | ✓ |
| `W-24` | the Rumusan reported as approved | ✓ |
| `W-25` | quiz content reported as approved | ✓ |
| `W-26` | the storyboard claimed approved | |
| `W-27` | an evidence SHA-256 no longer matches | |
| `W-28` | the 3-vs-1 delivery discrepancy hidden | |
| `W-29` | the illegible Akta line attributed to the screenshot | |
| `W-30` | D-05 reappears in the pending list | |
| `W-31` | the Slide 2 candidate dropped from the mapping | |
| `W-32` | a final screen count claimed | |

# 4. Two gates worth singling out

**`NO_COMPLIANCE_CONTENT_IN_ANY_CHARACTER_LINE`** scans every drafted dialogue line for the
source's own compliance vocabulary — statute, licence, PPE, SDS, pesticide, spraying, locked
storage, warning signage, reporting. It exists because the source states that spraying must be
done by a licensed operator, and Encik Rahman is a senior contractor, not a licensed operator.
A mentor character stating a statutory duty converts a source citation into a character's
word. `W-15` proves the gate fires.

**`OBLIGATION_COUNT_NOT_ASSERTED_AS_UNIQUE_ASSET_COUNT`** exists because "46 visuals required"
reads like "produce 46 files" and is not the same claim. `W-18` and `W-19` prove both the
structured and the prose route are caught.

# 5. Chain status

| Suite | Gates | Fixtures |
|---|---|---|
| **Stage 4.2F-B0.7 final rulings** | **105 / 105** | **32 / 32 detected** |
| Stage 4.2F-B0.6 rulings | 130 / 130 | 26 / 26 detected |
| Stage 4.2F-B0.5 decision pack | 107 / 107 | 39 / 39 detected |
| Stage 4.2F-B0 extraction | 109 / 109 | 30 ran, 30 detected · **4 `SKIPPED_NO_DOCX`, not counted as passing** |
| Stage 4.2F-A2 PL06 inventory | 140 / 140 | 54 / 54 detected |

# 6. What no gate here checks

- Whether Alya and Encik Rahman are actually the right characters for T04 Slide 2. The gates
  check that the assessment exists, is CAIR's, and stays pending — not that its conclusion is
  right.
- Whether the five drafted dialogue turns read naturally in Malay.
- Whether hiding spraying conditions, notification and reporting behind a reveal is
  instructionally sound. Bariah ruled it; the gates enforce her ruling, they do not judge it.
- Whether the seven asset groups are the right groups.
- Whether the inferred Akta line was in fact what Bariah confirmed.
