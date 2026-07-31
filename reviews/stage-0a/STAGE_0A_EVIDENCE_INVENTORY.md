# STAGE_0A_EVIDENCE_INVENTORY

- **Status:** reference / reconciliation record — **docs-only**
- **Stage:** 0A — K5 historical Decision ID reconciliation
- **Gate:** this document must be read before `K5_DECISION_REGISTER_v1.1.md`
- **Doctrine (inherited, binding):** *AI suggests; humans ratify. No production mapping until ratified.*
  — `taxonomy/INTERACTION_ID_RECONCILIATION.md` §0

This is the inventory and collision/orphan report. It does **not** issue decisions. It establishes
what evidence exists, what namespaces exist, and what breaks — so that the register can be read with
its limits visible.

---

## 0. Headline findings, stated up front

Three facts govern everything below and should be settled before the register is used.

**F1 — There is no historical K5 decision-ID namespace to crosswalk.**
The historical K5 corpus is 16 rows in `window.BARIAH_DATA` inside `sbat/cair-decision-desk.html`.
The row schema is `Kursus · PL · Slide · Jenis Keputusan · Apa Bariah Perlu Buat · Keputusan Bariah (isi)`.
**There is no ID column.** All 16 rows have an **empty** `Keputusan Bariah (isi)`.
Decision identity in the ratified system is a *composite key*, not an ID — `UNIQUE(course_code, pl, topik)`
per `SBAT-ADR-004` §1. A crosswalk was requested; its left-hand column is empty by construction.
`MEASURED_FACT`

**F2 — K5 is a locked course.**
`SBAT-ADR-004` §3 (Accepted, 2026-07-03): *"K4 sahaja terbuka. K2/K3/K5 **dikunci** (dua lapis: UI tidak
render + `saveCard` guard `OPEN_COURSES`)."* Verified in code: `sbat/cair-decision-desk.html` contains
`OPEN_COURSES = ["K4"]`. The lock lifts only when the per-course source drill is complete.
**Nothing in Stage 0A unlocks K5, and the register must not be read as unlocking it.** `MEASURED_FACT`

**F3 — The evidence and the ratified key are at different granularities.**
All Phase B1 evidence is at **Bahagian** granularity — `K5PL06T03**B02**`. The ratified decision key is
**Topik** granularity — `(K5, PL06, T3)`. `SBAT-ADR-004` §1 explicitly rejected per-bahagian rows
because they collide on the unique constraint and silently overwrite each other. Every Phase B1
finding must therefore be recorded **against `(K5, PL06, T3)`**, and B02 cannot hold its own key row.
This is the single most consequential reconciliation constraint in Stage 0A. `MEASURED_FACT`

---

## 1. Evidence inventory

### 1.1 Phase B1 evidence set — treated as the primary input

Per instruction, the `PHASE_B1_COMPARATIVE_ADDENDUM.md` correction register is **controlling** wherever
it corrects, upgrades or narrows the earlier five documents.

| Document | Role in Stage 0A | Controlling status |
|---|---|---|
| `BARIAH_REVIEW_INGEST.md` | annotation transcription, provenance classification, 4-to-8 mapping | superseded on §2.1, §4, §5–6, §8.5, §10.3 |
| `CARD_ARCHETYPE_SPEC.md` | Card geometry, five-card arithmetic | narrowed on §1.1, §2.6, §5 |
| `STATE_ARCHETYPE_OPTIONS.md` | reveal-child archetype options | upgraded on §2.3 Q1/Q2; narrowed on §2.1, §4 |
| `SME_RULE_CHECKABILITY.md` | rule-by-rule checkability, Card/Hotspot, normalisation, residue | upgraded §7.3; narrowed §1, §2.2, §4.4, §6.3, §8.3 |
| `DISPLAY_BUDGET_REDERIVED.md` | display budget, gate determination | upgraded §1, §8 |
| **`PHASE_B1_COMPARATIVE_ADDENDUM.md`** | **correction register — controlling** | — |

