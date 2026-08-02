# OBLIGATION_COVERAGE_MATRIX — v0.4.4

> A model-only row is **not** artifact assurance. This matrix exists so no obligation can be reported as covered when only the plan was checked.

| Metric | Value |
|---|---:|
| `OBLIGATIONS` | 17 |
| `CHECKED_AT_MODEL` | 17 |
| `CHECKED_IN_GENERATED_PPTX` | 17 |
| `CHECKED_ON_RENDERED_PAGE` | 11 |
| `CHECKED_AGAINST_INDEPENDENT_ORACLE` | 13 |
| `CHECKED_BY_NEGATIVE_MUTATION` | 17 |
| `MODEL_ONLY_ROWS` | 0 |

| Obligation | Model | PPTX | Rendered | Oracle | Mutation |
|---|:-:|:-:|:-:|:-:|---|
| Papan Tanda overview = 2 source-bound visuals | ✅ | ✅ | ✅ | ✅ | C-01, C-02, C-03, C-07 |
| BBQ Pit overview = 1 source-bound visual | ✅ | ✅ | ✅ | ✅ | C-04, C-05, C-06 |
| all nine component-main overviews rendered | ✅ | ✅ | ✅ | — | C-06 |
| no invented or cross-component overview subject | ✅ | ✅ | ✅ | ✅ | C-02, C-03, C-07 |
| overview persists on all-viewed and return states | ✅ | ✅ | ✅ | ✅ | C-08, C-09 |
| example/information popup carries a larger focused visual | ✅ | ✅ | ✅ | ✅ | R-015, R-016 |
| specification popup carries no visual panel | ✅ | ✅ | ✅ | ✅ | R-009, C-21 |
| Slide 5 Asas Pembinaan on canvas | ✅ | ✅ | ✅ | ✅ | C-10, C-11 |
| Slide 5 canvas/VO parity | ✅ | ✅ | — | ✅ | C-12 |
| S01 three blocks, lines 1-2 without a full stop | ✅ | ✅ | — | ✅ | C-13, R-012, R-013, R-014 |
| exact quiz feedback strings | ✅ | ✅ | ✅ | ✅ | C-15 |
| no quiz rationale in Notes or spoken export | ✅ | ✅ | — | ✅ | C-14 |
| no micro-control instruction in spoken VO | ✅ | ✅ | — | ✅ | C-16 |
| cast names only on bound screens | ✅ | ✅ | ✅ | ✅ | C-18 |
| Tamat learner copy unchanged, mechanism in metadata | ✅ | ✅ | ✅ | — | C-19, R-006 |
| PL06 pronunciation remains inactive | ✅ | ✅ | — | — | C-20 |
| structural totals unchanged | ✅ | ✅ | — | — | R-004 |

# Notes

- **Papan Tanda overview = 2 source-bound visuals** — oracle = D4 cardinality screenshot, re-hashed each run
- **BBQ Pit overview = 1 source-bound visual** — oracle = D4
- **all nine component-main overviews rendered** — cardinality per component comes from the frozen mapping contract, not from an oracle
- **no invented or cross-component overview subject** — subject strings are MODULE_SOURCE_ATTESTED; D4 names only the two Papan Tanda figures
- **overview persists on all-viewed and return states** — population pinned to learner_screen_id; oracle = D3 persistence reply
- **example/information popup carries a larger focused visual** — oracle = D2 treatment reply
- **specification popup carries no visual panel** — oracle = the 4:37 PM subtype ruling
- **Slide 5 Asas Pembinaan on canvas** — oracle = D1
- **Slide 5 canvas/VO parity** — package twin added after C-12 was missed; not separately visible on a rendered page
- **S01 three blocks, lines 1-2 without a full stop** — oracle = D3 'Buang noktah'
- **exact quiz feedback strings** — oracle = D3
- **no quiz rationale in Notes or spoken export** — rationale retained in the production panel and asserted there
- **no micro-control instruction in spoken VO** — package twin added after C-16 was missed
- **cast names only on bound screens** — oracle = D3 cast reply; reuse permitted but never automatic
- **Tamat learner copy unchanged, mechanism in metadata** — LMS-owner ruling, not Bariah; no independent artifact oracle exists
- **PL06 pronunciation remains inactive** — absence assertion; no oracle can confirm an unratified rule
- **structural totals unchanged** — model + package counts

Every obligation is checked in the generated package. Six are not separately verifiable on a rendered page (Notes content, absence assertions and counts are not visual), and four have no independent oracle because no artifact exists that could serve as one — the LMS navigation ruling, the cardinality-per-component contract, the structural totals and the unratified pronunciation rule. Those four are disclosed here rather than counted as oracle-backed.
