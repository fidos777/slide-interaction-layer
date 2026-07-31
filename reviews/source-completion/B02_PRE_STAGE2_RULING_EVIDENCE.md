# B02_PRE_STAGE2_RULING_EVIDENCE — K5 PL06 T03 B02

```
EVIDENCE PACK ONLY — NO RULING IS SELECTED IN THIS DOCUMENT
STAGE 1.5 · SOURCE HARDENING + CONFLICT EVIDENCE + VALIDATION AUDIT
PRE_STAGE2_RULING_EVIDENCE_BLOCKED
BLOCKED_MODULE_DOCX_INTEGRITY_NOT_VERIFIED
```

> **This is not a decision register.** It contains no selected governance ruling and no selected
> instructional ruling. Every issue below is presented with its conflicting clauses, its options, the
> consequence of each option, and the authority that must decide. **Nothing is decided on behalf of
> Firdaus, Bariah, or CAIR.**

---

# 0. Repository and scope

| Field | Value |
|---|---|
| Repository | `/home/user/slide-interaction-layer` |
| Branch | `claude/verify-powerpoint-file-vpfzkg` |
| HEAD SHA at Stage 1.5 start | `7ac83e59ed565542d2617ab7e3993ea42bffd2b2` |
| Working tree at Stage 1.5 start | one untracked file — `reviews/source-completion/TABLE_ROW_TO_POPUP_MATRIX.md` |
| Modified files at Stage 1.5 start | none |
| Evidence date | 31 July 2026 |

**Not performed:** screen/state map, generator modification, PowerPoint regeneration or patching,
component propagation, decision-register creation, ruling selection.

## 0.1 Source inventory preservation

The Stage 1 inventory is a **source-evidence count** and was not altered.

| Preserved quantity | Value | Verified by |
|---|---:|---|
| Provisional row IDs | 26, unchanged | Appendix A check 26 |
| Source row order | unchanged | Appendix A checks 4, 5 |
| Source locators | unchanged | Appendix A checks 7, 8, 27 |
| Image ownership findings | unchanged | Appendix A check 28 |
| `SOURCE_ROW_COUNT` | **26** | Appendix A checks 1, 5 |
| Asset total | **14**, none orphaned | Appendix A check 28 |

**No interaction split was converted into a source row.** See `TABLE_ROW_TO_POPUP_MATRIX.md` §8.3.

```
SOURCE_ROW_COUNT                = 26   ← frozen; changes only on a demonstrable extraction error
PROPOSED_INTERACTION_ITEM_COUNT = 26   ← implementation proposal; may change under A-05 / A-06
```

---

# A. Frozen inputs used by this evidence pack

| # | Input | Bytes | SHA-256 |
|---|---|---:|---|
| I-1 | Updated S&G v0.2 — `…/uploads/…/5efad61e-K5_PL06_T03_B02_UPDATED_SG_v0.2.docx` | 51,443 | `d52f0fe123863c0d7ff968efdacda91157331f49ac46f3b3aaf2e630b3c2403a` |
| I-1t | Text+table extraction of I-1 (raw OOXML walk) — `…/scratchpad/sg02.txt` | 21,374 | `c89fd3f78de898eb2ed107f4c7435e89ded02bd2a754bcd65e1c6db5b718c923` |
| I-2 | Module rendered PDF pp. 237–250 — `…/uploads/…/6a5c03ec-K5_PL06_T03_B02_pages_256269.pdf` | 429,918 | `30a6903dacbd7e8bce60dc1aa32026fc4ed98439054aeced9e895b5df828a3f4` |
| I-3 | Module approved DOCX (Drive `16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4`) | 16,832,861 | **NOT OBTAINED — §B** |
| I-3a | Text extraction derived from I-3 — `…/scratchpad/module.txt` | 422,686 | `07595d7f74d5b0ebdf2122dcfd9e0731597a486e3de78959df95d1880be35fc3` |
| I-3b | B02 body span cut from I-3a — `…/scratchpad/b02_body.txt` | 14,304 | `f35ce9ceaf17a68f4dd05fd4486a8223d7203bae249a84374c741154529768a2` |
| I-3c | Independent PDF table geometry derived from I-2 — `…/scratchpad/pdf_tables.json` | 9,810 | `1d58079fad6d67575a4ab984427ab5baf540a0727cedceb03482ed4a4d2b0527` |
| I-4 | Storyboard v0.1 — `reviews/storyboard-bariah/K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_1.pptx` | 109,954 | `749b6c90f468bc0a1986b853319e62b1a1cec83600a98cbade628214d5bf8e7a` |
| I-12 | S&G Storyboard Development **v1.0** (`Versi 1.0 \| Julai 2026`), Drive `1T4X-Mr8nBJhSTZ2GF62hPJHcSrPqfeCE` | 56,274 | not hashed — Drive-resident, same tooling limitation as I-3 |

**I-1 and I-12 are both live specification documents with overlapping authority over this bahagian.**
Every conflict in §D is a conflict between them, or an incompleteness in one of them.

---

# B. Module DOCX integrity — `BLOCKED_MODULE_DOCX_INTEGRITY_NOT_VERIFIED`

## B.1 Exact identity of the file whose hash is required

| Field | Value |
|---|---|
| Filename | `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx` |
| Drive fileId | `16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4` |
| Parent folder | `1p18qHATFfn0oLHyCvYOfA8rQQlxkwJXS` — "5_Kursus Kerja Bangunan - Pembinaan Landskap Luar" |
| mimeType | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| Byte size | **16,832,861** |
| createdTime | `2026-06-16T03:20:48.816Z` |
| modifiedTime | `2026-06-07T23:30:02Z` |
| **SHA-256** | **NOT OBTAINED** |

**Uniqueness re-confirmed at Stage 1.5:** a Drive query on the parent folder returns exactly one file.
No conflicting copy of the approved module exists in that folder.

## B.2 Methods attempted — four routes, all failed

| # | Method | Result | Evidence |
|---|---|---|---|
| 1 | **Hash-in-place via Drive metadata.** Drive API v3 exposes `sha256Checksum` / `md5Checksum` for binary files. | ❌ **Not available.** The MCP `get_file_metadata` response schema returns `canAddChildren, createdTime, fileExtension, fileSize, id, mimeType, modifiedTime, parentId, title, viewUrl` — **no checksum field of any kind**. | Live call against `16j15Knt…` returned the field set above with no checksum key |
| 2 | **Direct authenticated Drive API call** for `fields=sha256Checksum,md5Checksum` using the container's `CLOUDSDK_AUTH_ACCESS_TOKEN`. | ❌ **HTTP 401.** `"Request had invalid authentication credentials… Expected OAuth 2 access token"`. The token is a Google Cloud SDK credential without Drive scope. | `www.googleapis.com/drive/v3/files/…` → 401 `authError`; `drive.googleapis.com` → 404 |
| 3 | **Direct file download over HTTPS** (`drive.google.com/uc?export=download&id=…`). | ❌ **Blocked at the network policy.** `curl: (56) CONNECT tunnel failed, response 403`. The agent proxy logged `connect_rejected … "gateway answered 403 to CONNECT (policy denial)" host: drive.google.com:443`. | `$HTTPS_PROXY/__agentproxy/status` `recentRelayFailures` entry, ts `2026-07-31T13:32:31.708Z` |
| 4 | **Chunked / ranged download via MCP** `download_file_content`. | ❌ **No chunking exists.** The tool schema accepts only `fileId` and `exportMimeType` — **no range, offset, or page parameter.** A probe against a 504-byte Drive file returned the file's *entire* contents as one base64 string in a single `content` field, confirming all-or-nothing behaviour. | Probe on `1Ccz9WfGrdRHsB2X4Z5GtTLZJOUHaWQ3S` returned complete base64 with no range control |

