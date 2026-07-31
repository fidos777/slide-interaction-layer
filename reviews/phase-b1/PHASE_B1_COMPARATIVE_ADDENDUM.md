# PHASE_B1_COMPARATIVE_ADDENDUM

Comparative evidence closure for Phase B1. Read-only.
This document **supplements** the five existing Phase B1 documents; none of them has been rewritten.
Where a prior finding is corrected, narrowed or upgraded, §8 states it explicitly with the locus.

---

## 0. Custody of the newly attached artifacts

| Artifact | Bytes | SHA-256 | Verdict |
|---|---:|---|---|
| `…_TREATMENT_PROBE_4SLIDES_NOT_A_STORYBOARD1.pptx` | **55,269** | `24dcaa049130d067de2ce95704cae99bd5a49c0b2c8d99819604a8dbac1d471c` | **probe v0.1** — exact match to the authoritative value |
| `TREATMENT_PROBE_README.md` | 2,868 | `06b0ef5d…f000c` | v0.2 documentation |
| `TREATMENT_PROBE_MAPPING.md` | 2,638 | `3bbfe6b3…53a4` | v0.2 documentation |
| `TREATMENT_PROBE_VALIDATION.md` | 3,408 | `44d102db…1c2c` | v0.2 documentation |
| `LOCAL_REVIEW_CHECKLIST.md` | 3,075 | `d2c92e63…37b9` | v0.2 documentation |
| `3f626ac5-BARIAH_REVIEW_8SLIDES.pptx` | 68,710 | `ee4f5479…8bb9e7` | **unchanged** — re-verified |

**The attached PPTX is probe v0.1, not v0.2.** Confirmed three ways: hash equality with `24dcaa04…`;
byte size 55,269 (v0.2 is 55,271); and package part names `ppt/slides/slide4|9|12|17.xml`, which
`TREATMENT_PROBE_MAPPING.md` declares as the v0.1 naming (v0.2 renumbers to `slide1|2|3|4.xml`).
`MEASURED_FACT`

**Probe v0.2 is not attached.** It is present only as documentation: its hash, its size, and a precise
account of its single delta. §2 shows this is nonetheless sufficient to close the base-revision
question, because the documented delta is exactly the discriminator needed.

### 0.1 The documentation authenticates itself against the file — `MEASURED_FACT`

Every checkable value in `TREATMENT_PROBE_VALIDATION.md` was independently re-measured on the attached
v0.1 and matches:

| Validation claim | Re-measured on v0.1 | Match |
|---|---|---|
| slide count 4 | 4 | ✅ |
| package entries 49 | 49 | ✅ |
| S04 notes 481 ch `bdd9084a6dda` | 481 ch, sha `bdd9084a6dda…` | ✅ |
| S12 notes 449 ch `ba0a525663eb` | 449 ch, sha `ba0a525663eb…` | ✅ |
| S09 notes 0 ch `e3b0c44298fc` | **0 ch (empty)**, sha `e3b0c44298fc…` | ✅ |
| S17 notes 586 ch `9d2694129582` | 586 ch, sha `9d2694129582…` | ✅ |
| S12 punctuation `{',':7, '.':4}` | 7 commas, 4 full stops | ✅ |
| S12 50 tokens | 50 words | ✅ |
| S12 body bbox `6.87,2.56 5.66×3.87` | `6.8667, 2.5594, 5.6621 × 3.8708` | ✅ |
| `Kembali` at `6.00, 7.10` | `6.0028, 7.1009` | ✅ |
| S12 four bullets, `buChar '•'`, `buFont Arial` | confirmed | ✅ |
| v0.1 p2–p4 lack `marL`/`indent`/`buFont` | confirmed — `<a:pPr><a:buChar char="•"/></a:pPr>` | ✅ |
| tick x 11.77, y 3.01/3.78/4.54/5.31 | exact | ✅ |
| S17 layout `Title and Content`; others `Blank` | `slideLayout6` = `Title and Content`, `slideLayout7` = `Blank` | ✅ |

14 of 14 independently checkable claims verified. The documentation set is reliable and its statements
about v0.2 are treated as trustworthy evidence below, marked `DOCUMENTED_NOT_MEASURED` where they
cannot be re-measured.

---

## 1. The reviewed deck against probe v0.1 — complete correspondence

### 1.1 Probe slide order — `MEASURED_FACT`

`ppt/presentation.xml` of probe v0.1:

```
<p:sldIdLst><p:sldId id="9003" .../><p:sldId id="9011" .../><p:sldId id="9008" .../><p:sldId id="9016" .../></p:sldIdLst>
```

Probe order is **9003, 9011, 9008, 9016** = S04 → S12 → S09 → S17, matching
`TREATMENT_PROBE_MAPPING.md` exactly. Stage `12192000 × 6858000` — identical to the reviewed deck.

### 1.2 The 4-to-8 mapping, now closed with source screen identity — `MEASURED_FACT`

| Reviewed part | `sldId` | Probe part | Screen | Canonical archetype | Bariah's action |
|---|---:|---|---|---|---|
| `slide1.xml` | 9003 | `slide4.xml` | **S04 CR_BASE** | canon slide 10 — vertical-menu base | **none** |
| `slide2.xml` | 9020 | — | — | — | created (`new`) |
| `slide3.xml` | 9019 | — | — | — | inserted (`add`) |
| `slide4.xml` | 9011 | `slide12.xml` | **S12 FULL** | canon slide 6 — **split-STATE child** | edited in place → full-width |
| `slide5.xml` | 9008 | `slide9.xml` | **S09 TICK** | canon slide 15 — vertical-menu completion | rebuilt in place → card grid |
| `slide6.xml` | 9021 | — | — | — | inserted (`add`) |
| `slide7.xml` | 9016 | `slide17.xml` | **S17 RUMUSAN** | *none — untouched control* | **none** |
| `slide8.xml` | 9017 | — | — | — | inserted (`add`), duplicate of `slide7` |
| — | 9018 | — | — | — | created then discarded |

All four `sldId`s carry through unchanged from probe to reviewed deck. Every `changesInfo` record
reconciles against the observed probe→reviewed delta — see §1.4.

### 1.3 The 19-screen packet skeleton is recoverable from the probe — `MEASURED_FACT`

Probe `docProps/app.xml` was **not** rewritten by `python-pptx` and still carries the source
specification's title vector: `<Slides>19</Slides>`, `<Notes>19</Notes>`, 19 titles.

