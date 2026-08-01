# B02_V0_4_4_IMPLEMENTATION_DELTA

Authored at **Stage 4.2E-A**. **v0.4.4 is not generated here.** This is the controlled list of every change the frozen decisions require, so the generating stage implements a specification rather than a memory.

Base deck `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_3.pptx`, SHA-256 `b9c24dac48047581f31b4f4cb165d3cf419851d1a845f2d2caf87edba034924f` — unchanged by this stage.

| Authority | Evidence |
|---|---|
| `D1` | B02_BARIAH_DECISION_TAMBAHAN_TEXT.png — 6:48 PM |
| `D2` | B02_BARIAH_DECISION_VISUAL_PERSISTENCE.png — 6:52 PM |
| `D3` | B02_BARIAH_DECISION_CAST_QUIZ_VO_PUNCTUATION.png — 7:03 PM |
| `LMS` | Firdaus / LMS owner ruling, Stage 4.2E-A |

| Metric | Value |
|---|---:|
| `ITEMS` | 12 |
| `ITEMS_REQUIRING_DECK_CHANGE` | 10 |
| `ITEMS_EXPLICITLY_NO_CHANGE` | 2 |
| `NEW_QA_GATES` | 44 |
| `NEW_MUTATION_FIXTURES` | 23 |
| `PAGES_NEEDING_VISUAL_PERSISTENCE_REPAIR` | 13 |
| `HUMAN_DECISIONS_SELF_RESOLVED` | 0 |

## Structural invariants — none of these may move

```
REVIEW_PAGES                      = 100
LEARNER_SCREENS                   = 29
RUNTIME_STATES                    = 100
INTERACTION_ITEMS                 = 54
SOURCE_ROWS                       = 26
SOURCE_ASSETS                     = 14
COMPONENTS                        = 9
SLIDES_MANUALLY_PATCHED           = 0
NEW_CANONICAL_PATTERN_IDS_MINTED  = 0
```

Two items are **explicitly no-change** and are listed so the generating stage does not implement them by momentum: item 4 (specification popups keep no visual) and item 12 (PL06 pronunciation stays inactive).

---

# 1. Slide 5 — Asas Pembinaan on-screen and VO parity

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D1

> Bariah's 4:40 PM corrected slide already showed this structure; the v0.4.3 deck collapsed it to one compressed bullet. D1 makes the omission explicit.

## Changes

**controlled_content**

- Add a controlled field on STRUKTUR_PERSISIR_AIR carrying heading 'Asas Pembinaan' and the two bullets VERBATIM from D1, with NO trailing full stop on either bullet.
- Replace the compressed 4th display bullet 'Asas stabil dan rata, dengan saliran permukaan yang berkesan' with the full D1 wording.
- ONE field derives both surfaces — on-canvas text and spoken VO — as with learner_interaction_instruction. Do not maintain two typed copies.

**generator**

- Render 'Asas Pembinaan' as a sub-heading with two sub-bullets on the component-main body, matching Bariah's corrected slide 5 layout.
- Measure the body block from wrapped text; the screen gains two lines.

**notes_writer**

- The VO already states both facts. Assert parity rather than adding copy: the canvas text must be derivable from the same field the VO uses.

**model**

- No change. NEW_LEARNER_SCREEN = false, no new runtime-state family.

## QA gates

- `SLIDE5_ASAS_PEMBINAAN_HEADING_PRESENT`
- `SLIDE5_ASAS_PEMBINAAN_BULLETS_EXACT`
- `SLIDE5_BULLETS_CARRY_NO_TRAILING_PERIOD`
- `SLIDE5_CANVAS_VO_PARITY`
- `LEARNER_SCREENS_UNCHANGED`
- `REVIEW_PAGES_UNCHANGED`

## Mutation fixtures

- remove the Asas Pembinaan heading
- truncate bullet 1 to the old compressed wording
- add a trailing full stop to a bullet

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| RP-005 full-page render | slide 5 |

---

# 2. Component-main overview visuals — REQUIRED for all nine

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D2

## Changes

**visual_policy**

