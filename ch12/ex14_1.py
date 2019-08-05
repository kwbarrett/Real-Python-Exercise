import sqlite3

values = (
    ("Jean-Baptiste Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5)
)

with sqlite3.connect("species_database.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE Roster(
            Name TEXT,
            Species TEXT,
            IQ INT
            );"""
    )
    cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values)

    cursor.execute(
        "SELECT * FROM Roster;"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.execute(
        "UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas';"
    )

    cursor.execute(
        "SELECT Name, IQ FROM Roster WHERE Species = 'Human';"
    )

    for row in cursor.fetchall():
        print(row)

