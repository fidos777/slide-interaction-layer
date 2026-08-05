# -*- coding: utf-8 -*-
"""Stage 4.2F-I — provisional ID working packets for the 12 ACTIVE PL06 units.

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
QUIZ_ANCHORED_SLOT, never a drafted item.
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

STAGE = "4.2F-I"
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
             text=("Skop: " + "; ".join(subs["items"])) if subs["items"] else None,
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
            a = heads[i] if i < len(heads) else None
            items.append(dict(slot=f"Q{i + 1}", kind=kind, stem=None, correct=None,
                              correct_rows=[a["row_id"]] if a else [],
                              anchor_row=a["row_id"] if a else None, distractors=[],
                              feedback=None, state="QUIZ_ANCHORED_SLOT",
                              key_status=A.NO_KEY_PENDING_AUTHORING))
    return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS",
                authority_status=A.DRAFTED_NOT_APPROVED,
                composition=f"{shape['mcq']} MCQ + {shape['mr']} MR",
                pass_percent=shape["pass_percent"], items=items,
                drafted=len([i for i in items if i["state"] == "QUIZ_DRAFT_COMPLETE"]),
                anchored=len([i for i in items if i["state"] == "QUIZ_ANCHORED_SLOT"]))


# ==========================================================================================
# DIALOGUE / VISUAL / INTERACTION
# ==========================================================================================
TENSION_KINDS = [("OBLIGATION", [" mesti ", " wajib "]),
                 ("RISK", ["kegagalan", "risiko", "hakisan", "kerosakan", "bahaya"]),
                 ("DECISION", ["pilihan", "alternatif", "bergantung"]),
                 ("CONFLICT", ["tidak dibenarkan", "elakkan", "mengelakkan"])]


def _dialogue(unit_id, ex, roles):
    if ex is None:
        return dict(cls="PENDING_SOURCE_EXTRACTION", status=JUDGMENT, turns=[],
                    reason="No controlled rows.")
    anal = U.UNIT_ANALYSIS.get(unit_id)
    anchors = []
    if anal:
        anchors = [dict(text=s["statement"], rows=s["rows"], kind=s["why"])
                   for s in anal["compliance_sensitive"]]
    if not anchors:
        for kind, keys in TENSION_KINDS:
            for r in _prose(ex):
                t = _txt(r)
                if any(k in t for k in keys):
                    anchors.append(dict(text=_first_sentence(t), rows=[r["row_id"]],
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
             rows=anchors[0]["rows"], cls="SOURCE_DERIVED"),
    ]
    if len(anchors) > 1:
        turns.append(dict(seq=3, speaker=senior["name"], role_family=FAM_SENIOR,
                          kind="SOURCE_BACKED_CONSEQUENCE", text=anchors[1]["text"],
                          rows=anchors[1]["rows"], cls="SOURCE_DERIVED"))
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


def _interaction(unit_id, ex):
    anal = U.UNIT_ANALYSIS.get(unit_id)
    comps = U.components(ex) if ex else []
    if anal:
        return dict(cls="COMMITTED_UNIT_PATTERN", authority_status=A.DRAFTED_NOT_APPROVED,
                    primary=anal["pattern"]["primary"], secondary=anal["pattern"]["secondary"],
                    reason=anal["pattern"]["reason"], resolved=True,
                    repeated_components=len(comps))
    if ex is None:
        return dict(cls="PENDING_SOURCE_EXTRACTION", primary=None, secondary=None,
                    resolved=False)
    heads = len(_structural(ex))
    if len(comps) >= 3:
        return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS",
                    authority_status=A.DRAFTED_NOT_APPROVED, primary="click-to-reveal",
                    secondary="static content", resolved=True,
                    repeated_components=len(comps),
                    reason=f"The module repeats {len(comps)} components with the same "
                           "internal shape.")
    if heads >= 6:
        return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS",
                    authority_status=A.DRAFTED_NOT_APPROVED, primary="click-to-reveal",
                    secondary="static content", resolved=True, repeated_components=len(comps),
                    reason=f"{heads} structural headings give enough parallel entries for a "
                           "reveal treatment even though the Fungsi/Fokus markers do not "
                           "repeat.")
    return dict(cls="CAIR_DRAFTED_FROM_CONTROLLED_ROWS",
                authority_status=A.DRAFTED_NOT_APPROVED, primary="static content",
                secondary=None, resolved=True, repeated_components=len(comps),
                reason=f"Only {heads} structural headings and {len(comps)} repeated "
                       "components; static content is the honest default.")


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

    completion = dict(
        PACKET_SCHEMA_COMPLETE=True,
        SOURCE_EXTRACTION_COMPLETE=ex is not None,
        SOURCE_ANALYSIS_COMPLETE=tier == "COMMITTED_ANALYSIS_AND_ROWS",
        DIALOGUE_COPY_COMPLETE=bool(dlg.get("copy_complete")),
        RUMUSAN_COPY_COMPLETE=bool(rum.get("copy_complete")),
        QUIZ_COPY_COMPLETE=qz.get("anchored", 1) == 0 and qz.get("drafted", 0) > 0,
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
        dialogue_judgment_required=len([p for p in ps
                                        if p["dialogue"].get("status") == JUDGMENT]),
        source_rows_total=sum(p["controlled_source_rows"]["count"] for p in ps),
        legacy_artifacts=sum(l["artifact_count"] for l in ls))


if __name__ == "__main__":
    for k, v in totals().items():
        print(f"{k:32} {v}")
