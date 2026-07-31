# DISPLAY_BUDGET_REDERIVED

Phase B1 — display budget of the reviewed `Papan Tanda` full-slide reveal state, re-derived from
measured typography rather than assumed.

Source artifact: `3f626ac5-BARIAH_REVIEW_8SLIDES.pptx`, SHA-256 `ee4f5479…8bb9e7`.
Primary locus: `ppt/slides/slide4.xml` (`sldId 9011`), shape `id=9` `TextBox 12`.
Bound VO: `ppt/notesSlides/notesSlide3.xml`. Stage 13.3333 × 7.5 in.

---

## 1. The S12 comparison cannot be performed — `NOT_DETERMINABLE`

The task requires comparing Bariah's reviewed display against **the issued S12 display**. S12 is a
screen of the 19-slide K5 B02 Tier-1 specification / `packet_B02.json`, and **neither artifact is
present in this session** (see `BARIAH_REVIEW_INGEST.md §1.1`). No S12 text exists to measure, so no
character, word, sentence, bullet, or word-set delta against S12 can be produced.

**Substitute comparison, and why it is legitimate.** The reviewed slide's own bound VO
(`notesSlide3.xml`) is the source-bound channel for the same screen. Comparing display against its
own VO answers the question the gate actually exists to answer — *did display shortening delete
propositions, or resegment them across channels?* — without needing S12. Everything in §2–§5 is
measured against that pair and is labelled `MEASURED_FACT`. The S12 delta remains
`NOT_DETERMINABLE` and must be produced in Stage 0A once the packet is supplied.

A second, fully-controlled pair **is** available in-package and is measured in §6: the untouched base
Rumusan (`slide7`, `sldId 9016`) against Bariah's revision (`slide8`, `sldId 9017`).

---

## 2. Reviewed display — measured content — `MEASURED_FACT`

`slide4.xml` shape `id=9`, 8 non-empty paragraphs:

| ¶ | Level | Chars | Words | Text |
|---:|---:|---:|---:|---|
| 0 | 0 | 77 | 10 | `Elemen penting untuk navigasi, maklumat, dan keselamatan dalam ruang landskap` |
| 1 | 0 | 55 | 8 | `Jelas, mudah dibaca, dan diletakkan di lokasi strategik` |
| 2 | 0 | 13 | 2 | `Boleh berupa:` |
| 3 | 1 | 13 | 2 | `penunjuk arah` |
| 4 | 1 | 10 | 2 | `peta taman` |
| 5 | 1 | 45 | 6 | `informasi tentang tumbuhan atau ciri landskap` |
| 6 | 1 | 15 | 2 | `peraturan taman` |
| 7 | 0 | 50 | 8 | `Bahan digunakan harus tahan cuaca dan tahan luntur` |

| Metric | Value |
|---|---:|
| Character count (joined, incl. spaces) | **285** |
| Character count (excl. spaces) | **246** |
| Word count | **40** |
| Sentence count (`.` `!` `?`) | **0** |
| Bullet count | **8** (4 at level 0, 4 at level 1) |
| Longest paragraph | 77 chars |
| Mean paragraph | 35.6 chars |

### 2.1 Bound VO — `notesSlide3.xml` — `MEASURED_FACT`

Header (constant across the deck): `PL06: Pengurusan Operasi Pembinaan Landskap` /
`Topik 3 Bahagian 2: Komponen Landskap`. Section label: `Perabot Taman` (13 chars).

VO body, 346 chars, **50 words, 4 sentences**:

> `Papan tanda adalah elemen penting untuk navigasi, maklumat, dan keselamatan dalam ruang landskap. Papan tanda mesti jelas, mudah dibaca, dan diletakkan di lokasi yang strategik. Ia boleh berupa penunjuk arah, peta taman, informasi tentang tumbuhan atau ciri landskap, atau peraturan taman. Bahan yang digunakan harus tahan cuaca dan tahan luntur.`

No `Hilmi:` prefix (cf. `SME_RULE_CHECKABILITY.md §1`).

---

## 3. Display versus VO — the deltas

### 3.1 Aggregate — `MEASURED_FACT`

