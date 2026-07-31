# SOURCE_CUSTODY_AND_COVERAGE — K5 PL06 T3 B02, S01–S19

- **Status:** custody gate — **docs-only**. Run **before** construction.
- **Standing:** sample only — **NOT CAIR-ratified**. `K5_LIVE_RATIFICATION_LOCKED`
- **Rule enforced:** **no factual content may be constructed for a `MISSING_SOURCE` screen.**

---

## 0. Two findings that apply to every screen

**F1 — No B02 source image exists in any available artifact.** `MEASURED_FACT`

Both packages were enumerated. The complete media inventory is:

| Package | Media parts |
|---|---|
| Reviewed deck | `ppt/media/image1.svg` — 228 bytes, `id="Icons_Checkmark"`, one `<path>` |
| Probe v0.1 | `ppt/media/image3.svg` — the same checkmark |

**Two checkmark icons. Zero content images.** Every `Visual:` on every screen is a **text placeholder
describing an image that is not in the package**. What the probe supplies is a **source locator**
(`K5PL06T03-B02-IMG-01, ms 237` / `IMG-05, ms 243`), never an asset.

Consequently the *asset binding* column below reads `LOCATOR ONLY` at best and `NONE` otherwise — for
all 19 screens, including the four with verified text. **A screen can be `VERIFIED_SOURCE` for text and
still have no image.** `asset_manifest.json` (`M3`) is what closes this, and it is absent.

**F2 — The approved K5 module is not present.** `MEASURED_FACT`

No module PDF, no extracted B02 source nodes, no `packet_B02.json`, no screen-to-source binding table.
What stands in for them is probe v0.1, whose shapes `TREATMENT_PROBE_MAPPING.md` records as cloned
**verbatim** from `SB_K5PL06T03B02_TIER1_STORYBOARD_SPEC_v1_2_CANDIDATE.pptx` — and whose 14
independently checkable claims were re-measured and matched. Probe text is therefore **source-grade for
the four screens it covers**, and supplies nothing for the other fifteen.

---

## 1. Per-screen custody table

