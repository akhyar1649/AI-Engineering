# Solution Explanation — Integrated System

Solusi memakai event ledger sebagai source of truth dan orchestrator untuk langkah yang membutuhkan urutan. Notification failure masuk retry/compensation queue tanpa menghapus ledger event.

Kesalahan umum adalah menganggap semua external calls atomic dan tidak menyimpan correlation id lintas service.