**Supporting negative results:** no Drive credential file on disk; no `gdown`, `rclone` or `gcloud`
binary; no `googleapiclient` or `google.oauth2` Python module.

## B.3 Why route 4 was not executed against the 16.8 MB file

This is a deliberate decision, not an omission.

`download_file_content` has no range parameter, so any call is all-or-nothing. 16,832,861 bytes
base64-encode to **≈ 22,443,816 characters** returned in a single tool result. Two disqualifying
consequences:

1. **It exceeds tool-result limits and would consume the entire working context**, ending the task
   without producing any deliverable.
2. **Even on success there is no lossless path back to exact bytes.** Reconstructing the file would
   require re-emitting ~22 MB of base64 through a shell heredoc. Any truncation, wrapping or encoding
   artifact would silently yield a *wrong* SHA-256 — a hash that looks authoritative and certifies the
   wrong bytes. **A wrong hash is worse than no hash**, because it converts an open gap into a false
   assurance.

The task's instruction was to use "an available **safe** method". A 22 MB context-exhausting transfer
with a silent-corruption failure mode is not one.

## B.4 What is explicitly NOT recorded as a substitute

Per instruction, none of the following is offered in place of the DOCX SHA-256:

- ❌ the Drive `fileId`
- ❌ the `modifiedTime`
- ❌ the byte size
- ❌ a converted or exported copy
- ❌ the hash of I-3a (`module.txt`) or I-3b (`b02_body.txt`) — these are *derived artifacts*
- ❌ the PDF hash (I-2)

Those values are recorded as **identity metadata**, clearly labelled as such. They are not a
cryptographic integrity proof and this document does not present them as one.

## B.5 Containment — what the gap does and does not affect

| | |
|---|---|
| **Affected** | Provenance certification of the DOCX as text authority. Stage 2 adoption. |
| **Not affected** | The 26-row inventory, row order, page locators, image ownership, and the 14-asset register — **all independently reproducible from I-2, which is hashed.** Appendix A check 5 re-derives the 26-row count from I-2 alone, with no reference to the matrix or to I-3a. |

## B.6 Routes that would close this

Not actions to take now — options for whoever can act:

1. Attach the DOCX to a session the way I-1 and I-2 were attached; it lands on local disk and hashes
   in one command.
2. Add `drive.google.com` (or `www.googleapis.com`) to the environment's network policy allowlist and
   supply a Drive-scoped credential.
3. Compute `sha256sum` on the file wherever it is held authoritatively and record the value.
4. Extend the MCP Drive connector to surface Drive's own `sha256Checksum` field.

---

# C. A-09 — phantom empty rows: DOCX extraction versus rendered PDF

## C.1 What was compared

The DOCX-derived text extraction (I-3a → I-3b) renders **seven** of the nine source tables with a
leading row whose every cell is empty. The rendered PDF (I-2) shows no such row. Each of the seven was
examined individually.

## C.2 Per-row evidence

| # | Component | I-3b line | Row as extracted | Cells | Learner-facing proposition? | Present in rendered PDF (I-2)? | Classification |
|---|---|---:|---|---:|:-:|:-:|---|
| P-1 | Struktur Persisir Air | 15 | `\|  \|  \|  \|` | 3 empty | **NO** — all cells empty | **NO** — I-2 p238 tbl0 r0 is the header `JENIS STRUKTUR \| FUNGSI & PENERANGAN \| CONTOH` | conversion artifact |
| P-2 | Struktur Teduhan | 30 | `\|  \|  \|  \|` | 3 empty | **NO** | **NO** — I-2 p239 tbl0 r0 is the header | conversion artifact |
| P-3 | Kemudahan Awam | 51 | `\|  \|  \|` | 2 empty | **NO** | **NO** — I-2 p240 tbl0 r0 is the header `CONTOH \| PENERANGAN` | conversion artifact |
| P-4 | Water Feature | 68 | `\|  \|  \|` | 2 empty | **NO** | **NO** — I-2 p241 tbl1 r0 is the header | conversion artifact |
| P-5 | Papan Tanda | 101 | `\|  \|  \|` | 2 empty | **NO** | **NO** — I-2 p244 tbl0 r0 is the header `CONTOH \| SPESIFIKASI` | conversion artifact |
| P-6 | Drinking Fountain | 124 | `\|  \|  \|` | 2 empty | **NO** | **NO** — I-2 p248 tbl0 r0 is the header | conversion artifact |
| P-7 | BBQ Pit | 134 | `\|  \|  \|` | 2 empty | **NO** | **NO** — I-2 p249 tbl0 r0 is the header | conversion artifact |

## C.3 The mechanism is provable, not inferred

Every phantom row is followed **immediately** by a Markdown alignment row and then the real header:

```
|  |  |  |                                           ← phantom (empty header)
| :-: | :-: | :-: |                                  ← alignment row
| JENIS STRUKTUR | FUNGSI & PENERANGAN | CONTOH |     ← real header, demoted to a body row
```

This is the signature of a Markdown pipe table whose **header row is empty**: the converter emitted an
empty header because the DOCX table had no *marked* header row, and pushed the real header down into
the first body row.

**The control case confirms it.** The two components with **no** phantom row — `Kerusi Taman` and
`Tong Sampah` — are exactly the two whose Markdown places the real header *first*, followed by the
alignment row:

```
| CONTOH | SPESIFIKASI |                             ← real header, in header position
| :-: | :-: |                                        ← alignment row
| Kerusi Kayu Keras… |                               ← first data row
```

Seven tables lack a marked header row and produce a phantom; two have one and do not. **The
correlation is 9/9 with no exceptions.**

## C.4 Does excluding them change any meaningful content?

**No.** All seven rows are empty in every cell. They carry no `Jenis / Bahan`, no
`Fungsi & Penerangan`, no `Contoh`, no specification text, and no figure reference. Excluding them
removes zero propositions.

Independent confirmation: classifying **every** physical table row in I-2 by geometry alone — without
reference to the matrix — yields **26 DATA rows, 11 HEADER rows, 2 CONTINUATION rows, 1 EMPTY row =
40 physical rows**, exactly reconciling with the matrix §5.2 register. The seven phantoms have no
counterpart in that classification because they do not exist in the rendered source.

**They are therefore not added to the 26-row count.** They contain no independent instructional
proposition.

## C.5 Proposed source-precedence rule — for authority approval

```
PENDING_CAIR_SOURCE_PRECEDENCE_RULING
```

**Proposed, not adopted:**

> **DOCX (I-3) governs textual propositions** — the wording of every cell, every specification clause,
> every example string.
>
> **Rendered PDF (I-2) governs visible table structure** — row boundaries, row counts, header
> identification, continuation behaviour, pagination, printed page numbers, and figure/image ownership
> by heading-relative position.

**Rationale offered for consideration:** the DOCX is the approved editorial artifact and carries the
authoritative wording; the PDF is what the SME and the learner-facing pagination actually reflect, and
it is the only artifact in which "which row is a row" and "which page is a page" are observable. The
phantom-row finding is a worked example of the DOCX extraction being unreliable on *structure* while
remaining reliable on *text*.

**Counter-consideration to weigh:** the PDF is a 14-page extract, not the whole module. If a future
scope extends beyond pp. 237–250, the structural authority would have no coverage there.

