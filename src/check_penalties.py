import pandas as pd

df = pd.read_csv("data/raw/world_cup.csv")

penalty_games = df[
    df["win_conditions"].notna()
]

print(penalty_games[
    [
        "year",
        "home_team",
        "away_team",
        "home_score",
        "away_score",
        "win_conditions",
        "winning_team"
    ]
])