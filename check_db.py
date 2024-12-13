import sqlite3

conn = sqlite3.connect("contact.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()

if rows:
    for row in rows:
        print(row)
else:
    print("No data found in the contacts table.")

conn.close()
