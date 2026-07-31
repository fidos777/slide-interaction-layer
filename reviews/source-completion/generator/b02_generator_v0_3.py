# -*- coding: utf-8 -*-
"""K5 PL06 T03 B02 storyboard generator — review build v0.3.

Branched from the preserved v0.1 builder; that bundle is not modified.

Reads: b02_content_v0_3.json (controlled content data)
       b02_model_v0_3.py     (screen / state / review-page model)
Writes: K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3.pptx

Rules enforced in code, not by hand-patching:
  R-2  every table-derived popup carries VO
  R-3  popups are states rendered as review pages; learner depth stays 2
  R-5  Kembali lives on the example screen, starts disabled, enables on completion
  R-6  no Kepentingan / Apa Yang Dipelajari / Isi Utama / Manfaat label on canvas
  L-01 PL pronunciation note stays off-canvas
  A-06 adaptive popup — a field absent from source renders no heading at all
  Notes grammar: VO / transcript only. Silent states get genuinely empty notes.
  Learner canvas carries no screen ID, state ID or status token.
"""
import os, re, shutil, sys, zipfile
from xml.sax.saxutils import escape as X

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b02_model_v0_3 as MODEL

HERE = os.path.dirname(os.path.abspath(__file__))
E = lambda i: str(int(round(i * 914400)))

# ============================ accepted geometry ============================
STAGE_W, STAGE_H = 13.3333, 7.5
BAND_X, BAND_W = 0.7917, 11.75
NAV_CLR, KW, KH = 0.10, 1.75, 0.38
NAV_H = NAV_CLR + KH + NAV_CLR                 # 0.58
SP_PX, SP_PY, SP_PW = 0.8046, 1.7813, 5.8621
SP_PH = (STAGE_H - NAV_H) - SP_PY              # 5.1387
HD_X, HD_Y, HD_W, HD_H = 6.8667, 1.8291, 5.6621, 0.5068
BD_X, BD_Y, BD_W, BD_H = 6.8667, 2.5594, 5.6621, 3.8708
CH, GAP_Y, LAB_R, LH, LG = 1.9901, 0.25, 0.92, 0.50, 0.0185
ROW_PITCH = CH + LG + LH + GAP_Y
TOP, INSTR_Y, INSTR_H = 1.9438, 1.2936, 0.4039
GM_TOP, GM_INSTR_Y = 1.65, 1.15      # group master only: room for global Seterusnya
F4 = dict(cw=3.935, gx=0.7074)
F5 = dict(cw=3.60, gx=0.4750)
TICK = 0.3937
GOLD, GREY, GREEN = "7F6000", "808080", "2E7D32"
DARK = ('<a:solidFill><a:schemeClr val="tx1"><a:lumMod val="85000"/>'
        '<a:lumOff val="15000"/></a:schemeClr></a:solidFill>')
LEX = {"Water Feature", "Drinking Fountain", "BBQ Pit"}


def grid4():
    cw, gx = F4["cw"], F4["gx"]
    x0 = (STAGE_W - (2 * cw + gx)) / 2
    return [(x0 + c * (cw + gx), GM_TOP + r * ROW_PITCH) for r in range(2) for c in range(2)], cw, x0, 2 * cw + gx


def grid5():
    cw, gx = F5["cw"], F5["gx"]
    w2 = 2 * cw + gx
    r2 = (STAGE_W - w2) / 2
    return ([(BAND_X + i * (cw + gx), GM_TOP) for i in range(3)] +
            [(r2 + i * (cw + gx), GM_TOP + ROW_PITCH) for i in range(2)]), cw, BAND_X, 3 * cw + 2 * gx


def item_grid(n):
    """Level 2 item cards. Label sits inside the card, so no label-width coupling."""
    h = 1.62
    y0 = 2.15
    if n <= 3:
        gx = 0.45
        cw = (BAND_W - (n - 1) * gx) / n
        return [(BAND_X + i * (cw + gx), y0) for i in range(n)], cw, h
    if n == 4:
        gx = 0.40
        cw = (BAND_W - 3 * gx) / 4
        return [(BAND_X + i * (cw + gx), y0) for i in range(4)], cw, h
    gx = 0.4750
    cw = F5["cw"]
    w2 = 2 * cw + gx
    return ([(BAND_X + i * (cw + gx), y0) for i in range(3)] +
            [((STAGE_W - w2) / 2 + i * (cw + gx), y0 + h + 0.34) for i in range(2)]), cw, h


# ============================ emitters ============================
def runs(parts, sz=None, b=False, clr=None, dark=False):
    o = ""
    for t, it in parts:
        a = ' lang="en-MY"'
        if sz: a += f' sz="{sz}"'
        if b: a += ' b="1"'
        if it: a += ' i="1"'
        fill = f'<a:solidFill><a:srgbClr val="{clr}"/></a:solidFill>' if clr else (DARK if dark else "")
        o += f'<a:r><a:rPr{a} dirty="0">{fill}</a:rPr><a:t>{X(t)}</a:t></a:r>'
    return o


def nv(i, n): return f'<p:cNvPr id="{i}" name="{n}"/>'


def box(i, name, x, y, w, h, inner, fill=None, ln=None, anchor=None, af="noAutofit", lnw=19050, dash=True):
    f = f'<a:solidFill><a:srgbClr val="{fill}"/></a:solidFill>' if fill else "<a:noFill/>"
    d = '<a:prstDash val="dash"/>' if dash else ""
    l = (f'<a:ln w="{lnw}"><a:solidFill><a:srgbClr val="{ln}"/></a:solidFill>{d}</a:ln>') if ln else ""
    an = f' anchor="{anchor}"' if anchor else ""
    return (f'<p:sp><p:nvSpPr>{nv(i,name)}<p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>{f}{l}</p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square"{an}><a:{af}/></a:bodyPr><a:lstStyle/>{inner}</p:txBody></p:sp>')


