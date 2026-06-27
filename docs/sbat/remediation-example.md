# SBAT remediation examples (illustration only)

> **Illustration, not content import.** These two cases are summarized from prior CIDB remediation
> work to show the governed loop in action. **No CIDB content, assets, or SCORM specifics are stored
> in this repo** (ADR non-goal); only the governance shape is shown. The cases live in
> `cidb-k1pl1t1-prototype`, which is **not** touched.

The loop being illustrated:
```
audit finding → source check → limited edit → diff → validation → commit → unresolved items stay open
```

## Case A — Q2 distractor: plausibility ≠ source
- **Finding:** a quiz distractor read a *plausible but unsourced* waterproofing material; SB Bariah's
  source named a different one. Plausible-but-wrong risks an AI-fabricated "fact" passing as official.
- **Source check:** SB source identified the correct value; the distractor was not source-backed.
- **Limited edit:** changed **only** the one distractor's text to the source-backed value;
  `is_correct` stayed `false` (it remains a distractor, just a *correct* distractor).
- **Diff / decision:** shown as `- old` / `+ new`, routed to the human gate → `COMMITTED` after
  ratification.
- **Lesson → field mapping:** quiz-option governance (field 4) at **option** granularity; source flag
  (field 3) beats plausibility.

## Case B — scope count 6-vs-7
- **Finding:** the declared scope count disagreed with the implemented slide IDs (one extra slide
  present in navigation but not counted).
- **Source check / validation:** `SCOPE_CONSISTENCY_CHECK` — declared count vs implemented IDs vs
  excluded IDs vs storyboard total failed to reconcile.
- **Limited edit:** corrected the declared count to a consistent value; nothing else changed.
- **Lesson → field mapping:** slide implementation status (field 1) + the scope check
  (`validator-notes.md`, Check 1). Trivial as code, serious as governance.

## Case C — report-only (no source)
- **Finding:** two distractors were *suspected* fabricated, but **no** SB-sourced replacement existed.
- **Action:** **reported, not edited** → `REPORT_ONLY`; the items stayed **open**.
- **Lesson → field mapping:** human decision gate (field 6) + the report-only doctrine. *AI
  accelerates; humans decide.*

## Why these three
Each maps directly to an M1 governance field and to a validator check, demand-pulling the M1 scope —
no field or check exists here that a real finding did not require.
