# Assessment Handbook — Cara Mengerjakan Assignment, Capstone, dan Final Project

Dokumen ini adalah kontrak pengerjaan untuk seluruh bootcamp. Setiap assignment menguji part yang baru selesai, tetapi outputnya juga harus dapat dipakai oleh part berikutnya. Jangan mengumpulkan screenshot sebagai satu-satunya bukti; kumpulkan code, fixture, test, result, dan reasoning yang dapat dijalankan ulang.

## Alur kerja yang wajib dipakai

1. Baca konteks kasus dan nyatakan keputusan bisnis yang hendak didukung.
2. Baca bagian Posisi part, Kapan konsep ini dipakai, Walkthrough, dan Checkpoint pada materi.
3. Buka notebook dan jalankan dari awal sampai akhir dalam local/mock mode. Catat input, output, warning, dan asumsi yang ditemukan.
4. Tulis contract sebelum implementasi: input, output, grain atau schema, error behavior, owner, dan acceptance criteria.
5. Implementasikan satu vertical slice kecil yang selesai dari input sampai output.
6. Tambahkan happy-path test dan minimal dua failure-path test yang relevan dengan kasus.
7. Jalankan ulang dengan seed atau fixture yang sama. Untuk pipeline dan workflow, buktikan idempotence atau jelaskan mengapa tidak dapat dijamin.
8. Buat evidence folder berisi command, test result, sample output, quality/evaluation result, dan limitation.
9. Tulis notes.md dengan keputusan, trade-off, tool/version yang benar-benar dipakai, serta langkah reproduksi.
10. Jalankan self-check pada assignment sebelum submit.

## Tools per fase

### Fase 1 — Data Infrastructure

Gunakan Python 3.14.7 dan pandas 3.0.3 untuk notebook, generator, dan transformasi tabular. Gunakan SQLite fallback pada notebook ketika server tidak tersedia, lalu uji ulang syntax PostgreSQL 18.6 untuk query yang ditujukan ke database. Gunakan Jupyter untuk eksplorasi, Docker Engine 29.6.2 untuk service lokal, Apache Airflow 3.3.2 untuk orchestration yang memang diperlukan, Apache Spark 4.2.0 untuk distributed-processing exercise, dan MongoDB 8.3 untuk document-store exercise.

Tool wajib untuk setiap submission ditentukan oleh tugas. Jangan menambahkan service hanya agar terlihat kompleks. Jika tool tidak tersedia, gunakan adapter/mock yang memiliki contract sama, nyatakan perbedaannya, dan sertakan command untuk menjalankan local mode.

### Fase 2 — AI Engineering & LLM

Gunakan Python 3.14.7 sebagai runtime. Gunakan OpenAI SDK 3.15.0, LangChain 1.x, Pinecone SDK 10.0.0, Google Gemini adapter, Transformers 5.17.0, Ollama, DeepEval, dan LangSmith hanya bila sesuai dengan scope assignment. Provider dapat diganti fake adapter/local model untuk latihan; API key tidak boleh ditulis di notebook, log, atau repository.

Setiap AI submission wajib mencatat model/provider identifier, prompt/index version, input fixture, output schema, latency, token atau cost signal bila tersedia, fallback, dan limitation. Untuk agent atau tool call, sertakan permission serta side-effect boundary.

### Fase 3 — Automation

Gunakan n8n 2.x untuk workflow exercise, Docker Engine 29.6.2 untuk local runtime, PostgreSQL atau Python fake service untuk ledger/adapter, Redis bila memang dibutuhkan untuk queue atau idempotency, dan MCP sesuai contract/spec yang dipakai oleh implementasi. Workflow JSON harus dapat diimport; credential harus direferensikan sebagai placeholder atau environment variable.

Setiap workflow submission wajib memiliki trigger contract, node input/output, correlation id, idempotency strategy, retry matrix, exception route, replay procedure, dan execution evidence. Jangan menguji side effect ke customer nyata; gunakan fake notification, sandbox, atau dry-run mode.

## Bukti hasil minimal

Setiap assignment harus dapat menjawab:

- input apa yang digunakan dan bagaimana cara membuatnya;
- output apa yang dihasilkan dan bagaimana memeriksa kebenarannya;
- test apa yang dijalankan dan apa hasilnya;
- bagaimana sistem berperilaku pada input kosong, invalid, duplicate, timeout, atau dependency failure yang relevan;
- tool dan versi apa yang dipakai;
- asumsi apa yang belum terbukti;
- bagian mana yang local/mock dan apa yang harus berubah saat deployment.

## Self-check sebelum submit

- [ ] Repository atau folder submission dapat dijalankan dari README pada environment baru.
- [ ] Tidak ada credential, data pelanggan nyata, atau secret pada file, output, dan trace.
- [ ] Ada fixture atau generator sintetis dengan seed jika randomness digunakan.
- [ ] Ada test untuk normal case dan failure case.
- [ ] Output utama dapat diverifikasi dengan angka, schema, query, atau assertion.
- [ ] Error tidak ditelan tanpa reason, status, dan correlation identifier.
- [ ] Assignment menjelaskan kapan tool dipakai dan kapan tidak dipakai.
- [ ] Notes menyebut trade-off, limitation, dan next step.
- [ ] Nama file dan format sesuai bagian Format pengumpulan.
- [ ] Hubungan output assignment dengan part berikutnya tertulis jelas.

## Capstone dan final project

Capstone harus menggabungkan artifact beberapa part, sehingga peserta wajib memulai dari problem brief dan architecture contract, bukan langsung coding. Milestone, evidence, test, deployment/demo, report, dan presentation harus terhubung. Final project harus menunjukkan keputusan pengembangan dari discovery sampai operate, termasuk backlog setelah submission. Rubric menilai reasoning dan evidence, bukan jumlah tool.
