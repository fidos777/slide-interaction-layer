# Stage 4.2F-E — run manifest

Branch `claude/verify-powerpoint-file-vpfzkg`, started from the clean Stage 4.2F-D HEAD
`b603f44`. No prior commit was amended. T04 was not reopened. No K5 or K3 instructional
decision was modified.

---

## The premise of this run did not hold

The brief states that a local K2 binary is available at

    /mnt/data/2. PENGURUSAN PEMBINAAN LANDASAN.pdf

**It is not there, and it is nowhere else on this box.** Everything below follows from
that, and nothing below pretends otherwise.

### Locations searched

| location | method | found |
|---|---|---|
| the path the brief names | direct stat | no — `/mnt/data` is not a directory here |
| all of `/mnt` | recursive listing | no — `attach` is empty, `user-data` holds only `working` |
| whole filesystem, by exact size | `find / -size 25043306c` | no |
| whole filesystem, by name | `find / -iname '*LANDASAN*'` | no |
| all PDFs over 20 MB | `find / -iname '*.pdf' -size +20M` | no — largest PDF present is 9,039,981 bytes |
| session upload directory | listing | no — 21 files, newest 2026-08-03, nothing uploaded for this run |
| every ZIP over 1 MB | member enumeration | no — nearest is the PL06 freeze at 25,142,903 bytes, a different file |
| all runtime mounts | `findmnt` | no user-data mount carries it |
| files written in the last 3 hours | `find -newermt` | only logs and this session's own output |
| rclone remotes | `rclone listremotes` | binary absent at that path |
| Google Drive, by the known id | connector | metadata + truncated text only |

### Locations *not* searched

- any machine other than this container
- Drive folders other than the parent of the known identifier
- any CIDB internal system, SharePoint or shared drive
- email or chat outside this session

Status: **`NOT_FOUND_IN_LOCATIONS_SEARCHED`** — scoped, not an unqualified absence.

---

## Binary identity and hash result

| field | expected (from the brief) | observed |
|---|---|---|
| filename | `2. PENGURUSAN PEMBINAAN LANDASAN.pdf` | Drive title matches |
| bytes | 25,043,306 | Drive `fileSize` matches |
| SHA-256 | `0b2d81dd…f405680` | **not verified — a hash needs the bytes** |
| pages | 346 | **not verified** |
| PDF validity, encryption, image/table readability, PDF metadata | — | **`NOT_READ_BINARY_UNAVAILABLE`** |

The brief asked for the live status to move to `SOURCE_BINARY_LOCAL`,
`SOURCE_BINARY_READABLE` and `SOURCE_CONTENT_READ`. Two of those three are false and the
third is only partly true, so **none is claimed**. Moving a status because a run expected
it to move is precisely the failure this register exists to prevent, and eight QA gates
now hold that line.

### Drive binding, K2-BIND-01

The identifier `1BW-OibYv3sDyordi0YIQkb5vXeAdOtMn` resolves to a file whose title *and*
byte count both equal the brief's expected identity. That is a strong binding, recorded at
`CONNECTOR_IDENTIFIED` — one class below `LOCAL_BINARY_HASH_VERIFIED`. It is not proof of
content: two files can share a size.

### Connector text is truncated

62,638 characters for a 346-page document — about 181 a page, against the 1,500–2,000 a
page the K3 packages returned through the same connector. It ends mid-sentence inside
teaching plan PT09, and not one `KOD PL PLxx Muka Surat` marker appears anywhere, so no
page of any PL package came back.

- **Covers:** front matter, the KANDUNGAN summary table, §1.5 Silibus and its table, §1.6
  Tempoh Latihan, teaching plans PT01–PT08 in full, PT09 pages 1–2 of 6.
- **Does not cover:** every PL package body, all LATIHAN, all SKEMA JAWAPAN, appendices,
  and every image and table outside the front matter.

State: `SOURCE_CONTENT_PARTIALLY_READ`.

---

## K2-SOURCE-CONFLICT-01 — resolved

**Classification: `TYPOGRAPHICAL`. Routed to Firdaus. Not placed in any Bariah register.
The source was not altered.**

