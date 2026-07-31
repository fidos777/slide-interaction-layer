# BARIAH_REVIEW_INGEST

Phase B1 — read-only ingest of the verified Bariah review deck.
Evidence only. Not source authority. Not compiler input. Not a baseline. Not production-authorised.

---

## 0. Origin attribution and custody lineage

### 0.1 Custody confirmation — `MEASURED_FACT`

| Property | Measured value | Locus |
|---|---|---|
| Resolved path | `/root/.claude/uploads/12837c42-b6ab-597b-8301-85c5b457471b/3f626ac5-BARIAH_REVIEW_8SLIDES.pptx` | filesystem |
| Byte size | 68,710 | `stat` |
| SHA-256 | `ee4f54790bd22afb82457237d63d290eb6ac0ceabbead88ec5f7d7fced8bb9e7` | `sha256sum` |
| Slide count | 8 | `ppt/slides/slide1..8.xml`; `docProps/app.xml → <Slides>8</Slides>` |
| Notes count | 7 | `docProps/app.xml → <Notes>7</Notes>` |
| `lastModifiedBy` | `Bariah Ahmad` | `docProps/core.xml` |
| `changesInfo1.xml` | present, 22,856 bytes | `ppt/changesInfos/changesInfo1.xml` |

Re-verified after extraction: package hash unchanged. **No byte of the PPTX was modified.**
All reads were streaming (`unzip -p`, `unzip -q` to a scratchpad copy). The scratchpad copy was never written back.

### 0.2 Package self-description contradicts its own content — `MEASURED_FACT`

`docProps/core.xml`:

- `dc:title` = `Contoh Treatment — 4 slaid — bukan storyboard penuh`
- `dc:subject` = `Treatment probe. Not a storyboard. Output-only, disposable.`
- `dc:creator` = `SMEC courseware.my`
- `cp:keywords` = `storyboard; K5; source-bound`
- `dc:description` = `Hand-built from 4 slides of the Tier-1 storyboard specification. Not regenerable, not a baseline, must never be promoted.`
- `cp:category` = `Storyboard Specification`
- `cp:revision` = `1`
- `dcterms:created` = `2021-11-01T02:42:52Z`
- `dcterms:modified` = `2026-07-29T23:13:59Z`

The title still declares **4 slides**; the package contains **8**. Section 2 below shows this is not an
error — the title describes the *probe base*, and the four extra slides are Bariah's additions layered
on top without the title being refreshed. The stale title is therefore corroborating evidence, not noise.

### 0.3 Toolchain lineage — `MEASURED_FACT`

`docProps/app.xml`: `Application = Microsoft Office PowerPoint`, `AppVersion = 16.0000`,
`TotalTime = 87` (minutes), `Words = 1154`, `Paragraphs = 147`, `PresentationFormat = Widescreen`.

Fonts declared: Arial, Calibri, Ebrima, Raleway, Roboto Light.
Theme (`ppt/theme/theme1.xml`): `majorFont/latin = Raleway`, `minorFont/latin = Ebrima`.

`ppt/revisionInfo.xml`: single client `{2B3460C8-3DFB-41D1-B96C-0E2B89D95DBA}`, `v=31`,
`dt=2026-07-29T23:07:29.482`.

Stage size `p:sldSz cx=12192000 cy=6858000` → **13.3333 × 7.5 in**. `MEASURED_FACT`

### 0.4 Provenance carried from an unrelated iSpring project — `MEASURED_FACT`

`ppt/tags/tag1.xml` (presentation-level, bound via `p:custDataLst/p:tags r:id="rId11"`) carries
23 tags whose payload describes **PL06 Topik 3 B2**, not the K5 B02 job this artifact is being read
against. See `SME_RULE_CHECKABILITY.md §7` for the full enumeration and survival analysis.
Course identifiers embedded: `MMD_KAK_PL1_T1_1_B1_V2`, `MMD_KAK_PL1_T6_T3_B2_V4`,
`ISPRING_PRESENTATION_PATH = D:\KERJA DANIEL\CIDB CYCLE 6 KAK\MMD\PL 06\Topik 3\B2\MMD_KAK_PL6_T3_B2_V4.pptx`.

`ISPRING_PRESENTATION_INFO_2` lists **14 slide GUIDs** — the deck this tag block was authored against
had 14 slides, not 4 and not 8. The tag block is inherited debris from a donor file. `MEASURED_FACT`

---

## 1. Diff against probe v0.1 and v0.2

### 1.1 The probe revisions are not present in this session — `NOT_DETERMINABLE`

