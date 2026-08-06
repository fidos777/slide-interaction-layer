# -*- coding: utf-8 -*-
"""Lane O — shared canonical hashing and run-metadata capture.

This module is the ONE place the two pre-refactor oracles (A1, A2) canonicalise
and hash their record payloads, so both lanes agree byte-for-byte on the recipe.

CANONICAL HASHING CONTRACT
--------------------------
Reproduced verbatim from the binding block in
    docs/pl06/tools/k5_treatment_resolver_v1.py
    ("CANONICAL HASHING (both pre-refactor oracles and any frozen baseline here)")

    payload_bytes    = json.dumps(records, sort_keys=True,
                                  separators=(",", ":")).encode("utf-8")
    canonical_sha256 = sha256(payload_bytes).hexdigest()

Rules carried over from that contract:
  * Hash the RECORDS payload ONLY — never metadata that carries the hash itself.
  * Default JSON separators are forbidden; the compact separators above are used
    so two runs cannot disagree over whitespace and read as content drift.
  * `ensure_ascii` is left at its default (True). The recipe names no override,
    so none is applied here — the non-ASCII Malay text is escaped consistently.
  * The serialization string is recorded verbatim in every baseline (SERIALIZATION).

METADATA IS CAPTURED, NEVER TYPED
---------------------------------
`execution_commit` and any git blob id are read from command output at run time
(`git rev-parse HEAD`, `git hash-object <path>`). Nothing here hard-codes an
expected SHA, blob, count or path into the generated baseline.
"""
import hashlib
import json
import os
import subprocess

# The serialization recipe, recorded verbatim in each baseline's metadata.
SERIALIZATION = ('json.dumps(records, sort_keys=True, separators=(",", ":"))'
                 '.encode("utf-8")')


def canonical_bytes(records):
    """The exact payload bytes the contract hashes. Records payload only."""
    return json.dumps(records, sort_keys=True, separators=(",", ":")).encode("utf-8")


def canonical_sha256(records):
    """sha256 hexdigest of the canonical record payload."""
    return hashlib.sha256(canonical_bytes(records)).hexdigest()


# ---------------------------------------------------------------- git capture ---
def _git(args, repo):
    """Run a git command in `repo` and return its single-line stdout, verbatim."""
    out = subprocess.check_output(["git", "-C", repo] + args)
    return out.decode("utf-8").strip()


def execution_commit(repo):
    """OBSERVED: the HEAD the capture ran against — `git rev-parse HEAD`."""
    return _git(["rev-parse", "HEAD"], repo)


def blob_sha1(repo, path_rel):
    """OBSERVED: git blob id of a tracked file — `git hash-object <path>`.

    `path_rel` is relative to `repo`. This is the object git already stores, so
    a later `git hash-object` on the same bytes reproduces it exactly.
    """
    return _git(["hash-object", path_rel], repo)


def repo_root(start):
    """The worktree root that owns `start` — `git rev-parse --show-toplevel`."""
    return _git(["rev-parse", "--show-toplevel"], start)


def write_json(path, obj):
    """Write a baseline artifact. File formatting never feeds the canonical hash;
    it is `sort_keys`-stable and UTF-8 readable for review only."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
