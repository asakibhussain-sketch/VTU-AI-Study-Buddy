import sqlite3

conn = sqlite3.connect('Backend/vtu.db')
cursor = conn.cursor()

print("Checking for new subjects...")
cursor.execute("SELECT * FROM subjects WHERE scheme='2021' AND semester='1'")
rows = cursor.fetchall()
for row in rows:
    print(row)

if not rows:
    print("No subjects found for 2021 Sem 1.")
else:
    print(f"Found {len(rows)} subjects for 2021 Sem 1.")

conn.close()
