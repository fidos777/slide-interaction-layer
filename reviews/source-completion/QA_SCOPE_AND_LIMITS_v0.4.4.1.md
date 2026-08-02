# QA_SCOPE_AND_LIMITS — v0.4.4.1

> **No single number here means "approved".** Read §1.1 before quoting any of them: this
> stage exists because a fully green suite shipped four releases with the wrong version
> stamped on all 100 pages, and two of the gates covering that metadata were the reason it
> could not be seen.

# 1. Test accounting

| Metric | Value |
|---|---:|
| `ACTIVE_TEST_GATES_PASSING` | **441 / 441** |
| `SUPERSESSION_MARKERS_PRESENT` | **20** |
| `TOTAL_EMITTED_GATE_RECORDS` | **461** |

A supersession marker is an inert self-assertion: expected and actual are both the constant
`SUPERSEDED`. It keeps a retired ruling visible instead of letting it vanish. Twenty of them
are not twenty passing checks.

## 1.1 What a green suite did not catch, twice over

Two findings from this stage, both of the same species — a check that measured a **name** or
a **neighbouring value** instead of the property it was supposed to hold.

**The version gate forbade the previous version instead of asserting the current one.**
`V0_3_TOKENS_IN_PANEL` tested that the panel did not say `v0.3`. It never asked what the
panel *should* say. That gate goes green for every version except one, and stayed green
through four releases of drift.

**The token gate mandated the stale answer.** Five `PACKAGE_TOKEN_*` gates required the Stage
4 release tokens to be present on every page. The suite did not merely tolerate the wrong
release status — it enforced it, and correcting the panel would have turned three gates red.
A check that enforces the wrong answer is worse than no check.

**And the marker count was taken by substring.** `SUPERSESSION_MARKERS_PRESENT` was computed
by matching `SUPERSEDED` in the gate ID, which swept in six ordinary live tests. v0.4.4's
published 367 / 19 / 386 should have read 373 / 13 / 386 — the live suite was understated by
six. Corrected in §1 of `STORYBOARD_QA_REPORT_v0.4.4.1.md`; v0.4.4's artifacts are left as
published because they are the record of what was reported at the time.

All three are now computed from a definition rather than a name, and the identity comparison
is by exact token set — never substring, because `CANONICALLY_FROZEN` sits inside the active
`NOT_CANONICALLY_FROZEN` and `… PAPAN CERITA v0.4` is a prefix of `… PAPAN CERITA v0.4.4.1`.

# 2. Layers

| Layer | What it reads |
|---|---|
| `MODEL` | the frozen model and the policy derived from it — **not the artifact** |
| `PACKAGE_XML` | the generated `.pptx` read back out of its own bytes |
| `ARTIFACT_AGREEMENT` | package vs run manifest, checklist, release report, exemption registry, mapping contract — added this stage |
| `ORACLE_CONFORMANCE` | expected values from modules that import nothing from the generator and re-hash their evidence |
| `RENDERED_GEOMETRY` | positions and extents in inches, every shape on the slide |
| `CLASSIFICATION_POPULATION` | populations pinned to `learner_screen_id`, not to review-page class |
| `MUTATION_SENSITIVITY` | 51 fixtures |
| `SUPERSESSION` markers | 20 — not tests |
| `PENDING_SOURCE_AUTHORITY` | 3 — MS2680, `B02-CAIR-INT-001`, OD-10 / L-01 |

`ARTIFACT_AGREEMENT` is new and is the direct answer to B02-META-REG-001. Before it, nothing
in the suite ever put two surfaces side by side; the panel, the filename, the manifest, the
register and the verdict were each internally consistent and free to diverge from one another.

# 3. What this build establishes

- The production panel on all 100 pages states the artifact's real version and its real
  release standing, and both agree with the run manifest read off disk.
- All nine component-main governance blocks state the settled position, with the requirement
  and treatment authority separated from subject authority, and zero promotions.
- Every shape outside the stage is covered by a registry entry keyed on placeholder type,
  name and exact coordinates — or it fails.
- 51 injected defects all fire, including twelve aimed at exactly what this stage changed.
- **Zero learner-facing delta from v0.4.4**, proved shape by shape across all 100 pages, with
  an identical render report.

# 4. What it does **not** prove

- **Microsoft PowerPoint equivalence.** No Impress import filter in this container;
  `soffice --convert-to pdf` fails. Rendering is a package parser with Liberation Sans
  metrics, which is metric-compatible with Arial and not with Calibri. **No smoke test has
  run.** That is the next stage.
- **Instructional correctness.** Nothing checks whether the teaching is right.
- **Visual suitability.** Directions are text. No image is embedded or assessed.
- **Actual LMS navigation.** Both Tamat route claims remain NOT PROVEN.
- **That the metadata is now complete.** It is now *consistent across five surfaces* and
  pinned by fixtures. Consistency is not completeness.
- **Completeness outside the fixture set.** 51 fixtures cover the defects we have thought of.

## 4.1 Limits found in this stage's own work

- **A superseded gate would have forced a false promotion.**
  `COMPONENT_MAIN_RESOLVED_WITHOUT_BARIAH_AUTHORITY` required the direction's authority to be
  `BARIAH_DIRECT` wherever the status was RESOLVED. Correct while one component main was
  resolved; against nine it would have demanded that eight module-attested directions claim
  Bariah named them. Carried forward unexamined, a gate can compel the defect it was written
  to prevent.
- **A second unregistered exemption was found only by widening the population.** The `Title 1`
  threshold was the reported finding. `ProdPanel` escaping the four-edge gate entirely — via
  the reader's canvas/panel partition, not via any rule — was found by asking what else the
  gate never looked at. The reported instance of a class is rarely the only one.
- **The stale-claim gate on the release documents is scoped to prose.** The release report
  embeds the verbatim suite transcript, and three gate IDs legitimately contain the token
  they forbid. Fenced blocks are excluded from that check. The exclusion is stated, and it is
  a real hole: a retired claim hidden inside a fence would not fire.

# 5. Historical replay is not a ranking

See `REGRESSION_REPLAY_REPORT_v0.4.4.1.md`. Earlier decks fail the current suite by
construction — v0.4.4 fails the identity gates because the identity gates are what this stage
added, and v0.4.4 was READY under its own oracle.

# 6. Standing

`REVIEW_CANDIDATE` · `FINAL_BARIAH_DECISIONS_IMPLEMENTED` · `INSTANCE_MAPPING_COMPLETE` ·
`READY_FOR_MICROSOFT_POWERPOINT_SMOKE` · `NOT_FOR_MMD_BUILD` · `NOT_CANONICALLY_FROZEN` ·
`MULTIMEDIA_NOT_PRODUCED`

Not asserted: `PRODUCTION_APPROVED`, `CANONICAL_FREEZE`, `MMD_BUILD_READY`,
`SOURCE_INTEGRITY_FULLY_VERIFIED`, `MICROSOFT_POWERPOINT_EQUIVALENCE`,
**`SOURCE_GOVERNANCE_COMPLETE`**.
