# STAGE_4_2F_B1_RUN_MANIFEST

```
STAGE      = 4.2F-B1 — T04 STORYBOARD MODEL AND REVIEW PPTX
SUITE_ID   = T04_STORYBOARD_QA_v1
SCREENS    = 22          SLIDES = 26 (1 title + 25 content pages)
PPTX       = K5PL06T04B01_STORYBOARD_FOR_BARIAH_REVIEW_v1_0.pptx  ·  76,248 bytes
PREVIEWS   = 26 pages, 1280×720, 0 blank, 0 truncated
NATIVE_RENDER = NOT_CHECKED_POWERPOINT_RENDERER_UNAVAILABLE
MMD = 0 · REACT = 0 · SCORM = 0 · LMS = 0 · OTHER_PL = 0
VERDICT    = T04_STORYBOARD_BUILT_READY_FOR_BARIAH_VISUAL_REVIEW
```

Entered on the Stage 4.2F-B0.9.1 release decision, which permitted storyboard layout:
`T04_ASSESSMENT_DIVERGENCE_CLOSED` · `STORYBOARD_LAYOUT_READY` ·
`SUPPLEMENTARY_CNF_MAPPING_PARTIALLY_OPEN`.

# 1. What was built

| Deliverable | Where |
|---|---|
| controlled storyboard model | `T04_STORYBOARD_MODEL_v1.json` / `.md` |
| review PPTX | `reviews/storyboard-bariah/t04_storyboard/K5PL06T04B01_STORYBOARD_FOR_BARIAH_REVIEW_v1_0.pptx` |
| screen → source traceability | `T04_STORYBOARD_SOURCE_TRACEABILITY_v1.json` / `.md` |
| screen → authority traceability | `T04_STORYBOARD_AUTHORITY_TRACEABILITY_v1.json` / `.md` |
| interaction and state model | `T04_STORYBOARD_INTERACTION_MODEL_v1.json` / `.md` |
| visual obligation and asset mapping | `T04_STORYBOARD_VISUAL_MAPPING_v1.json` / `.md` |
| assessment-status register | `T04_STORYBOARD_ASSESSMENT_STATUS_v1.json` / `.md` |
| evidence-status register | `T04_STORYBOARD_EVIDENCE_STATUS_v1.json` / `.md` |
| rendered pages | `docs/pl06/t04/storyboard_preview/` — 26 PNG |
| structural + rendered QA | `t04_storyboard_qa_v1.py` — 114 gates |
| mutation suite | `t04_storyboard_mutations_v1.py` — 72 fixtures |

The deck is generated and was never hand-edited. The QA suite re-opens the saved package and
re-extracts its text, so a sentence living only in the builder cannot pass.

# 2. Twenty-two screens, twenty-six slides

The screen count and the slide count are different numbers and are never conflated. Four
screens carry more content than one page holds, so they spill onto a labelled continuation
slide — `(samb. 1/2)`, `(samb. 2/2)`.

| Screen | Title | Treatment | Pages |
|---|---|---|---:|
| T04-S01 | Tajuk dan Mula | TITLE | 1 |
| T04-S02 | Pengenalan — perbualan di tapak | DIALOGUE_SCENARIO | 1 |
| T04-S03 | Aliran proses penjagaan dan penyelenggaraan | PROCESS_FLOW_STEPPED | 1 |
| T04-S04 | Landskap Lembut — pengenalan | CONTENT_STATIC | 1 |
| T04-S05 | Siram — penerangan utama | CONTENT_STATIC | 1 |
| T04-S06 | Siram — kaedah pelaksanaan | CLICK_TO_REVEAL | 1 |
| T04-S07 | Siram — aspek pengurusan untuk kontraktor | CLICK_TO_REVEAL | **2** |
| T04-S08 | Baja — penerangan utama | CONTENT_STATIC | 1 |
| T04-S09 | Baja — kaedah pelaksanaan | CLICK_TO_REVEAL | 1 |
| T04-S10 | Baja — aspek pengurusan untuk kontraktor | CLICK_TO_REVEAL | **2** |
| T04-S11 | Racun — penerangan utama | CONTENT_STATIC | 1 |
| T04-S12 | Racun — pendekatan IPM | CONTENT_STATIC | 1 |
| T04-S13 | Racun — jenis racun | CONTENT_STATIC | 1 |
| T04-S14 | Racun — aspek pengurusan untuk kontraktor | CLICK_TO_REVEAL | 1 |
| T04-S15 | Racun — perundangan dan pelesenan | CONTENT_STATIC | 1 |
| T04-S16 | Racun — keselamatan dan kesihatan (HSE) | CLICK_TO_REVEAL | 1 |
| T04-S17 | Racun — pengurusan risiko | CONTENT_STATIC | 1 |
| T04-S18 | Landskap Kejur — pengenalan | CONTENT_STATIC | 1 |
| T04-S19 | Landskap Kejur — empat kumpulan fungsi | CLICK_TO_REVEAL | **2** |
| T04-S20 | Rumusan | RUMUSAN | 1 |
| T04-S21 | Kuiz | QUIZ | **2** |
| T04-S22 | Tamat Topik | CLOSING | 1 |

