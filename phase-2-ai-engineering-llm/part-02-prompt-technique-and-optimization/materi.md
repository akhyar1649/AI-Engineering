# Prompt Technique and Optimization

**Fase:** 2 — AI Engineering (LLM)  
**Section:** AI & LLM Foundations

> Diverifikasi: OpenAI API documentation — sumber: https://platform.openai.com/docs/quickstart — tanggal cek: 2026-09-18
> Diverifikasi: Gemini API documentation — sumber: https://ai.google.dev/gemini-api/docs — tanggal cek: 2026-09-18

## Tujuan belajar

- menyusun prompt dengan role, task, context, constraints, dan output schema;
- memilih zero-shot, few-shot, decomposition, atau self-check sesuai task;
- mengurangi ambiguity dan prompt injection risk;
- mengoptimalkan prompt memakai test set, bukan intuisi satu contoh;
- mendokumentasikan prompt version dan perubahan performa.

## Konteks di PT Kirimin

Jawaban assistant kadang terlalu panjang, menyarankan kebijakan yang tidak ada, dan tidak meminta klarifikasi. Fajar membutuhkan prompt yang menghasilkan jawaban ringkas berbasis evidence dengan format yang konsisten.

## Konsep kunci

### Prompt structure

**Definisi teknis:** Prompt adalah input terstruktur yang mengarahkan model melalui instruksi, context, examples, constraints, dan output format. Struktur memisahkan data tidak tepercaya dari instruksi sistem.

**Penjelasan sederhana:** Brief kerja yang lengkap mengurangi salah tafsir; “jawab pelanggan” terlalu kabur.

### Few-shot dan decomposition

**Definisi teknis:** Few-shot memberi examples input-output untuk membentuk pola; decomposition memecah task kompleks menjadi subtask yang dapat divalidasi.

**Penjelasan sederhana:** Anda memberi contoh jawaban yang baik dan membagi pekerjaan besar menjadi checklist kecil.

### Structured output

**Definisi teknis:** Structured output membatasi response ke schema yang dapat diparse, tetapi valid schema tidak menjamin truthfulness. Validasi domain tetap diperlukan.

**Penjelasan sederhana:** JSON yang rapi bisa tetap berisi informasi salah; format dan isi adalah dua pemeriksaan berbeda.

### Prompt injection

**Definisi teknis:** Prompt injection adalah input yang mencoba mengubah instruction hierarchy atau meminta model membocorkan context/tool. Defense mencakup trust boundary, least privilege, delimiters, validation, dan human approval.

**Penjelasan sederhana:** Pesan pelanggan adalah isi surat, bukan perintah kepada petugas keamanan gedung.

## Prompt contract Kirimin

Sistem prompt: peran dan policy. User content: pertanyaan yang tidak dipercaya. Retrieved context: evidence dengan citation id. Output: `answer`, `citations`, `confidence`, `needs_human`. Semua prompt disimpan dengan version.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| OpenAI Responses API | current official API | contoh structured output |
| Gemini API | current official API | provider comparison |

## Referensi resmi

- [OpenAI prompt engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Gemini prompting strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)

## Lanjut ke praktik

Notebook membandingkan prompt buruk dan prompt terstruktur dengan mock evaluator.

## Posisi part dalam bootcamp

Part ini mengubah tujuan bisnis dan output contract menjadi prompt yang dapat diuji. Prompt bukan mantra; ia adalah interface antara instruksi, context, examples, format, dan policy. Hasil part ini akan dipakai oleh RAG, agent, evaluation, dan automation.

## Kapan konsep ini dipakai

Gunakan prompt engineering ketika task sudah jelas tetapi kualitas, consistency, atau format output belum stabil. Jika masalah sebenarnya adalah evidence yang hilang, perbaiki retrieval atau data, bukan hanya memperpanjang prompt. Jika output harus selalu valid, tambahkan schema validation dan retry terkontrol.

## Walkthrough terpandu: klasifikasi tiket customer

1. Tetapkan label: status_order, policy_question, complaint, refund_request, dan human_review.
2. Tulis system instruction dengan role, scope, policy, dan larangan mengarang status order.
3. Susun input template yang memisahkan customer text dari instruction agar batas tidak ambigu.
4. Berikan output JSON dengan enum, rationale singkat, escalation flag, dan evidence field.
5. Buat few-shot examples yang mewakili kasus normal dan edge case, bukan hanya contoh mudah.
6. Uji prompt pada baseline set. Ukur label accuracy, invalid JSON rate, refusal quality, latency, dan token usage.
7. Ubah satu komponen pada satu eksperimen, simpan prompt_version, lalu bandingkan hasil agar optimasi dapat diatribusikan.

## Latihan terbimbing

- Buat prompt zero-shot dan few-shot untuk task yang sama.
- Tambahkan contoh prompt injection dan uji apakah model mengikuti data sebagai data.
- Buat parser yang menolak enum tidak valid.
- Bandingkan prompt panjang versus context terkurasi.
- Tulis stopping rule kapan prompt tidak lagi menjadi solusi utama.

## Checkpoint penguasaan

Anda siap lanjut jika setiap prompt memiliki contract, test set, version, failure handling, dan alasan perubahan yang dapat dibandingkan.

## Jembatan ke assignment

Assignment harus menyertakan prompt versions, eval cases, output schema, experiment table, dan notes trade-off quality versus token/cost.