- COMPONENT_MAIN_SCREEN visual_requirement CONDITIONAL -> REQUIRED.
- Retire the PROVISIONAL_VISUAL_PROPOSAL marker; proposal_class becomes None.
- Treatment field = SEVERAL_SMALLER_VISUALS_AS_OVERVIEW.
- Subjects come from the module's own source-attested component visual, now ratified. D2 confirms requirement and treatment, NOT new subjects — invent nothing.

**generator**

- Render the component-main direction as an overview set rather than a single grey line, sized smaller than a popup panel.

**model**

- No change.

## QA gates

- `COMPONENT_MAIN_VISUAL_REQUIREMENT_IS_REQUIRED`
- `COMPONENT_MAINS_PENDING_HUMAN = 0`
- `COMPONENT_MAINS_RESOLVED_BY_BARIAH = 9`
- `COMPONENT_MAIN_SELF_RESOLVED_BY_CC = 0`
- `COMPONENT_MAIN_OVERVIEW_TREATMENT_APPLIED`
- `NEW_VISUAL_SUBJECTS_INVENTED = 0`

## Mutation fixtures

- downgrade one component main to CONDITIONAL
- replace a component-main subject with a generated 'Pelbagai {name}' string

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| all 9 component-main base pages | slides 5, 13, 21, 27, 34, 51, 62, 72, 85 |

---

# 3. Example / information popup — larger, focused visual

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D2

## Changes

**visual_policy**

- EXAMPLE_POPUP and INFORMATION_POPUP treatment = LARGE_FOCUSED.
- Requirement itself unchanged (REQUIRED since the 4:37 PM ruling).

**generator**

- Widen the popup visual panel and increase the direction's prominence relative to the component-main overview, so the size relationship Bariah describes is visible: smaller and many on the main, larger and single in the popup.

## QA gates

- `EXAMPLE_POPUP_VISUAL_TREATMENT_IS_LARGE_FOCUSED`
- `POPUP_VISUAL_PANEL_LARGER_THAN_COMPONENT_MAIN_OVERVIEW`
- `EXAMPLE_POPUPS_WITHOUT_VISUAL = 0`

## Mutation fixtures

- shrink a popup visual panel below the component-main overview size
- remove a popup visual panel

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| a popup page from each of Family S and Family P1 | slides 7, 36 |

---

# 4. Specification popup — still no visual

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D2 (confirms the 4:37 PM ruling)

## Changes

**visual_policy**

- SPECIFICATION_POPUP remains NOT_REQUIRED. D2 does not reopen it.
- No change to code; this item exists so the gate is not weakened by the surrounding work on the other popup subtypes.

## QA gates

- `SPECIFICATION_POPUPS_WITH_UNNECESSARY_VISUAL_PANEL = 0`
- `NOT_REQUIRED_VISUAL_POPUPS_FORCED_TO_HAVE_VISUAL = 0`

## Mutation fixtures

- force a visual panel onto a specification popup (existing fixture R-009)

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| a specification popup page | slide 52 |

---

# 5. Visual persistence through all-viewed and return states

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D3

## Changes

**runtime_state_persistence**

- Derive the component-main visual from the LEARNER SCREEN, not from the page's runtime state classification — the same correction made for selection screens at Stage 4.2C.
- 13 pages across 5 screens currently lose it: see B02_PINNED_POPULATION_TARGETS_v0.4.4.json.

**generator**

- render_family_p1 and render_family_p2 must draw the component-main visual on every state of the screen, including specification-popup and all-viewed states.

**visual_policy**

- Expose a screen-level accessor so generator and validator share ONE population helper.

## QA gates

- `COMPONENT_MAIN_STATES_MISSING_OVERVIEW_VISUAL = 0`
- `COMPONENT_MAIN_STATE_PAGES_EVALUATED = 22`
- `COMPONENT_MAIN_SCREENS_IDENTIFIED = 9`

## Mutation fixtures

- remove the overview visual from a specification-popup state
- remove it from an all-viewed state
- remove it from a return state whose review_page_role differs from the base

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| all 13 pages in the pinned target list | slides 50, 52-56, 70, 84, 86-90 |

---

# 6. Alya and Encik Rahman — provenance upgrade

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D3