Exhaustive filesystem sweep (`find / -xdev`, excluding `/proc`, `/sys`, package caches) returns
**exactly one** `.pptx` or `.potx` on this machine: the reviewed deck itself. Likewise absent:

| Artifact named in the task | Present? |
|---|---|
| probe v0.1 — `24dcaa04…1d471c` | **absent** |
| probe v0.2 — `75f8b168…c15045` | **absent** |
| canonical `SB_K4PL3T2_v1.2.pptx` | **absent** |
| authoritative 19-slide K5 B02 Tier-1 specification | **absent** |
| `packet_B02.json` | **absent** |
| `asset_manifest.json` | **absent** |

Only the two SHA-256 digests for the probes were supplied. A digest permits an equality test against a
file in hand; it cannot reconstruct content, so no diff, no byte comparison, and no shape-tree comparison
against either probe revision is possible.

**Every cross-artifact requirement in task items 1, 4, 5, and the packet-scoped halves of items 5 and 6
is therefore blocked at the evidence layer, not at the reasoning layer.**

What follows instead is a diff derived entirely from **inside** the package: PowerPoint's own
co-authoring change log, `ppt/changesInfos/changesInfo1.xml`, which records what Bariah did to a base
deck during the editing session. This is weaker than a two-file diff — it cannot show the base's
*content* — but it does discriminate base slides from added slides with high confidence.

### 1.2 Method and its limits — `MEASURED_FACT`

`changesInfo1.xml` root `pc:chgInfo` contains one `pc:docChg` with
`chg="undo redo custSel addSld delSld modSld sldOrd"`, 7 `pc:sldChg` records, 52 `pc:spChg`,
4 `pc:picChg`. Slide identity in the log is `pc:sldMk/@sldId`, which joins directly to
`ppt/presentation.xml → p:sldIdLst`.

Limit to state plainly: a slide with **no** `sldChg` record was not touched in the recorded session.
That is not the same as proving it is byte-identical to a probe revision — the log could in principle
have been truncated, and any editing that happened *before* this change log began is invisible. The
inference is strong, not absolute. `MEASURED_FACT` (the absence); the lineage reading built on it is
labelled where it becomes inference.

---

## 2. The exact 4-to-8 slide mapping — `MEASURED_FACT`

`p:sldIdLst` order → `sldId` → change-log verdict:

| Pos | Part | `sldId` | `sldChg/@chg` | Verdict |
|---:|---|---:|---|---|
| 1 | `slide1.xml` | 9003 | *(no record)* | **BASE — untouched** |
| 2 | `slide2.xml` | 9020 | `addSp delSp modSp new mod` | **NEW — Bariah-created** |
| 3 | `slide3.xml` | 9019 | `addSp delSp modSp add mod modNotesTx` | **INSERTED — Bariah** |
| 4 | `slide4.xml` | 9011 | `addSp delSp modSp mod ord modNotesTx` | **BASE — edited in place, reordered** |
| 5 | `slide5.xml` | 9008 | `addSp delSp modSp mod ord` | **BASE — rebuilt in place, reordered** |
| 6 | `slide6.xml` | 9021 | `addSp delSp modSp add mod modNotesTx` | **INSERTED — Bariah** |
| 7 | `slide7.xml` | 9016 | *(no record)* | **BASE — untouched** |
| 8 | `slide8.xml` | 9017 | `addSp modSp add mod modNotesTx` | **INSERTED — Bariah** |
| — | *(never in final deck)* | 9018 | `add del` | **GHOST — created then discarded** |

**The four base slides are exactly `9003, 9008, 9011, 9016`** — precisely the four that carry neither
`add` nor `new` at slide level. This independently reproduces the "4 slaid" claim in `dc:title`.
The four survivors in the final deck are positions 1, 4, 5, 7.

### 2.1 Base order and the reorder — `MEASURED_FACT`

Base `sldId`s ascend `9003 < 9008 < 9011 < 9016`. In the final deck the order is
`9003, 9011, 9008, 9016` — positions 2 and 3 of the base are transposed. Both `9008` and `9011`
carry `ord` in their `sldChg`; `9003` and `9016` carry no record at all. The log and the ID ordering
agree: **Bariah swapped the two middle base slides and left the outer two in place.**

| Base pos | `sldId` | → Final pos | Movement |
|---:|---:|---:|---|
| 1 | 9003 | 1 | fixed |
| 2 | 9008 | 5 | moved down (`ord`) |
| 3 | 9011 | 4 | moved up (`ord`) |
| 4 | 9016 | 7 | fixed (displaced by insertions) |

### 2.2 The discarded slide — `MEASURED_FACT`

