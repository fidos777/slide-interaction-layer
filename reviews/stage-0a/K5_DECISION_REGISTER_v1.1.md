# K5_DECISION_REGISTER — v1.1

- **Status:** reference / reconciliation record — **docs-only**
- **Stage:** 0A · **Gated on:** `STAGE_0A_EVIDENCE_INVENTORY.md` — read that first
- **Doctrine (inherited, binding):** *AI suggests; humans ratify. No production mapping until ratified.*
- **All `K5-DR-###` identifiers are PROVISIONAL.** None is ratified. None may be written to
  `cair_decisions`, the MMD readiness register, or any executable contract.
- **K5 remains LOCKED** (`SBAT-ADR-004` §3; `OPEN_COURSES = ["K4"]`). This register does not unlock it.

---

## 0. Why "v1.1", when no v1.0 was found

A repository-wide search for a prior K5 Decision Register returned **nothing** — no `v1.0`, no
`DR-###` namespace, no ID column anywhere in the historical corpus. The version was specified as v1.1
and is honoured, but it should be read as **"first register, reconciled against a corpus that had no
register"** rather than as an increment over a v1.0 that exists somewhere unseen.

If a v1.0 does exist outside this session, **stop and reconcile before using this file** — a second
independent numbering would reproduce exactly the `P11`-class harm that
`taxonomy/INTERACTION_ID_RECONCILIATION.md` exists to prevent.

---

## 1. Reading rules

1. **Provisional means provisional.** `K5-DR-###` is a docs-only handle. Promotion path in §8.
2. **The key is the key.** Decision identity in the ratified system is `UNIQUE(course_code, pl, topik)`
   — `SBAT-ADR-004` §1. Every pedagogical entry below folds into **one** card at `(K5, PL06, T3)`.
   `K5-DR-###` numbers entries *within* that card; they are not row keys.
3. **No bare `P#`.** Minting or citing a bare `P#` is forbidden by the frozen namespace rule. Interaction
   types are named canonically, with `T-` cross-reference where one exists.
4. **Ratified entries are recovered, not reopened.** Entries marked `RATIFIED` are restated for
   traceability only. Nothing in Stage 0A revisits them.
5. **`INHERITED` ≠ Bariah's.** Text that predates the review carries `authority = probe-base` and must
   never be attributed to the SME.
6. **Aliases are DO_NOT_CITE** (§7). They are preserved so that historical prose stays readable, never
   so that it can be cited forward.

**Classification vocabulary:** `UNIQUE` · `COLLIDED` · `ORPHANED` · `COMPOUND` · `SUPERSEDED` ·
`WITHDRAWN` · `OPEN` · `DUPLICATE-SEMANTIC`.

---

## 2. Historical Decision ID crosswalk

The crosswalk was requested in full. Its historical column is empty by construction — see
`STAGE_0A_EVIDENCE_INVENTORY.md` F1. This is the complete mapping.

| Historical handle | Historical ID | Semantic content | → Provisional | Class |
|---|---|---|---|---|
| `BARIAH_DATA.cair` K5 × 8 (`PL01–PL08`, `s02`, `Scenario + Casting`) | **none** | prompt only; decision empty | `K5-DR-090` | ORPHANED |
| `BARIAH_DATA.cair` K5 × 8 (`PL01–PL08`, `s03`, `Reflection Prompt`) | **none** | prompt only; decision empty | `K5-DR-091` | ORPHANED |
| Slide-level CAIR schema (`Kursus·PL·Slide·Jenis Keputusan`) | **none** | superseded by topik-level schema | `K5-DR-S01` | SUPERSEDED |
| `SBAT-ADR-004` §1 | `SBAT-ADR-004` | topik granularity + upsert key | `K5-DR-001` | UNIQUE |
| `SBAT-ADR-004` §3 | `SBAT-ADR-004` | K2/K3/K5 lock | `K5-DR-002` | UNIQUE |
| `BARIAH_DATA.chars["Hilmi"]` | **none** | narrator, VO-only, LOCKED | `K5-DR-003` | UNIQUE |
| `BARIAH_DATA.chars` canonical + off-canon | **none** | cast ratification | `K5-DR-004` | UNIQUE |
| Probe S04 note ¶3–¶4 | **none** | `4 hotspot` / `Klik hotspot -> reveal full-slide` | `K5-DR-042` | UNIQUE (inherited) |
| Probe S04 note ¶5 | **none** | `VO PL & Topik tidak perlu lagi` | `K5-DR-012` | UNIQUE (inherited) |
| Reviewed `slide8` id 3 ¶0–¶4 | **none** | Bariah's five rules | `K5-DR-010/011/020/030/031/032` | COMPOUND → split |
| Reviewed `slide2` id 6 | **none** | Card vs Hotspot criterion | `K5-DR-040` | UNIQUE |
| Reviewed `slide3` id 9 ¶0 | **none** | S04 → Card recommendation | `K5-DR-041` | UNIQUE |
| Reviewed `slide4` id 6 ¶8 | **none** | `VO subtopik tidak perlu lagi` | `K5-DR-013` | UNIQUE |
| Reviewed `slide4`/`slide8` + probe S12 | **none** | concise display / full VO | `K5-DR-050` | UNIQUE |
| Phase B1 CAIR recommendations | **none** | state archetype; five-card layout | `K5-DR-060/061` | OPEN |

