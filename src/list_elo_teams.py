import sqlite3
import pandas as pd

conn = sqlite3.connect("database/world_cup.db")

elo = pd.read_sql_query(
    """
    SELECT DISTINCT country
    FROM elo_history
    ORDER BY country
    """,
    conn
)

conn.close()

print(elo.to_string(index=False))