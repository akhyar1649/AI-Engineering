# Capstone 2 — Kirimin Support Intelligence

## Konteks bisnis

Fajar ingin mengurangi pertanyaan repetitif customer support tanpa membuat agent percaya pada jawaban yang tidak memiliki evidence. Solusi harus menjawab FAQ SOP, mengambil angka sederhana dari structured data, dan melakukan handoff untuk kasus berisiko.

## Tantangan

Bangun AI integrated system dengan ingestion dokumen SOP sintetis, RAG, structured query boundary, output contract, evaluation set, monitoring trace, risk controls, dan deployment demo.

## Deliverable wajib

1. **Repository code:** ingestion, retrieval, prompt/chain/agent boundary, tests, evaluation, API, README, dan version log.
2. **Aplikasi live deploy:** URL/demo atau reproduksi container yang dapat diverifikasi mentor, menggunakan data sintetis.
3. **Laporan/presentasi:** architecture, dataset/data card, retrieval metrics, safety policy, cost/latency, failure demo, dan trade-off.

## Scope minimum

- minimal 30 SOP chunks dengan version/effective date/access label;
- minimal 40 evaluation cases, termasuk no-evidence, conflict, injection, structured query, dan sensitive request;
- citation untuk setiap answer grounded;
- abstain/human review policy;
- structured query allowlist yang read-only;
- metrics retrieval, groundedness, latency, cost estimate, and escalation;
- runbook serta rollback/kill switch.

## Timeline yang disarankan

| Hari | Fokus | Output |
|---|---|---|
| 1 | data card, risk, schema | manifest dan policy |
| 2 | retrieval/structured | RAG prototype |
| 3 | reliability/agent/API | integrated service |
| 4 | eval/monitor/deploy | benchmark dan demo |
| 5 | hardening/presentasi | final submission |

## Prasyarat dan hubungan dengan Fase 2

Capstone ini dikerjakan setelah Part 1–15. Peserta harus sudah memahami model selection, prompt contract, ingestion/chunking, RAG, structured retrieval, reliability wrapper, agent tool contract, serving, cost/latency, evaluation, governance, dan troubleshooting. Gunakan artifact Capstone 1 sebagai source data bila tersedia; jika belum, gunakan dataset Kirimin sintetis dengan schema dan quality contract yang setara.

## Tools yang digunakan

- Python 3.14.7 dan Jupyter untuk baseline, app, fixtures, tests, dan evaluation.
- OpenAI SDK 3.15.0, LangChain 1.x, Pinecone SDK 10.0.0, Gemini adapter, Transformers 5.17.0, atau Ollama sesuai jalur arsitektur.
- DeepEval atau evaluator lokal untuk evaluation; LangSmith hanya dengan trace yang sudah disanitasi.
- PostgreSQL 18.6 atau mock structured-data adapter untuk pertanyaan KPI.
- FastAPI dan Docker Engine 29.6.2 untuk service/deployment.
- Git untuk versioning prompt, index, dataset, model, dan code.

Provider API dapat diganti mock/local mode. Submission wajib menjelaskan contract yang sama, perbedaan quality/latency, dan cara mengganti adapter saat credential tersedia.

## Rencana pengerjaan dan milestone wajib

### Milestone 1 — Use case dan baseline

Pilih customer-support intelligence atau operations intelligence. Tulis problem, user, non-goal, risk tier, baseline question set, expected behavior, model selection, dan output contract. Exit criteria: sepuluh kasus baseline dapat dijalankan tanpa provider secret.

### Milestone 2 — Data/evidence layer

Bangun ingestion, metadata, versioning, chunk/index atau structured query contract. Uji stale document, access filter, empty evidence, dan update/delete. Exit criteria: setiap evidence memiliki id/version/source dan retrieval report tersedia.

### Milestone 3 — AI application dan reliability

Implementasikan RAG/structured assistant/agent dengan schema validation, citation, abstention, timeout, retry, fallback, max-step, approval, dan sanitized trace. Exit criteria: normal dan failure path dapat didemokan.

### Milestone 4 — Evaluation dan risk

Buat eval dataset, rubric, baseline/candidate comparison, error analysis, risk register, threat model, controls, monitoring, dan release gate. Exit criteria: perubahan tidak dipromosikan hanya berdasarkan satu demo.

### Milestone 5 — Serving dan komunikasi

Containerize atau deploy service, tambahkan health/observability, cost-latency result, rollback, runbook, report, dan presentation. Exit criteria: mentor dapat menjalankan local mode dan memahami kebutuhan production.

## Definition of done

- [ ] Baseline dan candidate dibandingkan dengan dataset serta metric yang jelas.
- [ ] Jawaban memiliki evidence/citation atau abstain ketika evidence tidak cukup.
- [ ] Structured query/tool dibatasi schema, permission, timeout, dan side-effect policy.
- [ ] Prompt/index/model version, trace sanitized, latency, cost signal, dan fallback terlihat.
- [ ] Minimal lima failure case diuji dan memiliki mitigation atau escalation.
- [ ] Risk register memiliki owner, control, evidence, residual risk, dan kill switch/rollback.
- [ ] Service/local deployment reproducible, test dan evaluation dapat dijalankan ulang.
- [ ] Report dan presentasi menjelaskan trade-off quality, latency, cost, privacy, dan maintainability.
