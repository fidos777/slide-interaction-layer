# -*- coding: utf-8 -*-
"""Stage 4.2D — population audit harness.

For every gate emitted by the active suite this module answers one question:

    WHICH records does this gate actually look at, and which records that carry the
    same obligation does it never see?

It does not read the gate code alone. It runs the suite, captures the real local
variables each gate's expression references, resolves them to concrete review-page IDs
against the v0.4.3 deck and model, and computes the excluded set.

Three sources are combined:

  STATIC    ast over the four QA modules: gate ID, source expression, referenced names,
            the source line where each referenced name was defined, and the
            classification fields that appear in either.
  RUNTIME   a return-trace over each module's run(), capturing f_locals so a population
            name resolves to the list/dict it actually held.
  MODEL     the frozen model, to map each page to learner_screen_id, interaction items,
            parent screen, component and runtime state.

The obligation SCOPE of each gate — page-level, screen-level, item-level, component-level
or global — is authored in OBLIGATION_SCOPE below and is the one judged input. Everything
else is computed. A gate is flagged only when its computed population is a proper subset
of the semantic population its authored scope implies.
"""
import ast, collections, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
V4 = os.path.join(os.path.dirname(HERE), "v0_4")
SRC = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, V4); sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))

import b02_model_adapter_v0_4 as ADAPT

MODULES = [("STAGE_4_FULL", os.path.join(V4, "b02_full_qa_v0_4.py"), "b02_full_qa_v0_4"),
           ("STAGE_4_1_REGRESSION", os.path.join(V4, "b02_regression_qa_v0_4_1.py"),
            "b02_regression_qa_v0_4_1"),
           ("STAGE_4_2B_GOVERNANCE", os.path.join(V4, "b02_governance_qa_v0_4_2.py"),
            "b02_governance_qa_v0_4_2"),
           ("STAGE_4_2C_SCREENSHOT_ORACLE", os.path.join(V4, "b02_governance_qa_v0_4_3.py"),
            "b02_governance_qa_v0_4_3")]

CLASSIFICATION_FIELDS = [
    "semantic_screen_subtype", "screen_role", "runtime_state_type", "review_page_role",
    "execution_family", "popup_subtype", "notes_policy", "notes_policy_family",
    "control_type", "next_control_type", "back_control_type", "close_control_type",
    "completion_scope", "visual_requirement", "visual_status", "parent_screen_id",
    "learner_screen_id", "component_id", "group_id", "item_kind", "runtime_state_id",
    "source_row_uid", "source_row_uids", "interaction_item_id", "interaction_item_ids",
]

# ---------------------------------------------------------------- authored input
# The semantic level at which each gate's obligation lives. This is the ONE judged field.
# Anything not listed defaults to GLOBAL_OR_MODEL, which is never flagged for population
# blindness because it has no per-record population to be blind about.
SCREEN_LEVEL_PREFIX = (
    "EXAMPLE_SELECTION", "EXAMPLE_CARD", "REQUIRED_VISUAL", "FAMILY_S_VISUAL",
    "COMPONENT_MAIN", "S01_", "SHOT_S01", "SHOT_PERSISIR", "TAMAT_", "PERABOT_",
)
ITEM_LEVEL_PREFIX = ("TICK_", "COMPLETION_TICKS", "CARDS_DROPPED", "FAMILY_P1_PREMATURE",
                     "FAMILY_P2_PREMATURE")
PAGE_LEVEL_PREFIX = ("SHAPES_BEYOND", "CANVAS_SHAPES", "TEXT_COVERED", "MODAL_",
                     "NON_MODAL", "SPECIFICATION_POPUPS", "EXAMPLE_POPUPS",
                     "NOT_REQUIRED_VISUAL", "GENERIC_VISUAL", "QUIZ_", "ANSWER_KEY",
                     "MCQ_", "NOTES_", "SPOKEN_", "SILENT_STATES", "ACTION_INSTRUCTIONS",
                     "TECHNICAL_METADATA", "FAMILY_LABELS", "VISUAL_PANEL")

SCOPE_SCREEN, SCOPE_ITEM, SCOPE_PAGE = "SCREEN_LEVEL", "ITEM_LEVEL", "PAGE_LEVEL"
SCOPE_GLOBAL = "GLOBAL_OR_MODEL"


def authored_scope(gate):
    if gate.startswith(ITEM_LEVEL_PREFIX):
        return SCOPE_ITEM
    if gate.startswith(SCREEN_LEVEL_PREFIX):
        return SCOPE_SCREEN
    if gate.startswith(PAGE_LEVEL_PREFIX):
        return SCOPE_PAGE
    return SCOPE_GLOBAL