| source | kind | says |
|---|---|---|
| narrative prose, §1.5 | prose | "Panduan ini mengandungi **lapan (8) modul latihan**" |
| the silibus table, same page | table | **6** named modules, 9 LP codes |
| front-matter KANDUNGAN table | table | **6** module rows, PL01–PL09 |
| §1.6 Tempoh Latihan hours table | table | LP01–LP09 |
| the nine teaching plans | repeated sections | PT01–04→M01, PT05→M02, PT06→M03, PT07→M04, PT08→M05, PT09→M06 |

Four independent enumerations agree on **six modules and nine packages**. One prose
sentence says eight — and eight matches *nothing* in the document: not the six modules,
not the nine LP codes, not the nine PL codes, not the nine teaching plans. It is
contradicted by the table printed directly beneath it.

It is `TYPOGRAPHICAL` and not `SOURCE_AUTHORITY_CONFLICT` because the sources are not of
equal weight, and not `INSTRUCTIONAL_STRUCTURE_DECISION_REQUIRED` because nobody has to
choose: six and nine are consistently supported. There is nothing to decide, only
something to correct. Six modules and nine packages are used provisionally for
decomposition, exactly as the brief permits, and this record travels with them.

**K2-SOURCE-OBS-01** (secondary): the silibus KOD column prefixes all nine packages
`M01-`, wrong for five of the nine. A parser keyed on that column would file the entire
course under M01 — the same defect the K3 queue carried until Stage 4.2F-D. K2 unit IDs
are built from the teaching-plan headers instead, and a gate enforces it.

---

## Page and boundary map result

**Not produced.** The 346-page decomposition, the per-PL page spans, the rendered-PDF page
oracle, the table-heavy extraction paths and the image and table counts all require the
binary. None was attempted and none was estimated.

What *was* derived, from the source's own repeated headers and footers:

| PT | module | plan pages | tajuk |
|---|---|---|---|
| PT01 | M01 | 8 | PENGENALAN MODUL PEMBINAAN LANDASAN (TRACKWORKS) |
| PT02 | M01 | 6 | PENGURUSAN OPERASI PERNIAGAAN DALAM PEMBINAAN LANDASAN |
| PT03 | M01 | 7 | REGULASI DAN PEMATUHAN INDUSTRI REL DALAM PEMBINAAN |
| PT04 | M01 | 7 | INOVASI DAN TEKNOLOGI DIGITAL SERTA AUTOMASI DALAM |
| PT05 | M02 | 7 | PENGURUSAN TENDER DALAM PEMBINAAN LANDASAN |
| PT06 | M03 | 7 | PELAKSANAAN DAN PENGURUSAN KONTRAK PEMBINAAN LANDASAN |
| PT07 | M04 | 6 | PERANCANGAN DAN PENJADUALAN PEMBINAAN LANDASAN |
| PT08 | M05 | 8 | PENGURUSAN OPERASI PEMBINAAN LANDASAN |
| PT09 | M06 | 6 | PENYERAHAN PROJEK PEMBINAAN LANDASAN |

62 teaching-plan pages, each read from that plan's own `Muka Surat: n/N` footer. These are
teaching-plan lengths and are **not** the lengths of the corresponding PL packages.

---

## Structure

```
CONFIRMED_K2_UNITS       = 0
K2_CANDIDATE_STRUCTURES  = 9
K2_UNMAPPED_REGIONS      = 1   (the whole PL package body)
```

| module | title | packages |
|---|---|---|
| M01 | PENGURUSAN OPERASI PERNIAGAAN | PL01, PL02, PL03, PL04 |
| M02 | PENGURUSAN TENDER | PL05 |
| M03 | PENGURUSAN DAN PELAKSANAAN KONTRAK | PL06 |
| M04 | PERANCANGAN DAN PENJADUALAN PROJEK | PL07 |
| M05 | PENGURUSAN OPERASI PEMBINAAN | PL08 |
| M06 | PENYERAHAN PROJEK | PL09 |

