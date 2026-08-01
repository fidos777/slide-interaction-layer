# BARIAH_FEEDBACK_IMPLEMENTATION_MAP — K5 PL06 T03 B02 v0.4

```
BARIAH_FEEDBACK_ARTIFACTS_RECEIVED_AND_FROZEN
ALL_BARIAH_COMMENTS_ACCOUNTED = true
UNCLASSIFIED_BARIAH_COMMENTS = 0
SILENTLY_REJECTED_COMMENTS = 0
NO_COMMENT_FABRICATED
DOCS_ONLY · GENERATOR_UNTOUCHED · NO_POWERPOINT_REGENERATED
```

> Supersedes the `BARIAH_FEEDBACK_ARTIFACT_NOT_RECEIVED` verdict recorded in
> `B02_FEEDBACK_DELTA_PROTOCOL_v0_4.md` §1 and `B02_V0_4_INPUT_FREEZE.md` §5. That blocker was an
> **execution-environment artifact-handoff gap**, not an absence of stakeholder feedback. Bariah's
> feedback existed; this session could not see it until the four artifacts were attached directly.
>
> This document is the v0.4 delta. `BARIAH_FEEDBACK_IMPLEMENTATION_MAP.md` (unversioned) remains the
> v0.3-era file and is **not** amended or replaced by this one.

---

# 1. Authoritative source artifacts

| Ref | Artifact | Authority class | Frozen at |
|---|---|---|---|
| **A1** | `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx` | **primary — slide-level evidence** | `reviews/storyboard-bariah/v0_3_bariah_review/` |
| **A2** | `Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx` | **primary — decision evidence** | `reviews/storyboard-bariah/v0_3_bariah_review/` |
| **A3** | `K5_PL06_T03_B02_UPDATED_SG_v0.3.docx` | **consolidated executable S&G** | `reviews/storyboard-bariah/v0_3_bariah_review/` |
| **A4** | `BARIAH_CORRECTION_EXEMPLARS_v0.4.md` | **derived navigation index — not authoritative** | `reviews/storyboard-bariah/v0_3_bariah_review/` |

Byte-level identity, sizes and SHA-256 digests: `B02_V0_4_INPUT_FREEZE.md` §2.

**A4 was used only to locate corrected exemplars efficiently.** Every conclusion below was re-verified
directly against A1 (slide text and Notes text) or A2 (per-item decision cells). Where A4 and the
primary artifacts disagree, the primary artifact wins — see BFB-12, where A4 reproduces a double-space
typographic artifact that must not enter a clean build.

## 1.1 How the annotated deck encodes feedback

A1 contains **75 slides, 75 notes parts and zero PowerPoint comment parts.** Bariah's annotations are
**on-slide text**, in two forms:

| Form | Count | Meaning |
|---|---:|---|
| `Changes made. Refer next slide.` | 12 | the slide is the v0.3 original; the **following** slide is Bariah's corrected exemplar |
| inline directive text | 7 | a written instruction on slides 8, 10, 12, 14, 20, 43, 75 |

Every one of those 19 markers is classified below. The `n → n+1` locators (e.g. *slide 13 → 14*)
name the original and its corrected exemplar.

---

# 2. Disposition summary

| Disposition | Count | Meaning |
|---|---:|---|
| `CONFIRMED_IMPLEMENT` | 16 | ruling is unambiguous; build it in v0.4 |
| `CONFIRMED_PROPAGATE` | 8 | ruling is unambiguous and Bariah explicitly extended it beyond the exemplar |
| `APPROVED_NO_CONTENT_CHANGE` | 2 | Bariah passed the v0.3 behaviour; nothing to change |
| `PENDING_SOURCE_VERIFICATION` | 1 | ruling is clear but rests on a factual claim not yet traced to source |
| `PENDING_FIRDAUS_CONFIRMATION` | 1 | Bariah explicitly routed the decision to Firdaus |
| `PENDING_CHARACTER_NAME` | 2 | policy confirmed; the concrete names were not supplied |
| `SUPERSEDED_V0_3_BEHAVIOUR` | 1 | a v0.3 architectural assumption is retired, with no direct replacement string |
| **Total** | **31** | |

No other disposition value is used. **No comment was rejected and none was omitted** — the four
non-`CONFIRMED_*` items are held open with a named dependency, not discarded.

---

# 3. Feedback index

