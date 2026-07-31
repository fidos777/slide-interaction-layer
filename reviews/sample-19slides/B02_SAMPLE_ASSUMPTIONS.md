# B02_SAMPLE_ASSUMPTIONS

- **Status:** gate document — **docs-only**. Nothing implemented.
- **Scope:** one K5 PL06 T3 B02 19-slide visual sample
- **Standing:** **sample only — NOT CAIR-ratified.** `K5_LIVE_RATIFICATION_LOCKED`
- **Authority key:** `(K5, PL06, T3)`. B02 is a bahagian below the key and gets no key row.

> **CORRECTED — preflight round.** Two assumptions were wrong and are superseded below:
> **`A-13` cast** (was: "cast limited to `Haziq` + `Encik Roslan`") and **`A-09` S03 narrator**
> (was: framed as an unresolved contradiction). Correction log at §5.

---

## 0. What this sample is, and is not

| It is | It is not |
|---|---|
| One visual sample of B02 at 19 screens | A storyboard |
| A rendering of assumptions, so they can be *seen* and judged | A ratified treatment |
| A vehicle for the CAIR family judgement that has never been made | A baseline, candidate, manifest or freeze |
| Docs-gated, per this file | Authorised to write to `cair_decisions` or the MMD register |

`LOCAL_REVIEW_CHECKLIST.md` records that **no revision of either deck has ever been seen rendered** —
LibreOffice cannot load them in the build sandbox. The open question it names is still open:

> *Does it read as one coherent interaction family? Or does the child feel like a different deck?*

**That judgement is the sample's purpose.** The sample exists to make it answerable, not to pre-empt it.

---

## 1. Assumption register

Each assumption carries its evidence, its status, and the risk taken by assuming it.
`A-##` handles are **local to this document** — not decision IDs, not a namespace.

### `A-01` — Sample only, not CAIR-ratified
- **status** CONSTRAINT — not an assumption
- **evidence** `SBAT-ADR-004` §3; `OPEN_COURSES = ["K4"]`; Stage 0A status addendum §2
- **risk if violated** A sample mistaken for a ratified treatment would enter MMD handoff unratified —
  the exact harm `INTERACTION_ID_RECONCILIATION.md` §0 exists to prevent.
- **mitigation** Every sample artefact carries the `NOT CAIR-RATIFIED` banner. No `K5-DR-###` or `P#`
  is written into it.

### `A-02` — One B02 19-slide visual sample
- **status** SCOPE
- **evidence** 19-screen vector recovered from probe v0.1 `docProps/app.xml`
  (`S01 TAJUK` … `S19 TAMAT`, `<Slides>19</Slides>`)
- **risk** 15 of 19 screens have **no measured source** (`INPUT_CUSTODY.md` §3). Their content will be
  constructed, not transcribed.
- **mitigation** `SCREEN_CHANGE_MATRIX.md` marks every screen `MEASURED` or `CONSTRUCTED`. No
  constructed screen may be cited as evidence of source.

### `A-03` — S04 / S09 use the 4-card family
- **status** ASSUMPTION — **well grounded**
- **evidence** S04 binds 4 children (S05–S08); reviewed `slide3` is Bariah's worked 2 × 2 Card grid,
  `slide5` its completion state (probe S09's 7 vertical-menu shapes `sp41–47` deleted, 9 card-grid
  shapes added). Card geometry measured: 3.935 × 1.9901, gap 0.7074 / 0.3701, label ratio 0.770597.
- **risk** `K5-DR-041`'s supersession is **not in force**; the inherited Hotspot treatment
  (`K5-DR-042`) is still the active instruction, and Bariah **retained** it on the very slide where she
  proposed Card. The sample takes the proposal over the retained text.
- **mitigation** Recorded as the sample's most consequential unratified choice. The Card selection is
  bounded to B02 (Stage 0A addendum §7.2) and asserts nothing about Hotspot generally.