def para(lines, sz=1400, b=False, clr=None, algn=None, dark=True, spc=0):
    o = ""
    for t in lines:
        a = f'<a:pPr algn="{algn}">' if algn else "<a:pPr>"
        a += f'<a:spcBef><a:spcPts val="{spc}"/></a:spcBef>' if spc else ""
        a += "</a:pPr>"
        parts = t if isinstance(t, list) else [(t, False)]
        o += f"<a:p>{a}{runs(parts, sz=sz, b=b, clr=clr, dark=dark)}</a:p>"
    return o


def txt(i, name, x, y, w, h, lines, **kw):
    af = kw.pop("af", "noAutofit")
    fill = kw.pop("fill", None); ln = kw.pop("ln", None)
    anchor = kw.pop("anchor", None); dash = kw.pop("dash", True)
    return box(i, name, x, y, w, h, para(lines, **kw), fill=fill, ln=ln, anchor=anchor, af=af, dash=dash)


def bullets(i, name, x, y, w, h, items, sz=1400, spc=None):
    ps = ""
    for lv, parts in items:
        marL = 285750 * (lv + 1)
        lvl = f' lvl="{lv}"' if lv else ""
        sb = f'<a:spcBef><a:spcPts val="{spc}"/></a:spcBef>' if spc else ""
        ps += (f'<a:p><a:pPr marL="{marL}"{lvl} indent="-285750">{sb}'
               '<a:buFont typeface="Arial" panose="020B0604020202020204" pitchFamily="34" charset="0"/>'
               '<a:buChar char="&#8226;"/></a:pPr>' + runs(parts, sz=sz, dark=True) + "</a:p>")
    return box(i, name, x, y, w, h, ps)


def panel(i, x, y, w, h, lines, sz=1200, name="Rectangle 9"):
    ps = ""
    for k, t in enumerate(lines):
        ps += f'<a:p>{runs([(t, False)], sz=(1100 if k == 0 else sz), b=(k == 0), dark=True)}</a:p>'
    return (f'<p:sp><p:nvSpPr>{nv(i,name)}<p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(w)}" cy="{E(h)}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
            '<a:solidFill><a:schemeClr val="accent2"><a:lumMod val="10000"/>'
            '<a:lumOff val="90000"/></a:schemeClr></a:solidFill>'
            '<a:ln><a:noFill/></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr rtlCol="0" anchor="t"/><a:lstStyle/>{ps}</p:txBody></p:sp>')


def card(i, x, y, w, h, label, ital=False, sz=1600, viewed=False):
    fill = "E8F5E9" if viewed else None
    edge = GREEN if viewed else "404040"
    inner = ('<a:p><a:pPr algn="ctr"/>' +
             runs([(label, ital)], sz=sz, b=True, dark=True) + "</a:p>")
    return box(i, "ItemCard", x, y, w, h, inner,
               fill=(fill or "F2F2F2"), ln=edge, anchor="ctr", dash=False,
               lnw=(28575 if viewed else 12700))


CHK = [(861, 158), (349, 642), (103, 390), (18, 471), (345, 807), (431, 727), (942, 242)]


def tick(i, x, y, size=TICK):
    pts = "".join((f'<a:moveTo><a:pt x="{px}" y="{py}"/></a:moveTo>' if k == 0
                   else f'<a:lnTo><a:pt x="{px}" y="{py}"/></a:lnTo>')
                  for k, (px, py) in enumerate(CHK))
    return (f'<p:sp><p:nvSpPr>{nv(i,"Tick")}<p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(size)}" cy="{E(size)}"/></a:xfrm>'
            '<a:custGeom><a:avLst/><a:gdLst/><a:ahLst/><a:cxnLst/><a:rect l="0" t="0" r="r" b="b"/>'
            f'<a:pathLst><a:path w="960" h="960">{pts}<a:close/></a:path></a:pathLst></a:custGeom>'
            f'<a:solidFill><a:srgbClr val="{GREEN}"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr>'
            '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="en-MY"/></a:p></p:txBody></p:sp>')


def button(i, x, y, w, h, label, enabled):
    """Learner control. Disabled state is drawn, never described on canvas."""
    fill = "1F4E79" if enabled else "D9D9D9"
    clr = "FFFFFF" if enabled else GREY
    inner = '<a:p><a:pPr algn="ctr"/>' + runs([(label, False)], sz=1600, b=True, clr=clr) + "</a:p>"
    return box(i, "Btn", x, y, w, h, inner, fill=fill,
               ln=("1F4E79" if enabled else "BFBFBF"), anchor="ctr", dash=False, lnw=12700)


def titlebar(i, t, w=12.0075):
    it = ' i="1"' if t in LEX else ""
    return (f'<p:sp><p:nvSpPr>{nv(i,"TextBox 5")}<p:cNvSpPr txBox="1"/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E(0.6758)}" y="{E(0.42)}"/><a:ext cx="{E(w)}" cy="{E(0.6479)}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr>'
            '<p:txBody><a:bodyPr wrap="square" rtlCol="0"><a:noAutofit/></a:bodyPr><a:lstStyle/>'
            '<a:p><a:pPr><a:lnSpc><a:spcPts val="3600"/></a:lnSpc></a:pPr>'
            f'<a:r><a:rPr lang="en-MY" sz="3600" b="1"{it} dirty="0"/><a:t>{X(t)}</a:t></a:r></a:p></p:txBody></p:sp>')


def title_ph(t):
    return ('<p:sp><p:nvSpPr><p:cNvPr id="2" name="Title 1"/><p:cNvSpPr><a:spLocks noGrp="1"/></p:cNvSpPr>'
            '<p:nvPr><p:ph type="title"/></p:nvPr></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="0" y="{E(-0.6311)}"/><a:ext cx="{E(13.3333)}" cy="{E(0.5722)}"/></a:xfrm></p:spPr>'
            '<p:txBody><a:bodyPr><a:noAutofit/></a:bodyPr><a:lstStyle/>'
            f'<a:p><a:r><a:rPr lang="en-MY" sz="2400" b="1" dirty="0"/><a:t>{X(t)}</a:t></a:r></a:p></p:txBody></p:sp>')


