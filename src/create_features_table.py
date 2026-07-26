import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS team_features (
    team TEXT PRIMARY KEY,
    matches_played INTEGER,
    wins INTEGER,
    losses INTEGER,
    draws INTEGER,
    win_percentage REAL,
    avg_goals_for REAL,
    avg_goals_against REAL
)
""")


connection.commit()

print("Team features table created!")

connection.close()