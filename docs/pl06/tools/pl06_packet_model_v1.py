# -*- coding: utf-8 -*-
"""Stage 4.2F-J — provisional ID working packets for the 12 ACTIVE PL06 units.

SCOPE
-----
Bariah's written scope is FORWARD_FROM_B03. The frozen inventory holds 14 units; two are
retained legacy artifacts and are NOT regeneration targets:

    K5-PL06-T03-B02   LEGACY_RETAINED · LEGACY_STORYBOARD_ONLY
                      named exception: LAMPIRAN_NOT_PART_OF_ORIGINAL_DELIVERY_CONTRACT
    K5-PL06-T04-B01   LEGACY_RETAINED · STORYBOARD_AND_LAMPIRAN

Legacy units get a MANIFEST ENTRY with paths and hashes, never an empty production packet,
and they never appear in PRODUCTION refusal totals.

AUTHORITY
---------
Every instructional value is read from `pl06_authority_v1`, which reads the committed
declaration. Nothing is re-declared here as a literal.

HONEST COMPLETION
-----------------
A packet with every field present is SCHEMA complete. That is not the same as the copy being
written, and this module reports them separately. A quiz slot carrying only a cited row is a
QUIZ_ANCHORED_SLOT, never a drafted item; a slot with no candidate row at all is
QUIZ_UNANCHORED_SLOT, because calling that one anchored overstates how far it has got.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import pl06_extract_v1 as EX            # noqa: E402
import pl06_extract_rest_v1 as EXR      # noqa: E402
import pl06_unit_model_v1 as U          # noqa: E402
import pl06_authority_v1 as A           # noqa: E402

STAGE = "4.2F-J"
SUITE_ID = "PL06_PACKET_PREP_QA_v1"
GENERATED_BY = "docs/pl06/tools/pl06_packet_emit_v1.py"
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
OUT_DIR = os.path.join(os.path.dirname(HERE), "packets")

STATUS_MARKS = ["PROVISIONAL_WORKING_PACKET", A.NOT_INSTRUCTIONALLY_APPROVED,
                "AWAITING_BARIAH_ID_WATAK_DIALOG_RUMUSAN"]

PENDING_CAST = "NAME_PENDING_PROPOSAL"
ROLE_NEW = "ROLE_NEW_REQUIRED"
EXCEPTION = "EXCEPTION_FOR_REVIEW"
JUDGMENT = "DIALOGUE_JUDGMENT_REQUIRED"
ANCHORED = "QUIZ_ANCHORED_SLOT"
UNANCHORED = "QUIZ_UNANCHORED_SLOT"

# ----------------------------------------------------------------------- role classification
SPEAKER_NOT_REQUIRED = "SPEAKER_NOT_REQUIRED"
REUSE_ALYA = "REUSE_ALYA"
REUSE_ENCIK_RAHMAN = "REUSE_ENCIK_RAHMAN"
NEW_ROLE_REQUIRED = "NEW_ROLE_REQUIRED"

FAM_JUNIOR = "CONTRACTOR_JUNIOR_TRAINEE_OPERATIONAL_LEARNER"
FAM_SENIOR = "MENTOR_CONTRACTOR_SENIOR"

# ------------------------------------------------------------------------------ the 14 units
UNIT_ROLL = [
    ("K5-PL06-T03-B02", 3, 2, "Struktur Taman dan Perabot Taman"),
    ("K5-PL06-T04-B01", 4, 1, "Penjagaan dan Penyelenggaraan"),
    ("K5-PL06-T01-B01", 1, 1, "Proses Memula Kerja - Penyediaan Tapak"),
    ("K5-PL06-T01-B02", 1, 2, "Jadual Kerja dan Perlaksanaan Pembinaan Landskap"),
    ("K5-PL06-T01-B03", 1, 3, "Sumber-Sumber yang Diperlukan Untuk Memulakan Projek Landskap"),
    ("K5-PL06-T02-B01", 2, 1, "Elemen Landskap Kejur dan Elemen Landskap Lembut/Penanaman"),
    ("K5-PL06-T02-B02", 2, 2, "Kerja-Kerja Berkaitan dengan Mekanikal & Elektrikal (M&E)"),
    ("K5-PL06-T03-B01", 3, 1, "Kawasan Berturap dan Gelanggang Sukan & Permainan"),
    ("K5-PL06-T03-B03", 3, 3, "Infrastruktur"),
    ("K5-PL06-T03-B04", 3, 4, "Badan Air (Water Body)"),
    ("K5-PL06-T03-B05", 3, 5, "Pencahayaan dan Pengairan"),
    ("K5-PL06-T05-B01", 5, 1, "Pengurusan Kualiti Projek"),
    ("K5-PL06-T06-B01", 6, 1, "Perlindungan dan Penambahbaikan Alam Sekitar"),
    ("K5-PL06-T07-B01", 7, 1, "Demobilisasi"),
]

EVIDENCE_TIERS = ["COMMITTED_ANALYSIS_AND_ROWS", "ROWS_ONLY", "NO_EXTRACTOR"]


def legacy():
    return A.legacy_units()


def active_unit_ids():
    return [u[0] for u in UNIT_ROLL if u[0] not in legacy()]


# ==========================================================================================
# SOURCE ACCESS
# ==========================================================================================
_ROWS = None


def all_rows():
    global _ROWS
    if _ROWS is None:
        out = dict(EX.extract_all())
        for uid, ex in EXR.extract_all().items():
            out.setdefault(uid, ex)
        _ROWS = out
    return _ROWS


def evidence_tier(unit_id):
    if unit_id in U.UNIT_ANALYSIS and unit_id in all_rows():
        return "COMMITTED_ANALYSIS_AND_ROWS"
    if unit_id in all_rows():
        return "ROWS_ONLY"
    return "NO_EXTRACTOR"


def _txt(r):
    return (r.get("controlled_display_text") or "").strip()


def _structural(ex):
    return [r for r in ex["rows"]
            if r["content_type"].startswith("HEADING") and U.is_structural(r)]


def _prose(ex):
    """Substantive prose rows — the ones that carry a claim rather than a label."""
    return [r for r in ex["rows"]
            if not U.is_structural(r) and len(_txt(r)) > 40]


def _first_sentence(t):
    t = " ".join(t.split())
    m = re.search(r"(?<=[.!?])\s", t)
    return (t[:m.start()] if m else t).strip()


# ==========================================================================================
# CHARACTER ROLE RE-AUDIT
#
# Classification order is the written contract's: does the role need to SPEAK at all; if so
# does it fall inside an approved role family; only then is a new role proposed.
# ==========================================================================================
ROLE_CANDIDATES = [
    dict(role_id="ROLE-KONTRAKTOR", markers=["kontraktor", "Kontraktor"],
         family=FAM_JUNIOR, speaks=True,
         why="The module addresses the contractor's own execution duties, which is an "
             "operational learner function."),
    dict(role_id="ROLE-PENYELIA", markers=["penyelia", "Penyelia", "pemeriksaan",
                                           "diperiksa", "pemantauan"],
         family=FAM_SENIOR, speaks=True,
         why="Supervision and inspection are mentor functions and need no separate "
             "professional licence to voice."),
    dict(role_id="ROLE-JURUTERA", markers=["Jurutera", "Ir."],
         family=None, speaks=False,
         why="The engineer appears as the AUTHORITY BEHIND A DOCUMENT (the structural "
             "drawing), not as a participant in the work being described."),
    dict(role_id="ROLE-PEGAWAI-PENGUASA", markers=["Pegawai Penguasa", "S.O."],
         family=None, speaks=False,
         why="The S.O. appears as an APPROVAL BODY. Approval is an event, not a speaking "
             "part."),
    dict(role_id="ROLE-JURUUKUR", markers=["Pelan Ukur", "juruukur", "Juruukur"],
         family=None, speaks=False,
         why="The surveyor appears only through the Pelan Ukur Sempadan, a cited reference "
             "document."),
]

# A role that would otherwise be reference-only becomes a genuine speaking role if the
# module shows it DECIDING or ACTING rather than being cited. Checked against the module's
# own verbs so the classification is evidence-led, not assumed.
ACTING_VERBS = ["memutuskan", "mengarahkan", "menolak kerja", "memberi arahan",
                "mengesahkan di tapak", "menghentikan kerja"]


def _cited_text(ex, markers, limit=2):
    out = []
    for r in ex["rows"]:
        t = _txt(r)
        if any(m in t for m in markers):
            out.append(dict(row_id=r["row_id"], text=t[:180]))
        if len(out) >= limit:
            break
    return out


def role_audit(unit_id, ex):
    """One record per candidate role the module's own text actually raises."""
    if ex is None:
        return []
    text = " ".join(_txt(r) for r in ex["rows"])
    out = []
    for c in ROLE_CANDIDATES:
        if not any(m in text for m in c["markers"]):
            continue
        cites = _cited_text(ex, c["markers"])
        # The acting verb must appear in the SAME ROW as the role marker. Scanning the whole
        # unit attributed "Mengawal dan mengarahkan aliran air permukaan" — a sentence about
        # water — to the engineer, the S.O. and the surveyor at once, and would have sent
        # three invented new roles to Bariah.
        acting = sorted({v for r in ex["rows"]
                         if any(m in _txt(r) for m in c["markers"])
                         for v in ACTING_VERBS if v in _txt(r)})
        if not c["speaks"] and not acting:
            cls, reuse, desc = SPEAKER_NOT_REQUIRED, None, None
        elif not c["speaks"] and acting:
            cls, reuse = NEW_ROLE_REQUIRED, None
            desc = (f"{c['role_id']} is shown acting or deciding, not merely cited "
                    f"({', '.join(acting)}). A separate professional authority would need "
                    "to speak.")
        else:
            ch = A.character_by_family(c["family"])
            cls = REUSE_ALYA if c["family"] == FAM_JUNIOR else REUSE_ENCIK_RAHMAN
            reuse, desc = (ch["name"] if ch else None), None
            if ch is None:
                cls, desc = NEW_ROLE_REQUIRED, f"No approved character for {c['family']}."
        out.append(dict(unit_id=unit_id, role_id=c["role_id"],
                        cited_module_text=cites, needs_to_speak=bool(c["speaks"] or acting),
                        role_family=c["family"], classification=cls,
                        reused_character=reuse,
                        new_role_description=desc,
                        name=(reuse if reuse else
                              (PENDING_CAST if cls == NEW_ROLE_REQUIRED else None)),
                        reason=c["why"] if cls == SPEAKER_NOT_REQUIRED else
                        (f"Role family {c['family']} is covered by an approved character."
                         if reuse else desc)))
    return out


