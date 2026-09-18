# Capstone 1 — Kirimin Data Operations Platform

## Konteks bisnis

PT Kirimin Digital Nusantara memproses puluhan ribu order per hari, tetapi Dinda belum dapat menjamin bahwa dashboard Ops memakai data yang lengkap dan konsisten. Sari membutuhkan backlog shipment dan delivery success rate sebelum briefing pagi. Reza meminta platform kecil yang dapat dijalankan lokal atau di cloud dengan batasan biaya yang jelas.

## Tantangan

Bangun pipeline data end-to-end yang menerima order dan shipment sintetis, menyimpan raw, melakukan cleaning dan quality checks, menghasilkan curated/serving dataset, menyediakan API summary, dan memiliki observability serta deployment story.

## Deliverable wajib

1. **Repository code:** README, struktur project, generator data sintetis, pipeline, quality checks, tests, dan cara run.
2. **Aplikasi/pipeline live deploy:** URL/demo atau bukti deployment yang dapat diulang mentor; jika credential cloud tidak tersedia, gunakan container lokal dengan instruksi reproduksi lengkap.
3. **Laporan dan presentasi:** konteks bisnis, arsitektur, grain/schema, quality results, SLO, cost estimate, trade-off, demo flow, dan backlog perbaikan.

## Scope minimum

- minimal 10.000 order sintetis dan 20.000 shipment event atau generator yang dapat menghasilkan skala tersebut;
- data kotor: missing, duplicate, city alias, timestamp out-of-order, outlier, schema variation;
- raw, curated, quarantine, dan serving output;
- minimal 10 quality rules dengan severity dan owner;
- pipeline idempotent berdasarkan partition/run date;
- API `/health` dan endpoint summary;
- dashboard/specification minimal tiga KPI;
- runbook incident dan capacity/cost model.

## Batasan

- tidak boleh memakai data pelanggan nyata;
- secret tidak boleh masuk repository;
- setiap keputusan teknologi harus menyebut alasan, risiko, dan alternatif;
- tool eksternal dapat diganti mock/local adapter selama contract dan deployment story jelas.

## Timeline yang disarankan

| Hari | Fokus | Output |
|---|---|---|
| 1 | framing, schema, generator | ADR dan dataset generator |
| 2 | ingestion, cleaning, quality | raw/curated/quarantine |
| 3 | serving, API, KPI | endpoint dan metric contract |
| 4 | deployment, observability, cost | runbook dan demo |
| 5 | testing, report, presentation | final submission |

## Prasyarat dan hubungan dengan Fase 1

Capstone ini dikerjakan setelah Part 1–16. Peserta harus sudah dapat menjelaskan grain dan key, membuat cleaning yang idempotent, menulis quality rule, merancang serving model, membaca failure evidence, dan membuat cost/capacity assumption. Setiap deliverable harus menunjuk part yang menjadi sumber keputusan: query dari Part 1/3, transform dari Part 2/4, pipeline dari Part 5, metric dari Part 7, governance dari Part 8/9, reliability dari Part 10, deployment dari Part 11–13, NoSQL bila dipilih dari Part 14–15, dan capacity dari Part 16.

## Tools yang digunakan

- Python 3.14.7, pandas 3.0.3, dan Jupyter untuk generator, pipeline, quality report, dan tests.
- PostgreSQL 18.6 atau SQLite fallback untuk source/serving query.
- Docker Engine 29.6.2 untuk API, database, dan pipeline yang reproducible.
- FastAPI sesuai version log untuk endpoint health/summary.
- Airflow 3.3.2 bila DAG dijalankan sungguhan; simulasi DAG diperbolehkan jika contract, retry, dan evidence lengkap.
- Spark 4.2.0 atau equivalent hanya bila kebutuhan distributed processing dibuktikan.
- MongoDB 8.3 hanya bila document-store menjadi bagian arsitektur.
- Git untuk review dan history.

Semua harga, provider, dan version yang berubah harus diverifikasi ulang dan dicatat. Credential cloud boleh diganti local/self-hosted deployment, tetapi peserta wajib menunjukkan perbedaan risiko dan langkah reproduksi. Tidak boleh ada data pelanggan nyata.

## Rencana pengerjaan dan milestone wajib

### Milestone 1 — Frame dan contract

Buat problem statement, stakeholder map, non-goals, data dictionary, grain, schema, quality rule, metric contract, ADR, dan generator seed. Exit criteria: mentor dapat membuat ulang dataset dan memahami expected output.

### Milestone 2 — Raw sampai curated

Implementasikan ingestion, raw immutable, profile, cleaning, deduplication, quarantine, dan quality gate. Exit criteria: ada test untuk missing, duplicate, alias, invalid timestamp, outlier, dan rerun partition.

### Milestone 3 — Serving dan consumer

Bangun serving table/API/dashboard specification dengan /health, summary endpoint, freshness, dan tiga KPI. Exit criteria: angka API dapat direkonsiliasi dengan curated sample.

### Milestone 4 — Deploy dan operate

Jalankan container/local deployment, tambahkan log/metric, SLO, retry, alert, cost model, backup/restore, incident runbook, dan rollback. Exit criteria: orang lain dapat menjalankan demo dan mengikuti recovery procedure.

### Milestone 5 — Evidence dan komunikasi

Jalankan clean-room reproduction, test suite, failure demo, dan capacity scenario. Lengkapi report serta presentation. Exit criteria: demo memperlihatkan normal path dan failure path, bukan hanya source code.

## Definition of done

- [ ] Dataset sintetis dapat dibuat ulang dengan seed dan skala minimum.
- [ ] Raw, curated, quarantine, serving, quality report, dan lineage tersedia.
- [ ] Minimal 10 quality rule memiliki severity, owner, observed result, dan action.
- [ ] Pipeline idempotent untuk partition/run date dan backfill terdokumentasi.
- [ ] API health/summary, tiga KPI, freshness, dan rekonsiliasi tersedia.
- [ ] Local atau cloud deployment dapat dijalankan ulang tanpa secret di repository.
- [ ] Test normal/failure, runbook, cost/capacity, backup/restore, dan rollback tersedia.
- [ ] Report dan presentasi menjelaskan trade-off serta gap yang masih tersisa.
