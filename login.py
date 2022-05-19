class Login():
	def __init__(self, username, password):
		self.username = username
		self.password = password

	def login(self):
		print("Logging in...")
		if self.username == "admin" and self.password == "admin":
			print("Login successful")
		elif self.username == "user" and self.password == "user":
			print("Login successful")
		else:
			print("Login failed")
			exit()

	