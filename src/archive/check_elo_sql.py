import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM elo_history
ORDER BY rating DESC
LIMIT 10;
""")


for row in cursor.fetchall():
    print(row)


connection.close()