# STATE_ARCHETYPE_OPTIONS

Phase B1 — measurement of the rebuilt full-slide reveal state, numeric comparison against two
archetypes, and a recommendation held pending decision.

Source artifact: `3f626ac5-BARIAH_REVIEW_8SLIDES.pptx`, SHA-256 `ee4f5479…8bb9e7`.
Reveal-child state under measurement: **`ppt/slides/slide4.xml`**, `sldId 9011`, title `Papan Tanda`.
Stage 13.3333 × 7.5 in. All values in inches.

Lineage (from `BARIAH_REVIEW_INGEST.md §2`): `slide4` is a **base slide edited in place**
(`sldChg chg="addSp delSp modSp mod ord modNotesTx"`, no `add`/`new`), reordered from base position 3
to final position 4. Its off-canvas note panel reads `(PENAMBAHBAIKAN)` /
`Slide 5b (Full-slide reveal)` / `Dipapar penuh selepas learner klik card.` `MEASURED_FACT`

---

## 1. Complete shape and geometry inventory

### 1.1 Reviewed reveal-child state — `slide4.xml` — `MEASURED_FACT`

| z | Shape type | Name | ID | x | y | w | h | Locus |
|---:|---|---|---:|---:|---:|---:|---:|---|
| 2 | `p:sp` placeholder `title` | `Title 1` | 2 | *(inherited)* | | | | on-canvas |
| 3 | `p:sp` rect | `Rectangle 5` | 6 | −3.3500 | 0.0000 | 3.1496 | 7.5000 | **off-canvas** |
| 4 | `p:sp` rect | `TextBox 6` | 7 | 0.6758 | 0.4583 | 12.0075 | 0.6479 | on-canvas |
| 5 | `p:sp` rect | `Rectangle 8` | 8 | 0.8046 | 1.7813 | 11.7371 | 5.2604 | on-canvas |
| 6 | `p:sp` rect | `TextBox 12` | 9 | 0.9046 | 4.4115 | 11.6371 | 2.5244 | on-canvas |
| 7 | `p:sp` rect | `TextBox 19` | 11 | 6.0028 | 7.1009 | 1.3277 | 0.3366 | on-canvas |
| 8 | `p:sp` rect | `Rectangle 3` | 4 | −3.1531 | 4.0845 | 2.7559 | 2.7559 | **off-canvas** |

`Title 1` (id 2) declares no `a:xfrm`; it inherits from
`slideMaster1.xml` → `Title Placeholder 1` at **(0.5833, 0.4583) 12.1667 × 0.5074**. Its text
`Papan Tanda` is therefore rendered twice — once by the inherited placeholder and once by the explicit
title bar `TextBox 6` at (0.6758, 0.4583). `PROVISIONAL_IDENTIFIER` — duplicate title render, enters
Stage 0A.

### 1.2 Per-shape detail — `MEASURED_FACT`

**`id=8` `Rectangle 8` — visual panel.**
`prstGeom prst="rect"`, `bodyPr rtlCol="0" anchor="t"`, no `lstStyle`, no `solidFill` declared.
Text purpose: **visual placeholder**, content `Visual: papan tanda` (4 runs).
Extent: x 0.8046 → **12.5417**; y 1.7813 → **7.0417**.
Width 11.7371 = **88.03 %** of stage width. Left margin 0.8046, right margin 0.7916.
Aspect 2.2312. Change record `spChg chg="mod" spId=8 dt=2026-07-29T22:58:03.540`.

**`id=9` `TextBox 12` — display body.**
`bodyPr wrap="square" spAutoFit`, `noFill`, no `lstStyle`.
Extent: x 0.9046 → **12.5417**; y 4.4115 → **6.9359**.
**Fully nested inside the panel** — the panel spans y 1.7813–7.0417 and the body sits entirely within
it, inset 0.1000 from the panel's left edge and flush with its right edge (both end at 12.5417).
Clearance to panel bottom 0.1058.
8 paragraphs, 2 levels: 5 at level 0 (`marL=285750 indent=-285750`) and 4 at level 1
(`marL=742950 indent=-285750`). Bullet `buChar "•"`, `buFont Arial` throughout.
Typography: no explicit `sz` on any run → inherits `otherStyle/lvl1pPr` **18 pt Ebrima**
(`+mn-lt`, `theme1.xml`). Bold spans present on 8 phrases; **no italic spans**.
Change record `spChg chg="mod" spId=9 dt=2026-07-29T22:57:04.178`.

