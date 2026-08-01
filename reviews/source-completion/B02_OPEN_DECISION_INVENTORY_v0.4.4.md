# B02_OPEN_DECISION_INVENTORY — v0.4.4

Stage 4.2E-A. Deck `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_3.pptx`, unchanged.

> **Every Bariah-routed decision is closed. Every Firdaus/LMS decision is closed.**
> What remains is source-authority governance, which neither Bariah nor CC can settle.

| Metric | Count |
|---|---:|
| `OPEN_DECISIONS` | 3 |
| `BARIAH_OPEN_DECISIONS` | 0 |
| `FIRDAUS_LMS_OPEN_DECISIONS` | 0 |
| `SOURCE_AUTHORITY_OPEN_DECISIONS` | 3 |
| `CLOSED_THIS_STAGE` | 8 |
| `CLOSED_BY_BARIAH` | 7 |
| `CLOSED_BY_LMS_OWNER` | 1 |
| `BLOCKING_CURRENT_BARIAH_REVIEW` | 0 |
| `BLOCKING_POWERPOINT_SMOKE` | 0 |
| `BLOCKING_MMD_BUILD` | 1 |
| `BLOCKING_CANONICAL_FREEZE` | 3 |
| `BLOCKING_PRODUCTION` | 3 |
| `RESOLVED_BY_CC_IN_THIS_STAGE` | 0 |

# 1. Closed at this stage

| # | Item | Authority | Closed by | Implementation |
|---|---|---|---|---|
| OD-01 | Eight remaining component-main visual decisions | Bariah | D2 (6:52 PM) + D3 (7:03 PM) | `IMPLEMENTATION_REQUIRED_V0_4_4` |
| OD-01b | 13-page component-main visual persistence gap | Bariah | D3 (7:03 PM) | `IMPLEMENTATION_REQUIRED_V0_4_4 — 13 pages, pinned target list` |
| OD-02 | Exact B02 cast-name provenance — Alya / Encik Rahman | Bariah | D3 (7:03 PM) | `REGISTER_UPDATE_ONLY` |
| OD-03 | Quiz rationale placement | Bariah | D3 (7:03 PM) | `IMPLEMENTATION_REQUIRED_V0_4_4` |
| OD-04 | Micro-control VO scope | Bariah | D3 (7:03 PM) | `CONFORMANCE_TARGET_V0_4_4 — denylist gate, no copy change` |
| OD-05 | Two S01 Speaker-Notes punctuation confirmations | Bariah | D3 (7:03 PM) | `IMPLEMENTATION_REQUIRED_V0_4_4` |
| OD-06 | "Skrin: Tambahan Text" interpretation | Bariah | D1 (6:48 PM) | `IMPLEMENTATION_REQUIRED_V0_4_4` |
| OD-07 | Tamat physical navigation mechanism | Firdaus / LMS owner | LMS-owner ruling, Stage 4.2E-A | `METADATA_ONLY_V0_4_4` |

## Resolutions

**OD-01 — Eight remaining component-main visual decisions**  
`B02-BARIAH-20260801-COMPONENT-MAIN-VISUAL-02` · closed by D2 (6:52 PM) + D3 (7:03 PM)

COMPONENT_MAIN_VISUAL_REQUIREMENT = REQUIRED, several smaller visuals as an overview. All 9 records move PENDING_HUMAN -> RESOLVED_BY_BARIAH.

**OD-01b — 13-page component-main visual persistence gap**  
`B02-BARIAH-20260801-VISUAL-STATE-PERSISTENCE-01` · closed by D3 (7:03 PM)

TECHNICAL_GAP = CONFIRMED, SEMANTIC_OBLIGATION = NOW_CONFIRMED. Every runtime state of a component-main screen retains the same overview visual.

**OD-02 — Exact B02 cast-name provenance — Alya / Encik Rahman**  
`B02-BARIAH-20260801-CAST-PROVENANCE-02` · closed by D3 (7:03 PM)

CONFIRMED_BARIAH_DIRECT. Reuse APPROVED_WHERE_CONTEXTUALLY_APPROPRIATE across other Bahagian/Topik/PL. Hilmi unchanged.

**OD-03 — Quiz rationale placement**  
`B02-BARIAH-20260801-QUIZ-RATIONALE-01` · closed by D3 (7:03 PM)

Learner feedback after submission only: 'Pilihan jawapan tepat.' / 'Pilihan jawapan tidak tepat.' Production metadata YES, Speaker Notes NO.

**OD-04 — Micro-control VO scope**  
`B02-BARIAH-20260801-MICRO-CONTROL-VO-01` · closed by D3 (7:03 PM)