`sldId=9018`, `chg="add del"`, `dt=2026-07-29T23:04:24.765`, zero shape records. A slide was created
and removed inside the session. Its content is unrecoverable from this package. Flagged for Stage 0A:
**an intermediate design state existed that no surviving artifact documents.** `OPEN_DECISION`

---

## 3. Classification of the eight slides

### 3.1 Preserved unchanged — `MEASURED_FACT`

| Part | `sldId` | Subject | Evidence |
|---|---:|---|---|
| `slide1.xml` | 9003 | `Struktur Taman` — 4-label + single covering visual | no `sldChg` record |
| `slide7.xml` | 9016 | `Rumusan` (base wording, with `Kepentingan:` / `Isi utama:` / `Manfaat kefahaman:` labels) | no `sldChg` record |

These two are the **internal control pair**. Every judgement in this document about what Bariah
*changed* is anchored to them.

### 3.2 Edited in place — `MEASURED_FACT`

**`slide4.xml` (9011) — `Papan Tanda`, full-slide reveal child.**
6 shape records: `sp2 mod` (title placeholder, 23:05:33), `sp4 add mod` (off-canvas module-reference
box, 23:06:09), `sp6 mod` (off-canvas Note-to-MMD panel, 23:06:43), `sp8 mod` (full-width visual panel,
22:58:03), `sp9 mod` (display body, 22:57:04), `sp10 del mod` (deleted shape, 22:52:53).

**`slide5.xml` (9008) — `Struktur Taman`, card completion state.**
Structurally a **rebuild**, not an edit: 7 shapes deleted in one action
(`sp41–sp47 del @23:07:48.686`), then 9 shapes added in one action
(`sp4, sp7, sp10, sp12, sp14, sp16, sp18, sp20, sp22 add @23:07:55.355`) — the entire 2×2 card grid
plus labels and instruction line. `sp9 mod` (note panel, 23:10:53). Four `picChg mod ord` records
(`pic34 @23:08:12`, `pic36 @23:08:19`, `pic38 @23:08:23`, `pic40 @23:08:27`) — the tick icons, each
nudged individually, seven seconds apart. That per-icon sequence is the direct forensic signature of
the hand-placement variance quantified in `CARD_ARCHETYPE_SPEC.md §2.5`. `MEASURED_FACT`

### 3.3 Deleted and replaced

No slide in this package was deleted-and-replaced as a pair. The one deletion (`9018`) was of a slide
Bariah had herself created minutes earlier, with no replacement bearing a lineage marker.
The nearest thing to a replacement is **shape-level**, inside `9008` (§3.2) and inside `9021`
(`sp3/sp4/sp5/sp18 del`, `sp7/sp8/sp10 add`). `MEASURED_FACT`

### 3.4 Newly inserted — `MEASURED_FACT`

| Part | `sldId` | Marker | Function |
|---|---:|---|---|
| `slide2.xml` | 9020 | `new` | Bariah's written rationale contrasting Hotspot vs Card. Title placeholder left empty (`app.xml` lists its title as `PowerPoint Presentation`). |
| `slide3.xml` | 9019 | `add` | The proposed **Card** base state, 2×2 grid, 4 discrete visuals. |
| `slide6.xml` | 9021 | `add` | The **Hotspot** counter-example, one covering visual + 4 `[button label]` markers. |
| `slide8.xml` | 9017 | `add` | Revised `Rumusan` + the off-canvas rule list (yellow box, `sp3 add mod @23:12:17`). |

`9020` is marked `new` (created from blank); `9019`, `9021`, `9017` are marked `add` (duplicated from
an existing slide, then modified). `slide8` is a duplicate of `slide7` — the control pair for the
Rumusan analysis in `DISPLAY_BUDGET_REDERIVED.md`. `MEASURED_FACT`

---

## 4. Byte-identity / shape-tree identity of surviving control slides

**`NOT_DETERMINABLE` against the probes.** Neither probe revision is available, so neither a byte
comparison nor a shape-tree comparison against v0.1 or v0.2 can be performed.

What *is* established, and is the strongest available substitute:

- `slide1.xml` (9003) and `slide7.xml` (9016) carry **zero** change records in a log that captured
  52 shape-level and 4 picture-level changes across the other six slides. `MEASURED_FACT`
- Within the session recorded by `changesInfo1.xml`, they are untouched. Their shape trees are
  therefore the closest surviving proxy for the probe base and should be treated as the control
  reference for Stage 0A until a probe revision is supplied. `MEASURED_FACT`

Their full geometry is inventoried in `STATE_ARCHETYPE_OPTIONS.md §1.3` (slide 7) and
`CARD_ARCHETYPE_SPEC.md §1.1` (slide 1).

---

## 5–6. Exact base revision determination

