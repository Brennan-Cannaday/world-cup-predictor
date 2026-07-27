import pandas as pd

elo = pd.read_csv("data/raw/elo_ratings.csv")

for team in [
    "Bolivia",
    "Chile",
    "Peru",
    "Romania",
    "Nigeria",
    "Poland",
    "Russia"
]:
    print("\n" + "=" * 50)
    print(team)

    print(
        elo[elo["country"] == team][
            ["year", "country", "rating"]
        ].head(20)
    )