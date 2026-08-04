# -*- coding: utf-8 -*-
"""Immutability guard for historical run reports.

    python3 docs/source/tools/src_historical_freeze_v1.py       # audit only

WHY THIS EXISTS
---------------
Stage 4.2F-E rewrote three Stage 4.2F-D reports. Not maliciously and not by hand — the
Stage-D emitters were simply re-run, because a Stage-D gate had been legitimately renamed
and re-running the emitter looked like keeping things tidy. The result was that a report
describing what Stage D found silently started describing what Stage E found.

A run report is evidence of what was true at a moment. Regenerating it destroys the only
record of the earlier state and makes every later claim unfalsifiable. Live protections
may evolve through new commits; the report of a finished stage may not.

The frozen hashes below are the bytes as committed at the end of Stage 4.2F-D (b603f44).
Any emitter that would write one of these paths must call `guard()` first and honour a
refusal. `audit()` reports drift without changing anything.
"""
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.dirname(HERE)

# path -> (sha256 as committed, the commit that froze it, the stage it belongs to)
FROZEN = {
    "STAGE_4_2F_D_QA_REPORT_v1.md":
        ("c99d2693fc781e4988662865e0869582f11a4106909dab400364fc321503c043",
         "b603f44", "4.2F-D"),
    "STAGE_4_2F_D_QA_REPORT_v1.json":
        ("67d5fbd80c46b8b48c876be1902119c37dae01183e4ae3e2a159f9458ebe53c3",
         "b603f44", "4.2F-D"),
    "STAGE_4_2F_D_MUTATION_REPORT_v1.md":
        ("c4074766aeb7553285fc2fe5f4fc91e53e7a0bb94a678cad61a625e9367a0708",
         "b603f44", "4.2F-D"),
    "STAGE_4_2F_D_RUN_MANIFEST.md":
        ("2fa3252284b1ac2299b707aecc484a4b60aedcbe31856026c85395753c591689",
         "b603f44", "4.2F-D"),
}

# Every frozen path is enforced. There is no partially-protected tier: a report is either
# a finished stage's evidence or it is not.
ENFORCED = sorted(FROZEN)


def _sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


class HistoricalReportFrozen(RuntimeError):
    """Raised when a generator tries to overwrite a finished stage's report."""


def guard(filename):
    """Call before writing. Raises if `filename` is a frozen historical report.

    A generator that legitimately produces a NEW report is unaffected: only the exact
    paths in FROZEN are protected, and only while they still hold their frozen bytes.
    """
    if filename not in ENFORCED:
        return True
    path = os.path.join(SRC_DIR, filename)
    if not os.path.exists(path):
        return True
    sha, commit, stage = FROZEN[filename]
    if _sha256(path) == sha:
        raise HistoricalReportFrozen(
            f"{filename} is the Stage {stage} run report, frozen at {commit}. It records "
            f"what that stage found and must not be regenerated. Write a new "
            f"stage-specific report instead, and record any supersession in an addendum.")
    return True


def audit():
    rows = []
    for name, (sha, commit, stage) in sorted(FROZEN.items()):
        path = os.path.join(SRC_DIR, name)
        exists = os.path.exists(path)
        actual = _sha256(path) if exists else None
        rows.append(dict(artifact=name, stage=stage, frozen_at=commit,
                         enforced=name in ENFORCED, exists=exists,
                         frozen_sha256=sha, actual_sha256=actual,
                         intact=(actual == sha) if exists else None))
    return dict(total=len(rows), enforced=len(ENFORCED),
                intact=[r["artifact"] for r in rows if r["intact"]],
                drifted=[r["artifact"] for r in rows
                         if r["exists"] and r["intact"] is False and r["enforced"]],
                rows=rows)


if __name__ == "__main__":
    a = audit()
    print(f"frozen artifacts: {a['total']} ({a['enforced']} enforced)")
    for r in a["rows"]:
        mark = "intact" if r["intact"] else ("DRIFTED" if r["exists"] else "absent")
        if not r["enforced"]:
            mark += " (not enforced — hash not recorded from disk)"
        print(f"  {r['artifact']:<40} {mark}")
    sys.exit(1 if a["drifted"] else 0)
