import pandas as pd
from pathlib import Path

root = Path.cwd()

df_list = []

for folder in root.iterdir():

    csv = folder / "all.csv"

    if not csv.exists():
        continue

    df = pd.read_csv(csv, usecols=['ID'])
    df['company'] = folder.name
    df_list.append(df)

combined = pd.concat(df_list, ignore_index=True)

summary = (
    combined
    .groupby('ID', as_index=False)['company']
    .agg(lambda values: sorted(set(values)))
)
summary.head()

summary.to_json(
    root / 'problem_company_mapping.json',
    orient='records',
)
