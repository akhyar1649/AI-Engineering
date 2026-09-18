# Advanced SQL

**Fase:** 1 — Data Infrastructure  
**Section:** Foundations

> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menyusun query kompleks dengan CTE yang mudah diaudit;
- memakai window function untuk ranking, deduplikasi, dan running metric;
- memilih correlated subquery, join, atau window sesuai kebutuhan;
- menangani waktu, `NULL`, dan conditional aggregation;
- membaca `EXPLAIN` sebagai langkah awal troubleshooting performa.

## Konteks di PT Kirimin

Dinda perlu SLA shipment per kota dan daftar order yang berada pada percentile nilai tertinggi. Query dasar sudah ada, tetapi laporan mulai lambat dan hasilnya mudah salah ketika satu order memiliki banyak event.

## Konsep kunci

### CTE

**Definisi teknis:** Common Table Expression (`WITH`) memberi nama pada relation sementara dalam satu statement. CTE membantu memisahkan tahap deduplikasi, enrichment, dan agregasi, meskipun optimizer tetap menentukan rencana eksekusi.

**Penjelasan sederhana:** CTE adalah meja kerja bernama. Anda menyelesaikan satu tahap, memberi label, lalu memakai hasilnya di tahap berikutnya tanpa menjejalkan semua logika dalam satu baris.

### Window function

**Definisi teknis:** Window function menghitung nilai lintas baris yang berhubungan tanpa mereduksi baris seperti `GROUP BY`. `ROW_NUMBER`, `RANK`, `LAG`, dan `SUM() OVER` berguna untuk latest record, perubahan status, dan running total.

**Penjelasan sederhana:** Anda tetap melihat setiap event, tetapi juga dapat melihat urutan event, event sebelumnya, atau posisi event dalam kelompoknya.

### Query plan

**Definisi teknis:** `EXPLAIN` menampilkan rencana operator seperti sequential scan, index scan, join strategy, estimasi rows, dan cost. `EXPLAIN ANALYZE` menjalankan query sehingga harus dipakai hati-hati pada operasi yang mengubah data.

**Penjelasan sederhana:** Query plan adalah rute yang dipilih database. Untuk tabel besar, Anda ingin tahu apakah database membuka index yang tepat atau membaca seluruh gudang.

## Pola query Kirimin

Gunakan CTE `latest_events`, lalu hitung durasi antara `picked_up` dan `delivered` dengan `LAG` atau conditional aggregation. Untuk ranking merchant, gunakan `DENSE_RANK` dan dokumentasikan ties.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| PostgreSQL | 18.6 | CTE, window function, dan `EXPLAIN` |
| Python | 3.14.7 | notebook fallback |

## Referensi resmi

- [PostgreSQL window functions](https://www.postgresql.org/docs/current/tutorial-window.html)
- [PostgreSQL `WITH`](https://www.postgresql.org/docs/current/queries-with.html)
- [PostgreSQL `EXPLAIN`](https://www.postgresql.org/docs/current/using-explain.html)

## Lanjut ke praktik

Notebook memperlihatkan latest status dan running total dengan SQLite-compatible SQL. Assignment meminta Anda menambahkan metrik SLA dan menjelaskan rencana eksekusi PostgreSQL.

## Posisi part dalam bootcamp

Part ini memakai grain dari Part 1 dan disiplin validasi dari Part 2 untuk menjawab pertanyaan yang memerlukan urutan waktu dan transformasi bertahap. Anda akan menghasilkan query yang mudah diaudit, bukan query pendek yang sulit dibuktikan. Hasilnya menjadi dasar serving table di Part 5 dan metrik operasional di Part 7.

## Kapan konsep ini dipakai

Gunakan CTE ketika query memiliki tahapan yang perlu diberi nama: memilih latest event, menghitung durasi, kemudian mengagregasi. Gunakan window function ketika baris perlu dibandingkan dengan baris lain tanpa menghilangkan detail. Gunakan EXPLAIN saat data membesar atau query dipakai berulang. Hindari EXPLAIN ANALYZE pada statement yang mengubah data kecuali efeknya dipahami.

## Walkthrough terpandu: SLA pickup-to-delivery

1. Definisikan SLA: durasi dari event picked_up ke delivered, dalam timezone yang sama. Event yang hilang tidak boleh diperlakukan sebagai durasi nol.
2. Buat CTE ordered_events yang memberi ROW_NUMBER per order_id berdasarkan event_at descending, lalu pilih rn = 1 untuk latest status.
3. Buat CTE event_times dengan conditional aggregation untuk mengambil timestamp picked_up dan delivered per order.
4. Hitung delivery_hours hanya jika kedua timestamp ada dan delivered_at tidak lebih awal dari picked_up_at. Tandai anomaly jika urutannya terbalik.
5. Gunakan LAG untuk menghitung perubahan status sebelumnya dan mendeteksi lompatan status yang tidak diizinkan.
6. Agregasikan satu baris per kota: total order, delivered_count, missing_event_count, anomaly_count, serta p95 approximation yang definisinya ditulis.
7. Jalankan EXPLAIN pada query raw join dan query yang telah mereduksi event lebih dahulu. Bandingkan scan, join, estimated rows, dan index yang diperlukan.

## Latihan terbimbing

- Ranking merchant berdasarkan on-time delivery dengan aturan ties yang eksplisit.
- Running total nilai order per hari menggunakan SUM OVER.
- Deduplikasi event dengan tie-breaker event_at lalu ingestion_at.
- Buat quality_status untuk complete, missing_event, dan invalid_sequence.
- Tulis dua versi query, CTE dan nested subquery, lalu jelaskan mana yang lebih dapat diaudit dan mengapa.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjelaskan perbedaan GROUP BY dan window function, menghasilkan satu baris per order dari banyak event, dan membaca EXPLAIN untuk menemukan kemungkinan row explosion atau full scan.

## Jembatan ke assignment

Assignment harus menyertakan advanced_queries.sql, fixture data kecil, expected result, dan explain.md. Dokumentasikan definisi SLA, timezone, missing event, anomaly, tie-breaker, serta bukti bahwa query tidak menggandakan nilai order.
