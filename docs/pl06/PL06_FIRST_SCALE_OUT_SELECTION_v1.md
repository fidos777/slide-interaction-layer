# PL06_FIRST_SCALE_OUT_SELECTION — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py`.

```
SELECTED_FIRST_SCALE_OUT_UNIT = K5-PL06-T04-B01
SELECTION_STATUS = SELECTED_CONDITIONAL_PENDING_CONTENT_EXTRACTION
SELECTION_IS_UNCONDITIONAL = false
```

# 1. Scoring

Scores are 0–5. **A criterion with no evidence scores 0, not a midpoint.** That is why four of the ten columns are zero for every candidate.

| candidate | source_completeness | source_authority | visual_availability | interaction_representativeness | quiz_completeness | generator_compatibility | qa_compatibility | b02_coupling_exposure | expected_proof_value | estimated_duration | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `K5-PL06-T04-B01` | 4 | 4 | 0 | 0 | 0 | 3 | 3 | 5 | 5 | 4 | 28 |
| `K5-PL06-T03-B03` | 4 | 4 | 0 | 0 | 0 | 4 | 4 | 1 | 2 | 5 | 24 |
| `K5-PL06-T07-B01` | 4 | 4 | 0 | 0 | 0 | 2 | 2 | 5 | 3 | 4 | 24 |
| `K5-PL06-T05-B01` | 4 | 4 | 0 | 0 | 0 | 2 | 2 | 5 | 4 | 3 | 24 |
| `K5-PL06-T02-B02` | 4 | 4 | 0 | 0 | 0 | 3 | 3 | 4 | 4 | 3 | 25 |

Notes on each candidate:

- **`K5-PL06-T04-B01`** — Topik 4 Bahagian 1 — Penjagaan dan Penyelenggaraan. Designated PREFERRED_FIRST_SCALE_OUT_PROOF by the freeze package itself. Different Topik from B02; clean page boundary on both sides — no shared page, no heading split; the smallest remaining unit at 8 module pages; and the only unit whose boundary carries frozen visual evidence in this repository (p294, p302).
- **`K5-PL06-T03-B03`** — Topik 3 Bahagian 3 — Infrastruktur. This is what Stage 4.2F-A called T03-BNEXT — the unit Bariah's Tamat ruling sends the B02 learner to. Smallest of all at 6 module pages, but it sits in B02's own Topik and both its boundaries are shared pages. A green build here would most likely be B02's grammar succeeding at B02's shape.
- **`K5-PL06-T07-B01`** — Topik 7 Bahagian 1 — Demobilisasi. 7 module pages, clean boundaries, three subtopics. Structurally furthest from a component catalogue, which is high coupling exposure and also the highest chance of needing new treatment.
- **`K5-PL06-T05-B01`** — Topik 5 Bahagian 1 — Pengurusan Kualiti Projek. 10 module pages, four subtopics, clean boundaries. Good proof value; larger and more procedural than T04.
- **`K5-PL06-T02-B02`** — Topik 2 Bahagian 2 — Mekanikal & Elektrikal (M&E). 11 module pages with a shared start page, so it also exercises heading-anchor extraction. Worth doing early, but not first — one new variable at a time.

# 2. Selection rationale

- The freeze package designates it PREFERRED_FIRST_SCALE_OUT_PROOF in the frozen boundary map — this is no longer only our judgement.
- It is a different Topik from B02, which is the only way a first scale-out proof can distinguish portable capability from B02-shaped capability.
- Its boundary is clean on both sides: shared_start and shared_end are both false, and the map records 'page boundary is clean'. Six of the fourteen units start or end on a shared page; this one does not, so extraction is not also a test of heading-anchor splitting.
- At 8 module pages (276-283) it is among the smallest units, and it is the only unit whose start and stop headings are backed by frozen page images in this repository — p294 for '4.0 PENJAAGAAN DAN PENYELENGGARAAN' and p302 for the '5.0 PENGURUSAN KUALITI PROJEK' heading that defines its stop.
- The 14-lesson grouping authority being unfrozen does not touch it: Topik 4 has exactly one lesson, so no grouping judgement is involved.

