# Infrastructure as Code & Collaborative Engineering

**Fase:** 1 — Data Infrastructure  
**Section:** Reliability & Cloud Infrastructure

> Diverifikasi: Terraform AWS Provider v6.62.0 — sumber: https://registry.terraform.io/providers/-/aws/latest — tanggal cek: 2026-09-18
> Diverifikasi: Docker Engine v29.6.2 — sumber: https://docs.docker.com/engine/release-notes/29/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menjelaskan deklaratif versus imperatif pada Infrastructure as Code;
- memisahkan configuration, state, module, dan environment;
- membuat perubahan infra yang reviewable dan repeatable;
- merancang CI checks untuk lint, security, plan, dan test;
- bekerja dengan branch, pull request, code ownership, dan rollback.

## Konteks di PT Kirimin

Resource staging dan production mulai berbeda karena perubahan manual. Reza meminta semua perubahan infrastructure direview, memiliki state yang aman, dan dapat direkonstruksi tanpa mengandalkan ingatan satu engineer.

## Konsep kunci

### Declarative IaC

**Definisi teknis:** Declarative IaC mendeskripsikan desired state; tool menghitung perbedaan dan melakukan perubahan untuk mencapai state tersebut. State file memetakan resource konfigurasi ke resource aktual.

**Penjelasan sederhana:** Anda menyebutkan bentuk gudang yang diinginkan; tool menyusun langkah membangun atau memperbaikinya.

### State dan drift

**Definisi teknis:** Drift terjadi ketika actual infrastructure berbeda dari konfigurasi atau state. State harus dilindungi, dikunci saat update, dan tidak menyimpan secret secara sembarang.

**Penjelasan sederhana:** Denah mengatakan rak ada di posisi A, tetapi orang memindahkannya manual ke B. Pemeriksaan drift menemukan perbedaan itu.

### Collaborative engineering

**Definisi teknis:** Review, CI, ownership, small changes, and audit trail menurunkan risiko perubahan. Plan harus diperiksa sebelum apply.

**Penjelasan sederhana:** Perubahan besar pada gudang perlu second pair of eyes sebelum alat berat dinyalakan.

## Workflow yang disarankan

`format → validate → plan → review → apply → verify → record`. Gunakan module untuk pola berulang, variable untuk environment, output untuk contract, dan policy check untuk guardrail.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| Terraform AWS Provider | 6.62.0 | contoh provider IaC |
| Git | verifikasi runtime lokal | collaborative change |

## Referensi resmi

- [Terraform language documentation](https://developer.hashicorp.com/terraform/language)
- [Terraform AWS provider](https://registry.terraform.io/providers/-/aws/latest)
- [GitHub flow documentation](https://docs.github.com/en/get-started/using-github/github-flow)

## Lanjut ke praktik

Notebook memvalidasi desired resource model secara lokal tanpa apply cloud. Assignment meminta module skeleton, CI checklist, dan review workflow.

## Posisi part dalam bootcamp

Part ini memperkenalkan infrastructure as code dan cara bekerja dalam perubahan yang dapat direview. Anda akan mengubah target cloud dari diagram menjadi deklarasi, plan, review, apply, dan destroy yang terkendali. Ini mempersiapkan deployment capstone dan final project.

## Kapan konsep ini dipakai

Gunakan IaC ketika environment harus konsisten, dapat direview, dan dapat dibuat ulang. Gunakan manual console hanya untuk eksplorasi atau recovery yang terdokumentasi. Jangan menyimpan state atau secret sensitif ke repository.

## Walkthrough terpandu: environment staging Kirimin

1. Definisikan input variables untuk environment, region, instance size, storage retention, dan tags.
2. Buat network, storage bucket, database, compute, identity, dan observability resource dengan naming convention.
3. Jalankan format, validate, dan plan. Baca diff untuk menemukan resource replacement atau permission terlalu luas.
4. Gunakan remote/state locking sesuai platform; untuk latihan lokal, dokumentasikan keterbatasan local state.
5. Review perubahan dengan pull request: tujuan, blast radius, cost delta, migration, rollback, dan evidence test.
6. Apply hanya setelah plan disetujui, lalu output endpoint dan resource identifiers tanpa secret.
7. Uji destroy atau rollback pada environment disposable dan catat resource yang sengaja dipertahankan.

## Latihan terbimbing

- Buat module untuk storage dan database.
- Tambahkan tagging owner, environment, data_classification, dan retention.
- Simulasikan perubahan instance size dan baca plan.
- Tambahkan policy check untuk public storage.
- Rancang branch/PR flow untuk perubahan aplikasi dan infra.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjelaskan lifecycle resource, membaca plan, menjaga secret/state, dan menunjukkan review yang menghubungkan diff infra dengan risiko bisnis.

## Jembatan ke assignment

Assignment harus berisi IaC skeleton, variables, README runbook, plan output yang disanitasi, policy/security checks, cost delta, dan prosedur apply/rollback/destroy yang aman.
