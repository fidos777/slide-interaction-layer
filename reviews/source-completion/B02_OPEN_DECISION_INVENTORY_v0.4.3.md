# B02_OPEN_DECISION_INVENTORY — v0.4.3

Stage 4.2D. Deck `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_3.pptx`, unchanged.

**Nothing here is resolved by this stage, and nothing here is resolvable by CC.** Each item names the one authority who can close it, what would close it, and what the deck does meanwhile.

| Metric | Count |
|---|---:|
| `OPEN_DECISIONS` | 9 |
| `AWAITING_BARIAH` | 6 |
| `AWAITING_FIRDAUS_OR_LMS_OWNER` | 1 |
| `AWAITING_SOURCE_AUTHORITY` | 2 |
| `BLOCKING_CURRENT_BARIAH_REVIEW` | 4 |
| `BLOCKING_POWERPOINT_SMOKE` | 0 |
| `BLOCKING_MMD_BUILD` | 7 |
| `BLOCKING_CANONICAL_FREEZE` | 9 |
| `BLOCKING_PRODUCTION` | 9 |
| `RESOLVED_BY_CC_IN_THIS_STAGE` | 0 |

# Routing

| # | Item | Authority |
|---|---|---|
| OD-01 | Eight remaining component-main visual decisions | Bariah |
| OD-02 | Exact B02 cast-name provenance — Alya / Encik Rahman | Bariah |
| OD-03 | Quiz rationale placement | Bariah |
| OD-04 | Micro-control VO scope | Bariah |
| OD-05 | Two S01 Speaker-Notes punctuation confirmations | Bariah |
| OD-06 | "Skrin: Tambahan Text" interpretation | Bariah |
| OD-07 | Tamat physical navigation mechanism | Firdaus / LMS owner |
| OD-08 | MS2680 verification | Source authority — CAIR / module owner |
| OD-09 | B02-CAIR-INT-001 — canonical module DOCX integrity | Firdaus / CAIR — explicitly not Bariah's to close |

# Blocking matrix

| # | Bariah review | PPT smoke | MMD build | Canonical freeze | Production |
|---|:-:|:-:|:-:|:-:|:-:|
| OD-01 | 🔴 | — | 🔴 | 🔴 | 🔴 |
| OD-02 | 🔴 | — | 🔴 | 🔴 | 🔴 |
| OD-03 | 🔴 | — | 🔴 | 🔴 | 🔴 |
| OD-04 | 🔴 | — | 🔴 | 🔴 | 🔴 |
| OD-05 | — | — | 🔴 | 🔴 | 🔴 |
| OD-06 | — | — | 🔴 | 🔴 | 🔴 |
| OD-07 | — | — | 🔴 | 🔴 | 🔴 |
| OD-08 | — | — | — | 🔴 | 🔴 |
| OD-09 | — | — | — | 🔴 | 🔴 |

**Nothing blocks the PowerPoint smoke test.** Four items block the current Bariah review, and they are the four she is being asked about. Every item blocks canonical freeze and production; `B02-CAIR-INT-001` has blocked freeze since Stage 1 and is not Bariah's to close.

# Detail

## OD-01 — Eight remaining component-main visual decisions

**Authority:** Bariah  
**Status:** `PENDING_BARIAH`

**Current safe treatment.** Each of the 8 screens shows the module's OWN source-attested visual text, classified CONDITIONAL / PENDING_HUMAN and marked PROVISIONAL_VISUAL_PROPOSAL. Struktur Persisir Air is the only component main with direct authority. The Stage 4.1 'Pelbagai {name}' propagation stays retired.

**Evidence that would close it.** A ruling per screen, or one ruling stating that the module's own visual text is accepted for all eight. Her 4:40 PM caption 'apply to yang lain where applicable/necessary' authorises the principle, not the content.

**Impact if unresolved.** 8 screens ship to MMD with unconfirmed visual directions. Also blocks the pinned-population fix for the component-main gate family (QA_PINNED_POPULATION_PLAN § COMPONENT_MAINS_*), because 13 pages measurably lose their base visual direction and whether that is a defect depends on this decision.

*Screens: Struktur Teduhan, Kemudahan Awam, Water Feature, Kerusi Taman, Papan Tanda, Tong Sampah, Drinking Fountain, BBQ Pit.*

## OD-02 — Exact B02 cast-name provenance — Alya / Encik Rahman

**Authority:** Bariah  
**Status:** `PENDING_BARIAH`

**Current safe treatment.** Both names remain in the deck with status CONFIRMED_LOCAL_ARTIFACT, not CONFIRMED_CANON. DIRECT_BARIAH_NAME_PROVENANCE = PENDING. Hilmi is artifact-backed in all four frozen sources and is not in question.

**Evidence that would close it.** Any frozen Bariah artifact naming Alya or Encik Rahman for B02. Neither appears in the annotated deck, the review guide, the S&G v0.3 or the exemplars, and the guide says 'nama watak khusus untuk B02 belum disahkan'.

**Impact if unresolved.** Character names would be voiced and animated in MMD without provenance.

*Recorded in CAST_PROVENANCE_REGISTER_v0.4.2.json. Self-corrected at Stage 4.2A.*

