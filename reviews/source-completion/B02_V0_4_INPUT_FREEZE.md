# B02_V0_4_INPUT_FREEZE — K5 PL06 T03 B02

```
V0_4_INPUTS_FROZEN
BARIAH_FEEDBACK_ARTIFACTS_RECEIVED_AND_FROZEN
FEEDBACK_DELTA_EXECUTABLE
CAIR_INTEGRITY_EXCEPTION_FOR_REVIEW_BUILD_ONLY (carried forward, B02-CAIR-INT-001)
NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

| Field | Value |
|---|---|
| Repository | `/home/user/slide-interaction-layer` |
| Branch | `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at first freeze | `ba1f52a4c8ceef978e8b4304a1764cbeca8eadda` |
| HEAD at amendment | `5ca77dd9b3f630e1ef29b20541dc192411495c29` |
| Working tree at freeze | clean |
| First freeze date | 31 July 2026 |
| Amendment date | **1 August 2026** — Bariah feedback artifacts received and frozen (§2A) |

---

## 1. What a v0.4 freeze requires, and what is present

| # | Required input | Present | Status |
|---|---|:-:|---|
| A | v0.3 review package (becomes the v0.4 baseline) | ✅ | frozen below, §2 |
| B | v0.3 generator toolchain | ✅ | frozen below, §3 |
| C | Updated S&G v0.2 | ✅ | frozen below, §4 |
| D | Module rendered PDF | ✅ | frozen below, §4 |
| E | Module approved DOCX | ⚠ | identity pinned, **unhashed** — `B02-CAIR-INT-001` |
| F | **Bariah's review feedback on v0.3** | ✅ | **RECEIVED AND FROZEN — see §2A and §5** |
| G | Updated S&G v0.3 (supersedes v0.2 for B02) | ✅ | frozen below, §2A |

**All six required inputs are now frozen**, plus the consolidated S&G v0.3. Input E remains the single
open integrity item and is governed by `B02-CAIR-INT-001`, which is not Bariah's to close.

---

## 2. v0.4 baseline — the frozen v0.3 package

