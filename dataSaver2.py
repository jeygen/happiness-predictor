from happinessPredictor import happinessAlgo
import pandas as pd
import datetime

# dictionary of lists
# d = {'Car': ['BMW', 'Lexus', 'Audi', 'Mercedes', 'Jaguar', 'Bentley'],'Date_of_purchase': ['2020-10-10', '2020-10-12', '2020-10-17', '2020-10-16', '2020-10-19', '2020-10-22']
# }
d = {datetime.datetime.now().strftime('%Y-%m-%d') : str(happinessAlgo())}

# creating dataframe from the above dictionary of lists
dataFrame = pd.DataFrame(d)
print("DataFrame...\n",dataFrame)

# write dataFrame to SalesRecords CSV file
dataFrame.to_csv("appData.csv")
