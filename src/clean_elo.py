import pandas as pd
import re


# -------------------------
# Load raw elo file
# -------------------------

raw = pd.read_csv(
    "data/raw/elo_raw.csv",
    header=None,
    encoding="latin1"
)

print("Raw shape:")
print(raw.shape)

print()
print(raw.head())


# -------------------------
# Convert rows into strings
# -------------------------

rows = []

for _, row in raw.iterrows():

    text = " ".join(
        str(x)
        for x in row.tolist()
        if pd.notna(x)
    )

    rows.append(text)


# -------------------------
# Extract useful fields
# -------------------------

records = []


for row in rows:

    # remove weird encoding characters
    row = row.replace("â", "")

    parts = row.split()

    if len(parts) < 5:
        continue


    try:

        rank = int(parts[0])

    except:
        continue


    country_code = parts[1]


    try:
        rating = int(parts[2])

    except:
        continue


    records.append(
        {
            "rank": rank,
            "country_code": country_code,
            "rating": rating
        }
    )


elo = pd.DataFrame(records)


print()
print("Clean rows:")
print(elo.head())

print()
print("Rows:")
print(len(elo))


elo.to_csv(
    "data/processed/elo_clean.csv",
    index=False
)

print()
print("Saved elo_clean.csv")