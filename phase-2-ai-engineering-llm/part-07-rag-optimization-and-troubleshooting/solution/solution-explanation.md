# Solution Explanation — RAG Optimization & Troubleshooting

Solusi memulai dengan labeled set dan mengukur recall/precision sebelum mengubah model. Candidate retrieval dan reranking dipisahkan sehingga failure dapat dilokalisasi; latency budget memastikan peningkatan recall tidak diam-diam merusak UX.

Kesalahan umum: memilih top-k terbesar, memakai LLM judge tanpa calibration, dan menyimpulkan generation failure ketika relevant chunk sebenarnya tidak retrieved.
