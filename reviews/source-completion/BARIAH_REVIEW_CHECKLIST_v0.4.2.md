# BARIAH_REVIEW_CHECKLIST — v0.4.2

Deck: `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_2.pptx` — 100 review pages.

# What happened, plainly

The output you reviewed contained **generator regressions** — defects introduced by the code that
builds the deck, not by anyone editing slides. The clearest one:

**BEFORE**
```
[Visual: Arahan visual untuk Promenade — spesifikasi teks sahaja, modul ms 238. Tidak dibenamkan.]
```

**AFTER** (RP-007, and every other Contoh popup)
```
ARAHAN VISUAL — TIDAK DIBENAMKAN
[Visual: Promenade Tasik Titiwangsa, KL]
```

# Why this correction will survive the next regeneration

The old text was not typed into a slide. It was produced by a fallback branch in the generator
whenever a source row carried no figure — 14 of the 26 rows. That branch is gone. The visual
direction now comes from one resolver that reads your corrected exemplar's own rule: name the
source-attested example.

The deck is rebuilt from controlled data on every run, so **editing a slide by hand would be
overwritten the next time it runs, and the pipeline would keep producing the defect.** That is why
the fix had to be in the generator. Nothing you see here was hand-placed.

A regression check now reads the **generated PowerPoint XML, the Notes XML and the rendered
geometry** and fails the build if that fallback text ever reappears. The same is true for each of
the other corrections: 12 deliberate defect fixtures are injected on every run and all 12 must be
caught.

# Review priorities — not limits

Please look at these first. **If you see anything else wrong, flag it** — this list is where we
think the risk is, not a boundary on what you may raise.

1. **Contoh popup visuals** — RP-007 Promenade and two or three others. Right subject, right panel?
2. **Specification popups have no visual** — RP-052 onward. That follows your ruling
   *"KECUALI pop up Spesifikasi"*. Confirm it reads correctly.
3. **Component-main visuals** — 12 screens are **awaiting your decision** and currently show the
   module's own visual text. We did not invent directions for them.
4. **One conflict we could not resolve** — for Struktur Persisir Air the instruction said
   *"follow the reviewed treatment"* and gave `[Visual: Pelbagai Struktur Persisir Air…]`, but your
   corrected slide 10 shows `[Visual: Rajah 23 — Contoh Boardwalk…]`. We render the first and flag
   the second. **Which do you want?**
5. **Speaker Notes italics** — any content page.
6. **Quiz answer key** — RP-093 to RP-097, the cream CIDB block.
7. **Tamat** — RP-100, your wording and hierarchy.
8. **Perabot gateway** — RP-034, visual cards, no internal labels.

# Two things we are not claiming

- **The character names.** `Alya` and `Encik Rahman` appear in no document you signed off; your
  review guide says *"nama watak khusus untuk B02 belum disahkan"*. They are in the deck and marked
  `CONFIRMED_LOCAL_ARTIFACT`, not confirmed by you. Please confirm or replace them. `Hilmi` is
  properly evidenced and unchanged.
- **The quiz review/retry instruction.** A sentence telling learners to click *Semak Jawapan* was
  written by us, not by you. It has been removed pending your decision.

# Still waiting on others

MS2680 applicability (source/Firdaus) · physical LMS navigation on Tamat (Firdaus/LMS) · where the
detailed quiz rationale belongs (you) · the Pengurus Projek name (you).

This is a review build: not production-approved, not canonically frozen, not MMD-ready, and we do
not claim it matches Microsoft PowerPoint rendering.
