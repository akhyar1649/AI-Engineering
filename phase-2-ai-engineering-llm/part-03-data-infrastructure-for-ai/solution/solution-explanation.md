# Solution Explanation — Data Infrastructure for AI

Solusi memisahkan raw document dari chunk index, menyimpan effective date/access label, dan menerapkan filter sebelum similarity search. Chunk id memuat source/version agar citation dan reindex dapat dilacak.

Kesalahan umum: indexing tanpa metadata access, menghapus dokumen lama tanpa deletion propagation, dan menganggap top-k tinggi selalu meningkatkan jawaban.
