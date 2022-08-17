from happinessPredictor import happinessAlgo
import pandas as pd
import datetime
import time
from os.path import exists

location = 'appData.csv'

# dictionary of lists
# d = {'Car': ['BMW', 'Lexus', 'Audi', 'Mercedes', 'Jaguar', 'Bentley'],'Date_of_purchase': ['2020-10-10', '2020-10-12', '2020-10-17', '2020-10-16', '2020-10-19', '2020-10-22']
# }
now = datetime.datetime.now()
date_string = now.strftime('%Y-%m-%d')
curr_time = time.strftime("%H:%M", time.localtime())

c1 = 'Date'
c1Data = date_string
c2 = 'Time'
c2Data = curr_time 
c3 = 'Happiness Score'
c3Data = happinessAlgo()

d = {c1 : [c1Data], c2 : [c2Data], c3 : [c3Data]}

# creating dataframe from the above dictionary of lists
df = pd.DataFrame(d)
print("DataFrame...\n",df)

if exists(location):
    df.to_csv(location, mode = 'a', index = False, header = False)
else:
    # write dataFrame to SalesRecords CSV file
    df.to_csv(location, index = False)
