# Solution Explanation — RAG for Structured Data Sources

Solusi memakai query template berparameter untuk pertanyaan yang known, bukan membiarkan model bebas mengakses schema. Query dijalankan dengan read-only role, timeout, dan row limit; angka disertai query definition dan timestamp.

Kesalahan umum: hanya mengecek SQL diawali `SELECT`, mengandalkan prompt untuk security, dan memberikan result tanpa periode/timezone.
