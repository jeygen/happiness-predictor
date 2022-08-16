import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

location = 'appData.csv'
df = pd.read_csv(location)

x = np.array(df['Time'])
y = np.array(df['Happiness Score'])
# # Define X and Y variable data
# x = np.array([1, 2, 3, 4])
# y = x*2



plt.plot(x, y)
plt.xlabel("X-axis") # add X-axis label
plt.ylabel("Y-axis") # add Y-axis label
plt.title("Any suitable title") # add title
plt.show()
