# ADR-005 — Addendum A: Validation Empirik Ujian Komposisi
## Untuk digabung ke dalam ADR-005 (Namespace E/I/P/R) sebelum commit

| | |
|---|---|
| **Tarikh** | 5 Julai 2026 |
| **Status ADR induk** | Draf siap, belum commit (tertahan disk) |
| **Tindakan** | Append seksyen ini ke hujung ADR-005 sebagai "Addendum A" |
| **Sumber bukti** | 9 SS WhatsApp Bariah 16/06/2026 + 12 attachment penuh + raw notes AMEND-K1 |

---

## Konteks

ADR-005 menetapkan **ujian keahlian**: gubahan object + state + trigger +
feedback atas P sedia ada = **varian**, bukan P baru. Semasa digubal, ujian ini
ialah keputusan reka bentuk deduktif — kita percaya ia cara betul untuk elak
taxonomy explode, tapi tiada bukti luaran.

## Penemuan

Trace penuh sesi WhatsApp 16/06/2026 menunjukkan Bariah — tanpa pengetahuan
tentang ADR-005 — secara natural men-spec keperluan dia sebagai **komposisi
micro-behaviours**, bukan sebagai template atau widget:

```
"Any gambar/item boleh click kan.. ia bukannya click ikut turutan"
        → clickable-any-order
"Mouse over pun boleh buat highlight merah?"
        → hover-highlight
"Selepas klik (appear tick icon)"
        → visited-tick
"After all have been clicked, only unlock/enable button navigation Seterusnya"
        → unlock-on-all-visited
```

Digabungkan, "sample interactivity Click & Reveal" dia =

```
Click & Reveal  =  clickable-any-order
                 + nav-lock-until-complete
                 + hover-highlight
                 + active-highlight (merah)
                 + visited-tick
                 + unlock-on-all-visited
```

Sepanjang sesi, dia tidak sekali pun menggunakan istilah widget (modal, dialog,
overlay, accordion). Semua arahan dalam raw notes AMEND-K1 juga berbentuk
behaviour (CHANGE / ADD ON / click to reveal / changing images / POP UP +
maintain + with VO), iaitu **apa learner alami**, bukan **komponen apa
programmer guna**.

## Implikasi kepada ADR-005

1. **Status ujian keahlian dinaik taraf**: dari keputusan deduktif → keputusan
   yang disahkan secara empirik oleh cara kerja sebenar Lead ID projek.
   Instructional designer berpengalaman berfikir dalam model yang sama dengan
   model taxonomy ini.
2. **Medan baharu dicadangkan untuk skema taxonomy**: `composition[]` —
   senarai micro-behaviour bagi setiap komposisi bernama. Faedah: bila kursus
   akan datang minta variasi ("sama tapi tanpa tick"), jawapannya komposisi
   tolak satu behaviour, bukan P baharu. Ini mekanisme anti-explosion yang
   ADR-005 sasarkan, kini dengan bentuk data konkrit.
3. **Lapisan bahasa disahkan**: SB Bariah = behaviour spec; taxonomy = named
   compositions; React = implementation. Percanggahan istilah antara lapisan
   (cth "popup" SB ≠ PopupModal React; "branching out" Bariah ≠ Branching
   Scenario pedagogi) mesti diurus melalui glosari padanan — bukan dengan
   memaksa satu lapisan guna istilah lapisan lain.

## Rujukan silang

- Komposisi bernama pertama: `taxonomy/interaction-patterns-v0.md` §3.1
  (Gated Click & Reveal, [confirmed-written 16/06/2026]).
- Mekanisme yang membolehkan spec ini muncul: ADR-006 case study
  "3 clarification cycles" (artifak-sebagai-soalan).
