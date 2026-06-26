# Ontology mapping verifier

Keeps the Element Ontology internally consistent as it grows. Run during the **VERIFY** step of the
pre-release gate when `ontology/` changed (or any release that touches mappings).

## Checks

- [ ] **Element IDs unique** — `E1`–`E15` each defined exactly once in `ontology/element-ontology.md`.
- [ ] **No E/P collision** — no element ID equals a pattern ID (distinct prefixes `E` vs `P`).
- [ ] **Pattern refs valid** — every `P<n>` referenced in `ontology/element-to-pattern-map.md` is
      within `P0`–`P8` (the taxonomy's defined range).
- [ ] **Full coverage** — every element has a **primary** pattern in the map.
- [ ] **No orphan mappings** — the map references only elements that exist in the catalog.
- [ ] **Gating table complete** — every gateable element appears in the gating-justification table
      with a stance (justified / conditional / never-gate).
- [ ] **Critical rule intact** — `E13` (Warning) is marked never-gate / never-hide.

## Suggested manual commands (read-only)

```bash
# distinct element IDs defined (expect 15)
grep -oE '^## E([1-9]|1[0-5])\b' ontology/element-ontology.md | sort -u | wc -l
# any invalid pattern reference in the map (expect empty)
grep -oE '\bP[0-9]+\b' ontology/element-to-pattern-map.md | sort -u | grep -vE '^P[0-8]$'
```

## Optional: validate the sidecar (if present)

If a deck ships a `<deck>.ontology.json` sidecar, also validate it against
[`../ontology/schema.json`](../ontology/schema.json): valid `E1`–`E15` / `P0`–`P8`, `objective` and
`gating` present, `slideCount` == the deck's `.slide` count, and `index` contiguous `1..slideCount`.
(A standalone validator CLI is planned for v0.5.1; until then use any JSON Schema draft 2020-12 tool.)

## Output
PASS / FAIL + the offending IDs. A FAIL is a **blocker** for any release that changed the ontology.
