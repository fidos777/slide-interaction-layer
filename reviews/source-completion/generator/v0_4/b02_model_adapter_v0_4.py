# -*- coding: utf-8 -*-
"""Model adapter for the K5 PL06 T03 B02 v0.4 proof build.

The generator MUST NOT reconstruct the architecture. Everything structural is read
from the frozen Stage 2 model artifacts:

  B02_V0_4_MODEL_CONTRACT.json          families, controls, notes policy, cast, depth
  STORYBOARD_SCREEN_STATE_MAP_v0.4.json screens, states, interaction items
  DECISION_REGISTER_B02_v0.4.json       decision status and unresolved items

Source content (the frozen 26-row matrix and the 14-asset register) is read from the
preserved v0.3 data, which this stage does not touch.

This module resolves a proof page list. A page is a (screen record, state record) pair
plus the model-derived facts the generator needs. No page invents a field.
"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.dirname(HERE)
REV = os.path.dirname(GEN)

P_CONTRACT = os.path.join(REV, "B02_V0_4_MODEL_CONTRACT.json")
P_MAP      = os.path.join(REV, "STORYBOARD_SCREEN_STATE_MAP_v0.4.json")
P_REG      = os.path.join(REV, "DECISION_REGISTER_B02_v0.4.json")
P_SRC      = os.path.join(GEN, "b02_content_v0_3.json")
P_ASSETS   = os.path.join(REV, "source-assets", "_manifest.json")


def _load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


class Model:
    """Read-only view over the frozen model. Raises rather than guessing."""

    def __init__(self):
        self.contract = _load(P_CONTRACT)
        self.map = _load(P_MAP)
        self.register = _load(P_REG)
        self.source = _load(P_SRC)
        self.assets = _load(P_ASSETS)
        self.screens = {s["learner_screen_id"]: s for s in self.map["screens"]}
        self.states = {s["runtime_state_id"]: s for s in self.map["states"]}
        self.items = {i["interaction_item_id"]: i for i in self.map["interaction_items"]}
        self.rows = {r["uid"]: r for r in self.source["rows"]}
        self.comps = {c["id"]: c for c in self.source["components"]}
        self.groups = {g["id"]: g for g in self.source["groups"]}
        self.control_types = set(self.contract["control_semantics"]["allowed_control_types"])
        self.decisions = {d["decision_id"]: d for d in self.register["decisions"]}

    # ---- structural accessors ------------------------------------------------
    def screen(self, sid):
        if sid not in self.screens:
            raise KeyError(f"screen not in frozen model: {sid}")
        return self.screens[sid]

    def state(self, stid):
        if stid not in self.states:
            raise KeyError(f"state not in frozen model: {stid}")
        return self.states[stid]

    def item(self, iid):
        if iid not in self.items:
            raise KeyError(f"interaction item not in frozen model: {iid}")
        return self.items[iid]

    def family(self, cid):
        for s in self.map["screens"]:
            if s.get("component_id") == cid:
                return s["execution_family"]
        raise KeyError(f"no execution family in model for component {cid}")

    def states_of(self, sid, role=None):
        out = [s for s in self.map["states"] if s["learner_screen_id"] == sid]
        if role:
            out = [s for s in out if s["screen_role"] == role]
        return out

    def items_of(self, sid):
        return [i for i in self.map["interaction_items"] if i["parent_screen_id"] == sid]

    def row_of_item(self, iid):
        return self.rows[self.item(iid)["source_row_uid"]]

    def assets_of_row(self, uid):
        v = self.rows[uid].get("visual") or ""
        return [a["asset_id"] for a in self.assets if a["asset_id"] in v]

    # ---- notes ---------------------------------------------------------------
    def notes_spec(self, rec):
        """Structured Notes description. Never a pre-concatenated string."""
        pol = rec["notes_policy"]
        fam = rec["notes_policy_family"]
        return dict(policy=pol, family=fam,
                    context_headers=list(rec["notes_context_headers"]),
                    context_spoken=bool(rec["notes_context_spoken"]),
                    spoken_required=bool(rec["spoken_transcript_required"]),
                    spoken_elements=rec.get("spoken_transcript_elements"))


# ============================ proof page resolution ============================
# The proof shows only what is needed to verify the three families plus the frames.
# Every entry names model IDs; nothing here describes layout or content.

FAMILY_S_COMPONENT = "STRUKTUR_PERSISIR_AIR"
FAMILY_P1_COMPONENT = "KERUSI_TAMAN"
FAMILY_P1_EXAMPLE_ROW = "K5-PL06-T03-B02-KERUSI-TAMAN-ROW-01"   # Kerusi Kayu Keras
FAMILY_P2_COMPONENT = "PAPAN_TANDA"


def proof_pages(M):
    """Ordered proof pages. Each carries screen_id + state_id and nothing invented."""
    P = []

    def add(pid, sid, stid, note=""):
        sc, st = M.screen(sid), M.state(stid)
        P.append(dict(id=pid, screen_id=sid, state_id=stid,
                      review_page_role=st["review_page_role"],
                      execution_family=st["execution_family"],
                      component_id=st.get("component_id"),
                      group_id=st.get("group_id"),
                      proof_note=note))

    # ---------------- frame screens ----------------
    add("PP-01", "SCR_S01", "ST_S01_BASE", "S01 spoken entry titles")
    add("PP-02", "SCR_S02", "ST_S02_BASE", "S02 confirmed cast, MS2680 excluded")
    add("PP-03", "SCR_S03", "ST_S03_BASE", "S03 Hilmi continuity")

    # ---------------- FAMILY S ----------------
    add("PP-04", "SCR_GM_STRUKTUR", "ST_GM_STRUKTUR_BASE", "Family S group master")
    c = FAMILY_S_COMPONENT
    add("PP-05", f"SCR_{c}_MAIN", f"ST_{c}_MAIN_BASE", "Family S main explanation")
    add("PP-06", f"SCR_{c}_EXAMPLES", f"ST_{c}_EXAMPLES_BASE", "Family S example selection")
    for n in range(1, 6):
        add(f"PP-{6+n:02d}", f"SCR_{c}_EXAMPLES", f"ST_{c}_POPUP_{n:02d}",
            f"Family S popup {n} of 5")
    add("PP-12", f"SCR_{c}_EXAMPLES", f"ST_{c}_ALL_VIEWED", "Family S all-viewed, Kembali enabled")
    # Kembali returns to the group master with THIS component ticked. The group is not
    # complete — only one of its four components has been done — so the base state is the
    # honest one to show here.
    add("PP-13", "SCR_GM_STRUKTUR", "ST_GM_STRUKTUR_BASE",
        "Family S return target: component complete, group NOT complete")

    # ---------------- FAMILY P1 ----------------
    add("PP-14", "SCR_PERABOT_OVERVIEW", "ST_PERABOT_OVERVIEW_BASE",
        "Perabot gateway, no click level")
    c = FAMILY_P1_COMPONENT
    add("PP-15", f"SCR_{c}_MAIN", f"ST_{c}_MAIN_BASE", "Family P1 component overview + example list")
    det = f"SCR_{c}_EX01_DETAIL"
    add("PP-16", det, f"ST_{c}_EX01_BASE", "Family P1 Level 1 full-slide example detail")
    specs = [i for i in M.items_of(det)]
    for k, it in enumerate(specs, 1):
        add(f"PP-{16+k:02d}", det, it["runtime_state_id"],
            f"Family P1 Level 2 specification popup {k} of {len(specs)}")
    nxt = 17 + len(specs)
    add(f"PP-{nxt:02d}", det, f"ST_{c}_EX01_ALL_SPEC_VIEWED", "Family P1 example complete")
    add(f"PP-{nxt+1:02d}", f"SCR_{c}_MAIN", f"ST_{c}_MAIN_BASE",
        "Family P1 return target, one example ticked, component NOT yet complete")
    n = nxt + 2

    # ---------------- FAMILY P2 ----------------
    c = FAMILY_P2_COMPONENT
    add(f"PP-{n:02d}", f"SCR_{c}_MAIN", f"ST_{c}_MAIN_BASE",
        "Family P2 explanation + specification-category list"); n += 1
    cats = M.items_of(f"SCR_{c}_MAIN")
    for k, it in enumerate(cats, 1):
        add(f"PP-{n:02d}", f"SCR_{c}_MAIN", it["runtime_state_id"],
            f"Family P2 category popup {k} of {len(cats)}"); n += 1
    add(f"PP-{n:02d}", f"SCR_{c}_MAIN", f"ST_{c}_ALL_CATEGORIES_VIEWED",
        "Family P2 component complete"); n += 1

    # ---------------- closing frames ----------------
    add(f"PP-{n:02d}", "SCR_RUMUSAN", "ST_RUMUSAN_BASE", "Rumusan"); n += 1
    add(f"PP-{n:02d}", "SCR_KUIZ", "ST_KUIZ_INTRO", "Kuiz entry, MULA KUIZ"); n += 1
    add(f"PP-{n:02d}", "SCR_KUIZ", "ST_KUIZ_Q1", "MCQ proof"); n += 1
    add(f"PP-{n:02d}", "SCR_KUIZ", "ST_KUIZ_Q5", "Multiple Response proof"); n += 1
    add(f"PP-{n:02d}", "SCR_KUIZ", "ST_KUIZ_RESULT", "Quiz result"); n += 1
    add(f"PP-{n:02d}", "SCR_TAMAT", "ST_TAMAT_BASE", "Tamat, shell Next disabled"); n += 1
    return P


# proof-time viewed-state simulation: which items are ticked on which page.
def viewed_items(M, page, pages):
    """Items already viewed when this page renders.

    Derived from what the proof path has actually completed by this point — never from
    "some earlier page touched this screen". The distinction matters: completing one
    Family P1 example must NOT tick the others, because the whole point of the return
    page is to show that the component is not yet complete.
    """
    st = M.state(page["state_id"])
    sid = page["screen_id"]
    role = st["screen_role"]
    items = M.items_of(sid)
    if role in ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE"):
        return set(i["interaction_item_id"] for i in items)
    if role == "STATE_POPUP":
        order = [i["interaction_item_id"] for i in items]
        mine = st["interaction_item_ids"][0]
        return set(order[:order.index(mine) + 1])
    if role == "STATE_BASE":
        idx = pages.index(page)
        seen_states = {p["state_id"] for p in pages[:idx]}
        seen_complete = {p["state_id"] for p in pages[:idx]
                         if M.state(p["state_id"])["screen_role"] in
                         ("STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE")}
        out = set()
        for i in items:
            rs = i["runtime_state_id"]
            if rs in seen_states:                       # its popup was opened
                out.add(i["interaction_item_id"]); continue
            # an example-selection item is complete only when its own detail screen
            # reached its all-viewed state earlier in the path
            m = re.match(r"^ST_(.+)_EX(\d+)_BASE$", rs)
            if m and f"ST_{m.group(1)}_EX{m.group(2)}_ALL_SPEC_VIEWED" in seen_complete:
                out.add(i["interaction_item_id"])
        return out
    return set()


def completed_components(M, page, pages):
    """Components whose completion state has been reached earlier in the proof path."""
    idx = pages.index(page)
    done = set()
    for p in pages[:idx]:
        st = M.state(p["state_id"])
        if st["screen_role"] == "STATE_ALL_VIEWED" and st.get("component_id") \
           and st["completion_scope"] == "COMPONENT":
            done.add(st["component_id"])
    return done


# ============================ complete v0.4 deck ============================
def all_pages(M):
    """Every runtime state in the frozen model, in learner order, as a review page.

    One review page per runtime state. The count is NOT chosen — it follows the model.
    A review page is an artefact of the review build; it is neither a learner screen
    nor a runtime state, and each page record names all three.
    """
    P = []
    seq = [0]

    def add(sid, stid, note=""):
        sc, st = M.screen(sid), M.state(stid)
        seq[0] += 1
        P.append(dict(id=f"RP-{seq[0]:03d}", screen_id=sid, state_id=stid,
                      review_page_role=st["review_page_role"],
                      execution_family=st["execution_family"],
                      component_id=st.get("component_id"),
                      group_id=st.get("group_id"), proof_note=note))

    def states(sid, role):
        return [s["runtime_state_id"] for s in M.states_of(sid, role)]

    order = [c["id"] for c in M.source["components"]]

    # ---- opening frames ----
    for sid, stid in (("SCR_S01", "ST_S01_BASE"), ("SCR_S02", "ST_S02_BASE"),
                      ("SCR_S03", "ST_S03_BASE")):
        add(sid, stid, "frame screen")

    # ---- Struktur Taman group ----
    add("SCR_GM_STRUKTUR", "ST_GM_STRUKTUR_BASE", "group master, no component visited")
    for cid in [c for c in order if M.comps[c]["group"] == "STRUKTUR_TAMAN"]:
        add(f"SCR_{cid}_MAIN", f"ST_{cid}_MAIN_BASE", "component main explanation")
        ex = f"SCR_{cid}_EXAMPLES"
        add(ex, f"ST_{cid}_EXAMPLES_BASE", "example selection, none viewed")
        for stid in sorted(states(ex, "STATE_POPUP")):
            add(ex, stid, "example popup state")
        add(ex, f"ST_{cid}_ALL_VIEWED", "all examples viewed, Kembali enabled")
    add("SCR_GM_STRUKTUR", "ST_GM_STRUKTUR_GROUP_COMPLETE", "group complete, shell Next enabled")

    # ---- Perabot Taman group ----
    add("SCR_PERABOT_OVERVIEW", "ST_PERABOT_OVERVIEW_BASE", "gateway, no click level")
    for cid in [c for c in order if M.comps[c]["group"] == "PERABOT_TAMAN"]:
        fam = M.family(cid)
        main = f"SCR_{cid}_MAIN"
        if fam == "FAMILY_P1":
            add(main, f"ST_{cid}_MAIN_BASE", "component overview + example list")
            for r in sorted([r for r in M.source["rows"] if r["comp"] == cid],
                            key=lambda r: r["order"]):
                det = f"SCR_{cid}_EX{r['order']:02d}_DETAIL"
                add(det, f"ST_{cid}_EX{r['order']:02d}_BASE", "example detail, Level 1")
                for stid in sorted(states(det, "STATE_POPUP")):
                    add(det, stid, "specification popup, Level 2")
                add(det, f"ST_{cid}_EX{r['order']:02d}_ALL_SPEC_VIEWED", "example complete")
            add(main, f"ST_{cid}_ALL_EXAMPLES_VIEWED", "component complete")
        else:                                   # FAMILY_P2
            add(main, f"ST_{cid}_MAIN_BASE", "explanation + specification-category list")
            for stid in sorted(states(main, "STATE_POPUP")):
                add(main, stid, "specification category popup")
            add(main, f"ST_{cid}_ALL_CATEGORIES_VIEWED", "component complete")

    # ---- closing frames ----
    add("SCR_RUMUSAN", "ST_RUMUSAN_BASE", "frame screen")
    add("SCR_KUIZ", "ST_KUIZ_INTRO", "quiz entry")
    for q in range(1, 6):
        add("SCR_KUIZ", f"ST_KUIZ_Q{q}", "quiz question with both immediate-feedback variants")
    add("SCR_KUIZ", "ST_KUIZ_RESULT", "quiz result")
    add("SCR_KUIZ", "ST_KUIZ_REVIEW", "Semak Jawapan / Ulang Kuiz")
    add("SCR_TAMAT", "ST_TAMAT_BASE", "frame screen")

    covered = {p["state_id"] for p in P}
    missing = {s["runtime_state_id"] for s in M.map["states"]} - covered
    if missing:
        raise AssertionError(f"runtime states not represented in the deck: {sorted(missing)}")
    if len(P) != len(M.map["states"]):
        raise AssertionError(f"review pages {len(P)} != runtime states {len(M.map['states'])}")
    return P
