# B02_ASSET_MANIFEST

```
AUTHORITY: PDF (rendered visuals)  ·  14 ASSETS EXTRACTED  ·  7 of 9 screens covered
```

Source: `K5_PL06_T03_B02_pages_256269.pdf` — `sha256 30a6903dacbd7e8bce60dc1aa32026fc4ed98439054aeced9e895b5df828a3f4`, 429,918 B, 14 pages.
Extracted to `source-assets/`. Machine-readable copy: `source-assets/_manifest.json`.

**This supersedes the DOCX-era finding that six mapped screens had no figure.** That was an artefact of
text extraction: only *captioned* `Rajah` figures survive in text. The rendered PDF carries **10 further
unnumbered photographs embedded inside specification tables**.

---

## 1. Register — 14 assets

| asset_id | source component | mod p | phys p | crop boundary (pt) | type | dims | sha256 (12) | screen | usage status |
|---|---|---:|---:|---|---|---|---|---|---|
| `…IMG-p239-x20` | **Rajah 23** — Contoh Boardwalk dalam Taman Paya Bakau | 239 | 258 | (146.5,57.6)-(462.3,247.2) | jpeg | 658×395 | `bef9c985cb4f` | **S05** | EXTRACTED — not yet bound |
| `…IMG-p240-x23` | **Rajah 24** — Contoh Pergola | 240 | 259 | (164.5,57.6)-(445.4,268.1) | jpeg | 506×379 | `e8b70553d778` | **S06** | EXTRACTED — not yet bound |
| `…IMG-p242-x28` | Kerusi Taman — jadual spesifikasi (Kerusi Kayu Keras) | 242 | 261 | (115.8,469.7)-(326.6,680.4) | jpeg | 439×439 | `20156d98825a` | **S11** | EXTRACTED — not yet bound |
| `…IMG-p243-x31` | Kerusi Taman — jadual spesifikasi (Kerusi Konkrit) | 243 | 262 | (115.8,88.9)-(330.5,249.2) | jpeg | 447×334 | `cc93e6d12192` | **S11** | EXTRACTED — not yet bound |
| `…IMG-p243-x32` | Kerusi Taman — jadual spesifikasi (Komposit/WPC) | 243 | 262 | (115.8,359.2)-(322.0,532.4) | jpeg | 429×361 | `af47d4bb630b` | **S11** | EXTRACTED — not yet bound |
| `…IMG-p245-x37` | **Rajah 25** — Contoh Lukisan Spesifikasi Papan Tanda Informasi | 245 | 264 | (195.2,57.6)-(414.8,313.8) | jpeg | 408×476 | `68734d4280d4` | **S12** | EXTRACTED — not yet bound |
| `…IMG-p245-x38` | **Rajah 26** — Contoh Spesifikasi Papan Tanda Penunjuk Arah | 245 | 264 | (193.7,365.4)-(416.2,619.7) | jpeg | 413×472 | `6c686e23f8b9` | **S12** | EXTRACTED — not yet bound |
| `…IMG-p246-x41` | Tong Sampah — jadual spesifikasi (Logam) | 246 | 265 | (115.9,262.1)-(329.6,515.5) | jpeg | 420×498 | `32d066ad134e` | **S13** | EXTRACTED — not yet bound |
| `…IMG-p247-x44` | Tong Sampah — jadual spesifikasi (Konkrit/Batu) | 247 | 266 | (136.1,73.0)-(310.1,247.0) | jpeg | 337×337 | `102aa3928eeb` | **S13** | EXTRACTED — not yet bound |
| `…IMG-p247-x45` | Tong Sampah — jadual spesifikasi (Plastik HDPE, kiri) | 247 | 266 | (115.8,376.5)-(210.9,511.3) | jpeg | 198×281 | `dcb49ca52d02` | **S13** | EXTRACTED — not yet bound |
| `…IMG-p247-x46` | Tong Sampah — jadual spesifikasi (Plastik HDPE, kanan) | 247 | 266 | (214.3,376.5)-(308.0,510.9) | jpeg | 195×280 | `6f7c1939d836` | **S13** | EXTRACTED — not yet bound |
| `…IMG-p248-x49` | Drinking Fountain — jadual spesifikasi (Keluli Tahan Karat) | 248 | 267 | (126.4,200.0)-(319.4,446.7) | jpeg | 273×349 | `029462212a70` | **S14** | EXTRACTED — not yet bound |
| `…IMG-p249-x56` | Drinking Fountain — jadual spesifikasi (Konkrit/Batu) | 249 | 268 | (127.2,56.6)-(319.1,248.6) | jpeg | 344×344 | `0ecab1c85c44` | **S14** | EXTRACTED — not yet bound |
| `…IMG-p249-x57` | BBQ pit — jadual spesifikasi (Struktur Kekal) | 249 | 268 | (118.5,578.5)-(327.8,735.6) | jpeg | 436×327 | `c9fcef880b27` | **S15** | EXTRACTED — not yet bound |

