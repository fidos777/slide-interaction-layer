# -*- coding: utf-8 -*-
"""Full structural QA for the complete K5 PL06 T03 B02 v0.4 review deck.

Every assertion is made against parsed model records or the parsed PPTX package.
Ticks, control fills and off-canvas separation are read back out of the artifact, so a
gate cannot pass merely because the model was right.
"""
import json, os, re, sys, zipfile, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
import b02_model_adapter_v0_4 as ADAPT
import b02_proof_content_v0_4 as C
from b02_proof_qa_v0_4 import read_pptx, _spoken_block


def run(pptx):
    M = ADAPT.Model()
    pages = ADAPT.all_pages(M)
    deck = read_pptx(pptx)
    assert len(pages) == len(deck), (len(pages), len(deck))
    res = []
    def chk(k, v, e): res.append((k, v, e, v == e))

    idx = {p["id"]: k for k, p in enumerate(pages)}
    st_of = {p["id"]: M.state(p["state_id"]) for p in pages}
    rec_of = {p["id"]: M.screen(p["screen_id"]) for p in pages}
    D = {p["id"]: d for p, d in zip(pages, deck)}
    ctext = {pid: " ".join(s["text"] for s in d["canvas"]) for pid, d in D.items()}
    ptext = {pid: " ".join(s["text"] for s in d["panel"]) for pid, d in D.items()}
    # Panel paragraphs in order. The production panel writes one run per paragraph, so the
    # run list IS the line list — which is what lets the identity block be read back as
    # lines instead of being grepped out of one concatenated string.
    plines = {pid: [r for s in d["panel"] if s["name"] == "ProdPanel" for r in s["runs"]]
              for pid, d in D.items()}
    ticks = {pid: sum(1 for s in d["canvas"] if s["name"] == "Tick") for pid, d in D.items()}
    notes = {pid: d["notes"] for pid, d in D.items()}
    fam_of = {}
    for s in M.map["screens"]:
        if s.get("component_id"): fam_of[s["component_id"]] = s["execution_family"]

    # ============================ SOURCE QA ============================
    uids = [r["uid"] for r in M.source["rows"]]
    chk("SOURCE_ROWS_EXPECTED", len(uids), 26)
    bound = {u for st in M.map["states"] for u in st["source_row_uids"]}
    chk("SOURCE_ROWS_ACCOUNTED", len(bound & set(uids)), 26)
    chk("SOURCE_ROWS_CREATED", len({i["source_row_uid"] for i in M.map["interaction_items"]} - set(uids)), 0)
    chk("DUPLICATE_SOURCE_ROW_UID", len(uids) - len(set(uids)), 0)
    chk("SOURCE_ASSETS_EXPECTED", len(M.assets), 14)
    ab = {a for st in M.map["states"] for a in st["source_asset_ids"]}
    chk("SOURCE_ASSETS_ACCOUNTED", len(ab), 14)
    chk("ORPHAN_SOURCE_ASSETS", len({a["asset_id"] for a in M.assets} - ab), 0)
    chk("INTERACTION_ITEMS_WITHOUT_SOURCE_BINDING",
        sum(1 for i in M.map["interaction_items"] if not i.get("source_row_uid")), 0)
    chk("INTERACTION_ITEMS_WITHOUT_LOCATOR",
        sum(1 for i in M.map["interaction_items"] if not i.get("content_source_locator")), 0)
    chk("INTERACTION_ITEMS_WITHOUT_FAMILY",
        sum(1 for i in M.map["interaction_items"] if i.get("execution_family") not in
            ("FAMILY_S", "FAMILY_P1", "FAMILY_P2")), 0)
    chk("STATES_WITHOUT_DECISION_ID", sum(1 for st in M.map["states"] if not st["decision_ids"]), 0)
    # every source row must be visible on at least one rendered review page
    row_pages = collections.defaultdict(set)
    for p in pages:
        for u in st_of[p["id"]]["source_row_uids"]:
            row_pages[u].add(p["id"])
    chk("SOURCE_ROWS_WITHOUT_A_REVIEW_PAGE", sum(1 for u in uids if not row_pages[u]), 0)
    chk("SOURCE_ROW_LOCATOR_IN_PANEL",
        sum(1 for u in uids if not any(u in ptext[pid] for pid in row_pages[u])), 0)

    # ============================ FAMILY QA ============================
    fc = collections.Counter(fam_of.values())
    chk("FAMILY_S_COMPONENTS", fc["FAMILY_S"], 4)
    chk("FAMILY_P1_COMPONENTS", fc["FAMILY_P1"], 3)
    chk("FAMILY_P2_COMPONENTS", fc["FAMILY_P2"], 2)
    chk("UNKNOWN_COMPONENT_FAMILY",
        sum(1 for f in fam_of.values() if f not in ("FAMILY_S", "FAMILY_P1", "FAMILY_P2")), 0)
    chk("COMPONENTS_GENERATED", len({p["component_id"] for p in pages if p["component_id"]}), 9)
    chk("PAPAN_TANDA_SPEC_CATEGORIES", len(M.items_of("SCR_PAPAN_TANDA_MAIN")), 4)
    chk("BBQ_PIT_SPEC_CATEGORIES", len(M.items_of("SCR_BBQ_PIT_MAIN")), 4)
    chk("BBQ_PIT_CATEGORY_LABELS", [i["label"] for i in M.items_of("SCR_BBQ_PIT_MAIN")],
        ["Bahan Pembinaan", "Dimensi", "Gril", "Keselamatan"])
    chk("GENERIC_ONE_ITEM_PAPAN_TANDA_SCREEN",
        sum(1 for s in M.map["screens"] if s.get("component_id") == "PAPAN_TANDA"
            and "EXAMPLE" in s["screen_role"]), 0)
    chk("GENERIC_ONE_ITEM_BBQ_PIT_SCREEN",
        sum(1 for s in M.map["screens"] if s.get("component_id") == "BBQ_PIT"
            and "EXAMPLE" in s["screen_role"]), 0)
    for cid, n in (("PAPAN_TANDA", 4), ("BBQ_PIT", 4)):
        chk(f"{cid}_SOURCE_ROWS_CREATED_BY_SPLIT",
            len({i["source_row_uid"] for i in M.items_of(f"SCR_{cid}_MAIN")}) - 1, 0)
    # every card the deck draws must correspond to a model interaction item
    dropped = 0
    for p in pages:
        if st_of[p["id"]]["screen_role"] != "STATE_BASE": continue
        n_items = len(M.items_of(p["screen_id"]))
        if not n_items: continue
        n_cards = sum(1 for s in D[p["id"]]["canvas"] if s["name"] == "ItemCard")
        if n_cards != n_items: dropped += 1
    chk("CARDS_DROPPED_OR_INVENTED", dropped, 0)

    # ============================ STATE QA ============================
    sids = {s["learner_screen_id"] for s in M.map["screens"]}
    stids = {s["runtime_state_id"] for s in M.map["states"]}
    chk("RUNTIME_STATES_WITHOUT_PARENT",
        sum(1 for s in M.map["states"] if s["parent_screen_id"] not in sids), 0)
    chk("RETURN_TARGET_MISSING",
        sum(1 for s in M.map["states"] if s["screen_role"] == "STATE_POPUP" and not s["return_target"]), 0)
    pop = {s["runtime_state_id"] for s in M.map["states"] if s["screen_role"] == "STATE_POPUP"}
    chk("POPUP_PARENT_IS_POPUP",
        sum(1 for s in M.map["states"] if s["screen_role"] == "STATE_POPUP"
            and (s["parent_screen_id"] in pop or s["return_target"] in pop)), 0)
    chk("UNKNOWN_CONTROL_TYPE",
        sum(1 for s in M.map["states"] for k in
            ("next_control_type", "back_control_type", "close_control_type")
            if s[k] not in M.control_types), 0)
    chk("REVIEW_PAGES_EQUAL_RUNTIME_STATES", len(pages), len(M.map["states"]))

    # -------- completion topology, read from the rendered ticks --------
    prem_s = false_sib = prem_p1 = prem_p2 = 0
    for p in pages:
        st = st_of[p["id"]]; k = idx[p["id"]]
        seen_states = {q["state_id"] for q in pages[:k]}
        seen_done = {q["state_id"] for q in pages[:k]
                     if M.state(q["state_id"])["screen_role"] in
                     ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE")}
        items = M.items_of(p["screen_id"])
        fam = st["execution_family"]
        role = st["screen_role"]
        # expected ticks = items whose own state was reached earlier (or on this popup)
        exp = 0
        for it in items:
            rs = it["runtime_state_id"]
            if rs in seen_states or rs == st["runtime_state_id"]:
                exp += 1; continue
            m = re.match(r"^ST_(.+)_EX(\d+)_BASE$", rs)
            if m and f"ST_{m.group(1)}_EX{m.group(2)}_ALL_SPEC_VIEWED" in seen_done:
                exp += 1
        if role in ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE"):
            exp = len(items) if items else ticks[p["id"]]
        got = ticks[p["id"]]
        if fam == "FAMILY_P1" and rec_of[p["id"]]["screen_role"] == \
           "COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST" and got != exp:
            false_sib += 1
        # Exact-match, not "fewer than all": opening the LAST specification legitimately
        # ticks every item while the state is still a popup. What must never happen is a
        # tick count that does not equal what the path has actually completed.
        if fam == "FAMILY_P1" and rec_of[p["id"]]["screen_role"] == "EXAMPLE_DETAIL_FULL_SLIDE" \
           and got != exp:
            prem_p1 += 1
        if fam == "FAMILY_P2" and items and got != exp:
            prem_p2 += 1
        # Kembali drawn enabled before completion
        if st["back_control_type"] == "KEMBALI_BUTTON":
            enabled_expected = role == "STATE_ALL_VIEWED"
            xml = _slide_xml(pptx, k + 1)
            m2 = re.search(r'name="Btn".{0,1200}?srgbClr val="([0-9A-F]{6})"', xml, re.S)
            drawn_enabled = bool(m2 and m2.group(1) == "1F4E79")
            if drawn_enabled and not enabled_expected and fam == "FAMILY_S":
                prem_s += 1
    chk("FAMILY_S_PREMATURE_KEMBALI", prem_s, 0)
    chk("FAMILY_P1_FALSE_SIBLING_TICKS", false_sib, 0)
    chk("FAMILY_P1_PREMATURE_EXAMPLE_COMPLETION", prem_p1, 0)
    chk("FAMILY_P2_PREMATURE_COMPONENT_COMPLETION", prem_p2, 0)

    shell = [p for p in pages if st_of[p["id"]]["next_control_type"] == "LMS_SHELL_NEXT"]
    chk("DUPLICATE_CUSTOM_SETERUSNYA",
        sum(1 for p in shell for s in D[p["id"]]["canvas"]
            if s["name"] == "Btn" and "Seterusnya" in s["text"]), 0)
    chk("TEXT_TUTUP_BUTTON",
        sum(1 for p in pages for s in D[p["id"]]["canvas"]
            if s["name"] == "Btn" and "Tutup" in s["text"]), 0)
    chk("POPUPS_WITHOUT_CLOSE_ICON",
        sum(1 for p in pages if st_of[p["id"]]["screen_role"] == "STATE_POPUP"
            and not any(s["name"] == "CloseIcon" for s in D[p["id"]]["canvas"])), 0)
    # close icon must not collide with the popup title box
    coll = 0
    for p in pages:
        d = D[p["id"]]
        ic = [s for s in d["canvas"] if s["name"] == "CloseIcon"]
        ti = [s for s in d["canvas"] if s["name"] in ("PopupTitle", "PopupKicker")]
        for a in ic:
            for b in ti:
                if min(a["x"] + a["w"], b["x"] + b["w"]) - max(a["x"], b["x"]) > 0.01 and \
                   min(a["y"] + a["h"], b["y"] + b["h"]) - max(a["y"], b["y"]) > 0.01:
                    coll += 1
    chk("CLOSE_ICON_TITLE_COLLISIONS", coll, 0)

    # ============================ FRAME QA ============================
    s01 = [p for p in pages if p["screen_id"] == "SCR_S01"][0]["id"]
    # Stage 4.2C: the S01 Speaker Notes are re-cut against B02_BARIAH_S01_EVIDENCE.jpg. The
    # four superseded gate IDs are retained as SUPERSEDED markers so a reader can see the
    # ruling changed rather than finding the checks quietly absent. Each is replaced by a
    # gate of equal or greater strength, listed immediately after it.
    chk("S01_NOTES_POLICY__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT", "SUPERSEDED", "SUPERSEDED")
    chk("S01_NOTES_POLICY", st_of[s01]["notes_policy"],
        "SPOKEN_ENTRY_TITLES_PLUS_START_INSTRUCTION")
    chk("S01_SPOKEN_ELEMENTS__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT", "SUPERSEDED", "SUPERSEDED")
    chk("S01_SPOKEN_ELEMENTS", len(st_of[s01]["spoken_transcript_elements"]), 3)
    n1 = notes[s01]
    chk("S01_PL06_TITLE_SPOKEN__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT", "SUPERSEDED", "SUPERSEDED")
    chk("S01_PL06_TITLE_SPOKEN__SUPERSEDED_BY_D3_PUNCTUATION_RULING", "SUPERSEDED", "SUPERSEDED")
    chk("S01_PL06_TITLE_SPOKEN", "PL06: Pengurusan Operasi Pembinaan Landskap" in n1, True)
    chk("S01_PL06_TITLE_SPOKEN_WITH_TRAILING_PERIOD",
        "PL06: Pengurusan Operasi Pembinaan Landskap." in n1, False)
    chk("S01_PL06_TITLE_LONG_FORM_WITHDRAWN", "Pakej Latihan 06" in n1, False)
    chk("S01_TOPIC_TITLE_SPOKEN", "Topik 3 Bahagian 2" in n1, True)
    chk("S01_ORIENTATION_SPOKEN__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT", "SUPERSEDED", "SUPERSEDED")
    chk("S01_ORIENTATION_SENTENCE_REMOVED", "Dalam bahagian ini" in n1, False)
    chk("S01_MULA_INSTRUCTION_SPOKEN__SUPERSEDED_BY_LATEST_BARIAH_SCREENSHOT",
        "SUPERSEDED", "SUPERSEDED")
    chk("S01_MULA_INSTRUCTION_SPOKEN",
        "Klik butang “Mula” untuk memulakan pembelajaran." in n1, True)
    chk("S01_MULA_INSTRUCTION_OLD_WORDING_WITHDRAWN", "Klik Mula untuk meneruskan" in n1, False)
    chk("S01_TOPIC_LINE_ON_CANVAS",
        any(s["text"].strip() == "Topik 3 Bahagian 2: Komponen Landskap"
            for s in D[s01]["canvas"] if s["name"] == "Topic"), True)
    chk("S01_VISUAL_HEADING_ON_CANVAS",
        "ARAHAN VISUAL — SPESIFIKASI SAHAJA" in ctext[s01], True)
    chk("S01_COURSE_INTRO_REPEATED", any(k in n1 for k in ("lapan Pakej", "eight Pakej")), False)
    chk("S01_PL06_OBJECTIVES_REPEATED", "objektif" in n1.lower(), False)
    chk("S01_TOPIC_LIST_REPEATED", "tujuh topik" in n1.lower(), False)
    chk("S01_HILMI_REINTRODUCED", "Hilmi" in n1, False)
    chk("S01_COURSE_TITLE_NOT_SPOKEN", "KURSUS KERJA BANGUNAN" in n1, False)

    s02 = [p for p in pages if p["screen_id"] == "SCR_S02"][0]["id"]
    chk("S02_CAST", sorted(c["character_name"] for c in rec_of[s02]["characters"]),
        ["Alya", "Encik Rahman"])
    chk("S02_CAST_IN_TRANSCRIPT", "Alya:" in notes[s02] and "Encik Rahman:" in notes[s02], True)
    chk("S02_MS2680_LEARNER_CLAIMS", ("MS2680" in notes[s02]) + ("MS2680" in ctext[s02]), 0)
    chk("S02_MS2680_IN_PRODUCTION_PANEL", "MS2680" in ptext[s02], True)
    chk("S02_GENERIC_ROLE_NAMES_AS_FINAL_NAMES",
        sum(1 for k in ("Pelatih:", "Penyelia Tapak:", "[Pelatih]", "[Penyelia Tapak]")
            if k in notes[s02]), 0)

    s03 = [p for p in pages if p["screen_id"] == "SCR_S03"][0]["id"]
    chk("S03_NARRATOR", [c["character_name"] for c in rec_of[s03]["characters"]], ["Hilmi"])
    chk("S03_HILMI_REINTRODUCED_AS_NEW",
        any(k in notes[s03] for k in ("Hai, saya Hilmi", "saya Hilmi", "Saya Hilmi")), False)
    chk("S03_MIND_MAP_DIRECTION_PRESENT", "Mind Map" in ctext[s03], True)
    chk("S03_BOTH_GROUPS_PRESENT",
        ("Struktur Taman:" in ctext[s03] and "Perabot Taman:" in ctext[s03]), True)
    # A component name wrapped across two paragraphs concatenates without a space, so the
    # comparison is made on whitespace-stripped text. A genuinely absent name still fails.
    _s03 = re.sub(r"\s+", "", ctext[s03])
    chk("S03_ALL_NINE_COMPONENTS",
        sum(1 for c in M.source["components"] if re.sub(r"\s+", "", c["name"]) in _s03), 9)
    chk("HILMI_LABEL_OUTSIDE_S03",
        sum(1 for pid, t in ctext.items() if pid != s03 and "Hilmi" in t), 0)

    rum = [p for p in pages if p["screen_id"] == "SCR_RUMUSAN"][0]["id"]
    chk("RUMUSAN_FORBIDDEN_LABELS_DISPLAYED",
        sum(1 for l in rec_of[rum]["forbidden_labels"] if l in ctext[rum]), 0)

    qz = [p["id"] for p in pages if p["screen_id"] == "SCR_KUIZ"]
    qq = [p for p in qz if st_of[p]["screen_role"] == "STATE_QUIZ_QUESTION"]
    chk("QUIZ_ITEMS", len(qq), 5)
    chk("QUIZ_MCQ", sum(1 for p in qq if st_of[p]["question_kind"] == "MCQ"), 4)
    chk("QUIZ_MULTIPLE_RESPONSE",
        sum(1 for p in qq if st_of[p]["question_kind"] == "MULTIPLE_RESPONSE"), 1)
    mr = [p for p in qq if st_of[p]["question_kind"] == "MULTIPLE_RESPONSE"][0]
    chk("QUIZ_MR_LETTER_LABELS",
        sum(1 for s in D[mr]["canvas"] if s["name"] == "Opt"
            and re.match(r"^[A-D]\.", s["text"].strip())), 0)
    chk("QUIZ_IMMEDIATE_FEEDBACK_VARIANTS", len(C.FEEDBACK), 2)
    chk("QUIZ_QUESTIONS_WITHOUT_BOTH_FEEDBACK_VARIANTS",
        sum(1 for p in qq if not (C.FEEDBACK["correct"]["text"] in ctext[p]
                                  and C.FEEDBACK["incorrect"]["text"] in ctext[p])), 0)
    chk("QUIZ_DETAILED_RATIONALE_LEARNER_FACING",
        sum(1 for p in qq for q in C.QUESTIONS.values()
            if q["rationale"][:40] in ctext[p] or q["rationale"][:40] in notes[p]), 0)
    chk("QUIZ_RATIONALE_IN_PRODUCTION_PANEL",
        sum(1 for p in qq if not any(q["rationale"][:30] in ptext[p] for q in C.QUESTIONS.values())), 0)
    rs = [p for p in qz if st_of[p]["screen_role"] == "STATE_QUIZ_RESULT"][0]
    chk("QUIZ_RESULT_ELEMENTS",
        all(k in ctext[rs] for k in ("Markah", "Lulus", "Semak Jawapan", "Ulang Kuiz")), True)
    chk("QUIZ_REVIEW_STATE_PRESENT",
        sum(1 for p in qz if st_of[p]["screen_role"] == "STATE_QUIZ_REVIEW"), 1)

    tm = [p for p in pages if p["screen_id"] == "SCR_TAMAT"][0]["id"]
    # Bariah's reviewed Tamat exemplar (1 August 2026) supersedes the earlier provisional
    # close-the-window ruling. These five checks are the 1:1 replacements for the five that
    # encoded the superseded ruling; the count is unchanged and none was dropped.
    ex = rec_of[tm]["exit_model"]
    chk("TAMAT_COPY_STATUS", ex["copy_status"], "CONFIRMED_BARIAH")
    chk("TAMAT_LOGICAL_DESTINATION", ex["logical_destination"], "NEXT_BAHAGIAN")
    chk("TAMAT_PHYSICAL_NAVIGATION_STATUS", ex["physical_navigation_behaviour"],
        "PENDING_FIRDAUS_OR_LMS_CONFIRMATION")
    chk("TAMAT_CLOSE_WINDOW_INSTRUCTION_PRESENT",
        any(k in ctext[tm] for k in ("Tutup tetingkap", "Tutup lesson", "Tutup window",
                                     "Sila tutup halaman")), False)
    chk("TAMAT_UNVERIFIED_PHYSICAL_NAVIGATION_CLAIM",
        sum(1 for k in ("shell Next disabled", "Seterusnya shell DISABLED", "DISABLED")
            if k in ptext[tm]), 0)
    chk("TAMAT_NO_CANVAS_NEXT_BUTTON",
        sum(1 for s in D[tm]["canvas"] if s["name"] == "Btn"), 0)

    # ============================ NOTES QA ============================
    need = [p["id"] for p in pages if st_of[p["id"]]["notes_policy"] != "SILENT_STATE_NOTES"]
    chk("CONTENT_SLIDES_WITHOUT_NOTES", sum(1 for p in need if not notes[p].strip()), 0)
    later = [p["id"] for p in pages if p["id"] != s01]
    chk("S02_ONWARDS_PL_TITLE_REANNOUNCEMENTS",
        sum(1 for p in later
            if re.search(r"PL06: Pengurusan Operasi Pembinaan Landskap", _spoken_block(notes[p]))), 0)
    def announces(b):
        return any(l.strip().startswith("Topik 3 Bahagian 2") for l in b.splitlines() if l.strip())
    chk("S02_ONWARDS_TOPIC_TITLE_REANNOUNCEMENTS",
        sum(1 for p in later if announces(_spoken_block(notes[p]))), 0)
    chk("CONTEXT_BLOCK_MISSING_ON_CONTENT_SLIDES",
        sum(1 for p in later if st_of[p]["notes_policy"] != "SILENT_STATE_NOTES"
            and "NON-SPOKEN CONTEXT" not in notes[p]), 0)
    silent = [p["id"] for p in pages if st_of[p["id"]]["notes_policy"] == "SILENT_STATE_NOTES"]
    chk("SILENT_STATES_WITH_NONEMPTY_NOTES", sum(1 for p in silent if notes[p].strip()), 0)
    BAD = ("VO PENUH:", "PERINCIAN", "RP-", "ST_", "SCR_", "II_", "PENDING_", "CLASS-", "runtime_state")
    chk("TECHNICAL_IDS_IN_FINAL_NOTES",
        sum(1 for p in pages for b in BAD if b in notes[p["id"]]), 0)

    # ============================ CLEAN-DECK QA ============================
    MARKERS = ("Changes made", "Refer next slide", "Apply changes", "Bariah:",
               "New structure. Refer doc")
    chk("BARIAH_REVIEW_ANNOTATIONS_IN_DECK",
        sum(1 for pid in ctext for m in MARKERS if m in ctext[pid]), 0)
    chk("BARIAH_ANNOTATIONS_IN_NOTES",
        sum(1 for pid in notes for m in MARKERS if m in notes[pid]), 0)
    chk("V0_3_TOKENS_IN_PANEL",
        sum(1 for pid in ptext if "v0.3" in ptext[pid] or "PAPAN CERITA v0.3" in ptext[pid]), 0)
    # Stage 4.2E-C, defect B02-META-REG-001. The two gates that used to live here are the
    # reason four releases shipped stamped "v0.4" with the Stage 4 tokens: one forbade only
    # the literal "v0.3", and the other REQUIRED REVIEW_READY / BARIAH_FEEDBACK_IMPLEMENTED /
    # PENDING_TARGETED_CONFIRMATION to be present on every page. A suite that mandates the
    # stale value cannot report the drift. Both are now driven by the controlled identity
    # source, and the panel's token set is compared for EQUALITY, not for presence.
    import b02_artifact_identity_v0_4_4_1 as IDENT
    ident = {pid: IDENT.panel_identity_from_text(plines[pid]) for pid in plines}
    chk("PANEL_VERSION_LINES_READ", sum(1 for pid in ident if ident[pid][0]), len(ptext))
    chk("ACTIVE_PANEL_VERSION",
        sorted({(v or "").replace("K5 PL06 T03 B02 — PAPAN CERITA ", "")
                for v, _ in ident.values()}), [IDENT.VERSION])
    chk("PANEL_VERSION_MISMATCHES",
        sum(1 for v, _ in ident.values() if v != IDENT.VERSION_LINE), 0)
    # Exact line equality, not substring: "…PAPAN CERITA v0.4" is a prefix of
    # "…PAPAN CERITA v0.4.4.1", so a substring test would report the active version as stale.
    chk("SUPERSEDED_VERSION_LINES_IN_PANEL",
        sum(1 for v, _ in ident.values() if v in IDENT.SUPERSEDED_VERSION_LINES), 0)
    chk("PANEL_STATUS_TOKEN_SET_MISMATCHES",
        sum(1 for _, t in ident.values() if t != IDENT.STATUS_TOKENS), 0)
    for tok in IDENT.STATUS_TOKENS:
        chk(f"PACKAGE_TOKEN_{tok}", all(tok in t for _, t in ident.values()), True)
    for tok in IDENT.STALE_STATUS_TOKENS:
        chk(f"STALE_STATUS_TOKEN_{tok}", sum(1 for _, t in ident.values() if tok in t), 0)
    chk("STALE_RELEASE_TOKENS",
        sum(1 for _, t in ident.values() for tok in IDENT.STALE_STATUS_TOKENS if tok in t), 0)
    for tok in IDENT.FORBIDDEN_STATUS_TOKENS:
        chk(f"FORBIDDEN_STATUS_TOKEN_{tok}", sum(1 for _, t in ident.values() if tok in t), 0)
    for tok in IDENT.FORBIDDEN_CLAIM_STRINGS:
        chk(f"FORBIDDEN_TOKEN_{tok}", sum(1 for pid in ptext if tok in ptext[pid]), 0)

    # ============================ RICH TEXT ============================
    bad_i = ok_i = 0
    for pid, d in D.items():
        for s in d["canvas"]:
            for r, i in zip(s["runs"], s["italics"] + [False] * len(s["runs"])):
                if r in C.ITALIC_TERMS:
                    ok_i += 1 if i else 0
                    bad_i += 0 if i else 1
    chk("APPROVED_TERMS_NOT_ITALICISED", bad_i, 0)
    chk("APPROVED_TERMS_ITALICISED_AT_LEAST", ok_i >= 10, True)
    chk("PRODUCTION_IDS_ITALICISED",
        sum(1 for pid, d in D.items() for s in d["canvas"]
            for r, i in zip(s["runs"], s["italics"] + [False] * len(s["runs"]))
            if i and any(r.startswith(x) for x in C.NEVER_ITALIC_PREFIXES)), 0)
    chk("BBQ_PIT_LOWERCASE_P_ON_CANVAS", sum(1 for t in ctext.values() if re.search(r"BBQ pit\b", t)), 0)
    chk("WPC_NORMALISATION_PRESENT",
        any("Wood-Plastic Composite / Plastik Kitar Semula" in t for t in ctext.values()), True)
    chk("PROMENADE_PRESENT", any("Promenade" in t for t in ctext.values()), True)

    # ============================ PANELS ============================
    chk("PAGES_WITHOUT_PRODUCTION_PANEL",
        sum(1 for pid, d in D.items() if not any(s["name"] == "ProdPanel" for s in d["panel"])), 0)
    chk("PRODUCTION_PANEL_ON_CANVAS",
        sum(1 for pid, d in D.items() for s in d["canvas"] if s["name"] == "ProdPanel"), 0)
    REQ = ("FUNGSI SKRIN", "KELUARGA PELAKSANAAN", "PERANAN HALAMAN SEMAKAN", "POLISI NOTA",
           "KAWALAN", "SKOP SELESAI", "PERSISTEN", "STATUS BELUM SELESAI")
    chk("PRODUCTION_PANEL_MISSING_FIELD",
        sum(1 for pid in ptext for k in REQ if k not in ptext[pid]), 0)
    return res


_XC = {}
def _slide_xml(pptx, n):
    if (pptx, n) not in _XC:
        _XC[(pptx, n)] = zipfile.ZipFile(pptx).read(f"ppt/slides/slide{n}.xml").decode("utf-8")
    return _XC[(pptx, n)]


if __name__ == "__main__":
    rep = run(sys.argv[1])
    w = max(len(k) for k, _, _, _ in rep)
    fail = 0
    for k, v, e, ok in rep:
        if not ok: fail += 1
        print(f"{'PASS' if ok else 'FAIL'}  {k:<{w}}  {v!r}" + ("" if ok else f"   expected {e!r}"))
    print(f"\n{len(rep)-fail}/{len(rep)} PASS")
    sys.exit(1 if fail else 0)
