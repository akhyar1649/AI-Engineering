# Tech Stack Version Log

Tanggal verifikasi awal: **2026-09-18**. Versi di bawah adalah target pembelajaran pada tanggal tersebut dan harus diverifikasi ulang jika pengerjaan dilanjutkan setelah jeda panjang. Link selalu diarahkan ke dokumentasi atau release page resmi.

| Tool | Versi target/verifikasi | Sumber resmi | Dipakai pada |
|---|---:|---|---|
| Python | 3.14.7 | https://docs.python.org/3/ | seluruh fase |
| PostgreSQL | 18.6 | https://www.postgresql.org/docs/release/ | Fase 1, 2, 3 |
| Apache Airflow | 3.3.2 | https://airflow.apache.org/docs/apache-airflow/3.3.2/ | Fase 1 |
| Docker Engine | 29.6.2 | https://docs.docker.com/engine/release-notes/29/ | seluruh fase |
| pandas | 3.0.3 | https://pandas.pydata.org/docs/whatsnew/v3.0.3.html | Fase 1 |
| FastAPI | 0.141.1 | https://fastapi.tiangolo.com/release-notes/ | Fase 1, 2 |
| MongoDB | 8.3 series | https://www.mongodb.com/docs/manual/release-notes/ | Fase 1 |
| Great Expectations | 1.23.0 | https://docs.greatexpectations.io/docs/core/changelog/ | Fase 1 |
| Apache Spark | 4.2.0 | https://spark.apache.org/releases/ | Fase 1 |
| OpenAI Python SDK | 3.15.0 | https://github.com/openai/openai-python/releases | Fase 2, 3 |
| LangChain | 1.x, pin per notebook | https://docs.langchain.com/oss/python/releases/langchain-v1 | Fase 2 |
| CrewAI | pin per notebook | https://docs.crewai.com/ | Fase 2 |
| Hugging Face Transformers | 5.17.0 | https://huggingface.co/docs/transformers/main/ | Fase 2 |
| Pinecone Python SDK | 10.0.0 | https://sdk.pinecone.io/python/ | Fase 2 |
| Gemini API model | gemini-3.6-flash stable; embedding-2 preview | https://ai.google.dev/gemini-api/docs/models | Fase 2, 3 |
| DeepEval | pin per notebook | https://deepeval.com/docs/introduction | Fase 2 |
| Ollama | pin release/image saat deployment | https://ollama.com/library | Fase 2 |
| LangSmith | current hosted platform; record workspace date | https://docs.smith.langchain.com/ | Fase 2 |
| Redis | pin image saat deployment | https://redis.io/docs/latest/ | Fase 2 |
| n8n | 2.x, pin deployment image | https://docs.n8n.io/release-notes/ | Fase 3 |
| Model Context Protocol | specification current | https://modelcontextprotocol.io/specification/ | Fase 3 |
| Terraform AWS Provider | 6.62.0 | https://registry.terraform.io/providers/-/aws/latest | Fase 1, 3 |
| Databricks Runtime | 19 | https://docs.databricks.com/aws/en/release-notes/runtime/19 | Fase 1 |

## Catatan verifikasi

- `Python 3.14.7` tercantum pada halaman dokumentasi Python resmi.
- PostgreSQL 18.6 tercantum pada arsip release notes resmi PostgreSQL.
- Airflow 3.3.2, Docker Engine 29.6.2, pandas 3.0.3, FastAPI 0.141.1, MongoDB 8.3, dan Great Expectations 1.23.0 tercantum pada halaman resmi masing-masing.
- OpenAI Python SDK 3.15.0 diverifikasi dari release page repository resmi OpenAI di GitHub pada tanggal 2026-09-18.
- Untuk tool yang tidak memiliki satu halaman versi stabil yang mudah dipin, notebook wajib mencatat output `pip index versions` atau release page yang dipakai pada saat notebook dibuat. Versi model/API harus dipin secara eksplisit bila provider mendukung snapshot.

## Format catatan per part

Setiap `materi.md` dan notebook yang menggunakan tool harus menyertakan blok berikut:

```text
> Diverifikasi: <nama-tool> v<versi> — sumber: <link resmi> — tanggal cek: 2026-09-18
```

Jika tool sudah deprecated, pertahankan nama topik kurikulum tetapi gunakan pendekatan pengganti yang direkomendasikan resmi dan catat alasan perubahan di file ini.
