# Solution Explanation — Reliability Layer

Solusi membatasi retry pada error transient, memakai total deadline, memvalidasi schema dan policy, lalu mengembalikan fallback yang dapat dijelaskan. Sensitive requests selalu memiliki human review route.

Kesalahan umum adalah retry semua exception, fallback ke jawaban model tanpa evidence, dan mencatat prompt lengkap yang dapat mengandung data sensitif.
