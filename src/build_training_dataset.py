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

# -----------------------
# Load team name mapping
# -----------------------

mapping = pd.read_csv(
    "data/raw/team_name_mapping.csv"
)

conn.close()

print("Team Features:", team_features.shape)
print("Elo:", elo.shape)
print("World Cup:", world_cup.shape)

# -----------------------
# Apply team name mapping
# -----------------------

world_cup = world_cup.merge(
    mapping,
    left_on="team",
    right_on="world_cup_name",
    how="left"
)

# If a team is not in the mapping file,
# keep the original name
world_cup["elo_team"] = world_cup["elo_name"].fillna(
    world_cup["team"]
)

# -----------------------
# Prepare Elo data
# -----------------------

world_cup_years = world_cup["year"].unique()

elo = elo[
    elo["year"].isin(world_cup_years)
]

elo = (
    elo.sort_values("snapshot_date")
       .groupby(["country", "year"], as_index=False)
       .last()
)

# -----------------------
# Merge World Cup + Elo
# -----------------------

training = world_cup.merge(
    elo,
    left_on=["elo_team", "year"],
    right_on=["country", "year"],
    how="left"
)

print(training.head())

print()

print(training.shape)

missing = training[
    training["rating"].isna()
]

print()
print("Missing Elo rows:", len(missing))
print()

print(
    missing[["year", "team"]]
    .sort_values(["year", "team"])
)