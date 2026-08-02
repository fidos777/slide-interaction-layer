# B02_DEFECT_REGISTER — v0.4.4.1

This file is the one place the retired strings are kept verbatim. The release documents are
barred by gate from restating them, so without this register the evidence of what was wrong
would disappear along with the defect.

# B02-META-REG-001 — `ARTIFACT_VERSION_AND_STATUS_DRIFT`

**Severity:** governance. Not cosmetic. The artifact's visible production metadata is what a
reviewer reads to decide what they are holding, and it disagreed with the filename, the run
manifest, the decision register, the accepted verdict and the package status for four
consecutive releases.

**Found:** Stage 4.2E-C, by direct package inspection of all 100 review pages.

## What was present

Affected pages: **100 of 100**, every page of v0.4, v0.4.1, v0.4.2, v0.4.3 and v0.4.4.

Version line, verbatim:

```
K5 PL06 T03 B02 — PAPAN CERITA v0.4
```

Status tokens, verbatim, across two panel lines:

```
REVIEW_READY · BARIAH_FEEDBACK_IMPLEMENTED
PENDING_TARGETED_CONFIRMATION · NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED
```

Also carried, and equally stale, on the earlier deck:

```
K5 PL06 T03 B02 — PAPAN CERITA v0.3
```

## What it should have said

| Surface | Said | Should have said |
|---|---|---|
| Filename | `…_v0_4_4.pptx` | — |
| Run manifest | v0.4.4 | — |
| Decision register | 47 decisions through Stage 4.2E-A | — |
| Accepted verdict | `B02_V0_4_4_CONSOLIDATED_BUILD_READY_FOR_POWERPOINT_SMOKE` | — |
| **Production panel** | **`… PAPAN CERITA v0.4`** | **`… PAPAN CERITA v0.4.4.1`** |

Two of the five tokens were still true and are retained: `NOT_FOR_MMD_BUILD` and
`MULTIMEDIA_NOT_PRODUCED`. Three were not, and are now prohibited as current status claims —
see `ACTIVE_PACKAGE_STATUS_CONTRACT_v0.4.4.1.json`, key `prohibited_as_current_status`.

The third of them deserves its own note. It asserted that the feedback round was implemented;
that was true of the Stage 4.1 round and said nothing at all about the final 2 August
decisions. `FINAL_BARIAH_DECISIONS_IMPLEMENTED` states the thing that is actually true now.

## The source that emitted it

`generator/v0_4/b02_generator_v0_4.py`, function `prodpanel_v4`:

- `head[0]`, a hand-written literal version string;
- `TOKENS_V4`, a module-level list of five hand-written status tokens.

Neither was derived from anything. Neither was updated at v0.4.1, v0.4.2, v0.4.3 or v0.4.4.

## Why the existing gates did not detect it

Both gates that touched this metadata made detection impossible.

**1. The version gate forbade only the previous version.** In `b02_full_qa_v0_4.py`:

```python
chk("V0_3_TOKENS_IN_PANEL",
    sum(1 for pid in ptext if "v0.3" in ptext[pid] or "PAPAN CERITA v0.3" in ptext[pid]), 0)
```

It never asked what the version *should* be — only that it was not the one before. A gate
written that way goes green for every version except one, and stays green as the artifact
drifts arbitrarily far from its own filename.

**2. The token gate required the stale tokens to be present.** Same file:

```python
for tok in ("REVIEW_READY", "BARIAH_FEEDBACK_IMPLEMENTED", "PENDING_TARGETED_CONFIRMATION",
            "NOT_FOR_MMD_BUILD", "MULTIMEDIA_NOT_PRODUCED"):
    chk(f"PACKAGE_TOKEN_{tok}", all(tok in ptext[pid] for pid in ptext), True)
```

This is the sharper failure. The suite did not merely tolerate the stale release status — it
**mandated** it on every page. Correcting the panel would have turned three gates red. A
check that enforces the wrong answer is worse than no check, because it converts the fix
into a regression.

**3. Nothing compared the panel to any other artifact.** No gate read the run manifest, the
filename or the status contract and compared it with what the package says about itself. The
five surfaces were free to diverge because nothing ever put two of them side by side.

## Corrections made at Stage 4.2E-C

- One controlled identity source: `generator/v0_4/b02_artifact_identity_v0_4_4_1.py`. The
  panel, the run manifest, the QA expected values, the checklist and the release report all
  read it. Nothing restates a version or a token by hand.
- Token comparison is by **exact token set**, recovered by splitting the panel line on its
  separator — never by substring. `CANONICALLY_FROZEN` is a substring of the active
  `NOT_CANONICALLY_FROZEN`, and `… PAPAN CERITA v0.4` is a prefix of `… PAPAN CERITA
  v0.4.4.1`; both would have produced a wrong answer under substring matching, in opposite
  directions.
- `PANEL_VERSION_EQUALS_RUN_MANIFEST_VERSION` and `PANEL_STATUS_EQUALS_ACTIVE_PACKAGE_STATUS`
  read the manifest off disk, so the two surfaces are now compared rather than assumed.
- Three mutation fixtures (`M-01`, `M-02`, `M-03`) revert the panel to each stale value and
  are required to fire.

## Related finding — supersession-marker accounting

Recorded here because it is the same species of error: a governance number produced by
matching a **name** instead of a **definition**.

`SUPERSESSION_MARKERS_PRESENT` was reported as 19 at v0.4.4. That figure came from counting
gate IDs containing the substring `SUPERSEDED`. Six of those nineteen are ordinary live
tests, not markers — among them `SUPERSEDED_RULINGS_MISSING_FROM_PRODUCTION_PANEL`,
`SUPERSEDED_DIRECTION_RENDERED_AS_ACTIVE` and `SHOT_PERSISIR_SUPERSEDED_STATUS_RECORDED`.

A supersession marker is an **inert self-assertion**: expected and actual are both the
constant `SUPERSEDED`. By that definition v0.4.4 had **13** markers and **373** active
passing gates, not 19 and 367. The v0.4.4 figures understated the live suite by six.

`b02_governance_qa_v0_4_4_1.accounting()` now computes all three counts from the definition.
The v0.4.4 artifacts are left as published — they are the record of what was reported at the
time — and this entry is the correction.

# B02-GEOM-REG-001 — `UNREGISTERED_GEOMETRY_EXEMPTION`

See `GEOMETRY_EXEMPTION_REGISTRY_v0.4.4.1.json` for the full record and
`STORYBOARD_QA_REPORT_v0.4.4.1.md` §4 for the classification.

Two shapes sat outside the stage with no registered rule permitting it: the `Title 1` title
placeholder, cleared only by the ad hoc threshold `y < -0.66` in the four-edge gate, and
`ProdPanel`, which the four-edge gate never saw because it iterated the reader's `canvas`
partition and the panel is in `panel`. Both shapes are intentional and neither was moved.
What changed is that the exemption is now a registry entry keyed on placeholder type, shape
name and all four coordinates, the top threshold is `-0.01` like the other three edges, and
the gate iterates every shape on the slide.
