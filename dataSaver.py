from happinessPredictor import happinessAlgo
import sqlite3
import datetime 

now = datetime.datetime.now()
date_string = now.strftime('%Y-%m-%d')

con = sqlite3.connect('example.db') # always need connection to db, creates local if non-extistent

# Once a Connection has been established, create a Cursor object and call its execute() method to perform 
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE happiness_tracker 
               (date text, happiness_score int)''')

# Insert a row of data
cur.execute("INSERT INTO happiness_tracker VALUES (date_string, str(happinessAlgo())")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#con.close()
'''
 res = cur.execute('SELECT count(rowid) FROM stocks')
 print(res.fetchone())

#  Now, let us insert three more rows of data, using executemany():
data = [
    ('2006-03-28', 'BUY', 'IBM', 1000, 45.0),
    ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0),
    ('2006-04-06', 'SELL', 'IBM', 500, 53.0),
]
cur.executemany('INSERT INTO stocks VALUES(?, ?, ?, ?, ?)', data)
'''
for row in cur.execute('SELECT * FROM happiness_tracker ORDER BY date'):
    print(row)

con.close()
