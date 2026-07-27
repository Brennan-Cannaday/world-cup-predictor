import pandas as pd
import requests
from io import StringIO


records = []


for year in range(1901, 2027):

    print(f"Downloading: {year}")

    url = f"https://www.eloratings.net/{year}.tsv"

    response = requests.get(url)

    if response.status_code != 200:
        continue


    df = pd.read_fwf(
        StringIO(response.text),
        header=None
    )

    df["year"] = year

    records.append(df)


elo = pd.concat(
    records,
    ignore_index=True
)


print()
print("Rows:", len(elo))
print()
print(elo.head())
print()
print("Columns:", elo.shape[1])


elo.to_csv(
    "data/raw/full_elo_history_raw.csv",
    index=False
)

print("Saved!")