

#start:end:step
def display(list):
	if len(list)==0:
		return
	print(list[-1],list)
	newList = list[0:len(list)-1]
	display(newList)

data = [21,43,53,66,23,65]

display(data) 
