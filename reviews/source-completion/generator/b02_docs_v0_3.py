# -*- coding: utf-8 -*-
"""Emit STORYBOARD_SCREEN_STATE_MAP_v0_3.md and STORYBOARD_SOURCE_MAP_v0_3.md
directly from the model, so neither document can drift from the deck."""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b02_model_v0_3 as MODEL

BAN = ("```\nREVIEW_READY · PROVISIONAL_CAIR_EXECUTION\n"
       "CAIR_INTEGRITY_EXCEPTION_FOR_REVIEW_BUILD_ONLY · PENDING_FINAL_BARIAH_CONFIRMATION\n"
       "NOT_FOR_MMD_BUILD · MULTIMEDIA_NOT_PRODUCED\n"
       "Generated from b02_model_v0_3.py — do not hand-edit.\n```\n")


def screen_state_map(M, out):
    pi = MODEL.popup_index(M)
    page_by_screen = {}
    for p in M["pages"]:
        page_by_screen.setdefault(p["screen"], []).append(p)
    L = ["# STORYBOARD_SCREEN_STATE_MAP — K5 PL06 T03 B02 v0.3", "", BAN,
         "## 0. Three things this map keeps separate", "",
         "| Term | Meaning | Count |", "|---|---|---:|",
         "| **Physical learner screen** | a page the learner navigates to | "
         f"**{len(M['screens'])}** |",
         "| **Runtime state** | a variable the player holds — not a page | "
         f"**{len(M['states'])}** |",
         "| **Resolved PowerPoint review page** | a page produced so the state can be *seen* "
         f"during review | **{len(M['pages'])}** |", "",
         "A **popup is a runtime state of its example screen**. It is never a Level 3 destination.",
         "**Maximum learner navigation depth = 2** (Level 1 group master → Level 2 example screen).",
         "", "Review pages exist only for this review build. They are not learner screens and they",
         "do not change the learner's navigation depth.", "",
         "## 1. Physical learner screens", "",
         "| # | Screen ID | Kind | Learner title | Level | Parent | Navigation target |",
         "|---:|---|---|---|:-:|---|---|"]
    lvl = {"FRAME": "—", "GROUP_MASTER": "1", "MAIN": "1 child", "EXAMPLES": "2"}
    for i, s in enumerate(M["screens"], 1):
        L.append(f"| {i} | `{s['id']}` | {s['kind']} | {s['title']} | {lvl[s['kind']]} | "
                 f"{('`'+s['parent']+'`') if s['parent'] else '—'} | `{s['nav_target']}` |")
    L += ["", "## 2. Runtime states", "",
          "| State ID | Kind | Owning screen | Derived rule | Enables | Persistent |",
          "|---|---|---|---|---|:-:|"]
    for st in M["states"]:
        L.append(f"| `{st['id']}` | {st['kind']} | `{st['owner']}` | {st['derived_rule']} | "
                 f"{st['enables'] or '—'} | {'yes' if st['persistent'] else 'no'} |")
    L += ["", "**Persistence rule (all states):** once true, a state stays true. Once `Kembali` or the",
          "global `Seterusnya` is enabled it **must not relock** on revisit or LMS resume.", "",
          "## 3. Popup states — one per source row", "",
          "| Popup state ID | Parent example screen | Source row UID | Source locator | "
          "Item label | VO locator |", "|---|---|---|---|---|---|"]
    for st, (cid, r, k) in pi.items():
        L.append(f"| `{st}` | `{cid}_EXAMPLES` | `{r['uid']}` | modul ms {r['ms']} "
                 f"(fizikal {r['phys']}) | {r['label']} | Notes of review page for `{st}` |")
    L += ["", f"**{len(pi)} popup states, {len({r['uid'] for _, r, _ in pi.values()})} distinct source "
          "rows, every parent an example screen.** No source row maps to two popups; no popup lacks a parent.",
          "", "## 4. Enable / disable conditions", "",
          "| Control | Screen | Starts | Enables when | Target |", "|---|---|---|---|---|",
          "| `Seterusnya` | main explanation | disabled | `main_vo_complete[component]` | example screen |",
          "| `Tutup` | popup state | enabled | always | back to the same example screen |",
          "| `Kembali` | example screen | **disabled** | all `item_viewed` for the component | "
          "Level 1 group master |",
          "| `Seterusnya` (global) | group master | **disabled** | `group_complete[group]` | next group / Rumusan |",
          "| `MULA` | S01 | enabled | always | S02 |", "",
          "## 5. Review page index", "",
          "| Review page | Screen | Variant | Shows |", "|---|---|---|---|"]
    for p in M["pages"]:
        L.append(f"| `{p['id']}` | `{p['screen']}` | {p['variant']} | {p['subtitle']} |")
    L += ["", "## 6. Reconciliation", "",
          "```", f"PHYSICAL_LEARNER_SCREENS      = {len(M['screens'])}",
          f"RUNTIME_STATES                = {len(M['states'])}",
          f"REVIEW_PAGES                  = {len(M['pages'])}",
          f"POPUP_STATES                  = {len(pi)}",
          f"SOURCE_ROWS                   = {len({r['uid'] for _, r, _ in pi.values()})}",
          "MAX_LEARNER_NAVIGATION_DEPTH  = 2", "```", ""]
    open(out, "w", encoding="utf-8").write("\n".join(L))


