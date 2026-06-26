# MMD E-learning — Process Terms

A shared glossary so humans and AI agents use the same words across a governed courseware project.
Spec only. Adapt the specific codes to your programme; the *categories* are what matter.

## Course structure

- **Module** — a top-level course unit (often coded, e.g. `K1`).
- **PL (Pembelajaran / Learning unit)** — a sub-unit within a module. Spoken as "PL satu",
  "PL dua" — **never** "PL kosong satu". Written codes may still be zero-padded (`PL01`).
- **Topic (T)** — a lesson within a PL (e.g. `T1`–`T4`). A full address looks like `K1PL1T1`.
- **Storyboard deck** — the source slide deck (often `.pptx`) that defines each screen, its
  voice-over, on-screen text, media, and interactions before production.

## People & voice

- **Narrator** — the off-screen voice (e.g. "Hilmi" as a narrator persona).
- **Characters** — named on-screen personas used consistently across the module (define a
  *character bank* so names/roles never drift between decks).
- **Voice-over (VO)** — the recorded narration for a screen. VO scripts follow the spoken-number
  rule above and must match the on-screen text intent.

## Interaction & assessment

- **Interaction** — an on-screen activity mapped to a core pattern (`P5` Hotspot, `P6` Quiz,
  `P7` Branching, etc.). In governed e-learning these are often *required*, not decorative.
- **Quiz** — an assessment screen. Must have: a clear stem, the correct answer marked, feedback,
  and a consistent naming convention. Empty/placeholder quizzes are blockers.
- **Completion rule** — the condition that marks an interaction "done" (reuses core rules:
  `all_hotspots_clicked`, `answered_correctly`, `reached_an_ending`, etc.).

## Tracking & evidence (vocabulary only here)

- **Completion status** — whether the learner finished the required screens (`completed` / `incomplete`).
- **Success status** — whether they passed assessment (`passed` / `failed`).
- **Score** — the assessment result, against a defined pass threshold.
- **Audit evidence** — the artifacts proving the above (a registration result, a checklist, a
  screenshot/log). Required for compliance sign-off.
- **SCORM / xAPI** — the LMS standards these statuses map to. (Mapping is specified in
  `interaction-decision-sop.md`; no runtime here.)

## Naming hygiene (common blockers)

- VO says "PL satu", not "PL kosong satu".
- Quiz screens follow the agreed naming pattern; no `Quiz`, `Quiz copy`, `Untitled`.
- No stale module/PL/topic codes left over from a copied deck.
- Navigation present and consistent (back / next / menu) on every screen.
