# Media Assembly SOP (spec)

How to turn an approved storyboard + raw assets into **verified** media for a governed module.
This is a process specification — no scripts ship in this release.

## Source-of-truth rule

- A **canonical master** is the authoritative high-quality render of a segment
  (e.g. `…_master_crf17.mp4`). It is the source of truth.
- A **delivery derivative** is a smaller file produced *from* a master for the LMS/SCORM package
  (e.g. `…_scorm.mp4`). Never confuse the two; never edit a derivative and treat it as a master.
- Every master gets a recorded **fingerprint (MD5)** so you can prove it is unchanged later.

## Assembly order

1. **Lock the storyboard.** Screens, VO scripts, on-screen text, interactions, and media list are
   approved before any rendering. Late storyboard changes invalidate downstream media.
2. **Build the master VO.** Concatenate per-segment voice-over into one master track. Derive timings
   from the **actual audio durations**, not estimates.
3. **Build the EDL / cut sheet.** A frame-accurate map of in/out times, tracks, trims, and motion,
   driven by the real VO durations from step 2.
4. **Prepare B-roll / cutaways.** Stills become exact-duration silent clips (subtle push-in) at the
   target spec; talking-head "plates" are trimmed to their windows.
5. **Assemble to the EDL.** Lay plates + B-roll over the continuous timeline against the master VO,
   with no black gaps and a consistent target resolution/fps.
6. **QC the draft** (see checklist) before promoting to final quality.
7. **Promote to final** at master quality, then derive the delivery file(s) for packaging.

## QC checklist (must pass before promote)

- Duration matches the EDL within tolerance; total matches the master VO.
- Resolution / fps / codec match the agreed delivery spec.
- No black frames or audio gaps; VO stays in sync at key beats.
- On-screen text matches VO intent; spoken-number rule respected ("PL satu").
- Each interaction window aligns with its screen.

## Delivery consistency (before packaging)

- Delivery files in the build (e.g. `public/` and `dist/`) are **identical to each other**.
- Each derivative matches its master by duration/spec/frame content (it will **not** match by MD5 —
  that's expected for a re-encode).
- The package (e.g. SCORM zip) embeds the **current** delivery files, not stale ones, and is under
  the size limit.

## Definition of done (media)

Masters validated against their fingerprints · derivatives consistent and current · QC passed ·
package gate green. Anything failing → raise as an S0 board blocker (see `s0-board-governance.md`).
