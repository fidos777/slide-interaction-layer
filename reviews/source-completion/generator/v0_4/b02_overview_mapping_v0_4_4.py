# -*- coding: utf-8 -*-
"""Component-main overview subjects — the ONE population helper shared by the generator
and the validators.

Reads the frozen contract COMPONENT_OVERVIEW_MAPPING_v0.4.4.json. It does not derive
subjects itself, so the generator cannot drift from the mapping the validators check.

Authority split, per the frozen screenshots:
    requirement  D2 6:52 PM   component-main visual REQUIRED
    treatment    D2 6:52 PM   several smaller visuals as an overview
    cardinality  D4 8:24 AM   Papan Tanda = 2 (Pilihan A), BBQ Pit = 1
    subjects     MODULE_SOURCE_ATTESTED, except the two Papan Tanda figures which D4 names
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(os.path.dirname(HERE))
CONTRACT = os.path.join(SRC, "COMPONENT_OVERVIEW_MAPPING_v0.4.4.json")

MAIN_ROLES = ("COMPONENT_MAIN_EXPLANATION", "COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST",
              "COMPONENT_EXPLANATION_WITH_SPEC_LIST")

HEADING = "ARAHAN VISUAL — OVERVIEW KOMPONEN (TIDAK DIBENAMKAN)"


class OverviewMappingError(RuntimeError):
    """The frozen mapping is missing, incomplete or still ambiguous. Fail closed."""


def _load():
    if not os.path.exists(CONTRACT):
        raise OverviewMappingError(f"overview mapping contract missing: {CONTRACT}")
    m = json.load(open(CONTRACT, encoding="utf-8"))
    t = m["totals"]
    if t["AMBIGUOUS_OVERVIEW_MAPPINGS"] != 0 or not t["GENERATION_PERMITTED"]:
        raise OverviewMappingError(
            "overview mapping is still ambiguous — generation is not permitted")
    return m


_M = None


def mapping():
    global _M
    if _M is None:
        _M = _load()
    return _M


def by_component():
    return {c["component_id"]: c for c in mapping()["components"]}


def subjects(component_id):
    """Ordered overview subjects for one component: (label, direction_text)."""
    c = by_component().get(component_id)
    if c is None:
        raise OverviewMappingError(f"component not in the frozen mapping: {component_id}")
    out = [(s["subject_label"], s["visual_direction_text"]) for s in c["subjects"]]
    if len(out) != c["overview_visual_count"]:
        raise OverviewMappingError(
            f"{component_id}: {len(out)} subjects but overview_visual_count="
            f"{c['overview_visual_count']}")
    if not out:
        raise OverviewMappingError(f"{component_id}: no overview subject")
    return out


def count(component_id):
    return by_component()[component_id]["overview_visual_count"]


def is_component_main(screen_role):
    return screen_role in MAIN_ROLES


def component_main_screens(M):
    """Every component-main learner screen id, pinned by screen_role — not by review-page
    classification, which varies across the states of one screen."""
    return sorted(s["learner_screen_id"] for s in M.map["screens"]
                  if s["screen_role"] in MAIN_ROLES)


def state_pages(M, pages):
    """Every review page bound to a component-main learner screen, by learner_screen_id."""
    ids = set(component_main_screens(M))
    return [p["id"] for p in pages if p["screen_id"] in ids]
