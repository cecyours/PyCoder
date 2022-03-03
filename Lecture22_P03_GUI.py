


from tkinter import *
import random
root = Tk(className="PyCoder")
root.geometry("1920x1080")
root.config(bg="#138D75")

def setColor():
	root.config(bg=random.choice(["red","blue","white","black"]))

Button(root,text="Hello There",command=lambda: setColor()).pack()

root.mainloop()