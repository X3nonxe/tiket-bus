from bis import Bis

class Jadwal(Bis):
   def __init__(self, kode_bis, id_jadwal: int, tujuan: str, tgl_berangkat: str):
      super().__init__(kode_bis)
      self.id_jadwal = id_jadwal
      self.tujuan = tujuan
      self.tgl_berangkat = tgl_berangkat 

   def lihat_jadwal(self):
      pass

   def tambah_jadwal(self):
      pass

   def edit_jadwal(self, idjadwal_baru: int, tujuan_baru: str, tglberangkat_baru: str):
      self.idjadwal_baru = idjadwal_baru
      self.tujuan_baru = tujuan_baru
      self.tglberangkat_baru = tglberangkat_baru

   def hapus_jadwal():
      pass