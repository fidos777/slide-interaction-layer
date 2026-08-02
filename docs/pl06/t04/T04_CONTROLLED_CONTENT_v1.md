# T04_CONTROLLED_CONTENT — v1

Stage 4.2F-B0. Generated from `docs/pl06/t04/tools/t04_emit_v1.py` — do not hand-edit. Every row is read from `T04_SOURCE_EXTRACT_v1.json`.

```
UNIT            = K5-PL06-T04-B01
LESSON          = Penjagaan dan Penyelenggaraan
MODULE PAGES    = 276-283
SUBTOPICS       = 4.1 Landskap Lembut + 4.2 Landskap Kejur
CONTENT ROWS    = 100
AUTHORITY       = MODULE_SOURCE_ATTESTED (all rows)
VERDICT         = T04_SOURCE_COMPLETE_PENDING_TARGETED_INSTRUCTIONAL_DECISIONS
```

# 1. Boundary

| field | value |
|---|---|
| raw start anchor | `PENJAAGAAN DAN PENYELENGGARAAN` |
| governed display label | `PENJAGAAN DAN PENYELENGGARAAN` |
| normalisation status | **RECORDED_NOT_SILENTLY_CORRECTED** |
| normalisation authority | K5-STR-005 table of contents, per the frozen boundary map; REFERENCED_NOT_FROZEN — the artifact is not in custody |
| raw stop anchor | `PENGURUSAN KUALITI PROJEK` (excluded) |
| paragraph span | 5220 to before 5360 |
| module pages | 276–283 |

**The misspelled heading is the anchor.** Searching the body for the correctly spelled `PENJAGAAN DAN PENYELENGGARAAN` returns 0 body headings — the only match in the document is the table-of-contents entry, which is not a section start. An extraction driven from the governed label would find nothing.

## 1.1 The paragraph index is enumeration-dependent

The frozen map's 5220 and 5360 hold under **one** enumeration: direct `<w:p>` children of `<w:body>` — python-docx `Document.paragraphs` — which **excludes paragraphs nested inside tables**. Counting every `<w:p>` in the body instead gives **6534** and **6674** — the same 140-paragraph span, shifted by 1314.

Both are recorded in the extract. Extraction walks **body children** between the two anchor elements, not the index, so a table inside the boundary would be captured even though the index that located the boundary cannot see one. There are none — measured, not assumed.

# 2. Totals

| metric | value |
|---|---|
| body_elements_in_span | 140 |
| empty_spacing_paragraphs | 40 |
| content_rows | 100 |
| headings | 49 |
| paragraphs | 38 |
| numbered_paragraphs | 61 |
| list_item_rows | 12 |
| tables | 0 |
| diagrams | 1 |
| raster_images | 0 |
| assets | 1 |

# 3. Structure

| level | heading | module page |
|---|---|---|
| H1 | PENJAGAAN DAN PENYELENGGARAAN | 276 |
| H2 | Landskap Lembut | 276 |
| H2 | Landskap Kejur | 280 |

Below the two Heading-2 blocks sit 46 Heading-3 rows. Landskap Lembut decomposes into three maintenance operations — **Siram**, **Baja**, **Racun** — each with a definition, a *Kaedah Pelaksanaan* block and an *Aspek Pengurusan untuk Kontraktor* block. Landskap Kejur decomposes into four function groups, each with two sub-items.

# 4. Every row

