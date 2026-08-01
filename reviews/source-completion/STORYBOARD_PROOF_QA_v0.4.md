# STORYBOARD_PROOF_QA — K5 PL06 T03 B02 v0.4 three-family proof

```
B02_V0_4_THREE_FAMILY_PROOF_READY
CHECKABLE_GATES = 87 · PASS = 87 · FAIL = 0
PROOF_PAGES = 34 · LEARNER_SCREENS = 13 · RUNTIME_STATES = 32 · INTERACTION_ITEMS = 16
SOURCE_ROWS = 26 · SOURCE_ASSETS = 14 · SOURCE_ROWS_CREATED = 0
SLIDES_MANUALLY_PATCHED = 0 · COMPONENTS_PROPAGATED = 0 · NEW_CANONICAL_PATTERN_IDS_MINTED = 0
NOT_THE_COMPLETE_STORYBOARD · NOT_FOR_MMD_BUILD · PRODUCTION_APPROVAL_NOT_CLAIMED
```

Proof deck: `K5PL06T03B02_v0_4_THREE_FAMILY_PROOF.pptx` — 164,564 B,
`sha256 f73c795b44a1dee71040c1fd8a641e65dabf726c03e417e41e1d17a6df13047a`.

This stage proves the frozen v0.4 model can be **executed** before the remaining six components
are propagated. It is deliberately not the full storyboard.

---

# 1. What the generator is, and what it refuses to be

The v0.3 toolchain is untouched — `GENERATOR_FILES_CHANGED_V0_3 = 0`. The v0.4 implementation lives
in `generator/v0_4/` and **imports** the v0.3 drawing primitives rather than reimplementing them:
geometry constants, `box`/`txt`/`bullets`/`card`/`tick`/`button`/`titlebar`, the donor package and
the package writer all come from `b02_generator_v0_3`. Nothing was rebuilt from scratch, because no
incompatibility required it.

| File | Role |
|---|---|
| `generator/v0_4/b02_model_adapter_v0_4.py` | read-only view over the frozen model; resolves the proof page list |
| `generator/v0_4/b02_proof_content_v0_4.py` | frame-screen copy only — no architecture, no component copy |
| `generator/v0_4/b02_generator_v0_4.py` | family strategy dispatch, example-detail screen, close icon, structured Notes |
| `generator/v0_4/b02_proof_qa_v0_4.py` | the 87 structural gates |

**The architecture is never reconstructed in presentation code.** `execution_family`,
`parent_screen_id`, `return_target`, control types, `completion_scope`, notes policy, character
assignment, spoken transcript, source locators and unresolved status are all read from
`STORYBOARD_SCREEN_STATE_MAP_v0.4.json`, `B02_V0_4_MODEL_CONTRACT.json` and
`DECISION_REGISTER_B02_v0.4.json`. `build_page` raises rather than guessing when a control type
falls outside the model's own vocabulary.

Component copy is read from the preserved 26-row source data. The proof content file carries frame
copy only, so there is no second copy of the source to drift.

---

# 2. Family strategy dispatch

```python
FAMILY_STRATEGY = {"FAMILY_S": render_family_s,
                   "FAMILY_P1": render_family_p1,
                   "FAMILY_P2": render_family_p2}
```

Dispatch is on the model-assigned `execution_family` of the record being rendered. **No layout
function inspects a component name.** Group masters, the Perabot gateway and the frame screens carry
no `component_id` and therefore never reach a family strategy at all — that guard is what stops the
Perabot overview being mistaken for a Family P1 screen.

| Family | Proof component | Level 1 | Level 2 | Popup parent | Close returns to | Kembali returns to |
|---|---|---|---|---|---|---|
| **S** | Struktur Persisir Air | click example → popup | — | `Contoh` screen | same `Contoh` screen | Struktur Taman group master |
| **P1** | Kerusi Taman | click example → **full slide** | click specification → popup | example detail | same example detail | component overview/list |
| **P2** | Papan Tanda | click category → popup | — | specification list | same specification list | — |

