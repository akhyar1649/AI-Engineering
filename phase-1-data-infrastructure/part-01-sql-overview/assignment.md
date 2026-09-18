# Assignment — SQL Overview

## Konteks kasus

Fajar meminta laporan harian untuk customer support. Ia ingin mengetahui order paid yang belum delivered, kota dengan backlog terbesar, dan daftar tiket yang terkait dengan order bernilai tinggi. Data sintetis tersedia melalui setup notebook atau boleh Anda generate ulang dengan seed yang sama.

## Tugas dan requirement

Buat satu file `submission.sql` yang berisi query berikut:

1. Tampilkan 10 order paid dengan nilai terbesar pada periode yang diberikan.
2. Hitung jumlah order per `origin_city` dan `payment_status`, termasuk kota yang memiliki nama tidak konsisten.
3. Buat ringkasan shipment terbaru per order menggunakan window function atau subquery, lalu tampilkan order yang belum delivered.
4. Hitung total nilai order per kota tanpa menggandakan nilai akibat banyaknya shipment event.
5. Tampilkan tiket customer yang belum resolved dan memiliki order dengan nilai minimal IDR 500.000.
6. Tambahkan query validasi yang memeriksa duplicate `order_id`, missing `order_id`, dan row count setiap tahap.

Untuk setiap query, tulis komentar singkat berisi grain hasil dan asumsi bisnis. Jangan menghapus data kotor; tampilkan temuan inkonsistensi secara eksplisit.

## Bahan/dataset

Gunakan dataset sintetis PT Kirimin dari notebook. Jika membuat generator sendiri, gunakan minimal 30 order, 50 shipment event, dan 10 ticket; sertakan seed serta sengaja masukkan minimal satu duplicate, missing value, dan variasi nama kota.

## Kriteria penilaian

- 25% ketepatan filter dan agregasi.
- 25% join dan pengendalian grain.
- 20% penanganan `NULL` serta inkonsistensi data.
- 20% validasi hasil dan keterbacaan SQL.
- 10% dokumentasi asumsi.

## Format pengumpulan

```text
submission/
├── submission.sql
└── notes.md
```

`notes.md` berisi cara menjalankan query, asumsi, dan tiga temuan data.

## Estimasi waktu

1–3 jam.

## Prasyarat dari part ini

Sebelum mengerjakan, jalankan notebook part ini dari awal dan pahami kontrak data, grain/schema, serta contoh kasus pada materi. Pastikan output assignment dapat menggunakan artifact dari part sebelumnya atau membuat fixture sintetis yang setara.

## Tools yang digunakan

- Python 3.14.7 untuk generator, transformasi, test, dan command-line runner.
- Jupyter untuk eksplorasi dan validasi bertahap.
- pandas 3.0.3 bila tugas memproses data tabular.
- SQLite fallback untuk latihan SQL lokal; PostgreSQL 18.6 untuk syntax dan explain yang ditujukan ke database.
- Docker Engine 29.6.2, Airflow 3.3.2, Spark 4.2.0, atau MongoDB 8.3 hanya jika disebut oleh scope assignment.
- Git untuk versioning dan review perubahan.

Versi dan link verifikasi ada di docs/00-tech-stack-version-log.md. Jika memakai mock/local adapter, jelaskan contract yang dipertahankan dan perbedaannya dengan service nyata.

## Langkah pengerjaan

1. Baca konteks kasus dan tulis tujuan keputusan yang ingin didukung.
2. Jalankan notebook dan simpan fixture atau seed yang digunakan.
3. Tulis contract input, output, grain/schema, quality rule, dan error behavior.
4. Implementasikan tugas satu per satu sesuai daftar requirement di atas.
5. Tambahkan test untuk normal case serta minimal dua failure case yang relevan, misalnya missing value, duplicate, empty input, invalid schema, timeout, atau rerun.
6. Jalankan validasi dengan command yang tercantum di README dan simpan hasil ringkasnya.
7. Buat notes yang menjelaskan asumsi, trade-off, keterbatasan local mode, dan hubungan output dengan part berikutnya.

## Output dan bukti yang harus terlihat

Submission harus berisi seluruh file pada bagian Format pengumpulan, fixture/generator sintetis, test result, contoh output, dan README atau notes yang dapat diikuti mentor. Query/pipeline/storage harus menunjukkan grain, lineage, quality evidence, dan idempotence bila relevan; diagram harus memiliki input, output, owner, dan failure boundary.

## Self-check sebelum submit

- [ ] Command run dapat dijalankan ulang tanpa langkah tersembunyi.
- [ ] Tidak ada credential atau data pelanggan nyata.
- [ ] Ada seed/fixture dan expected result.
- [ ] Ada validasi jumlah, schema, key, NULL, atau quality sesuai kasus.
- [ ] Failure tidak disembunyikan; setiap reject/error memiliki alasan.
- [ ] Assignment menjelaskan kapan tool dipakai dan kapan solusi lebih sederhana cukup.
- [ ] Notes menyebut limitation dan next step ke part berikutnya.

## Hubungan dengan part berikutnya

Artifact ini bukan hasil terpisah. Pastikan nama field, definisi metric, quality rule, dan keputusan arsitektur dapat dipakai sebagai input part berikutnya atau dijelaskan adapter-nya.
