# Troubleshooting Automation and Governance

**Fase:** 3 — Automation  
**Section:** AI-Driven Automation & Solution Design

> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18
> Diverifikasi: Model Context Protocol specification — sumber: https://modelcontextprotocol.io/specification/ — tanggal cek: 2026-09-18

## Tujuan belajar

- mengklasifikasikan failure workflow dan governance failure;
- membaca execution trace, DLQ, audit, dan provider logs;
- menyiapkan mitigation, replay, rollback, dan kill switch;
- merancang access/approval/change control;
- menulis postmortem dan corrective action.

## Konteks di PT Kirimin

Satu workflow mengirim notifikasi dua kali dan satu MCP tool muncul dengan scope terlalu luas. Anda perlu menangani incident teknis dan governance secara bersamaan.

## Konsep kunci

### Technical versus governance incident

**Definisi teknis:** Technical incident mengganggu availability/correctness; governance incident melanggar policy, access, consent, retention, atau audit. Keduanya dapat terjadi bersamaan.

**Penjelasan sederhana:** Mesin bisa macet, tetapi mesin juga bisa bekerja melakukan hal yang tidak boleh.

### Replay safety

**Definisi teknis:** Replay mengulang processing dari durable input dengan mode dry-run, idempotency, side-effect suppression, dan approval. Raw input harus immutable.

**Penjelasan sederhana:** Memutar ulang resep tidak berarti mengirim ulang paket ke customer.

### Change governance

**Definisi teknis:** Workflow change harus memiliki owner, review, test evidence, version, rollout, rollback, and access audit. Emergency change tetap perlu retrospective review.

**Penjelasan sederhana:** Perubahan darurat boleh dilakukan, tetapi tetap harus dicatat dan diperiksa setelah keadaan tenang.

## Incident flow

`contain → preserve evidence → assess impact → disable unsafe route → recover safely → verify → communicate → prevent recurrence`.

## Tools & versi

| Tool | Status | Peran |
|---|---:|---|
| n8n | 2.x; pin release | execution/replay |
| MCP | current specification | capability governance |

## Referensi resmi

- [n8n error handling](https://docs.n8n.io/flow-logic/error-handling/)
- [n8n source control](https://docs.n8n.io/source-control-environments/)
- [MCP specification](https://modelcontextprotocol.io/specification/)

## Lanjut ke praktik

Notebook mengklasifikasikan incident dan memilih containment action.

## Posisi part dalam bootcamp

Part ini menyatukan troubleshooting, governance, dan operational ownership. Anda akan menangani workflow yang salah, credential bocor, duplicate side effect, stale data, dan perubahan policy secara terstruktur.

## Kapan konsep ini dipakai

Gunakan incident process untuk failure technical maupun business. Gunakan change governance ketika workflow, credential, schema, model, atau recipient berubah. Semua change harus memiliki test, reviewer, rollout, and rollback.

## Walkthrough terpandu: duplicate notification incident

1. Nyatakan customer impact, period, workflow version, and affected count.
2. Cari correlation_id/event_id di ledger dan execution trace.
3. Hentikan side effect dengan kill switch atau disable path.
4. Temukan apakah duplicate berasal dari trigger, retry, missing idempotency, atau provider acknowledgment.
5. Mitigasi dan komunikasi stakeholder dengan fakta.
6. Tambahkan idempotency/ledger/regression control, lalu replay hanya event yang valid.
7. Tulis postmortem dan update risk register, runbook, and owner.

## Latihan terbimbing

- Buat incident severity matrix.
- Simulasikan leaked credential response.
- Tambahkan approval untuk recipient change.
- Buat change request template.
- Uji rollback workflow version.

## Checkpoint penguasaan

Anda siap lanjut jika dapat containment cepat, evidence preserving, safe recovery, dan prevention yang bisa diuji.

## Jembatan ke assignment

Assignment harus berisi taxonomy, incident timeline, runbook, governance checklist, change record, postmortem, regression test, and ownership.
