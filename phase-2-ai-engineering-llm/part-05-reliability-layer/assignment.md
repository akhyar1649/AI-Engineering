# Assignment — Reliability Layer

## Konteks kasus

Assistant SOP harus tetap aman ketika model timeout, rate limit, output invalid, atau evidence kosong.

## Tugas dan requirement

1. Buat reliability wrapper dengan timeout, retry/backoff, dan reason code.
2. Validasi structured output dan domain policy.
3. Buat fallback/human review path untuk sensitive query.
4. Buat test matrix untuk transient, permanent, invalid, dan policy failure.
5. Ukur success rate, fallback rate, latency, dan cost.

## Kriteria penilaian

- 25% failure classification.
- 25% retry/fallback correctness.
- 25% validation/safety.
- 15% metrics.
- 10% tests.

## Format pengumpulan

```text
submission/
├── reliability.py
├── policy.md
├── tests/
└── evaluation-report.md
```

## Estimasi waktu

3–4 jam.

## Prasyarat dari part ini

Sebelum mengerjakan, jalankan notebook part ini dan pahami baseline, input/output contract, failure mode, serta checkpoint pada materi. Gunakan data dan dokumen sintetis PT Kirimin; jangan mengirim data pelanggan nyata ke provider.

## Tools yang digunakan

- Python 3.14.7 dan Jupyter untuk implementasi serta eksperimen.
- OpenAI SDK 3.15.0, LangChain 1.x, Pinecone SDK 10.0.0, Gemini adapter, Transformers 5.17.0, atau Ollama sesuai scope tugas.
- DeepEval dan/atau evaluator lokal untuk evaluation; LangSmith hanya jika trace provider digunakan dan data telah disanitasi.
- Fake model, fake retriever, atau local adapter untuk mode tanpa credential.
- Docker Engine 29.6.2 bila service perlu dijalankan sebagai container.
- Git untuk versioning prompt, index, dataset, model, dan code.

Versi dan sumber ada di docs/00-tech-stack-version-log.md. API key wajib berasal dari environment variable atau secret manager. Catat model/provider identifier, prompt/index version, latency, token/cost signal bila tersedia, dan mode local/mock.

## Langkah pengerjaan

1. Tetapkan task, user, risk level, success metric, dan non-goal.
2. Jalankan notebook untuk memperoleh baseline dan pahami contoh output.
3. Tulis contract: input schema, output schema, evidence/citation, timeout, retry, fallback, escalation, dan side-effect boundary.
4. Implementasikan satu vertical slice dengan fake dependency lebih dahulu.
5. Tambahkan test untuk grounded/normal case dan minimal dua failure case: empty evidence, invalid output, provider error, prompt injection, stale data, atau wrong tool.
6. Jalankan evaluasi pada fixture versioned; bandingkan baseline dan candidate dengan metric yang sesuai.
7. Simpan sanitized trace, sample output, experiment log, limitation, dan cara menjalankan local mode.

## Output dan bukti yang harus terlihat

Submission harus memuat code/contract yang diminta, test, eval dataset atau fixtures, sample answer/trace, dan README. Setiap jawaban AI harus dapat ditelusuri ke evidence atau menyatakan abstain. Setiap agent/tool harus memiliki permission, max step, timeout, validation, dan approval bila ada side effect.

## Self-check sebelum submit

- [ ] Tidak ada API key, PII, atau raw provider payload sensitif.
- [ ] Model, prompt, index, dan dataset memiliki version atau identifier.
- [ ] Output divalidasi schema dan failure path memiliki fallback.
- [ ] Ada metric quality dan bukan hanya demo manual.
- [ ] Trace mencatat request/correlation id tanpa membocorkan secret.
- [ ] Ada regression case untuk failure utama.
- [ ] Notes menyebut kapan LLM tidak dipakai dan keterbatasan local/mock.
- [ ] Cost, latency, privacy, dan human review dibahas bila relevan.

## Hubungan dengan part berikutnya

Simpan contract dan fixtures secara stabil. Part berikutnya akan memakai output ini untuk RAG, agent, serving, evaluation, governance, atau troubleshooting sehingga perubahan schema harus versioned dan didokumentasikan.
