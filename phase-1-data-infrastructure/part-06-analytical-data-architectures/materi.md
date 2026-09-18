# Analytical Data Architectures

**Fase:** 1 — Data Infrastructure  
**Section:** Data Architecture, Pipeline & Governance

> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18
> Diverifikasi: Apache Spark v4.2.0 — sumber: https://spark.apache.org/releases/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan OLTP dan OLAP berdasarkan workload;
- membandingkan warehouse, data lake, dan lakehouse;
- merancang star schema dengan fact dan dimension;
- memilih partitioning, clustering, dan materialization berdasarkan query;
- menjelaskan trade-off consistency, cost, governance, dan latency.

## Konteks di PT Kirimin

Database transaksi Kirimin harus tetap responsif ketika analyst menjalankan laporan berat. Reza meminta architecture decision record untuk memisahkan workload operasional dari analytical workload.

## Konsep kunci

### OLTP versus OLAP

**Definisi teknis:** OLTP mengoptimalkan transaksi kecil dengan concurrency dan consistency tinggi; OLAP mengoptimalkan scan dan agregasi atas volume besar. Menjalankan keduanya pada engine yang sama tanpa workload isolation dapat menyebabkan contention.

**Penjelasan sederhana:** Kasir perlu mencatat satu pembelian cepat, sedangkan analyst perlu menghitung penjualan setahun. Keduanya membutuhkan tata letak gudang yang berbeda.

### Warehouse, lake, dan lakehouse

**Definisi teknis:** Warehouse menyediakan storage dan execution terstruktur dengan schema-on-write; lake menyimpan data beragam dengan fleksibilitas lebih tinggi; lakehouse menggabungkan fleksibilitas lake dengan table format, governance, dan query semantics yang lebih terkelola.

**Penjelasan sederhana:** Warehouse seperti toko dengan rak dan label ketat; lake seperti gudang bahan mentah; lakehouse mencoba memberi rak dan katalog pada gudang yang fleksibel.

### Star schema

**Definisi teknis:** Star schema memiliki fact table pada grain terdefinisi dan dimension table untuk atribut deskriptif. Denormalisasi terkontrol mengurangi join saat analitik.

**Penjelasan sederhana:** Fact adalah buku transaksi; dimension adalah kamus tentang siapa, kapan, di mana, dan produk apa.

### Partitioning dan materialization

**Definisi teknis:** Partitioning membagi data menurut key seperti tanggal agar engine dapat melakukan pruning. Materialized view menyimpan hasil query yang mahal untuk mempercepat konsumsi dengan trade-off freshness dan storage.

**Penjelasan sederhana:** Anda tidak membuka semua kotak tahun lalu ketika hanya mencari paket hari ini.

## Keputusan arsitektur Kirimin

Mulai dengan PostgreSQL read replica atau analytical schema untuk skala awal; gunakan object storage + Spark/lakehouse ketika volume dan variasi data menuntut. Keputusan harus didasarkan pada query pattern, freshness, compliance, skill tim, dan biaya operasional.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| PostgreSQL | 18.6 | OLTP dan contoh analytical schema |
| Apache Spark | 4.2.0 | processing skala besar |

## Referensi resmi

- [PostgreSQL table partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)
- [Spark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [AWS analytics lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html)

## Lanjut ke praktik

Notebook membangun fact/dimension kecil dan mensimulasikan query per tanggal. Assignment meminta ADR yang membandingkan minimal dua pilihan architecture.

## Posisi part dalam bootcamp

Part ini menjawab pertanyaan: setelah data berhasil diproses, di mana data disimpan dan bagaimana konsumen menggunakannya? Anda akan membawa output curated dari Part 5 ke model analitik yang stabil. Keputusan arsitektur di sini memengaruhi BI, AI retrieval, biaya, dan kemampuan audit pada fase selanjutnya.

## Kapan konsep ini dipakai

Gunakan normalized model untuk transaksi dan konsistensi update. Gunakan dimensional model ketika analyst membutuhkan fakta dan dimensi yang mudah di-query. Gunakan lake/lakehouse ketika menyimpan raw dan berbagai bentuk data pada skala besar. Pilih storage berdasarkan pola akses, freshness, retention, governance, dan cost, bukan nama produk.

## Walkthrough terpandu: model shipment operations

1. Mulai dari pertanyaan KPI: backlog, on-time delivery, dan revenue per merchant. Tuliskan grain masing-masing.
2. Bentuk fact_order dengan satu baris per order dan fact_shipment_event dengan satu baris per event.
3. Bentuk dim_date, dim_city, dim_merchant, dan dim_status. Tetapkan natural key, surrogate key, dan aturan perubahan atribut.
4. Buat mart_daily_city dengan satu baris per city-date untuk dashboard. Simpan definisi metric di kontrak, termasuk denominator.
5. Uji double counting: total order pada fact_order harus sama dengan total order unik di mart, sedangkan event count boleh lebih besar.
6. Dokumentasikan late event, backfill, timezone, retention raw, serta konsumen yang boleh membaca PII.
7. Bandingkan model star schema dengan wide table dan jelaskan trade-off query simplicity versus duplication.

## Latihan terbimbing

- Rancang schema untuk pertanyaan merchant weekly performance.
- Tambahkan SCD Type 2 sederhana untuk perubahan zona layanan merchant.
- Tulis data contract untuk fact_shipment_event.
- Tentukan partition dan clustering key untuk tabel event.
- Buat lineage dari raw file sampai dashboard KPI.

## Checkpoint penguasaan

Anda siap lanjut jika setiap tabel memiliki grain, key, owner, freshness, dan retention yang jelas serta Anda dapat menunjukkan mengapa sebuah metric tidak double counted.

## Jembatan ke assignment

Assignment harus menghasilkan ERD atau schema diagram, DDL, sample data, metric contract, dan ADR yang membandingkan minimal dua pilihan arsitektur. Sertakan query validasi grain dan lineage table.