| # | Title | Role | Parent |
|---:|---|---|---|
| S01 | `S01 TAJUK` | title | — |
| S02 | `S02 DIALOG` | dialogue | — |
| S03 | `S03 OVERVIEW` | overview | — |
| **S04** | `S04 CR_BASE` | **Click-&-Reveal base** | — |
| S05–S08 | `S05/06/07/08 FULL` | **4 reveal children** | S04 |
| **S09** | `S09 TICK` | completion state | S04 |
| **S10** | `S10 CR_BASE` | **Click-&-Reveal base** | — |
| S11–S15 | `S11/12/13/14/15 FULL` | **5 reveal children** | S10 |
| **S16** | `S16 TICK` | completion state | S10 |
| S17 | `S17 RUMUSAN` | summary | — |
| S18 | `S18 KUIZ` | quiz | — |
| S19 | `S19 TAMAT` | end | — |

Two Click-&-Reveal groups: **S04 with 4 children, S10 with 5 children.** Cross-referencing the Rumusan
inventory measured on S17 — `struktur taman` = Struktur Persisir Air, Struktur Teduhan, Kemudahan Awam,
Water Feature (**4**); `perabot taman` = Kerusi Taman, Papan Tanda, Tong Sampah, Drinking Fountain,
BBQ pit (**5**) — and confirming that S12's title placeholder reads **`Perabot Taman`** with body
content `Papan Tanda`:

- **S04 = Struktur Taman**, children S05–S08 = the four structures.
- **S10 = Perabot Taman**, children S11–S15 = the five furniture items; **S12 = Papan Tanda**, the
  second of five.

This is a **reconstruction from measured evidence, not a packet read** — `packet_B02.json` remains
absent. It is labelled `PROVISIONAL_IDENTIFIER` at the per-child level and `MEASURED_FACT` for the
screen roles and child counts, which come directly from `app.xml` and the S17 inventory.

### 1.4 Every `changesInfo` record reconciles — `MEASURED_FACT`

**`slide4` (9011) ← probe S12.** Six shape records, six observed changes, exact 1:1:

| Record | Shape | Probe S12 | Reviewed `slide4` |
|---|---|---|---|
| `sp2 mod` | `Title 1` | `Perabot Taman` | `Papan Tanda` |
| `sp4 add mod` | `Rectangle 3` | **absent** | added off-canvas at −3.1531, 4.0845 |
| `sp6 mod` | `Rectangle 5` note panel | `klik hotspot` | `klik card`; `(PENAMBAHBAIKAN)` and `VO subtopik tidak perlu lagi` added |
| `sp8 mod` | `Rectangle 8` visual panel | 0.8046, 1.7813 **5.8621** × 5.2604 | 0.8046, 1.7813 **11.7371** × 5.2604 |
| `sp9 mod` | `TextBox 12` body | 6.8667, 2.5594 5.6621 × 3.8708 | 0.9046, 4.4115 11.6371 × 2.5244 |
| **`sp10 del mod`** | **`TextBox 16` body heading** | 6.8667, 1.8291 5.6621 × 0.5068, text `Papan Tanda` | **deleted** |
| *(unrecorded)* | `TextBox 19` `Kembali` | 6.0028, 7.1009 | **unchanged** |

**`slide5` (9008) ← probe S09.** The rebuild reconciles to the shape ID:

- `sp41–47 del` — probe S09's seven vertical-menu shapes are `Rectangle 9` id 41, `TextBox 16` id 42,
  `TextBox 17/19/21/23` id 43–46, `TextBox 25` id 47. **Exactly ids 41–47, exactly seven.**
- `sp4, 7, 10, 12, 14, 16, 18, 20, 22 add` — the nine card-grid shapes.
- `pic 34/36/38/40 mod ord` — the four ticks, moved from probe positions
  `x 11.77, y 3.01 / 3.78 / 4.54 / 5.31` to the card-grid positions.
- `sp9 mod` — note panel: `Semua hotspot selesai.` → `Semua card selesai.`, `(PENAMBAHBAIKAN)` added.

**`slide1` (9003) and `slide7` (9016)** — no records, and none needed (§3).

---

## 2. Base revision — now provable

# `BASE_REVISION_PROVEN = v0.1`

This **supersedes** `BASE_REVISION_NOT_DETERMINABLE` in `BARIAH_REVIEW_INGEST.md §5–6`.

### 2.1 Why the question is answerable at all

Per `TREATMENT_PROBE_VALIDATION.md` and `TREATMENT_PROBE_README.md`, v0.1 and v0.2 differ in **exactly
one place**: the `<a:pPr>` elements of the four body paragraphs on Probe Slide 2 = **S12**. Probe slides
1, 3 and 4 are byte-identical between revisions; the run elements on S12 were "never read, written or
re-encoded".

S12 is the reviewed deck's `slide4` (`sldId 9011`). **The one slide that discriminates the revisions is
present in the reviewed deck.** `MEASURED_FACT`

### 2.2 The two paragraph-property signatures

**v0.1, measured** (`p1/ppt/slides/slide12.xml`, `TextBox 12` id 9):

```xml
p0  <a:pPr marL="285750" indent="-285750"><a:buFont typeface="Arial" panose="020B0604020202020204" pitchFamily="34" charset="0"/><a:buChar char="•"/></a:pPr>
p1  <a:pPr><a:buChar char="•"/></a:pPr>
p2  <a:pPr><a:buChar char="•"/></a:pPr>
p3  <a:pPr><a:buChar char="•"/></a:pPr>
```

**v0.2, documented** (`TREATMENT_PROBE_README.md`, `TREATMENT_PROBE_VALIDATION.md`) —
all four paragraphs uniform: `marL=285750`, `indent=-285750`, **`spcBef=600` (6.0 pt)**,
`buFont=Arial`, `buChar='•'`, children emitted in schema order `spcBef, buFont, buChar`.
`DOCUMENTED_NOT_MEASURED`

**The discriminator is `spcBef`.** It is present on all four paragraphs in v0.2 and on none in v0.1.

### 2.3 What the reviewed deck carries — `MEASURED_FACT`

`x/ppt/slides/slide4.xml`, `TextBox 12` id 9, all eight paragraphs:

```xml
p0  <a:pPr marL="285750" indent="-285750"><a:buFont typeface="Arial" panose="020B0604020202020204" pitchFamily="34" charset="0"/><a:buChar char="•"/></a:pPr>
p1  (identical to p0)
p2  (identical to p0)
p3  <a:pPr marL="742950" lvl="1" indent="-285750"><a:buFont typeface="Arial" panose="020B0604020202020204" pitchFamily="34" charset="0"/><a:buChar char="•"/></a:pPr>
p4  (identical to p3)   p5 (identical to p3)   p6 (identical to p3)
p7  (identical to p0)
```

