# TABLE_ROW_TO_POPUP_MATRIX — K5 PL06 T03 B02 Komponen Landskap

```
SOURCE-EVIDENCE ARTIFACT — INPUT FREEZE + COMPLETE SOURCE-TABLE INVENTORY + ROW-TO-POPUP COVERAGE
SOURCE_TABLE_INVENTORY_COMPLETE
NOT_READY_FOR_SCREEN_STATE_MAP_PENDING_AUTHORITY_RULINGS
BLOCKED_MODULE_DOCX_INTEGRITY_NOT_VERIFIED
NO GENERATOR CHANGED · NO PPTX REGENERATED OR PATCHED · NO COMPONENT PROPAGATED
```

> **Revision.** Stage 1 issued this document with a readiness verdict of
> `TABLE_INVENTORY_COMPLETE_READY_FOR_SCREEN_STATE_MAP`. **Stage 1.5 supersedes that verdict.** The
> source inventory is unchanged — 26 rows, 26 IDs, same locators, same image ownership — but the
> readiness claim was too strong: implementation-facing fields depend on rulings that have not been
> made, and the module DOCX integrity gap remains open. See §8.

---

# 1. Document status

## 1.1 Task scope

Stage 1 of the S&G v0.2 regeneration, **hardened at Stage 1.5**. This document establishes the
**authoritative source-table inventory** and the **row → Level 2 item → popup coverage matrix** that
must exist before any generator work begins.

**Stage 1.5 changed the status of this document, not its inventory.** Amendments: readiness verdict
superseded (§8); `IMPLEMENTATION AUTHORITY STATUS` added (§8); `SOURCE_ROW_COUNT` separated from
`PROPOSED_INTERACTION_ITEM_COUNT` (§8.3, §7); module DOCX integrity blocker recorded (§1.3, §8.5); one
Stage 1 statement corrected (§8.3). **No provisional row ID, source row order, source locator, image
ownership finding, row total or asset total was altered.**

**In scope:** locating and freezing authoritative inputs; enumerating every meaningful source-table row
across all nine learning components; assigning a stable provisional source-mapping ID to each; mapping
each to exactly one Level 2 item and one popup state, or recording an explicit exclusion; resolving
figure/image ownership by heading position; recording anomalies and normalisations.

**Explicitly out of scope and not performed:** storyboard generator changes, PowerPoint regeneration or
patching, component propagation, screen/state map production, MMD asset binding, multimedia production,
commit or push.

| Field | Value |
|---|---|
| Evidence date | 31 July 2026 |
| Repository | `/home/user/slide-interaction-layer` |
| Branch | `claude/verify-powerpoint-file-vpfzkg` |
| HEAD SHA | `7ac83e59ed565542d2617ab7e3993ea42bffd2b2` |
| Working tree at Stage 1 start | **clean** — `git status --porcelain` empty |
| Working tree at Stage 1.5 start | one untracked file — this document, as issued by Stage 1 |
| Files changed at Stage 1.5 | this file (status sections only) + `B02_PRE_STAGE2_RULING_EVIDENCE.md` (new) |

## 1.2 Change statement

**No generator code was changed. No PowerPoint was regenerated, patched, opened for write, or
re-saved. No source document was modified. No component was propagated. No screen/state map was
begun.** Every input below was opened read-only. The 19-screen storyboard v0.1 and the module PDF were
re-hashed after all analysis and are byte-identical to their frozen values.

**Stage 1.5 additionally asserts:** no provisional row ID was renamed or renumbered; no source row
order changed; no source locator changed; no image ownership finding changed; the 26-row and 14-asset
totals are unchanged; and no interaction split was converted into a source row. Verified mechanically —
see `B02_PRE_STAGE2_RULING_EVIDENCE.md` Appendix A.

## 1.3 Input freeze manifest

All hashes are SHA-256 of the exact bytes read.

### Authoritative specification

| # | Input | Path | Bytes | SHA-256 |
|---|---|---|---:|---|
| I-1 | **Updated S&G v0.2** — `K5 STORYBOARD & GENERATION SPECIFICATION / PL06 T03 B02 / Updated S&G v0.2 / Evidence date 31 July 2026 / Review authority: Bariah` | `/root/.claude/uploads/12837c42-b6ab-597b-8301-85c5b457471b/5efad61e-K5_PL06_T03_B02_UPDATED_SG_v0.2.docx` | 51,443 | `d52f0fe123863c0d7ff968efdacda91157331f49ac46f3b3aaf2e630b3c2403a` |

**Identity confirmed.** The document self-identifies as `Updated S&G v0.2`, evidence date
`31 July 2026`, review authority `Bariah - Instructional Design / eLearning`, scope
`K5 - PL06 - Topic 3 - Bahagian 2: Komponen Landskap`. This is the input the task names.

### Approved source module

| # | Input | Path / locator | Bytes | SHA-256 |
|---|---|---|---:|---|
| I-2 | **Module — rendered PDF**, module pp. 237–250 (physical 256–269), 14 pp. **Pagination and visual authority** | `/root/.claude/uploads/12837c42-b6ab-597b-8301-85c5b457471b/6a5c03ec-K5_PL06_T03_B02_pages_256269.pdf` | 429,918 | `30a6903dacbd7e8bce60dc1aa32026fc4ed98439054aeced9e895b5df828a3f4` |
| I-3 | **Module — approved DOCX**, `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx`. **Text-extraction authority** | Google Drive `fileId 16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4`, folder `1p18qHATFfn0oLHyCvYOfA8rQQlxkwJXS` ("5_Kursus Kerja Bangunan - Pembinaan Landskap Luar"), `modifiedTime 2026-06-07T23:30:02Z` | 16,832,861 | **not hashed — `BLOCKED_MODULE_DOCX_INTEGRITY_NOT_VERIFIED`, 4 routes attempted, see evidence pack §B** |
| I-3a | Local text extraction derived from I-3 (earlier session) | `…/scratchpad/module.txt` | 422,686 | `07595d7f74d5b0ebdf2122dcfd9e0731597a486e3de78959df95d1880be35fc3` |
| I-3b | B02 body span cut from I-3a, offsets 309045–323349 | `…/scratchpad/b02_body.txt` | 14,304 | `f35ce9ceaf17a68f4dd05fd4486a8223d7203bae249a84374c741154529768a2` |
| I-3c | Independent PDF row classification derived from I-2 (Stage 1.5) | `…/scratchpad/pdf_tables.json` | 9,810 | `1d58079fad6d67575a4ab984427ab5baf540a0727cedceb03482ed4a4d2b0527` |

> **I-3 integrity gap — `BLOCKED_MODULE_DOCX_INTEGRITY_NOT_VERIFIED`.** The exact bytes of the
> 16,832,861-byte source DOCX have **not** been cryptographically hashed. Four independent routes were
> attempted and all failed; the full attempt log is in `B02_PRE_STAGE2_RULING_EVIDENCE.md` §B.
> Identity remains pinned by Drive `fileId` + byte size + `modifiedTime`, which match the session that
> produced I-3a — **but a fileId, a byte size and a timestamp are not a cryptographic hash and are not
> recorded here as a substitute for one.**
>
> **Containment.** Every factual claim in §4 was cross-verified against I-2, which *is* hashed
> (`30a6903d…f828a3f4`) and covers the entire B02 page range. No row, page number, image assignment or
> row count in this document rests on I-3a alone. The gap therefore bounds *provenance certification*,
> not the correctness of the inventory — but it is a genuine blocker for Stage 2 adoption.

**Source uniqueness check.** A Drive search of the module's parent folder returns **exactly one** file
(`16j15Knt…`). Searches on `PL06`, `B02`, `T03` and `Landskap` surfaced no second, conflicting copy of
the approved module for this course. `AUTHORITATIVE_SOURCE_ESTABLISHED` — the
`BLOCKED_AUTHORITATIVE_SOURCE_NOT_ESTABLISHED` condition does **not** fire.

### Traceability-only inputs (read, never edited)

| # | Input | Path | Bytes | SHA-256 |
|---|---|---|---:|---|
| I-4 | Storyboard v0.1 (traceability only) | `reviews/storyboard-bariah/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_1.pptx` | 109,954 | `749b6c90f468bc0a1986b853319e62b1a1cec83600a98cbade628214d5bf8e7a` |
| I-5 | Bariah review checklist | `reviews/storyboard-bariah/BARIAH_REVIEW_CHECKLIST.md` | 11,753 | `cafc6da849930095082397066048cc139b9d10ef5f18e2d3f469e1876d87a6e1` |
| I-6 | Asset manifest — 14 extracted assets | `reviews/source-completion/B02_ASSET_MANIFEST.md` | 8,069 | `7107ea4943a31329d8dd0088aba26ca9bff45778ba03af6c7831b6602c949f55` |
| I-7 | Page and node map | `reviews/source-completion/B02_PAGE_AND_NODE_MAP.md` | 3,475 | `f04035fe995ca36c45b87222dd46ee219a114685b214af8db16ccbf158402d70` |
| I-8 | S01–S19 source coverage matrix | `reviews/source-completion/S01_S19_SOURCE_COVERAGE_MATRIX.md` | 5,525 | `0f9e76d3223435e5bfa9e3e0d498df42ab95108721bab5690dbb1e4881d53f38` |
| I-9 | Display/VO draft matrix | `reviews/source-completion/DISPLAY_VO_DRAFT_MATRIX.md` | 11,035 | `c0d755267cb52832e1c87d36482de2508dcaf5912fb9b1dad474bda330f77f2f` |
| I-10 | Source defect register | `reviews/source-completion/SOURCE_DEFECT_REGISTER.md` | 7,941 | `b730c40a03fb78cae95696967a207347b6013f6079ddf54cdb87a74c7df90259` |
| I-11 | Machine-readable asset manifest | `reviews/source-completion/source-assets/_manifest.json` | 7,294 | `2195a5ac6b2c27810e4b6be4ebf951d232b1060dd97d5fdd4f5085ccc2a08ada` |
| I-12 | **S&G Storyboard Development v1.0** (`Versi 1.0 \| Julai 2026`) — cross-check only; **conflicts with I-1 on two points, see §6 A-01** | Google Drive `fileId 1T4X-Mr8nBJhSTZ2GF62hPJHcSrPqfeCE` | 56,274 | not hashed locally (Drive-resident) |

---

# 2. Confirmed mapping contract

Extracted from **I-1 (S&G v0.2)**. This is a targeted extraction of the rules that govern this Stage 1
inventory — not a restatement of the specification.

## 2.1 Mandatory segmentation — I-1 §3.1

| Source element | Generated artifact |
|---|---|
| Main prose | **One main explanation screen** — function, description, construction aspects |
| Source table | **One separate example screen**, titled `Contoh [Nama Komponen]` |
| Each meaningful row | **One clickable Level 2 item** on that example screen |
| Each item | **One popup** carrying the row content, visual direction and VO |
| Nothing | **No omission** — every source row is accounted for in the screen map, a popup, or a documented exclusion decision |

## 2.2 Navigation depth — I-1 §2.1

> `Maximum navigation depth = 2.` Level 1 = component cards on the group master screen. Level 2 =
> table-derived example items on the example screen. **A popup is a content state, not a third
> navigation level.**

