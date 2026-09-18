# Solution Explanation — Infrastructure as Code & Collaborative Engineering

Solusi memisahkan module dari environment config, melindungi state, dan mensyaratkan plan review. Production memiliki deletion protection dan approval tambahan. CI tidak melakukan apply otomatis tanpa policy dan approval yang sesuai.

Kesalahan umum adalah menyimpan secret di variable plain text, commit state, dan menjalankan `apply` dari laptop tanpa audit trail.
