import sqlite3

db = sqlite3.connect(':memory:')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')


#cursor.execute('''SHOW DATABASES''')