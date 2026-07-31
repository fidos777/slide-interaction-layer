# STORYBOARD_QA_REPORT — K5 PL06 T03 B02

```
STORYBOARD_REVIEW_DRAFT · SOURCE_BOUND_TEXT · VISUALS_NOT_EMBEDDED
MULTIMEDIA_NOT_PRODUCED · PENDING_BARIAH_APPROVAL · NOT_FOR_MMD_BUILD
```

| | |
|---|---|
| Artifact | `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_1.pptx` |
| `sha256` | `749b6c90f468bc0a1986b853319e62b1a1cec83600a98cbade628214d5bf8e7a` |
| Size | 109,954 B · 19 slides · 19 notes pages |
| Checks | **72 executed · 72 PASS · 0 FAIL** |

**A mechanical pass is not a rendered pass.** LibreOffice cannot load these decks in the build sandbox,
so **nothing in this artifact has been seen rendered** — only measured. Everything below is measurement.
`BARIAH_REVIEW_CHECKLIST.md` covers what has to be looked at on a machine with PowerPoint.

---

## 1. The instruction, item by item

| Required | Verified by | Result |
|---|---|---|
| 19 screens exactly | check 01–03 | ✅ 19 slides, 19 notes parts |
| Screen ID **and function** on every screen | check 13 | ✅ 19 / 19, on canvas, top strip |
| Learner-facing display text | checks 22–23, 56 | ✅ 19 / 19, within budget |
| **Complete VO** | checks 14–15 | ✅ 19 / 19; S09 and S16 empty by stated convention |
| Interaction instruction | check 12 | ✅ 19 / 19 |
| State / transition behaviour | check 12 | ✅ 19 / 19 |
| Visual direction **as a text placeholder** | checks 12, 17 | ✅ 19 / 19 carry a `[Visual: …]` specification |
| Module source page | check 16 | ✅ 19 / 19 (4 correctly record *no* module page) |
| MMD implementation notes | check 12 | ✅ 19 / 19 |
| Decision status | checks 11–12 | ✅ 19 / 19 |
| **No source photographs** | checks 04, 06, 07, 09 | ✅ `ppt/media` empty; 0 `a:blip`; 0 `p:pic`; 0 image rels |
| **No cropped PDF images** | checks 04, 05 | ✅ no image extension declared anywhere in the package |
| **No audio, video** | checks 05, 07 | ✅ no audio/video content type, no media relationship |
| **No animation** | check 08 | ✅ 0 `p:timing` blocks |
| **No final multimedia assets** | checks 04–09 | ✅ nothing bound; 14 registered assets remain unbound |
| S07 / S08 diagram **described only, not drawn** | checks 18–21 | ✅ described in the visual instruction; **shape count identical to S05** — nothing extra was drawn |
| S02 / S03 / S18 / S19 proposed, not blank | checks 22–23 | ✅ each ≥ 845 chars on canvas, each token-marked |
| S02 role-neutral, bounded dialogue | checks 24–26 | ✅ 5 turns, `[PELATIH]` / `[PENYELIA TAPAK]`, no named cast anywhere |
| S03 narrator visual, no `Hilmi:` prefix | checks 27, 28, 28b | ✅ Hilmi on canvas on S03 only; 0 prefix occurrences in any VO body |
| S18 — 4 MCQ + 1 Multiple Response | checks 30–32 | ✅ exactly 4 + 1 |
| S18 — correct answer + immediate feedback | checks 33–35 | ✅ 5 answer keys, 5 correct-branches, 5 incorrect-branches, 5 source citations |
| S19 routing stated as assumption, not CAIR-ratified | checks 36–38 | ✅ `ANDAIAN LALUAN` present; ratification explicitly denied; 0 `K5-DR-###` anywhere |
| Preserve 19 screens, card families, full-slide states, Kembali, Rumusan, off-canvas metadata | checks 39–55 | ✅ see §2 |
| **Accepted visual sample unmodified** | check 61 | ✅ re-hashed after the build: `8d93e2ce…646a982b` |

---

