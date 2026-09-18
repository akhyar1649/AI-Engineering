# Solution Explanation — Database and Big Data Pipeline

Solusi menggunakan partition date sebagai unit retry, menyimpan run metadata, dan menulis curated output secara replace/merge berdasarkan key partition. Quality gate menghentikan load ketika invalid rate melewati threshold; record invalid tetap tersedia di quarantine.

Kesalahan umum adalah memakai timestamp saat proses sebagai partition, menulis append setiap retry, dan menjadikan semua error sebagai retryable. Bedakan transient infrastructure failure dari deterministic data failure.
