from bis import Bis
from db import *

class Jadwal(Bis):
   # Atribut yang dibutuhkan:
   def __init__(self, id_jadwal: int, kode_bis: str, tujuan: str, tgl_berangkat: str, id_bis: int, plat_bis: str):
      super().__init__(id_bis, kode_bis, plat_bis)
      self.id_jadwal = id_jadwal
      self.tujuan = tujuan
      self.tgl_berangkat = tgl_berangkat

   # Method yang dibutuhkan:
   def lihat_jadwal(self):
      # mengambil semua data dari tabel jadwal
      cursor.execute("SELECT * FROM jadwal")
      data = cursor.fetchall()

      # Tampilan jadwal
      print("=== JADWAL ===")
      for row in data:
         print("ID Jadwal:", row[0])
         print("Kode Bis:", row[1])
         print("Tujuan:", row[2])
         print("Tanggal Berangkat:", row[3])
         print("")

   def tambah_jadwal(self):
      # Input user untuk menambah jadwal
      inp_id_jadwal = input("Masukkan ID Jadwal: ")
      inp_kode_bis = input("Masukkan Kode Bis: ")
      inp_tujuan = input("Masukkan Tujuan: ")
      inp_tgl_berangkat = input("Masukkan Tanggal Berangkat: ")

      # run query
      cursor.execute("INSERT INTO jadwal (id_jadwal, kode_bis, tujuan, tgl_berangkat) VALUES (%s, %s, %s, %s)", (inp_id_jadwal, inp_kode_bis, inp_tujuan, inp_tgl_berangkat))
      db.commit()
      print("Jadwal berhasil ditambahkan")

   def edit_jadwal(self):
      # input ID Lama
      inp_id_jadwal_lama = input("Masukan ID jadwal lama: ")
      # input data Baru
      inp_id_jadwal_baru = input("Masukan ID jadwal baru: ")
      inp_kode_bis = input("Masukan kode bis baru: ")
      inp_tujuan = input("Masukan Tujuan baru: ")
      inp_tgl_berangkat = input("Masukan tanggal keberangkatan: ")

      # run Query
      cursor.execute("UPDATE jadwal SET id_jadwal = %s, kode_bis = %s, tujuan = %s, tgl_berangkat = %s WHERE id_jadwal = %s", (inp_id_jadwal_baru, inp_kode_bis, inp_tujuan, inp_tgl_berangkat, inp_id_jadwal_lama))
      db.commit()
      print("Jadwal berhasil diedit")

   def hapus_jadwal(self):
      #input ID jadwal 
      inp_id_jadwal = input("Masukan ID jadwal: ")

      #run query
      cursor.execute("DELETE FROM jadwal WHERE id_jadwal = %s", (inp_id_jadwal))
      db.commit()
      print("Jadwal berhasil dihapus")
