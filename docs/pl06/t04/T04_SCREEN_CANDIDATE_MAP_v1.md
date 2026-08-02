# T04_SCREEN_CANDIDATE_MAP — v1

Stage 4.2F-B0. Generated from `docs/pl06/t04/tools/t04_emit_v1.py`.

```
CANDIDATES = 6
NEW_TREATMENT_REQUIRED = 2
PENDING_HUMAN = 1
B02_FAMILIES_PROPAGATED = 0
```

> **These are candidates, not a design.** Every one names the source rows it rests on. None imports FAMILY_S, FAMILY_P1, FAMILY_P2, a B02 cardinality, the Papan Tanda or BBQ Pit rulings, a B02 learner-screen count, or Alya and Encik Rahman.

# Candidates

## `T04-SC-01` — PROCESS_FLOW: Aliran proses penjagaan dan penyelenggaraan

| field | value |
|---|---|
| source rows | `T04-ROW-003`, `T04-ROW-002` |
| reason | The unit opens with a sentence introducing a process flow and a SmartArt diagram carrying six named nodes. The flow is source-drawn, not inferred. |
| reusable capability | the B02 shell, Notes schema and production panel carry it; the six nodes are source-bound subjects |
| new treatment required | **YES — B02 has no process-flow screen type. Its visual treatment is a source-bound overview of PHOTOGRAPHS; this is a vector diagram with ordered nodes.** |
| human decision required | how a SmartArt diagram is rendered for MMD — re-drawn, exported, or rebuilt as six sequential reveals |
| visual dependency | T04-DGM-01 — the only visual in the unit |
| narration dependency | one screen-level VO; the six node labels are the spoken spine |

## `T04-SC-02` — CLICK_TO_REVEAL: Landskap Lembut — tiga operasi penyelenggaraan

| field | value |
|---|---|
| source rows | `T04-ROW-004`, `T04-ROW-005`, `T04-ROW-006` |
| reason | Landskap Lembut decomposes into exactly three named operations — Siram, Baja, Racun — each with its own definition, Kaedah Pelaksanaan and Aspek Pengurusan untuk Kontraktor. Three peers with parallel internal structure is the shape a reveal pattern fits. |
| reusable capability | completion-state treatment, all-viewed state, screen-level VO |
| new treatment required | **NO — structurally similar to a B02 selection screen, but the similarity must be re-derived, not imported** |
| human decision required | whether three items warrant a selection screen or read better as three sequential screens |
| visual dependency | NONE — no source visual exists for Siram, Baja or Racun |
| narration dependency | screen-level 'Klik pada setiap …' instruction if reveal is chosen |

## `T04-SC-03` — SEQUENTIAL_STEPS: Racun — Perundangan, HSE dan Pengurusan Risiko

| field | value |
|---|---|
| source rows | `T04-ROW-066`, `T04-ROW-067`, `T04-ROW-069`, `T04-ROW-071`, `T04-ROW-073`, `T04-ROW-076` |
| reason | The Racun subsection carries the unit's entire compliance load — statute, licensing, PPE, storage, SDS, spray conditions, reporting. It is ordered obligation, not a menu. |
| reusable capability | Notes typed-block schema; production-instruction blocks |
| new treatment required | **NO** |
| human decision required | whether legislative content may be reveal-gated at all, or must be shown in full — a compliance question, not a design one |
| visual dependency | NONE |
| narration dependency | high — this is the material a learner is most likely to be assessed on |

## `T04-SC-04` — COMPARISON: Landskap Lembut vs Landskap Kejur

| field | value |
|---|---|
| source rows | `T04-ROW-004`, `T04-ROW-079` |
| reason | The unit is built on exactly two Heading-2 blocks that are explicit counterparts — living horticultural elements against permanent built elements. The source itself frames the second as contrast to the first ('Elemen kejur memberikan kontras yang menarik kepada kelembutan elemen tumbuhan'). |
| reusable capability | shell and Notes only |
| new treatment required | **YES — B02 has no comparison screen type** |
| human decision required | whether to spend a screen on the contrast or let the two sections stand alone |
| visual dependency | NONE |
| narration dependency | low |

## `T04-SC-05` — CLICK_TO_REVEAL: Landskap Kejur — empat kumpulan fungsi

| field | value |
|---|---|
| source rows | `T04-ROW-081`, `T04-ROW-082`, `T04-ROW-084`, `T04-ROW-086` |
| reason | Landskap Kejur decomposes into four function groups — Pengurusan Ruang dan Sirkulasi, Fungsi Struktur dan Kejuruteraan, Kebolehgunaan dan Kemudahan, Estetika dan Reka Bentuk — each with exactly two sub-items. |
| reusable capability | completion-state treatment, all-viewed state |
| new treatment required | **NO** |
| human decision required | none anticipated |
| visual dependency | NONE — and this is the finding that matters most for portability |
| narration dependency | screen-level instruction |

## `T04-SC-06` — PENDING_HUMAN: Rumusan and quiz screens

| field | value |
|---|---|
| source rows | **none** |
| reason | The module contains no Rumusan and no assessment items, for this unit or any other. Both screens exist in the B02 shell and have no source to fill them. |
| reusable capability | the Rumusan and quiz-review STRUCTURES are portable (RP-007, RP-008, RP-011) |
| new treatment required | **NO — the structures exist** |
| human decision required | REQUIRED — the CONTENT must be authored and signed off, and the 4+1 composition and 60% threshold must be confirmed as PL06-wide rather than B02-specific |
| visual dependency | NONE |
| narration dependency | follows the authored content |

# The portability finding

**Five of six candidates have no visual dependency at all, because the unit has no photographs.** T04 contains exactly one visual — the opening SmartArt process diagram — against B02's fourteen extracted assets.

That single fact is the most useful thing this stage produced. B02's component-main treatment is a *source-bound overview of photographs*; it was ruled by Bariah on a unit that had photographs to bind. T04 has none. Applying the same treatment here would require inventing subjects, which is prohibited — so RP-101 arrives with nothing to bind to, and that needs a human ruling rather than a default.
