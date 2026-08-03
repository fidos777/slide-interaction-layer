# STAGE_4_2F_B0_9_QA_REPORT

```
STAGE             = 4.2F-B0.9 — T04 AUTHORITY DECISION INGESTION AND CONTENT FREEZE
SUITE_ID          = T04_AUTHORITY_DECISION_INGESTION_QA_v1
SUITE             = docs/pl06/t04/tools/t04_authority_qa_v1.py
FIXTURES          = docs/pl06/t04/tools/t04_authority_mutations_v1.py
ACTIVE_GATE_COUNT = 237
RESULT            = 237/237 active gates PASS · 237 emitted records
VACUOUS_GATES     = 0
FIXTURES          = 122/122 detected · 0 missed · 0 baseline false failures
SOURCE_ARTIFACTS  = 33 distinct artifacts named across the gates
SKIPPED_CHECKS    = none — no renderer is needed by this stage
```

**This suite is separate from every other suite in the chain and its 237 gates must never be
added to another suite's total.** It governs the ingestion of Bariah's decisions and the
frozen content model. `T04_BARIAH_REVIEW_ARTIFACT_QA_v1` governs the document she reviewed;
`T04_CONTENT_QA_v1` governs the content she reviewed. Different things, different populations,
different numbers. A combined figure would mean nothing.

# 1. Gate accounting

Every gate in this suite reports four things: the **population** it examined, the **expected**
value, the **observed** value, and the **source artifact** it read. A gate that cannot say
where its observed value came from is not evidence of anything.

| Gate type | Count | Holds |
|---|---:|---|
| `SEQUENCE_INTEGRITY` | 30 | 22 screens, one insertion, eight renumberings, four treatment changes |
| `ASSESSMENT_INTEGRITY` | 29 | stems verbatim, checkboxes on MR, no key final, distractors attributed |
| `DECISION_TYPING` | 24 | seven classes, every quote present, nothing flattened |
| `EVIDENCE_INTEGRITY` | 23 | hash and size match the file; nothing invented for what was not supplied |
| `VISUAL_SCOPE` | 20 | 46 ≠ 41, decision-basis lines, item-level restrictions, precedence |
| `CONTENT_FIDELITY` | 19 | dialogue and Rumusan verbatim, boundaries held, dependency archived |
| `RECONCILIATION` | 15 | no emitted artifact asserts a superseded fact as current |
| `CONFIRMATION_DISCIPLINE` | 14 | the WhatsApp record is degraded, ambiguous and non-actionable where it is |
| `FREEZE_HONESTY` | 14 | ten final states; frozen is not stated as approved |
| `PRODUCTION_GUARD` | 11 | no PPTX, no MMD, no generator change, no authority artifact modified |
| `GLOBAL_RULE_SCOPE` | 11 | two course-wide rules and no third inferred |
| `SOURCE_STATUS` | 11 | bindings present, round trip open, never `SOURCE_UNSUPPORTED` |
| `ACCOUNTING` | 9 | typed, unique, non-vacuous, and every snapshot agrees with its live derivation |
| `REPORTING` | 7 | suite identity, populations, source artifacts, `NOT_CHECKED` |
| **TOTAL** | **237** | |

`DECLARED_EMPTY_GATES`: none. No population in this suite is legitimately empty.

# 2. Two gate defects the first run exposed, and one blind spot a fixture found

## 2.1 The verbatim check failed on text that was verbatim — REAL GATE DEFECT

`EVERY_DIALOGUE_LINE_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX` reported two missing lines and
`EVERY_QUIZ_STEM_APPEARS_VERBATIM_IN_THE_AUTHORITY_DOCX` reported four missing stems. Neither
was actually missing.

The extractor joined Word's `<w:t>` runs with a space. Word splits a single word across runs
at formatting and proofing boundaries, so `tanggungjawab` can arrive as `tanggung` + `jawab`
in two runs — and joining with a space produced `tanggung jawab`, which does not match.
**Every one of those six "failures" was the gate mis-reading the document, not the model
mis-copying it.** Runs are now joined with no separator and the whitespace is normalised
afterwards. This is exactly the kind of gate that is worth having and worth distrusting: it
would have failed just as loudly on a real paraphrase.

