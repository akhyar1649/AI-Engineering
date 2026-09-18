# Model Serving & Production-Grade Deployment

**Fase:** 2 — AI Engineering (LLM)  
**Section:** Deployment, Evaluation & Governance

> Diverifikasi: FastAPI v0.141.1 — sumber: https://fastapi.tiangolo.com/release-notes/ — tanggal cek: 2026-09-18
> Diverifikasi: Docker Engine v29.6.2 — sumber: https://docs.docker.com/engine/release-notes/29/ — tanggal cek: 2026-09-18
> Diverifikasi: Ollama model library — sumber: https://ollama.com/library — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan hosted API, self-hosted model server, dan local runtime;
- merancang inference API dengan queue, concurrency, timeout, dan streaming;
- membuat readiness, observability, auth, rate limit, dan secret policy;
- menyiapkan canary, rollback, dan model/prompt versioning;
- menjelaskan trade-off GPU, CPU, throughput, dan latency.

## Konteks di PT Kirimin

Assistant support mulai digunakan banyak agent. Fajar membutuhkan response stabil dan Reza ingin tahu kapan memakai hosted provider versus model yang dijalankan internal.

## Konsep kunci

### Serving boundary

**Definisi teknis:** Model serving exposes inference as a service with request schema, batching/concurrency, lifecycle, auth, telemetry, and resource policy. Model artifact alone is not a production system.

**Penjelasan sederhana:** Mesin AI harus punya loket, antrean, jam kerja, dan petugas keselamatan; model file saja belum cukup.

### Throughput dan latency

**Definisi teknis:** Latency mencakup queue, prefill, decode, network, dan postprocess; throughput mengukur request/token per unit waktu. Optimasi salah satu dapat mengorbankan yang lain.

**Penjelasan sederhana:** Melayani satu pelanggan tercepat belum tentu membuat antrean sepuluh ribu pelanggan selesai cepat.

### Deployment safety

**Definisi teknis:** Canary/blue-green, health check, rollback artifact, and schema compatibility reduce blast radius of model/prompt changes.

**Penjelasan sederhana:** Coba resep baru pada satu meja dahulu sebelum seluruh kantin mengganti menu.

## Serving blueprint Kirimin

API gateway → auth/rate limit → request classifier → model route → RAG/tools → output validator → response. Redis dapat digunakan untuk cache/queue; model runtime local hanya dipilih jika security, cost, latency, dan operational skill mendukung.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| FastAPI | 0.141.1 | inference API |
| Docker Engine | 29.6.2 | deployment |
| Ollama | pin release/image saat deployment | local model runtime |
| Redis | pin image saat deployment | cache/queue |

## Referensi resmi

- [FastAPI deployment](https://fastapi.tiangolo.com/deployment/)
- [Docker production guidance](https://docs.docker.com/build/building/best-practices/)
- [Ollama library](https://ollama.com/library)
- [Redis documentation](https://redis.io/docs/latest/)

## Lanjut ke praktik

Notebook mensimulasikan request queue dan model route; deployment adapter dapat diganti dengan provider/API runtime yang diverifikasi.

## Posisi part dalam bootcamp

Part ini membawa model atau AI application ke service yang dapat dipanggil. Anda akan menghubungkan API contract, container, concurrency, health, rollout, security, and observability yang telah dipelajari di Fase 1.

## Kapan konsep ini dipakai

Gunakan model serving ketika consumer membutuhkan endpoint stabil dengan SLA. Pisahkan model loading, request validation, inference, post-processing, dan telemetry. Untuk provider API, serving service tetap perlu mengelola timeout, quota, fallback, dan version.

## Walkthrough terpandu: inference API internal

1. Tetapkan POST /predict atau /answer contract, schema, max input, auth, request_id, dan error codes.
2. Load model/provider client sekali saat startup jika aman, bukan setiap request.
3. Tambahkan readiness yang memeriksa dependency dan liveness yang hanya memeriksa process.
4. Ukur concurrency, queueing, p50/p95/p99 latency, timeout, token usage, dan error rate.
5. Terapkan rate limit, payload limit, redaction, and access control.
6. Deploy versioned image ke staging, run smoke and contract tests, lalu canary dengan rollback criteria.
7. Tulis runbook untuk high latency, model load failure, provider outage, dan bad release.

## Latihan terbimbing

- Buat service local dengan fake model.
- Tambahkan OpenAPI/schema validation.
- Uji concurrent requests dan timeout.
- Buat graceful shutdown.
- Simulasikan canary versus all-at-once rollout.

## Checkpoint penguasaan

Anda siap lanjut jika endpoint memiliki contract, health, telemetry, security, test, deployment, dan rollback yang dapat didemokan.

## Jembatan ke assignment

Assignment harus berisi service code, Dockerfile, API spec, tests, load/latency result, deployment notes, observability, and rollback runbook.
