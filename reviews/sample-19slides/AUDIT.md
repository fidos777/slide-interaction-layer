# AUDIT — 19-slide visual treatment sample v0.2

```
K5PL06T03B02_19SLIDE_VISUAL_TREATMENT_SAMPLE_v0_2.pptx
84,756 bytes
sha256  8d93e2ce861624f0ff61271538900189c707ac6ec95dd1b1e6db0191646a982b
md5     16bc57ac60be6c4b4f4540d12ccc0eb5
19 slides · 1 master · 7 layouts · 19 notes slides
```

v0.1 (`5e35198a…3ac7b5bf`, 84,253 B) is **preserved unchanged** and re-hashed after the v0.2 build.

## 0. v0.2 — three bounded fixes

**9 / 9 package checks · 33 / 33 rule checks — all executed.**

### Fix 1 — S17 `BBQ pit` cannot split across lines

The wrap risk was real, not cosmetic. Bullet 3 is **92 characters** against a line-box capacity of
**90–98** at 18 pt, and the break lands exactly on the final token:

```
…Drinking Fountain dan BBQ pit
                       ^^^^^^^ break falls here
```

Fixed by a **non-breaking space** (U+00A0) between `BBQ` and `pit` in the display run.

| check | result |
|---|---|
| display bullet (`TextBox 24`) uses `BBQ`+U+00A0+`pit` | **PASS** |
| off-canvas note (`Rectangle 8`) keeps the normal space — it documents the *source form* | **PASS** |
| exactly two occurrences on S17, no stray third | **PASS** |
| displayed wording unchanged — reads `Drinking Fountain dan BBQ pit` | **PASS** |
| `BBQ pit` still italic | **PASS** |
| full-width Rumusan geometry preserved — panel 11.7292 | **PASS** |

**Stated plainly:** the rendered wording is identical; the *codepoint* is not. A byte-exact
source-fidelity check will see U+00A0 where the source has U+0020. This is a typographic control, not
a wording change, and the off-canvas note deliberately retains the plain-space form so the source
reading is still recorded on the slide.

### Fix 2 — S10 / S16 pending marker reduced to a chip

| | v0.1 | **v0.2** |
|---|---|---|
| Form | full-width dashed banner | **compact chip**, `roundRect` |
| Geometry | 0.7917, 1.2936 · **11.75 × 0.4039** | 0.7917, 1.3436 · **2.95 × 0.30** |
| Text | one 18 pt sentence | `SOURCE PENDING · arahan`, 11 pt bold |
| Explanation | on canvas | **moved to the off-canvas note, in full** |

Canvas footprint drops from 4.75 in² to 0.89 in² — **81 % less**. The Card grid is now visually
dominant, and the screen still declares its own incompleteness.

| check | result |
|---|---|
| pending marker is a chip ≤ 3.0 in wide on both screens | **PASS** |
| chip clears the card grid (bottom 1.6436 < card top 1.9438) | **PASS** |
| no full-width pending banner remains | **PASS** |
| S10/S16 still carry `SOURCE PENDING` on canvas | **PASS** |
| full explanation preserved off-canvas | **PASS** |

### Fix 3 — five-card direction recorded

Written into the off-canvas production note of **both** S10 and S16:

```
FIVE_CARD_SAMPLE_DIRECTION = OPTION_5B
  CARD_W = 3.60   GAP_X = 0.475
  Status: FIRDAUS_SAMPLE_DIRECTION, NOT CANONICAL.
```

| check | result |
|---|---|
| `FIVE_CARD_SAMPLE_DIRECTION = OPTION_5B` on S10 and S16 | **PASS** |
| `CARD_W = 3.60` and `GAP_X = 0.475` recorded | **PASS** |
| `FIRDAUS_SAMPLE_DIRECTION, NOT CANONICAL` recorded | **PASS** |

This is a **sample direction from Firdaus**, not a CAIR ratification and not canonical geometry.
`K5-DR-061` remains `OPEN`, and S10's Card/Hotspot classification remains `NOT_DETERMINABLE`.

### Complete diff v0.1 → v0.2 — five elements, nothing else

| Screen | Element | Change |
|---|---|---|
| S10 | `Rectangle 8` (off-canvas note) | text — explanation + direction added |
| S10 | id 25 → chip | geometry 11.75 × 0.4039 → 2.95 × 0.30; text |
| S16 | `Rectangle 8` (off-canvas note) | text — explanation + direction added |
| S16 | id 25 → chip | geometry 11.75 × 0.4039 → 2.95 × 0.30; text |
| S17 | `TextBox 24` | **NBSP only** — no other character differs |