HDR = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<p:sld '
       'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
       'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
       'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"><p:cSld><p:spTree>'
       '<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
       '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/>'
       '<a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>')
FTR = '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>'

TOKENS = ["REVIEW_READY", "PROVISIONAL_CAIR_EXECUTION",
          "CAIR_INTEGRITY_EXCEPTION_FOR_REVIEW_BUILD_ONLY",
          "PENDING_FINAL_BARIAH_CONFIRMATION", "NOT_FOR_MMD_BUILD", "MULTIMEDIA_NOT_PRODUCED"]


def prodpanel(i, page, screen, lines):
    head = ["K5 PL06 T03 B02 — PAPAN CERITA v0.3 (BUILD SEMAKAN)",
            " · ".join(TOKENS[:2]), " · ".join(TOKENS[2:4]), " · ".join(TOKENS[4:]),
            "Tiada imej, audio, video atau animasi dibenamkan.", "",
            f"REVIEW PAGE: {page['id']}  ({page['variant']})",
            f"PHYSICAL LEARNER SCREEN: {screen['id']}  [{screen['kind']}]", ""]
    body = ""
    for k, t in enumerate(head + lines):
        b = (k == 0) or (t[:1].isupper() and t.endswith(":")) or t.split(":")[0] in (
            "REVIEW PAGE", "PHYSICAL LEARNER SCREEN", "RUNTIME STATE", "INTERAKSI",
            "NAVIGASI", "SUMBER", "NOTA MMD", "STATUS", "PERSISTEN", "LEVEL")
        body += f'<a:p>{runs([(t, False)], sz=900, b=b, dark=True)}</a:p>'
    return (f'<p:sp><p:nvSpPr>{nv(i,"Rectangle 8")}<p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E(-6.90)}" y="0"/><a:ext cx="{E(6.60)}" cy="{E(7.5)}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
            '<a:solidFill><a:srgbClr val="FFF2CC"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr rtlCol="0" anchor="t"/><a:lstStyle/>{body}</p:txBody></p:sp>')


# ============================ page builders ============================
def _sec(i, x, y, w, head, body_lines, sz=1300):
    """One adaptive popup field. Never emitted when the source field is absent."""
    o = [txt(i, "FieldHead", x, y, w, 0.26, [head], sz=1000, b=True, clr=GOLD)]
    o.append(txt(i + 1, "FieldBody", x, y + 0.28, w, 0.30, body_lines, sz=sz))
    return o


