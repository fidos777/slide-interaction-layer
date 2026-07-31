# SAMPLE_IMPLEMENTATION_PLAN — K5 PL06 T3 B02, 19-slide visual sample

- **Status:** gate document — **docs-only. NOT IMPLEMENTED.**
- **Standing:** sample only — **NOT CAIR-ratified**. `K5_LIVE_RATIFICATION_LOCKED`
- **Authority key:** `(K5, PL06, T3)`. B02 is a bahagian below the key; it gets no key row.
- **Gate:** read `INPUT_CUSTODY.md`, `B02_SAMPLE_ASSUMPTIONS.md`, `SCREEN_CHANGE_MATRIX.md` and
  `SOURCE_QA_PATCH_LIST.md` first.

---

## 1. Purpose

Produce **one** visual sample of B02 across 19 screens so that the assumptions in
`B02_SAMPLE_ASSUMPTIONS.md` can be **seen and judged**, and so that the CAIR family question — open
since 16/06, never answered because nothing has ever been rendered — becomes answerable:

> *Does it read as one coherent interaction family? Or does the child feel like a different deck?*
> — `LOCAL_REVIEW_CHECKLIST.md`

The sample is a **judgement instrument**, not a deliverable. Its success condition is that a reviewer
can accept or reject `A-05` on sight — not that it ships.

---

## 2. Standing constraints — hold for every phase

| # | Constraint |
|---|---|
| 1 | **Do not unlock K5.** `SBAT-ADR-004` §3 and `OPEN_COURSES = ["K4"]` remain as they are. |
| 2 | **Do not alter the live CAIR decision desk**, `BARIAH_DATA`, `INTENT_MAP` or `saveCard`. |
| 3 | **Do not modify either PPTX.** `ee4f5479…8bb9e7` and `24dcaa04…1d471c` are read-only evidence. |
| 4 | **Do not write to `cair_decisions`** or the MMD readiness register. |
| 5 | **Do not mint or cite a bare `P#`.** Live `P0`/`P6`/`P11` must not be reused or repointed. |
| 6 | **Do not write `K5-DR-###` into any sample artefact.** The namespace is provisional, not canonical. |
| 7 | **Do not create a baseline, manifest, digest pin, candidate or freeze.** |
| 8 | Every sample artefact carries the banner **`SAMPLE — NOT CAIR-RATIFIED`**. |
| 9 | `POPUP` is never selected. Both realisations are DEFERRED. |
| 10 | The 3-term italic lexicon is closed: `Water Feature`, `Drinking Fountain`, `BBQ pit`. Nothing added by inference. |
| 11 | **No named scenario cast.** The current B02 cast is not provable (`A-13`); use role-neutral placeholders. Do not revive `Haziq`/`Encik Roslan` and do not assert `Alya`/`Encik Rahman`. `Hilmi` remains the narrator. |
| 12 | Screens are cited as `S01`–`S19`. The storyboard aliases `Slide 4`, `Slide 4(1)`, `Slide 5b`, `Slide 6` are DO_NOT_CITE. |

---

## 3. Phases

### Phase 0 — Ratify the gate *(no build)*
Confirm the four gate documents, and in particular obtain a position on the two high risks
(`A-05`, `A-02`) **before** any screen is built. Phase 0 is the decision point; everything after it is
execution.

**Exit:** gate accepted, or `A-05` overturned and the plan revised.

### Phase 1 — Parameter sheet *(no screens)*
Derive one parameter set from the measured geometry, so no screen copies an absolute coordinate.

- Stage 13.3333 × 7.5 in · content band `x = 0.7917`, `w = 11.75`
- **4-card family (S04, S09):** `CARD_W = 3.935`, `CARD_H = 1.9901` (aspect 1.97729),
  `GAP_X = 0.7074`, `GAP_Y = 0.3644`, `LABEL_W = CARD_W × 0.770597`, `LABEL_H = 0.4364`,
  `LABEL_GAP = 0.0185`
