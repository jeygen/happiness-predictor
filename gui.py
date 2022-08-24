from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC
from PIL import ImageTk,Image
#from dataSaver2 import deleteAppData, runSaveAppData
from grapher import graphTail
from happinessPredictor import happinessAlgo
import sqlite3
import datetime 
import os
#from dataSaver import runBackupSave
import pandas as pd
import time
from os.path import exists
from os import remove


#from globals import new_h_score, new_h1
#from globals import h

root = Tk()
root.title('Happiness Predictor')
root.iconbitmap('images/happyFace.ico')
root.geometry("530x433")
root['bg'] = '#d9ead3'

my_img1 = Image.open('images/flowers.png')
my_img1.thumbnail((500,500))
my_img1.save('images/f_thumbnail.png')
my_img1 = ImageTk.PhotoImage(Image.open("images/f_thumbnail.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/f_thumbnail.png"))

image_list = [my_img1, my_img2]

with open('appWelcome.txt') as f:
    appText = f.read()

my_label = Label(
				root, image=my_img1, text=appText, compound=CENTER, anchor=S, 
				font=("System", 24, BOLD), wraplength=500, border=3, relief=RAISED, 
				justify=CENTER, borderwidth=5, padx=10, pady=10, background='green',
				foreground='white'
				)

my_label.grid(row=0, column=0, columnspan=4)

h_score = happinessAlgo()

'''
def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget() # delete current image from screen
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 2: # if last image
		button_forward = Button(root, text=">>", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

def back(image_number):
	global my_label # remember to declare global to access global in python
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(root, text="<<", command=lambda: back(image_number-1))

	if image_number == 1:
		button_back = Button(root, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)
'''
h_score = 0

def getScore():
	global my_label
	#global saveButton
	#global deleteButton
	#global graphButton
	#global button_exit
	global my_img1
	global h_score
	h_score = happinessAlgo()


	my_label.grid_forget() # delete current image from screen
	my_label = Label(
				root, image=my_img1, text='On scale of -1 (very sad) to 1 (very happy), you are: ' + 
				str(h_score), compound=CENTER, anchor=S, 
				font=("System", 24, BOLD), wraplength=500, border=3, relief=RAISED, 
				justify=CENTER, borderwidth=5, padx=10, pady=10, background='green',
				foreground='black'
				)
	my_label.grid(row=0, column=0, columnspan=4)
	runSaveAppData()


def clearData():
	result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
	if result == 'yes':
		print('Deleted')
		#deleteAppData()
	else:
		print('Not Deleted')

def graphData():
	graphTail()

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

    data = [(date_string, str(h_score))]
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

location = 'appData.csv'
#c3Data = happinessAlgo()

def saveAppData():
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
    #c3Data = happinessAlgo()

    d = {c1 : [c1Data], c2 : [c2Data], c3 : [h_score]}

    # creating dataframe from the above dictionary of lists
    df = pd.DataFrame(d)
    print("DataFrame...\n",df)

    if exists(location):
        df.to_csv(location, mode = 'a', index = False, header = False)
    else:
        # write dataFrame to SalesRecords CSV file
        df.to_csv(location, index = False)

def deleteAppData():
    remove(location)
    print("Data deleted")

def runSaveAppData():
    try:
        saveAppData()
        runBackupSave()
        print("Data saved")
    except Exception as e:
        print("Error saving data")
        print(e)
        print("Data not saved")

#button_back = Button(root, text="<<", command=back, state=DISABLED)
saveButton = Button(root, text="                   Happiness                     ", command=lambda: getScore())
deleteButton = Button(root, text="   Delete   ", command=lambda: clearData())
graphButton = Button(root, text="             Graph           ", command=lambda: graphData())
button_exit = Button(root, text="         Exit         ", command=root.quit)
#button_forward = Button(root, text=">>", command=lambda: forward(2))


#button_back.grid(row=1, column=0)
saveButton.grid(row=1, column=0, sticky=SW)
graphButton.grid(row=1, column=1, sticky=SW)
deleteButton.grid(row=1, column=2)
button_exit.grid(row=1, column=3, sticky=SE)

#button_forward.grid(row=1, column=2)

root.mainloop()
