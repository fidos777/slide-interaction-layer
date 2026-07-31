# LOCAL_19SLIDE_VISUAL_REVIEW_CHECKLIST — v0.1

Everything below needs **PowerPoint on a local machine**. LibreOffice cannot load these decks in the
build sandbox, so **nothing here has been seen rendered** — only measured. 34 mechanical checks pass;
that is not the same as looking right.

## Before you start

Open `K5PL06T03B02_19SLIDE_VISUAL_TREATMENT_SAMPLE_v0_1.pptx` (`5e35198a…`, 84,253 B).
File→Info must show **"Visual Treatment Sample v0.1 — 19 skrin — bukan storyboard"**.

- [ ] 19 slides, in order S01 → S19
- [ ] Fonts resolve — no substitution boxes. Body Ebrima, title Raleway, bullets Arial
- [ ] Off-canvas production panels stay off-canvas in Normal view, **absent from Slide Show**
- [ ] Notes present on all 19

**This is a treatment sample, not a storyboard.** 15 of 19 screens have no verified source and show
`SOURCE PENDING`. Judge the *treatment*, not the completeness.

---

## A. The four source-verified screens — judge the treatment here

These carry real content. If the treatment is wrong, it is wrong here.

**S04 — four-card base**
- [ ] Four cards, 2 × 2, grid reads as centred
- [ ] Each label centred under **its own** card — check both columns
- [ ] Labels read as labels, not captions (20 pt in a 3.62 × 0.50 in box)
- [ ] Longest label `Struktur Persisir Air` fits one line
- [ ] Placeholder text inside the cards reads clearly against the tint
- [ ] Instruction line spans the grid width, does not wrap
- [ ] `Water Feature` italic in both card and label

**S09 — completion state**
- [ ] Exactly **four** ticks, one per card, all at the same relative position
- [ ] Ticks render as green checkmarks, **not** missing-image boxes — they are drawn shapes here, so
      this should be safe; confirm anyway
- [ ] Cards and labels identical in position to S04

**S12 — split-STATE detail. Review this most closely**
- [ ] Panel occupies the **left ~44 %**; right column not crowded
- [ ] Body heading `Papan Tanda` reads as a heading
- [ ] 8 bullets, 2 levels; sub-bullets under `Boleh berupa:` visibly indented
- [ ] **`Kembali` sits in a clear navigation band** — 0.10 in above and below. Does the band read as
      deliberate?
- [ ] Body does not run into the navigation band
- [ ] Off-canvas note cites **`IMG-05, ms 243`**. If you see `IMG-01` or `237`, the patch failed

**S17 — revised Rumusan**
- [ ] Heading uses an **em dash**; `dan` lowercase
- [ ] No `Kepentingan:` / `Isi Utama:` / `Manfaat:` anywhere
- [ ] Fourth bullet begins `Kontraktor`; `anda` appears nowhere
- [ ] `Water Feature`, `Drinking Fountain`, `BBQ pit` italic — **lowercase `p`**, source form
- [ ] Bullets have visible breathing room; heading clear of the first bullet

---

## B. Propagation — does the treatment hold across all nine detail screens?

S05, S06, S07, S08, S11, S12, S13, S14, S15.

- [ ] **Click through all nine in sequence.** Panel, heading box, body and `Kembali` should not move
      by a hair between them
- [ ] Exactly **one** `Kembali` on each — and **none** on S01–S04, S09, S10, S16–S19
- [ ] The navigation band sits identically on all nine
- [ ] Every one carries a verified label in the heading box
- [ ] Eight of nine show `SOURCE PENDING` in the body — only **S12** has real content
- [ ] Does the empty split-STATE frame still read as a coherent screen, or does it look broken when
      the body is pending?

**S10 / S16 — the five-card family, seen for the first time**
- [ ] Five cards, **3 on top, 2 centred below**
- [ ] Cards are visibly narrower than S04's (3.60 vs 3.935 — an 8.5 % reduction). Acceptable?
- [ ] Row 2 reads as deliberately centred, not as a broken grid
- [ ] Row pitch matches S04 — the two bases should feel like one family
- [ ] S16 has exactly **five** ticks
- [ ] The instruction zone shows `SOURCE PENDING` — S04's wording was **not** copied across. Right call?

---

## C. Source honesty — is the incompleteness unmistakable?

- [ ] Every `SOURCE PENDING` block is impossible to mistake for content
- [ ] **S02** shows role-neutral `[PELATIH]` / `[PENYELIA]` only — no dialogue, no named character
- [ ] **S03** introduces `Hilmi` as narrator visually, with the provenance line beneath. No `Hilmi:`
      prefix appears in any VO anywhere in the deck
- [ ] **S18** contains **no** question, option, answer key, feedback or routing. Confirm by eye —
      this is the one screen where invented content would be most damaging
- [ ] Notes on every pending screen read `[VO SOURCE PENDING …]`, never invented narration
- [ ] No scenario character names anywhere — no Haziq, Roslan, Alya, Rahman

---

## D. Whole-deck read

- [ ] Play it start to finish. Does it read as **one course bahagian**, or as several treatments?
- [ ] Do the two card bases (S04 4-card, S10 5-card) read as the same family?
- [ ] Does a detail screen read as clearly *not* a summary screen when set beside S17?
- [ ] Is the ratio of pending to verified screens acceptable to circulate, or should this stay internal
      until the packet arrives?

---

## E. Known gaps — do not review these as defects

| Gap | Why |
|---|---|
| No images anywhere | No B02 source image exists in any available artifact — 0 of 19 |
| 15 screens without content | `packet_B02.json` and the Tier-1 spec are absent |
| No click-through interaction | Static visual sample; the base → child → base loop is not wired |
| S10 may not be a Card screen at all | Classification still `NOT_DETERMINABLE` without region data |
| Detail screen numbering | Only `S12 = Papan Tanda` is confirmed; the other eight assignments are inferred |

---

## Do not

- Do not treat this as a storyboard, baseline, candidate or production artifact
- Do not circulate without `AUDIT.md`, `SOURCE_STATUS.md` and `CHANGELOG.md`
- Do not fill the `SOURCE PENDING` blocks by hand — that is what the packet is for
- Do not save over any preflight or probe revision. None is regenerable
