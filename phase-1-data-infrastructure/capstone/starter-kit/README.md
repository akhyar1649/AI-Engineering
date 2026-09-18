# Capstone 1 Starter Kit

Gunakan struktur ini sebagai titik awal. Anda boleh mengganti implementasi selama contract pada case brief tetap terpenuhi.

```text
starter-kit/
├── README.md
├── pyproject.toml
├── src/kirimin_pipeline/
│   ├── __init__.py
│   ├── generate.py
│   ├── pipeline.py
│   ├── quality.py
│   └── api.py
├── tests/
├── data/.gitkeep
└── docs/architecture.md
```

Mulai dengan `python -m kirimin_pipeline.generate --rows 10000 --seed 42`, lalu jalankan pipeline pada satu partition. Jangan commit output data besar; simpan generator dan sample kecil saja.
