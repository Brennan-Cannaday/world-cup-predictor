import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS team_matches (
    id INTEGER PRIMARY KEY,
    date TEXT,
    team TEXT,
    opponent TEXT,
    goals_for INTEGER,
    goals_against INTEGER,
    result TEXT,
    tournament TEXT
)
""")


connection.commit()

print("Team matches table created!")

connection.close()