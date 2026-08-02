# PL06 source-boundary freeze — ingested subset

Stage 4.2F-A2. Thirteen files from `PL06_SOURCE_BOUNDARY_EVIDENCE_FREEZE_v1.zip`
(25,142,903 B, `c32f9bee…cd3927`), ingested **byte-identically**. The package verified
29/29 manifest artifacts and 30/30 hash-register lines before ingest.

## What is here

| File | Role |
|---|---|
| `SOURCE_CUSTODY_RECORD.md` | frozen — what the package asserts about custody |
| `PL06_EXTERNAL_CUSTODY_RECORD_v1.md` | **repository-owned** — what this repo decided to do about it |
| `BOUNDARY_EVIDENCE_REGISTER.md` | frozen — topology, shared pages, T04 boundary |
| `FREEZE_MANIFEST.json` | frozen — 29 artifact identities |
| `SHA256SUMS.txt` | frozen — 30 hash lines |
| `PL06_LESSON_BOUNDARY_MAP_v1.{md,csv,json}` | frozen — the 14-unit map |
| `PL06_TOPIK_LIST_USER_SCREENSHOT_2026-08-02.png` | frozen — user-provided, non-reproducible |
| `boundary_pages/p294.png`, `p302.png` | frozen — T04-B01 start and stop evidence |
| `PACKAGE_README.md` | frozen — the package's own README |
| `tools/verify_freeze.sh`, `tools/verify_manifest.py` | frozen — the package's verifiers |

## The two tools do not run here

`verify_freeze.sh` and `verify_manifest.py` expect the **full** package layout —
`source/`, `derived/`, `records/`, all 29 artifacts. This directory holds thirteen of them,
flattened. Running them here will report the other sixteen as `MISSING`, correctly.

They are tracked because they are part of the freeze record, not because they are runnable
against this subset. The subset **is** verified, on every QA run, by
`INGESTED_FILES_MATCH_FREEZE_HASHES` in `docs/pl06/tools/pl06_inventory_qa_v1.py`, which
re-hashes each of the thirteen against `FREEZE_MANIFEST.json` and `SHA256SUMS.txt`.

To run the package's own tools, obtain the full ZIP — see
`PL06_EXTERNAL_CUSTODY_RECORD_v1.md` §2, where its durable location is currently
`NOT_YET_SUPPLIED`.

## What is deliberately absent

The 16.8 MB DOCX, the 9.0 MB rendered PDF, fifteen of the seventeen boundary-page images and
the contact sheet. See `PL06_EXTERNAL_CUSTODY_RECORD_v1.md` for each one's classification and
identity.

## What the freeze does not establish

The 14-lesson grouping is anchored to DOCX body headings, but the human authority behind
*those particular groupings* — `SMC-CIDB-K5-DAFTAR-KEPUTUSAN-BARIAH-KONSOLIDASI_v1.0`,
`K5-STR-004`/`K5-STR-006` — is referenced by the map and is **not** in this repository or in
the package. Recorded as `PL06_14_UNIT_GROUPING_AUTHORITY = REFERENCED_NOT_FROZEN` in
`docs/pl06/tools/pl06_inventory_data_v1.py` and gated.
