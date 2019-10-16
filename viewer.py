import pandas as pd
import json
import os

# Truncate the JSON file to save RAM/memory
os.system('head -n 1000 endomondoHR_proper.json > truncatedData.json')

# Transform the datafile to a dataframe
data = []
with open('truncatedData.json') as f:
	for l in f:
		data.append(eval(l))

dataframe = pd.DataFrame.from_dict(data)
print(dataframe.head())
