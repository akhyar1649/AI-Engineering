# Solution Explanation — SQL Overview

## Pendekatan

Solusi memisahkan pertanyaan pada grain order, shipment event, dan ticket. Shipment diringkas lebih dahulu dengan `ROW_NUMBER()` agar laporan satu baris per order tidak menggandakan `order_value_idr`. Query agregasi kota sengaja memakai `origin_city_raw` terlebih dahulu sehingga masalah standardisasi dapat terlihat, bukan disembunyikan.

## Kesalahan umum peserta

1. **Menjumlahkan nilai order setelah join langsung ke semua shipment event.** Satu order dengan tiga event akan dihitung tiga kali. Ringkas sisi many terlebih dahulu atau gunakan metrik pada grain yang tepat.
2. **Menggunakan `= NULL`.** Kondisi ini tidak pernah menjadi `TRUE`; gunakan `IS NULL`.
3. **Menganggap `COUNT(column)` sama dengan `COUNT(*)`.** `COUNT(column)` mengabaikan `NULL`, sedangkan `COUNT(*)` menghitung baris.
4. **Menghapus duplicate tanpa investigasi.** Duplicate dapat merupakan retry yang perlu dideduplikasi berdasarkan `order_id` dan aturan “latest record wins”.
5. **Mengubah `JKT` menjadi `Jakarta` di query laporan tanpa dokumentasi.** Normalisasi adalah keputusan data quality yang harus dapat ditelusuri.

## Cara memperbaiki

Mulai dari pertanyaan bisnis, tulis grain target, cek key dan row count setelah setiap join, lalu baru memilih agregasi. Untuk production, pindahkan normalisasi kota ke staging/curated layer dengan mapping table berversi.
