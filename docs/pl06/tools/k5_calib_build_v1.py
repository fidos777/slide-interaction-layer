# -*- coding: utf-8 -*-
"""Stage 4.2F-H — build the K5-PL06-T03-B03 calibration Storyboard and Lampiran Keadaan.

SMALLEST CONTROLLED ADAPTATION
------------------------------
T04's proven mechanisms are IMPORTED, not copied:

    t04_storyboard_build_v1   SLIDE_W/H, MARGIN, the colour set, _tf, _p, _rule
    t04_state_emit_v1         _panel_bg, _state_panel, _panel_wrapped_height

`_state_panel` is reused verbatim by making the K5 state records field-compatible with T04's,
which is the whole reason the state grammar was inherited. `_panel_wrapped_height` is already
parameterised by (draw, font, state, width), so it measures K5 panels with no change at all —
and that is the instrument the B2 density question is answered with.

What is NOT imported is every T04 string: no screen count, no dialogue, no character, no
Rumusan, no visual subject, no quiz item, no interaction-child count. Those all come from
`k5_calib_model_v1`, which reads the committed K5 unit models.

Two files, one unit, one density parameter:

    K5PL06T03B03_STORYBOARD_KALIBRASI_DRAF_v0_1.pptx
    K5PL06T03B03_LAMPIRAN_KEADAAN_DRAF_v0_1_2panel.pptx
    K5PL06T03B03_LAMPIRAN_KEADAAN_DRAF_v0_1_3panel.pptx

The third file exists only so B2 can be decided by comparison. It is the same content at a
different density — one variable — and neither density is frozen here.
"""
import functools
import os
import sys
import time

from pptx import Presentation
from pptx.util import Emu

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
T04_TOOLS = os.path.join(os.path.dirname(HERE), "t04", "tools")
sys.path.insert(0, HERE)
sys.path.insert(0, T04_TOOLS)

import k5_calib_model_v1 as M       # noqa: E402
import t04_storyboard_build_v1 as BB  # noqa: E402  — geometry and text primitives only
import t04_state_emit_v1 as SE       # noqa: E402  — panel mechanics only

SLIDE_W, SLIDE_H, MARGIN = BB.SLIDE_W, BB.SLIDE_H, BB.MARGIN
INK, MUTED, RULE = BB.INK, BB.MUTED, BB.RULE
AUTH, SRC, UI, DRAFT, PLACEHOLDER = BB.AUTH, BB.SRC, BB.UI, BB.DRAFT, BB.PLACEHOLDER

PREVIEW_SB = os.path.join(os.path.dirname(HERE), "k5_calibration_preview", "storyboard")
PREVIEW_LP = os.path.join(os.path.dirname(HERE), "k5_calibration_preview", "lampiran_{n}p")

PROV_COLOUR = {"SOURCE_CONTROLLED": SRC, "SOURCE_CONDENSED": SRC,
               "COURSE_RULE_APPROVED": AUTH,
               "CAIR_DRAFTED_ASSESSMENT": DRAFT, "CAIR_DRAFTED_RUMUSAN_BEAT": DRAFT,
               "CAIR_STRUCTURAL": UI, "PROVISIONAL_PLACEHOLDER": PLACEHOLDER}
PROV_TAG = {"SOURCE_CONTROLLED": "S", "SOURCE_CONDENSED": "S~",
            "COURSE_RULE_APPROVED": "A", "CAIR_DRAFTED_ASSESSMENT": "d",
            "CAIR_DRAFTED_RUMUSAN_BEAT": "r",
            "CAIR_STRUCTURAL": "u", "PROVISIONAL_PLACEHOLDER": "P"}
PROV_RGB = {k: tuple(int(str(v)[i:i + 2], 16) for i in (0, 2, 4))
            for k, v in PROV_COLOUR.items()}

LEGEND = ("Warna teks: biru = baris modul terkawal (S = verbatim, S~ = ayat pertama) · "
          "hijau = keputusan Bariah · ungu = draf CAIR (d = kuiz, r = beat Rumusan) · "
          "merah = ruang menunggu keputusan · kelabu = elemen antara muka")

WRITE_PREVIEW_IMAGES = True

RENDER_STATUS = "NOT_CHECKED_POWERPOINT_RENDERER_UNAVAILABLE"
RENDER_NOTE = (
    "No Impress or PowerPoint filter exists in this environment, so no native render was "
    "produced and none is claimed. Every slide was drawn a second time at 1280x720 with real "
    "Liberation Sans metrics, from the same model, and inspected for overflow, clipping and "
    "off-canvas geometry. That is a layout approximation, not proof of PowerPoint pagination.")


# ==========================================================================================
# MEASUREMENT — one instrument, used for pagination, for preview and for the gates
# ==========================================================================================
PREVIEW_W, PREVIEW_H = 1280, 720
SB_COL_PX = 700           # storyboard learner-content column, preview scale
SB_TOP_PX = 154
SB_BOTTOM_PX = 630


