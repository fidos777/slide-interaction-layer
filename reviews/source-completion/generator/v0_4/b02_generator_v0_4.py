# -*- coding: utf-8 -*-
"""K5 PL06 T03 B02 — v0.4 three-family proof generator.

Reuses the v0.3 drawing primitives unchanged (geometry, theme, donor package). What is
new is architecture-driven: family strategy dispatch, the Level-2 example detail screen,
the close-icon control, structured Speaker Notes, and off-canvas panels that quote the
model rather than restating it.

NOTHING structural is decided here. execution_family, parent_screen_id, return_target,
control types, completion_scope, notes policy, character assignment, spoken transcript,
source locators and unresolved status are all read from the frozen model.
"""
import os, re, sys, shutil, zipfile, json

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.dirname(HERE)
sys.path.insert(0, GEN); sys.path.insert(0, HERE)

import b02_generator_v0_3 as V3          # primitives only
import b02_model_adapter_v0_4 as ADAPT
import b02_proof_content_v0_4 as C
import b02_glossary_v0_4 as GL
import b02_visual_directions_v0_4 as VD
import b02_overview_mapping_v0_4_4 as OV
import b02_instructions_v0_4 as INS
import b02_visual_policy_v0_4 as VP

from b02_generator_v0_3 import (
    E, X, STAGE_W, STAGE_H, BAND_X, BAND_W, NAV_CLR, KW, KH, NAV_H,
    GM_TOP, ROW_PITCH, TICK, GOLD, GREY, GREEN, DARK,
    grid4, grid5, item_grid, runs, nv, box, para, txt, bullets, panel,
    card, tick, button, titlebar, title_ph, HDR, FTR,
)

BLUE = "1F4E79"
OUTNAME = "K5PL06T03B02_v0_4_THREE_FAMILY_PROOF.pptx"

# ============================ rich text ============================
def ital_parts(s):
    """Delegates to the ONE controlled glossary shared with the Speaker Notes writer."""
    return GL.parts(s)


def rt(lines):
    """Lines -> para()-compatible rich-text parts."""
    return [ital_parts(l) for l in lines]


# ============================ new controls ============================
def title_ph_rt(t):
    """PowerPoint title placeholder, off the top of the stage, with the approved italic
    treatment applied to its runs. The outline pane shows this text, so the lexicon rule
    applies to it as much as to the canvas."""
    return ('<p:sp><p:nvSpPr><p:cNvPr id="2" name="Title 1"/><p:cNvSpPr><a:spLocks noGrp="1"/>'
            '</p:cNvSpPr><p:nvPr><p:ph type="title"/></p:nvPr></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="0" y="{E(-0.6311)}"/>'
            f'<a:ext cx="{E(13.3333)}" cy="{E(0.5722)}"/></a:xfrm></p:spPr>'
            '<p:txBody><a:bodyPr><a:noAutofit/></a:bodyPr><a:lstStyle/><a:p>'
            + runs(ital_parts(t), sz=2400, b=True) + '</a:p></p:txBody></p:sp>')


def close_icon(i, x, y, size=0.42):
    """CLOSE_ICON. A drawn icon, never a text button labelled Tutup."""
    r = size / 2.0
    circ = (f'<p:sp><p:nvSpPr>{nv(i,"CloseIcon")}<p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E(x)}" y="{E(y)}"/><a:ext cx="{E(size)}" cy="{E(size)}"/></a:xfrm>'
            '<a:prstGeom prst="ellipse"><a:avLst/></a:prstGeom>'
            f'<a:solidFill><a:srgbClr val="{BLUE}"/></a:solidFill>'
            '<a:ln><a:noFill/></a:ln></p:spPr>'
            '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="en-MY"/></a:p></p:txBody></p:sp>')
    # The X is a FILLED polygon, not a stroked path: a line-only custGeom is ambiguous
    # to renderers and would leave the control unverifiable in visual inspection.
    XPTS = [(25, 0), (50, 25), (75, 0), (100, 25), (75, 50), (100, 75),
            (75, 100), (50, 75), (25, 100), (0, 75), (25, 50), (0, 25)]
    pad = size * 0.27
    pts = "".join((f'<a:moveTo><a:pt x="{a}" y="{b}"/></a:moveTo>' if k == 0
                   else f'<a:lnTo><a:pt x="{a}" y="{b}"/></a:lnTo>')
                  for k, (a, b) in enumerate(XPTS))
    cross = (f'<p:sp><p:nvSpPr>{nv(i+1,"CloseGlyph")}<p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
             f'<p:spPr><a:xfrm><a:off x="{E(x+pad)}" y="{E(y+pad)}"/>'
             f'<a:ext cx="{E(size-2*pad)}" cy="{E(size-2*pad)}"/></a:xfrm>'
             '<a:custGeom><a:avLst/><a:gdLst/><a:ahLst/><a:cxnLst/><a:rect l="0" t="0" r="r" b="b"/>'
             f'<a:pathLst><a:path w="100" h="100">{pts}<a:close/></a:path></a:pathLst></a:custGeom>'
             '<a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr>'
             '<p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:endParaRPr lang="en-MY"/></a:p></p:txBody></p:sp>')
    return circ + cross


# ============================ off-canvas production panel ============================
TOKENS_V4 = ["REVIEW_READY", "BARIAH_FEEDBACK_IMPLEMENTED", "PENDING_TARGETED_CONFIRMATION",
             "NOT_FOR_MMD_BUILD", "MULTIMEDIA_NOT_PRODUCED"]


def prodpanel_v4(i, page, rec, st, lines):
    head = ["K5 PL06 T03 B02 — PAPAN CERITA v0.4",
            " · ".join(TOKENS_V4[:2]), " · ".join(TOKENS_V4[2:]),
            "Tiada imej, audio, video atau animasi dibenamkan.", "",
            f"FUNGSI SKRIN: {rec['semantic_screen_name']}",
            f"KELUARGA PELAKSANAAN: {st['execution_family']}",
            f"PERANAN HALAMAN SEMAKAN: {st['review_page_role']}", ""]
    body = ""
    for k, t in enumerate(head + lines):
        b = (k == 0) or t.rstrip().endswith(":") and t == t.lstrip()
        body += f'<a:p>{runs([(t, False)], sz=900, b=b, dark=True)}</a:p>'
    return (f'<p:sp><p:nvSpPr>{nv(i,"ProdPanel")}<p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E(-6.90)}" y="0"/><a:ext cx="{E(6.60)}" cy="{E(7.5)}"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>'
            '<a:solidFill><a:srgbClr val="FFF2CC"/></a:solidFill><a:ln><a:noFill/></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr rtlCol="0" anchor="t"/><a:lstStyle/>{body}</p:txBody></p:sp>')


def model_lines(M, rec, st, extra=None):
    """Production metadata quoted FROM the model. Never restated by hand."""
    L = [f"POLISI NOTA: {st['notes_policy']}  ({st['notes_policy_family']})",
         f"  konteks dituturkan: {'YA' if st['notes_context_spoken'] else 'TIDAK'}",
         "KAWALAN:",
         f"  next  = {st['next_control_type']}  [{st['next_enabled_condition']}]",
         f"  back  = {st['back_control_type']}  [{st['back_enabled_condition']}]",
         f"  close = {st['close_control_type']}",
         f"  return_target = {st['return_target'] or '—'}",
         f"SKOP SELESAI: {st['completion_scope']}",
         f"PERSISTEN: {st['persistence_rule']}",
         f"LEVEL: pilihan interaksi {st['interaction_selection_level']} · "
         f"lapisan skrin {st['screen_path_layer']}",
         f"INDUK: {st['parent_screen_id']}"]
    if st["source_row_uids"]:
        L.append("SUMBER:")
        for u in st["source_row_uids"]:
            r = M.rows[u]
            L.append(f"  {u}")
            L.append(f"    ms {r['ms']} / fizikal {r['phys']}")
    if st["source_asset_ids"]:
        L.append("ASET SUMBER (tidak dibenamkan):")
        L += [f"  {a}" for a in st["source_asset_ids"]]
    if st["interaction_item_ids"]:
        L.append("ITEM INTERAKSI:")
        for iid in st["interaction_item_ids"]:
            it = M.item(iid)
            L.append(f"  {iid}  <-  {it['source_row_uid']}")
    if extra:
        L += extra
    L.append(f"STATUS KEPUTUSAN: {', '.join(st['decision_ids']) or '—'}")
    us = st.get("unresolved_status") or "NONE"
    L.append(f"STATUS BELUM SELESAI: {us}")
    return L


