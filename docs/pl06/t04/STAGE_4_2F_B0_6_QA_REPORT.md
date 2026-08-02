# STAGE_4_2F_B0_6_QA_REPORT

```
STAGE   = 4.2F-B0.6 — INCORPORATE BARIAH PARTIAL RULINGS
SUITE   = docs/pl06/t04/tools/t04_rulings_qa_v1.py
FIXTURES= docs/pl06/t04/tools/t04_rulings_mutations_v1.py
RESULT  = 130/130 active gates PASS · 0 supersession markers · 130 emitted records
FIXTURES= 26/26 detected · 0 missed · 0 baseline false failures
```

**A green suite measures the suite, not the artifact.** 130/130 means the gates I wrote agree
with the data I wrote. It does not mean the visual subjects are right, that the Rumusan reads
well in Malay, or that the quiz blueprint tests the right things. Those are Bariah's calls and
no gate can stand in for them.

# 1. Gate accounting

| Gate type | Count | Holds |
|---|---:|---|
| `EVIDENCE_INTEGRITY` | 11 | both images byte-identical to their recorded hashes; class, reviewer, scope, no modification |
| `DECISION_INTEGRITY` | 20 | the seven decision statuses exactly as instructed; supersession recorded; nothing approved |
| `POPULATION_COMPLETENESS` | 18 | 46 obligations derived from the source; every descendant present; no vague phrase |
| `AUTHORITY_DISCIPLINE` | 6 | requirement authority vs subject authority never merged |
| `INVENTION_GUARD` | 10 | no image claimed that the source does not hold; six nodes unchanged; no seventh step |
| `ASSESSMENT_INTEGRITY` | 15 | 4 MCQ + 1 MR, scope `ALL_PLS_IN_KURSUS`, threshold unresolved, no stem/option/key |
| `AUTHORSHIP_GUARD` | 9 | Rumusan stays a CAIR draft; the medium-risk flag survives; v1 statements accounted for |
| `SAFETY_DISCLOSURE` | 9 | 19 legal rows in 9 groups; no obligation proposed for reveal-only; split not applied |
| `MAPPING_INTEGRITY` | 9 | screen count not claimed; unmapped obligations declared; accounting adds up |
| `PROPAGATION_GUARD` | 5 | zero B02 families; no B02 fact in the Rumusan |
| `ARTIFACT_AGREEMENT` | 16 | Markdown / CSV / JSON agree; no PPTX; no production generator touched |
| `ACCOUNTING` | 2 | no duplicate gate IDs; every record carries a type |
| **TOTAL** | **130** | |

`SUPERSESSION_MARKER` records: **0**. Nothing in this stage supersedes a prior gate.

# 2. Five gates failed on first run. All five were my own false positives.

Every one was fixed at the gate. No artifact was weakened to make a gate pass.

## 2.1 `HILMI_NOT_INTRODUCED_AS_APPROVED`

Fired on D-03's own supersession note: *"Hilmi must NOT be carried forward as approved
treatment."* The gate scanned prose for "Hilmi" near "approved" and matched the sentence whose
entire purpose is to say the opposite. This is the same shape as the Stage 4.2F-B0
`EXTRACT_FREE_OF_B02_CONTENT` bug — a keyword co-occurrence test cannot read a negation.

Replaced with three structural gates that do not read prose at all:
`HILMI_CONFINED_TO_THE_UNRESOLVED_D03_RECORD` (Hilmi may appear only inside the D-03 record
and its follow-up), `D03_CARRIES_NO_RULING`, and
`HILMI_NOT_ASSIGNED_IN_ANY_CONTRACT_OR_OBLIGATION`.

## 2.2 `NO_VAGUE_SUBTOPIC_PHRASE_IN_CONTROLLED_RECORDS`

Fired on `"Their sub – perlu visual"` — **Bariah's own words**, quoted verbatim in the evidence
register. The gate was punishing faithful transcription of the ruling it exists to enforce.

A verbatim ruling is evidence, not a controlled record. The scan was narrowed to the inventory,
mapping, contracts and legal rows — where a vague phrase would be a real defect — and a
companion gate `BARIAH_VAGUE_PHRASE_PRESERVED_VERBATIM_IN_EVIDENCE` now requires BR-L4 to
still read exactly as she wrote it. The rule has two halves: enumerate in the records, preserve
in the evidence.

## 2.3 `SIXTY_PERCENT_NOT_CONFIRMED`

Fired on D-02B's own text: *"Composition is confirmed; the threshold was not mentioned. The 60
percent figure exists only in the B02 slice…"* — "confirmed" refers to composition, "60
percent" to the threshold, and the gate matched their co-occurrence in one string.

This is the third time this exact bug has appeared in this workstream (the
`PASS_THRESHOLD_TREATED_AS_CONFIRMED` false positive at Stage 4.2F-B0.5 was the second).
Replaced with a bounded-window regex that requires the confirmation word within 40 characters
of the threshold mention, in either order, and never across a sentence boundary.

## 2.4 `NO_FINAL_QUIZ_STEM`

Matched `"answer key"` inside the blueprint's own `not_produced` list — the declaration of what
was deliberately **not** written. Disclosure was being read as the defect it discloses.