| ID | Source | Locator | Affected | Disposition |
|---|---|---|---|---|
| `BFB-01` | annotated PPTX | slide 1 → 2 (EX-01, RP-001/S01) | `S01` | `CONFIRMED_IMPLEMENT` |
| `BFB-02` | annotated PPTX | slide 3 → 4 (EX-02, RP-002/S02) | `S02` | `CONFIRMED_IMPLEMENT` |
| `BFB-03` | annotated PPTX | slide 4 Notes (EX-02) | `S02` | `PENDING_SOURCE_VERIFICATION` |
| `BFB-04` | annotated PPTX | slide 4 Notes (EX-02) | `S02` | `PENDING_CHARACTER_NAME` |
| `BFB-05` | annotated PPTX | slide 5 → 6 (EX-03, RP-003/S03) | `S03` | `CONFIRMED_IMPLEMENT` |
| `BFB-06` | annotated PPTX | slide 7 → 8 (EX-04, RP-004) | `STRUKTUR_TAMAN_MASTER` | `CONFIRMED_IMPLEMENT` |
| `BFB-07` | annotated PPTX | slide 8 inline comment | `all group masters + all main screens` | `CONFIRMED_PROPAGATE` |
| `BFB-08` | annotated PPTX | slide 9 → 10 (EX-05, RP-005) | `STRUKTUR_PERSISIR_AIR_MAIN` | `CONFIRMED_IMPLEMENT` |
| `BFB-09` | annotated PPTX | slide 10 inline comment | `STRUKTUR_TEDUHAN, KEMUDAHAN_AWAM, WATER_FEATURE` | `CONFIRMED_PROPAGATE` |
| `BFB-10` | annotated PPTX | slide 11 → 12 (EX-06, RP-006) | `STRUKTUR_PERSISIR_AIR_EXAMPLES` | `CONFIRMED_IMPLEMENT` |
| `BFB-11` | annotated PPTX | slide 12 inline comment | `all 4 Family S components` | `CONFIRMED_PROPAGATE` |
| `BFB-12` | annotated PPTX | slide 13 → 14 (EX-07, RP-007) | `STRUKTUR_PERSISIR_AIR popups` | `CONFIRMED_IMPLEMENT` |
| `BFB-13` | annotated PPTX | slide 14 inline comment | `all Family S popups (16 source rows)` | `CONFIRMED_PROPAGATE` |
| `BFB-14` | annotated PPTX | slide 19 → 20 (EX-08, RP-012) | `STRUKTUR_PERSISIR_AIR all-viewed` | `CONFIRMED_IMPLEMENT` |
| `BFB-15` | annotated PPTX | slide 20 inline comment | `all equivalent completion states` | `CONFIRMED_PROPAGATE` |
| `BFB-16` | annotated PPTX + review guide | slide 42 → 43 (EX-09, RP-034), plus the slide 43 inline directive; guide items 1–4 | `PERABOT_TAMAN_MASTER + all 5 Perabot components` | `CONFIRMED_IMPLEMENT` |
| `BFB-17` | review guide | item 1 — Papan Tanda single item; "Keputusan dan catatan Bariah" | `PAPAN_TANDA` | `CONFIRMED_IMPLEMENT` |
| `BFB-18` | review guide | item 2 — BBQ Pit single item | `BBQ_PIT` | `CONFIRMED_IMPLEMENT` |
| `BFB-19` | review guide | item 1 — "Keputusan dan catatan Bariah" | `KERUSI_TAMAN, TONG_SAMPAH, DRINKING_FOUNTAIN` | `CONFIRMED_IMPLEMENT` |
| `BFB-20` | review guide | item 3 — popup density | `Family S popups` | `APPROVED_NO_CONTENT_CHANGE` |
| `BFB-21` | review guide | item 4 — learning flow | `Family S` | `APPROVED_NO_CONTENT_CHANGE` |
| `BFB-22` | annotated PPTX + review guide | slide 70 → 71 (EX-10, RP-061); guide item 5 | `RUMUSAN` | `CONFIRMED_IMPLEMENT` |
| `BFB-23` | review guide | item 5 — "Cadangan ayat Rumusan" cell | `all screens` | `CONFIRMED_PROPAGATE` |
| `BFB-24` | annotated PPTX + S&G v0.3 | slide 72 → 73 (EX-11, RP-062) | `KUIZ` | `CONFIRMED_IMPLEMENT` |
| `BFB-25` | annotated PPTX + review guide | slide 74 → 75 (EX-12, RP-063); guide item 7 | `TAMAT` | `CONFIRMED_IMPLEMENT` |
| `BFB-26` | annotated PPTX | slide 75 inline comment | `TAMAT` | `PENDING_FIRDAUS_CONFIRMATION` |
| `BFB-27` | review guide | item 6 — casting | `S02 (and any future named-cast screen)` | `PENDING_CHARACTER_NAME` |
| `BFB-28` | review guide + S&G v0.3 | item 8 — N-06 | `KERUSI_TAMAN row 3` | `CONFIRMED_IMPLEMENT` |
| `BFB-29` | annotated PPTX | slides 2,4,6,8,10,12,14,43,71,73,75 Notes (G-01) | `all content/VO screens` | `CONFIRMED_PROPAGATE` |
| `BFB-30` | S&G v0.3 | § close control | `all popups in all three families` | `CONFIRMED_PROPAGATE` |
| `BFB-31` | derived exemplars index | EX-09 "Superseded assumption" | `all nine components` | `SUPERSEDED_V0_3_BEHAVIOUR` |

---

# 4. Feedback records

Each record carries all sixteen required fields.

---

## BFB-01 — S01

| Field | Value |
|---|---|
| **feedback_id** | `BFB-01` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 1 → 2 (EX-01, RP-001/S01) |
| **original v0.3 behaviour** | Canvas: PL + topic only. VO: long "Selamat datang ke Pakej Latihan enam…". Notes: VO only. |
| **Bariah-required v0.4 behaviour** | Add course title KURSUS KERJA BANGUNAN – PEMBINAAN LANDSKAP LUAR. VO becomes "Klik butang MULA untuk memulakan pembelajaran." Notes open with course/PL/topic headers. |
| **affected component / frame screen** | `S01` |
| **propagation scope** | frame screen, 1 page |
| **content impact** | canvas title added; VO replaced |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | Notes header block added |
| **source-row impact** | none |
| **required generator change** | frame builder + notes grammar |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 2: canvas carries the course title; Notes begin with the three-line header then the short VO. |
| **unresolved dependency** | none |

---

## BFB-02 — S02

| Field | Value |
|---|---|
| **feedback_id** | `BFB-02` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 3 → 4 (EX-02, RP-002/S02) |
| **original v0.3 behaviour** | Heading "Pengenalan / Komponen Landskap". Dialogue in Notes without bracketed labels; learner asks from zero knowledge. |
| **Bariah-required v0.4 behaviour** | Heading becomes "Pengenalan". Dialogue rewritten so Pelatih demonstrates baseline knowledge and seeks scope confirmation. Bracketed labels [Pelatih] / [Penyelia Tapak]. |
| **affected component / frame screen** | `S02` |
| **propagation scope** | frame screen, 1 page |
| **content impact** | heading + dialogue rewritten |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | dialogue transcript rewritten; headers restored |
| **source-row impact** | none |
| **required generator change** | frame builder |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 4: heading "Pengenalan"; Notes carry [Pelatih]/[Penyelia Tapak] and the revised exchange. |
| **unresolved dependency** | none |

---

## BFB-03 — S02

| Field | Value |
|---|---|
| **feedback_id** | `BFB-03` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 4 Notes (EX-02) |
| **original v0.3 behaviour** | No MS2680 statement anywhere. |
| **Bariah-required v0.4 behaviour** | Dialogue asserts both groups must follow MS2680. |
| **affected component / frame screen** | `S02` |
| **propagation scope** | frame screen, 1 page |
| **content impact** | adds a factual claim |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | claim sits in the VO transcript |
| **source-row impact** | none |
| **required generator change** | frame builder — hold or flag until verified |
| **status** | **`PENDING_SOURCE_VERIFICATION`** |
| **evidence** | "Dan jangan lupa, kedua-duanya kena ikut MS2680." S&G v0.3: "PENDING SOURCE VERIFICATION … hold or flag the sentence rather than presenting it as final fact." |
| **unresolved dependency** | U-01 — source QA / Firdaus before final factual adoption |

