#!/usr/bin/env python3
"""
Ontology sidecar validator (v0.5.1) — stdlib only.

Validates that a *.ontology.json sidecar matches ontology/schema.json and mirrors its HTML deck.
Read-only dev/CI tool. Not part of any deck's runtime. Zero required dependencies; if the optional
`jsonschema` package is installed it is also used, but its absence never causes a failure.

Usage:
  python3 ontology/validate.py <sidecar.json> [deck.html]
  python3 ontology/validate.py --all          # scan repo (excludes ontology/test-fixtures/)
Flags: --json (machine-readable), --quiet (errors only)
Exit:  0 = all valid, 1 = errors found, 2 = usage error
Run from the repository root.
"""
import argparse, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))   # the ontology/ dir
SCHEMA_PATH = os.path.join(HERE, "schema.json")

# Allowed element -> pattern mapping (mirrors ontology/element-to-pattern-map.md).
# Used only for the advisory "mapping fidelity" warning (check 15).
ALLOWED = {
    "E1": {"P1", "P3", "P0"}, "E2": {"P1", "P0", "P2"}, "E3": {"P5", "P1"},
    "E4": {"P5", "P0"}, "E5": {"P2", "P1"}, "E6": {"P0", "P1"},
    "E7": {"P7", "P5", "P0"}, "E8": {"P4", "P0"}, "E9": {"P0", "P3"},
    "E10": {"P7"}, "E11": {"P6"}, "E12": {"P8"}, "E13": {"P0"},
    "E14": {"P0"}, "E15": {"P1", "P6"},
}
GATING_ENUM = {"none", "all_cards_revealed", "all_hotspots_clicked", "answered_correctly",
               "reached_an_ending", "user_changed", "at_least_one_opened", "attempted"}
RE_E = re.compile(r"^E([1-9]|1[0-5])$")
RE_P = re.compile(r"^P[0-8]$")
TOP_KEYS = {"$schema", "sidecarVersion", "deck", "deckTitle", "slideCount", "gatingMode", "slides"}
SLIDE_KEYS = {"index", "element", "objective", "pattern", "gating", "required", "bloom", "rationale"}


def resolve_deck(sidecar_path, data, deck_arg):
    if deck_arg:
        return deck_arg
    if isinstance(data, dict) and data.get("deck"):
        return data["deck"]  # repo-relative
    # filename convention: <base>.ontology.json -> <base>.html (same dir)
    base = sidecar_path[:-len(".ontology.json")] if sidecar_path.endswith(".ontology.json") else None
    return base + ".html" if base else None