PL06, PL07 and PL09 are named outright by their own teaching plan. The other six are
mapped by ordinal position, and that inference is labelled as one rather than presented as
a reading.

Every package is a `CANDIDATE_STRUCTURE`. A PL code with a module and a teaching plan is a
structure, not a unit — nothing about its page span or internal boundaries is known.
**Nothing is claimed as a confirmed unit**, and one PL is not assumed to be one storyboard
unit.

---

## First clean units extracted and modelled

**None — and this is the honest outcome, not an omission.**

The brief's own selection criteria for a `SOURCE_READY_CLEAN` candidate begin with *binary
readable* and *boundary independently confirmed*. Both are false for all nine packages. No
candidate qualifies, so none was selected, and no controlled extraction, model, ambiguity
register or runtime-state estimate was fabricated to fill the slot.

Commit 2 of the required three was therefore skipped, as the brief's own commit discipline
directs when a lane produces no artifact.

---

## K2 decision register

**Not generated**, deliberately. The brief says to produce one *only if the source evidence
shows course-level decisions are required*, and not to build a questionnaire prematurely.

The one K2 question raised so far — the module-count discrepancy — is a source correction
owned by Firdaus, not an instructional decision. Unit grouping, assessment treatment,
Rumusan convention and dialogue use are all genuinely open, but every one of them depends
on a decomposition that could not be performed. Asking Bariah to rule on the shape of
content nobody has read would waste the review.

---

## Queue changes

Live queue is now **`PRODUCTION_QUEUE_v4`**.

| count | Stage 4.2F-D | Stage 4.2F-E |
|---|---|---|
| confirmed production units | 23 | 23 |
| candidate structures | 22 | **31** |
| unresolved source records | 1 | **0** |
| immediately executable units | 13 | 13 |
| extracted units | 14 | 14 |
| source-content-read units | 9 | 9 |
| model-ready units | 23 | 23 |
| ready-to-emit units | 0 | 0 |
| total rows | 46 | **54** |

The single `K2-MONOLITH-UNRESOLVED` row is retired. It said one true thing — the binary is
missing — and hid nine structures the source's own tables evidence. The binary is still
missing; that fact now travels on each of the nine rows as its exact blocker instead of
standing in for the whole course.

`IMMEDIATELY_EXECUTABLE_UNITS` did **not** move. Nine new rows arrived and not one of them
is executable, which is the point of keeping that metric narrow.

### Named member lists

```
IMMEDIATELY_EXECUTABLE_UNIT_IDS (13)
  K5-PL06-T01-B01  K5-PL06-T01-B02  K5-PL06-T01-B03
  K5-PL06-T02-B01  K5-PL06-T02-B02  K5-PL06-T03-B01
  K5-PL06-T03-B03  K5-PL06-T03-B04  K5-PL06-T03-B05
  K5-PL06-T04-B01  K5-PL06-T05-B01  K5-PL06-T06-B01
  K5-PL06-T07-B01

READY_TO_EMIT_PPTX_UNIT_IDS (0)
  none
```

K2 is also reported separately, so a course whose binary is missing cannot inflate a
project-wide figure: 9 candidates, 0 confirmed, 0 immediately executable, 0 extracted,
0 model-ready.

### Blockers by owner

| owner | Stage 4.2F-D | Stage 4.2F-E | what unblocks them |
|---|---|---|---|
| BARIAH | 22 | 22 | K5 pattern package v1.2, and K3-COURSE-01 |
| CAIR | 22 | 22 | unit-granularity decisions on the K5 candidates |
| FIRDAUS | 1 | **9** | the K2 binary — one blocker, nine rows |
| none | 1 | 1 | `K5-PL06-T03-B02`, the delivered proof |

---

## Stale queue retirement

```
PRODUCTION_QUEUE_v1 = REMOVED_FROM_LIVE_TREE_AS_SUPERSEDED
PRODUCTION_QUEUE_v2 = REMOVED_FROM_LIVE_TREE_AS_SUPERSEDED
PRODUCTION_QUEUE_v3 = REMOVED_FROM_LIVE_TREE_AS_SUPERSEDED
SUPERSEDED_BY       = PRODUCTION_QUEUE_v4
```

