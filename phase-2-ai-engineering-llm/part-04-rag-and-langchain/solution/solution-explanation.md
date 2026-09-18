# Solution Explanation — RAG and LangChain

Solusi memisahkan retriever, context formatter, generator, dan output validator. Citation menggunakan stable document id/version, dan model abstain jika retrieval score di bawah threshold atau evidence konflik.

Kesalahan umum: memasukkan seluruh dokumen ke prompt, memakai top-k tanpa filter access/version, dan menganggap citation string otomatis membuktikan claim.
