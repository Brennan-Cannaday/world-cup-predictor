import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


# Pull all matches from original table
cursor.execute("""
SELECT 
    date,
    home_team,
    away_team,
    home_score,
    away_score,
    tournament
FROM matches
""")


matches = cursor.fetchall()


team_rows = []


for match in matches:

    date, home, away, home_score, away_score, tournament = match


    # Determine result
    if home_score > away_score:
        home_result = "Win"
        away_result = "Loss"

    elif home_score < away_score:
        home_result = "Loss"
        away_result = "Win"

    else:
        home_result = "Draw"
        away_result = "Draw"


    # Add home team perspective
    team_rows.append(
        (
            date,
            home,
            away,
            home_score,
            away_score,
            home_result,
            tournament
        )
    )


    # Add away team perspective
    team_rows.append(
        (
            date,
            away,
            home,
            away_score,
            home_score,
            away_result,
            tournament
        )
    )


# Insert rows
cursor.executemany("""
INSERT INTO team_matches
(
date,
team,
opponent,
goals_for,
goals_against,
result,
tournament
)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", team_rows)


connection.commit()


print(f"Inserted {len(team_rows)} rows into team_matches")


connection.close()