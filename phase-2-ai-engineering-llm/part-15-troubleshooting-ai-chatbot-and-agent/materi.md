# Troubleshooting AI Chatbot and Agent

**Fase:** 2 — AI Engineering (LLM)  
**Section:** Deployment, Evaluation & Governance

> Diverifikasi: LangSmith documentation — sumber: https://docs.smith.langchain.com/ — tanggal cek: 2026-09-18
> Diverifikasi: DeepEval documentation — sumber: https://deepeval.com/docs/introduction — tanggal cek: 2026-09-18

## Tujuan belajar

- mendiagnosis failure pada routing, retrieval, prompt, tool, model, dan presentation;
- memakai trace untuk menemukan root cause tanpa melog PII berlebihan;
- membedakan regression, drift, outage, dan policy violation;
- membuat runbook dan reproducible test case;
- menyusun corrective action dengan owner dan verification.

## Konteks di PT Kirimin

Assistant tiba-tiba memberi jawaban SOP lama dan agent mencoba memanggil tool refund. Fajar membutuhkan mitigasi cepat; Reza membutuhkan root cause dan perubahan permanen.

## Konsep kunci

### Failure taxonomy

**Definisi teknis:** Failure taxonomy memetakan symptom ke stage: input, routing, retrieval, context assembly, generation, tool, output validation, UX, infrastructure, policy.

**Penjelasan sederhana:** Sebelum memperbaiki mesin, cari tahu apakah masalah ada di pesanan, rak, petugas, atau pintu keluar.

### Reproduction

**Definisi teknis:** Reproduction menyimpan minimal sanitized input, versions, retrieved ids, tool decisions, and expected behavior. Jangan mengandalkan prompt lengkap production jika mengandung data sensitif.

**Penjelasan sederhana:** Kasus yang bisa diulang lebih mudah diperbaiki daripada cerita “tadi sempat salah”.

### Rollback dan kill switch

**Definisi teknis:** Rollback mengembalikan model/prompt/index/config ke known-good version; kill switch mematikan route/tool berisiko tanpa redeploy seluruh sistem.

**Penjelasan sederhana:** Jika fitur baru berbahaya, tutup kerannya dulu sambil mencari penyebab.

## Runbook Kirimin

1. Triage impact dan policy risk.
2. Freeze version/trace sample.
3. Compare expected versus actual stage output.
4. Disable unsafe route or fallback human.
5. Reproduce sanitized case.
6. Patch, evaluate regression, deploy canary, verify, document.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| LangSmith | current hosted platform; record date | trace |
| DeepEval | pin evaluation environment | regression |

## Referensi resmi

- [LangSmith observability](https://docs.smith.langchain.com/observability)
- [DeepEval](https://deepeval.com/docs/introduction)
- [OpenAI evals](https://platform.openai.com/docs/guides/evals)

## Lanjut ke praktik

Notebook mengklasifikasikan trace failure dan memilih mitigasi.

## Posisi part dalam bootcamp

Part ini mengintegrasikan semua teknik Fase 2 dalam kegiatan incident response. Anda akan menganalisis trace dari data ingestion sampai UI/tool, memilih mitigation, dan mengubah insiden menjadi regression test.

## Kapan konsep ini dipakai

Gunakan playbook ini ketika assistant menjawab salah, tidak merespons, memanggil tool keliru, membocorkan data, atau biaya/latency melonjak. Mulai dari request_id dan trace, bukan dari asumsi bahwa model adalah satu-satunya penyebab.

## Walkthrough terpandu: SOP lama dan tool salah

1. Bekukan trace sanitized: input class, retrieved ids/versions, tool calls, model/prompt/index version, timings, errors, and final state.
2. Reproduce dengan fixture yang sama dalam local/mock mode.
3. Cari layer pertama yang berbeda dari expected: stale index, wrong filter, prompt injection, wrong tool schema, model output, parser, atau UI rendering.
4. Pilih mitigation immediate: disable tool, force human review, rollback prompt/index/model, or switch to fallback.
5. Tulis root cause dan contributing factors. Jangan hanya menulis “LLM hallucination”.
6. Tambahkan regression test dan monitoring signal yang akan mendeteksi recurrence.
7. Tutup incident setelah evidence recovery, stakeholder communication, dan owner corrective action tersedia.

## Latihan terbimbing

- Triage five traces dengan failure berbeda.
- Buat decision tree untuk retrieval versus tool misuse.
- Simulasikan kill switch dan rollback.
- Tulis postmortem tanpa PII.
- Tambahkan one-click reproduction command untuk mentor.

## Checkpoint penguasaan

Anda siap menyelesaikan Capstone 2 jika dapat menganalisis trace end-to-end, memilih containment yang aman, dan membuktikan perbaikan dengan regression test serta metric.

## Jembatan ke assignment

Assignment harus berisi taxonomy, sanitized traces, reproduction fixtures, runbook, postmortem, tests, rollback/kill switch design, dan ownership matrix.
