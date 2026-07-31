# BARIAH_REVIEW_CHECKLIST — K5 PL06 T03 B02 v0.3

```
REVIEW_READY · PROVISIONAL_CAIR_EXECUTION
CAIR_INTEGRITY_EXCEPTION_FOR_REVIEW_BUILD_ONLY · PENDING_FINAL_BARIAH_CONFIRMATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

Open `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3.pptx` — **63 review pages**.

**Read this first.** The deck has 63 pages but the learner navigates **26 screens**. The other 37 pages
exist so you can *see* a state that the learner experiences as a change on screen — a popup opening, a
tick appearing, a button unlocking. Each such page says so in its off-canvas panel. Nothing about them
adds a screen or a navigation level for the learner.

Production metadata lives **off-canvas, to the left of each slide**, visible in Normal view and absent
from Slide Show. Notes carry **VO only** — no headings, no IDs.

---

## A. CONFIRMED BARIAH FEEDBACK IMPLEMENTED

Please confirm each reads as you intended. These are not being reopened.

- [ ] **Table content is no longer missing.** Every source table now produces a `Contoh [Nama Komponen]`
      screen. All **26** source rows appear as clickable items, one popup each.
- [ ] **One main explanation screen + one example screen** per component, for all nine.
- [ ] **Items clickable in any order**; a tick appears only after an item is viewed.
- [ ] **`Kembali` starts disabled** and unlocks only when every item in that component is viewed, then
      returns to the group master.
- [ ] **Main-screen `Seterusnya` is disabled** until the VO ends.
- [ ] **Global `Seterusnya`** on a group master unlocks only when every card in the group is complete.
- [ ] **Maximum navigation depth = 2.** A popup is a state, never a third level.
- [ ] **Every popup carries VO** (this deliberately overrides the general v1.0 No-VO rule for tables).
- [ ] **S01** uses a `MULA` button, no auto-advance.
- [ ] **S02** is titled *Pengenalan / Komponen Landskap*, shows character labels only, and keeps the
      dialogue in Notes.
- [ ] **S03** shows Hilmi, its VO begins `Hilmi:` (the only screen where it does), names all nine
      components, and carries the reflection question and a **textual** Mind Map specification.
- [ ] **Rumusan** shows no `Kepentingan` / `Apa Yang Dipelajari` / `Isi Utama` / `Manfaat` label and uses
      contractor language.
- [ ] **Kuiz**: 5 items, 4 MCQ + 1 Multiple Response, pass 3/5 = 60%, immediate feedback, `Semak Jawapan`
      and `Ulang Kuiz`, and a sub-60% score does not block progression.
- [ ] **Tamat** carries no routing assumption on the learner canvas.
- [ ] **Nothing multimedia is embedded** — every visual is a text specification with a source locator.

---

## B. FINAL CONFIRMATION REQUESTED

Ten decisions. The first two change screens; the rest are wording, casting or governance.

### B1 — Papan Tanda: one item on its example screen  ⚠

`Contoh Papan Tanda` carries **one** clickable item, because the module gives Papan Tanda exactly one
table row. `Kembali` therefore unlocks after a single click.

The source row does contain four lettered sub-fields (`a. Bahan Panel` with four materials, `b. Bahan
Struktur/Tiang` with two, `c. Grafik`, `d. Rekaan`) — all printed enumerators in the module, so a split
into 4, 6 or 8 items is defensible.

- [ ] **Keep as one item** (as built), or
- [ ] **Split** — state which granularity, or
- [ ] **Fold into the main screen** (this would override S&G v0.2, which requires a separate example screen)

> Whichever you choose, **Papan Tanda remains 1 source row**. Splitting changes interaction items, not
> source identity.

### B2 — BBQ Pit: one item on its example screen  ⚠

Same situation. Four source-attested lettered sub-fields (`a. Bahan Pembinaan`, `b. Dimensi Umum`,
`c. Gril`, `d. Ciri-ciri Keselamatan`).

- [ ] Keep as one item / split into 4 / fold into the main screen

### B3 — Popup density

- [ ] Do the specification popups read comfortably? The densest is **Pancutan Air Minum Keluli Tahan
      Karat** (7 lettered sub-fields) — review pages `RP-050`. Compare with a short one such as
      **Promenade** (`RP-008`).

### B4 — Character naming

- [ ] S02 uses role-neutral `PELATIH` and `PENYELIA TAPAK`. Approve, or supply names.

### B5 — Rumusan wording

- [ ] Does the fourth bullet — *"Kontraktor dapat merancang, melaksana dan menyelenggara setiap komponen
      landskap mengikut fungsinya di tapak"* — read as genuine site application, or generic?

### B6 — Tamat route

- [ ] What does `Tamat Bahagian` actually exit to? Currently unverified and held in production metadata
      only.

### B7 — `Kerusi Komposit` punctuation

- [ ] Source reads `Kerusi KompositContoh: WPC — Wood-Plastic Composite / Plastik Kitar Semula**)**:`
      — an unbalanced closing parenthesis. **Left uncorrected on purpose**: one reading is a dropped
      opening bracket, the other a stray character, and they parse the cell differently. Which is it?

### B8 — Terminology

- [ ] `BBQ Pit` with a capital P is used learner-facing (the module heading is lowercase `BBQ pit`).
- [ ] Italic lexicon stays closed at `Water Feature`, `Drinking Fountain`, `BBQ Pit`. About a dozen
      Tier-2 English terms (`WPC`, `HDPE`, `stainless steel`, `firebrick`…) are **not** italicised —
      confirm that is right.

### B9 — Provisional CAIR rulings

- [ ] R-1 VO fidelity · R-2 popup VO · R-3 state model · R-4 closing structure · R-5 Kembali ·
      R-6 Rumusan · L-01 PL pronunciation · L-02 Mind Map · A-05 single-row · A-06 adaptive popup ·
      A-09 source precedence · N-06 punctuation — all currently `confirmed-CAIR-provisional`.

### B10 — One geometry change you should know about

- [ ] Adding the global `Seterusnya` to the group master collided with the second row of component
      labels. The card grid was **raised**; `CARD_W`, `CARD_H`, `GAP_X`, `GAP_Y` and the label box are
      **unchanged**. Confirm the group master still reads correctly.

---

## C. What is NOT being asked

Geometry accepted in earlier rounds is carried forward: card dimensions and gaps, split-STATE
proportions, the navigation strip, tick placement, Rumusan layout. Asset *binding* is not asked either —
14 assets are named in visual directions and **none is bound**.

---

## D. Known limitation, disclosed

**The module DOCX has no SHA-256.** Four routes were attempted and all failed. Firdaus authorised a
documented integrity exception (`B02-CAIR-INT-001`) for **this review build only**. Text provenance
rests on a derived extraction cross-checked against the module PDF, which *is* hashed, and which
independently confirms the 26-row count.

This exception must be closed before canonical freeze, production approval or MMD build.

**Also:** the container has no PowerPoint renderer, so no page has been seen in PowerPoint itself. Pages
were rendered with metric-accurate font measurement from the generated package. Please flag anything
that looks different when you open it.

---

## E. Do not

- Do not treat this as production-approved, canonically frozen or MMD-ready. It is none of those.
- Do not bind assets or produce multimedia from it.
- Do not hand-edit the deck. Corrections go into the source matrix, the screen/state map, the generator
  or the controlled content data, and the deck is regenerated.