---

## BFB-04 — S02

| Field | Value |
|---|---|
| **feedback_id** | `BFB-04` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 4 Notes (EX-02) |
| **original v0.3 behaviour** | Role-neutral PELATIH / PENYELIA TAPAK, no name token. |
| **Bariah-required v0.4 behaviour** | Character-name placeholder [Nama] inserted; do not invent a name. |
| **affected component / frame screen** | `S02` |
| **propagation scope** | frame screen, 1 page |
| **content impact** | placeholder token only |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | placeholder in transcript |
| **source-row impact** | none |
| **required generator change** | frame builder emits [Nama] until names supplied |
| **status** | **`PENDING_CHARACTER_NAME`** |
| **evidence** | "Encik [Nama], lepas kerja tanaman…" — placeholder retained rather than a name. |
| **unresolved dependency** | U-02 — actual names from Bariah / ID |

---

## BFB-05 — S03

| Field | Value |
|---|---|
| **feedback_id** | `BFB-05` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 5 → 6 (EX-03, RP-003/S03) |
| **original v0.3 behaviour** | Heading "Gambaran Keseluruhan". Reflection question phrased around choosing a material. |
| **Bariah-required v0.4 behaviour** | Heading becomes "Pengenalan". Reflection refined to "Jika anda ditugaskan memasang kerusi taman di tepi tasik, apakah jenis bahan yang anda akan pilih, dan mengapa?" VO connects explicitly to the previous page. Hilmi: stays on S03 only. |
| **affected component / frame screen** | `S03` |
| **propagation scope** | frame screen, 1 page |
| **content impact** | heading + reflection reworded |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | headers restored; VO rewritten |
| **source-row impact** | none |
| **required generator change** | frame builder |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 6: heading and reflection wording as stated; Mind Map direction and Hilmi retained. |
| **unresolved dependency** | none |

---

## BFB-06 — STRUKTUR_TAMAN_MASTER

| Field | Value |
|---|---|
| **feedback_id** | `BFB-06` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 7 → 8 (EX-04, RP-004) |
| **original v0.3 behaviour** | Group master carried a custom learner-canvas Seterusnya button. |
| **Bariah-required v0.4 behaviour** | Remove the custom Seterusnya. Retain four cards and the instruction. Notes carry group context + overview VO + interaction instruction. |
| **affected component / frame screen** | `STRUKTUR_TAMAN_MASTER` |
| **propagation scope** | group master |
| **content impact** | canvas control removed |
| **screen/state impact** | completion gating moves to the shell |
| **navigation impact** | player_next_enabled = group_complete[STRUKTUR_TAMAN] |
| **Notes impact** | headers + group context added |
| **source-row impact** | none |
| **required generator change** | group-master builder; off-canvas metadata must say shell navigation |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 8: no Seterusnya on canvas; Notes carry the header block and group context. |
| **unresolved dependency** | none |

---

## BFB-07 — all group masters + all main screens

| Field | Value |
|---|---|
| **feedback_id** | `BFB-07` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 8 inline comment |
| **original v0.3 behaviour** | Custom Seterusnya on learner canvas. |
| **Bariah-required v0.4 behaviour** | "Tidak perlu letak butang Seterusnya, kerana ia ialah butang di navigasi" — the next control belongs to the shell. |
| **affected component / frame screen** | `all group masters + all main screens` |
| **propagation scope** | global navigation rule |
| **content impact** | none |
| **screen/state impact** | gating semantics preserved on the shell control |
| **navigation impact** | removes every duplicate canvas Seterusnya |
| **Notes impact** | off-canvas wording must stop saying "Satu butang Seterusnya" |
| **source-row impact** | none |
| **required generator change** | button emitter + production-panel text |
| **status** | **`CONFIRMED_PROPAGATE`** |
| **evidence** | Bariah verbatim, slide 8. |
| **unresolved dependency** | none |

---

## BFB-08 — STRUKTUR_PERSISIR_AIR_MAIN

| Field | Value |
|---|---|
| **feedback_id** | `BFB-08` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 9 → 10 (EX-05, RP-005) |
| **original v0.3 behaviour** | Main explanation as one bullet block with a canvas Seterusnya. |
| **Bariah-required v0.4 behaviour** | Remove canvas Seterusnya. Split content into an explanation block and an Aspek Pembinaan block where the source has one. Preserve full source-bound VO and the transition sentence. |
| **affected component / frame screen** | `STRUKTUR_PERSISIR_AIR_MAIN` |
| **propagation scope** | main explanation template |
| **content impact** | content split into two blocks |
| **screen/state impact** | none |
| **navigation impact** | shell next |
| **Notes impact** | headers + group context added |
| **source-row impact** | none |
| **required generator change** | main-screen builder |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 10. |
| **unresolved dependency** | none |

---

## BFB-09 — STRUKTUR_TEDUHAN, KEMUDAHAN_AWAM, WATER_FEATURE

| Field | Value |
|---|---|
| **feedback_id** | `BFB-09` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 10 inline comment |
| **original v0.3 behaviour** | Template applied to one component only. |
| **Bariah-required v0.4 behaviour** | "Apply changes to other struktur taman." — propagate the main-explanation template. |
| **affected component / frame screen** | `STRUKTUR_TEDUHAN, KEMUDAHAN_AWAM, WATER_FEATURE` |
| **propagation scope** | Family S main screens ×3 (×4 incl. exemplar) |
| **content impact** | same split where source supports it |
| **screen/state impact** | none |
| **navigation impact** | shell next |
| **Notes impact** | headers + group context |
| **source-row impact** | none |
| **required generator change** | main-screen builder applies to all Family S |
| **status** | **`CONFIRMED_PROPAGATE`** |
| **evidence** | Bariah verbatim, slide 10. Do not invent an Aspek Pembinaan section where the module has none — Struktur Teduhan has no such block. |
| **unresolved dependency** | Struktur Teduhan has no Aspek Pembinaan block in source |

---

## BFB-10 — STRUKTUR_PERSISIR_AIR_EXAMPLES

