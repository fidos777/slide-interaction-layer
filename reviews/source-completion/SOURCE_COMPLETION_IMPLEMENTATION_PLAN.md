# SOURCE_COMPLETION_IMPLEMENTATION_PLAN — K5 PL06 T3 B02

```
GATE STATUS: BLOCKED — awaiting the module PDF
```

This plan is complete and executable. It does not depend on source content — only on the source
arriving. See `SOURCE_ARTIFACT_INVENTORY.md` §1.2 for the blocker.

---

## 1. Target scope, as specified

| Section | Module pages | Physical PDF pages | Screens |
|---|---|---|---|
| **3.3 Struktur Taman** | 237–241 | ~256–260 | S04 base · S05–S08 children · S09 tick |
| **3.4 Perabot Taman** | 242–250 | ~261–269 | S10 base · S11–S15 children · S16 tick |

Module→physical offset is stated as **≈ +19** and will be **verified, not assumed** — step 2 confirms
it against printed folios before any page number is recorded.

## 2. Required screen mapping — as given

| Screen | Subject | Section |
|---|---|---|
| S05 | Struktur Persisir Air | 3.3 |
| S06 | Struktur Teduhan | 3.3 |
| S07 | Kemudahan Awam | 3.3 |
| S08 | Water Feature | 3.3 |
| S11 | Kerusi Taman | 3.4 |
| S12 | Papan Tanda | 3.4 |
| S13 | Tong Sampah | 3.4 |
| S14 | Drinking Fountain | 3.4 |
| S15 | BBQ pit | 3.4 |

This supersedes the earlier **provisional** ordering. Only `S12 = Papan Tanda` had been confirmed by
measurement; the other eight were inferred from label order and are now **directed**. Step 4 checks
each against its source heading and reports any mismatch rather than silently accepting.

## 3. Execution steps

### Step 1 — intake and custody
Hash the PDF (SHA-256, MD5, bytes), record page count, confirm it is text-bearing rather than scanned
images. If page text is absent, stop and report — OCR would make every proposition an inference.

### Step 2 — page-offset verification
Read printed folio numbers on ~10 sampled physical pages, derive the true module→physical offset, and
confirm 237 and 250 land where expected. **Record the measured offset.** Everything downstream keys off it.

### Step 3 — section boundary confirmation
Locate the literal headings `3.3` and `3.4` and their sub-numbered children. Record the exact heading
string and physical page for each. **This is where the repeated `3.4.1` numbering gets located and
quoted.**

### Step 4 — per-screen extraction *(the 9 mapped screens)*
For each, record exactly what the source says, and nothing more:

| Field | Rule |
|---|---|
| module page | measured |
| physical PDF page | measured |
| source heading | verbatim |
| **exact factual propositions** | verbatim or minimally-normalised; each traceable to a page |
| available figure / table | measured — **absence recorded as absence** |
| proposed asset ID | `K5PL06T03-B02-IMG-nn` only where a real figure exists |
| concise display draft | derived, subject to the accepted budget |
| full source-bound VO draft | derived, fuller than display |
| terminology treatment | italic lexicon + variant handling |
| source defects | quoted with page reference |
| confidence / status | `VERIFIED` / `PARTIAL` / `MISSING` |

### Step 5 — asset extraction *(bounded)*
Extract figures and tables in scope to `source-assets/`, named
`K5PL06T03-B02-IMG-nn__p<physical>.png`, with a manifest row each: page, caption, dimensions, hash,
bound screen. **Where a screen has no suitable figure, that is recorded and no visual is fabricated.**

Existing verified locators to reconcile against: `IMG-01` ms 237 (S04) and `IMG-05` ms 243 (S12). If
extraction disagrees with either, the disagreement is reported — the locators are not overwritten.

### Step 6 — defect register
Every defect quoted with page and surrounding text. The four pre-registered items in §4 are checked
first, then a sweep for others.

### Step 7 — display / VO drafting
Against the accepted budget: **split-STATE line box 5.1496 in → 41–45 chars/line**; the S12 body sits
at 10 lines against ~12.5. Display concise, VO fuller and source-bound, no narrator prefix, italic
lexicon applied. **Drafts only — nothing enters a PPTX at this gate.**

### Step 8 — coverage matrix
All 19 screens, including the four held open.

## 4. Pre-registered defects to verify — **reported, not yet observed**

Recorded from the request. **None has been located or quoted** — the PDF is absent.

| # | Item | To determine |
|---|---|---|
| D-1 | `Promenande` / `Promenade` variant | which spelling appears, where, how many times, which is intended; display and VO treatment |
| D-2 | repeated `3.4.1` numbering | which headings collide, whether it is a numbering slip or two genuine subsections; effect on the S11–S15 mapping |
| D-3 | English-origin term styling | which terms appear in English in scope, whether the module already styles them, whether the 3-term lexicon (`Water Feature`, `Drinking Fountain`, `BBQ pit`) needs extending |
| D-4 | `reka bentuk` / `rekabentuk` variants | which form dominates, whether both appear in scope, which to carry into display and VO |

Each becomes a `SOURCE_DEFECT_REGISTER.md` row **with a quotation and a page reference**, or is marked
not-found.

## 5. Screens held open

S02, S03, S18 and S19 stay `MISSING_SOURCE` unless separately supported by decision evidence.

- **S02 / S03** — decision slots `(K5, PL06, s02)` and `(K5, PL06, s03)` are **empty**; the current B02
  cast is not provable. The module may supply topic content but cannot supply a casting or reflection
  decision.
- **S18** — no quiz item, answer key or routing is constructed. If the module contains assessment
  material it will be **reported**, not converted into a quiz.
- **S19** — no closing content.

## 6. Constraints held throughout

| Constraint | Status |
|---|---|
| Do not edit the PowerPoint at this gate | held — no PPTX written |
| Do not modify the accepted visual sample | held — `8d93e2ce…` unchanged |
| Do not generate the source-bound PPTX yet | held |
| Do not unlock K5 | held |
| Do not issue canonical IDs | held |
| Do not fabricate a visual without a source image | held — `source-assets/` is empty by design |
| Do not fabricate pages, headings, propositions or defects | held — five deliverables left unpopulated |

## 7. Estimated shape of the work once unblocked

| Step | Nature |
|---|---|
| 1–3 intake, offset, boundaries | mechanical |
| 4 per-screen extraction × 9 | the bulk — reading and verbatim capture |
| 5 asset extraction | mechanical, bounded to scope |
| 6 defect register | 4 pre-registered + sweep |
| 7 display/VO drafting × 9 | judgement, against a fixed budget |
| 8 coverage matrix | roll-up |

Single pass, no iteration expected — the treatment geometry is already accepted and frozen at v0.2.