def build_page(M, page):
    """Return (shapes, notes_text). notes_text is VO/transcript only, or ''. """
    D = M["content"]; F = D["frames"]
    scr = next(s for s in M["screens"] if s["id"] == page["screen"])
    kind, var, pay = scr["kind"], page["variant"], page["payload"]
    sh, notes, pl = [], "", []
    sid = 30

    def add(*shapes):
        nonlocal sid
        for s in shapes:
            sh.append(s)

    # ---------------- frame screens ----------------
    if scr["id"] == "S01":
        f = F["s01"]
        add(title_ph(f["title"]), titlebar(6, f["title"]),
            txt(20, "Course", BAND_X, 2.30, BAND_W, 0.60, [f["course"]], sz=2600, b=True, algn="ctr"),
            txt(21, "Topic", BAND_X, 3.05, BAND_W, 0.50, [f["topic"]], sz=2000, algn="ctr"),
            panel(22, BAND_X, 3.95, BAND_W, 1.30, ["ARAHAN VISUAL — SPESIFIKASI SAHAJA",
                  "[Visual: Imej pembuka bahagian — foto tapak landskap siap yang memaparkan",
                  "struktur taman dan perabot taman dalam satu bingkai. Tidak dibenamkan.]"]),
            button(24, (STAGE_W - 2.4) / 2, 5.75, 2.4, 0.62, f["button"], True))
        notes = f["vo"]
        pl = ["INTERAKSI:", "  Butang MULA. Tiada auto-advance.",
              "NAVIGASI:", "  MULA -> S02.",
              "SUMBER:", "  Rentetan kursus/topik disahkan. Tiada halaman modul khusus.",
              "NOTA MMD:", f"  {f['mmd']}", "  Tiada aset diikat.",
              "STATUS:", "  PENDING_FINAL_BARIAH_CONFIRMATION"]

    elif scr["id"] == "S02":
        f = F["s02"]
        add(title_ph(f["title"]), titlebar(6, f["title"]),
            panel(19, BAND_X, 1.45, BAND_W, 1.05, ["ARAHAN VISUAL — SPESIFIKASI SAHAJA",
                  "[Visual: Latar tapak landskap dalam pembinaan. Dua watak neutral peranan",
                  "berdiri di kawasan yang sudah ditanam, struktur taman di latar belakang.]"]))
        w = (BAND_W - 0.6) / 2
        for k, (role, _) in enumerate(f["dialogue"][:2]):
            add(box(30 + k, "Char", BAND_X + k * (w + 0.6), 2.85, w, 1.85,
                    para(["", role], sz=1800, b=True, algn="ctr", dark=True),
                    fill="F2F2F2", ln="404040", anchor="ctr", dash=False, lnw=12700))
        add(txt(40, "CharNote", BAND_X, 4.95, BAND_W, 0.42,
                ["Dialog penuh dimainkan sebagai video watak. Teks dialog berada dalam Notes."],
                sz=1300, algn="ctr", clr=GOLD))
        notes = "\n".join(f"{r}: {l}" for r, l in f["dialogue"])
        pl = ["INTERAKSI:", "  Tiada interaksi pengguna. Video watak dimainkan, kemudian auto ke S03.",
              "NAVIGASI:", "  S02 -> S03.",
              "SUMBER:", "  Premis diterbitkan daripada modul ms 237 dan ms 242. Dialog ditulis, bukan petikan.",
              "NOTA MMD:", "  Watak NEUTRAL PERANAN. Nama watak belum diluluskan.",
              "  Tiada dakwaan MS2680 dibuat pada skrin ini.",
              "STATUS:", "  PENDING_FINAL_BARIAH_CONFIRMATION — penamaan watak"]

    elif scr["id"] == "S03":
        f = F["s03"]
        gl = [f'{g["name"]}: ' + ", ".join(M["comps"][c]["name"] for c in M["order"]
              if M["comps"][c]["group"] == g["id"]) for g in D["groups"]]
        add(title_ph(f["title"]), titlebar(6, f["title"]),
            panel(19, BAND_X, 1.42, 4.35, 2.30, ["ARAHAN VISUAL", "[Visual: Kad narator Hilmi —",
                  "potret separuh badan, pakaian", "kerja lapangan, latar tapak", "landskap kabur.]"]),
            txt(20, "Narr", 5.45, 1.42, 7.10, 0.45, ["Hilmi"], sz=2400, b=True),
            txt(21, "NarrRole", 5.45, 1.95, 7.10, 0.38, ["Narator kursus"], sz=1500),
            txt(22, "Groups", 5.45, 2.45, 7.10, 1.30, gl, sz=1400, spc=300),
            panel(23, BAND_X, 3.90, BAND_W, 1.55, ["ARAHAN VISUAL — MIND MAP (SPESIFIKASI TEKS SAHAJA)"] +
                  _wrap_lines(f["mindmap"], 96)),
            txt(24, "Reflect", BAND_X, 5.65, BAND_W, 0.75, [f["reflect"]], sz=1500, b=True))
        notes = f["vo"]
        pl = ["INTERAKSI:", "  Tiada interaksi pengguna. Auto ke Level 1 selepas VO.",
              "NAVIGASI:", "  S03 -> STRUKTUR_TAMAN_MASTER.",
              "SUMBER:", "  Senarai komponen daripada modul ms 237 dan ms 242.",
              "NOTA MMD:", "  Mind Map ialah SPESIFIKASI TEKS. Aset Mind Map TIDAK dihasilkan.",
              "  VO S03 sahaja bermula dengan label penutur 'Hilmi:'.",
              "STATUS:", "  PENDING_FINAL_BARIAH_CONFIRMATION"]

    elif scr["id"] == "RUMUSAN":
        f = F["rumusan"]
        add(title_ph(f["title"]), titlebar(6, f["title"]),
            panel(19, BAND_X, 1.42, BAND_W, 0.95, ["ARAHAN VISUAL"] + _wrap_lines(f["visual"], 96)),
            txt(24, "RumHead", BAND_X, 2.60, BAND_W, 0.45, [f["heading"]], sz=1800, b=True),
            bullets(25, "RumBody", BAND_X, 3.15, BAND_W, 3.20,
                    [(0, [(t, i) for t, i in b]) for b in f["bullets"]], sz=1500, spc=600))
        notes = f["vo"]
        pl = ["INTERAKSI:", "  Tiada interaksi pengguna. Auto ke Kuiz selepas VO.",
              "NAVIGASI:", "  RUMUSAN -> KUIZ.",
              "SUMBER:", "  Modul ms 237-250 (skop bahagian).",
              "NOTA MMD:", "  Label struktur TIDAK dipaparkan (Kepentingan / Apa Yang Dipelajari /",
              "  Isi Utama / Manfaat). Logik asas kekal memandu susunan sahaja.",
              "  Bahasa kontraktor/aplikasi tapak. Tiada 'anda' generik.",
              "STATUS:", "  Klausa aplikasi tapak — PENDING_HUMAN (R-6)"]

    elif scr["id"] == "KUIZ":
        f = F["kuiz"]
        rows = []
        for q in f["items"]:
            rows.append((0, [(f"Soalan {q['n']} · {q['typ']} — {q['stem']}", False)]))
            rows.append((1, [(f"Jawapan: {q['key']}   ·   Pilihan: {len(q['opts'])}   ·   Sumber: {q['src']}", False)]))
        add(title_ph(f["title"]), titlebar(6, f["title"]),
            txt(20, "QHead", BAND_X, 1.30, BAND_W, 0.34,
                [f"5 soalan — 4 MCQ + 1 Multiple Response   ·   Lulus: {f['pass_mark']}"], sz=1400, b=True),
            bullets(21, "QBody", BAND_X, 1.72, BAND_W, 4.55, rows, sz=1250, spc=300),
            button(40, BAND_X, 6.55, 2.9, 0.52, "Semak Jawapan", True),
            button(41, BAND_X + 3.2, 6.55, 2.9, 0.52, "Ulang Kuiz", True))
        notes = f["vo"]
        pl = ["INTERAKSI:", "  5 item satu demi satu. Maklum balas serta-merta setiap item.",
              "  Semak Jawapan dan Ulang Kuiz selepas keputusan. Ulangan bersifat sukarela.",
              "STATE / PERALIHAN:", "  Lulus = 3/5 = 60%. Keputusan memaparkan skor dan Lulus / Tidak Lulus.",
              "  Skor bawah 60% TIDAK menghalang progression.",
              "NAVIGASI:", "  KUIZ -> TAMAT.",
              "SUMBER:", "  Item diterbitkan daripada modul ms 238-249. Modul tiada bank soalan.",
              "NOTA MMD:", "  Teks penuh pilihan dan maklum balas berada dalam Notes.",
              "STATUS:", "  PENDING_FINAL_BARIAH_CONFIRMATION — kandungan penilaian"]
        qn = [f["vo"], ""]
        for q in f["items"]:
            qn += [f"Soalan {q['n']} — {q['typ']} (sumber: {q['src']})", q["stem"]]
            qn += [f"   {L}. {t}" for L, t in q["opts"]]
            qn += [f"Jawapan betul: {q['key']}",
                   f"Maklum balas betul: {q['ok']}", f"Maklum balas salah: {q['bad']}", ""]
        notes = "\n".join(qn).rstrip()

    elif scr["id"] == "TAMAT":
        f = F["tamat"]
        add(title_ph(f["title"]), titlebar(6, f["title"]),
            panel(19, BAND_X, 1.45, BAND_W, 1.00, ["ARAHAN VISUAL"] + _wrap_lines(f["visual"], 96)),
            txt(20, "Close", BAND_X, 3.05, BAND_W, 1.40, f["lines"], sz=2000, spc=600, algn="ctr"),
            button(24, (STAGE_W - 2.6) / 2, 5.20, 2.6, 0.62, "Seterusnya", True))
        notes = f["vo"]
        pl = ["INTERAKSI:", "  Butang Seterusnya.",
              "NAVIGASI:", "  Destinasi seterusnya BELUM DISAHKAN — metadata produksi sahaja.",
              "  Tiada andaian laluan dipaparkan pada kanvas pelajar.",
              "SUMBER:", "  Tiada halaman modul khusus.",
              "NOTA MMD:", "  Sasaran laluan mesti disahkan terhadap struktur Topik/Bahagian",
              "  sebelum binaan MMD.",
              "STATUS:", "  PENDING_FINAL_BARIAH_CONFIRMATION — sasaran laluan"]

    # ---------------- Level 1 group master ----------------
    elif kind == "GROUP_MASTER":
        g = M["groups"][scr["group"]]
        members = [c for c in M["order"] if M["comps"][c]["group"] == g["id"]]
        pos, cw, gx0, gw = (grid4() if len(members) == 4 else grid5())
        lw = cw * LAB_R
        add(title_ph(g["name"]), titlebar(6, g["name"]),
            txt(25, "Instr", gx0, GM_INSTR_Y, gw, INSTR_H, [g["instr"]], sz=1600, algn="ctr"))
        n = 40
        for (x, y), cid in zip(pos, members):
            c = M["comps"][cid]
            ital = bool(c.get("ital"))
            add(panel(n, x, y, cw, CH, ["ARAHAN VISUAL", f"[Visual: {c['name']}]"] + _card_cue(c["visual"])))
            n += 1
            add(box(n, "TextBox 3", x + (cw - lw) / 2, y + CH + LG, lw, LH,
                    '<a:p><a:pPr algn="ctr"/>' + runs([(c["name"], ital)], sz=1800, b=True) + "</a:p>",
                    fill="DEEAF6", ln="404040", anchor="ctr", dash=False, lnw=12700))
            n += 1
        if var == "GROUP_COMPLETE":
            for (x, y) in pos:
                add(tick(n, x + (cw - TICK) / 2, y + (CH - TICK) / 2)); n += 1
        add(button(90, STAGE_W - 2.40 - 0.7917, STAGE_H - NAV_H + NAV_CLR, 2.40, KH,
                   "Seterusnya", var == "GROUP_COMPLETE"))
        notes = g["vo"] if var == "BASE" else ""
        done = "SEMUA kad selesai" if var == "GROUP_COMPLETE" else "tiada kad selesai"
        pl = ["LEVEL: 1 — group master",
              "INTERAKSI:", "  Kad komponen boleh diklik dalam sebarang susunan.",
              "  Kad kekal boleh diklik selepas selesai, untuk semakan.",
              "RUNTIME STATE:", f"  group_complete[{g['id']}] = semua component_complete benar",
              f"  Keadaan pada halaman ini: {done}",
              "  Seterusnya dikunci sehingga group_complete benar.",
              "PERSISTEN:", "  Tik kad dan Seterusnya kekal selepas lawatan semula dan LMS resume.",
              "  Kawalan yang telah dibuka TIDAK dikunci semula.",
              "NAVIGASI:", f"  Kad -> [komponen]_MAIN.   Seterusnya -> {scr['nav_target']}",
              "SUMBER:", f"  Modul ms {g['ms']} (fizikal {g['phys']}).",
              "NOTA MMD:", "  Tik dilukis sebagai geometri native, bukan imej.",
              "STATUS:", "  PROVISIONAL_CAIR_EXECUTION"]
        if var == "GROUP_COMPLETE":
            pl += ["  Halaman ini ialah REVIEW PAGE bagi satu runtime state.",
                   "  Ia BUKAN skrin pelajar tambahan."]

    # ---------------- main explanation ----------------
    elif kind == "MAIN":
        c = M["comps"][scr["comp"]]
        ital = bool(c.get("ital"))
        add(title_ph(c["name"]), titlebar(7, M["groups"][scr["group"]]["name"]),
            panel(8, SP_PX, SP_PY, SP_PW, SP_PH, ["ARAHAN VISUAL — TIDAK DIBENAMKAN", ""] +
                  _wrap_lines(c["visual"], 40)),
            box(10, "Head", HD_X, HD_Y, HD_W, HD_H,
                '<a:p>' + runs([(c["name"], ital)], sz=1800, b=True) + '</a:p>'),
            bullets(9, "Body", BD_X, BD_Y, BD_W, BD_H,
                    [(0, [(t, False)]) for t in c["display"]], sz=1500, spc=400),
            button(11, STAGE_W - 2.75 - 0.7917, 6.86, 2.75, 0.50, "Seterusnya", False))
        notes = c["vo"] + f" Mari lihat contoh bagi {c['name']} di halaman seterusnya."
        pl = ["LEVEL: 1 child — skrin penerangan utama",
              "INTERAKSI:", "  Tiada interaksi kandungan. Satu butang Seterusnya.",
              "RUNTIME STATE:", f"  main_vo_complete[{c['id']}] — benar apabila VO skrin tamat",
              "  Seterusnya DIKUNCI sehingga VO tamat.",
              "NAVIGASI:", f"  Seterusnya -> {scr['nav_target']}",
              "  Skrin ini TIDAK membawa Kembali ke group master (R-5).",
              "SUMBER:", f"  Modul ms {c['ms']} (fizikal {c['phys']}).",
              "NOTA MMD:", "  VO diakhiri dengan ayat penghubung wajib ke skrin contoh.",
              "  Tiada aset imej diikat.",
              "STATUS:", "  PROVISIONAL_CAIR_EXECUTION"]
        if c.get("note"):
            pl.insert(-2, "  " + c["note"])

    # ---------------- Level 2 example screen ----------------
    elif kind == "EXAMPLES":
        c = M["comps"][scr["comp"]]
        items = M["by_comp"][c["id"]]
        pos, cw, chh = item_grid(len(items))
        viewed = set(pay.get("viewed", []))
        add(title_ph(f"Contoh {c['name']}"), titlebar(6, f"Contoh {c['name']}"),
            txt(25, "Instr", BAND_X, 1.32, BAND_W, 0.42,
                ["Klik pada setiap item untuk penjelasan lanjut."], sz=1600, algn="ctr"))
        n = 40
        for k, ((x, y), r) in enumerate(zip(pos, items), 1):
            st = f"{c['id']}_EXAMPLE_{k:02d}"
            v = st in viewed
            add(card(n, x, y, cw, chh, r["label"], sz=1500, viewed=v)); n += 1
            if v:
                add(tick(n, x + cw - 0.46, y + 0.10, 0.34)); n += 1
        add(button(95, (STAGE_W - KW) / 2, STAGE_H - NAV_H + NAV_CLR, KW, KH,
                   "Kembali", bool(pay.get("kembali"))))
        if var == "POPUP":
            _popup(add, M, page, c)
        # notes: VO only. Base + all-viewed carry no new VO (silent states).
        if var == "POPUP":
            pi = MODEL.popup_index(M)
            notes = pi[pay["popup_state"]][1]["vo"]
        else:
            notes = ""
        allv = f"{len(viewed)}/{len(items)} item dilihat"
        pl = ["LEVEL: 2 — skrin contoh (Contoh [Nama Komponen])",
              "INTERAKSI:", "  Item boleh diklik dalam sebarang susunan.",
              "  Setiap item membuka SATU popup. Popup ialah STATE, bukan Level 3.",
              "  Menutup popup kembali ke skrin contoh yang sama.",
              "RUNTIME STATE:", f"  item_viewed[...] — {allv}",
              f"  component_complete[{c['id']}] = semua item_viewed benar",
              "  Kembali DIKUNCI sehingga component_complete benar.",
              "PERSISTEN:", "  Tik item dan Kembali kekal selepas lawatan semula dan LMS resume.",
              "NAVIGASI:", f"  Kembali -> {scr['nav_target']} (group master, R-5)",
              "SUMBER:"]
        for k, r in enumerate(items, 1):
            pl.append(f"  {c['id']}_EXAMPLE_{k:02d}  <-  {r['uid']}  (ms {r['ms']}/fiz {r['phys']})")
        pl += ["NOTA MMD:", "  Setiap popup membawa VO (R-2, mengatasi peraturan No-VO v1.0).",
               "  Medan popup bersifat adaptif — medan yang tiada dalam sumber tidak dirender.",
               "STATUS:", "  PROVISIONAL_CAIR_EXECUTION"]
        if c.get("single_item"):
            pl += ["  SINGLE_ITEM_EXAMPLE_TREATMENT",
                   "  PENDING_FINAL_BARIAH_CONFIRMATION — A-05 rawatan satu item.",
                   "  Identiti sumber kekal: 1 baris sumber bermakna. Tiada pemecahan dibuat."]
        if var == "POPUP":
            pl.insert(0, f"RUNTIME STATE DIPAPARKAN: {pay['popup_state']}")
        if var in ("POPUP", "ALL_VIEWED"):
            pl += ["  Halaman ini ialah REVIEW PAGE bagi satu runtime state.",
                   "  Ia BUKAN skrin pelajar tambahan."]

    sh.append(prodpanel(9, page, scr, pl))
    return sh, notes


