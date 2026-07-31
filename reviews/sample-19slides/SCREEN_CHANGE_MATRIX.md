# SCREEN_CHANGE_MATRIX — K5 PL06 T3 B02, 19 screens

- **Status:** gate document — **docs-only**. Nothing implemented.
- **Standing:** sample only — **NOT CAIR-ratified**. `K5_LIVE_RATIFICATION_LOCKED`
- **Screen inventory:** probe v0.1 `docProps/app.xml`, 19-title vector, `<Slides>19</Slides>`

Legend — **source basis**: `MEASURED` = probe v0.1 and/or verified reviewed-deck control ·
`CONSTRUCTED` = no measured source, content built from structure and adjacent evidence.

---

## 1. Matrix

| # | Screen | Role | Source basis | Pattern / trigger / reveal | Layout family | Change vs source | Blockers |
|---|---|---|---|---|---|---|---|
| 1 | **S01** | TAJUK | `CONSTRUCTED` | none | title | new build | M1, M2 |
| 2 | **S02** | DIALOG | `CONSTRUCTED` | none (scene) | dialogue | new build; cast limited to `Haziq` + `Encik Roslan` | **`K5-DR-090` slot EMPTY** · M2 |
| 3 | **S03** | OVERVIEW | `CONSTRUCTED` | none | overview | new build; **no `Hilmi:` prefix** (`A-09`) | **`K5-DR-091` slot EMPTY** · **`K5-DR-011` exemption unresolved** · M2 |
| 4 | **S04** | CR_BASE — Struktur Taman | ✅ `MEASURED` | `CLICK_REVEAL` / **CARD** / `FULL_SLIDE` | **4-card 2 × 2** | **vertical-menu → Card grid** | `K5-DR-041` supersession **not in force** |
| 5 | **S05** | FULL — Struktur Persisir Air | `CONSTRUCTED` | reveal child | **split-STATE** | new build | M1, M2, M3 |
| 6 | **S06** | FULL — Struktur Teduhan | `CONSTRUCTED` | reveal child | split-STATE | new build | M1, M2, M3 |
| 7 | **S07** | FULL — Kemudahan Awam | `CONSTRUCTED` | reveal child | split-STATE | new build | M1, M2, M3 |
| 8 | **S08** | FULL — Water Feature | `CONSTRUCTED` | reveal child | split-STATE | new build; `Water Feature` **italic** | M1, M2, M3 |
| 9 | **S09** | TICK — Struktur Taman | ✅ `MEASURED` | completion state | **4-card 2 × 2** + `visited-tick` | vertical-menu → Card grid; **ticks re-anchored** | tick offsets are hand-placed (§3.2) |
| 10 | **S10** | CR_BASE — Perabot Taman | `CONSTRUCTED` | `CLICK_REVEAL` / **CARD** / `FULL_SLIDE` | **5-card 3+2** | new build | **`A-04` conditional** — Card/Hotspot unresolved · M2, M3 |
| 11 | **S11** | FULL — Kerusi Taman | `CONSTRUCTED` | reveal child | split-STATE | new build — **deliberately omitted from the probe** | M1, M2, M3 |
| 12 | **S12** | FULL — **Papan Tanda** | ✅ `MEASURED` | reveal child | **split-STATE** | ⚠️ **reverts Bariah's full-width edit**; heading box **restored**; locator corrected to `IMG-05`/243 | `A-05` high risk · `K5-DR-060` OPEN |
| 13 | **S13** | FULL — Tong Sampah | `CONSTRUCTED` | reveal child | split-STATE | new build | M1, M2, M3 |
| 14 | **S14** | FULL — Drinking Fountain | `CONSTRUCTED` | reveal child | split-STATE | new build; `Drinking Fountain` **italic** | M1, M2, M3 |
| 15 | **S15** | FULL — BBQ pit | `CONSTRUCTED` | reveal child | split-STATE | new build; `BBQ pit` **italic**, **lowercase `p` per measured source** | M1, M2, M3 |
| 16 | **S16** | TICK — Perabot Taman | `CONSTRUCTED` | completion state | **5-card 3+2** + `visited-tick` | new build | inherits `A-04` |
| 17 | **S17** | RUMUSAN | ✅ `MEASURED` | none | full-width panel | **revised Rumusan treatment** — 3 rules (`A-11`) | `K5-DR-032` not mechanically verifiable |
| 18 | **S18** | KUIZ | `CONSTRUCTED` | quiz | quiz | new build; **not** a matching activity | M2 · `P6` is live — do not cite bare |
| 19 | **S19** | TAMAT | `CONSTRUCTED` | none | end | new build | M2 |

**Totals — 4 `MEASURED` · 15 `CONSTRUCTED` · 9 split-STATE detail screens · 2 card bases · 2 tick states.**

---

## 2. Per-screen treatment applied uniformly

