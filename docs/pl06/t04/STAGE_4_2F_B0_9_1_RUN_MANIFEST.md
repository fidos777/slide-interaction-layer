# STAGE_4_2F_B0_9_1_RUN_MANIFEST

```
STAGE            = 4.2F-B0.9.1 — SUPPLEMENTARY EVIDENCE CUSTODY CLOSURE AND REGISTER AUDIT
SUITE_ID         = T04_SUPPLEMENTARY_EVIDENCE_QA_v1
PART_A_RESULT    = BLOCKED
BLOCKER          = B091-BLOCK-01 — no screenshot binary exists in this environment
PART_B_STARTED   = 0
RELEASE_RECORD   = NOT_ISSUED
PPTX_GENERATED   = 0 · MMD = 0 · REACT/SCORM = 0 · LMS = 0
AUTHORITY_ARTIFACTS_MODIFIED = 0
```

**Part A did not pass, so Stage 4.2F-B1 was not started.** Everything in Part A that does not
depend on the missing binary was completed, and one of those findings is a correction to a
committed Stage 4.2F-B0.9 record.

# 1. Pre-flight

| Check | Result |
|---|---|
| Branch | `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at start | `a7d6ce2d12226018129bc34d734b7848b157893b` — matches `a7d6ce2` |
| Working tree at start | clean, 0 porcelain lines |
| `T04_AUTHORITY_DECISION_INGESTION_QA_v1` at start | 237 / 237, 0 vacuous |
| B0.9 artifacts | all 24 present and unmodified |
| Authority DOCX | 36,105 bytes, `2eea2101…` — unchanged |
| **Runtime path of the new PNG** | **none — the file does not exist** |
| Prior copy of the same screenshot in the repository | none |

# 2. The blocker

```
B091-BLOCK-01   supplementary screenshot custody
required        a PNG binary to hash, measure, validate and freeze
observed        no image file exists anywhere in this environment
owner           FIRDAUS
```

The screenshot reached this run as a **rendered image in the conversation**, not as a file
upload. Four locations were searched:

| Location | Result |
|---|---|
| `/mnt/data` | does not exist — reconfirmed, as in Stage 4.2F-B0.9 |
| `/root/.claude/uploads/12837c42-…/` | 21 files, newest is the 02:28 authority DOCX. No PNG, JPG or WEBP was added. |
| whole filesystem, one device, modified after 2026-08-03 02:29 | no matching image |
| session tool-results cache | two text files, no image |

So every field that can only be measured from a binary is unavailable:

| Field | Value |
|---|---|
| original runtime path | `NOT_AVAILABLE_NO_BINARY` |
| repository custody path | `NOT_CREATED` |
| byte size · SHA-256 · MIME type | `NOT_AVAILABLE_NO_BINARY` |
| pixel width · pixel height | `NOT_AVAILABLE_NO_BINARY` |
| file-format validation | `NOT_PERFORMED_NO_BINARY` |
| intake time | `NOT_APPLICABLE_NO_INTAKE` |
| byte-identity vs source | `NOT_VERIFIABLE_NO_BINARY` |

The intended path `reviews/storyboard-bariah/t04_bariah_review/T04_BARIAH_WHATSAPP_CONFIRMATION_2026-08-03.png`
was **not created**. Writing a placeholder there would put a file in the evidence directory
that is not the evidence. Fixture `A-02b` creates exactly such a placeholder and the suite
fires.

**Consequence.** The evidence class cannot be upgraded to `AUTHORITY_DIRECT_SCREENSHOT`, the
`NOT_SUPPLIED` state on `AUTH-EV-02` cannot be cleared, and no superseding release record is
issued. **What would unblock it:** re-send the screenshot as a file attachment. Everything
else in this stage is already done and will not need repeating.

## 2.1 Three kinds of timestamp, kept apart

Only one of the three exists, and it is the weakest of the three as file evidence.

| Class | Available | Values |
|---|---|---|
| `VISIBLE_IN_SCREENSHOT` | yes | 7:17, 7:18, 7:20, 7:20, 7:21 AM · date separator reads only *Today* |
| `RUNTIME_FILESYSTEM` | **no** | there is no file, so no mtime, ctime or atime |
| `IMAGE_METADATA_EXIF` | **no** | none read, none asserted |

The calendar date 3 August 2026 comes from the stage brief, **not from the pixels**.

# 3. Visual reading — and a misattribution it exposed

The exchange was read by looking at the rendered image. OCR was not used and no prior
transcript was treated as sufficient on its own. Speaker attribution is from WhatsApp bubble
geometry: outgoing messages green, right-aligned, sent/read ticks; incoming white and
left-aligned under the *Bariah eLearning* header.

| # | Time | Sender | Content |
|---|---|---|---|
| WA-01 | 7:17 | **Firdaus** | decision summary + three numbered confirmation requests |
| WA-02 | 7:18 | **Bariah** | *Yes to both* |
| WA-03 | 7:20 | **Firdaus** | *Q3 tu nnt u pilih ya* |
| WA-04 | 7:20 | **Firdaus** | *Ni for first 2 Q kan* (quoting her *Yes to both*) |
| WA-05 | 7:21 | **Bariah** | *Yes to both screenshots. Q5 multiple response - yes, ok* |

## 3.1 `T04-COR-02` — a material misattribution of authorship

**Stage 4.2F-B0.9 recorded *"Q3 tu nnt u pilih ya"* as a Bariah message and as a delegation
from the authority to CAIR.** It is Firdaus's message — green, right-aligned, sent/read ticks.
That stage had no image and read the line from an unattributed transcription in its brief.

The consequence is not cosmetic. **There is no Bariah delegation to CAIR anywhere in this
exchange.** `T04-DEC-X01` is Firdaus deferring his own third question, which Bariah then
answered three minutes later. Corrected in the live model:

- `T04-CNF-03` → `author = FIRDAUS`, `is_authority_statement = False`,
  status `NOT_AN_AUTHORITY_STATEMENT_MISATTRIBUTED_IN_B0_9`
- `T04-DEC-X01` → `authority = FIRDAUS_NOT_AN_AUTHORITY_ACT`

Two B0.9 gates that encoded the superseded belief were re-pointed, and gate
`AUTHORITY_IS_ALWAYS_BARIAH` was split into `EVERY_AUTHORITY_ACT_IS_BARIAHS` plus
`EXACTLY_ONE_NON_AUTHORITY_RECORD_AND_IT_IS_NAMED` — a bare filter would have let a second
non-authority record slip in unseen, which is the same defect class as C-05.

The B0.9 run manifest and QA report are **not** rewritten. They record what was true when they
were written, and the correction is traceable from both ends.

## 3.2 `T04-COR-03` — the referent of "Q3"

Supported reading: the **third of Firdaus's three numbered requests** — the Q5 proposal. His
message enumerates exactly three items, and WA-04 speaks of *"first 2 Q"* against that same
enumeration. The quiz-item reading is retained as the weaker alternative and is **not**
selected. The ambiguity is now moot rather than resolved by assertion: Bariah answered the
third request explicitly in WA-05.

# 4. What the exchange confirms, at what precision

None of these carries `AUTHORITY_DIRECT_SCREENSHOT`, because no screenshot artifact was
verified. All three carry `CONTENT_CONFIRMED_CUSTODY_UNVERIFIED` and name
`CUSTODY_FAILED_NO_BINARY` as what blocks the upgrade.

| ID | Subject | Mode | Status if custody had passed |
|---|---|---|---|
| `T04-CNF-01` | pembajaan → racun on T04-S14 | `BUNDLED_ACCEPTANCE_OF_TWO_PROPOSITIONS` | `CONFIRMED_THROUGH_BUNDLED_SCREENSHOT_ACCEPTANCE` |
| `T04-CNF-02` | S14 reuses three AG-06 assets; scope stays 41 | `CAIR_PROPOSAL_CONFIRMED_BY_AUTHORITY` | `CONFIRMED_BARIAH_ON_CAIR_PROPOSAL` |
| `T04-CNF-03` | Q5 item type = `MULTIPLE_RESPONSE` | `EXPLICITLY_WORDED_INDIVIDUAL_DECISION` | `EXPLICITLY_CONFIRMED` |

Held precisely:

- **CNF-01** — Bariah did not write the corrected sentence. She answered a yes/no question
  Firdaus phrased. It is not recorded as a Bariah-originated sentence.
- **CNF-02** — 41 is not an idea Bariah originated and AG-06 reuse is not a Bariah-authored
  design. Both are CAIR production proposals she assented to. **41 is not immutable**: if MMD
  later demonstrates a genuine new asset requirement, 41 → 42 must be a new scope-change
  decision, never absorbed silently.
- **CNF-03** — confirms the item type only. It does **not** confirm the five answer keys, the
  exact two replacement distractors, every source-row binding, or a general delegation to
  approve assessment content. Answer keys stay `PROPOSED_NOT_FINAL`; the two CAIR-written
  distractors stay `CAIR_DRAFTED_UNDER_AUTHORITY_INSTRUCTION` / `PENDING_BARIAH_CONFIRMATION`.

## 4.1 The confirmation ID collision, declared not resolved

The stage brief re-scopes `T04-CNF-01/02/03` onto three different subjects from the ones
already committed under those IDs. That re-scoping is the intended end state but it is
conditional on the custody upgrade, which failed. **Nothing was renumbered.** The mapping is
published instead, including the fourth row: the old `T04-CNF-03` has no successor, because
once authorship is corrected the line has no place in a confirmation register at all.

# 5. `T04-DIV-01` — the Q5 the authority saw is not the Q5 in the frozen model

This is the finding the screenshot makes visible and it is **not resolved here.**

Firdaus put a six-option Q5 to Bariah. Options 1–4 are identical to the frozen model.
**Options 5 and 6 are not.**

| # | Put to the authority | Frozen in the model | Same? |
|---|---|---|---|
| 5 | Notifikasi kepada penduduk dibuat hanya selepas semburan selesai | Semburan dijadualkan pada waktu petang selepas waktu kerja tapak tamat | **NO** |
| 6 | SDS hanya perlu disimpan di pejabat projek dan tidak perlu berada di tapak | Semua racun dibeli daripada satu pembekal tunggal yang dilantik projek | **NO** |

The stems differ too: Firdaus wrote *"Pilih SEMUA pernyataan yang tepat tentang kawalan semasa
aktiviti semburan racun"*; the frozen model carries **Bariah's own written replacement stem**
from the authority DOCX, *"Pilih SEMUA kawalan yang mesti dipatuhi oleh kontraktor semasa
aktiviti semburan racun."*

So Bariah's *"Q5 multiple response - yes, ok"* was written against Firdaus's option set, not
against the frozen one. Resolving that would mean either overwriting her frozen stem with his
wording, or asserting her *"yes, ok"* reaches option text she was never shown. **Both are
decisions for the authority, not for CAIR, and neither was taken.** The frozen model is
unchanged; fixture `E-03` fires if the WhatsApp options are silently adopted.

Tracked as **E-07**. Does not block storyboard layout. **Does block a scored quiz.**

# 6. AG-01 … AG-08 register audit

Two things are true at once and the register has to hold both: **every one of the eight
per-group decision cards in the authority DOCX is blank**, and the Section B narrative
nevertheless accepts conditional sharing across AG-01 to AG-08 as a set.

| Layer | What | Value |
|---|---|---|
| 1 | set-level acceptance | `ACCEPTED_AS_A_SET_WITH_CONDITIONS`, basis `BARIAH_DIRECT_SET_LEVEL_NARRATIVE` |
| 2 | individual card markings | `NOT_INDIVIDUALLY_MARKED` |
| 3 | item-level no-reuse restrictions | three items closed |
| 4 | S14-specific AG-06 reuse | `CONFIRMED_ON_CAIR_PROPOSAL` |

The groups are **not** represented as eight individual acceptances, **not** as eight
unanswered decisions, and **not** as eight pending-human blockers. Each of those three loses
different information: the first invents ticks that are not on the page, the second discards a
set-level acceptance she did write, the third would stall a build over a question she has
already answered. Fixtures `F-01`, `F-02` and `F-03` fire on each.

The three no-reuse decisions remain closed — Baja Pengurusan Stok dan Penyimpanan, Baja
Keselamatan Pekerja, Racun Keselamatan dan Kesihatan (HSE) — with decision basis
`BOTH_INSTRUCTIONAL_AND_PRODUCTION` at evidence precision
`DERIVED_FROM_BARIAH_SECTION_LEVEL_NARRATIVE`. **Bariah did not tick a basis field on each
item.** She stated both grounds once, at section level, covering all three, and the record
says derived rather than ticked.

# 7. Filtered-population predicate audit

Fixture `C-05` got past the B0.9 suite because a gate selected its population by a mutable
property and then checked that property — so when the mutation made a record *leave* the
population, the gate saw a smaller, still-correct population and passed. **A filter cannot
observe its own departures.**

The rule is now applied across the whole suite, not just the C-05 site: **18 closed
populations**, each carrying the property check, a named-membership assertion and a
population-count delta. All 18 pass with 0 unexpected additions and 0 unexpected removals.

| ID | Selector | n | Origin fixture |
|---|---|---:|---|
| POP-01 | `decision_class == DELEGATED_PENDING_AUTHORITY_CONFIRMATION` | 2 | C-05 |
| POP-02 | `settled is False` | 2 | C-05 |
| POP-03 | `scope == ALL_PLS_IN_KURSUS` | 2 | G-03 / G-04 |
| POP-04 | `change_type contains TREATMENT_CHANGED` | 4 | D-08 |
| POP-05 | `change_type == INSERTED` | 1 | D-01 |
| POP-06 | `change_type == RENUMBERED` | 2 | D-09 |
| POP-07 | `question_type == MULTIPLE_RESPONSE` | 1 | F-03 |
| POP-08 | `question_type == MCQ` | 4 | F-03 |
| POP-09 | `treatment == CONTENT_STATIC` | 9 | D-10 |
| POP-10 | `named_reveal_items` non-empty | 2 | D-07 |
| POP-11 | `named_aspect_list` non-empty | 3 | D-15 |
| POP-12 | `class == …EXECUTED_BY_CAIR` | 9 | C-02 |
| POP-13 | `class == …AUTHORITY_SUPPLIED_REPLACEMENT_TEXT` | 7 | C-01 |
| POP-14 | `source_artifact == AUTH-EV-02` | 1 | C-04 |
| POP-15 | `settled is False` among final states | 2 | K-01 / K-02 |
| POP-16 | `supplied_in_this_run is False` | 1 | A-02 |
| POP-17 | `restriction == REUSE_NOT_ALLOWED` | 3 | H-03 / H-05 |
| POP-18 | open items carried past the stage | 6 | K-04 |

**Five exclusions, documented.** Naming members is only meaningful for a population whose
membership is itself a governed fact. `EXC-01` every substantive string · `EXC-02` every file
in the directory · `EXC-03` every gate in the suite · `EXC-04` every controlled source row ·
`EXC-05` every emitted artifact. Each names the delta guard that covers it instead — for
example `SOURCE_BINDINGS_NOT_REMOVED_FROM_THE_MODEL` is a genuine delta assertion over the
row set.

# 8. Exact-element XML matching

Substring matching on OOXML is wrong in a way that reads as right, and this project has been
bitten twice. A shared helper `t04_ooxml_v1.py` now matches namespace plus local name exactly,
using the standard library's own namespace-aware parser. It is a helper, not a framework —
four functions, no new architecture.

| Case | Kind | Proves | Exact | Naive substring |
|---|---|---|---:|---:|
| XML-01 | confusion | `<w:insideH>` is not `<w:ins>` | 0 | 1 |
| XML-02 | confusion | `<w:insideV>` is not `<w:ins>` | 0 | 1 |
| XML-03 | confusion | `<w:tcPr>` is not `<w:t>` | 0 | 4 |
| XML-04 | **positive control** | a real `<w:ins>` is still found | 1 | 1 |
| XML-05 | confusion | a real `<w:t>` survives alongside `<w:tcPr>` | 1 | 5 |
| XML-06 | confusion | `<w:delText>` is not `<w:del>` | 0 | 1 |

XML-04 exists so the helper cannot pass by returning zero for everything. Fixture `H-03`
deletes it and the suite fires.

Re-checked against the live authority DOCX by exact match: **tracked insertions = 0, tracked
deletions = 0**, while the naive `<w:ins` substring count is still 12 on that same file. The
trap is real and is now closed.

# 9. QA and mutations

| Suite | Gates | Fixtures |
|---|---|---|
| `T04_SUPPLEMENTARY_EVIDENCE_QA_v1` (new) | **111 / 111**, 0 vacuous | **71 / 71 detected** |
| `T04_AUTHORITY_DECISION_INGESTION_QA_v1` (B0.9, after the correction) | **239 / 239**, 0 vacuous | **122 / 122 detected** |

Never add those totals — they govern different things.

`A-01` … `A-03` were re-scoped to the reality of a missing binary and expanded to twelve
fixtures, because "no PNG, so nothing can be invented" has more than three ways to go wrong:

| Fixture | Injected defect |
|---|---|
| `A-01` | a SHA-256 is invented |
| `A-01b` | a byte size is invented |
| `A-01c` | pixel dimensions are invented |
| `A-01d` | format validation is claimed |
| `A-01e` | a MIME type is asserted from the conversation label |
| `A-02` | the custody outcome is flipped to success |
| `A-02b` | **a placeholder file is created at the custody path** (real file, on disk) |
| `A-02c` | byte-identity against the source is claimed |
| `A-03` | the B0.9 evidence record is flipped to supplied |
| `A-03b` | the B0.9 evidence record is given a hash |
| `A-03c` | a reading claims `AUTHORITY_DIRECT_SCREENSHOT` |
| `A-03d` / `A-03e` | a filesystem timestamp / EXIF is asserted |

All twelve fire. `custody_path_clean` confirms the placeholder was removed.

Gates also prove: the screenshot supplements and does not replace the authority DOCX; CNF-01
is bundled acceptance not individual wording; CNF-02 is a confirmed CAIR proposal; CNF-03
confirms only the item type; answer keys and Q5 distractors are not relabelled Bariah-direct;
AG-01…AG-08 use set-level semantics; blank individual cards stay recorded; S14 adds zero
unique assets; scope remains 41; `NOT_SUPPLIED` cannot survive a successful custody nor be
cleared without one; and no prior B0.9 decision is silently altered.

# 10. What was NOT done

- **No release record was issued.** The would-be verdict is held as a template with
  `issued = False`, so the difference between *ready to state* and *stated* stays visible. The
  Stage 4.2F-B0.9 release record stands unchanged.
- **Part B was not started.** No storyboard model, no review PPTX, no rendering.
- No MMD production, no React, no SCORM, no LMS work.
- Neither authority artifact was modified. The v3 DOCX is byte-identical.
- No historical run record was rewritten. `STAGE_4_2F_B0_9_RUN_MANIFEST.md` and
  `STAGE_4_2F_B0_9_QA_REPORT.md` are untouched.
- No Bariah decision that was closed has been reopened.
- No new governance framework — the OOXML helper is four functions and the audits are two
  modules, all inside the existing `docs/pl06/t04/tools/` convention.
- Commit `a7d6ce2` was not amended.

# 11. Open items after this stage

| ID | Subject | Owner |
|---|---|---|
| E-01 | Q5 replacement options E and F | Bariah |
| E-02 | Quiz answer keys, all five | Bariah |
| E-03 | The "Q3" referent | **closed by T04-COR-03 as moot** — it was Firdaus's line |
| E-04 | The pembajaan → racun correction | Bariah |
| E-05 | Original module DOCX round trip | Firdaus |
| E-06 | Individual asset subjects and styles | Bariah |
| **E-07** | **Which Q5 six-option set stands** | Bariah |
| **E-08** | **Supplementary screenshot binary custody** | Firdaus |
