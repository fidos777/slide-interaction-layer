# B02_ASSET_MANIFEST

```
FIGURES IDENTIFIED: 4  ·  FIGURES EXTRACTED: 0  ·  SCREENS WITH NO FIGURE: 6 of 9
source-assets/ REMAINS EMPTY — image binaries not obtainable this session
```

---

## 1. Figures present in scope — `MEASURED_FACT`

Every `Rajah` reference between module pages 237–250. There are exactly four.

| # | Caption (verbatim) | Bound screen | Module page | Proposed asset ID |
|---|---|---|---:|---|
| Rajah 23 | `Contoh Boardwalk dalam Taman Paya Bakau` | **S05** Struktur Persisir Air | ~238 | `K5PL06T03-B02-IMG-23` |
| Rajah 24 | `Contoh Pergola` | **S06** Struktur Teduhan | ~239 | `K5PL06T03-B02-IMG-24` |
| Rajah 25 | `Contoh Lukisan Spesifikasi Papan Tanda Informasi` | **S12** Papan Tanda | ~245 | `K5PL06T03-B02-IMG-25` |
| Rajah 26 | `Contoh Spesifikasi Papan Tanda Penunjuk Arah` | **S12** Papan Tanda | ~245 | `K5PL06T03-B02-IMG-26` |

**IDs are proposals keyed to the module's own `Rajah` numbering**, not minted sequentially. They do
**not** replace the measured `IMG-01` / `IMG-05` locators, whose numbering scheme is different and
whose origin is the Tier-1 spec, not this document.

## 2. Screens with no figure — six of nine — `MEASURED_FACT`

| Screen | Figure | What the source does provide |
|---|---|---|
| **S07** Kemudahan Awam | **none** | 3-row table: Tandas Awam · Surau · Bangunan Interpretatif |
| **S08** Water Feature | **none** | 3-row table: Air Pancut · Kolam · Kolam Renang/Hiasan |
| **S11** Kerusi Taman | **none** | 3-row table: Kayu Keras · Konkrit · Komposit |
| **S13** Tong Sampah | **none** | 3-row table: Logam · Konkrit/Batu · Plastik HDPE |
| **S14** Drinking Fountain | **none** | 2-row table: Keluli Tahan Karat · Konkrit/Batu |
| **S15** BBQ pit | **none** | 1-row table: Struktur Kekal (Bata/Konkrit/Batu) |

**No visual is fabricated for these six.** The module provides no suitable image, and per the standing
instruction that absence is recorded rather than filled. Their `Visual:` regions stay as source-bound
placeholders.

**The specification tables are a genuine alternative.** Each is real, source-bound, on-topic content
that could carry the visual region without inventing anything — see
`SOURCE_COMPLETION_IMPLEMENTATION_PLAN.md` §5 for that as an open option, not a decision.

## 3. Why nothing was extracted — `MEASURED_FACT`

| Route | Outcome |
|---|---|
| Drive `read_file_content` | text only — figures appear as captions |
| Drive `download_file_content` | base64 of the whole 16.8 MB file ≈ 22 MB encoded, exceeds a returnable tool result |
| Attachment | failed three times |

`source-assets/` is empty and correctly so.

## 4. Extraction schema — ready

| asset ID | source ref | module page | caption | type | px w×h | sha256 | bound screen |
|---|---|---|---|---|---|---|---|
| *(pending image binaries)* | | | | | | | |

Naming once obtainable: `K5PL06T03-B02-IMG-<rajah>__p<module>.png`

## 5. To close

Any one of: the PDF · the four figures exported individually · a DOCX containing only pages 237–250.
**Four images are needed. Not four hundred.**
