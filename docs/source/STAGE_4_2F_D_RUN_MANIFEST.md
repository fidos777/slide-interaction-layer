# Stage 4.2F-D — run manifest

Branch `claude/verify-powerpoint-file-vpfzkg`. Started from a clean tree at `41ab01e`.
Required commits verified present before any work: `82e541f`, `d4ecb1d`, `41ab01e`.
No prior commit was amended.

**Objective:** fill the production queue and prepare units to emit storyboard PPTX
immediately after Bariah's decisions arrive.

`K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2.docx` was treated as
`PENDING_BARIAH_REVIEW` throughout. No proposed v1.2 rule was quoted, ingested or applied
as approved authority.

---

## What the run produced

| lane | outcome |
|---|---|
| 0 preflight | branch, HEAD, tree state and required commits reported; every source location searched and recorded with a scoped status |
| 1 source-status model | `SOURCE_READY` retired; 14 granular states plus an alias map; headline metric `IMMEDIATELY_EXECUTABLE_UNITS` |
| 2 K2 intake | binary not local; scoped absence recorded with the exact Drive identifier and the locations searched *and* not searched. No decomposition, no estimate |
| 3 K3 | all nine packages read in full and modelled |
| 4 K3 decision addendum | `K3_Keputusan_Peringkat_Kursus_v0_1.docx`, one page, rendered and inspected |
| 5 PL06 remaining | 8 units derived from the frozen map, extracted and modelled |
| 6 K5 PL01–PL08 | 22 candidate structures re-derived, not carried forward |
| 7 T04 page reconciliation | 32 mismatches recorded; regeneration declined with a reason |
| 8 targeted oracle check | 60 gates, 44 fixtures, `ORACLE_SEPARATION_STRUCTURAL = DEFERRED_BY_DELIVERY_DEADLINE` |
| 9 four-deck readiness | manifest for the four calibration units with an entry point each |
| 10 production queue | 46 rows, rebuilt from artifacts, no typed percentage |

---

## Source custody

Every absence statement is scoped. No unqualified `NOT_IN_CUSTODY` or `SOURCE_MISSING`
appears in any live register — a QA gate enforces it.

| source | status | evidence class |
|---|---|---|
| K5 module DOCX + rendered PDF | `FOUND_IN_UPLOADED_ARCHIVE` | `LOCAL_BINARY_HASH_VERIFIED` |
| K3 nine PL PDFs | `LOCATED_BY_CONNECTOR_BINARY_NOT_LOCAL` | `CONNECTOR_TEXT_READABLE` |
| K2 monolith | `NOT_FOUND_IN_LOCATIONS_SEARCHED` | `CONNECTOR_IDENTIFIED` |

K2 was searched in the repository, uploads, every ZIP on the box, all runtime mounts, by
filename and by exact byte size, and through the connector. Locations *not* searched are
named in `SOURCE_LOCATION_REPORT_v1.md` rather than left implicit. Only metadata was
available — never the binary — so no page count, unit count or content was estimated.

---

## K3 — all nine read

216 source pages, 41 questions, counted from the files rather than assumed.

| module | packages |
|---|---|
| M01 BUSINESS OPERATION MANAGEMENT | PL01, PL02, PL03 |
| M02 TENDERING MANAGEMENT | PL04 |
| M03 CONTRACT IMPLEMENTATION & MANAGEMENT | PL05 |
| M04 PROJECT PLANNING AND SCHEDULING | PL06 |
| M05 CONSTRUCTION OPERATION MANAGEMENT | PL07, PL08 |
| M06 PROJECT HANDOVER | PL09 |

Stage 4.2F-C recorded a single module code from two packages. That is now superseded; the
v1 artifacts are left on disk unchanged as the honest record of what was known then.

Three things the full read established that a template would have hidden:

1. **The question count is not uniform.** Seven packages carry five; PL01 and PL03 carry
   three.
2. **The answer keys take four structural shapes under six labels** — two-column table
   (PL01, PL02, PL06), prose (PL04, PL07, PL09), bulleted (PL05, PL08), rubric (PL03).
3. **PL03 is not a model answer at all.** It is a marking rubric with explicit allocations
   (2 + 4 + 4 = 10 marks a question) — instructions to a marker, not something a learner
   can be shown. It is the only one of the nine that states marks anywhere.

The K5 rule (4 MCQ + 1 Multiple Response, 60 percent) was **not** applied. Every K3 model
classifies assessment as `PENDING_K3_COURSE_ASSESSMENT_RULE`. The open question did not
block source reading, content extraction, visual modelling or screen modelling — all four
were completed for all nine.

### Observations routed to Firdaus, not to Bariah

None of these needs an instructional decision, so none is in the addendum.

- **K3-SRC-CONFLICT-01** — PL01's front matter is shifted one row from its second entry:
  the PL02 row duplicates PL01's title and the PL03 row carries PL02's title, so PL03's
  real title appears nowhere in it. Two rows are wrong, not one; reading PL03 established
  the full extent. Classified `TYPOGRAPHICAL`. Three independent sources agree on PL02's
  correct title.