# `BASE_REVISION_NOT_DETERMINABLE`

Precise reasons, in order of how they block the question:

1. **No probe artifact is reachable.** Filesystem sweep of the entire container found one PPTX — the
   reviewed deck. Neither `24dcaa04…1d471c` nor `75f8b168…c15045` exists on disk, in any attached
   repository, or in any session-mounted path. `NOT_DETERMINABLE`

2. **A hash is a one-way check, not a source.** The two supplied digests can only confirm or deny
   identity for a file already in hand. They cannot be inverted to produce v0.1 or v0.2 content, and
   the reviewed deck's own hash matches neither — which was expected, since the reviewed deck contains
   four slides that the probe base demonstrably did not.

3. **The surviving base is discriminating-poor even if the probes appeared.** Only two of the four base
   slides (`9003`, `9016`) survive untouched. The other two (`9008`, `9011`) were modified in place,
   and `9008` had its entire shape population replaced. If v0.1 and v0.2 differ only in slides that
   correspond to `9008` or `9011`, the difference has been overwritten and would be unrecoverable even
   with both probes present.

4. **The change log has no base-revision field.** `pc:chgData` records author, `userId`, `providerId`,
   `clId`, and timestamps only. There is no baseline digest, no document-version marker, and no
   `p:extLst` revision pin anywhere in the package. `ppt/revisionInfo.xml` records a single client at
   `v=31`, which counts *this client's* saves, not the ancestry of the file it opened.

5. **`docProps` cannot discriminate either.** `cp:revision = 1` and
   `dcterms:created = 2021-11-01T02:42:52Z` are both inherited from a donor template — the creation
   date precedes the K5 B02 work by years, and a revision counter of 1 after an 87-minute editing
   session with 56 recorded change events is not a real counter.

**To resolve this**, exactly one thing is needed: the actual bytes of probe v0.1 and v0.2. With both in
hand, the test is mechanical — compare the shape trees of `slide1.xml` (9003) and `slide7.xml` (9016)
against the corresponding slides in each revision; the revision that matches on both is the base. Until
then, no assertion about which revision Bariah opened may enter Stage 0A.

---

## 7. Author identities, timestamps, and change metadata

### 7.1 Sole author — `MEASURED_FACT`

Every one of the **65** `name=` attributes in `changesInfo1.xml` reads `Bariah Ahmad`.
No second author appears anywhere in the package.

| Field | Value |
|---|---|
| `name` | `Bariah Ahmad` (65/65 occurrences) |
| `userId` | `0648d156d4325605` (65/65) |
| `providerId` | `LiveId` (65/65) |
| `clId` | `{B2932A15-7E90-46D7-93E4-B64D1E7A69C0}` |
| `cp:lastModifiedBy` | `Bariah Ahmad` |
| `dc:creator` | `SMEC courseware.my` *(inherited from base; not Bariah)* |

The split between `dc:creator` and `cp:lastModifiedBy` is itself lineage evidence: the file was
authored by SMEC and last written by Bariah. `MEASURED_FACT`

### 7.2 Session envelope — `MEASURED_FACT`

| Marker | Value |
|---|---|
| Earliest change timestamp | `2026-07-29T22:15:20.436` |
| Latest change timestamp | `2026-07-29T23:13:50.698` |
| Elapsed span | 58 min 30 s |
| `docProps/app.xml TotalTime` | 87 min |
| `revisionInfo.xml` client `dt` | `2026-07-29T23:07:29.482` (`v=31`) |
| `dcterms:modified` | `2026-07-29T23:13:59Z` |

39 distinct timestamps. Densest cluster `23:07:48–23:07:55` (16 events) — the slide-5 rebuild.

### 7.3 Change-record inventory — `MEASURED_FACT`

| Element | Count |
|---|---:|
| `pc:sldChg` | 7 |
| `pc:spChg` | 52 |
| `pc:picChg` | 4 |
| `pc:chgData` | 9 |
| `ac:chgData` | 56 |

Per-slide totals: `9008` → 19 sp + 4 pic; `9021` → 12 sp; `9019` → 11 sp; `9011` → 6 sp;
`9017` → 3 sp; `9020` → 2 sp; `9018` → 0.

### 7.4 Comments and annotation parts — `MEASURED_FACT`

**None.** The package contains no `ppt/comments/`, no `ppt/modernComments/`, no
`ppt/authors.xml`, and no ink annotation parts. `[Content_Types].xml` declares no comment override.

This is materially important: **all of Bariah's review commentary is carried as ordinary off-canvas
text boxes on the slide surface, not as PowerPoint comments.** Any downstream tooling that harvests
review feedback by reading the comments API will find nothing. Enters Stage 0A.

