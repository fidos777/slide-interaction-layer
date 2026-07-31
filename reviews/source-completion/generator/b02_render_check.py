# -*- coding: utf-8 -*-
"""Render + geometric QA for the B02 review deck.

LibreOffice in this container ships without any document import filter
(libreoffice-core only), so it cannot open a .pptx at all. This renderer reads
the GENERATED PACKAGE back out of the .pptx and draws it with metric-accurate
font measurement (Liberation Sans is metric-compatible with Arial), so the
output is a render of the artifact rather than of the generator's memory.

It produces:
  * one PNG per review page, for actual visual inspection
  * an overflow / overlap / off-canvas-leak report measured in inches
"""
import json, os, re, sys, zipfile
from xml.etree import ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
EMU = 914400.0
DPI = 110
SW, SH = 13.3333, 7.5

FONTS = {
    (0, 0): "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    (1, 0): "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    (0, 1): "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf",
    (1, 1): "/usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf",
}
_cache = {}


def font(pt, b=False, i=False):
    key = (round(pt, 1), b, i)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(FONTS[(int(b), int(i))], max(1, int(round(pt * DPI / 72.0))))
    return _cache[key]


def emu(v):
    try: return int(v) / EMU
    except Exception: return 0.0


def parse_slide(xml):
    root = ET.fromstring(xml)
    tree = root.find(f"{P}cSld/{P}spTree")
    shapes = []
    for sp in tree.findall(f"{P}sp"):
        nv = sp.find(f"{P}nvSpPr/{P}cNvPr")
        name = nv.get("name") if nv is not None else ""
        xfrm = sp.find(f"{P}spPr/{A}xfrm")
        if xfrm is None:
            off = ext = None
        else:
            o, e = xfrm.find(f"{A}off"), xfrm.find(f"{A}ext")
            off = (emu(o.get("x")), emu(o.get("y"))) if o is not None else None
            ext = (emu(e.get("cx")), emu(e.get("cy"))) if e is not None else None
        spPr = sp.find(f"{P}spPr")
        fill = None
        if spPr is not None:
            sf = spPr.find(f"{A}solidFill/{A}srgbClr")
            if sf is not None: fill = sf.get("val")
            elif spPr.find(f"{A}solidFill/{A}schemeClr") is not None: fill = "EAF1F8"
        ln = None
        lnel = spPr.find(f"{A}ln") if spPr is not None else None
        if lnel is not None:
            c = lnel.find(f"{A}solidFill/{A}srgbClr")
            if c is not None: ln = c.get("val")
            elif lnel.find(f"{A}solidFill/{A}schemeClr") is not None: ln = "404040"
        body = sp.find(f"{P}txBody")
        anchor = "t"
        paras = []
        if body is not None:
            bp = body.find(f"{A}bodyPr")
            if bp is not None: anchor = bp.get("anchor") or "t"
            for p in body.findall(f"{A}p"):
                pPr = p.find(f"{A}pPr")
                algn = pPr.get("algn") if pPr is not None else None
                bullet = pPr is not None and pPr.find(f"{A}buChar") is not None
                sb = pPr.find(f"{A}spcBef/{A}spcPts") if pPr is not None else None
                spc = (int(sb.get("val")) / 100.0 / 72.0) if sb is not None else 0.0
                lvl = int(pPr.get("lvl") or 0) if pPr is not None else 0
                runs = []
                for r in p.findall(f"{A}r"):
                    rPr = r.find(f"{A}rPr")
                    t = r.find(f"{A}t")
                    if t is None or t.text is None: continue
                    sz = int(rPr.get("sz") or 1800) / 100.0 if rPr is not None else 18.0
                    b = (rPr.get("b") == "1") if rPr is not None else False
                    it = (rPr.get("i") == "1") if rPr is not None else False
                    col = "202020"
                    if rPr is not None:
                        c = rPr.find(f"{A}solidFill/{A}srgbClr")
                        if c is not None: col = c.get("val")
                    runs.append(dict(t=t.text, sz=sz, b=b, i=it, col=col))
                paras.append(dict(runs=runs, algn=algn, bullet=bullet, lvl=lvl, spc=spc))
        geom = "rect"
        if spPr is not None and spPr.find(f"{A}custGeom") is not None:
            geom = "custGeom"
            pth = spPr.find(f"{A}custGeom/{A}pathLst/{A}path")
            pts = []
            if pth is not None:
                for el in list(pth):
                    pt = el.find(f"{A}pt")
                    if pt is not None:
                        pts.append((int(pt.get("x")), int(pt.get("y"))))
                geom = ("path", int(pth.get("w") or 960), int(pth.get("h") or 960), pts)
        shapes.append(dict(name=name, off=off, ext=ext, fill=fill, ln=ln,
                           anchor=anchor, paras=paras, geom=geom))
    return shapes


