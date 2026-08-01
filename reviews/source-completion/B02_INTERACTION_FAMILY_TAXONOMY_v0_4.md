# B02_INTERACTION_FAMILY_TAXONOMY — K5 PL06 T03 B02, Stage 2

```
STAGE_2_TAXONOMY_READY_FOR_IMPLEMENTATION
NO_NEW_PRODUCTION_P_ID_MINTED
PENDING_CAIR_PATTERN_RATIFICATION
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

Classification of every interaction the v0.3 build actually contains, expressed in the repository's
**existing** pattern vocabulary. Derived from the frozen v0.3 model — independent of any Bariah
feedback, so it is valid now and stays valid after the delta lands.

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

# 6. Standing

Docs-only. No generator modified, no PowerPoint regenerated, no component propagated, no production
`P#` minted, no canonical ID issued. K5 remains locked and the live CAIR decision desk is untouched.
