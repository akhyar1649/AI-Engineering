# Storage Strategy, Capacity Planning & Cost Management

**Fase:** 1 — Data Infrastructure  
**Section:** NoSQL & Storage Strategy

> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18
> Diverifikasi: MongoDB v8.3 series — sumber: https://www.mongodb.com/docs/manual/release-notes/ — tanggal cek: 2026-09-18
> Diverifikasi: Databricks Runtime v19 — sumber: https://docs.databricks.com/aws/en/release-notes/runtime/19 — tanggal cek: 2026-09-18

## Tujuan belajar

- menghitung kapasitas berdasarkan volume, growth, retention, replication, dan overhead;
- memilih storage tier berdasarkan access frequency dan recovery need;
- membuat model biaya dengan asumsi transparan;
- merancang retention, archival, deletion, dan restore test;
- menghubungkan capacity plan dengan SLO dan budget guardrail.

## Konteks di PT Kirimin

Tracking event bertambah setiap hari, raw file harus disimpan untuk audit, dan dashboard hanya membaca agregasi. Reza meminta storage strategy yang tidak menyimpan semua data panas selamanya.

## Konsep kunci

### Capacity formula

**Definisi teknis:** Kapasitas efektif memperhitungkan records/day × bytes/record × retention × replication × overhead, lalu dibandingkan dengan headroom dan growth scenario.

**Penjelasan sederhana:** Menyewa gudang berdasarkan barang hari ini tanpa menghitung pertumbuhan dan ruang jalan akan membuat gudang cepat penuh.

### Tiering dan lifecycle

**Definisi teknis:** Hot tier mengoptimalkan latency; warm/cold/archive mengurangi cost dengan retrieval trade-off. Lifecycle policy memindahkan atau menghapus data berdasarkan umur dan policy.

**Penjelasan sederhana:** Paket yang sering dicari ditaruh dekat meja; arsip lama dipindah ke gudang yang lebih murah tetapi lebih lambat diambil.

### Cost allocation

**Definisi teknis:** Cost allocation menggunakan tags/labels dan unit economics seperti cost per million events atau cost per dashboard refresh. Forecast harus menyebut uncertainty dan sensitivity.

**Penjelasan sederhana:** Jangan hanya tahu total sewa; tahu juga biaya per paket agar dapat melihat proses mana yang boros.

### Recovery dan deletion

**Definisi teknis:** Backup, restore point objective, recovery time objective, retention, legal hold, dan deletion verification menentukan lifecycle data. Backup yang tidak pernah diuji bukan bukti recoverability.

**Penjelasan sederhana:** Memiliki salinan kunci tidak berarti Anda pernah mencoba membuka pintu dengan salinan itu.

## Contoh hitungan

Jika 80.000 event/hari × 1,2 KB × 90 hari × replication 3 = sekitar 25,9 GB payload sebelum index, metadata, compression, dan headroom. Angka aktual harus diukur dari sample produksi sintetis.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| PostgreSQL | 18.6 | serving/relational storage |
| MongoDB | 8.3 series | event document storage |
| Databricks Runtime | 19 | contoh lakehouse processing |

## Referensi resmi

- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html)
- [MongoDB backup and restore](https://www.mongodb.com/docs/manual/core/backups/)
- [Databricks Runtime 19 release notes](https://docs.databricks.com/aws/en/release-notes/runtime/19)

## Lanjut ke praktik

Notebook menghitung capacity scenario dan sensitivity. Assignment meminta storage decision record, lifecycle policy, dan cost guardrail.

## Posisi part dalam bootcamp

Part ini menutup Fase 1 dengan keputusan kapasitas dan biaya. Semua artifact sebelumnya menjadi input: volume generator, retention, partition, query pattern, quality evidence, dan deployment model. Anda akan belajar membela desain berdasarkan angka dan asumsi, bukan preferensi tool.

## Kapan konsep ini dipakai

Gunakan capacity planning sebelum volume naik, SLO berubah, atau provider dipilih. Gunakan cost model ketika membandingkan managed service, self-hosted, storage tier, dan retention. Model harus memiliki scenario dan sensitivity analysis karena volume serta harga dapat berubah.

## Walkthrough terpandu: forecast tiga skenario

1. Ambil baseline: order per hari, event per order, row size, retry rate, raw/curated retention, query frequency, dan peak multiplier.
2. Hitung storage bulanan untuk raw, curated, index, backup, dan log. Tulis asumsi kompresi dan overhead.
3. Hitung compute berdasarkan run duration, worker size, concurrency, dan backfill frequency.
4. Buat tiga scenario low, base, high. Ubah satu asumsi pada satu waktu untuk melihat sensitivitas.
5. Hubungkan capacity ke SLO: jika morning dashboard harus siap pukul 07.00, berapa processing window dan headroom yang dibutuhkan?
6. Bandingkan tiga desain: single database, managed warehouse, dan object storage plus query engine.
7. Tambahkan budget alert, owner, retention enforcement, dan trigger review saat forecast melewati threshold.

## Latihan terbimbing

- Buat spreadsheet atau script cost model yang dapat mengubah input.
- Hitung pengaruh duplicate event 5 persen terhadap storage dan compute.
- Bandingkan hot versus cold retention.
- Rancang capacity test dari generator 10.000 sampai 1.000.000 order.
- Tulis recommendation memo dengan trade-off dan batas keyakinan.

## Checkpoint penguasaan

Anda siap masuk Capstone 1 jika dapat menelusuri setiap angka cost ke asumsi, menunjukkan headroom terhadap SLO, dan menyebut kapan model harus diperbarui.

## Jembatan ke assignment

Assignment harus berisi capacity model, tiga scenario, sensitivity table, cost assumptions, SLO mapping, recommendation memo, dan trigger governance. Gunakan synthetic data dan catat harga/provider yang perlu diverifikasi ulang.
