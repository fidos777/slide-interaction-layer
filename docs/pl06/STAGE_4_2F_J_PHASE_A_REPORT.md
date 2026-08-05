# STAGE 4.2F-J — PHASE A: returned-authority ingestion

```
PASS                 = PHASE_A_RETURNED_AUTHORITY_INGESTION + OWNER_TENSION_DISPOSITION
ARTIFACT             = docs/pl06/authority/K5_Pengesahan_ID_Watak_Dialog_Rumusan_v0_2_vBariah.docx
SHA256               = a4775daaacb551d7db44851f3cd8cd888fbdf47637d79c572dc172ff8f9de0b3
GATES                = 108 / 108
MUTATION_FIXTURES    = 52 / 52   (49 detect, 3 positive controls)
REFUSAL_CASES        = 3 / 3
COMMITTED            = YES — Phase A checkpoint, no PPTX generated
PROJECT_STATE        = FINAL_TENSION_CLEARANCE_GRANTED
```

> **Revision 3 — the largest correction in this pass.** **A6 and A7 exist.** They are
> decisions of `K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2_vBariah.docx`, dated 4 August
> 2026, authored by Bariah Ahmad, ingested at Stage 4.2F-G into `docs/pl06/k5_policy/` and
> gated by a 93-gate suite. My warrant audit searched the returned document's Section A and
> the rule-portability matrix, did not search that directory, and reported both as resolving
> to nothing. Findings **WA-01, WA-02, WA-03 and WA-05 are withdrawn**. Only WA-04 and WA-06
> survive as genuine warrant findings. WA-07 records the method defect; see §3 and §14.
>
> **Revision 2.** The owner's human review under E2 corrected this pass in seven places. Three
> of them are corrections to *my* Phase A findings, not to the underlying rules: WA-03, WA-04
> and WA-06 all turned out to be rules the authority had already confirmed at **D3 rules 4 and
> 5**, which live in a table cell rather than in body text and which the first pass did not
> read. The downgrades to `PROPOSED_NOT_APPROVED` are withdrawn. See §3 and §12.

Nothing in this pass approves anything. No unit is `INSTRUCTIONALLY_APPROVED`, no quiz item or
answer key is marked approved, no PPTX was emitted, and B03 and T04 were not regenerated.

---

## 1. The artifact

Verified at the earlier checkpoint and not re-verified here: filename, byte length, MD5,
SHA-256, zero tracked changes, zero comment parts, the 41 / 31 option-mark census, and
`lastModifiedBy = Bariah Ahmad`.

| Property | Value |
|---|---|
| bytes | 49,045 |
| MD5 | `4e4f2bdd14d92f222ff35d7745c94d3d` |
| signature objects | **0** — the artifact carries no cryptographic or digital signature of any kind |
| identity basis | byte hash controlling; document metadata supporting |
| renderer used | LibreOffice Writer 24.2.7.2 420(Build:2) |
| render page size | A4 210×297 mm |
| font substitutions | Calibri and Calibri Light → Carlito; Cambria → Caladea (metric-compatible) |
| pages rendered | **16**, against 14 expected |

The 16-page render is an observation from a substitute layout engine, not a property of the
artifact, and it does not block ingestion because the controlling byte identity matches.
**No evidence available here establishes that the expected 14 pages came from Microsoft Word,
and that claim is not made.**

Marks reconcile: 23 in Sections A–F across 17 option blocks, plus 18 in Section G, = 41
checked. Section G's own instruction reads *"Ringkasan ini diisi selepas Bahagian A hingga F
dilengkapkan."*

---

## 2. Crosswalk correction — C5

C5 was previously read as an independent generator-contract rule. It is not.

| Field | Value |
|---|---|
| authority_record_id | `AR-C5` |
| source decision block | C5 |
| selected option | **none — C5 carries no option block anywhere in Sections A–F** |
| authority from A–F? | **no** |
| Section G merely reconciles? | no |
| Section G is the only explicit confirmation? | **yes** |
| scope | `B03_SAHAJA` |
| resulting status | `WRITTEN_CONFIRMED` |
| confirmation path | `SECTION_G_ONLY` |

C5 is a worked exhibit showing how the C4 formula lands on B03 — two speakers, Alya opens by
asking whether the work may proceed, Encik Rahman answers with the document-check and control
principle, five lines. Its own text says *"Susunan ini khusus untuk B03. Unit lain akan
mengikut formula C4…"*, and its only explicit confirmation is the Section G row *"Penerapan
formula pada B03 (C5) | B03 sahaja — kandungan unit"*.