def _roles(unit_id, ex):
    audit = role_audit(unit_id, ex)
    narrator = A.character_by_family("NARRATOR")
    return dict(
        cls="WRITTEN_CHARACTER_CONTRACT_APPLIED",
        audit=audit,
        speaker_not_required=[a for a in audit
                              if a["classification"] == SPEAKER_NOT_REQUIRED],
        reused=[dict(role_id=a["role_id"], name=a["reused_character"],
                     role_family=a["role_family"], authority=A.WRITTEN_CONFIRMED)
                for a in audit if a["reused_character"]],
        new_required=[dict(role_id=a["role_id"], status=ROLE_NEW, name=PENDING_CAST,
                           role_description=a["new_role_description"],
                           authority_basis=a["reason"])
                      for a in audit if a["classification"] == NEW_ROLE_REQUIRED],
        narrator=dict(name=narrator["name"], authority=narrator["authority_source"],
                      reused=True) if narrator else None)


# ==========================================================================================
# RUMUSAN — EXACTLY THREE INTERNAL BEATS
# ==========================================================================================
def _subtopics(unit_id, ex):
    raw = ex.get("boundary", {}).get("subtopics") if ex else None
    parts = [p.strip() for p in (raw or "").split("+") if p.strip()]
    return dict(cls="SOURCE_DERIVED" if ex else "PENDING_SOURCE_EXTRACTION",
                declared=raw, items=parts, count=len(parts))


# D3 rule 1: the learner-facing copy flows WITHOUT the small headings Kepentingan / Skop /
# Manfaat, and D2 states outright that the labels are not shown to the trainee. An inline
# "Skop: " prefix is that label, moved. The lead-in below is a sentence, not a heading, and
# it is the shape the authority's own D1 copy uses ("Komponen infrastruktur merangkumi…").
SCOPE_LEAD_IN = "Kerja ini merangkumi "


def scope_copy(items):
    """Flowing scope copy containing every declared subtopic and no beat label."""
    if not items:
        return None
    if len(items) == 1:
        return f"{SCOPE_LEAD_IN}{items[0]}."
    return f"{SCOPE_LEAD_IN}{', '.join(items[:-1])} dan {items[-1]}."


def _rumusan(unit_id, ex, subs):
    """importance / scope(subtopics[]) / benefit. Never one beat per subtopic."""
    beats_decl = A.rumusan_beats()
    anal = U.UNIT_ANALYSIS.get(unit_id)
    committed = anal["rumusan_beats"] if anal else []
    prose = _prose(ex) if ex else []

    def pick(pred, fallback_idx):
        hit = next((r for r in prose if pred(_txt(r))), None)
        if hit:
            return _first_sentence(_txt(hit)), [hit["row_id"]]
        if committed and fallback_idx < len(committed):
            return committed[fallback_idx], []
        if prose:
            return _first_sentence(_txt(prose[0])), [prose[0]["row_id"]]
        return None, []

    imp_t, imp_rows = pick(lambda t: any(k in t.lower() for k in
                                         ("penting", "kritikal", "memastikan", "wajib")), 0)
    ben_t, ben_rows = pick(lambda t: any(k in t.lower() for k in
                                         ("manfaat", "membantu", "mengelakkan", "kualiti")),
                           len(committed) - 1 if committed else 0)
    beats = [
        dict(beat="importance", learner_facing_label=None, learner_facing=False,
             text=imp_t, rows=imp_rows,
             cls="SOURCE_DERIVED" if imp_rows else "COMMITTED_UNIT_BEAT"),
        dict(beat="scope", learner_facing_label=None, learner_facing=False,
             subtopics=list(subs["items"]), subtopic_count=len(subs["items"]),
             text=scope_copy(subs["items"]),
             rows=[], cls="SOURCE_DERIVED_SUBTOPIC_ENUMERATION"),
        dict(beat="benefit", learner_facing_label=None, learner_facing=False,
             text=ben_t, rows=ben_rows,
             cls="SOURCE_DERIVED" if ben_rows else "COMMITTED_UNIT_BEAT"),
    ]
    copy_done = all(b.get("text") for b in beats)
    fp = A.forbidden_phrase()
    return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS",
                authority_status=A.DRAFTED_NOT_APPROVED,
                declared_beats=beats_decl, beats=beats, beat_count=len(beats),
                copy_complete=copy_done,
                support_visual_required=A.value("rumusan", "support_visual_required"),
                uses_forbidden_phrase=any(fp in (b.get("text") or "") for b in beats))


# ==========================================================================================
# QUIZ
# ==========================================================================================
def _heading_blocks(ex):
    """(heading_row, rows_until_the_next_structural_heading) for every structural heading."""
    heads = _structural(ex)
    ids = {h["row_id"] for h in heads}
    out, cur, body = [], None, []
    for r in ex["rows"]:
        if r["row_id"] in ids:
            if cur is not None:
                out.append((cur, body))
            cur, body = r, []
        elif cur is not None:
            body.append(r)
    if cur is not None:
        out.append((cur, body))
    return out


# A lead-in is not an option. "Prosedur Rasmi iaitu proses pengambilan tapak biasanya
# melibatkan:" introduces the items; it is not one of them.
LEAD_IN_TAILS = ("melibatkan:", "termasuk:", "berikut:", "adalah:", "ialah:", "meliputi:")


def _point_text(r):
    t = _txt(r)
    return t[:-1].strip() if t.endswith(":") else t


def _points(body):
    """Parallel sub-points under a heading — the natural material for a MR item.

    Bare section labels ("Skop Kerja", "Kepentingan Kontrak") are excluded by length: they
    name a block rather than state anything a learner could be asked to select.
    """
    out = []
    for r in body:
        if r["content_type"] != "LIST_ITEM":
            continue
        t = _txt(r)
        if any(t.endswith(x) for x in LEAD_IN_TAILS):
            continue
        if 25 <= len(_point_text(r)) <= 130:
            out.append(r)
    return out


def _mr_item(ex, slot, avoid_rows):
    """A Multiple Response built from sibling sub-points, not from a fifth heading.

    A MR asks which of several things apply. The units that ran out of HEADING_3 rows did not
    run out of source: each has headings whose sub-points are exactly such a set. Correct
    options are the real sub-points of one heading; distractors are sub-points of ANOTHER
    heading in the same unit — same domain, so plausible, but they answer a different
    question.
    """
    blocks = [(h, _points(b)) for h, b in _heading_blocks(ex)]
    usable = [(h, p) for h, p in blocks if len(p) >= 3]
    if len(usable) < 2:
        return None
    # Most usable points wins, then least overlap with what earlier slots already used.
    usable.sort(key=lambda hp: (-len(hp[1]), len({r["row_id"] for r in hp[1]} & avoid_rows)))
    head, pts = usable[0]
    other = next((p for h, p in usable[1:] if h["row_id"] != head["row_id"]), [])
    correct = [_point_text(r) for r in pts[:3]]
    return dict(slot=slot, kind="MULTIPLE_RESPONSE",
                stem=f"Yang manakah antara berikut termasuk dalam {_txt(head)}? "
                     "(Pilih semua yang berkenaan.)",
                correct=correct,
                correct_rows=[r["row_id"] for r in pts[:3]],
                anchor_row=head["row_id"],
                distractors=[_point_text(r) for r in other[:3]],
                distractor_rows=[r["row_id"] for r in other[:3]],
                feedback="; ".join(correct),
                state="QUIZ_DRAFT_COMPLETE", key_status=A.DRAFTED_NOT_APPROVED,
                cls="CAIR_DRAFTED_MULTIPLE_RESPONSE_FROM_SIBLING_SUBPOINTS")


