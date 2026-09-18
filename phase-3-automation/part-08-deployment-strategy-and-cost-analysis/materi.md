# Deployment Strategy & Cost Analysis

**Fase:** 3 — Automation  
**Section:** System Integration & Deployment

> Diverifikasi: Docker Engine v29.6.2 — sumber: https://docs.docker.com/engine/release-notes/29/ — tanggal cek: 2026-09-18
> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membandingkan n8n cloud, self-hosted VPS, dan container platform;
- menghitung fixed, variable, operations, backup, dan egress cost;
- memilih deployment berdasarkan volume, risk, skill, dan availability;
- merancang environment promotion dan secret management;
- menulis deployment decision record.

## Konteks di PT Kirimin

Sari ingin workflow murah untuk awal, tetapi Reza tidak mau kehilangan execution history dan recovery. Pilihan deployment harus melihat total cost of ownership, bukan harga VM saja.

## Konsep kunci

### Deployment topology

**Definisi teknis:** Topology mencakup runtime, database, queue, reverse proxy, storage, backup, network, and monitoring. Managed platform mengurangi toil tetapi memiliki control/portability trade-off.

**Penjelasan sederhana:** Memindahkan workflow ke server berarti juga memikirkan rumah, listrik, backup, dan keamanan rumah tersebut.

### TCO

**Definisi teknis:** Total cost of ownership mencakup license/compute, engineering time, upgrades, incidents, monitoring, backup, recovery, and opportunity cost.

**Penjelasan sederhana:** Sewa murah bisa menjadi mahal jika setiap minggu perlu diperbaiki manual.

### Environment promotion

**Definisi teknis:** Workflow definition dipromosikan dari dev → staging → production dengan version control, parameterized credentials, test, approval, dan rollback.

**Penjelasan sederhana:** Resep diuji di dapur latihan sebelum dipakai di restoran penuh.

## Cost model

`monthly = runtime + database + storage + backup + network + monitoring + maintenance_hours × engineer_rate`. Nyatakan asumsi dan sensitivity.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| Docker Engine | 29.6.2 | packaging |
| n8n | 2.x; pin release | workflow runtime |

## Referensi resmi

- [n8n hosting options](https://docs.n8n.io/choose-n8n/)
- [Docker deployment](https://docs.docker.com/engine/)

## Lanjut ke praktik

Notebook menghitung TCO scenario sederhana. Assignment meminta ADR deployment.

## Posisi part dalam bootcamp

Part ini mengubah workflow yang berjalan menjadi deployment strategy yang dapat dibayar dan dioperasikan. Anda membawa cost model dan container knowledge dari Fase 1, lalu menambahkan execution volume, credential, queue, and support burden.

## Kapan konsep ini dipakai

Bandingkan managed n8n, self-hosted VM/container, dan hybrid ketika workflow akan dipakai lebih luas. Pilih berdasarkan volume, availability, data sensitivity, team capability, customization, dan total cost of ownership.

## Walkthrough terpandu: memilih deployment workflow

1. Hitung executions per day, average duration, concurrency, payload size, retry, and retention.
2. Petakan component: n8n, database, queue/worker, secret store, reverse proxy, monitoring, backup.
3. Tentukan SLO, RPO, RTO, and support hours.
4. Buat cost model low/base/high termasuk compute, storage, egress, and human operations.
5. Bandingkan managed versus self-hosted dengan risk and exit strategy.
6. Rancang deployment, upgrade, backup, restore, and rollback.
7. Tetapkan decision threshold untuk pindah tier.

## Latihan terbimbing

- Buat TCO model.
- Rancang architecture untuk sandbox dan production.
- Hitung impact retry storm.
- Tulis backup restore drill.
- Buat migration/exit checklist.

## Checkpoint penguasaan

Anda siap lanjut jika deployment choice dapat dipertanggungjawabkan dengan volume, SLO, cost, ownership, and recovery evidence.

## Jembatan ke assignment

Assignment harus menghasilkan deployment diagram, cost model, environment strategy, backup/restore, risk register, and recommendation.
