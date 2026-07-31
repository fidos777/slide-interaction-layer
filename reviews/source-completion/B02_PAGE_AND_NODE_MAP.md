# B02_PAGE_AND_NODE_MAP

Source: `[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx` (Drive `16j15Knt…bJ4`)

```
Module pages: MEASURED from TOC (section level) · ESTIMATED by interpolation (screen level)
Physical PDF pages: NOT DETERMINABLE — this is a DOCX with no fixed pagination
```

---

## 1. Section-level map — measured

| Node | Heading (verbatim) | Module page | Char offset | Status |
|---|---|---:|---:|---|
| 3.3 | `Struktur Taman` | **237** | 309,048 | ✅ measured (TOC) |
| 3.4 | `Perabot Taman` | **242** | 313,807 | ✅ measured (TOC) |
| 3.5 | `Infrastruktur` | 251 | 323,348 | boundary — out of scope |

Scope span: **14,300 characters over module pages 237–250**.

## 2. Screen-level map

Sub-headings are **not in the TOC**, so their module pages are **interpolated** from the measured
anchors at 1,021.4 chars/page. Marked `~` throughout — these are derived, not read off the page.

| Screen | Source heading (verbatim) | Module page | Char offset | Table | Figure |
|---|---|---|---:|---|---|
| **S05** | `Struktur Persisir Air (Promenande, Jeti, Dek, Boardwalk, footbridge)` | ~237 | 309,348 | ✅ 5 rows | **Rajah 23** |
| **S06** | `Struktur Teduhan` | ~239 | 310,618 | ✅ 5 rows | **Rajah 24** |
| **S07** | `Kemudahan Awam` | ~240 | 311,619 | ✅ 3 rows | — none |
| **S08** | `Water Feature (Fountain, Pond, Pool)` | ~240 | 312,573 | ✅ 3 rows | — none |
| **S11** | `Kerusi Taman` | ~242 | 314,102 | ✅ 3 rows | — none |
| **S12** | `Papan Tanda` | ~244 | 316,112 | ✅ 1 row | **Rajah 25 + 26** |
| **S13** | `Tong Sampah` | ~245 | 317,573 | ✅ 3 rows | — none |
| **S14** | `Drinking Fountain` | ~247 | 319,283 | ✅ 2 rows | — none |
| **S15** | `BBQ pit` | ~249 | 321,361 | ✅ 1 row | — none |

**All nine mapped screens exist in the source with a specification table. Only three have a figure.**

## 3. Directed mapping — verified against source headings

Every directed assignment matches a real heading, in source order. **No mismatch found.**

| Directed | Source heading | Verdict |
|---|---|---|
| S05 Struktur Persisir Air | `Struktur Persisir Air (…)` | ✅ |
| S06 Struktur Teduhan | `Struktur Teduhan` | ✅ |
| S07 Kemudahan Awam | `Kemudahan Awam` | ✅ |
| S08 Water Feature | `Water Feature (Fountain, Pond, Pool)` | ✅ |
| S11 Kerusi Taman | `Kerusi Taman` | ✅ |
| S12 Papan Tanda | `Papan Tanda` | ✅ *(previously the only measured one)* |
| S13 Tong Sampah | `Tong Sampah` | ✅ |
| S14 Drinking Fountain | `Drinking Fountain` | ✅ |
| S15 BBQ pit | `BBQ pit` | ✅ |

The earlier provisional ordering — inferred from S04 label order and the S17 furniture list — **was
correct on all eight unverified screens.** That inference is now retired in favour of measurement.

## 4. Reconciliation with the existing verified locators

| Locator | Held | Source position | Verdict |
|---|---|---|---|
| `IMG-01`, ms **237** (S04) | probe v0.1 | 3.3 opens at p237 ✅ | page confirmed. **But the first figure in 3.3 is `Rajah 23` (Boardwalk), which sits at the *end* of S05, not at the section opener.** What `IMG-01` depicts is not resolvable from text |
| `IMG-05`, ms **243** (S12) | probe v0.1 | Papan Tanda interpolates to **~244** | ±1 page of the interpolation — consistent. Papan Tanda has **two** figures (`Rajah 25`, `26`) |

**Neither locator is overwritten.** `IMG-05`/243 stands; the ~244 estimate is within interpolation
error and is not evidence against it.

## 5. What could not be mapped

| Item | Why |
|---|---|
| Physical PDF pages ~256–269 | DOCX has no fixed pagination |
| Per-screen module pages, **measured** | sub-headings absent from the TOC; interpolation used |
| `IMG-01` subject | figure captions do not identify it |