def validate(sidecar_path, deck_arg=None, schema=None):
    errors, warnings = [], []
    def err(check, msg, slide=None): errors.append({"check": check, "slide": slide, "severity": "error", "message": msg})
    def warn(check, msg, slide=None): warnings.append({"check": check, "slide": slide, "severity": "warning", "message": msg})

    # --- A. schema / shape ---
    try:
        with open(sidecar_path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        err(1, "not valid JSON: %s" % e)
        return {"sidecar": sidecar_path, "deck": None, "ok": False, "errors": errors, "warnings": warnings}
    if not isinstance(data, dict):
        err(1, "top-level value is not an object")
        return {"sidecar": sidecar_path, "deck": None, "ok": False, "errors": errors, "warnings": warnings}

    if data.get("sidecarVersion") != "1.0":
        err(2, 'sidecarVersion must be "1.0" (got %r)' % data.get("sidecarVersion"))
    for k in ("deck", "slideCount", "slides"):
        if k not in data:
            err(2, "missing required key: %s" % k)
    for k in data:
        if k not in TOP_KEYS:
            err(3, "unknown top-level key: %s" % k)

    slides = data.get("slides")
    if not isinstance(slides, list) or not slides:
        err(4, "slides must be a non-empty array")
        slides = []

    for s in slides:
        idx = s.get("index") if isinstance(s, dict) else None
        if not isinstance(s, dict):
            err(4, "slide entry is not an object", idx); continue
        for k in ("index", "element", "objective", "pattern", "gating"):
            if k not in s: err(4, "missing required field: %s" % k, idx)
        for k in s:
            if k not in SLIDE_KEYS: err(3, "unknown slide key: %s" % k, idx)
        if "element" in s and not RE_E.match(str(s["element"])):
            err(5, 'element %r out of range (expected E1-E15)' % s.get("element"), idx)
        if "pattern" in s and not RE_P.match(str(s["pattern"])):
            err(6, 'pattern %r out of range (expected P0-P8)' % s.get("pattern"), idx)
        if "objective" in s and not (isinstance(s["objective"], str) and s["objective"].strip()):
            err(7, "objective is empty", idx)
        if "gating" in s and s["gating"] not in GATING_ENUM:
            err(8, 'gating %r not in the allowed enum' % s.get("gating"), idx)
        if "bloom" in s and s["bloom"] not in {"remember","understand","apply","analyze","evaluate","create"}:
            warn(9, 'bloom %r not a recognized level' % s.get("bloom"), idx)
        if "required" in s and not isinstance(s["required"], bool):
            warn(9, "required should be a boolean", idx)
        # C16. critical-visibility (blocker)
        if s.get("element") == "E13" and s.get("gating") not in (None, "none"):
            err(16, "E13 (Warning/Critical) must have gating: none", idx)
        # C15. mapping fidelity (warning)
        el, pat = s.get("element"), s.get("pattern")
        if el in ALLOWED and isinstance(pat, str) and pat not in ALLOWED[el]:
            warn(15, "%s not a listed mapping for %s" % (pat, el), idx)

    # optional jsonschema pass (enhancement only)
    if schema is not None:
        try:
            import jsonschema  # noqa
            jsonschema.validate(data, schema)
        except ImportError:
            pass
        except Exception as e:
            err("schema", "jsonschema: %s" % str(e).splitlines()[0])

    # --- B. deck-mirror ---
    deck_path = resolve_deck(sidecar_path, data, deck_arg)
    if not deck_path or not os.path.exists(deck_path):
        err(10, "deck not found for mirror checks: %r" % deck_path)
        deck_path = None
    if deck_path:
        html = open(deck_path, encoding="utf-8").read()
        deck_slide_count = len(re.findall(r'class="slide\b', html))
        if isinstance(data.get("slideCount"), int) and data["slideCount"] != deck_slide_count:
            err(10, "slideCount %s != deck .slide count %s" % (data["slideCount"], deck_slide_count))
        idxs = [s.get("index") for s in slides if isinstance(s, dict)]
        if idxs != list(range(1, len(slides) + 1)):
            err(11, "slides[].index must be contiguous 1..%d (got %s)" % (len(slides), idxs))
        deck_els = re.findall(r"element:\s*(E\d+)", html)
        deck_pats = re.findall(r"pattern:\s*(P\d)", html)
        json_els = [s.get("element") for s in slides if isinstance(s, dict)]
        json_pats = [s.get("pattern") for s in slides if isinstance(s, dict)]
        if deck_els and deck_els != json_els:
            err(12, "element sequence != deck comments\n      deck: %s\n      json: %s" % (deck_els, json_els))
        if deck_pats and deck_pats != json_pats:
            err(13, "pattern sequence != deck comments\n      deck: %s\n      json: %s" % (deck_pats, json_pats))
        m = re.search(r'data-sil-gating="([^"]+)"', html)
        if m and data.get("gatingMode") and m.group(1) != data["gatingMode"]:
            warn(14, "gatingMode %r != deck data-sil-gating %r" % (data.get("gatingMode"), m.group(1)))

    return {"sidecar": sidecar_path, "deck": deck_path, "ok": len(errors) == 0,
            "errors": errors, "warnings": warnings,
            "counts": {"errors": len(errors), "warnings": len(warnings)}}


def find_all():
    out = []
    for p in glob.glob("**/*.ontology.json", recursive=True):
        if "test-fixtures" + os.sep in p or "/test-fixtures/" in p.replace(os.sep, "/"):
            continue
        out.append(p)
    return sorted(out)


def print_report(r, quiet=False):
    n = r["counts"]["errors"] if "counts" in r else len(r["errors"])
    w = r["counts"]["warnings"] if "counts" in r else len(r["warnings"])
    if r["ok"]:
        if not quiet:
            print("✓ %s — %s, %d errors, %d warnings" %
                  (r["sidecar"], _slides_str(r), 0, w))
        for x in r["warnings"]:
            print("  WARN   %s%s   [check %s]" % (_sl(x), x["message"], x["check"]))
    else:
        print("✗ %s" % r["sidecar"])
        for x in r["errors"]:
            print("  ERROR  %s%s   [check %s]" % (_sl(x), x["message"], x["check"]))
        for x in r["warnings"]:
            print("  WARN   %s%s   [check %s]" % (_sl(x), x["message"], x["check"]))
        print("  %d errors, %d warnings" % (n, w))


def _sl(x): return ("slide %s: " % x["slide"]) if x.get("slide") else ""
def _slides_str(r): return "validated"


def load_schema():
    try:
        with open(SCHEMA_PATH, encoding="utf-8") as f:
            sc = json.load(f)
        sc.pop("$id", None)
        return sc
    except Exception:
        return None


def main(argv=None):
    ap = argparse.ArgumentParser(description="Validate ontology sidecars against schema.json + their deck.")
    ap.add_argument("sidecar", nargs="?", help="path to a *.ontology.json file")
    ap.add_argument("deck", nargs="?", help="optional deck .html (else derived from sidecar)")
    ap.add_argument("--all", action="store_true", help="scan repo (excludes ontology/test-fixtures/)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--quiet", action="store_true", help="errors only")
    a = ap.parse_args(argv)

    if not a.all and not a.sidecar:
        ap.print_usage(); return 2

    schema = load_schema()
    targets = find_all() if a.all else [a.sidecar]
    if a.all and not targets:
        if not a.quiet and not a.json:
            print("No *.ontology.json sidecars found (excluding test-fixtures).")
        return 0

    reports = [validate(t, a.deck if not a.all else None, schema) for t in targets]
    if a.json:
        print(json.dumps(reports if a.all else reports[0], indent=2))
    else:
        for r in reports:
            print_report(r, a.quiet)
        if a.all:
            te = sum(r["counts"]["errors"] for r in reports)
            tw = sum(r["counts"]["warnings"] for r in reports)
            print("\n%d sidecar(s): %d errors, %d warnings" % (len(reports), te, tw))
    return 1 if any(not r["ok"] for r in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
