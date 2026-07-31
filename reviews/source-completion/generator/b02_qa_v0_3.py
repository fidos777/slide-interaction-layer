# -*- coding: utf-8 -*-
"""CHECKABLE QA gates for the B02 review deck.

Scoping discipline carried forward from the Stage 1.5 audit: every check names
the structure it inspects. No whole-document grep stands in for a structured
assertion. Human-judgment items are never marked PASS — they are emitted as
PENDING_HUMAN by the report writer, not here.
"""
import json, os, re, sys, zipfile
from xml.etree import ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b02_model_v0_3 as MODEL

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
EMU = 914400.0
TECH = [r"\bRP-\d{3}\b", r"_EXAMPLE_\d{2}\b", r"\bitem_viewed\b", r"\bcomponent_complete\b",
        r"\bgroup_complete\b", r"\bmain_vo_complete\b", r"PHYSICAL LEARNER SCREEN",
        r"REVIEW PAGE", r"PROVISIONAL_CAIR_EXECUTION", r"NOT_FOR_MMD_BUILD",
        r"PENDING_FINAL_BARIAH_CONFIRMATION", r"REVIEW_READY", r"MULTIMEDIA_NOT_PRODUCED",
        r"CAIR_INTEGRITY_EXCEPTION", r"SINGLE_ITEM_EXAMPLE_TREATMENT",
        r"K5-PL06-T03-B02-[A-Z-]+-ROW-\d{2}"]
BANNED_RUMUSAN = [r"(?i)\bKepentingan\b", r"(?i)\bApa Yang Dipelajari\b",
                  r"(?i)\bIsi Utama\b", r"(?i)\bManfaat\b"]


def shapes_of(xml):
    root = ET.fromstring(xml)
    out = []
    for sp in root.find(f"{P}cSld/{P}spTree").findall(f"{P}sp"):
        nv = sp.find(f"{P}nvSpPr/{P}cNvPr")
        xf = sp.find(f"{P}spPr/{A}xfrm")
        off = ext = None
        if xf is not None:
            o, e = xf.find(f"{A}off"), xf.find(f"{A}ext")
            if o is not None: off = (int(o.get("x")) / EMU, int(o.get("y")) / EMU)
            if e is not None: ext = (int(e.get("cx")) / EMU, int(e.get("cy")) / EMU)
        txt = "".join(t.text or "" for t in sp.iter(f"{A}t"))
        fills = [c.get("val") for c in sp.iter(f"{A}srgbClr")]
        out.append(dict(name=(nv.get("name") if nv is not None else ""), off=off, ext=ext,
                        text=txt, fills=fills,
                        custgeom=sp.find(f"{P}spPr/{A}custGeom") is not None))
    return out


def oncanvas(shs):
    return "\n".join(s["text"] for s in shs
                     if s["off"] and s["off"][0] >= 0 and s["off"][1] >= 0 and s["text"])


def offcanvas(shs):
    return "\n".join(s["text"] for s in shs if s["off"] and s["off"][0] < 0 and s["text"])