**Not decided here. Authority: Firdaus / CAIR.**

---

# D. Pre-Stage-2 ruling evidence

Twelve issues. **No option is selected in any of them.**

Status vocabulary:

| Status | Meaning |
|---|---|
| `RULING_REQUIRED` | A human authority must choose; the specifications conflict or are silent |
| `TECHNICAL_MAPPING_REQUIRED` | No content decision needed; a schema or emission rule must be written |
| `RESOLVED_BY_EXISTING_RULE` | An existing clause already determines the outcome unambiguously |

---

## R-1 — VO source fidelity

**Locators**

| Artifact | Clause | Rule |
|---|---|---|
| I-12 | §6.1 "Sumber Kandungan VO: Modul Klien" | *"VO MESTI menggunakan ayat yang sama seperti dalam modul klien. JANGAN parafrasa atau ubah susunan ayat"*; *"Salin kandungan modul secara setia"*; additions permitted **only** for narrative connectives |
| I-12 | §9.2 QA checklist | *"VO menggunakan ayat asal dari modul klien – bukan parafrasa atau ayat sendiri"* |
| I-1 | §5.2 | *"Display text may be concise; VO should carry the fuller source-bound explanation without adding unsupported facts."* |
| I-1 | §3.2 | *"Fungsi & Penerangan → Popup learner display + expanded VO … display may be concise but VO must preserve propositions"* |
| I-1 | §4.2 | Mandates a generated closing sentence: *"Mari lihat contoh bagi [Nama Komponen] di halaman seterusnya."* |

**Conflict.** I-12 requires **verbatim transcription** and forbids paraphrase outright. I-1 requires
**proposition preservation**, which permits reformulation. These are different standards. I-4 (v0.1)
was written to the I-1 standard — its VOs are reformulated, not copied.

**Changes:** VO generation. **Does not change** source inventory, interaction granularity, or navigation.

| Option | Consequence |
|---|---|
| **A — verbatim per I-12 §6.1** | VO is lifted sentence-for-sentence from the module. Longest specification rows (Drinking Fountain ROW-01: 7 lettered sub-fields; BBQ Pit ROW-01: 4 with roman sub-items) produce very long VO. Highest source fidelity, lowest authoring latitude. All v0.1 VO must be rewritten. |
| **B — proposition-preserving per I-1 §5.2** | VO may reformulate while preserving every proposition. Shorter, more listenable. Requires a per-row proposition check rather than a diff against the module. v0.1 VO largely survives. |
| **C — hybrid** | Verbatim for specification content; reformulation permitted only where I-1 mandates a template sentence (§4.2 closing line) or a connective. Needs an explicit boundary rule stating which rows are which. |

**Required authority:** Bariah (instructional). **Status: `RULING_REQUIRED`.**

---

## R-2 — Popup VO requirement

**Locators**

| Artifact | Clause | Rule |
|---|---|---|
| I-1 | §3.1 | *"Each item → open one popup containing the row content, visual direction and VO."* |
| I-1 | §4.3 | *"Each item opens one popup with complete row content, visual direction and VO."* |
| I-1 | Appendix A | *"Popup with VO for each item — Confirmed"* |
| I-12 | §5.4.2 type 3 | **Pop Up (With VO)** — *"memaparkan tetingkap pop up DENGAN narasi VO"* |
| I-12 | §5.4.2 type 4 | **Pop Up (No VO)** — *"TANPA narasi VO. Pelajar membaca sendiri."* *"Sesuai untuk: Senarai panjang, jadual, rajah, atau maklumat rujukan"* |
| I-12 | §5.4.1 selection guide | *"Jadual, senarai panjang, atau maklumat rujukan untuk baca sendiri → Pop Up (No VO)"* |

**Conflict — and it is sharp.** I-1 mandates VO on **every** popup. I-12's own selection guide routes
**exactly this content type** — table-derived specification lists — to the **No-VO** variant. Every one
of the 26 B02 popups is table-derived; five components carry dense `SPESIFIKASI` cells.

**Changes:** VO generation, screen schema (audio asset per popup), MMD production scope and cost.
**Does not change** source inventory.

| Option | Consequence |
|---|---|
| **A — VO on every popup (I-1)** | 26 popup VO tracks. Uniform behaviour, simplest state model. Highest recording cost; long specification VO may be tedious to listen to. |
| **B — No-VO popups for specification tables (I-12 §5.4.1)** | 0 popup VO tracks; learner reads at own pace — the stated purpose of the No-VO variant. Contradicts I-1 §4.3 and Appendix A "Confirmed". Reduces MMD cost substantially. |
| **C — mixed by row type** | VO for the 16 rows from 3-column `FUNGSI & PENERANGAN` tables (short, narratable); no VO for the 10 rows from `SPESIFIKASI` tables (dense, reference-style). Requires an explicit routing rule and a non-uniform state model. |

**Required authority:** Bariah (instructional), with an MMD cost consequence.
**Status: `RULING_REQUIRED`.**

---

## R-3 — Physical status slides versus runtime state model

**Locators**

| Artifact | Clause | Rule |
|---|---|---|
| I-12 | §5.4.3 "Struktur Sub-Slide Interaktiviti" | Explicit **physical slide** pattern: `Slide X` (main) → `Slide Xa` (sub 1) → `Slide X(1)` (status slide, tick) → `Slide Xb` → `Slide X(2)` → `Slide Xc` … |
| I-12 | §6.4 | *"Slide Status (Tick Icon) — TIADA VO"* |
| I-12 | §6.5 | Mandatory MMD note *"This is just to show tick icon."* |
| I-1 | §1.3 | *"Popup views are states within the example screen and are **not counted as separate physical slides**."* |
| I-1 | §2.1 | *"Popup = content state, not a third navigation level."* |
| I-1 | §4.5 | Runtime state model: `item_viewed[item_id]`, `component_complete[component_id]`, `group_complete[group_id]`, `main_vo_complete[…]`, `resume_state` |
| I-4 | slides 9, 16 | v0.1 implements **physical** completion screens (S09, S16) — the I-12 approach |

**Conflict.** I-12 models progress as a sequence of physical storyboard slides. I-1 models it as
runtime state variables. Both are internally coherent; they produce very different artifacts.

**Changes:** screen schema, physical screen count, generator output shape, what Bariah actually reviews.
**Does not change** source inventory or source row identity.

| Option | Consequence |
|---|---|
| **A — physical status slides (I-12 §5.4.3)** | Every intermediate tick state is a storyboard slide. With 26 popups the deck grows well beyond the ~28-screen planning baseline in I-1 §1.3. Reviewer sees exactly what the learner sees at each step. Large, repetitive deck. |
| **B — runtime state model (I-1 §4.5)** | ~28 physical screens; popups and ticks are states described in production metadata. Matches I-1's pseudocode (Appendix B) and the LMS-resume requirement in §4.4. Reviewer must read state descriptions rather than see each state rendered. |
| **C — hybrid** | State model for popups; one physical completion screen per group master, as I-4 already does for S09/S16. Preserves the reviewable "all ticks complete" moment without one slide per tick. |

**Required authority:** Firdaus / CAIR (executable contract shape), with Bariah confirming
reviewability. **Status: `RULING_REQUIRED`.**

---

## R-4 — Rumusan / Kuiz / Tamat: per Topik or per Bahagian

**Locators**