- **5-card family (S10, S16) — option 5B:** `CARD_W = 3.60`, `GAP_X = 0.4750`, margins 0.7917,
  row 1 = 3 cards, row 2 = 2 cards centred
- **Rules, not coordinates:** `R-LABEL-X` (centre each label on **its own card** — this is what removes
  the measured ±0.09725 in mirror error), `R-TICK` (single alignment intent for all ticks),
  `R-INSTR` (bind instruction width to grid width), `R-GRID-X`, `R-ROW-PITCH`, `R-FIT`
- **split-STATE (9 detail screens):** panel 0.8046, 1.7813 · 5.8621 × 5.2604 · heading box
  6.8667, 1.8291 · 5.6621 × 0.5068 · body 6.8667, 2.5594 · 5.6621 × 3.8708 · `Kembali` 6.0028, 7.1009 ·
  1.3277 × 0.3366, centred at 6.66665
- **Display budget:** full-width **8 lines hard / 7 target**; split-STATE line box 5.1496 in →
  **41–45 chars/line** — detail screens need a *tighter* budget than the measured full-width one
- **Label ceiling:** 22–24 chars (boxes are `noAutofit`; 25 chars overflows silently)

**Exit:** every geometric value in the sample traceable to a rule plus a measured constant.

### Phase 2 — The four measured screens
Build **S04, S09, S12, S17** first. They have measured source and carry all four high-signal
treatments. If the sample is going to fail, it fails here, cheaply.

- S04 — 4-card 2 × 2; patch `P-02`; instruction per `R-INSTR` (`P-10`)
- S09 — S04 + `visited-tick` derived from `R-TICK`; `P-09` z-order
- **S12 — the pivotal screen.** split-STATE restored, heading box restored, locator corrected to
  `IMG-05`/243 (`P-01`), section/screen title split restored (`P-08`)
- S17 — revised Rumusan: label suppression, `kontraktor`, italic terms, `P-04` `dan`

**Exit:** these four render. **Review `A-05` on S12 before Phase 3** — it governs 9 screens.

### Phase 3 — The nine detail screens
S05–S08 and S11, S13–S15 to the Phase 1 split-STATE parameters, plus S12 already built.
Content constructed; italic on S08, S14, S15.

**Exit:** the base→child→base loop is walkable for both groups.

### Phase 4 — The second card base and its completion
S10 (5-card 3+2, option 5B) and S16.
⚠️ **Conditional** — if S10 resolves to Hotspot under `K5-DR-040`, `A-04` is void and both screens are
rebuilt on the Hotspot component.

### Phase 5 — The five remaining screens
S01, S18, S19 — constructed, no decision required.
**S02 and S03 — constructed on empty decision slots** (`SCREEN_CHANGE_MATRIX` §3.1). Render both as
visibly provisional; they must not read as instantiating an SME decision that was never made.
S02 uses **role-neutral placeholders** (`A-13`). S03 may visually introduce Hilmi as narrator (`A-09`).

### Phase 6 — Self-check *(no ratification)*
Mechanical checks only, against `SME_RULE_CHECKABILITY.md`:

| Check | Grade |
|---|---|
| No `^\s*Hilmi\s*:` in any VO body | flagging-grade |
| No `Kepentingan` / `Isi Utama` / `Manfaat` prefix on S17 — **case-insensitive**, `Manfaat` as prefix | **gate-grade** |
| No `\banda\b` in S17 display or VO | deterministic, Rumusan-scoped only |
| The 3 lexicon terms carry `i="1"` wherever they appear in display | deterministic given the list |
| Display line count ≤ budget per family | deterministic |
| No label exceeds 24 characters | deterministic |
| S12 locator reads `IMG-05` / ms 243 | deterministic |
| `K5-DR-032` industry-application | ❌ **not mechanically checkable** — human review |

