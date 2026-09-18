# Solution Explanation — Prompt Technique and Optimization

Solusi menempatkan policy pada system instruction, memisahkan user content, dan membatasi model pada evidence. Output memiliki citations dan `needs_human`; test set mencakup injection dan konflik SOP.

Kesalahan umum: menaruh aturan keamanan hanya di user prompt, memakai contoh yang bocor sebagai few-shot, dan mengoptimalkan berdasarkan satu pertanyaan.
