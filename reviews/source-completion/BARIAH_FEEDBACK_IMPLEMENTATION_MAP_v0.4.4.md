# BARIAH_FEEDBACK_IMPLEMENTATION_MAP — v0.4.4

```
BARIAH_OPEN_DECISIONS        = 0
FIRDAUS_LMS_OPEN_DECISIONS   = 0
COMMENTS_CLASSIFIED          = 8   (7 Bariah + 1 LMS owner)
PENDING_HUMAN_CLOSED_BY_CC   = 0
DECK_REGENERATED             = false
```

Classified against the schema in `B02_FEEDBACK_DELTA_PROTOCOL_v0_4.md` §2. Every record
names the frozen screenshot it came from; `DECISION_SUMMARY.md` is not used as a source.

---

# 1. The eight records

| # | Class | Anchor | Verbatim | Register action | Status |
|---|---|---|---|---|---|
| F-01 | `CLASS-1` + `CLASS-6` | RP-005 · `SCR_STRUKTUR_PERSISIR_AIR_MAIN` | *"Slide 5 (tambahan text pada skrin sama, to follow VO) - yg ni:"* + `Asas Pembinaan` and two bullets | resolve `B02-D-TAMBAHAN-TEXT-01` | `RESOLVED_BY_BARIAH` |
| F-02 | `CLASS-8` | all 9 component mains | *"Soalan 1: Component-main - Visual diperlukan"* | new `B02-BARIAH-20260801-COMPONENT-MAIN-VISUAL-02`; supersedes the qualified propagation record | `RESOLVED_BY_BARIAH` |
| F-03 | `CLASS-8` | all example / information popups | *"Pop up - visual diperlukan… di pop up, visual nya lebih besar dan fokus"* | amends the visual requirement table with a treatment field | `RESOLVED_BY_BARIAH` |
| F-04 | `CLASS-4` | 22 state pages of 9 component mains | *"Untuk all-viewed dan return state, kita kekalkan semula visual overview component-main yang sama - ya, betul"* | new `B02-BARIAH-20260801-VISUAL-STATE-PERSISTENCE-01` | `RESOLVED_BY_BARIAH` |
| F-05 | `CLASS-6` | cast register | *"Yes lulus. Boleh diguna pakai di Bahagian/Topik/PL lain jika bersesuaian"* | amends `CAST_PROVENANCE_REGISTER` | `RESOLVED_BY_BARIAH` |
| F-06 | `CLASS-1` + `CLASS-2` | `SCR_KUIZ` | *"Rationale jawapan, hanya maklum balas… Speaker Notes tidak perlu."* | new `B02-BARIAH-20260801-QUIZ-RATIONALE-01` | `RESOLVED_BY_BARIAH` |
| F-07 | `CLASS-2` | all interaction instructions | *"Tidak. VO cuma arahan screen level \"Klik pada setiap …\"* | new `B02-BARIAH-20260801-MICRO-CONTROL-VO-01`; ratifies the Stage 4.2B bounded scope | `RESOLVED_BY_BARIAH` |
| F-08 | `CLASS-1` | RP-001 · `SCR_S01` | *"Buang noktah - yang ni kan -"* | new `B02-BARIAH-20260801-S01-PUNCTUATION-01`; supersedes raster records S1-c and S1-d | `RESOLVED_BY_BARIAH` |
| F-09 | — | `SCR_TAMAT` | LMS-owner ruling, **not Bariah's** | `B02-U-03` | `RESOLVED_BY_LMS_OWNER` |

## 1.1 The `CLASS-3` / `CLASS-9` test

**No record is `CLASS-3` and none is `CLASS-9`.** Nothing here changes how many interaction
items a source row yields, and nothing changes what the source says. F-01 adds display copy
that the module's own VO already asserts; it is not a source correction and does not touch
the 26-row baseline.

`SOURCE_ROW_COUNT = 26` · `INTERACTION_ITEMS = 54` · `LEARNER_SCREENS = 29` — all unchanged.

---

# 2. Propagation scope, measured

| # | Screens touched | Review pages | Artifacts to regenerate |
|---|---:|---:|---|
| F-01 | 1 | **1** (RP-005) | controlled content → generator → deck |
| F-02 | 9 | **22** (every state of every component main) | visual policy → generator → deck |
| F-03 | 12 | **38** example and information popups | visual policy → generator → deck |
| F-04 | 5 | **13** state pages that currently lose the visual | generator (state → screen derivation) → deck |
| F-05 | 0 | **0** | registers only; names already render |
| F-06 | 1 | **5** quiz question pages | controlled content → generator → deck, Notes |
| F-07 | 0 | **0** | conformance gate only; no copy changes |
| F-08 | 1 | **1** (RP-001 Notes) | model → Notes writer → deck |
| F-09 | 1 | **1** (RP-100 panel only) | generator metadata → deck |

The 13 pages in F-04 are enumerated in `B02_PINNED_POPULATION_TARGETS_v0.4.4.json`, selected
by `learner_screen_id` plus every bound runtime state — **not** by review-page classification,
which is the selector that produced the blindness in the first place.

---

# 3. Where each ruling stops

Recording what a ruling does **not** authorise matters as much as what it does.

- **F-02 confirms the requirement and the treatment, not the subjects.** Bariah said a
  component-main visual is required and should be several smaller visuals as an overview. She
  did not name a subject for any of the eight. The module's own source-attested visual text is
  therefore ratified as the overview subject and **no subject is invented**.
- **F-03 is a treatment ruling.** Example and information popups were already `REQUIRED`; what
  is new is `LARGE_FOCUSED`. Specification popups are untouched and stay `NOT_REQUIRED`.
- **F-05 permits reuse, it does not perform it.** *"jika bersesuaian"* is a judgement retained
  by the reviewer. Alya and Encik Rahman are not propagated anywhere automatically.
- **F-07 excludes micro-controls from the spoken VO only.** Production metadata describing
  control behaviour is kept.
- **F-08 covers lines 1 and 2.** Line 3 was not mentioned; its full stop was `HIGH` confidence
  in the earlier transcription and is retained.
- **F-09 is not a Bariah ruling** and is filed under Firdaus / LMS owner. The two unproven
  routes — automatic next and LMS shell Next — are recorded as unproven, and the learner-facing
  copy is unchanged.

---

# 4. Implementation standing

All nine are **frozen as decisions and unimplemented in the artifact**. Seven carry
`IMPLEMENTATION_REQUIRED_V0_4_4`, one is `REGISTER_UPDATE_ONLY`, one is `METADATA_ONLY_V0_4_4`.
The change list is `B02_V0_4_4_IMPLEMENTATION_DELTA.md`; the v0.4.3 deck is byte-identical and
was not regenerated.
