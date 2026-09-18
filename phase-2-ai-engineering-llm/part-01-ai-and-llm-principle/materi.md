# AI and LLM Principle

**Fase:** 2 — AI Engineering (LLM)  
**Section:** AI & LLM Foundations

> Diverifikasi: OpenAI Python SDK v3.15.0 — sumber: https://github.com/openai/openai-python/releases — tanggal cek: 2026-09-18
> Diverifikasi: Gemini model documentation — sumber: https://ai.google.dev/gemini-api/docs/models — tanggal cek: 2026-09-18

## Tujuan belajar

- menjelaskan token, embedding, transformer, context window, inference, dan temperature;
- membedakan pretraining, instruction tuning, fine-tuning, dan retrieval;
- memilih model berdasarkan quality, latency, cost, context, dan risk;
- mengenali hallucination dan batas pengetahuan model;
- membuat baseline model call yang memiliki input/output contract.

## Konteks di PT Kirimin

Fajar tidak membutuhkan “AI yang terdengar pintar”; ia membutuhkan jawaban SOP yang benar, konsisten, dan dapat diarahkan ke agent manusia jika evidence tidak cukup. Pemahaman prinsip membantu tim memilih solusi yang proporsional.

## Konsep kunci

### LLM dan token

**Definisi teknis:** Large Language Model memodelkan distribusi token bersyarat untuk menghasilkan sequence. Token adalah unit subword/karakter yang memengaruhi context usage dan biaya.

**Penjelasan sederhana:** Model tidak membaca kalimat seperti manusia; ia memproses potongan teks dan memperkirakan potongan berikutnya.

### Transformer dan attention

**Definisi teknis:** Transformer menggunakan attention untuk memproses hubungan antar token secara paralel dalam context. Attention bukan bukti bahwa model memahami dunia secara grounded.

**Penjelasan sederhana:** Model menimbang bagian pesan mana yang paling relevan ketika memilih kata berikutnya, tetapi tetap bisa membuat jawaban meyakinkan yang salah.

### Embedding dan retrieval

**Definisi teknis:** Embedding memetakan input ke vector space sehingga kemiripan semantik dapat dihitung. Retrieval memasukkan context eksternal saat inference tanpa mengubah parameter model.

**Penjelasan sederhana:** Embedding seperti koordinat makna; dokumen yang topiknya mirip diletakkan berdekatan dan dapat diambil saat menjawab.

### Sampling dan determinisme

**Definisi teknis:** Temperature/top-p mengubah distribusi sampling. Seed atau temperature rendah dapat membantu repeatability, tetapi tidak menjamin determinisme lintas backend/model update.

**Penjelasan sederhana:** Dengan pilihan hampir tunggal, model lebih konsisten; dengan pilihan lebar, model lebih bervariasi.

## Model selection Kirimin

Mulai dari model kecil/cepat untuk routing dan FAQ, model lebih kuat untuk kasus ambigu, dan retrieval sebelum fine-tuning bila masalahnya knowledge freshness. Simpan model identifier/snapshot dan prompt version.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| OpenAI Python SDK | 3.15.0 | API example |
| Gemini API | gemini-3.6-flash stable | provider example |
| Python | 3.14.7 | notebook |

## Referensi resmi

- [OpenAI API quickstart](https://platform.openai.com/docs/quickstart)
- [Gemini models](https://ai.google.dev/gemini-api/docs/models)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/main/)

## Lanjut ke praktik

Notebook memakai mock completion untuk menghitung token dan membandingkan policy model tanpa mengirim data ke provider.

## Posisi part dalam bootcamp

Part ini menjadi pintu masuk Fase 2. Anda membawa data contract dan quality mindset dari Fase 1 ke sistem AI yang probabilistic. Tujuan akhirnya bukan membuat chatbot yang terlihat pintar, tetapi memahami kapan LLM cocok, output seperti apa yang aman dikonsumsi, dan bagaimana mengukur keberhasilannya.

## Kapan konsep ini dipakai

Gunakan LLM untuk language transformation, classification, extraction, summarization, dan conversational reasoning ketika variasi bahasa terlalu besar untuk rule biasa. Jangan memakai LLM sebagai sumber kebenaran untuk angka operasional tanpa evidence. Pertimbangkan deterministic code, SQL, atau human review jika kesalahan memiliki dampak tinggi.

## Walkthrough terpandu: memilih assistant FAQ Kirimin

1. Definisikan task: menjawab pertanyaan status kebijakan pengiriman dan mengarahkan kasus yang memerlukan data order.
2. Pisahkan knowledge statis, data terstruktur, dan tindakan side effect. Ketiganya membutuhkan tool atau kontrol berbeda.
3. Tulis baseline question set dengan expected behavior, termasuk pertanyaan di luar cakupan.
4. Bandingkan kandidat model pada quality, context, latency, cost, privacy, availability, dan observability.
5. Buat output contract: answer, evidence, confidence signal, escalation, model_id, prompt_version, dan token usage.
6. Uji prompt yang sama pada pertanyaan ambigu, adversarial, dan multilingual. Catat failure mode.
7. Tentukan human-in-the-loop untuk refund, perubahan alamat, atau keputusan yang berdampak pada customer.

## Latihan terbimbing

- Klasifikasikan sepuluh use case menjadi LLM, rule, SQL, atau human.
- Hitung token secara kasar dari prompt dan context.
- Bedakan hallucination, incomplete context, dan wrong business rule.
- Buat model selection matrix berbobot.
- Tulis lima pertanyaan yang harus dijawab “saya tidak memiliki evidence”.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjelaskan batas kemampuan model, membuat output contract yang dapat diuji, dan memilih deterministic fallback untuk risiko yang tepat.

## Jembatan ke assignment

Assignment harus menghasilkan model-selection memo, baseline cases, contract, dan risk notes. Setiap klaim model/provider yang berubah harus ditautkan ke version log atau diverifikasi saat implementasi.
