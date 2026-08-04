# Stage 4.2F-E addendum — historical report correction

This addendum exists because Stage 4.2F-E rewrote three Stage 4.2F-D reports. It records
what happened, what was restored, and what changed so it cannot happen again. It does not
amend any commit.

---

## What happened

Stage 4.2F-E was required to end a condition that a Stage 4.2F-D gate asserted. The gate
`K2_REMAINS_AN_UNRESOLVED_SOURCE_RECORD_NOT_A_UNIT` claimed every K2 queue row carried
`record_type = UNRESOLVED_SOURCE`. Stage E replaced that single row with nine candidate
structures, so the gate went red and was renamed to
`NO_K2_ROW_IS_A_CONFIRMED_PRODUCTION_UNIT` — preserving its intent while updating the fact.

**That gate change was correct and stands.**

The error was what followed. With the suite changed, the Stage-D emitters were re-run.
Nothing about that felt like tampering — it looked like keeping generated artifacts in
sync with their generators. But those particular artifacts are not live projections of a
current model; they are the record of what Stage 4.2F-D found. Re-running the emitters
silently replaced a Stage-D finding with a Stage-E finding, in a file whose entire purpose
is to say what was true at the end of Stage D.

Three files were affected. A fourth, the Stage-D run manifest, was not touched.

| artifact | Stage-D bytes (SHA-256, first 16) | after Stage E | status now |
|---|---|---|---|
| `STAGE_4_2F_D_QA_REPORT_v1.md` | `c99d2693fc781e49` | `6d0bf6bd85226d63` | **restored** |
| `STAGE_4_2F_D_QA_REPORT_v1.json` | `67d5fbd80c46b8b4` | `675d63dfd8335441` | **restored** |
| `STAGE_4_2F_D_MUTATION_REPORT_v1.md` | `c4074766aeb75532` | `2010068c5ce423ff` | **restored** |
| `STAGE_4_2F_D_RUN_MANIFEST.md` | `2fa3252284b1ac22` | unchanged | intact throughout |

All three were restored byte-for-byte from commit `b603f44`, the Stage 4.2F-D HEAD.

---

## What the restored reports say, and why that is correct

The restored Stage-D QA report describes a 60-gate suite in which the K2 gate is named
`K2_REMAINS_AN_UNRESOLVED_SOURCE_RECORD_NOT_A_UNIT`. That is an accurate record of Stage
4.2F-D. It is **not** a description of the current suite, and it is not supposed to be.

The current suite is described in `STAGE_4_2F_E_QA_REPORT_v1.md`, which names the gate
change explicitly.

So the two reports disagree about the gate's name, and that disagreement is the point: it
is what lets a reader see that something changed and when. A single silently-updated file
would have shown a consistent history that never happened.

---

## Supersession record

```
GATE      K2_REMAINS_AN_UNRESOLVED_SOURCE_RECORD_NOT_A_UNIT
STATUS    SUPERSEDED_FOR_LIVE_CHECKING_BY
          NO_K2_ROW_IS_A_CONFIRMED_PRODUCTION_UNIT
SINCE     Stage 4.2F-E, commit 9d4d0f2
HISTORICAL_RECORD  PRESERVED_UNCHANGED in STAGE_4_2F_D_QA_REPORT_v1.{md,json}
```

- The **intent** did not change: K2 must not be promoted to a production unit on the
  strength of a missing binary.
- The **fact** changed: K2 is no longer a single unresolved row, because the source's own
  tables evidence nine packages.
- The live suite is `STAGE_4_2F_D_RELEASE_FACTS_QA_v1` at 60/60 with 44/44 fixtures
  detected, unchanged in total by the rename.

---

## What changed so this cannot recur

`docs/source/tools/src_historical_freeze_v1.py` records the committed SHA-256 of every
finished-stage report and exposes `guard(filename)`, which raises
`HistoricalReportFrozen` if a generator is about to overwrite one while it still holds its
frozen bytes.

The guard is wired into both Stage-D emitters:

- `src_run2_qa_emit_v1.py` — refuses to rewrite the Stage-D QA report; still prints the
  live suite result, so the suite stays verifiable.
- `src_run2_mutations_v1.py` — refuses to rewrite the Stage-D mutation report; fixtures
  still run and still fail the process on a miss.

Both degrade gracefully rather than crashing, so the protection cannot be worked around by
someone simply wanting the script to finish.

`python3 docs/source/tools/src_historical_freeze_v1.py` audits all four frozen artifacts
and exits non-zero on drift.

Four artifacts frozen, four enforced, four intact.

---

## Scope

- No previous commit was amended.
- The corrected live gate was **not** reverted.
- Only the three drifted historical files were restored; nothing else was rolled back.
- Live protections may still evolve through new commits. Finished stages' reports may not.
