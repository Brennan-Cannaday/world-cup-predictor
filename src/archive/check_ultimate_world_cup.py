import pandas as pd

df = pd.read_csv(
    "data/raw/ultimate_world_cup.csv"
)

print("Columns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nFirst rows:")
print(df.head())

print("\nMissing values:")
print(df.isna().sum())