**Zero historical IDs were renamed, because zero existed.** Every `renamed_from` field below is
therefore `—`, and that is a finding, not an omission.

---

## 3. Register — recovered ratified decisions (NOT reopened)

### `K5-DR-001` — Decision granularity is TOPIK
- **class** UNIQUE · **status** RATIFIED · **authority** Bariah (confirmed) via `SBAT-ADR-004` §1
- **scope** all courses, all PL — governs this register's own shape
- **evidence** `decisions/SBAT-ADR-004.md` §1; verified in `sbat/cair-decision-desk.html`
  (`onConflict:"course_code…"`, `decision_type:"topik-card"`)
- **renamed_from** — · **supersedes** `K5-DR-S01` · **superseded_by** — · **alias_of** —
- **reason** One topik = one row; `UNIQUE(course_code, pl, topik)`; `choice` is a single JSON card.
  Per-bahagian rows were explicitly rejected: they collide on the unique constraint and overwrite each
  other. **This is why all Phase B1 B02-level findings fold into `(K5, PL06, T3)`.**

### `K5-DR-002` — K5 is a locked course
- **class** UNIQUE · **status** RATIFIED — **IN FORCE** · **authority** `SBAT-ADR-004` §3
- **scope** K2, K3, K5
- **evidence** `SBAT-ADR-004` §3; `OPEN_COURSES = ["K4"]` in `sbat/cair-decision-desk.html`
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** Two-layer lock (UI does not render + `saveCard` guard) until the per-course source drill
  is complete. **Every `OPEN` entry below is blocked on this lock, not merely awaiting review.**

### `K5-DR-003` — `Hilmi` is the course narrator, VO-only
- **class** UNIQUE · **status** RATIFIED — `LOCKED (memory)` · **authority** character bank
- **scope** all courses
- **evidence** `BARIAH_DATA.chars` — `{"name":"Hilmi","role":"Course narrator (VO-only)","status":"LOCKED (memory)"}`;
  present identically in `sbat/cair-decision-desk.html` and the archived lineage copy
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** Recovered because it is the **premise** of `K5-DR-010`. Bariah's *"Understood that it's
  Hilmi"* is a restatement of this locked fact, not a new casting decision. Not reopened.

### `K5-DR-004` — Canonical and off-canon cast
- **class** UNIQUE · **status** RATIFIED · **authority** character bank
- **scope** all courses
- **evidence** `BARIAH_DATA.chars` — `Haziq` (Apprentice/learner) `CANONICAL`;
  `Encik Roslan` (Mentor/expert) `CANONICAL`; `Encik Fahmi` `OFF-CANON → being replaced by Aril`;
  `Encik Aril`, `Puan Suraya`, `Puan Yati`, `Puan Hana`, `Mr. Jason`, `Encik Zulkifli`, `Puan Aishah` `OFF-CANON`
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** Recovered as the ratified input to `K5-DR-090` (the orphaned Scenario + Casting slots).
  Not reopened.

---

## 4. Register — Phase B1 pedagogical decisions

All entries in this section are **`OPEN`** unless marked `INHERITED`. None is ratified; the ratification
channel is closed by `K5-DR-002`.

### 4.1 `K5-DR-01C` — VO rule bundle → **SPLIT** (requirement 5)

- **class** COMPOUND · **status** SPLIT — do not cite `K5-DR-01C` as a decision
- **reason** Four separable rules were bundled by *locus* (the VO channel), not by content. They
  suppress four different things, have three different authorities, and two different provenances.
  Citing "the VO rule" is ambiguous across all four.
- **children** `K5-DR-010`, `K5-DR-011`, `K5-DR-012`, `K5-DR-013`

#### `K5-DR-010` — VO carries no narrator-name prefix
- **class** UNIQUE · **status** OPEN · **authority** SME (Bariah), authored **and** executed
- **scope** VO channel, all screens except the `K5-DR-011` exemption
- **evidence** rule text — `slide8.xml` id 3 ¶0, `spChg add mod @23:12:17.323`.
  Execution measured: probe `notesSlide16` (S12) opens `Hilmi: Papan Tanda.` → reviewed `notesSlide3`
  opens `Perabot Taman`; probe `notesSlide12` (S17) opens `Hilmi: …` → reviewed `notesSlide7` has no
  prefix. **Two removals**, both on screens she revised (addendum N6).
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** Redundant against `K5-DR-003`, which already locks Hilmi as the VO narrator.
  Checkability: **flagging-grade**, `^\s*Hilmi\s*:` on notes bodies — 5/5 on the reviewed deck, 3/3 on
  the probe. Not gate-grade: no scenario-dialogue instance exists anywhere in either package to
  calibrate the narrator/dialogue distinction (`SME_RULE_CHECKABILITY` §1.5).

