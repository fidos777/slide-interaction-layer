# -*- coding: utf-8 -*-
"""Structural QA for the v0.4 three-family proof.

Every assertion is made against parsed model records or the parsed PPTX package.
No gate is decided by a whole-document text search.
"""
import json, os, re, sys, zipfile, collections
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import b02_model_adapter_v0_4 as ADAPT
import b02_proof_content_v0_4 as C

A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P = "{http://schemas.openxmlformats.org/presentationml/2006/main}"


def read_pptx(path):
    """Slides parsed into shapes, with the off-canvas production panel separated."""
    z = zipfile.ZipFile(path)
    n = len([x for x in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", x)])
    out = []
    for i in range(1, n + 1):
        root = ET.fromstring(z.read(f"ppt/slides/slide{i}.xml"))
        notes = ""
        try:
            nroot = ET.fromstring(z.read(f"ppt/notesSlides/notesSlide{i}.xml"))
            body = [sp for sp in nroot.iter(f"{P}sp")
                    if (sp.find(f".//{P}ph") is not None
                        and sp.find(f".//{P}ph").get("type") == "body")]
            if body:
                notes = "\n".join("".join(t.text or "" for t in p.iter(f"{A}t"))
                                  for p in body[0].iter(f"{A}p"))
        except KeyError:
            pass
        shapes = []
        for sp in root.iter(f"{P}sp"):
            nm = sp.find(f".//{P}cNvPr")
            name = nm.get("name") if nm is not None else ""
            off = sp.find(f".//{A}off"); ext = sp.find(f".//{A}ext")
            x = int(off.get("x")) / 914400.0 if off is not None else 0.0
            y = int(off.get("y")) / 914400.0 if off is not None else 0.0
            w = int(ext.get("cx")) / 914400.0 if ext is not None else 0.0
            h = int(ext.get("cy")) / 914400.0 if ext is not None else 0.0
            runs = [(t.text or "") for t in sp.iter(f"{A}t")]
            ital = [r.get("i") == "1" for r in sp.iter(f"{A}rPr")]
            geom = "custGeom" if sp.find(f".//{A}custGeom") is not None else (
                sp.find(f".//{A}prstGeom").get("prst") if sp.find(f".//{A}prstGeom") is not None else "")
            # Placeholder identity, read from the package. Stage 4.2E-C: the registered
            # off-stage geometry exemption keys on the real <p:ph type="..."/> element, so a
            # shape merely renamed "Title 1" cannot inherit the exemption.
            ph = sp.find(f".//{P}ph")
            shapes.append(dict(name=name, x=x, y=y, w=w, h=h, text="".join(runs),
                               runs=runs, italics=ital, geom=geom,
                               is_placeholder=ph is not None,
                               ph_type=(ph.get("type") if ph is not None else None),
                               offcanvas=(x + w) <= 0.001))
        out.append(dict(slide=i, shapes=shapes, notes=notes,
                        canvas=[s for s in shapes if not s["offcanvas"]],
                        panel=[s for s in shapes if s["offcanvas"]]))
    return out


def run(pptx):
    M = ADAPT.Model()
    pages = ADAPT.proof_pages(M)
    deck = read_pptx(pptx)
    res = []
    def chk(k, v, e):
        res.append((k, v, e, v == e))

    by_page = {p["id"]: (p, d) for p, d in zip(pages, deck)}
    st_of = {p["id"]: M.state(p["state_id"]) for p in pages}
    rec_of = {p["id"]: M.screen(p["screen_id"]) for p in pages}
    canvas_text = {pid: " ".join(s["text"] for s in d["canvas"]) for pid, (p, d) in by_page.items()}

    # ---------------- source and model ----------------
    chk("SOURCE_ROW_COUNT_REMAINS", len(M.source["rows"]), 26)
    chk("SOURCE_ASSET_COUNT_REMAINS", len(M.assets), 14)
    chk("PROOF_SOURCE_ROWS_CREATED",
        len({i["source_row_uid"] for i in M.map["interaction_items"]} - {r["uid"] for r in M.source["rows"]}), 0)
    chk("PROOF_INTERACTION_ITEMS_WITHOUT_SOURCE_BINDING",
        sum(1 for p in pages for iid in st_of[p["id"]]["interaction_item_ids"]
            if not M.item(iid).get("source_row_uid")), 0)
    chk("PROOF_STATES_WITHOUT_PARENT",
        sum(1 for p in pages if not st_of[p["id"]]["parent_screen_id"]), 0)
    chk("PROOF_RETURN_TARGET_MISSING",
        sum(1 for p in pages if st_of[p["id"]]["screen_role"] == "STATE_POPUP"
            and not st_of[p["id"]]["return_target"]), 0)

    # ---------------- FAMILY S ----------------
    S = [p for p in pages if p["execution_family"] == "FAMILY_S" and p.get("component_id")]
    chk("FAMILY_S_PROOF_COMPONENT", {p["component_id"] for p in S}, {"STRUKTUR_PERSISIR_AIR"})
    ex_screen = "SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES"
    chk("FAMILY_S_EXAMPLES", len(M.items_of(ex_screen)), 5)
    spops = [p for p in S if st_of[p["id"]]["screen_role"] == "STATE_POPUP"]
    chk("FAMILY_S_POPUPS", len(spops), 5)
    chk("FAMILY_S_TEXT_TUTUP_BUTTONS",
        sum(1 for p in spops for s in by_page[p["id"]][1]["canvas"]
            if s["name"] == "Btn" and "Tutup" in s["text"]), 0)
    chk("FAMILY_S_CLOSE_ICONS",
        sum(1 for p in spops if any(s["name"] == "CloseIcon" for s in by_page[p["id"]][1]["canvas"])), 5)
    chk("FAMILY_S_KEMBALI_TARGET",
        {st_of[p["id"]]["return_target"] for p in S
         if st_of[p["id"]]["back_control_type"] == "KEMBALI_BUTTON"}, {"SCR_GM_STRUKTUR"})
    # a Kembali drawn as ENABLED before every item is viewed would be premature
    prem = 0
    for p in S:
        st = st_of[p["id"]]
        if st["back_control_type"] != "KEMBALI_BUTTON":
            continue
        btns = [s for s in by_page[p["id"]][1]["canvas"] if s["name"] == "Btn" and "Kembali" in s["text"]]
        enabled_expected = st["screen_role"] == "STATE_ALL_VIEWED"
        for b in btns:
            drawn_enabled = "1F4E79" in _fill_of(pptx, p, b)
            if drawn_enabled and not enabled_expected:
                prem += 1
    chk("FAMILY_S_PREMATURE_KEMBALI", prem, 0)

    # ---------------- FAMILY P1 ----------------
    P1 = [p for p in pages if p["execution_family"] == "FAMILY_P1"]
    chk("FAMILY_P1_PROOF_COMPONENT", {p["component_id"] for p in P1}, {"KERUSI_TAMAN"})
    det = "SCR_KERUSI_TAMAN_EX01_DETAIL"
    chk("FAMILY_P1_EXAMPLE_DETAIL_PRESENT",
        any(p["screen_id"] == det for p in P1), True)
    p1specs = [p for p in P1 if st_of[p["id"]]["screen_role"] == "STATE_POPUP"]
    chk("FAMILY_P1_SPEC_ITEMS_PRESENT>=1", len(p1specs) >= 1, True)
    chk("FAMILY_P1_POPUP_PARENT_IS_EXAMPLE_DETAIL",
        all(st_of[p["id"]]["parent_screen_id"] == det for p in p1specs), True)
    chk("FAMILY_P1_POPUP_RETURN_TARGET_IS_EXAMPLE_DETAIL",
        all(st_of[p["id"]]["return_target"] == det for p in p1specs), True)
    chk("FAMILY_P1_KEMBALI_TARGET_IS_COMPONENT_OVERVIEW",
        {st_of[p["id"]]["return_target"] for p in P1
         if st_of[p["id"]]["back_control_type"] == "KEMBALI_BUTTON"}, {"SCR_KERUSI_TAMAN_MAIN"})
    chk("FAMILY_P1_SOURCE_ROWS_CREATED_BY_SPLIT",
        len({M.item(i)["source_row_uid"] for i in
             [x["interaction_item_id"] for x in M.items_of(det)]}) - 1, 0)
    chk("FAMILY_P1_WPC_NORMALISATION",
        "WPC (Wood-Plastic Composite / Plastik Kitar Semula)" in
        (M.rows["K5-PL06-T03-B02-KERUSI-TAMAN-ROW-03"].get("contoh") or "")
        or "Wood-Plastic Composite" in (M.rows["K5-PL06-T03-B02-KERUSI-TAMAN-ROW-03"].get("contoh") or ""), True)

    # ---------------- FAMILY P2 ----------------
    P2 = [p for p in pages if p["execution_family"] == "FAMILY_P2"]
    chk("FAMILY_P2_PROOF_COMPONENT", {p["component_id"] for p in P2}, {"PAPAN_TANDA"})
    cats = M.items_of("SCR_PAPAN_TANDA_MAIN")
    chk("FAMILY_P2_CATEGORIES", len(cats), 4)
    p2pops = [p for p in P2 if st_of[p["id"]]["screen_role"] == "STATE_POPUP"]
    chk("FAMILY_P2_POPUPS", len(p2pops), 4)
    chk("FAMILY_P2_GENERIC_ONE_ITEM_CONTOH_SCREEN",
        sum(1 for s in M.map["screens"] if s["execution_family"] == "FAMILY_P2"
            and "EXAMPLE" in s["screen_role"]), 0)
    chk("FAMILY_P2_SOURCE_ROWS_CREATED_BY_SPLIT",
        len({c["source_row_uid"] for c in cats}) - 1, 0)
    chk("FAMILY_P2_POPUP_RETURN_TARGET_IS_SPEC_LIST",
        all(st_of[p["id"]]["return_target"] == "SCR_PAPAN_TANDA_MAIN" for p in p2pops), True)
    chk("FAMILY_P2_CATEGORY_LOCATORS_RETAINED",
        all(M.rows[c["source_row_uid"]]["uid"] in c["content_source_locator"]
            or "modul ms" in c["content_source_locator"] for c in cats), True)

    # ---------------- frame screens ----------------
    chk("S01_NOTES_POLICY", st_of["PP-01"]["notes_policy"], "SPOKEN_ENTRY_TITLES_PLUS_ORIENTATION")
    el = st_of["PP-01"]["spoken_transcript_elements"]
    chk("S01_SPOKEN_ELEMENTS", len(el), 4)
    n1 = by_page["PP-01"][1]["notes"]
    chk("S01_PL06_TITLE_SPOKEN", "Pakej Latihan 06" in n1, True)
    chk("S01_TOPIC_TITLE_SPOKEN", "Topik 3 Bahagian 2" in n1, True)
    chk("S01_ORIENTATION_SPOKEN", "Dalam bahagian ini" in n1, True)
    chk("S01_MULA_INSTRUCTION_SPOKEN", "Klik Mula" in n1, True)
    chk("S01_COURSE_INTRO_REPEATED", any(k in n1 for k in ("lapan Pakej Latihan", "eight Pakej")), False)
    chk("S01_PL06_OBJECTIVES_REPEATED", "objektif" in n1.lower(), False)
    chk("S01_TOPIC_LIST_REPEATED", "tujuh topik" in n1.lower(), False)
    chk("S01_COURSE_TITLE_NOT_SPOKEN", "KURSUS KERJA BANGUNAN" in n1, False)
    chk("S01_COURSE_TITLE_ON_CANVAS", "KURSUS KERJA BANGUNAN" in canvas_text["PP-01"], True)
    chk("S01_MULA_BUTTON", any(s["name"] == "Btn" and s["text"] == "MULA"
                               for s in by_page["PP-01"][1]["canvas"]), True)

    n2 = by_page["PP-02"][1]["notes"]
    chk("S02_CAST", sorted(c["character_name"] for c in rec_of["PP-02"]["characters"]),
        ["Alya", "Encik Rahman"])
    chk("S02_CAST_IN_TRANSCRIPT", ("Alya:" in n2 and "Encik Rahman:" in n2), True)
    chk("S02_MS2680_LEARNER_CLAIMS",
        ("MS2680" in n2) + ("MS2680" in canvas_text["PP-02"]), 0)
    chk("S02_GENERIC_ROLE_NAMES_AS_FINAL_NAMES",
        sum(1 for k in ("Pelatih:", "Penyelia Tapak:", "[Pelatih]", "[Penyelia Tapak]") if k in n2), 0)
    chk("S02_MS2680_IN_PRODUCTION_PANEL",
        any("MS2680" in s["text"] for s in by_page["PP-02"][1]["panel"]), True)

    n3 = by_page["PP-03"][1]["notes"]
    chk("S03_NARRATOR", [c["character_name"] for c in rec_of["PP-03"]["characters"]], ["Hilmi"])
    chk("S03_HILMI_REINTRODUCED_AS_NEW",
        any(k in n3 for k in ("Hai, saya Hilmi", "Saya Hilmi", "saya Hilmi")), False)
    chk("S03_HILMI_SPEAKER_LABEL", "Hilmi:" in n3, True)
    chk("S03_MIND_MAP_DIRECTION_PRESENT", "Mind Map" in canvas_text["PP-03"], True)
    chk("HILMI_LABEL_ON_S03_ONLY",
        sum(1 for pid, t in canvas_text.items() if pid != "PP-03" and "Hilmi" in t), 0)

    qz = [p for p in pages if p["screen_id"] == "SCR_KUIZ"]
    intro = [p for p in qz if st_of[p["id"]]["screen_role"] == "STATE_QUIZ_INTRO"][0]
    chk("QUIZ_MULA_KUIZ_PRESENT",
        any(s["name"] == "Btn" and "MULA KUIZ" in s["text"]
            for s in by_page[intro["id"]][1]["canvas"]), True)
    mr = [p for p in qz if st_of[p["id"]].get("question_kind") == "MULTIPLE_RESPONSE"][0]
    opts = [s["text"] for s in by_page[mr["id"]][1]["canvas"] if s["name"] == "Opt"]
    chk("QUIZ_MULTIPLE_RESPONSE_LETTER_LABELS",
        sum(1 for o in opts if re.match(r"^[A-D]\.", o.strip())), 0)
    chk("QUIZ_MULTIPLE_RESPONSE_OPTIONS", len(opts), 7)
    chk("QUIZ_IMMEDIATE_FEEDBACK_VARIANTS", len(C.FEEDBACK), 2)
    for p in qz:
        if st_of[p["id"]]["screen_role"] != "STATE_QUIZ_QUESTION":
            continue
        d = C.Q1 if st_of[p["id"]]["runtime_state_id"].endswith("1") else C.Q5
        chk(f"QUIZ_FEEDBACK_ON_CANVAS_{d['n']}",
            (C.FEEDBACK["correct"]["text"] in canvas_text[p["id"]]
             and C.FEEDBACK["incorrect"]["text"] in canvas_text[p["id"]]), True)
        chk(f"QUIZ_RATIONALE_LEARNER_FACING_{d['n']}",
            d["rationale"][:40] in canvas_text[p["id"]] or d["rationale"][:40] in by_page[p["id"]][1]["notes"],
            False)
        chk(f"QUIZ_RATIONALE_IN_PANEL_{d['n']}",
            any(d["rationale"][:30] in " ".join(s["text"] for s in by_page[p["id"]][1]["panel"])
                for _ in [0]), True)
    res_p = [p for p in qz if st_of[p["id"]]["screen_role"] == "STATE_QUIZ_RESULT"][0]
    rt_ = canvas_text[res_p["id"]]
    chk("QUIZ_RESULT_SCORE", "Markah" in rt_, True)
    chk("QUIZ_RESULT_VERDICT", "Lulus" in rt_, True)
    chk("QUIZ_RESULT_CONTROLS",
        all(c in rt_ for c in ("Semak Jawapan", "Ulang Kuiz")), True)

    tm = by_page["PP-34"]
    # Superseded by Bariah's reviewed Tamat exemplar, 1 August 2026: the copy is confirmed,
    # the physical navigation mechanism is not, and no claim is made about the shell control.
    chk("TAMAT_PHYSICAL_NAVIGATION_STATUS",
        rec_of["PP-34"]["exit_model"]["physical_navigation_behaviour"],
        "PENDING_FIRDAUS_OR_LMS_CONFIRMATION")
    chk("TAMAT_NO_CUSTOM_NEXT_BUTTON",
        sum(1 for s in tm[1]["canvas"] if s["name"] == "Btn"), 0)
    chk("TAMAT_COPY_STATUS", rec_of["PP-34"]["exit_model"]["copy_status"], "CONFIRMED_BARIAH")
    chk("TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT",
        any(k in canvas_text["PP-34"] for k in ("Tutup tetingkap", "Tutup lesson")), False)
    chk("TAMAT_LOGICAL_DESTINATION",
        rec_of["PP-34"]["exit_model"]["logical_destination"], "NEXT_BAHAGIAN")

    # ---------------- notes ----------------
    need = [p for p in pages if st_of[p["id"]]["notes_policy"] != "SILENT_STATE_NOTES"]
    chk("CONTENT_SLIDES_WITHOUT_REQUIRED_NOTES_POLICY",
        sum(1 for p in need if not by_page[p["id"]][1]["notes"].strip()), 0)
    later = [p for p in pages if p["id"] != "PP-01"]
    # The ruling forbids repeating the ENTRY TITLES after S01. Two distinct assertions:
    #  (1) the PL title is absolute — it is never spoken again anywhere;
    #  (2) the Topic/Bahagian title must not appear as a standalone entry announcement.
    # A completion sentence that names the Bahagian ("Tamat Topik 3 Bahagian 2: ...") is a
    # different construction and is attested by Bariah's own corrected Tamat exemplar, so
    # it is not an entry-title repetition. Checking for the bare substring would have
    # rejected Bariah's own approved wording.
    chk("S02_ONWARDS_PL_TITLE_IN_SPOKEN_TRANSCRIPT",
        sum(1 for p in later
            if re.search(r"PL06: Pengurusan Operasi Pembinaan Landskap",
                         _spoken_block(by_page[p["id"]][1]["notes"]))), 0)
    def _announces(block):
        for ln in [l.strip() for l in block.splitlines() if l.strip()]:
            if ln.startswith("Topik 3 Bahagian 2") or ln == C.TOPIC:
                return True
        return False
    chk("S02_ONWARDS_TOPIC_TITLE_ANNOUNCED_AS_ENTRY",
        sum(1 for p in later if _announces(_spoken_block(by_page[p["id"]][1]["notes"]))), 0)
    chk("S02_ONWARDS_CONTEXT_BLOCK_PRESENT",
        sum(1 for p in later if st_of[p["id"]]["notes_policy"] != "SILENT_STATE_NOTES"
            and "NON-SPOKEN CONTEXT" not in by_page[p["id"]][1]["notes"]), 0)
    silent = [p for p in pages if st_of[p["id"]]["notes_policy"] == "SILENT_STATE_NOTES"]
    chk("SILENT_STATES_WITH_NONEMPTY_NOTES",
        sum(1 for p in silent if by_page[p["id"]][1]["notes"].strip()), 0)
    BAD = ("VO PENUH:", "PERINCIAN", "RP-", "ST_", "SCR_", "II_", "PENDING_", "CLASS-")
    chk("TECHNICAL_IDS_IN_FINAL_NOTES",
        sum(1 for p in pages for b in BAD if b in by_page[p["id"]][1]["notes"]), 0)

    # ---------------- controls ----------------
    shell = [p for p in pages if st_of[p["id"]]["next_control_type"] == "LMS_SHELL_NEXT"]
    chk("DUPLICATE_CUSTOM_SETERUSNYA_WHEN_SHELL_NEXT",
        sum(1 for p in shell for s in by_page[p["id"]][1]["canvas"]
            if s["name"] == "Btn" and "Seterusnya" in s["text"]), 0)
    chk("TEXT_TUTUP_BUTTON",
        sum(1 for p in pages for s in by_page[p["id"]][1]["canvas"]
            if s["name"] == "Btn" and "Tutup" in s["text"]), 0)
    pop_states = {s["runtime_state_id"] for s in M.map["states"] if s["screen_role"] == "STATE_POPUP"}
    chk("POPUP_PARENT_IS_POPUP",
        sum(1 for p in pages if st_of[p["id"]]["screen_role"] == "STATE_POPUP"
            and (st_of[p["id"]]["parent_screen_id"] in pop_states
                 or st_of[p["id"]]["return_target"] in pop_states)), 0)
    chk("UNKNOWN_CONTROL_TYPE",
        sum(1 for p in pages for k in ("next_control_type", "back_control_type", "close_control_type")
            if st_of[p["id"]][k] not in M.control_types), 0)
    chk("CLOSE_ICON_ON_EVERY_POPUP",
        sum(1 for p in pages if st_of[p["id"]]["screen_role"] == "STATE_POPUP"
            and not any(s["name"] == "CloseIcon" for s in by_page[p["id"]][1]["canvas"])), 0)

    # ---------------- rich text ----------------
    ital_ok = 0; ital_bad = 0
    for pid, (p, d) in by_page.items():
        for s in d["canvas"]:
            for r, i in zip(s["runs"], s["italics"] + [False] * len(s["runs"])):
                if r in C.ITALIC_TERMS and i: ital_ok += 1
                if r in C.ITALIC_TERMS and not i: ital_bad += 1
    chk("APPROVED_TERMS_NOT_ITALICISED", ital_bad, 0)
    chk("APPROVED_TERMS_ITALICISED>=4", ital_ok >= 4, True)
    chk("PRODUCTION_IDS_ITALICISED",
        sum(1 for pid, (p, d) in by_page.items() for s in d["canvas"]
            for r, i in zip(s["runs"], s["italics"] + [False] * len(s["runs"]))
            if i and any(r.startswith(x) for x in C.NEVER_ITALIC_PREFIXES)), 0)
    chk("BBQ_PIT_CAPITAL_P",
        sum(1 for t in canvas_text.values() if re.search(r"BBQ pit\b", t)), 0)

    # ---------------- off-canvas panels ----------------
    chk("PAGES_WITHOUT_PRODUCTION_PANEL",
        sum(1 for pid, (p, d) in by_page.items()
            if not any(s["name"] == "ProdPanel" for s in d["panel"])), 0)
    chk("PRODUCTION_PANEL_LEAKS_ONTO_CANVAS",
        sum(1 for pid, (p, d) in by_page.items()
            for s in d["canvas"] if s["name"] == "ProdPanel"), 0)
    REQ = ("FUNGSI SKRIN", "KELUARGA PELAKSANAAN", "POLISI NOTA", "KAWALAN",
           "SKOP SELESAI", "PERSISTEN", "STATUS BELUM SELESAI")
    chk("PRODUCTION_PANEL_MISSING_REQUIRED_FIELD",
        sum(1 for pid, (p, d) in by_page.items()
            for k in REQ
            if k not in " ".join(s["text"] for s in d["panel"])), 0)
    chk("PROOF_PAGES", len(pages), len(deck))
    return res


def _spoken_block(notes):
    if "SPOKEN TRANSCRIPT" not in notes:
        return ""
    return notes.split("SPOKEN TRANSCRIPT", 1)[1]


_FILLCACHE = {}
def _fill_of(pptx, page, shape):
    """Fill colour of a drawn button, read back from the package."""
    key = (pptx, page["id"])
    if key not in _FILLCACHE:
        z = zipfile.ZipFile(pptx)
        idx = int(page["id"].split("-")[1])
        _FILLCACHE[key] = z.read(f"ppt/slides/slide{idx}.xml").decode("utf-8")
    xml = _FILLCACHE[key]
    m = re.search(r'name="Btn".{0,900}?srgbClr val="([0-9A-F]{6})"', xml, re.S)
    return m.group(1) if m else ""


if __name__ == "__main__":
    rep = run(sys.argv[1])
    w = max(len(k) for k, _, _, _ in rep)
    fail = 0
    for k, v, e, ok in rep:
        if not ok: fail += 1
        print(f"{'PASS' if ok else 'FAIL'}  {k:<{w}}  {v!r}" + ("" if ok else f"   expected {e!r}"))
    print(f"\n{len(rep)-fail}/{len(rep)} PASS")
    sys.exit(1 if fail else 0)
