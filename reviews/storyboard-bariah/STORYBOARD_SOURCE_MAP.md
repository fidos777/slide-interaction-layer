# STORYBOARD_SOURCE_MAP — K5 PL06 T03 B02

```
STORYBOARD_REVIEW_DRAFT · SOURCE_BOUND_TEXT · VISUALS_NOT_EMBEDDED
MULTIMEDIA_NOT_PRODUCED · PENDING_BARIAH_APPROVAL · NOT_FOR_MMD_BUILD
```

Per-screen trace: what each screen says, where it came from, and what is proposed rather than sourced.

**Page convention.** `ms` = module page as printed. Physical PDF page = module page **+ 19**, constant
across all 14 pages of the extracted range. Both are given.

**Authority split.** DOCX = text-extraction authority. Rendered PDF = pagination and visual authority.

---

## 1. Sources

| Source | Identifier | Governs |
|---|---|---|
| Module DOCX | `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx`, 16,832,861 B | display and VO text |
| Module PDF | `K5_PL06_T03_B02_pages_256269.pdf`, `sha256 30a6903d…f828a3f4`, 429,918 B, 14 pp | page numbers, headings, images |
| Probe v0.1 | `K5PL06T03B02_TREATMENT_PROBE_4SLIDES…`, `sha256 24dcaa04…9dbac1d471c` | S04, S09, S12, S17 verbatim text; locators |
| Reviewed deck | `BARIAH_REVIEW_8SLIDES.pptx`, `sha256 ee4f5479…7fced8bb9e7` | SME edits — evidence only |
| Accepted sample | `…19SLIDE_VISUAL_TREATMENT_SAMPLE_v0_2.pptx`, `sha256 8d93e2ce…646a982b` | **structural donor only** |

All five were read only. None was modified — the accepted sample's hash was re-verified after the build.

---

## 2. Section map — measured, not interpolated

| Rendered no. | Heading | ms | phys | Screen | Assets |
|---|---|---:|---:|---|---:|
| `3.3.` | Struktur Taman | 237 | 256 | **S04** base | 0 |
| `3.3.1` | Struktur Persisir Air | 238 | 257 | **S05** | 1 |
| `3.3.2` | Struktur Teduhan | 239 | 258 | **S06** | 1 |
| `3.3.3` | Kemudahan Awam | 240 | 259 | **S07** | **0** |
| `3.3.4` | Water Feature | 241 | 260 | **S08** | **0** |
| `3.4.` | Perabot Taman | 242 | 261 | **S10** base | 0 |
| `3.4.1` ⚠ | Kerusi Taman | 242 | 261 | **S11** | 3 |
| `3.4.1` ⚠ | Papan Tanda | 243 | 262 | **S12** | 2 |
| `3.4.1` ⚠ | Tong Sampah | 245 | 264 | **S13** | 4 |
| `3.4.2` | Drinking Fountain | 247 | 266 | **S14** | 2 |
| `3.4.3` | BBQ pit | 249 | 268 | **S15** | 1 |

⚠ The number `3.4.1` is used three times in the module. Screens are keyed by heading **title**, which is
unique, so the collision does not affect the mapping.

**One locator was vindicated by this measurement.** The probe's `K5PL06T03-B02-IMG-05, ms 243` for S12 is
exact — `3.4.1 Papan Tanda` renders on module 243. An earlier DOCX-based interpolation had estimated
~244 and was wrong by one page. The probe was right; the estimate was not.

---

## 3. Per-screen trace

Legend — **Display / VO origin**:
`SOURCE` = derived from module text · `MEASURED` = strings measured from the probe ·
`PROPOSED` = written for this storyboard, not present in the module · `DRAFT` = constructed assessment
content.

### S01 — TAJUK

| | |
|---|---|
| Display | `SOURCE` — course and topic strings, verbatim in all four probe notes headers |
| VO | `PROPOSED` — welcome line; no module page carries opening narration |
| Visual | `[Visual: Imej pembuka bahagian…]` — no module image exists for a title screen |
| Module page | none — title screen has no source page |
| Decision | `SOURCE_BOUND_TEXT` (strings) / `PROPOSED_FOR_BARIAH_REVIEW` (visual, VO) |

### S02 — DIALOG

| | |
|---|---|
| Display | `PROPOSED` — five-turn dialogue, role-neutral `[PELATIH]` / `[PENYELIA TAPAK]` |
| VO | `PROPOSED` — the dialogue itself |
| Visual | `[Visual: Latar tapak landskap dalam pembinaan…]` |
| Module page | premise derived from ms 237 and ms 242; **the lines are written, not transcribed** |
| Decision | `PROPOSED_FOR_BARIAH_REVIEW` — `D-01`. Desk slot `(K5, PL06, s02)` is empty |

