# Solution Explanation — Model Serving & Production-Grade Deployment

Solusi memisahkan gateway/routing dari model runtime, menetapkan high-risk human review, membatasi queue/timeout, dan menyimpan model/prompt version. Hosted API menjadi default untuk skala awal; self-hosted hanya jika requirement privacy/latency/cost membenarkan operational burden.

Kesalahan umum: autoscaling tanpa provider rate limit, liveness yang memanggil model, dan deploy model baru tanpa canary atau rollback artifact.
