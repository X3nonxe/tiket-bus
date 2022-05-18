class User:

   # Attributes
   def __init__(self, id_user, username, password):
      self.id_user = id_user
      self.username = username
      self.password = password

   # Methods
   def beli_tiket(self):
      # Input user untuk membeli tiket
      inp_id_user = input("Masukkan ID User: ")
      inp_username = input("Masukkan Username: ")
      inp_password = input("Masukkan Password: ")

      if inp_id_user != None and inp_username != None and inp_password != None:
         pass


      print("Tiket berhasil dibeli")