`not_produced` is now excluded from every prose scan, and `QUIZ_NOT_PRODUCED_LIST_INTACT`
asserts the list still names all six withheld items, so the exclusion cannot become a hole.
`"answer key"` also moved to `ANSWER_KEY_MARKERS`, where it belonged.

## 2.5 `NO_FINAL_ANSWER_OPTION`

The `^[a-dA-D][).]` pattern matched D-01's three requirement groups (*"A. a visual for every
step…"*), D-03's three cast options and D-05's three confirmations. Those are **decision**
options, not quiz answers.

The scan is now scoped to the quiz records only. A/B/C lettering is used throughout this pack
for human decisions and a repository-wide scan will always call those quiz options.

# 3. A defect the gates caught that was mine, not a false positive

Five of the nineteen visual-obligation IDs cited in the D-04 legal clarification sheet were
**wrong**. I typed them before the inventory was generated, and obligation IDs are assigned
during construction — they cannot be predicted. `T04-ROW-043` pointed at *Aspek Pengurusan
untuk Kontraktor* instead of *Keselamatan Pekerja*; four others were off by the same kind of
slip.

Fixed by deriving the reference from the row→obligation index rather than typing it, and held
permanently by `LEGAL_VISUAL_REFERENCES_RESOLVE`, which checks that every cited obligation
actually covers the row citing it.

This is worth stating plainly: the first version of that sheet would have sent Bariah to the
wrong visual five times out of nineteen, and it looked completely plausible.

# 4. Mutation fixtures

26 fixtures, **26 detected, 0 missed, 0 baseline false failures**. All sixteen mutations named
in the stage brief are covered; ten more were added.

| Fixture | Defect injected | Named in brief |
|---|---|---|
| `Z-01` | one of the six process-node obligations removed | ✓ |
| `Z-02` | a Siram descendant removed | ✓ |
| `Z-03` | a Baja descendant removed | ✓ |
| `Z-04` | a Racun descendant removed | ✓ |
| `Z-05` | one of the four named Kejur groups removed | ✓ |
| `Z-06` | an enumerated descendant replaced by "their subtopics" | |
| `Z-07` | a visual subject promoted to `BARIAH_DIRECT_SCREENSHOT` | ✓ |
| `Z-08` | a non-existent source photograph claimed to exist | ✓ |
| `Z-09` | a required asset no longer labelled `NEW_MMD_ASSET_REQUIRED` | |
| `Z-10` | 60 percent marked confirmed | ✓ |
| `Z-11` | quiz composition changed to five MCQ | ✓ |
| `Z-12` | quiz scope reduced to T04 only | ✓ |
| `Z-13` | a final question stem written into a slot | ✓ |
| `Z-14` | a final answer key written into a slot | ✓ |
| `Z-15` | Rumusan marked `BARIAH_APPROVED` | ✓ |
| `Z-16` | legal base/reveal split marked confirmed | ✓ |
| `Z-17` | cast decision marked approved | ✓ |
| `Z-18` | SmartArt MMD treatment marked approved | ✓ |
| `Z-19` | `TEXT_AND_DIAGRAM_LED` presented as the final ruling | |
| `Z-20` | a final screen count claimed | ✓ |
| `Z-21` | a B02 execution family propagated onto a T04 screen | ✓ |
| `Z-22` | B02 factual content copied into the Rumusan | |
| `Z-23` | an evidence SHA-256 no longer matches the frozen bytes | |
| `Z-24` | an evidence item downgraded from `BARIAH_DIRECT_SCREENSHOT` | |
| `Z-25` | a coverage point silently discarded from the blueprint | |
| `Z-26` | a mandatory legal row moved behind an optional reveal | |

# 5. Chain status

| Suite | Result |
|---|---|
| Stage 4.2F-B0.6 rulings gates | **130 / 130** |
| Stage 4.2F-B0.6 fixtures | **26 / 26 detected** |
| Stage 4.2F-B0.5 decision-pack gates | 107 / 107 |
| Stage 4.2F-B0.5 fixtures | 39 / 39 detected |
| Stage 4.2F-B0 extraction gates | 109 / 109 |
| Stage 4.2F-B0 fixtures | 30 ran, 30 detected · **4 `SKIPPED_NO_DOCX`, not counted as passing** |
| Stage 4.2F-A2 PL06 inventory gates | 140 / 140 |
| Stage 4.2F-A2 fixtures | 54 / 54 detected |

The four skipped fixtures — `E-01` to `E-04` — require the primary DOCX, which was deleted at
the end of Stage 4.2F-B0 by that stage's own cleanup rule. They are reported as skipped, not
as passed.

# 6. What no gate here checks

- Whether any proposed visual subject is the right subject. Every one is `PENDING_BARIAH_REVIEW`.
- Whether the Malay in the Rumusan draft or the WhatsApp message is idiomatic.
- Whether 46 visuals is a proportionate production ask for one lesson.
- Whether the QB-03 + QB-04 consolidation loses something Bariah cares about.
- Whether the eight Landskap Kejur sub-items should have been in scope.
