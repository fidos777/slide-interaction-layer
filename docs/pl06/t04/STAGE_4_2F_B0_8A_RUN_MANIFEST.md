# STAGE_4_2F_B0_8A_RUN_MANIFEST

```
STAGE                  = 4.2F-B0.8A — GOVERNED BARIAH REVIEW ARTIFACT
SUITE_ID               = T04_BARIAH_REVIEW_ARTIFACT_QA_v1
SCOPE                  = ONE GOVERNED REVIEW MODEL AND ITS THREE REPRESENTATIONS
PPTX_GENERATED         = 0
GENERATOR_TOUCHED      = 0
MMD_PRODUCTION_STARTED = 0
DOCX_NATIVE_RENDER     = NOT_CHECKED_RENDERER_UNAVAILABLE
DELIVERY_STATUS        = READY_FOR_FIRDAUS_VISUAL_CHECK
VERDICT = T04_GOVERNED_BARIAH_REVIEW_ARTIFACT_READY_FOR_FIRDAUS_VISUAL_CHECK
```

# 1. Pre-flight

| Check | Result |
|---|---|
| Repository / branch | `/home/user/slide-interaction-layer` · `claude/verify-powerpoint-file-vpfzkg` |
| HEAD at start | `1df741e72bb49b82eb8f7882afbeec4abe7624cb` — matches `1df741e` |
| Working tree | clean |
| Stage 4.2F-B0.8 commit | present |
| `T04_CONTENT_QA_v1` | **138 / 138** |
| B0.8 mutations | **53 / 53 detected**, 0 missed, 0 baseline false failures |
| Six controlled JSON artifacts | all parse |
| `T04_BARIAH_CONTENT_REVIEW_PACK_v1.md` | present, 7,717 bytes |

# 2. The external manual DOCX

```
filename          = T04_Pakej_Semakan_Bariah_v1.docx
byte_size         = 46,676
sha256            = 9c354b0e39e8667401b70a675775ce990169e8dbbb3f403e7d7bd57d32f24873
non_empty_paras   = 296
status            = NON_GOVERNED_REFERENCE
delivery_status   = WITHDRAWN_NOT_FOR_BARIAH
used_as_authority = False
copied_into_repo  = False
```

**Page count is not readable.** `docProps/app.xml` declares `Pages=1` and `Words=0`, which
Word writes when a document has never been repaginated by the application. No renderer here
can determine the real count, so none is claimed.

**Six classes of substantive content existed only inside it** — which is what made it
non-governed, and what this stage exists to close:

- reviewer instructions (*"Cara semak"*), absent from the validated Markdown
- a *"Ringkasan cadangan"* totals line, present only in the DOCX
- **two different final-verdict vocabularies in one document** — *"Lulus / Lulus dengan
  pindaan / Perlu dibaiki"* near the top and *"Lulus untuk generate storyboard / Lulus dengan
  pindaan / Belum lulus"* at the end. A reviewer could tick both and mean different things
- decision boxes abbreviated to `A / E / M / R`, unexpandable without a legend
- MERGE offered with no target field, so a merge decision could not be recorded at all
- *"Arahan selepas semakan"* instructions, present only in the DOCX

It is a competent human document. It is not a governed one. It was not committed, not copied
into the evidence directory, and not read as data.

# 3. Declared artifact hierarchy

| Role | Artifact |
|---|---|
| `CONTROLLED_CONTENT_SOURCE_OF_TRUTH` | `docs/pl06/t04/T04_BARIAH_REVIEW_MODEL_v1.json` |
| `GENERATED_REFERENCE_VIEW` | `docs/pl06/t04/T04_BARIAH_CONTENT_REVIEW_PACK_v2.md` |
| `HUMAN_APPROVAL_ARTIFACT` | `reviews/storyboard-bariah/t04_bariah_review/T04_Pakej_Semakan_Bariah_v2.docx` |

**The design that makes this hold.** `t04_review_render_v1.blocks()` turns the model into one
ordered list of semantic blocks. The Markdown renderer and the DOCX renderer both consume that
same list and neither may add a block. A sentence cannot appear in the DOCX and not in the
Markdown because **there is no code path that could put it there**. The DOCX is assembled as
OOXML directly — no document library, no template — so "nothing was manually added" is
auditable rather than asserted.