### 7.5 Non-standard metadata — `MEASURED_FACT`

| Part | Standard? | Note |
|---|---|---|
| `ppt/tags/tag1.xml` | non-standard payload in a standard part | 23 iSpring tags, presentation-level — see `SME_RULE_CHECKABILITY.md §7` |
| `ppt/changesInfos/changesInfo1.xml` | MS extension (`.../2016/11/relationships/changesInfo`) | the change log used throughout this document |
| `ppt/revisionInfo.xml` | MS extension (`.../2015/10/relationships/revisionInfo`) | single client, `v=31` |
| `p:extLst` in `presentation.xml` | MS extension | two user-drawn guides: horizontal `pos=1026`, vertical `pos=3817` |

The two guides are authoring aids, not layout constraints, but the vertical guide at `pos=3817`
(1/8 pt units → 3817/576 = **6.6267 in**) sits within 0.04 in of stage centre (6.6667 in) and is
plausibly the alignment reference Bariah used. `PROVISIONAL_IDENTIFIER`

---

## 8. Verbatim transcription of every Bariah annotation

Locus convention: the stage is 0 → 13.3333 in horizontally. Any shape with negative `x` is **off-canvas**
(scratch/margin) and never renders to a learner.

### 8.1 Off-canvas review panel — the rule list

**`slide8.xml` (`sldId 9017`), shape `id=3`, name `TextBox 2`.**
Locus **off-canvas**, `x = -3.2297`, `y = 1.8593`, `w = 2.8438`, `h = 5.8566`.
Fill `FFFF00` (yellow), bullet char `-`, `spAutoFit`.
Change record: `spChg chg="add mod" spId=3 dt=2026-07-29T23:12:17.323`.
**Created by Bariah in this session** — the single highest-authority annotation in the package.

| # | Verbatim text | Classification |
|---:|---|---|
| 1 | `Tidak perlu letak Hilmi di VO. Understood that it’s Hilmi. (Only put Hilmi in Slide 3 Narrator)` | `SME_AUTHORED_RULE` |
| 2 | `English Words in italic (cth: Water Feature)` — `Water Feature` is itself italic (`i="1"`) | `SME_AUTHORED_RULE` |
| 3 | `Tidak perlu letak perkataan Kepentingan, Isi Utama, Manfaat` | `SME_AUTHORED_RULE` |
| 4 | `Di Rumusan, Jangan guna anda, guna kontraktor` | `SME_AUTHORED_RULE` |
| 5 | `Manfaat – relate to application in industry` | `SME_AUTHORED_RULE` |

Note on rule 2: the rule is stated in the annotation **and** demonstrated in the same box — the example
token carries the italic run property it prescribes. Bariah wrote a self-exemplifying rule. `MEASURED_FACT`

### 8.2 On-canvas authored rationale

**`slide2.xml` (`sldId 9020`), shape `id=6`, name `TextBox 5`.**
Locus **on-canvas**, `x = 3.4469`, `y = 1.4015`, `w = 6.7396`, `h = 4.342`, `spAutoFit`.
Slide marked `new`; `spChg chg="add mod" spId=6 dt=2026-07-29T23:09:30.194`.

> `Perbezaan Interaktiviti Click & Reveal - Hotspot & Card`
>
> `Click & Reveal (Hotspot) digunakan untuk item, kategori atau komponen yang dipaparkan pada satu imej atau gambar rajah.`
>
> `Click & Reveal (Card) digunakan untuk item, kategori atau komponen yang disusun sebagai senarai atau grid berasingan.`
>
> `Apabila diklik, kedua-duanya memaparkan maklumat secara paparan penuh, atau pop up dengan butang tutup, bergantung kepada tahap penjelasan yang diperlukan.`

Classification: `SME_AUTHORED_RULE` — a **selection criterion**, and the only definitional statement in
the package that distinguishes the two interaction archetypes. It is the governing input to the
Card-vs-Hotspot analysis in `SME_RULE_CHECKABILITY.md §6`. The slide has an empty title placeholder,
which is why `app.xml` lists it as `PowerPoint Presentation`. `MEASURED_FACT`

### 8.3 Off-canvas recommendation embedded in the Note-to-MMD panel

**`slide3.xml` (`sldId 9019`), shape `id=9`, name `Rectangle 8`.**
Locus **off-canvas**, `x = -3.35`, `y = 0.0`, `w = 3.1496`, `h = 7.5`.
`spChg chg="mod" spId=9 dt=2026-07-29T22:47:50.318`.

Paragraph `p0`, verbatim:

> `(PENAMBAHBAIKAN, I think it’s best/logical to use Click & Reveal (Card))`

