# Solution Explanation — n8n Reliability

Solusi menyimpan raw event sebelum ack, memakai event id dedup, retry hanya transient, dan mengirim permanent failure ke DLQ dengan replay approval. Side effect memiliki idempotency key sendiri.

Kesalahan umum adalah retry setelah side effect tanpa idempotency, menghapus DLQ untuk “membersihkan”, dan tidak memberi age metric.