| Field | Value |
|---|---|
| **feedback_id** | `BFB-10` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 11 → 12 (EX-06, RP-006) |
| **original v0.3 behaviour** | Instruction read "Klik pada setiap item untuk penjelasan lanjut." |
| **Bariah-required v0.4 behaviour** | Instruction becomes "Klik pada setiap contoh untuk penjelasan lanjut." Notes carry group context, screen context and the interaction instruction. |
| **affected component / frame screen** | `STRUKTUR_PERSISIR_AIR_EXAMPLES` |
| **propagation scope** | example-selection template |
| **content impact** | instruction reworded |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | headers + two context lines |
| **source-row impact** | none |
| **required generator change** | example-screen builder |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 12. |
| **unresolved dependency** | none |

---

## BFB-11 — all 4 Family S components

| Field | Value |
|---|---|
| **feedback_id** | `BFB-11` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 12 inline comment |
| **original v0.3 behaviour** | Applied to one component. |
| **Bariah-required v0.4 behaviour** | "Apply changes to other struktur taman." — propagate to all Family S example screens. |
| **affected component / frame screen** | `all 4 Family S components` |
| **propagation scope** | Family S example screens ×4 |
| **content impact** | instruction wording |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | context headers |
| **source-row impact** | none |
| **required generator change** | example-screen builder |
| **status** | **`CONFIRMED_PROPAGATE`** |
| **evidence** | Bariah verbatim, slide 12. |
| **unresolved dependency** | none |

---

## BFB-12 — STRUKTUR_PERSISIR_AIR popups

| Field | Value |
|---|---|
| **feedback_id** | `BFB-12` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 13 → 14 (EX-07, RP-007) |
| **original v0.3 behaviour** | Popup used ALL-CAPS field labels and a text Tutup button; no visual direction when source had no figure. |
| **Bariah-required v0.4 behaviour** | Title-style labels "Fungsi dan Penerangan" / "Contoh". Replace text Tutup with a close icon. Add a visual direction tied to the selected example even where the source has no dedicated figure. |
| **affected component / frame screen** | `STRUKTUR_PERSISIR_AIR popups` |
| **propagation scope** | popup template |
| **content impact** | label case; visual direction added |
| **screen/state impact** | popup remains a state |
| **navigation impact** | close control becomes an icon |
| **Notes impact** | headers + group and example context |
| **source-row impact** | none |
| **required generator change** | popup emitter + close-control asset |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 14. The close icon is a real embedded image: ppt/media/image1.png is referenced by slide 14 alone. Exemplar shows "Fungsi Dan  Penerangan" with a double space — clean build must use "Fungsi dan Penerangan". |
| **unresolved dependency** | none |

---

## BFB-13 — all Family S popups (16 source rows)

| Field | Value |
|---|---|
| **feedback_id** | `BFB-13` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 14 inline comment |
| **original v0.3 behaviour** | Applied to one popup. |
| **Bariah-required v0.4 behaviour** | "Apply changes to other contoh struktur pop ups." — propagate to every Family S popup. |
| **affected component / frame screen** | `all Family S popups (16 source rows)` |
| **propagation scope** | Family S popups |
| **content impact** | label case + visual direction |
| **screen/state impact** | none |
| **navigation impact** | close icon everywhere |
| **Notes impact** | context headers |
| **source-row impact** | none |
| **required generator change** | popup emitter |
| **status** | **`CONFIRMED_PROPAGATE`** |
| **evidence** | Bariah verbatim, slide 14. |
| **unresolved dependency** | none |

---

## BFB-14 — STRUKTUR_PERSISIR_AIR all-viewed

| Field | Value |
|---|---|
| **feedback_id** | `BFB-14` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 19 → 20 (EX-08, RP-012) |
| **original v0.3 behaviour** | All-viewed state used the old "item" instruction wording. |
| **Bariah-required v0.4 behaviour** | Use "Klik pada setiap contoh…" consistently. Preserve ticks and enabled Kembali. Notes stay genuinely empty. |
| **affected component / frame screen** | `STRUKTUR_PERSISIR_AIR all-viewed` |
| **propagation scope** | completion-state template |
| **content impact** | instruction wording |
| **screen/state impact** | state preserved |
| **navigation impact** | none |
| **Notes impact** | Notes remain empty — no headers on silent states |
| **source-row impact** | none |
| **required generator change** | completion-state builder |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 20. |
| **unresolved dependency** | none |

---

## BFB-15 — all equivalent completion states

| Field | Value |
|---|---|
| **feedback_id** | `BFB-15` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 20 inline comment |
| **original v0.3 behaviour** | Applied to one state. |
| **Bariah-required v0.4 behaviour** | "Apply changes to others, where applicable." — terminology and visual-state treatment propagate; do NOT add Notes headers to silent states. |
| **affected component / frame screen** | `all equivalent completion states` |
| **propagation scope** | completion states |
| **content impact** | instruction wording |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | silent states stay empty |
| **source-row impact** | none |
| **required generator change** | completion-state builder |
| **status** | **`CONFIRMED_PROPAGATE`** |
| **evidence** | Bariah verbatim, slide 20. The "where applicable" qualifier is what keeps the Notes-header rule off silent states. |
| **unresolved dependency** | none |

---

## BFB-16 — PERABOT_TAMAN_MASTER + all 5 Perabot components

| Field | Value |
|---|---|
| **feedback_id** | `BFB-16` |
| **source artifact** | A1 + A2 |
| **locator** | slide 42 → 43 (EX-09, RP-034), plus the slide 43 inline directive; guide items 1–4 |
| **original v0.3 behaviour** | Perabot Taman was a clickable five-card group master with group completion, then the same Main → Contoh → popup pattern as Struktur Taman. |
| **Bariah-required v0.4 behaviour** | Perabot gateway becomes overview + list only, not a clickable interaction level; entry via shell navigation. Perabot splits into Family P1 and Family P2. |
| **affected component / frame screen** | `PERABOT_TAMAN_MASTER + all 5 Perabot components` |
| **propagation scope** | major architecture change — whole Perabot group |
| **content impact** | gateway becomes non-interactive list |
| **screen/state impact** | new families replace the single pattern |
| **navigation impact** | entry through shell navigation |
| **Notes impact** | Notes end "Mari lihat setiap contoh perabot di halaman seterusnya." |
| **source-row impact** | none — 26 rows unchanged |
| **required generator change** | model + generator: two new Perabot families |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Slide 43: "New structure. Refer doc Panduan_Semakan_Bariah…". Guide: "Perabot Taman – penerangan + list contoh (tiada klik/level)." |
| **unresolved dependency** | none |