`grep -c spcBef` on `slide4.xml` returns **1**, and that single occurrence is `spcBef spcPts=0` inside
the **title placeholder**, not the body. **Zero body paragraphs carry `spcBef`.**

### 2.4 Proof

**Ground 1 — byte-identical inheritance.** Reviewed `p0`'s `<a:pPr>` is **byte-for-byte identical** to
v0.1 `p0`'s, including the serialisation-level attributes `panose="020B0604020202020204"`,
`pitchFamily="34"`, `charset="0"`. Bariah's edit to this paragraph was a text change; PowerPoint
preserves `<a:pPr>` across text edits. The surviving `<a:pPr>` is the base's.

**Ground 2 — `spcBef` is absent where v0.2 mandates it.** In v0.2 every one of the four body paragraphs
carries `spcBef=600`. `spcBef` is a paragraph property that survives text editing, `Enter`-key
paragraph splits, and `Tab` demotion — the exact operations that turn 4 paragraphs into 8 across two
outline levels. For all eight reviewed paragraphs to lack it, either the base lacked it, or Bariah
explicitly cleared spacing-before on every paragraph individually. There is no evidence of the latter
and it would leave no other trace.

**Ground 3 — the propagation pattern is v0.1's, exactly.** In v0.1, `p0` carries the full property set
and `p1–p3` carry `buChar` only. In the reviewed deck **all eight** paragraphs carry the full set. That
is precisely what results from placing the caret in `p0` and building the new list by `Enter`/`Tab`:
new paragraphs inherit the properties of the paragraph being split — `p0`'s — which include
`marL`/`indent`/`buFont` and **exclude `spcBef`**. Starting from v0.2 the same operation would have
propagated `spcBef=600` to all eight.

Three independent grounds, all pointing the same way, and no evidence pointing the other way.

### 2.5 Residual uncertainty, stated

Ground 2 and Ground 3 depend on v0.2's content being as documented, since v0.2 itself is not attached.
That documentation verified 14/14 on independently checkable claims (§0.1), so the reliance is
well-founded but is not a measurement. Ground 1 — the byte-identical `<a:pPr>` — rests on **measured
v0.1 bytes alone** and is independent of the documentation.

**To convert this from proven-on-strong-evidence to proven-on-measurement, attach v0.2** and confirm
its S12 `<a:pPr>` carries `spcBef=600`. Nothing else is needed.

---

## 3. Control-slide shape-tree verification

This **supersedes** the `NOT_DETERMINABLE` in `BARIAH_REVIEW_INGEST.md §4`.

Method: extract `<p:spTree>…</p:spTree>` from each part and diff element-by-element.
Byte-identity is **not** the correct test — the reviewed deck was re-serialised by PowerPoint while the
probe was written by `python-pptx`, so identical content necessarily differs in encoding. The test
applied is structural identity of the shape tree.

### 3.1 `slide1` (9003) versus probe S04 — `MEASURED_FACT`

Both trees are **13,091 characters**. The unified diff is **one hunk**:

```
- <a:endParaRPr lang="en-US" sz="1600" b="1" dirty="0"> … </a:endParaRPr>   (end of empty ¶4)
+ <a:endParaRPr lang="en-US" sz="1600" b="1" dirty="0"> … </a:endParaRPr>   (end of empty ¶6)
```

An `a:endParaRPr` block **relocated between two empty paragraphs** in the off-canvas note panel.
`a:endParaRPr` records the formatting state at the caret at end-of-paragraph; it renders nothing.

**Zero shapes added or removed. Zero geometry changes. Zero text changes. Zero `a:pPr` or `a:rPr`
changes on any run. All 11 shapes present with identical IDs, names, geometry and z-order.**

Verified identical: `Title 1` id 2 · `Rectangle 8` id 9 (−3.35, 0.0, 3.1496×7.5) · `TextBox 5` id 6 ·
`Rectangle 17` id 18 · `Rectangle 9` id 19 (0.8046, 1.7813, **5.8621**×5.2604) · `TextBox 16` id 20 ·
`TextBox 3/7/10/12` id 21–24 at x 8.5938, y 2.8614/3.646/4.4307/5.2552 · `TextBox 14` id 25.

**Verdict: shape-tree identity confirmed, modulo one caret marker.**

### 3.2 `slide7` (9016) versus probe S17 — `MEASURED_FACT`

Trees 7,362 vs 7,400 characters. The diff is **one element**:

```
- <a:endParaRPr lang="en-MY" dirty="0"/>
```

Removed from the trailing empty paragraph of `TextBox 24`. Again a caret marker with no rendered
content.

All 5 shapes identical: `Rectangle 18` id 19 (0.7917, 1.7812, 11.7292×5.2604) · `Title 1` id 2 ·
`TextBox 6` id 7 · `Rectangle 8` id 9 · `TextBox 24` id 25 (0.8125, 4.43, 11.7083×2.5244).
Body text identical to the character, including the em dash in
`Komponen Landskap — Struktur Taman dan Perabot Taman`, the lowercase `Isi utama:`, and **`BBQ pit`**
with lowercase `p`.

**Verdict: shape-tree identity confirmed, modulo one caret marker.**

### 3.3 What this establishes

The two control slides are **verified pristine against the actual probe base**, not merely inferred
pristine from an absence of change records. The `changesInfo`-based inference in
`BARIAH_REVIEW_INGEST.md §3.1` was correct, and is now superseded by direct measurement — a stronger
basis, since it does not depend on the change log being complete.

Because probe slides 1, 3 and 4 are byte-identical between v0.1 and v0.2, this verification holds
against **both** revisions and is therefore independent of §2's determination.

---

## 4. The reviewed full-width state against the canonical archetypes

### 4.1 Canonical STATE — canon slide 6, measured via probe S12 — `MEASURED_FACT`

| Shape | ID | x | y | w | h | Role |
|---|---:|---:|---:|---:|---:|---|
| `Title 1` | 2 | *(inherited)* | | | | section title `Perabot Taman` |
| `Rectangle 5` | 6 | −3.3500 | 0.0000 | 3.1496 | 7.5000 | off-canvas note panel |
| `TextBox 6` | 7 | 0.6758 | 0.4583 | 12.0075 | 0.6479 | title bar `Papan Tanda` |
| `Rectangle 8` | 8 | 0.8046 | 1.7813 | **5.8621** | 5.2604 | **visual panel — left half** |
| **`TextBox 16`** | **10** | **6.8667** | **1.8291** | **5.6621** | **0.5068** | **body heading `Papan Tanda`** |
| `TextBox 12` | 9 | 6.8667 | 2.5594 | 5.6621 | 3.8708 | body, 4 bullets — right column |
| `TextBox 19` | 11 | 6.0028 | 7.1009 | 1.3277 | 0.3366 | `Kembali` |