def _quiz(unit_id, ex):
    shape = A.quiz_shape()
    anal = U.UNIT_ANALYSIS.get(unit_id)
    if anal:
        items = [dict(slot=f"Q{i + 1}", kind=q["kind"], stem=q["stem"],
                      correct=q["correct"], correct_rows=q["correct_rows"],
                      distractors=q["distractors"], feedback=q["correct"],
                      state="QUIZ_DRAFT_COMPLETE", key_status=shape["key_status"])
                 for i, q in enumerate(anal["assessment"])]
        return dict(cls="COMMITTED_UNIT_ITEMS", authority_status=shape["key_status"],
                    composition=f"{shape['mcq']} MCQ + {shape['mr']} MR",
                    pass_percent=shape["pass_percent"], items=items,
                    drafted=len(items), anchored=0)
    if ex is None:
        return dict(cls="PENDING_SOURCE_EXTRACTION", authority_status=A.NO_KEY_PENDING_AUTHORING,
                    items=[], drafted=0, anchored=0)

    # Rows-only authoring: a stem per structural heading whose following prose carries the
    # answer. The correct answer is source text; distractors are drawn from OTHER rows in
    # the same unit — same domain, so plausible, but they answer a different question.
    prose = _prose(ex)
    heads = [r for r in _structural(ex) if r["content_type"] == "HEADING_3"]
    idx = {r["row_id"]: i for i, r in enumerate(ex["rows"])}
    pairs = []
    for h in heads:
        after = [r for r in prose if idx[r["row_id"]] > idx[h["row_id"]]]
        if after and idx[after[0]["row_id"]] - idx[h["row_id"]] <= 2:
            pairs.append((h, after[0]))
        if len(pairs) >= shape["mcq"] + shape["mr"]:
            break
    pool = [_first_sentence(_txt(r)) for r in prose]
    items = []
    for i in range(shape["mcq"] + shape["mr"]):
        kind = "MULTIPLE_RESPONSE" if i >= shape["mcq"] else "MULTIPLE_CHOICE"
        if i < len(pairs):
            h, ans = pairs[i]
            correct = _first_sentence(_txt(ans))
            distr = [p for p in pool if p != correct][:3]
            items.append(dict(slot=f"Q{i + 1}", kind=kind,
                              stem=f"Apakah yang mesti dipastikan berkaitan {_txt(h)}?",
                              correct=correct, correct_rows=[ans["row_id"]],
                              anchor_row=h["row_id"], distractors=distr,
                              feedback=correct,
                              state="QUIZ_DRAFT_COMPLETE",
                              key_status=A.DRAFTED_NOT_APPROVED))
        else:
            used = {r for it in items for r in (it.get("correct_rows") or [])}
            mr = _mr_item(ex, f"Q{i + 1}", used) if kind == "MULTIPLE_RESPONSE" else None
            if mr:
                items.append(mr)
                continue
            # A slot with no heading left to point at is NOT an anchored slot. Calling it one
            # reads as "the row is chosen, only the wording is missing", which is false.
            a = heads[i] if i < len(heads) else None
            items.append(dict(slot=f"Q{i + 1}", kind=kind, stem=None, correct=None,
                              correct_rows=[a["row_id"]] if a else [],
                              anchor_row=a["row_id"] if a else None, distractors=[],
                              feedback=None,
                              state=ANCHORED if a else UNANCHORED,
                              key_status=A.NO_KEY_PENDING_AUTHORING))
    return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS",
                authority_status=A.DRAFTED_NOT_APPROVED,
                composition=f"{shape['mcq']} MCQ + {shape['mr']} MR",
                pass_percent=shape["pass_percent"], items=items,
                drafted=len([i for i in items if i["state"] == "QUIZ_DRAFT_COMPLETE"]),
                anchored=len([i for i in items if i["state"] == ANCHORED]),
                unanchored=len([i for i in items if i["state"] == UNANCHORED]))


# ==========================================================================================
# DIALOGUE / VISUAL / INTERACTION
# ==========================================================================================
TENSION_KINDS = [("OBLIGATION", [" mesti ", " wajib "]),
                 ("RISK", ["kegagalan", "risiko", "hakisan", "kerosakan", "bahaya"]),
                 ("DECISION", ["pilihan", "alternatif", "bergantung"]),
                 ("CONFLICT", ["tidak dibenarkan", "elakkan", "mengelakkan"])]


def _sentence_with(t, keys):
    """The sentence that actually carries the marker, not the row's first sentence.

    A row can open with a description and state its obligation two sentences later. Taking
    the first sentence produced anchors labelled OBLIGATION whose text contained no obligation
    at all — T01B02-ROW-011 was one. The anchor must be able to show its own evidence.
    """
    t = " ".join(t.split())
    parts, buf = [], ""
    for ch in t:
        buf += ch
        if ch in ".!?":
            parts.append(buf.strip())
            buf = ""
    if buf.strip():
        parts.append(buf.strip())
    hit = next((s for s in parts if any(k in s for k in keys)), None)
    return hit or (parts[0] if parts else t)


# ------------------------------------------------------------------- E2 tension screening ---
# E2 is confirmed AND its verification is explicitly withheld from automated checking:
# "keperluan ini akan disemak oleh manusia, bukan oleh pemeriksa automatik." So this screen
# does NOT decide whether a dialogue satisfies E2. It sorts anchors by whether they can show
# their own evidence, so a human is handed the weak ones first instead of all twelve.
DESCRIPTIVE_FRAMES = ["adalah kritikal", "adalah struktur", "adalah penting",
                      "berfungsi sebagai", "Ini adalah", "Lazimnya", "merangkumi",
                      "adalah tarikh", "ialah "]
PROCEDURE_OPENERS = ["Menggunakan ", "Mengesahkan ", "Memastikan ", "Memeriksa ",
                     "Menyemak ", "Melaksanakan "]
MODAL_MARKERS = [" mesti ", " wajib ", "hendaklah", "tidak dibenarkan", "perlu "]


def anchor_strength(anchor):
    """(verdict, reasons) for one tension anchor. Never a pass/fail on E2 itself."""
    t = anchor.get("text") or ""
    why = []
    if not any(m in t for m in MODAL_MARKERS):
        why.append("NO_MODAL_OR_PROHIBITION_IN_THE_ANCHOR_TEXT")
    if any(t.startswith(o) for o in PROCEDURE_OPENERS):
        why.append("READS_AS_A_PROCEDURE_STEP_NOT_A_PROBLEM")
    if any(f in t for f in DESCRIPTIVE_FRAMES):
        why.append("DESCRIPTIVE_FRAME_STATES_WHAT_A_THING_IS_NOT_WHAT_IS_AT_STAKE")
    if len(t.split()) < 8:
        why.append("TOO_SHORT_TO_CARRY_A_SCENARIO")
    kind_keys = dict(TENSION_KINDS).get(anchor.get("kind"), [])
    if kind_keys and not any(k in t for k in kind_keys):
        why.append("ANCHOR_TEXT_LACKS_THE_MARKER_THAT_CLASSIFIED_IT")
    return ("QUESTIONABLE_NEEDS_HUMAN_REVIEW" if why else "ANCHOR_SHOWS_ITS_OWN_EVIDENCE"), why


def tension_screen():
    """One record per ACTIVE unit whose dialogue anchors came from the keyword fallback."""
    out = []
    for p in packets():
        d = p["dialogue"]
        if not d.get("anchors"):
            continue
        anchors = []
        for a in d["anchors"]:
            v, why = anchor_strength(a)
            anchors.append(dict(a, verdict=v, reasons=why))
        weak = [a for a in anchors if a["verdict"] != "ANCHOR_SHOWS_ITS_OWN_EVIDENCE"]
        out.append(dict(
            unit_id=p["unit_id"], title=p["title"], evidence_tier=p["evidence_tier"],
            derivation=("COMMITTED_COMPLIANCE_SENSITIVE_STATEMENTS"
                        if p["evidence_tier"] == "COMMITTED_ANALYSIS_AND_ROWS"
                        else "KEYWORD_FALLBACK_OVER_CONTROLLED_PROSE"),
            tension_kind=d.get("tension_kind"), anchors=anchors,
            weak_anchors=len(weak), total_anchors=len(anchors),
            verdict=("ALL_ANCHORS_SHOW_THEIR_OWN_EVIDENCE" if not weak else
                     "SOME_ANCHORS_QUESTIONABLE" if len(weak) < len(anchors) else
                     "EVERY_ANCHOR_QUESTIONABLE"),
            e2_verification="HUMAN_REVIEW_NOT_AN_AUTOMATED_CHECKER"))
    return out


# The three records the owner asked to see in full. Named here rather than computed, so that
# the mechanical screen above can disagree with the list and the disagreement is visible.
TENSION_REVIEW_REQUESTED = ["K5-PL06-T01-B03", "K5-PL06-T02-B01", "K5-PL06-T02-B02"]