`INTERNAL_UNIT_ID = K5-PL06-T04-B01` is carried on every screen record and appears once on the
title slide as *Rujukan dalaman*. **No learner-facing screen displays "Bahagian".**

# 3. Every learner-facing string carries a provenance

| Label | Meaning | Colour in the deck |
|---|---|---|
| `SOURCE_CONTROLLED` | verbatim `controlled_display_text` from the extract | blue, tag `S` |
| `AUTHORITY_SUPPLIED` | wording Bariah wrote | green, tag `A` |
| `AUTHORITY_SELECTED` | wording Bariah chose from enumerated options | green, tag `A*` |
| `CAIR_DRAFTED_ASSESSMENT_OPTION` | quiz option CAIR wrote, Bariah reviewed | purple, tag `d` |
| `CAIR_STRUCTURAL` | buttons, hints, screen furniture | grey, tag `u` |

**There is no category for CAIR-written teaching content**, and a gate asserts the forbidden
label `CAIR_INSTRUCTIONAL_CONTENT` is never used. A second gate keeps structural furniture
under 60 characters, because a long "UI string" is how teaching prose would sneak in.

99 source-derived strings, all verbatim. One screen carries source rows but shows
authority-written replacement text — T04-S02, whose dialogue Bariah rewrote — and it is named
rather than filtered, so a second cannot join it silently.

# 4. Three defects this stage found

## 4.1 The B0.8 → B0.9 numbering trap — REAL, and silent

The obligation closure and the asset-group plan were written in Stage 4.2F-B0.8 against the
**21-screen** sequence. Stage 4.2F-B0.9 inserted a screen and shifted everything from the old
T04-S14 onward by one. Reading either register against the new IDs without translating is
**off by one for ten screens**, and nothing complains — AG-07 (Landskap Kejur) landed on the
Racun risk-management screen.

Fixed with an explicit `to_current()` translation applied at every read: 8 obligations and 2
asset groups translated. Two gates now assert the *result* rather than the raw mapping —
AG-07 must land on T04-S18/S19 and AG-06 on the four Racun compliance screens. Fixtures `R-01`
and `R-02` switch the translation off and both fire.

## 4.2 `T04-COR-05` — a do-not-reuse ID pointing at the wrong obligation

The register named `T04-VO-039` as the pesticide HSE do-not-reuse item. `T04-VO-039` is
*Perundangan dan Pelesenan*. The PPE obligation is **`T04-VO-040`**, and the Stage 4.2F-B0.8
closure already carried `reuse_policy = DO_NOT_REUSE` on it.

Left uncorrected, the storyboard would have shown the do-not-reuse restriction on the legal
screen and **not** on the PPE screen — the exact confusion Bariah's ruling exists to prevent.

**Second occurrence of this defect class.** Stage 4.2F-B0.6 had five hand-typed obligation IDs
in the legal sheet, fixed then by deriving from an index; the lesson did not carry across to
this register. It does now: `DO_NOT_REUSE_IDS_AGREE_WITH_THE_CLOSURE` derives the ID set from
the closure's own `reuse_policy` and compares. No gate could have caught it before, because
every gate read the same typed list.

## 4.3 Content overflow — found by looking at the rendered pages

The first render truncated T04-S21 and T04-S19 with an ellipsis. In the deck the text would
have run off the slide instead. Fixed with pagination, and the page budget is calibrated
against the renderer's measured capacity rather than guessed. The preview now prints
**TRUNCATED — PAGINATION FAILED** in red if it ever happens again, instead of quietly eliding.

A related smaller one: the first pass left four stale PNGs behind when pagination changed the
filenames, so the folder held pages from two different runs. The renderer now clears first.

# 5. Two blind spots the fixtures found — the same defect class

Both were gates **comparing a value against its own source**, which proves only that a copy
succeeded.

- `S-11` raised the page budget to 200 and the `fits` check declared everything fitted —
  because it compared the pages against the very knob that had been moved. Now checked against
  `RENDERER_LINE_CAPACITY`, a measured property of the renderer, with a second gate asserting
  the budget stays within it.
- `E-02` overstated the release decision to full approval and the carry-forward gate passed —
  because it compared the register to the object it was built from. Now asserted against the
  three literal tokens, plus a gate that the full-approval verdict is never claimed.

This is a sibling of the C-05 filter defect and the three stale-constant defects before it:
**a check is only worth what its reference point is worth.**

# 6. Assessment — what is settled and what is not

```
4 MCQ + 1 Multiple Response · pass mark 60 peratus · scope ALL_PLS_IN_KURSUS
Q5 options: checkboxes, no A/B/C labels
```

| Item | Stem provenance | Authority-authored stem |
|---|---|---|
| Q1–Q4 | `AUTHORITY_SUPPLIED_REPLACEMENT_TEXT` | yes |
| Q5 | `FIRDAUS_DIRECTED_PRESENTED_AS_FIXED_NOT_CONTESTED_BY_AUTHORITY` | **no** |

