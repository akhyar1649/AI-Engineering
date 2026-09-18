# RAG Optimization & Troubleshooting

**Fase:** 2 — AI Engineering (LLM)  
**Section:** RAG & AI Agent Development

> Diverifikasi: Pinecone Python SDK v10.0.0 — sumber: https://sdk.pinecone.io/python/ — tanggal cek: 2026-09-18
> Diverifikasi: LangChain Python v1.x — sumber: https://docs.langchain.com/oss/python/releases/langchain-v1 — tanggal cek: 2026-09-18

## Tujuan belajar

- memisahkan retrieval failure dari generation failure;
- menganalisis recall, precision, MRR, context precision, dan faithfulness;
- mengoptimalkan chunk, query rewrite, hybrid retrieval, reranking, dan top-k;
- men-debug latency dan context overflow;
- membuat regression set untuk perubahan index/prompt/model.

## Konteks di PT Kirimin

Prototype menemukan SOP yang benar hanya 70% dari waktu. Menambah top-k membuat context terlalu panjang dan latency meningkat. Anda harus menemukan tahap yang gagal sebelum mengganti model.

## Konsep kunci

### Retrieval versus generation error

**Definisi teknis:** Retrieval error terjadi saat evidence relevan tidak masuk context; generation error terjadi saat model salah menggunakan context yang benar. Diagnosis membutuhkan labeled queries dan stage-level trace.

**Penjelasan sederhana:** Petugas bisa gagal karena mengambil buku salah atau membaca buku benar dengan keliru. Solusinya berbeda.

### Recall dan precision

**Definisi teknis:** Recall mengukur seberapa banyak relevant items yang ditemukan; precision mengukur proporsi hasil yang relevan. MRR memperhatikan posisi relevant item pertama.

**Penjelasan sederhana:** Menemukan semua buku termasuk banyak buku salah bukan pengalaman pencarian yang baik.

### Query rewrite/reranking

**Definisi teknis:** Query rewrite memperkaya atau mengubah query untuk retrieval; reranker mengurutkan kandidat dengan model/heuristic yang lebih mahal setelah initial retrieval.

**Penjelasan sederhana:** Petugas pertama mengambil satu rak; petugas kedua memilih buku paling tepat dari rak itu.

### Latency budget

**Definisi teknis:** End-to-end latency adalah jumlah latency retrieval, rerank, model, serialization, dan network; optimasi harus mengalokasikan budget per stage.

**Penjelasan sederhana:** Waktu jawab bukan hanya waktu mengetik; ada waktu mencari buku dan menyiapkan meja.

## Troubleshooting checklist

Log query, filters, candidate ids/scores, selected context, prompt version, model latency, output validation, dan final route. Jangan log raw PII secara sembarangan.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| Pinecone Python SDK | 10.0.0 | vector query |
| LangChain | 1.x | composition/tracing |

## Referensi resmi

- [Pinecone performance](https://docs.pinecone.io/guides/optimize/)
- [LangChain retrieval concepts](https://docs.langchain.com/oss/python/langchain/retrieval)

## Lanjut ke praktik

Notebook menghitung precision/recall dari labeled toy set dan menunjukkan trade-off top-k.

## Posisi part dalam bootcamp

Part ini mengajarkan diagnosis ketika RAG tidak menjawab dengan benar. Anda akan memisahkan retrieval failure, context failure, generation failure, dan data freshness failure. Optimasi dilakukan berdasarkan trace dan evaluation, bukan intuisi prompt saja.

## Kapan konsep ini dipakai

Gunakan troubleshooting RAG ketika citation salah, answer tidak grounded, relevant document tidak ditemukan, atau latency/cost meningkat. Perbaiki layer pertama yang gagal; jangan menambah k tanpa mengetahui apakah retriever memang melewatkan evidence.

## Walkthrough terpandu: SOP lama selalu diretrieve

1. Simpan query, expected document/version, retrieved ids, scores, filters, prompt_version, answer, dan latency.
2. Tanyakan apakah dokumen baru masuk index. Jika tidak, ini ingestion/index freshness problem.
3. Jika dokumen ada tetapi tidak terambil, uji chunk boundary, metadata filter, embedding, dan top-k.
4. Jika evidence benar tetapi answer salah, uji prompt instruction, context ordering, parser, dan conflict policy.
5. Buat satu perubahan per eksperimen: chunk size, overlap, hybrid search, reranking, atau filter.
6. Ukur recall@k, precision@k, citation accuracy, groundedness, answer correctness, latency, dan cost.
7. Promosikan perubahan hanya jika baseline set membaik tanpa regression pada pertanyaan lain.

## Latihan terbimbing

- Buat tiga failure fixture: missed evidence, stale version, dan conflict.
- Bandingkan dense, keyword, dan hybrid retrieval.
- Buat table error taxonomy.
- Tambahkan trace viewer sederhana berbasis JSONL.
- Tulis rollback criteria untuk index dan prompt version.

## Checkpoint penguasaan

Anda siap lanjut jika dapat menunjuk layer penyebab dengan trace, menguji satu hipotesis per eksperimen, dan melaporkan trade-off quality versus latency/cost.

## Jembatan ke assignment

Assignment harus menyertakan failure taxonomy, before/after metrics, experiment log, changed artifact, regression set, dan rollback recommendation.
