# Troubleshooting Reliability & Prioritization

**Fase:** 1 — Data Infrastructure  
**Section:** Reliability & Cloud Infrastructure

> Diverifikasi: Apache Airflow v3.3.2 — sumber: https://airflow.apache.org/docs/apache-airflow/3.3.2/ — tanggal cek: 2026-09-18
> Diverifikasi: Grafana release documentation — sumber: https://grafana.com/docs/grafana/latest/whatsnew/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan symptom, cause, dan contributing factor;
- membaca log, metric, dan trace secara berurutan;
- memprioritaskan incident memakai impact dan urgency;
- merancang retry, timeout, circuit breaker, dan dead-letter path;
- menulis postmortem tanpa blame.

## Konteks di PT Kirimin

Pipeline pagi terlambat tiga kali minggu ini. Sari hanya melihat dashboard kosong, sementara Dinda membutuhkan diagnosis yang dapat dibuktikan dan rencana perbaikan yang tidak sekadar menambah retry.

## Konsep kunci

### Reliability dan SLO

**Definisi teknis:** Reliability adalah probabilitas sistem menjalankan fungsi sesuai kontrak selama periode tertentu. SLI mengukur perilaku, SLO menetapkan target, dan error budget memberi batas risiko perubahan.

**Penjelasan sederhana:** Bukan cukup mengatakan “sistem jarang gagal”; kita menentukan berapa kali laporan boleh terlambat dan kapan tim harus berhenti menambah fitur.

### Debugging berlapis

**Definisi teknis:** Troubleshooting bergerak dari scope/impact ke timeline, dependency, recent change, logs, metrics, dan controlled reproduction. Hypothesis harus dapat dibuktikan atau difalsifikasi.

**Penjelasan sederhana:** Dokter menanyakan gejala, kapan mulai, dan memeriksa tanda vital sebelum memberi obat. Engineer juga perlu urutan pemeriksaan.

### Resilience pattern

**Definisi teknis:** Timeout membatasi blocking; retry menangani transient failure dengan backoff/jitter; circuit breaker menghentikan call ke dependency yang gagal; dead-letter menyimpan message yang tidak dapat diproses.

**Penjelasan sederhana:** Menggedor pintu yang terkunci terus-menerus tidak membantu. Beri waktu, coba terbatas, lalu simpan paket untuk pemeriksaan.

## Prioritization matrix

Gunakan impact terhadap order/customer, urgency terhadap SLA, blast radius, dan confidence. P1 melibatkan keputusan mitigasi segera; P3 dapat masuk backlog dengan owner dan due date.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| Apache Airflow | 3.3.2 | task state dan retry |
| Grafana | lihat release notes resmi saat deployment | dashboard observability |

## Referensi resmi

- [Airflow monitoring and alerting](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/logging-monitoring/index.html)
- [Grafana documentation](https://grafana.com/docs/grafana/latest/)

## Lanjut ke praktik

Notebook mengklasifikasikan incident dari dataset log sederhana. Assignment meminta incident runbook dan postmortem.

## Posisi part dalam bootcamp

Part ini mengajarkan cara bergerak dari gejala ke akar masalah tanpa menebak. Anda akan memakai observability pipeline, quality evidence, dan prioritas bisnis untuk memilih perbaikan. Kemampuan ini menjadi dasar runbook dan incident response pada capstone.

## Kapan konsep ini dipakai

Gunakan troubleshooting ketika freshness turun, jumlah baris berubah, dashboard berbeda, atau task gagal. Gunakan prioritization ketika banyak alert masuk bersamaan. Bedakan incident data, incident infrastructure, dan incident consumer.

## Walkthrough terpandu: backlog melonjak dua kali lipat

1. Nyatakan gejala dan waktu mulai, lalu bekukan perubahan yang tidak perlu.
2. Cek freshness, input count, duplicate rate, quarantine count, dan run metadata dibanding baseline tujuh hari.
3. Trace lineage dari dashboard ke mart, curated, raw, lalu source. Cari titik pertama angka berubah.
4. Hipotesiskan kemungkinan: duplicate ingestion, filter tanggal berubah, late event, atau dashboard query menggandakan join.
5. Uji satu hipotesis dengan query kecil dan evidence yang dapat diulang. Jangan memperbaiki production data sebelum raw dan run ID dicatat.
6. Klasifikasikan severity berdasarkan dampak dan durasi. Tetapkan mitigation, owner, ETA, serta komunikasi stakeholder.
7. Setelah pulih, lakukan post-incident review: root cause, detection gap, corrective action, dan prevention test.

## Latihan terbimbing

- Analisis kasus task retry yang menulis partition dua kali.
- Buat decision tree untuk missing source versus bad source.
- Hitung prioritas dengan impact x urgency x confidence.
- Tulis runbook satu halaman untuk quality gate gagal.
- Tambahkan regression check agar insiden serupa terdeteksi lebih awal.

## Checkpoint penguasaan

Anda siap lanjut jika dapat membedakan symptom, contributing factor, dan root cause, memilih evidence yang cukup, serta menghasilkan tindakan pencegahan yang dapat diuji.

## Jembatan ke assignment

Assignment harus berisi tiga incident scenario, investigation timeline, evidence query/log, severity rationale, runbook, postmortem, dan backlog prevention. Semua rekomendasi harus menunjuk ke owner dan acceptance criteria.
