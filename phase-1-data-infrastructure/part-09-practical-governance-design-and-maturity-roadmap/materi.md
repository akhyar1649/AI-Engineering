# Practical Governance Design & Maturity Roadmap

**Fase:** 1 — Data Infrastructure  
**Section:** Data Architecture, Pipeline & Governance

> Diverifikasi: Great Expectations v1.23.0 — sumber: https://docs.greatexpectations.io/docs/core/changelog/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menerjemahkan prinsip governance menjadi workflow yang dipakai tim;
- membuat RACI untuk domain data Kirimin;
- menyusun data product contract dan change management;
- menilai maturity saat ini dengan evidence;
- membuat roadmap 30/60/90 hari yang realistis.

## Konteks di PT Kirimin

Kirimin tidak dapat membeli platform governance mahal lalu berharap masalah selesai. Dinda meminta desain minimum yang dapat dijalankan tim kecil dan roadmap yang menghubungkan peningkatan governance dengan risiko bisnis.

## Konsep kunci

### RACI dan decision rights

**Definisi teknis:** RACI membedakan Responsible, Accountable, Consulted, dan Informed. Governance membutuhkan decision rights yang eksplisit agar perubahan schema, definisi metric, dan akses data memiliki pemilik.

**Penjelasan sederhana:** Saat pipa bocor, semua orang tidak boleh hanya menunjuk satu sama lain. Harus jelas siapa yang memperbaiki, siapa yang menyetujui, dan siapa yang diberi tahu.

### Data product contract

**Definisi teknis:** Contract menetapkan schema, semantics, quality SLO, freshness, owner, compatibility, dan deprecation policy antara producer dan consumer.

**Penjelasan sederhana:** Kontrak memberi tahu konsumen bentuk paket, kapan dikirim, dan apa yang terjadi jika format berubah.

### Maturity model

**Definisi teknis:** Maturity model menggambarkan kapabilitas bertahap dari ad hoc menuju managed, measured, dan optimized. Level harus dibuktikan dengan artefak, bukan label.

**Penjelasan sederhana:** Naik level bukan karena membeli dashboard baru, tetapi karena proses benar-benar konsisten dan dapat diukur.

## Roadmap Kirimin

- **0–30 hari:** domain inventory, owner, critical data elements, baseline quality.
- **31–60 hari:** automated checks, lineage minimal, incident workflow, metric contracts.
- **61–90 hari:** SLA quality per domain, access review, schema compatibility, quarterly maturity review.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| Great Expectations | 1.23.0 | automation quality |

## Referensi resmi

- [Great Expectations docs](https://docs.greatexpectations.io/docs/core/)
- [AWS Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html)

## Lanjut ke praktik

Notebook membuat RACI dan maturity scoring berbasis evidence. Assignment meminta roadmap yang disepakati stakeholder.

## Posisi part dalam bootcamp

Part ini mengubah prinsip governance menjadi desain operating model yang realistis untuk organisasi yang sedang tumbuh. Anda akan menentukan proses, peran, evidence, dan urutan investasi. Hasilnya membantu Reza memilih perbaikan yang memberi dampak terbesar sebelum Capstone 1.

## Kapan konsep ini dipakai

Gunakan maturity assessment ketika organisasi memiliki banyak masalah tetapi kapasitas perbaikan terbatas. Gunakan roadmap ketika ingin mengubah governance menjadi backlog dengan owner dan ukuran keberhasilan, bukan dokumen aspirasi.

## Walkthrough terpandu: roadmap tiga tahap Kirimin

1. Inventarisir asset orders, shipments, merchant, customer ticket, dan KPI dashboard.
2. Nilai current state pada dimensi ownership, quality, metadata, lineage, access, incident, dan automation dengan skala yang didefinisikan.
3. Hubungkan gap ke dampak: shipment event yang tidak lengkap mengganggu SLA dan customer support; definisi metric yang berbeda mengganggu keputusan.
4. Prioritaskan dengan impact, effort, risk reduction, dan dependency. Pilih quick win seperti glossary dan critical quality rules.
5. Rancang tahap 30, 60, dan 90 hari dengan deliverable, owner, leading indicator, dan exit criteria.
6. Tulis governance decision record: keputusan, alternatif, alasan, konsekuensi, dan cara meninjau ulang.
7. Validasi roadmap dengan persona Dinda, Reza, Fajar, dan Sari agar tidak hanya mewakili engineering.

## Latihan terbimbing

- Buat heatmap maturity untuk lima domain.
- Bandingkan prioritas “quality first” dengan “platform first”.
- Ubah tiga rekomendasi menjadi backlog issue dengan acceptance criteria.
- Definisikan metric governance seperti rule coverage, incident MTTR, dan glossary adoption.
- Tulis risiko jika quick win dijalankan tanpa ownership.

## Checkpoint penguasaan

Anda siap lanjut jika roadmap memiliki baseline, target, owner, dependency, metric, dan alasan urutan yang dapat diperdebatkan secara sehat.

## Jembatan ke assignment

Assignment harus menghasilkan maturity assessment, prioritization matrix, roadmap, RACI, tiga decision records, dan rencana review. Sertakan hubungan tiap inisiatif dengan artifact pipeline yang sudah dibuat.