Visual panel occupies **43.97 %** of stage width and ends at x 6.6667; the right column begins at
x 6.8667. Gutter **0.2000 in**. Non-overlapping, side-by-side. **This is unambiguously a split-STATE
layout, and it carries a dedicated body-heading box.**

### 4.2 Canonical RUMUSAN — S17, measured — `MEASURED_FACT`

| Shape | ID | x | y | w | h |
|---|---:|---:|---:|---:|---:|
| `Rectangle 18` | 19 | 0.7917 | 1.7812 | **11.7292** | 5.2604 |
| `TextBox 24` | 25 | 0.8125 | 4.4300 | 11.7083 | 2.5244 |

### 4.3 The two canonical archetypes are distinct by a factor of two — `MEASURED_FACT`

| Quantity | canon STATE (S12) | canon RUMUSAN (S17) | Ratio |
|---|---:|---:|---:|
| Panel width | 5.8621 | 11.7292 | **2.0009×** |
| Panel x | 0.8046 | 0.7917 | — |
| Panel y / h | 1.7813 / 5.2604 | 1.7812 / 5.2604 | identical |
| Body width | 5.6621 | 11.7083 | 2.0679× |
| Separate heading box | **yes** | no (inline bold lead) | — |
| `Kembali` | yes | no | — |

Same vertical frame, **half the width**. The canonical system distinguishes a reveal-child from a
summary screen by panel width, and does so by an almost exact 2:1 ratio.

### 4.4 What Bariah changed — `MEASURED_FACT`

| Quantity | Probe S12 (canonical) | Reviewed `slide4` | Δ |
|---|---:|---:|---:|
| Visual panel w | 5.8621 | **11.7371** | **+5.8750 (+100.22 %)** |
| Body x | 6.8667 | 0.9046 | −5.9621 |
| Body y | 2.5594 | 4.4115 | +1.8521 |
| Body w | 5.6621 | **11.6371** | **+5.9750 (+105.53 %)** |
| Body h | 3.8708 | 2.5244 | −1.3464 (−34.78 %) |
| Body heading box | present | **deleted** | `sp10 del` |
| `Kembali` | 6.0028, 7.1009 | 6.0028, 7.1009 | **unchanged** |

### 4.5 The collapse, quantified — `MEASURED_FACT`

| Comparison | Δ panel width |
|---|---:|
| Reviewed `slide4` panel (11.7371) vs **canon RUMUSAN** panel (11.7292) | **+0.0079 in** |
| Reviewed `slide4` panel (11.7371) vs **canon STATE** panel (5.8621) | **+5.8750 in** |

**Bariah widened the canonical split-STATE panel to within 0.0079 in — 1.1 px at 1920 — of the
canonical Rumusan panel, and deleted the heading box that distinguished the child's body from a
summary body.**

`STATE_ARCHETYPE_OPTIONS.md §2.2` measured the reviewed state as indistinguishable from Rumusan
(max Δ 0.0129 in). That finding stands, and its cause is now determinate: it is not a coincidence of
authoring, it is the numeric endpoint of a deliberate widening away from a canonical archetype that
was exactly half as wide.

---

## 5. Does any canonical reveal-child use a full-width form?

## Answer for the one measurable canonical reveal-child: **No.** `MEASURED_FACT`

Canon slide 6, cloned verbatim into probe S12 and measured in §4.1, uses the **split** form:
5.8621 in visual panel (43.97 % of stage), right-hand body column, a dedicated heading box, and
`Kembali` below. There is no full-width element on it.

### 5.1 Scope of the answer

| Screen | Role | Measured? | Form |
|---|---|---|---|
| S12 | FULL — reveal child of S10 | **yes, directly** | **split-STATE** |
| S05, S06, S07, S08 | FULL — reveal children of S04 | no | `NOT_DETERMINABLE` |
| S11, S13, S14, S15 | FULL — reveal children of S10 | no | `NOT_DETERMINABLE` |

**1 of 9 reveal children measured; it is split-STATE.** The remaining eight require
`SB_K5PL06T03B02_TIER1_STORYBOARD_SPEC_v1_2_CANDIDATE.pptx` (`d523f467…`) or
`SB_K4PL3T2_v1.2.pptx` (`16521234…0287cf2`), neither of which is attached.

### 5.2 Documentary corroboration — `DOCUMENTED_NOT_MEASURED`

`TREATMENT_PROBE_MAPPING.md` names canon slide 6 as **"split-STATE child"** — singular archetype
language, describing a canonical form rather than one instance. `TREATMENT_PROBE_README.md` states
that probe slides 1–3 pair "vertical-menu base (canon slide 10) with **split-STATE children**
(canon slide 6)", again treating split-STATE as *the* child archetype.

Neither statement is a measurement of S05–S08 or S11/S13–S15. Together with §5.1 they make a full-width
canonical reveal-child unlikely, but the eight unmeasured screens remain formally open.

### ⚠️ 5.3 Naming collision — must be resolved before any decision is minuted

`TREATMENT_PROBE_README.md` uses **"Option B"** to mean *vertical-menu base paired with split-STATE
children* — a statement about **pairing**.

`STATE_ARCHETYPE_OPTIONS.md` uses **"Option B"** to mean the **full-width panel archetype** — a
statement about **one screen's geometry**.

**These are different axes, and on the geometry axis they point in opposite directions:** the probe
README's "Option B" *contains* split-STATE children, which is `STATE_ARCHETYPE_OPTIONS.md`'s
**Option A**. Any minute that says "adopt Option B" is ambiguous to the point of being reversible.
`OPEN_DECISION` — the two option sets must be renamed before use.

---

## 6. Packet-side baselines

### 6.1 What is now measurable, and what is not

| Requirement | Status |
|---|---|
| `anda` across all 19 screens | **4 of 19 measured** (S04, S09, S12, S17); 15 `NOT_DETERMINABLE` |
| English lexicon with source nodes | **source forms now measured** on the source-bound probe; source *nodes* still absent |
| Per-screen Card/Hotspot inputs | **screen roles and child counts recovered** (§1.3); per-screen image bindings `NOT_DETERMINABLE` |
| Source label vs reviewed display | **now a direct measurement**, not a proxy |

