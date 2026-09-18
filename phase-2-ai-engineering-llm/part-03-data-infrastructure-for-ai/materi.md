# Data Infrastructure for AI

**Fase:** 2 — AI Engineering (LLM)  
**Section:** AI & LLM Foundations

> Diverifikasi: Pinecone Python SDK v10.0.0 — sumber: https://sdk.pinecone.io/python/ — tanggal cek: 2026-09-18
> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18

## Tujuan belajar

- merancang ingestion dokumen yang memiliki metadata dan provenance;
- memilih chunking berdasarkan struktur dokumen dan query;
- menjelaskan embedding, vector index, hybrid search, dan reranking;
- menerapkan redaction, access control, dan freshness policy;
- mengukur retrieval quality sebelum menilai generation.

## Konteks di PT Kirimin

SOP Fajar tersebar dalam PDF, Markdown, dan spreadsheet internal. Assistant harus mengambil versi SOP yang tepat, menghormati access scope, dan dapat menunjukkan dokumen sumber.

## Konsep kunci

### Ingestion dan provenance

**Definisi teknis:** Ingestion mengubah sumber menjadi canonical documents/chunks dengan metadata seperti document id, version, effective date, owner, access label, dan checksum.

**Penjelasan sederhana:** Sebelum memasukkan halaman ke mesin pencari, Anda perlu tahu dokumen itu milik siapa, versi berapa, dan kapan berlaku.

### Chunking

**Definisi teknis:** Chunking membagi dokumen menjadi unit retrieval. Chunk terlalu kecil kehilangan context; terlalu besar menurunkan precision dan menghabiskan context window.

**Penjelasan sederhana:** Potongan SOP harus cukup besar untuk menjelaskan satu aturan, tetapi tidak membawa satu buku penuh setiap kali dicari.

### Vector search

**Definisi teknis:** Vector search mengambil item terdekat berdasarkan similarity metric. Index dan metadata filter menentukan trade-off latency, recall, cost, dan isolation.

**Penjelasan sederhana:** Cari dokumen berdasarkan kemiripan makna, bukan hanya kata yang identik.

### AI data governance

**Definisi teknis:** AI data layer harus mengatur PII redaction, access-aware retrieval, retention, deletion propagation, evaluation set lineage, dan reindex policy.

**Penjelasan sederhana:** Dokumen yang bisa dicari assistant tetap harus mengikuti hak akses manusia yang menggunakannya.

## Reference architecture

`source → parse → classify → redact → chunk → embed → index → retrieve → cite`. Simpan raw dan processed manifest agar reindex dapat dilakukan tanpa menebak history.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| Pinecone Python SDK | 10.0.0 | vector index example |
| PostgreSQL | 18.6 | metadata/structured source |
| Gemini Embedding | embedding-2 preview | embedding example; pin saat API digunakan |

## Referensi resmi

- [Pinecone Python SDK](https://sdk.pinecone.io/python/)
- [Pinecone vector concepts](https://docs.pinecone.io/guides/indexes/understanding-indexes)
- [Gemini embeddings](https://ai.google.dev/gemini-api/docs/embeddings)

## Lanjut ke praktik

Notebook membuat chunk metadata dan cosine similarity sederhana tanpa service eksternal.

## Posisi part dalam bootcamp

Part ini menghubungkan pipeline data Fase 1 dengan kebutuhan aplikasi AI. Data yang valid untuk dashboard belum tentu siap untuk embedding atau retrieval. Anda akan membangun ingestion, metadata, versioning, dan update strategy agar evidence AI dapat ditelusuri.

## Kapan konsep ini dipakai

Gunakan AI data infrastructure ketika knowledge berasal dari dokumen, tabel, event, atau kombinasi sumber yang berubah. Pisahkan source of truth dari index/embedding layer. Setiap chunk atau record harus memiliki document_id, version, source, timestamp, access metadata, dan deletion behavior.

## Walkthrough terpandu: membangun knowledge base SOP

1. Inventarisir SOP PDF/Markdown, FAQ, dan metric definition. Tandai owner, version, effective_date, dan sensitivity.
2. Normalisasi text tanpa menghilangkan heading, table meaning, atau policy boundary.
3. Chunk berdasarkan unit makna; simpan chunk_index, parent_document_id, section, dan character/token count.
4. Buat embedding dan index metadata. Jangan mencampur dokumen expired dengan active tanpa filter.
5. Simulasikan update SOP: buat versi baru, re-index hanya bagian berubah, dan pertahankan lineage.
6. Simulasikan deletion/access revocation. Retrieval harus berhenti mengembalikan chunk yang tidak lagi boleh dipakai.
7. Buat ingestion report: documents_seen, chunks_created, failed_documents, stale_documents, dan index_version.

## Latihan terbimbing

- Bandingkan fixed-size dan semantic chunking pada SOP yang sama.
- Buat metadata filter untuk product, role, locale, dan effective_date.
- Uji re-ingestion terhadap dokumen yang sama.
- Buat dead-letter list untuk dokumen gagal diparse.
- Jelaskan perbedaan source freshness dan index freshness.

## Checkpoint penguasaan

Anda siap lanjut jika setiap evidence memiliki lineage dan access metadata, re-ingestion idempotent, serta update/delete tidak meninggalkan data stale yang dapat diretrieve.

## Jembatan ke assignment

Assignment harus menghasilkan ingestion pipeline, metadata schema, versioning strategy, sample index, update/delete test, dan operational report.