- **K3-SRC-OBS-01** — PL08's last page footer reads `1/13`, not `13/13`.
- **K3-SRC-OBS-03** — PL01 and PL02 use `Page:`, the other seven `Muka Surat:`. A page
  oracle anchored on one spelling silently returns zero pages for the other two.

---

## K3-COURSE-01

`reviews/storyboard-bariah/k3_course_decision/K3_Keputusan_Peringkat_Kursus_v0_1.docx` —
one page, A4, deliberately **not** folded into the K5 Kelompok 0 package that is under
review right now. Four options A–D, each with its production consequence and cost, a tick
box per option, a signature line.

`cair_recommendation` is `None`. Eight packages supply answer keys that could be used
directly; PL03 does not. Choosing a format without Bariah would either waste the eight or
hide the PL03 gap.

Rendered to PNG and visually inspected: one page, all Malay, four options legible, tick
boxes and signature line present. The DOCX was verified structurally (parts, zip integrity,
table grid, expected strings). It was **not** opened in Microsoft Word — there is still no
Writer filter in this environment, and the one-page claim rests on the PIL preview and the
OOXML parts, not on Word.

---

## PL06 — remaining units

Derived from the frozen boundary map, not assumed. 14 frozen units, 6 already represented,
so **8 remain** — not 8 by assumption, 8 by subtraction, and a gate re-derives it from the
raw map on disk against a hand-typed represented list.

Extracted and modelled: `K5-PL06-T01-B01`, `T01-B02`, `T01-B03`, `T02-B01`, `T02-B02`,
`T03-B01`, `T03-B05`, `T07-B01`.

Model depth is stated rather than implied: propositions are derived mechanically by a
published rule; assessment items, Rumusan beats and dialogue verdicts are left
`PENDING_UNIT_EXCEPTION_REVIEW` rather than guessed. No T04 screen count, dialogue,
character, Rumusan structure, visual obligation, asset group or interaction-child count was
inherited.

---

## K5 PL01–PL08

22 candidate structures — **re-derived** from the module's own syllabus and body headings,
not carried forward. The number is the same as the previous queue's because the evidence is
the same, not because it was inherited (`count_confirmed = true`).

- 7 confirmed units, 20 clean candidates, 2 amber, 7 unmapped source regions over 184 pages.
- No candidate structure is called a final deck. Extraction was **not** performed on
  candidates: a sub-modul heading is not a unit, and extracting one would fix a granularity
  nobody has decided.
- Amber candidates carry exact boundary evidence and no invented grouping.

---

## T04 page reconciliation

Narrow record only. No T04 content, interaction or authority decision was reopened, and no
further T04 architecture work was done.

100 rows, 93 resolved, 7 unresolved, **32 mismatches**. Cause: the committed extract
attributed pages by counting Word's cached `<w:lastRenderedPageBreak>`, which drifts — the
same defect Stage 4.2F-C found in the batch 1 units, present in T04's own extract.

`regenerate = false`. The drift lives in internal JSON registers; both decks were re-opened
from disk and no module page number reaches either. Regenerating a reviewed artifact to fix
a number nobody can see would be churn.

---

## Production queue

Rebuilt from artifacts. No percentage is typed anywhere; the retired 97.8 percent figure
appears only inside the record that retires it, and a gate enforces exactly that.

```
IMMEDIATELY_EXECUTABLE_UNITS = 13
```

| count | value |
|---|---|
| confirmed production units | 23 |
| candidate structures | 22 |
| unresolved source records | 1 |
| immediately executable units | 13 |
| extracted units | 14 |
| source-content-read units | 9 |
| model-ready units | 23 |
| waiting-authority units | 44 |
| ready-to-emit units | 0 |
| total rows | 46 |

**`extracted_units` and `source_content_read_units` are counted separately on purpose.**
They were merged until this run. The moment nine K3 packages became "read", the merged
figure jumped from 16 to 23 and would have read as seven more units ready to work on when
none were. `EXTRACTED` means rows cut from a frozen boundary in a local binary;
`SOURCE_CONTENT_READ` means text came back through a connector and nothing has been cut.

Two identity corrections landed here as well. Every K3 row was stamped `K3-M01-<PL>`
because M01 was the only module code known when the queue was built, so the queue and the
K3 model were naming the same unit two different ways; and rows were split BARIAH/CAIR on
read-versus-unread, a split that now has no members on the CAIR side. Both are fixed, and
gates hold them fixed.

### Blockers by owner

| owner | count | what unblocks them |
|---|---|---|
| BARIAH | 22 | K5 pattern package v1.2 (13 PL06 units) and K3-COURSE-01 (9 K3 packages) |
| CAIR | 22 | unit-granularity decisions on the K5 candidate structures |
| FIRDAUS | 1 | the K2 monolith binary |
| none | 1 | `K5-PL06-T03-B02`, the delivered proof |

---

## Four-deck calibration readiness

`K5-PL06-T03-B03`, `T03-B04`, `T05-B01`, `T06-B01`. All four: source verified, extraction
complete, provisional model complete. None is ready to emit — all four wait on the pattern
package.

