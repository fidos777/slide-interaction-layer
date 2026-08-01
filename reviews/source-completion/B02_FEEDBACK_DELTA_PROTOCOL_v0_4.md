# B02_FEEDBACK_DELTA_PROTOCOL — K5 PL06 T03 B02 v0.4

```
FEEDBACK_DELTA_BLOCKED — BARIAH_FEEDBACK_ARTIFACT_NOT_RECEIVED
PROPAGATION_SCOPE_MODEL_COMPLETE
DECISION_REGISTER_UPDATE_CONTRACT_DEFINED
NO_COMMENT_FABRICATED
```

> **This document contains no Bariah comment, because none exists.** It is the executable machinery
> that turns comments into changes the moment they arrive: a classification schema, a measured
> propagation scope per change class, and the contract for updating the decision register. Every blast
> radius below is computed from the frozen v0.3 model, not estimated.

---

# 1. Why the delta itself is blocked

The v0.3 package was committed at `ba1f52a` today at ~15:00, for review *tomorrow morning*. The search
recorded in `B02_V0_4_INPUT_FREEZE.md` §5 found no feedback artifact anywhere — uploads, filesystem,
or Drive. The newest Bariah-owned file predates the package by about five hours and belongs to a
different workstream.

**Classifying comments that do not exist would mean inventing them.** That is the one failure mode
that would make every downstream artifact — the delta, the register update, the propagation plan —
confidently wrong. So the delta stays empty and the machinery around it is finished instead.

---

# 2. Comment classification schema

Every incoming comment is assigned exactly one class. The class determines the propagation scope, the
artifacts to touch, and whether a decision-register entry is required.

| Class | Meaning | Register entry? | May change `SOURCE_ROW_COUNT`? |
|---|---|:-:|:-:|
| `CLASS-1` | Content string — one display line, label or VO record | no | **no** |
| `CLASS-2` | VO policy — fidelity or popup-VO rule | **yes** (amends `B02-R-1` / `B02-R-2`) | **no** |
| `CLASS-3` | Item granularity — how many Level 2 items a source row yields | **yes** (resolves `B02-A-05`) | **no** |
| `CLASS-4` | State model — physical slides vs runtime states | **yes** (amends `B02-R-3`) | **no** |
| `CLASS-5` | Navigation — `Kembali` / `Seterusnya` target, label or gating | **yes** (amends `B02-R-5`) | **no** |
| `CLASS-6` | Frame screen — S01, S02, S03, Rumusan, Kuiz, Tamat | yes if it changes a ruling | **no** |
| `CLASS-7` | Terminology, lexicon or normalisation | **yes** (amends `B02-N-06` or the lexicon) | **no** |
| `CLASS-8` | Geometry, layout or density | no | **no** |
| `CLASS-9` | **Source correction** — a demonstrable extraction defect | **yes** | **YES — the only class that may** |

## 2.1 The `CLASS-3` / `CLASS-9` distinction

This is the one classification that must never be got wrong.

> **`CLASS-3` changes how many interaction items a source row produces.
> `CLASS-9` changes what the source says.**

If Bariah asks to split Papan Tanda into six items, that is `CLASS-3`:
`PROPOSED_INTERACTION_ITEM_COUNT` rises, `SOURCE_ROW_COUNT` stays **26**, and
`K5-PL06-T03-B02-PAPAN-TANDA-ROW-01` keeps its ID. Only evidence that the module actually contains a
different number of rows is `CLASS-9`, and that requires re-deriving row geometry from the hashed PDF.

## 2.2 Required fields per classified comment

```
comment_id          from the source artifact (PowerPoint comment id, or feedback-pack row)
anchor              review page ID (RP-nnn) where available
resolved_screen     physical learner screen ID
resolved_state      runtime state ID, where the comment targets a state
resolved_source_row source row UID, where the comment targets content
class               CLASS-1 … CLASS-9
verbatim            Bariah's words, unedited
scope               computed from §3
register_action     none | amend <decision_id> | new <decision_id>
status              CLASSIFIED | NEEDS_CLARIFICATION
```

`NEEDS_CLARIFICATION` is a legitimate terminal state. A comment that could be `CLASS-3` or `CLASS-9`
must not be guessed into one of them.

---

# 3. Propagation scope — measured, not estimated

Computed from the frozen v0.3 model: 26 physical screens, 46 runtime states, 63 review pages.

| Class | Screens touched | Review pages | Artifacts to regenerate |
|---|---|---:|---|
| `CLASS-1` | 1 | **2** (the popup page, plus the `ALL_VIEWED` page if a label changes) | content data → deck |
| `CLASS-2` | up to 26 | **41** (26 popups + 9 mains + 6 frames) | content data → deck, source map |
| `CLASS-3` | 1 example screen | **4** for `PAPAN_TANDA`, **4** for `BBQ_PIT` | content data, model, deck, screen/state map, source map, QA |
| `CLASS-4` | all 26 | **63** | model, generator, deck, screen/state map, QA, manifest |
| `CLASS-5` | 9 example + 2 masters | **48** | generator, deck, screen/state map, QA |
| `CLASS-6` | 1 per frame (6 total) | **1** each | content data → deck |
| `CLASS-7` | all | **63** | content data → deck, source map, matrix if a normalisation changes |
| `CLASS-8` | per family | group master **4** · main **9** · examples **44** · frame **6** | generator, deck, render check |
| `CLASS-9` | variable | up to **63** | **matrix first**, then content data, model, deck, all maps, QA, manifest |