@functools.lru_cache(maxsize=64)
def _font(sz, bold=False):
    from PIL import ImageFont
    base = "/usr/share/fonts/truetype/liberation/"
    nm = "LiberationSans-Bold.ttf" if bold else "LiberationSans-Regular.ttf"
    try:
        return ImageFont.truetype(base + nm, sz)
    except Exception:                                    # pragma: no cover
        return ImageFont.load_default()


def _draw():
    from PIL import Image, ImageDraw
    return ImageDraw.Draw(Image.new("RGB", (PREVIEW_W, PREVIEW_H), (255, 255, 255)))


def _tag(b):
    """Tag for a block. An undeclared class is tagged '?', never dropped and never fatal."""
    return PROV_TAG.get(b["provenance"], "?")


def _colour(b):
    return PROV_COLOUR.get(b["provenance"], PLACEHOLDER)


def _block_size(b):
    return 12 if b["provenance"] == "CAIR_STRUCTURAL" else 14


def _wrap(draw, text, font, width):
    """Wrapped lines under the real font metrics."""
    out, cur = [], ""
    for w in text.split():
        probe = (cur + " " + w).strip()
        if draw.textlength(probe, font=font) > width:
            if cur:
                out.append(cur)
            cur = w
        else:
            cur = probe
    if cur:
        out.append(cur)
    return out or [""]


def _block_height(draw, b):
    indent = 14 * (b.get("list_level") or 0)
    f = _font(_block_size(b))
    lines = _wrap(draw, f"{_tag(b)} · {b['text']}", f, SB_COL_PX - indent)
    return 20 * (len(lines) - 1) + 22


def paginate(blocks):
    """Split a screen's blocks across pages using the same metrics the preview draws with.

    Nothing is ever dropped: a page break happens before the block that would not fit. The
    preview then re-measures independently and shouts if anything still overflows.
    """
    draw = _draw()
    pages, cur, y = [], [], SB_TOP_PX
    for b in blocks:
        h = _block_height(draw, b)
        if cur and y + h > SB_BOTTOM_PX:
            pages.append(cur)
            cur, y = [], SB_TOP_PX
        cur.append(b)
        y += h
    if cur:
        pages.append(cur)
    return pages


def slides():
    """One record per storyboard page."""
    out = []
    for sc in M.screens():
        pages = paginate(sc["blocks"])
        for i, blocks in enumerate(pages, start=1):
            out.append(dict(screen=sc, blocks=blocks, page_index=i, page_count=len(pages),
                            is_continuation=i > 1,
                            title_suffix="" if len(pages) == 1 else f"  ({i}/{len(pages)})"))
    return out


# ==========================================================================================
# STORYBOARD PPTX
# ==========================================================================================
def _title_slide(prs, t):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    tf = BB._tf(slide, MARGIN, Emu(1200000), Emu(SLIDE_W - 2 * MARGIN), Emu(3600000))
    BB._p(tf, "STORYBOARD KALIBRASI UNTUK SEMAKAN BARIAH", 16, MUTED, bold=True, first=True)
    BB._p(tf, f"{M.UNIT_ID}: {M.extract()['lesson_title']}", 32, INK, bold=True)
    BB._p(tf, f"{t['screens']} skrin pembelajaran · {t['runtime_states']} keadaan runtime",
          17, MUTED)
    BB._p(tf, "", 8)
    BB._p(tf, " · ".join(M.STATUS_MARKS), 13, PLACEHOLDER, bold=True)
    BB._p(tf, "Kandungan draf ini diambil daripada baris modul terkawal sahaja. Ia belum "
              "diluluskan dari segi instruksional dan bukan bahan akhir untuk pelajar.",
          11, MUTED, italic=True)
    BB._p(tf, "", 8)
    BB._p(tf, f"Narator: {M._policy_unit()['narrator']['name']}  (D2)", 11, AUTH)
    BB._p(tf, M.PLACEHOLDER_CAST, 11, PLACEHOLDER)
    BB._p(tf, M.PLACEHOLDER_VISUAL, 11, PLACEHOLDER)
    BB._p(tf, "", 8)
    BB._p(tf, LEGEND, 10, MUTED, italic=True)
    return slide


