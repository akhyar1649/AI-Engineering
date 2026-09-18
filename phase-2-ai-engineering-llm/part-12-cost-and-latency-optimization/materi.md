# Cost & Latency Optimization

**Fase:** 2 — AI Engineering (LLM)  
**Section:** Deployment, Evaluation & Governance

> Diverifikasi: OpenAI model documentation — sumber: https://platform.openai.com/docs/models — tanggal cek: 2026-09-18
> Diverifikasi: Gemini model documentation — sumber: https://ai.google.dev/gemini-api/docs/models — tanggal cek: 2026-09-18
> Diverifikasi: Redis documentation — sumber: https://redis.io/docs/latest/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menghitung token/call cost dan end-to-end latency;
- memilih model routing berdasarkan task dan risk;
- memakai caching, prompt/context compression, batching, dan streaming;
- membuat budget guardrail dan cost attribution;
- memastikan optimasi tidak menurunkan quality/safety melewati threshold.

## Konteks di PT Kirimin

Volume pertanyaan naik 4x dan budget AI tidak boleh mengikuti kenaikan secara linear. Fajar tetap meminta accuracy untuk refund dan policy-sensitive queries.

## Konsep kunci

### Cost unit economics

**Definisi teknis:** Cost dapat dimodelkan sebagai input/output tokens, embedding, retrieval, requests, compute, and human review. Unit metric misalnya cost per resolved ticket.

**Penjelasan sederhana:** Hitung biaya per tiket yang selesai, bukan hanya total tagihan bulanan.

### Caching

**Definisi teknis:** Exact/semantic/prefix cache mengurangi repeated work tetapi membutuhkan key design, TTL, invalidation, privacy boundary, dan stale response policy.

**Penjelasan sederhana:** Jawaban FAQ yang sama boleh dipakai ulang, tetapi SOP baru harus membatalkan cache lama.

### Routing dan compression

**Definisi teknis:** Routing memilih model/tool berdasarkan intent, complexity, risk, and context size. Compression mengurangi token/context dengan summarization atau selective retrieval, tetapi perlu loss evaluation.

**Penjelasan sederhana:** Pertanyaan jam operasional tidak membutuhkan mesin besar; pertanyaan ambigu mungkin membutuhkan pemeriksaan lebih mendalam.

## Optimization loop

Baseline → profile → hypothesis → change one variable → evaluate quality/safety → promote with budget guardrail. Jangan mengoptimalkan p95 latency dengan menonaktifkan validation.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| OpenAI API | current official models | model cost/latency |
| Gemini API | stable model list | routing comparison |
| Redis | pin image saat deployment | cache |

## Referensi resmi

- [OpenAI models](https://platform.openai.com/docs/models)
- [Gemini models](https://ai.google.dev/gemini-api/docs/models)
- [Redis expiration](https://redis.io/docs/latest/commands/expire/)

## Lanjut ke praktik

Notebook menghitung cost estimate, cache hit ratio, dan model routing sederhana.

## Posisi part dalam bootcamp

Part ini mengajarkan optimasi berdasarkan budget dan user experience. Anda akan menelusuri cost/latency dari input, retrieval, model, tool, network, dan retry. Perubahan tidak boleh hanya menurunkan cost dengan merusak quality.

## Kapan konsep ini dipakai

Gunakan cost/latency analysis ketika traffic naik, SLA tidak terpenuhi, atau budget perlu dikontrol. Optimasi prompt, model routing, cache, retrieval, batching, streaming, dan concurrency hanya setelah baseline tersedia.

## Walkthrough terpandu: target jawaban support

1. Tetapkan SLO p95 latency, quality threshold, cost per resolved ticket, dan monthly budget.
2. Instrument setiap stage: input token, retrieval time, model time, output token, retry, and fallback.
3. Buat baseline pada representative workload.
4. Uji optimasi satu per satu: prompt compaction, top-k reduction, cache hit, smaller model for classification, or streaming.
5. Evaluasi quality regression pada baseline and adversarial set.
6. Buat routing policy: simple FAQ ke model murah, ambiguous/high-risk ke model lebih kuat atau human.
7. Tetapkan budget guard, rate limit, and alert saat cost/unit atau latency melewati threshold.

## Latihan terbimbing

- Buat cost calculator dari trace.
- Bandingkan cache exact dan semantic.
- Hitung dampak retry terhadap cost.
- Uji batching versus interactive latency.
- Tulis optimization decision log.

## Checkpoint penguasaan

Anda siap lanjut jika setiap optimasi memiliki baseline, metric, guardrail quality, dan rollback condition.

## Jembatan ke assignment

Assignment harus berisi instrumentation, baseline, minimal tiga experiment, cost/latency comparison, quality result, routing policy, and recommendation.