### S03 — GAMBARAN KESELURUHAN

| | |
|---|---|
| Display | `PROPOSED` — narrator card + four overview lines |
| VO | `PROPOSED` — names both groups and all nine components; **no `Hilmi:` prefix** |
| Visual | `[Visual: Kad narator Hilmi…]` + two group icons |
| Module page | ms 237 (3.3) and ms 242 (3.4); component counts measured from the sub-headings |
| Decision | `PROPOSED_FOR_BARIAH_REVIEW` — `D-02`. Desk slot `(K5, PL06, s03)` is empty; no reflection question drafted |

### S04 — KAD INDUK, Struktur Taman

| | |
|---|---|
| Display | `MEASURED` — four card labels + instruction line, verified against probe `slide4` and reviewed `slide1` |
| VO | `MEASURED` — probe `notesSlide4`, 481 ch, `sha bdd9084a6dda` |
| Visual | card 1 → Rajah 23 (ms 239) · card 2 → Rajah 24 (ms 240) · cards 3, 4 → no source image |
| Module page | **ms 237** (phys 256) · locator `K5PL06T03-B02-IMG-01, ms 237` retained |
| Note | ms 237 carries **no embedded image**. What `IMG-01` depicts is still unresolved — the first figure in 3.3 is Rajah 23 on ms 239 |
| Decision | `SOURCE_BOUND_TEXT`; card treatment → `D-03` |

### S05 — Struktur Persisir Air

| | |
|---|---|
| Display | `SOURCE` — 5 bullets, ~9 lines |
| VO | `SOURCE` — intro + `Aspek Pembinaan` + the 5-row type table |
| Visual | `[Visual: Gunakan Rajah 23 — Contoh Boardwalk dalam Taman Paya Bakau, modul ms 239]` |
| Module page | **ms 238** (phys 257) · asset on ms 239 (phys 258) |
| Terminology | `Promenande` → **`Promenade`** corrected; five English-origin terms present, none italic under the current lexicon |
| Decision | `SOURCE_BOUND_TEXT`; asset choice → `PENDING_BARIAH_APPROVAL` |

### S06 — Struktur Teduhan

| | |
|---|---|
| Display | `SOURCE` — 3 bullets, ~5 lines |
| VO | `SOURCE` — includes the Wakaf and Pergola glosses and the modern-materials sentence |
| Visual | `[Visual: Gunakan Rajah 24 — Contoh Pergola, modul ms 240]` |
| Module page | **ms 239** (phys 258) · asset on ms 240 (phys 259) |
| Terminology | `Wakaf` is Malay and is **not** italicised |
| Note | the only subsection in 3.3 with **no `Aspek Pembinaan` block** |
| Decision | `SOURCE_BOUND_TEXT` |

### S07 — Kemudahan Awam

| | |
|---|---|
| Display | `SOURCE` — 5 bullets, ~8 lines |
| VO | `SOURCE` |
| Visual | **`NO_DEDICATED_SOURCE_IMAGE`** — confirmed in the rendered PDF. A native diagram is **described** in the visual instruction and **not drawn** |
| Module page | **ms 240** (phys 259) |
| Evidence | `3.3.3` sits at y = 320 on p. 240; the only image on that page is at y = 57.6, above it, and belongs to S06 |
| Terminology | `reka bentuk` spaced |
| Decision | `SOURCE_BOUND_TEXT` (text) / `OPEN_DECISION` (visual) — `D-06` |

### S08 — Water Feature

| | |
|---|---|
| Display | `SOURCE` — 5 bullets, ~9 lines |
| VO | `SOURCE` |
| Visual | **`NO_DEDICATED_SOURCE_IMAGE`** — a native cross-section diagram is **described** and **not drawn** |
| Module page | **ms 241** (phys 260) |
| Evidence | `3.3.4` at y = 112 on p. 241; **zero embedded images on that page** |
| Terminology | module uses `Ciri air` in body, `Water Feature` in heading — both source-attested. Card label uses `Water Feature`, italic |
| Decision | `SOURCE_BOUND_TEXT` (text) / `OPEN_DECISION` (visual) — `D-06` |

### S09 — Completion state of S04

| | |
|---|---|
| Display | inherits S04 |
| VO | **intentionally empty** — probe `notesSlide6` measured 0 ch, `sha e3b0c44298fc`. Stated on the notes page so it cannot read as a gap |
| Visual | inherits S04. Ticks are native geometry, not images |
| Module page | ms 237, inherited |
| Decision | `SOURCE_BOUND_TEXT`; VO convention → `D-09` |

