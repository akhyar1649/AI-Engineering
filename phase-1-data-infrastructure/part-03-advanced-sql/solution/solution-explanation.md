# Solution Explanation — Advanced SQL

Solusi membuat `ranked_events` sebagai CTE, memilih event terbaru dengan `ROW_NUMBER`, kemudian memakai `LAG` untuk duration. Event disortir berdasarkan timestamp, tetapi timestamp yang lebih awal dari event sebelumnya ditandai sebagai anomali, bukan diam-diam diperbaiki.

Kesalahan umum: memakai `MAX(status)` untuk memilih status terakhir, menghitung SLA setelah `GROUP BY` terlalu dini, dan menganggap `EXPLAIN` cost sebagai waktu aktual. Perbaiki dengan ordering eksplisit, grain per event, dan pembandingan `EXPLAIN ANALYZE` pada dataset aman.
