# STAGE_4_2F_B0_6_RUN_MANIFEST

```
STAGE   = 4.2F-B0.6 — INCORPORATE BARIAH PARTIAL RULINGS
SCOPE   = EVIDENCE FREEZE, DECISION REGISTRATION AND REVISED DRAFTS ONLY
PPTX_GENERATED    = 0
GENERATOR_TOUCHED = 0
APPROVED_ITEMS    = 0
MMD_ASSETS_MADE   = 0
VERDICT = T04_PARTIAL_RULINGS_INCORPORATED_READY_FOR_FINAL_BARIAH_CLARIFICATIONS
```

# 1. Pre-flight

| Check | Result |
|---|---|
| Repository / branch | `/home/user/slide-interaction-layer` · `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at start | `88c415577939e5cc1ab63ead76ae80f10bf359ae` — matches `88c4155` |
| Working tree | clean |
| Stage 4.2F-B0.5 commit | present |
| T04 pre-storyboard QA | **107 / 107** |
| T04 decision-pack mutations | **39 / 39 detected** |
| T04 controlled source rows | **100** |
| Screen candidates | **6** |
| SmartArt assets | **1** |
| Raster source images | **0** |
| B02 families propagated | **0** |

## 1.1 DOCX-dependent fixtures, reported separately

The Stage 4.2F-B0 extraction fixtures split into two populations:

| Population | Result |
|---|---|
| Source-independent (`D-01`…`D-30`) | 30 ran, **30 detected**, 0 missed |
| DOCX-dependent (`E-01`…`E-04`) | **`SKIPPED_NO_DOCX`** |

**The four skipped fixtures are not counted as passing.** The primary DOCX was deleted at the
end of Stage 4.2F-B0 by that stage's cleanup rule; re-running them requires re-obtaining the
source.

# 2. Bariah evidence, frozen byte-identically

Both files were written from the bytes delivered with this stage's instruction. Nothing was
cropped, recompressed, rotated or annotated.

| | `T04-EV-01` | `T04-EV-02` |
|---|---|---|
| Frozen file | `T04_BARIAH_VISUAL_REQUIREMENT_SHEET_20260802.jpg` | `T04_BARIAH_QUIZ_RUMUSAN_WHATSAPP_20260802.webp` |
| Bytes | 75,362 | 121,162 |
| SHA-256 | `95f84819c70b6ef89fb8fe29ddd8ac19850014790de18587a0cfe850637a2008` | `0ae2aa29a05640495f42863b9c5e7daa2a1adaa1961f925951b9e393fd2154e9` |
| Media type | `image/jpeg` | `image/webp` |
| Dimensions | 772 × 697 | 1076 × 1338 |
| Evidence date | 2026-08-02 | 2026-08-02 |
| Reviewer | BARIAH | BARIAH |
| Class | `BARIAH_DIRECT_SCREENSHOT` | `BARIAH_DIRECT_SCREENSHOT` |
| Scope | `K5-PL06-T04-B01` | `K5-PL06-T04-B01` |

Location: **`reviews/storyboard-bariah/t04_bariah_review/`** — a sibling of the existing
`v0_3_bariah_review/` inside the Bariah evidence hierarchy that already exists. No new
governance hierarchy was created, and no existing evidence file was touched.

**Filename limitation, stated rather than hidden.** The original uploaded filenames are **not
recoverable**. The images arrived as inline image blocks on the instruction message rather than
as named files in the upload area, and no filename is carried anywhere in the session record. I
checked. The frozen names were assigned by me, following the B02 naming pattern already in that
directory, and both are recorded as `NOT_RECOVERABLE_FROM_SESSION_TRANSPORT`. The bytes are the
evidence; the names are not.

Eleven ruling locators were transcribed verbatim from the two images — `BR-L1`…`BR-L6` from the
requirement sheet, `BR-W1`…`BR-W5` from the WhatsApp messages.

# 3. Decision status, exactly as registered

| | Decision | Status | Ruling |
|---|---|---|---|
| `D-01` | Visual treatment | **`CONFIRMED_WITH_EXPANSION`** | `VISUAL_REQUIRED_FOR_BARIAH_NAMED_POPULATION` |
| `D-02A` | Quiz composition | **`CONFIRMED_BARIAH_DIRECT`** | 4 MCQ + 1 MR · scope `ALL_PLS_IN_KURSUS` |
| `D-02B` | Passing threshold | **`UNRESOLVED`** | — |
| `D-02C` | Rumusan | **`DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW`** | follow Topik 3 Bahagian 2 style |
| `D-03` | T04 cast | **`UNRESOLVED`** | — |
| `D-04` | Legislative content | **`CLARIFICATION_REQUIRED`** | — |
| `D-05` | SmartArt production | **`PARTIALLY_RESOLVED`** | `EVERY_PROCESS_STEP_REQUIRES_A_VISUAL` |

Three prior recommendations are recorded as **superseded, not approved**:
`TEXT_AND_DIAGRAM_LED` (D-01), `HILMI_NARRATOR_LED` (D-03), and the base/reveal split (D-04).
`APPROVED_ITEMS = 0`.

**A scope asymmetry, recorded not escalated.** Under Landskap Lembut Bariah wrote *"Their sub –
perlu visual"*. Under Landskap Kejur she named four groups and stopped — the eight source
sub-items beneath those four are not covered by her ruling. The inventory covers exactly what
she named and creates nothing for the eight. The asymmetry may well be deliberate: the Kejur
sub-items are one-line examples, the Lembut sub-items are full management topics. It is written
into the ruling record rather than turned into a seventh question, because the brief prohibits
asking her to restate a ruling she gave clearly.

# 4. Visual obligations — 46

| Group | Ruling | Count |
|---|---|---:|
| A — six process nodes, one obligation each | `BR-L1` | 6 |
| B — Landskap Lembut main explanation | `BR-L2` | 1 |
| B — Siram, Baja, Racun main explanations | `BR-L3` | 3 |
| B — descendants of the three operations | `BR-L4` | 31 |
| C — Landskap Kejur main explanation | `BR-L5` | 1 |
| C — the four named Kejur groups | `BR-L6` | 4 |
| **TOTAL** | | **46** |

The BR-L4 descendants, enumerated rather than left as *their subtopics*: **Siram 8, Baja 10,
Racun 13**. Every one is bound to its own source rows. The population is derived from the
controlled extract by code, and a gate recomputes it independently, so the counts are checkable
against the source rather than asserted.

```
existing raster source images   0
existing source assets          1  (T04-DGM-01, the SmartArt)
NEW_MMD_ASSET_REQUIRED         46
PENDING_HUMAN                   3  (the three "Aspek Pengurusan untuk Kontraktor" grouping
                                    headings — a heading with no body text of its own has no
                                    subject, and inventing one is not mine to do)
