# RAG for Structured Data Sources

**Fase:** 2 — AI Engineering (LLM)  
**Section:** RAG & AI Agent Development

> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18
> Diverifikasi: OpenAI Python SDK v3.15.0 — sumber: https://github.com/openai/openai-python/releases — tanggal cek: 2026-09-18

## Tujuan belajar

- membedakan semantic retrieval dokumen dan query structured data;
- merancang text-to-SQL dengan schema grounding dan validation;
- mencegah SQL injection, data leakage, dan query runaway;
- menggabungkan result table dengan unstructured evidence;
- menyajikan provenance untuk angka yang dihasilkan AI.

## Konteks di PT Kirimin

Fajar bertanya “berapa tiket urgent yang belum selesai minggu ini?” SOP tidak cukup; answer harus mengambil angka dari PostgreSQL. Assistant perlu tahu kapan melakukan SQL dan kapan mengambil dokumen.

## Konsep kunci

### Structured retrieval

**Definisi teknis:** Structured retrieval mengeksekusi query terhadap schema terdefinisi lalu mengubah hasil menjadi context atau response. Ia membutuhkan schema, permissions, query validation, dan result limits.

**Penjelasan sederhana:** Untuk menghitung order, assistant harus membuka buku kas, bukan mencari kalimat yang kebetulan menyebut angka.

### Text-to-SQL boundary

**Definisi teknis:** Text-to-SQL memetakan natural language ke SQL. Production design harus membatasi tables/columns, read-only role, parameterize values, lint/parse SQL, timeout, dan row limit.

**Penjelasan sederhana:** Assistant boleh meminta petugas menghitung, tetapi tidak boleh diberi kunci untuk menghapus buku.

### Hybrid answer

**Definisi teknis:** Hybrid answer menggabungkan numeric result, source metadata, dan policy document. Setiap claim harus memiliki provenance berbeda jika sumbernya berbeda.

**Penjelasan sederhana:** Jawaban bisa berkata “87 tiket” dari database dan “eskalasi dalam 30 menit” dari SOP; keduanya harus menunjukkan asal.

## Safe query flow

`intent classify → schema allowlist → generate SQL → parse/validate → execute read-only → bound result → explain with citations`. Jika intent ambiguous, minta klarifikasi.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| PostgreSQL | 18.6 | structured source |
| OpenAI Python SDK | 3.15.0 | model adapter |

## Referensi resmi

- [PostgreSQL roles](https://www.postgresql.org/docs/current/user-manag.html)
- [PostgreSQL transaction read-only](https://www.postgresql.org/docs/current/sql-set-transaction.html)
- [OpenAI function calling/tools](https://platform.openai.com/docs/guides/function-calling)

## Lanjut ke praktik

Notebook menjalankan allowlisted query pada in-memory SQLite dan menolak statement mutating.

## Posisi part dalam bootcamp

Part ini membawa pola RAG ke data yang memiliki schema dan angka: order, shipment, KPI, dan metric dictionary. Tantangan utama bukan hanya mengambil dokumen, tetapi menghasilkan query yang benar, membatasi akses, dan mencegah model mengarang angka.

## Kapan konsep ini dipakai

Gunakan structured retrieval ketika pertanyaan membutuhkan filter, agregasi, atau latest record dari database. Gunakan semantic retrieval untuk penjelasan naratif. Sering kali keduanya digabung: SQL mengambil angka, dokumen memberi definisi dan caveat.

## Walkthrough terpandu: “berapa backlog Jakarta?”

1. Klasifikasikan pertanyaan sebagai metric query, bukan free-form document question.
2. Ambil metric contract untuk definisi backlog, timezone, date filter, dan source table.
3. Validasi parameter city dan date range terhadap allowlist.
4. Generate SQL dari template aman atau query plan terkontrol; jangan mengeksekusi arbitrary SQL dari user.
5. Jalankan query dengan read-only role, kembalikan rows, freshness, dan query_id.
6. Ambil dokumentasi definisi KPI untuk menjelaskan denominator dan caveat.
7. Render answer dengan angka, periode, source, dan link evidence. Jika data stale atau query kosong, state-kan dengan jelas.

## Latihan terbimbing

- Buat lima metric contract dan template query.
- Uji city injection dan invalid date range.
- Bandingkan direct SQL tool dengan retrieval metric dictionary.
- Tambahkan maximum row limit dan timeout.
- Buat regression set untuk query yang sering salah denominator.

## Checkpoint penguasaan

Anda siap lanjut jika dapat membedakan retrieval angka versus retrieval penjelasan, membatasi query, dan memberikan freshness serta evidence bersama hasil.

## Jembatan ke assignment

Assignment harus menghasilkan structured retrieval module, contracts, safe query templates, permission model, test cases, dan contoh jawaban dengan evidence.
