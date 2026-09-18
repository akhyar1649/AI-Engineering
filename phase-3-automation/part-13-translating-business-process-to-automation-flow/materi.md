# Translating Business Process to Automation Flow

**Fase:** 3 — Automation  
**Section:** AI-Driven Automation & Solution Design

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- memetakan as-is process dan pain point;
- mengidentifikasi decision, handoff, exception, dan system of record;
- mengubah BPMN-like flow menjadi workflow implementable;
- mendefinisikan acceptance criteria dan KPI;
- memvalidasi desain dengan stakeholder.

## Konteks di PT Kirimin

Proses update shipment melibatkan Ops, customer support, courier partner, dan finance. Automation harus mengikuti proses nyata, bukan hanya gambar happy path.

## Konsep kunci

### Process discovery

**Definisi teknis:** Process discovery mengumpulkan actor, trigger, input, output, decision, SLA, exception, system, dan policy dari pemilik proses.

**Penjelasan sederhana:** Sebelum membuat conveyor, lihat bagaimana orang benar-benar memindahkan barang, termasuk saat label rusak.

### To-be workflow

**Definisi teknis:** To-be design mengurangi manual handoff, tetapi mempertahankan control point, approval, evidence, dan ownership yang diperlukan.

**Penjelasan sederhana:** Tujuannya bukan membuat semua langkah otomatis, tetapi membuat proses lebih aman dan jelas.

### Acceptance criteria

**Definisi teknis:** Acceptance criteria menetapkan observable conditions untuk correctness, timing, error handling, security, and user outcome.

**Penjelasan sederhana:** “Workflow selesai” harus berarti event tercatat dan customer menerima notifikasi, bukan hanya node terakhir hijau.

## Process canvas Kirimin

`actor → trigger → data → decision → automation → approval → side effect → evidence → exception owner`. Tandai system of record pada tiap state.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | flow implementation |

## Referensi resmi

- [n8n workflow design](https://docs.n8n.io/workflows/)
- [n8n best practices](https://docs.n8n.io/hosting/scaling/best-practices/) 

## Lanjut ke praktik

Notebook mengubah process steps menjadi node candidates dan acceptance checks.

## Posisi part dalam bootcamp

Part ini melatih translasi dari bahasa stakeholder ke workflow yang implementable. Anda akan menjaga agar setiap langkah bisnis memiliki input, rule, owner, output, exception, dan measurable outcome.

## Kapan konsep ini dipakai

Gunakan process translation sebelum membuka tool builder. Ia mencegah automation dibangun dari asumsi engineer dan membantu menemukan langkah yang belum memiliki data atau policy.

## Walkthrough terpandu: onboarding merchant

1. Tulis as-is dari trigger merchant approved sampai first shipment.
2. Interview stakeholder persona dan catat fakta versus asumsi.
3. Ubah setiap aktivitas menjadi contract: input, decision, action, owner, SLA, and evidence.
4. Tandai manual judgment, system-of-record, and exception.
5. Buat to-be flow dengan happy path dan failure path.
6. Pilih automation boundary, human approval, and phased rollout.
7. Tulis acceptance criteria yang dapat diuji dengan data sintetis.

## Latihan terbimbing

- Buat swimlane process map.
- Temukan ambiguity dalam istilah “aktif”.
- Ubah tiga business rule menjadi test case.
- Buat RACI.
- Bandingkan automation candidate dengan non-goal.

## Checkpoint penguasaan

Anda siap lanjut jika stakeholder dapat membaca flow dan menyetujui outcome, boundary, exception, serta bukti sukses.

## Jembatan ke assignment

Assignment harus memuat as-is/to-be, interview synthesis, contracts, decision log, acceptance tests, and proposed workflow.
