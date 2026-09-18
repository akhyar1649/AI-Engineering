# Solution Explanation — Capstone 3

Solusi menjadikan event ledger sebagai durable boundary sebelum action, lalu menggunakan idempotency key untuk notification/ticket side effects. Adapter menormalkan payload courier sebelum workflow mengambil keputusan. AI hanya mengklasifikasikan exception dan confidence rendah masuk human review; MCP read tool tidak diberi finance write scope.

Kesalahan umum: ack sebelum persistence, menggunakan vendor status langsung di banyak node, retry side effect tanpa dedup, replay tanpa dry-run, dan menambahkan AI/MCP tanpa risk boundary.