---

# 3. Proof page inventory

| # | page | family | screen | state | review page role | notes chars |
|---:|---|---|---|---|---|---:|
| 1 | `PP-01` | `FRAME` | `SCR_S01` | `ST_S01_BASE` | `TOPIC_SECTION_ENTRY_BASE` | 192 |
| 2 | `PP-02` | `FRAME` | `SCR_S02` | `ST_S02_BASE` | `FRAME_SCENARIO_BASE` | 720 |
| 3 | `PP-03` | `FRAME` | `SCR_S03` | `ST_S03_BASE` | `FRAME_NARRATOR_BASE` | 692 |
| 4 | `PP-04` | `FAMILY_S` | `SCR_GM_STRUKTUR` | `ST_GM_STRUKTUR_BASE` | `GROUP_MASTER_BASE` | 532 |
| 5 | `PP-05` | `FAMILY_S` | `SCR_STRUKTUR_PERSISIR_AIR_MAIN` | `ST_STRUKTUR_PERSISIR_AIR_MAIN_BASE` | `COMPONENT_MAIN_BASE` | 659 |
| 6 | `PP-06` | `FAMILY_S` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ST_STRUKTUR_PERSISIR_AIR_EXAMPLES_BASE` | `COMPONENT_EXAMPLES_BASE` | 185 |
| 7 | `PP-07` | `FAMILY_S` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ST_STRUKTUR_PERSISIR_AIR_POPUP_01` | `COMPONENT_EXAMPLE_POPUP` | 324 |
| 8 | `PP-08` | `FAMILY_S` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ST_STRUKTUR_PERSISIR_AIR_POPUP_02` | `COMPONENT_EXAMPLE_POPUP` | 298 |
| 9 | `PP-09` | `FAMILY_S` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ST_STRUKTUR_PERSISIR_AIR_POPUP_03` | `COMPONENT_EXAMPLE_POPUP` | 314 |
| 10 | `PP-10` | `FAMILY_S` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ST_STRUKTUR_PERSISIR_AIR_POPUP_04` | `COMPONENT_EXAMPLE_POPUP` | 331 |
| 11 | `PP-11` | `FAMILY_S` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ST_STRUKTUR_PERSISIR_AIR_POPUP_05` | `COMPONENT_EXAMPLE_POPUP` | 322 |
| 12 | `PP-12` | `FAMILY_S` | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | `ST_STRUKTUR_PERSISIR_AIR_ALL_VIEWED` | `COMPONENT_EXAMPLES_ALL_VIEWED` | 0 |
| 13 | `PP-13` | `FAMILY_S` | `SCR_GM_STRUKTUR` | `ST_GM_STRUKTUR_BASE` | `GROUP_MASTER_BASE` | 532 |
| 14 | `PP-14` | `FAMILY_P1+FAMILY_P2` | `SCR_PERABOT_OVERVIEW` | `ST_PERABOT_OVERVIEW_BASE` | `GROUP_OVERVIEW_BASE` | 574 |
| 15 | `PP-15` | `FAMILY_P1` | `SCR_KERUSI_TAMAN_MAIN` | `ST_KERUSI_TAMAN_MAIN_BASE` | `COMPONENT_EXPLANATION_LIST_BASE` | 557 |
| 16 | `PP-16` | `FAMILY_P1` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ST_KERUSI_TAMAN_EX01_BASE` | `EXAMPLE_DETAIL_BASE` | 175 |
| 17 | `PP-17` | `FAMILY_P1` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ST_KERUSI_TAMAN_R01_SPEC01` | `SPECIFICATION_POPUP` | 341 |
| 18 | `PP-18` | `FAMILY_P1` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ST_KERUSI_TAMAN_R01_SPEC02` | `SPECIFICATION_POPUP` | 250 |
| 19 | `PP-19` | `FAMILY_P1` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ST_KERUSI_TAMAN_R01_SPEC03` | `SPECIFICATION_POPUP` | 304 |
| 20 | `PP-20` | `FAMILY_P1` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ST_KERUSI_TAMAN_R01_SPEC04` | `SPECIFICATION_POPUP` | 272 |
| 21 | `PP-21` | `FAMILY_P1` | `SCR_KERUSI_TAMAN_EX01_DETAIL` | `ST_KERUSI_TAMAN_EX01_ALL_SPEC_VIEWED` | `EXAMPLE_DETAIL_ALL_VIEWED` | 0 |
| 22 | `PP-22` | `FAMILY_P1` | `SCR_KERUSI_TAMAN_MAIN` | `ST_KERUSI_TAMAN_MAIN_BASE` | `COMPONENT_EXPLANATION_LIST_BASE` | 557 |
| 23 | `PP-23` | `FAMILY_P2` | `SCR_PAPAN_TANDA_MAIN` | `ST_PAPAN_TANDA_MAIN_BASE` | `COMPONENT_SPEC_LIST_BASE` | 148 |
| 24 | `PP-24` | `FAMILY_P2` | `SCR_PAPAN_TANDA_MAIN` | `ST_PAPAN_TANDA_CAT01` | `SPECIFICATION_CATEGORY_POPUP` | 313 |
| 25 | `PP-25` | `FAMILY_P2` | `SCR_PAPAN_TANDA_MAIN` | `ST_PAPAN_TANDA_CAT02` | `SPECIFICATION_CATEGORY_POPUP` | 303 |
| 26 | `PP-26` | `FAMILY_P2` | `SCR_PAPAN_TANDA_MAIN` | `ST_PAPAN_TANDA_CAT03` | `SPECIFICATION_CATEGORY_POPUP` | 274 |
| 27 | `PP-27` | `FAMILY_P2` | `SCR_PAPAN_TANDA_MAIN` | `ST_PAPAN_TANDA_CAT04` | `SPECIFICATION_CATEGORY_POPUP` | 243 |
| 28 | `PP-28` | `FAMILY_P2` | `SCR_PAPAN_TANDA_MAIN` | `ST_PAPAN_TANDA_ALL_CATEGORIES_VIEWED` | `COMPONENT_SPEC_LIST_ALL_VIEWED` | 0 |
| 29 | `PP-29` | `FRAME` | `SCR_RUMUSAN` | `ST_RUMUSAN_BASE` | `FRAME_SUMMARY_BASE` | 612 |
| 30 | `PP-30` | `FRAME` | `SCR_KUIZ` | `ST_KUIZ_INTRO` | `QUIZ_INTRO` | 216 |
| 31 | `PP-31` | `FRAME` | `SCR_KUIZ` | `ST_KUIZ_Q1` | `QUIZ_QUESTION_1` | 545 |
| 32 | `PP-32` | `FRAME` | `SCR_KUIZ` | `ST_KUIZ_Q5` | `QUIZ_QUESTION_5` | 363 |
| 33 | `PP-33` | `FRAME` | `SCR_KUIZ` | `ST_KUIZ_RESULT` | `QUIZ_RESULT` | 239 |
| 34 | `PP-34` | `FRAME` | `SCR_TAMAT` | `ST_TAMAT_BASE` | `FRAME_END_BASE` | 240 |

---

# 4. Checkable gates — 87 of 87 pass

Every gate is asserted against parsed model records or the parsed PPTX package. Off-canvas
production shapes are separated from learner-canvas shapes by geometry (`x + w <= 0`), so a gate can
say "not on the learner canvas but present in production metadata" and mean it.

## 4.1 Source and model

```
SOURCE_ROW_COUNT_REMAINS = 26            SOURCE_ASSET_COUNT_REMAINS = 14
PROOF_SOURCE_ROWS_CREATED = 0            PROOF_STATES_WITHOUT_PARENT = 0
PROOF_INTERACTION_ITEMS_WITHOUT_SOURCE_BINDING = 0
PROOF_RETURN_TARGET_MISSING = 0
```

## 4.2 Family S

```
FAMILY_S_PROOF_COMPONENT = STRUKTUR_PERSISIR_AIR
FAMILY_S_EXAMPLES = 5                    FAMILY_S_POPUPS = 5
FAMILY_S_CLOSE_ICONS = 5                 FAMILY_S_TEXT_TUTUP_BUTTONS = 0
FAMILY_S_KEMBALI_TARGET = SCR_GM_STRUKTUR
FAMILY_S_PREMATURE_KEMBALI = 0
```

`FAMILY_S_PREMATURE_KEMBALI` reads the **drawn fill colour** of the Kembali button back out of the
package and requires the enabled fill to appear only on the all-viewed state. A gate that merely
checked the model would have proved nothing about the deck.

## 4.3 Family P1

```
FAMILY_P1_PROOF_COMPONENT = KERUSI_TAMAN
FAMILY_P1_EXAMPLE_DETAIL_PRESENT = true
FAMILY_P1_SPEC_ITEMS_PRESENT = 4
FAMILY_P1_POPUP_PARENT_IS_EXAMPLE_DETAIL = true
FAMILY_P1_POPUP_RETURN_TARGET_IS_EXAMPLE_DETAIL = true
FAMILY_P1_KEMBALI_TARGET_IS_COMPONENT_OVERVIEW = true
FAMILY_P1_SOURCE_ROWS_CREATED_BY_SPLIT = 0
```

The four specification items — Bahan, Dimensi, Penyambungan, Kemasan — are the module's own labelled
lines for `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-01`. `_spec_body` **raises** if a requested label has no
source-attested line, so a specification popup can never be filled with invented text.

## 4.4 Family P2

```
FAMILY_P2_PROOF_COMPONENT = PAPAN_TANDA
FAMILY_P2_CATEGORIES = 4                 FAMILY_P2_POPUPS = 4
FAMILY_P2_GENERIC_ONE_ITEM_CONTOH_SCREEN = 0
FAMILY_P2_SOURCE_ROWS_CREATED_BY_SPLIT = 0
FAMILY_P2_POPUP_RETURN_TARGET_IS_SPEC_LIST = true
FAMILY_P2_CATEGORY_LOCATORS_RETAINED = true
```

## 4.5 Frame screens

```
S01_NOTES_POLICY = SPOKEN_ENTRY_TITLES_PLUS_ORIENTATION
S01_SPOKEN_ELEMENTS = 4                  S01_MULA_BUTTON = true
S01_PL06_TITLE_SPOKEN = true             S01_TOPIC_TITLE_SPOKEN = true
S01_ORIENTATION_SPOKEN = true            S01_MULA_INSTRUCTION_SPOKEN = true
S01_COURSE_INTRO_REPEATED = false        S01_PL06_OBJECTIVES_REPEATED = false
S01_TOPIC_LIST_REPEATED = false
S01_COURSE_TITLE_NOT_SPOKEN = true       S01_COURSE_TITLE_ON_CANVAS = true