`packet_B02.json` and `asset_manifest.json` remain absent.

**Why the probe is a legitimate source baseline:** `TREATMENT_PROBE_MAPPING.md` records that probe
shapes were cloned **verbatim** from the Tier-1 specification deck, and §0.1 verifies 14/14 of the
documentation's checkable claims. Probe text on S04/S09/S12/S17 is therefore source text for those four
screens — a materially stronger basis than the `slide7`-as-proxy used in
`SME_RULE_CHECKABILITY.md §7`.

### 6.2 `anda` and `kontraktor` across the measured screens — `MEASURED_FACT`

| Token | Locus | Channel | Screen |
|---|---|---|---|
| `anda` | `slide17.xml` `TextBox 24` ¶3 | display | **S17 RUMUSAN** |
| `anda` | `notesSlide12.xml` | VO | **S17 RUMUSAN** |
| `kontraktor` | — | — | **zero occurrences anywhere in probe v0.1** |

| Deck | `anda` | `kontraktor` |
|---|---:|---:|
| Probe v0.1 (S04, S09, S12, S17) | **2** | **0** |
| Reviewed deck, learner-visible | 1 (`slide7`) | 1 (`slide8`) |

Three findings:

1. **`anda` is Rumusan-scoped in the source too.** Both occurrences are on S17. S04, S09 and S12 —
   a base, a completion state and a reveal child — contain **zero**. The scope boundary in Bariah's
   rule matches the source's own practice on the four measured screens.
2. **`kontraktor` does not exist in the source baseline.** Every occurrence in the reviewed deck is
   Bariah's.
3. The substitution is confined to S17/Rumusan in both channels. **`SME_RULE_CHECKABILITY.md §4.4`'s
   `OPEN_DECISION` on scope narrows** but does not close: 15 screens remain unmeasured, and absence of
   `anda` on 3 non-Rumusan screens is weak evidence about a rule for 19.

### 6.3 English-origin lexicon with measured source forms — `MEASURED_FACT`

| Term | **Source form (probe)** | Loci in probe | Italic in probe | Reviewed display | Italic in reviewed |
|---|---|---|---|---|---|
| `Water Feature` | `Water Feature` | `slide4`, `slide9`, `slide17`, `notesSlide4`, `notesSlide12` | **no** (5/5) | `Water Feature` | only on `slide8` |
| `Drinking Fountain` | `Drinking Fountain` | `slide17`, `notesSlide12` | **no** (2/2) | `Drinking Fountain` | only on `slide8` |
| **`BBQ pit`** | **`BBQ pit`** — lowercase `p` | `slide17`, `notesSlide12` | **no** (2/2) | **`BBQ Pit`** on `slide8` | yes on `slide8` |

**Zero italic runs on any English-origin term anywhere in probe v0.1** — 9 occurrences, 9 non-italic.
Rule R2 has no precedent in the source baseline; it is entirely new practice.

**The `BBQ pit` source form is now measured, not assumed.** `SME_RULE_CHECKABILITY.md §7.3` took the
source form from the task statement; it is confirmed: source reads `BBQ pit`, lowercase `p`, in both
the S17 display and the S17 VO.

### 6.4 Per-screen Card / Hotspot inputs — `PROVISIONAL_IDENTIFIER`

| Screen | Role | Bound children | One covering image? | Children discrete? | Coordinates? | Provisional |
|---|---|---:|---|---|---|---|
| S04 | CR_BASE (Struktur Taman) | **4** (S05–S08) | yes — `Rectangle 9` 5.8621×5.2604, `IMG-01` ms 237 | yes — 4 boxes at x 8.5938, **outside** the image | **no** | `INDETERMINATE` |
| S05–S08 | FULL | 0 (children) | — | — | — | n/a |
| S09 | TICK | 4 tick states | as S04 | as S04 | no | `INDETERMINATE` |
| **S10** | **CR_BASE (Perabot Taman)** | **5** (S11–S15) | `NOT_DETERMINABLE` | `NOT_DETERMINABLE` | `NOT_DETERMINABLE` | `NOT_DETERMINABLE` |
| S11–S15 | FULL | 0 (children) | — | — | — | n/a |
| S16 | TICK | 5 tick states | `NOT_DETERMINABLE` | — | — | `NOT_DETERMINABLE` |
| S17 | RUMUSAN | 0 | — | — | — | n/a |
| S01–S03, S18, S19 | title/dialog/overview/quiz/end | 0 | — | — | — | n/a |

**S04's `INDETERMINATE` verdict is confirmed at source, not introduced by the reviewed deck.** The
probe's S04 — cloned verbatim from canon slide 10 — has the same contradiction reported in
`SME_RULE_CHECKABILITY.md §6.3`: the note panel says `4 hotspot`, while the four menu items sit at
x 8.5938, **1.9271 in clear of the image's right edge at x 6.6667**. The ambiguity is a property of
the canonical vertical-menu archetype. That materially strengthens Bariah's `slide2` rationale and her
`I think it's best/logical to use Click & Reveal (Card)` recommendation — she is resolving a real
canonical ambiguity, not inventing a problem.

**Still absent:** no coordinate or region data on any probe screen either. Probe media is
`ppt/media/image3.svg` — the tick checkmark — and nothing else. Every `Visual:` panel is a text
placeholder. The Card/Hotspot **gate remains unconstructible**; `SME_RULE_CHECKABILITY.md §6.4` stands.

### 6.5 Source label versus reviewed display — direct measurement — `MEASURED_FACT`

Probe S17 is the source; reviewed `slide8` is Bariah's revision. `slide7` is verified identical to the
probe (§3.2), so the §7 table in `SME_RULE_CHECKABILITY.md` is now **confirmed against source rather
than proxy** — every row holds unchanged:

| # | Source (probe S17) | Reviewed `slide8` | Classification |
|---:|---|---|---|
| 1 | `BBQ pit` | `BBQ Pit` | **display normalisation — deviates from measured source** |
| 2 | `—` (U+2014) | `-` (U+002D) | punctuation change from source |
| 3 | `…Taman dan Perabot…` | `…Taman Dan Perabot…` | **over-capitalisation — regression, confirmed against source** |
| 4 | `perabot taman merangkumi` | `Elemen Perabot Taman -` | display normalisation |
| 5 | `struktur taman merangkumi` | `Struktur Taman -` | display normalisation |
| 6 | `anda` | `Kontraktor` | SME rule R4 |
| 7 | `Kepentingan:` / `Isi utama:` / `Manfaat kefahaman:` | removed | SME rule R3 |
| 8 | all bullets end `.` | none end with punctuation | display normalisation |
| 9 | `Drinking Fountain, BBQ pit.` | `Drinking Fountain dan BBQ Pit` | display normalisation |
| 10 | no italics | 3 terms italic | SME rule R2 |