**Applied corrections carried into Stage 0A** (addendum §8):

| Ref | Effect on Stage 0A |
|---|---|
| C1 | No base-slide transposition occurred. Any decision framed on a slide-order change is void. |
| C2 | `This is just to show tick icon.` is inherited, **not** an SME rule → excluded from the register. |
| C3 | `Dipapar penuh selepas learner klik card.` is inherited text with one word changed → not an authored rule. |
| C4 | `Semua card selesai.` likewise → not an authored rule. |
| U1 | Base revision **= probe v0.1**. Provenance of all inherited text is now determinate. |
| U2 | Control slides verified against probe → inherited/authored split is measured, not inferred. |
| U3 | `VO subtopik tidak perlu lagi` **is** Bariah-authored → enters the register. |
| U4 | IMG regression is a **source QA defect**, not a decision → excluded per requirement 10. |
| U5 | Canonical reveal-child (canon slide 6) is **split-STATE** → the full-width form is a departure. |
| U6 | The missing body-heading box is a **deletion**, not an omission. |
| U7/U8 | Issued S12 display and `BBQ pit` source form are measured. |
| N9 | S04's Card/Hotspot ambiguity is **canonical**, not introduced by the review. |
| N10 | iSpring residue entered at the source specification → **package residue**, not a decision. |
| N11 | Prior editing history exists outside the reviewed change log. |

### 1.2 Historical K5 decision corpus — `MEASURED_FACT`

**Source:** `sbat/cair-decision-desk.html`, `window.BARIAH_DATA.cair` (65 rows total).
**Lineage copy:** `sbat/archive/Meja-Keputusan-CAIR-Bariah.md5-8cce12c60255c6b009b0b791da22636b.html`
(75 rows — same 65 plus 10 K4 rows), archived per `SBAT-ADR-004` §4.

| Course | Rows | Filled decisions |
|---|---:|---:|
| K2 | 25 | — |
| K3 | 24 | — |
| **K5** | **16** | **0** |
| K4 (archive only) | 10 | — |

**All 16 K5 rows, verbatim key fields:**

| PL | Slide | Jenis Keputusan | `Keputusan Bariah (isi)` |
|---|---|---|---|
| PL01 | s02 / s03 | Scenario + Casting / Reflection Prompt | *(empty)* |
| PL02 | s02 / s03 | Scenario + Casting / Reflection Prompt | *(empty)* |
| PL03 | s02 / s03 | Scenario + Casting / Reflection Prompt | *(empty)* |
| PL04 | s02 / s03 | Scenario + Casting / Reflection Prompt | *(empty)* |
| PL05 | s02 / s03 | Scenario + Casting / Reflection Prompt | *(empty)* |
| PL06 | s02 / s03 | Scenario + Casting / Reflection Prompt | *(empty)* |
| PL07 | s02 / s03 | Scenario + Casting / Reflection Prompt | *(empty)* |
| PL08 | s02 / s03 | Scenario + Casting / Reflection Prompt | *(empty)* |

The 16 `Apa Bariah Perlu Buat` prompts are **16 distinct strings**, each naming its own PL's topics —
template-instantiated, not duplicated. They are prompts *for* decisions, not decisions.

**K5 PL06 is the Phase B1 module.** Its prompt reads: *"Babak pembuka untuk 'Pengurusan Operasi
Pembinaan Landskap'… Topik teras: Proses Memula Kerja, Elemen Pembinaan Landskap, **Komponen
Landskap**"* — matching the reviewed deck's `Topik 3 Bahagian 2: Komponen Landskap`. So **PL06 T3 =
Komponen Landskap**, and the ratified key for all Phase B1 evidence is `(K5, PL06, T3)`.

**Critically: the historical K5 slots are s02/s03; the Phase B1 evidence covers S04, S09, S12, S17.
The two sets are disjoint.** There is no screen on which a historical K5 record and a Phase B1 finding
both speak — therefore **zero true decision-content collisions** between them. The collisions reported
in §3 are all *namespace* and *granularity* collisions, not contradictions of substance.