Classification: `SME_AUTHORED_RULE` (recommendation). First-person English inside an otherwise Malay
production panel; the remaining paragraphs `p1–p7` of this same shape are inherited — see §9–10.

### 8.4 `(PENAMBAHBAIKAN)` markers — `MEASURED_FACT`

A bare `(PENAMBAHBAIKAN)` prefix (Malay: *improvement*) heads the off-canvas note panel of every
Bariah-authored or Bariah-modified slide, and of **no** untouched slide:

| Part | `sldId` | Shape | Marker text | Slide-level verdict |
|---|---:|---|---|---|
| `slide1` | 9003 | `id=9` | *(absent)* | untouched |
| `slide3` | 9019 | `id=9` | `(PENAMBAHBAIKAN, I think it’s best/logical to use Click & Reveal (Card))` | inserted |
| `slide4` | 9011 | `id=6` | `(PENAMBAHBAIKAN)` | edited in place |
| `slide5` | 9008 | `id=9` | `(PENAMBAHBAIKAN)` | rebuilt in place |
| `slide6` | 9021 | `id=9` | `(IF HOTSPOT - CONTOH)` | inserted |
| `slide7` | 9016 | `id=9` | *(absent)* | untouched |
| `slide8` | 9017 | `id=9` | `(PENAMBAHBAIKAN)` | inserted |

**The marker and the change log agree on all eight slides, independently.** This is the single
strongest corroboration in the ingest: a human-authored convention and a machine-generated change log,
neither aware of the other, partition the deck identically. `MEASURED_FACT`

`slide6`'s variant marker `(IF HOTSPOT - CONTOH)` is duplicated into its notes slide
(`notesSlide5.xml`, sole content) and marks the slide as an illustrative alternative, not a proposal.

### 8.5 Other off-canvas production notes — `INHERITED_PROBE_CONTENT` unless flagged

| Part | Shape | Locus | Verbatim | Classification |
|---|---|---|---|---|
| `slide1` | `id=18 Rectangle 17` | off-canvas `x=-3.1531` | `Rujukan modul: imej K5PL06T03-B02-IMG-01, ms 237.` | `INHERITED_PROBE_CONTENT` |
| `slide3` | `id=18 Rectangle 17` | off-canvas `x=-3.1531` | `Rujukan modul: imej K5PL06T03-B02-IMG-01, ms 237.` | `INHERITED_PROBE_CONTENT` |
| `slide4` | `id=4 Rectangle 3` | off-canvas `x=-3.1531` | `Rujukan modul: imej K5PL06T03-B02-IMG-01, ms 237. Paparkan sebagai visual utama skrin penuh.` | `SME_AUTHORED_RULE` — shape carries `spChg chg="add mod" dt=23:06:09.402`; **added by Bariah** |
| `slide5` | `id=9` p4–p5 | off-canvas | `This is just to show tick icon.` / `Semua card selesai.` | `SME_AUTHORED_RULE` |
| `slide4` | `id=6` p4 | off-canvas | `Dipapar penuh selepas learner klik card.` | `SME_AUTHORED_RULE` (shape `mod` @23:06:43; see §10.3 caveat) |
| `slide4` | `id=6` p5 | off-canvas | `Rujukan imej modul: K5PL06T03-B02-IMG-05, ms 243.` | `PROVISIONAL_IDENTIFIER` — cites a *different* image ID (`IMG-05`, ms 243) from the `IMG-01`/ms 237 used everywhere else |

The `IMG-05` / ms 243 citation on `slide4` conflicts with the `IMG-01` / ms 237 citation in the
off-canvas box on the *same slide* (`id=4`). One slide cites two different module images for one
visual. This must be reconciled against `asset_manifest.json` before any binding is issued. `OPEN_DECISION`

---

## 9. Confirmation: did `VO PL & Topik tidak perlu lagi` predate the review?

## **CONFIRMED — the line existed in the probe base.** `INHERITED_PROBE_CONTENT`

**Evidence.** The exact string occurs at:

| Part | `sldId` | Shape | Paragraph | Slide change record |
|---|---:|---|---|---|
| `slide1.xml` | **9003** | `id=9 Rectangle 8` | `p5` (auto-numbered, `marL=342900 indent=-342900`) | **none — slide untouched** |
| `slide3.xml` | 9019 | `id=9 Rectangle 8` | `p6` (auto-numbered) | slide `add`; shape `mod` @22:47:50 |
| `slide4.xml` | 9011 | `id=6 Rectangle 5` | `p6` (plain, `lvl=0`) | slide base; shape `mod` @23:06:43 |

