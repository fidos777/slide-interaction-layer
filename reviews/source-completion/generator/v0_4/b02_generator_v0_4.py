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
    """Split a string into (text, italic) runs for the approved English-origin terms.
    Production IDs are never italicised even when they look English."""
    if not s:
        return [("", False)]
    terms = sorted(C.ITALIC_TERMS, key=len, reverse=True)
    pat = re.compile("(" + "|".join(re.escape(t) for t in terms) + ")")
    out = []
    for tok in pat.split(s):
        if not tok:
            continue
        is_term = tok in C.ITALIC_TERMS
        if is_term and any(tok.startswith(p) for p in C.NEVER_ITALIC_PREFIXES):
            is_term = False
        out.append((tok, is_term))
    return out or [(s, False)]


def rt(lines):
    """Lines -> para()-compatible rich-text parts."""
    return [ital_parts(l) for l in lines]


# ============================ new controls ============================
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
TOKENS_V4 = ["PROOF_BUILD", "V0_4_MODEL_DRIVEN", "NOT_FOR_MMD_BUILD",
             "MULTIMEDIA_NOT_PRODUCED", "PRODUCTION_APPROVAL_NOT_CLAIMED"]


def prodpanel_v4(i, page, rec, st, lines):
    head = ["K5 PL06 T03 B02 — PAPAN CERITA v0.4 (BUKTI TIGA KELUARGA)",
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
def build_notes(M, rec, st, spoken):
    """Structured Notes. Context headers and spoken transcript stay unambiguous."""
    spec = M.notes_spec(st)
    if spec["policy"] == "SILENT_STATE_NOTES":
        return ""                       # genuinely empty. No placeholder, no headers.
    if spec["context_spoken"]:
        # S01 only: the entry titles ARE the spoken transcript.
        el = spec["spoken_elements"] or []
        return "\n".join(e["text"] for e in sorted(el, key=lambda e: e["order"]))
    out = ["NON-SPOKEN CONTEXT", ""]
    out += spec["context_headers"]
    out += ["", "SPOKEN TRANSCRIPT", ""]
    out += spoken if isinstance(spoken, list) else [spoken]
    return "\n".join(out).rstrip()


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
    add(txt(i, "VisualDir", x, y, w, 0.28 * len(lines) + 0.12, lines, sz=sz, clr=GREY))


def _modal(add, M, st, title, blocks, note_lines=None):
    """Popup overlay. Close control is an icon; children are measured to fit inside.

    A long title is split into a small kicker (the owning row) plus the item name, and
    the head band is measured rather than assumed — a two-line title must not spill.
    """
    PX, PW = 1.35, 10.6333
    PY_MIN, PY_BOT = 1.42, 6.88
    AVAIL = PY_BOT - PY_MIN
    TW = PW - 1.30                       # title width, leaving room for the close icon
    kicker, main = (title.split(" — ", 1) if " — " in title else ("", title))
    tsz, tlead = 2000, 0.34
    tl = V3._wrap_lines(main, 62)
    if len(tl) > 1:
        tsz, tlead = 1600, 0.28
        tl = V3._wrap_lines(main, 78)
    head_h = (0.24 if kicker else 0.0) + len(tl) * tlead + 0.14
    for bsz, cpl, lead in ((1250, 96, 0.235), (1150, 105, 0.216), (1050, 115, 0.198)):
        h = 0.0; meas = []
        for head, lines in blocks:
            wr = []
            for l in lines:
                wr += V3._wrap_lines(l, cpl) or [""]
            bh = 0.26 + 0.02 + len(wr) * lead + 0.16
            meas.append((head, wr, bh, lead)); h += bh
        ph = max(2.1, 0.16 + head_h + 0.16 + h + 0.24)
        if ph <= AVAIL:
            break
    ph = min(ph, AVAIL)
    PY = PY_MIN if ph > AVAIL - 0.5 else 1.90
    add(box(200, "PopupPanel", PX, PY, PW, ph, "", fill="FFFFFF", ln=BLUE, dash=False, lnw=28575))
    ty = PY + 0.16
    if kicker:
        add(txt(202, "PopupKicker", PX + 0.28, ty, TW, 0.22, rt([kicker]), sz=1100, b=True, clr=GOLD))
        ty += 0.24
    add(txt(201, "PopupTitle", PX + 0.28, ty, TW, len(tl) * tlead + 0.06,
            rt(tl), sz=tsz, b=True))
    add(close_icon(260, PX + PW - 0.70, PY + 0.18, 0.42))
    y = PY + 0.16 + head_h + 0.16
    i = 210
    for head, wr, bh, lead in meas:
        # A field head that merely repeats the popup title is noise, not structure.
        if head.strip().lower() != main.strip().lower():
            add(txt(i, "FHead", PX + 0.28, y, PW - 0.56, 0.24, [head], sz=950, b=True, clr=GOLD))
            top = y + 0.26
        else:
            top = y
        i += 1
        add(txt(i, "FBody", PX + 0.28, top, PW - 0.56, max(0.24, len(wr) * lead),
                rt(wr), sz=bsz)); i += 1
        y += bh


def _cards(add, items, labels, viewed, start=40, y0=None, n=None):
    pos, cw, chh = item_grid(len(labels))
    if y0 is not None:
        pos = [(x, y0 + (yy - pos[0][1])) for x, yy in pos]
    idx = start
    for (x, y), lab, iid in zip(pos, labels, items):
        v = iid in viewed
        parts = ital_parts(lab)
        it = any(p[1] for p in parts)
        add(card(idx, x, y, cw, chh, lab, ital=it, sz=1500, viewed=v)); idx += 1
        if v:
            add(tick(idx, x + cw - 0.46, y + 0.10, 0.34)); idx += 1
    return pos, cw, chh


# ============================ FAMILY STRATEGIES ============================
def render_family_s(M, page, rec, st, add, viewed):
    """FAMILY_S — Struktur Taman. group master -> main -> Contoh -> popup -> all-viewed."""
    role = rec["screen_role"]
    c = M.comps[rec["component_id"]]
    if role == "COMPONENT_MAIN_EXPLANATION":
        add(title_ph(c["name"]), titlebar(6, M.groups[c["group"]]["name"]))
        add(txt(20, "Head", BAND_X, 1.30, BAND_W, 0.46, rt([c["name"]]), sz=2000, b=True))
        add(bullets(22, "Body", BAND_X, 1.92, BAND_W, 3.4,
                    [(0, ital_parts(l)) for l in c["display"]], sz=1500, spc=600))
        _visual(add, 30, 5.55, V3._wrap_lines(c["visual"], 108))
        spoken = [c["vo"] + f" Mari lihat contoh bagi {c['name']} di halaman seterusnya."]
        return spoken, ["INTERAKSI:", "  Tiada interaksi kandungan. Kemajuan melalui shell LMS."]

    # example-selection screen (base / popup / all-viewed)
    items = M.items_of(rec["learner_screen_id"])
    labels = [M.rows[i["source_row_uid"]]["label"] for i in items]
    ids = [i["interaction_item_id"] for i in items]
    add(title_ph(f"Contoh {c['name']}"), titlebar(6, f"Contoh {c['name']}"))
    add(txt(25, "Instr", BAND_X, 1.32, BAND_W, 0.42,
            [rec["interaction_instruction"]], sz=1600, algn="ctr"))
    _cards(add, ids, labels, viewed)
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
        vis = r.get("visual") or (f"[Visual: Arahan visual untuk {r['label']} — "
                                  f"spesifikasi teks sahaja, modul ms {r['ms']}. Tidak dibenamkan.]")
        blocks.append(("ARAHAN VISUAL — TIDAK DIBENAMKAN", V3._wrap_lines(vis, 100)))
        _modal(add, M, st, r["label"], blocks)
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
        add(title_ph(c["name"]), titlebar(6, M.groups[c["group"]]["name"]))
        add(txt(20, "Head", BAND_X, 1.22, BAND_W, 0.44, rt([c["name"]]), sz=2000, b=True))
        add(txt(25, "Instr", BAND_X, 1.74, BAND_W, 0.40,
                [rec["interaction_instruction"]], sz=1500, algn="ctr"))
        _cards(add, ids, labels, viewed, y0=2.36)
        _visual(add, 30, 5.90, V3._wrap_lines(c["visual"], 108))
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
    add(title_ph(r["label"]), titlebar(6, c["name"]))
    add(txt(20, "ExHead", BAND_X, 1.22, BAND_W, 0.44, rt([r["label"]]), sz=2200, b=True))
    add(txt(25, "Instr", BAND_X, 1.76, BAND_W, 0.40,
            [rec["interaction_instruction"]], sz=1500, algn="ctr"))
    _cards(add, ids, labels, viewed, y0=2.34)
    if r.get("contoh"):
        add(txt(70, "ExContoh", BAND_X, 5.24, BAND_W, 0.40,
                rt([f"Contoh: {r['contoh']}"]), sz=1400, b=True))
    _visual(add, 30, 5.76, V3._wrap_lines(r.get("visual") or "", 108))
    _nav(add, st)
    spoken = []
    if st["screen_role"] == "STATE_POPUP":
        iid = st["interaction_item_ids"][0]
        it = M.item(iid)
        body = _spec_body(r, it["label"])
        _modal(add, M, st, f"{r['label']} — {it['label']}",
               [(it["label"], V3._wrap_lines(body, 96))])
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
    add(title_ph(c["name"]), titlebar(6, M.groups[c["group"]]["name"]))
    add(txt(20, "Head", BAND_X, 1.22, BAND_W, 0.44, rt([c["name"]]), sz=2000, b=True))
    add(txt(21, "Sub", BAND_X, 1.72, BAND_W, 0.36, rt([r["label"]]), sz=1400, b=True, clr=GOLD))
    add(txt(25, "Instr", BAND_X, 2.10, BAND_W, 0.40,
            [rec["interaction_instruction"]], sz=1500, algn="ctr"))
    _cards(add, ids, labels, viewed, y0=2.68)
    _visual(add, 30, 5.90, V3._wrap_lines(r.get("visual") or "", 108))
    _nav(add, st)
    spoken = []
    if st["screen_role"] == "STATE_POPUP":
        it = M.item(st["interaction_item_ids"][0])
        body = _spec_body(r, it.get("source_attested_label") or it["label"])
        _modal(add, M, st, f"{r['label']} — {it['label']}",
               [(it["label"], V3._wrap_lines(body, 96))])
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
        add(title_ph(C.S01["canvas_title"]), titlebar(6, C.S01["canvas_title"]))
        add(txt(20, "Course", BAND_X, 1.34, BAND_W, 0.40, [C.S01["canvas"][0]], sz=1500, b=True, clr=GOLD))
        add(txt(21, "PL", BAND_X, 1.86, BAND_W, 0.46, [C.S01["canvas"][1]], sz=1900, b=True))
        add(txt(22, "Topic", BAND_X, 2.38, BAND_W, 0.46, [C.S01["canvas"][2]], sz=1900, b=True))
        _visual(add, 30, 3.30, C.S01["visual"])
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
        add(title_ph(C.S02["canvas_title"]), titlebar(6, C.S02["canvas_title"]))
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
        add(title_ph(C.S03["canvas_title"]), titlebar(6, C.S03["canvas_title"]))
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
        add(title_ph(g["name"]), titlebar(6, g["name"]))
        add(txt(25, "Instr", BAND_X, 1.15, BAND_W, 0.40,
                ["Klik pada setiap struktur untuk penjelasan lanjut."], sz=1600, algn="ctr"))
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
        add(title_ph(g["name"]), titlebar(6, g["name"]))
        add(bullets(22, "Body", BAND_X, 1.34, BAND_W, 2.0,
                    [(0, ital_parts(l)) for l in V3._wrap_lines(g["vo"], 110)], sz=1300, spc=300))
        y = 3.70
        for k, c in enumerate(members):
            fam = M.family(c["id"])
            add(txt(80 + k * 2, "PerLbl", BAND_X, y, 6.4, 0.36, rt([c["name"]]), sz=1600, b=True))
            add(txt(81 + k * 2, "PerFam", BAND_X + 6.6, y + 0.03, 5.0, 0.32, [fam], sz=1100, clr=GREY))
            y += 0.52
        _nav(add, st)
        spoken = [g["vo"], "Mari lihat setiap contoh perabot di halaman seterusnya."]
        extra = ["INTERAKSI:",
                 "  TIADA klik dan TIADA aras interaksi. Ini gerbang penerangan sahaja.",
                 "  Pelajar memasuki setiap komponen melalui navigasi shell.",
                 "AGIHAN KELUARGA:"]
        extra += [f"  {c['name']} -> {M.family(c['id'])}" for c in members]
        return spoken, extra

    # ---------------- Rumusan ----------------
    if sid == "SCR_RUMUSAN":
        add(title_ph(C.RUMUSAN["canvas_title"]), titlebar(6, C.RUMUSAN["canvas_title"]))
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
        add(title_ph("Tamat"), titlebar(6, "Tamat"))
        add(txt(20, "Course", BAND_X, 1.36, BAND_W, 0.38, [C.TAMAT["canvas"][0]], sz=1400, b=True, clr=GOLD))
        add(txt(21, "PL", BAND_X, 1.84, BAND_W, 0.42, [C.TAMAT["canvas"][1]], sz=1600, b=True))
        add(txt(22, "Head", BAND_X, 2.52, BAND_W, 0.60, rt(V3._wrap_lines(C.TAMAT["canvas_title"], 60)),
                sz=2400, b=True))
        add(txt(23, "Status", BAND_X, 3.50, BAND_W, 0.42, [C.TAMAT["status"]], sz=1600))
        add(txt(24, "Instr", BAND_X, 4.10, BAND_W, 0.42, [C.TAMAT["instruction"]], sz=1600, b=True))
        _nav(add, st)
        ex = rec["exit_model"]
        extra = ["KELUAR LMS:",
                 f"  destinasi logik: {ex['logical_destination']}",
                 f"  kelakuan keluar fizikal: {ex['physical_exit_behaviour']}",
                 f"  keadaan Seterusnya shell: {ex['shell_next_state']}",
                 f"  status: {ex['status']}",
                 "  " + ex["canvas_disclosure"]]
        return [C.TAMAT["vo"]], extra

    raise KeyError(f"no frame strategy for {sid}")


def _render_quiz(M, page, rec, st, add):
    role = st["screen_role"]
    q = rec["quiz_spec"]
    if role == "STATE_QUIZ_INTRO":
        add(title_ph("Kuiz"), titlebar(6, C.KUIZ_INTRO["canvas_title"]))
        add(txt(20, "Strap", BAND_X, 1.26, BAND_W, 0.36, [C.KUIZ_INTRO["strap"]], sz=1300, clr=GOLD))
        y = 1.86
        for k, l in enumerate(C.KUIZ_INTRO["purpose"]):
            w = V3._wrap_lines(l, 92)
            add(txt(30 + k, "Purpose", BAND_X, y, BAND_W, 0.32 * len(w) + 0.08, w, sz=1500))
            y += 0.32 * len(w) + 0.24
        y += 0.20
        for k, l in enumerate(C.KUIZ_INTRO["instruction"]):
            add(txt(40 + k, "Instr", BAND_X, y, BAND_W, 0.40, [l], sz=1600, b=(k == 1)))
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
        d = C.Q1 if n == 1 else C.Q5
        add(title_ph(f"Kuiz — Soalan {n}"), titlebar(6, f"Soalan {n}"))
        add(txt(20, "Kind", BAND_X, 1.26, BAND_W, 0.32,
                [f"{d['kind'].replace('_',' ')}   ·   sumber: {d['src']}"], sz=1150, clr=GREY))
        w = V3._wrap_lines(d["stem"], 92)
        add(txt(22, "Stem", BAND_X, 1.66, BAND_W, 0.34 * len(w) + 0.10, rt(w), sz=1600, b=True))
        y = 1.66 + 0.34 * len(w) + 0.36
        if d["kind"] == "MCQ":
            for k, (lab, opt) in enumerate(d["options"]):
                add(txt(40 + k, "Opt", BAND_X + 0.30, y, BAND_W - 0.6, 0.40,
                        rt([f"{lab}.  {opt}"]), sz=1500))
                y += 0.46
        else:
            for k, opt in enumerate(d["options"]):     # no A/B/C labels
                add(txt(40 + k, "Opt", BAND_X + 0.30, y, BAND_W - 0.6, 0.36, rt([opt]), sz=1450))
                y += 0.40
        fb = C.FEEDBACK
        add(txt(70, "FbC", BAND_X, 6.30, 5.6, 0.32, [fb["correct"]["text"]], sz=1300, clr=GREEN))
        add(txt(71, "FbW", BAND_X + 6.0, 6.30, 5.6, 0.32, [fb["incorrect"]["text"]], sz=1300, clr="C0392B"))
        _nav(add, st)
        spoken = [d["stem"]]
        if d["kind"] == "MCQ":
            spoken += [f"{lab}. {opt}" for lab, opt in d["options"]]
        else:
            spoken += list(d["options"])
        spoken += [f"Maklum balas betul: {fb['correct']['text']}",
                   f"Maklum balas salah: {fb['incorrect']['text']}"]
        extra = ["MAKLUM BALAS SERTA-MERTA:",
                 f"  betul: teks \"{fb['correct']['text']}\" · SFX {fb['correct']['sfx']} · VO sama",
                 f"  salah: teks \"{fb['incorrect']['text']}\" · SFX {fb['incorrect']['sfx']} · VO sama",
                 "JAWAPAN (metadata sahaja, tidak dilihat pelajar):",
                 "  " + (d["answer"] if d["kind"] == "MCQ" else ", ".join(d["answers"])),
                 "RASIONAL TERPERINCI (metadata sahaja):"]
        extra += ["  " + l for l in V3._wrap_lines(d["rationale"], 66)]
        extra += [f"  status: {st['unresolved_status']}"] if st.get("unresolved_status") != "NONE" else []
        if d["kind"] == "MULTIPLE_RESPONSE":
            extra += ["LABEL PILIHAN:", "  TIADA label A/B/C. Teks pilihan dipaparkan terus."]
        return spoken, extra

    # result
    d = C.RESULT
    add(title_ph("Kuiz — Keputusan"), titlebar(6, d["canvas_title"]))
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
    viewed = ADAPT.viewed_items(M, page, pages)
    page["completed_components"] = ADAPT.completed_components(M, page, pages)
    fam = st["execution_family"]
    # Component screens dispatch on the model-assigned execution family. Group masters,
    # gateways and frames are not component screens and never reach a family strategy.
    if fam in FAMILY_STRATEGY and rec.get("component_id"):
        spoken, extra = FAMILY_STRATEGY[fam](M, page, rec, st, add, viewed)
    else:
        spoken, extra = render_frame(M, page, rec, st, add, viewed)
    notes = build_notes(M, rec, st, spoken or [])
    lines = model_lines(M, rec, st, extra)
    lines.insert(0, f"BUKTI: {page['proof_note']}")
    sh.append(prodpanel_v4(9, page, rec, st, lines))
    return sh, notes


# ============================ package ============================
DONOR = os.path.join(GEN, "donor_skeleton")


def generate(outdir, outname=OUTNAME):
    M = ADAPT.Model()
    pages = ADAPT.proof_pages(M)
    work = os.path.join(outdir, "_build_v0_4")
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
        shapes, notes = build_page(M, page, pages)
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
        if not body:
            body = '<a:p><a:endParaRPr lang="en-MY" dirty="0"/></a:p>'
        wr(f"ppt/notesSlides/notesSlide{i}.xml", NOTE_DONOR[:m.start(2)] + body + NOTE_DONOR[m.end(2):])
        wr(f"ppt/notesSlides/_rels/notesSlide{i}.xml.rels", NRELS.replace("{n}", str(i)))
        manifest.append(dict(slide=i, page=page["id"], screen=page["screen_id"],
                             state=page["state_id"], role=page["review_page_role"],
                             family=page["execution_family"], notes_chars=len(notes)))
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


if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "."
    out, man = generate(outdir)
    print("wrote", out, "pages", len(man))
