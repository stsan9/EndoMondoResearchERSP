import pandas as pd
import json
import numpy as np

data = []
with open('truncatedData.json') as f:
    for l in f:
        data.append(eval(l))

dataframe = pd.DataFrame.from_dict(data)

# This section makes each timestamp its own row
def row_to_table(row):
    """
    Transforms each row with exercise data into a table with a timestamp for
    each row.
    """
    stamps = len(row[0])
    data = {
        'altitude': row[0],
        'gender': ([row[1]] * stamps),
        'heart_rate': row[2],
        'id': ([row[3]] * stamps),
        'latitude': row[4],
        'longitude': row[5],
        'speed': row[6],
        'sport': ([row[7]] * stamps),
        'timestamp': row[8],
        'url': ([row[9]] * stamps),
        'userId': ([row[10]] * stamps)
    }
    df = pd.DataFrame(data)
    return df
# Applies the function to each row and combines the outputted tables. Will take
# longer to run
data = {
    'altitude': [],
    'gender': [], 
    'heart_rate': [],
    'id': [],
    'latitude': [],
    'longitude': [],
    'speed': [],
    'sport': [],
    'timestamp': [],
    'url': [],
    'userId': []
}
df = pd.DataFrame(data)
for i in np.arange(1000):
    temp = row_to_table(dataframe.iloc[i])
    df = pd.concat([df, temp], ignore_index=True)

# Coverts time from unix to the percent of the exercise that has been completed.
def time_convert(i):
    times = df[df['id'] == df.iloc[i][3]]
    time_list = list(times['timestamp'])
    start = min(time_list)
    total = max(time_list) - start
    for i in np.arange(len(time_list)):
        if total != 0:
            time_list[i] = (time_list[i] - start) / total
        else:
            time_list[i] = 1
    return time_list
# Appiles function again.
new_time = []
i = 0
while i < 470185:
    convert = time_convert(i)
    new_time += convert
    i += len(convert)

df['timestamp'] = new_time
print(df)
