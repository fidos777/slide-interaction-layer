# PREFLIGHT_MAPPING — v0.3

```
OUTPUT_ONLY_DISPOSABLE_PREFLIGHT
NOT_A_19_SLIDE_STORYBOARD
NOT_CAIR_RATIFIED
NOT_PRODUCTION_AUTHORISED
```

## Artifact — **current revision v0.3**

```
K5PL06T03B02_3SCREEN_IMPLEMENTATION_PREFLIGHT_v0_3.pptx
35,593 bytes
sha256  ebf0eb8a1e5564bee2f656041f210ec48760a87cc811f6879b976e6298bf3e1c
md5     3415f5ed790a2b57b998e69e803c37cf
3 slides · 1 master · 7 layouts · 3 notes slides · 41 package entries
```

### v0.3 — one bounded correction: reserved navigation strip

`LOCAL_PREFLIGHT_REVIEW_PASS_WITH_ONE_FIX` — the v0.2 treatment is accepted except the S12 `Kembali`
clearance (0.0333 above / 0.045 below). v0.3 corrects that and nothing else.

**The panel had to shorten — that is a derivation, not a preference.** Below the canonical panel there
are **0.4583 in** to the stage edge. `Kembali` at 16 pt needs 0.38 in, so even the *lower* target
requires `0.08 + 0.38 + 0.08 = 0.54 in`. **0.54 > 0.4583.** No arrangement meets even 0.08 in on both
sides without either shrinking `Kembali` (forbidden — it was enlarged by approval in v0.2) or
shortening the panel. The panel was shortened.

```
R-NAVSTRIP   NAV_CLR = 0.10
             NAV_H   = NAV_CLR + KEMBALI_H + NAV_CLR = 0.58
             PANEL_H = (7.5 − NAV_H) − PANEL_Y       = 5.1387
             KEMBALI_Y = (7.5 − NAV_H) + NAV_CLR     = 7.02
```

| Quantity | v0.2 | **v0.3** |
|---|---:|---:|
| Panel height | 5.2604 | **5.1387** (−0.1217) |
| Panel bottom | 7.0417 | **6.92** |
| Reserved navigation strip | — | **0.58 in**, 6.92 → 7.5 |
| Clearance **above** `Kembali` | 0.0333 | **0.10** |
| `Kembali` | 1.55 × 0.38 @ 16 pt, y 7.075 | 1.55 × 0.38 @ 16 pt, **y 7.02** — size unchanged |
| Clearance **below** `Kembali` | 0.045 | **0.10** |
| Panel **width** | 5.8621 | **5.8621 — unchanged** |
| **S17 ÷ S12 width ratio** | 2.0009× | **2.0009× — preserved** |
| Body bottom vs panel bottom | 6.4302 / 7.0417 | 6.4302 / **6.92** — slack 0.4898, body untouched |

Both clearances land at **0.10**, the top of the requested 0.08–0.10 range.

**⚠️ A new, bounded departure from canon.** Canonical panel height is 5.2604 — the same as Rumusan's.
v0.3 makes S12's panel **5.1387**, so the reveal-child now differs from Rumusan in *height* as well as
width. This was not previously true and is recorded as a deliberate consequence of reserving the strip.
It is bounded to height; width, and therefore the archetype ratio, is untouched. It arguably increases
archetype separation, but it is a departure and is not presented as an improvement.

**The strip is reserved geometry, not a drawn band.** No new visible shape was added — that would
exceed "one bounded correction". If a visible navigation band is wanted, say so; it is a small
addition to `R-NAVSTRIP`.

**Complete diff v0.2 → v0.3** — three changes, all on S12, verified shape-by-shape:

| Shape | Change |
|---|---|
| `Rectangle 9` (panel) | height 5.2604 → 5.1387. `x`, `y`, **width** unchanged |
| `TextBox 19` (`Kembali`) | `y` 7.075 → 7.02. Width, height, size, centring unchanged |
| `Rectangle 8` (off-canvas note) | one documentation line added recording the strip |

**Unchanged and verified:** all three notes bodies byte-identical (474 / 443 / 622 ch) · S04 entirely
untouched (card geometry, labels, instruction) · S17 entirely untouched (Rumusan heading, body,
spacing) · all display and VO content · locators · italic lexicon.

### Revision history

