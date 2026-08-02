# STAGE_4_2F_B0_8A_QA_REPORT

```
STAGE             = 4.2F-B0.8A — GOVERNED BARIAH REVIEW ARTIFACT
SUITE_ID          = T04_BARIAH_REVIEW_ARTIFACT_QA_v1
SUITE             = docs/pl06/t04/tools/t04_review_artifact_qa_v1.py
FIXTURES          = docs/pl06/t04/tools/t04_review_artifact_mutations_v1.py
ACTIVE_GATE_COUNT = 133
RESULT            = 133/133 active gates PASS · 133 emitted records
VACUOUS_GATES     = 0
FIXTURES          = 45/45 detected · 0 missed · 0 baseline false failures
SKIPPED_CHECKS    = native DOCX render — see §5
```

**This suite is separate from `T04_CONTENT_QA_v1` and its 133 gates must never be added to
that suite's 138.** They govern different things: `T04_CONTENT_QA_v1` governs the content,
this one governs the artifact that carries it. A combined number would mean nothing.

# 1. Gate accounting

| Gate type | Count | Holds |
|---|---:|---|
| `ARTIFACT_AUTHORITY` | 8 | the hierarchy is declared; the manual DOCX is a reference, never data |
| `SEMANTIC_PARITY` | 20 | model / Markdown / DOCX agree, in both directions |
| `MERGE_DISCIPLINE` | 12 | MERGE only where it applies, always with a resolving target, never confused with reuse |
| `VISUAL_REPORTING` | 24 | 46 ≠ 41, every disclosure present, provenance separated |
| `CONTENT_BOUNDARY` | 22 | dialogue boundary, Rumusan risk, dependency, quiz status |
| `LANGUAGE_PRESENTATION` | 14 | Malay throughout, no technical leak, one verdict block, signature field |
| `DOCX_STRUCTURE` | 14 | valid OOXML, relationships resolve, tables fit, no media, no external links |
| `RENDER_HONESTY` | 6 | the renderer is unavailable and the document says so |
| `PRODUCTION_GUARD` | 5 | no PPTX, no MMD, no generator change, manual v1 untracked |
| `REPORTING` | 6 | suite ID, populations, `NOT_CHECKED`, live totals |
| `ACCOUNTING` | 2 | no duplicate IDs, every record typed |
| **TOTAL** | **133** | |

`DECLARED_EMPTY_GATES`: `NO_BROKEN_MEDIA_LINKS` — the governed document embeds no media at
all, which is stated rather than left as a silent zero.

# 2. Five gates failed on first run. Two were real artifact defects.

## 2.1 Reviewable items with no visible ID — REAL DEFECT

`ITEM_IDS_AGREE` found 33 IDs where the model has 42, and
`EVERY_REVIEWABLE_ITEM_HAS_DECISION_FIELDS_IN_DOCX` named the missing ones: every dialogue
line (`T04-DLG-01`…`05`) and every Rumusan point (`T04-RUM2-01`…`04`).

The document showed the speaker and the text but not the item ID. Bariah could tick a box but
could not write *"lihat T04-DLG-03"* in a comment, and nobody could match her comment back to
a record. For a document whose entire purpose is to capture decisions against identified
items, that is a functional defect, not a cosmetic one.

Fixed in the renderer, so Markdown and DOCX gained the IDs together. The expected count is now
derived live from `M.reviewable_item_ids()` rather than typed as a literal.

## 2.2 Obligation IDs leaking into the reviewer's document — REAL DEFECT

`NO_TECHNICAL_LEAK_IN_DOCX` found `T04-VO-` strings in the composite-covered list, the
no-separate-asset list and the per-group reuse restrictions. The brief permits *"the affected
IDs **or** clear item labels"*; internal obligation IDs are noise to a reviewer who has never
seen the obligation register.

