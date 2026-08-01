# BARIAH_REGRESSION_CORRECTION_REPORT — v0.4.1

```
REVIEW_READY · BARIAH_LATEST_FEEDBACK_IMPLEMENTED · PENDING_TARGETED_CONFIRMATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED

ORIGINAL_STAGE_4_CHECKS = 105 · PASS = 105 · FAIL = 0
EXPANDED_CHECKS = 188 · PASS = 188 · FAIL = 0
REVIEW_PAGES = 100 · LEARNER_SCREENS = 29 · RUNTIME_STATES = 100 · INTERACTION_ITEMS = 54
SOURCE_ROWS = 26 · SOURCE_ASSETS = 14 · SOURCE_ROWS_CREATED = 0
```

Deck: `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_1.pptx` — 453,859 B,
`sha256 247eadb10bde4e7f227c6df947b1821c55faad140b212465ae774bd2c932f59a`.

The v0.4 deck is **retained** and marked `SUPERSEDED_BY_v0_4_1`. It was never deleted.

> **Bariah must not patch the PowerPoint by hand.** Any manual edit would be destroyed by the
> next regeneration and would leave the pipeline still producing the defect. Every correction
> below is in controlled data, the model adapter, the Notes writer, the generator or the
> validators, and the complete 100-page deck was regenerated from those inputs in one run.

---

# 1. Direct Bariah feedback in this round

| ID | Feedback | Status |
|---|---|---|
| `B02-BARIAH-20260801-VISUAL-01` | Popup visual directions reverted to a generic fallback | `CONFIRMED_REGRESSION` |
| `B02-BARIAH-20260801-NOTES-ITALIC-01` | English terms in Speaker Notes are not italicised | `CONFIRMED_REGRESSION` |
| `B02-BARIAH-20260801-VISUAL-02` | *"Semua contoh ada visual. Semua pop up ada visual, KECUALI pop up Spesifikasi"* | `CONFIRMED_BARIAH` |
| `B02-BARIAH-20260801-QUIZ-KEY-01` | Every quiz review page must visibly show the correct answer for CIDB review | `CONFIRMED_BARIAH` |
| `B02-BARIAH-20260801-TAMAT-01` | Tamat must follow the reviewed example; drop the close-window instruction | `CONFIRMED_BARIAH` |
| `B02-BARIAH-20260801-PERABOT-01` | Perabot overview must be visual; `FAMILY_P1`/`FAMILY_P2` must never appear on canvas | `CONFIRMED_REGRESSION` |
| `B02-BARIAH-20260801-VO-PARITY-01` | Every learner-facing interaction instruction must also be spoken | `CONFIRMED_BARIAH` |

---

# 2. Root causes

## 2.1 Visual-direction regression

The data path is: Bariah exemplar → implementation map → controlled content → model adapter →
generator → slide → render. The break was in the **generator**, at one line:

```python
vis = r.get("visual") or (f"[Visual: Arahan visual untuk {r['label']} — "
                          f"spesifikasi teks sahaja, modul ms {r['ms']}. Tidak dibenamkan.]")
```

Fourteen of the 26 source rows carry no dedicated figure, so fourteen popups fell through to a
sentence assembled from the row label and page number. Bariah's corrected exemplar (annotated
deck, slide 14) shows the intended treatment plainly:

```
ARAHAN VISUAL — TIDAK DIBENAMKAN
[Visual:  Promenade Tasik Titiwangsa, KL]
```

— the direction names the **source-attested example**, which was sitting unused in the row's own
`contoh` field. The fallback was not a missing decision; it was a decision the generator declined
to look up.

Fixed by extracting the choice into `b02_visual_directions_v0_4.py`, the single place any visual
direction is now decided, with the authority order recorded per row. `is_generic()` in that module
is what the validator uses, so the fallback shape can never silently return.

## 2.2 Missing Notes italics

The canvas already used rich-text runs. The Notes writer did not: it emitted one plain
`<a:r>` per line. Italics were never lost — they were never written. Fixed by giving the Notes
emitter the same glossary the canvas uses and building one `<a:r>` per fragment, `i="1"` on the
glossary terms.

