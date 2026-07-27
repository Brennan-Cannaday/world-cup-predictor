import pandas as pd

# Load World Cup dataset
file_path = "data/raw/world_cups.csv"

df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nYears Included:")
print(df["year"].unique())

print("\nNumber of World Cups:")
print(df["year"].nunique())