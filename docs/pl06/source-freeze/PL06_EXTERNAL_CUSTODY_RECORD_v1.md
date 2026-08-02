# PL06_EXTERNAL_CUSTODY_RECORD — v1

Stage 4.2F-A2. **Repository-owned.** This is the custody extension required by the ingest
brief.

## Why this is a separate file

The brief asked for the custody record to be updated. `SOURCE_CUSTODY_RECORD.md` in this
directory is **frozen evidence** — it carries a manifest hash
(`23782ddd559593c9…`) and the gate `INGESTED_FILES_MATCH_FREEZE_HASHES` verifies it against
`FREEZE_MANIFEST.json` on every run. Editing it would break that check and would mean
amending an artifact whose whole purpose is to be unamendable.

So the frozen record is preserved byte-identically and the custody decisions this repository
makes are recorded here instead. Nothing is lost: the frozen record states what the package
asserts, this record states what the repository has decided to do about it.

## 1. Primary source DOCX

| Field | Value |
|---|---|
| Filename | `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx` |
| Bytes | **16,832,861** |
| SHA-256 | `5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7` |
| Google Drive file ID | `16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4` |
| Drive folder | `https://drive.google.com/drive/folders/1p18qHATFfn0oLHyCvYOfA8rQQlxkwJXS` |
| Reported Drive size | 16,832,861 B — agrees with the measured byte count |
| Reported modified | `2026-06-07T23:30:02.000Z` |
| Evidence class | `PRIMARY_SOURCE_ARTIFACT` |
| Authority | `PROOFREAD_FINAL_MODULE_SOURCE` |
| **Custody** | **`EXTERNAL_DURABLE_SOURCE_BY_IDENTITY`** |
| Tracked in Git | **No** — by decision, and following the B02 precedent |

The DOCX is not in this repository and is not intended to be. It is bound here by exact
identity: any future copy that hashes to `5a9142cd…78df7` is this source, and any copy that
does not is a different document regardless of its filename.

This follows the established convention. B02's source PDF (429,918 B,
`30a6903dacbd7e…`) was never committed either — only its identity was recorded, in
`B02_PRE_STAGE2_RULING_EVIDENCE.md` I-2 and `TABLE_ROW_TO_POPUP_MATRIX.md` — and only the 14
bounded crops were tracked.

## 2. Freeze transport package

| Field | Value |
|---|---|
| Filename | `PL06_SOURCE_BOUNDARY_EVIDENCE_FREEZE_v1.zip` |
| Bytes | **25,142,903** |
| SHA-256 | `c32f9bee73f9044f3b041417d6a8955854bc6c1e62045fd5fa96d37b56cd3927` |
| Contents | 29 manifest artifacts + `SHA256SUMS.txt`, all verified 29/29 and 30/30 |
| Evidence class | `TRANSPORT_ONLY` |
| **Durable location** | **`NOT_YET_SUPPLIED`** |
| **Custody** | **`DURABLE_CUSTODY_PENDING`** |
| Tracked in Git | **No** — by decision |

### 2.1 This is an open item, not a closed one

No durable location has been supplied for the ZIP. The brief is explicit that the
repository's `incoming/` and `tmp/` directories must **not** be described as durable custody,
and they are not: both are untracked, both sit in an ephemeral container, and both are
deleted at the end of this stage.

What survives this stage is:

- **the identity** of the ZIP and of every file inside it, tracked here and in
  `FREEZE_MANIFEST.json` / `SHA256SUMS.txt`;
- **thirteen of its files**, ingested byte-identically into this directory;
- **the DOCX**, externally durable in Drive by identity.

What does **not** survive is the ZIP's own bytes, and with them the rendered PDF, the other
fifteen boundary-page images and the contact sheet. Those become re-derivable only by
re-rendering the DOCX. Re-rendering will not reproduce the frozen PDF hash — a different
renderer or version produces different bytes — so `295a1749cf3f…` would become an identity
that can be checked against but no longer produced.

`DURABLE_CUSTODY_PENDING` closes when a Drive location for the ZIP is supplied and recorded
here. Until then, do not describe the freeze package as durably held.

### 2.2 Classification if only a local path is known

If the ZIP is held only at a local or iCloud path on an individual's machine, the correct
classification is **`USER_CONTROLLED_EXTERNAL_CUSTODY`** — not shared team custody. That
distinction is not pedantry: a path on one laptop is not a location the team can verify
against, and this project has already lost a source once by assuming otherwise
(`SOURCE_CUSTODY_AND_COVERAGE.md` F2).

`SHARED_TEAM_CUSTODY` may be claimed only once a Drive location is recorded above.

## 3. Rendered PDF

| Field | Value |
|---|---|
| Filename | `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.pdf` |
| Bytes | 9,039,981 |
| SHA-256 | `295a1749cf3fce16d9dfd8c3b45b2e3b5c64c1c9a6073ccc26235f81ec6fbb4b` |
| Pages | **350** — verified independently via the PDF Pages-tree `/Count` and by counting `/Type /Page` objects |
| Evidence class | **`DERIVED_ARTIFACT_PRESERVED_INSIDE_FREEZE_PACKAGE`** |
| Tracked in Git | **No**, and not tracked separately by decision |

A note for whoever checks this later: the `file` utility reports this PDF as **944 pages**.
That is wrong — it reads an outline or structure-tree `/Count`. The authoritative page count
is **350**, and it agrees with the freeze manifest and the boundary map metadata. Do not
propagate 944.

## 4. Boundary-page images

Two of the seventeen are tracked, by decision: `boundary_pages/p294.png` and
`boundary_pages/p302.png` — the rendered pages that evidence the selected `K5-PL06-T04-B01`
start heading and the `5.0 PENGURUSAN KUALITI PROJEK` heading that defines its stop.

The other fifteen and the contact sheet are `REPRODUCIBLE_INSPECTION_ARTIFACT` and are not
tracked. Their identities remain in `FREEZE_MANIFEST.json`, so a later stage can verify a
re-supplied copy even though it cannot regenerate one from this repository.

## 5. Git LFS

Not installed, not configured, and not proposed. There is no `.gitattributes` and no LFS
pointer in this repository. The tracked ingest is 464 KB against a pack of 309 KB, which
needs no LFS; the 24.67 MB that would have needed it is held externally by identity instead.

## 6. Standing

```
PRIMARY_DOCX_CUSTODY        = EXTERNAL_DURABLE_SOURCE_BY_IDENTITY
FREEZE_PACKAGE_CUSTODY      = DURABLE_CUSTODY_PENDING
RENDERED_PDF_CUSTODY        = DERIVED_ARTIFACT_PRESERVED_INSIDE_FREEZE_PACKAGE
GIT_LFS                     = NOT_CONFIGURED
SHARED_TEAM_CUSTODY_CLAIMED = false
```
