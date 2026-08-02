# T04_BARIAH_REVIEW_ARTIFACT_MANIFEST_v1

```
STAGE            = 4.2F-B0.8A
UNIT             = K5-PL06-T04-B01
DELIVERY_STATUS  = READY_FOR_FIRDAUS_VISUAL_CHECK
NATIVE_RENDER    = NOT_CHECKED_RENDERER_UNAVAILABLE
```

# 1. Artifact hierarchy

| Role | Artifact |
|---|---|
| CONTROLLED_CONTENT_SOURCE_OF_TRUTH | `docs/pl06/t04/T04_BARIAH_REVIEW_MODEL_v1.json` |
| GENERATED_REFERENCE_VIEW | `docs/pl06/t04/T04_BARIAH_CONTENT_REVIEW_PACK_v2.md` |
| HUMAN_APPROVAL_ARTIFACT | `reviews/storyboard-bariah/t04_bariah_review/T04_Pakej_Semakan_Bariah_v2.docx` |

Every substantive item in the DOCX is generated from the model. Nothing substantive may exist only in the DOCX, and no reviewable item may exist only in the Markdown.

# 2. Governed DOCX

```
filename                  = T04_Pakej_Semakan_Bariah_v2.docx
path                      = reviews/storyboard-bariah/t04_bariah_review/T04_Pakej_Semakan_Bariah_v2.docx
byte_size                 = 12571
sha256                    = d7e62a8cb5625a6023ea4c951f52b195cced031a3eb0418a91fcde1315f7473d
page_count (estimated)    = 10
generation_timestamp      = 2026-08-02T10:40:00Z
source_model_hash         = 52b71c9e2874d40b974a3d648373b387e0b9030902a8ca89441605b081f9c86d
generator_version         = t04_review_render_v1
semantic_item_count       = 47
delivery_status           = READY_FOR_FIRDAUS_VISUAL_CHECK
```

**Page count caveat.** deterministic preview from the same model — NOT a Word pagination; Word decides the real count

# 3. Other governed artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `docs/pl06/t04/T04_BARIAH_REVIEW_MODEL_v1.json` | 63,655 | `52b71c9e2874d40b974a3d648373b387e0b9030902a8ca89441605b081f9c86d` |
| `docs/pl06/t04/T04_BARIAH_CONTENT_REVIEW_PACK_v2.md` | 25,371 | `f74338950106d990507070af1830fb71d6334580a47b2163c630d61dc40b2f63` |

# 4. Semantic parity

```
JSON_MODEL_SEMANTIC_DIGEST = 22d42f1b9b6bd1e0b57650b078d342fe574cb2e04d07d732e68dba98bc834145
MARKDOWN_SEMANTIC_DIGEST   = 22d42f1b9b6bd1e0b57650b078d342fe574cb2e04d07d732e68dba98bc834145
DOCX_SEMANTIC_DIGEST       = 22d42f1b9b6bd1e0b57650b078d342fe574cb2e04d07d732e68dba98bc834145
all_three_agree            = True
substantive strings        = {'model': 489, 'markdown': 489, 'docx': 489}
docx_only_substantive      = []
markdown_only_substantive  = []
```

**Proves** that no substantive sentence exists in one artifact and not the others.

**Does not prove** that the DOCX renders correctly — see the visual-check record.

Permitted formatting differences: heading markers, bold and italic markers, bullet glyphs, table pipes, blockquote markers, horizontal rules, runs of underscores used as write-in rules.

# 5. Rendering

`NOT_CHECKED_RENDERER_UNAVAILABLE`

LibreOffice 24.2.7.2 is installed but only libreoffice-core and libreoffice-common are present — there is no libreoffice-writer package and therefore no Writer import filter. `soffice --convert-to pdf` and `--convert-to txt` both fail with 'source file could not be loaded' on a known-good DOCX. Same shape as the missing Impress filter recorded in earlier stages.

Fallback: 10 deterministic preview pages in `docs/pl06/t04/preview`.

A deterministic layout approximation, not a Word render. It uses Liberation Sans, which lacks the U+2610 ballot box, so checkboxes appear as a fallback glyph in the preview only.

# 6. The non-governed reference

```
filename         = T04_Pakej_Semakan_Bariah_v1.docx
byte_size        = 46676
sha256           = 9c354b0e39e8667401b70a675775ce990169e8dbbb3f403e7d7bd57d32f24873
status           = NON_GOVERNED_REFERENCE
delivery_status  = WITHDRAWN_NOT_FOR_BARIAH
used_as_authority= False
copied_into_repo = False
```

docProps/app.xml declares Pages=1 and Words=0, which Word writes when a document has never been repaginated by the application. The real page count is not readable from the package, and no renderer is available to determine it.

**Divergences that made it non-governed:**

- reviewer instructions ('Cara semak') present in the DOCX, absent from the Markdown
- a 'Ringkasan cadangan' totals line present only in the DOCX
- TWO different final-verdict vocabularies in one document — 'Lulus / Lulus dengan pindaan / Perlu dibaiki' near the top and 'Lulus untuk generate storyboard / Lulus dengan pindaan / Belum lulus' at the end
- decision checkboxes abbreviated to A / E / M / R, which a reviewer cannot expand without the legend
- MERGE offered with no target-ID field, so a merge decision could not be recorded
- 'Arahan selepas semakan' instructions present only in the DOCX

It is a competent human document. It is not a governed one: six classes of substantive content existed only inside it.

# 7. QA

```
SUITE_ID        = T04_BARIAH_REVIEW_ARTIFACT_QA_v1
SIBLING_SUITE   = T04_CONTENT_QA_v1
```

This suite governs the review ARTIFACT. T04_CONTENT_QA_v1 governs the CONTENT. Their gate counts are not additive and must never be merged.

**NOT_CHECKED**

- how Microsoft Word paginates the document — no Writer-compatible renderer exists here
- whether the ☐ glyph (U+2610) resolves in Word's font fallback on the reviewer's machine
- whether any table overflows its page width once Word applies its own column fitting
- whether headings orphan at page boundaries in Word
- whether the document reads well to a native Malay speaker
- whether Bariah finds the decision fields usable in practice
- the real page count — the deterministic preview estimates it, Word decides it

# 8. Production guards

```
PPTX_GENERATED = 0
GENERATOR_TOUCHED = 0
MMD_PRODUCTION_STARTED = 0
```
