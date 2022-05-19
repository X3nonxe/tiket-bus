from db import *

class User:
   # Attributes
   def __init__(self, id_user, username, password):
      self.id_user = id_user
      self.username = username
      self.password = password

   # Methods
   def beli_tiket(self):
      # Mengambil semua data dari tabel jadwal
      cursor.execute("SELECT * FROM jadwal")
      data = cursor.fetchall()
      for row in data:
         print("ID Jadwal:", row[0])
         print("Kode Bis:", row[1])
         print("Tujuan:", row[2])
         print("Tanggal Berangkat:", row[2])
         print("")

      inp_id_jadwal = input("Pilih ID Jadwal: ")
      cursor.execute("SELECT kode_bis FROM jadwal WHERE id_jadwal = %s", (inp_id_jadwal,))
      data2 = cursor.fetchall()

      for row in data2:
         inp_kode_pesanan = input("Masukkan Kode Pesanan: ")
         inp_harga = input("Masukkan Harga Tiket: ")
         inp_tgl_pesanan = input("Masukkan Tanggal Pemesanan: ")

         # Simpan Data Tiket
         cursor.execute("INSERT INTO pemesanan(kode_pesanan, kode_bis, id_jadwal, harga, tgl_pesanan) VALUES (%s, %s, %s, %s, %s)", (inp_kode_pesanan, row[0], inp_id_jadwal, inp_harga, inp_tgl_pesanan))
         db.commit()
         print("Tiket berhasil dibeli")
