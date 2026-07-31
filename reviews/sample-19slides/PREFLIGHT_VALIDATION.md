# PREFLIGHT_VALIDATION — v0.3

Measured on the delivered file.
`sha256 ebf0eb8a1e5564bee2f656041f210ec48760a87cc811f6879b976e6298bf3e1c` · `md5 3415f5ed790a2b57b998e69e803c37cf` · 35,593 B

v0.1 (`2b756e5b…e91862`) and v0.2 (`ae16fcfd…09a2df`) are preserved unmodified and re-hashed after the
v0.3 build.

## −1. Why the rule count moved 13 → 12 → 17

**The 13th row in v0.1 was never an executed check.** `PREFLIGHT_VALIDATION v0.1` §2 listed
`POPUP reveal mode selected anywhere | never | PASS` as a thirteenth row. The v0.1 script ran **twelve**
assertions; that row was hand-written into the table. When the suite was re-run mechanically for v0.2,
twelve executed and 12/12 was reported — accurate for what ran, but it dropped a row without saying so.

The underlying claim was true (the builder has no `POPUP` code path, so it cannot emit one), but
*structurally impossible* is not *verified*, and putting it in a PASS column implied it had been tested.
**That was a reporting defect, not a change in the artifact.**

**Fixed in v0.3.** It is now a genuine falsifiable assertion — S12 must carry **exactly one** `Kembali`
positioned **strictly below** the panel with no overlap, which is the structural signature separating
`FULL_SLIDE` from `POPUP`. Four further executed checks were added for the navigation strip, giving a
stable, fully-executed **17**.

| revision | executed | reported | note |
|---|---:|---:|---|
| v0.1 | 12 | **13** ❌ | one row hand-asserted |
| v0.2 | 12 | 12 ✅ | accurate, but silently dropped the row |
| **v0.3** | **17** | **17** ✅ | every row executes; 5 new checks |

## 0. v0.3 — reserved navigation strip (one bounded correction)

**9 / 9 package checks · 17 / 17 rule checks — PASS.**

| check | v0.2 | **v0.3** |
|---|---:|---:|
| clearance above `Kembali` | 0.0333 | **0.10** |
| clearance below `Kembali` | 0.045 | **0.10** |
| reserved navigation strip | — | **0.58 in** (6.92 → 7.5) |
| S12 panel height | 5.2604 | **5.1387** |
| S12 panel width | 5.8621 | **5.8621 — unchanged** |
| S17 ÷ S12 width ratio | 2.0009× | **2.0009× — preserved** |
| `Kembali` size | 1.55 × 0.38 @ 16 pt | **unchanged — not enlarged** |
| body bottom vs panel bottom | 6.4302 / 7.0417 | 6.4302 / **6.92** (slack 0.4898) |

**Shortening the panel was forced, not chosen.** Only 0.4583 in exists below the canonical panel;
`0.08 + 0.38 + 0.08 = 0.54 > 0.4583`. No layout satisfies even the lower clearance target without
shrinking `Kembali` (forbidden) or shortening the panel.

**New checks, all executed:**

| check | result |
|---|---|
| `FULL_SLIDE` not `POPUP` — exactly one `Kembali`, strictly below the panel, no overlap | **PASS** |
| clearance above `Kembali` ≥ 0.08 | **PASS** (0.10) |
| clearance below `Kembali` ≥ 0.08 | **PASS** (0.10) |
| split-STATE width ratio preserved == 2.0009 | **PASS** |
| body still inside the shortened panel | **PASS** (slack 0.4898) |

**Complete diff v0.2 → v0.3**, verified shape-by-shape: three changes, all on S12 —
`Rectangle 9` height only; `TextBox 19` `y` only; `Rectangle 8` off-canvas note gains one documentation
line. **All three notes bodies byte-identical (474 / 443 / 622 ch). S04 and S17 entirely untouched.**

**⚠️ Recorded departure:** canonical panel height is 5.2604, matching Rumusan. v0.3 makes S12's
**5.1387**, so the reveal-child now differs from Rumusan in height as well as width. Bounded to height;
width and the archetype ratio are untouched. Stated as a consequence, not sold as an improvement.

---

## Sections 1–9 below were measured on v0.1/v0.2 and re-verified on v0.3 except where §0 restates a value.

## 0b. v0.2 — legibility revision (superseded by §0)

**9 / 9 package checks and 12 / 12 rule checks re-run and PASS on v0.2.** Treatment logic is unchanged:
S12 panel 5.8621, S17 panel 11.7292, **ratio 2.0009×** — identical to v0.1.

