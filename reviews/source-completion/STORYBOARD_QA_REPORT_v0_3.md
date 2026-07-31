# STORYBOARD_QA_REPORT — K5 PL06 T03 B02 v0.3

```
REVIEW_READY · PROVISIONAL_CAIR_EXECUTION
CAIR_INTEGRITY_EXCEPTION_FOR_REVIEW_BUILD_ONLY · PENDING_FINAL_BARIAH_CONFIRMATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

| | |
|---|---|
| Artifact | `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3.pptx` |
| Review pages | 63 |
| Physical learner screens | 26 |
| Runtime states | 46 |
| Source rows | 26, each mapped to exactly one popup |

Validation reuses the **hardened scoping discipline from the Stage 1.5 audit**: every check names the
structure it inspects, and no whole-document grep stands in for a structured assertion. Learner-canvas
token checks read only shapes at x ≥ 0; production-panel checks read only shapes at x < 0; button
enable state is read from the **fill colour in the generated package**, not from the generator's memory.

---

# 1. CHECKABLE

| Gate | Required | Actual | Result |
|---|---:|---:|:-:|
| `SOURCE_ROWS_EXPECTED` | 26 | 26 | ✅ PASS |
| `SOURCE_ROWS_MAPPED` | 26 | 26 | ✅ PASS |
| `DUPLICATE_ROW_MAPPINGS` | 0 | 0 | ✅ PASS |
| `OMITTED_SOURCE_ROWS` | 0 | 0 | ✅ PASS |
| `POPUPS_WITHOUT_PARENT` | 0 | 0 | ✅ PASS |
| `POPUPS_WITHOUT_VO` | 0 | 0 | ✅ PASS |
| `INVALID_NAVIGATION_DEPTH` | 0 | 0 | ✅ PASS |
| `ITEMS_WITHOUT_VIEWED_STATE` | 0 | 0 | ✅ PASS |
| `COMPONENTS_WITHOUT_COMPLETE_RULE` | 0 | 0 | ✅ PASS |
| `GROUPS_WITHOUT_COMPLETE_RULE` | 0 | 0 | ✅ PASS |
| `PREMATURE_KEMBALI` | 0 | 0 | ✅ PASS |
| `PREMATURE_GLOBAL_SETERUSNYA` | 0 | 0 | ✅ PASS |
| `NONEMPTY_NOTES_ON_SILENT_STATES` | 0 | 0 | ✅ PASS |
| `LEARNER_CANVAS_TECHNICAL_TOKENS` | 0 | 0 | ✅ PASS |
| `MISSING_SOURCE_LOCATORS` | 0 | 0 | ✅ PASS |
| `ORPHAN_SOURCE_ASSETS` | 0 | 0 | ✅ PASS |

**All 16 CHECKABLE gates pass.**

## 1.1 Supporting measurements

| Measurement | Value |
|---|---|
| `review_pages` | 63 |
| `physical_screens` | 26 |
| `runtime_states` | 46 |
| `popup_states` | 26 |
| `slides_in_package` | 63 |
| `rumusan_banned_labels` | 0 |
| `notes_grammar_violations` | 0 |
| `embedded_media` | 0 |
| `pl_note_offcanvas` | True |
| `hilmi_prefix_pages` | ['RP-003'] |
| `ticks_are_native` | True |

## 1.2 Render inspection

LibreOffice in this container ships as `libreoffice-core` only — **no import filter for any document
format** — so it cannot open a `.pptx` at all, and the missing packages are not fetchable (404 from the
archive). Rendering is therefore done by parsing the **generated package** back out of the `.pptx` and
drawing it with metric-accurate font measurement (Liberation Sans is metric-compatible with Arial).
It renders the artifact, not the generator's memory. This is stated as a limitation, not as an
equivalent of a PowerPoint render — see §3.

| Check | Result |
|---|---|
| Pages rendered and inspected | 63 / 63 |
| `TEXT_OVERFLOW` | 0 |
| `LINE_CLIP` (text wider than its box) | 0 |
| `OFFCANVAS_LEAK` (production panel crossing x=0) | 0 |
| `PANEL_CONTENT_OVERRUN` | 0 |
| `BOX_OVERLAP` | 80 — all are the popup modal over its own example screen, drawn last and therefore on top |

## 1.3 Defects found and fixed during this build

Every fix was made in the generator or the controlled content data. **No generated slide was hand-patched.**

| # | Defect | Where fixed |
|---|---|---|
| 1 | Main explanation screen repeated the component name in both the title bar and the body heading | generator — title bar now carries the group/section |
| 2 | Popup `JENIS / BAHAN` field repeated the popup heading verbatim on 20 of 26 rows | generator — field suppressed when identical to the label |
| 3 | Popup `Tutup` button was drawn over the last field's text | generator — reserved footer band inside the panel |
| 4 | Two asset IDs written in abbreviated form (`-x38`, `-x46`) so they were not traceable | controlled content data — both written in full |
| 5 | Global `Seterusnya` on the group master collided with row-2 component labels (measured 1.01 × 0.35 in) | generator — grid raised; `CARD_W`, `CARD_H`, `GAP_X`, `GAP_Y` and the label box unchanged |
| 6 | Group-master card visual specs truncated mid-sentence | generator — short complete source cue on the card, full spec in the production panel |
| 7 | **BBQ Pit popup content overran its panel** — the densest specification row. Each field box fitted its own text, so no box overflowed individually while their sum overran the panel | generator — panel sized to content within the usable band, body font steps down only if needed |
| 8 | **The checker never verified that a child sits inside its parent panel**, which is why defect 7 passed | renderer/checker — `PANEL_CONTENT_OVERRUN` added, scoped to the popup's own children so cards behind the modal are not falsely flagged |
| 9 | Renderer ignored `spcBef` and `custGeom`, so bullets looked tighter than PowerPoint will draw them and completion ticks drew as squares | renderer — both now honoured, so the inspection is faithful |

Items 1–7 were artifact defects. Items 8 and 9 were **checker/renderer** defects — 8 is the one that let 7 through, and is recorded because a checker that cannot see a class of defect is itself a finding. Item 9: the ticks were always correct
`custGeom` checkmarks in the package (verified: 5 tick shapes, 7 path points each, on the all-viewed page).

---

# 2. PENDING_HUMAN

**None of these is marked PASS. A mechanical harness cannot decide them.**

| # | Item | Why it needs a human | Authority |
|---|---|---|---|
| H-1 | **Papan Tanda single-item example treatment** | The source has one row, so `Contoh Papan Tanda` carries one clickable item and the Level 2 gate is satisfied by one click. Built as `SINGLE_ITEM_EXAMPLE_TREATMENT` under B02-A-05. | Bariah |
| H-2 | **BBQ Pit single-item example treatment** | Same. Four source-attested lettered sub-fields exist and could support a split, but splitting is an interaction ruling, not a source correction. | Bariah |
| H-3 | **Popup readability and density** | The five `SPESIFIKASI` components produce dense popups. Geometry is measured clean; whether it *reads* well is judgement. Drinking Fountain row 1 is the densest, with seven lettered sub-fields. | Bariah |
| H-4 | **Character naming** | S02 uses role-neutral `PELATIH` / `PENYELIA TAPAK`. The B02 cast is still unproven. | Bariah |
| H-5 | **Rumusan site-application wording** | The fourth bullet must read as genuine site application. Lexical proxies false-pass. | Bariah |
| H-6 | **Exact Tamat route** | The next destination is unverified and is held in production metadata only; the learner canvas shows no routing assumption. | Course navigation owner |
| H-7 | **N-06 punctuation** | Unbalanced parenthesis in `Kerusi Komposit` left as found. Two readings exist; either repair changes how the cell parses. | Bariah |
| H-8 | **Final visual execution** | All visuals are text specifications with source locators. No asset is bound. | MMD, after approval |
| H-9 | **Final approval of the provisional CAIR rulings** | R-1…R-6, L-01, L-02, A-05, A-06, A-09, N-06 are all `confirmed-CAIR-provisional`. | Bariah, then Firdaus / CAIR |
| H-10 | **Module DOCX integrity exception closure** | `B02-CAIR-INT-001` must be closed before canonical freeze, production approval or MMD build. | Firdaus / CAIR |

---

# 3. Limitations of this QA

1. **No PowerPoint render exists.** The container has no Impress filter and cannot obtain one. Font
   substitution, autofit recomputation on open, and PowerPoint's own line breaking remain unverified.
   The render here is metric-accurate but is not PowerPoint.
2. **`spAutoFit` is not used** anywhere in this build — every text box is `noAutofit` with measured
   geometry — which removes the largest source of open-in-PowerPoint drift, but does not eliminate it.
3. **The module DOCX is unhashed.** Text provenance rests on a derived extraction cross-checked against
   the hashed PDF. See `B02-CAIR-INT-001`.
4. **Interaction behaviour is specified, not executed.** Ticks, gating and persistence are drawn as
   resolved states and described in production metadata; nothing is running.
