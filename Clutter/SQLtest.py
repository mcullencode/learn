import mysql.connector

"""
mydb = mysql.connector.connect(
  host="localhost",
  user="cullen",
  passwd="password123"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
"""

mydb = mysql.connector.connect(
  host="localhost",
  user="cullen",
  passwd="password123"
)