**Verified unchanged:** card positions · tick positions · split-STATE geometry (5.8621 × 5.1387 on all
9) · navigation strip (0.58, clearance 0.10/0.10 on all 9) · S12 content · slide count (19) · source
status (4/11/4) · **all 19 VO bodies** · interaction logic. No shape was added or removed on any slide.

### One check was wrong, not the artifact

The first v0.2 run reported 30/31 with `"S17 no breakable 'BBQ pit' remains"` failing. The assertion
was **shape-blind** — it treated the off-canvas note's legitimate plain-space occurrence as a defect,
and its comparison constant was corrupted passing U+00A0 through the build shell. Re-specified as three
shape-scoped codepoint assertions, all passing. **The artifact never changed.**

---

```
VISUAL_TREATMENT_SAMPLE_ONLY · SOURCE_INCOMPLETE
NOT_CAIR_RATIFIED · NOT_PRODUCTION_AUTHORISED · NOT_A_STORYBOARD
```

**9 / 9 package checks · 25 / 25 rule checks — all executed, none hand-asserted.**

---

## 1. Package integrity — 9 / 9 PASS

| check | result |
|---|---|
| opens as a Presentation | **PASS** |
| slide count == 19 | **PASS** |
| notes slides == 19 | **PASS** |
| duplicate shape IDs | 0 — **PASS** |
| iSpring / `changesInfo` / `revisionInfo` / media residue | none — **PASS** |
| dangling relationships | 0 — **PASS** |
| orphan content-type overrides | 0 — **PASS** |
| parts lacking a content type | 0 — **PASS** |
| duplicate zip entries | 0 — **PASS** |

## 2. Propagation of the accepted v0.3 geometry — 12 / 12 PASS

| check | result |
|---|---|
| exactly one `Kembali` on each of the 9 detail screens | **PASS** |
| **no** `Kembali` on any non-detail screen | **PASS** |
| detail panel width **5.8621** on all 9 | **PASS** |
| detail panel height **5.1387** on all 9 | **PASS** |
| reserved navigation strip **0.58 in** on all 9 | **PASS** |
| clearance **0.10 above** `Kembali` on all 9 | **PASS** |
| clearance **0.10 below** `Kembali` on all 9 | **PASS** |
| `Kembali` strictly below panel — `FULL_SLIDE`, not `POPUP` | **PASS** |
| S04 card geometry preserved — 4 cards, 3.935 × 1.9901 | **PASS** |
| S04 label centring exact on all four | **PASS** |
| S10 / S16 five cards, 3 + 2, `CARD_W` 3.60 | **PASS** |
| S09 four ticks · S16 five ticks | **PASS** |

Detail screens carrying the propagated split-STATE: **S05, S06, S07, S08, S11, S12, S13, S14, S15** —
nine, exactly as specified.

## 3. Treatment rules — 9 / 9 PASS

| check | result |
|---|---|
| no `^Hilmi:` in any of the 19 VO bodies | **PASS** |
| S17 structural labels suppressed (case-insensitive, prefix match) | **PASS** |
| S17 no `\banda\b` in display or VO | **PASS** |
| S17 `Kontraktor` present | **PASS** |
| S12 locator `IMG-05` / ms 243 | **PASS** |
| S12 no `IMG-01` and no `237` | **PASS** |
| italic set exactly `{Water Feature, Drinking Fountain, BBQ pit}` | **PASS** |
| source form `BBQ pit` present, `BBQ Pit` absent deck-wide | **PASS** |
| no scenario cast names deck-wide | **PASS** |

## 4. Source-honesty rules — 4 / 4 PASS

| check | result |
|---|---|
| every `PARTIAL` / `MISSING` screen carries `SOURCE PENDING` on canvas | **PASS** (15/15) |
| no `SOURCE PENDING` on any `VERIFIED` screen | **PASS** (4/4) |
| no invented VO — every non-verified screen's notes read `[VO SOURCE PENDING …]` | **PASS** |
| S18 carries no quiz item, option, answer key or routing | **PASS** |

## 5. Per-screen record

