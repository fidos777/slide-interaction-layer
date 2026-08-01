# -*- coding: utf-8 -*-
"""ONE controlled learner-interaction instruction per screen.

Bariah: every learner-facing interaction instruction must also be spoken. So the canvas
string and the VO string must not be two independently typed copies — they are generated
from a single field.

    learner_interaction_instruction  ->  canvas_instruction
                                     ->  spoken_instruction

Object-specific wording is preserved per screen kind; there is no single generic phrase.
Silent completion states, popup states and review-only blocks receive NO instruction.
"""

# keyed by (execution_family, screen_role) or by screen id for frames
BY_SCREEN_ROLE = {
    ("FAMILY_S", "GROUP_MASTER"): "Klik pada setiap struktur untuk penjelasan lanjut.",
    ("FAMILY_S", "COMPONENT_EXAMPLE_SELECTION"): "Klik pada setiap contoh untuk penjelasan lanjut.",
    ("FAMILY_P1", "COMPONENT_EXPLANATION_WITH_EXAMPLE_LIST"): "Klik pada setiap contoh untuk melihat perincian.",
    ("FAMILY_P1", "EXAMPLE_DETAIL_FULL_SLIDE"): "Klik pada setiap spesifikasi untuk penjelasan lanjut.",
    ("FAMILY_P2", "COMPONENT_EXPLANATION_WITH_SPEC_LIST"): "Klik pada setiap kategori untuk penjelasan lanjut.",
}

# Scope of the 1 Aug 2026 parity ruling: SCREEN-LEVEL learner instructions.
# The quiz-entry Klik instruction is corroborated on Bariah's corrected slide 73.
BY_STATE_ROLE = {
    "STATE_QUIZ_INTRO": "Klik Mula Kuiz untuk memulakan kuiz.",
}

# Deliberately NOT implemented. These refer to micro-controls (review / retry buttons) and
# have no direct authority; the earlier CC-invented sentence has been withdrawn from both the
# canvas and the VO rather than left in place as if confirmed.
PENDING_BARIAH_CONFIRMATION_SCOPES = {
    "STATE_QUIZ_RESULT": "Semak Jawapan / Ulang Kuiz button instruction",
    "CLOSE_ICON": "popup close icon",
    "KEMBALI_BUTTON": "Kembali control",
    "STATE_ALL_VIEWED": "completion-only controls",
}

# Task-supplied wording (1 Aug 2026 transcript). Screen-level, not micro-control, so it is
# implemented — but its authority class is recorded as TASK_SUPPLIED, not CONFIRMED_BARIAH.
BY_QUESTION_KIND = {
    "MCQ": "Pilih satu jawapan.",
    "MULTIPLE_RESPONSE": "Pilih semua jawapan yang tepat.",
}

AUTHORITY = {
    "Klik pada setiap struktur untuk penjelasan lanjut.": "BARIAH_DIRECT_FROZEN_SLIDE",
    "Klik pada setiap contoh untuk penjelasan lanjut.": "BARIAH_DIRECT_FROZEN_SLIDE",
    "Klik pada setiap contoh untuk melihat perincian.": "TASK_SUPPLIED",
    "Klik pada setiap spesifikasi untuk penjelasan lanjut.": "TASK_SUPPLIED",
    "Klik pada setiap kategori untuk penjelasan lanjut.": "TASK_SUPPLIED",
    "Klik Mula Kuiz untuk memulakan kuiz.": "BARIAH_CORROBORATED_SLIDE_73",
    "Pilih satu jawapan.": "TASK_SUPPLIED",
    "Pilih semua jawapan yang tepat.": "TASK_SUPPLIED",
}


def authority(instruction):
    return AUTHORITY.get(instruction, "UNCLASSIFIED")


def is_screen_level_click(instruction):
    """The confirmed parity scope: a screen-level learner instruction starting with Klik."""
    return bool(instruction) and instruction.startswith("Klik pada setiap")

# Frames whose action is a single button. S01's instruction is already element 4 of its
# spoken transcript, so it is not duplicated here.
NO_INSTRUCTION_STATE_ROLES = {
    "STATE_POPUP", "STATE_ALL_VIEWED", "STATE_GROUP_COMPLETE",
}


def for_screen(rec):
    """The instruction the SCREEN displays. A popup state draws the screen beneath it, so
    the canvas string is a property of the screen, not of the state."""
    return BY_SCREEN_ROLE.get((rec["execution_family"], rec["screen_role"]))


def for_page(rec, st):
    """The one instruction for this page, or None. Same value feeds canvas and VO."""
    if st["screen_role"] in NO_INSTRUCTION_STATE_ROLES:
        return None
    if st["screen_role"] == "STATE_QUIZ_QUESTION":
        return BY_QUESTION_KIND.get(st.get("question_kind"))
    if st["screen_role"] in BY_STATE_ROLE:
        return BY_STATE_ROLE[st["screen_role"]]
    return BY_SCREEN_ROLE.get((st["execution_family"], rec["screen_role"]))


# Learner canvas must never show generator or model metadata.
CANVAS_METADATA_DENYLIST = (
    "FAMILY_P1", "FAMILY_P2", "FAMILY_S", "execution_family",
    "source_row_uid", "interaction_item_id", "runtime_state_id",
    "completion_scope", "return_target", "learner_screen_id", "review_page_role",
    "notes_policy", "parent_screen_id", "screen_path_layer",
    "interaction_selection_level", "persistence_rule",
)