`OPEN_DECISION` on the approval policy stands. Row 3 is now confirmed a regression **against measured
source**, not against a proxy.

### 6.6 The issued S12 display — the comparison `DISPLAY_BUDGET_REDERIVED.md §1` could not run

`MEASURED_FACT` — probe `slide12.xml`, `TextBox 12` id 9:

| Metric | **Issued S12** | Bariah's reviewed `slide4` | Δ |
|---|---:|---:|---:|
| Paragraphs | 4 | 8 | +4 |
| Characters | **346** | 285 | **−61 (−17.6 %)** |
| Words | **50** | 40 | −10 (−20.0 %) |
| Sentences | **4** | 0 | −4 |
| Commas | **7** | 4 | −3 |
| Bullets | 4 (1 level) | 8 (2 levels) | +4 |
| Box | 6.8667, 2.5594 · 5.6621 × 3.8708 | 0.9046, 4.4115 · 11.6371 × 2.5244 | — |
| Level-0 line box | **5.1496 in** | 11.1246 in | **+116 %** |
| Capacity | 41–45 ch/line | 89–97 ch/line | +117 % |
| Est. rendered lines | ~10 (box admits 12.6) | **8 (box admits 8.08)** | −2 |
| Line-slot utilisation | ~80 % | **100 %** | — |

### 6.7 The issued S12 display was a verbatim copy of its own VO — `MEASURED_FACT`

Probe `notesSlide16.xml` (bound to S12), 449 characters:

> `PL06: Pengurusan Operasi Pembinaan Landskap` / `Topik 3 Bahagian 2: Komponen Landskap` /
> `Hilmi: Papan Tanda. Papan tanda adalah elemen penting untuk navigasi, maklumat, dan keselamatan dalam ruang landskap. Papan tanda mesti jelas, mudah dibaca, dan diletakkan di lokasi yang strategik. Ia boleh berupa penunjuk arah, peta taman, informasi tentang tumbuhan atau ciri landskap, atau peraturan taman. Bahan yang digunakan harus tahan cuaca dan tahan luntur.`

**The four VO sentences and the four S12 display bullets are the same four sentences, character for
character.** In the issued baseline, display **is** VO.

Bariah's revision:

- **VO body: unchanged.** Reviewed `notesSlide3` carries the same four sentences verbatim. Only the
  header changed — `Hilmi: Papan Tanda.` → `Perabot Taman`, applying rule R1.
- **Display: compressed** 346 → 285 chars, 4 sentences → 8 bullets, subject/copula/relativiser elided,
  all terminal punctuation removed, the inline list exploded into 4 sub-bullets.

This is the cleanest possible instance of the pattern. **She broke a display≡VO identity in one
direction only: display down, VO propositions intact.**

---

## 7. Consequences for the gate determinations

### 7.1 `LOSSLESS_RESEGMENTATION_GATE_SUPERSEDED` — confirmed against the issued baseline

`DISPLAY_BUDGET_REDERIVED.md §7` established this on the reviewed deck's internal evidence and its
Rumusan control pair, with the S12 comparison outstanding. **The S12 comparison now runs, and it is the
strongest evidence in the set:**

1. The issued S12 display was **byte-identical to its VO body** (§6.7). There was no display/VO
   distinction to preserve — Bariah created one.
2. The VO body survived her edit **verbatim**. Not shortened, not reworded — only the `Hilmi:` header
   changed, under a separately-stated rule.
3. Display compression is grammatical: 4/4 propositions retained
   (`DISPLAY_BUDGET_REDERIVED.md §3.7`), zero content words removed, **zero tokens added**.
4. She simultaneously **widened** the display column 116 % and **reduced** its content 17.6 %, landing
   on 8/8 line slots.

The determination stands and its `NOT_DETERMINABLE` caveat on S12 is closed. Coverage remains
**2 screens measured of 19**; the 17 unmeasured screens are still formally open.

### 7.2 The five-card arithmetic is not hypothetical

`CARD_ARCHETYPE_SPEC.md §5` computed the five-card variants without knowing whether a five-child screen
existed. **It does: S10 CR_BASE binds S11–S15** — Kerusi Taman, Papan Tanda, Tong Sampah,
Drinking Fountain, BBQ Pit (§1.3). Every option in `CARD_ARCHETYPE_SPEC.md §5.5` applies to a real
screen, and the finding that **no arrangement preserves the reviewed card size within the deck's
content band** is a live constraint on S10, not a thought experiment.

Note the interaction with §6.4: S10's own Card/Hotspot classification is `NOT_DETERMINABLE`. If S10
resolves to Hotspot, the five-card geometry question does not arise for it at all.

---

## 8. Corrections, narrowings and upgrades to the existing five documents

The five documents are **not rewritten**. This section is the correction register.

### 8.1 Corrections — prior statements that were wrong

| # | Document · locus | Prior statement | Correction |
|---:|---|---|---|
| **C1** | `BARIAH_REVIEW_INGEST.md` **§2.1** | "Base `sldId`s ascend `9003 < 9008 < 9011 < 9016`… **Bariah swapped the two middle base slides**", with a movement table showing 9008 base-pos 2 → final 5 and 9011 base-pos 3 → final 4. | **Wrong.** The probe's actual `sldIdLst` is **`9003, 9011, 9008, 9016`** — S04 → S12 → S09 → S17. The relative order of 9011 and 9008 is **identical** in probe and reviewed deck. **No transposition occurred.** The `ord` flags reflect absolute position shifts caused by the four insertions (9011: 2→4, 9008: 3→5). The error came from assuming `sldId` assignment order equals slide order; it does not. §2.1's table is void; §2's main mapping table is unaffected. |
| **C2** | `BARIAH_REVIEW_INGEST.md` **§8.5**, `§10.3 R9` | `This is just to show tick icon.` classified `SME_AUTHORED_RULE`. | **Wrong.** Verbatim in probe S09 note panel ¶3. → **`INHERITED_PROBE_CONTENT`.** |
| **C3** | `BARIAH_REVIEW_INGEST.md` **§8.5** | `Dipapar penuh selepas learner klik card.` classified `SME_AUTHORED_RULE`. | **Narrow.** Probe S12 reads `Dipapar penuh selepas learner klik **hotspot**.` Bariah changed one word. → **inherited text, Bariah-modified** — not an authored rule. |
| **C4** | `BARIAH_REVIEW_INGEST.md` **§10.3 R9** | `Semua card selesai.` classified `SME_AUTHORED_RULE`. | **Narrow.** Probe S09 reads `Semua **hotspot** selesai.` Same one-word substitution. → **inherited text, Bariah-modified.** |