Legend — **construction status**:
`VERIFIED_SOURCE` = display **and** VO **and** locator present and measured ·
`PARTIAL_SOURCE` = some element verified (typically the screen's subject name), body content absent ·
`MISSING_SOURCE` = no source evidence of any kind.

| # | Screen | Source evidence present | Source node / page | Asset binding | Display source | VO source | Status |
|---|---|---|---|---|---|---|---|
| S01 | TAJUK | Course/topic title strings, verbatim in **all 4** probe notes headers | — | NONE | `PL06: Pengurusan Operasi Pembinaan Landskap` · `Topik 3 Bahagian 2: Komponen Landskap` | none | **`PARTIAL_SOURCE`** |
| S02 | DIALOG | none | — | NONE | none | none | **`MISSING_SOURCE`** |
| S03 | OVERVIEW | none | — | NONE | none | none | **`MISSING_SOURCE`** |
| **S04** | CR_BASE — Struktur Taman | probe `slide4.xml` + reviewed `slide1` (control, shape-tree verified) | **`K5PL06T03-B02-IMG-01`, ms 237** | LOCATOR ONLY | `Empat jenis struktur taman.` + 4 labels + instruction line | `notesSlide4`, **481 ch**, sha `bdd9084a6dda` | ✅ **`VERIFIED_SOURCE`** |
| S05 | FULL — Struktur Persisir Air | subject name only — measured on S04 label + S17 list | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| S06 | FULL — Struktur Teduhan | subject name only | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| S07 | FULL — Kemudahan Awam | subject name only | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| S08 | FULL — Water Feature | subject name only | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| **S09** | TICK — Struktur Taman | probe `slide9.xml` + reviewed `slide5` | inherits `IMG-01`, ms 237 | LOCATOR ONLY | `Visual: struktur taman — semua komponen bertanda selesai.` · `Semua 4 subtopik telah dilihat.` | `notesSlide6`, **0 ch — intentionally EMPTY** (tick convention), sha `e3b0c44298fc` | ✅ **`VERIFIED_SOURCE`** |
| S10 | CR_BASE — Perabot Taman | section title measured on S12's title placeholder; 5 item names measured on S17 | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| S11 | FULL — Kerusi Taman | subject name only; **deliberately omitted from the probe** | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| **S12** | FULL — Papan Tanda | probe `slide12.xml` + reviewed `slide4` | **`K5PL06T03-B02-IMG-05`, ms 243** | LOCATOR ONLY | 4 bullets, 346 ch, 50 words, 4 sentences | `notesSlide16`, **449 ch**, sha `ba0a525663eb` | ✅ **`VERIFIED_SOURCE`** |
| S13 | FULL — Tong Sampah | subject name only | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| S14 | FULL — Drinking Fountain | subject name only | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| S15 | FULL — BBQ pit | subject name only — **source form lowercase `p`, measured** | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| S16 | TICK — Perabot Taman | structure only (5 children → 5 tick states) | — | NONE | none | none | **`PARTIAL_SOURCE`** |
| **S17** | RUMUSAN | probe `slide17.xml` + reviewed `slide7` (control, shape-tree verified) | — | NONE | heading + 3 bullets, 496 ch | `notesSlide12`, **586 ch**, sha `9d2694129582` | ✅ **`VERIFIED_SOURCE`** |
| S18 | KUIZ | none — **no quiz items, no answer keys, no routing** | — | NONE | none | none | **`MISSING_SOURCE`** |
| S19 | TAMAT | none | — | NONE | none | none | **`MISSING_SOURCE`** |

---

## 2. Coverage summary

| Status | Screens | Count | % |
|---|---|---:|---:|
| ✅ `VERIFIED_SOURCE` | S04, S09, S12, S17 | **4** | 21 % |
| `PARTIAL_SOURCE` | S01, S05–S08, S10, S11, S13–S16 | **11** | 58 % |
| `MISSING_SOURCE` | S02, S03, S18, S19 | **4** | 21 % |

| Dimension | Coverage |
|---|---|
| Display text | 4 / 19 verified |
| VO text | 4 / 19 verified (one of which is verified-**empty** by convention) |
| Source locator | **2 / 19** — only S04 (`IMG-01`/237) and S12 (`IMG-05`/243) |
| **Actual image asset** | **0 / 19** |
| Quiz items and routing | **0** |
| Screen-to-source binding table | **0** — no packet |

---

## 3. What may and may not be constructed

### 3.1 `MISSING_SOURCE` — construction of factual content is **prohibited**

| Screen | Prohibited | Permitted |
|---|---|---|
| S02 DIALOG | any scenario, dialogue line, named character, or situation | structural frame + **role-neutral placeholders** (`A-13`); visibly marked provisional |
| S03 OVERVIEW | any learning-objective text, any reflection question | structural frame; may **visually introduce the narrator** (`A-09`) |
| S18 KUIZ | any question, option, answer key, feedback or routing rule | structural frame only; **no quiz content of any kind** |
| S19 TAMAT | any closing statement or next-step instruction | structural frame only |

**S18 is the sharpest case.** A quiz screen built without source would fabricate assessment content —
answer keys included. That is the one construction on this deck that could produce a factually wrong
artefact a reviewer might not catch. **No quiz content is constructed. Full stop.**

### 3.2 `PARTIAL_SOURCE` — subject names only

The subject name of each detail screen is verified — S05–S08 from S04's measured card labels, S11 and
S13–S15 from S17's measured furniture list. **Nothing else is.** No body content, no VO, no locator,
no asset.

**Permitted:** the verified subject name, the split-STATE frame, and a visible `SOURCE PENDING` marker
in the body region.
**Prohibited:** any descriptive sentence about the subject. There is no source for one, and a plausible
sentence is the most dangerous thing this sample could contain — `Papan Tanda` is the *only* furniture
item whose body text exists anywhere, and it exists because the probe cloned S12 specifically.

### 3.3 `VERIFIED_SOURCE` — build to source

S04, S09, S12, S17 may be built to their measured display and VO. **These four are exactly the
preflight scope.** That is not a coincidence — it is why the preflight is three screens (S09 excluded
only because its tick geometry adds a variable without adding a new archetype).

---

## 4. Blockers, and what each one unblocks

| Blocker | Unblocks |
|---|---|
| `M1` Tier-1 spec (`d523f467…`) | display + VO for 11 `PARTIAL_SOURCE` screens |
| `M2` `packet_B02.json` | screen-to-source binding; S02/S03/S18/S19 content; `K5-DR-011` and `K5-DR-031` scope |
| `M3` `asset_manifest.json` + the images | **all 19 asset bindings**; the Hotspot gate; `A-04`'s conditional |
| Approved K5 module / B02 source nodes | source-label adjudication (`P-03`, `P-05`, `P-06`, `P-07`) |
| Quiz source | S18 — nothing else will do |

**The 19-slide sample cannot be completed from what is held.** 4 screens can be built to source, 11 to
a frame plus a name, 4 not at all. Attempting all 19 today would mean fabricating content for 15 of
them — which is precisely the failure this custody gate exists to prevent.

---

## 5. Modification statement

Docs-only. No PPTX modified, no compiler patched, no schema altered, no canonical ID issued. K5 remains
locked; the live CAIR decision desk is untouched. Both evidence packages re-hashed unchanged:
`ee4f5479…8bb9e7`, `24dcaa04…1d471c`.