### `A-04` — S10 / S16 use the 5-card 3+2 family
- **status** ASSUMPTION — **arithmetically forced, option unratified**
- **evidence** S10 binds **5** children (S11–S15). Measured arithmetic: 2 × 3 at reviewed card size
  needs 8.0581 in vertically and **exceeds the entire 7.5 in stage by 0.5581 in** — impossible. 3+2
  fits vertically unchanged.
- **risk** **A fifth card cannot be free.** No 3+2 arrangement preserves the reviewed card width inside
  the deck's 11.75 in content band (would require a **−0.0275 in** gap). One of three costs must be
  accepted: card width −8.51 % (5B, gap 0.7074→0.4750), card width −12.45 % (5A, gap preserved), or the
  content band abandoned (5C, margins collapse to 0.0568 in).
- **selection for the sample** **Option 5B** — `CARD_W = 3.60`, `GAP_X = 0.4750`, margins held at
  0.7917. Rationale: smallest card-size loss (8.51 %) while respecting the deck's own content band.
  5 parameter deviations vs 5A's 4 — one more deviation bought 4 points of card width.
- **mitigation** The choice is the sample's, not CAIR's. `K5-DR-061` stays `OPEN`. **Conditional:**
  if S10 resolves to Hotspot under `K5-DR-040`, this assumption is void and the screen is rebuilt.

### `A-05` — Detail screens use split-STATE
- **status** ASSUMPTION — ⚠️ **departs from the reviewed deck**
- **scope** S05–S08 and S11–S15 — **9 screens**
- **evidence** Canonical STATE measured via probe S12 (canon slide 6): visual panel
  0.8046, 1.7813 **5.8621** × 5.2604 (43.97 % of stage), body right column 6.8667, 2.5594
  5.6621 × 3.8708, **dedicated heading box** 5.6621 × 0.5068, `Kembali` below. Canonical RUMUSAN panel
  is **11.7292** — the two archetypes differ by **2.0009×**.
- **⚠️ conflict, stated plainly** Bariah's reviewed `slide4` **widened** S12's panel to 11.7371 — within
  **0.0079 in (1.1 px at 1920)** of the Rumusan panel — and **deleted** the heading box
  (`sp10 del @22:52:53`). **The sample reverts that edit on all 9 detail screens.** S12 in the sample
  will not look like S12 in her review deck.
- **basis for reverting** `K5-DR-060`, a CAIR recommendation: at 0.0079 in the reveal-child becomes
  geometrically indistinguishable from Rumusan, leaving a 14 pt `Kembali` at 0.45 % of stage area as
  the only discriminator — and it sits *outside* the content region.
- **cost, measured** Body line box falls 11.1246 → 5.1496 in (**−53.7 %**); capacity 89–97 → 41–45
  chars/line; the measured 285-char S12 body reflows from 8 lines to ~13.
- **mitigation** This is the assumption most likely to be rejected on sight, and it is the one the
  sample most needs rendered to settle. Flagged at the top of `SAMPLE_IMPLEMENTATION_PLAN.md` §5.

### `A-06` — Reveal mode `FULL_SLIDE`
- **status** ASSUMPTION — **carried by pre-existing provenance**
- **evidence** Probe v0.1 S04 note ¶4, verbatim: `Klik hotspot -> reveal full-slide, bukan pop up.`
  An explicit variant selection **in the negative**, recorded before the review (`K5-DR-042`,
  inherited). Maps to `interaction-patterns-v0.md` §3.2 variant **`detail-screen-kembali`** — which has
  precedent (sample cementitious 16/06), not deferred status.
- **risk** Low. The POP UP anti-drift guardrail requires an explicit variant choice with provenance;
  both are present and neither is the sample's invention.
- **note** Only the **trigger** axis is contested between `K5-DR-041` and `K5-DR-042`. The **reveal
  mode is contested by no one.** That is what unblocks the sample.

