

# import tkinter

from tkinter import *
import random
root = Tk(className="PyCoder")

root.geometry("1920x1080")
import random

# btn1 = Button(root,text="hello World",width=20,height=10)
# btn1.place(x=900,y=400)

for i in range(4):
	Button(root,text="Button"+str(i),width=10).place(x=random.choice([200,399,288,188]),y=i*random.choice([200,199,288,188]))

root.mainloop()