Full IDs carry the `K5PL06T03-B02-` prefix. Filenames are `<asset_id>.jpeg`. Total 408 KB.
`usage_status` is `EXTRACTED — not yet bound` for all 14: no PPTX is generated at this gate.

## 2. Coverage

| Screen | Assets | Kind |
|---|---:|---|
| S05 Struktur Persisir Air | 1 | numbered figure |
| S06 Struktur Teduhan | 1 | numbered figure |
| **S07 Kemudahan Awam** | **0** | **`NO_DEDICATED_SOURCE_IMAGE`** — §4 |
| **S08 Water Feature** | **0** | **`NO_DEDICATED_SOURCE_IMAGE`** — §4 |
| S11 Kerusi Taman | 3 | table photographs |
| S12 Papan Tanda | 2 | numbered figures |
| S13 Tong Sampah | 4 | table photographs |
| S14 Drinking Fountain | 2 | table photographs |
| S15 BBQ pit | 1 | table photograph |

**7 of 9 screens now have source imagery. 4 numbered figures + 10 unnumbered table photographs.**

## 3. Ownership method — and one refinement to the directed list

Every image was assigned by **vertical position against the numbered heading on its page**, not by page
number alone. Section headings and images interleave, so page-level assignment would misattribute.

Worked example — module p247 (phys 266): `3.4.2 Drinking Fountain` sits at **y = 537.2**. All three
images on that page are at y = 73.0, 376.5, 376.5 — **above the heading**, therefore inside the
preceding *Tong Sampah* table.

**Refinement to the instruction's asset list, offered for confirmation:**

| Directed | Measured | Reason |
|---|---|---|
| S13 Tong Sampah — p246–247 | ✅ **p246–247**, 4 images | matches |
| S14 Drinking Fountain — p247–**248** | ⚠️ **p248–249**, 2 images | the *section* begins on p247 (heading at y = 537), but its **images** are on p248 and the top of p249. p247's three images sit above the heading and belong to Tong Sampah |
| S15 BBQ pit — p249 | ✅ **p249**, 1 image | `3.4.3 BBQ pit` at y = 274.3; the p249 image at y = 578.5 is below it. The other p249 image (y = 56.6) is above it and belongs to Drinking Fountain |

Same total either way — 14 of 14 assigned, none orphaned. The difference is only which of the two
p247/p249 boundary images falls on which side. **Not silently applied; flag if you read it differently.**

## 4. S07 and S08 — `NO_DEDICATED_SOURCE_IMAGE`

| Screen | Module page | Verified |
|---|---:|---|
| **S07 Kemudahan Awam** | 240 | `3.3.3` at y = 320.0 on p240; the only p240 image (y = 57.6) is above it and belongs to S06. **p241 carries no image at all** |
| **S08 Water Feature** | 241 | `3.3.4` at y = 112.0 on p241; **zero embedded images on that page** |

Both are confirmed absences in the rendered PDF, not extraction failures.

### Two treatment recommendations — **neither selected, neither implemented**

**Option A — source-derived native typology diagram.**
Build a simple native-shape diagram from the screen's own specification table. S07 → three labelled
cells (Tandas Awam · Surau · Bangunan Interpretatif); S08 → three (Air Pancut · Kolam · Kolam
Renang/Hiasan). Every label and gloss comes from the table verbatim.
*For:* fills the visual region with source-bound content, matches the deck's native-geometry approach,
scales to the panel. *Against:* it is a **rendering of** the source, not an image **from** it — a
distinction that must stay visible in provenance.

**Option B — cropped source table.**
Crop the specification table from the rendered PDF and place it as an image.
*For:* unambiguously an artefact of the module; zero interpretive step. *Against:* small type in a
5.8621 × 5.1387 in panel — legibility needs testing; it duplicates content the display already carries.

**Both are source-bound. Neither invents imagery, and no external image is sourced.**
`OPEN_DECISION` — carried to `SOURCE_COMPLETION_IMPLEMENTATION_PLAN.md` as `DEC-1`.

## 5. Reconciliation with the pre-existing locators

| Locator | Held | Rendered PDF | Verdict |
|---|---|---|---|
| `IMG-05`, ms **243** (S12) | probe v0.1 | `3.4.1 Papan Tanda` measured at **module 243** | ✅ **confirmed exactly.** The DOCX interpolation had estimated ~244 — the probe was right and the estimate was off by one |
| `IMG-01`, ms **237** (S04) | probe v0.1 | `3.3 Struktur Taman` opens on **module 237** ✅ | page confirmed. **p237 carries no image**; the first figure in 3.3 is Rajah 23 on p239. What `IMG-01` depicts is still unresolved |

Neither locator is overwritten. The `IMG-p<mod>-x<xref>` scheme is **provisional and parallel**, keyed
to measured page and PDF object; it does not replace the Tier-1 `IMG-nn` numbering.
