from happinessPredictor import happinessAlgo
import sqlite3
import datetime 
import os
#from dataSaver2 import c3Data


def backupSave():
    global c3Data 
    c3Data = happinessAlgo()
    now = datetime.datetime.now()
    date_string = now.strftime('%Y-%m-%d')
    path = 'appData.db'

    con = sqlite3.connect('appData.db')

    # Once a Connection has been established, create a Cursor object and call its execute() method to perform 
    cur = con.cursor()

    # Create table
    if os.path.exists(path) == False:
        cur.execute('''CREATE TABLE happiness_tracker 
                    (date text, happiness_score int)''')

    data = [(date_string, str(c3Data))]
    # Insert a row of data
    cur.executemany("INSERT INTO happiness_tracker VALUES (?, ?)", data)

    # Save (commit) the changes
    con.commit()

    for row in cur.execute('SELECT * FROM happiness_tracker ORDER BY date'):
        print(row)

    con.close()

def runBackupSave():
    try:
        backupSave()
        print("Data saved")
    except Exception as e:
        print("Error saving back-up data")
        print(e)
        print("Data not saved")

if __name__ == '__main__':
    try:
        backupSave()
        print("Data saved")
    except Exception as e:
        print("Error saving back-up data")
        print(e)
        print("Data not saved")
        pass

