# Solution Explanation — NoSQL in Practice (MongoDB)

Solusi menggunakan `event_id` sebagai unique idempotency key, menyimpan event immutable, dan memilih latest berdasarkan `event_time` setelah dedupe. Index compound mendukung lookup shipment dan sort descending.

Kesalahan umum adalah memakai timestamp sebagai unique key, mengoverwrite event lama tanpa audit, dan menaruh semua event dalam satu document yang tidak bounded.
