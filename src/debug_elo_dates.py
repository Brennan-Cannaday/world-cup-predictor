import sqlite3
import pandas as pd


conn = sqlite3.connect("database/world_cup.db")

elo = pd.read_sql_query(
    """
    SELECT *
    FROM elo_history
    """,
    conn
)

conn.close()


teams = [
    "Bolivia",
    "Chile",
    "Peru",
    "Romania",
    "Yugoslavia",
    "Nigeria",
    "Poland"
]


for team in teams:

    print("\n")
    print("="*40)
    print(team)

    print(
        elo[
            elo["country"] == team
        ][
            ["year", "snapshot_date", "rating"]
        ]
        .head(10)
    )