| rev | file | bytes | sha256 | change |
|---|---|---:|---|---|
| **v0.1** | `…_v0_1.pptx` | 35,390 | `2b756e5b…e91862` | initial 3-screen build. Preserved unmodified. |
| **v0.2** | `…_v0_2.pptx` | 35,528 | `ae16fcfd…09a2df` | legibility only — contrast, label size, `Kembali` size, S17 spacing. Preserved unmodified. |
| **v0.3** | `…_v0_3.pptx` | 35,593 | `ebf0eb8a…8bf3e1c` | **navigation strip only** — S12 panel height and `Kembali` position. No content, VO, card geometry or Rumusan change. |

### What changed in v0.2

Five instructions, all presentation. **Treatment logic is untouched** — same archetypes, same rules,
same content, same locators, same italic lexicon, same no-narrator-prefix, same source forms.

| # | Instruction | Change | Was → Now |
|---:|---|---|---|
| 1 | *darken placeholder text / tambah contrast* | Placeholder runs in card and panel shapes given an explicit dark fill (`tx1` @ `lumMod 85000`) | Inherited `<p:style><a:fontRef><a:schemeClr val="lt1"/>` — **light text on a light tint**. That was the cause, and it is now overridden at run level. |
| 2 | *besarkan label card sedikit* | Card label box and type enlarged | `3.0323 × 0.4364 @ 18 pt` → **`3.6202 × 0.50 @ 20 pt`** (label ratio 0.7706 → 0.92 of card width) |
| 3 | *besarkan / tebalkan Kembali* | Control enlarged; already bold, kept bold | `1.3277 × 0.3366 @ 14 pt` → **`1.55 × 0.38 @ 16 pt`**, still exact-centred (6.6667) |
| 4 | *beri S17 sedikit spacing tambahan* | `spcBef` 6 pt on all four Rumusan bullets; heading raised and body given more room | heading `4.2 / 0.42` → **`3.92 / 0.45`**; body `4.7011 / 2.2215` → **`4.45 / 2.55`** |
| 5 | *jangan ubah treatment logic* | Nothing in §3–§5 below changed | S12/S17 panel ratio still **2.0009×** |

**Knock-on geometry, recomputed rather than nudged.** The taller label forced the row pitch to absorb
it: `GAP_Y` 0.3644 → **0.25**, `ROW_PITCH` 2.8094 → **2.7586**, row 2 top 4.7532 → **4.7024**. Lowest
label bottom 7.211, leaving a **0.289 in** stage margin. Label centring is still exact — `R-LABEL-X`
holds, deltas **0.0000** on all four cards.

**`Kembali` clearance is the tightest constraint in the deck.** Below the panel there are only
0.4583 in before the stage edge. At 16 pt the box needs 0.38 in, so the gap to the panel narrows
0.0592 → **0.0333** and the stage clearance lands at **0.045 in**. The control could not grow further
without either shortening the canonical panel or moving `Kembali` inside it — both of which would be
treatment changes, so neither was done.

**One defect found and fixed during v0.2.** The first build left the S17 heading at `y = 4.2` while the
body moved to `4.45`, giving a **−0.17 in overlap**. Corrected to `y = 3.92`, gap now **+0.08 in**.

**Scope: three screens, not nineteen.** S04, S12, S17 — the three `VERIFIED_SOURCE` screens that carry
one archetype each. S09 is `VERIFIED_SOURCE` too but was excluded: it adds tick geometry without adding
an archetype.

---

## 1. Screen-to-source mapping

| Preflight # | Screen | Source part (probe v0.1) | Archetype | Layout | Notes | Status |
|---|---|---|---|---|---|---|
| 1 | **S04** | `slide4.xml` + `notesSlide4.xml` | CR_BASE — **4-card** | `Blank` | 474 ch | `VERIFIED_SOURCE` |
| 2 | **S12** | `slide12.xml` + `notesSlide16.xml` | FULL — **split-STATE** | `Blank` | 443 ch | `VERIFIED_SOURCE` |
| 3 | **S17** | `slide17.xml` + `notesSlide12.xml` | **RUMUSAN** | `Title and Content` | 622 ch | `VERIFIED_SOURCE` |

**Not built:** S01–S03, S05–S11, S13–S16, S18, S19. Sixteen screens, of which four are
`MISSING_SOURCE` and eleven `PARTIAL_SOURCE` (`SOURCE_CUSTODY_AND_COVERAGE.md`).

## 2. Package derivation

Built by **direct OOXML assembly** from probe v0.1 as structural donor, so the preflight sits in the
same visual family by construction rather than by imitation. Carried over unchanged: `slideMaster1`,
`slideLayout1–7`, `theme1`, `theme2`, `notesMaster1`, `presProps`, `viewProps`, `tableStyles`.