#### `K5-DR-011` — Narrator-prefix exemption at "Slide 3 Narrator"
- **class** **COLLIDED** · **status** OPEN — **referent unresolved** · **authority** SME (Bariah)
- **scope** one screen — which screen is not determinable
- **evidence** `slide8.xml` id 3 ¶0, parenthetical `(Only put Hilmi in Slide 3 Narrator)`
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** Three candidate referents, none confirmable:
  (a) reviewed `slide3.xml` — the Card base state, whose notes contain **no** `Hilmi:`, so this reading
  makes the exemption vacuous;
  (b) packet screen **`S03 OVERVIEW`** — the most plausible reading;
  (c) `BARIAH_DATA` slot **`s03`**, typed `Reflection Prompt`.
  Readings (b) and (c) disagree about what screen 3 *is* — `S03` is OVERVIEW in the packet but `s03` is
  a Reflection Prompt slot in the desk. The lowercase `s0N` ↔ uppercase `S0N` correspondence holds
  plausibly at `s02`↔`S02 DIALOG` and **breaks** at `s03`↔`S03 OVERVIEW`.
  **Blocked on `packet_B02.json`.** Until resolved, `K5-DR-010` must be applied without exemption, or
  not enforced at all — it must not be applied with a *guessed* exemption.

#### `K5-DR-012` — VO does not restate PL and Topik
- **class** UNIQUE · **status** **INHERITED — ACTIVE** · **authority** probe-base (pre-review)
- **scope** VO channel
- **evidence** probe v0.1 `slide4.xml` (S04) note ¶5, verbatim `VO PL & Topik tidak perlu lagi`;
  retained unchanged on reviewed `slide1` (untouched control, shape-tree verified — addendum §3.1),
  `slide3` ¶6, `slide4` ¶6
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** **Must not be attributed to Bariah.** Base revision proven v0.1 (addendum §2); the line
  is present on a control slide verified identical to the probe. She retained it; she did not write it.

#### `K5-DR-013` — VO does not restate Subtopik
- **class** UNIQUE · **status** OPEN · **authority** SME (Bariah)
- **scope** VO channel
- **evidence** reviewed `slide4.xml` id 6 ¶8, `VO subtopik tidak perlu lagi`. **Absent from probe S12's
  note panel** — addendum U3, upgrading `BARIAH_REVIEW_INGEST` §10.3 from `NOT_DETERMINABLE`
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** Extends `K5-DR-012` to a third VO layer. Separated from it because provenance differs:
  012 is inherited, 013 is authored. Bundling them would attribute inherited text to the SME.

### 4.2 `K5-DR-020` — English-origin terms italicised in display

- **class** UNIQUE · **status** OPEN · **authority** SME (Bariah)
- **scope** learner display; VO/notes scope not stated by the rule
- **evidence** `slide8.xml` id 3 ¶1 — `English Words in italic (cth: Water Feature)`, with the example
  token itself carrying `rPr i="1"` (a self-exemplifying rule). Applied at exactly one locus:
  `slide8` (`Water Feature`, `Drinking Fountain`, `BBQ Pit`). **Zero italic runs on any English-origin
  term anywhere in probe v0.1** — 9 occurrences, 9 non-italic (addendum §6.3, N7)
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** No source precedent; entirely new practice. Mechanically checkable
  (`a:t` text vs `a:rPr/@i`) **given a term list** — and the term list is the open artifact, not the
  checker. Current lexicon seed is **3 terms** from one 8-slide deck. The loan-word boundary is the
  hard problem: `informasi` and `Water Feature` are both English-derived; only the second is in scope,
  and no algorithm separates them.

### 4.3 `K5-DR-03C` — Rumusan rule bundle → **SPLIT** (requirement 5)

- **class** COMPOUND · **status** SPLIT — do not cite `K5-DR-03C` as a decision
- **reason** Three rules share the *Rumusan* locus but differ in kind: one deletes tokens, one
  substitutes a token, one constrains meaning. Their checkability ranges from **gate-grade** to
  **not deterministic at all**. A single "Rumusan rule" would be enforced at the weakest member's
  confidence or the strongest member's strictness — both wrong.
- **children** `K5-DR-030`, `K5-DR-031`, `K5-DR-032`
- **cross-scope note** `K5-DR-020` and `K5-DR-050` also apply *at* Rumusan but are **not**
  Rumusan-scoped. They are deliberately not children.

#### `K5-DR-030` — Rumusan suppresses structural labels
- **class** UNIQUE · **status** OPEN · **authority** SME (Bariah), authored **and** executed
- **scope** Rumusan screens only
- **evidence** `slide8.xml` id 3 ¶2 — `Tidak perlu letak perkataan Kepentingan, Isi Utama, Manfaat`.
  Control pair: probe S17 / reviewed `slide7` carry all four label forms
  (`Kepentingan:`, `Isi utama:`, `Manfaat kefahaman:`) in display **and** VO; reviewed `slide8` and
  `notesSlide7` carry **none**
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** **The most checkable rule in the set — gate-grade.** 4/4 present in base, 0/4 in revision.
  Two calibrations are mandatory: match **case-insensitively** (the rule says `Isi Utama`, the source
  says `Isi utama` — a case-sensitive matcher misses the real occurrence), and match `Manfaat` as a
  **prefix** (source carries `Manfaat kefahaman:`). Scope to Rumusan via title-bar text.

