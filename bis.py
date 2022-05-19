class Bis:
   def __init__(self, id_bis: str, kode_bis: str, plat_bis: str):
      self.id_bis = id_bis
      self.kode_bis = kode_bis
      self.plat_bis = plat_bis

   def pemberangkatan(self):
      print("==PEMBERANGKATAN BIS==")
      print(f"ID Bis: {self.id_bis}")
      print(f"Kode Bis: {self.kode_bis}")
      print(f"Plat Bis: {self.plat_bis}")

   def tambahdatabis(self):
      # Input untuk menambahkan jadwal
      inp_id_bis = input("Masukan ID Bis: ")
      inp_kode_bis = input("Masukan kode Bis: ")
      inp_plat_bis = input("Masukan plat Bis: ")

   def editdatabis(self, idbis_baru: str, kodebis_baru: str, platbis_baru: str):
      self.idbis_baru = idbis_baru
      self.kodebis_baru = kodebis_baru
      self.platbis_baru = platbis_baru

   def hapusdatabis(self):
      print("Jadwal berhasil dihapus")