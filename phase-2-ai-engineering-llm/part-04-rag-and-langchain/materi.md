# RAG and LangChain

**Fase:** 2 — AI Engineering (LLM)  
**Section:** RAG & AI Agent Development

> Diverifikasi: LangChain Python v1.x — sumber: https://docs.langchain.com/oss/python/releases/langchain-v1 — tanggal cek: 2026-09-18
> Diverifikasi: OpenAI Python SDK v3.15.0 — sumber: https://github.com/openai/openai-python/releases — tanggal cek: 2026-09-18

## Tujuan belajar

- menjelaskan alur load, split, embed, retrieve, generate, dan cite;
- menyusun chain yang memiliki input/output contract;
- menghubungkan retriever dengan prompt dan model provider;
- menyimpan citation dan retrieval trace;
- membedakan framework convenience dari logic bisnis yang harus Anda kuasai.

## Konteks di PT Kirimin

Assistant Fajar perlu menjawab dari SOP yang dapat berubah. RAG dipilih agar knowledge dapat di-update tanpa melatih ulang model, dan LangChain menjadi contoh orkestrasi komponen.

## Konsep kunci

### RAG pipeline

**Definisi teknis:** Retrieval-Augmented Generation mengambil context relevan dari knowledge source lalu menyertakannya dalam model input sebelum generation. Kualitas RAG terurai menjadi retrieval quality, context construction, generation faithfulness, dan citation correctness.

**Penjelasan sederhana:** Sebelum menjawab, assistant membuka manual yang relevan. Jika manual yang dibuka salah, jawaban yang fasih tetap salah.

### Retriever dan chain

**Definisi teknis:** Retriever menerima query dan mengembalikan documents; chain menghubungkan retrieval, prompt, model, parser, dan metadata. Setiap boundary sebaiknya dapat diuji terpisah.

**Penjelasan sederhana:** Retriever adalah petugas arsip; chain adalah alur kerja dari pertanyaan sampai jawaban.

### Citation dan grounding

**Definisi teknis:** Citation menghubungkan claim ke source span/document id. Grounding mengukur apakah jawaban didukung context, bukan sekadar format citation ada.

**Penjelasan sederhana:** Menaruh nomor referensi tanpa membuka buku yang benar tidak membuat klaim menjadi benar.

## LangChain guidance

Gunakan abstraction untuk composition dan tracing, tetapi dokumentasikan retriever, prompt, parser, retry, dan error policy secara eksplisit. Pin package family yang kompatibel pada setiap notebook.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| LangChain | 1.x | chain/orchestration |
| OpenAI Python SDK | 3.15.0 | model adapter |

## Referensi resmi

- [LangChain Python docs](https://docs.langchain.com/oss/python/langchain/overview)
- [LangChain v1 release](https://docs.langchain.com/oss/python/releases/langchain-v1)
- [OpenAI quickstart](https://platform.openai.com/docs/quickstart)

## Lanjut ke praktik

Notebook membuat retriever dan response dengan mock model; adapter provider dapat ditambahkan setelah API key tersedia.

## Posisi part dalam bootcamp

Part ini menyusun retrieval-augmented generation dari komponen yang telah dipahami: source, chunk, embedding, retriever, prompt, model, parser, dan citation. LangChain dipakai sebagai orchestration library, tetapi boundary dan contract tetap milik aplikasi Anda.

## Kapan konsep ini dipakai

Gunakan RAG ketika jawaban membutuhkan knowledge yang berubah atau private dan model tidak boleh mengandalkan memory parameternya. RAG tidak otomatis benar: kualitas chunk, metadata, retrieval, prompt, dan citation harus diuji bersama.

## Walkthrough terpandu: assistant SOP Fajar

1. Masukkan tiga dokumen SOP sintetis dengan document_id dan version berbeda.
2. Parse, chunk, embed, dan index. Simpan metadata section dan effective_date.
3. Terima pertanyaan, terapkan access/effective filter, lalu retrieve top-k evidence.
4. Bentuk prompt yang menyertakan evidence berlabel dan instruksi untuk abstain jika evidence tidak cukup.
5. Generate jawaban dengan citation document_id/section. Parse output ke schema.
6. Jika retrieval kosong, kembalikan escalation response; jika evidence konflik, tampilkan konflik dan minta human review.
7. Simpan trace minimal: query, retrieved ids, prompt_version, model_id, latency, token usage, result status, tanpa secret atau data sensitif.

## Latihan terbimbing

- Uji pertanyaan yang jawabannya berada pada satu dan beberapa dokumen.
- Bandingkan top-k 3 dan top-k 8.
- Tambahkan citation validator.
- Buat fake retriever agar unit test tidak memerlukan provider.
- Ukur retrieval hit rate dan answer groundedness pada baseline set.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menjelaskan setiap komponen RAG, menunjukkan evidence yang mendasari jawaban, dan menangani empty/conflicting retrieval secara aman.

## Jembatan ke assignment

Assignment harus berisi app, documents, tests, trace schema, citation examples, abstention examples, dan README yang membedakan local/mock mode dengan provider mode.
