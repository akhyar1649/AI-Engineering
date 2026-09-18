# Consuming and Presenting AI Output

**Fase:** 2 — AI Engineering (LLM)  
**Section:** RAG & AI Agent Development

> Diverifikasi: FastAPI v0.141.1 — sumber: https://fastapi.tiangolo.com/release-notes/ — tanggal cek: 2026-09-18
> Diverifikasi: OpenAI Python SDK v3.15.0 — sumber: https://github.com/openai/openai-python/releases — tanggal cek: 2026-09-18

## Tujuan belajar

- merancang API contract untuk answer, citation, confidence, dan escalation;
- membedakan streaming, synchronous, dan asynchronous consumption;
- menyajikan uncertainty dan source dalam UI yang dipahami user;
- menjaga backward compatibility schema;
- menghindari kebocoran prompt, PII, dan internal trace.

## Konteks di PT Kirimin

Fajar akan memakai assistant melalui dashboard support. UI harus menunjukkan sumber, status confidence, dan tombol eskalasi; ia tidak boleh menyamakan jawaban AI dengan keputusan final.

## Konsep kunci

### Output contract

**Definisi teknis:** Output contract menetapkan schema, field semantics, error codes, versioning, and backward compatibility. Structured output membantu parsing tetapi tidak menjamin semantic correctness.

**Penjelasan sederhana:** Frontend membutuhkan bentuk paket yang stabil; isi paket tetap harus diperiksa.

### Streaming dan UX

**Definisi teknis:** Streaming mengirim partial output sebelum generation selesai; client harus menangani disconnect, cancellation, partial content, dan final metadata.

**Penjelasan sederhana:** User melihat jawaban muncul bertahap, tetapi aplikasi harus tahu apakah kalimat itu sudah final atau masih dapat berubah.

### Uncertainty dan human handoff

**Definisi teknis:** Confidence bukan probabilitas kebenaran otomatis. Handoff policy memanfaatkan evidence score, risk category, validation result, dan user request.

**Penjelasan sederhana:** Label “confidence 0.9” tidak cukup; jelaskan alasan dan alihkan kasus sensitif.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| FastAPI | 0.141.1 | API contract |
| OpenAI Python SDK | 3.15.0 | model adapter |

## Referensi resmi

- [FastAPI response models](https://fastapi.tiangolo.com/tutorial/response-model/)
- [FastAPI streaming](https://fastapi.tiangolo.com/advanced/custom-response/)
- [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses)

## Lanjut ke praktik

Notebook membuat response schema dan renderer yang membedakan answer, citation, dan escalation.

## Posisi part dalam bootcamp

Part ini memindahkan output model ke UI, API, dashboard, atau workflow yang dipakai manusia. Fokusnya adalah contract, status, uncertainty, citation, accessibility, dan action boundary. Jawaban yang benar tetapi tidak dapat dipahami atau tidak dapat ditindaklanjuti tetap gagal sebagai produk.

## Kapan konsep ini dipakai

Gunakan presentation layer ketika output AI akan dibaca, disalin, disetujui, atau memicu tindakan. Pisahkan raw model response dari rendered response. Tampilkan evidence dan status data agar pengguna dapat menilai tingkat kepercayaan.

## Walkthrough terpandu: layar customer support copilot

1. Tentukan state: loading, answered, needs clarification, evidence unavailable, provider error, dan human review.
2. Render answer dengan citation, timestamp, confidence signal yang tidak menyesatkan, dan suggested next action.
3. Tampilkan data order dari tool secara terpisah dari narrative agar angka tidak terlihat seperti opini model.
4. Sediakan feedback: helpful, incorrect, missing evidence, harmful, dengan request_id.
5. Batasi side effect: draft reply boleh dibuat, pengiriman atau refund memerlukan approval.
6. Uji screen reader, long answer, empty evidence, malformed output, dan provider outage.
7. Simpan analytics yang relevan tanpa menyimpan secret atau PII berlebihan.

## Latihan terbimbing

- Buat API response schema untuk answer plus evidence.
- Rancang error message yang dapat ditindaklanjuti.
- Buat approval step untuk action high-impact.
- Tambahkan citation link dan stale data warning.
- Uji dengan persona agent baru dan supervisor.

## Checkpoint penguasaan

Anda siap lanjut jika pengguna tahu apa yang dijawab, dari mana evidence berasal, kapan harus percaya, dan apa tindakan berikutnya.

## Jembatan ke assignment

Assignment harus menghasilkan response/UI contract, example states, implementation atau prototype, accessibility/error checklist, feedback event schema, dan side-effect policy.