| Artifact | Clause | Rule |
|---|---|---|
| I-12 | §4.3 "Peringkat Topik (7 Bahagian Standard)" | *"Setiap **topik** WAJIB mengandungi tujuh bahagian berikut"* — including 5 Rumusan, 6 Kuiz, 7 Tamat Topik |
| I-1 | §6.5 | *"Summarise the **bahagian**, not the entire topic."* |
| I-1 | §2.2 | Global flow ends *"Rumusan -> Kuiz -> Tamat/continue to the next approved destination"* **within B02** |
| I-1 | §6.7 | *"completion of Topic 3 **Bahagian 2** and continuation to the next learning section"* |
| I-1 | §10 open items | *"Exact S19 route target — next bahagian/destination ID not yet bound"* |

**Conflict.** I-12 places the closing set once per **Topik**; I-1 places it at the end of **Bahagian 2**.
If T03 contains multiple bahagian, these cannot both hold without either duplicating the closing set
per bahagian or deferring it to topic level.

**Compounding gap:** the number and identity of the other bahagian in T03 is **not verified from any
held artifact** (matrix §6 A-02/§8, I-1 §10).

**Changes:** frame screens, navigation, quiz placement and scope. **Does not change** source inventory.

| Option | Consequence |
|---|---|
| **A — per-Bahagian (I-1)** | B02 carries its own Rumusan, Kuiz and Tamat. Self-contained; matches I-1 §2.2 exactly. If T03 has n bahagian, the learner meets n quizzes in one topic — which I-12 §4.3 does not contemplate. |
| **B — per-Topik (I-12)** | B02 ends without Kuiz; assessment defers to a T03-level quiz covering all bahagian. Contradicts I-1 §2.2 and §6.6, and the 5 drafted B02 quiz items would move scope. |
| **C — split** | Per-bahagian Rumusan (closes the content), per-topik Kuiz (assesses the whole topic). Needs an explicit rule for what Tamat means at bahagian boundaries. |

**Required authority:** Bariah (instructional) **and** the course navigation owner named in I-1 §10.
**Status: `RULING_REQUIRED`.**

---

## R-5 — `Kembali` target, label and gating

**Locators**

| Artifact | Clause | Rule |
|---|---|---|
| I-1 | §4.3 | *"Kembali MUST be disabled until all example items have completion ticks… After all items are viewed, Kembali MUST be enabled and return to the Level 1 group master screen."* |
| I-1 | §4.2 | Main explanation screen *"does not carry the final Kembali to the group master"*; its control is `Seterusnya`, VO-gated |
| I-1 | §3.4 | *"Kembali returns to the Struktur Taman group master screen."* |
| I-1 | §4.3 | *"Closing the popup returns the learner to the same example screen"* — **the closing control is not named** |
| I-12 | §5.4.2 type 1 | *"Slide sub (kandungan didedahkan + butang 'Kembali')"* — Kembali on every sub-slide, ungated |
| I-12 | §9.4 QA | *"Butang 'Kembali' disertakan pada semua sub-slide interaktiviti"* |
| I-4 | 9 detail screens | v0.1 puts one ungated `Kembali` on every detail screen in a 0.58 in navigation strip |

**Three distinct disagreements:** *target* (group master vs immediate parent), *gating* (gated on full
completion vs always available), and *which screens carry it* (example screen only vs every sub-slide).
**Plus one genuine gap:** I-1 never names the control that closes a popup.

**Changes:** navigation, screen schema, reuse of the accepted v0.1 navigation-strip geometry.
**Does not change** source inventory.

| Option | Consequence |
|---|---|
| **A — I-1 as written** | Gated `Kembali` on the example screen only, returning to group master. Enforces the completion contract in §2.3. A learner who wants out before viewing all items has no exit — a usability question Bariah should weigh. |
| **B — I-12 as written** | Ungated `Kembali` on every sub-slide, returning to the immediate parent. Familiar and permissive, but **defeats the Level 2 completion gate** that I-1 §2.3 and Appendix A record as Confirmed. |
| **C — two controls** | `Kembali` gated per I-1 on the example screen; a separate, always-available popup-close control (e.g. `Tutup`) that returns to the example screen without completing the component. Closes the I-1 §4.3 naming gap. Adds a control to the lexicon. |

**Required authority:** Bariah (instructional) for gating and label; Firdaus / CAIR for the contract.
**Status: `RULING_REQUIRED`.**

---

## R-6 — Rumusan display structure and language register

**Locators**

| Artifact | Clause | Rule |
|---|---|---|
| I-12 | §5.5.1 | Rumusan **WAJIB** contain three components in order: *"1. Kepentingan Topik … 2. Apa Yang Telah Dipelajari … 3. Manfaat / Hasil"* |
| I-12 | §5.5 | *"Kandungan: Ringkasan mengikut struktur: Kepentingan → Apa yang dipelajari → Manfaat"* |
| I-12 | §8.3 | *"Narrator … menggunakan 'anda' untuk merujuk kepada pelajar"* |
| I-1 | §6.5 | *"Do not display labels such as Kepentingan, Isi Utama or Manfaat. Use contractor/site application language; avoid generic 'anda' framing."* |
| I-1 | §6.5 | *"The benefit/application clause remains a human-review item and must read as genuine site application."* |
| I-4 | slide 17 | v0.1 implements the I-1 form: labels suppressed, `kontraktor` addressee, no `anda` |

**Conflict, with a possible reconciliation.** I-12 mandates a three-part **structure**; I-1 forbids the
three **labels**. These are not necessarily the same prohibition — a Rumusan can follow the structure
without printing the labels. **That reading is offered as Option C and is not asserted as correct.**
The `anda` register conflict is direct.

**Changes:** Rumusan display, VO generation, register. **Does not change** source inventory.

| Option | Consequence |
|---|---|
| **A — I-1** | No labels; contractor/site register; benefit clause remains a human-review item. Matches v0.1 and Bariah's recorded review. Departs from the course-wide I-12 template. |
| **B — I-12** | Labelled three-part structure, `anda` register. Consistent with the other four courses. Reverses Bariah's B02 review edits. |
| **C — structure without labels** | Three-part structure retained as an authoring discipline, labels not displayed, contractor register. Satisfies the stated *intent* of both texts; satisfies the *letter* of neither completely. |

**Required authority:** Bariah (instructional). **Status: `RULING_REQUIRED`.**

---

## L-01 — "PL satu", not "PL kosong satu"

**Locators**

| Artifact | Clause | Rule |
|---|---|---|
| I-12 | §5.1, box "FORMAT VO TAJUK TOPIK" | *"VO mesti membaca PL secara penuh: 'Pakej Latihan satu' atau 'PL satu', BUKAN 'PL kosong satu'. Ini terpakai untuk semua PL dan topik."* |
| I-12 | §4.1, box "ARAHAN VO MONTAJ KURSUS" | *"VO mesti menyebut 'PL satu' (bukan 'PL kosong satu')"* |
| I-12 | §6.5 | Mandatory MMD note string: *"VO PL satu bukan PL kosong satu, dan seterusnya."* on Slide 1 and montage |
| I-1 | — | **Silent.** v0.2 contains no pronunciation rule and does not revoke this one |
| I-4 | S01 | Neither pronunciation appears — the v0.1 S01 VO does not vocalise the PL number at all — **and the required MMD note string is absent from v0.1 production notes** |

**Not a conflict — an omission on two sides.** I-12 states the rule unambiguously and course-wide. I-1
neither restates nor revokes it. v0.1 carries neither the vocalisation nor the mandated note.