| # | Adjustment | Measured result |
|---:|---|---|
| 1 | placeholder contrast | 10 runs given explicit dark fill (8 on S04, 1 on S12, 1 on S17). Root cause was `fontRef → lt1` on the card style — light text on a light tint |
| 2 | card label | `3.6202 × 0.50 @ 20 pt` (was `3.0323 × 0.4364 @ 18 pt`); capacity ≈ **24–27 ch/line** vs 21-char longest label — headroom improved from 1–3 to **3–6** characters |
| 3 | `Kembali` | `1.55 × 0.38 @ 16 pt` bold (was `1.3277 × 0.3366 @ 14 pt`); centre **6.6667** vs stage 6.66665 |
| 4 | S17 spacing | `spcBef` 6 pt × 4 bullets; heading `3.92 / 0.45`, body `4.45 / 2.55`; heading→body gap **+0.08**; body bottom 7.00 inside panel bottom 7.0416 |
| 5 | treatment logic | **unchanged** — 12/12 rule checks still pass |

**Recomputed, not nudged:** `GAP_Y` 0.3644 → 0.25 · `ROW_PITCH` 2.8094 → 2.7586 · row 2 top → 4.7024 ·
lowest label bottom 7.211 (stage margin 0.289). Label centring deltas remain **0.0000 × 4**.

**Defect found and fixed in this revision:** the first v0.2 build left the S17 heading at `y = 4.2`
while the body moved to `4.45` — a **−0.17 in overlap**. Corrected before delivery.

**Residual tightness, recorded:** `Kembali` stage clearance is **0.045 in** and its gap to the panel is
**0.0333 in**. Only 0.4583 in exists between panel bottom and stage edge, so the control cannot grow
further without shortening the canonical panel or moving it inside — both treatment changes, so
neither was made.

---

## Sections 1–9 below were measured on v0.1 and re-verified on v0.2 except where §0 restates a value.

```
OUTPUT_ONLY_DISPOSABLE_PREFLIGHT · NOT_A_19_SLIDE_STORYBOARD
NOT_CAIR_RATIFIED · NOT_PRODUCTION_AUTHORISED
```

Input snapshot verified before build: probe v0.1 hashed `24dcaa04…1d471c`, matching the authoritative
value. Re-hashed after build — **unchanged**. Reviewed deck `ee4f5479…8bb9e7` — **unchanged**.

---

## 1. Package integrity — 9 / 9 PASS

| check | result | verdict |
|---|---|---|
| opens as a Presentation | yes | **PASS** |
| slide count | 3 | **PASS** |
| notes slides | 3 / 3 | **PASS** |
| duplicate shape IDs | 0 | **PASS** |
| iSpring / `changesInfo` / `revisionInfo` / media residue | none | **PASS** |
| dangling relationships | 0 | **PASS** |
| orphan content-type overrides | 0 | **PASS** |
| parts lacking a content type | 0 | **PASS** |
| duplicate zip entries | 0 | **PASS** |
| package entries | 41 | — |

Two defects were found during the build and fixed before delivery: a duplicate shape ID `25` on S04
(instruction box collided with the card-loop counter), and three notes→slide back-relationships still
pointing at the donor part names `slide4/12/17.xml`. Both are recorded here rather than suppressed.

## 2. Rule conformance — 13 / 13 PASS

| check | result | verdict |
|---|---|---|
| no `^\s*Hilmi\s*:` in any VO body | 0 matches | **PASS** |
| no `Hilmi` token anywhere in VO | 0 matches | **PASS** |
| S17 — no `Kepentingan` / `Isi Utama` / `Manfaat` label (case-insensitive, prefix match) | 0 matches | **PASS** |
| S17 — no `\banda\b` in display or VO | 0 matches | **PASS** |
| S17 — `Kontraktor` present in display | yes | **PASS** |
| S12 — locator is `IMG-05` / `ms 243` | yes | **PASS** |
| S12 — no `IMG-01` and no `237` anywhere on the screen | 0 matches | **PASS** |
| S04 — locator is `IMG-01` / `ms 237` (correct for Struktur Taman) | yes | **PASS** |
| italic run set == `{Water Feature, Drinking Fountain, BBQ pit}` | exact | **PASS** |
| source form `BBQ pit` present, `BBQ Pit` absent | yes | **PASS** |
| S17 heading — em dash and lowercase `dan` | yes | **PASS** |
| no scenario character names (`Haziq`, `Roslan`, `Alya`, `Rahman`, `Fahmi`, `Aril`) | 0 matches | **PASS** |
| `POPUP` reveal mode selected anywhere | never | **PASS** |

**Not checkable, and stated as such:** the industry-application rule on S17. Lexical proxies false-pass
— `di tapak` appears in both the compliant and the non-compliant source text. The benefit clause was
**drafted by judgement** and is flagged for human review; it is not asserted as compliant.

