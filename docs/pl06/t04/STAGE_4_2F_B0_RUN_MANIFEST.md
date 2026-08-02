# STAGE_4_2F_B0_RUN_MANIFEST

```
STAGE   = 4.2F-B0 — T04-B01 CONTROLLED SOURCE EXTRACTION
SCOPE   = SOURCE EXTRACTION AND INSTRUCTIONAL ANALYSIS ONLY
PPTX_GENERATED   = 0
GENERATOR_TOUCHED = 0
VERDICT = T04_SOURCE_COMPLETE_PENDING_TARGETED_INSTRUCTIONAL_DECISIONS
```

# 1. Pre-flight

| Check | Result |
|---|---|
| Repository / branch | `/home/user/slide-interaction-layer` · `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at start | `5535ecd76daf515e0a39852599de7f7e880eeb5e` — matches |
| Working tree | clean, 0 tracked changes |
| Stage 4.2F-A2 commit | present |
| PL06 inventory QA | **136/136** reproduced |
| PL06 mutations | **54/54** reproduced, 0 missed |
| `p294.png` | present, `e51574b6d57a034a…` |
| `p302.png` | present, `243d11590b86c6d1…` |
| Inventory units | 14 unique lesson units |

**Clarification requested in the brief.** Stage 4.2F-A2 modified the **PL06 inventory QA
gates** at `docs/pl06/tools/pl06_inventory_qa_v1.py` — five gates that the inventory rewrite
had silently switched off. It did **not** touch the production storyboard validators under
`reviews/source-completion/generator/`, which remain at their Stage 4.2E-C state
(461 gate records, 51 mutation fixtures) with zero changed files. The two suites are
independent: one governs PL06 planning data, the other governs the B02 artifact.

# 2. Primary DOCX identity

| Field | Value |
|---|---|
| Filename | `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx` |
| Bytes | **16,832,861** — matches |
| SHA-256 | `5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7` — matches |
| Drive metadata | `fileSize 16832861`, `parentId 1p18qHATFfn0oLHyCvYOfA8rQQlxkwJXS`, title matches |
| Verified | **before** any read; extraction refuses to open a non-matching file |

## 2.1 One deviation, stated

The brief said to retrieve the DOCX from Drive. The Drive connector returns file content as a
**base64 string in a tool result** — 16.8 MB becomes ~22 MB of text inline, which would end
this session, and a truncated download would hand me a corrupt file.

So: `get_file_metadata` was called live against file ID `16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4`
and confirmed the filename, the 16,832,861-byte size and the parent folder at source; the
**bytes** were taken from the verified freeze ZIP still present in the upload area outside the
repository — the same package that verified 29/29 and 30/30 at Stage 4.2F-A2, whose
`source/` member is the byte-identical DOCX.

The identity that matters was checked either way: 16,832,861 bytes and
`5a9142cd…78df7`, matched before reading. What I did **not** do is hash the bytes Drive
would have served. Drive's own metadata agrees on size and name, which is corroboration, not
proof of content.

# 3. Boundary

| | |
|---|---|
| Raw start anchor | **`PENJAAGAAN DAN PENYELENGGARAAN`** — misspelled in the body, and this is the anchor |
| Governed display label | `PENJAGAAN DAN PENYELENGGARAAN` |
| Normalisation status | **`RECORDED_NOT_SILENTLY_CORRECTED`** |
| Normalisation authority | K5-STR-005 table of contents — `REFERENCED_NOT_FROZEN` |
| Raw stop anchor | `PENGURUSAN KUALITI PROJEK` (excluded) |
| Paragraph span | **5220 → before 5360**, 140 paragraphs |
| Module pages | **276–283**, 8 distinct pages |

**Searching the body for the correctly spelled label returns zero headings.** The only match
in the document is the table-of-contents entry, which carries a page number and is not a
section start. Fixture `E-01` proves it: anchoring on the canonical spelling raises
`ExtractionError: raw start anchor not found`.

## 3.1 The paragraph index is enumeration-dependent — a finding

The frozen map's 5220/5360 hold under **one** enumeration: direct `<w:p>` children of
`<w:body>` — python-docx `Document.paragraphs` — which **excludes paragraphs nested inside
tables**. Counting every `<w:p>` in the body gives **6534** and **6674**: the same
140-paragraph span, shifted by **1314**.

Both are recorded in the extract. Extraction walks **body children between the two anchor
elements**, not the index, so a table inside the boundary would still be captured even though
the index that located the boundary cannot see one. There are none — measured.

This matters beyond T04: eleven other units carry anchors from the same map. Anyone reading
them with a different paragraph enumeration will land 1314 paragraphs away.

# 4. Extracted content

| Metric | Value |
|---|---:|
| Body elements in span | **140** |
| Content rows | **100** |
| Empty spacing paragraphs | 40 |
| Headings | 49 — 1 H1, 2 H2, 46 H3 |
| Paragraphs | 38 |
| Numbered paragraphs (`w:numPr`) | **61** |
| List-item rows (`ListParagraph`) | 12 |
| Tables | **0** |
| Diagrams | **1** |
| Raster images | **0** |
| Assets | **1** |

100 + 40 = 140. Every element accounted for.

Two counts are reported for lists because a single figure would hide the difference: 61
paragraphs carry `<w:numPr>`, but most are Heading-3 runs Word numbered; only 12 are
`ListParagraph` list items.

**Structure.** Two Heading-2 blocks. *Landskap Lembut* decomposes into three maintenance
operations — **Siram**, **Baja**, **Racun** — each with a definition, a *Kaedah Pelaksanaan*
block and an *Aspek Pengurusan untuk Kontraktor* block. *Landskap Kejur* decomposes into four
function groups, each with exactly two sub-items.

# 5. Visual, table and list inventories

**One visual in the entire unit**: a SmartArt process-flow diagram at the opening,
`word/diagrams/data1.xml`, sha `f88edf2d305a546d…`, 6.79 × 3.92 in, carrying **six named
nodes** — Koordinasi dan Demonstrasi Penyelenggaraan Taman · Penyeliaan Penyelenggaraan Taman ·
Penyeliaan Operasi Nurseri · Penyeliaan Alatan dan Mesin Penyelenggaraan Taman · Penyeliaan
Inventori Taman · Perancangan Sumber Manusia dan Kebajikan Pekerja. Status
`SOURCE_BOUND_CAPTIONLESS`, kind `SMARTART_DIAGRAM_NOT_RASTER`.

**Zero tables.** The table inventory ships with a header row and an explicit statement, so a
reader can tell "no tables" from "not checked".

**Zero raster images.** Nothing was extracted as a photograph, because there is nothing to
extract.

# 6. Rumusan and quiz

```
RUMUSAN     = NOT_FOUND        QUIZ_ITEMS  = NOT_FOUND      ANSWER_KEY = NOT_FOUND
FEEDBACK    = SOURCE_AVAILABLE_ELSEWHERE
COMPOSITION = AUTHORITY_UNRESOLVED   THRESHOLD = AUTHORITY_UNRESOLVED
```

Searched the **entire module DOCX**, all 6,167 body-level paragraphs: `Rumusan` **0 hits**,
`Kuiz` **0 hits**, `Soalan` **0 hits**.

This retro-explains B02: its Rumusan and its five quiz questions were **authored**, not
extracted. No storyboard in this project has ever had a source-supplied Rumusan, and the
source ingest does not change that. `4 MCQ + 1 MR` and the `60%` threshold come from A3 — the
B02 slice of the S&G — and remain `AUTHORITY_UNRESOLVED` for T04.

Nothing was drafted.

# 7. External claims — 9, none blocking this unit

Two require external verification before canonical freeze: the **Akta Racun Makhluk Perosak
1974** citation and the licensed-operator obligation. The rest are source statements safe to
render in a review deck: PPE, SDS retention, spray-drift conditions, watering timing, IPM,
Pegawai Penguasa.

Recorded as a deliberate **negative** finding: **MS2680 appears nowhere in T04.** The open
B02 standards item does not touch this unit — a global open item must not block unrelated
content.

Two cautions carried into the storyboard model: do not turn *cuaca tenang* into a wind speed,
and do not state a watering frequency the source deliberately defers to plant type, weather
and growth stage.

# 8. Screen candidates — 6

`PROCESS_FLOW` (opening diagram) · `CLICK_TO_REVEAL` (Landskap Lembut, three operations) ·
`SEQUENTIAL_STEPS` (Racun compliance load) · `COMPARISON` (Lembut vs Kejur) ·
`CLICK_TO_REVEAL` (Landskap Kejur, four function groups) · `PENDING_HUMAN` (Rumusan and quiz).

Two need new treatment: `PROCESS_FLOW` and `COMPARISON`. B02 has neither.
`B02_FAMILIES_PROPAGATED = 0`.

## 8.1 The portability finding

**Five of six candidates have no visual dependency, because the unit has no photographs.**
T04 has one visual against B02's fourteen extracted assets.

B02's component-main treatment is a *source-bound overview of photographs*, ruled by Bariah
on a unit that had photographs to bind. T04 has none. Applying it here would require
inventing subjects, which is prohibited — so RP-101 arrives with nothing to bind to. That is
the first genuine portability failure this scale-out has produced, and it is exactly what a
first non-B02 proof was chosen to surface.

# 9. Readiness semantics

`SOURCE_INCOMPLETE` is retired for these units. It conflated three states with three owners:

| State | Who clears it |
|---|---|
| `SOURCE_PRESENT_CONTENT_NOT_EXTRACTED` | us, by working |
| `CONTENT_ASSESSMENT_PENDING` | us to propose, a human to approve |
| `SOURCE_GAP_CONFIRMED` | **nobody, by reading** — it must be authored |

T04-B01 is **`CONTENT_ASSESSMENT_PENDING`**. The other twelve are
**`SOURCE_PRESENT_CONTENT_NOT_EXTRACTED`**. The typed field was added to the PL06 inventory
alongside the existing `readiness_status`, which keeps its Stage 4.2F-A vocabulary so the
existing gates stay meaningful rather than being renamed away.

# 10. QA and mutations

| | |
|---|---:|
| T04 gates | **109 / 109**, 0 markers |
| T04 fixtures | **34 / 34 detected**, 0 missed, 0 skipped, 0 false failures |
| PL06 inventory gates | **140 / 140** (136 + 4 typed-readiness) |
| PL06 fixtures | **54 / 54 detected** |

Two of my own gates were over-broad and the fixtures caught them before they shipped — see
`STAGE_4_2F_B0_QA_REPORT.md` §2.1.

# 11. Cleanup and constraints

- Temporary DOCX staging deleted; no `tmp/` in the repository.
- No `.docx`, `.pdf` or `.zip` in the Git index — gated.
- **No PPTX generated.** No generator or validator under `reviews/source-completion/`
  modified — 0 changed files.
- No MMD, React or SCORM work.
- `5535ecd` not amended.