Nine files removed from the working tree. **Git history is untouched** — every file remains
in every commit that contained it.

The brief named v2. v1 and v3 were retired alongside it because the same instruction
requires automation and human-facing indexes to point at one live queue only, and leaving
two other superseded queues on disk would contradict that. The widening is recorded here
rather than done quietly. A gate now asserts that exactly one queue version is live and
that it ships all three projections.

---

## QA and fixtures

```
SUITE_ID = STAGE_4_2F_E_K2_QA_v1
GATES    = 70   (70 passed, 0 failed)
FIXTURES = 51   (51 detected, 0 missed)
BASELINE = 70/70
ORACLE_SEPARATION_STRUCTURAL = DEFERRED_BY_DELIVERY_DEADLINE
```

Own identity, own total. Oracle bases: 36 `BRIEF_LITERAL`, 14 `SOURCE_TEXT_LITERAL`,
2 `CONNECTOR_METADATA`, 18 `INDEPENDENT_MEASURE`. **No gate claims to have read the
binary**, and one gate asserts that no gate does.

Every one of the 51 fixtures is a version of the single defect this run could most easily
have committed — claiming the binary was seen: a status upgraded because the brief expected
it, an unknown that becomes a number, a truncated read described as complete, a candidate
promoted to a unit, a typographical slip escalated to Bariah.

### One sibling gate was changed, and it is named

`STAGE_4_2F_D_RELEASE_FACTS_QA_v1` carried
`K2_REMAINS_AN_UNRESOLVED_SOURCE_RECORD_NOT_A_UNIT`, asserting every K2 row was
`UNRESOLVED_SOURCE`. This run was explicitly required to end that condition, so the gate
would have gone red. Its *intent* was never "K2 must stay unresolved" — it was "K2 must not
be promoted to a production unit on the strength of a missing binary". That intent is
unchanged and the gate now reads `NO_K2_ROW_IS_A_CONFIRMED_PRODUCTION_UNIT`. The fact
moved; the protection did not. Its fixture was repointed and Stage 4.2F-D is still 60/60
with 44/44 detected.

---

## Artifacts

| # | artifact | status |
|---|---|---|
| 1 | `K2_BINARY_CUSTODY_v1.{json,md}` | delivered |
| 2 | `K2_SOURCE_CONFLICT_01_v1.{json,md}` | delivered |
| 3 | `K2_COURSE_HIERARCHY_v1.{json,md}` | delivered, partial by evidence |
| 4 | PDF page and boundary map | **not produced — needs the binary** |
| 5 | assessment and answer-scheme inventory | **not produced — needs the binary** |
| 6 | image and table inventory | **not produced — needs the binary** |
| 7 | confirmed-unit and candidate-structure register | delivered (0 confirmed, 9 candidates) |
| 8 | first two clean controlled extractions | **not produced — no candidate qualifies** |
| 9 | first two provisional models | **not produced — no candidate qualifies** |
| 10 | K2 decision register | **not produced — deliberately, see above** |
| 11 | `PRODUCTION_QUEUE_v4.{json,md,csv}` | delivered |
| 12 | `QUEUE_RETIREMENT_v1.{json,md}` | delivered |
| 13 | `STAGE_4_2F_E_QA_REPORT_v1.{json,md}` | delivered |
| 14 | `STAGE_4_2F_E_MUTATION_REPORT_v1.md` | delivered |
| 15 | this file | delivered |

## Not generated

No final storyboard PPTX. No MMD, React, SCORM or LMS artifact. No new framework or QA
architecture — the K2 suite reuses the existing gate/fixture shape exactly. No K5 or K3
rule was applied to K2: K2 carries no assessment classification at all, because no K2
assessment has been read. No Bariah decision was invented, and no answer key was approved.

## What would unblock the rest

Place the 25,043,306-byte PDF on local disk. Every lane that could not run — the 346-page
decomposition, the page oracle, the table paths, the two clean models, and any K2 decision
register worth Bariah's time — becomes executable immediately, and PyMuPDF is already
available here.
