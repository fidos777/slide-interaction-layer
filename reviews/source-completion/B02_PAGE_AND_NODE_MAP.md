# B02_PAGE_AND_NODE_MAP

```
AUTHORITY: PDF (rendered pagination + heading numbering)  ·  ALL PAGES MEASURED
```

Text source: `…300426.docx` · Rendered source: `K5_PL06_T03_B02_pages_256269.pdf`
(`sha256 30a6903d…f828a3f4`, 429,918 B, 14 pages)

---

## 1. Folio map — measured on every page

Printed folio reads `Pembinaan Landskap Luar | Mukasurat NNN`. Read on all 14 pages.

| physical | module | | physical | module |
|---:|---:|---|---:|---:|
| 256 | 237 | | 263 | 244 |
| 257 | 238 | | 264 | 245 |
| 258 | 239 | | 265 | 246 |
| 259 | 240 | | 266 | 247 |
| 260 | 241 | | 267 | 248 |
| 261 | 242 | | 268 | 249 |
| 262 | 243 | | 269 | 250 |

**Offset = +19, constant across all 14 pages.** Scope `237–250` ↔ `256–269` confirmed exactly as stated.

## 2. Node map — measured, with rendered numbering

| Rendered no. | Heading (verbatim) | mod p | phys p | Screen | Table | Assets |
|---|---|---:|---:|---|---|---:|
| `3.3.` | Struktur Taman | 237 | 256 | S04 base | — | 0 |
| `3.3.1` | Struktur Persisir Air (Promenande, Jeti, Dek, Boardwalk, footbridge) | **238** | 257 | **S05** | ✅ 5 rows | 1 |
| `3.3.2` | Struktur Teduhan | **239** | 258 | **S06** | ✅ 5 rows | 1 |
| `3.3.3` | Kemudahan Awam | **240** | 259 | **S07** | ✅ 3 rows | **0** |
| `3.3.4` | Water Feature (Fountain, Pond, Pool) | **241** | 260 | **S08** | ✅ 3 rows | **0** |
| `3.4.` | Perabot Taman | 242 | 261 | S10 base | — | 0 |
| **`3.4.1`** | Kerusi Taman | **242** | 261 | **S11** | ✅ 3 rows | 3 |
| **`3.4.1`** | Papan Tanda | **243** | 262 | **S12** | ✅ 1 row | 2 |
| **`3.4.1`** | Tong Sampah | **245** | 264 | **S13** | ✅ 3 rows | 4 |
| `3.4.2` | Drinking Fountain | **247** | 266 | **S14** | ✅ 2 rows | 2 |
| `3.4.3` | BBQ pit | **249** | 268 | **S15** | ✅ 1 row | 1 |

`3.4.1` appears **three times** — see `SOURCE_DEFECT_REGISTER.md` D-2, now
`CONFIRMED_IN_RENDERED_PDF`. Section 3.3 numbers correctly 1–4.

## 3. Correction to the DOCX-era interpolation

Module pages were previously interpolated at 1,021.4 chars/page. **Three of nine were wrong by one page.**

| Screen | Interpolated | **Measured** | |
|---|---:|---:|---|
| S05 | ~237 | **238** | ✗ off by 1 |
| S06 | ~239 | 239 | ✓ |
| S07 | ~240 | 240 | ✓ |
| S08 | ~240 | **241** | ✗ off by 1 |
| S11 | ~242 | 242 | ✓ |
| **S12** | ~244 | **243** | ✗ off by 1 — **and this vindicates the probe** |
| S13 | ~245 | 245 | ✓ |
| S14 | ~247 | 247 | ✓ |
| S15 | ~249 | 249 | ✓ |

**S12 matters.** Probe v0.1 records the Papan Tanda locator as `IMG-05, ms 243`. The interpolation said
~244 and I noted it as "within interpolation error". The rendered PDF measures **243** — the probe was
exactly right and the estimate was wrong. All `~` markers are now retired; every page above is measured.

## 4. Directed mapping — verified

All nine directed assignments match a real numbered heading, in source order. **No mismatch.**
The earlier provisional ordering was correct on all eight previously-unverified screens.

## 5. Now resolved

| Previously | Now |
|---|---|
| Physical PDF pages `NOT DETERMINABLE` | **measured, offset +19** |
| Per-screen module pages interpolated | **measured** — 3 corrections |
| Heading numbering invisible | **measured** — D-2 confirmed |
| `IMG-05` / ms 243 "within interpolation error" | **exactly confirmed** |

Still open: what `IMG-01` (ms 237) depicts — module p237 carries no image, and the first figure in 3.3
is Rajah 23 on p239.
