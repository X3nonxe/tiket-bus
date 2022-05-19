import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="databis"
)

cursor = db.cursor()
