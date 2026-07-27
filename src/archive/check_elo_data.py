import pandas as pd


df = pd.read_csv("data/raw/elo_ratings.csv")


print("First 5 rows:")
print(df.head())


print("\nColumns:")
print(df.columns)


print("\nShape:")
print(df.shape)


print("\nData types:")
print(df.dtypes)


print("\nMissing values:")
print(df.isnull().sum())