These become the *inputs* to v0.4. Any delta is computed against exactly these bytes.

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3.pptx` | 273,740 | `f4e2a3797c8cf24c9d861141a9589ae460659d591c43f691cd248c3719bc4f58` |
| `DECISION_REGISTER_B02_v0_3.json` | 10,779 | `c423d58b9125ce3668d916a80b52f6fdfa51af9f38e6199d12b26d298a1f7256` |
| `TABLE_ROW_TO_POPUP_MATRIX.md` | 83,319 | `29ee3df5e2917f568aa4884679374aa8eb5a8cc4624854b94225b8d3006482e7` |
| `STORYBOARD_SCREEN_STATE_MAP_v0_3.md` | 24,074 | `211d6fba86749b8d693232833a855c0c17480ba033d62e52c3110ec2542aabe9` |
| `STORYBOARD_SOURCE_MAP_v0_3.md` | 8,019 | `af6df1b50093f4a384388f444129e782d7070fbbeb5fedcc1c38fc498f05ad90` |
| `STORYBOARD_QA_REPORT_v0_3.md` | 8,124 | `cb457c7ea93eaf37804a3f853e7106b36864207a676bd84ee08e8e0d786e37b5` |
| `BARIAH_FEEDBACK_IMPLEMENTATION_MAP.md` | 6,748 | `c29b0ff8da374f4210f3736137556821846131c7659dbb5cdcd1a2547b8f80a9` |
| `BARIAH_REVIEW_CHECKLIST_v0_3.md` | 7,353 | `952179b105f8c72dacc03e4f7d63157aad9a0f4d53f4a772510532cea2847448` |
| `RUN_MANIFEST_v0_3.json` | 5,028 | `d486341f38124c4543a82b4880389f6087c39dc423e647cb4b7bd7dc90269b09` |
| `B02_PRE_STAGE2_RULING_EVIDENCE.md` | 57,060 | `47c4e980f8b8bdafe1434a0234bd27966ce8ff841b991b9e86af3727e24a450f` |

---

## 2A. Bariah feedback artifacts — received and frozen

```
BARIAH_FEEDBACK_ARTIFACTS_RECEIVED_AND_FROZEN
```

Frozen location: `reviews/storyboard-bariah/v0_3_bariah_review/`
Evidence date: **1 August 2026**, supplied as task attachments to this session (upload timestamps
`2026-08-01 05:16` for all four).

| # | Filename | Frozen path | Bytes | SHA-256 | Role | Authority class |
|---|---|---|---:|---|---|---|
| **A1** | `K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3_vBariah.pptx` | `reviews/storyboard-bariah/v0_3_bariah_review/` | 365,773 | `cdfc78e6395614ca79badda54ff5bbf2241c075e16ed26606fe6e69749e72809` | Bariah's annotated v0.3 deck with corrected exemplar slides | **PRIMARY — slide-level evidence** |
| **A2** | `Panduan_Semakan_Bariah_K5_PL06_T03_B02_v0.3_vBariah.docx` | `reviews/storyboard-bariah/v0_3_bariah_review/` | 43,342 | `c15ae05e20358eda17b8e272f5dd9a5ef85831016976a926346371ea5790bcf3` | completed review guide, 8 items answered | **PRIMARY — decision evidence** |
| **A3** | `K5_PL06_T03_B02_UPDATED_SG_v0.3.docx` | `reviews/storyboard-bariah/v0_3_bariah_review/` | 56,475 | `f3166e42f84d4b1f1c792c28fdc0278cc1c56a061b1598bfcce0efde91ad429d` | consolidated executable Style & Guidelines, v0.3 | **CONSOLIDATED EXECUTABLE S&G** |
| **A4** | `BARIAH_CORRECTION_EXEMPLARS_v0.4.md` | `reviews/storyboard-bariah/v0_3_bariah_review/` | 16,303 | `dec29895304f8ff08839321c2109fcca3e4db3364c341c9c833869ba06902890` | index locating the 12 corrected exemplar slides | **DERIVED — navigation aid, not authoritative** |

All four were copied byte-for-byte from the supplied originals and verified with `cmp -s`; no
normalisation, re-save or re-zip was performed. The two SHA-256 values cited *inside* A4 match the
actual bytes of A1 and A2 exactly, which is itself a consistency check on the derived index.

**A4's authority is strictly navigational.** It was used to locate corrected exemplars efficiently;
every conclusion drawn from it was re-verified against A1's slide and Notes text or A2's decision
cells. Where they diverge, the primary artifact wins — recorded in
`BARIAH_FEEDBACK_IMPLEMENTATION_MAP_v0.4.md` §4, BFB-12.

### 2A.1 How A1 encodes feedback

A1 carries **75 slides, 75 notes parts and zero PowerPoint comment parts.** Bariah annotated on-slide
rather than through the comment mechanism: 12 slides carry `Changes made. Refer next slide.` (the
following slide being the corrected exemplar) and 7 slides carry inline written directives. All 19
markers are classified in the implementation map. The relationship `slide n → RP-{n:03d}` used by the
delta protocol does **not** hold in A1, because A1 interleaves originals with exemplars; A1 locators
are therefore recorded as explicit `slide n → n+1` pairs.

### 2A.2 S&G version supersession

S&G **v0.3** (A3) supersedes S&G v0.2 as the executable style authority for B02. §4 below retains the
v0.2 hash because the v0.3 *deck* was built against it; the v0.4 delta is written against v0.3.

---

## 2B. Upstream narrative-context artifacts — frozen

```
UPSTREAM_NARRATIVE_CONTEXT
COURSE_MONTAGE_HASH_RECORDED = true
PL06_MONTAGE_HASH_RECORDED   = true
MONTAGE_FILES_FROZEN_ON_DISK = 2 of 2
FROZEN 1 August 2026 — third delivery attempt
```

Two Bariah-supplied montages sit upstream of B02. They are **prerequisites to the B02 learner flow,
never screens inside the B02 storyboard**, and are never counted in `LEARNER_SCREENS` or regenerated.

| Ref | Filename | Repository path | Bytes | SHA-256 | Role | Relationship to B02 | Frozen? |
|---|---|---|---:|---|---|---|:-:|
| **M1** | `SB_K5_montaj_v1.pptx` | `reviews/storyboard-bariah/v0_3_bariah_review/SB_K5_montaj_v1.pptx` | 61,292 | `79a07b460ddb940de9dec0c1f92147beeb9ccf7af2b0ba35aab720369b393076` | Course Montage — K5 course-level opening | two steps upstream of B02 S01 | ✅ |
| **M2** | `SB_K5PL6_montaj_v1.pptx` | `reviews/storyboard-bariah/v0_3_bariah_review/SB_K5PL6_montaj_v1.pptx` | 70,656 | `97ccab1c2aef889145ff416d2058a1ed848a5e0315a42308d9792ae845260390` | PL06 Montage — Pakej Latihan 06 opening | immediate predecessor of B02 S01; ends by naming Topik 3 as Komponen Landskap | ✅ |

| Ref | Authority / evidence source | Freeze status |
|---|---|---|
| **M1** | Bariah-supplied upstream-context artifact, delivered as a task attachment on 1 August 2026 | `FROZEN — byte-identical, independently hashed` |
| **M2** | Bariah-supplied upstream-context artifact, delivered as a task attachment on 1 August 2026 | `FROZEN — byte-identical, independently hashed` |

Both are structurally valid OOXML PresentationML packages: M1 carries 41 parts and 2 slides, M2 carries
45 parts and 3 slides, and `zipfile.testzip()` reports no corrupt member in either.

### 2B.0 Declared identities — now verified

The Stage 2.1A run recorded the expected identities as unverified cross-check targets. This run
received the bytes and hashed them independently. **Every value matches.**

| Ref | Declared bytes | Computed bytes | Declared SHA-256 | Computed SHA-256 | Verdict |
|---|---:|---:|---|---|:-:|
| **M1** | 61,292 | **61,292** | `79a07b46…b393076` | `79a07b46…b393076` | ✅ **MATCH** |
| **M2** | 70,656 | **70,656** | `97ccab1c…5260390` | `97ccab1c…5260390` | ✅ **MATCH** |

The digests were computed from the received bytes, not read from any accompanying declaration, and the
comparison target came from the task text — an independent channel from the files themselves. The
`expected_byte_size` / `expected_sha256` fields in `B02_V0_4_MODEL_CONTRACT.json` are retained
alongside the now-populated `byte_size` / `sha256` fields, so the prediction and its confirmation stay
separately auditable.

### 2B.1 Delivery history

Three attempts were needed. The record is kept because it shows what was and was not asserted while
the evidence was missing.

| Attempt | Stage | Outcome |
|---|---|---|
| 1 | 2.1 | not delivered — nothing recorded, no hash estimated |
| 2 | 2.1A | not delivered — expected identities recorded as explicitly unverified targets |
| 3 | this run | **delivered and frozen** — bytes received, hashed independently, both match |

Throughout attempts 1 and 2 the `sha256` fields stayed `null`. No digest was ever fabricated, and a
size-adjacent candidate found during attempt 2 — `BARIAH_REVIEW_8SLIDES.pptx` at 68,710 bytes, from an
earlier workstream — was deliberately **not** adopted. That rejection is what made this run a
verification rather than a first assertion.

The files arrived as two direct attachments rather than inside the announced `B02_MONTAGE_HANDOFF.zip`,
so there was no `MANIFEST.txt` to cross-check against. The comparison was made against the expected
identities in the task text instead, which is the stronger check of the two: a manifest travelling
inside the same archive as the files it describes cannot detect a substitution of both together.

### 2B.2 What is *not* blocked by this

Every ruling that depends on the montages' **content** is already recorded, because that content was
supplied in the task text itself:

| Covered by the Course Montage | Covered by the PL06 Montage |
|---|---|
| full course title | introduction to Pakej Latihan 06 |
| introduction to the eight Pakej Latihan | PL06 title |
| introduction of Hilmi | PL06 objectives |
| statement that Hilmi accompanies the learner | the seven PL06 topics |
| each PL contains topics and quizzes | Topik 3 identified as Komponen Landskap |

```
COURSE_MONTAGE_COMPLETED          = true
PL06_MONTAGE_COMPLETED            = true
HILMI_ALREADY_INTRODUCED          = true
UPSTREAM_TOPIC_LIST_ALREADY_PRESENTED = true
```

Narrative chain:

```
Montaj Kursus → Montaj PL06 → B02 S01 (Topik/Bahagian) → B02 S02 (Alya + Encik Rahman)
              → B02 S03 (Hilmi overview) → learning groups
