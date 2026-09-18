# Integration Readiness & System Compatibility

**Fase:** 3 — Automation  
**Section:** AI-Driven Automation & Solution Design

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18
> Diverifikasi: PostgreSQL v18.6 — sumber: https://www.postgresql.org/docs/release/ — tanggal cek: 2026-09-18
> Diverifikasi: Model Context Protocol specification — sumber: https://modelcontextprotocol.io/specification/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menilai API/schema/auth/rate limit/webhook readiness;
- menemukan compatibility gap dan dependency risk;
- merancang adapter, mapping, contract test, dan migration;
- menyusun integration readiness scorecard;
- membuat go/no-go recommendation.

## Konteks di PT Kirimin

Partner courier memiliki API berbeda, satu hanya mendukung polling, dan satu belum memiliki idempotency field. Workflow tidak boleh dianggap siap hanya karena credentials tersedia.

## Konsep kunci

### Integration readiness

**Definisi teknis:** Readiness meliputi API contract, auth, environment, data quality, rate limit, webhook/retry semantics, observability, support owner, test sandbox, and legal/privacy.

**Penjelasan sederhana:** Memiliki nomor telepon tidak berarti dua tim siap bekerja; mereka juga perlu bahasa, jam kerja, dan cara menangani salah sambung.

### Compatibility

**Definisi teknis:** Compatibility mencakup schema, semantics, protocol, version, performance, auth, and failure behavior. Adapter mengisolasi perbedaan vendor.

**Penjelasan sederhana:** Dua colokan sama-sama listrik tetapi bentuk dan voltasenya bisa berbeda; adapter dan pemeriksaan diperlukan.

### Contract test

**Definisi teknis:** Contract test memverifikasi producer/consumer agreement pada sample and edge cases tanpa harus menjalankan seluruh production system.

**Penjelasan sederhana:** Sebelum conveyor disambung, coba sambungkan dua ujung dengan paket contoh.

## Readiness scorecard

Status `ready`, `conditional`, atau `blocked` harus memiliki evidence dan owner. Blocker seperti auth belum aman, no retry/idempotency, atau PII contract tidak jelas tidak boleh disembunyikan oleh score rata-rata.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | integration runtime |
| PostgreSQL | 18.6 | data contract example |
| MCP | current specification | capability boundary |

## Referensi resmi

- [n8n integrations](https://docs.n8n.io/integrations/)
- [PostgreSQL protocol/client docs](https://www.postgresql.org/docs/current/protocol.html)
- [MCP specification](https://modelcontextprotocol.io/specification/)

## Lanjut ke praktik

Notebook menghitung readiness dengan blocker override.

## Posisi part dalam bootcamp

Part ini menutup Fase 3 dengan kesiapan integrasi. Anda akan membuktikan bahwa partner/API/source dapat dihubungkan secara aman dan dapat dipelihara, bukan hanya bahwa satu request berhasil di sandbox.

## Kapan konsep ini dipakai

Gunakan integration readiness review sebelum pilot atau production connection. Periksa schema, authentication, rate limit, webhook semantics, retry, idempotency, error, observability, data protection, support, and change notification.

## Walkthrough terpandu: memilih courier partner

1. Minta evidence kontrak dan sandbox untuk tiga partner sintetis.
2. Buat scorecard dengan status verified, partial, unknown, blocker, owner, and due date.
3. Uji normal, missing field, enum drift, invalid signature, timeout, 429, 5xx, duplicate, and out-of-order event.
4. Buat adapter yang memetakan partner payload ke canonical shipment event.
5. Jalankan contract tests pada fixture versioned.
6. Nilai operational readiness: docs, support, SLA, alert, replay, and rollback.
7. Tulis go/no-go recommendation dan remediation plan dengan exit criteria.

## Latihan terbimbing

- Buat canonical schema dan mapping table.
- Tambahkan consumer-driven contract test.
- Simulasikan partner schema version change.
- Hitung rate-limit capacity.
- Buat pilot checklist dan rollback.

## Checkpoint penguasaan

Anda siap menyelesaikan Capstone 3 jika dapat menunjukkan evidence readiness, adapter behavior, failure handling, contract tests, dan keputusan pilot yang dapat diaudit.

## Jembatan ke assignment

Assignment harus mengumpulkan readiness scorecard, adapter, contract tests, integration review, remediation plan, go/no-go, dan limitation note.
