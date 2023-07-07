"""Modul ini untuk menjalankan transaksi Supermarket"""

import pandas as pd
import numpy as np


class Transaction:
    """Berisi metode yang digunakan dalam menjalankan program supermarket"""

    def __init__(self):
        """Metode untuk keterangan item dan pelanggan"""
        self.nama_item = list()
        self.jumlah_item = list()
        self.harga_per_item = list()
        self.id_pelanggan = list()

    def id_transaksi(self, id_cust):
        """Memasukkan ID pelanggan"""
        print("-----------------------------")
        self.id_pelanggan.append(id_cust)
        print(f'Selamat berbelanja, pelanggan {id_cust}!')

    def add_item(self, nama, jumlah, harga):
        """
        Memasukkan nama, jumlah, dan harga item ke list pada objek.
        Mengembalikan bool

        Parameters:
            nama(any): Nama dari item yang diinput
            jumlah(int): Jumlah dari item yang diinput
            harga(int): Harga dari item yang diinput

        Returns:
            bool
        """
        print("-----------------------------")
        self.nama_item.append(nama)
        self.jumlah_item.append(jumlah)
        self.harga_per_item.append(harga)
        print(f'Item {nama} berhasil ditambahkan!')
        self.print_order()
        return True

    def update_item_name(self, nama_item, nama_baru):
        """
        Mengubah nama item

        Parameters:
            nama_item(any): Nama sekarang dari item yang akan diganti
            nama_baru(any): Nama baru item yang akan diganti

        Returns:
            bool
        """
        print("-----------------------------")
        if nama_item not in self.nama_item:
            print("Nama item tidak ditemukan")
            return True
        else:
            self.nama_item[self.nama_item.index(nama_item)] = nama_baru
            print('Nama item berhasil di update!')
            self.print_order()
            return False

    def update_item_qty(self, nama_item, qty_baru):
        """
        Mengubah jumlah item

        Parameters:
            nama_item(any): Nama dari item yang jumlahnya akan diganti
            qty_baru(int): Jumlah baru item

        Returns:
            bool
        """
        print("-----------------------------")
        if nama_item not in self.nama_item:
            print("Nama item tidak ditemukan")
            return True
        else:
            self.jumlah_item[self.nama_item.index(nama_item)] = qty_baru
            print('Jumlah item berhasil di update!')
            self.print_order()

    def update_item_price(self, nama_item, harga_baru):
        """
        Mengubah jumlah item

        Parameters:
            nama_item(any): Nama dari item yang harganya akan diganti
            harga_baru(int): Harga baru item

        Returns:
            bool
        """
        print("-----------------------------")
        if nama_item not in self.nama_item:
            print("Nama item tidak ditemukan")
            return True
        else:
            self.harga_per_item[self.nama_item.index(nama_item)] = harga_baru
            print('Harga item berhasil di update!')
            self.print_order()

    def delete_item(self, nama_item):
        """
        Menghapus satu item

        Parameters:
            nama_item(any): Nama dari item yang akan dihapus

        Returns:
            bool
        """
        print("-----------------------------")
        if nama_item not in self.nama_item:
            print("Nama item tidak ditemukan")
            return True
        else:
            index_delete = self.nama_item.index(nama_item)
            del self.nama_item[index_delete]
            del self.jumlah_item[index_delete]
            del self.harga_per_item[index_delete]
            print(f'Item {nama_item} berhasil di hapus!')
            self.print_order()

    def reset_transaction(self):
        """Menghapus semua item di keranjang"""
        print("-----------------------------")
        self.nama_item.clear()
        self.jumlah_item.clear()
        self.harga_per_item.clear()
        print('Keranjang belanja berhasil dikosongkan!')
        self.print_order()

    def check_order(self):
        """
        Memastikan format input order sudah benar

        Returns:
            bool
        """
        print("-----------------------------")
        self.print_order()
        semua_value = self.nama_item + self.jumlah_item + self.harga_per_item
        if '' in semua_value:
            print('Terdapat kesalahan input data')
            return False
        else:
            print('Pemesanan sudah benar')
            return True

    def total_price(self):
        """Menghitung harga total dari belanja"""
        print("-----------------------------")
        data_frame = self.print_order()
        total = data_frame['Total Harga'].sum()
        print(f'Total belanja sebelum diskon Anda adalah: {total}')
        if total > 500_000:
            diskon = 0.1
        elif total > 300_000:
            diskon = 0.08
        elif total > 200_000:
            diskon = 0.05
        else:
            diskon = 0
        total = total - (diskon*total)
        print(f'Anda mendapatkan diskon {"{:.0%}".format(diskon)}')
        print(f'Total belanja sesudah diskon Anda adalah: {total}')
        print(f'Terima kasih sudah berbelanja pelanggan {self.id_pelanggan}!')

    def print_order(self):
        """
        Mengembalikan tabel isi keranjang pembelian

        Returns:
            pandas DataFrame
        """
        tabel = {'Nama Item': self.nama_item, 'Jumlah Item': self.jumlah_item,
                 'Harga Item': self.harga_per_item,
                 'Total Harga': np.array(self.jumlah_item) * np.array(self.harga_per_item)}
        data_frame = pd.DataFrame(tabel)
        print(data_frame)
        return data_frame

    def cek_kosong(self):
        """
        Memastikan keranjang tidak kosong

        Returns:
            bool
        """
        semua_value = self.nama_item + self.jumlah_item + self.harga_per_item
        if len(semua_value) == 0:
            print('Keranjang masih kosong')
            return True
        else:
            return False

    def menu_setelah_input(self):
        """Menu memilih input/edit/hapus/checkout"""
        print('-----------------------------')
        print('Ketikkan angka pilihan:')
        print('1. Input item baru')
        print('2. Edit item di keranjang')
        print('3. Hapus item di keranjang')
        print('4. Check order/checkout')
        return input('Pilihan:')

    def menu_pilih_update(self):
        """Menu memilih update nama/jumlah/harga/kembali ke menu sebelumnya"""
        print('-----------------------------')
        print('Ketikkan angka pilihan:')
        print('1. Update nama item')
        print('2. Update jumlah item')
        print('3. Update harga item')
        print('4. Kembali ke menu sebelumnya')
        return input('Pilihan:')

    def menu_pilih_hapus(self):
        """Menu memilih menghapus satu/seluruh item/kembali ke menu sebelumnya"""
        print('-----------------------------')
        print('Ketikkan angka pilihan:')
        print('1. Hapus satu item')
        print('2. Hapus seluruh keranjang belanja')
        print('3. Kembali ke menu sebelumnya')
        return input('Pilihan:')
