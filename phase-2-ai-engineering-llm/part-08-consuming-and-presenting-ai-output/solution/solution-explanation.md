# Solution Explanation — Consuming and Presenting AI Output

Solusi menggunakan schema version, citations sebagai object terpisah, reason code yang aman untuk user, dan handoff state. Internal prompt/trace tidak dikirim ke UI support.

Kesalahan umum: menampilkan confidence sebagai kebenaran, menampilkan raw exception, dan menganggap partial streaming sebagai final answer.
