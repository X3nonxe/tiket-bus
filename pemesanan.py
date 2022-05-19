from jadwal import Jadwal
from bis import Bis
from db import *

class Pemesanan(Jadwal):
   def __init__(self, kode_pesanan, harga, tgl_pesanan, id_jadwal, tujuan, tgl_berangkat, id_bis, kode_bis, plat_bis):
      super().__init__(id_jadwal, tujuan, tgl_berangkat, id_bis, kode_bis, plat_bis)
      self.kode_pesanan = kode_pesanan
      self.harga = harga
      self.tgl_pesanan = tgl_pesanan

   def cetak(self):
      # mengambil semua data dari tabel pemesanan
      cursor.execute("SELECT * FROM pemesanan")
      data = cursor.fetchall()

      # mencetak/menampilkan data
      print("==CETAK PEMESANAN==")
      for row in data:
         print("Kode Pesanan:", row[0])
         print("Kode Bis: ", row[1])
         print("ID Jadwal: ", row[2])
         print("Harga Tiket: ", row[3])
         print("Tanggal Pemesanan: ", row[4])

   def batalkan(self):
      kode_pesanan = input("Masukkan kode pesanan: ")
      cursor.execute("DELETE FROM pemesanan WHERE kode_pesanan = %s", (kode_pesanan,))
      db.commit()
      print("Pemesanan berhasil dibatalkan")

