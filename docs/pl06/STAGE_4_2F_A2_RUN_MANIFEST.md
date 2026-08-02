# STAGE_4_2F_A2_RUN_MANIFEST

```
STAGE  = 4.2F-A2 — CONTROLLED PL06 SOURCE INGEST
SCOPE  = SOURCE INGEST, INVENTORY CORRECTION, QA EXTENSION
PPTX_GENERATED = 0
VERDICT = PL06_SOURCE_BOUNDARY_INGEST_COMPLETE_READY_FOR_T04_EXTRACTION
```

# 1. Pre-flight

| Check | Result |
|---|---|
| Repository | `/home/user/slide-interaction-layer` |
| Branch | `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at start | `3ef866de7931a6e3a0cdddbc58c5825ff4ee64fd` — matches |
| Tracked-file changes at start | **0** |
| Package bytes | **25,142,903** — matches |
| Package SHA-256 | `c32f9bee73f9044f3b041417d6a8955854bc6c1e62045fd5fa96d37b56cd3927` — matches |
| `sha256sum -c SHA256SUMS.txt` | **30 OK, 0 FAILED** |
| `verify_freeze.sh` | **PASS 29/29 artifacts verified** |

# 2. Grouping authority

```
PL06_14_UNIT_GROUPING_AUTHORITY = REFERENCED_NOT_FROZEN
```

Searched the repository for `SMC-CIDB-K5-DAFTAR-KEPUTUSAN-BARIAH-KONSOLIDASI_v1.0`,
`K5-STR-004`, `K5-STR-006` and `K5-STR-005`. **Zero occurrences** outside the freeze
package's own metadata, which is a reference to the artifact, not the artifact.

What the freeze does establish: every unit's start and end is a **named DOCX body heading
with a paragraph index**, independently checkable against the source. What it does not
establish is *why these particular fourteen groupings* — two adjacent subtopics being one
lesson rather than two is a human decision and the record of it is elsewhere.

Not a blocker for T04 extraction, by instruction and on the merits: Topik 4 contains exactly
one lesson, so no grouping judgement enters it. It matters most for Topik 1, 2 and 3, where
3 + 2 + 5 lessons were grouped out of subtopics that could have been divided differently.
Recorded as `STOP-013`, scope `BLOCKS_CANONICAL_FREEZE_ONLY`.

# 3. Tracked files — 15, 464 KB

Ingested to `docs/pl06/source-freeze/`. All thirteen frozen files re-hashed after copying and
verified against **both** `FREEZE_MANIFEST.json` and `SHA256SUMS.txt`: **zero mismatches.**

| File | Bytes | SHA-256 (16) | Source |
|---|---:|---|---|
| `SOURCE_CUSTODY_RECORD.md` | 2,142 | `23782ddd559593c9` | frozen |
| `BOUNDARY_EVIDENCE_REGISTER.md` | 1,224 | `bda6b1889adc4add` | frozen |
| `FREEZE_MANIFEST.json` | 12,167 | `8747fd311ec164a7` | frozen |
| `SHA256SUMS.txt` | 3,037 | `0fe9ccb8d6d446f3` | frozen |
| `PL06_LESSON_BOUNDARY_MAP_v1.md` | 9,146 | `26d5f5604228c0a9` | frozen |
| `PL06_LESSON_BOUNDARY_MAP_v1.csv` | 5,128 | `bbe22c9d332e7616` | frozen |
| `PL06_LESSON_BOUNDARY_MAP_v1.json` | 12,977 | `aa02cd3c784113b0` | frozen |
| `PACKAGE_README.md` | 993 | `c3ba4e371b5ee40d` | frozen (`README.md`) |
| `tools/verify_freeze.sh` | 151 | `5aee366e8eb38492` | frozen |
| `tools/verify_manifest.py` | 880 | `0f0908ac45c6e0be` | frozen |
| `PL06_TOPIK_LIST_USER_SCREENSHOT_2026-08-02.png` | 74,122 | `db944526c0246e65` | frozen |
| `boundary_pages/p294.png` | 93,975 | `e51574b6d57a034a` | frozen — T04 start |
| `boundary_pages/p302.png` | 156,560 | `243d11590b86c6d1` | frozen — T04 stop |
| `PL06_EXTERNAL_CUSTODY_RECORD_v1.md` | — | — | **repository-owned**, new |
| `README.md` | — | — | **repository-owned**, new |

## 3.1 One deviation, stated

The brief said to update the custody record. `SOURCE_CUSTODY_RECORD.md` is **frozen
evidence** carrying a manifest hash, and the gate `INGESTED_FILES_MATCH_FREEZE_HASHES`
verifies it on every run. Editing it would break that check and would mean amending an
artifact whose purpose is to be unamendable.

So the frozen record is preserved byte-identically and the custody decisions are recorded in
a new repository-owned file, `PL06_EXTERNAL_CUSTODY_RECORD_v1.md`. Nothing is lost: the
frozen record states what the package asserts, the new one states what this repository
decided.

The two frozen verifier tools are tracked but **cannot run against this subset** — they
expect all 29 artifacts in the original layout. That is documented in the directory README.

# 4. External custody

| Artifact | Bytes | Custody |
|---|---:|---|
| Primary DOCX | 16,832,861 | **`EXTERNAL_DURABLE_SOURCE_BY_IDENTITY`** — Drive `16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4`, sha `5a9142cd…78df7` |
| Freeze ZIP | 25,142,903 | **`DURABLE_CUSTODY_PENDING`** — no durable location supplied |
| Rendered PDF | 9,039,981 | **`DERIVED_ARTIFACT_PRESERVED_INSIDE_FREEZE_PACKAGE`**, 350 pages |
| Git LFS | — | `NOT_CONFIGURED` |
| Shared team custody | — | **not claimed** |

`DURABLE_CUSTODY_PENDING` is an open item, `STOP-014`. `incoming/` and `tmp/` are not durable
custody and both are deleted by this stage. What survives is the identity of the ZIP and of
every file in it, thirteen of its files ingested, and the DOCX in Drive. What does not
survive is the ZIP's own bytes — and with them the rendered PDF, fifteen boundary images and
the contact sheet. Re-rendering the DOCX will not reproduce `295a1749…`, so that hash becomes
checkable but no longer producible.

# 5. Corrected inventory

| | Stage 4.2F-A | Stage 4.2F-A2 |
|---|---|---|
| Units | 8, Topik granularity | **14**, lesson granularity |
| Topology | not established | **3 / 2 / 5 / 1 / 1 / 1 / 1** |
| Bahagian enumerated | 1 of unknown | **14 of 14** |
| B02 bahagian title | `Komponen Landskap` *(the Topik title)* | **`Struktur Taman dan Perabot Taman`** |
| `T03-BNEXT` | attested, unnumbered | **`K5-PL06-T03-B03` Infrastruktur, modul 250–255** |
| Preferred first proof | `K5-PL06-T04` | **`K5-PL06-T04-B01`**, modul 276–283 |
| Source authority | `SOURCE_AUTHORITY_UNRESOLVED` ×7 | **resolved for all 14** |

Every unit row is now **read from** `PL06_LESSON_BOUNDARY_MAP_v1.json`, not asserted in the
data module. The inventory cannot drift from the boundary evidence: change the map and the
inventory follows, or the hash gate fails and nothing is emitted.

Execution order: 0 = the delivered B02, 1 = the designated first proof, then **module page
order** — mechanical and traceable rather than a judgement.

# 6. Readiness and lanes

| Readiness | Units |
|---|---:|
| `READY_WITH_HOLDS` | 1 — the delivered B02 |
| `SOURCE_INCOMPLETE` | 13 |
| `READY` | **0** |

| Lane | Units |
|---|---:|
| `LANE_A_EXISTING_SUPPORTED_PATTERN` | 1 |
| `LANE_B` / `LANE_C` | 0 |
| `LANE_D_SOURCE_INCOMPLETE` | 13 |

The thirteen are still Lane D, but for a **different and much weaker reason** than yesterday.
Before, no source existed at all. Now the source and the boundaries are in custody and what
is missing is that nobody has read the content. The lane moves at extraction, not before —
a unit cannot be classified against generator capability until its structure is known.

Stop conditions: **2 RESOLVED** (`STOP-001` missing source, `STOP-002` missing boundary),
12 OPEN — 4 `BLOCKS_THIS_UNIT`, 4 `BLOCKS_CANONICAL_FREEZE_ONLY`, 3 `BLOCKS_FINAL_RELEASE_ONLY`,
1 `BLOCKS_MMD_ONLY`.

# 7. QA

| Metric | Value |
|---|---:|
| `ACTIVE_TEST_GATES_PASSING` | **136 / 136** |
| `SUPERSESSION_MARKERS_PRESENT` | **0** |
| `TOTAL_EMITTED_GATE_RECORDS` | **136** |

Every record carries an explicit `gate_type`; nothing is classified by ID substring.
New types this stage: `SOURCE_CUSTODY` (13) and `BOUNDARY_INTEGRITY` (23).

| `gate_type` | Gates |
|---|---:|
| `BOUNDARY_INTEGRITY` | 23 |
| `AUTHORITY_DISCIPLINE` | 22 |
| `INVENTORY_INTEGRITY` | 18 |
| `ARTIFACT_AGREEMENT` | 17 |
| `SELECTION_INTEGRITY` | 13 |
| `SOURCE_CUSTODY` | 13 |
| `STOP_CONDITION` | 10 |
| `PLAN_INTEGRITY` | 9 |
| `RULE_PORTABILITY` | 9 |
| `ACCOUNTING` | 2 |

# 8. Mutations

**54 fixtures, 54 detected, 0 missed, 0 baseline false failures.** 22 are new to this stage,
covering every correction: unit count, topology, B02 title regression, the BNEXT placeholder,
T04 page range and anchors, shared-boundary pages, custody classifications, DOCX identity,
the forbidden-tracked guard list, grouping-authority upgrade, stop-status discipline and the
verdict.

## 8.1 Four stale gates the fixtures caught

Worth recording, because it is the same species of defect as `B02-META-REG-001` and it was
found the same way — by a negative fixture, not by a green suite.

Rewriting the inventory silently switched four gates off:

- **`UNSUPPORTED_INTERACTION_CLASSIFIED_READY`** matched one literal
  (`NOT_DETERMINABLE_WITHOUT_SOURCE`) that the new data renamed. It matched nothing and
  passed. Now matches the `NOT_DETERMINABLE` prefix.
- **`EXISTENCE_ONLY_EVIDENCE_CLAIMING_CONTENT`** listed the old attestation vocabulary and
  did not include `UNIT_BOUNDARY_AND_PAGE_RANGE`, so the thirteen new units fell outside it.
- **`UNIT_CLAIMING_CONTENT_WITHOUT_SOURCE_DOCUMENT`** was pinned to
  `source_document == "NONE_IN_CUSTODY"`, a population that emptied the moment the module
  arrived. **The gate went vacuous.**
- **`SOURCELESS_CANDIDATE_SCORED_ON_CONTENT`** was pinned to `source_completeness == 0`,
  which stopped selecting anything for the same reason.

A fifth, `FORBIDDEN_TRACKED_FULL_DOCX`, could be switched off by deleting its pattern from
the guard list — the gate simply stopped being emitted. `FORBIDDEN_TRACKED_PATTERNS_COMPLETE`
now pins the list itself before it is iterated.

All five are fixed at the gate, not by adjusting the fixture to match. A green suite would
have shipped all five.

# 9. Staging cleanup

`incoming/pl06/PL06_SOURCE_BOUNDARY_EVIDENCE_FREEZE_v1.zip` and
`tmp/pl06-source-boundary-v1/` deleted after tracked files were verified, custody recorded,
QA passed and mutations passed. Zero residue. The upload outside the repository environment
is untouched.

# 10. Constraints honoured

- No PPTX generated, patched or opened.
- No generator or validator under `reviews/source-completion/` modified — 0 changed files there.
- No MMD, React or SCORM work.
- `3ef866d` not amended.
- Git LFS not installed or configured; no `.gitattributes` created.
- `.gitignore` not modified.
- No DOCX, PDF or ZIP entered the Git index — gated by `FORBIDDEN_TRACKED_*`.
