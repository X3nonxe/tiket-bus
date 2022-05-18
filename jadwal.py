from bis import Bis

class Jadwal(Bis):

   # Atribut yang dibutuhkan:
   def __init__(self, id_jadwal: str, kode_bis: str, tujuan: str, tgl_berangkat: str):
      super().__init__(id_jadwal, kode_bis)
      self.id_jadwal = id_jadwal
      self.kode_bis = kode_bis
      self.tujuan = tujuan
      self.tgl_berangkat = tgl_berangkat

   # Method yang dibutuhkan:
   def lihat_jadwal(self):
      # Tampilan jadwal
      print("=== JADWAL ===")
      print(f"ID Jadwal: {self.id_jadwal}")
      print(f"Kode Bis: {self.kode_bis}")
      print(f"Tujuan: {self.tujuan}")
      print(f"Tanggal Berangkat: {self.tgl_berangkat}")

   def tambah_jadwal(self):
      # Input user untuk menambah jadwal
      inp_id_jadwal = input("Masukkan ID Jadwal: ")
      inp_kode_bis = input("Masukkan Kode Bis: ")
      inp_tujuan = input("Masukkan Tujuan: ")
      inp_tgl_berangkat = input("Masukkan Tanggal Berangkat: ")

      print("Jadwal berhasil ditambahkan")

   def edit_jadwal(self, idjadwal_baru: str, kodebis_baru: str, tujuan_baru: str, tglberangkat_baru: str):
      self.idjadwal_baru = idjadwal_baru
      self.kodebis_baru = kodebis_baru
      self.tujuan_baru = tujuan_baru
      self.tglberangkat_baru = tglberangkat_baru

      print("Jadwal berhasil diedit")

   def hapus_jadwal(self):
      print("Jadwal berhasil dihapus")

   