INS_X, INS_Y = 0.1, 0.05


def layout(shape):
    """Return (lines, total_height_in). Each line: (text, x_off_in, y_in, h_in, run)."""
    if not shape["ext"] or not shape["paras"]: return [], 0.0
    w = shape["ext"][0] - 2 * INS_X
    out, y = [], 0.0
    for p in shape["paras"]:
        y += p.get("spc", 0.0)
        if not p["runs"]:
            y += 0.16; continue
        r0 = p["runs"][0]
        f = font(r0["sz"], r0["b"], r0["i"])
        lh = r0["sz"] * 1.21 / 72.0
        indent = 0.3125 * (p["lvl"] + 1) if p["bullet"] else 0.0
        avail = w - indent
        text = "".join(r["t"] for r in p["runs"])
        if p["bullet"]: text = "• " + text
        words, cur = text.split(), ""
        wrapped = []
        for wd in words:
            trial = (cur + " " + wd).strip()
            if f.getlength(trial) / DPI > avail and cur:
                wrapped.append(cur); cur = wd
            else:
                cur = trial
        wrapped.append(cur)
        for ln_ in wrapped:
            out.append(dict(text=ln_, y=y, h=lh, sz=r0["sz"], b=r0["b"], i=r0["i"],
                            col=r0["col"], algn=p["algn"], indent=indent))
            y += lh
    return out, y


