# Monitoring & Observability for Automation

**Fase:** 3 — Automation  
**Section:** System Integration & Deployment

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18
> Diverifikasi: Grafana documentation — sumber: https://grafana.com/docs/grafana/latest/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan logs, metrics, traces, dan audit events;
- mendefinisikan SLI/SLO untuk workflow;
- membuat correlation id lintas system;
- merancang alert yang actionable dan low-noise;
- melindungi observability data dari PII/secret.

## Konteks di PT Kirimin

Workflow tampak “success” tetapi customer tidak menerima notifikasi. Sari perlu melihat setiap boundary: event diterima, ledger committed, provider accepted, dan delivery confirmed.

## Konsep kunci

### Three pillars

**Definisi teknis:** Logs memberi event detail, metrics memberi aggregate time series, traces menghubungkan span lintas service. Audit log mencatat actor/action/target untuk accountability.

**Penjelasan sederhana:** Log adalah catatan kejadian, metric adalah meteran, trace adalah jejak satu paket, audit adalah buku siapa melakukan apa.

### SLI/SLO automation

**Definisi teknis:** SLI dapat berupa execution success rate, event-to-action latency, DLQ age, duplicate side effect rate, and freshness. SLO menetapkan target dan alert threshold.

**Penjelasan sederhana:** Ukur apakah workflow selesai, berapa lama, dan apakah ia mengulang tindakan.

### Alert design

**Definisi teknis:** Alert harus memiliki symptom, impact, threshold, owner, runbook link, dedup/grouping, dan severity. Alert untuk setiap error kecil menciptakan noise.

**Penjelasan sederhana:** Alarm harus berbunyi ketika seseorang perlu bertindak, bukan setiap kali ada paket terlambat satu menit.

## Dashboard minimum

Execution success, p95 duration, trigger volume, retry rate, DLQ count/age, duplicate prevented, provider error rate, and last successful run.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | execution data |
| Grafana | release verified at deployment | dashboards/alerts |

## Referensi resmi

- [n8n executions](https://docs.n8n.io/workflows/executions/)
- [Grafana dashboards](https://grafana.com/docs/grafana/latest/dashboards/)
- [Grafana alerting](https://grafana.com/docs/grafana/latest/alerting/)

## Lanjut ke praktik

Notebook menghitung SLI dari execution sample dan memilih alert.

## Posisi part dalam bootcamp

Part ini membuat workflow dapat diamati setelah deployment. Anda akan menghubungkan execution log, business outcome, quality, cost, and alerting agar operator tahu bukan hanya bahwa workflow gagal, tetapi dampaknya.

## Kapan konsep ini dipakai

Gunakan observability ketika workflow memiliki dependency, SLA, side effect, atau volume yang membuat inspeksi manual tidak cukup. Log, metric, and trace harus memiliki correlation_id dan retention yang sesuai.

## Walkthrough terpandu: monitoring notification workflow

1. Definisikan technical metrics: execution success, duration, retry, timeout, queue depth, and provider error.
2. Definisikan business metrics: events processed, notifications delivered, duplicate prevented, exception rate, and time to resolve.
3. Tambahkan structured log per node dengan redaction.
4. Buat dashboard dan alert dengan threshold serta owner.
5. Hubungkan alert ke runbook dan severity; hindari alert yang tidak memicu tindakan.
6. Uji missing telemetry, stale dashboard, and alert delivery failure.
7. Review data retention, cardinality, and cost.

## Latihan terbimbing

- Buat event schema for execution.
- Rancang four golden signals plus business KPI.
- Simulasikan retry storm.
- Buat alert fatigue review.
- Tulis query investigasi dengan correlation_id.

## Checkpoint penguasaan

Anda siap lanjut jika operator dapat menemukan execution, dampak bisnis, root cause candidate, dan langkah pemulihan dari telemetry.

## Jembatan ke assignment

Assignment harus berisi instrumentation schema, dashboard/metric spec, alert rules, runbooks, sample traces, and privacy/retention note.
