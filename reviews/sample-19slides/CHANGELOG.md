# CHANGELOG — K5 PL06 T3 B02 visual treatment

All artifacts are **output-only and disposable**. None is CAIR-ratified or production-authorised.
Every revision is preserved; none is overwritten.

---

## 19-slide visual treatment sample

### v0.1 — 2026-07-31
`K5PL06T03B02_19SLIDE_VISUAL_TREATMENT_SAMPLE_v0_1.pptx` · 84,253 B · `sha256 5e35198a…3ac7b5bf`

First 19-screen build. Propagates the approved preflight v0.3 geometry.

**Propagated**
- split-STATE to all **9** detail screens (S05–S08, S11–S15): panel 5.8621 × 5.1387, heading box,
  body, reserved 0.58 in navigation strip
- exactly **one** `Kembali` per detail screen, 0.10 in clearance above and below, centred 6.6667
- S04 Card geometry: 4 cards 3.935 × 1.9901, labels 3.6202 × 0.50 @ 20 pt, exact centring,
  grid-width instruction
- S17 Rumusan treatment: labels suppressed, `kontraktor`, italic lexicon, `BBQ pit` source form,
  em dash, lowercase `dan`, 6 pt bullet spacing
- 5-card 3 + 2 (option 5B) to S10/S16; `visited-tick` to S09 (×4) and S16 (×5)

**Source honesty**
- 4 `VERIFIED` · 11 `PARTIAL` · 4 `MISSING`
- all 15 non-verified screens carry `SOURCE PENDING` on canvas; the 4 verified do not
- no factual content, VO, quiz item, answer key or routing invented anywhere
- S18 has **no** quiz content of any kind

**Build decisions**
- ticks redrawn as native `a:custGeom` instead of the probe's SVG blip, which has no raster fallback
  and an unverified render history
- S10/S16 instruction line marked pending rather than copied from S04

**Checks** — 9/9 package, 25/25 rules, all executed.

---

## 3-screen implementation preflight

### v0.3 — navigation strip *(approved)*
`…_PREFLIGHT_v0_3.pptx` · 35,593 B · `sha256 ebf0eb8a…8bf3e1c`

One bounded correction on S12. `R-NAVSTRIP` reserves 0.58 in below the panel; clearance 0.0333/0.045
→ **0.10/0.10**. Panel height 5.2604 → 5.1387; **width unchanged**, ratio preserved at 2.0009×.
`Kembali` size unchanged, `y` 7.075 → 7.02.

Shortening the panel was **forced**: only 0.4583 in exists below it and 0.08 + 0.38 + 0.08 = 0.54.

*Recorded departure* — canonical panel height 5.2604 matched Rumusan; S12 is now 5.1387, so the
reveal-child differs in height as well as width. Bounded to height.

*Validation count corrected* — v0.1 reported 13/13 but executed 12; the `POPUP` row was hand-asserted
in the table, never run. v0.2 reported 12/12, accurate but silently dropped it. v0.3 made it a real
check (exactly one `Kembali`, strictly below the panel) and added four strip checks → **17/17 executed**.

### v0.2 — legibility *(approved)*
`…_PREFLIGHT_v0_2.pptx` · 35,528 B · `sha256 ae16fcfd…09a2df`

Placeholder contrast (root cause: card style `fontRef → lt1`, light text on a light tint) ·
card labels 3.0323 × 0.4364 @ 18 pt → 3.6202 × 0.50 @ 20 pt · `Kembali` 14 → 16 pt in a larger box ·
S17 `spcBef` 6 pt and repositioned heading/body. `GAP_Y` 0.3644 → 0.25 recomputed, not nudged.
No treatment logic changed.

*Defect found and fixed in-revision* — first build left the S17 heading overlapping the body by
0.17 in.

### v0.1 — initial
`…_PREFLIGHT_v0_1.pptx` · 35,390 B · `sha256 2b756e5b…e91862`

Three screens (S04, S12, S17) assembled by direct OOXML from probe v0.1 as structural donor.
iSpring tags, `changesInfo`, `revisionInfo` and `custDataLst` excluded.

*Defects found and fixed in-revision* — duplicate shape ID on S04; three dangling notes→slide
back-relationships.

---

## Corrections carried in from the gate round

| # | Was | Now | Basis |
|---|---|---|---|
| cast | "limited to `Haziq` + `Encik Roslan`" | **role-neutral placeholders**; current B02 cast **not provable** | bank undated and scope-less; casting prompt allowed `baru`; zero evidence for any named cast in B02 material |
| S03 narrator | framed as an unresolved contradiction | **resolved by interpretation** — S03 may visually introduce the narrator; routine VO carries no prefix | no evidence Bariah required a literal `Hilmi:` on S03 |

---

## Standing constraints — held in every revision

K5 not unlocked · live CAIR desk not altered · no compiler, database or authority schema patched ·
no canonical decision ID issued · no manifest, digest pin, baseline or freeze · not merged ·
both evidence packages (`ee4f5479…8bb9e7`, `24dcaa04…1d471c`) re-hashed unchanged after every build.
