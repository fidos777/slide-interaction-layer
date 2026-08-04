# Stage 4.2F-C — run manifest

**Fill the production queue while Bariah reviews the pattern package**

```
BRANCH         = claude/verify-powerpoint-file-vpfzkg
CONTINUES FROM = f55db06
STAGE          = 4.2F-C
AUTHORITY      = SRC-AUTH-01
SUITE_ID       = PROJECT_SOURCE_CUSTODY_QA_v1
```

`K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2.docx` was treated as `PENDING_BARIAH_REVIEW`
throughout. It was not read, cited, or applied. No default from it became a rule.

---

## Lane 0 — SRC-AUTH-01

Source-processing authority recorded once, at source-package level, owned by
`FIRDAUS_PROJECT_DELIVERY_AUTHORITY`, status `APPROVED`, scope the official K5, K3 and K2
source packages. Six permitted operations; six explicit exclusions, and the exclusions are
the half that does the work — no instructional approval, no frozen grouping or treatment, no
approved answer key, no approved visual direction, no client release, no Bariah decision
replaced.

`PL06-B1-D-25` is preserved unchanged in the batch 1 package as the question that was asked.
The live relationship is recorded separately:

```
PL06-B1-D-25  SUPERSEDED_FOR_LIVE_PROCESSING_BY  SRC-AUTH-01
```

The record also names what SRC-AUTH-01 does **not** unblock: STOP-006 cast binding, and the
pattern package still under review.

## Lane 1 — source custody

Twelve packages. **2 hash-verified locally, 1 connector-text-readable, 9
connector-identified, 0 unavailable.** Ten carry `SHA256_NOT_COMPUTED_NO_LOCAL_BINARY` rather
than a plausible-looking value.

**The K5 module binary was believed unavailable and is not.** The uploaded Stage 4.2F-A2
freeze package carries the source DOCX in full:

```
bytes   16,832,861   matches the pinned identity
sha256  5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7   matches
format  valid OOXML — 6,167 body paragraphs, 51 tables, 52 media parts, 82 package parts
```

The rendered PDF is in the same package and matches its own frozen hash
(`295a1749…`, 9,039,981 bytes, 350 pages).

All seven frozen boundary anchors were opened in the binary and read back. Every one lands on
its named heading. The indices are python-docx body paragraphs; a naive count of every `<w:p>`
gives 7,481 and lines up with nothing. The anchors carry a section numeral the body text does
not, because Word supplies it from list numbering, so the match is on heading text and the
record says so.

K3 and K2 were located under the official source root `1JRa1p9oGjZTWz1L6-1NPH2cW3jJpUKRF`,
whose five numbered course folders tie a course code to a package. K5 is corroborated
independently by the PL06 custody record's own folder and file IDs.

## Lane 2 — PL06 batch 1 controlled extraction

**418 controlled rows** across four units, extracted by named heading anchor, never by page
range.

| Unit | Pages | Rows | Structural headings | Tables | Figures |
| --- | --- | ---: | ---: | ---: | ---: |
| K5-PL06-T03-B03 Infrastruktur | 250–255 | 76 | 39 | 0 | 0 |
| K5-PL06-T03-B04 Badan Air | 255–261 | 92 | 36 | 0 | 0 |
| K5-PL06-T05-B01 Pengurusan Kualiti Projek | 284–293 | 132 | 44 | 0 | 0 |
| K5-PL06-T06-B01 Perlindungan Alam Sekitar | 294–302 | 118 | 37 | 0 | 1 |

**The reader was checked, not asserted.** Run over T04's own boundary it reproduces the
committed `T04_SOURCE_EXTRACT_v1.json` exactly — same row count, same text, same content
types, same paragraph indices, same totals. `t04_extract_v1` is untouched.

**Shared boundaries are proved.** T03-B03 ends on the paragraph before "Badan Air (Water
Body)" and T03-B04 begins on it: contiguous, gap zero. The last record excluded before
T03-B03 is T03-B02's "BBQ pit". No row in any unit lands inside another unit's span.

Every unit also produced: exact headings and subheadings, mandatory content propositions,
source-supported assessment propositions, candidate visual subjects, terminology and
compliance-sensitive statements, an ambiguity register, a missing-source register, and
extraction QA.

## Lane 3 — provisional unit models

Four models. Every element classified `SOURCE_DERIVED`, `CAIR_PROPOSAL`,
`COURSE_RULE_ALREADY_APPROVED`, `PENDING_BARIAH_PATTERN_DECISION` or
`PENDING_UNIT_EXCEPTION_REVIEW`. Nothing frozen: screen count, sequence, dialogue, Rumusan
form, pattern family, assessment key, visual reuse.