#### `K5-DR-031` — Rumusan addresses `kontraktor`, not `anda`
- **class** UNIQUE · **status** OPEN — **scope unreconciled** · **authority** SME (Bariah)
- **scope** Rumusan screens; behaviour outside Rumusan **not** established
- **evidence** `slide8.xml` id 3 ¶3 — `Di Rumusan, Jangan guna anda, guna kontraktor`.
  Probe baseline: `anda` ×2, both on S17, display and VO; `kontraktor` **×0 anywhere**.
  Reviewed: `slide7` display `anda` ×1; `slide8` display `Kontraktor` ×1; changed in both channels
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** String test is trivially deterministic; the **scope boundary is the open question**.
  Source practice matches the rule on the 4 measured screens (S04/S09/S12 have zero `anda`), but that
  is 4 of 19. Per the standing instruction, the rule is **not** assumed to apply outside Rumusan.
  Blocked on `packet_B02.json`.

#### `K5-DR-032` — Rumusan benefit connects learning to industry application
- **class** UNIQUE · **status** OPEN — **`JUDGMENT_RULE_NOT_DETERMINISTIC`** · **authority** SME (Bariah)
- **scope** Rumusan benefit clause
- **evidence** `slide8.xml` id 3 ¶4 — `Manfaat – relate to application in industry`.
  Control pair: base `anda boleh mengenal pasti dan menerangkan … di tapak` → revised
  `Kontraktor dapat merancang, melaksana dan menyelenggara … di tapak`
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** **Lexical proxies produce false passes.** `di tapak` is present in *both* the compliant and
  the non-compliant text, so any site-reference keyword test passes the sentence Bariah rewrote
  *because* it failed her rule. What changed is the actor (`anda` → `Kontraktor`) and the verb class
  (cognition → operational) — both semantic. A three-part rubric (occupational actor + operational verb
  + site locative) discriminates the one available pair, but n = 1 cannot fix closed list membership,
  and condition 3 is inert. **Advisory prompt only; never a gate.**

### 4.4 Card versus Hotspot

#### `K5-DR-040` — Card / Hotspot selection criterion
- **class** UNIQUE · **status** OPEN · **authority** SME (Bariah) — **the governing definition**
- **scope** all Click-&-Reveal screens
- **evidence** `slide2.xml` id 6 (`sldId 9020`, slide-level `new`, `spChg add mod @23:09:30.194`),
  three paragraphs: Hotspot = items *"dipaparkan pada satu imej atau gambar rajah"*; Card = items
  *"disusun sebagai senarai atau grid berasingan"*; both reveal full-screen or pop-up by depth needed
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** — · see §7.2
- **reason** The only definitional statement distinguishing the two archetypes in any artifact
  inventoried. Its vocabulary is **DUPLICATE-SEMANTIC** against three other registries and belongs to
  none of them (§7.2). **A selection gate is not constructible from current evidence:** neither package
  contains coordinate or region data for any screen — no image maps, no region identifiers, no
  slide-level `custDataLst`; the only media in the probe is a checkmark SVG. Hotspot selection requires
  source-side region identification that the source does not supply.

