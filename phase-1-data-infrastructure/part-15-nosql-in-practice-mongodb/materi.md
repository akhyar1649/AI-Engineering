# NoSQL in Practice (MongoDB)

**Fase:** 1 — Data Infrastructure  
**Section:** NoSQL & Storage Strategy

> Diverifikasi: MongoDB v8.3 series — sumber: https://www.mongodb.com/docs/manual/release-notes/ — tanggal cek: 2026-09-18
> Diverifikasi: Python v3.14.7 — sumber: https://docs.python.org/3/ — tanggal cek: 2026-09-18

## Tujuan belajar

- membuat document schema untuk tracking event;
- menggunakan CRUD, filter, projection, dan index secara aman;
- merancang idempotent event ingestion;
- menulis aggregation pipeline untuk status terbaru;
- menjelaskan TTL, retention, dan observability.

## Konteks di PT Kirimin

Sari perlu status tracking terakhir dengan latency rendah. Event dapat datang ulang atau terlambat. MongoDB dipakai sebagai contoh document store; keputusan production tetap harus mengikuti workload dan operational readiness.

## Konsep kunci

### Document modeling

**Definisi teknis:** Document menyimpan data berbentuk BSON dengan nested field dan array. Embed cocok untuk data bounded yang dibaca bersama; reference cocok untuk data besar/berubah atau relasi yang dibaca terpisah.

**Penjelasan sederhana:** Informasi yang selalu dibutuhkan bersama bisa berada dalam satu map; daftar event tak terbatas sebaiknya tidak terus dimasukkan ke satu map.

### Index

**Definisi teknis:** Index mempercepat query tertentu dengan biaya write, storage, dan memory. Index harus dirancang berdasarkan filter/sort dan diverifikasi dengan query explain.

**Penjelasan sederhana:** Daftar isi mempercepat pencarian, tetapi membuat buku lebih besar dan harus diperbarui ketika isi berubah.

### Idempotent ingestion

**Definisi teknis:** Ingestion idempotent menggunakan unique event identifier atau compound key sehingga retry tidak membuat semantic duplicate. Upsert harus memiliki predicate yang tepat.

**Penjelasan sederhana:** Kurir yang mengulang laporan event yang sama tidak boleh membuat sistem mengira ada dua kejadian.

## Contoh document

```json
{
  "shipment_id": "S-1001",
  "event_id": "E-1001-03",
  "status": "in_transit",
  "event_time": "2026-09-18T10:00:00+07:00",
  "hub_code": "JKT-01",
  "source": "courier-api"
}
```

Index utama dapat berupa `{shipment_id: 1, event_time: -1}`; unique event key dipilih sesuai contract sumber.

## Tools & versi

| Tool | Versi | Peran |
|---|---:|---|
| MongoDB | 8.3 series | document store |
| Python | 3.14.7 | local mock/client runtime |

## Referensi resmi

- [MongoDB CRUD](https://www.mongodb.com/docs/manual/crud/)
- [MongoDB indexes](https://www.mongodb.com/docs/manual/indexes/)
- [MongoDB aggregation](https://www.mongodb.com/docs/manual/aggregation/)

## Lanjut ke praktik

Notebook memakai in-memory mock yang meniru insert, dedupe, dan latest status. Assignment meminta implementasi yang dapat dipindah ke MongoDB lokal.

## Posisi part dalam bootcamp

Part ini menguji keputusan NoSQL pada database nyata/lokal, bukan hanya diagram. Anda akan membuat collection, index, query, dan failure handling untuk timeline shipment. Hasilnya dibandingkan dengan kebutuhan pipeline dan serving dari part sebelumnya.

## Kapan konsep ini dipakai

Gunakan MongoDB ketika document aggregate dan access pattern shipment timeline lebih dominan daripada join lintas banyak entitas. Gunakan relational serving untuk metric rekonsiliasi yang memerlukan constraint dan agregasi lintas fakta. Satu organisasi boleh memakai keduanya, tetapi contract dan ownership harus jelas.

## Walkthrough terpandu: MongoDB shipment timeline

1. Buat database lokal atau mock adapter dengan collection shipments. Setiap document memiliki order_id, city, events, schema_version, dan updated_at.
2. Insert satu order dengan beberapa event. Query seluruh timeline dan latest event tanpa membaca dokumen order lain.
3. Tambahkan unique index untuk idempotency key event_id atau kombinasi order_id dan event_id.
4. Simulasikan retry insert. Pastikan duplicate terdeteksi atau menjadi no-op yang aman.
5. Simulasikan event terlambat. Jangan hanya memakai urutan kedatangan; gunakan event_at dan aturan tie-breaker.
6. Buat query backlog per kota dan bandingkan hasilnya dengan relational expected result. Jelaskan kapan aggregation pipeline menjadi mahal.
7. Tambahkan schema validation, explain query, backup/restore note, dan retention strategy.

## Latihan terbimbing

- Bandingkan embedded events dengan collection terpisah.
- Uji query tanpa index dan dengan index.
- Buat migration saat schema_version berubah.
- Tangani document rusak tanpa menghentikan seluruh batch.
- Tulis contract untuk adapter mock agar dapat diganti MongoDB.

## Checkpoint penguasaan

Anda siap lanjut jika dapat melakukan read/write/query/retry, membuktikan idempotence, membaca explain sederhana, dan mengakui batasan local/mock mode.

## Jembatan ke assignment

Assignment harus menyertakan seed script, schema/index, query examples, failure tests, expected outputs, dan note tentang perbedaan local mock dengan MongoDB deployment.