| Unit | Groups | Min screens | Propositions | Quiz | Visual subjects | Dialogue |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| T03-B03 | 6 | 11 | 9 | 5 | 4 (0 attested) | NOT_JUSTIFIED |
| T03-B04 | 5 | 10 | 8 | 5 | 3 (0 attested) | NOT_JUSTIFIED |
| T05-B01 | 4 | 10 | 8 | 5 | 3 (0 attested) | JUSTIFIED |
| T06-B01 | 3 | 8 | 8 | 5 | 3 (1 attested) | UNCERTAIN |

Twenty source-backed assessment stems, 4 MCQ + 1 MR per unit. Every stem and every correct
response cites the rows it came from; the distractors are ours and say so. Key status
`DRAFTED_NOT_APPROVED`, authority `NONE`.

Thirteen candidate visual subjects, of which exactly **one** has a figure behind it — Rajah 26
in T06-B01. The other twelve are readings of text and are labelled as such.

No character name is proposed anywhere; STOP-006 is open.

## Lane 4 — K3 inventory

Nine PDFs under `10QLkopBVCp4TwaYbofAiStmqGsNTHvQe`. **Two read in full, seven identified and
not read.** The seven are recorded `IDENTIFIED_NOT_READ` with page count `UNKNOWN_NOT_MEASURED`
rather than described from the template the two read files share. Each full text read costs a
large fixed amount of this run's working context; reading all nine would have left the
remaining lanes undone. That is the reason, and it is stated rather than hidden.

| PL | Pages | Top sections | Tables | Figures | LATIHAN | SKEMA | Class |
| --- | ---: | ---: | ---: | ---: | --- | --- | --- |
| PL01 | 17 | 7 | 2 | 7 | yes | yes | SOURCE_READY_CLEAN |
| PL03 | 9 | 3 | 1 | 0 | yes | yes | SOURCE_READY_CLEAN |

Two provisional models built, using the same classifications as Lane 3.

**One PDF is not assumed to be one unit.** Both read files are self-contained — own header,
own page numbering from 1, own LATIHAN, own SKEMA JAWAPAN — so on that evidence each is one
candidate unit. Whether a 9-page PL and a 17-page PL should both become single storyboard
units is an instructional question and is not answered here.

**`K3-SRC-CONFLICT-01`** — PL01's header and PL03's header disagree about PL02's title.
Recorded, not resolved; PL02 was not read.

**`K3-ASSESS-01`** — every K3 package ships its own LATIHAN and SKEMA JAWAPAN: short-essay
questions with model answers and mark allocations. The course-wide rule is 4 MCQ + 1 MR. The
source assessment and the course format do not match. Three options are listed and none is
chosen — this is exactly what the pattern package exists to settle, and the source answers
are strong enough that guessing would waste them.

## Lane 5 — K2 monolith

```
OUTCOME  = NOT_PERFORMED_LOCAL_BINARY_UNAVAILABLE
FILE     = 2. PENGURUSAN PEMBINAAN LANDASAN.pdf
DRIVE ID = 1BW-OibYv3sDyordi0YIQkb5vXeAdOtMn
BYTES    = 25,043,306 (Drive metadata)
```

Every field this lane was asked to produce is `UNKNOWN_NOT_MEASURED`. None is estimated — not
the page count, not the unit count, not the image or table inventory. A 25 MB PDF may be 100
image-heavy pages or 900 text pages, and a guess would put a number nobody measured into the
production queue.

What would unblock it: the PDF on local disk, where PyMuPDF is already available and gives the
page count, heading tree, images and tables directly; or a connector that can return a named
page range rather than the whole file.

**This is the one lane that did not complete.** Every other lane continued.

## Lane 6 — remaining K5 inventory

Measured from the verified binary: each heading located in the DOCX body, its printed page
read off the typeset PDF footer.

**The module contains EIGHT Pakej Latihan, not seven.** Its own syllabus table on module pages
xvii–xviii lists PL01 to PL08, and every one has body headings. The lane was scoped to
PL01–PL05 and PL07; **PL08 "Inovasi & Teknologi Landskap" exists**, occupies module pages 316
onward, and is inventoried here rather than left unmentioned.

