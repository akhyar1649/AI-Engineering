# Solution Explanation — Integration Readiness & Compatibility

Solusi memblokir partner tanpa idempotency/retry contract meski score lainnya baik. Adapter memetakan status vendor ke canonical Kirimin dan contract tests menyimpan evidence per release.

Kesalahan umum adalah merata-ratakan blocker, menganggap 200 response berarti business success, dan menaruh vendor mapping tersebar di banyak node.