| Metric | VO body | Display | Δ |
|---|---:|---:|---:|
| Characters | 346 | 285 | **−61 (−17.6 %)** |
| Words | 50 | 40 | **−10 (−20.0 %)** |
| Sentences | 4 | 0 | −4 |
| Bullets | 0 | 8 | +8 |
| Full stops | 4 | **0** | −4 |
| Commas | 7 | 4 | −3 |
| Colons | 0 | 1 | +1 |

### 3.2 Word-set removed — `MEASURED_FACT`

Complete list. **Every removed token is a function word, a copula, a modal, a relativiser, or the
repeated grammatical subject.** No content word was removed.

| Token | VO | Display | Class |
|---|---:|---:|---|
| `papan` | 2 | **0** | repeated subject noun |
| `tanda` | 2 | **0** | repeated subject noun |
| `yang` | 2 | **0** | relativiser |
| `adalah` | 1 | **0** | copula |
| `mesti` | 1 | **0** | modal |
| `ia` | 1 | **0** | resumptive pronoun |
| `atau` | 2 | 1 | list connective (one retained, one replaced by bullet structure) |

`papan tanda` is the screen's own title (`TextBox 6`: `Papan Tanda`), so dropping it from the body is
de-duplication against the title bar, not content loss.

### 3.3 Word-set added — **empty** — `MEASURED_FACT`

**Zero tokens appear in the display that are absent from the VO.** The display vocabulary is a strict
subset of the VO vocabulary.

Lexical retention: **35 of 41 unique VO tokens = 85.4 %**; 34 unique tokens retained at identical
multiplicity.

### 3.4 Changed phrasing — `MEASURED_FACT`

| VO sentence | Display | Transformation |
|---|---|---|
| `Papan tanda adalah elemen penting untuk navigasi, maklumat, dan keselamatan dalam ruang landskap.` | `Elemen penting untuk navigasi, maklumat, dan keselamatan dalam ruang landskap` | subject + copula elided; predicate promoted to head |
| `Papan tanda mesti jelas, mudah dibaca, dan diletakkan di lokasi yang strategik.` | `Jelas, mudah dibaca, dan diletakkan di lokasi strategik` | subject + modal elided; `yang` dropped |
| `Ia boleh berupa penunjuk arah, peta taman, informasi tentang tumbuhan atau ciri landskap, atau peraturan taman.` | `Boleh berupa:` + 4 level-1 bullets | pronoun elided; inline list **exploded into 4 sub-bullets**; `atau` connectives replaced by bullet structure |
| `Bahan yang digunakan harus tahan cuaca dan tahan luntur.` | `Bahan digunakan harus tahan cuaca dan tahan luntur` | `yang` dropped |

### 3.5 Punctuation changes — `MEASURED_FACT`

- **All 4 sentence-final full stops removed.** Display carries no terminal punctuation on any bullet —
  applied consistently, 8/8.
- 3 commas removed — the 3 that separated the inline list absorbed into bullet structure.
- 1 colon added — `Boleh berupa:` introducing the sub-list.

### 3.6 Capitalisation changes — `MEASURED_FACT`

| VO | Display | Cause |
|---|---|---|
| `…adalah **e**lemen penting…` | `**E**lemen penting…` | new bullet-initial position |
| `…mesti **j**elas…` | `**J**elas,…` | new bullet-initial position |
| `**I**a boleh berupa…` | `**B**oleh berupa:` | pronoun elided; `boleh` promoted |
| `**B**ahan yang digunakan…` | `**B**ahan digunakan…` | unchanged |

All four are mechanical consequences of promoting a mid-sentence word to bullet-initial position. No
term was recased. Consistent with the run-level XML: the capitalised initial is its own run
(`<a:r><a:rPr lang="en-MY"/><a:t>E</a:t></a:r>` + `<a:t>lemen</a:t>`), so the edit was made by
retyping the first character.

### 3.7 Display versus full VO coverage — **4 of 4 propositions retained** — `MEASURED_FACT`

| # | VO proposition | Display carrier | Retained? |
|---:|---|---|---|
| 1 | signage is essential for navigation, information, safety in landscape space | ¶0 | **yes** |
| 2 | must be clear, legible, strategically located | ¶1 | **yes** |
| 3 | may be: direction marker / park map / plant or feature information / park rules | ¶2 + ¶3–¶6 | **yes — expanded to 4 discrete bullets** |
| 4 | materials must be weather- and fade-resistant | ¶7 | **yes** |