# 4. Governed review model

6 top-level sections · **47 reviewable items** · every item carries a stable ID, display text,
`CAIR_ASSISTED_DRAFT`, `BARIAH`, `PENDING_BARIAH_REVIEW`, its allowed decisions, a comment
field, its source artifact and its internal provenance.

# 5. Screen-review decision model

21 screens, each showing only what a reviewer needs: ID, title, treatment **in clear Malay**,
short purpose, content population, proposed visual, decision fields, merge-target field,
comment. Technical treatment codes stay in the model.

```
CONTENT_STATIC                → Kandungan statik
CLICK_TO_REVEAL               → Klik untuk paparkan maklumat
PROCESS_FLOW_STEPPED          → Aliran proses berperingkat
DIALOGUE_SCENARIO             → Senario perbualan
CONTENT_WITH_CONFIRMED_REVEAL → Kandungan utama dengan maklumat tambahan boleh dibuka
```

`PROPOSED_LEARNER_SCREEN_COUNT = 21` · `FINAL_LEARNER_SCREEN_COUNT = PENDING_BARIAH_APPROVAL`.

# 6. MERGE relationship model

MERGE is offered **only** on screens and asset groups. Dialogue lines, Rumusan points and quiz
items get `TERIMA / PINDA / BUANG` and nothing else.

Every MERGE carries four fields — `merge_source_id`, `merge_target_id`, `merge_reason`,
`proposed_resulting_title_or_group`. Gates reject a merge with no target, a merge with itself,
and a target that does not resolve.

```
☐ TERIMA   ☐ PINDA   ☐ BUANG   ☐ GABUNG DENGAN ID: __________
Sebab / cadangan susunan baharu: ____________________________________
```

**MERGE is not REUSE.** Reuse has its own field —
`Boleh dikongsi / Tidak boleh dikongsi / Boleh dikongsi dengan syarat`. Conflating them would
let a reuse answer silently delete a screen.

# 7. Visual totals and arithmetic

```
46 keperluan visual
tolak 5 keperluan yang dipenuhi oleh visual gabungan
tolak 3 tajuk pengelompokan yang tidak memerlukan visual berasingan
tambah 3 aset tambahan yang bukan keperluan visual
bersamaan 41 visual berasingan yang dicadangkan          PROPOSED_NOT_APPROVED
```

A gate recomputes `46 − 5 − 3 + 3 = 41` and fails if the stated total drifts from the stated
components. 46 obligations are never described as 46 assets.

# 8. AG-01 and AG-08 provenance

**AG-01.** The six step visuals are `KEPERLUAN_VISUAL_BARIAH`. The **seventh** asset — the
controlled redraw of the six-step process diagram — is
`CADANGAN_PELAKSANAAN_CAIR_DARIPADA_D05`, a CAIR implementation proposal following D-05, not
something Bariah named.

**AG-08.** Both Slide 2 scenario assets are `CADANGAN_CAIR_UNTUK_SENARIO` and are **not part of
the 46**. Bariah's visual ruling covers content headings; the scenario screen arrives from the
separate dialogue ruling.

Stated in the document in Malay, verbatim:

> Bariah menetapkan bahawa kandungan yang dinyatakan memerlukan layanan visual. Hierarki tajuk
> dalam modul digunakan untuk menyenaraikan populasi terperinci. CAIR mencadangkan pengumpulan
> aset dan pendekatan penghasilan.

# 9. Composite and no-separate-asset disclosures

Both are disclosed with their affected items named, not hidden to keep a table short.

**5 composite-covered** — *"Lima keperluan visual dipenuhi oleh satu visual gabungan yang telah
pun menyokong keperluan lain yang berkaitan. Setiap satu tetap mendapat layanan visual — sebagai
panel berlabel di dalam visual gabungan itu."*

**3 no-separate-asset** — *"Tiga tajuk berfungsi sebagai pengelompokan kandungan sahaja dan
tidak memerlukan imej tersendiri."*