No popup opens another popup. No submenu inside a popup (I-1 §9.2).

## 2.3 Column-to-popup mapping — I-1 §3.2

| Source table field | Generated role | Requirement |
|---|---|---|
| Jenis / Bahan | Clickable item label and popup heading | MUST preserve source meaning; normalise only documented typos/case |
| Fungsi & Penerangan | Popup learner display + expanded VO | MUST be retained; display may be concise but VO must preserve propositions |
| Contoh | Popup example text and visual direction | MUST be retained when present |
| Embedded source image | Visual specification for MMD | Do not embed at ID review stage; cite source page/figure |
| No source image | Textual visual direction or approved native diagram spec | **Do not fabricate external visual content** |
| Missing source field | Production note | **Do not invent learner-facing facts** |

## 2.4 Naming and completion — I-1 §3.3, §2.3, §4.3

- All example screens use the generic title `Contoh [Nama Komponen]`, "because source tables may mix
  types, materials, functions, specifications and real examples".
- Level 2 items are clickable **in any order**; each viewed item receives a completion tick.
- `Kembali` is disabled until **all** Level 2 items carry ticks.
- A Level 1 card completes only after its Level 2 set is complete **and** the learner returns.
- Global `Seterusnya` enables only after all Level 1 cards in the group are complete.
- Viewed/completed states persist across revisit and LMS resume and **MUST NOT relock**.

## 2.5 Structure this Stage 1 inventory must feed

```
LEVEL 1 — group master screen
   └─ component card  →  MAIN EXPLANATION SCREEN   (from main prose)
                            └─ Seterusnya (VO-gated)
                                 →  LEVEL 2 — "Contoh [Nama Komponen]"   (from source table)
                                       └─ one clickable item per meaningful row
                                             └─ one popup state per item
```

## 2.6 Screen-count consequence — I-1 §1.3

The 19-screen model is `SUPERSEDED FOR LEARNING-CONTENT SEGMENTATION`. I-1 gives a planning baseline of
**approximately 28 physical screens** (original structure + one example screen per component). Popup
views are **states within** the example screen and are **not** counted as separate physical slides.
Final numbering is regenerated only after this inventory is reconciled — which is what this document
delivers.

---

# 3. Component inventory summary

| # | Group | Component | Prose located | Table located | Meaningful rows | Embedded source images | Rows without image | Ambiguities | Inventory status |
|---:|---|---|:-:|:-:|---:|---:|---:|---|---|
| 1 | Struktur Taman | Struktur Persisir Air | YES | YES | **5** | 1 | 4 | heading typo `Promenande` | `COMPLETE` |
| 2 | Struktur Taman | Struktur Teduhan | YES | YES | **5** | 1 | 4 | row 5 begins lowercase; no `Aspek Pembinaan` block | `COMPLETE` |
| 3 | Struktur Taman | Kemudahan Awam | YES | YES | **3** | 0 | 3 | `NO_DEDICATED_SOURCE_IMAGE`; prose/table spelling split | `COMPLETE` |
| 4 | Struktur Taman | Water Feature | YES | YES | **3** | 0 | 3 | `NO_DEDICATED_SOURCE_IMAGE`; missing space in row 3 label | `COMPLETE` |
| 5 | Perabot Taman | Kerusi Taman | YES | YES | **3** | 3 | 0 | unbalanced `)` in row 3 label | `COMPLETE` |
| 6 | Perabot Taman | Papan Tanda | YES | YES | **1** | 2 | 0 | **single-item example screen**; split candidate | `COMPLETE_WITH_REVIEW` |
| 7 | Perabot Taman | Tong Sampah | YES | YES | **3** | 4 | 0 | trailing colon in row 2 label | `COMPLETE` |
| 8 | Perabot Taman | Drinking Fountain | YES | YES | **2** | 2 | 0 | trailing colon in row 1 label | `COMPLETE` |
| 9 | Perabot Taman | BBQ Pit | YES | YES | **1** | 1 | 0 | **single-item example screen**; split candidate; source case `BBQ pit` | `COMPLETE_WITH_REVIEW` |
| | | **TOTAL** | **9/9** | **9/9** | **26** | **14** | **14** | | |

Rows carrying at least one embedded source image: **12**. Rows without: **14**. 12 + 14 = 26. ✅

**All 14 registered assets are assigned to a component and, where the source layout permits, to a
specific row. No asset is orphaned.**

---

# 4. Complete row-to-popup matrix

## 4.0 What these identifiers are — and are not

Every included row carries a stable provisional identifier:

```
K5-PL06-T03-B02-{COMPONENT_SLUG}-ROW-{NN}
```

**These are source-mapping identifiers only.** They exist so that a source row can be traced through
regeneration, review and QA without ambiguity.

**They are NOT:**

- canonical governance decision IDs — no `K5-DR-###` is issued, requested or implied here;
- production screen IDs — screen IDs are regenerated at Stage 2 under I-1 §8.1;
- popup implementation IDs — implementation placeholders follow I-1 §8.2
  (`[component]_EXAMPLE_[nn]`) and are assigned by the generator, not by this document.

K5 remains locked. This document issues no authority.

## 4.1 Index — 26 records

| provisional_row_id | Component | Order | Mod p | Level 2 item label | Popup | Status |
|---|---|:-:|:-:|---|:-:|:-:|
| `…-STRUKTUR-PERSISIR-AIR-ROW-01` | Struktur Persisir Air | 1 | 238 | Promenade | YES | INCLUDED |
| `…-STRUKTUR-PERSISIR-AIR-ROW-02` | Struktur Persisir Air | 2 | 238 | Jeti | YES | INCLUDED |
| `…-STRUKTUR-PERSISIR-AIR-ROW-03` | Struktur Persisir Air | 3 | 238 | Dek Kayu | YES | INCLUDED |
| `…-STRUKTUR-PERSISIR-AIR-ROW-04` | Struktur Persisir Air | 4 | 238 | Boardwalk | YES | INCLUDED |
| `…-STRUKTUR-PERSISIR-AIR-ROW-05` | Struktur Persisir Air | 5 | 238 | Footbridge | YES | INCLUDED |
| `…-STRUKTUR-TEDUHAN-ROW-01` | Struktur Teduhan | 1 | 239 | Gazebo | YES | INCLUDED |
| `…-STRUKTUR-TEDUHAN-ROW-02` | Struktur Teduhan | 2 | 239 | Wakaf | YES | INCLUDED |
| `…-STRUKTUR-TEDUHAN-ROW-03` | Struktur Teduhan | 3 | 239 | Pergola | YES | INCLUDED |
| `…-STRUKTUR-TEDUHAN-ROW-04` | Struktur Teduhan | 4 | 239 | Canopy | YES | INCLUDED |
| `…-STRUKTUR-TEDUHAN-ROW-05` | Struktur Teduhan | 5 | 239 | Struktur Teduhan Moden | YES | INCLUDED |
| `…-KEMUDAHAN-AWAM-ROW-01` | Kemudahan Awam | 1 | 240 | Tandas Awam | YES | INCLUDED |
| `…-KEMUDAHAN-AWAM-ROW-02` | Kemudahan Awam | 2 | 240 | Surau | YES | INCLUDED |
| `…-KEMUDAHAN-AWAM-ROW-03` | Kemudahan Awam | 3 | 240–241 | Bangunan Interpretatif | YES | INCLUDED |
| `…-WATER-FEATURE-ROW-01` | Water Feature | 1 | 241 | Air Pancut (Fountain) | YES | INCLUDED |
| `…-WATER-FEATURE-ROW-02` | Water Feature | 2 | 241 | Kolam (Pond) | YES | INCLUDED |
| `…-WATER-FEATURE-ROW-03` | Water Feature | 3 | 241 | Kolam Renang / Kolam Hiasan Besar (Pool) | YES | INCLUDED |
| `…-KERUSI-TAMAN-ROW-01` | Kerusi Taman | 1 | 242 | Kerusi Kayu Keras | YES | INCLUDED |
| `…-KERUSI-TAMAN-ROW-02` | Kerusi Taman | 2 | 243 | Kerusi Konkrit | YES | INCLUDED |
| `…-KERUSI-TAMAN-ROW-03` | Kerusi Taman | 3 | 243 | Kerusi Komposit | YES | INCLUDED |
| `…-PAPAN-TANDA-ROW-01` | Papan Tanda | 1 | 244 | Papan Tanda Arah / Papan Tanda Interpretatif | YES | INCLUDED |
| `…-TONG-SAMPAH-ROW-01` | Tong Sampah | 1 | 246 | Tong Sampah Logam | YES | INCLUDED |
| `…-TONG-SAMPAH-ROW-02` | Tong Sampah | 2 | 246–247 | Tong Sampah Konkrit/Batu | YES | INCLUDED |
| `…-TONG-SAMPAH-ROW-03` | Tong Sampah | 3 | 247 | Tong Sampah Plastik Kitar Semula (HDPE) | YES | INCLUDED |
| `…-DRINKING-FOUNTAIN-ROW-01` | Drinking Fountain | 1 | 248 | Pancutan Air Minum Keluli Tahan Karat | YES | INCLUDED |
| `…-DRINKING-FOUNTAIN-ROW-02` | Drinking Fountain | 2 | 248–249 | Pancutan Air Minum Konkrit/Batu | YES | INCLUDED |
| `…-BBQ-PIT-ROW-01` | BBQ Pit | 1 | 249–250 | BBQ Pit Struktur Kekal | YES | INCLUDED |

Prefix `…` expands to `K5-PL06-T03-B02`.

## 4.2 Records

Field values use `NOT_PRESENT_IN_SOURCE` where the source genuinely has no such field, and
`REVIEW_REQUIRED` where a human decision is needed. No cell is left ambiguously blank.

---

### GROUP: Struktur Taman

#### Component 1 — Struktur Persisir Air

Section heading measured at module p. 238, y = 79.2. Table at p. 238, y = 352.3–609.3, 6 rendered rows
(1 header + 5 data), 3 columns: `JENIS STRUKTUR | FUNGSI & PENERANGAN | CONTOH`.
Example screen title: **`Contoh Struktur Persisir Air`**.

> I-1 §3.4 independently names exactly these five items — *"Promenade, Jeti, Dek Kayu, Boardwalk and
> Footbridge as clickable items in any order"* — which corroborates this row count against the
> specification.

**`K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-01`**
- group: Struktur Taman · component: Struktur Persisir Air
- source_section: `3.3.1 Struktur Persisir Air (Promenande, Jeti, Dek, Boardwalk, footbridge)`
- source_table_title: `JENIS STRUKTUR | FUNGSI & PENERANGAN | CONTOH`
- source_row_order: 1 · printed_module_page: **238** · physical_pdf_page: **257**
- source_row_label: `Promenade`
- jenis_bahan: `Promenade`
- fungsi_penerangan: `Laluan lebar di sepanjang pinggir air, selesa untuk berjalan dan bersantai.`
- contoh: `Promenade Tasik Titiwangsa, KL`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE`
- image_ownership_evidence: the only figure in this section is Rajah 23, captioned `Contoh Boardwalk`, which attributes to ROW-04 by caption
- proposed_level_2_item_label: **`Promenade`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE_AT_ROW_LEVEL`
- normalisation_reason: the table cell already reads `Promenade`; the typo `Promenande` is confined to the section heading — see N-01
- ambiguity_or_human_review: `NONE`
- evidence_reference: I-2 p258 tbl0 r1 · I-3a `## Struktur Taman → ### Struktur Persisir Air` table