### 1.3 Ratified decisions recovered — **not reopened** (requirement 4)

| Source | Decision | Status | Date |
|---|---|---|---|
| `SBAT-ADR-004` §1 | Decision granularity = **TOPIK**; key `UNIQUE(course_code, pl, topik)`; `decision_type="topik-card"` is a static label, not part of the key; `choice` is one JSON card | **Accepted — Bariah confirmed** | 2026-07-03 |
| `SBAT-ADR-004` §1 | Per-bahagian rows rejected — they collide on the unique constraint and overwrite each other | **Accepted** | 2026-07-03 |
| `SBAT-ADR-004` §2 | Schema change + dependent code change = **one deploy unit** | **Accepted** | 2026-07-03 |
| `SBAT-ADR-004` §3 | **K2/K3/K5 locked**, two layers; K4 only open course | **Accepted** | 2026-07-03 |
| `BARIAH_DATA.chars` | **`Hilmi` — Course narrator (VO-only) — `LOCKED (memory)`** | **LOCKED** | — |
| `BARIAH_DATA.chars` | `Haziq` — Apprentice/learner — `CANONICAL`; `Encik Roslan` — Mentor/expert — `CANONICAL` | **CANONICAL** | — |
| `BARIAH_DATA.chars` | 8 further names `OFF-CANON`; `Encik Fahmi` → replaced by `Encik Aril` | **OFF-CANON** | — |
| `ADR-0001` | P0–P8 taxonomy | Accepted | 2026-06-26 |
| `ADR-0006` | Extend taxonomy P9–P11, append-only | Accepted | 2026-06-27 |
| `taxonomy/INTERACTION_ID_RECONCILIATION.md` §1 | Live production namespace = **`P0`, `P6`, `P11` only** | frozen (see §3.6) | M1.12A |
| `taxonomy/INTERACTION_ID_RECONCILIATION.md` §3 | **`P#` = live · `T-Name` = draft**; draft IDs never written to the MMD register | frozen (see §3.6) | M1.12A |
| `lexicon/ALIAS-GLOSSARY-v0.md` | 3 APPROVED contract aliases; **exact string match only**; alias never overrides canon | v0 draft | — |

**The `Hilmi` recovery is materially important.** Bariah's Phase B1 rule R1 —
*"Tidak perlu letak Hilmi di VO. Understood that it's Hilmi"* — is not a new position. It follows from
a **already-LOCKED** character-bank entry establishing Hilmi as the course narrator, VO-only. The rule
removes a prefix made redundant by a ratified fact. It is recorded in the register as a *derived
display rule*, not as a new casting decision, and the LOCKED entry is **not reopened**.

### 1.4 Complete ID namespace check (requirement 8)

Every ID-shaped namespace found in the repository:

| Namespace | Form | Population | Authority |
|---|---|---|---|
| Live interaction patterns | `P0`, `P6`, `P11` | **3 IDs, live** | MMD-0 register |
| Draft interaction taxonomy | `T-Name` | 11 candidates | reconciliation record, draft |
| Non-live P-tokens | `P1`–`P5`, `P7`–`P10` | contested — see §3.4 | none live |
| Architecture decisions | `ADR-0001`…`ADR-0006` | 6 | Accepted |
| Architecture decisions (3-digit) | `ADR-005`, `ADR-006` | 2 addenda | draft, pre-merge |
| SBAT decisions | `SBAT-ADR-001`…`004` | 4 | Accepted |
| CAIR decision key | `(course_code, pl, topik)` | composite — no ID | `SBAT-ADR-004` |
| MMD-0 readiness refs | `PL1T3-s2`, `PL3T1-s28`, `PL5T3-s4` | 3 | MMD-0 register |
| Contract aliases | free text, exact-match | 3 APPROVED | `ALIAS-GLOSSARY-v0` |
| Screen IDs (K5 PL06 T3 B02) | `S01`…`S19` | 19 | probe `docProps/app.xml` |
| Probe note labels | `Slide 4`, `Slide 4(1)`, `Slide 5b`, `Slide 6` | 4 — **collide, see §3.1** | storyboard prose |

