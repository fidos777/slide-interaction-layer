# B02_INTERACTION_FAMILY_TAXONOMY — K5 PL06 T03 B02, Stage 2

```
STAGE_2_TAXONOMY_READY_FOR_IMPLEMENTATION
RECONCILED_AGAINST_BARIAH_EXECUTION_FAMILIES (1 August 2026)
EXECUTION_FAMILIES = 3 · UNKNOWN_COMPONENT_FAMILY = 0
NO_NEW_PRODUCTION_P_ID_MINTED
PENDING_CAIR_PATTERN_RATIFICATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

**Sections 1–5 are the technical taxonomy** — a classification of the *mechanics* each screen uses,
expressed in the repository's existing pattern vocabulary, derived from the frozen v0.3 model.
**Section 6 is the reconciliation** against Bariah's three approved execution families, which are the
authority on *what gets built*. Where the two views could conflict, §6 governs: the technical
taxonomy describes mechanism, the execution families decide architecture.

Sections 1–5 were written before the feedback landed and are preserved unedited, so the delta between
the two views stays visible.

**Governing constraint, carried from `taxonomy/INTERACTION_ID_RECONCILIATION.md`:**

> Only `P0`, `P6` and `P11` are live production IDs. Everything else is draft or candidate.
> **No candidate ID becomes a production `P#` until reconciled and ratified.**

Nothing here mints a new `P#`. Where B02 diverges from a documented pattern, the divergence is named
as a **variant of an existing pattern**, not as a new number.

---

# 1. The six interaction families in B02

| # | Family | Screens / states | Nearest repo pattern | Pattern status | Divergence |
|---|---|---:|---|---|---|
| **F1** | Level 1 group master — component cards | 2 screens, 4 review pages | `P1` Reveal Cards | **draft** | cards **navigate away** instead of revealing in place |
| **F2** | Main explanation screen | 9 screens, 9 review pages | `P0` Static | **LIVE** | adds a VO completion gate |
| **F3** | Level 2 example screen — item cards | 9 screens, 44 review pages | `P1` Reveal Cards | **draft** | reveal surface is a modal, not in-place |
| **F4** | Popup content state | 26 states, 26 review pages | `P4` Modal (Deep Dive) | **draft** | **many and required**, not one and optional |
| **F5** | Kuiz | 1 screen, 1 review page | `P6` Quiz | **LIVE** | score does **not** gate progression |
| **F6** | Frame screens | 5 screens, 5 review pages | `P0` Static | **LIVE** | none |

**Patterns not used anywhere in B02:** `P2` Accordion, `P3` Tooltip, `P5` Hotspot, `P7` Branching,
`P8` Calculator, `P9` Timeline, `P10` Before/After, `P11` Drag-Match.

---

# 2. Family detail

## F1 — Level 1 group master

| | |
|---|---|
| Instances | `STRUKTUR_TAMAN_MASTER` (4 cards), `PERABOT_TAMAN_MASTER` (5 cards) |
| Learner action | click any component card, in any order |
| Result | navigates to that component's `_MAIN` screen |
| Completion rule | `all_cards_visited` — a **variant** of the documented `all_cards_revealed` |
| Gate | global `Seterusnya` disabled until `group_complete[group]` |
| Required / optional | **required** (governed SOP: gate the next control) |

**Divergence from `P1`.** The documented `P1` reveals content *in place* on the same slide. F1's cards
are a **navigation hub**: clicking leaves the screen entirely and returns later with a tick. The
completion semantics match `P1`; the reveal semantics do not.

> **Classification:** `P1-NAV` — Reveal Cards, navigation variant. **Not a new production ID.**
> Requires CAIR ratification before MMD handoff.

## F2 — Main explanation screen

| | |
|---|---|
| Instances | 9, one per component |
| Learner action | none on content; one `Seterusnya` |
| Completion rule | **`vo_complete`** — not in the documented completion-rule table |
| Gate | `Seterusnya` disabled until the screen VO ends |
| Required / optional | **required** |

`P0` Static is **live**, so this family maps to a ratified production ID. The VO gate is an addition:
`taxonomy/decision-rules.md` §4 lists no `vo_complete` rule.

> **Classification:** `P0` Static + `vo_complete` gate. **`vo_complete` is a new completion rule and
> needs ratification** even though the pattern itself is live.

