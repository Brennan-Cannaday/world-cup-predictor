import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


query = """
SELECT
    home_team AS team,
    COUNT(*) AS games,
    SUM(
        CASE 
            WHEN home_score > away_score THEN 1 
            ELSE 0 
        END
    ) AS wins
FROM matches
GROUP BY home_team
ORDER BY wins DESC
LIMIT 10;
"""


cursor.execute(query)

results = cursor.fetchall()


print("Top teams by wins as home team:")

for row in results:
    print(row)


connection.close()