## 3.1 Per-component scope, for `CLASS-1` and `CLASS-3`

| Component | Source rows | Review pages | Popup states |
|---|---:|---:|---:|
| Struktur Persisir Air | 5 | 8 | 5 |
| Struktur Teduhan | 5 | 8 | 5 |
| Kemudahan Awam | 3 | 6 | 3 |
| Water Feature | 3 | 6 | 3 |
| Kerusi Taman | 3 | 6 | 3 |
| **Papan Tanda** | **1** | **4** | **1** |
| Tong Sampah | 3 | 6 | 3 |
| Drinking Fountain | 2 | 5 | 2 |
| **BBQ Pit** | **1** | **4** | **1** |
| **Total** | **26** | **63** ¹ | **26** |

¹ 63 includes the 6 frame pages and the 2 group-complete pages, which belong to no single component.

## 3.2 Change-propagation order

Corrections flow in one direction. Reversing it is how a source inventory silently drifts.

```
source matrix  →  controlled content data  →  screen/state model  →  generator  →  deck  →  maps, QA, manifest
```

`CLASS-9` is the only class that enters at the first box. Every other class enters at the second or
later. **No class ever enters at the deck.**

---

# 4. Decision-register update contract

`DECISION_REGISTER_B02_v0_3.json` holds 13 entries, all `confirmed-CAIR-provisional`. v0.4 amends it
rather than replacing it.

## 4.1 Status transitions

| From | To | Trigger |
|---|---|---|
| `confirmed-CAIR-provisional` | `confirmed-Bariah` | Bariah confirms the ruling as built |
| `confirmed-CAIR-provisional` | `amended-Bariah` | Bariah changes it; `ruling` is rewritten and `superseded_by` recorded |
| `confirmed-CAIR-provisional` | `disputed` | Bariah's comment conflicts with S&G v0.2 and needs Firdaus / CAIR |
| any | *unchanged* | no comment touches it — **absence of comment is not confirmation** |

**The last row matters most.** A ruling nobody commented on stays `confirmed-CAIR-provisional`. It
does not graduate by silence.

## 4.2 Entries awaiting a specific answer

Each names the question its status depends on, so an incoming comment can be routed without
interpretation.

| Decision | Awaiting | Class if commented |
|---|---|---|
| `B02-R-1` | Is proposition-preserving VO acceptable, or is verbatim required? | `CLASS-2` |
| `B02-R-2` | Does every popup keep VO, or do specification popups go silent? | `CLASS-2` |
| `B02-R-3` | Are runtime states + review pages the right representation? | `CLASS-4` |
| `B02-R-4` | Rumusan / Kuiz / Tamat per bahagian — confirmed? | `CLASS-6` |
| `B02-R-5` | `Kembali` target, label and gating — confirmed? | `CLASS-5` |
| `B02-R-6` | Rumusan register and the site-application clause | `CLASS-6` / `CLASS-7` |
| `B02-L-01` | PL pronunciation note stays off-canvas? | `CLASS-6` |
| `B02-L-02` | Textual Mind Map spec sufficient? | `CLASS-6` |
| `B02-A-05` | **Papan Tanda and BBQ Pit — one item, split, or fold?** | `CLASS-3` |
| `B02-A-06` | Adaptive popup fields — confirmed? | `CLASS-1` / `CLASS-2` |
| `B02-A-09` | DOCX text / PDF structure precedence | `CLASS-9` |
| `B02-N-06` | `Kerusi Komposit` parenthesis — which reading? | `CLASS-7` |
| `B02-CAIR-INT-001` | **Not Bariah's to close** — Firdaus / CAIR only | — |

## 4.3 Invariants the update must not break

```
SOURCE_ROW_COUNT              = 26     unless a CLASS-9 correction is proven from the hashed PDF
COMPONENTS                    = 9
SOURCE_ASSETS                 = 14     none embedded
ORPHAN_SOURCE_ASSETS          = 0
PROVISIONAL_ROW_IDS           unchanged — never renamed or renumbered
MAX_LEARNER_NAVIGATION_DEPTH  = 2
```

A v0.4 register that changes `SOURCE_ROW_COUNT` without a `CLASS-9` evidence record is invalid.

---

# 5. Readiness

| Deliverable | State |
|---|---|
| v0.4 input freeze | ✅ complete — 5 of 6 inputs frozen and hashed |
| Interaction-family taxonomy | ✅ complete — 6 families, 0 new production IDs |
| Propagation scope model | ✅ complete — 9 classes, blast radius measured |
| Decision-register update contract | ✅ complete — transitions and invariants defined |
| **Bariah comment classification** | ❌ **blocked — no comments exist** |
| **Executable feedback delta** | ❌ **blocked — depends on the above** |

**When the feedback artifact arrives**, the remaining work is mechanical: extract comments, resolve
each anchor to a review page → screen → state → source row, assign a class, look up the scope in §3,
apply the register transitions in §4, and regenerate along the §3.2 path.

A commented `.pptx` is the better input — every PowerPoint comment carries a slide anchor, and slide
*n* maps directly to review page `RP-{n:03d}` in the frozen v0.3 deck.

---

# 6. Standing

Docs-only. No generator modified, no PowerPoint regenerated, no component propagated, no comment
fabricated, no ruling selected on behalf of Bariah or Firdaus. `B02-CAIR-INT-001` remains open and
still blocks canonical freeze, production approval and MMD build.
