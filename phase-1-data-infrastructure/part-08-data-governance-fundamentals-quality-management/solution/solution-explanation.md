# Solution Explanation — Data Governance Fundamentals & Quality Management

Solusi memisahkan ownership domain dari custodianship pipeline, lalu memberi severity berbasis dampak. Check key dan integrity bersifat blocking; outlier bersifat quarantine/review agar bisnis tidak kehilangan transaksi valid.

Kesalahan umum: menuntut semua kolom non-null, membuat check tanpa owner, dan hanya menyimpan pass/fail tanpa sample failure. Quality result harus cukup informatif untuk tindakan.