def _card_cue(v):
    """Short, complete visual cue for a Level 1 card. Never a truncated sentence."""
    v = v or ""
    if "TIADA IMEJ SUMBER" in v:
        return ["TIADA IMEJ SUMBER", "Cadangan rajah native —", "lihat panel produksi"]
    out = []
    m = re.search(r"(Rajah \d+(?: dan Rajah \d+)?)", v)
    if m: out.append(m.group(1))
    elif "Foto jadual" in v: out.append("Foto jadual spesifikasi")
    m2 = re.search(r"(modul ms [\d\u2013-]+)", v)
    if m2: out.append(m2.group(1))
    out.append("Tidak dibenamkan")
    return out


def _wrap_lines(s, width):
    out, cur = [], ""
    for w in (s or "").split():
        if len(cur) + len(w) + 1 > width:
            out.append(cur); cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur: out.append(cur)
    return out


def _popup(add, M, page, c):
    """Adaptive popup overlay (A-06). Absent source fields render nothing at all."""
    pi = MODEL.popup_index(M)
    cid, r, idx = pi[page["payload"]["popup_state"]]
    PX, PW = 1.35, 10.6333
    PY_MIN, PY_MAX_BOTTOM = 1.42, 6.88   # usable band between title bar and nav strip
    fields = []
    if r.get("jenis") and r["jenis"].strip() != r["label"].strip():
        fields.append(("JENIS / BAHAN", [r["jenis"]]))
    if r.get("fungsi"):
        lab = "FUNGSI & PENERANGAN" if not r["fungsi"].startswith(("Bahan", "Bahan panel")) else "SPESIFIKASI"
        fields.append((lab, [l for l in r["fungsi"].split("\n")]))
    if r.get("contoh"): fields.append(("CONTOH", [r["contoh"]]))
    if r.get("visual"): fields.append(("ARAHAN VISUAL — TIDAK DIBENAMKAN", _wrap_lines(r["visual"], 100)))
    # measure, stepping the body font down only if the content will not otherwise fit
    FOOT = 0.72                      # reserved footer band for Tutup
    AVAIL = PY_MAX_BOTTOM - PY_MIN
    for bsz, cpl, lead in ((1250, 96, 0.235), (1150, 105, 0.216), (1050, 115, 0.198)):
        body_h = 0.0
        blocks = []
        for head, lines in fields:
            wrapped = []
            for l in lines:
                wrapped += _wrap_lines(l, cpl) or [""]
            h = 0.26 + 0.02 + len(wrapped) * lead + 0.14
            blocks.append((head, wrapped, h, lead)); body_h += h
        ph = max(2.1, 0.62 + body_h + FOOT)
        if ph <= AVAIL:
            break
    ph = min(ph, AVAIL)
    PY = PY_MIN if ph > AVAIL - 0.5 else 1.90
    add(box(200, "PopupPanel", PX, PY, PW, ph, "", fill="FFFFFF", ln="1F4E79", dash=False, lnw=28575))
    add(txt(201, "PopupTitle", PX + 0.28, PY + 0.16, PW - 2.0, 0.40,
            [r["label"]], sz=2000, b=True))
    y = PY + 0.62
    i = 210
    for head, wrapped, h, lead in blocks:
        add(txt(i, "FHead", PX + 0.28, y, PW - 0.56, 0.24, [head], sz=950, b=True, clr=GOLD)); i += 1
        add(txt(i, "FBody", PX + 0.28, y + 0.26, PW - 0.56, max(0.24, len(wrapped) * lead),
                wrapped, sz=bsz)); i += 1
        y += h
    add(button(260, PX + PW - 1.55, PY + ph - FOOT + 0.14, 1.30, 0.44, "Tutup", True))


