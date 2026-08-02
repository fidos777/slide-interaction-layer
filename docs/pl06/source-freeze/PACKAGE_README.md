# PL06 Source and Boundary Evidence Freeze v1

This package freezes the full module source and the derived PL06 lesson-boundary evidence used for the remaining storyboard scale-out.

## Verify

From the package root:

```bash
./tools/verify_freeze.sh
```

Expected result:

```text
PASS <count>/<count> artifacts verified
```

## Authority model

- `source/` contains the byte-identical primary DOCX.
- `derived/` contains reproducible render and boundary evidence.
- `records/` contains custody, scope and hash records.
- Derived evidence does not supersede or replace the primary source.

## Closed by this freeze

- Full module source custody
- PL06 source span
- Seven Topik
- Fourteen lesson-unit boundary map
- Shared-page heading-anchor requirements
- T04-B01 source boundary

## Still open

- T04 controlled content extraction
- T04 visual inventory
- T04 Rumusan and quiz completeness
- T04 interaction treatment
- Storyboard generation
- PowerPoint smoke
- MMD, React and SCORM work
