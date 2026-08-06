# Lane O — pre-refactor oracles (A1, A2)

Frozen baselines captured **before** the 0a/0b/0c refactor, so that refactor can be
checked against what the generators produce today. Nothing here changes production
behaviour, touches PPTX, refreezes a golden map, or clears `MID_MIGRATION`.

- **Captured at (BASE):** `ebd6d81cf9c3b9e842d01d0b571ee16e32b5fb18`
- **Worktree branch:** `cc/pl06-oracles`
- Every SHA, blob, count and path below was **captured from command output**, never
  typed. Where a value is a pinned expectation it is labelled **TARGET** and the gate
  checks it against a freshly **OBSERVED** command.

## Canonical hashing (binding on both oracles)

Reproduced verbatim from the `CANONICAL HASHING` block in
`docs/pl06/tools/k5_treatment_resolver_v1.py`:

```
payload_bytes    = json.dumps(records, sort_keys=True, separators=(",", ":")).encode("utf-8")
canonical_sha256 = sha256(payload_bytes).hexdigest()
```

The **records payload only** is hashed — never the metadata that carries the hash.
Default separators are forbidden. The recipe string is stored verbatim in each
baseline as `serialization`. The one implementation lives in `lane_o_canonical_v1.py`.

## A1 — the 11 non-B03 packet interaction records

The current packet population is "ONE interaction record per active unit"
(`k5_treatment_resolver_v1.py`, POST-0A PARITY block). A1 freezes those records with
the calibrated B03 unit removed — B03 is frozen instead by A2.

| field (OBSERVED, captured) | value |
|---|---|
| `execution_commit` | `ebd6d81cf9c3b9e842d01d0b571ee16e32b5fb18` |
| `controlling_module` | `docs/pl06/tools/pl06_packet_model_v1.py` |
| `controlling_module_blob_sha1` | `a4e6db69e08f93f3151fe4166d17c6d481765e8f` |
| `record_count` | `11` |
| `canonical_sha256` | `e827a996f81f74f8cebc6d608baa0dc41bd23b205490a827bca14dc5c373623b` |
| `source_docx_sha256` | `5a9142cdfa1a8090c2075e78caf45609438844daeac88e331bed3069a6a78df7` |

- **Baseline:** `A1_packet_interaction_oracle_v1.json`
- **Capture:** `A1_packet_interaction_oracle_capture_v1.py`
- Rebuilding A1 (and the gate's live-parity check) needs the K5 module DOCX, resolved
  by `PL06_MODULE_DOCX` (search order in `docs/source/tools/src_authority_v1.py`).
  Its identity is asserted against `source_docx_sha256`.

## A2 — the six B03 content groups

The current calibration population is "six B03 content groups". A2 derives them
**directly from the controlled extract** — `docs/pl06/batch1_extract/K5_PL06_T03_B03_SOURCE_EXTRACT_v1.json`
— using source-order boundaries and the parent/head relationship. It records each
group's full row span, its `left`/`right` neighbouring exclusions, the parent
`HEADING_2`, and the marker row. **It does not call `k5_calib_model_v1.screens()`**;
the group rule is inlined in the capture (independent second reading).

| field (OBSERVED, captured) | value |
|---|---|
| `execution_commit` | `ebd6d81cf9c3b9e842d01d0b571ee16e32b5fb18` |
| `controlling_extract` | `docs/pl06/batch1_extract/K5_PL06_T03_B03_SOURCE_EXTRACT_v1.json` |
| `extract_blob_sha1` | `e4049c6bcf6daad667b8a32786a8b92ca960376a` |
| `group_count` | `6` |
| `parent_row` | `T03B03-ROW-001` (`Infrastruktur`, HEADING_2) |
| `canonical_sha256` | `2c4ded4e23586e54a4d2b670d36544a6ff15ea386436de3094f2885c9e2f774a` |

Groups G1..G6 and their spans (ROW-002..ROW-076 tile the unit disjointly after the
parent): G1 `Landform / Earthmound` ROW-002..015 · G2 `Sub soil drainage` ROW-016..031
· G3 `Dinding Penahan (Retaining Wall)` ROW-032..041 · G4 `Fencing` ROW-042..054 ·
G5 `Swale/ Natural Drain` ROW-055..063 · G6 `Jalan akses` ROW-064..076.

- **Baseline:** `A2_b03_group_source_oracle_v1.json`
- **Capture:** `A2_b03_group_source_oracle_capture_v1.py`
- Self-contained: rebuild and gate need no external DOCX.

## Gate and biting fixtures

`lane_o_oracle_gates_v1.py` re-derives each oracle, asserts it still matches the
committed baseline, and runs fixtures that each apply **one** mutation and require the
canonical hash to **move** (a fixture that did not bite would be vacuous):

- **A1:** integrity · record_count · B03 absent · TARGET base-commit & module-blob vs
  OBSERVED · live re-derivation parity (when the DOCX is present) · single-field-edit
  bite (with an unmutated control that must still match).
- **A2:** integrity · re-derivation parity · six distinct G1..G6 · parent/head relation
  · disjoint tiling · TARGET base-commit & extract-blob vs OBSERVED · five bites —
  **missing group**, **duplicate id**, **reordered row**, **missing head**,
  **neighbouring-row leakage**.

```
# with the module DOCX (full A1 live parity): 21/21
PL06_MODULE_DOCX="…/[PROOFREAD FINAL] SKP 2025 PEMBINAAN LANDSKAP LUAR 300426.docx" \
  python3 docs/pl06/oracles/lane_o_oracle_gates_v1.py
# without it (A1 live parity skips): 19/19
python3 docs/pl06/oracles/lane_o_oracle_gates_v1.py
```

Green prints `ALL_LANE_O_CHECKS_PASS` and exits 0.
