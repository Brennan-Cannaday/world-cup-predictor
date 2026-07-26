import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


query = """
SELECT home_team, COUNT(*) AS matches_played
FROM matches
GROUP BY home_team
ORDER BY matches_played DESC
LIMIT 10;
"""


cursor.execute(query)

results = cursor.fetchall()


print("Most matches played as home team:")

for row in results:
    print(row)


connection.close()