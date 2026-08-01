# QA_WEAKNESS_TAXONOMY — v0.4.3

The Stage 4.2A taxonomy (classes A–H) with one class added at Stage 4.2D.

Every class describes a way a predicate can be **green and uninformative**. They are not
severity levels and they compose: one gate can carry several.

---

# I. CLASSIFICATION_SCOPED_POPULATION *(new at Stage 4.2D)*

> A gate selects its test population using a **classification field** that can exclude
> records which still share the semantic obligation being tested.

The predicate is correct. The comparison is correct. The population is wrong, and the gate
is green because the records that would have failed were never in it.

## Canonical example

```python
ess = [pid for pid in pol if pol[pid]["semantic_screen_subtype"] == "EXAMPLE_SELECTION_SCREEN"]
chk("EXAMPLE_SELECTION_SCREENS_WITHOUT_VISUAL", sum(1 for pid in ess if not has_dir[pid]), 0)
```

`semantic_screen_subtype` is assigned per **runtime state**. A selection screen has three
kinds of state — base, popup, all-viewed — and only the base state classifies as
`EXAMPLE_SELECTION_SCREEN`; a popup state classifies as `EXAMPLE_POPUP` and an all-viewed
state as `COMPLETION_STATE`. So `ess` holds **4 of the 24 pages** that render that screen.

The obligation — *every example on this screen carries its own visual* — belongs to the
**learner screen**, not to one of its states. When the popup and all-viewed states rendered
with no card visuals at all, the gate stayed green and the suite reported 216/216. The
defect was found by looking at a rendered page.

## The signature

A gate is classification-scoped when **all** of these hold:

1. its population comes from a field that varies **across states of one screen**, one of:
   `semantic_screen_subtype`, `screen_role`, `review_page_role`, `runtime_state_type`,
   `popup_subtype`, `visual_requirement`, `notes_policy`, `completion_scope`;
2. the obligation it tests is owned by a **stabler anchor** — `learner_screen_id`,
   `interaction_item_id`, `parent_screen_id` or `component_id`;
3. the selected set is a **proper subset** of that anchor's full record set.

Condition 3 is computable. Condition 2 is a judgement and is recorded per gate in
`QA_POPULATION_AUDIT_v0.4.3.json` as `obligation_scope`.

## How it is distinguished from the other classes

| Class | The gate's flaw is in… | Would a bigger population fix it? |
|---|---|:-:|
| **I · CLASSIFICATION_SCOPED_POPULATION** | **which records it looks at** | **yes — this is the definition** |
| A · PRESENCE_ONLY | how weakly it looks (exists ≠ correct) | no |
| B · SINGLE_AXIS_GEOMETRY | how many dimensions it measures | no |
| C · COUNT_WITHOUT_IDENTITY | whether it names *which* record | no |
| D · MODEL_ONLY_ASSERTION | which artifact it reads (model, not package) | no |
| E · SHARED_DERIVATION | where the expected value comes from | no |
| F · VISIBILITY_BLIND | whether the reader could actually see it | no |
| G · FAIL_OPEN | what happens when the population is empty | related, opposite |
| H · SELF_RESOLVED_JUDGMENT | who decided the expected value | no |

The two easiest to confuse:

- **vs. C (COUNT_WITHOUT_IDENTITY).** C looks at the right records and reports only a
  total, so a swap of two records passes. I looks at the *wrong set* of records; it can be
  perfectly identity-precise about the records it does see. `TICK_IDENTITY_MISMATCHES` is
  identity-precise (not C) and was still population-limited until Stage 4.2C.
- **vs. G (FAIL_OPEN).** G passes because the population is **empty** — `sum(...) == 0` over
  nothing. I passes because the population is **non-empty but incomplete**, which is worse:
  the non-vacuity guards added at Stage 4.2B (`*_EVALUATED`) defeat G and are blind to I.
  `EXAMPLE_SELECTION_SCREENS_TOTAL == 4` was a live non-vacuity guard sitting directly
  beside the blind gate, asserting the wrong number confidently.

## Detection

Two independent methods, and both are run:

- **Computed** — `generator/audit/b02_population_audit_v0_4_3.py` resolves each gate's real
  population against the deck and compares it with the anchor's full record set.
- **Empirical** — `generator/audit/b02_classification_scope_fixtures_v0_4_3.py` mutates
  records that lie *outside* the classification-selected population but *inside* the
  semantic one. A gate that does not fire is blind by demonstration, not by argument.

## Remedy

Pin the population to the stable anchor, and let the classification field select the
*expectation*, never the *population*. The pattern that works:

```python
# population: every state page of every screen that owns the obligation
sel_screens = {rec_of[pid]["learner_screen_id"] for pid in D
               if rec_of[pid]["screen_role"] == "COMPONENT_EXAMPLE_SELECTION"}
sel_pages = [pid for pid in D if rec_of[pid]["learner_screen_id"] in sel_screens]
```

`rec_of[...]["screen_role"]` is a **screen** attribute and is constant across the screen's
states; `pol[...]["semantic_screen_subtype"] `is a **state** attribute and is not. Selecting
the screen set first and then taking all its pages is what makes the population complete.

An added `*_EVALUATED` gate should assert the **pinned** count (24), not the classified one
(4), so a future narrowing of the population fails a gate instead of passing silently.
