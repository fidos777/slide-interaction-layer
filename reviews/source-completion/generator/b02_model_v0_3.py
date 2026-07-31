# -*- coding: utf-8 -*-
"""Screen / state model for K5 PL06 T03 B02 review build v0.3.

Single source of truth for the deck AND the screen/state map. The generator and
the map writer both import this module, so the two can never drift apart.

Three distinct things, never conflated:

  PHYSICAL LEARNER SCREEN  a page the learner navigates to. 26 of them.
  RUNTIME STATE            a variable the player holds. Not a page.
  REVIEW PAGE              a resolved PowerPoint page produced so Bariah can SEE
                           a state. 63 of them. Review pages are an artefact of
                           the review build; they are NOT learner screens.

Navigation depth (R-3): Level 1 = group master, Level 2 = example screen.
A popup is a STATE of its example screen and never a Level 3 destination.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "b02_content_v0_3.json")

KIND_FRAME, KIND_MASTER, KIND_MAIN, KIND_EXAMPLES = "FRAME", "GROUP_MASTER", "MAIN", "EXAMPLES"


def load():
    with open(CONTENT, encoding="utf-8") as f:
        return json.load(f)


def build():
    d = load()
    rows = d["rows"]
    comps = {c["id"]: c for c in d["components"]}
    groups = {g["id"]: g for g in d["groups"]}
    order = [c["id"] for c in d["components"]]
    by_comp = {cid: [r for r in rows if r["comp"] == cid] for cid in order}
    for cid in order:
        by_comp[cid].sort(key=lambda r: r["order"])

    screens, states, pages = [], [], []

    def screen(sid, kind, title, group=None, comp=None, parent=None, nav=None):
        s = dict(id=sid, kind=kind, title=title, group=group, comp=comp,
                 parent=parent, nav_target=nav)
        screens.append(s)
        return s

    def state(sid, kind, owner, derived, enables=None, persist=True):
        states.append(dict(id=sid, kind=kind, owner=owner, derived_rule=derived,
                           enables=enables, persistent=persist))

    def page(pid, screen_id, variant, title, subtitle, payload):
        pages.append(dict(id=pid, screen=screen_id, variant=variant, title=title,
                          subtitle=subtitle, payload=payload))

    # ---------------- frame screens ----------------
    screen("S01", KIND_FRAME, "Komponen Landskap", nav="S02")
    screen("S02", KIND_FRAME, "Pengenalan / Komponen Landskap", nav="S03")
    screen("S03", KIND_FRAME, "Gambaran Keseluruhan", nav="STRUKTUR_TAMAN_MASTER")
    for gid in ("STRUKTUR_TAMAN", "PERABOT_TAMAN"):
        g = groups[gid]
        members = [c for c in order if comps[c]["group"] == gid]
        nxt = "PERABOT_TAMAN_MASTER" if gid == "STRUKTUR_TAMAN" else "RUMUSAN"
        screen(f"{gid}_MASTER", KIND_MASTER, g["name"], group=gid, nav=nxt)
        for cid in members:
            screen(f"{cid}_MAIN", KIND_MAIN, comps[cid]["name"], group=gid, comp=cid,
                   parent=f"{gid}_MASTER", nav=f"{cid}_EXAMPLES")
            screen(f"{cid}_EXAMPLES", KIND_EXAMPLES, f"Contoh {comps[cid]['name']}",
                   group=gid, comp=cid, parent=f"{gid}_MASTER", nav=f"{gid}_MASTER")
    screen("RUMUSAN", KIND_FRAME, "Rumusan", nav="KUIZ")
    screen("KUIZ", KIND_FRAME, "Kuiz", nav="TAMAT")
    screen("TAMAT", KIND_FRAME, "Tamat Bahagian", nav="[route pending — production metadata only]")

    # ---------------- runtime states ----------------
    for cid in order:
        state(f"main_vo_complete[{cid}]", "VO_GATE", f"{cid}_MAIN",
              "true when the main explanation VO ends",
              enables=f"Seterusnya -> {cid}_EXAMPLES", persist=True)
        for i, r in enumerate(by_comp[cid], 1):
            pid = f"{cid}_EXAMPLE_{i:02d}"
            state(f"item_viewed[{pid}]", "ITEM_VIEWED", f"{cid}_EXAMPLES",
                  f"true once popup {pid} has been viewed", enables="Level 2 tick", persist=True)
        state(f"component_complete[{cid}]", "COMPONENT_COMPLETE", f"{cid}_EXAMPLES",
              "all item_viewed for this component are true",
              enables="Kembali; on return, Level 1 card tick", persist=True)
    for gid in ("STRUKTUR_TAMAN", "PERABOT_TAMAN"):
        members = [c for c in order if comps[c]["group"] == gid]
        state(f"group_complete[{gid}]", "GROUP_COMPLETE", f"{gid}_MASTER",
              "all component_complete for " + ", ".join(members) + " are true",
              enables="global Seterusnya", persist=True)

    # ---------------- review pages (learner flow order) ----------------
    n = [0]
    def pid():
        n[0] += 1
        return f"RP-{n[0]:03d}"

    page(pid(), "S01", "BASE", "Komponen Landskap", "skrin tajuk", {})
    page(pid(), "S02", "BASE", "Pengenalan / Komponen Landskap", "senario tapak", {})
    page(pid(), "S03", "BASE", "Gambaran Keseluruhan", "narator + mind map", {})

    for gid in ("STRUKTUR_TAMAN", "PERABOT_TAMAN"):
        g = groups[gid]
        members = [c for c in order if comps[c]["group"] == gid]
        page(pid(), f"{gid}_MASTER", "BASE", g["name"],
             "Level 1 — tiada kad selesai", dict(ticked=[], next_enabled=False))
        for cid in members:
            c = comps[cid]
            page(pid(), f"{cid}_MAIN", "BASE", c["name"],
                 "penerangan utama — Seterusnya dikunci sehingga VO tamat",
                 dict(next_enabled=False))
            items = by_comp[cid]
            page(pid(), f"{cid}_EXAMPLES", "BASE", f"Contoh {c['name']}",
                 "Level 2 — tiada item dilihat", dict(viewed=[], kembali=False))
            for i, r in enumerate(items, 1):
                page(pid(), f"{cid}_EXAMPLES", "POPUP", f"Contoh {c['name']}",
                     f"popup — {r['label']}",
                     dict(popup_state=f"{cid}_EXAMPLE_{i:02d}", row=r["uid"],
                          viewed=[f"{cid}_EXAMPLE_{j:02d}" for j in range(1, i)],
                          kembali=False, item_index=i))
            page(pid(), f"{cid}_EXAMPLES", "ALL_VIEWED", f"Contoh {c['name']}",
                 "Level 2 — semua item dilihat, Kembali dibuka",
                 dict(viewed=[f"{cid}_EXAMPLE_{j:02d}" for j in range(1, len(items) + 1)],
                      kembali=True))
        page(pid(), f"{gid}_MASTER", "GROUP_COMPLETE", g["name"],
             "Level 1 — semua kad selesai, Seterusnya dibuka",
             dict(ticked=members, next_enabled=True))

    page(pid(), "RUMUSAN", "BASE", "Rumusan", "rumusan bahagian", {})
    page(pid(), "KUIZ", "BASE", "Kuiz", "5 item — 4 MCQ + 1 Multiple Response", {})
    page(pid(), "TAMAT", "BASE", "Tamat Bahagian", "penutup bahagian", {})

    return dict(content=d, comps=comps, groups=groups, order=order, by_comp=by_comp,
                screens=screens, states=states, pages=pages)


def popup_index(M):
    """popup_state_id -> (component_id, row, item_index). Exactly one per source row."""
    out = {}
    for cid in M["order"]:
        for i, r in enumerate(M["by_comp"][cid], 1):
            out[f"{cid}_EXAMPLE_{i:02d}"] = (cid, r, i)
    return out


if __name__ == "__main__":
    M = build()
    pi = popup_index(M)
    print(f"physical learner screens : {len(M['screens'])}")
    print(f"runtime states           : {len(M['states'])}")
    print(f"review pages             : {len(M['pages'])}")
    print(f"popup states             : {len(pi)}")
    assert len(pi) == 26, len(pi)
    assert len({r['uid'] for _, r, _ in pi.values()}) == 26, "one popup per source row"
    assert len(M["screens"]) == 26, len(M["screens"])
    kinds = {}
    for p in M["pages"]:
        kinds[p["variant"]] = kinds.get(p["variant"], 0) + 1
    print("review pages by variant  :", kinds)
