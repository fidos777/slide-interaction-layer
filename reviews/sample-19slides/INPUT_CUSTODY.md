# INPUT_CUSTODY — K5 PL06 T3 B02 19-slide sample

- **Status:** gate document — **docs-only**. Nothing implemented.
- **Authority key:** `(K5, PL06, T3)` — B02 is a bahagian below the key and gets no key row
  (`SBAT-ADR-004` §1)
- **Course status:** `K5_LIVE_RATIFICATION_LOCKED` — this sample is **not** CAIR-ratified

---

## 1. Inputs held — verified

All hashes re-measured this turn.

| # | Artifact | Bytes | SHA-256 | Class |
|---:|---|---:|---|---|
| I1 | `3f626ac5-BARIAH_REVIEW_8SLIDES.pptx` | 68,710 | `ee4f54790bd22afb82457237d63d290eb6ac0ceabbead88ec5f7d7fced8bb9e7` | SME review evidence |
| I2 | `5ccb3cc2-K5PL06T03B02_TREATMENT_PROBE_4SLIDES_NOT_A_STORYBOARD1.pptx` | 55,269 | `24dcaa049130d067de2ce95704cae99bd5a49c0b2c8d99819604a8dbac1d471c` | **probe v0.1** — source-bound clone |
| I3 | `TREATMENT_PROBE_README.md` | 2,868 | `06b0ef5d92ba1ad2506e30746af303d898354ad0325e2157b22fc3edbaef000c` | probe documentation |
| I4 | `TREATMENT_PROBE_MAPPING.md` | 2,638 | `3bbfe6b3a2e7a906d143199de9dfe4f61199f793a3c719d9696c0102819f53a4` | screen ↔ canon mapping |
| I5 | `TREATMENT_PROBE_VALIDATION.md` | 3,408 | `44d102db5cc5c1e07b49bb6065a4160544cf20a96a9231a2a620e8af3c671c2c` | v0.1↔v0.2 validation |
| I6 | `LOCAL_REVIEW_CHECKLIST.md` | 3,075 | `d2c92e63242f287cc5aad15cf1b7bbb61fe3439ebdb32274f9d38675d50c37b9` | render-review checklist |
| I7 | `sbat/cair-decision-desk.html` | 100,731 | *(in-repo)* | `BARIAH_DATA` — historical corpus + character bank |
| I8 | `sbat/archive/Meja-Keputusan-CAIR-Bariah.md5-8cce12c60255c6b009b0b791da22636b.html` | 60,095 | md5 pinned in filename | archived lineage |
| I9 | `taxonomy/interaction-patterns-v0.md` | — | *(in-repo)* | LOCKED pattern families + POP UP guardrail |
| I10 | `taxonomy/INTERACTION_ID_RECONCILIATION.md` | — | *(in-repo)* | frozen namespace rule; live `P0/P6/P11` |
| I11 | `lexicon/ALIAS-GLOSSARY-v0.md` | — | *(in-repo)* | 3 APPROVED aliases, exact-match rule |
| I12 | `decisions/SBAT-ADR-004.md` | — | *(in-repo)* | topik key + K5 lock |
| I13 | Phase B1 set (6 docs) | — | `reviews/phase-b1/` | measurements; addendum controlling |
| I14 | Stage 0A set (3 docs) | — | `reviews/stage-0a/` | provisional register + status addendum |

**I2 authenticates I3–I6.** All 14 independently checkable claims in `TREATMENT_PROBE_VALIDATION.md`
were re-measured against probe v0.1 and matched (notes hashes, token counts, punctuation, bounding
boxes, tick coordinates, layout names).

---

## 2. Inputs NOT held — the sample's real boundary

| # | Missing artifact | Consequence for the sample |
|---:|---|---|
| M1 | `SB_K5PL06T03B02_TIER1_STORYBOARD_SPEC_v1_2_CANDIDATE.pptx` (`d523f467…`) | **15 of 19 screens have no measured source.** The authoritative 19-slide deck is absent. |
| M2 | `packet_B02.json` | No per-screen bindings, no display/VO text for unmeasured screens |
| M3 | `asset_manifest.json` | No image bindings, no region/coordinate data → **Hotspot gate not constructible** |
| M4 | Source nodes | Source-label normalisation cannot be adjudicated at source |
| M5 | probe v0.2 (`75f8b168…`) | Base-revision proof rests on measured v0.1 + documented v0.2 (§2 of the addendum) |
| M6 | `SB_K4PL3T2_v1.2.pptx` (`16521234…0287cf2`) | Canonical archetype set unavailable except via probe clones |
| M7 | Rendering environment | **No revision of either deck has ever been seen rendered** — `LOCAL_REVIEW_CHECKLIST.md` records that LibreOffice cannot load them in the build sandbox |

