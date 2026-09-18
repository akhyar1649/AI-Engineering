# n8n Data Handling & Logic

**Fase:** 3 — Automation  
**Section:** Automation & n8n Foundations

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membaca dan mengubah item JSON tanpa kehilangan context;
- memakai IF, Switch, Merge, Loop, dan batching dengan benar;
- membedakan per-item dan per-workflow behavior;
- menangani null, array, pagination, dan schema variation;
- membuat workflow deterministic dan idempotent.

## Konteks di PT Kirimin

Satu webhook dapat membawa beberapa shipment event. Workflow harus memproses setiap item, menggabungkan hasil dari database dan API, lalu mengirim notifikasi hanya sekali.

## Konsep kunci

### Item model dan shape

**Definisi teknis:** n8n workflow memproses item data antar node; mapping expression bergantung pada JSON path dan execution context. Shape contract mengurangi breakage.

**Penjelasan sederhana:** Setiap paket memiliki label; node harus tahu apakah sedang memegang satu paket atau satu keranjang.

### Branch, merge, loop

**Definisi teknis:** Branch memilih path; merge menggabungkan stream dengan aturan key/ordering; loop memproses batch dan harus memiliki termination/pagination guard.

**Penjelasan sederhana:** Memisahkan paket berdasarkan tujuan, mempertemukan kembali daftar, dan memastikan conveyor tidak berputar selamanya.

### Idempotency

**Definisi teknis:** Idempotency key dan dedup store mencegah side effect berulang ketika execution diulang. Key harus stabil terhadap retry dan memiliki retention.

**Penjelasan sederhana:** Satu event yang dikirim ulang tidak boleh membuat dua notifikasi.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | JSON handling dan logic |
| PostgreSQL | 18.6 | idempotency/dedup store example |

## Referensi resmi

- [n8n data transformation](https://docs.n8n.io/data/)
- [n8n loop over items](https://docs.n8n.io/flow-logic/looping/)

## Lanjut ke praktik

Notebook memproses batch event dengan dedup key dan branch result.

## Posisi part dalam bootcamp

Part ini memperdalam transformasi data dan branching di n8n. Anda akan memastikan setiap path memiliki contract dan item tidak hilang diam-diam saat workflow memproses banyak event.

## Kapan konsep ini dipakai

Gunakan node logic untuk mapping ringan, filter, merge, split, dan routing. Pindahkan transformasi panjang ke tested service agar workflow tetap dapat dibaca dan dirawat.

## Walkthrough terpandu: route event per severity

1. Terima array shipment events dan validasi setiap item.
2. Gunakan event_id sebagai idempotency key; pisahkan duplicate dari invalid.
3. Enrich city and merchant dari lookup service.
4. Hitung severity berdasarkan SLA yang telah didefinisikan, bukan intuisi node.
5. Route critical ke human approval, warning ke notification, dan normal ke audit.
6. Gabungkan hasil dengan status per item: processed, rejected, duplicate, atau failed.
7. Pastikan workflow response merangkum counts dan correlation_id.

## Latihan terbimbing

- Uji array kosong, satu item, dan mixed-validity.
- Buat branch yang mempertahankan rejected item.
- Uji merge ketika lookup timeout.
- Tambahkan schema version.
- Bandingkan expression dengan Code node terpisah.

## Checkpoint penguasaan

Anda siap lanjut jika tidak ada item yang hilang tanpa status, branch dapat dilacak, dan transformasi memiliki test fixture.

## Jembatan ke assignment

Assignment harus berisi workflow, input/output samples, branch explanation, test fixtures, error summary, dan design note.
