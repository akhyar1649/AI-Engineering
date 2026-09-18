# Data Governance Fundamentals & Quality Management

**Fase:** 1 — Data Infrastructure  
**Section:** Data Architecture, Pipeline & Governance

> Diverifikasi: Great Expectations v1.23.0 — sumber: https://docs.greatexpectations.io/docs/core/changelog/ — tanggal cek: 2026-09-18
> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menjelaskan ownership, stewardship, lineage, dan access policy;
- mendefinisikan dimensi data quality dan business rule;
- membuat expectation yang dapat dijalankan otomatis;
- merancang quality gate dan escalation path;
- membedakan quality issue, security issue, dan semantic issue.

## Konteks di PT Kirimin

Dinda ingin data order yang dipakai AI dan dashboard memiliki owner serta bukti kualitas. Tim tidak cukup mengatakan “data sudah dicek”; mereka harus menunjukkan aturan, hasil, dan siapa yang bertindak ketika gagal.

## Konsep kunci

### Governance sebagai operating model

**Definisi teknis:** Data governance adalah kumpulan decision rights, roles, policies, standards, dan controls untuk memastikan data aman, tersedia, dapat ditemukan, dan sesuai tujuan.

**Penjelasan sederhana:** Governance bukan polisi data yang hanya melarang. Ia adalah aturan bersama tentang siapa yang menjaga apa, bagaimana perubahan disetujui, dan apa yang dilakukan ketika terjadi masalah.

### Data quality dimensions

**Definisi teknis:** Completeness, validity, uniqueness, consistency, accuracy, timeliness, dan integrity mengukur aspek berbeda dari fitness for use. Tidak semua dimensi harus 100%; target harus dikaitkan dengan use case.

**Penjelasan sederhana:** Paket bisa punya alamat lengkap tetapi tetap terlambat. Satu ukuran kualitas tidak cukup untuk semua keputusan.

### Expectation dan quality gate

**Definisi teknis:** Expectation adalah assertion yang dapat dievaluasi terhadap data atau metadata. Quality gate menggunakan hasil assertion untuk mengizinkan, menahan, atau mengarantina output.

**Penjelasan sederhana:** Expectation adalah checklist otomatis. Jika jumlah order negatif melewati batas, batch ditahan sebelum masuk dashboard.

### Metadata dan lineage

**Definisi teknis:** Metadata menjelaskan struktur, makna, owner, klasifikasi, dan lifecycle data. Lineage memetakan asal, transformasi, dan consumer.

**Penjelasan sederhana:** Saat angka salah, lineage menjawab “angka ini berasal dari file mana, melewati proses apa, dan dipakai siapa”.

## Quality operating model Kirimin

Tetapkan Dinda sebagai data owner untuk domain order, engineer sebagai custodian, Fajar/Sari sebagai consumer representative. Buat rule severity: blocking untuk key/integrity, warning untuk outlier yang perlu review, informational untuk coverage rendah pada field opsional.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| Great Expectations | 1.23.0 | expectation dan validation result |
| PostgreSQL | 18.6 | source checks |

## Referensi resmi

- [Great Expectations Core](https://docs.greatexpectations.io/docs/core/)
- [Great Expectations expectations](https://docs.greatexpectations.io/docs/core/define_expectations/)
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)

## Lanjut ke praktik

Notebook membuat validasi sederhana yang dapat diadaptasi ke Great Expectations. Assignment meminta data quality specification dan escalation playbook.

## Posisi part dalam bootcamp

Part ini membuat kualitas dan governance menjadi bagian dari sistem, bukan pekerjaan manual setelah masalah terjadi. Anda akan mengubah aturan bisnis menjadi quality checks, owner, severity, dan evidence. Kontrak ini dipakai oleh pipeline, AI, dan automation pada fase berikutnya.

## Kapan konsep ini dipakai

Gunakan data governance ketika banyak tim memakai definisi yang sama, data mengandung risiko, atau kesalahan dapat memengaruhi keputusan. Quality rule harus muncul saat data masuk atau berubah, bukan hanya ketika dashboard sudah diprotes.

## Walkthrough terpandu: quality contract shipment

1. Pilih dataset fact_shipment_event dan tetapkan owner, steward, consumer, grain, freshness, serta sensitivity.
2. Tulis rule uniqueness event_id, non-null order_id, valid status enum, referential integrity ke order, event_at tidak di masa depan, dan freshness maksimal dua jam.
3. Beri severity critical, warning, atau informational. Jelaskan apa yang terjadi jika tiap rule gagal.
4. Jalankan checks pada batch sintetis yang sengaja mengandung duplicate, orphan event, dan stale partition.
5. Simpan run_id, rule_id, observed_value, threshold, status, dan sample failing rows.
6. Buat incident workflow: siapa menerima alert, kapan data dikarantina, bagaimana owner memberi resolusi, dan kapan rule diubah.
7. Publikasikan glossary backlog, delivered, on-time, dan active merchant agar BI dan AI memakai definisi konsisten.

## Latihan terbimbing

- Tambahkan rule untuk city canonical dan positive order value.
- Bedakan rule yang menahan publish dari rule yang hanya memberi warning.
- Buat data owner matrix untuk orders, shipment events, dan customer ticket.
- Rancang evidence retention untuk quality results.
- Simulasikan perubahan definisi on-time dan analisis dampak ke dashboard.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menghubungkan setiap rule dengan risiko bisnis, owner, severity, evidence, dan tindakan perbaikan.

## Jembatan ke assignment

Assignment harus menghasilkan data quality specification, minimal sepuluh rule, sample failure report, ownership matrix, glossary, dan prosedur eskalasi. Jangan hanya menuliskan daftar rule; tunjukkan bagaimana rule dijalankan dan keputusan yang dipicu.
