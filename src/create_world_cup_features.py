import pandas as pd

# Load data
df = pd.read_csv("data/raw/world_cup.csv")

records = []

for year in sorted(df["year"].unique()):

    tournament = df[df["year"] == year]

    teams = pd.unique(
        pd.concat(
            [
                tournament["home_team"],
                tournament["away_team"]
            ]
        )
    )

    # -----------------------------
    # Special case: 1950 World Cup
    # -----------------------------
    if year == 1950:

        standings = {}

        for team in teams:
            standings[team] = {
                "points": 0,
                "gd": 0,
                "gf": 0
            }

        final_round = tournament[
            tournament["stage"] == "Final Round"
        ]

        for _, row in final_round.iterrows():

            home = row["home_team"]
            away = row["away_team"]

            hs = row["home_score"]
            aw = row["away_score"]

            standings[home]["gf"] += hs
            standings[home]["gd"] += hs - aw

            standings[away]["gf"] += aw
            standings[away]["gd"] += aw - hs

            # 1950 used 2 points for a win
            if hs > aw:
                standings[home]["points"] += 2
            elif aw > hs:
                standings[away]["points"] += 2
            else:
                standings[home]["points"] += 1
                standings[away]["points"] += 1

        ranking = sorted(
            standings.items(),
            key=lambda x: (
                x[1]["points"],
                x[1]["gd"],
                x[1]["gf"]
            ),
            reverse=True
        )

        finish_lookup = {}

        finish_lookup[ranking[0][0]] = "Champion"
        finish_lookup[ranking[1][0]] = "Runner-up"
        finish_lookup[ranking[2][0]] = "Third Place"
        finish_lookup[ranking[3][0]] = "Fourth Place"

        for team in teams:

            finish = finish_lookup.get(team, "Group Stage")

            records.append(
                {
                    "year": year,
                    "team": team,
                    "finish": finish
                }
            )

        continue

    # -----------------------------
    # Normal World Cups
    # -----------------------------
    for team in teams:

        team_games = tournament[
            (tournament["home_team"] == team) |
            (tournament["away_team"] == team)
        ]

        finish = "Group Stage"

        # ----- Final -----
        final = tournament[tournament["stage"] == "Final"]

        if not final.empty:

            final = final.iloc[0]

            if team == final["winning_team"]:
                finish = "Champion"

            elif team == final["losing_team"]:
                finish = "Runner-up"

        # ----- Third Place -----
        if finish == "Group Stage":

            third = tournament[tournament["stage"] == "Third place"]

            if not third.empty:

                third = third.iloc[0]

                if team == third["winning_team"]:
                    finish = "Third Place"

                elif team == third["losing_team"]:
                    finish = "Fourth Place"

        # ----- Other stages -----
        if finish == "Group Stage":

            stages = set(team_games["stage"])

            if "Semifinals" in stages:
                finish = "Semifinal"

            elif "Quarterfinals" in stages:
                finish = "Quarterfinal"

            elif "Round of 16" in stages:
                finish = "Round of 16"

            elif any("Group" in s for s in stages):
                finish = "Group Stage"

        records.append(
            {
                "year": year,
                "team": team,
                "finish": finish
            }
        )

history = pd.DataFrame(records)

history = history.sort_values(
    ["year", "team"]
)

history.to_csv(
    "data/processed/world_cup_team_history.csv",
    index=False
)

print(history.head(25))
print()
print("Rows:", len(history))
print()
print(history["finish"].value_counts())