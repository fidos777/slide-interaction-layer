# PL06_EXECUTION_PLAN — v1

Stage 4.2F-A. Generated from `docs/pl06/tools/pl06_emit_v1.py`.

```
WAVE_0_UNITS = 1
WAVE_1_UNITS = 0
WAVE_2_UNITS = 0
WAVE_3_UNITS = 0
HELD_UNITS = 12
WAVE_0_WORKING_TIME = 2h46m
```

> Waves 1, 2 and 3 are empty and that is the honest state. A unit cannot be placed in a lane before its source is read, so every remaining unit sits on Hold and the plan below is a plan for **one** unit plus a source-delivery request.

# 1. Duration basis

Every figure in this plan is either measured in this repository or marked `NOT_EVIDENCED`. Nothing is estimated from experience.

| metric | value | basis |
|---|---|---|
| source acquisition to bound asset manifest | **25m** | commit history 31 Jul 04:07 (intake BLOCKED) to 04:32 (14 assets extracted) |
| controlled model to first complete generated deck | **1h41m** | commit history 1 Aug 05:02 (freeze inputs) to 06:43 (regenerate complete v0.4) |
| ingest to first storyboard, whole first block | **3h18m** | commit history 31 Jul 01:39 to 04:57 |
| a full governance correction stage | **42m** | commit history 2 Aug 01:37 to 02:19, Stage 4.2E-C |
| generate 100-page deck | **under 5s** | timed, Stage 4.2E-C |
| full QA suite, 461 gate records | **5s** | timed, Stage 4.2E-C |
| mutation replay, 51 fixtures + 5 historical decks | **3m20s** | timed, Stage 4.2E-C |
| render and inspect 100 pages | **25s** | timed, Stage 4.2E-C |
| Bariah review turnaround | **14h15m mean of two** | commit history: 31 Jul 14:34 to 1 Aug 05:02 (14h28m); 1 Aug 11:36 to 2 Aug 01:37 (14h01m). CALENDAR time, not working time. |
| Microsoft PowerPoint smoke | **NOT_EVIDENCED** | never executed in this environment |

# 2. Waves

| wave | title | units | entry condition |
|---|---|---|---|
| Wave 0 | First non-B02 proof | `K5-PL06-T04-B01` | PRE-03 through PRE-06 satisfied. PRE-01 and PRE-02 closed by the Stage 4.2F-A2 source ingest. |
| Wave 1 | Lane A units | — | a unit is Lane A only once its content is extracted and its structure matches an already-supported pattern. No unit qualifies yet. |
| Wave 2 | Lane B units | — | content extracted, treatment portable with per-unit binding. None yet. |
| Wave 3 | Lane C units after human ruling | — | new treatment or Bariah ruling obtained. None yet. |
| Hold | Lane D units | `K5-PL06-T01-B01`, `K5-PL06-T01-B02`, `K5-PL06-T01-B03`, `K5-PL06-T02-B01`, `K5-PL06-T02-B02`, `K5-PL06-T03-B01`, `K5-PL06-T03-B03`, `K5-PL06-T03-B04`, `K5-PL06-T03-B05`, `K5-PL06-T05-B01`, `K5-PL06-T06-B01`, `K5-PL06-T07-B01` | held until content extraction, which is now unblocked for every one of them — the source and the boundaries are in custody |

# 3. Per-unit plan

| unit_id | wave | owner | deps | source | model | gen | QA | render | smoke | Bariah | output | blocker |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `K5-PL06-T04-B01` | Wave 0 | CC | PRE-03, PRE-04, PRE-05, PRE-06 | 25m | 1h41m | 5m | 5m | 30m | NOT_EVIDENCED | 14h15m calendar | v0.1 review candidate | STOP-003, STOP-004, STOP-005, STOP-006 |
| `K5-PL06-T01-B01` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T01-B02` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T01-B03` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T02-B01` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T02-B02` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T03-B01` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T03-B03` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T03-B04` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T03-B05` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T05-B01` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T06-B01` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |
| `K5-PL06-T07-B01` | Hold | CC — after the Wave 0 proof | STOP-003, STOP-004, STOP-005, STOP-006 | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | NOT_EVIDENCED | none | content not extracted |

# 4. Wave 0 total

**2h46m of working time.** Basis: 25m source extraction + 1h41m controlled model + 5m generation + 5m automated QA + 30m rendered inspection. Every component is a measured B02 figure. PowerPoint smoke is excluded because it has never been run and no honest number exists for it.

The Bariah review turnaround measured twice at a mean of **14h15m calendar** is excluded — it is not our time to spend and it is not working hours.

# 5. The critical path is not ours

Wave 0's working time is under three hours. It has been blocked for the entire life of this project on one thing: **a module extract that is not in the repository.** The same blocker held B02 up at its intake gate on 31 July until the source arrived by Drive, at which point the whole first block took 3h18m end to end.

The highest-value action available today is not engineering. It is asking for the Topik 4 page range and the Bahagian list.
