# Solution Explanation — n8n Data Handling & Logic

Solusi menetapkan data contract antar node, memisahkan per-item processing dari workflow summary, dan menggunakan event id sebagai dedup key. Loop memiliki max pages/items dan partial response masuk exception path.

Kesalahan umum adalah mengandalkan execution order sebagai idempotency dan menggabungkan array tanpa mempertahankan correlation id.