# 3. What this selection is not

Stage 4.2F-A2 moved two of ten scoring columns and left eight where they were. Source completeness and source authority went from 0 to 4 for every unit, because the module and the boundaries are now in custody. Visual availability, interaction representativeness and quiz completeness are still ZERO for all fourteen — nobody has read a single page of content. What changed is that these are now questions we can answer by working, rather than questions blocked on someone else sending a file. The selection still cannot be called ready, and the ranking should be re-run the moment T04's content is extracted, because the first real look at a unit's structure will outweigh every proxy above it.

# 4. Rejected candidates

| unit_id | reason |
|---|---|
| `K5-PL06-T03-B03` | Same Topik as B02 and both boundaries are shared pages. Was Stage 4.2F-A's T03-BNEXT; now fully identified as Infrastruktur, module 250-255. |
| `K5-PL06-T05-B01` | Strong second choice — clean boundaries, high proof value — but 10 pages and four subtopics against T04's 8 pages and two. |
| `K5-PL06-T02-B02` | Shared start page adds heading-anchor extraction as a second new variable. |
| `K5-PL06-T07-B01` | Most likely of all to need new treatment, which makes it a poor first proof and a useful second. |
| `K5-PL06-T01-B01` | Not scored — Topik 1 groups 3 lessons out of 4 subtopics, so it leans hardest on the grouping authority that is REFERENCED_NOT_FROZEN. |
| `K5-PL06-T01-B02` | As T01-B01; shared on both boundaries. |
| `K5-PL06-T01-B03` | As T01-B01; shared start page. |
| `K5-PL06-T02-B01` | Shared end page; 15 module pages, the largest. |
| `K5-PL06-T03-B01` | Same Topik as B02; shared end page. |
| `K5-PL06-T03-B04` | Same Topik as B02; shared start page. |
| `K5-PL06-T03-B05` | Same Topik as B02; 14 module pages. |
| `K5-PL06-T06-B01` | Clean boundaries and 9 pages — a reasonable third proof, no differentiator over T04. |

# 5. Required preconditions

None of these is ours to satisfy alone.

- PRE-01 — CLOSED at Stage 4.2F-A2: the module source is in custody by identity
- PRE-02 — CLOSED at Stage 4.2F-A2: the Topik 4 boundary is stated by named heading anchor, module 276-283, DOCX paragraph 5220 to before 5360
- PRE-03 — extract and hash figures and table photographs from module 276-283 into an asset manifest (resolves STOP-003)
- PRE-04 — extract the controlled content model by heading anchor; determine the interaction pattern from this unit's own structure, not B02's (resolves STOP-004)
- PRE-05 — establish Rumusan and quiz source with an SME-signed answer key (resolves STOP-005)
- PRE-06 — settle the cast binding against the ratified character bank (resolves STOP-006)
- PRE-07 — written confirmation of Bariah's call approval, upgrading APPROVAL_RECORD from FIRDAUS_ATTESTED_BARIAH_CALL

# 6. Expected end-to-end path

1. extract module pages 276-283 from the external DOCX by heading anchor, paragraph 5220 to before 5360 — not by page slicing
2. extract and hash figures and table photographs into an asset manifest
3. derive the controlled content module from that extract — no content invented
4. derive the screen / state / interaction-item model and its counts from that content
5. re-derive the interaction pattern from the unit's own structure; do NOT import FAMILY_S / P1 / P2
6. generate the review deck through the shared shell, with the artifact-identity source carrying the new unit's version line
7. run the portable gate set, then add unit-specific content gates
8. build mutation fixtures for every unit-specific rule
9. render and inspect every page
10. Microsoft PowerPoint smoke — and record it this time
11. Bariah review

Step 5 is the one that matters for a scale-out proof. If the unit's structure is re-derived and it happens to land on something like Family S, that is a finding. If Family S is imported and then found to fit, that is not a finding — it is the architecture answering its own question.
