# Solution Explanation — AI on Automation

Solusi memakai AI untuk classification/summary, bukan keputusan refund. Confidence rendah atau category sensitif masuk human review dengan context dan trace id; fallback deterministic template menjaga operasi saat provider down.

Kesalahan umum adalah membiarkan AI langsung memanggil side-effect node dan memperlakukan confidence sebagai jaminan kebenaran.
