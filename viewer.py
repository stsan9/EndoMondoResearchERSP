import pandas as pd
import json

data = []
with open('truncatedData.json') as f:
    for l in f:
        data.append(eval(l))

df = pd.DataFrame.from_dict(data)
print(df.head())