# ============================ package ============================
DONOR = os.path.join(HERE, "donor_skeleton")
OUTNAME = "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_3.pptx"


def generate(outdir, only=None, outname=None):
    """only=list of component ids -> proof build. None -> full deck."""
    M = MODEL.build()
    pages = M["pages"]
    if only:
        keep = set(only)
        pages = [p for p in pages
                 if (next(s for s in M["screens"] if s["id"] == p["screen"]).get("comp") in keep)]
    work = os.path.join(outdir, "_build")
    if os.path.exists(work): shutil.rmtree(work)
    shutil.copytree(DONOR, work)
    rd = lambda p: open(os.path.join(work, p), encoding="utf-8").read()
    wr = lambda p, s: open(os.path.join(work, p), "w", encoding="utf-8").write(s)
    for d in ("ppt/slides", "ppt/notesSlides"):
        os.makedirs(os.path.join(work, d, "_rels"), exist_ok=True)
        for f in os.listdir(os.path.join(work, d)):
            if f.endswith(".xml"): os.remove(os.path.join(work, d, f))
        for f in os.listdir(os.path.join(work, d, "_rels")): os.remove(os.path.join(work, d, "_rels", f))

    NOTE_DONOR = open(os.path.join(DONOR, "ppt/notesSlides/notesSlide4.xml"), encoding="utf-8").read()
    m = re.search(r'(<p:sp>(?:(?!</p:sp>).)*?type="body".*?)(<a:p>.*?)(</p:txBody></p:sp>)', NOTE_DONOR, re.S)
    NRELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships '
             'xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
             '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
             'relationships/notesMaster" Target="../notesMasters/notesMaster1.xml"/>'
             '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
             'relationships/slide" Target="../slides/slide{n}.xml"/></Relationships>')
    manifest = []
    for i, page in enumerate(pages, 1):
        shapes, notes = build_page(M, page)
        wr(f"ppt/slides/slide{i}.xml", HDR + "".join(shapes) + FTR)
        wr(f"ppt/slides/_rels/slide{i}.xml.rels",
           '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships '
           'xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
           '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
           'relationships/slideLayout" Target="../slideLayouts/slideLayout7.xml"/>'
           f'<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
           f'relationships/notesSlide" Target="../notesSlides/notesSlide{i}.xml"/></Relationships>')
        body = "".join('<a:p><a:r><a:rPr lang="en-MY" dirty="0"/><a:t>%s</a:t></a:r></a:p>' % X(t)
                       if t else '<a:p><a:endParaRPr lang="en-MY" dirty="0"/></a:p>'
                       for t in (notes.split("\n") if notes else []))
        if not body: body = '<a:p><a:endParaRPr lang="en-MY" dirty="0"/></a:p>'
        wr(f"ppt/notesSlides/notesSlide{i}.xml", NOTE_DONOR[:m.start(2)] + body + NOTE_DONOR[m.end(2):])
        wr(f"ppt/notesSlides/_rels/notesSlide{i}.xml.rels", NRELS.replace("{n}", str(i)))
        manifest.append(dict(slide=i, page=page["id"], screen=page["screen"],
                             variant=page["variant"], notes_chars=len(notes)))
    N = len(pages)
    s = rd("ppt/presentation.xml")
    s = re.sub(r"<p:sldIdLst>.*?</p:sldIdLst>",
               "<p:sldIdLst>" + "".join(f'<p:sldId id="{9400+i}" r:id="rId{100+i}"/>'
                                        for i in range(1, N + 1)) + "</p:sldIdLst>", s, flags=re.S)
    s = re.sub(r"<p:custDataLst>.*?</p:custDataLst>", "", s, flags=re.S)
    wr("ppt/presentation.xml", s)
    R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/"
    rels = ['<Relationship Id="rId1" Type="%sslideMaster" Target="slideMasters/slideMaster1.xml"/>' % R]
    rels += ['<Relationship Id="rId%d" Type="%sslide" Target="slides/slide%d.xml"/>' % (100 + i, R, i)
             for i in range(1, N + 1)]
    rels += ['<Relationship Id="rId2" Type="%snotesMaster" Target="notesMasters/notesMaster1.xml"/>' % R,
             '<Relationship Id="rId3" Type="%spresProps" Target="presProps.xml"/>' % R,
             '<Relationship Id="rId4" Type="%sviewProps" Target="viewProps.xml"/>' % R,
             '<Relationship Id="rId5" Type="%stheme" Target="theme/theme1.xml"/>' % R,
             '<Relationship Id="rId6" Type="%stableStyles" Target="tableStyles.xml"/>' % R]
    wr("ppt/_rels/presentation.xml.rels",
       '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships '
       'xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' + "".join(rels) + "</Relationships>")
    ct = rd("[Content_Types].xml")
    for pat in (r"/ppt/slides/slide\d+\.xml", r"/ppt/notesSlides/notesSlide\d+\.xml",
                r"/ppt/tags/tag1\.xml", r"/ppt/changesInfos/changesInfo1\.xml", r"/ppt/revisionInfo\.xml"):
        ct = re.sub(r'<Override PartName="' + pat + r'"[^>]*?/>', "", ct)
    ct = re.sub(r'<Default Extension="svg"[^>]*?/>', "", ct)
    ct = ct.replace("</Types>",
        "".join('<Override PartName="/ppt/slides/slide%d.xml" ContentType="application/vnd.'
                'openxmlformats-officedocument.presentationml.slide+xml"/>' % i for i in range(1, N + 1)) +
        "".join('<Override PartName="/ppt/notesSlides/notesSlide%d.xml" ContentType="application/vnd.'
                'openxmlformats-officedocument.presentationml.notesSlide+xml"/>' % i for i in range(1, N + 1)) +
        "</Types>")
    present = set()
    for root, _, fs in os.walk(work):
        for f in fs: present.add("/" + os.path.relpath(os.path.join(root, f), work).replace("\\", "/"))
    ct = re.sub(r'<Override PartName="([^"]+)"[^>]*?/>',
                lambda mm: mm.group(0) if mm.group(1) in present else "", ct)
    wr("[Content_Types].xml", ct)
    title = "Papan Cerita untuk Semakan Bariah v0.3 — K5 PL06 T03 B02"
    wr("docProps/core.xml",
       '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
       'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
       'xmlns:dcmitype="http://purl.org/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
       f'<dc:title>{X(title)}</dc:title>'
       f'<dc:subject>{X(" · ".join(TOKENS))}</dc:subject>'
       '<dc:creator>CAIR storyboard generator v0.3</dc:creator>'
       f'<cp:keywords>{X("; ".join(TOKENS))}</cp:keywords>'
       '<dc:description>Review build. 26 physical learner screens, 46 runtime states, resolved as '
       'review pages so states can be inspected. 26 source rows, one popup each, every popup carries VO. '
       'No photograph, audio, video, animation or multimedia asset is embedded. Module DOCX SHA-256 '
       'unresolved under CAIR integrity exception B02-CAIR-INT-001 for this review build only.</dc:description>'
       '<cp:lastModifiedBy>CAIR storyboard generator v0.3</cp:lastModifiedBy><cp:revision>1</cp:revision>'
       '<dcterms:created xsi:type="dcterms:W3CDTF">2026-07-31T00:00:00Z</dcterms:created>'
       '<dcterms:modified xsi:type="dcterms:W3CDTF">2026-07-31T00:00:00Z</dcterms:modified>'
       '<cp:category>Storyboard — Review Build v0.3</cp:category></cp:coreProperties>')
    app = rd("docProps/app.xml")
    app = re.sub(r"<TitlesOfParts>.*?</TitlesOfParts>",
                 '<TitlesOfParts><vt:vector size="%d" baseType="lpstr"><vt:lpstr>Theme</vt:lpstr>' % (N + 1) +
                 "".join(f"<vt:lpstr>{X(p['id'])}</vt:lpstr>" for p in pages) +
                 "</vt:vector></TitlesOfParts>", app, flags=re.S)
    app = re.sub(r"<Slides>\d+</Slides>", f"<Slides>{N}</Slides>", app)
    app = re.sub(r"<Notes>\d+</Notes>", f"<Notes>{N}</Notes>", app)
    app = re.sub(r"<HeadingPairs>.*?</HeadingPairs>",
                 '<HeadingPairs><vt:vector size="4" baseType="variant">'
                 '<vt:variant><vt:lpstr>Theme</vt:lpstr></vt:variant><vt:variant><vt:i4>1</vt:i4></vt:variant>'
                 '<vt:variant><vt:lpstr>Slide Titles</vt:lpstr></vt:variant>'
                 f'<vt:variant><vt:i4>{N}</vt:i4></vt:variant></vt:vector></HeadingPairs>', app, flags=re.S)
    wr("docProps/app.xml", app)
    out = os.path.join(outdir, outname or OUTNAME)
    if os.path.exists(out): os.remove(out)
    allf = []
    for root, _, fs in os.walk(work):
        for f in fs: allf.append(os.path.relpath(os.path.join(root, f), work).replace("\\", "/"))
    z = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
    order = ["[Content_Types].xml", "_rels/.rels", "ppt/presentation.xml"]
    for p_ in order + [f for f in sorted(allf) if f not in order]:
        if p_ in allf: z.write(os.path.join(work, p_), p_)
    z.close()
    shutil.rmtree(work)
    return out, manifest


if __name__ == "__main__":
    import argparse, json as _j
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--only", default=None, help="comma-separated component ids (proof build)")
    ap.add_argument("--outname", default=None)
    a = ap.parse_args()
    only = a.only.split(",") if a.only else None
    out, man = generate(a.outdir, only=only, outname=a.outname)
    print(f"WROTE {out}  ({os.path.getsize(out):,} bytes, {len(man)} pages)")
    _j.dump(man, open(os.path.join(a.outdir, "page_manifest.json"), "w"), indent=1)
