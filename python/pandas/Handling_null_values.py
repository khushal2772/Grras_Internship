import pandas as pd
import numpy as np
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/file2.json"
df = pd.read_json(url)
df.loc[4,"marks"] = np.nan
df.loc[2,"marks"] = np.nan
print(df.isnull())
print(df.isnull().sum(axis=0))

print(df.fillna({"roll no": 200, "marks": 100}, inplace=True))

print(df['marks'].fillna(df["marks"].mean()))