### 8.2 Upgrades — `NOT_DETERMINABLE` now resolved

| # | Document · locus | Prior | Now |
|---:|---|---|---|
| **U1** | `BARIAH_REVIEW_INGEST.md` **§5–6** | `BASE_REVISION_NOT_DETERMINABLE` | **`BASE_REVISION_PROVEN = v0.1`** on three grounds (§2.4). |
| **U2** | `BARIAH_REVIEW_INGEST.md` **§4** | Byte/shape-tree identity vs probes `NOT_DETERMINABLE` | **Verified.** `slide1` vs S04 and `slide7` vs S17 differ only by `a:endParaRPr` caret markers (§3). |
| **U3** | `BARIAH_REVIEW_INGEST.md` **§10.3 caveat**, **§11 item 6** | `VO subtopik tidak perlu lagi` — authorship `NOT_DETERMINABLE` at paragraph granularity | **Resolved: absent from probe S12's note panel → `SME_AUTHORED_RULE`.** |
| **U4** | `BARIAH_REVIEW_INGEST.md` **§8.5**, **§11 item 3** | `IMG-01`/ms 237 vs `IMG-05`/ms 243 conflict — `OPEN_DECISION` / `PROVISIONAL_IDENTIFIER` | **Resolved to `MEASURED_FACT` with determinate cause.** Probe S12 correctly cites `IMG-05`, ms 243 in **both** its visual panel and its note panel. Bariah added an off-canvas box (`Rectangle 3` id 4, `sp4 add mod`) cloned from the **Struktur Taman** slides, carrying `IMG-01`, ms 237 — the wrong image for `Papan Tanda`. **A provenance regression introduced by Bariah**, not a pre-existing ambiguity. The correct citation survives in `slide4`'s note panel ¶5. |
| **U5** | `STATE_ARCHETYPE_OPTIONS.md` **§2.3 Q1** | "Does any canonical reveal-child use the full-width form?" `NOT_DETERMINABLE` | **Answered for the one measurable canonical reveal-child: No** (§5). Canon slide 6 = split-STATE, 5.8621 in panel. Eight further FULL screens remain open. |
| **U6** | `STATE_ARCHETYPE_OPTIONS.md` **§2.3 Q2** | "Does the reviewed state contain a separate body-heading box? **No.**" | **Upgrade — the absence is a deletion.** Probe S12 carries `TextBox 16` id 10 at 6.8667, 1.8291, 5.6621 × 0.5068, text `Papan Tanda`. `changesInfo` records `sp10 del mod @22:52:53`. Bariah **deleted the canonical body-heading box.** |
| **U7** | `DISPLAY_BUDGET_REDERIVED.md` **§1**, **§8** | S12 comparison `NOT_DETERMINABLE` | **Resolved** (§6.6): 4 ¶, 346 ch, 50 words, 4 sentences, 7 commas, box 5.6621 × 3.8708. |
| **U8** | `SME_RULE_CHECKABILITY.md` **§7.3** | `BBQ pit` source form "taken as given from the task statement" | **Measured.** Probe S17 display and `notesSlide12` VO both read `BBQ pit`, lowercase `p`, non-italic (§6.3). |

### 8.3 Narrowings — findings that survive but change weight

| # | Document · locus | Narrowing |
|---:|---|---|
| **N1** | `STATE_ARCHETYPE_OPTIONS.md` **§2.1** | Option A's reference geometry was taken from reviewed `slide1` — a *parent* state used as a proxy, with the caveat stated. **Replace with the real canonical child geometry:** panel 0.8046, 1.7813, **5.8621** × 5.2604; body **6.8667, 2.5594, 5.6621 × 3.8708**; heading box 6.8667, 1.8291, 5.6621 × 0.5068. The proxy was close on panel width (identical, 5.8621) but wrong on the body column (proxy 6.8633, 1.7979, 6.1867 × 1.0098). Option A's **capacity** figures should be restated: line box **5.1496 in** → **41–45 ch/line**, not the 5.6742 in / 45–49 ch estimated from the proxy. The direction and magnitude of the conclusion are unchanged. |
| **N2** | `STATE_ARCHETYPE_OPTIONS.md` **§4** | The Option A recommendation was framed as a proposal against an unknown canon. **It is now a restoration**, not a proposal: split-STATE is the measured canonical form Bariah departed from. Reasoning items 1–3 strengthen; item 5's "sample of one reveal-child" caveat is superseded by §5.1. **Subject to the §5.3 naming collision — do not minute "Option A"/"Option B" without renaming.** |
| **N3** | `CARD_ARCHETYPE_SPEC.md` **§2.6** | Tick deviations were attributed to Bariah's hand placement. **The canonical baseline is also imperfect:** probe S09 ticks sit at pitch 0.77 / 0.76 / 0.77 against a menu-item pitch of 0.7846 / 0.7847 / **0.8245**, max mismatch **0.083 in**. Hand placement is **inherited practice**; Bariah amplified it (max deviation 0.3113 in vs 0.083 in, a 3.7× increase). She did not introduce it. |
| **N4** | `CARD_ARCHETYPE_SPEC.md` **§1.1** | C2's text `Visual: Struktur Persisir Teduhan` was flagged `PROVISIONAL_IDENTIFIER`. **Confirmed `MEASURED_FACT`:** no such string exists anywhere in probe v0.1; the four card rectangles are Bariah-created (`sp add @23:07:55`). Bariah-introduced copy-paste error. |
| **N5** | `CARD_ARCHETYPE_SPEC.md` **§5** | Five-card arithmetic was hypothetical. **Grounded on S10 CR_BASE / S11–S15** (§7.2). |
| **N6** | `SME_RULE_CHECKABILITY.md` **§1** | `Hilmi:` — reviewed deck shows 2 occurrences, both on untouched slides. **Bariah removed it twice, not once:** probe carries `Hilmi:` on **all three** non-empty notes (S04, S12, S17). She removed it from S12's notes (→ `notesSlide3`, `modNotesTx` on 9011) **and** from S17's (→ `notesSlide7`). Two removals, both on screens she revised; both retained screens are ones she never opened. |
| **N7** | `SME_RULE_CHECKABILITY.md` **§2.2** | Italic application rate 3/9 within the reviewed deck. **Extend:** probe v0.1 has **zero** italic runs on any English-origin term (9 occurrences, 9 non-italic). R2 has no source precedent. |
| **N8** | `SME_RULE_CHECKABILITY.md` **§4.4** | `anda` scope beyond Rumusan `OPEN_DECISION`. **Narrows:** probe `anda` occurs only on S17, in both channels; S04, S09 and S12 have zero. Source practice matches the rule's scope on 4 of 19 screens. Does not close — 15 screens unmeasured. |
| **N9** | `SME_RULE_CHECKABILITY.md` **§6.3** | S04's `INDETERMINATE` verdict was read as an ambiguity in the reviewed deck. **It is canonical.** Probe S04 — cloned verbatim from canon slide 10 — has the same `4 hotspot` note against menu items 1.9271 in clear of the image. The list-beside-image ambiguity is a property of the canonical vertical-menu archetype, which **strengthens** Bariah's Card recommendation. |
| **N10** | `BARIAH_REVIEW_INGEST.md` **§0.4**, `SME_RULE_CHECKABILITY.md` **§8.3** | iSpring block called "inherited debris from a donor file". **Chain now established:** the identical 23-tag block is present in probe v0.1, which `python-pptx` cloned from the Tier-1 specification deck. It entered at the **source specification**, propagated through the probe build, and survived Bariah's PowerPoint save. Not introduced by the probe build and not by Bariah. §8.4's recommendation against reinjection is unchanged and now better founded. |
| **N11** | `BARIAH_REVIEW_INGEST.md` **§1.2** | Caveat: "editing before this change log began is invisible." **Confirmed real.** Probe v0.1 carries its own `changesInfo1.xml` — **71,825 bytes, 206 records, all `Bariah Ahmad`, `dt` 2026-07-14 → 2026-07-25, 33 distinct `sldId`s in the range 8000–8051** — which match neither the probe's slides nor the reviewed deck's. PowerPoint **replaced** rather than appended the log. Prior editing history exists and is absent from the reviewed deck's log. **Conclusions are unaffected**, because §3 replaces the change-log inference for the control slides with direct measurement. |

