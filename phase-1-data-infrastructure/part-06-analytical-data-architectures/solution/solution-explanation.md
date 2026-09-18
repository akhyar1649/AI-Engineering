# Solution Explanation — Analytical Data Architectures

Solusi memilih analytical schema sebagai langkah awal karena workload Kirimin masih dapat dilayani dengan platform relational yang dikuasai tim, lalu menyiapkan jalur evolusi ke lakehouse ketika volume/event variety meningkat. Fact table menyatakan grain satu baris per order dan dimension city memiliki surrogate key.

Kesalahan umum adalah memilih teknologi berdasarkan popularitas, menggabungkan fact dengan grain berbeda, dan menyebut “real-time” tanpa target freshness. Perbaiki dengan workload matrix dan SLO yang terukur.
