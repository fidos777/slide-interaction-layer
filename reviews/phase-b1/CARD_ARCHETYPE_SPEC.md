# CARD_ARCHETYPE_SPEC

Phase B1 — measured Card archetype, parameterised derivation, five-card variant arithmetic.
Read-only. No component created. No deck modified. No geometry frozen.

Source artifact for every measurement in this file:
`3f626ac5-BARIAH_REVIEW_8SLIDES.pptx`, SHA-256 `ee4f5479…8bb9e7`.
Stage: `p:sldSz cx=12192000 cy=6858000` → **13.3333 × 7.5 in**. All values in inches, EMU ÷ 914400.

Two loci carry the Card archetype:

- **Card base state** — `ppt/slides/slide3.xml` (`sldId 9019`, Bariah-inserted)
- **Card completion state** — `ppt/slides/slide5.xml` (`sldId 9008`, Bariah-rebuilt in place)

The two are geometrically identical for cards, labels and instruction; `slide5` adds four tick
pictures. `MEASURED_FACT`

---

## 1. Measured inventory

### 1.1 Card panels — `MEASURED_FACT`

`p:sp`, `prstGeom prst="rect"`, name `Rectangle 9`, `bodyPr anchor="t"`, no `lstStyle`.

| Card | `slide3` id | `slide5` id | x | y | w | h | Text purpose |
|---|---:|---:|---:|---:|---:|---:|---|
| C1 | 19 | 4 | 2.3207 | 1.9438 | 3.9350 | 1.9901 | `Visual: Struktur Persisir Air` |
| C2 | 3 | 18 | 6.9631 | 1.9375 | 3.9350 | 1.9901 | `Visual: Struktur Persisir Teduhan` |
| C3 | 4 | 20 | 2.3207 | 4.7532 | 3.9350 | 1.9901 | `Visual: Kemudahan Awam` |
| C4 | 5 | 22 | 6.9631 | 4.7469 | 3.9350 | 1.9901 | `Visual: Water Feature` |

Width and height are **exactly uniform** across all four cards. Only the origins vary.
Card aspect ratio `w/h` = **1.97729**.

C2's text `Visual: Struktur Persisir Teduhan` is a copy-paste residue — the label beneath it reads
`Struktur Teduhan`, and `Persisir` belongs to C1. `PROVISIONAL_IDENTIFIER`, enters Stage 0A.

### 1.2 Labels — `MEASURED_FACT`

`p:sp`, `bodyPr wrap="square" anchor="ctr"` **`noAutofit`**, `pPr algn="ctr"`, `noFill`.
Uniform `w = 3.0323`, `h = 0.4364`.

| Label | `slide3` id | `slide5` id | x | y | Text |
|---|---:|---:|---:|---:|---|
| L1 | 21 | 7 | 2.6748 | 3.9467 | `Struktur Persisir Air` |
| L2 | 22 | 10 | 7.5117 | 3.9467 | `Struktur Teduhan` |
| L3 | 23 | 12 | 2.6748 | 6.7612 | `Kemudahan Awam` |
| L4 | 24 | 14 | 7.5117 | 6.7612 | `Water Feature` |

Label ratio `LABEL_W / CARD_W` = 3.0323 / 3.935 = **0.770597**.

### 1.3 Instruction box — `MEASURED_FACT`

`slide3` id `25`, `slide5` id `16`. `x = 0.7917`, `y = 1.2936`, `w = 6.3367`, `h = 0.4039`.
`bodyPr wrap="square" spAutoFit`, `noFill`, no `lstStyle`, `pPr` empty (left-aligned).
Text: `Klik pada setiap struktur untuk penjelasan lanjut.` — 49 characters, 7 words, 12 runs, no `a:br`.

