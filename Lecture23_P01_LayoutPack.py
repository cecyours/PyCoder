
# import tkinter

from tkinter import *
import random
root = Tk(className="PyCoder")

root.geometry("1920x1080")

clrlist = ["red","blue","yellow","#747284","#32ff32"]
for i in range(0,10):
	clr = random.choice(clrlist)
	fb = random.choice(clrlist)
	Button(root,text="Button "+str(i+1),width=20,height=20,bg=clr,fg=fb).pack(side=LEFT,padx=10)

root.mainloop()
