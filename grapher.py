import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def graphTail():

    location = 'appData.csv'
    df = pd.read_csv(location)

    x = np.array(df['Time'].tail(5))
    y = np.array(df['Happiness Score'].tail(5))
    # # Define X and Y variable data
    # x = np.array([1, 2, 3, 4])
    # y = x*2
    plt.ylim(-1,1)


    plt.plot(x, y, color = 'green')
    plt.xlabel("Time") # add X-axis label
    plt.ylabel("Happiness Score") # add Y-axis label
    plt.title("Happiness vs Time of Day") # add title
    plt.show()

if __name__ == '__main__':
    graphTail()
    print("Graph plotted")