So it is a **B03 content implementation record derived from C4, confirmed only through
Section G** — neither a pure Section-G reconciliation of an A–F decision, nor a generator
contract in its own right.

**Corrected representation.** The first pass minted a new status,
`WRITTEN_CONFIRMED_VIA_SECTION_G_ONLY`, to carry this. That was wrong: minting a status per
confirmation route grows the enum without bound and turns every membership test into a place
to get it wrong — the exact failure mode that has already bitten this project twice on
substring matching. C5 now carries the existing `WRITTEN_CONFIRMED` status, and HOW it was
confirmed is a separate typed field, `confirmation_path`. The status enum is back to seven
members and pinned by `THE_STATUS_ENUM_IS_THE_DECLARED_ONE`. Gates
`A_SECTION_G_ONLY_RECORD_IS_NOT_COUNTED_AS_AN_A_TO_F_DECISION`,
`THE_NON_DEFAULT_CONFIRMATION_PATHS_ARE_THE_DECLARED_ONES` and
`EXACTLY_ONE_RECORD_IS_CONFIRMED_BY_SECTION_G_ALONE` hold the distinction; fixture PL-45
promotes C5 to a normal A-to-F decision and must be caught.

A1 is recorded as `ASSERTED_PRIOR_BARIAH_DECISION_REPEATED_IN_RETURNED_DOCUMENT`: it carries
no option mark and has no Section G row, and it attributes the cast to *"Keputusan Bariah
T04"*. The full 22-record crosswalk is in `packets/PL06_AUTHORITY_CROSSWALK_v0_1.md`.

---

## 3. Warrant audit — six findings, in both directions

The historical A7 audit was the entry point and it found more than A7. **A warrant audit can
fail in two directions**, and the first revision of this report only looked for one of them.

| Finding | Rules | Prior citation | Verdict | Repair | Value changed |
|---|---|---|---|---|---|
| WA-01 | `quiz.mcq_count`, `quiz.multiple_response_count`, `quiz.pass_percent` | `A7` | **WITHDRAWN** — citation valid | re-cited to A7 in the registered Kelompok 0 artifact; re-confirmed by F2(a) | **no** |
| WA-02 | `rumusan.internal_beats` | `A6 as amended…` | **WITHDRAWN** — citation valid | re-cited to A6; D3 rule 1 supersedes the LABEL DISPLAY only | **no** |
| WA-03 | `rumusan.support_visual_required` | `A6` | **WITHDRAWN** — citation valid; A6 requires the visual outright | re-cited to A6, re-confirmed by D3 rule 5 | **no** |
| WA-04 | `rumusan.forbidden_phrase` | `written course-wide rule` | **STANDS** — no locus was ever named | re-cited to D3 rule 4, `WRITTEN_CONFIRMED` | **no** |
| WA-05 | `quiz.answer_key_approval` | `A7 authorises composition only` | **WITHDRAWN** — A7 genuinely covers composition only | re-cited to A7 scope with F2(b) | **no** |
| WA-06 | `visual_direction.suits_unit_topic` | `Firdaus proposed contract` | **STANDS** — under-claimed a rule the authority had confirmed | re-cited to D3 rule 5, raised to `WRITTEN_CONFIRMED` | **no** |
| WA-07 | the audit method itself | — | the method declared a citation nonexistent on an incomplete index | the Kelompok 0 ingestion is now a registered artifact | **no** |

**A6 and A7 exist.** Both are decisions of `K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2_vBariah.docx`,
dated 4 August 2026, authored by Bariah Ahmad, ingested at Stage 4.2F-G into
`docs/pl06/k5_policy/` and gated by `K5_BARIAH_POLICY_QA_v1` (93 gates). Revision 1 of this
report asserted that neither existed; that assertion is withdrawn in full. §14 carries the
evidence and the corrected verdicts.

The figures 4 MCQ + 1 MR at 60 percent were **already** settled by A7 on 4 August, including
A7's own note that it resolves the `RP-009` / `RP-010` VERIFY flags. F2(a) on 5 August is a
re-confirmation, not the first warrant. The F2 preamble sentence *"Angka ini belum ada dalam
mana-mana dokumen keputusan"* is **CAIR's own wording in the request form**, not Bariah's, and
it was factually wrong when written.