```

**Two authorities, never merged.** Every obligation carries
`treatment_authority = BARIAH_DIRECT_SCREENSHOT` (she required a visual) and
`subject_authority = MODULE_SOURCE_ATTESTED` (what it shows comes from the module). Bariah
required visuals; she did not specify a single subject. Labelling any subject `BARIAH_DIRECT`
would invent a ruling she never gave.

The six process-node obligations record `SOURCE_SMARTART_NODE_LABEL_ONLY` — the source holds
the six node *labels*, not six step illustrations. No obligation anywhere claims an image the
module does not contain.

# 5. Screen-mapping impact

**The six-candidate map cannot hold the ruling.** 18 of 46 obligations land on an existing
candidate; **28 have no screen at all** — the Siram, Baja and Racun subtopics, which the v1 map
compressed into three reveals on one screen. All 28 are listed by ID rather than absorbed.

| | Stage 4.2F-B0.5 | Stage 4.2F-B0.6 |
|---|---|---|
| Source visuals | 1 | 1 — unchanged |
| Required visuals | not counted | **46** |
| Screens with a visual treatment | 1 of 6 | 5 of 6 |
| Obligations with no screen | — | **28** |

`FINAL_SCREEN_COUNT = NOT_CLAIMED`. Every contract keeps its v1 visual treatment as
`superseded_visual_treatment`, so the change the ruling forced is visible rather than
overwritten. **`B02_FAMILIES_PROPAGATED = 0`** — B02's Family S / P1 / P2 structure exists to
organise 14 extracted photographs into overview cardinalities; T04 has zero raster source
images, so there is nothing for it to organise.

**The portability prediction inverts.** Stage 4.2F-B0.5 predicted visual-treatment reuse would
be the lowest row because T04 has 1 visual against B02's 14. With 46 required visuals it is not
merely the lowest reuse row — it is the largest single production item in the unit.

# 6. Rumusan v2

Four statements, down from five, because **SR-02 — the four-point rule — is part of the Topik 3
Bahagian 2 style Bariah instructed.** Ten style characteristics were extracted from the
approved B02 treatment and every one is recorded with what was observed and how it was applied.
No B02 fact appears anywhere in the draft; a gate checks eleven B02 component names against it.

T04 has five structural blocks against B02's four, so exactly one merge was unavoidable. The
compliance statement was merged into the contractor-outcome point — which is where B02's own
fourth point sits. The full v1→v2 mapping is published so nothing was dropped silently.

`T04-RUM2-04` carries the **MEDIUM** factual-risk flag, preserved deliberately. Worth noting
for Bariah: B02's approved Rumusan ends on the same *"Kontraktor dapat …"* shape, so the style
rule itself invites the generalisation — that does not make the T04 source support it.

`content_status = CAIR_ASSISTED_DRAFT` · `approval_status = PENDING_BARIAH_REVIEW` ·
`instructional_authority = BARIAH`.

# 7. Quiz blueprint v2 — five slots

```
QUIZ_COMPOSITION = CONFIRMED_BARIAH_DIRECT     4 MCQ + 1 Multiple Response
SCOPE            = ALL_PLS_IN_KURSUS
PASS_THRESHOLD   = UNRESOLVED
QUIZ_CONTENT     = BLUEPRINT_ONLY
FINAL_AUTHORITY  = BARIAH
```

| Slot | Type | From | Learning point |
|---|---|---|---|
| Q1 | MCQ | `QB-01` | the three soft-landscape operations |
| Q2 | MCQ | `QB-02` | irrigation method selection |
| Q3 | MCQ | `QB-05` | IPM control priority order |
| Q4 | MCQ | `QB-06` | the four hard-landscape functions |
| Q5 | MR | `QB-03` + `QB-04` | pesticide legal, licensing and HSE obligations |

**Six coverage points into five slots, 0 discarded.** `QB-03` and `QB-04` merge into Q5: they
are the same compliance cluster split by heading, not by concept, and the source presents those
controls as co-applying rather than as alternatives. The cost is named — the statute's *name*
no longer has a stem of its own, and if Bariah wants it tested by name it has to displace
another slot.

No stem, option, key, rationale or feedback was written. The 60 percent figure is **not**
carried forward as a default.

# 8. What is still unresolved

| # | Decision | Status |
|---|---|---|
| 1 | `D-02B` passing threshold | `UNRESOLVED` |
| 2 | `D-03` T04 cast / narrator | `UNRESOLVED` — three options, this unit only |
| 3 | `D-04` legal base/reveal split | `CLARIFICATION_REQUIRED` |
| 4 | `D-05` SmartArt review and MMD treatment | `PARTIALLY_RESOLVED` — three confirmations |
| 5 | `D-02C` Rumusan draft review | drafted, awaiting review |
| 6 | `D-02A` five-slot blueprint review | composition settled, content not |

**D-04 answered concretely.** Bariah asked *"Kandungan Akta - Tak pasti ni yang di mana?"* The
answer is nineteen source rows in nine groups, every one listed individually with its wording,
proposed treatment and a confirmation field. Stage 4.2F-B0.5 counted eleven — sweeping the
whole unit for compliance instructions rather than just the Racun section found four more in
Baja (PPE, storage, specification compliance, documentation) plus four structural headings.
Only **three** rows are proposed as reveal candidates, and all three expand a duty already
stated on the base screen. **The split is not applied to any contract** —`T04-CT-04` still
carries every row in its base state, which is the safe position until she confirms.

**D-05** shows the six node labels in order, with the layout, hash and the measured fact that
the source hierarchy is flat — so a redraw that introduces a tree or a grouping would assert a
relationship the source does not contain.

# 9. WhatsApp follow-up

Malay, WhatsApp-ready, no QA terminology. Thanks Bariah, summarises the three rulings already
recorded, asks only the six open items, states that no storyboard has been generated and that
the Rumusan and quiz remain drafts. **`DRAFT_NOT_SENT`** — sending is Firdaus's call.

# 10. QA and mutations

| | |
|---|---:|
| Rulings gates | **130 / 130**, 0 markers |
| Rulings fixtures | **26 / 26 detected**, 0 missed, 0 baseline false failures |
| Decision-pack gates (4.2F-B0.5) | 107 / 107 |
| Extraction gates (4.2F-B0) | 109 / 109 |
| PL06 inventory gates (4.2F-A2) | 140 / 140 |

Five gates failed on first run — all five my own false positives, all fixed at the gate. And
the fixtures caught a real defect of mine: **five of nineteen visual-obligation IDs in the D-04
sheet were wrong**, typed before the inventory existed. See the QA report §2 and §3.

# 11. Constraints honoured

- **No PPTX generated.**
- No production storyboard generator modified — 0 changed files under `reviews/source-completion/`.
- No MMD asset production, no React, no SCORM.
- No unresolved decision marked approved — `APPROVED_ITEMS = 0`.
- No final quiz question, option, key or rationale.
- CAIR is not named as Instructional Designer anywhere.
- `88c4155` not amended.
