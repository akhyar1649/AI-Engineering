# Solution Explanation — Data Cleaning and Processing

Solusi mempertahankan raw input, melakukan profiling sebelum perubahan, memakai parser dengan `errors='coerce'`, dan menaruh record yang melanggar aturan ke quarantine dengan alasan. Deduplikasi dilakukan setelah key dan timestamp diparse agar aturan latest-record konsisten.

Kesalahan umum adalah mengisi semua missing dengan nol, menghapus outlier tanpa review, dan memperbaiki tanggal ambigu tanpa menyimpan nilai mentah. Perbaikan: definisikan aturan domain, simpan raw columns, serta ukur jumlah baris di setiap tahap.
