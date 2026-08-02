# -*- coding: utf-8 -*-
"""Registered off-stage geometry exemptions.

Stage 4.2E-C Part 4, outcome B — UNREGISTERED_GEOMETRY_EXEMPTION.

Two shapes in this deck sit outside the 13.3333 x 7.5 in stage on purpose, and until this
module neither was registered:

  Title 1     a real PowerPoint title placeholder, <p:ph type="title"/>, pushed above the
              top edge. It passed the four-edge gate only because that gate tested
              `y < -0.66` — an ad hoc numeric threshold chosen to clear -0.631 in. Any
              ordinary shape parked between -0.66 and 0 would have passed with it.

  ProdPanel   the review-only production panel at x = -6.90 in. It passed because the
              package reader partitions shapes on `(x + w) <= 0` into `canvas` and `panel`,
              and the four-edge gate only ever iterated `canvas`. That is a partition, not
              a rule: anything pushed fully left of the stage disappeared from the gate.

An entry here matches only on the full identity of the shape — placeholder-ness, placeholder
type, shape name and all four coordinates to 0.001 in. A shape merely NAMED "Title 1", or a
real title placeholder MOVED, matches nothing and fails the four-edge gate like any other
shape. That is what makes this a registry rather than a second ad hoc threshold.

Neither shape is moved or deleted: the title placeholder is what PowerPoint's outline pane,
the accessibility tree and Ctrl+F use to identify a slide, and the production panel is the
reviewer's metadata surface. Both are outside the Slide Show viewport, so neither is
learner-facing.
"""
EMU = 914400.0
TOL = 0.001                                     # inches


def _in(v):
    return v / EMU


OFF_CANVAS_EXEMPTIONS = [
    dict(
        exemption_id="GEX-001",
        shape_name="Title 1",
        requires_placeholder=True,
        ph_type="title",
        x=_in(0), y=_in(-577078), w=_in(12191970), h=_in(523220),
        edges_exempted=("top",),
        page_population="ALL_REVIEW_PAGES",
        learner_facing=False,
        visible_in_slide_show=False,
        purpose="PowerPoint slide-title identity: outline pane, accessibility name, "
                "slide navigator and search. Off the top edge so it never paints on the "
                "learner canvas while remaining the slide's programmatic title.",
        why_not_deleted="Deleting it would leave every slide untitled in the outline pane "
                        "and in the accessibility tree. It is not proven unnecessary.",
        enforcement_gate="OFF_CANVAS_PLACEHOLDER_EXEMPTION_REGISTERED",
        registered_at="Stage 4.2E-C",
    ),
    dict(
        exemption_id="GEX-002",
        shape_name="ProdPanel",
        requires_placeholder=False,
        ph_type=None,
        x=_in(-6309360), y=_in(0), w=_in(6035040), h=_in(6858000),
        edges_exempted=("left",),
        page_population="ALL_REVIEW_PAGES",
        learner_facing=False,
        visible_in_slide_show=False,
        purpose="Review-only production metadata panel. Deliberately parked left of the "
                "stage so a reviewer reads it in Normal view and a learner never sees it.",
        why_not_deleted="It is the review surface this whole storyboard exists to carry.",
        enforcement_gate="OFF_CANVAS_PRODUCTION_PANEL_EXEMPTION_REGISTERED",
        registered_at="Stage 4.2E-C",
    ),
]

STAGE_W, STAGE_H = 13.3333, 7.5


def _match(shape, e):
    if shape.get("name") != e["shape_name"]:
        return False
    if e["requires_placeholder"]:
        if not shape.get("is_placeholder") or shape.get("ph_type") != e["ph_type"]:
            return False
    elif shape.get("is_placeholder"):
        return False
    for k in ("x", "y", "w", "h"):
        if abs(shape.get(k, 0.0) - e[k]) > TOL:
            return False
    return True


def exemption_for(shape):
    """The registry entry covering this shape, or None. None means the four-edge gate
    applies in full — which is the default for every shape in the deck."""
    for e in OFF_CANVAS_EXEMPTIONS:
        if _match(shape, e):
            return e
    return None


def edges_outside(shape):
    """Which stage edges this shape crosses, ignoring any exemption."""
    out = []
    if shape["x"] < -0.01:
        out.append("left")
    if shape["y"] < -0.01:
        out.append("top")
    if shape["x"] + shape["w"] > STAGE_W + 0.01:
        out.append("right")
    if shape["y"] + shape["h"] > STAGE_H + 0.01:
        out.append("bottom")
    return out


def unregistered_off_canvas(shapes):
    """Every shape crossing a stage edge that no registry entry covers, or that a registry
    entry covers for a different edge than the one it actually crosses."""
    bad = []
    for s in shapes:
        edges = edges_outside(s)
        if not edges:
            continue
        e = exemption_for(s)
        if e is None or any(edge not in e["edges_exempted"] for edge in edges):
            bad.append((s.get("name"), tuple(edges), round(s["x"], 3), round(s["y"], 3)))
    return bad


def registry_records():
    return [{k: (list(v) if isinstance(v, tuple) else v) for k, v in e.items()}
            for e in OFF_CANVAS_EXEMPTIONS]