S02_CAST = Alya + Encik Rahman           S02_CAST_IN_TRANSCRIPT = true
S02_MS2680_LEARNER_CLAIMS = 0            S02_MS2680_IN_PRODUCTION_PANEL = true
S02_GENERIC_ROLE_NAMES_AS_FINAL_NAMES = 0

S03_NARRATOR = HILMI                     S03_HILMI_REINTRODUCED_AS_NEW = false
S03_HILMI_SPEAKER_LABEL = true           S03_MIND_MAP_DIRECTION_PRESENT = true
HILMI_LABEL_ON_S03_ONLY = 0 elsewhere

QUIZ_MULA_KUIZ_PRESENT = true            QUIZ_MULTIPLE_RESPONSE_LETTER_LABELS = 0
QUIZ_IMMEDIATE_FEEDBACK_VARIANTS = 2     QUIZ_RATIONALE_LEARNER_FACING = 0
QUIZ_RESULT_SCORE / VERDICT / CONTROLS = present

TAMAT_SHELL_NEXT_STATE = disabled        TAMAT_NO_CUSTOM_NEXT_BUTTON = 0
TAMAT_UNVERIFIED_ROUTE_ON_CANVAS = false TAMAT_LOGICAL_DESTINATION_IN_PANEL = true
```

## 4.6 Notes, controls, rich text, panels

```
CONTENT_SLIDES_WITHOUT_REQUIRED_NOTES_POLICY = 0
S02_ONWARDS_PL_TITLE_IN_SPOKEN_TRANSCRIPT = 0
S02_ONWARDS_TOPIC_TITLE_ANNOUNCED_AS_ENTRY = 0
S02_ONWARDS_CONTEXT_BLOCK_PRESENT on every content slide
SILENT_STATES_WITH_NONEMPTY_NOTES = 0    TECHNICAL_IDS_IN_FINAL_NOTES = 0

