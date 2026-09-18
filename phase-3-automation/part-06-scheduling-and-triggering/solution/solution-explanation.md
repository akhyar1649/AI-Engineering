# Solution Explanation — Scheduling & Triggering

Solusi memakai event_id untuk webhook dan business_date untuk scheduled reconciliation. Backfill menggunakan dry-run/default no-notify agar historical processing tidak memicu side effect lama.

Kesalahan umum adalah memakai process timestamp sebagai key, mengabaikan timezone, dan menjalankan backfill dengan notification aktif.