## 2. Geometry preserved from the accepted sample

The accepted sample v0.2 is the **structural donor**. Every geometric constant was re-measured out of
the new package, not assumed.

| Element | Accepted value | Measured in storyboard |
|---|---|---|
| 4-card `CARD_W` × `CARD_H` | 3.935 × 1.9901 | 3.935 × 1.9901 ✅ ×4 |
| 4-card `GAP_X` | 0.7074 | 0.7074 ✅ (x = 2.3779, 7.0203) |
| 5-card `CARD_W` (OPTION_5B) | 3.60 | 3.60 ✅ ×5 |
| 5-card `GAP_X`, 3 + 2 | 0.4750 | 0.4750 ✅ within each row |
| 5-card row 1 span | 0.7917 → 12.5417 | exact ✅ |
| 5-card row 2 centring | 6.66665 | exact ✅ |
| split-STATE panel | 5.8621 × 5.1387 | ✅ on all 9 detail screens |
| Navigation strip | 0.58 in reserved | ✅ |
| `Kembali` clearance | 0.10 above / 0.10 below | ✅ exact on all 9 |
| `Kembali` centring | 6.66665 | ✅ on all 9 |
| `Kembali` count | exactly one per detail screen, zero elsewhere | ✅ 9 / 9 and 10 / 10 |
| Ticks | 4 on S09, 5 on S16, native geometry | ✅ |
| S17 Rumusan | heading + 4 bullets, `spcBef` 600 | ✅ |
| Off-canvas production metadata | present, off-canvas | ✅ 19 / 19, entirely off-canvas |

---

## 3. SME rules re-verified on this artifact

| Rule | Grade | Result |
|---|---|---|
| No `Hilmi:` prefix in any VO | gate | ✅ 0 occurrences across 19 VO bodies and all canvas text |
| No named scenario cast | gate | ✅ no `Haziq`, `Roslan`, `Alya`, `Rahman` anywhere |
| S17 — no `Kepentingan` / `Isi Utama` / `Manfaat` | gate | ✅ case-insensitive, none |
| S17 — no `anda`, addressee is `kontraktor` | gate | ✅ |
| S17 — em dash, lowercase `dan` | deterministic | ✅ |
| Lexicon terms italic in display | deterministic | ✅ — see §4, `F-01` |
| `BBQ pit` lowercase `p` | deterministic | ✅ |
| Display within budget | deterministic | ✅ all 9 detail screens under the 12.5-line ceiling |
| No canonical `K5-DR-###` written | gate | ✅ 0 |
| Nothing from another course | gate | ✅ — see §4, `F-02` |
| `K5-DR-032` industry application | **not mechanically checkable** | ⚠️ human review — `D-05` |

---

## 4. Findings raised and resolved during the build

Five real defects were found and fixed, plus two validator defects. All are recorded, including the ones
that were my own error.

### `F-01` — Title bar left the lexicon italic off · **fixed, and it is a deviation**

The rule is that the three lexicon terms carry italic *wherever they appear in display*. The accepted
sample v0.2 applies it to card labels and body text but leaves the **40 pt title bar roman** on S08,
S14 and S15 — the three screens whose title *is* a lexicon term.

The storyboard **applies the italic to the title bar**, on the reading that a title bar is display text.
That is a deliberate deviation from the accepted sample and it is raised as **`D-12`** rather than
absorbed silently. Verified: all three title bars now carry `i="1"`.

**If Bariah prefers the accepted sample's treatment, revert it and restate the rule as "body text and
labels" so it stops reading as a violation.**

### `F-02` — Quiz item labels `K1`–`K5` collided with the course codes `K4` / `K5` · **fixed**

The first draft numbered the quiz items `K1`–`K5`. `K4` and `K5` are course codes in this project's
namespace, and the course-isolation check fired on `K4` — correctly, from its point of view. A reviewer
scanning the deck would hit the same ambiguity. Items renamed `Soalan 1`–`Soalan 5`. No collision remains.

### `F-03` — S18 carried no VO · **fixed**

