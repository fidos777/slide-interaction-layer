# INTERACTION_INSTRUCTION_SCOPE — v0.4.2

```
SCREEN_LEVEL_CLICK_INSTRUCTIONS   = 18
SCREEN_LEVEL_CLICK_PARITY_PASS    = 18
SCREEN_LEVEL_CLICK_PARITY_FAIL    = 0
MICRO_CONTROL_INSTRUCTIONS        = 71
MICRO_CONTROL_SCOPE_PENDING       = 71
OTHER_SPOKEN_INSTRUCTIONS_NOT_KLIK = 7
```

# The confirmed rule, and only that

Bariah's evidence is a screen-level instruction: *"Klik pada setiap struktur untuk penjelasan lanjut."*
(annotated deck slide 8). The parity ruling — that such an
instruction must also be spoken — is **transcript-only**, from 1 August 2026.

**The ruling is applied to screen-level `Klik pada setiap …` instructions and nowhere else.**

# What is deliberately NOT extended

| Control | Instances | Classification | Why not extended |
|---|---:|---|---|
| `CLOSE_ICON` on popups | 46 | `MICRO_CONTROL_PARITY_PENDING` | No Bariah evidence that a close icon needs a spoken instruction. Speaking one on every popup would add 46 VO lines nobody asked for. |
| `KEMBALI_BUTTON` | 25 | `MICRO_CONTROL_PARITY_PENDING` | Same. |
| completion-state controls | all silent states | `SILENT_STATE_NOT_SPOKEN` | Silent states carry no Notes at all by ruling. |
| quiz answer key | 5 | `REVIEW_ONLY_NOT_SPOKEN` | Reviewer information, explicitly not learner runtime content. |

Two instructions currently spoken are **not** `Klik pada setiap …` — the quiz entry and the quiz
result controls. They are classified `MICRO_CONTROL_PARITY_PENDING` and flagged here rather than
presented as confirmed: CC extended the rule to them, and that extension has no direct evidence.

# Screen-level instructions carrying parity

| page | screen | instruction |
|---|---|---|
| RP-004 | `SCR_GM_STRUKTUR` | Klik pada setiap struktur untuk penjelasan lanjut. |
| RP-006 | `SCR_STRUKTUR_PERSISIR_AIR_EXAMPLES` | Klik pada setiap contoh untuk penjelasan lanjut. |
| RP-014 | `SCR_STRUKTUR_TEDUHAN_EXAMPLES` | Klik pada setiap contoh untuk penjelasan lanjut. |
| RP-022 | `SCR_KEMUDAHAN_AWAM_EXAMPLES` | Klik pada setiap contoh untuk penjelasan lanjut. |
| RP-028 | `SCR_WATER_FEATURE_EXAMPLES` | Klik pada setiap contoh untuk penjelasan lanjut. |
| RP-035 | `SCR_KERUSI_TAMAN_MAIN` | Klik pada setiap contoh untuk melihat perincian. |
| RP-036 | `SCR_KERUSI_TAMAN_EX01_DETAIL` | Klik pada setiap spesifikasi untuk penjelasan lanjut. |
| RP-042 | `SCR_KERUSI_TAMAN_EX02_DETAIL` | Klik pada setiap spesifikasi untuk penjelasan lanjut. |
| RP-046 | `SCR_KERUSI_TAMAN_EX03_DETAIL` | Klik pada setiap spesifikasi untuk penjelasan lanjut. |
| RP-051 | `SCR_PAPAN_TANDA_MAIN` | Klik pada setiap kategori untuk penjelasan lanjut. |
| RP-057 | `SCR_TONG_SAMPAH_MAIN` | Klik pada setiap contoh untuk melihat perincian. |
| RP-058 | `SCR_TONG_SAMPAH_EX01_DETAIL` | Klik pada setiap spesifikasi untuk penjelasan lanjut. |
| RP-062 | `SCR_TONG_SAMPAH_EX02_DETAIL` | Klik pada setiap spesifikasi untuk penjelasan lanjut. |
| RP-066 | `SCR_TONG_SAMPAH_EX03_DETAIL` | Klik pada setiap spesifikasi untuk penjelasan lanjut. |
| RP-071 | `SCR_DRINKING_FOUNTAIN_MAIN` | Klik pada setiap contoh untuk melihat perincian. |
| RP-072 | `SCR_DRINKING_FOUNTAIN_EX01_DETAIL` | Klik pada setiap spesifikasi untuk penjelasan lanjut. |
| RP-080 | `SCR_DRINKING_FOUNTAIN_EX02_DETAIL` | Klik pada setiap spesifikasi untuk penjelasan lanjut. |
| RP-085 | `SCR_BBQ_PIT_MAIN` | Klik pada setiap kategori untuk penjelasan lanjut. |

# CC-extended, evidence pending

| page | screen | instruction |
|---|---|---|
| RP-092 | `SCR_KUIZ` | Klik Mula Kuiz untuk memulakan kuiz. |
| RP-093 | `SCR_KUIZ` | Pilih satu jawapan. |
| RP-094 | `SCR_KUIZ` | Pilih satu jawapan. |
| RP-095 | `SCR_KUIZ` | Pilih satu jawapan. |
| RP-096 | `SCR_KUIZ` | Pilih satu jawapan. |
| RP-097 | `SCR_KUIZ` | Pilih semua jawapan yang tepat. |
| RP-098 | `SCR_KUIZ` | Klik Semak Jawapan untuk menyemak, atau Ulang Kuiz untuk mencuba semula. |

No VO was altered in this audit stage.
