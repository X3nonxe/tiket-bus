from bis import Bis
from jadwal import Jadwal
from pemesanan import Pemesanan
from user import User
from login import Login

if __name__ == '__main__':
   # Membuat objek
   bis = Bis(0, "", "")
   user = User(0, "", "")
   jadwal = Jadwal(0, "", "", "", "", "")
   pemesanan = Pemesanan(0, "", 0, "", "", "", "", "", "")

   login = Login("admin", "admin")
   login.login()
  

   def menu_utama():
      print("=========== MENU UTAMA ===========")
      print("1. Tambah Bis")
      print("2. Tambah Jadwal")
      print("3. Buat Tiket")
      print("")
      print("4. Hapus Bis")
      print("5. Hapus Jadwal")
      print("6. Hapus Tiket")
      print("")
      print("7. Lihat Bis")
      print("8. Lihat Jadwal")
      print("9. Lihat Tiket")
      print("")
      print("0. Keluar")
      print("==================================")
      menu = input("Pilih menu: ")
      
      if menu == "1":
         bis.tambahdatabis()
      elif menu == "2":
         jadwal.tambah_jadwal()
      elif menu == "3":
         user.beli_tiket()
      elif menu == "4":
         bis.hapusdatabis()
      elif menu == "5":
         jadwal.hapus_jadwal()
      elif menu == "6":
         pemesanan.batalkan()
      elif menu == "7":
         bis.pemberangkatan()
      elif menu == "8":
         jadwal.lihat_jadwal()
      elif menu == "9":
         pemesanan.cetak()
      
   menu_utama()