
# import tkinter

from tkinter import *
import random
root = Tk(className="PyCoder")

root.geometry("1920x1080")
 
frame = Frame(root)
frame.pack()

#2x5
for rows in range(2):
	for columns in range(5):
		Button(frame,text= (str(rows))+","+(str(columns)),width=20,height=10).grid(row=rows,column=columns)


root.mainloop()
