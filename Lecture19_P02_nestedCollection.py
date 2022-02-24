

student = {"name":None,
			"rollno":None,
			"marks":{"python":None,"java":None,"php":None},
			"status":None}


student["name"] = input("Enter your name : ")
student["rollno"] = int(input("Enter your rollno : "))
student["marks"]["python"] = float(input("Enter python marks : ")) 
student["marks"]["java"] = float(input("Enter java marks : ")) 
student["marks"]["php"] = float(input("Enter php marks : ")) 


x = min(student["marks"].values())
if x>33:
	student["status"]="pass"
else:
	student["status"]="better luck next time"


for i in student:
	print("{:>10}  : {}".format(i,student[i]))