**Exit:** a check report. **Not** a ratification, **not** a gate pass.

---

## 4. Deliverables

| # | Artefact | Note |
|---|---|---|
| D1 | 19-screen visual sample | banner `SAMPLE — NOT CAIR-RATIFIED` |
| D2 | Parameter sheet (Phase 1) | rules + constants; no per-screen coordinates |
| D3 | Provenance map | per screen: `MEASURED` / `CONSTRUCTED`, and which assumption governs it |
| D4 | Phase 6 check report | including the checks that could not be run |
| D5 | Render-review checklist | extending `LOCAL_REVIEW_CHECKLIST.md` to 19 screens |

**Not produced:** storyboard, baseline, manifest, digest pin, candidate deck, freeze, executable
contract, compiler patch, schema change, canonical ID.

---

## 5. Risks — carried into the build, not discovered in it

### R1 — `A-05` reverts Bariah's own edit on 9 screens — **HIGH**
The sample restores canonical split-STATE where she widened the panel to within **0.0079 in** of the
Rumusan panel and deleted the heading box. S12 will not look like her review deck.
**This is the sample's central proposition, and it may be rejected.** Rejection is a successful
outcome — it answers the question. Cost of the revert, measured: body line box −53.7 %, the 285-char
S12 body reflows 8 → ~13 lines.
**Mitigation:** Phase 2 builds S12 before the other eight. Review it before Phase 3.

### R2 — 79 % of screens are constructed — **HIGH**
15 of 19 have no measured source (`M1`, `M2` absent). Their content is built, not transcribed.
**Mitigation:** D3 marks every screen. No constructed screen may be cited as evidence of source.

### R3 — S02 / S03 have no decision behind them, and the cast is unprovable — **MEDIUM**
Both PL06 desk slots are empty; `s03`↔`S03` does not type-match; and the current B02 scenario cast
cannot be established from any available artifact (`A-13`).
**Mitigation:** render as visibly provisional; **role-neutral placeholders**, no named cast.

### R4 — S10 may not be a Card screen — **MEDIUM**
No region data exists for any B02 screen, so the Hotspot gate is not constructible either way.
**Mitigation:** Phase 4 is last and isolated; only 2 screens rebuild if it flips.

### R5 — `K5-DR-032` cannot be verified — **MEDIUM**
Lexical proxies false-pass: `di tapak` appears in both the compliant and the non-compliant text.
**Mitigation:** drafted by judgement, flagged for human review, never asserted as compliant.

### R6 — Nothing has ever been seen rendered — **MEDIUM**
No revision of either deck has been viewed; LibreOffice cannot load them in the build sandbox. Every
measurement to date is of XML.
**Mitigation:** the sample must be rendered in an environment that actually displays it, or it inherits
the same blindness it exists to cure.

### R7 — Sample mistaken for a ratified treatment — **LOW / HIGH IMPACT**
**Mitigation:** constraint 8 (banner on every artefact), constraints 4–7, and the standing status
tokens.

---

## 6. Blockers that the sample does **not** clear

| Blocker | Effect |
|---|---|
| `M1` Tier-1 spec absent | 15 screens stay constructed |
| `M2` `packet_B02.json` absent | no per-screen bindings; `K5-DR-011` and `K5-DR-031` scope stay open |
| `M3` `asset_manifest.json` absent | Hotspot gate not constructible; `A-04` stays conditional |
| `K5-DR-002` K5 locked | **no ratification path exists** — the sample cannot become ratified, only viewed |

**The sample produces a judgement, not a ratification.** Ratification needs the lock lifted, and the
lock needs the per-course source drill.

---

## 7. Modification statement

**Nothing implemented.** No PPTX modified, no compiler patched, no schema altered, no executable
contract issued, no visual candidate created, no canonical ID assigned. K5 remains locked; the live
CAIR decision desk is untouched. This plan is docs-only.
