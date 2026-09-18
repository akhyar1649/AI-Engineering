# Python Overview untuk Data Engineering

**Fase:** 1 — Data Infrastructure  
**Section:** Foundations

> Diverifikasi: Python v3.14.7 — sumber: https://docs.python.org/3/ — tanggal cek: 2026-09-18
> Diverifikasi: pandas v3.0.3 — sumber: https://pandas.pydata.org/docs/whatsnew/v3.0.3.html — tanggal cek: 2026-09-18

## Tujuan belajar

- menyusun fungsi Python yang memiliki kontrak input/output jelas;
- memproses data tabular dengan pandas secara dapat diulang;
- menggunakan exception handling dan logging untuk pipeline kecil;
- memilih antara list, generator, dan DataFrame berdasarkan ukuran data;
- menulis validasi sederhana sebelum data diteruskan ke tahap berikutnya.

## Konteks di PT Kirimin

Sari menerima file order harian dari beberapa channel. Formatnya tidak selalu sama dan beberapa batch gagal diproses tanpa pesan yang jelas. Python menjadi glue code untuk membaca, memvalidasi, membersihkan, dan menghasilkan artefak yang dapat diaudit.

## Konsep kunci

### Fungsi dan kontrak data

**Definisi teknis:** Fungsi adalah unit komputasi dengan parameter, return value, dan precondition/postcondition yang dapat diuji. Pada data pipeline, kontrak perlu menjelaskan kolom wajib, tipe data, dan perilaku terhadap baris invalid.

**Penjelasan sederhana:** Fungsi seperti mesin dengan lubang masuk dan keluar. Jika Anda tidak menentukan bentuk barang yang bisa dimasukkan, setiap orang akan memasukkan bentuk berbeda dan hasilnya sulit dipercaya.

### DataFrame dan operasi vektor

**Definisi teknis:** DataFrame adalah struktur data tabular berlabel yang mendukung operasi kolom secara vektor. Operasi vektor biasanya lebih jelas dan efisien daripada loop Python per baris untuk transformasi tabular.

**Penjelasan sederhana:** DataFrame seperti spreadsheet yang dapat diberi instruksi ke satu kolom sekaligus, bukan menyentuh sel satu per satu.

### Error handling dan observability

**Definisi teknis:** Exception handling memisahkan error yang dapat dipulihkan dari error yang harus menghentikan pipeline. Logging terstruktur merekam event, konteks, dan severity tanpa membocorkan secret.

**Penjelasan sederhana:** Jika satu paket kiriman rusak, kurir perlu tahu paket mana dan apa masalahnya. Pesan “gagal” saja tidak membantu investigasi.

### Iterator dan memory

**Definisi teknis:** List menyimpan seluruh elemen di memory, sedangkan generator menghasilkan elemen secara lazy. Untuk file besar, streaming/chunking mencegah penggunaan memory yang tidak terkendali.

**Penjelasan sederhana:** List membawa seluruh barang ke meja sekaligus; generator mengambil satu kardus saat dibutuhkan.

## Pola implementasi

Gunakan fungsi kecil seperti `parse_orders`, `validate_required_columns`, dan `standardize_city`. Kembalikan data bersih bersama ringkasan quality report. Jangan menelan exception secara diam-diam; sertakan identifier batch dan baris yang gagal.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| Python | 3.14.7 | runtime |
| pandas | 3.0.3 | transformasi tabular |

## Referensi resmi

- [Python functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python exceptions](https://docs.python.org/3/tutorial/errors.html)
- [pandas user guide](https://pandas.pydata.org/docs/user_guide/)

## Lanjut ke praktik

Jalankan notebook untuk memproses batch order sintetis dan mengamati perbedaan error yang ditangani versus error yang harus menghentikan pipeline.

## Posisi part dalam bootcamp

Part ini menerjemahkan aturan SQL dan kontrak grain dari Part 1 menjadi program yang dapat dijalankan ulang. Fokusnya bukan menghafal syntax Python, melainkan membangun fungsi yang menerima input yang jelas, mengembalikan output yang jelas, dan meninggalkan bukti ketika ada baris invalid. Output praktik akan dipakai pada cleaning Part 4 dan pipeline Part 5.

## Kapan konsep ini dipakai

Gunakan Python ketika transformasi memerlukan parsing file, aturan bercabang, pemanggilan API, validasi yang dapat diuji, atau orkestrasi library. Gunakan SQL untuk filter dan agregasi yang lebih dekat dengan database. Pada dataset kecil, pandas membuat inspeksi mudah; pada dataset besar, gunakan chunking, generator, atau engine terdistribusi sesuai kebutuhan.

## Walkthrough terpandu: parser batch order

1. Mulai dengan kontrak: kolom wajib order_id, origin_city, order_value_idr, payment_status, dan order_created_at. Tentukan bahwa output bersih memiliki satu baris per order.
2. Buat fungsi require_columns yang mengembalikan error terstruktur jika kolom hilang. Error harus menyebut batch_id dan daftar kolom, bukan hanya “KeyError”.
3. Buat standardize_orders yang menyalin input, menormalkan nama kota dari mapping terbatas, dan mengubah tanggal dengan aturan timezone yang eksplisit.
4. Pisahkan baris valid ke curated dan baris bermasalah ke quarantine. Setiap quarantine row memiliki reason_code seperti missing_order_id atau invalid_value.
5. Kembalikan tiga objek: curated DataFrame, quarantine DataFrame, dan quality_report berisi input_count, curated_count, quarantine_count, serta null_rate.
6. Jalankan fungsi dua kali pada input yang sama. Output dan report harus sama; ini adalah pemeriksaan awal idempotence.
7. Tambahkan test untuk kolom hilang, angka negatif, tanggal invalid, dan input kosong.

## Latihan terbimbing

- Tambahkan mapping kota Bandung, BDO, dan bandung menjadi satu canonical value.
- Buat generator pembaca batch yang memproses data per chunk dan tunjukkan bahwa seluruh file tidak harus berada di memory.
- Ubah exception parsing tanggal menjadi quarantine reason, tetapi biarkan error konfigurasi kolom menghentikan pipeline.
- Tambahkan logging dengan batch_id dan jumlah baris tanpa menulis data pelanggan.
- Uji bahwa fungsi tidak mengubah DataFrame input di tempat.

## Checkpoint penguasaan

Anda siap lanjut jika dapat membedakan data error yang harus dikarantina dari programming error yang harus menghentikan job, menjelaskan kontrak fungsi, dan membuktikan rerun menghasilkan output yang sama.

## Jembatan ke assignment

Assignment harus berisi modul Python yang dapat diimpor, test case untuk happy path dan failure path, quality report, serta contoh command untuk menjalankan batch. Sertakan keputusan kapan solusi Python tersebut sebaiknya dipindahkan ke SQL atau Spark.