SCREEN_LEVEL_CLICK_VO = REQUIRED, MICRO_CONTROL_VO = NOT_REQUIRED. The conservative Stage 4.2B reading is ratified.

**OD-05 — Two S01 Speaker-Notes punctuation confirmations**  
`B02-BARIAH-20260801-S01-PUNCTUATION-01` · closed by D3 (7:03 PM)

'Buang noktah' — trailing full stops removed from lines 1 and 2. Line 3 keeps its full stop. Three-block structure preserved.

**OD-06 — "Skrin: Tambahan Text" interpretation**  
`B02-D-TAMBAHAN-TEXT-01` · closed by D1 (6:48 PM)

Same screen, additional text, follows the VO. NEW_LEARNER_SCREEN = false; LEARNER_SCREENS = 29 and REVIEW_PAGES = 100 unchanged.

**OD-07 — Tamat physical navigation mechanism**  
`B02-U-03` · closed by LMS-owner ruling, Stage 4.2E-A

Learner closes the lesson/content window and returns to the course menu, then selects the next section. Automatic next route and LMS shell Next both recorded as NOT PROVEN. Learner-facing copy unchanged.

# 2. Still open — source authority only

| # | Item | Authority | Status |
|---|---|---|---|
| OD-08 | MS2680 verification | Source authority — CAIR / module owner | `PENDING_SOURCE_AUTHORITY` |
| OD-09 | B02-CAIR-INT-001 — canonical module DOCX integrity | Firdaus / CAIR — explicitly not Bariah's to close | `PENDING_FIRDAUS_CAIR` |
| OD-10 | L-01 / PL06 pronunciation precedence ratification | Source governance — Universal S&G v1.0 vs B02 S&G v0.2 precedence | `PENDING_SOURCE_GOVERNANCE_RATIFICATION` |

| # | Bariah review | PPT smoke | MMD build | Canonical freeze | Production |
|---|:-:|:-:|:-:|:-:|:-:|
| OD-08 | — | — | — | 🔴 | 🔴 |
| OD-09 | — | — | — | 🔴 | 🔴 |
| OD-10 | — | — | 🔴 | 🔴 | 🔴 |

## Detail

### OD-08 — MS2680 verification

**Authority:** Source authority — CAIR / module owner  
**Status:** `PENDING_SOURCE_AUTHORITY`

**Current safe treatment.** The MS2680 sentence is OMITTED from the S02 dialogue (U-01) and is not replaced by any other standards claim. Nothing in the deck asserts a standard.

**Evidence that would close it.** Whether MS2680 is the correct standard reference, and the clause it supports.

**Impact if unresolved.** A standards citation stays out of the courseware. Safe, but a required reference may be missing.

### OD-09 — B02-CAIR-INT-001 — canonical module DOCX integrity

**Authority:** Firdaus / CAIR — explicitly not Bariah's to close  
**Status:** `PENDING_FIRDAUS_CAIR`

**Current safe treatment.** The 26-row source baseline is derived from the hashed PDF pages 256-269 and is frozen. SOURCE_ROW_COUNT may change only on a proven CLASS-9 correction. SOURCE_INTEGRITY_FULLY_VERIFIED is not asserted.

**Evidence that would close it.** A verified canonical module DOCX, or confirmation that the hashed PDF is canonical for B02.

**Impact if unresolved.** Canonical freeze cannot be declared. Open since Stage 1.

### OD-10 — L-01 / PL06 pronunciation precedence ratification

**Authority:** Source governance — Universal S&G v1.0 vs B02 S&G v0.2 precedence  
**Status:** `PENDING_SOURCE_GOVERNANCE_RATIFICATION`

**Current safe treatment.** Display token PL06 unchanged. Proposed spoken form 'PL enam' is RESERVED_NOT_ACTIVE and is implemented nowhere. The generic course rule string stays in the S01 production panel; S01 Notes and pronunciation metadata are untouched.

**Evidence that would close it.** Ratification that the Universal S&G v1.0 pronunciation rule takes precedence over B02 S&G v0.2, which is silent on pronunciation.

**Impact if unresolved.** TTS would voice PL06 with no pronunciation instruction attached.

*Promoted to a first-class open decision at Stage 4.2E-A. It was previously carried inside the pronunciation register as IMPLEMENTATION_REQUIRED_NEXT_STAGE; that understated it, because the precedence question is not CC's to settle.*

# 3. What this does not mean

Zero Bariah-open decisions does not mean the deck is finished. Seven of the eight closures carry `IMPLEMENTATION_REQUIRED_V0_4_4` — the rulings are frozen, the changes are specified in `B02_V0_4_4_IMPLEMENTATION_DELTA.md`, and **none of them are in the v0.4.3 deck**, which this stage was not permitted to regenerate.
