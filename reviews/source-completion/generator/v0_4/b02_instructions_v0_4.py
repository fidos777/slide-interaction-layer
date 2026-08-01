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

BY_STATE_ROLE = {
    "STATE_QUIZ_INTRO": "Klik Mula Kuiz untuk memulakan kuiz.",
    "STATE_QUIZ_RESULT": "Klik Semak Jawapan untuk menyemak, atau Ulang Kuiz untuk mencuba semula.",
}

BY_QUESTION_KIND = {
    "MCQ": "Pilih satu jawapan.",
    "MULTIPLE_RESPONSE": "Pilih semua jawapan yang tepat.",
}

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