---

## BFB-17 — PAPAN_TANDA

| Field | Value |
|---|---|
| **feedback_id** | `BFB-17` |
| **source artifact** | A2 — Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx |
| **locator** | item 1 — Papan Tanda single item; "Keputusan dan catatan Bariah" |
| **original v0.3 behaviour** | Papan Tanda: Main → Contoh Papan Tanda → 1 clickable item → popup → Kembali. |
| **Bariah-required v0.4 behaviour** | Papan Tanda: component explanation + specification-category list → click category (Level 1) → popup → close icon. Categories: Bahan Panel, Bahan Struktur Tiang, Grafik, Rekaan. No generic one-item Contoh screen. |
| **affected component / frame screen** | `PAPAN_TANDA` |
| **propagation scope** | Family P2 |
| **content impact** | 1 source row yields 4 interaction categories |
| **screen/state impact** | Contoh screen removed; category list added |
| **navigation impact** | close icon returns to the specification list |
| **Notes impact** | context headers |
| **source-row impact** | NONE — still 1 source row |
| **required generator change** | model + generator: Family P2 |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Guide verbatim: "Papan Tanda – penerangan + list spesifikasi: Bahan Panel / Bahan Struktur Tiang / Grafik / Rekaan (klik spesifikasi - level 1, pop up, butang tutup guna ikon)". |
| **unresolved dependency** | none |

---

## BFB-18 — BBQ_PIT

| Field | Value |
|---|---|
| **feedback_id** | `BFB-18` |
| **source artifact** | A2 — Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx |
| **locator** | item 2 — BBQ Pit single item |
| **original v0.3 behaviour** | BBQ Pit: Main → Contoh BBQ Pit → 1 clickable item → popup → Kembali. |
| **Bariah-required v0.4 behaviour** | "Refer comment [1]" → BBQ Pit follows the Papan Tanda structure: explanation + specification-category list → popup → close icon. |
| **affected component / frame screen** | `BBQ_PIT` |
| **propagation scope** | Family P2 |
| **content impact** | 1 source row yields several specification categories |
| **screen/state impact** | Contoh screen removed; category list added |
| **navigation impact** | close icon returns to the specification list |
| **Notes impact** | context headers |
| **source-row impact** | NONE — still 1 source row |
| **required generator change** | model + generator: Family P2 |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Guide item 2 answer cell: "Refer comment [1]". Guide comment 1: "BBQ Pit – sama struktur dengan Papan Tanda." |
| **unresolved dependency** | U-04 — BBQ Pit category labels must be derived from source-attested substructure, then confirmed if wording is interpretive |

---

## BFB-19 — KERUSI_TAMAN, TONG_SAMPAH, DRINKING_FOUNTAIN

| Field | Value |
|---|---|
| **feedback_id** | `BFB-19` |
| **source artifact** | A2 — Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx |
| **locator** | item 1 — "Keputusan dan catatan Bariah" |
| **original v0.3 behaviour** | Kerusi Taman / Tong Sampah / Drinking Fountain used Main → Contoh → popup → Kembali. |
| **Bariah-required v0.4 behaviour** | Family P1: component explanation + example list → click example (Level 1) → full-slide example with Kembali → click specification (Level 2) → popup → close icon. |
| **affected component / frame screen** | `KERUSI_TAMAN, TONG_SAMPAH, DRINKING_FOUNTAIN` |
| **propagation scope** | Family P1 ×3 |
| **content impact** | each example gains a full-slide detail plus specification items |
| **screen/state impact** | adds a full-slide example level and a specification level |
| **navigation impact** | Kembali returns to the component explanation/list; close icon returns to the example detail |
| **Notes impact** | context headers |
| **source-row impact** | NONE — 8 source rows across the three components unchanged |
| **required generator change** | model + generator: Family P1 |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Guide verbatim: "Kerusi Taman – penerangan + list contoh … (klik contoh - level 1, full slide, Kembali) / … list spesifikasi (klik spesifikasi - level 2, pop up, butang tutup guna ikon) / Tong Sampah, Drinking Fountain – sama struktur dengan Kerusi Taman". |
| **unresolved dependency** | none |

---

## BFB-20 — Family S popups

| Field | Value |
|---|---|
| **feedback_id** | `BFB-20` |
| **source artifact** | A2 — Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx |
| **locator** | item 3 — popup density |
| **original v0.3 behaviour** | Uniform popup treatment across all nine components. |
| **Bariah-required v0.4 behaviour** | Struktur Persisir Air density approved. Perabot popups follow the new structure. |
| **affected component / frame screen** | `Family S popups` |
| **propagation scope** | Family S |
| **content impact** | no change to Struktur popup density |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | none |
| **source-row impact** | none |
| **required generator change** | none |
| **status** | **`APPROVED_NO_CONTENT_CHANGE`** |
| **evidence** | Guide: "Struktur Persisir Air – Lulus / Perabot Taman – new structure. Refer comment [1]". |
| **unresolved dependency** | none |

---

## BFB-21 — Family S

| Field | Value |
|---|---|
| **feedback_id** | `BFB-21` |
| **source artifact** | A2 — Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx |
| **locator** | item 4 — learning flow |
| **original v0.3 behaviour** | One flow for all nine components. |
| **Bariah-required v0.4 behaviour** | Struktur Taman flow approved unchanged. Perabot flow amended per comment [1]. |
| **affected component / frame screen** | `Family S` |
| **propagation scope** | Family S — 4 components |
| **content impact** | none |
| **screen/state impact** | Struktur flow retained as built |
| **navigation impact** | none |
| **Notes impact** | none |
| **source-row impact** | none |
| **required generator change** | none for Family S |
| **status** | **`APPROVED_NO_CONTENT_CHANGE`** |
| **evidence** | Guide: "Struktur Taman – Lulus / Perabot Taman – Pinda – refer comment [1]". |
| **unresolved dependency** | none |

