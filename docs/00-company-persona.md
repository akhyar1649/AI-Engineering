# Persona Perusahaan: PT Kirimin Digital Nusantara

## Ringkasan

PT Kirimin Digital Nusantara adalah scale-up beranggotakan sekitar 150 orang yang mengoperasikan Kirimin, platform on-demand logistics dan fulfillment untuk UMKM di Indonesia. Kirimin menggabungkan layanan pengiriman, warehousing, dan marketplace kecil. Perusahaan beroperasi di lebih dari 20 kota dan memproses puluhan ribu order per hari.

Benang merah bootcamp adalah perjalanan memperbaiki operasi Kirimin dari data mentah menjadi sistem yang dapat dianalisis, dibantu AI, dan diotomatisasi. Peserta bekerja sebagai engineer yang harus menjelaskan trade-off kepada stakeholder, bukan sekadar menulis kode.

## Stakeholder fiktif

| Nama | Peran | Kebutuhan utama |
|---|---|---|
| Dinda | Head of Data | trusted data, lineage, reliability, dan governance |
| Reza | CTO | arsitektur yang aman, dapat dirawat, dan masuk akal secara biaya |
| Fajar | Head of Customer Support | jawaban SOP yang cepat, akurat, dan dapat diaudit |
| Sari | Ops Lead | status order yang konsisten dan workflow tanpa pekerjaan manual berulang |

## Masalah bisnis lintas fase

1. Data order, shipment, inventori, dan komplain tersebar di banyak sistem.
2. Tim customer support menjawab pertanyaan repetitif tetapi harus tetap mengikuti SOP internal.
3. Update status kirim, notifikasi pelanggan, dan rekonsiliasi keuangan kurir masih dikerjakan lintas tool secara manual.

## Skema data inti

Skema berikut adalah kontrak konseptual. Kolom dapat bertambah dalam latihan untuk meniru schema evolution.

### `orders`

| Kolom | Tipe konseptual | Keterangan |
|---|---|---|
| `order_id` | string | identifier order unik; retry sistem dapat membuat duplikasi mentah |
| `customer_id` | string | identifier pelanggan sintetis |
| `merchant_id` | string | identifier UMKM sintetis |
| `order_created_at` | timestamp | waktu order dibuat; format mentah dapat bervariasi |
| `origin_city` | string | kota asal, misalnya `Jakarta`, `JKT`, atau `jakarta` |
| `destination_city` | string | kota tujuan |
| `order_value_idr` | numeric | nilai order; dapat memiliki outlier |
| `payment_status` | string | `paid`, `pending`, `refunded`, atau nilai tidak dikenal |
| `channel` | string | `web`, `mobile`, `marketplace`, atau `partner_api` |

### `shipments`

| Kolom | Tipe konseptual | Keterangan |
|---|---|---|
| `shipment_id` | string | identifier pengiriman |
| `order_id` | string | relasi ke order |
| `courier_id` | string | relasi ke kurir |
| `status` | string | `created`, `picked_up`, `in_transit`, `delivered`, `failed` |
| `event_time` | timestamp | waktu event tracking; dapat out-of-order |
| `hub_code` | string | kode hub atau warehouse |
| `delivery_attempt` | integer | jumlah percobaan pengantaran |
| `last_updated_at` | timestamp | waktu update terakhir |

### `inventory`

| Kolom | Tipe konseptual | Keterangan |
|---|---|---|
| `sku` | string | identifier produk |
| `warehouse_id` | string | relasi ke warehouse |
| `stock_on_hand` | integer | stok fisik tercatat |
| `reserved_qty` | integer | stok yang sudah dipesan |
| `updated_at` | timestamp | waktu snapshot |
| `batch_code` | string | batch inventori, dapat kosong pada data lama |

### `customer_tickets`

| Kolom | Tipe konseptual | Keterangan |
|---|---|---|
| `ticket_id` | string | identifier tiket |
| `customer_id` | string | relasi pelanggan |
| `order_id` | string | dapat kosong jika pertanyaan umum |
| `category` | string | kategori komplain atau pertanyaan |
| `message` | text | pesan pelanggan |
| `priority` | string | `low`, `normal`, `high`, `urgent` |
| `created_at` | timestamp | waktu tiket dibuat |
| `resolved_at` | timestamp nullable | waktu penyelesaian |

### `couriers`

| Kolom | Tipe konseptual | Keterangan |
|---|---|---|
| `courier_id` | string | identifier kurir |
| `courier_name` | string | nama sintetis |
| `service_area` | string | area operasi |
| `contract_type` | string | `fleet`, `partner`, atau `temporary` |
| `active` | boolean | status keaktifan |

### `warehouses`

| Kolom | Tipe konseptual | Keterangan |
|---|---|---|
| `warehouse_id` | string | identifier warehouse |
| `warehouse_name` | string | nama fasilitas sintetis |
| `city` | string | kota |
| `capacity_units` | integer | kapasitas unit |
| `manager` | string | nama stakeholder sintetis |

## Aturan dataset latihan

Dataset dibuat secara sintetis dengan seed yang terdokumentasi. Kecuali sebuah part secara eksplisit memerlukan data bersih, dataset harus dapat memuat missing value, duplicate record akibat retry, variasi format tanggal, variasi penulisan kota, outlier nilai, timestamp yang salah urutan, dan kolom baru pada periode tertentu. Ukuran dataset disesuaikan dengan tujuan part; contoh kecil harus tetap dipakai untuk menjelaskan konsep sebelum skala diperbesar.

Data pribadi nyata, token, email operasional nyata, dan data pelanggan asli tidak boleh digunakan. Identifier pelanggan dan nama stakeholder hanyalah data fiktif.

## Narasi perkembangan sistem

- **Fase 1:** Dinda meminta pipeline terpercaya untuk menyatukan data operasional dan membuat metrik yang dapat dipakai Ops.
- **Fase 2:** Fajar meminta assistant berbasis SOP yang dapat menyebutkan sumber jawaban dan menghindari halusinasi.
- **Fase 3:** Sari meminta workflow yang menghubungkan event operasional, database, notifikasi, dan langkah AI dengan reliability yang jelas.
- **Final project:** peserta memilih solusi data+AI atau data+automation dan menyusun rencana layaknya engagement konsultasi untuk Kirimin.
