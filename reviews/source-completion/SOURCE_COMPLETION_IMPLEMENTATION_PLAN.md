# SOURCE_COMPLETION_IMPLEMENTATION_PLAN — K5 PL06 T3 B02

```
GATE STATUS: TEXT COMPLETE (13/19) · ASSETS OUTSTANDING (0/19)
No PPTX generated. Accepted visual sample unmodified.
```

---

## 1. What this gate achieved

| Step | Result |
|---|---|
| Source acquired | via Google Drive after three failed attachments — **DOCX, 16.8 MB** |
| Scope confirmed | module pages **237–250**, exactly as specified (TOC-measured) |
| Sections mapped | 3.3 @ p237, 3.4 @ p242, boundary 3.5 @ p251 |
| Screens mapped | **9 of 9**, every directed assignment matching a real heading, **no mismatch** |
| Text extracted | all nine, plus the 3.4 section intro for S10 |
| Figures identified | 4 (`Rajah 23`–`26`) covering 3 screens; **6 screens have none** |
| Defects | D-1 confirmed · D-2 **not confirmed as stated** · D-3 confirmed and much larger than expected · D-4 confirmed · **D-5 new** |
| Drafts | display + VO for all 8 outstanding screens, all within budget |
| Probe corroborated | S04 and S12 source text **matches probe v0.1 verbatim** |

## 2. What remains

| # | Gap | Blocking | Needs |
|---|---|---|---|
| **G-1** | **Figure binaries** for S05, S06, S12 | asset binding | PDF · 4 exported images · or a p237–250 DOCX |
| **G-2** | **Six screens have no source figure** | visual regions on S07, S08, S11, S13, S14, S15 | **a decision, not a file** — see §5 |
| **G-3** | D-3 lexicon scope — 42 terms vs a 3-term list | italic treatment | a human cut-line — see §4 |
| **G-4** | D-2 numbering | nothing downstream | rendered document |
| **G-5** | S02 / S03 / S18 / S19 | 4 screens | ratified decisions and quiz source — **not** the module |
| **G-6** | Measured per-screen module pages | precision only | rendered pagination |

**Only G-1 and G-2 stand between here and a source-bound deck.** G-3 affects styling, not content.

## 3. Next steps, in order

### Step 1 — close G-1
Obtain the four figures. Extract to `source-assets/` as
`K5PL06T03-B02-IMG-<rajah>__p<module>.png`, hash each, complete the manifest.

### Step 2 — resolve G-2 *(decision required)*
Six of nine screens have no module figure. Three options, none taken:

| Option | Effect |
|---|---|
| **A** — visual region carries the **specification table** | source-bound, real content, no fabrication. Table is dense — needs a display-budget check per screen |
| **B** — visual region stays a `SOURCE PENDING` placeholder | honest, but six of nine detail screens ship with an empty panel |
| **C** — commission photography | out of scope here; a production request |

**Recommended: A**, with B as the fallback where a table will not fit. Not decided.

### Step 3 — resolve G-3 *(decision required)*
Pick the lexicon cut-line: Tier 1 (12 terms) · Tier 1+2 (30) · all (42). **Tier 1 recommended** — it
keeps italic on learner-facing type names and out of specification tables. Not decided.

### Step 4 — build the source-bound deck
Only after 1–3. Apply the **accepted v0.2 treatment geometry unchanged**; fill display and VO from
`DISPLAY_VO_DRAFT_MATRIX.md`; bind assets; keep S02/S03/S18/S19 as `SOURCE PENDING`.
Output would be `…SOURCE_BOUND_v0_1.pptx` — a **new artifact**, not an edit of the accepted sample.

### Step 5 — re-run checks
Package + rule suite, plus new source-fidelity checks: every display proposition traceable to a page;
`Promenade` not `Promenande`; `reka bentuk` not `rekabentuk`; `BBQ pit` lowercase.

## 4. Decisions needed before Step 4

| # | Decision | Recommendation |
|---|---|---|
| **DEC-1** | Visual region for the six figure-less screens | **Option A** — specification table |
| **DEC-2** | Italic lexicon scope | **Tier 1**, 12 terms |
| **DEC-3** | `Promenande` → `Promenade` in display/VO | **yes** — heading typo, table is correct |
| **DEC-4** | `rekabentuk` → `reka bentuk` | **yes** — 131:8 majority |
| **DEC-5** | Report D-5 heading defect to the module owner | **yes** — affects their TOC, not our deck |

All five are recommendations. None is applied.

## 5. Constraints held

| Constraint | Status |
|---|---|
| Do not generate the source-bound PPTX yet | ✅ none generated |
| Do not modify the accepted visual sample | ✅ `8d93e2ce…646a982b` unchanged |
| Do not unlock K5 | ✅ |
| Do not issue canonical IDs | ✅ proposed asset IDs key to the module's own `Rajah` numbering, and are proposals |
| Do not fabricate a visual where the module provides none | ✅ six screens recorded as having none; `source-assets/` empty |
| Keep S02, S03, S18, S19 open | ✅ all four held |

## 6. Honest position on the source

The DOCX is the authoritative `[PROOFREAD FINAL]` document and its **text is fully sufficient** for
nine screens — better than the PDF would have been for extraction. Two things it cannot give:

1. **Physical PDF pages** — it has no fixed pagination. The requested ~256–269 mapping is not
   producible from this file, and per-screen module pages are interpolated, not read.
2. **Images** — reachable only as base64 of the whole 16.8 MB file, which exceeds a returnable result.

Both are file-format limits, not source defects.
