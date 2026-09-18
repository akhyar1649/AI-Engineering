# Solution Explanation — Python Overview

Solusi memisahkan parsing, normalisasi, deduplikasi, dan laporan kualitas. Data input disalin agar fungsi tidak memiliki side effect. Nilai yang gagal diparse menjadi `NaN` dan dihitung; keputusan reject atau quarantine ditulis di report.

Kesalahan umum adalah memakai `inplace=True` tanpa memahami side effect, menangkap `Exception` lalu mengembalikan DataFrame kosong, dan menghapus duplicate tanpa aturan latest-record. Perbaiki dengan kontrak eksplisit, exception yang spesifik, serta test untuk setiap aturan bisnis.
