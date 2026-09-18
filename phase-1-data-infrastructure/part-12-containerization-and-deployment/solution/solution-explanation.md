# Solution Explanation — Containerization & Deployment

Solusi menjalankan process non-root, memisahkan build/runtime config, menambahkan liveness/readiness, dan memberi rollback condition berdasarkan error rate serta latency. API mengembalikan schema version agar consumer dapat berevolusi dengan aman.

Kesalahan umum: menaruh `.env` di image, menggunakan `latest` tanpa promotion, menganggap HTTP 200 selalu berarti ready, dan tidak memiliki rollback path.