# ==========================================================================================
# AUTHORED S02 DIALOGUE
#
# Three units were re-authored after the owner's human review under E2. The copy lives here,
# in the controlled model, for the same reason every other string does: it is regenerated, not
# hand-patched into an artifact.
#
# Line classes come from the authority's paraphrase contract:
#   SOURCE_VERBATIM        the row's own words
#   CONTROLLED_PARAPHRASE  the row's claim in natural speech; `paraphrase_of` names the row
#   CAIR_STRUCTURAL_FRAME  scenario framing that makes no claim of its own
#
# A frame carries no source burden but may name only objects the unit's own rows name. A
# paraphrase may not introduce an obligation, prohibition, approval or legal duty its cited
# rows do not carry — `escalation_defects()` checks that against the declared marker list.
# ==========================================================================================
VERBATIM = "SOURCE_VERBATIM"
PARAPHRASE = "CONTROLLED_PARAPHRASE"
FRAME = "CAIR_STRUCTURAL_FRAME"

AUTHORED_DIALOGUE = {
    "K5-PL06-T01-B03": dict(
        tension_kind="DECISION",
        disposition="INTERNAL_HUMAN_AUTHORING_REVIEW",
        decision="Whether the handover may proceed before the electrical insulation test and "
                 "T&C are done.",
        turns=[
            dict(seq=1, family=FAM_JUNIOR, kind="DECISION_POINT", cls=FRAME,
                 rows=["T01B03-ROW-123", "T01B03-ROW-124"],
                 text="Encik Rahman, pemasangan lampu dan pam air dah siap. Klien nak kita "
                      "serahkan minggu ini. Boleh tak kita teruskan dulu, ujian penebatan "
                      "buat kemudian?"),
            dict(seq=2, family=FAM_SENIOR, kind="SOURCE_BACKED_RESPONSE", cls=PARAPHRASE,
                 rows=["T01B03-ROW-125"], paraphrase_of="T01B03-ROW-125",
                 text="Ujian itulah yang tunjukkan sama ada penebatan kabel dah rosak atau "
                      "bocor, Alya. Kalau ada kebocoran, kita berdepan litar pintas atau "
                      "renjatan elektrik."),
            dict(seq=3, family=FAM_SENIOR, kind="SOURCE_BACKED_CONSEQUENCE", cls=PARAPHRASE,
                 rows=["T01B03-ROW-142"], paraphrase_of="T01B03-ROW-142",
                 text="Dan T&C itu yang sahkan semua sistem, terutamanya elektrik, selamat "
                      "dikendalikan dan tidak mendatangkan bahaya kepada pengguna akhir."),
            # Alya ensures the testing is completed and tells the team; she does not
            # release or hand over. The junior contractor is not the approving authority and
            # the source gives her no such role.
            dict(seq=4, family=FAM_JUNIOR, kind="DECISION_TAKEN", cls=FRAME, rows=[],
                 text="Baiklah. Saya pastikan ujian penebatan dan T&C selesai dahulu, dan "
                      "saya maklumkan kepada pasukan sebelum proses serahan diteruskan."),
        ]),
    "K5-PL06-T02-B01": dict(
        tension_kind="DECISION",
        disposition="CLOSED_BY_FIRDAUS_HUMAN_REVIEW",
        decision="Whether watering and pest monitoring may be reduced when the planting looks "
                 "healthy in the early period.",
        turns=[
            dict(seq=1, family=FAM_JUNIOR, kind="DECISION_POINT", cls=FRAME,
                 rows=["T02B01-ROW-039"],
                 text="Encik Rahman, pokok yang kita tanam dua minggu lepas nampak sihat "
                      "semua. Boleh tak kita jarangkan siraman dan pemantauan perosak?"),
            dict(seq=2, family=FAM_SENIOR, kind="SOURCE_BACKED_RESPONSE", cls=PARAPHRASE,
                 rows=["T02B01-ROW-040"], paraphrase_of="T02B01-ROW-040",
                 text="Belum boleh. Dalam tempoh awal penanaman, siraman yang mencukupi dan "
                      "pemantauan serangan perosak adalah wajib."),
            dict(seq=3, family=FAM_JUNIOR, kind="DECISION_TAKEN", cls=FRAME, rows=[],
                 text="Jadi pokok nampak sihat bukan sebab untuk kita jarangkan. Saya "
                      "teruskan jadual asal."),
        ]),
    "K5-PL06-T02-B02": dict(
        tension_kind="DECISION",
        disposition="INTERNAL_SOURCE_SCOPE_REVIEW",
        decision="Whether the surface swale alone is enough or a sub-soil drainage system is "
                 "still needed.",
        turns=[
            dict(seq=1, family=FAM_JUNIOR, kind="DECISION_POINT", cls=FRAME,
                 rows=["T02B02-ROW-042", "T02B02-ROW-050"],
                 text="Encik Rahman, kawasan ini dah ada swale. Kita masih perlu pasang "
                      "sistem saliran bawah tanah juga?"),
            dict(seq=2, family=FAM_SENIOR, kind="SOURCE_BACKED_RESPONSE", cls=PARAPHRASE,
                 rows=["T02B02-ROW-045", "T02B02-ROW-051"],
                 paraphrase_of="T02B02-ROW-051",
                 text="Swale alirkan air hujan secara semula jadi. Yang di bawah tanah lain "
                      "ceritanya — sistem saliran bawah tanah kritikal untuk mengelakkan "
                      "genangan air dan kerosakan pada struktur."),
            dict(seq=3, family=FAM_SENIOR, kind="SOURCE_BACKED_CONSEQUENCE", cls=PARAPHRASE,
                 rows=["T02B02-ROW-051"], paraphrase_of="T02B02-ROW-051",
                 text="Ia paling penting di kawasan tanah liat atau di mana paras air tanah "
                      "tinggi. Di situ paip berlubang dibalut geotekstil dan ditimbun kerikil "
                      "untuk kumpul dan alirkan air bawah tanah yang berlebihan."),
            dict(seq=4, family=FAM_JUNIOR, kind="DECISION_TAKEN", cls=FRAME, rows=[],
                 text="Baik, saya semak dulu jenis tanah dan paras air tanah tapak ini "
                      "sebelum kita putuskan."),
        ]),
}


# ------------------------------------------------------------- APPROVED B03 S02 COPY ----
# C3 reads "TERIMA — dialog boleh digunakan seadanya." The paraphrase contract governs
# UNAPPROVED or generated dialogue; this copy is approved instructional content and is
# reproduced from the declaration, never regenerated, paraphrased or reordered here.
APPROVED_COPY = "APPROVED_INSTRUCTIONAL_COPY"
B03_S02_UNIT = "K5-PL06-T03-B03"


def _approved_b03_s02():
    rec = A.rule("dialogue", "b03_s02_canonical_copy")
    fam = {"Alya": FAM_JUNIOR, "Encik Rahman": FAM_SENIOR}
    turns = [dict(seq=l["seq"], speaker=l["speaker"], role_family=fam[l["speaker"]],
                  kind="APPROVED_LINE", text=l["text"], rows=[], cls=APPROVED_COPY,
                  paraphrase_of=None, paraphrase_source=None)
             for l in rec["value"]]
    return dict(cls="REPRODUCED_APPROVED_C1_COPY",
                authority_status=A.WRITTEN_CONFIRMED,
                status="DIALOGUE_COPY_COMPLETE", tension_kind="DECISION",
                turns=turns, anchors=[], copy_complete=True,
                disposition="APPROVED_BY_C3_NOT_SUBJECT_TO_THE_PARAPHRASE_CONTRACT",
                decision="Whether fence installation may proceed before the boundary survey "
                         "and approved structural drawing are checked.",
                source_file=rec["source_file"], source_sha256=rec["source_sha256"],
                source_sections=list(rec["source_sections"]),
                source_date_ms=rec["source_date_ms"], authority=rec["named_authority"],
                canonical_line_count=rec["line_count"])


def canonical_b03_s02_lines():
    """(speaker, text) in order, from the declaration. The oracle for the exact-match gate."""
    return [(l["speaker"], l["text"])
            for l in A.rule("dialogue", "b03_s02_canonical_copy")["value"]]


def _authored(unit_id, ex):
    if unit_id == B03_S02_UNIT:
        return _approved_b03_s02()
    spec = AUTHORED_DIALOGUE.get(unit_id)
    if not spec:
        return None
    by_id = {r["row_id"]: _txt(r) for r in ex["rows"]}
    junior = A.character_by_family(FAM_JUNIOR)
    senior = A.character_by_family(FAM_SENIOR)
    who = {FAM_JUNIOR: junior["name"], FAM_SENIOR: senior["name"]}
    turns = []
    for t in spec["turns"]:
        turns.append(dict(seq=t["seq"], speaker=who[t["family"]], role_family=t["family"],
                          kind=t["kind"], text=t["text"], rows=list(t["rows"]),
                          cls=t["cls"],
                          paraphrase_of=t.get("paraphrase_of"),
                          paraphrase_source=by_id.get(t.get("paraphrase_of"))))
    return dict(cls="AUTHORED_AFTER_HUMAN_TENSION_REVIEW",
                authority_status=A.DRAFTED_NOT_APPROVED,
                status="DIALOGUE_COPY_COMPLETE",
                tension_kind=spec["tension_kind"], turns=turns,
                anchors=[dict(text=by_id.get(t["paraphrase_of"]), rows=t["rows"],
                              kind=spec["tension_kind"])
                         for t in spec["turns"] if t.get("paraphrase_of")],
                decision=spec["decision"], disposition=spec["disposition"],
                copy_complete=True)


