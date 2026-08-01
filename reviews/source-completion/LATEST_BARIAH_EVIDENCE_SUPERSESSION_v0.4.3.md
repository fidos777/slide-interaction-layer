# LATEST_BARIAH_EVIDENCE_SUPERSESSION — v0.4.3

```
LATEST_EVIDENCE_PRECEDENCE_RECORDED
ACTIVE_EVIDENCE_CONFLICTS            = 0
SUPERSEDED_RULINGS_RECORDED          = 1 direction + 6 gate IDs
REGRESSION_CHECKS_SILENTLY_REMOVED   = 0
COMPONENT_MAIN_SELF_RESOLVED_BY_CC   = 0
PENDING_HUMAN_ITEMS_CLOSED_BY_CC     = 0
```

Evidence date **1 August 2026**. Superseding artifacts: the three screenshots frozen at
`B02_V0_4_INPUT_FREEZE.md` §2C, evidence class `BARIAH_DIRECT_SCREENSHOT`.

---

# 1. Precedence

Where the three frozen screenshots speak, they outrank every earlier source — the annotated v0.3
deck, the correction exemplars, and task transcript text alike. Where they are silent, the earlier
position stands unchanged. **Silence is not supersession**, and nothing below was retired because
it had become inconvenient.

| Rank | Source | Class |
|---|---|---|
| 1 | The three 1 Aug 2026 screenshots | `BARIAH_DIRECT_SCREENSHOT` |
| 2 | Annotated v0.3 deck, review guide, correction exemplars | `FROZEN_ARTIFACT_OOXML` |
| 3 | Task transcript statements | `TASK_TRANSCRIPT_ONLY` |
| 4 | Module source rows and assets | `SOURCE_ATTESTED` |

---

# 2. Rulings superseded

## 2.1 S01 spoken transcript — 4 blocks become 3

Evidence: `B02_BARIAH_S01_EVIDENCE.jpg`, the grey block is the build she reviewed, the boxed block is
labelled **"Speaker Notes: Edit to this"**.

| | Before | After |
|---|---|---|
| 1 | Pakej Latihan 06: Pengurusan Operasi Pembinaan Landskap. | **PL06:** Pengurusan Operasi Pembinaan Landskap. |
| 2 | Topik 3 Bahagian 2: Komponen Landskap. | *unchanged* |
| 3 | Dalam bahagian ini, anda akan mempelajari tentang komponen landskap. | **removed** |
| 4 | Klik Mula untuk meneruskan. | **Klik butang “Mula” untuk memulakan pembelajaran.** |

The model's `notes_policy` changes with it: `SPOKEN_ENTRY_TITLES_PLUS_ORIENTATION` →
`SPOKEN_ENTRY_TITLES_PLUS_START_INSTRUCTION`, because there is no longer an orientation sentence to
name.

Two canvas divergences from her corrected page were also found and fixed: the **Topik/Bahagian body
line** was missing (her page carries it below the PL06 line, distinct from the title band), and the
**`ARAHAN VISUAL — SPESIFIKASI SAHAJA` heading** above the visual direction was not being drawn.

The two title annotations — ① retitle to the full Topik/Bahagian line, ② remove the standalone
"Komponen Landskap" — were already implemented at Stage 4.1 and are now bound to a frozen oracle
rather than to transcript text.

## 2.2 Family S Contoh screens — CONDITIONAL becomes REQUIRED

Evidence: `B02_BARIAH_VISUAL_POLICY_EVIDENCE.png`, 4:37 PM, verbatim:

> Semua contoh ada visual. Semua pop up ada visual, KECUALI pop up Spesifikasi (bahan, dimensi etc)

Stage 4.2B classified `EXAMPLE_SELECTION_SCREEN` as `CONDITIONAL / PENDING_HUMAN` on the reasoning
that her corrected slide 12 shows no screen-level direction and that the rule was qualified
*"where an example visual is presented"*. **The frozen message carries no such qualifier.** That
reading is withdrawn.

The requirement attaches to each *example*, and on a selection screen every example is a card. Each
card therefore carries **its own source-attested direction** — the same string its example popup
shows, bound to its own `source_row_uid`. Nothing is composed at screen level, so the screen still
invents no subject of its own. 16 example cards across 4 screens.

## 2.3 Struktur Persisir Air component main — conflict closed

Evidence: `B02_BARIAH_STRUKTUR_PERSISIR_EVIDENCE.jpg`, 4:40 PM.

Stage 4.2B disclosed an unresolved conflict and rendered neither side as settled. Her corrected
component main shows one direction and no other:

```
ACTIVE      [Visual: Pelbagai Struktur Persisir Air. Tidak dibenamkan.]
SUPERSEDED  [Visual: Rajah 23 — Contoh Boardwalk dalam Taman Paya Bakau, modul ms 239.
             Tidak dibenamkan.]   ← at COMPONENT-MAIN level only
```

The supersession is **level-specific**. Rajah 23 remains the Boardwalk *example row's* own
source-attested direction and still appears in the Boardwalk example popup and on its card; what is
superseded is its use as the component-main screen's direction. A gate asserts both halves.

