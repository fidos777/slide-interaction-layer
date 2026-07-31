# STAGE_0A_STATUS_AND_NEW_EVIDENCE_ADDENDUM

```
STAGE_0A_DISCOVERY_COMPLETE
PROVISIONAL_REGISTER_NOT_CANONICAL
K5_LIVE_RATIFICATION_LOCKED
```

- **Status:** bounded addendum — **docs-only**
- **Applies to:** `STAGE_0A_EVIDENCE_INVENTORY.md`, `K5_DECISION_REGISTER_v1.1.md`
- **Effect:** status correction + new SME evidence + ontology correction. **No decision is ratified here.**

---

## 1. No historical K5 decision-ID namespace was found

Stated plainly, because everything downstream depends on it.

**A repository-wide search found no K5 decision-ID namespace of any kind.** The historical K5 corpus is
16 rows in `window.BARIAH_DATA.cair` inside `sbat/cair-decision-desk.html`. The row schema is:

```
Kursus · PL · Slide · Jenis Keputusan · Apa Bariah Perlu Buat · Keputusan Bariah (isi)
```

There is **no ID column**. `Keputusan Bariah (isi)` is **empty on all 16 rows**. The 16
`Apa Bariah Perlu Buat` values are prompts *for* decisions, not decisions.

Decision identity in the ratified system is not an ID at all — it is the composite key
`UNIQUE(course_code, pl, topik)` (`SBAT-ADR-004` §1). There was therefore never an ID namespace to
recover, and the crosswalk in `K5_DECISION_REGISTER_v1.1.md` §2 has an empty historical column by
construction. Every `renamed_from` field reads `—` for the same reason.

**Consequence:** no historical K5 decision was renamed, lost, or superseded by Stage 0A, because none
existed in identified form.

---

## 2. `K5_DECISION_REGISTER_v1.1.md` is a provisional synthesis

**It is not a released reconciled authority register.** It is a discovery artefact.

| Property | Value |
|---|---|
| Class | provisional synthesis / reconciliation record |
| Authority | **none** — it confers no authority on any entry |
| Canonical? | **No** |
| Ratifies anything? | **No** |
| `K5-DR-###` namespace | **PROVISIONAL — not issued as canonical** |
| Writable to `cair_decisions`? | **No** |
| Writable to the MMD readiness register? | **No** |
| Usable in MMD handoff? | **No** |

**The `K5-DR-###` namespace is expressly NOT issued as canonical.** It is a docs-only handle for
referring to entries inside this reconciliation. It dies at ratification and is replaced by the
composite key. Any downstream artefact that cites a `K5-DR-###` must cite it as *provisional* and must
not treat it as a decision identifier.

The register's own §10 summary — 4 ratified / 2 inherited-active / 11 open / 2 orphaned / 1 superseded
/ 3 withdrawn — describes **the state of the evidence**, not a set of decisions in force. The four
`RATIFIED` entries are recovered restatements of decisions ratified elsewhere (`SBAT-ADR-004`, the
character bank); their authority remains with their original source, not with the register.

---

## 3. Topik-level authority key — preserved unchanged

`K5-DR-001` stands exactly as recorded, and is restated here so it survives this status correction:

> **Decision granularity is TOPIK.** One topik = one row. Upsert key `UNIQUE(course_code, pl, topik)`.
> `decision_type = "topik-card"` is a static label, not part of the key. `choice` is a single JSON card.
> Per-**bahagian** rows were explicitly rejected: under one unique constraint they overwrite each other
> (`upsert satu memadam yang lain`).
> — `SBAT-ADR-004` §1, Accepted 2026-07-03, Bariah confirmed

**All B02 work — including the 19-slide sample gated by this addendum — folds into one card at
`(K5, PL06, T3)`.** B02 is a *bahagian* below the authority key. It gets no key row of its own. Nothing
in this addendum or in the sample gate creates, implies, or reserves a per-bahagian key.

---

## 4. New SME evidence — Bariah's clarification

> **Pairing = drag-and-drop matching.**

- **authority** SME (Bariah) · **status** clarification of existing practice · **scope** interaction ontology
- **effect on K5 decisions** none — see §4.2

### 4.1 The clarification is corroborated by the historical record — `MEASURED_FACT`

This is not new practice being introduced; it names practice already in the corpus.

`window.BARIAH_DATA.cair` contains **13 rows** typed `Interaction Pairing`. Every one of them defines
the task as drag-drop:

| Course | Example prompt |
|---|---|
| K3 PL01 s12 | `Sahkan pasangan item↔jawapan untuk aktiviti drag-drop (dari Jadual sumber).` |
| K2 PL01 s13 | `Sahkan pasangan drag-drop untuk 'Pengenalan Modul…' (item dari Jadual sumber).` |
| K2 PL03/04/05/06/08/09 | same construction, per PL |

13 of 13 `Interaction Pairing` rows say **drag-drop**. The clarification ratifies what the corpus
already did.

Independently, `taxonomy/decision-rules.md` line 23 already routes the concept:

> `Pairing across two sets (term↔definition, cause↔effect, tool↔use, item↔category)` → **`P11 Drag-Match`**

And `P11` is one of the **three live production IDs** (`taxonomy/INTERACTION_ID_RECONCILIATION.md` §1),
ratified live as `Drag-Match`, `T-DragMatch` in the draft namespace, backed by MMD-0 record `PL5T3-s4`.

**Reconciliation win: `DRAG_DROP` + `PAIRING/MATCHING` already has a live production ID — `P11`.**
It does not need one minted, and per the frozen namespace rule none may be minted.

### 4.2 The clarification does not touch any K5 decision — `MEASURED_FACT`

**K5 has zero `Interaction Pairing` rows.** Of the 65 rows in `BARIAH_DATA.cair`, the 13 pairing rows
are K2 and K3 only; K5's 16 rows are 8 `Scenario + Casting` and 8 `Reflection Prompt`. No K5 decision,
historical or Phase B1-derived, is affected.

Its value is preventive: it closes a latent ambiguity **before** `Pairing` could be mistaken for a
click-reveal association task in the B02 sample or in any later K5 work.

---

## 5. Interaction ontology correction

### 5.1 The corrected ontology, as instructed

```
CLICK_REVEAL
  trigger component : CARD | HOTSPOT
  reveal mode       : POPUP | FULL_SLIDE

DRAG_DROP
  pattern : PAIRING / MATCHING
  pattern : SEQUENCE / ORDERING
```