### The three findings that pointed the other way

D3's five rules live in a **table cell**, not in body text. The first pass read the narrative
sentence beside the table — *"Peraturan 5 sengaja tidak menetapkan bentuk visual"* — and
concluded no visual was required course-wide. It read the sentence correctly and the rule not
at all. The rules read, verbatim:

> **4.** Frasa "Unit ini" tidak boleh digunakan.
> **5.** Rumusan disertai satu visual sokongan yang sesuai dengan topik unit berkenaan.

Rule 4 is the forbidden phrase. Rule 5 requires a supporting visual **and** requires it to suit
the unit's topic — which is a third rule, `visual_direction.suits_unit_topic`, that had been
carried as an owner proposal. The note beside rule 5 does not remove the requirement; it says
the **form** is set per unit, which is now recorded separately as `rumusan.visual_form_not_fixed`.

All three downgrades are withdrawn. Recording a rule as a proposal that nobody agreed to, when
the authority confirmed it in writing, misstates what she said just as surely as claiming a
warrant that does not exist. Fixture **PL-21** now reproduces this direction: it demotes a
confirmed rule to a proposal and must be caught.

No rule VALUE was changed by any repair, in either direction.

---

## 4. The citation gate

`EVERY_WRITTEN_CONFIRMED_RULE_CITES_A_DATED_ARTIFACT_AND_NAMED_AUTHORITY`. A record must name
an artifact in the registry, a locus inside it, a human on the declared roster, and a date
that agrees with the registry. All four, separately.

**Population reconciliation.** The first revision reported "48 of 51", which leaves three rules
unaccounted for and gives a reader no way to tell whether they were exempt or simply missed.
Three gates now close it:

| Gate | What it holds |
|---|---|
| `THE_CITATION_POPULATION_ACCOUNTS_FOR_EVERY_RULE` | required + exempt = total, with an empty intersection |
| `THE_CITATION_EXEMPT_RULES_ARE_THE_DECLARED_ONES` | the exempt set is named by the suite, not inferred |
| `NO_RULE_CARRIES_A_STATUS_IN_NEITHER_SET` | no status falls outside both sets (fixture PL-44) |

After the D3 corrections the arithmetic is **54 required + 0 exempt = 54 total**. The count rose
from 51 because three records were added (the paraphrase contract, the T02-B02 source-scope
verification and the ROW-058 disposition), and the exempt set emptied because the three
`PROPOSED_NOT_APPROVED` rules turned out to be confirmed at D3.

Supporting gates: artifact bytes and hashes are re-read from disk; the returned artifact is
compared against the verification checkpoint; the declaration is checked for claiming a
signature it does not have; every warrant-audit repair is checked to have landed on the rule
it names.

Fixtures:

| Fixture | Kind | What it does |
|---|---|---|
| PL-16 | **positive control** | adds a well-formed `WRITTEN_CONFIRMED` rule with a complete citation — the gate must NOT trip |
| PL-17 | negative | the A7 defect reintroduced verbatim: a confirmed rule citing a locus that resolves to no artifact |
| PL-18 | negative | real artifact and locus, nobody named |
| PL-19 | **partial-citation collision** | every field populated, so any "is the field non-empty" check passes — but the named authority is the label `SEE_ABOVE` and the date disagrees with the registry |

Also new: `all_rules()` now walks lists as well as dicts. The three approved-character records
live inside a list and were invisible to every status gate before this pass.

---

## 5. What the returned document settled

| Locus | Effect |
|---|---|
| A1 | cast stated: Alya, Encik Rahman, Hilmi. Haziq and Encik Roslan recorded as replaced. Closes STOP-006 and SRC-ANOM-003, with the residual noted above. |
| A2 / A3 / B5 | character selection contract, no per-PL roster now, role inventory is a reference |
| C2 | three procedural claims confirmed; Encik Rahman must not be depicted approving structural changes or confirming boundaries |
| C3 / C4 / C5 | B03 dialogue accepted as-is; C4 is the K5 default formula; C5 is the B03 exhibit |
| D1 / D2 / D3 / D4 | B03 Rumusan copy accepted; labels never shown to the trainee; the five Rumusan rules; one whole-site visual for B03 |
| E1 | **S02 must be a dialogue for every K5 unit** — supersedes AR-06 |
| E2 | tension required, and its verification is explicitly human, not automated |
| F1 / F6 / F7 | no per-unit pre-review; B03 accepted as sample *conditionally*; responsibility split written down |
| F2 | 4 MCQ + 1 MR at 60 %; keys reviewed inside the unit's own storyboard slot |
| F3 / F4 | four named treatments with a definition of symmetry; B03's two screens fixed |
| F5 | **3 panels is the production Lampiran density** |

