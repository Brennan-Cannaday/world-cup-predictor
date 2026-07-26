import sqlite3


# Connect to database
connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


# Create matches table
cursor.execute("""
CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY,
    date TEXT,
    home_team TEXT,
    away_team TEXT,
    home_score INTEGER,
    away_score INTEGER,
    tournament TEXT,
    city TEXT,
    country TEXT,
    neutral BOOLEAN
)
""")


# Save changes
connection.commit()


print("Matches table created!")


# Close connection
connection.close()