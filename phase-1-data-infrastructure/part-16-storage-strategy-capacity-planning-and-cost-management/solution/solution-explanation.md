# Solution Explanation — Storage Strategy, Capacity Planning & Cost Management

Solusi memisahkan payload dari overhead, memberi replication dan headroom, lalu melakukan sensitivity 2x/5x. Event panas disimpan pada store berlatency rendah, raw di object storage dengan lifecycle, dan agregasi di serving layer.

Kesalahan umum adalah menghitung payload saja, mengabaikan index/replication, dan menganggap archive selalu gratis. Semua asumsi harus dapat diganti dan dihitung ulang.
