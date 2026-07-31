# SOURCE_ARTIFACT_INVENTORY — K5 PL06 T3 B02 source completion

```
GATE STATUS: SOURCE COMPLETE — TEXT (DOCX) + RENDERED PAGINATION & VISUALS (PDF)
AUTHORITY SPLIT:  DOCX = text extraction  ·  PDF = pagination, heading numbering, visuals
```

## 0. Two sources, two authorities

| Artifact | Authority for | Status |
|---|---|---|
| `[PROOFREAD FINAL] … 300426.docx` (Drive `16j15Knt…bJ4`, 16.8 MB) | **text extraction** | ✅ accepted, **not redone** |
| `K5_PL06_T03_B02_pages_256269.pdf` — `sha256 30a6903dacbd7e8bce60dc1aa32026fc4ed98439054aeced9e895b5df828a3f4`, 429,918 B, 14 pp | **rendered pagination · heading numbering · visuals** | ✅ received, extracted |

The DOCX text extraction stands unchanged and the 13/19 text-coverage result is preserved. The PDF
resolved the three things text could not carry: physical pagination, Word heading numbering, and
embedded images.

---

## 1. Source acquired — via Google Drive, not attachment

Three attachment attempts did not reach the session. The file was retrieved from Drive instead.

| Property | Value |
|---|---|
| Drive file ID | `16j15Knt75d1ybg1i1E2SWfeUfMRmcbJ4` |
| Title | `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx` |
| MIME type | `application/vnd.openxmlformats-officedocument.wordprocessingml.document` |
| Size | **16,832,861 bytes (16.8 MB)** |
| Modified | 2026-06-07T23:30:02Z |
| Text extracted | **422,472 characters**, 9,566 lines |
| B02 scope extracted | **14,300 characters** |

### 1.1 Three discrepancies against the request — `MEASURED_FACT`

| # | Stated | Actual | Consequence |
|---|---|---|---|
| 1 | `…300426_compressed.pdf` | **`.docx`** | Same document, Word form. Text is *better* for extraction; pagination is worse — see #2 |
| 2 | 3 MB | **16.8 MB** | The 3 MB figure was presumably the compressed PDF. Size is why attachment failed |
| 3 | physical PDF pages ~256–269 | DOCX has no fixed pagination | ~~impossible~~ → **RESOLVED by the PDF extract.** Offset measured at **+19** on all 14 pages |

**This is the authoritative `[PROOFREAD FINAL]` document** and remains the text authority. The
physical-page half of the mapping, which it could not supply, is now supplied by the PDF extract.

## 2. Module page scope — confirmed from the table of contents — `MEASURED_FACT`

| TOC entry | Module page | Requested | Match |
|---|---:|---:|---|
| `3.3. Struktur Taman` | **237** | 237–241 | ✅ |
| `3.4. Perabot Taman` | **242** | 242–250 | ✅ |
| `3.5. Infrastruktur` | 251 | *(scope ends 250)* | ✅ boundary confirmed |

**B02 scope = module pages 237–250**, exactly as specified.

## 3. Text extraction — complete for scope

| Section | Char offset | Content |
|---|---|---|
| `## Struktur Taman` | 309,048 | intro + 4 subsections + tips block |
| `## Perabot Taman` | 313,807 | intro + 5 subsections |
| `## Infrastruktur` | 323,348 | out of scope — boundary |

All **9 mapped screens** have source text. All 9 have a specification **table**. See
`B02_PAGE_AND_NODE_MAP.md`.

### 3.1 Probe v0.1 verified source-faithful — `MEASURED_FACT`

The module's opening line for 3.3 is:

> `Struktur taman membina fungsi dan estetika landskap merangkumi pelbagai jenis binaan yang
> mengintegrasikan reka bentuk seni bina dengan landskap semula jadi…`

This is **verbatim** the S04 VO in probe v0.1 `notesSlide4`. The Papan Tanda paragraph likewise matches
`notesSlide16` verbatim. **The probe's clone-from-source claim is now independently confirmed against
the module itself**, not just against its own documentation.

## 4. Images — RESOLVED by the PDF extract — `MEASURED_FACT`

**14 embedded images extracted** to `source-assets/`, covering **7 of 9** mapped screens.
The earlier "six screens have no figure" finding was an artefact of text extraction: only *captioned*
`Rajah` figures survive text export, and the module carries **10 further unnumbered photographs inside
specification tables**. See `B02_ASSET_MANIFEST.md`.

Only **S07 Kemudahan Awam** and **S08 Water Feature** genuinely have no image — confirmed by position
against their headings in the rendered PDF, not inferred.

### 4.1 Superseded — why the DOCX could not do this

The module contains figures in scope (`Rajah 23`–`26`, see `B02_ASSET_MANIFEST.md`), but **no image
file could be extracted.**

| Route | Outcome |
|---|---|
| `read_file_content` | returns text only — figures appear as captions, not image data |
| `download_file_content` | returns base64 of the **whole 16.8 MB** file ≈ 22 MB encoded — exceeds what a tool result can return |
| Attachment | failed three times |

This is now closed. `source-assets/` holds 14 JPEGs, 408 KB total, each with a recorded crop boundary,
dimensions and SHA-256.

## 5. Other evidence held

| Artifact | SHA-256 | Role |
|---|---|---|
| Visual sample v0.2 | `8d93e2ce…646a982b` | accepted treatment — **not modified by this gate** |
| Probe v0.1 | `24dcaa04…1d471c` | now **corroborated** against the module (§3.1) |
| Bariah review deck | `ee4f5479…8bb9e7` | SME intent |

Still absent: `packet_B02.json`, `asset_manifest.json`, the Tier-1 spec deck.

## 6. Toolchain

PyMuPDF 1.28.0 — used for all PDF work: folio reading, heading extraction, image inventory and
extraction with crop boundaries. Text extraction used the Drive representation plus local Python.