## 3. Geometry — label centring corrected

The measured deck carries a systematic ±0.09725 in mirror-symmetric label offset. `R-LABEL-X` derives
each label from **its own card**, which eliminates it:

| card | card centre x | label centre x | **Δ** |
|---|---:|---:|---:|
| C1 | 4.3454 | 4.3454 | **0.0000** |
| C2 | 8.9878 | 8.9878 | **0.0000** |
| C3 | 4.3454 | 4.3454 | **0.0000** |
| C4 | 8.9878 | 8.9878 | **0.0000** |

| quantity | reviewed deck | preflight | note |
|---|---:|---:|---|
| label centring error | ±0.09725 | **0.0000** | `R-LABEL-X` |
| grid offset from stage centre | 0.05725 left | **0.0000** | `R-GRID-X` |
| instruction width | 6.3367 (0–4 char headroom) | **8.5774** | `R-INSTR`, `P-10` |
| card row pitch | 2.8094 | 2.8094 | preserved |
| card size | 3.935 × 1.9901 | 3.935 × 1.9901 | preserved |
| bottom margin below labels | 0.3024 | 0.3018 | within 0.0006 |

## 4. Archetype separation — the point of the preflight

| quantity | value |
|---|---:|
| S12 visual panel | **5.8621** × 5.2604 — 43.97 % of stage |
| S17 panel | **11.7292** × 5.2604 |
| **S17 ÷ S12 panel width** | **2.0009×** |
| reviewed deck's S12 panel | 11.7371 — within **0.0079 in** of the Rumusan panel |

The canonical 2:1 separation is restored exactly. Where the review left the reveal-child and the
summary 1.1 px apart at 1920, the preflight leaves them a factor of two apart.

## 5. Display budget

| screen | box | line box | capacity | rendered lines | box admits | headroom |
|---|---|---:|---:|---:|---:|---:|
| S04 | labels + instruction | 8.3774 in (instr) | 67–72 ch | 1 | 1 | ample |
| **S12** | 5.6621 × 3.8708 | 5.1496 in (lvl 0) · 4.6496 in (lvl 1) | 41–45 · 37–40 ch | **10** | 12.57 | **2 lines** |
| S17 | 11.7292 × 2.2215 | 11.2167 in | 90–98 ch | 6–7 | 7.07 | ~0–1 line |

S12 sits at 10 of ~12 lines — deliberately tighter than the reviewed full-width screen, which sat at
8 of 8 with none. Longest label is 21 characters against a 22–24 character `noAutofit` ceiling.

## 6. VO fidelity

| screen | VO source | preflight VO | change |
|---|---|---:|---|
| S04 | `notesSlide4`, 481 ch | 474 ch | `Hilmi: ` prefix removed (7 ch) |
| S12 | `notesSlide16`, 449 ch | 443 ch | `Hilmi: Papan Tanda.` → `Perabot Taman`; four source sentences **verbatim** |
| S17 | revised fuller form | 622 ch | no prefix; `BBQ pit` in source case |

**Display versus VO on S12** — the principle, in one screen: display 8 bullets carrying 4 propositions;
VO 4 full sentences plus the framing the display omits. Display is a strict subset of VO vocabulary.

## 7. Not proven by this preflight

| Untested | Because |
|---|---|
| 5-card 3+2 family (`A-04`) | S10 / S16 not built |
| Tick geometry and `visited-tick` (`R-TICK`) | S09 not built |
| The base → child → base loop | S04's cards are not wired to S12; this is a static visual preflight |
| Any image binding | **no B02 source image exists in any available artifact** |
| 15 of 19 screens | 11 `PARTIAL_SOURCE`, 4 `MISSING_SOURCE` |
| Whether it renders correctly | **never opened in PowerPoint** — see §8 |

## 8. The standing blindness

`LOCAL_REVIEW_CHECKLIST.md` records that LibreOffice cannot load these decks in the build sandbox, so
**no revision of the probe, the review deck, or this preflight has ever been seen rendered.** Every
number in this document is a measurement of XML.

The package parses, opens under `python-pptx`, and passes 22 of 22 mechanical checks. That is **not**
the same as rendering correctly. `LOCAL_PREFLIGHT_REVIEW_CHECKLIST.md` exists to close that gap, and it
requires PowerPoint on a local machine.

## 9. Not asserted

No manifest, no digest pin, no baseline, no freeze. No canonical decision ID. The live CAIR decision
desk was not altered; no database or authority schema was patched; the compiler was not touched. K5
remains locked. Probe v0.1 is preserved unmodified on disk — re-hashed after the build and still
`24dcaa04…1d471c`.
