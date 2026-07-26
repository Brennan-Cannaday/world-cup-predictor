import pandas as pd
import sqlite3


# Load CSV
file_path = "data/raw/international_results.csv"

df = pd.read_csv(file_path)

# Convert date format
df["date"] = pd.to_datetime(df["date"], format="mixed")


# Connect to database
connection = sqlite3.connect("database/world_cup.db")


# Load data into SQL table
df.to_sql(
    "matches",
    connection,
    if_exists="append",
    index=False
)


print("Data loaded successfully!")

# Close connection
connection.close()