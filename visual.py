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
#print(sports)

#Drop unecessary URLs
df = df.drop(['id', 'url'], axis = 1)
df.head(1)

#Array of all unique users
#print(df['userId'].unique())

#Speed and heart rate of first user for a workout
x = df['speed'][0]
y = df['heart_rate'][0]

#Speed VS Heart Rate
#plt.scatter(x, y, color='g', s=6)
#plt.xlabel('Speed')
#plt.ylabel('Heart Rate')
#plt.show()

#Has various different exercise methods
id_ = 3905196
#Prints out all of the users sports
#for v in dupdf['sport']:
#    print(v)

#Save only the dataframe where the userid is the id_
dupdf = df[df.duplicated('userId')]
dupdf = dupdf.loc[df['userId'] == id_]

#Grab rows of different exercise methods
run = df.loc[df['sport'] == 'run']
bike = df.loc[df['sport'] == 'bike'] 

#Row with run
x = run['altitude'][30]
y = run['heart_rate'][30]

#Plot running data
for i in range(0, len(y)):
   plt.scatter(x[i], y[i], s=1, c='b')

#Repeat for biking
x = bike['altitude'][0]
y = bike['heart_rate'][0]

#Plot running data
for i in range(0, len(y)):
   plt.scatter(x[i], y[i], s=1, c='r')

#Heart Rate vs Speed for two sports
plt.title('Heart Rate vs Speed Scatter plot (Biking and Running)')
plt.xlabel('Heart Rate')
plt.ylabel('Speed')
plt.show()
