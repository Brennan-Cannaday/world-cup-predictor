import sqlite3
import pandas as pd

# -----------------------
# Connect to database
# -----------------------

conn = sqlite3.connect("database/world_cup.db")

# -----------------------
# Load team features
# -----------------------

team_features = pd.read_sql_query(
    """
    SELECT *
    FROM team_features
    """,
    conn
)

# -----------------------
# Load Elo ratings
# -----------------------

elo = pd.read_sql_query(
    """
    SELECT *
    FROM elo_history
    """,
    conn
)

# -----------------------
# Load World Cup finishes
# -----------------------

world_cup = pd.read_csv(
    "data/processed/world_cup_team_history.csv"
)

conn.close()

print("Team Features:", team_features.shape)
print("Elo:", elo.shape)
print("World Cup:", world_cup.shape)

world_cup_years = world_cup["year"].unique()

elo = elo[elo["year"].isin(world_cup_years)]

elo = (
    elo.sort_values("snapshot_date")
       .groupby(["country", "year"], as_index=False)
       .last()
)

elo = elo.rename(columns={"country": "team"})

training = world_cup.merge(
    elo,
    on=["team", "year"],
    how="left"
)

print(training.head())

print()

print(training.shape)

missing = training[training["rating"].isna()]

print()
print("Missing Elo rows:", len(missing))
print()

print(
    missing[["year", "team"]]
    .sort_values(["year", "team"])
)