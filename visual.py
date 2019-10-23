import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import json
import os
import seaborn as sns

#Truncating currently existing data to open file
data = []
path = 'endomondoHR_proper.json'
os.system('head -n 1000 endomondoHR_proper.json > truncatedData.json')

with open('truncatedData.json') as f:
    for l in f:
        data.append(eval(l))

#Creating dataframe from dictionary file
df = pd.DataFrame.from_dict(data)
df.head()

#Array of all unique sports
sports = df['sport'].unique()
print(sports)

#Drop unecessary URLs
df = df.drop(['id', 'url'], axis = 1)
df.head(1)

#Array of all unique users
print(df['userId'].unique())

#Speed and heart rate of first user for a workout
x = df['speed'][0]
y = df['heart_rate'][0]

#Speed VS Heart Rate
plt.scatter(x, y, color='g', s=6)
plt.xlabel('Speed')
plt.ylabel('Heart Rate')
plt.show()

id_ = 10921915

x = df[df['userId'] == id_]['speed']
y = df[df['userId'] == id_]['heart_rate']
z = df[df['userId'] == id_]['sport']

for i in range(0, 4):
    if z[i] == 'bike':
        plt.scatter(x[i], y[i], s=8, c='b')
    elif z[i] == 'bike (transport)':
        plt.scatter(x[i], y[i], s=20, c='r')

#Heart Rate vs Speed for two sports
plt.title('Heart Rate vs Speed Scatter plot (Biking and Running)')
plt.xlabel('Heart Rate')
plt.ylabel('Speed')
plt.show()