# ============================ Speaker Notes ============================
NB_CONTEXT = "NON_SPOKEN_CONTEXT"
NB_VO = "SPOKEN_CONTENT_VO"
NB_INSTR = "SPOKEN_INTERACTION_INSTRUCTION"
NB_PROD = "PRODUCTION_INSTRUCTION_NOT_SPOKEN"

MARK_CONTEXT = "NON-SPOKEN CONTEXT"
MARK_SPOKEN = "SPOKEN TRANSCRIPT"


def build_notes_blocks(M, rec, st, spoken, instruction=None):
    """Speaker Notes as an ordered list of EXPLICITLY TYPED blocks.

    Every paragraph that reaches the package originates here with a block_type and a
    spoken flag. Downstream TTS/VO export reads spoken=True and never infers speech from
    paragraph order or styling.
    """
    spec = M.notes_spec(st)
    if spec["policy"] == "SILENT_STATE_NOTES":
        return []                                   # genuinely empty; no blocks at all
    blocks = []
    n = [0]

    def blk(bt, spoken_flag, text, marker=False):
        n[0] += 1
        blocks.append(dict(block_type=bt, spoken=spoken_flag, text=text,
                           sequence_order=n[0], is_marker=marker,
                           source_decision_id=(st["decision_ids"][0] if st["decision_ids"] else None),
                           runs=[dict(text=t, italic=i) for t, i in GL.parts(text) if t]))

    if spec["context_spoken"]:
        # S01 only: the entry titles ARE the spoken transcript.
        for e in sorted(spec["spoken_elements"] or [], key=lambda e: e["order"]):
            bt = NB_INSTR if e["element"] == "MULA_INSTRUCTION" else NB_VO
            blk(bt, True, e["text"])
        return blocks

    blk(NB_CONTEXT, False, MARK_CONTEXT, marker=True)
    blk(NB_CONTEXT, False, "", marker=True)
    for hdr in spec["context_headers"]:
        blk(NB_CONTEXT, False, hdr)
    blk(NB_CONTEXT, False, "", marker=True)
    blk(NB_CONTEXT, False, MARK_SPOKEN, marker=True)
    blk(NB_CONTEXT, False, "", marker=True)
    for line in (spoken if isinstance(spoken, list) else [spoken]):
        for part in str(line).split("\n"):
            bt = NB_INSTR if (instruction and part.strip() == instruction.strip()) else NB_VO
            blk(bt, True, part)
    return blocks


def blocks_to_text(blocks):
    return "\n".join(b["text"] for b in blocks).rstrip()


def spoken_export(blocks):
    """What TTS would read. Driven by the spoken flag, never by position."""
    return [b["text"] for b in blocks if b["spoken"] and b["text"].strip()]


# ============================ shared page furniture ============================
def _nav(add, st, kembali_label="Kembali"):
    """Learner-canvas controls only. LMS_SHELL_NEXT is never drawn."""
    if st["back_control_type"] == "KEMBALI_BUTTON":
        enabled = "enabled" in (st["back_enabled_condition"] or "") or \
                  st["screen_role"] in ("STATE_ALL_VIEWED",)
        add(button(95, (STAGE_W - KW) / 2, STAGE_H - NAV_H + NAV_CLR, KW, KH,
                   kembali_label, enabled))
    if st["next_control_type"] == "MULA_BUTTON":
        add(button(96, (STAGE_W - KW) / 2, STAGE_H - NAV_H + NAV_CLR, KW, KH, "MULA", True))
    if st["next_control_type"] == "MULA_KUIZ_BUTTON":
        add(button(96, (STAGE_W - 2.4) / 2, STAGE_H - NAV_H + NAV_CLR, 2.4, KH, "MULA KUIZ", True))
    # LMS_SHELL_NEXT and NO_CONTROL draw nothing on the learner canvas.


def _visual(add, i, y, lines, w=BAND_W, x=BAND_X, sz=1100):
    h = 0.28 * len(lines) + 0.12
    add(txt(i, "VisualDir", x, y, w, h, lines, sz=sz, clr=GREY))
    return y + h


# Calibrated against the package renderer's own Liberation Sans metrics at 110 dpi, with a
# safety margin, so the generator over-estimates line counts rather than under-estimating and
# silently clipping. avg chars/in: 7.5pt 20.6, 9pt bold 15.4. Line heights: 0.118 / 0.145.
OVR_CW_MAX, OVR_GAP = 2.60, 0.20
OVR_H_MAX = 1.34
SUBJ_CPI, SUBJ_LEAD = 12.5, 0.152
DIR_CPI, DIR_LEAD = 18.5, 0.125


def _overview(add, component_id, y0, start=300):
    """Component-main overview: several SMALLER source-bound visual placeholders.

    Cardinality comes from the frozen mapping, never from a constant here. Card width is
    capped so an overview card is always visibly smaller than a popup's focused panel —
    that size relationship is the treatment Bariah described, and a one-card overview
    (BBQ Pit) must not stretch to full width and read as the larger treatment.

    Box heights are derived from the measured line counts, not assumed.
    """
    subs = OV.subjects(component_id)
    n = len(subs)
    cw = min(OVR_CW_MAX, (BAND_W - (n - 1) * OVR_GAP) / n)
    inner = cw - 0.20
    laid = []
    for label, direction in subs:
        sl = V3._wrap_lines(label, max(6, int(inner * SUBJ_CPI)))[:3]
        dl = V3._wrap_lines(direction, max(8, int(inner * DIR_CPI)))
        laid.append((sl, dl))
    subj_h = max(len(sl) for sl, _ in laid) * SUBJ_LEAD + 0.06
    room = OVR_H_MAX - 0.06 - subj_h - 0.04 - 0.08
    keep = max(1, int(room / DIR_LEAD))
    dir_h = min(max(len(dl) for _, dl in laid), keep) * DIR_LEAD + 0.06
    card_h = 0.06 + subj_h + 0.04 + dir_h + 0.08

    add(txt(start, "OverviewHead", BAND_X, y0, BAND_W, 0.22, [OV.HEADING], sz=850,
            b=True, clr=GOLD))
    top = y0 + 0.26
    i = start + 1
    for k, ((sl, dl), (label, direction)) in enumerate(zip(laid, subs)):
        x = BAND_X + k * (cw + OVR_GAP)
        add(box(i, "OverviewCard", x, top, cw, card_h, "", fill="F7F7F7", ln="BFBFBF",
                dash=False, lnw=12700)); i += 1
        add(txt(i, "OverviewSubject", x + 0.10, top + 0.06, inner, subj_h,
                rt(sl), sz=900, b=True)); i += 1
        add(txt(i, "OverviewDir", x + 0.10, top + 0.06 + subj_h + 0.04, inner, dir_h,
                dl[:keep], sz=750, clr=GREY)); i += 1
    return top + card_h