### `A-07` — Concise source-bound display
### `A-08` — Fuller source-bound VO
- **status** ASSUMPTION — **strongest evidential support in the set**
- **evidence** Issued S12 baseline: probe display = 4 ¶, 346 ch, 50 words, 4 sentences — **byte-identical
  to its own VO body** in `notesSlide16`. Display **was** VO. Bariah's revision: display 285 ch / 8 ¶ /
  0 sentences, VO body **unchanged verbatim**; 4/4 propositions retained; 7 removed token types all
  function words, copula, modal, relativiser or the de-duplicated subject; **zero tokens added**.
  Rumusan control pair: display **−7.5 %** while VO **+7.2 %** — truncation cannot produce a VO that
  grows.
- **risk** Coverage is **2 screens of 19**. `LOSSLESS_RESEGMENTATION_GATE_SUPERSEDED` is established on
  S12 and S17 only and must not be generalised to the packet without measurement.
- **budget** `MAX_DISPLAY_LINES = 8` hard at 18 pt full-width; **7 as the design target.** The measured
  S12 revision sits at **8/8 line slots with zero headroom** — a 9th bullet overflows the panel and
  collides with `Kembali`. Under `A-05` the line box narrows 53.7 %, so the sample's split-STATE
  detail screens need a **tighter** display budget than the measured full-width one, not a looser one.

### `A-09` — No routine `Hilmi` prefix — **CORRECTED**
- **status** ASSUMPTION — **resolved, not a contradiction**
- **evidence** `K5-DR-010`. Probe carries `Hilmi:` on all 3 non-empty notes (S04, S12, S17); Bariah
  removed it on both screens she revised. Premise ratified: `BARIAH_DATA.chars` locks
  `Hilmi — Course narrator (VO-only) — LOCKED (memory)`.
- **interpretation adopted**
  1. **S03 may visually introduce Hilmi as the narrator.** Identifying the narrator once, on the
     screen that introduces him, is a normal courseware move and is what
     `(Only put Hilmi in Slide 3 Narrator)` most naturally means.
  2. **Routine narrator VO does not carry the literal `Hilmi:` prefix.**
  3. **Hilmi is not repeated on ordinary learning screens** unless functionally required — e.g. a
     screen where the narrator must be distinguished from a scenario speaker.
- **why this is not a contradiction** Bariah's text says *put Hilmi in Slide 3 Narrator* — it speaks to
  **where the narrator is identified**, not to a VO **prefix string**. Nothing in either package shows
  her requiring a literal `Hilmi:` prefix on S03; the only measured `Hilmi:` occurrences are the probe's
  routine VO openings on S04/S12/S17, which is exactly the usage her rule removes. The earlier framing
  of this as an unresolved referent collision over-read the evidence.
- **residual, and it is small** *Which* screen "Slide 3" denotes is still not measured
  (`packet_B02.json` absent). Under this interpretation it does not block: **S03 OVERVIEW** is the only
  candidate that makes the instruction meaningful, and the preflight does not build S03.
- **preflight effect** No `Hilmi:` prefix on S04, S12 or S17 — all three are routine learning screens.
  **Verified: zero `Hilmi` tokens in any VO.**

### `A-10` — English-origin terms italic
- **status** ASSUMPTION — **new practice, no source precedent**
- **evidence** `K5-DR-020`. Applied at exactly one locus in the reviewed deck (`slide8`:
  `Water Feature`, `Drinking Fountain`, `BBQ Pit`). **Probe v0.1 has zero italic runs on any
  English-origin term** — 9 occurrences, 9 non-italic.
- **risk** The lexicon seed is **3 terms** from one 8-slide deck. The loan-word boundary is the hard
  problem: `informasi`, `landskap`, `struktur`, `navigasi` are all English-derived and all **out** of
  scope; `Water Feature` is in. No algorithm separates them — only a maintained list.
- **sample term list** exactly three: `Water Feature`, `Drinking Fountain`, `BBQ pit`. **No term is
  added by inference.** Any further candidate encountered in a constructed screen is left non-italic
  and logged.