**Zero propositions dropped. Zero content words dropped. Zero tokens added.** Proposition 3 is
*more* granular on the display than in the VO — the four list members become four addressable bullets.

---

## 4. Reviewed display formatting — `MEASURED_FACT`

`slide4.xml` shape `id=9` `TextBox 12` — (0.9046, 4.4115) 11.6371 × 2.5244.

| Property | Value | Source of value |
|---|---|---|
| Font face | **Ebrima** | `+mn-lt` → `theme1.xml` `minorFont/latin`; no run override |
| Font size | **18 pt** | `slideMaster1.xml` `otherStyle/lvl1pPr sz="1800"`; lvl2 also `1800` — no run carries `sz` |
| Kerning | `kern="1200"` | `otherStyle` |
| **Bold spans** | **8** | `navigasi`, `maklumat`, `keselamatan` (¶0); `Jelas`, `mudah dibaca` (¶1); `lokasi strategik` (¶1); `tahan cuaca`, `tahan luntur` (¶7) |
| **Italic spans** | **0** | no `rPr/@i` anywhere in this shape |
| Paragraph levels | **0 and 1** | 4 paragraphs each |
| `marL` | **285750** (lvl 0) · **742950** (lvl 1) | explicit `pPr` |
| `indent` | **−285750** (both levels) | explicit `pPr` |
| `spcBef` | **not declared** | inherits none |
| `spcAft` | not declared | — |
| Bullet character | **`•`** (U+2022), both levels | `buChar char="•"` |
| Bullet font | **Arial**, both levels | `buFont typeface="Arial"` |
| Line spacing | **not declared → 100 %** | no `lnSpc` |
| Text-box dimensions | **11.6371 × 2.5244 in** | `a:ext` |
| Insets | `lIns`/`rIns` 0.1 in, `tIns`/`bIns` 0.05 in | defaults, none overridden |
| **Autofit** | **`spAutoFit`** | `bodyPr/a:spAutoFit` |
| Fill / outline | `noFill`, no `a:ln` | — |

`spAutoFit` matters: PowerPoint wrote back the height the text actually needed, so `h = 2.5244` is a
**measured rendering result**, not a design intent. It is used as ground truth in §5.

Bold usage is a keyword-emphasis pattern (8 spans across 3 of 8 bullets), not structural. Note ¶1 is
bold on `Jelas` and `mudah dibaca` but **not** on `diletakkan`, while `lokasi strategik` is bold —
inconsistent emphasis within one bullet. `PROVISIONAL_IDENTIFIER`

---

## 5. Practical capacity at the measured typography

### 5.1 Model — `MEASURED_FACT`

```
line box (lvl 0) = 11.6371 − lIns 0.1 − rIns 0.1 − marL 0.3125 = 11.1246 in
line box (lvl 1) = 11.6371 − 0.1 − 0.1 − marL 0.8125           = 10.6246 in
line height      = 18 pt × 1.00 ≈ 21.6 pt = 0.3000 in
text height      = 2.5244 − tIns 0.05 − bIns 0.05 = 2.4244 in = 174.56 pt
rendered lines   = 174.56 / 21.6 = 8.08 → 8 lines
```

Ebrima at 18 pt: em = 0.25 in; mean advance for Malay lowercase-dominant text 0.46–0.50 em
= **0.115–0.125 in/char**.

| Level | Line box | Capacity |
|---|---:|---:|
| 0 | 11.1246 in | **89–97 chars/line** |
| 1 | 10.6246 in | **85–92 chars/line** |

### 5.2 The model is validated by the artifact itself — `MEASURED_FACT`

The model predicts 8 rendered lines. The content is 8 paragraphs, longest **77 chars** — below the
89-char level-0 threshold, so **every paragraph occupies exactly one line**, giving 8 lines.
`spAutoFit` independently resolved the box to a height admitting exactly 8 lines.

Two independent routes agree. The capacity model is calibrated, not assumed.

### 5.3 Practical capacity — and the real constraint