> Reuse is conditional. 'jika bersesuaian' is a judgement retained by the reviewer; no automatic propagation to other Bahagian/Topik/PL.

## Changes

**interaction_metadata**

- CAST_PROVENANCE_REGISTER: CONFIRMED_LOCAL_ARTIFACT -> CONFIRMED_BARIAH_DIRECT.
- DIRECT_BARIAH_NAME_PROVENANCE: PENDING -> CONFIRMED.
- Add REUSE_POLICY = APPROVED_WHERE_CONTEXTUALLY_APPROPRIATE with scope Bahagian/Topik/PL.

**generator**

- No change. Names already render; only their provenance class moves.

## QA gates

- `CAST_PROVENANCE_CONFIRMED_BARIAH_DIRECT`
- `HILMI_PROVENANCE_UNCHANGED`
- `CAST_AUTO_INSERTED_INTO_UNRELATED_SCREENS = 0`

## Mutation fixtures

- insert Alya into a screen with no cast binding

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| RP-002 (S02 scenario) | slide 2 |

---

# 7. Exact quiz feedback strings

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D3

## Changes

**controlled_content**

- correct_feedback = 'Pilihan jawapan tepat.'
- incorrect_feedback = 'Pilihan jawapan tidak tepat.'
- Both carry a trailing full stop, verbatim from D3.

**quiz_feedback**

- Learner feedback after submission renders exactly these two strings.
- Replace the current per-question 'Pilihan jawapan tepat. / tidak tepat.' variants only if they differ from these strings verbatim.

**generator**

- Feedback derives from the controlled field, not from typed copy on the quiz pages.

## QA gates

- `QUIZ_CORRECT_FEEDBACK_EXACT`
- `QUIZ_INCORRECT_FEEDBACK_EXACT`
- `QUIZ_FEEDBACK_STRINGS_FROM_CONTROLLED_FIELD`
- `QUIZ_FEEDBACK_AFTER_SUBMISSION_PRESENT = 5`

## Mutation fixtures

- reword one feedback string
- drop the trailing full stop from a feedback string

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| all 5 quiz question pages | slides 93-97 |

---

# 8. No quiz rationale in Speaker Notes

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D3

## Changes

**notes_writer**

- Assert that no per-question rationale text reaches the Notes.
- Detailed rationale is retained in PRODUCTION metadata only and is not deleted.

**quiz_feedback**

- QUIZ_RATIONALE_SPEAKER_NOTES = NOT_REQUIRED. QUIZ_FEEDBACK_VO = NOT_REQUIRED unless separately authorised.

## QA gates

- `QUIZ_RATIONALE_IN_SPEAKER_NOTES = 0`
- `QUIZ_FEEDBACK_IN_SPOKEN_VO = 0`
- `QUIZ_RATIONALE_RETAINED_IN_PRODUCTION_PANEL = 5`

## Mutation fixtures

- move a rationale string into a quiz page's Notes
- add a feedback string to the spoken export

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| all 5 quiz question pages, Notes and panel | slides 93-97 |

---

# 9. No micro-control VO

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D3

## Changes

**notes_writer**

- Keep the bounded parity scope: only screen-level 'Klik pada setiap' instructions are spoken.

**interaction_metadata**

- Add an explicit conformance denylist for Tutup, Kembali, Semak Jawapan, Ulang Kuiz and close-icon instructions so they cannot be silently added to spoken VO later.
- Production metadata describing control behaviour is NOT removed.

## QA gates

- `MICRO_CONTROL_VO_STRINGS_IN_SPOKEN_EXPORT = 0`
- `SCREEN_LEVEL_CLICK_VO_PRESENT`
- `MICRO_CONTROL_DENYLIST_EVALUATED`
- `MICRO_CONTROL_SCOPE_SELF_RESOLVED = 0`

## Mutation fixtures

- add 'Klik Tutup untuk kembali' to a popup page's spoken VO
- add 'Klik Semak Jawapan' to the quiz result VO

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| a popup page, the quiz result page | slides 7, 98 |

---

# 10. S01 punctuation removal

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** D3

> Two Stage 4.2C oracle records (S1-c, S1-d) move MEDIUM punctuation confidence -> RESOLVED. Their transcription is superseded by a direct ruling, not corrected.