On the untouched base `slide1` the same box sits at `x = 6.8633`, `y = 5.9817`, same `w = 6.3367`,
with `algn="ctr"` and the wording `Klik pada setiap komponen untuk penjelasan lanjut.`
**Bariah moved it from the right column to the top-left content band and changed one word**
(`komponen` → `struktur`); shape carries `spChg chg="mod" @22:49:05`. `MEASURED_FACT`

### 1.4 Tick marks — `MEASURED_FACT`

`slide5` only. `p:pic`, uniform `0.3937 × 0.3937` (= 10 mm). All four reference the single media part
`ppt/media/image1.svg` (228 bytes, `id="Icons_Checkmark"`, single `<path>`, no fill declared).

| Tick | id | x | y | `picChg` timestamp |
|---|---:|---:|---:|---|
| T1 | 34 | 3.9941 | 2.8285 | 23:08:12.689 |
| T2 | 36 | 8.7338 | 2.8285 | 23:08:19.076 |
| T3 | 38 | 3.9941 | 5.8627 | 23:08:23.588 |
| T4 | 40 | 8.7768 | 5.7767 | 23:08:27.008 |

Four separate `mod ord` records, ~4–7 s apart — each icon was positioned by hand, individually.
This is the forensic origin of every alignment deviation in §2.5. `MEASURED_FACT`

### 1.5 Typography — `MEASURED_FACT`

No run in any card, label or instruction box carries an explicit `sz`, `b`, or `i`. None of these
shapes is a placeholder and none declares a `lstStyle`, so all inherit
`slideMaster1.xml → p:txStyles/p:otherStyle/a:lvl1pPr`:

| Property | Inherited value |
|---|---|
| Size | `sz="1800"` → **18 pt** |
| Typeface | `+mn-lt` → **Ebrima** (`theme1.xml minorFont/latin`) |
| Kerning | `kern="1200"` |
| `marL` / `indent` | `0` / none |
| Bullet | none on cards, labels, instruction |

Layout is `slideLayout7.xml`, `cSld/@name = "Blank"`, `type` unset. `MEASURED_FACT`

### 1.6 Z-order — `MEASURED_FACT`

`slide5` spTree order: title → note panel → title bar → C1 → L1 → L2 → L3 → L4 → instruction →
C2 → C3 → C4 → T1 → T2 → T3 → T4.

**Labels L2–L4 are painted beneath cards C2–C4.** The four tick pictures sit at the very top, which is
why their `picChg` records carry `ord` as well as `mod`. Cards have no fill declared, so nothing is
currently occluded — but the z-order is incoherent and will occlude the moment a card receives a fill.
`PROVISIONAL_IDENTIFIER`, enters Stage 0A.

### 1.7 Navigation position — `MEASURED_FACT`

Neither Card state carries a `Kembali` control. `Kembali` appears **only** on the reveal-child state
`slide4` (`id=11`, `x=6.0028 y=7.1009 w=1.3277 h=0.3366`) — analysed in `STATE_ARCHETYPE_OPTIONS.md`.
The Card parent states are navigation-free by construction; entry is via card click, exit via the
child's `Kembali`.

---

## 2. Derived deviations

### 2.1 Frame — `MEASURED_FACT`

| Quantity | Derivation | Value |
|---|---|---:|
| Horizontal gap | `C2.x − (C1.x + CARD_W)` | 0.7074 |
| Column pitch | `C2.x − C1.x` | 4.6424 |
| Card row pitch (both columns) | `C3.y − C1.y` | 2.8094 |
| Label row pitch | `L3.y − L1.y` | 2.8145 |
| Grid left margin | `C1.x` | 2.3207 |
| Grid right margin | `13.3333 − (C2.x + CARD_W)` | 2.4352 |
| Grid top | `C1.y` | 1.9438 |
| Bottom margin | `7.5 − (L3.y + LABEL_H)` | 0.3024 |
| Deck content band | `Rectangle 9`/`18` on slides 6–8 | x = 0.7917, w = 11.75 |

### 2.2 Label horizontal centring — the dominant defect