### `A-11` — Revised Rumusan treatment
- **status** ASSUMPTION — three separable rules, differing confidence
- **scope** S17 only
- **components**
  | Rule | Confidence | Note |
  |---|---|---|
  | `K5-DR-030` suppress `Kepentingan` / `Isi Utama` / `Manfaat` labels | **gate-grade** — 4/4 present in base, 0/4 in revision | match case-insensitively (`Isi Utama` vs source `Isi utama`) and `Manfaat` as prefix |
  | `K5-DR-031` `kontraktor` not `anda` | deterministic string test; **scope unreconciled** | probe: `anda` ×2 both on S17, `kontraktor` ×0 anywhere |
  | `K5-DR-032` benefit → industry application | **`JUDGMENT_RULE_NOT_DETERMINISTIC`** | `di tapak` appears in *both* compliant and non-compliant text — keyword tests false-pass |
- **risk** `K5-DR-032` cannot be verified mechanically in the sample. It will be drafted by judgement
  and flagged for human review, not asserted as compliant.

### `A-12` — Papan Tanda source locator `IMG-05`, page 243
- **status** **CORRECTION** — reverts a measured regression
- **evidence** Probe v0.1 S12 cites `K5PL06T03-B02-IMG-05, ms 243` correctly in **both** its visual
  panel and its note panel. Bariah's reviewed `slide4` added an off-canvas box (`Rectangle 3` id 4,
  `sp4 add mod @23:06:09`) cloned from the **Struktur Taman** slides, carrying `IMG-01, ms 237` — the
  wrong image for `Papan Tanda`. The correct citation survives only in her note panel ¶5.
- **risk** None on the evidence; this is the best-supported item in the register. Cause is determinate.
- **note** Tracked as a **source QA defect**, not a decision — `SOURCE_QA_PATCH_LIST.md` P-01.

### `A-13` — Scenario cast — **CORRECTED · role-neutral placeholders**
- **status** ASSUMPTION — **current B02 cast NOT PROVABLE**
- **scope** S02 DIALOG and any scenario screen. **Not exercised by the preflight** — S04, S12 and S17
  carry no scenario characters.
- **prior position (withdrawn)** "Cast limited to the ratified `CANONICAL` pair: `Haziq`,
  `Encik Roslan`." That treated a character-bank entry as the current course-wide cast. It is withdrawn.
- **what the evidence actually shows**
  | Finding | Detail |
  |---|---|
  | `Haziq` / `Encik Roslan` marked `CANONICAL` | `BARIAH_DATA.chars` — **undated, no scope statement**. It does not say "K5 course-wide, current". |
  | The bank was a **menu, not a closed cast** | The K5 PL06 casting prompt reads `Tentukan jalan cerita + watak (Haziq/Roslan/**baru**)` — *baru* = **new**. A new character was always permitted. |
  | The bank **does** record supersession when it happens | `Encik Fahmi` → `OFF-CANON → being replaced by Aril`. No such marker exists against Haziq/Roslan — which means the bank is **stale** relative to the reported latest position, not that the position is wrong. |
  | B02's own decks contain **no scenario characters at all** | Only `Hilmi` (narrator) appears in either package. Zero occurrences of Haziq, Roslan, Alya or Rahman. |
  | `Alya` / `Encik Rahman` | **Zero occurrences** anywhere in the repository or either deck. |
  | Cast Bible | **Zero occurrences.** No such artefact is present. |
  | The screen that would settle it | **S02 is unmeasured**, and its decision slot `(K5, PL06, s02)` is **empty**. |
- **conclusion** The available evidence can neither confirm the reported B02 local cast
  (`Alya` + `Encik Rahman`) nor revive `Haziq` + `Encik Roslan`. The fixed-pair treatment is reported
  superseded; the course-wide **Cast Bible remains OPEN**; **`Hilmi` remains the narrator** (ratified,
  `LOCKED`, and independent of the scenario cast).
- **sample decision** Use **role-neutral placeholders** — `[PELATIH]`, `[PENYELIA]`, `[KONTRAKTOR]` —
  on any scenario screen. **Do not revive a superseded cast, and do not assert an unproven one.**
- **risk** Placeholders make S02 visibly incomplete. That is correct: the casting decision was never
  made, and the sample must not manufacture one.

---