## Changes

**model**

- spoken_transcript_elements: drop the trailing full stop from PL06_TITLE and TOPIC_BAHAGIAN_TITLE. MULA_INSTRUCTION is unchanged and keeps its full stop.
- Block count stays 3.

**notes_writer**

- No structural change; the three typed blocks are preserved.

**oracle_registry**

- Update the Stage 4.2C screenshot oracle's spoken_after list so the S01 gates assert the new strings.

## QA gates

- `S01_LINE_1_NO_TRAILING_PERIOD`
- `S01_LINE_2_NO_TRAILING_PERIOD`
- `S01_LINE_3_TRAILING_PERIOD_RETAINED`
- `SHOT_S01_PACKAGE_NOTES_EXACT`
- `S01_SPOKEN_ELEMENTS = 3`

## Mutation fixtures

- restore a trailing full stop to line 1
- remove the full stop from line 3

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| RP-001 Notes | slide 1 |

---

# 11. Tamat close-window -> course-menu metadata

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** LMS_OWNER_RULING (not Bariah)

> Authority is Firdaus / LMS owner. Recorded under that authority, not as a Bariah ruling.

## Changes

**interaction_metadata**

- Record in the production panel: 'Learner menutup lesson/content window untuk kembali ke course menu dan memilih bahagian pembelajaran seterusnya.'
- Record AUTOMATIC_NEXT_ROUTE = not proven and LMS_SHELL_NEXT = not proven.

**generator**

- Learner-facing copy is NOT changed. 'Teruskan pembelajaran ke bahagian seterusnya.' stays exactly as is.

## QA gates

- `TAMAT_LEARNER_COPY_UNCHANGED`
- `TAMAT_NAVIGATION_METADATA_PRESENT`
- `TAMAT_UNVERIFIED_PHYSICAL_NAVIGATION_CLAIM = 0`

## Mutation fixtures

- put the close-window mechanism into the learner canvas
- assert an automatic next route in the panel

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| RP-100 canvas and panel | slide 100 |

---

# 12. PL06 pronunciation stays inactive

**Authority:** `BARIAH_DIRECT_SCREENSHOT` · **Evidence:** NONE — no ruling exists

> PRECEDENCE_OVER_V0_2 = PENDING_SOURCE_GOVERNANCE_RATIFICATION, IMPLEMENTATION_STATUS = RESERVED_NOT_ACTIVE. Carried as open decision OD-10. Listed here so the generating stage does not implement it by momentum.

## Changes

**model**

- NO CHANGE.

**notes_writer**

- NO CHANGE.

**interaction_metadata**

- NO CHANGE. The generic course rule string stays in the S01 production panel exactly as it is.

## QA gates

- `PL06_PRONUNCIATION_IMPLEMENTED = false`
- `S01_NOTES_ALTERED_FOR_PRONUNCIATION = false`

## Mutation fixtures

- none — a fixture would assert an unratified obligation

## Rendered inspection · PowerPoint resmoke

| Inspect | Resmoke |
|---|---|
| none | none |

---

# Change groups, consolidated

| Group | Items touching it |
|---|---|
| `model` | 1, 2, 10, 12 |
| `controlled_content` | 1, 7 |
| `generator` | 1, 2, 3, 5, 6, 7, 11 |
| `notes_writer` | 1, 8, 9, 10, 12 |
| `visual_policy` | 2, 3, 4, 5 |
| `runtime_state_persistence` | 5 |
| `quiz_feedback` | 7, 8 |
| `interaction_metadata` | 6, 9, 11, 12 |
| `oracle_registry` | 10 |

# What this delta does not authorise

- Generating v0.4.4. That is the next stage.
- Any change to the v0.4.3 deck, which stays byte-identical.
- Implementing the PL06 pronunciation rule — see item 12 and open decision OD-10.
- Inventing a visual subject. D2 ratifies the requirement and the treatment; the subjects remain the module's own source-attested text.
- Propagating Alya and Encik Rahman into unrelated screens. Reuse is conditional on contextual suitability.
- Microsoft PowerPoint smoke testing. The resmoke targets above are a list for that stage, not a claim that anything has been tested.