**`K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-02`**
- source_row_order: 2 · printed_module_page: **238** · physical_pdf_page: **257**
- source_row_label / jenis_bahan: `Jeti`
- fungsi_penerangan: `Platform atau pelantar panjang untuk akses ke air, sering digunakan untuk bot.`
- contoh: `Jeti Lumut, Perak`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: `NOT_APPLICABLE`
- proposed_level_2_item_label: **`Jeti`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: `NONE` · evidence_reference: I-2 p258 tbl0 r2

**`K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-03`**
- source_row_order: 3 · printed_module_page: **238** · physical_pdf_page: **257**
- source_row_label / jenis_bahan: `Dek Kayu`
- fungsi_penerangan: `Ruang kayu terbuka di atas atau berhampiran air untuk rehat & pemandangan.`
- contoh: `Wetland Park Putrajaya`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: `NOT_APPLICABLE`
- proposed_level_2_item_label: **`Dek Kayu`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: source heading abbreviates this to `Dek`; the table row reads `Dek Kayu`. Table form adopted — no conflict, recorded for transparency
- evidence_reference: I-2 p258 tbl0 r3

**`K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-04`**
- source_row_order: 4 · printed_module_page: **238** · physical_pdf_page: **257**
- source_row_label / jenis_bahan: `Boardwalk`
- fungsi_penerangan: `Laluan kayu di atas tanah berpaya/basah, mesra alam dan visual semula jadi.`
- contoh: `Boardwalk Paya Indah Wetlands`
- source_image_or_figure: **`Rajah 23: Contoh Boardwalk dalam Taman Paya Bakau`** — asset `K5PL06T03-B02-IMG-p239-x20`, module p. 239, physical 258, 658 × 395 jpeg
- image_ownership_evidence: image at p239 y 57.6–247.2, caption at y 255.4. Nearest preceding section heading is Struktur Persisir Air (p238 y 79.2); the next heading, Struktur Teduhan, is at p239 y 298.8 — **below** the image. **Caption names Boardwalk explicitly**, so row-level attribution is caption-verified, not inferred
- proposed_level_2_item_label: **`Boardwalk`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: `NONE`
- evidence_reference: I-2 p258 tbl0 r4; I-2 p258 image xref 20; I-6 row 1

**`K5-PL06-T03-B02-STRUKTUR-PERSISIR-AIR-ROW-05`**
- source_row_order: 5 · printed_module_page: **238** · physical_pdf_page: **257**
- source_row_label / jenis_bahan: `Footbridge`
- fungsi_penerangan: `Jambatan kecil untuk laluan pejalan kaki melintasi aliran air atau longkang besar.`
- contoh: `Footbridge Taman Botani Perdana`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: `NOT_APPLICABLE`
- proposed_level_2_item_label: **`Footbridge`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE_AT_ROW_LEVEL`
- normalisation_reason: source heading writes `footbridge` lowercase; the table row is already `Footbridge` — see N-02
- ambiguity_or_human_review: `NONE` · evidence_reference: I-2 p258 tbl0 r5

---

#### Component 2 — Struktur Teduhan

Heading at module p. 239, y = 298.8. Table at p. 239, y = 402.5–707.0, 6 rendered rows (1 header +
5 data), 3 columns. Example screen title: **`Contoh Struktur Teduhan`**.
**This is the only subsection in 3.3 with no `Aspek Pembinaan` block** — see §6 A-06.

**`K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-01`**
- source_section: `3.3.2 Struktur Teduhan` · source_table_title: `JENIS STRUKTUR | FUNGSI & PENERANGAN | CONTOH`
- source_row_order: 1 · printed_module_page: **239** · physical_pdf_page: **258**
- source_row_label / jenis_bahan: `Gazebo`
- fungsi_penerangan: `Struktur berbumbung terbuka untuk bersantai atau menikmati pemandangan.`
- contoh: `Taman Tasik Shah Alam`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: `NOT_APPLICABLE`
- proposed_level_2_item_label: **`Gazebo`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: English-origin term; italic treatment governed by the lexicon decision — see N-07
- evidence_reference: I-2 p258 tbl0 r1

**`K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-02`**
- source_row_order: 2 · printed_module_page: **239** · physical_pdf_page: **258**
- source_row_label / jenis_bahan: `Wakaf`
- fungsi_penerangan: `Struktur tradisional Melayu yang digunakan sebagai tempat berehat.`
- contoh: `Wakaf di Taman Desa, KL`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: `NOT_APPLICABLE`
- proposed_level_2_item_label: **`Wakaf`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE`
- normalisation_reason: **`Wakaf` is Malay and MUST NOT receive English-term italic treatment**, unlike its table neighbours
- ambiguity_or_human_review: `NONE` · evidence_reference: I-2 p258 tbl0 r2

**`K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-03`**
- source_row_order: 3 · printed_module_page: **239** · physical_pdf_page: **258**
- source_row_label / jenis_bahan: `Pergola`
- fungsi_penerangan: `Rangka struktur terbuka yang biasanya ditumbuhi tanaman pemanjat seperti bougainvillea.`
- contoh: `Pergola di Laman Herba Putrajaya`
- source_image_or_figure: **`Rajah 24: Contoh Pergola`** — asset `K5PL06T03-B02-IMG-p240-x23`, module p. 240, physical 259, 506 × 379 jpeg
- image_ownership_evidence: image at p240 y 57.6–268.1, caption y 276.2. Preceding heading Struktur Teduhan (p239 y 298.8); next heading Kemudahan Awam at p240 y 320.0 is **below** the image. **Caption names Pergola explicitly** — row-level attribution caption-verified
- proposed_level_2_item_label: **`Pergola`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: `NONE` · evidence_reference: I-2 p259 tbl0 r3; I-2 p259 image xref 23; I-6 row 2

**`K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-04`**
- source_row_order: 4 · printed_module_page: **239** · physical_pdf_page: **258**
- source_row_label / jenis_bahan: `Canopy`
- fungsi_penerangan: `Struktur kain atau polikarbonat ringan untuk teduhan kawasan aktiviti`
- contoh: `Canopy rekreasi di Taman Jaya`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: `NOT_APPLICABLE`
- proposed_level_2_item_label: **`Canopy`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `RECORDED_NOT_APPLIED` — terminal full stop absent on this cell alone, unlike its four neighbours
- normalisation_reason: punctuation-only inconsistency; **not corrected at Stage 1** — display punctuation is a Stage 2 authoring decision
- ambiguity_or_human_review: `NONE` · evidence_reference: I-2 p258 tbl0 r4

**`K5-PL06-T03-B02-STRUKTUR-TEDUHAN-ROW-05`**
- source_row_order: 5 · printed_module_page: **239** · physical_pdf_page: **258**
- source_row_label / jenis_bahan: `Struktur Teduhan Moden`
- fungsi_penerangan: `struktur teduhan dengan reka bentuk kontemporari, menggunakan bahan seperti keluli dan panel lutsinar atau berlubang untuk mencipta corak cahaya dan bayangan.`
- contoh: `Banyak kawasan awam di Putrajaya`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: `NOT_APPLICABLE`
- proposed_level_2_item_label: **`Struktur Teduhan Moden`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `RECORDED_NOT_APPLIED` — cell begins lowercase `struktur`; sentence case proposed
- normalisation_reason: sentence-case inconsistency against the other four rows of the same table; **recorded, not silently corrected** — see N-03
- ambiguity_or_human_review: `NONE` · evidence_reference: I-2 p258 tbl0 r5

---

#### Component 3 — Kemudahan Awam

Heading at module p. 240, y = 320.0. Table at p. 240, y = 530.9–770.9, **2 columns**:
`CONTOH | PENERANGAN`. The last data row continues onto p. 241 (y 56.4–88.6).
Example screen title: **`Contoh Kemudahan Awam`**.
**`NO_DEDICATED_SOURCE_IMAGE`** for the whole component — see §6 A-04.

> This table has **no `Jenis / Bahan` column**. Under I-1 §3.2 the clickable item label is taken from
> the `CONTOH` column, which is this table's identifying field. Recorded as a structural variance, not
> a missing field.

**`K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-01`**
- source_section: `3.3.3 Kemudahan Awam` · source_table_title: `CONTOH | PENERANGAN`
- source_row_order: 1 · printed_module_page: **240** · physical_pdf_page: **259**
- source_row_label: `Tandas Awam`
- jenis_bahan: `NOT_PRESENT_IN_SOURCE` — table has no Jenis/Bahan column
- fungsi_penerangan: `Kemudahan sanitasi yang bersih dan boleh diakses. Pembinaannya perlu mematuhi piawaian kebersihan dan mempunyai sistem bekalan air serta saliran yang cekap.`
- contoh: `Tandas Awam` — the row label is itself the Contoh value
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE`
- image_ownership_evidence: `3.3.3` heading at p240 y 320.0; the only image on p240 is at y 57.6–268.1, **above** the heading, and belongs to Struktur Teduhan. **p241 carries no image at all.** Confirmed absence in the rendered PDF, not an extraction failure
- proposed_level_2_item_label: **`Tandas Awam`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: popup visual direction requires a decision under I-1 §3.2 row "No source image" — textual direction or approved native diagram spec. `REVIEW_REQUIRED` at Stage 2
- evidence_reference: I-2 p259 tbl0 r1

**`K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-02`**
- source_row_order: 2 · printed_module_page: **240** · physical_pdf_page: **259**
- source_row_label: `Surau` · jenis_bahan: `NOT_PRESENT_IN_SOURCE`
- fungsi_penerangan: `Ruang ibadah yang disediakan untuk umat Islam menunaikan solat. Reka bentuk biasanya ringkas tetapi memenuhi keperluan keagamaan.`
- contoh: `Surau`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: as ROW-01
- proposed_level_2_item_label: **`Surau`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: visual direction `REVIEW_REQUIRED` as ROW-01
- evidence_reference: I-2 p259 tbl0 r2

**`K5-PL06-T03-B02-KEMUDAHAN-AWAM-ROW-03`**
- source_row_order: 3 · printed_module_page: **240–241** (row starts p240, continues p241) · physical_pdf_page: **259–260**
- source_row_label: `Bangunan Interpretatif` · jenis_bahan: `NOT_PRESENT_IN_SOURCE`
- fungsi_penerangan: `Struktur yang menyediakan maklumat pendidikan tentang persekitaran (flora, fauna, sejarah, geologi) melalui pameran, paparan, atau papan tanda.`
- contoh: `Bangunan Interpretatif`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: as ROW-01
- proposed_level_2_item_label: **`Bangunan Interpretatif`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `RECORDED_NOT_APPLIED`
- normalisation_reason: the **prose** above this table spells it `bangunan interpretative` (English form); the **table row** reads `Bangunan Interpretatif` (Malay form). Both are source-attested. Table form adopted as the item label — see N-04
- ambiguity_or_human_review: this row's text is split across two pages by a continuation row (E-12); the two fragments are joined here. Fragment boundary falls mid-parenthesis after `sejarah,`
- evidence_reference: I-2 p259 tbl0 r3 + p260 tbl0 r0 (continuation)

---

#### Component 4 — Water Feature

Heading at module p. 241, y = 112.0, rendered in **Arial,Italic** in the source. Table at p. 241,
y = 343.6–536.1, 2 columns: `CONTOH | PENERANGAN`. Example screen title:
**`Contoh Water Feature`**. **`NO_DEDICATED_SOURCE_IMAGE`** — see §6 A-04.

**`K5-PL06-T03-B02-WATER-FEATURE-ROW-01`**
- source_section: `3.3.4 Water Feature (Fountain, Pond, Pool)` · source_table_title: `CONTOH | PENERANGAN`
- source_row_order: 1 · printed_module_page: **241** · physical_pdf_page: **260**
- source_row_label: `Air Pancut (Fountain)` · jenis_bahan: `NOT_PRESENT_IN_SOURCE`
- fungsi_penerangan: `Struktur yang mengeluarkan air dalam corak tertentu, mewujudkan bunyi yang menenangkan dan pergerakan visual.`
- contoh: `Air Pancut (Fountain)`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE`
- image_ownership_evidence: `3.3.4` heading at p241 y 112.0; **p241 carries zero embedded images**. Confirmed absence in the rendered PDF
- proposed_level_2_item_label: **`Air Pancut (Fountain)`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: visual direction `REVIEW_REQUIRED` — no source image
- evidence_reference: I-2 p260 tbl1 r1