Ideal inset: `(CARD_W − LABEL_W) / 2 = (3.935 − 3.0323) / 2 = 0.45135`

| Label | Reviewed x | Derived ideal | Deviation | Label ctr − Card ctr |
|---|---:|---:|---:|---:|
| L1 | 2.6748 | 2.77205 | **−0.09725** | −0.0972 |
| L2 | 7.5117 | 7.41445 | **+0.09725** | +0.0973 |
| L3 | 2.6748 | 2.77205 | **−0.09725** | −0.0972 |
| L4 | 7.5117 | 7.41445 | **+0.09725** | +0.0973 |

The error is **exactly ±0.09725 in, mirror-symmetric about the stage midline**. Column-A labels sit
0.097 in left of their cards; column-B labels sit 0.097 in right of theirs. Consequently:

- label column pitch 4.8369 vs card column pitch 4.6424 → **Δ = +0.1945 = 2 × 0.09725** `MEASURED_FACT`

This is not random drift. It is a single systematic offset: the labels were spaced on their **own**
pitch and then the pair was centred as a block, rather than each label being centred on its card.

### 2.3 Grid centring — `MEASURED_FACT`

Grid block width = `2 × 3.935 + 0.7074` = 8.5774.
Centred origin = `(13.3333 − 8.5774) / 2` = **2.37795**. Reviewed = 2.3207.

**The whole grid sits 0.05725 in left of stage centre** — consistent with the left/right margin
asymmetry (2.3207 vs 2.4352, Δ 0.1145 = 2 × 0.05725).

### 2.4 Row and column alignment variance — `MEASURED_FACT`

| Pair | Reviewed | Ideal | Deviation |
|---|---:|---:|---:|
| C1.y vs C2.y | 1.9438 / 1.9375 | equal | **0.0063** |
| C3.y vs C4.y | 4.7532 / 4.7469 | equal | **0.0063** |
| Card row pitch vs label row pitch | 2.8094 / 2.8145 | equal | **0.0051** |

Column B is 0.0063 in high on **both** rows — a rigid vertical offset of the whole right column, not
per-card jitter.

### 2.5 Card-to-label vertical gap — `MEASURED_FACT`

| Pair | `L.y − (C.y + CARD_H)` | Deviation from mean 0.0185 |
|---|---:|---:|
| C1 → L1 | 0.0128 | −0.0057 |
| C2 → L2 | 0.0191 | +0.0006 |
| C3 → L3 | 0.0179 | −0.0006 |
| C4 → L4 | 0.0242 | +0.0057 |

Spread 0.0114 in. Four different values where one is intended.

### 2.6 Tick offsets — the largest deviations — `MEASURED_FACT`

Ideal centred-on-card offset from card top-left:
`(CARD_W − 0.3937)/2 = 1.77065`, `(CARD_H − 0.3937)/2 = 0.79820`

| Tick | Reviewed offset (dx, dy) | Deviation from ideal | Tick ctr vs **card** ctr | Tick ctr vs **label** ctr-x |
|---|---|---|---|---:|
| T1 | (1.6734, 0.8847) | (−0.09725, +0.08650) | (−0.0972, +0.0865) | **0.0000** |
| T2 | (1.7707, 0.8910) | (+0.00005, +0.09280) | (**0.0000**, +0.0928) | −0.0972 |
| T3 | (1.6734, 1.1095) | (−0.09725, +0.31130) | (−0.0972, +0.3113) | **0.0000** |
| T4 | (1.8137, 1.0298) | (+0.04305, +0.23160) | (+0.0430, +0.2316) | −0.0542 |

Three mutually inconsistent alignment intents in four ticks:

- **T1, T3** are centred on the **label**, inheriting the −0.09725 label error.
- **T2** is centred on the **card**, to within 0.00005 in.
- **T4** is centred on **neither** — 0.0430 from card centre, 0.0542 from label centre.