## 2.2 `SUPERSEDED_STEMS_DID_CARRY_THE_ATTRIBUTION` expected the wrong number

Written expecting four of the five superseded stems to carry module attribution. All five did
— Q5's old stem ended *"…mengikut modul"*. Expectation corrected to 5. A wrong expectation in
a passing direction is the more dangerous version of this mistake; here it failed loudly.

## 2.3 The blind spot — fixture `C-05`

`C-05` relabels the delegated Q3 decision as `ACCEPTED_AS_PROPOSED`. **The suite did not
notice.**

`UNSETTLED_DECISIONS_ARE_ONLY_THE_DELEGATED_CLASS` inspects the unsettled population and
checks what is in it. Relabelling the decision removed it from that population — and a gate
that only looks *inside* a population cannot see something leave it. The unsettled set shrank
from two to one and every member still had the right class, so the gate passed while the very
claim it exists to protect ("Q3 is not settled") had been quietly reversed.

Fixed by asserting the named delegations directly rather than filtering for them:
`THE_TWO_NAMED_DELEGATIONS_REMAIN_UNSETTLED` and `THE_Q3_DELEGATION_KEEPS_ITS_DELEGATED_CLASS`.

**The generalisable form: a gate that filters a population by property P and then checks P
cannot detect a record leaving the filter.** This is a sibling of the stale-constant defect
that fixtures `W-22`, `V-03` and `X-34` found in the three preceding stages — the same shape
of blindness, now in the filter rather than in the cache.

## 2.4 Two fixtures had the wrong gate designated, not the wrong defect

`H-04` and `H-10` patch the published snapshot (`FINAL_VISUAL_SCOPE[...]`) while the
substantive gates read the live derivation, so those gates correctly saw nothing wrong with
the live data. The guard that *did* fire was the snapshot-agrees-with-live pair. The fixtures
now designate those gates. Coverage was complete in both directions — edit the live source and
the substantive gate fires; edit the snapshot and the agreement gate fires — but the fixture
was pointing at the wrong one, which would have made a future regression harder to read.

# 3. Live derivation, as a standing rule

Three consecutive stages lost a fixture to a value cached at import: a total (`W-22`), then a
count (`V-03`), then a whole projection (`X-34`). This suite recomputes every quantity inside
the gate, and additionally asserts that each snapshot the data module publishes for the
emitter equals its live recomputation:

```
DECISION_REGISTER_SNAPSHOT_AGREES_WITH_LIVE
SCREEN_SEQUENCE_SNAPSHOT_AGREES_WITH_LIVE
QUIZ_SNAPSHOT_AGREES_WITH_LIVE
DO_NOT_REUSE_SNAPSHOT_AGREES_WITH_LIVE
ASSET_GROUP_SNAPSHOT_AGREES_WITH_LIVE
FINAL_STATES_SNAPSHOT_AGREES_WITH_LIVE
```

Six fixtures exercise them. This is the first stage in the chain where the class of defect was
anticipated rather than discovered.

# 4. Mutation fixtures

**122 fixtures, 122 detected, 0 missed, 0 baseline false failures.** Every emitted artifact is
byte-identical after the whole fixture set — `post_run_restored = true`.

| Target | Fixtures | What it models |
|---|---:|---|
| `D` — the controlled data source | 115 | a wrong decision, a dropped quote, a fabricated hash |
| `QA` — the reporting harness | 4 | the suite losing its identity, its `NOT_CHECKED` list, its marker set |
| `DISK` — the emitted artifact | 3 | a claim that exists only in the Markdown file |

The three disk fixtures rewrite an emitted `.md` on disk and restore it byte-for-byte, because
a memory patch cannot model "a stale claim lives only in the published file" — the
reconciliation gates read the file.

