# AI on Automation

**Fase:** 3 — Automation  
**Section:** AI-Driven Automation & Solution Design

> Diverifikasi: OpenAI Python SDK v3.15.0 — sumber: https://github.com/openai/openai-python/releases — tanggal cek: 2026-09-18
> Diverifikasi: Gemini model documentation — sumber: https://ai.google.dev/gemini-api/docs/models — tanggal cek: 2026-09-18
> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- memilih langkah automation yang benar-benar membutuhkan AI;
- merancang classify, extract, summarize, route, dan tool-use pattern;
- mengisolasi AI dari side effect tanpa approval;
- memvalidasi output dan menangani uncertainty;
- menghitung cost/latency serta fallback.

## Konteks di PT Kirimin

Pesan customer tidak selalu terstruktur. AI dapat mengklasifikasikan kategori dan merangkum ticket, tetapi tidak boleh memutuskan refund atau mengubah status finansial sendiri.

## Konsep kunci

### AI as bounded component

**Definisi teknis:** AI component menerima input terdefinisi dan menghasilkan output terstruktur dengan confidence/evidence; workflow deterministik tetap memegang policy dan side effect.

**Penjelasan sederhana:** AI boleh menjadi petugas membaca surat, tetapi supervisor tetap menekan tombol tindakan.

### Human-in-the-loop

**Definisi teknis:** Human review dipicu oleh risk class, uncertainty, policy boundary, or failure. Handoff harus membawa context, recommendation, and audit trail.

**Penjelasan sederhana:** Manusia harus menerima paket lengkap, bukan hanya pesan “AI gagal”.

### AI fallback

**Definisi teknis:** Fallback dapat berupa deterministic rule, template, queue, or unavailable response. Fallback tidak boleh diam-diam melakukan action berisiko.

**Penjelasan sederhana:** Jika AI tidak yakin, gunakan checklist manual atau antrekan ke staf.

## Pattern Kirimin

`ticket → redact → classify → confidence gate → RAG/summary → human approve → CRM/notification`. Classification membantu routing; ia bukan sumber keputusan final.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| OpenAI Python SDK | 3.15.0 | model adapter |
| Gemini API | stable model; pin saat deploy | provider option |
| n8n | 2.x; pin release | workflow |

## Referensi resmi

- [OpenAI function calling](https://platform.openai.com/docs/guides/function-calling)
- [Gemini API docs](https://ai.google.dev/gemini-api/docs)
- [n8n documentation](https://docs.n8n.io/)

## Lanjut ke praktik

Notebook membuat AI classification mock dengan confidence gate dan human route.

## Posisi part dalam bootcamp

Part ini memasukkan AI ke workflow yang sudah reliable. Anda akan menentukan titik yang cocok untuk classification, extraction, summarization, atau decision support, lalu mempertahankan schema, risk, evaluation, and approval boundary dari Fase 2.

## Kapan konsep ini dipakai

Gunakan AI untuk input yang tidak terstruktur atau aturan yang terlalu variatif, tetapi tetap gunakan deterministic validation untuk output. Jangan memberikan agent permission side effect hanya karena workflow membutuhkan fleksibilitas.

## Walkthrough terpandu: triage email partner

1. Terima email dan simpan raw dengan correlation_id.
2. Redact atau classify data sebelum dikirim ke model.
3. Minta model mengeluarkan schema category, urgency, entities, evidence, and confidence.
4. Validasi JSON dan taxonomy; invalid output masuk exception.
5. Route low-risk category otomatis, high-risk ke human approval.
6. Catat model/prompt version, token/cost, latency, and outcome.
7. Evaluasi false escalation dan missed escalation, lalu ubah prompt/model hanya melalui versioned release.

## Latihan terbimbing

- Buat fake model adapter.
- Uji prompt injection dalam email.
- Tambahkan confidence threshold dan human review.
- Buat fallback rule-based.
- Tulis regression cases dari error.

## Checkpoint penguasaan

Anda siap lanjut jika AI step memiliki input/output contract, guardrail, fallback, evaluation, and observability.

## Jembatan ke assignment

Assignment harus berisi workflow, AI contract, adapter/mock, tests, safety boundary, evaluation set, traces, and cost note.