There is now exactly **one** glossary, `b02_glossary_v0_4.py`, imported by both writers. A gate
asserts the generator's canvas splitter and the glossary return the same result, so the two cannot
drift apart again.

## 2.3 Family labels on the learner canvas

The Perabot gateway printed each component's `execution_family` beside its name — model metadata
rendered as learner content. Fixed by redesigning the gateway as five visual component cards and
adding a **canvas metadata denylist** checked on every one of the 100 pages.

---

# 3. The Promenade example

**BEFORE**

```
[Visual: Arahan visual untuk Promenade — spesifikasi teks sahaja, modul ms 238.
 Tidak dibenamkan.]
```

**AFTER**

```
ARAHAN VISUAL — TIDAK DIBENAMKAN
[Visual: Promenade Tasik Titiwangsa, KL]
```

drawn in a dedicated right-hand visual panel with its own heading and a blank production area
beneath it, close icon top-right and clear of both.

**No image was embedded.** This review build carries a textual MMD visual direction, as every
visual in it does.

---

# 4. Visual-direction audit — all 26 source rows

| source row | example | authority | direction |
|---|---|---|---|
| `UR-PERSISIR-AIR-ROW-01` | Promenade | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Promenade Tasik Titiwangsa, KL] |
| `UR-PERSISIR-AIR-ROW-02` | Jeti | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Jeti Lumut, Perak] |
| `UR-PERSISIR-AIR-ROW-03` | Dek Kayu | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Wetland Park Putrajaya] |
| `UR-PERSISIR-AIR-ROW-04` | Boardwalk | `SOURCE_ASSET_FIGURE` | [Visual: Rajah 23 — Contoh Boardwalk dalam Taman Paya Bakau, modul ms 239. A |
| `UR-PERSISIR-AIR-ROW-05` | Footbridge | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Footbridge Taman Botani Perdana] |
| `TRUKTUR-TEDUHAN-ROW-01` | Gazebo | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Taman Tasik Shah Alam] |
| `TRUKTUR-TEDUHAN-ROW-02` | Wakaf | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Wakaf di Taman Desa, KL] |
| `TRUKTUR-TEDUHAN-ROW-03` | Pergola | `SOURCE_ASSET_FIGURE` | [Visual: Rajah 24 — Contoh Pergola, modul ms 240. Aset K5PL06T03-B02-IMG-p24 |
| `TRUKTUR-TEDUHAN-ROW-04` | Canopy | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Canopy rekreasi di Taman Jaya] |
| `TRUKTUR-TEDUHAN-ROW-05` | Struktur Teduhan Moden | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Banyak kawasan awam di Putrajaya] |
| `-KEMUDAHAN-AWAM-ROW-01` | Tandas Awam | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Tandas Awam] |
| `-KEMUDAHAN-AWAM-ROW-02` | Surau | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Surau] |
| `-KEMUDAHAN-AWAM-ROW-03` | Bangunan Interpretatif | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Bangunan Interpretatif] |
| `2-WATER-FEATURE-ROW-01` | Air Pancut (Fountain) | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Air Pancut (Fountain)] |
| `2-WATER-FEATURE-ROW-02` | Kolam (Pond) | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Kolam (Pond)] |
| `2-WATER-FEATURE-ROW-03` | Kolam Renang / Kolam Hiasan Besar (Pool) | `BARIAH_EXEMPLAR_CONTOH` | [Visual: Kolam Renang/Kolam Hiasan Besar(Pool)] |
| `02-KERUSI-TAMAN-ROW-01` | Kerusi Kayu Keras | `SOURCE_ASSET_FIGURE` | [Visual: Foto jadual spesifikasi Kerusi Kayu Keras, modul ms 242. Aset K5PL0 |
| `02-KERUSI-TAMAN-ROW-02` | Kerusi Konkrit | `SOURCE_ASSET_FIGURE` | [Visual: Foto jadual spesifikasi Kerusi Konkrit, modul ms 243. Aset K5PL06T0 |
| `02-KERUSI-TAMAN-ROW-03` | Kerusi Komposit | `SOURCE_ASSET_FIGURE` | [Visual: Foto jadual spesifikasi Kerusi Komposit, modul ms 243. Aset K5PL06T |
| `B02-PAPAN-TANDA-ROW-01` | Papan Tanda Arah / Papan Tanda Interpretatif | `SOURCE_ASSET_FIGURE` | [Visual: Rajah 25 — Lukisan Spesifikasi Papan Tanda Informasi, dan Rajah 26  |
| `B02-TONG-SAMPAH-ROW-01` | Tong Sampah Logam | `SOURCE_ASSET_FIGURE` | [Visual: Foto jadual spesifikasi Tong Sampah Logam, modul ms 246. Aset K5PL0 |
| `B02-TONG-SAMPAH-ROW-02` | Tong Sampah Konkrit/Batu | `SOURCE_ASSET_FIGURE` | [Visual: Foto jadual spesifikasi Tong Sampah Konkrit/Batu, modul ms 247. Ase |
| `B02-TONG-SAMPAH-ROW-03` | Tong Sampah Plastik Kitar Semula (HDPE) | `SOURCE_ASSET_FIGURE` | [Visual: Dua foto jadual spesifikasi Tong Sampah Plastik HDPE, modul ms 247. |
| `INKING-FOUNTAIN-ROW-01` | Pancutan Air Minum Keluli Tahan Karat | `SOURCE_ASSET_FIGURE` | [Visual: Foto jadual spesifikasi Pancutan Air Minum Keluli Tahan Karat, modu |
| `INKING-FOUNTAIN-ROW-02` | Pancutan Air Minum Konkrit/Batu | `SOURCE_ASSET_FIGURE` | [Visual: Foto jadual spesifikasi Pancutan Air Minum Konkrit/Batu, modul ms 2 |
| `T03-B02-BBQ-PIT-ROW-01` | BBQ Pit Struktur Kekal | `SOURCE_ASSET_FIGURE` | [Visual: Foto jadual spesifikasi BBQ Pit Struktur Kekal, modul ms 249. Aset  |

`GENERIC_VISUAL_FALLBACKS_IN_LEARNER_PAGES = 0` · `VISUAL_DIRECTIONS_PENDING = 0` ·
14 corrected from fallback to `BARIAH_EXEMPLAR_CONTOH`, 12 already asset-bound.

---

# 5. Visual requirement by semantic subtype

Bariah's clarification made the earlier "every popup has a visual" gate **wrong**, and it was
replaced rather than kept: a specification popup is text-led by design and must not be given a
panel to satisfy a generic check.

| subtype | pages |
|---|---:|
| `SPECIFICATION_POPUP` | 30 |
| `COMPLETION_STATE` | 18 |
| `EXAMPLE_POPUP` | 16 |
| `EXAMPLE_SCREEN` | 12 |
| `COMPONENT_MAIN_SCREEN` | 9 |
| `QUIZ_QUESTION` | 5 |
| `FRAME_SCREEN` | 4 |
| `TOPIC_ENTRY_SCREEN` | 1 |
| `GROUP_MASTER` | 1 |
| `GROUP_VISUAL_GATEWAY` | 1 |
| `QUIZ_INTRO` | 1 |
| `QUIZ_RESULT` | 1 |
| `QUIZ_REVIEW` | 1 |

```
REQUIRED     29     example screens, example popups, S01
CONDITIONAL  10     component-main screens, the visual gateway — all resolved
NOT_REQUIRED 61    specification popups, completion states, quiz, frames

REQUIRED_VISUAL_SCREENS_WITHOUT_VISUAL             = 0
REQUIRED_VISUAL_POPUPS_WITHOUT_VISUAL              = 0
NOT_REQUIRED_VISUAL_POPUPS_FORCED_TO_HAVE_VISUAL   = 0
SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL = 0
CONDITIONAL_VISUAL_REQUIREMENTS_UNRESOLVED         = 0
EXAMPLE_POPUPS_TOTAL = 16 · WITH_SPECIFIC_VISUAL = 16 · WITHOUT = 0
EXAMPLE_SCREENS_TOTAL = 12 · WITH_SPECIFIC_VISUAL = 12 · WITHOUT = 0
SPECIFICATION_POPUPS_TOTAL = 30 · REQUIRING_VISUAL = 0
```

The requirement is stored per record as `semantic_screen_subtype`, `popup_subtype`,
`visual_requirement`, `visual_direction`, `visual_authority`, `visual_status`, and the generator
renders from `visual_requirement` — never from the execution family.

---

# 6. Speaker Notes italics

```
NOTES_GLOSSARY_OCCURRENCES_FOUND      = 40
NOTES_GLOSSARY_OCCURRENCES_ITALICISED = 40
NOTES_GLOSSARY_ITALIC_MISSES          = 0
NOTES_FALSE_ITALICS_ON_TECHNICAL_IDS  = 0
NOTES_MARKDOWN_ITALIC_MARKERS         = 0
NOTES_RICH_TEXT_PACKAGE_ROUNDTRIP_FAILURES = 0
CANVAS_GLOSSARY_ITALIC_MISSES         = 0
```

Validated by **parsing the generated Notes XML back out of the package**, not by inspecting the
content that produced it. The validator maps each phrase's character range onto the runs that
carry it, so a term split across runs is still judged correctly.

Glossary: `Wood-Plastic Composite`, `Multiple Response`, `Drinking Fountain`, `Water Feature`,
`Boardwalk`, `Footbridge`, `Promenade`, `Mind Map`, `BBQ Pit`. Never italicised: identifiers,
filenames, URLs, acronyms (`ACP`, `HPL`, `WPC`, `HDPE`, `PL06`, `MS2680`), production metadata keys.

---

# 7. Quiz answer key

All five question review pages carry a bordered block headed **SEMAKAN CIDB — MAKLUMAT PENYEMAK,
BUKAN PAPARAN PELAJAR**, generated from the same structured answer data the quiz logic uses.

```
QUIZ_QUESTIONS = 5                                    QUIZ_REVIEW_PAGES_WITH_VISIBLE_ANSWER_KEY = 5
QUIZ_REVIEW_PAGES_WITHOUT_ANSWER_KEY = 0              MCQ_ANSWER_KEYS_WITH_LETTER_AND_TEXT = 4
MULTIPLE_RESPONSE_ANSWER_KEY_USES_FULL_OPTION_TEXT = true
MULTIPLE_RESPONSE_LEARNER_OPTIONS_WITH_LETTER_LABELS = 0
ANSWER_KEY_SOURCE_MISMATCH = 0                        ANSWER_KEY_READ_IN_VO = 0
ANSWER_KEY_VISIBLE_DURING_LEARNER_PRE_SUBMISSION_STATE = 0
```

The key is review-page annotation only: it is labelled as reviewer information, is not in the
spoken transcript, and is not runtime learner content.

---

# 8. Tamat

Bariah's reviewed example supersedes the previous provisional close-the-window instruction.

```
TAMAT_COPY_STATUS                 = CONFIRMED_BARIAH
TAMAT_LOGICAL_DESTINATION         = NEXT_BAHAGIAN
TAMAT_PHYSICAL_NAVIGATION_STATUS  = PENDING_FIRDAUS_OR_LMS_CONFIRMATION
TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT = false
TAMAT_UNVERIFIED_PHYSICAL_NAVIGATION_CLAIM = 0
```

**Five of the original 105 checks encoded the superseded ruling** and were replaced 1:1 — the count
is unchanged and none was dropped. No claim is now made about the shell control, no custom canvas
navigation button was created, and the red triangle in the exemplar is treated as a visual cue
rather than an interactive button until evidence says otherwise.

---

# 9. Canvas↔VO instruction parity

One field, `learner_interaction_instruction`, generates both the canvas string and the spoken
string. Object-specific wording is preserved per screen kind; there is no single generic phrase.

```
LEARNER_SCREENS_WITH_ACTION_INSTRUCTION        = 25
ACTION_INSTRUCTIONS_PRESENT_ON_CANVAS          = 25
ACTION_INSTRUCTIONS_PRESENT_IN_SPOKEN_TRANSCRIPT = 25
ACTION_INSTRUCTION_CANVAS_VO_MISMATCHES        = 0
ACTION_INSTRUCTIONS_MISSING_FROM_NOTES         = 0
SILENT_STATES_RECEIVING_NEW_VO                 = 0
REVIEW_ONLY_ANSWER_KEYS_INCLUDED_IN_VO         = 0
TECHNICAL_CONTROLS_READ_AS_VO                  = 0
```

Two quiz screens were found carrying hand-typed instruction copies — exactly the duplication the
rule forbids — and now render from the controlled field.

---

# 10. Metadata denylist

```
FAMILY_LABELS_ON_LEARNER_CANVAS      = 0
TECHNICAL_METADATA_ON_LEARNER_CANVAS = 0
PERABOT_OVERVIEW_VISUAL_CARDS = 5 · COMPONENT_NAMES_PRESENT = 5 · WITH_VISUAL_DIRECTION = 5
PERABOT_OVERVIEW_INTERNAL_MAPPING_UNCHANGED   = true
PERABOT_OVERVIEW_NAVIGATION_MODEL_UNCHANGED   = true
BASE_STATE_FALSE_COMPLETION_TICKS             = 0
```

Checked against the generated slide XML on every page, for `FAMILY_P1`, `FAMILY_P2`,
`execution_family`, `source_row_uid`, `interaction_item_id`, `runtime_state_id`,
`completion_scope`, `return_target` and six more. The family mapping is unchanged and lives in
model data and off-canvas production metadata only.

---

# 11. Defects found during this correction

| # | Defect | Fix |
|---|---|---|
| 1 | Generic visual fallback on 14 popups | visual-direction resolver, authority-ordered |
| 2 | Notes had no rich-text runs at all | run-level OOXML emitter sharing the canvas glossary |
| 3 | `FAMILY_P1`/`FAMILY_P2` printed on the Perabot canvas | visual gateway + canvas metadata denylist |
| 4 | Visual panel overflowed on Papan Tanda's long figure reference | popup height now sized from the visual need; then made moot by the specification-popup exception |
| 5 | Full-width specification-popup titles ran under the close icon | title width always reserves the icon's space |
| 6 | Perabot component cards ran past the bottom of the stage | card geometry reduced — **and a real off-canvas gate added**, see below |
| 7 | Q5's answer key pushed the feedback row off-stage | question layout now fits options + key + feedback inside the stage |
| 8 | Two quiz screens had hand-typed instruction copies | both render from the controlled instruction field |

**Defect 6 is the one worth naming.** The Stage 4 suite separated on-canvas from off-canvas shapes
by the *left edge only*, so a card running off the *bottom* was invisible to it. Visual inspection
caught it; the new `CANVAS_SHAPES_OUTSIDE_STAGE` gate tests all four edges and caught defect 7
immediately afterwards.

---

# 12. Environment

LibreOffice retested at Stage 4.1 and still cannot open a `.pptx`:

```
$ soffice --headless --convert-to pdf K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_1.pptx
Error: source file could not be loaded
```

No Impress import filter is installed. Rendering used the package parser with Liberation Sans.
**Microsoft PowerPoint equivalence is not proven.** All 100 pages were rendered and inspected.

---

# 13. PENDING_HUMAN

Visual judgment: Family P1 density · Family P2 category treatment · close-icon clarity ·
Alya / Encik Rahman visual treatment · S01 VO naturalness · S03 reflection wording · Rumusan
visual treatment · quiz presentation · Tamat visual treatment · Microsoft PowerPoint font wrapping.

Open decisions: **U-01** MS2680 · **U-02b** Pengurus Projek name · **U-03** physical LMS navigation
(`PENDING_FIRDAUS_OR_LMS_CONFIRMATION`) · **U-05** quiz rationale placement · `B02-CAIR-INT-001`.
`SOURCE_INTEGRITY_FULLY_VERIFIED` is not claimed.