Vertically, row 1 is coherent (+0.0865, +0.0928 below card centre) while **row 2 is not**
(+0.3113, +0.2316) — a **0.2248 in** discrepancy between rows, and T3/T4 differ from each other by
0.0860 in. T3 and T4 y-values (5.8627, 5.7767) are not even equal, though T1 and T2 are.

**Deviation count: 4 of 4 ticks deviate; 0 conform.** Largest single deviation **0.3113 in**
(≈ 7.9 mm on a 1920 px stage ≈ 45 px).

**Weighting caveat.** `slide5`'s own off-canvas note reads `This is just to show tick icon.` — Bariah
declared the slide demonstrative. The tick deviations are strong evidence of *hand placement*, and must
**not** be read as intended geometry. `SME_AUTHORED_RULE` (the disclaimer) / `MEASURED_FACT` (the numbers).

---

## 3. Parameterised Card specification

Conceptual normalisation only. **Nothing below has been applied to any artifact.**

### 3.1 Parameters

```
STAGE_W      = 13.3333
STAGE_H      = 7.5
BAND_X       = 0.7917                    # deck content band, from Rectangle 9/18
BAND_W       = 11.75

CARD_W                                   # free
CARD_H       = CARD_W / 1.97729          # measured card aspect, locked
GAP_X                                    # free
GAP_Y                                    # free
LABEL_W      = CARD_W * 0.770597         # measured label ratio, locked
LABEL_H      = 0.4364
LABEL_GAP    = 0.0185                    # mean of four measured gaps
TICK_S       = 0.3937
INSTR_H      = 0.4039
GRID_TOP     = 1.9438
BOTTOM_SAFE  = 0.3024
```

### 3.2 Rules

```
R-GRID-X    GRID_X0 = (STAGE_W - (n_cols*CARD_W + (n_cols-1)*GAP_X)) / 2
R-CARD-X    CARD_X[c]  = GRID_X0 + c * (CARD_W + GAP_X)
R-ROW-PITCH ROW_PITCH  = CARD_H + LABEL_GAP + LABEL_H + GAP_Y
R-CARD-Y    CARD_Y[r]  = GRID_TOP + r * ROW_PITCH
R-LABEL-X   LABEL_X[c] = CARD_X[c] + (CARD_W - LABEL_W)/2        # centre on card, never on pitch
R-LABEL-Y   LABEL_Y[r] = CARD_Y[r] + CARD_H + LABEL_GAP
R-TICK      TICK_X[c]  = CARD_X[c] + (CARD_W - TICK_S)/2
            TICK_Y[r]  = CARD_Y[r] + (CARD_H - TICK_S)/2         # single intent for all ticks
R-INSTR     INSTR_W    = n_cols*CARD_W + (n_cols-1)*GAP_X        # match the grid it refers to
            INSTR_X    = GRID_X0
R-FIT       GRID_TOP + n_rows*ROW_PITCH - GAP_Y <= STAGE_H - BOTTOM_SAFE
```

`R-LABEL-X` is the single rule that eliminates the ±0.09725 defect: it derives label x from **its own
card**, so a label can never be spaced on an independent pitch.

### 3.3 Reviewed → derived-ideal reconciliation

Instantiating `CARD_W = 3.935`, `GAP_X = 0.7074`, `GAP_Y = 0.3644`, `n_cols = 2`, `n_rows = 2`:

