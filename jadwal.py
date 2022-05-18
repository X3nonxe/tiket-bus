from bis import Bis

class Jadwal(Bis):
   def __init__(self, kode_bis, id_jadwal: int, tujuan: str, tgl_berangkat: str):
      super().__init__(kode_bis)
      self.id_jadwal = id_jadwal
      self.tujuan = tujuan
      self.tgl_berangkat = tgl_berangkat 

   def tambah_jadwal(self):
      pass

   def edit_jadwal(self, idjadwal_baru: int, tujuan_baru: str, tglberangkat_baru: str):
      self.idjadwal_baru = idjadwal_baru
      self.tujuan_baru = tujuan_baru
      self.tglberangkat_baru = tglberangkat_baru

   def hapus_jadwal():
      pass

   def lihat_jadwal(self):
      print(f"Jadwal Keberangkatan Bis {self.kode_bis}")
      print(f"ID jadwal : {self.id_jadwal}")
      print(f"Dengan Tujuan : {self.tujuan}")
      print(f"Tanggal keberangkatan : {self.tgl_berangkat}")