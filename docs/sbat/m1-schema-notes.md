# SBAT M1 — schema notes (the six governance fields)

> **Notes, not a schema.** This is a draft governance *contract* in prose for the six M1 fields
> (ADR Decision 6). It is intentionally **not** a JSON Schema and introduces no code. The contract is
> **CIDB-agnostic** — it describes governance shape only; any CIDB names below are illustration, not
> structure to import. A real `sbat.schema.json` is deferred until explicitly approved.

Scope: one slide (M1), end-to-end, through Screen C. Nothing here scales beyond one slide yet.

## 1. Slide implementation status
Tracks whether a slide exists across the four places it can exist, so scope can never silently drift.
- `storyboard_present` — the slide exists in approved storyboard evidence.
- `implemented_in_repo` — a corresponding implementation exists downstream.
- `in_navigation` — present in the navigation order.
- `declared_in_scope` — counted in the declared scope total.
- Derived: `status` ∈ { complete · missing-impl · missing-nav · scope-mismatch }.

## 2. Interaction pattern
The chosen pattern for the slide, drawn from the repo's existing vocabulary — SBAT selects, it does
not invent patterns.
- `pattern` ∈ the ADR's M1 set: static · video · visited-gate menu · popup modal · subtopic detail ·
  drag-drop · quiz single · quiz multi · end screen.
- Note: this list is the ADR's M1 governance vocabulary; the repo's own taxonomy IDs (P0–P11) are the
  build-layer mapping and are referenced, not redefined, here.

## 3. Source-backed content flag
Every content unit must declare provenance — this is the core anti-fabrication check.
- `source` ∈ { SB-sourced · ID-approved · AI-suggested · repo-existing · needs-review }.
- Rule: AI-suggested or needs-review content may be **reported** but not committed as fact without a
  human-ratified source.

## 4. Quiz option governance
Per quiz option, not per question — the Q2 case proved option-level granularity is required.
- `option_id` · `text` · `is_correct` (bool) · `source` (as in field 3) ·
  `risk` ∈ { valid-distractor · fabricated · misleading · pending }.
- Rule: a *plausible* distractor is not automatically acceptable; it must be source-backed or flagged.

## 5. Repo patch preview
Changes are shown as a diff before any commit — never edited silently.
- `diff` shows `- old` / `+ new` for the single field being changed.
- Rule: minimal/limited edit only; one governed field at a time.

## 6. Human decision gate
The terminal state of a finding is a human decision, never an automated close.
- `decision` ∈ { REPORT_ONLY · READY_TO_PATCH · PATCHED_NOT_COMMITTED · COMMITTED ·
  BLOCKED_PENDING_SB · BLOCKED_PENDING_ASSET }.
- Rule: final fact/quiz/interaction ratification is human (Bariah / Laila / ID). AI never closes a
  finding by edit.

## Field relationships (governance flow, not code)
```
status (1) + pattern (2) + source (3) + quiz governance (4)
        → patch preview (5)
        → human decision gate (6)
```
Open decisions intentionally deferred: exact field names/keys, JSON encoding, enums-as-strings vs
codes, and whether a machine-readable schema is warranted. None are decided here.
