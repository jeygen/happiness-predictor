from tkinter import *
from tkinter.font import BOLD, ITALIC
from PIL import ImageTk,Image
from dataSaver2 import deleteAppData, runSaveAppData
from grapher import graphTail

root = Tk()
root.title('Happiness Predictor')
root.iconbitmap('images/happyFace.ico')
root.geometry("800x600")

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

my_label.grid(row=0, column=0, columnspan=5)

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
	runSaveAppData()

def clearData():
	deleteAppData()

def graphData():
	#pass
	graphTail()



#button_back = Button(root, text="<<", command=back, state=DISABLED)
saveButton = Button(root, text="  Happiness  ", command=lambda: getScore())
deleteButton = Button(root, text="Delete", command=lambda: deleteAppData())
graphButton = Button(root, text="Graph", command=lambda: graphData())
button_exit = Button(root, text="Exit", command=root.quit)
#button_forward = Button(root, text=">>", command=lambda: forward(2))


#button_back.grid(row=1, column=0)
saveButton.grid(row=1, column=0)
graphButton.grid(row=1, column=2)
deleteButton.grid(row=1, column=3)
button_exit.grid(row=1, column=4)

#button_forward.grid(row=1, column=2)

root.mainloop()
