import sqlite3


connection = sqlite3.connect("database/world_cup.db")

cursor = connection.cursor()


query = """
SELECT
    team,
    COUNT(*) AS matches_played,

    SUM(
        CASE 
            WHEN result = 'Win' THEN 1
            ELSE 0
        END
    ) AS wins,

    SUM(
        CASE 
            WHEN result = 'Loss' THEN 1
            ELSE 0
        END
    ) AS losses,

    SUM(
        CASE 
            WHEN result = 'Draw' THEN 1
            ELSE 0
        END
    ) AS draws,

    CAST(
        SUM(
            CASE 
                WHEN result = 'Win' THEN 1
                ELSE 0
            END
        ) AS FLOAT
    ) / COUNT(*) AS win_percentage,

    AVG(goals_for) AS avg_goals_for,

    AVG(goals_against) AS avg_goals_against

FROM team_matches

GROUP BY team;
"""


cursor.execute(query)

features = cursor.fetchall()


cursor.executemany("""
INSERT OR REPLACE INTO team_features
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", features)


connection.commit()


print(f"Created features for {len(features)} teams")


connection.close()