**Proposed provisional namespace: `K5-DR-###`.**
Repository-wide search for `K5-DR` returns **0 matches**. It collides with none of the eleven
namespaces above: it is not a bare `P#` (forbidden to mint by the frozen namespace rule), not `T-`,
not `ADR-`/`SBAT-ADR-`, not a composite key, not an `S##` screen ID, and not a `PL#T#-s#` readiness ref.

**All `K5-DR-###` IDs are PROVISIONAL** and remain so until ratified through the promotion path in
`INTERACTION_ID_RECONCILIATION.md` §7. They are docs-only and must never be written to
`cair_decisions`, the MMD register, or any executable contract.

---

## 2. Evidence separation (requirement 3)

Four categories are held apart. Only category **A** may enter the pedagogical Decision Register.

### A. Decision evidence — enters the register

| Finding | Locus | Provenance |
|---|---|---|
| Card vs Hotspot selection criterion | `slide2.xml` id 6 (`sldId 9020`, `new`) | Bariah-authored |
| S04 → Card treatment recommendation | `slide3.xml` id 9 ¶0 | Bariah-authored |
| S04 inherited Hotspot treatment | probe S04 note ¶3–¶4 | inherited, pre-review |
| Narrator prefix suppression in VO | `slide8.xml` id 3 ¶0 | Bariah-authored |
| `Slide 3 Narrator` exemption | `slide8.xml` id 3 ¶0 | Bariah-authored |
| VO must not restate PL & Topik | probe S04 note ¶5 | **inherited** |
| VO must not restate Subtopik | `slide4.xml` id 6 ¶8 | Bariah-authored (addendum U3) |
| English terms italicised | `slide8.xml` id 3 ¶1 | Bariah-authored |
| Rumusan label suppression | `slide8.xml` id 3 ¶2 | Bariah-authored |
| Rumusan `anda` → `kontraktor` | `slide8.xml` id 3 ¶3 | Bariah-authored |
| Rumusan benefit → industry application | `slide8.xml` id 3 ¶4 | Bariah-authored |
| Concise display / full source-bound VO | `slide4`, `slide8` + probe S12 baseline | Bariah-executed |
| Character bank: Hilmi LOCKED, Haziq/Roslan CANONICAL | `BARIAH_DATA.chars` | **ratified** |

### B. Source QA defects — **excluded** (requirement 10)

| Defect | Locus | Addendum ref |
|---|---|---|
| `IMG-01`/ms 237 cited on a `Papan Tanda` screen; correct ref is `IMG-05`/ms 243 | `slide4.xml` id 4 | U4 |
| Card C2 reads `Visual: Struktur Persisir Teduhan` — `Persisir` belongs to C1 | `slide3`/`slide5` | N4 |
| `dan` → `Dan` over-capitalisation in a Malay title | `slide8.xml` id 25 ¶0 | §6.5 row 3 |
| `BBQ pit` → `BBQ Pit` — deviates from measured source | `slide8.xml` id 25 ¶3 | U8 |
| Title rendered twice (inherited placeholder + explicit title bar) | `slide4.xml` id 2 + id 7 | §1.1 |
| Labels L2–L4 painted beneath cards C2–C4 | `slide5.xml` | `CARD_ARCHETYPE_SPEC` §1.6 |

### C. Geometry measurements — **excluded** (requirement 10)

Card grid deviations (±0.09725 in label centring, 0.0063 in column offset); tick offsets (max 0.3113 in;
canonical baseline itself off by up to 0.083 in); panel widths (5.8621 / 11.7292 / 11.7371); display
budget (8/8 line slots, 89–97 ch/line); five-card arithmetic (2×3 overflows the stage by 0.5581 in;
3+2 requires ≥8.51 % width reduction).

**Boundary rule applied:** the *arithmetic* is measurement; the *choice among the options it produces*
is a decision. The choices appear in the register as `OPEN`; none of the numbers do.

