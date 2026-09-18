# NoSQL Concepts: Reliability & Scalability

**Fase:** 1 — Data Infrastructure  
**Section:** NoSQL & Storage Strategy

> Diverifikasi: MongoDB v8.3 series — sumber: https://www.mongodb.com/docs/manual/release-notes/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membandingkan key-value, document, wide-column, graph, dan relational model;
- memilih model berdasarkan access pattern, bukan popularitas;
- menjelaskan replication, partitioning, consistency, dan availability;
- mengenali hot key, unbounded document, dan duplicate write;
- menyusun reliability checklist untuk storage NoSQL.

## Konteks di PT Kirimin

Shipment tracking menghasilkan event cepat dan bentuk payload dapat berubah. Sari perlu membaca status terbaru per shipment tanpa membebani database transaksi order.

## Konsep kunci

### Model NoSQL

**Definisi teknis:** NoSQL mencakup beberapa keluarga storage dengan trade-off schema flexibility, query model, consistency, dan scaling. Tidak ada satu model yang optimal untuk semua access pattern.

**Penjelasan sederhana:** Lemari laci, rak dokumen, dan papan relasi cocok untuk barang berbeda. Pilih berdasarkan cara Anda mencari barang.

### Replication dan consistency

**Definisi teknis:** Replication menyimpan salinan data pada beberapa node; consistency model menentukan kapan read melihat write. Strong consistency mengurangi stale read tetapi dapat meningkatkan latency/coordination.

**Penjelasan sederhana:** Memiliki beberapa gudang meningkatkan availability, tetapi butuh aturan kapan semua gudang dianggap memiliki stok yang sama.

### Partitioning dan hot key

**Definisi teknis:** Partition key menentukan distribusi data. Key yang terlalu populer membuat hot partition; key yang terlalu acak menyulitkan query range.

**Penjelasan sederhana:** Jika semua paket ditaruh di satu pintu, pintu itu menjadi macet meski gudang lain kosong.

### Denormalization

**Definisi teknis:** Denormalization menyimpan data turunan agar read pattern cepat, dengan konsekuensi duplicate data dan write coordination.

**Penjelasan sederhana:** Menulis alamat pada label setiap paket mempercepat pengiriman, tetapi perubahan alamat harus memperbarui banyak label.

## Design checklist

Mulai dari query paling sering, target latency, write/read ratio, retention, replay, backup, failure mode, dan biaya. Jangan memilih NoSQL hanya karena schema fleksibel.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| MongoDB | 8.3 series | document storage dan indexing |

## Referensi resmi

- [MongoDB data modeling](https://www.mongodb.com/docs/manual/data-modeling/)
- [MongoDB replication](https://www.mongodb.com/docs/manual/replication/)
- [MongoDB sharding](https://www.mongodb.com/docs/manual/sharding/)

## Lanjut ke praktik

Notebook memilih partition key dan memeriksa potensi hot key. Assignment meminta storage decision record.

## Posisi part dalam bootcamp

Part ini memperluas pilihan storage ketika workload event, document, atau key-value tidak cocok dipaksa ke satu model relasional. Anda akan membandingkan access pattern, consistency, partitioning, dan operational trade-off. Part 15 akan mempraktikkannya dengan MongoDB.

## Kapan konsep ini dipakai

Gunakan document store untuk data yang dibaca sebagai aggregate document dan schema berubah terkontrol. Gunakan key-value untuk lookup sederhana ber-throughput tinggi. Gunakan wide-column atau event store untuk volume dan pola partition tertentu. Jangan memilih NoSQL hanya karena schema fleksibel; desain harus dimulai dari query.

## Walkthrough terpandu: shipment timeline document

1. Tulis access pattern: ambil seluruh timeline satu order, cari event terbaru per order, dan hitung backlog per kota.
2. Tentukan document boundary. Timeline satu order dapat di-embed jika ukurannya terbatas; event tak terbatas lebih aman dipisah.
3. Pilih partition/shard key yang tidak hot, misalnya kombinasi order atau time bucket sesuai pola.
4. Tentukan consistency: status customer-facing memerlukan read-after-write pada jalur tertentu, sedangkan agregasi dapat eventual.
5. Rancang index dari query aktual dan uji selectivity.
6. Simulasikan duplicate delivery event, out-of-order event, dan retry write. Tentukan idempotency key.
7. Bandingkan implementasi document dengan fact/event relational dan tulis kapan masing-masing lebih baik.

## Latihan terbimbing

- Rancang dua schema untuk timeline kecil dan timeline besar.
- Hitung risiko hot partition jika semua query memakai city.
- Tulis retry policy yang tidak menggandakan event.
- Buat consistency decision record.
- Rancang retention dan archival untuk event lama.

## Checkpoint penguasaan

Anda siap lanjut jika schema NoSQL diturunkan dari access pattern, key dan index memiliki alasan, dan trade-off consistency, cost, serta operability tertulis.

## Jembatan ke assignment

Assignment harus menghasilkan access-pattern matrix, dua alternatif schema, index/partition rationale, failure scenario, consistency policy, dan ADR rekomendasi.