### S10 — KAD INDUK, Perabot Taman

| | |
|---|---|
| Display | `SOURCE` — five item names measured from the module sub-headings |
| VO | `PROPOSED` — built from the measured item names; **not a verbatim module passage** |
| Visual | five card-level `[Visual: …]` specifications, each naming its module pages and how many images exist |
| Module page | **ms 242** (phys 261) — 3.4. Perabot Taman |
| Instruction line | `PROPOSED` — built in parallel with S04's verified line |
| Decision | `SOURCE_BOUND_TEXT` (names) / `PROPOSED_FOR_BARIAH_REVIEW` (VO, instruction, 3+2 grid) — `D-03`, `D-04` |

### S11 — Kerusi Taman

| | |
|---|---|
| Display / VO | `SOURCE` |
| Visual | `[Visual: foto jadual spesifikasi — tiga bahan, ms 242–243]` — 3 images available, none bound |
| Module page | **ms 242** (phys 261) · assets ms 242–243 |
| Terminology | table carries `WPC`, `pressure-treated`, `mortise and tenon joints`, `stainless steel`, `outdoor sealant`, `wood oil`, `precast concrete`, `exposed aggregate` — Tier-2, none italic — `D-07` |
| Decision | `SOURCE_BOUND_TEXT` |

### S12 — Papan Tanda · **calibration reference**

| | |
|---|---|
| Display | `MEASURED` — 4 bullets, 346 ch, verified **verbatim** against the module |
| VO | `MEASURED` — probe `notesSlide16`, 449 ch, `sha ba0a525663eb` |
| Visual | `[Visual: Rajah 25 — Lukisan Spesifikasi Papan Tanda Informasi and/or Rajah 26 — Spesifikasi Papan Tanda Penunjuk Arah, both ms 245]` |
| Module page | **ms 243** (phys 262) · assets both on ms 245 (phys 264) |
| Locator | `K5PL06T03-B02-IMG-05, ms 243` — **confirmed exactly** |
| Note | Papan Tanda has **two** figures, not one |
| Decision | `SOURCE_BOUND_TEXT`; which figure(s) to use → `PENDING_BARIAH_APPROVAL` |

### S13 — Tong Sampah

| | |
|---|---|
| Display / VO | `SOURCE` |
| Visual | `[Visual: foto jadual spesifikasi — empat bahan, ms 246–247]` |
| Module page | **ms 245** (phys 264) · assets ms 246–247 |
| Note | the three images on ms 247 sit **above** the `3.4.2` heading and therefore belong to Tong Sampah — `D-13` |
| Terminology | `HDPE` ×3, `liner`, `galvanized and powder-coated steel`, `stainless steel` — Tier-2 |
| Decision | `SOURCE_BOUND_TEXT` |

### S14 — Drinking Fountain

| | |
|---|---|
| Display / VO | `SOURCE` |
| Visual | `[Visual: foto jadual spesifikasi — dua bahan, ms 248–249]` |
| Module page | **ms 247** (phys 266) — the *section* begins here; its **images** are on ms 248–249 |
| Note | this refines the directed asset list (p. 247–248 → p. 248–249). Applied and **stated on screen**, not silently — `D-13` |
| Terminology | module body says `Pancutan air minum`; heading and card label say `Drinking Fountain`, italic. Table adds `push-button valve`, `self-cleaning`, `shut-off valve`, `faucet`, `basin`, `Universal Design` |
| Decision | `SOURCE_BOUND_TEXT`; asset ownership → `D-13` |

### S15 — BBQ pit

| | |
|---|---|
| Display / VO | `SOURCE` |
| Visual | `[Visual: foto jadual spesifikasi — Struktur Kekal, ms 249]` |
| Module page | **ms 249** (phys 268) · asset ms 249 |
| Terminology | `BBQ pit`, lowercase `p` — **confirmed at source** (`### BBQ pit`). Table adds `firebrick`, `cast iron` |
| Decision | `SOURCE_BOUND_TEXT` |

### S16 — Completion state of S10

| | |
|---|---|
| Display | inherits S10 |
| VO | **intentionally empty** — same convention as S09 |
| Visual | inherits S10; ticks are native geometry |
| Module page | ms 242, inherited |
| Decision | `SOURCE_BOUND_TEXT`; VO convention → `D-09` |

### S17 — RUMUSAN