def escalation_defects(turn, rows_index):
    """A paraphrase may not carry an obligation its cited rows do not carry."""
    if turn.get("cls") != PARAPHRASE:
        return []
    src = " ".join(rows_index.get(r, "") for r in (turn.get("rows") or [])).lower()
    line = (turn.get("text") or "").lower()
    return [m for m in A.escalation_markers() if m in line and m not in src]


def _dialogue(unit_id, ex, roles):
    if ex is None:
        return dict(cls="PENDING_SOURCE_EXTRACTION", status=JUDGMENT, turns=[],
                    reason="No controlled rows.")
    authored = _authored(unit_id, ex)
    if authored:
        return authored
    anal = U.UNIT_ANALYSIS.get(unit_id)
    by_id = {r["row_id"]: r for r in ex["rows"]}
    anchors = []
    if anal:
        # The committed `statement` is an ANALYST NOTE — English-mixed, written to explain why
        # a row is compliance-sensitive ("… — a land-encroachment exposure"). It was being put
        # straight into a learner-facing dialogue line. The line must be the module's own
        # words; the analyst note is kept beside it as the reason the row was chosen.
        for s in anal["compliance_sensitive"]:
            src = next((_txt(by_id[r]) for r in s["rows"] if r in by_id and _txt(by_id[r])),
                       None)
            anchors.append(dict(text=_first_sentence(src) if src else None,
                                rows=s["rows"], kind=s["why"],
                                analyst_note=s["statement"],
                                cls="SOURCE_ROW_TEXT_WITH_ANALYST_RATIONALE"))
        anchors = [a for a in anchors if a["text"]]
    if not anchors:
        for kind, keys in TENSION_KINDS:
            for r in _prose(ex):
                t = _txt(r)
                if any(k in t for k in keys):
                    anchors.append(dict(text=_sentence_with(t, keys), rows=[r["row_id"]],
                                        kind=kind))
                if len(anchors) >= 2:
                    break
            if anchors:
                break
    if not anchors:
        return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS", status=JUDGMENT, turns=[],
                    reason="Full analysis of the controlled rows found no obligation, risk, "
                           "decision or conflict defensible as a scenario tension. Not "
                           "fabricated; escalated as a judgment call.")
    junior = A.character_by_family(FAM_JUNIOR)
    senior = A.character_by_family(FAM_SENIOR)
    turns = [
        dict(seq=1, speaker=junior["name"], role_family=FAM_JUNIOR, kind="QUESTION",
             text=f"Apa yang perlu saya pastikan sebelum kerja ini diteruskan?",
             cls="CAIR_STRUCTURAL_FRAME", rows=[]),
        dict(seq=2, speaker=senior["name"], role_family=FAM_SENIOR,
             kind="SOURCE_BACKED_RESPONSE", text=anchors[0]["text"],
             rows=anchors[0]["rows"], cls=VERBATIM),
    ]
    if len(anchors) > 1:
        turns.append(dict(seq=3, speaker=senior["name"], role_family=FAM_SENIOR,
                          kind="SOURCE_BACKED_CONSEQUENCE", text=anchors[1]["text"],
                          rows=anchors[1]["rows"], cls=VERBATIM))
    return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS",
                authority_status=A.DRAFTED_NOT_APPROVED,
                status="DIALOGUE_COPY_COMPLETE",
                tension_kind=anchors[0]["kind"], turns=turns, anchors=anchors,
                copy_complete=True)


def _visual(unit_id, ex):
    anal = U.UNIT_ANALYSIS.get(unit_id)
    if anal:
        subs = anal["visual_subjects"]
        return dict(cls="COMMITTED_UNIT_SUBJECTS", authority_status=A.DRAFTED_NOT_APPROVED,
                    subjects=subs, count=len(subs), copy_complete=bool(subs),
                    source_attested=len([s for s in subs if s["has_source_figure"]]))
    if ex is None:
        return dict(cls="PENDING_SOURCE_EXTRACTION", subjects=[], count=0,
                    copy_complete=False, source_attested=0)
    figs = [r for r in ex["rows"] if r.get("visual_relationship")]
    subs = [dict(subject=f"Rajah sumber pada {r['row_id']}", rows=[r["row_id"]],
                 has_source_figure=True) for r in figs[:4]]
    if not subs:
        heads = _structural(ex)[:3]
        subs = [dict(subject=f"Keratan atau susunan bagi {_txt(h)}", rows=[h["row_id"]],
                     has_source_figure=False) for h in heads]
    return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS",
                authority_status=A.DRAFTED_NOT_APPROVED, subjects=subs, count=len(subs),
                copy_complete=bool(subs), source_attested=len(figs),
                rp104_note=A.rule("visual_direction", "rp104_source_figure_required")["scope"])


# ---------------------------------------------------------------- F3 treatment selection ---
# F3 is a WRITTEN_CONFIRMED rule since the returned authority landed, and it names its own
# four treatments. The selector below is F3's decision order, applied to the module's own
# rows. The English pattern names the four committed analyses carry predate F3 and are kept
# alongside as `committed_pattern`, never silently rewritten.
SEQ_MARKERS = ["Langkah 1", "Langkah 2", "Proses ", "Prosedur", "Tertib Kerja",
               "Peringkat 1", "Peringkat 2"]
CMP_MARKERS = ["berbanding", "Perbezaan antara", "perbezaan antara", " vs ", "berbeza dengan"]
COMMITTED_TO_F3 = {"progressive process": "SEQUENTIAL_PROCESS",
                   "click-to-reveal": "LAYERED_NON_PROCESS_NON_COMPARISON",
                   "comparison": "EXPLICIT_SYMMETRIC_COMPARISON",
                   "static content": "OTHERWISE"}


def _f3_treatment(when):
    r = next((x for x in A.treatment_rules() if x["when"] == when), None)
    return r["treatment"] if r else None


def _f3_select(ex, comps):
    """Return (when, evidence). Symmetry is judged by F3's own definition: BOTH sides must
    carry their own information in the controlled source. Where the source names a comparison
    but only one side is described, F3 sends it to Click-to-Reveal — which is exactly the
    reasoning the authority recorded for B03's Swale screen at F4(b)."""
    heads = _structural(ex)
    text = " ".join(_txt(r) for r in ex["rows"])
    seq = [m for m in SEQ_MARKERS if m in text]
    if seq:
        return "SEQUENTIAL_PROCESS", f"Source names an ordered process ({', '.join(seq[:3])})."
    cmp_hits = [m for m in CMP_MARKERS if m in text]
    if cmp_hits:
        sides = [r for r in _prose(ex) if any(m in _txt(r) for m in CMP_MARKERS)]
        if len(sides) >= 2:
            return ("EXPLICIT_SYMMETRIC_COMPARISON",
                    f"{len(sides)} controlled rows each carry their own side of the "
                    "comparison, so both sides have source information of their own.")
        return ("LAYERED_NON_PROCESS_NON_COMPARISON",
                f"Source names a comparison ({cmp_hits[0]}) but only {len(sides)} row carries "
                "its own side, so it is not symmetric under F3; Click-to-Reveal follows.")
    if len(comps) >= 3:
        return ("LAYERED_NON_PROCESS_NON_COMPARISON",
                f"The module repeats {len(comps)} components with the same internal shape.")
    if len(heads) >= 6:
        return ("LAYERED_NON_PROCESS_NON_COMPARISON",
                f"{len(heads)} structural headings give parallel layered entries even though "
                "the Fungsi/Fokus markers do not repeat.")
    return ("OTHERWISE",
            f"Only {len(heads)} structural headings and {len(comps)} repeated components; "
            "no process and no comparison in the source.")


def _interaction(unit_id, ex):
    anal = U.UNIT_ANALYSIS.get(unit_id)
    comps = U.components(ex) if ex else []
    if ex is None:
        return dict(cls="PENDING_SOURCE_EXTRACTION", primary=None, secondary=None,
                    resolved=False)
    when, why = _f3_select(ex, comps)
    out = dict(cls="F3_RULE_APPLIED_TO_CONTROLLED_ROWS",
               authority_status=A.DRAFTED_NOT_APPROVED,
               f3_case=when, primary=_f3_treatment(when), secondary=None,
               reason=why, resolved=True, repeated_components=len(comps),
               authority_locus="F3", committed_pattern=None, agrees_with_committed=None)
    if anal:
        out["committed_pattern"] = dict(anal["pattern"])
        prior = COMMITTED_TO_F3.get(anal["pattern"]["primary"])
        out["agrees_with_committed"] = (prior == when) if prior else None
        out["cls"] = "F3_RULE_APPLIED_OVER_A_COMMITTED_UNIT_PATTERN"
    return out


