from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD, ITALIC
from PIL import ImageTk,Image
from dataSaver2 import deleteAppData, runSaveAppData
from grapher import graphTail
from happinessPredictor import happinessAlgo

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
				foreground='black'
				)

my_label.grid(row=0, column=0, columnspan=4)

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

def getScore():
	global my_label
	global saveButton
	global deleteButton
	global graphButton
	global button_exit
	global my_img1

	runSaveAppData()
	my_label.grid_forget() # delete current image from screen
	my_label = Label(
				root, image=my_img1, text=str(happinessAlgo()), compound=CENTER, anchor=S, 
				font=("System", 24, BOLD), wraplength=500, border=3, relief=RAISED, 
				justify=CENTER, borderwidth=5, padx=10, pady=10, background='green',
				foreground='black'
				)
	my_label.grid(row=0, column=0, columnspan=4)


def clearData():
	result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
	if result == 'yes':
		print('Deleted')
		#deleteAppData()
	else:
		print('Not Deleted')

def graphData():
	graphTail()



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