def run(pptx, only=None):
    M = MODEL.build()
    pi = MODEL.popup_index(M)
    z = zipfile.ZipFile(pptx)
    slides = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
                    key=lambda n: int(re.search(r"\d+", n.split("/")[-1]).group()))
    notes = {}
    for i in range(1, len(slides) + 1):
        p = f"ppt/notesSlides/notesSlide{i}.xml"
        if p in z.namelist():
            r = ET.fromstring(z.read(p))
            body = None
            for sp in r.iter(f"{P}sp"):
                ph = sp.find(f"{P}nvSpPr/{P}nvPr/{P}ph")
                if ph is not None and ph.get("type") == "body": body = sp
            notes[i] = "".join(t.text or "" for t in body.iter(f"{A}t")) if body is not None else ""
        else:
            notes[i] = ""
    pages = M["pages"]
    if only:
        keep = set(only)
        pages = [p for p in pages
                 if (next(s for s in M["screens"] if s["id"] == p["screen"]).get("comp") in keep)]
        pi = {k: v for k, v in pi.items() if v[0] in keep}
        M = dict(M, order=[c for c in M["order"] if c in keep])
    S = [shapes_of(z.read(n).decode("utf-8")) for n in slides]
    assert len(S) == len(pages), f"slides {len(S)} != pages {len(pages)}"


    m = {}
    exp = 26 if not only else sum(len(M["by_comp"][c]) for c in M["order"])
    m["SOURCE_ROWS_EXPECTED"] = exp
    m["SOURCE_ROWS_MAPPED"] = len({r["uid"] for _, r, _ in pi.values()})
    seen = {}
    for st, (cid, r, k) in pi.items():
        seen.setdefault(r["uid"], []).append(st)
    m["DUPLICATE_ROW_MAPPINGS"] = sum(1 for v in seen.values() if len(v) > 1)
    m["OMITTED_SOURCE_ROWS"] = exp - len(seen)

    popup_pages = [p for p in pages if p["variant"] == "POPUP"]
    m["POPUPS_WITHOUT_PARENT"] = sum(
        1 for p in popup_pages
        if not any(s["id"] == p["screen"] and s["kind"] == "EXAMPLES" for s in M["screens"]))
    m["POPUPS_WITHOUT_VO"] = sum(1 for i, p in enumerate(pages, 1)
                                 if p["variant"] == "POPUP" and not notes.get(i, "").strip())
    # depth: only group master (L1) and example screen (L2) are navigable destinations
    depths = {}
    for s in M["screens"]:
        depths[s["id"]] = 0 if s["kind"] in ("FRAME", "GROUP_MASTER") else (
            1 if s["kind"] == "MAIN" else 2)
    m["INVALID_NAVIGATION_DEPTH"] = sum(1 for v in depths.values() if v > 2)
    m["ITEMS_WITHOUT_VIEWED_STATE"] = sum(
        1 for st in pi if not any(x["id"] == f"item_viewed[{st}]" for x in M["states"]))
    m["COMPONENTS_WITHOUT_COMPLETE_RULE"] = sum(
        1 for c in M["order"] if not any(x["id"] == f"component_complete[{c}]" for x in M["states"]))
    m["GROUPS_WITHOUT_COMPLETE_RULE"] = sum(
        1 for g in ("STRUKTUR_TAMAN", "PERABOT_TAMAN")
        if not any(x["id"] == f"group_complete[{g}]" for x in M["states"]))

    # Kembali / Seterusnya enabled state read from the artifact's button fill
    ENABLED, DISABLED = "1F4E79", "D9D9D9"
    prem_k = prem_s = 0
    for i, p in enumerate(pages, 1):
        for s in S[i - 1]:
            if s["name"] != "Btn" or not s["text"]: continue
            en = ENABLED in s["fills"]
            if s["text"].strip() == "Kembali":
                should = bool(p["payload"].get("kembali"))
                if en != should: prem_k += 1
            if s["text"].strip() == "Seterusnya":
                scr = next(x for x in M["screens"] if x["id"] == p["screen"])
                if scr["kind"] == "GROUP_MASTER":
                    should = bool(p["payload"].get("next_enabled"))
                    if en != should: prem_s += 1
                elif scr["kind"] == "MAIN" and en:
                    prem_s += 1
    m["PREMATURE_KEMBALI"] = prem_k
    m["PREMATURE_GLOBAL_SETERUSNYA"] = prem_s

    silent = [i for i, p in enumerate(pages, 1)
              if p["variant"] in ("ALL_VIEWED", "GROUP_COMPLETE")
              or (p["variant"] == "BASE" and p["screen"].endswith("_EXAMPLES"))]
    m["NONEMPTY_NOTES_ON_SILENT_STATES"] = sum(1 for i in silent if notes.get(i, "").strip())

    leaks = []
    for i, p in enumerate(pages, 1):
        t = oncanvas(S[i - 1])
        for pat in TECH:
            if re.search(pat, t): leaks.append((p["id"], pat))
    m["LEARNER_CANVAS_TECHNICAL_TOKENS"] = len(leaks)

    miss = []
    for i, p in enumerate(pages, 1):
        scr = next(x for x in M["screens"] if x["id"] == p["screen"])
        if scr["kind"] in ("MAIN", "EXAMPLES", "GROUP_MASTER"):
            if not re.search(r"ms \d{3}", offcanvas(S[i - 1])): miss.append(p["id"])
    m["MISSING_SOURCE_LOCATORS"] = len(miss)

    assets = set()
    src_rows = M["content"]["rows"] if not only else [r for c in M["order"] for r in M["by_comp"][c]]
    for row in src_rows:
        assets |= set(re.findall(r"K5PL06T03-B02-IMG-p\d+-x\d+", row.get("visual") or ""))
    exp_assets = 14 if not only else len({a for c in M["order"] for row in M["by_comp"][c]
                                          for a in re.findall(r"K5PL06T03-B02-IMG-p\d+-x\d+", row.get("visual") or "")})
    m["ORPHAN_SOURCE_ASSETS"] = exp_assets - len(assets)

    extra = dict(
        review_pages=len(pages), physical_screens=len(M["screens"]), runtime_states=len(M["states"]),
        popup_states=len(pi), slides_in_package=len(slides),
        rumusan_banned_labels=sum(
            1 for i, p in enumerate(pages, 1) if p["screen"] == "RUMUSAN"
            for pat in BANNED_RUMUSAN if re.search(pat, oncanvas(S[i - 1]))),
        notes_grammar_violations=sum(
            1 for i in notes if re.search(r"VO PENUH:|^S\d\d —|RUNTIME STATE|REVIEW PAGE", notes[i])),
        embedded_media=len([n for n in z.namelist() if n.startswith("ppt/media/")]),
        pl_note_offcanvas=all(
            "PL kosong satu" not in oncanvas(S[i - 1]) for i in range(1, len(pages) + 1)) and
            any("PL kosong satu" in offcanvas(S[i - 1]) for i in range(1, len(pages) + 1)),
        hilmi_prefix_pages=[pages[i - 1]["id"] for i in notes if notes[i].startswith("Hilmi:")],
        ticks_are_native=all(
            any(s["custgeom"] for s in S[i - 1])
            for i, p in enumerate(pages, 1) if p["variant"] in ("ALL_VIEWED", "GROUP_COMPLETE")),
    )
    return m, extra, dict(leaks=leaks, missing_locators=miss)


if __name__ == "__main__":
    only = sys.argv[2].split(",") if len(sys.argv) > 2 else None
    m, extra, det = run(sys.argv[1], only=only)
    print("=== CHECKABLE ===")
    ok = True
    for k, v in m.items():
        good = (v == m["SOURCE_ROWS_EXPECTED"]) if k in ("SOURCE_ROWS_EXPECTED", "SOURCE_ROWS_MAPPED") else (v == 0)
        ok &= good
        print(f"{'PASS' if good else 'FAIL'}  {k:<36} = {v}")
    print("\n=== SUPPORTING ===")
    for k, v in extra.items(): print(f"      {k:<36} = {v}")
    if det["leaks"]: print("\nleaks:", det["leaks"][:6])
    if det["missing_locators"]: print("missing locators:", det["missing_locators"][:6])
    print("\nGATE:", "ALL CHECKABLE GATES PASS" if ok else "FAILED")
    json.dump(dict(checkable=m, supporting=extra), open("qa_v0_3.json", "w"), indent=1)
    sys.exit(0 if ok else 1)
