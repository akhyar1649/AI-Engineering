# Scheduling & Triggering

**Fase:** 3 — Automation  
**Section:** System Integration & Deployment

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- memilih webhook, polling, schedule, queue, atau event trigger;
- memahami timezone, daylight saving, missed run, dan duplicate trigger;
- merancang backfill dan replay untuk time-based workflow;
- mengatur concurrency dan rate limits;
- membuat trigger contract dan test.

## Konteks di PT Kirimin

Notifikasi delivery harus real-time, rekonsiliasi kurir berjalan setiap malam, dan backlog report berjalan pukul 06.00 WIB. Trigger yang salah dapat mengirim notifikasi ganda atau melewatkan window.

## Konsep kunci

### Event versus schedule

**Definisi teknis:** Event trigger merespons occurrence dengan latency rendah; schedule memulai workflow berdasarkan wall-clock/timezone. Polling menukar kesederhanaan dengan latency dan duplicate detection.

**Penjelasan sederhana:** Bel pintu berbeda dari alarm jam 6; keduanya memulai pekerjaan dengan alasan berbeda.

### Timezone dan idempotency

**Definisi teknis:** Timestamp harus memiliki timezone/normalization rule. Scheduled run membutuhkan run key berdasarkan logical date, bukan waktu process aktual.

**Penjelasan sederhana:** “Pukul 06.00” tanpa kota tidak lengkap; dan jika alarm berbunyi dua kali, pekerjaan tetap satu.

### Backfill

**Definisi teknis:** Backfill menjalankan workflow untuk historical window dengan controlled rate dan side-effect policy. Notification backfill biasanya disabled atau diarahkan ke dry-run.

**Penjelasan sederhana:** Menghitung laporan bulan lalu tidak berarti mengirim ulang semua notifikasi bulan lalu.

## Trigger matrix Kirimin

| Proses | Trigger | Duplicate key | Side effect |
|---|---|---|---|
| shipment status | webhook | event_id | notify |
| reconciliation | schedule 23:00 WIB | business_date | report |
| exception review | queue/poll | ticket_id | create task |

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | trigger/scheduler |

## Referensi resmi

- [n8n trigger nodes](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/)
- [n8n webhook node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook/)

## Lanjut ke praktik

Notebook membentuk logical run key dan membandingkan trigger behavior.

## Posisi part dalam bootcamp

Part ini mengajarkan memilih trigger dan schedule yang tepat. Trigger menentukan freshness, concurrency, retry behavior, dan beban downstream. Anda akan menghubungkan event-time reasoning dari Fase 1 dengan kebutuhan operational automation.

## Kapan konsep ini dipakai

Gunakan webhook untuk event yang dikirim source, polling bila source tidak menyediakan event, schedule untuk reconciliation atau batch, dan manual trigger untuk recovery. Jangan memakai polling agresif untuk menutupi contract source yang buruk.

## Walkthrough terpandu: hourly reconciliation

1. Tentukan SLA dan lag yang dapat diterima.
2. Pilih schedule hourly untuk mencari event yang hilang, sementara webhook menangani event normal.
3. Gunakan watermark dan lookback window agar late event masuk tanpa memproses seluruh history.
4. Tambahkan lock/concurrency policy agar dua run overlap tidak menggandakan action.
5. Buat backfill parameterized by date range.
6. Uji timezone, daylight-saving assumption jika relevan, missed schedule, dan retry.
7. Catat trigger metadata untuk audit.

## Latihan terbimbing

- Bandingkan webhook, polling, dan schedule untuk tiga source.
- Buat lookback query.
- Simulasikan dua execution bersamaan.
- Buat manual backfill workflow.
- Tentukan alert jika schedule terlambat.

## Checkpoint penguasaan

Anda siap lanjut jika pemilihan trigger dikaitkan dengan freshness, source capability, concurrency, and recovery.

## Jembatan ke assignment

Assignment harus berisi trigger decision, schedule config, watermark/backfill design, concurrency test, timezone assumptions, dan runbook.
