import sqlite3

conn = sqlite3.connect('Backend/vtu.db')
cursor = conn.cursor()

print("Subjects Table:")
cursor.execute("SELECT * FROM subjects")
for row in cursor.fetchall():
    print(row)

conn.close()