**Changes:** VO generation (S01 and any montage screen) and the MMD note emission.
**Does not change** source inventory, interaction granularity, or navigation.

| Option | Consequence |
|---|---|
| **A — carry the I-12 rule forward** | S01 VO says "PL enam" / "Pakej Latihan enam"; the note string *"VO PL satu bukan PL kosong satu, dan seterusnya."* is emitted on S01. Consistent with the other four courses. Mechanical to implement. |
| **B — treat I-1 as an exhaustive replacement for B02** | The rule does not apply; S01 VO is free. Creates a pronunciation inconsistency between B02 and the rest of K5, and discards a rule with no evidence it was withdrawn. |

**This resolves mechanically once document precedence is settled** (see A-09 and matrix §6 A-01). No
independent content decision is required — only the emission rule.

**Required authority:** Bariah, contingent on the precedence ruling.
**Status: `TECHNICAL_MAPPING_REQUIRED`** — dependent on the A-09 / precedence outcome.

---

## L-02 — Mind Map on S03

**Locators**

| Artifact | Clause | Rule |
|---|---|---|
| I-12 | §4.3 row 3 | Section name is *"Pengenalan (Narrator) + **Mind Map**"* |
| I-12 | §5.3 | *"Visual On-Screen: [Image from previous Video], [Image: Narrator], **Senarai subtopik (Mind Map)**, Soalan refleksi"* |
| I-12 | §7.1 | Standard visual tag `[Mind Map]` — *"Arahan untuk paparan mind map subtopik"* |
| I-12 | §5.3.1 | VO must carry three components: Konteks, Senarai Subtopik, Soalan Refleksi |
| I-1 | §6.3 | *"Show Hilmi visually on this screen. VO begins with 'Hilmi:'… VO must contain three parts: context from S02, a list of all subtopics/components, and one open reflection question."* — **the term "Mind Map" never appears in v0.2, and no visual form is specified** |
| I-4 | S03 | v0.1 renders a plain four-line overview; no mind map, and no reflection question |

**Incompleteness rather than contradiction.** Both documents require a subtopic list. I-12 additionally
requires it to be presented as a **Mind Map** and gives it a visual tag; I-1 specifies only that the VO
list the subtopics and says nothing about the on-screen visual form.

**Changes:** S03 screen schema, visual direction, MMD asset scope. **Does not change** source inventory.

| Option | Consequence |
|---|---|
| **A — Mind Map visual (I-12 §5.3)** | S03 carries a `[Mind Map]` visual specification listing all nine components in two groups. Consistent with the other courses. Adds an MMD asset. |
| **B — plain subtopic list (I-1 §6.3 literal)** | S03 carries a text list. Simplest; matches v0.1. Drops a course-wide visual convention with no evidence it was withdrawn. |
| **C — Mind Map as the visual treatment of the I-1 list** | The I-1 subtopic list is rendered *as* a mind map. Satisfies both texts. Requires confirming that "list of all subtopics/components" and "Senarai subtopik (Mind Map)" denote the same content. |

Note: I-1 §6.3 also requires a reflection question with a **specific reference direction** — *"ask the
learner to select a suitable material for a garden seat beside a lake and justify the choice"* —
which v0.1 does not carry. That content gap travels with this issue.

**Required authority:** Bariah (instructional). **Status: `RULING_REQUIRED`.**

---

## A-05 — Single-row source tables: Papan Tanda and BBQ Pit

### A-05.1 Source inventory — preserved, not up for decision

```
Papan Tanda  = 1 meaningful source row   (K5-PL06-T03-B02-PAPAN-TANDA-ROW-01)
BBQ Pit      = 1 meaningful source row   (K5-PL06-T03-B02-BBQ-PIT-ROW-01)
```

**These counts are source evidence and are not changed by any option below.** Both rows are single
physical table rows in I-2 (p244 tbl0 r1; p249 tbl0 r1). Whatever interaction granularity is chosen,
`SOURCE_ROW_COUNT` remains **26** and both row IDs remain unchanged.

### A-05.2 The consequence that forces the question

