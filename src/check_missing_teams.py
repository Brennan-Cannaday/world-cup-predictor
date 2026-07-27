import pandas as pd
import sqlite3

conn = sqlite3.connect("database/world_cup.db")

world_cup = pd.read_csv(
    "data/processed/world_cup_team_history.csv"
)

elo = pd.read_sql_query(
    """
    SELECT *
    FROM elo_history
    """,
    conn
)

missing = []

for team in world_cup["team"].unique():

    if team not in elo["country"].unique():
        missing.append(team)

print("Missing teams:")
for team in sorted(missing):
    print(team)