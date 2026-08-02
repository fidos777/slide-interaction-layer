# STAGE_4_2F_B0_7_RUN_MANIFEST

```
STAGE   = 4.2F-B0.7 — CONSOLIDATE FINAL BARIAH STRUCTURAL RULINGS
SCOPE   = EVIDENCE FREEZE AND CONTROLLED DECISION ARTIFACTS ONLY
PPTX_GENERATED          = 0
GENERATOR_TOUCHED       = 0
MMD_PRODUCTION_STARTED  = 0
VERDICT = T04_STRUCTURAL_RULINGS_CLOSED_READY_FOR_CONTENT_APPROVAL
```

```
CONFIRMED_POLICY_DECISIONS                 = 6   D-01, D-02A, D-02B, D-02C, D-04, D-05
CONDITIONALLY_CONFIRMED_DECISIONS          = 1   D-03
APPROVED_FINAL_INSTRUCTIONAL_CONTENT_ITEMS = 0
PENDING_BARIAH_CONTENT_REVIEWS             = 4
```

# 1. Pre-flight

| Check | Result |
|---|---|
| Repository / branch | `/home/user/slide-interaction-layer` · `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at start | `7a792e884968aae6179265ac198b555bad77d9b9` — matches `7a792e8` |
| Working tree | clean |
| Stage 4.2F-B0.6 commit | present |
| B0.6 QA | **130 / 130** |
| B0.6 mutations | **26 / 26 detected** |
| `T04-EV-01` byte-identical | **yes** — `95f84819…637a2008`, 75,362 B |
| `T04-EV-02` byte-identical | **yes** — `0ae2aa29…fd2154e9`, 121,162 B |

# 2. Evidence — a delivery discrepancy, stated plainly

**The instruction says three screenshots are attached. One arrived.**

I checked the instruction message payload, the session upload area and the transcript. Exactly
one image block was delivered. That one image carries **all three** confirmations the
instruction describes — the legal split, the 60 percent pass mark with the Slide 2 dialogue
ruling, and the six-step diagram — plus the Alya / Encik Rahman condition. So no ruling is
missing; the evidence-item count differs, and it is registered as one item rather than
padded to three.

| | `T04-EV-03` |
|---|---|
| Frozen file | `T04_BARIAH_FINAL_STRUCTURAL_CONFIRMATIONS_20260802.webp` |
| Bytes | 138,074 |
| SHA-256 | `9cf3842e70b24d304bb32e5e3947ece0db2b3bbc826727a3915be80ab068c353` |
| Media type | `image/webp` |
| Dimensions | 1194 × 1520 |
| Evidence date | 2026-08-02 (received 09:22:55 UTC) |
| Reviewer / class | BARIAH · `BARIAH_DIRECT_SCREENSHOT` |
| Scope | `K5-PL06-T04-B01` |
| Modification | **NONE — byte-identical** |
| Original filename | `NOT_RECOVERABLE_FROM_SESSION_TRANSPORT` |

Five ruling locators transcribed verbatim: `BR-C1` … `BR-C5`. Evidence total is now **3
items, 16 locators**.

**One element is not legible.** The quoted proposal in the 4:56 PM message is cropped at the
left margin. What can be read is *"…rator berlesen dan PPE dipaparkan terus pada skrin"* — the
item before "operator berlesen" is cut off, and the word **Akta appears nowhere in the
screenshot**. The statute's place on the base screen is therefore recorded as
`INFERRED_FROM_CROPPED_LINE_PLUS_FIRDAUS_STAGE_INSTRUCTION`, not as a legible Bariah line. A
gate holds that classification, and a fixture proves the gate fires if it is upgraded.

# 3. Decision state — structure is closed

| | Decision | Status | Structural | Changed here |
|---|---|---|---|---|
| `D-01` | Visual treatment | `CONFIRMED_WITH_EXPANSION` | RESOLVED | no |
| `D-02A` | Quiz composition | `CONFIRMED_BARIAH_DIRECT` | RESOLVED | no |
| `D-02B` | Passing threshold | **`CONFIRMED_BARIAH_DIRECT`** | RESOLVED | **yes** |
| `D-02C` | Rumusan | `DRAFT_AUTHORISED_PENDING_BARIAH_REVIEW` | RESOLVED | no |
| `D-03` | Cast and Slide 2 | **`CONFIRMED_WITH_CONDITION`** | CONDITIONALLY_RESOLVED | **yes** |
| `D-04` | Legislative split | **`CONFIRMED_BARIAH_DIRECT`** | RESOLVED | **yes** |
| `D-05` | SmartArt treatment | **`CONFIRMED_BARIAH_DIRECT`** | RESOLVED | **yes** |

**D-02B** — `60_PERCENT`, scope `ALL_PLS_IN_KURSUS`. Stage 4.2F-B0.6 refused to carry the A3
figure forward as a default. Bariah has now confirmed it directly. The figure and the ruling
agree, but it is the ruling that authorises it.

**D-05** — source-bound diagram in the review storyboard, controlled redraw in MMD, six-node
identity and order invariant, production `NOT_STARTED`. Removed from every unresolved list.

# 4. Approval reporting, corrected

Stage 4.2F-B0.6 published a single `APPROVED_ITEMS = 0`. That number conflated two different
things: it was true of learner-facing content and **false of policy**, since Bariah had
already confirmed the visual ruling and the quiz composition. Reporting one figure for both
understated her decisions.

Four typed totals replace it, and `APPROVED_ITEMS` is no longer emitted at all — a gate
asserts the attribute is absent, so it cannot creep back.

# 5. D-04 — the confirmed split, applied

**Base screen, may not be hidden:** the statute (`T04-ROW-066`), the licensed-operator
requirement (`T04-ROW-067`), PPE and its item list (`T04-ROW-069`, `T04-ROW-070`), plus the
three group headings.

**Reveal-eligible:** storage (`071`, `072`), SDS (`073`, `074`), spraying conditions (`076`),
notification (`077`), reporting (`078`).

This is **applied**, not proposed — `T04-CT-04` carries the split and keeps its Stage 4.2F-B0.6
base state as `superseded_base_state`.

**Her ruling is broader than what CAIR recommended, in both directions.** PPE detail moved
*onto* the base screen — Stage 4.2F-B0.6 had proposed it as a reveal candidate and Bariah put
it on screen. And spraying conditions, notification and reporting became reveal-eligible,
which Stage 4.2F-B0.6 had argued against on the grounds that a learner who never interacts
should still see them.

She is the Instructional Designer and she answered the exact question put to her. The ruling is
implemented as written. The residual risk — a non-interacting learner does not see the
spray-drift limit, the notification duty or the reporting duty — is recorded in
`D04_SPLIT.residual_risk` rather than quietly designed around, and it is **not** re-asked in
the follow-up message.

The five Baja-section compliance rows were not part of the question she was asked and stay
base-visible, unchanged.

# 6. D-03 — cast, and the condition that is the ruling

Bariah was asked whether Hilmi alone, narrator-only with no characters, would do. **She
answered against that**: an additional character in a dialogue scenario on Slide 2 — and then
added *"jika Alya & Encik Rahman, sesuai, boleh guna semula. Jika tidak, guna watak baru."*

The condition is half the ruling. Naming the pair without assessing fit would implement the
first half and ignore the second, so a contextual-fit assessment was produced:

| | |
|---|---|
| Result | **`ALYA_ENCIK_RAHMAN_CONTEXTUALLY_SUITABLE`** |
| Scope of that finding | **Slide 2 only** — not the unit |
| Alya — Kontraktor Junior | fits · risk `LOW` |
| Encik Rahman — Mentor / Kontraktor Senior | fits · risk `MEDIUM_IF_UNSCOPED` |
| Specialist expertise needed for Slide 2 | no |
| Specialist expertise needed in the unit | **yes** |
| Unsupported-expertise risk | `MEDIUM` → `LOW` after mitigation |
| Authority | `CAIR_ASSESSMENT_NOT_A_BARIAH_RULING` · `PENDING_BARIAH_REVIEW` |
| `character_instance_mapping` | **`NOT_COMPLETE`** |

**The risk, stated concretely.** The source says pesticide spraying must be done by a licensed
operator. Encik Rahman is a senior contractor, not a licensed operator. If the Slide 2 dialogue
were extended into the Racun material, he would be voicing statutory and licensing obligations
that no source attributes to him — a source citation would become a character's word.

**Mitigation, enforced by gate.** Slide 2 is bound to seven process-and-category rows and to
nothing else. All compliance content stays on `T04-CT-04`, quoted from the source. No character
line may contain a compliance obligation; a fixture proves the gate fires when one does.

A new contract `T04-CT-07` and candidate `T04-SC-07` carry the Slide 2 scenario, with five
drafted dialogue turns marked `CAIR_ASSISTED_DRAFT` / `PENDING_BARIAH_REVIEW` on the same
footing as the Rumusan.

# 7. Obligations are not assets

```
VISUAL_OBLIGATIONS     = 46      retained, unchanged
UNIQUE_ASSET_COUNT     = NOT_YET_DETERMINED
VISUAL_COVERAGE_STATUS = NEW_MMD_VISUAL_COVERAGE_REQUIRED
ASSET_GROUPS           = 7
PRODUCTION_STARTED     = 0
```

46 is a count of **places a visual is required**, not a count of files to produce. One
composite may discharge several obligations — the three fertiliser application methods are a
single comparison in the source — and one obligation may need more than one state. Asserting
`UNIQUE_MMD_ASSETS = 46` would turn a requirement count into a production estimate nobody has
made. A gate blocks that claim in both its structured and its prose form.

Seven asset groups, one planning row per obligation with all eight required fields. Only the
**7** obligations whose source presents a set are marked composite candidates; the other **36**
stay `UNDETERMINED_PENDING_BARIAH`, because a guess dressed as a plan is worse than an open
field.

**Three subjects look reusable and are not** — the two PPE sets (gloves and mask for fertiliser
against respirator, goggles, chemical gloves and suit for pesticide) and the two storage
specifications (dry and secure against locked, labelled and ventilated). Reusing one for the
other would understate the pesticide requirement.

The Slide 2 scenario visual is **not** one of the 46 — Bariah's visual ruling covers content
headings; the scenario screen arrives from a separate ruling.

# 8. Readiness

Structural decisions: **CLOSED**. What remains is content.

| # | Review | Decision |
|---|---|---|
| `CR-1` | Character instance mapping | D-03 |
| `CR-2` | Slide 2 dialogue review | D-03 |
| `CR-3` | Rumusan v2 review | D-02C |
| `CR-4` | Five-slot quiz authoring, editing and approval | D-02A |

**Not claimed:** that the final storyboard is approved — none has been generated; a final
screen count; a unique asset count; that any learner-facing text is approved; that the
character instance mapping is complete.

Mapping v3 adds one candidate (`T04-SC-07`, Slide 2) for seven in total. The **28 unmapped
visual obligations from Stage 4.2F-B0.6 are unchanged** — closing the structural decisions did
not give them a home.

# 9. QA and mutations

| | |
|---|---:|
| Final-rulings gates | **105 / 105**, 0 markers |
| Final-rulings fixtures | **32 / 32 detected**, 0 missed, 0 baseline false failures |
| B0.6 rulings gates | 130 / 130 |
| B0.5 decision-pack gates | 107 / 107 |
| B0 extraction gates | 109 / 109 |
| PL06 inventory gates | 140 / 140 |

The suite passed on first run — which proves nothing on its own. **One fixture failed**:
`W-22` was missed because the gate read a cached total instead of the live plan, so a plan edit
was invisible to it. Fixed at the gate, plus a new `ASSET_TOTALS_AGREE_WITH_THE_LIVE_PLAN`
gate so that staleness class fires on sight. See the QA report §2.1.

# 10. Constraints honoured

- **No PPTX generated.**
- No production storyboard generator modified — 0 changed files under `reviews/source-completion/`.
- **No MMD asset production started** — `mmd_production_status = NOT_STARTED`, 0 asset rows in production.
- No React, no SCORM.
- No unresolved item marked approved; no final instructional content approved.
- CAIR is not named as Instructional Designer anywhere.
- `7a792e8` not amended.
