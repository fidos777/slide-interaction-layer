# SBAT-ADR-003 — Ratify M1 Scope Expansion to Review-First Multi-View Prototype

- **Status:** Accepted
- **Date:** 2026-06-27

## Context

- Original M1 / Screen C was framed as a **one-slide authoring surface**.
- The actual shipped M1 became a **review-first multi-view prototype**.
- This includes: MMD Readiness Dashboard, Asset Requirement View, Slide Review, WYSIWYG-lite Slide Mock Preview, "Can MMD proceed?" decision gate, Reviewer Decision Panel, Print / Save PDF handoff, a demo checklist, and Vercel deployment.
- This is a **scope expansion** relative to the original framing and must be recorded explicitly rather than left as undocumented scope drift.

## Decision

- **Ratify M1 as a review-first multi-view prototype** for Bariah / Laila validation.
- Treat M1 as **pilot validation tooling, not final product scope**.
- Preserve the **authoring concept as a later track**, not as a completed M1 claim.

## Rationale

- The 3-record pilot needed a **review workflow** to validate real SB → MMD planning.
- The pilot records represent three major issue classes: **character blocker** (PL1T3), **quiz blocker** (PL3T1), and **asset / interactivity review** (PL5T3).
- Review-first is currently **higher-value** because the immediate Cycle 7 problem is **deciding what can proceed to MMD**, not authoring new slides.

## Non-goals

- No importer.
- No database.
- No auth.
- No persistence.
- No SCORM builder.
- No full WYSIWYG / canvas authoring.
- No bulk data ingestion.
- No claim that all CIDB records are loaded.
- No claim that reviewer panel decisions are persisted or are authoritative approvals.

## Governance invariants

- **AI suggests; humans ratify.**
- **Confirmed-from-file** means the source text was found, **not** that amendment is completed.
- **REVIEW is a valid state** — uncertainty is not forced into a block or an approval.
- **PL5T3 s4 remains `REVIEW`, not `BLOCKED_PENDING_ASSET`.**
- **Production notes and governance blockers must remain distinguishable.**

## Consequences

- M1 can be shared as a **review-first pilot**, not as final SBAT.
- **M2 must begin with schema and source-lane discipline** before importing more records.
- Any future expansion must have an **explicit ADR or scoped sprint note**.

## Verification

- See the verification evidence file created in this sprint: [`sbat/M1_GOVERNANCE_VERIFICATION.md`](../sbat/M1_GOVERNANCE_VERIFICATION.md).
- Related prior decisions: [`decisions/SBAT-ADR-001.md`](SBAT-ADR-001.md), [`decisions/SBAT-ADR-002.md`](SBAT-ADR-002.md).