| Basis | Capacity | Current load | Utilisation |
|---|---:|---:|---:|
| **Characters** (8 lines × 89–97) | 712–776 | 285 | **37–40 %** |
| **Line slots** | 8 | 8 | **100 %** |

**The binding constraint is line slots, not characters.** The box is 60 % empty by character volume
and completely full by line count, because the content is 8 short bullets (mean 35.6 chars) rather
than fewer, fuller ones.

### 5.4 The hard ceiling is 8 lines — zero headroom — `MEASURED_FACT`

`spAutoFit` grows the box downward from `y = 4.4115`. The obstacles below:

| Limit | y | Available | Max lines |
|---|---:|---:|---:|
| Visual panel bottom (`id=8`) | 7.0417 | 2.6302 in | **8** |
| `Kembali` top (`id=11`) | 7.1009 | 2.6894 in | **8** |
| Stage bottom | 7.5000 | 3.0885 in | 9 |

**A 9th bullet overflows the panel and collides with `Kembali`.** The display sits at exactly 100 % of
its usable line budget with no reserve. Any of the following breaks the layout:

- adding a bullet or sub-bullet
- lengthening any bullet past 89 chars (level 0) or 85 chars (level 1) — current longest is 77, so
  headroom is **12 characters** on the longest line
- raising the font above 18 pt
- introducing `spcBef` on any paragraph

**Recommended parameter: `MAX_DISPLAY_LINES = 8` at 18 pt for the full-width reveal-child archetype,
with a design target of 7 to preserve one line of reserve.** `CAIR_RECOMMENDATION`

Note the interaction with `STATE_ARCHETYPE_OPTIONS.md`: Option A (split-STATE) narrows the line box to
5.6742 in ≈ 45–49 chars/line, reflowing this same 285-char body from 8 lines to **13**. Since the
present layout has zero headroom at 8, Option A is viable only if display load is *reduced* — which
§7 establishes is the correct direction anyway.

---

## 6. Controlled pair — Rumusan base versus Bariah revision — `MEASURED_FACT`

`slide7` (`sldId 9016`, **untouched base**) vs `slide8` (`sldId 9017`, Bariah), with their bound VOs.

| Metric | `slide7` display | `slide7` VO | `slide8` display | `slide8` VO |
|---|---:|---:|---:|---:|
| Characters | 496 | 503 | **459** | **539** |
| Words | 63 | 64 | 59 | 68 |
| Sentences | 3 | 3 | **0** | 3 |
| Bullets | 3 + heading | — | 4 + heading | — |
| Box | 11.7083 × 2.5244 | — | 11.7292 × 2.2215 | — |
| Rendered lines | 8.08 → 8 | — | 7.07 → **7** | — |
| Capacity | 90–97 ch/line | — | 90–98 ch/line | — |

**The direction of change is the finding.**

- In the **base**, display (496) ≈ VO (503) — a **1.4 %** difference. The display was essentially a
  transcript of the VO.
- In **Bariah's revision**, display (459) is **80 characters and 9 words shorter** than VO (539) — a
  **14.8 %** divergence, and the VO **grew** relative to the base (503 → 539, **+7.2 %**).

**Bariah moved content in opposite directions in the two channels simultaneously: display down,
VO up.** That is not truncation. That is deliberate channel separation.

The specific proposition proves it. `notesSlide7` sentence 3 opens with a framing clause the display
does not carry:

> VO: `**Dengan memahami komponen-komponen ini,** kontraktor dapat merancang, melaksana dan menyelenggara setiap komponen landskap mengikut fungsinya di tapak.`
> Display ¶4: `Kontraktor dapat merancang, melaksana dan menyelenggara setiap komponen landskap mengikut fungsinya di tapak`

The causal framing is **retained in the source-bound VO and omitted from the learner display**. The
proposition is not lost from the screen; it is carried in the channel built to carry it.

Bariah also reduced the box height 2.5244 → 2.2215 (−12 %), i.e. she **shrank the container to match
the reduced display load** rather than leaving slack. The revision runs at 7 lines against the base's
8 — one line of reserve gained.

---

## 7. Gate determination

# `LOSSLESS_RESEGMENTATION_GATE_SUPERSEDED`