**`id=11` `TextBox 19` — `Kembali` navigation control.**
`bodyPr wrap="square" anchor="ctr" spAutoFit`, `pPr algn="ctr"`.
Run properties: `sz="1400"` → **14 pt**, `b="1"` → bold, `latin="+mj-lt"` → **Raleway**
(`theme1.xml majorFont`), `lang="en-US"`.
Extent: x 6.0028 → **7.3305**; y 7.1009 → **7.4375**.
Horizontal centre **6.66665**; stage centre 6.66665 — **exact to 5 decimal places.**
Bottom clearance to stage edge **0.0625**.
Carries a 9-level `lstStyle` declaring `latin="Source Sans Pro"`, overridden at run level by `+mj-lt`.
`Source Sans Pro` does not appear in `docProps/app.xml`'s font list — inherited dead styling.
`PROVISIONAL_IDENTIFIER`

**`id=7` `TextBox 6` — main title bar.**
`spAutoFit`, `noFill`, `pPr lnSpc spcPts=3900` → **39 pt line spacing**. Text `Papan Tanda`.
This locus (x 0.6758, y 0.4583, h 0.6479) is shared by **every** slide in the deck — `slide1`,
`slide3`–`slide6` at w 12.0075; `slide7`, `slide8` at w 12.1367.

**Off-canvas shapes** (`id=6`, `id=4`) are production notes; neither renders to a learner.
`id=4` (`Rectangle 3`) carries `spChg chg="add mod" dt=23:06:09.402` — Bariah-added, text
`Rujukan modul: imej K5PL06T03-B02-IMG-01, ms 237. Paparkan sebagai visual utama skrin penuh.`

### 1.3 Rumusan reference geometry — `slide7.xml` (untouched base) and `slide8.xml` — `MEASURED_FACT`

| Shape | Slide | x | y | w | h |
|---|---|---:|---:|---:|---:|
| `Rectangle 18` (panel) | `slide7` | 0.7917 | 1.7812 | 11.7292 | 5.2604 |
| `Rectangle 18` (panel) | `slide8` | 0.7917 | 1.7812 | 11.7292 | 5.2604 |
| `TextBox 24` (body) | `slide7` | 0.8125 | 4.4300 | 11.7083 | 2.5244 |
| `TextBox 24` (body) | `slide8` | 0.8125 | 4.7011 | 11.7292 | 2.2215 |
| `TextBox 6` (title bar) | both | 0.6758 | 0.4583 | 12.1367 | 0.6479 |

Neither Rumusan slide carries a `Kembali` control. Both carry a **bold lead paragraph** as the first
paragraph of the body box (`rPr b="1"`), functioning as an inline heading.

---

## 2. Numeric comparison

### 2.1 Option A — canonical split-STATE archetype

*Visual panel left · heading and body right · canonical `Kembali`.*

The reviewed deck's nearest realisation of this form is the untouched base `slide1.xml` (`sldId 9003`),
which is a **parent** state, not a reveal-child — but it is the only split geometry in the package and
supplies the numeric reference. `MEASURED_FACT`

| Element | `slide1` measured | Reviewed `slide4` | Δ |
|---|---|---|---|
| Visual panel | (0.8046, 1.7813) 5.8621 × 5.2604 | (0.8046, 1.7813) **11.7371** × 5.2604 | **w +5.8750** |
| Panel width as % of stage | 43.97 % | **88.03 %** | +44.06 pp |
| Text column x | 6.8633 | 0.9046 | −5.9587 |
| Text column w | 6.1867 | 11.6371 | +5.4504 |
| Body/visual relationship | **side-by-side, non-overlapping** (panel ends 6.6667; text begins 6.8633; gutter 0.1966) | **nested — body wholly inside panel** | topological change |
| `Kembali` | absent (parent state) | present, centred | — |

Fitting Option A to the reveal-child would require: panel width 5.8621 (−50.06 %), body relocated to
x 6.8633 w 6.1867 (−46.83 % width), a body heading introduced in the right column, and `Kembali`
repositioned within or beneath the right column. **Deviation count vs reviewed: 5 parameters.**

Capacity consequence — body line box narrows from
`11.6371 − 0.2 − 0.3125 = 11.1246 in` to `6.1867 − 0.2 − 0.3125 = 5.6742 in`, a **49.0 % loss**.
At 18 pt the level-0 bullet capacity falls from ≈ 89–97 to ≈ 45–49 characters per line. The reviewed
body's 8 paragraphs (longest 77 chars) would go from 8 rendered lines to **13**, requiring
≈ 281 pt = 3.90 in of text height against the 5.2604 in panel. It fits, but the box must grow 54 %
and the visual panel loses half its width. `MEASURED_FACT`

### 2.2 Option B — full-width panel archetype

*Full-width panel · nested or structured display body · canonical `Kembali` · visually closer to the
canonical Rumusan geometry.*

This **is** the reviewed geometry. The comparison that matters is therefore against Rumusan:

