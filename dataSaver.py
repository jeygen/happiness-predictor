from happinessPredictor import happinessAlgo
import sqlite3
import datetime 
import os

now = datetime.datetime.now()
date_string = now.strftime('%Y-%m-%d')

con = sqlite3.connect('appData.db') # always need connection to db, creates local if non-extistent

# Once a Connection has been established, create a Cursor object and call its execute() method to perform 
cur = con.cursor()

path = './appData.db'
if os.path.exists(path) is False:
    # Create table
    cur.execute('''CREATE TABLE happiness_tracker 
                (date text, happiness_score int)''')

data = [(date_string, str(happinessAlgo()))]
# Insert a row of data
cur.executemany("INSERT INTO happiness_tracker VALUES (?, ?)", data)

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#con.close()
# res = cur.execute('SELECT count(rowid) FROM stocks')
# print(res.fetchone())
'''
#  Now, let us insert three more rows of data, using executemany():
data = [
    (date_string, str(happinessAlgo()))
]
cur.executemany('INSERT INTO happiness_tracker VALUES( ?, ?)', data)
'''
for row in cur.execute('SELECT * FROM happiness_tracker ORDER BY date'):
    print(row)

con.close()