| Quantity | Reviewed | Derived ideal | Deviation | Rule |
|---|---:|---:|---:|---|
| Grid origin x | 2.3207 | 2.37795 | −0.05725 | `R-GRID-X` |
| C1.x / C3.x | 2.3207 | 2.37795 | −0.05725 | `R-CARD-X` |
| C2.x / C4.x | 6.9631 | 7.02035 | −0.05725 | `R-CARD-X` |
| C2.y | 1.9375 | 1.9438 | −0.0063 | `R-CARD-Y` |
| C4.y | 4.7469 | 4.7532 | −0.0063 | `R-CARD-Y` |
| L1.x / L3.x | 2.6748 | 2.82930 | **−0.15450** | `R-LABEL-X` |
| L2.x / L4.x | 7.5117 | 7.47170 | **+0.04000** | `R-LABEL-X` |
| Label→card gap | 0.0128 / 0.0191 / 0.0179 / 0.0242 | 0.0185 | ±0.0057 | `R-LABEL-Y` |
| Card row pitch | 2.8094 | 2.8094 | 0.0000 | `R-ROW-PITCH` |
| Label row pitch | 2.8145 | 2.8094 | −0.0051 | `R-LABEL-Y` |
| T1 offset | (1.6734, 0.8847) | (1.77065, 0.79820) | (−0.09725, +0.08650) | `R-TICK` |
| T2 offset | (1.7707, 0.8910) | (1.77065, 0.79820) | (+0.00005, +0.09280) | `R-TICK` |
| T3 offset | (1.6734, 1.1095) | (1.77065, 0.79820) | (−0.09725, **+0.31130**) | `R-TICK` |
| T4 offset | (1.8137, 1.0298) | (1.77065, 0.79820) | (+0.04305, **+0.23160**) | `R-TICK` |
| Instruction w | 6.3367 | 8.5774 | **−2.2407** | `R-INSTR` |
| Instruction x | 0.7917 | 2.37795 | **−1.58625** | `R-INSTR` |

**Total: 16 measured quantities deviate from the derived ideal; 1 conforms exactly (card row pitch).**

The instruction row is the largest single deviation in the whole archetype. The instruction box is
aligned to the deck **content band** (0.7917) while the cards it refers to are aligned to a **centred
grid** (2.3207). Two competing alignment systems on one slide. `OPEN_DECISION` — Stage 0A must choose
whether the Card grid adopts the content band or the instruction adopts the grid.

---

## 4. Instruction line wrap analysis

**Finding: the instruction line does not currently wrap, and there is no manual line break.**
`MEASURED_FACT`

Evidence, in order:

1. **No manual break.** The paragraph contains 12 `a:r` runs and **zero** `a:br` elements. Wrapping,
   if any, would be automatic.
2. **The box height proves one rendered line.** `bodyPr` is `spAutoFit`, so PowerPoint wrote back the
   height it actually needed: `h = 0.4039 in = 29.08 pt`. Default insets `tIns = bIns = 45720 EMU`
   = 0.05 in = 3.6 pt each. Available text height = `29.08 − 7.2 = 21.88 pt`. One 18 pt line at 100 %
   spacing occupies ≈ 21.6 pt. Two lines would require ≈ 43.2 pt and `spAutoFit` would have written
   `h ≈ 0.6039`. **The stored height admits exactly one line.**
3. **Paragraph spacing is not a factor.** `pPr` carries no `spcBef`, no `spcAft`, no `lnSpc`.
4. **Font size is not a factor** at the current string — no run overrides the inherited 18 pt, and
   18 pt fits.

**But the margin is negligible.** Line box width = `6.3367 − lIns 0.1 − rIns 0.1` = **6.1367 in**
= 441.8 pt. At 18 pt Ebrima with a mean advance of 0.46–0.50 em (8.28–9.00 pt) for Malay
lowercase-dominant text, capacity is **49–53 characters**. The string is **49 characters**.

**The binding constraint is box width**, and headroom is **0 to 4 characters**. Any of the following
forces a second line and, because `spAutoFit` will grow the box downward from `y = 1.2936`, pushes the
instruction into the 0.2463 in clearance above the card grid at `y = 1.9438`:

- a longer subtopic noun than `struktur` (the base `slide1` wording `komponen` is also 49 chars — no headroom either)
- any deviation from 18 pt upward
- substituting a wider typeface for Ebrima

**Recommended parameter rule** (not applied): bind `INSTR_W` to the grid via `R-INSTR`
(→ 8.5774 in, capacity ≈ 66–72 chars) rather than leaving it at the inherited 6.3367.
`CAIR_RECOMMENDATION`