Fixed in the model: those disclosures now read *"Kaedah Pelaksanaan (Siram)"* rather than
*"T04-VO-009 — Kaedah Pelaksanaan"*. The IDs remain in the model for traceability. Note the
distinction held elsewhere — screen, asset-group, dialogue, Rumusan, quiz and approval IDs
**are** shown, because Bariah needs them to name a MERGE target or reference an item.

## 2.3–2.5 Three extractor and expectation errors — MINE, not the artifact's

- `QUIZ_OPTIONS_MATCH_THE_MODEL` matched the six **section headings** (`A. Cadangan susunan
  skrin`, `B. …`) as quiz options, because both are formatted `X. text`. Fixed by excluding
  the known section titles from the option extractor.
- The same gate then failed on whitespace: the document renders `   [cadangan jawapan]` with
  three spaces and the extractor collapses them to one. Whitespace is a *permitted formatting
  difference*, so the expected value is now normalised through the same collapse.
- `ITEM_IDS_AGREE` carried a hardcoded `38`. Replaced with a live derivation.

# 3. A fixture caught what the suite could not — for the third stage running

`X-34` edits the model so the internal custody caveat (`ORIGINAL_DOCX_ROUND_TRIP_NOT_REPROVEN`)
appears in a Bariah-facing string. **The suite did not notice.**

The cause: `t04_review_semantic_v1.model_strings()` read `R.BLOCKS` — a module constant
computed once at import. Edit the model and the projection keeps reporting the old content, so
every parity gate was comparing the artifacts against a snapshot rather than against the model.

This is the same stale-constant defect that fixture `W-22` found in the Stage 4.2F-B0.7 suite
and fixture `V-03` found in the Stage 4.2F-B0.8 suite. **Third occurrence, third different
shape:** a cached total, then a cached count, now a cached projection.

Fixed: `model_strings()` calls `R.blocks()` live, the DOCX-structure gates use a live block
list, and `MODEL_PROJECTION_DERIVED_LIVE` was added. The custody gate now scans both the DOCX
text and the live projection, so either route fires.

**The generalisable rule, stated plainly: any module-level value computed from mutable data is
invisible to a gate that reads it.** Three stages have now paid for that lesson in three
different places. Every derived quantity in these suites should be recomputed inside the gate.

# 4. Mutation fixtures

45 fixtures across three patch targets, **45 detected, 0 missed, 0 baseline false failures**.
All 29 mutations named in the brief are covered; 16 more were added. The suite is re-run after
the whole fixture set and `post_run_restored` confirms the on-disk artifacts came back
byte-identical.

Seven fixtures rewrite the **artifact on disk** rather than patching memory — that is the only
honest way to model "a sentence exists only in the DOCX":

| Fixture | Target | Defect |
|---|---|---|
| `X-01` | DOCX file | a sentence added only to the DOCX |
| `X-02` | MD file | a reviewable item removed from the Markdown |
| `X-03` | DOCX file | one quiz option altered only in the DOCX |
| `X-04` | DOCX file | a repository path injected |
| `X-05` | DOCX file | English instructions in Section F |
| `X-06` | DOCX file | the final verdict removed |
| `X-07` | DOCX file | the signature field removed |

Named in the brief and covered: `X-01` DOCX-only instruction · `X-02` MD item removed · `X-03`
DOCX-only option change · `X-08` 41→46 · `X-09` composite disclosure removed · `X-10`
no-separate-asset disclosure removed · `X-11` AG-08 as a Bariah ruling · `X-13` AG-01 seventh
asset as Bariah-named · `X-14` hidden do-not-reuse constraint · `X-15` unrestricted reuse
question · `X-17` MERGE with no target · `X-18` merge with itself · `X-20` MERGE on a quiz item
· `X-21` MERGE treated as REUSE · `X-23` Slide 2 boundary removed · `X-24` licensed-operator
duty in dialogue · `X-26` Rumusan 04 risk note removed · `X-27` DEP-RUM04-Q5 removed · `X-28`
Q5 auto-deleted · `X-29` answer key final · `X-30` composition changed · `X-32` source evidence
removed · `X-05` English Section F · `X-04` repository path · `X-06` verdict removed · `X-07`
signature removed · `X-44` total edited after caching · `X-37` manual DOCX marked deliverable ·
`X-40` native render claimed passed.