**Deliberately excluded** — per the standing recommendation against reinjecting residue:

| Excluded | Reason |
|---|---|
| `ppt/tags/tag1.xml` (23 iSpring tags) | describes PL06 T3 B2 with 14 dangling slide GUIDs, a foreign SCORM course ID and an LRS endpoint |
| `ppt/changesInfos/changesInfo1.xml` | 206 records, `sldId` 8000–8051, matching neither deck |
| `ppt/revisionInfo.xml` | one client's save counter |
| `ppt/media/image3.svg` | tick icon — S09 not built |
| `p:custDataLst` in `presentation.xml` | the tag-block binding |

Verified absent in the output: **zero** residue parts, **zero** orphan content-type overrides.

## 3. Interaction ontology applied

```
CLICK_REVEAL
  trigger component : CARD          (S04)
  reveal mode       : FULL_SLIDE    (S12)  → detail-screen-kembali
```

`FULL_SLIDE` is not a new token: it maps to `interaction-patterns-v0.md` §3.2 variant
**`detail-screen-kembali`**, which has precedent (sample cementitious 16/06). The POP UP anti-drift
guardrail is satisfied by **pre-existing** provenance, not by an assumption of this build — probe v0.1
S04 states the choice in the negative: `Klik hotspot -> reveal full-slide, bukan pop up.`
`POPUP` is never selected; both its realisations are DEFERRED. No `DRAG_DROP` pattern is exercised.

## 4. Per-screen construction

### S04 — four-card base

Geometry derived from **rules**, not copied coordinates:

```
CARD_W 3.935 · CARD_H 1.9901 · GAP_X 0.7074 · GAP_Y 0.25          ← v0.2
LABEL_W = CARD_W × 0.92 = 3.6202 · LABEL_H 0.50 · LABEL_GAP 0.0185  ← v0.2
ROW_PITCH = CARD_H + LABEL_GAP + LABEL_H + GAP_Y = 2.7586
R-GRID-X   GRID_X0 = (13.3333 − (2·CARD_W + GAP_X))/2 = 2.3779
R-LABEL-X  LABEL_X = CARD_X + (CARD_W − LABEL_W)/2
R-INSTR    INSTR_W = 2·CARD_W + GAP_X = 8.5774 ; INSTR_X = GRID_X0
```

| Element | Value |
|---|---|
| Cards | (2.3779, 1.9438) (7.0203, 1.9438) (2.3779, **4.7024**) (7.0203, **4.7024**), each 3.935 × 1.9901 |
| Labels | (**2.5354** / **7.1778**) × (3.9524 / **6.7110**), each **3.6202 × 0.50 @ 20 pt** |
| Placeholder text | explicit dark fill — `tx1` @ `lumMod 85000` |
| Instruction | (2.3779, 1.2936) 8.5774 × 0.4039 |
| Locator | `K5PL06T03-B02-IMG-01, ms 237` — correct for Struktur Taman |

**Defects corrected against the reviewed deck:**

| Ref | Fix |
|---|---|
| `R-LABEL-X` | Label-to-card centring delta **0.0000 on all four** (measured deck: ±0.09725 mirror error) |
| `R-GRID-X` | Grid centred; margins symmetric (measured deck: 0.05725 left of centre) |
| `P-02` | Card 2 reads `Visual: Struktur Teduhan` (measured deck: `Struktur Persisir Teduhan`) |
| `P-10` | Instruction width 8.5774 → ≈ 67–72 chars capacity for a 49-char string (inherited 6.3367 gave 0–4 chars headroom) |
| `P-09` | Each label emitted after its own card |

**Display treatment.** Four card labels + instruction. The probe's intro line
`Empat jenis struktur taman.` is **not** on the canvas — its proposition is carried in the VO
(`Terdapat empat jenis struktur taman: …`) and the four types are visible as labels. Concise display,
full VO, zero proposition loss.

### S12 — split-STATE detail, actual Papan Tanda source

Canonical geometry from probe S12 (= canon slide 6), restored:

| Element | Value |
|---|---|
| Visual panel | (0.8046, 1.7813) **5.8621 × 5.1387** — width 43.97 % of stage; height shortened in v0.3 for the nav strip |
| **Body heading box** | (6.8667, 1.8291) 5.6621 × 0.5068 — **restored** |
| Body | (6.8667, 2.5594) 5.6621 × 3.8708 |
| Panel placeholder text | explicit dark fill — `tx1` @ `lumMod 85000` |
| Navigation strip | **6.92 → 7.5**, 0.58 in reserved (`R-NAVSTRIP`) |
| `Kembali` | (**5.8917, 7.02**) **1.55 × 0.38 @ 16 pt bold** — centre **6.6667**; clearance **0.10 / 0.10** |
| Locator | **`K5PL06T03-B02-IMG-05, ms 243`** |

