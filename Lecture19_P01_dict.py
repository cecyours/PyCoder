
# data = [31,3,"Coder",22]
# # index : numberical
# print(data[0]) 

# non-numerical index

marks = {"python":70,
		   "java":89,
		    "php":92,
		    "C++":49}

# print(marks["python"])

# for i in marks:
# 	print("{:>10} {} ".format(i,marks[i]))

string = "{:3} | {} "

print(string.format(1,marks))
newMarks = marks.copy()
marks.clear()
print(string.format(2,marks))
marks = newMarks.copy()
print(string.format(3,marks))

keys = ("python","java")
value = 100
marks = marks.fromkeys(keys,value)
print(string.format(4,marks))

info = ["name","rollno","subject","status"]

data =  dict.fromkeys(info)
print(string.format(5,data))


marks = {"python":70,
		   "java":89,
		    "php":92,
		    "C++":49} 
print(string.format(6,marks.get("C++"))) #None if not found
print(string.format(7,marks["C++"])) # error if not found

print(string.format(8,marks.items()))
print(string.format(9,marks.keys()))
print(string.format(10,marks.values()))

marks.pop("php") #specific
print("\n",string.format(11,marks))
marks.popitem() #last one
print(string.format(12,marks))

data = {"home":"pyCoder","info":"Coins","buy":"failed"} #user not define
data.setdefault("buy","done") #ignore if defined.
# data["buy"] = "done"
print(string.format(13,data.get("buy")))
print(string.format(14,data))
data.update({"amount":40000})
print(string.format(15,data))