### D. Package / toolchain residue — **excluded** (requirement 10)

23 iSpring tags (presentation-level, describing PL06 T3 B2 with 14 dangling slide GUIDs and a foreign
SCORM course ID — entered at the source specification per N10); `changesInfo1.xml` in both packages;
`revisionInfo.xml`; stale `docProps/app.xml`; `python-pptx` part renumbering; `a:endParaRPr` caret
markers; the probe's inherited 206-record change log (`sldId` 8000–8051, matching no known deck).

### E. CAIR recommendations — recorded, **not** decisions

Split-STATE archetype recommendation (`CAIR_RECOMMENDATION_PENDING_DECISION`); `MAX_DISPLAY_LINES = 8`
hard / 7 design target; bind `INSTR_W` to the grid; label-centring rule `R-LABEL-X`; deliberate
non-preservation of the iSpring block.

These are AI-side proposals. Under the inherited doctrine they may enter the register **only** as
`OPEN` items with `authority = CAIR-recommendation`, never as ratified positions.

---

## 3. Collision and orphan report

### 3.1 `slide 4` — HARD COLLISION, three referents — `MEASURED_FACT`

| Token as cited | Referent | Source |
|---|---|---|
| package part `slide4.xml` (reviewed deck) | **S12 — Papan Tanda**, reveal child | measured |
| note label `Slide 4 (Click & Reveal)` | **S04 — CR_BASE**, Struktur Taman | probe S04 note ¶0 |
| note label `Slide 4(1)` | **S09 — TICK**, completion state | probe S09 note ¶0 |
| package part `slide4.xml` (probe v0.1) | **S04** | measured |

Four uses, three distinct screens, and the **same filename means different screens in the two
packages**. This is the same failure mode as the ratified `P11` conflict: a token that silently
re-points a record. **`slide 4` must not be cited without a package qualifier.**

### 3.2 `slide 6` — HARD COLLISION, two referents — `MEASURED_FACT`

| Token as cited | Referent | Source |
|---|---|---|
| note label `Slide 6` | **S17 — RUMUSAN** | probe S17 note ¶0; reviewed `slide7`/`slide8` id 9 |
| `canon slide 6` | **the split-STATE child archetype** | `TREATMENT_PROBE_MAPPING.md` |

Citing "slide 6" can re-point a **Rumusan** decision onto a **STATE archetype**. Given that Phase B1's
central geometric finding is precisely that the reveal-child was collapsed onto Rumusan geometry, this
collision sits exactly where confusion is most costly. **Highest-severity alias in the set.**

### 3.3 Further storyboard aliases — DO_NOT_CITE

| Alias | Referent | Verdict |
|---|---|---|
| `Slide 5b (Full-slide reveal)` | S12 | DO_NOT_CITE — no `5b` exists in any namespace |
| `Slide 4(1)` | S09 | DO_NOT_CITE — parenthetical suffix has no schema |
| `Slide 6` | S17 | DO_NOT_CITE — see §3.2 |
| `Slide 4 (Click & Reveal)` | S04 | DO_NOT_CITE — see §3.1 |

Canonical replacements are the `S01`–`S19` screen IDs from `docProps/app.xml`, which are unambiguous.

### 3.4 `P#` — pre-existing conflict, now three systems — `MEASURED_FACT`

| Token | `taxonomy/decision-rules.md` | Candidate taxonomy | `SBAT-ADR-004` `choice.intent` | Live register |
|---|---|---|---|---|
| `P0` | Static | Static Slide / Navigation | in range | **Static / Presenter** |
| `P1` | Reveal Cards | — | in range | not live |
| `P5` | Hotspot | — | in range | not live |
| `P6` | Quiz | Visited Gate | in range | **Quiz / Visited-Gate** |
| `P7` | Branching | Drag & Drop | **range ends at P7** | not live |
| `P8` | Calculator | Quiz | out of range | not live |
| `P11` | Drag-Match | Timeline Navigation | out of range | **Drag-Match** |