## OD-03 — Quiz rationale placement

**Authority:** Bariah  
**Status:** `PENDING_BARIAH`

**Current safe treatment.** Per-question rationales are carried in the off-canvas production panel and the Semak Jawapan production note, never on the learner canvas and never in the spoken VO. REVIEW_ONLY_ANSWER_KEYS_IN_SPOKEN_VO = 0.

**Evidence that would close it.** Whether learners see rationales, and if so on which screen and in what form.

**Impact if unresolved.** The quiz ships without learner-facing rationale; if Bariah expects one, the Kuiz screen architecture changes.

## OD-04 — Micro-control VO scope

**Authority:** Bariah  
**Status:** `PENDING_BARIAH`

**Current safe treatment.** VO/canvas parity is bounded to screen-level instructions beginning 'Klik pada setiap'. Micro-controls (Semak, Tutup, Kembali) are NOT spoken; MICRO_CONTROL_SCOPE_SELF_RESOLVED = 0. The CC-invented quiz-result instruction was withdrawn at Stage 4.2B.

**Evidence that would close it.** Whether 'every learner-facing interaction instruction must also be spoken' extends to popup-close and navigation micro-controls.

**Impact if unresolved.** Up to 7 further instructions would need spoken counterparts; the VO line count and the TTS export both change.

## OD-05 — Two S01 Speaker-Notes punctuation confirmations

**Authority:** Bariah  
**Status:** `PENDING_BARIAH`

**Current safe treatment.** Both lines rendered WITH the trailing full stop, carried from the unambiguous grey 'before' block. Recorded at MEDIUM punctuation confidence in BARIAH_RASTER_TRANSCRIPTION_REGISTER_v0.4.3.json as S1-c and S1-d.

**Evidence that would close it.** Confirmation only: 'Mohon sahkan penggunaan tanda noktah pada dua baris Speaker Notes S01.' The WORDING of all three lines is HIGH confidence and settled — she is not being asked to re-review the S01 text.

**Impact if unresolved.** Two characters in the VO transcript. No structural effect, but the TTS cut would carry an unconfirmed sentence terminator.

*Question ID Q-PUNCT-S01. Deliberately scoped to punctuation.*

## OD-06 — "Skrin: Tambahan Text" interpretation

**Authority:** Bariah  
**Status:** `PENDING_BARIAH_CONFIRMATION`

**Current safe treatment.** Retained as review/production metadata. No new learner screen created. LEARNER_SCREENS = 29 and REVIEW_PAGES = 100 unchanged.

**Evidence that would close it.** Whether the label means additional content on the SAME screen or a NEW learner screen. No direct evidence currently confirms the current reading.

**Impact if unresolved.** If the alternative reading is right, LEARNER_SCREENS becomes 30, REVIEW_PAGES at least 101, and the Struktur Taman group navigation and completion topology must be re-derived. Six structural totals move.

*Decision B02-D-TAMBAHAN-TEXT-01. Question: 'Label “Skrin: Tambahan Text” bermaksud tambahan kandungan pada skrin yang sama, atau perlu diwujudkan satu skrin learner baharu?'*

## OD-07 — Tamat physical navigation mechanism

**Authority:** Firdaus / LMS owner  
**Status:** `PENDING_FIRDAUS_LMS_OWNER`

**Current safe treatment.** The Tamat screen carries Bariah's exemplar wording 'Teruskan pembelajaran ke bahagian seterusnya.' The superseded 'Tutup tetingkap pelajaran untuk keluar.' is gated out, and TAMAT_UNVERIFIED_PHYSICAL_NAVIGATION_CLAIM asserts that no unverified mechanism is described.

**Evidence that would close it.** How the LMS shell actually advances the learner out of B02 — shell Next, window close, or automatic return to a menu.

**Impact if unresolved.** The final screen may describe a navigation action the shell does not perform. Not Bariah's to answer.

## OD-08 — MS2680 verification

**Authority:** Source authority — CAIR / module owner  
**Status:** `PENDING_SOURCE_AUTHORITY`

**Current safe treatment.** The MS2680 sentence is OMITTED from the S02 dialogue (U-01) and is NOT replaced by any other standards claim. Nothing in the deck asserts a standard.

**Evidence that would close it.** Whether MS2680 is the correct standard reference for this content, and the clause it supports.

**Impact if unresolved.** A standards citation stays out of the courseware. Safe, but a required reference may be missing.

## OD-09 — B02-CAIR-INT-001 — canonical module DOCX integrity

**Authority:** Firdaus / CAIR — explicitly not Bariah's to close  
**Status:** `PENDING_FIRDAUS_CAIR`

**Current safe treatment.** The 26-row source baseline is derived from the hashed PDF pages 256–269 and is frozen. SOURCE_ROW_COUNT may change only on a proven CLASS-9 correction re-derived from that PDF. SOURCE_INTEGRITY_FULLY_VERIFIED is not asserted.

**Evidence that would close it.** A verified canonical module DOCX, or confirmation that the hashed PDF is canonical for B02.

**Impact if unresolved.** Canonical freeze cannot be declared. Open since Stage 1.
