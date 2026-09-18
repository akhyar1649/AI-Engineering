# Solution Explanation — Capstone 2

Solusi menjadikan RAG sebagai default untuk FAQ, structured query sebagai tool read-only, dan human review sebagai route untuk refund/account/PII. Setiap output menyimpan citation atau reason code. Evaluasi mencakup retrieval, groundedness, abstention, latency, cost, dan safety cases.

Kesalahan umum yang harus dicari mentor: context tanpa version/access metadata, text-to-SQL tanpa allowlist, confidence palsu, evaluation hanya happy path, dan prompt/trace yang menyimpan PII.
