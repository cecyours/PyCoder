

from tkinter import *

root = Tk(className="PyCoder")
root.geometry("700x350") # widthxheight
root.config(bg="#000050")

frame = Frame(root,width="200",height="324",bg="#000050")
frame.place(x=100,y=10)


lblName = Label(frame,text="Enter your name : ")
lblName.grid(row=0,column=0,pady=5);

txtName = Entry(frame)
txtName.grid(row=0,column=1,pady=5)

lblPass = Label(frame,text="enter password : ")
lblPass.grid(row=1,column=0)

txtPass = Entry(frame,show='☻')
txtPass.grid(row=1,column=1)

lblMsg = Label(root,text="404", font=("Cooper",48),bg="#000050",fg="#DCDCDC")
lblMsg.place(x=100,y=200)

def work(): # call when btnLogin clicked..
	name = txtName.get();
	password = txtPass.get()

	if(name=="PyCoder" and password=="PyCoder"):
		print("welcome")
		lblMsg.config(text="PyCoder")
	else:
		print("Bye Bye...")


btnLogin = Button(frame,text="Login",height="1",width="20",command=lambda: work())
btnLogin.grid(row=2,column=0,columnspan=2,pady=6)

root.mainloop()