Excluded by the document itself: *"Soalan kuiz sebenar dan kunci jawapan setiap unit."*
Nothing here approves a quiz item or a key.

### C2 claim 1

`"Kedudukan pagar perlu disemak dengan Pelan Ukur Sempadan."` was marked but, unlike claims 2
and 3, carries **no annotation**. The controlled-source search found it supported:
`T03B03-ROW-048` — *"Jajaran pagar mesti ditanda mengikut Pelan Ukur Sempadan untuk
mengelakkan isu pencerobohan tanah."* — under heading `T03B03-ROW-047` *"Penjajaran Sempadan"*.
Recorded as `SOURCE_SUPPORTED_NOT_VERBATIM`: the source supports it, the paraphrase from
*"ditanda mengikut"* to *"disemak dengan"* is ours, not hers.

---

## 6. Defects found and repaired in this pass

**Beat label moved rather than removed.** The scope beat's learner-facing copy read
`"Skop: …"`. D3 rule 1 requires the copy to flow *without* the small headings and D2 says the
labels are not shown to the trainee — an inline prefix is that label, moved. Copy now flows
(`"Kerja ini merangkumi …"`). Gates `NO_RUMUSAN_BEAT_NAME_SURVIVES_AS_AN_INLINE_PREFIX` and
`EVERY_DECLARED_SUBTOPIC_APPEARS_IN_THE_SCOPE_COPY_ITSELF`; fixture PL-24.

