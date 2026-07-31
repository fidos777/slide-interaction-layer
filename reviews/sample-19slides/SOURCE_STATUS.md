# SOURCE_STATUS — 19-slide visual treatment sample v0.1

```
VISUAL_TREATMENT_SAMPLE_ONLY
SOURCE_INCOMPLETE — 4 of 19 screens verified
NOT_CAIR_RATIFIED · NOT_PRODUCTION_AUTHORISED
```

**No claim of source completeness is made.** 15 of 19 screens lack verified source and are marked
`SOURCE PENDING` on the canvas. Nothing factual was invented for any of them.

---

## 1. Status per screen

| # | Screen | Status | Verified content used | `SOURCE PENDING` on canvas | Locator |
|---|---|---|---|---|---|
| S01 | TAJUK | `PARTIAL` | course + topic strings (probe notes header, all 4 slides) | ✅ | — |
| S02 | DIALOG | **`MISSING`** | none | ✅ | — |
| S03 | OVERVIEW | **`MISSING`** | narrator identity (`Hilmi`, ratified `LOCKED`) | ✅ | — |
| **S04** | CR_BASE Struktur Taman | ✅ `VERIFIED` | display, 4 labels, instruction, VO 474 ch | — | `IMG-01`, ms 237 |
| S05 | FULL Struktur Persisir Air | `PARTIAL` | label only | ✅ | pending |
| S06 | FULL Struktur Teduhan | `PARTIAL` | label only | ✅ | pending |
| S07 | FULL Kemudahan Awam | `PARTIAL` | label only | ✅ | pending |
| S08 | FULL Water Feature | `PARTIAL` | label only (italic) | ✅ | pending |
| **S09** | TICK Struktur Taman | ✅ `VERIFIED` | display; VO verified **empty** (tick convention) | — | inherits `IMG-01` |
| S10 | CR_BASE Perabot Taman | `PARTIAL` | 5 item names (from S17); section title (from S12) | ✅ | pending |
| S11 | FULL Kerusi Taman | `PARTIAL` | label only | ✅ | pending |
| **S12** | FULL Papan Tanda | ✅ `VERIFIED` | display 8 bullets, VO 443 ch | — | **`IMG-05`, ms 243** |
| S13 | FULL Tong Sampah | `PARTIAL` | label only | ✅ | pending |
| S14 | FULL Drinking Fountain | `PARTIAL` | label only (italic) | ✅ | pending |
| S15 | FULL BBQ pit | `PARTIAL` | label only (italic, lowercase `p`) | ✅ | pending |
| S16 | TICK Perabot Taman | `PARTIAL` | inherits S10 | ✅ | pending |
| **S17** | RUMUSAN | ✅ `VERIFIED` | display 4 bullets + heading, VO 622 ch | — | — |
| S18 | KUIZ | **`MISSING`** | none | ✅ | — |
| S19 | TAMAT | **`MISSING`** | none | ✅ | — |

**4 `VERIFIED` · 11 `PARTIAL` · 4 `MISSING`.**

## 2. What was deliberately not created

| Screen | Not created |
|---|---|
| S02 | any scenario, dialogue line or named character. The casting slot `(K5, PL06, s02)` is **empty**, and the current B02 cast is not provable — role-neutral `[PELATIH]` / `[PENYELIA]` placeholders only |
| S03 | any overview text or reflection question. The slot `(K5, PL06, s03)` is **empty** |
| S05–S08, S11, S13–S15 | any descriptive sentence about the subject. `Papan Tanda` is the only furniture item whose body text exists anywhere |
| S10, S16 | the instruction line — S04's wording is verified for S04 only, so the instruction zone is marked pending rather than copied |
| **S18** | **any question, option, answer key, feedback or routing rule.** No quiz source exists. Structural frame only |
| S19 | any closing statement or next-step instruction |
| all `PARTIAL`/`MISSING` | VO. Their notes read `[VO SOURCE PENDING …]`, never invented narration |

## 3. Universal gap — no image asset exists

The complete media inventory across both evidence packages is **two checkmark SVGs**. There is no B02
content image anywhere. Every `Visual:` is a text placeholder, locators exist for **2 of 19** screens
and assets for **0 of 19**. `asset_manifest.json` closes this and is absent.

The completion ticks on S09/S16 are drawn as **native geometry**, not the probe's SVG blip — that blip
carries no raster fallback and its rendering was already flagged unverified in the probe's own checklist.

## 4. Provisional screen assignments

`S12 = Papan Tanda` is confirmed by measurement. The other eight detail assignments are **inferred**:
S05–S08 from S04's measured label order, S11/S13–S15 from S17's measured furniture list order. Each
carries that caveat in its off-canvas note. The *names* are verified; their *screen numbers* are not.

## 5. What would close each gap

| Blocker | Closes |
|---|---|
| Tier-1 spec (`d523f467…`) | display + VO for the 11 `PARTIAL` screens |
| `packet_B02.json` | S02/S03/S18/S19 content; screen-to-source binding; provisional assignments |
| `asset_manifest.json` + images | all 19 asset bindings; the Hotspot gate; S10's conditional |
| Quiz source | S18 — nothing else will do |