### 8.4 New finding — provenance of the source specification — `PROVISIONAL_IDENTIFIER`

The probe's inherited change log (N11) names **`Bariah Ahmad`** as the sole editor across 206 records
and 33 slides, 14–25 July 2026 — while the probe's own `cp:lastModifiedBy` is **`CAIR compiler`** and
`dcterms:modified` is `2026-07-25T19:09:29Z`.

The most economical reading of the custody chain:

```
Tier-1 specification deck   — edited by Bariah Ahmad, 14–25 Jul 2026 (206 records, 33 slides)
        ↓ python-pptx clone of 4 screens
probe v0.1                  — built by "CAIR compiler", 25 Jul 2026 19:09Z
        ↓ (v0.2: pPr-only revision on S12 — not attached)
reviewed deck               — edited by Bariah Ahmad, 29 Jul 2026 22:15–23:14Z (65 records)
```

If correct, **Bariah is not solely a downstream reviewer of this material — she is also an author of
the source specification the probe was cloned from.** That would change how her review annotations
should be weighted: parts of what reads as external SME review may be the source author revising her
own earlier work.

Marked `PROVISIONAL_IDENTIFIER`: the inherited log's `sldId`s match neither deck, so the inference that
it belongs to the Tier-1 specification is well-supported but not directly verified. Confirm by opening
`SB_K5PL06T03B02_TIER1_STORYBOARD_SPEC_v1_2_CANDIDATE.pptx` (`d523f467…`) and checking whether its
`sldIdLst` falls in the 8000–8051 range. **Enters Stage 0A.**

---

## 9. What remains open

| # | Item | Blocking artifact | Label |
|---:|---|---|---|
| 1 | Confirm v0.2's S12 `spcBef=600` by measurement | probe v0.2 (`75f8b168…`) | `DOCUMENTED_NOT_MEASURED` |
| 2 | Form of reveal children S05–S08, S11, S13–S15 | Tier-1 spec (`d523f467…`) or canonical (`16521234…`) | `NOT_DETERMINABLE` |
| 3 | `anda` / lexicon / Card-Hotspot inputs for the 15 unmeasured screens | `packet_B02.json` | `NOT_DETERMINABLE` |
| 4 | Per-screen image bindings and region data — Card/Hotspot **gate** | `asset_manifest.json` + source nodes | `NOT_DETERMINABLE` |
| 5 | Whether S10 is Card or Hotspot — governs whether the five-card geometry question arises | `packet_B02.json` | `NOT_DETERMINABLE` |
| 6 | Content of the discarded slide `sldId 9018` | none — unrecoverable | `NOT_DETERMINABLE` |
| 7 | Option A/B naming collision between the two option sets | — | `OPEN_DECISION` |
| 8 | Source-normalisation approval policy (10 rows, §6.5) | — | `OPEN_DECISION` |
| 9 | Bariah's authorship of the source specification (§8.4) | Tier-1 spec (`d523f467…`) | `PROVISIONAL_IDENTIFIER` |
| 10 | The CAIR family judgement the probe exists to answer — requires PowerPoint rendering, per `LOCAL_REVIEW_CHECKLIST.md` | local PowerPoint | `OPEN_DECISION` |

Item 10 is worth restating: `LOCAL_REVIEW_CHECKLIST.md` records that **neither probe revision has ever
been seen rendered** — LibreOffice cannot load them in the build sandbox. Everything in Phase B1,
including this addendum, is measurement of XML. The family-coherence judgement the probe was built to
support has still not been made.

---

## 10. Modification statement

No PPTX was modified. Both packages were re-hashed after all analysis:
reviewed deck `ee4f54790bd22afb82457237d63d290eb6ac0ceabbead88ec5f7d7fced8bb9e7`,
probe v0.1 `24dcaa049130d067de2ce95704cae99bd5a49c0b2c8d99819604a8dbac1d471c` — both unchanged.
Reads were streaming plus scratchpad extractions never written back.
No compiler code was patched, no schema altered, no canonical ID issued, and no candidate, manifest,
baseline, digest pin or freeze created. The five existing Phase B1 documents are unmodified; §8 is a
correction register, not an edit.