---

## 3. Measurement coverage — 4 of 19 screens

Screen inventory recovered from probe v0.1 `docProps/app.xml`, which `python-pptx` did not rewrite and
which still carries the source specification's 19-title vector (`<Slides>19</Slides>`).

| Screen | Title | Measured? | Source |
|---|---|---|---|
| S01 | `S01 TAJUK` | ✗ | — |
| S02 | `S02 DIALOG` | ✗ | — |
| S03 | `S03 OVERVIEW` | ✗ | — |
| **S04** | `S04 CR_BASE` | ✅ **direct** | probe `slide4.xml` + reviewed `slide1` (control, verified) |
| S05–S08 | `S05–S08 FULL` | ✗ | — |
| **S09** | `S09 TICK` | ✅ **direct** | probe `slide9.xml` + reviewed `slide5` (rebuilt) |
| S10 | `S10 CR_BASE` | ✗ | — |
| S11 | `S11 FULL` | ✗ | **deliberately omitted from the probe** |
| **S12** | `S12 FULL` | ✅ **direct** | probe `slide12.xml` + reviewed `slide4` (edited) |
| S13–S15 | `S13–S15 FULL` | ✗ | — |
| S16 | `S16 TICK` | ✗ | — |
| **S17** | `S17 RUMUSAN` | ✅ **direct** | probe `slide17.xml` + reviewed `slide7` (control, verified) |
| S18 | `S18 KUIZ` | ✗ | — |
| S19 | `S19 TAMAT` | ✗ | — |

**Coverage: 4/19 measured (21 %). 15/19 unmeasured (79 %).**

Structure recovered with confidence: **S04 CR_BASE binds 4 children (S05–S08) + S09 TICK;
S10 CR_BASE binds 5 children (S11–S15) + S16 TICK.** Cross-referenced against the S17 Rumusan
inventory — *struktur taman* = 4 items, *perabot taman* = 5 items — and against S12's title placeholder
reading `Perabot Taman` with body content `Papan Tanda`.

Derived child mapping — `PROVISIONAL_IDENTIFIER`, inference from two measured lists, not a packet read:

| Base | Children |
|---|---|
| S04 = Struktur Taman | S05 Struktur Persisir Air · S06 Struktur Teduhan · S07 Kemudahan Awam · S08 Water Feature |
| S10 = Perabot Taman | S11 Kerusi Taman · **S12 Papan Tanda** ✅ measured · S13 Tong Sampah · S14 Drinking Fountain · S15 BBQ pit |

S12 = Papan Tanda is **confirmed by measurement**, which anchors the ordering. The other four
assignments follow the S17 list order and are provisional.

---

## 4. What each input authorises

| Input | Authorises | Does **not** authorise |
|---|---|---|
| I2 probe v0.1 | source-bound text and canonical geometry for S04, S09, S12, S17 | anything about the other 15 screens |
| I1 reviewed deck | SME intent, five authored rules, worked Card/Hotspot examples | canonical geometry — it is a review artefact, not source |
| I4 mapping | screen ↔ canon-slide correspondence for the 4 probe screens | canon geometry for unmeasured archetypes |
| I7 `BARIAH_DATA` | ratified character bank; historical decision slots | any filled K5 decision — all 16 are empty |
| I9 patterns | LOCKED families, reveal variants, POP UP guardrail | new pattern minting |

---

## 5. Custody statement

Both PPTX packages were re-hashed after all analysis and are unchanged:
`ee4f5479…8bb9e7` and `24dcaa04…1d471c`. All reads were streaming or scratchpad extractions never
written back. The live CAIR decision desk was read only. No PPTX modified, no compiler patched, no
schema altered, no visual candidate created.
