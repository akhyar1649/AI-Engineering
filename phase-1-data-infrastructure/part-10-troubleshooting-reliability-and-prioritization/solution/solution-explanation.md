# Solution Explanation — Troubleshooting Reliability & Prioritization

Solusi dimulai dengan impact dan timeline, lalu mengecek dependency dan recent changes. Retry hanya dipakai untuk transient errors dengan batas dan backoff; quality failure tidak di-retry tanpa perubahan input.

Kesalahan umum adalah menganggap root cause pertama sebagai fakta, menambah retry untuk semua error, dan tidak menulis owner corrective action. Postmortem harus menghasilkan perubahan sistem yang dapat diverifikasi.