Items are named by **clear label**, not by internal obligation ID — see the QA report §2.2.

# 10. Do-not-reuse disclosures

**2 groups, 3 obligations**, both counts reported separately and both shown before the reuse
question is asked:

- Pengurusan Stok dan Penyimpanan (Baja) — fertiliser storage differs from pesticide storage
- Keselamatan Pekerja (Baja) — fertiliser PPE differs from pesticide PPE
- Keselamatan dan Kesihatan (HSE) (Racun) — the heavier pesticide set

The question asked is the constrained one:

> Selain visual yang telah ditandakan tidak boleh digunakan semula, adakah visual lain boleh
> dikongsi antara lebih daripada satu skrin?

A gate rejects the unrestricted form, which would hide three known constraints.

# 11. Dialogue boundary

`PROCESS_OVERVIEW_ONLY`, held in the **model**, not only in the DOCX. Four rules, printed in
Malay for the reviewer: no statutory obligation in character dialogue; Encik Rahman is not
represented as a licensed pesticide operator; no PPE, SDS or chemical-storage instruction.

A gate scans every dialogue line for the source's own compliance vocabulary. Fixture `X-24`
puts a licensed-operator duty in Encik Rahman's mouth and it fires. Cast status remains
`PROPOSED_SUBJECT_TO_BARIAH_APPROVAL`, scoped to Slide 2 only.

# 12. Rumusan 04 and the Q5 dependency

`T04-RUM2-04` keeps `MEDIUM_FACTUAL_RISK` and
`GENERALISATION_REQUIRES_BARIAH_DECISION`, with the note printed in plain Malay asking her to
accept, narrow or remove it.

```
dependency_id           = DEP-RUM04-Q5
trigger                 = RUMUSAN_04_EDITED_OR_REMOVED_DUE_TO_OVER_GENERALISATION
effect                  = Q5_REQUIRES_CONSISTENCY_REVIEW
automatic_invalidation  = False
```

The document does **not** say that removing Rumusan 04 invalidates Q5. It says Q5's wording
would need re-checking. Fixture `X-28` proves the gate fires if that is ever upgraded to
automatic deletion.

# 13. Q5 distractor review — REVISED

The Part 10 review found the old options E and F were direct negations of stated duties
(*empty containers may be reused*, *spraying needs no notification*) — refutable without
understanding the material.

Searching **only the controlled T04 extract**, two stronger distractors exist. Both are
**true statements in the module** that belong to Baja rather than to pesticide spraying:

| | Old | New |
|---|---|---|
| E | Bekas racun kosong boleh digunakan semula (contradicted by `T04-ROW-072`) | Baja disimpan di tempat yang kering dan jauh dari sumber air (`T04-ROW-041`) |
| F | Semburan tanpa memaklumkan penduduk (contradicted by `T04-ROW-077`) | Rekod pembajaan disimpan sebagai bukti kerja untuk tuntutan bayaran (`T04-ROW-045`) |

Four proposed correct answers preserved. Difficulty moves from `LOW_DISTRACTOR_DIFFICULTY` to
`MODERATE_DISTRACTOR_DIFFICULTY`.

**The trade-off is flagged, not decided.** Option F asks the learner to distinguish *rekod
pembajaan* from the spraying record duty in `T04-ROW-078` — a fine distinction a reviewer could
reasonably call a trick. Bariah is told so in Malay and can revert both options.

**Where the revision was applied.** In `t04_content_data_v1.py`, the single controlled source
for quiz content — not in the review model. Applying it only here would have created a fresh
divergence between the B0.8 quiz artifact and the review model while claiming to close one.
`T04_CONTENT_QA_v1` was re-run afterwards: still 138/138, 53/53 fixtures. This means Stage
4.2F-B0.8's quiz artifacts were regenerated in this stage, which goes beyond Part 17's commit
list — stated here rather than slipped in.

# 14. Semantic parity

