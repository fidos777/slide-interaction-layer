# FIRDAUS_TENSION_DISPOSITION — v1

```
AUTHORITY_CLASS = OWNER_HUMAN_REVIEW_DISPOSITION
NAMED_AUTHORITY = Firdaus Ismail
DATE            = 2026-08-05
SCOPE           = K5-PL06-T01-B03, K5-PL06-T02-B01, K5-PL06-T02-B02
```

E2 is a `WRITTEN_CONFIRMED` instructional rule and its own note reserves verification to a
human: *"keperluan ini akan disemak oleh manusia, bukan oleh pemeriksa automatik."* This
record is that human review, performed by the owner. It is **not** an instructional approval
and it does not carry Bariah Ahmad's authority. It disposes of three internal review items and
records why none of them was escalated.

## 1. K5-PL06-T01-B03

| Field | Value |
|---|---|
| source basis | **ACCEPTED** |
| current tension | **NOT ACCEPTED** |
| action | **REAUTHOR** |
| classification | `INTERNAL_HUMAN_AUTHORING_REVIEW` |
| rows permitted | `T01B03-ROW-125`, `T01B03-ROW-142` |

Build a real work decision from those rows — for example whether the work may proceed before
the electrical safety test is done.

Prohibited: restating raw procedure; inserting analyst notes; claiming a legal duty the source
does not support; using verbatim source text where it does not sound like natural speech.

Required: natural Malay; a real work decision, doubt or risk; source trace kept; no authority
or obligation added that the source does not carry.

## 2. K5-PL06-T02-B01

| Field | Value |
|---|---|
| tension | **ACCEPTED** |
| classification | `CLOSED_BY_FIRDAUS_HUMAN_REVIEW` |
| rows permitted | `T02B01-ROW-040` |

Use `ROW-040` as the basis of an operational decision: whether watering or pest monitoring may
be reduced when the planting looks healthy in the early period. The answer stays on the source
claim — adequate watering and pest monitoring are mandatory in the early planting period.

**A compliance-sensitive or legal issue is not required to accept a tension.** E2 asks only for
a meaningful question, problem, doubt, tension or decision point.

## 3. K5-PL06-T02-B02

| Field | Value |
|---|---|
| `ROW-051` | **CONDITIONALLY ACCEPTED** |
| required check | verify source / subtopic mapping before authoring |
| `ROW-058` | **NOT ACCEPTED for the same dialogue** |
| classification | `INTERNAL_SOURCE_SCOPE_REVIEW` |

Confirm `ROW-051` is genuinely inside the unit's source scope and declared subtopic, and report
the source hierarchy and declared subtopic that bind it. If the mapping holds, build the
decision of whether surface drainage alone is enough or a sub-soil drainage system is still
needed, using the risk of standing water and structural damage as the basis of the answer.

`ROW-058` may enter the same dialogue only with all of: a clear subtopic relationship; a second
coherent decision; a separate source trace; and a justification for why a retaining wall is
relevant to the same tension.

## 4. Exception classification

These three units are **not** `BARIAH_EXCEPTION`.

| Unit | Class |
|---|---|
| K5-PL06-T01-B03 | `INTERNAL_HUMAN_AUTHORING_REVIEW` |
| K5-PL06-T02-B01 | `CLOSED_BY_FIRDAUS_HUMAN_REVIEW` |
| K5-PL06-T02-B02 | `INTERNAL_SOURCE_SCOPE_REVIEW` |

Escalate to Bariah Ahmad only if a review leaves a source conflict, a real technical ambiguity,
an unsupportable claim, or a need for a character with different authority, licence or
competence.

## 5. Owner engineering authoring contract

These are the owner's mechanism decisions, not instructional decisions. They exist to make
E1 and E2 reachable; they carry no instructional authority of their own.

**Controlled paraphrase is permitted for natural dialogue.** A generated learner-facing line
may be `SOURCE_VERBATIM`, `CONTROLLED_PARAPHRASE` or `CAIR_STRUCTURAL_FRAME`. A paraphrase
must cite at least one controlled row of its own unit, must name the row it paraphrases, and
must not introduce an obligation, prohibition, approval or legal duty that its cited rows do
not carry. A structural frame makes no claim and so carries no source burden, but may name
only rows of its own unit.

**Analyst notes, reviewer annotations and unsupported claims are forbidden in learner-facing
dialogue.** An analyst note is written to explain to a reviewer why a row matters; it is not
something a character says.

**This contract does not apply to approved instructional copy.** Where the instructional
authority has written a dialogue and accepted it as-is, the copy is reproduced, not
regenerated. K5-PL06-T03-B03 S02 is such a case, accepted at C3.

## 6. Puan Nadia

| Field | Value |
|---|---|
| status | `UNRESOLVED_RECONCILIATION` |
| revocation | `NOT_EXPLICITLY_REVOKED` |
| activation | `NOT_AUTOMATICALLY_ACTIVE` |
| blocking | `NON_BLOCKING_WHILE_UNUSED` |

The name appears nowhere in the returned authority document — not in A1's cast table, not
among the replaced names, and not in Section G. Silence is not revocation and it is not
approval. She is not added to any active PL06 packet and is not removed from historical cast
evidence. If a future unit needs her, that is a fresh proposal to the instructional authority.
