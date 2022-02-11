



# break -> exit the loops/block
# continue -> skip the after part
# return -> exit from function
# exit -> exit from the program..


name = input("Enter your name : ")
x = input("do want to exit [y/n] : ")

if x=="Y" or x=="y":
	print("Exit....")
	exit(0)

print("welcome ",name)