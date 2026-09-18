# Final Project — Kirimin Data & AI-Driven Operations Strategy

## Konteks

PT Kirimin Digital Nusantara ingin memilih satu investasi strategis berikutnya: (A) data + AI untuk customer support intelligence, atau (B) data + automation untuk shipment operations. Anda bertindak sebagai engineer-consultant yang menyusun solusi dari problem framing sampai development strategy.

## Pilihan scope

Pilih salah satu jalur dan nyatakan alasannya:

- **Jalur A — Data + AI:** RAG/structured assistant, evaluation, governance, deployment, dan operating model.
- **Jalur B — Data + Automation:** workflow n8n, integrations, reliability, deployment, observability, dan operating model.

Keduanya wajib memakai data sintetis dan menghubungkan keputusan dengan stakeholder Kirimin.

## Deliverable wajib

1. Problem framing dan stakeholder interview synthesis.
2. Current-state/as-is dan target-state/to-be.
3. Requirements, non-goals, assumptions, risks, and success metrics.
4. Architecture diagram dan data/integration contracts.
5. Development strategy: milestones, backlog, team roles, testing, CI/CD, environments, rollout, and rollback.
6. Working code/pipeline/workflow dengan tests.
7. Live deployment/demo dan runbook.
8. Cost, capacity, security, privacy, governance, and operational plan.
9. Written report dan presentation untuk Dinda, Reza, Fajar, dan Sari.

## Tahapan yang disarankan

| Tahap | Pertanyaan kunci | Artefak |
|---|---|---|
| Discover | Masalah siapa dan seberapa besar? | problem brief, stakeholder map |
| Define | Outcome dan batasannya apa? | requirements, KPI, risk register |
| Design | Sistem apa yang dibutuhkan? | architecture, contracts, ADR |
| Build | Increment pertama apa? | backlog, code/workflow, tests |
| Validate | Bagaimana membuktikan benar/aman? | evaluation, acceptance, demo |
| Deploy | Bagaimana release dan recover? | deployment, runbook, rollback |
| Operate | Bagaimana mengukur dan memperbaiki? | SLO, monitoring, roadmap |

## Batasan penting

- Tidak boleh menggunakan data pelanggan nyata.
- Jangan mengklaim production readiness tanpa evidence deployment, test, security, dan recovery.
- AI tidak boleh memiliki side effect high-impact tanpa human approval.
- Semua harga/provider/version yang berubah harus diverifikasi ulang saat implementasi.

## Prasyarat dan hubungan dengan bootcamp

Final project menggabungkan Fase 1, Fase 2, dan Fase 3. Peserta harus memilih artifact yang benar-benar diperlukan, bukan menyalin semua tool. Jalur A memerlukan data contract, evidence/RAG atau structured retrieval, evaluation, governance, serving, dan deployment. Jalur B memerlukan process map, integration contract, n8n workflow, reliability, observability, deployment, dan integration readiness. Kedua jalur wajib membawa problem framing, testing, security, cost, rollback, dan stakeholder communication.

## Tools yang digunakan

### Tools bersama

Python 3.14.7, Jupyter, PostgreSQL 18.6 atau mock relational adapter, Docker Engine 29.6.2, Git, diagram tool berbasis Markdown/Mermaid, dan test runner yang tercantum di README.

### Jalur A — Data + AI

OpenAI SDK 3.15.0 atau provider adapter setara, LangChain 1.x bila diperlukan, Pinecone SDK 10.0.0 atau vector adapter/local index, DeepEval atau evaluator lokal, FastAPI, dan LangSmith hanya dengan trace tersanitasi. Gunakan fake model/retriever untuk test deterministik.

### Jalur B — Data + Automation

n8n 2.x, Docker Engine 29.6.2, Python adapter/fake service, PostgreSQL ledger, Redis bila dibutuhkan, dan MCP/tool adapter bila agent memerlukan interface terstandar. Semua external integration harus sandbox/mock atau dry-run.

Tool/provider boleh diganti jika contract, evidence, security, dan operating model tetap setara. Catat versi aktual di docs/00-tech-stack-version-log.md dan verifikasi kembali claim yang berubah.

## Development strategy yang wajib dikumpulkan

### Tahap 1 — Discovery dan decision

Kumpulkan stakeholder synthesis, problem statement, measurable outcome, non-goal, assumption, risk, success metric, dan decision log. Tandai fakta, asumsi, dan pertanyaan yang belum terjawab.

### Tahap 2 — Contract dan architecture

Tulis requirements, data/integration contract, grain/schema, permission, error behavior, architecture diagram, ADR, test strategy, dan acceptance criteria. Pilih MVP vertical slice serta backlog setelah MVP.

### Tahap 3 — Build dan test

Implementasikan vertical slice dengan synthetic fixture, lalu tambahkan normal, edge, failure, security, and recovery test. Version-kan prompt/model/index/workflow bila digunakan. Simpan evidence command dan output.

### Tahap 4 — Validate dan deploy

Jalankan evaluation atau contract test, container/local deployment, smoke test, observability, cost/capacity model, security check, backup/restore, rollback, dan demo. Jangan menyamakan service hidup dengan production readiness.

### Tahap 5 — Operate dan roadmap

Lengkapi SLO/SLA, alert, runbook, incident response, owner, maintenance, vendor/provider risk, technical debt, roadmap 30/60/90 hari, serta keputusan yang diminta dari stakeholder.

## Definition of done

- [ ] Problem, user, outcome, non-goal, requirements, dan acceptance criteria jelas.
- [ ] Architecture dan contracts konsisten dengan implementasi.
- [ ] Working solution berjalan dengan data sintetis dan test evidence tersedia.
- [ ] Normal, failure, security, privacy, rollback, dan recovery path diuji.
- [ ] Deployment/demo dapat direproduksi; live URL hanya diklaim jika benar-benar dapat diakses.
- [ ] Cost, capacity, SLO, monitoring, ownership, dan operating model tersedia.
- [ ] Risk register, governance, human approval, dan limitation dijelaskan.
- [ ] Report serta presentation dapat menjawab pertanyaan Dinda, Reza, Fajar, dan Sari.
- [ ] Backlog perbaikan menunjukkan apa yang belum selesai dan mengapa.
