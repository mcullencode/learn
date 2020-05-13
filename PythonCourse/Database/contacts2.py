import sqlite3

#will connect to contacts.sqlite database. if it doesnt exist, will create
db = sqlite3.connect("contacts.sqlite")

#here we query without explicitly creating a cursor like done previously

new_email = "newemail@update.com"
phone = input("please enter phone number of email youd like to update")


update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
print(update_sql)

#sql injection attack, can inset phone number 1234; drop table, and it can delete db.

update_cursor = db.cursor()
update_cursor.executescript(update_sql)
print('{} rows updated'.format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-'*20)

#doesnt print, because nothing is saved to the database unless it is committed

db.close()