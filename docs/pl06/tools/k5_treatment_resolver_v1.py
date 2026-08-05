# -*- coding: utf-8 -*-
"""Stage 4.2F-K — the ONE treatment resolver, shared by the packet and calibration lanes.

Two independent decision paths are how this deck ended up with two dialogues: the packet
lane held the approved copy while the calibration lane, which emits the artifact Bariah
receives, quietly drafted its own. The same shape was live for interaction treatment —
`pl06_packet_model_v1` applied F3 per unit while `k5_calib_model_v1` applied one global
`screen_pattern_plan["primary"]` to every content group, leaving Sub-soil Drainage on
click-to-reveal against F4(a).

INCOMPLETE AS OF 2026-08-05 (f082dd2). Only `k5_calib_model_v1` calls this module. The
packet lane still runs its own `_f3_select`, so there are still two evidence-to-treatment
paths joined at a shared final mapping — which is weaker than it looks: a parity gate built
on the current API would compare two independent classifications that agree only because the
last step is shared. The final API must be `resolve_for_group(unit_id, screen_name,
controlled_group_evidence)` with F3 evidence classification INSIDE this module and no
caller-supplied `f3_case`.

    F4 override   a screen the authority named explicitly wins outright
    F3 fallback   everything else is selected from the module's own structure

POST-0A PARITY POPULATION TARGET (binding on the 0c gate and its fixtures)
--------------------------------------------------------------------------
SUPERSEDES_THE_PRESENT_TENSE_PARITY_POPULATION_CLAIM_IN_ba73600.

The ba73600 revision of this block stated five populations in the present tense,
as though both six-record populations already existed. They do not. At the
current commit:

    current packet population      = ONE interaction record per active unit
    current calibration population = six B03 content groups

The packet lane has no group-level treatment decision at all, so there is nothing
on that side to compare six-to-six with until 0a creates it. The six-and-six
figures below are a TARGET the refactor must produce, not a description of today.

    future packet population       = six canonical B03 group evidence records
    future calibration population  = six canonical B03 group evidence records

The shared constructor is NOT the parity population. Each lane must independently
supply its own raw adapter inputs; the comparison population is the six canonical
evidence records produced from those two independently supplied input sets.

An evidence-parity fixture MUST mutate exactly one lane BEFORE shared
canonicalisation. It must NOT mutate the shared constructor, the shared resolver
or the authority declaration: those change both lanes together, so the fixture
would pass while proving nothing about divergence at the lane boundary. A fixture
that only perturbs the shared final treatment mapping is likewise insufficient —
it cannot distinguish agreement from a shared last step, which is the whole defect
this module exists to remove.

CANONICAL HASHING (both pre-refactor oracles and any frozen baseline here)
--------------------------------------------------------------------------
    payload_bytes    = json.dumps(records, sort_keys=True,
                                  separators=(",", ":")).encode("utf-8")
    canonical_sha256 = sha256(payload_bytes).hexdigest()

Hash the RECORDS payload only, never metadata that carries the hash itself.
Default JSON separators are forbidden for hash comparison: they emit different
bytes for semantically identical data, so two runs can disagree over whitespace
and look like content drift. The serialization string must be recorded verbatim
in the baseline metadata.

Nothing here restates an F4 value as a literal. The overrides are read from the authority
declaration, and this module holds no unit-specific wording of its own.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pl06_authority_v1 as A   # noqa: E402

OVERRIDE = "F4_AUTHORITY_OVERRIDE"
FALLBACK = "F3_RULE_APPLIED_TO_CONTROLLED_ROWS"

# F3's four cases, named by the authority. The `when` keys are the declaration's own.
SEQUENTIAL = "SEQUENTIAL_PROCESS"
COMPARISON = "EXPLICIT_SYMMETRIC_COMPARISON"
LAYERED = "LAYERED_NON_PROCESS_NON_COMPARISON"
OTHERWISE = "OTHERWISE"


def treatment_for(when):
    """The authority's own name for an F3 case. Never a literal typed here."""
    r = next((x for x in A.treatment_rules() if x["when"] == when), None)
    return r["treatment"] if r else None


def treatment_vocabulary():
    return sorted(r["treatment"] for r in A.treatment_rules())


def _norm(s):
    """Screen names are written by humans on both sides — 'Sub soil drainage' in the module
    heading, 'Sub-soil Drainage' in F4. Match on letters and digits only so a hyphen or a
    stray space cannot silently drop an override on the floor."""
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def overrides(unit_id):
    """{normalised screen name: treatment} for every screen F4 names for this unit.

    INCOMPLETE: this still carries a unit literal, which a unit-neutral shared module must
    not. The lookup belongs in `pl06_authority_v1.treatment_overrides(unit_id)` — the
    resolver asks, it does not know which unit has overrides.
    """
    if unit_id != "K5-PL06-T03-B03":   # TODO(0b): move to pl06_authority_v1
        return {}
    return {_norm(t["screen"]): t["treatment"]
            for t in A.value("interaction", "b03_treatments")}


def resolve(unit_id, screen_name, f3_case, f3_reason=None):
    """The single decision. `f3_case` is the caller's F3 reading of its own source; it is
    used only when the authority has not named this screen.

    Returns a record rather than a bare string so both lanes can show WHY, and so a parity
    test can compare the whole decision and not just its outcome.
    """
    ov = overrides(unit_id)
    key = _norm(screen_name)
    if key in ov:
        return dict(unit_id=unit_id, screen=screen_name, treatment=ov[key],
                    basis=OVERRIDE, authority_locus="F4",
                    reason=f"F4 names this screen explicitly; the F3 reading "
                           f"({f3_case}) does not apply.",
                    f3_case=f3_case, overridden=True)
    return dict(unit_id=unit_id, screen=screen_name, treatment=treatment_for(f3_case),
                basis=FALLBACK, authority_locus="F3",
                reason=f3_reason or f"F3 case {f3_case} read from the module's own rows.",
                f3_case=f3_case, overridden=False)


def is_step_by_step(treatment):
    return treatment == treatment_for(SEQUENTIAL)


def is_click_to_reveal(treatment):
    return treatment == treatment_for(LAYERED)