# ---------------------------------------------------------------- static pass
class GateVisitor(ast.NodeVisitor):
    def __init__(self, src):
        self.src = src
        self.gates = []
        self.assigns = {}          # name -> (lineno, source segment)

    def visit_Assign(self, node):
        seg = ast.get_source_segment(self.src, node) or ""
        for t in node.targets:
            for n in ast.walk(t):
                if isinstance(n, ast.Name):
                    self.assigns.setdefault(n.id, (node.lineno, seg))
        self.generic_visit(node)

    def visit_Call(self, node):
        f = node.func
        if isinstance(f, ast.Name) and f.id == "chk" and node.args:
            a0 = node.args[0]
            seg = ast.get_source_segment(self.src, node) or ""
            names = sorted({n.id for n in ast.walk(node) if isinstance(n, ast.Name)}
                           - {"chk", "sum", "len", "any", "all", "sorted", "set",
                              "list", "dict", "min", "max", "open", "str", "int",
                              "bool", "next", "zip", "range", "abs", "round"})
            # The population a gate TESTS is the one it iterates. A name used only as a
            # lookup table (has_dir[pid], ctext[pid]) spans every page and would mask the
            # restrictive population if the two were unioned.
            iterated = sorted({c.iter.id for n in ast.walk(node)
                               if isinstance(n, (ast.ListComp, ast.SetComp, ast.DictComp,
                                                 ast.GeneratorExp))
                               for c in n.generators if isinstance(c.iter, ast.Name)})
            if isinstance(a0, ast.Constant) and isinstance(a0.value, str):
                self.gates.append(dict(gate=a0.value, lineno=node.lineno, expr=seg,
                                       names=names, iterated=iterated, template=None))
            elif isinstance(a0, ast.JoinedStr):
                # gate ID built at run time inside a loop, e.g. f"SHAPES_BEYOND_{e}_EDGE".
                # Record the literal skeleton so runtime IDs can be matched back to it.
                lit = [v.value for v in a0.values
                       if isinstance(v, ast.Constant) and isinstance(v.value, str)]
                self.gates.append(dict(gate=None, lineno=node.lineno, expr=seg,
                                       names=names, iterated=iterated, template=lit))
        self.generic_visit(node)


def static_gates():
    out = []
    for layer, path, mod in MODULES:
        src = open(path, encoding="utf-8").read()
        v = GateVisitor(src); v.visit(ast.parse(src))
        for g in v.gates:
            defs = {n: v.assigns[n] for n in g["names"] if n in v.assigns}
            blob = g["expr"] + " " + " ".join(s for _, s in defs.values())
            g.update(layer=layer, module=mod,
                     definitions={n: dict(lineno=l, source=s) for n, (l, s) in defs.items()},
                     classification_fields=sorted(
                         {f for f in CLASSIFICATION_FIELDS if f'"{f}"' in blob
                          or f"'{f}'" in blob or f".{f}" in blob}))
            out.append(g)
    return out


# ---------------------------------------------------------------- runtime pass
def runtime_locals(pptx):
    """f_locals of each module's run() at return, so a population name resolves to the
    value it actually held against this deck."""
    snap = {}
    import importlib

    def tracer(frame, event, arg):
        if event == "call" and frame.f_code.co_name == "run":
            mod = frame.f_globals.get("__name__")
            if mod in {m for _, _, m in MODULES}:
                def local_tracer(f, e, a):
                    if e == "return":
                        snap[mod] = dict(f.f_locals)
                    return local_tracer
                return local_tracer
        return None

    for _, _, mod in MODULES:
        m = importlib.import_module(mod)
        sys.settrace(tracer)
        try:
            m.run(pptx)
        finally:
            sys.settrace(None)
    return snap


# ---------------------------------------------------------------- population resolution
def resolve(value, all_pages):
    """Page IDs a population value denotes, or None if it is not a page population."""
    if isinstance(value, (list, set, tuple)):
        ids = {v for v in value if isinstance(v, str) and v in all_pages}
        if ids and len(ids) == len([v for v in value if isinstance(v, str)]):
            return ids
    if isinstance(value, dict):
        ids = {k for k in value if isinstance(k, str) and k in all_pages}
        if ids and len(ids) == len(value):
            return ids
    return None


