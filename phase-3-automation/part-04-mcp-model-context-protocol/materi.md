# MCP (Model Context Protocol)

**Fase:** 3 — Automation  
**Section:** Automation & n8n Foundations

> Diverifikasi: Model Context Protocol specification — sumber: https://modelcontextprotocol.io/specification/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menjelaskan host, client, server, tools, resources, dan prompts dalam MCP;
- membedakan tool invocation dari data retrieval biasa;
- merancang auth, consent, capability, dan audit boundary;
- menghubungkan MCP concept dengan workflow automation;
- mengenali tool poisoning dan over-privileged integration.

## Konteks di PT Kirimin

Assistant atau workflow dapat membutuhkan akses standar ke shipment status. MCP memberi protocol boundary, tetapi tidak otomatis membuat tool aman; Sari tetap harus mengontrol capability dan approval.

## Konsep kunci

### MCP architecture

**Definisi teknis:** MCP memisahkan host yang mengorkestrasi AI/app, client yang mempertahankan connection, dan server yang mengekspos tools/resources/prompts melalui protocol.

**Penjelasan sederhana:** Host adalah supervisor, client adalah telepon, server adalah departemen yang menawarkan layanan tertentu.

### Tool versus resource

**Definisi teknis:** Tool adalah callable action dengan side effect/policy; resource adalah context/data yang dapat dibaca. Capability negotiation dan schema membantu interoperability.

**Penjelasan sederhana:** Membaca daftar SOP berbeda dengan menekan tombol update status.

### Consent dan security

**Definisi teknis:** MCP integration membutuhkan explicit user/model authorization, scoped credentials, input validation, output sanitization, audit log, and confirmation for risky action.

**Penjelasan sederhana:** Menyambungkan departemen tidak berarti semua orang boleh mengambil semua tindakan.

## MCP workflow pattern

`discover capability → validate schema → request consent if risky → call tool → validate result → audit`. Jangan meneruskan arbitrary tool result ke action node tanpa policy.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| MCP specification | current spec; pin SDK/server at implementation | tool/context interoperability |
| n8n | 2.x | workflow integration |

## Referensi resmi

- [MCP specification](https://modelcontextprotocol.io/specification/)
- [MCP concepts](https://modelcontextprotocol.io/docs/concepts/architecture)
- [n8n documentation](https://docs.n8n.io/)

## Lanjut ke praktik

Notebook membuat capability registry dan risk check sebelum tool call.

## Posisi part dalam bootcamp

Part ini memperkenalkan MCP sebagai contract untuk mengekspos tools/resources ke model atau client. Anda menghubungkan agent skill Fase 2 dengan workflow automation Fase 3 tanpa memberikan akses yang terlalu luas.

## Kapan konsep ini dipakai

Gunakan MCP ketika beberapa client membutuhkan interface tools/resources yang konsisten. Gunakan REST atau internal library jika hanya ada satu consumer dan contract tersebut sudah cukup. MCP bukan pengganti permission model, validation, atau audit.

## Walkthrough terpandu: read-only shipment tools

1. Definisikan tool get_order_status dengan input order_id dan output schema yang ketat.
2. Definisikan resource metric_definition untuk menjelaskan backlog dan SLA.
3. Tambahkan permission, timeout, rate limit, correlation_id, dan audit event.
4. Validasi input terhadap allowlist dan baca data melalui service read-only.
5. Uji tool result normal, not found, stale, timeout, dan unauthorized.
6. Hubungkan tool ke agent dengan max-step dan approval boundary.
7. Dokumentasikan versioning contract dan compatibility policy.

## Latihan terbimbing

- Buat mock MCP server/client atau adapter contract.
- Bandingkan tool result text versus structured content.
- Uji prompt injection di data resource.
- Tambahkan redaction.
- Buat contract test untuk breaking change.

## Checkpoint penguasaan

Anda siap lanjut jika tool contract, permission, error, audit, dan versioning jelas serta client tidak dapat melakukan side effect tanpa kontrol.

## Jembatan ke assignment

Assignment harus mengumpulkan MCP/adapter implementation, schemas, tests, security note, sample traces, dan client usage example.
