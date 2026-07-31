# DISPLAY_VO_DRAFT_MATRIX

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

## Schema — one row per mapped screen

| Screen | Source propositions | Display draft | VO draft | Terminology | Budget check | Confidence |
|---|---|---|---|---|---|---|
| *(pending source)* | | | | | | |

## Drafting rules — fixed by the accepted treatment

| Rule | Value |
|---|---|
| Display | concise, source-bound. **Never** exceeds the propositions in the source |
| VO | fuller than display, source-bound; carries framing the display omits |
| Coverage | every display proposition must appear in the VO; no proposition may be dropped from both |
| Narrator prefix | **none** — routine VO carries no `Hilmi:` |
| Italic lexicon | `Water Feature` · `Drinking Fountain` · `BBQ pit` — closed unless D-3 extends it |
| `BBQ pit` | source form, lowercase `p`, non-breaking space in display |
| Rumusan rules | S17 only; not applied to detail screens |

## Budget — measured, not assumed

| Family | Line box | Capacity @ 18 pt | Ceiling |
|---|---:|---:|---|
| split-STATE detail (S05–S08, S11–S15) | 5.1496 in (lvl 0) · 4.6496 in (lvl 1) | 41–45 · 37–40 ch/line | ~12.5 lines; S12 sits at **10** |
| full-width (S17) | 11.2167 in | 90–98 ch/line | ~7 lines |
| card label | 3.4202 in | 24–27 ch | **1 line**, `noAutofit` — overflows silently past 24 ch |

**The detail screens are the tight ones.** At 41–45 chars/line a draft overruns fast, and the accepted
S12 body already sits at 10 of ~12.5 lines. Drafts that do not fit are **cut**, not squeezed — the
budget is part of the accepted treatment, not a suggestion.

## The nine screens to draft

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

S12 is **already drafted and verified** — its display and VO come from probe v0.1 and are in the
accepted sample. It is the calibration reference for the other eight, not a screen to redraft.

## Not drafted at this gate

S02, S03, S18, S19 — held open. No scenario, reflection question, quiz item, answer key, routing or
closing content is drafted.