```

B02 therefore opens at **section level**. It does not repeat the course introduction, the eight PLs,
the PL06 objectives, the seven PL06 topics, Hilmi's self-introduction, or the overall course
structure. Recorded as `B02-D-25`; the outstanding byte freeze is `B02-D-27` / dependency `U-07`.


---

## 2C. Latest Bariah screenshot evidence — frozen

```
LATEST_BARIAH_SCREENSHOT_EVIDENCE_FROZEN
SCREENSHOT_FILES_FROZEN_ON_DISK = 3 of 3
EVIDENCE_CLASS                  = BARIAH_DIRECT_SCREENSHOT
DELIVERED_AS                    = B02_BARIAH_EVIDENCE_20260801.zip
FROZEN 1 August 2026 — second delivery attempt
```

Three screenshots from Bariah's WhatsApp thread of 1 August 2026. They are the **oracle for the
Stage 4.2C rulings**: the S01 correction, the subtype visual policy, and the Struktur Persisir Air
component-main direction. Before this delivery those rulings existed only as task transcript text,
which Stage 4.2C was explicitly forbidden to treat as a screenshot oracle.

Transport archive, independently hashed on receipt:

| Archive | Bytes | SHA-256 | ZIP validity |
|---|---:|---|---|
| `B02_BARIAH_EVIDENCE_20260801.zip` | 772,667 | `25be512ea4cb9d7150c68bad82dd7f8613abc57caf9a40ff3be0baa99c2ac2ba` | valid; `testzip()` reports no corrupt member; 4 members, exactly as expected |

| Ref | Repository filename | Original filename | Bytes | SHA-256 | Subject | Frozen? |
|---|---|---|---:|---|---|:-:|
| **S1** | `B02_BARIAH_S01_EVIDENCE.jpg` | `PHOTO-2026-08-01-16-39-06.jpg` | 96,289 | `7e59a0e882c1de063f9e86ee16ea1ed079ad6bdbf95ce4998d76636b943bbff0` | S01 title, duplicate removal, visual direction, Speaker Notes | ✅ |
| **S2** | `B02_BARIAH_STRUKTUR_PERSISIR_EVIDENCE.jpg` | `PHOTO-2026-08-01-16-40-33.jpg` | 53,895 | `936b78c270274874bfa4921a35205e4ca1d679959ebf6f1880e7c76e6f890ab7` | Struktur Persisir Air component-main visual direction | ✅ |
| **S3** | `B02_BARIAH_VISUAL_POLICY_EVIDENCE.png` | `Screenshot 2026-08-01 at 5.21.12 PM.png` | 655,935 | `feb29e86228b7f240379b9830bbd59f3e30db2fae03389a68e1ba1bd32ef867b` | all examples and example popups require visuals; specification popups excepted | ✅ |

All three live in `reviews/storyboard-bariah/v0_3_bariah_review/`. The repository filenames are ASCII
aliases; **identity is bytes, hash and the recorded mapping above**, not the filename.

### 2C.1 Three-way identity concordance

Each file was hashed independently after extraction, then compared against two other statements of
the same value. All three agree for all three files, with no exceptions:

| Source of the expected value | Agreement |
|---|---|
| Independently computed from the extracted bytes | baseline |
| Task-supplied expected identities | ✅ all 3 match |
| `MANIFEST.txt` inside the archive (supplementary only) | ✅ all 3 match |

Repository copies were re-hashed after copying and compared byte-for-byte with `cmp`: **identical**.

### 2C.2 Delivery history

| Attempt | Date | Outcome |
|---|---|---|
| 1 | 1 Aug 2026 | Three filenames named in the task; no image reached any location in the container. Stage stopped with `LATEST_BARIAH_SCREENSHOT_EVIDENCE_NOT_AVAILABLE`. No hash was estimated and no transcript text was recorded as screenshot evidence. |
| 2 | 1 Aug 2026 | Delivered as a single ZIP. Verified, extracted, hashed, frozen. |

### 2C.3 What this evidence is, and is not

These are **raster images with no text layer**. The expected values used by the QA suite are
therefore **transcribed**, not machine-extracted. `generator/audit/b02_screenshot_oracle_v0_4_3.py`
records, for every value, the pixel crop it was read from, and re-hashes the file before returning
anything — so a gate built on it fails closed if the evidence is edited, replaced or removed.

One transcription limit is recorded rather than hidden: in the boxed Speaker-Notes block a trailing
full stop on lines 1 and 2 is consistent with the pixels but not separable from the spell-check
underline beneath it. The sentence-final period is carried over from the unambiguous "before" block,
whose every line ends in one.

---

## 3. Generator toolchain frozen

| Module | Bytes | SHA-256 |
|---|---:|---|
| `generator/b02_content_v0_3.py` | 39,037 | `04e56936cf2aaff5c08915d5a37cf4204055cf874151ff89b14732d5c2746bb2` |
| `generator/b02_content_v0_3.json` | 40,319 | `4401f9b54336f2c830a06e5a363479ba9ac99aefa9c80ffaa34e2161c579ac5a` |
| `generator/b02_model_v0_3.py` | 7,620 | `f05908eea56c111cea2ef918b872cd4a9ebb59ef48de3b5a21bab745870c527b` |
| `generator/b02_generator_v0_3.py` | 39,999 | `1cc9ca74b6ad50ea70c33594fa883e755ee224205048bc71ef0b10b0c76b1d35` |
| `generator/b02_render_check.py` | 11,475 | `e65b6f38e58ea88a21e60d498af99f497af62f8e3ad71c0cc42e1d0f406346e2` |
| `generator/b02_qa_v0_3.py` | 9,491 | `9d98dc164562c2f55e28f0ac5a7ff847c420bc50085596aaad3c0554243a70d4` |
| `generator/b02_docs_v0_3.py` | 8,056 | `56c7777730d7e80ccbf21319aefc7859f4441c6008efe0734d411f86c279be9d` |

Plus `generator/donor_skeleton/` (37 parts) — the PowerPoint package skeleton.

## 4. Upstream authoritative inputs (unchanged since v0.3)

| Input | Bytes | SHA-256 |
|---|---:|---|
| Updated S&G v0.2 | 51,443 | `d52f0fe123863c0d7ff968efdacda91157331f49ac46f3b3aaf2e630b3c2403a` |
| Module rendered PDF pp.237–250 | 429,918 | `30a6903dacbd7e8bce60dc1aa32026fc4ed98439054aeced9e895b5df828a3f4` |
| Module approved DOCX | 16,832,861 | **NOT OBTAINED** — Drive `16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4`, `modifiedTime 2026-06-07T23:30:02Z`. No substitute hash recorded. |
| S&G Storyboard Development v1.0 | 56,274 | Drive `1T4X-Mr8nBJhSTZ2GF62hPJHcSrPqfeCE` — cross-check only, not hashed locally |

All three re-verified byte-identical to their v0.3 values at freeze time.

---

## 5. The former blocker — superseded, and why

```
BARIAH_FEEDBACK_ARTIFACT_NOT_RECEIVED   →   SUPERSEDED 1 August 2026
BARIAH_FEEDBACK_ARTIFACTS_RECEIVED_AND_FROZEN
```

**The earlier blocker was an execution-environment artifact-handoff gap, not an absence of
stakeholder feedback.** Bariah's review existed; this session had no path to it. Recording the
distinction precisely matters, because the two conditions call for opposite responses — a missing
review means wait for the reviewer, a missing handoff means fix the delivery channel.

### 5.1 What the earlier search actually established

The search recorded at the previous freeze was sound in method and correct in what it observed. Its
scope was the failure:

| Location searched | Observed then | Why it could not have found the artifacts |
|---|---|---|
| Session upload directory | 8 files, newest the S&G v0.2 from 13:11 on 31 July | the four artifacts were attached to a **later** session turn, timestamped `2026-08-01 05:16` |
| Local filesystem globs | only an unrelated repo scorecard | the artifacts had never been written to this container |
| Drive, modified since 2026-07-30 | 4 files, none B02 | the artifacts were delivered as task attachments, not via Drive |
| Drive full-text and title queries | module DOCX, both S&G documents, unrelated K1 material | same |
| Newest Bariah-owned Drive file | a Cycle 7 spreadsheet from a different workstream | same |

Every one of those observations remains true of the state at the time. **The inference drawn from
them — that no feedback had been produced — was the error**, and it was an error of scope: the search
could only see channels the session had access to, and the actual delivery channel was not among them.

### 5.2 The correct standing conclusion

> Absence of an artifact in the session's reachable channels is evidence about the channels.
> It is not evidence about the reviewer.

Per the current task instruction, that Drive and repository search is **not to be repeated** to
re-test whether the artifacts are absent. They are task-provided attachments, now frozen at §2A with
byte-for-byte identity to the originals.

### 5.3 What did not change

No comment was ever fabricated during the blocked period. The delta machinery built while blocked —
the classification schema, the measured propagation scope and the register-update contract in
`B02_FEEDBACK_DELTA_PROTOCOL_v0_4.md` — was built to be independent of the comments' content, and it
absorbed the real feedback without amendment. The one behavioural note is that A1 uses on-slide
annotation rather than PowerPoint comment parts, so the protocol's `slide n → RP-{n:03d}` shortcut
does not apply to it; see §2A.1.

---

## 6. What this freeze does and does not authorise

| | |
|---|---|
| **Does** | Lock the exact bytes any v0.4 delta is computed against, **including Bariah's four feedback artifacts**. Establish the propagation-scope model, the Stage 2 interaction taxonomy and the executable feedback delta. |
| **Does not** | Authorise generator changes, PowerPoint regeneration, component propagation, canonical freeze, production approval, MMD build or multimedia binding. |

No generator was modified and no PowerPoint was regenerated in producing this freeze.
