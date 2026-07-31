# B02_PAGE_AND_NODE_MAP

```
STATUS: BLOCKED — NOT POPULATED
```

**No content has been entered in this document.** The module PDF
(`[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426_compressed.pdf`) is **absent from this
session** — see `SOURCE_ARTIFACT_INVENTORY.md` §1.2 for the searches run.

Every field below must be **read from the source**. Filling it from inference would produce a
source-completion record that is not source-bound, which is the one failure this gate exists to
prevent. The schema is fixed here so that intake is a single pass once the PDF arrives.

---

## Scope to be mapped

| Section | Module pages | Physical PDF pages (stated, **to verify**) |
|---|---|---|
| 3.3 Struktur Taman | 237–241 | ~256–260 |
| 3.4 Perabot Taman | 242–250 | ~261–269 |

Module→physical offset stated as ≈ **+19**. It will be **measured against printed folios**, not
assumed — the whole map keys off it.

## Schema — one row per source node

| module page | physical page | heading level | heading (verbatim) | node ID | bound screen | notes |
|---|---|---|---|---|---|---|
| *(pending source)* | | | | | | |

## Known verified anchors to reconcile against

| Anchor | Value | Source |
|---|---|---|
| S04 locator | `K5PL06T03-B02-IMG-01`, ms **237** | probe v0.1, measured |
| S12 locator | `K5PL06T03-B02-IMG-05`, ms **243** | probe v0.1, measured |

If extraction disagrees with either, the disagreement is **reported**; the measured locators are not
overwritten.

## Required screen mapping — as directed

| Screen | Subject | Section |
|---|---|---|
| S05 | Struktur Persisir Air | 3.3 Struktur Taman |
| S06 | Struktur Teduhan | 3.3 |
| S07 | Kemudahan Awam | 3.3 |
| S08 | Water Feature | 3.3 |
| S11 | Kerusi Taman | 3.4 Perabot Taman |
| S12 | Papan Tanda | 3.4 |
| S13 | Tong Sampah | 3.4 |
| S14 | Drinking Fountain | 3.4 |
| S15 | BBQ pit | 3.4 |

This supersedes the earlier provisional ordering, in which only `S12 = Papan Tanda` was confirmed by
measurement. Each assignment will be checked against its source heading and any mismatch reported.

## Must be resolved here

- **D-2 repeated `3.4.1` numbering** — which headings collide, and whether it is a numbering slip or
  two genuine subsections. This directly affects whether S11–S15 map cleanly onto 3.4's children.