The instruction requires a complete VO on **every** screen. S18's notes page was built by hand and had
an item bank but no VO section. A quiz-introduction VO was added, plus an explicit note that item text is
read on screen rather than voiced separately.

### `F-04` — Off-canvas production panel overflowed on 14 of 19 screens · **fixed**

At the donor's 3.1496 in width the panel could not hold the eight storyboard fields. Widened to 4.75 in
and it still overflowed on 14 screens — worst case 63 lines against a 44-line capacity. Resized to
**6.60 × 7.5 in at 9 pt**: capacity 49 lines, worst case 44. Verified per screen, all 19 fit.
The panel remains entirely off-canvas — verified, right edge at exactly x = 0.

### `F-05` — Validator defect: the `Hilmi:` check was shape-blind · **check fixed, artifact was correct**

The check searched all text for `Hilmi\s*:` and fired three times. All three hits were **my own
production notes quoting the forbidden string** in sentences like *"Tiada awalan 'Hilmi:' dalam mana-mana
VO."* The artifact was never wrong; the check was.

Rescoped to what the rule actually governs — line-initial position, in VO bodies and learner-facing
canvas text only — plus a second check (`28b`) confirming Hilmi appears on canvas on S03 alone. This is
the same class of defect as the earlier shape-blind `BBQ pit` check, and it is recorded rather than
quietly corrected.

### `F-06` — Validator defect: the 5-card gap check mixed both rows · **check fixed, geometry was correct**

The check sorted all five card x-positions together and compared adjacent values. In a 3 + 2 grid the
rows interleave when merged, so the comparison was meaningless. Rewritten to measure pitch **within each
row**, plus row-1 band span and row-2 centring. Geometry was correct throughout and matches the accepted
sample exactly.

### `F-07` — Three dangling notes back-relationships in an earlier build stage · **fixed**

Inherited from the donor package. Notes-slide relationships were rewritten so every `notesSlide{n}`
points at `slide{n}`. Verified for all 19.

---

## 5. What was **not** done — by instruction

| Not done | Verified |
|---|---|
| Source photographs embedded | ✅ `ppt/media` empty |
| Cropped PDF images embedded | ✅ no image content type declared |
| Audio, video, animation | ✅ no media relationship, 0 `p:timing` |
| Final multimedia assets selected or bound | ✅ 14 registered assets remain `EXTRACTED — not yet bound` |
| S07 / S08 diagram drawn | ✅ shape count equals S05 exactly |
| Accepted visual sample modified | ✅ hash unchanged after the build |
| MMD asset binding started | ✅ nothing bound |
| Canonical decision ID issued | ✅ 0 `K5-DR-###` |
| Compiler patched, schema altered, baseline / manifest / freeze created | ✅ none — docs and one new PPTX only |
| K5 unlocked, live CAIR desk touched | ✅ neither |

---

## 6. What this artifact cannot tell you

1. **How it renders.** Nothing has been seen. Every value here is measured out of XML. Font substitution,
   autofit recomputation on open, and actual line wrapping are all unverified.
2. **Whether `spAutoFit` holds.** PowerPoint recomputes autofit on open. The 12.5-line budget is a
   calculation, not an observation. The screens closest to the ceiling are S05, S08 and S12.
3. **Whether the industry-application clause on S17 lands.** Lexical proxies false-pass — `di tapak`
   appears in both compliant and non-compliant phrasing. `D-05` is human-only.
4. **Whether the CAIR family question resolves.** Open since 16/06. It needs a rendered S04 beside a
   rendered S05, and that still has not happened.
5. **Whether the quiz items are pedagogically right.** Their factual traceability to module pages was
   checked. Their difficulty, discrimination and fairness were not — that is `D-08`.

---

## 7. Standing

This artifact is a **review draft**. It is not a baseline, a candidate, a manifest, a freeze or an
executable contract. It carries no canonical ID and grants no production authority. K5 remains locked,
so no ratification path exists for it — it can be reviewed, not ratified.

**Nothing proceeds to MMD until `BARIAH_REVIEW_DECISION_LIST.md` has positions recorded against it.**
