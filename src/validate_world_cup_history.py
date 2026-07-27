import pandas as pd

df = pd.read_csv("data/processed/world_cup_team_history.csv")

years = sorted(df["year"].unique())

for year in years:

    print("\n" + "=" * 50)
    print(year)
    print("=" * 50)

    tournament = df[df["year"] == year]

    finishes = [
        "Champion",
        "Runner-up",
        "Third Place",
        "Fourth Place",
        "Semifinal",
        "Quarterfinal",
        "Round of 16",
        "Group Stage",
        "Final Round"
    ]

    for finish in finishes:
        teams = tournament[tournament["finish"] == finish]["team"].tolist()

        if teams:
            print(f"\n{finish}:")
            for team in sorted(teams):
                print("   ", team)

print("\nOverall Finish Counts:")
print(df["finish"].value_counts())