| row_id | seq | type | page | heading path | controlled display text |
|---|---|---|---|---|---|
| `T04-ROW-001` | 1 | HEADING_1 | 276 | PENJAAGAAN DAN PENYELENGGARAAN | PENJAGAAN DAN PENYELENGGARAAN |
| `T04-ROW-002` | 2 | PARAGRAPH | 276 | PENJAAGAAN DAN PENYELENGGARAAN | Secara umumnya, berikut ialah aliran proses penjagaan dan penyelenggaran yang terlibat di dalam kerja pembinaan landskap luar: |
| `T04-ROW-003` | 3 | DIAGRAM | 276 | PENJAAGAAN DAN PENYELENGGARAAN | — |
| `T04-ROW-004` | 4 | HEADING_2 | 276 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut | Landskap Lembut |
| `T04-ROW-005` | 5 | PARAGRAPH | 276 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut | Landskap lembut merujuk kepada semua elemen hortikultur atau hidupan dalam sesebuah projek landskap. Ini termasuk pokok, palma, pokok renek, penutup b |
| `T04-ROW-006` | 6 | HEADING_3 | 276 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Siram | Siram |
| `T04-ROW-007` | 7 | PARAGRAPH | 276 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Siram | Membekalkan kuantiti air yang mencukupi untuk kelangsungan hidup dan proses fisiologi tumbuhan (fotosintesis, penyerapan nutrien), terutamanya bagi ta |
| `T04-ROW-008` | 8 | HEADING_3 | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kaedah Pelaksanaan | Kaedah Pelaksanaan |
| `T04-ROW-009` | 9 | HEADING_3 | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Penyiraman Manual | Penyiraman Manual |
| `T04-ROW-010` | 10 | PARAGRAPH | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Penyiraman Manual | Menggunakan hos getah dengan muncung semburan (nozzle). Kaedah ini fleksibel tetapi memerlukan tenaga kerja yang ramai dan kurang konsisten. |
| `T04-ROW-011` | 11 | HEADING_3 | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Sistem Pengairan Automatik | Sistem Pengairan Automatik |
| `T04-ROW-012` | 12 | LIST_ITEM | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Sistem Pengairan Automatik | Sistem Semburan (Sprinkler System) |
| `T04-ROW-013` | 13 | PARAGRAPH | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Sistem Pengairan Automatik | Sesuai untuk kawasan rumput yang luas. |
| `T04-ROW-014` | 14 | LIST_ITEM | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Sistem Pengairan Automatik | Sistem Titis (Drip Irrigation System) |
| `T04-ROW-015` | 15 | PARAGRAPH | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Sistem Pengairan Automatik | Sangat efisien untuk pokok individu atau pokok renek kerana ia membekalkan air terus ke zon akar, mengurangkan pembaziran air melalui penyejatan. |
| `T04-ROW-016` | 16 | HEADING_3 | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Aspek Pengurusan untuk Kontraktor: | Aspek Pengurusan untuk Kontraktor: |
| `T04-ROW-017` | 17 | HEADING_3 | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Jadual Penyiraman | Jadual Penyiraman |
| `T04-ROW-018` | 18 | LIST_ITEM | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Jadual Penyiraman | Membangunkan jadual kerja penyiraman yang sistematik. Amalan terbaik adalah menyiram pada awal pagi atau lewat petang untuk meminimumkan kehilangan ai |
| `T04-ROW-019` | 19 | LIST_ITEM | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Jadual Penyiraman | Kekerapan dan kuantiti siraman mesti disesuaikan mengikut jenis tanaman, keadaan cuaca, dan peringkat tumbesaran. Tanaman baru memerlukan siraman lebi |
| `T04-ROW-020` | 20 | HEADING_3 | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pengurusan Sumber Air | Pengurusan Sumber Air |
| `T04-ROW-021` | 21 | PARAGRAPH | 277 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pengurusan Sumber Air | Memastikan sumber air mencukupi dan tekanan air memadai untuk keseluruhan tapak. Sekiranya menggunakan sistem automatik, kontraktor bertanggungjawab u |
| `T04-ROW-022` | 22 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pemantauan & Pelaporan | Pemantauan & Pelaporan |
| `T04-ROW-023` | 23 | PARAGRAPH | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pemantauan & Pelaporan | Pekerja perlu dilatih untuk mengenal pasti tanda-tanda kekurangan air (daun layu, kering) atau terlebih air (daun kuning, akar reput). Aktiviti penyir |
| `T04-ROW-024` | 24 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kecekapan Kos | Kecekapan Kos |
| `T04-ROW-025` | 25 | PARAGRAPH | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kecekapan Kos | Mengoptimumkan kaedah penyiraman untuk mengawal kos bil air, terutamanya dalam projek berskala besar. |
| `T04-ROW-026` | 26 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Baja | Baja |
| `T04-ROW-027` | 27 | PARAGRAPH | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Baja | Membekalkan nutrien penting yang mungkin kurang di dalam tanah untuk merangsang pertumbuhan yang sihat, pengeluaran bunga/buah, dan meningkatkan daya  |
| `T04-ROW-028` | 28 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kaedah Pelaksanaan | Kaedah Pelaksanaan |
| `T04-ROW-029` | 29 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pembajaan Tabur (Broadcasting) | Pembajaan Tabur (Broadcasting) |
| `T04-ROW-030` | 30 | PARAGRAPH | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pembajaan Tabur (Broadcasting) | Menabur baja butiran (granular) secara rata di sekeliling zon akar tumbuhan atau di atas permukaan rumput. |
| `T04-ROW-031` | 31 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pembajaan Poket (Pocketing) | Pembajaan Poket (Pocketing) |
| `T04-ROW-032` | 32 | PARAGRAPH | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pembajaan Poket (Pocketing) | Menggali lubang-lubang kecil di sekeliling zon akar pokok, memasukkan baja, dan menutupnya kembali. Kaedah ini lebih berkesan untuk pokok besar. |
| `T04-ROW-033` | 33 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Semburan Folia (Foliar Spray) | Semburan Folia (Foliar Spray) |
| `T04-ROW-034` | 34 | PARAGRAPH | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Semburan Folia (Foliar Spray) | Menyembur baja cecair terus ke daun untuk penyerapan nutrien yang pantas. |
| `T04-ROW-035` | 35 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Aspek Pengurusan untuk Kontraktor | Aspek Pengurusan untuk Kontraktor |
| `T04-ROW-036` | 36 | HEADING_3 | 278 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Program Pembajaan | Program Pembajaan |
| `T04-ROW-037` | 37 | PARAGRAPH | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Program Pembajaan | Merancang program pembajaan yang mematuhi spesifikasi kontrak. Program ini perlu menyatakan jenis baja (organik atau kimia), kadar NPK, kuantiti, dan  |
| `T04-ROW-038` | 38 | HEADING_3 | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pematuhan Spesifikasi | Pematuhan Spesifikasi |
| `T04-ROW-039` | 39 | PARAGRAPH | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pematuhan Spesifikasi | Memastikan baja yang digunakan adalah seperti yang ditetapkan dalam dokumen kontrak atau diluluskan oleh Pegawai Penguasa (S.O.). Penggunaan baja yang |
| `T04-ROW-040` | 40 | HEADING_3 | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pengurusan Stok dan Penyimpanan | Pengurusan Stok dan Penyimpanan |
| `T04-ROW-041` | 41 | PARAGRAPH | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pengurusan Stok dan Penyimpanan | Baja mesti disimpan di tempat yang kering, selamat, dan jauh dari sumber air untuk mengelakkan pencemaran. |
| `T04-ROW-042` | 42 | HEADING_3 | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan Pekerja | Keselamatan Pekerja |
| `T04-ROW-043` | 43 | PARAGRAPH | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan Pekerja | Memastikan pekerja menggunakan Peralatan Pelindung Diri (PPE) yang sesuai seperti sarung tangan dan topeng muka semasa mengendalikan baja kimia. |
| `T04-ROW-044` | 44 | HEADING_3 | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Dokumentasi | Dokumentasi |
| `T04-ROW-045` | 45 | PARAGRAPH | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Dokumentasi | Merekodkan tarikh, jenis baja, kuantiti yang digunakan, dan kawasan yang telah dibaja. Ini penting sebagai bukti kerja untuk tuntutan bayaran dan ruju |
| `T04-ROW-046` | 46 | HEADING_3 | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Racun | Racun |
| `T04-ROW-047` | 47 | PARAGRAPH | 279 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Racun | Mengawal dan mengurus serangan perosak (serangga), penyakit (kulat), dan pertumbuhan rumpai yang boleh menjejaskan kesihatan dan estetika landskap lem |
| `T04-ROW-048` | 48 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › IPM memberi keutamaan kepada: | IPM memberi keutamaan kepada: |
| `T04-ROW-049` | 49 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kawalan Kultur | Kawalan Kultur |
| `T04-ROW-050` | 50 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kawalan Kultur | Amalan penyelenggaraan yang baik (penyiraman, pembajaan seimbang). |
| `T04-ROW-051` | 51 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kawalan Fizikal | Kawalan Fizikal |
| `T04-ROW-052` | 52 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kawalan Fizikal | Membuang bahagian berpenyakit secara manual, mencabut rumpai. |
| `T04-ROW-053` | 53 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kawalan Biologi | Kawalan Biologi |
| `T04-ROW-054` | 54 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kawalan Biologi | Menggunakan musuh semula jadi kepada perosak. |
| `T04-ROW-055` | 55 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kawalan Kimia | Kawalan Kimia |
| `T04-ROW-056` | 56 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Kawalan Kimia | Penggunaan racun secara terkawal dan bersasar. |
| `T04-ROW-057` | 57 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Jenis Racun | Jenis Racun |
| `T04-ROW-058` | 58 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Racun Serangga (Insecticide) | Racun Serangga (Insecticide) |
| `T04-ROW-059` | 59 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Racun Serangga (Insecticide) | Untuk mengawal serangga perosak. |
| `T04-ROW-060` | 60 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Racun Kulat (Fungicide) | Racun Kulat (Fungicide) |
| `T04-ROW-061` | 61 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Racun Kulat (Fungicide) | Untuk mengawal penyakit disebabkan kulat. |
| `T04-ROW-062` | 62 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Racun Rumpai (Herbicide) | Racun Rumpai (Herbicide) |
| `T04-ROW-063` | 63 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Racun Rumpai (Herbicide) | Untuk mengawal pertumbuhan rumpai. |
| `T04-ROW-064` | 64 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Aspek Pengurusan untuk Kontraktor: | Aspek Pengurusan untuk Kontraktor: |
| `T04-ROW-065` | 65 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Perundangan dan Pelesenan | Perundangan dan Pelesenan |
| `T04-ROW-066` | 66 | LIST_ITEM | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Perundangan dan Pelesenan | Penggunaan racun kimia dikawal oleh Akta Racun Makhluk Perosak 1974. |
| `T04-ROW-067` | 67 | LIST_ITEM | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Perundangan dan Pelesenan | Kontraktor mesti memastikan pekerja yang menjalankan semburan racun adalah pengendali racun berlesen atau sekurang-kurangnya telah menerima latihan da |
| `T04-ROW-068` | 68 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan dan Kesihatan (HSE) | Keselamatan dan Kesihatan (HSE) |
| `T04-ROW-069` | 69 | LIST_ITEM | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan dan Kesihatan (HSE) | PPE Lengkap |
| `T04-ROW-070` | 70 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan dan Kesihatan (HSE) | Memastikan pekerja memakai PPE yang lengkap dan bersesuaian (topeng pernafasan, cermin mata keselamatan, sarung tangan kimia, sut pelindung). |
| `T04-ROW-071` | 71 | LIST_ITEM | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan dan Kesihatan (HSE) | Penyimpanan & Pelupusan |
| `T04-ROW-072` | 72 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan dan Kesihatan (HSE) | Racun mesti disimpan di dalam stor berkunci, berlabel, dan mempunyai pengudaraan yang baik. Bekas racun kosong tidak boleh digunakan semula dan mesti  |
| `T04-ROW-073` | 73 | LIST_ITEM | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan dan Kesihatan (HSE) | Helaian Data Keselamatan (SDS) |
| `T04-ROW-074` | 74 | PARAGRAPH | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Keselamatan dan Kesihatan (HSE) | Kontraktor wajib menyimpan Salinan SDS untuk setiap racun yang digunakan di tapak dan memastikan pekerja memahaminya. |
| `T04-ROW-075` | 75 | HEADING_3 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pengurusan Risiko | Pengurusan Risiko |
| `T04-ROW-076` | 76 | LIST_ITEM | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pengurusan Risiko | Semburan hanya boleh dilakukan semasa cuaca tenang (tidak berangin) untuk mengelakkan spray drift. |
| `T04-ROW-077` | 77 | LIST_ITEM | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pengurusan Risiko | Maklumkan kepada pihak pengurusan bangunan atau penduduk sekitar sebelum aktiviti semburan dijalankan. Letakkan papan tanda amaran di kawasan kerja. |
| `T04-ROW-078` | 78 | LIST_ITEM | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Lembut › Pengurusan Risiko | Pelaporan: Menyimpan rekod lengkap bagi setiap aktiviti semburan, termasuk: tarikh, lokasi, jenis racun, kadar bancuhan, nama pengendali, dan keadaan  |
| `T04-ROW-079` | 79 | HEADING_2 | 280 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur | Landskap Kejur |
| `T04-ROW-080` | 80 | PARAGRAPH | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur | Landskap Kejur merujuk kepada semua elemen binaan yang bukan hidup dan bersifat kekal dalam reka bentuk landskap. Ia membentuk struktur, rangka, dan ' |
| `T04-ROW-081` | 81 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Pengurusan Ruang dan Sirkulasi | Pengurusan Ruang dan Sirkulasi |
| `T04-ROW-082` | 82 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Membentuk Ruang | Membentuk Ruang |
| `T04-ROW-083` | 83 | PARAGRAPH | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Membentuk Ruang | Dinding, pagar, dan perubahan aras lantai digunakan untuk membahagikan ruang luaran kepada "bilik" yang berbeza (cth., kawasan rehat, kawasan permaina |
| `T04-ROW-084` | 84 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Laluan Pergerakan | Laluan Pergerakan |
| `T04-ROW-085` | 85 | PARAGRAPH | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Laluan Pergerakan | Lorong pejalan kaki (pathways), jalan masuk (driveways), dan tangga menyediakan laluan yang selamat dan jelas untuk pergerakan manusia dan kenderaan. |
| `T04-ROW-086` | 86 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Fungsi Struktur dan Kejuruteraan | Fungsi Struktur dan Kejuruteraan |
| `T04-ROW-087` | 87 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Menstabilkan Tanah | Menstabilkan Tanah |
| `T04-ROW-088` | 88 | PARAGRAPH | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Menstabilkan Tanah | Dinding penahan (retaining walls) dibina untuk menahan tanah di kawasan bercerun, mengelakkan hakisan dan tanah runtuh. |
| `T04-ROW-089` | 89 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Pengurusan Air | Pengurusan Air |
| `T04-ROW-090` | 90 | PARAGRAPH | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Pengurusan Air | Parit, longkang, dan permukaan yang dicerunkan dengan betul (properly graded surfaces) adalah penting untuk menguruskan aliran air larian permukaan. |
| `T04-ROW-091` | 91 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Kebolehgunaan dan Kemudahan | Kebolehgunaan dan Kemudahan |
| `T04-ROW-092` | 92 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Menyediakan Permukaan Rata | Menyediakan Permukaan Rata |
| `T04-ROW-093` | 93 | PARAGRAPH | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Menyediakan Permukaan Rata | Laman (patios), dek (decks), dan dataran (plazas) menyediakan permukaan yang stabil dan selesa untuk aktiviti seperti meletakkan perabot luar, barbeku |
| `T04-ROW-094` | 94 | HEADING_3 | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Menyediakan Kemudahan | Menyediakan Kemudahan |
| `T04-ROW-095` | 95 | PARAGRAPH | 281 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Menyediakan Kemudahan | Struktur seperti wakaf, gazebo, pergola, bangku, dan lampu landskap meningkatkan keselesaan dan kebolehgunaan ruang pada waktu yang berbeza. |
| `T04-ROW-096` | 96 | HEADING_3 | 282 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Estetika dan Reka Bentuk | Estetika dan Reka Bentuk |
| `T04-ROW-097` | 97 | HEADING_3 | 282 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Menambah Tekstur, Warna, dan Corak | Menambah Tekstur, Warna, dan Corak |
| `T04-ROW-098` | 98 | PARAGRAPH | 282 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Menambah Tekstur, Warna, dan Corak | Penggunaan bahan seperti batu, kayu, dan konkrit menambah dimensi visual kepada landskap. |
| `T04-ROW-099` | 99 | HEADING_3 | 282 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Mencipta Kontras | Mencipta Kontras |
| `T04-ROW-100` | 100 | PARAGRAPH | 282 | PENJAAGAAN DAN PENYELENGGARAAN › Landskap Kejur › Mencipta Kontras | Elemen kejur memberikan kontras yang menarik kepada kelembutan elemen tumbuhan. |

Every row carries `authority_class = MODULE_SOURCE_ATTESTED`. Nothing in this unit is BARIAH_DIRECT: she has ruled on B02's treatment, not on T04's content.