`INTERACTION_ID_RECONCILIATION.md` §2 recorded two conflicting systems. **A third is in play:**
`SBAT-ADR-004` §1 defines `choice.intent` over `P1..P7|null` — a *range* that presupposes an assignment
it does not name, and that stops at `P7` while the live namespace runs to `P11`.

**Stage 0A consequence:** no `K5-DR` entry may carry a bare `P#` value. Interaction types are recorded
by canonical name, with `T-` cross-reference where one exists.

### 3.5 `ADR-006` vs `ADR-0006` — COLLISION — `MEASURED_FACT`

| Token | Decision | Status |
|---|---|---|
| `ADR-0006` | Extend the taxonomy with P9–P11 (append-only) | **Accepted**, 2026-06-27 |
| `ADR-006` | Case Study: 3 Clarification Cycles — *"Untuk digabung ke dalam ADR-006 (Cost of Asking) sebelum commit"* | **draft, pre-merge** |

`binding/K4-topic-cold-prep-v0-review-r1.md` cites *"rule ADR-006 langkah 2"* and *"calon ADR-006"* —
both referring to the **process** decision, not the taxonomy extension. The same pattern repeats at
`ADR-005` (Namespace E/I/P/R, draft) vs `ADR-0005` (Defer ontology.json sidecar, Accepted).

Two ADRs whose tokens differ by one leading zero and whose subjects are unrelated. Not a K5 decision,
but it is a live citation hazard in the same register the K5 work will be filed beside.

### 3.6 `INTERACTION_ID_RECONCILIATION` — ratification status is self-contradictory — `OPEN`

§1 states the live IDs "are frozen here as the authoritative reference" and §3 heads the namespace rule
"**Namespace rule (frozen)**". But §8 lists as **next step 1**: *"Firdaus ratifies this reconciliation
rule."*

The document declares itself frozen while recording its own ratification as pending. Stage 0A treats
the namespace rule as **binding** — it is committed, it is the only reconciliation in force, and acting
against it risks exactly the harm it documents. **But its formal status is unresolved and should be
closed**, because the whole `K5-DR` provisional-namespace argument rests on it.

### 3.7 `Reflection` — term in active use is declared non-canonical — COLLISION — `MEASURED_FACT`

`lexicon/ALIAS-GLOSSARY-v0.md` "Contoh BUKAN-alias": **`Reflection` — `TIADA-PADANAN` sehingga
diverifikasi — bukan alias, bukan kanon.**

Yet it is in active use in two places:

- `BARIAH_DATA.cair` — decision type **`Reflection Prompt`**, on 8 of 16 K5 rows;
- `sbat/data/k4-topik.json` — `interaktiviti_cadangan.jenis = "Reflection"` (the file is marked
  `provenans: BEKU`, frozen, `source_md5 f8a58d5f…`).

Half the historical K5 decision slots are typed with a term the glossary says is neither alias nor
canon. Under the glossary's rule 2 (**exact match only, no fuzzy match, no courtesy match**) these
rows cannot be mapped to a canonical interaction type at all.

