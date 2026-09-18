# AI Engineer Bootcamp

Repository kurikulum praktis untuk membangun kemampuan AI Engineer dari fondasi data infrastructure, AI engineering berbasis LLM, sampai workflow automation. Seluruh latihan menggunakan studi kasus sintetis PT Kirimin Digital Nusantara agar peserta memahami hubungan antara keputusan teknis dan kebutuhan bisnis.

## Learning path

1. **Fase 1 — Data Infrastructure:** SQL, Python untuk data, pipeline, analytical architecture, governance, reliability, cloud, deployment, NoSQL, dan capacity planning.
2. **Fase 2 — AI Engineering (LLM):** prinsip LLM, prompting, data infrastructure for AI, RAG, agents, serving, evaluation, cost, risk, dan troubleshooting.
3. **Fase 3 — Automation:** automation design, n8n, MCP, reliability, deployment, observability, AI-driven workflow, dan solution fit.
4. **Capstone dan Final Project:** setiap fase berakhir dengan proyek terintegrasi yang memiliki codebase, deployment, laporan, dan presentasi.

## Cara menggunakan repository

1. Baca [persona perusahaan](docs/00-company-persona.md) dan [learning path](docs/00-learning-path-overview.md).
2. Ikuti part secara berurutan. Baca `materi.md`, jalankan `notebook.ipynb`, lalu kerjakan `assignment.md`.
3. Gunakan folder `solution/` hanya untuk review setelah submission selesai.
4. Periksa [log versi tools](docs/00-tech-stack-version-log.md) sebelum menjalankan notebook.
5. Lihat [STATUS.md](STATUS.md) untuk progres pembangunan repository.
6. Gunakan [Course Coherence & Teaching Guide](docs/00-course-coherence-and-teaching-guide.md) untuk memahami hubungan antar-part, output yang dibawa ke part berikutnya, dan standar sesi pembelajaran.
7. Gunakan [Assessment Handbook](docs/00-assessment-handbook.md) sebelum mengerjakan assignment, capstone, atau final project agar tools, bukti hasil, failure test, dan self-check konsisten.

## Prasyarat

- Python dan SQL dasar.
- Terminal dasar dan kemampuan memasang package.
- Pemahaman umum tentang API dan database.
- Tidak diperlukan pengalaman sebelumnya dengan Docker, cloud, LLM, RAG, atau n8n.

## Prinsip repository

- Bahasa penjelasan utama adalah Bahasa Indonesia; nama kode dan istilah teknis mengikuti praktik industri.
- Semua data latihan bersifat sintetis dan dirancang dengan masalah data yang realistis.
- Konsep baru selalu dijelaskan dalam dua lapis: formal/profesional lalu sederhana dengan analogi.
- Versi dan API tool diverifikasi ke dokumentasi resmi dan dicatat terpusat.
- Materi peserta dan solution dipisahkan agar repository dapat dipakai untuk pengajaran.
- Setiap part harus dapat menjawab tiga pertanyaan peserta: masalah apa yang diselesaikan, kapan tool ini dipakai, dan bagaimana hasilnya divalidasi.
- Setiap assignment, capstone, dan final project harus memiliki instruksi pengerjaan, tools yang digunakan, output yang terlihat, failure path, dan hubungan ke pembelajaran berikutnya.

## Struktur utama

```text
docs/
phase-1-data-infrastructure/
phase-2-ai-engineering-llm/
phase-3-automation/
final-project/
STATUS.md
```

## Catatan deployment

Capstone dan final project mendefinisikan deployment live sebagai deliverable. Kredensial, endpoint privat, dan data produksi tidak boleh dimasukkan ke repository. Gunakan environment variable dan dataset sintetis.