```
JSON_MODEL_SEMANTIC_DIGEST = 22d42f1b9b6bd1e0…
MARKDOWN_SEMANTIC_DIGEST   = 22d42f1b9b6bd1e0…
DOCX_SEMANTIC_DIGEST       = 22d42f1b9b6bd1e0…
all_three_agree            = True
substantive strings        = model 489 · markdown 489 · docx 489
docx_only_substantive      = []
markdown_only_substantive  = []
```

The Markdown and the DOCX are **re-parsed from disk**, not re-derived from the renderer, so the
check genuinely catches content living in one artifact and not another. Permitted formatting
differences: heading markers, bold/italic, bullet glyphs, table pipes, blockquote markers,
horizontal rules, runs of underscores.

**Proves** that no substantive sentence exists in one artifact and not the others.
**Does not prove** that the DOCX renders correctly.

# 15. Governed DOCX

```
filename               = T04_Pakej_Semakan_Bariah_v2.docx
path                   = reviews/storyboard-bariah/t04_bariah_review/
byte_size              = 12,571
sha256                 = d7e62a8cb5625a6023ea4c951f52b195cced031a3eb0418a91fcde1315f7473d
page_count (estimated) = 10
generation_timestamp   = 2026-08-02T10:40:00Z
source_model_hash      = 52b71c9e2874d40b974a3d648373b387e0b9030902a8ca89441605b081f9c86d
generator_version      = t04_review_render_v1
semantic_item_count    = 47
delivery_status        = READY_FOR_FIRDAUS_VISUAL_CHECK
```

**The page count is an estimate from the deterministic preview, not a Word pagination.** Word
decides the real count.

# 16. Rendering

```
DOCX_NATIVE_RENDER = NOT_CHECKED_RENDERER_UNAVAILABLE
```

LibreOffice 24.2.7.2 is installed but only `libreoffice-core` and `libreoffice-common` are
present — there is no `libreoffice-writer` package and therefore no Writer import filter.
`--convert-to pdf` and `--convert-to txt` both fail with *"source file could not be loaded"* on
a known-good DOCX.

**I did not open this in Word and I am not claiming I did.** Fallback: 10 deterministic preview
pages under `docs/pl06/t04/preview/`, rendered from the same block list at A4 with real font
metrics. Its limitation is recorded: it uses Liberation Sans, which lacks U+2610, so checkboxes
show a fallback glyph *in the preview only*.

Structural validation, which needs no renderer, passed in full: valid ZIP, all XML parses, all
relationships resolve, no duplicate relationship IDs, no media, no external links, 6 page
breaks matching 6 modelled section boundaries, every table grid summing exactly to the content
width, A4, ends on content. python-docx opens it: 281 paragraphs, 6 tables.

**For Firdaus to check in Word:** the ☐ glyph renders; no table spills past the right margin;
no heading is orphaned at a page foot; the Section F block sits on one page; the signature line
is not the only thing on a final page.

# 17. QA

| | |
|---|---:|
| `T04_BARIAH_REVIEW_ARTIFACT_QA_v1` | **133 / 133**, 0 vacuous |
| Fixtures | **45 / 45 detected**, 0 missed, 0 baseline false failures |

**Not merged with `T04_CONTENT_QA_v1`'s 138.** Different suites, different artifacts,
non-additive.

Five gates failed on first run: **two real artifact defects** (reviewable items with no visible
ID; obligation IDs leaking into the reviewer's document) and three errors in my own extractor
and expectations. And for the **third stage running**, a fixture caught what the suite could
not — a cached module constant, this time the model projection itself. See the QA report §2–§3.

# 18. `NOT_CHECKED`

Seven items, published in full in the QA report §6 — headed by Word pagination, the ☐ glyph
fallback, table overflow under Word's own column fitting, and whether the Malay reads well to a
native speaker.

# 19. Constraints honoured

- **No storyboard PPTX generated.**
- No production storyboard generator modified — 0 changed files under `reviews/source-completion/`.
- **No MMD production started.**
- No React, no SCORM.
- No content marked Bariah-approved — every reviewable item is `CAIR_ASSISTED_DRAFT` /
  `PENDING_BARIAH_REVIEW`, gate-checked across all 47.
- The manual v1 DOCX was not committed, not copied into the evidence directory, and not used as
  data.
- `1df741e` not amended.
