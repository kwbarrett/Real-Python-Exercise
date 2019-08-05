import sqlite3

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM People;")

# cursor.execute("DROP TABLE People;")
for row in cursor.fetchall():
    print(row)