## F3 — Level 2 example screen

| | |
|---|---|
| Instances | 9, one per component |
| Items | 5, 5, 3, 3, 3, **1**, 3, 2, **1** — 26 total |
| Learner action | click any item, in any order |
| Result | opens that item's popup (F4) |
| Completion rule | `all_items_viewed` ≈ documented `all_cards_revealed` |
| Gate | `Kembali` disabled until `component_complete[component]` |
| Required / optional | **required** |

**Two divergences.**

1. **The reveal surface is a modal.** F3 is `P1` card selection whose reveal is an `F4`/`P4` modal.
   That is a **composite of two patterns on one screen**, and
   `extensions/mmd-elearning/interaction-decision-sop.md` says plainly: *"Keep one primary interaction
   per screen. Do not stack."* This composite is currently unratified against that rule.
2. **Two instances carry a single item** (`PAPAN_TANDA`, `BBQ_PIT`). A one-item `P1` is degenerate —
   the completion gate is satisfied by one click. Already flagged as `SINGLE_ITEM_EXAMPLE_TREATMENT`.

> **Classification:** `P1-MODAL` — Reveal Cards with modal reveal. **Composite; needs an explicit
> ruling against the one-primary-interaction rule.**

## F4 — Popup content state

| | |
|---|---|
| Instances | 26 states, one per source row |
| Learner action | read; close with `Tutup` |
| Result | returns to the same example screen; sets `item_viewed` |
| Navigation level | **none — a popup is a state, not a destination** |
| Required / optional | **required** (feeds the F3 gate) |

**Divergence from `P4`.** `taxonomy/decision-rules.md` selects `P4` Modal for *"exactly one optional
deep dive that would clutter the slide."* B02 uses **many** modals per screen and every one is
**required**. Both the cardinality and the optionality invert.

> **Classification:** `P4-REQ-N` — Modal, required-multiple variant. **Not a new production ID.**

## F5 — Kuiz

| | |
|---|---|
| Instances | 1 |
| Structure | 4 MCQ + 1 Multiple Response |
| Completion rule | documented `answered_correctly`; pass 3/5 = 60% |
| Gate | **none** — a sub-60% score does not block progression |
| Required / optional | tracked but **non-blocking** |

`P6` Quiz is **live**. The divergence is the gate: the governed SOP maps `P6` to *"gate next slide:
yes, for learning"*, and `B02-R-4`/S&G v0.2 §6.6 explicitly make B02's quiz non-blocking.

> **Classification:** `P6` Quiz, **non-blocking variant**. The pattern is live; the gating behaviour
> departs from the governed default and is already recorded as a provisional ruling.

## F6 — Frame screens

| | |
|---|---|
| Instances | `S01`, `S02`, `S03`, `RUMUSAN`, `TAMAT` |
| Learner action | `MULA` on S01, `Seterusnya` on TAMAT; none elsewhere |
| Completion rule | none |
| Required / optional | required for progression, not for interaction |

