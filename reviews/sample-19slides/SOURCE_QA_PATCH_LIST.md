# SOURCE_QA_PATCH_LIST — K5 PL06 T3 B02

- **Status:** gate document — **docs-only**. **No patch has been applied.**
- **Standing:** sample only — NOT CAIR-ratified
- **Boundary:** these are **source QA defects**, deliberately excluded from the pedagogical Decision
  Register (`K5_DECISION_REGISTER_v1.1.md` §9.1). Fixing them is editorial, not a decision.

Patch handles `P-##` are **local to this document** — not decision IDs, not a namespace.

---

## 1. Patch list

### `P-01` — Wrong source locator on Papan Tanda — **HIGH**
| | |
|---|---|
| **Screen** | S12 |
| **Defect** | Reviewed `slide4.xml` carries an off-canvas box citing `K5PL06T03-B02-IMG-01, ms 237` |
| **Correct** | **`K5PL06T03-B02-IMG-05, ms 243`** |
| **Evidence** | Probe v0.1 S12 cites `IMG-05`/243 correctly in **both** its visual panel (`Rectangle 8`) and its note panel (¶4). Reviewed `slide4` retains the correct citation in the note panel ¶5 while contradicting it in the added box. |
| **Cause** | Determinate — Bariah added `Rectangle 3` id 4 (`spChg add mod @23:06:09.402`) cloned from the **Struktur Taman** slides, which correctly cite `IMG-01`/237 for *their* subject. The clone carried the wrong subject's locator onto a Papan Tanda screen. |
| **Patch** | Use `IMG-05`, page 243 on S12. Do not carry the `IMG-01` box forward. |
| **Risk if unpatched** | A Perabot Taman screen bound to a Struktur Taman image — wrong asset in MMD handoff. |
| **Ref** | Addendum U4 · assumption `A-12` |

### `P-02` — Card visual label carries the wrong subject — **MEDIUM**
| | |
|---|---|
| **Screen** | S04 base state, card C2 |
| **Defect** | `Visual: Struktur Persisir Teduhan` — `Persisir` belongs to C1 (`Struktur Persisir Air`); the label beneath C2 correctly reads `Struktur Teduhan` |
| **Correct** | `Visual: Struktur Teduhan` |
| **Evidence** | No such string exists anywhere in probe v0.1. The four card rectangles are Bariah-created (`spChg add @23:07:55`). Copy-paste residue introduced in the review. |
| **Patch** | Drop `Persisir` from C2's visual placeholder. |
| **Ref** | Addendum N4 |

### `P-03` — `BBQ pit` recased against measured source — **MEDIUM**
| | |
|---|---|
| **Screens** | S15, S17 |
| **Defect** | Reviewed `slide8` reads `BBQ Pit`; measured source reads **`BBQ pit`**, lowercase `p` |
| **Evidence** | Probe v0.1 S17 display **and** `notesSlide12` VO both read `BBQ pit`, non-italic. Bariah changed **both** channels. |
| **Patch — sample** | Use **`BBQ pit`** (source form) with italic per `A-10`. |
| **⚠️ not a clean defect** | The four sibling furniture items — `Kerusi Taman`, `Papan Tanda`, `Tong Sampah`, `Drinking Fountain` — are title-cased in both base and revision. `BBQ pit` was the odd one out, and recasing made the list internally consistent. That is a defensible editorial reason, and it is still a source deviation. |
| **Standing** | **`OPEN_DECISION`, not a defect verdict.** The policy question — does list-internal consistency override exact source reproduction for proper-noun furniture labels — is for a human and governs `P-03`, `P-05`, `P-06` and `P-07` **together**. The sample takes source form pending that ruling. |

### `P-04` — `dan` → `Dan` over-capitalisation — **LOW**
| | |
|---|---|
| **Screen** | S17 |
| **Defect** | `Komponen Landskap - Struktur Taman **Dan** Perabot Taman`. Malay title case does not capitalise the coordinating conjunction `dan`. |
| **Correct** | `dan` |
| **Evidence** | Probe S17 reads `…Struktur Taman dan Perabot Taman`. |
| **Cause** | A title-case normalisation pass over-applied. The mechanism is a correction; the outcome on this token is a regression. |
| **Patch** | Restore lowercase `dan`. |

### `P-05` — Em dash replaced by hyphen-minus — **LOW**
| | |
|---|---|
| **Screen** | S17 |
| **Defect** | Source `Komponen Landskap **—** Struktur…` (U+2014); revision `Komponen Landskap **-** Struktur…` (U+002D) |
| **Standing** | `unresolved source variant` — grouped under `P-03`'s policy question. Sample takes source form (U+2014). |

