import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM matches
LIMIT 5;
""")


results = cursor.fetchall()


for row in results:
    print(row)


connection.close()