import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM team_features
ORDER BY win_percentage DESC
LIMIT 10;
""")


for row in cursor.fetchall():
    print(row)


connection.close()