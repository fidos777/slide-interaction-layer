# PREFLIGHT_VALIDATION — v0.2

Measured on the delivered file.
`sha256 ae16fcfd31200a3681785d1d970e236dc05624292ecf178076ddb44ff109a2df` · `md5 9935e17397ec563c99a6f0a1fd57a0ae` · 35,528 B

v0.1 (`2b756e5b…e91862`, 35,390 B) is preserved unmodified and re-hashed after the v0.2 build.

## 0. v0.2 — legibility revision

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