# ==========================================================================================
# LEARNER-FACING COPY vs REVIEWER ANNOTATION
#
# D2 states it outright: "Label ini TIDAK dipaparkan kepada pelatih." Everything this repo
# adds for a reviewer's benefit — provenance tags, status marks, beat labels, row ids, cast
# placeholders — is production metadata. None of it may reach a learner. The two lists below
# are the definition of the boundary; the QA suite holds its own copy and compares.
# ==========================================================================================
REVIEWER_ANNOTATION_MARKERS = [
    "[S]", "[S~]", "[A]", "[D]", "[R]", "[U]", "[P]", "[dicadangkan betul]",
    "TECHNICAL_PROOF", "DRAFT_FOR_BARIAH_REVIEW", "NOT_INSTRUCTIONALLY_APPROVED",
    "NOT_LEARNER_FACING_FINAL", "PROVISIONAL_WORKING_PACKET",
    "AWAITING_BARIAH_ID_WATAK_DIALOG_RUMUSAN", "DRAFTED_NOT_APPROVED",
    "NO_KEY_PENDING_AUTHORING", "PENDING_AUTHORING", "QUIZ_ANCHORED_SLOT",
    "NAME_PENDING_PROPOSAL", "SOURCE_CONTROLLED", "CAIR_",
    "Kepentingan:", "Skop:", "Manfaat:", "Isi Utama:",
]
ROW_ID_PATTERN = re.compile(r"\b(?:T\d{2}B\d{2}-)?ROW-\d{3}\b")

# The internal beat names are English production keys; the labels D3 rule 1 forbids are the
# Malay ones a learner would recognise. Checking the key against the copy would find nothing.
BEAT_LEARNER_LABELS = {"importance": "Kepentingan", "scope": "Skop", "benefit": "Manfaat"}


def learner_facing_strings(p):
    """(locus, string) for every string in a packet that a learner would eventually read.

    Visual directions, interaction reasons, analysis records and the role audit are excluded
    on purpose: they are instructions to a producer, not copy.
    """
    out = []
    for t in p["dialogue"].get("turns", []):
        out.append((f"dialogue#{t['seq']}", t.get("text")))
    for b in p["rumusan"].get("beats", []):
        out.append((f"rumusan.{b['beat']}", b.get("text")))
    for i in p["quiz"].get("items", []):
        out.append((f"quiz.{i['slot']}.stem", i.get("stem")))
        out.append((f"quiz.{i['slot']}.correct", i.get("correct")))
        out.append((f"quiz.{i['slot']}.feedback", i.get("feedback")))
        for n, d in enumerate(i.get("distractors") or []):
            out.append((f"quiz.{i['slot']}.distractor{n}", d))
    # A Multiple Response item's correct answer is a list of options, not one string.
    flat = []
    for loc, s in out:
        if isinstance(s, (list, tuple)):
            flat += [(f"{loc}[{i}]", x) for i, x in enumerate(s) if isinstance(x, str)]
        elif isinstance(s, str):
            flat.append((loc, s))
    return [(loc, s) for loc, s in flat if s]


def annotation_leaks(p, markers=None, row_ids=True):
    """(locus, marker) for every reviewer annotation found in learner-facing copy."""
    marks = REVIEWER_ANNOTATION_MARKERS if markers is None else markers
    out = []
    for loc, s in learner_facing_strings(p):
        for m in marks:
            if m in s:
                out.append((f"{p['unit_id']}:{loc}", m))
        if row_ids and ROW_ID_PATTERN.search(s):
            out.append((f"{p['unit_id']}:{loc}", "ROW_ID"))
    return out


# ==========================================================================================
# SOURCE_ANALYSIS_COMPLETE — a checkable contract, derived from the four units that have one
#
# Four units carry a committed analysis. Before this pass `SOURCE_ANALYSIS_COMPLETE` was a
# membership test — "is this unit in UNIT_ANALYSIS" — which proves a dict key exists, not
# that anybody analysed anything. The contract below is what those four records actually
# contain, stated as required fields and floor counts, so a fifth unit can be checked
# against it instead of being waved through by a key.
# ==========================================================================================
ANALYSIS_CONTRACT = {
    "mandatory_propositions": dict(min=8, item_rows="rows",
                                   why="Obligations the unit states, each traced to the row "
                                       "that states it."),
    "terminology": dict(min=6, item_rows="rows",
                        why="Terms the unit introduces, each traced."),
    "compliance_sensitive": dict(min=2, item_rows="rows",
                                 why="Statements where getting it wrong has a professional "
                                     "or legal consequence. These are the dialogue anchors."),
    "assessment": dict(min=5, exact=5, item_rows="correct_rows",
                       why="F2(a) fixes the composition at 4 MCQ + 1 MR."),
    "visual_subjects": dict(min=3, item_rows="rows",
                            why="Named visual subjects, each traced to a row."),
    "rumusan_beats": dict(min=3, item_rows=None,
                          why="At least the three internal beats D3 requires."),
    "ambiguities": dict(min=2, item_rows="rows",
                        why="Places the source is genuinely unclear and how it was resolved. "
                            "An analysis that found none did not look."),
    "pattern": dict(min=1, item_rows=None, fields=["primary", "secondary", "reason"],
                    why="The interaction reading, with its reason."),
    "dialogue": dict(min=1, item_rows=None, fields=["verdict", "reason"],
                     why="The dialogue judgment. SUP-03: E1 now makes S02 a dialogue "
                         "regardless, so this field is retained evidence, not a gate."),
}
ANALYSIS_FIELDS = sorted(ANALYSIS_CONTRACT)


# A floor forces an analyst to produce findings. An analyst who looked and honestly found
# none must be able to say so and still pass — otherwise the contract rewards invention.
# ASSESSED_NO_FINDINGS satisfies a floor; ABSENCE never does, and the record must carry a
# basis saying what was examined.
ASSESSED_NO_FINDINGS = "ASSESSED_NO_FINDINGS"


def _no_findings(v):
    """A field explicitly assessed as empty: {'assessed': 'ASSESSED_NO_FINDINGS', 'basis': …}"""
    return isinstance(v, dict) and v.get("assessed") == ASSESSED_NO_FINDINGS


def analysis_conformance(unit_id):
    """Does this unit's committed analysis satisfy the contract? Defect list, empty = yes."""
    anal = U.UNIT_ANALYSIS.get(unit_id)
    if anal is None:
        return ["NO_COMMITTED_ANALYSIS"]
    valid = {r["row_id"] for r in all_rows().get(unit_id, {}).get("rows", [])}
    bad = []
    for f, spec in sorted(ANALYSIS_CONTRACT.items()):
        v = anal.get(f)
        if v is None:
            bad.append(f"{f}:ABSENT")
            continue
        if _no_findings(v):
            # Explicitly assessed and empty. It clears the floor, but it must say what was
            # looked at — an unexplained "nothing here" is indistinguishable from not looking.
            if not (v.get("basis") or "").strip():
                bad.append(f"{f}:ASSESSED_NO_FINDINGS_WITHOUT_A_BASIS")
            continue
        n = len(v) if isinstance(v, list) else 1
        if n < spec["min"]:
            bad.append(f"{f}:BELOW_MINIMUM_{n}_OF_{spec['min']}")
        if spec.get("exact") and n != spec["exact"]:
            bad.append(f"{f}:NOT_EXACTLY_{spec['exact']}")
        for req in spec.get("fields", []):
            if not (isinstance(v, dict) and v.get(req)):
                bad.append(f"{f}.{req}:ABSENT")
        key = spec.get("item_rows")
        if key and isinstance(v, list):
            for i, it in enumerate(v):
                rs = it.get(key) or []
                if not rs:
                    bad.append(f"{f}[{i}]:NO_ROW_TRACE")
                elif [r for r in rs if r not in valid]:
                    bad.append(f"{f}[{i}]:ROW_NOT_IN_THIS_UNIT")
    return bad


# --------------------------------------------------------------- gap matrix for ROWS_ONLY ---
# Applying the contract to a unit with no analysis returns "absent" nine times, which is true
# and useless. What an author needs to know is whether the SOURCE can support each field, so
# the matrix below counts the evidence already present in the controlled rows and compares it
# to the floor. Nothing is authored here.
MANDATORY_MARKERS = [" mesti ", " wajib ", " perlu ", "hendaklah"]
COMPLIANCE_MARKERS = ["Jurutera", "Ir.", "Pegawai Penguasa", "S.O.", "Pelan Ukur",
                      "diluluskan", "kelulusan", "piawaian", "MS "]
TERM_MARKERS = ["(", ")"]