The occurrence on **`slide1.xml` is decisive.** `slide1` is `sldId 9003`, one of the two slides with
**zero** change records in a log that captured 56 individual change events elsewhere. Bariah did not
touch that slide, therefore she did not write that line, therefore the line was already in the probe
base she opened.

Byte-exact form as stored (no trailing punctuation, ampersand as literal `&`):

```
VO PL & Topik tidak perlu lagi
```

**Consequence for classification:** this line is `INHERITED_PROBE_CONTENT` and must **not** be recorded
as a Bariah decision. Its presence on `slide3` and `slide4` is *retention*, not authorship.

**Residual caveat, stated for completeness:** this proves the line predates the *recorded editing
session*. It cannot prove the line predates probe v0.1 specifically versus v0.2, because — per §5 —
neither revision is available. If the line was introduced *between* v0.1 and v0.2, this evidence would
not distinguish that. `NOT_DETERMINABLE` at revision granularity; `MEASURED_FACT` at session granularity.

---

## 10. Provenance classification of every instruction

### 10.1 Pre-existing probe instruction — `INHERITED_PROBE_CONTENT`

Present on `slide1.xml` (9003, untouched) and therefore proven to predate the review:

| Text | Locus |
|---|---|
| `Slide 4 (Click & Reveal)` | `slide1 id=9 p0` |
| `Subtopik` | `slide1 id=9 p1` |
| `Note to MMD:` | `slide1 id=9 p2` |
| `4 hotspot. Nombor selebihnya dibuang.` | `slide1 id=9 p3` |
| `Klik hotspot -> reveal full-slide, bukan pop up.` | `slide1 id=9 p4` |
| **`VO PL & Topik tidak perlu lagi`** | `slide1 id=9 p5` |
| `Rujukan modul: imej K5PL06T03-B02-IMG-01, ms 237.` | `slide1 id=18` |
| `Empat jenis struktur taman.` | `slide1 id=20` (display) |
| `Klik pada setiap komponen untuk penjelasan lanjut.` | `slide1 id=25` (display) |
| `Slide 6` / `Rumusan Bahagian` / `Rumusan bahagian, bukan rumusan topik penuh.` | `slide7 id=9` |
| Full base Rumusan display body incl. `Kepentingan:` / `Isi utama:` / `Manfaat kefahaman:` | `slide7 id=25` |
| `Hilmi:` narrator prefix in VO | `notesSlide1`, `notesSlide6` |

### 10.2 Bariah-retained instruction — `INHERITED_PROBE_CONTENT` (retained, not authored)

Carried forward by Bariah onto slides she created or edited. **Must not be counted as new decisions.**

| Text | Retained onto |
|---|---|
| `VO PL & Topik tidak perlu lagi` | `slide3 id=9 p6`, `slide4 id=6 p6` |
| `Klik hotspot -> reveal full-slide, bukan pop up.` | `slide3 id=9 p5` |
| `4 hotspot. Nombor selebihnya dibuang.` | `slide3 id=9 p4` |
| `Slide 4 (Click & Reveal)` / `Subtopik` / `Note to MMD:` | `slide3 id=9 p1–p3` |
| `Rujukan modul: imej K5PL06T03-B02-IMG-01, ms 237.` | `slide3 id=18` |
| `Slide 6` / `Rumusan Bahagian` / `Rumusan bahagian, bukan rumusan topik penuh.` | `slide8 id=9 p1–p4` |

`slide3`'s instruction line `Klik pada setiap struktur untuk penjelasan lanjut.` differs from the base
`slide1` form `Klik pada setiap komponen untuk penjelasan lanjut.` — one word, `komponen` → `struktur`.
The shape (`id=25`) carries `spChg chg="mod" @22:49:05`. **Bariah-edited inherited text**, not a new
rule. `MEASURED_FACT`

### 10.3 Bariah-created rule — `SME_AUTHORED_RULE`

| # | Rule | Locus | Evidence of authorship |
|---:|---|---|---|
| R1 | `Tidak perlu letak Hilmi di VO. Understood that it’s Hilmi. (Only put Hilmi in Slide 3 Narrator)` | `slide8 id=3 p0` | shape `add mod` @23:12:17 |
| R2 | `English Words in italic (cth: Water Feature)` | `slide8 id=3 p1` | same shape |
| R3 | `Tidak perlu letak perkataan Kepentingan, Isi Utama, Manfaat` | `slide8 id=3 p2` | same shape |
| R4 | `Di Rumusan, Jangan guna anda, guna kontraktor` | `slide8 id=3 p3` | same shape |
| R5 | `Manfaat – relate to application in industry` | `slide8 id=3 p4` | same shape |
| R6 | `Click & Reveal (Hotspot)` vs `(Card)` selection criterion (3 paragraphs) | `slide2 id=6` | slide `new`, shape `add mod` @23:09:30 |
| R7 | `(PENAMBAHBAIKAN, I think it’s best/logical to use Click & Reveal (Card))` | `slide3 id=9 p0` | shape `mod` @22:47:50; first-person English |
| R8 | `Paparkan sebagai visual utama skrin penuh.` | `slide4 id=4` | shape `add mod` @23:06:09 |
| R9 | `Semua card selesai.` / `This is just to show tick icon.` | `slide5 id=9 p4–p5` | shape `mod` @23:10:53; slide rebuilt |