### `P-06` — Sentence-terminal punctuation stripped from all bullets — **LOW**
| | |
|---|---|
| **Screen** | S17 |
| **Defect** | Source bullets all end `.`; revision bullets end with **no** punctuation, consistently 4/4 |
| **Standing** | Deliberate house style, applied uniformly — **display normalisation, not drift.** Grouped under `P-03`'s policy question. Sample follows the revision (no terminal punctuation) because consistency is evident and intentional. |

### `P-07` — Structural rewording in the Rumusan body — **LOW**
| | |
|---|---|
| **Screen** | S17 |
| **Defect** | `perabot taman merangkumi` → `Elemen Perabot Taman -`; `struktur taman merangkumi` → `Struktur Taman -`; `Drinking Fountain, BBQ pit.` → `Drinking Fountain dan BBQ Pit` |
| **Standing** | Display normalisation. Grouped under `P-03`'s policy question. Sample follows the revision — it is the treatment `A-11` is testing. |

### `P-08` — Title rendered twice — **LOW**
| | |
|---|---|
| **Screen** | S12 |
| **Defect** | Reviewed `slide4` `Title 1` (id 2) declares no `a:xfrm` and inherits the master title placeholder at (0.5833, 0.4583) 12.1667 × 0.5074, while `TextBox 6` (id 7) renders the same text at (0.6758, 0.4583). Bariah also changed the placeholder text from `Perabot Taman` to `Papan Tanda`, collapsing two heading levels into one. |
| **Patch** | Restore the section/screen split: placeholder = `Perabot Taman` (section), title bar = `Papan Tanda` (screen). This is consistent with `A-05` restoring the body heading box. |
| **Note** | Under `A-05` the sample carries **three** heading levels: section, screen title bar, body heading — as canon slide 6 does. |

### `P-09` — Card labels painted beneath cards — **LOW / latent**
| | |
|---|---|
| **Screen** | S09 (and S04 base if fills are added) |
| **Defect** | `spTree` order places labels L2–L4 **below** cards C2–C4. Nothing is occluded today because the cards declare no fill; it occludes the moment a fill is applied. |
| **Patch** | Emit labels after their cards. |

### `P-10` — Instruction line at capacity — **LOW / latent**
| | |
|---|---|
| **Screens** | S04, S09, S10, S16 |
| **Defect** | Instruction box `w = 6.3367` gives a 6.1367 in line box ≈ **49–53 chars** at 18 pt; the string `Klik pada setiap struktur untuk penjelasan lanjut.` is **49 chars**. Headroom **0–4 characters**. It does not wrap today; `spAutoFit` would grow the box downward into the 0.2463 in clearance above the card grid if it did. |
| **Patch** | Bind `INSTR_W` to the grid width (`R-INSTR`) rather than inheriting 6.3367. |
| **Note** | Card-label boxes are `noAutofit` with 22–24 char capacity against a 21-char longest label — a 25-char label overflows **silently**. Constructed screens must respect both ceilings. |

---

## 2. Not patched — deliberately

| Item | Why not |
|---|---|
| iSpring 23-tag block | Package residue, not source. Entered at the Tier-1 specification (identical block in probe v0.1). **Recommend non-preservation** on any rebuild — reinjecting it would propagate a wrong SCORM course ID, a wrong LRS endpoint and 14 dangling slide GUIDs. Not a sample concern. |
| `changesInfo` / `revisionInfo` | Toolchain residue. Evidentiary value only. |
| Stale `docProps` (`4 slaid` vs 8 slides; `revision = 1`; 2021 creation date) | Metadata, excluded from the register by requirement 10. |
| Tick coordinate deviations | Geometry measurement. The sample derives ticks from `R-TICK`, so no coordinate is patched — the rule replaces them. |
| `slide 4` / `slide 6` storyboard aliases | DO_NOT_CITE aliases, not defects. The sample uses `S01`–`S19` throughout. |

---

## 3. Patch summary

| Severity | Patches | Screens touched |
|---|---|---|
| HIGH | `P-01` | S12 |
| MEDIUM | `P-02`, `P-03` | S04, S15, S17 |
| LOW | `P-04` … `P-10` | S04, S09, S10, S12, S16, S17 |

**Only `P-01`, `P-02`, `P-04` and `P-08` are unambiguous defects.**
`P-03`, `P-05`, `P-06` and `P-07` are the same `OPEN_DECISION` seen four times — a normalisation policy
question for a human. `P-09` and `P-10` are latent layout fragilities, not errors in the current render.

---

## 4. Modification statement

**No patch has been applied.** No PPTX was modified, no compiler patched, no schema altered, no visual
candidate created. K5 remains locked; the live CAIR decision desk is untouched.
