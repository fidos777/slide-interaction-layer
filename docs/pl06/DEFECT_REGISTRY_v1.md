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
| **#14** | **Stage 4.2F-K** | **the five B03 canonical fixtures** | **repaired** |

### Occurrence #14

| Field | Value |
|---|---|
| affected fixtures | `PL-46` … `PL-50`, the five B03 canonical-copy fixtures |
| defect | all five assert against the packet RECORD while the deck Bariah receives is emitted by the calibration lane. The record held the approved C1 dialogue; the emitted deck carried `WATAK: PENDING_UNIT_REVIEW` and three static `[S]` statements. |
| result | five green fixtures over a deck that violated E1 and carried none of the approved copy |
| detected_by | **reading the emitted artifact** — no gate and no fixture caught it |
| detected_by_reading | **true** |
| built | in the same session that registered #13 |
| repair | five artifact-level gates that read the emitted PPTX, fixtures `KB-01` … `KB-06` |

Knowing the defect class did not prevent producing another instance of it, and this time no
fixture caught it either. The only thing that did was opening the file.

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

## D. STALE_COMMENT_AUTHORISES_SUPERSEDED_BEHAVIOUR

> Code is correct against a decision that has been withdrawn. The comment citing that
> decision is the thing that makes the behaviour look justified.

| # | Recorded at | Locus | Status |
|---|---|---|---|
| **#1** | Stage 4.2F-K | `k5_calib_model_v1.scenario()` | repaired |

`scenario()` built a cast-free `SITUASI` frame. Its `SCENARIO_FORMAT_BASIS` read: *"The
committed unit model records dialogue verdict NOT_JUSTIFIED for this unit, so the cast-free
SITUASI frame is used."* That verdict had already been superseded by **SUP-03** under **E1**,
which makes S02 a dialogue for every K5 unit. The code did exactly what the comment said, and
the comment was describing a withdrawn decision. It is the enabling condition for occurrence
**#14**: the reviewer reading `scenario()` sees a justification and stops.

**Control.** A comment that cites a decision id as justification is a claim about that
decision's current status, and it ages exactly as fast as the decision does.

### Toolchain sweep — comments citing a decision id as justification

| Locus | Comment cites | Current status | Action |
|---|---|---|---|
| `k5_calib_model_v1.py` `SCENARIO_FORMAT_BASIS` | `dialogue.verdict = NOT_JUSTIFIED` | **SUPERSEDED** by SUP-03 / E1 | rewritten; the defect that caused #14 |
| `k5_calib_model_v1.py:384` `# S02 shell: scenario (D3 mandatory)` | Kelompok 0 `D3` | requirement holds but the **locus is wrong** — E1 is what makes S02 a dialogue | corrected to E1 |
| `k5_pattern_policy_v1.py:142`, `:522` | `B2` "test required, neither approved nor pending" | **SUPERSEDED** by F5 (3 panels frozen) | supersession note added; the 4 Aug record itself left unchanged |
| `pl06_unit_model_v1.py:42` | `RP-009` / `RP-010` VERIFY flags | **SETTLED** by A7 at K5 scope | note added |
| `k5_calib_model_v1.py:268–279` `A6` labels | `A6` | current, with the D3 rule 1 display supersession already stated inline | no action |
| `k5_calib_model_v1.py:461,465` | `D3 rule 1`, `D4(a)` | current | no action |
| `k5_calib_build_v1.py:50` | `F5` resolves `B2` | current | no action |
| `pl06_packet_model_v1.py` `D1 D2 D3 E2 C3 F3 F4` | — | all current | no action |
| `k5_calib_model_v1.py:314` `A4` | `A4` | data label, not a justification; `applied_in_this_deck = False` | no action |

---

## E. MEASUREMENT_INSTRUMENT_DELTA

> Two instruments measure the same artifact and disagree by a small constant. Until that is
> shown to be the instrument, it must be treated as unexplained movement.

| # | Recorded at | Quantity | Status |
|---|---|---|---|
| **#1** | Stage 4.2F-K | worst body-to-footer clearance | **resolved — instrument, not content** |

After the approved C1 and D1 copy was wired into the deck, my clearance measurement returned
**34.4 / 104.8 / 29.1 pt** against owner baselines of **35.2 / 105.8 / 30.2 pt** — about 1pt
tighter on all three, same worst page each time.

**Test.** The three previous blobs were extracted from commit `3766cfa` and measured with the
SAME instrument, before any further regeneration.

| File | Old blob, my instrument | New file, my instrument | Owner baseline |
|---|---|---|---|
| storyboard (87,699 B) | **34.4pt page 9** | 34.4pt page 9 | 35.2pt page 9 |
| lampiran 2-panel (69,364 B) | **104.8pt page 14** | 104.8pt page 14 | 105.8pt page 14 |
| lampiran 3-panel (59,866 B) | **29.1pt page 4** | 29.1pt page 4 | 30.2pt page 4 |

The old blobs return the same values as the new files. **The ~1pt is instrument resolution,
not content movement.** No page offends in either method and the worst page is identical.

**Both methods stated.** Mine: LibreOffice → PDF, PyMuPDF text-block extraction, clearance =
`footer_top_pt − max_text_bottom_pt` over blocks with `max_text_bottom_pt > 0`. The residual
constant is most likely a raster/text-block boundary convention. Excluding empty-body pages
made no difference here — both filters returned the same worst page and value, so the earlier
"cover reports 0.0pt" explanation I offered was wrong for these files.

**Consequence.** The baseline is now clean, so clearance movement after the F4 regeneration is
interpretable against **34.4 / 104.8 / 29.1** measured by this instrument.

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