**Locators:** I-1 §3.1 (*"Source table → generate one separate example screen"*; *"Each meaningful row
→ one clickable Level 2 item"*), I-1 §4.3 (*"Kembali MUST be disabled until all example items have
completion ticks"*), I-1 §2.3 (Local gate: *"All example/specification items for the selected component
are viewed"*).

Under a literal reading, each of these two components produces a `Contoh …` screen carrying **one**
clickable item. The Level 2 completion gate is then satisfied by a single click — a degenerate gate.

### A-05.3 Source-attested substructure — measured from I-2's text layer

Enumerator tokens verified in the rendered PDF, in reading order:

**`…-PAPAN-TANDA-ROW-01`** (module p244)

```
a. Bahan Panel:                       ← attested
     i.   Aluminium Komposit (ACP)              ← attested
     ii.  HPL (High-Pressure Laminate) Gred Luar ← attested
     iii. Akrilik (UV-Stabilized Acrylic)       ← attested
     iv.  Kayu Dirawat Tekanan/Kayu Keras       ← attested
b. Bahan Struktur/Tiang:              ← attested
     i.   Keluli Bersalut Serbuk/Tahan Karat    ← attested
     ii.  Kayu Keras/Dirawat Tekanan            ← attested
c. Grafik:                            ← attested
d. Rekaan:                            ← attested
```

**`…-BBQ-PIT-ROW-01`** (module pp. 249–250)

```
a. Bahan Pembinaan:                   ← attested   (i, ii, iii attested)
b. Dimensi Umum:                      ← attested   (i, ii attested; ii falls on p250)
c. Gril/Jeriji Memanggang:            ← attested   (i, ii attested)
d. Ciri-ciri Keselamatan & Fungsi:    ← attested   (i…v attested)
```

Both letter-level (`a.`–`d.`) and roman-level (`i.`–`v.`) boundaries are **source-attested** — they are
printed enumerators in the module, not an interpretive division.

### A-05.4 The three options

**OPTION A — one source row → one Level 2 item → one popup**

The literal row mapping in I-1 §3.1.

| | |
|---|---|
| Item count | Papan Tanda **1**; BBQ Pit **1** |
| For | Exactly what I-1 §3.1 says. No interpretive step. Zero divergence between source row and interaction item. |
| Against | One-click completion path. The Level 2 gate (I-1 §4.3, §2.3) becomes vacuous for these two components. A `Contoh …` screen with a single card is visually thin beside the 5-item Struktur Persisir Air screen. The entire specification — 10 attested sub-fields for Papan Tanda — lands in one dense popup. |

**OPTION B — one complex source row → multiple interaction items from its attested substructure**

| Granularity | Papan Tanda | BBQ Pit | Boundaries used |
|---|---:|---:|---|
| By letter (`a.`–`d.`) | **4** | **4** | letter enumerators — attested |
| By material (panel + post romans, letters `c`/`d` kept whole) | **6** | — | letters + romans under `a.`/`b.` — attested |
| Fully expanded to leaf enumerators | **8** | **12** | all letters and romans — attested |

| | |
|---|---|
| For | Produces a substantive example screen with a meaningful completion gate. Every boundary is a printed enumerator in the module — no invented division. Puts the specification detail where a learner can take it one piece at a time. |
| Against | **One source row then maps to several interaction items**, so `PROPOSED_INTERACTION_ITEM_COUNT` diverges from `SOURCE_ROW_COUNT` and the generator needs a stable sub-item identifier scheme. Three defensible granularities exist and the source does not indicate which is intended. For Papan Tanda, splitting `a. Bahan Panel` into four items presents four *materials for the same sign* as four peer items, which may misread as four sign types. |

> **These are not new source rows.** Under any granularity, `…-PAPAN-TANDA-ROW-01` and
> `…-BBQ-PIT-ROW-01` remain single source rows with unchanged IDs, and `SOURCE_ROW_COUNT` stays 26.

**OPTION C — no separate example screen; fold the specification into the main explanation screen**

| | |
|---|---|
| Item count | **0** separate interaction items for these two components |
| For | Avoids a degenerate one-item screen entirely. Keeps a single coherent screen for a component the source treats as a single record. Fewest screens. |
| Against | **⚠ This option requires an explicit override of Updated S&G v0.2.** I-1 §3.1 mandates *"Source table → generate one separate example screen titled 'Contoh [Nama Komponen]'"* with no stated exception, and I-1 §9.1 requires that *"No table is represented only as one screenshot or one summary bullet."* Adopting Option C means two of nine components deviate from the group pattern, so the Level 1 card behaviour is no longer uniform. |

### A-05.5 Authority

| Decision | Authority |
|---|---|
| Interaction granularity — which of A, B (and at which granularity), or C | **Bariah** — instructional authority |
| Adoption of that choice into the executable contract | **Firdaus / CAIR** |

**Status: `RULING_REQUIRED`. No option is selected.**

---

## A-06 — Heterogeneous table-field structures

**Locator:** I-1 §3.2 "Column-to-popup mapping" names three source fields — `Jenis / Bahan`,
`Fungsi & Penerangan`, `Contoh` — plus rules for `Embedded source image`, `No source image` and
`Missing source field` (*"Production note — Do not invent learner-facing facts"*).

**Only two of nine source tables carry all three named fields as distinct columns.** The question is
whether that is a contract conflict or a schema-adaptation task. **It is not automatically a conflict.**

### A-06.1 Field structure across all nine components

| Component | Actual source columns | Jenis / Bahan | Fungsi & Penerangan | Contoh | Equivalent field names | Genuinely missing | Covered by I-1 §3.2 "Missing source field"? | Adaptive popup with optional sections sufficient? | Human content ruling required? |
|---|---|:-:|:-:|:-:|---|---|:-:|:-:|---|
| Struktur Persisir Air | `JENIS STRUKTUR \| FUNGSI & PENERANGAN \| CONTOH` | ✅ | ✅ | ✅ | exact match | none | n/a | ✅ | **NO** |
| Struktur Teduhan | `JENIS STRUKTUR \| FUNGSI & PENERANGAN \| CONTOH` | ✅ | ✅ | ✅ | exact match | none | n/a | ✅ | **NO** |
| Kemudahan Awam | `CONTOH \| PENERANGAN` | ❌ | ✅ | ⚠ | `CONTOH` col serves as identifier; `PENERANGAN` ≡ Fungsi & Penerangan | no `Contoh` distinct from the label | ✅ yes | ✅ | **NO** |
| Water Feature | `CONTOH \| PENERANGAN` | ❌ | ✅ | ⚠ | as above | as above | ✅ yes | ✅ | **NO** |
| Kerusi Taman | `CONTOH \| SPESIFIKASI` | ⚠ packed | ⚠ substitute | ⚠ packed | type name packed in label cell; `SPESIFIKASI` stands in for Fungsi & Penerangan; `Contoh:` clause inside label cell | ROW-02 has no `Contoh:` clause | ✅ yes | ✅ | **see A-06.3** |
| Papan Tanda | `CONTOH \| SPESIFIKASI` | ⚠ packed | ⚠ substitute | ❌ | as above | no `Contoh:` clause at all | ✅ yes | ✅ | **see A-06.3** |
| Tong Sampah | `CONTOH \| SPESIFIKASI` | ⚠ packed | ⚠ substitute | ⚠ packed | as above | none | ✅ yes | ✅ | **see A-06.3** |
| Drinking Fountain | `CONTOH \| SPESIFIKASI` | ⚠ packed | ⚠ substitute | ⚠ packed | as above | none | ✅ yes | ✅ | **see A-06.3** |
| BBQ Pit | `CONTOH \| SPESIFIKASI` | ⚠ packed | ⚠ substitute | ⚠ packed | as above | none | ✅ yes | ✅ | **see A-06.3** |

Legend — ⚠ *packed*: the field exists but shares a cell with another field and must be routed, not
invented. ⚠ *substitute*: a differently-named column occupies the role.

### A-06.2 What is `TECHNICAL_SCHEMA_ADAPTATION`

Three adaptations, none of which needs a content decision:

1. **Absent `Jenis / Bahan` column (Kemudahan Awam, Water Feature).** The `CONTOH` column is the row's
   identifying field. Routing it to the item label is a mapping rule, not a content judgment.
2. **Packed label cells (five `SPESIFIKASI` components).** The label cell holds `<type name>` +
   `Contoh: <example>`. Splitting on the literal `Contoh:` token routes both to their I-1 §3.2 roles
   **without altering any text** — already done and recorded per record in the matrix.
3. **Genuinely absent fields.** `…-KERUSI-TAMAN-ROW-02` and `…-PAPAN-TANDA-ROW-01` have no `Contoh`.
   I-1 §3.2 already governs this: *"Missing source field → Production note. Do not invent learner-facing
   facts."* An adaptive popup that omits an empty section satisfies it.

**A popup template with optional sections — heading, description/specification, example (optional),
visual direction (optional) — covers all nine components.** No new contract clause is needed.

**Status for items 1–3: `TECHNICAL_MAPPING_REQUIRED`.** Authority: Firdaus / CAIR (schema).

### A-06.3 What may be `INSTRUCTIONAL_RULING_REQUIRED`

One question is **not** schema-shaped.

I-1 §3.2 maps `Fungsi & Penerangan` → *"Popup learner display + expanded VO"*. In the five
`SPESIFIKASI` components there is no `Fungsi & Penerangan` column; the substitute is a
**specification** column — dense, technical, reference-style content (materials, gauges, thicknesses,
standards). **Specification is not function.** The function of those components lives in the main
prose, which feeds the main explanation screen.

The consequence: for four of nine components the Level 2 popups would carry engineering specification
rather than functional explanation — a different learner experience from the Struktur Taman popups,
which carry genuine `FUNGSI & PENERANGAN` text.

| Option | Consequence |
|---|---|
| **A — route `SPESIFIKASI` into the popup display as-is** | Full source fidelity; dense popups; two visibly different popup characters across the bahagian. |
| **B — popup carries a functional summary, specification demoted to a reference section** | Uniform popup character. Requires deriving functional text for rows where the source supplies only specification — which risks inventing learner-facing facts, contrary to I-1 §3.2. |
| **C — accept two popup types by group** | `FUNGSI` popups for Struktur Taman, `SPESIFIKASI` popups for Perabot Taman. Honest to the source; needs an explicit rule and interacts with **R-2** (VO on specification popups). |

**Required authority:** Bariah (instructional). **Status: `RULING_REQUIRED`** — and it should be
decided together with **R-2**, which asks the VO half of the same question.

### A-06.4 Summary

```
TECHNICAL_SCHEMA_ADAPTATION      : absent Jenis/Bahan column; packed label cells; genuinely
                                   absent Contoh fields  →  already covered by I-1 §3.2
INSTRUCTIONAL_RULING_REQUIRED    : whether SPESIFIKASI content is appropriate Level 2 popup
                                   display content, or must be reframed  →  couple with R-2
```

**A missing named column is not, by itself, a contract conflict.** Eight of the nine structural
variances resolve as schema adaptation under an existing clause. One is a genuine instructional
question.

---

## A-09 — PDF versus DOCX row-structure precedence

**Locators:** full evidence in §C above. I-1 §9.1 requires *"Source page/figure locators are present in
production metadata"* but **does not name which artifact is authoritative** when the DOCX extraction
and the rendered PDF disagree on structure.

**Conflict class:** incompleteness in I-1 — no precedence rule exists.

**Changes:** source inventory **methodology** (which artifact settles a row boundary), page locators,
image ownership. **Does not change** the current 26-row count under either reading — verified in §C.4.

| Option | Consequence |
|---|---|
| **A — DOCX text + PDF structure (proposed in §C.5)** | Matches the observed reliability of each artifact. The 26-row inventory stands unchanged. Structural authority covers only pp. 237–250, the extent of the PDF extract. |
| **B — DOCX governs everything** | Single artifact, simplest custody. The seven phantom rows would have to be individually excluded by rule rather than by structural evidence, and page/figure ownership becomes unobservable. |
| **C — PDF governs everything** | Structure and pagination are reliable, but the PDF text layer breaks words across lines and columns; textual propositions would degrade. |

**Required authority:** Firdaus / CAIR. **Status: `RULING_REQUIRED`** —
`PENDING_CAIR_SOURCE_PRECEDENCE_RULING`.

---

## N-06 — Normalisation declined: unbalanced parenthesis

**Locator:** `K5-PL06-T03-B02-KERUSI-TAMAN-ROW-03`, module p243 (physical 262), I-2 p262 tbl0 r2.

**Source text, verbatim:**

```
Kerusi KompositContoh: WPC - Wood-Plastic Composite / Plastik Kitar Semula):
```

The trailing `)` has no opening parenthesis anywhere in the cell.

**Locator for the governing rule:** I-1 §3.2 — *"Jenis / Bahan → MUST preserve source meaning;
normalise only documented typos/case."* I-1 §7 lists specific permitted normalisations (`Promenade`,
`BBQ Pit`, `reka bentuk`) and **does not cover this case**.