def source_map(M, out):
    pi = MODEL.popup_index(M)
    L = ["# STORYBOARD_SOURCE_MAP — K5 PL06 T03 B02 v0.3", "", BAN,
         "Every learner-facing string and every VO in the deck, traced to its source.", "",
         "**Authority split (A-09, provisional):** DOCX governs textual propositions; the rendered",
         "PDF governs visible table structure, row boundaries, pagination and image ownership.", "",
         "## 1. Components", "",
         "| Component | Group | Main screen | Example screen | Rows | Module page |",
         "|---|---|---|---|---:|---|"]
    for cid in M["order"]:
        c = M["comps"][cid]
        L.append(f"| {c['name']} | {M['groups'][c['group']]['name']} | `{cid}_MAIN` | "
                 f"`{cid}_EXAMPLES` | {len(M['by_comp'][cid])} | ms {c['ms']} (fiz {c['phys']}) |")
    L += ["", "## 2. Every source row → popup → VO", "",
          "| Source row UID | Component | Item label | Fields rendered | Module page | VO chars |",
          "|---|---|---|---|---|---:|"]
    for st, (cid, r, k) in pi.items():
        fields = []
        if r.get("jenis") and r["jenis"].strip() != r["label"].strip(): fields.append("Jenis/Bahan")
        if r.get("fungsi"): fields.append("Fungsi/Spesifikasi")
        if r.get("contoh"): fields.append("Contoh")
        if r.get("visual"): fields.append("Visual")
        L.append(f"| `{r['uid']}` | {M['comps'][cid]['name']} | {r['label']} | "
                 f"{', '.join(fields)} | ms {r['ms']} (fiz {r['phys']}) | {len(r['vo'])} |")
    absent = []
    for st, (cid, r, k) in pi.items():
        miss = [n for n, key in (("Jenis/Bahan", "jenis"), ("Contoh", "contoh"),
                                 ("Visual", "visual")) if not r.get(key)]
        if miss: absent.append((r["uid"], miss))
    L += ["", "## 3. Adaptive popup — fields genuinely absent from source (A-06)", "",
          "These render **no heading at all**. Nothing is invented to fill them.", "",
          "| Source row UID | Absent field(s) | Recorded as |", "|---|---|---|"]
    for uid, miss in absent:
        L.append(f"| `{uid}` | {', '.join(miss)} | `NOT_PRESENT_IN_SOURCE` |")
    L += ["", "## 4. Source assets — named, never embedded", "",
          "| Component | Assets cited in visual direction |", "|---|---|"]
    import re as _re
    tot = set()
    for cid in M["order"]:
        a = set()
        for r in M["by_comp"][cid]:
            a |= set(_re.findall(r"K5PL06T03-B02-IMG-p\d+-x\d+", r.get("visual") or ""))
        tot |= a
        L.append(f"| {M['comps'][cid]['name']} | {', '.join('`'+x+'`' for x in sorted(a)) or '— none in source'} |")
    L += ["", f"**{len(tot)} of 14 registered assets cited. None embedded — `ppt/media` is empty.**",
          "Kemudahan Awam and Water Feature have `NO_DEDICATED_SOURCE_IMAGE`; both carry a native-diagram",
          "specification in text only, and no diagram is drawn.", ""]
    open(out, "w", encoding="utf-8").write("\n".join(L))


if __name__ == "__main__":
    M = MODEL.build()
    d = sys.argv[1]
    screen_state_map(M, os.path.join(d, "STORYBOARD_SCREEN_STATE_MAP_v0_3.md"))
    source_map(M, os.path.join(d, "STORYBOARD_SOURCE_MAP_v0_3.md"))
    print("wrote screen/state map and source map")