**Analyst notes were being spoken by the cast.** For the four units with a committed analysis,
the dialogue line was the analyst's `statement` field — English-mixed commentary written to
explain why a row matters (*"Jajaran pagar mengikut Pelan Ukur Sempadan — a land-encroachment
exposure."*). It cited the right row and said something the row does not say. Lines are now the
module's own text; the analyst note is kept beside the anchor as the reason the row was chosen.
Gate `EVERY_SOURCE_BACKED_DIALOGUE_LINE_IS_TEXT_FROM_THE_ROW_IT_CITES` reads the extractors;
fixture PL-35.

**Anchors that did not contain their own marker.** A tension anchor took the row's *first*
sentence while the keyword that classified it sat two sentences later, producing anchors
labelled OBLIGATION whose text carried no obligation. The anchor now takes the sentence that
carries the marker.

**Two slots called anchored with no anchor.** `QUIZ_ANCHORED_SLOT` means the row is chosen and
only the wording is missing. Two slots had no anchor row at all. New state
`QUIZ_UNANCHORED_SLOT`; gates `NO_SLOT_CALLED_ANCHORED_LACKS_AN_ANCHOR_ROW` and
`EVERY_INCOMPLETE_SLOT_IS_COUNTED_IN_EXACTLY_ONE_STATE`.

**Self-referential oracle, occurrence #13 — in a gate written during this pass.**
`EVERY_UNIT_CLAIMING_ANALYSIS_COMPLETE_SATISFIES_THE_CONTRACT` took its population from the
model's own completeness flag, which the model computes *as* the absence of contract defects.
The gate was vacuous by construction and could never fail. Fixture PL-31 caught it, not
reading. Replaced by `THE_FOUR_DECLARED_ANALYSIS_UNITS_SATISFY_THE_CONTRACT`, whose population
is the suite's own list of four units.

---

## 7. Reconciliations

**Role instances — 27 vs 28.** The canonical figure is **28**, and it reconciles four
independent ways: the audit list length, the sum of the three classification counts
(11 REUSE_ALYA + 8 REUSE_ENCIK_RAHMAN + 9 SPEAKER_NOT_REQUIRED), the sum by `role_id`
(11 + 8 + 4 + 3 + 2), and the sum of the per-unit counts. Eleven of the twelve active units
carry role markers; **K5-PL06-T02-B02 carries none**, and it is named rather than absorbed —
which is where a count of 27 comes from if the empty unit is dropped instead of recorded.
Gates: `THE_ROLE_INSTANCE_TOTAL_RECONCILES_THREE_INDEPENDENT_WAYS`,
`THE_PER_UNIT_ROLE_COUNTS_ARE_THE_DECLARED_ONES` (fixture PL-27 moves an instance between
units while leaving the headline total unchanged), `A_UNIT_WITH_NO_ROLE_MARKER_IS_NAMED_NOT_ABSORBED`.

**14 Storyboards and 13 Lampiran, derived.** `derived_package_shape()` counts the unit roll and
subtracts the profiles that declare no Lampiran, reaching the totals a different way from the
declaration so the two can disagree and be caught. Gates
`THE_PACKAGE_SHAPE_IS_DERIVED_FROM_THE_ROLL_NOT_ASSERTED`,
`THE_DERIVED_SHAPE_AGREES_WITH_THE_AUTHORITY_DECLARATION`,
`EXACTLY_ONE_UNIT_CARRIES_NO_LAMPIRAN_AND_IT_IS_NAMED`,
`PRIMARY_PPTX_TOTAL_IS_STORYBOARDS_PLUS_LAMPIRAN`; fixture PL-28.

---

## 8. F5 — the density sweep

`PRODUCTION_PANEL_DENSITY` is now read from the declaration (3). `CALIBRATION_DENSITIES`
remains `(2, 3)`. **Nothing was deleted**: the 2-panel PPTX, both preview sets and the
regression gates that prove only the layout differs between the densities are all retained, and
gate `THE_CALIBRATION_DENSITIES_ARE_RETAINED_NOT_DELETED` (fixture PL-30) fails if the 2-panel
evidence is dropped. `THE_PRODUCTION_DENSITY_IS_ONE_OF_THE_DENSITIES_ACTUALLY_TESTED` stops the
production format being set to a density nobody built.

The calibration QA suite was **not re-run**, because running it rebuilds the B03 PPTX and this
pass is prohibited from emitting an active-unit PPTX. The sweep is verified instead by the
packet suite, which imports the builder module and reads the constants without emitting.

---

## 9. `SOURCE_ANALYSIS_COMPLETE` — from membership test to contract

It used to mean "is this unit a key in `UNIT_ANALYSIS`", which proves a dict key exists. The
contract is now the nine fields the four completed analyses actually carry, with floors and a
requirement that every item traces to a row of its own unit. All four still pass.

**A floor rewards invention.** An analyst who looked for ambiguities and honestly found none
could not pass a floor of two without making some up. A field may therefore be recorded as
`{"assessed": "ASSESSED_NO_FINDINGS", "basis": …}`, which clears the floor. **Absence never
does** — and an unexplained "nothing here" is indistinguishable from not having looked, so the
basis is mandatory. Fixture **PL-42** supplies `ASSESSED_NO_FINDINGS` with an empty basis and
must be caught; fixture **PL-43** is the positive control, supplying it with a real basis, and
must NOT trip.

| Field | Floor | Every item traced by |
|---|---|---|
| `mandatory_propositions` | 8 | `rows` |
| `terminology` | 6 | `rows` |
| `compliance_sensitive` | 2 | `rows` |
| `assessment` | exactly 5 | `correct_rows` |
| `visual_subjects` | 3 | `rows` |
| `rumusan_beats` | 3 | — |
| `ambiguities` | 2 | `rows` |
| `pattern` | primary + secondary + reason | — |
| `dialogue` | verdict + reason | — |

The gap matrix (`packets/PL06_ANALYSIS_GAP_MATRIX_v0_1.md`) applies it to the eight ROWS_ONLY
units and reports, per field, how much evidence the controlled rows already carry against the
floor. **Nothing is authored.** `ambiguities` is short everywhere by construction — nothing
mechanical can find the places a source is genuinely unclear. `compliance_sensitive` is short
in T01-B03, T02-B01, T02-B02 and T03-B05, and `mandatory_propositions` in T01-B03 and T02-B02.
A short field's verdict now reads `EVIDENCE_SHORT_ASSESS_THEN_AUTHOR_OR_RECORD_NO_FINDINGS`,
because "short" is a prompt to look, not a demand to produce.

`dialogue.verdict` in the committed analyses is now superseded evidence: E1 makes S02 a
dialogue regardless of whether AR-06 would have justified one. The committed records were not
rewritten; the supersession is recorded as `SUP-03`.

---

## 10. Exception report, reclassified

```
AUTHORING_TODO                   = 10
OWNER_DEFAULT_DECISION           =  8
INTERNAL_REVIEW                  =  3
BARIAH_EXCEPTION                 =  0
CLOSED_BY_THE_RETURNED_AUTHORITY =  7
```

F7 wrote the split down, so items that used to be escalated because nobody owned them are now
owned. F3 closes the treatment default, F5 the density, D3 the Rumusan rules, F1 the per-unit
pre-review, A1 the cast, D4(b) the B03 visual, and the document's arrival closes the blanket
"awaiting the returned document" exception.

**The three tension records are not Bariah exceptions.** The first revision filed them as such,
which was wrong under F7: the owner's human review under E2 is the review E2 asks for, and all
three were disposed of internally.

| Unit | Class |
|---|---|
| K5-PL06-T01-B03 | `INTERNAL_HUMAN_AUTHORING_REVIEW` |
| K5-PL06-T02-B01 | `CLOSED_BY_FIRDAUS_HUMAN_REVIEW` |
| K5-PL06-T02-B02 | `INTERNAL_SOURCE_SCOPE_REVIEW` |

`BARIAH_EXCEPTION` is now **0**. Escalation is reserved for a source conflict, a real technical
ambiguity, an unsupportable claim, or a need for a character with different authority, licence
or competence — and gate `NO_TENSION_DISPOSITION_IS_ESCALATED_WITHOUT_A_NAMED_TRIGGER` requires
an escalation to name which one.

---

## 11. The paraphrase contract and the three re-authored dialogues

The gate `EVERY_SOURCE_BACKED_DIALOGUE_LINE_IS_TEXT_FROM_THE_ROW_IT_CITES` was right about the
defect it caught and wrong as a rule. E1 asks for a conversation and E2 rejects "penerangan
panjang yang dibahagikan antara dua nama" — neither is reachable if every line must be a
verbatim substring of a source row. The authority declaration now carries a paraphrase
contract with three line classes and five limits, and seven gates enforce it:

| Line class | Burden |
|---|---|
| `SOURCE_VERBATIM` | the line must be text from a row it cites |
| `CONTROLLED_PARAPHRASE` | must cite rows, must name the row it paraphrases, and must not introduce an obligation, prohibition, approval or legal duty its cited rows do not carry |
| `CAIR_STRUCTURAL_FRAME` | makes no claim, so carries no source burden — but may name only rows of its own unit |

`NO_CONTROLLED_PARAPHRASE_ESCALATES_BEYOND_ITS_SOURCE` compares each paraphrase against the raw
text of the rows it cites for a declared marker list (*mesti, wajib, hendaklah, dilarang, tidak
dibenarkan, diluluskan, kelulusan, mandatori, undang-undang, sah di sisi*). Fixture **PL-37**
rewrites a line to claim a legal duty its row does not carry.

The three dialogues are authored in the controlled model, not patched into an artifact. Full
copy, line classes, row citations and the paraphrase source text are in
`packets/PL06_DIALOGUE_TENSION_REVIEW_v0_1.md`.

**T02-B02 source and subtopic verification.** `ROW-051` sits under `HEADING_3` *Sub-soil
drainage* (`ROW-050`) inside the unit's anchor-frozen slice (paragraphs 4340–4463, module pages
215–225) bound to declared subtopic *2.3 Kerja-Kerja berkaitan dengan Mekanikal & Elektrikal
(M&E)*. **Mapping valid.** Recorded anomaly: the declared subtopic label names M&E while the
components in the slice are Swale, Sub-soil drainage and Retaining Wall. Body-anchor precedence
governs extraction, so the row is in scope; the label does not describe the content. Recorded,
not silently corrected.

