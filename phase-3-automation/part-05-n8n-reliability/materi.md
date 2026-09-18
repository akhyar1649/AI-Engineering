# n8n Reliability

**Fase:** 3 — Automation  
**Section:** Automation & n8n Foundations

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18
> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18

## Tujuan belajar

- merancang retry, backoff, timeout, error workflow, dan dead-letter path;
- membuat workflow idempotent dan replayable;
- menyimpan execution/audit state;
- membatasi concurrency dan external API rate;
- mendefinisikan SLO automation.

## Konteks di PT Kirimin

Webhook courier dikirim ulang ketika endpoint lambat. Workflow harus memproses event sekali, retry transient failure, dan menaruh event permanen gagal ke review queue.

## Konsep kunci

### Retry classification

**Definisi teknis:** Retry hanya untuk transient error seperti timeout/5xx/rate limit; validation, auth, dan business rejection membutuhkan correction atau escalation.

**Penjelasan sederhana:** Mencoba ulang karena jalan macet masuk akal; mencoba ulang karena alamat salah tidak akan memperbaiki alamat.

### Idempotency dan replay

**Definisi teknis:** Idempotency key mengikat event dan side effect; replay menggunakan raw input/audit record dengan kontrol agar tidak mengulang tindakan irreversible.

**Penjelasan sederhana:** Anda boleh memutar ulang rekaman untuk memperbaiki laporan, tetapi tidak otomatis mengirim uang dua kali.

### SLO automation

**Definisi teknis:** SLO meliputi execution success, processing latency, freshness, duplicate side effect rate, and DLQ age.

**Penjelasan sederhana:** Workflow dinilai bukan hanya “jalan”, tetapi juga tepat waktu dan tidak melakukan tindakan ganda.

## Reliability pattern

`receive → persist raw → dedup → process → confirm → ack`; jika gagal, retry bounded lalu DLQ. Jangan ack sebelum raw event aman tersimpan.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | workflow runtime |
| PostgreSQL | 18.6 | idempotency/execution state |

## Referensi resmi

- [n8n error handling](https://docs.n8n.io/flow-logic/error-handling/)
- [n8n executions](https://docs.n8n.io/workflows/executions/)
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)

## Lanjut ke praktik

Notebook mensimulasikan retry classifier dan dedup store.

## Posisi part dalam bootcamp

Part ini membuat workflow n8n siap menghadapi duplicate, timeout, rate limit, dan partial failure. Prinsipnya sama dengan reliability layer AI, tetapi diterapkan pada graph execution dan side effect.

## Kapan konsep ini dipakai

Gunakan retry hanya untuk transient error dan pastikan action idempotent. Gunakan error workflow untuk capture context. Gunakan dead-letter/exception queue ketika event tidak dapat diproses otomatis.

## Walkthrough terpandu: notification gagal

1. Simpan event_id, execution_id, correlation_id, node, attempt, and payload hash.
2. Bedakan provider timeout, 429, 4xx validation, dan 5xx.
3. Retry 429/5xx dengan backoff dan batas attempt.
4. Sebelum send ulang, cek notification ledger agar duplicate tidak terkirim.
5. Setelah retry habis, tulis exception record dan beri owner.
6. Buat replay procedure yang memilih event tertentu, bukan menjalankan seluruh workflow.
7. Ukur success, retry, dead-letter, duplicate prevented, and time-to-recovery.

## Latihan terbimbing

- Simulasikan timeout dan provider 500.
- Tambahkan idempotency ledger.
- Buat manual replay command.
- Uji partial success pada batch.
- Tulis runbook incident.

## Checkpoint penguasaan

Anda siap lanjut jika setiap side effect aman diulang, failed execution dapat direplay, dan evidence cukup untuk diagnosis.

## Jembatan ke assignment

Assignment harus berisi workflow reliability, error route, retry matrix, idempotency design, replay runbook, tests, dan metrics.
