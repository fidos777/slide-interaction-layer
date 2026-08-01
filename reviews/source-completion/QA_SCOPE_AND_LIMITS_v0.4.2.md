# QA_SCOPE_AND_LIMITS — v0.4.2

> **189 of 189 mechanical checks passing does not mean the deck is approved.**
> It means every check that exists passed. Stage 4.2A found a class of defect that
> passed 188/188, so the number measures the suite, not the artifact.

# 1. Totals, disaggregated

| Category | Count |
|---|---:|
| `MODEL_CHECKS` | 60 |
| `PACKAGE_XML_CHECKS` | 110 |
| `RENDERED_GEOMETRY_CHECKS` | 5 |
| `ORACLE_CONFORMANCE_CHECKS` | 14 |
| `HISTORICAL_REPLAY_CHECKS` | 1 artifact (40 gates fire) |
| `MUTATION_SENSITIVITY_CHECKS` | 12 |
| `PENDING_HUMAN` | 15 disclosed items + 9 conditional visual records |
| `NOT_CHECKED` | see §3 |

Of 189 predicates, only **14** compare
against an independently-derived expected value, and only
**2 of 11** registry
records have a frozen-artifact oracle. Every 1 August 2026 ruling is `TASK_TRANSCRIPT_ONLY`: no
WhatsApp screenshot or exported chat is frozen in this repository.

# 2. What the suite does establish

- The generated package is internally consistent with the frozen model.
- Source identity holds: 26 rows, 14 assets, 0 created.
- No known regression shape is present: all 12 fixtures fire their gate.
- The superseded v0.4 deck fails 40 gates, so the suite
  discriminates between the bad and corrected artifacts.
- No canvas object lies outside the stage on any edge.
- Every glossary occurrence in Notes carries OOXML italic formatting.

# 3. NOT CHECKED

| Area | Status | Why |
|---|---|---|
| Microsoft PowerPoint font wrapping | **NOT CHECKED** | LibreOffice has no Impress import filter; rendering uses a Liberation Sans metric renderer. PowerPoint equivalence is not proven. |
| Microsoft PowerPoint Notes appearance | **NOT CHECKED** | italic runs are verified in XML; their on-screen appearance in PowerPoint is not. |
| Actual Slide Show behaviour | **NOT CHECKED** | this is a storyboard, not a runtime package. |
| Actual LMS navigation behaviour | **NOT CHECKED** | `TAMAT_PHYSICAL_NAVIGATION_STATUS = PENDING_FIRDAUS_OR_LMS_CONFIRMATION`. |
| Human visual suitability | **NOT CHECKED** | 10 PENDING_HUMAN items; density and hierarchy are judgement. |
| Unresolved conditional visual decisions | **NOT CHECKED** | 9 component-main / gateway records pending Bariah. |
| Final multimedia suitability | **NOT CHECKED** | no asset is bound; every visual is a textual direction. |
| Complete module DOCX integrity | **NOT CHECKED** | `B02-CAIR-INT-001` open; `SOURCE_INTEGRITY_FULLY_VERIFIED` not claimed. |
| Whether the glossary is complete | **NOT CHECKED** | the 9-term list is CC-authored; no frozen artifact enumerates it. |
| Whether the canvas denylist is complete | **NOT CHECKED** | CC-authored from the model vocabulary. |
| Text visibility (clipping / covering) | **NOT CHECKED** | 124 predicates read XML without proving the text is visible. |

# 4. Structural limits of the suite

- **21 predicates share a helper with the generator.** They detect
  drift, never a wrong shared rule.
- **60 predicates never read the package.**
- **32 assert presence, not conformance.**
- **2 are green because CC resolved a CONDITIONAL.**

# 5. Honest headline

```
MECHANICAL_CHECKS_PASSING            = 189 / 189
INDEPENDENT_ORACLE_BACKED_RECORDS    = 2 / 11
DEFECT_CLASSES_KNOWN_UNGUARDED       = 0 (one was found and closed this stage)
AREAS_NOT_CHECKED                    = 11
PENDING_HUMAN_ITEMS                  = 15 + 9 conditional visuals
DECK_APPROVED                        = NO — review build only
```
