# Solution Explanation — AI Agent

Solusi memilih single router dengan tiga safe tools dan human handoff; multi-agent tidak diperlukan untuk scope ini. Tool schema typed, max steps, timeout, trace, dan no-refund permission mencegah side effect yang tidak disetujui.

Kesalahan umum: tool description ambigu, loop tanpa batas, memberikan database write access, dan menganggap agent success hanya karena model berhenti.
