# Fine-Tuning Model

**Fase:** 2 — AI Engineering (LLM)  
**Section:** Deployment, Evaluation & Governance

> Diverifikasi: Hugging Face Transformers v5.17.0 — sumber: https://huggingface.co/docs/transformers/main/ — tanggal cek: 2026-09-18
> Diverifikasi: Gemini model documentation — sumber: https://ai.google.dev/gemini-api/docs/models — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan prompt, retrieval, fine-tuning, dan pretraining;
- menyiapkan dataset instruction yang konsisten dan bebas data sensitif;
- menjelaskan supervised fine-tuning, adapters, validation, dan data leakage;
- menentukan kapan fine-tuning tidak diperlukan;
- merancang experiment tracking dan rollback model.

## Konteks di PT Kirimin

Fajar ingin gaya jawaban konsisten dan klasifikasi intent lebih akurat. SOP berubah sering, sehingga peserta harus menilai apakah masalah diselesaikan dengan prompt/RAG atau benar-benar membutuhkan parameter update.

## Konsep kunci

### Fine-tuning versus RAG

**Definisi teknis:** Fine-tuning mengubah parameter/adapters model berdasarkan dataset; RAG memasukkan knowledge saat inference. Fine-tuning cocok untuk behavior/style/task pattern, bukan sumber fakta yang sering berubah.

**Penjelasan sederhana:** Fine-tuning melatih cara petugas bekerja; RAG memberi manual terbaru di meja kerja.

### Dataset quality

**Definisi teknis:** Dataset harus memiliki coverage, label consistency, privacy review, train/validation/test split, hard cases, dan deduplication. Leakage membuat hasil evaluasi terlalu optimistis.

**Penjelasan sederhana:** Ujian tidak valid jika soal latihan muncul persis di ujian akhir.

### Adapter dan rollback

**Definisi teknis:** Parameter-efficient fine-tuning mengubah sebagian kecil parameter/adapters sehingga lebih murah. Registry dan versioned evaluation memungkinkan promotion/rollback.

**Penjelasan sederhana:** Anda mengganti modul perilaku, bukan membangun ulang seluruh mesin.

## Decision gate

Sebelum fine-tune: baseline prompt/RAG, error taxonomy, expected gain, dataset rights, cost, latency, and rollback. Jika knowledge freshness adalah masalah utama, perbaiki retrieval/lifecycle lebih dahulu.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| Hugging Face Transformers | 5.17.0 | training/inference examples |
| Gemini API | model versioned | provider fine-tuning option; cek availability |

## Referensi resmi

- [Transformers documentation](https://huggingface.co/docs/transformers/main/)
- [Gemini tuning docs](https://ai.google.dev/gemini-api/docs/model-tuning)
- [Hugging Face datasets](https://huggingface.co/docs/datasets/)

## Lanjut ke praktik

Notebook membuat dataset split dan baseline accuracy; tidak menjalankan training GPU berbayar.

## Posisi part dalam bootcamp

Part ini membandingkan fine-tuning dengan prompt, RAG, dan structured tools. Anda akan belajar bahwa fine-tuning mengubah behavior atau style model, bukan cara yang tepat untuk memasukkan knowledge yang sering berubah.

## Kapan konsep ini dipakai

Pertimbangkan fine-tuning ketika task, format, style, atau classification behavior stabil dan dataset berlabel cukup. Pilih RAG untuk knowledge yang berubah, tool untuk data transactional, dan prompt untuk perubahan kecil. Mulai dari baseline dan hitung cost/maintenance sebelum training.

## Walkthrough terpandu: classification tiket

1. Tetapkan label taxonomy dan contoh ambiguous. Hindari label yang tidak dapat dibedakan manusia.
2. Pisahkan train, validation, dan held-out test berdasarkan waktu atau entity agar tidak leakage.
3. Buat baseline prompt/model sederhana.
4. Bersihkan data, dokumentasikan annotation guideline, dan ukur inter-annotator disagreement.
5. Jalankan eksperimen kecil dengan seed/config tercatat. Simpan dataset_version dan model_version.
6. Evaluasi accuracy per class, confusion matrix, calibration, latency, cost, dan regression pada out-of-domain cases.
7. Putuskan fine-tune, prompt, atau reject berdasarkan threshold dan operating model.

## Latihan terbimbing

- Buat data card dan annotation guide.
- Deteksi duplicate/leakage antar split.
- Bandingkan baseline dengan fine-tune atau mock training.
- Buat rollback ke model baseline.
- Tulis risk jika label historis mengandung bias.

## Checkpoint penguasaan

Anda siap lanjut jika dapat membela alasan fine-tuning, menjaga data split, dan membandingkan gain quality dengan biaya serving serta maintenance.

## Jembatan ke assignment

Assignment harus menghasilkan dataset card, training/evaluation script atau reproducible mock, model comparison, error analysis, model card, dan rollback plan.
