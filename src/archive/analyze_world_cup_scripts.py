import pandas as pd

df = pd.read_csv("data/raw/world_cups.csv")

print("Stages:")
print(df["stage"].value_counts())

print("\nYears:")
print(df["year"].nunique())

print("\nOldest World Cup:")
print(df["year"].min())

print("\nNewest World Cup:")
print(df["year"].max())

print("\nOutcome values:")
print(df["outcome"].value_counts())