**`K5-PL06-T03-B02-WATER-FEATURE-ROW-02`**
- source_row_order: 2 · printed_module_page: **241** · physical_pdf_page: **260**
- source_row_label: `Kolam (Pond)` · jenis_bahan: `NOT_PRESENT_IN_SOURCE`
- fungsi_penerangan: `Kawasan air statik atau perlahan, boleh menjadi kolam hiasan, kolam ikan, atau kolam refleksi.`
- contoh: `Kolam (Pond)`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: as ROW-01
- proposed_level_2_item_label: **`Kolam (Pond)`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: visual direction `REVIEW_REQUIRED`
- evidence_reference: I-2 p260 tbl1 r2

**`K5-PL06-T03-B02-WATER-FEATURE-ROW-03`**
- source_row_order: 3 · printed_module_page: **241** · physical_pdf_page: **260**
- source_row_label: `Kolam Renang/Kolam Hiasan Besar(Pool)` — **verbatim, including the missing space**
- jenis_bahan: `NOT_PRESENT_IN_SOURCE`
- fungsi_penerangan: `Kolam berskala lebih besar, sama ada untuk berenang atau sebagai kolam hiasan dengan ciri-ciri reka bentuk yang kompleks.`
- contoh: `Kolam Renang/Kolam Hiasan Besar(Pool)`
- source_image_or_figure: `NOT_PRESENT_IN_SOURCE` · image_ownership_evidence: as ROW-01
- proposed_level_2_item_label: **`Kolam Renang / Kolam Hiasan Besar (Pool)`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: **`TYPOGRAPHIC`** — space inserted before `(Pool)`; spaces added around the solidus
- normalisation_reason: `Besar(Pool)` is a source spacing defect. Typographic only; **no word, order or meaning changed**. Source form preserved verbatim in `source_row_label` above — see N-05
- ambiguity_or_human_review: visual direction `REVIEW_REQUIRED`
- evidence_reference: I-2 p260 tbl1 r3

---

### GROUP: Perabot Taman

#### Component 5 — Kerusi Taman

Heading at module p. 242, y = 182.6. Table spans **pp. 242–243**, 2 columns:
`CONTOH | SPESIFIKASI`. The header row is **repeated** on p. 243 (see E-05).
Example screen title: **`Contoh Kerusi Taman`**.

> **Spec-cell structure.** Every `SPESIFIKASI` cell in the Perabot Taman tables is a **lettered list**
> (`a.`, `b.`, `c.`, `d.`) with roman sub-items (`i.`, `ii.`, `iii.`) where present — verified in the
> rendered PDF text layer. These letters are **sub-fields of one record**, not independent records.
> This is the evidentiary basis for not splitting these rows; see §6 A-05.

**`K5-PL06-T03-B02-KERUSI-TAMAN-ROW-01`**
- source_section: `3.4.1 Kerusi Taman` · source_table_title: `CONTOH | SPESIFIKASI`
- source_row_order: 1 · printed_module_page: **242** · physical_pdf_page: **261**
- source_row_label: `Kerusi Kayu KerasContoh: Jati, Cengal, Balau` — rendered as two lines, `Kerusi Kayu Keras` / `Contoh: Jati, Cengal, Balau`
- jenis_bahan: `Kerusi Kayu Keras`
- fungsi_penerangan: `a. Bahan: Kayu padu gred perabot luar, dengan ketahanan semula jadi yang tinggi terhadap serangga dan reput, atau kayu yang telah dirawat tekanan (pressure-treated) untuk meningkatkan ketahanan. b. Dimensi Komponen: Ketebalan minimum komponen utama (kaki, tempat duduk, sandaran) sekitar 25mm hingga 50mm untuk kestabilan dan kekuatan. c. Penyambungan: Menggunakan skru tahan karat (stainless steel), bolt, atau tanggam kayu yang kuat (mortise and tenon joints) untuk sambungan yang kukuh. d. Kemasan: Selesai dengan sealant luaran (outdoor sealant), minyak kayu (wood oil), atau varnis yang tahan UV dan kelembapan untuk perlindungan daripada cuaca dan mengekalkan warna kayu`
- contoh: `Jati, Cengal, Balau`
- source_image_or_figure: asset `K5PL06T03-B02-IMG-p242-x28`, module p. 242, physical 261, 439 × 439 jpeg — **unnumbered table photograph, no caption**
- image_ownership_evidence: image at p242 y 469.7–680.4, inside the table bbox (y 389.7–755.8). Section heading Kerusi Taman at p242 y 182.6; next heading Papan Tanda at p243 y 574.0. Only one data row on p242, so the image falls within it
- proposed_level_2_item_label: **`Kerusi Kayu Keras`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `STRUCTURAL_SPLIT_OF_LABEL_CELL` — the `Contoh:` clause is separated from the item label into the `contoh` field
- normalisation_reason: the source cell packs label and examples into one cell across two rendered lines; I-1 §3.2 maps them to different generated roles. **No text altered, only routed**
- ambiguity_or_human_review: Tier-2 English terms (`pressure-treated`, `stainless steel`, `mortise and tenon joints`, `outdoor sealant`, `wood oil`) carry no italic rule — see N-07
- evidence_reference: I-2 p261 tbl0 r1; I-2 p261 image xref 28; I-6 row 3

**`K5-PL06-T03-B02-KERUSI-TAMAN-ROW-02`**
- source_row_order: 2 · printed_module_page: **243** · physical_pdf_page: **262**
- source_row_label / jenis_bahan: `Kerusi Konkrit`
- fungsi_penerangan: `a. Konkrit bertetulang gentian (Fiber-Reinforced Concrete - FRC) atau konkrit pratuang (precast concrete). Pembesaran (expansion joints) mungkin diperlukan untuk mengelakkan keretakan akibat perubahan suhu. b. Kemasan: Boleh dibiarkan asli, digilap, dicat, atau mempunyai kemasan tekstur (exposed aggregate). Permukaan mestilah licin untuk keselesaan, tanpa tepi tajam.`
- contoh: `NOT_PRESENT_IN_SOURCE` — this row carries no `Contoh:` clause
- source_image_or_figure: asset `K5PL06T03-B02-IMG-p243-x31`, module p. 243, physical 262, 447 × 334 jpeg
- image_ownership_evidence: image at p243 y 88.9–249.2. Table on p243 spans y 56.5–550.8 with two data rows; this image sits in the upper band, which is the `Kerusi Konkrit` row. Papan Tanda heading at p243 y 574.0 is **below** the table, so the image cannot belong to Papan Tanda
- proposed_level_2_item_label: **`Kerusi Konkrit`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `NONE` · normalisation_reason: `NOT_APPLICABLE`
- ambiguity_or_human_review: `contoh` field genuinely absent — I-1 §3.2 requires `Contoh` "when present". Popup must not invent one
- evidence_reference: I-2 p262 tbl0 r1; I-2 p262 image xref 31; I-6 row 4

**`K5-PL06-T03-B02-KERUSI-TAMAN-ROW-03`**
- source_row_order: 3 · printed_module_page: **243** · physical_pdf_page: **262**
- source_row_label: `Kerusi KompositContoh: WPC - Wood-Plastic Composite / Plastik Kitar Semula):` — **verbatim, including the unbalanced `)`**
- jenis_bahan: `Kerusi Komposit`
- fungsi_penerangan: `a. Bahan: Papan atau profil yang dihasilkan daripada campuran gentian kayu/selulosa dan plastik kitar semula. Tahan UV, kalis air, tidak reput, dan kalis serangga. b. Kemasan: Warna disepadukan dalam bahan, tidak memerlukan cat atau varnis. Tekstur permukaan mungkin meniru urat kayu.`
- contoh: `WPC - Wood-Plastic Composite / Plastik Kitar Semula`
- source_image_or_figure: asset `K5PL06T03-B02-IMG-p243-x32`, module p. 243, physical 262, 429 × 361 jpeg
- image_ownership_evidence: image at p243 y 359.2–532.4, lower band of the same table, corresponding to the `Kerusi Komposit` row; still **above** the Papan Tanda heading at y 574.0
- proposed_level_2_item_label: **`Kerusi Komposit`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `RECORDED_NOT_APPLIED` — trailing `):` is unbalanced; no opening parenthesis exists
- normalisation_reason: **not corrected.** Two readings are possible — a dropped `(` before `WPC`, or a stray character. Guessing which would change source meaning. `REVIEW_REQUIRED` — see N-06
- ambiguity_or_human_review: **`REVIEW_REQUIRED`** — unbalanced parenthesis in the source label cell
- evidence_reference: I-2 p262 tbl0 r2; I-2 p262 image xref 32; I-6 row 5

---

#### Component 6 — Papan Tanda

Heading at module p. 243, y = 574.0. **Table at module p. 244** (physical 263), y = 56.5–676.6,
2 columns, **1 header + 1 data row**. Two captioned figures follow on p. 245.
Example screen title: **`Contoh Papan Tanda`**.

> ⚠ **Single-item example screen.** This component yields exactly **one** Level 2 item. Under I-1 §4.3
> `Kembali` is gated on "all example items viewed", which a one-item screen satisfies after a single
> click. Flagged in §6 A-05 as a design consequence requiring a human decision — it is **not** an
> inventory defect.

