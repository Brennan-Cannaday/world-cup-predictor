import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS elo_history (

    year INTEGER,
    snapshot_date TEXT,
    country TEXT,
    rating INTEGER,
    rank INTEGER,
    matches_total INTEGER,
    wins INTEGER,
    losses INTEGER,
    draws INTEGER,
    goals_for INTEGER,
    goals_against INTEGER,
    confederation TEXT,
    is_host INTEGER

)
""")


connection.commit()

print("Elo table created!")

connection.close()