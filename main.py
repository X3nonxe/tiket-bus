from bis import Bis
from jadwal import Jadwal
from pemesanan import Pemesanan



if __name__ == '__main__':
   # Object Bis
   bis = Bis(1, "1234", "K1234")
   bis.pemberangkatan()
   bis.tambahdatabis()
   bis.editdatabis()
   bis.hapusdatabis()

   # Object Jadwal
   jadwal = Jadwal(1, "1234", "Jakarta", "Bandung", "2020-01-01")
   jadwal.lihat_jadwal()
   jadwal.tambah_jadwal()
   jadwal.edit_jadwal()
   jadwal.hapus_jadwal()

   # # Object Pemesanan
   pemesanan = Pemesanan(1, "1234", 1, "10000", "2020-01-01")
   pemesanan.cetak()
   pemesanan.batalkan()