Added beyond the brief: `X-12` AG-08 folded into the 46 · `X-16` proposed assets shown as
approved · `X-19` merge target does not resolve · `X-22` structural item loses MERGE · `X-25`
cast marked final · `X-31` threshold changed · `X-33` quiz declared source-unsupported · `X-34`
custody caveat pushed to Bariah · `X-35` Q5 distractor review removed · `X-36` reviewable item
marked approved · `X-38` manual DOCX as authority · `X-39` Markdown declared the approval
artifact · `X-41` delivery upgraded without a render · `X-42` `NOT_CHECKED` removed · `X-43`
suite identity lost · `X-45` gate population emptied.

# 5. Rendering — what was and was not checked

```
DOCX_NATIVE_RENDER = NOT_CHECKED_RENDERER_UNAVAILABLE
```

LibreOffice 24.2.7.2 is installed, but `dpkg -l` shows only `libreoffice-core` and
`libreoffice-common` — there is **no `libreoffice-writer` package** and therefore no Writer
import filter. Both `soffice --convert-to pdf` and `--convert-to txt` fail with *"source file
could not be loaded"* on a known-good DOCX. This is the same shape as the missing Impress
filter recorded in earlier stages.

**I did not open this document in Word and I am not claiming otherwise.** A gate asserts the
render status starts with `NOT_CHECKED`, a second asserts that the delivery status follows
from it, and fixtures `X-40` and `X-41` prove both fire if someone upgrades either.

What exists instead: **10 deterministic preview pages** rendered from the same block list at A4
with real font metrics. Its limitations are recorded, not glossed — it is a layout
approximation, and it uses Liberation Sans, which lacks U+2610, so the checkboxes show a
fallback glyph *in the preview only*.

Structural DOCX validation, which does not need a renderer, all passed: valid ZIP, every XML
part parses, all relationships resolve, no duplicate relationship IDs, no media, no external
links, 6 page breaks matching the 6 modelled section boundaries, every table grid summing
exactly to the content width, A4 page size, document ends on content. python-docx opens the
file and reports 281 paragraphs and 6 tables.

# 6. `NOT_CHECKED`

- how Microsoft Word paginates the document — no Writer-compatible renderer exists here
- whether the ☐ glyph (U+2610) resolves in Word's font fallback on the reviewer's machine
- whether any table overflows its page width once Word applies its own column fitting
- whether headings orphan at page boundaries in Word
- whether the document reads well to a native Malay speaker
- whether Bariah finds the decision fields usable in practice
- the real page count — the deterministic preview estimates it, Word decides it

# 7. Chain status, each with its own suite identity

| `SUITE_ID` | Governs | Gates | Fixtures |
|---|---|---|---|
| `T04_BARIAH_REVIEW_ARTIFACT_QA_v1` | the review artifact | **133 / 133** | **45 / 45 detected** |
| `T04_CONTENT_QA_v1` | T04 content and instance mapping | 138 / 138 | 53 / 53 detected |
| `T04_FINAL_RULINGS_QA_v1` | final structural rulings | 105 / 105 | 32 / 32 detected |
| `T04_RULINGS_QA_v1` | partial rulings | 130 / 130 | 26 / 26 detected |
| `T04_PACK_QA_v1` | pre-storyboard decision pack | 107 / 107 | 39 / 39 detected |
| `T04_EXTRACTION_QA_v1` | controlled source extraction | 109 / 109 | 30 ran, 30 detected · **4 `SKIPPED_NO_DOCX`, not counted as passing** |
| `PL06_INVENTORY_QA_v1` | PL06 inventory | 140 / 140 | 54 / 54 detected |

`T04_CONTENT_QA_v1` was re-run after the Part 10 Q5 distractor revision and still reports
138/138 with 53/53 fixtures detected.