def _modal(add, M, st, title, blocks, visual=None):
    """Popup overlay in Bariah's reviewed grammar (annotated deck, slide 14).

    Left  — item title, Fungsi dan Penerangan, Contoh when source-attested.
    Right — a dedicated visual-direction panel with its own heading, the SPECIFIC
            direction, and blank production area beneath it.
    Close — icon, top-right, clear of both.
    """
    PX, PW = 1.35, 10.6333
    PY_MIN, PY_BOT = 1.42, 6.88
    AVAIL = PY_BOT - PY_MIN
    spec_only = bool(visual) and visual.get("visual_requirement") != VP.REQUIRED
    LW = 10.07 if spec_only else 5.75      # left content column
    # Focused popup treatment (D2): the popup visual is LARGER than a component-main
    # overview card (capped at OVR_CW_MAX) and carries a single selected subject.
    VX, VW = PX + 6.20, 4.14               # right visual panel — focused, larger
    TW = LW - 1.30 if spec_only else LW   # always clear of the close icon
    kicker, main = (title.split(" — ", 1) if " — " in title else ("", title))
    tsz, tlead = 2000, 0.34
    tl = V3._wrap_lines(main, 54 if spec_only else 38)
    if len(tl) > 1:
        tsz, tlead = 1600, 0.28
        tl = V3._wrap_lines(main, 68 if spec_only else 49)
    head_h = (0.24 if kicker else 0.0) + len(tl) * tlead + 0.14

    WRAPS = ((1250, 92, 0.235), (1150, 100, 0.216), (1050, 110, 0.198)) if spec_only else \
            ((1250, 52, 0.235), (1150, 57, 0.216), (1050, 63, 0.198))
    for bsz, cpl, lead in WRAPS:
        h = 0.0; meas = []
        for hd, lines in blocks:
            wr = []
            for l in lines:
                wr += V3._wrap_lines(l, cpl) or [""]
            bh = 0.26 + 0.02 + len(wr) * lead + 0.16
            meas.append((hd, wr, bh, lead)); h += bh
        ph = max(3.05, 0.16 + head_h + 0.16 + h + 0.24)
        if ph <= AVAIL:
            break
    ph = min(ph, AVAIL)
    PY = PY_MIN if ph > AVAIL - 0.5 else 1.62
    add(box(200, "PopupPanel", PX, PY, PW, ph, "", fill="FFFFFF", ln=BLUE, dash=False, lnw=28575))
    ty = PY + 0.16
    if kicker:
        add(txt(202, "PopupKicker", PX + 0.28, ty, TW, 0.22, rt([kicker]), sz=1100, b=True, clr=GOLD))
        ty += 0.24
    add(txt(201, "PopupTitle", PX + 0.28, ty, TW, len(tl) * tlead + 0.06, rt(tl), sz=tsz, b=True))
    add(close_icon(260, PX + PW - 0.70, PY + 0.18, 0.42))

    y = PY + 0.16 + head_h + 0.16
    i = 210
    for hd, wr, bh, lead in meas:
        if hd.strip().lower() != main.strip().lower():
            add(txt(i, "FHead", PX + 0.28, y, LW, 0.24, [hd], sz=950, b=True, clr=GOLD))
            top = y + 0.26
        else:
            top = y
        i += 1
        add(txt(i, "FBody", PX + 0.28, top, LW, max(0.24, len(wr) * lead), rt(wr), sz=bsz)); i += 1
        y += bh

    # ---- dedicated visual-direction panel ----
    need = bool(visual) and visual.get("visual_requirement") == VP.REQUIRED
    if need and visual.get("visual_status") == "RESOLVED":
        vy = PY + 0.74
        vh = ph - (vy - PY) - 0.26
        add(box(230, "VisualPanel", VX, vy, VW, vh, "", fill="F7F7F7", ln="BFBFBF",
                dash=False, lnw=12700))
        add(txt(231, "VisualPanelHead", VX + 0.18, vy + 0.14, VW - 0.36, 0.24,
                [VD.HEADING], sz=900, b=True, clr=GOLD))
        vw_ = V3._wrap_lines(visual["visual_direction"], max(8, int((VW - 0.36) * 11.3)))
        add(txt(232, "VisualPanelBody", VX + 0.18, vy + 0.42, VW - 0.36,
                min(vh - 0.62, 0.200 * len(vw_) + 0.08), rt(vw_), sz=1150))
        add(txt(233, "VisualPanelArea", VX + 0.18, vy + vh - 0.30, VW - 0.36, 0.22,
                ["Ruang visual produksi — aset tidak dibenamkan."], sz=800, clr=GREY))
    elif need:
        add(txt(231, "VisualPanelPending", VX + 0.18, PY + 0.90, VW - 0.36, 0.60,
                ["ARAHAN VISUAL", VD.PENDING], sz=950, b=True, clr=GREY))


