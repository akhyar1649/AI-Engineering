# Solution Explanation — Fine-Tuning Model

Solusi menolak fine-tuning sebagai first response untuk SOP yang berubah; ia memakai RAG untuk knowledge dan mengusulkan fine-tuning hanya jika intent/style baseline tetap gagal setelah retrieval diperbaiki. Dataset dipisah, disanitasi, dan memiliki hard cases.

Kesalahan umum: train/test leakage, memasukkan PII, mengukur hanya training loss, dan tidak memiliki promotion/rollback policy.
