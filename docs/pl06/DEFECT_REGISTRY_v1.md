# PL06 / K5 — defect registry v1

Consolidated register for the two recurring defect classes this project tracks across stages.
Earlier occurrences stay where they were recorded and are **not renumbered**; this file
carries the running numbering forward and adds the taxonomy entries.

---

## A. SELF_REFERENTIAL_ORACLE

> A gate that compares a value against its own source proves only that a copy succeeded.

| # | Recorded at | Gate | Status |
|---|---|---|---|
| #1–#7 | earlier stages | — | recorded in their own stage manifests |
| #8 | Stage 4.2F-D manifest | — | repaired |
| #9 | Stage 4.2F-D manifest | — | repaired |
| #10 | K5 calibration QA | montage-marks gate | repaired |
| #11 | K5 calibration QA | status-marks gate | repaired |
| #12 | K5 calibration QA | native oracle importing forbidden-band geometry from the generator under test | repaired |
| **#13** | **Stage 4.2F-J** | **`EVERY_UNIT_CLAIMING_ANALYSIS_COMPLETE_SATISFIES_THE_CONTRACT`** | **repaired** |

### Occurrence #13

| Field | Value |
|---|---|
| affected gate | `EVERY_UNIT_CLAIMING_ANALYSIS_COMPLETE_SATISFIES_THE_CONTRACT` |
| defect | population derived from a completeness flag that the model computes from the absence of the same defects the gate validates |
| result | vacuous pass by construction — the gate could never fail |
| detected_by | `PL-31` |
| detected_by_reading | **false** |
| repair | replaced by `THE_FOUR_DECLARED_ANALYSIS_UNITS_SATISFY_THE_CONTRACT`, whose population is the suite's own declared list of units |

The gate was written during the same pass that registered occurrences #10–#12. Knowing the
defect class did not prevent producing another instance of it; the fixture did.

---

## B. CITATION_VALID_CONTENT_DIVERGENT

> A controlled citation resolves correctly, but the generated sentence states content the
> cited source does not support.

The citation machinery is unaffected — the row exists, belongs to the unit, and is named. What
fails is the relationship between the sentence and the row. A traceability gate cannot see it,
because traceability was never violated.

| # | Recorded at | Cause | Status |
|---|---|---|---|
| **#1** | Stage 4.2F-J | `ANALYST_NOTE_LEAKAGE` | repaired |

### Occurrence #1 — ANALYST_NOTE_LEAKAGE

For the four units carrying a committed analysis, the S02 dialogue line was drawn from the
analysis record's `statement` field. That field is an **analyst note** — English-mixed
commentary written to explain to a reviewer why a row is compliance-sensitive:

> `Jajaran pagar mengikut Pelan Ukur Sempadan — a land-encroachment exposure.`

The line cited `T03B03-ROW-048` correctly. The row says the fence alignment must be marked
according to the boundary survey plan. It does not say "a land-encroachment exposure" — that
is the analyst's characterisation, and Encik Rahman was going to say it out loud.

**Repair.** Lines are the module's own text; the analyst note is retained beside the anchor as
the reason the row was chosen. Gate
`EVERY_SOURCE_VERBATIM_LINE_IS_TEXT_FROM_THE_ROW_IT_CITES`, fixture `PL-35`.

### What is and is not automated here

`NO_CONTROLLED_PARAPHRASE_ESCALATES_BEYOND_ITS_SOURCE` compares a paraphrase against the raw
text of the rows it cites for a declared list of obligation, prohibition, approval and legal-
duty markers. That catches **escalation** — the failure mode with the worst consequences.

It does **not** prove semantic fidelity. A paraphrase can carry no escalation marker and still
say something the source does not support, and no gate in this repository can decide that.
Content-fidelity review stays human-assisted, and no gate here claims otherwise.

---

## C. UNRESOLVED_AGAINST_AN_INCOMPLETE_INDEX

> An audit reports a citation as nonexistent when it is merely absent from the index the audit
> happened to search.

| # | Recorded at | Affected | Status |
|---|---|---|---|
| **#1** | Stage 4.2F-J | warrant-audit findings WA-01, WA-02, WA-03, WA-05 | withdrawn and repaired |

The Phase A warrant audit searched the returned authority document's Section A and
`PL06_RULE_PORTABILITY_MATRIX_v1.md`, then reported that **A6 and A7 "resolve to nothing"**.
Both exist: they are decisions of `K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2_vBariah.docx`,
dated 4 August 2026, authored by Bariah Ahmad, ingested at Stage 4.2F-G into
`docs/pl06/k5_policy/` and gated by a 93-gate suite. The audit did not search that directory.

**Standing control.** A citation that cannot be resolved is reported as
`UNRESOLVED_AGAINST_THE_REGISTERED_INDEX`, never as nonexistent, until the index is shown to be
complete. Recorded as warrant finding `WA-07`.
