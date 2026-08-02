# PL06_FIRST_SCALE_OUT_SELECTION — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py`.

```
SELECTED_FIRST_SCALE_OUT_UNIT = K5-PL06-T04
SELECTION_STATUS = SELECTED_CONDITIONAL_PENDING_SOURCE_DELIVERY
SELECTION_IS_UNCONDITIONAL = false
```

# 1. Scoring

Scores are 0–5. **A criterion with no evidence scores 0, not a midpoint.** That is why four of the ten columns are zero for every candidate.

| candidate | source_completeness | source_authority | visual_availability | interaction_representativeness | quiz_completeness | generator_compatibility | qa_compatibility | b02_coupling_exposure | expected_proof_value | estimated_duration | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `K5-PL06-T04` | 0 | 2 | 0 | 0 | 0 | 3 | 3 | 5 | 5 | 3 | 21 |
| `K5-PL06-T03-BNEXT` | 0 | 4 | 0 | 0 | 0 | 4 | 4 | 1 | 2 | 4 | 19 |
| `K5-PL06-T01` | 0 | 2 | 0 | 0 | 0 | 2 | 2 | 5 | 4 | 2 | 17 |
| `K5-PL06-T02` | 0 | 2 | 0 | 0 | 0 | 3 | 3 | 4 | 4 | 3 | 19 |
| `K5-PL06-T07` | 0 | 2 | 0 | 0 | 0 | 2 | 2 | 5 | 3 | 2 | 16 |

Notes on each candidate:

- **`K5-PL06-T04`** — Topik 4 — Penjagaan Dan Penyelenggaraan. Different Topik, so a successful build proves portability rather than repeating B02's grammar. Adjacent to the only page range whose custody chain is proven, so one contiguous extraction request covers it.
- **`K5-PL06-T03-BNEXT`** — Topik 3 — the next Bahagian after B02. Strongest existence evidence of any non-B02 unit — a human ruled in writing that the B02 learner navigates to it. But it sits in the same Topik as B02 and would very likely reuse B02's component grammar, so a green build would prove almost nothing about portability.
- **`K5-PL06-T01`** — Topik 1 — Proses Memula Kerja. A process topic is structurally furthest from B02's component catalogue, which is high coupling exposure but also the highest chance of needing new treatment. Not a first proof.
- **`K5-PL06-T02`** — Topik 2 — Elemen Pembinaan Landskap. An element catalogue is plausibly close to B02's structure. Reasonable runner-up to T04 on the same evidence footing.
- **`K5-PL06-T07`** — Topik 7 — Demobilisasi. Likely the smallest unit and likely process-shaped. 'Likely' is doing all the work in that sentence — nobody has read it.

# 2. Selection rationale

- It is a different Topik from B02, which is the only way a first scale-out proof can distinguish portable capability from B02-shaped capability. A build inside Topik 3 that went green would not tell us which of the two we have.
- Its existence and title are source-attested by the frozen PL06 montage — the same class of evidence available for every other Topik, and the best available for any of them.
- It is adjacent to modul ms 238-249, the only page range whose custody chain this project has ever completed, so the extraction request that unblocks it is a contiguous continuation rather than a new acquisition.
- It scores highest on expected proof value among candidates that are not inside Topik 3.

# 3. What this selection is not

This selection is NOT a readiness statement. Every candidate scored ZERO on source completeness, visual availability, interaction representativeness and quiz completeness, because no source document exists in custody for any of them. T04 wins a comparison between units we cannot yet build. The differentiators that decided it — proof value and extraction adjacency — are planning judgements, not measurements, and the ranking should be re-run the moment any unit's source actually arrives, because a single page of real content will outweigh all of it.

# 4. Rejected candidates

| unit_id | reason |
|---|---|
| `K5-PL06-T03-BNEXT` | Same Topik as B02. Highest existence evidence, lowest proof value — a green build would most likely be B02's grammar succeeding at B02's shape. |
| `K5-PL06-T02` | Equal evidence footing with T04, slightly lower expected proof value. Retained as first runner-up. |
| `K5-PL06-T01` | A process topic is the most likely to require new treatment, which makes it a poor FIRST proof and a good second one. |
| `K5-PL06-T07` | Everything asserted about its size and shape is guesswork. |
| `K5-PL06-T05` | Not scored separately — same zero source footing, no differentiator. |
| `K5-PL06-T06` | Not scored separately — same zero source footing, no differentiator. |

# 5. Required preconditions

None of these is ours to satisfy alone.

- PRE-01 — the approved module extract covering Topik 4 is delivered, with byte size and SHA-256, and frozen in the repository (resolves STOP-001)
- PRE-02 — the Bahagian boundaries of Topik 4 are stated by a human with authority, including how many there are and what each is called (resolves STOP-002)
- PRE-03 — figures and table photographs are extracted from the delivered range and hashed into an asset manifest (resolves STOP-003)
- PRE-04 — the quiz source and answer key for the selected Bahagian are supplied and SME-signed (resolves STOP-005)
- PRE-05 — the cast binding for non-B02 PL06 units is settled against the ratified character bank (resolves STOP-006, SRC-ANOM-003)
- PRE-06 — written confirmation of Bariah's call approval is received and frozen, upgrading APPROVAL_RECORD from FIRDAUS_ATTESTED_BARIAH_CALL

# 6. Expected end-to-end path

1. freeze the delivered source extract and its hash
2. extract and hash figures and table photographs into an asset manifest
3. derive the controlled content module from the source — no content invented
4. derive the screen / state / interaction-item model and its counts from that content
5. re-derive the interaction pattern from the unit's own structure; do NOT import FAMILY_S / P1 / P2
6. generate the review deck through the shared shell, with the artifact-identity source carrying the new unit's version line
7. run the portable gate set, then add unit-specific content gates
8. build mutation fixtures for every unit-specific rule
9. render and inspect every page
10. Microsoft PowerPoint smoke — and record it this time
11. Bariah review

Step 5 is the one that matters for a scale-out proof. If the unit's structure is re-derived and it happens to land on something like Family S, that is a finding. If Family S is imported and then found to fit, that is not a finding — it is the architecture answering its own question.
