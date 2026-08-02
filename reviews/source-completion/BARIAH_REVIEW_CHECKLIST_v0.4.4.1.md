# BARIAH_REVIEW_CHECKLIST — v0.4.4.1

Deck: `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4_1.pptx` — 100 review pages.

# 1. Read this first: nothing you review has changed

**Not one word of instructional content differs from v0.4.4.** Every learner-facing shape on
all 100 pages is byte-identical, in the same position, at the same size; every Speaker Notes
transcript is identical, down to the italic runs. This release changes only the off-canvas
production panel — the metadata block a reviewer reads in Normal view and a learner never
sees.

So if you already reviewed v0.4.4, **your review still stands**. Nothing needs re-checking
for content. Section 2 is the whole of what changed.

# 2. What actually changed

## 2.1 The deck was stamped with the wrong version and the wrong release status

Every page of v0.4, v0.4.1, v0.4.2, v0.4.3 and v0.4.4 carried the same hand-written version
line — the one written for v0.4 — and the same five release tokens from that stage. The
filename, the run manifest, the decision register and the accepted verdict had all moved on
four times; the panel had not.

Two of the five tokens were still true and are kept. Three were not. The exact retired
strings are recorded verbatim in `B02_DEFECT_REGISTER_v0.4.4.1.md` under
**B02-META-REG-001**, along with the reason our own QA suite could not see it — briefly, one
gate forbade only the previous version number and never asked what the version should be,
and another **required** the stale tokens to be present on every page, so correcting them
would have turned the suite red.

The panel now reads:

```
K5 PL06 T03 B02 — PAPAN CERITA v0.4.4.1
REVIEW_CANDIDATE · FINAL_BARIAH_DECISIONS_IMPLEMENTED
INSTANCE_MAPPING_COMPLETE · READY_FOR_MICROSOFT_POWERPOINT_SMOKE
NOT_FOR_MMD_BUILD
NOT_CANONICALLY_FROZEN · MULTIMEDIA_NOT_PRODUCED
```

## 2.2 The nine component mains still said your decision was pending

This is the one worth your attention. On 2 August you settled two things about component-main
screens: that a visual is required, and that the treatment is several smaller visuals as an
overview. The overview mapping was then frozen at 9/9 and built into v0.4.4 — the visuals are
**there**, on the page, in the cardinalities you ruled.

But the metadata block underneath them still said `CONDITIONAL`, still said `PENDING_HUMAN`
on eight of the nine, and still called the treatment a provisional proposal. A reader of the
production panel would have concluded your decision was outstanding when it was implemented.

All nine now read:

```
keperluan visual: REQUIRED
kuasa keperluan:  BARIAH_DIRECT_SCREENSHOT
rawatan:          SOURCE_BOUND_OVERVIEW
kuasa rawatan:    BARIAH_DIRECT_SCREENSHOT
status pemetaan:  RESOLVED
pemetaan instans: COMPLETE
menunggu keputusan manusia: TIDAK
```

**We have not credited you with anything you did not say.** You settled the requirement and
the treatment. You named a *subject* for none of the nine — except the two Papan Tanda
figures — so every subject on every overview is still recorded as coming from the module's
own sources, and the visual directions themselves carry exactly the authority they carried
before. The count of promotions we made on your behalf is zero, and there is a gate on it.

The old `CONDITIONAL` / pending / provisional wording is not deleted from the record; it is
kept as lineage in `COMPONENT_MAIN_VISUAL_GOVERNANCE_v0.4.4.1.json`, just no longer printed
as the live status of a settled question.

## 2.3 An off-stage shape was passing a geometry check by accident

Housekeeping, no visible effect. Every slide carries a PowerPoint title placeholder parked
above the top edge — it is what the outline pane, the accessibility tree and Ctrl+F use to
identify a slide, and it never paints in Slide Show. It was passing our four-edge geometry
check because that check used a threshold picked to clear it, which meant any stray shape
parked in the same band would have passed too. The same was true of the production panel off
to the left.

Both are now explicit registry entries matched on placeholder type, shape name and exact
coordinates; the thresholds are back to normal; and four fixtures confirm that an ordinary
shape at those same coordinates — including one renamed to impersonate the placeholder —
fails. Nothing was moved or deleted.

# 3. Unchanged and re-verified

| | |
|---|---|
| Overview counts | 5, 5, 3, 3, 3, **2**, 3, 2, **1** — Papan Tanda 2, BBQ Pit 1 |
| Slide 5 | *Asas Pembinaan* and both bullets, unchanged, still in the VO |
| Pop-up treatment | one large focused panel; all 30 specification pop-ups still text-led |
| Persistence | all 22 component-main states carry the same overview by subject identity |
| S01 Notes | exactly three spoken blocks; the two lines without full stops |
| Cast | *Alya* and *Encik Rahman* on their approved screens only |
| Quiz | *Pilihan jawapan tepat.* / *Pilihan jawapan tidak tepat.*, not spoken |
| Embedded media | none |

# 4. What is still open, and who owns it

Nothing here is yours to close:

- **MS2680 verification** — source authority.
- **`B02-CAIR-INT-001`**, canonical module DOCX integrity — Firdaus / CAIR.
- **PL06 pronunciation precedence** — source governance. The rule stays `RESERVED_NOT_ACTIVE`
  and is implemented nowhere in this deck.

# 5. Standing — please note before circulating

`REVIEW_CANDIDATE` · `FINAL_BARIAH_DECISIONS_IMPLEMENTED` · `INSTANCE_MAPPING_COMPLETE` ·
`READY_FOR_MICROSOFT_POWERPOINT_SMOKE` · `NOT_FOR_MMD_BUILD` · `NOT_CANONICALLY_FROZEN` ·
`MULTIMEDIA_NOT_PRODUCED`

**This deck has not been opened in Microsoft PowerPoint.** This container has no Impress
import filter, so it cannot run the test. `MICROSOFT_POWERPOINT_EQUIVALENCE` is not claimed
and the smoke test is the next step — please do not circulate before it passes. 100 pages
were rendered and inspected here with the frozen package renderer and the layout is
identical to v0.4.4, page for page.

One honest note on the numbers in the QA report: they measure the checks, not the courseware.
This stage exists because a fully green suite shipped four releases with the wrong version
stamped on every page — and two of the gates covering that metadata were the reason it could
not be seen. If something looks wrong to you, it is worth more than the count.
