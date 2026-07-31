# B02_ASSET_MANIFEST

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

## Extraction target

```
reviews/source-completion/source-assets/     EMPTY BY DESIGN
```

Empty is correct. There is no PDF to extract from, and per the standing instruction **no visual is
fabricated where the module provides no suitable image**.

## Schema — one row per extracted asset

| asset ID | physical page | module page | caption (verbatim) | type | px w×h | sha256 | bound screen | fidelity |
|---|---|---|---|---|---|---|---|---|
| *(pending source)* | | | | | | | | |

Naming: `K5PL06T03-B02-IMG-nn__p<physical>.png`

## Current asset position — `MEASURED_FACT`

**Zero B02 content images exist in any artifact held.** The complete media inventory across both
evidence packages is two checkmark SVGs. Every `Visual:` on every screen of the accepted sample is a
text placeholder. Locators exist for **2 of 19** screens; assets for **0 of 19**.

This gate is what closes that — for the screens where the module actually provides a figure.

## Rules at extraction

1. A screen with no suitable figure gets **no asset ID** and is recorded as having none.
2. Asset IDs must reference a real page object; none is minted speculatively.
3. `IMG-01` (ms 237) and `IMG-05` (ms 243) are **measured anchors** — extraction reconciles against
   them and reports disagreement rather than overwriting.
4. Extraction is bounded to module pages 237–250. Nothing outside scope is pulled.