**Why it was declined at Stage 1:** two readings are available and they are not equivalent.

| Reading | Repair | Implication |
|---|---|---|
| A dropped opening parenthesis | `Kerusi Komposit (Contoh: WPC - Wood-Plastic Composite / Plastik Kitar Semula)` | the whole clause is parenthetical to the type name |
| A stray character | `Kerusi Komposit — Contoh: WPC - Wood-Plastic Composite / Plastik Kitar Semula` | `Contoh:` is a peer field, consistent with the other four `SPESIFIKASI` components |

Choosing between them changes how the cell is parsed into `jenis_bahan` and `contoh`. **Guessing would
alter source meaning**, which I-1 §3.2 forbids.

**Changes:** the item label and `contoh` routing for one row. **Does not change** source inventory,
row count, or row identity.

| Option | Consequence |
|---|---|
| **A — leave as found** | Source fidelity preserved; the defect surfaces to the learner if the label is rendered verbatim. |
| **B — read as a dropped `(`** | Clean label; assumes an editorial intent not evidenced in the source. |
| **C — read as a stray character** | Consistent with the other four packed label cells in the same table family; also assumes intent. |
| **D — refer upstream** | Ask the module owner to correct the source, and normalise only after that. Slowest; only option that resolves the ambiguity at its origin. |

**Required authority:** Bariah (source/content). **Status: `RULING_REQUIRED`.**

---

## D.99 Issue index

| ID | Changes | Status | Authority |
|---|---|---|---|
| `R-1` | VO generation | `RULING_REQUIRED` | Bariah |
| `R-2` | VO generation, screen schema, MMD cost | `RULING_REQUIRED` | Bariah |
| `R-3` | Screen schema, screen count, generator output | `RULING_REQUIRED` | Firdaus / CAIR + Bariah |
| `R-4` | Frame screens, navigation | `RULING_REQUIRED` | Bariah + navigation owner |
| `R-5` | Navigation, screen schema | `RULING_REQUIRED` | Bariah + Firdaus / CAIR |
| `R-6` | Rumusan display, VO generation | `RULING_REQUIRED` | Bariah |
| `L-01` | VO generation, MMD notes | `TECHNICAL_MAPPING_REQUIRED` (depends on precedence) | Bariah |
| `L-02` | Screen schema (S03), visual direction | `RULING_REQUIRED` | Bariah |
| `A-05` | Interaction granularity **only** — not source inventory | `RULING_REQUIRED` | Bariah → Firdaus / CAIR |
| `A-06` (schema) | Screen schema | `TECHNICAL_MAPPING_REQUIRED` | Firdaus / CAIR |
| `A-06` (content) | Popup display content | `RULING_REQUIRED` — couple with R-2 | Bariah |
| `A-09` | Source methodology | `RULING_REQUIRED` | Firdaus / CAIR |
| `N-06` | One item label | `RULING_REQUIRED` | Bariah |

**Every pending item names its authority. No ruling is selected anywhere in this document.**

---

# Appendix A — validation harness audit

The Stage 1 harness reported 32 checks, of which **one was a confirmed false positive**: a
whole-document grep for `"not useful"` matched the narrative sentence *asserting* the exclusion rule
rather than any register value. That prompted this audit of **all 32**.

## A.1 Governing principle applied

> **No check may claim PASS on the basis of a whole-document grep when it is intended to validate a
> structured field or a register column.**

Every check now declares the structure it inspects, and the harness provides scoping helpers
(`section`, `subsection`, `record_blocks`, `field`, `register_rows`) so a check cannot silently read
prose. Whole-document scope is retained **only** for check 22, whose assertion is genuinely
document-wide.

## A.2 Two harness defects found during the audit

Both were defects in the *checking code*, not in the matrix. Both would have produced misleading
results.

| Defect | Symptom | Impact if unfixed |
|---|---|---|
| **`field()` anchored to `^-`** | Fields written mid-line after a middot separator — `- source_row_order: 1 · printed_module_page: **238** · physical_pdf_page: **257**` — were invisible to the parser | **5 spurious FAILs** (checks 7, 8, 11, 12, 16) plus a spurious FAIL on the new check 27. The document was correct throughout |
| **`subsection()` terminated on any deeper heading** | `## 1.3` contains `### Authoritative specification`, which ended the scan immediately, returning an empty string | **Check 25 passed VACUOUSLY on an empty set** — a false PASS, precisely the failure class this audit exists to catch. Now guarded by requiring ≥5 rows |

After the fix, check 25 **correctly failed**, exposing a genuine documentation gap: input row I-3b
carried no SHA-256. It was hashed and recorded rather than the check being loosened.

A **third** defect of the same class appeared in the Part F final-validation script (not in the audited
harness): a check that extracted the §D.99 issue index by splitting on the literal `---` truncated at
the markdown table's own separator row `|---|---|---|---|`, returning zero rows and reporting a
spurious FAIL on "every index row names an authority". Re-split on a horizontal rule (`\n---\n`), the
check reads all **13** index rows and passes. **The document was correct; the parser was not.**

**Pattern worth carrying into Stage 2:** all three defects were the checking code reading the wrong
span of text — never the artifact being wrong. A validator that parses Markdown by substring is itself
a source of false results in both directions, and its failures must be diagnosed before they are
believed.

## A.3 The 32 audited checks

