# Integrated System

**Fase:** 3 — Automation  
**Section:** System Integration & Deployment

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18
> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18

## Tujuan belajar

- merancang integrasi antar API, database, queue, dan notification;
- menetapkan contract, correlation id, timeout, dan retry per boundary;
- membedakan orchestration dan choreography;
- mengelola partial failure dan compensation;
- membuat end-to-end test dengan fake systems.

## Konteks di PT Kirimin

Event shipment perlu dibaca, disimpan ke PostgreSQL, status customer diambil, notifikasi dikirim, dan exception dibuat. Semua dependency memiliki failure mode berbeda.

## Konsep kunci

### Contract-first integration

**Definisi teknis:** Contract-first mendefinisikan schema, auth, error codes, idempotency, timeout, and compatibility sebelum node dihubungkan.

**Penjelasan sederhana:** Dua tim harus sepakat bentuk paket dan cara melaporkan kerusakan sebelum conveyor disambungkan.

### Orchestration versus choreography

**Definisi teknis:** Orchestration memiliki coordinator yang mengatur langkah; choreography membuat services bereaksi pada events. Orchestration mudah ditelusuri, choreography dapat mengurangi coupling tetapi meningkatkan observability complexity.

**Penjelasan sederhana:** Satu dispatcher versus banyak departemen yang bereaksi pada pengumuman.

### Compensation

**Definisi teknis:** Compensation melakukan tindakan pemulihan ketika transaksi lintas sistem tidak atomic. Ia bukan rollback database biasa dan harus aman/idempotent.

**Penjelasan sederhana:** Jika notifikasi gagal setelah status tersimpan, Anda mengantrekan ulang notifikasi; bukan menghapus status yang benar.

## Integration map Kirimin

`shipment webhook → PostgreSQL event ledger → customer lookup → notification provider → ticket exception`. Setiap boundary membawa `correlation_id` dan `idempotency_key`.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | orchestration |
| PostgreSQL | 18.6 | event ledger |

## Referensi resmi

- [n8n integrations](https://docs.n8n.io/integrations/)
- [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)

## Lanjut ke praktik

Notebook menjalankan fake integration services dan ledger idempotency.

## Posisi part dalam bootcamp

Part ini menggabungkan event, database ledger, external service, notification, dan exception handling menjadi satu system. Ini adalah latihan utama sebelum Capstone 3 karena menuntut contract lintas komponen.

## Kapan konsep ini dipakai

Gunakan orchestration ketika satu process memiliki central coordinator dan dependency jelas. Gunakan choreography ketika service bereaksi terhadap event secara independen. Pilih berdasarkan observability, coupling, recovery, dan ownership.

## Walkthrough terpandu: shipment-to-notification

1. Terima shipment event dan validasi schema/signature.
2. Tulis event ledger secara idempotent.
3. Enrich order/customer dengan timeout dan access policy.
4. Tentukan notification eligibility dan buat notification intent, bukan langsung send jika approval diperlukan.
5. Kirim notification melalui adapter, catat provider response, dan update ledger.
6. Jika dependency gagal, route ke retry atau exception queue tanpa kehilangan correlation.
7. Jalankan end-to-end test untuk normal, duplicate, out-of-order, lookup not found, timeout, and provider failure.

## Latihan terbimbing

- Buat contract table untuk lima dependency.
- Bandingkan saga/compensation dengan simple retry.
- Tambahkan fake services.
- Visualisasikan trace lintas system.
- Uji replay satu event.

## Checkpoint penguasaan

Anda siap lanjut jika system dapat ditelusuri end-to-end, side effect idempotent, dan partial failure memiliki outcome eksplisit.

## Jembatan ke assignment

Assignment harus mengumpulkan workflow, contracts, fake services, tests, architecture decision, trace examples, dan recovery note.