**ROW-058 disposition — excluded.** Three of the four conditions fail: it sits under its own
`HEADING_3` *Retaining Wall* parallel to Sub-soil drainage rather than beneath it; a retaining
wall answers a different question from surface-versus-subsurface drainage; and no justification
for its relevance to the same tension is available from the controlled rows. Only "separate
source trace" is met. It stays in the unit's row inventory for a future separate screen. Gate
`THE_EXCLUDED_ROW_IS_NOT_CITED_IN_THE_T02B02_DIALOGUE`; fixture **PL-41** puts it back.

---

## 12. Corrections to revision 1 of this report

| # | What revision 1 said | Correction |
|---|---|---|
| 1 | `rumusan.forbidden_phrase` downgraded to `PROPOSED_NOT_APPROVED` | D3 rule 4 confirms it verbatim; restored to `WRITTEN_CONFIRMED` |
| 2 | `rumusan.support_visual_required` downgraded | D3 rule 5 confirms it verbatim; restored |
| 3 | `visual_direction.suits_unit_topic` carried as an owner proposal | D3 rule 5 confirms it; raised (WA-06) |
| 4 | citation gate reported "48 of 51" | reconciled: 54 required + 0 exempt = 54, with the exempt set named and gated |
| 5 | C5 given a new status `WRITTEN_CONFIRMED_VIA_SECTION_G_ONLY` | existing enum + typed `confirmation_path` |
| 6 | `SOURCE_ANALYSIS_COMPLETE` floors could only be met by producing findings | `ASSESSED_NO_FINDINGS` with a mandatory basis clears a floor |
| 7 | dialogue lines required to be verbatim source text | controlled paraphrase permitted; escalation beyond source forbidden |
| 8 | the three tension records filed as `BARIAH_EXCEPTION` | internal review classes; `BARIAH_EXCEPTION` = 0 |