#### `K5-DR-041` — S04 treated as Card *(proposed supersession)*
- **class** UNIQUE · **status** OPEN — **supersession NOT in force**
- **authority** SME (Bariah), recommendation
- **scope** S04 (`K5 PL06 T3`), and by extension S09 as its completion state
- **evidence** `slide3.xml` id 9 ¶0 — `(PENAMBAHBAIKAN, I think it's best/logical to use Click & Reveal (Card))`.
  Worked example: `slide3` (2 × 2 grid, 4 discrete visuals, `add` @22:45), `slide5` (completion state,
  rebuild — probe S09's 7 vertical-menu shapes `sp41–47` deleted, 9 card-grid shapes added)
- **renamed_from** — · **supersedes** `K5-DR-042` *(proposed — not in force)* · **superseded_by** —
- **reason** Resolves a **canonical** ambiguity, not one the review introduced: probe S04 — cloned
  verbatim from canon slide 10 — declares `4 hotspot` in its note while placing all four menu items at
  x 8.5938, **1.9271 in clear of the image's right edge at x 6.6667** (addendum N9). Under `K5-DR-040`
  the canonical screen satisfies **neither** branch. `slide6` (`IF HOTSPOT - CONTOH`) is Bariah's
  counter-example showing markers *inside* the image.
  **The supersession does not take effect until ratified**, and ratification is blocked by `K5-DR-002`.
  Until then `K5-DR-042` remains active.

#### `K5-DR-042` — S04 inherited Hotspot treatment
- **class** UNIQUE · **status** **INHERITED — ACTIVE** · **authority** probe-base (pre-review)
- **scope** S04
- **evidence** probe v0.1 `slide4.xml` note ¶3 `4 hotspot. Nombor selebihnya dibuang.` and ¶4
  `Klik hotspot -> reveal full-slide, bukan pop up.`; retained verbatim on reviewed `slide1` (control,
  verified) and `slide3` ¶4–¶5
- **renamed_from** — · **supersedes** — · **superseded_by** `K5-DR-041` *(proposed — not in force)*
- **reason** Recorded so the supersession has an explicit antecedent. Bariah **retained** this text on
  the very slide where she proposed Card — both instructions coexist in `slide3`'s note panel. That is
  a live internal inconsistency in the review artifact and must be resolved at ratification, not
  silently by preferring the newer text.

### 4.5 `K5-DR-050` — Concise learner display with full source-bound VO

- **class** UNIQUE · **status** OPEN · **authority** SME (Bariah), executed — gate determination
  `LOSSLESS_RESEGMENTATION_GATE_SUPERSEDED`
- **scope** display and VO channels
- **evidence**
  - **Issued S12 baseline:** probe `slide12.xml` display = 4 ¶, 346 ch, 50 words, 4 sentences,
    7 commas — **byte-identical to its own VO body** in `notesSlide16`. Display **was** VO.
  - **Revision:** reviewed `slide4` display = 8 ¶, 285 ch, 40 words, 0 sentences. VO body **unchanged
    verbatim**; only the header changed (`Hilmi: Papan Tanda.` → `Perabot Taman`, per `K5-DR-010`).
  - **Coverage:** 4/4 propositions retained; proposition 3 carried at *higher* granularity (4 bullets).
  - **Lexis:** 7 removed token types — all function words, copula, modal, relativiser, or the repeated
    subject `papan tanda` (de-duplication against the title bar). **Zero tokens added**; display
    vocabulary is a strict subset of VO vocabulary; 85.4 % unique-token retention.
  - **Rumusan control pair:** base display ≈ VO (496 vs 503, 1.4 % apart); revision display **−7.5 %**
    while VO **+7.2 %**, opening a 14.8 % gap, with `Dengan memahami komponen-komponen ini,` retained
    in VO and absent from display. **Truncation cannot produce a VO that grows.**
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** Shorter display is **not** source deletion where proposition coverage remains in the VO
  and the source locator. Both conditions hold on both measured screens. **Coverage is 2 screens of
  19** — the determination must not be generalised to the packet without measurement.

---

## 5. Register — open CAIR decisions

These carry `authority = CAIR-recommendation`. Under the inherited doctrine they are AI-side proposals
and can never be more than `OPEN` until a human ratifies.

### `K5-DR-060` — Reveal-child state archetype
- **class** UNIQUE · **status** OPEN · **authority** CAIR-recommendation
- **scope** all FULL screens (S05–S08, S11–S15)
- **evidence** Canonical STATE (canon slide 6, measured via probe S12): visual panel
  0.8046, 1.7813 **5.8621** × 5.2604 (43.97 % of stage), body in a right column 6.8667, 2.5594
  5.6621 × 3.8708, **dedicated heading box** `TextBox 16` 5.6621 × 0.5068, `Kembali` below.
  Canonical RUMUSAN (S17): panel **11.7292** × 5.2604 — the two canonical archetypes differ by
  **2.0009×** in panel width. Reviewed `slide4`: panel widened to **11.7371**, i.e. within **0.0079 in
  (1.1 px at 1920)** of the Rumusan panel, and the heading box **deleted** (`sp10 del @22:52:53`).
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** `CAIR_RECOMMENDATION_PENDING_DECISION` — recommend **restoring** the canonical split form.
  The addendum upgraded this from a proposal against an unknown canon to a **restoration** of a measured
  one (N2). Cost is real and stated: body line box falls 11.1246 → 5.1496 in (**−53.7 %**), reflowing
  the measured 285-char body from 8 lines to ~13.
  ⚠️ **Do not minute this as "Option A" or "Option B."** `TREATMENT_PROBE_README.md` uses "Option B" for
  the *pairing* (vertical-menu base + split-STATE child) — which contains what
  `STATE_ARCHETYPE_OPTIONS.md` calls **Option A**. The labels invert across documents (addendum §5.3).

### `K5-DR-061` — Five-card layout for S10
- **class** UNIQUE · **status** OPEN · **authority** CAIR-recommendation
- **scope** S10 CR_BASE (Perabot Taman) and S16 its completion state
- **evidence** S10 binds **five** FULL children S11–S15 = Kerusi Taman, Papan Tanda, Tong Sampah,
  Drinking Fountain, BBQ Pit (recovered from the probe's stale `app.xml`, addendum §1.3).
  Arithmetic: 2 × 3 at reviewed card size needs 8.0581 in vertically — **exceeds the entire 7.5 in
  stage by 0.5581 in**. 3 + 2 fits vertically unchanged but **no** arrangement preserves the reviewed
  card width inside the deck's 11.75 in content band (would require a **−0.0275 in** gap). Options
  ranked by deviation count: 5A (−12.45 % width, 4 deviations) · 5B (−8.51 %, gap 0.7074 → 0.4750,
  5 deviations) · 5A′ (aspect-locked, 7) · 5C (exact size, band breached 0.735 in) · 5D (2 × 3 scaled,
  −46.97 %).
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** **A fifth card cannot be free** — either card width drops ≥ 8.5 %, or the gap drops 33 %,
  or the content band is abandoned. **Conditional:** S10's own Card/Hotspot classification is
  `NOT_DETERMINABLE`. If S10 resolves to Hotspot under `K5-DR-040`, this decision does not arise.

---

## 6. Register — orphaned, superseded and withdrawn

### `K5-DR-090` — Historical K5 `Scenario + Casting` slots (× 8)
- **class** **ORPHANED** · **status** ORPHANED · **authority** none — never filled
- **scope** K5 PL01–PL08, slot `s02`
- **evidence** `BARIAH_DATA.cair`, 8 rows; `Keputusan Bariah (isi)` empty on all 8; 8 distinct
  PL-specific prompts (template-instantiated, **not** duplicates)
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** Orphaned on **three** independent grounds: keyed by `Slide`, not `topik`, so unmappable
  under `K5-DR-001` without the source drill; the type string `Scenario + Casting` appears in **no**
  canonical vocabulary and the alias glossary's exact-match rule forbids inferring it from the APPROVED
  `Scenario with Questions`; and the course is locked. Ratified input `K5-DR-004` (canonical cast) is
  available whenever they are recovered.

### `K5-DR-091` — Historical K5 `Reflection Prompt` slots (× 8)
- **class** **ORPHANED** · **status** ORPHANED · **authority** none — never filled
- **scope** K5 PL01–PL08, slot `s03`
- **evidence** `BARIAH_DATA.cair`, 8 rows, all empty
- **renamed_from** — · **supersedes** — · **superseded_by** — · **alias_of** —
- **reason** As `K5-DR-090`, plus a sharper term problem: `lexicon/ALIAS-GLOSSARY-v0.md` lists
  **`Reflection`** under *"Contoh BUKAN-alias"* — `TIADA-PADANAN` until verified, *"bukan alias, bukan
  kanon."* **Half the historical K5 decision slots are typed with a term the lexicon declares
  non-canonical**, and the same term is live in the frozen `sbat/data/k4-topik.json`. Resolve at the
  glossary before recovery.

### `K5-DR-S01` — Slide-level CAIR decision schema
- **class** **SUPERSEDED** · **status** SUPERSEDED · **authority** `SBAT-ADR-004` §1
- **scope** all courses
- **evidence** legacy schema `Kursus · PL · Slide · Jenis Keputusan · Apa Bariah Perlu Buat ·
  Keputusan Bariah (isi)`, retained in `BARIAH_DATA` as artefact and **not rendered**
- **renamed_from** — · **supersedes** — · **superseded_by** `K5-DR-001` · **alias_of** —
- **reason** Superseded 2026-07-03. Recorded because `K5-DR-090`/`091` are keyed under it and cannot be
  read without it.

### Withdrawn decision candidates

Three items were carried as SME-authored rules in the earlier Phase B1 documents and are **withdrawn**
from the register on the addendum's controlling corrections. Withdrawn, not deleted — so the earlier
attribution is not silently rewritten.

| ID | Text | Withdrawn because | Ref |
|---|---|---|---|
| `K5-DR-W01` | `This is just to show tick icon.` | **verbatim in probe S09** → `INHERITED_PROBE_CONTENT`, never an authored rule | C2 |
| `K5-DR-W02` | `Semua card selesai.` | probe S09 reads `Semua **hotspot** selesai.` → inherited text, one word changed | C4 |
| `K5-DR-W03` | `Dipapar penuh selepas learner klik card.` | probe S12 reads `… klik **hotspot**.` → inherited text, one word changed | C3 |

- **class** WITHDRAWN · **status** WITHDRAWN · **authority** probe-base
- **reason** All three were reclassified when probe v0.1 became measurable. W02 and W03 remain
  *evidence* of the Hotspot → Card shift recorded at `K5-DR-041`, but they are **not** independent
  decisions. Also withdrawn, though never a decision: the base-slide transposition claim in
  `BARIAH_REVIEW_INGEST` §2.1 (correction C1) — probe order is `9003, 9011, 9008, 9016`, identical in
  relative order to the reviewed deck; **no transposition occurred.**

---

## 7. Alias register — **DO_NOT_CITE** (requirement 6)

Preserved so historical prose stays readable. **None may be cited forward.**

### 7.1 Storyboard slide-label aliases

| Alias | True referent | Severity | Canonical replacement |
|---|---|---|---|
| `Slide 6` | **S17 RUMUSAN** | **HARD** — also denotes the split-STATE archetype as *"canon slide 6"* | `S17` |
| `Slide 4 (Click & Reveal)` | **S04** | **HARD** — `slide4.xml` is S12 in the reviewed package, S04 in the probe | `S04` |
| `Slide 4(1)` | **S09** | HIGH — parenthetical suffix has no schema | `S09` |
| `Slide 5b (Full-slide reveal)` | **S12** | HIGH — no `5b` exists in any namespace | `S12` |

`Slide 6` is the highest-severity alias in the set: citing it can re-point a **Rumusan** decision onto
a **STATE archetype** — precisely the axis on which Phase B1's central geometric finding sits.

### 7.2 Interaction-type vocabulary — DUPLICATE-SEMANTIC

| Concept | `decision-rules.md` | Draft taxonomy | `K5-DR-040` wording | Live |
|---|---|---|---|---|
| Reveal-card | `P1 Reveal Cards` | `T-Reveal` | `Click & Reveal (Card)` | *(none live)* |
| Hotspot | `P5 Hotspot` | `T-Hotspot` | `Click & Reveal (Hotspot)` | *(none live)* |
| Quiz | `P6 Quiz` | `T-Quiz` | — | `P6` |

- **class** DUPLICATE-SEMANTIC · **status** unreconciled
- **reason** Four vocabularies for two concepts. The governing definition (`K5-DR-040`) is written in
  the one vocabulary that appears in **no** registry. `P1` and `P5` are **not live** — bare `P#` may
  not be cited. Use canonical names with `T-` cross-reference until ratified.

### 7.3 Adjacent citation hazards — not K5 decisions, recorded to prevent misfiling

| Token | Referent A | Referent B |
|---|---|---|
| `ADR-006` / `ADR-0006` | *Case Study: 3 Clarification Cycles* (draft, pre-merge) | *Extend taxonomy P9–P11* (**Accepted**) |
| `ADR-005` / `ADR-0005` | *Namespace E/I/P/R* (draft addendum) | *Defer ontology.json sidecar* (**Accepted**) |
| `P11` | Drag-Match (**live**) | Timeline Navigation (draft) — pre-existing HARD CONFLICT |
| `s03` / `S03` | `Reflection Prompt` slot (desk) | `S03 OVERVIEW` (packet) |

---

## 8. Promotion path

Adapted from `taxonomy/INTERACTION_ID_RECONCILIATION.md` §7 — the ratified precedent for this class of
work.

```
K5-DR-### PROVISIONAL  (this register — docs-only)
  → K5 source drill complete            ← blocked by K5-DR-002
  → K5 unlocked in OPEN_COURSES         ← requires a schema+code deploy unit (SBAT-ADR-004 §2)
  → packet_B02.json + asset_manifest.json attached   ← closes scope on 010/011, 031, 040, 050
  → Bariah confirms learning intent
  → Laila confirms MMD / iSpring feasibility
  → behaviour, required fields, completion rule, accessibility fallback, QA rule defined
  → human ratification
  → folded into ONE topik-card at (K5, PL06, T3)     ← never as per-bahagian rows
  → enters cair_decisions and may be used in MMD handoff
```

**Do not** mint a bare `P#`. **Do not** reuse or repoint live `P0`, `P6`, `P11`. **Do not** write any
`K5-DR-###` to `cair_decisions` — the provisional handle dies at ratification and is replaced by the
composite key.

---

## 9. Non-decision findings — **excluded** from the register (requirement 10)

Listed here so nothing is lost, and kept out of the pedagogical register so nothing is mis-ratified.

### 9.1 Source QA defects
| Finding | Locus | Severity |
|---|---|---|
| `IMG-01`/ms 237 cited on `Papan Tanda`; correct is `IMG-05`/ms 243. Probe S12 cites correctly in **both** places; Bariah added a box cloned from the Struktur Taman slides. Correct ref survives only in the note panel | `slide4.xml` id 4 | **HIGH — provenance regression** |
| Card C2 reads `Visual: Struktur Persisir Teduhan`; `Persisir` belongs to C1. No such string in probe | `slide3`/`slide5` | MEDIUM |
| `dan` → `Dan` — Malay title case does not capitalise the conjunction | `slide8` id 25 ¶0 | LOW — regression |
| `BBQ pit` → `BBQ Pit` — deviates from measured source, in display **and** VO | `slide8` id 25 ¶3 | MEDIUM — see below |
| Title rendered twice (inherited placeholder + explicit title bar) | `slide4` id 2 + id 7 | LOW |
| Labels L2–L4 painted beneath cards C2–C4 | `slide5` | LOW — latent |

**Normalisation approval remains an `OPEN_DECISION`**, not a defect verdict: 5 of the 10 measured
source→display differences are defensible normalisations that nonetheless deviate from source. The
policy question — does list-internal consistency override exact source reproduction for proper-noun
furniture labels — is for a human, and it governs `BBQ pit` and three sibling rows together.

### 9.2 Geometry measurements
Card grid deviations (±0.09725 in label centring, mirror-symmetric; 0.0063 in column offset); tick
offsets (max 0.3113 in — **but the canonical baseline is itself off by up to 0.083 in**, so hand
placement is inherited practice amplified 3.7×, not introduced); panel widths; display budget (8/8 line
slots, zero headroom, 12-character margin on the longest line); five-card arithmetic.
**The numbers stay here; the choices they inform are `K5-DR-060` and `K5-DR-061`.**

### 9.3 Package / toolchain residue
23 iSpring tags (presentation-level; describe PL06 T3 B2 with 14 dangling slide GUIDs and a foreign
SCORM course ID and LRS endpoint; **identical block present in probe v0.1** → entered at the source
specification, not introduced by the probe build or by Bariah); `changesInfo1.xml` in both packages
(reviewed: 65 records, Bariah, 29 Jul; probe: 206 records, Bariah, 14–25 Jul, `sldId` 8000–8051
matching neither deck); `revisionInfo.xml`; stale `docProps/app.xml`; `python-pptx` renumbering;
`a:endParaRPr` caret markers.

**Recommendation carried, not decided:** do **not** reinject the iSpring block on any compiler rebuild
— it would propagate a wrong SCORM course ID, a wrong LRS endpoint and 14 dangling references.

### 9.4 Slide metadata
`dc:title` still reads *"Contoh Treatment — 4 slaid"* against 8 slides; `cp:revision = 1` after 56
recorded changes; `dcterms:created 2021-11-01` inherited from a donor template; `dc:creator` = SMEC
vs `cp:lastModifiedBy` = Bariah Ahmad (probe: `CAIR compiler`).

### 9.5 Open provenance question — `PROVISIONAL_IDENTIFIER`
The probe's inherited 206-record change log names **Bariah Ahmad** as sole editor across 33 slides,
14–25 July, while the probe's own `lastModifiedBy` is `CAIR compiler`. If that log belongs to the
Tier-1 specification, **Bariah is also an author of the source the probe was cloned from** — which
changes how her review annotations should be weighted, since parts of what reads as external SME
review may be the source author revising her own earlier work.
Verify by checking whether `SB_K5PL06T03B02_TIER1_STORYBOARD_SPEC_v1_2_CANDIDATE.pptx` (`d523f467…`)
has `sldId`s in the 8000–8051 range. **This bears on `authority` for every entry in §4.**

---

## 10. Register summary

| ID | Title | Class | Status |
|---|---|---|---|
| `K5-DR-001` | Decision granularity = TOPIK | UNIQUE | **RATIFIED** |
| `K5-DR-002` | K5 course locked | UNIQUE | **RATIFIED — in force** |
| `K5-DR-003` | Hilmi = narrator, VO-only | UNIQUE | **RATIFIED — LOCKED** |
| `K5-DR-004` | Canonical / off-canon cast | UNIQUE | **RATIFIED** |
| `K5-DR-01C` | VO rule bundle | COMPOUND | SPLIT |
| `K5-DR-010` | VO carries no narrator prefix | UNIQUE | OPEN |
| `K5-DR-011` | Narrator-prefix exemption at "Slide 3" | **COLLIDED** | OPEN — referent unresolved |
| `K5-DR-012` | VO does not restate PL & Topik | UNIQUE | **INHERITED — active** |
| `K5-DR-013` | VO does not restate Subtopik | UNIQUE | OPEN |
| `K5-DR-020` | English terms italicised | UNIQUE | OPEN |
| `K5-DR-03C` | Rumusan rule bundle | COMPOUND | SPLIT |
| `K5-DR-030` | Rumusan suppresses structural labels | UNIQUE | OPEN — gate-grade |
| `K5-DR-031` | Rumusan uses `kontraktor` | UNIQUE | OPEN — scope unreconciled |
| `K5-DR-032` | Rumusan benefit → industry | UNIQUE | OPEN — not deterministic |
| `K5-DR-040` | Card / Hotspot criterion | UNIQUE | OPEN |
| `K5-DR-041` | S04 → Card treatment | UNIQUE | OPEN — supersession not in force |
| `K5-DR-042` | S04 inherited Hotspot treatment | UNIQUE | **INHERITED — active** |
| `K5-DR-050` | Concise display / full VO | UNIQUE | OPEN |
| `K5-DR-060` | Reveal-child state archetype | UNIQUE | OPEN — CAIR |
| `K5-DR-061` | Five-card layout for S10 | UNIQUE | OPEN — CAIR |
| `K5-DR-090` | Historical `Scenario + Casting` × 8 | **ORPHANED** | ORPHANED |
| `K5-DR-091` | Historical `Reflection Prompt` × 8 | **ORPHANED** | ORPHANED |
| `K5-DR-S01` | Slide-level CAIR schema | **SUPERSEDED** | SUPERSEDED |
| `K5-DR-W01/W02/W03` | Three inherited note lines | **WITHDRAWN** | WITHDRAWN |

**26 entries · 4 ratified (recovered, not reopened) · 2 inherited-active · 11 open · 2 orphaned ·
1 superseded · 3 withdrawn · 2 compound splits · 1 collided.**

---

## 11. Modification statement

No PPTX was modified — `ee4f5479…8bb9e7` and `24dcaa04…1d471c` both re-verified unchanged. The compiler
was not patched. No schema was altered. No executable contract was issued. No visual candidate was
created. No canonical decision ID was assigned — every `K5-DR-###` is provisional and docs-only. K5
remains locked. No Stage 1, Stage 2 or Stage 3 work was performed.
