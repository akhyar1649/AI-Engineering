# n8n Fundamentals

**Fase:** 3 — Automation  
**Section:** Automation & n8n Foundations

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menjelaskan workflow, node, connection, execution, credential, dan expression;
- membuat workflow trigger-to-action sederhana;
- memisahkan credential dari workflow definition;
- menguji workflow pada sample input;
- mengekspor workflow tanpa secret.

## Konteks di PT Kirimin

Sari ingin workflow yang menerima webhook shipment dan mengirim notifikasi. Anda harus memahami execution data dan credential boundary sebelum menyambungkan sistem sungguhan.

## Konsep kunci

### Workflow dan node

**Definisi teknis:** Workflow adalah graph node yang mengeksekusi trigger, transform, decision, integration, dan output. Node memiliki input/output contract dan execution metadata.

**Penjelasan sederhana:** Workflow adalah jalur kerja; node adalah stasiun yang melakukan satu pekerjaan.

### Credentials

**Definisi teknis:** Credential menyimpan secret/config untuk koneksi, idealnya dikelola n8n secret store atau environment. Export workflow harus tidak mengekspos value.

**Penjelasan sederhana:** Workflow boleh menyebut loker mana yang dipakai, tetapi tidak menulis kunci loker di papan publik.

### Expressions dan data shape

**Definisi teknis:** Expression mengambil value dari execution context. Perubahan JSON shape dapat memutus node downstream, sehingga sample contract dan validation penting.

**Penjelasan sederhana:** Jika stasiun berikutnya mengharapkan label `shipment_id` tetapi stasiun sebelumnya mengirim `id`, conveyor berhenti.

## Workflow pertama

`Webhook → Validate payload → IF delivered? → Notify customer / Create exception`. Tambahkan correlation id dan idempotency key sejak awal.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin image/release saat deploy | workflow editor/runtime |

## Referensi resmi

- [n8n workflows](https://docs.n8n.io/workflows/)
- [n8n credentials](https://docs.n8n.io/credentials/)
- [n8n expressions](https://docs.n8n.io/code/expressions/)

## Lanjut ke praktik

Notebook merepresentasikan workflow n8n sebagai graph JSON sederhana.

## Posisi part dalam bootcamp

Part ini memperkenalkan n8n sebagai execution environment untuk process yang telah dipilih. Anda belajar membaca workflow sebagai graph trigger → action → state, memahami node input/output, dan menjaga credential boundary.

## Kapan konsep ini dipakai

Gunakan n8n untuk menghubungkan API, database, notification, dan approval dengan cepat. Gunakan code service terpisah untuk logic kompleks, heavy computation, atau domain yang membutuhkan testing dan versioning lebih ketat.

## Walkthrough terpandu: webhook shipment event

1. Buat Webhook trigger dengan schema event_id, order_id, status, event_at, dan signature.
2. Validasi payload dan signature sebelum node berikutnya.
3. Normalisasi field dan tambahkan correlation_id.
4. Lookup order atau ledger dengan read-only credential.
5. Route status delayed ke notification draft dan status normal ke audit path.
6. Tambahkan response code yang sesuai, log execution metadata, dan jangan menulis secret.
7. Export workflow JSON, simpan version, dan jalankan fixture tanpa sistem eksternal menggunakan mock.

## Latihan terbimbing

- Buat workflow happy path dan invalid payload.
- Tambahkan environment-specific credential.
- Uji duplicate webhook.
- Pisahkan configuration dari expression.
- Buat README import/run/test.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjelaskan input/output setiap node, workflow dapat diimport ulang, credential aman, dan error path terlihat.

## Jembatan ke assignment

Assignment harus mengumpulkan workflow JSON, fixture, contract, README, execution evidence, dan limitations local/mock.
