# Solution Explanation — NoSQL Concepts

Solusi memilih document storage untuk payload tracking yang berevolusi, memakai `shipment_id` untuk lookup utama, serta secondary index terbatas untuk operational query. Event append-only dan idempotency key mencegah duplicate akibat retry.

Kesalahan umum adalah menaruh semua event dalam satu unbounded document dan memilih partition key berdasarkan field yang sering difilter tanpa menghitung distribusi.
