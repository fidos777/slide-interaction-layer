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

## 2B. Upstream narrative-context artifacts — named, classified, **not yet frozen**

```
UPSTREAM_NARRATIVE_CONTEXT
COURSE_MONTAGE_HASH_RECORDED = false   ← PENDING_ARTIFACT_DELIVERY
PL06_MONTAGE_HASH_RECORDED   = false   ← PENDING_ARTIFACT_DELIVERY
```

Two Bariah-supplied montages sit upstream of B02. They are **prerequisites to the B02 learner flow,
never screens inside the B02 storyboard**, and are never counted in `LEARNER_SCREENS` or regenerated.

| Ref | Filename | Role | Relationship to B02 | Frozen? |
|---|---|---|---|:-:|
| **M1** | `SB_K5_montaj_v1.pptx` | Course Montage — K5 course-level opening | two steps upstream of B02 S01 | ❌ |
| **M2** | `SB_K5PL6_montaj_v1.pptx` | PL06 Montage — Pakej Latihan 06 opening | immediate predecessor of B02 S01; ends by naming Topik 3 as Komponen Landskap | ❌ |

Intended frozen path for both: `reviews/storyboard-bariah/v0_3_bariah_review/`.

### 2B.0 Declared identities — supplied, **not verified**

A second delivery attempt (Stage 2.1A) supplied the expected identities in the task text. They are
recorded here as a **cross-check target for whoever completes the freeze**, and they are explicitly
*not* verified digests — no bytes have been hashed, because no bytes arrived.

| Ref | Declared bytes | Declared SHA-256 | Verified? |
|---|---:|---|:-:|
| **M1** `SB_K5_montaj_v1.pptx` | 61,292 | `79a07b460ddb940de9dec0c1f92147beeb9ccf7af2b0ba35aab720369b393076` | ❌ **not computed** |
| **M2** `SB_K5PL6_montaj_v1.pptx` | 70,656 | `97ccab1c2aef889145ff416d2058a1ed848a5e0315a42308d9792ae845260390` | ❌ **not computed** |

> **These values carry no provenance weight.** They are a stated expectation, not evidence. The freeze
> is complete only when the received bytes are hashed independently and the computed digest is
> compared against the row above. The model fields `byte_size` and `sha256` in
> `B02_V0_4_MODEL_CONTRACT.json` remain `null`; the declared values live in separate
> `expected_byte_size` / `expected_sha256` fields so that no validator can mistake one for the other.

### 2B.1 Why no hash is recorded

The two files **have not reached this execution environment across two delivery attempts.** The
session upload directory holds no file matching `SB_K5*montaj*` or `*montaj*`, and its newest batch
still predates Stage 2.1. This is the same artifact-handoff class of failure documented at §5 — a
delivery-channel gap, not an absent artifact.

**No SHA-256 or byte size is computed, and no frozen copy exists.** A fabricated or assumed digest
would be worse than none: it would look like provenance while carrying none. The verified columns are
left explicitly empty so that completing the freeze fills a hole rather than overwriting a fiction.

### 2B.1a A near-miss that was deliberately rejected

A bounded search for `.pptx` files in the 55–80 KB band returned exactly one candidate:
`BARIAH_REVIEW_8SLIDES.pptx` at **68,710 bytes**. It is neither 61,292 nor 70,656, it is a different
artifact from an earlier workstream, and it was **not** adopted. Recording this matters: a
size-adjacent file in the same directory is precisely the substitution that would silently corrupt
the evidence chain.

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