DUPLICATE_CUSTOM_SETERUSNYA_WHEN_SHELL_NEXT = 0
TEXT_TUTUP_BUTTON = 0                    CLOSE_ICON_ON_EVERY_POPUP = 0 missing
POPUP_PARENT_IS_POPUP = 0                UNKNOWN_CONTROL_TYPE = 0

APPROVED_TERMS_NOT_ITALICISED = 0        PRODUCTION_IDS_ITALICISED = 0
BBQ_PIT_CAPITAL_P = 0 violations

PAGES_WITHOUT_PRODUCTION_PANEL = 0       PRODUCTION_PANEL_LEAKS_ONTO_CANVAS = 0
PRODUCTION_PANEL_MISSING_REQUIRED_FIELD = 0
```

### One gate was rewritten, and it is worth saying why

`S02_ONWARDS_ENTRY_TITLES_SPOKEN` originally searched the spoken block for the substring
`Topik 3 Bahagian 2`. It failed on Tamat — whose VO is *"Tamat Topik 3 Bahagian 2: Komponen
Landskap…"*, taken verbatim from **Bariah's own corrected exemplar, slide 75**. The gate was wrong,
not the content: the ruling forbids repeating the *entry titles*, and a completion sentence that
names the Bahagian is a different construction.

It was replaced by two narrower gates, not relaxed into one: `S02_ONWARDS_PL_TITLE_IN_SPOKEN_TRANSCRIPT`
(absolute — the PL title is never spoken again anywhere) and
`S02_ONWARDS_TOPIC_TITLE_ANNOUNCED_AS_ENTRY` (a spoken **line that begins with** the topic title,
i.e. the header form). Tamat passes both; a re-announced entry header would still fail.

---

# 5. Layout gates

```
TEXT_OVERFLOW = 0        LINE_CLIPPING = 0        PANEL_CONTENT_OVERRUN = 0
OFF_CANVAS_LEAKAGE = 0   UNINTENDED_OVERLAPS = 0
```

The renderer reports 57 `BOX_OVERLAP` events, **all of them a
modal deliberately covering the screen beneath it** — every one involves `PopupPanel`, `CloseIcon`,
`CloseGlyph`, `PopupTitle`, `PopupKicker`, `FHead` or `FBody`. Overlaps between non-modal shapes:
**0**. A modal that did not overlap its own screen would be the defect.

---

# 6. Defects found and fixed at source

Every one was fixed in the generator or the adapter and the **whole proof regenerated**. No slide was
edited by hand.

| # | Defect | Where it was fixed |
|---|---|---|
| 1 | Popup title overflowed its box on the longest Papan Tanda category — 0.672in of text in a 0.400in box | `_modal` now splits a long title into a small kicker plus the item name and **measures** the head band instead of assuming one line |
| 2 | The close icon rendered as an unreadable green glyph: a stroke-only `custGeom` is ambiguous to renderers, so the control could not be visually verified at all | the X is now a **filled** 12-point polygon in white on the blue disc — truthful in both PowerPoint and the checker |
| 3 | Specification popups repeated the item name as a field heading directly under the identical title | `_modal` suppresses a field head that equals the popup title |
| 4 | A specification body promoted out of `Label: text` began mid-sentence in lower case | `_sentence` capitalises the first character only; wording is untouched |
| 5 | **The Family P1 return page ticked all three Kerusi examples when only one had been completed** | `viewed_items` now derives completion from what the proof path actually finished, not from "some earlier page touched this screen" |
| 6 | The Family S return page used the group-complete state, implying all four Struktur components were done | the return page is now the group-master **base** state with only Struktur Persisir Air ticked |

Defect 5 is the one that mattered. That page exists precisely to prove that *completing one example
does not complete the component* — and it was rendering the opposite. It would have passed every
model-level gate, because the model was right; only the visual inspection caught it.

---

# 7. Rendering and environment limitations

The repository's normal rendering path was attempted first and failed, exactly as at v0.3:

```
$ soffice --headless --convert-to pdf K5PL06T03B02_v0_4_THREE_FAMILY_PROOF.pptx --outdir .
Error: source file could not be loaded
```

No PDF is produced. Installed packages are `libreoffice-core`, `libreoffice-common`,
`libreoffice-style-colibre` and `libreoffice-uiconfig-common` — there is **no Impress import
filter**, so LibreOffice cannot open a `.pptx` at all.

Rendering therefore uses the established path: read the generated package back out of the `.pptx`
and draw it with Liberation Sans, which is metric-compatible with Arial. All 34 pages were
rendered and visually inspected individually and as a contact sheet.

**This is not Microsoft PowerPoint equivalence.** It is a faithful render of the artifact under a
metric-compatible font. Two known approximations: the renderer draws a `prstGeom` ellipse as its
bounding box, so the close icon reads as a square in the proof images while the package carries a
true ellipse; and Microsoft PowerPoint's own font wrapping remains unverified.

Page images and the contact sheet were produced for internal QA and are **not** committed.

---

# 8. PENDING_HUMAN — not mechanically passed

These need a person to look, and none of them is marked PASS.

| # | Item | What to look at |
|---|---|---|
| 1 | Family P1 readability and density | the example-detail screen leaves a wide empty band between the specification cards and the Contoh line |
| 2 | Papan Tanda category treatment | four categories from one source row — do the labels read as specification facets rather than as products? |
| 3 | Visual clarity of the close icon | 0.42in disc, top-right of the modal — large enough, and unambiguous against the panel edge? |
| 4 | Alya / Encik Rahman visual treatment | S02 currently shows name + role as text; the character video treatment is a specification only |
| 5 | S01 VO naturalness | two titles, an orientation sentence and a Mula instruction read consecutively |
| 6 | S03 reflection wording | the reflection question carried forward from the Bariah exemplar |
| 7 | Rumusan visual treatment | four unlabelled statements; Bariah approved the wording, not this layout |
| 8 | Quiz presentation | option spacing, and whether both feedback variants shown side by side is the right storyboard convention |
| 9 | Tamat instruction clarity | "Tutup tetingkap pelajaran untuk keluar" with no visible next control |
| 10 | Microsoft PowerPoint font wrapping | every measured line, re-checked in the real application |

---

# 9. Non-blocking open items, carried forward unchanged

| Item | Status |
|---|---|
| U-01 MS2680 source verification | `PENDING_SOURCE_VERIFICATION` — excluded from learner content, retained in the S02 production panel |
| U-02b Pengurus Projek name | `PENDING_CHARACTER_NAME` — not used in B02 |
| U-03 physical LMS exit | `PENDING_FIRDAUS_CONFIRMATION` — shell Next disabled on Tamat, logical destination in metadata only |
| U-05 quiz rationale placement | `PENDING_BARIAH_CONFIRMATION` — rationale is production metadata only |
| `B02-CAIR-INT-001` module DOCX integrity | open; `SOURCE_INTEGRITY_FULLY_VERIFIED` is **not** claimed |

---

# 10. Standing

Proof build only. The v0.3 generator and its output bundle are unchanged. No component was
propagated, no slide was manually patched, no multimedia was created, no final visual asset was
bound, no canonical `P#` was minted. **READY does not authorise full propagation** — that is the next
stage's decision, not this one's.
