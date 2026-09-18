# Assignment — AI on Automation

## Konteks kasus

Klasifikasikan customer ticket dan arahkan ke workflow yang tepat.

## Tugas dan requirement

1. Pilih satu AI task dan jelaskan mengapa rule biasa tidak cukup.
2. Buat structured output, confidence gate, human route, dan fallback.
3. Integrasikan mock AI node ke workflow n8n.
4. Tambahkan privacy/redaction dan audit event.
5. Hitung cost/latency serta quality threshold.

## Kriteria penilaian

- 25% problem fit.
- 25% output/policy boundary.
- 20% reliability/fallback.
- 20% privacy/audit.
- 10% cost/quality.

## Format pengumpulan

```text
submission/
├── workflow.json
├── ai_contract.md
├── policy.md
├── eval-cases.jsonl
└── notes.md
```

## Estimasi waktu

3–4 jam.

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
