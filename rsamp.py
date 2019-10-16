import pandas as pd
import json
import random

data = []

with open('endomondoHR_proper.json') as f:
    for l in f:
        if random.random() > 0.9:
            data.append(eval(l))

df = pd.DataFrame.from_dict(data)
print (df.head())