| Quantity | Reviewed `slide4` | Rumusan `slide7` | **Δ** |
|---|---:|---:|---:|
| Panel x | 0.8046 | 0.7917 | **+0.0129** |
| Panel y | 1.7813 | 1.7812 | **+0.0001** |
| Panel w | 11.7371 | 11.7292 | **+0.0079** |
| Panel h | 5.2604 | 5.2604 | **0.0000** |
| Body x | 0.9046 | 0.8125 | +0.0921 |
| Body y | 4.4115 | 4.4300 | −0.0185 |
| Body w | 11.6371 | 11.7083 | −0.0712 |
| Body h | 2.5244 | 2.5244 | **0.0000** |

**Maximum panel deviation: 0.0129 in.** On a 1920 × 1080 render that is **1.86 px**. Panel height is
identical to four decimal places; body height is identical to four decimal places.

### 2.3 The four determinations

**Q1 — Does any canonical reveal-child use the full-width form?**

`NOT_DETERMINABLE`. The canonical archetype set — `SB_K4PL3T2_v1.2.pptx` and the 19-slide K5 B02
Tier-1 specification — is **not present in this session** (see `BARIAH_REVIEW_INGEST.md §1.1`). No
statement about canonical practice can be made from the reviewed deck alone.

What the reviewed evidence *does* show, and its exact scope: the package contains **one** reveal-child
state (`slide4`), and it uses the full-width form. That is 1 of 1, from a sample of one, on a slide
whose own note declares it a `(PENAMBAHBAIKAN)` proposal. It is **not** evidence of canonical practice.
`MEASURED_FACT` (the count) / `NOT_DETERMINABLE` (the canonical question).

**Q2 — Does the reviewed state contain a separate body-heading box?**

**No.** `MEASURED_FACT`

`slide4` has seven shapes; five are accounted for as title placeholder, title bar, panel, body,
`Kembali`, and two are off-canvas notes. There is no heading shape between the title bar
(ends y 1.1062) and the body (begins y 4.4115) — a 3.3053 in vertical span occupied solely by the
visual panel.

Nor is there an inline heading. The body's first paragraph is an ordinary level-0 bullet
(`buChar "•"`, no `b="1"`): `Elemen penting untuk navigasi, maklumat, dan keselamatan dalam ruang
landskap`. Contrast Rumusan `slide7`/`slide8`, whose first body paragraph carries `rPr b="1"` and no
bullet — a genuine inline heading. **The reveal-child has strictly less heading structure than Rumusan.**

**Q3 — Does it rely on the main title bar?**

**Yes, exclusively.** `MEASURED_FACT`

The only heading-level text on the slide is `Papan Tanda`, carried by `TextBox 6` at the shared
title-bar locus (0.6758, 0.4583) — the identical locus used by all eight slides — and duplicated by
the inherited title placeholder. With no body heading (Q2), the title bar is the sole carrier of
subject identity for the revealed content.

**Q4 — Does `Kembali` sit below, inside, or overlapping the panel?**

**Below, with clear separation.** `MEASURED_FACT`

```
panel   (id=8)  y 1.7813 → 7.0417
Kembali (id=11) y 7.1009 → 7.4375
                gap = 7.1009 − 7.0417 = +0.0592   (no overlap)
                stage bottom clearance = 7.5 − 7.4375 = 0.0625
```

Not inside. Not overlapping. Below, by 0.0592 in — and only 0.0625 in from the stage edge.
Horizontally exact-centred (6.66665 vs stage 6.66665).

The 0.0592 in gap and 0.0625 in bottom clearance are both under 1/16 in ≈ 9 px at 1920 wide. The
control is correctly placed but has **no vertical tolerance**: any growth of the panel, or any
`spAutoFit` reflow of `Kembali` to two lines, collides with the stage edge. `PROVISIONAL_IDENTIFIER`

**Q5 — Can the visual hierarchy still be distinguished from Rumusan?**

**Not by geometry.** `MEASURED_FACT`

Panel deviations are ≤ 0.0129 in (1.86 px at 1920). Panel height and body height are identical to four
decimal places. A learner comparing the two screens sees the same frame in the same place at the same
size.

Three non-geometric signals remain, and each is weak:

| Signal | `slide4` reveal-child | Rumusan | Discriminating? |
|---|---|---|---|
| Inline bold lead paragraph | **absent** | present | Yes — but it is *Rumusan* that carries the extra structure, so the reveal-child reads as a **degraded Rumusan**, not as a distinct type |
| `Kembali` control | present | absent | Yes — but it is 14 pt, 1.3277 in wide, and 0.0592 in below the panel: **0.45 % of stage area** |
| Title bar text | `Papan Tanda` | `Rumusan` | Yes — but this is content, not archetype |

