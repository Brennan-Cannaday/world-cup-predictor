import pandas as pd


# Location of dataset
file_path = "data/raw/international_results.csv"


# Load CSV into pandas DataFrame
df = pd.read_csv(file_path)


# Convert date column from text to actual dates
df["date"] = pd.to_datetime(df["date"], format="mixed")


# Display first 5 rows
print("First 5 rows:")
print(df.head())


# Display column names and data types
print("\nColumns and Data Types:")
print(df.dtypes)


# Display dataset size
print("\nDataset shape:")
print(df.shape)


# Check missing values
print("\nMissing values:")
print(df.isnull().sum())


# Tournament counts
print("\nTournament counts:")
print(df["tournament"].value_counts().head(20))


# Date range
print("\nDate range:")
print(df["date"].min())
print(df["date"].max())


# Number of unique teams
teams = set(df["home_team"]).union(set(df["away_team"]))

print("\nNumber of teams:")
print(len(teams))