| Treatment | Applies to | Assumption | Exceptions |
|---|---|---|---|
| Concise source-bound display | all content screens | `A-07` | — |
| Fuller source-bound VO | all content screens | `A-08` | — |
| No `Hilmi:` prefix | **all 19**, including S03 | `A-09` | ⚠️ S03 exemption unresolved |
| English terms italic | S08, S14, S15, S17 | `A-10` | 3-term list only; nothing added by inference |
| `FULL_SLIDE` reveal (`detail-screen-kembali`) | S05–S08, S11–S15 | `A-06` | never `POPUP` |
| `Kembali` at 6.0028, 7.1009 | 9 detail screens | measured, unchanged by Bariah | — |
| `visited-tick` + `nav-lock-until-complete` | S09, S16 | LOCKED micro-behaviours §3.1 | — |

---

## 3. Screens carrying a known problem

### 3.1 S02 and S03 sit directly on **empty** decision slots — highest structural gap

The historical K5 corpus holds exactly two decision slots per PL, and for PL06 they are:

| Desk row | Type | `Keputusan Bariah (isi)` |
|---|---|---|
| `(K5, PL06, s02)` | `Scenario + Casting` | **empty** |
| `(K5, PL06, s03)` | `Reflection Prompt` | **empty** |

These map to sample screens **S02 DIALOG** and **S03 OVERVIEW**. The sample must therefore construct
two screens whose governing decisions **were never made** — not lost, not superseded: never filled.

- **S02** — the casting decision is unmade. The sample may use only the ratified cast:
  `Haziq` (Apprentice/learner, `CANONICAL`) and `Encik Roslan` (Mentor/expert, `CANONICAL`).
  The other nine names are `OFF-CANON` and must not appear.
- **S03** — the reflection decision is unmade, *and* the desk types `s03` as `Reflection Prompt` while
  the packet types `S03` as `OVERVIEW`. The correspondence that holds at `s02`↔`S02 DIALOG` **breaks
  here**, which is the same break that makes `K5-DR-011`'s "Slide 3 Narrator" referent unresolvable.

**Both screens are constructed on no decision at all.** They must be rendered as clearly provisional
and must not be read as instantiating an SME decision.

### 3.2 S09 tick geometry is hand-placed at both ends

Measured tick deviations on the reviewed deck reach **0.3113 in** from card centre, with three mutually
inconsistent alignment intents across four ticks. But the **canonical baseline is also imperfect**:
probe S09's ticks sit at pitch 0.77 / 0.76 / 0.77 against a menu-item pitch of 0.7846 / 0.7847 /
**0.8245** — max mismatch **0.083 in**.

Hand placement is inherited practice, amplified 3.7× by the review, **not introduced by it**. The
sample derives tick positions from the parameterised rule
`TICK = CARD + (CARD_W − 0.3937)/2, (CARD_H − 0.3937)/2` rather than copying either set of measured
coordinates. Bariah's own note declares `slide5` non-normative: `This is just to show tick icon.`

### 3.3 S12 is the one screen where the sample and the review disagree

| Property | Bariah's reviewed `slide4` | Sample S12 |
|---|---|---|
| Visual panel | 11.7371 wide (**+100.22 %** vs canon) | **5.8621** — canonical |
| Body | 0.9046, 4.4115 · 11.6371 × 2.5244, nested in panel | 6.8667, 2.5594 · 5.6621 × 3.8708 — right column |
| Body heading box | **deleted** (`sp10 del`) | **restored** — 5.6621 × 0.5068 |
| Source locator | `IMG-01`, ms 237 ❌ | **`IMG-05`, ms 243** ✅ |
| Δ vs Rumusan panel | **0.0079 in** — indistinguishable | 5.8671 in — 2.0009× narrower |

The sample reverts three of four. Only the locator correction is uncontested; the other three implement
`K5-DR-060`, which is an **unratified CAIR recommendation**.

### 3.4 S10 may not be a Card screen at all

`A-04` assumes 5-card 3+2. But S10's Card/Hotspot classification is `NOT_DETERMINABLE` — `asset_manifest.json`
and the source nodes are absent, so no screen in B02 has region data and a Hotspot gate is not
constructible. **If S10 resolves to Hotspot, S10 and S16 are rebuilt and `A-04` is void.**

---

## 4. Change classes across the sample

| Class | Screens | Count |
|---|---|---:|
| Measured, treatment changed | S04, S09, S12, S17 | 4 |
| Constructed from recovered structure + adjacent evidence | S05–S08, S10, S11, S13–S16 | 10 |
| Constructed on an **empty decision slot** | S02, S03 | 2 |
| Constructed, no decision required | S01, S18, S19 | 3 |

---

## 5. Modification statement

Docs-only. Nothing implemented. No PPTX modified, no compiler patched, no schema altered, no visual
candidate created. K5 remains locked; the live CAIR decision desk is untouched.