| # | Screen | Status | Shapes | `SOURCE PENDING` | `Kembali` (above / below) |
|---|---|---|---:|---|---|
| S01 | TAJUK | PARTIAL | 6 | ✅ | — |
| S02 | DIALOG | MISSING | 7 | ✅ | — |
| S03 | OVERVIEW | MISSING | 8 | ✅ | — |
| S04 | CR_BASE | **VERIFIED** | 12 | — | — |
| S05 | FULL | PARTIAL | 7 | ✅ | 0.10 / 0.10 |
| S06 | FULL | PARTIAL | 7 | ✅ | 0.10 / 0.10 |
| S07 | FULL | PARTIAL | 7 | ✅ | 0.10 / 0.10 |
| S08 | FULL | PARTIAL | 7 | ✅ | 0.10 / 0.10 |
| S09 | TICK | **VERIFIED** | 16 | — | — |
| S10 | CR_BASE | PARTIAL | 14 | ✅ | — |
| S11 | FULL | PARTIAL | 7 | ✅ | 0.10 / 0.10 |
| S12 | FULL | **VERIFIED** | 7 | — | 0.10 / 0.10 |
| S13 | FULL | PARTIAL | 7 | ✅ | 0.10 / 0.10 |
| S14 | FULL | PARTIAL | 7 | ✅ | 0.10 / 0.10 |
| S15 | FULL | PARTIAL | 7 | ✅ | 0.10 / 0.10 |
| S16 | TICK | PARTIAL | 19 | ✅ | — |
| S17 | RUMUSAN | **VERIFIED** | 6 | — | — |
| S18 | KUIZ | MISSING | 4 | ✅ | — |
| S19 | TAMAT | MISSING | 4 | ✅ | — |

## 6. Geometry actually applied

```
split-STATE (9 screens)
  panel        0.8046, 1.7813 · 5.8621 × 5.1387   → bottom 6.92
  heading box  6.8667, 1.8291 · 5.6621 × 0.5068
  body         6.8667, 2.5594 · 5.6621 × 3.8708
  R-NAVSTRIP   6.92 → 7.5 = 0.58 reserved
  Kembali      5.8917, 7.02 · 1.55 × 0.38 @ 16 pt bold · centre 6.6667 · 0.10 / 0.10

4-card (S04, S09)
  CARD 3.935 × 1.9901 · GAP_X 0.7074 · GAP_Y 0.25 · ROW_PITCH 2.7586
  LABEL 3.6202 × 0.50 @ 20 pt · LABEL_GAP 0.0185 · R-LABEL-X exact
  INSTR grid-width 8.5774 at x 2.3779

5-card 3+2 (S10, S16) — option 5B
  CARD 3.60 × 1.9901 · GAP_X 0.4750 · band 0.7917 / 11.75
  row 1: x 0.7917 / 4.8667 / 8.9417   row 2 centred: x 2.8292 / 6.9042
  LABEL 3.312 × 0.50 @ 20 pt · same ROW_PITCH as the 4-card family

ticks (S09 ×4, S16 ×5)
  R-TICK: CARD + (CARD_W − 0.3937)/2, (CARD_H − 0.3937)/2 — one alignment intent
```

## 7. Two build decisions worth flagging

**Ticks are native geometry, not the probe's SVG.** The probe's tick is an `a:blip` carrying only an
`asvg:svgBlip` with **no raster fallback**, and the probe's own checklist flags "ticks render as the
checkmark, not a missing-image box" as unverified. Reusing it would inherit an unverified render risk
into 9 tick instances. The checkmark is redrawn as `a:custGeom` from the same path data — no media
part, no fallback problem, theme-independent. Colour green per the LOCKED `visited-tick` behaviour.

**S10/S16 instruction line is marked pending, not copied.** S04's `Klik pada setiap struktur…` is
verified for S04. Reusing it on a *Perabot Taman* screen would be inventing display text. The zone
renders as `SOURCE PENDING`, which is less tidy and more honest.

## 8. Not proven by this sample

The base → child → base loop is not wired — this is a static visual sample, not an interactive build.
No image is bound because none exists. 15 of 19 screens have no verified content. S10's Card/Hotspot
classification is still `NOT_DETERMINABLE`; if it resolves to Hotspot, S10 and S16 are rebuilt.
And **nothing has been seen rendered** — LibreOffice cannot load these decks in the sandbox, so every
figure here is a measurement of XML. `LOCAL_19SLIDE_VISUAL_REVIEW_CHECKLIST.md` is the gate that closes
that.

## 9. Not asserted

No source completeness. No CAIR ratification. No production authorisation. No manifest, digest pin,
baseline or freeze. No canonical decision ID. K5 remains locked; the live CAIR decision desk was not
altered; no compiler, database or authority schema was patched. Both evidence packages re-hashed
unchanged: `ee4f5479…8bb9e7`, `24dcaa04…1d471c`.
