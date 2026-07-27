import pandas as pd
import sqlite3


df = pd.read_csv("data/raw/elo_ratings.csv")


df = df[
[
"year",
"snapshot_date",
"country",
"rating",
"rank",
"matches_total",
"wins",
"losses",
"draws",
"goals_for",
"goals_against",
"confederation",
"is_host"
]
]


connection = sqlite3.connect("database/world_cup.db")


df.to_sql(
    "elo_history",
    connection,
    if_exists="append",
    index=False
)


connection.close()


print("Elo data loaded!")