def analysis_gap_row(unit_id):
    ex = all_rows().get(unit_id)
    if ex is None:
        return dict(unit_id=unit_id, evidence_tier=evidence_tier(unit_id), fields={},
                    verdict="NO_EXTRACTOR")
    prose = _prose(ex)
    heads = _structural(ex)
    figs = [r for r in ex["rows"] if r.get("visual_relationship")]
    avail = {
        "mandatory_propositions": len([r for r in prose
                                       if any(m in _txt(r) for m in MANDATORY_MARKERS)]),
        "terminology": len([r for r in ex["rows"]
                            if "(" in _txt(r) and ")" in _txt(r)]),
        "compliance_sensitive": len([r for r in prose
                                     if any(m in _txt(r) for m in COMPLIANCE_MARKERS)]),
        "assessment": len([h for h in heads if h["content_type"] == "HEADING_3"]),
        "visual_subjects": len(figs) if figs else len(heads),
        # D3 fixes the beat count at three; the evidence question is whether the unit has
        # enough substantive prose to draw three beats from, not how many subtopics it has.
        "rumusan_beats": len(prose),
        "ambiguities": 0,
        "pattern": 1,
        "dialogue": 1,
    }
    fields = {}
    have = U.UNIT_ANALYSIS.get(unit_id) is not None
    for f in ANALYSIS_FIELDS:
        floor = ANALYSIS_CONTRACT[f]["min"]
        n = avail[f]
        fields[f] = dict(
            required=floor, source_evidence=n, authored=have,
            closable_by_assessed_no_findings=True,
            verdict=("AUTHORED" if have else
                     "EVIDENCE_SUFFICIENT_AUTHORING_REQUIRED" if n >= floor else
                     "EVIDENCE_SHORT_ASSESS_THEN_AUTHOR_OR_RECORD_NO_FINDINGS"))
    short = [f for f, v in fields.items()
             if v["verdict"] == "EVIDENCE_SHORT_ASSESS_THEN_AUTHOR_OR_RECORD_NO_FINDINGS"]
    return dict(unit_id=unit_id, evidence_tier=evidence_tier(unit_id), fields=fields,
                fields_short=sorted(short),
                verdict=("ANALYSIS_COMPLETE" if have else
                         "AUTHORING_REQUIRED_EVIDENCE_SUFFICIENT" if not short else
                         "AUTHORING_REQUIRED_EVIDENCE_SHORT"))


def analysis_gap_matrix():
    """Every ACTIVE unit without a committed analysis. Nothing is authored — this is a map."""
    return [analysis_gap_row(u) for u in active_unit_ids()
            if U.UNIT_ANALYSIS.get(u) is None]


# ==========================================================================================
# PACKAGE ACCOUNTING — derived from the roll, never asserted
# ==========================================================================================
def derived_package_shape():
    """14 Storyboards and 13 Lampiran, computed from the unit roll and the artifact profiles.

    The authority declaration states these numbers. This function reaches them a different
    way — by counting units and subtracting the profiles that declare no Lampiran — so the
    two can disagree and be caught. A gate that compared the declaration to itself would
    prove only that JSON parses.
    """
    leg = legacy()
    storyboards = len(UNIT_ROLL)
    no_lampiran = [u for u, spec in leg.items()
                   if spec["artifact_profile"] == "LEGACY_STORYBOARD_ONLY"]
    named_exceptions = [u for u, spec in leg.items() if spec.get("named_exception")]
    lampiran = storyboards - len(no_lampiran)
    return dict(total_units=storyboards, legacy_retained=len(leg),
                active_generation=storyboards - len(leg),
                total_storyboards=storyboards, total_lampiran=lampiran,
                total_primary_pptx=storyboards + lampiran,
                named_legacy_exception=len(named_exceptions),
                units_without_lampiran=sorted(no_lampiran),
                units_with_named_exception=sorted(named_exceptions))


def role_instance_ledger():
    """Per-unit role-instance counts plus the three classification totals.

    The reconciliation this exists for: a headline total and a per-classification breakdown
    that agree are not evidence, because both come from the same list. This returns the
    per-unit counts as well, so a shift inside one unit that leaves the total unchanged is
    still visible.
    """
    ps = packets()
    per_unit = {p["unit_id"]: len(p["roles"]["audit"]) for p in ps}
    aud = [a for p in ps for a in p["roles"]["audit"]]
    by_cls = {}
    for a in aud:
        by_cls[a["classification"]] = by_cls.get(a["classification"], 0) + 1
    by_role = {}
    for a in aud:
        by_role[a["role_id"]] = by_role.get(a["role_id"], 0) + 1
    return dict(total=len(aud), per_unit=per_unit, by_classification=by_cls,
                by_role_id=by_role,
                sum_of_classifications=sum(by_cls.values()),
                sum_of_role_ids=sum(by_role.values()),
                sum_of_per_unit=sum(per_unit.values()),
                units_with_no_role_marker=sorted(u for u, n in per_unit.items() if n == 0))


# ==========================================================================================
def analysis_record(unit_id, ex, dlg, inter, roles):
    return dict(
        dialogue_tension=(f"Selected a {dlg.get('tension_kind')} anchor because the module's "
                          f"own rows state it; no obligation was invented."
                          if dlg.get("turns") else
                          "No defensible tension found after reading every controlled row."),
        treatment=inter.get("reason"),
        role_mapping=("; ".join(f"{a['role_id']}={a['classification']}"
                                for a in roles["audit"]) or "no role markers in source"))


# ==========================================================================================
# ANALYSIS RECORDS — moved out of the authority declaration
#
# These three were briefly written into the instructional authority declaration so that they
# would pass the citation gate. That was the wrong home. A source/subtopic verification for
# one unit, a row-use disposition for one dialogue, and a human tension-review outcome are
# ANALYSIS records about the work; none of them governs generation the way an instructional
# decision does. They live here, are emitted with the packets, and are cited by artifact and
# section rather than carrying an authority status of their own.
# ==========================================================================================
ANALYSIS_RECORD_ARTIFACT = "docs/pl06/authority/FIRDAUS_TENSION_DISPOSITION_v1.md"
ANALYSIS_RECORD_AUTHORITY = "Firdaus Ismail"
ANALYSIS_RECORD_DATE = "2026-08-05"

SOURCE_SCOPE_VERIFICATIONS = {
    "K5-PL06-T02-B02": {'unit': 'K5-PL06-T02-B02', 'declared_subtopic': '2.3 Kerja-Kerja berkaitan dengan Mekanikal & Elektrikal (M&E)', 'extraction_method': 'HEADING_ANCHOR_BODY_CHILD_SLICE_NEVER_PAGE_RANGE', 'frozen_paragraphs': [4340, 4463], 'module_pages': [215, 225], 'row_051': {'inside_frozen_slice': True, 'parent_heading': 'T02B02-ROW-050', 'parent_heading_text': 'Sub-soil drainage', 'heading_level': 'HEADING_3', 'verdict': 'MAPPING_VALID'}, 'row_058': {'inside_frozen_slice': True, 'parent_heading': 'T02B02-ROW-057', 'parent_heading_text': 'Retaining Wall', 'heading_level': 'HEADING_3', 'verdict': 'DIFFERENT_COMPONENT_HEADING_NOT_THE_SAME_DECISION'}, 'recorded_anomaly': 'The declared subtopic string names Mechanical & Electrical, while the HEADING_3 components inside the frozen slice are Swale/dry river bed, Sub-soil drainage and Retaining Wall — drainage and earth-retaining work. The boundary is anchor-frozen and body-anchor precedence governs extraction, so ROW-051 is in scope; the LABEL does not describe the content. Recorded, not silently corrected.'},
}

ROW_USE_DISPOSITIONS = {
    "K5-PL06-T02-B02": dict(
        row_id="T02B02-ROW-058",
        outcome="Three of four conditions fail. ROW-058 is not used. It is retained in the unit's row inventory and remains available for a separate screen.",
        value='EXCLUDED_FROM_THE_T02B02_S02_DIALOGUE',
        conditions_tested=[{'condition': 'clear subtopic relationship', 'met': False, 'finding': "ROW-058 sits under its own HEADING_3 'Retaining Wall' with its own Fungsi and Contoh block, parallel to 'Sub-soil drainage', not beneath it."}, {'condition': 'a second coherent decision', 'met': False, 'finding': 'The authored decision is surface drainage versus sub-soil drainage. A retaining wall answers a different question.'}, {'condition': 'separate source trace', 'met': True, 'finding': 'ROW-058 does carry its own row id and heading.'}, {'condition': 'justification for relevance to the same tension', 'met': False, 'finding': 'None available from the controlled rows.'}],
        artifact=ANALYSIS_RECORD_ARTIFACT, locus="section 3",
        named_authority=ANALYSIS_RECORD_AUTHORITY, date=ANALYSIS_RECORD_DATE),
}