---

## BFB-22 — RUMUSAN

| Field | Value |
|---|---|
| **feedback_id** | `BFB-22` |
| **source artifact** | A1 + A2 |
| **locator** | slide 70 → 71 (EX-10, RP-061); guide item 5 |
| **original v0.3 behaviour** | Rumusan VO opened with the label "Komponen Landskap — Struktur Taman dan Perabot Taman." |
| **Bariah-required v0.4 behaviour** | Wording LULUS. Canvas retained. Remove the redundant VO opening label from the narrated paragraph. Notes add "Rumusan" context heading. |
| **affected component / frame screen** | `RUMUSAN` |
| **propagation scope** | frame screen, 1 page |
| **content impact** | canvas unchanged; VO opening label removed |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | headers + Rumusan context; VO trimmed |
| **source-row impact** | none |
| **required generator change** | frame builder |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Guide item 5: "✓ LULUS wording sesuai". Verified on slide 71: Notes VO starts at "Mengenal pasti…", not the label. |
| **unresolved dependency** | none |

---

## BFB-23 — all screens

| Field | Value |
|---|---|
| **feedback_id** | `BFB-23` |
| **source artifact** | A2 — Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx |
| **locator** | item 5 — "Cadangan ayat Rumusan" cell |
| **original v0.3 behaviour** | English-origin terms italicised only in a closed three-term lexicon on the canvas. |
| **Bariah-required v0.4 behaviour** | "GLOBAL di speaker notes untuk semua slide. English words in italic" — italicise approved English terms across learner canvas and Speaker Notes. |
| **affected component / frame screen** | `all screens` |
| **propagation scope** | global styling rule |
| **content impact** | italic styling across content |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | italics applied in Notes too |
| **source-row impact** | none |
| **required generator change** | run emitter + notes emitter |
| **status** | **`CONFIRMED_PROPAGATE`** |
| **evidence** | Guide verbatim. S&G v0.3: "Approved English-origin terms MUST be italicised consistently on the learner canvas and in Speaker Notes." |
| **unresolved dependency** | none |

---

## BFB-24 — KUIZ

| Field | Value |
|---|---|
| **feedback_id** | `BFB-24` |
| **source artifact** | A1 + A3 |
| **locator** | slide 72 → 73 (EX-11, RP-062) |
| **original v0.3 behaviour** | Quiz listed 5 stems with long "Maklum balas betul:/salah:" rationale as immediate feedback. |
| **Bariah-required v0.4 behaviour** | Add knowledge-check-only statement, learner instruction and a MULA KUIZ control before Q1. Concise immediate feedback per item. Result state with score and Lulus/Tidak Lulus. Semak Jawapan and Ulang Kuiz retained. Multiple Response shows option text with no A/B/C labels. Add subsection locators to source references. |
| **affected component / frame screen** | `KUIZ` |
| **propagation scope** | frame screen, 1 page |
| **content impact** | substantial rewrite of quiz presentation |
| **screen/state impact** | adds MULA KUIZ and a result state |
| **navigation impact** | entry control added |
| **Notes impact** | headers restored; long rationale removed from immediate feedback |
| **source-row impact** | none |
| **required generator change** | quiz builder |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 73: MULA KUIZ instruction present; knowledge-check statement present; Soalan 5 options carry no A/B/C labels; old rationale lines removed (Notes 3006 → 1581 chars). S&G v0.3 authorises "concise immediate feedback". |
| **unresolved dependency** | U-05 — detailed rationale placement under Semak Jawapan |

---

## BFB-25 — TAMAT

| Field | Value |
|---|---|
| **feedback_id** | `BFB-25` |
| **source artifact** | A1 + A2 |
| **locator** | slide 74 → 75 (EX-12, RP-063); guide item 7 |
| **original v0.3 behaviour** | Tamat: two closing lines, enabled Seterusnya, routing held in metadata. |
| **Bariah-required v0.4 behaviour** | Heading "Tamat Topik 3 Bahagian 2: Komponen Landskap" with course and PL hierarchy on canvas. Concise VO. Logical next destination = next Bahagian in Topik 3. |
| **affected component / frame screen** | `TAMAT` |
| **propagation scope** | frame screen, 1 page |
| **content impact** | heading and hierarchy rewritten |
| **screen/state impact** | none |
| **navigation impact** | logical next = next Bahagian in Topik 3 |
| **Notes impact** | headers restored; concise VO |
| **source-row impact** | none |
| **required generator change** | frame builder |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Verified on slide 75. Guide item 7: "✓ A. Bahagian seterusnya dalam Topik 3." Wording: "Refer storyboard". |
| **unresolved dependency** | none |

---

## BFB-26 — TAMAT

| Field | Value |
|---|---|
| **feedback_id** | `BFB-26` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slide 75 inline comment |
| **original v0.3 behaviour** | Shell Seterusnya enabled on Tamat; exit behaviour unspecified. |
| **Bariah-required v0.4 behaviour** | "Butang Seterusnya di shell navigation DISABLED. Di LMS, learners perlu TUTUP lesson dengan tutup window. Firdaus, please confirm." |
| **affected component / frame screen** | `TAMAT` |
| **propagation scope** | frame screen + LMS integration |
| **content impact** | none |
| **screen/state impact** | shell control disabled on this screen |
| **navigation impact** | physical exit = close the lesson window |
| **Notes impact** | none |
| **source-row impact** | none |
| **required generator change** | shell-control state on TAMAT |
| **status** | **`PENDING_FIRDAUS_CONFIRMATION`** |
| **evidence** | Bariah verbatim, slide 75 — explicitly addressed to Firdaus. |
| **unresolved dependency** | U-03 — when completion is reported, where the LMS returns, whether the next Bahagian launches manually or automatically |

---

## BFB-27 — S02 (and any future named-cast screen)

