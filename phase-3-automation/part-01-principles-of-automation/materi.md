# Principles of Automation

**Fase:** 3 — Automation  
**Section:** Automation & n8n Foundations

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan automation, orchestration, integration, dan software product;
- memilih proses yang layak diotomasi berdasarkan volume, rule stability, dan risk;
- memetakan trigger, action, state, exception, dan owner;
- menghitung benefit, failure cost, dan maintenance cost;
- membuat human-in-the-loop boundary.

## Konteks di PT Kirimin

Sari memiliki spreadsheet pekerjaan manual untuk update status shipment dan notifikasi customer. Tidak semua langkah layak diotomasi; refund dan exception tertentu harus tetap membutuhkan approval manusia.

## Konsep kunci

### Automation fit

**Definisi teknis:** Automation fit menilai rule determinism, input quality, volume, repeatability, risk, exception rate, dan system access. Proses yang ambigu atau high-impact membutuhkan review boundary.

**Penjelasan sederhana:** Mesin cocok untuk pekerjaan berulang dengan aturan jelas; pekerjaan yang membutuhkan judgment tetap punya petugas.

### Trigger, action, state

**Definisi teknis:** Trigger memulai workflow; action mengubah atau membaca sistem; state menyimpan posisi/progress agar workflow dapat dilanjutkan dan dideduplikasi.

**Penjelasan sederhana:** Trigger adalah bel, action adalah langkah kerja, state adalah buku catatan agar pekerjaan tidak diulang.

### ROI dan failure cost

**Definisi teknis:** ROI automation harus memasukkan time saved, error avoided, infrastructure/license, monitoring, maintenance, incident, dan opportunity cost.

**Penjelasan sederhana:** Menghemat lima menit tidak sepadan jika satu kegagalan menghentikan pengiriman satu kota.

## Automation canvas Kirimin

Tulis proses sebagai `event → decision → action → confirmation → exception → owner`. Tandai langkah yang side effect, irreversible, atau menyentuh PII/uang.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin image/release saat deploy | workflow automation |

## Referensi resmi

- [n8n documentation](https://docs.n8n.io/)
- [n8n workflow concepts](https://docs.n8n.io/getting-started/)

## Lanjut ke praktik

Notebook membuat automation canvas dan score fit sederhana.

## Posisi part dalam bootcamp

Part ini memulai Fase 3 dengan mengubah pain point bisnis menjadi kandidat automation. Anda membawa data contract, AI risk, dan reliability mindset dari fase sebelumnya. Fokus awalnya adalah process fit dan decision quality, bukan langsung membuat workflow.

## Kapan konsep ini dipakai

Gunakan automation ketika proses berulang, aturan cukup jelas, input tersedia, dan benefit lebih besar daripada maintenance/risk. Jangan otomatisasi proses yang belum dipahami, sering berubah, atau memerlukan judgment high-impact tanpa human approval.

## Walkthrough terpandu: shipment exception

1. Petakan proses saat shipment terlambat: trigger, actor, data input, decision, action, exception, dan outcome.
2. Pisahkan langkah deterministic dari langkah yang memerlukan AI atau human review.
3. Hitung volume, waktu manual, failure impact, SLA, dan dependency.
4. Nilai automation fit dengan score yang memiliki definisi, bukan preferensi.
5. Rancang state machine dari detected, enriched, notified, acknowledged, resolved, dan failed.
6. Tentukan idempotency key dan owner untuk setiap exception path.
7. Pilih satu slice kecil untuk prototype dan tulis non-goals.

## Latihan terbimbing

- Buat inventory sepuluh proses.
- Bandingkan automation penuh, human-assisted, dan manual.
- Identifikasi hidden state dan duplicate trigger.
- Buat ROI kasar tiga kandidat.
- Tulis decision memo untuk satu proses.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjelaskan proses as-is, target outcome, state, exception, owner, risk, dan alasan mengapa automation dipilih.

## Jembatan ke assignment

Assignment harus menghasilkan process inventory, fit score, canvas, prioritization, human boundary, dan decision memo yang menjadi input ke Part 2.
