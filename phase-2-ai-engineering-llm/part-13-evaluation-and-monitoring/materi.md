# Evaluation and Monitoring

**Fase:** 2 — AI Engineering (LLM)  
**Section:** Deployment, Evaluation & Governance

> Diverifikasi: DeepEval documentation — sumber: https://deepeval.com/docs/introduction — tanggal cek: 2026-09-18
> Diverifikasi: LangSmith documentation — sumber: https://docs.smith.langchain.com/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan offline evaluation, online monitoring, dan human review;
- memilih metric untuk retrieval, groundedness, answer relevance, latency, cost, dan safety;
- membuat trace yang dapat dianalisis tanpa logging data sensitif;
- mendeteksi drift pada query, retrieval, model, dan policy;
- mendefinisikan release gate dan alert threshold.

## Konteks di PT Kirimin

Demo terlihat baik, tetapi Fajar melaporkan jawaban yang tidak membantu. Tim harus dapat membuktikan perubahan kualitas dari release ke release dan melihat kapan real traffic berbeda dari test set.

## Konsep kunci

### Offline evaluation

**Definisi teknis:** Offline evaluation menjalankan fixed cases dengan expected answer/evidence/behavior sebelum deployment. Ia repeatable tetapi dapat tertinggal dari traffic nyata.

**Penjelasan sederhana:** Ujian laboratorium penting, tetapi tidak menggantikan melihat bagaimana sistem bekerja di jalan.

### Online monitoring

**Definisi teknis:** Monitoring mengukur traffic, latency, errors, token cost, retrieval distribution, user feedback, escalation, and policy violations. Sampling dan redaction diperlukan.

**Penjelasan sederhana:** Pantau kondisi nyata tanpa merekam semua isi percakapan secara sembrono.

### LLM-as-judge

**Definisi teknis:** LLM judge memberi rubric-based assessment; ia perlu calibration, reference/human audit, consistency checks, dan tidak boleh menjadi satu-satunya safety signal.

**Penjelasan sederhana:** Penilai otomatis membantu menyaring banyak jawaban, tetapi tetap perlu pemeriksaan manusia.

## Evaluation matrix Kirimin

Case type: FAQ, ambiguity, no evidence, conflicting SOP, sensitive, injection, structured count, outage. Metric: retrieval recall, citation support, answer relevance, abstention correctness, p95 latency, cost, escalation rate.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| DeepEval | pin environment | offline evaluation |
| LangSmith | hosted current; record date/workspace | tracing/monitoring |

## Referensi resmi

- [DeepEval](https://deepeval.com/docs/introduction)
- [LangSmith observability](https://docs.smith.langchain.com/observability)
- [OpenAI evals guidance](https://platform.openai.com/docs/guides/evals)

## Lanjut ke praktik

Notebook menghitung simple rubric score dan alert decision dari trace sintetis.

## Posisi part dalam bootcamp

Part ini membuat kualitas AI terukur sebelum dan sesudah deployment. Anda akan menggabungkan offline evaluation, online monitoring, human feedback, traces, dan regression set. Evaluation adalah contract perubahan, bukan laporan akhir.

## Kapan konsep ini dipakai

Gunakan offline evaluation untuk membandingkan versi sebelum release. Gunakan online monitoring untuk drift, latency, cost, failure, dan feedback setelah release. Gunakan human review untuk dimensi yang belum dapat dinilai otomatis atau berisiko tinggi.

## Walkthrough terpandu: evaluation suite support assistant

1. Buat dataset 50 pertanyaan sintetis yang mencakup normal, ambiguous, out-of-scope, policy, and adversarial.
2. Tetapkan expected answer properties: grounded, citation present, correct escalation, no PII leakage, valid schema.
3. Jalankan baseline dan candidate dengan model/prompt/index version tercatat.
4. Hitung retrieval metrics, answer correctness, groundedness, citation accuracy, refusal quality, latency, cost, and invalid output rate.
5. Review sampel disagreement secara manual dan perbarui rubric, bukan hanya menaikkan threshold.
6. Buat dashboard online untuk request volume, error, fallback, feedback, drift, and stale evidence.
7. Tetapkan release gate dan alert threshold. Simpan regression cases dari incident nyata.

## Latihan terbimbing

- Buat evaluator rule-based dan LLM-as-judge dengan caveat.
- Hitung confusion matrix untuk escalation.
- Tambahkan slice per language, city, and question type.
- Simulasikan quality drift saat SOP berubah.
- Buat release report satu halaman.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjelaskan metric, dataset, threshold, evidence, limitation, dan tindakan ketika score turun.

## Jembatan ke assignment

Assignment harus berisi eval dataset, rubric, evaluator code, baseline/candidate report, monitoring schema/dashboard, release gate, dan feedback loop.