def main(pptx):
    M = ADAPT.Model(); pages = ADAPT.all_pages(M)
    all_pages = {p["id"]: p for p in pages}
    screen_of = {p["id"]: p["screen_id"] for p in pages}
    pages_of_screen = collections.defaultdict(list)
    for p in pages:
        pages_of_screen[p["screen_id"]].append(p["id"])
    items_of_screen = {s: [i["interaction_item_id"] for i in M.items_of(s)]
                       for s in pages_of_screen}
    comp_of = {p["id"]: p.get("component_id") for p in pages}

    snap = runtime_locals(pptx)
    gates = static_gates()

    # Every ID the suite actually emits, in order. Gates whose ID is an f-string built in
    # a loop have gate=None statically; bind each emitted ID to the template whose literal
    # parts it contains, so no emitted gate escapes the audit.
    import importlib
    emitted = [k for k, _, _, _ in importlib.import_module(MODULES[-1][2]).run(pptx)]
    static_ids = {g["gate"] for g in gates if g["gate"]}
    templates = [g for g in gates if g["gate"] is None]
    expanded = []
    for gid in emitted:
        if gid in static_ids:
            continue
        for t in templates:
            if t["template"] and all(part in gid for part in t["template"] if part):
                e = dict(t); e["gate"] = gid; e["expanded_from_template"] = t["template"]
                expanded.append(e); break
    gates = [g for g in gates if g["gate"]] + expanded
    unbound = sorted(set(emitted) - {g["gate"] for g in gates})

    seen = collections.Counter(g["gate"] for g in gates)
    duplicates = sorted(k for k, v in seen.items() if v > 1)

    recs = []
    for g in gates:
        loc = snap.get(g["module"], {})
        pops = {}
        for n in g["names"]:
            if n in loc:
                ids = resolve(loc[n], all_pages)
                if ids is not None:
                    pops[n] = ids
        # prefer the iterated population; a bare `len(x)` gate iterates nothing, so fall
        # back to the smallest resolved population rather than the union
        it = [n for n in g.get("iterated") or [] if n in pops]
        if it:
            selected = set().union(*(pops[n] for n in it))
            tested_by = it
        elif pops:
            smallest = min(pops, key=lambda n: len(pops[n]))
            selected = set(pops[smallest])
            tested_by = [smallest]
        else:
            selected, tested_by = None, []
        superseded = "SUPERSEDED" in g["gate"]
        scope = SCOPE_GLOBAL if superseded else authored_scope(g["gate"])

        rec = dict(
            gate_id=g["gate"], status="SUPERSEDED_MARKER" if superseded else "ACTIVE",
            layer=g["layer"], module=g["module"], source_line=g["lineno"],
            property_tested=g["expr"].split("\n")[0][:200],
            population_selector=(tested_by or None),
            population_names_referenced=(sorted(pops) or None),
            population_selector_source={n: g["definitions"].get(n, {}).get("source", "")
                                        for n in (tested_by or pops)},
            classification_fields=g["classification_fields"],
            obligation_scope=scope,
            selected_records=(sorted(selected) if selected is not None else None),
            selected_count=(len(selected) if selected is not None else None),
        )

        if selected is None or superseded:
            rec.update(semantic_population=None, semantic_count=None,
                       excluded_records=[], excluded_count=0,
                       excluded_share_obligation=False,
                       weakness_classes=([] if not superseded else ["SUPERSEDED_MARKER"]),
                       replacement_strategy=None)
            recs.append(rec); continue

        # semantic population implied by the authored scope
        if scope == SCOPE_SCREEN:
            screens = {screen_of[p] for p in selected}
            semantic = {q for s in screens for q in pages_of_screen[s]}
            anchor = "learner_screen_id"
        elif scope == SCOPE_ITEM:
            screens = {screen_of[p] for p in selected if items_of_screen.get(screen_of[p])}
            semantic = {q for s in screens for q in pages_of_screen[s]}
            anchor = "interaction_item_id via parent learner_screen_id"
        else:
            semantic = set(selected)
            anchor = "review_page_id (page-local obligation)"

        excluded = sorted(semantic - selected)
        rec.update(
            semantic_population_anchor=anchor,
            semantic_count=len(semantic),
            excluded_records=excluded, excluded_count=len(excluded),
            excluded_share_obligation=bool(excluded),
            excluded_by_state_role=dict(collections.Counter(
                M.state(all_pages[p]["state_id"])["screen_role"] for p in excluded)),
            weakness_classes=(["CLASSIFICATION_SCOPED_POPULATION"] if excluded else []),
            replacement_strategy=("PIN_TO_" + anchor.split()[0].upper() if excluded else None),
        )
        recs.append(rec)

    active = [r for r in recs if r["status"] == "ACTIVE"]
    scoped = [r for r in active if r["classification_fields"] and r["selected_count"]]
    gaps = [r for r in active if r["excluded_count"]]
    complete = [r for r in active if r["selected_count"] and not r["excluded_count"]]

    return dict(
        audit="QA_POPULATION_AUDIT_v0.4.3",
        deck=os.path.basename(pptx),
        gate_ids_unbound_to_source=unbound,
        totals=dict(
            GATES_EMITTED_BY_SUITE=len(emitted),
            GATES_RESOLVED_TO_SOURCE=len(recs),
            GATES_UNBOUND_TO_SOURCE=len(unbound),
            DUPLICATE_GATE_IDS=len(duplicates),
            SUPERSEDED_MARKERS=len(recs) - len(active),
            ACTIVE_GATES_AUDITED=len(active),
            CLASSIFICATION_SCOPED_GATES=len(scoped),
            GATES_WITH_SEMANTIC_POPULATION_GAPS=len(gaps),
            RECORDS_WRONGLY_EXCLUDED=sum(r["excluded_count"] for r in gaps),
            GATES_REQUIRING_PINNED_POPULATION=len(gaps),
            GATES_WITH_COMPLETE_POPULATION=len(complete),
            GATES_WITHOUT_PAGE_POPULATION=len([r for r in active
                                               if not r["selected_count"]]),
        ),
        duplicate_gate_ids=duplicates,
        gates=recs,
    )


if __name__ == "__main__":
    print(json.dumps(main(sys.argv[1]), ensure_ascii=False, indent=1))