The correction is **two orthogonal axes on CLICK_REVEAL** — what the learner clicks, and how the result
is presented. Conflating them is what produced the Phase B1 confusion in the first place: Bariah's own
selection criterion (`K5-DR-040`) mixes the trigger axis (*"pada satu imej"* vs *"senarai atau grid
berasingan"*) with the presentation axis (*"paparan penuh, atau pop up"*) in the same three sentences.

### 5.2 Mapping onto the existing LOCKED vocabulary — **the correction refines, it does not replace**

`taxonomy/interaction-patterns-v0.md` already governs this ground. The corrected tokens are **new
names for existing entries**, not new patterns. Recording the map so the correction cannot silently
displace a locked family:

| Corrected token | Existing repo entry | Existing status |
|---|---|---|
| `CLICK_REVEAL` | §3.1 *Gated Click & Reveal (3-state)* | 🟢 **LOCKED** — WhatsApp Bariah 16/06/2026, "standard untuk propose ke client" |
| `CLICK_REVEAL` naming | glossary: SnG contract `Click and Show` · Bariah `Click & Reveal` | already reconciled — *"satu pattern, tiga nama"* |
| reveal mode `FULL_SLIDE` | §3.2 variant **`detail-screen-kembali`** | **has precedent** — sample cementitious 16/06 |
| reveal mode `POPUP` | §3.2 variants `overlay-with-close`, `overlay-maintain-VO` | ⚠️ **both DEFERRED** |
| reveal mode *(third, unnamed by the correction)* | §3.2 variant `inline` — detail replaces main screen | `sedia` (ready) |
| trigger `CARD` / `HOTSPOT` | composition axis under §3.1 | **not previously named as an axis** — this is the correction's actual new content |
| `DRAG_DROP` + `PAIRING/MATCHING` | `P11 Drag-Match` / `T-DragMatch` | 🟢 **LIVE** |
| `DRAG_DROP` + `SEQUENCE/ORDERING` | **no entry** — see §5.4 | **NEW — unbacked** |

Three consequences follow, and each matters:

1. **`CARD` vs `HOTSPOT` as a named trigger axis is the correction's genuine new content.** Under
   `interaction-patterns-v0.md` §3.1's scale note — *"Variasi masa depan = komposisi tolak/tambah
   micro-behaviour, **bukan pattern baru**"* — naming this axis is a composition refinement, **not** a
   new pattern. It requires no new `P#` and none may be minted.
2. **`POPUP` maps to two DEFERRED variants.** The corrected ontology names `POPUP` as a first-class
   reveal mode while the repo holds both its realisations deferred. That is not a contradiction — the
   *concept* is real and locked, the *binding* is deferred — but any screen selecting `POPUP` lands on
   deferred ground.
3. **`inline` has no slot in the corrected ontology.** The repo carries a third presentation variant,
   `inline` (detail replaces the main screen), marked `sedia`. A two-value reveal-mode enum cannot
   express it. **Flagged as `OPEN` — do not delete `inline` to fit the enum.** Deleting a real variant
   to satisfy a model is the failure class `interaction-patterns-v0.md` §3.2 warns against by name.

### 5.3 The POP UP anti-drift guardrail still applies — `MEASURED_FACT`

`interaction-patterns-v0.md` §3.2 carries a mandatory guardrail:

> **🔒 Peraturan konversi POP UP (guardrail anti-drift — WAJIB):** Jika storyboard tulis `POP UP`,
> JANGAN auto-convert kepada PopupModal. Perkataan tu behaviour SB, bukan komponen. Mesti pilih variant
> secara eksplisit, dengan provenance pilihan.

Recorded precedent for the cost of ignoring it: a K1 build auto-bound popup→PopupModal when the
storyboard meant full-screen branching — one afternoon of rework, 16/06.

**Renaming the axis `POPUP | FULL_SLIDE` does not lift this guardrail.** `POPUP` remains a behaviour
token requiring an explicit variant choice with provenance, not a component binding.

### 5.4 `SEQUENCE / ORDERING` has no backing entry — `OPEN`

The corrected ontology's second `DRAG_DROP` pattern has **no** entry in the repo taxonomy, **no**
`T-` draft ID, **no** live `P#`, and **no** instance in `BARIAH_DATA` (all 13 pairing rows are matching,
none is ordering). The nearest adjacent entries are `P9 Timeline` (ordered/chronological sequence —
a *navigation* pattern, not drag-drop) and the `clickable-any-order` micro-behaviour, which is the
explicit **negation** of ordering.

Recorded as `OPEN`. Under the promotion path it is a **CANDIDATE** requiring a `T-` handle before use.
**It has no bearing on B02** — no B02 screen uses drag-drop of any kind.

---

## 6. The correction does not block the B02 sample

**B02 uses `CARD` + `FULL_SLIDE`.** Both are on already-supported ground.

| Axis | B02 value | Status | Evidence |
|---|---|---|---|
| Pattern | `CLICK_REVEAL` | 🟢 LOCKED family | `interaction-patterns-v0.md` §3.1 |
| Trigger | `CARD` | composition refinement, no new pattern | `K5-DR-041`; reviewed `slide3`/`slide5` |
| Reveal mode | `FULL_SLIDE` → `detail-screen-kembali` | **has precedent** (cementitious 16/06) | reveal child carries `Kembali` at 6.0028, 7.1009 |
| Completion | `visited-tick` + `nav-lock-until-complete` | 🟢 LOCKED micro-behaviours | §3.1 rows 2, 5, 6; S09/S16 TICK screens |

**The guardrail is satisfied by pre-existing provenance, not by an assumption.** Probe v0.1 S04's note
panel states the variant explicitly and in the negative:

> `Klik hotspot -> reveal full-slide, bukan pop up.`

That is an explicit `FULL_SLIDE` selection with recorded provenance (`K5-DR-042`, inherited probe base,
verified against probe v0.1). B02 therefore never needs to resolve `POPUP`, and never touches the two
DEFERRED overlay variants.

**Had B02 required `POPUP`, the sample would be blocked.** It does not, so it is not.

`DRAG_DROP` is not exercised anywhere in B02 — S18 KUIZ is a quiz screen, not a matching activity, and
no B02 screen binds paired sets. The §5.4 gap is therefore out of the sample's path entirely.

---

## 7. General Hotspot capability versus B02-specific Card treatment

These are **separate concerns** and must not be collapsed. Conflating them would either delete a
capability or over-generalise a single screen's treatment.

### 7.1 General Hotspot capability — retained, unaffected

| Property | Value |
|---|---|
| Scope | layer-wide, all courses |
| Status | **retained** — a real trigger component under `CLICK_REVEAL` |
| Repo assets | `components/hotspot/hotspot.html`, `components/hotspot/README.md` |
| Draft ID | `T-Hotspot` (CANDIDATE) |
| Affected by B02? | **No** |

**Nothing in the B02 sample removes, deprecates, or narrows Hotspot.** `slide6` of the reviewed deck
(`IF HOTSPOT - CONTOH`) is Bariah's own worked Hotspot counter-example and remains valid evidence of
the capability.

### 7.2 B02-specific Card treatment — bounded to one bahagian

| Property | Value |
|---|---|
| Scope | **K5 PL06 T3 B02 only** — screens S04/S09 and S10/S16 |
| Status | `OPEN` — `K5-DR-041`, supersession **not in force** |
| Basis | resolves a **canonical** ambiguity, not a general preference |

The Card selection for B02 rests on a screen-specific measurement, not on a doctrine that Card beats
Hotspot. Probe S04 — cloned verbatim from canon slide 10 — declares `4 hotspot` in its note while
placing all four menu items at x 8.5938, **1.9271 in clear of the image's right edge at x 6.6667**.
Under `K5-DR-040` that screen satisfies **neither** branch: the children are not *"dipaparkan pada satu
imej"*, and there is no *"grid berasingan"* either. Card resolves it **for that geometry**.

**The generalisation is invalid.** A screen whose children genuinely sit on one covering image is a
Hotspot screen, and B02's Card selection says nothing about it.

**Additional standing blocker on Hotspot selection anywhere:** neither package contains coordinate or
region data for any screen — no image maps, no region identifiers, no slide-level `custDataLst`. A
Hotspot **gate** is not constructible until `asset_manifest.json` and the source nodes arrive. That is
a tooling gap, not a reason to prefer Card.

---

## 8–10. Constraints observed in this turn

| # | Constraint | Status |
|---:|---|---|
| 8 | **Do not unlock K5** | ✅ K5 remains locked. `SBAT-ADR-004` §3 and `OPEN_COURSES = ["K4"]` untouched. `K5_LIVE_RATIFICATION_LOCKED` is restated as a status token, not relaxed. |
| 9 | **Do not alter the live CAIR decision desk** | ✅ `sbat/cair-decision-desk.html` read-only. No edit to `BARIAH_DATA`, `OPEN_COURSES`, `INTENT_MAP`, or `saveCard`. The archived lineage copy is likewise untouched. |
| 10 | **Do not patch the compiler in this turn** | ✅ No compiler file was read for modification or written. No schema altered. No executable contract issued. |

Also unchanged: no PPTX modified; no visual candidate created; no canonical ID assigned; no baseline,
manifest, digest pin or freeze; no Stage 1/2/3 work.

---

## 11. Effect on the existing Stage 0A register

No register entry is deleted. The following are amended in status only.

| Entry | Amendment |
|---|---|
| *(all `K5-DR-###`)* | Namespace **not issued as canonical**. Provisional handles only. |
| `K5-DR-040` Card/Hotspot criterion | **Refined by §5.1.** The criterion mixes two axes; it should be read as trigger (`CARD`\|`HOTSPOT`) **and separately** reveal mode (`POPUP`\|`FULL_SLIDE`). Status remains `OPEN`. |
| `K5-DR-041` S04 → Card | **Scope narrowed** to K5 PL06 T3 B02 per §7.2. Supersession still **not in force**. |
| `K5-DR-042` inherited Hotspot treatment | **Re-read** under §5: `Klik hotspot -> reveal full-slide, bukan pop up` is now understood as *trigger = HOTSPOT, reveal mode = FULL_SLIDE*. Only the **trigger** is contested by `K5-DR-041`; the **reveal mode is not contested by anyone** and is what unblocks B02 (§6). |
| *(new)* `K5-DR-070` | **`DRAG_DROP` + `PAIRING/MATCHING` = drag-and-drop matching.** class UNIQUE · status **SME-CLARIFIED**, backed by live `P11` · authority SME (Bariah) · scope ontology-wide · evidence §4.1 · **not exercised in K5** |
| *(new)* `K5-DR-071` | **`DRAG_DROP` + `SEQUENCE/ORDERING`.** class UNIQUE · status **OPEN — no backing entry** · authority ontology correction · evidence §5.4 · needs a `T-` handle before use · **not exercised in B02** |
| *(new)* `K5-DR-072` | **Reveal-mode enum omits `inline`.** class **COLLIDED** · status OPEN · reason a two-value enum cannot express the repo's third `sedia` variant; do not delete `inline` to fit the enum (§5.2) |

Register totals become **29 entries**. All provisional.

---

## 12. Modification statement

No PPTX was modified. The live CAIR decision desk was not altered. The compiler was not patched. No
schema was changed, no executable contract issued, no visual candidate created, no canonical namespace
issued. K5 remains locked. This addendum is docs-only and bounded to the seven content items requested.