Items 1–3 are the same mistake: I searched for a warrant, did not find it in body text, and
downgraded rather than reading the rule list in the table. The correction direction matters —
under-claiming an authority's decision misstates what she said just as much as over-claiming.

---

## 14. Revision 3 — A6 / A7, RP-007 and the authority boundary

### A6 and A7 exist

| | |
|---|---|
| document | `K5_Pakej_Keputusan_Corak_Bariah_Kelompok0_v1_2_vBariah.docx` |
| sha256 | `d22f6315a9bdec2c00d376aee710aacb301d97b2587ca82ee2ce0adcb8d964ce` (33,406 B) |
| date | 4 August 2026 · Bariah Ahmad · 17 declared decisions, 16 approved |
| ingested | Stage 4.2F-G → `docs/pl06/k5_policy/`, gated by `K5_BARIAH_POLICY_QA_v1` (93/93) |

**A7 verbatim effect:** *"Default K5 quiz is 4 MCQ + 1 Multiple Response with a 60 percent pass
mark"*, with its own note recording that it settles the RP-009 / RP-010 VERIFY flags.
**A6 verbatim amendment:** *"Terima struktur tiga-beat (Kepentingan / Skop dan Isi Utama /
Manfaat)… Rumusan sepatutnya mempunyai visual sokongan… Visual adalah elemen standard
Rumusan."*

Corrected verdicts:

| Finding | Revision 1/2 said | Revision 3 |
|---|---|---|
| WA-01 | A7 resolves to nothing | **withdrawn** — citation valid; re-confirmed by F2(a) |
| WA-02 | A6 resolves to nothing | **withdrawn** — citation valid; D3 rule 1 supersedes the LABEL DISPLAY only |
| WA-03 | A6 phantom, rule downgraded then re-cited to D3 r5 | **withdrawn twice** — A6 requires the visual outright |
| WA-05 | A7 citation unwarranted | **withdrawn** — A7 genuinely covers composition only |
| WA-04 | citation resolved to nothing | **stands** — no locus was ever named; D3 rule 4 supplies it |
| WA-06 | rule under-claimed as a proposal | **stands** |
| WA-07 | — | **new** — the audit method defect that produced the false findings |

A separate finding: the F2 preamble sentence *"Angka ini belum ada dalam mana-mana dokumen
keputusan"* is **CAIR's own wording in the request form**, not Bariah's, and it was factually
wrong when written because A7 already existed. She then ticked SAH, so the value is confirmed
twice. No source conflict on her side, and nothing to escalate.

### RP-007 — RESOLVED

| Field | Value |
|---|---|
| issue | Rumusan summarises this Bahagian only, contractor perspective, **no** Kepentingan / Isi Utama / Manfaat labels |
| held in | `PL06_RULE_PORTABILITY_MATRIX_v1.md`, `pl06_inventory_data_v1.py` |
| original status | `PL06_GLOBAL_REUSABLE`, oracle yes, propagation risk LOW |
| original evidence | a **verbatim Bariah answer**, not a CAIR proposal |
| historical closing warrant | A6 — and A6 was the **sole** basis |
| historical A6 closure | **WITHDRAWN** |
| disposition | **RESOLVED** |
| current warrant | **D3 rules 1 and 2**, returned authority, 2026-08-05, Bariah Ahmad |

