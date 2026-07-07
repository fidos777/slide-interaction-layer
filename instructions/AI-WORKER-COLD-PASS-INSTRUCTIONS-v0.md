# Arahan AI Worker — Cold-Coverage Pass v0
**Sasaran repo:** `instructions/AI-WORKER-COLD-PASS-INSTRUCTIONS-v0.md` · Anda ialah AI worker menjalankan pass pertama. Ikut fail ini SAHAJA + PR-001 + taxonomy kanon.

## Objektif
Isi `binding/<DECK>-binding-v0.md`: satu baris per momen interaksi, klasifikasi ikut checklist, token ambiguous diserahkan — BUKAN diputuskan. Output anda ialah jadual DRAFT + metrik pusingan-1 + stub kad. Keputusan bukan kerja anda.

## Peraturan tidak boleh runding
1. **JANGAN cipta pattern/μB baru** — hanya cadang melalui mini-ADR (template e). `proposed_binding` hanya boleh mengandungi nama dropdown-sah taxonomy atau senarai calon `{...}`.
2. **JANGAN auto-bind token SME ambiguous** — POP UP tanpa qualifier, "branching" tanpa qualifier, kata kerja tak dikenali → `AMBIGUOUS`, sentiasa.
3. **JANGAN import nama UI generik** — Modal, Accordion, Tooltip, Tabs, Timeline, Process tak boleh muncul dalam `proposed_binding`, walau "sementara". PR-001.3.
4. **Ketiadaan sebutan ≠ ketiadaan requirement** — jangan padam/turunkan apa-apa sebab ia "belum resolved" (guard Bitumen-Sheet).
5. **JANGAN ubah fail taxonomy** — md5 mesti sama sebelum dan selepas pass anda.
6. **JANGAN anggap niat Bariah melebihi teks verbatim** — "mesti dia maksudkan X" ialah pelanggaran, bukan inferens.

## Checklist klasifikasi — jalankan atas SETIAP baris, ikut turutan, berhenti pada padanan pertama
```
Q0  Duplikat token+slide?           → row_disposition: DUPLICATE, paut row_id asal
Q1  Nampak pada learner?  TIDAK     → row_disposition: IMPL-ONLY
Q2  Token ambiguous ikut lexicon?   → binding_status: AMBIGUOUS
    (POP UP / "branching" tanpa qualifier / kata kerja tak dikenali /
     spec bertulis vs build bercanggah)
      + isi ambiguity_reason + senarai calon + stub kad
Q3  Unit tunggal trigger+state+feedback, tiada gate?
      dalam set μB tertutup         → kelas: μB (koordinat, bukan entri)
      luar set                      → AMBIGUOUS + draf mini-ADR
Q4  Tiada feedback/gate, navigasi/rendering tulen? → kelas: R
      SME namakan sendiri → nota "sme_visible: true"
Q5  Topology sama + terungkap add/remove/param atas set tertutup? → kelas: VARIAN
Q6  Topology/μB baru, player SUDAH mampu? → kelas: P — TAPI status AMBIGUOUS
      + mini-ADR (anda tak boleh cipta P; rujuk peraturan #1)
Q7  Player BELUM mampu (topology/coupling baru)? → kelas: T2 + mini-ADR + park
```

## Pengendalian token khusus
| Token | Buat |
|---|---|
| **POP UP** dengan qualifier jelas ("+ close button" / "+ maintain, with VO") | Map ke varian sepadan menu konversi; status ikut taxonomy (kebanyakan DEFERRED) |
| **POP UP** tanpa qualifier | `AMBIGUOUS` + 4 calon menu konversi + kad. Tiada pengecualian |
| **"branching"** | Decision/consequence dalam SB → calon Branching Scenario (T2, qualifier wajib). Hub→leaf→hub + Kembali → Detail Screen + Kembali. Tak jelas → `AMBIGUOUS` + kad |
| **"detail" / detail screen** | Calon presentation detail-screen(Kembali); sahkan topology hub-spoke dulu; ingat nota sme_visible |
| **"click"** | Bukan pattern. Pecahkan kepada μB: clickable-any-order? trigger reveal? Kemudian jalankan checklist |

## Tracking — isi SETIAP baris INTERACTION
- `none` — tiada kesan LMS
- `completion` — mempengaruhi gate/completion (cth unlock-on-all-visited, gate-until-all-correct)
- `interaction-path` — memerlukan laporan laluan cmi.interactions (cth Branching Scenario)
Ragu antara dua nilai → pilih yang lebih tinggi + catat di `notes` (strictest-wins).
Baris bukan-INTERACTION: REJECTED/DUPLICATE → `—` · IMPL-ONLY → `none`.

## Jangan buat
- Jangan parafrasa `sb_token` — petikan tepat dalam `"..."` sahaja
- Jangan tinggalkan baris AMBIGUOUS tanpa `ambiguity_reason` + calon + card stub
- Jangan kira metrik atas baris bukan-INTERACTION
- Jangan tanda RESOLVED atau LOCKED — dua status itu milik manusia
- Jangan hantar apa-apa terus kepada Bariah — kad melalui Firdaus sahaja

## Format output akhir
1. `binding/<DECK>-binding-v0.md` — jadual lengkap (semua baris DRAFT/AMBIGUOUS/DEFERRED), blok metrik pusingan-1 terisi, log RS terisi
2. Queue belum selesai (template d) dijana dari baris AMBIGUOUS, blocking dahulu
3. Stub kad (template b/c) untuk setiap baris AMBIGUOUS — draf, belum hantar
4. Draf mini-ADR (template e) untuk setiap cadangan P/T2/μB baru

## Checklist serah-balik — lengkapkan SEMUA sebelum hantar kepada Firdaus
- [ ] Setiap baris ada `binding_status` + `row_disposition` (`binding_status: —` untuk IMPL-ONLY / REJECTED / DUPLICATE)
- [ ] Setiap baris yang anda isi: `decided_by: AI-draft` — jangan sesekali tulis Firdaus/Bariah dalam kolum itu
- [ ] Sifar nama generik (Modal/Accordion/Tooltip/Tabs/Timeline/Process) dalam `proposed_binding`
- [ ] Setiap cadangan generik ditolak → satu baris log RS
- [ ] Setiap AMBIGUOUS ada `ambiguity_reason` + senarai calon + `card_id` stub
- [ ] Sifar baris auto-bind token ambiguous
- [ ] Semua `sb_token` verbatim dalam `"..."`
- [ ] Enam metrik pusingan-1 dikira, formula ditunjukkan
- [ ] md5 taxonomy sama seperti metadata (tiada mutasi)
- [ ] Baris contoh template sudah dipadam
- [ ] Tiada status RESOLVED/LOCKED ditanda oleh anda
