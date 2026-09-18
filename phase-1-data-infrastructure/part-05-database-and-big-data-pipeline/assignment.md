# Assignment — Database and Big Data Pipeline

## Konteks kasus

Dinda ingin pipeline order harian yang dapat diulang, di-backfill, dan memberikan alert ketika data partner terlambat.

## Tugas dan requirement

1. Buat diagram pipeline raw–curated–serving.
2. Implementasikan pipeline lokal dengan partition date, checkpoint, quality gate, dan quarantine.
3. Tulis rancangan DAG berisi task, dependency, retry policy, dan SLA.
4. Jelaskan kapan transformasi dipindahkan ke Spark dan apa biaya tambahannya.

## Kriteria penilaian

- 25% desain layer.
- 25% idempotence dan backfill.
- 20% quality gate.
- 15% orchestration reasoning.
- 15% dokumentasi operasi.

## Format pengumpulan

```text
submission/
├── pipeline.py
├── dag-design.md
├── architecture.mmd
└── notes.md
```

## Estimasi waktu

3–4 jam.

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
