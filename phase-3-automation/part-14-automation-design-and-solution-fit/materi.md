# Automation Design & Solution Fit

**Fase:** 3 — Automation  
**Section:** AI-Driven Automation & Solution Design

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- memilih low-code, custom code, integration platform, atau service berdasarkan fit;
- mengukur complexity, maintainability, volume, risk, dan team skill;
- merancang MVP dan evolution path;
- menghindari over-automation dan tool sprawl;
- membuat ADR dengan alternative dan exit criteria.

## Konteks di PT Kirimin

Stakeholder mengusulkan tiga platform berbeda untuk workflow yang sama. Anda harus memilih solusi yang dapat dirawat tim Kirimin, bukan yang paling banyak fitur.

## Konsep kunci

### Solution fit

**Definisi teknis:** Fit adalah kesesuaian capability, reliability, security, cost, integration, operability, and skills terhadap requirement.

**Penjelasan sederhana:** Sepatu yang paling mahal belum tentu cocok dengan kaki dan jalur yang ditempuh.

### MVP boundary

**Definisi teknis:** MVP membatasi scope untuk membuktikan risk/benefit paling penting, dengan non-goals dan migration path yang eksplisit.

**Penjelasan sederhana:** Uji satu jalur pengiriman dahulu, tetapi jangan berpura-pura sudah membangun seluruh jaringan.

### ADR

**Definisi teknis:** Architecture Decision Record mencatat context, decision, alternatives, consequences, assumptions, and review trigger.

**Penjelasan sederhana:** ADR adalah memori keputusan agar tim masa depan mengerti mengapa pilihan dibuat.

## Fit matrix Kirimin

Nilai tiap option dari 1–5 untuk time-to-value, integration, reliability, security, cost, maintainability, extensibility, dan exit cost. Bobot berasal dari stakeholder.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | low-code option |
| Docker | 29.6.2 | custom service packaging |

## Referensi resmi

- [n8n documentation](https://docs.n8n.io/)
- [Docker documentation](https://docs.docker.com/engine/)

## Lanjut ke praktik

Notebook membuat weighted fit matrix. Assignment meminta ADR dan MVP plan.

## Posisi part dalam bootcamp

Part ini membantu memilih solusi yang tepat setelah proses dipahami. Anda akan membandingkan n8n, custom service, scheduled job, existing platform, dan manual operation berdasarkan fit, risk, cost, and lifecycle.

## Kapan konsep ini dipakai

Gunakan solution-fit analysis ketika banyak tool dapat menyelesaikan problem yang sama. Jangan menyamakan prototype speed dengan long-term suitability. Pertimbangkan ownership dan exit cost sejak awal.

## Walkthrough terpandu: tiga opsi shipment alert

1. Tetapkan requirements: volume, latency, integrations, audit, approval, security, and budget.
2. Bandingkan n8n workflow, Python service, dan managed alert feature.
3. Nilai each option dengan weighted criteria dan confidence/evidence.
4. Identifikasi hidden cost: maintenance, vendor lock-in, credentials, testing, and incident support.
5. Pilih MVP dan target-state bila kebutuhan tumbuh.
6. Tulis ADR dengan alternatif rejected dan trigger untuk re-evaluation.
7. Validasi recommendation dengan stakeholder non-engineering.

## Latihan terbimbing

- Buat scorecard dari requirement nyata.
- Bedakan must-have dan nice-to-have.
- Hitung TCO tiga tahun secara kasar.
- Rancang exit strategy.
- Tulis architecture review questions.

## Checkpoint penguasaan

Anda siap lanjut jika solution choice dapat ditelusuri ke requirement, evidence, risk, cost, and lifecycle.

## Jembatan ke assignment

Assignment harus menghasilkan solution-fit matrix, ADR, TCO assumptions, risk register, MVP/target-state design, and re-evaluation triggers.
