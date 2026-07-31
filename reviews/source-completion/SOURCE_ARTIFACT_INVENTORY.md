# SOURCE_ARTIFACT_INVENTORY — K5 PL06 T3 B02 source completion

```
GATE STATUS: SOURCE ACQUIRED — TEXT COMPLETE, IMAGES NOT EXTRACTABLE
```

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
| 3 | physical PDF pages ~256–269 | **DOCX has no fixed pagination** | **Physical page mapping is impossible.** Module pages are recoverable from the TOC; physical pages are a PDF property this file does not have |

**This is the authoritative `[PROOFREAD FINAL]` document**, so it is the correct source — but the
physical-page half of the requested mapping cannot be produced from it. If physical page numbers are
needed downstream, the PDF is still required.

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

## 4. Images — NOT extractable in this session — `MEASURED_FACT`

The module contains figures in scope (`Rajah 23`–`26`, see `B02_ASSET_MANIFEST.md`), but **no image
file could be extracted.**

| Route | Outcome |
|---|---|
| `read_file_content` | returns text only — figures appear as captions, not image data |
| `download_file_content` | returns base64 of the **whole 16.8 MB** file ≈ 22 MB encoded — exceeds what a tool result can return |
| Attachment | failed three times |

**`source-assets/` therefore remains empty**, and per the standing instruction no visual is fabricated
where none can be obtained. The manifest records which figures *exist*, their captions and their bound
screens — that is real, source-bound information — but the image binaries are still outstanding.

**To close:** the PDF (any route), or the four figures exported individually, or a smaller DOCX
containing only pages 237–250.

## 5. Other evidence held

| Artifact | SHA-256 | Role |
|---|---|---|
| Visual sample v0.2 | `8d93e2ce…646a982b` | accepted treatment — **not modified by this gate** |
| Probe v0.1 | `24dcaa04…1d471c` | now **corroborated** against the module (§3.1) |
| Bariah review deck | `ee4f5479…8bb9e7` | SME intent |

Still absent: `packet_B02.json`, `asset_manifest.json`, the Tier-1 spec deck.

## 6. Toolchain

PyMuPDF 1.28.0 installed (unused — no PDF arrived). Extraction was done with the Drive text
representation plus local Python. Pillow present.
