# Analytics and Business Intelligence

**Fase:** 1 — Data Infrastructure  
**Section:** Data Architecture, Pipeline & Governance

> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18
> Diverifikasi: Tableau release notes — sumber: https://help.tableau.com/current/tableau/en-us/whatsnew_all.htm — tanggal cek: 2026-09-18

## Tujuan belajar

- menerjemahkan pertanyaan bisnis menjadi KPI dengan definisi dan grain;
- membangun semantic layer yang mencegah metric drift;
- memilih visualisasi berdasarkan pertanyaan, bukan dekorasi;
- merancang dashboard dengan filter, freshness indicator, dan data quality note;
- mengkomunikasikan insight serta keterbatasannya kepada stakeholder.

## Konteks di PT Kirimin

Sari dan Fajar melihat angka “delivery success” yang berbeda karena definisinya tidak sama. Anda perlu membuat metric contract dan dashboard yang menunjukkan definisi, denominator, periode, serta freshness.

## Konsep kunci

### KPI dan metric contract

**Definisi teknis:** KPI adalah ukuran yang dipakai untuk menilai outcome terhadap target. Metric contract menetapkan nama, formula, grain, filter, sumber, owner, dan freshness.

**Penjelasan sederhana:** Sebelum menanyakan skor pertandingan, semua orang harus sepakat aturan menghitung gol. Kalau tidak, dua dashboard bisa sama-sama terlihat benar tetapi menghasilkan angka berbeda.

### Semantic layer

**Definisi teknis:** Semantic layer memusatkan definisi dimensi, measure, relationship, dan policy agar konsumen memakai logika yang konsisten.

**Penjelasan sederhana:** Ini seperti kamus resmi perusahaan. “Order delivered” harus memiliki satu arti di seluruh laporan.

### Visual encoding

**Definisi teknis:** Visualisasi memetakan data ke posisi, panjang, warna, atau bentuk. Pilihan encoding memengaruhi akurasi pembacaan dan risiko misleading.

**Penjelasan sederhana:** Grafik adalah bahasa. Bar chart cocok membandingkan kota; line chart cocok melihat tren; pie chart sering menyulitkan perbandingan bagian kecil.

### Dashboard sebagai produk

**Definisi teknis:** Dashboard memiliki pengguna, keputusan, refresh SLO, access control, dan maintenance cost. Ia bukan sekadar kumpulan chart.

**Penjelasan sederhana:** Dashboard yang tidak dipakai untuk keputusan adalah poster, bukan alat kerja.

## Contoh metric contract

`delivery_success_rate = delivered_orders / eligible_orders`, dengan eligible berarti order paid yang memiliki shipment valid dan dibuat dalam periode lokal Asia/Jakarta. Owner: Ops Analytics. Refresh target: harian pukul 06.30 WIB.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| PostgreSQL | 18.6 | serving metrics |
| Tableau | lihat release notes resmi saat deployment | BI visualization |

## Referensi resmi

- [Tableau release notes](https://help.tableau.com/current/tableau/en-us/whatsnew_all.htm)
- [PostgreSQL aggregate functions](https://www.postgresql.org/docs/current/functions-aggregate.html)

## Lanjut ke praktik

Notebook membuat metric contract dan dataset agregat. Assignment meminta dashboard specification yang dapat diimplementasikan di Tableau tanpa ambiguitas.

## Posisi part dalam bootcamp

Part ini mengubah curated data menjadi keputusan yang dapat dipakai Ops dan manajemen. Anda akan menghubungkan definisi metric, query, visualisasi, dan tindakan. Ini adalah latihan penting sebelum hasil AI disajikan ke pengguna pada Fase 2.

## Kapan konsep ini dipakai

Gunakan dashboard ketika pengguna perlu memantau tren atau mengambil tindakan berulang. Gunakan ad-hoc analysis untuk pertanyaan eksploratif yang belum stabil. Jangan membuat visual sebelum definisi metric, grain, denominator, freshness, dan owner disepakati.

## Walkthrough terpandu: dashboard morning briefing

1. Tanyakan keputusan apa yang harus dibuat Sari pada pukul 07.00: kota mana yang memiliki backlog dan merchant mana yang perlu dihubungi.
2. Definisikan KPI: backlog_count, on_time_rate, missing_event_rate, dan delivered_count. Tulis numerator, denominator, filter, timezone, dan refresh SLA.
3. Buat serving query satu baris per city-date. Validasi terhadap order-level sample sebelum membuat chart.
4. Pilih visual: KPI cards untuk status saat ini, trend line untuk perubahan tujuh hari, bar chart untuk perbandingan kota, dan table untuk drill-down.
5. Tambahkan filter tanggal dan kota tanpa mengubah definisi denominator secara diam-diam.
6. Simulasikan data terlambat. Dashboard harus menunjukkan freshness timestamp dan status data, bukan memberi kesan angka terbaru ketika source belum lengkap.
7. Tulis action note: setiap warna atau threshold harus mengarah pada tindakan yang disepakati.

## Latihan terbimbing

- Buat metric contract untuk on-time delivery.
- Temukan visual yang menyesatkan karena denominator berbeda.
- Rancang drill-down dari city ke merchant lalu ke order.
- Tambahkan annotation saat pipeline quality gate gagal.
- Uji dashboard dengan pengguna persona Dinda dan Sari, lalu catat perubahan.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjawab “angka ini menghitung apa?” untuk setiap KPI, menunjukkan query sumbernya, dan menjelaskan tindakan pengguna ketika metric melewati threshold.

## Jembatan ke assignment

Assignment harus berisi dashboard specification atau implementasi lokal, metric dictionary, query, mock data, screenshot/output yang dapat direproduksi, dan catatan tiga keputusan yang dapat dibuat dari dashboard.
