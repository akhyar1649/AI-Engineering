# Solution Explanation — Troubleshooting AI Chatbot and Agent

Solusi memprioritaskan policy violation sebagai incident tertinggi, mengaktifkan kill switch, lalu membandingkan stage trace. SOP stale ditangani dengan index/version freshness fix dan regression cases, bukan hanya menambah prompt instruction.

Kesalahan umum: mengulang prompt secara acak, menghapus trace sehingga diagnosis hilang, dan menyalakan kembali tool tanpa test negative cases.