Scope column names the exact structure inspected. All 32 exclude narrative prose except check 22,
where document-wide scope is the assertion.

| # | Check | Scope inspected | Prose excluded | Result | False-positive risk before audit | Rescoping applied |
|---|---|---|:-:|:-:|---|---|
| 1 | 26 records emitted | §4.2 bolded record IDs | YES | PASS | LOW | none |
| 2 | no duplicate `provisional_row_id` | §4.2 record IDs | YES | PASS | LOW | none |
| 3 | nine component slugs | §4.2 record IDs | YES | PASS | LOW | none |
| 4 | per-component orders 1..n | §4.2 record IDs | YES | PASS | LOW | none |
| 5 | row counts match source | §4.2 count **vs I-2 geometry** | YES | PASS | **HIGH — compared against a dict transcribed by the same author (circular)** | expectation re-derived from I-2; circularity removed |
| 6 | block count == record count | §4.2 record blocks | YES | PASS | LOW | none |
| 7 | `printed_module_page` non-empty | §4.2 field | YES | PASS | MEDIUM | value must contain a page number; parser fixed |
| 8 | `physical_pdf_page` non-empty | §4.2 field | YES | PASS | MEDIUM | as above |
| 9 | `proposed_level_2_item_label` non-empty | §4.2 field | YES | PASS | MEDIUM | value must be a real label |
| 10 | `popup_required` == YES | §4.2 field | YES | PASS | LOW | value asserted, not field name |
| 11 | `inclusion_status` == INCLUDED | §4.2 field | YES | PASS | LOW | value asserted; parser fixed |
| 12 | `exclusion_reason` non-empty | §4.2 field | YES | PASS | MEDIUM | **was field-name presence only**; now a non-empty value |
| 13 | source propositions non-empty | §4.2 `fungsi_penerangan` | YES | PASS | MEDIUM | **was field-name presence only**; now >20 chars |
| 14 | `normalisation_applied` non-empty | §4.2 field | YES | PASS | MEDIUM | was field-name presence only |
| 15 | `ambiguity_or_human_review` non-empty | §4.2 field | YES | PASS | MEDIUM | was field-name presence only |
| 16 | `evidence_reference` non-empty | §4.2 field | YES | PASS | MEDIUM | now requires an `I-n` input reference |
| 17.1–17.8 | eight sections present | line-anchored `^# ` headings | YES | PASS ×8 | MEDIUM — a prose mention could match | anchored to `^# ` |
| 18 | register has 15 entries | §5.2 `\| E-nn \|` rows | YES | PASS | LOW | none |
| 19 | every exclusion reason valid | **§5.2 Reason column only** | YES | PASS | **CONFIRMED FALSE POSITIVE** | scoped to the register table, last column, per row |
| 20 | invariant holds | §7 counts block | YES | PASS | MEDIUM — matched a pre-formatted literal, so a typo would still PASS | numbers parsed, arithmetic recomputed |
| 21 | readiness token correct | **§8 only** | YES | PASS | MEDIUM — whole-doc would match a token quoted in prose | scoped to §8; supersession note in §1 deliberately excluded |
| 22 | no `K5-DR-###` issued | whole document | N/A | PASS | LOW — assertion **is** document-wide | none; scope is correct by design |
| 23 | ID-discipline statement | **§4.0 only** | YES | PASS | MEDIUM | scoped to §4.0 |
| 24 | no ambiguous blank values | §4.2 optional field values | YES | PASS | **HIGH — original only checked the two tokens appeared somewhere** | now inspects every optional field in every record |
| 25 | input rows carry SHA-256 | **§1.3 `\| I-n \|` rows** | YES | PASS | **HIGH — vacuous pass on an empty set** | subsection parser fixed; ≥5 rows required; I-3b hashed |

## A.4 Stage 1.5 additional checks

| # | Check | Scope | Result |
|---|---|---|:-:|
| 26 | PRESERVATION — 26 record IDs match the Stage 1 set exactly | §4.2 record IDs | PASS |
| 27 | PRESERVATION — source locators match I-2 page geometry | §4.2 vs I-2 | PASS |
| 28 | PRESERVATION — 14 assets referenced, none orphaned | §4 asset IDs | PASS |
| 29 | `SOURCE_ROW_COUNT` separated from `PROPOSED_INTERACTION_ITEM_COUNT` | §8.3 | PASS |
| 30 | `IMPLEMENTATION AUTHORITY STATUS` present with required assertions | §8 | PASS |
| 31 | all 12 pending ruling IDs listed | §8.4 | PASS |
| 32 | DOCX integrity blocker recorded, no substitute hash attributed to I-3 | §1.3 + §8.5 | PASS |

## A.5 Items reclassified as human judgment

**These are reported as `HUMAN_JUDGMENT` and are never marked PASS.** A mechanical harness cannot
decide them, and marking them PASS would manufacture false assurance.

| # | Item | Why it is not mechanically decidable |
|---|---|---|
| H-1 | A row is "meaningful" | I-2 shows 26 rows with ≥2 populated cells — that is geometry. Whether each carries instructional value is an ID/SME judgment. |
| H-2 | Normalisations are correct | Typographic edits are checkable; semantic ones (N-03 sentence case, N-04 language form, N-08 `BBQ Pit` case) are editorial. N-06 is explicitly declined. Authority: Bariah. |
| H-3 | Image ownership is correct | Heading-relative geometry is measured and reproducible; the step from geometry to *semantic* ownership is a human reading. Reported as measured, not adjudicated. |
| H-4 | Proposed Level 2 labels are appropriate | Derivation from `Jenis / Bahan` is mechanical; suitability, length policy (A-08) and register are instructional. Authority: Bariah. |
| H-5 | A-05 interaction granularity | Three options evidenced; none selected. Authority: Bariah, then Firdaus / CAIR. |

## A.6 Audit totals

```
ORIGINAL CHECKS AUDITED          = 32
STAGE 1.5 CHECKS ADDED           =  7
MECHANICAL CHECKS RUN            = 39

CHECKS_CLEAN_ON_FIRST_SCOPE      =  7
CHECKS_RESCOPED                  = 32
CHECKS_FAILED_AFTER_RESCOPING    =  0
CHECKS_REQUIRING_HUMAN_JUDGMENT  =  5   (H-1 … H-5, reported as HUMAN_JUDGMENT, never PASS)
```

Harness: `…/scratchpad/audit32.py`; machine-readable results `…/scratchpad/audit32.json`.

---

# Final verdict

```
PRE_STAGE2_RULING_EVIDENCE_BLOCKED
```

Against the stated READY conditions:

| Condition for READY | Status |
|---|:-:|
| The exact module DOCX SHA-256 is obtained | ❌ **NOT OBTAINED** — §B, four routes attempted |
| The 26-row source inventory remains intact | ✅ 26 rows, 26 IDs, unchanged locators, 14 assets |
| The 32-check validation audit is complete | ✅ 32 audited + 7 added, 0 failures, 5 human-judgment |
| The conflict/ruling evidence covers all listed issues | ✅ all 12, each with options, consequences and authority |
| No unresolved integrity issue remains | ❌ **the DOCX integrity gap is unresolved** |

**Blocked on one condition only: `BLOCKED_MODULE_DOCX_INTEGRITY_NOT_VERIFIED`.** Every other READY
condition is met. §B.6 lists what would close it.

**Standing.** This document selects no governance ruling and no instructional ruling. It issues no
canonical ID, no screen ID and no popup implementation ID. K5 remains locked and the live CAIR decision
desk is untouched.
