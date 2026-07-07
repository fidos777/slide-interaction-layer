# ADR-006 — Case Study: 3 Clarification Cycles (Sesi 16/06/2026)
## Untuk digabung ke dalam ADR-006 (Cost of Asking) sebelum commit

| | |
|---|---|
| **Tarikh** | 5 Julai 2026 |
| **Status ADR induk** | Draf siap, belum commit (tertahan disk) |
| **Tindakan** | Append sebagai seksyen "Case Study A" dalam ADR-006 |
| **Sumber bukti** | SS WhatsApp + 12 attachment elicitation/artifak, sesi 16/06/2026, 5:59–6:48 PM |
| **Nota label** | "Clarification cycles" dipilih (bukan "near miss") — tiada kod di-commit atau deploy; semua berlaku pra-commit. Tapi kos yang DIELAK tetap direkod, sebab itulah metrik ADR ini |

---

## Ringkasan

Dalam satu petang, tafsiran kita terhadap keperluan Bariah **salah tiga kali
berturut-turut**. Ketiga-tiga kali, koreksi datang BUKAN daripada soalan
tambahan, tetapi daripada **artifak** (jadual spec-vs-build, kad perbandingan
dua tafsiran) yang membuatkan Bariah mudah nampak dan tulis: "bukan macam ni."
Hasil akhir: spec 3-state lengkap ditulis oleh Bariah sendiri (6:28 PM), lock
bertulis (6:33 PM), dan jumlah kerja kod = **satu delta sahaja** (hover) —
berbanding tiga set perubahan yang hampir dilaksanakan.

Ini bukti operasi bagi dua prinsip ADR-006: (1) **artifak boleh jadi soalan**,
dan (2) cost-if-wrong perlu dinilai SEBELUM bertindak atas tafsiran.

## Tiga cycle

| # | Masa | Tafsiran kita (artifak elicitation) | Hampir jadi tindakan | Koreksi Bariah (bertulis) | Kos dielak |
|---|---|---|---|---|---|
| 1 | 18:16 | "Kembali" = label popup × ATAU skrin berasingan? (kita tak pasti) | Ubah label sahaja | "Branching out (full screen).. Kembali" — skrin penuh, bukan popup; dia classify sample sendiri | Build bercanggah dengan SB; rework s06 + keliru review |
| 2 | 18:19 | "Klik bebas" = buang gate → toggle JSON `next_locked_until_complete: false` **siap-apply** | Apply toggle JSON | Spec 3-state (6:28): klik bebas order **DAN** gate kekal — "After all have been clicked, only unlock... Seterusnya" | Ship gate-off yang bercanggah dengan kehendak dia; patah balik selepas review |
| 3 | 18:23 | "Buang counter & highlight" = sentuh 2 fail kod (option dipilih) | Edit 2 fail kod | "Maksud I highlight tu kat item/gambar. **I yg buang kat SB, tade related coding**" (6:21) | 2 fail kod diubah tanpa sebab; risiko regression pada komponen G6-proven |

**Pattern seragam:** tafsir → hampir act → artifak dipapar → Bariah tulis spec
sebenar → tafsiran tumbang → sifar/minimum kod.

## Mekanisme yang berjaya

Yang menyelamatkan bukan "tanya lagi banyak soalan". Bariah sendiri respon
"Ha pening, jap aa I baca, kakakaka" bila soalan berlapis — tetapi bila
diberi **jadual spec-vs-build** (5 baris: state / Bariah nak / build sekarang),
dia jawab dengan menulis spec 3-state lengkap dalam satu mesej, kemudian lock.

Klasifikasi ikut rangka ADR-006:

- Cycle 1 = **ASK** yang wajar (dua tafsiran menghasilkan kod berlainan;
  cost-if-wrong tinggi) — tapi bentuk terbaik ASK ialah kad perbandingan
  visual (Tafsiran A vs B), bukan soalan teks.
- Cycle 2 & 3 = tafsiran yang sepatutnya kelas **WAIT**: kedua-duanya
  menghasilkan arahan perubahan kod SEBELUM spec ditulis. Artifak semakan
  ("build kau sekarang" column) yang menahannya daripada menjadi commit.

## Pengajaran (untuk badan ADR-006)

1. **Artifak-sebagai-soalan disahkan 3/3.** Jadual perbandingan
   menjawab lebih pantas dan lebih tepat daripada soalan berturutan, dan
   menghasilkan spec bertulis gred provenance tertinggi
   ([confirmed-written], bukan [confirmed-verbal]).
2. **Kolum "build kau sekarang" ialah brek — dinaik taraf ke OPERATING RULE.**
   Setiap artifak yang memaparkan keadaan build semasa bersebelahan tafsiran
   baharu memaksa perbandingan eksplisit — tiga kali ia mendedahkan bahawa
   build SEDIA ADA sudah betul dan tafsiran baharu yang salah.

   **Operating rule (wajib sebelum minta approve apa-apa perubahan):**

   ```
   1. Bariah nak        (spec, dengan provenance)
   2. Build sekarang    (verified — grep/render, bukan ingatan)
   3. Delta dicadang    (apa sebenarnya berubah)
   4. Kos kalau salah   (rework / regression / trust)
   ```

   Ini bukan format dokumentasi — ini workflow. Perubahan tanpa 4 baris ni
   tidak layak dibawa untuk approval.
3. **Kos sebenar bukan pada bertanya — pada bertindak atas tafsiran.**
   Ketiga-tiga cycle melibatkan arahan perubahan konkrit (toggle JSON, 2 fail
   kod) yang hampir dilaksanakan. Cost-if-wrong = rework + regression pada
   komponen G6-proven + hakisan trust bila Bariah jumpa build lari dari SB.
4. **Elicitation berlapis ada had mesra-pengguna.** Bariah engage penuh dengan
   1 kad pilihan; mula pening pada mesej panjang. Had praktikal: satu artifak,
   satu keputusan.

## Rujukan silang

- Spec hasil sesi ini: `taxonomy/interaction-patterns-v0.md` §3.1.
- Validation lapisan behaviour: ADR-005 Addendum A.
- Item terbuka yang sesi ini tinggalkan: OPEN-a…OPEN-e dalam
  `interaction-patterns-v0.md` §4.
