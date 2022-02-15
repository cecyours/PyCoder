

s = "Hello %s, i am here %s, ater %d just %.2f times."
print(s%("PyCoder","HEll",34,2.1234567890));

# step 1 : scan data from user with n args
# step 2 : calculate marks & display.


collection = []

n = int(input("Enter n size : "))

for i in range(0,n):
	userData = {"name":None,"marks":None}
	
	userData["name"] = input("Enter your name : ")
	userData["marks"] = float(input("Enter your marks : "))

	collection.append(userData);
	print();	


for i in collection:
	status = ""
	if(i["marks"]>=33):
		status = "pass"
	else:
		status = "F t APP"
		
	print("%10s | %3.2f | %10s "%(i["name"],i["marks"],status))