**Caveat on `slide4 id=6 p8` — `VO subtopik tidak perlu lagi`.** This line does **not** appear on the
untouched base `slide1`, which suggests Bariah authored it as an extension of the inherited
`VO PL & Topik` rule. But `slide4` is a *base* slide (9011) whose note panel carries only a
whole-shape `mod` record — `changesInfo` records modification at shape granularity, never at paragraph
granularity, so it cannot say which paragraph changed. The line may equally have been present in the
probe base and merely survived a `mod` to a neighbouring paragraph.
**Classified `NOT_DETERMINABLE`. Resolve by inspecting probe v0.1/v0.2 `slide4`.** Do not promote to
`SME_AUTHORED_RULE` until then.

### 10.4 Bariah-created example or explanatory note — `SME_AUTHORED_RULE` (demonstrative, non-normative)

These are *illustrations* of rules, not rules. They must not be lifted into a rule registry.

| Item | Locus | Nature |
|---|---|---|
| `slide3` — the 2×2 Card grid itself | `slide3` (9019) | worked example of R7 |
| `slide5` — the all-ticks completion state | `slide5` (9008) | worked example of R9; note explicitly says `This is just to show tick icon.` |
| `slide6` — `(IF HOTSPOT - CONTOH)` with 4 `[button label]` placeholders | `slide6` (9021) | counter-example illustrating R6's Hotspot branch |
| `slide8` display body | `slide8 id=25` | worked example of R1–R5 applied simultaneously (see `DISPLAY_BUDGET_REDERIVED.md`) |
| `Water Feature` italic token inside R2 | `slide8 id=3 p1` | self-exemplifying example |
| `[button label]` × 4 | `slide6 id=21, 7, 8, 10` | placeholder text — **not content**; must not enter any lexicon |

`slide5`'s own note — `This is just to show tick icon.` — is Bariah explicitly declaring the slide
non-normative. Its hand-placement variance (`CARD_ARCHETYPE_SPEC.md §2.5`) must therefore **not** be
read as intended geometry. `MEASURED_FACT`

---

## 11. Evidence that must enter Stage 0A reconciliation

| # | Item | Label |
|---:|---|---|
| 1 | Probe v0.1 and v0.2 bytes — required to resolve `BASE_REVISION_NOT_DETERMINABLE` | `NOT_DETERMINABLE` |
| 2 | Discarded slide `sldId 9018` — an intermediate design state no artifact documents | `OPEN_DECISION` |
| 3 | `IMG-01`/ms 237 vs `IMG-05`/ms 243 conflict on `slide4` | `OPEN_DECISION` |
| 4 | All review commentary is off-canvas text, not PowerPoint comments — comment-harvesting tooling will return empty | `MEASURED_FACT` |
| 5 | iSpring tag block describes PL06 T3 B2 / 14 slides — foreign to K5 B02 | `MEASURED_FACT` |
| 6 | `slide4 id=6 p8` `VO subtopik tidak perlu lagi` — authorship unresolved at paragraph granularity | `NOT_DETERMINABLE` |
| 7 | `dc:title` still says 4 slides; package holds 8 | `MEASURED_FACT` |
| 8 | Source-label normalisation `BBQ pit` → `BBQ Pit` and 3 further cases | `SME_RULE_CHECKABILITY.md §8` |
| 9 | Reviewed reveal-child state is geometrically indistinguishable from Rumusan (max Δ 0.0129 in) | `STATE_ARCHETYPE_OPTIONS.md` |
| 10 | Five-card layout cannot preserve reviewed card size within the deck's own content band | `CARD_ARCHETYPE_SPEC.md §3` |

---

## 12. Modification statement

No PPTX was modified. No compiler code was patched. No schema was updated. No candidate deck, manifest,
digest pin, or baseline was created. No geometry was frozen. No canonical decision ID was assigned.
The reviewed package hash was re-measured after all analysis and is unchanged at
`ee4f54790bd22afb82457237d63d290eb6ac0ceabbead88ec5f7d7fced8bb9e7`.
