# Containerization & Deployment

**Fase:** 1 — Data Infrastructure  
**Section:** Reliability & Cloud Infrastructure

> Diverifikasi: Docker Engine v29.6.2 — sumber: https://docs.docker.com/engine/release-notes/29/ — tanggal cek: 2026-09-18
> Diverifikasi: FastAPI v0.141.1 — sumber: https://fastapi.tiangolo.com/release-notes/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menjelaskan image, container, registry, volume, network, dan health check;
- menulis Dockerfile yang reproducible dan tidak membocorkan secret;
- membuat API kecil untuk serving data quality summary;
- membedakan build-time dan runtime configuration;
- merancang deployment dengan health, rollback, dan resource limit.

## Konteks di PT Kirimin

Tim ingin menyajikan quality summary ke internal dashboard. “Berjalan di laptop” belum cukup; service harus memiliki contract, health endpoint, image yang dapat dipromosikan, dan konfigurasi terpisah dari code.

## Konsep kunci

### Image dan container

**Definisi teknis:** Image adalah artefak immutable berisi filesystem layer dan metadata; container adalah instance runtime dari image dengan process, network, dan filesystem writable sementara.

**Penjelasan sederhana:** Image adalah cetak biru paket; container adalah paket yang benar-benar dikirim dan sedang berjalan.

### Reproducibility dan supply chain

**Definisi teknis:** Build reproducible mengunci base image/dependency, meminimalkan context, dan memisahkan build stage. Supply-chain security meliputi provenance, vulnerability scan, dan non-root execution.

**Penjelasan sederhana:** Jika resep dan bahan berubah setiap kali, hasil paket bisa berbeda. Simpan versi bahan dan periksa sebelum dikirim.

### Health dan deployment

**Definisi teknis:** Liveness menunjukkan process hidup; readiness menunjukkan service siap menerima traffic. Deployment yang aman membutuhkan startup behavior, timeout, rollback, dan observability.

**Penjelasan sederhana:** Orang yang masih bangun tidak sama dengan orang yang siap menerima order.

## FastAPI service contract

`GET /health` harus ringan dan tidak memanggil dependency berat. `GET /quality-summary?run_date=...` mengembalikan schema stabil, status, counts, dan generated timestamp. Secret dibaca dari environment atau secret manager.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| Docker Engine | 29.6.2 | build/run container |
| FastAPI | 0.141.1 | API serving |
| Python | 3.14.7 | runtime |

## Referensi resmi

- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Docker build best practices](https://docs.docker.com/build/building/best-practices/)
- [FastAPI deployment concepts](https://fastapi.tiangolo.com/deployment/concepts/)

## Lanjut ke praktik

Notebook menjalankan service contract dengan pure Python mock. Assignment meminta Dockerfile dan deployment runbook.

## Posisi part dalam bootcamp

Part ini membuat aplikasi dan pipeline dapat dijalankan konsisten di laptop, CI, atau platform deployment. Container adalah packaging boundary; ia tidak otomatis membuat sistem aman, observable, atau production-ready.

## Kapan konsep ini dipakai

Gunakan container ketika runtime, dependency, atau service perlu direproduksi lintas environment. Gunakan Compose untuk local multi-service development. Pisahkan image build, configuration, secrets, health check, dan persistent data.

## Walkthrough terpandu: container pipeline dan API

1. Identifikasi process boundary: generator, pipeline worker, API, dan database. Mulai dari container minimal yang benar-benar dibutuhkan.
2. Buat Dockerfile dengan base image resmi, non-root user, pinned dependency, dan command eksplisit.
3. Gunakan environment variable untuk config non-secret dan secret manager atau local secret file yang tidak di-commit untuk secret.
4. Tambahkan health endpoint, readiness check, log ke stdout, dan volume hanya untuk data yang memang persistent.
5. Jalankan Compose, panggil /health, jalankan pipeline sample, lalu matikan dan hidupkan kembali untuk menguji reproducibility.
6. Uji image tanpa internet setelah dependency tersedia, sehingga masalah network build terdeteksi.
7. Dokumentasikan rollback ke image tag sebelumnya dan bukti bahwa schema/data migration kompatibel.

## Latihan terbimbing

- Kecilkan image dan jelaskan perubahan.
- Tambahkan health check yang membedakan process hidup dari dependency siap.
- Uji bad configuration dan missing secret.
- Pisahkan development dan production configuration.
- Buat smoke test yang berjalan setelah container start.

## Checkpoint penguasaan

Anda siap lanjut jika orang lain dapat menjalankan sistem dari README, container gagal secara jelas saat config invalid, dan Anda dapat menjelaskan data mana yang ephemeral versus persistent.

## Jembatan ke assignment

Assignment harus memuat Dockerfile/Compose atau equivalent, config contract, health/readiness behavior, smoke test, image security checklist, run command, dan rollback note.