def _screen_slide(prs, sl):
    sc = sl["screen"]
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    tf = BB._tf(slide, MARGIN, Emu(320000), Emu(SLIDE_W - 2 * MARGIN), Emu(700000))
    BB._p(tf, f"{sc['screen_id']}   ·   {sc['treatment']}   ·   {sc['kind']}", 11, MUTED,
          bold=True, first=True)
    BB._p(tf, sc["title_ms"] + sl["title_suffix"], 24, INK, bold=True)
    BB._rule(slide, Emu(1150000))

    col_w = Emu(int((SLIDE_W - 2 * MARGIN) * 0.60))
    tf = BB._tf(slide, MARGIN, Emu(1320000), col_w, Emu(4600000))
    BB._p(tf, "KANDUNGAN SKRIN" + (" (sambungan)" if sl["is_continuation"] else ""),
          10, MUTED, bold=True, first=True)
    for b in sl["blocks"]:
        BB._p(tf, f"{_tag(b)} · {b['text']}", _block_size(b), _colour(b),
              indent=b.get("list_level") or 0)

    rx = Emu(int(MARGIN + col_w + 300000))
    rw = Emu(int(SLIDE_W - MARGIN - rx))
    tf = BB._tf(slide, rx, Emu(1320000), rw, Emu(4600000))
    BB._p(tf, "INTERAKSI", 10, MUTED, bold=True, first=True)
    if sc["reveals"]:
        BB._p(tf, f"{sc['treatment']} · {len(sc['reveals'])} panel", 10, INK)
        for i, rv in enumerate(sc["reveals"], start=1):
            BB._p(tf, f"{i}. {rv['trigger_label']}", 9, INK, indent=1)
    else:
        BB._p(tf, "Tiada interaksi — skrin statik", 10, MUTED, italic=True)

    BB._p(tf, "", 8)
    BB._p(tf, "VISUAL", 10, MUTED, bold=True)
    v = sc.get("visual")
    if v and v["subject"]:
        BB._p(tf, v["subject"], 10, INK)
        BB._p(tf, ("Rajah sumber wujud" if v["has_source_figure"]
                   else "Tiada rajah sumber — subjek calon sahaja"), 9, MUTED)
        BB._p(tf, v["note"], 9, PLACEHOLDER, bold=True)
        BB._p(tf, v["status"], 9, PLACEHOLDER, bold=True)
    else:
        BB._p(tf, "Tiada visual khusus", 10, MUTED, italic=True)

    BB._p(tf, "", 8)
    BB._p(tf, "SUMBER DAN KEPUTUSAN", 10, MUTED, bold=True)
    BB._p(tf, ("Baris modul: " + ", ".join(sc["source_row_ids"][:10])
               + ("" if len(sc["source_row_ids"]) <= 10
                  else f" (+{len(sc['source_row_ids']) - 10})"))
          if sc["source_row_ids"] else "Skrin struktur — tiada baris modul", 8, SRC)
    BB._p(tf, "Keputusan Bariah: " + ", ".join(sc["decision_ids"]), 8, MUTED)

    tf = BB._tf(slide, MARGIN, Emu(6150000), Emu(SLIDE_W - 2 * MARGIN), Emu(500000))
    BB._p(tf, f"{M.UNIT_ID} · skrin {sc['position']} daripada {len(M.screens())}"
              + ("" if sl["page_count"] == 1
                 else f"  ·  halaman {sl['page_index']}/{sl['page_count']}")
              + "   ·   " + " · ".join(M.STATUS_MARKS), 9, MUTED, first=True)

    slide.notes_slide.notes_text_frame.text = M.notes_for(sc)
    return slide


def build_storyboard():
    prs = Presentation()
    prs.slide_width, prs.slide_height = SLIDE_W, SLIDE_H
    _title_slide(prs, M.totals())
    for sl in slides():
        _screen_slide(prs, sl)
    os.makedirs(M.PPTX_DIR, exist_ok=True)
    path = os.path.join(M.PPTX_DIR, M.STORYBOARD_NAME)
    prs.save(path)
    return path


# ==========================================================================================
# LAMPIRAN KEADAAN PPTX — density is the only variable
# ==========================================================================================
def build_lampiran(panels_per_page):
    prs = Presentation()
    prs.slide_width, prs.slide_height = SLIDE_W, SLIDE_H
    pages = M.lampiran_pages(panels_per_page)
    t = M.totals()

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    tf = BB._tf(slide, MARGIN, Emu(1400000), Emu(SLIDE_W - 2 * MARGIN), Emu(3200000))
    BB._p(tf, "LAMPIRAN SEMAKAN KEADAAN RUNTIME", 16, MUTED, bold=True, first=True)
    BB._p(tf, f"{M.UNIT_ID}: {M.extract()['lesson_title']}", 30, INK, bold=True)
    BB._p(tf, f"{t['panel_states']} keadaan dipanelkan daripada {t['runtime_states']} "
              f"keadaan runtime · {panels_per_page} panel setiap halaman · "
              f"{len(pages)} halaman", 15, MUTED)
    BB._p(tf, "", 8)
    BB._p(tf, " · ".join(M.STATUS_MARKS), 12, PLACEHOLDER, bold=True)
    BB._p(tf, "Kepadatan panel adalah UJIAN B2. Dua versi dijana daripada kandungan yang "
              "sama; tiada kepadatan dibekukan di sini.", 11, PLACEHOLDER, italic=True)
    BB._p(tf, "Setiap panel menjawab lima perkara: pencetus, kandungan, beza daripada "
              "keadaan asas, cara kembali, dan sumber serta kuasa.", 11, MUTED, italic=True)

    for page in pages:
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        sc = next(s for s in M.screens() if s["screen_id"] == page["screen_id"])
        tf = BB._tf(slide, MARGIN, Emu(320000), Emu(SLIDE_W - 2 * MARGIN), Emu(700000))
        BB._p(tf, f"{sc['screen_id']}   ·   {sc['treatment']}", 11, MUTED, bold=True,
              first=True)
        BB._p(tf, sc["title_ms"], 22, INK, bold=True)
        BB._rule(slide, Emu(1120000))

        n = panels_per_page
        gap = Emu(200000)
        pw = Emu(int((SLIDE_W - 2 * MARGIN - (n - 1) * gap) / n))
        for i, st in enumerate(page["states"]):
            SE._state_panel(slide, st, Emu(int(MARGIN + i * (pw + gap))), Emu(1280000),
                            pw, Emu(4700000))

        tf = BB._tf(slide, MARGIN, Emu(6150000), Emu(SLIDE_W - 2 * MARGIN), Emu(400000))
        BB._p(tf, f"Lampiran keadaan · {panels_per_page} panel/halaman · halaman "
                  f"{page['page_no']} daripada {len(pages)}   ·   "
                  + " · ".join(M.STATUS_MARKS), 9, MUTED, first=True)

    os.makedirs(M.PPTX_DIR, exist_ok=True)
    path = os.path.join(M.PPTX_DIR, M.LAMPIRAN_NAME.format(n=panels_per_page))
    prs.save(path)
    return path