| Group | Range | Covers |
|---|---|---|
| Evidence | `A-01`…`A-12` | fabricated hash, invented dimensions, drifted size, claimed tracked changes, dropped limitations |
| Confirmations | `B-01`…`B-08` | Q3 resolved without authority, Q3 as a Bariah rule, Q3 as an ID, evidence upgraded |
| Decision typing | `C-01`…`C-12` | flattened classes, CAIR work as hers, silent correction, unresolved supersession |
| Sequence | `D-01`…`D-15` | screen dropped, Tamat Bahagian restored, PPE reveal removed, unit ID collapsed |
| Content | `E-01`…`E-11` | fifth dialogue line, paraphrase, compliance duty, banned contrast, course-wide Rumusan |
| Quiz | `F-01`…`F-16` | module attribution, letter labels, fertiliser distractors, key marked final |
| Global rules | `G-01`…`G-06` | scope narrowed, quote removed, a third rule inferred |
| Visual | `H-01`…`H-10` | 46 as 41, basis line dropped, precedence removed, inserted screen given an asset |
| Source | `J-01`…`J-06` | open risks closed, bindings denied, `SOURCE_UNSUPPORTED` applied |
| Freeze | `K-01`…`K-10` | Q5 options approved, key final, E-01…E-04 closed, forbidden label applied |
| Production | `L-01`…`L-04` | PPTX, generator, MMD, authority artifact |
| Reporting | `M-01`…`M-09` | reconciliation gutted, suite identity lost, marker set emptied |
| On disk | `N-01`…`N-03` | stale claim in the emitted Markdown, disclosure deleted |

# 5. Rendering

```
DOCX_NATIVE_RENDER = NOT_APPLICABLE_THIS_STAGE
```

This stage produces no document for a human to read in Word. It reads one and emits JSON and
Markdown. The renderer limitation recorded in Stage 4.2F-B0.8A — LibreOffice installed without
`libreoffice-writer`, so no Writer import filter exists — is unchanged and unchallenged, but
nothing here depends on it.

The authority DOCX was parsed as OOXML, not rendered. The suite asserts its ZIP integrity, its
hash, its byte size, the absence of tracked-change elements and the absence of a comments
part. **It does not assert what the document looks like in Word, and no claim is made about
that.**

# 6. `NOT_CHECKED`

- whether Bariah's replacement dialogue reads naturally to a native Malay speaker
- whether the three-beat Rumusan is instructionally better than the four points it replaced —
  she ruled it, the gates carry it, they do not judge it
- whether the two CAIR-written Q5 distractors are good distractors, or whether Bariah will
  accept them
- whether the proposed answer keys are correct — no key is final and none is asserted
- whether "Q3" in the WhatsApp line means quiz Q3 — the referent is unresolved and the suite
  records it as unresolved rather than picking one
- whether the `pembajaan` → `racun` correction matches Bariah's intent — the correction is
  recorded, not validated
- whether the inserted screen sits at the right point in the sequence for learning
- whether 22 screens is the right length
- whether the original module DOCX still matches the controlled extract — that round trip was
  not run in this session and is recorded as `OPEN`
- any rendered output — no PPTX exists for T04 and none was generated

**A green suite measures the suite, not the artifact.** Three of the four sections above
describe cases where a gate was wrong, an expectation was wrong, or a defect walked past a
green run. That is the honest reading of 237/237.

# 7. Chain status, each with its own suite identity

| `SUITE_ID` | Governs | Gates | Fixtures |
|---|---|---|---|
| `T04_AUTHORITY_DECISION_INGESTION_QA_v1` | the ingested decisions and the frozen model | **237 / 237** | **122 / 122 detected** |
| `T04_BARIAH_REVIEW_ARTIFACT_QA_v1` | the review artifact | 133 / 133 | 45 / 45 detected |
| `T04_CONTENT_QA_v1` | T04 content and instance mapping | 138 / 138 | 53 / 53 detected |
| `T04_FINAL_RULINGS_QA_v1` | final structural rulings | 105 / 105 | 32 / 32 detected |
| `T04_RULINGS_QA_v1` | partial rulings | 130 / 130 | 26 / 26 detected |
| `T04_PACK_QA_v1` | pre-storyboard decision pack | 107 / 107 | 39 / 39 detected |
| `T04_EXTRACTION_QA_v1` | controlled source extraction | 109 / 109 | 30 ran, 30 detected · **4 `SKIPPED_NO_DOCX`, not counted as passing** |
| `PL06_INVENTORY_QA_v1` | PL06 inventory | 140 / 140 | 54 / 54 detected |