The one structural affordance that separates them is a 14 pt word occupying under half a percent of
the stage. **Geometrically, the reviewed reveal-child and Rumusan are the same archetype.**

---

## 3. Both options, side by side

| Criterion | **Option A** — split-STATE | **Option B** — full-width |
|---|---|---|
| Panel | 5.8621 × 5.2604 (43.97 % width), left | 11.7371 × 5.2604 (88.03 % width) |
| Body | right column, x 6.8633 w 6.1867, side-by-side | nested inside panel, x 0.9046 w 11.6371 |
| Body line capacity @ 18 pt | 5.6742 in ≈ 45–49 ch/line | 11.1246 in ≈ 89–97 ch/line |
| Reviewed body reflow | 8 → **13** lines; box must grow 54 % | 8 lines as measured, exactly fits |
| Body heading | required (right column needs its own head) | absent; relies on title bar |
| `Kembali` | must be repositioned | centred, below panel, exact-centred |
| Distinguishable from Rumusan | **Yes** — 44 pp panel-width difference | **No** — max Δ 0.0129 in |
| Deviation count vs reviewed | **5 parameters** | **0 parameters** |
| Visual : text area balance | 44 : 56 | 88 : nested |
| Matches reviewed evidence | no | yes (it *is* the reviewed evidence) |
| Matches canonical practice | `NOT_DETERMINABLE` | `NOT_DETERMINABLE` |

The trade is clean and it is not close on either axis. **Option B costs nothing to adopt and is already
built, but it collapses the visual distinction between a reveal-child and a summary screen.**
**Option A restores that distinction at the cost of five parameter changes and half the body's line
width.**

---

## 4. Recommendation

# `CAIR_RECOMMENDATION_PENDING_DECISION`

**Recommended: Option A — canonical split-STATE archetype, with the reveal-child retaining a
full-width panel only where a single covering source image is bound.**

Reasoning, in order of weight:

1. **Q5 is the decisive finding.** A reveal-child and a section summary that share a frame to within
   1.86 px are not two archetypes; they are one archetype used twice. The only surviving discriminator
   is a 14 pt `Kembali` occupying 0.45 % of the stage — and it sits *outside* the panel, where a
   learner scanning the content region will not encounter it. Option B does not fail on aesthetics; it
   fails on **state legibility**.

2. **The degradation runs the wrong way.** Rumusan carries a bold inline lead; the reveal-child does
   not (Q2). The screen with *less* structure is the one revealed on demand after a deliberate learner
   action. Option A's right column forces a body heading back in.

3. **Option B's zero deviation count is not evidence of correctness.** It scores zero because it is the
   measured state — the metric is circular. Its real cost surfaces in the Q4 tolerances: 0.0592 in
   panel gap and 0.0625 in stage clearance, both under 9 px, with `spAutoFit` live on the `Kembali`
   box. That is a layout with no slack.

4. **Option A's capacity cost is real and must be stated.** Body line width falls 49.0 %, and the
   reviewed 8-paragraph body reflows to ~13 lines needing ≈ 3.90 in against a 5.2604 in panel. It fits,
   but with 26 % headroom rather than the present comfortable margin. Any reveal-child whose display
   body exceeds ~14 lines at 18 pt will not fit Option A and must either drop to Option B or reduce
   display load — and `DISPLAY_BUDGET_REDERIVED.md` establishes that display load *should* be reducible,
   because full propositional coverage is carried in the VO, not on the canvas.

5. **The hedge is deliberate.** Where a screen binds one covering source image with no discrete
   sub-regions — the `Papan Tanda` case, and `slide6`'s Hotspot form — a 43.97 % panel may crop the
   evidence below usefulness. The recommendation is therefore conditional on binding, not absolute.

**This recommendation is not implemented and must not be treated as decided.** It rests on a sample of
one reveal-child, on a slide Bariah herself marked `(PENAMBAHBAIKAN)`, and Q1 is `NOT_DETERMINABLE` —
canonical practice is unknown because the canonical archetype set is absent from this session.

**Blocking input required before this decision can close:** the canonical archetype set
(`SB_K4PL3T2_v1.2.pptx` and the 19-slide K5 B02 Tier-1 specification). If any canonical reveal-child
already uses the full-width form, Q1 resolves in Option B's favour and reasoning items 1–3 must be
re-weighed against established practice rather than against Rumusan alone.

---

## 5. Modification statement

Nothing was implemented. No deck was modified, no geometry frozen, no archetype selected. Every value
is a measurement of, or derivation from, `3f626ac5-BARIAH_REVIEW_8SLIDES.pptx` @ `ee4f5479…8bb9e7` at
the slide and shape loci cited.
