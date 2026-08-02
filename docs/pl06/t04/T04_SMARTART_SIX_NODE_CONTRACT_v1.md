# T04_SMARTART_SIX_NODE_CONTRACT — v1

Stage 4.2F-B0.5. Generated from `docs/pl06/t04/tools/t04_pack_emit_v1.py`.

```
ASSET  = T04-DGM-01
NODES  = 6
FLOW   = LINEAR_LEFT_TO_RIGHT
HIERARCHY = NONE
SMARTART_TREATMENT_STATUS = PENDING_BARIAH_REVIEW
```

> **Every proposal below is `CAIR_ASSISTED_DRAFT` / `PENDING_BARIAH_REVIEW`.** Bariah is the sole Instructional Designer and the only approval authority. CAIR prepared the source analysis, the mapping and the drafts; none of it is approved instructional content and none of it may be treated as an ID decision.

# 1. Asset identity

| field | value |
|---|---|
| asset_id | `T04-DGM-01` |
| SHA-256 | `f88edf2d305a546dfd05e45b9306503fbe7963bdd7ea1bcfe1ff9d74a1516e43` |
| relationship IDs | `dm=rId64,lo=rId65,qs=rId66,cs=rId67` |
| embedded part | `word/diagrams/data1.xml` |
| source page | modul ms 276 |
| source paragraph | 5223 |
| source row | `T04-ROW-003` |
| original dimensions | 6.79 x 3.92 in |
| caption | NONE — the diagram carries no caption in the source |
| source authority | MODULE_SOURCE_ATTESTED |

# 2. The six nodes, in source order

| # | raw node text |
|---|---|
| 1 | Koordinasi dan Demonstrasi Penyelenggaraan Taman |
| 2 | Penyeliaan Penyelenggaraan Taman |
| 3 | Penyeliaan Operasi Nurseri |
| 4 | Penyeliaan Alatan dan Mesin Penyelenggaraan Taman |
| 5 | Penyeliaan Inventori Taman |
| 6 | Perancangan Sumber Manusia dan Kebajikan Pekerja |

| property | measured value |
|---|---|
| node sequence | document order in word/diagrams/data1.xml, preserved exactly |
| directional flow | **LINEAR_LEFT_TO_RIGHT** |
| flow evidence | layout1.xml declares urn:microsoft.com/office/officeart/2005/8/layout/process2 with algorithms lin (linear) and conn (connector) |
| connectors | 6 sibTrans sibling transitions — the connectors a process2 layout draws between consecutive nodes |
| hierarchy | **NONE — flat. All six nodes are parOf the single doc root; zero parOf links exist between text nodes, so no node is subordinate to another.** |

The flat structure matters: nothing in the source subordinates one activity to another, so a redraw must not introduce a tree, a cycle or a grouping.

# 3. Treatment A — review storyboard

| field | value |
|---|---|
| approach | SOURCE_BOUND_DIAGRAM_REFERENCE |
| asset production | NOT_STARTED |

- reference T04-DGM-01 by asset id and SHA-256
- render either a controlled redraw or a readable placeholder carrying all six labels
- no invented nodes
- no reordered nodes
- no altered meaning
- the six labels must be reachable as text

# 4. Treatment B — future MMD

| field | value |
|---|---|
| approach | CONTROLLED_REDRAW |
| asset production | NOT_STARTED_IN_THIS_STAGE |

- redraw as a controlled process diagram
- preserve the six-node sequence exactly
- preserve the linear directional relationship
- no hierarchy may be introduced — the source has none

```
SMARTART_TREATMENT_STATUS = PENDING_BARIAH_REVIEW
```