`Scenario + Casting` — the other 8 rows' type — is likewise absent from the glossary. `Scenario with
Questions` **is** APPROVED, but rule 2 forbids treating `Scenario + Casting` as a variant of it.

**Neither historical K5 decision type resolves to a canonical interaction name.** Both are recorded as
orphaned terms.

### 3.8 Granularity collision — Bahagian vs Topik — `MEASURED_FACT`

| Layer | Granularity | Example |
|---|---|---|
| Phase B1 evidence | **Bahagian** | `K5PL06T03B02` |
| Ratified decision key | **Topik** | `(K5, PL06, T3)` |
| Historical K5 rows | **Slide** | `(K5, PL06, s02)` |

Three granularities across three layers, none of which nests cleanly into the key. `SBAT-ADR-004` §1
already diagnosed the failure mode: rows at a finer granularity than the key *"saling tindih pada
constraint unik yang sama (upsert satu memadam yang lain)"*.

**This is the collision most likely to cause real data loss**, and it is not hypothetical — it is the
recorded cause of the 03/07 incident in `SBAT-ADR-004` §2. Every Phase B1 decision must be folded into
a single `(K5, PL06, T3)` card, not written as separate B02 rows.

### 3.9 Orphan register

| # | Orphan | Why orphaned | Recoverable? |
|---:|---|---|---|
| O1 | 16 K5 `BARIAH_DATA` rows | slide-keyed (`s02`/`s03`) under a **superseded** schema; no `topik`; all empty; course locked | only via the per-course source drill required by `SBAT-ADR-004` §3 |
| O2 | Decision type `Reflection Prompt` | declared `TIADA-PADANAN` by the alias glossary | needs glossary verification |
| O3 | Decision type `Scenario + Casting` | absent from the glossary; exact-match rule forbids inference | needs glossary entry |
| O4 | Bariah's five Phase B1 rules | authored, but **no ratification channel is open** — K5 is locked and the desk does not render it | blocked on F2 |
| O5 | Discarded slide `sldId 9018` | created and deleted in-session; content unrecoverable | **no** |
| O6 | Probe's inherited 206-record change log | `sldId` 8000–8051 match neither deck | verify against the Tier-1 spec |
| O7 | `ISPRING_PRESENTATION_INFO_2` — 14 slide GUIDs | reference a 14-slide deck that is not this artifact | **no** — recommend non-preservation |
| O8 | Screens S01–S03, S05–S08, S10, S11, S13–S16, S18, S19 | 15 of 19 screens never measured | needs `packet_B02.json` |

### 3.10 Collisions expressly **not** found

Worth stating, because their absence narrows the work:

- **No decision-content contradiction between the historical K5 rows and Phase B1.** The historical
  slots are s02/s03; Phase B1 covers S04/S09/S12/S17. Disjoint (§1.2).
- **No duplicate `K5-DR` ID**, because none existed before this document.
- **No collision among the 16 historical prompts** — 16 distinct strings, template-instantiated per PL,
  not duplicates.
- **No conflict between Bariah's R1 and the ratified character bank** — R1 is *consequent on* the
  LOCKED `Hilmi` entry, not a change to it (§1.3).

### 3.11 DUPLICATE-SEMANTIC clusters — one concept, three namespaces — `MEASURED_FACT`

| Concept | `decision-rules.md` | Draft taxonomy | Bariah's Phase B1 wording | Live |
|---|---|---|---|---|
| Reveal-card interaction | `P1 Reveal Cards` | `T-Reveal` | `Click & Reveal (Card)` | — |
| Hotspot interaction | `P5 Hotspot` | `T-Hotspot` | `Click & Reveal (Hotspot)` | — |
| Quiz | `P6 Quiz` | `T-Quiz` | — | `P6` |

Three vocabularies for the same two concepts, none of which is the live namespace, and Bariah's Card /
Hotspot criterion — the governing definition in Phase B1 — is written in a **fourth** vocabulary that
appears in no registry at all.

---

## 4. Gate status

| Gate | Verdict |
|---|---|
| Historical K5 decisions inventoried | ✅ 16 rows, all empty, no IDs |
| Ratified decisions recovered without reopening | ✅ 12 recovered (§1.3) |
| Complete ID namespace checked | ✅ 11 namespaces (§1.4) |
| Provisional namespace collision-free | ✅ `K5-DR-###`, 0 matches |
| Evidence separated into A–E | ✅ (§2) |
| Collisions reported | ✅ 8 (§3.1–3.8) |
| Orphans reported | ✅ 8 (§3.9) |
| **K5 unlocked** | ❌ **No — and Stage 0A does not unlock it** |
| Any decision ratified by this stage | ❌ **No** |

**The register may now be read**, subject to: every `K5-DR-###` is PROVISIONAL; nothing here is
ratified; K5 remains locked; and all entries fold into the single ratified key `(K5, PL06, T3)`.

No PPTX was modified. No compiler was patched. No executable contract was issued. No visual candidate
was created. This document and the register are docs-only.
