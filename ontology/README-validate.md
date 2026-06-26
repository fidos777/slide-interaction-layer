# Ontology sidecar validator (`validate.py`)

A lightweight, **stdlib-only** Python 3 tool that checks each `*.ontology.json` sidecar against
[`schema.json`](schema.json) and confirms it **mirrors its HTML deck**. Read-only dev/CI tool — not
part of any deck's runtime, no npm/pip required.

## Usage

```bash
# validate one sidecar (deck derived from its `deck` field or <base>.html convention)
python3 ontology/validate.py examples/ai-workflow-for-smes.ontology.json

# pass the deck explicitly
python3 ontology/validate.py path/to/deck.ontology.json path/to/deck.html

# validate every sidecar in the repo (excludes ontology/test-fixtures/)
python3 ontology/validate.py --all
```

Run it **from the repository root**.

### Flags & exit codes
- `--all` — scan `**/*.ontology.json` (skips `ontology/test-fixtures/`).
- `--json` — machine-readable report.
- `--quiet` — print errors only.
- Exit `0` = all valid · `1` = errors found · `2` = usage error.

### Optional dependency
If the `jsonschema` package is installed, a full draft-2020-12 validation against `schema.json` runs
*in addition* to the built-in checks. If it's absent, the built-in checks (below) run alone —
**the tool never fails because a library is missing**.

## Checks (each finding cites its number)

**Schema / shape**
1. valid JSON object · 2. `sidecarVersion=="1.0"` + required keys · 3. no unknown keys ·
4. each slide has `index/element/objective/pattern/gating` · 5. `element` ∈ E1–E15 ·
6. `pattern` ∈ P0–P8 · 7. `objective` non-empty · 8. `gating` in enum · 9. `bloom`/`required` types (warn).

**Deck-mirror**
10. `slideCount` == deck `.slide` count · 11. `index` contiguous `1..N` · 12. element sequence ==
deck `element:` comments · 13. pattern sequence == deck `pattern:` comments · 14. `gatingMode` vs
deck `data-sil-gating` (warn).

**Ontology-rule**
15. mapping fidelity vs `element-to-pattern-map.md` (warn) · 16. `E13` must be `gating: none` (error).

**Errors block; warnings do not.**

## Test fixtures

`ontology/test-fixtures/` holds a deliberately broken sidecar + deck used to prove the validator
catches real problems. Fixtures are **excluded** from `--all` and from the release audit.

```bash
python3 ontology/validate.py ontology/test-fixtures/broken.ontology.json   # expect: fails, exit 1
```

## CI / RRI

The RRI release audit runs `python3 ontology/validate.py --all`; a non-zero exit is a release
**blocker** when sidecars exist. See [`../improvement/release-audit-checklist.md`](../improvement/release-audit-checklist.md).
