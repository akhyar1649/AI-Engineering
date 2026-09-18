# Capstone 1 Reference Solution

Reference solution memakai generator sintetis seeded, partitioned raw/curated/quarantine, quality gates blocking/warning, dan API FastAPI minimal. Implementasi mentor dapat menambahkan PostgreSQL, Airflow, Docker, Spark, atau MongoDB sesuai target deployment selama trade-off dijelaskan.

## Review checklist

- Apakah satu retry menghasilkan output yang sama?
- Apakah data invalid dapat ditelusuri ke source batch dan alasan reject?
- Apakah metric contract menyebut denominator, freshness, dan owner?
- Apakah API memiliki health/readiness dan tidak mengembalikan secret?
- Apakah capacity model menyertakan growth, replication, overhead, dan retention?
