from jadwal import Jadwal
from bis import Bis
class Pemesanan(Jadwal, Bis):
   def __init__(self, id_bis: str, id_jadwal: str, harga: str, tglpesanan: str):
      super().__init__(id_bis, id_jadwal)
      self.harga = harga
      self.tglpesanan = tglpesanan

   def batalkan(self):
      pass

   def cetak(self):
      print(f"Harga tiket Bis {self.id_bis} dengan keberangkatan {self.id_jadwal} senilai {self.harga}")
      print(f"Tiket di pesan pada tanggal {self.tglpesanan}")