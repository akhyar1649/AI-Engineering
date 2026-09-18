# Self-Hosted Infrastructure Setup

**Fase:** 3 — Automation  
**Section:** System Integration & Deployment

> Diverifikasi: Docker Engine v29.6.2 — sumber: https://docs.docker.com/engine/release-notes/29/ — tanggal cek: 2026-09-18
> Diverifikasi: n8n documentation — sumber: https://docs.n8n.io/ — tanggal cek: 2026-09-18

## Tujuan belajar

- menyiapkan VPS/container topology untuk n8n;
- mengamankan reverse proxy, TLS, firewall, user, dan secret;
- memisahkan n8n database, queue, backup, dan execution data;
- menulis provisioning/runbook yang reproducible;
- menguji restore dan upgrade rollback.

## Konteks di PT Kirimin

Pilot automation akan self-hosted agar biaya predictable. Reza meminta setup yang aman, memiliki backup, dan tidak bergantung pada satu laptop engineer.

## Konsep kunci

### Server hardening

**Definisi teknis:** Hardening meliputi minimal OS/user, patching, firewall, SSH policy, TLS, secret management, logging, backup, dan least privilege.

**Penjelasan sederhana:** Pintu depan harus terkunci, kunci tidak dibagikan di grup, dan ada rencana jika gedung rusak.

### Persistent state

**Definisi teknis:** Workflow definitions, credentials, execution history, database, encryption keys, dan volumes memiliki lifecycle/recovery requirement berbeda.

**Penjelasan sederhana:** Menghapus container tidak boleh menghapus buku kerja dan kunci toko tanpa sengaja.

### Upgrade/restore

**Definisi teknis:** Upgrade perlu compatibility check, backup, staging test, migration plan, health verification, and rollback. Restore test membuktikan backup usable.

**Penjelasan sederhana:** Backup yang hanya disimpan tetapi tidak pernah dicoba seperti payung yang tidak pernah dibuka.

## Setup blueprint

Reverse proxy/TLS → n8n → PostgreSQL/Redis → backup object storage. Management access melalui restricted network. Credential values masuk secret store/environment, bukan workflow export.

## Tools & versi

| Tool | Versi/status | Peran |
|---|---:|---|
| Docker Engine | 29.6.2 | container runtime |
| n8n | 2.x; pin image | workflow |
| PostgreSQL | 18.6 | n8n state |

## Referensi resmi

- [n8n hosting](https://docs.n8n.io/hosting/)
- [Docker security](https://docs.docker.com/engine/security/)
- [PostgreSQL backup](https://www.postgresql.org/docs/current/backup.html)

## Lanjut ke praktik

Notebook memvalidasi deployment checklist dan backup/restore state mock.

## Posisi part dalam bootcamp

Part ini mempraktikkan self-hosted workflow secara reproducible. Tujuannya memahami runtime, persistent database, secret, network, upgrade, dan recovery; bukan sekadar berhasil membuka UI.

## Kapan konsep ini dipakai

Gunakan self-hosted bila kontrol data, customization, atau economics membenarkan operational overhead. Jangan memilihnya tanpa owner untuk patching, backup, monitoring, and incident response.

## Walkthrough terpandu: local-to-staging n8n

1. Jalankan n8n dengan Docker Compose dan database persistent.
2. Pisahkan environment variables, secret, encryption key, and public URL.
3. Tambahkan health/readiness, backup volume/database, and log collection.
4. Import workflow versioned dan jalankan fixture.
5. Uji restart, database restore, expired credential, and unavailable downstream.
6. Dokumentasikan upgrade procedure dan schema compatibility.
7. Buat hardening checklist: non-default access, network exposure, least privilege, and data retention.

## Latihan terbimbing

- Buat compose file untuk local.
- Simulasikan volume loss dan restore.
- Uji reverse proxy/TLS boundary secara mock.
- Rotasi credential.
- Buat operator runbook.

## Checkpoint penguasaan

Anda siap lanjut jika environment dapat direproduksi, data persistent dilindungi, secret tidak masuk repository, dan restore pernah diuji.

## Jembatan ke assignment

Assignment harus berisi deployment files, env contract, backup/restore runbook, hardening checklist, smoke test, and limitation note.
