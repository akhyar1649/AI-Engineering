# Capstone 3 — Kirimin Shipment Automation

## Konteks bisnis

Sari ingin mengotomasi alur shipment event sampai notifikasi customer dan exception handling. Courier partner memiliki payload dan reliability berbeda. Workflow harus memakai n8n, dapat di-deploy, serta menunjukkan bagaimana AI/MCP dipakai hanya pada boundary yang tepat.

## Tantangan

Bangun integrated automation yang menerima event sintetis, menyimpan ledger, melakukan dedup, memperbarui status, mengirim notifikasi mock/provider adapter, membuat exception ticket, dan menyediakan observability. Tambahkan satu AI step yang bounded, misalnya klasifikasi exception.

## Deliverable wajib

1. **Repository code:** workflow exports, adapters, schemas, tests, runbook, cost model, dan README.
2. **Live deployment:** URL/demo atau self-hosted/container reproduction yang dapat diverifikasi mentor.
3. **Laporan/presentasi:** as-is/to-be, architecture, readiness, SLO, failure demo, security/governance, cost, dan roadmap.

## Scope minimum

- webhook/schedule trigger;
- persistent event ledger dan idempotency;
- normal, duplicate, transient failure, permanent failure, DLQ, dan replay flow;
- notifikasi dan exception route;
- AI classification dengan confidence/human boundary;
- optional MCP read tool dengan scope/audit;
- dashboard/metrics execution dan business outcome;
- deployment/backup/restore/cost documentation.

## Timeline yang disarankan

| Hari | Fokus | Output |
|---|---|---|
| 1 | process/readiness | as-is/to-be, contracts |
| 2 | workflow core | trigger, ledger, dedup |
| 3 | integration/error | notification, DLQ, replay |
| 4 | AI/MCP/observability | bounded intelligence |
| 5 | deploy/test/present | final demo |

## Prasyarat dan hubungan dengan Fase 3

Capstone ini dikerjakan setelah Part 1–15. Peserta harus sudah memahami process mapping, n8n fundamentals, data handling, MCP/tool contract, retry/idempotency, scheduling, integrated system, deployment/cost, self-hosting, observability, AI-on-automation, governance, solution fit, dan integration readiness. Gunakan contract data dari Capstone 1 dan AI adapter dari Capstone 2 bila relevan.

## Tools yang digunakan

- n8n 2.x untuk workflow dan import/export.
- Docker Engine 29.6.2 untuk local/self-hosted runtime.
- Python 3.14.7 untuk fake service, adapter, fixtures, dan contract tests.
- PostgreSQL untuk ledger atau mock/in-memory equivalent dengan contract yang sama.
- Redis bila queue, concurrency, atau idempotency membutuhkan layer tersebut.
- MCP sesuai protocol/adapter yang digunakan untuk tool/resource interface.
- Git untuk versioning workflow, contracts, fixtures, dan runbook.

Gunakan fake courier, fake notification, sandbox, dan dry-run. Deskripsikan setiap credential sebagai environment variable. Jika deployment live tidak memungkinkan, self-hosted local deployment dengan restore evidence dianggap valid sesuai rubric.

## Rencana pengerjaan dan milestone wajib

### Milestone 1 — Process dan integration contract

Pilih satu workflow, tulis as-is/to-be, outcome, trigger, state, dependency, schema, owner, SLA, non-goal, dan automation-fit decision. Exit criteria: semua stakeholder boundary dan failure path tertulis.

### Milestone 2 — Workflow vertical slice

Bangun trigger → validate → enrich → decision → ledger → notification/approval. Sertakan correlation_id, idempotency key, dry-run, dan fake systems. Exit criteria: happy path dan duplicate path lulus.

### Milestone 3 — Reliability dan integration

Tambahkan timeout, retry matrix, dead-letter/exception route, replay, schema drift handling, contract tests, dan readiness scorecard. Exit criteria: partial failure tidak menggandakan side effect dan dapat direplay.

### Milestone 4 — Deploy dan observe

Jalankan local/self-hosted environment, persistent storage, secret boundary, backup/restore, health, metrics, alerts, SLO, cost model, runbook, dan rollback. Exit criteria: clean-room operator dapat menjalankan dan memulihkan demo.

### Milestone 5 — AI/MCP dan komunikasi

Jika memakai AI/MCP, tambahkan output schema, permission, prompt injection test, approval gate, evaluation, and trace. Lengkapi report/presentation dengan architecture, trade-off, risk, cost, dan roadmap.

## Definition of done

- [ ] Workflow dapat diimport dan dijalankan pada local/mock/self-hosted mode.
- [ ] Trigger, node/service contract, state, owner, dan exception path jelas.
- [ ] Duplicate, retry, timeout, partial success, dan schema drift diuji.
- [ ] Side effect dapat dibuktikan idempotent, dry-run, atau human-approved.
- [ ] Ada ledger/DLQ/replay evidence, correlation trace, metrics, alert, dan runbook.
- [ ] Deployment, backup/restore, rollback, security, retention, dan cost terdokumentasi.
- [ ] Readiness scorecard dan remediation plan tersedia untuk dependency partner.
- [ ] Report dan presentasi memperlihatkan normal/failure demo serta keputusan yang diminta.