**`K5-PL06-T03-B02-PAPAN-TANDA-ROW-01`**
- source_section: `3.4.1 Papan Tanda` (heading p. 243; table p. 244) · source_table_title: `CONTOH | SPESIFIKASI`
- source_row_order: 1 · printed_module_page: **244** · physical_pdf_page: **263**
- source_row_label / jenis_bahan: `Papan Tanda Arah/Papan Tanda Interpretatif`
- fungsi_penerangan: `a. Bahan Panel: i. Aluminium Komposit (ACP): Panel sandwic aluminium dengan teras polietilena, ringan, tahan cuaca, dan stabil dimensi. Ketebalan 3-4mm. ii. HPL (High-Pressure Laminate) Gred Luar: Tahan luntur UV, calar, dan lelasan. Ketebalan 6-10mm. iii. Akrilik (UV-Stabilized Acrylic): Tahan UV, jernih, dan ringan. Ketebalan 5-10mm. iv. Kayu Dirawat Tekanan/Kayu Keras: Tebal minimum 20mm, dengan ukiran atau cetakan laser. b. Bahan Struktur/Tiang: Keluli Bersalut Serbuk/Tahan Karat: Tiub atau profil keluli 50mm x 50mm atau lebih besar, dengan salutan anti-karat. Kayu Keras/Dirawat Tekanan: Tiang berukuran minimum 75mm x 75mm. c. Grafik: Cetakan UV langsung pada panel, cetakan digital pada vinil gred luar, atau ukiran laser/ukiran mekanikal. Mesti tahan pudar (fade-resistant). d. Rekaan: Font yang jelas, saiz teks yang sesuai untuk jarak pandang, kontras warna yang tinggi. Ikonografi universal jika perlu.`
- contoh: `NOT_PRESENT_IN_SOURCE` — no `Contoh:` clause in the label cell
- source_image_or_figure: **two captioned figures** — `Rajah 25: Contoh Lukisan Spesifikasi Papan Tanda Informasi` (asset `K5PL06T03-B02-IMG-p245-x37`, 408 × 476 jpeg) and `Rajah 26: Contoh Spesifikasi Papan Tanda Penunjuk Arah` (asset `K5PL06T03-B02-IMG-p245-x38`, 413 × 472 jpeg), both module p. 245, physical 264
- image_ownership_evidence: figures at p245 y 57.6–313.8 (caption y 322.8) and y 365.4–619.7 (caption y 629.2). Preceding section heading is Papan Tanda (p243 y 574.0); the next heading, Tong Sampah, is at **p245 y 672.8 — below both figures**. Both captions name Papan Tanda explicitly. **Section-level figures: they follow the table rather than sitting inside a row cell**, so they attach to this component's single row and to its main explanation screen
- proposed_level_2_item_label: **`Papan Tanda Arah / Papan Tanda Interpretatif`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `TYPOGRAPHIC` — spaces added around the solidus in the item label
- normalisation_reason: readability of a 44-character item label; no word or order changed
- ambiguity_or_human_review: **`REVIEW_REQUIRED` — proposed split, flagged and NOT applied.** The single spec cell contains four lettered sub-fields, of which `a. Bahan Panel` has four roman sub-items (ACP, HPL, Akrilik, Kayu Dirawat Tekanan/Kayu Keras) and `b. Bahan Struktur/Tiang` has two. A defensible alternative reading is **6 Level 2 items** (4 panel materials + 2 post materials) instead of 1. **Not applied**, because the lettered structure marks these as sub-fields of one record rather than independent records — the source presents one sign type with a specification, not six sign types. Bariah/ID decision required
- evidence_reference: I-2 p263 tbl0 r1; I-2 p264 images xref 37, 38; I-6 rows 6–7

---

#### Component 7 — Tong Sampah

Heading at module p. 245, y = 672.8. Table spans **pp. 246–247**, 2 columns. Header row **repeated**
on p. 247 (E-09); an empty continuation row also appears on p. 247 (E-13).
Example screen title: **`Contoh Tong Sampah`**.

**`K5-PL06-T03-B02-TONG-SAMPAH-ROW-01`**
- source_section: `3.4.1 Tong Sampah` · source_table_title: `CONTOH | SPESIFIKASI`
- source_row_order: 1 · printed_module_page: **246** · physical_pdf_page: **265**
- source_row_label: `Tong Sampah Logam (Keluli Bersalut Serbuk, Keluli Tahan Karat)Contoh: Tong sampah silinder atau segi empat tepat dengan penutup berayun atau bukaan di atas, sering dilihat di taman bandar.`
- jenis_bahan: `Tong Sampah Logam (Keluli Bersalut Serbuk, Keluli Tahan Karat)`
- fungsi_penerangan: `a. Bahan: Keluli lembut yang digalvani dan disalut serbuk (galvanized and powder-coated steel) atau keluli tahan karat (stainless steel). Ketebalan dinding badan minimum 1.2mm. b. Ciri-ciri: Penutup yang tahan cuaca dan tahan haiwan, pembukaan pembuangan sampah yang ergonomik. Dilengkapi dengan tong dalam (liner) yang mudah dikeluarkan (biasanya plastik atau galvanised steel) untuk pengosongan yang mudah.`
- contoh: `Tong sampah silinder atau segi empat tepat dengan penutup berayun atau bukaan di atas, sering dilihat di taman bandar.`
- source_image_or_figure: asset `K5PL06T03-B02-IMG-p246-x41`, module p. 246, physical 265, 420 × 498 jpeg — unnumbered table photograph
- image_ownership_evidence: image at p246 y 262.1–515.5. Row label `Tong Sampah Logam…` renders at y 135.3; the next row label, `Tong Sampah Konkrit/Batu:`, at y 645.5. The image falls **between** them → this row
- proposed_level_2_item_label: **`Tong Sampah Logam`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `STRUCTURAL_SPLIT_OF_LABEL_CELL` + `LABEL_SHORTENED_FOR_DISPLAY`
- normalisation_reason: the material qualifier `(Keluli Bersalut Serbuk, Keluli Tahan Karat)` is retained in `jenis_bahan` and in the popup heading but dropped from the clickable label, which would otherwise run 62 characters. **Full form preserved in the record; nothing lost**
- ambiguity_or_human_review: label-length policy for Level 2 items is undefined — see §6 A-08
- evidence_reference: I-2 p265 tbl0 r1; I-2 p265 image xref 41; I-6 row 8

**`K5-PL06-T03-B02-TONG-SAMPAH-ROW-02`**
- source_row_order: 2 · printed_module_page: **246–247** (starts p246, continues p247) · physical_pdf_page: **265–266**
- source_row_label: `Tong Sampah Konkrit/Batu:Contoh: Tong sampah berat dan kukuh yang disepadukan dengan reka bentuk landskap.`
- jenis_bahan: `Tong Sampah Konkrit/Batu` — source carries a trailing colon
- fungsi_penerangan: `a. Bahan: Konkrit bertetulang atau batu asli/tiruan. Berat yang mencukupi untuk mengelakkan kecurian atau pergerakan yang tidak disengajakan. b. Ciri-ciri: Pembukaan yang sesuai untuk sampah, mungkin dengan atau tanpa tong dalam logam.`
- contoh: `Tong sampah berat dan kukuh yang disepadukan dengan reka bentuk landskap.`
- source_image_or_figure: asset `K5PL06T03-B02-IMG-p247-x44`, module p. 247, physical 266, 337 × 337 jpeg
- image_ownership_evidence: image at p247 y 73.0–247.0. **This is the p247–249 boundary case.** The `3.4.2 Drinking Fountain` heading sits at p247 y 537.2 — **below** the image, so the image cannot belong to Drinking Fountain. On p247 the next row label, `Tong Sampah Plastik Kitar Semula`, renders at y 265.7 — **below** the image. The image therefore falls in the band belonging to the row continuing from p246, i.e. `Tong Sampah Konkrit/Batu`. **Determined by heading and row-label position, not page number**
- proposed_level_2_item_label: **`Tong Sampah Konkrit/Batu`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `TYPOGRAPHIC` — trailing colon removed from the item label
- normalisation_reason: `Tong Sampah Konkrit/Batu:` — the colon separates the label from the `Contoh:` clause in the packed source cell; it is punctuation, not part of the name. Source form preserved verbatim above
- ambiguity_or_human_review: `NONE` — boundary resolved by measurement
- evidence_reference: I-2 p265 tbl0 r2; I-2 p266 image xref 44; I-6 row 9

**`K5-PL06-T03-B02-TONG-SAMPAH-ROW-03`**
- source_row_order: 3 · printed_module_page: **247** · physical_pdf_page: **266**
- source_row_label: `Tong Sampah Plastik Kitar Semula (HDPE)Contoh: Tong sampah berwarna-warni yang sering digunakan untuk pengasingan sisa kitar semula.`
- jenis_bahan: `Tong Sampah Plastik Kitar Semula (HDPE)`
- fungsi_penerangan: `a. Bahan: Plastik berketumpatan tinggi (HDPE) yang tahan UV, tidak reput, dan mudah dibersihkan. b. Ciri-ciri: Ringan, mudah dialihkan (jika tidak dipasang tetap), tersedia dalam pelbagai warna untuk tujuan pengasingan.`
- contoh: `Tong sampah berwarna-warni yang sering digunakan untuk pengasingan sisa kitar semula.`
- source_image_or_figure: **two assets** — `K5PL06T03-B02-IMG-p247-x45` (198 × 281 jpeg) and `K5PL06T03-B02-IMG-p247-x46` (195 × 280 jpeg), both module p. 247, physical 266
- image_ownership_evidence: both at p247 y ≈ 376.5–511, **below** this row's label at y 265.7 and **above** the `3.4.2 Drinking Fountain` heading at y 537.2. Side-by-side pair within the same row cell
- proposed_level_2_item_label: **`Tong Sampah Plastik Kitar Semula (HDPE)`** — 39 characters
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `STRUCTURAL_SPLIT_OF_LABEL_CELL`
- normalisation_reason: `Contoh:` clause routed to the `contoh` field per I-1 §3.2. Source also carries a trailing double space, dropped as whitespace only
- ambiguity_or_human_review: **longest proposed item label in the inventory at 39 characters** — see §6 A-08
- evidence_reference: I-2 p266 tbl0 r2; I-2 p266 images xref 45, 46; I-6 rows 10–11

---

#### Component 8 — Drinking Fountain

Heading at module p. 247, y = 537.2, rendered **Arial,Italic** in the source. Table at p. 248,
y = 56.5–740.5, 2 columns, 1 header + 2 data rows; the second row continues onto p. 249.
Example screen title: **`Contoh Drinking Fountain`**.