| PL | Title | Pages | Sub-modul | Confirmed | Candidate |
| --- | --- | --- | ---: | ---: | ---: |
| PL01 | Pengenalan Dan Latar Belakang Industri | 1–32 | 4 | 0 | 4 |
| PL02 | Pengurusan Operasi Perniagaan | 33–76 | 3 | 0 | 3 |
| PL03 | Pengurusan Tender | 77–131 | 8 | 0 | 8 |
| PL04 | Pelaksanaan Dan Pengurusan Kontrak | 132–155 | 2 | 0 | 2 |
| PL05 | Perancangan Dan Penjadualan Projek | 156–161 | 2 | 0 | 2 |
| PL06 | Pengurusan Operasi Pembinaan Landskap | 162–309 | 7 | **14** | 0 |
| PL07 | Penyerahan Projek | 310–315 | 2 | 0 | 2 |
| PL08 | Inovasi & Teknologi Landskap | 316–332 | 1 | 0 | 1 |

```
CONFIRMED_UNIT          = 14   (PL06 only — the one PL with a frozen boundary map)
CANDIDATE_UNIT          = 22   (sub-modul headings, one candidate each)
UNMAPPED_SOURCE_REGION  = 7    (184 of 332 module pages)
```

The prior planning estimate of ~33 units is **not carried forward as a production fact**.

Findings: PL07's syllabus entry repeats PL02's third sub-modul (source anomaly, recorded not
corrected); PL03 begins two top-level headings on the same printed page 80 (a shared-page
boundary risk); PL05 and PL07 are six pages each while PL03 is fifty-five, so unit counts
cannot be spread evenly. The K5 module carries **no LATIHAN or SKEMA JAWAPAN anywhere** —
unlike K3.

## Lane 7 — production queue

46 rows, every column and every percentage computed from artifacts on disk.

```
CONFIRMED_UNITS   = 16
CANDIDATE_UNITS   = 30
SOURCE_READY      = 45  (97.8%)
EXTRACTED         =  8  (17.4%)
MODEL_READY       =  8  (17.4%)
BLOCKED           = 45
```

By course: K5 36 rows, K3 9, K2 1. Blockers by owner: **CAIR 37, BARIAH 7, FIRDAUS 1**. The
single FIRDAUS blocker is the K2 monolith.

## Targeted QA

```
SUITE_ID = PROJECT_SOURCE_CUSTODY_QA_v1
63/63 active gates PASS, 0 vacuous
54 mutation fixtures, 54 detected, 0 missed
```

Gate types: ORACLE 13, QUEUE 9, PENDING 8, ACCOUNTING 7, AUTHORITY 7, BOUNDARY 7,
EXTRACTION 7, CUSTODY 5. Deliberately narrow — the ten named protections plus the new source
and queue paths. No historical gate or fixture was refactored. Never added to
`PL06_AUTHORITY_HARVEST_BATCH1_QA_v1` (132) or `T04_STATE_COVERAGE_QA_v1` (108).

### Where a green suite hid a defect

**Page attribution was wrong on every unit in the batch.** The T04 extractor counted Word's
cached `<w:lastRenderedPageBreak>`, which happened to land on T04's frozen range. On these
four it under-counts the last page of T03-B03, T03-B04 and T05-B01 by one and over-counts
T06-B01 by one. Publishing them would have contradicted the frozen map on all four while the
map was right. Page attribution now comes from the typeset PDF, which is hash-verified and
prints its own module page number in the footer; the cached-layout number is still computed
and reported as the weaker second opinion.

**A first-match page search collapsed six components onto one page.** "Fungsi" and "Fokus
Utama Kontraktor" repeat once per component in T03-B03, and a plain search sent every one of
them back to page 250. The search is now forward-only from the current page, and the result
is monotonic.

**`OR-07` walked past the suite.** The regeneration gate compared two calls of the same
extractor, so a moved anchor appeared on both sides. It now reads the raw frozen boundary map.
That is the fifth time this project has found the same self-referential shape, and the remedy
was the same one each time: anchor the expected value on something the generator cannot
rewrite.

**The automatic component detector under-read T03-B04**, finding two of five water-body types.
Rather than loosen it until it agreed, the five are listed in a declared override and the
detector's own answer is kept beside it.

## Not checked

- the K2 monolith's structure — the binary is not local, and the lane records that;
- seven of the nine K3 PDFs — identified, not read, and recorded as not read;
- whether any provisional model is instructionally sound;
- how any artifact renders in Microsoft Word or PowerPoint;
- whether the unmapped K5 Pakej Latihan really contain the candidate units their sub-modul
  headings suggest.

---

## Verdict

```
PRODUCTION_QUEUE_FILLED_AWAITING_BARIAH_PATTERN_DECISIONS
```

Six units are extracted and modelled and can be projected the day the pattern package returns.
Nothing instructional was decided on Bariah's behalf.
