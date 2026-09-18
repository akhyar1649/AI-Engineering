# AI Risk and Governance

**Fase:** 2 — AI Engineering (LLM)  
**Section:** Deployment, Evaluation & Governance

> Diverifikasi: OpenAI safety and usage policies — sumber: https://openai.com/policies/usage-policies/ — tanggal cek: 2026-09-18
> Diverifikasi: NIST AI Risk Management Framework — sumber: https://www.nist.gov/itl/ai-risk-management-framework — tanggal cek: 2026-09-18

## Tujuan belajar

- membuat AI risk register berdasarkan use case dan impact;
- menerapkan privacy, security, human oversight, dan access control;
- membedakan model risk, data risk, product risk, dan operational risk;
- menyusun incident response dan documentation artifacts;
- menentukan batas penggunaan assistant support.

## Konteks di PT Kirimin

Assistant dapat memproses data order dan customer ticket. Fajar ingin manfaat produktivitas, tetapi Reza melarang AI mengambil keputusan refund atau membocorkan data antar pelanggan.

## Konsep kunci

### Risk-based governance

**Definisi teknis:** AI governance mengatur lifecycle, accountability, controls, documentation, monitoring, and remediation berdasarkan risk dan impact.

**Penjelasan sederhana:** Tidak semua pertanyaan membutuhkan pagar yang sama; sistem yang menyentuh uang memerlukan kontrol lebih ketat daripada FAQ umum.

### Privacy dan data minimization

**Definisi teknis:** Data minimization mengumpulkan dan mengirim data minimum untuk tujuan yang sah. PII handling mencakup discovery, masking, access, retention, deletion, dan processor boundary.

**Penjelasan sederhana:** Assistant tidak perlu mengetahui seluruh identitas pelanggan untuk menjawab jam operasional.

### Human oversight

**Definisi teknis:** Human-in-the-loop menetapkan kapan manusia menyetujui, meninjau, atau dapat membatalkan output/action model. Handoff harus usable, bukan sekadar label.

**Penjelasan sederhana:** Jika keputusan berdampak besar, petugas manusia tetap memegang tombol final.

### Documentation

**Definisi teknis:** Model card, data card, system card, prompt/version log, risk assessment, evaluation report, and incident log membantu auditability.

**Penjelasan sederhana:** Tim masa depan perlu tahu apa yang dibuat, dari data apa, dengan batasan apa, dan kapan gagal.

## Risk boundaries Kirimin

Allowed: FAQ SOP dengan citation. Review required: account-specific status, refund, complaint escalation, PII. Prohibited: autonomous payment/refund, exposure of another customer, bypassing access control.

## Tools & versi

| Framework | Status | Peran |
|---|---:|---|
| NIST AI RMF | current framework | risk vocabulary |
| OpenAI policies | current policy page | provider/safety reference |

## Referensi resmi

- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)
- [OpenAI usage policies](https://openai.com/policies/usage-policies/)
- [Google AI safety](https://ai.google/responsibility/safety/)

## Lanjut ke praktik

Notebook membuat risk scoring sederhana dan policy route.

## Posisi part dalam bootcamp

Part ini menghubungkan AI system dengan privacy, security, safety, fairness, accountability, and compliance. Anda akan memakai governance artifact dari Fase 1 untuk mengendalikan model, data, prompt, tool, dan human action.

## Kapan konsep ini dipakai

Gunakan AI risk assessment sebelum pilot, saat scope/model/data berubah, dan setelah incident. Bedakan risk pada confidentiality, integrity, availability, harmful advice, bias, automation overreach, and vendor dependency.

## Walkthrough terpandu: risk review customer support copilot

1. Petakan data input, evidence, output, tool, user role, and side effect.
2. Identifikasi threat: prompt injection, PII leakage, stale policy, hallucinated refund promise, insecure tool, and over-trust.
3. Nilai likelihood, impact, detectability, and residual risk.
4. Pilih controls: access filter, redaction, grounding, schema validation, human approval, audit log, retention, and kill switch.
5. Uji controls dengan red-team cases dan normal cases agar false positive terukur.
6. Tetapkan owner, evidence, review cadence, and exception process.
7. Tulis user-facing limitation and escalation language.

## Latihan terbimbing

- Buat threat model sederhana.
- Tambahkan PII redaction test.
- Rancang permission matrix untuk agent tools.
- Buat AI incident severity matrix.
- Tulis model/system card yang jujur.

## Checkpoint penguasaan

Anda siap lanjut jika setiap risiko memiliki control, owner, evidence, residual risk, dan tindakan ketika control gagal.

## Jembatan ke assignment

Assignment harus menghasilkan risk register, threat model, control test, governance checklist, model/system card, incident flow, dan rollout recommendation.
