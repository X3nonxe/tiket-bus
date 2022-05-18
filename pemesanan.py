from jadwal import Jadwal

class Pemesanan(Jadwal):


   # Atribut yang dibutuhkan:
   def __init__(self, id_bis, id_jadwal, harga, tanggal_pemesanan):
      super().__init__(id_bis, id_jadwal)
      self.id_bis = id_bis
      self.id_jadwal = id_jadwal
      self.harga = harga
      self.tanggal_pemesanan = tanggal_pemesanan

   # Method yang dibutuhkan:
   def batalkan_pemesanan(self):
      # Input user untuk membatalkan pemesanan
      inp_id_bis = input("Masukkan ID Bis: ")
      inp_id_jadwal = input("Masukkan ID Jadwal: ")
      inp_harga = input("Masukkan Harga: ")
      inp_tanggal_pemesanan = input("Masukkan Tanggal Pemesanan: ")

      print("Tiket berhasil dibatalkan")

   def cetak_tiket(self):
      # Input user untuk mencetak tiket
      inp_id_bis = input("Masukkan ID Bis: ")
      inp_id_jadwal = input("Masukkan ID Jadwal: ")
      inp_harga = input("Masukkan Harga: ")
      inp_tanggal_pemesanan = input("Masukkan Tanggal Pemesanan: ")

      # Tampilan tiket yang di cetak
      print("=== TIKET ===")
      print(f"ID Bis: {inp_id_bis}")
      print(f"ID Jadwal: {inp_id_jadwal}")
      print(f"Harga: {inp_harga}")
      print(f"Tanggal Pemesanan: {inp_tanggal_pemesanan}")

      print("Tiket berhasil dicetak")