| Field | Value |
|---|---|
| **feedback_id** | `BFB-27` |
| **source artifact** | A2 — Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx |
| **locator** | item 6 — casting |
| **original v0.3 behaviour** | Role-neutral PELATIH / PENYELIA TAPAK. |
| **Bariah-required v0.4 behaviour** | "Gunakan nama watak untuk keseluruhan PL06. Gunakan nama watak yang sama bergantung kepada kesesuaian." — course-wide PL06 naming policy confirmed; actual names not supplied. |
| **affected component / frame screen** | `S02 (and any future named-cast screen)` |
| **propagation scope** | course-wide policy |
| **content impact** | names not yet insertable |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | [Nama] placeholder retained |
| **source-row impact** | none |
| **required generator change** | none until names supplied |
| **status** | **`PENDING_CHARACTER_NAME`** |
| **evidence** | Guide item 6 answer cell verbatim. No A/B/C box was ticked; the written answer is the decision. |
| **unresolved dependency** | U-02 |

---

## BFB-28 — KERUSI_TAMAN row 3

| Field | Value |
|---|---|
| **feedback_id** | `BFB-28` |
| **source artifact** | A2 + A3 |
| **locator** | item 8 — N-06 |
| **original v0.3 behaviour** | Source form "Kerusi KompositContoh: WPC - Wood-Plastic Composite / Plastik Kitar Semula):" left uncorrected; NORMALISATION_DECLINED. |
| **Bariah-required v0.4 behaviour** | "✓ B. Betulkan tanda kurungan sahaja." Normalise to: WPC (Wood-Plastic Composite / Plastik Kitar Semula). |
| **affected component / frame screen** | `KERUSI_TAMAN row 3` |
| **propagation scope** | one source row label |
| **content impact** | punctuation normalised; wording otherwise unchanged |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | none |
| **source-row impact** | label form only — row UID and count unchanged |
| **required generator change** | content data normalisation |
| **status** | **`CONFIRMED_IMPLEMENT`** |
| **evidence** | Guide item 8 verbatim: "Tukar kepada WPC (Wood-Plastic Composite / Plastik Kitar Semula)". S&G v0.3: "WPC punctuation is authorised as: WPC (Wood-Plastic Composite / Plastik Kitar Semula)." |
| **unresolved dependency** | none |

---

## BFB-29 — all content/VO screens

| Field | Value |
|---|---|
| **feedback_id** | `BFB-29` |
| **source artifact** | A1 — K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx |
| **locator** | slides 2,4,6,8,10,12,14,43,71,73,75 Notes (G-01) |
| **original v0.3 behaviour** | Notes carried exact VO/transcript only. |
| **Bariah-required v0.4 behaviour** | Content/VO slides: Notes open with course title where applicable, PL title, Topic/Bahagian title, blank line, screen/group context, then the exact VO. Silent completion states keep genuinely empty Notes. |
| **affected component / frame screen** | `all content/VO screens` |
| **propagation scope** | global Notes grammar |
| **content impact** | none |
| **screen/state impact** | none |
| **navigation impact** | none |
| **Notes impact** | Notes header block added everywhere except silent states |
| **source-row impact** | none |
| **required generator change** | notes emitter |
| **status** | **`CONFIRMED_PROPAGATE`** |
| **evidence** | Verified across every corrected exemplar. S&G v0.3: "Production-context headers + exact VO/transcript on content slides; silent completion states remain empty." |
| **unresolved dependency** | none |

---

## BFB-30 — all popups in all three families

| Field | Value |
|---|---|
| **feedback_id** | `BFB-30` |
| **source artifact** | A3 — K5_PL06_T03_B02_UPDATED_SG_v0.3.docx |
| **locator** | § close control |
| **original v0.3 behaviour** | Popup close was a text button labelled Tutup. |
| **Bariah-required v0.4 behaviour** | Popup close control MUST be an icon. Do not display a text "Tutup" button. |
| **affected component / frame screen** | `all popups in all three families` |
| **propagation scope** | global control rule |
| **content impact** | none |
| **screen/state impact** | none |
| **navigation impact** | close control becomes an icon |
| **Notes impact** | none |
| **source-row impact** | none |
| **required generator change** | popup emitter + icon asset |
| **status** | **`CONFIRMED_PROPAGATE`** |
| **evidence** | S&G v0.3 verbatim. Corroborated by the real image part ppt/media/image1.png referenced only by slide 14. |
| **unresolved dependency** | none |

---

## BFB-31 — all nine components

| Field | Value |
|---|---|
| **feedback_id** | `BFB-31` |
| **source artifact** | A4 — BARIAH_CORRECTION_EXEMPLARS_v0.4.md (derived; every claim re-verified against A1/A2) |
| **locator** | EX-09 "Superseded assumption" |
| **original v0.3 behaviour** | A single global interaction pattern was applied to all nine components. |
| **Bariah-required v0.4 behaviour** | Superseded: Struktur Taman and Perabot Taman now use different interaction families. |
| **affected component / frame screen** | `all nine components` |
| **propagation scope** | architecture-level supersession |
| **content impact** | none |
| **screen/state impact** | one pattern → three families |
| **navigation impact** | family-specific returns |
| **Notes impact** | none |
| **source-row impact** | none |
| **required generator change** | model restructure |
| **status** | **`SUPERSEDED_V0_3_BEHAVIOUR`** |
| **evidence** | Corroborated by the review guide and S&G v0.3, both of which split Perabot into P1 and P2. |
| **unresolved dependency** | none |

---

# 5. Unresolved dependency register

Five dependencies are open. None of them blocks the v0.4 delta itself; each blocks a specific
downstream string or state.

| Dep | Raised by | Question | Owner | Blocks |
|---|---|---|---|---|
| **U-01** | BFB-03 | Is the MS2680 applicability claim attested by the module source? | source QA / Firdaus | one VO sentence on S02 |
| **U-02** | BFB-04, BFB-27 | What are the PL06 character names? | Bariah / instructional design | the `[Nama]` placeholder on S02 |
| **U-03** | BFB-26 | LMS exit: when is completion reported, where does the LMS return, does the next Bahagian launch manually or automatically? | **Firdaus** | shell-control state on TAMAT |
| **U-04** | BFB-18 | BBQ Pit specification-category labels — derivable from source, or interpretive? | source QA, then Bariah if interpretive | Family P2 category list for BBQ Pit |
| **U-05** | BFB-24 | Where does the detailed answer rationale live once immediate feedback is concise — under `Semak Jawapan`? | Bariah | quiz result-state content |

