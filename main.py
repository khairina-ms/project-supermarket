from module import *


def supermarket():
    """Fungsi untuk menjalankan program supermarket"""
    print("SELAMAT DATANG DI SUPERMARKET")
    print("-----------------------------")

    # Membuat objek dari kelas Transaksi
    trnsct_123 = Transaction()

    # Menginput ID pelanggan
    id_cust = input('ID transaksi anda: ')
    trnsct_123.id_transaksi(id_cust)

    # Opsi memilih input/edit/hapus/checkout
    while type(id_cust) == str:
        setelah_input = trnsct_123.menu_setelah_input()

        # Menginput item ke keranjang
        while setelah_input == '1':
            nama = input('Masukkan nama item:')
            jumlah = input('Masukkan jumlah item:')
            while type(jumlah) != int:  # Cek agar input integer
                try:
                    jumlah = int(jumlah)
                except ValueError:
                    print("Tolong masukkan integer")
                    jumlah = input('Masukkan jumlah item:')
            harga = input('Masukkan harga item:')
            while type(harga) != int:
                try:
                    harga = int(harga)
                except ValueError:
                    print("Tolong masukkan integer")
                    harga = input('Masukkan harga item:')
                trnsct_123.add_item(nama, int(jumlah), int(harga))
                setelah_input = trnsct_123.menu_setelah_input()
            else:
                continue

        # Mengedit item di keranjang
        while setelah_input == '2':
            if trnsct_123.cek_kosong():  # Keranjang kosong tidak bisa di edit
                setelah_input = trnsct_123.menu_setelah_input()
                continue
            else:
                pilih_update = trnsct_123.menu_pilih_update()

                # Update nama
                while pilih_update == '1':
                    nama_item = input("Item yang akan diganti namanya:")
                    nama_baru = input("Nama baru item: ")
                    trnsct_123.update_item_name(nama_item, nama_baru)
                    pilih_update = trnsct_123.menu_pilih_update()

                # Update jumlah
                while pilih_update == '2':
                    nama_item = input("Item yang akan diganti jumlahnya:")
                    qty_baru = input("Jumlah baru item: ")
                    while type(qty_baru) != int:
                        try:
                            qty_baru = int(qty_baru)
                        except ValueError:
                            print("Tolong masukkan integer")
                            qty_baru = input("Jumlah baru item: ")
                    trnsct_123.update_item_qty(nama_item, qty_baru)
                    pilih_update = trnsct_123.menu_pilih_update()

                # Update harga
                while pilih_update == '3':
                    nama_item = input("Item yang akan diganti harganya:")
                    harga_baru = input("Harga baru item: ")
                    while type(harga_baru) != int:
                        try:
                            harga_baru = int(harga_baru)
                        except ValueError:
                            print("Tolong masukkan integer")
                            harga_baru = input("Harga baru item: ")
                    trnsct_123.update_item_price(nama_item, harga_baru)
                    pilih_update = trnsct_123.menu_pilih_update()

                # Kembali ke menu input/edit/hapus/checkout
                if pilih_update == '4':
                    break
                else:
                    print("Input salah")
                    continue

        # Menghapus item di keranjang
        while setelah_input == '3':
            if trnsct_123.cek_kosong():
                setelah_input = trnsct_123.menu_setelah_input()
                continue
            else:
                pilih_hapus = trnsct_123.menu_pilih_hapus()

                # Menghapus 1 item
                while pilih_hapus == '1':
                    nama_item = input("Nama item yang akan dihapus:")
                    trnsct_123.delete_item(nama_item)
                    pilih_hapus = trnsct_123.menu_pilih_hapus()
                    continue

                # Menghapus seluruh item dalam keranjang
                while pilih_hapus == '2':
                    trnsct_123.reset_transaction()
                    pilih_hapus = trnsct_123.menu_pilih_hapus()
                    continue

                # Kembali ke menu input/edit/hapus/checkout
                if pilih_hapus == '3':
                    break
                else:
                    print("Input salah")
                    continue

        # Memilih check order/checkout
        if setelah_input == '4':
            pengecekan = trnsct_123.check_order()

            # Menghitung total biaya
            if pengecekan:
                hitung = input('Hitung total biaya dan bayar? (y/n)')
                if hitung == 'y':
                    print('Menghitung total biaya')
                    trnsct_123.total_price()
                    return
                elif hitung == 'n':
                    continue
                else:
                    print("Input salah")
                    continue
            else:
                print('Anda harus mengedit keranjang terlebih dahulu')
                continue  # Kembali ke edit nama/qty/harga
        else:
            continue  # Kembali ke input/edit/hapus/checkout


# Menjalankan program supermarket
supermarket()
