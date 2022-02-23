'''
	IDE ? Framework ? 
	Programming : which generate executable, c,c++,java,python
		-> 
	Scripting : Just output without executable file
		-> php,javascript,
	markup : structure
		-> html, Markup, xml
'''
data = ["java","php","python","Ruby","php"]
print("1 ",data)

myList = data.copy()  #create backup
 
data.append("Html") # insert at last
print("2 ",data)

myList = data.copy()  #create backup
 
data.clear() # clear the list
print("3 ",data)

data = myList.copy() #restore
print("4 ",data)

x = data.count("php") # count the number of elements
print("5 ","count : ",x)

code = ["C","C++","Kotlin"]
print("6 ",code)
print("7 ",data)

data.extend(code) # data = data+code
print("8 ",data)

x = None
try: 
	req = input("data to search : ")
	x = data.index(req.lower())
except:
	print("There is no data...")
print("9 ",x)

data.insert(2,"VB.NET")
print("10 ",data)

data.pop() # remove last element
print("11 ",data)

data.pop(2) # remove 2nd index element
print("12 ",data)

data.remove("php")
print("13 ",data)

data.reverse()
print("14 ",data)

data.sort()
print("15 ",data)