**U-04 is the one to watch.** Bariah ruled that BBQ Pit takes the Papan Tanda structure, but unlike
Papan Tanda — whose four categories (`Bahan Panel`, `Bahan Struktur Tiang`, `Grafik`, `Rekaan`) are
named verbatim in A2 — BBQ Pit's categories are not enumerated anywhere in the feedback. They must be
derived from the module's own substructure for that row. Inventing them would be fabrication.

---

# 6. Invariants preserved by this delta

```
SOURCE_ROW_COUNT                             = 26      unchanged
SOURCE_ASSET_COUNT                           = 14      unchanged
SOURCE_ROW_COUNT_CHANGED_BY_INTERACTION_SPLIT = false
PROVISIONAL_ROW_IDS                          unchanged — none renamed or renumbered
NEW_CANONICAL_PATTERN_IDS_MINTED             = 0
```

Every architectural change in §4 is a change to **interaction items**, never to **source rows**. The
clearest case is BFB-17: Papan Tanda's single source row now yields four interaction categories, and
`K5-PL06-T03-B02-PAPAN-TANDA-ROW-01` keeps its identity and its count of one. Under the
`B02_FEEDBACK_DELTA_PROTOCOL_v0_4.md` §2.1 rule this is `CLASS-3`, not `CLASS-9`: it changes how many
items a row produces, not what the source says. See `B02_INTERACTION_FAMILY_TAXONOMY_v0_4.md` §7 for
the four-level identifier separation.

---

# 7. Validation totals

Every value below is asserted by a scoped check, not by a whole-document search. **39 of 39 checks
pass.**

```
ALL_BARIAH_COMMENTS_ACCOUNTED                  = true
UNCLASSIFIED_BARIAH_COMMENTS                   = 0
SILENTLY_REJECTED_COMMENTS                     = 0

SOURCE_ROW_COUNT                               = 26
SOURCE_ASSET_COUNT                             = 14
SOURCE_ROW_COUNT_CHANGED_BY_INTERACTION_SPLIT  = false

EXECUTION_FAMILIES                             = 3
UNKNOWN_COMPONENT_FAMILY                       = 0
STRUCTURE_COMPONENTS_IN_FAMILY_S               = 4
PERABOT_COMPONENTS_IN_FAMILY_P1                = 3
PERABOT_COMPONENTS_IN_FAMILY_P2                = 2

ANNOTATED_PPTX_HASH_RECORDED                   = true
COMPLETED_REVIEW_GUIDE_HASH_RECORDED           = true
UPDATED_SG_V0_3_HASH_RECORDED                  = true
CORRECTION_EXEMPLARS_HASH_RECORDED             = true

GENERATOR_FILES_CHANGED                        = 0
POWERPOINT_FILES_GENERATED                     = 0
COMPONENTS_PROPAGATED                          = 0
NEW_CANONICAL_PATTERN_IDS_MINTED               = 0
```

## 7.1 How each total is established

| Total | Method |
|---|---|
| `ALL_BARIAH_COMMENTS_ACCOUNTED` | the 12 `Changes made.` markers and 7 inline directives are enumerated from A1's slide text, and guide items 1–8 from A2; every one is required to appear in a record locator |
| `UNCLASSIFIED_BARIAH_COMMENTS` | every record must carry a disposition drawn from the seven permitted values |
| `SILENTLY_REJECTED_COMMENTS` | no disposition expresses rejection; the four non-`CONFIRMED_*` records each name an open dependency |
| `SOURCE_ROW_COUNT` / `SOURCE_ASSET_COUNT` | asserted independently in `DECISION_REGISTER_B02_v0.4.json` and `V0_3_TO_V0_4_CHANGESET.json`, and the changeset's nine per-component row counts are summed to 26 twice, from two different structures |
| family counts | derived by grouping the changeset's nine components by `new_interaction_family`, then cross-checked against the assignment table in `B02_INTERACTION_FAMILY_TAXONOMY_v0_4.md` §6.2 |
| the four hash totals | each file is re-hashed from disk and the digest must appear both in the freeze document and in the register's evidence block |
| `GENERATOR_FILES_CHANGED` | `git diff --name-only HEAD` plus untracked files, filtered to `/generator/` |
| `POWERPOINT_FILES_GENERATED` | same file list, filtered to `.pptx`/`.potx`, excluding the frozen evidence directory — A1 is a received artifact, not a generated one |
| `NEW_CANONICAL_PATTERN_IDS_MINTED` | every `P<n>` token in this map and the taxonomy must fall inside the existing `P0`–`P11` namespace |
| byte preservation | the four frozen artifacts are compared byte-for-byte against the supplied originals |
| record completeness | all 31 records must carry all 16 required fields |

---

# 9. Build status — implemented in the v0.4 review deck

```
BARIAH_FEEDBACK_IMPLEMENTED
DECK = K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4.pptx
REVIEW_PAGES = 100 · LEARNER_SCREENS = 29 · RUNTIME_STATES = 100
CHECKABLE_GATES = 105 · PASS = 105 · FAIL = 0
```

Every `CONFIRMED_IMPLEMENT` and `CONFIRMED_PROPAGATE` record in §4 is built and mechanically verified
in the deck. The four records that were never confirmable are built **as held**, not quietly dropped:

| Record | Held how |
|---|---|
| `BFB-03` MS2680 | omitted from S02 learner dialogue; retained in the S02 production panel with its `PENDING_SOURCE_VERIFICATION` status |
| `BFB-26` LMS exit | shell Next disabled on Tamat; the logical next Bahagian stays in production metadata and is not shown on the learner canvas |
| `BFB-24` quiz rationale | concise immediate feedback on canvas; detailed rationale in the production panel only |
| `BFB-04` / `BFB-27` cast | superseded — Alya, Encik Rahman and Hilmi are confirmed and built. Only the Pengurus Projek name stays open, and that role is not used in B02 |

Per-record verification lives in `STORYBOARD_QA_REPORT_v0.4.md` §2. Implementation status per
decision is recorded in `DECISION_REGISTER_B02_v0.4.json` under `implementation_status`.

---

# 10. Standing

Documentation only. No generator file modified, no PowerPoint regenerated, no component propagated,
no screen/state map produced, no canonical `P#` minted, no comment fabricated, and no ruling selected
on behalf of Bariah or Firdaus. `B02-CAIR-INT-001` remains open and still blocks canonical freeze,
production approval and MMD build.
