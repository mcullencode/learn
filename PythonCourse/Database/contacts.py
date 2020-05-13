import sqlite3

#will connect to contacts.sqlite database. if it doesnt exist, will create
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('Mikey',123456, 'mikey@gmail.com')")
db.execute("INSERT INTO contacts VALUES('brian', 1234, 'brian@gmail.com')")

#to query we use a cursor
cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
#row is tuple, can separate out as (for name, number, email in cursor:)

#print(cursor.fetchall())

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
for row in cursor:
    print(row)

cursor.close()

#this saves the changes of the database
db.commit()

db.close()