TENSION_DISPOSITIONS = [{'unit_id': 'K5-PL06-T01-B03', 'source_basis': 'ACCEPTED', 'current_tension': 'NOT_ACCEPTED', 'action': 'REAUTHOR', 'classification': 'INTERNAL_HUMAN_AUTHORING_REVIEW', 'rows_permitted': ['T01B03-ROW-125', 'T01B03-ROW-142'], 'direction': 'Build a real work decision, for example whether the work may proceed before the electrical safety test is done.', 'escalated_to_authority': False, 'escalation_reason': None}, {'unit_id': 'K5-PL06-T02-B01', 'source_basis': 'ACCEPTED', 'current_tension': 'ACCEPTED', 'action': 'CLOSE', 'classification': 'CLOSED_BY_FIRDAUS_HUMAN_REVIEW', 'rows_permitted': ['T02B01-ROW-040'], 'direction': 'Operational decision: whether watering or pest monitoring may be reduced when the planting looks healthy in the early period. The answer stays on the source claim. A compliance-sensitive or legal issue is NOT required to accept a tension; E2 asks only for a meaningful question, problem, doubt, tension or decision point.', 'escalated_to_authority': False, 'escalation_reason': None}, {'unit_id': 'K5-PL06-T02-B02', 'source_basis': 'CONDITIONALLY_ACCEPTED', 'current_tension': 'NOT_ACCEPTED', 'action': 'VERIFY_THEN_REAUTHOR', 'classification': 'INTERNAL_SOURCE_SCOPE_REVIEW', 'rows_permitted': ['T02B02-ROW-051'], 'rows_excluded': ['T02B02-ROW-058'], 'direction': 'After verifying the mapping, build the decision of whether surface drainage alone is enough or a sub-soil drainage system is still needed, using the risk of standing water and structural damage as the basis of the answer.', 'escalated_to_authority': False, 'escalation_reason': None}]
TENSION_ESCALATION_TRIGGERS = ['SOURCE_CONFLICT', 'REAL_TECHNICAL_AMBIGUITY', 'UNSUPPORTABLE_CLAIM', 'CHARACTER_WITH_DIFFERENT_AUTHORITY_LICENCE_OR_COMPETENCE']


def tension_dispositions():
    return [dict(d, artifact=ANALYSIS_RECORD_ARTIFACT,
                 named_authority=ANALYSIS_RECORD_AUTHORITY, date=ANALYSIS_RECORD_DATE)
            for d in TENSION_DISPOSITIONS]


def source_scope_verification(unit_id):
    return SOURCE_SCOPE_VERIFICATIONS.get(unit_id)


def row_use_disposition(unit_id):
    return ROW_USE_DISPOSITIONS.get(unit_id)


def packet(unit_id, topik, bahagian, title):
    ex = all_rows().get(unit_id)
    tier = evidence_tier(unit_id)
    subs = _subtopics(unit_id, ex)
    roles = _roles(unit_id, ex)
    dlg = _dialogue(unit_id, ex, roles)
    rum = _rumusan(unit_id, ex, subs)
    qz = _quiz(unit_id, ex)
    vis = _visual(unit_id, ex)
    inter = _interaction(unit_id, ex)

    # SOURCE_ANALYSIS_COMPLETE is now the contract, not a dict-key membership test. A unit
    # passes when its committed analysis carries every required field, clears every floor
    # and traces every item to a row of its own.
    conf = analysis_conformance(unit_id)

    completion = dict(
        PACKET_SCHEMA_COMPLETE=True,
        SOURCE_EXTRACTION_COMPLETE=ex is not None,
        SOURCE_ANALYSIS_COMPLETE=not conf,
        DIALOGUE_COPY_COMPLETE=bool(dlg.get("copy_complete")),
        RUMUSAN_COPY_COMPLETE=bool(rum.get("copy_complete")),
        QUIZ_COPY_COMPLETE=(qz.get("anchored", 1) == 0 and qz.get("unanchored", 0) == 0
                            and qz.get("drafted", 0) > 0),
        VISUAL_DIRECTION_COMPLETE=bool(vis.get("copy_complete")),
        INTERACTION_TREATMENT_COMPLETE=bool(inter.get("resolved")),
        PRODUCTION_READY=False)

    blockers = []
    if not completion["SOURCE_EXTRACTION_COMPLETE"]:
        blockers.append("SOURCE_TRACE_UNRESOLVED")
    if roles["new_required"]:
        blockers.append("CAST_UNRESOLVED")
    if not completion["DIALOGUE_COPY_COMPLETE"]:
        blockers.append("DIALOGUE_ABSENT")
    if not completion["RUMUSAN_COPY_COMPLETE"]:
        blockers.append("RUMUSAN_WORDING_UNRESOLVED")
    if not completion["QUIZ_COPY_COMPLETE"]:
        blockers.append("QUIZ_KEY_UNRESOLVED")
    if not completion["VISUAL_DIRECTION_COMPLETE"]:
        blockers.append("VISUAL_DIRECTION_UNRESOLVED")
    if not completion["INTERACTION_TREATMENT_COMPLETE"]:
        blockers.append("INTERACTION_TREATMENT_UNRESOLVED")
    # Nothing is approved yet: every packet is blocked on the returned Bariah document.
    blockers.append("AWAITING_BARIAH_WRITTEN_RETURN")

    return dict(
        unit_id=unit_id, topik=topik, bahagian=bahagian, title=title, stage=STAGE,
        generation_scope="ACTIVE_GENERATION", status_marks=list(STATUS_MARKS),
        evidence_tier=tier, subtopics=subs,
        controlled_source_rows=dict(
            cls="SOURCE_DERIVED" if ex else "PENDING_SOURCE_EXTRACTION",
            count=len(ex["rows"]) if ex else 0,
            structural_headings=len(_structural(ex)) if ex else 0,
            first_row=ex["rows"][0]["row_id"] if ex else None,
            last_row=ex["rows"][-1]["row_id"] if ex else None),
        roles=roles, dialogue=dlg, rumusan=rum, quiz=qz,
        visual_direction=vis, interaction=inter,
        analysis=analysis_record(unit_id, ex, dlg, inter, roles),
        analysis_conformance=dict(satisfied=not conf, defects=conf,
                                  contract_fields=ANALYSIS_FIELDS),
        source_scope_verification=source_scope_verification(unit_id),
        row_use_disposition=row_use_disposition(unit_id),
        tension_disposition=next((d for d in tension_dispositions()
                                  if d["unit_id"] == unit_id), None),
        completion=completion,
        production_ready=False, production_blockers=sorted(set(blockers)))


def legacy_entry(unit_id, topik, bahagian, title):
    spec = legacy()[unit_id]
    arts = [a for a in A.legacy_artifacts() if a["unit_id"] == unit_id]
    return dict(unit_id=unit_id, topik=topik, bahagian=bahagian, title=title,
                generation_scope="LEGACY_RETAINED",
                artifact_profile=spec["artifact_profile"],
                named_exception=spec["named_exception"], basis=spec["basis"],
                declared_artifacts=arts, artifact_count=len(arts),
                production_packet=False,
                note="Retained artifact. No production packet is created and this unit "
                     "never appears in PRODUCTION refusal totals.")


def packets():
    """ACTIVE units only — 12."""
    return [packet(*u) for u in UNIT_ROLL if u[0] not in legacy()]


def legacy_entries():
    return [legacy_entry(*u) for u in UNIT_ROLL if u[0] in legacy()]


def totals():
    ps, ls = packets(), legacy_entries()
    aud = [a for p in ps for a in p["roles"]["audit"]]
    keys = ["PACKET_SCHEMA_COMPLETE", "SOURCE_EXTRACTION_COMPLETE",
            "SOURCE_ANALYSIS_COMPLETE", "DIALOGUE_COPY_COMPLETE", "RUMUSAN_COPY_COMPLETE",
            "QUIZ_COPY_COMPLETE", "VISUAL_DIRECTION_COMPLETE",
            "INTERACTION_TREATMENT_COMPLETE", "PRODUCTION_READY"]
    return dict(
        TOTAL_PL06_UNITS=len(UNIT_ROLL), LEGACY_RETAINED=len(ls),
        ACTIVE_GENERATION=len(ps),
        ACTIVE_UNITS_WITH_EXTRACTION=len([p for p in ps
                                          if p["completion"]["SOURCE_EXTRACTION_COMPLETE"]]),
        by_tier={t: len([p for p in ps if p["evidence_tier"] == t]) for t in EVIDENCE_TIERS},
        completion={k: len([p for p in ps if p["completion"][k]]) for k in keys},
        role_instances=len(aud),
        speaker_not_required=len([a for a in aud
                                  if a["classification"] == SPEAKER_NOT_REQUIRED]),
        reuse_alya=len([a for a in aud if a["classification"] == REUSE_ALYA]),
        reuse_encik_rahman=len([a for a in aud
                                if a["classification"] == REUSE_ENCIK_RAHMAN]),
        new_role_required=len([a for a in aud if a["classification"] == NEW_ROLE_REQUIRED]),
        distinct_new_roles=len({a["role_id"] for a in aud
                                if a["classification"] == NEW_ROLE_REQUIRED}),
        quiz_items_drafted=sum(p["quiz"].get("drafted", 0) for p in ps),
        quiz_anchored_slots=sum(p["quiz"].get("anchored", 0) for p in ps),
        quiz_unanchored_slots=sum(p["quiz"].get("unanchored", 0) for p in ps),
        dialogue_judgment_required=len([p for p in ps
                                        if p["dialogue"].get("status") == JUDGMENT]),
        source_rows_total=sum(p["controlled_source_rows"]["count"] for p in ps),
        legacy_artifacts=sum(l["artifact_count"] for l in ls))


if __name__ == "__main__":
    for k, v in totals().items():
        print(f"{k:32} {v}")
