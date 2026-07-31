# BARIAH_FEEDBACK_IMPLEMENTATION_MAP — K5 PL06 T03 B02 v0.3

```
REVIEW_READY · PROVISIONAL_CAIR_EXECUTION
CAIR_INTEGRITY_EXCEPTION_FOR_REVIEW_BUILD_ONLY · PENDING_FINAL_BARIAH_CONFIRMATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

Where each piece of confirmed Bariah feedback landed in the v0.3 deck, and how it was verified.

---

## 1. The core finding

> *"The learning-slide treatment was generally acceptable, but the generator omitted instructional
> content contained inside source tables."* — Updated S&G v0.2 §1

| Was | Is now |
|---|---|
| 9 components → 9 detail slides; table content summarised or dropped | 9 components → 9 main explanation screens **+ 9 example screens + 26 popup states** |
| Table treated as one visual or one bullet | Every meaningful row is a clickable Level 2 item with its own popup and VO |
| 19 screens | **26 physical learner screens**, 46 runtime states, 63 review pages |

**26 source rows in, 26 popups out, zero omitted, zero duplicated.**

---

## 2. Feedback → implementation → verification

| S&G v0.2 clause | Confirmed direction | Where it landed | Verified by |
|---|---|---|---|
| §3.1 | Source table → separate example screen `Contoh [Nama Komponen]` | 9 example screens | screen/state map §1 |
| §3.1 | Each meaningful row → one clickable Level 2 item | 26 item cards | `SOURCE_ROWS_MAPPED = 26` |
| §3.1 | Each item → one popup | 26 popup states | `DUPLICATE_ROW_MAPPINGS = 0`, `POPUPS_WITHOUT_PARENT = 0` |
| §3.2 | Popup carries Jenis/Bahan + Fungsi & Penerangan + Contoh + visual + VO | adaptive popup | source map §3 |
| §3.2 | Missing source field → production note, invent nothing | absent fields render **no heading** | source map §3, `NOT_PRESENT_IN_SOURCE` |
| §3.3 | Generic title `Contoh [Nama Komponen]` | all 9 example screens | screen/state map §1 |
| §2.1 | Maximum navigation depth = 2; popup is a state | popups are states rendered as review pages | `INVALID_NAVIGATION_DEPTH = 0` |
| §4.1 | Level 1 cards clickable in any order | group master cards | screen/state map §4 |
| §4.1 | Global `Seterusnya` disabled until group complete | drawn disabled on base, enabled on complete | `PREMATURE_GLOBAL_SETERUSNYA = 0` |
| §4.2 | Main screen `Seterusnya` gated on VO end | drawn disabled on every main screen | `PREMATURE_GLOBAL_SETERUSNYA = 0` |
| §4.2 | Final VO leads explicitly to the example screen | *"Mari lihat contoh bagi … di halaman seterusnya."* appended to all 9 | notes of each `*_MAIN` page |
| §4.3 | Items clickable in any order; tick after viewing | per-item viewed state and tick | `ITEMS_WITHOUT_VIEWED_STATE = 0` |
| §4.3 | `Kembali` disabled until all items viewed, returns to group master | disabled on base and popup pages, enabled on all-viewed | `PREMATURE_KEMBALI = 0` |
| §4.4 | Viewed/completed states persist, never relock | stated on every affected page's production panel | screen/state map §2 |
| §5.1 | No technical IDs on the learner canvas | all IDs off-canvas | `LEARNER_CANVAS_TECHNICAL_TOKENS = 0` |
| §5.2 | `Hilmi:` prefix on S03 only | S03 notes only | `hilmi_prefix_pages = ['RP-003']` |
| §5.2 | Silent states have genuinely empty Notes — no placeholder | empty notes on all silent states | `NONEMPTY_NOTES_ON_SILENT_STATES = 0` |
| §5.2 | Notes carry exact VO/transcript only | no `VO PENUH:`, no IDs, no diagnostics | `notes_grammar_violations = 0` |
| §5.3 | No final photograph, audio, video, animation or popup multimedia | text specifications only | `embedded_media = 0` |
| §6.1 | S01 uses `MULA`, no auto-advance | MULA button | S01 page |
| §6.2 | S02 titled *Pengenalan / Komponen Landskap*, dialogue in Notes | character labels on canvas, transcript in Notes | S02 page |
| §6.2 | Learner shows baseline knowledge, not zero knowledge | turn 3 states what the learner already understands | S02 Notes |
| §6.2 | No unverified MS2680 claim | none present | S02 production panel |
| §6.3 | S03: context + all subtopics + one reflection question | all three present | S03 page and Notes |
| §6.5 | Rumusan: no structural labels, contractor register | labels absent | `rumusan_banned_labels = 0` |
| §6.6 | Quiz 5 items, 4 MCQ + 1 MR, 60%, feedback, Semak/Ulang | all present | Kuiz page and Notes |
| §6.7 | Tamat concise; routing stays in production metadata | no assumption on canvas | Tamat page |
| §7 | `BBQ Pit` capital P; `Promenade` corrected; `reka bentuk` spaced | applied | content data |
| §8.1 | Regenerate rather than patch the old 19-screen deck | new model, new generator, new IDs | run manifest |

---

## 3. Feedback that changed the build mid-flight

Six artifact defects were found by rendering and fixed **at source** — generator or controlled content
data — never by editing a slide.

| Defect | Fix |
|---|---|
| Component name repeated in title bar and body heading on main screens | title bar carries the group/section |
| Popup `JENIS / BAHAN` repeated the popup heading on 20 of 26 rows | field suppressed when identical |
| `Tutup` drawn over the last field's text | reserved footer band |
| Two asset IDs abbreviated (`-x38`, `-x46`) and so untraceable | written in full |
| Global `Seterusnya` collided with row-2 labels (1.01 × 0.35 in) | grid raised; card geometry unchanged |
| Card visual specs truncated mid-sentence | short complete cue on card, full spec off-canvas |

---

## 4. What was deliberately NOT changed

| Item | Why |
|---|---|
| Papan Tanda = 1 source row, BBQ Pit = 1 source row | Source evidence. A-05 is an interaction ruling; it never rewrites source identity. Built as `SINGLE_ITEM_EXAMPLE_TREATMENT`, flagged for confirmation. |
| `Kerusi Komposit` unbalanced parenthesis | `NORMALISATION_DECLINED` — either repair changes how the cell parses. |
| Accepted card geometry (`CARD_W`, `CARD_H`, `GAP_X`, `GAP_Y`, label box) | Reviewed and accepted; only the vertical start moved, to open the navigation strip. |
| The 14 source assets | Named in visual directions, **none bound**. Binding starts after approval. |

---

## 5. Open against v1.0

Two rules from the course-wide S&G v1.0 are **deliberately overridden for this B02 review build**, on
CAIR-provisional authority, and both need Bariah's final word:

| v1.0 rule | v0.3 build | Decision |
|---|---|---|
| §5.4.1 routes tables and reference lists to **Pop Up (No VO)** | every popup carries VO | `B02-R-2` |
| §5.5.1 requires Rumusan to display *Kepentingan → Apa Yang Dipelajari → Manfaat* | labels not displayed | `B02-R-6` |

Two further v1.0 rules are **carried forward** because v0.2 is silent and does not revoke them:
`L-01` (PL pronunciation note, kept off-canvas) and `L-02` (Mind Map on S03, as a text specification only).