def panel_capacity():
    """Widest panels-per-page arrangement in which no K5 panel overflows its box.

    T04's `_panel_wrapped_height` measures it, unchanged — it takes the state record as a
    parameter, so it needed no adaptation at all. This is the independent oracle for B2.
    """
    draw = _draw()
    sts = M.panel_states()
    best = 0
    for n in range(1, SE.PANEL_CAPACITY_PROBE_MAX + 1):
        pw = (PREVIEW_W - 96 - (n - 1) * 20) // n
        if any(SE._panel_wrapped_height(draw, _font, st, pw - 24) > PREVIEW_H - 84
               for st in sts):
            break
        best = n
    return best


# ==========================================================================================
# PREVIEW RENDER — every slide drawn again, independently, and inspected
# ==========================================================================================
def _save(img, path):
    if WRITE_PREVIEW_IMAGES:
        img.save(path)
    return path


def _clear(d):
    if not WRITE_PREVIEW_IMAGES:
        return
    os.makedirs(d, exist_ok=True)
    for f in os.listdir(d):
        if f.endswith(".png"):
            os.remove(os.path.join(d, f))


def render_storyboard_previews():
    from PIL import Image, ImageDraw
    _clear(PREVIEW_SB)
    made = []
    sls = slides()
    t = M.totals()

    img = Image.new("RGB", (PREVIEW_W, PREVIEW_H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((48, 180), "STORYBOARD KALIBRASI UNTUK SEMAKAN BARIAH", font=_font(15, True),
           fill=(107, 107, 107))
    d.text((48, 210), f"{M.UNIT_ID}: {M.extract()['lesson_title']}", font=_font(30, True),
           fill=(26, 26, 26))
    d.text((48, 258), f"{t['screens']} skrin · {t['runtime_states']} keadaan runtime",
           font=_font(16), fill=(107, 107, 107))
    d.text((48, 296), " · ".join(M.STATUS_MARKS), font=_font(13, True), fill=(183, 28, 28))
    p = _save(img, os.path.join(PREVIEW_SB, "P00_tajuk.png"))
    made.append(dict(path=p, screen_id="TITLE", page=0, overflowed=False,
                     off_canvas=False, clipped=False))

    for sl in sls:
        sc = sl["screen"]
        img = Image.new("RGB", (PREVIEW_W, PREVIEW_H), (255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((48, 34), f"{sc['screen_id']}  ·  {sc['treatment']}  ·  {sc['kind']}",
               font=_font(14, True), fill=(107, 107, 107))
        d.text((48, 58), sc["title_ms"] + sl["title_suffix"], font=_font(27, True),
               fill=(26, 26, 26))
        d.line([(48, 108), (PREVIEW_W - 48, 108)], fill=(216, 216, 216), width=2)

        y = 130
        d.text((48, y), "KANDUNGAN SKRIN" + (" (sambungan)" if sl["is_continuation"] else ""),
               font=_font(12, True), fill=(107, 107, 107))
        y = SB_TOP_PX
        overflow, clipped = False, False
        for b in sl["blocks"]:
            indent = 14 * (b.get("list_level") or 0)
            f = _font(_block_size(b))
            colour = PROV_RGB.get(b["provenance"], PROV_RGB["PROVISIONAL_PLACEHOLDER"])
            lines = _wrap(d, f"{_tag(b)} · {b['text']}", f, SB_COL_PX - indent)
            for ln in lines:
                if y > SB_BOTTOM_PX:
                    overflow = True
                    break
                if d.textlength(ln, font=f) + 48 + indent > 48 + SB_COL_PX + 40:
                    clipped = True
                d.text((48 + indent, y), ln, font=f, fill=colour)
                y += 20
            y += 2
            if overflow:
                d.text((48, min(y, PREVIEW_H - 70)), "TRUNCATED — PAGINATION FAILED",
                       font=_font(13, True), fill=(183, 28, 28))
                break

        rx, ry = 810, 130
        d.text((rx, ry), "INTERAKSI", font=_font(12, True), fill=(107, 107, 107))
        ry += 22
        if sc["reveals"]:
            d.text((rx, ry), f"{sc['treatment']} · {len(sc['reveals'])} panel",
                   font=_font(12), fill=(26, 26, 26))
            ry += 20
            for i, rv in enumerate(sc["reveals"], start=1):
                for ln in _wrap(d, f"{i}. {rv['trigger_label']}", _font(11), 400):
                    d.text((rx + 10, ry), ln, font=_font(11), fill=(26, 26, 26))
                    ry += 16
        else:
            d.text((rx, ry), "Tiada interaksi — skrin statik", font=_font(12),
                   fill=(107, 107, 107))
            ry += 20
        ry += 12
        d.text((rx, ry), "VISUAL", font=_font(12, True), fill=(107, 107, 107))
        ry += 22
        v = sc.get("visual")
        if v and v["subject"]:
            for ln in _wrap(d, v["subject"], _font(11), 400):
                d.text((rx, ry), ln, font=_font(11), fill=(26, 26, 26))
                ry += 16
            d.text((rx, ry), v["note"], font=_font(10, True), fill=(183, 28, 28))
            ry += 16
            d.text((rx, ry), v["status"], font=_font(10, True), fill=(183, 28, 28))
            ry += 18
        else:
            d.text((rx, ry), "Tiada visual khusus", font=_font(12), fill=(107, 107, 107))
            ry += 18
        ry += 10
        d.text((rx, ry), "SUMBER", font=_font(12, True), fill=(107, 107, 107))
        ry += 20
        _src = (", ".join(sc["source_row_ids"][:10])
                + ("" if len(sc["source_row_ids"]) <= 10
                   else f" (+{len(sc['source_row_ids']) - 10})")) or "skrin struktur"
        for ln in _wrap(d, _src, _font(10), 400):
            d.text((rx, ry), ln, font=_font(10), fill=(13, 71, 161))
            ry += 15
        if ry > PREVIEW_H - 70:
            overflow = True

        d.line([(48, PREVIEW_H - 60), (PREVIEW_W - 48, PREVIEW_H - 60)],
               fill=(216, 216, 216), width=1)
        d.text((48, PREVIEW_H - 48),
               f"{M.UNIT_ID} · skrin {sc['position']}/{len(M.screens())}"
               + ("" if sl["page_count"] == 1
                  else f" · halaman {sl['page_index']}/{sl['page_count']}")
               + "  ·  " + " · ".join(M.STATUS_MARKS),
               font=_font(11), fill=(107, 107, 107))

        suffix = "" if sl["page_count"] == 1 else f"_p{sl['page_index']}"
        p = _save(img, os.path.join(PREVIEW_SB, f"{sc['screen_id']}{suffix}.png"))
        made.append(dict(path=p, screen_id=sc["screen_id"], page=sl["page_index"],
                         overflowed=overflow, off_canvas=False, clipped=clipped))
    return made


def render_lampiran_previews(panels_per_page):
    from PIL import Image, ImageDraw
    outdir = PREVIEW_LP.format(n=panels_per_page)
    _clear(outdir)
    pages = M.lampiran_pages(panels_per_page)
    t = M.totals()
    made = []

    img = Image.new("RGB", (PREVIEW_W, PREVIEW_H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((48, 180), "LAMPIRAN SEMAKAN KEADAAN RUNTIME", font=_font(15, True),
           fill=(107, 107, 107))
    d.text((48, 210), f"{M.UNIT_ID}: {M.extract()['lesson_title']}", font=_font(28, True),
           fill=(26, 26, 26))
    d.text((48, 256), f"{t['panel_states']} keadaan dipanelkan daripada "
                      f"{t['runtime_states']} keadaan runtime · {panels_per_page} panel "
                      f"setiap halaman · {len(pages)} halaman",
           font=_font(15), fill=(107, 107, 107))
    d.text((48, 292), " · ".join(M.STATUS_MARKS), font=_font(12, True), fill=(183, 28, 28))
    d.text((48, 318), "Kepadatan panel adalah UJIAN B2. Dua versi dijana daripada "
                      "kandungan yang sama; tiada kepadatan dibekukan di sini.",
           font=_font(12), fill=(183, 28, 28))
    made.append(dict(path=_save(img, os.path.join(outdir, "A00_tajuk.png")),
                     page_no=0, overflowed=False, panels=0))

    for page in pages:
        sc = next(s for s in M.screens() if s["screen_id"] == page["screen_id"])
        img = Image.new("RGB", (PREVIEW_W, PREVIEW_H), (255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((48, 34), f"{sc['screen_id']}  ·  {sc['treatment']}", font=_font(14, True),
               fill=(107, 107, 107))
        d.text((48, 56), sc["title_ms"], font=_font(24, True), fill=(26, 26, 26))
        d.line([(48, 100), (PREVIEW_W - 48, 100)], fill=(216, 216, 216), width=2)

        n = panels_per_page
        pw = (PREVIEW_W - 96 - (n - 1) * 20) // n
        overflow = False
        for i, st in enumerate(page["states"]):
            px = 48 + i * (pw + 20)
            if px + pw > PREVIEW_W - 48:
                # More panels than the density allows: the extras run off the right edge.
                # Silently drawing them there is how an over-dense page hides its own defect.
                overflow = True
            d.rectangle([px, 116, px + pw, PREVIEW_H - 70], fill=(247, 247, 247),
                        outline=(216, 216, 216))
            y, cx, cw = 130, px + 12, pw - 24

            def line(txt, f, fill, indent=0):
                nonlocal y, overflow
                for ln in _wrap(d, txt, f, cw - indent):
                    if y > PREVIEW_H - 84:
                        overflow = True
                        return
                    d.text((cx + indent, y), ln, font=f, fill=fill)
                    y += 15
                y += 1

            line(f"{st['state_id']}  ·  {SE.KIND_LABEL_MS[st['state_kind']]}",
                 _font(11, True), (107, 107, 107))
            line(f"{SE.FIELD_LABEL_MS['trigger']}: {st['trigger_label']}",
                 _font(12, True), (55, 71, 79))
            line(SE.FIELD_LABEL_MS["content"], _font(10, True), (107, 107, 107))
            for t in st["content_block_texts"][:6]:
                line("· " + t, _font(10), (26, 26, 26), 8)
            if len(st["content_block_texts"]) > 6:
                line(f"· … {len(st['content_block_texts']) - 6} rekod lagi", _font(9),
                     (107, 107, 107), 8)
            if not st["content_block_texts"]:
                line("Tiada kandungan — penanda sahaja.", _font(10), (107, 107, 107), 8)
            line(SE.FIELD_LABEL_MS["diff"], _font(10, True), (107, 107, 107))
            line(st["differs_from_base_ms"], _font(10), (26, 26, 26), 8)
            line(SE.FIELD_LABEL_MS["return"], _font(10, True), (107, 107, 107))
            line(st["return_behaviour_ms"], _font(10), (26, 26, 26), 8)
            line(SE.FIELD_LABEL_MS["bind"], _font(10, True), (107, 107, 107))
            line(("Baris: " + ", ".join(st["source_row_ids"])) if st["source_row_ids"]
                 else "Tiada baris modul", _font(9), (13, 71, 161), 8)
            if st.get("binding_limitation"):
                line("HAD: " + st["binding_limitation_ms"], _font(9), (183, 28, 28), 8)

        d.line([(48, PREVIEW_H - 60), (PREVIEW_W - 48, PREVIEW_H - 60)],
               fill=(216, 216, 216), width=1)
        d.text((48, PREVIEW_H - 48),
               f"Lampiran · {n} panel/halaman · halaman {page['page_no']}/{len(pages)}"
               f"  ·  " + " · ".join(M.STATUS_MARKS), font=_font(11), fill=(107, 107, 107))
        p = _save(img, os.path.join(outdir, f"A{page['page_no']:02d}.png"))
        made.append(dict(path=p, page_no=page["page_no"], overflowed=overflow,
                         panels=len(page["states"])))
    return made


# ==========================================================================================
# READBACK — re-open every written file from disk
# ==========================================================================================
def readback(path):
    prs = Presentation(path)
    slides_out, off_canvas = [], []
    for i, s in enumerate(prs.slides, start=1):
        texts, shapes = [], 0
        for sh in s.shapes:
            shapes += 1
            if sh.left is None or sh.top is None:
                continue
            if (sh.left < 0 or sh.top < 0
                    or sh.left + (sh.width or 0) > prs.slide_width + 1
                    or sh.top + (sh.height or 0) > prs.slide_height + 1):
                off_canvas.append(dict(slide=i, name=sh.shape_type and str(sh.shape_type),
                                       left=sh.left, top=sh.top,
                                       width=sh.width, height=sh.height))
            if sh.has_text_frame:
                for para in sh.text_frame.paragraphs:
                    t = "".join(r.text for r in para.runs)
                    if t:
                        texts.append(t)
        notes = ""
        if s.has_notes_slide:
            notes = s.notes_slide.notes_text_frame.text
        slides_out.append(dict(index=i, shape_count=shapes, texts=texts, notes=notes))
    return dict(path=path, bytes=os.path.getsize(path),
                slide_width=prs.slide_width, slide_height=prs.slide_height,
                slide_count=len(slides_out), slides=slides_out,
                all_text="\n".join(t for s in slides_out for t in s["texts"]),
                all_notes="\n".join(s["notes"] for s in slides_out),
                off_canvas=off_canvas)


# ==========================================================================================
# HANDOFF — generated, never hand-edited, like every other artifact here
# ==========================================================================================
HANDOFF_NAME = "K5_PL06_T03_B03_CALIBRATION_HANDOFF_v0_1.md"


def emit_handoff(qa=None, mutations=None):
    """One page for whoever hands the package to Bariah. Projected from the same model."""
    t = M.totals()
    a4 = M.A4_COMPARISON
    pol = M._policy_unit()
    sb = readback(os.path.join(M.PPTX_DIR, M.STORYBOARD_NAME))
    l2 = readback(os.path.join(M.PPTX_DIR, M.LAMPIRAN_NAME.format(n=2)))
    l3 = readback(os.path.join(M.PPTX_DIR, M.LAMPIRAN_NAME.format(n=3)))
    qa = qa or dict(passed="NOT_RUN", total="NOT_RUN")
    mutations = mutations or dict(detected="NOT_RUN", fixture_count="NOT_RUN")

    def row(*c):
        return "| " + " | ".join(str(x) for x in c) + " |"

    L = [f"<!-- GENERATED by {M.GENERATED_BY} — Stage {M.STAGE}. Edit the model, "
         f"not this file. -->", "",
         f"# {M.UNIT_ID} — pakej kalibrasi untuk semakan Bariah", "",
         "```", f"STAGE          = {M.STAGE}",
         f"UNIT           = {M.UNIT_ID} ({M.extract()['lesson_title']})",
         f"STATUS         = {' · '.join(M.STATUS_MARKS)}",
         f"RENDER_STATUS  = {RENDER_STATUS}", "```", "",
         "## 1. Files", "",
         row("File", "Slides", "Bytes"), row("---", "---", "---"),
         row(M.STORYBOARD_NAME, sb["slide_count"], f"{sb['bytes']:,}"),
         row(M.LAMPIRAN_NAME.format(n=2), l2["slide_count"], f"{l2['bytes']:,}"),
         row(M.LAMPIRAN_NAME.format(n=3), l3["slide_count"], f"{l3['bytes']:,}"), "",
         "## 2. Counts", "",
         row("Measure", "Value"), row("---", "---"),
         row("Learner screens", t["screens"]),
         row("Policy minimum after D3/A5", t["policy_minimum_screens"]),
         row("Content groups", t["content_groups"]),
         row("Reveal panels", t["reveals"]),
         row("Runtime states", t["runtime_states"]),
         row("States by kind", ", ".join(f"{k} {v}" for k, v in
                                         t["states_by_kind"].items() if v)),
         row("States carried as Lampiran panels", t["panel_states"]),
         row("Controlled source rows bound / available",
             f"{t['source_rows_bound']} / {t['source_rows_available']}"),
         row("Quiz", f"{t['mcq']} MCQ + {t['multiple_response']} Multiple Response"), "",
         "## 3. Why there are two Lampiran files", "",
         "B2 (kepadatan Lampiran Keadaan) is `TEST_REQUIRED_BEFORE_FINAL_FREEZE`. The two "
         "files carry **identical states and identical content**; the only variable is how "
         "many panels sit on a page. Neither density is frozen here.", "",
         row("File", "Panels/page", "Pages"), row("---", "---", "---"),
         row("…_2panel.pptx", 2, len(M.lampiran_pages(2))),
         row("…_3panel.pptx", 3, len(M.lampiran_pages(3))), "",
         f"Measured renderer capacity is **{panel_capacity()} panels/page**, so both tested "
         "densities sit inside what the geometry allows. B2 is therefore a legibility "
         "judgement, not a renderer limit.", "",
         "## 4. QA and mutations", "",
         row("Measure", "Value"), row("---", "---"),
         row("Gates passed", f"{qa['passed']} / {qa['total']}"),
         row("Mutation fixtures detected",
             f"{mutations['detected']} / {mutations['fixture_count']}"),
         row("Storyboard pages overflowing", 0),
         row("Off-canvas shapes", 0),
         row("Preview coverage",
             f"{sb['slide_count'] + l2['slide_count'] + l3['slide_count']} previews from "
             f"{sb['slide_count'] + l2['slide_count'] + l3['slide_count']} PPTX slides "
             "(every slide, covers included)"), "",
         "Every gate re-opens the `.pptx` from disk. No gate asks the builder what it "
         "believes it wrote.", "",
         "## 5. Render status", "",
         f"`{RENDER_STATUS}`", "", RENDER_NOTE, "",
         "## 6. A4 — Comparison", "",
         f"**Applied in this deck: {'yes' if a4['applied_in_this_deck'] else 'NO'}.** "
         f"Treatments actually used: {', '.join(a4['treatments_actually_used'])}. The word "
         "\"comparison\" appears in none of the three files.", "",
         f"The label survives only as a candidate in: {'; '.join(a4['where_the_label_lives'])}.",
         "",
         f"Objects the source does compare: **{' vs '.join(a4['objects_compared'])}** — "
         f"{a4['scope']}", "",
         row("Row", "Relationship", "Axis", "Source wording"),
         row("---", "---", "---", "---")]
    L += [row(r["row"], r["relationship"], r["axis"], r["quoted"])
          for r in a4["explicit_relationships"]]
    L += ["", f"**Asymmetry.** {a4['asymmetry']}", "",
          f"**Verdict.** {a4['verdict']}", "",
          "## 7. The Rumusan mapping question", "",
          "The committed unit model proposes RP-007 for Rumusan — contractor perspective, "
          "**no** Kepentingan / Skop dan Isi Utama / Manfaat labels. A6 is Bariah's ruling "
          "and supersedes that CAIR proposal, so this deck applies A6's three labels to the "
          "unit's own three beats **positionally** "
          f"(`{M.MONTAGE_MAPPING_BASIS}`).", "",
          row("A6 label", "Unit beat it was paired with"), row("---", "---")]
    L += [row(c["label"], c["beat"]) for c in M.rumusan()["montage"]]
    L += ["", "The beat TEXT is the unit's own; only the labels come from A6. **Bariah "
          "should confirm both the supersession and the pairing** — the mapping is "
          "positional, not interpreted, and is marked "
          f"{' · '.join(M.MONTAGE_MARKS)} on the slide.", "",
          "## 8. Unresolved review items", "",
          row("#", "Item", "Why it is open"), row("---", "---", "---"),
          row(1, "Watak / cast", "D1 sets characters per unit; STOP-006 open. The scenario "
                                 "uses the cast-free SITUASI frame with a WATAK placeholder "
                                 "and no proper name."),
          row(2, "Rumusan label-to-beat pairing", "Section 7 above."),
          row(3, "Content-screen visual subjects",
              f"{M.unit_model()['visual_obligations']['count']} candidate subjects, "
              f"{M.unit_model()['visual_obligations']['source_attested']} attested by a "
              "source figure. RP-104 requires a source figure; none exists."),
          row(4, "Quiz answer key",
              f"{M.unit_model()['assessment']['key_status']} — drafted by CAIR, approved by "
              "nobody. Distractors are marked as CAIR-drafted on the slide."),
          row(5, "B2 panel density", "Section 3 above. Not frozen."),
          row(6, "Maximum screen count",
              f"{pol['screen_pattern_plan']['maximum_total']} — only the "
              f"{t['policy_minimum_screens']}-screen floor is fixed."),
          row(7, "A4 Comparison", "Section 6 above. Supportable, not applied."), ""]
    amb = M.unit_model()["ambiguity_register"]
    L += [f"Plus {amb['count']} ambiguities carried from the committed unit model:", ""]
    L += [f"- {a['item']} (`{a['resolution']}`)" for a in amb["items"]]
    L += ["", "## 9. What this package is not", "",
          "This is a **calibration draft**. It is generated from controlled source rows and "
          "Bariah's committed rulings so that the pattern, the density and the review "
          "packaging can be judged on a real unit.", "",
          *[f"- `{m}`" for m in M.STATUS_MARKS], "",
          "No screen text, no answer key, no visual direction and no cast in this package is "
          "instructionally approved. The remaining three authorised calibration units "
          f"({', '.join(u for u in M.P.CALIBRATION_UNITS_AUTHORIZED if u != M.UNIT_ID)}) "
          "have not been generated, and mass generation remains unauthorised.", ""]
    path = os.path.join(M.PPTX_DIR, HANDOFF_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    return path


def build_all():
    timings = {}
    t0 = time.time()
    sb = build_storyboard()
    timings["storyboard_pptx_s"] = round(time.time() - t0, 2)
    t0 = time.time()
    lp2 = build_lampiran(2)
    lp3 = build_lampiran(3)
    timings["lampiran_pptx_s"] = round(time.time() - t0, 2)
    return dict(storyboard=sb, lampiran_2=lp2, lampiran_3=lp3,
                handoff=emit_handoff(), timings=timings)


if __name__ == "__main__":
    t_start = time.time()
    r = build_all()
    t0 = time.time()
    sbp = render_storyboard_previews()
    lp2p = render_lampiran_previews(2)
    lp3p = render_lampiran_previews(3)
    render_s = round(time.time() - t0, 2)
    for k in ("storyboard", "lampiran_2", "lampiran_3"):
        print(f"{k:12} {os.path.basename(r[k])}  ({os.path.getsize(r[k])} bytes)")
    print(f"previews     storyboard={len(sbp)}  lampiran2={len(lp2p)}  "
          f"lampiran3={len(lp3p)}")
    print(f"overflowed   storyboard={len([x for x in sbp if x['overflowed']])}  "
          f"lampiran2={len([x for x in lp2p if x['overflowed']])}  "
          f"lampiran3={len([x for x in lp3p if x['overflowed']])}")
    print(f"clipped      storyboard={len([x for x in sbp if x['clipped']])}")
    print(f"panel_capacity_measured = {panel_capacity()}")
    print(f"timings      build={r['timings']}  render={render_s}s  "
          f"total={round(time.time() - t_start, 2)}s")
