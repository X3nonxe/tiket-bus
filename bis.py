from db import *

class Bis:
   def __init__(self, id_bis: int, kode_bis: str, plat_bis: str):
      self.id_bis = id_bis
      self.kode_bis = kode_bis
      self.plat_bis = plat_bis

   def pemberangkatan(self):
      # Mengambil semua data dari tabel bis
      cursor.execute("SELECT * FROM bis")
      data = cursor.fetchall()

      # Menampilkan data
      print("==PEMBERANGKATAN BIS==")
      for row in data:
         print("ID Bis:", row[0])
         print("Kode Bis:", row[1])
         print("Plat Bis:", row[2])
         print("")
      
   def tambahdatabis(self):
      # Input untuk menambahkan bis
      inp_id_bis = input("Masukan ID Bis: ")
      inp_kode_bis = input("Masukan kode Bis: ")
      inp_plat_bis = input("Masukan plat Bis: ")

      # Menjalankan Query
      cursor.execute("INSERT INTO bis(id_bis, kode_bis, plat_bis) VALUES (%s, %s, %s)", (inp_id_bis, inp_kode_bis, inp_plat_bis))
      db.commit()
      print("Bis berhasil ditambahkan")

   def editdatabis(self):
      # Input Id Lama
      inp_id_bis_lama = input("Masukan ID Bis Lama: ")

      # Input Data Baru
      inp_id_bis_baru = input("Masukan ID Bis Baru: ")
      inp_kode_bis = input("Masukan kode Bis Baru: ")
      inp_plat_bis = input("Masukan plat Bis Baru: ")

      # Menjalankan Query
      cursor.execute("UPDATE bis SET id_bis = %s, kode_bis = %s, plat_bis = %s WHERE id_bis = %s", (inp_id_bis_baru, inp_kode_bis, inp_plat_bis, inp_id_bis_lama))
      db.commit()
      print("Bis berhasil diedit")

   def hapusdatabis(self):
      # Input Id Bis
      inp_id_bis = input("Masukan ID Bis: ")

      # Menjalankan Query
      cursor.execute("DELETE FROM bis WHERE id_bis = %s", (inp_id_bis,))
      db.commit()
      print("Bis berhasil dihapus")