**`K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-01`**
- source_section: `3.4.2 Drinking Fountain` · source_table_title: `CONTOH | SPESIFIKASI`
- source_row_order: 1 · printed_module_page: **248** · physical_pdf_page: **267**
- source_row_label: `Pancutan Air Minum Keluli Tahan Karat:Contoh: Unit pancutan air yang moden dan bersih, biasa ditemui di taman-taman bandar utama seperti KLCC Park atau Taman Botani Perdana, Kuala Lumpur.`
- jenis_bahan: `Pancutan Air Minum Keluli Tahan Karat` — source carries a trailing colon
- fungsi_penerangan: `a. Bahan: Keluli Tahan Karat Gred 304 atau 316 (Gred 316 lebih tahan kakisan untuk persekitaran pantai). Tebal minimum 1.5mm. b. Injap & Mekanisme: Injap tekan (push-button valve) yang tahan lasak dan tahan vandalisme. Mekanisme pancutan air yang membersihkan diri (self-cleaning) adalah bonus. c. Kepala Pancutan: Direka untuk aliran air yang stabil dan bersih, dilindungi daripada sentuhan langsung dengan mulut pengguna. d. Sistem Penapisan (Pilihan): Penapis karbon atau sedimen untuk meningkatkan kualiti air. e. Sistem Perpaipan: Perpaipan air bersih (biasanya PVC atau HDPE) dan sistem saliran air buangan yang cekap, bersambung terus ke bekalan air dan sistem perparitan. Injap tutup (shut-off valve) perlu dipasang untuk penyelenggaraan. f. Reka Bentuk: Permukaan yang licin, mudah dibersihkan, tanpa tepi tajam. g. Aksesibiliti: Mengikut piawaian reka bentuk universal (Universal Design) seperti yang disarankan oleh pihak berkuasa tempatan. Ini mungkin termasuk ketinggian yang berbeza untuk kanak-kanak dan akses bagi kerusi roda.`
- contoh: `Unit pancutan air yang moden dan bersih, biasa ditemui di taman-taman bandar utama seperti KLCC Park atau Taman Botani Perdana, Kuala Lumpur.`
- source_image_or_figure: asset `K5PL06T03-B02-IMG-p248-x49`, module p. 248, physical 267, 273 × 349 jpeg
- image_ownership_evidence: image at p248 y 200.0–446.7, inside the table (y 56.5–740.5), upper band → row 1. Preceding heading is Drinking Fountain (p247 y 537.2); no heading intervenes on p248
- proposed_level_2_item_label: **`Pancutan Air Minum Keluli Tahan Karat`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `TYPOGRAPHIC` (trailing colon removed) + `STRUCTURAL_SPLIT_OF_LABEL_CELL`
- normalisation_reason: colon is a separator, not part of the name; `Contoh:` clause routed per I-1 §3.2
- ambiguity_or_human_review: seven lettered sub-fields — the richest spec cell in the inventory. `REVIEW_REQUIRED` at Stage 2 for popup display budget, **not** for splitting (sub-fields, not records)
- evidence_reference: I-2 p267 tbl0 r1; I-2 p267 image xref 49; I-6 row 12

**`K5-PL06-T03-B02-DRINKING-FOUNTAIN-ROW-02`**
- source_row_order: 2 · printed_module_page: **248–249** (starts p248, continues p249) · physical_pdf_page: **267–268**
- source_row_label: `Pancutan Air Minum Konkrit/BatuContoh: Unit yang lebih berat dan kukuh, disepadukan dengan reka bentuk taman yang lebih semula jadi atau tradisional.`
- jenis_bahan: `Pancutan Air Minum Konkrit/Batu`
- fungsi_penerangan: `a. Bahan: Struktur asas dari konkrit bertetulang atau batu asli/tiruan. Bahagian pancutan air (faucet/basin) biasanya masih keluli tahan karat untuk kebersihan. b. Piawaian Kesihatan: Mesti mematuhi piawaian kualiti air minuman yang ditetapkan oleh Kementerian Kesihatan Malaysia atau badan berkaitan.`
- contoh: `Unit yang lebih berat dan kukuh, disepadukan dengan reka bentuk taman yang lebih semula jadi atau tradisional.`
- source_image_or_figure: asset `K5PL06T03-B02-IMG-p249-x56`, module p. 249, physical 268, 344 × 344 jpeg
- image_ownership_evidence: **the second boundary case.** Image at p249 y 56.6–248.6. The `3.4.3 BBQ pit` heading is at p249 y 274.3 — **below** the image — and the BBQ Pit table does not begin until y 419.1. The image therefore belongs to the Drinking Fountain content continuing from p248, i.e. this row. **Determined by heading position, not page number**
- proposed_level_2_item_label: **`Pancutan Air Minum Konkrit/Batu`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: `STRUCTURAL_SPLIT_OF_LABEL_CELL`
- normalisation_reason: `Contoh:` clause routed per I-1 §3.2
- ambiguity_or_human_review: `NONE` — boundary resolved by measurement. This measurement **supersedes** the directed asset list that placed Drinking Fountain images on pp. 247–248; see §6 A-03
- evidence_reference: I-2 p267 tbl0 r2; I-2 p268 image xref 56; I-6 row 13

---

#### Component 9 — BBQ Pit

Heading at module p. 249, y = 274.3, rendered **Arial,Italic** and spelled `BBQ pit` (lowercase `p`) in
the source. Table at p. 249, y = 419.1–776.2, 2 columns, 1 header + 1 data row; the row continues onto
p. 250. Example screen title: **`Contoh BBQ Pit`**.

> ⚠ **Single-item example screen** — same consequence as Papan Tanda. See §6 A-05.

**`K5-PL06-T03-B02-BBQ-PIT-ROW-01`**
- source_section: `3.4.3 BBQ pit` · source_table_title: `CONTOH | SPESIFIKASI`
- source_row_order: 1 · printed_module_page: **249–250** (starts p249, continues p250) · physical_pdf_page: **268–269**
- source_row_label: `BBQ Pit Struktur Kekal (Bata/Konkrit/Batu)Contoh: Lubang barbeku yang dibina tetap di taman perumahan, tapak perkhemahan awam, atau kawasan rekreasi keluarga seperti di Taman Rekreasi Bukit Jalil, Kuala Lumpur.`
- jenis_bahan: `BBQ Pit Struktur Kekal (Bata/Konkrit/Batu)`
- fungsi_penerangan: `a. Bahan Pembinaan: i. Dinding Dalam Ruang Pembakaran: Menggunakan bata tahan api (firebrick) atau blok konkrit yang tahan suhu tinggi. Mortar yang digunakan mestilah mortar tahan api. ii. Dinding Luar/Kemasan: Bata biasa, blok konkrit, atau batu semula jadi/tiruan. iii. Pelat/Permukaan Kerja: Konkrit, jubin seramik tahan haba, atau batu granit/marble. b. Dimensi Umum: i. Ketinggian Memanggang: Lazimnya 750-900mm dari aras tanah ke permukaan gril untuk keselesaan pengguna. ii. Saiz Lubang Api: Bergantung pada saiz gril yang digunakan, memadai untuk arang atau kayu bakar. c. Gril/Jeriji Memanggang: Bahan: Keluli tahan karat gred makanan atau besi tuang (cast iron) yang tahan karat dan haba tinggi. Ciri-ciri: Boleh laras ketinggian atau tetap. Tebal palang minimum 6mm. d. Ciri-ciri Keselamatan & Fungsi: Pengudaraan: Celah udara atau lubang di bahagian bawah ruang pembakaran untuk memastikan pembakaran yang cekap. Saliran: Lubang kecil di dasar ruang pembakaran untuk saliran air hujan. Cerobong Asap (Pilihan): Jika BBQ pit dibina dalam struktur bertutup atau di kawasan berdekatan tempat duduk. Ruang Persediaan: Permukaan kerja bersebelahan BBQ pit untuk menyediakan makanan atau meletakkan perkakas. Jarak Selamat: Rekaan yang memastikan jarak minimum dari bahan mudah terbakar (contohnya, pagar kayu, tumbuhan kering) mengikut piawaian keselamatan kebakaran.`
- contoh: `Lubang barbeku yang dibina tetap di taman perumahan, tapak perkhemahan awam, atau kawasan rekreasi keluarga seperti di Taman Rekreasi Bukit Jalil, Kuala Lumpur.`
- source_image_or_figure: asset `K5PL06T03-B02-IMG-p249-x57`, module p. 249, physical 268, 436 × 327 jpeg
- image_ownership_evidence: image at p249 y 578.5–735.6, inside the BBQ Pit table (y 419.1–776.2) and **below** the `3.4.3 BBQ pit` heading at y 274.3. Unambiguous
- proposed_level_2_item_label: **`BBQ Pit Struktur Kekal`**
- popup_required: **YES** · inclusion_status: **INCLUDED** · exclusion_reason: `NOT_APPLICABLE`
- normalisation_applied: **`CASE`** — component and item use `BBQ Pit` with capital `P`
- normalisation_reason: I-1 §7 mandates learner-facing `BBQ Pit` "unless the final lexicon explicitly reverts to source case". The **section heading** reads `BBQ pit`; the **table row already reads `BBQ Pit`**, so the table agrees with the S&G and only the heading differs — see N-08. This reverses the direction carried in storyboard v0.1; see §6 A-02
- ambiguity_or_human_review: **`REVIEW_REQUIRED` — proposed split, flagged and NOT applied.** Four lettered sub-fields, two with roman sub-items. A defensible alternative is 4 Level 2 items (Bahan Pembinaan / Dimensi Umum / Gril / Ciri-ciri Keselamatan). **Not applied** — these are sub-fields describing one BBQ pit type, not four independent records
- evidence_reference: I-2 p268 tbl0 r1; I-2 p268 image xref 57; I-2 p269 tbl0 r0 (continuation); I-6 row 14

---

# 5. Exclusion register

## 5.1 How to read this register

**No meaningful source row was excluded.** All 26 carry `popup_required = YES`.

This register lists the **table elements that are not meaningful rows** — the physical rows in the
rendered source that carry no instructional content. They are enumerated so that the difference
between "26 meaningful rows" and "40 physical row instances" is auditable, and so that nobody later
mistakes a repeated header for lost content.

**`ROWS_EXPLICITLY_EXCLUDED` in §7 counts excluded *meaningful* rows, and is therefore 0.** The
invariant in §7 operates on meaningful rows only. The elements below sit outside that set by
definition.

## 5.2 Register — 14 rendered elements + 7 extraction artifacts

| # | Element | Component | Mod p | Reason |
|---|---|---|:-:|---|
| E-01 | Header row `JENIS STRUKTUR \| FUNGSI & PENERANGAN \| CONTOH` | Struktur Persisir Air | 238 | decorative table heading |
| E-02 | Header row `JENIS STRUKTUR \| FUNGSI & PENERANGAN \| CONTOH` | Struktur Teduhan | 239 | decorative table heading |
| E-03 | Header row `CONTOH \| PENERANGAN` | Kemudahan Awam | 240 | decorative table heading |
| E-04 | Header row `CONTOH \| PENERANGAN` | Water Feature | 241 | decorative table heading |
| E-05 | Header row `CONTOH \| SPESIFIKASI` | Kerusi Taman | 242 | decorative table heading |
| E-06 | Header row `CONTOH \| SPESIFIKASI` — **repeat** on the continuation page | Kerusi Taman | 243 | decorative table heading, repeated by page-break rendering |
| E-07 | Header row `CONTOH \| SPESIFIKASI` | Papan Tanda | 244 | decorative table heading |
| E-08 | Header row `CONTOH \| SPESIFIKASI` | Tong Sampah | 246 | decorative table heading |
| E-09 | Header row `CONTOH \| SPESIFIKASI` — **repeat** on the continuation page | Tong Sampah | 247 | decorative table heading, repeated by page-break rendering |
| E-10 | Header row `CONTOH \| SPESIFIKASI` | Drinking Fountain | 248 | decorative table heading |
| E-11 | Header row `CONTOH \| SPESIFIKASI` | BBQ Pit | 249 | decorative table heading |
| E-12 | 1-row table fragment, p241 y 56.4–88.6, text `geologi) melalui pameran, paparan, atau papan tanda.` | Kemudahan Awam | 241 | **duplicate continuation row** — tail of `Bangunan Interpretatif`, already carried whole in `…-KEMUDAHAN-AWAM-ROW-03` |
| E-13 | Empty row, p247 table row index 1, no extractable cell text | Tong Sampah | 247 | **empty formatting row** produced by the page-break continuation of `Tong Sampah Konkrit/Batu` |
| E-14 | 1-row table fragment, p250 y 56.3–676.1, text beginning `ii. Saiz Lubang Api: …` | BBQ Pit | 250 | **duplicate continuation row** — tail of `BBQ Pit Struktur Kekal`, already carried whole in `…-BBQ-PIT-ROW-01` |
| E-15 | Leading empty markdown row `\| \| \|` emitted by the DOCX-to-text conversion for 7 of the 9 tables (all except Kerusi Taman and Tong Sampah) | 7 components | — | **extraction artifact, not a source row.** Absent from the rendered PDF (I-2). Recorded so it is never mistaken for an empty source row; see §6 A-09 |