| | |
|---|---|
| Display | `MEASURED` — heading + 4 bullets, verified against probe `slide17` and reviewed `slide7`; SME edits applied |
| VO | `MEASURED` — probe `notesSlide12`, 586 ch, `sha 9d2694129582` |
| Visual | `[Visual: Papan rumusan — two component groups side by side]` — no module image for a summary screen |
| Module page | ms 237–250 (phys 256–269) — the whole bahagian scope |
| Open | the fourth bullet, the industry-application clause, was **drafted by judgement** and is not mechanically checkable — `D-05` |
| Decision | `SOURCE_BOUND_TEXT`, one open clause |

### S18 — KUIZ

| | |
|---|---|
| Display | `DRAFT` — five item stems, types and answer keys on canvas |
| VO | `PROPOSED` — quiz introduction. Item text is read on screen |
| Notes | complete item bank — all options, correct answers, both feedback branches, per-item source page |
| Visual | standard quiz frame described; no image needed, none embedded |
| Module page | items trace to ms 238, 239, 240, 241 and 242–249 respectively |
| Note | **the module carries no question bank.** These items are constructed from source content |
| Decision | `DRAFT_FOR_BARIAH_REVIEW` — `D-08`. Pass mark, attempts and fail routing: **undefined** — `D-10` |

### S19 — TAMAT BAHAGIAN

| | |
|---|---|
| Display | `PROPOSED` — three closing lines + three routing assumptions shown on screen |
| VO | `PROPOSED` |
| Visual | `[Visual: Papan penutup — pairs with the S01 opener]` |
| Module page | none. Group names from ms 237 and ms 242 |
| Routing | A1, A2, A3 — stated as **assumptions**, explicitly **not** ratified K5 decisions. A2's premise (a following bahagian exists) is **unverified** |
| Decision | `PROPOSED_FOR_BARIAH_REVIEW` — `D-11` |

---

## 4. Coverage

| Origin | Screens | Count |
|---|---|---:|
| `MEASURED` — verified strings from the probe | S04, S09, S12, S17 | **4** |
| `SOURCE` — derived from module text this cycle | S05, S06, S07, S08, S11, S13, S14, S15, S10 (names) | **9** |
| `PROPOSED` — written for review | S01 (VO/visual), S02, S03, S19 | **4** |
| `DRAFT` — constructed assessment | S18 | **1** |

| Dimension | Coverage |
|---|---|
| Learner-facing display text | **19 / 19** |
| Complete VO | **19 / 19** (S09, S16 empty by stated convention) |
| Interaction instruction | 19 / 19 |
| State / transition behaviour | 19 / 19 |
| Visual direction as a text specification | 19 / 19 |
| Module source page | 19 / 19 (4 screens correctly record *no* module page) |
| MMD implementation notes | 19 / 19 |
| Decision status | 19 / 19 |
| **Embedded images / audio / video / animation** | **0 / 19 — by instruction** |
| Bound MMD assets | **0** — binding has not begun |

The earlier coverage position — 4 verified, 11 partial, 4 missing — is superseded for **text**. Thirteen
screens are now source-bound and the remaining six carry explicit, labelled proposals instead of blanks.

---

## 5. Asset register — identified, **not bound**

Fourteen assets were extracted from the rendered PDF and registered. **None is embedded in this
storyboard.** They are named in visual instructions so Bariah can judge the direction.

| Screen | Assets | Kind | Module pp. |
|---|---:|---|---|
| S05 | 1 | numbered figure (Rajah 23) | 239 |
| S06 | 1 | numbered figure (Rajah 24) | 240 |
| **S07** | **0** | `NO_DEDICATED_SOURCE_IMAGE` | 240 |
| **S08** | **0** | `NO_DEDICATED_SOURCE_IMAGE` | 241 |
| S11 | 3 | table photographs | 242–243 |
| S12 | 2 | numbered figures (Rajah 25, 26) | 245 |
| S13 | 4 | table photographs | 246–247 |
| S14 | 2 | table photographs | 248–249 |
| S15 | 1 | table photograph | 249 |

Seven of nine detail screens have source imagery. **`usage_status` remains `EXTRACTED — not yet bound`
for all fourteen.**

---

## 6. Modification statement

One new artifact created: `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_1.pptx`, on its own lineage.

**Nothing else was touched.** The accepted visual sample v0.2 was re-hashed after the build and is
unchanged at `8d93e2ce861624f0ff61271538900189c707ac6ec95dd1b1e6db0191646a982b`. No compiler patched, no
schema altered, no canonical ID issued, no baseline, manifest, digest pin, candidate or freeze created.
K5 remains locked; the live CAIR decision desk is untouched. No MMD asset binding has begun.