**The evidence proves Bariah intentionally used concise learner display while preserving fuller
source-bound VO.** Stated on four independent measurements, each `MEASURED_FACT`:

1. **Zero propositions dropped on `Papan Tanda`.** All 4 VO propositions are carried on the display
   (§3.7); proposition 3 is carried at *higher* granularity as 4 addressable bullets than as the VO's
   inline list.

2. **Zero content words dropped, zero tokens added.** All 7 removed token types are function words,
   the copula `adalah`, the modal `mesti`, the relativiser `yang`, the resumptive `ia`, or the repeated
   subject `papan tanda` — which is de-duplication against the slide's own title bar. Display
   vocabulary is a **strict subset** of VO vocabulary; 85.4 % lexical retention with **nothing added**
   (§3.2–§3.3). Compression is grammatical, not propositional.

3. **The controlled pair shows the channels moving in opposite directions.** Base: display ≈ VO
   (496 vs 503, 1.4 % apart). Revision: display **−7.5 %** vs base while VO **+7.2 %** vs base,
   opening a 14.8 % display-under-VO gap — with an identified proposition
   (`Dengan memahami komponen-komponen ini`) present in the VO and deliberately absent from the
   display (§6). Truncation cannot produce a VO that grows.

4. **The container was resized to match.** Bariah reduced the Rumusan display box height 12 %
   (2.5244 → 2.2215) rather than leaving the freed space empty (§6) — an authoring act consistent
   with intent, not with omission.

**Consequence, per the task's own instruction:** shorter display text must **not** be treated as source
deletion where proposition coverage remains in the VO and the source locator. Both conditions hold —
coverage is 4/4 on `Papan Tanda`, and the module locators (`imej K5PL06T03-B02-IMG-01, ms 237`;
`K5PL06T03-B02-IMG-05, ms 243`) are retained in the off-canvas reference boxes on the same slides.

**Residual scope limits — this determination does not extend past what was measured:**

- It is established on **two screens** — `Papan Tanda` (`slide4`) and Rumusan (`slide8`).
- It is `NOT_DETERMINABLE` for the remaining 17 packet screens; `packet_B02.json` is absent.
- The **S12 comparison remains outstanding** (§1) and must be produced in Stage 0A.
- The `IMG-01`/ms 237 vs `IMG-05`/ms 243 conflict on `slide4` (`BARIAH_REVIEW_INGEST.md §8.5`) is
  unresolved; source-locator retention is asserted on the *presence* of locators, not their
  correctness.

---

## 8. Summary of budget parameters

| Parameter | Measured / derived | Label |
|---|---:|---|
| Font | Ebrima 18 pt (inherited `otherStyle/lvl1pPr`) | `MEASURED_FACT` |
| Line height | 21.6 pt (100 %, no `lnSpc`) | `MEASURED_FACT` |
| Level-0 line box | 11.1246 in → 89–97 chars | `MEASURED_FACT` |
| Level-1 line box | 10.6246 in → 85–92 chars | `MEASURED_FACT` |
| Rendered lines, reviewed | 8 (validated two ways) | `MEASURED_FACT` |
| Character capacity | 712–776 | `MEASURED_FACT` |
| Character load | 285 (37–40 %) | `MEASURED_FACT` |
| **Line-slot load** | **8 / 8 = 100 %** | `MEASURED_FACT` |
| Hard ceiling (panel + `Kembali`) | **8 lines** | `MEASURED_FACT` |
| Longest-line headroom | **12 characters** | `MEASURED_FACT` |
| Proposed `MAX_DISPLAY_LINES` | 8 hard / 7 design target | `CAIR_RECOMMENDATION` |
| S12 delta | — | `NOT_DETERMINABLE` |
| Gate status | superseded | `LOSSLESS_RESEGMENTATION_GATE_SUPERSEDED` |

---

## 9. Modification statement

No PPTX was modified. No budget was frozen, no schema updated, no manifest or digest pin created.
Every value above is a measurement of, or a derivation from,
`3f626ac5-BARIAH_REVIEW_8SLIDES.pptx` @ `ee4f5479…8bb9e7`, at the slide, shape, and notes loci cited.
