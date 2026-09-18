# Reliability Layer

**Fase:** 2 — AI Engineering (LLM)  
**Section:** RAG & AI Agent Development

> Diverifikasi: DeepEval documentation — sumber: https://deepeval.com/docs/introduction — tanggal cek: 2026-09-18
> Diverifikasi: FastAPI v0.141.1 — sumber: https://fastapi.tiangolo.com/release-notes/ — tanggal cek: 2026-09-18

## Tujuan belajar

- mendesain timeout, retry, fallback, circuit breaker, dan rate limit untuk AI call;
- memvalidasi output dengan schema dan domain rules;
- memisahkan transient failure dari model/content failure;
- membuat confidence dan human escalation policy;
- mengukur reliability RAG melalui test cases.

## Konteks di PT Kirimin

Satu provider LLM timeout pada jam sibuk, sementara jawaban refund harus selalu melalui review finance. Reliability layer menjaga user experience tanpa mengorbankan policy.

## Konsep kunci

### Reliability boundary

**Definisi teknis:** Reliability boundary adalah tempat sistem menerapkan timeout, retry budget, fallback, validation, dan observability terhadap dependency yang tidak sepenuhnya dikendalikan.

**Penjelasan sederhana:** Setiap pintu keluar kantor harus memiliki batas tunggu dan rencana jika pintu utama macet.

### Structured validation

**Definisi teknis:** Schema validation memeriksa bentuk output; semantic/domain validation memeriksa nilai terhadap aturan bisnis. Keduanya diperlukan.

**Penjelasan sederhana:** Formulir bisa memiliki semua kolom tetapi masih memilih status refund yang tidak boleh.

### Graceful degradation

**Definisi teknis:** Sistem tetap memberi outcome aman saat dependency gagal, misalnya cached answer, retrieval-only response, queue for human, atau explicit unavailable message.

**Penjelasan sederhana:** Jika mesin otomatis rusak, proses tidak boleh mengarang; alihkan paket ke petugas.

## Policy Kirimin

- max model call timeout 8 detik untuk chat;
- retry hanya error transient, maksimal dua kali dengan backoff;
- refund/account access selalu human review;
- no-evidence response tidak boleh terdengar pasti;
- semua fallback diberi reason code.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| DeepEval | pin pada environment evaluasi | metric/evaluation |
| FastAPI | 0.141.1 | service boundary |

## Referensi resmi

- [DeepEval introduction](https://deepeval.com/docs/introduction)
- [FastAPI handling errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
- [OpenAI API error handling guidance](https://platform.openai.com/docs/guides/error-codes)

## Lanjut ke praktik

Notebook menjalankan policy retry/fallback dan output validation tanpa provider eksternal.

## Posisi part dalam bootcamp

Part ini menambahkan lapisan engineering di sekeliling model: schema validation, timeout, retry, circuit breaker, fallback, redaction, dan correlation id. AI feature baru layak digunakan ketika failure dapat terlihat dan ditangani.

## Kapan konsep ini dipakai

Gunakan retry untuk transient failure yang aman diulang, bukan untuk invalid input atau policy violation. Gunakan timeout untuk membatasi tail latency. Gunakan circuit breaker ketika dependency gagal berulang. Gunakan fallback deterministic atau human escalation ketika jawaban tidak dapat dipercaya.

## Walkthrough terpandu: provider timeout dan output invalid

1. Bungkus model call dengan request_id, timeout, model_id, dan prompt_version.
2. Validasi input sebelum request. Jika context kosong, jangan kirim request yang pasti gagal.
3. Parse output ke schema. Jika invalid, lakukan satu repair/retry terbatas atau fallback; jangan loop tanpa batas.
4. Bedakan provider timeout, rate limit, authentication, content policy, dan application validation.
5. Terapkan exponential backoff hanya untuk error retryable dan gunakan idempotency key jika ada side effect.
6. Redact PII/secret dari log, tetapi simpan metadata yang cukup untuk debugging.
7. Uji failure matrix dan ukur success rate, fallback rate, p95 latency, serta cost per request.

## Latihan terbimbing

- Buat fake provider yang timeout, mengembalikan invalid JSON, dan rate limit.
- Tambahkan circuit breaker state open/half-open/closed.
- Buat dead-letter record untuk request yang gagal permanen.
- Uji duplicate request dengan correlation id.
- Tulis runbook untuk provider outage.

## Checkpoint penguasaan

Anda siap lanjut jika dapat mengklasifikasikan error, memilih retry/fallback yang tepat, dan membuktikan log tidak membocorkan data sensitif.

## Jembatan ke assignment

Assignment harus menyertakan reliability wrapper, failure tests, sanitized traces, policy retry, fallback behavior, dan metrics definition.
