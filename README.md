# Project Cashier System Supermarket
Program kasir sederhana dengan menggunakan bahasa pemrograman Python.
## Latar Belakang
Kasir adalah perangkat yang biasanya digunakan bisnis untuk menghitung transaksi keuangan. Pembuatan kasir self-service dapat mempermudah bisnis seperti Supermarket dengan memperbolehkan customer langsung memasukkan nama item, jumlah item, dan harga item yang dibeli.
## Requirements
### Functions
Program memiliki fitur untuk:
- Membuat ID transaksi
- Memasukkan nama, jumlah, dan harga item
- Memperbaiki nama, jumlah, dan harga item yang sudah di-input.
- Menghapus satu item dari daftar input
- Menghapus semua item dari daftar input
- Mengecek pesanan
- Menghitung total harga dengan ketentuan diskon yang diberikan

### Flowchart

## Methods Description
Berikut merupakan metode-metode dari kelas Transaksi dari modul program beserta penjelasannya:
|No| Metode | Penjelasan |
|---|---|---|
|1| id_transaksi(id_cust): | Memasukkan ID pelanggan |
|2| add_item(nama, jumlah, harga): | Memasukkan nama, jumlah, dan harga item ke list pada objek. |
|3|update_item_name(nama_item, nama_baru)|Mengubah nama item|
|4|update_item_qty(nama_item, qty_baru)|Mengubah jumlah item|
|5|update_item_price(nama_item, harga_baru)|Mengubah jumlah item|
|6|delete_item(nama_item)|Menghapus satu item|
|7|reset_transaction()|Menghapus semua item di keranjang|
|8|check_order()|Memastikan format input order sudah benar|
|9|total_price()|Menghitung harga total dari belanja|
|10|print_order()|Mengembalikan tabel isi keranjang pembelian|
|11|cek_kosong()|Memastikan keranjang tidak kosong|
|12|menu_setelah_input()|Menu memilih input/edit/hapus/checkout|
|13|menu_pilih_update()|Menu memilih update nama/jumlah/harga/kembali ke menu sebelumnya|
|14|menu_pilih_hapus()|Menu memilih menghapus satu/seluruh item/kembali ke menu sebelumnya|

## Hasil Test Case
---
- Hasil input ID
- Hasil menambahkan item
- Hasil menghapus satu item
- Hasil menghapus semua item
- Hasil menghitung belanja