The superseded direction is disclosed in the production panel of that page under
`ARAHAN DIGANTI — SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT`, and a gate fails if that disclosure is
dropped or if the superseded string ever reaches the learner canvas.

---

# 3. Rulings deliberately NOT superseded

## 3.1 The other eight component mains stay a human decision

Her 4:40 PM caption reads:

> Slide 5 - apply to yang lain where applicable/necessary

That authorises the **principle** for the other component mains. It does not name content for any of
them, and "where applicable/necessary" is a judgement she has reserved, not delegated. All eight
therefore remain `CONDITIONAL / PENDING_HUMAN`, each showing the module's own source-attested visual
text marked `PROVISIONAL_VISUAL_PROPOSAL`.

`COMPONENT_MAIN_SELF_RESOLVED_BY_CC = 0`. `PENDING_HUMAN_ITEMS_CLOSED_BY_CC = 0`.

The Stage 4.1 `Pelbagai {name}` pattern stays retired: it was supplied for one screen and had been
applied to nine.

## 3.2 Untouched

The 26-row source baseline, the 14-asset baseline, the S / P1 / P2 architecture, interaction counts,
runtime-state counts, completion topology, quiz architecture, and the bounded screen-level `Klik`
parity scope are all unchanged by this stage.

---

# 4. Gate supersessions — every retired ID has a named replacement

No check was removed. Each superseded ID is retained in the suite as an explicit `SUPERSEDED`
marker, so a reader sees that a ruling changed rather than finding a check quietly absent.

| Superseded gate | Why | Replacement |
|---|---|---|
| `S01_NOTES_POLICY` (old value) | policy renamed with the orientation sentence | `S01_NOTES_POLICY` = `SPOKEN_ENTRY_TITLES_PLUS_START_INSTRUCTION` |
| `S01_SPOKEN_ELEMENTS` = 4 | three blocks now | `S01_SPOKEN_ELEMENTS` = 3 |
| `S01_PL06_TITLE_SPOKEN` (long form) | reworded to `PL06:` | `S01_PL06_TITLE_SPOKEN` (exact string) **+** `S01_PL06_TITLE_LONG_FORM_WITHDRAWN` |
| `S01_ORIENTATION_SPOKEN` = True | sentence removed | `S01_ORIENTATION_SENTENCE_REMOVED` (absolute) |
| `S01_MULA_INSTRUCTION_SPOKEN` (old wording) | reworded | `S01_MULA_INSTRUCTION_SPOKEN` (exact) **+** `S01_MULA_INSTRUCTION_OLD_WORDING_WITHDRAWN` |
| `EXAMPLE_SELECTION_SCREENS_WITH_INVENTED_VISUAL` | a visual here is now required, not evidence of invention | `EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL` **+** `EXAMPLE_SELECTION_SCREENS_WITH_PER_EXAMPLE_VISUAL` **+** `EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED` **+** `EXAMPLE_SELECTION_SCREEN_LEVEL_INVENTED_DIRECTION` |
| `EVIDENCE_CONFLICTS_DISCLOSED` > 0 | passing required a conflict to stay alive | `ACTIVE_EVIDENCE_CONFLICTS` = 0 **+** `SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL` = 0 **+** `SUPERSEDED_DIRECTION_RENDERED_AS_ACTIVE` = 0 |
| `EVIDENCE_CONFLICTS_IN_PRODUCTION_PANEL` (vacuous at 0 conflicts) | population now empty | kept live for any future conflict, **plus** the supersession-disclosure gates above |

Each replacement is at least as strong as what it retires. The example-selection replacements are
strictly stronger: the retired gate could only detect the *presence* of a direction, while the new
ones demand a direction on every one of these screens **and** that every card's text be identical to
its own source row's — which the retired gate could never have caught.

`CONDITIONAL_PENDING_HUMAN` moves 12 → 8. The four that left were the example-selection screens; the
eight that remain are pinned by `CONDITIONAL_PENDING_HUMAN_ARE_COMPONENT_MAINS`.

---

# 5. One occlusion gate reworked, not loosened

Rendering per-example captions put text behind the modal on popup states.
`TEXT_COVERED_BY_OPAQUE_SHAPE` flagged 16 of them. A popup state **is** a modal overlay — the screen
behind it is meant to be obscured — so that occlusion is excluded from the defect count and then
pinned from four directions, any one of which fails if the exclusion widens:

```
MODAL_OCCLUDED_SHAPES_EVALUATED     = 16          exact count
MODAL_OCCLUDED_SHAPE_NAMES          = [VisualDir] only card captions
MODAL_OCCLUSION_ON_NON_POPUP_PAGES  = 0           only STATE_POPUP pages
NON_MODAL_OCCLUSIONS                = []          only PopupPanel
```

Any other covered text still fails `TEXT_COVERED_BY_OPAQUE_SHAPE` exactly as before.

---

# 6. What this stage does not authorise

`PRODUCTION_APPROVED`, `CANONICAL_FREEZE`, `MMD_BUILD_READY`, `SOURCE_INTEGRITY_FULLY_VERIFIED` and
`MICROSOFT_POWERPOINT_EQUIVALENCE` remain unasserted. `B02-CAIR-INT-001` is still open and still
blocks canonical freeze. Eight component-main visual decisions are still Bariah's to make.