**Departure from the reviewed deck, recorded:** the review widened this panel to 11.7371 — within
0.0079 in of the Rumusan panel — and deleted the heading box (`sp10 del @22:52:53`). The preflight
reverts both, implementing `K5-DR-060`, an **unratified CAIR recommendation**. Measured outcome:
S17 panel ÷ S12 panel = **2.0009×**, matching the canonical ratio exactly.

`P-01` applied: locator `IMG-05` / ms 243. **No `IMG-01` or `237` appears on this screen.**

**Display treatment.** Source's 4 sentences (346 ch) → 8 bullets across 2 levels, subject/copula/
relativiser elided, terminal punctuation removed, the inline list exploded into 4 sub-bullets. All 4
propositions retained; zero content words dropped; zero tokens added.
Rendered load **10 lines** against a **12.57-line** box — 2 lines of headroom, deliberately tighter
than the full-width 8/8 the review left with none.

**VO.** Probe `notesSlide16` body **verbatim**, `Hilmi: Papan Tanda.` replaced by the section label
`Perabot Taman`. All four source sentences intact.

### S17 — revised Rumusan

| Element | Value |
|---|---|
| Panel | (0.7917, 1.7812) 11.7292 × 5.2604 |
| Heading box | (0.8125, 4.2) 11.7083 × 0.42 — bold, separate |
| Body | (0.8125, 4.7011) 11.7292 × 2.2215 — 4 bullets |

Rules applied:

| Rule | Applied |
|---|---|
| Suppress `Kepentingan` / `Isi Utama` / `Manfaat` | all four label forms absent from display **and** VO |
| `kontraktor`, not `anda` | display and VO both read `Kontraktor` / `kontraktor`; zero `anda` |
| Benefit → industry application | `Kontraktor dapat merancang, melaksana dan menyelenggara … di tapak` — **drafted by judgement**, not mechanically verifiable |
| English terms italic | `Water Feature`, `Drinking Fountain`, `BBQ pit` |
| `P-03` | **`BBQ pit`** — source form, lowercase `p` |
| `P-04` | `dan` lowercase in the heading |
| `P-05` | em dash `—` restored in the heading |
| `P-06`, `P-07` | revision followed — no terminal punctuation; structural rewording retained |

**VO.** Bariah's fuller revised form, with `BBQ pit` in source case and no narrator prefix — including
the framing clause `Dengan memahami komponen-komponen ini,` that the display deliberately omits. That
asymmetry is the concise-display / full-VO principle, visible in one screen.

## 5. Cast and narrator

**No scenario character appears anywhere in the preflight** — verified: zero occurrences of `Haziq`,
`Roslan`, `Alya`, `Rahman`, `Fahmi`, `Aril`. None of the three screens is a scenario screen, so the
unprovable-cast question (`A-13`) is not exercised.

**`Hilmi` appears nowhere either** — zero tokens in all three VO bodies. All three are routine learning
screens; the narrator is not re-identified on them. S03, the screen that may visually introduce him, is
not built.

## 6. What this preflight does not do

Does not generate 19 slides · does not construct content for any `MISSING_SOURCE` screen · does not
build S09, S10 or S16 (so the 5-card 3+2 family and tick geometry are untested) · does not bind any
image (none exists) · does not modify the live CAIR desk · does not unlock K5 · does not patch any
database or authority schema · does not issue a canonical decision ID · does not merge.

## 7. Why it cannot be promoted

Not regenerable — no packet binding, compiler path or skeleton geometry produces it; it was assembled
from a donor package against a hand-derived parameter sheet. Not authoritative — 3 of 19 screens, and
the two most contested assumptions (`A-05` split-STATE revert, `A-04` five-card) are respectively
**shown once** and **not shown at all**. No manifest, digest pin or baseline was issued. K5 remains
locked, so no ratification path exists for it.

## 8. The open question

S12 is built here to canonical split-STATE while the reviewed deck made it full-width. **Rendering S12
beside S17 is the point**: if the reveal-child still reads as a different thing from the summary, the
revert is right; if it reads as a foreign deck, `A-05` is wrong and 9 screens change. Either answer
closes a question open since 16/06 that no artifact has ever been able to answer, because nothing has
ever been seen rendered.
