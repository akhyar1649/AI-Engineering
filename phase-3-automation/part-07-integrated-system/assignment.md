# Assignment — Integrated System

## Konteks kasus

Bangun integrated workflow shipment-to-notification dengan PostgreSQL ledger mock dan exception route.

## Tugas dan requirement

1. Definisikan contracts untuk webhook, ledger, customer lookup, notification, dan ticket.
2. Implementasikan correlation/idempotency.
3. Tambahkan timeout/retry/compensation per dependency.
4. Buat end-to-end tests dengan fake systems.
5. Dokumentasikan orchestration/choreography decision.

## Kriteria penilaian

- 25% contracts.
- 25% failure/idempotency.
- 20% integration flow.
- 20% tests/observability.
- 10% architecture reasoning.

## Format pengumpulan

```text
submission/
├── workflow.json
├── contracts/
├── fake_services.py
├── tests/
└── architecture.md
```

## Estimasi waktu

3–5 jam.

## Prasyarat dari part ini

Sebelum mengerjakan, jalankan notebook atau fixture part ini dan pahami process map, trigger, state, dependency, serta exception path pada materi. Gunakan fake service, sandbox, dry-run, atau local runtime; jangan mengirim notification ke customer nyata.

## Tools yang digunakan

- n8n 2.x untuk workflow dan import/export JSON.
- Docker Engine 29.6.2 untuk local n8n atau dependency yang diperlukan.
- Python 3.14.7 untuk adapter, fake service, fixture, dan contract test.
- PostgreSQL untuk ledger/serving mock atau adapter in-memory jika scope mengizinkan.
- Redis bila queue/idempotency exercise membutuhkannya.
- MCP sesuai contract/spec yang dipakai pada part, dengan tool permission terbatas.
- Git untuk versioning workflow, contracts, fixtures, dan runbook.

Versi dan sumber ada di docs/00-tech-stack-version-log.md. Credential harus berupa placeholder/environment variable. Workflow export tidak boleh menyimpan secret, personal token, atau data pelanggan.

## Langkah pengerjaan

1. Nyatakan outcome bisnis, trigger, input/output contract, owner, SLA, dan non-goal.
2. Gambar atau tulis state machine: normal, duplicate, invalid, retrying, failed, approved, resolved.
3. Implementasikan happy path dengan fake dependency dan correlation_id.
4. Tambahkan idempotency key, timeout, retry matrix, exception route, dead-letter atau replay procedure.
5. Jalankan fixture normal dan minimal dua failure case: duplicate trigger, timeout, 4xx/5xx, schema drift, unauthorized, or partial success.
6. Verifikasi execution output, business outcome, log/trace, dan side-effect count.
7. Dokumentasikan import/run/test, environment variables, limitation, rollback, dan owner.

## Output dan bukti yang harus terlihat

Submission harus memuat workflow/adapter/contract yang diminta, fixture, test result, execution evidence, error route, runbook, dan architecture note. Setiap side effect harus dapat dibuktikan idempotent, dry-run, atau berada di balik human approval.

## Self-check sebelum submit

- [ ] Workflow dapat diimport dan dijalankan pada local/mock mode.
- [ ] Input dan output setiap node atau service terdokumentasi.
- [ ] Correlation id dan idempotency strategy terlihat pada trace/ledger.
- [ ] Retry hanya untuk error yang retryable dan memiliki batas.
- [ ] Failed execution dapat diinvestigasi dan direplay secara aman.
- [ ] Tidak ada credential atau customer data nyata.
- [ ] Ada alert/metric/runbook bila scope menyentuh operasi.
- [ ] Trade-off tool choice, cost, security, dan ownership tertulis.

## Hubungan dengan part berikutnya

Pastikan workflow contract dapat digunakan ulang pada integrated system, deployment, monitoring, AI-on-automation, dan integration readiness. Perubahan partner/schema harus dibuat sebagai versioned adapter atau contract update.
