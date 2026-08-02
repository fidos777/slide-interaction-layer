# PL06_RULE_PORTABILITY_MATRIX — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py`.

```
PL06_GLOBAL_REUSABLE = 17
REUSABLE_WITH_SOURCE_SPECIFIC_BINDING = 8
B02_SPECIFIC_DO_NOT_PROPAGATE = 15
TOTAL_RULES = 40
```

> **A rule is not global because it worked once.** Every entry in class A had to be traceable to a statement about the shell, the grammar or the governance mechanism — not to the fact that B02 shipped with it. Two entries (RP-009, RP-010) are marked GLOBAL on the strength of a Style and Guidelines document that is itself the B02 slice, and both carry `human_authority_required = VERIFY` for that reason.

# A. PL06_GLOBAL_REUSABLE

| rule_id | rule | evidence | destination scope | human authority | oracle | propagation risk |
|---|---|---|---|---|---|---|
| `RP-001` | Review storyboard shell: 13.3333x7.5in stage, navigation band at 6.92in, off-canvas production panel, one review page per runtime state | A3 §2.1 global flow; implemented and gated in B02 across 100 pages | ALL_PL06_UNITS | NONE — mechanical | yes | LOW |
| `RP-002` | S01 / S02 / S03 screen grammar: topic-entry, dialog, orientation | A3 §2.1; A2 answered; B02 S01 spoken-block ruling frozen in D3 | ALL_PL06_UNITS | NONE for the grammar; the CONTENT of S02/S03 is per-unit | yes | LOW for structure. The S01 spoken text is unit-specific and must be re-derived — reusing B02's three blocks verbatim would state the wrong Topik and Bahagian. |
| `RP-003` | Production-panel treatment: off-canvas at x=-6.90in, model-quoted metadata, never hand-restated | b02_generator_v0_4.prodpanel_v4; GEX-002 registered exemption | ALL_PL06_UNITS | NONE | yes | LOW |
| `RP-004` | Speaker Notes typed-block schema: NON_SPOKEN_CONTEXT / SPOKEN_CONTENT_VO / SPOKEN_INTERACTION_INSTRUCTION / PRODUCTION_INSTRUCTION_NOT_SPOKEN, each with an explicit spoken boolean | NOTES_BLOCK_SCHEMA_v0.4.2.json; gated by NOTES_BLOCKS_WITHOUT_TYPE and NOTES_BLOCKS_WITHOUT_SPOKEN_FLAG | ALL_PL06_UNITS | NONE | yes | LOW |
| `RP-005` | English-term italics mechanism: run-level <a:rPr i="1"/> applied through one controlled glossary shared by canvas and Notes writers | b02_glossary_v0_4; APPROVED_TERMS_NOT_ITALICISED gate | ALL_PL06_UNITS | The TERM LIST is per-unit and needs SME sign-off; the mechanism does not | yes | MEDIUM — the mechanism is global, the B02 term list is not. Propagating the list would italicise words a different unit never uses and miss the ones it does. |
| `RP-006` | Completion-state treatment: all-viewed and group-complete states re-render the base screen with completion marks, never a new screen | A3; B02 22 component-main state pages; PERSISTENCE_TARGET gates | ALL_PL06_UNITS | NONE | yes | LOW |
| `RP-007` | Rumusan treatment: summarises THIS Bahagian only, contractor/site perspective, no Kepentingan / Isi Utama / Manfaat labels | A2 answered verbatim: 'Rumusan perlu merumuskan Bahagian 2 sahaja dan menggunakan perspektif kontraktor. Ia tidak memaparkan label Kepentingan, Isi Utama atau Manfaat.' | ALL_PL06_UNITS | NONE for the rule; the CONTENT is per-unit | yes | LOW |
| `RP-008` | Quiz review structure: question -> answer -> review state, answer key visible in the review state, rationale in the production panel only | A3; B02 five questions; QUIZ_REVIEW_STATE_* gates | ALL_PL06_UNITS | NONE for the structure | yes | LOW |
| `RP-009` | Quiz composition: 4 MCQ + 1 MR | A3; implemented in B02 and gated | ALL_PL06_UNITS | VERIFY — A3 is the B02 slice of the S&G. Whether 4+1 is a PL06 standard or a B02 instantiation has NOT been confirmed by anyone. | yes | MEDIUM — classified GLOBAL on the strength of a Style and Guidelines document, not on a statement that it applies to every unit. Flagged for confirmation, not assumed. |
| `RP-010` | 60 percent pass threshold | A3 | ALL_PL06_UNITS | VERIFY — same caveat as RP-009 | yes | MEDIUM |
| `RP-011` | Correct / incorrect feedback wording: 'Pilihan jawapan tepat.' and 'Pilihan jawapan tidak tepat.', not spoken | D3 frozen screenshot ruling, Stage 4.2E-A; QUIZ_FEEDBACK_REGISTER_v0.4.4.json | ALL_PL06_UNITS | NONE — Bariah ruled the wording directly | yes | LOW |
| `RP-012` | Tamat and close-window behaviour: learner closes the window, shell next disabled, route recorded as LMS-owner metadata with both claims NOT PROVEN | A3; Firdaus/LMS ruling recorded at Stage 4.2E-A | ALL_PL06_UNITS | The DESTINATION is per-unit — B02's is 'next Bahagian in Topik 3' and no other unit's is known | yes | LOW for behaviour, HIGH for destination text |
| `RP-013` | Off-canvas registered geometry treatment: an off-stage shape passes only if a registry entry matches its placeholder type, name and all four coordinates | GEOMETRY_EXEMPTION_REGISTRY_v0.4.4.1.json; fixtures M-08 to M-11 | ALL_PL06_UNITS | NONE | yes | LOW |
| `RP-014` | Artifact identity and exact release-token validation: one controlled identity source, token comparison by exact set, panel vs manifest agreement | b02_artifact_identity_v0_4_4_1.py; defect B02-META-REG-001 | ALL_PL06_UNITS | NONE | yes | LOW — and this one is the highest-value rule to propagate first. It is the rule whose absence let four B02 releases ship mis-stamped. |
| `RP-015` | Three-way separation of physical learner screen, runtime state and review page | B02 model contract 29 / 100 / 100; gated | ALL_PL06_UNITS | NONE | yes | LOW |
| `RP-016` | Oracle contract: an oracle module imports nothing from the generator and re-hashes its evidence before returning a value | generator/audit/*; *_ORACLE_IMPORTS_NO_GENERATOR gates | ALL_PL06_UNITS | NONE | yes | LOW |
| `RP-017` | Population pinning: a gate's population is pinned to learner_screen_id and its bound runtime states, never to review-page classification | class I CLASSIFICATION_SCOPED_POPULATION, Stage 4.2D | ALL_PL06_UNITS | NONE | yes | LOW |

# B. REUSABLE_WITH_SOURCE_SPECIFIC_BINDING

| rule_id | rule | evidence | destination scope | human authority | oracle | propagation risk |
|---|---|---|---|---|---|---|
| `RP-101` | Visual overview treatment: a component-main screen carries several smaller source-bound visuals as an overview | D2 6:52 PM screenshot — 'Component-main - Visual diperlukan' and the overview treatment | PL06 units that HAVE component-main screens | Per unit: whether the unit even has component-main screens, and what the subjects are | yes | HIGH — D2 was given while reviewing B02. It is written generally enough to read as a treatment rule, but every subject in it is bound to a B02 source row. A unit with no component structure has nothing for this rule to attach to. |
| `RP-102` | Example popup treatment: one large focused visual panel, measurably wider than any overview card | D2; B02 4.14in panel vs 2.60in card, gated | PL06 units with example popups | Per unit: whether example popups exist | yes | MEDIUM |
| `RP-103` | Specification popups are text-led and carry NO visual | Bariah 4:37 PM verbatim: 'Semua contoh ada visual. Semua pop up ada visual, KECUALI pop up Spesifikasi (bahan, dimensi etc)' | PL06 units with specification popups | Per unit: whether spec popups exist | yes | LOW |
| `RP-104` | Source figure binding: a visual direction is read from the source row's own figure or table photograph, never composed from the component name | B02_ASSET_MANIFEST.md 14 assets; EXAMPLE_CARD_VISUALS_NOT_SOURCE_ATTESTED gate | ALL_PL06_UNITS with extracted assets | None for the rule; the ASSETS must be extracted and hashed per unit | yes | MEDIUM — the rule is portable, the asset register is not. A unit with no extracted assets cannot satisfy it and must not be given placeholder subjects to pass. |
| `RP-105` | Learner-screen persistence: base identity persists across all bound runtime states, compared by SUBJECT IDENTITY not by shape count | D2 persistence ruling; B02 22 state pages | PL06 units with multi-state screens | Per unit: which screens have states | yes | LOW |
| `RP-106` | Character use: named cast appears only on screens with an explicit cast binding | Bariah A2 answer: 'Gunakan nama watak untuk keseluruhan PL06. Gunakan nama watak yang sama bergantung kepada kesesuaian.' — PL06 SCOPE, conditional on suitability | ALL_PL06_UNITS | REQUIRED — and unresolved. See SRC-ANOM-003: the ratified bank marks Haziq and Encik Roslan CANONICAL while B02 ships Alya and Encik Rahman. Bariah's PL06-wide instruction does not say WHICH pair. | **no** | HIGH — this is the single rule most likely to be propagated wrongly. Bariah's answer is PL06-scoped, which makes it look global; it is conditional on 'kesesuaian' and it conflicts with a ratified character bank that nobody has reconciled. |
| `RP-107` | Screen-level VO instructions only: 'Klik pada setiap…' is spoken; Tutup, Kembali, Semak Jawapan and Ulang Kuiz are not | D3 frozen ruling; MICRO_CONTROL_INSTRUCTIONS_IN_PACKAGE_NOTES gate | ALL_PL06_UNITS | The micro-control LIST is B02's control vocabulary; a unit with different controls needs its own list | yes | LOW |
| `RP-108` | Question and answer mapping: every quiz option maps to a source row and the answer key is derived from controlled content | ANSWER_KEY_SOURCE_MISMATCH gate; B02 five questions | ALL_PL06_UNITS | SME sign-off on each unit's answer key | yes | LOW |

# C. B02_SPECIFIC_DO_NOT_PROPAGATE

| rule_id | rule | evidence | destination scope | human authority | oracle | propagation risk |
|---|---|---|---|---|---|---|
| `RP-201` | FAMILY_S execution family — 4 components, selection screen with example cards | B02_INTERACTION_FAMILY_TAXONOMY_v0_4.md; derived from B02's 26 source rows | K5-PL06-T03-B02 ONLY | Any reuse needs a fresh derivation from the target unit's source | yes | HIGH — the three families are a reading of B02's table structure. They are not a PL06 interaction taxonomy and were never presented to anyone as one. |
| `RP-202` | FAMILY_P1 execution family — 3 components, per-example specification popups | same | K5-PL06-T03-B02 ONLY | same | yes | HIGH |
| `RP-203` | FAMILY_P2 execution family — 2 components, category-level popups | same | K5-PL06-T03-B02 ONLY | same | yes | HIGH |
| `RP-204` | The nine B02 component names — Struktur Persisir Air, Struktur Teduhan, Kemudahan Awam, Water Feature, Kerusi Taman, Papan Tanda, Tong Sampah, Drinking Fountain, BBQ Pit | modul ms 238-249 | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH |
| `RP-205` | The nine B02 overview cardinalities 5, 5, 3, 3, 3, 2, 3, 2, 1 | COMPONENT_OVERVIEW_MAPPING_v0.4.4.json; D4 for the 2 and the 1 | K5-PL06-T03-B02 ONLY | N/A — and note the frozen rule UNIVERSAL_FIXED_CARD_COUNT = False, which forbids treating any of these as a template | yes | HIGH — a fixed card count is exactly the kind of rule that looks reusable and is not. The mapping contract records MINIMUM_OVERVIEW_CARDINALITY = 1 and nothing above it. |
| `RP-206` | Papan Tanda ruling — two visuals, Pilihan A, the figures Informasi and Penunjuk Arah | D4 8:24 AM verbatim 'Yup, papan tanda Pilihan A, ok bbq pit 1 gamba' | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH — and the frozen ruling explicitly records informasi_equals_interpretatif_global_rule = False. It is not a naming rule. |
| `RP-207` | BBQ Pit ruling — exactly one visual, five alternatives rejected | D4 | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH |
| `RP-208` | The 26 B02 source rows and their UIDs | STORYBOARD_SOURCE_MAP_v0.4.md | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH |
| `RP-209` | The 27 B02 visual subjects | COMPONENT_OVERVIEW_MAPPING_v0.4.4.json | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH — INVENTED_VISUAL_SUBJECTS = 0 is a per-unit obligation, not a transferable result. |
| `RP-210` | B02 learner-screen count 29 | B02_V0_4_MODEL_CONTRACT.json | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH |
| `RP-211` | B02 runtime-state count 100 | B02_V0_4_MODEL_CONTRACT.json | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH |
| `RP-212` | B02 interaction-item count 54 | B02_V0_4_MODEL_CONTRACT.json | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH |
| `RP-213` | B02-specific text and factual claims, including the MS2680 citation and the Slide 5 Asas Pembinaan bullets | controlled content b02_proof_content_v0_4.py | K5-PL06-T03-B02 ONLY | N/A | yes | HIGH |
| `RP-214` | The B02 glossary term list and its italic set | b02_glossary_v0_4.py | K5-PL06-T03-B02 ONLY | Per-unit SME derivation | yes | MEDIUM — see RP-005: the MECHANISM is global, this LIST is not. |
| `RP-215` | The Alya / Encik Rahman cast pair | B02 S02 binding; approved by Bariah for B02 | K5-PL06-T03-B02 ONLY until SRC-ANOM-003 is resolved | REQUIRED — conflicts with the ratified CANONICAL pair Haziq / Encik Roslan | **no** | HIGH — Bariah's 'keseluruhan PL06' answer is about the PRACTICE of naming characters, not an instruction to use these two names everywhere. Reading it the other way would override a ratified character bank on the strength of an answer to a different question. |

# The two rules most likely to be propagated wrongly

**RP-106 / RP-215 — the cast.** Bariah's answer *"Gunakan nama watak untuk keseluruhan PL06"* is PL06-scoped, which makes it read like a global instruction. It is an answer about the *practice* of naming characters, qualified by *bergantung kepada kesesuaian*, and it names no one. Meanwhile the ratified character bank marks **Haziq** and **Encik Roslan** CANONICAL while B02 ships **Alya** and **Encik Rahman**. Reading her answer as "use Alya and Encik Rahman everywhere" would override a ratified bank on the strength of an answer to a different question. Recorded as `SRC-ANOM-003` and `STOP-006`.

**RP-205 — the overview cardinalities.** 5, 5, 3, 3, 3, 2, 3, 2, 1 is the most template-shaped artefact B02 produced, and the frozen mapping contract explicitly records `UNIVERSAL_FIXED_CARD_COUNT = False` and `MINIMUM_OVERVIEW_CARDINALITY = 1`. The counts are per-component derivations from B02's own source rows. Nothing above the minimum transfers.