**Reconciliation.** 26 meaningful rows + 11 header rows + 3 continuation/empty rows = **40 physical row
instances** in the rendered source (I-2). The 7 items under E-15 exist only in the derived text
extraction (I-3a) and have no counterpart in the rendered source.

No element was excluded for being "not useful". Every exclusion is a structural property of the source
layout — a heading, a page-break artifact, or a conversion artifact.

---

# 6. Anomalies and source issues

**No contradiction below is resolved silently.** Each records what was found, what was done, and what
still needs a human decision.

## A-01 — Two S&G documents exist and they conflict on two points · **UNRESOLVED**

| | |
|---|---|
| I-1 | `Updated S&G v0.2`, evidence date 31 July 2026, scope **K5 PL06 T03 B02**, authority Bariah |
| I-12 | `S&G Storyboard Development`, `Versi 1.0 \| Julai 2026`, scope **all five CIDB courses** |

Both are live documents with overlapping authority. Two direct conflicts:

1. **Rumusan structure.** I-12 §5.5.1 requires *"Kepentingan → Apa Yang Telah Dipelajari → Manfaat"* as
   a mandatory three-component structure. I-1 §6.5 requires *"Do not display labels such as
   Kepentingan, Isi Utama or Manfaat"*. **Directly opposed.**
2. **Narrator prefix.** I-12 §5.3 describes narrator VO without a speaker-label convention; I-1 §5.2
   requires `"Hilmi:"` on S03 and forbids it elsewhere.

**Treatment here:** I-1 governs, because it is scope-specific to K5 PL06 T03 B02, dated later, and
records Bariah's review directly. **This precedence is asserted for this inventory only and needs
confirmation before Stage 2.** I-12 §2.2 does independently corroborate two facts used here: Hilmi is
the narrator for Kursus 5, and the Kursus 5 character set is still to be confirmed with the SME.

## A-02 — S&G v0.2 reverses storyboard v0.1 on three points · **RECORDED**

| Point | Storyboard v0.1 (I-4) | S&G v0.2 (I-1) | Effect on this inventory |
|---|---|---|---|
| `BBQ pit` case | lowercase `p`, source form, verified | **`BBQ Pit`** capital `P`, §7 | applied — N-08 |
| `Hilmi:` VO prefix | none anywhere; verified 0 occurrences | **required on S03 only**, §5.2 | none — S03 is out of Stage 1 scope |
| Completion-state notes | `[VO SENGAJA KOSONG …]` placeholder | **genuinely empty Notes**, §5.2 | none in Stage 1; Stage 2 must strip the placeholder |

Also superseding: I-1 §5.1 forbids `"VO PENUH:"` and `"S05 - PERINCIAN"`-style technical prefixes in
final Speaker Notes. Storyboard v0.1 uses both. **A regeneration concern, recorded here so it is not
lost between stages.**

## A-03 — Image ownership at the pp. 247–249 boundary · **RESOLVED BY MEASUREMENT**

The confirmed boundary issue is now settled with positional evidence rather than page arithmetic.

| Asset | Mod p | Image y | Governing heading | Owner |
|---|:-:|---|---|---|
| `…IMG-p247-x44` | 247 | 73.0–247.0 | `3.4.2 Drinking Fountain` at y **537.2** → image is above it | **Tong Sampah** (Konkrit/Batu) |
| `…IMG-p247-x45` | 247 | 376.5–511.3 | same | **Tong Sampah** (Plastik HDPE) |
| `…IMG-p247-x46` | 247 | 376.5–510.9 | same | **Tong Sampah** (Plastik HDPE) |
| `…IMG-p248-x49` | 248 | 200.0–446.7 | no heading intervenes on p248 | **Drinking Fountain** (Keluli Tahan Karat) |
| `…IMG-p249-x56` | 249 | 56.6–248.6 | `3.4.3 BBQ pit` at y **274.3** → image is above it | **Drinking Fountain** (Konkrit/Batu) |
| `…IMG-p249-x57` | 249 | 578.5–735.6 | below the BBQ heading, inside the BBQ table | **BBQ Pit** |

**Confirmed:** images above the `3.4.2` heading belong to Tong Sampah; Drinking Fountain's images are
on pp. **248–249**, not 247–248. This supersedes the directed asset list. Same 14 assets either way —
only the two boundary images move. **No residual ambiguity: all 14 assets have an unambiguous
heading-relative position.**

## A-04 — Two components have no source image at all · **CONFIRMED ABSENCE**

| Component | Mod p | Evidence |
|---|:-:|---|
| Kemudahan Awam | 240 | `3.3.3` at y 320.0; the only p240 image is at y 57.6–268.1, above it, and belongs to Struktur Teduhan. **p241 carries no image whatsoever** |
| Water Feature | 241 | `3.3.4` at y 112.0; **zero embedded images on p241** |

Confirmed absences in the rendered PDF, not extraction failures. **6 of the 26 rows** (3 + 3) therefore
have no source visual. Under I-1 §3.2 these need a textual visual direction or an approved native
diagram specification — and **must not** be filled with fabricated external visual content.

## A-05 — Two components yield a single Level 2 item · **REVIEW_REQUIRED**

`Papan Tanda` and `BBQ Pit` each have exactly **one** meaningful row, so each `Contoh …` example screen
would carry one clickable item. Under I-1 §4.3 `Kembali` unlocks once "all example items" are viewed,
which one click satisfies. The interaction is valid but degenerate.

Both spec cells are internally structured — lettered fields `a.`–`d.`, with roman sub-items — verified
in the PDF text layer. A split is arguable:

| Component | Current | Alternative split | Why not applied |
|---|:-:|:-:|---|
| Papan Tanda | 1 item | 6 (4 panel materials + 2 post materials) | the lettered structure marks sub-fields of one sign specification, not six independent sign types |
| BBQ Pit | 1 item | 4 (Bahan Pembinaan / Dimensi Umum / Gril / Keselamatan) | the same — four aspects of one BBQ pit type |

**Neither split is applied.** The task rule is explicit: do not split one source row into several popup
items unless the source itself clearly contains independent records; any proposed split must be marked
for human review. **Marked. Bariah/ID decision required before Stage 2.**

## A-06 — Structural variance across the nine source tables · **RECORDED**

| Variance | Components |
|---|---|
| 3-column `JENIS STRUKTUR \| FUNGSI & PENERANGAN \| CONTOH` | Struktur Persisir Air, Struktur Teduhan |
| 2-column `CONTOH \| PENERANGAN` — **no Jenis/Bahan column** | Kemudahan Awam, Water Feature |
| 2-column `CONTOH \| SPESIFIKASI` — label cell packs name + `Contoh:` clause | Kerusi Taman, Papan Tanda, Tong Sampah, Drinking Fountain, BBQ Pit |

Only two of nine tables carry all three of I-1 §3.2's named fields as distinct columns. For the
`CONTOH | PENERANGAN` tables the item label is drawn from `CONTOH`; for the `CONTOH | SPESIFIKASI`
tables the packed label cell is split into `jenis_bahan` + `contoh` without altering any text.
`Struktur Teduhan` additionally has **no `Aspek Pembinaan` prose block** — the only subsection in 3.3
lacking one, which thins its main explanation screen.

## A-07 — Duplicate subsection numbering · **CONFIRMED IN RENDERED SOURCE**

`3.4.1` occurs **three times** in the rendered PDF text layer — for `Kerusi Taman`, `Papan Tanda` and
`Tong Sampah`. `3.3.1`–`3.3.4`, `3.4.2` and `3.4.3` each occur once.

Screens and rows here are keyed by heading **title**, which is unique, so the collision does not affect
any mapping. **It does mean a numeric section reference is not a safe locator for this bahagian** —
production metadata must cite the title and page, never the number alone.

## A-08 — Level 2 item label length has no governing budget · **REVIEW_REQUIRED**

Proposed labels range from 4 characters (`Jeti`) to 44 (`Papan Tanda Arah / Papan Tanda Interpretatif`).
The 24-character ceiling measured for the Level 1 card family does not transfer — Level 2 items are a
new layout that does not yet exist. Two labels were already shortened for display
(`…-TONG-SAMPAH-ROW-01`, and the material qualifier on `…-TONG-SAMPAH-ROW-03` retained in full at 39
characters). **A label budget must be set when the Level 2 layout is designed.** Full source forms are
preserved in every record, so nothing is lost either way.

## A-09 — DOCX text extraction emits phantom empty header rows · **RESOLVED**

The derived extraction I-3a renders 7 of the 9 tables with a leading `|  |  |` row that does **not**
exist in the rendered source (I-2). Cross-checking every table against the PDF establishes that these
are conversion artifacts. Recorded as E-15 so a later reader does not count them as empty source rows.

**This is why the PDF is the row-structure authority and the DOCX the text authority.** Row counts in
this document come from I-2; cell wording comes from I-3a and was verified against I-2.

## A-10 — Source module could not be hashed locally · **ACCEPTED LIMITATION**

See the note under I-3 in §1.3. Identity pinned by Drive fileId, byte size and modifiedTime — all three
matching the earlier session's record. Every claim in §4 is independently supported by I-2, which is
hashed.

## A-11 — Mixed-language and typographic defects in source · **RECORDED, NOT SILENTLY FIXED**

