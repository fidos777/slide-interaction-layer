# LOCAL_PREFLIGHT_REVIEW_CHECKLIST — v0.1

Everything below needs **PowerPoint on a local machine**. LibreOffice cannot load these decks in the
build sandbox, so **nothing here has been seen rendered** — only measured. The package passes 22 of 22
mechanical checks; that is not the same as looking right.

## Before you start

Open `K5PL06T03B02_3SCREEN_IMPLEMENTATION_PREFLIGHT_v0_1.pptx`
(`2b756e5b…`, 35,390 B). File→Info must show **"Preflight — 3 skrin — bukan storyboard, bukan 19
slaid"**. If not, you have the wrong file.

Keep probe v0.1 (`24dcaa04…`) open beside it. Probe slide 2 is the canonical S12; preflight slide 2 is
the same archetype with the corrected locator and a concise display. Side by side is the fastest read.

- [ ] 3 slides only. If you see 19, you have the wrong file
- [ ] Fonts resolve — no substitution boxes. Bullet font is Arial by declaration; body is Ebrima, title
      Raleway
- [ ] Off-canvas production panels stay off-canvas in Normal view and are **absent from Slide Show**
- [ ] Notes present on all three slides

---

## Slide 2 — S12, split-STATE. **Review this first**

This is the screen the preflight exists to settle. The reviewed deck made this panel full-width; the
preflight reverts it to canonical split. **If this reads wrong, nine screens change.**

- [ ] **Put S12 and S17 side by side. Do they read as two different kinds of screen?**
      That is the whole question
- [ ] Visual panel occupies the **left ~44 %** and does not crowd the right column
- [ ] Gutter between panel and text column reads as deliberate, not as a gap
- [ ] Body heading `Papan Tanda` sits above the body and reads as a heading, not a stray line
- [ ] Title bar `Papan Tanda` and body heading `Papan Tanda` **repeat**. Is that acceptable, or should
      the title bar carry `Perabot Taman` (the section) instead? — see `P-08`
- [ ] Body: 8 bullets, 2 levels. Sub-bullets under `Boleh berupa:` are visibly indented
- [ ] **Body does not run past `Kembali`** — measured 10 lines against a ~12.5-line box, but
      `spAutoFit` is recomputed on open
- [ ] `Kembali` sits **below** the panel, horizontally centred, not overlapping
- [ ] `Kembali` is not clipped at the bottom edge — measured clearance is **0.0625 in**
- [ ] Left panel reads as a production-instruction placeholder, not artwork
- [ ] Off-canvas note cites **`K5PL06T03-B02-IMG-05, ms 243`**. If you see `IMG-01` or `237`, the patch
      failed

---

## Slide 1 — S04, four-card base

- [ ] Four cards, 2 × 2, evenly spaced; the grid reads as centred on the slide
- [ ] **Each label is centred under its own card.** In the reviewed deck they were 0.097 in off,
      mirrored left and right — check both columns
- [ ] Card 2's placeholder reads `Visual: Struktur Teduhan`, **not** `Struktur Persisir Teduhan`
- [ ] Longest label — **Struktur Persisir Air** — fits on one line without clipping. Check first
- [ ] Instruction line spans the grid width and does not wrap
- [ ] Instruction line clear of the top card row; nothing crowds
- [ ] `Water Feature` is **italic** in both the card placeholder and the label
- [ ] Nothing numbered anywhere
- [ ] Off-canvas note cites `K5PL06T03-B02-IMG-01, ms 237`

---

## Slide 3 — S17, revised Rumusan

- [ ] Heading `Komponen Landskap — Struktur Taman dan Perabot Taman` uses an **em dash**, and `dan` is
      **lowercase**
- [ ] Heading reads as a heading — bold, separated from the bullets below
- [ ] **No** `Kepentingan:`, `Isi Utama:`, `Manfaat:` or `Manfaat kefahaman:` anywhere
- [ ] Fourth bullet begins `Kontraktor`. The word `anda` appears nowhere
- [ ] `Water Feature`, `Drinking Fountain`, `BBQ pit` are italic
- [ ] **`BBQ pit`** — lowercase `p`. This is the source form and it deliberately differs from the
      reviewed deck's `BBQ Pit`
- [ ] Bullets carry **no** terminal full stops
- [ ] Body fits the panel; 4 bullets should render in 6–7 lines against a ~7-line box — **this is the
      tightest box in the deck**

---

## Cross-cutting

- [ ] **No `Hilmi:` anywhere in any VO.** Check all three notes pages
- [ ] No scenario character names anywhere — no Haziq, Roslan, Alya, Rahman
- [ ] Every off-canvas panel opens with the preflight banner
- [ ] Nothing K4, nothing lift-related, nothing from another course — including File→Info
- [ ] No iSpring tab or publish settings appear (the tag block was deliberately excluded)

---

## The question the preflight exists to answer

Probe slides 1–3 pair a **card base** with a **split-STATE child**. Whether that reads as one coherent
interaction family has been open since 16/06 and has never been answerable, because nothing has ever
been seen rendered.

- [ ] Does S04 → S12 read as one family — a base and its detail?
- [ ] Or does S12 feel like a different deck?
- [ ] And separately: does S12 read as clearly *not* a summary screen when set beside S17?

**That judgement is the CAIR family decision.** The 19-slide sample stays blocked until it is made.

## If S12 fails

Then `A-05` is wrong, the 9 detail screens revert to the full-width form Bariah used, and
`K5-DR-060` closes against the recommendation. **That is a successful outcome** — it answers the
question at the cost of three screens instead of nineteen.

## Do not

- Do not save over the preflight or the probe. Neither is regenerable
- Do not treat this as a storyboard, a baseline, a candidate or a review artifact
- Do not circulate without this checklist, `PREFLIGHT_MAPPING.md` and `PREFLIGHT_VALIDATION.md`
- Do not build the remaining 16 screens on the strength of this — 4 of them have **no source at all**
  and 11 have only a subject name (`SOURCE_CUSTODY_AND_COVERAGE.md`)
