# Release audit checklist (HARD gate)

Mechanical pre-release safety. Formalizes what the `push-*.sh` scripts already enforce. **Any
blocker stops the release** (fail-closed). Tick every item before cutting a tag.

## Inputs
- The staged bundle + the new tag.
- The release type: **patch** (`0.0.x`) or **minor** (`0.x.0`).
- The previous tag (for the diff).

## Checks

### Integrity
- [ ] `git bundle verify` passes on the staged bundle.
- [ ] New tag present in the bundle; **all previous tags still present** (none dropped).
- [ ] `main` fast-forwards from the previous tag (no history rewrite).

### Cleanliness
- [ ] No stray files tracked: `ziIs4QgH`, `.DS_Store`, editor scratch.
- [ ] No nested archives tracked: `.zip`, `.bundle`, `.tar`, `.tgz`, `.gz`, `.7z`, `.rar`.
- [ ] No `node_modules/` tracked.

### Scope discipline (by release type)
- [ ] **Docs/patch release:** `components/`, `taxonomy/`, `gating/`, `ontology/` are **untouched**
      vs the previous tag.
- [ ] **Minor release:** only the intended new area changed; no taxonomy/ontology **ID** changes;
      core decks remain ungated by default.

### Consistency
- [ ] `.claude-plugin/plugin.json` version **equals** the new tag.
- [ ] `CHANGELOG.md` has an entry for the new version + compare links updated.
- [ ] All internal markdown links resolve (README, SKILL, MAINTAINER, docs, decisions, ontology,
      gating, improvement).
- [ ] `gating/gate.js` passes `node --check` (if present/changed).
- [ ] `python3 ontology/validate.py --all` exits `0` (if any `*.ontology.json` sidecars exist).
      Errors are a release **blocker**; warnings are advisory.

### Examples
- [ ] Each example deck opens; its interactions fire (verified, not assumed).
- [ ] Gated example: forward nav blocks until complete, backward always works.

## Output
Record **PASS / FAIL** with a findings list. On any FAIL → fix, re-stage, re-run. Do not proceed to
the push script until PASS.