| # | Defect | Location | Treatment |
|---|---|---|---|
| N-01 | `Promenande` → `Promenade` | section heading, mod p238 | **normalise** per I-1 §7. The table row already reads `Promenade`, so only the heading is affected |
| N-02 | `footbridge` lowercase in heading; `Footbridge` in table row | mod p238 | table form adopted; heading form recorded |
| N-03 | Row cell begins lowercase `struktur teduhan…` | Teduhan ROW-05, mod p239 | sentence case **proposed, not applied** — Stage 2 authoring decision |
| N-04 | `bangunan interpretative` (English) in prose vs `Bangunan Interpretatif` (Malay) in table | mod p240 | table form adopted for the item label; both forms are source-attested and recorded |
| N-05 | `Kolam Renang/Kolam Hiasan Besar(Pool)` — missing space | Water Feature ROW-03, mod p241 | typographic normalisation applied to the label; source form preserved verbatim in the record |
| N-06 | `Kerusi KompositContoh: … Plastik Kitar Semula):` — **unbalanced parenthesis** | Kerusi Taman ROW-03, mod p243 | **not corrected.** Two readings possible; guessing would change meaning. `REVIEW_REQUIRED` |
| N-07 | Tier-2 English terms have no italic rule | throughout — `WPC`, `HDPE`, `pressure-treated`, `stainless steel`, `precast concrete`, `firebrick`, `cast iron`, `Universal Design`, `push-button valve`, `shut-off valve`, `exposed aggregate`, `mortise and tenon joints`, and others | **unresolved.** I-1 §7 mandates italic for "English-origin learner-facing terms" but the working lexicon is closed at three (`Water Feature`, `Drinking Fountain`, `BBQ Pit`). The source itself italicises exactly those three section headings and no others — see A-12. Roughly a dozen Tier-2 terms sit outside any rule |
| N-08 | `BBQ pit` (source heading) vs `BBQ Pit` (source table row and I-1 §7) | mod p249 | **`BBQ Pit` adopted** per I-1 §7. Note the source is internally inconsistent: heading lowercase, table row capitalised |
| N-09 | Trailing colons in packed label cells | Tong Sampah ROW-02, Drinking Fountain ROW-01 | punctuation removed from item labels only; source forms preserved verbatim |
| N-10 | `Rajah 25:  Contoh …` — double space after colon | mod p245 | typographic, recorded; affects a caption, not a row |
| N-11 | `rekabentuk` unspaced in the `Tips Penting` bullets vs `reka bentuk` elsewhere | mod p241 | I-1 §7 mandates the spaced form; the affected text is prose, not a table row |

## A-12 — The italic lexicon has a source basis · **NEW EVIDENCE**

Font analysis of the rendered PDF shows the source itself sets exactly three section headings in
`Arial,Italic` — `Water Feature (Fountain, Pond, Pool)` (p241), `Drinking Fountain` (p247) and
`BBQ pit` (p249). Every other component heading is roman `Arial`.

**The three-term lexicon is therefore source-derived, not an editorial invention.** This is the first
positive evidence for it and it strengthens the case for keeping the lexicon closed at three (N-07).

---

# 7. Coverage totals

**Read §8.3 first: `SOURCE_ROW_COUNT` and `PROPOSED_INTERACTION_ITEM_COUNT` are different quantities
that currently share the value 26. Every count below is a source-evidence count.**

```
COMPONENTS_EXPECTED              =  9
COMPONENTS_INVENTORIED           =  9
SOURCE_ROW_COUNT                 = 26   ← frozen source-evidence count
MEANINGFUL_ROWS_FOUND            = 26   ← same quantity, Stage 1 field name
PROPOSED_INTERACTION_ITEM_COUNT  = 26   ← implementation proposal, may change under ruling
ROWS_MAPPED_TO_POPUPS            = 26
ROWS_EXPLICITLY_EXCLUDED         =  0
UNRESOLVED_ROWS                  =  0
DUPLICATE_ROW_MAPPINGS           =  0
ROWS_WITHOUT_PAGE_LOCATOR        =  0
ROWS_WITHOUT_POPUP_LABEL         =  0
ROWS_WITHOUT_SOURCE_PROPOSITIONS =  0
```

**Invariant check**

```
MEANINGFUL_ROWS_FOUND  =  ROWS_MAPPED_TO_POPUPS + ROWS_EXPLICITLY_EXCLUDED + UNRESOLVED_ROWS
                  26   =            26           +            0            +        0
                  26   =            26                                          ✅ HOLDS
```

## 7.1 Supporting counts

| Metric | Value |
|---|---:|
| Physical table-row instances in the rendered source | 40 |
| — meaningful data rows | 26 |
| — header rows (11, incl. 2 page-break repeats) | 11 |
| — continuation / empty formatting rows | 3 |
| Extraction artifacts (derived text only, absent from rendered source) | 7 |
| Level 2 items proposed | 26 |
| Popup states required | 26 |
| Example screens required (`Contoh [Nama Komponen]`) | 9 |
| Main explanation screens required | 9 |
| Source assets registered and assigned | 14 |
| Rows with ≥ 1 source image | 12 |
| Rows with no source image | 14 |
| Components with **no** source image at all | 2 (Kemudahan Awam, Water Feature) |
| Rows flagged `REVIEW_REQUIRED` | 3 (Papan Tanda ROW-01 split, BBQ Pit ROW-01 split, Kerusi Taman ROW-03 parenthesis) |
| Proposed splits **flagged and not applied** | 2 |

## 7.2 Validation performed on this matrix

Re-read after generation; each check run against the finished §4.

| # | Check | Result |
|---|---|:-:|
| 1 | Duplicate `provisional_row_id` values | **0** — 26 IDs, all distinct |
| 2 | Duplicate `component + source_row_order` pairs | **0** — each component's orders run 1..n with no repeat |
| 3 | Missing page locators | **0** — every row carries printed module page and physical PDF page |
| 4 | Rows `INCLUDED` without `popup_required = YES` | **0** |
| 5 | Exclusions without a reason | **0** — all 15 register entries carry a structural reason; none says "not useful" |
| 6 | All nine components present | **9/9** |
| 7 | Rows without a proposed Level 2 item label | **0** |
| 8 | Rows without source propositions | **0** |
| 9 | Ambiguous blank cells | **0** — `NOT_PRESENT_IN_SOURCE` or `REVIEW_REQUIRED` used throughout |
| 10 | Row counts cross-verified PDF ↔ DOCX | **9/9 tables agree** |
| 11 | Asset assignment complete | **14/14**, none orphaned |
| 12 | No PPTX / generator / schema / unrelated artifact changed | **confirmed** — `git status` shows only this untracked file |

---

# 8. IMPLEMENTATION AUTHORITY STATUS

```
SOURCE_TABLE_INVENTORY_COMPLETE
NOT_READY_FOR_SCREEN_STATE_MAP_PENDING_AUTHORITY_RULINGS
```

## 8.1 What is complete

- **All nine learning components are inventoried** — prose section and source table located for each.
- **26 meaningful source rows are inventoried**, in source order, each with a stable provisional
  source-mapping ID.
- **Row identity is complete** — 26 IDs, all unique, no duplicate `component + source_row_order` pair.
- **Source locators are complete** — every row carries a printed module page and a physical PDF page.
- **Image ownership is complete** — all 14 registered assets are assigned by heading-relative position;
  none is orphaned; the pp. 247–249 boundary is resolved by measurement (§6 A-03).

## 8.2 What this artifact is

**This matrix is a source-evidence artifact. It is not yet the governing screen/state contract.**

It records what the approved module contains and where. It does not, and must not, decide how that
content is segmented into screens, states or interaction items.

Two fields in §4 are **implementation-facing, not source-facing**:

| Field | Standing |
|---|---|
| `popup_required` | Reflects the **B02-specific Updated S&G v0.2 interpretation** — I-1 §3.1, "each meaningful row → one clickable Level 2 item; each item → one popup". **Provisional.** |
| `proposed_level_2_item_label` | Derived under I-1 §3.2 from the row's `Jenis / Bahan` (or `CONTOH` where no Jenis column exists). **Provisional.** |

Both remain provisional until (a) contract reconciliation between I-1 and I-12 is recorded, and
(b) the A-05 and A-06 rulings are recorded. Until then they are a **proposal traceable to a named
specification clause**, not an instruction to the generator.

## 8.3 Two counts that must never be conflated

```
SOURCE_ROW_COUNT               = 26     ← source-evidence count. FROZEN.
PROPOSED_INTERACTION_ITEM_COUNT = 26    ← implementation proposal. May change under ruling.
```

`SOURCE_ROW_COUNT` is a property of the approved module. It changes only if a **demonstrable
extraction error** is found — not because a design decision is taken.

`PROPOSED_INTERACTION_ITEM_COUNT` is a property of the screen/state design. It may resolve to a
different number under A-05, A-06 or contract reconciliation.

**A complex source row may later map to one, several or no separate interaction items. That is a
screen/state ruling and it does not rewrite source identity.** Concretely: if A-05 Option B is
adopted, `PROPOSED_INTERACTION_ITEM_COUNT` could rise (Papan Tanda 1 → up to 6, BBQ Pit 1 → up to 4),
while **`SOURCE_ROW_COUNT` stays 26** and `…-PAPAN-TANDA-ROW-01` and `…-BBQ-PIT-ROW-01` remain single
source rows with unchanged IDs.

> **Correction to the Stage 1 text this section replaces.** The superseded §8.1 stated that an A-05
> split would take `MEANINGFUL_ROWS_FOUND` from 26 to 34. That was wrong: it conflated an interaction
> ruling with a source-evidence count. Interaction splits do **not** create source rows.

## 8.4 Status separation

```
ROW_MAPPING_UNRESOLVED = 0
```

Every meaningful source row is mapped exactly once. There is no unresolved *mapping*. This is a
closed, mechanical result.

```
AUTHORITY_OR_DESIGN_RULINGS_PENDING = 12
```

| ID | Pending item | Required authority |
|---|---|---|
| `R-1` | VO source fidelity — verbatim-module vs concise-display reconciliation | Bariah (instructional) |
| `R-2` | Popup VO requirement — whether every popup carries VO | Bariah (instructional) |
| `R-3` | Physical status slides versus state model | Firdaus / CAIR (technical contract) |
| `R-4` | Per-Topik versus per-Bahagian closing structure (Rumusan / Kuiz / Tamat) | Bariah + course navigation owner |
| `R-5` | `Kembali` target, label and gating | Bariah (instructional) + CAIR (contract) |
| `R-6` | Rumusan display structure and language register | Bariah (instructional) |
| `L-01` | "PL satu", not "PL kosong satu" — VO pronunciation note | Bariah (instructional) |
| `L-02` | Mind Map requirement on S03 | Bariah (instructional) |
| `A-05` | Single-row example-screen treatment (Papan Tanda, BBQ Pit) | Bariah (interaction) → Firdaus / CAIR (adoption) |
| `A-06` | Heterogeneous table-field mapping | CAIR (technical schema) unless content gaps require Bariah |
| `A-09` | PDF versus DOCX row-structure precedence | Firdaus / CAIR (source-precedence ruling) |
| `N-06` | Normalisation declined — unbalanced parenthesis in `…-KERUSI-TAMAN-ROW-03` | Bariah (source/content) |

Evidence for every item above is in `B02_PRE_STAGE2_RULING_EVIDENCE.md`. **No ruling is selected in
either document.**

## 8.5 Outstanding integrity blocker

```
BLOCKED_MODULE_DOCX_INTEGRITY_NOT_VERIFIED
```

The exact bytes of the approved module DOCX (I-3) have not been cryptographically hashed. See the note
under §1.3 and the four-route attempt log in `B02_PRE_STAGE2_RULING_EVIDENCE.md` §B. This is
independent of the ruling backlog and blocks Stage 2 adoption on its own.

## 8.6 Standing

Nothing in this document is a governance decision, a canonical ID, a screen ID, a popup implementation
ID, or a production authority. K5 remains locked and the live CAIR decision desk is untouched.