def grid_n(n, y0, h, gx=0.42, gy=0.30):
    """Card grid for ANY item count.

    The v0.3 item_grid tops out at five positions and silently drops the rest, which is
    invisible until a component carries six. Drinking Fountain carries six.
    """
    if n <= 4:
        rows = [n]
    elif n == 5:
        rows = [3, 2]
    elif n == 6:
        rows = [3, 3]
    elif n == 7:
        rows = [4, 3]
    else:
        rows = [4] * (n // 4) + ([n % 4] if n % 4 else [])
    mx = max(rows)
    cw = (BAND_W - (mx - 1) * gx) / mx
    pos, y = [], y0
    for r in rows:
        w = r * cw + (r - 1) * gx
        x0 = (STAGE_W - w) / 2
        pos += [(x0 + c * (cw + gx), y) for c in range(r)]
        y += h + gy
    return pos, cw, y - gy


CAP_H = 0.56                                   # caption strip carved out of the card's own height


def _cards(add, items, labels, viewed, start=40, y0=2.15, sub=False, captions=None):
    """sub=True renders subordinate interactions: shorter cards, smaller type, so an
    example detail reads as primary content and its specifications as secondary.

    captions: one visual direction per item. The strip is carved OUT of the card, so the
    grid pitch, the row bottom and every downstream y stay exactly as they were.
    """
    h = 1.06 if sub else 1.62
    sz = 1350 if sub else 1500
    pos, cw, bottom = grid_n(len(labels), y0, h)
    chh = h - CAP_H if captions else h
    idx = start
    for k, ((x, y), lab, iid) in enumerate(zip(pos, labels, items)):
        v = iid in viewed
        parts = ital_parts(lab)
        it = any(p[1] for p in parts)
        add(card(idx, x, y, cw, chh, lab, ital=it, sz=sz, viewed=v)); idx += 1
        if v:
            add(tick(idx, x + cw - 0.44, y + 0.09, 0.32)); idx += 1
        if captions:
            add(txt(idx, "VisualDir", x + 0.04, y + chh + 0.04, cw - 0.08, CAP_H - 0.06,
                    V3._wrap_lines(captions[k], int((cw - 0.16) / 0.055)),
                    sz=800, clr=GREY)); idx += 1
    return pos, cw, bottom


# ============================ FAMILY STRATEGIES ============================
def render_family_s(M, page, rec, st, add, viewed):
    """FAMILY_S — Struktur Taman. group master -> main -> Contoh -> popup -> all-viewed."""
    role = rec["screen_role"]
    c = M.comps[rec["component_id"]]
    if role == "COMPONENT_MAIN_EXPLANATION":
        add(title_ph_rt(c["name"]), titlebar(6, M.groups[c["group"]]["name"]))
        add(txt(20, "Head", BAND_X, 1.30, BAND_W, 0.46, rt([c["name"]]), sz=2000, b=True))
        sub = C.COMPONENT_SUBSECTIONS.get(rec["component_id"])
        # Bariah's Slide 5 ruling: the sub-heading and its two bullets are additional text on
        # the SAME screen, and the on-screen copy follows the VO. Both surfaces are derived
        # from one controlled record, so they cannot drift apart.
        disp = list(c["display"])
        blocks = [(0, ital_parts(l)) for l in disp]
        if sub:
            disp = disp[:3]                       # the 4th bullet is superseded by the block
            blocks = [(0, ital_parts(l)) for l in disp]
            blocks.append((0, [(sub["heading"], False)]))
            blocks += [(1, ital_parts(b)) for b in sub["bullets"]]
        add(bullets(22, "Body", BAND_X, 1.92, BAND_W, 3.4, blocks, sz=1500, spc=600))
        vp = VP.classify(M, rec, st)
        vbot = 5.10
        if vp["visual_direction"]:
            vbot = _visual(add, 30, 5.10, V3._wrap_lines(vp["visual_direction"], 108))
        # Overview is drawn from the SCREEN's component, on every state of that screen, and
        # is placed BELOW whatever the component direction actually occupied.
        _overview(add, rec["component_id"], vbot + 0.06)
        vo = c["vo"]
        if sub:
            vo = vo + " " + C.subsection_vo(rec["component_id"])
        spoken = [vo + f" Mari lihat contoh bagi {c['name']} di halaman seterusnya."]
        return spoken, ["INTERAKSI:", "  Tiada interaksi kandungan. Kemajuan melalui shell LMS."]

    # example-selection screen (base / popup / all-viewed)
    items = M.items_of(rec["learner_screen_id"])
    labels = [M.rows[i["source_row_uid"]]["label"] for i in items]
    ids = [i["interaction_item_id"] for i in items]
    add(title_ph_rt(f"Contoh {c['name']}"), titlebar(6, f"Contoh {c['name']}"))
    add(txt(25, "Instr", BAND_X, 1.32, BAND_W, 0.42,
            [INS.for_screen(rec)], sz=1600, algn="ctr"))
    vp = VP.classify(M, rec, st)
    # "Semua contoh ada visual" — each card carries its OWN example's source-attested
    # direction. Nothing is composed at screen level, so the screen invents no subject.
    #
    # Captions are derived from the SCREEN, not from this page's state. A base state, a popup
    # state and an all-viewed state are three runtime states of ONE learner screen; deriving
    # from the state made the same screen render three different ways, because a popup state
    # classifies as EXAMPLE_POPUP and an all-viewed state as COMPLETION_STATE.
    cards = VP.example_card_visuals(M, rec)
    caps = None
    if cards and all(c["status"] == "RESOLVED" for c in cards):
        by_item = {c["interaction_item_id"]: c["text"] for c in cards}
        caps = [by_item[i] for i in ids]
    _cards(add, ids, labels, viewed, y0=2.15, captions=caps)
    # No screen-level direction on this screen: a popup state's own direction belongs inside
    # its modal panel, and drawing it again at screen level made the underlying screen appear
    # to carry a direction that changes as the learner clicks.
    _nav(add, st)
    spoken = []
    if st["screen_role"] == "STATE_POPUP":
        iid = st["interaction_item_ids"][0]
        r = M.row_of_item(iid)
        blocks = []
        if r.get("jenis") and r["jenis"].strip() != r["label"].strip():
            blocks.append(("JENIS / BAHAN", [r["jenis"]]))
        if r.get("fungsi"):
            blocks.append(("Fungsi dan Penerangan", r["fungsi"].split("\n")))
        if r.get("contoh"):
            blocks.append(("Contoh", [r["contoh"]]))
        _modal(add, M, st, r["label"], blocks, visual=VP.classify(M, rec, st))
        spoken = [r["vo"]]
    extra = ["INTERAKSI:",
             "  Contoh boleh diklik dalam sebarang susunan.",
             "  Setiap contoh membuka SATU popup. Popup ialah STATE.",
             "  Menutup popup (ikon tutup) kembali ke skrin contoh yang sama.",
             f"  {len(viewed)}/{len(ids)} contoh dilihat."]
    return spoken, extra


def render_family_p1(M, page, rec, st, add, viewed):
    """FAMILY_P1 — Kerusi Taman etc. overview+list -> example detail -> spec popup."""
    role = rec["screen_role"]
    c = M.comps[rec["component_id"]]
    if role == "COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST":
        items = M.items_of(rec["learner_screen_id"])
        labels = [M.rows[i["source_row_uid"]]["label"] for i in items]
        ids = [i["interaction_item_id"] for i in items]
        add(title_ph_rt(c["name"]), titlebar(6, M.groups[c["group"]]["name"]))
        add(txt(20, "Head", BAND_X, 1.22, BAND_W, 0.44, rt([c["name"]]), sz=2000, b=True))
        add(txt(25, "Instr", BAND_X, 1.74, BAND_W, 0.40,
                [INS.for_screen(rec)], sz=1500, algn="ctr"))
        _cards(add, ids, labels, viewed, y0=2.36)
        vp = VP.classify(M, rec, st)
        vbot = 4.86
        if vp["visual_direction"]:
            vbot = _visual(add, 30, 4.86, V3._wrap_lines(vp["visual_direction"], 108))
        # Drawn on the base AND the all-viewed state: the obligation belongs to the screen.
        _overview(add, rec["component_id"], max(5.44, vbot + 0.06))
        _nav(add, st)
        spoken = [c["vo"]] if c.get("vo") else []
        return spoken, ["INTERAKSI:",
                        "  Klik contoh = Bariah Level 1. Membuka skrin penuh, bukan popup.",
                        f"  {len(viewed)}/{len(ids)} contoh dilihat.",
                        "  component_complete hanya benar apabila SEMUA contoh selesai."]

    # full-slide example detail (Level 1 destination) + specification popups (Level 2)
    uid = rec["source_row_uids"][0]
    r = M.rows[uid]
    specs = M.items_of(rec["learner_screen_id"])
    ids = [i["interaction_item_id"] for i in specs]
    labels = [i["label"] for i in specs]
    add(title_ph_rt(r["label"]), titlebar(6, c["name"]))
    add(txt(20, "ExHead", BAND_X, 1.22, BAND_W, 0.44, rt([r["label"]]), sz=2200, b=True))
    add(txt(25, "Instr", BAND_X, 1.76, BAND_W, 0.40,
            [INS.for_screen(rec)], sz=1500, algn="ctr"))
    _, _, cards_bottom = _cards(add, ids, labels, viewed, y0=2.30, sub=True)
    y = cards_bottom + 0.34
    if r.get("contoh"):
        cw_ = V3._wrap_lines(f"Contoh: {r['contoh']}", 104)
        add(txt(70, "ExContoh", BAND_X, y, BAND_W, 0.30 * len(cw_) + 0.10,
                rt(cw_), sz=1400, b=True))
        y += 0.30 * len(cw_) + 0.22
    _visual(add, 30, y, V3._wrap_lines(r.get("visual") or "", 108))
    _nav(add, st)
    spoken = []
    if st["screen_role"] == "STATE_POPUP":
        iid = st["interaction_item_ids"][0]
        it = M.item(iid)
        body = _spec_body(r, it["label"])
        _modal(add, M, st, f"{r['label']} — {it['label']}",
               [(it["label"], V3._wrap_lines(body, 96))],
               visual=VP.classify(M, rec, st))
        spoken = [f"{it['label']}. {body}"]
    extra = ["INTERAKSI:",
             "  Skrin penuh ini ialah hasil Level 1 (klik contoh).",
             "  Klik spesifikasi = Bariah Level 2. Membuka popup (STATE).",
             "  Ikon tutup kembali ke skrin contoh penuh yang SAMA.",
             f"  Kembali -> {st['return_target']} (senarai contoh komponen).",
             f"  {len(viewed)}/{len(ids)} spesifikasi dilihat.",
             "IDENTITI SUMBER:",
             f"  {len(ids)} item interaksi daripada SATU baris sumber: {uid}",
             "  Tiada baris sumber baharu dicipta."]
    return spoken, extra


def render_family_p2(M, page, rec, st, add, viewed):
    """FAMILY_P2 — Papan Tanda, BBQ Pit. explanation + spec-category list -> popup."""
    c = M.comps[rec["component_id"]]
    uid = rec["source_row_uids"][0]
    r = M.rows[uid]
    cats = M.items_of(rec["learner_screen_id"])
    ids = [i["interaction_item_id"] for i in cats]
    labels = [i["label"] for i in cats]
    add(title_ph_rt(c["name"]), titlebar(6, M.groups[c["group"]]["name"]))
    add(txt(20, "Head", BAND_X, 1.22, BAND_W, 0.44, rt([c["name"]]), sz=2000, b=True))
    add(txt(21, "Sub", BAND_X, 1.72, BAND_W, 0.36, rt([r["label"]]), sz=1400, b=True, clr=GOLD))
    add(txt(25, "Instr", BAND_X, 2.10, BAND_W, 0.40,
            [INS.for_screen(rec)], sz=1500, algn="ctr"))
    _cards(add, ids, labels, viewed, y0=2.68)
    vp = VP.classify(M, rec, st)
    vbot = 4.86
    if vp["visual_direction"]:
        vbot = _visual(add, 30, 4.86, V3._wrap_lines(vp["visual_direction"], 108))
    # Drawn on the base state, all four specification-popup states and the all-viewed state.
    _overview(add, rec["component_id"], max(5.44, vbot + 0.06))
    _nav(add, st)
    spoken = []
    if st["screen_role"] == "STATE_POPUP":
        it = M.item(st["interaction_item_ids"][0])
        body = _spec_body(r, it.get("source_attested_label") or it["label"])
        _modal(add, M, st, f"{r['label']} — {it['label']}",
               [(it["label"], V3._wrap_lines(body, 96))],
               visual=VP.classify(M, rec, st))
        spoken = [f"{it['label']}. {body}"]
    extra = ["INTERAKSI:",
             "  Klik kategori spesifikasi = Level 1. Membuka popup (STATE).",
             f"  Ikon tutup kembali ke senarai spesifikasi ({st['return_target']}).",
             "  TIADA skrin Contoh satu item untuk komponen ini.",
             f"  {len(viewed)}/{len(ids)} kategori dilihat.",
             "IDENTITI SUMBER:",
             f"  {len(ids)} kategori interaksi daripada SATU baris sumber: {uid}",
             "  Tiada baris sumber baharu dicipta."]
    return spoken, extra


def _sentence(s):
    """A specification fragment lifted out of 'Label: text' starts a sentence once the
    label becomes the heading. Only the first character changes; wording is untouched."""
    return (s[:1].upper() + s[1:]) if s and s[:1].islower() else s


def _spec_body(row, label):
    """The module's own labelled specification line for this row. Source-attested."""
    for line in (row.get("fungsi") or "").split("\n"):
        if ":" in line and line.split(":", 1)[0].strip().lower() == label.strip().lower():
            return _sentence(line.split(":", 1)[1].strip())
    # normalised label (e.g. 'Bahan Struktur/Tiang' vs source 'Bahan struktur/tiang')
    for line in (row.get("fungsi") or "").split("\n"):
        if ":" in line:
            k = line.split(":", 1)[0].strip().lower().replace("/", " ").replace("  ", " ")
            if k == label.strip().lower().replace("/", " ").replace("  ", " "):
                return _sentence(line.split(":", 1)[1].strip())
    raise KeyError(f"no source-attested specification line '{label}' in {row['uid']}")


FAMILY_STRATEGY = {
    "FAMILY_S": render_family_s,
    "FAMILY_P1": render_family_p1,
    "FAMILY_P2": render_family_p2,
}


# ============================ FRAME STRATEGY ============================
def render_frame(M, page, rec, st, add, viewed):
    sid = rec["learner_screen_id"]
    role = st["screen_role"]

    # ---------------- S01 — topic/section entry ----------------
    if sid == "SCR_S01":
        vp = VP.classify(M, rec, st)
        add(title_ph_rt(C.S01["display_title"]), titlebar(6, C.S01["display_title"], w=12.4))
        add(txt(20, "Course", BAND_X, 1.44, BAND_W, 0.44, rt([C.S01["canvas"][0]]),
                sz=1600, b=True, clr=GOLD))
        add(txt(21, "PL", BAND_X, 2.00, BAND_W, 0.46, rt([C.S01["canvas"][1]]), sz=1900, b=True))
        # The Topik/Bahagian line is body copy on Bariah's corrected S01, below the PL06 line
        # and distinct from the page title band. Frozen evidence: B02_BARIAH_S01_EVIDENCE.jpg.
        add(txt(22, "Topic", BAND_X, 2.56, BAND_W, 0.46, rt([C.S01["canvas"][2]]), sz=1900, b=True))
        # Her corrected page keeps the ARAHAN VISUAL heading above the direction. The heading is
        # controlled copy; the direction itself still comes from the visual policy, single-source.
        _visual(add, 30, 3.30,
                [C.S01["visual"][0]] + V3._wrap_lines(vp["visual_direction"], 96))
        _nav(add, st)
        el = sorted(st["spoken_transcript_elements"], key=lambda e: e["order"])
        extra = ["KONTEKS HULU:", "  " + ", ".join(rec["upstream_context"]),
                 "  Montaj Kursus dan Montaj PL06 telah menyampaikan pengenalan kursus,",
                 "  lapan Pakej Latihan, objektif PL06, tujuh topik PL06 dan Hilmi.",
                 "  Skrin ini BERMULA di aras bahagian dan TIDAK mengulanginya.",
                 "TRANSKRIP DITUTURKAN (slide 1 sahaja):"]
        extra += [f"  {e['order']}. {e['element']}" for e in el]
        extra += ["  Tajuk kursus kekal visual sahaja — tidak dituturkan.",
                  "NOTA PRODUKSI:", "  " + rec["production_note"]]
        return None, extra

    # ---------------- S02 — scenario ----------------
    if sid == "SCR_S02":
        add(title_ph_rt(C.S02["canvas_title"]), titlebar(6, C.S02["canvas_title"]))
        _visual(add, 30, 1.32, C.S02["visual"])
        y = 2.50
        for k, (nm, role_lbl) in enumerate(C.S02["cast"]):
            add(txt(40 + k * 2, "CastName", BAND_X, y, 5.0, 0.42, [nm], sz=1900, b=True))
            add(txt(41 + k * 2, "CastRole", BAND_X, y + 0.44, 5.6, 0.34, [role_lbl], sz=1300, clr=GREY))
            y += 1.10
        add(txt(60, "Note", BAND_X, 5.10, BAND_W, 0.40, [C.S02["canvas_note"]], sz=1300, clr=GREY))
        _nav(add, st)
        spoken = [f"{sp}: {ln}" for sp, ln in C.S02["dialogue"]]
        om = rec["omitted_content"][0]
        extra = ["WATAK:"]
        for ch in rec["characters"]:
            extra.append(f"  {ch['character_name']} — {ch['canonical_role']}")
            extra.append(f"    {ch['scene_role']}")
        extra += ["  Label peranan generik (Pelatih / Penyelia Tapak) ialah metadata produksi",
                  "  sahaja dan BUKAN nama akhir yang dilihat pelajar.",
                  "KANDUNGAN DIKELUARKAN:", f"  \"{om['text']}\"",
                  f"  sebab: {om['reason']}", f"  status: {om['status']}",
                  f"  gantian: {om['replacement']}",
                  "KESINAMBUNGAN:", "  " + rec["continuity"]]
        return spoken, extra

    # ---------------- S03 — Hilmi overview ----------------
    if sid == "SCR_S03":
        add(title_ph_rt(C.S03["canvas_title"]), titlebar(6, C.S03["canvas_title"]))
        _visual(add, 30, 1.30, C.S03["visual"], w=5.3, x=BAND_X)
        add(txt(40, "Narr", BAND_X, 2.28, 5.3, 0.40, [C.S03["narrator"]], sz=1800, b=True))
        add(txt(41, "NarrRole", BAND_X, 2.70, 5.3, 0.32, [C.S03["narrator_role"]], sz=1200, clr=GREY))
        gx = 6.55
        for k, g in enumerate(C.S03["groups"]):
            add(txt(50 + k, "Grp", gx, 1.32 + k * 0.86, 6.0, 0.80, rt(V3._wrap_lines(g, 52)),
                    sz=1250, b=True))
        _visual(add, 60, 3.20, C.S03["mindmap"], w=6.0, x=gx, sz=1000)
        add(txt(70, "Reflect", BAND_X, 5.36, BAND_W, 0.72,
                rt(V3._wrap_lines(C.S03["reflection"], 96)), sz=1500, b=True, clr=GOLD))
        _nav(add, st)
        spoken = [C.S03["vo"], C.S03["vo2"]]
        nc = rec["narrator_continuity"]
        extra = ["NARATOR:", f"  {rec['characters'][0]['character_name']} — "
                            f"{rec['characters'][0]['canonical_role']}",
                 "  HILMI_REINTRODUCED_AS_NEW = false",
                 "  HILMI_CONTINUITY_FROM_COURSE_MONTAGE = true",
                 "  " + nc["rule"],
                 "  Pembukaan dilarang: " + "; ".join(nc["forbidden_openings"]),
                 "  " + nc["spoken_content_requirement"],
                 "NOTA PRODUKSI:", "  " + rec["production_note"]]
        return spoken, extra

    # ---------------- Struktur Taman group master ----------------
    if sid == "SCR_GM_STRUKTUR":
        g = M.groups["STRUKTUR_TAMAN"]
        members = [c for c in M.source["components"] if c["group"] == "STRUKTUR_TAMAN"]
        pos, cw, x0, _ = grid4()
        add(title_ph_rt(g["name"]), titlebar(6, g["name"]))
        add(txt(25, "Instr", BAND_X, 1.15, BAND_W, 0.40,
                [INS.for_screen(rec)], sz=1600, algn="ctr"))
        done = st["screen_role"] == "STATE_GROUP_COMPLETE"
        proof_done = page.get("completed_components", set())
        n = 40
        for (x, y), c in zip(pos, members):
            v = done or c["id"] in proof_done
            parts = ital_parts(c["name"])
            add(card(n, x, y, cw, 1.9901, c["name"], ital=any(p[1] for p in parts),
                     sz=1600, viewed=v)); n += 1
            if v:
                add(tick(n, x + cw - 0.52, y + 0.12, TICK)); n += 1
        _nav(add, st)
        spoken = [g["vo"]] if st["screen_role"] != "STATE_GROUP_COMPLETE" else []
        extra = ["INTERAKSI:",
                 "  Empat kad komponen. Boleh diklik dalam sebarang susunan.",
                 "  Setiap komponen yang selesai menerima tik.",
                 "  Kemajuan kumpulan dikawal oleh Seterusnya shell LMS.",
                 "  TIADA butang Seterusnya tersuai dilukis pada kanvas pelajar.",
                 "SASARAN KEMBALI:",
                 "  Skrin contoh Family S kembali ke sini."]
        return spoken, extra

    # ---------------- Perabot overview (non-interactive gateway) ----------------
    if sid == "SCR_PERABOT_OVERVIEW":
        g = M.groups["PERABOT_TAMAN"]
        members = [c for c in M.source["components"] if c["group"] == "PERABOT_TAMAN"]
        add(title_ph_rt(g["name"]), titlebar(6, g["name"]))
        add(txt(22, "Body", BAND_X, 1.22, BAND_W, 0.86,
                rt(V3._wrap_lines(g["vo"], 118)[:3]), sz=1200))
        # Visual component gateway. Each card carries the learner-facing component name and
        # its own visual placeholder. Execution family is model metadata and stays off-canvas.
        pos, cw, bottom = grid_n(len(members), 2.18, 2.02)
        n = 80
        for (x, y), c in zip(pos, members):
            row0 = [r for r in M.source["rows"] if r["comp"] == c["id"]][0]
            vis = VD.for_row(row0)
            add(box(n, "ComponentCard", x, y, cw, 2.02, "", fill="F2F2F2",
                    ln="404040", dash=False, lnw=12700)); n += 1
            add(box(n, "ComponentVisual", x + 0.14, y + 0.14, cw - 0.28, 1.06, "",
                    fill="FFFFFF", ln="BFBFBF", dash=True, lnw=9525)); n += 1
            add(txt(n, "ComponentVisualDir", x + 0.22, y + 0.24, cw - 0.44, 0.88,
                    rt(["ARAHAN VISUAL"] + V3._wrap_lines(
                        vis["text"] if vis["status"] == "RESOLVED" else VD.PENDING, 30)[:3]),
                    sz=750, clr=GREY)); n += 1
            add(txt(n, "ComponentName", x + 0.14, y + 1.28, cw - 0.28, 0.40,
                    rt([c["name"]]), sz=1400, b=True, algn="ctr")); n += 1
            add(txt(n, "ComponentCue", x + 0.14, y + 1.68, cw - 0.28, 0.28,
                    ["Halaman seterusnya"], sz=900, clr=GREY, algn="ctr")); n += 1
        _nav(add, st)
        spoken = [g["vo"], "Mari lihat setiap contoh perabot di halaman seterusnya."]
        extra = ["INTERAKSI:",
                 "  TIADA klik dan TIADA aras interaksi. Ini gerbang penerangan visual.",
                 "  Pelajar memasuki setiap komponen melalui navigasi shell.",
                 "AGIHAN KELUARGA (metadata dalaman — tidak dipaparkan pada kanvas):"]
        extra += [f"  {c['name']} -> {M.family(c['id'])}" for c in members]
        return spoken, extra

    # ---------------- Rumusan ----------------
    if sid == "SCR_RUMUSAN":
        add(title_ph_rt(C.RUMUSAN["canvas_title"]), titlebar(6, C.RUMUSAN["canvas_title"]))
        _visual(add, 30, 1.30, C.RUMUSAN["visual"])
        y = 2.20
        for k, l in enumerate(C.RUMUSAN["lines"]):
            w = V3._wrap_lines(l, 96)
            add(txt(40 + k, "RumLine", BAND_X, y, BAND_W, 0.30 * len(w) + 0.10, rt(w), sz=1450))
            y += 0.30 * len(w) + 0.36
        _nav(add, st)
        extra = ["INTERAKSI:", "  Tiada. Rumusan aras Bahagian.",
                 "LABEL DILARANG DIPAPARKAN:",
                 "  " + ", ".join(rec["forbidden_labels"]),
                 "NOTA PRODUKSI:", "  " + rec["production_note"]]
        return [C.RUMUSAN["vo"]], extra

    # ---------------- Kuiz ----------------
    if sid == "SCR_KUIZ":
        return _render_quiz(M, page, rec, st, add)

    # ---------------- Tamat ----------------
    if sid == "SCR_TAMAT":
        add(title_ph_rt("Tamat"), titlebar(6, "Tamat"))
        y = 1.36
        for k, blk in enumerate(C.TAMAT["hierarchy"]):
            for j, line in enumerate(blk):
                add(txt(20 + k * 4 + j, "TamatLine", BAND_X, y, BAND_W, 0.46,
                        rt([line]), sz=(2000 if k == 2 else 1500),
                        b=True, clr=(None if k == 2 else GOLD)))
                y += 0.44
            y += 0.30
        add(txt(60, "TamatInstr", BAND_X, y + 0.30, BAND_W, 0.46,
                rt([C.TAMAT["instruction"]]), sz=1700, b=True))
        _nav(add, st)
        ex = rec["exit_model"]
        extra = ["KELUAR / NAVIGASI:",
                 f"  salinan Tamat: {C.TAMAT['copy_status']}",
                 f"  destinasi logik: {ex['logical_destination']}",
                 f"  kelakuan navigasi fizikal: {C.TAMAT['physical_status']}",
                 # Firdaus / LMS owner ruling, Stage 4.2E-A. Production metadata only —
                 # the learner-facing copy is unchanged and no route is claimed as proven.
                 "  MEKANISME NAVIGASI (FIRDAUS / PEMILIK LMS):",
                 "    tindakan pelajar: menutup lesson/content window",
                 "    hasil navigasi: kembali ke course menu",
                 "    langkah seterusnya: pelajar memilih bahagian pembelajaran seterusnya",
                 "    laluan seterusnya automatik: TIDAK TERBUKTI",
                 "    LMS shell Next: TIDAK TERBUKTI",
                 "  Tiada dakwaan dibuat tentang keadaan Seterusnya shell LMS.",
                 "  Tiada butang navigasi kanvas tersuai dicipta.",
                 "  Segitiga merah dalam contoh Bariah dianggap ISYARAT VISUAL,",
                 "  bukan butang interaktif, sehingga ada bukti sebaliknya."]
        return [C.TAMAT["vo"]], extra

    raise KeyError(f"no frame strategy for {sid}")


def _render_quiz(M, page, rec, st, add):
    role = st["screen_role"]
    q = rec["quiz_spec"]
    if role == "STATE_QUIZ_INTRO":
        add(title_ph_rt("Kuiz"), titlebar(6, C.KUIZ_INTRO["canvas_title"]))
        add(txt(20, "Strap", BAND_X, 1.26, BAND_W, 0.36, [C.KUIZ_INTRO["strap"]], sz=1300, clr=GOLD))
        y = 1.86
        for k, l in enumerate(C.KUIZ_INTRO["purpose"]):
            w = V3._wrap_lines(l, 92)
            add(txt(30 + k, "Purpose", BAND_X, y, BAND_W, 0.32 * len(w) + 0.08, w, sz=1500))
            y += 0.32 * len(w) + 0.24
        y += 0.20
        for k, l in enumerate(C.KUIZ_INTRO["instruction"] + [INS.for_page(rec, st)]):
            add(txt(40 + k, "Instr", BAND_X, y, BAND_W, 0.40, rt([l]), sz=1600,
                    b=(k == len(C.KUIZ_INTRO["instruction"]))))
            y += 0.44
        for k, lbl in enumerate(C.KUIZ_INTRO["result_controls"]):
            add(txt(50 + k, "Ctl", BAND_X + k * 3.2, 5.60, 3.0, 0.36, [lbl], sz=1300, clr=GREY))
        _nav(add, st)
        extra = ["KUIZ:",
                 f"  {q['question_count']} soalan — {q['mcq']} MCQ + {q['multiple_response']} Multiple Response",
                 f"  Lulus: {q['pass_mark']}   Menyekat kemajuan: {'YA' if q['blocking'] else 'TIDAK'}",
                 f"  Cuba semula: {q['retry']}",
                 "  Semakan pengetahuan sahaja, bukan gred peperiksaan akhir kursus."]
        return [" ".join(C.KUIZ_INTRO["instruction"])], extra

    if role == "STATE_QUIZ_QUESTION":
        n = int(st["runtime_state_id"][-1])
        d = C.QUESTIONS[n]
        add(title_ph_rt(f"Kuiz — Soalan {n}"), titlebar(6, f"Soalan {n}"))
        add(txt(20, "Kind", BAND_X, 1.26, BAND_W, 0.32,
                rt([f"{'MCQ' if d['kind']=='MCQ' else 'Multiple Response'}"
                    f"   ·   sumber: {d['src']}"]), sz=1150, clr=GREY))
        w = V3._wrap_lines(d["stem"], 92)
        add(txt(22, "Stem", BAND_X, 1.62, BAND_W, 0.34 * len(w) + 0.10, rt(w), sz=1600, b=True))
        y = 1.62 + 0.34 * len(w) + 0.16
        add(txt(23, "Instr", BAND_X, y, BAND_W, 0.34, [INS.for_page(rec, st)], sz=1400, b=True))
        y += 0.44
        # Fit the options, the reviewer answer key and the feedback row inside the stage.
        BOTTOM = 7.02
        key = ([f"Jawapan: {d['answer']}", dict(d["options"])[d["answer"]]]
               if d["kind"] == "MCQ" else
               ["Jawapan betul:"] + [f"•  {o}" for o in d["answers"]])
        for opitch, osz, kpitch, ksz in ((0.42, 1450, 0.28, 1250), (0.36, 1350, 0.25, 1150),
                                         (0.32, 1250, 0.22, 1050), (0.29, 1150, 0.20, 950)):
            need = len(d["options"]) * opitch + 0.16 + (0.34 + kpitch * len(key)) + 0.16 + 0.32
            if y + need <= BOTTOM:
                break
        oy = y
        if d["kind"] == "MCQ":
            for k, (lab, opt) in enumerate(d["options"]):
                add(txt(40 + k, "Opt", BAND_X + 0.30, oy, BAND_W - 0.6, opitch - 0.04,
                        rt([f"{lab}.  {opt}"]), sz=osz))
                oy += opitch
        else:
            for k, opt in enumerate(d["options"]):     # no A/B/C labels, learner-facing
                add(txt(40 + k, "Opt", BAND_X + 0.30, oy, BAND_W - 0.6, opitch - 0.04,
                        rt([opt]), sz=osz))
                oy += opitch
        # ---- reviewer answer key, generated from the same structured answer data ----
        oy += 0.16
        kh = 0.34 + kpitch * len(key)
        add(box(70, "AnswerKeyBox", BAND_X, oy, BAND_W, kh, "", fill="FFF7E6",
                ln=GOLD, dash=False, lnw=12700))
        add(txt(71, "AnswerKeyHead", BAND_X + 0.20, oy + 0.06, BAND_W - 0.4, 0.24,
                ["SEMAKAN CIDB — MAKLUMAT PENYEMAK, BUKAN PAPARAN PELAJAR"],
                sz=850, b=True, clr=GOLD))
        add(txt(72, "AnswerKeyBody", BAND_X + 0.20, oy + 0.32, BAND_W - 0.4, kpitch * len(key),
                rt(key), sz=ksz, b=True))
        oy += kh + 0.16
        fb = C.FEEDBACK
        add(txt(75, "FbC", BAND_X, oy, 5.6, 0.30, [fb["correct"]["text"]], sz=1250, clr=GREEN))
        add(txt(76, "FbW", BAND_X + 6.0, oy, 5.6, 0.30, [fb["incorrect"]["text"]],
                sz=1250, clr="C0392B"))
        _nav(add, st)
        spoken = [d["stem"]]
        if d["kind"] == "MCQ":
            spoken += [f"{lab}. {opt}" for lab, opt in d["options"]]
        else:
            spoken += list(d["options"])
        # Bariah 1 Aug 7:03 PM (D3): learner feedback after submission only.
        # QUIZ_FEEDBACK_VO = NOT_REQUIRED unless separately authorised, so the two feedback
        # strings are rendered on canvas and described in the production panel, but are NOT
        # added to the spoken transcript.
        extra = ["MAKLUM BALAS SERTA-MERTA:",
                 f"  betul: teks \"{fb['correct']['text']}\" · SFX {fb['correct']['sfx']} · TIADA VO",
                 f"  salah: teks \"{fb['incorrect']['text']}\" · SFX {fb['incorrect']['sfx']} · TIADA VO",
                 "  maklum balas dipaparkan selepas penghantaran sahaja; tidak dituturkan.",
                 "KUNCI JAWAPAN (blok semakan CIDB pada halaman semakan):",
                 "  " + (d["answer"] if d["kind"] == "MCQ" else ", ".join(d["answers"])),
                 "  Dijana daripada data jawapan berstruktur yang sama dengan logik kuiz.",
                 "  BUKAN kandungan masa jalan pra-hantar; tidak dibaca dalam VO.",
                 "RASIONAL TERPERINCI (metadata sahaja):"]
        extra += ["  " + l for l in V3._wrap_lines(d["rationale"], 66)]
        if d["kind"] == "MULTIPLE_RESPONSE":
            extra += ["LABEL PILIHAN:", "  TIADA label A/B/C pada pilihan pelajar."]
        return spoken, extra

    if role == "STATE_QUIZ_REVIEW":
        d = C.REVIEW
        add(title_ph_rt(d["canvas_title"]), titlebar(6, d["canvas_title"]))
        add(txt(20, "Intro", BAND_X, 1.30, BAND_W, 0.40, [d["intro"]], sz=1600, b=True))
        y = 1.92
        for q in sorted(C.QUESTIONS):
            qq = C.QUESTIONS[q]
            ans = qq["answer"] if qq["kind"] == "MCQ" else ", ".join(qq["answers"])
            w = V3._wrap_lines(f"Soalan {q}: {qq['stem']}", 104)
            add(txt(40 + q * 2, "RvQ", BAND_X, y, BAND_W, 0.28 * len(w) + 0.06, rt(w), sz=1250))
            y += 0.28 * len(w) + 0.04
            add(txt(41 + q * 2, "RvA", BAND_X + 0.30, y, BAND_W - 0.6, 0.30,
                    rt([f"Jawapan: {ans}"]), sz=1250, b=True, clr=GREEN))
            y += 0.42
        add(button(60, BAND_X, 6.44, 2.30, 0.46, "Ulang Kuiz", True))
        _nav(add, st)
        extra = ["SEMAK JAWAPAN:",
                 "  Jawapan betul dipaparkan bagi kelima-lima soalan.",
                 "  Cuba semula bersifat sukarela.",
                 "RASIONAL TERPERINCI:", "  " + d["note"],
                 f"  status: {st.get('unresolved_status')}"]
        return [], extra

    # result
    d = C.RESULT
    add(title_ph_rt("Kuiz — Keputusan"), titlebar(6, d["canvas_title"]))
    add(txt(20, "Score", BAND_X, 1.60, BAND_W, 0.80, [f"Markah: {d['sample_score']}"], sz=2800, b=True))
    add(txt(21, "Verdict", BAND_X, 2.50, BAND_W, 0.50, [d["verdicts"][0]], sz=2200, b=True, clr=GREEN))
    add(txt(22, "Pass", BAND_X, 3.10, BAND_W, 0.36, [d["pass_mark"]], sz=1300, clr=GREY))
    for k, lbl in enumerate(d["controls"]):
        add(button(60 + k, BAND_X + k * 2.6, 4.10, 2.30, 0.46, lbl, True))
    _nav(add, st)
    extra = ["KEPUTUSAN:",
             f"  Markah dipaparkan. Keputusan: {' / '.join(d['verdicts'])}. {d['pass_mark']}.",
             f"  Kawalan: {', '.join(d['controls'])}. Cuba semula: sukarela.",
             "  Markah di bawah 60% TIDAK menyekat kemajuan yang lebih luas.",
             "RASIONAL TERPERINCI:",
             "  Kekal sebagai metadata produksi sahaja sehingga Bariah mengesahkan",
             "  penempatan akhirnya (U-05)."]
    return [d["vo"]], extra


# ============================ page assembly ============================
def build_page(M, page, pages):
    rec = M.screen(page["screen_id"])
    st = M.state(page["state_id"])
    if st["next_control_type"] not in M.control_types or \
       st["back_control_type"] not in M.control_types or \
       st["close_control_type"] not in M.control_types:
        raise ValueError(f"control type outside the model vocabulary on {page['id']}")
    sh = []
    add = lambda *x: sh.extend(x)
    instruction = INS.for_page(rec, st)
    viewed = ADAPT.viewed_items(M, page, pages)
    page["completed_components"] = ADAPT.completed_components(M, page, pages)
    fam = st["execution_family"]
    # Component screens dispatch on the model-assigned execution family. Group masters,
    # gateways and frames are not component screens and never reach a family strategy.
    if fam in FAMILY_STRATEGY and rec.get("component_id"):
        spoken, extra = FAMILY_STRATEGY[fam](M, page, rec, st, add, viewed)
    else:
        spoken, extra = render_frame(M, page, rec, st, add, viewed)
    # Canvas instruction and spoken instruction come from the SAME field. If the screen
    # carries one, it is appended to the spoken transcript verbatim.
    spoken = list(spoken or [])
    if instruction and st["notes_policy"] != "SILENT_STATE_NOTES" and instruction not in spoken:
        spoken.append(instruction)
    nblocks = build_notes_blocks(M, rec, st, spoken, instruction)
    notes = blocks_to_text(nblocks)
    if instruction:
        extra = (extra or []) + ["ARAHAN INTERAKSI (kanvas = VO):", "  " + instruction]
    vpol = VP.classify(M, rec, st)
    extra = (extra or []) + [
        "VISUAL:",
        f"  subjenis skrin: {vpol['semantic_screen_subtype']}",
        f"  subjenis popup: {vpol['popup_subtype'] or '—'}",
        f"  keperluan visual: {vpol['visual_requirement']}",
        f"  status: {vpol['visual_status']}",
        f"  kuasa: {vpol['visual_authority'] or '—'}"]
    if vpol.get("proposal_class"):
        extra += [f"  kelas cadangan: {vpol['proposal_class']}"]
    if vpol.get("evidence_conflict"):
        ec = vpol["evidence_conflict"]
        extra += ["  KONFLIK BUKTI — PENDING_BARIAH_CONFIRMATION:",
                  "    dirender: " + ec["rendered"],
                  "    alternatif beku: " + ec["frozen_alternative"],
                  "    lokasi: " + ec["frozen_locator"]]
    if vpol.get("superseded_ruling"):
        sr = vpol["superseded_ruling"]
        extra += ["  ARAHAN DIGANTI — SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT:",
                  "    aktif: " + sr["active_direction"],
                  "    diganti: " + sr["superseded_direction"],
                  "    lokasi lama: " + sr["superseded_locator"],
                  "    bukti pengganti: " + sr["superseding_evidence"],
                  "    nota: " + sr["note"]]
    if vpol.get("example_card_visuals"):
        extra += ["  visual setiap contoh (satu per kad):"] + [
            f"    {c['label']} — {c['text']}" for c in vpol["example_card_visuals"]]
    lines = model_lines(M, rec, st, extra)
    lines.insert(0, f"BUKTI: {page['proof_note']}")
    sh.append(prodpanel_v4(9, page, rec, st, lines))
    return sh, notes, nblocks


# ============================ package ============================
DONOR = os.path.join(GEN, "donor_skeleton")


def generate(outdir, outname=OUTNAME, page_fn=None):
    M = ADAPT.Model()
    pages = (page_fn or ADAPT.proof_pages)(M)
    work = os.path.join(outdir, "_build_" + outname.replace(".pptx", ""))
    if os.path.exists(work):
        shutil.rmtree(work)
    shutil.copytree(DONOR, work)
    rd = lambda p: open(os.path.join(work, p), encoding="utf-8").read()
    wr = lambda p, s: open(os.path.join(work, p), "w", encoding="utf-8").write(s)
    for d in ("ppt/slides", "ppt/notesSlides"):
        os.makedirs(os.path.join(work, d, "_rels"), exist_ok=True)
        for f in os.listdir(os.path.join(work, d)):
            if f.endswith(".xml"):
                os.remove(os.path.join(work, d, f))
        for f in os.listdir(os.path.join(work, d, "_rels")):
            os.remove(os.path.join(work, d, "_rels", f))

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
        shapes, notes, nblocks = build_page(M, page, pages)
        wr(f"ppt/slides/slide{i}.xml", HDR + "".join(shapes) + FTR)
        wr(f"ppt/slides/_rels/slide{i}.xml.rels",
           '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships '
           'xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
           '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
           'relationships/slideLayout" Target="../slideLayouts/slideLayout7.xml"/>'
           f'<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
           f'relationships/notesSlide" Target="../notesSlides/notesSlide{i}.xml"/></Relationships>')
        # Speaker Notes carry REAL OOXML run formatting, not markdown or slanted glyphs.
        # Every glossary term becomes its own <a:r> with i="1"; the rest stays plain.
        def _note_para(b):
            if not b["text"]:
                return '<a:p><a:endParaRPr lang="en-MY" dirty="0"/></a:p>'
            runs_xml = ""
            for r in b["runs"]:
                it = ' i="1"' if r["italic"] else ""
                runs_xml += (f'<a:r><a:rPr lang="en-MY"{it} dirty="0"/>'
                             f'<a:t>{X(r["text"])}</a:t></a:r>')
            return f"<a:p>{runs_xml}</a:p>"
        body = "".join(_note_para(b) for b in nblocks)
        if not body:
            body = '<a:p><a:endParaRPr lang="en-MY" dirty="0"/></a:p>'
        wr(f"ppt/notesSlides/notesSlide{i}.xml", NOTE_DONOR[:m.start(2)] + body + NOTE_DONOR[m.end(2):])
        wr(f"ppt/notesSlides/_rels/notesSlide{i}.xml.rels", NRELS.replace("{n}", str(i)))
        manifest.append(dict(slide=i, page=page["id"], screen=page["screen_id"],
                             state=page["state_id"], role=page["review_page_role"],
                             family=page["execution_family"], notes_chars=len(notes),
                             notes_blocks=nblocks,
                             spoken_export=spoken_export(nblocks)))
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
       '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
       '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
       + "".join(rels) + "</Relationships>")
    ct = rd("[Content_Types].xml")
    ct = re.sub(r'<Override PartName="/ppt/(slides|notesSlides)/[^"]+"[^/]*/>', "", ct)
    ins = "".join(
        f'<Override PartName="/ppt/slides/slide{i}.xml" ContentType="application/vnd.openxmlformats-'
        f'officedocument.presentationml.slide+xml"/>'
        f'<Override PartName="/ppt/notesSlides/notesSlide{i}.xml" ContentType="application/vnd.'
        f'openxmlformats-officedocument.presentationml.notesSlide+xml"/>' for i in range(1, N + 1))
    ct = ct.replace("</Types>", ins + "</Types>")
    wr("[Content_Types].xml", ct)

    out = os.path.join(outdir, outname)
    if os.path.exists(out):
        os.remove(out)
    zf = zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED)
    for root, _, files in os.walk(work):
        for f in sorted(files):
            p = os.path.join(root, f)
            zf.write(p, os.path.relpath(p, work).replace(os.sep, "/"))
    zf.close()
    shutil.rmtree(work)
    return out, manifest


FULL_OUTNAME = "K5PL06T03B02_STORYBOARD_FOR_BARIAH_REVIEW_v0_4_4.pptx"


def generate_full(outdir, outname=FULL_OUTNAME):
    """The complete clean v0.4 review deck: one page per runtime state."""
    return generate(outdir, outname=outname, page_fn=ADAPT.all_pages)


if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    mode = sys.argv[2] if len(sys.argv) > 2 else "proof"
    out, man = (generate_full(outdir) if mode == "full" else generate(outdir))
    print("wrote", out, "pages", len(man))