```
NEXT_STAGE_TRIGGER = BARIAH_K5_PATTERN_PACKAGE_INGESTED
                     AND UNIT_EXCEPTION_BLOCKERS_RESOLVED
```

Each unit carries the exact entry point to emit its PPTX once that trigger fires.

---

## QA and fixtures

```
SUITE_ID                      = STAGE_4_2F_D_RELEASE_FACTS_QA_v1
GATES                         = 60      (60 passed, 0 failed)
FIXTURES                      = 44      (44 detected, 0 missed)
BASELINE                      = 60/60
ORACLE_SEPARATION_STRUCTURAL  = DEFERRED_BY_DELIVERY_DEADLINE
```

This suite has its own identity and its own total. No gate count from
`PROJECT_SOURCE_CUSTODY_QA_v1`, `PL06_AUTHORITY_HARVEST_BATCH1_QA_v1` or any T04 suite is
merged into it, and none of them was edited to agree with it. No historical QA was
refactored and no broad repository refactor was performed.

Oracle separation is structural-deferred, so per-gate oracle *independence* is enforced
instead: 48 gates anchor on hand-typed literals, 4 re-read a raw file from disk, 8 measure
a quantity a second way. A gate whose expected value would be its own producer is not
written at all.

### Two self-referential gates caught by their own fixtures

Both were written by me in this run and both were caught before the suite shipped — the
eighth and ninth instances of this defect class in the project.

- `NO_UNIT_IS_BOTH_REMAINING_AND_ALREADY_REPRESENTED` compared the remaining set against
  the set it is derived from. It could never fail. Fixture DB-02 walked past it. Replaced
  with `REMAINING_UNITS_EQUAL_FROZEN_MAP_MINUS_THE_REPRESENTED_LITERAL`, built from the raw
  frozen map and a hand-typed list.
- `THE_QUESTION_COUNT_IS_NOT_CLAIMED_UNIFORM` asserted a property of the QA file's own
  constant, not of the model. Fixture DA-05 flattened every package to five questions and
  the gate did not notice. Replaced with a model-side gate plus
  `SHAPE_AND_PACKAGE_QUESTION_COUNTS_AGREE`, which cross-checks two independent question
  counts.

A third defect was caught by a gate working as intended: `PL06_ALREADY_REPRESENTED_LITERAL`
was typed with seven entries including `K5-PL06-T02-B02`, which is not represented — it is
one of the eight extracted this run. The literal-anchored count gate failed and the anchor
was corrected. That is the reason these anchors are typed rather than read back.

---

## Generator fixes, no hand patching

- `pl06_docx_v1.render_preview` ignored the `widths` a caller passed and divided the content
  width evenly, while `_table_xml` honoured those widths in the DOCX. Every preview of a
  width-controlled table was a picture of a table no reader would receive — and it is why
  the K3 decision page first appeared to overflow to two pages. The preview now uses the
  same column arithmetic as the DOCX. No DOCX bytes change.
- The decision page uses an ASCII tick box. U+2610 BALLOT BOX rendered as tofu in the
  preview font, and a missing glyph is a worse risk on a page whose whole job is to be
  ticked.

No generated artifact was hand-edited. Every correction went into a generator, followed by
complete regeneration.

---

## Artifacts

| # | artifact |
|---|---|
| 1 | `SOURCE_LOCATION_REPORT_v1.{json,md}`, `SOURCE_CUSTODY_MANIFEST_v1.{json,md}` |
| 2 | K2 scoped binary blocker — recorded in the location report and as one queue row |
| 3 | `K3_SOURCE_INVENTORY_v2.{json,md}` — all nine |
| 4 | `K3_PROVISIONAL_MODELS_v2.{json,md}` — all nine |
| 5 | `K3_COURSE_DECISION_v1.{json,md}`, `K3_SOURCE_OBSERVATIONS_v1.{json,md}`, `K3_Keputusan_Peringkat_Kursus_v0_1.docx` + preview |
| 6 | `docs/pl06/rest_extract/` — 8 remaining PL06 extractions |
| 7 | `docs/pl06/rest_extract/` — 8 remaining PL06 provisional models |
| 8 | `K5_STRUCTURE_INVENTORY_v2.{json,md}` |
| 9 | none — extraction on candidate structures was deliberately declined, with the reason recorded |
| 10 | `T04_PAGE_REFERENCE_RECONCILIATION_v1.{json,md}` |
| 11 | `FOUR_DECK_CALIBRATION_READINESS_v1.{json,md}` |
| 12 | `PRODUCTION_QUEUE_v3.{json,md,csv}` |
| 13 | `STAGE_4_2F_D_QA_REPORT_v1.{json,md}` |
| 14 | `STAGE_4_2F_D_MUTATION_REPORT_v1.md` |
| 15 | this file |

## Not generated

No final storyboard PPTX for any new unit. No Bariah approval record. No final answer-key
approval. No MMD, React, SCORM or LMS artifact. No new framework, MCP server or QA
architecture. CAIR is not named as Instructional Designer anywhere.