def render(pptx, outdir, prefix="page"):
    os.makedirs(outdir, exist_ok=True)
    z = zipfile.ZipFile(pptx)
    names = sorted([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)],
                   key=lambda n: int(re.search(r"\d+", n.split("/")[-1]).group()))
    report = []
    for idx, n in enumerate(names, 1):
        shapes = parse_slide(z.read(n).decode("utf-8"))
        W, H = int(SW * DPI), int(SH * DPI)
        img = Image.new("RGB", (W, H), "white")
        d = ImageDraw.Draw(img)
        issues = []
        boxes = []
        for s in shapes:
            if not s["off"] or not s["ext"]: continue
            x, y = s["off"]; w, h = s["ext"]
            if x < 0 or y < 0:            # off-canvas production panel / title ph
                if x + w > 0.001 and x < 0:
                    issues.append(dict(kind="OFFCANVAS_LEAK", shape=s["name"],
                                       detail=f"right edge {x+w:.4f}in > 0"))
                continue
            px, py, pw, ph = x * DPI, y * DPI, w * DPI, h * DPI
            g = s.get("geom", "rect")
            if isinstance(g, tuple) and g[0] == "path":
                _, gw, gh, pts = g
                poly = [(px + qx / gw * pw, py + qy / gh * ph) for qx, qy in pts]
                if len(poly) >= 3:
                    d.polygon(poly, fill="#" + (s["fill"] or "2E7D32"))
            else:
                if s["fill"]:
                    d.rectangle([px, py, px + pw, py + ph], fill="#" + s["fill"])
                if s["ln"]:
                    d.rectangle([px, py, px + pw, py + ph], outline="#" + s["ln"], width=2)
            lines, th = layout(s)
            if th > h + 0.02:
                issues.append(dict(kind="TEXT_OVERFLOW", shape=s["name"],
                                   detail=f"text {th:.3f}in > box {h:.3f}in (+{th-h:.3f})"))
            y0 = py + INS_Y * DPI
            if s["anchor"] == "ctr":
                y0 = py + (ph - th * DPI) / 2
            for L in lines:
                f = font(L["sz"], L["b"], L["i"])
                tw = f.getlength(L["text"]) / DPI
                lx = px + (INS_X + L["indent"]) * DPI
                if L["algn"] == "ctr":
                    lx = px + (pw - tw * DPI) / 2
                d.text((lx, y0 + L["y"] * DPI), L["text"], font=f, fill="#" + L["col"])
                if tw > (w - 2 * INS_X - L["indent"]) + 0.02:
                    issues.append(dict(kind="LINE_CLIP", shape=s["name"],
                                       detail=f"'{L['text'][:34]}' {tw:.2f}in > {w-2*INS_X:.2f}in"))
            if s["fill"] or s["ln"]:
                boxes.append((s["name"], x, y, w, h))
        # containment: nothing may extend past the popup panel it belongs to
        panels = [b for b in boxes if b[0] == "PopupPanel"]
        for pn, pxx, pyy, pww, phh in panels:
            for s2 in shapes:
                if not s2["off"] or not s2["ext"]: continue
                # only the popup's own children — item cards sit BEHIND the modal
                if s2["name"] not in ("PopupTitle", "FHead", "FBody", "Btn"): continue
                x2, y2 = s2["off"]; w2, h2 = s2["ext"]
                if x2 < 0 or y2 < 0: continue
                inside_x = x2 >= pxx - 0.01 and x2 + w2 <= pxx + pww + 0.01
                starts_in = pyy - 0.01 <= y2 <= pyy + phh + 0.01
                if s2["name"] == "Btn" and not inside_x: continue
                if inside_x and starts_in:
                    _, th2 = layout(s2)
                    bottom = y2 + max(h2, th2)
                    if bottom > pyy + phh + 0.02:
                        issues.append(dict(kind="PANEL_CONTENT_OVERRUN", shape=s2["name"],
                                           detail=f"content bottom {bottom:.3f}in > panel bottom "
                                                  f"{pyy+phh:.3f}in (+{bottom-pyy-phh:.3f})"))

        # overlap among filled/bordered boxes
        for a in range(len(boxes)):
            for b in range(a + 1, len(boxes)):
                n1, x1, y1, w1, h1 = boxes[a]; n2, x2, y2, w2, h2 = boxes[b]
                ox = min(x1 + w1, x2 + w2) - max(x1, x2)
                oy = min(y1 + h1, y2 + h2) - max(y1, y2)
                if ox > 0.02 and oy > 0.02:
                    inner = (x1 >= x2 - .01 and y1 >= y2 - .01 and x1 + w1 <= x2 + w2 + .01 and y1 + h1 <= y2 + h2 + .01) or \
                            (x2 >= x1 - .01 and y2 >= y1 - .01 and x2 + w2 <= x1 + w1 + .01 and y2 + h2 <= y1 + h1 + .01)
                    if not inner:
                        issues.append(dict(kind="BOX_OVERLAP", shape=f"{n1} ∩ {n2}",
                                           detail=f"{ox:.2f}×{oy:.2f}in"))
        img.save(os.path.join(outdir, f"{prefix}{idx:03d}.png"))
        report.append(dict(slide=idx, issues=issues))
    return report


if __name__ == "__main__":
    pptx, outdir = sys.argv[1], sys.argv[2]
    rep = render(pptx, outdir)
    bad = [r for r in rep if r["issues"]]
    print(f"rendered {len(rep)} pages -> {outdir}")
    kinds = {}
    for r in bad:
        for i in r["issues"]: kinds[i["kind"]] = kinds.get(i["kind"], 0) + 1
    print("issue counts:", kinds or "none")
    for r in bad:
        for i in r["issues"]:
            print(f"  p{r['slide']:>3} {i['kind']:<16} {i['shape'][:30]:<30} {i['detail']}")
    json.dump(rep, open(os.path.join(outdir, "render_report.json"), "w"), indent=1)
