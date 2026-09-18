# Cloud Platform Fundamentals

**Fase:** 1 — Data Infrastructure  
**Section:** Reliability & Cloud Infrastructure

> Diverifikasi: AWS Data Analytics Lens — sumber: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html — tanggal cek: 2026-09-18
> Diverifikasi: Google Cloud Architecture Framework — sumber: https://cloud.google.com/architecture/framework — tanggal cek: 2026-09-18

## Tujuan belajar

- menjelaskan compute, storage, network, identity, dan managed service;
- membandingkan shared responsibility pada cloud;
- merancang environment dev/staging/production;
- memilih managed database, object storage, dan compute berdasarkan workload;
- membuat estimasi biaya dan guardrail dasar.

## Konteks di PT Kirimin

Kirimin ingin memperluas pipeline tanpa membeli server sendiri. Reza meminta proposal cloud-neutral yang membahas portability, operational burden, network egress, IAM, backup, dan biaya idle.

## Konsep kunci

### Abstraction dan managed service

**Definisi teknis:** Cloud menyediakan resource on-demand dengan abstraction level berbeda: IaaS, PaaS, dan SaaS. Managed service mengurangi operational work tetapi membatasi kontrol dan dapat meningkatkan vendor coupling.

**Penjelasan sederhana:** Menyewa gudang lengkap mengurangi pekerjaan memperbaiki atap, tetapi Anda mengikuti aturan pemilik gedung.

### Shared responsibility

**Definisi teknis:** Provider bertanggung jawab atas keamanan “of” cloud; customer bertanggung jawab atas konfigurasi, identity, data, secret, dan workload sesuai service.

**Penjelasan sederhana:** Kunci gedung dijaga pemilik, tetapi siapa yang diberi akses ruang arsip tetap tanggung jawab Anda.

### IAM dan least privilege

**Definisi teknis:** Identity and Access Management mengatur principal, authentication, authorization, policy, dan audit. Least privilege memberi akses minimum untuk tugas tertentu.

**Penjelasan sederhana:** Operator pipeline tidak perlu kunci ruang payroll hanya karena ia perlu masuk ruang data.

### Cost model

**Definisi teknis:** Biaya cloud dapat berasal dari compute time, storage, request, transfer, managed control plane, dan observability. Tagging, budget alert, lifecycle policy, dan rightsizing adalah control dasar.

**Penjelasan sederhana:** Sewa gudang bukan hanya luas lantai; ada biaya bongkar muat, listrik, dan pengiriman keluar.

## Cloud blueprint Kirimin

Object storage untuk raw, managed relational untuk serving, container compute untuk API/pipeline, secret manager untuk credential, private network untuk database, dan monitoring terpusat. Pilihan provider dapat berubah; interface serta policy harus terdokumentasi.

## Tools & versi

| Platform | Status | Peran |
|---|---:|---|
| AWS | service API diverifikasi saat deployment | contoh object storage/compute |
| Google Cloud | service API diverifikasi saat deployment | alternatif cloud |

## Referensi resmi

- [AWS Well-Architected Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html)
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)

## Lanjut ke praktik

Notebook membuat resource decision matrix dan cost estimate sederhana. Assignment meminta cloud architecture proposal yang tidak bergantung pada credential.

## Posisi part dalam bootcamp

Part ini menerjemahkan pipeline lokal menjadi komponen cloud yang dapat diskalakan dan dioperasikan. Anda belum memilih provider karena prinsipnya lebih penting: compute, storage, network, identity, observability, dan cost harus dipetakan ke kebutuhan Kirimin.

## Kapan konsep ini dipakai

Gunakan cloud ketika workload membutuhkan availability, kapasitas, managed service, atau kolaborasi yang tidak efisien disediakan sendiri. Tetap gunakan local development untuk iterasi cepat dan data sintetis. Setiap komponen cloud harus memiliki alasan, data classification, dan estimasi cost.

## Walkthrough terpandu: target architecture minimal

1. Petakan raw object storage, relational serving database, containerized pipeline, scheduler, secret manager, log/metric service, dan private network.
2. Tentukan boundary: data plane untuk data, control plane untuk orchestration, dan identity plane untuk permission.
3. Tulis IAM least privilege: ingestion hanya menulis raw, transform membaca raw dan menulis curated, BI membaca serving.
4. Pilih deployment unit dan availability target. Jangan mengklaim high availability jika hanya satu instance.
5. Buat cost model berdasarkan storage GB, compute hours, requests, egress, dan retention.
6. Rancang failure: source unavailable, region issue, credential expiry, quota, dan corrupt batch.
7. Bandingkan cloud managed service dengan self-hosted container memakai criteria cost, operability, portability, dan security.

## Latihan terbimbing

- Gambar logical architecture dan trust boundary.
- Buat permission matrix untuk empat persona.
- Hitung rough monthly cost dari volume sintetis.
- Tulis backup, restore, retention, dan deletion policy.
- Buat checklist pre-deployment tanpa menyimpan credential di repository.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjelaskan fungsi setiap layanan dengan bahasa bisnis, menunjukkan least privilege, dan mengaitkan cost dengan asumsi volume serta SLO.

## Jembatan ke assignment

Assignment harus menghasilkan cloud architecture diagram, service mapping, IAM matrix, cost estimate, risk register, backup/restore plan, dan provider-agnostic deployment checklist.