The Q5 incorrect options are **Set B**, verbatim from the forced choice Bariah answered:
*Semburan dijadualkan pada waktu petang tanpa mengambil kira keadaan cuaca* and *Semua racun
dibeli daripada satu pembekal tunggal*. Gates assert the rejected Set A is **not** in the deck
and neither is the superseded Stage 4.2F-B0.9 CAIR draft.

**Selecting is not authoring.** `q5_distractors_are_bariah_direct_authored = False`. **No
answer key is final** — `PROPOSED_NOT_FINAL`, `answer_key_is_bariah_direct_approved = False`.
**No runtime assessment packet was generated**: no scoring logic, no key export, no SCORM
interaction descriptors.

# 7. Visual scope — nothing was drawn

```
46 visual obligations · 8 asset groups · 41 proposed unique assets · 0 artwork produced
```

Every visual slot is a labelled placeholder naming its asset group and obligations, and every
one carries **ASET BELUM DIHASILKAN** on the slide. T04-S14 reuses AG-06 and adds **0** unique
assets, so the total stays 41. The three do-not-reuse restrictions appear on T04-S10 (the two
Baja items) and T04-S16 (the pesticide PPE item), marked **TIDAK BOLEH DIKONGSI**.

# 8. Rendering — what was and was not checked

```
NATIVE_RENDER = NOT_CHECKED_POWERPOINT_RENDERER_UNAVAILABLE
```

LibreOffice has no Impress filter in this environment. **The deck was not opened by any
presentation application and no native render was produced.** What exists is 26 deterministic
preview pages drawn from the same model at 1280×720 with real font metrics — a layout
approximation. Every page was visually inspected; 0 blank, 0 truncated, all the same size.

It does **not** prove PowerPoint pagination, autofit behaviour, font fallback or shape
overflow. Fixtures `N-01`, `N-02` and `N-03` fire if a native render, PowerPoint equivalence,
or the removal of that limitation note is ever claimed.

Structural checks that need no renderer all passed: valid package, 26 slides matching the
model, every slide has text, every screen ID and title present, no embedded media, no external
relationship, 16:9, no repository path and no SHA-256 leaked onto a slide.

# 9. QA and mutations

| Suite | Gates | Fixtures |
|---|---|---|
| `T04_STORYBOARD_QA_v1` | **114 / 114**, 0 vacuous | **72 / 72 detected** |

| Gate type | Count |
|---|---:|
| `SEQUENCE` | 19 |
| `ASSESSMENT` | 14 |
| `PPTX_STRUCTURE` | 11 |
| `VISUAL_SCOPE` | 11 |
| `PRODUCTION_GUARD` | 10 |
| `SOURCE_TRACE` | 9 |
| `TEXT_PROVENANCE` | 8 |
| `ACCOUNTING` | 7 |
| `EVIDENCE` | 7 |
| `RENDER` | 7 |
| `INTERACTION` | 6 |
| `AUTHORITY_TRACE` | 5 |

Eight fixtures **rebuild the deck from a mutated model** and leave the corrupted PPTX on disk,
because gates that re-open the package cannot be exercised any other way. The real deck is
rebuilt clean afterwards and `deck_rebuilt_clean` compares its extracted text back to the
baseline — byte comparison would be useless, since python-pptx writes non-deterministic
package metadata.

Upstream suites re-run after this stage's corrections: `T04_AUTHORITY_DECISION_INGESTION_QA_v1`
**251 / 251** with 129 / 129 fixtures; `T04_SUPPLEMENTARY_EVIDENCE_QA_v1` **133 / 133** with
83 / 83 fixtures. **Never add these totals together** — they govern different things.

# 10. What was not done

- No MMD asset produced. No React. No SCORM. No LMS upload. No other PL touched.
- The frozen production storyboard generator was not opened or modified.
- Neither authority artifact was modified; the v3 DOCX is still 36,105 bytes, `2eea2101…`.
- No prior commit was amended. No historical run record was rewritten.
- No Bariah decision that was closed has been reopened.
- The PPTX was never hand-edited.

# 11. Open after this stage

| ID | Subject | Owner | Blocks |
|---|---|---|---|
| E-02 | Quiz answer keys, all five | Bariah | a scored quiz, not the storyboard |
| E-04 | The pembajaan → racun correction | Bariah | nothing — applied and recorded |
| E-05 | Original module DOCX round trip | Firdaus | nothing — non-blocking risk token |
| E-06 | Individual asset subjects and styles | Bariah | MMD production |
| E-08 | Supplementary screenshot binary custody | Firdaus | canonical evidence closure |

# 12. Verdict

```
T04_STORYBOARD_BUILT_READY_FOR_BARIAH_VISUAL_REVIEW
```

Read it precisely. **Built** means the deck exists, is generated from the frozen model, and
passes 114 structural and rendered gates. **Ready for Bariah's visual review** means it is
fit to be looked at by the authority — not that she has approved it, and not that it has been
seen in PowerPoint. The five items above stay open, and none of them blocks her reading it.