### 4.1 Related fragility — label boxes are `noAutofit` — `MEASURED_FACT`

Label line box = `3.0323 − 0.2` = 2.8323 in = 203.9 pt → capacity **22–24 characters** at 18 pt.
Longest reviewed label `Struktur Persisir Air` = **21 characters**. Available text height
`0.4364 in − 7.2 pt` = 24.2 pt → one line only.

Because the box is **`noAutofit`**, a label of 25+ characters wraps to two lines needing 43.2 pt in a
24.2 pt box and **overflows silently past the card**. Headroom: 1–3 characters. `PROVISIONAL_IDENTIFIER`

---

## 5. Five-card variant arithmetic

All arithmetic uses the measured reviewed geometry. **No layout was instantiated.**
Reviewed vertical unit `U = CARD_H + LABEL_GAP + LABEL_H` = `1.9901 + 0.0128 + 0.4364` = **2.4393**
(using the as-measured C1→L1 gap). Reviewed `GAP_Y` = 0.3701.

### 5.1 Test — 2 columns × 3 rows at reviewed card size

```
required vertical = 3*U + 2*GAP_Y = 3(2.4393) + 2(0.3701) = 7.3179 + 0.7402 = 8.0581
available (GRID_TOP 1.9438 → 7.5 − BOTTOM_SAFE 0.3024 = 7.1976) = 5.2538
```

| Test | Result |
|---|---|
| Fits available band | **NO** — overflow **+2.8043 in** |
| Fits full 7.5 in canvas, top margin zero | **NO** — overflow **+0.5581 in** |

**Proven: 2 × 3 at reviewed card size cannot fit the 13.3333 × 7.5 canvas.** It exceeds the *entire
stage height* by 0.5581 in even with every margin set to zero. `MEASURED_FACT`

To fit the available band, the unit must shrink to
`U₃ = (5.2538 − 2(0.3701)) / 3 = 1.50453` → `CARD_H = 1.05533`.

| Quantity | Reviewed | Required for 2×3 | Reduction |
|---|---:|---:|---:|
| Card height | 1.9901 | 1.05533 | **46.97 %** |
| Card width (aspect-locked) | 3.9350 | 2.08670 | **46.97 %** |

A 47 % linear reduction — the card visual drops to 28 % of its reviewed area. Not viable for a
visual-bearing card.

### 5.2 Test — 3 columns × 2 rows, `3 + 2` arrangement

Vertically identical to the reviewed two-row layout → **fits without change**. The constraint is
entirely horizontal. `MEASURED_FACT`

**Option 5A — preserve deck content band (0.7917 / 11.75) and reviewed gap 0.7074**

```
3*CARD_W + 2*0.7074 = 11.75  →  CARD_W = 3.44507
```

| Quantity | Value |
|---|---:|
| Card width | 3.44507 |
| **Width reduction vs 3.935** | **12.45 %** |
| Label width (ratio-locked ×0.770597) | 2.65478 |
| Row-1 card x | 0.79170, 4.94410, 9.09650 |
| Row-2 card x (2 centred) | 2.86790, 7.02030 |
| Card height | unchanged 1.9901 |
| Resulting aspect | 1.7311 vs reviewed 1.97729 |

Card height held → aspect changes. Aspect-locking instead gives `CARD_H = 1.74227` (−12.45 %), which
frees 0.4957 in vertically.

**Option 5B — preserve margins, absorb the loss in the gap**

| Card width | Required `GAP_X` | Width reduction |
|---:|---:|---:|
| 3.60000 | 0.4750 | 8.51 % |
| 3.50000 | 0.6250 | 11.05 % |
| 3.44507 | 0.7074 | 12.45 % |

Reducing the gap from 0.7074 to 0.4750 buys back 4 points of card width (12.45 % → 8.51 %).

### 5.3 Test — can any five-card arrangement preserve the exact reviewed card size?