> **Classification:** `P0` Static. **Live, no divergence.** S02 is a video-character screen and S03 a
> narrator screen; both are `P0` under the documented rule (*"title, quote, section break, transition,
> pure narrative beat"*).

---

# 3. Completion-rule vocabulary — extensions required

`taxonomy/decision-rules.md` §4 documents five completion rules. B02 uses three that are not there.

| Completion rule | Documented? | Used by | Maps to LMS |
|---|:-:|---|---|
| `all_cards_revealed` | ✅ | — (F1/F3 use variants) | progress |
| `answered_correctly` | ✅ | F5 | `success_status` + score |
| **`vo_complete`** | ❌ | F2 ×9 | progress |
| **`all_items_viewed`** | ❌ | F3 ×9 | progress |
| **`component_complete` → `group_complete`** | ❌ | F1 ×2, F3 ×9 | two-tier progress |

**The two-tier gate is the substantive extension.** No documented pattern chains a child completion
into a parent completion. B02 does: `item_viewed` → `component_complete` → `group_complete` → global
`Seterusnya`. That is a **new completion topology**, not merely a new rule name, and it is the single
most important thing for CAIR to ratify before MMD handoff.

---

# 4. Production-ID readiness

| Family | Pattern | Live production ID? | MMD handoff blocked by |
|---|---|:-:|---|
| F2, F6 | `P0` Static | ✅ live | `vo_complete` rule (F2 only) |
| F5 | `P6` Quiz | ✅ live | non-blocking gate variant |
| F1 | `P1-NAV` | ❌ draft | pattern ratification |
| F3 | `P1-MODAL` | ❌ draft | pattern ratification + one-primary-interaction ruling |
| F4 | `P4-REQ-N` | ❌ draft | pattern ratification |

**Four of six families rest on draft patterns.** `P1` and `P4` are candidate IDs in the repository's
own reconciliation record and are **not** live. Under the frozen-namespace rule, F1, F3 and F4 cannot
be handed to MMD under a `P#` token until reconciled and ratified.

This is a governance finding, not a defect in the build: the v0.3 deck is a storyboard, and storyboards
do not carry production IDs. It matters at the MMD boundary, which is exactly where Stage 2 ends.

---

# 5. Implementation-ready summary

```
INTERACTION_FAMILIES            = 6
FAMILIES_ON_LIVE_PATTERNS       = 2   (F2, F5, F6 share P0/P6 — 3 families, 2 pattern IDs)
FAMILIES_ON_DRAFT_PATTERNS      = 3   (F1, F3, F4)
NEW_PRODUCTION_IDS_MINTED       = 0
PATTERN_VARIANTS_NAMED          = 4   (P1-NAV, P1-MODAL, P4-REQ-N, P6 non-blocking)
NEW_COMPLETION_RULES            = 3   (vo_complete, all_items_viewed, two-tier component/group)
COMPOSITE_SCREENS               = 9   (F3 stacks P1 selection with P4 reveal)
DEGENERATE_INSTANCES            = 2   (single-item F3: PAPAN_TANDA, BBQ_PIT)
```

## 5.1 What Stage 2 implementation can start on immediately

Nothing in F2, F5 or F6 depends on an unratified pattern or on Bariah's pending comments. Those three
families — 15 of 26 physical screens — are implementable against live production IDs today, subject
only to the `vo_complete` rule being written into the completion-rule table.

## 5.2 What Stage 2 must not start on

F1, F3 and F4 — 11 screens and all 26 popup states. They need, in order:

1. CAIR ratification of `P1` and `P4` as production patterns (or a decision to map them onto live IDs).
2. A ruling on the composite in F3 against the one-primary-interaction rule.
3. The A-05 outcome for the two degenerate F3 instances, which changes item counts but **never** the
   26-row source inventory.

---

# 6. Reconciliation with Bariah's three execution families

Bariah's completed review guide (A2) and S&G v0.3 (A3) approve **three** execution families. These are
architectural rulings, not mechanism labels: they say which screens exist, in what order, and where
each control returns to. **The six technical families of §1 do not disappear — they are the mechanics
each execution family is built from.** Every one of the nine components is assigned to exactly one
execution family; none is unassigned.

## 6.1 The three approved families

### FAMILY S — STRUKTUR TAMAN

Approved unchanged from v0.3. Guide item 4: *"Struktur Taman – Lulus"*; item 3: *"Struktur Persisir
Air – Lulus"*.

```
Struktur Taman group master (4 component cards)
  → component main explanation
    → Contoh [Nama Komponen]  (clickable example list)
      → example popup state    (close icon)
      → … all examples viewed  (all-viewed state, Kembali enabled)
    → Kembali  →  Struktur Taman group master
```

| Component | Source rows |
|---|---:|
| Struktur Persisir Air | 5 |
| Struktur Teduhan | 5 |
| Kemudahan Awam | 3 |
| Water Feature | 3 |
| **Total** | **16** |

`STRUCTURE_COMPONENTS_IN_FAMILY_S = 4`

Amendments inside Family S are presentational, not architectural: the canvas `Seterusnya` is removed
in favour of shell navigation (BFB-06/07), the instruction wording becomes *"Klik pada setiap
contoh…"* (BFB-10/11), popup labels take title case and the close control becomes an icon
(BFB-12/13/30).

### FAMILY P1 — MULTI-EXAMPLE PERABOT

New in v0.4. Guide item 1, verbatim: *"Kerusi Taman – penerangan + list contoh: Kerusi Kayu Keras /
Konkrit / Komposit (klik contoh - level 1, full slide, Kembali) / … list spesifikasi (klik spesifikasi
- level 2, pop up, butang tutup guna ikon)"* and *"Tong Sampah, Drinking Fountain – sama struktur
dengan Kerusi Taman"*.

```
Perabot Taman overview + list        (NO click, NO interaction level — entry via shell navigation)
  → component explanation + list of examples
    → click example  (LEVEL 1)  → full-slide example detail
        → specification items
          → click specification  (LEVEL 2)  → specification popup
            → close icon  →  back to the full-slide example detail
        → Kembali  →  back to the component explanation / example list
```

| Component | Source rows |
|---|---:|
| Kerusi Taman | 3 |
| Tong Sampah | 3 |
| Drinking Fountain | 2 |
| **Total** | **8** |

`PERABOT_COMPONENTS_IN_FAMILY_P1 = 3`

### FAMILY P2 — SPECIFICATION-DIRECT PERABOT

New in v0.4. Guide item 1, verbatim: *"Papan Tanda – penerangan + list spesifikasi: Bahan Panel /
Bahan Struktur Tiang / Grafik / Rekaan (klik spesifikasi - level 1, pop up, butang tutup guna ikon)"*
and *"BBQ Pit – sama struktur dengan Papan Tanda"*.

```
Perabot Taman overview + list        (NO click, NO interaction level)
  → component explanation + list of specification categories
    → click specification category  (LEVEL 1)  → popup
      → close icon  →  back to the specification list
```

| Component | Source rows | Specification categories |
|---|---:|---|
| Papan Tanda | 1 | 4 — `Bahan Panel`, `Bahan Struktur Tiang`, `Grafik`, `Rekaan` (named verbatim in A2) |
| BBQ Pit | 1 | several — **not enumerated in the feedback**; see U-04 |
| **Total** | **2** | |

`PERABOT_COMPONENTS_IN_FAMILY_P2 = 2`

> **There is no generic one-item `Contoh` screen for Papan Tanda or BBQ Pit under the latest Bariah
> ruling.** The v0.3 degenerate single-item example screen (§2, F3, `DEGENERATE_INSTANCES = 2`) is
> **removed**, not retained and not re-labelled. This also closes `B02-A-05` — the open question was
> *"one item, split, or fold?"* and the answer is **split into specification categories**, with
> `SOURCE_ROW_COUNT` unchanged.

## 6.2 Complete component assignment

| # | Component | Execution family | Source rows | Was (v0.3) |
|---|---|---|---:|---|
| 1 | Struktur Persisir Air | **S** | 5 | one global pattern |
| 2 | Struktur Teduhan | **S** | 5 | one global pattern |
| 3 | Kemudahan Awam | **S** | 3 | one global pattern |
| 4 | Water Feature | **S** | 3 | one global pattern |
| 5 | Kerusi Taman | **P1** | 3 | one global pattern |
| 6 | Tong Sampah | **P1** | 3 | one global pattern |
| 7 | Drinking Fountain | **P1** | 2 | one global pattern |
| 8 | Papan Tanda | **P2** | 1 | one global pattern (degenerate) |
| 9 | BBQ Pit | **P2** | 1 | one global pattern (degenerate) |
| | **Total** | **3 families** | **26** | |

```
EXECUTION_FAMILIES                = 3
UNKNOWN_COMPONENT_FAMILY          = 0
STRUCTURE_COMPONENTS_IN_FAMILY_S  = 4
PERABOT_COMPONENTS_IN_FAMILY_P1   = 3
PERABOT_COMPONENTS_IN_FAMILY_P2   = 2
```

## 6.3 Mapping the six technical families onto the three execution families

Every one of F1–F6 is placed. No technical family is left outside an execution family, and no
technical family is allowed to contradict one.

| Technical family (§1) | Mechanism | S | P1 | P2 | Frame | Fate in v0.4 |
|---|---|:-:|:-:|:-:|:-:|---|
| **F1** group master, clickable cards | `P1-NAV` | ✅ Struktur Taman master, 4 cards | ❌ | ❌ | — | **retained for S; removed for Perabot.** The Perabot master loses its click level and becomes a non-interactive overview + list |
| **F2** main explanation | `P0` + `vo_complete` | ✅ ×4 | ✅ ×3 (explanation + example list) | ✅ ×2 (explanation + specification list) | — | retained in all three; the list block that follows it differs per family |
| **F3** example-selection screen | `P1-MODAL` | ✅ ×4 `Contoh [Nama Komponen]` | ✅ ×3 — but the reveal is a **full slide**, not a modal | ❌ **removed** | — | S keeps the modal reveal; P1's Level 1 becomes a screen, which *un-stacks* the composite; P2 drops the level entirely |
| **F3′** full-slide example detail | `P0` + item list — **new in v0.4** | ❌ | ✅ ×8 examples | ❌ | — | new screen kind; the only genuinely new screen family in v0.4 |
| **F4** popup content state | `P4-REQ-N` | ✅ 16 popups, Level 1 | ✅ Level **2**, from the example detail | ✅ Level **1**, from the specification list | — | retained everywhere; **only the parent and the return target differ** |
| **F5** Kuiz | `P6` non-blocking | — | — | — | ✅ | unchanged in family terms; content amended per BFB-24 |
| **F6** frame screens | `P0` | — | — | — | ✅ S01, S02, S03, Rumusan, Tamat | unchanged in family terms; content amended per BFB-01/02/05/22/25 |

**The single most important line in that table is F4's.** A popup is a state, not a destination, in
all three families — what changes is which screen owns it and where the close icon returns. That is
why the Perabot restructure adds a navigation level without adding a navigation *depth* problem:

| Family | Popup parent | Close icon returns to | Max learner navigation depth |
|---|---|---|:-:|
| S | `Contoh [Nama Komponen]` example screen | that example screen | 2 |
| P1 | full-slide example detail | that example detail | **3** |
| P2 | specification list on the component explanation | that specification list | 2 |

`MAX_LEARNER_NAVIGATION_DEPTH` rises from **2 to 3** for Family P1 only. That invariant was declared
in `B02_FEEDBACK_DELTA_PROTOCOL_v0_4.md` §4.3 and is **amended by Bariah's ruling**, not violated by
it — the guide names the two levels explicitly (*"klik contoh - level 1"*, *"klik spesifikasi - level
2"*), on top of the component entry itself.

## 6.4 Where the two views could have contradicted each other, and how it was resolved

| Potential contradiction | Technical view (§1–5) | Bariah ruling | Resolution |
|---|---|---|---|
| Single-item example screens | F3 has two degenerate instances; flagged `SINGLE_ITEM_EXAMPLE_TREATMENT` | no generic one-item `Contoh` screen exists | **execution family wins** — F3 is removed for P2 |
| Composite screen stacking `P1` selection with `P4` reveal | flagged against the *one primary interaction per screen* rule | P1's Level 1 opens a **full slide**, not a modal | **the ruling reduces the conflict** for P1; it persists for S and P2 — see §8 |
| Perabot group master as a navigation hub | F1 `P1-NAV`, 2 instances | Perabot gateway has *"tiada klik/level"* | **execution family wins** — F1 has one instance in v0.4 |
| Uniform popup treatment | F4, 26 uniform states | Struktur density *Lulus*; Perabot restructured | both hold — F4 is uniform in *mechanism*, family-specific in *parentage* |

No unresolved contradiction remains between the two views.

---

# 7. Identifier separation — four distinct levels

The Perabot restructure multiplies interaction items without touching the source inventory. That is
only safe if the four identifier spaces stay explicitly separate. They are not interchangeable and
none of them is derived by counting another.

| Level | Identifier | Owned by | Changes in v0.4? | Count |
|---|---|---|:-:|---:|
| 1 | `source_row_uid` | the module source table | **NO** | **26** |
| 2 | `interaction_item_id` | the execution family | **yes** | rises |
| 3 | `runtime_state_id` | the runtime model | **yes** | rises |
| 4 | `review_page_id` | the storyboard rendering | **yes** | not claimed at this stage |

## 7.1 The rule

> **A source row is a fact about the module. An interaction item is a decision about the courseware.
> One row may yield many items; no number of items ever creates, destroys or renames a row.**

`SOURCE_ROW_COUNT = 26` and `SOURCE_ASSET_COUNT = 14` are invariant across this entire delta.
`SOURCE_ROW_COUNT_CHANGED_BY_INTERACTION_SPLIT = false`.

## 7.2 The three worked cases Bariah's ruling depends on

**Papan Tanda** — `K5-PL06-T03-B02-PAPAN-TANDA-ROW-01`

```
source_row_uid        1   ← unchanged, same UID, never renumbered
interaction_item_id   4   Bahan Panel · Bahan Struktur Tiang · Grafik · Rekaan
runtime_state_id      4 popup states + 1 list state
review_page_id        not claimed at this stage
```

**BBQ Pit** — `K5-PL06-T03-B02-BBQ-PIT-ROW-01`

```
source_row_uid        1   ← unchanged
interaction_item_id   several specification categories, count pending U-04
runtime_state_id      pending
review_page_id        not claimed at this stage
```

**Kerusi Taman** — 3 rows, one per material

```
source_row_uid        3   Kerusi Kayu Keras · Kerusi Konkrit · Kerusi Komposit  ← unchanged
interaction_item_id   3 example items, each opening a full-slide detail,
                      each detail carrying several specification items
runtime_state_id      3 example-detail screens + n specification popups
review_page_id        not claimed at this stage
```

## 7.3 What is deliberately not stated here

**No final review-page count is claimed at this stage.** The v0.3 figures (26 screens / 46 states /
63 pages) describe the superseded architecture and are retained only as the delta baseline. The v0.4
figures depend on U-04 (BBQ Pit categories) and on the per-example specification item counts, which
must be derived from the module source — not invented to make a total come out round. The screen/state
map is the next stage's deliverable, and it is explicitly out of scope for this one.

---

# 8. Interaction-pattern governance concerns — recorded separately

These are **repository-pattern governance items, not Bariah decisions.** They are kept in their own
section so that no CAIR ratification question is ever mistaken for a stakeholder ruling, and so that
nothing here can be read as Bariah having approved a pattern namespace change.

| # | Concern | Raised in | Status after Bariah's ruling | Owner |
|---|---|---|---|---|
| **G-1** | `P1` and `P4` are candidate IDs, not live production IDs | §4 | **unchanged** — Bariah's ruling is architectural and does not ratify pattern IDs | CAIR |
| **G-2** | F3 stacks `P1` selection with `P4` reveal, against *"Keep one primary interaction per screen"* | §2 F3 | **narrowed** — P1's Level 1 is now a full slide, so the composite persists only in Family S and Family P2 | CAIR |
| **G-3** | `vo_complete` is not in the documented completion-rule table | §3 | unchanged | CAIR |
| **G-4** | `all_items_viewed` is not in the documented completion-rule table | §3 | unchanged | CAIR |
| **G-5** | Two-tier `component_complete → group_complete` is a new completion **topology** | §3 | **extended** — Family P1 adds a third tier (`specification_viewed → example_complete → component_complete`) | CAIR |
| **G-6** | `P6` quiz is non-blocking, against the governed default | §2 F5 | unchanged; corroborated by S&G v0.3 | CAIR |
| **G-7** | Completion gating moves from a learner-canvas control to the LMS shell control | BFB-06/07 | **new** — the gate semantics survive, but the gated control is no longer authored in the deck | CAIR + LMS integration |
| **G-8** | `MAX_LEARNER_NAVIGATION_DEPTH` rises from 2 to 3 for Family P1 | §6.3 | **new** — amends the invariant declared in the delta protocol §4.3 | CAIR |

**None of G-1 … G-8 blocks the v0.4 documentation delta.** G-1, G-2 and G-8 block the MMD handoff.
G-7 additionally depends on U-03, which is Firdaus's to answer.

```
NEW_CANONICAL_PATTERN_IDS_MINTED = 0
```

Nothing in §6, §7 or §8 mints a `P#`. `FAMILY S`, `FAMILY P1` and `FAMILY P2` are **execution-family
labels in Bariah's own vocabulary**, deliberately named so that they cannot be confused with the
repository's `P0`–`P11` pattern namespace. `F3′` is a descriptive extension of this document's own
`F`-numbering, not an interaction ID.

---

# 9. Standing

Docs-only. No generator modified, no PowerPoint regenerated, no component propagated, no production
`P#` minted, no canonical ID issued, no screen/state map produced and no final review-page count
claimed. K5 remains locked and the live CAIR decision desk is untouched.
