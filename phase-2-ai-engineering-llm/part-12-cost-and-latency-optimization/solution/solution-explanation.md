# Solution Explanation — Cost & Latency Optimization

Solusi memakai fast route untuk FAQ, strong route untuk ambiguous/high-risk, cache hanya untuk response yang access-safe, dan invalidation pada prompt/SOP version. Quality gate memblokir optimasi jika groundedness atau safety turun.

Kesalahan umum: cache tanpa access key, merangkum context hingga kehilangan exception, dan mengukur average latency tanpa p95.