## 2. Assumptions the sample does **not** make

Recorded because their absence is load-bearing.

| Not assumed | Why it matters |
|---|---|
| That Card beats Hotspot generally | `A-03` is bounded to B02. Hotspot capability is retained and untouched (Stage 0A addendum §7.1). |
| That `POPUP` is available | Both realisations (`overlay-with-close`, `overlay-maintain-VO`) are **DEFERRED**. The sample never selects `POPUP`. |
| That `inline` reveal is unavailable | The repo carries it as `sedia`. The two-value enum omits it; the sample does not delete it (`K5-DR-072`). |
| That `anda` is prohibited outside Rumusan | Explicitly not assumed. `K5-DR-031` is Rumusan-scoped until the packet says otherwise. |
| That a literal `Hilmi:` prefix is required on S03 | `A-09` — no evidence supports it; the rule speaks to where the narrator is *identified*. |
| That `Haziq` + `Encik Roslan` are the current B02 cast | `A-13` — the fixed-pair treatment is reported superseded and the bank is undated. |
| That `Alya` + `Encik Rahman` are the current B02 cast | `A-13` — reported, but **zero corroborating evidence** is available. |
| That drag-drop appears anywhere in B02 | No B02 screen binds paired sets. `S18 KUIZ` is a quiz, not a matching activity. |
| That constructed screens carry source authority | 15 of 19 are constructed. None may be cited as source. |
| That B02 earns a key row | It is a bahagian; the key is `(K5, PL06, T3)`. |

---

## 3. Assumption risk summary

| Risk | Assumptions | Nature |
|---|---|---|
| **High** | `A-05` | Reverts Bariah's own edit on 9 screens; most likely to be rejected on sight |
| **High** | `A-02` | 79 % of screens constructed without measured source |
| Medium | `A-03`, `A-04` | Unratified selections; `A-04` conditional on S10's Card/Hotspot resolution |
| Medium | `A-13` | Cast unprovable → placeholders; S02 renders visibly incomplete |
| Medium | `A-10` | A 3-term lexicon seed from one 8-slide deck |
| Low | `A-09` | Resolved by interpretation; not exercised beyond "no prefix" |
| Medium | `A-11` (`K5-DR-032` only) | Not mechanically verifiable |
| Low | `A-06`, `A-07`, `A-08`, `A-12` | Carried by measured evidence or pre-existing provenance |

**Two high risks, both structural, both known before implementation.** Neither is a reason to stop —
they are the reasons the sample exists — but neither may be discovered by a reviewer for the first time
in the rendered output.

---

## 5. Correction log — preflight round

| # | Assumption | Was | Now | Basis |
|---:|---|---|---|---|
| C-1 | `A-13` cast | "cast limited to `Haziq` + `Encik Roslan`" (derived from `K5-DR-004`) | **role-neutral placeholders**; current B02 cast **NOT PROVABLE** | The bank is undated and scope-less; the casting prompt explicitly allowed `baru`; zero evidence for any named cast in B02's own material |
| C-2 | `A-09` S03 narrator | framed as an unresolved referent collision / "guessed exemption is worse than none" | **resolved by interpretation**; S03 may visually introduce the narrator, routine VO carries no prefix | No evidence Bariah required a literal `Hilmi:` prefix on S03; her rule addresses narrator *identification*, not a prefix string |

**Knock-on corrections applied to sibling documents** (same round, for consistency):
`SCREEN_CHANGE_MATRIX.md` S02/S03 rows and `SAMPLE_IMPLEMENTATION_PLAN.md` constraint 11, Phase 5 and
risk R3. `K5-DR-011` in `K5_DECISION_REGISTER_v1.1.md` should be **downgraded from `COLLIDED` to
`OPEN — interpretation adopted`**; that register is provisional and non-canonical, so no reissue is
required.

---

## 4. Modification statement

Docs-only. Nothing implemented. No PPTX modified, no compiler patched, no schema altered, no visual
candidate created, no canonical ID issued. K5 remains locked; the live CAIR decision desk is untouched.
