# Solution Explanation — Capstone 1

Solusi referensi membagi sistem menjadi raw immutable, processing, curated, quarantine, dan serving. Generator meniru kondisi produksi agar peserta harus mengukur kualitas, bukan hanya membuat pipeline happy path. Partition/run date menjadi idempotency key; quality failure yang deterministic tidak di-retry tanpa perubahan input.

Deployment minimal dapat berupa container API dan batch runner. Untuk skala lebih besar, Spark atau managed warehouse dipilih berdasarkan volume/query pattern, sementara Airflow mengatur dependency. PostgreSQL dapat menjadi serving layer awal dan MongoDB dipakai khusus event tracking ketika access pattern mendukung.

Kesalahan umum yang harus dibahas peserta: append pada setiap retry, menghapus duplicate tanpa audit, dashboard tanpa metric contract, IAM terlalu luas, dan cost model yang hanya menghitung compute.