| Arrangement | Required extent | Verdict |
|---|---|---|
| 2 cols × 3 rows | 8.0581 vertical | **NO** — exceeds 7.5 stage height by 0.5581 |
| 3 + 2, within deck band 11.75 | `3(3.935) + 2·GAP_X` = 11.805 + gaps | **NO** — 11.805 alone exceeds the band by 0.055 before any gap; required gap is **−0.0275**, i.e. cards would have to overlap |
| 3 + 2, within full canvas, gap 0.7074 | 13.2198 | **Technically yes** — residual margin **0.0568 in** each side, vs the deck's own 0.7917 band (a 92.8 % margin loss) |
| 5 in a single row | 22.5046 | **NO** — overflow **+9.1713 in** |

**Conclusion: no five-card arrangement preserves the exact reviewed card size within the deck's own
content band.** The single arrangement that preserves it at all (3 + 2 across the full canvas) leaves
0.0568 in of margin — the cards would sit 0.73 in outside the band every other slide respects.
`MEASURED_FACT`

### 5.4 Deviation counts

Deviation = one parameter in §3.1 whose value must change from its reviewed instantiation.

| Option | Arrangement | Deviating parameters | Count | Band respected |
|---|---|---|---:|---|
| **5A** | 3+2, `CARD_W` 3.44507, gap 0.7074 | `CARD_W`, `LABEL_W`, `GRID_X0`/`CARD_X[]`, `TICK_X[]` | **4** | yes |
| **5A′** | 5A + aspect-locked height | 5A + `CARD_H`, `ROW_PITCH`, `TICK_Y[]` | **7** | yes |
| **5B** | 3+2, `CARD_W` 3.60, gap 0.4750 | `CARD_W`, `GAP_X`, `LABEL_W`, `CARD_X[]`, `TICK_X[]` | **5** | yes |
| **5C** | 3+2, exact reviewed card size | `GRID_X0` only — but **band violated by 0.735 in** | **1 + 1 violation** | **no** |
| **5D** | 2×3 scaled to fit | `CARD_W`, `CARD_H`, `LABEL_W`, `ROW_PITCH`, `GAP_Y`, `CARD_X[]`, `CARD_Y[]`, `TICK_X[]`, `TICK_Y[]` | **9** | yes |

Note that all five options additionally require the **row-2 centring** rule
(`GRID_X0_row2 = (STAGE_W − (2·CARD_W + GAP_X))/2`), which the reviewed 2×2 archetype does not
exercise. That rule is new to every option and is not counted above.

### 5.5 Options returned for CAIR selection — `OPEN_DECISION`

| Rank by deviation count | Option | Card width | Reduction | Trade |
|---:|---|---:|---:|---|
| 1 | **5A** | 3.44507 | 12.45 % | fewest deviations; card aspect shifts 1.977 → 1.731 |
| 2 | 5B | 3.60000 | 8.51 % | best card width; gap tightens 0.7074 → 0.4750 |
| 3 | 5A′ | 3.44507 | 12.45 % | aspect preserved; 7 deviations, frees 0.4957 in vertically |
| 4 | 5C | 3.93500 | 0 % | preserves size, **breaches the content band** |
| 5 | 5D | 2.08670 | 46.97 % | 2×3 only; card visual → 28 % of reviewed area |

No recommendation is issued here — five-card selection is a CAIR decision and the task directs that
options be returned, not chosen. The measured constraint that must govern the choice:
**a fifth card cannot be free.** Either card width drops at least 8.5 %, or the inter-card gap drops
33 %, or the deck's own 0.7917 content band is abandoned.

---

## 6. Modification statement

No component was created. No deck was modified. No geometry was frozen. Every value above is a
measurement of, or an arithmetic derivation from,
`3f626ac5-BARIAH_REVIEW_8SLIDES.pptx` @ `ee4f5479…8bb9e7`, at the slide and shape loci cited.