D3 rule 1 removes the headings from learner-facing copy; D3 rule 2 keeps all three components
inside it. Structure and display separated, the A6 / RP-007 conflict disappears.

**Named open consequence.** The B03 calibration deck pairs `A6_LABELS` to the three beats and
displays them. Under D3 rule 1 that display is no longer correct. B03 is not regenerated in
this pass; correction notes are written into `k5_calib_model_v1.py` and `k5_calib_build_v1.py`
so the next regeneration carries them, and the existing
`K5_PL06_T03_B03_CALIBRATION_HANDOFF_v0_1.md` is **stale on this point** until B03 is rebuilt.

### A6 / A7 active-reference sweep

| Location | Finding |
|---|---|
| `docs/pl06/k5_policy/*` | the source of truth for A6/A7 — correct, unchanged |
| `k5_pattern_policy_v1.py`, `k5_policy_apply_v1.py` | carry A6/A7 as data with correct bases — unchanged |
| authority declaration | re-cited to A6/A7 through the newly registered Kelompok 0 artifact |
| `k5_calib_model_v1.py`, `k5_calib_build_v1.py` | correction notes added (label display superseded; RP-007 is not a CAIR proposal; A6 is not phantom) |
| `PL06_AUTHORITY_CROSSWALK_v0_1.md` | regenerated, carries the withdrawn verdicts |
| `t04/*` A6/A7 hits | **false positives** — appendix page numbers, not decision ids |
| this report | revision 3 note at the head |

### Authority / analysis boundary

Removed from the authority declaration and rehoused:

| Record | Destination |
|---|---|
| `dialogue.t02b02_source_scope_verification` | `pl06_packet_model_v1.SOURCE_SCOPE_VERIFICATIONS` → `packet["source_scope_verification"]` |
| `dialogue.row_058_disposition` | `pl06_packet_model_v1.ROW_USE_DISPOSITIONS` → `packet["row_use_disposition"]` |
| `tension_dispositions` | `pl06_packet_model_v1.TENSION_DISPOSITIONS` → `packet["tension_disposition"]` |

`dialogue.paraphrase_contract` **stays**, explicitly typed
`record_type = OWNER_ENGINEERING_AUTHORING_CONTRACT`, named authority Firdaus Ismail, cited to
`FIRDAUS_TENSION_DISPOSITION_v1` §5 — the instructional requirement is Bariah's (E1, E2, C4);
the authoring mechanism is the owner's and is recorded as his.

**Active authority population: 55** — 52 `WRITTEN_CONFIRMED` + 3 `ASSERTED_PRIOR…`, **0 exempt**.
Not 54, and not forced to 52: three records left and three arrived (RP-007 disposition, the B03
canonical copy, the Puan Nadia reconciliation). Gates `THE_ACTIVE_AUTHORITY_POPULATION_IS_THE_DECLARED_ONE`,
`THE_AUTHORITY_STATUS_SPLIT_IS_THE_DECLARED_ONE`, `NO_ACTIVE_WRITTEN_CONFIRMED_RECORD_IS_CITATION_EXEMPT`,
`NO_ANALYSIS_RECORD_LIVES_IN_THE_AUTHORITY_DECLARATION`; fixtures PL-51, PL-52.

### Approved B03 S02 copy

C3 reads *"TERIMA — dialog boleh digunakan seadanya."* The five C1 lines are **reproduced**, not
regenerated: `B03_S02_DIALOGUE_MATCHES_APPROVED_C1_CANONICAL_LINES` compares them against a
suite-owned oracle. Fixtures PL-46 (positive control), PL-47 (word change), PL-48 (speaker
order), PL-49 (line removed), PL-50 (annotation restored). The paraphrase contract explicitly
does not reach this deck.

---

## 15. What was NOT done

- No PPTX emitted. B03 and T04 not regenerated. No batch generation.
- No quiz item or answer key completed, and none marked approved.
- The eight analysis passes were **not** authored — only mapped.
- No unit marked `INSTRUCTIONALLY_APPROVED`; B03 is not `PRODUCTION_READY_FOR_REVIEW` either,
  because F6's acceptance is conditional on amendments that have not been applied.
- The calibration QA suite was not re-run (see §8).
- **Nothing committed or pushed.** The working tree is preserved for review.
